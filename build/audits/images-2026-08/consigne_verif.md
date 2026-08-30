# Audit des images — second passage, vérification

Un premier lecteur a levé la main sur ces images. **Ton travail n'est pas de
refaire le sien : c'est de le contredire quand il a tort.** Beaucoup de ses
doutes ne tiendront pas. Tu blanchis sans hésiter ; tu ne confirmes que ce que
tu vois vraiment.

## Le point de méthode qui change tout : la taille d'affichage

Chaque entrée porte **deux chemins** :
- `original` — l'image telle qu'elle est sur le disque, 800 à 1200 px ;
- `ecran` — la même, réduite à **223 px de large, la largeur réelle de la zone
  où l'élève la voit** dans le module.

Ouvre les deux avec Read. Un texte qu'on déchiffre en scrutant l'original de
1200 px peut n'être qu'un pâté gris à 223 px — et alors **il ne gêne
personne** : le défaut n'existe pas dans l'usage. Le critère est simple :

> **Le défaut se voit-il encore sur la vue `ecran` ?** Si non, l'image est
> blanchie, quel que soit ce qu'on lit sur l'original.

Trois exceptions, où l'on tranche sur l'original même si l'écran l'atténue :
1. une **marque réelle** identifiable (STM, IGA, Visa, Epson, Dell…) — c'est
   un problème juridique et de neutralité, pas de lisibilité ;
2. un **visage reconnaissable** — c'est un problème de droit à l'image ;
3. une image **hors sujet** — la taille n'y change rien.

## Les autres motifs

- `hors-sujet` / `ambigu` — pose-toi la question de l'élève : en voyant cette
  image, peut-il nommer LE mot ? S'il le peut, blanchis, même si le lecteur a
  trouvé la scène imparfaite. « Trop générique » n'est pas un défaut si le mot
  se devine.
- `texte` — applique la règle de la taille d'affichage. Une écriture floue,
  des lignes grises, un titre plus gras mais indéchiffrable : c'est **voulu**,
  beaucoup de prompts le demandent explicitement. Relis le `prompt` avant de
  confirmer.
- `decor` — ne confirme que si le décor **contredit** la scène demandée, pas
  s'il est simplement quelconque.
- `doublon` — ouvre les deux images citées et compare pour de vrai.
- `anatomie`, `technique` — confirme seulement si c'est visible à 223 px.

## Ce que tu rends

**Uniquement** un tableau JSON, une entrée par image du lot, écrit dans le
fichier de sortie indiqué :

```json
[{"id":"module-x/vocab/mot.jpg","verdict":"ok",
  "motifs":[],"gravite":"","note":"",
  "pourquoi":"Le mot « SORTIE » ne se lit plus du tout à 223 px."}]
```

- `verdict` : `ok` si tu blanchis, `doute` si tu confirmes.
- Quand tu confirmes, rends `motifs`, `gravite` (`bloquant` / `genant` /
  `mineur`) et `note` — corrige ceux du lecteur si tu n'es pas d'accord, y
  compris à la hausse.
- `pourquoi` : une phrase, toujours, blanchi ou confirmé, qui dit ce que la
  comparaison des deux vues t'a montré.

Ne touche à aucun fichier du dépôt. Ne régénère aucune image.
