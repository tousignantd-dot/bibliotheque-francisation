#!/usr/bin/env python3
"""Azure Speech contre ElevenLabs, sur la mini-leçon qui fait le plus mal.

    python3 build/essai_azure.py

Pourquoi ce banc d'essai
------------------------
Deux chantiers ouverts du cours tiennent au même défaut d'ElevenLabs : le
modèle **devine**. Il devine la langue d'un mot nu — d'où `voix.py` et son
`previous_text` — et il devine le débit, qu'on ne peut donc corriger qu'après
coup, au `atempo`, avec un facteur mesuré voix par voix et palier par palier.
Les deux corrections sont des rattrapages, et aucune n'est reproductible : la
même requête ne redonne pas le même son.

Azure ne devine pas : le SSML **dit**. `<prosody rate="-20%">` fixe le débit à
la synthèse, `<say-as interpret-as="characters">` force les lettres à sortir
en français. Si ça tient, `ralentir_dialogues.py`, `mesurer_debits.py` et le
contexte de `voix.py` deviennent tous sans objet — et le caractère coûte 16 $
le million au lieu de ~200 $.

Le cobaye est `prAlpha` (« Épeler son nom », module-n1-presenter) : c'est la
mini-leçon qui cumule les lettres nues et le besoin de lenteur. Si Azure passe
là, il passe partout.

Ce que le script produit
------------------------
Quatre blocs dans `~/Claude/generations/essai-azure`, plus une page
`comparer.html` qui les met côte à côte :

1. **épellation** — trois traitements du même « A, M, I, N, A. Amina. » :
   le texte brut, `say-as`, et les lettres séparées par des `break`. C'est le
   bloc décisif : si `say-as` sort en français à tout coup, le problème des
   lettres est réglé pour de bon.
2. **ralenti** — la même phrase à 0 %, −20 % et −35 %, avec les c/s mesurés.
   À comparer au 0,85 appliqué aujourd'hui à l'enseignante.
3. **voix** — Sylvie et Antoine sur le même extrait. Il y a quatre voix fr-CA
   chez Azure contre une douzaine chez ElevenLabs : c'est la vraie perte, et
   elle s'entend ici.
4. **mots nus** — les mots sur lesquels la langue a déjà basculé
   (`voix.MOTS_DIFFICILES`), sans aucun contexte. ElevenLabs a besoin de
   `previous_text` pour les tenir ; Azure ne devrait pas en avoir besoin.

Il faut une clé
---------------
Aucune clé Azure n'est dans `.env`. Le palier gratuit (F0) donne 500 000
caractères par mois, soit largement de quoi faire cet essai — et une bonne
part de la production. Poser dans `~/Claude/.env` :

    AZURE_SPEECH_KEY=...
    AZURE_SPEECH_REGION=canadacentral

La région doit être celle de la ressource, et le 401 qu'on récolte sinon ne
dit pas que c'est la cause. À noter pour la prochaine ressource : un
abonnement **Azure for Students** refuse la plupart des régions par politique
(`RequestDisallowedByAzure`) — `eastus` est bloquée, `canadacentral` passe.
"""
import html
import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from page_ecoute import page
from voix import MOTS_DIFFICILES                      # noqa: E402

SORTIE = pathlib.Path.home() / "Claude" / "generations" / "essai-azure"

# Les quatre voix fr-CA d'Azure. Sylvie et Jean sont les plus anciennes et les
# plus posées ; Antoine et Thierry, plus récentes, articulent davantage.
VOIX = {
    "sylvie":  "fr-CA-SylvieNeural",     # féminine — candidate « enseignante »
    "antoine": "fr-CA-AntoineNeural",    # masculin
    "jean":    "fr-CA-JeanNeural",       # masculin
    "thierry": "fr-CA-ThierryNeural",    # masculin
}

# Les paliers de la barre de vitesse de l'élève : 1,0 / 0,8 / 0,65. En SSML on
# les exprime en pourcentage relatif, ce qui n'est pas la même échelle qu'un
# `atempo` mais vise le même résultat à l'oreille.
PALIERS = [("normal", "+0%"), ("lent", "-20%"), ("tres-lent", "-35%")]

PHRASE = ("Au centre, à la clinique, à la banque. "
          "On vous demandera d'épeler votre nom, lettre par lettre.")

EN_TETE = ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
           'xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="fr-CA">')


def ssml(corps, voix, rate=None):
    """Un document SSML complet autour d'un fragment déjà balisé."""
    if rate:
        corps = '<prosody rate="%s">%s</prosody>' % (rate, corps)
    return '%s<voice name="%s">%s</voice></speak>' % (EN_TETE, VOIX[voix], corps)


def epeler_sayas(mot):
    """Les lettres par `say-as`, puis le mot entier — comme la leçon le dit.

    `interpret-as="characters"` est l'alias Azure de `spell-out`. La balise
    hérite du `xml:lang` du document, donc du fr-CA : c'est exactement ce qui
    manque à ElevenLabs, où la lettre nue n'a aucune marque de langue et
    ressort à l'anglaise une fois sur trois.
    """
    return ('<say-as interpret-as="characters">%s</say-as>'
            '<break time="400ms"/>%s.' % (mot.upper(), mot.capitalize()))


def epeler_pauses(mot):
    """Les lettres à la main, séparées par des silences.

    Le repli si `say-as` déçoit : on garde la maîtrise de la pause, que la
    leçon réclame explicitement (« Faites une pause entre chaque lettre »),
    mais on retombe sur la lettre nue et son ambiguïté de langue.
    """
    lettres = '<break time="280ms"/>'.join(l for l in mot.upper())
    return '%s<break time="400ms"/>%s.' % (lettres, mot.capitalize())


