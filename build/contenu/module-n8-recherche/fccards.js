const FC_CARDS = [
// Seize mots, et seulement cinq portent une image.
//
// C'est un choix, pas un oubli : le lexique d'un processus de sélection est
// abstrait — une présélection, un échelon, un motif, une contrepartie. Donner
// une photo aux onze autres aurait mis derrière chaque carte une vue générique
// de salle de réunion, c'est-à-dire le thème du module à la place de ce que dit
// la carte. C'est le quatrième défaut de la relecture du 22 août 2026, et
// `module-n7-banque` avait déjà tranché dans le même sens. Le poids visuel du
// module est porté par les deux `imgmatch`, dont les énoncés sont des scènes.
  {word:"un processus de sélection",
   def:"L'ensemble des étapes qu'un employeur fait franchir avant de choisir quelqu'un.",
   ex:"Le <strong>processus de sélection</strong> de Boréalis comporte trois étapes étalées sur deux semaines.",
   tache:'prep'},

  {word:"la présélection",
   def:"Le premier tri, souvent fait par téléphone, avant les vraies rencontres.",
   ex:"L'appel de <strong>présélection</strong> dure vingt minutes et sert surtout à vérifier la disponibilité.",
   tache:'prep'},

  {word:"un accusé de réception",
   def:"Le court message qui confirme qu'un envoi est bien arrivé, sans rien décider.",
   ex:"Elle a reçu un <strong>accusé de réception</strong> automatique le soir même, puis plus rien pendant douze jours.",
   tache:'prep'},

  {word:"un contremaître",
   def:"La personne qui dirige une équipe directement sur le plancher d'une usine.",
   ex:"Le <strong>contremaître</strong> du quart de jour transmet ses notes à celui du soir avant de partir.",
   img:"/assets/interactive/module-n8-recherche/vocab/contremaitre.jpg",
   tache:'prep'},

  {word:"un quart de soir",
   def:"La période de travail qui commence en après-midi et se termine tard le soir.",
   ex:"Le <strong>quart de soir</strong> va de quinze heures à vingt-trois heures trente, du lundi au vendredi.",
   img:"/assets/interactive/module-n8-recherche/vocab/quart-de-soir.jpg",
   tache:'prep'},

  {word:"une chaîne de production",
   def:"La suite de machines et de postes où un produit se fabrique du début à la fin.",
   ex:"Les trois <strong>chaînes de production</strong> du quart de soir tournent à quatre-vingt-deux pour cent.",
   img:"/assets/interactive/module-n8-recherche/vocab/chaine-de-production.jpg",
   tache:'t1'},

  {word:"une mise en situation",
   def:"Un cas inventé qu'on donne à résoudre pour voir comment quelqu'un réfléchit.",
   ex:"L'examen écrit est une <strong>mise en situation</strong> : une ligne arrêtée, trois problèmes, et l'ordre à choisir.",
   tache:'t1'},

  {word:"une entrevue de groupe",
   def:"Une rencontre où plusieurs candidats sont reçus et observés en même temps.",
   ex:"À l'<strong>entrevue de groupe</strong>, on regarde autant comment vous écoutez que ce que vous dites.",
   img:"/assets/interactive/module-n8-recherche/vocab/entrevue-de-groupe.jpg",
   tache:'t1'},

  {word:"le taux de roulement",
   def:"La proportion du personnel qui quitte une entreprise dans une année.",
   ex:"Un <strong>taux de roulement</strong> de onze pour cent est bas pour ce secteur : les gens restent.",
   tache:'t2'},

  {word:"un carnet de commandes",
   def:"L'ensemble des commandes déjà reçues et pas encore livrées.",
   ex:"Le <strong>carnet de commandes</strong> a doublé en dix-huit mois, et il a fallu ouvrir un troisième quart.",
   tache:'t2'},

  {word:"un temps d'arrêt",
   def:"Le moment où une machine ne produit pas, prévu ou non.",
   ex:"Les dix points qui manquent viennent des <strong>temps d'arrêt</strong> imprévus, pas des arrêts planifiés.",
   img:"/assets/interactive/module-n8-recherche/vocab/temps-d-arret.jpg",
   tache:'t2'},

  {word:"une acquisition",
   def:"Le rachat d'une entreprise par une autre.",
   ex:"Depuis l'<strong>acquisition</strong> de janvier, l'usine appartient à un groupe de Mississauga.",
   tache:'t2'},

  {word:"un motif de discrimination",
   def:"Une caractéristique personnelle qu'on n'a pas le droit d'invoquer contre quelqu'un.",
   ex:"L'âge, la grossesse et l'origine sont des <strong>motifs de discrimination</strong> nommés par la Charte.",
   tache:'t3'},

  {word:"un échelon",
   def:"Un des degrés d'une échelle de salaires, à l'intérieur d'un même poste.",
   ex:"L'échelle compte six <strong>échelons</strong>, et on n'embauche pas obligatoirement au premier.",
   tache:'t3'},

  {word:"une contrepartie",
   def:"Ce qu'on offre en échange de ce qu'on demande.",
   ex:"Elle n'a pas demandé deux <strong>échelons</strong> : elle en a proposé un tout de suite, et l'autre en <strong>contrepartie</strong> d'un résultat.",
   tache:'t3'},

  {word:"le service continu",
   def:"Le temps travaillé sans interruption chez un même employeur.",
   ex:"Les trois semaines de vacances viennent après trois ans de <strong>service continu</strong> chez le même employeur.",
   tache:'t3'},
];
