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

    # Les deux rôles du JEU DE RÔLE, et eux seuls. Ils se synthétisent en
    # direct, réplique par réplique : rien à régénérer, donc rien qui touche
    # au gel des MP3. D'où le modèle DragonHD — même comédienne, mais la
    # prosodie s'y calcule sur la phrase entière au lieu d'être plate. Écouté
    # le 31 août 2026 (essais/essai-jeu-de-role.html) : c'est le seul remède,
    # aucune voix fr-CA d'Azure n'accepte de style expressif.
    #
    # `reference: ""` coupe le TAUX_GLOBAL du cours. Le +15% a été calibré sur
    # les voix neurales pour rattraper le tempo d'ElevenLabs ; sur HD il rend
    # une parole pressée, et c'est la version SANS lui qui a été retenue à
    # l'écoute. Le ralenti passe par le palier, donc par la barre de débit.
    # Les mêmes voix HD, pour les DIALOGUES des modules. Nommées à part des
    # rôles du jeu de rôle : ce n'est pas le même usage, et un jour l'un des
    # deux changera sans l'autre. Réservées aux dialogues où un seul
    # personnage de chaque genre parle — le français canadien n'a que ces
    # deux voix HD, et deux personnages du même genre s'y confondraient.
    "hd_feminin":  {"azure": "fr-CA-Sylvie:DragonHDLatestNeural", "reference": ""},
    "hd_masculin": {"azure": "fr-CA-Thierry:DragonHDLatestNeural", "reference": ""},

    "jr_feminin":  {"azure": "fr-CA-Sylvie:DragonHDLatestNeural", "reference": ""},
    "jr_masculin": {"azure": "fr-CA-Thierry:DragonHDLatestNeural", "reference": ""},
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

# Les mots isolés et les mini-leçons ont besoin d'un taux à eux. Mesuré le
# 27 août 2026 : `+15%` rend le tempo des **dialogues** au centième (×1,02),
# mais sur les mots et les phrases de mini-leçon il donne ×0,85 — 15 % plus
# rapide qu'avant, et c'est trop. Les deux familles n'ont pas la même densité :
# une phrase de dialogue et un mot nu ne se prononcent pas au même rythme, et
# un taux unique ne peut convenir aux deux.
#
# `-10%` place la famille des sons **plus lentement qu'ElevenLabs**, ce qui est
# voulu : un mot que l'élève doit imiter gagne à être plus posé que la parole
# courante. C'est là que le cours sert de modèle.
TAUX_SONS = "-10%"


# --- L'échelle de débit par niveau -------------------------------------------
#
# Décidée le 29 août 2026, après la mesure des 5 936 répliques
# (`build/debit_par_voix.py`). Le constat qui l'a imposée : à `+15%`, un module
# Azure tourne à ~25 c/s **quel que soit son niveau**, et 20 % plus vite que
# son voisin resté chez ElevenLabs. La progression apparente 18 → 25 c/s du
# niveau 1 au niveau 8 n'était pas une conception pédagogique, seulement la
# proportion de modules déjà migrés, qui montait avec le niveau parce que les
# niveaux hauts avaient été produits plus tard.
#
# Le débit se déduit linéairement du taux : à `+15%` on mesure 25,2 c/s, donc
# viser T revient à poser `1 + r = 1,15 × T / 25,2`. D'où :
#
#     niveaux 1-2  →  18 c/s  →  -18%
#     niveaux 3-4  →  20 c/s  →   -9%
#     niveaux 5-6  →  22 c/s  →    0%
#     niveaux 7-8  →  24 c/s  →  +10%
#
# Le naturel de la voix s'écrit `""`, **jamais `None`** : dans `ssml()`,
# `reference is None` veut dire « prends la valeur par défaut » et retombe sur
# TAUX_GLOBAL. Le banc d'essai du 29 août l'a pris sur le fait — les niveaux 5
# et 6 ressortaient à 26,2 c/s, exactement comme à `+15%`, sans que rien ne le
# signale. La chaîne vide, elle, est fausse au test de vérité : aucune balise
# `<prosody>` n'est posée.
ECHELLE_NIVEAU = {1: "-18%", 2: "-18%", 3: "-9%", 4: "-9%",
                  5: "",     6: "",     7: "+10%", 8: "+10%"}


