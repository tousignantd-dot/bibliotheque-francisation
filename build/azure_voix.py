#!/usr/bin/env python3
"""La synthèse vocale du cours, chez Azure — le socle des générateurs.

    from azure_voix import parle, PALIERS

    parle("Bonjour, je m'appelle Sylvie.", "enseignante", chemin)
    parle("A, M, I, N, A.", "enseignante", chemin, epeler="Amina")

Pourquoi Azure et non ElevenLabs
--------------------------------
Décidé le 26 août 2026, après avoir mesuré les trois candidats. Ce qui a
tranché n'est pas le prix — quoique ~17 $ contre 160-180 $ pour le reste du
cours — mais le fait qu'**Azure obéit à un nombre plutôt qu'à une intention**.

    <prosody rate="-20%">   →  0,80 fois la durée, à la milliseconde près
    « lis lentement »       →  entre 0,72 et 0,53 selon le tirage

Trois tirages du même SSML donnent 8,712 s, 8,712 s, 8,712 s. Trois tirages de
la même consigne chez Gemini donnaient 15,5 à 20,4 s. Toute la machinerie de
rattrapage du dépôt — `voix.py` et son `previous_text`, `ralentir_dialogues`,
`mesurer_debits`, le registre `.audio-ralentis.json` — existait pour compenser
une synthèse qui devinait. Elle n'a plus d'objet.

Le trou : une seule voix féminine
---------------------------------
Azure ne publie qu'une voix féminine en fr-CA (Sylvie) contre trois masculines,
alors que le dépôt en emploie deux. Les faire lire par la même voix rendrait
inintelligibles les dialogues où deux femmes se répondent — l'élève n'a que le
timbre pour savoir qui parle.

La parade est `<prosody pitch>` : `feminin_2` est Sylvie descendue de 7 % et
légèrement ralentie. Ce n'est pas une seconde comédienne, c'est la même voix
placée plus bas, et **il faut l'avoir écoutée avant de produire quoi que ce
soit** — `python3 build/azure_voix.py --essai` fait entendre les deux à la
suite dans un échange. Si elles ne se distinguent pas, il faudra confier
`feminin_2` à une voix masculine et réécrire les personnages concernés, ce qui
est un travail de contenu et non de code.

La variante DragonHD de Sylvie n'est **pas** une solution : c'est un meilleur
modèle de la même comédienne, donc le même timbre.
"""
import html
import json
import pathlib
import re
import subprocess

RACINE = pathlib.Path(__file__).resolve().parent.parent

# Les quatre rôles du dépôt, tels qu'ils vivent dans les `generer_audio_*.py`,
# et ce qu'Azure leur donne. `pitch` et `rate` ne servent qu'à écarter les deux
# féminines ; les masculines sont des voix distinctes et n'ont besoin de rien.
VOIX = {
    "enseignante": {"azure": "fr-CA-SylvieNeural"},
    "feminin_2":   {"azure": "fr-CA-SylvieNeural", "pitch": "-7%",
                    "rate": "-4%"},
    "masculin_1":  {"azure": "fr-CA-AntoineNeural"},
    "narrateur":   {"azure": "fr-CA-JeanNeural"},
    # Thierry reste libre : c'est la voix de secours pour un personnage
    # masculin de plus dans un même dialogue.
    "masculin_3":  {"azure": "fr-CA-ThierryNeural"},
}

# Les identifiants ElevenLabs rencontrés dans les 110 générateurs, et le rôle
# qu'ils tenaient. C'est cette table qui permet de convertir un générateur sans
# relire son dialogue.
DEPUIS_ELEVENLABS = {
    "mActWQg9kibLro6Z2ouY": "enseignante",   # 36 générateurs
    "WW0JfNPk5DgcQdM0d6X6": "feminin_2",     # 27
    "IPgYtHTNLjC7Bq7IPHrm": "narrateur",     # 27
    "93nuHbke4dTER9x2pDwE": "masculin_1",    # 26
    "K7gx0ylJdff0yjM2uVQS": "enseignante",   # ancien identifiant, essai_debit
    "rCmVtv8cYU60uhlsOo1M": "masculin_3",    # 3, rare
}

