"""La palette Denim des pages de la Maison Francœur (guide, démo, pilote).

Choisie par Daniel le 24 septembre 2026 parmi quatre propositions
(`assets/presentations/francoeur-couleurs.html`) : les cours en entreprise ne
portent pas les couleurs du portail. L'écran de l'employé la porte dans
`francoeur_planches.py` (jetons du système de design) ; les pages de
présentation, bâties sur l'en-tête de `magasin-vetements-plan.html`, ont leurs
propres jetons (--ground, --ink, --acier…) : on les redéfinit ici, clair ET
sombre, une seule fois pour les trois pages.

Bleu jean pour l'accent (#2B4A78), orange « surpiqûre » (#C8692A) pour le filet
du haut de page — jamais pour du texte courant : il n'y fait que 3,8:1.
"""

CSS = """
/* ── Palette Denim (build/francoeur_denim.py) ── */
:root{
  --ground:#EDF1F5; --card:#FFFFFF; --sunken:#F5F7FA;
  --ink:#17212E; --body:#2C3644; --muted:#4F5B6A;
  --line:#D5DDE6; --line-fort:#B9C4D1;
  --acier:#2B4A78; --acier-bg:#E3EAF2;
  --surpiqure:#C8692A;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#111822; --card:#18212C; --sunken:#1C2632;
    --ink:#EEF2F6; --body:#C9D2DC; --muted:#94A1B0;
    --line:#2A3542; --line-fort:#3A4757;
    --acier:#8FB0DE; --acier-bg:#172335;
    --surpiqure:#E08A4F;
  }
}
:root[data-theme="dark"]{
  --ground:#111822; --card:#18212C; --sunken:#1C2632;
  --ink:#EEF2F6; --body:#C9D2DC; --muted:#94A1B0;
  --line:#2A3542; --line-fort:#3A4757;
  --acier:#8FB0DE; --acier-bg:#172335;
  --surpiqure:#E08A4F;
}
body{border-top:4px solid var(--surpiqure)}
@media print{body{border-top:0}}
"""