def niveau(chemin):
    """Le niveau du module auquel appartient ce fichier, ou None.

    Se lit sur le chemin — `assets/interactive/<slug>/<bloc>/line_NN.mp3` —
    comme `famille()` se lit sur le nom. Même raison : les 110 générateurs ne
    le disent pas, et les rouvrir coûterait plus que ça ne rapporterait.
    """
    try:
        parties = pathlib.Path(chemin).resolve().parts
        i = parties.index("interactive")
        slug = parties[i + 1]
    except (ValueError, IndexError):
        return None
    import sys as _s
    _s.path.insert(0, str(RACINE / "build" / "powerpoints"))
    try:
        from modules import MODULES
    except ImportError:
        return None
    return MODULES.get(slug, {}).get("niveau")


def taux_dialogue(chemin):
    """Le taux à poser sur une réplique, d'après le niveau de son module.

    Un module hors registre — un atelier, un module neuf pas encore inscrit —
    retombe sur `TAUX_GLOBAL`, qui reste la valeur par défaut du dépôt.
    """
    n = niveau(chemin)
    if not n or n not in ECHELLE_NIVEAU:
        return TAUX_GLOBAL
    return ECHELLE_NIVEAU[n]


def famille(chemin):
    """« dialogue » ou « sons », d'après le nom du fichier.

    Les générateurs ne disent pas à quelle famille appartient un extrait, et
    rouvrir les cent dix pour l'ajouter coûterait plus cher que ça ne
    rapporterait. La règle se lit donc sur le nom : `line_NN_perso.mp3` est une
    réplique, tout le reste appartient à la famille enseignante — mots,
    phrases, mini-leçons, bancs de vocabulaire.

    C'est implicite, et c'est le prix à payer. La convention `line_*` est tenue
    par les 110 générateurs sans exception : elle a servi à vérifier, fichier
    par fichier, qu'aucune réplique n'avait basculé pendant la migration.
    """
    return "dialogue" if pathlib.Path(chemin).name.startswith("line_") else "sons"

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


# --- Lexique de prononciation ------------------------------------------------
#
# Décidé le 29 août 2026, après l'écoute des niveaux 1 et 2. Azure lit
# correctement le français courant, mais bute sur trois familles : les sigles
# qu'il épelle au lieu de les dire, les noms propres dont il prononce la
# consonne finale, et les lettres isolées, qu'il bascule en anglais.
#
# La correction passe par `<sub alias>` : le texte **affiché à l'élève** ne
# change pas, seul ce qui est envoyé à la synthèse est réécrit. C'est ce qui
# permet de garder « NIP » au tableau et d'entendre « nip ».
#
# Règle de sûreté : **jamais de substitution sur un mot du français courant.**
# « point » revient dans 39 répliques de 17 modules, presque toujours au sens
# ordinaire (« point de service ») — il est donc traité par PHRASES, sur son
# contexte exact, et non par LEXIQUE.

LEXIQUE = {                      # mot entier → ce que la voix doit dire
    "NIP": "nipe",               # entendu « ni-pé » ou « enne-i-pé »
    "Pelchat": "Pelcha",         # le t final ne se prononce pas
}

PHRASES = {                      # suite exacte → sa lecture, contexte compris
    "a v point": "a vé point",           # l'abréviation « av. » épelée
    "a p p point": "a pé pé point",       # « app. »
    "T é l point": "té é elle point",     # « tél. »
}

# Les numéros civiques se disent par groupes de deux au Québec : le 3120 est
# « trente et un vingt », jamais « trois mille cent vingt ». Seuls les nombres
# **suivis d'une voie** sont concernés — sept dans tout le cours. Les numéros
# de local, de téléphone et les années gardent leur lecture ordinaire.
ADRESSES = {
    "2140": "vingt et un quarante",
    "3120": "trente et un vingt",
    "3420": "trente-quatre vingt",
    "4520": "quarante-cinq vingt",
    "5680": "cinquante-six quatre-vingts",
    "7412": "soixante-quatorze douze",
}
VOIE = r"(?=,?\s*(?:rue|avenue|av\.|boulevard|boul\.|chemin|place|côte)\b)"

