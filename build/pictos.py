#!/usr/bin/env python3
"""Les pictogrammes de la banque du niveau 1, dessinés et jamais générés.

Deux jeux, deux usages :

- **`SIGNALISATION`** — les panneaux qu'on lit dans un lieu public. Le cadre y
  porte la moitié du sens avant tout dessin : rond rouge barré = interdit,
  carré vert = secours et circulation, carré bleu = information et services,
  triangle jaune = danger. C'est la convention réelle, et c'est ce qu'un élève
  doit apprendre à lire avant le glyphe — elle lui permet de deviner juste
  devant un panneau qu'il n'a jamais vu.
- **`ACTIONS`** — les consignes de classe (`n1-s17`, impératif présent). Ce ne
  sont pas des panneaux : pas de cadre, pas de couleur, un trait en
  `currentColor` qui prend la couleur de son bouton.

**Pourquoi dessinés.** Un modèle d'image écrit du charabia dès qu'un panneau
porte une inscription — c'est la règle des images de `CLAUDE.md`, payée
plusieurs fois. Et un pictogramme est justement de la géométrie : ni ombre, ni
décor, ni texte, ce qui est exactement ce qui le rend lisible de loin. Une
photo générée serait à la fois plus chère et moins juste.

Le bloc `SIGNALISATION` a été déplacé ici depuis `build/appariement.py` sans
qu'un octet du HTML produit change — l'ordre des clés est celui d'origine, et
`python3 build/appariement.py --verifier` le vérifie.
"""

# ── La bibliothèque de pictogrammes ────────────────────────────────────
# Chacun est un carré de 100. Le cadre dit déjà la moitié : rond rouge barré
# pour l'interdit, carré vert pour le secours, carré bleu pour l'information,
# triangle jaune pour le danger. C'est la convention réelle de la
# signalisation, et c'est ce que l'élève doit apprendre à lire avant le glyphe.
# Les couleurs sont celles des panneaux, pas celles du système de design : ce
# sont des données du monde, pas des choix d'interface.
CADRE_VERT = '<rect x="4" y="4" width="92" height="92" rx="6" fill="#127A46"/>'
CADRE_BLEU = '<rect x="4" y="4" width="92" height="92" rx="6" fill="#1A5FA8"/>'
CADRE_ROND = ('<circle cx="50" cy="50" r="45" fill="#FFFFFF" stroke="#C8202B" stroke-width="10"/>'
              '<line x1="19" y1="81" x2="81" y2="19" stroke="#C8202B" stroke-width="10" stroke-linecap="round"/>')
CADRE_JAUNE = '<path d="M50 6 L96 88 H4 Z" fill="#F2C200" stroke="#1B1B1B" stroke-width="6" stroke-linejoin="round"/>'

SIGNALISATION = {
    # ── Secours et circulation (carré vert) ───────────────────────────
    'sortie': CADRE_VERT + (
        '<rect x="20" y="22" width="30" height="56" rx="3" fill="none" stroke="#FFFFFF" stroke-width="6"/>'
        '<path d="M56 50 H86 M74 38 L86 50 L74 62" fill="none" stroke="#FFFFFF" '
        'stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>'),
    'premiers-soins': CADRE_VERT + (
        '<path d="M50 24 V76 M24 50 H76" stroke="#FFFFFF" stroke-width="14" stroke-linecap="round"/>'),
    'escalier': CADRE_VERT + (
        '<path d="M20 78 H38 V60 H56 V42 H74 V24 H86" fill="none" stroke="#FFFFFF" '
        'stroke-width="7" stroke-linejoin="round" stroke-linecap="round"/>'),

    # ── Information et services (carré bleu) ──────────────────────────
    'accueil': CADRE_BLEU + (
        '<circle cx="50" cy="27" r="7" fill="#FFFFFF"/>'
        '<rect x="43" y="41" width="14" height="36" rx="4" fill="#FFFFFF"/>'),
    'cafeteria': CADRE_BLEU + (
        '<path d="M32 22 V50 M32 50 V80 M24 22 V40 M40 22 V40 M24 40 H40" fill="none" '
        'stroke="#FFFFFF" stroke-width="5" stroke-linecap="round"/>'
        '<path d="M68 80 V22 c9 4 9 26 0 30" fill="none" stroke="#FFFFFF" '
        'stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'),
    'ascenseur': CADRE_BLEU + (
        '<path d="M36 46 L46 32 L56 46" fill="none" stroke="#FFFFFF" stroke-width="6" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<path d="M36 58 L46 72 L56 58" fill="none" stroke="#FFFFFF" stroke-width="6" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
        '<rect x="66" y="28" width="14" height="48" rx="3" fill="none" stroke="#FFFFFF" stroke-width="5"/>'),
    'telephone': CADRE_BLEU + (
        '<path d="M32 26 c-6 0-10 5-9 11 3 20 20 37 40 40 6 1 11-3 11-9 v-8 '
        'c0-3-2-5-5-6l-9-2c-3-1-6 1-7 4l-2 4 c-7-4-13-10-17-17l4-2 c3-1 5-4 4-7 '
        'l-2-9 c-1-3-3-5-6-5 z" fill="#FFFFFF"/>'),

    # ── Interdictions (rond rouge barré) ──────────────────────────────
    'defense-de-fumer': CADRE_ROND + (
        '<rect x="26" y="46" width="42" height="10" rx="2" fill="#1B1B1B"/>'
        '<rect x="71" y="46" width="7" height="10" rx="2" fill="#1B1B1B"/>'),
    'stationnement-interdit': CADRE_ROND + (
        '<path d="M38 74 V30 h16 a12 12 0 0 1 0 24 h-16" fill="none" stroke="#1B1B1B" '
        'stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>'),

    # ── Danger (triangle jaune) ───────────────────────────────────────
    'attention': CADRE_JAUNE + (
        '<rect x="45" y="34" width="10" height="28" rx="4" fill="#1B1B1B"/>'
        '<circle cx="50" cy="72" r="6" fill="#1B1B1B"/>'),
    'plancher-mouille': CADRE_JAUNE + (
        '<path d="M50 34 c-8 12-14 19-14 26 a14 14 0 0 0 28 0 c0-7-6-14-14-26 z" fill="#1B1B1B"/>'),
}