# Les paliers de la barre de vitesse de l'élève. Mesurés le 26 août 2026 :
# `-20%` rend 0,80 fois la durée et `-35%` en rend 0,65 — soit exactement les
# facteurs que la barre applique déjà. Rien à calibrer.
PALIERS = {"normal": None, "lent": "-20%", "tres-lent": "-35%"}

# Azure parle plus lentement qu'ElevenLabs : à texte égal, les répliques du
# module témoin sortaient **33 % plus longues** que celles en production le
# 26 août 2026. Ma première calibration ne l'avait pas vu parce qu'elle
# comparait des c/s mesurés sur des textes différents — ce qui ne vaut que si
# la densité caractères/syllabes est la même, et elle ne l'est pas.
#
# `+33%` rendrait le tempo actuel au millième. On retient `+15%` : les MP3
# d'aujourd'hui sont **déjà** le produit d'un ralentissement à 0,85, appliqué
# justement parce qu'ElevenLabs allait trop vite pour des débutants. Rendre le
# tempo exact annulerait cette intention. Le cours parlera donc 15 % plus
# lentement qu'avant, et l'élève garde sa barre de vitesse par-dessus.
TAUX_GLOBAL = "+15%"

# Azure pose ~0,19 s de silence en tête et en queue là où ElevenLabs n'en
# mettait pas. Sur une phrase c'est imperceptible ; sur une lettre seule du
# banc d'alphabet, ça double la durée du fichier. On rogne — sans appel d'API,
# donc sans coût, et avec une marge pour ne jamais mordre sur la parole.
MARGE_ROGNAGE_S = 0.04

REGION_DEFAUT = "canadacentral"
FORMAT = "audio-24khz-160kbitrate-mono-mp3"
EN_TETE = ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
           'xml:lang="fr-CA">')


def _env():
    vals = {}
    f = pathlib.Path.home() / "Claude" / ".env"
    if f.exists():
        for ligne in f.read_text().splitlines():
            if "=" in ligne and not ligne.lstrip().startswith("#"):
                k, v = ligne.split("=", 1)
                vals[k.strip()] = v.strip()
    return vals


def cle_region():
    import os
    v = _env()
    return (os.environ.get("AZURE_SPEECH_KEY") or v.get("AZURE_SPEECH_KEY"),
            os.environ.get("AZURE_SPEECH_REGION")
            or v.get("AZURE_SPEECH_REGION") or REGION_DEFAUT)


def ssml(texte, role, palier=None, epeler=None, pause_lettres="280ms"):
    """Le document SSML d'un extrait.

    `epeler` demande les lettres une par une, séparées par un silence, puis le
    mot entier — c'est la forme que la leçon « Épeler son nom » réclame
    (« faites une pause entre chaque lettre »). On n'emploie pas
    `<say-as interpret-as="characters">`, qui enchaîne les lettres sans
    respirer : mesuré à 3,46 s contre 5,52 s pour la version à silences sur le
    même prénom. Les lettres nues ne posent pas le problème de langue qu'elles
    avaient chez ElevenLabs, le `xml:lang` du document les couvre.
    """
    v = VOIX[role]
    if epeler:
        lettres = ('<break time="%s"/>' % pause_lettres).join(epeler.upper())
        corps = '%s<break time="400ms"/>%s' % (lettres,
                                               html.escape(epeler.capitalize()))
    else:
        corps = html.escape(texte)

    # `rate` du palier et `rate` du rôle se cumulent : on les pose sur deux
    # balises imbriquées plutôt que d'additionner des pourcentages, qui ne
    # s'additionnent pas linéairement.
    taux = PALIERS.get(palier) if palier else None
    if v.get("pitch") or v.get("rate"):
        attrs = "".join(' %s="%s"' % (k, v[k]) for k in ("pitch", "rate")
                        if v.get(k))
        corps = "<prosody%s>%s</prosody>" % (attrs, corps)
    if taux:
        corps = '<prosody rate="%s">%s</prosody>' % (taux, corps)
    # Le taux global enveloppe tout le reste : c'est le débit de référence du
    # cours, sur lequel palier et rôle viennent se composer.
    if TAUX_GLOBAL:
        corps = '<prosody rate="%s">%s</prosody>' % (TAUX_GLOBAL, corps)
    return '%s<voice name="%s">%s</voice></speak>' % (EN_TETE, v["azure"], corps)


