// ═══════════════════════════════════════════════════════════════════════════
// Point express — « La personne qui appelle » ou « que j'appelle » ?
//
// Savoirs n4-s14 (phrases subordonnées relatives) et n4-s24 (pronoms
// relatifs). Dix minutes, dix écrans. Une ORDONNANCE : l'enseignant l'envoie
// à un élève dont l'écrit montre « le formulaire qui j'ai rempli » ou « la
// dame qu'a téléphoné ».
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Deux mini-leçons couvrent déjà le sujet, toutes deux au-dessus du niveau 4 :
// `module-n5-services` (« Qui, que, dont, où ») et `module-n6-relations`
// (« Qui, que, où : tout dire en une seule phrase »). Les cinq écarts tenus :
//
//   1. DEUX MOTS, PAS QUATRE. Ni « dont », ni « où », ni l'accord du
//      participe après « que », ni la structure Dét + nom + relative. Le
//      programme du niveau 4 demande de RECONNAÎTRE une relative et de
//      comprendre le rôle de qui et de que : ce point express s'y tient.
//   2. INDUCTIF. L'élève range huit phrases AVANT qu'aucune règle ne soit
//      donnée. La règle de l'écran 3 est un constat de son propre tri.
//   3. UN TEST SANS MÉTALANGAGE. Les deux mini-leçons expliquent par le sujet
//      et le complément. Ici, une seule question, posée sur ce qu'on VOIT :
//      « après le mot, est-ce que quelqu'un est déjà là pour faire l'action ? »
//      Les mots « subordonnée » et « sujet » n'arrivent qu'à l'écran 3, une
//      fois le tri fait.
//   4. LE CONTRESENS DE SENS EST TRAITÉ DE FRONT (écran 5). Aucune des deux
//      mini-leçons ne le nomme : beaucoup d'élèves croient que « qui » sert
//      pour les personnes et « que » pour les choses. Tant que cette idée
//      tient, le test ne peut pas s'installer.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS, JAMAIS À UN MODULE. Une annonce
//      d'appartement, un texto, un courriel à un employeur, une note à
//      l'école. L'élève doit reconnaître la faute partout.
//
// Aucun média : la faute est invisible à l'oral — « qu'a » et « qui a » se
// ressemblent trop — et c'est précisément le sujet de l'écran 4.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'qui-ou-que',
  titre:    "« La personne qui appelle » ou « que j'appelle » ?",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s14 · n4-s24',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Qui téléphone ?',
    titre: "Une seule de ces phrases dit que c'est VOUS qui téléphonez.",
    consigne: "Répondez avec ce que vous savez déjà — ou à l'oreille. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "« La personne que j'appelle ne répond jamais. »", juste: true },
      { txt: "« La personne qui appelle ne répond jamais. »",
        rat_t: "Cette phrase-là dit le contraire.",
        rat: "Ici, c'est <b>elle</b> qui compose le numéro, pas vous — et du coup la phrase ne "
           + "veut plus dire grand-chose&nbsp;: quelqu'un qui appelle et qui ne répond pas. Un "
           + "seul mot change, et les rôles s'inversent." },
      { txt: "Les deux disent la même chose.",
        rat_t: "Un seul mot, et deux sens opposés.",
        rat: "C'est ce qui rend la faute coûteuse&nbsp;: personne ne vous corrige, mais votre "
           + "lecteur comprend l'inverse de ce que vous vouliez dire. Relisez les deux "
           + "phrases&nbsp;: dans l'une, vous composez le numéro&nbsp;; dans l'autre, on vous "
           + "appelle." },
    ],
    pourquoi: "«&nbsp;La personne <b>que j'appelle</b>&nbsp;». Retenez la phrase entière pour "
            + "l'instant&nbsp;; on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases à compléter. Quel mot manque ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez la phrase dans votre tête, "
            + "les deux fois, et gardez celle qui passe.",
    colonnes: [
      { id: 'qui', t: 'qui', b: 'qui' },
      { id: 'que', t: 'que · qu’', b: 'que · qu’' },
    ],
    items: [
      { txt: "Le camion ___ bloque l'entrée est là depuis hier.", ok: 'qui',
        rat: "Juste après le mot, il n'y a personne&nbsp;: le verbe part tout de suite. "
           + "Retenez ça, on y revient dans un écran.",
        pourquoi: "qui bloque. Le verbe part tout de suite." },
      { txt: "Le formulaire ___ vous avez signé est incomplet.", ok: 'que',
        rat: "Juste après le mot, il y a déjà quelqu'un&nbsp;: <b>vous</b>. C'est lui qui "
           + "signe, pas le formulaire.",
        pourquoi: "que vous avez signé. Quelqu'un est déjà là : vous." },
      { txt: "La dame ___ m'a répondu était très patiente.", ok: 'qui',
        rat: "«&nbsp;M'&nbsp;» n'est pas la personne qui répond&nbsp;: c'est moi qui reçois la "
           + "réponse. Rien ne fait l'action à part la dame.",
        pourquoi: "qui m'a répondu. Personne d'autre ne répond." },
      { txt: "L'autobus ___ je prends le matin passe à 7 h 10.", ok: 'que',
        rat: "«&nbsp;Je&nbsp;» est là, juste après. C'est moi qui prends l'autobus&nbsp;; "
           + "l'autobus ne prend rien.",
        pourquoi: "que je prends. Quelqu'un est déjà là : je." },
      { txt: "Les papiers ___ manquent au dossier sont chez le notaire.", ok: 'qui',
        rat: "Le verbe suit immédiatement. Ce sont les papiers eux-mêmes qui manquent.",
        pourquoi: "qui manquent. Le verbe suit immédiatement." },
      { txt: "Le numéro ___ elle m'a donné ne fonctionne pas.", ok: 'que',
        rat: "«&nbsp;Elle&nbsp;» est déjà là pour donner. Le numéro, lui, ne donne rien à "
           + "personne.",
        pourquoi: "qu'elle m'a donné. « elle » est déjà là — et « que » s'élide." },
      { txt: "L'appartement ___ est au sous-sol coûte moins cher.", ok: 'qui',
        rat: "Rien entre le mot et le verbe. C'est l'appartement qui est au sous-sol.",
        pourquoi: "qui est. Rien entre le mot et le verbe." },
      { txt: "Le message ___ tu as laissé était coupé.", ok: 'que',
        rat: "«&nbsp;Tu&nbsp;» occupe déjà la place. C'est toi qui laisses le message.",
        pourquoi: "que tu as laissé. Quelqu'un est déjà là : tu." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'La place est-elle prise ?',
    titre: "Vous n'avez pas regardé le sens. Vous avez regardé le mot d'après.",
    paras: [
      "Dans votre colonne «&nbsp;que&nbsp;», il y avait toujours quelqu'un juste "
      + "après&nbsp;: <b>vous</b>, <b>je</b>, <b>elle</b>, <b>tu</b>. Dans la colonne "
      + "«&nbsp;qui&nbsp;», rien&nbsp;: le verbe partait tout de suite. Voilà toute la règle, "
      + "et vous venez de la trouver sans qu'on vous la dise.",

      "<b>Le test, à poser sur n'importe quelle phrase&nbsp;:</b> après le mot, regardez <b>un "
      + "seul mot plus loin</b>. Est-ce que quelqu'un est <b>déjà là</b> pour faire l'action&nbsp;? "
      + "Si oui → <i>que</i>. Si la place est vide et que le verbe arrive → <i>qui</i>.",

      "Votre enseignant appellera ce morceau de phrase une <b>subordonnée relative</b>, et il "
      + "dira que «&nbsp;qui&nbsp;» en est le <b>sujet</b>. Vous n'avez pas besoin des noms pour "
      + "vous en servir, mais vous les entendrez.",
    ],
    retenir: "<b>La place du sujet est-elle déjà prise&nbsp;?</b> Oui → <i>que</i>. "
           + "Non → <i>qui</i>. Une question se repose sur n'importe quelle phrase&nbsp;; "
           + "une explication s'oublie.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège de l'oreille : « qu'a » n'existe pas. ────────────────────
  {
    id:   'jamais-delision',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: "Ce qu'on entend",
    titre: "« La dame qu'a téléphoné » s'entend partout. Ça ne s'écrit nulle part.",
    consigne: "Vous écrivez à votre employeur au sujet d'un appel reçu. Quelle phrase "
            + "écrivez-vous&nbsp;?",
    options: [
      { txt: "« La dame qui a téléphoné voulait votre numéro de dossier. »", juste: true },
      { txt: "« La dame qu'a téléphoné voulait votre numéro de dossier. »",
        rat_t: "Vous avez écrit ce que vous entendez, et c'est logique.",
        rat: "À l'oral, on entend bien «&nbsp;<i>k a</i>&nbsp;» — les deux mots se collent. Mais "
           + "«&nbsp;qui&nbsp;» ne perd <b>jamais</b> son <i>i</i>, même devant une voyelle. "
           + "Seul «&nbsp;que&nbsp;» s'écrit «&nbsp;qu'&nbsp;»." },
      { txt: "« La dame que a téléphoné voulait votre numéro de dossier. »",
        rat_t: "Vous avez bien vu qu'il fallait choisir. Vous avez pris le mauvais mot.",
        rat: "Deux choses ne vont pas&nbsp;: après le mot, personne n'est là pour téléphoner à "
           + "la place de la dame — donc c'est «&nbsp;qui&nbsp;». Et «&nbsp;que&nbsp;» ne reste "
           + "jamais entier devant une voyelle&nbsp;: il devient «&nbsp;qu'&nbsp;»." },
    ],
    pourquoi: "<b>«&nbsp;qui&nbsp;» ne s'élide jamais&nbsp;; «&nbsp;que&nbsp;» s'élide "
            + "toujours.</b> Autrement dit&nbsp;: si vous voyez «&nbsp;qu'&nbsp;» avec une "
            + "apostrophe, quelqu'un doit suivre.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le contresens de fond, traité de front. ───────────────────────────
  {
    id:   'ni-personne-ni-chose',
    type: 'notion',
    eye:  "L'idée qu'il faut jeter",
    menu: 'Ni personne, ni chose',
    titre: "« Qui » ne veut pas dire une personne. Et « que » ne veut pas dire une chose.",
    paras: [
      "C'est l'idée fausse la plus répandue, et elle vient d'ailleurs&nbsp;: dans une question, "
      + "«&nbsp;qui&nbsp;» demande bien une personne — «&nbsp;qui a appelé&nbsp;?&nbsp;». Au "
      + "milieu d'une phrase, ce n'est plus du tout le même mot.",

      "La preuve tient en deux phrases&nbsp;: «&nbsp;<b>le camion qui</b> bloque l'entrée&nbsp;» "
      + "— un camion n'est pas une personne. «&nbsp;<b>La dame que</b> j'ai vue&nbsp;» — une dame "
      + "n'est pas une chose. Les deux mots servent aux personnes comme aux objets.",

      "Ce qui décide, c'est uniquement <b>ce qui vient après</b>. Tant que vous cherchez si vous "
      + "parlez d'un être humain ou d'un objet, vous vous trompez une fois sur deux — et jamais "
      + "aux mêmes endroits, ce qui rend la faute impossible à corriger seul.",
    ],
    retenir: "Le sens ne décide <b>rien</b>. Seule décide la place juste après le mot&nbsp;: "
           + "prise → <i>que</i>, libre → <i>qui</i>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-correct',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Une seule chose à regarder&nbsp;: le mot juste après <i>qui</i> ou <i>que</i>.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Le logement que nous visitons samedi a deux chambres.", ok: 'ok',
        rat: "«&nbsp;Nous&nbsp;» est déjà là pour visiter&nbsp;: la place est prise, donc "
           + "<i>que</i>. La phrase tient.",
        pourquoi: "La place est prise par « nous ». Juste." },
      { txt: "Le voisin que a signé le formulaire est parti.", ok: 'faux',
        rat: "Personne ne signe à la place du voisin&nbsp;: la place est libre, donc "
           + "<i>qui</i>. Et de toute façon, <i>que</i> ne reste jamais entier devant une "
           + "voyelle. «&nbsp;Le voisin qui a signé.&nbsp;»",
        pourquoi: "Il faut « le voisin qui a signé »." },
      { txt: "La lettre qu'elle m'a envoyée est arrivée lundi.", ok: 'ok',
        rat: "«&nbsp;Elle&nbsp;» occupe la place juste après&nbsp;: <i>que</i>, élidé en "
           + "<i>qu'</i> devant la voyelle. Rien à corriger.",
        pourquoi: "« elle » occupe la place. Élision normale. Juste." },
      { txt: "Les enfants qui je garde le mercredi ont six et huit ans.", ok: 'faux',
        rat: "«&nbsp;Je&nbsp;» est déjà là pour garder&nbsp;: c'est <i>que</i>. Ce qui trompe "
           + "ici, c'est qu'on parle de personnes — mais le sens ne décide rien. "
           + "«&nbsp;Les enfants que je garde.&nbsp;»",
        pourquoi: "Il faut « que je garde ». Le sens ne décide rien." },
      { txt: "Le chèque qui arrive à la fin du mois couvre le loyer.", ok: 'ok',
        rat: "Le verbe part tout de suite&nbsp;: la place est libre, donc <i>qui</i>. Un chèque "
           + "n'est pas une personne, et ça n'y change rien.",
        pourquoi: "La place est libre. Juste, même pour un objet." },
      { txt: "La technicienne qu'est venue hier a laissé sa carte.", ok: 'faux',
        rat: "Vous avez écrit ce que vous entendez&nbsp;: à l'oral, «&nbsp;qui est&nbsp;» sonne "
           + "comme «&nbsp;qu'est&nbsp;». Mais <i>qui</i> ne s'élide jamais. "
           + "«&nbsp;La technicienne qui est venue.&nbsp;»",
        pourquoi: "Il faut « qui est venue ». « qui » ne s'élide jamais." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas fréquent dans une vraie production. ────────────────────────
  {
    id:   'la-note',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une note à corriger',
    titre: "Une note à l'école. Une seule ligne est fautive.",
    consigne: "«&nbsp;<i>Bonjour, voici le formulaire que vous m'avez demandé. Le papier qui "
            + "manquait est joint. La personne qui j'ai vue au secrétariat m'a dit de vous "
            + "l'envoyer directement.</i>&nbsp;»",
    options: [
      { txt: "« La personne qui j'ai vue au secrétariat… »", juste: true },
      { txt: "« Le formulaire que vous m'avez demandé… »",
        rat_t: "Celle-là est juste.",
        rat: "«&nbsp;Vous&nbsp;» est déjà là pour demander&nbsp;: la place est prise, donc "
           + "<i>que</i>. Rien à corriger." },
      { txt: "« Le papier qui manquait est joint. »",
        rat_t: "Celle-là est juste aussi.",
        rat: "Le verbe part tout de suite après le mot&nbsp;: personne ne fait l'action à la "
           + "place du papier. C'est bien <i>qui</i>, même pour un objet." },
    ],
    pourquoi: "«&nbsp;La personne <b>que</b> j'ai vue&nbsp;». «&nbsp;J'&nbsp;» est déjà là pour "
            + "voir — c'est vous qui avez vu la personne, pas l'inverse. La faute vient de "
            + "l'idée que «&nbsp;qui&nbsp;» irait avec «&nbsp;personne&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La variante qui trompe : le sujet peut être un nom. ───────────────
  {
    id:   'un-nom-aussi',
    type: 'notion',
    eye:  'La variante',
    menu: 'Pas seulement un pronom',
    titre: "Celui qui occupe la place n'est pas toujours un petit mot.",
    paras: [
      "Jusqu'ici, la place était prise par <i>je</i>, <i>tu</i>, <i>elle</i>, <i>nous</i>, "
      + "<i>vous</i> — des mots courts, faciles à voir. Mais ce peut être un nom entier&nbsp;: "
      + "«&nbsp;le dossier <b>que la secrétaire</b> m'a demandé&nbsp;», «&nbsp;la clé <b>que mon "
      + "propriétaire</b> a fait refaire&nbsp;».",

      "Le test ne change pas&nbsp;: quelqu'un est-il déjà là pour faire l'action&nbsp;? Ici, "
      + "oui — la secrétaire demande, le propriétaire fait refaire. Le dossier et la clé, eux, "
      + "ne font rien.",

      "Un repère qui aide quand la phrase est longue&nbsp;: si vous pouvez remplacer le groupe "
      + "par «&nbsp;elle&nbsp;» ou «&nbsp;il&nbsp;» et que la phrase tient — «&nbsp;le dossier "
      + "qu'<b>elle</b> m'a demandé&nbsp;» — la place était bien prise.",
    ],
    retenir: "La place peut être prise par un <b>nom</b> autant que par un pronom. "
           + "«&nbsp;Le dossier <b>que la secrétaire</b> m'a demandé.&nbsp;»",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Choisir dans un message entier. ───────────────────────────────────
  {
    id:   'lannonce',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre annonce',
    titre: "Vous rédigez une petite annonce pour vendre un divan. Quelle version tient ?",
    consigne: "Trois versions de la même annonce. Une seule est correcte d'un bout à l'autre.",
    options: [
      { txt: "« Divan trois places qui vient d'un salon sans animaux. Le tissu que j'ai fait nettoyer est comme neuf. »",
        juste: true },
      { txt: "« Divan trois places que vient d'un salon sans animaux. Le tissu que j'ai fait nettoyer est comme neuf. »",
        rat_t: "La seconde phrase est bonne. C'est la première qui glisse.",
        rat: "«&nbsp;Que vient&nbsp;»&nbsp;: personne ne vient à la place du divan, la place est "
           + "libre — donc <i>qui</i>. Et notez qu'aucun mot ne peut rester entre "
           + "«&nbsp;que&nbsp;» et un verbe&nbsp;: c'est le signe le plus visible que vous vous "
           + "êtes trompé." },
      { txt: "« Divan trois places qui vient d'un salon sans animaux. Le tissu qui j'ai fait nettoyer est comme neuf. »",
        rat_t: "La première phrase est bonne, et vous avez recopié dessus.",
        rat: "«&nbsp;Qui vient&nbsp;»&nbsp;: parfait, la place était libre. Mais dans la seconde, "
           + "«&nbsp;j'&nbsp;» est déjà là pour faire nettoyer&nbsp;: la place est prise, donc "
           + "<i>que</i>. Deux phrases voisines n'appellent pas forcément le même mot." },
    ],
    pourquoi: "Une place libre, une place prise&nbsp;: <b>qui</b>, puis <b>que</b>. "
            + "<b>C'est tout le point en deux lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la phrase du début. Vous écrivez à votre propriétaire.",
    consigne: "Vous avez essayé de joindre le plombier plusieurs fois, sans succès. Quelle "
            + "phrase écrivez-vous&nbsp;?",
    options: [
      { txt: "« Le plombier que j'appelle depuis lundi ne répond jamais. »", juste: true },
      { txt: "« Le plombier qui j'appelle depuis lundi ne répond jamais. »",
        rat_t: "C'est la faute de l'écran 1, dans l'autre sens.",
        rat: "«&nbsp;J'&nbsp;» est déjà là pour appeler&nbsp;: la place est prise, donc "
           + "<i>que</i>. Et un signe visible&nbsp;: après «&nbsp;qui&nbsp;», il ne peut rien y "
           + "avoir d'autre qu'un verbe." },
      { txt: "« Le plombier qui appelle depuis lundi ne répond jamais. »",
        rat_t: "La phrase est correcte, mais elle dit le contraire de la vôtre.",
        rat: "Écrite comme ça, elle raconte que c'est <b>lui</b> qui téléphone depuis lundi — et "
           + "qu'il ne répond pas quand on le rappelle. Votre propriétaire comprendra que le "
           + "plombier vous cherche&nbsp;: c'est l'inverse de ce que vous voulez dire." },
    ],
    pourquoi: "«&nbsp;Le plombier <b>que j'appelle</b>&nbsp;». Vous avez regardé un mot plus "
            + "loin, vous avez vu que la place était prise, et vous avez tranché sans penser "
            + "au sens.",
    attente: "Choisissez une réponse pour finir.",
  },

];
