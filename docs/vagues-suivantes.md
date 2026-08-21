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

**21 août 2026 — activité 67, `module-n5-travail`.** « Le travail par écrit »,
niveau 5, `numero` 7. Scénario inventé : Dorine Kabeya, 41 ans, arrivée de
Kinshasa il y a deux ans, passe de l'entretien à l'accueil de la Coopérative
d'aide à domicile de Rosemont — un bureau, un poste de téléphone, et presque
tout ce qui change s'écrit. Ghislain Marcoux est son chef d'équipe, Kevin
Dorais le collègue du corridor, Sylvie Painchaud tient la paie, et madame
Thériault est la cliente dont on entend le message dans la boîte vocale.
20 exercices, 14 mini-leçons, 4 dialogues, 16 mots, 20 images, **309 extraits
audio** (76 répliques et 233 sons), 16 séances (195 diapositives, 140 blocs de
fiches). Originalité : 203 énoncés visibles, **0 identique** dans les 4 687 des
vingt-six autres modules de `build/contenu/`.

*Ce qui le distingue de ses trois voisins* : `module-travail` (39), au niveau 4,
fait **annoncer une absence ou un retard** par téléphone, dans l'urgence du
matin ; ici l'absence se prépare trois semaines d'avance, par écrit, en six
étapes, et le téléphone ne sert qu'à laisser un message que personne n'écoute
en direct. `module-n8-emploi` (61) fait **tenir son bout** et défendre un point
de vue devant un supérieur ; ici on ne négocie rien, on suit une procédure et
on réclame une trace écrite. `module-n6-recherche` (59) **cherche** un emploi —
offre, demande, entrevue ; ici l'emploi est déjà obtenu, et c'est la paperasse
du poste qu'il faut apprendre.

*C'est le cadre qui a décidé de la forme du module, et il surprend.* La
situation « Emploi » du niveau 5 ne parle pas de relations d'équipe : ses sept
intentions sont des **écrits et des procédures** — comprendre puis nommer les
étapes d'une démarche administrative simple, enregistrer un message
téléphonique, lire un mode d'emploi, rédiger des notes pratiques sur
l'utilisation du matériel courant, rédiger un court message à partir de notes
détaillées, et rédiger un courriel de réponse automatique en cas d'absence. Les
savoirs lexicaux du niveau les répètent mot pour mot : « photocopieur,
imprimante, boîte vocale », « appuyer, insérer, verrouiller, confirmer »,
« autorisation d'absence, registre des heures », « abréviations ». Aucun
lexique n'est fourni : les seize mots s'inventent à partir des savoirs. La
progression grammaticale vient du même endroit : la liaison obligatoire et le
registre en « Je découvre », impératif et place du pronom puis discours
rapporté au présent au défi 1, marqueurs de temps et impératif contre infinitif
de consigne au défi 2, futur simple et interrogation indirecte au défi 3. Un
scénario `conge` a été ajouté à `server.py` : `entrevue` porte l'embauche et non
la vie du poste, et tous les autres mettent en scène un service qui répond à la
demande d'un client — alors qu'ici l'interlocuteur est un supérieur qui
n'accorde rien de vive voix et renvoie au formulaire.

*Les faits québécois ont été vérifiés, pas inventés*, le 21 août 2026 auprès de
la CNESST et de Légis Québec : deux journées d'absence payées par année pour
maladie ou obligations familiales après trois mois de service continu, jusqu'à
dix journées d'absence par année à ce titre ; deux semaines de vacances après
un an de service continu et trois semaines après trois ans ; l'employeur doit
faire connaître les dates de vacances au moins quatre semaines à l'avance ;
le bulletin de paie doit permettre de vérifier le calcul du salaire (art. 46 de
la Loi sur les normes du travail). Le délai de trois semaines de la coopérative,
lui, est une **politique interne inventée**, et le module le dit explicitement —
savoir d'où vient une règle permet de savoir si elle se discute.

Trois choses apprises, qui valent pour les modules restants :

- **Le gabarit ne rend les pastilles d'un bloc `savoir` que si celui-ci porte
  `speak:true`.** Écrire des listes `savoir[…][2]` sans ce champ produit des
  pastilles qui n'existent pas : rien ne s'affiche, rien ne s'entend, et rien
  ne le signale. Les quinze bandeaux du module ont été passés à `speak:true`
  d'un coup, ce qui a fait passer le relevé de 206 à 233 sons — vingt-sept
  pastilles, une par mot du banc, chacune lisant sa phrase porteuse.
- **Le relevé des sons hors navigateur se fait en trente lignes de node, et il
  faut charger `fccards.js` en premier.** `exos.js` appelle `FC_CARDS.map()` au
  moment de l'évaluation : dans l'autre ordre, node s'arrête sur « Cannot access
  FC_CARDS before initialization ». Et `eval(src)` ne fait pas fuir les `const`
  hors de sa portée en CommonJS : il faut terminer par
  `; ({EXOS, PLUS, CARRIER_PHRASES})` et déstructurer le résultat.
  `build/collecte_sons.py` n'a pas été lancé une seule fois, et le point noir
  des deux nuits précédentes ne s'est donc pas représenté.
- **Un `git commit` avec des chemins de dossier emporte tout ce que le dossier
  contient, y compris ce qui vient d'y arriver.** Le commit des pastilles,
  fait avec `-- build/contenu/<slug> assets/interactive/<slug>`, a emporté les
  309 MP3 et les 20 images produits pendant l'écriture des séances : rien de
  perdu, rien à réparer, mais le message ne parlait que des pastilles. Nommer
  les fichiers plutôt que les dossiers quand des médias sont en train de
  tomber dedans, ou dire dans le message qu'ils suivent.

*Sur les contrôles* : les six passent, plus le `node --check` du script produit
et la vérification que les 233 clés du manifeste ont chacune leur MP3.
`sommaire.py --verifier` ne signale plus aucun lien cassé.

**21 août 2026 — activité 66, `module-n5-urgence`.** « Une nuit à l'urgence »,
niveau 5, `numero` 6. Scénario inventé : Marisol Quintero, 38 ans, arrivée de
Colombie il y a trois ans, opératrice dans une buanderie industrielle de
Saint-Léonard ; sa mère Amparo, 71 ans, fait de la fièvre depuis deux jours et
répète que ce n'est rien, puis tombe dans l'escalier à deux heures du matin.
Patrick tient la ligne d'Info-Santé, Vincent celle du 9-1-1, Karine le comptoir
du triage, la docteure Lamontagne l'unité de soins, et Julio est le frère resté
à Laval qui ne sait encore rien. 19 exercices, 12 mini-leçons, 4 dialogues,
16 mots, 19 images, **283 extraits audio**, 16 séances (190 diapositives,
138 blocs de fiches). Originalité : 283 énoncés visibles, **0 identique** dans
les 6 001 énoncés des vingt-trois autres modules de `build/contenu/`.