# ── Les consignes de classe ────────────────────────────────────────────
# Aucun cadre, aucune couleur : ce sont des gestes, pas des panneaux. Le trait
# est en `currentColor` pour que le pictogramme suive la couleur de son bouton
# — y compris quand le bouton passe en vert « juste » ou en rouge « non ».
_T = 'fill="none" stroke="currentColor" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"'

ACTIONS = {
    # La chaise vue de côté, et une flèche qui dit dans quel sens on va.
    'leve-toi': ('<path d="M30 82 V44 h30 v38 M30 60 h30" %s/>'
                 '<path d="M76 62 V26 M64 38 L76 26 L88 38" %s/>' % (_T, _T)),
    'assieds-toi': ('<path d="M30 82 V44 h30 v38 M30 60 h30" %s/>'
                    '<path d="M76 26 V62 M64 50 L76 62 L88 50" %s/>' % (_T, _T)),
    # Le crayon et sa ligne. La mine est un triangle plein : sans elle, le
    # crayon se lit comme une simple barre oblique.
    'ecris': ('<path d="M26 74 L62 38 l12 12 L38 86 L20 92 Z" %s/>'
              '<path d="M62 38 l8-8 a6 6 0 0 1 8 0 l4 4 a6 6 0 0 1 0 8 l-8 8" %s/>'
              '<path d="M18 96 H88" %s/>' % (_T, _T, _T)),
    # L'oreille : deux arcs. Le petit à l'intérieur est ce qui empêche de la
    # lire comme une virgule.
    'ecoute': ('<path d="M62 22 a26 26 0 0 0-26 26 v18 a14 14 0 0 0 14 14 '
               'a10 10 0 0 0 10-10 a12 12 0 0 1 12-12 a20 20 0 0 0 6-36 z" %s/>'
               '<path d="M52 52 a10 10 0 0 1 16 0" %s/>' % (_T, _T)),
    # L'œil : deux arcs qui se rejoignent, et la pupille.
    'regarde': ('<path d="M10 50 c14-20 28-30 40-30 s26 10 40 30 '
                'c-14 20-28 30-40 30 s-26-10-40-30 z" %s/>'
                '<circle cx="50" cy="50" r="11" fill="currentColor"/>' % _T),
    # Le livre : deux pages ouvertes autour d'une reliure.
    'ouvre': ('<path d="M50 30 C38 22 24 20 12 22 v50 c12-2 26 0 38 8 '
              'c12-8 26-10 38-8 V22 c-12-2-26 0-38 8 z" %s/>'
              '<path d="M50 30 V80" %s/>' % (_T, _T)),
    # Le même livre, fermé : le dos et la tranche.
    'ferme': ('<rect x="24" y="18" width="52" height="64" rx="4" %s/>'
              '<path d="M36 18 V82" %s/>' % (_T, _T)),
    # Prendre : l'objet quitte la table. Aucune main — la règle des images du
    # dépôt vaut aussi pour un dessin, et une main dessinée est illisible.
    'prends': ('<rect x="34" y="46" width="32" height="24" rx="3" %s/>'
               '<path d="M50 38 V12 M38 24 L50 12 L62 24" %s/>'
               '<path d="M14 84 H86" %s/>' % (_T, _T, _T)),
    'depose': ('<rect x="34" y="30" width="32" height="24" rx="3" %s/>'
               '<path d="M50 62 V88 M38 76 L50 88 L62 76" %s/>'
               '<path d="M14 94 H86" %s/>' % (_T, _T, _T)),
    # Répéter : la flèche qui revient sur elle-même.
    'repete': ('<path d="M22 50 a28 28 0 1 1 10 21" %s/>'
               '<path d="M18 30 L22 52 L44 46" %s/>' % (_T, _T)),
}

# Un seul dictionnaire pour le rendu : les deux jeux ne partagent aucune clé,
# et un exercice peut vouloir les mélanger (une consigne « sortez » à côté du
# panneau SORTIE).
TOUS = dict(SIGNALISATION, **ACTIONS)

if __name__ == '__main__':
    doublons = set(SIGNALISATION) & set(ACTIONS)
    if doublons:
        raise SystemExit('!! clé dans les deux jeux : %s' % ', '.join(sorted(doublons)))
    print('%d panneaux, %d consignes, %d en tout'
          % (len(SIGNALISATION), len(ACTIONS), len(TOUS)))
