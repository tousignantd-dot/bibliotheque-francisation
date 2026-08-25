#!/usr/bin/env python3
"""Ralentissement des voix trop rapides pour le niveau qu'elles servent.

Les quatre voix du dépôt sont ralenties après coup : la narration selon sa
propre règle, les trois voix de dialogue selon celle de leur niveau.

**La voix « enseignante »** (`mActWQg9kibLro6Z2ouY`) narre les mini-leçons et
les mots isolés de presque tous les modules, en plus de rôles de dialogue :
c'est la voix que l'élève entend le plus, et c'est donc celle dont le débit
compte le plus. Elle a changé le 23 août 2026. L'ancienne
(`K7gx0ylJdff0yjM2uVQS`) est abandonnée : mesurée sur une même phrase contre
les trois autres du dépôt, elle sortait à 20,8 caractères par seconde quand
les autres tenaient 18 à 19 — la plus rapide des quatre, et ralentie à 0,85
elle restait au niveau des autres non ralenties. La remplaçante débite 17,7
c/s sans aucun traitement, soit exactement ce que l'ancienne donnait *après*
`atempo` — et ralentie à son tour, elle descend à 15,1. Le facteur reste donc
appliqué, mais il part de plus bas. Ne pas revenir à l'ancienne : la plainte
portait sur elle, y compris ralentie.

**Les trois voix de dialogue** — féminine #2 (`WW0JfNPk5DgcQdM0d6X6`),
masculin #1 (`93nuHbke4dTER9x2pDwE`), narrateur (`IPgYtHTNLjC7Bq7IPHrm`) — ont
été prises le 25 août 2026, en deux temps et pour une seule raison.

La féminine #2 est venue la première. Elle ne narre rien, elle ne fait que du
dialogue, et elle y était la plus rapide des quatre : 16,5 à 16,9 c/s aux
quatre modules de niveau 1, là où l'enseignante ralentie tenait 11,9-12,3 —
près de 40 % plus vite que sa partenaire, **dans le même dialogue**. Trois
choses aggravaient le cas au niveau 1 : le contraste est immédiat, c'est la
voix du personnage-élève (celui à qui l'apprenant s'identifie, et celui qui a
le plus de répliques), et les répliques y sont si courtes que le silence de
tête et de queue *abaisse* le c/s mesuré — la parole elle-même était encore
plus rapide que le chiffre.

La traiter seule n'a fait que déplacer le problème d'un cran : les deux voix
masculines, jusque-là dans la fourchette, sont devenues à leur tour les plus
rapides de la scène — 15,1 et 14,9 c/s aux niveaux 1-2, 17,6 et 16,7 au-delà.
Dans `module-n1-presenter`, monsieur Tremblay et Paul se sont mis à parler
plus vite qu'Amina : exactement la configuration qui avait déclenché la
plainte. La règle vaut donc pour les trois.

**Le facteur a deux moitiés : le palier et la voix.**

    facteur = palier × (débit de référence / débit propre à la voix)

Le **palier** dit ce qu'on veut de l'élève : 0,85 aux niveaux 1 et 2, 0,90 à
partir du niveau 3. Au-delà du niveau 2, un dialogue a le droit d'aller son
train ; aux deux premiers, la vitesse est le premier obstacle.

Le **rapport de débits** met les voix à égalité entre elles. Chaque voix a son
articulation propre, et un facteur unique conservait ces écarts au lieu de les
effacer. Le débit de référence est celui de l'enseignante, la voix dont le
rythme a été validé : le facteur d'une voix est celui qui l'amène au débit
qu'aurait l'enseignante au même palier.

Un facteur au-dessus de 1 serait une accélération. `facteur_pour` rend `None`
dans ce cas et laisse l'extrait tel quel : le but est de ramener les voix
rapides, jamais de presser celles qui sont déjà posées.

Comment ces débits ont été mesurés — et pourquoi pas autrement
-------------------------------------------------------------
**En caractères par seconde de parole, silences de tête et de queue retirés**
(`silenceremove` aux deux bouts, puis caractères ÷ durée restante), sur 150
répliques par voix tirées de tout le dépôt.

Les deux façons plus simples de mesurer sont fausses, toutes deux pour la même
raison, et toutes deux ont été essayées :

- **Caractères ÷ durée du fichier.** Le silence de tête et de queue vaut 0,33 à
  0,37 s quelle que soit la voix ; sur une réplique de niveau 1 qui fait deux
  secondes, c'est un sixième du fichier, sur une réplique de niveau 8 c'est un
  vingtième. Le chiffre monte donc avec la longueur du texte sans que personne
  ait parlé plus vite : l'enseignante, à facteur strictement constant, mesure
  12,4 c/s aux niveaux 1-2 et 14,8 au-delà. **Ne jamais comparer deux voix par
  ce chiffre si leurs répliques n'ont pas la même longueur** — c'est ce qui a
  fait croire, le 25 août, que la féminine #2 était 40 % plus rapide que sa
  partenaire alors que l'écart d'articulation était de 20 %.
- **Régression durée ≈ a + b × caractères.** L'idée est bonne, l'estimation ne
  tient pas : les distributions de longueur diffèrent trop d'une voix à
  l'autre, et l'ordonnée à l'origine part à 0,73 s pour l'enseignante contre
  −0,16 s pour la féminine #2 — deux valeurs que la mesure directe des
  silences dément l'une comme l'autre.

Ce que cette calibration ne peut pas faire
------------------------------------------
**L'écart entre voix est quatre fois plus petit que l'écart dans une voix.**
Les médianes d'articulation tiennent en 1,6 c/s (17,9 à 19,5) ; à l'intérieur
d'une seule voix, du p10 au p90, il y a 6,7 c/s. Le débit que rend ElevenLabs
dépend d'abord du texte et de son contexte, pas du locuteur : dans
`module-n1-classe`, Bopha articule à 18,4 c/s et Ivan à 15,3 avec la même
consigne. Un facteur par voix déplace donc toute la distribution d'une voix
sans rien faire de sa dispersion, et une réplique du p90 restera bien plus
rapide que la médiane d'à côté. Ce qui traiterait vraiment le problème est un
**plafond par réplique** — mesurer chaque extrait et ne ralentir que ceux qui
dépassent le débit visé. Ce n'est pas ce que fait ce module.

**Le niveau est déduit du chemin de sortie** — `assets/interactive/module-nX-…`
— et vaut 4 par défaut, ce qui est juste : les modules sans préfixe de niveau
sont la série de niveau 4. Les générateurs n'ont donc rien à passer et rien à
savoir ; ils appellent la même fonction qu'avant.

Le paramètre `speed` d'ElevenLabs ne corrige rien ici : avec
`eleven_multilingual_v2`, l'API renvoie le même fichier octet pour octet avec
ou sans `"speed": 0.85`. On ralentit donc après coup, avec le filtre `atempo`
de ffmpeg, qui étire la durée sans toucher à la hauteur : même timbre, débit
posé.

À appeler juste après l'écriture d'un MP3, dans chaque générateur. Sans
ffmpeg, le fichier reste tel quel et un avertissement s'affiche — mieux vaut
un module rapide qu'un module muet.
"""
import re
import shutil
import subprocess
from pathlib import Path

