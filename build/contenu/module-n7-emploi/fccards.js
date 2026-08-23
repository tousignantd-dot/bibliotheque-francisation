const FC_CARDS = [
  // Seize mots, quatre par section. La situation « Emploi » du niveau 7 n'a
  // aucun lexique dans le programme : ces mots sortent des quatre intentions
  // et des savoirs lexicaux du niveau (« présentation d'un projet, d'une
  // évaluation sommaire ou d'un problème provenant de collègues », « lettre
  // d'affaires courantes »). Dix sur seize sont illustrés : les six autres
  // sont trop abstraits pour qu'une photo dise quoi que ce soit.
  {word:"un projet", def:"Ce qu'on veut faire, avec les étapes, le coût et la date qui vont avec.", ex:"Elle a préparé son <strong>projet</strong> sur une seule feuille.", tache:"prep"},
  {word:"une évaluation sommaire", def:"Un premier examen rapide d'une situation, qui donne des ordres de grandeur et non des chiffres définitifs.", ex:"Il a fait une <strong>évaluation sommaire</strong> du coût : entre onze et treize mille dollars.", tache:"prep"},
  {word:"un ordre du jour", def:"La liste écrite des points dont une réunion va traiter, dans l'ordre.", ex:"Le réaménagement du quai est le premier point de l'<strong>ordre du jour</strong>.", img:"/assets/interactive/module-n7-emploi/vocab/ordre-du-jour.jpg", tache:"prep"},
  {word:"une réunion de production", def:"La rencontre régulière où l'équipe fait le point sur le travail de l'usine.", ex:"La <strong>réunion de production</strong> commence à huit heures le lundi.", img:"/assets/interactive/module-n7-emploi/vocab/reunion-production.jpg", tache:"prep"},

  {word:"un échéancier", def:"Le calendrier d'un projet : ce qui se fait, et à quelle date.", ex:"Selon l'<strong>échéancier</strong>, les relevés se terminent le 19 septembre.", img:"/assets/interactive/module-n7-emploi/vocab/echeancier.jpg", tache:"t1"},
  {word:"une étape", def:"Un des moments d'un travail, qui vient après le précédent et avant le suivant.", ex:"La première <strong>étape</strong>, c'est de mesurer.", tache:"t1"},
  {word:"la mise en œuvre", def:"Le moment où l'on passe du plan au travail réel, sur le terrain.", ex:"La <strong>mise en œuvre</strong> commencera après l'essai.", tache:"t1"},
  {word:"un budget", def:"L'argent prévu pour faire quelque chose, avant de le dépenser.", ex:"Le <strong>budget</strong> de l'essai est de quatre cents dollars.", img:"/assets/interactive/module-n7-emploi/vocab/budget.jpg", tache:"t1"},

  {word:"la manutention", def:"Le fait de déplacer des charges à la main : soulever, porter, déposer.", ex:"La <strong>manutention</strong> répétitive est la cause des maux de dos au poste 4.", img:"/assets/interactive/module-n7-emploi/vocab/manutention.jpg", tache:"t2"},
  {word:"un poste de travail", def:"L'endroit précis où une personne fait sa tâche, avec ce qu'il y a autour.", ex:"Le <strong>poste de travail</strong> numéro 4 sert à l'emballage.", img:"/assets/interactive/module-n7-emploi/vocab/poste-travail.jpg", tache:"t2"},
  {word:"un correctif", def:"Le changement qu'on apporte pour régler un problème constaté.", ex:"La rotation des tâches est un <strong>correctif</strong> qui ne coûte rien.", tache:"t2"},
  {word:"un programme de prévention", def:"Le document où un employeur écrit les dangers de son établissement et ce qu'il fait pour les enlever.", ex:"Le <strong>programme de prévention</strong> se met à jour chaque année.", img:"/assets/interactive/module-n7-emploi/vocab/programme-prevention.jpg", tache:"t2"},

  {word:"une soumission", def:"Le prix écrit qu'un fournisseur propose pour un travail ou un équipement précis.", ex:"La <strong>soumission</strong> est valide jusqu'à la fin novembre.", img:"/assets/interactive/module-n7-emploi/vocab/soumission.jpg", tache:"t3"},
  {word:"un fournisseur", def:"L'entreprise qui vend à une autre entreprise ce dont elle a besoin.", ex:"Équipements Sorel est notre <strong>fournisseur</strong> depuis douze ans.", img:"/assets/interactive/module-n7-emploi/vocab/fournisseur.jpg", tache:"t3"},
  {word:"une note de service", def:"Un court texte officiel qui informe le personnel d'une entreprise de quelque chose.", ex:"La <strong>note de service</strong> annonce la rotation à l'essai.", img:"/assets/interactive/module-n7-emploi/vocab/note-service.jpg", tache:"t3"},
  {word:"un accusé de réception", def:"Le mot par lequel on confirme qu'on a bien reçu une lettre ou un document.", ex:"Il a envoyé un <strong>accusé de réception</strong> le lendemain matin.", tache:"t3"},
];
