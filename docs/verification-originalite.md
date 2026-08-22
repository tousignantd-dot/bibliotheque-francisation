# Relevé d'originalité des modules

Mesure produite le **20 août 2026** par
`~/.claude/skills/module-parite/scripts/verifier_copie.py`, qui compare les
énoncés visibles par l'élève (`EXOS`) de la version actuelle au plus ancien
état du fichier dans l'historique git — c'est-à-dire au contenu dérivé de la
Collection Connexion (SOFAD) d'avant la réécriture.

Seuils du vérificateur : 🟢 < 10 %, 🟠 10–20 %, 🔴 ≥ 20 %.

| Module | Énoncés | Identiques | % | Verdict |
|---|---|---|---|---|
| module-consultation | 94 | 0 | 0 % | 🟢 |
| module-sante | 24 | 0 | 0 % | 🟢 |
| module-meteo | 90 | 0 | 0 % | 🟢 |
| module-pub | 71 | 0 | 0 % | 🟢 |
| module-logement | 86 | 0 | 0 % | 🟢 |
| module-banque | 101 | 0 | 0 % | 🟢 |
| module-urgence | 98 | 1 | 1 % | 🟢 |
| module-procedure | 71 | 1 | 1 % | 🟢 |
| module-probleme | 141 | 2 | 1 % | 🟢 |
| module-nouvelles | 85 | 5 | 6 % | 🟢 |
| module-travail | 110 | 12 | 11 % | 🟠 |

## Nature des coïncidences

Elles ont été relevées une à une, pas seulement comptées. La quasi-totalité
sont des **consignes génériques** d'exercice, pas du contenu narratif :
« Qui appelle qui ? », « Quel est le but de l'appel ? », « La formule de
politesse », « Qui ? (les personnes concernées) ». Ce sont les formes
standard d'un exercice de compréhension orale, imposées par le type de tâche
et par le vocabulaire du programme ministériel.

Deux exceptions notées :

- `module-nouvelles` — une question porte sur une expression précise du texte
  source (« un franc succès »). À reformuler à la prochaine touche.
- `module-probleme` — deux phrases de contenu banales (« Le robinet de la
  cuisine coule depuis deux jours. »), sur 141 énoncés.

## Suite

- `module-travail` : varier les 12 consignes pour descendre sous 5 %. Aucune
  urgence, mais à faire avant une éventuelle diffusion élargie.
- **Les modules produits à partir de maintenant ne sont plus des réécritures.**
  Ils sont écrits à partir de `~/Claude/programme/programme-francisation.json`
  — le programme d'études officiel du MEQ — sans source antérieure. Le
  vérificateur n'a plus d'objet pour eux : il n'existe pas de version d'origine
  à laquelle les comparer.

## Les modules neufs, mesurés autrement

Faute de version d'origine, un module écrit à partir du programme se mesure à
ses voisins : combien de ses énoncés visibles se retrouvent mot pour mot dans
un autre module du dépôt. Le seuil reste 5 %.

| Module | Énoncés | Communs | % | Nature |
|---|---|---|---|---|
| module-n6-recherche | 209 | 4 | 1,9 % | quatre consignes du gabarit |

Les quatre : « Le mot et sa définition », « Choisissez un mot, puis sa
définition. Six mots à la fois. », « Écoutez de nouveau le dialogue, puis
répondez. », « Glissez chaque photo sur la phrase qui la décrit. » Ce sont les
consignes que le moteur impose à ses types d'exercice — les faire varier pour
elles-mêmes nuirait à l'élève, qui les reconnaît d'un module à l'autre.

## Les modules neufs — mesure du 21 août 2026

Un module produit à partir du programme n'a **aucun antécédent SOFAD** : le
vérificateur de réécriture ne s'y applique pas, puisqu'il compare au plus
ancien état du fichier dans git — qui est déjà la version neuve. Le risque
change de nature : ce n'est plus la copie, c'est la **coïncidence avec les
modules déjà écrits**, sur les consignes génériques que le type de tâche
impose (« Écoutez de nouveau le dialogue, puis répondez. »).