# Les noms français des lettres. Sans eux, une épellation part à l'anglaise :
# le Y de « Yusuf. Y - U - S - U - F. » sortait « ouaï ». La docstring de
# ssml() affirmait que le xml:lang suffisait — l'écoute l'a démentie.
LETTRES = {
    "A": "a", "B": "bé", "C": "cé", "D": "dé", "E": "eu", "F": "effe",
    "G": "gé", "H": "ache", "I": "i", "J": "ji", "K": "ka", "L": "elle",
    "M": "emme", "N": "enne", "O": "o", "P": "pé", "Q": "ku", "R": "erre",
    "S": "esse", "T": "té", "U": "u", "V": "vé", "W": "double vé",
    "X": "iks", "Y": "i grec", "Z": "zède",
    # Les majuscules accentuées épellent des noms bien réels — Traoré, café.
    # Sans elles, la suite « T-R-A-O-R-É » se coupait avant le É, qui repartait
    # tout seul et à l'anglaise.
    "É": "e accent aigu", "È": "e accent grave", "Ê": "e accent circonflexe",
    "À": "a accent grave", "Ç": "c cédille", "Ô": "o accent circonflexe",
    "Î": "i accent circonflexe", "Û": "u accent circonflexe",
}
# Une suite d'au moins deux lettres isolées : « D - A - O - U - D »,
# « P, A, P, I, N, E, A, U ». Le mot qui précède n'est pas touché.
# « ou » et « et » relient les lettres d'une liste — « P, M ou G » sur une
# étiquette de vêtement. Sans eux, le G restait dehors et sortait « djî ».
_L = "[A-ZÀÇÈÉÊÎÔÛ]"
SUITE_LETTRES = re.compile(
    r"(?:\b%s\b[ ]*(?:[-–,][ ]*|,?[ ]+(?:ou|et)[ ]+)){1,}\b%s\b" % (_L, _L))


def _sub(texte, alias):
    """La balise SSML qui fait dire `alias` là où le texte porte `texte`."""
    return '<sub alias="%s">%s</sub>' % (html.escape(alias, quote=True),
                                         html.escape(texte))


def _insiste(sortie, chemin):
    """Monte les deux temps d'une leçon sur l'accent d'insistance.

    La phrase plate, un silence, la même phrase **appuyée**. Un accent posé
    seul ne s'entend pas chez Azure ; c'est la comparaison qui le rend audible.
    Le pourquoi, les valeurs et leurs limites sont dans `build/insistance.py`.

    `sortie` est la phrase déjà échappée. Rendue telle quelle si **ce fichier**
    n'est pas dans la table, ou si le mot visé n'est plus dans la phrase — une
    leçon retouchée ne doit pas produire un fichier bancal en silence. La table
    est indexée par fichier et non par texte : la même phrase sert ailleurs
    dans des leçons où une démonstration en trois temps n'a rien à faire.
    """
    import sys as _s
    _s.path.insert(0, str(RACINE / "build"))
    try:
        from insistance import (marque, RATE, PITCH, VOLUME,
                                PAUSE_ENTRE, PAUSE_AVANT)
    except ImportError:
        return sortie
    mot = marque(chemin)
    if not mot:
        return sortie
    cible = html.escape(mot)
    if cible not in sortie:
        return sortie
    appuyee = sortie.replace(
        cible,
        '<break time="%s"/><prosody rate="%s" pitch="%s" volume="%s">%s</prosody>'
        % (PAUSE_AVANT, RATE, PITCH, VOLUME, cible), 1)
    silence = '<break time="%s"/>' % PAUSE_ENTRE
    return sortie + silence + appuyee


def prononce(texte, chemin=None):
    """Le texte, préparé pour la voix : échappé, et corrigé par le lexique.

    Rend du SSML, donc **déjà échappé** — ne pas le repasser dans html.escape.
    L'ordre compte : les suites de lettres d'abord, parce qu'elles contiennent
    des majuscules isolées qu'un lexique de mots ne doit pas voir passer.
    """
    morceaux, reste = [], texte

    def decoupe(motif, rendu):
        nonlocal morceaux, reste
        sortie, pos = [], 0
        for m in re.finditer(motif, reste):
            sortie.append((reste[pos:m.start()], rendu(m)))
            pos = m.end()
        sortie.append((reste[pos:], None))
        return sortie

    # 1. les épellations
    parts, pos = [], 0
    for m in SUITE_LETTRES.finditer(texte):
        parts.append(html.escape(texte[pos:m.start()]))
        # Ne prendre que les lettres **isolées** : « ou » et « et » relient
        # la liste, ils ne s'épellent pas. Les chercher au motif, et non par
        # isalpha(), qui rendait « pé emme o u gé » pour « P, M ou G ».
        lu = " ".join(LETTRES.get(c, c)
                      for c in re.findall(r"\b%s\b" % _L, m.group(0)))
        parts.append(_sub(m.group(0), lu))
        pos = m.end()
    parts.append(html.escape(texte[pos:]))
    out = "".join(parts)

    # 2. les phrases à contexte, puis les mots du lexique, puis les adresses.
    #    On travaille sur du texte déjà échappé : aucun de ces motifs ne
    #    contient de caractère que l'échappement aurait transformé, et les
    #    balises déjà posées ne contiennent aucun des motifs cherchés.
    for phrase, lu in PHRASES.items():
        out = out.replace(html.escape(phrase), _sub(phrase, lu))
    for mot, lu in LEXIQUE.items():
        out = re.sub(r"\b%s\b" % re.escape(html.escape(mot)),
                     lambda m, lu=lu, mot=mot: _sub(mot, lu), out)
    for num, lu in ADRESSES.items():
        out = re.sub(r"\b%s\b%s" % (num, VOIE),
                     lambda m, lu=lu, num=num: _sub(num, lu), out)
    return _insiste(out, chemin)


