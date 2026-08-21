# Module 62 — « Un dégât d'eau » (niveau 5, `module-n5-degat`)

Journal de production, 21 août 2026. Vague 2 de `docs/vagues-suivantes.md`,
deuxième module du niveau 5. Activité **62**, `numero` 2, seize séances en
trois défis.


## Ce qui distingue ce module de son voisin du niveau 4

Le module 10 du niveau 4 (`module-probleme`) **signale** un problème au
propriétaire par téléphone et s'arrête à la promesse de réparation ; celui-ci
**lit l'avis officiel** affiché dans l'entrée — la seule intention que le
programme donne à cette situation au niveau 5 —, relate le sinistre au passé
composé et à l'imparfait, et mène la démarche jusqu'au bout : réduction de
loyer et réclamation d'assurance.

C'est `build/cadre.py 5 "Problèmes reliés à l'habitation"` qui a tranché. La
situation n'a **qu'une intention de communication** au niveau 5, en
compréhension écrite : *lire un avis*. Elle n'a **aucun lexique** — le document
de Laval ne couvre pas cette situation-là —, donc les dix-sept mots du banc
sont inventés à partir des intentions et des savoirs du cours. Le défi 2 est
bâti autour de cette unique intention plutôt que d'en faire un passage :
quatre séances entières (C1 à C4) sur la lecture d'un avis et sur la langue
qui l'écrit.

Coïncidence mesurée avec `module-probleme` : **1,1 %** (3 énoncés sur 269), et
les trois sont des consignes génériques — « Écoutez de nouveau le dialogue,
puis répondez » — plus le mot *une infiltration*. Bien en dessous du seuil de
5 % de `docs/verification-originalite.md`.


## Le scénario et les personnages

Mariama Baldé loue un quatre et demie au deuxième étage d'un immeuble de six
logements, au 118 rue Sainte-Hélène, à Longueuil. Un matin de novembre, l'eau
tombe du plafond de sa chambre : le chauffe-eau de sa voisine du dessus, un
réservoir de quinze ans, a lâché pendant la nuit.

| Personnage | Rôle | Voix |
|---|---|---|
| **Mariama Baldé** | la locataire | féminine #2 |
| **Kim** (Thi Kim Nguyên) | la voisine du dessus | enseignante |
| **Réjean Cloutier** | le propriétaire de l'immeuble | masculin #1 |
| **Sylvie Painchaud** | agente en assurance habitation | enseignante |

Kim et Sylvie partagent une voix : elles ne se répondent jamais — Kim tient
`prep` et `t2`, Sylvie seulement `t3`.


## Le découpage

| Section | Titre | Ce qu'on y fait |
|---|---|---|
| `prep` | Je découvre | nommer les dommages, les quatre gestes des premières heures |
| `t1` | Défi 1 · Le constat | relater le sinistre, décrire pièce par pièce, écrire le courriel |
| `t2` | Défi 2 · L'avis | lire l'avis affiché, en tirer ses obligations |
| `t3` | Défi 3 · La réclamation | argumenter, demander une compensation, suivre la démarche |
| `appli` | Je me lance | jeu de rôle, récit oral, lettre de demande de réduction |
| `retiens` | Je retiens des mots | les dix-sept mots du banc |

Dix-neuf exercices plus le banc de vocabulaire, **dix mini-leçons**, quatre
dialogues (62 répliques), dix-sept cartes de vocabulaire.


## La progression grammaticale

Sept points, tous pris dans les savoirs du niveau 5, chacun avec son exercice
**et** sa mini-leçon :

| Section | Point | Clé |
|---|---|---|
| `prep` | le son [o] et ses trois graphies (eau, au, o) | `prSon` |
| `prep` | décrire un dégât : quoi, où, quelle taille | `prDegat` |
| `t1` | imparfait / passé composé pour relater un sinistre | `t1temps` |
| `t1` | le gérondif (simultanéité et manière) | `t1ger` |
| `t2` | lire un avis officiel | `t2sens` |
| `t2` | l'impersonnel, le passif, « veuillez » | `t2imperso` |
| `t2` | le subjonctif présent et ses quatre déclencheurs | `t2subj` |
| `t3` | les phrases emphatiques | `t3emph` |
| `t3` | cause et conséquence, le deux-points explicatif | `t3conn` |
| `t3` | écrire une demande qui aboutit | `t3lettre` |

Deux points de ponctuation nommés dans les attentes de fin de cours du
niveau 5 sont traités explicitement : le **deux-points qui annonce une cause**
et la **virgule après une subordonnée placée en tête de phrase**.


## Un scénario de jeu de rôle à part : `degat`

