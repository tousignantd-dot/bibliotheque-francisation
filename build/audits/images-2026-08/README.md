# Audit des images — août 2026

Les **1 502 images générées** des modules (`assets/interactive/*/images` et
`*/vocab`), passées en revue les 29 et 30 août 2026. Ce dossier garde les
**jugements** : ce qui ne se rebâtit pas. Les miniatures, les lots distribués
aux agents et les pages HTML se refabriquent tous à partir d'ici.

## Comment il a été mené

Trois passages, chacun ne voyant que ce que le précédent a levé.

1. **Lecteur** — 33 agents, un par groupe de modules, qui ratissent tout et
   lèvent la main. 387 doutes sur 1 502. → `verdicts/`
2. **Vérificateur** — 13 agents qui ne voient que les 387, et **blanchissent**
   ou confirment. 187 doutes tombent. → `verifications/`
3. **Arbitre** — 6 agents sur les 91 bloquantes seulement, qui tranchent en
   dernier ressort **et écrivent la correction de prompt à appliquer**. Ils
   rétrogradent un bloquant sur deux. → `arbitrages/`

Puis la reprise : 10 agents reportent les corrections dans les
`gen_images.py` (→ `reprises/`), et 102 images sont refaites.

## La règle qui décide de tout : 223 px

C'est la largeur réelle de `.imgzone` chez l'élève. Le vérificateur ouvre
chaque image **deux fois** — l'original de 1 200 px et une réduction à 223 px.
Un texte qu'on déchiffre en scrutant l'original et qui redevient un pâté gris
à l'écran **ne gêne personne** : le défaut n'existe pas dans l'usage. Cette
seule règle a écarté 187 des 387 doutes.

Trois exceptions se jugent sur l'original, quelle que soit la taille : une
**marque réelle** (STM, IGA, Visa…), un **visage reconnaissable**, une image
**hors sujet**.

## Les fichiers

| fichier | ce qu'il contient |
|---|---|
| `travail.json` | les 1 502 images, avec mot, énoncé et prompt **d'avant la reprise** |
| `verdicts/` | le premier passage, un fichier par lot, une entrée par image |
| `verifications/` | le second passage, sur les 387 doutes |
| `arbitrages/` | le troisième, sur les 91 bloquantes, avec la correction de prompt |
| `reprises/` | ce que chaque prompt est devenu — `avant`, `apres`, `note` |
| `reprise.json` | les 102 images refaites |
| `consigne*.md` | les consignes données aux agents, dans l'ordre des passages |

`travail.json` garde les prompts **tels qu'ils étaient avant la reprise** :
c'est la trace de ce qui a été jugé. Les prompts d'aujourd'hui sont dans les
`gen_images.py`, et `build/audit_images_releve.py` les en ressort.

## Refaire les pages

    python3 build/audit_images_page.py build/audits/images-2026-08
    python3 build/audit_avant_apres.py build/audits/images-2026-08

La seconde ressort les images « avant » de l'historique git : elle ne marche
que tant que le commit `f7de3c75b` reste atteignable.

## Ce qui reste ouvert

- **101 images en doute**, sur `assets/presentations/audit-images.html` : leur
  prompt n'a pas bougé, les régénérer telles quelles serait relancer le même
  dé. 61 gênantes, 40 mineures, aucune bloquante.
- **La carte d'assurance maladie** de `vocab-flash-sante` est devenue une carte
  bleue nue : conforme à la règle de ne pas faire dessiner un document
  officiel, mais le mot ne s'en devine plus.
- Les **1 238 vignettes** de `assets/vignettes/` n'ont pas été auditées : ce
  sont des captures de diapositives, pas des images générées.
