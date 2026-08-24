# Deux agents en parallèle — consignes

Ce fichier existe parce que quatre sessions ont travaillé dans ce dépôt le
20 août 2026 et que trois d'entre elles se sont nui sans le vouloir. Il dit ce
qu'il faut faire pour que deux agents produisent deux modules en même temps
sans se marcher dessus.

Il sert de deux façons : le **protocole** vaut pour n'importe quelle paire
d'agents, et la **répartition** en fin de fichier est celle du moment. Quand
la paire change, on réécrit la répartition, pas le protocole.


## La répartition en cours

**Les activités 124 à 145 sont réservées** — la banque du niveau 1,
produite le 24 août 2026. Ce ne sont **pas des modules** : aucune entrée dans
`build/powerpoints/modules.py`, aucune séance, aucune fiche. Elles touchent
`data/activities.json` une seule fois, à la livraison.

| Numéros | Famille | Générateur |
|---|---|---|
| 124 | A · apparier — livré | `build/appariement.py` |
| 125-129 | A · apparier | `build/appariement.py` |
| 130-135 | C · construire une phrase | `build/phrase.py` |
| 136-139 | D · écrire et copier | `build/graphie.py` |
| 140-145 | B · discriminer à l'oreille | `build/oreille.py` |

Le plan complet est dans `docs/plan-exercices-niveau-1.md`. Si une autre
session a besoin d'un numéro pendant ce chantier, **prendre à partir de 146**.

Les activités 60 à 64 sont livrées ; la file des modules reprend à **65**,
consigne prête dans `docs/consignes-a-coller.md`. Le journal des vagues est
dans `docs/vagues-suivantes.md`.

**Les numéros d'activité sont réservés d'avance, et c'est le point le plus
important de ce fichier.** Le numéro d'activité est la clé qui relie
`build/powerpoints/modules.py`, `data/activities.json` et le portail. Deux
agents qui prennent « le prochain numéro libre » à dix minutes d'intervalle
prennent le même.

Le format long, seize séances, se prend dans `build/powerpoints/modules.py` :
`GRILLE_3_DEFIS` (quatre séances par bloc, trois défis) ou `GRILLE_2_DEFIS`
(deux défis plus longs). `GRILLE_COURTE` est réservée aux niveaux 1 et 2.


## Les cinq règles

**1. `git add` avec des chemins explicites. Jamais `git add -A`, jamais
`git add .`.**

C'est la règle qui compte le plus. Le 19 août, trois commits d'affilée ont
emporté le travail non commité d'une autre session sous un message sans
rapport — 271 lignes de `forge.py` ont failli être perdues. Un `git status`
qui montre des fichiers que tu n'as pas écrits n'est pas une anomalie à
nettoyer : c'est le travail de quelqu'un d'autre.

**Et `git commit` prend des chemins, lui aussi : `git commit -- <chemins>`.**
Ajouté le 21 août 2026, en produisant le niveau 5. La règle ne parlait que de
`git add`, ce qui ne suffit pas : les deux sessions partagent **le même index**,
et un `git commit` nu emporte tout ce qui s'y trouve — y compris ce que l'autre
session vient d'y mettre et n'a pas encore commité. Pendant cette production,
les huit fichiers du niveau 6 se sont trouvés *staged* au moment précis d'un
commit du niveau 5. Répéter les chemins après `--` est la seule façon de s'en
tenir aux siens, et `git show --name-only --format="" HEAD` le vérifie en une
ligne.

**Vu de l'autre côté, le 21 août 2026, en produisant le niveau 5 · services.**
La règle est écrite du point de vue de celui qui commet la faute ; voici ce que
ça fait quand on la subit. Un `git add` avait échoué sur un chemin de
`.gitignore`, laissant quatre-vingt-douze fichiers *staged* sans commit. Dans
l'intervalle, une autre session a fait son `git commit` — et les
quatre-vingt-douze sont partis dans le sien, sous un message qui parlait
d'extraits audio. **Rien n'a été perdu**, et il n'y a rien à réparer : les
fichiers sont suivis, poussés, servis. Mais l'historique ment, et on ne
réécrit pas l'historique d'une branche partagée pour si peu.

Deux conséquences pratiques, à ajouter à la règle 1 :

- **ne jamais laisser l'index habité entre un `add` et un `commit`.** Si le
  `commit` échoue, il faut recommencer tout de suite, pas plus tard ;