def cle_et_region():
    env = pathlib.Path.home() / "Claude" / ".env"
    vals = {}
    if env.exists():
        for ligne in env.read_text().splitlines():
            if "=" in ligne and not ligne.lstrip().startswith("#"):
                k, v = ligne.split("=", 1)
                vals[k.strip()] = v.strip()
    cle = os.environ.get("AZURE_SPEECH_KEY") or vals.get("AZURE_SPEECH_KEY")
    reg = (os.environ.get("AZURE_SPEECH_REGION")
           or vals.get("AZURE_SPEECH_REGION") or "canadacentral")
    return cle, reg


def synthese(doc, cle, region, dest):
    """Un POST, un MP3. Renvoie la durée en secondes, ou lève."""
    req = urllib.request.Request(
        "https://%s.tts.speech.microsoft.com/cognitiveservices/v1" % region,
        data=doc.encode("utf-8"),
        headers={
            "Ocp-Apim-Subscription-Key": cle,
            "Content-Type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "audio-24khz-160kbitrate-mono-mp3",
            "User-Agent": "essai-azure-francisation",
        },
        method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        dest.write_bytes(r.read())
    return duree(dest)


def duree(chemin):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nw=1:nk=1", str(chemin)],
        capture_output=True, text=True)
    try:
        return float(out.stdout.strip())
    except ValueError:
        return 0.0


def plan():
    """La liste des extraits à produire : (bloc, nom, texte lisible, ssml)."""
    p = []

    # 1. Épellation — le bloc décisif.
    for mot in ("Amina", "Tremblay", "Benali"):
        brut = "%s. %s." % (", ".join(mot.upper()), mot.capitalize())
        p.append(("epellation", "%s-brut" % mot.lower(), brut,
                  ssml(html.escape(brut), "sylvie", "-20%")))
        p.append(("epellation", "%s-sayas" % mot.lower(),
                  "say-as characters + le mot",
                  ssml(epeler_sayas(mot), "sylvie", "-20%")))
        p.append(("epellation", "%s-pauses" % mot.lower(),
                  "lettres séparées par des break",
                  ssml(epeler_pauses(mot), "sylvie", "-20%")))

    # 2. Ralenti — la même phrase aux trois paliers de la barre de vitesse.
    for nom, rate in PALIERS:
        p.append(("ralenti", "phrase-%s" % nom, "%s  (%s)" % (PHRASE, rate),
                  ssml(html.escape(PHRASE), "sylvie", rate)))

    # 3. Voix — le même extrait par les quatre, pour juger le timbre.
    for v in VOIX:
        p.append(("voix", "phrase-%s" % v, "%s  [%s]" % (PHRASE, VOIX[v]),
                  ssml(html.escape(PHRASE), v, "-20%")))

    # 4. Mots nus — sans contexte, là où ElevenLabs bascule de langue.
    for mot in MOTS_DIFFICILES:
        p.append(("mots-nus", mot, mot, ssml(html.escape(mot), "sylvie", "-20%")))

    return p


def main():
    cle, region = cle_et_region()
    travaux = plan()
    cars = sum(len(t[2]) for t in travaux)
    print("%d extraits, ~%d caractères (%.4f $ à 16 $/M)"
          % (len(travaux), cars, cars * 16 / 1_000_000))
    if not cle:
        print("\nAZURE_SPEECH_KEY absente de ~/Claude/.env — rien n'a été appelé.")
        print("Palier gratuit F0 : 500 000 caractères/mois, cet essai en use", cars)
        SORTIE.mkdir(parents=True, exist_ok=True)
        (SORTIE / "requetes.json").write_text(json.dumps(
            [{"bloc": b, "nom": n, "texte": t, "ssml": s}
             for b, n, t, s in travaux], ensure_ascii=False, indent=1))
        print("Les %d documents SSML sont écrits dans %s/requetes.json."
              % (len(travaux), SORTIE))
        return 1

    SORTIE.mkdir(parents=True, exist_ok=True)
    resultats = []
    for bloc, nom, texte, doc in travaux:
        f = SORTIE / ("%s--%s.mp3" % (bloc, nom))
        try:
            d = synthese(doc, cle, region, f)
        except urllib.error.HTTPError as e:
            print("  %-28s HTTP %s %s" % (nom, e.code, e.read().decode()[:200]))
            if e.code in (401, 403):
                print("\n401/403 : la clé ou la région ne correspond pas à la "
                      "ressource. Région essayée : %s" % region)
                return 1
            continue
        resultats.append({"bloc": bloc, "nom": nom, "texte": texte,
                          "affiche": texte, "fichier": f.name, "duree": d})
        print("  %-28s %5.2f s" % (nom, d))
    (SORTIE / "comparer.html").write_text(page(
        resultats, "Azure Speech — voix fr-CA",
        "Mini-leçon <b>prAlpha « Épeler son nom »</b>. Le bloc "
        "<b>épellation</b> compare trois traitements du même nom : texte brut, "
        "<code>say-as</code>, et lettres séparées par des <code>break</code>.",
        ("voix", "epellation", "ralenti", "mots-nus"), cle="banc-azure"))
    print("\n%d fichiers dans %s" % (len(resultats), SORTIE))
    print("Ouvrir %s/comparer.html" % SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
