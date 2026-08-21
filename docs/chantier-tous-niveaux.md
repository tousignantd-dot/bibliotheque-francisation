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
| 1 | Relations sociales | `module-n1-presenter` | 8 séances | 4 intentions sur 9 ; se présenter est le premier besoin de tous |
| 2 | Déplacement dans une ville | `module-n2-autobus` | 8 séances | 4 intentions ; concret, visuel, immédiatement utile |
| 3 | Achat d'aliments ou de produits d'entretien | `module-n3-epicerie` | 16 séances | 8 intentions, la plus riche du niveau |
| 5 | Location d'un logement | `module-n5-logement` | 16 séances | 4 intentions ; la démarche la plus lourde d'une installation |
| 6 | Recherche d'emploi | `module-n6-emploi` | 16 séances | 4 intentions ; le tournant du stade intermédiaire |
| 7 | Suivi de l'actualité | `module-n7-actualite` | 16 séances | 6 intentions ; compréhension de discours longs |
| 8 | Emploi | `module-n8-emploi` | 16 séances | 10 intentions, de loin la plus dense du programme |

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

**Fait le 20 août 2026.** `GRILLE_COURTE` (huit séances : a1 a2 a3, b1 b2,
c1 c2, e1) est dans le registre ; `ORDRE` trie par `(niveau, numero)` ;
`build_fiches.py` sait écrire « Huit fiches » et non « 8 fiches ».

**La convention de slug change**, et c'est une décision du chantier : le slug
porte le niveau, `module-n3-epicerie`. Sans lui, le premier module du niveau 1
sur les relations sociales entrerait en collision avec `module-relations` du
niveau 4 — la même situation revient à cinq niveaux dans le programme. Le
préfixe `module-` reste : huit scripts balaient `assets/interactive/module-*`
et le perdre les rendrait aveugles.

## Ce que le programme donne, et ce qu'il faut chercher ailleurs

