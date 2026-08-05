---
name: francisation-design
description: Système de design pour la bibliothèque de francisation pour adultes (modules interactifs FR-QC). À utiliser pour créer ou modifier toute interface, activité interactive, fiche imprimable ou maquette de ce projet — en production comme en prototype jetable. Contient les jetons CSS, la couche de composants, les règles d'accessibilité et le ton rédactionnel.
user-invocable: true
---

Lisez `README.md` dans ce dossier, puis explorez `tokens/` et `components/`.

Point d'entrée unique : `<link rel="stylesheet" href="styles.css">`. Ne liez jamais un fichier
de `tokens/` ou `components/` directement.

Trois interdits, dans cet ordre d'importance :
1. **Aucun système de marque externe.** Ce projet n'utilise QUE ce système. En particulier, jamais
   de palette jaune-noir industrielle (« SLB ») : elle a été explicitement rejetée.
2. **Aucune valeur en dur** quand un jeton existe. `#0A8F5B` s'écrit `var(--accent)`.
3. **Aucune information codée par la couleur seule** — chaque état porte aussi un glyphe ou un mot.

Public : adultes en francisation. Toute décision se tranche par la lisibilité : corps ≥ 17 px,
cibles tactiles ≥ 44 px, contraste ≥ 4.5:1, focus clavier visible, zoom jamais désactivé.

Si l'utilisateur invoque cette compétence sans autre consigne, demandez-lui quel module ou quel
écran il veut construire, posez quelques questions (niveau, tâche visée, support écran ou papier),
puis produisez du HTML statique lisible ou du code de production selon le besoin.
