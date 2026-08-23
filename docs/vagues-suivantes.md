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

**22 août 2026 — l'activité 95 est livrée : le niveau 2 est complet.**
`module-n2-secretaire` · « Je vais au secrétariat » : huit séances,
95 diapositives, huit fiches, huit vignettes, un scénario de jeu de rôle neuf
(`secretaire`), 167 sons relevés et 229 extraits audio en attente. Dixième et
dernier module du niveau — la vague 4 est close.

**Le scénario.** Amel Tazi, arrivée d'Algérie en septembre, en est à sa
deuxième semaine au Centre Sainte-Émilie. Line Chartrand tient le comptoir du
secrétariat, Marc Ouellet est le concierge, et Sami arrive pour son premier
jour dans le dernier dialogue — c'est alors Amel qui explique. Défi 1 : le
comptoir, demander un papier, une heure, un jour. Défi 2 : prévenir d'une
absence, et lire l'avis collé sur la porte un matin de congé.

**Ce qui distingue ce module de ses voisins.** `module-n3-secretariat`
(niveau 3, activité 86) passe la même porte, mais y justifie une absence avec
un billet du médecin et du passé composé ; ici on ne justifie rien et on ne
raconte rien — on dit « demain, je ne viens pas », on donne son nom, et c'est
fini. La consigne du jeu de rôle l'écrit noir sur blanc à l'assistant : ne
jamais demander pourquoi.

**Sans images et sans audio** : cette session n'avait aucune clé d'API. Les
deux générateurs sont écrits, vérifiés et commités —
`build/contenu/module-n2-secretaire/gen_images.py` (vingt images, routé par
`build/route_images.py`) et `generer_audio_module_n2_secretaire.py` (229
extraits). Le septième contrôle sort donc **20 écarts, tous « image absente du
disque »**, et rien d'autre. Une fois les images produites, il faut
reconstruire les huit `.pptx` : les séances les reprennent.

**Trois choses que cette production a apprises.**

- **Le chemin absolu des générateurs d'images ne survit pas à un *worktree*.**
  Les `gen_images.py` plus anciens écrivent
  `/Users/…/bibliotheque-francisation/assets/…` en dur. Produit dans un
  worktree git — nécessaire ici, la copie principale étant occupée par la
  session voisine — ce chemin dépose les images dans **l'autre** copie du
  dépôt. Celui-ci déduit la racine de `__file__`.
- **Les séances ne doivent pas s'arrêter faute de photo.** `theme.py` ouvre
  l'image avec Pillow : un fichier manquant lève une exception et le module
  entier ne se construit plus. Les quatre decks à déclencheur passent par une
  petite fonction `img()` qui rend le chemin seulement si le fichier existe.
- **La mesure d'originalité se fait avant de committer, pas après.** Première
  mesure : 6,0 % de coïncidence avec les autres modules, au-dessus du seuil de
  5 %. Onze consignes et titres reformulés, et la mesure tombe à 1,6 %. Le
  relevé des sons est resté identique à l'octet près — ni les `sub` ni les
  `tit` n'y entrent, donc rien à repayer.

**22 août 2026 — l'activité 94 est livrée.** `module-n2-colis` · « J'envoie
une lettre et un colis » : huit séances, 97 diapositives, huit fiches, huit
vignettes, un scénario de jeu de rôle neuf. Les neuf fichiers de contenu
existaient déjà sur `main`, produits par une session précédente ; cette
session a fait tout le reste — registre, `JEU_DE_ROLE_COLIS` dans `server.py`,
catalogue, build, séances, relevé des sons et générateur audio.

**Sans médias, et c'était le mandat** : cette session n'avait pas les clés
d'API. `build/contenu/module-n2-colis/gen_images.py` est écrit, passe par
`build/route_images.py` (jamais fal.ai en dur) et couvre exactement les vingt
images du module ; `generer_audio_module_n2_colis.py` et son relevé sont
prêts et relançables — ils sautent ce qui existe :

    python3 build/contenu/module-n2-colis/gen_images.py   # 20 images
    python3 generer_audio_module_n2_colis.py              # 231 extraits attendus
                                                          # 63 répliques sur 6 dialogues + 168 sons

Les **vingt écarts** de `node build/coherence.js module-n2-colis` sont donc
tous « image absente du disque » — six illustrations d'exercice, quatorze
photos du banc de vocabulaire — et rien d'autre. Les huit séances portent un
garde-fou `_photo()` qui les laisse se construire sans les photos et les
reprend d'elles-mêmes dès qu'elles existent : reconstruire les `.pptx` après
la génération suffit.