*Ce qui le distingue de son voisin du 4* : `module-urgence` (activité 36) fait
**raconter après coup** un accident de travail — une brûlure — à l'urgence puis
à l'accueil, et l'élève y est le blessé. Ici l'élève accompagne quelqu'un
d'autre : il compose le 9-1-1 **pendant** que ça se passe et doit tenir un
appel où c'est l'autre qui mène, puis il traverse le triage, l'attente, une
hospitalisation de trois jours et un congé — tout ce que le niveau 4 ne fait
pas. Le programme ne donne qu'une intention pour cette situation, en CO et en
PO — « téléphoner au 9-1-1 et au 8-1-1 » — et aucun lexique : les seize mots
sont inventés à partir des savoirs. La progression grammaticale vient du même
endroit : nasales [ɑ̃]/[ɔ̃] au téléphone, impératif présent et place du pronom
au défi 1, imparfait contre passé composé et interrogation indirecte au défi 2,
futur simple et discours rapporté au défi 3. Un scénario `urgence911` a été
ajouté à `server.py` : aucun des existants ne convenait, tous mettant en scène
un service qui répond à une demande, alors que le répartiteur mène l'échange
dans un ordre fixe, ne console pas, ne diagnostique pas, interrompt le récit
pour redemander l'adresse et n'autorise pas à raccrocher.

*Les faits québécois ont été vérifiés, pas inventés*, auprès de Québec.ca, du
MSSS et d'Urgences-santé : 8-1-1 gratuit jour et nuit toute l'année ; échelle
canadienne de triage et de gravité à cinq niveaux, évaluation de moins de cinq
minutes ; transport ambulancier facturé environ 125 $ plus 1,75 $ le kilomètre,
payé pour les 65 ans et plus **lorsque le médecin de l'établissement confirme
après coup** que le transport était nécessaire — la nuance compte, et le module
la porte telle quelle.

Trois choses apprises, qui valent pour les modules restants :

- **Les symboles de l'alphabet phonétique n'existent pas dans Verdana.** Le
  contrôle de glyphes de `theme.py` arrête le build sur `ɑ̃`, `ɔ̃`, `ɛ̃` — et
  sur la flèche `→`, qu'on emploie pourtant volontiers dans un tableau de
  transformation. Le module interactif, lui, les affiche très bien : c'est une
  contrainte des séances seulement. La séance de phonétique dit donc « an » et
  « on », et les tableaux disent « donne » au lieu de la flèche.
- **Le contrôle de densité des tableaux se déclenche vite** : quatre tableaux
  ont dû être raccourcis, cellule par cellule. Écrire court dès le départ coûte
  moins cher que raccourcir après coup.
- **Reformuler les consignes génériques à la fin ne coûte rien** — à condition
  de vérifier que le relevé des sons est identique avant et après. Seize
  coïncidences ont fait passer l'originalité de 5,7 % à 0 % sans qu'un seul MP3
  soit à refaire : ni les identifiants, ni les textes lus à voix haute ne
  touchent aux `sub` et aux `tit` des exercices.

*Sur les contrôles* : les six passent, plus le `node --check` du script produit.
`sommaire.py --verifier` signale encore deux liens cassés — `module-n3-restaurant`
(77) et `module-n2-classe` (89), inscrits au registre par les deux sessions
voisines mais pas encore produits. Ce ne sont pas des écarts de ce module.

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


**21 août 2026 — activité 76, `module-n3-electro`.** « Acheter un appareil »,
niveau 3, `numero` 3. Scénario inventé : Marisol, dont la laveuse lâche au
milieu d'un lavage ; sa voisine Louise lui apprend à lire la circulaire, le
vendeur Mario tient le rayon, Rachid le comptoir de la livraison. 22 exercices,
8 mini-leçons, 5 dialogues (60 répliques), 16 mots, 23 images, **246 extraits
audio**, 16 séances (180 diapositives, 136 blocs de fiches).

*Ce qui le distingue de son voisin du 4* : `module-achat` (activité 52)
s'informe sur l'appareil, lit une garantie et un mode d'emploi ; au niveau 3,
le programme ne donne à cette situation qu'**une seule** intention, et elle est
en compréhension écrite — « lire des circulaires, des catalogues, des
affichettes et des sites d'achats en ligne ». Le module est donc construit
autour de quatre papiers — la circulaire, l'affiche du rayon, l'affichette, le
bon de livraison — et l'oral n'y sert qu'à demander ce que le papier ne dit
pas. Le scénario `appareil` de `server.py` portait la garantie et la
comparaison : un scénario `electro` a été ajouté, trois cas, phrases courtes,
et un vendeur qui ne donne jamais un renseignement avant qu'on le lui demande.

Deux choses apprises, qui valent pour les dix modules restants du niveau 3 :

- **`build/powerpoints/sommaire.py` a une étape d'écriture** que la liste des
  six contrôles ne nomme pas. `--verifier` échoue sur « lien diaporamas cassé »
  tant que `python3 build/powerpoints/sommaire.py <slug>` n'a pas produit
  `assets/powerpoints/<slug>/presentations.html` — ni `build.py` ni
  `build_fiches.py` ne le font. C'est une commande de plus dans la séquence de
  l'étape 6, pas un écart à diagnostiquer.
- **`maj-mur.py` n'est pas dans le dépôt** : il vit dans
  `~/Claude/generations`, à côté des médias qu'il relève. Il se lance depuis ce
  dossier-là.

*Sur les fichiers partagés* : trois sessions écrivaient encore dans
`modules.py` et `activities.json`. Les deux entrées ont été écrites, commitées
et poussées en une minute, index vidé aussitôt, et `git show --name-only` l'a
confirmé. Les deux écarts que laissent `pieds_de_page.py` et
`sommaire.py --verifier` à la fin de cette production — `module-n2-classe` et
`module-n5-urgence` — appartiennent aux deux sessions voisines, qui n'avaient
pas encore produit leurs séances.