Le scénario `probleme` du niveau 4 existait, et il a été examiné avant d'en
écrire un autre. Il ne tient pas à l'intermédiaire : sa conduite dit au
locataire d'exposer son problème « en une ou deux phrases », puis de laisser
l'élève poser ses questions, et l'échange se clôt sur une entente de
réparation. Au niveau 5, l'élève doit tenir un **échange suivi** — raconter au
passé, décrire pièce par pièce, argumenter, demander une compensation.

D'où `JEU_DE_ROLE_DEGATS` et l'entrée `"degat"` dans `server.py` : trois cas
(`plafond`, `soussol`, `laveuse`), deux rôles (`locataire`, `proprietaire`),
sept sujets à couvrir. La conduite du propriétaire porte la contrainte qui
fait travailler l'élève : **il ne propose jamais d'argent le premier**, et
répond « on verra » à une demande sans raison ni chiffre.

Les identifiants de cas et de rôles ont été vérifiés des deux côtés —
`custom.js` et `server.py` s'accordent, et le `jr_cas` du manifeste (`plafond`)
existe bien côté serveur. Rien ne vérifie cela automatiquement : le module se
construit sans erreur même si la clé manque, et le jeu de rôle échouerait
seulement chez l'élève.


## Les médias

**Images — 20, environ 0,68 $** (fal.ai, `nano-banana-2`, format 3:2). Huit
illustrations pour l'exercice `prImg`, douze photos de vocabulaire réduites à
800 px. Le dosage a demandé un mot dans les prompts : un dégât d'eau se
photographie facilement en catastrophe spectaculaire, ce qui n'aide pas à
reconnaître un cerne ou une latte gondolée. Les prompts demandent donc des
dommages **ordinaires, nets et lisibles**.

**Audio — 241 extraits** (62 répliques + 179 sons). ElevenLabs a coupé la
liaison TLS (`SSLEOFError`) par intermittence toute la journée du 21 août,
comme le 20. Le générateur `generer_audio_module_n5_degat.py` reprend cinq
fois en doublant l'attente et **saute ce qui existe déjà** : il se relance
sans précaution.

    python3 generer_audio_module_n5_degat.py

Aucun `AUDIO_V` à incrémenter : ce sont des fichiers neufs, pas des fichiers
régénérés sous le même nom.

### Le manifeste des sons, produit hors navigateur

`build/collecte_sons.py` reste la voie normale : il reçoit du navigateur le
relevé que le moteur produit au rendu. Elle n'était pas praticable ce jour-là
— quatre sessions se partageaient le même onglet de prévisualisation et se le
reprenaient l'une à l'autre en pleine mesure. `sons_module_n5_degat.json` a
donc été produit en rejouant, hors navigateur, les **sept endroits du gabarit
qui appellent `playWord`** :

| Origine | Identifiant | Ligne du module |
|---|---|---|
| bloc `savoir` avec `speak` | `<exo>_savoir_<ri>_<wi>` | 2560 |
| `it.audio` d'un exercice `write` | `<exo>_<i>` | 2620 |
| bloc `ana` d'une mini-leçon | `plus_<exo>_ana<bi>` | 4293 |
| bloc `ex` d'une mini-leçon | `plus_<exo>_ex<bi>_<ri>` | 4316 |
| bloc `labo` d'une mini-leçon | `plus_<exo>_lab<bi>_<clé>` | 4370 |
| exercice à cartes | `<exo>_<row.id>` | 4613 |
| exercice `vf` écoutable | `<exo>_<row.id>` | 4642 |

Résultat : 179 entrées, aucun mot sans phrase porteuse. Si un doute survient,
relancer la collecte par le navigateur et comparer les deux fichiers.


## Ce qui a été rencontré en chemin

- **Le thème refuse les flèches.** `→` n'existe pas dans Verdana et le
  garde-fou de `theme.py` arrête l'enregistrement. Quatre decks en portaient ;
  remplacées par « donne » ou par une virgule.
- **Trois tableaux débordaient de la diapositive projetée** (C2, E1, E2). Le
  contrôle de `theme.py` est strict et il a raison : coupés en deux, ils se
  lisent mieux.
- **Une illustration de E1 pointait vers `vocab/`** au lieu de `images/`. Les
  deux dossiers ne servent pas au même usage ; un contrôle rapide des chemins
  `IMG +` a été fait sur les seize decks.
- **`build/vignettes.py` se lance depuis la racine**, pas depuis
  `build/powerpoints/`.


## Les contrôles

    python3 build/sections.py --verifier            OK
    python3 build/materiel.py --verifier            OK
    python3 build/couleurs_niveau.py --verifier     OK — 0 à corriger
    python3 build/couleurs_sections.py --verifier   OK — 0 couleur verte
    python3 build/controles/pieds_de_page.py        OK — 0 écart
    python3 build/powerpoints/sommaire.py --verifier OK pour 62

Les deux liens « diaporamas » que `sommaire.py` signalait encore appartiennent
à des modules d'autres sessions, en cours au même moment.
