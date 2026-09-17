# « Place ce que j'entends » — les cinq exercices de placement (niveau 2)

L'élève écoute une description, pose chaque image au bon endroit **et de la
bonne couleur**, puis vérifie. Contrairement aux exercices de dessin, la
réponse se corrige toute seule et remonte au direct de la classe.

    python3 build/places/fabrique.py      → reconstruit les cinq dans places/

Puis on dépose le contenu de `places/<slug>/` dans
`assets/interactive/<slug>/`, **sans toucher à `fiche-eleve.pdf`** : la fiche
imprimable ne change pas et ne reçoit pas de corrigé (décision de
l'enseignant, 17 septembre 2026).

## Les fichiers

| | |
|---|---|
| `scenes.py`   | zones, banques et réponses des cinq scènes. **C'est le seul fichier à modifier** pour changer une tenue, une couleur ou une case. |
| `couleurs.py` | la palette et ses accords — « une tasse bleue », jamais « une tasse bleu ». |
| `gabarit.py`  | le HTML et le JavaScript, **communs aux cinq**. Une correction ici les corrige toutes. |
| `fabrique.py` | masques, audio, assemblage. |

## Ce qu'il faut savoir avant d'y toucher

**Les zones se posent à l'œil, pas au jugé.** Les tracer sur l'image avec PIL,
enregistrer un PNG, et le regarder. Une case « sur la table » qui mord sur la
nappe qui tombe enseigne le contraire de ce qu'on veut.

**Les couleurs se posent dans la couche alpha.** Un masque CSS lit l'alpha, pas
les niveaux de gris : des masques opaques partout ne découpent rien et donnent
un rectangle de couleur. L'intérieur d'un objet se trouve en inondant depuis
les **bords de l'image** — ce qu'on atteint est le dehors.

**Les dessins sont recadrés sur leur encre.** Sans ça, la taille apparente
dépend du cadrage : la fourchette occupe 15 % de son image, la tasse 71 %.

**`ajuste`** vaut `"zone"` quand l'objet doit *couvrir* (un vêtement sur un
personnage : l'objet remplit sa case) et `"fixe"` ailleurs, où un objet garde
la même taille d'une case à l'autre.

**Un objet ne peut pas servir deux fois** dans une scène : le poser une
seconde fois le retire de sa case précédente.

**L'audio ne se refait que s'il manque.** Si vous changez une phrase, effacez
les `desc-*.mp3` et `description-*.mp3` correspondants, sinon la page décrira
l'ancienne scène pendant que la correction en attend une autre.

**Glisser-déposer ET clic-clic.** Le glisser a été demandé par l'enseignant ;
le clic reste indispensable, car les événements de glisser HTML5 n'existent ni
sur tablette ni sur téléphone.

`_decoupe_silhouette.py` découpe les vêtements dans la silhouette elle-même.
Essayé puis abandonné : une découpe étiquetée « des souliers » montre des
pieds nus. Gardé parce que la technique peut servir ailleurs.
