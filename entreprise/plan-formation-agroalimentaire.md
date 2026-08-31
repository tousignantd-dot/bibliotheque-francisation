# Programme de démonstration — transformation alimentaire
Chantier « formation en entreprise ». Décisions prises le 31 août 2026 :
secteur = transformation alimentaire, format = 8 blocs d'une heure.

## L'entreprise (fictive)

**Aliments Belrive inc.** — conditionnement et surgélation de légumes.
Entreprise inventée de toutes pièces pour la démonstration ; toute ressemblance
est fortuite.

- 140 employés, dont environ 90 sur le plancher
- Trois quarts : jour (6 h – 14 h), soir (14 h – 22 h), nuit (entretien et lavage)
- Cinq zones : réception, parage, ligne d'emballage, tunnel de surgélation, expédition
- Une soixantaine de travailleurs dont le français n'est pas la langue première,
  la plupart entre les niveaux 1 et 3
- Dangers réels du lieu : sol mouillé, lames, chariot élévateur, froid,
  arrêts d'urgence, cadenassage, allergènes

## Les personnages

| Personnage | Poste | Niveau | Rôle dans les dialogues |
|---|---|---|---|
| Nadia Osei | parage | 1 | l'apprenante la plus fragile ; 8 mois d'ancienneté |
| Rachid Benali | opérateur d'emballage | 2 | 3 ans d'ancienneté ; comprend mieux qu'il ne parle |
| Vitor Almeida | mécanicien d'entretien | 3 | circule partout ; sert de relais entre les zones |
| Marie-Ève Cormier | chef d'équipe, quart de jour | — | parle clairement, reformule ; alliée |
| Jean-Guy Tremblay | superviseur de plancher | — | parle vite et court ; c'est lui, la difficulté |
| Luda Savchuk | emballage, quart de soir | 2 | l'autre bout du relais de quart |

## Le format

Huit blocs d'une heure, un par semaine, **sur les heures payées**, en groupes de
8 à 12. Trois groupes permettent de couvrir les trois quarts. Salle près du
plancher, pas de devoirs à la maison.

### Ce que dure une heure

| Minutes | Étape | Ce que ça sert (Gagné / Merrill) |
|---|---|---|
| 5 | **Le moment** — l'image du problème, l'objectif de l'heure | attention, objectif |
| 10 | **On écoute** — le dialogue de l'usine, sans le texte | problème réel, démonstration |
| 15 | **Les mots** — vocabulaire imagé, banque d'énoncés | présentation du contenu |
| 20 | **On pratique** — exercices, puis micro et jeu de rôle | pratique guidée, rétroaction |
| 10 | **On emporte** — fiche de poche, défi de la semaine | intégration, transfert |

## Les huit blocs

1. **L'usine et mon poste** — se présenter, nommer les zones, dire où l'on est et
   où l'on va. Sert d'assise et de diagnostic d'entrée.
2. **La consigne : comprendre et confirmer** — recevoir une tâche en quinze
   secondes, la reformuler, confirmer un délai.
3. **La consigne : je n'ai pas compris** — faire répéter, faire ralentir,
   demander qu'on montre, dire qu'on n'y arrivera pas. Le cœur du programme.
4. **Le danger : nommer et situer** — ce qu'on voit, où c'est, à quel point c'est
   urgent.
5. **Le danger : alerter et arrêter** — crier utile, comprendre un ordre crié,
   l'arrêt d'urgence, le cadenassage.
6. **L'incident : raconter ce qui est arrivé** — le passé composé au service des
   premiers soins ; dire où l'on a mal.
7. **Le relais de quart** — ce qui est fait, ce qui reste, ce qui a mal tourné.
8. **Le visiteur et l'autre service** — accueillir, faire répéter sans vexer,
   aller chercher quelqu'un. Puis bilan et diagnostic de sortie.

**Arbitrage assumé :** dans une usine, la situation « client » ne vaut qu'un seul
bloc. Dans un commerce ou une résidence, elle en vaudrait trois et la sécurité un
seul. Le programme est un gabarit à pondérer par secteur, pas une liste figée.

## Le transfert : le défi de la semaine

