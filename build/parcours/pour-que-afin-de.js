// ═══════════════════════════════════════════════════════════════════════════
// Point express — Dire à quoi ça doit servir
//
// Savoirs n7-s27 (subjonctif obligatoire après « pour que ») et n7-s03
// (l'expression du but avec des marqueurs courants). Une ORDONNANCE :
// l'enseignant l'envoie à l'élève dont les demandes écrites laissent le
// lecteur se demander qui doit agir. Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Le dépôt porte « Le subjonctif après pour que et avant que » : elle part de
// la conjonction, donne la conjugaison, puis illustre. C'est exactement
// l'ordre inverse de celui-ci, et c'est aussi pourquoi elle ne règle rien
// chez l'élève qui écrit « je vous écris pour changer la serrure » alors
// qu'il veut que le propriétaire la change : cette phrase-là ne contient
// aucun subjonctif, elle est parfaitement correcte, et elle dit le contraire
// de ce que l'élève voulait dire. Les cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR UNE QUESTION DE FAIT. L'écran 2 ne demande pas de
//      reconnaître une conjonction : il demande QUI fait la deuxième action.
//      L'élève range huit phrases sur cette seule question, et découvre que
//      la réponse commande la forme.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de subjonctif. Un TEST :
//      compter les personnes. Une seule → un verbe nu. Deux → « pour que »
//      et une phrase complète. Plus une sortie de secours pour l'élève chez
//      qui la forme ne vient pas : « je vous demande de… », qui nomme la
//      personne et garde l'infinitif.
//   3. LE CAS PAR DÉFAUT EST DIT EN DERNIER. « Pour » couvre toutes les
//      situations du point ; « afin de » n'est qu'un habit plus écrit posé
//      sur la même règle. L'annoncer d'entrée aurait fait croire à deux
//      systèmes à apprendre.
//   4. LE MÉTALANGAGE APRÈS. « Subjonctif » n'est écrit qu'à l'écran 5, la
//      chose ayant été maniée quatorze fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un guichet, un message à un
//      propriétaire, un voisin, un échange en magasin, une demande d'horaire
//      à un employeur, une note laissée sur une table.
//
// Aucun média : la faute enseignée ici ne s'entend pas — les deux phrases
// sont bien prononcées, bien construites, et n'ont pas le même sens.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'pour-que-afin-de',
  titre:    "Dire à quoi ça doit servir",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s27 · n7-s03',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Deux phrases presque pareilles. Dans laquelle est-ce l'agent qui remplit le formulaire ?",
    consigne: "Vous êtes au guichet d'un bureau gouvernemental. Répondez avec ce que vous savez "
            + "déjà — c'est fait exprès.",
    options: [
      { txt: "«&nbsp;J'ai apporté mes relevés pour que vous remplissiez le formulaire.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;J'ai apporté mes relevés pour remplir le formulaire.&nbsp;»",
        rat_t: "Dans celle-là, c'est vous qui remplissez.",
        rat: "Le verbe est seul, sans personne devant lui&nbsp;: il reprend alors la personne de "
           + "la phrase, c'est-à-dire <b>vous</b>. L'agent comprendra que vous avez apporté vos "
           + "relevés pour vous asseoir et remplir le formulaire vous-même." },
      { txt: "Les deux disent la même chose.",
        rat_t: "Elles se ressemblent beaucoup, et c'est bien là le problème.",
        rat: "Le début est identique, le sujet du deuxième verbe ne l'est pas. À un guichet, cette "
           + "différence décide de qui repart avec le travail à faire — et personne ne vous "
           + "corrigera&nbsp;: les deux phrases sont correctes." },
    ],
    pourquoi: "La première. Gardez les deux en tête&nbsp;: elles reviennent au dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir, sur une question de fait. ────────────────
  {
    id:   'tri-combien-de-personnes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases. Qui fait la deuxième action ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Une seule question&nbsp;: la personne "
            + "qui parle fait-elle les deux choses, ou attend-elle quelque chose de "
            + "quelqu'un d'autre&nbsp;?",
    colonnes: [
      { id: 'une',  t: "Une seule personne", b: "Une seule personne" },
      { id: 'deux', t: "Deux personnes",     b: "Deux personnes" },
    ],
    items: [
      { txt: "Je pars à sept heures pour arriver à temps.", sous: "à un collègue", ok: 'une',
        rat: "Celui qui part est celui qui arrive. Une seule personne fait les deux actions, et "
           + "le deuxième verbe n'a personne devant lui.",
        pourquoi: "Je pars, j'arrive. La même personne." },
      { txt: "Je pars à sept heures pour que les enfants arrivent à temps.", sous: "à son conjoint", ok: 'deux',
        rat: "C'est le parent qui part&nbsp;; ce sont les enfants qui arrivent. La phrase nomme "
           + "cette deuxième personne, juste avant le deuxième verbe.",
        pourquoi: "Je pars, les enfants arrivent. Deux personnes." },
      { txt: "Elle a téléphoné afin d'obtenir un rendez-vous.", sous: "un compte rendu écrit", ok: 'une',
        rat: "Celle qui téléphone est celle qui veut le rendez-vous. Le marqueur est plus écrit "
           + "que dans les autres phrases, mais ça ne change rien à qui agit.",
        pourquoi: "Elle téléphone, elle obtient. La même personne." },
      { txt: "Elle a téléphoné pour qu'on lui donne un rendez-vous.", sous: "le même compte rendu", ok: 'deux',
        rat: "Elle téléphone&nbsp;; c'est le bureau qui donne le rendez-vous. La phrase nomme ce "
           + "deuxième acteur — «&nbsp;on&nbsp;» — même s'il reste flou.",
        pourquoi: "Elle téléphone, le bureau donne. Deux personnes." },
      { txt: "Baissez le son après vingt-deux heures pour que mes enfants puissent dormir.", sous: "un mot glissé sous une porte", ok: 'deux',
        rat: "Le voisin baisse le son&nbsp;; ce sont les enfants qui dorment. Deux personnes, et "
           + "c'est justement ce qui rend la demande compréhensible.",
        pourquoi: "Il baisse, les enfants dorment. Deux personnes." },
      { txt: "Baissez le son après vingt-deux heures pour ne pas réveiller l'immeuble.", sous: "le même mot, autre version", ok: 'une',
        rat: "Une seule personne cette fois&nbsp;: le voisin baisse le son, et c'est lui qui "
           + "éviterait de réveiller. Le deuxième verbe n'a personne devant lui.",
        pourquoi: "Il baisse, il ne réveille pas. La même personne." },
      { txt: "J'ai gardé la facture pour pouvoir échanger l'appareil.", sous: "à un ami", ok: 'une',
        rat: "Celui qui garde la facture est celui qui échangera. Rien ne vient s'intercaler entre "
           + "«&nbsp;pour&nbsp;» et le verbe.",
        pourquoi: "Je garde, j'échange. La même personne." },
      { txt: "J'ai gardé la facture pour que le marchand accepte l'échange.", sous: "au comptoir du magasin", ok: 'deux',
        rat: "Celui-là trompe souvent&nbsp;: c'est bien vous qui allez échanger. Mais la phrase ne "
           + "parle pas de l'échange — elle parle de l'<b>acceptation</b>, et c'est le marchand "
           + "qui accepte.",
        pourquoi: "Je garde, le marchand accepte. Deux personnes." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez compté des personnes, et la forme du verbe a suivi.",
    paras: [
      "Relisez vos deux colonnes. Dans «&nbsp;une seule personne&nbsp;», le deuxième verbe est "
      + "toujours <b>nu</b>&nbsp;: <i>arriver</i>, <i>obtenir</i>, <i>réveiller</i>, "
      + "<i>pouvoir</i>. Dans «&nbsp;deux personnes&nbsp;», il y a d'abord un petit "
      + "<b>que</b>, puis quelqu'un, puis le verbe&nbsp;: <i>que les enfants arrivent</i>, "
      + "<i>qu'on lui donne</i>, <i>que le marchand accepte</i>.",

      "<b>Le test, à appliquer sur n'importe quelle phrase que vous écrivez&nbsp;:</b> comptez les "
      + "personnes. <b>Une seule</b>&nbsp;→ «&nbsp;pour&nbsp;» et le verbe tout seul. "
      + "<b>Deux</b>&nbsp;→ «&nbsp;pour que&nbsp;», la personne, puis son verbe. C'est tout, et "
      + "ça marche sur un verbe que vous n'avez jamais rencontré.",

      "Ce que vous écrivez là s'appelle un <b>but</b>&nbsp;: à quoi votre première action doit "
      + "servir. Dans une demande, c'est la partie qui décide si l'autre comprend ce qu'on attend "
      + "de lui. Vous n'avez pas besoin du mot pour vous en servir, mais votre enseignant "
      + "l'emploiera.",
    ],
    retenir: "<b>Une personne&nbsp;: pour + le verbe nu. Deux personnes&nbsp;: pour que + qui + "
           + "son verbe.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : la phrase juste qui dit le contraire. ──────────────────
  {
    id:   'la-serrure',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Qui agit ?',
    titre: "La faute la plus coûteuse ne casse aucune règle : elle change qui doit agir.",
    consigne: "Sofia écrit à son propriétaire. La serrure de son entrée ne ferme plus, et elle "
            + "veut que <b>lui</b> la change. Quelle ligne écrit-elle&nbsp;?",
    options: [
      { txt: "«&nbsp;Je vous écris pour que vous changiez la serrure de mon entrée.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Je vous écris pour changer la serrure de mon entrée.&nbsp;»",
        rat_t: "Sofia vient de se porter volontaire.",
        rat: "La phrase est correcte, bien construite, et un correcteur automatique n'y verra "
           + "rien. Seulement, le verbe nu reprend la personne de la phrase&nbsp;: c'est "
           + "<b>Sofia</b> qui change la serrure. Le propriétaire lira qu'elle l'avertit de "
           + "travaux — et il pourra même les lui facturer." },
      { txt: "«&nbsp;Je vous écris afin de changer la serrure de mon entrée.&nbsp;»",
        rat_t: "L'autre marqueur, exactement le même problème.",
        rat: "«&nbsp;Afin de&nbsp;» sonne plus officiel que «&nbsp;pour&nbsp;», et beaucoup "
           + "d'élèves le choisissent en croyant que la phrase devient plus sûre. Le verbe reste "
           + "nu, donc la personne ne change pas&nbsp;: c'est toujours Sofia qui changerait la "
           + "serrure." },
    ],
    pourquoi: "<b>Ce n'est pas une faute de grammaire, c'est une erreur de fait</b>&nbsp;: les "
            + "trois phrases s'écrivent, et deux disent le contraire de ce que Sofia veut. Rien "
            + "ne l'avertira.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La forme du deuxième verbe, et la sortie de secours. ──────────────
  {
    id:   'la-forme-et-la-sortie',
    type: 'notion',
    eye:  'La parade',
    menu: 'Le deuxième verbe',
    titre: "Après « pour que », le verbe prend une autre forme — et vous avez une porte de sortie.",
    paras: [
      "«&nbsp;Pour que vous <b>remplissiez</b>&nbsp;», «&nbsp;pour que mes enfants "
      + "<b>puissent</b>&nbsp;», «&nbsp;pour que le dossier <b>soit</b> complet&nbsp;»&nbsp;: le "
      + "verbe ne s'écrit pas comme d'habitude. Cette forme s'appelle le <b>subjonctif</b>, et "
      + "elle est obligatoire après <i>pour que</i> — ce n'est pas une question de style.",

      "Deux repères suffisent à couvrir presque tout ce que vous écrivez. Avec <b>vous</b>, la "
      + "fin est <b>-iez</b>&nbsp;: que vous <i>fassiez</i>, que vous <i>remplissiez</i>, que "
      + "vous <i>puissiez</i>, que vous <i>veniez</i>. Avec <b>il, elle, on</b> ou un nom, la "
      + "plupart des verbes s'écrivent comme au présent ordinaire&nbsp;: que le marchand "
      + "<i>accepte</i>, que la Ville <i>ramasse</i>. Les seuls qui changent vraiment sont ceux "
      + "que vous employez tous les jours&nbsp;: <i>soit</i>, <i>ait</i>, <i>puisse</i>, "
      + "<i>fasse</i>, <i>vienne</i>.",

      "<b>Et quand la forme ne vient pas, ne bricolez pas&nbsp;: changez de phrase.</b> "
      + "«&nbsp;<i>Je vous demande de changer la serrure.</i>&nbsp;» — vous nommez la personne "
      + "<b>avant</b> le verbe, et le verbe reste nu. C'est correct, c'est net, et une lettre "
      + "officielle en est pleine.",
    ],
    retenir: "Après <i>pour que</i>&nbsp;: le subjonctif. Si la forme ne vient pas, écrivez "
           + "<b>«&nbsp;je vous demande de…&nbsp;»</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Comptez les personnes, puis regardez si le petit mot «&nbsp;que&nbsp;» est là ou "
            + "non. Rien d'autre.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je vous envoie mon relevé pour que vous puissiez traiter ma demande.", ok: 'ok',
        rat: "Deux personnes&nbsp;: j'envoie, vous traitez. Le «&nbsp;que&nbsp;» est là, la "
           + "personne aussi, et le verbe est à la bonne forme.",
        pourquoi: "Deux personnes, « pour que » : juste." },
      { txt: "Je vous envoie mon relevé pour que traiter ma demande.", ok: 'faux',
        rat: "Le «&nbsp;que&nbsp;» annonce quelqu'un, et il n'y a personne derrière&nbsp;: la "
           + "phrase s'arrête en plein milieu. Deux corrections possibles — "
           + "«&nbsp;pour que <b>vous traitiez</b>&nbsp;» si c'est le bureau qui agit, "
           + "«&nbsp;<b>pour traiter</b>&nbsp;» si c'est vous.",
        pourquoi: "« pour que » attend une personne." },
      { txt: "J'arrive une heure plus tôt pour installer la salle.", ok: 'ok',
        rat: "Une seule personne&nbsp;: j'arrive, j'installe. Le verbe est nu, sans "
           + "«&nbsp;que&nbsp;» devant, et c'est exactement ce qu'il faut.",
        pourquoi: "Une personne, verbe nu : juste." },
      { txt: "J'arrive une heure plus tôt pour que j'installe la salle.", ok: 'faux',
        rat: "Ce n'est pas la fin du monde à l'oral, mais ça ne s'écrit pas&nbsp;: quand la "
           + "personne est la même des deux côtés, on ne la répète pas. "
           + "«&nbsp;<b>pour installer</b>&nbsp;», et la phrase s'allège.",
        pourquoi: "Même personne : on ne répète pas le sujet." },
      { txt: "Nous avons avancé la réunion afin que tout le monde soit là.", ok: 'ok',
        rat: "Deux acteurs&nbsp;: nous avançons, tout le monde est là. «&nbsp;Afin que&nbsp;» "
           + "fonctionne exactement comme «&nbsp;pour que&nbsp;», dans un registre plus écrit.",
        pourquoi: "« Afin que » suit la même règle." },
      { txt: "Nous avons avancé la réunion afin de tout le monde soit là.", ok: 'faux',
        rat: "«&nbsp;Afin de&nbsp;» annonce un verbe nu, et on lui a donné une personne et un "
           + "verbe conjugué. Dès qu'une deuxième personne entre dans la phrase, c'est "
           + "«&nbsp;afin <b>que</b>&nbsp;» — ou «&nbsp;pour que&nbsp;».",
        pourquoi: "Deux personnes : afin que, pas afin de." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. La négation, où le but se casse le plus souvent. ──────────────────
  {
    id:   'la-negation',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Dire le contraire',
    titre: "Vous voulez dire ce qu'il faut éviter. Où se placent les deux petits mots ?",
    consigne: "Vous laissez une note sur la table du personnel&nbsp;: la porte du congélateur doit "
            + "rester fermée. Qu'écrivez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Refermez bien la porte pour ne pas gaspiller d'électricité.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Refermez bien la porte pour gaspiller pas d'électricité.&nbsp;»",
        rat_t: "C'est la place de la négation dans une phrase ordinaire, et le verbe nu n'en est "
           + "pas une.",
        rat: "Dans «&nbsp;je ne gaspille pas&nbsp;», les deux mots entourent le verbe. Devant un "
           + "verbe nu, ils se mettent <b>tous les deux devant</b>, l'un contre l'autre&nbsp;: "
           + "«&nbsp;pour <b>ne pas</b> gaspiller&nbsp;». C'est la seule chose à retenir, et elle "
           + "vaut aussi pour «&nbsp;ne jamais&nbsp;», «&nbsp;ne rien&nbsp;», "
           + "«&nbsp;ne plus&nbsp;»." },
      { txt: "«&nbsp;Refermez bien la porte pour qu'on ne gaspille pas d'électricité.&nbsp;»",
        rat_t: "Elle est correcte. Elle ajoute simplement une personne dont vous n'aviez pas besoin.",
        rat: "Rien à corriger&nbsp;: deux acteurs, «&nbsp;que&nbsp;», la personne, le verbe à la "
           + "bonne forme. Mais c'est le même collègue qui referme la porte et qui gaspillerait "
           + "l'électricité&nbsp;: une seule personne suffit, et la note est plus courte." },
    ],
    pourquoi: "<b>Devant un verbe nu, «&nbsp;ne pas&nbsp;» reste groupé et passe devant&nbsp;:</b> "
            + "pour ne pas oublier, pour ne rien perdre, afin de ne plus attendre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, gardé pour la fin. ─────────────────────────────
  {
    id:   'pour-suffit',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: '« Pour » suffit',
    titre: "« Pour » couvre tout ce que vous venez de faire. Le reste n'est qu'un habit.",
    paras: [
      "On a gardé ceci pour la fin exprès. <i>Afin de</i> et <i>afin que</i> ne sont pas une "
      + "deuxième règle à apprendre&nbsp;: ils obéissent exactement à la même — une personne, "
      + "verbe nu&nbsp;; deux personnes, «&nbsp;que&nbsp;» et le subjonctif. Ils sonnent "
      + "seulement plus écrit.",

      "Où chacun se met, en pratique&nbsp;: <b>pour</b> passe partout, du texto à la lettre de "
      + "réclamation, et personne ne le trouvera familier. <b>Afin de</b> et <b>afin que</b> "
      + "conviennent à une lettre officielle, un courriel à un employeur, un compte rendu. "
      + "Les employer dans un message à un ami sonne raide, sans être faux.",

      "Le but s'écrit aussi <b>sans aucun verbe</b>, et c'est souvent le plus court&nbsp;: "
      + "«&nbsp;<i>Je joins mon relevé d'emploi <b>pour votre dossier</b>.</i>&nbsp;» Là, il n'y "
      + "a personne à compter et rien à conjuguer&nbsp;: si votre phrase peut se dire ainsi, "
      + "prenez cette version.",
    ],
    retenir: "<b>«&nbsp;Pour&nbsp;» suffit.</b> «&nbsp;Afin de&nbsp;» et «&nbsp;afin que&nbsp;» "
           + "sont les mêmes, en plus écrit&nbsp;; ils ne changent aucune règle.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre courriel',
    titre: "Vous demandez un horaire de jour à votre employeur. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous commencez une formation le soir en septembre. Vous voulez que le responsable "
            + "des horaires vous place de jour, et vous voulez qu'il comprenne du premier coup ce "
            + "qu'il doit faire.",
    options: [
      { txt: "«&nbsp;Je commence une formation le soir en septembre. Je vous demande de me placer "
           + "de jour afin que je puisse y assister.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je commence une formation le soir en septembre. Je vous écris afin de me "
           + "placer de jour et pour que je puisse y assister.&nbsp;»",
        rat_t: "Les deux moitiés sont retournées&nbsp;: la personne est du mauvais côté à chaque fois.",
        rat: "«&nbsp;Afin de me placer&nbsp;» dit que <b>vous</b> vous placez de jour&nbsp;: le "
           + "responsable ne lit aucune demande. Et «&nbsp;pour que je puisse&nbsp;» répète une "
           + "personne qui est déjà celle de la phrase&nbsp;: il fallait l'inverse des deux — "
           + "nommer le responsable pour le placement, et laisser le verbe nu pour vous." },
      { txt: "«&nbsp;Je commence une formation le soir en septembre. Je vous demande de me placer "
           + "de jour afin de pouvoir y assister.&nbsp;»",
        rat_t: "Celle-là est presque juste — et c'est la seule vraie hésitation du point.",
        rat: "«&nbsp;Afin de pouvoir y assister&nbsp;» est correct&nbsp;: le verbe nu reprend la "
           + "personne la plus proche, c'est-à-dire vous. Mais la phrase vient de nommer votre "
           + "employeur juste avant, et un lecteur pressé peut lire que c'est <b>lui</b> qui doit "
           + "assister au cours. Dès que la phrase contient deux personnes, la version qui les "
           + "nomme ne se lit jamais de travers." },
    ],
    pourquoi: "La personne nommée pour ce que l'autre doit faire, le verbe nu pour ce que vous "
            + "faites — et quand un doute est possible, on nomme. <b>C'est tout le point en deux "
            + "lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au guichet. Cette fois, l'agent vous demande d'écrire votre demande.",
    consigne: "Vous laissez vos relevés et une note. Vous voulez que <b>le bureau</b> remplisse le "
            + "formulaire, et que <b>vous</b> soyez rappelé quand ce sera fait. Que "
            + "choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Je laisse mes relevés pour que vous remplissiez le formulaire. Merci de "
           + "m'appeler au 450 555-0142 pour me confirmer l'envoi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je laisse mes relevés pour remplir le formulaire. Merci de m'appeler au "
           + "450 555-0142 pour me confirmer l'envoi.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, et elle vous a mis le formulaire sur les bras.",
        rat: "La deuxième ligne est parfaite&nbsp;: vous y nommez la personne qui doit appeler, "
           + "et le verbe nu qui suit vous revient bien. Mais la première fait de vous celui qui "
           + "remplit&nbsp;: c'est «&nbsp;pour que <b>vous remplissiez</b>&nbsp;» qu'il faut, "
           + "puisque deux personnes agissent." },
      { txt: "«&nbsp;Je laisse mes relevés pour que vous remplissiez le formulaire. Merci de "
           + "m'appeler au 450 555-0142 pour que je confirme l'envoi.&nbsp;»",
        rat_t: "La première ligne est juste. C'est la seconde qui a retourné les rôles.",
        rat: "«&nbsp;Pour que je confirme&nbsp;» dit que c'est <b>vous</b> qui confirmez l'envoi "
           + "au bureau — l'inverse de ce que vous demandez. Ici la même personne fait les deux "
           + "actions du bout de phrase (on vous appelle, on vous confirme)&nbsp;: le verbe nu "
           + "suffit, «&nbsp;pour me confirmer&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: compter les personnes avant d'écrire, mettre "
            + "«&nbsp;que&nbsp;» et le subjonctif dès qu'elles sont deux, et laisser le verbe nu "
            + "quand il n'y en a qu'une.",
    attente: "Choisissez une réponse pour finir.",
  },

];