- **`git add` échoue en entier sur un seul mauvais chemin.** Un dossier ignoré
  dans la liste (`build/powerpoints/_captures`, par exemple) et rien n'est
  ajouté — sans que ce soit une erreur fatale visible dans un enchaînement.
  D'où l'intérêt de `--pathspec-from-file`, qui prend la liste dans un fichier
  et se relit.

Et un piège de shell, qui a coûté deux tentatives : **le shell de cet outil est
zsh, où `$VARIABLE` ne se découpe pas en mots.** `git add $CHEMINS` passe donc
la liste entière comme un seul chemin et échoue avec un message de cent lignes.
`${=CHEMINS}` en zsh, ou `--pathspec-from-file`, qui est plus lisible.

**Le même piège fait mentir les six contrôles.** Ajouté le 21 août 2026, en
produisant l'activité 77. Les enchaîner dans une boucle — `for c in
"build/sections.py --verifier" … ; python3 $c` — les fait tous échouer d'un
coup : zsh passe la ligne entière comme un seul nom de fichier. Six « ÉCART »
alignés, et pas un seul écart réel. `python3 ${=c}`, et les six repassent.

**2. Commiter et pousser souvent, par petites tranches.**

Ce qui traîne non commité est ce qui se fait ramasser. Un module se pousse
très bien en quatre ou cinq commits : le contenu, les médias, les séances, la
livraison. N'attends pas d'avoir tout fini.

**3. `git pull` juste avant de toucher un fichier partagé.**

La liste est plus bas. Ce sont les seuls endroits où deux agents peuvent
vraiment entrer en collision, et ils sont peu nombreux.

**4. Ce qui doit survivre s'écrit dans le dépôt, pas dans un message.**

Une session meurt et emporte tout ce qu'elle savait. Le 20 août, une session a
travaillé toute sa durée en s'interdisant `build/gabarit.py` pour protéger une
greffe qui n'avait jamais été en danger ; elle est morte avant que la
correction ne lui parvienne. Une décision, une contrainte, un piège découvert :
ça va dans `CLAUDE.md` ou dans `docs/`. Un message à une session sœur ne sert
qu'à la prévenir qu'un fichier vient de changer.

**5. Les changements transversaux se font quand personne d'autre n'écrit.**

Refonte du gabarit, du moteur, du système de design, d'une règle de couleur :
ces changements touchent tous les modules à la fois. Le 20 août, la règle
« la couleur d'un module est celle de son niveau » a modifié 141 fichiers en
une fois. Si quelqu'un avait été au milieu d'un module, le conflit aurait été
pénible. Préviens et attends.


## Les fichiers partagés

Tout le reste est à toi seul. Le contenu d'un module est isolé — c'est ce qui
rend la parallélisation possible :

    build/contenu/<slug>/            à toi
    assets/interactive/<slug>/       à toi
    build/powerpoints/decks/<slug>/  à toi
    assets/powerpoints/<slug>/       à toi
    generer_audio_<slug>.py          à toi
    sons_<slug>.json                 à toi

Les fichiers ci-dessous sont **partagés**. Fais `git pull` juste avant, écris,
commite et pousse tout de suite — ne les garde pas ouverts une demi-journée.

| Fichier | Quand tu y touches | Risque |
|---|---|---|
| `build/powerpoints/modules.py` | une fois, pour inscrire ton module | deux entrées ajoutées au même endroit |
| `data/activities.json` | une fois, pour inscrire ton activité | idem, et le numéro d'activité |
| `data/sections.json` | à la livraison, via `python3 build/sections.py` | le script réécrit tout le fichier |
| `data/materiel.json` | à la livraison, via `python3 build/materiel.py` | idem |
| `server.py` | si ton module a besoin d'un scénario de jeu de rôle | deux ajouts dans le même dictionnaire |
| `CLAUDE.md`, `docs/` | quand tu documentes une décision | à écrire, jamais à réécrire |

Les deux scripts `sections.py` et `materiel.py` **régénèrent le fichier
entier** à partir du disque. Si tu le lances alors que l'autre agent vient de
publier son module, tu inscris son module aussi — c'est sans danger, c'est même
souhaitable, mais dis-le dans ton message de commit pour que la ligne
supplémentaire ne surprenne pas.


## Un mot sur `server.py`

Le niveau 6 « Recherche d'emploi » n'a **pas** de scénario de jeu de rôle : les
douze scénarios existants sont `louer`, `probleme`, `relations`, `chemin`,
`activite`, `epicerie`, `appareil`, `restaurant`, `presenter`, `allees`,
`vetement`, `autobus`. Tu devras en ajouter un.

Trois pièges appris en le faisant :

- Un module se construit **sans erreur** même si son `jr_scenario` n'existe pas
  dans `server.py`. Rien ne le vérifie. Le jeu de rôle échoue seulement à
  l'exécution, chez l'élève. Vérifie que la clé existe.
- **Pire que la clé absente : la clé en double.** Découvert le 23 août 2026 en
  produisant `module-n7-oeuvres` (116), dont le scénario devait s'appeler
  `oeuvres` — nom déjà pris par `module-n5-oeuvres` (73), avec une constante
  `JEU_DE_ROLE_OEUVRES` du même nom. Deux clés identiques dans un littéral de
  dictionnaire Python ne provoquent **rien** : la dernière gagne, en silence, et
  la constante aussi. Le module aurait joué le scénario du niveau 5, avec des
  rôles qui ne sont pas les siens. Le contrôle, à passer après tout ajout :

      python3 - <<'PY'
      import importlib.util, os, re
      os.environ.setdefault('STORAGE_DIR', '/tmp/verif')
      spec = importlib.util.spec_from_file_location("srv", "server.py")
      m = importlib.util.module_from_spec(spec)
      try: spec.loader.exec_module(m)
      except SystemExit: pass
      man = open('build/contenu/<slug>/manifest.py', encoding='utf-8').read()
      sid  = re.search(r"'jr_scenario':\s*'([^']+)'", man).group(1)
      role = re.search(r"'jr_role':\s*'([^']+)'", man).group(1)
      s = m.JEU_DE_ROLE_SCENARIOS[sid]
      print(sid, list(s['roles']), role in s['roles'])
      PY

  S'il rend des rôles que tu n'as pas écrits, ta clé est en collision :
  renomme-la (`avisoeuvre` plutôt que `oeuvres`) **et** renomme ta constante.
- Ne réutilise pas un scénario d'un autre niveau parce que le sujet ressemble.
  Ils portent leur niveau dans leur conduite : le scénario `chemin` du niveau 4
  donne six étapes et des noms de terminus, ce qui est ingérable au niveau 2. Un
  scénario, c'est un dictionnaire de cas et une entrée dans
  `JEU_DE_ROLE_SCENARIOS` — une trentaine de lignes.

Concrètement : `git pull`, ajoute ton dictionnaire de cas **juste avant**
`JEU_DE_ROLE_SCENARIOS`, ajoute ton entrée **en tête** du dictionnaire, commite,
pousse. Deux agents qui font ça chacun de leur côté fusionnent proprement.

Le niveau 5 « Location d'un logement » réutilisera le scénario `louer`, qui
existe déjà. La session A ne devrait donc pas toucher `server.py`, mais fais
quand même ton `git pull`.


## La méthode

Elle est écrite et elle ne s'invente pas : **la skill `module-neuf`**, avec ses
six références (`1-cadrer` … `6-livraison`). Suis-la. Elle couvre le cadrage
par le programme, l'invention du scénario, les sept fichiers de contenu, la
construction, les médias et la livraison.

Trois rappels qui viennent des modules livrés cette semaine :

- **Rien ne se copie du manuel SOFAD.** Le manuel est un modèle de structure et
  de progression grammaticale, jamais une source de texte. Le scénario, les
  personnages, les dialogues et les exercices s'inventent.
- **Un module neuf n'a aucune couleur à choisir.** La couleur de l'en-tête est
  celle de son niveau — le 6 est acier `#1D6B8F` / `#E7F0F6`. Il suffit de
  donner le niveau au registre : `build/couleurs_niveau.py` pose le reste. Et
  `sections.js` ne doit contenir ni `#166534` ni `#0F766E` : le vert est sorti
  du repérage.