La mesure est donc l'autre : on compare les énoncés visibles par l'élève
(`txt:` et `q:` de `exos.js`) à ceux de **tous** les autres modules générés.

| Module | Énoncés | Identiques ailleurs | % | Verdict |
|---|---|---|---|---|
| module-n5-logement | 162 | 0 | 0 % | 🟢 |
| module-n5-rendezvous | 136 | 0 | 0 % | 🟢 |
| module-n5-urgence | 283 | 0 | 0 % | 🟢 |

Comparé aux 1 949 énoncés des quatorze autres modules de `build/contenu/`.
Les consignes courtes (« Écoutez de nouveau le dialogue, puis répondez. »)
sont sous le seuil de longueur du relevé — elles se répètent d'un module à
l'autre et c'est voulu : une consigne d'exercice n'a pas à être originale, et
la varier pour la varier nuirait à l'élève, qui la reconnaît d'un module au
suivant.

`module-n5-rendezvous` (activité 65), mesuré le 21 août 2026 : ses 136 énoncés
visibles de 25 caractères ou plus ont été comparés aux 2 618 des vingt-deux
autres modules de `build/contenu/`. Aucun n'est identique. La situation du
programme ne fournissant aucun lexique, les seize mots du banc sont eux aussi
composés à partir des savoirs du niveau.

`module-n5-urgence` (activité 66), mesuré le 21 août 2026 : ses 283 énoncés
visibles de plus de douze caractères — consignes, titres d'exercices, intitulés
de bandeau noir compris, donc un relevé plus sévère que celui du module
précédent — ont été comparés aux 6 001 des vingt-trois autres modules de
`build/contenu/`. Première mesure : 16 identiques, soit 5,7 %, toutes des
consignes génériques (« Le mot et sa définition », « Écoutez le dialogue du
Défi 1, puis répondez. ») ou des intitulés de règle (« La forme négative »).
Elles ont été reformulées avec les mots du module — « Réécoutez l'appel de deux
heures du matin, puis répondez. » — ce qui ramène la mesure à **0 identique**.

L'opération est sans risque à condition de vérifier une chose : ni les `sub` ni
les `tit` d'un exercice n'entrent dans le relevé des sons. Le manifeste des 183
extraits est resté identique avant et après, donc aucun MP3 n'a été à refaire.

`module-n3-loisirs` (activité 85), mesuré le 22 août 2026 : ses **148** énoncés
visibles de plus de vingt-cinq caractères — les tuiles des Vrai/Faux, les deux
colonnes des appariements et les phrases à trous — ont été comparés aux **5 807**
des **quarante-quatre** autres modules de `build/contenu/`. **Aucun n'est
identique.**

La situation « Participation à une activité culturelle ou sportive » ne fournit
aucun lexique au niveau 3 : le programme ne donne, pour elle, que quatre points
de savoir — les types de loisirs, les noms d'activités, les outils de cuisine
(bol, tasse à mesurer, poêle, casserole) et les abréviations utiles. Les seize
mots du banc sont composés à partir de là, et le scénario — Marisol, Camila,
Thierry, Roxane, Denis, le centre de la rue Galt — est inventé de bout en bout.

`module-n3-restaurant` (activité 77), mesuré le 21 août 2026 : ses **139**
énoncés visibles de plus de vingt-cinq caractères ont été comparés à ceux des
vingt-cinq autres modules de `build/contenu/`. **Aucun n'est identique.**

Le relevé large — 225 chaînes, consignes, titres d'exercices et mots du banc
compris — rend 17 coïncidences, soit 7,6 %. Elles ont été regardées une à une :
ce sont les six consignes que le moteur impose à ses types d'exercice
(« Le mot et sa définition », « Écoute de nouveau le dialogue, puis
réponds. », « Glisse chaque photo sur la phrase qui la décrit. »,
« Complète avec « ce », « cet », « cette » ou « ces ». »…) et **quatre mots du
lexique** — *la caisse*, *un accompagnement*, *le poulet*, *une minute* — qui
appartiennent au programme et qu'on ne va pas renommer pour éviter un doublon.
Rien de narratif, aucun énoncé de contenu.

