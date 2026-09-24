# Journal de révision — Maison Francœur

## Tour 1 → révision des bloquants (24 septembre 2026)

Premier audit : **2 bloquants, 29 majeurs, 43 mineurs** (`audit1-contenu.json`,
`audit1-page.json`, page `assets/presentations/francoeur-audit-1.html`).
Critères les plus touchés : A3, E1, F1, D4, G1.

| Élément | Statut | Avant | Après | Critères | Pourquoi |
|---|---|---|---|---|---|
| Exercice 5 « Ce que le client veut » (20 demandes) | modifié | trois distracteurs qui changent chacun UN trait de la bonne carte (article, couleur ou taille) | carré latin : (A,C,T) (A,C′,T′) (A′,C,T′) (A′,C′,T) — chaque valeur deux fois ; sans taille, (A,C) (A,C′) (A′,C) (A′,C′) | D4 · bloquant | La bonne carte était la majoritaire sur chaque trait : 20 demandes sur 20 se réussissaient sans écouter. Désormais aucune carte n'est majoritaire ; seule la phrase désigne la bonne. |
| Test, partie B, crans 2 et 3 (9 items) | modifié | même règle ; au cran 3, trois cartes écrites à la main | même carré latin ; au cran 3 on écrit les valeurs que la phrase ÉCARTE (b31 : le chandail, b32 : le rose, b33 : le moyen, b34 : le noir), et le carré les place | F1 · bloquant | 9 items sur 14 se devinaient : le niveau proposé et l'écart entre deux passations étaient faussés. Le piège voulu (ce que le client nie ou reprend) est conservé. |
| Construction (`francoeur_planches.py`) | ajouté | — | `devinable()` : la construction s'arrête si une bonne carte est seule à réunir les valeurs les plus fréquentes | D4, F1 | Le contrôle qui manquait. Vu échouer sur l'ancien motif (vrai), et passer sur le carré (faux). |

Vérifié : 0 item devinable sur 20 (exercice) et sur 14 (test B) ; l'exercice et
le test se jouent au navigateur sans erreur.

**Reste à traiter** : les 29 majeurs, selon les décisions de Daniel sur la page
des constats — puis le tour 2 de l'audit, sur TOUTE la grille.
