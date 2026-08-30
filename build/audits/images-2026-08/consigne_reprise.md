# Reprise des prompts d'images — appliquer les corrections dans les fichiers

Un audit a jugé les images des modules. Pour chacune de celles de ton lot, un
arbitre a écrit **ce qu'il faut changer au prompt** pour que la reprise ne
répète pas la faute. Ton travail : **reporter ces corrections dans les
fichiers**. Tu n'écris pas de nouvelles images, tu n'exécutes rien.

## Où

Chaque entrée porte `module` et `nom`. Le prompt vit dans
`/Users/danieltousignant/Claude/bibliotheque-francisation/build/contenu/<module>/gen_images.py`,
dans la liste `IMAGES`, sous la forme :

```python
 ('<nom>', '<dossier>', P_VOC, STYLE + " La phrase qui décrit la scène."),
```

`STYLE`, `PERS` et leurs variantes sont des constantes partagées par tout le
module : **n'y touche pas**, sauf si la correction le demande explicitement.
Ce que tu modifies, c'est la phrase propre à cette image.

**Un seul agent travaille sur tes modules. Ne touche à aucun fichier d'un
module absent de ton lot.**

## Comment

Lis `correction` — c'est la consigne — et `diagnostic`, qui dit ce qui cloche
dans l'image actuelle. Réécris la phrase de scène en conséquence.

Ce que l'audit a établi, et qui vaut partout :

- **Cadrer plutôt que nier.** « Aucun texte lisible » n'a jamais tenu devant un
  objet qui *porte* une inscription : le modèle écrit quand même. Il faut
  sortir l'écriture du champ — bord haut qui coupe l'en-tête, face écrite
  tournée en trois quarts arrière, enseigne au-dessus du cadre.
- **Interdire l'objet par son nom quand le mot l'appelle.** Dire « aucun logo »
  ne suffit pas : « carte » fait apparaître une VISA. Écrire « aucune carte de
  plastique à logo dans le champ ».
- **Ne pas reprendre dans le prompt un mot polysémique de l'énoncé.**
  « Lettres » a produit un alphabet ; décrire la forme.
- **Décrire la posture, pas l'atmosphère.** « Penchée en avant, front dans la
  main », pas « atmosphère de malaise ».
- **Vider le cadre de tout second document** : une feuille de texte parasite au
  premier plan mange le sujet.
- **Un pictogramme n'est pas du texte** : le symbole normalisé est permis et
  débloque des mots autrement inillustrables.
- **Interdire nommément la marque** dès qu'un appareil entre dans le champ
  (« boîtier nu, aucun nom de fabricant »).

Garde le ton et la longueur des autres prompts du fichier : une à trois
phrases, concrètes, qui décrivent ce qu'on voit. Le français du dépôt.

## Contrôle

Après tes modifications, lance :

```
python3 -m py_compile build/contenu/<module>/gen_images.py
```

pour chaque module touché, depuis
`/Users/danieltousignant/Claude/bibliotheque-francisation`. Le fichier doit
compiler. **N'exécute jamais `gen_images.py` lui-même** : il appelle une API
payante.

## Ce que tu rends

Un tableau JSON dans le fichier de sortie indiqué, une entrée par image :

```json
[{"id":"module-x/vocab/mot.jpg","fait":true,
  "avant":"la phrase de scène telle qu'elle était",
  "apres":"la phrase de scène telle que tu l'as écrite",
  "note":"ce que ta réécriture change, en une phrase"}]
```

`fait` vaut `false` si tu n'as pas trouvé l'entrée dans le fichier — dis-le
dans `note` plutôt que d'inventer.