La leçon de `module-n5-urgence` tient toujours : reformuler une consigne avec
les mots du module est sans risque, puisque ni les `sub` ni les `tit` n'entrent
dans le relevé des sons. Ici, elle n'a pas été appliquée aux quatre mots de
lexique — les renommer aurait éloigné le module du programme, qui est la seule
source.

`module-n5-travail` (activité 67), mesuré le 21 août 2026 : ses **203** énoncés
visibles de plus de douze caractères — `txt`, `q`, `a`, `sub` et `tit`, donc le
relevé large — ont été comparés aux 4 687 des vingt-six autres modules de
`build/contenu/`. Première mesure : **3 identiques, soit 1,5 %**, toutes des
consignes que le moteur impose à ses types d'exercice (« Chaque mot, sa
définition », « Prenez un mot, puis glissez dessus la définition qui lui va »,
« Faites glisser chaque photo vers la phrase qui lui correspond »). Elles ont
été reformulées avec les mots du module — « Les seize mots du poste »,
« Prenez un mot du bureau… », « Faites glisser chaque photo du bureau vers la
phrase qui la décrit » — ce qui ramène la mesure à **0 identique**.

La leçon de `module-n5-urgence` a été appliquée dans l'ordre qu'elle recommande :
**le contrôle d'originalité passe avant la génération des MP3, pas après.** Les
trois reformulations ne touchent que des `sub` et des `tit`, qui n'entrent pas
dans le relevé des sons ; aucun extrait n'a été payé puis jeté.

`module-n2-couloirs` (activité 90), mesuré le 21 août 2026 : ses énoncés
visibles de plus de douze caractères — `txt`, `q`, `a`, `sub`, `tit`, plus les
mots et définitions du banc, donc le relevé large — ont été comparés à ceux des
vingt-huit autres modules de `build/contenu/`. Première mesure : **6 identiques
sur 113, soit 5,3 %**, toutes des consignes que le moteur impose à ses types
d'exercice (« Le mot et sa définition », « Écoute de nouveau le dialogue, puis
réponds. », « Glisse chaque photo sur la phrase qui la décrit. »). Reformulées
avec les mots du module — « Réécoute Soraya et Gilles dans le corridor, puis
réponds. », « Les seize mots du centre » —, la mesure retombe à **0 identique
sur 117**.

La mesure a été faite **avant** la génération des MP3, comme la nuit du 21 août
l'a établi : les 205 clés du relevé des sons sont restées identiques après
reformulation, puisque ni les `sub` ni les `tit` n'y entrent. Aucun extrait
n'a été payé deux fois.

`module-n3-pharmacie` (activité 78), mesuré le 21 août 2026 : ses **228**
énoncés visibles de plus de douze caractères — `txt`, `q`, `a`, `sub` et `tit`,
donc le relevé large — ont été comparés aux 6 312 des vingt-huit autres modules
de `build/contenu/`. Première mesure : **17 identiques, soit 7,5 %**, toutes
des consignes ou des titres que le moteur impose à ses types d'exercice (« Le
mot et sa définition », « Écoute de nouveau le dialogue, puis réponds. »,
« Glisse chaque photo sur la phrase qui la décrit. ») — plus quatre mots du
lexique. Dix reformulations avec les mots du module — « Les seize mots de la
pharmacie », « Réécoute la scène du renouvellement, puis réponds. », « Fais
glisser chaque photo de la pharmacie vers la phrase qui la décrit » — ramènent
la mesure à **4 identiques, soit 1,8 %**.

