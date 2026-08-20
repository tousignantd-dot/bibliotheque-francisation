# Un premier module pour chaque niveau

Mandat du 20 août 2026. Le niveau 4 compte dix-huit modules ; les sept autres
niveaux n'en ont aucun. Ce chantier produit **un module par niveau** — le
premier — pour vérifier que la chaîne de production tient à tous les stades,
du débutant qui apprend à se présenter à l'avancé qui suit l'actualité.

## Ce que l'utilisateur a tranché

1. **Les situations sont choisies par moi**, une par niveau (tableau plus bas).
2. **Le format s'adapte aux niveaux 1 et 2** : huit séances, deux défis, deux
   blocs de quatre heures. Les niveaux 3 et 5 à 8 gardent le format du niveau
   4 : seize séances, trois défis.
3. **Médias et mise en ligne autorisés** : images fal.ai, MP3 ElevenLabs, et
   `git push` au fur et à mesure. Estimation : 25 $ à 40 $ pour les sept.

## Les sept modules

| Niveau | Situation retenue | Slug prévu | Format | Pourquoi elle |
|--------|-------------------|------------|--------|---------------|
| 1 | Relations sociales | `n1-relations` | 8 séances | 4 intentions sur 9 ; se présenter est le premier besoin de tous |
| 2 | Déplacement dans une ville | `n2-deplacement` | 8 séances | 4 intentions ; concret, visuel, immédiatement utile |
| 3 | Achat d'aliments ou de produits d'entretien | `n3-alimentation` | 16 séances | 8 intentions, la plus riche du niveau |
| 5 | Location d'un logement | `n5-logement` | 16 séances | 4 intentions ; la démarche la plus lourde d'une installation |
| 6 | Recherche d'emploi | `n6-emploi` | 16 séances | 4 intentions ; le tournant du stade intermédiaire |
| 7 | Suivi de l'actualité | `n7-actualite` | 16 séances | 6 intentions ; compréhension de discours longs |
| 8 | Emploi | `n8-emploi` | 16 séances | 10 intentions, de loin la plus dense du programme |

Les situations se répètent d'un niveau à l'autre dans le programme lui-même —
« Relations sociales » existe aux niveaux 1, 2, 3, 4 et 6. Ce n'est pas une
redite : les intentions de communication changent complètement. Au niveau 1 on
se présente ; au niveau 6 on exprime un désaccord dans un groupe.

## L'ordre de production, et pourquoi

1. **Niveau 3** — le voisin immédiat du 4. Aucune inconnue : c'est le format
   connu, à peine simplifié. Il donne un livrable rapidement et confirme que
   la chaîne accepte un autre niveau que le 4.
2. **Niveau 1** — la vraie inconnue du chantier : format court, stade
   débutant, très peu de lexique disponible. À affronter tôt plutôt que tard.
3. **Niveau 2** — profite de tout ce que le niveau 1 aura appris.
4. **Niveau 5**, puis **6**, **7**, **8** — de plus en plus longs et abstraits ;
   le lexique du programme s'amenuise à mesure qu'on monte, et le contenu
   s'invente davantage.

## Le socle technique à poser avant le niveau 1

- **Une grille de huit séances** dans `build/powerpoints/modules.py` :
  `GRILLE_COURTE = a1 a2 a3 b1 b2 c1 c2 e1`, deux blocs de quatre. Les deux
  grilles existantes (`GRILLE_3_DEFIS`, `GRILLE_2_DEFIS`) font seize séances
  chacune ; c'est une troisième, pas une modification.
- **La numérotation par niveau.** Aujourd'hui `numero` est unique et l'ordre
  d'affichage s'y fie. Sept modules qui portent tous le numéro 1 vont se
  télescoper : il faudra trier par `(niveau, numero)` dans `ORDRE` et vérifier
  le portail. C'est le seul point qui touche du code partagé.
- **Le nombre de sections n'est pas un problème** : il vit dans `sections.js`,
  donc dans le contenu. Un module à cinq sections ne demande rien au gabarit.

## Ce que le programme donne, et ce qu'il faut chercher ailleurs

Le programme donne la spécification complète : intentions, savoirs, lexique,
critères. Il ne donne aucun fait du monde réel. Pour les modules qui reposent
sur une procédure — le bail du niveau 5, l'assurance emploi du niveau 8 — il
faut vérifier les faits québécois (montants, délais, noms d'organismes) plutôt
que les inventer. Ces vérifications se font au coup par coup, sur les sites
officiels, et se notent ici.

## Journal

_(une section par module, remplie à mesure)_
