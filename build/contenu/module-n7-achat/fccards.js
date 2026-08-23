const FC_CARDS = [
  // Seize mots, quatre par section. La situation « Achat de biens de
  // consommation durables » n'a **aucune** entrée de lexique au niveau 7 : la
  // liste se compose à partir des trois intentions — décrire un problème de
  // fonctionnement, faire une réclamation, rédiger une lettre de réclamation
  // — et des savoirs lexicaux du niveau (« Discussion et explications portant
  // sur la réclamation d'un bien de consommation durable », « Rédaction d'une
  // lettre de réclamation », « produits financiers reliés au crédit »).
  //
  // Les quatre familles suivent le dossier d'Ernestine : ce qu'on a signé,
  // la panne, la réclamation, l'écrit.
  //
  // Les mots abstraits n'ont pas d'image : une photo de « l'obligation
  // totale » montrerait un document, donc du texte — et la règle 1 de la
  // vague 7 l'interdit. Huit mots sur seize sont illustrés ; les huit autres
  // se passent très bien de vignette.

  {word:"une auto d'occasion", def:"Un véhicule qui a déjà appartenu à quelqu'un et qu'on achète en deuxième ou en troisième main.", ex:"Son <strong>auto d'occasion</strong> avait cent quatre mille kilomètres à la livraison.", img:"/assets/interactive/module-n7-achat/vocab/auto-d-occasion.jpg", tache:"prep"},
  {word:"l'odomètre", def:"Le compteur qui affiche le nombre total de kilomètres parcourus par un véhicule depuis sa sortie d'usine.", ex:"Le chiffre inscrit à l'<strong>odomètre</strong> doit paraître sur l'étiquette du commerçant.", tache:"prep"},
  {word:"les frais de crédit", def:"Ce qu'on paie en plus du prix, pour avoir le droit de payer plus tard et par versements.", ex:"Sur cinq ans, les <strong>frais de crédit</strong> ajoutaient deux mille sept cent quarante et un dollars.", tache:"prep"},
  {word:"l'obligation totale", def:"La somme complète qu'un acheteur à crédit s'engage à verser : le montant financé et les frais réunis.", ex:"L'<strong>obligation totale</strong> se lit dans la case du bas, à droite.", tache:"prep"},

  {word:"la transmission", def:"La partie mécanique qui transmet la force du moteur aux roues et qui change les rapports.", ex:"La <strong>transmission</strong> cognait chaque matin, au coin de la rue Notre-Dame.", img:"/assets/interactive/module-n7-achat/vocab/transmission.jpg", tache:"t1"},
  {word:"un cognement", def:"Un bruit sourd et bref, comme un coup frappé une seule fois.", ex:"Le <strong>cognement</strong> revenait à froid, jamais le soir.", tache:"t1"},
  {word:"un témoin lumineux", def:"La petite lampe du tableau de bord qui s'allume pour signaler un problème au conducteur.", ex:"Aucun <strong>témoin lumineux</strong> ne s'était allumé avant la panne.", img:"/assets/interactive/module-n7-achat/vocab/temoin-lumineux.jpg", tache:"t1"},
  {word:"un diagnostic", def:"Le résultat de l'examen par lequel un spécialiste établit d'où vient un problème.", ex:"Le <strong>diagnostic</strong> tenait en deux lignes : fuite au carter et jeu anormal.", img:"/assets/interactive/module-n7-achat/vocab/diagnostic.jpg", tache:"t1"},

  {word:"la garantie de bon fonctionnement", def:"La protection que la loi accorde à l'acheteur d'une auto d'occasion, pour une durée qui dépend de l'âge et du kilométrage du véhicule.", ex:"En catégorie C, la <strong>garantie de bon fonctionnement</strong> dure un mois ou mille sept cents kilomètres.", tache:"t2"},
  {word:"une garantie prolongée", def:"Une protection payante que le commerçant propose en plus, et qui comporte presque toujours des exclusions.", ex:"La <strong>garantie prolongée</strong> lui avait coûté douze cents dollars et ne couvrait pas les joints.", tache:"t2"},
  {word:"l'usure normale", def:"La détérioration qu'un objet subit forcément à l'usage, et qu'aucune garantie ne répare.", ex:"« C'est de l'<strong>usure normale</strong> » est la première phrase qu'on entend au comptoir.", img:"/assets/interactive/module-n7-achat/vocab/usure-normale.jpg", tache:"t2"},
  {word:"une réclamation", def:"La démarche par laquelle un client demande à un commerçant de réparer, de remplacer ou de rembourser.", ex:"Sa <strong>réclamation</strong> portait sur les pièces et la main-d'œuvre, rien de plus.", tache:"t2"},

  {word:"une mise en demeure", def:"Une lettre qui expose des faits, formule une demande précise et accorde un dernier délai avant d'aller plus loin.", ex:"La <strong>mise en demeure</strong> d'Ernestine tenait sur une page et accordait dix jours.", tache:"t3"},
  {word:"un vice caché", def:"Un défaut grave qu'un acheteur attentif ne pouvait pas voir au moment de l'achat.", ex:"La rouille sous le plancher du coffre était un <strong>vice caché</strong>.", img:"/assets/interactive/module-n7-achat/vocab/vice-cache.jpg", tache:"t3"},
  {word:"une pièce justificative", def:"Un papier qui prouve ce qu'on avance : une facture, un rapport, un contrat.", ex:"Elle a joint trois <strong>pièces justificatives</strong> à sa lettre.", img:"/assets/interactive/module-n7-achat/vocab/piece-justificative.jpg", tache:"t3"},
  {word:"la Division des petites créances", def:"Le tribunal où l'on réclame soi-même, sans avocat, une somme de quinze mille dollars ou moins.", ex:"À la <strong>Division des petites créances</strong>, chacun présente son dossier lui-même.", img:"/assets/interactive/module-n7-achat/vocab/petites-creances.jpg", tache:"t3"},
];