Les quatre qui restent sont des **mots du lexique du programme** — *une
ordonnance*, *la carte d'assurance maladie*, *une étiquette* — que
`module-n5-rendezvous` et `module-alimentation` emploient aussi. Les renommer
éloignerait le module du programme, qui est sa seule source. Rien de narratif,
aucun énoncé de contenu.

Le contrôle a été fait **avant la génération des MP3**, et les reformulations
ne touchent que des `sub` et des `tit`, qui n'entrent pas dans le relevé des
sons : les 231 clés de `sons_module_n3_pharmacie.json` sont restées les mêmes
avant et après.

`module-n5-voisinage` (activité 68), mesuré le 21 août 2026 : ses **202**
énoncés visibles de plus de douze caractères — `txt`, `q`, `a`, `sub` et `tit`,
donc le relevé large — ont été comparés aux 4 969 des vingt-neuf autres modules
de `build/contenu/`. Première mesure : **2 identiques, soit 1,0 %**, toutes deux
des consignes que le type d'exercice impose (« Complétez avec le mot juste.
Écrivez le mot seul, sans article. » et « Mettez le verbe entre parenthèses au
futur simple. »). Elles ont été reformulées avec les mots du module —
« Complétez avec le mot de l'immeuble qui convient. » et « Chaque phrase est une
promesse : mettez le verbe entre parenthèses au futur simple. » — ce qui ramène
la mesure à **0 identique**.

Mesure faite **avant** la génération des MP3, comme la leçon de
`module-n5-urgence` le demande. Les deux reformulations ne touchent que des
`sub`, qui n'entrent pas dans le relevé des sons : le manifeste des 190 extraits
est resté identique avant et après.

`module-n3-poste` (activité 80), mesuré le 21 août 2026, **avant la génération
du moindre MP3** : ses **307** énoncés visibles de plus de douze caractères —
`txt`, `q`, `a`, `sub`, `tit`, les intitulés et les explications des bandeaux
`savoir`, plus les mots et définitions du banc, donc le relevé large — ont été
comparés aux 10 650 des trente autres modules de `build/contenu/`. Première
mesure : **9 identiques, soit 2,9 %**, déjà sous le seuil. Toutes des
**intitulés de bandeau** : les cinq lignes de la leçon sur « ce, cet, cette,
ces », que `module-n3-restaurant` porte mot pour mot parce que la grammaire est
la même, plus « Demander le prix », « Demander la permission », « La place du
petit mot » et la formule « Merci beaucoup. Bonne journée. ».

Huit reformulations avec les mots du module — « Le carton, le colis, le reçu :
ce », « La boîte, l'enveloppe, la lettre : cette », « Demander le prix de
l'envoi » — ramènent la mesure à **1 identique sur 307, soit 0,3 %**.

Le dernier est « Merci beaucoup. Bonne journée. », et il reste **exprès** :
c'est une formule de politesse figée, elle est la bonne réponse d'un exercice
d'écoute (`t1qui`), et à ce titre elle porte un extrait audio. La reformuler
changerait une clé du relevé des sons sans rien améliorer.

Le point de méthode, une fois de plus vérifié : le relevé des **244** clés de
`sons_module_n3_poste.json` est identique à l'octet avant et après les huit
reformulations. Ni les `sub`, ni les `tit`, ni les intitulés de bandeau
n'entrent dans le manifeste audio — seules les listes `savoir[…][2]` et les
`txt` des exercices à cartes y entrent. Reformuler une consigne ou un intitulé
est donc gratuit ; reformuler la réponse d'un exercice d'écoute ne l'est pas.

`module-n3-loyer` (activité 81), mesuré le 21 août 2026, **avant tout média** :
ses **212** énoncés visibles de plus de douze caractères — `txt`, `q`, `a`,
`sub` et `tit`, donc le relevé large — ont été comparés aux **7 153** des
trente-sept autres modules de `build/contenu/`. Première mesure :
**6 identiques, soit 2,8 %**, déjà sous le seuil.

