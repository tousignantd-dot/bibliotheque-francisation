# Chantier des modules neufs — niveau 4

Journal d'avancement, tenu à jour à chaque étape. **Après une interruption,
c'est ce fichier qui dit où reprendre.**

Méthode : skill `module-neuf` (`~/.claude/skills/module-neuf/`).
Mandat d'autonomie du 20 août 2026 : numérotation séquentielle, médias
générés, poussé en production au fur et à mesure.

Les six étapes par module : **cadrer · inventer · contenu · build · médias ·
livrer**.

| N° | Slug | Situation | Étape atteinte |
|----|------|-----------|----------------|
| 11 | `module-relations` | Relations sociales | **terminé** |
| 12 | `module-deplacement` | Déplacement dans une ville | **terminé** |
| 13 | `module-activite` | Participation à une activité culturelle ou sportive | **terminé** |
| 14 | `module-alimentation` | Achat d'aliments ou de produits d'entretien | **terminé** |
| 15 | `module-achat` | Achat de biens de consommation durables | **terminé** |
| 16 | `module-restaurant` | Service de restauration | **terminé** |
| 18 | `module-vetements` | Achat de vêtements | **terminé** |

Le 17 est pris par `module-banque`, d'où le saut.

## Module 11 — Relations sociales

- **Scénario** : Mariama (Guinée, arrivée il y a 14 mois) rejoint la ligue de
  volleyball du centre communautaire et se lie avec Chantal. Fatou, la sœur
  restée au pays, annonce une naissance.
- **Sections** : Je découvre (au vestiaire) · Défi 1 · Ce que je fais de mes
  semaines · Défi 2 · Ce que j'ai vécu · Défi 3 · Donner des nouvelles ·
  Je me lance.
- **Grammaire** : accent d'insistance · pronoms relatifs qui/que/où ·
  imparfait et passé composé · y et là · la carte postale et la carte de vœux ·
  grâce à / à cause de. Aucun de ces six points n'est déjà traité dans les
  onze modules existants — vérifié en relevant les titres de toutes les
  mini-leçons produites.
- **Couleur** : teal `#0D7A6F` / `#DCF2EF` (rotation à cinq couleurs du
  projet). **Activité** : 48.

### Fait

- Jeu de rôle : le serveur n'acceptait que la paire de rôles
  locataire/propriétaire, écrite en dur à trois endroits. Généralisée aux
  rôles déclarés par le scénario, plus une clé `adresse` pour qu'un échange
  informel se tutoie. Les deux scénarios existants produisent une consigne
  système **identique au caractère près** (346 lignes comparées).

- Contenu écrit : 7 dialogues (86 répliques), 15 mots de vocabulaire,
  25 exercices, 7 mini-leçons (34 combinaisons de laboratoire), 18 phrases
  porteuses. Module construit : 285 776 octets.
- Le gabarit a gagné un vingt-et-unième jeton, `%%JR_ROLE%%` : le rôle de
  départ du jeu de rôle était écrit en dur (`role:'locataire'`) et aurait
  envoyé un rôle inexistant au serveur. `module-probleme` se reconstruit
  toujours à l'octet près (md5 inchangé).
- Vérifié dans le navigateur : 6 sections rendues sans erreur, 25 exercices,
  les 7 mini-leçons s'ouvrent, **34 combinaisons de laboratoire toutes
  pourvues**, aucune clé de `PLUS` orpheline, aucun dialogue inutilisé ni
  manquant, 95 identifiants d'audio relevés.
- Une faute de fabrication attrapée là : une virgule doublée dans
  `dialogues.js`, produite par le script d'ajout du septième dialogue. Elle
  cassait tout le script de la page — et la page continuait de s'afficher,
  muette. Le contrôle utile n'est pas « la page s'affiche » mais « les
  constantes existent ».
- **Médias faits.** 21 images (fal.ai / Nano Banana 2, 0,71 $) : huit
  illustrations d'exercice à 1024 px et treize photos de vocabulaire réduites à
  800 px / qualité 82. 213 MP3 (ElevenLabs) : 82 répliques sur sept dialogues
  et 131 mots, phrases et mini-leçons. Contrôle : les **213 URL d'audio et les
  22 URL d'images que la page peut demander répondent toutes** — aucune n'est
  manquante.
- Le générateur d'audio de ce module **ne recopie plus les dialogues** : il lit
  `build/contenu/module-relations/dialogues.js`. Les générateurs précédents en
  gardaient une copie, qui divergeait du module à la première correction.
- Nouvel outil : `build/collecte_sons.py`. Le relevé des identifiants d'audio
  se collait jusqu'ici à la main depuis la console du navigateur ; il est
  maintenant reçu directement et écrit dans `sons_<slug>.json`.