**21 août 2026 — activité 77, `module-n3-restaurant`.** « Commander au
comptoir », niveau 3, `numero` 4. Scénario inventé : Yolette Désir, arrivée
d'Haïti il y a huit mois, dîne au casse-croûte Chez Marcel entre deux cours ;
sa camarade Fatou lui apprend à lire le tableau du menu, Steve prend les
commandes à la caisse, Marcel appelle les numéros au poste de ramassage.
22 exercices, 10 mini-leçons, 5 dialogues (61 répliques), 16 mots, 24 images,
**289 extraits audio**, 16 séances (187 diapositives, 141 blocs de fiches).

*Ce qui le distingue de son voisin du 4* : `module-restaurant` (activité 53)
tient le repas complet — la table d'hôte, le service aux tables, ce qu'on
demande pendant le repas, l'addition, les taxes et le pourboire ; au niveau 3,
le programme ne donne que trois intentions, « commander au comptoir et
comprendre l'information donnée par le préposé » et « lire un menu simple »,
alors il n'y a ni serveur, ni addition, ni pourboire : une file, un tableau
qu'on lit de loin, un format à choisir et un numéro qu'on appelle. Le lexique
du programme, deux entrées seulement — les types de formats, les ustensiles,
serviettes de table et condiments —, donne à lui seul la moitié du banc de
mots et deux des dix mini-leçons.

*Le jeu de rôle a demandé un scénario neuf.* Le scénario `restaurant` existe,
mais il vient du niveau 4 : sa liste de sujets porte la table d'hôte, les
allergies, l'addition et le pourboire — trop lourd d'un cran. `server.py`
gagne donc `JEU_DE_ROLE_COMPTOIR` et l'entrée `comptoir` : trois cas (le trio
du midi, la soupe du jour, deux repas pour emporter), deux rôles, `client` et
`prepose`, et un préposé qui ne donne jamais un renseignement avant qu'on le
lui demande. Vérification en une ligne :
`python3 -c "import server; print(server.JEU_DE_ROLE_SCENARIOS['comptoir'])"`.

Trois choses apprises, qui valent pour les neuf modules restants du niveau 3 :

- **`build/collecte_sons.py` n'a pas été lancé du tout**, et c'est la bonne
  façon de faire disparaître les deux incidents de la nuit précédente. Vingt
  lignes de node sur `exos.js`, `carrier.js` et `plus.js` rendent le même
  relevé — 228 clés ici — sans port à réserver, sans processus à arrêter et
  sans écrivain tardif. Le générateur audio le dit dans son en-tête, pour que
  le prochain ne rouvre pas la question.
- **Un `nohup … &` lancé dans une commande de fond meurt avec elle.** Le
  générateur d'images, lancé ainsi, a produit **une** image sur vingt-quatre
  avant d'être emporté par la fin de la commande qui l'avait lancé — et son
  journal, écrit à part, ne montrait rien d'anormal. La commande longue se
  lance en avant-plan dans une tâche de fond de l'outil, sans `nohup` ni `&`.
- **Le piège de shell de la règle 1 vaut aussi pour les contrôles.** Enchaîner
  les six dans une boucle zsh avec `python3 $c` les fait tous échouer d'un
  coup, pour la seule raison que zsh ne découpe pas `$c` en mots : « ÉCART »
  partout, sans qu'aucun écart existe. `${=c}`, et les six repassent.

*Sur les fichiers partagés* : deux sessions voisines écrivaient en même temps
(activités 67 et 89). Les deux entrées de `modules.py` et d'`activities.json`
ont été écrites, commitées et poussées en une minute, index vidé aussitôt, puis
**revérifiées après coup** — elles y sont. `sections.py` et `materiel.py` ont
inscrit au passage `module-n2-classe` (89) et `module-n5-travail` (67), ce qui
est dit dans le message de commit. Les six contrôles passent, plus le
`node --check` du script produit ; le seul écart restant,
`module-n5-travail` dans `sommaire.py --verifier`, appartient à la session
voisine, qui n'avait pas encore produit ses séances.


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

**21 août 2026 — l'activité 91 est livrée.** `module-n2-inscription` · « Je
m'inscris au cours de français » : huit séances, 91 diapositives, 244 extraits
audio, les six contrôles verts pour ce module plus le `node --check`. **Six
images sur dix-sept seulement** : le compte fal.ai est verrouillé faute de
crédit. Le journal détaillé est dans `docs/chantier-tous-niveaux.md`, avec la
liste des onze images manquantes et leurs prompts. **La file du niveau 2
reprend à l'activité 92** (Météo, `module-n2-neige`).

Deux choses que cette production a apprises : le **403 « User is locked.
Reason: TOP_UP » peut ne pas se résorber** — le compte laisse passer une image
par lot, puis se referme, et relancer dix fois n'y change rien. La conduite qui
tient : livrer le module complet pour tout le reste, garder le champ `img` des
cartes du banc (le gabarit affiche la carte sans photo), **changer de type
l'exercice de glisser-déposer de photos** plutôt que de le laisser avec des
vignettes cassées, et écrire au journal la liste exacte de ce qui manque. Et
un **exercice `vf` à cartes écoutables lit son `txt` tel quel** : les
`CARRIER_PHRASES` ne s'appliquent qu'aux pastilles des blocs `savoir`, donc une
lettre seule doit s'écrire « la lettre B » et non « B ».

**21 août 2026 — l'activité 90 est livrée.** `module-n2-couloirs` · « Où est
le local 214 ? » : huit séances, 89 diapositives, 18 images, 261 extraits
audio, les six contrôles verts pour ce module plus le `node --check`. Le
journal détaillé est dans `docs/chantier-tous-niveaux.md`. **La file du
niveau 2 reprend à l'activité 91** (Inscription, `module-n2-inscription`).

Deux choses que cette production a apprises : le générateur d'images peut
rendre **HTTP 403 « User is locked. Reason: TOP_UP »** en pleine série — c'est
le crédit fal.ai épuisé, pas le prompt ni la clé, et une relance quelques
minutes plus tard suffit, le script sautant ce qui existe déjà ; et le
garde-fou de `theme.py` refuse un **tableau trop plein** avant de refuser un
glyphe absent de Verdana — un plan de bâtiment en six rangées se coupe en deux
diapositives.

**21 août 2026 — l'activité 89 est livrée.** `module-n2-classe` · « Ouvrez
votre cahier » : huit séances, 88 diapositives, 18 images, 280 extraits audio,
les six contrôles verts pour ce module plus le `node --check`. Le journal
détaillé est dans `docs/chantier-tous-niveaux.md`. **La file du niveau 2
reprend à l'activité 90** (Orientation dans l'établissement,
`module-n2-couloirs`).