Quatre ont été reformulés avec les mots du module : deux consignes que le
moteur impose à ses types d'exercice (« Réécoute la conversation dans le
corridor, puis réponds. », « Lis chaque phrase et dis si elle est vraie ou
fausse. »), un titre de vrai-ou-faux (« Vrai ou Faux — Je vous appelle pour
l'annonce », que `module-n5-logement` portait déjà) et **une phrase de
contenu** — « Le logement est libre le premier juillet. » — que le même voisin
portait mot pour mot. Elle est devenue « On peut emménager à partir du premier
juillet. » La mesure tombe à **2 identiques sur 212, soit 0,9 %**.

Les deux qui restent sont des **entrées du lexique du programme** : « un quatre
et demie » et « chauffé et éclairé ». Elles sont communes à
`module-n5-logement` parce que le programme les rattache à la même situation
aux deux niveaux. Les renommer éloignerait le module de sa seule source, comme
pour les quatre mots de `module-n3-restaurant`.

Le point de méthode tient une fois de plus, et il a été vérifié par `diff` :
les 224 clés de `sons_module_n3_loyer.json` sont identiques avant et après les
quatre reformulations. La ligne de contenu touchée appartient à un `vf` **sans
cartes écoutables** — seuls les `vf` à `cards:true, listen:true` mettent leurs
`txt` au manifeste. Vérifier ce point avant de reformuler une réponse coûte dix
secondes et évite de repayer des MP3.

`module-n2-secretaire` (activité 95), mesuré le 22 août 2026 : ses **250**
énoncés visibles de plus de douze caractères — consignes, titres d'exercices,
intitulés et rangées de bandeau noir compris — comparés aux **12 470** des
autres modules de `build/contenu/`. Première mesure : **15 identiques, 6,0 %**,
au-dessus du seuil. Onze ont été reformulés avec les mots du module (« Les
seize mots du secrétariat et des couloirs », « On entend “ou” ou on entend
“u” ? », « Le local 214 se trouve au ___ étage. »), ce qui ramène la mesure à
**4 identiques, 1,6 %** 🟢.

Les quatre qui restent sont assumés : « le secrétariat », « le
rez-de-chaussée » et « une attestation » sont des entrées du **lexique du
programme** pour cette situation — les varier serait enseigner autre chose que
ce que le ministère nomme ; « On ne dit pas » est l'intitulé de rangée que tous
les bandeaux noirs du dépôt emploient, et le faire varier nuirait à l'élève qui
le reconnaît.

Confirmation du point relevé pour `module-n5-urgence` : le relevé des sons est
resté **identique à l'octet près** avant et après les onze reformulations
(`diff` vide sur `sons_module_n2_secretaire.json`). Ni les `sub` ni les `tit`
n'entrent dans le manifeste des extraits.

---

`module-n6-emploi` (activité 100), mesuré le 22 août 2026 : ses **1 439**
énoncés visibles de 25 caractères ou plus — consignes, titres, énoncés,
rangées de bandeau, blocs de mini-leçon, répliques et intitulés de section —
comparés aux **43 192** des cinquante-trois autres modules de
`build/contenu/`. Première mesure : **60 identiques, 4,2 %**, sous le seuil,
mais la moitié venait d'un seul endroit — la mini-leçon de **graphie-phonie**,
calquée sur celle du module pilote du niveau, `module-n6-actualite`.

C'est le cas de figure que la vague 6 va rencontrer huit fois : le savoir
(« ch » qui se dit k, « x » qui se dit s, « sh » et « sch » qui se disent ch)
est **commun à tout le niveau 6**, donc les huit modules porteront la même
mini-leçon. Le savoir est commun ; les phrases qui l'expliquent n'ont aucune
raison de l'être. Une quarantaine de tournures ont été réécrites — titres de
cas, notes de laboratoire, pièges, questions de vérification — ce qui ramène
la mesure à **11 identiques, 0,8 %** 🟢.

Ce qui reste est assumé, et c'est la même liste qu'ailleurs : les consignes que
le moteur impose à ses types d'exercice (« Choisis un mot, puis sa
définition. Six mots à la fois. », « Glisse chaque photo sur la phrase qui la
décrit. », « glisse la description ici »), les intitulés de bloc de mini-leçon
que tous les modules emploient (« Est-ce que c'est clair maintenant ? »,
« Quatre questions rapides. ») et la phrase d'accueil de « Je retiens des
mots ». Les faire varier pour elles-mêmes nuirait à l'élève, qui les reconnaît
d'un module au suivant.

