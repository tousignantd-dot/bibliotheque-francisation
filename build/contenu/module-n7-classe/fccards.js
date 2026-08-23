const FC_CARDS = [
  // Vingt mots, quatre illustrés. La proportion est basse et elle est voulue :
  // la moitié de ce vocabulaire nomme des façons de travailler — animer, un
  // mandat, un tour de parole, un consensus, un compte rendu — qui ne se
  // photographient pas. Les quatre qui restent nomment un lieu, une couverture
  // végétale, un objet planté et une personne devant un groupe. Les images
  // montrent la scène, jamais le document : voir le docstring de gen_images.py.
  //
  // Les mots du travail d'équipe viennent des intentions de la situation ; les
  // quatre mots du sujet de recherche (îlot de chaleur, canopée,
  // évapotranspiration, arbre de rue) sont là parce qu'un élève ne peut pas
  // animer une rencontre sur un sujet dont il n'a pas les mots.

  {word:"un sujet de recherche", def:"La question précise qu'une équipe reçoit et sur laquelle elle devra présenter ses trouvailles.", ex:"Chaque équipe reçoit un <strong>sujet de recherche</strong> différent et trois semaines pour le traiter.", tache:"prep"},
  {word:"un mandat", def:"Ce qu'on demande à quelqu'un de faire, avec ce qui est attendu à la fin.", ex:"Le <strong>mandat</strong> tient en trois lignes : chercher, présenter, remettre un texte.", tache:"prep"},
  {word:"animer une rencontre", def:"Conduire une réunion : ouvrir, donner la parole, faire préciser, résumer à la fin.", ex:"<strong>Animer une rencontre</strong>, ce n'est pas parler le plus longtemps.", tache:"prep"},
  {word:"la répartition des rôles", def:"Le partage du travail entre les personnes d'une équipe, décidé au début.", ex:"La <strong>répartition des rôles</strong> se fait avant la première rencontre, jamais pendant.", tache:"prep"},
  {word:"un échéancier", def:"La liste de ce qui doit être fait, avec la date de chaque étape.", ex:"Notre <strong>échéancier</strong> tient sur une feuille : trois rencontres et une remise.", tache:"prep"},

  {word:"une personne-ressource", def:"Quelqu'un qui connaît bien un sujet et qu'on invite pour l'entendre et le questionner.", ex:"La <strong>personne-ressource</strong> est venue un mardi soir et elle est restée une heure.", img:"/assets/interactive/module-n7-classe/vocab/personne-ressource.jpg", tache:"t1"},
  {word:"la prise de notes", def:"Le fait d'écrire pendant qu'une personne parle, pour retrouver plus tard ce qu'elle a dit.", ex:"Sa <strong>prise de notes</strong> tient sur une page et il retrouve tout.", tache:"t1"},
  {word:"une estimation", def:"Un chiffre approché, calculé à partir de ce qu'on sait, mais qui n'a pas été mesuré.", ex:"Dix degrés d'écart, c'est une <strong>estimation</strong> : la mesure a été prise un seul jour.", tache:"t1"},
  {word:"un îlot de chaleur", def:"Un secteur dont la surface devient beaucoup plus chaude que celle des secteurs voisins.", ex:"Le stationnement du centre commercial est le plus gros <strong>îlot de chaleur</strong> du quartier.", img:"/assets/interactive/module-n7-classe/vocab/ilot-de-chaleur.jpg", tache:"t1"},
  {word:"la canopée", def:"La couverture formée par la cime des arbres, vue d'en haut, mesurée en pourcentage du territoire.", ex:"La <strong>canopée</strong> de ce secteur reste sous les dix pour cent.", img:"/assets/interactive/module-n7-classe/vocab/canopee.jpg", tache:"t1"},
  {word:"l'évapotranspiration", def:"L'eau qu'un arbre pompe par ses racines et rejette en vapeur par ses feuilles, ce qui rafraîchit l'air.", ex:"L'<strong>évapotranspiration</strong> refroidit l'air même quand on n'est pas sous l'arbre.", tache:"t1"},
  {word:"un arbre de rue", def:"Un arbre planté dans le trottoir ou en bordure de la chaussée, dans une ouverture étroite.", ex:"Un <strong>arbre de rue</strong> mal arrosé meurt en silence, souvent au troisième été.", img:"/assets/interactive/module-n7-classe/vocab/arbre-de-rue.jpg", tache:"t1"},

  {word:"la question de départ", def:"Ce que l'équipe cherche à savoir, et à quoi chaque phrase du travail doit se rattacher.", ex:"Si la phrase ne répond pas à la <strong>question de départ</strong>, elle sort du résumé.", tache:"t2"},
  {word:"une source fiable", def:"Un document dont on connaît l'auteur, la date, et qui peut être vérifié ailleurs.", ex:"Une <strong>source fiable</strong> porte une date : sans date, on ne sait pas ce qu'on cite.", tache:"t2"},
  {word:"une fiche d'information", def:"Une page courte, écrite par un organisme, qui présente un sujet par courtes sections.", ex:"La <strong>fiche d'information</strong> de la ville tient sur deux écrans.", tache:"t2"},
  {word:"un résumé", def:"Un texte court qui redit avec ses propres mots ce qu'un texte long apporte à la question posée.", ex:"Un <strong>résumé</strong> de dix lignes qui contient trois citations n'est pas un résumé.", tache:"t2"},

  {word:"un tour de parole", def:"Le moment où c'est à une personne de parler, et où les autres écoutent.", ex:"Elle a donné un <strong>tour de parole</strong> à chacun avant d'ouvrir la discussion.", tache:"t3"},
  {word:"un désaccord", def:"Le fait que deux personnes ne pensent pas la même chose et le disent.", ex:"Le <strong>désaccord</strong> portait sur ce qu'on note, pas sur le fait d'y aller.", tache:"t3"},
  {word:"un consensus", def:"Un accord que tout le monde accepte, même ceux qui auraient préféré autre chose.", ex:"On est arrivés à un <strong>consensus</strong> en reformulant les deux positions.", tache:"t3"},
  {word:"un compte rendu", def:"Le texte écrit après une rencontre : qui a proposé quoi, ce qui a été décidé, ce qui reste à faire.", ex:"Le <strong>compte rendu</strong> part le soir même à ceux qui n'étaient pas là.", tache:"t3"},
];
