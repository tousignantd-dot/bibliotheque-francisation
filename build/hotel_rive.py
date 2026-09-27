"""La palette Rive-Claire des pages de présentation de l'hôtel (pilote, guide, démo).

Choisie par Daniel le 25 septembre 2026 parmi six propositions
(`assets/presentations/hotellerie-couleurs.html`). L'écran de l'employé la porte
dans `hotel_planches.py` (jetons du système de design) ; les pages bâties sur
l'en-tête de `magasin-vetements-plan.html` ont leurs propres jetons (--ground,
--ink, --acier…) : on les redéfinit ici, clair ET sombre, une seule fois — comme
`francoeur_denim.py` le fait pour Francœur.

Sarcelle pour l'accent (#0F5E63), corail (#C4613A) pour le filet du haut de page
— jamais pour du texte courant.
"""

CSS = """
/* ── Palette Rive-Claire (build/hotel_rive.py) ── */
:root{
  --ground:#F3EFE6; --card:#FFFFFF; --sunken:#ECE6DA;
  --ink:#132A2C; --body:#223A3C; --muted:#4D5E5F;
  --line:#DFD8C9; --line-fort:#C9C0AE;
  --acier:#0F5E63; --acier-bg:#DDEDEC;
  --surpiqure:#C4613A;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0F1A1B; --card:#152324; --sunken:#1A2B2C;
    --ink:#EEF3F2; --body:#C6D3D2; --muted:#93A5A4;
    --line:#26393A; --line-fort:#34494A;
    --acier:#7CC4C4; --acier-bg:#13302F;
    --surpiqure:#E0875F;
  }
}
:root[data-theme="dark"]{
  --ground:#0F1A1B; --card:#152324; --sunken:#1A2B2C;
  --ink:#EEF3F2; --body:#C6D3D2; --muted:#93A5A4;
  --line:#26393A; --line-fort:#34494A;
  --acier:#7CC4C4; --acier-bg:#13302F;
  --surpiqure:#E0875F;
}
body{border-top:4px solid var(--surpiqure)}
"""
