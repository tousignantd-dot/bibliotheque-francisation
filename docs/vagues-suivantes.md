# Les vagues suivantes — niveaux 7 et 8, puis les niveaux 5 et 3 au complet

Écrit le 20 août 2026, pendant que les modules des niveaux 5 et 6 se
terminent. Ce fichier dit **quoi produire, dans quel ordre, avec quels
numéros réservés**. Le *comment* est ailleurs et ne se répète pas ici :

- la méthode de production : skill **`module-neuf`** (six références) ;
- le travail à plusieurs : **`docs/deux-agents-en-parallele.md`** (cinq règles,
  fichiers partagés) — son protocole reste valable, seule sa *répartition en
  cours* est remplacée par les tableaux ci-dessous ;
- les contrôles avant publication : `CLAUDE.md`, section « Les contrôles avant
  de publier un module ».

**Condition d'entrée** : `module-n5-logement` et `module-n6-recherche` livrés,
commités, poussés. Rien de cette page ne commence avant.


## La règle des numéros réservés

Le numéro d'activité relie `build/powerpoints/modules.py`, `data/activities.json`
et le portail. Deux agents qui prennent « le prochain libre » prennent le même.
**Tous les numéros sont donc réservés d'avance, ici, une fois pour toutes.** Un
agent prend le sien dans le tableau, même s'il publie avant ou après les autres.
Dernier numéro utilisé au 20 août 2026 : **59** (`module-n6-recherche`).

Le `numero` d'un module, lui, recommence à 1 à chaque niveau et suit l'ordre
des tableaux. La couleur ne se choisit pas : elle vient du niveau.


## Vague 1 — niveaux 7 et 8, deux agents en parallèle

| Agent | Niveau | Situation du programme | Slug | Activité | `numero` | Format |
|---|---|---|---|---|---|---|
| A | 7 | Suivi de l'actualité | `module-n7-actualite` | **60** | 1 | 16 séances |
| B | 8 | Emploi | `module-n8-emploi` | **61** | 1 | 16 séances |

Ce sont les deux derniers niveaux sans aucun module. Les faire ensemble ferme
le chantier « un module par niveau » (`docs/chantier-tous-niveaux.md`).

Ce que ces deux-là portent de particulier, et qu'aucun module précédent n'a eu :

- **Des discours longs.** Au niveau 7 comme au 8, la compétence porte sur des
  textes et des échanges étendus. Les dialogues de trois répliques du niveau 2
  n'y ont pas leur place ; prévoir des extraits audio plus longs, donc un budget
  ElevenLabs plus élevé et un découpage en écoutes successives.
- **Peu de lexique fourni.** Le programme s'amenuise à mesure qu'on monte : la
  liste de vocabulaire s'invente presque entièrement à partir des savoirs.
- **Des faits québécois à vérifier, jamais à inventer** — normes du travail,
  assurance emploi, organismes. Vérifier sur les sites officiels et noter la
  vérification dans le journal de `docs/chantier-tous-niveaux.md`.
- **Un scénario de jeu de rôle à ajouter** dans `server.py` pour chacun :
  aucun des scénarios existants ne convient à ces niveaux. Voir la section
  « Un mot sur `server.py` » du fichier des deux agents.


## Vague 2 — le niveau 5 au complet

`module-n5-logement` (activité 58) est le premier. Restent les treize autres
situations du niveau, activités **62 à 74** :

| `numero` | Situation | Slug | Activité |
|---|---|---|---|
| 2 | Problèmes reliés à l'habitation | `module-n5-degat` | 62 |
| 3 | Emménagement dans un nouveau logement | `module-n5-emmenagement` | 63 |
| 4 | Utilisation des services publics | `module-n5-services` | 64 |
| 5 | Consultation d'un professionnel de la santé | `module-n5-rendezvous` | 65 |
| 6 | Urgence et hospitalisation | `module-n5-urgence` | 66 |
| 7 | Emploi | `module-n5-travail` | 67 |
| 8 | Relations sociales | `module-n5-voisinage` | 68 |
| 9 | Déplacements dans une ville | `module-n5-transport` | 69 |
| 10 | Déplacements dans tout le Québec | `module-n5-quebec` | 70 |
| 11 | Suivi de l'actualité | `module-n5-actualite` | 71 |
| 12 | Météo | `module-n5-saisons` | 72 |
| 13 | Découverte d'œuvres littéraires, musicales, cinématographiques ou télévisuelles | `module-n5-oeuvres` | 73 |
| 14 | Communication avec le personnel de l'établissement | `module-n5-ecole` | 74 |

