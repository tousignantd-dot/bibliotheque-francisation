# Bibliothèque Francisation

Bibliothèque d'activités pédagogiques FLS (Niveau 4) pour enseignant en francisation au Québec. Serveur Python simple (`server.py`, stdlib seulement) + fichiers statiques HTML.

## Déploiement (Railway)

- Push sur `main` → redéploiement automatique sur Railway
  (https://bibliotheque-francisation-production.up.railway.app)
- **Python épinglé à 3.12** via `.python-version` — le module `cgi` utilisé par server.py a été supprimé en Python 3.13. Ne pas retirer ce fichier.
- Builder : Railpack (`railway.toml`) — ne pas remettre Nixpacks (buggé).
- Healthcheck : `/api/activities`. `init_storage()` tourne en arrière-plan au démarrage pour ne pas bloquer le healthcheck.

## Flux de travail important

- Quand l'utilisateur ajoute des fichiers via **admin.html en local**, ils arrivent dans le working tree mais ne sont PAS en ligne tant qu'on n'a pas fait `git add + commit + push`. « Mettre en ligne » = pousser sur main.
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
`build/module-probleme/build.py`, jamais à la main.

## Cours et ateliers

Chaque activité porte une `categorie` : `cours` (modules de 4 h, le matin) ou
`atelier` (activités de 2 h, l'après-midi). Les listes enseignantes
(`admin.html`, `index.html`) sont rendues en deux sections dans cet ordre.
Le champ se choisit à la création et dans le modal de modification ; pour une
activité qui ne l'aurait pas, `normalize_categorie()` le déduit du chemin
(`assets/interactive/module-*` → `cours`). Il figure dans `USER_FIELDS`, donc le
choix de l'enseignant survit aux redéploiements.
- Authentification enseignante : courriel + mot de passe (PBKDF2-SHA256), jeton
  de session envoyé dans l'en-tête `X-Prof-Token`. `prof.html` porte la
  connexion, l'installation initiale, la gestion des groupes et des comptes.
  `js/prof.js` fournit `Prof.fetch` / `Prof.withGroup` / `Prof.body` aux trois
  pages enseignantes (`admin.html`, `index.html`, `lms.html`) — toute requête
  d'administration doit passer par là, sinon elle répond 401.
- Rôles : `admin` (crée les autres enseignants, voit tous les groupes) et `prof`.
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
- `prof.html` — installation du premier compte, groupes et comptes (ancienne page)
- `admin.html` / `eleve.html` — catalogue (téléversement) / interface élève

## Portail enseignant (`enseignant.html`)

- Refait selon la remise `~/Downloads/design_handoff_portail_enseignant`, qui
  est la **source de vérité visuelle** de cette page. Trois onglets dans une
  seule page : Planifier · Élèves · Groupes et comptes, plus son propre écran
  de connexion. Il **remplace l'usage courant** de `lms.html` et de la partie
  « groupes » de `prof.html` ; `admin.html` reste la page du catalogue
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
- **Planifier des sections d'un module sans date ouvre le module** à la
  première d'entre elles (`modulesAOuvrir()`). Sans cela, la classe ne verrait
  rien : un module fermé cache toutes ses sections, datées ou non.

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
  fichier à son activité. À plat, le `A1` du prochain module écraserait celui du
  module 9. La constante `MODULE` de `build/powerpoints/build.py` fixe le
  dossier de sortie.
- **`data/materiel.json` est produit, jamais écrit à la main**
  (`python3 build/materiel.py`). C'est le relevé de ce qui existe sur le
  disque : une entrée non vérifiée serait un lien mort. `--verifier` compare
  sans écrire. Il ne recopie **aucun** titre d'activité : il ne connaît que des
  `activiteId` — les **entiers** de `activities.json`, pas des slugs.
- La grille des séances a une source unique : `SEANCES` de
  `build/powerpoints/build.py`. Un module sans dossier de production est mesuré
  contre la grille standard à seize (4-4-4-2-2), ce qui permet d'afficher
  « 0 séance sur 16 » au lieu de le taire.
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

- Six outils permanents dans chaque module : traduire · lire · simplifier ·
  prononcer · demander à l'assistant · mon carnet. Code partagé dans
  `assets/design-system/outils-eleve.{js,css}` — ne rien y écrire qui dépende
  d'un module précis.
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
- Trois partis pris à ne pas défaire : la traduction s'ajoute **sous** le
  français et ne le remplace jamais (pas de « traduire toute la page ») ;
  « simplifier » reformule **en français** ; l'assistant **ne donne jamais la
  réponse d'un exercice**, il cite la phrase du dialogue et repose une
  question plus facile.
- Icônes : les six tracés SVG du système de design (grille 24, trait 2,2,
  bouts ronds). **Aucun émoji, aucun jeu d'icônes tierce partie.** Rouge
  réservé à « Lire » ; sélectionné = plaque encre `#17181A`.
- `server.py` lit `.env` au démarrage (les variables déjà définies gagnent) :
  sans ça, rien n'est testable en local. En production les clés viennent des
  Variables Railway — **et un changement de variable n'atteint le serveur
  qu'au redéploiement**, sinon l'ancienne valeur reste en mémoire.

## Langue

Répondre en français à l'utilisateur.