**Ce qui distingue ce module de ses voisins.** `module-n3-poste` (niveau 3,
activité 80) porte la même situation du programme, mais son unique intention
est **orale** — on se renseigne au comptoir, on compare deux vitesses d'envoi,
on demande un mandat-poste ; ici, `build/cadre.py 2 "Démarches à la poste"` ne
rend que deux intentions et elles sont toutes deux **écrites**, si bien que la
parole tient en trois mots (« Un timbre, s'il vous plaît. ») et que tout le
module se joue sur le papier : les cinq lignes d'une adresse, le code postal,
les cases d'un formulaire et l'endroit où l'on signe.

**Ce que cette production a appris.** `build/controles/pieds_de_page.py` fixe
`ROOT` à `~/Claude/bibliotheque-francisation` en dur : lancé depuis un
*worktree*, il contrôle le dépôt principal et **ne voit pas le module qu'on
vient de produire**, sans rien dire. Il sort alors « OK » pour de mauvaises
raisons. Depuis un worktree, refaire le relevé à la main avec le fragment de
`docs/` ou de la skill — recoller les runs `<a:t>` — plutôt que de croire le
script. Vérifié ainsi ici : les huit `.pptx` portent bien `MODULE 9`.

**21 août 2026 — l'activité 92 est livrée.** `module-n2-neige` · « Il fait
froid, je m'habille » : huit séances, 100 diapositives, 20 images, les six
contrôles verts pour ce module plus le `node --check`. **Sans audio** : le
compte ElevenLabs répond encore `401 quota_exceeded` (« 0 credits
remaining »), vérifié sur un seul extrait avant tout gros travail, comme la
consigne le demandait. Le relevé `sons_module_n2_neige.json` est complet et
vérifié (`node build/releve_sons.js module-n2-neige`, 177 sons, identique à
celui de la veille), et le générateur est prêt et relançable — il saute ce qui
existe, donc une reprise ne coûte rien :

    python3 generer_audio_module_n2_neige.py      # 234 extraits attendus
                                                  # 57 répliques sur 6 dialogues + 177 sons

**Ce qui distingue ce module de ses voisins.** `module-meteo` (niveau 4) fait
lire un bulletin écrit et une alerte météo, avec des subordonnées et du futur ;
ici, trois mots et un chiffre suffisent — le mot du temps, la ville, le nombre
de degrés — et toute la grammaire du module tient dans la phrase
impersonnelle (« il neige », « il fait froid », « il y a du vent ») et dans le
signe qui précède la température.

**Ce que cette production a appris.** Le `401 quota_exceeded` d'ElevenLabs et
le `401 missing_permissions` de `/v1/user/subscription` ne veulent pas dire la
même chose : la clé du dépôt n'a pas la permission `user_read`, donc
**interroger l'abonnement ne dit rien de l'état du quota**. Le seul test qui
tranche est une vraie génération d'un extrait court. Et un `tableau` de six
rangées qui porte en plus une `note` dépasse la diapositive : `theme.py` le
refuse en clair, et c'est la `note` qu'on retire, pas une rangée.

**21 août 2026 — l'activité 91 est complétée.** Ses **dix-sept images**
existent maintenant (le compte fal.ai s'est débloqué), et l'exercice 3 de
« Je découvre » est **rendu à sa forme d'origine** : `imgmatch`, six photos du
secrétariat à glisser sur six phrases, comme le commentaire en tête de
l'exercice l'avait prévu. Les huit `.pptx` ont été reconstruits pour reprendre
les photos.

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

**21 août 2026 — l'activité 80 est livrée.** `module-n3-poste` · « Le colis
de Yassine » : 16 séances, 190 diapositives, 16 fiches, 23 images, les six
contrôles verts pour ce module plus le `node --check`. **Sans audio** : le
compte ElevenLabs répond encore `401 quota_exceeded` (« 0 credits
remaining »), vérifié sur un seul extrait de deux mots avant tout gros
travail. Le relevé des sons, le générateur complet et relançable et le nombre
d'extraits attendus sont en place : `python3
generer_audio_module_n3_poste.py`, **316 extraits** — 72 répliques sur cinq
dialogues et les 244 clés de `sons_module_n3_poste.json`. **La file du
niveau 3 reprend à l'activité 81** (Location d'un logement), déjà entamée par
une session voisine. Le journal détaillé est dans
`docs/chantier-tous-niveaux.md`.

Ce que cette production a appris ou confirmé :

- **« Démarches à la poste » n'a aucun voisin au niveau 4.** C'est une
  situation des niveaux 2 et 3 seulement ; les dix-sept modules du 4 ne la
  traitent nulle part. Ses voisins sont les six autres comptoirs du niveau 3,
  et ce qui l'en sépare tient en une phrase : ici l'objet part sans vous, et
  tout ce qui se demande porte sur un moment qu'on ne verra pas.
- **Le lexique du programme donne des énoncés-types tout faits.** Le cadre du
  niveau 3 rend « Donnez-moi… », « Je vais le prendre » et « Je vais en prendre
  trois » comme entrées de lexique. Ils sont devenus deux exercices et une
  séance entière. Au niveau 3, le programme est plus prescriptif qu'on ne le
  croit : le lire avant d'inventer économise une invention inutile.
- **Le contrôle d'originalité passe avant les MP3, et il est gratuit.** Mesuré
  ici avant le premier extrait : 2,9 %, ramené à 0,3 % par huit reformulations
  d'intitulés de bandeau. Le relevé des 244 sons est identique à l'octet avant
  et après — ni les `sub`, ni les `tit`, ni les intitulés n'y entrent.
- **Commiter après chaque morceau, pas après chaque étape.** Ce module a été
  interrompu quatre fois. Rien n'a été perdu, et rien n'a été réécrit deux
  fois : chaque reprise a commencé par `git status` et a trouvé le travail
  précédent en place.

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

---

**21 août 2026 — activité 70, `module-n5-quebec` « Une semaine au Bic ».**
Niveau 5, situation « Déplacements dans tout le Québec », numéro 10 du niveau,
seize séances. Module repris après **quatre interruptions** : les dix
mini-leçons et les sept fichiers de contenu étaient déjà commités
(`a44f9d6c`, `0f23ce5b`) et intacts — `node --check` vert sur les six vrais
`.js`, `custom.js` étant un fragment qui n'a pas à passer seul. Rien n'a été
réécrit ; tout ce qui manquait était en aval du contenu.

**Ce qui le distingue de ses voisins**, en une phrase : `module-n5-transport`
(69) est un module d'écoute où la route est bloquée et où tout se joue dans
l'heure qui vient, tandis qu'ici la route n'est pas bloquée, elle est longue —
un horaire interurbain à lire, un billet à acheter, une valise à mettre en
soute et cinq cents kilomètres à faire ; `module-deplacement` (niveau 4)
compose un trajet dans une ville et lit un plan de métro, alors qu'on quitte
ici la ville pour une semaine.

**Ce qui manquait, et qui a été fait** : l'inscription au registre
`build/powerpoints/modules.py` et à `data/activities.json` (id 70, aucune des
deux n'existait — vérifié, pas supposé), le scénario de jeu de rôle
`regions` dans `server.py`, le module bâti, les 18 images, les 16 séances, les
fiches, le sommaire et les deux relevés.

**Le jeu de rôle : le rôle de l'élève était à l'envers.** Le manifeste portait
`jr_role: 'prepose'`, ce qui aurait fait *renseigner* l'élève au lieu de le
faire *demander* — `jeu_de_role_system()` donne à l'assistant le rôle que
l'élève ne joue pas. Corrigé en `voyageur`, et la résolution a été rejouée
hors serveur sur les trois cas et les deux rôles avant d'écrire quoi que ce
soit : avec `jr_role: 'voyageur'`, l'assistant prend bien `prepose`. Le
scénario `regions` a trois cas — `depart` (le comptoir de la rue Berri),
`gite` (le salon du gîte), `sentier` (la conversation entre vacanciers) — et
deux rôles.

**ElevenLabs · toujours `401 · quota_exceeded`, 0 crédit.** Vérifié comme
demandé par **un seul extrait court** (« un phare », 4 crédits) avant tout
travail en gros : `"You have 0 credits remaining"`. Le compte n'a pas été
rechargé depuis l'activité 69. Rien n'a été insisté. Le module est donc livré
complet et **sans audio**, avec tout le nécessaire pour que ça ne soit qu'une
commande à lancer :

    python3 generer_audio_module_n5_quebec.py

**281 extraits attendus** : 70 répliques sur quatre dialogues (`prep` 17,
`t1` 17, `t2` 17, `t3` 19) et 211 sons de
`sons_module_n5_quebec.json`. Le relevé a été fait par
`node build/releve_sons.js module-n5-quebec` — **`build/collecte_sons.py` n'a
jamais été lancé**. Le générateur est relançable sans risque (un extrait
présent est sauté) et son en-tête porte l'état exact. Vérifier d'abord le
rechargement avec `--only pr1_savoir_0_0` plutôt que de relire 281 échecs.
Cinq personnages pour quatre voix : THUY traverse les quatre dialogues et
garde la voix féminine #2 ; CAMILLE et ROSE-AIMÉE ne paraissent jamais dans
le même dialogue et partagent la voix « enseignante », ralentie à 0,85 — ce
sont les deux qui *expliquent* à Thuy, un débit lent y est voulu. Aucune
collision de voix dans aucun dialogue, vérifié par script.

**Les images, elles, fonctionnent** : 18 sur 18 par fal.ai (nano-banana-2, 3:2,
0 échec), six illustrations de `prImg` et douze photos du banc réduites à
800 px. Les 18 chemins référencés par le contenu ont été croisés avec ce que
le générateur produit — correspondance exacte dans les deux sens — puis
revérifiés par `fetch` dans le navigateur avec les quatre icônes : 22 sur 22.
`maj-mur.py` lancé depuis `~/Claude/generations`.

**L'originalité, mesurée puis corrigée.** Faute de source antérieure, la
mesure est celle des voisins : 23 énoncés sur 417 communs à un autre module,
soit **5,5 %** — au-dessus du seuil de 5 %. Aucun n'était narratif : c'était
l'échafaudage des mini-leçons (« Qui — le sujet du verbe qui suit », « Le
gérondif : dire par quel moyen… ») partagé mot pour mot avec
`module-n5-transport`, écrit la même nuit par la même méthode. Les onze
libellés en cause ont été réécrits — l'audio n'existant pas encore, ça ne
coûtait rien — et la mesure est retombée à **3,1 %** (13 énoncés, tous des
libellés du gabarit ou des fragments de deux mots). Refaire cette mesure sur
un module neuf vaut la peine : elle attrape ce qu'aucun contrôle ne regarde.

**Les six contrôles** sont verts pour ce module. Les deux seuls écarts du
dépôt appartiennent à quelqu'un d'autre : `pieds_de_page.py` et
`sommaire.py --verifier` signalent tous deux `module-n3-loyer` (activité 81),
dont l'étape d'écriture du sommaire n'a pas encore été lancée par la session
qui le produit. `module-n5-quebec` y sort
`OK · niveau 5 · numéro 10 · 16 pptx`. Plus le `node --check` du script en
ligne du module bâti, et la vérification au navigateur : les six sections
rendues sans erreur, zéro message de console, les 88 blocs des dix
mini-leçons rendus, le manifeste audio à 148 clés.

**Les 16 séances** font 178 diapositives, et les fiches élèves 133 blocs en
noir et blanc. Le bloc D compte deux séances pour six exercices : D1 prend le
dialogue et le registre (tu/vous), D2 le gérondif et le couple passé composé /
imparfait.

**Un seul `git push`, à la fin**, sur consigne reçue en cours de route : trois
agents qui poussent mettent le catalogue en 502 toutes les six minutes. Les
fichiers partagés — `modules.py`, `activities.json`, `server.py`,
`sections.json`, `materiel.json` — ont été pris avec `git pull --rebase` juste
avant et commités aussitôt après, chemins explicites, jamais `-A`.

**Un grain de sable partagé, à savoir** : `data/materiel.json` est un relevé
du **disque**, pas du dépôt. Au moment où il a été refait, la session qui
produit `module-n3-loyer` (activité 81) avait ses fichiers sur le disque mais
pas encore commités : le relevé les mentionne donc neuf fois. Ce n'est pas une
erreur à corriger à la main — elle se dissout dès que cette session commite les
siens et relance `python3 build/materiel.py`. Le contrôle a aussi échoué une
première fois parce que l'autre session écrivait pendant la génération :
relancer avant de conclure à un écart.

**La file reprend** à l'activité 71 (niveau 5).

---

**21 août 2026 — activité 81, `module-n3-loyer` « Trois questions avant de
louer ».** Niveau 3, situation « Location d'un logement », numéro 8 du niveau,
seize séances. Livré, vérifié, poussé — **sans ses médias, et sans qu'aucun
appel n'ait été tenté** : cette session tournait dans un environnement distant
qui ne porte ni la clé d'ElevenLabs ni celle de fal.ai. Voir « Ce qui manque »
plus bas. 204 diapositives, 16 fiches, 23 exercices, 11 mini-leçons, 16 mots,
0 image sur 26, 0 extrait audio sur 301.

Dilnoza Karimova, arrivée d'Ouzbékistan il y a quatorze mois, qui vit à trois
dans un deux et demie de Villeray où son garçon de six ans dort dans le salon ;
Rachid, le camarade de classe qui a déjà déménagé deux fois et qui lit
l'annonce avec elle ; Claudine, la propriétaire du quatre et demie de la rue
Chabot, au téléphone puis pendant la visite ; Théo, le concierge, qui montre la
buanderie du sous-sol.

**C'est `build/cadre.py 3 "Location d'un logement"` qui a décidé de la forme, et
il a été étroit** : la situation ne porte au niveau 3 que **deux intentions de
communication** — *demander et comprendre des renseignements sur le logement
pendant une visite*, inscrite en compréhension et en production orales, et
*lire des petites annonces simples* en compréhension écrite. Aucune production
écrite rattachée à la situation ; celle du module s'appuie donc sur les attentes
de fin de cours du niveau, qui demandent « un message compréhensible d'une ou de
quelques phrases simples ». Les trois défis sont ces deux intentions mises en
gestes : on lit une annonce, on téléphone, on pose trois questions sur place.
Le lexique que le programme rattache à la situation — les pièces, 3 ½ et 4 ½,
meublé, chauffé, éclairé, électricité comprise, le bail, louer, se renseigner,
chauffer, éclairer — a servi tel quel, comme la consigne le demandait.

**Ce qui distingue ce module de ses deux voisins**, puisque la consigne le
demandait en une phrase. De `module-logement` (niveau 4, module 9), qui porte la
même situation : là-bas on visite **deux** logements et on les compare pour
choisir, on argumente, on pèse ce qui compte pour soi — ici il n'y a qu'un seul
logement et aucune comparaison, tout le travail consiste à aller chercher six
renseignements qu'on ne vous donnera pas spontanément. De `module-n5-logement` :
lui fait la démarche entière, l'appel avec prise de notes, la visite, puis le
bail, l'annexe et l'avis de renouvellement — ici aucun papier ne se lit sauf six
lignes d'annonce, et personne ne signe.

**Le scénario de jeu de rôle `louer` ne convenait pas**, et la consigne
demandait justement de le vérifier. Il existe et il sert aux niveaux 4 et 5,
mais ses trois cas font comparer un budget, soupeser le bruit et les animaux et
discuter la durée du bail — sept sujets pour un débutant qui a trois questions à
poser. D'où `visite`, ajouté à `server.py` : trois cas tenus en six lignes
d'annonce chacun (le 4 ½ chauffé et éclairé de la rue Chabot, le 3 ½ non chauffé
du sous-sol, le 2 ½ meublé), deux rôles, six sujets au lieu de sept, et une
conduite qui impose au niveau 3 des phrases courtes, un renseignement à la fois
et jamais deux questions dans la même réplique.

**Les faits québécois ont été vérifiés, pas devinés.** Le bail est le formulaire
obligatoire du Tribunal administratif du logement — la Régie du logement jusqu'en
2020 — il dure habituellement douze mois et se reconduit tout seul si personne
n'envoie d'avis ; le 1er juillet est la date de déménagement usuelle et la
plupart des baux courent du 1er juillet au 30 juin ; un propriétaire ne peut
exiger ni dépôt de garantie, ni dernier mois d'avance, ni plus d'un mois de
loyer — seulement le premier ; il ne peut pas refuser un logement à une famille
avec des enfants, la Charte des droits l'interdit ; un 3 ½ a une chambre fermée,
un 4 ½ en a deux, et le demi est la salle de bain. Les personnes, l'immeuble,
l'annonce, l'adresse et le numéro de téléphone sont inventés — le numéro est
dans la plage 555-01xx, réservée à la fiction.

Ce que cette production ajoute ou confirme :

- **Les pièges de `CLAUDE.md` ont tous tenu.** `build/collecte_sons.py` n'a
  jamais été lancé — `node build/releve_sons.js module-n3-loyer` a rendu ses
  224 clés sans ouvrir de port ; les quinze bandeaux `savoir` portaient
  `speak:true` dès l'écriture ; les 57 clés de `CARRIER_PHRASES` sont les mots
  accentués, dont neuf à apostrophe, écrites entre guillemets doubles ; le champ
  `theme` du manifeste échappe son apostrophe (« Location d\\'un logement ») ;
  `render()` a été appelé sans argument, `curSec` posé avant ; `sommaire.py
  <slug>` a eu son étape d'écriture avant `--verifier`.
- **Le contrôle de cohérence en une commande `node`, réclamé par la nuit du
  20 août, a de nouveau tout attrapé du premier coup** : chaque `sec` existe
  dans `SECTIONS`, chaque clé de `PLUS` correspond à un exercice réel, aucun
  `id` d'énoncé n'est dupliqué, chaque `ok` d'`imgmatch` a son image, chaque
  `ok` de `vf` est dans ses `tiles`, chaque `write` a des `items`, chaque
  pastille `savoir` a sa phrase porteuse et chaque bloc `ana` son `say:`. Il a
  rendu **57 mots à pastille pour 57 phrases porteuses, aucune clé inutile**.
  Il mérite toujours de devenir un septième contrôle.
- **La vérification navigateur a pu se faire, cette fois**, sur le serveur de
  prévisualisation : zéro erreur console, les six sections se rendent, les onze
  mini-leçons s'ouvrent et leurs laboratoires couvrent toutes leurs
  combinaisons, les trois productions de « Je me lance » sont là avec leurs huit
  sujets et leurs six exigences, et **les quatre-vingt-dix zones de dépôt ont
  toutes une bonne réponse enregistrée** — le contrôle qui manquait le
  21 août, quand `imgmatch` lisait `aid` au lieu de `ok`. Les seuls 404 sont les
  vingt-six images absentes.
- **L'originalité : 6 identiques sur 212, soit 2,8 %**, ramenés à **0,9 %** en
  reformulant quatre chaînes. Les deux qui restent sont des entrées du lexique
  du programme. Le manifeste des sons est identique avant et après, vérifié par
  `diff` — détail dans `docs/verification-originalite.md`.
- **Un seul tableau refusé par `theme.py`** sur trente-deux, en C3, et
  raccourci sur place. La consigne « deux colonnes, quatre à six lignes,
  cellules brèves » fonctionne.
- **Les fichiers partagés n'ont voyagé nulle part.** `git status` juste avant
  chaque `commit`, chemins explicites après `--`, `git show --name-only` juste
  après : les lignes de `modules.py`, d'`activities.json` et de `server.py` sont
  parties dans le commit prévu, et y sont restées après les commits des trois
  sessions voisines. `--pathspec-from-file` pour les soixante-six fichiers des
  séances, comme la règle 1 le conseille.

### Ce qui manque à ce module, et comment le finir

**Rien n'a été tenté, et c'est voulu.** Cette session tournait dans un
environnement distant sans `~/Claude/.env` : les deux clés sont absentes, tout
appel aurait échoué. Le contenu n'a donc **pas** été ajusté au manque — les
treize cartes à photo gardent leur champ `img`, les deux `imgmatch` gardent
leurs treize illustrations, les bandeaux gardent leurs pastilles. Deux commandes
à lancer sur la machine locale, dans n'importe quel ordre.

**fal.ai · 26 images.** Treize dans `images/` et treize dans `vocab/`. Le
générateur est écrit, commenté et relançable tel quel ; il saute ce qui existe
déjà :

    python3 build/contenu/module-n3-loyer/gen_images.py

Les sept de `prPieces` : `images/cuisine.jpg`, `salon`, `chambre`,
`salle-de-bain`, `balcon-arriere`, `couloir`, `escalier-exterieur`. Les six de
`t3img` : `images/buanderie`, `fenetres-neuves`, `cour-arriere`,
`rue-stationnement`, `sous-sol-escalier`, `immeuble-facade`. Les treize du banc :
`vocab/logement`, `quatre-et-demie`, `chambre-a-coucher`, `balcon`,
`petite-annonce`, `meuble`, `chauffe`, `electricite-comprise`, `proprietaire`,
`bail`, `sous-sol`, `chauffage`, `stationnement`. Environ **0,88 $** au total.
Deux contraintes propres à ce module sont écrites dans les prompts : les
logements sont **vides** — un générateur produit spontanément des intérieurs
meublés, ce qui contredirait l'annonce « non meublé » et fausserait l'exercice —
et les papiers (l'annonce, le bail) montrent leur forme sans qu'un mot ne se
lise.

**ElevenLabs · 301 extraits.** 77 répliques sur cinq dialogues, plus les 224
clés de `sons_module_n3_loyer.json`, déjà relevé et commité. Une seule commande,
en avant-plan dans une tâche de fond de l'outil — **jamais `nohup … &`**, qui
meurt avec la commande qui l'a lancé :

    python3 generer_audio_module_n3_loyer.py

Quatre personnages, quatre voix : Dilnoza sur `feminin_2`, Claudine sur
`enseignante` — ralentie à 0,85 par `voix_lente.py`, ce qui tombe juste
puisqu'elle donne tous les loyers, les dates et les heures —, Rachid sur
`masculin_1`, Théo sur `narrateur`. Le décompte a été vérifié à vide, sans clé :
14 + 17 + 18 + 18 + 10 répliques et 224 sons. Aucune valeur du manifeste ne
contient de balise HTML, et les cinq seuls extraits d'un mot nu sont les cartes
de `prPhon`, où le mot doit précisément être dit seul.

**Et après les médias** : `python3 build/module.py module-n3-loyer` pour que le
HTML reprenne les images, puis `python3 build/materiel.py` et
`python3 maj-mur.py`. Ce dernier n'existe pas dans l'environnement distant : il
n'a pas été lancé.

**La file reprend** à l'activité 82 (niveau 3).

---

## Vague 5 — les quatre derniers niveaux (1, 4, 6, 7, 8)

Ouverte le 22 août 2026, une fois les niveaux 2, 3 et 5 fermés.

`python3 build/bilan_programme.py` dit ce qui manque et le tiendra à jour :
**28 modules**, répartis sur cinq niveaux. Trois d'entre eux sont des trous
dans des niveaux qu'on croyait finis — dont « Communication avec le personnel
de l'établissement » au **niveau 4**, que personne n'avait vu manquer.

**Ce que cette vague a de neuf, et qui commande la prudence.** Les niveaux 6, 7
et 8 sont d'un autre stade : textes suivis, argumentation, nuances. Les deux
grilles du dépôt — `GRILLE_COURTE` (8 séances) et `GRILLE_3_DEFIS` (16) —
viennent des niveaux 1 à 5 et n'ont jamais servi au-delà. Lancer neuf agents
de niveau 6 sur un gabarit non validé, c'est risquer neuf modules à refaire.
D'où l'ordre : le niveau 1 d'abord (terrain connu), **un pilote au niveau 6**
ensuite, et les vagues suivantes seulement une fois le pilote relu.

**Les numéros sont réservés ici**, et nulle part ailleurs. Un agent ne prend
jamais « le prochain numéro libre » : deux agents lancés la même minute
prendraient le même.

| Numéro | Niveau | Situation | Slug réservé |
|--------|--------|-----------|--------------|
| 96 | 1 | Inscription | `module-n1-inscription` |
| 97 | 1 | Orientation dans l'établissement | `module-n1-orientation` |
| 98 | 1 | Salle de classe | `module-n1-classe` |
| 99 | 6 | Suivi de l'actualité — **pilote** | `module-n6-actualite` |

Le pilote est « Suivi de l'actualité » parce qu'il a deux voisins déjà écrits,
`module-n5-actualite` et `module-n7-actualite` : l'agent peut calibrer le
niveau 6 entre les deux au lieu de l'inventer.

**Format** : `GRILLE_COURTE` aux numéros 96-98 (le niveau 1 est le plus court
du programme) ; au 99, l'agent décide et **écrit pourquoi** — c'est la
question à laquelle le pilote doit répondre.

### Journal de la vague 5

**22 août 2026 — activité 98, `module-n1-classe`.** « Regardez le tableau »,
niveau 1, `numero` 4, `GRILLE_COURTE`. Scénario inventé : Bopha Sok, 34 ans,
arrivée du Cambodge il y a un mois, premier lundi au centre ; madame Cyr,
l'enseignante, lui montre sa place, une chaise, un livre, un stylo ; Ivan,
arrivé d'Ukraine trois semaines plus tôt, est le voisin de pupitre qui ne
comprend pas non plus. 16 exercices, 6 mini-leçons, 5 dialogues, 14 mots,
19 images, **160 extraits audio** (37 répliques et 123 sons), 8 séances
(90 diapositives, 67 blocs de fiches). Originalité : 242 énoncés visibles,
**2 identiques** dans les 18 866 des quarante-neuf autres modules, soit 0,8 %.

*Ce qui le sépare de `module-n2-classe` (89), même situation au niveau 2* :
le programme ne donne au niveau 1 que **deux intentions, toutes deux en
compréhension orale** — comprendre l'information sur le fonctionnement de la
classe, comprendre une consigne. Aucune production, aucune compréhension
écrite. Le module ne demande donc jamais d'expliquer quoi que ce soit : au 2,
l'élève lit une directive écrite, demande une permission, annonce une absence
et explique le fonctionnement de la classe à un nouveau ; ici, une consigne
fait deux mots, la bonne réponse est un geste, le seul texte lu est l'heure sur
une horloge, et la phrase à savoir est « Pardon ? ». Les quatorze mots ne
reprennent aucun des seize du niveau 2 — le cahier, le crayon et le pupitre y
restent, le livre, le stylo, l'horloge et l'horaire sont ici.

*La deuxième entrée de lexique du niveau commande la moitié du module* :
« heure, horaire ». Le défi 2 lui est entièrement donné — l'heure juste, la
demie, midi, les jours, la feuille affichée près de la porte. C'est aussi ce
qui a décidé de la graphie-phonie : les quatre paires de nombres qui ne
diffèrent que par la fin du mot (deux/douze, trois/treize, quatre/quatorze,
six/seize), parce qu'une page, une heure et un numéro de local sont les
premiers nombres qu'un débutant doit entendre juste.

Un scénario `classe1` a été ajouté à `server.py` : le `classe` existant est
celui du niveau 2 et fait demander une permission, annoncer une absence et
expliquer les règles — trois choses que le niveau 1 ne demande pas.

Trois choses apprises, qui valent pour les modules restants :

- **Les séances se construisent avant les images.** `Deck.image()` ouvre le
  fichier avec PIL : une image pas encore produite arrête le build sur une
  erreur qui ne nomme pas sa cause. Les quatre decks à `declencheur` passent
  par une petite fonction `photo()` qui rend le chemin ou rien.
- **La reformulation des consignes génériques se fait à la fin, et coûte
  presque rien.** Seize coïncidences sur 242 énoncés — toutes des consignes
  que tous les modules finissent par écrire pareil, aucune un emprunt — ont
  fait passer l'originalité de 6,6 % à 0,8 %. Une seule valeur du relevé des
  sons a bougé, et aucun MP3 n'était encore payé.
- **`build/voix.py` n'existe pas dans un worktree ouvert avant lui.** Le
  générateur audio l'importe quand même : il arrivera par la fusion vers
  `main`. Vérifier après la fusion que l'import passe, avant de lancer les
  160 extraits.

*Restent à faire* : lancer `build/contenu/module-n1-classe/gen_images.py`
(19 images) et `generer_audio_module_n1_classe.py` (160 extraits). Les
19 écarts de `node build/coherence.js module-n1-classe` sont exactement ces
19 images absentes du disque, et rien d'autre.

---

## Le pilote du niveau 6 — ce qu'il a trouvé

**22 août 2026 — activité 99, `module-n6-actualite`.** « Suivre un sujet dans
les médias », niveau 6, `numero` 2. Scénario inventé : Nadège Beauplan,
44 ans, arrivée d'Haïti il y a six ans, tient le comptoir d'accueil de la
bibliothèque de la Batture, à Trois-Rivières. Sa laveuse de 780 $ a cessé de
vidanger après trois ans et quatre mois, et le marchand lui répond que la
garantie est expirée. Elle suit alors le même sujet à travers cinq genres :
son collègue Raphaël Choquette le lui explique, la chroniqueuse Claudine
Rousseau en fait une chronique pratique, l'animateur Théo Marchesseault
interroge Myriam Vaugeois de l'Office de la protection du consommateur, un
documentaire remonte à 1924, et le courrier des lecteurs du Courrier de la
Batture s'en empare. 24 exercices, 15 mini-leçons, 4 dialogues (75 répliques),
16 mots, 15 images, **232 extraits audio**, 16 séances. Originalité :
433 énoncés visibles, **14 identiques** dans les 14 377 des quarante-neuf
autres modules de `build/contenu/`, soit **3,2 %** — quatre consignes du
gabarit, quatre mots du programme et six intitulés de bandeau.

*Les faits québécois sont vérifiés, pas devinés*, auprès de l'Office de la
protection du consommateur le 22 août 2026 : la garantie légale veut qu'un
bien serve à l'usage normal auquel il est destiné et qu'il y serve **pendant
une durée raisonnable** compte tenu du prix payé, du contrat et des conditions
d'utilisation ; elle s'applique même quand la garantie du fabricant est
expirée ; le recours passe par une **mise en demeure** écrite, où dix jours
sont le plus souvent tenus pour un délai raisonnable, puis par la **Division
des petites créances** pour une réclamation de 15 000 $ ou moins, où l'on se
représente soi-même. Tout le reste — les personnes, la station CFTR, le journal,
les prix, les dates — est inventé.

### 1. La grille : `GRILLE_3_DEFIS`, et la règle n'est pas celle qu'on croit

Seize séances, trois défis. Mais la raison n'est **pas** que le niveau 6 serait
un niveau 5 en plus long, et ce n'est pas non plus le nombre d'intentions.

`GRILLE_COURTE` existe parce qu'un débutant du niveau 1 ou 2 n'a pas encore
l'alphabet et se fatigue : elle répond à une limite de l'élève. Au niveau 6, la
limite n'est plus là. Elle est dans la **matière** : ce qu'il y a à apprendre,
c'est de tenir le fil d'un texte suivi, et un fil ne se tient qu'en y revenant.
Trois défis, ce sont trois retours sur le même dossier sous trois angles
différents. Une grille courte n'aurait pas raccourci le module : elle aurait
obligé à choisir un genre et à jeter les trois autres, donc à laisser sans
exercice trois des quatre intentions du programme.

**La règle pour les neuf suivants**, tirée de `python3 build/cadre.py 6` :

| Situation | Intentions | Grille |
|---|---|---|
| Emploi | 5 | `GRILLE_3_DEFIS` |
| Suivi de l'actualité | 4 | `GRILLE_3_DEFIS` (fait) |
| Relations sociales | 4 | `GRILLE_3_DEFIS` |
| Communication avec le personnel de l'établissement | 4 | `GRILLE_3_DEFIS` |
| Recherche d'emploi | 4 | `GRILLE_3_DEFIS` (fait, act. 59) |
| Découverte d'œuvres | 3 | `GRILLE_3_DEFIS` |
| Consultation d'un professionnel de la santé | 3 | `GRILLE_3_DEFIS` |
| Location d'un logement | 1 | `GRILLE_2_DEFIS` |
| Problèmes reliés à l'habitation | 1 | `GRILLE_2_DEFIS` |
| Salle de classe | 1 | `GRILLE_2_DEFIS` |

**`GRILLE_COURTE` n'a sa place à aucun de ces dix modules.** Et une seule
intention ne condamne pas mécaniquement au format à deux défis :
`module-n5-actualite` n'en avait qu'une et a tenu trois défis en les tirant des
attentes de fin de cours. Le vrai test est celui-ci : **peut-on nommer trois
façons distinctes d'entrer dans la situation, chacune avec son dialogue et ses
cinq ou six exercices ?** Si oui, trois défis. Si le troisième défi ne se
remplit qu'en répétant le deuxième, deux défis — inventer une séance sans
contenu reste pire que de n'en pas avoir.

### 2. Ce que le stade intermédiaire-avancé exige, et que le gabarit ne prévoit pas

Quatre points. Le premier est le seul qui vaudrait qu'on touche au moteur ; les
trois autres se contournent, à condition de le savoir d'avance.

**a) Il n'existe aucun type d'exercice pour un texte suivi — et c'est le cœur
du niveau.** Les six types du moteur (`match`, `imgmatch`, `vf`, `write`,
`blanks`, `rows`) travaillent tous la **phrase isolée**. Or trois des quatre
intentions de compréhension écrite du niveau 6 portent sur un **texte** :
comprendre un article informatif, comprendre un fait divers, lire le courrier
des lecteurs. Le seul moyen de mettre un texte devant l'élève est de le loger
dans le bloc `savoir` d'un `vf` et de poser les questions en rangées — c'est ce
que fait `module-n7-actualite` (`t2lire`) et c'est ce que fait ici `t3fd`, avec
les cinq phrases du fait divers. Ça fonctionne, et le résultat se lit bien.
Mais c'est un détournement : le bandeau noir est fait pour une règle, pas pour
un texte ; il n'y a aucun moyen de faire cliquer l'élève **dans** le texte, ni
de lui faire retrouver un référent en le surlignant, ni d'afficher le texte à
côté des questions plutôt qu'au-dessus. **Un type `texte` — un paragraphe suivi
et ses questions — est le seul ajout au moteur qui vaudrait son coût, et il
servirait aux niveaux 6, 7 et 8 à la fois.** À ne pas entreprendre au milieu
d'une série de neuf modules : à décider avec l'utilisateur, une fois.

**b) La reprise de l'information ne s'exerce pas en une phrase.** « Je le sais »
n'a de sens qu'après la phrase qu'il reprend. Chaque item de `t1repr` est donc
écrit en **deux phrases**, la première portant le référent souligné, la seconde
le trou. Ça tient dans un `write`, mais les items font deux fois la longueur de
ceux d'un module de niveau 3, et `cols:2` devient illisible. **Tout exercice de
grammaire du texte se met en `cols:1`.** Cela vaut pour la reprise (`le`, `en`,
`y`, `où`), pour la subordonnée relative et pour la substitution lexicale — les
trois savoirs de grammaire du texte que tout module de niveau 6 devrait porter.

**c) Le programme demande de *reconnaître*, et aucun type ne fait « reconnaître ».**
Le passé simple en est le cas net : « reconnaître les verbes courants à la
3e personne » et « associer le passé simple au passé composé ». `write` fait
produire — et faire écrire un passé simple à un élève est exactement ce qu'il
ne faut pas ; `vf` fait trancher entre deux étiquettes, ce qui est pauvre. Le
seul type juste est **`match`** : la forme au passé simple d'un côté, son
équivalent parlé de l'autre. Ce savoir étant commun à tout le niveau, les neuf
modules le rencontreront : qu'ils le traitent tous en `match`.

**d) Plusieurs situations du niveau 6 n'ont *aucune* intention de production, et
« Je me lance » en réclame trois.** « Suivi de l'actualité » n'a que de la
compréhension : une intention orale, trois écrites. Les productions se tirent
alors des **attentes de fin de cours**, qui sont communes à tout le niveau et
qui, elles, sont productives — « rédige un courriel [...] pour informer son
destinataire du contenu d'un article d'intérêt général », « rédige un court
texte en organisant ses idées à l'aide de paragraphes », « décrit les étapes
d'une démarche administrative en donnant les détails nécessaires ». D'où, ici,
un compte rendu oral en trois temps et un courriel formel au courrier des
lecteurs. **Le docstring du manifeste doit dire d'où vient la production**,
sinon le module a l'air d'avoir inventé une tâche hors programme — et le
relecteur suivant la retirera.

### 3. Ce qui a résisté

**Les cinquante-quatre savoirs du niveau, dont trente en grammaire de la
phrase.** Il est impossible d'en couvrir le quart, et rien dans le programme ne
dit lesquels choisir. Le critère qui a servi, et qui se recommande :
**« est-ce que ce savoir sert à suivre un texte ? »** Il retient d'un coup la
reprise de l'information, les connecteurs, le plus-que-parfait, le passé
simple, l'hypothèse en « si », le subjonctif après verbe introducteur, la
relative en « où », la ponctuation. Il écarte tout aussi vite les déterminants
non quantifiants indéfinis, les subordonnées corrélatives, les auxiliaires
factitifs — grammaticalement intéressants, sans emploi dans la situation. Neuf
savoirs retenus sur cinquante-quatre, répartis à raison de deux ou trois par
défi.

**Ne pas recouper le voisin du 5 ni celui du 7 sur la même situation.** La
solution n'est pas de changer de sujet — elle est de changer de **travail**.
`module-n5-actualite` *raconte* un fait divers à quelqu'un qui ne l'a pas lu.
`module-n7-actualite` *démasque* l'opinion chez un auteur qui la mêle aux
faits. Le niveau 6, entre les deux, *suit un fil* : le même sujet dans cinq
genres, et ce qui est difficile n'est plus le jugement mais la cohésion — savoir
ce que reprend « le », ce que « où » rattache, ce qu'un plus-que-parfait place
avant quoi. Cette formulation-là est ce qui a débloqué le module, et elle vaut
pour les neuf autres : **le niveau 6 n'est pas un niveau 7 facile, c'est le
niveau de la cohésion.**

**Le lexique de la situation est vide**, comme presque partout. Mais au
niveau 6, les savoirs lexicaux **du niveau** nomment eux-mêmes la situation en
deux lignes (ici : « vocabulaire lié à l'univers médiatique, à l'actualité, à
l'opinion : documentaire, reportage, fait divers, courrier des lecteurs » et
« verbes et locutions exprimant l'opinion »). C'est peu, mais c'est un point de
départ ferme, et il faut aller le chercher avec `--savoirs` : la sortie sans
argument ne le montre pas.

**Une découverte payée par le pilote, sur l'audio.** Pour un exercice `vf` à
`cards:true listen:true`, le relevé de `build/releve_sons.js` rend **le texte
de la rangée**, pas la phrase porteuse de `CARRIER_PHRASES` — vérifié :
`prGraphie_gr12` vaut « un short », pas la phrase. Les clés que l'on écrit dans
`carrier.js` pour ces mots-là sont donc **inutilisées par le moteur** (et
`coherence.js` a raison de ne pas les compter comme un écart). Conséquence
réelle : ces mots partent **seuls** à la synthèse. Or l'exercice de
graphie-phonie du niveau 6 porte précisément sur « six », « dix », « un
short », « un schéma » — des mots courts que l'anglais connaît aussi. Sans le
contexte français d'`enrichir()` (`build/voix.py`, posé le 22 août), ils
seraient sortis à l'anglaise, et c'est exactement le mot dont l'élève doit
entendre la prononciation française. **Les neuf modules du niveau 6 auront tous
un exercice de graphie-phonie — le savoir est commun au niveau. Que leur
générateur audio passe par `enrichir()`, sans exception.**

### 4. Ce que je conseille aux neuf agents suivants

1. **`GRILLE_3_DEFIS`**, sauf pour « Location d'un logement », « Problèmes
   reliés à l'habitation » et « Salle de classe » — une seule intention chacune
   — où `GRILLE_2_DEFIS` est plus honnête. Jamais `GRILLE_COURTE`.
2. **Lire `build/cadre.py 6 "<situation>" --savoirs`, pas seulement
   `build/cadre.py 6 "<situation>"`.** Au niveau 6, la situation est maigre (une
   à cinq intentions) et le niveau est riche (54 savoirs). Le module se
   construit à quatre-vingts pour cent sur les savoirs communs.
3. **Neuf ou dix savoirs, pas davantage**, choisis par la question « est-ce que
   ça sert à suivre un texte ? ». Deux ou trois par défi, chacun avec son couple
   exercice + mini-leçon.
4. **Les trois savoirs de grammaire du texte — connecteurs, reprise de
   l'information, présentation matérielle — sont ce qui distingue vraiment le
   niveau 6 des niveaux 3 et 5.** Aucun module de ce niveau ne devrait s'en
   passer, quelle que soit sa situation.
5. **`cols:1` pour tout exercice de grammaire du texte** : ses items font deux
   phrases.
6. **Le passé simple se travaille en `match`**, jamais en `write`.
7. **Les productions se tirent des attentes de fin de cours**, et le docstring
   du manifeste doit le dire.
8. **Les dialogues font 18 à 20 répliques**, pas 10 à 16 : le niveau vise « des
   discours détaillés et structurés ». Compter environ **230 extraits audio**
   par module, dont plusieurs longs — le coût par extrait est plus élevé qu'aux
   niveaux 2 et 3 à nombre égal.
9. **Changer de travail, pas de sujet**, quand un voisin du 5 ou du 7 occupe
   déjà la situation. Et l'écrire dans le manifeste, en une phrase par voisin.
10. **Numéros** : `module-n6-recherche` est le `numero` 1 du niveau,
    `module-n6-actualite` le 2. Les neuf suivants prennent 3 à 11, dans l'ordre
    du tableau de la section 1 de cette note. Leurs numéros d'activité restent
    à réserver ici avant qu'un agent commence.

### 5. Les seize séances — ce que le niveau 6 leur fait subir

190 diapositives, 134 blocs de fiches, 2 049 lignes de decks. Quatre points que
les neuf modules suivants rencontreront, et qui coûtent une reprise chacun si
on ne les sait pas d'avance.

- **`d.dialogue` ne tient confortablement que quatre répliques par
  diapositive**, alors qu'un dialogue de niveau 6 en fait dix-huit à vingt.
  Au-delà de quatre, le corps du texte descend au plancher et la diapositive
  n'est plus lisible de loin. Le bon rapport : **trois pages de quatre
  répliques**, et le reste travaillé à l'écoute plutôt que projeté. C'est la
  différence la plus visible avec les niveaux 2 et 3, dont les dialogues
  tiennent en deux pages.
- **Le contrôle de densité des tableaux se déclenche sur la colonne de
  gauche**, pas sur le texte long de droite : à deux colonnes, la première ne
  reçoit que 34 % de la largeur, et un libellé de plus de vingt-cinq caractères
  se replie sur deux lignes et pousse toute la rangée. Règle pratique tirée du
  pilote : **six rangées avec note, sept rangées sans note, libellé de gauche
  sous vingt caractères.** Écrire court dès le départ ; raccourcir après coup
  se paie cellule par cellule.
- **`Slide.image()` ouvre le fichier sans garde** : un fichier absent lève une
  exception et arrête le build des seize séances. Un module dont les images ne
  sont pas encore générées se fait donc **sans aucun `image=`** — les
  déclencheurs rendent alors en pleine largeur, et la mise en page l'absorbe
  proprement. Ajouter les `image=` plus tard, quand `gen_images.py` aura
  tourné, est un geste de deux minutes ; découvrir le problème au milieu du
  build en coûte davantage.
- **Les glyphes n'ont posé aucun problème** — `œ`, `«  »`, `’`, `—`, `·`
  passent tous. Il a suffi d'éviter par principe ce que le dépôt sait déjà
  refusé : l'alphabet phonétique, la flèche `→`, `✓`, `✕`, les emojis et les
  points de suspension typographiques. Au niveau 6, la graphie-phonie porte
  justement sur des lettres et non sur des symboles (« les lettres *ch* qui se
  disent comme un *k*, dans *chronique* ») : le niveau se prête bien à la
  contrainte.

Une remarque de forme, pour que personne ne la reprenne à l'envers : **la
couleur d'une séance n'est pas celle du module.** `theme.py` donne un sens à
chacune — acier pour la compréhension orale, indigo pour la graphie-phonie,
ambre pour l'écriture et la grammaire, teal pour l'écoute et la réponse,
framboise pour le bilan — et `module-n6-recherche` les répartissait déjà ainsi.
Le pilote a suivi cette répartition, et non la couleur acier du niveau 6 : la
couleur de niveau tient l'en-tête du module, pas les séances.

---

## Vague 6 — le niveau 6 au complet

Ouverte le 22 août 2026, une fois le pilote (activité 99) livré et le type
d'exercice `texte` versé au moteur. **Lire « Le pilote du niveau 6 — ce qu'il
a trouvé » avant de commencer** : la grille de chaque situation y est décidée,
et trois pièges du stade intermédiaire y sont nommés.

**Les numéros sont réservés ici, et nulle part ailleurs.**

| Numéro | Situation | Slug réservé | Grille |
|--------|-----------|--------------|--------|
| 100 | Emploi | `module-n6-emploi` | `GRILLE_3_DEFIS` (fait) |
| 101 | Relations sociales | `module-n6-relations` | `GRILLE_3_DEFIS` |
| 102 | Communication avec le personnel de l'établissement | `module-n6-etablissement` | `GRILLE_3_DEFIS` |
| 103 | Découverte d'œuvres | `module-n6-oeuvres` | `GRILLE_3_DEFIS` |
| 104 | Consultation d'un professionnel de la santé | `module-n6-sante` | `GRILLE_3_DEFIS` |
| 105 | Location d'un logement | `module-n6-logement` | `GRILLE_2_DEFIS` |
| 106 | Problèmes reliés à l'habitation | `module-n6-habitation` | `GRILLE_2_DEFIS` |
| 107 | Salle de classe | `module-n6-classe` | `GRILLE_2_DEFIS` |

Les grilles viennent du tableau du pilote, tiré de `build/cadre.py 6` : trois
défis quand la situation porte trois intentions ou plus, deux quand elle n'en
porte qu'une. **`GRILLE_COURTE` n'a sa place à aucun de ces huit modules.**
Mais une seule intention ne condamne pas mécaniquement au format court : le
vrai test est de savoir si l'on peut nommer trois façons distinctes d'entrer
dans la situation, chacune avec son dialogue et ses exercices. Si le troisième
défi ne se remplit qu'en répétant le deuxième, deux défis — inventer une
séance sans contenu reste pire que de n'en pas avoir.

**Le type `texte` est disponible et attendu.** Chaque module du niveau 6
devrait porter au moins un exercice de compréhension d'un texte suivi : c'est
le cœur du niveau, et c'est pour ces huit modules que le type a été ajouté.
Sa forme est dans `CLAUDE.md`.

**Les agents partent quatre à la fois**, jamais huit. Cinq agents lancés
ensemble ont épuisé la limite de session le 22 août et sont morts à la même
seconde. Quatre tiennent, et la fusion de la vague précédente se fait pendant
que la suivante travaille.

### Journal de la vague 6

**22 août 2026 — activité 106, `module-n6-habitation`.** « Faire faire des
travaux », niveau 6, `numero` 9, **`GRILLE_3_DEFIS`** alors que le tableau du
pilote réservait deux défis à cette situation. Scénario inventé : Doïna
Petrescu, 46 ans, arrivée de Roumanie il y a cinq ans, aide-cuisinière dans une
résidence pour aînés de Saint-Jérôme, propriétaire depuis deux ans d'une petite
maison de 1961 rue des Mésanges. Sa mère Aurica arrive le 12 mai et il faut
aménager le sous-sol. Léandre Bergevin est le voisin qui a fait les mêmes
travaux l'an passé, Fernand Trudelle l'entrepreneur général, Kettly Alcindor
l'inspectrice en bâtiment, Réjean Toupin le service des permis. 25 exercices,
16 mini-leçons, 4 dialogues (83 répliques), 16 mots, 16 images, **341 extraits
audio** (83 répliques et 258 sons), 16 séances (191 diapositives, 131 blocs de
fiches). Originalité : 460 énoncés visibles, **5 identiques** dans les 18 937
des cinquante-sept autres modules de `build/contenu/`, soit **1,1 %**.

*Trois défis pour une intention, et pourquoi.* Le programme ne donne à cette
situation qu'une seule intention, portée deux fois — « comprendre de
l'information **et poser des questions** reliées à des travaux de réparation ou
de rénovation ». C'est le mot « et » qui tranche : l'intention est double, et
ses deux moitiés ne se travaillent pas dans la même séance. Défi 1, on
*comprend* — un homme de métier explique un diagnostic de vive voix, l'élève
reçoit. Défi 2, on *lit* — un rapport d'inspection et une soumission, deux
exercices `texte`. Défi 3, on *demande* — le chantier découvre autre chose que
prévu, quatre personnes en parlent en même temps, et c'est l'élève qui pose les
questions et qui décide. Le troisième ne répète pas le deuxième : il change de
genre (une rencontre à quatre voix), de temps (le futur et l'hypothèse en
« si » là où le diagnostic était au plus-que-parfait) et de rôle. **La règle du
pilote n'est donc pas « une intention, deux défis » : c'est « trois façons
distinctes d'entrer, trois défis ».** Une situation à une seule intention peut
en porter trois si l'intention elle-même est composite ; c'est à vérifier avant
de se rabattre sur `GRILLE_2_DEFIS`.

*Les faits québécois sont vérifiés, pas devinés*, et le module n'en avance que
**trois** : un entrepreneur qui exécute ou fait exécuter des travaux de
construction pour autrui doit détenir une **licence de la Régie du bâtiment du
Québec**, vérifiable au registre public des détenteurs de licence ; la plupart
des municipalités exigent un **permis** pour certains travaux de rénovation, et
les exigences varient de l'une à l'autre, donc elles se demandent à sa propre
municipalité ; avant de creuser, la localisation gratuite des infrastructures
souterraines se demande à **Info-Excavation**. Rien d'autre n'est présenté
comme la loi. Les personnes, les entreprises, l'adresse, les montants
(34 500 $, 6 800 $, 1 900 $), les délais et les numéros de dossier sont
inventés : une soumission ou un rapport au nom d'une entreprise réelle serait un
faux document.

*Ce qui le sépare de ses deux voisins sur la même situation*, et ce n'est pas
le sujet mais le **rapport à la chose**. `module-probleme` (45, niveau 4) est
le module du **locataire qui signale** : le calorifère du 4B, les parties
communes, l'insalubrité, le recours. `module-n5-degat` (62, niveau 5) est celui
du **locataire qui raconte un sinistre** : l'eau tombée pendant la nuit, le
constat, l'avis de travaux, la réclamation. Dans les deux, rien n'est voulu et
tout est subi, et il y a quelqu'un à convaincre. Ici, personne n'est locataire
et rien n'est arrivé : la maison appartient à celle qui parle, les travaux sont
**voulus, choisis et payés** par elle, et il n'y a personne à convaincre — il y
a un métier à comprendre. C'est le seul des trois où l'élève est celui qui
décide et qui paie.

*Deux exercices du type `texte`* : le rapport d'inspection (huit passages, huit
questions) et la soumission (neuf passages, neuf questions). Le septième
contrôle les valide sans rien signaler. La section « Historique du bâtiment »
du rapport porte le passé simple — c'est le prétexte le plus naturel qu'on
puisse lui donner à ce niveau, puisqu'un rapport recopie des archives — et le
savoir se travaille en `match`, jamais en `write`.

Trois choses apprises, qui valent pour les modules restants :

- **Le contrôle de densité des tableaux se déclenche sur la longueur des
  cellules de gauche, même à quatre rangées.** Un tableau de `b4` a été refusé
  avec quatre rangées seulement, parce que sa colonne de gauche portait des
  phrases entières (« Quand ils ont acheté, la fissure s'était ouverte. »).
  Réécrit en deux colonnes de fragments courts — « ils ont acheté » contre « la
  fissure s'était ouverte » —, il passe, et il se lit mieux de loin. La règle
  n'est donc pas un nombre de rangées : c'est **la longueur de la cellule la
  plus longue de la colonne étroite**.
- **Mesurer l'originalité ne suffit pas, il faut regarder d'où viennent les
  coïncidences.** Le premier relevé rendait 4,1 % — sous le seuil — mais
  **neuf** des dix-neuf venaient d'un seul endroit : la mini-leçon de formation
  des mots, écrite avec les mêmes intitulés que celle de `module-n6-emploi`
  (« Le verbe donne le nom en -age », etc.). Le savoir est commun au niveau, la
  formulation ne doit pas l'être. Réécrits en partant du chantier — « Ce qu'on
  fait devient un -age » —, ils ramènent l'ensemble à 1,1 %. **Ni les `sub` ni
  les `tit` ni les intitulés de bandeau sans `speak` n'entrent dans le relevé
  des sons** : le manifeste est resté à 258 clés avant et après, donc la
  réécriture n'a rien coûté en audio. C'est le troisième module de la vague à
  tomber dans ce piège ; il vaut mieux écrire les mini-leçons sans ouvrir
  celles du voisin.
- **Cinq personnages tiennent dans quatre voix** à condition de dresser la
  matrice avant d'écrire les dialogues. Ici, LÉANDRE (le voisin, dans `prep`)
  et RÉJEAN (le service des permis, dans `t3`) partagent le timbre
  « narrateur » : ils n'apparaissent jamais ensemble. C'est le dialogue le plus
  peuplé qui fixe la répartition — `t3` réunit quatre voix à lui seul —, donc
  on l'écrit en premier dans sa tête, même s'il s'écrit en dernier.

*Sur les contrôles* : les sept passent. `coherence.js` rend 16 écarts, tous
« image absente du disque » — `gen_images.py` est écrit mais n'a pas tourné, et
le générateur audio non plus : le module est livré muet et sans illustration,
les deux se rattrapent d'un seul coup. `pieds_de_page.py` signale un écart, sur
`module-n3-horaire`, étranger à ce module. `sommaire.py --verifier` ne rend
aucun lien cassé.

**22 août 2026 — activité 102, `module-n6-etablissement`.** « Choisir la
suite », niveau 6, `numero` 5, `GRILLE_3_DEFIS`. Scénario inventé : Bintou
Sangaré, 34 ans, arrivée du Mali il y a trois ans, commis de soir dans une
pharmacie de quartier de Sherbrooke, termine sa francisation en février et ne
sait pas ce qui vient après. Réal Duquette tient le comptoir de l'accueil,
Pascal Lachapelle est le conseiller d'orientation, Rosa Villalba est sa
camarade de classe, Marc-Olivier Béliveau son enseignant, et Amélie Dostie
tient l'admission du centre de formation professionnelle. 23 exercices,
15 mini-leçons, 4 dialogues (80 répliques), 16 mots, 18 images, **255 extraits
audio** (80 répliques et 175 sons), 16 séances (182 diapositives, 130 blocs de
fiches). Originalité : 1 209 énoncés visibles, **13 identiques** dans les
43 192 des cinquante-trois autres modules de `build/contenu/`, soit **1,1 %**.

*Les faits québécois sont vérifiés, pas devinés*, le 22 août 2026 : les trois
voies d'admission d'un diplôme d'études professionnelles (diplôme d'études
secondaires ou équivalent reconnu ; seize ans au 30 septembre et les unités de
4e secondaire en langue d'enseignement, langue seconde et mathématiques ;
dix-huit ans, la réussite du **test de développement général** et les
préalables particuliers) ; la distinction entre ce test et le **test
d'équivalence de niveau de scolarité**, seul à mener à une attestation valant
une cinquième secondaire ; et la portée réelle de l'**évaluation comparative
des études effectuées hors du Québec**, qui est un avis d'expert du ministère
de l'Immigration — ni équivalence de diplôme, ni permis d'exercice, ni
garantie d'admission. Le centre, les personnes, les dates et les numéros de
dossier sont inventés : un avis officiel au nom d'un vrai établissement serait
un faux document.

*Ce qui le sépare de ses cinq voisins sur la même situation*, et ce n'est pas
le sujet mais le **travail** : `module-n2-inscription` (91) s'inscrit,
`module-n2-secretaire` (95) demande un renseignement, `module-n3-secretariat`
(86) informe d'une absence, `module-travail` (39, niveau 4) justifie un retard
au téléphone, `module-n5-ecole` (74) règle une affaire déjà là. Ici rien n'est
arrivé et rien ne cloche : l'élève vient chercher de quoi **décider**. Il
assemble une dizaine de renseignements venus de trois sources qui ne disent pas
la même chose, il reçoit un avis officiel qui ne se discute pas au comptoir, et
il finit assis dans une rencontre où quatre personnes parlent de son dossier.
C'est le seul module de la série où il faut **suivre plusieurs interlocuteurs à
la fois** — le savoir « saisir les rapports entre les interlocuteurs »
n'apparaît qu'au niveau 6.

*Deux exercices du type `texte`*, un par intention de compréhension écrite du
programme : la description du programme d'études (six passages, six questions)
et l'avis d'admission conditionnelle (cinq passages, cinq questions). Le
septième contrôle les valide sans rien signaler.

Trois choses apprises, qui valent pour les modules restants du niveau :

- **Le contrôle de densité des tableaux se déclenche à six rangées, pas à
  sept**, dès que la note est un peu longue et que la colonne de gauche porte
  des libellés courts mais nombreux. Deux tableaux de `a2` et un de `c3` ont dû
  passer à cinq rangées, et la note à une phrase. La règle pratique du pilote —
  six rangées avec note — est un plafond, pas une garantie.
- **Reprendre la structure d'une mini-leçon du pilote coûte cher en
  originalité.** Les mini-leçons de graphie-phonie et de reprise de
  l'information partaient à 9,1 % de coïncidence : le savoir est commun au
  niveau, mais la formulation, elle, doit être refaite. Réécrites en ancrant
  chaque exemple dans le contexte scolaire, elles ramènent l'ensemble à 1,1 %.
  Ni les identifiants ni les textes lus à voix haute des bandeaux n'ayant
  bougé, le relevé des sons est resté identique — la réécriture n'a rien coûté
  en audio.
- **`build/liens_catalogue.py` n'existe pas sur cette branche.** Le lien des
  fiches a donc été vérifié à la main : le `studentDoc` et le `slideshow` de
  l'entrée 102 pointent sur des fichiers présents. Si le script est arrivé sur
  `main` entre-temps, le lancer après la fusion ne coûte rien.

*Sur les contrôles* : les sept passent. `coherence.js` rend 18 écarts, tous
« image absente du disque » — `gen_images.py` est écrit mais n'a pas tourné, et
le générateur audio non plus : le module est livré muet et sans illustration,
les deux se rattrapent d'un seul coup. `sommaire.py --verifier` signale huit
liens cassés, aucun de ce module : ce sont des modules inscrits au registre par
des sessions voisines et pas encore produits.
### Ce que le premier module de la vague 6 a trouvé

**22 août 2026 — activité 100, `module-n6-emploi`.** « Le poste affiché à
l'interne », niveau 6, `numero` 3. Yaneth Mosquera, 36 ans, arrivée de
Colombie il y a quatre ans, deux ans à l'expédition chez Emballages Bocage, à
Saint-Hyacinthe. Un poste de vérificatrice à la qualité est affiché au
babillard et il reste dix jours ouvrables. 24 exercices, 17 mini-leçons,
4 dialogues (84 répliques), 16 mots, 15 images, **290 extraits audio**,
16 séances, 191 diapositives. Originalité : 0,8 %.

Quatre points pour les sept modules qui restent.

**1. La situation « Emploi » est la seule du niveau qui n'a pas à emprunter
ses productions.** Ses cinq intentions couvrent les quatre compétences : la
production orale du programme est « décrire les étapes d'une démarche
administrative » et la production écrite « rédiger un courriel dans le
contexte de relations professionnelles » — ce sont, mot pour mot, les deux
blocs de « Je me lance ». Le pilote devait aller chercher les siennes dans les
attentes de fin de cours ; ici, non. Vérifier ce point pour chaque situation
avant d'écrire : c'est la première chose que `build/cadre.py` doit dire.

**2. Le type `texte` supporte très bien d'être employé deux fois dans le même
défi.** `t2note` porte la note de service, `t2polit` l'article 4 de la
politique — deux genres différents du même dossier, le premier avec des
puces, le second avec des articles numérotés. Ce n'est pas une répétition :
c'est ce que le programme demande en distinguant « lire de la documentation
interne » de la lecture ordinaire. Un bloc `savoir` se pose sur un exercice
`texte` comme sur les autres ; le moteur le rend avant la grille.

**3. Le contrôle de densité des tableaux de séance se déclenche plus tôt qu'on
ne croit.** La règle du pilote — six rangées avec note, sept sans — est
juste, mais elle suppose une colonne de gauche courte **et** une note courte.
Deux tableaux ont été refusés : l'un à six rangées dont une note de quatre-
vingt-dix caractères, l'autre à six rangées dont la colonne de gauche faisait
vingt-cinq caractères. Le remède le moins coûteux est de descendre la note
dans les `notes` de l'enseignante : elle y sert autant, et la diapositive
passe.

**4. La graphie-phonie sera la même dans les huit modules — ses phrases ne
doivent pas l'être.** Le savoir (`ch` qui dit k, `x` qui dit s, `sh`/`sch` qui
disent ch) est commun au niveau, donc chaque module portera cet exercice et sa
mini-leçon. Écrite en s'appuyant sur celle du pilote, elle a produit à elle
seule la moitié des coïncidences du relevé d'originalité. La mesure globale
restait sous le seuil (4,2 %), ce qui aurait laissé passer un quasi-doublon.
**Mesurer par module ne suffit pas : regarder d'où viennent les coïncidences.**
Le détail est dans `docs/verification-originalite.md`.

### Le premier module à deux défis du niveau 6

**22 août 2026 — activité 105, `module-n6-logement`.** « Six mois ailleurs »,
niveau 6, `numero` 8, `GRILLE_2_DEFIS`. Scénario inventé : Farida Belkacem,
39 ans, arrivée d'Algérie il y a quatre ans, aide-cuisinière dans un centre
d'hébergement de Québec, part six mois remplacer quelqu'un à Sept-Îles et veut
sous-louer son quatre et demie de la rue de la Canardière plutôt que de le
perdre. Gilles Bédard est son collègue de cuisine, Mylène Poitras la préposée
au service de renseignements du Tribunal, Lucien Tardif le locateur, Nicolas
Trudel le sous-locataire proposé. 20 exercices, 16 mini-leçons, 4 dialogues
(83 répliques), 16 mots, 15 images, **284 extraits audio** (83 répliques et
201 sons), 16 séances (172 diapositives, 124 blocs de fiches). Originalité :
1 216 énoncés visibles, **4 identiques** dans les 49 021 des cinquante-sept
autres modules de `build/contenu/`, soit **0,3 %**.

*Les faits québécois sont vérifiés, pas devinés* : le Tribunal administratif du
logement a remplacé la Régie du logement le 31 août 2020, et la Régie avait été
créée en 1980 — les deux dates servent l'exercice de passé simple. Les règles
de la **sous-location** sont celles du Code civil et elles sont stables : avis
écrit indiquant le nom et l'adresse de la personne proposée ; quinze jours pour
répondre, à compter de la réception ; consentement présumé en cas de silence ;
refus possible pour un **motif sérieux** seulement, et par écrit ; remboursement
des **dépenses raisonnables** que la sous-location occasionne ; locataire qui
demeure tenu de ses obligations. Le module s'arrête là : il ne dit **rien** de
la procédure de refus d'une **cession** de bail, qui a changé récemment. La
cession n'y est nommée que pour la distinguer de la sous-location, et le
`server.py` l'interdit explicitement à l'assistant du jeu de rôle. Tout le reste
est inventé, y compris la page Web citée, qui imite la forme d'une fiche
officielle sans en reprendre le texte : prêter à un tribunal réel une page qu'il
n'a pas écrite en ferait un faux document, et le Défi 1 dit à l'élève, dans un
bandeau, que la page du module est un exemple.

**La grille : deux défis, et le test du pilote appliqué pour vrai.** Une seule
intention au programme — « s'informer sur ses droits et ses obligations en
consultant un site Web », de compréhension écrite. Deux façons distinctes
d'entrer dans la situation tiennent debout, chacune avec son dialogue et ses
sept exercices : **le texte public** (une fiche de droits, écrite pour tout le
monde, en intertitres et en puces, où l'on cherche une règle qui ne parle de
personne) et **les deux lettres privées** (l'avis qu'on envoie, la réponse qu'on
reçoit, adressées, datées, signées, qui parlent d'un seul cas et ne disent pas
la même chose). Le troisième aurait été l'audience au Tribunal : c'est un autre
travail — parler devant un tribunal n'est plus s'informer — et c'est le terrain
de « Problèmes reliés à l'habitation » (106), qui suit dans la même vague. Le
remplir ici aurait voulu dire faire relire une troisième lettre du même dossier.
Deux défis, donc, et la répartition 4-5-5-2 se remplit sans effort : les blocs B
et C portent sept exercices chacun.

**Trois exercices du type `texte`, dont deux dans le même défi**, comme
`module-n6-emploi` l'avait montré : la fiche de droits (onze passages, onze
questions), l'avis de Farida (sept et sept), la réponse du locateur (sept et
sept). Le septième contrôle les valide sans rien signaler. Une remarque qui vaut
pour les modules restants : le type se prête particulièrement bien à **deux
textes qui se répondent**. La fiche écrit « le locataire » et « celui-ci » ; la
lettre écrit « vous » et « votre logement ». Faire chercher la même règle dans
les deux, c'est exactement la cohésion que le niveau 6 demande, et c'est ce qui
a donné sa forme au Défi 2.

Trois choses apprises :

- **Un quatrième dialogue n'a pas besoin d'une section à lui.** Le gabarit rend
  `ex.dialogue` **uniquement** pour le type `write` (une seule occurrence dans
  `build/gabarit/module.html`) : la visite du logement est donc portée par
  l'exercice sur l'hypothèse en « si », qui est un `write`. Un module à deux
  défis garde ainsi les quatre dialogues et les 80 répliques attendues au
  niveau 6, sans inventer un onglet de plus. `module-n5-logement` a un dialogue
  `t1b` qu'aucun exercice ne porte : il n'est jamais joué.
- **La flèche a encore coûté un build.** `theme.py` a refusé le deck A4 pour
  trois `→` — la mise en garde de `CLAUDE.md` est exacte, et elle vaut aussi
  pour les listes de nominalisation, où la flèche vient toute seule sous les
  doigts. Dans le HTML du module, elle passe sans problème ; c'est seulement
  dans les `.pptx` qu'elle est interdite.
- **Les intitulés partagés du niveau 6 pèsent, même sans copier une
  mini-leçon.** Écrites de zéro, sans regarder celles des voisins, seize
  mini-leçons ont tout de même rendu 2,0 % de coïncidence — pas un bloc entier,
  mais vingt titres courts et prévisibles que le savoir commun appelle : « Les
  terminaisons de la 3e personne », « Trois verbes irréguliers à connaître »,
  « Deux passés dans la même phrase », « Le subjonctif après un verbe
  introducteur ». Vingt reformulations les ramènent à **0,3 %**. Elles ne
  coûtent rien : le relevé des sons est resté identique à l'octet près, ni les
  `tit`, ni les `sub`, ni les intitulés de rangée n'entrant dans le manifeste
  des extraits. La leçon du module 100 tient donc dans les deux sens — ce n'est
  pas seulement la mini-leçon recopiée qui coûte, c'est aussi le titre qui va de
  soi.

*Sur les contrôles* : les sept passent. `coherence.js` rend 15 écarts, tous
« image absente du disque » — `gen_images.py` est écrit mais n'a pas tourné, et
le générateur audio non plus : le module est livré muet et sans illustration,
les deux se rattrapent d'un seul coup. `pieds_de_page.py` signale un écart sur
`module-n3-horaire`, antérieur et étranger à ce module. La vérification au
navigateur n'a pas pu se faire : le volet de prévisualisation était occupé par
une autre session.
### Ce que l'activité 104 a trouvé

**22 août 2026 — activité 104, `module-n6-sante`.** « Nommer ce qu'on a »,
niveau 6, `numero` 7, `GRILLE_3_DEFIS`. Scénario inventé : Leyla Demirci,
41 ans, arrivée de Turquie il y a cinq ans, aide à domicile à Rimouski, entre
chez les gens à sept heures du matin sept jours sur quatorze. Depuis février,
une fatigue qui ne part pas ; une demande de consultation partie en avril, un
appel en octobre, un rendez-vous en médecine interne ce matin à 9 h 40, à
l'Hôpital de la Baie-Ronde. Mariette Pouliot tient l'accueil de la clinique
externe, Gilles Ferron attend sa femme sur la banquette d'à côté, la docteure
Sylvine Charest est l'interniste, Pierre-Luc Nadeau l'infirmier de liaison.
23 exercices, 17 mini-leçons, 4 dialogues (85 répliques), 16 mots, 18 images,
**292 extraits audio** (85 répliques et 207 sons), 16 séances
(187 diapositives, 138 blocs de fiches). Originalité : 1 590 énoncés visibles,
**10 identiques** dans les 49 021 des cinquante-sept autres modules de
`build/contenu/`, soit **0,6 %**.

*Ce qui le sépare de ses cinq voisins sur la même situation*, et ce n'est pas
le sujet mais le **travail** : `module-n3-pharmacie` (78) demande un service au
comptoir, `module-sante` (34, niveau 4) téléphone pour obtenir un rendez-vous,
`module-consultation` (35, niveau 4) s'oriente dans le réseau et décrit une
douleur au triage, `module-n5-rendezvous` (65) raconte à son médecin de famille
un problème qui dure, `module-n5-urgence` (66) réagit dans l'urgence. Ici rien
n'est urgent et rien ne fait mal : le rendez-vous est obtenu depuis sept mois,
la spécialiste ne connaît pas la personne, et le motif tient en deux mots que
personne ne sait dire. Ce qu'il faut faire est d'une autre nature — **nommer**.
C'est aussi le seul module de la série où l'élève **parle à un autre patient**
plutôt qu'à un professionnel : l'intention « échanger avec quelqu'un dans la
salle d'attente » n'existe qu'au niveau 6, et c'est une conversation entre
égaux, sans guichet entre les deux.

*Les faits médicaux ne sont jamais inventés, parce qu'il n'y en a pas.* Le
module enseigne la langue d'une consultation, pas la médecine : rien n'y
indique quoi faire devant un symptôme, quoi prendre, quoi éviter, ni quand
s'inquiéter. Les quatre notions de santé nommées — un malaise, une fatigue
chronique, une anémie légère, des effets secondaires — le sont comme
**vocabulaire**, à la façon dont le programme les nomme lui-même. La
spécialiste ne pose aucun diagnostic, ne nomme aucun médicament, ne donne
aucune dose : elle explique une démarche, demande des examens complémentaires
et dit qu'une fatigue a beaucoup de causes possibles. Le feuillet du Défi 3 est
un feuillet **de procédure** — quoi apporter, à qui téléphoner, ce qu'un compte
rendu contient — et non un feuillet sur une maladie. Le scénario du jeu de
rôle (`specialiste`, dans `server.py`) porte l'interdiction en toutes lettres
dans la conduite du personnage, et non seulement dans un commentaire.

Ce qui n'est pas médical est tenu pour vrai à un seul endroit : le
fonctionnement courant d'un rendez-vous en spécialité — un médecin de famille
adresse une demande de consultation, une clinique externe reçoit sans
hospitaliser, on présente sa carte à l'accueil, le spécialiste envoie un compte
rendu au médecin qui a fait la demande. Tout le reste — les personnes,
l'hôpital, les dates, les numéros de dossier et de poste — est inventé : un
compte rendu au nom d'un vrai établissement serait un faux document.

*Deux exercices du type `texte`*, un par genre de l'unique intention de
compréhension écrite de la situation : le feuillet d'information (cinq
paragraphes, sept passages, sept questions) et le compte rendu de consultation
(cinq paragraphes, sept passages, sept questions). Le septième contrôle les
valide sans rien signaler.

Trois choses apprises, qui valent pour les modules restants du niveau :

- **L'avertissement du premier module de la vague se vérifie une deuxième
  fois, et il faut le prendre au pied de la lettre.** La mini-leçon de
  graphie-phonie, écrite en s'appuyant sur celle d'un voisin, portait à elle
  seule **vingt-cinq** des cinquante-cinq coïncidences du premier relevé. La
  mesure globale était pourtant de 3,5 %, sous le seuil : elle aurait laissé
  passer un quasi-doublon. Réécrite depuis la situation — le mot entendu dans
  un corridor d'hôpital, les noms d'examens et de spécialités —, elle ramène
  l'ensemble à 0,6 %. **Ne pas ouvrir le `plus.js` d'un voisin avant d'avoir
  écrit le sien.** C'est le seul moyen fiable, et il ne coûte rien.
- **La liste de mots de la graphie-phonie, elle, se recoupe forcément.** Le
  programme nomme lui-même les trois cas, et « six », « dix », « un schéma »,
  « un shampoing », « un short » n'ont pas d'équivalent à substituer. Deux des
  dix coïncidences restantes sont là, et il n'y a rien à en faire. Ce qui se
  varie, c'est la moitié du choix qu'on maîtrise : les mots de la famille `ch`
  se prennent dans le champ du module (échographie, psychiatre, cholestérol
  ici ; psychologie, orchestre, chronologie ailleurs).
- **Un module de santé peut être écrit sans donner un seul conseil de santé**,
  et le résultat est meilleur. La contrainte force à porter la matière sur ce
  que le programme demande vraiment — décrire, dater, préciser, lire un
  document — au lieu de la porter sur des contenus cliniques qui n'y sont pas.
  Elle se tient à trois endroits, et il faut les tenir tous les trois : le
  contenu, le docstring du manifeste, et la `conduite` du personnage dans
  `server.py`.

*Sur les contrôles* : les sept passent. `coherence.js` rend 18 écarts, tous
« image absente du disque » — `gen_images.py` est écrit mais n'a pas tourné, et
le générateur audio non plus : le module est livré muet et sans illustration,
les deux se rattrapent d'un seul coup. `pieds_de_page.py` signale un seul
écart, `module-n3-horaire`, qui n'est pas de ce module : c'est un module
inscrit au registre par une session voisine et pas encore produit. La
vérification dans le navigateur n'a **pas** pu être faite : le plafond d'onglets
de la session partagée était atteint. Elle est remplacée par trois contrôles
hors navigateur — `node --check` sur le script en ligne du HTML produit (320 866
octets), `node build/coherence.js`, et un relevé qui vérifie que les vingt-trois
identifiants d'exercice, les quatorze passages cliquables des deux `texte`, le
slug, le niveau et la couleur d'en-tête sont bien dans le fichier livré, et
qu'aucun jeton `%%…%%` ni aucun résidu du gabarit n'y a survécu.
### Le dernier module du niveau 6

**22 août 2026 — activité 107, `module-n6-classe`.** « Un travail de recherche
en équipe », niveau 6, `numero` 10, `GRILLE_2_DEFIS`. Milagros Zevallos,
43 ans, arrivée du Pérou il y a cinq ans, où elle était technicienne de
laboratoire, suit sa francisation le jour au Centre d'éducation des adultes des
Trois-Chênes. Son enseignante annonce un travail de recherche : trois semaines,
équipe de trois, trois sources, un texte de deux pages et cinq minutes devant
la classe. Son équipe prend le bac brun. 18 exercices, 13 mini-leçons,
3 dialogues (62 répliques), 16 mots, 20 images, **217 extraits audio**
(62 répliques et 155 sons), 16 séances, 172 diapositives, 121 blocs de fiches.
Originalité : **0 sur 323** énoncés visibles et **0 sur 651** chaînes de
mini-leçon, après reformulation — voir le point 3 ci-dessous.

*La municipalité est inventée, et c'est délibéré.* Les faits provinciaux
retenus sont généraux et établis : les matières organiques enfouies se
décomposent sans air et produisent du **méthane** ; deux traitements existent,
le **compostage** et la **biométhanisation** ; le gouvernement du Québec s'est
donné pour objectif que l'ensemble des municipalités soient desservies ; le
plastique dit « biodégradable » n'est pas accepté sans certification. Mais la
ville de Sainte-Angèle-des-Prés, son bulletin municipal, ses tonnages et ses
dates n'ont aucun modèle réel — **attribuer une page d'information fabriquée à
une vraie ville produirait un faux document, et un élève la citerait de bonne
foi dans un vrai travail.** C'est un cran de prudence de plus que pour les
autres modules : ici, la source inventée est le matériel de l'exercice.

Quatre points pour la suite.

**1. Le test des trois défis, et pourquoi il a échoué ici — proprement.**
Deux entrées se nomment sans effort : ce que l'établissement **demande** (la
consigne de travail, la grille d'évaluation) et ce que les sources
**racontent** (trois documents qui ne concordent pas). La troisième qui vient à
l'esprit — la rencontre d'équipe, la répartition, le compte rendu devant la
classe — **est déjà « Je me lance » en entier** : c'est le jeu de rôle, c'est
l'exposé oral, c'est le texte écrit. En faire un défi 3 aurait produit une
séance qui répète la suivante. C'est un cas d'échec utile à nommer, parce qu'il
ne ressemble pas à celui qu'on redoute : le troisième défi ne manquait pas de
matière, il empiétait sur une section qui existe déjà. **Avant de trancher,
regarder si la troisième entrée n'est pas « Je me lance » déguisé.**
`GRILLE_2_DEFIS` donne d'ailleurs cinq séances par défi au lieu de quatre : les
deux défis y gagnent ce que le troisième aurait pris.

**2. Trois exercices du type `texte`, et deux d'entre eux ne lisent pas un
document d'information.** La consigne de travail (`t1cons`, 6 passages) et la
grille d'évaluation (`t1grille`, 5 passages) sont des écrits qui **ordonnent** ;
la page de la ville (`t2src`, 6 passages) est un écrit qui **rapporte**. Le
type se prête aussi bien aux deux, et l'écart entre les genres est précisément
ce que le défi 1 et le défi 2 travaillent séparément. Un bloc `savoir` se pose
sans problème sur un exercice `texte` : `t1grille` en porte un, à `speak:true`,
et le moteur le rend avant la grille de questions. Le septième contrôle valide
les trois sans rien signaler.

**3. Le relevé d'originalité doit couvrir `plus.js`, pas seulement `exos.js`.**
Le relevé habituel — les énoncés visibles de `fccards.js` et `exos.js` — rendait
7 coïncidences sur 323, soit 2,2 %, toutes des consignes du gabarit. Vert. Un
second relevé, passé sur les 651 chaînes de `plus.js`, en rendait **23**, soit
3,5 % : vert aussi, et pourtant **dix-huit venaient de la seule mini-leçon de
graphie-phonie**, comparée à celle de `module-n6-etablissement`. La leçon de la
vague — mesurer par module ne suffit pas — se double donc d'une seconde : **le
relevé qui ne regarde que `exos.js` ne voit pas l'endroit où la coïncidence se
loge vraiment.** Les mini-leçons sont le plus gros fichier du module et le plus
tentant à décalquer, puisque trois de leurs savoirs sont communs à tout le
niveau. Les vingt-cinq formulations ont été refaites ; les deux relevés rendent
maintenant **0**. L'opération est gratuite en audio à une condition, vérifiée
ici : les identifiants de bloc et la **position** des `say:` ne bougent pas —
le manifeste est resté à 155 clés, à l'octet près.

**4. Trois Marisol au niveau 6, c'était deux de trop.** Le personnage
s'appelait Marisol Ferreyra, 41 ans, arrivée du Pérou. `module-n6-recherche` a
déjà une Marisol Aguirre et `module-n6-relations` une **Marisol Quintanilla,
41 ans, arrivée du Salvador** — le sosie. Rebaptisée Milagros Zevallos, 43 ans,
au prix d'un remplacement dans les six fichiers de contenu, les six decks
concernés et **le seul bloc de `server.py` qui est le mien** : le prénom sert de
`role_eleve` à trois autres scénarios de jeu de rôle, et un remplacement global
dans `server.py` les aurait cassés sans bruit. **Avant de nommer un personnage,
`grep -rl "<Prénom>" build/contenu/` — trente secondes, et le renommage après
coup coûte une heure.**

*Sur les contrôles* : les sept passent. `coherence.js` rend 20 écarts, tous
« image absente du disque » — `gen_images.py` est écrit mais n'a pas tourné, et
le générateur audio non plus : le module est livré muet et sans illustration,
les deux se rattrapent d'un seul coup. `pieds_de_page.py` sort un écart, sur
`module-n3-horaire`, qui n'a aucun `.pptx` sur cette branche et n'a rien à voir
avec ce module. Le tableau de bilan de la séance E2 a dû descendre à cinq
rangées **sans note** : le contrôle de densité l'a refusé à cinq rangées avec
note, ce qui confirme une fois de plus que « six rangées avec note » est un
plafond théorique. La flèche `→` a été retirée d'un billet de sortie de B4,
comme prévu.

*Ce qui reste* : les 20 images, les 217 extraits audio, et la vérification dans
le navigateur — la fenêtre d'aperçu était saturée par les onglets des agents
voisins et le plafond d'onglets refusait toute création. Le script inclus passe
`node --check`, `coherence.js` ne signale rien d'autre que les images, et le
HTML produit porte bien son niveau, son titre, ses deux défis et son scénario
de jeu de rôle.

---

## Vague 7 — les seize derniers modules (niveaux 4, 7 et 8)

Ouverte le 22 août 2026, une fois le niveau 6 fermé (activités 99 à 107).
`python3 build/bilan_programme.py` dit : **16 modules**, un seul trou au
niveau 4, tout le reste aux niveaux 7 et 8. C'est la dernière vague : quand
elle est close, les huit niveaux du programme sont couverts en entier.

**Les numéros sont réservés ici, et nulle part ailleurs.** Dernier numéro
utilisé au 22 août 2026 : **107** (`module-n6-classe`).

| Activité | Niveau | Situation | Slug réservé | `numero` | Grille |
|---|---|---|---|---|---|
| 108 | 4 | Communication avec le personnel de l'établissement | `module-n4-etablissement` | 17 | `GRILLE_3_DEFIS` |
| 109 | 7 | Emploi | `module-n7-emploi` | 2 | `GRILLE_3_DEFIS` |
| 110 | 7 | Recherche d'emploi | `module-n7-recherche` | 3 | `GRILLE_3_DEFIS` |
| 111 | 7 | Location ou achat d'un logement | `module-n7-logement` | 4 | `GRILLE_3_DEFIS` |
| 112 | 7 | Problèmes reliés à l'habitation | `module-n7-habitation` | 5 | au choix (2 ou 3 défis) |
| 113 | 7 | Achat de biens de consommation durables | `module-n7-achat` | 6 | au choix |
| 114 | 7 | Transactions bancaires | `module-n7-banque` | 7 | au choix |
| 115 | 7 | Publicité | `module-n7-publicite` | 8 | au choix |
| 116 | 7 | Découverte d'œuvres | `module-n7-oeuvres` | 9 | `GRILLE_3_DEFIS` |
| 117 | 7 | Salle de classe | `module-n7-classe` | 10 | au choix |
| 118 | 7 | Communication avec le personnel de l'établissement | `module-n7-etablissement` | 11 | au choix |
| 119 | 8 | Recherche d'emploi | `module-n8-recherche` | 2 | `GRILLE_3_DEFIS` |
| 120 | 8 | Emménagement dans un nouveau logement | `module-n8-emmenagement` | 3 | au choix |
| 121 | 8 | Problèmes reliés à l'habitation | `module-n8-habitation` | 4 | au choix |
| 122 | 8 | Suivi de l'actualité | `module-n8-actualite` | 5 | `GRILLE_3_DEFIS` |
| 123 | 8 | Découverte d'œuvres | `module-n8-oeuvres` | 6 | `GRILLE_3_DEFIS` |

**« Au choix » veut dire : `build/cadre.py <niveau>` décide, et l'agent écrit
pourquoi dans le journal.** La règle du pilote du niveau 6 vaut ici aussi :
trois défis quand la situation porte trois intentions ou plus, deux quand elle
n'en porte qu'une — mais le vrai test est de pouvoir nommer trois façons
distinctes d'entrer dans la situation. `GRILLE_COURTE` n'a sa place à aucun de
ces seize modules.

**Ce que les niveaux 7 et 8 imposent**, et qui est déjà écrit ailleurs :
la section « Le pilote du niveau 6 » de ce fichier (les trois pièges du stade
intermédiaire, le type d'exercice `texte`), et le paragraphe de la vague 1 sur
les discours longs, le lexique qui s'amenuise et les faits québécois à
vérifier plutôt qu'à inventer. Chaque module de cette vague porte **au moins
un exercice de type `texte`** — au niveau 8, deux.

**Deux voisins par module, presque toujours.** `module-n7-actualite` (60) et
`module-n8-emploi` (61) sont les seuls modules déjà écrits à ces niveaux ; en
revanche chaque situation existe aux niveaux 3, 5 et 6. Avant d'inventer le
scénario, lire ce que font les voisins et écrire en une phrase ce qui distingue
le sien — c'est la discipline qui a tenu l'originalité sous 1 % depuis le
niveau 2.

**Les agents partent quatre à la fois**, jamais plus, chacun dans son propre
worktree (`isolation: "worktree"`). Cinq ont épuisé la limite de session le
22 août et sont morts à la même seconde ; six lancés en « remote » sont
retombés dans le même répertoire et se sont marchés dessus. La fusion se fait
avec `python3 build/fusionner_module.py`, jamais à la main.

### Journal de la vague 7