L'ordre suivi est celui de l'installation vécue : on habite, on emménage, on
branche les services, on se soigne, on travaille, puis viennent le loisir et
l'école. Un agent qui prend un module prend **la ligne suivante non commencée**,
et annonce laquelle dans son premier commit.

**Les slugs des trois tableaux sont arrêtés** — décision de l'utilisateur, le
20 août 2026. Un agent les prend tels quels : il n'a ni slug ni numéro à
choisir, seulement un scénario à inventer. Ils nomment d'ailleurs le scénario
et non la situation du programme, ce qui est la convention du dépôt depuis les
niveaux 1 et 2. Si l'un d'eux s'avère vraiment impraticable, le changement se
discute avec l'utilisateur avant d'écrire la première ligne, jamais après.


## Vague 3 — le niveau 3 au complet

`module-n3-epicerie` (activité 55) est le premier. Restent les douze autres,
activités **75 à 86**, en 16 séances comme le reste du niveau :

| `numero` | Situation | Slug | Activité |
|---|---|---|---|
| 2 | Achat de vêtements | `module-n3-vetements` | 75 |
| 3 | Achat de biens de consommation durables | `module-n3-electro` | 76 |
| 4 | Service de restauration | `module-n3-restaurant` | 77 |
| 5 | Consultation en pharmacie | `module-n3-pharmacie` | 78 |
| 6 | Déplacement dans une ville | `module-n3-metro` | 79 |
| 7 | Démarches à la poste | `module-n3-poste` | 80 |
| 8 | Location d'un logement | `module-n3-loyer` | 81 |
| 9 | Relations sociales | `module-n3-voisins` | 82 |
| 10 | Recherche d'emploi | `module-n3-recherche-emploi` | 83 |
| 11 | Emploi | `module-n3-horaire` | 84 |
| 12 | Participation à une activité culturelle ou sportive | `module-n3-loisirs` | 85 |
| 13 | Communication avec le personnel de l'établissement | `module-n3-secretariat` | 86 |

**Attention aux collisions de sujet avec le niveau 4**, qui a dix-huit modules
et couvre presque les mêmes situations. Le niveau 3 n'est pas un niveau 4
allégé : les intentions de communication diffèrent, et c'est `build/cadre.py`
qui le dit. Le faire dire au programme avant d'inventer le scénario ; le
préciser en une phrase dans le journal, comme l'a fait `module-n3-epicerie`
(« ici on trouve, on choisit, on paie », là-bas le comptoir et l'étiquette).


## Combien d'agents à la fois

Deux. Le 20 août, quatre sessions simultanées ont coûté plus de messages que
de code, et trois se sont nui. Deux agents, avec les cinq règles, tiennent deux
modules par jour.

Vingt-sept modules restent au total après les niveaux 5 et 6 : deux en vague 1,
treize en vague 2, douze en vague 3.


## La consigne à coller à un agent

Les vingt-sept consignes sont déjà écrites, une par module, dans
**`docs/consignes-a-coller.md`** : il n'y a qu'à copier celle de la ligne
voulue. Le modèle ci-dessous est la forme dont elles sortent, pour le jour où
il faudra en écrire une de plus.

Une seule forme, pour n'importe quelle ligne des trois tableaux. Remplacer les
cinq valeurs entre chevrons, rien d'autre.

> Tu produis un module de francisation dans
> `/Users/danieltousignant/Claude/bibliotheque-francisation`.
>
> **Ton module** : niveau `<N>`, situation « `<situation>` » du programme,
> slug `<slug>`, numéro d'activité **`<activité>`** (réservé — ne prends jamais
> « le prochain libre »), `numero` `<numero>` dans son niveau, format
> `<16 séances / 8 séances>`.
>
> Lis d'abord, dans cet ordre : `docs/vagues-suivantes.md` (pourquoi ce module
> et ce numéro), `docs/deux-agents-en-parallele.md` (les cinq règles et les
> fichiers partagés — un autre agent travaille en même temps que toi), puis la
> skill **`module-neuf`**, que tu suis étape par étape.
>
> Les points sur lesquels je ne veux aucune improvisation :
> `git add` avec des chemins explicites, jamais `-A` ni `.` ; `git pull` avant
> tout fichier partagé ; commits petits et fréquents ; rien n'est copié d'un
> manuel, tout s'invente à partir du programme ; les six contrôles de
> `CLAUDE.md` passent avant la publication ; le déploiement se fait par
> `git push`, jamais `railway up` ; `python3 maj-mur.py` après les médias.
>
> Tu m'écris en français. Tu m'annonces au départ, en cinq lignes, le scénario
> et les personnages que tu as inventés, et tu continues sans attendre ma
> réponse. Tu me préviens seulement si tu dois toucher un fichier transversal
> (gabarit, moteur, système de design). Ton slug et ton numéro d'activité
> sont arrêtés : ils ne se renégocient pas.