Troisième confirmation du même point : le relevé des sons est resté
**identique à l'octet près** avant et après les réécritures
(`git diff` vide sur `sons_module_n6_emploi.json`, 206 clés). Ni les `sub`, ni
les `tit`, ni les `note` d'un bloc de mini-leçon n'entrent dans le manifeste
des extraits — seuls les `say` y entrent, et aucun n'a été touché.

`module-n6-habitation` (activité 106), mesuré le 22 août 2026 : ses **460**
énoncés visibles de plus de douze caractères — consignes, titres d'exercices,
intitulés de bandeau, paragraphes des exercices `texte` et cartes de
vocabulaire compris — ont été comparés aux **18 937** des **cinquante-sept**
autres modules de `build/contenu/`. Première mesure : 19 identiques, soit
**4,1 %** — sous le seuil, et pourtant à corriger.

**Le total ne disait pas l'essentiel.** Neuf des dix-neuf coïncidences venaient
d'un seul endroit : la mini-leçon de formation des mots, écrite avec les mêmes
intitulés de rangée que celle de `module-n6-emploi` (« Le verbe donne le nom en
-age », « Le verbe donne l'adjectif en -able », « Le préfixe dé- ou dés-
défait »). Le savoir est commun au niveau 6 — tous ses modules le portent — mais
la formulation, elle, doit être refaite. Réécrits en partant du chantier plutôt
que de la grammaire (« Ce qu'on fait devient un -age », « Ce qu'on peut faire
devient -able »), ils ramènent l'ensemble à **5 identiques, soit 1,1 %**.

Les cinq qui restent sont les consignes que le moteur impose à ses types
d'exercice (« Le mot et sa définition », « Choisis un mot, puis sa définition.
Six mots à la fois. », « Glisse chaque photo sur la phrase qui la décrit. ») et
deux intitulés de rangée de trois mots. Elles ne se corrigent pas : les faire
varier pour elles-mêmes nuirait à l'élève, qui les reconnaît d'un module à
l'autre.

L'opération est sans risque, et la vérification à faire est toujours la même :
ni les `sub`, ni les `tit`, ni les intitulés d'un bandeau `savoir` sans
`speak:true` n'entrent dans le relevé des sons. Le manifeste des **258**
extraits est resté identique avant et après, donc aucun MP3 n'était à refaire.
---

`module-n6-logement` (activité 105), mesuré le 22 août 2026 : ses **1 216**
énoncés visibles de 25 caractères ou plus, comparés aux **49 021** des
cinquante-sept autres modules de `build/contenu/`. Première mesure : **25
identiques, 2,0 %** 🟢 — bien sous le seuil, et sans point chaud : aucune
mini-leçon n'avait été bâtie sur celle d'un voisin, et les coïncidences se
répartissaient sur onze modules différents.

Ce qui les produisait était plus discret que le cas du module 100 : non pas une
leçon recopiée, mais **vingt titres courts que le savoir commun appelle tout
seul** — « Les terminaisons de la 3e personne », « Trois verbes irréguliers à
connaître », « Deux passés dans la même phrase », « Le subjonctif après un verbe
introducteur », « Poser une condition avec si ». Aucun n'a été emprunté ; chacun
est simplement la façon la plus évidente de nommer la chose, et cinq agents
successifs y arrivent séparément. Les vingt ont été refaits : la mesure tombe à
**4 identiques, 0,3 %** 🟢.

