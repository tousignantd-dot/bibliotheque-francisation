// ═══════════════════════════════════════════════════════════════════════════
// Point express — Placer en tête ce sur quoi vous ne céderez pas
//
// Savoir n8-s07 (Phrases emphatiques), avec n8-s14 (relative avec « qui »,
// accord du verbe avec le pronom de la 1re personne). Une ORDONNANCE :
// l'enseignant l'envoie à un élève dont les courriels de réclamation, les
// interventions en réunion ou les résumés d'opinion posent tout à plat, si
// bien qu'on ne sait pas ce qu'il conteste. Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Le dépôt en porte sept qui touchent au sujet :
//   · « La mise en relief : faire ressortir un mot »
//   · « Mettre en relief : c'est… qui, c'est… que »
//   · « Mettre en relief : c'est… qui, ce que… c'est »
//   · « Mettre en avant : "c'est… qui", "ce que…, c'est" »
//   · « Mettre en relief ce qui compte »
//   · « Mettre en relief : choisir ce que le lecteur retiendra »
//   · « La phrase emphatique : mettre un mot en avant »
// Toutes présentent le PROCÉDÉ : voici deux moules, voici comment les remplir.
// Un élève qui les a lues sait fabriquer « c'est… qui » sur commande — et il
// continue d'écrire des courriels où l'on ne voit pas ce qui est contesté.
//
// Les cinq écarts tenus :
//
//   1. LE SUJET N'EST PAS LE MOULE, C'EST LE CHOIX. Ce point ne demande jamais
//      « transformez cette phrase » ; il demande, phrase après phrase,
//      QUEL MOT il fallait encadrer, la même phrase pouvant se mettre en
//      relief de quatre façons selon ce qu'on conteste.
//   2. INDUCTIF. L'élève range six phrases selon ce qu'elles mettent en avant
//      AVANT qu'aucun moule ne soit nommé. L'écran 3 constate.
//   3. UN TEST, JAMAIS LA LISTE DES MOULES. Une question unique — « à quelle
//      objection est-ce que je réponds ? » — plus un second test, mécanique,
//      pour choisir entre qui et que : le mot encadré fait-il l'action ?
//   4. L'ACCORD EST TRAITÉ COMME UN PIÈGE (écrans 4 et 6), pas comme un
//      chapitre : « c'est moi qui ai », « c'est nous qui devons », là où la
//      logique de l'élève dit « a » et « doit ».
//   5. LA DISLOCATION ORALE EST DITE EN DERNIER (écran 8), alors que c'est la
//      forme que l'élève entend le plus. La nommer d'entrée ferait croire
//      qu'elle s'écrit.
//
// Aucun média : la mise en relief s'entend à l'oral par la voix seule, et le
// sujet du point est justement ce qu'on en fait quand la voix manque — à
// l'écrit.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'c-est-lui-qui',
  titre:    "Placer en tête ce sur quoi vous ne céderez pas",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s07',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Une signature',
    titre: "On vous reproche d'avoir signé un bon de commande. Ce n'est pas vous.",
    consigne: "Vous répondez par courriel à votre gestionnaire. Vous voulez qu'une seule chose "
            + "reste en tête après la lecture&nbsp;: la signature est celle du superviseur. "
            + "Répondez avec ce que vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "C'est le superviseur qui a signé le bon de commande.", juste: true },
      { txt: "Le superviseur a signé le bon de commande.",
        rat_t: "Elle est correcte, et c'est ce qui la rend insuffisante.",
        rat: "Rien n'y est faux&nbsp;: elle dit exactement ce qui s'est passé. Mais elle le dit "
           + "<b>à plat</b>, comme une information neuve, alors que vous répondez à une "
           + "accusation. Le lecteur ne voit pas que vous corrigez quelque chose." },
      { txt: "Le bon de commande a été signé par le superviseur.",
        rat_t: "Elle éloigne la personne au lieu de la mettre en avant.",
        rat: "Cette tournure met le <b>document</b> en tête et repousse celui qui a agi tout au "
           + "bout de la phrase. C'est utile quand on ne veut désigner personne&nbsp;; ici, vous "
           + "voulez précisément désigner quelqu'un." },
    ],
    pourquoi: "Gardez cette phrase en tête&nbsp;: on y revient au dernier écran, avec une autre "
            + "accusation.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-objection',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites en réponse à quelqu'un. Qu'est-ce que chacune conteste ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Lisez chaque phrase et "
            + "demandez-vous&nbsp;: <b>l'auteur corrige-t-il la personne, la chose, ou le "
            + "moment&nbsp;?</b>",
    colonnes: [
      { id: 'qui',   t: "La personne", b: "La personne" },
      { id: 'quoi',  t: "La chose",    b: "La chose" },
      { id: 'quand', t: "Le moment",   b: "Le moment" },
    ],
    items: [
      { txt: "C'est la comptable qui a annulé le paiement.",
        sous: "réponse à un fournisseur en colère", ok: 'qui',
        rat: "Le paiement, l'annulation, tout le monde est d'accord là-dessus. Ce qui est corrigé "
           + "est <b>l'auteur du geste</b>&nbsp;: ce n'est pas celui qu'on accusait.",
        pourquoi: "L'auteur du geste, et rien d'autre." },
      { txt: "C'est le deuxième versement que je conteste, pas le premier.",
        sous: "courriel à un service de recouvrement", ok: 'quoi',
        rat: "Personne ne discute de qui conteste&nbsp;: c'est vous, et vous le dites en passant. "
           + "Ce qui est corrigé, c'est <b>de quel versement on parle</b>.",
        pourquoi: "Lequel des deux : la chose visée." },
      { txt: "C'est en mars que j'ai envoyé le formulaire, pas en mai.",
        sous: "réclamation à un assureur", ok: 'quand',
        rat: "L'envoi n'est pas contesté, ni par qui il a été fait. C'est la <b>date</b> qui "
           + "change tout — un délai s'y joue.",
        pourquoi: "La date, parce qu'un délai en dépend." },
      { txt: "Ce que je demande, c'est un délai, pas une annulation.",
        sous: "message à une conseillère",  ok: 'quoi',
        rat: "On a mal compris votre demande, pas qui la faisait. Vous remettez donc "
           + "<b>l'objet de la demande</b> à la place où on ne peut pas le manquer.",
        pourquoi: "L'objet de la demande." },
      { txt: "C'est nous qui devons produire le rapport, pas le siège social.",
        sous: "intervention en réunion", ok: 'qui',
        rat: "Le rapport est attendu, tout le monde le sait. La question est <b>qui s'en "
           + "charge</b>, et la phrase répond en désignant.",
        pourquoi: "Qui s'en charge." },
      { txt: "C'est à la fin du contrat que la garantie s'applique.",
        sous: "note à un client", ok: 'quand',
        rat: "La garantie existe, tout le monde en convient. Ce qui est corrigé est "
           + "<b>le moment où elle joue</b> — et c'est là-dessus que reposait le malentendu.",
        pourquoi: "Le moment où elle joue." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Six phrases, le même moule, trois travaux différents.",
    paras: [
      "Vous n'avez rangé aucune phrase d'après sa forme&nbsp;: elles se ressemblent toutes. Vous "
      + "les avez rangées d'après <b>ce que l'auteur voulait corriger</b>. Et le mot corrigé est "
      + "à chaque fois celui qui est pris entre <b>c'est</b> et <b>qui</b> ou <b>que</b>.",

      "<b>Le test, avant d'écrire une phrase de ce genre&nbsp;:</b> demandez-vous <i>à quelle "
      + "objection est-ce que je réponds&nbsp;?</i> — puis encadrez le mot qui y répond. La même "
      + "situation donne quatre phrases différentes selon l'objection&nbsp;: «&nbsp;<i>c'est le "
      + "superviseur qui a signé</i>&nbsp;», «&nbsp;<i>c'est le bon de commande qu'il a "
      + "signé</i>&nbsp;», «&nbsp;<i>c'est vendredi qu'il l'a signé</i>&nbsp;», "
      + "«&nbsp;<i>c'est sous la pression qu'il l'a signé</i>&nbsp;».",

      "Ce procédé s'appelle la <b>mise en relief</b>, et la phrase qui en résulte, une phrase "
      + "<b>emphatique</b>. Vous n'aviez pas besoin de ces noms pour trancher les six cas, mais "
      + "votre enseignant les emploiera.",
    ],
    retenir: "Une seule question avant d'écrire&nbsp;: <b>à quelle objection est-ce que je "
           + "réponds&nbsp;?</b> Le mot qui y répond va entre «&nbsp;c'est&nbsp;» et "
           + "«&nbsp;qui&nbsp;» ou «&nbsp;que&nbsp;».",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : le verbe suit la personne, pas « c'est ». ──────
  {
    id:   'accord-du-verbe',
    type: 'verif',
    eye:  'Le piège du verbe',
    menu: 'Le verbe',
    titre: "Vous vous désignez vous-même. Que devient le verbe ?",
    consigne: "Vous écrivez à un service de facturation pour dire que la demande de "
            + "remboursement vient de vous, et non de votre conjoint. Quelle phrase "
            + "écrivez-vous&nbsp;?",
    options: [
      { txt: "C'est moi qui ai fait la demande.", juste: true },
      { txt: "C'est moi qui a fait la demande.",
        rat_t: "Vous avez suivi «&nbsp;c'est&nbsp;», qui est au singulier de la 3e personne.",
        rat: "C'est logique, et c'est faux. Le verbe qui suit «&nbsp;qui&nbsp;» ne se règle pas "
           + "sur «&nbsp;c'est&nbsp;»&nbsp;: il se règle sur <b>le mot encadré</b>. Le mot "
           + "encadré est «&nbsp;moi&nbsp;», donc <i>j'ai fait</i> → «&nbsp;qui <b>ai</b> "
           + "fait&nbsp;». De même&nbsp;: «&nbsp;c'est nous qui <b>devons</b>&nbsp;», jamais "
           + "«&nbsp;qui doit&nbsp;»." },
      { txt: "C'est moi que j'ai fait la demande.",
        rat_t: "Le verbe est bon. C'est le mot de liaison qui ne l'est pas.",
        rat: "Vous avez senti qu'il fallait la 1re personne, et vous avez raison. Mais en "
           + "écrivant «&nbsp;que&nbsp;», vous devez ajouter un sujet — d'où ce "
           + "«&nbsp;j'&nbsp;» en trop. Avec «&nbsp;qui&nbsp;», le mot encadré <b>est</b> le "
           + "sujet&nbsp;: il n'y a rien à ajouter." },
    ],
    pourquoi: "Le verbe suit toujours le mot encadré&nbsp;: «&nbsp;c'est moi qui <b>ai</b>&nbsp;», "
            + "«&nbsp;c'est nous qui <b>devons</b>&nbsp;», «&nbsp;c'est vous qui "
            + "<b>avez</b>&nbsp;». L'écran suivant montre quand employer «&nbsp;que&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le second test, mécanique celui-là : qui ou que. ──────────────────
  {
    id:   'qui-ou-que',
    type: 'notion',
    eye:  'Le deuxième test',
    menu: 'Qui ou que',
    titre: "Une seule question sépare « qui » de « que ».",
    paras: [
      "<b>Le mot encadré fait-il l'action&nbsp;?</b> S'il la fait, c'est <b>qui</b>&nbsp;: "
      + "«&nbsp;<i>c'est la comptable <b>qui</b> a annulé le paiement</i>&nbsp;» — la comptable "
      + "annule. S'il la subit, ou s'il n'est ni l'auteur ni l'action, c'est <b>que</b>&nbsp;: "
      + "«&nbsp;<i>c'est le paiement <b>qu'</b>elle a annulé</i>&nbsp;» — le paiement ne fait "
      + "rien, il est annulé.",

      "Le repère qui ne trompe pas&nbsp;: après <b>que</b>, il y a toujours un sujet — "
      + "«&nbsp;qu'<b>elle</b> a annulé&nbsp;», «&nbsp;qu'<b>on</b> m'a remis&nbsp;», "
      + "«&nbsp;que <b>je</b> conteste&nbsp;». Après <b>qui</b>, il n'y en a pas, parce que le "
      + "mot encadré occupe déjà la place.",

      "Pour mettre en avant un moment, un lieu ou une manière, c'est <b>que</b> aussi&nbsp;: "
      + "«&nbsp;<i>c'est en mars que j'ai envoyé le formulaire</i>&nbsp;», «&nbsp;<i>c'est à la "
      + "succursale de Laval que le dossier a été ouvert</i>&nbsp;». Ces mots-là ne font jamais "
      + "l'action.",
    ],
    retenir: "Le mot encadré fait l'action → <b>qui</b>, sans sujet derrière. Sinon → "
           + "<b>que</b>, avec un sujet derrière.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites : correct ou faute. ─────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases tirées de courriels. Lesquelles sont correctes ?",
    consigne: "Deux choses à regarder, dans cet ordre&nbsp;: le mot de liaison "
            + "(«&nbsp;qui&nbsp;» ou «&nbsp;que&nbsp;»), puis le verbe qui vient après.",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "C'est vous qui avez demandé le report, pas nous.", ok: 'ok',
        rat: "Le mot encadré fait l'action, donc «&nbsp;qui&nbsp;» sans sujet derrière&nbsp;; et "
           + "le verbe suit «&nbsp;vous&nbsp;»&nbsp;: <i>avez</i>. Les deux moitiés sont justes.",
        pourquoi: "« Qui » sans sujet, verbe accordé sur « vous »." },
      { txt: "C'est nous qui doit répondre à la mise en demeure.", ok: 'faux',
        rat: "«&nbsp;Qui&nbsp;» est bon&nbsp;: c'est nous qui répondons. Mais le verbe s'est "
           + "réglé sur «&nbsp;c'est&nbsp;» au lieu du mot encadré — «&nbsp;c'est nous qui "
           + "<b>devons</b>&nbsp;».",
        pourquoi: "Il faut « qui devons » : le verbe suit « nous »." },
      { txt: "C'est ce montant que je conteste, pas la totalité de la facture.", ok: 'ok',
        rat: "Le montant ne fait rien&nbsp;: il est contesté. Donc «&nbsp;que&nbsp;», avec le "
           + "sujet «&nbsp;je&nbsp;» derrière, exactement comme attendu.",
        pourquoi: "« Que » + un sujet : la construction est complète." },
      { txt: "C'est le technicien que est venu mardi.", ok: 'faux',
        rat: "Le technicien <b>vient</b>&nbsp;: il fait l'action, donc «&nbsp;qui&nbsp;». Le "
           + "signe visible est qu'il n'y a aucun sujet après «&nbsp;que&nbsp;», et il en faut "
           + "toujours un.",
        pourquoi: "Il faut « qui est venu » : le technicien agit." },
      { txt: "C'est en septembre que la nouvelle politique entre en vigueur.", ok: 'ok',
        rat: "Un moment ne fait jamais l'action&nbsp;: c'est «&nbsp;que&nbsp;», et la phrase qui "
           + "suit garde son sujet à elle, «&nbsp;la nouvelle politique&nbsp;».",
        pourquoi: "Un moment mis en avant prend toujours « que »." },
      { txt: "C'est moi qui a rempli le formulaire d'inscription.", ok: 'faux',
        rat: "Le piège de l'écran 4, dans un vrai courriel. «&nbsp;Moi&nbsp;» remplit, donc le "
           + "verbe est à la 1re personne&nbsp;: «&nbsp;c'est moi qui <b>ai</b> rempli&nbsp;».",
        pourquoi: "Il faut « qui ai rempli »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. L'autre moule, et ce qu'il permet de plus. ────────────────────────
  {
    id:   'ce-que-je-veux',
    type: 'verif',
    eye:  'Vérification',
    menu: "Ce que je veux",
    titre: "Vous voulez mettre en avant votre demande, pas un mot de la demande.",
    consigne: "Après trois échanges, un service à la clientèle vous propose un rabais. Vous ne "
            + "voulez pas de rabais&nbsp;: vous voulez que l'appareil soit réparé. Quelle phrase "
            + "ouvre votre message&nbsp;?",
    options: [
      { txt: "Ce que je demande depuis le début, c'est la réparation de l'appareil.",
        juste: true },
      { txt: "C'est la réparation de l'appareil que je demande depuis le début.",
        rat_t: "Elle n'est pas fautive&nbsp;: c'est une question de place.",
        rat: "Elle dit la même chose, et personne ne vous corrigerait. Mais elle livre la "
           + "réponse dès le troisième mot, avant d'avoir rappelé qu'il y a une demande en cours. "
           + "«&nbsp;Ce que je demande depuis le début&nbsp;» fait <b>attendre</b> le lecteur "
           + "une seconde — et c'est cette seconde qui donne du poids à ce qui suit." },
      { txt: "Je demande la réparation de l'appareil depuis le début.",
        rat_t: "Elle est plate là où il fallait insister.",
        rat: "Vous en êtes au quatrième message&nbsp;: dire les choses à plat, c'est répéter ce "
           + "qui n'a pas été entendu trois fois. La mise en relief ne sert à rien dans un "
           + "premier courriel&nbsp;; elle sert exactement ici." },
    ],
    pourquoi: "<b>«&nbsp;Ce que…, c'est…&nbsp;»</b> ouvre une porte que «&nbsp;c'est… que&nbsp;» "
            + "n'ouvre pas&nbsp;: elle met en avant <b>toute une demande</b>, pas un mot. Ses "
            + "sœurs&nbsp;: «&nbsp;ce qui me dérange, c'est…&nbsp;», «&nbsp;ce dont j'ai besoin, "
            + "c'est…&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La forme la plus fréquente, dite en dernier : l'oral. ─────────────
  {
    id:   'a-loral',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "À l'oral",
    titre: "À l'oral, on fait la même chose sans « c'est » — et ça ne s'écrit pas.",
    paras: [
      "On l'a gardée pour la fin bien que ce soit la forme que vous entendez le plus. En réunion, "
      + "au téléphone, entre collègues, on met un mot en avant en le <b>détachant</b>&nbsp;: "
      + "«&nbsp;<i>Le rapport, je l'ai envoyé hier.</i>&nbsp;» «&nbsp;<i>Je le trouve trop "
      + "court, moi.</i>&nbsp;» «&nbsp;<i>Ça, je vais leur en parler.</i>&nbsp;»",

      "Le mot sort de sa place et un petit pronom reste derrière lui pour la tenir — <i>l'</i>, "
      + "<i>en</i>, <i>y</i>, <i>lui</i>. C'est correct, c'est courant, et à l'oral personne ne "
      + "vous reprendra&nbsp;: la voix fait le reste du travail.",

      "<b>Dans un courriel professionnel ou une lettre, on revient à «&nbsp;c'est… qui&nbsp;».</b> "
      + "Non pas parce que l'autre forme serait fautive, mais parce qu'elle a besoin d'une voix "
      + "pour être lue comme une insistance&nbsp;; sans voix, elle se lit comme une phrase mal "
      + "construite. C'est la seule chose à retenir de cet écran.",
    ],
    retenir: "Détacher le mot marche <b>à l'oral</b>&nbsp;; à l'écrit, on encadre avec "
           + "«&nbsp;c'est&nbsp;». Même intention, deux outils, et le choix se fait sur le "
           + "support.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Choisir une version entière, dans une situation à enjeu. ──────────
  {
    id:   'la-reunion',
    type: 'verif',
    eye:  'Vérification',
    menu: 'La note de réunion',
    titre: "Après la réunion, vous écrivez pour corriger un point du compte rendu.",
    consigne: "Le compte rendu attribue à votre équipe la décision de reporter le projet. En "
            + "réalité, la décision vient du comité de direction&nbsp;; votre équipe n'a fait "
            + "que l'appliquer. Quelle version envoyez-vous&nbsp;?",
    options: [
      { txt: "Une précision sur le point 4&nbsp;: c'est le comité de direction qui a décidé du "
           + "report. Ce que notre équipe a fait, c'est appliquer cette décision.",
        juste: true },
      { txt: "Une précision sur le point 4&nbsp;: c'est le comité de direction qui a décidé du "
           + "report. C'est cette décision que notre équipe a appliquée.",
        rat_t: "Les deux phrases sont justes — mais elles insistent deux fois sur la même chose.",
        rat: "«&nbsp;C'est cette décision que…&nbsp;» met en avant <b>la décision</b>, qui vient "
           + "d'être mise en avant par la phrase précédente. La deuxième phrase doit déplacer "
           + "l'attention sur <b>ce qu'a fait votre équipe</b>&nbsp;: c'est le travail de "
           + "«&nbsp;ce que notre équipe a fait, c'est…&nbsp;»." },
      { txt: "Une précision sur le point 4&nbsp;: c'est le comité de direction qui a décidé du "
           + "report, et c'est notre équipe qui a appliqué cette décision.",
        rat_t: "Deux mises en relief à la file s'annulent.",
        rat: "Chacune des deux moitiés est correcte. Mais on ne peut pas contester deux choses "
           + "en même temps&nbsp;: le lecteur ne sait plus laquelle des deux vous corrigez. "
           + "<b>Une mise en relief par message</b>, sinon plus rien ne ressort." },
    ],
    pourquoi: "Vous avez répondu à l'objection — <i>qui a décidé&nbsp;?</i> — puis vous avez "
            + "déplacé l'attention avec l'autre moule. <b>Deux outils, deux travaux "
            + "différents.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la situation de l'écran 1, autre objection. ───────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au bon de commande. Cette fois, l'accusation a changé.",
    consigne: "Votre gestionnaire ne conteste plus la signature&nbsp;: il vous reproche d'avoir "
            + "signé <b>le bon de commande de 12&nbsp;000&nbsp;$</b>, alors que vous avez signé "
            + "celui de 1&nbsp;200&nbsp;$. Que répondez-vous&nbsp;?",
    options: [
      { txt: "C'est le bon de 1&nbsp;200&nbsp;$ que j'ai signé, pas celui de 12&nbsp;000&nbsp;$.",
        juste: true },
      { txt: "C'est moi qui ai signé le bon de 1&nbsp;200&nbsp;$, pas celui de 12&nbsp;000&nbsp;$.",
        rat_t: "C'était la bonne forme à l'écran 1 — l'objection n'est plus la même.",
        rat: "Vous répondez à «&nbsp;qui a signé&nbsp;?&nbsp;», une question que personne ne pose "
           + "plus&nbsp;: cette fois, on sait que c'est vous. En vous mettant vous-même en avant, "
           + "vous confirmez l'accusation au lieu de la corriger. C'est <b>le document</b> qui "
           + "doit être encadré." },
      { txt: "C'est le bon de 1&nbsp;200&nbsp;$ qui j'ai signé, pas celui de 12&nbsp;000&nbsp;$.",
        rat_t: "Le mot encadré est le bon. C'est le mot de liaison qui a glissé.",
        rat: "Le bon de commande ne signe rien&nbsp;: il <b>est</b> signé, et c'est vous qui "
           + "agissez. Le repère de l'écran 5 le dit tout seul&nbsp;: il y a un sujet juste "
           + "après («&nbsp;j'&nbsp;»), donc c'est <b>que</b>." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: identifier l'objection avant d'écrire, "
            + "encadrer le mot qui y répond, et choisir «&nbsp;que&nbsp;» parce que ce mot ne "
            + "fait pas l'action. <b>La même situation, une autre accusation, une autre "
            + "phrase.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