Pour la vague 1, les deux consignes se donnent en même temps, une par agent, en
ajoutant à chacune : « Un autre agent produit le niveau `<7 ou 8>` en parallèle.
Vos numéros d'activité sont 60 et 61 ; vos contenus sont isolés ; vos seuls
points de rencontre sont `modules.py`, `activities.json` et `server.py`. »

## Journal des vagues

**21 août 2026 — vague 1 close, vague 2 entamée.** Cinq modules livrés, en
ligne, audio complet, les six contrôles verts plus le `node --check` :

| Activité | Module | Extraits audio |
|---|---|---|
| 60 | Niveau 7 · Suivre l'actualité | 202 |
| 61 | Niveau 8 · Tenir son bout au travail | 230 |
| 62 | Niveau 5 · Un dégât d'eau | 241 |
| 63 | Niveau 5 · Emménager dans un nouveau logement | 255 |
| 64 | Niveau 5 · Les services de ma ville | 185 |

Le chantier « un module par niveau » de `docs/chantier-tous-niveaux.md` est
**terminé** : les huit niveaux ont chacun le leur. Le niveau 5 en a quatre.

Ce que cette nuit a appris, et qui est déjà écrit là où il faut :

- **Le `node --check` du script produit** manquait à la chaîne. Une apostrophe
  non échappée dans `bravo`, une accolade au lieu d'un crochet dans un bloc
  `piege` : le build ne voit rien, l'élève reçoit une page morte. Le contrôle
  est dans `CLAUDE.md`.
- **Tout bloc `ana` veut son champ `say:`**, sinon l'extrait lit les balises
  HTML à voix haute — et ça ne se découvre qu'une fois les MP3 payés.
- **Une coupure TLS n'est pas un refus de débit.** Le générateur attendait
  4-8-16-32 s pour une liaison qui revient en deux secondes ; la base courte
  est dans `generer_audio_module_n5_degat.py`, à copier dans les prochains.
- **Une limite d'usage peut tuer toutes les sessions d'un coup.** Ce jour-là,
  cinq agents sont morts en même temps ; tout ce qui était commité a survécu,
  le reste a été retrouvé dans l'arbre. C'est la règle 2 — commiter souvent —
  qui a fait la différence.

**La file reprend à l'activité 65** (niveau 5 · Consultation d'un professionnel
de la santé), consigne prête dans `docs/consignes-a-coller.md`.

**21 août 2026 — activité 65, `module-n5-rendezvous`.** « Prendre rendez-vous
chez le médecin », niveau 5, `numero` 5. Scénario inventé : Rachid Benali,
52 ans, préposé à l'entretien dans une école de Longueuil, a des
étourdissements le matin depuis le mois de mars et appelle ça « rien » ; sa
fille Nadia compte les mois à sa place, Manon tient le téléphone de la Clinique
de la Rive, la docteure Fongang tient le bureau. 19 exercices, 12 mini-leçons,
4 dialogues, 16 mots, 24 images, **267 extraits audio**, 16 séances
(185 diapositives, 129 blocs de fiches). Originalité : 136 énoncés visibles,
**0 identique** dans les 2 618 énoncés des vingt-deux autres modules.

*Ce qui le distingue de son voisin du 4* : `module-consultation` (activité 35)
fait **choisir le bon service** et décrire une douleur au triage ; ici l'élève
tient le rendez-vous d'un bout à l'autre — il l'obtient au téléphone, il
raconte trois mois de symptômes dans le bureau (imparfait pour le décor, passé
composé pour ce qui est arrivé, gérondif pour dire à quel moment), puis il le
déplace et l'annule dans les règles. Le programme ne donne qu'une intention
pour cette situation, en CO et en PO — « prendre, annuler ou modifier un
rendezvous par téléphone » — et aucun lexique : les seize mots sont inventés à
partir des savoirs. Un scénario `rendezvous` a été ajouté à `server.py` : au
bout du fil d'une clinique, il n'y a ni soignant ni commerçant, mais une agente
qui n'a pas le droit de donner un avis médical et qui n'annonce ni l'heure
d'arrivée ni le délai d'annulation tant qu'on ne les lui demande pas.

