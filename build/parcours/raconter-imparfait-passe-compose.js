// ═══════════════════════════════════════════════════════════════════════════
// Point express — Raconter : ce qui durait, ce qui est arrivé
//
// Savoir n5-s32 avec n5-s31. Dix minutes, dix écrans.
//
// ── L'écart avec les mini-leçons, qui est ici maximal ──────────────────────
// SIX modules portent déjà une mini-leçon sur ce couple (n5-degat,
// n5-emmenagement, n5-quebec, n5-rendezvous, n5-services, n5-urgence), et
// toutes emploient la même image — « le décor et l'évènement ». Un élève
// envoyé ici l'a lue au moins une fois. Le point express ne la reprend donc
// PAS :
//
//   1. Il ne part pas d'une image, il part d'un RÉCIT QUI CHANGE DE SENS
//      selon le temps employé. La règle sort de la comparaison, pas d'une
//      métaphore à retenir.
//   2. Il n'oppose jamais les deux temps en colonnes « durée / ponctuel » :
//      c'est ce que font les mini-leçons, et c'est ce qui produit des élèves
//      qui savent réciter la règle et se trompent quand même.
//   3. Le test qu'il donne est une QUESTION À SE POSER — « est-ce que ça a
//      une fin ? » — applicable à un verbe qu'on n'a jamais vu.
//   4. Le métalangage (« imparfait », « passé composé ») n'arrive qu'à
//      l'écran 4, une fois les deux formes manipulées.
//
// Extraits : module-n5-rendezvous, défi 2 — le récit de Rachid à la médecin.
// C'est le seul endroit du cours où les deux temps se suivent dans une même
// phrase dite à voix haute. Aucun média neuf.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'raconter-imparfait-passe-compose',
  module:   'module-n5-rendezvous',
  titre:    "Raconter : ce qui durait, ce qui est arrivé",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s32 · n5-s31',
};

