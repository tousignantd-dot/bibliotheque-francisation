const FC_CARDS = [
  // Seize mots, quatre par section. La situation « Location ou achat d'un
  // logement » n'a **aucune** entrée de lexique au niveau 7 : la liste se
  // compose à partir des deux intentions — négocier, s'informer pour
  // acheter — et des savoirs lexicaux du niveau (« Négociations en vue de
  // louer un logement », « Conversation portant sur l'achat d'un logement »).
  //
  // Les quatre familles suivent le dossier de Sokhna : le papier reçu,
  // la négociation, la visite, l'achat.

  {word:"un avis de modification", def:"Le papier par lequel un propriétaire annonce qu'il veut changer le loyer ou une autre condition du bail.", ex:"L'<strong>avis de modification</strong> était coincé dans la porte, sans enveloppe.", img:"/assets/interactive/module-n7-logement/vocab/avis-de-modification.jpg", tache:"prep"},
  {word:"une hausse de loyer", def:"L'augmentation du montant payé chaque mois pour habiter un logement.", ex:"La <strong>hausse de loyer</strong> demandée est de quatre-vingt-quatre dollars par mois.", img:"/assets/interactive/module-n7-logement/vocab/hausse-de-loyer.jpg", tache:"prep"},
  {word:"la fixation du loyer", def:"La décision par laquelle un tribunal établit lui-même le montant du loyer, quand les deux parties ne s'entendent pas.", ex:"Faute d'entente, le propriétaire doit demander la <strong>fixation du loyer</strong> au Tribunal.", tache:"prep"},
  {word:"un délai de réponse", def:"Le temps dont une personne dispose pour dire oui ou non avant qu'il soit trop tard.", ex:"Le <strong>délai de réponse</strong> est d'un mois à partir du jour où l'avis est reçu.", img:"/assets/interactive/module-n7-logement/vocab/delai-de-reponse.jpg", tache:"prep"},

  {word:"une contre-proposition", def:"Une offre différente qu'on présente à la place de celle qu'on vient de recevoir.", ex:"Sa <strong>contre-proposition</strong> tenait en deux points : quarante-cinq dollars et la fenêtre.", img:"/assets/interactive/module-n7-logement/vocab/contre-proposition.jpg", tache:"t1"},
  {word:"une contrepartie", def:"Ce qu'une personne donne en échange de ce qu'elle obtient dans une entente.", ex:"La fenêtre changée avant l'hiver était sa <strong>contrepartie</strong>.", tache:"t1"},
  {word:"une entente écrite", def:"Un accord noté sur papier, avec la date, pour que personne n'ait à se fier à sa mémoire.", ex:"Deux lignes et des initiales suffisent à faire une <strong>entente écrite</strong>.", img:"/assets/interactive/module-n7-logement/vocab/entente-ecrite.jpg", tache:"t1"},
  {word:"un compromis", def:"Une solution où chacune des deux personnes accepte de reculer un peu.", ex:"Cinquante-cinq dollars et un vitrier au mois de septembre : le <strong>compromis</strong> tenait.", tache:"t1"},

  {word:"un courtier immobilier", def:"La personne dont le métier est de faire vendre ou acheter une propriété, et qui travaille pour celle des deux parties avec qui elle a signé un contrat.", ex:"Le <strong>courtier immobilier</strong> du vendeur ne représente pas l'acheteur.", img:"/assets/interactive/module-n7-logement/vocab/courtier-immobilier.jpg", tache:"t2"},
  {word:"un contrat de courtage", def:"Le contrat qui lie un courtier à la personne pour qui il travaille et qui fixe sa rétribution.", ex:"Sa rétribution est écrite dans le <strong>contrat de courtage</strong> signé par le vendeur.", tache:"t2"},
  {word:"les frais de copropriété", def:"Le montant payé chaque mois par le propriétaire d'un logement dans un immeuble partagé, pour l'entretien commun.", ex:"Les <strong>frais de copropriété</strong> sont de cent quatre-vingt-dix dollars par mois.", img:"/assets/interactive/module-n7-logement/vocab/frais-de-copropriete.jpg", tache:"t2"},
  {word:"le fonds de prévoyance", def:"L'argent que les propriétaires d'un immeuble mettent de côté ensemble pour les grosses réparations à venir.", ex:"Demandez toujours ce qu'il y a dans le <strong>fonds de prévoyance</strong>, et depuis quand.", img:"/assets/interactive/module-n7-logement/vocab/fonds-de-prevoyance.jpg", tache:"t2"},

  {word:"une promesse d'achat", def:"Le document par lequel une personne s'engage à acheter une propriété à un prix et à des conditions écrites.", ex:"Une fois acceptée, la <strong>promesse d'achat</strong> engage les deux parties.", img:"/assets/interactive/module-n7-logement/vocab/promesse-dachat.jpg", tache:"t3"},
  {word:"la mise de fonds", def:"L'argent que l'acheteur paie de sa poche au moment de l'achat, en plus de ce qu'il emprunte.", ex:"Sous cinq cent mille dollars, la <strong>mise de fonds</strong> minimale est de cinq pour cent.", img:"/assets/interactive/module-n7-logement/vocab/mise-de-fonds.jpg", tache:"t3"},
  {word:"une inspection préachat", def:"L'examen d'un bâtiment par un professionnel, avant l'achat, pour savoir dans quel état il se trouve.", ex:"L'<strong>inspection préachat</strong> n'est pas obligatoire, mais y renoncer coûte cher.", img:"/assets/interactive/module-n7-logement/vocab/inspection-preachat.jpg", tache:"t3"},
  {word:"les droits de mutation", def:"L'impôt que le nouveau propriétaire verse à sa municipalité après avoir acheté une propriété.", ex:"Les <strong>droits de mutation</strong> arrivent quelques mois après l'achat, et surprennent tout le monde.", img:"/assets/interactive/module-n7-logement/vocab/droits-de-mutation.jpg", tache:"t3"},
];