Le programme donne la spécification complète : intentions, savoirs, lexique,
critères. Il ne donne aucun fait du monde réel. Pour les modules qui reposent
sur une procédure — le bail du niveau 5, l'assurance emploi du niveau 8 — il
faut vérifier les faits québécois (montants, délais, noms d'organismes) plutôt
que les inventer. Ces vérifications se font au coup par coup, sur les sites
officiels, et se notent ici.

## Le format des images, changé pour ce chantier

Les images des exercices étaient carrées. Mesure faite dans le navigateur sur
`module-vetements` : la zone de glisser-déposer (`.imgzone`) fait **223 × 132
px**, soit un rapport de 1,7 — un rectangle paysage. Une image carrée y est
recadrée par `object-fit:cover`, et le tiers du haut et du bas disparaît.

Décision : générer les prochaines images en **3:2 paysage** (1536 × 1024 chez
fal.ai), et aligner le CSS pour ne plus recadrer :

- `.imgtile` (la vignette de la banque) : 100 × 100 → `aspect-ratio:3/2`,
  largeur 150 px ;
- `.vc-photo` (le mot et son image) : `aspect-ratio:1/1` → `3/2` ;
- `.imgzone` : déjà un rectangle, à fixer en `aspect-ratio:3/2` pour que la
  zone vide annonce la forme de ce qu'elle attend.

**Ces trois retouches vivent dans le gabarit**, qu'une autre session est en
train de modifier (l'identité de marque SAAF). Elles se feront quand elle aura
commité — avant la génération d'images du premier module, pas après.

## Le suivi des images sur le mur

Toutes les images produites sont déjà versées dans `~/Claude/generations`, à
plat, avec leur fichier `.json` de traçabilité (prompt, modèle, coût). Le mur
`le-mur.html` les lit par `mur-data.js`, régénéré par `maj-mur.py`. État au
20 août 2026 : 210 médias, 6,94 $ cumulés. **Refaire `python3 maj-mur.py`
après chaque module**, sinon le mur montre l'état précédent.

## Journal

_(une section par module, remplie à mesure)_

## Niveau 3 — `module-n3-epicerie` · À l'épicerie · **livré**

Situation « Achat d'aliments ou de produits d'entretien », huit intentions.
Distinct du module 14 du niveau 4, qui porte sur le comptoir et l'étiquette :
ici, on **trouve** un produit, on **choisit** avec la circulaire, et on
**paie**.

**Scénario.** Marisol, arrivée du Guatemala il y a huit mois, fait ses courses
seule dans une grande épicerie. Elle cherche de la farine de maïs qui n'est pas
avec les farines ; sa voisine Ginette lui montre la circulaire et les mises en
garde des produits d'entretien ; au comptoir, Stéphane lui rembourse un spécial
qui n'était pas passé.

**Six mini-leçons** : treize ou trente · dire où c'est · demander de l'aide ·
les mots qui mesurent · les dessins qui avertissent · lire une facture.

**Médias.** 19 images (0,64 $), **les premières en 3:2**. 204 MP3. Contrôle des
URL : 227 demandées, 227 présentes.

**Défauts trouvés et corrigés.**

- Deux tableaux trop pleins pour une diapositive projetée (A4, C2) : coupés en
  deux. `theme.py` refuse proprement, c'est le bon comportement.
- Un item de type `write` sans `accept` est corrigé **par l'IA** — c'est ce
  qu'il fallait pour « Ma fiche », dont les réponses sont libres. Les `accept`
  y avaient été mis par réflexe et auraient rendu l'exercice impossible.
- La caissière est devenue **un caissier** : la banque ElevenLabs ne compte que
  deux voix féminines, déjà prises par Marisol et Ginette.

## Niveau 1 — `module-n1-presenter` · Je me présente · **livré**

Premier module **court** du projet : huit séances, deux défis, cinq sections au
lieu de six. Le moteur ne bronche pas — le nombre de sections vit dans
`sections.js`, donc dans le contenu.

**Scénario.** Amina, arrivée d'Algérie il y a deux semaines, passe son premier
jour au centre : on lui demande son nom et de l'épeler, elle se présente à Lin,
elle apprend à dire qu'elle ne comprend pas.

**Quatre mini-leçons** : épeler son nom · les cinq phrases pour se présenter ·
de, du, d' devant le pays · saluer, remercier, faire répéter.

**Médias.** 14 images (0,47 $). L'audio a été interrompu par une panne d'API.

**Le défaut que la panne a révélé.** `generer_audio_*.py` s'arrêtait sur la
trace d'une exception à la première coupure réseau, au milieu de deux cents
extraits. Une panne passagère du fournisseur n'est pas une erreur du
programme : `parle()` réessaie maintenant cinq fois, en doublant l'attente, et
traite aussi les 429 et les 5xx. À reporter dans les prochains générateurs.

**Livré.** Commit `3d2724d`. L'audio a été repris après la panne et le module
est en ligne.


## Niveau 2 — `module-n2-autobus` · Prendre l'autobus · **livré**

Deuxième module **court** : huit séances, deux défis, cinq sections. Distinct
de `module-deplacement` (niveau 4), qui porte sur le trajet complet et le
métro ; ici, on demande son chemin et on lit un horaire d'autobus.

**Scénario.** Hassan, arrivé de Syrie il y a huit mois, cherche la
bibliothèque de son quartier, puis apprend à lire un horaire, à comprendre un
avis affiché et à demander une correspondance.

**Quatre mini-leçons** : où on va — à la, au, à l' · les mots de la direction ·
répéter pour être sûr · l'heure de l'autobus.

**Le jeu de rôle a demandé un scénario neuf.** Le manifeste appelait
`jr_scenario: 'autobus'`, qui n'existait pas dans `server.py` — le scénario
`chemin` du niveau 4 était le seul voisin, et il est trop lourd pour un niveau
2 (six étapes, noms de terminus). `JEU_DE_ROLE_AUTOBUS` a donc été ajouté :
trois cas — dans la rue, à l'arrêt, dans l'autobus —, deux rôles, `passager` et
`habitant`, et une conduite qui impose une information à la fois.

**Médias.** 14 images (0,48 $) et 143 extraits audio, tous en place. Le décor
n'est pas le centre de formation, contrairement aux modules précédents :
c'est la rue, et les six photos de l'exercice doivent se reconnaître sans
légende.

ElevenLabs a de nouveau coupé par intermittence — neuf extraits manqués au
premier passage, trois au second. La reprise introduite pour le niveau 1 a
tenu : le script est allé au bout, et deux relances ont comblé les trous. À
retenir pour les niveaux suivants : **ne pas conclure d'un échec réseau que
l'extrait est en cause**, relancer plus tard suffit.

**Huit séances.** 87 diapositives. La séance de graphie-phonie (A2) ne porte
pas sur des lettres mais sur les chiffres de l'heure : c'est là que l'oreille
d'un élève de niveau 2 décroche à l'arrêt. B2 n'apprend aucun mot nouveau —
elle apprend ce qu'on fait quand les mots manquent.


## Niveau 5 — `module-n5-logement` · Louer un logement · **livré**

Produit en parallèle du niveau 6, selon le protocole de
`docs/deux-agents-en-parallele.md`. Activité **58**, réservée d'avance.
Aucun conflit : les deux sessions n'ont touché `modules.py` et
`activities.json` qu'une fois chacune, et s'en sont retirées aussitôt.

**Le niveau 4 traite déjà cette situation** (`module-logement`, « Comment est
le logement ? ») et s'arrête à la visite et à la comparaison. Le niveau 5 va
plus loin, là où le programme le demande : on téléphone, on **prend des
notes**, et on **lit son bail**. D'où un slug qui porte son niveau.

**Scénario.** Nadège habite un trois et demie à Fleurimont avec sa fille de
sept ans, qui dort dans le salon. En février, un avis de modification du bail
arrive dans sa boîte aux lettres : le loyer monte, et la case de stationnement
disparaît. Samuel, du comité logement, lui explique qu'elle a un mois pour
répondre. Hélène est la propriétaire du quatre et demie de la rue Bowen.

**Samuel n'est pas un collègue, et c'est un choix de langue** : entre
collègues on se tutoie, et le module tient le vouvoiement d'un bout à l'autre —
au niveau 5, l'élève s'adresse à un propriétaire, pas à un ami.

**Les trois défis portent les quatre intentions du programme**, sans qu'aucune
reste sans tâche : l'appel et la prise de notes (CO/PE), la visite comprise
**et donnée** (CO/PO), le bail et son renouvellement (CE).

**Neuf mini-leçons.** Les fusions de l'oral d'ici, la lecture d'une annonce et
l'avis de modification à la découverte ; discours indirect au présent et prise
de notes au Défi 1 ; relatifs *qui/que/où* et gérondif au Défi 2 ; futur simple
et phrases impersonnelles au Défi 3. Tous ces points sortent des savoirs du
niveau 5.

**Aucune écriture dans `server.py`.** Le scénario `louer` existe depuis le
niveau 4 et porte déjà les **deux rôles** dont le niveau 5 a besoin — celui qui
demande et celui qui donne les renseignements. C'est le seul module du chantier
à n'avoir rien coûté au fichier partagé.

**Deux défauts trouvés dans le mécanisme des phrases porteuses**, et ils valent
pour tous les modules :

- **Les clés de `carrier.js` sont les mots littéraux**, pas des noms de
  fichiers. Le gabarit fait `CARRIER_PHRASES[w]` **sans normaliser** : une clé
  `avis_modification` n'est jamais trouvée, et le mot part seul à la synthèse,
  mal accentué — précisément ce que le mécanisme existe pour éviter.
  `module-n3-epicerie` porte le même défaut (clés `allee`, `special` contre les
  mots `allée`, `spécial`) : ses mots isolés partent seuls. Non corrigé ici,
  c'est le module d'une autre session.
- **Une carte de phonétique ne porte jamais un fragment nu.** Les huit cartes
  disaient « sur le », « dans la ». Envoyé seul à la synthèse, un fragment de
  ce genre ressort **sur-articulé** — le contraire exact de ce que la leçon
  fait entendre, puisqu'elle porte justement sur la fusion à l'oral rapide.
  Elles portent maintenant la phrase entière, et l'élève y repère la
  préposition.

**Sept tableaux de séance dépassaient la hauteur d'une diapositive projetée.**
Coupés en deux plutôt que raccourcis : ce sont des tableaux de référence, que
l'élève photographie, et une cellule tronquée ne lui sert à rien. Le garde-fou
de `theme.py` les a tous attrapés d'un coup — il suffit d'importer les seize
decks et d'appeler leur `build()` dans un dossier temporaire pour avoir la
liste complète, au lieu de reconstruire seize fois de suite.

**La flèche « → » n'existe pas dans Verdana.** Le garde-fou de `save()` l'a
arrêtée dans trois decks de grammaire, où elle servait à écrire
« nous regardons → en regardant ». Remplacée par « donne » — le mot que
l'enseignante dit de toute façon à voix haute.

**Ce que le sujet a coûté aux images.** Comme au niveau 6, presque tout ce
qu'on photographie ici est du papier écrit : un bail, un avis, une annonce. Les
prompts interdisant tout texte lisible, les documents sont pris de biais et en
faible profondeur de champ, les lignes réduites à des traits gris. C'est voulu
et non un pis-aller : un élève ne doit pas lire un faux bail approximatif sur
une photo.

**Bilan.** 24 exercices, 9 mini-leçons, 5 dialogues, 16 mots, 30 images,
221 extraits audio, 16 présentations (200 diapositives), 16 fiches
(149 blocs), 16 vignettes.

**Quatre passes ont été nécessaires pour l'audio.** ElevenLabs a coupé par
intermittence pendant toute la production : 32 échecs à la première passe, puis
21, puis 12, puis 5. Aucun extrait n'était en cause — la reprise du script fait
exactement ce pour quoi elle a été écrite, et une relance saute ce qui existe
déjà. Deux images ont échoué de la même façon et se sont rattrapées en une
commande. **Conclusion pratique : ne pas surveiller la première passe, boucler
la relance.** `for i in 1 2 3 4 5; do python3 generer_audio_… ; done` coûte
moins cher en attention qu'un suivi ligne à ligne, et le compte de fichiers dit
seul quand c'est fini.

## Niveau 6 — `module-n6-recherche` · Chercher un emploi · **livré**

Produit en parallèle du niveau 5, selon le protocole de
`docs/deux-agents-en-parallele.md`. Activité **59**, réservée d'avance.

**Le slug a changé.** Le tableau de ce fichier annonçait `module-n6-emploi`.
La situation « Emploi » du programme est celle retenue pour le niveau 8 : deux
slugs voisins pour deux modules très différents se seraient confondus. Le slug
nomme le scénario, pas la situation du programme — comme aux niveaux 1 et 2.

**Scénario.** Marisol Aguirre, arrivée de Colombie il y a deux ans, ancienne
responsable des stocks, veut quitter son temps partiel. Djamila Toubaï la
reçoit au Tremplin-Emploi ; Robert Chartier, chef d'entrepôt chez Boisverte,
la reçoit en entrevue.

**Les trois défis suivent la démarche réelle**, et chacun porte une des quatre
intentions du programme : lire l'offre détaillée et s'informer sur
l'entreprise (CE), remplir la demande d'emploi (PE), passer la courte entrevue
et offrir ses services (CO/PO).

**Neuf mini-leçons.** Nasales AN/ON et formation des mots à la découverte ;
adjectifs en -able et relatif « où » au Défi 1 ; infinitif passé et
subordonnée infinitive avec de/à au Défi 2 ; subjonctif après verbe
introducteur et connecteurs d'exemplification au Défi 3. Tous ces points
sortent des savoirs du niveau 6, sans en inventer un seul.

**Un scénario de jeu de rôle neuf**, `entrevue` — le treizième de
`server.py`. Aucun des douze existants n'était voisin. Trois postes (commis à
l'inventaire, aide-cuisinier, préposé à l'entretien), deux rôles, et une
conduite qui **relance quand la réponse tient en une phrase** : c'est la
différence du niveau 6, où l'élève doit tenir un discours détaillé.

**Ce que le sujet a coûté aux images.** Tout ce qu'on photographie ici est du
papier écrit — une offre, un formulaire, une lettre. Au premier passage,
l'affiche d'offre d'emploi portait « ANNOUNCEMENT » en anglais bien lisible,
et quatre photos de feuilles posées sur une table de bois étaient
indistinguables les unes des autres dans un banc de vocabulaire. Cinq images
refaites, avec des supports distincts — une main qui tend un CV, un calendrier
mural, une tablette, une enveloppe — et une consigne explicite contre toute
lettre lisible. **À retenir pour le niveau 8**, qui portera sur l'emploi et
photographiera les mêmes objets.

**Deux limites du gabarit de diapositives**, découvertes ici et payées :
Verdana n'a ni les symboles de l'alphabet phonétique ni la flèche `→`, donc la
séance de graphie-phonie dit « le son AN » et « le son ON » là où le module
interactif garde `[ɑ̃]` et `[ɔ̃]` ; et un tableau de six lignes à deux colonnes
ne tient pas sur une diapositive projetée — `theme.py` le refuse avec un
message clair, et il faut le couper en deux.

**Originalité.** Le vérificateur de copie n'a pas d'objet : il n'existe aucune
version antérieure. La mesure faite est donc la coïncidence avec les onze
autres modules du dépôt : **4 énoncés sur 209, soit 1,9 %**, et les quatre sont
des consignes du gabarit (« Le mot et sa définition », « Écoutez de nouveau le
dialogue, puis répondez »). Sous le seuil de 5 %.

**Ce qui reste à corriger, et qui ne m'appartient pas.** Les invites de
`server.py` disent « niveau 4 (débutant-intermédiaire) » **en dur** — dans
`jeu_de_role_system()` comme dans les correcteurs de production orale et
écrite. Les sept modules des autres niveaux font donc parler l'assistant comme
au niveau 4 : trop simple pour le 6 et le 7, trop complexe pour le 1 et le 2.
Le niveau est pourtant connu (`modules.py`, `normalize_level`). C'est un
changement transversal qui touche tous les modules à la fois : selon la règle 5
de `docs/deux-agents-en-parallele.md`, il se fait quand personne d'autre
n'écrit, pas au milieu d'un module.


## Niveau 8 — `module-n8-emploi` · Tenir son bout au travail · **livré**

Activité **61**, `numero` 1 du niveau 8, seize séances. Produit le 21 août 2026,
en parallèle du niveau 7, selon `docs/vagues-suivantes.md`.

**Le scénario.** Nadia Kessab, adjointe administrative depuis huit mois chez
Portes et fenêtres Valmont, une PME de quarante employés à Laval. Autour
d'elle : Manon Trépanier, sa superviseure ; Yves Boudreault, magasinier ;
Sylvain Ouellet, au service de la paie ; Claudia Fortin, conseillère en
formation continue. L'arc suit une même personne **déjà en poste** — c'est ce
qui le sépare de `module-n6-recherche`, où l'on cherche encore un emploi. Elle
comprend ses tâches en détail, règle une erreur de paie, intervient dans une
réunion de décision, puis demande un congé de formation.

**Ce que le niveau 8 impose, et qu'aucun module précédent n'avait.** La
situation « Emploi » porte **dix** intentions de communication, la plus dense
des six du niveau. Les dialogues font de dix-huit à vingt et une répliques,
souvent longues : la compétence vise des communications complexes, pas des
échanges de trois tours. Le programme ne fournit **aucun lexique** pour cette
situation — les seize mots sont composés à partir des intentions et des
savoirs. Douze mini-leçons plutôt que neuf, pour couvrir la progression :
prosodie des phrases longues, registres, subjonctif de nécessité, phrase
passive, lettre d'affaires, les deux conditionnels, connecteurs, discours
rapporté, pronoms relatifs composés, hypothèse au plus-que-parfait, reprise de
l'information.

**Les faits québécois ont été vérifiés à la source, jamais écrits de
mémoire.** Ce module cite des normes du travail dans un exercice, une
mini-leçon et deux séances (B2 et D1) ; s'y tromper aurait des conséquences
réelles pour un élève. Vérifications faites le 20 août 2026 :

- **CNESST** — au-delà de **40 heures** par semaine, majoration de **50 %** ;
  remplacement par un congé payé équivalent aux heures **plus 50 %**, à la
  demande du salarié, à prendre dans les **12 mois** ;
- **CNESST** — période de repas de **30 minutes** après **5 heures**
  consécutives, non payée sauf si le salarié ne peut quitter son poste ;
  pause-café non obligatoire, mais payée et comptée si elle est accordée ;
- **CNESST / Tribunal administratif du travail** — congédiement sans cause
  juste et suffisante : **2 ans** de service continu, plainte dans les
  **45 jours** ; harcèlement psychologique ou sexuel : plainte dans les
  **2 ans** de la dernière manifestation ;
- **CPMT / Revenu Québec** — « loi du 1 % » : les employeurs dont la masse
  salariale dépasse **2 000 000 $** investissent au moins **1 %** en formation,
  sinon cotisent au FDRCMO.

Le site de la CNESST refuse les requêtes automatisées (HTTP 403) : les données
ont été relevées par recherche sur les domaines officiels, puis recoupées avec
les articles de la Loi sur les normes du travail (55, 79, 123.7, 124). Aucun
délai n'a été écrit sans avoir été vu — en particulier, **rien n'est dit du
délai de réclamation de salaire**, qui n'a pas été vérifié.

**Le jeu de rôle a demandé un scénario neuf dans `server.py`.** Clé `emploi`,
trois cas — une erreur sur la paie, un horaire changé sans avis, une facture
réglée deux fois — et deux rôles, `employe` et `service`. Aucun scénario
existant ne convenait : ceux du niveau 4 donnent des répliques courtes, et
`entrevue` suppose qu'on cherche encore un emploi. La conduite de l'assistant
lui impose **d'objecter au moins une fois** avant de bouger : c'est là que la
compétence du niveau 8 se joue, et un interlocuteur trop conciliant ne fait
rien travailler.

**Trois pièges payés, à ne pas repayer.**

- Le manifeste des sons se relève d'ordinaire dans le navigateur. Le poste n'a
  pas de Node, mais il a **`jsc`**
  (`/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`) :
  les quatre fichiers de contenu s'y chargent tels quels et la logique de
  `plAudioManifest()` s'y rejoue en vingt lignes. Résultat comparé au relevé du
  navigateur : 152 entrées de part et d'autre.
- **Le HTML produit par `build/module.py` est versionné, et rien ne le
  commite pour vous.** Les seize séances, les seize fiches, les dix-sept
  images, les relevés et le journal étaient en ligne ; la page que l'élève
  ouvre, non — elle répondait 404 en production pendant que tout le reste
  répondait 200. Le `git add` par chemins explicites, qui protège le travail
  des autres sessions, a exactement ce revers : ce qu'on n'a pas nommé n'est
  pas commité. Vérifier avant de conclure :

      git status --short assets/interactive/<slug>/

- Un bloc `ana` **sans `say`** ne produit pas un extrait audio : il produit la
  **concaténation de sa colonne `mots`**, balises `<i>` comprises, qui serait
  lue telle quelle à l'élève. Vingt-neuf blocs étaient dans ce cas. Écrire un
  `say` sur chaque `ana`, sans exception.

**L'audio est en attente, et c'est la seule pièce qui manque.** Neuf MP3 sur
230 ont été produits avant que `api.elevenlabs.io` ne devienne injoignable, le
21 août vers 00 h 25 — la poignée de main TLS est coupée juste après le
*Client hello*, y compris hors du bac à sable et avec `curl`. Voir la section
« Le bac à sable réseau bloque ElevenLabs » de `docs/deux-agents-en-parallele.md`
et sa précision du 21 août. Le générateur `generer_audio_module_n8_emploi.py`
est écrit, vérifié, relançable, et son manifeste `sons_module_n8_emploi.json`
est complet (152 entrées) : il n'y a qu'à le relancer quand la liaison revient.

    python3 generer_audio_module_n8_emploi.py

Aucun `AUDIO_V` à incrémenter : ce sont des fichiers neufs, pas des fichiers
régénérés sous le même nom.

**Originalité : 0 %.** Aucun des 184 énoncés visibles par l'élève n'est
identique à un énoncé d'un autre module du dépôt. Rien n'a été copié d'un
manuel ; le programme n'a donné que la spécification.


## Niveau 7 — `module-n7-actualite` · Suivre l'actualité · **livré**

Produit le 21 août 2026, en parallèle du niveau 8. Activité **60**, `numero` 1
dans le niveau 7, seize séances, indigo `#3B49A0` — la couleur du niveau, qui
ne se choisit plus.

**Le scénario.** Farida Benali, éducatrice en CPE, s'est mise à suivre
l'actualité de son quartier depuis qu'un projet municipal touche sa rue. Sa
voisine Suzie Lamontagne anime le blogue du quartier ; Ludovic Chagnon,
journaliste à la radio communautaire, signe le reportage et l'entrevue ;
Hélène Ferron est la conseillère, Benoît Sarrazin le dépanneur d'en face,
Marjolaine Cusson la résidente sans auto. Quatre pas : elle écoute un
reportage, elle lit un article, elle démêle le fait de l'opinion dans une
chronique, elle écrit son propre billet. Le module va du bruit de
l'information à la prise de parole.

**Ce que ce niveau porte de neuf, et qu'aucun module précédent n'avait.**

- **Des discours longs.** La compétence vise des textes et des échanges
  étendus, pas des dialogues de trois répliques. Le reportage fait dix-sept
  répliques, l'entrevue vingt-deux, plusieurs de quatre ou cinq phrases. Le
  Défi 1 est donc bâti sur la **méthode des trois écoutes** — une pour le
  sujet, une pour les chiffres, une pour ce qui est confirmé — et chaque
  séance du bloc B en fait une. C'est le découpage qui rend un extrait long
  travaillable ; sans lui, il est seulement décourageant.
- **Aucun lexique fourni.** `build/cadre.py 7 "Suivi de l'actualité"` rend
  zéro entrée : le document de lexique ne couvre pas cette situation. Les
  dix-huit mots du banc sont composés à partir des savoirs et des intentions,
  comme le script l'annonce lui-même.
- **Un scénario de jeu de rôle neuf.** `actualite` dans `server.py` : deux
  voisins qui discutent d'une nouvelle, trois cas, deux rôles. Le voisin
  sceptique défend d'abord une idée reçue fausse — que la Ville exploitera le
  dépôt — pour obliger l'élève à citer une source ; et il mêle une fois un
  fait exact à un jugement, pour qu'il ait à les séparer. Vérifié dans les
  deux sens : `jr_scenario`, `jr_cas` et `jr_role` du manifeste existent bien
  côté serveur. Rien ne le vérifie au build, et l'échec ne se verrait que chez
  l'élève.

**Le même conditionnel, deux fois, et le module le dit.** Au Défi 1 il marque
l'information non confirmée (« le local *serait* loué ») ; au Défi 2 la
postériorité dans le discours rapporté (« elle a promis qu'elle *rappellerait*
»). C'est le verbe introducteur qui tranche, et la mini-leçon `t2indirect` le
pose explicitement comme le piège du bloc. Les élèves qui ont bien compris B3
sur-interprètent en C3 : c'est bon signe, et il faut l'attendre.

**Les faits québécois, vérifiés et non inventés.** Deux seulement, et ils
portent tout le dossier :

- la **consigne** est de 0,10 $ sur les contenants visés et de 0,25 $ sur le
  verre de 500 ml et plus, en vigueur depuis le **1er novembre 2023** ; les
  contenants de plastique sont visés depuis le **1er mars 2025** ; le verre et
  les multicouches s'ajouteront en **mars 2027**. Vérifié sur RECYC-QUÉBEC et
  Consignaction, et sur l'annonce gouvernementale de la réforme.
- toute **séance du conseil** d'une municipalité comprend une **période de
  questions** où les personnes présentes peuvent interroger les élus ; le
  conseil en fixe la durée et la procédure par règlement. Vérifié à
  l'article 322 de la *Loi sur les cités et villes*.

Tout le reste — le quartier du Ruisseau, la rue Boisjoli, la radio
communautaire, le blogue, les six personnages — est **inventé**, et la séance
B2 le dit au groupe en toutes lettres : un élève doit savoir ce qu'il peut
répéter à l'extérieur du cours. C'est la raison pour laquelle aucune vraie
municipalité n'est nommée : prêter un projet fictif à une ville réelle aurait
fabriqué exactement le genre de fausse information que le module apprend à
repérer.

**Deux fautes trouvées en chemin, toutes deux dans le contenu, toutes deux
invisibles au build.**

1. L'apostrophe de `bravo` n'était pas échappée dans le manifeste. Elle est
   injectée dans une chaîne JavaScript à guillemets simples, exactement comme
   `relance` — dont la documentation, elle, signale l'échappement. Non
   échappée, elle ferme la chaîne : `SyntaxError`, script mort, plus un seul
   exercice affiché. Aucun module précédent ne l'avait rencontrée parce
   qu'aucun titre ne contenait d'apostrophe ; « Suivre l'actualité », si.
2. Treize lignes de bloc `piege` de `plus.js` étaient fermées par `}` au lieu
   de `]`. Même effet, même invisibilité.

D'où **une vérification qui manquait à la chaîne** et qui est maintenant dans
`CLAUDE.md` : extraire le plus gros script inline du HTML produit et le passer
à `node --check`. Le build assemble du JavaScript qu'il ne lit jamais ; sans ce
contrôle, la première personne à voir l'erreur est l'élève.

**Un détail des mini-leçons, à retenir pour les prochains modules.** Un bloc
`ana` sans champ `say:` ne fait pas taire le bouton d'écoute : le moteur
concatène toutes les lignes du tableau, balises comprises, et l'extrait part
lire « cent quarante mètres carrés huit places quinze minutes le 1er novembre
2023 ». Quatorze blocs étaient dans ce cas. **Tout bloc `ana` veut son
`say:`.**

**Les médias.** Treize images en 3:2 par fal.ai (environ 0,44 $) — six pour le
glisser-déposer, sept pour le banc. Le sujet étant l'information écrite,
presque chaque image contient du papier, un écran ou un micro : chaque prompt
exige que toute ligne de texte soit un trait gris. Vérifié sur
`journal-etale`, la plus risquée : ni mot ni manchette lisibles.

Côté audio, **201 extraits** attendus — 80 répliques et 121 sons — et la même
panne intermittente d'ElevenLabs que le niveau 8 a rencontrée le même jour. Le
générateur `generer_audio_module_n7_actualite.py` est écrit, relançable, et
son manifeste `sons_module_n7_actualite.json` est complet (121 entrées,
relevés dans le navigateur). Il saute ce qui existe déjà :

    python3 generer_audio_module_n7_actualite.py

Aucun `AUDIO_V` à incrémenter : ce sont des fichiers neufs.

**Originalité : 3 %.** Sur 218 énoncés visibles par l'élève, six sont
identiques à un énoncé d'un autre module du dépôt, et les six sont des
consignes génériques imposées par le moteur — « Le mot et sa définition »,
« Glissez chaque photo sur la phrase qui la décrit ». Sous le seuil de 5 %.
Rien n'a été copié d'un manuel ; le programme n'a donné que la spécification.


## Niveau 5 — `module-n5-services` · Les services de ma ville · **livré**

Quatrième module du niveau 5, activité **64**, produit le 21 août 2026 pendant
que trois autres sessions travaillaient dans le dépôt.

**La situation du programme est étroite, et c'est ce qui la rend difficile.**
« Utilisation des services publics » ne donne que trois intentions de
communication — comprendre et demander des renseignements par téléphone (CO et
PO), comprendre de l'information dans un formulaire complexe, une brochure ou
un site Web (CE) — et **aucun lexique** : le document de Laval ne couvre pas
cette situation. Les seize mots s'inventent donc entièrement à partir des
savoirs et des intentions. Le domaine général de formation, lui, tranche la
question du sujet : « Consommation et environnement », d'où l'angle municipal
plutôt qu'administratif au sens large.

**Ce qui distingue ce module de ses voisins.** Le niveau 4 n'a aucun module sur
cette situation ; le plus proche, « Quelle est la procédure ? » (40), reste
dans l'établissement scolaire. Le vrai risque de recoupement était
`module-n5-emmenagement` (63), dont le défi 2 fait justement changer d'adresse
et brancher les services. La ligne de partage est nette et vaut d'être notée :
**là-bas on branche un service le jour du déménagement, ici tout est branché
depuis huit mois et c'est le service qui a mal fonctionné.** Le module ne parle
donc pas d'installation mais de démarche — appeler, lire, se présenter,
relancer.

**Le scénario.** Leïla Haddad, 41 ans, arrivée de Tunis, habite Villeray depuis
huit mois. Elle a pris la brochure de la Ville pour de la publicité. Son bac
brun n'est plus ramassé : elle appelle le 311 (défi 1), lit la page de
l'écocentre et un formulaire qui se bloque (défi 2), puis se présente au
guichet avec un billet de file d'attente (défi 3). Autour d'elle : Pierre-Luc,
un collègue de son cours ; Micheline, préposée au service à la clientèle ;
Gaétan, agent au comptoir ; et VOIX, le menu automatisé.

**Les faits québécois, vérifiés le 21 août 2026 sur les sites officiels** —
aucun n'est inventé, et aucun montant en dollars n'apparaît dans le module :

- le **311** de la Ville de Montréal enregistre les demandes citoyennes sous
  forme de requêtes numérotées, et sert à signaler un problème de collecte
  (montreal.ca, « Signaler un problème de collecte », données ouvertes
  « Requêtes 311 ») ;
- **Info-collectes** donne l'horaire par code postal, et il diffère d'une rue
  à l'autre (montreal.ca, « Horaire des collectes ») ;
- les **écocentres** reprennent peinture, appareils électroniques, débris de
  construction et métal ; les tarifs et les temps d'attente sont publiés
  (montreal.ca, « Écocentres ») ;
- **Hydro-Québec**, service à la clientèle résidentielle : 1 888 385-7252
  (hydroquebec.com, « Nous joindre ») — vérifié, puis **non employé**, le
  module ayant basculé du branchement vers le municipal ;
- le **Service québécois de changement d'adresse** transmet l'adresse à sept
  ministères et organismes en une démarche (quebec.ca) ;
- la **SAAQ** demande d'être avisée dans les **30 jours** suivant un
  déménagement (saaq.gouv.qc.ca, « Changement d'adresse »).

Les seuls chiffres inventés du module sont le numéro de requête (24-118-7690),
l'adresse de Leïla et le numéro de téléphone de la production orale, qui est en
555 — c'est voulu.

**Le jeu de rôle a fallu l'écrire.** Aucun des scénarios existants ne rend la
conduite d'un appel à un service public, et le module s'était construit sans
erreur avec une clé absente : rien ne le vérifie. `server.py` gagne donc
`JEU_DE_ROLE_SERVICES` (trois cas : le bac non ramassé, l'écocentre, la demande
bloquée en ligne) et l'entrée `services`, rôles `citoyen` et `prepose`. Sa
règle de conduite est le cœur de l'exercice : **le préposé ne donne jamais un
renseignement avant qu'on le lui demande**, et il ne rappelle jamais à l'élève
ce qu'il a oublié de demander. La vérification tient en une ligne :
`python3 -c "import server; print(server.JEU_DE_ROLE_SCENARIOS['services'])"`.

**Trois choses apprises en produisant les séances**, qui valent pour le
prochain module :

- `theme.py` refuse l'alphabet phonétique, et il a raison : la séance A2 nomme
  les sons par leurs lettres et un mot repère (« le son AN, comme dans
  attente »). Le module interactif, lui, garde les symboles. **La flèche « → »
  n'est pas dans Verdana non plus** — elle passe le garde-fou des glyphes sans
  être signalée, parce que celui-ci ne contrôle pas les caractères de
  ponctuation. Trois séances en portaient.
- **Un tableau de six lignes ne passe pas sur une diapositive projetée.** Trois
  l'ont appris (A4, C4, D1) et sont coupés en deux.
- **`build/powerpoints/fiche.py` n'a pas de méthode `capture()`**, contrairement
  à `theme.py`. Les quatre appels sont donc gardés par `hasattr` dans les
  séances de ce module — une fiche noir et blanc n'a de toute façon rien à
  faire d'une capture d'écran. **Le défaut est antérieur et bloque aussi
  `module-sante`, dont les fiches ne se régénèrent plus** : à corriger dans le
  moteur quand personne d'autre n'écrit.

**Le dossier `icons/` ne sort d'aucun générateur.** Il se copie d'un module
voisin, et rien ne signale son absence : le build passe, les six contrôles
passent, et ce sont trois 404 chez l'élève. Vu seulement en ouvrant le module
déployé dans un navigateur — c'est l'argument pour continuer de le faire.

**Deux textes ont dû être réécrits pour la synthèse vocale.** Les six paires de
registres de `prReg` étaient reliées par une flèche, que la voix lit à haute
voix, et une formule de `t1notes` portait des points de suspension. La règle
générale : tout ce qui entre dans `sons_<slug>.json` doit se lire à voix haute
sans caractère qui ne se prononce pas.

**Originalité : 1 %.** Sur 151 énoncés visibles par l'élève, un seul est
identique à un énoncé d'un autre module — « Glissez chaque photo sur la phrase
qui la décrit », la consigne standard d'un `imgmatch`. Rien n'est copié d'un
manuel : le module n'a aucune source antérieure.

**Livré** : 19 exercices, 11 mini-leçons, 4 dialogues (70 répliques), 16 mots
de vocabulaire, 24 images fal.ai (0,82 $), 16 présentations (197 diapositives),
16 fiches (143 blocs), 16 vignettes, un scénario de jeu de rôle.

**L'audio reste à produire.** ElevenLabs coupait la liaison TLS au moment de la
production — `curl` sur `api.elevenlabs.io` rend `000` dans le bac à sable
**comme en dehors**. Les 185 extraits (70 répliques + 115 sons) sont relevés
dans `sons_module_n5_services.json` et le générateur est écrit ; il est
relançable et saute ce qui existe déjà. Une seule commande suffit quand la
liaison revient :

    for i in 1 2 3 4 5; do python3 generer_audio_module_n5_services.py; done

Le module se livre ainsi, comme le niveau 8 avant lui : les boutons d'écoute
restent en place et ne sont **pas** masqués à la main dans le HTML.

## La couleur d'un module est devenue celle de son niveau

Décidé par l'utilisateur le 20 août 2026, au milieu de ce chantier, et
appliqué à tout le dépôt avant de reprendre le niveau 2. Deux échelles
vivaient pour une seule idée : une pastille ambre au catalogue, un en-tête
forêt en ouvrant le module. Elles n'en font plus qu'une, et le vert en est
sorti — l'olive du niveau 3 et la forêt du niveau 4 ont disparu, l'ambre est
descendu du 2 au 3, la brique a pris le 2 et l'or le 4.

Deux scripts tiennent la règle, tous deux avec `--verifier` :

    python3 build/couleurs_niveau.py --verifier
    python3 build/couleurs_sections.py --verifier

Conséquence pour la suite du chantier : **un module neuf n'a plus de couleur à
choisir.** Lui donner son niveau dans `build/powerpoints/modules.py` suffit, et
`sections.js` ne doit contenir ni `#166534` ni `#0F766E`.

## Niveau 2 — `module-n2-panier` · Remplir mon panier · **livré**

Activité **87**, réservée d'avance par `docs/vagues-suivantes.md` (vague 4).
Troisième module **court** du dépôt : huit séances, deux défis, cinq sections,
`GRILLE_COURTE`. Produit le 21 août 2026, en parallèle des niveaux 5 et 3.

**Ce qui le distingue de ses voisins**, en une phrase : `module-n3-epicerie`
fait trouver, choisir et payer, `module-alimentation` (niveau 4) tient le
comptoir et l'étiquette — ici, on ne parle presque pas, on **lit des chiffres
et des formats** avant de remplir son panier, parce que l'unique intention que
le programme donne à cette situation au niveau 2 est en compréhension écrite :
« consulter des circulaires, des étiquettes et des affichettes pour repérer
des indications de mesure et de prix ».

**Scénario.** Aminata reçoit la circulaire du mardi dans sa boîte aux lettres.
Sa voisine Rose lui apprend à y lire les prix — « 2 pour 9 $ », « 3,99 $ le
kilo » — et à écrire une liste. Au magasin, le commis Denis lui donne l'allée,
le format et le prix ; à la caisse, elle fait valoir un spécial en montrant sa
circulaire.

**Cinq mini-leçons** : la lettre s, [s] ou [z] · lire un prix, et le dire ·
un, une, des — et « pas de » · les questions courtes du magasin · un kilo de
riz, un litre de lait.

**Le jeu de rôle a demandé un scénario neuf.** Le scénario `epicerie` existe,
mais il est écrit pour le niveau 3 et fait tenir un échange suivi.
`JEU_DE_ROLE_PANIER` a donc été ajouté à `server.py` : trois cas — dans
l'allée, devant les fruits, à la caisse —, deux rôles, `client` et `commis`,
et une conduite qui impose deux ou trois répliques, pas davantage.

**Médias.** 18 images (0,61 $) et 189 extraits audio (43 répliques sur six
dialogues, 146 mots et phrases). Aminata prend la voix féminine 2, Rose celle
de l'enseignante ralentie à 0,85, Denis la voix masculine — les trois se
répondent, aucune voix n'est partagée. ElevenLabs n'a pas coupé une seule
fois cette nuit-là ; une seule image a expiré et une relance a suffi.

**La difficulté propre à ce module est que ses images portent du texte.**
Circulaire, étiquette, affichette : ce sont des papiers écrits, et le
générateur a l'ordre de ne produire aucun texte lisible. Les prompts
demandent donc des papiers dont la *forme* est nette — grille de cases,
colonnes de chiffres, petit carton dans son rail — sans qu'aucun mot ne se
lise. Un élève de niveau 2 reconnaît l'objet ; le contenu, c'est l'exercice
qui le donne.

**Huit séances.** 90 diapositives, 67 blocs de fiches. A2 est la séance de
phonétique et porte sur [s] / [z], que le programme du niveau demande et que
le rayon des fruits offre tout fait — cerise, raisin, framboise, saucisse.
B1 est la séance qui répond à l'intention du programme : trois écritures de
prix, dont « 3,99 $ / kg », qui est le piège réel de l'épicerie.

**Un piège du build, payé une fois.** Le champ `theme` du manifeste passe lui
aussi dans une chaîne JavaScript à guillemets simples : « Achat d'aliments ou
de produits d'entretien » a dû s'écrire `d\\'aliments`, exactement comme
`bravo` et `relance`. Le build s'arrête proprement et le dit.

## Niveau 2 — `module-n2-bonjour` · Bonjour, ça va ? · **livré**

Activité **88**, réservée d'avance par `docs/vagues-suivantes.md` (vague 4).
Quatrième module **court** du dépôt, troisième du niveau 2 : huit séances,
deux défis, cinq sections, `GRILLE_COURTE`. Produit le 21 août 2026, en
parallèle des niveaux 3 et 5.

**Ce qui le distingue de ses voisins**, en une phrase : `module-n1-presenter`
apprend à dire son nom et `module-relations` (niveau 4) tient une conversation
suivie qui raconte au passé — ici, on entre dans un échange de deux ou trois
répliques, au présent, avec quelqu'un qu'on **recroisera demain matin** dans
l'entrée de l'immeuble.

**Le cadre l'a décidé.** `build/cadre.py 2 "Relations sociales"` donne cinq
intentions, et elles couvrent les quatre compétences : comprendre une demande
d'aide (CO), décrire ses activités quotidiennes (PO), comprendre des souhaits
ou des remerciements et choisir une carte de vœux (CE), rédiger des souhaits
et des remerciements simples (PE). C'est le premier module court du dépôt dont
le programme réclame les quatre — d'où deux défis nettement séparés : l'échange
parlé, puis l'aide et l'écrit.

**Scénario.** Nadia habite au troisième et croise madame Roy, sa voisine
retraitée du deuxième, chaque matin dans l'entrée. Au centre, elle tutoie son
camarade Samir ; avec madame Roy, elle vouvoie — et madame Roy la tutoie. Puis
la voisine revient de l'épicerie les mains pleines et demande de l'aide ;
samedi, c'est sa fête, et Nadia écrit une carte.

**Six mini-leçons** : la voix qui monte et la voix qui descend · bonjour,
bonsoir, bonne journée · tu ou vous · ma journée au présent · demander de
l'aide · merci et bonne fête.

**Le jeu de rôle a demandé un scénario neuf.** Le scénario `relations` existe,
mais il est écrit pour le niveau 4 : conversation suivie, récit au passé.
`JEU_DE_ROLE_BONJOUR` a donc été ajouté à `server.py` — trois cas (l'entrée le
matin, l'ascenseur avec les sacs, la carte de fête), deux rôles, `moi` et
`voisine`, et une conduite qui impose deux ou trois répliques, une seule
question à la fois, jamais de passé.

**Médias.** 18 images (0,61 $) et 214 extraits audio (50 répliques sur six
dialogues, 164 mots et phrases), sans un seul échec réseau. Nadia prend la voix
féminine 2, madame Roy celle de l'enseignante ralentie à 0,85, Samir la voix
masculine — les trois se répondent, aucune voix n'est partagée.

**La difficulté propre à ce module est que ses images montrent des gens qui se
parlent**, alors que le générateur a l'ordre de ne produire aucune personne
identifiable. Les prompts demandent donc des silhouettes de dos, des mains, des
pieds, ou la pièce juste après que la personne est passée : se croiser dans un
hall, tenir une porte, marcher sur un trottoir. Le geste se lit ; aucun visage
n'apparaît.

**Huit séances.** 93 diapositives, 70 blocs de fiches. A2 est la séance de
phonétique et porte sur l'**intonation** — la voix qui monte pour demander,
qui descend pour répondre —, le premier savoir prosodique que le programme
demande au niveau 2, et « ça va » l'offre tout fait. B1 porte le point de
langue du module : le même échange, joué deux fois, au « tu » puis au « vous ».

**Deux pièges, dont un neuf.**

- **Les flèches ↗ et ↘ ne sont pas dans Verdana**, et le garde-fou de
  `theme.py` refuse la production tant qu'elles restent dans un deck. C'est la
  règle « rien qui sorte de Verdana » appliquée à un cas qu'on ne voit venir
  qu'en écrivant une séance de prosodie : l'intonation se dit alors en mots
  (« la voix monte »), ce qui est de toute façon plus clair projeté. Les
  flèches restent dans le module interactif, que le navigateur rend bien.
- **`build/collecte_sons.py` écoute un port, et le port peut être déjà pris.**
  Lancé sur 8799 pendant qu'une autre session y écoutait, il a échoué au
  démarrage — `Address already in use`, dans un `nohup` dont personne ne lit la
  sortie — et le relevé envoyé depuis le navigateur est allé écrire dans le
  `sons_<slug>.json` **de l'autre module**. Rien n'a été perdu (la session
  voisine a régénéré le sien), mais l'incident est le même que celui déjà
  documenté dans `CLAUDE.md` : un collecteur qui n'est pas le sien répond « ok »
  sans qu'on puisse le distinguer. **Vérifier que le port est libre avant de
  lancer, et vérifier le nom du fichier écrit après.**

**Les six contrôles** passent pour ce module. `pieds_de_page.py` et
`sommaire.py --verifier` signalent encore `module-n3-electro` et
`module-n5-urgence` : ce sont les deux modules que les sessions voisines
produisaient au même moment, pas des écarts de celui-ci.


## Niveau 2 — `module-n2-classe` · Ouvrez votre cahier · **livré**

Activité **89**, réservée d'avance par `docs/vagues-suivantes.md` (vague 4).
Cinquième module **court** du dépôt, quatrième du niveau 2 : huit séances,
deux défis, cinq sections, `GRILLE_COURTE`. Produit le 21 août 2026, en
parallèle des activités 66 et 76.

**Ce qui le distingue de ses voisins**, en une phrase : `module-n2-bonjour`
salue un voisin dans une entrée d'immeuble et `module-procedure` (niveau 4)
suit une marche à suivre écrite de plusieurs étapes — ici, la directive fait
**trois mots**, commence par un verbe à l'impératif, et la bonne réponse de
l'élève est souvent « pouvez-vous répéter ? ».

**Le cadre l'a décidé.** `build/cadre.py 2 "Salle de classe"` ne donne que
**trois** intentions, et deux d'entre elles sont la même : comprendre une
directive à l'oral (CO), comprendre une directive à l'écrit (CE), donner des
renseignements sur le fonctionnement de la classe et de l'établissement (PO).
C'est le module le plus resserré du niveau, et c'est ce qui l'a structuré :
Défi 1 pour la directive entendue, Défi 2 pour la directive lue — l'avis
affiché près de la porte —, et « Je me lance » pour le renversement, où
l'élève explique enfin ce qu'il a passé quatre séances à comprendre. La
production écrite, qu'aucune intention ne réclame à ce niveau, se réduit à ce
qu'un débutant écrit vraiment : un mot d'absence de trois lignes.

Le lexique du programme est repris tel quel, sans un mot de plus : objets de la
classe ; les cinq couleurs rouge, bleu, jaune, vert, noir ; pause, congé,
calendrier ; permission, absence, retard ; et les énoncés à mémoriser — lisez,
ouvrez, fermez, enlevez, donnez, mettez, écoutez, c'est permis, c'est interdit,
soyez à l'heure.

**Scénario.** Tariq est arrivé lundi au centre et s'assoit au premier rang, à
côté de Myriam. Madame Leduc donne la première consigne du matin ; Tariq ne
comprend pas et le dit. Il apprend les huit verbes, puis demande la permission
de sortir, lit l'avis affiché, et prévient d'une absence pour un rendez-vous.
À la dernière séance, c'est lui qui explique la classe à quelqu'un d'autre.

**Huit mini-leçons** : la fin des mots en « é » · les couleurs de la classe ·
la consigne commence par un verbe · où se place la couleur · quand je n'ai pas
compris · demander la permission · permis, interdit · en retard, absent.

**Le jeu de rôle a demandé un scénario neuf.** Aucun scénario existant ne
convenait : `presenter` (niveau 1) s'arrête au nom, et ceux du niveau 4 tiennent
une conversation suivie. `JEU_DE_ROLE_CLASSE` a donc été ajouté à `server.py` —
trois cas (« je n'ai pas compris », « est-ce que je peux ? », « demain, je suis
absent »), deux rôles, `moi` et `enseignante`, et une conduite qui impose une
consigne à la fois et, surtout, de **répéter les mêmes mots plus lentement**
plutôt que de reformuler : reformuler donnerait à l'élève une deuxième phrase
inconnue à comprendre.

**Médias.** 18 images (0,61 $) et 280 extraits audio (51 répliques sur six
dialogues, 229 mots et phrases), sans un seul échec réseau. Tariq prend la voix
masculine, Myriam la voix féminine 2, madame Leduc celle de l'enseignante
ralentie à 0,85 — c'est elle qui donne toutes les consignes, et une consigne
mal entendue fait rater l'exercice entier.

**La difficulté propre à ce module est qu'une vraie salle de classe est pleine
de texte** — au tableau, sur les cahiers, sur l'avis affiché — alors que le
générateur a l'ordre de ne produire aucun mot lisible. Les prompts demandent
donc des traces d'effacement grises, des pages lignées vides, des lignes
d'écriture qui « se lisent comme des traits gris flous ». Deuxième difficulté,
plus insidieuse : dix-huit images de la même pièce se ressemblent. Chaque
prompt change donc de distance — le gros plan sur un objet posé, le pupitre vu
de trois quarts, la salle vue du fond, la porte vue du corridor.

**Huit séances.** 88 diapositives, 65 blocs de fiches. A2 est la séance de
graphie-phonie et porte sur la terminaison **-ez**, qui se dit « é » : toutes
les consignes de la classe finissent ainsi, et le z muet est l'erreur la plus
audible du niveau. B2 porte le premier accord du programme — la couleur après
l'objet, et son -e au féminin — que C2 réutilise aussitôt pour « absent /
absente ». C2 est la séance de compréhension écrite, bâtie sur l'avis affiché
près de la porte, avec la consigne d'apporter le vrai avis du centre.

**Le relevé des sons s'est fait sans `build/collecte_sons.py`**, et c'est la
seule chose neuve de cette production. Le script n'a **jamais** été lancé :
`build/releve_sons.js`, écrit ici, reproduit hors navigateur les trois endroits
du gabarit qui appellent `playWord`. Il a été validé en le rejouant sur
`module-n2-bonjour`, dont il rend les 164 clés **et leurs valeurs** à l'octet
près. Plus de port à surveiller, plus de collecteur oublié en tâche de fond,
plus de relevé qui part écraser le fichier de sons d'un autre module.

**Un piège de déploiement, à connaître.** Après le `git push`, le HTML du
module a été servi par Railway **plusieurs minutes avant ses médias** : la page
se chargeait, et les 301 images et MP3 répondaient tous 404. Ce n'est pas une
synchronisation cassée, c'est le volume qui n'a pas fini de se remplir — ici,
un peu plus de trois minutes. Vérifier en boucle sur un seul fichier plutôt que
de conclure trop vite :

    for i in $(seq 1 20); do curl -s -o /dev/null -w "%{http_code}\n" <url>; sleep 25; done

**Originalité : 4,2 %.** Sur les 120 énoncés visibles par l'élève, cinq se
retrouvent tels quels dans un autre module du dépôt, et ce sont les cinq
consignes génériques qu'on attendait : « Écoute de nouveau le dialogue, puis
réponds », « Glisse chaque photo sur la phrase qui la décrit », « Le mot et sa
définition ». Sous le seuil de 5 % de `docs/verification-originalite.md`, et
aucun contenu narratif en commun.

**Les six contrôles** passent pour ce module. `sommaire.py --verifier` signale
encore `module-n3-restaurant` (activité 77), produit au même moment par une
session voisine : ce n'est pas un écart de celui-ci.
