"""La palette « brique sur pierre » de Chez Jocelyne (écran, guide, démo, pilote, relecture).

Choisie par Daniel le 30 septembre 2026 au second tour de
`assets/presentations/restauration/restauration-couleurs.html` (build/restauration_couleurs.py) :
la brique gardée au premier tour, sur un fond gris chaud de béton poli (#EEEDEA) plutôt que le
crème provisoire, le rouge d'erreur passé au cramoisi (#D12F4B) et des bordures plus marquées.

Deux jeux de jetons, définis UNE fois ici :
- ECRAN : les jetons du système de design, pour l'écran de l'employé (restaurant_planches.py),
  qui reste en clair (meta color-scheme light) ;
- CSS : les jetons des pages de présentation (--ground, --ink, --acier…), clair ET sombre,
  pour le guide, la démo, le pilote et la relecture.

`python3 build/restauration_pierre.py` mesure les contrastes et refuse sous les seuils.
"""

# ── Clair : les valeurs de la page de couleurs, tour 2, « pierre ».
FOND, CARTE, ENCRE, APPUI = "#EEEDEA", "#FFFFFF", "#241A14", "#5E5046"
LIGNE, LIGNE_FORTE = "#D4D0C8", "#B9B3A8"
BRIQUE, BRIQUE_BG = "#8A2E1C", "#F3E3DC"
CUIVRE, HALO = "#C8692A", "#FBE9DC"          # enseigne, point du « i », filet ; jamais du texte courant
OK, OK_BG = "#1F7A4D", "#E3F2EA"
NON, NON_BG, NON_ENCRE = "#D12F4B", "#FCE9EC", "#A61E38"

# ── Sombre (pages de présentation seulement) : gris chaud, brique éclaircie.
S_FOND, S_CARTE, S_ENFONCE = "#171615", "#211F1D", "#1C1A18"
S_ENCRE, S_CORPS, S_APPUI = "#F1EEEA", "#D4CFC8", "#A39C93"
S_LIGNE, S_LIGNE_FORTE = "#34312D", "#4A4540"
S_BRIQUE, S_BRIQUE_BG, S_CUIVRE = "#EC9B85", "#3A231C", "#E08A4F"

ECRAN = f"""
  --surface-page:{FOND};--surface-card:{CARTE};--text-strong:{ENCRE};--text-body:{ENCRE};
  --line-200:{LIGNE};--line-300:{LIGNE_FORTE};--accent:{BRIQUE};--text-muted:{APPUI};
  --warn-bg:{HALO};--warn-line:{CUIVRE};--warn-ink:#8A3F0F;
  --ok-line:{OK};--ok-bg:{OK_BG};--ok-ink:{OK};
  --no-line:{NON};--no-bg:{NON_BG};--no-ink:{NON_ENCRE};
  --rj-teinte:{BRIQUE};--rj-fond:{BRIQUE_BG}"""

_SOMBRE = f"""--ground:{S_FOND};--card:{S_CARTE};--sunken:{S_ENFONCE};--ink:{S_ENCRE};--body:{S_CORPS};--muted:{S_APPUI};
    --line:{S_LIGNE};--line-fort:{S_LIGNE_FORTE};--acier:{S_BRIQUE};--acier-bg:{S_BRIQUE_BG};--surpiqure:{S_CUIVRE};"""

CSS = f"""
/* ── Palette « brique sur pierre » (build/restauration_pierre.py, choisie le 30 sept. 2026) ── */
:root{{
  --ground:{FOND};--card:{CARTE};--sunken:#F6F5F3;--ink:{ENCRE};--body:#3A2E26;--muted:{APPUI};
  --line:{LIGNE};--line-fort:{LIGNE_FORTE};--acier:{BRIQUE};--acier-bg:{BRIQUE_BG};--surpiqure:{CUIVRE};
}}
@media (prefers-color-scheme: dark){{:root:not([data-theme="light"]){{
    {_SOMBRE}
}}}}
:root[data-theme="dark"]{{
    {_SOMBRE}
}}
body{{border-top:4px solid var(--surpiqure)}}
@media print{{body{{border-top:0}}}}
"""


def _lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contraste(a, b):
    la, lb = sorted((_lum(a), _lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


CONTROLES = [
    ("texte sur le fond", ENCRE, FOND, 4.5), ("appui sur le fond", APPUI, FOND, 4.5),
    ("appui sur carte", APPUI, CARTE, 4.5), ("blanc sur brique", "#FFFFFF", BRIQUE, 4.5),
    ("brique sur le fond", BRIQUE, FOND, 4.5), ("juste sur carte", OK, CARTE, 4.5),
    ("juste sur son fond", OK, OK_BG, 4.5), ("pas juste (texte) sur son fond", NON_ENCRE, NON_BG, 4.5),
    ("bordure « pas juste » sur carte", NON, CARTE, 3), ("bordure forte sur carte", LIGNE_FORTE, CARTE, 1.8),
    ("sombre : texte", S_ENCRE, S_FOND, 4.5), ("sombre : corps sur carte", S_CORPS, S_CARTE, 4.5),
    ("sombre : appui sur carte", S_APPUI, S_CARTE, 4.5), ("sombre : brique sur carte", S_BRIQUE, S_CARTE, 4.5),
    ("sombre : brique sur son fond", S_BRIQUE, S_BRIQUE_BG, 4.5),
]


def verifier():
    fautes = [f"{n} : {contraste(a, b):.2f}:1 < {s}" for n, a, b, s in CONTROLES if contraste(a, b) < s]
    if fautes:
        raise SystemExit("Contrastes insuffisants :\n  " + "\n  ".join(fautes))


if __name__ == "__main__":
    for n, a, b, s in CONTROLES:
        print(f"{contraste(a, b):5.2f}:1  (≥ {s})  {n}")
    verifier()
    print("Tout passe.")