Une chose que cette production a apprise, et qui vaut pour toutes les
suivantes : **le relevé des sons n'a plus besoin de `build/collecte_sons.py`**.
`build/releve_sons.js` le fait hors navigateur, sans port à surveiller et sans
risque d'écraser le fichier d'un autre module ; il a été validé en le rejouant
sur `module-n2-bonjour`, dont il rend les 164 clés à l'octet près.

**21 août 2026 — l'activité 88 est livrée.** `module-n2-bonjour` · « Bonjour,
ça va ? » : huit séances, 93 diapositives, 18 images, 214 extraits audio, les
six contrôles verts pour ce module plus le `node --check`. Le journal détaillé
est dans `docs/chantier-tous-niveaux.md`. **La file du niveau 2 reprend à
l'activité 89** (Salle de classe, `module-n2-classe`).

Deux choses que cette production a apprises : les **flèches ↗ et ↘ ne sont pas
dans Verdana** et le garde-fou de `theme.py` refuse un deck qui en porte — une
séance de prosodie dit donc l'intonation en mots ; et
**`build/collecte_sons.py` peut trouver son port déjà pris** par la session
voisine, auquel cas le relevé part écrire dans le `sons_<slug>.json` d'un autre
module sans que rien ne le dise. Vérifier le port avant, le fichier écrit après.

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

**21 août 2026, nuit — neuf modules, trois voies.** Mandat d'absence : trois
modules du niveau 5, trois du niveau 3, trois du niveau 2. Tous livrés,
vérifiés et servis en production.

| Activité | Module | MP3 | Images | Séances |
|---|---|---|---|---|
| 65 | N5 · Prendre rendez-vous chez le médecin | 267 | 24 | 16 |
| 66 | N5 · Une nuit à l'urgence | 283 | 19 | 16 |
| 67 | N5 · Le travail par écrit | 309 | 20 | 16 |
| 75 | N3 · Magasiner du linge | 249 | 22 | 16 |
| 76 | N3 · Acheter un appareil | 246 | 23 | 16 |
| 77 | N3 · Commander au comptoir | 289 | 24 | 16 |
| 87 | N2 · Remplir mon panier | 189 | 18 | 8 |
| 88 | N2 · Bonjour, ça va ? | 214 | 18 | 8 |
| 89 | N2 · Ouvrez votre cahier | 280 | 18 | 8 |

**2 326 extraits audio, 186 images, 120 séances.** Les six contrôles repassés
à la fin de la nuit, tous verts, arbre propre. Le niveau 5 compte sept
modules, le niveau 3 quatre, le niveau 2 quatre.

Trois voies parallèles au lieu de deux : une par niveau, donc des contenus qui
ne se touchent jamais. Ça tient — les seuls incidents ont porté sur les
fichiers partagés et sur un serveur de relevé, pas sur les modules.

Ce que la nuit a appris, et qui est déjà dans `CLAUDE.md` :

- **`build/collecte_sons.py` est à abandonner.** Deux incidents en une nuit :
  un port déjà pris par un agent voisin, et un serveur oublié qui réécrit le
  relevé longtemps après. Dans les deux cas le fichier écrasé était celui d'un
  *autre* module, et rien ne le disait. `build/releve_sons.js`, écrit à
  l'activité 89, ne lance aucun serveur et rend le même relevé à l'octet près.
- **L'originalité se mesure avant les MP3, jamais après** (activités 66 et 67) :
  5,7 % et 1,5 % ramenés à 0 % sans repayer un seul extrait.
- **Les pastilles `savoir` sont muettes sans `speak:true`** — 27 clés
  manquaient au relevé de l'activité 67 avant qu'on s'en aperçoive.
- **Les clés de `CARRIER_PHRASES` sont les mots accentués**, pas des slugs.
  `module-n3-epicerie` porte encore ce défaut sur douze de ses quinze mots :
  c'est le seul travail en attente laissé par cette nuit.
- **Au niveau 3, c'est `build/cadre.py` qui décide de la forme du module.**
  Une seule intention en compréhension écrite pour l'activité 76, trois pour la
  77 : on bâtit sur ce que le programme donne, on ne calque pas le niveau 4.

