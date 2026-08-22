const FC_CARDS = [
  // Seize mots. La situation « Consultation d'un professionnel de la santé »
  // du niveau 6 n'a aucun lexique rattaché : ils sont inventés à partir des
  // quatre savoirs lexicaux du niveau qui la nomment — « mots servant à
  // décrire les problèmes de santé plus sérieux : malaise, fatigue chronique,
  // anémie », « vocabulaire lié au traitement de ces problèmes : effets
  // secondaires, diagnostic », « vocabulaire lié à l'hôpital, à l'urgence, aux
  // délais d'attente, aux heures de visite » et « phrases clés servant à
  // amorcer une conversation ».
  //
  // Cinq mots pour l'entrée à l'hôpital, quatre pour l'attente et ce qu'on y
  // dit, quatre pour l'entretien avec la spécialiste, trois pour l'écrit qui
  // reste. Aucun n'est un mot de la vie courante déguisé, et aucun ne double
  // le vocabulaire des voisins des niveaux 3, 4 et 5 : « une pharmacie », « un
  // rendez-vous », « une douleur », « l'urgence » appartiennent à ces
  // modules-là.
  //
  // Les définitions décrivent des façons de faire et des papiers, jamais un
  // état de santé et jamais une conduite à tenir. « Une anémie » est définie
  // par ce qu'un résultat d'analyse dit, et pas par ce qu'il faudrait en
  // faire.

  {word:"une clinique externe", def:"Le service d'un hôpital où l'on est reçu à une heure donnée, sans y être hospitalisé.", ex:"La <strong>clinique externe</strong> ferme à seize heures et n'ouvre pas la fin de semaine.", img:"/assets/interactive/module-n6-sante/vocab/clinique-externe.jpg", tache:"prep"},
  {word:"une demande de consultation", def:"Le papier par lequel un médecin en fait voir un autre, plus spécialisé, à la même personne.", ex:"La <strong>demande de consultation</strong> est partie en avril et l'appel est venu en octobre.", img:"/assets/interactive/module-n6-sante/vocab/demande-de-consultation.jpg", tache:"prep"},
  {word:"la médecine interne", def:"La spécialité de ceux qui cherchent la cause d'un problème qui touche l'ensemble du corps.", ex:"Elle a été dirigée en <strong>médecine interne</strong>, au troisième étage.", img:"/assets/interactive/module-n6-sante/vocab/medecine-interne.jpg", tache:"prep"},
  {word:"un délai d'attente", def:"Le temps qui sépare la demande du rendez-vous, et sur lequel personne au guichet n'a de pouvoir.", ex:"Le <strong>délai d'attente</strong> a été de sept mois, et ce n'était pas le plus long.", img:"/assets/interactive/module-n6-sante/vocab/delai-attente.jpg", tache:"prep"},
  {word:"un dossier médical", def:"L'ensemble de ce qui a été écrit sur une personne par ceux qui l'ont vue, et qui la suit d'un service à l'autre.", ex:"Ses résultats de mars étaient déjà au <strong>dossier médical</strong>.", img:"/assets/interactive/module-n6-sante/vocab/dossier-medical.jpg", tache:"prep"},

  {word:"un malaise", def:"Un dérangement du corps qu'on sent sans pouvoir le montrer du doigt ni le nommer.", ex:"Elle est venue pour un <strong>malaise</strong> qui n'a ni endroit ni date précise.", img:"/assets/interactive/module-n6-sante/vocab/malaise.jpg", tache:"t1"},
  {word:"la fatigue chronique", def:"Une fatigue qui dure des mois et que le repos ne fait pas partir.", ex:"Ce que le repos ne répare pas en trois nuits porte un nom : la <strong>fatigue chronique</strong>.", img:"/assets/interactive/module-n6-sante/vocab/fatigue-chronique.jpg", tache:"t1"},
  {word:"un proche aidant", def:"Celui qui accompagne quelqu'un de sa famille sans être payé pour le faire ni formé pour ça.", ex:"Il attend deux heures chaque mardi : c'est un <strong>proche aidant</strong>, et personne ne le compte.", img:"/assets/interactive/module-n6-sante/vocab/proche-aidant.jpg", tache:"t1"},
  {word:"les heures de visite", def:"Les moments de la journée où l'on a le droit d'entrer voir quelqu'un qui est hospitalisé.", ex:"Les <strong>heures de visite</strong> sont affichées à côté de l'ascenseur.", img:"/assets/interactive/module-n6-sante/vocab/heures-de-visite.jpg", tache:"t1"},

  {word:"un antécédent", def:"Une maladie, une opération ou un évènement de santé déjà arrivé, qu'on redit à chaque nouveau médecin.", ex:"Elle a mis ses <strong>antécédents</strong> sur une feuille pour ne plus les chercher de mémoire.", tache:"t2"},
  {word:"un prélèvement", def:"Le peu de sang ou de liquide qu'on prend sur une personne pour le faire analyser.", ex:"Le <strong>prélèvement</strong> se fait au rez-de-chaussée, sans rendez-vous.", img:"/assets/interactive/module-n6-sante/vocab/prelevement.jpg", tache:"t2"},
  {word:"un diagnostic", def:"Le nom qu'un médecin donne à un problème une fois qu'il a vérifié assez pour l'écrire.", ex:"Elle est ressortie sans <strong>diagnostic</strong> et avec un plan, ce qui n'est pas la même chose.", tache:"t2"},
  {word:"une anémie", def:"Un résultat d'analyse qui dit que le sang transporte l'oxygène moins bien qu'il le devrait.", ex:"Le mot <strong>anémie</strong> était écrit sur la feuille de mars, sans une ligne d'explication.", tache:"t2"},

  {word:"les effets secondaires", def:"Ce qu'un traitement fait en plus de ce qu'on lui demande, et qu'on signale au lieu de l'endurer.", ex:"Le feuillet consacre un paragraphe entier aux <strong>effets secondaires</strong> et à qui les dire.", img:"/assets/interactive/module-n6-sante/vocab/effets-secondaires.jpg", tache:"t3"},
  {word:"un feuillet d'information", def:"La feuille remise en sortant, qui explique la marche à suivre et non la maladie.", ex:"Le <strong>feuillet d'information</strong> tient sur une page et se garde sur le réfrigérateur.", img:"/assets/interactive/module-n6-sante/vocab/feuillet-information.jpg", tache:"t3"},
  {word:"un suivi", def:"Ce qui est prévu après le rendez-vous : qui rappelle, quand, et ce qu'il faut avoir fait d'ici là.", ex:"Sans date écrite, un <strong>suivi</strong> est une intention et rien de plus.", tache:"t3"},
];