- **La reprise réseau du générateur audio.** ElevenLabs coupe par
  intermittence, plusieurs fois par jour en ce moment. Copie la fonction
  `parle()` de `generer_audio_module_n2_autobus.py`, qui réessaie cinq fois en
  doublant l'attente et traite les 429 et les 5xx. Un échec réseau ne veut pas
  dire que l'extrait est en cause : relancer plus tard suffit, et le script est
  relançable — il saute ce qui existe déjà.


## Avant de publier

Les six contrôles sont réunis dans `CLAUDE.md`, section « Les contrôles avant
de publier un module ». C'est là qu'ils vivent, et c'est là qu'il faut les
relire : ils sortent tous en code 1 sur écart, donc ils s'enchaînent. Les
quatre premiers portent sur le module interactif, les deux derniers sur les
séances — un module n'est pas publié sans ses présentations et ses fiches.

Le déploiement se fait **sur `git push`** — Railway s'en charge, ne lance
jamais `railway up`. Compte quelques minutes avant que les médias neufs soient
servis, et vérifie en production plutôt qu'en local : une synchronisation de
volume s'est déjà arrêtée en cours de route et un module entier répondait 404.


## Ce qui a réellement mal tourné, le 20 août 2026

À lire une fois. Ce sont les quatre incidents qui ont produit les cinq règles.