Trois choses apprises, qui valent pour les modules restants :

- **`render()` du gabarit ne prend aucun argument** — il rend la section
  courante. Le `SECTIONS.forEach(s=>render(s.id))` que l'en-tête des
  générateurs audio recommande ne rend donc que la **première** section, et les
  pastilles à phrase porteuse des autres manquent au relevé, sans rien dire. Il
  faut poser `curSec` avant chaque `render()`. Relevé du navigateur et recalcul
  hors navigateur ont ensuite donné le même nombre : 183 extraits.
- **Le champ `theme` du manifeste échappe son apostrophe**, au même titre que
  `bravo` et `relance` : « Consultation d'un professionnel de la santé » arrête
  le build tant que l'apostrophe n'est pas écrite `\\'`. Aucun module ne
  l'avait montré, aucun thème n'en contenant jusqu'ici.
- **`d.capture()` n'existe que dans `theme.Deck`**, pas dans `fiche.Deck` : les
  quatre séances qui en portent une la mettent sous `if hasattr(d, 'capture')`,
  comme `module-n5-services` le faisait déjà. Et seuls les exercices à banc de
  réponses se capturent — un `write` n'en a pas.

*Sur les contrôles* : les six passent, plus le `node --check` du script produit.
`sommaire.py --verifier` signale encore deux liens cassés — `module-n3-electro`
(76) et `module-n2-bonjour` (88), inscrits au registre par les deux sessions
voisines mais pas encore produits. Ce ne sont pas des écarts de ce module.

**21 août 2026 — vague 3 entamée : activité 75, `module-n3-vetements`.**
« Magasiner du linge », niveau 3, `numero` 2. Scénario inventé : Farida,
arrivée du Maroc il y a cinq mois, achète son premier manteau d'hiver ;
Jocelyne conseille au rayon, Samir aux chaussures, Kevin est à la caisse.
23 exercices, 7 mini-leçons, 7 dialogues, 16 mots, 22 images, **249 extraits
audio**, 16 séances (195 diapositives, 145 blocs de fiches).

*Ce qui le distingue de son voisin du 4* : `module-vetements` (activité 54)
fait essayer, demander un avis, lire l'entretien et se faire rembourser ; au
niveau 3, les deux seules intentions du programme sont « s'informer sur un
vêtement » et « lire une étiquette », alors on nomme, on demande et on compare
deux prix — rien de plus. Le scénario `vetement` de `server.py` était trop
lourd d'un cran pour la même raison : un scénario `linge` a été ajouté, en
phrases courtes et au présent, sans entretien ni échange.

Quatre choses apprises, qui valent pour les onze modules restants du niveau 3 :

- **Les clés de `CARRIER_PHRASES` sont les mots accentués.** Le gabarit fait
  `CARRIER_PHRASES[w]` sur le mot **tel qu'il est écrit** dans la liste
  `savoir[…][2]`. Une clé en slug (`allee` pour « allée ») n'est jamais
  trouvée : la pastille lit alors le mot seul, mal prononcé — exactement ce
  que la phrase porteuse existe pour éviter. `module-n3-epicerie` a ce défaut
  sur douze de ses quinze mots.
- **`carrier.js` doit commencer par `const CARRIER_PHRASES = `.** Un
  commentaire d'en-tête arrête le build ; le commentaire va **dans** l'objet.
- **Le relevé des sons se fait très bien hors navigateur.** Une page ouverte
  en `data:` ne peut pas écrire dans `localStorage` : `render()` y échoue et le
  relevé par le DOM rend zéro pastille de mot — sans rien dire. Vingt lignes
  de node sur `exos.js`, `carrier.js` et `plus.js` reproduisent les trois
  endroits du gabarit qui appellent `playWord`, et le résultat a été comparé au
  relevé du navigateur : même nombre de clés, mêmes valeurs.
- **`theme.py` refuse un tableau trop chargé**, et c'est une bonne nouvelle.
  Quatre tableaux ont dû être raccourcis ou coupés en deux. De même, aucun
  caractère hors Verdana : une flèche dans un encadré de règle serait partie
  en carré vide chez l'enseignante.