Les quatre qui restent sont ceux de toute la série et sont assumés : les trois
consignes que le moteur impose à ses types d'exercice (« Choisissez un mot, puis
sa définition. Six mots à la fois. », « Glissez chaque photo sur la phrase qui
la décrit. », « glissez la définition ici ») et la phrase d'accueil de « Je
retiens des mots ». Les faire varier nuirait à l'élève, qui les reconnaît d'un
module au suivant.

Quatrième confirmation du même point : le relevé des sons est resté **identique
à l'octet près** avant et après les vingt réécritures (`diff` vide sur
`sons_module_n6_logement.json`, 201 clés). Ni les `tit`, ni les `sub`, ni les
intitulés de rangée d'un bandeau n'entrent dans le manifeste des extraits.
`module-n6-sante` (activité 104), mesuré le 22 août 2026 : ses **1 590**
énoncés visibles de vingt-cinq caractères ou plus — consignes, titres
d'exercices, intitulés et cellules de bandeau noir, blocs de mini-leçon,
paragraphes des exercices `texte`, définitions et exemples du banc, textes des
sections et répliques des dialogues compris, donc le relevé le plus large des
modules mesurés jusqu'ici — ont été comparés aux **49 021** des
**cinquante-sept** autres modules de `build/contenu/`. **10 identiques, soit
0,6 %.**

Le chemin y menant est la vraie leçon. La **première** mesure donnait 55
identiques, soit 3,5 % : sous le seuil, donc silencieuse. Mais **vingt-cinq
d'entre elles venaient d'un seul bloc** — la mini-leçon de graphie-phonie,
écrite en s'appuyant sur celle d'un module voisin. C'est exactement ce que
l'activité 100 avait signalé et que ce fichier consigne depuis : *mesurer par
module ne suffit pas, il faut regarder d'où viennent les coïncidences.* Un
seuil global respecté peut cacher un quasi-doublon sur une leçon entière.

La mini-leçon a été réécrite depuis la situation du module — le mot entendu
dans un corridor d'hôpital, les noms d'examens et de spécialités —, et une
quinzaine d'intitulés de bandeau et de bloc reformulés. Résultat : 0,6 %.

Les dix coïncidences restantes ont été regardées une à une, et aucune ne se
corrige :

- **deux consignes que le moteur impose** à ses types d'exercice (« Choisis un
  mot, puis va chercher sa définition dans le banc. Six à la fois. »,
  « Choisis une question, puis clique dans le texte le passage qui y
  répond. » — cette dernière est la forme canonique du type `texte`, écrite
  dans `CLAUDE.md`) ;
- **deux étiquettes de banc de réponses** (« Ce qu'on dirait à voix haute »,
  « glisse l'équivalent parlé ici ») ;
- **un terme du programme** (« la carte d'assurance maladie ») ;
- **deux lignes de la liste sh/sch** (« un schéma, un shampoing, un short »),
  que le programme nomme lui-même et pour lesquelles il n'existe pas
  d'équivalent à substituer ;
- **trois intitulés courts** de bloc de mini-leçon.

Ce que ce module ajoute à la méthode : **la moitié du choix se maîtrise quand
même**. Les trois cas de graphie-phonie sont imposés par le programme, mais les
mots de la famille `ch` se prennent dans le champ lexical du module — une
échographie, un psychiatre, le cholestérol ici ; une psychologie, un orchestre,
une chronologie ailleurs. Seuls « six », « dix » et les trois mots en sh/sch
sont réellement contraints.

Quatrième confirmation du point sur l'audio : le relevé des sons rend **207
clés avant comme après** les réécritures. Ni les `sub`, ni les `tit`, ni les
intitulés de bandeau, ni les `note` d'un bloc de mini-leçon n'entrent dans le
manifeste des extraits — seuls les `say` y entrent, et aucun n'a été touché.
Reformuler pour l'originalité reste gratuit en audio.
