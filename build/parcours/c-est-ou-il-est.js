// ═══════════════════════════════════════════════════════════════════════════
// Point express — « C'est mon voisin », « il est gentil »
//
// Savoir n2-s11 (Phrases à construction particulière : le présentatif c'est),
// avec n2-s19 en arrière-plan (les pronoms sujets il / elle). Une ORDONNANCE :
// l'enseignant l'envoie à un élève qui dit « il est mon voisin » ou « c'est
// gentil » pour parler d'une personne. Dix minutes, dix écrans, niveau 2.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Deux mini-leçons du dépôt emploient « c'est », et aucune ne l'oppose à
// « il est » :
//   · `module-n1-orientation` — « C'est · Ce n'est pas · C'est ici ? » : « c'est »
//     sert à dire un LIEU, jamais à présenter quelqu'un.
//   · `module-n2-couloirs` — « Il y a… et c'est… » : elle oppose « c'est » à
//     « il y a », donc l'élève range « c'est » du côté des choses et des
//     endroits, et il n'a rien pour parler d'une personne.
// Un élève qui a lu ces deux-là dit « il est mon frère » sans savoir pourquoi
// on le reprend. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases entendues AVANT qu'on lui dise
//      qu'il y a deux formes. La règle de l'écran 3 est le constat de son tri.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de constructions. Un TEST — que
//      vient-il APRÈS ? un petit mot comme un / une / mon, ou pas — qui marche
//      sur une phrase jamais vue.
//   3. LE CAS QU'ON CROIT SIMPLE (« il est ») EST DIT EN SECOND. Le nommer
//      d'entrée ferait croire à deux règles ; il n'y en a qu'une, et elle
//      regarde le mot d'après.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Déterminant » n'est écrit qu'une fois,
//      à l'écran 4, une fois la chose manipulée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Une présentation en classe,
//      un texto, un appel à un propriétaire, une note à l'école, un comptoir.
//
// Aucun média : les deux formes se prononcent clairement et l'élève les entend
// très bien. Ce qu'il ne sait pas, c'est laquelle choisir — et ça se voit dans
// le mot qui suit, pas dans le son.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'c-est-ou-il-est',
  titre:    "« C'est mon voisin », « il est gentil »",
  surtitre: "Point express · 10 minutes",
  niveau:   2,
  savoir:   'n2-s11',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Vous présentez un ami à la classe. Quelle phrase dites-vous ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "C'est mon ami Rachid.", juste: true },
      { txt: "Il est mon ami Rachid.",
        rat_t: "On vous comprend très bien. Mais personne ne dit ça.",
        rat: "Vous avez pensé à Rachid, donc vous avez dit «&nbsp;il&nbsp;». C'est logique. "
           + "Pourtant, dès qu'on met un petit mot devant — <b>mon</b> ami, <b>un</b> ami, "
           + "<b>le</b> voisin — le français demande <b>c'est</b>. On va voir pourquoi." },
      { txt: "Ce est mon ami Rachid.",
        rat_t: "Le mot est le bon, mais il ne s'écrit jamais entier ici.",
        rat: "Devant <b>est</b>, «&nbsp;ce&nbsp;» perd sa voyelle et prend une apostrophe&nbsp;: "
           + "<b>c'est</b>. Comme «&nbsp;je&nbsp;» devient «&nbsp;j'ai&nbsp;». Il n'y a pas "
           + "d'autre façon de l'écrire." },
    ],
    pourquoi: "«&nbsp;C'est mon ami Rachid.&nbsp;» Gardez cette phrase&nbsp;: on y revient au "
            + "dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-suite',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases correctes. Regardez ce qui vient juste après le verbe.",
    consigne: "Toutes ces phrases sont justes. Ne cherchez pas la règle&nbsp;: regardez seulement "
            + "le <b>premier mot après « est »</b>. Est-ce un petit mot comme <i>un</i>, "
            + "<i>une</i>, <i>mon</i>, <i>le</i>&nbsp;? Ou un mot qui décrit&nbsp;?",
    colonnes: [
      { id: 'petit', t: "Un petit mot d'abord", b: "Un petit mot" },
      { id: 'decrit', t: "Un mot qui décrit",   b: "Un mot qui décrit" },
    ],
    items: [
      { txt: "C'est <b>une</b> infirmière.", sous: "on présente quelqu'un à la clinique", ok: 'petit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>une</b>. C'est un petit mot, et il annonce le "
           + "nom du métier qui vient après.",
        pourquoi: "« une » : un petit mot d'abord." },
      { txt: "Elle est <b>gentille</b>.", sous: "un texto à une amie", ok: 'decrit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>gentille</b>. Aucun petit mot&nbsp;: on décrit "
           + "directement la personne.",
        pourquoi: "« gentille » décrit la personne." },
      { txt: "C'est <b>mon</b> voisin.", sous: "on présente quelqu'un dans l'entrée", ok: 'petit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>mon</b>. Encore un petit mot posé devant le nom.",
        pourquoi: "« mon » : un petit mot d'abord." },
      { txt: "Il est <b>malade</b> depuis hier.", sous: "une note à l'école", ok: 'decrit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>malade</b>. Rien entre les deux&nbsp;: c'est "
           + "un mot qui décrit.",
        pourquoi: "« malade » décrit la personne." },
      { txt: "C'est <b>le</b> directeur.", sous: "au comptoir d'un centre", ok: 'petit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>le</b>. Un petit mot, puis le nom.",
        pourquoi: "« le » : un petit mot d'abord." },
      { txt: "Elle est <b>étudiante</b>.", sous: "on parle de sa fille", ok: 'decrit',
        rat: "Un métier peut se dire sans petit mot&nbsp;: on ne dit pas <i>ce qu'elle a</i>, "
           + "on dit <b>ce qu'elle est</b>. Rien après «&nbsp;est&nbsp;», donc.",
        pourquoi: "Rien avant « étudiante »." },
      { txt: "C'est <b>un</b> bon restaurant.", sous: "un message à un collègue", ok: 'petit',
        rat: "Après «&nbsp;est&nbsp;», il y a <b>un</b>. Le mot qui décrit (bon) vient après le "
           + "petit mot, pas à sa place.",
        pourquoi: "« un » : un petit mot d'abord." },
      { txt: "Il est <b>en retard</b>.", sous: "au téléphone avec un employeur", ok: 'decrit',
        rat: "«&nbsp;En retard&nbsp;» dit dans quel état il est, comme «&nbsp;malade&nbsp;». "
           + "Ce n'est pas un nom annoncé par un petit mot.",
        pourquoi: "« en retard » décrit son état." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-constat',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Regardez vos deux colonnes : ce sont exactement « c'est » et « il est ».",
    paras: [
      "Dans votre colonne de gauche, toutes les phrases commencent par <b>c'est</b>. Dans celle "
      + "de droite, toutes commencent par <b>il est</b> ou <b>elle est</b>. Vous ne le saviez "
      + "pas, et vous avez trié juste.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> regardez le mot que vous "
      + "voulez mettre après le verbe. S'il y a d'abord un petit mot — <i>un</i>, <i>une</i>, "
      + "<i>le</i>, <i>la</i>, <i>mon</i>, <i>ma</i> — écrivez <b>c'est</b>. S'il n'y a pas de "
      + "petit mot, écrivez <b>il est</b> ou <b>elle est</b>.",

      "Ces petits mots s'appellent des <b>déterminants</b>. Votre enseignant emploiera ce mot-là. "
      + "Vous, vous avez seulement besoin de les reconnaître&nbsp;: vous les employez déjà tous "
      + "les jours.",
    ],
    retenir: "Un petit mot après le verbe&nbsp;: <b>c'est</b>. Pas de petit mot&nbsp;: "
           + "<b>il est</b>, <b>elle est</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : le métier. ─────────────────────────────────────
  {
    id:   'le-metier',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Le métier',
    titre: "Le métier se dit des deux façons. Mais pas avec les mêmes mots.",
    consigne: "Vous parlez de votre sœur, qui travaille comme infirmière. Quelle phrase est "
            + "<b>fautive</b>&nbsp;?",
    options: [
      { txt: "Elle est une infirmière.", juste: true },
      { txt: "Elle est infirmière.",
        rat_t: "Celle-là est correcte, et c'est la plus courante.",
        rat: "Aucun petit mot après «&nbsp;est&nbsp;»&nbsp;: on emploie donc <b>elle est</b>. "
           + "C'est la phrase que vous entendrez le plus souvent au Québec." },
      { txt: "C'est une infirmière.",
        rat_t: "Celle-là est correcte aussi.",
        rat: "Il y a le petit mot <b>une</b> après le verbe&nbsp;: on emploie donc <b>c'est</b>. "
           + "Les deux phrases correctes disent la même chose&nbsp;; ce qui change, c'est le "
           + "petit mot." },
    ],
    pourquoi: "«&nbsp;Elle est une infirmière&nbsp;» mélange les deux&nbsp;: le petit mot "
            + "<b>une</b> appelle <b>c'est</b>. C'est la faute la plus fréquente, et la seule "
            + "que le test attrape à tous les coups.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La chose et l'endroit. ────────────────────────────────────────────
  {
    id:   'chose-endroit',
    type: 'notion',
    eye:  'Pas seulement les personnes',
    menu: 'Les choses',
    titre: "Le même test marche pour une chose, un endroit, une date.",
    paras: [
      "«&nbsp;<b>C'est</b> une bonne école.&nbsp;» — petit mot <i>une</i>, donc "
      + "«&nbsp;c'est&nbsp;». «&nbsp;<b>Elle est</b> loin de chez moi.&nbsp;» — pas de petit "
      + "mot, donc «&nbsp;elle est&nbsp;», et «&nbsp;elle&nbsp;» remplace l'école.",

      "«&nbsp;<b>C'est</b> le mardi.&nbsp;» «&nbsp;<b>C'est</b> mon dernier jour.&nbsp;» "
      + "«&nbsp;<b>C'est</b> un long trajet.&nbsp;» Toujours un petit mot juste après.",

      "Une seule chose est particulière&nbsp;: quand on ne parle de rien de précis — le temps "
      + "qu'il fait, une heure, une situation — on dit <b>c'est</b>. «&nbsp;C'est loin.&nbsp;» "
      + "«&nbsp;C'est ouvert.&nbsp;» «&nbsp;C'est fermé le dimanche.&nbsp;» Il n'y a personne ni "
      + "rien derrière ce «&nbsp;c'&nbsp;».",
    ],
    retenir: "Le test vaut pour tout. Et quand on ne parle de <b>rien de précis</b>, c'est "
           + "toujours «&nbsp;c'est&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Une seule question&nbsp;: y a-t-il un petit mot juste après le verbe&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "C'est mon frère. Il est très occupé.", ok: 'ok',
        rat: "Petit mot <b>mon</b> dans la première&nbsp;: «&nbsp;c'est&nbsp;». Rien avant "
           + "«&nbsp;occupé&nbsp;» dans la seconde&nbsp;: «&nbsp;il est&nbsp;». Les deux sont "
           + "justes.",
        pourquoi: "Les deux phrases suivent le test. Juste." },
      { txt: "Il est le professeur de mon fils.", ok: 'faux',
        rat: "Le petit mot <b>le</b> est là&nbsp;: il faut «&nbsp;<b>C'est</b> le professeur de "
           + "mon fils.&nbsp;» C'est la même faute qu'avec «&nbsp;une infirmière&nbsp;».",
        pourquoi: "Il faut « C'est le professeur »." },
      { txt: "Elle est en congé cette semaine.", ok: 'ok',
        rat: "Pas de petit mot après «&nbsp;est&nbsp;»&nbsp;: «&nbsp;elle est&nbsp;» est bien "
           + "la forme attendue.",
        pourquoi: "Pas de petit mot : « elle est ». Juste." },
      { txt: "C'est fermé le dimanche.", ok: 'ok',
        rat: "On ne parle de personne ni de rien de précis&nbsp;: c'est le cas où l'on dit "
           + "toujours «&nbsp;c'est&nbsp;».",
        pourquoi: "Rien de précis derrière : « c'est ». Juste." },
      { txt: "C'est gentille, ma voisine.", ok: 'faux',
        rat: "<b>Gentille</b> décrit la personne, et il n'y a aucun petit mot devant. Il faut "
           + "«&nbsp;<b>Elle est</b> gentille, ma voisine.&nbsp;»",
        pourquoi: "Il faut « Elle est gentille »." },
      { txt: "C'est une longue journée.", ok: 'ok',
        rat: "Le petit mot <b>une</b> est là, donc «&nbsp;c'est&nbsp;». Le mot qui décrit "
           + "(longue) vient après le petit mot, il ne le remplace pas.",
        pourquoi: "« une » est là : « c'est ». Juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas fréquent : la personne qu'on vient de nommer. ──────────────
  {
    id:   'apres-le-nom',
    type: 'verif',
    eye:  'Vérification',
    menu: 'La suite',
    titre: "Vous avez présenté quelqu'un. Vous continuez à parler de lui.",
    consigne: "Vous avez dit&nbsp;: «&nbsp;C'est mon voisin Marc.&nbsp;» Vous voulez maintenant "
            + "dire qu'il travaille à l'hôpital. Quelle phrase&nbsp;?",
    options: [
      { txt: "Il travaille à l'hôpital.", juste: true },
      { txt: "C'est travaille à l'hôpital.",
        rat_t: "«&nbsp;C'est&nbsp;» ne se met pas devant un verbe.",
        rat: "«&nbsp;C'est&nbsp;» sert à <b>présenter</b>&nbsp;: il annonce un nom, avec son petit "
           + "mot. Dès qu'on raconte ce que la personne <b>fait</b>, on emploie <b>il</b> ou "
           + "<b>elle</b>." },
      { txt: "C'est il travaille à l'hôpital.",
        rat_t: "Vous avez gardé les deux, au cas où.",
        rat: "Une phrase n'a qu'un seul sujet. Une fois la personne présentée, «&nbsp;c'est&nbsp;» "
           + "a fini son travail&nbsp;: on continue avec <b>il</b> seul." },
    ],
    pourquoi: "<b>«&nbsp;C'est&nbsp;» présente une fois. Ensuite, on dit «&nbsp;il&nbsp;» ou "
            + "«&nbsp;elle&nbsp;».</b> C'est ce qui rend une conversation naturelle.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le pluriel, dit en dernier : rien de neuf à retenir. ──────────────
  {
    id:   'le-pluriel',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Au pluriel',
    titre: "Quand il y en a plusieurs, rien ne change de votre côté.",
    paras: [
      "«&nbsp;<b>Ce sont</b> mes voisins.&nbsp;» «&nbsp;<b>Ils sont</b> gentils.&nbsp;» Le test "
      + "est exactement le même&nbsp;: petit mot <i>mes</i>, donc la forme qui présente&nbsp;; "
      + "pas de petit mot, donc <b>ils</b>.",

      "À l'oral, au Québec, vous entendrez très souvent «&nbsp;<b>c'est</b> mes voisins&nbsp;». "
      + "Ce n'est pas une erreur de votre oreille&nbsp;: c'est ce qui se dit. Mais quand vous "
      + "<b>écrivez</b> — un courriel à l'école, un message à un propriétaire — écrivez "
      + "«&nbsp;ce sont&nbsp;».",

      "Autrement dit&nbsp;: <b>une seule chose à surveiller</b>, et c'est toujours le mot qui "
      + "vient juste après le verbe.",
    ],
    retenir: "Au pluriel&nbsp;: <b>ce sont</b> à l'écrit, <b>ils sont</b> / <b>elles sont</b> "
           + "pour décrire.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Amel écrit à l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Elle prévient que quelqu'un d'autre viendra chercher sa fille. Trois versions du "
            + "même message&nbsp;: une seule est correcte partout.",
    options: [
      { txt: "C'est ma sœur qui vient chercher Nour. Elle est grande, avec un manteau rouge.",
        juste: true },
      { txt: "Il est ma sœur qui vient chercher Nour. Elle est grande, avec un manteau rouge.",
        rat_t: "La deuxième phrase est parfaite. La première a lâché sur le premier mot.",
        rat: "Le petit mot <b>ma</b> est juste après le verbe&nbsp;: il faut donc "
           + "«&nbsp;<b>C'est</b> ma sœur&nbsp;». Vous aviez le test&nbsp;; il s'est perdu à la "
           + "première phrase." },
      { txt: "C'est ma sœur qui vient chercher Nour. C'est grande, avec un manteau rouge.",
        rat_t: "La première phrase est parfaite. C'est la deuxième qui a lâché.",
        rat: "<b>Grande</b> décrit la personne, sans petit mot devant&nbsp;: il faut "
           + "«&nbsp;<b>Elle est</b> grande&nbsp;». Et une fois la sœur présentée, on continue "
           + "avec «&nbsp;elle&nbsp;»." },
    ],
    pourquoi: "«&nbsp;C'est ma sœur&nbsp;» présente. «&nbsp;Elle est grande&nbsp;» décrit. "
            + "<b>C'est tout le point en deux phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « C'est mon ami Rachid. »",
    consigne: "Vous continuez la présentation&nbsp;: vous voulez dire qu'il est <b>mécanicien</b> "
            + "et qu'il est <b>très drôle</b>. Quelle suite&nbsp;?",
    options: [
      { txt: "Il est mécanicien. Il est très drôle.", juste: true },
      { txt: "C'est mécanicien. C'est très drôle.",
        rat_t: "Vous avez gardé la forme du début, celle qui présente.",
        rat: "«&nbsp;Mécanicien&nbsp;» n'a aucun petit mot devant, et «&nbsp;drôle&nbsp;» le "
           + "décrit&nbsp;: les deux appellent <b>il est</b>. «&nbsp;C'est&nbsp;» a déjà fait son "
           + "travail à la phrase d'avant." },
      { txt: "C'est un mécanicien. C'est très drôle.",
        rat_t: "La première phrase est correcte. La seconde ne l'est pas.",
        rat: "«&nbsp;C'est un mécanicien&nbsp;» passe très bien&nbsp;: le petit mot <b>un</b> est "
           + "là. Mais «&nbsp;drôle&nbsp;» décrit Rachid, sans petit mot&nbsp;: "
           + "«&nbsp;<b>Il est</b> très drôle.&nbsp;»" },
    ],
    pourquoi: "Vous avez fait les deux choses&nbsp;: regarder le mot juste après le verbe, et "
            + "passer à «&nbsp;il&nbsp;» une fois la personne présentée.",
    attente: "Choisissez une réponse pour finir.",
  },

];