RACINE = Path(__file__).resolve().parent
ORIGINAUX = RACINE / ".audio-originaux"

VOIX_ENSEIGNANTE = "mActWQg9kibLro6Z2ouY"

# Les voix qui ne font que du dialogue. Énumérées plutôt que déduites par
# « tout ce qui n'est pas l'enseignante » : une voix ajoutée un jour pourrait
# être posée d'origine, et se la voir ralentir sans que personne l'ait décidé
# serait une régression muette.
VOIX_FEMININ_2 = "WW0JfNPk5DgcQdM0d6X6"
VOIX_MASCULIN_1 = "93nuHbke4dTER9x2pDwE"
VOIX_NARRATEUR = "IPgYtHTNLjC7Bq7IPHrm"
VOIX_DIALOGUE = frozenset({VOIX_FEMININ_2, VOIX_MASCULIN_1, VOIX_NARRATEUR})

FACTEUR = 0.85          # 1,0 = débit d'origine ; 0,85 ≈ 15 % plus lent

# Le palier : ce qu'on demande de l'élève, indépendamment de qui parle.
PALIER_DEBUTANT = 0.85   # niveaux 1 et 2
PALIER = 0.90            # niveaux 3 et au-delà

# Débit d'articulation, en caractères par seconde de parole (silences
# retirés) — médiane de 120 répliques par case, mesurée le 25 août 2026 par
# `build/mesurer_debits.py`. À refaire si une voix change.
#
# **Une seule valeur par voix ne suffit pas.** Le débit que rend ElevenLabs
# dépend du texte autant que du locuteur, et les textes changent de nature
# avec le palier. Calibrer sur une médiane tous paliers confondus a été
# essayé : la féminine #2 ressortait à 18,5 c/s aux niveaux 1-2 pour une cible
# de 15,6, parce que sa médiane globale (17,7) écrasait son débit réel de
# début de programme (20,0). D'où deux colonnes.
DEBIT = {
    #                 n1-n2   n3+
    VOIX_ENSEIGNANTE: (17.3, 19.4),
    VOIX_FEMININ_2:   (20.0, 19.8),
    VOIX_MASCULIN_1:  (17.8, 19.5),
    VOIX_NARRATEUR:   (17.2, 18.3),
}

