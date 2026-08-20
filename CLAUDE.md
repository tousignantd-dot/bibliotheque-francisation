# Bibliothèque Francisation

Bibliothèque d'activités pédagogiques FLS (Niveau 4) pour enseignant en francisation au Québec. Serveur Python simple (`server.py`, stdlib seulement) + fichiers statiques HTML.

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
- **Les cinq greffes partagées** — barre d'outils, dépôt de l'écrit, verrou
  des sections, reprise de séance, identité de marque — commencent chacune par
  retirer celle du gabarit, qui porte le slug (ou le numéro d'activité) de la
  consultation. Sans ce dégreffage, un module hériterait du carnet d'un autre.
- La consigne de correction de la production **écrite** ne vit pas dans le
  gabarit : `build/greffe_depot_ecrit.py` la pose. L'ancien script croyait la
  remplacer et son `replace` était sans effet — code mort découvert en
  généralisant.

## L'identité de marque SAAF

La plateforme s'appelle **SAAF** — Système d'aide à l'apprentissage du
français. Le logotype est la **pilule à contour violet** (variante « 5c ») :
contour de 3 px `#6B4FBB`, fond blanc, « SAAF » en Nunito 900, descripteur **à
droite** du contour et séparé par un filet vertical. Il est purement
typographique — aucun fichier image, tout se construit en markup et en CSS — et
**statique** : aucun survol, aucune animation.

- `assets/design-system/marque-saaf.css` — les jetons et les classes du
  verrouillage et du monogramme. Les jetons s'appellent `--marque-600` et
  `--marque-100`, **pas** `--violet-600` : le système de design emploie déjà ce
  dernier nom comme couleur de repérage de la section « Les sons ». Deux noms,
  une seule valeur, pour que la marque ne dépende pas d'un jeton de repérage.
- `assets/design-system/marque-saaf-favicon.svg` — le monogramme « à », aplat
  violet, pastille ronde. Sous 44 px, la règle est l'aplat et non le contour.
- `build/greffe_marque.py` — pose le verrouillage en première ligne de `#hdr`,
  au-dessus du sur-titre du module. Idempotente, comme les autres greffes :

```
python3 build/greffe_marque.py            # tous les modules écrits à la main
python3 build/greffe_marque.py meteo pub  # seulement ceux-là
python3 build/greffe_marque.py --retirer  # dégreffe tout
```

Les modules qui ont un manifeste dans `build/contenu/` sont sautés : leur
greffe est posée par `build/module.py` pendant la construction. Le script lit
le dossier plutôt que d'en tenir une liste, qui vieillirait.

**Le violet est réservé à la marque** : il ne va sur aucun bouton, aucun état,
aucune rétroaction. L'action reste le vert `--accent`, l'audio reste le rouge
`--audio`, et le bandeau d'en-tête reste clair — jamais noir.

Dans le portail, la marque ne passe pas par une greffe : ces pages sont écrites
à la main et ne se régénèrent pas. Chacune lie `marque-saaf.css` et pose le
verrouillage **une fois**, dans son en-tête principal — jamais dans les
bandeaux de sous-vue, qui ne sont pas des en-têtes de page.

| Page | Verrouillage |
|---|---|
| `eleve.html` | grand (64 px) sur l'écran de connexion — c'est le `h1` ; réduit (44 px) sur l'accueil |
| `enseignant.html`, `prof.html` | grand sur la connexion, réduit dans l'en-tête permanent |
| `progression.html`, `fiche-eleve.html` | réduit, dans le bandeau d'identité — pas dans la barre collante |
| `catalogue.html` | de barre : pilule · filet · `.header-brand`, la disposition de l'en-tête de module |
| `presentations.html` | grand ; sa copie locale du logotype a été retirée au profit de la feuille partagée |

`lms.html` et `viewer.html` sont restés à l'écart : ils ne parlent pas le
système de design Francisation (Inter, accent bleu, chrome foncé pour le
lecteur). Y poser la pilule mettrait la marque sur une page qui la contredit ;
c'est une refonte, pas une greffe.

Le mot-symbole étiré de `eleve.html` (`letter-spacing: .06em`) a disparu : la
remise interdit l'interlettrage positif sur le nom.

Un écart assumé : le filet du verrouillage est `--violet-100` dans la remise,
sur fond blanc. Or ici le verrouillage vit toujours sur un bandeau teinté — un
en-tête de module porte sa couleur de repérage, ceux du portail la teinte acier
— où cette valeur s'efface au point de disparaître. `--marque-filet` vaut donc
`#C3B4EA` par défaut ; sur un fond blanc, le rendre à `--marque-100`.

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
`--marque-600` / `--marque-100`, dans `marque-saaf.css`. Le changement a touché
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

## Voix des modules (ElevenLabs)

Les MP3 des modules sont produits par les scripts `generer_audio_*.py` à la
racine : `<module>.py` pour les dialogues (une voix par personnage),
`<module>_sons.py` pour les mots isolés, `<module>_plus.py` pour les
mini-leçons. Les identifiants de voix sont volontairement les mêmes d'un
module à l'autre, pour qu'un personnage sonne pareil partout.

- **La voix « enseignante » (`K7gx0ylJdff0yjM2uVQS`) est ralentie à 0,85.**
  C'est la voix que l'élève entend le plus — elle narre les mini-leçons et
  les mots isolés de presque tous les modules, en plus de rôles de dialogue
  (la commis du module 5, madame Rioux du module 10, la conseillère…) — et
  elle débitait 18,6 caractères par seconde, trop vite pour du niveau 4.
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
