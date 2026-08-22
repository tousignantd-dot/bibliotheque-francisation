const FC_CARDS = [
  // Seize mots. La situation « Relations sociales » n'a aucun lexique
  // rattaché au niveau 6 ; les mots sortent des deux savoirs lexicaux du
  // niveau qui la nomment : « mots en rapport avec les évènements racontés :
  // naissance, mariage, enterrement, accident, voyage » et « mots servant à
  // décrire physiquement une personne : visage allongé, doigts effilés,
  // cheveux ondulés ». Les quatre derniers viennent de l'article d'intérêt
  // général du Défi 3, qu'il faut pouvoir résumer à quelqu'un.

  // ── Je découvre — ce qu'on annonce dans un courriel de nouvelles ──
  {word:"une naissance", def:"L'arrivée au monde d'un enfant, dans une famille.", ex:"Il annonce une <strong>naissance</strong> dès le premier paragraphe : sa fille Assia.", tache:"prep"},
  {word:"un déménagement", def:"Le fait de quitter un logement pour aller vivre dans un autre.", ex:"Leur <strong>déménagement</strong> a eu lieu en juin, trois mois après la naissance.", img:"/assets/interactive/module-n6-relations/vocab/demenagement.jpg", tache:"prep"},
  {word:"des funérailles", def:"La cérémonie qu'on tient après la mort de quelqu'un, avec la famille et les proches.", ex:"Les <strong>funérailles</strong> ont eu lieu au pays, en février, et il n'a pas pu s'y rendre.", tache:"prep"},
  {word:"un faire-part", def:"Une petite carte envoyée pour annoncer un évènement important de la vie familiale.", ex:"Elle a gardé le <strong>faire-part</strong> du mariage sur la porte du réfrigérateur.", img:"/assets/interactive/module-n6-relations/vocab/faire-part.jpg", tache:"prep"},

  // ── Défi 1 — ce que le courriel raconte ──────────────────────────
  {word:"un accident de travail", def:"Un évènement qui blesse quelqu'un pendant qu'il fait son métier.", ex:"Son beau-frère a eu un <strong>accident de travail</strong> en novembre : il est tombé d'une plateforme.", img:"/assets/interactive/module-n6-relations/vocab/accident-travail.jpg", tache:"t1"},
  {word:"une réadaptation", def:"La longue période pendant laquelle on réapprend à se servir d'une partie du corps blessée.", ex:"Après le plâtre, sa <strong>réadaptation</strong> a duré presque trois mois.", img:"/assets/interactive/module-n6-relations/vocab/readaptation.jpg", tache:"t1"},
  {word:"des retrouvailles", def:"Le moment où des gens qui ne s'étaient pas vus depuis longtemps se revoient.", ex:"Ces <strong>retrouvailles</strong> arrivent après deux ans sans nouvelles.", img:"/assets/interactive/module-n6-relations/vocab/retrouvailles.jpg", tache:"t1"},
  {word:"un imprévu", def:"Une chose qui arrive sans qu'on l'ait annoncée et qui change les plans.", ex:"Elle a répondu tout de suite, au cas où il y aurait un <strong>imprévu</strong> vendredi.", tache:"t1"},

  // ── Défi 2 — décrire quelqu'un ───────────────────────────────────
  {word:"une silhouette", def:"La forme générale d'une personne vue de loin : sa taille et sa carrure.", ex:"De l'autre bout du terminus, on ne voit qu'une <strong>silhouette</strong> et une valise.", img:"/assets/interactive/module-n6-relations/vocab/silhouette.jpg", tache:"t2"},
  {word:"un visage allongé", def:"Un visage plus long que large, souvent avec un menton fin.", ex:"Elle a un <strong>visage allongé</strong> et les pommettes hautes.", img:"/assets/interactive/module-n6-relations/vocab/visage-allonge.jpg", tache:"t2"},
  {word:"des cheveux ondulés", def:"Des cheveux qui font des vagues douces, ni raides ni frisés serré.", ex:"Ses <strong>cheveux ondulés</strong> sont attachés en chignon bas.", img:"/assets/interactive/module-n6-relations/vocab/cheveux-ondules.jpg", tache:"t2"},
  {word:"un signe particulier", def:"Un détail du corps qui n'appartient qu'à une personne et qui permet de la reconnaître.", ex:"Sa petite cicatrice au-dessus du sourcil est un <strong>signe particulier</strong>.", tache:"t2"},

  // ── Défi 3 — l'article d'intérêt général ─────────────────────────
  {word:"un jumelage", def:"Le fait de mettre ensemble deux familles ou deux personnes pour qu'elles se rencontrent régulièrement.", ex:"Le <strong>jumelage</strong> dure six mois, à raison d'une rencontre aux deux semaines.", img:"/assets/interactive/module-n6-relations/vocab/jumelage.jpg", tache:"t3"},
  {word:"un organisme communautaire", def:"Un groupe du quartier, sans but de profit, qui organise des services pour les gens qui y vivent.", ex:"L'<strong>organisme communautaire</strong> occupe deux locaux au sous-sol de l'église.", img:"/assets/interactive/module-n6-relations/vocab/organisme-communautaire.jpg", tache:"t3"},
  {word:"un bénévole", def:"Une personne qui donne son temps à un organisme sans être payée pour ça.", ex:"Chaque duo est accompagné par un <strong>bénévole</strong> du quartier.", tache:"t3"},
  {word:"une coordonnatrice", def:"La personne qui organise le travail des autres dans un organisme et qui répond aux questions.", ex:"La <strong>coordonnatrice</strong> a été citée deux fois dans l'article.", tache:"t3"},
];
