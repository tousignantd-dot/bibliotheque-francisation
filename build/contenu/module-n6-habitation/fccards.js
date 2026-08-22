const FC_CARDS = [
  // Seize mots. Le programme donne une seule ligne de lexique à la situation
  // « Problèmes reliés à l'habitation » au niveau 6 — « mots liés aux travaux
  // de réparation, de rénovation ou d'entretien : toiture, plancher, béton,
  // asphalte, etc. » — et un savoir lexical du niveau qui la complète :
  // « exploiter des champs lexicaux pour exprimer le détail ou la nuance ».
  // Les seize mots en sortent, et de rien d'autre.
  //
  // Quatre familles, une par section : les gens et les papiers du départ, ce
  // qui tient la maison debout, ce qu'on lit avant de signer, ce qu'on trouve
  // une fois le plancher ouvert.

  {word:"un entrepreneur général", def:"La personne qui prend le chantier en charge au complet et qui fait venir chaque métier au bon moment.", ex:"L'<strong>entrepreneur général</strong> ne pose pas la tuyauterie lui-même : il la fait poser.", img:"/assets/interactive/module-n6-habitation/vocab/entrepreneur-general.jpg", tache:"prep"},
  {word:"une soumission", def:"Le prix écrit qu'une entreprise propose pour des travaux, avec le détail de ce qu'elle fera.", ex:"La <strong>soumission</strong> tient sur deux pages et se lit ligne par ligne.", img:"/assets/interactive/module-n6-habitation/vocab/soumission.jpg", tache:"prep"},
  {word:"un corps de métier", def:"Chacun des métiers appelés sur un chantier : le maçon, le plombier, l'électricien, le poseur de gypse.", ex:"Quatre <strong>corps de métier</strong> vont se suivre dans le sous-sol.", img:"/assets/interactive/module-n6-habitation/vocab/corps-de-metier.jpg", tache:"prep"},
  {word:"un permis de rénovation", def:"L'autorisation que la municipalité donne avant certains travaux, et qui se demande à elle seule.", ex:"Le <strong>permis de rénovation</strong> a pris dix jours ouvrables.", tache:"prep"},

  {word:"la fondation", def:"Le mur de béton enfoui dans le sol, sur lequel toute la maison repose.", ex:"La <strong>fondation</strong> du côté nord a fendu sur un mètre.", img:"/assets/interactive/module-n6-habitation/vocab/fondation.jpg", tache:"t1"},
  {word:"une fissure", def:"Une fente étroite qui traverse un mur ou une dalle et qui s'agrandit avec les années.", ex:"La <strong>fissure</strong> monte en biais derrière l'étagère.", img:"/assets/interactive/module-n6-habitation/vocab/fissure.jpg", tache:"t1"},
  {word:"une descente de gouttière", def:"Le tuyau vertical qui conduit l'eau du toit jusqu'au sol.", ex:"La <strong>descente de gouttière</strong> se vide à trente centimètres du mur.", img:"/assets/interactive/module-n6-habitation/vocab/descente-de-gouttiere.jpg", tache:"t1"},
  {word:"la pente du terrain", def:"L'inclinaison du sol autour de la maison, qui éloigne l'eau de pluie ou qui la ramène vers elle.", ex:"On refait la <strong>pente du terrain</strong> sur deux mètres tout autour.", img:"/assets/interactive/module-n6-habitation/vocab/pente-du-terrain.jpg", tache:"t1"},

  {word:"un rapport d'inspection", def:"Le document où une inspectrice décrit l'état réel du bâtiment, pièce par pièce, sans rien proposer.", ex:"Le <strong>rapport d'inspection</strong> compte onze pages et deux photos par section.", img:"/assets/interactive/module-n6-habitation/vocab/rapport-inspection.jpg", tache:"t2"},
  {word:"le taux d'humidité", def:"Le chiffre qui dit combien d'eau un matériau contient encore.", ex:"Le <strong>taux d'humidité</strong> du mur nord est de dix-neuf pour cent.", tache:"t2"},
  {word:"les exclusions", def:"La liste de ce qu'une soumission ne comprend pas et qui sera facturé à part.", ex:"Les <strong>exclusions</strong> sont écrites en bas de la deuxième page.", tache:"t2"},
  {word:"un échéancier", def:"Le calendrier des travaux : ce qui se fait quand, et dans quel ordre.", ex:"L'<strong>échéancier</strong> prévoit six semaines, séchage compris.", img:"/assets/interactive/module-n6-habitation/vocab/echeancier.jpg", tache:"t2"},

  {word:"une dalle de béton", def:"La couche de béton coulée à plat qui sert de plancher au sous-sol.", ex:"La <strong>dalle de béton</strong> a été coulée en 1961, sans rien en dessous.", img:"/assets/interactive/module-n6-habitation/vocab/dalle-de-beton.jpg", tache:"t3"},
  {word:"une membrane", def:"La feuille étanche qu'on pose entre le sol et le plancher pour arrêter l'humidité.", ex:"Une <strong>membrane</strong> se pose avant les fourrures et le revêtement.", img:"/assets/interactive/module-n6-habitation/vocab/membrane.jpg", tache:"t3"},
  {word:"un imprévu", def:"Ce que personne ne pouvait voir avant d'ouvrir, et qui change le prix et la date.", ex:"Le vieux puisard condamné est un <strong>imprévu</strong> au sens de la soumission.", tache:"t3"},
  {word:"un acompte", def:"La part du prix versée avant la fin des travaux, en échange d'un reçu.", ex:"L'<strong>acompte</strong> de trente pour cent se verse à la signature.", tache:"t3"},
];
