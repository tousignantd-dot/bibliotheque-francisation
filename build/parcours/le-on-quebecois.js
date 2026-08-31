// ═══════════════════════════════════════════════════════════════════════════
// Point express — « On » : qui parle ?
//
// Savoir n6-s21 (Pronoms indéfinis). Une ORDONNANCE : l'enseignant l'envoie à
// un élève dont la production ou la compréhension montre qu'il ne sait pas qui
// se cache derrière un « on ». Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Aucune mini-leçon du dépôt ne traite « on » pour lui-même. Deux l'effleurent,
// et c'est justement le problème :
//   · `module-n5-transport` — « On demande aux automobilistes de… » : elle ne
//     montre QUE le « on » des autorités, dans une consigne de circulation.
//   · `module-alimentation` — « Ça se garde deux jours » : elle se sert de
//     « on » comme point de départ pour enseigner autre chose (le « se »).
// Un élève qui a lu ces deux-là croit donc que « on » veut dire « les
// autorités » — et il ne comprend pas le texto de sa colocataire. Les cinq
// écarts tenus :
//
//   1. INDUCTIF. L'élève range huit « on » entendus dans la vraie vie AVANT
//      qu'on lui dise qu'il y en a deux. La règle de l'écran 3 est écrite
//      comme un constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des pronoms indéfinis. Un
//      TEST unique — remplacer « on » par « nous » et voir si la phrase dit
//      encore la même chose — qui marche sur une phrase jamais vue.
//   3. LE « ON » INDÉFINI EST DIT EN DERNIER (écran 8), alors que c'est le
//      sens d'origine et celui des deux mini-leçons. Le nommer d'entrée ferait
//      croire à deux règles à retenir ; il n'y en a qu'une, et un test.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Pronom indéfini » n'est écrit qu'à
//      l'écran 3, une fois la chose manipulée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un texto entre sœurs, une
//      affiche d'immeuble, un courriel à un employeur, une annonce d'autocar,
//      un comptoir de clinique. L'élève doit reconnaître le mot partout.
//
// Aucun média : les deux « on » se prononcent exactement pareil, et c'est le
// sujet même du point. Rien à écouter — tout est dans la phrase autour.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'le-on-quebecois',
  titre:    "« On » : qui parle ?",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s21',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Deux phrases, le même mot. Dans laquelle « on » veut dire « nous » ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Mon frère et moi, on arrive vendredi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Ici, on paie avant de manger.&nbsp;»",
        rat_t: "Celle-là ne parle de personne en particulier.",
        rat: "Elle est tentante parce qu'elle décrit bien des gens qui paient. Mais essayez de "
           + "dire «&nbsp;ici, <b>nous payons</b> avant de manger&nbsp;»&nbsp;: la phrase change de "
           + "sens. Elle ne dit plus la règle de la maison, elle dit votre habitude à vous." },
      { txt: "Les deux veulent dire «&nbsp;nous&nbsp;».",
        rat_t: "À l'oreille, rien ne les distingue — c'est bien le problème.",
        rat: "Le mot est le même, la prononciation est la même, et personne ne vous dira jamais "
           + "lequel vous venez d'entendre. Ce qui les sépare est <b>autour</b> du mot, pas dedans." },
    ],
    pourquoi: "La première. Gardez la phrase entière en tête&nbsp;; on va voir dans deux écrans "
            + "comment les séparer à coup sûr.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-qui',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit « on »',
    titre: "Huit phrases entendues cette semaine. Qui se cache derrière chaque « on » ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Fiez-vous à la situation écrite sous "
            + "chaque phrase&nbsp;: elle vous dit presque tout.",
    colonnes: [
      { id: 'nous', t: "C'est nous",       b: "C'est nous" },
      { id: 'ind',  t: "N'importe qui",    b: "N'importe qui" },
    ],
    items: [
      { txt: "On soupe à six heures.", sous: "un texto à une amie", ok: 'nous',
        rat: "Celui qui écrit parle de sa maison et des gens qui y vivent. Remplacez par "
           + "«&nbsp;nous soupons&nbsp;»&nbsp;: la phrase ne bouge pas d'un millimètre.",
        pourquoi: "Nous soupons à six heures. Des personnes précises." },
      { txt: "On ne fume pas dans l'entrée.", sous: "une affiche à la porte d'un immeuble", ok: 'ind',
        rat: "Une affiche ne parle pas d'elle-même. Elle s'adresse à tout le monde&nbsp;: "
           + "les locataires, les visiteurs, vous. Personne n'est nommé, et c'est voulu.",
        pourquoi: "Personne en particulier : la règle vaut pour tous." },
      { txt: "On a manqué l'autobus.", sous: "un message à un enseignant", ok: 'nous',
        rat: "L'élève explique son retard. Il parle de lui et de la personne avec qui il était — "
           + "«&nbsp;nous avons manqué l'autobus&nbsp;».",
        pourquoi: "Nous avons manqué l'autobus. Des personnes précises." },
      { txt: "On demande aux voyageurs de rester assis.", sous: "une annonce dans un autocar", ok: 'ind',
        rat: "C'est la compagnie qui parle, sans se nommer. Remarquez qu'elle ne dit pas "
           + "«&nbsp;nous demandons&nbsp;»&nbsp;: elle évite justement de se désigner.",
        pourquoi: "La compagnie, sans se nommer." },
      { txt: "On m'a dit de revenir lundi.", sous: "au comptoir d'une clinique", ok: 'ind',
        rat: "Celui-là trompe souvent&nbsp;: la personne qui a parlé existe pour de vrai. Mais "
           + "celui qui raconte ne la nomme pas — il ne sait plus qui c'était, ou ça n'a pas "
           + "d'importance. «&nbsp;Nous m'a dit&nbsp;» ne se dit pas.",
        pourquoi: "Quelqu'un, qu'on ne nomme pas." },
      { txt: "On se voit demain ?", sous: "un texto", ok: 'nous',
        rat: "Deux personnes qui se donnent rendez-vous&nbsp;: «&nbsp;nous nous voyons "
           + "demain&nbsp;?&nbsp;» Même chose, en plus lourd.",
        pourquoi: "Toi et moi. Des personnes précises." },
      { txt: "On construit un tramway sur cette rue.", sous: "au bulletin de nouvelles", ok: 'ind',
        rat: "La Ville, un entrepreneur, un ministère — le journaliste ne le précise pas, parce "
           + "que ce qui compte est le tramway, pas celui qui creuse.",
        pourquoi: "La Ville, un entrepreneur : la phrase ne le dit pas." },
      { txt: "On est allés à l'épicerie ensemble.", sous: "un message à sa mère", ok: 'nous',
        rat: "Le mot «&nbsp;ensemble&nbsp;» le dit&nbsp;: ils étaient plusieurs, et celui qui "
           + "écrit en était. Regardez aussi la fin du verbe — on y revient bientôt.",
        pourquoi: "Nous sommes allés. Et la fin du mot le dit déjà." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez séparé les gens précis du reste.",
    paras: [
      "Regardez votre colonne «&nbsp;c'est nous&nbsp;»&nbsp;: à chaque fois, celui qui parle "
      + "<b>fait partie</b> du groupe, et on pourrait nommer les autres. Dans l'autre colonne, "
      + "personne n'est nommable — ou celui qui parle s'arrange pour ne pas l'être.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> remplacez «&nbsp;on&nbsp;» "
      + "par <b>nous</b>. Si la phrase dit encore exactement la même chose, «&nbsp;on&nbsp;» "
      + "voulait dire nous. Si elle change de sens ou devient bizarre, «&nbsp;on&nbsp;» voulait "
      + "dire quelqu'un, n'importe qui.",

      "Ce mot s'appelle un <b>pronom indéfini</b>&nbsp;: son travail d'origine est justement de "
      + "ne désigner personne. Vous n'avez pas besoin du nom pour vous en servir, mais votre "
      + "enseignant l'emploiera.",
    ],
    retenir: "Remplacez «&nbsp;on&nbsp;» par <b>nous</b>. Même sens&nbsp;: c'est nous. "
           + "Sens changé&nbsp;: c'est n'importe qui.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : le verbe ne bouge jamais. ──────────────────────
  {
    id:   'le-verbe',
    type: 'verif',
    eye:  'Le piège du verbe',
    menu: 'Le verbe',
    titre: "« On » veut dire nous. Est-ce que le verbe le sait ?",
    consigne: "Amadou écrit à son propriétaire pour dire que sa famille et lui sont partis tôt. "
            + "Quelle phrase écrit-il&nbsp;?",
    options: [
      { txt: "On est partis à sept heures.", juste: true },
      { txt: "On sont partis à sept heures.",
        rat_t: "C'est la faute de ceux qui ont bien compris le sens.",
        rat: "Vous avez entendu «&nbsp;nous&nbsp;» dans votre tête, et vous avez conjugué comme "
           + "«&nbsp;ils&nbsp;». C'est logique — et c'est faux. Le verbe qui suit "
           + "«&nbsp;on&nbsp;» se conjugue toujours comme avec <i>il</i> ou <i>elle</i>&nbsp;: "
           + "on <b>est</b>, on <b>a</b>, on <b>va</b>. Jamais on sont, jamais on ont." },
      { txt: "On est parti à sept heures.",
        rat_t: "Ce n'est pas une faute — mais ça ne dit pas ce qu'Amadou veut dire.",
        rat: "Sans le «&nbsp;s&nbsp;», on comprend une seule personne, ou n'importe qui. "
           + "Amadou parle de sa famille et de lui&nbsp;: ils étaient plusieurs, et la fin du mot "
           + "doit le dire. C'est l'écran suivant." },
    ],
    pourquoi: "Le verbe reste au singulier&nbsp;: <b>on est</b>, toujours. Mais la fin du "
            + "participe, elle, bouge — et c'est là que tout se joue.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La lettre qu'on n'entend pas. ─────────────────────────────────────
  {
    id:   'la-lettre-muette',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: "La lettre qu'on n'entend pas",
    titre: "« On est allé » et « on est allés » se prononcent exactement pareil.",
    paras: [
      "C'est pour ça que cette faute traverse des années sans être corrigée&nbsp;: à l'oral, il "
      + "n'y a rien à entendre. Elle n'apparaît qu'au moment où vous écrivez.",

      "Le verbe ne bouge pas, mais ce qui vient après suit <b>les personnes que « on » "
      + "cache</b>. Miriam écrit à sa sœur&nbsp;: «&nbsp;<i>Ma fille et moi, on est "
      + "arriv<b>ées</b> hier.</i>&nbsp;» Deux femmes&nbsp;: le «&nbsp;e&nbsp;» et le "
      + "«&nbsp;s&nbsp;». Son voisin écrit le même jour&nbsp;: «&nbsp;<i>Mon fils et moi, on est "
      + "arriv<b>és</b> hier.</i>&nbsp;»",

      "Et quand «&nbsp;on&nbsp;» ne cache personne, rien ne s'ajoute&nbsp;: «&nbsp;<i>Ici, on est "
      + "pri<b>é</b> de retirer ses bottes.</i>&nbsp;» C'est la même règle, appliquée à un groupe "
      + "vide.",
    ],
    retenir: "Le verbe se conjugue comme avec <i>il</i>. Ce qui vient <b>après</b> s'accorde avec "
           + "les personnes que «&nbsp;on&nbsp;» cache — et avec personne, quand il n'en cache aucune.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Regardez deux choses seulement&nbsp;: le verbe juste après «&nbsp;on&nbsp;», puis "
            + "la fin du mot qui suit.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "On sont arrivés en retard.", ok: 'faux',
        rat: "Le sens est bon — ils étaient plusieurs. C'est le verbe qui a suivi le sens au lieu "
           + "de suivre le mot&nbsp;: «&nbsp;on <b>est</b> arrivés&nbsp;».",
        pourquoi: "Il faut « on est arrivés »." },
      { txt: "Ma sœur et moi, on est allées à la clinique.", ok: 'ok',
        rat: "Verbe au singulier, fin du participe au féminin pluriel&nbsp;: les deux moitiés "
           + "sont justes, et on sait qui écrit.",
        pourquoi: "Verbe au singulier, accord avec deux femmes. Juste." },
      { txt: "Ici, on est prié de retirer ses bottes.", ok: 'ok',
        rat: "Une affiche&nbsp;: «&nbsp;on&nbsp;» ne cache personne. Rien ne s'ajoute à la fin, "
           + "et c'est correct.",
        pourquoi: "Aucun groupe caché : rien ne s'ajoute." },
      { txt: "On a reçu vos documents ce matin.", ok: 'ok',
        rat: "Avec <i>avoir</i>, la fin du participe ne bouge pas — que «&nbsp;on&nbsp;» cache "
           + "trois personnes ou aucune. Rien à corriger.",
        pourquoi: "Avec « avoir », rien ne bouge." },
      { txt: "Mon patron et moi, on est content de vous rencontrer.", ok: 'faux',
        rat: "Le verbe est bon. Mais ils sont deux&nbsp;: il manque le «&nbsp;s&nbsp;» — "
           + "«&nbsp;on est cont<b>ents</b>&nbsp;». La faute ne s'entend pas, elle se voit.",
        pourquoi: "Il manque le « s » : on est contents." },
      { txt: "Les enfants et moi, on est allé au parc.", ok: 'faux',
        rat: "Encore la lettre muette. «&nbsp;Les enfants et moi&nbsp;» est écrit juste devant, "
           + "et pourtant le participe est resté seul&nbsp;: «&nbsp;on est all<b>és</b>&nbsp;».",
        pourquoi: "Il manque le « s » : on est allés." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qu'on peut écrire, et où. ──────────────────────────────────────
  {
    id:   'ce-quon-ecrit',
    type: 'verif',
    eye:  'Vérification',
    menu: "À l'écrit",
    titre: "Vous répondez par courriel à un client. Que choisissez-vous ?",
    consigne: "Votre équipe a corrigé une erreur de facturation. Vous voulez le dire, et vous "
            + "voulez qu'on sache que c'est vous.",
    options: [
      { txt: "«&nbsp;Nous avons corrigé l'erreur.&nbsp;»", juste: true },
      { txt: "«&nbsp;On a corrigé l'erreur.&nbsp;»",
        rat_t: "Personne ne vous reprendrait à l'oral.",
        rat: "C'est exactement ce que vous direz au téléphone, et ce sera parfait. Mais dans un "
           + "courriel professionnel, «&nbsp;on&nbsp;» fait familier et laisse le lecteur se "
           + "demander qui a corrigé&nbsp;: vous, un collègue, le système&nbsp;? "
           + "<b>À l'écrit officiel, écrivez «&nbsp;nous&nbsp;».</b>" },
      { txt: "«&nbsp;L'erreur a été corrigée.&nbsp;»",
        rat_t: "Correcte, mais elle efface celui qui a agi.",
        rat: "C'est la phrase des avis administratifs&nbsp;: elle dit ce qui est arrivé sans dire "
           + "qui l'a fait. Ici, vous vouliez précisément qu'on sache que c'est votre équipe." },
    ],
    pourquoi: "<b>«&nbsp;On&nbsp;» à l'oral et dans un texto, «&nbsp;nous&nbsp;» à l'écrit "
            + "officiel.</b> Ce n'est pas une faute de grammaire, c'est une question de "
            + "situation — et c'est celle qu'on vous fera remarquer au travail.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le « on » indéfini, dit en dernier : c'est son travail d'origine. ─
  {
    id:   'lindefini-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "L'autre « on »",
    titre: "L'autre « on » ne cache personne, et c'est son vrai métier.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est volontaire&nbsp;: c'est le sens d'origine du mot, "
      + "et il n'y a <b>rien à accorder</b>. Il sert partout où l'on ne veut pas, ou ne peut pas, "
      + "nommer quelqu'un&nbsp;: «&nbsp;on ne fume pas ici&nbsp;», «&nbsp;on m'a rappelée&nbsp;», "
      + "«&nbsp;on ferme à dix-huit heures&nbsp;», «&nbsp;on refait la rue&nbsp;».",

      "Une chose vaut la peine d'être remarquée&nbsp;: quand une compagnie ou un bureau écrit "
      + "«&nbsp;on&nbsp;» plutôt que «&nbsp;nous&nbsp;», il évite de se désigner. Devant ce "
      + "«&nbsp;on&nbsp;»-là, il est toujours utile de se demander <b>qui exactement</b> a fait "
      + "l'action, et de le demander au comptoir si ça vous concerne.",

      "Autrement dit, vous n'avez <b>qu'une seule chose</b> à surveiller quand vous écrivez&nbsp;: "
      + "est-ce que je cache des personnes derrière ce mot&nbsp;? Si non, écrivez sans y penser.",
    ],
    retenir: "Un mot, deux emplois. <b>L'emploi à surveiller est celui qui cache des "
           + "personnes&nbsp;;</b> l'autre s'écrit tout seul.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Teodora écrit à sa mère. Quelle version tient d'un bout à l'autre ?",
    consigne: "Elle raconte son arrivée avec sa sœur. Trois versions du même message&nbsp;: "
            + "une seule est correcte partout.",
    options: [
      { txt: "On est arrivées hier soir, ma sœur et moi, et on a trouvé un logement.",
        juste: true },
      { txt: "On sont arrivées hier soir, ma sœur et moi, et on ont trouvé un logement.",
        rat_t: "Les accords sont bons. Ce sont les deux verbes qui ont suivi le sens.",
        rat: "«&nbsp;Arrivées&nbsp;» est juste&nbsp;: deux femmes. Mais les verbes se conjuguent "
           + "sur le <b>mot</b> «&nbsp;on&nbsp;», pas sur les personnes qu'il cache&nbsp;: "
           + "on <b>est</b>, on <b>a</b>. C'est la moitié qui ne s'entend pas qui était déjà "
           + "réglée, et celle qui s'entend qui a lâché." },
      { txt: "On est arrivé hier soir, ma sœur et moi, et on a trouvé un logement.",
        rat_t: "Les verbes sont bons. C'est la lettre muette qui manque.",
        rat: "Vous avez le plus difficile. Mais «&nbsp;ma sœur et moi&nbsp;» est écrit dans la "
           + "phrase même&nbsp;: deux femmes, donc «&nbsp;arriv<b>ées</b>&nbsp;». "
           + "«&nbsp;On a trouvé&nbsp;» ne bouge pas, lui&nbsp;: c'est <i>avoir</i>." },
    ],
    pourquoi: "Verbes au singulier, participe au féminin pluriel, et rien à ajouter après "
            + "<i>avoir</i>. <b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la phrase du début : « Mon frère et moi, on arrive vendredi. »",
    consigne: "Cette fois, ce n'est plus un texto&nbsp;: vous écrivez à votre employeur pour "
            + "annoncer votre retour de vacances. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Mon frère et moi serons de retour vendredi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Mon frère et moi, on arrive vendredi.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle était parfaite là-bas.",
        rat: "Rien n'est faux dedans. Mais elle a changé de destinataire&nbsp;: un employeur lit "
           + "un courriel, pas un texto. Le même contenu s'écrit avec <b>nous</b>, ou en nommant "
           + "les personnes, comme ici." },
      { txt: "«&nbsp;On sera de retour vendredi.&nbsp;»",
        rat_t: "Le registre est meilleur, mais on ne sait plus de qui vous parlez.",
        rat: "Votre employeur ne sait pas si «&nbsp;on&nbsp;» veut dire vous deux, votre équipe, "
           + "ou l'entreprise entière. C'est exactement le doute que le mot fabrique — et la "
           + "raison pour laquelle on l'évite à l'écrit officiel." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître qui se cache derrière "
            + "«&nbsp;on&nbsp;», conjuguer le verbe comme avec <i>il</i>, et choisir "
            + "«&nbsp;nous&nbsp;» quand la situation le demande.",
    attente: "Choisissez une réponse pour finir.",
  },

];
