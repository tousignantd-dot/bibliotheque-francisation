// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Tu » ou « tout » : quand on ne vous comprend pas
//
// Savoir n1-s22 (Système vocalique) — avec n1-s24 en arrière-plan, puisque le
// point passe par les lettres. Une ORDONNANCE : l'enseignant l'envoie à l'élève
// dont on répète les phrases, ou qui écrit « toute » pour « tu ».
// Dix minutes, dix écrans, niveau 1.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Quatre mini-leçons du dépôt touchent ces deux sons, et aucune n'est au niveau
// du destinataire :
//   · `module-n1-orientation`, « Trois sons pour commencer : [a], [i], [ou] » —
//     la seule de niveau 1, et elle ne traite QUE « ou » : le son « u » n'y est
//     pas, donc rien ne l'oppose à rien.
//   · `module-n2-secretaire`, « Ou et u : deux sons, deux mots » — l'opposition
//     complète, mais avec les mots d'un secrétariat (bureau, couloir, cours).
//   · `module-n5-quebec`, « Le son de ou et le son de u » et
//     `module-n5-rendezvous`, « Une et vous » — niveau 5, au téléphone.
// L'élève de niveau 1 à qui l'on demande de répéter ses phrases n'a donc lu que
// la première, qui ne parle pas du problème. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit mots qu'il dit tous les jours AVANT qu'on
//      lui explique où va la langue. Le classement se fait sur les lettres
//      écrites — c'est ce qu'il a sous les yeux.
//   2. PARTIEL, ET UN TEST DU CORPS. Pas de liste de paires, pas d'alphabet
//      phonétique. Un seul geste réutilisable : dire « i », garder la langue,
//      arrondir les lèvres — le « u » sort. Il marche sur un mot jamais vu.
//   3. LE MOT QUI CHANGE DE SENS EST DIT EN DERNIER (écran 8) : ce point n'est
//      pas un exercice de bouche, c'est un problème d'être compris. Le dire
//      d'entrée ferait peur avant d'avoir donné le geste.
//   4. LE MÉTALANGAGE APRÈS : « voyelle », à l'écran 3, une fois huit mots
//      triés — et c'est le seul mot savant du parcours, demandé par n1-s30.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Salut, bonjour, la rue, la
//      roue, douze, une minute, un texto, un formulaire.
//
// AUCUN SON, et c'est un choix, pas un manque. Un point express de dix minutes
// ne peut pas apprendre une voyelle à l'oreille — cela demande un enseignant
// devant soi. Ce qu'il peut faire, et que rien d'autre ne fait au niveau 1 :
// montrer que les deux sons s'écrivent différemment (une lettre contre deux),
// que le mot change avec eux, et donner le geste de bouche à répéter en classe.
// Tout se corrige par comparaison de chaînes : le parcours tourne dans un
// centre sans assistance.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'tu-ou-tout',
  titre:    "« Tu » ou « tout » : quand on ne vous comprend pas",
  surtitre: "Point express · 10 minutes",
  niveau:   1,
  savoir:   'n1-s22',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux questions',
    titre: "« Tu es prêt ? » et « Tout est prêt ? » — est-ce la même question ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Non. La première parle de <b>vous</b>. La deuxième parle des <b>choses</b>.",
        juste: true },
      { txt: "Oui, c'est la même question.",
        rat_t: "À l'oreille, elles se ressemblent beaucoup — c'est bien le problème.",
        rat: "Un seul son les sépare, et il est court. Mais les deux questions ne demandent pas la "
           + "même chose&nbsp;: à la première, vous répondez «&nbsp;oui, je suis prêt&nbsp;»&nbsp;; "
           + "à la deuxième, vous regardez vos affaires." },
      { txt: "Non&nbsp;: la deuxième phrase n'existe pas en français.",
        rat_t: "Elle existe, et vous l'entendrez souvent.",
        rat: "«&nbsp;Tout est prêt&nbsp;?&nbsp;» se dit avant de partir, avant de commencer un "
           + "cours, avant de fermer un magasin. Les deux phrases sont bonnes&nbsp;; ce qui les "
           + "sépare est un seul son." },
    ],
    pourquoi: "Deux questions différentes. Gardez-les en tête&nbsp;: on y revient à la fin.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-lettres',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit mots',
    titre: "Huit mots que vous dites chaque jour. Regardez les lettres.",
    consigne: "Aucune règle ne vous a été donnée — normal. Regardez seulement s'il y a "
            + "<b>une</b> lettre ou <b>deux</b> lettres collées.",
    colonnes: [
      { id: 'ou', t: "On écrit OU", b: "ou" },
      { id: 'u',  t: "On écrit U",  b: "u" },
    ],
    items: [
      { txt: "bonjour", sous: "le premier mot de la journée", ok: 'ou',
        rat: "Deux lettres collées à la fin&nbsp;: bonj<b>ou</b>r. C'est le son que presque toutes "
           + "les langues connaissent.",
        pourquoi: "bonj-ou-r : deux lettres." },
      { txt: "salut", sous: "entre amis", ok: 'u',
        rat: "Une seule lettre&nbsp;: sal<b>u</b>t. Ce n'est pas le même son que dans "
           + "«&nbsp;bonjour&nbsp;», même si les deux se ressemblent au début.",
        pourquoi: "sal-u-t : une seule lettre." },
      { txt: "vous", sous: "pour parler poliment", ok: 'ou',
        rat: "V<b>ou</b>s&nbsp;: deux lettres. C'est le mot le plus important du comptoir, et il a "
           + "le son du fond de la bouche.",
        pourquoi: "v-ou-s : deux lettres." },
      { txt: "une", sous: "une chaise, une carte", ok: 'u',
        rat: "<b>U</b>ne&nbsp;: une seule lettre, au tout début du mot. Beaucoup d'élèves disent "
           + "«&nbsp;oune&nbsp;» — c'est justement ce qu'on travaille.",
        pourquoi: "u-ne : une seule lettre." },
      { txt: "douze", sous: "un nombre", ok: 'ou',
        rat: "D<b>ou</b>ze&nbsp;: deux lettres. Les nombres se disent souvent au téléphone, alors "
           + "ce son-là doit être clair.",
        pourquoi: "d-ou-ze : deux lettres." },
      { txt: "minute", sous: "une minute, s'il vous plaît", ok: 'u',
        rat: "Min<b>u</b>te&nbsp;: une seule lettre. On l'entend cent fois par jour&nbsp;: "
           + "«&nbsp;une minute&nbsp;».",
        pourquoi: "min-u-te : une seule lettre." },
      { txt: "toujours", sous: "chaque fois", ok: 'ou',
        rat: "T<b>ou</b>j<b>ou</b>rs&nbsp;: deux fois le même son, deux fois deux lettres.",
        pourquoi: "t-ou-j-ou-rs : deux fois." },
      { txt: "rue", sous: "j'habite rue Papineau", ok: 'u',
        rat: "R<b>u</b>e&nbsp;: une seule lettre. Et le mot «&nbsp;roue&nbsp;» existe aussi, avec "
           + "deux lettres — on y revient bientôt.",
        pourquoi: "r-u-e : une seule lettre." },
    ],
    attente: "Tranchez les huit mots pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-geste',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le geste',
    titre: "Vous avez compté les lettres. Maintenant, la bouche.",
    paras: [
      "Vous venez de voir la première chose&nbsp;: le français écrit ces deux "
      + "<b>voyelles</b> autrement. Deux lettres collées, <b>ou</b>, pour le son de "
      + "«&nbsp;bonjour&nbsp;». Une seule lettre, <b>u</b>, pour le son de «&nbsp;salut&nbsp;».",

      "Dans la bouche, les lèvres font la même chose&nbsp;: elles avancent, en rond. Ce qui change, "
      + "c'est la <b>langue</b>. Pour <b>ou</b>, elle recule au fond. Pour <b>u</b>, elle monte en "
      + "avant, derrière les dents du bas.",

      "<b>Le geste, à faire dès maintenant&nbsp;:</b> dites «&nbsp;<b>i</b>&nbsp;», comme dans "
      + "«&nbsp;ici&nbsp;», et tenez le son. Ne bougez pas la langue. Arrondissez seulement les "
      + "lèvres, comme pour siffler. Le son qui sort, c'est le <b>u</b> de «&nbsp;salut&nbsp;».",
    ],
    retenir: "Deux lettres <b>ou</b>&nbsp;: la langue au fond. Une lettre <b>u</b>&nbsp;: dites "
           + "«&nbsp;i&nbsp;», puis arrondissez les lèvres sans bouger la langue.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : le mot change. ─────────────────────────────────────────
  {
    id:   'rue-ou-roue',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Rue ou roue',
    titre: "Vous dites : « Il y a un problème dans ma roue. » On comprend quoi ?",
    consigne: "Vous vouliez parler de la <b>rue</b> où vous habitez.",
    options: [
      { txt: "On comprend que le problème est sur <b>votre vélo ou votre auto</b>.",
        juste: true },
      { txt: "On comprend quand même&nbsp;: c'est presque le même mot.",
        rat_t: "Vous, vous savez ce que vous vouliez dire. La personne en face, non.",
        rat: "«&nbsp;Roue&nbsp;» et «&nbsp;rue&nbsp;» sont <b>deux mots différents</b>, pas deux "
           + "façons de dire le même. La personne en face n'a que le son pour choisir&nbsp;: elle "
           + "prendra celui qu'elle a entendu." },
      { txt: "On ne comprend rien du tout.",
        rat_t: "C'est pire que ça, et c'est pour ça que ça compte.",
        rat: "Si on ne comprenait rien, on vous ferait répéter. Le problème, c'est qu'on comprend "
           + "<b>autre chose</b>&nbsp;: la personne répond à côté, et vous ne savez même pas "
           + "pourquoi." },
    ],
    pourquoi: "Une lettre de différence, deux mots différents. <b>C'est ce qui rend ces deux sons "
            + "importants&nbsp;: ils changent le mot, pas seulement l'accent.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les paires qui comptent vraiment. ─────────────────────────────────
  {
    id:   'les-paires',
    type: 'notion',
    eye:  'Ce que ça vous rapporte',
    menu: 'Quatre paires',
    titre: "Quatre paires de mots que vous direz cette semaine.",
    paras: [
      "<b>tu</b> et <b>tout</b> — «&nbsp;<i>Tu viens&nbsp;?</i>&nbsp;» parle d'une personne. "
      + "«&nbsp;<i>Tout vient&nbsp;?</i>&nbsp;» parle des choses.",

      "<b>la rue</b> et <b>la roue</b> — l'une est dehors, sous vos pieds&nbsp;; l'autre est sous "
      + "l'autobus.",

      "<b>dessus</b> et <b>dessous</b> — «&nbsp;<i>le papier est dessus</i>&nbsp;»&nbsp;: on le "
      + "voit. «&nbsp;<i>Le papier est dessous</i>&nbsp;»&nbsp;: il est caché sous quelque chose. "
      + "Vous entendrez ces deux mots chaque fois qu'on cherchera un papier avec vous.",

      "Ne les apprenez pas en liste. Prenez-en <b>une</b>, celle qui vous sert le plus, et dites "
      + "les deux mots à voix haute, l'un après l'autre, cinq fois par jour. Le reste suivra.",
    ],
    retenir: "Deux mots qui ne changent que par ce son sont <b>deux mots</b>. Une paire par jour, "
           + "à voix haute.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases. Quel mot manque : « tu » ou « tout » ?",
    consigne: "Demandez-vous chaque fois&nbsp;: est-ce qu'on parle d'<b>une personne</b>, ou "
            + "de <b>toutes les choses</b>&nbsp;?",
    colonnes: [
      { id: 'tu',   t: "tu",   b: "tu" },
      { id: 'tout', t: "tout", b: "tout" },
    ],
    items: [
      { txt: "«&nbsp;… es en retard.&nbsp;»", sous: "un ami vous écrit", ok: 'tu',
        rat: "«&nbsp;Es&nbsp;» est le verbe d'une personne à qui l'on parle&nbsp;: "
           + "«&nbsp;<b>tu</b> es&nbsp;». Les choses ne sont pas en retard.",
        pourquoi: "Tu es en retard." },
      { txt: "«&nbsp;… est fermé aujourd'hui.&nbsp;»", sous: "une affiche sur la porte", ok: 'tout',
        rat: "Une affiche ne parle à personne en particulier. Elle parle de l'endroit "
           + "entier&nbsp;: «&nbsp;<b>tout</b> est fermé&nbsp;».",
        pourquoi: "Tout est fermé aujourd'hui." },
      { txt: "«&nbsp;… as ton cahier&nbsp;?&nbsp;»", sous: "un voisin de classe", ok: 'tu',
        rat: "«&nbsp;Ton cahier&nbsp;» s'adresse à une personne&nbsp;: c'est "
           + "«&nbsp;<b>tu</b> as&nbsp;».",
        pourquoi: "Tu as ton cahier ?" },
      { txt: "«&nbsp;… le monde est arrivé.&nbsp;»", sous: "au début du cours", ok: 'tout',
        rat: "«&nbsp;Tout le monde&nbsp;» veut dire <b>toutes les personnes</b>. C'est une "
           + "expression qui se retient comme un seul mot.",
        pourquoi: "Tout le monde est arrivé." },
      { txt: "«&nbsp;… habites où&nbsp;?&nbsp;»", sous: "une question entre amis", ok: 'tu',
        rat: "On pose la question à quelqu'un&nbsp;: «&nbsp;<b>tu</b> habites où&nbsp;?&nbsp;» "
           + "Les choses n'habitent nulle part.",
        pourquoi: "Tu habites où ?" },
      { txt: "«&nbsp;J'ai … compris.&nbsp;»", sous: "après une explication", ok: 'tout',
        rat: "Ici, le mot ne parle à personne&nbsp;: il veut dire «&nbsp;la chose "
           + "entière&nbsp;». «&nbsp;J'ai <b>tout</b> compris&nbsp;».",
        pourquoi: "J'ai tout compris." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Une phrase qui porte les deux sons. ───────────────────────────────
  {
    id:   'les-deux-ensemble',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Les deux ensemble',
    titre: "On vous demande : « Tu as tout ? » Qu'est-ce qu'on veut savoir ?",
    consigne: "Cette petite phrase contient les <b>deux</b> sons, l'un après l'autre. On vous la "
            + "dira souvent avant de partir.",
    options: [
      { txt: "On me demande si j'ai <b>toutes mes affaires</b> avec moi.", juste: true },
      { txt: "On me demande si je suis <b>tout seul</b>.",
        rat_t: "Vous avez pris le deuxième mot pour un autre.",
        rat: "«&nbsp;Tout seul&nbsp;» a deux mots, et le deuxième change tout. Ici, il n'y a que "
           + "«&nbsp;tout&nbsp;»&nbsp;: on parle de vos affaires, pas de vous." },
      { txt: "On me demande si tout va bien.",
        rat_t: "Presque la même phrase, et pas la même question.",
        rat: "«&nbsp;Tout va bien&nbsp;?&nbsp;» demande comment vous allez. "
           + "«&nbsp;Tu as tout&nbsp;?&nbsp;» demande si vous n'avez rien oublié. C'est le verbe "
           + "qui les sépare." },
    ],
    pourquoi: "«&nbsp;<b>Tu</b> as <b>tout</b>&nbsp;?&nbsp;» — la personne, puis les choses. "
            + "Dites-la à voix haute&nbsp;: c'est votre exercice, et il tient en trois mots.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Ce qu'on fait quand on n'est pas compris — gardé pour la fin. ─────
  {
    id:   'si-on-ne-comprend-pas',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "Si on vous fait répéter",
    titre: "On vous fera répéter. Ce n'est pas grave, et voici quoi faire.",
    paras: [
      "On a gardé ceci pour la fin, parce que ce parcours ne va pas régler le son en dix "
      + "minutes&nbsp;: cette voyelle-là n'existe pas dans beaucoup de langues, et elle "
      + "s'entraîne pendant des semaines. Ce n'est pas un défaut&nbsp;; c'est un muscle.",

      "Alors, quand on vous fait répéter&nbsp;: <b>ne répétez pas plus fort.</b> Le volume ne "
      + "change rien au son. Refaites plutôt le geste — la langue en avant pour "
      + "«&nbsp;u&nbsp;», au fond pour «&nbsp;ou&nbsp;» — et redites le mot doucement.",

      "Et si ça ne passe toujours pas, <b>donnez un autre mot autour</b>&nbsp;: "
      + "«&nbsp;<i>la rue&nbsp;: rue Papineau, où j'habite.</i>&nbsp;» La personne comprend tout de "
      + "suite. Ce n'est pas de la triche&nbsp;: c'est ce que font tous ceux qui parlent deux "
      + "langues.",
    ],
    retenir: "Pas plus fort&nbsp;: refaire le geste, et ajouter un mot autour.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Vous écrivez à votre enseignante. Quelle version est correcte ?",
    consigne: "Vous voulez dire que vous avez compris l'exercice au complet. Trois versions du "
            + "même message&nbsp;: une seule est correcte.",
    options: [
      { txt: "«&nbsp;Bonjour. J'ai tout compris. Merci beaucoup.&nbsp;»", juste: true },
      { txt: "«&nbsp;Bonjour. J'ai tu compris. Merci beaucoup.&nbsp;»",
        rat_t: "Les deux mots se ressemblent à l'oreille, et pas à l'écrit.",
        rat: "«&nbsp;Tu&nbsp;» sert à parler <b>à quelqu'un</b>&nbsp;: tu as, tu viens, tu es. "
           + "Ici, vous voulez dire «&nbsp;la chose entière&nbsp;»&nbsp;: c'est "
           + "«&nbsp;<b>tout</b>&nbsp;», avec ses quatre lettres." },
      { txt: "«&nbsp;Bonjour. J'ai toute compris. Merci beaucoup.&nbsp;»",
        rat_t: "Vous avez entendu le bon mot. C'est la fin qui a glissé.",
        rat: "«&nbsp;Toute&nbsp;» existe, mais devant un nom féminin&nbsp;: «&nbsp;toute la "
           + "journée&nbsp;». Devant un verbe, on écrit «&nbsp;<b>tout</b>&nbsp;»&nbsp;: j'ai tout "
           + "compris, j'ai tout fini." },
    ],
    pourquoi: "<b>J'ai tout compris.</b> Le son décide du mot, et le mot décide des lettres.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient aux deux questions du début.",
    consigne: "Vous partez en voyage avec un ami. Il est devant la porte avec les valises. "
            + "Vous lui demandez si <b>les affaires</b> sont prêtes. Vous dites quoi&nbsp;?",
    options: [
      { txt: "«&nbsp;Tout est prêt&nbsp;?&nbsp;»", juste: true },
      { txt: "«&nbsp;Tu es prêt&nbsp;?&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle demande autre chose.",
        rat: "Rien n'est faux dedans&nbsp;: vous demandez à votre ami s'il est prêt, lui. Mais vous "
           + "vouliez parler des <b>valises</b>. Un seul son sépare les deux questions, et il "
           + "change la réponse que vous allez recevoir." },
      { txt: "«&nbsp;Tout es prêt&nbsp;?&nbsp;»",
        rat_t: "Le bon mot, et le verbe de l'autre phrase.",
        rat: "«&nbsp;Es&nbsp;» va avec «&nbsp;tu&nbsp;»&nbsp;: tu es. Avec "
           + "«&nbsp;tout&nbsp;», le verbe est «&nbsp;<b>est</b>&nbsp;»&nbsp;: tout est prêt, tout "
           + "est fermé, tout est là." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: voir que les deux sons s'écrivent "
            + "différemment, savoir que le mot change avec eux, et connaître le geste à refaire "
            + "quand on vous fait répéter.",
    attente: "Choisissez une réponse pour finir.",
  },

];