def parle(texte, role, dest, palier=None, epeler=None, cle=None, region=None):
    """Synthétise un extrait dans `dest`. Renvoie sa durée en secondes.

    Les appels passent par `curl` et non `urllib` : sur le poste, `urllib` se
    bloque indéfiniment sur ces hôtes — dix minutes sans un octet, constaté le
    26 août 2026. Le corps transite par un fichier pour ne pas dépendre de la
    longueur d'argv sur les longs dialogues.
    """
    if cle is None:
        cle, region_env = cle_region()
        region = region or region_env
    if not cle:
        raise RuntimeError("AZURE_SPEECH_KEY absente de ~/Claude/.env")
    dest = pathlib.Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    doc = dest.with_suffix(".ssml.xml")
    doc.write_text(ssml(texte, role, palier, epeler), encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST",
         "-H", "Ocp-Apim-Subscription-Key: %s" % cle,
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: %s" % FORMAT,
         "-H", "User-Agent: francisation",
         "--data-binary", "@%s" % doc, "-o", str(dest),
         "-w", "%{http_code}",
         "https://%s.tts.speech.microsoft.com/cognitiveservices/v1" % region],
        capture_output=True, text=True, check=True)
    doc.unlink()
    code = out.stdout.strip()
    if code != "200":
        detail = dest.read_text(errors="replace")[:200] if dest.exists() else ""
        dest.unlink(missing_ok=True)
        # Le 401 d'une région qui ne correspond pas à la clé ne dit pas que
        # c'est la cause — d'où le rappel explicite.
        indice = (" — la région « %s » ne correspond peut-être pas à la "
                  "ressource" % region) if code == "401" else ""
        raise RuntimeError("HTTP %s%s %s" % (code, indice, detail))
    return rogner_silences(dest)


def rogner_silences(chemin, marge=None):
    """Retire le silence de tête et de queue, en gardant `marge` seconde.

    On ne se sert pas de `silenceremove`, qui coupe au ras de la parole et
    mange les plosives d'attaque — un « P » ou un « T » initial perd son
    explosion et le mot n'est plus le modèle qu'on voulait faire imiter. On
    repère les bornes et on coupe avec une marge.

    Les silences **internes** ne sont jamais touchés : une épellation est faite
    de pauses voulues. Le repérage est délégué à `garde_debit.bornes_parole`,
    qui porte la seule règle correcte — voir sa docstring, le rognage a
    d'abord été aléatoire.
    """
    import sys as _s
    _s.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from garde_debit import bornes_parole
    marge = MARGE_ROGNAGE_S if marge is None else marge
    chemin = pathlib.Path(chemin)
    totale = duree(chemin)
    if totale <= 0:
        return 0.0
    d, f = bornes_parole(chemin, totale)
    d = max(0.0, d - marge)
    f = min(totale, f + marge)
    if f - d < 0.15 or (d < 0.01 and f > totale - 0.01):
        return totale                      # rien à gagner, on ne réencode pas
    tmp = chemin.with_suffix(".rogne.mp3")
    subprocess.run(
        ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", str(chemin),
         "-ss", "%.3f" % d, "-to", "%.3f" % f, "-b:a", "160k", str(tmp)],
        check=True, capture_output=True)
    tmp.replace(chemin)
    return duree(chemin)


def duree(chemin):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(chemin)],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


# --- Couche de compatibilité avec les 110 générateurs ------------------------
#
# Les générateurs définissent tous la même fonction locale :
#
#     parle(cle, texte, voix, chemin, avant=None, apres=None)  -> bool
#
# où `voix` est un identifiant ElevenLabs. Plutôt que de réécrire 110 corps de
# fonction, chacun avec ses particularités, on offre ici la **même signature**
# et la migration se réduit à remplacer la définition par une délégation.
#
# `avant` et `apres` sont acceptés et **ignorés** : c'était le contexte français
# de `voix.py`, destiné à empêcher un mot nu de sortir à l'anglaise. Le
# `xml:lang="fr-CA"` du document SSML le fait désormais sans rien coûter.
#
# `cle` est ignorée aussi : c'était la clé ElevenLabs, lue de l'environnement
# par chaque générateur. On garde le paramètre pour que les appels existants
# continuent de compiler.