Chaque bloc se termine par **une seule chose à faire au poste** avant le bloc
suivant (« cette semaine, tu demandes une fois à Jean-Guy de répéter plus
lentement »). Le chef d'équipe la coche sur une fiche d'une page. C'est le seul
dispositif du programme qui produise du Kirkpatrick niveau 3.

## La mesure

| Niveau | Ce qu'on mesure | Comment | Quand |
|---|---|---|---|
| 1 Réaction | trois questions | au bloc 8 | fin |
| 2 Apprentissage | diagnostic d'entrée et de sortie | l'outil le fait déjà | blocs 1 et 8 |
| 3 Comportement | huit observations du chef d'équipe | grille d'une page | avant, et 3 mois après |
| 4 Résultats | incidents déclarés, reprises de lot, durée de formation d'un nouvel employé, roulement | chiffres de l'employeur | 12 mois |

**Honnêteté sur le niveau 4 :** on mesure une tendance, on ne prouve pas une
cause. Le dire avant que le client le demande vaut mieux que promettre un
retour sur investissement chiffré qu'on ne pourra pas défendre.

## Avant les huit blocs : l'analyse

Une demi-journée à l'usine, offerte ou facturée séparément : tournée de plancher,
cinq entrevues courtes (deux travailleurs, deux chefs d'équipe, le responsable
SST), et relevé des affiches et consignes existantes. C'est la phase A d'ADDIE, et
c'est ce qui permet de remplacer Belrive par leur vraie usine.

## La langue d'appui

Exigence ajoutée le 31 août 2026. En entreprise, l'obstacle n'est pas seulement le
français à apprendre, c'est le français **de la consigne qui explique l'exercice**.

### Trois couches à ne pas confondre

| Couche | Exemples | Bascule ? |
|---|---|---|
| 1. Le contenu à apprendre | dialogues, audio, énoncés à dire, vocabulaire visé | **Jamais** — c'est le produit |
| 2. La langue d'appui | consignes, boutons, titres, explications, corrections, fiche de poche | **Oui** — fr / es / en, extensible |
| 3. La traduction ponctuelle | « ce mot veut dire quoi ? » | **Existe déjà** — 11 langues, à la demande |

### Ce qui existe

`build/gabarit/vocab.js` porte déjà la couche 3 : onze langues (ar, es, uk, fa, zh,
pt, en, ro, ur, ru, ti), choix unique mémorisé sous `francisation-langue`, cache
des traductions sous `francisation-traductions`, appel serveur `/api/vocab/translate`,
RTL géré. Rien à refaire.

### Ce qui manque : la couche 2

**Route retenue : un fichier de langue écrit et relu d'avance** (`langues/es.json`,
`langues/en.json`), pas de traduction à la volée.

Deux raisons de refuser la volée pour les consignes :
1. Une consigne de sécurité mal traduite dans une usine n'est pas un défaut
   d'affichage. Aux blocs 4 à 6, c'est disqualifiant.
2. Le **mode sans assistance** (`build/greffe_sans_ia.py`) retire déjà « Voir dans
   ma langue ». Un employeur qui refuse l'assistant perdrait la langue d'appui,
   c'est-à-dire exactement ce qu'il a acheté.

Ajouter une langue = un fichier + une relecture, pas une reprise du module.

### Les règles

- L'audio ne bascule jamais : on n'enregistre pas les dialogues en espagnol.
- Le français reste visible en mode espagnol ; l'appui va **sous** le français,
  jamais à sa place.
- Un seul choix pour tout : réutiliser la clé `francisation-langue` du vocabulaire.
- L'employeur peut poser une langue par défaut au groupe ; chacun peut la changer.
- La fiche de poche devient bilingue — c'est l'objet qui reste dans la poche du
  sarrau, et celui que le patron regarde en premier.

### Le test

Trois langues sur le bloc de démonstration : **français, espagnol, anglais**.
Si la bascule tient sur ces trois-là, elle tiendra sur les onze autres.

## Reste à trancher

- Le prix, et si l'analyse est offerte ou facturée.
- À qui l'on parle en premier : l'employeur directement (hypothèse retenue faute
  de réponse) ou les programmes de subvention.
- Si la démo couvre un bloc complet ou deux blocs partiels.
- L'étendue de la couche 2 : le bloc de démo seulement, ou tout le gabarit
  (les 87 modules en profiteraient, mais c'est un autre chantier).