const ECRANS = [

  // ── 1. Deux phrases, deux histoires différentes. ─────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux histoires',
    titre: "Ces deux phrases ne racontent pas la même chose. Laquelle dit que le mal de tête est fini ?",
    consigne: "Aucune règle ne vous a été donnée. Lisez-les à voix basse et fiez-vous à ce que "
            + "vous comprenez.",
    options: [
      { txt: "J'avais mal à la tête.",
        rat_t: "Celle-là ne dit rien de la fin.",
        rat: "Elle vous met <b>dedans</b>&nbsp;: on est au milieu du mal de tête, on ne sait pas "
           + "s'il finit. C'est une phrase qui plante un décor, et on attend la suite&nbsp;— "
           + "«&nbsp;j'avais mal à la tête <i>quand…</i>&nbsp;»." },
      { txt: "J'ai eu mal à la tête.", juste: true },
      { txt: "Les deux disent la même chose.",
        rat_t: "Relisez-les l'une après l'autre.",
        rat: "Si c'était vrai, le français n'aurait pas gardé deux formes. Elles ne changent pas "
           + "la <i>vérité</i> — le mal de tête a bien existé — elles changent <b>ce que le "
           + "locuteur en fait</b>&nbsp;: il le raconte comme terminé, ou comme en cours." },
    ],
    pourquoi: "«&nbsp;J'ai eu mal&nbsp;» ferme l'épisode&nbsp;: c'est arrivé, c'est fini. "
            + "«&nbsp;J'avais mal&nbsp;» laisse la porte ouverte.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. Le vrai récit, entendu. ───────────────────────────────────────────
  {
    id:   'le-recit',
    type: 'notion',
    eye:  'Écoutez un vrai récit',
    menu: 'Rachid raconte',
    titre: "Rachid raconte trois mois à sa médecin. Les deux formes se suivent dans une seule phrase.",
    paras: [
      "Il ne récite pas une règle&nbsp;: il raconte. Écoutez, et repérez le moment où la phrase "
      + "<b>bascule</b>.",
      "«&nbsp;Ça <b>a commencé</b> au mois de mars&nbsp;»&nbsp;— un point sur le calendrier, "
      + "une date. «&nbsp;Je <b>me levais</b> le matin et tout <b>tournait</b>&nbsp;»&nbsp;— "
      + "pas un matin, <i>tous</i> les matins&nbsp;; pas une seconde, une habitude.",
    ],
    sons: [
      { fichier: 't2/line_02_rachid.mp3', qui: 'Rachid, dans le bureau',
        texte: "Ça a commencé au mois de mars. Je me levais le matin et tout tournait pendant "
             + "quelques secondes." },
    ],
    retenir: "Une même histoire emploie <b>les deux</b>. Ce n'est pas «&nbsp;choisir le bon "
           + "temps&nbsp;», c'est <b>alterner</b> — et savoir quand.",
    attente: "Écoutez l'extrait, puis continuez.",
  },

  // ── 3. Trier des phrases, toujours sans règle. ───────────────────────────
  {
    id:   'tri-fin',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Ça a une fin ?',
    titre: "Six phrases. Lesquelles racontent quelque chose qui a une fin ?",
    consigne: "Ne cherchez pas le temps du verbe. Demandez-vous seulement&nbsp;: "
            + "<b>est-ce que ça se termine, ou est-ce que ça dure&nbsp;?</b>",
    colonnes: [
      { id: 'fin',  t: 'Ça a une fin',  b: 'Ça a une fin' },
      { id: 'dure', t: 'Ça durait',     b: 'Ça durait' },
    ],
    items: [
      { txt: "Je suis tombé dans l'escalier.", ok: 'fin',
        rat: "Une chute prend une seconde et elle est finie. Impossible de tomber pendant trois "
           + "mois.",
        pourquoi: "Une seconde, et c'est fini." },
      { txt: "Je travaillais à l'entretien.", ok: 'dure',
        rat: "Un emploi, ce n'est pas un évènement&nbsp;: c'est ce qu'on faisait pendant des "
           + "années. C'est un décor, pas une action.",
        pourquoi: "Pendant des années. Un décor." },
      { txt: "La clinique a fermé à vingt et une heures.", ok: 'fin',
        rat: "La fermeture se produit à un instant précis, et l'heure est donnée. C'est un point "
           + "sur la ligne du temps.",
        pourquoi: "Un instant précis, avec l'heure." },
      { txt: "J'avais peur d'appeler.", ok: 'dure',
        rat: "La peur ne s'arrête pas au moment où on la nomme&nbsp;: elle était là avant, "
           + "pendant, après. Un état, jamais un évènement.",
        pourquoi: "Un état. Ça n'arrive pas, ça dure." },
      { txt: "Ma fille m'a dit d'y aller.", ok: 'fin',
        rat: "Elle l'a dit, une fois, et la phrase est finie. Si elle le répétait tous les "
           + "jours, on le raconterait autrement — «&nbsp;elle me disait&nbsp;».",
        pourquoi: "Une fois. Et c'est dit." },
      { txt: "Il faisait froid ce matin-là.", ok: 'dure',
        rat: "Le temps qu'il fait est le décor de l'histoire. Il ne se passe pas&nbsp;: il est "
           + "là pendant que le reste se passe.",
        pourquoi: "Le décor. Le froid ne « se produit » pas." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 4. La règle, tirée du tri. Le métalangage arrive ici. ────────────────
  {
    id:   'la-question',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'La question à se poser',
    titre: "Vous n'avez pas trié des verbes. Vous avez trié des histoires.",
    paras: [
      "Regardez votre colonne «&nbsp;ça a une fin&nbsp;»&nbsp;: tomber, fermer, dire. Regardez "
      + "l'autre&nbsp;: travailler, avoir peur, faire froid. <b>Ce n'est pas le verbe qui décide,"
      + " c'est ce que vous racontez avec.</b> Le même verbe change de colonne selon l'histoire.",

      "Les deux formes ont un nom&nbsp;: ce qui a une fin se dit au <b>passé composé</b> "
      + "(<i>j'ai eu, je suis tombé</i>), ce qui durait se dit à l'<b>imparfait</b> "
      + "(<i>j'avais, je travaillais</i>). Vous les employiez déjà avant de connaître les noms.",

      "<b>La question à se poser, sur n'importe quel verbe&nbsp;:</b> est-ce que ça se termine, "
      + "ou est-ce que c'était là&nbsp;? Si ça se termine, passé composé. Si c'était là, "
      + "imparfait.",
    ],
    retenir: "Ce n'est pas le verbe qui choisit le temps&nbsp;: <b>c'est vous</b>, selon ce que "
           + "vous voulez raconter.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le même verbe, deux colonnes. La preuve. ──────────────────────────
  {
    id:   'meme-verbe',
    type: 'verif',
    eye:  'La preuve',
    menu: 'Le même verbe',
    titre: "« Travailler » vient de passer dans la colonne « ça durait ». Où est-il ici ?",
    consigne: "«&nbsp;<i>J'ai travaillé toute la journée de samedi, et le soir j'étais "
            + "épuisé.</i>&nbsp;»",
    options: [
      { txt: "« J'ai travaillé » a une fin ; « j'étais épuisé » durait.", juste: true },
      { txt: "Les deux durent : ce sont deux longs moments.",
        rat_t: "La journée est longue, mais elle est <b>bornée</b>.",
        rat: "«&nbsp;Toute la journée de samedi&nbsp;» a un début et une fin — samedi est fini. "
           + "Une durée n'est pas la même chose qu'une chose qui dure&nbsp;: on peut raconter "
           + "douze heures comme un seul bloc terminé." },
      { txt: "La phrase est fautive : on ne mélange pas les deux.",
        rat_t: "C'est justement l'inverse.",
        rat: "Presque tout récit <b>alterne</b> les deux — c'est ce que fait Rachid à l'écran 2. "
           + "Une histoire écrite entièrement dans un seul temps est le vrai signe qu'on n'a pas "
           + "encore compris." },
    ],
    pourquoi: "Le même verbe, <i>travailler</i>, prend les deux formes selon l'histoire. "
            + "<b>Samedi est terminé&nbsp;; la fatigue, elle, était là.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Ce qui interrompt. ────────────────────────────────────────────────
  {
    id:   'interruption',
    type: 'notion',
    eye:  'Le cas le plus fréquent',
    menu: 'Quand ça coupe',
    titre: "Quelque chose durait. Quelque chose est arrivé et l'a coupé.",
    paras: [
      "C'est la charpente de presque tous les récits qu'on vous demandera d'écrire&nbsp;: "
      + "un accident, un retard, une panne, une chicane. <b>Le fond dure, l'évènement le "
      + "coupe.</b>",
      "«&nbsp;J'<b>attendais</b> l'autobus <i>quand</i> mon téléphone <b>a sonné</b>.&nbsp;» "
      + "«&nbsp;Elle <b>dormait</b> <i>quand</i> l'alarme <b>s'est déclenchée</b>.&nbsp;» "
      + "Le mot <i>quand</i> est presque toujours là, et il marque l'endroit exact où le temps "
      + "change.",
      "Écoutez la médecin&nbsp;: elle demande précisément <b>à quel moment</b> ça coupe.",
    ],
    sons: [
      { fichier: 't2/line_03_dre_fongang.mp3', qui: 'La docteure Fongang',
        texte: "Quelques secondes. Et ça arrive à quel moment, exactement&nbsp;?" },
    ],
    retenir: "<b>Ce qui dure à l'imparfait, ce qui coupe au passé composé.</b> "
           + "Cherchez le mot «&nbsp;quand&nbsp;»&nbsp;: la bascule est juste après.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 7. Trier des récits complets. ────────────────────────────────────────
  {
    id:   'tri-recits',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Cinq récits',
    titre: "Dans chaque phrase, une moitié est fautive. Laquelle ?",
    consigne: "Le fond doit durer, l'évènement doit couper. Trouvez celle qui s'est trompée "
            + "de rôle.",
    colonnes: [
      { id: 'a', t: 'La première moitié', b: 'La 1re moitié' },
      { id: 'b', t: 'La seconde moitié',  b: 'La 2e moitié' },
      { id: 'ok', t: 'Aucune : c\'est juste', b: 'Aucune' },
    ],
    items: [
      { txt: "Je dormais quand le téléphone a sonné.", ok: 'ok',
        rat: "Regardez les rôles&nbsp;: le sommeil dure, la sonnerie coupe. C'est exactement la "
           + "charpente de l'écran précédent.",
        pourquoi: "Le fond dure, l'évènement coupe. Juste." },
      { txt: "J'ai attendu l'autobus quand il a commencé à pleuvoir.", ok: 'a',
        rat: "«&nbsp;J'ai attendu&nbsp;» ferme l'attente — mais elle est le <b>fond</b> de "
           + "l'histoire&nbsp;: elle devrait durer. Il faut «&nbsp;j'attendais&nbsp;».",
        pourquoi: "Le fond a été fermé : « j'attendais »." },
      { txt: "Il faisait noir quand je sortais de la clinique.", ok: 'b',
        rat: "La sortie est un évènement, pas un décor&nbsp;: elle coupe la nuit qui, elle, "
           + "durait. Il faut «&nbsp;quand je suis sorti&nbsp;».",
        pourquoi: "L'évènement a été mis en décor : « je suis sorti »." },
      { txt: "Nous étions en retard, alors nous avons pris un taxi.", ok: 'ok',
        rat: "Le retard est un état qui durait, le taxi est une décision prise une fois. "
           + "Les deux rôles sont à leur place.",
        pourquoi: "Un état, puis une décision. Juste." },
      { txt: "Elle a été malade toute la semaine, alors elle appelait la clinique.", ok: 'b',
        rat: "L'appel est un geste unique, qui met fin à quelque chose&nbsp;: "
           + "«&nbsp;elle a appelé&nbsp;». À l'imparfait, on comprendrait qu'elle appelait tous "
           + "les jours, sans jamais aboutir.",
        pourquoi: "Un geste unique : « elle a appelé »." },
    ],
    attente: "Tranchez les cinq récits pour continuer.",
  },

  // ── 8. Le piège de « depuis ». ───────────────────────────────────────────
  {
    id:   'depuis',
    type: 'verif',
    eye:  'Le piège',
    menu: '« Depuis trois mois »',
    titre: "« Depuis trois mois » : quel temps ?",
    consigne: "C'est la phrase que Rachid doit dire à l'agente, et celle que la moitié des "
            + "élèves écrit au passé composé.",
    options: [
      { txt: "« J'ai des étourdissements depuis trois mois. » — au présent.", juste: true },
      { txt: "« J'ai eu des étourdissements depuis trois mois. »",
        rat_t: "Le passé composé ferme&nbsp;; «&nbsp;depuis&nbsp;» dit que ce n'est pas fini.",
        rat: "Les deux se contredisent dans la même phrase. Si c'était terminé, on dirait "
           + "«&nbsp;j'ai eu des étourdissements <b>pendant</b> trois mois&nbsp;» — et l'agente "
           + "n'aurait aucune raison de vous donner un rendez-vous." },
      { txt: "« J'avais des étourdissements depuis trois mois. »",
        rat_t: "Juste, mais seulement dans un récit au passé.",
        rat: "Cette phrase se dit&nbsp;: «&nbsp;j'avais des étourdissements depuis trois mois "
           + "<i>quand j'ai enfin appelé</i>&nbsp;». Elle raconte le passé. Au téléphone, "
           + "aujourd'hui, le problème est encore là&nbsp;: c'est le présent." },
    ],
    pourquoi: "<b>«&nbsp;Depuis&nbsp;» dit que ça continue</b>&nbsp;: le français emploie alors "
            + "le présent, là où beaucoup de langues emploient un passé. C'est la faute la plus "
            + "coûteuse de l'appel — elle fait croire que le problème est réglé.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'ecrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Trois phrases',
    titre: "Vous écrivez à l'école pour expliquer une absence. Quelle version tient debout ?",
    consigne: "Trois versions du même matin. Une seule raconte correctement.",
    options: [
      { txt: "« Ma fille était malade hier. Elle a vomi deux fois, alors je suis restée avec elle. »",
        juste: true },
      { txt: "« Ma fille a été malade hier. Elle vomissait deux fois, alors je restais avec elle. »",
        rat_t: "Tout est inversé.",
        rat: "L'état — être malade — a été fermé, et les deux évènements ont été mis en décor. "
           + "«&nbsp;Elle vomissait deux fois&nbsp;» laisse entendre que ça revenait chaque "
           + "jour&nbsp;; «&nbsp;je restais&nbsp;», que c'était une habitude." },
      { txt: "« Ma fille était malade hier. Elle vomissait deux fois, alors je suis restée avec elle. »",
        rat_t: "La moitié y est.",
        rat: "Le décor est bon et la décision aussi. Mais «&nbsp;deux fois&nbsp;» compte les "
           + "évènements&nbsp;: on ne peut pas compter ce qui dure. Il faut «&nbsp;elle a vomi "
           + "deux fois&nbsp;»." },
    ],
    pourquoi: "L'état durait, les deux vomissements sont des évènements comptés, la décision de "
            + "rester est un geste unique. <b>Un chiffre devant un verbe est presque toujours le "
            + "signe du passé composé.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. Fermeture : retour à l'écran 1. ──────────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début. Vous voulez dire que le mal de tête revient encore aujourd'hui.",
    consigne: "Vous êtes au téléphone avec la clinique. Vous dites quoi&nbsp;?",
    options: [
      { txt: "« J'ai mal à la tête depuis deux semaines. »", juste: true },
      { txt: "« J'avais mal à la tête depuis deux semaines. »",
        rat_t: "Vous venez de mettre votre problème au passé.",
        rat: "L'agente entendra que c'est fini, et vous donnera un rendez-vous dans cinq "
           + "semaines. <b>«&nbsp;Depuis&nbsp;» + présent</b>&nbsp;: c'est encore là." },
      { txt: "« J'ai eu mal à la tête pendant deux semaines. »",
        rat_t: "Juste — mais ça dit que c'est terminé.",
        rat: "La phrase est correcte, et c'est ce qui la rend dangereuse&nbsp;: rien ne vous "
           + "signalera l'erreur. Elle raconte un épisode clos. Si le mal est encore là, "
           + "il faut «&nbsp;depuis&nbsp;» et le présent." },
    ],
    pourquoi: "<b>Ce qui est fini se ferme, ce qui dure reste ouvert.</b> Vous avez fait les "
            + "deux&nbsp;: trier les histoires, et choisir celle que vous racontez.",
    attente: "Choisissez une réponse pour finir.",
  },

];
