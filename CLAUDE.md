# Bibliothèque Francisation

Bibliothèque d'activités pédagogiques FLS (Niveau 4) pour enseignant en francisation au Québec. Serveur Python simple (`server.py`, stdlib seulement) + fichiers statiques HTML.

## Si une autre session travaille dans ce dépôt

Vérifier au démarrage (`ListAgents`), et lire **`docs/deux-agents-en-parallele.md`**
avant d'écrire quoi que ce soit. Il donne le protocole — chemins explicites au
`git add`, jamais `-A` ; la liste des six fichiers réellement partagés, le
contenu d'un module étant isolé ; la réservation d'avance des numéros
d'activité — et la répartition en cours entre les sessions.

Quatre sessions ont travaillé ici le 20 août 2026 et trois se sont nui sans le
vouloir : du travail non commité emporté sous un message sans rapport, une
session bridée par une contrainte inexistante, une information périmée
propagée. Ce fichier-ci et `docs/` sont le seul canal qui survit à la
fermeture d'une session ; un message d'agent à agent, non.

## Déploiement (Railway)

- Push sur `main` → redéploiement automatique sur Railway
  (https://bibliotheque-francisation-production.up.railway.app)
- **Python épinglé à 3.12** via `.python-version` — le module `cgi` utilisé par server.py a été supprimé en Python 3.13. Ne pas retirer ce fichier.
- Builder : Railpack (`railway.toml`) — ne pas remettre Nixpacks (buggé).
- Healthcheck : `/api/activities`. `init_storage()` tourne en arrière-plan au démarrage pour ne pas bloquer le healthcheck.

## Flux de travail important

- Quand l'utilisateur ajoute des fichiers via **catalogue.html en local**, ils arrivent dans le working tree mais ne sont PAS en ligne tant qu'on n'a pas fait `git add + commit + push`. « Mettre en ligne » = pousser sur main.
- Le serveur Railway utilise un **volume persistant** (`STORAGE_DIR`). Les fichiers `assets/interactive/` sont servis depuis le code (BASE_DIR) ; les autres assets uploadés depuis le volume. Au démarrage, `init_storage()` resynchronise les chemins des activités intégrées au code dans le volume (les dates saisies par l'utilisateur sont préservées).

## Règles sur les fichiers

- **Jamais d'espaces ni de parenthèses** dans les noms de fichiers (ex. `Fichier (1).html` → renommer en kebab-case). Ça casse le build/les URLs.
- Fichiers interactifs HTML : viser < 1 Mo. Les exports « bundler » de ~4 Mo avec assets en base64 font planter le navigateur (FILE_ERROR_NO_SPACE).
- Chaque activité dans `data/activities.json` : vérifier que `interactive`, `studentDoc`, `planCours` pointent vers des fichiers existants. Valider le JSON avant de pousser : `python3 -c "import json; json.load(open('data/activities.json'))"`.

## Correction assistée par IA (« Corrige-moi ! »)

- `assets/interactive/corrige-moi/` appelle `/api/correct-french` (server.py), qui relaie vers l'API Anthropic (modèle `claude-haiku-4-5-20251001`) pour corriger une phrase d'élève.
- Nécessite la variable d'environnement `ANTHROPIC_API_KEY` sur Railway (Variables). Sans elle, l'endpoint répond 503 proprement (pas de crash).
- Le serveur tourne en **multi-thread** (`ThreadingMixIn`) depuis l'ajout de cet appel réseau, pour ne pas bloquer les autres élèves pendant un appel API.
- `viewer.html` relaie le `code` élève à l'iframe via `?code=...` sur l'URL de l'activité — nécessaire pour que l'activité authentifie ses appels à `/api/correct-french`.
- Ne jamais coder la clé API en dur dans le code ou la partager dans le chat.
- Suivi enseignant de l'atelier : `POST /api/corrige-moi/seance`
  (`{code, themeId, themeLabel, memePhrase}`) après chaque réponse corrigée, et
  `GET /api/admin/corrige-moi?groupId=` (jeton enseignant) pour l'écran Élèves.
  Le cumul vit dans `data/corrige_moi.json` : **un seul
  enregistrement par (élève, thème)** — `answers`, `firstTryOk`, `lastSeen`.
  Distinct de `data/oral_submissions.json`, qui garde les productions orales
  déposées avec leur fichier audio. L'atelier est une pratique libre : le
  suivi ne bloque jamais le dialogue (l'appel échoue en silence).

## Reprise de la séance dans les modules

L'élève commençait un module, s'arrêtait, revenait par sa fiche — et repartait
de la première section, tout effacé. Rien n'était gardé : l'état vit dans des
variables JavaScript (`S`, `TR`, `curSec`) et `/api/student/progress` ne reçoit
que des compteurs (`zonesDone`, `firstTry`…), **jamais les réponses**. On ne
pouvait donc pas restaurer depuis le serveur.

- **La mémoire est locale**, une clé par élève et par module :
  `localStorage['<MODULE_SLUG>:<code>:etat']`. La clé se construit à partir de
  `MODULE_SLUG`, jamais d'un nom écrit en dur — sans quoi le module 9, généré
  depuis `module-consultation`, hériterait de l'avancement du gabarit.
- **Un seul point d'accroche pour sauver** : tout ce qui change l'état passe
  par `render()`, où `reSauver()` est appelé (écriture regroupée à 300 ms). Les
  champs de texte, qui n'y passent pas, se sauvent sur leur `input`, et
  `pagehide` écrit sans attendre.
- Sont gardés : la section courante, `S.pl`, `S.vfSel`, `S.fb`, les paires de
  vocabulaire, `TR.attempts`/`TR.correct`, et la valeur de tous les `.winput`
  et `textarea` — donc aussi le courriel de « Je me lance ».
- **La reprise n'est jamais une prison** : la bannière « Tu reprends où tu
  étais » porte un bouton « Recommencer le module » qui efface et recharge.
- **La greffe passe par `build/greffe_reprise.py`**, jamais à la main :
  cinq régions marquées `REPRISE-*:début/fin`, dégreffe avant regreffe,
  `--retirer` pour dégreffer. Elle est réversible **à l'octet près** : chaque
  région occupe des lignes entières, et le dégreffage ne mange pas le saut de
  ligne qui la précède (sinon une ligne vide s'ajoute à chaque passage).
  `python3 build/greffe_reprise.py` traite les onze modules ; il saute
  `module-probleme`, **généré**, dont le `build.py` appelle la même `greffe()`.
- La bannière n'a **aucune couleur en dur** : son filet reprend `--hdr-accent`,
  donc elle prend la couleur du module.

## Dépôt des productions (oral et écrit)

**Rien ne part sans un geste de l'élève.** `/api/correct-french` et
`/api/check-written` répondent à l'écran et n'écrivent rien : la correction
reste privée. Ce qui atteint l'enseignant, c'est ce que l'élève envoie.

- **Oral** : `POST /api/oral/submit` (multipart), audio dans
  `assets/oral-submissions/`, fiche dans `data/oral_submissions.json`.
- **Écrit** : `POST /api/ecrit/submit` (JSON — pas de fichier joint, le texte
  tient dans l'enregistrement), fiche dans `data/written_submissions.json`.
- Lecture enseignante : `GET /api/admin/{oral,written}-submissions?groupId=`,
  suppression `DELETE .../<id>`. Filtrées au groupe, jeton obligatoire.
- **La greffe du bouton écrit passe par `build/greffe_depot_ecrit.py`**, jamais
  à la main : marqueurs `DEPOT-ECRIT:début/fin`, dégreffe avant regreffe,
  `--retirer` pour dégreffer. Elle **enveloppe `renderCorr()`** au lieu de
  modifier `peCheck()` — le module garde son code, et le bouton n'apparaît
  qu'une fois la correction demandée : on ne dépose pas un texte non relu. Le
  libellé de la tâche et la consigne se lisent dans la carte (`.prod-tit`,
  `.prod-lead`), donc aucune table à tenir module par module.
  `module-probleme` est **généré** : sa greffe est posée par son `build.py`.
- Côté enseignant, les dépôts paraissent dans le panneau « Productions écrites
  des élèves » de `lms.html` et dans la fiche individuelle.

## Fiche de l'élève (`fiche-eleve.html`)

Un seul élève à la fois, tout ce qu'il a fait : bilan, activité par activité
(zones, taux du premier coup, erreurs), productions orales et écrites avec leur
rétroaction, vocabulaire, « Corrige-moi ! », fichiers ouverts. Les tableaux de
`lms.html` répondent à « où en est le groupe ? » ; cette page répond à
« qu'est-ce que cet élève a fait ? ». On y arrive par l'icône de fiche à côté
de chaque code, ou par `fiche-eleve.html?code=XXXXXX` — le code de l'URL
choisit l'élève, donc une fiche se partage par son lien.

- Elle passe par `js/prof.js` (jeton + groupe) et lit le tableau de bord de
  l'élève avec son code. Aucune donnée écrite en dur.
- **Les dates se découpent à la chaîne**, jamais `new Date('2026-08-16')` :
  la chaîne serait lue en temps universel et affichée la veille au Québec.
- La tuile « Modules » compte les activités `categorie === 'cours'`, pas
  `activitiesTotal`, qui recense tout le catalogue, ateliers compris.
- **Le chevron d'une rangée d'activité ouvre ce que l'élève y a remis** —
  enregistrements et textes, rattachés par le préfixe du `taskId` comme dans
  `progression.html`. Le détail est déjà dans la page, seulement `hidden` : le
  déplier ne refait pas les sept appels du dossier. Sans remise, pas de chevron.

## Progression des élèves (`progression.html`)

Le tableau de bord du **groupe**, module par module : `enseignant.html` sert à
planifier, `fiche-eleve.html` répond à « qu'a fait cette personne ? », et cette
page-ci à « où en est la classe dans ce module, et qu'est-ce qui m'est arrivé ce
soir ? ». On y entre par le bouton « Progression des élèves » de l'écran
« Élèves » du portail, ou par `progression.html?module=<id>` — le module choisi
reste dans l'adresse, donc une vue se partage par son lien.

- **Deux filtres, et tout en découle** : le module regardé (ou tous) et la
  période — *aujourd'hui* (la soirée même), *depuis l'ouverture du module*
  (la `datePrevue` du module **pour ce groupe**), *depuis toujours*.
- Quatre blocs : le bilan en tuiles, une rangée par élève (avancement, taux du
  premier coup, enregistrements, textes, dernière trace, lien vers le dossier),
  les envois de la période lisibles et écoutables sur place, puis la liste des
  modules du groupe.
- **Le chevron d'une rangée déplie les envois de cet élève**, la même carte que
  la liste de la période mais sans répéter son nom. Comme dans le portail, il
  ne promet jamais du vide : sans envoi dans la période, pas de chevron.
- **Un envoi se rattache à son module par `taskId`** (`module-travail-po`,
  `module-travail-pe`) : le préfixe est le dossier du module, qu'on retrouve
  dans le chemin `interactive` de l'activité. Aucune table à tenir à jour ;
  le `theme` ne sert que de repli.
- **« Fait » se compte sur les élèves entrés**, jamais sur l'effectif : un
  groupe garde des codes d'avance et des absents. Un module est fait quand il
  est fermé ou que la moitié des élèves entrés l'a terminé — et un module fermé
  où personne n'est entré n'est pas fait.
- La progression est **un enregistrement par (élève, activité, événement)**,
  son `timestamp` étant celui de la dernière mise à jour : « aujourd'hui » se
  lit donc « travaillé aujourd'hui », pas « tout ce qui a été fait aujourd'hui ».
- Mêmes règles que la fiche : jeton par `js/prof.js`, dates découpées à la
  chaîne, aucune couleur en dur, chaque état porte glyphe **et** mot.

## Le direct de la classe (bloc en tête de `progression.html`)

**Ce que `progress.json` ne pouvait pas dire.** `/api/student/progress`
n'envoyait que des compteurs — `zonesDone`, `firstTry`, `totalErrors` — et
jamais les réponses. On savait donc où en était un élève, mais **jamais la
réussite d'une question**, qui est la seule chose utile pendant qu'une classe
répond sur ses téléphones. Trois pièces, livrées le 27 août 2026 ; la
proposition est dans `assets/presentations/direct-de-la-classe.html`.

| Pièce | Où | Ce qu'elle fait |
|---|---|---|
| `zone_repondue` | `build/greffe_direct.py` | un envoi par tentative, avec l'énoncé de la zone |
| `data/direct.json` | `server.py`, `db.py` | un enregistrement par (élève, activité, zone) |
| `GET /api/direct?groupId=&activityId=&section=` | `server.py` | le regroupement, prêt à afficher |

- **C'est un tampon, pas une trace.** `progress.json` continue de porter
  l'avancement ; perdre `direct.json` ne fait perdre aucune progression. Il
  n'est pas versionné, comme les autres traces d'élèves.
- **Le verrou ne couvre que le chemin fichier.** `_enregistrer_direct` portait
  d'abord `@sous_verrou`, comme les onze méthodes qui font une
  lecture-modification-écriture. Mais en base, l'écriture est un `ON CONFLICT DO
  UPDATE` qui ne relit rien : le verrou global aurait fait passer **toutes** les
  écritures du serveur derrière une classe qui répond, pendant un aller-retour
  vers Postgres — le mur que la migration avait fait tomber, remis en place par
  une précaution. Le décorateur est donc retiré et `donnees_verrouillees()`
  entoure la seule branche fichier, comme le fait déjà
  `_handle_student_progress`. Mesuré : 30 écritures simultanées → **30
  enregistrements sur 30** (0,17 s) sur le chemin fichier.
- **Aucune purge à tenir.** Un enregistrement par (élève, activité, zone),
  **réécrit** : la table grandit avec la classe, pas avec le temps. « En ligne »
  n'est pas un état gardé, c'est une trace fraîche — `DIRECT_EN_LIGNE_MIN`,
  dix minutes, parce qu'un exercice long se fait en silence.
- **Le texte d'une réponse ouverte ne monte pas.** La greffe n'envoie `reponse`
  que pour un vrai/faux, un glisser-déposer ou une case portant `accept` — de la
  comparaison de chaînes, déjà corrigée sur l'appareil. Une case corrigée par
  l'assistant n'envoie que juste/faux et le nombre d'essais. **Et le serveur ne
  fait pas confiance au module sur ce point : sans `bonne`, il jette
  `reponse`.** Vérifié en envoyant le texte quand même — il n'arrive pas dans
  le fichier.
- **Le ✓ d'une réponse suit le verdict du module**, jamais une comparaison
  refaite au serveur. Le premier jet recomparait la chaîne à la bonne réponse :
  une réponse marquée fausse dans le module ressortait cochée verte chez
  l'enseignante dès que la casse différait. Deux normalisations pour une même
  question, c'est le défaut « deux sources pour une idée » — vu à l'écran, pas
  en relisant. `_direct_net()` ne sert plus qu'à **regrouper** les écritures
  d'une même réponse (« Je suis retard » et « je suis retard. » font une ligne).

### La greffe enveloppe, elle ne modifie pas

`build/greffe_direct.py` remplace `window.trackPlacement` par une enveloppe qui
appelle l'originale puis rapporte. Même parti pris que `greffe_depot_ecrit.py`
avec `renderCorr()` : le module garde son code, et **les sept endroits** qui
appellent `trackPlacement` — vrai/faux, glisser-déposer, vocabulaire, texte,
cases à écrire — sont couverts d'un coup. Une fonction déclarée au premier
niveau d'un script classique est une propriété de `window` : la remplacer
change ce que voient les appels suivants.

    python3 build/greffe_direct.py --tous     # gabarit + les 87 modules
    python3 build/greffe_direct.py --retirer

Elle **ne connaît ni slug ni numéro d'activité** : le code de l'élève et
l'identifiant de l'activité se lisent dans l'adresse de la page parente, comme
le fait déjà `lmsTrack()`. C'est ce qui permet de la poser sur le gabarit sans
qu'un module généré hérite de l'identité d'un autre — et donc de ne pas
l'ajouter aux cinq greffes de `build/module.py`.

### Les trois décisions de l'écran

- **Le défi par défaut, le module en dépliant.** Vingt-quatre questions ne
  tiennent pas sur un projecteur. La section montrée d'office est celle dont la
  trace est **la plus fraîche** — celle où la classe travaille, pas la première.
  Les titres viennent de `/api/sections`, donc du découpage produit par
  `build/sections.py` : aucune table de sections écrite dans la page.
- **Cinq secondes tant que l'onglet est visible**, rien quand il est masqué
  (`visibilitychange`), et un bouton de pause. Un onglet oublié compterait des
  élèves partis comme des élèves en ligne.
- **L'anonymat est un réglage d'affichage, pas une permission.** L'enseignante a
  déjà accès aux dossiers nommés ; l'interrupteur sert à **projeter** un texte
  sans exposer son auteur. En anonyme, un rang stable (« Élève 7 ») — le même
  dans la grille et dans le mur des textes, pour qu'on puisse dire « le
  troisième texte » sans nommer personne. Et **l'élève ne voit rien de tout
  ça** : aucune route ne le lui rend.
- **Le bloc a sa donnée, son conteneur et son rythme** (`#pgDirect`), séparés du
  reste de la page. Le mêler à `rendre()` ferait reconstruire les tableaux et
  refermer les chevrons toutes les cinq secondes.
- Il ne s'imprime pas : c'est un écran de séance, pas un document.

## L'espace direction (`direction.html`)

**Gérer des comptes et regarder une dépense n'est pas enseigner.** « Les
chiffres » s'ouvrait depuis la barre du portail enseignant : un écran de
gestion dans la page où l'on prépare sa classe. Il en est sorti le 27 août
2026, remplacé par le lien **« Espace direction »**, qui ne paraît qu'à qui a
la charge d'un centre — et c'est le serveur qui le dit
(`/api/direction/portees`), jamais un rôle deviné dans la page.

**Une seule page, deux portées.** Une direction y voit son centre ; le
fondateur voit le réseau et ouvre les comptes de direction. Deux pages
auraient tenu les mêmes tableaux en double, et ce dépôt sait ce que deux
formulations d'une même règle finissent par faire.

| Route | Qui y entre |
|---|---|
| `GET /api/direction/portees` | toute session — rend ce que le compte peut administrer |
| `GET /api/direction/centre?orgId=` | `direction`/`conseiller` **sur ce centre précis**, ou le fondateur |
| `GET /api/direction/reseau` | le fondateur seul |
| `PATCH /api/direction/enseignants/<id>` | idem centre — règle l'IA d'une personne |
| `POST /api/direction/invitations` | `direction` sur le centre (rôle `prof`) ; `direction` en plus pour le fondateur |

- **Le goulot supprimé** : les invitations étaient **fondateur seulement**, et
  le commentaire du code le disait — « le fondateur ouvre tous les comptes du
  réseau ». Une direction invite maintenant ses enseignants, bornée à son
  centre. Ouvrir une **direction** reste au fondateur : ouvrir un pair est un
  pouvoir, pas une tâche courante.
- **Un conseiller consulte, il n'ouvre pas de compte.** `peutInviter` est
  rendu par le serveur et revalidé à l'écriture — l'écran ne doit pas offrir un
  geste que le serveur refusera.
- **`a_role_sur(..., exact=True)`**, comme la vue par enseignant des chiffres :
  un gestionnaire de CSS a le centre dans son sous-arbre et reste refusé. La
  règle est la même des deux côtés parce que la donnée est la même.

### Le drapeau IA par enseignant

Le champ `ia` (`herite` · `autorisee` · `interdite`) existe désormais **sur le
compte** en plus des nœuds de l'arbre. **Le plus précis gagne** : le drapeau de
la personne tranche, puis on remonte les nœuds. C'est la règle déjà écrite pour
les organisations — « celui qui a négocié une exception la porte écrite sur
elle-même » — et en avoir une seconde ici obligerait à expliquer, devant chaque
bouton grisé, laquelle des deux s'applique.

- `ia_pour_eleve()` passe par **le titulaire du groupe** avant le centre.
  `ia_pour_enseignant()` et `centre_de_enseignant()` portent la résolution ;
  les dix routes gardées par `_ia_refusee()` n'ont pas bougé.
- **Le message du refus ne nomme plus le centre** (« pas activée pour ta
  classe ») : la décision peut venir de la personne. Une interface qui décrit
  l'ancienne règle est un défaut, pas un détail.
- **Vérifié en jouant les trois combinaisons**, pas en relisant : centre
  *interdite* + personne *autorisée* → l'élève a l'IA ; centre *interdite* +
  personne *héritée* → refus au nom du centre ; et `/api/outils/traduire`
  répond bien 403 dans le second cas.

### La dépense par enseignant

**Le registre ne note ni l'enseignant ni le centre** : il note l'élève et son
**groupe** (`journal_api.py`). La clé se dérive donc — groupe → titulaire,
groupe → centre — par `journal_api.par_cle()`, plutôt que d'ajouter au registre
deux champs qui seraient faux le jour où un groupe change de main et
fausseraient rétroactivement tout l'historique.

- **Ce que le chiffre dit est écrit à l'écran** : ce sont les **élèves** qui
  appellent les modèles. « La dépense d'un enseignant », c'est ce que ses
  groupes ont dépensé. Et c'est un montant **estimé** par la table de tarifs,
  jamais la facture.
- **`sansCle` est une chaîne, pas une paire.** Les appels qu'aucun groupe ne
  porte — le tri d'un signalement — n'appartiennent à aucun centre. Les
  déballer comme les autres faisait **planter la vue réseau entière** ; trouvé
  en fabriquant la ligne dans un bac d'essai, pas en relisant. La vue rend donc
  `totalUsd` **et** `totalCentresUsd`, et la page nomme l'écart : sans lui, la
  somme des centres ne recompose pas le total et c'est la page qui a l'air
  fausse.

### Deux pièges de la page, tous deux vus en la jouant

- **`Prof.init({ redirect: true })` éjecte qui n'a aucun groupe.** Le renvoi
  vers `enseignant.html` est fait pour les pages de planification ; une
  direction qui n'enseigne pas n'a pas de groupe et se retrouvait dehors de son
  propre écran. `direction.html` appelle donc `redirect: false` et vérifie la
  connexion sur `/api/prof/me`.
- **La confirmation posée avant `recharger()` disparaît**, puisque le
  rechargement remet la ligne d'état à vide : le réglage passait et l'écran
  restait muet. Le message vient après.

## Multi-enseignants et multi-groupes

- Hiérarchie : **enseignant → groupes → élèves**. Le catalogue d'activités est
  **commun** à tous les enseignants ; ce qui appartient au groupe, c'est la
  planification (dates), les élèves, la progression, le journal et les
  productions orales.
- **Les dates ne sont plus portées par l'activité** mais par `data/schedule.json`
  (`{groupId, activityId, dateVue, datePrevue, dateFin}`, plus un `sectionId`
  facultatif — voir « Sections datées »). Deux enseignants
  peuvent donc placer la même activité à deux moments différents. Les champs
  `dateVue`/`datePrevue`/`dateFin` restants dans `activities.json` ne servent
  plus qu'à amorcer la migration ; ne rien y écrire.
- **Un groupe neuf part vide.** Une activité n'est offerte à un groupe que si
  elle a une `datePrevue` pour ce groupe (`is_offered()`). Sans date, l'élève
  ne la voit pas du tout — pas même en « à venir ». L'admin affiche alors
  « Non offerte à ce groupe ». La migration ouvre explicitement au groupe
  historique tout ce qui lui était déjà visible, pour ne rien retirer à la
  classe en cours.

## Le stockage Postgres (`db.py`)

**Le repli est la règle, pas l'exception.** Sans `DATABASE_URL`, ou sans le
pilote, `db.disponible()` répond « non » et tout écrit dans les fichiers du
volume — le comportement d'avant la migration. Revenir en arrière, c'est
retirer une variable d'environnement ; les fichiers ne sont jamais effacés.

    DATABASE_URL=… python3 build/migrer_postgres.py --etat    # ce qu'il y a
    DATABASE_URL=… python3 build/migrer_postgres.py --essai   # sans écrire
    DATABASE_URL=… python3 build/migrer_postgres.py           # migre

**En production, la migration se fait au démarrage, pas en ligne de commande.**
`migrer_vers_postgres()` tourne dans le fil d'initialisation : les fichiers
source vivent sur le volume Railway, et une commande lancée d'un poste local
migrerait les données du poste local. Elle ne fait rien si la base contient
déjà quoi que ce soit — rejouer une migration remettrait l'état des fichiers
par-dessus le travail fait depuis. `build/migrer_postgres.py` reste l'outil
d'inspection (`--etat`) et de reprise manuelle.

**`GET /api/health` dit quel stockage sert** : `{"stockage": "postgres" |
"fichiers", "migre": "faite" | "inutile" | "jamais" | …}`. Railway ne passe pas
`DATABASE_URL` d'un service à l'autre tout seul ; sans ce témoin, rien ne dit
de l'extérieur si la variable est arrivée jusqu'au serveur. Il ne rend que le
nom du stockage, jamais l'adresse ni les identifiants.

**L'ordre du démarrage a été payé.** Le premier jet plaçait la migration en
dernier, « pour copier l'état corrigé par les migrations précédentes ». Mais
celles-ci écrivent par la couche de stockage : sans schéma, chacune échouait
sur `relation "documents" does not exist`, et la copie n'avait jamais lieu — le
serveur tournait sur le repli fichier **en croyant être en base**. Le bon ordre
est l'inverse : poser le schéma, copier le volume, puis laisser les migrations
idempotentes travailler sur la base.

- **Deux formes de rangement, et la différence n'est pas cosmétique.** Les
  collections petites et bornées (comptes, groupes, arbre, accès, planification,
  invitations…) sont une **ligne de `documents`**, la liste entière en JSONB :
  on y gagne l'atomicité et l'indépendance du volume. Les **journaux d'élèves**
  (progression, accès, signaux d'aide, vocabulaire) sont une **ligne par
  enregistrement**, avec l'index unique qui porte la règle métier. L'écriture
  devient un `INSERT … ON CONFLICT DO UPDATE` : on ne relit plus la liste pour
  y ajouter une ligne. **C'est là qu'était le mur.**
- **Mesuré, pas supposé** : 600 écritures (30 élèves × 20 activités, 30 en
  parallèle) — **7,89 s en fichiers, 2,63 s en base**, et l'écart grandit avec
  la taille, puisque le fichier se réécrit en entier à chaque appel. Après ces
  600 écritures, `progress.json` pesait déjà 176 Ko.
- **La liste `db.DOCUMENTS` est explicite, jamais « tout ce qui traîne dans
  data/ ».** `materiel.json` et `sections.json` sont **produits par le build**
  et décrivent ce que le dépôt livre : les mettre en base créerait une deuxième
  vérité. Ce qui n'est pas nommé reste sur le volume, et c'est le défaut sûr.
- **Une erreur de base retombe sur le fichier, et c'est une correction.** Le
  premier jet rendait une liste vide, au motif que le fichier est périmé après
  la migration. Mais si la base tombe en pleine séance, une liste vide **vide le
  portail** — plus de groupes, plus d'élèves — et l'enseignante recrée ce
  qu'elle croit perdu. Le fichier est peut-être en retard, mais il est
  plausible et la classe continue de lire son matériel ; les écritures, elles,
  échouent bruyamment de toute façon. Même principe que le verrou des
  sections : un dispositif qui se trompe ne doit pas fermer la classe.
- **`migrer_postgres.py` refuse d'écraser une base déjà peuplée** sans
  `--forcer` : rejouer la migration remettrait l'état des fichiers par-dessus
  le travail fait depuis. C'est le seul geste vraiment irréversible.

### Le défaut que seul l'essai pouvait trouver

`load_sessions()` lisait le fichier **en direct**, sans passer par
`_load_json_list`. Dès que `save_sessions` a écrit en base, les jetons partaient
dans Postgres et on les cherchait sur le disque : **plus aucune connexion
enseignante n'était valide**. Le serveur démarrait parfaitement et répondait 401
à tout le monde.

Neuf autres collections avaient le même défaut. Toutes passent désormais par
`_load_json_list` / `_load_json_doc` / `_save_json`, qui sont **les seuls points
qui connaissent Postgres**. Le contrôle tient en une ligne, et il doit rendre
zéro :

    grep -n "open(\(STUDENTS\|ACCESS_LOG\|PROGRESS\|SESSIONS\|VOCAB_PROGRESS\|VOCAB_TRANSLATIONS\|ORAL_SUBMISSIONS\|WRITTEN_SUBMISSIONS\|CORRIGE_MOI\|SIGNAUX_AIDE\|SIGNALEMENTS\|ANALYSES_ERREURS\)_FILE" server.py

La leçon générale : **une couche d'abstraction ne vaut que si personne ne
passe à côté**, et c'est un `grep`, pas une relecture, qui le dit.

## Les écritures concurrentes (verrou et écriture atomique)

**Trouvé le 25 août 2026 en préparant la migration Postgres, et mesuré :
trente élèves qui terminent un exercice en même temps écrivaient
8 enregistrements sur 30.** Huit connexions étaient coupées par-dessus le
marché. Ce n'était pas un risque théorique — c'était une classe entière qui
perdait son travail, en silence, sans une ligne dans le journal.

La cause : presque toutes les écritures sont des **lecture-modification-
écriture du fichier entier** (`load_progress()`, on ajoute, `save_progress()`),
et le serveur est multi-thread depuis l'ajout des appels d'API. Deux requêtes
lisent la même liste et la réécrivent l'une après l'autre ; la seconde efface
la première.

- **`_VERROU_DONNEES`, réentrant, couvre la séquence entière** — la lecture
  autant que l'écriture. Protéger le seul `save` ne sert à rien : c'est la
  lecture qui doit être dans la section critique.
- **Le décorateur `@sous_verrou` plutôt qu'un `with` au milieu de la méthode.**
  La séquence à protéger commence à la première lecture ; un bloc posé à la
  main se décale au premier remaniement, et l'indentation à retoucher est une
  source d'erreur en soi. Onze méthodes le portent — vocabulaire, journal
  d'accès, dépôts oral et écrit, « Corrige-moi ! », signaux d'aide, ajout et
  retrait d'élève.
- **`_save_json` écrit maintenant de façon atomique** (fichier voisin puis
  `os.replace`). Un serveur tué au milieu d'un `json.dump` laissait un fichier
  tronqué — et `_load_json_list` repart alors sur une **liste vide**, ce qui
  efface tout ce que le fichier contenait.
- **La mesure est le contrôle.** Trente requêtes simultanées sur
  `/api/student/progress`, `/api/student/access` et les signaux d'aide :
  8/30 avant, **30/30 après**, sur les trois. Un correctif de concurrence qu'on
  n'a pas fait échouer d'abord ne prouve rien.

## Le réseau multi-centres (étapes 1 et 2 : l'arbre décide de la portée)

Le chantier est décrit dans `assets/presentations/reseau-des-centres.html`
(fiche sur `presentations.html`). **Étapes 1 et 2 livrées le 25 août 2026** :
l'arbre des organisations existe, se tient à jour, et c'est lui qui décide
désormais qui voit quels groupes.

**`role: "admin"` ne veut plus dire « voit tout ».** Un administrateur voit ce
que son accès lui donne — son centre, s'il y est posé en `direction`. Le champ
`role` du compte ne sert plus qu'aux **pouvoirs** (ouvrir un compte, promouvoir
un dépôt) ; la **portée**, elle, se lit dans `data/acces.json`. Ne pas
rebrancher l'un sur l'autre : c'est précisément la confusion que l'étape 2 a
défaite.

- **Deux fichiers du volume, non versionnés** : `data/organisations.json`
  (`{id, type, parentId, nom, actif}`, type parmi `reseau · css · centre`) et
  `data/acces.json` (`{id, teacherId, orgId, role, actif, accordePar,
  accordeLe}`). Un groupe porte désormais un `centreId` ; son `teacherId` ne
  dit plus la propriété, il dit **qui est titulaire**.
- **Une permission est un rôle posé sur un nœud, et vaut sur tout le
  sous-arbre.** C'est une **table**, jamais une colonne sur le compte : une
  même personne enseigne parfois dans deux centres, et on doit pouvoir lui
  retirer un rattachement sans toucher à son compte — le désactiver la
  couperait de l'autre centre.
- **Le rôle `prof` est le seul qui ne voit pas tout son sous-arbre.** Son accès
  dit *où il enseigne*, pas *ce qu'il voit* : `groupes_de_portee()` le restreint
  aux groupes dont il est titulaire. Sans cette exception, un enseignant
  rattaché à un centre verrait les groupes de tous ses collègues — défaut trouvé
  au bac d'essai de l'étape 1, pas en relisant le code.
- **`migrate_organisations()` tourne au démarrage, après
  `migrate_multi_groupes()`**, et elle est idempotente : arbre d'amorce (réseau
  → CSS → centre, noms réglables par `RESEAU_NOM` / `CSS_NOM` / `CENTRE_NOM`),
  groupes sans centre rattachés au centre d'amorce, une ligne d'accès par compte
  qui n'en a aucune. Le fondateur se pose sur le **réseau**, pas sur le centre :
  sur le centre, il ne verrait pas les CSS à venir.
- **`GET /api/admin/organisations`** — lecture seule, **fondateur seulement**
  (403 pour tout le reste, y compris un `admin`). C'est la seule fenêtre sur
  l'arbre tant qu'il n'y a pas d'écran, et elle rend aussi les orphelins
  (groupes sans centre, comptes sans accès).
- **Le contrôle, à passer comme les autres** — il n'écrit rien et sort en
  code 1 au premier écart :

      python3 build/controles/organisations.py           # contrôle
      python3 build/controles/organisations.py --etat    # + l'arbre à l'écran

  Il attrape ce que rien d'autre ne regarde et qui ne lève aucune erreur en
  service : un `parentId` dans le vide, un cycle, un rôle posé sur un type de
  nœud qui n'a pas de sens (`prof` sur un CSS), un groupe sans centre, un compte
  sans accès, deux fondateurs. Les six ont été **injectés dans un bac d'essai et
  vus détectés** — un contrôle qu'on n'a pas fait échouer ne prouve rien.

- **Les deux replis de `groups_of_teacher()`, à ne pas retirer.** Un verrou qui
  se trompe ferme une classe, et c'est le seul défaut de ce dépôt qu'on ne
  rattrape pas le lendemain. La portée retombe donc sur l'ancienne règle quand
  **l'arbre est vide** (installation neuve, migration pas encore passée) et
  quand **une personne n'a aucune ligne d'accès** — celle-là avec un `[WARN]`
  au journal, et le contrôle sort en écart. `_groups_of_teacher_avant_larbre()`
  n'est pas du code mort : c'est ce repli.
- **`teacher_can_access_group()` passe par `groups_of_teacher()`** au lieu de
  retester la portée. Deux formulations d'une même règle finissent toujours par
  diverger — c'est le défaut que l'étape 2 vient de supprimer, on ne le
  réintroduit pas dans la même fonction.
- **L'équivalence a été prouvée avant l'échange, pas après** :
  `organisations.py --portee` compare l'ancienne règle et l'arbre compte par
  compte et groupe par groupe. Elle ne vaut que tant qu'il n'y a **qu'un
  centre** ; au-delà, une divergence est normale et le contrôle le dit au lieu
  de crier au défaut. Elle a été **vue échouer** sur un arbre où un groupe avait
  changé de centre sans son enseignant — quatre écarts nommés.
- **Créer nourrit l'arbre, supprimer l'éteint.** Un groupe créé reçoit son
  `centreId`, un compte créé sa ligne d'accès (`prof`, ou `direction` si le
  compte est `admin`), et supprimer un compte **éteint** ses accès au lieu de
  les effacer. `retirer_acces(teacherId, orgId=None)` retire d'un centre sans
  toucher au compte : une personne rattachée à deux centres qui quitte l'un
  garde l'autre.
### La console du réseau (`reseau.html`)

Étape 3, première tranche. **Lecture seule**, réservée au **compte fondateur**
— refus côté serveur (403), et la page ne promet pas un écran qu'elle
n'obtiendra pas. On y entre par le bouton « Console du réseau » de `prof.html`,
qui ne paraît qu'au fondateur ; sans lui, la page n'était atteignable qu'en
tapant son adresse.

- **Sa raison d'être, ce sont les orphelins.** Un groupe sans centre ou un
  compte sans accès continue de travailler — c'est le repli de l'étape 2 — et
  ne se voyait jusqu'ici que dans les journaux Railway, que personne ne lit.
  `build/controles/organisations.py` ne lit que le volume **local** : il ne peut
  rien dire de la production. Cette page est le seul endroit d'où l'on voit
  l'arbre réel.
- **Les orphelins comptent dans les totaux.** Sans cela, la page annonçait
  « 2 groupes » juste au-dessus d'une bannière qui en signalait un troisième —
  et c'est la page qui avait l'air fausse, pas la donnée. Trouvé en jouant la
  page avec un orphelin fabriqué, pas en relisant le code.
- **Aucune couleur en dur, aucun jeton inventé** : un contrôle en dix lignes
  compare les `var(--…)` de la page aux jetons réellement définis dans
  `assets/design-system/`. Il a rendu zéro manquant.
- **`prof.html` disait une chose devenue fausse** : « un compte administrateur
  … voit tous les groupes ». Depuis l'étape 2, le rôle ne porte plus que les
  **pouvoirs** ; ce que chacun voit vient de son rattachement. La consigne a été
  réécrite dans le même commit — une interface qui décrit l'ancienne règle est
  un défaut, pas un détail.

### Les gestes d'écriture et le journal d'audit

Étape 3, deuxième tranche. **Toutes ces routes sont réservées au fondateur**
(`_require_founder()`, 403 sinon) et **toutes écrivent au journal**.

| Route | Geste |
|---|---|
| `POST /api/admin/organisations` | ouvrir un CSS ou un centre |
| `PATCH /api/admin/organisations/<id>` | renommer, activer, désactiver |
| `POST /api/admin/acces` | poser un accès |
| `DELETE /api/admin/acces/<id>` | **éteindre** un accès (jamais l'effacer) |
| `PATCH /api/admin/groupes/<id>/centre` | rattacher un groupe — le geste qui répare un orphelin |
| `GET /api/admin/audit` | le journal, les plus récentes d'abord (`?limite=`) |

- **Les refus sont au serveur, et ils ont chacun leur motif en clair.** Sept
  d'entre eux ont été joués et vus refuser : un centre sous le réseau, un CSS
  sous un centre, un second réseau, un nom vide, un rôle `prof` sur un CSS, une
  `direction` sur le réseau, un compte inexistant.
- **Deux refus protègent la console d'elle-même** : on ne retire pas l'accès du
  fondateur (plus personne ne pourrait la rouvrir) et on ne désactive pas le
  réseau (sa portée s'éteindrait avec). Ce sont les seuls gestes irréparables
  par l'interface elle-même.
- **Le rôle `fondateur` ne s'accorde pas.** Il se déduit de `founder_id()` — le
  compte du premier démarrage. Le distribuer ferait deux vérités pour une même
  question, et le contrôle sort déjà en écart sur deux fondateurs.
- **`journal()` n'échoue jamais l'appelant.** Un journal qui fait planter le
  geste qu'il enregistre est pire que pas de journal : on perdrait l'action
  *et* la trace. Il écrit un `[WARN]` et laisse passer. Verrou d'écriture,
  comme le cache des traductions — le serveur est multi-thread.
- **Les gestes qui existaient déjà y sont aussi** : ouvrir un compte, le
  supprimer, créer un groupe. Un journal qui ne couvrirait que les routes
  neuves mentirait par omission.
- `data/audit.json` est du volume, non versionné, en **ajout seulement**.

### Les gestes à l'écran

Étape 3, troisième tranche. `reseau.html` n'est plus en lecture : on y ouvre un
CSS et un centre, on renomme, on pose et on retire un accès, et on rattache un
groupe orphelin.

- **Chaque geste est posé là où il s'applique** : « Ouvrir un centre » est sur
  son CSS, « Poser un accès » sur son centre. Aucun formulaire ne demande
  « sous quoi ? » après coup. Un bouton absent est un geste que le serveur
  refuserait — même parti pris que `prof.html`.
- **Le message d'erreur affiché est celui du serveur, mot pour mot.** La page ne
  reformule pas un refus : c'est le serveur qui en connaît le motif, et deux
  formulations d'une même règle finiraient par diverger.
- **Un seul chemin d'écriture** : `agir()` appelle, affiche, puis recharge tout.
  Pas de mise à jour locale de l'affichage — une page qui se croit à jour sans
  avoir relu le serveur finit par montrer un arbre qui n'existe pas.
- **Le geste qui compte est « Rattacher »** : la bannière des orphelins porte un
  sélecteur de centre par groupe sans centre. C'est la réparation pour laquelle
  la console a été faite.
- **Tous les gestes ont été joués dans la page, pas seulement appelés** :
  rattacher un orphelin (bannière disparue), ouvrir un CSS puis son centre,
  refuser un renommage à nom vide (« Le nom est requis », en style d'erreur),
  renommer pour de bon, poser un accès `direction`, le retirer (la ligne passe
  à « Éteint », elle ne disparaît pas), et le journal qui enregistre les six.
  L'arbre construit ainsi repasse le contrôle sans écart.

### Les invitations (`bienvenue.html`)

Étape 3, quatrième et dernière tranche. **Un compte s'ouvre par jeton : on
n'envoie jamais un mot de passe**, même quand c'est le fondateur qui crée le
compte.

| Route | Qui | Geste |
|---|---|---|
| `POST /api/admin/invitations` | fondateur | inviter une personne **ou une liste collée** |
| `GET /api/admin/invitations` | fondateur | les invitations, sans jamais un jeton |
| `DELETE /api/admin/invitations/<id>` | fondateur | annuler — le lien cesse aussitôt |
| `GET /api/invitation?jeton=` | **public** | ce que la personne invitée voit |
| `POST /api/invitation` | **public** | crée le compte, pose l'accès, ouvre la session |

- **Le jeton se garde comme un mot de passe, en empreinte.** Il ouvre la
  création d'un compte ; le lire dans un fichier reviendrait à lire un mot de
  passe. SHA-256 suffit — un jeton de 256 bits tiré au hasard n'a pas de
  dictionnaire à lui opposer — et la comparaison passe par
  `hmac.compare_digest`, parce que `==` laisse fuir le préfixe commun par le
  temps de réponse. **Vérifié : le jeton en clair n'est nulle part sur le
  disque.**
- **Le lien ne s'affiche qu'une fois**, à la création, et la page le dit en
  toutes lettres. Sans cet avertissement, on ferme l'onglet et on recommence.
- **Une adresse fautive n'annule pas les autres.** Sur un collage de trente,
  tout refuser pour une faute de frappe ferait recommencer les vingt-neuf
  bonnes : le serveur rend deux listes, `invitations` et `refusees`, chacune
  avec son motif, et l'écran montre les deux.
- **Les deux routes publiques ne disent rien de plus qu'un « non ».** Un jeton
  faux ou périmé ne révèle ni le courriel visé, ni le centre, ni s'il a jamais
  existé.
- **`valider_acces_sans_compte()` existe parce qu'une invitation vise un
  courriel sans compte.** On ne peut pas vérifier le compte, mais on doit
  vérifier que le rôle a un sens sur ce nœud — sinon l'invitation créerait un
  accès que le contrôle déclarerait en écart le lendemain.
- **La liste des rattachements suit le rôle choisi**, à l'écran comme au
  serveur : proposer un centre pour une « gestion CSS » serait offrir un geste
  qui sera refusé.
- **Le parcours a été joué en entier dans le navigateur** : lien valide,
  mots de passe différents, mot de passe trop court, création, atterrissage
  direct dans `enseignant.html` avec la session déjà ouverte, puis le même
  jeton refusé la seconde fois. Et côté console : import d'une liste mêlant
  bonnes et mauvaises adresses, annulation d'une invitation — **suivie de la
  preuve que son lien ne fonctionne plus**, qui est le seul test qui compte.
- Une invitation vaut `INVITATION_JOURS` (14 jours) et ne sert qu'une fois.
  Annuler, c'est faire expirer : la ligne reste, le journal aussi.
- `data/invitations.json` est du volume, non versionné.

**L'étape 3 est complète.**

## Le portail des chiffres (étape 4)

### Le relevé quotidien, et la cloison qu'il porte

**Les tableaux de bord ne lisent jamais le journal d'événements** : ils lisent
`data/stats_jour.json`. Ce n'est pas une optimisation, c'est la cloison
elle-même — le relevé a **deux grains**, et la vue d'un CSS ne lit que le
premier :

- `jours` — par journée et par **centre**. Aucun identifiant d'enseignant.
- `parEnseignant` — par journée, centre **et** enseignant. Lu seulement par la
  vue d'un centre et par celle du réseau.

L'agrégation se fait donc à l'écriture, pas à l'affichage. Un filtre s'oublie
dans une requête ; une colonne absente ne fuit pas. **Vérifié sur la réponse
réelle** : la vue CSS ne contient ni `teacherId`, ni nom de personne, et sa
colonne s'appelle `rattachements`, jamais « enseignants ».

- **Les jours passés ne se recalculent jamais.** Le journal est en ajout
  seulement : une journée close ne bouge plus. Seul le jour courant est refait.
  C'est ce qui permettra au relevé de tenir quand `progress.json` fera des
  millions de lignes, et c'est pourquoi il n'a besoin d'**aucune tâche de
  nuit** — vérifié : un second passage sans événement du jour ne réécrit même
  pas le fichier.
- **Une séance d'élève se ferme après 30 minutes sans événement**
  (`STATS_PAUSE_MIN`), et un événement isolé compte pour une minute
  (`STATS_EVENEMENT_MIN`). Sans la borne, un onglet resté ouvert la nuit
  gonflerait tout un centre ; avec zéro pour l'événement isolé, un élève qui a
  réellement travaillé disparaîtrait. **Ce chiffre est un plancher**, et les
  écrans doivent le dire — rien ne mesure le temps réel passé dans une activité.
- **Les élèves actifs ne s'additionnent pas** d'une journée à l'autre : un élève
  venu cinq jours ferait cinq élèves. Le relevé ne garde qu'un nombre, donc on
  rend `elevesActifsPointe`, le maximum d'une journée — le seul chiffre honnête
  qu'il permette.

### Les trois vues, et qui y entre

| Route | Qui y entre |
|---|---|
| `GET /api/stats/reseau` | le fondateur seul |
| `GET /api/stats/css?orgId=` | `gestion_css` ou `conseiller` **sur ce CSS ou au-dessus** |
| `GET /api/stats/centre?orgId=` | `direction` ou `conseiller` **posé sur ce centre précis** |

- **`a_role_sur(..., exact=True)` tient la décision du 25 août 2026.** La vue
  par enseignant exige un accès posé **sur le centre lui-même** : un
  gestionnaire de CSS a le centre dans son sous-arbre et reste refusé. Joué et
  vu refuser, avec le motif en clair.
- **Réseau : personnes ≠ rattachements.** Les deux chiffres sont rendus
  séparément et nommés dans la réponse. Une même personne dans deux centres est
  *un* enseignant pour le réseau et *deux* lignes pour la somme des centres ;
  les deux sont justes et ne seront jamais égaux.
- **La vue d'un centre réunit deux sources** : les personnes rattachées, et
  celles qui y sont **titulaires d'un groupe**. Elles ne se recouvrent pas —
  le fondateur enseigne sans être rattaché à un centre. N'en lire qu'une faisait
  disparaître un enseignant de la liste pendant que son activité comptait au
  total du centre : le détail et le total se contredisaient, et c'est le détail
  qui avait tort. Un titulaire sans rattachement sort avec `rattache: false`.
- **`derniereConnexion` est écrite à la connexion.** C'était la seule mesure
  honnête de « ce compte a-t-il déjà servi ? » ; la deviner depuis les traces
  d'élèves se tromperait sur une enseignante qui prépare avant que sa classe
  ait rien ouvert. Elle appartient à la **personne**, pas au rattachement.

### L'écran (`chiffres.html`)

Trois vues dans une page — réseau, CSS, centre — en onglets. On y entre par
« Les chiffres » dans la barre de `enseignant.html`.

- **La page ne devine jamais sa propre portée : elle la demande.**
  `GET /api/stats/portees` rend ce que la personne a le droit de regarder.
  Sans cette route, l'écran devrait essayer chaque vue et lire les 403 — il
  apprendrait alors l'existence de CSS et de centres interdits rien qu'en
  comptant les refus. **Vérifié : un gestionnaire de CSS reçoit son CSS et une
  liste de centres vide**, donc il n'apprend même pas quels centres ont une vue
  par enseignant.
- **Le lien de la barre suit la même règle** : il ne paraît que si la portée
  n'est pas vide, et c'est le serveur qui le dit. Le `role` du compte ne porte
  plus la portée depuis l'étape 2 ; le deviner dans la page le referait mentir.
- **Un compte enseignant ne voit rien ici**, et la page l'envoie à
  `progression.html`, qui répond à « où en est mon groupe ? ». Vérifié qu'aucun
  nom de CSS ni de centre ne fuit dans son HTML.
- **Trois mises en garde sont écrites à l'écran, pas en note de bas de page**,
  parce qu'elles changent la lecture des colonnes qu'elles touchent : les
  minutes sont un **plancher**, la pointe d'élèves actifs est le **maximum d'une
  journée** et jamais une somme, et les chiffres par enseignant mesurent
  **l'adoption, pas la performance** — liste alphabétique, aucun classement.
- **La vue d'un CSS dit « rattachements », jamais « enseignants »**, et la
  colonne la plus utile est la moins flatteuse : *jamais connectés*, qui dit où
  la formation n'a pas été faite.

**L'étape 4 est complète.** Reste la migration Postgres, qui attend une
décision sur la dépendance externe.

- **Ce qui n'est pas fait, et pourquoi** : la migration vers Postgres, annoncée
  avec cette étape dans le document. Elle est restée dehors — `requirements.txt`
  dit « aucune dépendance externe », et toucher les trente `load_*`/`save_*` de
  `server.py` dans le même commit que l'arbre aurait rendu la régression
  impossible à isoler. L'arbre étant maintenant figé, la migration déplacera un
  schéma arrêté au lieu d'une cible mouvante.

## Sections datées (« sous-modules »)

Un module s'ouvre **par sections** : l'enseignante donne une date à « Défi 2 »
comme elle en donne une au module. Trois pièces, et une règle.

- **Le découpage est produit, jamais écrit à la main** :
  `python3 build/sections.py` écrit `data/sections.json` en lisant la constante
  `SECTIONS` de chaque module (`--verifier` compare sans écrire). Recopier ces
  listes les ferait diverger à la première réécriture d'un module. Le fichier
  se lit depuis BASE_DIR, comme `data/materiel.json` : il décrit le code livré.
- **Les dates vivent dans `data/schedule.json`**, dans des entrées portant un
  `sectionId`. Une entrée sans `sectionId` reste celle du module entier, et
  `schedule_for_group()` ne renvoie **que** celles-là — y mêler les sections
  avancerait ou reculerait la date d'une activité selon celle de son dernier
  défi. Les sections passent par `sections_schedule_for_group()`.
- **La règle : une section sans date propre suit son module**
  (`is_section_offered()`), et une section n'est jamais ouverte si son module
  ne l'est pas. C'est ce qui laisse les modules déjà planifiés s'ouvrir en
  entier comme avant : le découpage n'a retiré aucune activité à personne.
- **Retirer les dates d'une section supprime son entrée** plutôt que d'y
  laisser des champs vides — la section revient au régime de son module.

Côté élève, l'élève ouvre le fichier du module directement : c'est donc **le
module qui verrouille ses propres onglets**. `python3 build/greffe_sections.py`
greffe le nécessaire dans les onze modules (idempotent, `--retirer` dégreffe) :
il appelle `GET /api/student/sections?code=&activityId=`, grise les onglets
fermés avec leur date d'ouverture et repose l'élève sur la première section
ouverte si la sienne vient de se fermer. Le numéro d'activité est injecté par
la greffe depuis `activities.json` — un module ne connaît pas son propre id.
**Le silence ouvre tout** : sans code élève, sans serveur ou sans découpage, on
ne verrouille rien. Un verrou qui se trompe fermerait la classe.
`module-probleme` est **généré** : sa greffe est posée par
`build/module.py module-probleme`, jamais à la main.

## La chaîne de production des modules

Un module interactif n'est plus écrit à la main : il est **assemblé** à partir
d'un gabarit commun et de son contenu. Trois emplacements, un seul sens de
lecture.

- `build/gabarit/module.html` — le moteur, commun à tous les modules, percé de
  vingt jetons `%%NOM%%`. **Produit, jamais écrit à la main** :
  `python3 build/gabarit.py` le régénère depuis `module-consultation`, en y
  appliquant les améliorations qui valent pour tous (section vocabulaire à
  trois exercices, moteur de jeu de rôle, blocs de production refaits, grille
  des réponses courtes, tuiles Vrai/Faux à largeur variable). À côté de lui,
  `production.css`, `vocab.css` et `vocab.js` : les ressources génériques qu'il
  incorpore.
- `build/contenu/<slug>/manifest.py` — l'identité : couleur d'en-tête, thème
  LMS, consignes envoyées à l'IA de correction, scénario du jeu de rôle, texte
  de fin, et la liste des résidus interdits. **Ni `titre` ni `niveau`** : ils
  viennent de `build/powerpoints/modules.py`, qui se déclare source unique et
  les porte déjà. Les redéfinir ici ferait une source de plus — le défaut de
  numérotation à trois sources que ce projet traîne déjà — et le build refuse
  une valeur qui contredirait le registre.
- `build/contenu/<slug>/*.js` — le contenu pédagogique : `dialogues`,
  `sections`, `fccards`, `exos`, `carrier`, `plus`, `custom`.

```
python3 build/gabarit.py                 # après une amélioration du moteur
python3 build/module.py module-probleme  # un module
python3 build/module.py --tous           # tous ceux de build/contenu/
```

**Ne jamais éditer le HTML produit** — la prochaine construction l'écrase, et
une refonte a déjà été perdue ainsi. Toute correction se fait dans `build/`.

Pourquoi cette séparation : jusqu'au 20 août 2026, `module-probleme` était
fabriqué par un script à lui de 365 lignes qui appliquait quatre-vingt-treize
kilo-octets de retouches au HTML de la consultation. Ces retouches étaient
génériques, mais captives d'un seul module — d'où dix modules sur onze écrits à
la main, et une correction de design à refaire dix-huit fois. Le découpage
gabarit/contenu a été validé par reconstruction : le nouveau
`build/module.py` reproduit `module-probleme` **à l'octet près** (306 683
octets), ce qui reste le test de non-régression de la chaîne.

Deux pièges déjà payés :

- **Les marqueurs de fin de région n'ont pas de saut de ligne.** Un marqueur
  qui en contient un saute silencieusement jusqu'au bloc suivant et avale la
  constante d'après.
- **Les icônes vont avec le moteur, pas avec le contenu.** Le gabarit les
  appelle par `/assets/interactive/<slug>/icons/…`, un chemin qu'il fabrique à
  partir du slug : chaque module a donc besoin de sa propre copie des quatre
  SVG. Elles vivent dans `build/gabarit/icons/`, à côté de `production.css` et
  de `vocab.js`, et `build/module.py` les recopie à chaque construction. Avant
  le 23 août 2026 il ne le faisait pas, et l'oubli ne se voyait nulle part :
  le bouton reste cliquable, seule l'image manque, et ni le build, ni
  `coherence.js`, ni le `node --check` ne regardent là. Trois 404 dans le
  journal du serveur, et rien d'autre — `module-n3-recherche-emploi` les
  traînait depuis sa livraison.

- **Les cinq greffes partagées** — barre d'outils, dépôt de l'écrit, verrou
  des sections, reprise de séance, identité de marque — commencent chacune par
  retirer celle du gabarit, qui porte le slug (ou le numéro d'activité) de la
  consultation. Sans ce dégreffage, un module hériterait du carnet d'un autre.
- **Régénérer le gabarit ne détruit aucune greffe** — et la raison est le
  dégreffage ci-dessus, pas autre chose. Le gabarit **porte** les marqueurs des
  greffes : `MARQUE-FRANCIS` s'y lit aux alentours de la ligne 904, arrivé là par
  le HTML de `module-consultation`, déjà greffé. Ce sont `build/module.py` et
  ses cinq greffes qui les remettent d'aplomb à chaque construction, chacune en
  retirant d'abord la précédente. Conséquence pratique : `python3
  build/gabarit.py` peut être relancé sans précaution, même pendant qu'une
  autre session travaille sur l'identité de marque. Corollaire, dans l'autre
  sens : le `degreffe()` en tête de chaque greffe n'est **pas** du code mort —
  le retirer ferait empiler un bandeau de plus à chaque build. Un doute là-dessus
  a déjà coûté à une session de s'interdire `gabarit.py` pour rien.
- **La bonne réponse d'un `imgmatch` se lit sous `ok`, pas sous `aid`.** Le
  moteur ne lisait que `aid`, la clé de `module-consultation`, d'où il est
  sorti ; les modules assemblés depuis `build/contenu` écrivent tous `ok`,
  comme les `vf` et les `rows`. La zone n'avait donc aucune bonne réponse et
  **aucune photo n'était jamais acceptée** — glisser-déposer cassé dans les
  trente-quatre modules à `imgmatch`, sans la moindre erreur en console.
  Corrigé le 21 août 2026 : `cv:(r.ok!==undefined?r.ok:r.aid)`, `aid` restant
  toléré pour `module-consultation` et `module-probleme`. Le type `match`, lui,
  n'a que `aid` — c'est de là que venait la confusion. Ce que cet épisode
  enseigne : un exercice qui ne lève pas d'erreur peut être mort. Un module
  neuf mérite qu'on place une bonne réponse et qu'on vérifie qu'elle est
  acceptée, pas seulement que la page s'affiche.

- **Le type `texte` : un texte suivi et ses questions** — ajouté le 22 août
  2026, pour les niveaux 6, 7 et 8. Les six autres types travaillent tous la
  **phrase isolée**, or trois des quatre intentions de compréhension écrite du
  niveau 6 portent sur un **texte**. Le contournement d'avant — loger le texte
  dans le bandeau noir d'un `vf` — se lit bien mais interdit de faire cliquer
  l'élève *dans* le texte. C'est le pilote du niveau 6 (activité 99) qui a
  buté dessus et l'a demandé.

  ```js
  {sec:'d1', id:'t1art', type:'texte', num:'Exercice 2',
   tit:"Ce que dit l'article", color:'#3F6C51',
   sub:"Choisissez une question, puis cliquez dans le texte.",
   paras:[
     "La garantie protège l'acheteur [[ap|même après la fin de la garantie]].",
     "[[nb|Nadège]] a envoyé une mise en demeure. Elle donne [[dx|dix jours]]."
   ],
   rows:[
     {id:'q1', q:"Qui a envoyé la lettre ?", ok:'nb'},
     {id:'q2', q:"Combien de temps le marchand a-t-il ?", ok:'dx'},
     {id:'q3', q:"Jusqu'à quand la garantie protège-t-elle ?", ok:'ap'}
   ]}
  ```

  `[[identifiant|les mots]]` marque un passage cliquable ; le `ok` d'une
  question est l'identifiant du passage. L'élève arme une question, clique le
  passage, et le lien se voit des deux côtés. Recliquer un passage déjà pris
  le libère — sans quoi une erreur de clic n'aurait pas d'issue visible. Le
  texte reste **à côté** des questions au-dessus de 900 px, au-dessus en
  dessous : c'est tout l'intérêt du type, garder le texte sous les yeux.

  Trois pièges, que `node build/coherence.js` attrape désormais : un `ok` qui
  ne désigne aucun passage (la question devient invalidable), un passage
  cliquable qu'aucune question n'attend (l'élève le prend pour une réponse
  possible), et un exercice sans paragraphe. Le texte des `paras` est échappé
  **avant** que les balises soient posées : un article de journal est plein de
  guillemets et d'apostrophes, et les rendre bruts casserait le script du
  module.

- La consigne de correction de la production **écrite** ne vit pas dans le
  gabarit : `build/greffe_depot_ecrit.py` la pose. L'ancien script croyait la
  remplacer et son `replace` était sans effet — code mort découvert en
  généralisant.
- **Le build assemble du JavaScript qu'il ne lit jamais.** Une apostrophe non
  échappée ou une accolade à la place d'un crochet, quelque part dans les sept
  fichiers de contenu, produit un HTML de la bonne taille, sans erreur, dont le
  script entier meurt sur une `SyntaxError` : plus un seul exercice ne
  s'affiche, et la première personne à le voir est l'élève. Le contrôle qui
  manquait, à passer après chaque `build/module.py` :

      python3 - <<'PY' > /tmp/inline.js
      import re, pathlib, sys
      h = pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')
      print(max(re.findall(r'<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>', h, re.S), key=len))
      PY
      node --check /tmp/inline.js

  Deux façons de tomber dedans, toutes deux rencontrées le 21 août 2026 en
  produisant le niveau 7 : le champ **`bravo`** du manifeste doit échapper son
  apostrophe (`l\\'actualité`) au même titre que `relance`, dont la
  documentation le disait déjà — aucun module ne l'avait montré avant, parce
  qu'aucun titre ne contenait d'apostrophe ; et les lignes d'un bloc `piege` de
  `plus.js` sont des **tableaux**, donc fermées par `]`, jamais par `}`.
- **Les clés de `CARRIER_PHRASES` sont les mots accentués**, tels qu'ils
  paraissent dans les listes `savoir[…][2]` de `exos.js`. Le gabarit fait
  `CARRIER_PHRASES[w]` sur le mot affiché : une clé écrite en slug (`allee`
  pour « allée ») n'est jamais trouvée, et la pastille lit alors le mot seul —
  mal prononcé, ce que la phrase porteuse existe précisément pour éviter.
  Rien ne le signale : le build passe, l'audio se paie, et le défaut ne
  s'entend qu'à l'écoute. Découvert le 21 août 2026 en produisant
  `module-n3-vetements`. `module-n3-epicerie` a été corrigé le même jour —
  quatre pastilles lisaient le mot seul (`allée`, `dépanneur` deux fois,
  `mise en garde`), quatre MP3 refaits. Le relevé passé sur les vingt et un
  `build/contenu/*/carrier.js` en laisse **deux** qui portent encore le
  défaut, non corrigés : `module-n1-presenter` (`prenom`, `epeler`, `de_rien`
  contre « prénom », « épeler », « de rien ») et `module-n2-autobus`
  (`tout_droit` contre « tout droit »). Le même relevé, en trente lignes de
  node sur `fccards.js`+`exos.js`+`carrier.js`, est ce qui attrape le défaut ;
  des clés simplement **inutilisées** sont normales et ne se corrigent pas.
- **`carrier.js` doit commencer par `const CARRIER_PHRASES = `**, comme les
  six autres fichiers de contenu commencent par le leur. Un commentaire
  d'en-tête arrête le build : le commentaire va **dans** l'objet. Vérifié une
  seconde fois le 21 août 2026 sur `fccards.js`, en produisant l'activité 79 :
  la règle vaut pour **tous** les fichiers de contenu, pas seulement
  `carrier.js`, et le message d'erreur est explicite (« ne commence pas par
  'const FC_CARDS = ' »). Une note qui ne rentre pas dans l'objet va dans le
  docstring de `manifest.py`, qui est fait pour ça.
- **Les clés de `CARRIER_PHRASES` se relèvent, elles ne s'écrivent pas.**
  Trente lignes de node qui compilent `fccards.js`+`exos.js`+`carrier.js`,
  extraient les listes `savoir[…][2]` et comparent **dans les deux sens**
  rendent en une seconde les mots sans phrase porteuse et les clés inutiles.
  C'est ce qui a donné 60 clés pour 60 mots du premier coup à l'activité 79,
  et c'est le seul moyen fiable d'éviter le défaut des clés en slug décrit
  ci-dessus. Le même script vérifie utilement, dans la foulée, que chaque
  bloc `savoir` porte `speak:true`, que chaque bloc `ana` de `plus.js` porte
  son `say:`, que les clés de `PLUS` correspondent à un exercice réel et
  qu'aucune image référencée ne manque sur le disque.
- **Le relevé des sons se fait aussi hors navigateur.** Une page de module
  ouverte en `data:` ou en `file:` ne peut pas écrire dans `localStorage` :
  `render()` y échoue, et le relevé par le DOM rend **zéro** pastille de mot
  sans rien signaler. Vingt lignes de node sur `exos.js`, `carrier.js` et
  `plus.js` reproduisent les trois endroits du gabarit qui appellent
  `playWord` — le bloc `savoir` (`ex.id+'_savoir_'+ri+'_'+wi`), les exercices
  `vf` à cartes (`ex.id+'_'+r.id`) et `plAudioManifest()` — et donnent le même
  résultat que la console, vérification faite.
- **Le relevé des sons se fait maintenant par `build/releve_sons.js`**, et
  `build/collecte_sons.py` n'a plus à être lancé du tout :

      node build/releve_sons.js module-n2-classe > sons_module_n2_classe.json

  Vingt lignes de node sur `exos.js`, `carrier.js` et `plus.js`, qui
  reproduisent les trois endroits du gabarit appelant `playWord`. Écrit le
  21 août 2026 en produisant `module-n2-classe`, et validé en le rejouant sur
  `module-n2-bonjour` : il rend ses 164 clés **et leurs valeurs** à l'octet
  près. Il supprime d'un coup les deux incidents ci-dessous — plus de port à
  surveiller, plus de collecteur oublié en tâche de fond. Le point à ne pas
  perdre si le gabarit change : le suffixe des clés de `plus.js` est
  **l'indice du bloc** dans `blocs`, pas un compteur.
- **Arrêter `build/collecte_sons.py` dès que le relevé est obtenu autrement.**
  Il n'expire pas : il attend un seul envoi, et il écrit `sons_<slug>.json`
  quand celui-ci arrive — même longtemps après qu'on a cessé d'y penser. Laissé
  en tâche de fond après un relevé fait hors navigateur, il a écrasé un relevé
  de 169 clés par un relevé partiel de 164, une fois les MP3 déjà générés et
  commités. Le fichier commité était bon, `git checkout --` a suffi ; mais rien
  n'avertit, et un générateur relancé ensuite aurait produit un module troué.
- **Le plus sûr est de ne pas lancer `build/collecte_sons.py` du tout.** Le
  relevé hors navigateur, vingt lignes de node sur `exos.js`, `carrier.js` et
  `plus.js`, rend exactement les mêmes clés — vérifié sur quatre modules. Il
  n'a ni port à réserver, ni processus à arrêter, ni envoi tardif à craindre :
  les deux incidents ci-dessus disparaissent avec lui. `module-n3-restaurant`
  a été produit ainsi, et son générateur audio le dit dans son en-tête pour
  que la question ne se rouvre pas.
- **Un `nohup … &` lancé dans une commande de fond meurt avec elle.** Le
  générateur d'images de `module-n3-restaurant`, lancé ainsi, a produit **une**
  image sur vingt-quatre : la commande qui l'avait lancé s'est terminée tout de
  suite et a emporté son enfant. Rien ne le dit — le journal du générateur
  s'arrête net, sans erreur, et le code de sortie est 0. Une commande longue se
  lance en **avant-plan** dans une tâche de fond de l'outil, sans `nohup` ni
  `&`.
- **`build/module.py` ne copie pas le dossier `icons/`.** Les quatre SVG d'un
  module — `play`, `speaker`, `mic`, `assistant` — sont un geste manuel de la
  chaîne, et leur absence **ne se voit pas à l'écran** : la page se rend
  normalement, les onglets s'affichent, aucune erreur de script n'est levée.
  Elle se voit uniquement dans le journal du serveur, en trois 404 — et chez
  l'élève, en puces vides à la place des icônes d'écoute. Découvert le 23 août
  2026 en produisant `module-n7-achat`. Juste après le premier
  `build/module.py`, recopier les quatre `*.svg` d'un module voisin dans
  `assets/interactive/<slug>/icons/`.
- **Le champ `theme` du manifeste échappe son apostrophe**, comme `bravo` et
  `relance` : le gabarit le place lui aussi dans une chaîne JavaScript à
  guillemets simples, et le build s'arrête tant que l'apostrophe n'est pas
  écrite `\\'`. Découvert le 21 août 2026 avec « Consultation d'un
  professionnel de la santé » — aucun thème n'en contenait avant.
- **`render()` du gabarit ne prend aucun argument** : il rend la section
  **courante**. Le relevé des sons par la console —
  `SECTIONS.forEach(s=>render(s.id))` — ne rend donc que la première section,
  et les pastilles à phrase porteuse des autres manquent au manifeste sans
  qu'aucune erreur ne le dise. Poser `curSec` avant chaque `render()`.
- **Tout bloc `ana` d'une mini-leçon veut son champ `say:`.** Sans lui, le
  bouton d'écoute ne se tait pas : le moteur concatène toutes les lignes de
  `mots`, balises HTML comprises, et l'extrait audio part lire « cent quarante
  mètres carrés huit places quinze minutes le 1er novembre 2023 ». Ça ne se
  voit qu'au relevé des sons, une fois les MP3 payés.

- **Un exercice `write` n'a qu'un seul trou par `item`, et rien ne le dit.**
  Le moteur crée **un** champ par item (`wi_<exo>_<i>`), mais `blankify()`
  rend tous les `___` de l'énoncé. Un item à deux trous — « ___ je (avoir)
  ___ déjà suivi ce cours » — s'affiche donc avec deux blancs et une seule
  case : l'élève ne peut pas répondre, et ni le build, ni `coherence.js`, ni
  le `node --check` ne le signalent. La correction est de couper en deux
  items (le marqueur d'un côté, le mode du verbe de l'autre), et le contrôle
  tient en une ligne : `grep -n "___.*___" build/contenu/<slug>/exos.js` doit
  ne rien rendre. Découvert le 23 août 2026 en produisant
  `module-n7-etablissement`, sur trois exercices du même moule.
- **Le contrôle des zones tient en dix lignes de console, et il vaut la
  peine.** Après avoir rendu les six sections (`SECTIONS.forEach(s=>{curSec=
  s.id; render();})`), parcourir `ZONES` et vérifier que `checkOk()` accepte
  le `cv` de chacune, puis remplir chaque `.winput` avec `it.accept[0]` et
  vérifier que `checkWrite()` rend `wfb ok`. Les zones sans `cv` sont
  exactement celles des exercices `write` — la liste sert donc de
  contre-vérification. C'est ce que recommande l'épisode de l'`imgmatch`
  mort : un exercice qui ne lève aucune erreur peut être mort.
  **Les deux signatures se lisent avant d'écrire le contrôle**, sans quoi il
  ment : `checkOk(zid, iid, lbl)` prend **trois** arguments — les zones `vf`
  et `lbl` se jugent sur le troisième, toutes les autres sur le deuxième — et
  `checkWrite(exId, i)` veut l'**indice de l'item**, pas seulement l'exercice.
  Un contrôle qui passe le `cv` en deuxième position pour tout le monde rend
  un refus par tuile Vrai/Faux du module — 79 sur `module-n8-oeuvres`, le
  23 août 2026, sur un module parfaitement sain. Un contrôle qui se trompe
  coûte plus cher que pas de contrôle du tout : on cherche une panne qui
  n'existe pas.
- **Un bloc `savoir` ne rend ses pastilles que s'il porte `speak:true`.** Le
  gabarit teste `ex.savoir.speak && r[2]` : une troisième colonne de rangée
  écrite sans ce champ produit des pastilles qui n'existent pas — rien ne
  s'affiche, rien ne s'entend, aucune erreur. Découvert le 21 août 2026 en
  produisant `module-n5-travail`, dont les quinze bandeaux ont été passés à
  `speak:true` d'un coup : le relevé des sons est passé de 206 à 233 clés.
- **Le relevé des sons hors navigateur charge `fccards.js` en premier.**
  `exos.js` appelle `FC_CARDS.map()` à l'évaluation ; dans l'autre ordre, node
  s'arrête sur « Cannot access FC_CARDS before initialization ». Et en
  CommonJS, `eval(src)` ne fait pas fuir les `const` hors de sa portée : il
  faut terminer la source évaluée par `; ({EXOS, PLUS, CARRIER_PHRASES})` et
  déstructurer le résultat. Trente lignes de node, et `build/collecte_sons.py`
  n'a plus à être lancé du tout.
- **`build/module.py` ne pose pas les icônes du module.** Le gabarit référence
  `icons/play.svg`, `speaker.svg` et `mic.svg` **dans le dossier du module**, et
  rien ne les y met : un module neuf sort avec trois 404 sur le bouton d'écoute
  des dialogues et sur l'onglet « Je découvre ». Ni le build, ni
  `coherence.js`, ni le `node --check` ne le signalent. La correction tient en
  une ligne — `cp assets/interactive/<voisin>/icons/*.svg
  assets/interactive/<slug>/icons/` — mais elle ne se voit qu'en **ouvrant le
  module dans un navigateur et en regardant l'onglet réseau**, pas seulement la
  console. Découvert le 23 août 2026 en produisant `module-n7-habitation`.
- **Une clé de `JEU_DE_ROLE_SCENARIOS` en double ne lève aucune erreur.**
  Découvert le 23 août 2026 en produisant `module-n7-oeuvres` : la clé
  `oeuvres` était déjà prise par `module-n5-oeuvres` (73), avec une constante
  `JEU_DE_ROLE_OEUVRES` du même nom. Deux clés identiques dans un littéral de
  dictionnaire Python ne provoquent **rien** — la dernière gagne, en silence,
  et la constante aussi. Le module neuf joue alors le scénario d'un autre
  niveau, avec des rôles qui ne sont pas les siens, et le jeu de rôle échoue
  chez l'élève sans que ni le build, ni `coherence.js`, ni le `node --check`
  ne regardent là. `CLAUDE.md` avertissait déjà qu'un `jr_scenario` **absent**
  n'est pas vérifié ; le cas de l'**homonyme** est pire, puisque la clé existe.
  Le contrôle en quatre lignes est dans `docs/deux-agents-en-parallele.md`,
  section « Un mot sur `server.py` » : charger `server.py`, lire le
  `jr_scenario` du manifeste, et vérifier que ses rôles sont bien ceux qu'on
  vient d'écrire.
- **Le dépôt n'a que deux voix féminines**, `enseignante` et `feminin_2` (plus
  `masculin_1` et `narrateur`). Un dialogue qui fait parler **trois femmes** est
  donc impossible : deux d'entre elles sonneraient pareil, et l'élève ne
  pourrait pas dire qui a dit quoi. Compter les personnages **par dialogue et
  par genre avant d'écrire les dialogues** : la correction après coup a coûté
  quatre fichiers de contenu et une quinzaine d'accords à
  `module-n7-habitation`, dont la médiatrice est devenue un médiateur.
- **Le manifeste de sons d'un générateur audio doit porter le slug de SON
  module.** Découvert le 23 août 2026 en produisant `module-n8-emmenagement` :
  `generer_audio_module_n8_recherche.py` lisait `sons_module_n7_recherche
  .json`, celui du module du **niveau 7**. Le fichier existe, donc rien ne
  lève d'erreur — le script aurait déposé les 221 sons du voisin dans
  `assets/interactive/module-n8-recherche/sons/` au lieu de ses 334, et neuf
  clés seulement se recoupent. Le module serait sorti muet aux trois quarts,
  avec des extraits d'un autre par-dessus. Même famille de faute que la clé de
  scénario homonyme : le nom se lit, donc rien n'avertit, et ni le build, ni
  `coherence.js`, ni le `node --check` ne regardent là. Le générateur d'un
  module neuf construit désormais son nom — `MANIFESTE = RACINE / ("sons_%s
  .json" % MODULE.replace('-', '_'))` — plutôt que de l'écrire à la main.
- **`checkOk` prend trois arguments, et le troisième décide des zones `vf`.**
  Sa signature est `checkOk(zid, iid, lbl)`, et pour `z.zcat === 'vf'` ou
  `'lbl'` elle compare `lbl` à `z.cv` ; pour tout le reste, `iid`. Le contrôle
  des zones que recommande l'épisode de l'`imgmatch` mort déclare donc
  **toutes les zones `vf` du module « refusées »** s'il est écrit avec deux
  arguments — on croit avoir trouvé un défaut grave, et on a mal appelé la
  fonction. Le contrôle correct :
  `(z.zcat==='vf'||z.zcat==='lbl') ? checkOk(k,null,z.cv) : checkOk(k,z.cv,null)`.
  Et les zones `write` n'ont pas de `cv` du tout : elles se vérifient à part,
  en remplissant chaque `.winput` avec son `accept[0]` puis en appelant
  `checkWrite`.
- **`git commit -- <dossier>` emporte tout ce que le dossier contient**, y
  compris ce qui vient d'y tomber pendant que le message se rédigeait. Le
  21 août 2026, un commit qui devait porter trois lignes de contenu a emporté
  309 MP3 et 20 images arrivés entre-temps dans `assets/interactive/<slug>/` :
  rien de perdu, mais un message qui ne dit pas ce qu'il contient. Quand des
  médias sont en cours de génération, nommer les fichiers plutôt que leur
  dossier — ou l'annoncer dans le message.

### Les contrôles avant de publier un module

Ils existaient déjà, dispersés dans ce fichier ; les voici ensemble, parce que
c'est ainsi qu'on s'en sert. Aucun n'écrit quoi que ce soit, et **chacun sort
en code 1 quand il trouve un écart** — de quoi les enchaîner dans un `&&`.
Quatre portent sur le module interactif :

    python3 build/sections.py --verifier           # data/sections.json ↔ les SECTIONS des modules
    python3 build/materiel.py --verifier           # data/materiel.json ↔ ce qui est sur le disque
    python3 build/couleurs_niveau.py --verifier    # l'en-tête porte la couleur de son niveau
    python3 build/couleurs_sections.py --verifier  # aucun vert dans les couleurs de section

Un septième porte sur la **cohérence interne** du module — ce qu'aucun des six
autres ne regarde, puisqu'ils le jugent de l'extérieur :

    node build/coherence.js <slug>     # un module
    node build/coherence.js --tous     # les vingt et un

Il lit `fccards.js`, `exos.js`, `carrier.js`, `plus.js` et `sections.js`, et
attrape les fautes qui ne lèvent aucune erreur : un exercice sans bonne réponse
enregistrée, une réponse qui désigne une image inexistante, un identifiant en
double, une section inconnue, un mot à pastille sans phrase porteuse, un bloc
`ana` ou une sortie de labo sans `say:`, une mini-leçon appelée mais absente,
une image manquante sur le disque. Ce sont précisément celles qui ne se voient
qu'à l'usage — ou une fois les MP3 payés.

Il lit comme le moteur, pas comme on croit que le moteur lit : `aid` toléré
pour un `imgmatch` de `module-consultation` et `module-probleme`, `speak:true`
exigé **seulement** quand des rangées portent une troisième colonne, et une clé
de `CARRIER_PHRASES` inutilisée n'est pas un écart. Écrit le 21 août 2026 après
que trois agents l'aient réécrit de zéro trois nuits de suite, aux activités
69, 80 et 81. Il se valide lui-même : lancé sur les vingt et un modules, il
retrouve sans rien savoir de leur histoire les **deux seuls** modules que ce
fichier signale comme encore fautifs — `module-n1-presenter` (« prénom »,
« épeler », « de rien ») et `module-n2-autobus` (« tout droit ») — et rien
d'autre, hors les images des modules en cours de production.

Deux autres portent sur les **séances** produites — les présentations et les
fiches — plutôt que sur le module interactif. Un module n'est publié qu'avec
elles, donc ils font partie du même passage :

    python3 build/controles/pieds_de_page.py        # le numéro inscrit dans les .pptx livrés
    python3 build/powerpoints/sommaire.py --verifier # le sommaire ↔ les séances existantes

Le second a une **étape d'écriture** que rien d'autre ne fait : ni
`build.py` ni `build_fiches.py` ne produisent
`assets/powerpoints/<slug>/presentations.html`. Tant que
`python3 build/powerpoints/sommaire.py <slug>` n'a pas été lancé, le contrôle
sort « lien diaporamas cassé » pour le module neuf — ce n'est pas un écart à
diagnostiquer, c'est une commande qui manque à la séquence. Vu le 21 août 2026
en produisant `module-n3-electro`.

Les deux premiers sont des **relevés** : ils déduisent du disque ce que le
portail affiche, et un écart veut dire qu'un module a été produit sans que le
relevé soit refait. Les deux suivants tiennent la règle des couleurs — un
module qui sort de la forge ou d'un vieux gabarit réintroduit du vert sans le
savoir, et c'est le seul endroit qui l'attrape.

Deux pièges de lecture :

- `couleurs_niveau.py` liste sous « hors registre, sans niveau » les modules
  qu'il laisse tels quels — `module-banque` aujourd'hui. Ce n'est **pas** un
  écart : c'est un module absent de `build/powerpoints/modules.py`, donc sans
  niveau à appliquer. Le signaler plutôt que le corriger est le comportement
  voulu.
- `sections.py --verifier` échoue tant qu'un module neuf n'a pas été inscrit au
  relevé. Pendant une production en cours, c'est normal et ça se résout en
  lançant `python3 build/sections.py` à la livraison — pas en modifiant
  `data/sections.json` à la main.

## Le tableau de bord du projet (`build/tableau_bord.py`)

L'état entier de la production sur une page, relu sur le disque :

    python3 build/tableau_bord.py           # → assets/presentations/tableau-de-bord.html
    python3 build/tableau_bord.py --texte    # le même état, en clair, sans rien écrire

Il ne remplace pas les trois relevés existants, il les réunit et ajoute ce
qu'aucun ne regardait : les modules sans séance en PowerPoint ou sans une seule
piste audio, les liens de `activities.json` qui pointent dans le vide, ce qui
n'est ni commité ni poussé. `chantier.py` reste la page des banques,
`bilan_programme.py` celle de la couverture, `couts_api.py` celle de la
facture — le tableau de bord les importe plutôt que de recompter.

- **Rien n'y est écrit à la main.** Modules du registre `powerpoints/
  modules.py`, séances des `.pptx` livrés, fiches des noms de
  `assets/documents/`, audio des `.mp3` du dossier du module, ateliers et
  savoirs du relevé de `chantier.py`, dépense de `journal_api`.
- **Un module est comparé au nombre de séances qu'il déclare**, jamais à seize
  en dur : les niveaux 1 et 2 en ont huit.
- **La dépense affichée est celle du poste.** Le registre qui compte vit sur le
  volume Railway (`GET /api/admin/appels`) ; la page le dit à l'écran plutôt
  que de laisser croire que la production ne coûte rien.
- **La liste des alertes vide est une bonne nouvelle**, et elle s'écrit comme
  telle — une page qui n'affiche rien se lit comme une page cassée.

## L'identité de marque francis

La plateforme s'appelle **francis** — descripteur « Aide à l'apprentissage du
français ». Le nom s'écrit **toujours en minuscules**, en Nunito 900, à
`-0.035em`. Le logotype tient en trois éléments sur une ligne :

```
franc[i]s  │  Aide à l'apprentissage du français
```

Le **seul** signe de marque est **le point du « i »** : un disque plein dessiné
en CSS. Aucune pastille, aucun monogramme, aucun fichier image — tout se
construit en markup et en CSS. Il est **statique** : aucun survol, aucune
animation.

Le nom se compose avec **« ı » (U+0131, i sans point)** — un « i » ordinaire
laisserait son propre point sous le disque — et le bloc du nom porte
`role="img"` + `aria-label="francis"`, pour que ni un lecteur d'écran ni la
recherche ne lisent « francıs ».

**Jamais de boîte, de contour ni de pilule autour du nom.** C'est la raison
d'être de cette identité : la marque précédente (SAAF, pilule à contour mauve)
se lisait comme un bouton. Remise du 26 août 2026,
`~/Downloads/design_handoff_francis`.

- `assets/design-system/marque-francis.css` — les jetons et les classes du
  verrouillage. Les jetons s'appellent `--marque-600` et `--marque-100`, **pas**
  `--violet-600` : le système de design emploie déjà ce dernier nom comme
  couleur de repérage. Deux noms, une seule valeur, pour que la marque ne
  dépende pas d'un jeton de repérage.
- `assets/design-system/marque-francis-favicon.svg` — le point seul, blanc sur
  cadre mauve ; `marque-francis-favicon-clair.svg` en donne la version mauve sur
  blanc. Jamais une lettre.
- `build/greffe_marque.py` — pose la barre de marque **au-dessus** de `#hdr`.
  Idempotente, comme les autres greffes :

```
python3 build/greffe_marque.py            # tous les modules écrits à la main
python3 build/greffe_marque.py meteo pub  # seulement ceux-là
python3 build/greffe_marque.py --retirer  # dégreffe tout
```

Les modules qui ont un manifeste dans `build/contenu/` sont sautés : leur
greffe est posée par `build/module.py` pendant la construction. Le script lit
le dossier plutôt que d'en tenir une liste, qui vieillirait.

**La barre de marque est la place normale du logotype.** C'est le verrouillage
A de la remise : le nom, le trait et le descripteur sur du blanc, fermés par un
filet mauve de 2 px, sur toute la largeur — et jamais dans le bandeau de la
page. Le blanc appartient à la plateforme, la teinte au module ou à la page.
C'est aussi le seul filet mauve de la page.

Deux scripts ont fait le chemin, gardés parce qu'ils le documentent :
`build/marque_francis_bascule.py` a basculé SAAF vers francis sur tout le dépôt
— HTML construit et sources qui le construisent — et `build/marque_barre.py` a
ensuite sorti le verrouillage des bandeaux teintés pour lui donner sa barre.
Tous deux idempotents.

**Les classes** : `.fr-lockup` (28 px, taille de barre) avec les tailles
`--grand` (36 px, en-tête de page ; redescend à 28 px sous 640 px), `--etroit`
(24 px), `--courriel` (nom seul), `--mauve` (fond mauve), `--sombre` (le trait
forci, pour les rares verrouillages posés hors d'une barre). `.fr-barre` est la
bande blanche à fermeture mauve ; `.fr-barre__in` sa colonne intérieure —
centrée sur `--content-max` pour le portail et les ateliers, ou
`--fr-barre__in--large` en pleine largeur pour les modules, dont l'en-tête n'a
que la gouttière pour marge. Sur les pages du portail, la session (nom, bouton
de déconnexion) vit dans la barre et non dans le bandeau de page.

**Sur fond mauve ou noir, le nom n'est jamais blanc pur** : le point doit se
détacher **des lettres**, pas seulement du fond. Nom blanc + point blanc, c'est
1.07:1 entre les deux, donc aucun signe visible. D'où le nom en `--marque-100`
sur mauve, en `#B4B4B4` sur noir.

**Le nom et le descripteur s'assoient sur la même ligne de base**
(`align-items: baseline`). « francis » n'a aucune descendante — le bas de ses
lettres EST sa ligne de base — tandis que le descripteur a un « A » capitale et
trois descendantes. Centrer les boîtes, ce que la remise écrit littéralement,
laissait le descripteur flotter 5 px sous le nom. Le trait, lui, n'a pas de
ligne de base : il se centre à part.

**Sous 480 px**, le trait et le descripteur disparaissent : le nom reste seul.
Le descripteur ne passe jamais sur deux lignes et ne se met jamais en
majuscules.

**À l'impression, aucune couleur** : nom et point en noir, trait `#C8C8C8`.

**Le mauve est réservé à la marque** : il ne va sur aucun bouton, aucun état,
aucune rétroaction. L'action reste le vert `--accent`, l'audio reste le rouge
`--audio`, et le bandeau d'en-tête reste clair — jamais noir.

Dans le portail, la marque ne passe pas par une greffe : ces pages sont écrites
à la main et ne se régénèrent pas. Chacune lie `marque-francis.css` et pose le
verrouillage **une fois**, dans son en-tête principal — jamais dans les
bandeaux de sous-vue, qui ne sont pas des en-têtes de page.

| Page | Verrouillage |
|---|---|
| `eleve.html` | grand sur l'écran de connexion — c'est le `h1`, dans la barre ; taille de barre sur l'accueil, avec la déconnexion |
| `enseignant.html`, `prof.html` | grand sur la connexion, taille de barre dans l'en-tête permanent |
| `progression.html`, `fiche-eleve.html`, `chiffres.html`, `reseau.html` | la barre ouvre la page, au-dessus de leur barre d'outils collante |
| `catalogue.html` | sa barre collante `.header` est la barre de marque : blanche, fermée en mauve |
| `presentations.html` | grand ; sa copie locale du logotype a été retirée au profit de la feuille partagée |

`lms.html` et `viewer.html` sont restés à l'écart : ils ne parlent pas le
système de design Francisation (Inter, accent bleu, chrome foncé pour le
lecteur). Y poser le logotype mettrait la marque sur une page qui la contredit ;
c'est une refonte, pas une greffe.

Le trait vaut `--paper-200` (#F0F0EE), la valeur de la remise : le verrouillage
vit sur du blanc. Les rares logotypes posés ailleurs — un pied de page, un
document sur fond de papier — prennent `.fr-lockup--sombre`, qui fonce le trait
juste assez pour qu'il se voie.

### Le violet n'est plus qu'à la marque

Le 20 août 2026, `#6B4FBB` a cessé d'être une couleur du système pour n'être
plus que celle du logotype. Il ne sert plus ni de repérage, ni de niveau, ni
d'état. Ce qu'il occupait a été redistribué :

| Ce qui était violet | Devient | Pourquoi |
|---|---|---|
| section graphie-phonie « Les sons » | **indigo** `#3B49A0` / `#E8EAFA` | déjà la teinte du niveau 7 ; les deux échelles se partagent leurs hues depuis toujours |
| niveau 8 de l'arc-en-ciel | **pourpre** `#7E3F98` / `#F3E8F7` | franchement plus magenta — distinct du logotype comme de la framboise du niveau 1 |
| en-tête du module 3 santé | **teal** `#0D7A6F` | voisins : 2 ambre, 4 forêt |
| en-tête du module 5 procédure | **acier** `#1D6B8F` | voisins : 4 forêt, 6 teal |
| en-tête du module 10 problème | **ambre** `#B45309` | voisins : 9 acier, 11 teal |
| en-tête du module 14 épicerie | **teal** `#0D7A6F` | voisins : 13 forêt, 15 acier |
| étiquette « privée » de `presentations.html` | **neutre** `--paper-200` / `--ink-500` | « privée » est un état, et le violet n'en porte aucun |

`--violet-600` et `--violet-100` **n'existent plus** dans
`assets/design-system/tokens/colors.css`. Le seul violet du dépôt est
`--marque-600` / `--marque-100`, dans `marque-francis.css`. Le changement a touché
les jetons, `.exo--phonie`, le paquet React, `theme.py` et les sept decks `a2`,
les contenus de `build/contenu/`, les modules écrits à la main, les pages
d'outils et le compositeur — puis la reconstruction des huit modules générés et
des 3 835 diapositives.

### La couleur d'un module est celle de son niveau

Le 20 août 2026, la règle ci-dessus a été remplacée. Choisir une couleur
d'en-tête parmi quatre, en évitant seulement le module voisin, entretenait deux
échelles pour une seule idée : un élève voyait une pastille ambre au catalogue
et un en-tête forêt en ouvrant le module. **La couleur d'un module est
désormais celle de son niveau, et rien d'autre ne la décide** — les jetons
`--niv-N-line` / `--niv-N-bg` de `colors.css` servent au catalogue, au portail
et à l'en-tête du module.

Le vert est sorti de l'échelle par la même occasion. Les quatre premiers
niveaux forment une montée chaude, les quatre derniers une descente froide :

| Niveau | Teinte | Filet / fond |
|---|---|---|
| 1 | framboise | `#A5335F` / `#FCE9F0` |
| 2 | brique | `#A83A22` / `#FBEAE4` |
| 3 | ambre | `#B45309` / `#FBEEDC` |
| 4 | or | `#8C6A07` / `#F7F0DA` |
| 5 | sarcelle | `#0D7A6F` / `#DCF2EF` |
| 6 | acier | `#1D6B8F` / `#E7F0F6` |
| 7 | indigo | `#3B49A0` / `#E8EAFA` |
| 8 | pourpre | `#7E3F98` / `#F3E8F7` |

L'olive du niveau 3 et la forêt du niveau 4 ont disparu ; l'ambre est descendu
du niveau 2 au niveau 3, et la brique a pris le niveau 2, encore vide de
modules à ce moment-là. L'indigo reste aussi au repérage de la graphie-phonie.

`build/couleurs_niveau.py` est ce qui tient la règle. Il lit les jetons dans
`colors.css` et le niveau dans `build/powerpoints/modules.py`, puis pose la
paire dans `build/contenu/<slug>/manifest.py` pour les modules générés, ou
directement dans le HTML pour les plus anciens, qui n'ont pas de dossier de
contenu. `--verifier` signale les écarts, y compris un module généré dont le
manifeste est juste mais qui n'a pas été reconstruit.

    python3 build/couleurs_niveau.py --verifier

Un module neuf n'a donc **aucune couleur à choisir** pour son en-tête : lui
donner son niveau dans le registre suffit.

Le vert a quitté les **couleurs de section** par la même décision. La palette
qui distingue les onglets d'un module — `sections.js`, répétée par `exos.js`
sur les exercices — portait la forêt `#166534` sur « Je retiens des mots » et
le teal-vert `#0F766E` sur « Je me lance ». Elles sont devenues framboise
`#A5335F` et pourpre `#7E3F98`. `build/couleurs_sections.py` applique et
vérifie la substitution, dans les contenus comme dans le HTML des modules
anciens :

    python3 build/couleurs_sections.py --verifier

Le seul vert qui reste est celui du **système de design** : `--accent`
`#0A8F5B` — boutons, pastilles, focus, et la rétroaction « correct ». Il n'a
jamais servi au repérage, et le retirer serait une refonte du système, pas une
retouche de module.

Un reste connu : `assets/interactive/a-lepicerie/` — une activité ancienne,
exportée par un bundler — porte encore un `#6B4FBB` dans un rectangle SVG
décoratif. Elle est hors du système de design ; la reprendre serait la
réécrire.

## Le glisser-déposer au doigt

Trois défauts mesurés le 24 août 2026 en émulation iPhone (390 px), sur
`module-achat`, corrigés ensemble par `python3 build/tactile_mobile.py`
(`--verifier` pour un état des lieux ; substitutions exactes, un fichier qui a
divergé est signalé et laissé tel quel). Le script traite le gabarit et les dix
modules écrits à la main ; les 77 générés reçoivent le correctif à la
reconstruction — donc `build/module.py --tous` après.

- **Un glisser qui part trop vite confisque le défilement.** Le seuil était de
  8 px, sans autre condition : sur un téléphone, où le banc de réponses occupe
  la bande du bas, tout doigt qui poussait l'écran depuis le banc créait un
  fantôme de glisser et le gestionnaire appelait `preventDefault()`. Plus moyen
  d'atteindre les réponses suivantes, et le moindre tremblement transformait
  une sélection en glisser avorté. Le glisser part maintenant sur un **appui
  maintenu** de 250 ms — la convention de l'iPhone — et le seuil est à 12 px.
  Une première tentative distinguait les gestes par leur **direction**
  (horizontal = défilement, vertical = glisser) : elle tombe sur un glisser
  diagonal, où un pixel d'écart entre `dx` et `dy` décide de tout. Vérifié en
  jouant les quatre gestes, pas en lisant le code.
- **Une réponse doit tenir dans le banc.** Les tuiles défilaient en file
  horizontale : bande visible de 245 px pour des tuiles allant jusqu'à 370 px,
  donc du texte coupé à droite. Elles reviennent à la ligne, dans un banc borné
  à 40 % de la hauteur de l'écran.
- **Les gouttières se réduisent sous 640 px.** 32 px de page plus 22 px de
  carte de chaque côté, c'était 108 px des 390 px d'un iPhone. Elles passent à
  16 px. Les valeurs sont écrites en dur dans les blocs de section depuis
  l'origine : le correctif les reprend dans une requête de média plutôt que de
  les refactoriser dans les quatre-vingt-sept modules.

## Les images d'un module

Elles se relisent **avec l'énoncé qu'elles illustrent**, jamais seules :

    python3 build/planche_images.py    # planche de contact numérotée, 1 268 images
    node build/contexte_images.js      # ce que chaque image est censée montrer

La planche (`planche-images.html`, non versionnée) met sous chaque vignette
l'exercice, la phrase de la rangée `ok` qui lui est associée, ou le mot de la
carte de vocabulaire. On y marque une image d'un clic et on dit pourquoi —
**texte · mains · décor · hors sujet**. Le relevé couvre les deux dossiers d'un
module : `images/` (exercices d'association) et `vocab/` (cartes de
vocabulaire), soit 501 et 767 fichiers au 22 août 2026.

Quatre règles pour tout prompt d'image, tirées de la relecture du 22 août 2026.
Le détail, les exemples et les deux situations pièges sont dans
`docs/vagues-suivantes.md`, section « Les images de cette vague » :

1. **Aucun texte dans l'image** — enseigne, étiquette, panneau, logo, slogan.
   Le modèle écrit du charabia et l'élève le lit.
2. **Pas de mains ni de visages en gros plan.**
3. **Le décor est québécois et nommé** — pas « appartement moderne ».
4. **L'image montre ce que dit son énoncé, pas le thème du module.** Le prompt
   s'écrit à partir de la phrase de la rangée `ok`. C'est le défaut le plus
   fréquent, et le seul qui ne se voit pas sans mettre les deux côte à côte.

**La parade aux deux premières règles n'est pas de les répéter, c'est de
cadrer.** Vérifié le 23 août 2026 sur les quatre modules de la vague 7 : sept
images refaites sur cinquante, et jamais parce que le prompt avait oublié
d'interdire. Devant un objet qui *porte* une inscription — répondeur, réveil,
calendrier, babillard, étiquette de prix, écran de guichet — « aucun texte
lisible » ne tient pas : le modèle écrit le mot quand même, en charabia
(`1:520`) ou en anglais (« March », « PLAY / STOP »). Ce qui marche est de
mettre l'inscription **hors champ** : la face avant du répondeur tournée en
trois quarts arrière, l'afficheur du réveil hors cadre et seule sa lueur rouge
sur le bois, l'en-tête du calendrier coupé et seule la grille de cases. Même
mécanique pour les mains : **imposer le poste de l'appareil** (le clavier seul
sur la table, la feuille déjà signée et le stylo couché à côté) réussit du
premier coup là où « pas de mains » échoue. Une négation décrit ce qu'on ne
veut pas ; un cadrage décrit ce qu'on veut, et c'est la seule des deux qu'un
modèle d'image sait exécuter.

**Quand le texte *est* le sujet, il se compose en HTML, jamais dans l'image.**
Une publicité, une affiche, un formulaire : le gabarit sait afficher un
bandeau, un encadré, un texte suivi (type `texte`). L'image montre alors la
scène autour — l'abribus vu de loin, l'écran éteint, la personne qui regarde.

**Un objet qui porte son texte sur plusieurs faces ne se tourne pas : il se
retire du cadre.** Le cadrage suffit devant un répondeur ou un calendrier, qui
n'ont qu'une face écrite. Une console de mixage, un tableau de bord, un
appareil de studio en portent sur le dessus, le flanc et l'arrière : « vue de
trois quarts arrière et éteinte » ne les sauve pas, et le modèle y écrit une
**marque réelle** en toutes lettres. Découvert le 23 août 2026 en produisant
`module-n8-actualite`, dont le studio de radio est sorti avec un nom de
fabricant sur la console. Le prompt refait dit « aucun appareil électronique
n'entre dans le champ, seulement des câbles qui sortent par le bord droit » ;
l'image est juste du premier coup, et le micro sur bras suffit à dire le lieu.

**Une skill s'invoque par son nom, elle ne se cherche pas sur le disque.** Un
`find /` lancé pour retrouver un `SKILL.md` a fait ouvrir à macOS trois
demandes d'autorisation — calendrier, photothèque, « données d'autres apps » —
pour un fichier qui vit à `~/.claude/skills/<nom>/SKILL.md`.

## Le cadre programme d'un module (`build/cadre.py`)

Avant d'écrire une ligne d'un module, on en sort la spécification
ministérielle :

```
python3 build/cadre.py 4                      # les situations du niveau
python3 build/cadre.py 4 "Relations sociales" # le cadre d'une situation
python3 build/cadre.py 4 sante --savoirs      # + les points de savoir
```

Il lit `~/Claude/programme/programme-francisation.json` — **600 Ko** — et en
rend **une page** (~12 Ko) : la situation, son domaine, ses intentions de
communication rangées par compétence, son lexique, l'index des savoirs du
cours, les attentes et les critères. Éprouvé sur les huit niveaux. Ne jamais
charger le JSON entier pour cadrer un module : c'est cher, et ça invite à
reconstituer de mémoire ce qu'on aurait dû lire.

Trois défauts de la source, traités par le script plutôt que tus :

- **Le lexique vient d'un autre document** que le programme — la « Progression
  du lexique » du CSS de Laval, juin 2020 — et nomme parfois les situations
  autrement (« Consultation médicale » pour « Consultation d'un professionnel
  de la santé »). D'où `ALIAS_LEXIQUE`, explicite et commenté.
- **Une entrée de lexique sans situation continue la précédente** : les
  trente-deux expressions « avoir mal » suivent « Consultation médicale ». Le
  script reporte la situation et marque l'entrée « (rattachée) ». Sans cette
  règle, *Relations sociales* rendrait 7 entrées au lieu de 28.
- **Trois entrées du niveau 4 sont de la bouillie d'extraction** : des consignes
  de grammaire classées en vocabulaire. Elles sont écartées et **comptées dans
  un avertissement**, jamais supprimées en silence.

Huit des dix-sept situations du niveau 4 n'ont **aucun lexique** — le document
de Laval ne les couvre pas. Le script le dit au lieu d'afficher une liste vide :
le vocabulaire se compose alors à partir des intentions.

**Le programme donne la spécification, jamais le contenu.** Scénario,
personnages, dialogues et exercices s'inventent — voir la règle du contenu
inventé plutôt que copié.

## Les ateliers générés

Aucun de ces ateliers ne s'écrit à la main. Leur HTML sort d'un script, et
**l'éditer serait perdu au passage suivant** — même règle que les modules.

| Atelier | Script | Contenu |
|---|---|---|
| `vocab-flash-sante`, `vocab-flash-conso` | `build/vocab_flash.py` | `assets/interactive/<slug>/mots.json` |
| `polices-n1` — activité 124 | `build/polices.py` | `assets/interactive/polices-n1/mots.json` |
| **les banques des huit niveaux** — activités 124 à 211 | `build/banque.py` (qui appelle les générateurs de familles) | `assets/interactive/<slug>/contenu.json` |

## Les banques des huit niveaux (activités 124 à 211)

Soixante-trois ateliers, **six générateurs**, un contrat de contenu. Les plans
sont dans `docs/plan-exercices-niveau-1.md` (la banque d'origine) et
`docs/plan-banques-niveaux-2-8.md` (les sept autres), le format dans
`docs/schemas-banque-n1.md`, et l'état réel se lit d'une commande :

```
python3 build/banque.py --etat            # où en sont les huit banques
python3 build/banque.py --etat --niveau 5 # un seul niveau
python3 build/banque.py --verifier        # code 1 sur écart, s'enchaîne avec les autres
python3 build/banque.py                   # reconstruit tout
python3 build/inscrire_ateliers.py        # inscrit au catalogue ce qui est jouable
```

**Un atelier se déclare lui-même.** Le registre n'est pas une liste écrite à la
main : c'est le balayage de `assets/interactive/*/contenu.json`, et la clé
`generateur` est l'opt-in. Ajouter un atelier, c'est déposer un fichier de
contenu portant `niveau`, `generateur` et `activite` ; rien à inscrire
ailleurs. `build/banque_n1.py` reste comme renvoi vers `banque.py --niveau 1`.

**Pourquoi une banque plutôt que des modules.** Le niveau 1 n'a que quatre
situations au programme et les quatre ont leur module (56, 96, 97, 98). Un
cinquième cours referait ce qui existe. La place restante est dans les
**savoirs** que les modules ne peuvent pas drainer — douze des trente-deux
sont phonétiques ou graphiques. Un module de huit séances est le bon prix pour
une situation, le mauvais pour faire distinguer `a`, `i` et `ou`.

**Quatre familles, quatre formes.** Une famille = une forme d'exercice = un
générateur. Ajouter un atelier, c'est écrire un `contenu.json`, pas du code.

| Famille | Générateur | Forme | Où elle sert |
|---|---|---|---|
| A · apparier | `build/appariement.py` | une chose, plusieurs représentations | tous les niveaux — graphie au 1, abréviations au 3, registres au 5, familles de mots au 6 |
| B · écouter | `build/oreille.py` | un extrait, on tranche | niveaux 1 à 3 seulement : au-dessus du 4, le programme n'a plus qu'un ou deux savoirs phonétiques |
| C · construire | `build/phrase.py` | des morceaux à mettre en place | tous les niveaux ; la limite de tuiles suit le niveau (7 au débutant, 12 au 5 et plus) |
| D · écrire | `build/graphie.py` | on recopie, caractère par caractère | niveau 1 |
| E · lire un texte | `build/texte.py` | un texte sous les yeux, des questions qui y ramènent | niveaux 2 à 8 ; modes `questions` et `trous` |
| F · conjuguer | `build/conjugaison.py` | une phrase, un infinitif, un temps | niveaux 2 à 8 ; mode `choisir` au 2, `ecrire` à partir du 3 |

**Le profil des savoirs bascule avec le niveau**, et c'est ce qui décide des
familles à employer : la phonétique passe de quatre savoirs au niveau 1 à un
seul aux niveaux 7 et 8, pendant que le lexique triple et que la catégorie
« texte » quintuple. Une banque de niveau 7 bâtie sur le modèle du niveau 1
travaillerait des savoirs qui n'y sont plus.

`polices-n1` (124) garde `build/polices.py` : ses faces sont **calculées** par
la casse et la police, alors que celles de la famille A sont **données**. La
fusion se fera le jour où l'on pourra comparer l'ancien et le neuf octet pour
octet — pas avant, c'est une activité livrée et vérifiée.

**Deux exercices du plan sont retombés dans des formes existantes**, et c'est
une meilleure nouvelle qu'un générateur de plus : les lettres majuscule /
minuscule sont trois registres d'une même lettre, donc de l'appariement ; les
syllabes sont des morceaux à remettre en ordre, donc de la phrase.

### Ce qui n'entre pas au catalogue, et pourquoi

Un atelier de la famille B sans ses MP3 n'est pas « muet », il est
**injouable** : l'extrait *est* la question. Or le portail élève range ces
ateliers dans le banc des exercices libres, **toujours ouvert, sans date** —
les y inscrire les offrirait cassés, sans issue. Les six restent donc hors de
`data/activities.json` jusqu'à ce que `build/oreille.py --audio` les déclare
prêts. `banque_n1.py` sort en écart si l'on oublie la règle dans un sens ou
dans l'autre.

### Le banc des exercices libres : un filtre, trois copies

`eleve.html` range un atelier selon `domaineDeVie` testé contre une expression
régulière. Ce qui passe atterrit dans « Pour vous exercer seul » — sans date,
sans état, toujours ouvert. La banque emploie deux domaines : **« Graphie et
sons »** (familles A, B, D) et **« Grammaire transversale »** (famille C, qui
existait déjà).

**La même expression est écrite en trois endroits** — `eleve.html`
(`DOMAINES_LIBRES`), `catalogue.html` et `js/enseignant.js` (`DOMAINES_OUTILS`).
Elles ont été mises d'accord dans le même commit le 24 août 2026, mais trois
copies d'une règle est le défaut « deux sources pour une idée » que ce dépôt
connaît déjà. Les unifier est une refonte transversale : à faire quand
personne d'autre n'écrit, pas au passage.

### Les savoirs sont dans les mots-clés

Chaque activité de la banque porte ses identifiants de savoir
(`n1-s22`, `n1-s32`…) dans ses `keywords`. La recherche du catalogue les indexe
déjà : **chercher « n1-s22 » rend les ateliers qui travaillent ce savoir.**
C'est le routeur prévu au plan — « cet élève n'entend pas *a* de *ou*, je lui
donne quoi ? » — obtenu sans toucher au diagnostic.

Couverture au 24 août 2026 : **31 savoirs sur 32**. Le seul dehors est
`n1-s01`, les conventions de la communication — saluer, remercier, se
reprendre. Ça se travaille en situation, dans un module ; l'isoler dans un
exercice le viderait.

### Quatre pièges déjà payés

- **La rétroaction effacée par le rendu.** Dans `phrase.py`, `verifier()`
  posait le retour puis appelait `rendreJeu()`, qui commençait par l'effacer.
  L'élève n'aurait jamais su si sa phrase était juste, ni en vert ni en rouge.
  Ni le build, ni la console ne le signalaient — c'est le contrôle automatisé
  des douze items dans le navigateur qui l'a rendu visible. Le nettoyage
  appartient au début d'un tour, pas à chaque rendu.
- **Un contrôle qui a tort coûte plus cher que pas de contrôle.** Le build
  refusait « J'ai un stylo et un livre » parce que la phrase porte deux tuiles
  « un ». C'était la méthode qui était fausse : la justesse se juge sur les
  **mots composés**, jamais sur l'ordre des tuiles.
- **Un exemple faux dans un contrat de format enseigne une erreur.**
  `docs/schemas-banque-n1.md` donnait « m'app\[e\]ll\[e\] » comme e muet. Le e
  du milieu d'*appelle* se prononce \[ɛ\], et le programme le transcrit
  lui-même. Corrigé, avec la règle en deux temps.
- **Un pictogramme qui se lit comme une lettre.** La chaise de profil dessinée
  au trait donne successivement un « A » puis un « h ». Dans un niveau qui
  apprend l'alphabet, c'est le contresens à ne pas livrer : ce sont donc des
  silhouettes. Les pictogrammes se relisent sur une planche de contact, jamais
  un par un.

### Les médias

Tout est **dessiné ou composé, rien n'est généré** : horloges à aiguilles,
pastilles à compter, vingt et un pictogrammes, quatre écritures typographiques.
Coût média de la banque : zéro. C'est la règle des images du dépôt appliquée à
la lettre — un modèle écrit du charabia dès qu'un panneau porte une
inscription, et un pictogramme est de la géométrie, pas une photo.

L'audio, lui, est **préparé et non produit** :

```
python3 generer_audio_banque_n1.py --compter   # 262 extraits, ~0,76 $, sans rien payer
```

Le compte ElevenLabs était à zéro crédit (401 `quota_exceeded`) le 24 août
2026. Les boutons d'écoute restent en place et sans effet — on ne masque
jamais un bouton pour cacher un média manquant.


**« Même mot, autre police » (activité 124, niveau 1)**, ajouté le 24 août
2026. Le niveau 1 n'a que quatre situations au programme et les quatre ont
déjà leur module : la place restante n'est pas dans un cinquième cours, elle
est dans les savoirs que les modules ne peuvent pas drainer. Celui-ci est
`n1-s32`, Éléments de graphie — « comprendre des mots écrits en caractères
d'imprimerie différents ». L'atelier montre les quinze mots des quatre
modules du niveau dans six écritures, chacune nommée par l'endroit où l'élève
la rencontre : mon cahier, un livre, le panneau, le formulaire, la main, les
lettres détachées. **C'est le nom du lieu qui fait la leçon** ; sans lui, ce
serait une vitrine de polices.

Trois choses à savoir avant d'y toucher :

- **Cinq polices d'emprunt, importées par cette activité seule.** Le système
  de design garde Nunito et ne bougera pas : `tokens/fonts.css` est intouché.
  Hors ligne, les cinq tombent sur leurs replis système — les six écritures
  restent distinctes, l'exercice reste juste, elles sont moins typées. Écart
  accepté, pas défaut à corriger en embarquant des fichiers de police.
- **Les pièges de « Je trouve le même mot » sont écrits à la main** dans
  `mots.json`, deux par mot. Ce sont les confusions réelles du niveau —
  *nom* / *non* / *nombre*, *prénom* / *pronom*, *accueil* et sa graphie
  fautive *acceuil*, *code postal* / *carte postale*. Des leurres tirés au
  hasard rendraient l'exercice trivial.
- **La bonne réponse se marque au montage, jamais par son texte.**
  `data-bonne` existe parce qu'un test par `startsWith` allumait deux boutons
  en vert quand la cible était *nom* et le leurre *nombre*.
- **`ajuster()` mesure, les classes CSS ne suffisent pas.** Le corps de chaque
  mot est réduit jusqu'à ce qu'il tienne dans sa case, et `overflow-wrap` est
  à `normal` partout : sans ça, « TOILETTES » sortait coupé en TOILETT / ES
  sur le formulaire. Une classe posée sur la longueur en caractères ne peut
  pas savoir qu'un Courier espacé déborde là où un Nunito respire — et hors
  ligne, les polices de repli n'ont pas les mêmes chasses. La mesure est
  refaite à `document.fonts.ready`, au redimensionnement et à l'entrée en
  mode présentation.

L'audio des quinze mots (`audio/<slug>.mp3`, voix enseignante ralentie) reste
**à produire** : `generer_audio_polices_n1.py` est écrit et relançable, mais
le compte ElevenLabs était à zéro crédit le 24 août 2026. Les boutons
d'écoute restent en place et sans effet — on ne masque pas un bouton pour
cacher un média manquant.

## Cours et ateliers

Chaque activité porte une `categorie` : `cours` (modules de 4 h, le matin) ou
`atelier` (activités de 2 h, l'après-midi). Les listes enseignantes
(`catalogue.html`, `enseignant.html`) sont rendues en deux sections dans cet ordre.
Le champ se choisit à la création et dans le modal de modification ; pour une
activité qui ne l'aurait pas, `normalize_categorie()` le déduit du chemin
(`assets/interactive/module-*` → `cours`). Il figure dans `USER_FIELDS`, donc le
choix de l'enseignant survit aux redéploiements.
- Authentification enseignante : courriel + mot de passe (PBKDF2-SHA256), jeton
  de session envoyé dans l'en-tête `X-Prof-Token`. `prof.html` porte la
  connexion, l'installation initiale et **les comptes du personnel
  enseignant, rien d'autre** : ouvrir un compte, le retirer, réinitialiser un
  mot de passe, changer le sien. Les groupes en sont partis — ils vivent dans
  l'onglet « Groupes et comptes » du portail, qui les crée, les renomme et
  les supprime ; garder les deux menait à deux endroits pour un même geste.
  La liste montre **tous** les comptes, administrateurs en tête, et chaque
  ligne porte son rôle en toutes lettres.
  `js/prof.js` fournit `Prof.fetch` / `Prof.withGroup` / `Prof.body` aux trois
  pages enseignantes (`catalogue.html`, `lms.html`, `fiche-eleve.html`,
  `progression.html`) — toute requête
  d'administration doit passer par là, sinon elle répond 401.
- Rôles : `admin` (crée les autres enseignants, voit tous les groupes) et `prof`.
- **Le compte fondateur** est le seul à pouvoir ouvrir un compte
  `admin`. Un administrateur ordinaire ouvre des comptes `prof`, réinitialise
  leur mot de passe, gère les groupes — il ne fabrique pas ses pairs. Le
  fondateur est le compte du premier démarrage : `founder_id()` prend le plus
  petit `id` présent (les deux chemins d'amorce, `/api/prof/setup` et les
  variables `PROF_*`, lui donnent l'`id` 1), et la variable d'environnement
  `PROF_FONDATEUR` (un courriel) permet d'en désigner un autre sans toucher au
  code. Trois refus en 403, tous côté serveur : ouvrir un `admin`, changer le
  rôle d'un compte, et **toucher au compte fondateur** — sans ce dernier, un
  administrateur s'en emparerait en lui réinitialisant son mot de passe et la
  règle ne tiendrait plus. Le fondateur ne peut pas non plus être supprimé.
  `public_teacher()` porte le drapeau `fondateur` : `prof.html` s'en sert pour
  ne pas offrir un geste que le serveur refusera (le sélecteur de rôle
  n'apparaît qu'au fondateur, et la ligne du fondateur n'offre aucun geste
  aux autres).
- **Premier démarrage** : s'il n'existe aucun compte, `/prof.html` affiche
  l'écran d'installation qui crée le premier administrateur. On peut aussi
  semer ce compte par les variables `PROF_COURRIEL` / `PROF_MOTDEPASSE` /
  `PROF_NOM`. Dès qu'un compte existe, `/api/prof/setup` répond 409.
- `migrate_multi_groupes()` tourne au démarrage après `init_storage()` : elle
  crée le groupe historique, y reprend les dates des activités et y rattache
  les élèves existants. Idempotente.
- Healthcheck Railway : `/api/health` (et non plus `/api/activities`, désormais
  protégé par le jeton enseignant).

## Structure

- `data/activities.json` — métadonnées des activités (source de vérité côté code)
- `data/teachers.json` / `data/groups.json` / `data/schedule.json` — comptes,
  groupes, planification. Les deux premiers ne sont pas versionnés.
- `data/sections.json` — le découpage des modules en sections, **produit**
  par `python3 build/sections.py`. Versionné : il décrit le code livré.
- `assets/documents/` — fiches élèves (HTML imprimables)
- `assets/interactive/<slug>/` — activités interactives (HTML autonomes)
- `assets/plans/` — plans de cours
- `data/documents.json` — fichiers partagés à un groupe (non versionné),
  déposés dans `assets/documents-groupe/<groupId>/`
- `enseignant.html` + `js/enseignant.js` — portail enseignant (Planifier ·
  Élèves · Groupes et comptes)
- `progression.html` — tableau de bord du groupe, module par module
- `fiche-eleve.html` — le dossier d'un seul élève
- `prof.html` — installation du premier compte, connexion, comptes enseignants
- `catalogue.html` / `eleve.html` — catalogue (téléversement) / interface élève
  (l'ancien nom `admin.html` ne sert plus que de redirection vers
  `catalogue.html`, pour les signets pris avant le renommage)

## Catalogue (`catalogue.html`)

Le fonds, pas la planification : **toutes les activités, tous niveaux
confondus**, et le matériel qui va avec. On y fait deux choses, pas une de
plus — ajouter une activité, ajouter du matériel à une activité.

- **Aucune date.** Planifier appartient au portail enseignant, qui travaille
  par groupe. Le catalogue appelle donc `GET /api/activities?catalogue=1`,
  qui rend le fonds sans superposer les dates d'un groupe. Sans ce drapeau,
  la route se comporte exactement comme avant (`?groupId=` obligatoire) :
  rien ne change pour `lms.html` ni le portail élève.
- **Rien ne disparaît, rien ne se remplace.** Pas de suppression d'activité,
  pas de suppression de fichier, pas de renommage, pas de changement de type.
  Un emplacement déjà rempli s'affiche avec son fichier en lien et n'offre
  pas de zone de dépôt ; seuls les emplacements vides en ont une. Les routes
  `DELETE /api/activities/<id>`, `/clear-file` et `/rename` existent toujours
  côté serveur, mais plus aucune page ne les appelle.
- **Sept emplacements, une seule liste** : la constante `MATERIEL` de la page
  décide à la fois du formulaire d'ajout, de la ligne du catalogue et de la
  fenêtre d'ajout. Sa `cle` est le nom du champ côté serveur *et* la clé dans
  `activities.json` — présentation (`slideshow`), fiche élève (`studentDoc`),
  **corrigé (`corrige`)**, plan de cours, activité interactive, autres,
  miniature. Le corrigé est rangé dans `assets/corriges/<slug><ext>`.
- **Le niveau se choisit au dépôt** et se lit sur chaque ligne, avec son
  propre filtre. Le champ est `level`, dans la forme « Niveau N » déjà
  écrite partout ailleurs (`js/enseignant.js`, `js/materiel.js`) — on ne change
  pas de forme en chemin. `normalize_level()` accepte les huit niveaux du
  programme et retombe sur *Niveau 4* pour toute autre valeur, y compris
  l'absence : les 43 activités écrites avant ce champ sont de ce cours-là.
  Le niveau ne se modifie pas après coup, comme le reste : on ajoute.
- **Le matériel présent est un lien** : le catalogue sert d'abord à
  retrouver un fichier. Ce qui manque reste écrit en gris, pour qu'on voie
  le trou.
- **Un dépôt fait en ligne survit au redéploiement.** La fusion du volume
  (`init_storage`) laisse désormais le volume gagner sur les champs de
  fichier **quand le code n'en porte aucun** (`FICHIER_FIELDS`). Le code
  garde l'autorité s'il a lui-même un fichier — une fiche régénérée par git
  doit repartir. Sans cette nuance, un corrigé ajouté en production
  disparaissait au déploiement suivant.
- **Le bandeau ne porte que le retour vers l'espace enseignant** : c'est de
  là qu'on vient, et c'est la seule sortie. Pas de sélecteur de groupe (la
  page n'en dépend plus), donc plus de `Prof.renderBar` ici.
  - La page du catalogue s'intitule **« Catalogue »** et suit le système de
    design (aucune couleur en dur). Son en-tête ramène à l'espace enseignant,
    en face du bouton « Catalogue » du portail. La barre de groupe vient
    encore de `js/prof.js`, qui injecte ses bleus : elle est rhabillée sur
    place par `#profBar …`, sans toucher `prof.js` que partagent les autres
    pages enseignantes.

## Portail enseignant (`enseignant.html`)

- Refait selon la remise `~/Downloads/design_handoff_portail_enseignant`, qui
  est la **source de vérité visuelle** de cette page. Trois onglets dans une
  seule page : Planifier · Élèves · Groupes et comptes, plus son propre écran
  de connexion. Il **remplace l'usage courant** de `lms.html` et il est
  désormais le **seul** endroit où l'on crée un groupe : `Prof.init()` y
  envoie l'enseignant qui n'en a aucun. `catalogue.html` reste la page du catalogue
  (téléversement et modification d'activités), que la remise ne couvre pas.
- La page ne passe **pas** par `js/prof.js` : celui-ci renvoie vers
  `prof.html` sur un 401, alors que le portail porte sa propre connexion. Elle
  partage la session par les deux mêmes clés de `localStorage`
  (`prof_token`, `prof_groupe_actif`), donc basculer entre les pages ne
  redemande jamais le mot de passe.
- **Aucune couleur en dur** : uniquement des jetons du système de design. La
  pastille d'état porte toujours couleur **et** glyphe **et** mot (`— ✕ ✓ →`).
  Un seul bloc foncé par page, et jamais l'en-tête : ici, la barre de titre de
  l'aperçu élève.
- Les détails d'un module (savoirs, actes de parole, compétences CO/PO/CE/PE,
  vocabulaire) ne sont pas dans `activities.json` — ils décrivent le contenu
  pédagogique, pas le fichier. Ils vivent dans la constante `DETAILS` de
  `js/enseignant.js`, une entrée par module de cours.
- **Le chevron déplie les sections du module**, cochables et datables une à
  une (« Je découvre · Défi 1 · … · Je retiens des mots »). Les sous-sections
  nommées dans la remise (Vocabulaire · Compréhension orale · Graphie-phonie ·
  Écriture · Écoute et réponds) restent, elles, sans équivalent dans les
  modules : ce sont les vraies sections du module qui sont offertes, celles
  que `data/sections.json` relève.
- Une ligne de planification est donc soit un module (`35`), soit une de ses
  sections (`35:t1`) : `etat.selection` porte des **clés de chaîne**, et le
  rythme de dates court sur la liste ainsi ordonnée (le module, puis ses
  sections). « Cocher les N lignes » ne coche que les modules — cocher d'un
  coup les sections de vingt activités poserait une planification que personne
  n'a demandée.
- **L'écran « Élèves » inscrit et génère les codes.** Un élève ne s'inscrit
  jamais lui-même : l'enseignante l'ajoute au groupe actif et le serveur
  fabrique son code à six caractères (`POST /api/admin/students`, qui renvoie
  les élèves créés avec leur code). Sans nom, le code est anonyme (« Élève
  N ») — on en prépare d'avance et on les nomme à l'arrivée
  (`PATCH /api/admin/students/<id>` avec `label`). C'est ce que portait
  l'ancienne page `lms.html` ; le portail le reprend, avec « Copier le
  code », « Renommer », « Retirer » et l'impression des billets.
- **Un nom ne vaut que pour un élève** : le formulaire refuse « nom + N
  codes », sinon le serveur donnerait le même nom aux N créés. Le nombre est
  plafonné à 30 des deux côtés.
- **Retirer un élève retire son code** — la confirmation le dit en toutes
  lettres, parce que la personne perd l'accès à son portail.
- Les billets de codes s'impriment dans le cadre isolé `#matImpression`, le
  même que les fiches du dépôt, en **noir et blanc** : un billet par élève,
  avec le groupe, le nom, le code et l'adresse du portail.
- **Planifier des sections d'un module sans date ouvre le module** à la
  première d'entre elles (`modulesAOuvrir()`). Sans cela, la classe ne verrait
  rien : un module fermé cache toutes ses sections, datées ou non.

### Compositeur d'activité

Le bouton « Composer une activité » de la barre de groupe ouvre
`assets/outils/compositeur-activite.html` dans un nouvel onglet — la
planification en cours n'est pas perdue. La page est autonome : ni session, ni
groupe, ni appel au serveur ; elle assemble un prompt à partir du programme.

- **Le fichier du dépôt est une copie**, pas la source. La source vit hors du
  dépôt (`~/Claude/compositeur-activite.html`) et la greffe du programme
  produit `~/Claude/compositeur-activite-complet.html`. Après toute
  modification, regreffer **puis** recopier :

  ```
  python3 ~/Claude/programme/outils/greffe_programme.py ~/Claude/compositeur-activite.html
  cp ~/Claude/compositeur-activite-complet.html assets/outils/compositeur-activite.html
  ```

  Modifier la copie du dépôt ne sert à rien : la prochaine greffe l'écrase.
- Elle est servie comme les autres assets : `/assets/` cherche d'abord le
  volume, puis retombe sur `BASE_DIR`. Rien à ajouter à `init_storage()`.

#### Forge (génération réelle, poste local seulement)

Le bouton « Générer l'activité » fait exécuter la commande au lieu de la
copier : `forge.py` passe le prompt au **CLI Claude Code** installé sur le
poste, qui travaille dans `~/Claude/activites/commandes/<id>/` et y dépose
l'activité. Le CLI est authentifié par l'abonnement Claude — pas de clé
d'API, pas de facturation au jeton, et surtout des **outils** : il lit le
système de design et écrit de vrais fichiers, là où un appel d'API ne rendrait
que du texte.

- **Les images passent par la compétence `/generate`, jamais autrement.** Le
  préambule de `forge.py` l'impose et `~/Claude/generations` est ouvert au CLI
  par un second `--add-dir` : sans lui, l'agent ne peut ni y déposer l'image, ni
  écrire le journal `.json`, ni régénérer le mur. L'image est ensuite recopiée
  dans `images/` du dossier de commande et référencée en lien relatif — la
  publication conserve l'arborescence, la page la retrouve donc telle quelle.
  Interdits explicites : banque d'images en ligne, URL distante, émoji ou SVG
  bricolé en remplacement d'une illustration demandée. La vidéo, elle, est
  payante : le préambule interdit à l'agent d’en lancer une seule.
- **La fiche élève est un PDF format lettre, pas un markdown.** Le CLI écrit
  `fiche-eleve.html` (mise en page d'impression) puis appelle
  `~/Claude/programme/outils/fiche_pdf.py`, qui rend le PDF par Chrome sans
  interface — le seul moteur d'impression du poste, déjà utilisé par
  `captures.py`. Le format ne se règle **pas** en ligne de commande : Chrome
  imprime ce que dit `@page { size: letter }`, et le script relit le
  `/MediaBox` du PDF pour refuser tout ce qui ne fait pas 612 × 792 pt. Sans
  cette relecture, une page A4 filerait jusqu'à l'imprimante de l'école. Les
  deux fichiers sont gardés : le HTML est la mise en page, le PDF le livrable.
  `ROLES` reconnaît encore `activite.md` pour les commandes d'avant ce
  changement, et `ROLES_PRIORITE` fait gagner le PDF quand les deux existent —
  l'ordre alphabétique donnait sinon la fiche au markdown.
- **La mise en page des imprimés ne s'invente plus : elle se recopie.** Les dix
  documents `assets/documents/module-*-fiches-eleves.html` portaient la même
  feuille de style, identique octet pour octet, mais elle n'existait comme
  fichier nulle part ; la forge, elle, n'était renvoyée au système de design que
  « pour une page interactive » et réécrivait donc un habillage neuf à chaque
  commande — Helvetica contre Nunito, classes inventées, en-tête différent. La
  feuille est extraite en `assets/design-system/fiche-imprimee.css` et le
  préambule impose d'en **recopier le contenu** dans le `<style>` des trois
  imprimés. Recopier plutôt que lier : la fiche naît dans le dossier de la
  commande puis déménage vers `assets/interactive/`, où un `<link>` relatif
  casserait, et le HTML doit rester ouvrable par double-clic. Le prix de ce
  choix est connu : corriger le gabarit ne rattrape pas les fiches déjà
  produites. La feuille porte sa propre règle `@page{ size: 8.5in 11in }`, qui
  donne les 612 × 792 pt attendus — d'où la consigne de ne pas en ajouter une
  seconde. Elle demande aussi Nunito par le `<link>` Google Fonts des fiches du
  catalogue ; sans lui la conversion retombe sur Trebuchet, et ça se voit.
  `fiche_pdf.py` cherche cinq marques de la feuille (`--paper`, `--rule`,
  `.eyebrow`, `.nomline`, `.chapeau`) et avertit sur la sortie d'erreur quand
  elles manquent, **sans bloquer** : le format est une affaire d'imprimante et se
  refuse, l'habillage est une affaire de cohérence et se signale. `gabarit_desaccorde()`
  garde le contrôle honnête — si la feuille commune perdait ces marques, le script
  dirait que son propre contrôle ne veut plus rien dire au lieu de crier au
  manquement sur des documents conformes.
- **Le vérificateur trouve seul le prompt d'une commande.** `verifie_activite.py`
  ne cherchait que `<base>-prompt.md` ; la forge écrit `prompt.md`. Les commandes
  de la forge sortaient donc en « doute » avec un code 0 — un appel distrait
  ressemblait à une validation alors que quatre contrôles ne tournaient pas
  (durée, savoirs, faits hors documentation, exigences). Il essaie maintenant
  les deux noms, dans cet ordre, et le message de doute les nomme tous les deux.
- **Un mot isolé qui existe dans une autre langue en prend l'accent.** Sur la
  commande météo, « un abri » et « la radio » sont sortis à l'espagnol : `abrí`
  et `radio` sont des mots espagnols, et un mot seul ne donne au modèle aucun
  contexte de langue. Les six autres mots de la même liste, absents de
  l'espagnol, étaient justes — ce n'était donc pas une affaire d'accents, qui
  étaient bien présents dans les textes. Le seul levier reste l'orthographe
  (`eleven_multilingual_v2` n'accepte ni `<phoneme>` ni `language_code`) : on
  réécrit le mot d'une façon qui n'existe pas dans l'autre langue mais se
  prononce pareil — « un abris », « la radiot ». Même technique que
  `TEXT_OVERRIDES` dans `generer_audio_module_urgence_sons.py`. À vérifier
  systématiquement sur les listes de mots isolés, jamais sur les phrases.
- **Trois verrous, tous nécessaires** : session enseignante (`X-Prof-Token`),
  boucle locale (`_forge_locale()` refuse toute adresse autre que 127.0.0.1) et
  `forge.disponible()`, qui se tait dès que `RAILWAY_ENVIRONMENT` est présent
  ou que le CLI manque. La forge lance un processus : elle n'a rien à faire en
  ligne, et le serveur Railway n'a pas le CLI de toute façon.
- **La page reste autonome, mais elle ne se tait plus qu'ouverte en `file:`.**
  `sonderForge()` disait autrefois la même chose des trois cas (fichier local,
  serveur éteint, session expirée) : rien. Le bouton absent sans un mot se lit
  comme une livraison manquée — c'est la conclusion qu'en a tirée
  l'utilisateur. Chaque cause dit donc maintenant quoi faire (se connecter,
  démarrer le serveur, poste local seulement) ; seul le fichier ouvert par
  double-clic reste muet, puisqu'il n'y a alors rien à réparer.
- **Le livrable se coche à l'étape 1**, au-dessus du niveau : activité
  interactive · avec fichiers MP3 (dépend de la précédente) · fiche élève
  imprimable · corrigé. `S.livrables` est un champ de forme (`CHAMPS_FORME`),
  il se reprend donc d'un modèle. La section « LIVRABLE ATTENDU » du prompt en
  découle, et le préambule de `forge.py` s'y rapporte pour nommer les fichiers
  (`activite.html`, `activite.md`, `corrige.md`, `notes-enseignant.md`) : ce
  sont ces noms-là que la publication reconnaît.
- **`POST /api/forge/publier` fait entrer l'activité générée dans le
  catalogue et dans le dépôt.** Ce ne sont pas la même chose : `activities.json`
  dit qu'une activité existe, `materiel.json` relève les fichiers qui la
  servent — et le second se déduit du premier, d'où la régénération de
  l'inventaire (`regenerer_materiel()`) à la fin. Le dossier de commande est
  recopié tel quel dans `assets/interactive/<slug>/`, arborescence comprise :
  une page qui joue `audio/x.mp3` doit continuer de le trouver. Trois partis
  pris : publication **en atelier**, jamais en cours (un cours se découpe en
  seize séances outillées, qu'une commande ne produit pas) ; corrigé, notes,
  rapport **et la page interactive** deviennent des entrées de `depots.json`
  (l'inventaire ne relève que `slideshow`, `studentDoc` et `planCours` — sans
  cela l'activité paraîtrait au dépôt comme « rien encore ») ; et une commande
  déjà publiée est refusée (`publieeEn` sur sa fiche), sinon le catalogue
  accumulerait des jumelles.
- **Le préambule est dans `forge.py`, pas dans le compositeur.** Le prompt du
  compositeur décrit le *contenu* ; il a été écrit pour être collé dans une
  conversation, où la réponse est du texte. Le préambule ajoute le *livrable* :
  quel fichier, à quel endroit, avec quel système de design.
- Le travail tourne en `--permission-mode bypassPermissions`, `cwd` fixé au
  dossier de la commande et `--add-dir` sur la bibliothèque : il faut qu'il
  puisse écrire et lancer les scripts audio sans personne pour approuver.
  C'est le prix de la génération sans surveillance — d'où la boucle locale.
- **`--add-dir` ouvre un dossier en écriture, pas en lecture.** La bibliothèque
  y était ajoutée pour être *lue* ; en `bypassPermissions`, cela revenait à
  laisser une commande égarée réécrire un module. `forge_garde.py` la referme :
  branché comme hook `PreToolUse` (les hooks s'exécutent dans tous les modes,
  contrairement aux permissions), il refuse tout geste d'écriture vers la
  bibliothèque et laisse passer les lectures. Write et Edit sont décidés sur le
  champ `file_path` — exact ; Bash est décidé sur le texte de la commande —
  heuristique (redirections, `tee`, `mv`/`cp` à destination, `rm`, `sed -i`,
  `git` qui modifie). D'où la deuxième ligne : `_empreinte_biblio()` relève
  `git status` avant et après, et ce qui a bougé est écrit au journal et sur la
  fiche (`intrusions`). On ne répare rien tout seul — l'enseignante peut avoir
  édité un fichier pendant que la commande tournait.
- **`garde.log`, dans le dossier de la commande, dit si le garde s'est
  déclenché.** Fichier vide = le hook n'a jamais été appelé, ce qui est un
  défaut de branchement, pas une absence de danger. C'est le premier endroit à
  regarder si l'on doute du dispositif.
- **Trois plafonds, pas un.** `DUREE_MAX_S` (30 min), `TOURS_MAX` (150 tours,
  comptés ici — le CLI installé n'a pas de `--max-turns`) et `PLAFOND_USD`
  (5 $, réglable par `FORGE_PLAFOND_USD`). Le coût réel n'arrive qu'à la fin,
  dans l'événement `result` : trop tard pour couper. On l'estime donc au fil de
  l'eau — jetons d'entrée comptés exactement (dédoublonnés par `message.id`,
  un message arrivant en plusieurs morceaux), jetons de sortie déduits des
  caractères émis (`CARACTERES_PAR_JETON`). Formule et tarifs vérifiés sur la
  commande Météo : 2,2309 $ estimés contre 2,2201 $ facturés, soit 0,5 %
  d'écart. La dépense monte dans la ligne d'état du compositeur, marquée
  « estimé » tant que le chiffre réel n'est pas là.
- **« Le dossier n'est pas vide » ne veut pas dire « c'est livrable ».**
  `_verifier_livraison()` réclame les quatre fichiers (`activite.html` et les
  trois imprimés), vérifie que chaque PDF est bien au format lettre (612×792
  pt, lu dans son `/MediaBox`) et que sa source HTML porte les marques de la
  feuille commune. Ce qui manque devient une **réserve** : l'activité reste
  publiable, mais la réserve s'affiche en ambre dans le compositeur et reste
  sur la fiche. Seule l'absence d'`activite.html` est un échec — il n'y a alors
  rien à publier.
- Le prompt part par **l'entrée standard** : avec de la documentation jointe il
  dépasse ce qui passe confortablement en argument de ligne de commande.
- `/api/forge/fichier` ne sert que les chemins **réellement produits**, relevés
  par `fichiers_produits()` : le paramètre d'URL choisit parmi eux, il ne
  désigne jamais un chemin. Même règle que les archives du dépôt de matériel.
- `reglages.json` et `garde.log` sont posés par la forge dans le dossier de la
  commande : ils comptent parmi les **fichiers de service**, sans quoi la
  publication les recopierait dans l'activité.

## Dépôt de matériel (PowerPoints et fiches à imprimer)

Suit la remise `~/Downloads/design_handoff_depot_materiel`, source de vérité
visuelle. Quatrième onglet de `enseignant.html`, rendu par `js/materiel.js`.

- `js/materiel.js` **ne connaît ni la session ni les groupes** : `enseignant.js`
  lui passe `{ json, api, activites, groupe }` dans `Materiel.init()`, appelé
  depuis `ouvrirPortail()`. Le module ne touche jamais au `localStorage` ni à
  `fetch` — le jeton reste l'affaire de la page hôte, qui porte sa connexion.
  `init()` est protégé contre le double branchement (reconnexion).
- Le dépôt se charge **à la première ouverture de l'onglet**, pas au démarrage.
- **« Ma semaine » ne peut toujours pas dire « mardi, séance B3 »** : les dates
  de section de `schedule.json` suivent le découpage du *module* (six sections),
  pas la grille des **seize séances** du dépôt (`a1…e2`). Deux grilles
  distinctes : la première dit ce que l'élève peut ouvrir, la seconde ce que
  l'enseignante projette en classe. La rangée du jour affiche donc l'activité
  et offre ses seize séances en pastilles cliquables. Les relier demanderait
  une correspondance séance → section, qui n'existe pas encore.
- **L'impression passe par un cadre isolé** (`#matImpression`), pas par une
  zone de la page : les fiches sont déjà des documents imprimables noir et
  blanc, on les charge avec leurs propres styles et on imprime le cadre. Rien
  de l'interface ne peut s'y glisser, et une série sort en un seul dialogue
  (`page-break-after` entre les fiches). Ne pas remplacer par une injection
  dans la page : les classes des fiches (`.card`, `.bloc`) entreraient en
  collision avec celles du système de design.
- Le filtre « Niveau » ne paraît que s'il y a plus d'un niveau au catalogue.

### Promotion d'un dépôt (« Remplacer l'officiel », admin)

- **Une promotion n'écrase jamais le fichier officiel.** Elle est enregistrée
  dans `data/promotions.json` (volume, non versionné) et la substitution se
  fait **à la lecture**, dans `materiel_promu()`. Écraser le `.pptx` serait
  défait au prochain `build.py`, qui le régénère depuis `decks/` : la classe
  retrouverait l'ancienne version sans que personne l'ait demandé.
- `materiel_promu()` sert **l'écran et les archives** : promouvoir n'aurait
  aucun sens si « Tout prendre » continuait de descendre l'officiel.
- Le fichier promu **est remesuré** (diapositives, blocs) et perd la vignette
  de l'officiel : hériter de ses mesures ferait annoncer « 17 diapositives »
  devant une version qui en a douze. `cheminOfficiel` reste dans la réponse,
  et l'officiel demeure téléchargeable dans le panneau.
- Une promotion **antérieure** à la dernière production de l'officiel est
  marquée `perimee` : l'écran avertit qu'elle cache une production plus
  récente, au lieu de la laisser agir en silence.
- Retirer un dépôt promu **défait sa promotion** — sinon l'inventaire
  pointerait vers un fichier disparu.
- Routes : `POST /api/materiel/promotion` (`{fichierId, depotId}`),
  `DELETE /api/materiel/promotion/<fichierId>`. Les deux exigent le rôle
  `admin`, revalidé côté serveur.

- **Les présentations sont rangées par module** : `assets/powerpoints/<slug>/`.
  Le slug est celui de `assets/interactive/<slug>/` — c'est la clé qui relie un
  fichier à son activité. À plat, le `A1` du module 8 écraserait celui du
  module 9.
- **Les dix modules du registre sont produits**, seize séances chacune :
  `python3 build/powerpoints/build.py <slug>` et
  `python3 build/powerpoints/build_fiches.py <slug>`, ou `--tous` pour les dix.
  **`module-sante` était catalogué `atelier` par erreur** (reste de l'époque où
  le contenu santé n'était pas encore un module) : il disparaissait de la liste
  des modules du portail élève, et le dépôt ne montrait qu'une séance au lieu
  de seize — `porteur_cours` n'est appelé que pour une activité `cours`. Corrigé
  dans `data/activities.json` (activité 34 → `cours`), suivi de
  `python3 build/materiel.py`. **Attention** : `categorie` fait partie des
  `USER_FIELDS`, donc c'est le volume qui tranche, pas le code — la correction
  doit être refaite en ligne par le modal de modification d'admin, un
  redéploiement ne la porte pas.
  Le **registre `build/powerpoints/modules.py`** est la source unique : numéro,
  **niveau**, titre affiché en pied de page, nom des blocs et ordre
  d'enseignement. Aucun autre fichier ne porte de constante de module — pas
  `build.py`, pas `theme.py`, pas `fiche.py`, pas le manifeste de
  `build/contenu/<slug>/`.
- **Le niveau n'est écrit en dur nulle part** : il vient du registre. Le lisent
  `build/module.py` (jeton `%%NIVEAU%%` du HTML) et `build_fiches.py`
  (l'en-tête des fiches élèves) ; `build/vocab_flash.py` porte le sien dans sa
  propre table de thèmes. Les seuls « Niveau 4 » restants dans le code sont les
  **repères de recherche** de `build/gabarit.py` — le texte qu'il remplace par
  un jeton — et des commentaires sur les niveaux de titre.
- **Les slugs restent globalement uniques, tous niveaux confondus.** Les
  dossiers de sortie sont à plat (`assets/interactive/<slug>/`,
  `assets/powerpoints/<slug>/`) : un `module-sante` de niveau 6 écraserait
  celui du niveau 4. Lui donner un autre slug coûte un mot ; ranger les
  sorties par niveau casserait les adresses déjà distribuées aux élèves, les
  chemins de `activities.json` et les clés de reprise en `localStorage`.
- **Le nombre de séances suit le nombre de défis**, pas une grille imposée :
  trois défis donnent 4-4-4-2-2 (blocs A à E), deux défis donnent 4-5-5-2
  (blocs A, B, C, E). Seize séances dans les deux cas, mais un module sans
  « Défi 3 » n'a pas de bloc D.
- **Le contenu d'un deck est original**, écrit à partir des constantes du module
  interactif (`DIALOGUES`, `SECTIONS`, `EXOS`, `PLUS`, `FC_CARDS`) — jamais
  recopié d'un manuel. Un deck se relit à l'en-tête : il nomme les exercices
  dont la séance est tirée.
- **Rien qui sorte de Verdana** : ni alphabet phonétique, ni flèche, ni ✓ ni ✕.
  Les sons se nomment par leurs lettres et un mot repère (« le son *an*, comme
  dans *dent* »). `fontTools` doit être installé, sinon le garde-fou se tait et
  un carré vide part chez l'enseignant.
- **Le garde-fou des tableaux a un budget, et le connaître épargne trois
  reprises** : `d.tableau()` accepte six rangées, mais **pas** six rangées
  plus une `note`. Il descend le corps jusqu'au plancher puis refuse, plutôt
  que de livrer une diapositive tronquée — le message dit « coupez-le en deux
  tableaux », et c'est rarement la bonne correction. La bonne est de descendre
  la `note` dans les `notes` de l'enseignante : elle s'y lit de près, alors
  qu'en petits caractères sous un tableau projeté personne ne la lit. Trois
  déclenchements le 23 août 2026 en produisant `module-n8-oeuvres`, et les
  trois avaient raison.
- **`data/materiel.json` est produit, jamais écrit à la main**
  (`python3 build/materiel.py`). C'est le relevé de ce qui existe sur le
  disque : une entrée non vérifiée serait un lien mort. `--verifier` compare
  sans écrire. Il ne recopie **aucun** titre d'activité : il ne connaît que des
  `activiteId` — les **entiers** de `activities.json`, pas des slugs.
- La grille des séances a une source unique : `MODULES` de
  `build/powerpoints/modules.py`, que `build/materiel.py` importe. Un module sans
  dossier de production est mesuré contre la grille standard à seize (4-4-4-2-2),
  ce qui permet d'afficher « 0 séance sur 16 » au lieu de le taire.
- **Le `studentDoc` d'un module de cours est son sommaire de fiches**,
  `assets/documents/<slug>-fiches-eleves.html`, produit par `build_fiches.py`.
  Les neuf sont renseignés dans `data/activities.json`.
- **Captures des exercices dans les séances** :
  `python3 build/powerpoints/captures.py <slug>` produit une image par
  exercice à banc de réponses dans `build/powerpoints/_captures/<slug>/`, et
  `d.capture('pr1', "titre")` la pose dans un deck, **après** la diapositive
  « Pratique » du même exercice — elle ne la remplace pas : une image projetée
  ne se lit pas d'aussi loin qu'un texte composé pour l'être, et l'enseignante
  a besoin du corrigé écrit. L'écran est capturé **vierge**, zones de dépôt
  vides. Le nom du fichier est l'identifiant d'exercice que l'en-tête du deck
  cite déjà (« Source du module : … exercice `pr1` »).
  Trois pièges de Chrome sans interface, tous documentés dans le script :
  `--dump-dom` ne rend jamais la main sur ces modules (d'où le manifeste
  renvoyé au serveur) ; **la capture n'est écrite qu'à l'arrêt** du
  navigateur, mais le couper trop tôt n'écrit rien — d'où le signal « c'est
  cadré » émis par la page, puis quelques secondes de répit ; et le banc de
  réponses, `sticky`, doit repasser en `static` pour la capture, sinon il
  apparaît décroché de ses zones de dépôt.
- **Vignettes** : `python3 build/vignettes.py` → `assets/vignettes/<slug>/<CODE>.png`.
  Le poste n'a pas LibreOffice ; on réutilise `build/powerpoints/apercu.py`, qui
  relit le `.pptx` livré et le repeint avec Pillow (paramètre `limite=1`).
  Ne rend que ce qui a changé.
- **Deux fichiers, deux natures, jamais mêlés** : `data/materiel.json` est
  produit par le build et versionné (lu depuis `BASE_DIR`) ; `data/depots.json`
  et `assets/depots/` portent les fichiers téléversés par les enseignants, donc
  du volume et non versionnés. Les mêler effacerait le dépôt d'une collègue à
  chaque build.
- Routes : `GET /api/materiel` (inventaire + dépôts + `derniereVisite` + rôle),
  `GET /api/materiel/archive?activiteId=&portee=&codes=`,
  `POST /api/materiel/depot` (multipart), `POST /api/materiel/visite`,
  `DELETE /api/materiel/depot/<id>` (admin, rôle revalidé côté serveur).
- **Les archives se fabriquent à la demande, en mémoire** — jamais de `.zip` sur
  disque, qui serait périmé au prochain build. Portées : `module`,
  `presentations`, `fiches`, `seances`. Le nom reste lisible par un humain
  (`module-probleme_B3-C1-C2.zip`, suffixe `-et-N-autres` au-delà de quatre).
  Seuls les chemins **inscrits à l'inventaire** entrent dans une archive : le
  paramètre d'URL choisit parmi eux, il ne désigne jamais un chemin.
- `GET /api/materiel` **n'avance pas** `derniereVisite` : sinon un simple
  rafraîchissement effacerait les repères « nouveau » avant lecture. C'est
  `POST /api/materiel/visite` qui l'avance, une fois l'écran rendu. La date
  vit sur le compte (`derniereVisiteMateriel`), pas dans le `localStorage`.
- Le nombre de **pages** d'une fiche n'est pas mesurable (il dépend de
  l'imprimante) : l'inventaire compte des **blocs**, écrits dans la fiche.
  N'affichez pas « 2 pages » quelque part sans l'avoir mesuré.

## Fichiers du groupe et lien de rencontre

- Un fichier partagé (`data/documents.json`) a une **période de parution**
  (`ouverture` / `fermeture`) et suit exactement la règle des activités
  (`is_offered()`) : sans date d'ouverture, l'élève ne le voit pas. Un dépôt
  paraît dès le jour même, sans date de retrait.
- Endpoints : `GET/POST /api/prof/documents`, `PATCH/DELETE
  /api/prof/documents/<id>`. Le fichier est stocké sous
  `assets/documents-groupe/<groupId>/<id>-<nom>` — préfixé par l'identifiant
  pour que deux fichiers du même nom cohabitent.
- Le groupe porte un champ `teams` (lien de rencontre), et une entrée de
  `schedule.json` un champ `lien` (rencontre propre à une activité).
  `normalize_lien()` n'accepte que `http(s)` : rien d'autre n'atteint le
  portail des élèves.
- `POST /api/prof/planification/copier` reprend la planification d'un autre
  groupe de l'enseignant, décalée de N jours. **Elle remplace** les dates du
  groupe cible ; la date « vue en classe » n'est pas copiée.
- Côté élève, `/api/student/dashboard` renvoie `teams` et `documents`
  (uniquement ceux en parution aujourd'hui) ; `eleve.html` les affiche.

## Portail élève (`eleve.html`)

- Refait selon la remise de design « portail élève, variante 2a » : bande acier
  (`--surface-band: var(--acier-100)`), bilan en trois chiffres, un seul bloc
  encre (« Votre prochaine étape »), modules en tuiles à filet de couleur,
  ateliers et exercices libres en rangées d'une carte `card--flush`.
- La page lie `assets/design-system/styles.css` — **jamais `ds-bundle/`, qui est
  dans `.gitignore`** et n'existe donc pas en production — et n'utilise que les classes du système
  (`.band`, `.card`, `.btn--pri`, `.grid-auto`, `.exo--*`). **Aucune couleur en
  dur** : les deux seules pièces écrites à la main sont la barre de progression
  (`.om-bar`) et l'étiquette d'état (`.om-etat`), qui n'existent pas dans le
  système. L'état porte toujours un glyphe **et** un mot (`✓ → · `) — la
  couleur ne dit jamais l'information seule.
- Répartition : `categorie: "cours"` → tuiles de modules ; les autres ateliers
  → « Activités thématiques », sauf les domaines transversaux (vocabulaire,
  grammaire, pratique orale libre) → « Pour vous exercer seul », sans état.
- `/api/student/dashboard` renvoie `parActivite` (pct, faite, zones/zonesDone
  tirés des enregistrements `exercise_completed`) et `semaine`
  (jours de pratique sur sept, minutes **estimées** à partir des traces du
  journal — rien ne mesure le temps réel passé dans une activité).

## Barre d'outils élève (rail « Mes outils »)

- Sept outils permanents dans chaque module : traduire · lire · simplifier ·
  prononcer · demander à l'assistant · mon carnet · réviser. Code partagé dans
  `assets/design-system/outils-eleve.{js,css}` — ne rien y écrire qui dépende
  d'un module précis.
- **Ajouter un outil ne demande aucune regreffe** : la liste `OUTILS`, les
  tracés d'icônes et les panneaux vivent tous dans le fichier partagé. Les onze
  modules — `module-probleme` compris, pourtant généré — l'ont dès le
  rechargement. Ne pas relancer `greffe_outils.py` pour ça.
- **« Mon carnet » et « Réviser » ne se recouvrent pas** : le premier garde les
  mots que l'élève surligne (`localStorage`), le second travaille les listes que
  le cours lui donne. Le panneau « Réviser » **ne révise pas** — il montre l'état
  des listes (`GET /api/vocab/listes?code=&module=`) et ouvre l'application de
  cartes mémoire sur la bonne liste (`?code=&liste=<activityId>`). Deux moteurs
  de répétition espacée, ce serait deux progressions qui divergent.
- **Le module ne connaît pas son numéro d'activité** : il passe son slug, et
  c'est le serveur qui retrouve la liste courante par le chemin `interactive`
  du catalogue. Même règle que partout ailleurs — aucun id écrit dans un module.
- Les classes du panneau sont préfixées `.oe-liste` : `.oe-mots` appartient
  déjà à l'outil de prononciation.
- **La greffe dans les modules passe par `build/greffe_outils.py`**, jamais à
  la main : marqueurs `OUTILS-ELEVE:début/fin`, dégreffe avant regreffe, donc
  relançable après toute modification d'un gabarit.
  `python3 build/greffe_outils.py` traite les onze modules ; il saute
  `module-probleme`, **généré**, dont le `build.py` appelle la même fonction
  `greffe()`. Ce dégreffage préalable est nécessaire : `module-consultation`
  est le gabarit du module 9 et porte sa propre greffe, avec SON slug.
- Aucun `data-oe` dans le balisage des modules : chaque module passe le
  sélecteur `.card, .savoir` à `Outils.init()`, et un MutationObserver marque
  les blocs que `render()` recrée.
- Routes serveur : `/api/outils/traduire`, `/api/outils/simplifier`,
  `/api/outils/assistant`, plus `voix: "lecture"` sur `/api/voix`. Les deux
  premières sont mises en cache sur disque (`data/outils_cache.json`, non
  versionné) : trente élèves surlignent la même consigne, on paie une fois.
- **`/api/voix` est aussi en cache disque**, mais en fichiers et non en JSON :
  `data/voix-cache/<voix>-<empreinte>.mp3`. ElevenLabs facture au caractère et
  c'est le plus gros poste de la facture d'API — la lecture d'une consigne par
  toute une classe doit être payée une fois. Trois partis pris : le cache est
  consulté **avant** la clé d'API (une classe garde la voix des passages déjà
  lus si la clé vient à manquer) ; il vit sous `data/` et non `assets/`, sinon
  le serveur de fichiers rendrait les MP3 téléchargeables sans code élève ; et
  il est **plafonné** (`VOIX_CACHE_MAX_MO`, 300 Mo par défaut, élagage des
  moins récemment servis) parce que les répliques du jeu de rôle sont uniques
  et rempliraient le volume. Rien n'y est une source de vérité : tout ce qu'on
  jette est régénéré au prochain appel.
- Trois partis pris à ne pas défaire : la traduction s'ajoute **sous** le
  français et ne le remplace jamais (pas de « traduire toute la page ») ;
  « simplifier » reformule **en français** ; l'assistant **ne donne jamais la
  réponse d'un exercice**, il cite la phrase du dialogue et repose une
  question plus facile.
- Icônes : les six tracés SVG du système de design (grille 24, trait 2,2,
  bouts ronds). **Aucun émoji, aucun jeu d'icônes tierce partie.** Rouge
  réservé à « Lire » ; sélectionné = plaque encre `#17181A`.
- **Le rail se masque** (bouton « Masquer », onglet « Mes outils » pour le
  rappeler) mais **sans mémoire** : il est là à chaque ouverture du module. Un
  élève qui l'a masqué hier ne doit pas se retrouver sans outils aujourd'hui.
  Attention en y ajoutant du texte : `.oe-root button{font:inherit}` l'emporte
  sur un `font-size` posé sur le bouton — la taille va sur le libellé enfant.
- **Les cartes mémoire traduisent par `Outils.traduire(texte, contexte)`**, qui
  rend une promesse `{texte, langue}` et porte déjà la langue choisie, le code
  élève et le cache serveur. Ne pas rappeler `/api/outils/traduire` à la main
  depuis un module. La greffe dans les onze modules passe par
  `python3 build/cartes_memoire.py` (`--verifier` pour un état des lieux) :
  substitutions exactes, refusées si le module a divergé. `module-probleme`
  étant généré, on relance ensuite `build/module.py module-probleme`.
- `server.py` lit `.env` au démarrage (les variables déjà définies gagnent) :
  sans ça, rien n'est testable en local. En production les clés viennent des
  Variables Railway — **et un changement de variable n'atteint le serveur
  qu'au redéploiement**, sinon l'ancienne valeur reste en mémoire.

## Vocabulaire : le banc, les listes et la maîtrise

L'application de mémorisation est `assets/interactive/vocabulaire-flash/`
(activité 31). Répétition espacée à sept boîtes ; l'élève **écrit** le mot à
partir de sa définition, l'IA corrige, et trois boutons rangent la carte.

- **Le banc de mots est dans `server.py` (`VOCAB_BANK`), et lui seul.** Chaque
  mot porte les `activityIds` des activités qui l'enseignent. C'est cette
  liste-là qui relie un mot à un module — rien d'autre à tenir à jour.
- **Les cartes des modules y sont rattachées** : les 134 cartes `FC_CARDS` des
  onze modules donnent 129 mots (un mot enseigné par deux modules reste **une**
  entrée à deux `activityIds`, même boîte, comptée dans les deux listes).
  Leur identifiant reprend le **slug du module** (`probleme-16`), jamais un
  numéro : `wordId` est la clé de la progression enregistrée, et la
  renumérotation des modules ne doit pas la casser.
- **`VOCAB_BOITE_MAITRISE` (boîte 4) est le seuil de « maîtrisé », défini une
  seule fois.** La fiche de l'élève et l'écran des listes doivent compter
  pareil ; ne pas réécrire `>= 4` à la main.
- **Une liste, c'est le vocabulaire d'une activité offerte au groupe**
  (`GET /api/vocab/listes`) : total, maîtrisés, en cours, jamais vus, dus
  aujourd'hui. Les modules d'abord, dans l'ordre de leur numéro (« Module 10 »
  après « Module 9 »), puis les ateliers. Le titre vient du catalogue — le banc
  ne recopie aucun libellé.
- `GET /api/vocab/session` accepte `activityId` (une liste) ou `domain` (la
  session « tout ce qui est dû », qui traverse les modules).
- **L'élève entre par le rail « Mes outils » de son module** (outil « Réviser »),
  qui ouvre l'application sur la liste du module. L'atelier 31 reste
  planifiable, mais la révision ne dépend plus du calendrier.
- **Les mots ne servent que ce qui est ouvert au groupe** : `get_student_vocab_pool()`
  filtre sur `get_available_activity_ids()`. Un groupe neuf voit donc 0 mot,
  et le dénominateur de la fiche grandit à mesure que la planification avance.
- **La section « Je retiens des mots » d'un module n'écrit rien** : elle ne
  touche qu'à `/api/vocab/translate` et `/api/vocab/signaler`, le reste vit dans
  le `localStorage`. Seule l'activité 31 fait monter une boîte. C'est voulu —
  une seule porte d'entrée dans la progression.
- **Aucun mot n'a d'audio, et seul `module-probleme` a des images** (10 sur 16,
  dans `assets/interactive/module-probleme/vocab/`). La carte flash n'affiche ni
  l'un ni l'autre ; le banc ne porte donc pas ces champs.

## Tutoriels de l'espace enseignant

Deux formes du même contenu, à garder d'accord entre elles. Le bouton
« Tutoriels » de la barre de groupe ouvre la page vidéo, qui renvoie elle-même
vers les diapositives.

- `assets/outils/tutoriels-enseignant.html` — **produite** par
  `build/tutoriels/livrer.py`, jamais écrite à la main : sa transcription et
  ses sous-titres sont le texte même de la narration. Les sept capsules vivent
  dans `assets/tutoriels/`, versionnées avec leurs sous-titres `.vtt` et leurs
  affiches `.jpg`.
- **Les capsules sont un vrai enregistrement d'écran**, pas des captures
  fixes : `Page.startScreencast` filme pendant qu'un script se sert du
  portail, avec un pointeur animé injecté dans la page (`scene.js`). Un écran
  immobile n'émet aucune image — le montage donne donc à chaque image la durée
  relevée au tournage, jamais une cadence fixe, et **jamais de durée plancher**
  (Chrome émet par rafales ; un plancher les allonge et le film prend du retard
  sur la voix). Le tournage se fait à vitesse réelle : environ une minute par
  minute de capsule.
- **La voix et l'image sont calées au mot près.** `aligner.py` relève par
  **alignement forcé** l'instant de chaque mot des MP3 déjà produits, et un
  geste du manifeste porte un repère (`"apres": "une barre apparait"`) : le
  tournage attend ce mot pour le jouer. Sans ça, un plan n'est calé qu'à son
  début et l'écart grandit jusqu'à sa fin. Un repère introuvable arrête le
  tournage ; un repère raté s'affiche en avertissement.
- `assets/outils/guide-espace-enseignant.html` — le même parcours en vingt
  diapositives animées, navigables au clavier et imprimables. Écrit à la main.
- **La chaîne de production est dans `build/tutoriels/`** — voir son
  `LISEZMOI.md`. `manifeste.json` y est la source unique : gestes à capturer,
  élément à surligner et texte dit par la voix, dans la même entrée.
- **Les capsules sont filmées dans une instance jetable** (`lancer_demo.sh`,
  `STORAGE_DIR` hors du dépôt) peuplée de groupes et d'élèves **inventés**.
  `init_storage()` recopiant le catalogue dans le bac à sable, purger
  `teachers/groups/students/schedule.json` avant de recommencer — sinon on
  filme de vraies personnes.
- Voix « narrateur » d'ElevenLabs, distincte des voix de personnages des
  dialogues. `narrer.py` ne repaie pas un plan déjà narré (facturation au
  caractère) : effacer un MP3 précis pour le refaire.

## Le registre des appels d'API (`journal_api.py`)

**Une ligne par tentative, réussie ou non**, dans `data/appels_api.jsonl`
(volume, non versionné). Il existe parce que
`assets/presentations/prix-dun-module.html` chiffrait un module à 36 $ pour
vingt élèves sur des **hypothèses d'usage inventées** — vingt tours
d'assistant, vingt répliques de jeu de rôle. Personne ne comptait.

```
python3 build/couts_api.py                 # par élève
python3 build/couts_api.py --par-route     # par route
python3 build/couts_api.py --depuis 2026-08-25
```

En ligne, `GET /api/admin/appels?groupId=&depuis=` rend le même calcul,
filtré au groupe et réservé à son enseignant. Le script ne lit que le volume
**local** : il ne peut rien dire de la production, comme
`build/controles/organisations.py`.

- **Les jetons sont ceux que l'API renvoie**, jamais une estimation : le
  champ `usage` de la réponse est recopié tel quel. Le montant en dollars,
  lui, vient de la table `TARIFS` de `journal_api.py` — il vieillit, et c'est
  un montant estimé, jamais la facture. Même réserve que pour les images.
- **Les quatre compteurs de jetons se tarifent séparément.** Entrée, sortie,
  écriture de cache (1,25 × entrée) et lecture de cache (0,1 × entrée). Les
  additionner comme un seul nombre surestime d'un tiers un tour de jeu de
  rôle, dont la consigne système est mise en cache. Vérifié sur une réponse
  canonique : 0,0093 $ contre 0,0201 $ si l'on ignore le cache.
- **Ni texte ni code d'élève n'entrent dans le registre.** Le texte, parce que
  les corrections IA restent privées ; le code, parce qu'il *authentifie* —
  l'écrire dans un journal reviendrait à écrire un mot de passe. On garde
  l'`id` de l'élève et celui de son groupe. `_repere_eleve()` fait la
  résolution, au prix d'une relecture de `students.json` que
  l'authentification de la route venait déjà de faire.
- **Un appel servi par le cache est noté à zéro dollar, et noté quand même.**
  C'est la mesure qui intéresse : un registre qui ne verrait que les appels
  payés ne dirait jamais combien il en a épargné. Idem pour un refus (401,
  quota épuisé) : la ligne garde son nombre de caractères, son montant tombe
  à zéro.
- **`route`, `code` et `module` sont passés explicitement** aux deux
  fonctions d'appel, jamais devinés depuis le contexte de la requête. Une
  route mal étiquetée fausserait le compte par élève sans rien casser
  d'autre — donc sans que rien ne le signale.
- **`noter()` n'échoue jamais l'appelant**, comme `journal()` de l'audit : un
  registre qui fait planter le geste qu'il enregistre ferait perdre l'appel
  *et* la trace. Et l'import de `journal_api` est protégé comme celui de
  `forge` — un fichier oublié dans un commit ne doit pas tuer le conteneur.
- **Les trois modèles sont nommés une fois** (`MODELE_CORRECTION`,
  `MODELE_CONVERSATION`, `MODELE_VOIX`). Le registre les tarife par leur
  identifiant : un modèle changé dans un payload sans l'être dans la
  constante serait compté au prix de l'autre, en silence.

## Signalements (« Outil en développement »)

Le portail enseignant porte, sous la barre de parcours, un bandeau ambre qui
dit que l'outil est en développement, et le bouton **« Signaler un problème »**.
Personne d'autre ne le voit : le portail élève ne porte rien de cela.

- `POST /api/signalement` (session enseignante) écrit la fiche dans
  `data/signalements.json`, **puis répond**. Le tri par l'IA et le courriel
  partent dans un fil de fond : un serveur SMTP lent ne doit jamais faire
  croire que le signalement n'est pas passé.
- Le fil de fond fait deux choses, dans cet ordre : `triage_signalement()`
  (modèle `claude-haiku-4-5-20251001`, trois lignes — gravité, nature, à
  corriger ou non) écrit dans le champ `analyse`, puis `envoyer_courriel()`
  envoie la note au responsable avec la description **et** ce premier tri.
- Les deux appels sont sans filet obligatoire : sans `ANTHROPIC_API_KEY`
  l'analyse reste vide, sans configuration SMTP rien ne part — la fiche est
  gardée dans les deux cas, et le journal le dit.
- **Configuration du courriel** (variables Railway) — deux chemins, essayés
  dans cet ordre par `envoyer_courriel()` :
  1. **Resend** (celui en service) : `RESEND_API_KEY`, et `RESEND_EXPEDITEUR`
     si un domaine est vérifié — à défaut, l'adresse de bac à sable
     `onboarding@resend.dev`, qui n'écrit qu'au propriétaire du compte
     Resend. Une requête HTTPS, donc ni port sortant bloqué ni mot de passe
     de compte en jeu. **Gmail a été écarté** : les mots de passe
     d'application ne sont pas offerts au compte (comptes scolaires, clés
     d'accès ou double validation absente — Google masque l'option sans dire
     laquelle).
  2. **SMTP**, gardé pour un éventuel relais du centre : `SMTP_HOTE`,
     `SMTP_PORT` (465 SSL par défaut, 587 bascule en STARTTLS), `SMTP_USER`,
     `SMTP_MOTDEPASSE`.
  Destination commune : `SIGNALEMENT_DESTINATAIRE`. Une clé Resend présente
  mais refusée **ne bascule pas** sur le SMTP : une configuration cassée doit
  se voir dans le journal, pas se faire rattraper en silence.
- **L'en-tête `User-Agent` n'est pas décoratif.** Sans lui, urllib s'annonce
  « Python-urllib/3.x » et le pare-feu devant l'API de Resend répond
  `403 error code: 1010` — un refus de Cloudflare, jamais atteint par la clé.
  Le message ressemble à un problème d'authentification et n'en est pas un.
  Ne pas le retirer en nettoyant les en-têtes.
- **Le bouton « Tester l'envoi du courriel »** (fenêtre de signalement,
  `POST /api/signalement/essai`) déclenche un envoi et rapporte la réponse du
  service à l'écran : la voie utilisée, l'adresse de destination et le message
  brut du refus. Ouvert à **toute session enseignante** — le réserver à
  l'administrateur le cachait à la personne qui dépannait, et la réponse ne
  porte ni clé ni mot de passe. C'est lui qui a rendu le `1010` lisible ;
  sans lui, il fallait ouvrir les journaux de l'hébergeur.
- La raison de l'échec est gardée dans la fiche (`courrielRaison`) : on peut
  relire après coup pourquoi une note n'est pas partie.
- `GET /api/signalements` renvoie les siens ; le compte administrateur voit
  tout. La modale n'en affiche que les trois derniers : elle sert à écrire,
  pas à consulter.
- Le signalement ne porte **aucun nom d'élève ni aucune de leurs réponses** :
  nom de l'enseignante, écran, adresse de la page, navigateur, description.

## Le mode sans IA (un centre peut refuser l'assistant)

Une direction peut refuser que ses élèves parlent à une IA. Le refus se pose
sur **l'arbre des organisations**, pas sur un groupe ni sur un compte : c'est
la seule autorité qui a un sens ici, et elle est déjà en place.

- **Champ `ia` sur un nœud** : `herite` · `autorisee` · `interdite`.
  `ia_effective(orgId)` remonte vers la racine et **le premier réglage
  explicite tranche** — « interdite » sur un CSS ferme ses douze centres, et
  celui qui a négocié une exception la porte écrite sur lui-même. Sans réglage
  nulle part, l'IA reste **autorisée** : une mise en service ne doit rien
  éteindre au passage. Le réseau ne peut pas « hériter » — il n'a personne
  au-dessus.
- **Le bouton est dans `reseau.html`** (« Régler l'IA »), réservé au fondateur
  comme les autres gestes de l'arbre. Le badge de chaque nœud dit l'état
  **effectif** et, quand il vient d'ailleurs, de qui : « hérité de CSS X ».
  L'héritage est calculé au serveur (`arbre_pour_lecture`) — deux calculs
  d'une même règle finissent toujours par diverger.
- **Dix routes sont gardées, pas sept.** Les sept du module
  (`correct-french`, `correct-email`, `check-written`, `jeu-de-role`,
  `analyser-erreurs`, `vocab/translate`, `voix`) **et les trois de la barre
  « Mes outils »** (`outils/traduire`, `outils/simplifier`,
  `outils/assistant`), qui sont la plus grosse surface d'IA d'un module et
  qu'on oublie parce qu'elles ne sont pas dans le HTML. Le garde est
  `_ia_refusee()`, appelé juste après l'authentification.
- **`GET /api/student/ia?code=`** est la seule question que pose le module. Un
  code inconnu obtient `false` : un module ouvert hors du portail ne doit pas
  montrer des boutons que les routes refuseront.

Le repli côté élève est **cosmétique**, et c'est voulu : une page se modifie
avec deux touches, la décision vit au serveur.

    python3 build/greffe_sans_ia.py --tous       # gabarit + les 87 modules
    python3 build/greffe_sans_ia.py --un <slug>
    python3 build/greffe_sans_ia.py --tous --retirer

Ce qui tombe et ce qui reste : plus de rétroaction avant l'envoi (l'enseignant
reçoit le texte **non corrigé**), la moitié « avec l'assistant » du jeu de rôle
disparaît mais l'activité de classe reste, « Pourquoi je me trompe ? » part et
la mini-leçon reste, les réponses à réponse connue se corrigent comme avant
(c'est de la comparaison de chaînes), les réponses ouvertes donnent la réponse
attendue après deux essais. Dans le rail, `Outils.sansIA()` retire **traduire ·
simplifier · demander** et le bandeau de langue maternelle ; **lire · prononcer
· carnet · réviser** restent — quand `/api/voix` refuse, `dit()` retombe sur la
voix du navigateur, qui est une fonction du système d'exploitation.

Trois choses payées en le faisant :

- **La carte du jeu de rôle promet l'assistant dans 77 modules sur 78**, dans
  une phrase d'ouverture qui vit **avant** le séparateur, donc que le masquage
  ne touchait pas. Un module qui annonce « L'assistant joue la personne qui
  t'accueille » puis n'offre rien est pire que pas de repli du tout. La greffe
  retire les **blocs de texte** qui le mentionnent — un élément dont les
  enfants sont tous en ligne (`b`, `span`, `br`) ; se limiter aux feuilles ne
  suffit pas, ces phrases portent presque toutes un `<b>`.
- **Un seul module sur 78 a des fiches à imprimer** (`module-logement`). Le mot
  qui explique ce que devient l'exercice se règle donc sur la présence de
  `.jr-print`, sinon il renverrait 77 classes vers des fiches qui n'existent
  pas. Les 78 gardent, eux, du contenu de classe avant le séparateur —
  situations, sujets à couvrir, rappel de grammaire.
- **`marqueBlocs()` de la barre d'outils repousse à chaque `render()`.** Le
  drapeau `SANS_IA` du fichier partagé existe pour ça : retirer les marqueurs
  de traduction une fois au chargement les laisse revenir à la première
  section rendue.

Vérifié en jouant, jamais en relisant : les 87 modules ouverts un à un dans le
navigateur avec un centre à « interdite » — repli complet, aucune promesse
d'assistant visible, zéro erreur de console — puis quatre rouverts avec le
centre remis à « autorisée », qui retrouvent leurs sept outils et leurs deux
boutons de vérification. Le même fichier sert les deux versions.

## Le mode séance (travailler sans compte élève)

Un troisième mode, à côté d'« avec IA » et « sans IA ». L'enseignant ouvre une
**séance** sur un module d'un de ses groupes ; les élèves y entrent par un code
à six caractères (imprimé, un code QR) et travaillent **sans compte, sans
pseudo, sans donnée identifiante**. Le point de départ reste le compte de
l'enseignant : lui seul ouvre une séance, et tout remonte dans son portail, sur
la progression de ce groupe-là. Deux groupes sur un même module = deux séances,
deux codes, deux tableaux — le code dit d'où viennent les réponses.

**La direction autorise, l'enseignant choisit.** Deux gestes, et les confondre
serait l'erreur. Ouvrir une classe sans compte est une décision
d'établissement — elle touche à ce que l'école accepte de ne pas savoir de ses
élèves ; s'en servir un mardi matin est une décision pédagogique, qui
appartient à l'enseignant. Le réglage vit donc sur **l'arbre des
organisations**, à côté de `ia`, `voix` et `depot` : champ `seance`
(`herite` · `autorisee` · `interdite`), `seance_effective()` remonte et le
premier réglage explicite tranche, défaut « autorisée » — ce mode collecte
moins que le portail ordinaire, une direction qui n'a rien réglé n'a rien
perdu. **Sur les organisations seulement** : un drapeau par enseignant ferait
passer pour une permission ce qui est un choix, et un bouton absent
n'aurait plus d'explication. `seance_pour_enseignant()` remonte par le centre
de rattachement ; `/api/prof/me` rend `seanceAutorisee` pour que l'écran
n'offre pas un bouton mort, mais **c'est la route qui garde, pas la page**.
L'autorisation est vérifiée **à l'ouverture d'une séance, jamais à l'entrée
d'un élève** : une direction qui ferme le mode à 10 h ne doit pas éteindre une
classe en train de travailler.

**Le pivot.** L'identité de l'élève voyage déjà par le seul paramètre `code`, et
les vingt-sept routes qui la vérifient passent toutes par
`validate_student_code`. Le jeton de séance emprunte ce chemin : **aucun des 87
modules n'est retouché**, aucun ne sait ce qu'il transporte.

- **Ce qu'on n'a pas eu à écrire, et c'est le meilleur du chantier.**
  `ia_pour_eleve`, `voix_pour_eleve`, `depot_pour_eleve` et les sections
  remontent tous par `groupId` ; un participant en porte un vrai. Le refus d'IA
  d'une direction s'applique donc au mode séance **sans une ligne de plus** —
  c'était le premier risque identifié, et la bonne réponse était de n'avoir rien
  à écrire plutôt qu'un second chemin d'héritage à tenir.
- **Liste blanche, jamais liste noire.** `ROUTES_SEANCE` nomme les routes
  ouvertes à un participant ; le chemin de la requête est posé sur le fil par
  `_REQUETE.chemin` dans les quatre `do_*`. Une route ajoutée demain est fermée
  au mode séance d'office. Refusée, la couture rend `None` : les vingt-sept
  routes répondent déjà 401 sur un code inconnu, il n'y a rien à ajouter chez
  elles.
- **Identifiants négatifs.** Les participants partagent `progress.json`,
  `direct.json` et la colonne `student_id` de la base avec les vrais élèves. Il
  faut donc un entier, et il faut qu'aucun ne tombe sur celui d'un élève : les
  élèves comptent vers le haut depuis 1, les participants vers le bas depuis -1.
- **Un seul module.** `activite_de_la_seance()` borne le participant au module
  de sa séance ; sans elle, un code photocopié ouvre tout le catalogue du
  groupe. Posée sur `/api/student/sections`, `/api/student/progress` et
  `/api/student/access` — les trois routes ouvertes qui portent un `activityId`.
- **Le code de séance évite les codes d'élèves.** `validate_student_code`
  regarde les élèves d'abord : un code de séance tombé sur celui d'un élève
  ferait entrer toute une classe dans son dossier, sans que rien ne le signale.
- **Fermer ferme.** `participant_par_jeton` vérifie que la séance est encore
  ouverte, et pas seulement l'entrée. Le contrôle du 29 août 2026 a pris le
  premier jet en défaut : fermer n'empêchait que les entrées neuves, et tous les
  appareils déjà entrés continuaient — c'est-à-dire exactement ceux d'un code
  qui a circulé.
- **Ce qui est refusé, et pourquoi.** `/api/oral/submit` : la voix est la donnée
  la plus identifiante du portail, et le mode tire sa force de ne rien
  collecter — l'élève s'enregistre et s'écoute, rien ne part. Le vocabulaire :
  la répétition espacée suppose un lendemain. Le catalogue et le tableau de
  bord : ils appartiennent à l'élève inscrit, une séance ouvre un module.
- **Le jeton ne s'écrit nulle part.** Il authentifie ; l'inscrire dans un dépôt
  reviendrait à écrire un mot de passe. Le dépôt écrit porte `studentLabel`
  (« Participant 7 ») et un `seanceId`, jamais le jeton.

**L'entrée de l'élève.** L'adresse imprimée est `/s/KRB482` : le `do_GET` la
reconnaît avant tout le reste et redirige vers `seance.html?c=KRB482`. Elle ne
porte **aucun nom de domaine** — le code QR et la ligne imprimée se fabriquent
à partir de l'en-tête `Host`, pour qu'un domaine acheté plus tard n'oblige à
toucher à rien.

- `POST /api/seance/entrer` fait les deux gestes : entrer, et **revenir**.
  L'appareil garde son jeton dans `localStorage`, **rangé par code de séance** ;
  s'il le renvoie avec le bon code, il retrouve le même participant. Une seule
  route pour les deux, sinon un rechargement mal branché crée un Participant 8
  à chaque F5 et le tableau de la classe se remplit de fantômes.
- Le chemin du fichier à ouvrir est calculé **par le serveur**
  (`fichier_de_seance`), dans le même ordre de préférence que `fichierDe()` du
  portail élève. Attention : les chemins sont **à plat** dans l'enregistrement
  (`a["interactive"]`) ; le `files` groupé n'existe que dans la réponse de
  l'API. Lire `files` côté serveur rend une chaîne vide sans rien dire.
- `viewer.html` accepte un paramètre `retour` (borné à un `*.html` du site) :
  un participant n'a pas de portail où revenir, et le renvoyer sur `eleve.html`
  le poserait devant un écran de connexion qui ne le concerne pas. Quand
  `retour` est là, le viewer **navigue** au lieu de fermer l'onglet — une
  séance s'ouvre dans le même onglet, et le fermer emporterait tout.

Contrôles : `python3 build/controles/seances.py` (les gardes, fonction par
fonction) et `python3 build/controles/seances_http.py` (les routes, jouées par
HTTP sur un serveur jetable). Le second est celui qui compte : il vérifie que
les refus **refusent**, ce qu'un test qui se contente d'entrer dans une séance
laisserait passer même toutes gardes retirées.

Plan du chantier : `assets/presentations/mode-seance-sans-compte.html`.
Reste à faire : la feuille imprimable avec le code QR (et le bouton « Ouvrir
une séance » dans `enseignant.html`), puis le tableau de la classe.

## Voix des modules (ElevenLabs)

Les MP3 des modules sont produits par les scripts `generer_audio_*.py` à la
racine : `<module>.py` pour les dialogues (une voix par personnage),
`<module>_sons.py` pour les mots isolés, `<module>_plus.py` pour les
mini-leçons. Les identifiants de voix sont volontairement les mêmes d'un
module à l'autre, pour qu'un personnage sonne pareil partout.

- **Un générateur se copie sur son voisin, et un nom de fichier à moitié
  substitué ne lève aucune erreur.** Découvert le 23 août 2026 en produisant
  `module-n8-actualite` : la ligne `MANIFESTE` de
  `generer_audio_module_n8_recherche.py` portait `sons_module_n7_recherche.json`
  — le relevé d'un **autre module**. Le fichier existe, donc rien n'aurait
  protesté : le générateur aurait produit les 221 extraits du niveau 7 au lieu
  des 334 du sien, 9 clés en commun sur 334, et un module troué dont personne
  n'aurait su pourquoi. Le contrôle, à passer après avoir copié un générateur
  et avant de le lancer : le **charger sans appeler `main()`** et lui faire dire
  ce qu'il a trouvé — ses dialogues et leur nombre de répliques, les
  personnages sans voix, le nom de son manifeste et son nombre de sons. Vingt
  lignes, aucun appel réseau, aucun caractère facturé.
- **Il n'y a que quatre voix, et ça se compte AVANT d'écrire les dialogues.**
  Deux féminines (`enseignante`, `feminin_2`), deux masculines (`masculin_1`,
  `narrateur`). Deux personnages ne peuvent en partager une que s'ils ne se
  répondent **jamais** dans un même extrait — sinon l'élève entend la même
  voix se répondre à elle-même. Un dialogue à trois personnages du même genre
  est donc impossible, et c'est une contrainte d'écriture, pas de production.
  Découvert le 23 août 2026 en produisant `module-n7-publicite` : un extrait
  réunissait une mère, sa fille de onze ans et une agente de l'Office de la
  protection du consommateur. L'agente est devenue un agent. Compter les
  locuteurs par extrait est gratuit avant ; après, c'est une réécriture.
- **Une voix se choisit aussi contre le ralentissement.** L'annonceur des
  capsules publicitaires du même module prend `narrateur`, qui n'est pas
  ralentie : la vitesse de la mention légale **est** l'objet de l'exercice, et
  la poser sur la voix « enseignante » l'aurait effacée.
- **Il n'y a que quatre voix, et ça se compte AVANT d'écrire les dialogues.**
  Deux féminines (`enseignante`, `feminin_2`), deux masculines (`masculin_1`,
  `narrateur`). Deux personnages ne peuvent en partager une que s'ils ne se
  répondent **jamais** dans un même extrait — sinon l'élève entend la même
  voix se répondre à elle-même. Un dialogue à trois personnages du même genre
  est donc impossible, et c'est une contrainte d'écriture, pas de production.
- **La voix « enseignante » a changé le 23 août 2026.** L'ancienne
  (`K7gx0ylJdff0yjM2uVQS`) est **abandonnée, ne pas y revenir** : mesurée sur
  une même phrase contre les trois autres, elle sortait à 20,8 caractères par
  seconde quand les autres tenaient 18 à 19 — la plus rapide des quatre, et
  ralentie à 0,85 elle restait au niveau des autres non ralenties. La
  remplaçante est **`mActWQg9kibLro6Z2ouY`**, qui débite 17,7 c/s sans
  traitement, soit ce que l'ancienne donnait *après* `atempo`.
- **Un changement de voix peut régler des prononciations, pas seulement un
  débit.** Le 23 août 2026, deux défauts traînaient : les six lettres de
  l'exercice d'épellation du niveau 1 (`prAlpha`, qui fait distinguer E/I,
  G/J, M/N) sortaient à l'anglaise, et « brin » — dont tout l'exercice de
  graphie-phonie de `module-achat` est de l'opposer à « brun ». La nouvelle
  voix les dit **justes telles quelles** : cinq lettres sur six et « brin »
  n'ont eu besoin d'aucune substitution. Seul « I » résiste, en sortant
  « ir », et `TEXT_OVERRIDES` lui envoie **`i.`** — le point empêche le
  modèle de fermer la syllabe sur une consonne. Neuf graphies essayées avant
  celle-là. La leçon : avant d'écrire une table de substitution, réécouter
  avec la voix en service — une substitution inutile est une occasion de
  diverger, et elle ne se voit plus jamais.
- **La voix « enseignante » est ralentie à 0,85**, ce qui la met à 15,1 c/s.
  C'est la voix que l'élève entend le plus — elle narre les mini-leçons et
  les mots isolés de presque tous les modules, en plus de rôles de dialogue
  (la commis du module 5, madame Rioux du module 10, la conseillère…).
- **Changer de voix oblige à effacer ce qu'elle a produit.** Les générateurs
  sautent ce qui est sur le disque : sans effacement, la nouvelle voix ne
  serait jamais produite. `python3 build/retirer_voix.py` compte,
  `--effacer` retire — et seulement ce que le rôle nommé a produit (le
  dossier `sons/` quand `VOIX_MOTS` le porte, et les `line_NN_<perso>.mp3`
  des personnages qui l'ont). Tout effacer ferait repayer les milliers
  d'extraits des trois autres voix, qui n'ont pas bougé : 5 556 contre 8 538
  au changement du 23 août.
- **Le débit se mesure, il ne se devine pas** : `python3
  build/essai_debit.py [identifiant]` fait dire la même phrase aux quatre
  voix, plus une candidate, à trois vitesses, et imprime les caractères par
  seconde. Comparer deux voix sur deux textes différents ne veut rien dire.
- **Le paramètre `speed` d'ElevenLabs ne sert à rien ici** : avec
  `eleven_multilingual_v2`, l'API renvoie le *même fichier octet pour octet*
  avec ou sans `"speed": 0.85`. Vérifié, pas supposé. Le ralentissement se
  fait donc après coup, avec `atempo` de ffmpeg, qui étire la durée sans
  toucher à la hauteur : même timbre, débit posé.
- **`voix_lente.py` tient cette règle.** Chaque générateur appelle
  `ralentir_si_enseignante(chemin, voix)` juste après avoir écrit son MP3 :
  les autres voix passent intactes. Changer le débit se fait à un seul
  endroit — `FACTEUR` — puis en repassant les fichiers déjà produits.
- **Les MP3 modifiés à la main ne survivent pas à une régénération.** Si un
  fichier doit sonner autrement, c'est le script qui change, jamais le MP3.
- **Toucher aux MP3 oblige à incrémenter `AUDIO_V`** dans le HTML du module :
  les fichiers audio sont servis sans `Cache-Control`, et sans ce numéro le
  navigateur d'un élève resservirait l'ancienne voix. Pour `module-probleme`,
  le HTML est généré : le numéro se change dans le gabarit
  (`module-consultation`), puis `python3 build/module.py module-probleme`.

## Langue

Répondre en français à l'utilisateur.