**La file reprend** à l'activité 68 (niveau 5), 78 (niveau 3) et 91
(niveau 2 — l'activité 90 a été livrée le 21 août au soir).

**21 août 2026 — l'activité 79 est livrée.** `module-n3-metro` · « Le bon titre
de transport » : 16 séances, 188 diapositives, 16 fiches, 276 extraits audio,
**0 image sur 23** — le compte fal.ai est verrouillé, la liste exacte des
manquantes est plus bas. Les six contrôles passés, plus le `node --check` ;
verts pour ce module. Les deux contrôles de séances signalent encore
`module-n5-transport` (activité 69), dont la session voisine n'a pas fini ses
séances : `pieds_de_page.py` rend « OK module-n3-metro · niveau 3 · numéro 6 ·
16 pptx · vus ['6'] » et `sommaire.py --verifier` ne porte aucune ligne à ce
module. **La file du niveau 3 reprend à l'activité 80** (Démarches à la poste).

Ce que cette production a appris ou confirmé :

- **Au niveau 3, « Déplacement dans une ville » ne parle pas du trajet.**
  `build/cadre.py 3` rend **trois intentions, et les trois disent la même
  chose** : « demander et comprendre de l'information pour acheter un titre de
  transport » en compréhension et en production orales, « lire l'information
  pour acheter un titre de transport » en compréhension écrite. Il n'y a ni
  itinéraire, ni direction, ni terminus, ni annonce à comprendre. Les trois
  défis sont donc les trois intentions, dans cet ordre : comprendre ce qu'on me
  répond, demander au guichet, lire la grille des tarifs. C'est le cadre le
  plus étroit rencontré jusqu'ici, et il a décidé de tout.
- **Ce qui distingue ce module de chacun de ses trois voisins**, en une phrase
  chacun, comme la consigne le demandait. De `module-deplacement` (niveau 4,
  activité 49) : celui-là fait le trajet complet — demander son chemin,
  expliquer un itinéraire, comprendre les annonces du métro — et ne s'arrête à
  aucun guichet ni ne nomme aucun prix, alors qu'ici il n'y a qu'un comptoir,
  une carte, une grille et de l'argent. De `module-n2-autobus` (niveau 2) :
  celui-là demande son chemin dans la rue et lit l'heure du prochain passage,
  sans jamais parler de carte, de titre ni de tarif. De `module-n2-couloirs`
  (niveau 2) : celui-là se repère à des numéros de porte à l'intérieur d'un
  bâtiment, et ne touche pas au transport collectif.
- **Un scénario de jeu de rôle neuf, `titre`, a été ajouté à `server.py`.**
  `chemin` (niveau 4) donne un itinéraire en six étapes avec des noms de
  terminus, ce qui n'a aucun sens devant un comptoir ; `autobus` (niveau 2) se
  joue dans la rue, sans argent. Trois cas — `mensuel`, `reduit`,
  `occasionnel` — et deux rôles, `client` et `prepose`. La clé a été vérifiée
  dans `JEU_DE_ROLE_SCENARIOS` : rien ne la contrôle à la construction.
- **Les faits québécois viennent de la grille tarifaire de l'ARTM en vigueur
  le 1er juillet 2026 et des pages de la STM, pas d'une estimation.** Quatre
  zones (A · Montréal ; B · Laval et Longueuil ; C · couronnes ; D · hors
  territoire) ; en zone A, 1 passage 3,75 $ (2,75 $ réduit), 10 passages
  35,00 $ (23,50 $), hebdo 33,25 $ du lundi au dimanche (20,00 $), mensuel
  110,00 $ (66,00 $), 24 h 11,25 $, Soirée illimitée 6,75 $ de 18 h à 5 h,
  Week-end illimité 17,00 $ du vendredi 16 h au lundi 5 h ; quatre catégories
  — Ordinaire, Réduit 6-17 ans, Réduit étudiant 18 ans et plus, Réduit 65 ans
  et plus — toutes les trois réduites exigeant une carte OPUS **avec photo** ;
  les 11 ans et moins gratuits s'ils sont accompagnés d'une personne de 14 ans
  et plus, qui ne peut en accompagner plus de cinq ; correspondance de
  120 minutes à partir de la validation, sans retour sur le même parcours.
- **Le lexique du programme a servi tel quel**, comme le demandait la
  consigne : les titres de transport (tarif mensuel, tarif réduit), les
  catégories d'âge, le transport adapté avec ses places pour personnes à
  mobilité réduite, femmes enceintes et personnes âgées, le parcours, et les
  verbes se renseigner, se déplacer, se repérer, se perdre. Chacun est dans un
  exercice ou une mini-leçon.
- **L'originalité a été mesurée avant les MP3**, puis remesurée après
  l'ajustement des images : **0,8 %** sur 237 énoncés visibles, comparés aux
  32 autres modules du dépôt. Les deux seules coïncidences sont « un titre de
  transport » et « une correspondance », des mots du lexique du programme
  qu'on ne renomme pas. Une consigne générique a été reformulée avec les mots
  du module avant que le premier extrait ne soit payé.
- **Les 60 clés de `CARRIER_PHRASES` ont été relevées sur `exos.js`, pas
  écrites à la main** : un script rend les listes `savoir[…][2]` et compare
  dans les deux sens — 60 mots, 60 phrases porteuses, aucune clé en trop ni
  manquante. C'est trente secondes de travail contre les douze clés en slug
  que `module-n3-epicerie` traîne encore.
- **`theme.py` a refusé un tableau de E1** — sept rangées plus une note — et il
  a été coupé en deux diapositives, comme le prescrit `CLAUDE.md`. Un seul
  aller-retour : écrire les tableaux courts dès le départ finit par rentrer.
- **`build/module.py` refuse un `fccards.js` qui ne commence pas exactement par
  `const FC_CARDS = `.** Un commentaire d'en-tête, même de cinq lignes, fait
  échouer la construction avec un message clair. Les notes de ce genre vont
  dans le docstring du manifeste, pas en tête d'un fichier de contenu.

**Les vingt-trois images manquantes de l'activité 79.** Le 403 est revenu aux
deux tentatives, à une heure d'intervalle. Tous les prompts sont écrits et
prêts dans `build/contenu/module-n3-metro/gen_images.py`, qui saute ce qui
existe déjà : **une seule commande les produira toutes** quand le compte sera
renfloué.

    python3 build/contenu/module-n3-metro/gen_images.py

Treize vont dans `images/` — `comptoir-station`, `tourniquets`, `carte-main`,
`grille-affichee`, `borne-vente`, `autobus-arret`, `places-avant`,
`recharge-comptoir`, `validation-autobus`, `paiement-carte`,
`argent-comptant`, `photo-carte`, `recu-titre` — et dix dans `vocab/` :
`carte-opus`, `point-de-service`, `titre-mensuel`, `recharger-carte`,
`valider-titre`, `tourniquet`, `zone-tarifaire`, `place-reservee`,
`transport-adapte`, `correspondance`.

**Et il y a trois retouches à faire en même temps**, parce que le contenu a été
ajusté à leur absence plutôt que laissé à pointer dans le vide :

1. rendre à `fccards.js` les dix champs `img` retirés, sous la forme
   `img:"/assets/interactive/module-n3-metro/vocab/<nom>.jpg"` — les noms de
   fichiers sont ceux de la liste `vocab/` ci-dessus, et chacun correspond au
   mot de même sens ;
2. rendre `prImg` (« Ce qu'on voit dans la station », sept énoncés) et `t2img`
   (« Les gestes de l'achat », six énoncés) à leur type `imgmatch`, avec leur
   bloc `images:` — les identifiants `im1`-`im7` et `ig1`-`ig6` sont déjà en
   place sur les rangées, il n'y a que le bloc `images:` à remettre et le
   `type:` à changer ; un en-tête de commentaire le rappelle dans `exos.js` ;
3. reconstruire, puis refaire `build/vignettes.py` : la note de la séance A3
   parle du glisser-déposer sans dire « photos », elle n'a pas à changer.

La difficulté propre à ces prompts, notée pour celui qui les relancera : tout
l'univers du module est couvert d'écriture — une grille de tarifs, une carte,
un écran de borne, un reçu — alors que le générateur a l'ordre de ne produire
aucun texte lisible. Les prompts demandent donc des objets dont la forme est
reconnaissable sans qu'un mot ne se lise, et aucune marque de société de
transport. Vérifier à la réception qu'aucun sigle n'est apparu.

**21 août 2026 — l'activité 78 est livrée.** `module-n3-pharmacie` · « Aller à
la pharmacie » : 16 séances, 175 diapositives, 16 fiches, 295 extraits audio,
12 images. Les six contrôles passés, plus le `node --check` du script produit —
verts pour ce module ; au dernier passage, `sommaire.py --verifier` signalait
encore l'activité 68, dont la session voisine n'avait pas fini ses séances.
**La file du niveau 3 reprend à l'activité 79** (Déplacement dans une ville).

Ce que cette production a appris ou confirmé :

- **`build/cadre.py 3 "Consultation en pharmacie"` a décidé de la forme du
  module, comme la nuit précédente l'avait recommandé.** Trois intentions, pas
  une de plus : « décrire un problème de santé courant » et « demander le
  renouvellement de l'ordonnance d'un médicament » en production orale, « lire
  une posologie » en compréhension écrite. Les trois défis sont ces trois
  intentions, dans cet ordre — rien n'a été inventé autour. **Ce qui distingue
  ce module de son voisin du niveau 4** (`module-consultation`, activité 45) :
  il n'y a ni médecin, ni salle d'attente, ni formulaire à remplir ; il y a
  deux comptoirs, une carte d'assurance maladie et une étiquette à lire.
- **Le lexique du programme est généreux à ce niveau, et il a servi tel quel** :
  les parties du corps, les prépositions de temps (depuis, ça fait, il y a,
  pendant, dans), les marqueurs de fréquence, les expressions de posologie
  (de plus de, de moins de) et les onze verbes — tousser, avoir de la fièvre,
  se couper, s'étouffer, se faire mal, consulter, questionner, administrer,
  persister, rincer. Chacun est dans un exercice ou une mini-leçon.
- **Les faits québécois ont été vérifiés, pas devinés.** Le pharmacien peut
  prolonger une ordonnance qui vient à échéance, sans dépasser un an (loi 31,
  en vigueur depuis 2021) ; il tient un dossier des médicaments de chaque
  personne ; on présente sa carte d'assurance maladie ; le régime public
  laisse à la charge une franchise et une coassurance ; certains médicaments
  se vendent sans ordonnance mais restent derrière le comptoir, sous le
  jugement du pharmacien (annexes II et III). Sources consultées : Ordre des
  pharmaciens du Québec, RAMQ, Collège des médecins.
- **L'originalité a été mesurée avant les MP3**, comme la règle le demande :
  7,5 % au premier relevé, ramenés à **1,8 %** en reformulant dix consignes et
  titres génériques avec les mots du module. Les quatre coïncidences restantes
  sont des mots du lexique du programme — *une ordonnance*, *la carte
  d'assurance maladie*, *une étiquette* — qu'on ne renomme pas. Aucun extrait
  n'a été payé puis jeté.
- **Le compte fal.ai s'est verrouillé en cours de génération d'images**
  (`HTTP 403 · "User is locked. Reason: TOP_UP"`), après douze images sur
  vingt-quatre. Ce n'est ni un prompt refusé ni une panne : c'est le solde.
  Le contenu a été ajusté à ce qui existe — un énoncé retiré de l'`imgmatch`,
  les cartes sans photo laissées sans champ `img`, ce que le gabarit accepte —
  et `gen_images.py` est relançable tel quel : il saute ce qui est déjà là.
  **Les douze images manquantes sont le seul travail en attente laissé par
  cette production.**
- **Le `node --check` ne se lance pas sur le HTML produit** : l'extension
  `.html` fait échouer node avant même de lire le fichier, et `custom.js` est
  un fragment, donc il échoue lui aussi — c'est vrai de tous les modules. Ce
  qui se vérifie utilement : les six autres `.js` de `build/contenu/<slug>/`,
  et le contenu des balises `<script>` du HTML extrait dans un fichier `.js`
  temporaire. C'est ce qui a été fait ici, et c'est vert.
- **`theme.py` refuse les tableaux trop denses et les émojis**, l'un après
  l'autre, à la construction. Neuf tableaux ont dû être raccourcis et la grille
  d'autoévaluation de E2 a perdu ses trois frimousses : le gabarit est en
  Verdana, qui ne les possède pas. Écrire les tableaux courts dès le départ —
  deux colonnes, quatre à six lignes, des cellules de moins de quarante
  caractères — évite six allers-retours de construction.

---

**21 août 2026 — activité 68, `module-n5-voisinage` « La ruelle en fête ».**
Niveau 5, situation « Relations sociales », numéro 8 du niveau, seize séances.
Livré, vérifié, servi en production. 271 extraits audio, 19 images,
177 diapositives, 16 fiches.

Marisol Vergara, arrivée du Chili il y a trois ans, deuxième étage du 7412 rue
De Normanville ; Réjean Deslauriers, rez-de-chaussée, trente ans dans
l'immeuble, qui organise la fête de la ruelle ; Ndeye Faye, troisième étage,
infirmière de nuit, qui laisse le message dans le répondeur et obtient sa
citoyenneté.

**Ce qui distingue ce module de ses deux voisins**, puisque la consigne le
demandait en une phrase chacun. De `module-relations` (48, niveau 4), qui porte
la même situation : là-bas deux inconnus bavardent dans une activité de loisir
et se racontent leurs semaines, personne n'ayant rien à demander ni à refuser,
tandis qu'ici il y a une date, une heure, un plat à apporter, et une réponse
justifiée à donner. De `module-n5-travail` (67), qui a déjà la boîte vocale et
la note d'appel : les siennes sont celles d'un bureau et parlent au nom d'un
employeur, celles-ci sont celles d'une cuisine et ne doivent surtout pas dire
où l'on habite ni quand on part.

**C'est `build/cadre.py 5 "Relations sociales"` qui a décidé de la forme**, et
il a surpris : sur les dix intentions, une seule est du bavardage. Les neuf
autres sont des actes — accepter ou refuser avec justification, féliciter,
enregistrer un message d'accueil, laisser un message, rédiger un mot à partir
de notes, écrire un courriel de nouvelles. D'où trois défis qui suivent les
intentions plutôt que le fil d'une amitié : l'invitation, le message, les
félicitations. Recevoir des nouvelles n'est plus la matière du module, c'en est
le fil.

Ce que cette production ajoute à ce qui était déjà su :

- **Les cinq leçons de la nuit ont toutes tenu.** `build/releve_sons.js` a rendu
  ses 190 clés sans ouvrir de port ; les quinze bandeaux portaient `speak:true`
  dès l'écriture ; les seize clés de `CARRIER_PHRASES` sont les mots accentués,
  et aucun des seize mots de ce module ne contient d'apostrophe, ce qui a
  simplifié le contrôle ; l'originalité a été mesurée **avant** les MP3.
- **L'originalité : 2 identiques sur 202, soit 1,0 %**, ramenés à **0** en
  reformulant deux consignes (`sub`), qui n'entrent pas dans le relevé des
  sons. Aucun extrait payé puis jeté.
- **Ne pas écrire les decks sans accents, puis les rattraper par
  substitution.** Fait ici par excès de prudence — Verdana a pourtant tout le
  latin accentué, et `theme.py` refuse justement ce qu'il ne peut pas rendre.
  La substitution automatique a produit des « quantite » restés en chemin, des
  « a » qui auraient dû être « à », et surtout elle a renommé la méthode
  `d.regle` en `d.règle`. Les quatre fichiers ont été réécrits. **Écrire le
  français correct du premier coup coûte moins cher que de le restaurer.**
- **Deux tableaux sur trente-deux ont été refusés** par `theme.py` pour cause
  de densité, et c'est peu : la consigne « deux colonnes, quatre à six lignes,
  des cellules courtes », écrite après l'activité 90, fonctionne.
- **Le compte fal.ai était à sec** (`HTTP 403 · TOP_UP`) pendant toute la
  production. Les 19 images ont fini par sortir, mais en une quarantaine de
  relances étalées : le solde se libère par à-coups, probablement au rythme des
  sessions voisines. `gen_images.py` étant relançable et sautant ce qui existe,
  une boucle `for i in $(seq 1 12); do … && break; done` suffit — inutile
  d'ajuster le contenu au manque, comme il avait fallu le faire à l'activité 90.
- **Les fichiers partagés ont encore voyagé dans les commits des voisins.**
  Les trois lignes de `modules.py`, `activities.json` et `server.py` ont été
  écrites, puis emportées par les commits des activités 78 et 90 avant que le
  commit prévu ne les prenne. Rien n'a été perdu — vérification faite ligne à
  ligne, comme la règle 1 le demande — mais l'historique ment une fois de plus.
  Le point à retenir n'est pas nouveau : **entre le `add` et le `commit`, il ne
  doit rien se passer**, et un `git status` juste avant vaut mieux qu'une
  vérification juste après.
- **Le seul écart des six contrôles appartient à quelqu'un d'autre** :
  `sommaire.py --verifier` signale l'activité 91 (`module-n2-inscription`), qui
  n'a pas encore eu son étape d'écriture. Les cinq autres sont verts, plus le
  `node --check` du script produit.

**La file reprend** à l'activité 69 (niveau 5), 79 (niveau 3) et 91 (niveau 2).

---

**21 août 2026 — activité 69, `module-n5-transport` « Ça bloque ce matin ».**
Niveau 5, situation « Déplacements dans une ville », numéro 9 du niveau, seize
séances. Livré, vérifié, poussé — **sans ses médias**, et c'est le seul travail
en attente qu'il laisse : voir « Ce qui manque » plus bas. 175 diapositives,
16 fiches, 21 exercices, 10 mini-leçons, 16 mots, 0 image sur 19, 15 extraits
audio sur 258.

Tereza Nogueira, arrivée du Brésil il y a quatre ans, aide-technicienne dans un
atelier d'assemblage de Saint-Laurent, qui part de Longueuil à six heures
cinquante ; Amine Haddad, le collègue avec qui elle covoiture depuis deux ans ;
Gaétan Roy, la voix de la chronique de circulation ; Ghislaine Lachance, la
responsable de l'atelier, qu'on appelle quand la 40 est bloquée.

**C'est `build/cadre.py 5 "Déplacements dans une ville"` qui a décidé de la
forme, et il a été catégorique** : la situation ne donne au niveau 5 qu'**une
seule intention de communication**, en compréhension orale — *suivre un
bulletin de circulation routière*. Une seule. Le module n'est donc pas un
module de déplacement, c'est un module d'écoute, et les trois défis sont trois
étapes de la même intention : comprendre une annonce (défi 1), suivre un
bulletin entier de quatre routes (défi 2), en faire quelque chose — expliquer
le détour, annoncer le retard (défi 3). Les sept points de lexique du savoir
« Écoute d'un bulletin de circulation routière » ont tous servi ; le programme
ne fournissant aucun lexique pour cette situation, les seize mots du banc sont
composés à partir d'eux.

**Ce qui distingue ce module de ses trois voisins**, puisque la consigne le
demandait en une phrase chacun. De `module-deplacement` (niveau 4), qui porte
la même situation : là-bas on compose un trajet et on lit un plan de métro pour
se rendre quelque part, tandis qu'ici on ne cherche pas son chemin — on apprend
que celui qu'on connaît est bloqué, et tout le travail est de comprendre une
voix qui parle vite. De `module-n3-metro` (79, produit en parallèle cette même
nuit) : lui achète un titre de transport et demande son chemin à quelqu'un qui
répond, alors qu'ici personne ne répond — un bulletin ne prend pas de
questions. De `module-n2-autobus` (niveau 2) : lui lit une heure dans un
horaire imprimé, alors qu'ici l'information est dite une fois et que la durée
annoncée change pendant qu'on parle.

**Le scénario de jeu de rôle `chemin` ne convenait pas**, et le juger a pris
deux minutes : il vient du niveau 4 et il fait *demander* son chemin en six
étapes à quelqu'un qui sait. Ici c'est l'inverse — c'est l'élève qui sait,
parce qu'il a écouté la radio, et il doit expliquer à quelqu'un qui n'a rien
entendu. D'où `circulation`, ajouté à `server.py` : trois cas (un pont fermé,
un carambolage, une bretelle en travaux) et deux rôles pour l'assistant, le
collègue de covoiturage qui tutoie et la responsable de l'atelier qui vouvoie.

**Les faits québécois ont été vérifiés, pas devinés.** Québec 511 est le service
d'information routière du ministère des Transports (ligne 511 et
quebec511.info) et publie les entraves planifiées ; le pont Jacques-Cartier et
le pont Samuel-De Champlain relient la Rive-Sud à Montréal, le pont-tunnel
Louis-Hippolyte-La Fontaine passe par l'autoroute 25 ; la 40 est la
Métropolitaine et la 15 la Décarie ; la ligne jaune du métro relie Longueuil à
Berri-UQAM et la ligne orange dessert Saint-Laurent ; on se range à droite pour
un véhicule d'urgence, et il existe une règle du corridor de sécurité ; les
nids-de-poule se signalent au 311 à Montréal et apparaissent au dégel. Les
personnes, l'atelier, la station de radio et les heures sont inventés.

Ce que cette production ajoute ou confirme :

- **Les pièges de `CLAUDE.md` ont tous tenu.** `build/releve_sons.js` a rendu
  ses 200 clés sans ouvrir de port — `collecte_sons.py` n'a jamais été lancé ;
  les quinze bandeaux `savoir` portent `speak:true` dès l'écriture ; les seize
  clés de `CARRIER_PHRASES` sont les mots accentués, dont deux à apostrophe —
  *l'accotement* et *un véhicule d'urgence* — écrites entre guillemets doubles ;
  l'originalité a été mesurée **avant** les MP3 ; `sommaire.py <slug>` a eu son
  étape d'écriture avant `--verifier`.
- **L'originalité : 1 identique sur 169 énoncés, soit 0,6 %**, ramené à **0** en
  reformulant une seule consigne générique (« Faites glisser chaque photo vers
  la phrase qui la décrit »). Aucun extrait n'a été payé puis jeté — et pour
  cause, aucun n'a pu l'être.
- **Un contrôle de cohérence en une commande `node`, qui a trouvé zéro écart et
  qui vaut mieux qu'une capture d'écran.** Il charge les six `.js` dans un
  contexte vide et vérifie : chaque `sec` d'exercice existe dans `SECTIONS`,
  chaque clé de `PLUS` correspond à un `id` d'exercice, aucun `id` d'énoncé
  n'est dupliqué, chaque `ok` d'un `imgmatch` a son image, chaque `ok` d'un
  `vf` est dans ses `tiles`, chaque `write` a des `items`, **chaque pastille
  `savoir` et chaque `w:` de laboratoire a sa phrase porteuse**, et **chaque
  bloc `ana` a son `say:`** — quarante blocs vérifiés d'un coup. C'est la
  vérification que le navigateur ne fait pas et que les incidents des nuits
  précédentes réclamaient. Elle tient en trente lignes, se relance en deux
  secondes, et mériterait de devenir un septième contrôle.
- **Le serveur de prévisualisation n'a pas pu être lancé** : cinq serveurs
  tournaient déjà dans le dossier, tous appartenant aux sessions voisines. La
  vérification navigateur a donc été remplacée par le contrôle ci-dessus, plus
  le `node --check` des six `.js` et des quatre blocs `<script>` extraits du
  HTML produit — verts. `custom.js` échoue au `node --check` comme dans tous
  les modules : c'est un fragment, pas un fichier.
- **Les tableaux courts, écrits courts dès le départ, sont tous passés.** Aucun
  refus de `theme.py` sur les trente-deux tableaux des seize séances : deux
  colonnes, quatre à six lignes, cellules brèves. La consigne héritée de
  l'activité 90 fonctionne, et elle épargne une demi-heure d'allers-retours.
- **Les images des séances sont posées derrière un `img()` qui rend `None`
  quand le fichier n'existe pas.** Les seize decks se sont donc construits
  malgré l'absence totale d'illustrations, et les reprendront d'eux-mêmes à la
  prochaine construction, sans qu'on touche à un seul deck. À reprendre dans
  les modules suivants tant que fal.ai est verrouillé.
- **Les fichiers partagés n'ont voyagé nulle part, pour une fois.** `git status`
  juste avant chaque `commit`, chemins explicites après `--`, et
  `git show --name-only` juste après : les trois lignes de `modules.py`, de
  `activities.json` et de `server.py` sont parties dans le commit prévu.

### Ce qui manque à ce module, et comment le finir

**Les deux fournisseurs de médias étaient à sec en même temps.** Ce n'est pas
un défaut du module ni une erreur de manipulation : les deux comptes sont
vides, et les deux scripts sont relançables tels quels — ils sautent ce qui
existe déjà.

**fal.ai · `HTTP 403 · "User is locked. Reason: TOP_UP"` · 0 image sur 19.**
Une boucle de relances espacées de deux minutes a tourné pendant toute la
production sans obtenir une seule image ; contrairement à la nuit de l'activité
68, le solde ne s'est pas libéré par à-coups. Les dix-neuf prompts sont écrits,
commentés et prêts dans `build/contenu/module-n5-transport/gen_images.py` — il
n'y a rien à réécrire, seulement à relancer :

    python3 build/contenu/module-n5-transport/gen_images.py

Les six illustrations de l'exercice `prImg` : `images/autoroute-bouchon.jpg`,
`accotement-panne`, `chantier-cones`, `remorqueuse-travail`,
`nid-de-poule-rue`, `panneau-detour`. Les treize photos du banc de mots :
`vocab/ralentissement`, `bouchon`, `accotement`, `carambolage`, `remorqueuse`,
`voie`, `vehicule-urgence`, `chaussee`, `nid-de-poule`, `detour`, `bretelle`,
`covoiturage`, `stationnement-incitatif`. **Le contenu n'a pas été ajusté au
manque** — l'`imgmatch` garde ses six énoncés et les treize cartes gardent leur
champ `img` — parce qu'ici, contrairement à l'activité 90, il ne manque pas
quelques images sur vingt-quatre : elles manquent toutes. Amputer le module
d'un exercice entier pour une panne de facturation aurait coûté plus cher que
d'attendre.

**ElevenLabs · `401 · quota_exceeded`, 21 crédits restants · 15 extraits sur
258.** Ce n'est ni le bac à sable réseau ni la liaison coupée décrits dans
`CLAUDE.md` : `curl` répond `404` normalement, la clé est bonne, c'est le quota
du compte qui est épuisé — vraisemblablement par les 276 extraits de l'activité
79, produits quelques heures plus tôt sur la même clé. Le générateur a produit
treize répliques du dialogue `prep`, une de `t1` et une de `t3` avant de buter,
et il a été arrêté aussitôt plutôt que de brûler cinquante-huit secondes par
extrait dans le vide. Il reste **43 répliques de dialogue et les 200 extraits
de `sons_module_n5_transport.json`**. Une seule commande, hors bac à sable :

    nohup python3 generer_audio_module_n5_transport.py > /private/tmp/audio.log 2>&1 &

Le relevé des sons est déjà fait, commité et vérifié : aucune valeur ne
contient de balise HTML, et les dix seuls extraits courts sont les cartes de
l'exercice de discrimination `prPhon`, où le mot doit précisément être dit nu —
c'est le seul endroit du projet où une phrase porteuse nuirait.

**La file reprend** à l'activité 70 (niveau 5), 80 (niveau 3) et 92 (niveau 2).