- Piège aligné juste à temps : le calcul du nom de fichier d'une réplique doit
  reproduire `charSlug()` du moteur **au caractère près**. Une expression
  régulière « propre » aurait écrit `jean_philippe` là où le moteur demande
  `jean-philippe`.
- **Séances faites.** Seize présentations, 187 diapositives, et les seize
  fiches élèves qui en sortent (142 blocs, noir et blanc vérifié). Pied de page
  contrôlé dans les seize `.pptx` livrés : `MODULE 11` partout, conforme au
  registre. `sections.json` et `materiel.json` relevés et vérifiés.
- Un défaut du socle corrigé en passant : `_slug()` de `theme.py` passait par
  `NFKD`, qui **ne décompose pas les ligatures** — « vœux » devenait « vux »
  dans le nom de fichier. Les ligatures sont maintenant écrites en toutes
  lettres avant la normalisation. Aucun autre module n'est touché : aucun titre
  de séance existant ne contient de ligature (vérifié sur les 160 fichiers de
  `decks/`).
- `Deck.capture()` attend un **identifiant d'exercice**, pas un titre libre, et
  demande une capture produite par `captures.py`. Seul `module-sante` en
  utilise ; la diapositive prévue pour E1 a été refaite en cartes.

## Module 11 — terminé

Contenu, build, médias, seize séances, seize fiches, dépôt à jour, poussé en
production.

## Module 12 — Trouver son chemin

- **Scénario** : Nour, arrivée de Syrie il y a huit mois, cherche une adresse,
  puis un hôpital en métro, puis explique le chemin à Patrice. Sept dialogues,
  quinze mots, vingt-trois exercices, six mini-leçons.
- **Grammaire** : la chute des consonnes finales · l'impératif · jusqu'à, vers,
  par · les repères de lieu · celui, celle, ceux · la lecture d'un horaire et
  d'un plan. Aucun de ces six points n'était traité ailleurs.
- **Couleur** : ambre `#B45309` / `#FBEEDC`. **Activité** : 49.
- Médias : 21 images (0,71 $), 182 MP3. Contrôle : les **203 URL** que la page
  peut demander répondent toutes.
- Séances : 16 présentations, 187 diapositives, 16 fiches (144 blocs).
  `MODULE 12` dans les seize `.pptx`.
- Le serveur gagne un troisième scénario de jeu de rôle, aux rôles « perdu » et
  « guide ».

### Deux garde-fous du socle qui ont servi

- `theme.py` **refuse un caractère absent de Verdana** : le symbole phonétique
  du « r » aurait été projeté en carré vide. Remplacé par « le r final ».
- `theme.py` **refuse un tableau trop chargé** pour une diapositive projetée.
  Deux tableaux ont dû être scindés ou allégés. Ces deux contrôles valent mieux
  qu'une relecture : ils ne se fatiguent pas.

### Une situation sans production écrite au programme

« Déplacement dans une ville » ne porte **aucune intention de production
écrite** — seulement CO, PO et CE. Le module en propose une quand même (écrire
les indications pour venir chez soi), parce que l'architecture des modules en
prévoit une et que les attentes de fin de cours du niveau demandent un court
texte suivi. À signaler à l'utilisateur plutôt qu'à décider seul.


## Module 13 — S'inscrire à une activité

- **Scénario** : Rosa, arrivée de Colombie il y a un an, inscrit son garçon à
  la natation, puis se cherche une activité pour elle. Sept dialogues, quinze
  mots, vingt-deux exercices, sept mini-leçons.
- **Grammaire** : entendre les chiffres (70, 80, 90 et le piège de soixante) ·
  il faut / il est important que · le superlatif · l'impératif avec un pronom ·
  chaque, plusieurs, quelques · lire un dépliant · le registre familier contre
  le registre standard. Tous neufs dans la collection.
- **Couleur** : vert `#166534` / `#E3F1E7`. **Activité** : 50.
- Médias : 21 images (0,71 $), 200 MP3. Les **221 URL** de la page répondent.
- Séances : 16 présentations, 190 diapositives, 16 fiches (148 blocs).
  `MODULE 13` dans les seize `.pptx`.
- Cinquième scénario de jeu de rôle, aux rôles « parent » et « prepose ».

### Une faute qui rendait la page muette

Le titre du module commence par « S'inscrire ». Cette apostrophe, injectée
dans `el.innerHTML='…'`, a cassé **tout le script de la page** — qui a continué
de s'afficher, sans exercices, sans mini-leçons, sans rien. Le seul symptôme
visible était que les constantes n'existaient plus.

`build/module.py` **refuse maintenant** une apostrophe non échappée dans
`bravo` ou `relance`, avec le message qui dit quoi écrire. Le contrôle utile
n'est pas « la page s'affiche » mais « les constantes existent » — c'est
désormais la première chose que vérifie le relevé fait dans le navigateur.

