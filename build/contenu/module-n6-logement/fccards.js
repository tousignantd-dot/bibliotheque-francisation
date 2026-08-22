const FC_CARDS = [
  // Seize mots. Contrairement à la plupart des situations, celle-ci a bien un
  // savoir lexical au niveau 6, et les mots en sortent presque tous :
  // « vocabulaire lié aux droits et aux obligations du locataire : délai,
  // résiliation, renouvellement, défaut de paiement, dommages, compensation,
  // avis, locateur, indemnité, clauses, cession, sous-location, etc. ».
  //
  // Trois familles, une par section : les mots du bail (Je découvre), les
  // mots du site (Défi 1), les mots de la réponse (Défi 2).

  {word:"un locateur", def:"La personne qui loue son logement à quelqu'un d'autre et qui signe le bail de ce côté-là.", ex:"Le <strong>locateur</strong> habite le rez-de-chaussée du même immeuble.", img:"/assets/interactive/module-n6-logement/vocab/locateur.jpg", tache:"prep"},
  {word:"un bail", def:"Le contrat écrit qui dit qui occupe le logement, pour combien de temps et à quel prix.", ex:"Son <strong>bail</strong> se termine le trente juin.", img:"/assets/interactive/module-n6-logement/vocab/bail.jpg", tache:"prep"},
  {word:"une clause", def:"Une phrase du contrat qui pose une règle à part, souvent numérotée.", ex:"Aucune <strong>clause</strong> du bail ne parle de la sous-location.", tache:"prep"},
  {word:"un avis", def:"Un papier écrit qu'on remet à l'autre partie pour l'informer officiellement de quelque chose.", ex:"Elle a remis son <strong>avis</strong> en main propre, le dix-huit novembre.", img:"/assets/interactive/module-n6-logement/vocab/avis.jpg", tache:"prep"},
  {word:"un délai", def:"Le temps qu'une personne a pour agir avant qu'il soit trop tard.", ex:"Le <strong>délai</strong> de réponse est de quinze jours.", img:"/assets/interactive/module-n6-logement/vocab/delai.jpg", tache:"prep"},
  {word:"la reconduction", def:"Le fait qu'un bail continue tout seul aux mêmes conditions, sans qu'on le resigne.", ex:"La <strong>reconduction</strong> se fait sans papier si personne n'envoie d'avis.", tache:"prep"},

  {word:"la sous-location", def:"Le fait de prêter son logement à quelqu'un pour un temps, en gardant son bail à son nom.", ex:"Pendant la <strong>sous-location</strong>, elle reste responsable du loyer.", img:"/assets/interactive/module-n6-logement/vocab/sous-location.jpg", tache:"t1"},
  {word:"la cession de bail", def:"Le fait de transmettre son bail à quelqu'un d'autre et de sortir du contrat pour de bon.", ex:"Une <strong>cession de bail</strong> ne se reprend pas : le logement change de locataire.", img:"/assets/interactive/module-n6-logement/vocab/cession-de-bail.jpg", tache:"t1"},
  {word:"la résiliation", def:"La fin d'un contrat avant la date prévue, dans les cas que la loi permet.", ex:"La <strong>résiliation</strong> n'est pas possible seulement parce qu'on déménage.", tache:"t1"},
  {word:"un motif sérieux", def:"Une raison solide, vérifiable, qui touche la personne ou le logement — pas un simple goût.", ex:"Un refus doit s'appuyer sur un <strong>motif sérieux</strong> écrit noir sur blanc.", img:"/assets/interactive/module-n6-logement/vocab/motif-serieux.jpg", tache:"t1"},
  {word:"les obligations", def:"Ce qu'une personne doit faire à cause du contrat ou de la loi, qu'elle en ait envie ou non.", ex:"Payer le premier du mois fait partie de ses <strong>obligations</strong>.", tache:"t1"},

  {word:"le consentement", def:"L'accord donné par une personne à ce que l'autre lui propose.", ex:"Son silence pendant quinze jours vaut <strong>consentement</strong>.", tache:"t2"},
  {word:"un accusé de réception", def:"La preuve écrite qu'une personne a bien reçu un document, avec la date.", ex:"Elle a demandé un <strong>accusé de réception</strong> signé sur sa copie.", img:"/assets/interactive/module-n6-logement/vocab/accuse-de-reception.jpg", tache:"t2"},
  {word:"une indemnité", def:"L'argent versé pour réparer une perte causée à quelqu'un.", ex:"Il réclame une <strong>indemnité</strong> pour ses frais de vérification.", tache:"t2"},
  {word:"des dommages", def:"Les dégâts causés à un logement, ou la perte d'argent qui en résulte.", ex:"Les <strong>dommages</strong> au plancher de la cuisine ont été photographiés.", img:"/assets/interactive/module-n6-logement/vocab/dommages.jpg", tache:"t2"},
  {word:"le défaut de paiement", def:"Le fait de ne pas payer son loyer à la date prévue.", ex:"Un <strong>défaut de paiement</strong> de trois semaines est inscrit à son dossier.", img:"/assets/interactive/module-n6-logement/vocab/defaut-de-paiement.jpg", tache:"t2"},
];
