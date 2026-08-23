const FC_CARDS = [
  // Seize mots, quatre par section. La situation « Problèmes reliés à
  // l'habitation » n'a **aucune** entrée de lexique au niveau 7 : le document
  // de progression du lexique ne la couvre pas. La liste se compose donc à
  // partir des deux intentions — régler un problème de voisinage, rédiger une
  // lettre pour régler un problème — et du savoir lexical du niveau qui la
  // nomme : « Vocabulaire lié à un problème de voisinage : voisin bruyant,
  // stationnement, etc. » et « Mots servant à décrire les conséquences de la
  // situation en litige : cela m'empêche de…, cela m'oblige à…, etc. »
  //
  // Les quatre familles suivent le dossier de Ruslana : ce qui arrive, la
  // conversation, la preuve et l'arbitrage, l'écrit.

  // ── Je découvre : nommer ce qui arrive ──
  {word:"un trouble de voisinage", def:"Le dérangement qu'une personne fait subir à celle qui habite à côté ou au-dessus, dans l'usage normal de son logement.", ex:"Un bruit qui revient tous les matins pendant un mois devient un <strong>trouble de voisinage</strong>.", img:"/assets/interactive/module-n7-habitation/vocab/trouble-de-voisinage.jpg", tache:"prep"},
  {word:"une nuisance sonore", def:"Un bruit qui dépasse ce qu'une personne raisonnable accepterait, par son heure, sa force ou sa répétition.", ex:"Le règlement de la ville traite le tapis roulant de cinq heures du matin comme une <strong>nuisance sonore</strong>.", img:"/assets/interactive/module-n7-habitation/vocab/nuisance-sonore.jpg", tache:"prep"},
  {word:"la jouissance paisible", def:"Le droit d'habiter son logement tranquille, sans être dérangé sans arrêt par quelqu'un d'autre.", ex:"En signant le bail, la propriétaire s'est engagée à procurer à sa locataire la <strong>jouissance paisible</strong> des lieux.", img:"/assets/interactive/module-n7-habitation/vocab/jouissance-paisible.jpg", tache:"prep"},
  {word:"un inconvénient normal", def:"Le petit dérangement que tout le monde subit en habitant près des autres, et qu'il faut accepter.", ex:"Des pas au-dessus de la tête à sept heures du soir sont un <strong>inconvénient normal</strong> ; les mêmes pas à cinq heures du matin tous les jours ne le sont plus.", tache:"prep"},

  // ── Défi 1 : la conversation sur le palier ──
  {word:"un palier", def:"L'espace plat, devant les portes, où l'escalier s'arrête à chaque étage.", ex:"Toute la conversation s'est faite debout sur le <strong>palier</strong> du troisième.", img:"/assets/interactive/module-n7-habitation/vocab/palier.jpg", tache:"t1"},
  {word:"un arrangement à l'amiable", def:"Une solution que deux personnes trouvent elles-mêmes, sans juge et sans papier officiel.", ex:"Le caoutchouc sous le tapis roulant était un <strong>arrangement à l'amiable</strong>, et il a tenu.", img:"/assets/interactive/module-n7-habitation/vocab/arrangement-a-lamiable.jpg", tache:"t1"},
  {word:"une concession", def:"Ce qu'une personne accepte de lâcher pour que l'autre accepte quelque chose à son tour.", ex:"Descendre le vélo à l'épaule lui coûtait peu : c'était sa première <strong>concession</strong>.", tache:"t1"},
  {word:"un reproche", def:"Ce qu'on dit à quelqu'un pour lui signifier qu'il a mal agi.", ex:"Elle est montée avec des heures et des dates plutôt qu'avec un <strong>reproche</strong>.", tache:"t1"},

  // ── Défi 2 : la preuve et l'arbitrage ──
  {word:"un registre des bruits", def:"Le carnet où l'on note chaque jour l'heure, la durée et la nature de ce qu'on entend.", ex:"Son <strong>registre des bruits</strong> comptait quarante-sept lignes au bout d'un mois et demi.", img:"/assets/interactive/module-n7-habitation/vocab/registre-des-bruits.jpg", tache:"t2"},
  {word:"un témoin", def:"La personne qui a vu ou entendu la même chose que vous et qui peut le confirmer.", ex:"La voisine du deux est devenue un <strong>témoin</strong> le jour où elle a entendu le tapis, elle aussi.", tache:"t2"},
  {word:"la médiation citoyenne", def:"Un service gratuit où une personne neutre aide deux voisins à se parler jusqu'à ce qu'ils trouvent eux-mêmes une entente.", ex:"La <strong>médiation citoyenne</strong> ne dit jamais qui a raison : elle fait parler les deux.", img:"/assets/interactive/module-n7-habitation/vocab/mediation-citoyenne.jpg", tache:"t2"},
  {word:"le règlement municipal", def:"Les règles écrites par une ville pour son territoire, notamment sur le bruit et les heures.", ex:"Le <strong>règlement municipal</strong> découpe la journée en trois périodes : le jour, le soir et la nuit.", tache:"t2"},

  // ── Défi 3 : l'écrit qui règle ──
  {word:"une mise en demeure", def:"Une lettre qui expose un problème, demande précisément quelque chose et donne un délai pour le faire.", ex:"Sa <strong>mise en demeure</strong> tenait en une page et donnait dix jours.", img:"/assets/interactive/module-n7-habitation/vocab/mise-en-demeure.jpg", tache:"t3"},
  {word:"un délai raisonnable", def:"Le temps qu'on laisse à quelqu'un pour agir, ni trop court pour être tenable, ni assez long pour ne rien changer.", ex:"Dix jours est le <strong>délai raisonnable</strong> le plus souvent employé dans ce genre de lettre.", tache:"t3"},
  {word:"un courrier recommandé", def:"Un envoi postal dont on garde la preuve, parce que la personne doit signer pour le recevoir.", ex:"Elle a posté sa lettre en <strong>courrier recommandé</strong> et a rangé le reçu avec son registre.", img:"/assets/interactive/module-n7-habitation/vocab/courrier-recommande.jpg", tache:"t3"},
  {word:"une diminution de loyer", def:"La baisse du montant payé chaque mois, accordée quand le logement n'a pas donné tout ce qu'il devait donner.", ex:"Une <strong>diminution de loyer</strong> se demande au propriétaire avisé qui n'a rien fait, jamais au voisin.", tache:"t3"},
];