def ssml(texte, role, palier=None, epeler=None, pause_lettres="280ms",
         reference=None, chemin=None):
    """Le document SSML d'un extrait.

    `epeler` demande les lettres une par une, séparées par un silence, puis le
    mot entier — c'est la forme que la leçon « Épeler son nom » réclame
    (« faites une pause entre chaque lettre »). On n'emploie pas
    `<say-as interpret-as="characters">`, qui enchaîne les lettres sans
    respirer : mesuré à 3,46 s contre 5,52 s pour la version à silences sur le
    même prénom.

    Cette docstring a longtemps affirmé que « les lettres nues ne posent pas le
    problème de langue qu'elles avaient chez ElevenLabs, le `xml:lang` du
    document les couvre ». **C'est faux** : l'écoute des niveaux 1 et 2, le
    29 août 2026, a trouvé le Y de « Yusuf. Y - U - S - U - F. » dit « ouaï »
    et l'épellation de « Papineau » entièrement anglaise. Les lettres passent
    désormais par `LETTRES`, dans `prononce()`.
    """
    v = VOIX[role]
    if epeler:
        lettres = ('<break time="%s"/>' % pause_lettres).join(epeler.upper())
        corps = '%s<break time="400ms"/>%s' % (lettres,
                                               html.escape(epeler.capitalize()))
    else:
        corps = prononce(texte, chemin)

    # Les voix DragonHD (et les Multilingual) détectent la langue **mot à mot**,
    # toutes seules. C'est ce qui les rend vivantes, et c'est ce qui fait
    # basculer « entrez » à l'espagnole au milieu d'une phrase française — le
    # `xml:lang` du document n'y suffit pas. Entendu au jeu de rôle le 31 août
    # 2026, sur la première et la dernière réplique d'une visite.
    #
    # Seule parade qui porte : envelopper TOUT le corps dans <lang>. Mesuré le
    # même jour — `<lang>` autour du seul mot et `<phoneme>` rendent un fichier
    # identique à l'octet près au son non balisé, donc les voix HD les ignorent
    # purement et simplement ; `<lang>` autour de la phrase entière change le
    # son (essais/essai-entrez.html).
    #
    # Le test porte sur le NOM de la voix et non sur un drapeau de la table :
    # un rôle HD ajouté plus tard hériterait du problème sans que personne y
    # pense.
    if "DragonHD" in v["azure"] or "Multilingual" in v["azure"]:
        corps = '<lang xml:lang="fr-CA">%s</lang>' % corps

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
    # Le taux de référence enveloppe tout le reste ; palier et rôle se composent
    # par-dessus. `reference` laisse l'appelant choisir celui de sa famille ;
    # sans lui, c'est celui des dialogues.
    #
    # Ne pas nommer ce paramètre `taux` : c'est déjà le nom du taux **du
    # palier**, quelques lignes plus haut. Le collision l'écrasait, et le
    # palier se serait appliqué deux fois sans que rien ne le dise.
    # Un rôle peut porter son propre `reference` : les voix HD du jeu de rôle
    # n'ont pas à subir le taux calibré pour les voix neurales.
    if reference is None:
        reference = v.get("reference", TAUX_GLOBAL)
    if reference:
        corps = '<prosody rate="%s">%s</prosody>' % (reference, corps)
    return '%s<voice name="%s">%s</voice></speak>' % (EN_TETE, v["azure"], corps)


def parle(texte, role, dest, palier=None, epeler=None, cle=None, region=None,
          reference=None):
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
    doc.write_text(ssml(texte, role, palier, epeler, reference=reference,
                        chemin=dest), encoding="utf-8")
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
            # La famille se décide ici et nulle part ailleurs : les 110
            # générateurs passent tous par cette porte.
            ref = (TAUX_SONS if famille(chemin) == "sons"
                   else taux_dialogue(chemin))
            parle(texte, role, chemin, palier=palier, epeler=epeler,
                  reference=ref)
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