## Module 14 — Faire l'épicerie

- **Scénario** : Farida, arrivée du Maroc il y a deux ans, cherche un produit,
  s'informe sur la conservation, commande à trois comptoirs, puis apprend à
  lire une étiquette et un mode d'emploi. Sept dialogues, quinze mots,
  vingt-deux exercices, sept mini-leçons.
- **Grammaire** : la liaison des quantités (deux œufs) · du, de la, des · ça se
  garde · le pronom en · livres, kilos et grammes · les trois lignes d'une
  étiquette · un mode d'emploi en trois blocs. Tous neufs dans la collection.
- **Couleur** : teal `#0D7A6F` / `#DCF2EF`. **Activité** : 51.
  (Elle était violette. Le violet `#6B4FBB` est devenu la couleur de la marque
  francis, qui le veut exclusif : il ne sert plus au repérage.)
- Médias : 21 images (0,71 $), 204 MP3. Les **225 URL** de la page répondent.
- Séances : 16 présentations, 194 diapositives, 16 fiches (150 blocs).
  `MODULE 14` dans les seize `.pptx`.
- Sixième scénario de jeu de rôle, aux rôles « client » et « commis ».

### Le thème du module a cassé la page

Le thème de ce module est « Achat d'aliments ou de produits d'entretien ».
Deux apostrophes — et le gabarit injecte `%%THEME%%` dans
`fd.append('theme','…')`, une chaîne JavaScript à guillemets simples. Tout le
script de la page est mort, et la page a continué de s'afficher, muette.

Le garde-fou posé au module 13 ne couvrait que `bravo` et `relance`. Il est
maintenant **généralisé** : `build/module.py` regarde le gabarit, repère les
jetons qui y sont entourés de guillemets simples, et refuse toute valeur
contenant une apostrophe non échappée. Plus de liste de champs à tenir à jour.

### Trois sessions dans le même dépôt

Pendant la production de ce module, deux autres sessions travaillaient dans
`bibliotheque-francisation` : l'une sur une banque de présentations (commitée),
l'autre sur une marque « francis » greffée dans `build/gabarit/module.html` et
dans les quatorze modules produits. Conséquences, et ce qui a été fait :

- **Ne pas lancer `build/gabarit.py`** tant que la greffe de marque n'est pas
  intégrée : le script régénère le gabarit depuis `module-consultation` et
  effacerait le travail de l'autre session. Les deux sessions ont été prévenues.
- `build/module.py` accepte désormais **`--gabarit <chemin>`**, pour bâtir sur
  une autre copie du moteur — par exemple celle du dernier commit, quand une
  session modifie celle du dépôt.
- La marque a été **retirée du HTML de ce module avant le commit** : elle n'est
  pas encore commitée par la session qui la pose, et ce n'est pas à ce chantier
  de la mettre en production à sa place.
- **Ne plus utiliser `git add -A`** dans ce dépôt tant que plusieurs sessions y
  travaillent : il emporterait le travail en cours des autres.

### Un défaut du gabarit, à corriger quand il sera libre

`build/gabarit/module.html`, ligne ~2233 :

```
fd.append('taskLabel','Production orale — décrire une douleur');
fd.append('question','Décrire une douleur à un professionnel de la santé');
```

Un reste de `module-consultation`, jamais transformé en jeton. **Les six
modules bâtis par la nouvelle chaîne** — consultation, relations, deplacement,
activite, alimentation, probleme — envoient donc tous ce libellé au dépôt de
l'enseignant avec leur production orale. Les neuf plus anciens, écrits à la
main, n'ont pas le défaut.

