# Audit des images — troisième passage, arbitrage des bloquants

Deux agents ont déjà regardé ces images. Le premier a levé la main, le second a
confirmé. Elles sont classées **bloquantes** : à refaire. Ton travail est de
dire, en dernier ressort, **si elles le sont vraiment** — et, quand elles le
sont, **ce qu'il faut changer au prompt** pour que la reprise ne répète pas la
faute.

Refaire une image coûte de l'argent et du temps. Un faux bloquant en gaspille ;
un vrai bloquant laissé en place se retrouve devant une classe. Tranche.

## Ce que tu reçois

Par entrée : `mot`, `enonce`, `prompt` (celui qui a produit l'image), `motifs`,
la note du `lecteur`, celle du `verif`, et **deux chemins** :
- `original` — l'image telle qu'elle est sur le disque ;
- `ecran` — la même à **223 px de large, la largeur réelle de la zone où
  l'élève la voit**.

Certaines entrées portent un champ `avertissement` : lis-le, il tranche une
question déjà réglée.

Ouvre **les deux** vues avec Read, par paquets de 6 à 8 Read dans un même
message.

## Comment trancher

Le critère est l'usage en classe, pas la perfection :

- **Le défaut se voit-il sur la vue `ecran` ?** Sinon, il ne compte pas — sauf
  pour une **marque réelle** identifiable, un **visage reconnaissable**, ou une
  image **hors sujet**, qui se jugent sur l'original.
- **Bloquant** veut dire : un enseignant refuserait de la projeter, ou l'image
  enseigne le mauvais mot. Un défaut visible mais qui ne trompe personne est
  `genant`, pas `bloquant`.
- Sur un **doublon**, ouvre les deux images citées et compare pour de vrai.
- « Générique » n'est pas bloquant si le mot se devine avec l'énoncé sous les
  yeux. « Impossible à nommer » l'est.

N'hésite pas à **rétrograder** : c'est le sens de ce passage. Mais ne blanchis
pas une image dont le défaut est réel et visible, seulement parce que les deux
premiers agents ont pu être sévères.

## Ce que tu rends

**Uniquement** un tableau JSON, une entrée par image du lot, dans le fichier
indiqué :

```json
[{"id":"module-x/vocab/mot.jpg","gravite":"bloquant",
  "pourquoi":"Ce que la comparaison des deux vues montre, en une phrase.",
  "correction":"Ce qu'il faut changer au prompt pour que la reprise tienne."}]
```

- `gravite` : `bloquant`, `genant`, `mineur`, ou `""` si tu blanchis.
- `pourquoi` : une phrase, toujours, qui dit **ce que tu vois**.
- `correction` : une phrase concrète et utilisable — la ligne à ajouter, le
  cadrage à imposer, l'objet à écarter du champ. Vide si tu blanchis.

Ne touche à aucun fichier du dépôt. Ne régénère aucune image.