*Sur les fichiers partagés* : au plus fort de la soirée, **trois** sessions
écrivaient dans `modules.py` et `activities.json`. Mes deux entrées ont été
emportées par le commit d'une session voisine pendant qu'elles étaient dans
l'index — l'incident exact décrit à la règle 1. Rien n'a été perdu, tout est
poussé, et l'historique ment d'une ligne. La leçon tient : **ne pas laisser
l'index habité**, et vérifier tout de suite avec
`git show --name-only --format="" HEAD`.

*Un écrivain silencieux, découvert après coup.* `build/collecte_sons.py`, lancé
en tâche de fond puis oublié quand le relevé a été fait hors navigateur, a reçu
un envoi tardif et réécrit `sons_module_n3_vetements.json` : 164 clés à la
place de 169, **après** que les 249 MP3 aient été générés et commités. Le
fichier du dépôt était le bon, `git checkout --` a tout réglé, et la
vérification finale — 169 attendus, 0 manquant, 0 orphelin — le confirme. Mais
rien n'avertit, et un générateur relancé sur le fichier corrompu aurait produit
un module troué sans le dire. La consigne est dans `CLAUDE.md` : on l'arrête
dès qu'on n'en a plus besoin.


## Vague 4 — le niveau 2 au complet

Ajoutée le 21 août 2026, à la demande de l'utilisateur (« les modules suivants
du niveau 2 »). `module-n2-autobus` (activité 57) est le premier du niveau ;
restent les **neuf autres situations**, activités **87 à 95**, au **format
court** — huit séances, deux défis, deux blocs de quatre heures, `GRILLE_COURTE`
dans `build/powerpoints/modules.py`, comme le niveau 1.

| `numero` | Situation | Slug | Activité |
|---|---|---|---|
| 2 | Achat d'aliments ou de produits d'entretien | `module-n2-panier` | **87** |
| 3 | Relations sociales | `module-n2-bonjour` | **88** |
| 4 | Salle de classe | `module-n2-classe` | **89** |
| 5 | Orientation dans l'établissement | `module-n2-couloirs` | **90** |
| 6 | Inscription | `module-n2-inscription` | **91** |
| 7 | Météo | `module-n2-neige` | **92** |
| 8 | Transactions bancaires | `module-n2-guichet` | **93** |
| 9 | Démarches à la poste | `module-n2-colis` | **94** |
| 10 | Communication avec le personnel de l'établissement | `module-n2-secretaire` | **95** |

L'ordre suit la vie de l'élève dans son centre et son quartier : on fait son
épicerie, on salue ses voisins, on s'installe en classe, puis viennent les
démarches (inscription, banque, poste, secrétariat).

Ce que le niveau 2 impose, et qu'un agent habitué au niveau 4 oublie :

- **Le format court**, `GRILLE_COURTE` et deux défis — pas seize séances.
- **Des énoncés très courts** : deux ou trois répliques, du présent, pas de
  subordonnée. Le lexique du programme suffit presque ; ne pas l'enrichir de
  mots du niveau 4.
- **Le jeu de rôle** : les scénarios de `server.py` écrits pour le niveau 4
  sont trop lourds (six étapes, noms de terminus). En ajouter un, court.
- **Le numéro d'activité est réservé ici**, jamais « le prochain libre ».

Dernier numéro réservé après cette vague : **95**.

**21 août 2026 — l'activité 87 est livrée.** `module-n2-panier` · « Remplir mon
panier » : huit séances, 90 diapositives, 18 images, 189 extraits audio, les
six contrôles verts plus le `node --check`. Le journal détaillé est dans
`docs/chantier-tous-niveaux.md` ; les neuf consignes de la vague sont dans
`docs/consignes-a-coller.md`, section « Vague 4 ». **La file du niveau 2
reprend à l'activité 88** (Relations sociales, `module-n2-bonjour`).

Trois choses que cette production a apprises, et qui sont déjà écrites où il
faut : le champ **`theme`** du manifeste doit échapper son apostrophe, comme
`bravo` et `relance` — aucun module ne l'avait montré avant ; **`build/cadre.py`
attend l'apostrophe typographique** du programme (« Achat d’aliments »), sinon
il ne trouve pas la situation ; et **`maj-mur.py` vit dans
`~/Claude/generations`**, pas à la racine du dépôt.