La ligne 3529 (dépôt de l'écrit) montre la bonne façon de faire : elle calcule
`libelle()` et `consigne()` depuis la carte de production plutôt que de les
figer. Le correctif attend que la session qui travaille sur le gabarit ait
fini.

## Module 15 — Acheter un appareil

- **Scénario** : Yin, arrivée de Chine il y a trois ans, achète une laveuse
  pour un local de sous-sol d'un mètre de large. Elle compare deux modèles,
  découvre ce que couvre la garantie, et apprend qu'un mode d'emploi de
  quarante pages en contient quatre d'utiles. Sept dialogues, quinze mots,
  vingt-deux exercices, sept mini-leçons.
- **Grammaire** : le son de « un » contre celui de « pain » · la place et
  l'accord de l'adjectif · ce, cet, cette contre celui, celle · ce que couvre
  une garantie · le futur proche et le futur simple · le prix affiché et le
  total réel · les quatre pages utiles d'un mode d'emploi.
- **Couleur** : bleu `#1D6B8F` / `#E7F0F6`. **Activité** : 52.
- Médias : 21 images (0,71 $), 210 MP3. Les **231 URL** de la page répondent.
- Séances : 16 présentations, 192 diapositives, 16 fiches (149 blocs).
  `MODULE 15` dans les seize `.pptx`.
- Septième scénario de jeu de rôle, aux rôles « acheteur » et « vendeur ».
- La marque francis a de nouveau été retirée du HTML avant le commit : la session
  qui la pose regreffe les fichiers produits, et son travail n'est toujours pas
  commité.


## Module 16 — Au restaurant

- **Scénario** : Andrés, arrivé du Pérou il y a deux ans, invite une collègue
  pour la remercier. C'est son premier repas assis dans un restaurant d'ici.
  Sept dialogues, quinze mots, vingt-deux exercices, six mini-leçons.
- **Grammaire** : le « e » qui tombe — pour comprendre un serveur qui parle
  vite · l'accueil et ses trois questions · les quatre formules du menu · je
  voudrais, pourriez-vous, ce serait possible · demander et signaler pendant le
  repas · les taxes et le pourboire.
- **Couleur** : teal `#0D7A6F` / `#DCF2EF`. **Activité** : 53.
- Médias : 21 images (0,71 $), 193 MP3. Les **214 URL** de la page répondent.
- Séances : 16 présentations, 196 diapositives, 16 fiches (150 blocs).
  `MODULE 16` dans les seize `.pptx`.
- Huitième scénario de jeu de rôle, aux rôles « client » et « serveur ».

### Deux points culturels traités de front

Le module ne se contente pas du vocabulaire. Deux usages du Québec sont
expliqués parce qu'ils déroutent et qu'ils coûtent :

- **Le pourboire fait partie du revenu du personnel de service.** Il n'est
  jamais sur l'addition, il s'ajoute — environ 15 % du montant avant taxes. La
  méthode de calcul mental (le dixième, plus sa moitié) est enseignée deux fois.
- **Signaler n'est pas se plaindre.** Un plat froid se dit, et le restaurant
  préfère le savoir. Le module montre aussi la nuance : on peut signaler sans
  exiger de correction — « je préfère vous le dire ». Les deux séances qui en
  traitent comparent les usages sans les hiérarchiser.

## Module 18 — `module-vetements` · Acheter des vêtements

Situation du programme : « Achat de vêtements », niveau 4. Une seule intention
de communication au programme (s'informer sur un vêtement) ; le module a été
étoffé avec le lexique de la situation — entretien, tailles, essayage, échange,
remboursement, mise de côté — pour tenir les seize séances, sur décision de
l'utilisateur.

**Scénario.** Kofi, arrivé du Ghana il y a trois ans, a passé deux hivers avec
un manteau trop léger. Il en achète un vrai. Diane, une amie, lui donne son
avis ; VALÉRIE, conseillère, lui apprend à lire l'étiquette du col ; RÉMI, au
service à la clientèle, échange les bottes de son fils.

**Points de langue** (six mini-leçons, aucun doublon avec les onze autres
modules) :

- `prPhon` — le féminin qu'on entend : le -e réveille la consonne finale.
- `t1taille` — dire ce qui ne va pas : degré + adjectif + endroit.
- `t1decrire` — décrire un vêtement : l'adjectif suit le nom, la couleur
  s'accorde, les couleurs invariables.
- `t2opinion` — je trouve que, il me semble, à mon avis ; le pronom devant
  « aller ».
- `t2entretien` — les cinq symboles du col, la croix qui veut dire non.
- `t3echange` — échange, remboursement, note de crédit, mise de côté ; les
  quatre conditions.

**Médias.** 21 images fal.ai (0,71 $), dont `bottes-hiver.jpg` réencodée de
740 à 150 Ko. 193 MP3 ElevenLabs. Contrôle des URL : 214 demandées par la page,
214 présentes.

**Défauts trouvés et corrigés.**

- Deux entêtes de tableau écrits sans apostrophe (« Ce quon fait ») par
  prudence inutile : `theme.py` accepte très bien l'apostrophe, elle a été
  remise.
- `c3.py` pointait vers `etiquette-entretien.jpg` ; l'image produite s'appelle
  `etiquette-col.jpg`. Le build s'arrête proprement sur un `FileNotFoundError`
  de Pillow — c'est le bon comportement.
- Le délai de mise de côté disait « trente jours » en D2 alors que la carte
  mémoire dit quatorze. Aligné sur « souvent quatorze jours, parfois trente ».
- La greffe d'identité de marque (travail d'une autre session, non commité)
  ajoutait un bandeau francis dont le CSS n'est pas encore au dépôt. Les deux
  régions marquées ont été retirées du HTML avant le commit, comme pour les
  six modules précédents.