ESSAIS = 4
ATTENTE_BASE_S = 4       # doublée à chaque échec : 4, 8, 16 s

# Les codes qui valent une reprise. Un 401 (clé ou région) ou un 400 (SSML
# malformé) sont des erreurs à nous : insister ne ferait que les répéter.
TRANSITOIRES = {408, 429, 500, 502, 503, 504}


def parle_compat(cle, texte, voix, chemin, avant=None, apres=None,
                 palier=None, epeler=None):
    """La signature des générateurs, servie par Azure. Renvoie True/False.

    Ne lève pas : les générateurs attendent un booléen et tiennent leur propre
    compte des échecs, souvent au milieu d'une série de deux cents extraits.
    """
    import time
    role = DEPUIS_ELEVENLABS.get(voix, voix)
    if role not in VOIX:
        print("   ❌ voix inconnue : %s" % voix)
        return False
    chemin = pathlib.Path(chemin)
    for essai in range(1, ESSAIS + 1):
        try:
            parle(texte, role, chemin, palier=palier, epeler=epeler)
            return True
        except RuntimeError as e:
            msg = str(e)
            code = re.match(r"HTTP (\d+)", msg)
            recuperable = code and int(code.group(1)) in TRANSITOIRES
            if not recuperable or essai == ESSAIS:
                print("   ❌ %s" % msg[:160])
                return False
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print("⏳%ds" % attente, end="", flush=True)
            time.sleep(attente)
        except subprocess.CalledProcessError as e:
            if essai == ESSAIS:
                print("   ❌ curl : %s" % e)
                return False
            time.sleep(ATTENTE_BASE_S * (2 ** (essai - 1)))
    return False


def _essai():
    """Un échange entre les deux féminines, pour juger si on les distingue."""
    sortie = pathlib.Path.home() / "Claude" / "generations" / "essai-azure-voix"
    sortie.mkdir(parents=True, exist_ok=True)
    echange = [
        ("enseignante", "Bonjour ! Vous venez pour l'inscription ?"),
        ("feminin_2",   "Oui, bonjour. C'est ici, le cours de français ?"),
        ("enseignante", "C'est ici. Vous avez une pièce d'identité ?"),
        ("feminin_2",   "J'ai mon passeport. Est-ce que ça va ?"),
        ("enseignante", "Parfait. Pouvez-vous épeler votre nom, s'il vous plaît ?"),
        ("feminin_2",   "Oui. B, E, N, A, L, I. Benali."),
    ]
    print("Deux voix féminines — les distingue-t-on ?\n")
    for i, (role, txt) in enumerate(echange, 1):
        f = sortie / ("echange-%d-%s.mp3" % (i, role))
        d = parle(txt, role, f)
        print("  %-12s %5.2f s  %s" % (role, d, txt))
    # Les masculines, pour mémoire : elles sont distinctes par construction.
    for role in ("masculin_1", "narrateur", "masculin_3"):
        f = sortie / ("temoin-%s.mp3" % role)
        d = parle("Bonjour, je vous écoute. Asseyez-vous, je vous en prie.",
                  role, f)
        print("  %-12s %5.2f s  (témoin, %s)" % (role, d, VOIX[role]["azure"]))
    print("\nFichiers dans %s" % sortie)
    print("Écouter echange-1 à 6 dans l'ordre : si les deux femmes se")
    print("confondent, `feminin_2` doit changer de voix et non de hauteur.")
    return 0


if __name__ == "__main__":
    import sys
    if "--essai" in sys.argv:
        sys.exit(_essai())
    print(__doc__.strip().split("\n\n")[0])
    print("\n  python3 build/azure_voix.py --essai")
    sys.exit(2)
