# Système de design · Bibliothèque de francisation

Système visuel des modules interactifs de francisation pour adultes (français québécois).
Il décrit un produit pédagogique, pas une marque commerciale : la lisibilité passe avant
l'expression visuelle, toujours.

**Sources.** Extrait de `assets/interactive/module-travail/module-travail-activite-interactive.html`
(module « Absent ou en retard : que faire ? »), du bloc `#sec-prep` qui servait d'essai de style,
des documents d'audit `RETOUCHES.md` et `RETOUCHES-2.md`, et de la refonte de la page
« Je me prépare » (`Je me prepare - couleur.dc.html`). Aucune charte externe n'est utilisée.

> **Interdit explicite du client :** ne jamais appliquer le système « SLB » (jaune-noir industriel,
> soudure) à ce projet, même s'il est proposé par défaut par un outil.

---

## PUBLIC ET CONTRAINTES NON NÉGOCIABLES

Adultes en apprentissage du français, souvent sur téléphone, parfois avec une scolarité
interrompue. Ces cinq règles ne se négocient pas — elles précèdent toute considération esthétique.

| Règle | Valeur |
|---|---|
| Corps de texte | ≥ 17 px (jamais 15 px pour un énoncé) |
| Cibles tactiles | ≥ 44 px (`--tap-min`), 48 px de confort |
| Contraste | ≥ 4.5:1 pour tout texte, y compris les libellés secondaires |
| Focus clavier | visible partout (`:focus-visible`, contour vert 3 px) |
| Couleur | jamais porteuse d'information seule — toujours doublée d'un glyphe ou d'un mot |

Corollaires : `user-scalable=no` est proscrit ; tout ce qui se fait à la souris (glisser-déposer)
doit se faire au clavier — d'où l'association par clic-clic plutôt que par glissement.

---

## CONTENU · comment on écrit

- **Voix :** on s'adresse à l'apprenant au **vous** (« Écoutez de nouveau le dialogue, puis
  répondez »). L'infinitif est réservé aux titres d'action (« Écouter le dialogue »).
- **Phrases courtes, un fait par phrase.** Pas de subordonnées empilées, pas de tournure passive
  quand l'actif existe.
- **Casse :** phrase normale partout. Les majuscules servent uniquement aux sur-titres de 13 px
  (`VOCABULAIRE · 12 PAIRES`). Jamais de Titre En Capitales Partout.
- **Titres d'exercice :** un groupe nominal ou une phrase à la première personne, dans la voix de
  l'apprenant — « Je complète avec le bon son », « Le mot et sa définition », « Vrai ou faux ».
  C'est la logique des sections du module : *Je me prépare*, *Je mets en application*,
  *Je retiens des mots*.
- **Consigne = une phrase, sous le titre**, en gris secondaire : ce qu'on écoute, puis ce qu'on
  fait. « Écoutez le mot, puis indiquez le son que vous entendez. »
- **Rétroaction :** brève et factuelle. « ✓ Juste » · « ✕ La bonne réponse est VRAI ». Ni
  félicitation exagérée, ni jugement. On donne la bonne réponse, on n'humilie pas l'erreur.
- **Vocabulaire :** l'article fait partie du mot (« un retard », « une boîte vocale ») — c'est du
  contenu pédagogique, pas de la coquetterie.
- **Aucun émoji.** Ils sont lus à voix haute par les lecteurs d'écran (« téléphone portable ») et
  parasitent la consigne. Le titre de section porte déjà l'information.
- **Français québécois :** « courriel », « superviseur », heures en `15 h`, `9 h 30`.

---

## FONDATIONS VISUELLES