1. **Trois commits ont emporté le travail d'une autre session** sous des
   messages sans rapport. Cause unique : `git add -A`.
2. **Une session s'est bridée pour rien** pendant toute sa durée, en
   s'interdisant `build/gabarit.py` au nom d'une contrainte qui n'existait pas.
3. **Une information périmée a circulé** d'une session à l'autre : un défaut
   déjà corrigé la veille a été signalé comme à corriger, parce que l'arbre
   local de l'émetteur n'était pas à jour. `git pull` avant de diagnostiquer.
4. **La session concernée est morte** avant de recevoir la correction. Ce qui
   se dit entre agents ne survit pas ; ce qui est écrit dans le dépôt, oui.

À quatre, la coordination a coûté plus de messages que de code. À deux, avec
ces règles, deux modules par jour sont un objectif raisonnable.


## Le bac à sable réseau bloque ElevenLabs (21 août 2026)

Découvert en produisant `module-n5-emmenagement`. Les appels à
`api.elevenlabs.io` échouent tous en `SSLError` / « EOF occurred in violation
of protocol », y compris avec `curl`, et **quel que soit le nombre de
reprises** : la fonction `parle()` épuise ses cinq essais et rend
« ❌ réseau après 5 essais ».

Ce n'est pas une panne d'ElevenLabs, ce n'est pas la clé, et rien ne sert
d'attendre. C'est le bac à sable réseau de l'outil Bash, qui laisse passer
`fal.run` (les images) mais pas `api.elevenlabs.io`. Le générateur audio se
lance donc avec `dangerouslyDisableSandbox: true` :

    nohup python3 generer_audio_<slug>.py > /private/tmp/audio_<slug>.log 2>&1 &

Le test d'une ligne, pour ne pas diagnostiquer à l'aveugle :

    curl -s -o /dev/null -w "%{http_code}\n" https://api.elevenlabs.io/v1/models

`000` dans le bac à sable, `404` en dehors — le 404 signifie que la connexion
s'établit, ce qui est tout ce qu'on veut savoir.

**Précision du 21 août, en produisant `module-n8-emploi` : ce n'est pas
seulement le bac à sable.** Vers 00 h 25, `api.elevenlabs.io` a cessé de
répondre **aussi avec `dangerouslyDisableSandbox`**, après que neuf MP3 du
module de niveau 8 soient passés normalement. Le diagnostic en deux lignes :

    host api.elevenlabs.io          # résout : 31.169.123.224
    curl -sv https://api.elevenlabs.io/v1/models

La connexion TCP s'établit (« Connected … port 443 »), puis la poignée de main
TLS est coupée juste après le *Client hello* (`SSL_ERROR_SYSCALL`). Ce n'est
donc ni la clé, ni le bac à sable, ni ElevenLabs qui refuse la requête : c'est
la liaison qui est coupée en route. `fal.run` continue de répondre pendant ce
temps, ce qui rend le diagnostic trompeur.

**Ce qu'il faut en faire.** Ne pas laisser `parle()` brûler soixante secondes
par extrait dans le vide : arrêter le générateur, et le relancer plus tard —
il est relançable et saute ce qui existe déjà. Un module se livre très bien
avec son audio en attente, à condition de l'écrire dans le journal ; il ne se
livre pas avec un HTML modifié à la main pour masquer les boutons d'écoute.