# C'est cette case-là qui porte la plainte du 25 août 2026 : aux niveaux 1 et
# 2, la féminine #2 articule à 20,0 c/s quand ses deux partenaires de dialogue
# sont à 17,2 et 17,8 — 16 % plus vite, dans la même scène, sur la voix du
# personnage-élève. Au-delà du niveau 2 l'écart disparaît (19,8 contre 19,5 et
# 18,3) : le problème n'a jamais été général, il était logé au début du
# programme.

NIVEAU_DEFAUT = 4       # les modules sans préfixe sont la série de niveau 4
_averti = False


def niveau_du_chemin(chemin):
    """Le niveau du module d'après son dossier de sortie.

    `assets/interactive/module-n3-metro/t1/line_01_rosa.mp3` → 3. Un slug sans
    préfixe (`module-relations`, `je-demenage`) rend `NIVEAU_DEFAUT`.
    """
    m = re.search(r"module-n(\d)-", str(chemin))
    return int(m.group(1)) if m else NIVEAU_DEFAUT


def facteur_pour(voice_id, chemin):
    """Le facteur `atempo` de cette voix dans ce module, ou None si on n'y touche pas."""
    if voice_id == VOIX_ENSEIGNANTE:
        return FACTEUR          # elle est la référence : son facteur ne dépend de rien
    if voice_id not in VOIX_DIALOGUE:
        return None
    debutant = niveau_du_chemin(chemin) <= 2
    palier = PALIER_DEBUTANT if debutant else PALIER
    case = 0 if debutant else 1
    reference = DEBIT[VOIX_ENSEIGNANTE][case]
    facteur = round(palier * reference / DEBIT[voice_id][case], 2)
    # Une voix déjà plus posée que la référence donnerait un facteur au-dessus
    # de 1, c'est-à-dire une accélération. On ne touche pas à celle-là : le but
    # est de ramener les voix rapides, jamais de presser les autres.
    return None if facteur >= 1.0 else facteur


def _garder_original(chemin):
    """Met le fichier de côté avant de le toucher, s'il ne l'est pas déjà.

    Sans ça, un extrait ralenti au moment de la synthèse n'a aucun original,
    et il devient impossible de changer son facteur plus tard : ralentir par
    dessus du ralenti se compose. C'était le cas de 434 répliques de
    l'enseignante avant le 25 août 2026. On ne remplace jamais une sauvegarde
    existante — elle est plus ancienne, donc plus proche du brut.
    """
    try:
        rel = Path(chemin).resolve().relative_to(RACINE)
    except ValueError:
        return                      # hors du dépôt : rien à archiver
    sauve = ORIGINAUX / rel
    if sauve.exists():
        return
    sauve.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(chemin, sauve)


def ralentir(chemin, facteur=FACTEUR):
    """Ralentit un MP3 sur place. Rend True si le fichier a été réécrit."""
    global _averti
    chemin = Path(chemin)
    if not shutil.which("ffmpeg"):
        if not _averti:
            print("   ⚠️  ffmpeg absent : voix laissée au débit d'origine")
            _averti = True
        return False
    _garder_original(chemin)
    tmp = chemin.with_suffix(".ralenti.mp3")
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-y", "-i", str(chemin),
         "-filter:a", f"atempo={facteur}",
         "-c:a", "libmp3lame", "-b:a", "128k", "-ar", "44100", "-ac", "1",
         str(tmp)],
        capture_output=True, text=True)
    if r.returncode != 0 or not tmp.exists() or tmp.stat().st_size == 0:
        tmp.unlink(missing_ok=True)
        print(f"   ⚠️  ralentissement impossible : {r.stderr.strip()[:120]}")
        return False
    tmp.replace(chemin)
    return True


def ralentir_voix(chemin, voice_id):
    """Ralentit l'extrait si sa voix le demande, au facteur de son niveau."""
    facteur = facteur_pour(voice_id, chemin)
    if facteur is None:
        return False
    return ralentir(chemin, facteur)


# Le nom d'origine, gardé parce que cent-dix générateurs l'appellent — et
# parce qu'il reste exact tant qu'on ne lui demande pas *quelle* voix il
# ralentit. Ne pas le supprimer sans repasser sur tous les appelants.
ralentir_si_enseignante = ralentir_voix