**Couleur.** Fond neutre chaud (`--paper-100` #F7F7F5), cartes blanches, encre presque noire
(#17181A). **Un seul accent : le vert** `--accent` #0A8F5B (texte vert : `--green-800` #07734A).
Cinq couleurs de section (acier, violet, ambre, teal, forêt) servent **au repérage seulement** et
n'apparaissent qu'à quatre endroits : la pastille numérotée, le sur-titre, un filet gauche de
4 px, le point de la barre de parcours. Le **rouge est réservé à l'audio** et à l'erreur ; l'erreur
n'a pas d'aplat saturé (fond #FFF6F5, filet et texte rouges) afin que le seul rouge plein de la
page reste le bouton « Écouter ».

**Sélection.** Un élément choisi devient une **plaque encre** (fond #17181A, texte blanc) — pas
une teinte de plus. La couleur reste ainsi entièrement disponible pour dire « juste » ou
« à revoir ». C'est la règle qui empêche le bricolage de revenir.

**Type.** Nunito, 400 à 900. Choisie pour ses formes ouvertes et son `a`/`g` à un étage, plus
lisibles pour qui apprend à lire. Quatre niveaux à écarts francs : titre de page 62 px / 900,
titre d'exercice 30 px / 900, chapeau 19 px, énoncé 18 px, consigne 17 px. Sur-titre 13 px / 800
majuscules, interlettrage .12em. Rien sous 17 px sauf libellés d'interface.

**Hiérarchie de page** — quatre niveaux, dans cet ordre :
1. **Bandeau clair** (`--surface-band` #EDF6F1) : sur-titre du module, titre, chapeau, et la
   situation dans une carte blanche avec le bouton audio. *Le bandeau n'est jamais noir.*
2. **Barre de parcours collante** : une pastille par étape, cliquable, qui se teinte quand
   l'étape est réussie. L'apprenant sait toujours où il en est.
3. **En-tête d'exercice** : pastille numérotée teintée + sur-titre coloré + titre 30 px +
   consigne grise + score à droite.
4. **Contenu** : cartes blanches, filets 1 px, rangées séparées par un filet plutôt qu'encadrées.

**Espacement.** Base 4 px, échelle de 8 crans (4 · 8 · 12 · 16 · 20 · 24 · 32 · 48). Gouttière de
page 32 px, écart entre exercices 48 px, largeur de contenu 1000 px. Pas de valeur intermédiaire
inventée.

**Rayons.** Quatre valeurs : 10 px (contrôles, champs, tuiles), 14 px (jetons, pastilles),
18 px (cartes, cadres, bandeaux), pilule (boutons, étiquettes, scores).

**Filets et ombres.** La structure vient des **filets 1 px** et de l'alignement, pas de la
profondeur : `--sh-card` est presque invisible (0 1px 2px rgba(20,20,20,.04)). Un filet gauche de
4 px marque l'appartenance à une section. Aucun encadrement double : un énoncé dans une carte se
sépare par un filet, pas par une seconde boîte.

**Fonds.** Aplats uniquement. Aucun dégradé, aucune texture. Un seul bloc foncé par page au
maximum (l'appel à l'action final), jamais l'en-tête.

**Survol / appui / mouvement.** Survol : fond qui s'éclaircit d'un cran (blanc → #F7F7F5) ;
l'audio s'assombrit (#DC2626 → #B91C1C). Transitions de 140 ms sur `cubic-bezier(.2,.7,.3,1)`,
sur la couleur seulement. Aucun rebond, aucun déplacement, aucune parallaxe, aucune boucle
infinie : rien ne doit détourner l'attention d'une consigne. `prefers-reduced-motion` annule tout.
L'ancienne secousse (`shake`) sur l'erreur est retirée : elle sanctionne au lieu d'informer.

**Transparence et flou.** Un seul usage : la barre de parcours collante
(`rgba(247,247,245,.94)` + `blur(8px)`). Nulle part ailleurs.

**Imagerie.** Aucune illustration décorative. Les seules images sont pédagogiques (association
image-mot) : photos réelles, cadrées serré, en 100 × 100 ou 110 px de haut, rayon 10 px.
Quand une image manque, on laisse un emplacement neutre légendé — on ne dessine pas de substitut.

---

## ICONOGRAPHIE

Le module n'utilise que **trois icônes**, en SVG inline monochromes à trait ~2.2 px, qui héritent
de `currentColor` : **haut-parleur** (écouter), **micro** (s'enregistrer), **flèche** (continuer).
Elles vivent dans `assets/interactive/module-travail/icons/` du projet source (`play.svg`, etc.) —
copiez-les, ne les redessinez pas.

- Une icône seule est toujours dans une cible de 44 px minimum (`.btn-audio-round`).
- Sur fond rouge audio, l'icône est blanche ; ailleurs elle prend la couleur du texte.
- **Aucun émoji, aucun caractère unicode décoratif.** Les glyphes ✓ ✕ ! sont l'exception : ils
  portent l'information de rétroaction et sont générés en CSS (`::before`), donc toujours
  accompagnés du texte.
- Si une icône manque : Lucide (trait 2 px, sans remplissage) est le substitut le plus proche.
  Signalez toute substitution.

---

## INDEX

| Fichier | Contenu |
|---|---|
| `styles.css` | point d'entrée unique — uniquement des `@import` |
| `tokens/fonts.css` | Nunito, `--font-sans` |
| `tokens/colors.css` | neutres, vert d'accent, 5 accents de section, audio, 4 états de rétroaction, alias sémantiques |
| `tokens/typography.css` | échelle de 10 corps, interlignes, interlettrages, graisses |
| `tokens/spacing.css` | échelle d'espacement, rayons, largeur de contenu, cibles tactiles |
| `tokens/effects.css` | ombres, durées, courbe, focus |
| `tokens/base.css` | socle : reset minimal, titres, liens, `:focus-visible`, placeholder |
| `components/layout.css` | `.band` `.steps` `.step` `.exo` (en-tête d'exercice, couleur de section) |
| `components/buttons.css` | `.btn--pri` `.btn--ghost` `.btn--audio` `.btn-audio-round` |
| `components/forms.css` | `.field` `.field--area` `.field-label` |
| `components/cards.css` | `.card` `.savoir` `.dialogue__line` |
| `components/exercises.css` | `.choice` `.chip` (association) `.drop` `.blank` `.exo-row` |
| `components/feedback.css` | `.fb` `.fb-box` `.score` `.banner` |
| `SKILL.md` | enveloppe Agent Skill pour Claude Code |

**Couleur de section :** posez `.exo--orale` / `--phonie` / `--ecriture` / `--ecoute` / `--vocab`
sur le conteneur de l'exercice ; tout ce qui est à l'intérieur lit `--sec` et `--sec-soft`.

## À FAIRE (non livré)

- `preview.html` : planche de tous les composants dans leurs états.
- `MIGRATION.md` : table des ~39 valeurs codées en dur du module actuel vers les jetons.
- Les icônes SVG ne sont pas encore copiées dans `assets/` de ce dossier.
