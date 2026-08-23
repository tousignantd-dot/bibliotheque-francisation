const FC_CARDS = [
  // Seize mots, quatre par section. C'est la seule liste de mots du module :
  // « Je retiens des mots », ses cartes mémoire et l'exercice `prVocab` en
  // dérivent tous.
  //
  // Le savoir lexical que le programme rattache à cette situation, au
  // niveau 7, tient en trois points : « phrases clés pour se présenter,
  // exposer le motif de l'appel et mettre fin à une conversation
  // téléphonique » ; « vocabulaire en rapport avec les objectifs de
  // formation : choix de cours, motivation, profil, plan de carrière » ;
  // « vocabulaire en rapport avec la rédaction d'une lettre : présentation,
  // formules de courtoisie ». Les seize mots ci-dessous en sortent, et rien
  // d'autre ne les a décidés.
  //
  // **Trois cartes seulement portent une image.** Le vocabulaire de
  // l'admission est administratif — un préalable, une aptitude, un rang, une
  // reconnaissance des acquis ne se photographient pas. Leur donner une photo
  // reviendrait à mettre derrière chaque mot une vue générique de secrétariat
  // d'école, c'est-à-dire le thème du module à la place de ce que dit la
  // carte. Les trois retenues montrent un objet ou un lieu réel, décrit par la
  // phrase d'exemple de la carte elle-même.

  // ── Je découvre : ce qui décide qui entre ──
  {word:"un préalable",
   def:"Le cours ou le niveau qu'il faut avoir réussi avant d'être admis à une formation.",
   ex:"Il lui manque un seul <strong>préalable</strong> : les mathématiques de quatrième secondaire.",
   tache:"prep"},

  {word:"un programme contingenté",
   def:"Une formation où il y a plus de personnes qui demandent que de places offertes.",
   ex:"Le programme est <strong>contingenté</strong> : soixante-huit demandes pour vingt-quatre places.",
   tache:"prep"},

  {word:"une entrevue de sélection",
   def:"La rencontre où l'établissement décide qui il retient parmi les personnes qui ont posé leur candidature.",
   ex:"Son <strong>entrevue de sélection</strong> est fixée au mardi matin, à neuf heures quinze.",
   img:"/assets/interactive/module-n7-etablissement/vocab/entrevue-de-selection.jpg",
   tache:"prep"},

  {word:"un relevé de notes",
   def:"Le document officiel qui montre les cours suivis et les résultats obtenus.",
   ex:"Son <strong>relevé de notes</strong> de Syrie est traduit, mais il ne dit rien au comité.",
   tache:"prep"},

  // ── Défi 1 : le dossier et la lettre ──
  {word:"un dossier de candidature",
   def:"L'ensemble des documents qu'une personne dépose pour demander une place.",
   ex:"Son <strong>dossier de candidature</strong> est complet depuis le douze février.",
   tache:"t1"},

  {word:"une lettre de motivation",
   def:"La lettre où l'on explique pourquoi on veut suivre une formation et ce qu'on y apporte.",
   ex:"Sa première <strong>lettre de motivation</strong> disait ce qu'elle voulait, jamais pourquoi elle.",
   tache:"t1"},

  {word:"une pièce justificative",
   def:"Le papier qui prouve ce qu'on avance : un diplôme, une attestation, un contrat.",
   ex:"L'attestation de son employeur est la <strong>pièce justificative</strong> qui manquait au dossier.",
   img:"/assets/interactive/module-n7-etablissement/vocab/piece-justificative.jpg",
   tache:"t1"},

  {word:"une formule de courtoisie",
   def:"La phrase toute faite qui ouvre ou qui ferme une lettre formelle.",
   ex:"Une <strong>formule de courtoisie</strong> mal choisie se remarque plus qu'une phrase maladroite.",
   tache:"t1"},

  // ── Défi 2 : l'entrevue ──
  {word:"un comité de sélection",
   def:"Le petit groupe de personnes qui reçoit les candidats et qui classe les dossiers.",
   ex:"Le <strong>comité de sélection</strong> est composé du conseiller et d'un enseignant du programme.",
   tache:"t2"},

  {word:"un plan de carrière",
   def:"Ce qu'une personne veut faire dans son métier dans les prochaines années, et par quelles étapes.",
   ex:"Son <strong>plan de carrière</strong> tient en deux phrases : le diplôme, puis le permis de pratique.",
   tache:"t2"},

  {word:"une aptitude",
   def:"Ce qu'une personne est capable de faire, en dehors de ce qu'un diplôme atteste.",
   ex:"Rester calme devant une personne qui crie est une <strong>aptitude</strong>, pas un trait de caractère.",
   tache:"t2"},

  {word:"un stage",
   def:"La période de la formation qui se passe en milieu de travail plutôt qu'en classe.",
   ex:"Le <strong>stage</strong> se fait dans un établissement de la région, à raison de quatre jours par semaine.",
   img:"/assets/interactive/module-n7-etablissement/vocab/stage.jpg",
   tache:"t2"},

  // ── Défi 3 : le suivi ──
  {word:"une liste d'attente",
   def:"Le classement des personnes retenues qui n'ont pas eu de place, dans l'ordre où elles seraient appelées.",
   ex:"Elle est sur la <strong>liste d'attente</strong>, et personne ne lui dit à quel rang.",
   tache:"t3"},

  {word:"un rang",
   def:"La position d'une personne dans un classement : première, deuxième, quatrième.",
   ex:"Son <strong>rang</strong> ne change pas tout seul : il change quand quelqu'un se désiste.",
   tache:"t3"},

  {word:"une mise à niveau",
   def:"Le cours court qu'on suit pour atteindre le niveau exigé avant une formation.",
   ex:"Une <strong>mise à niveau</strong> de vingt-cinq heures suffirait pour son préalable manquant.",
   tache:"t3"},

  {word:"la reconnaissance des acquis",
   def:"La démarche par laquelle un établissement évalue ce qu'une personne sait déjà faire, appris ailleurs qu'à l'école.",
   ex:"Cinq ans comme préposée peuvent compter, mais seulement par la <strong>reconnaissance des acquis</strong>.",
   tache:"t3"},
];
