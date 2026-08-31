// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Je le vois » ou « je lui parle » ?
//
// Savoir n3-s22 (pronoms personnels conjoints CD et CI). Dix minutes,
// dix écrans. Une ORDONNANCE : l'enseignant l'envoie à un élève dont la
// production montre « je lui vois », « je le téléphone ».
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Trois mini-leçons traitent déjà les pronoms compléments :
// `module-n5-emmenagement` (« Les pronoms qui évitent de tout répéter »),
// `module-n6-classe` (« Ce que remplacent le, en et y ») et
// `module-n6-actualite` (« Le, en, y »). Toutes les trois donnent la série
// complète — le, la, les, lui, leur, y, en — en cinq ou six blocs d'analyse.
// Les cinq écarts tenus :
//
//   1. UN SEUL PRONOM, ET DEUX FAMILLES. Ni « y », ni « en », ni les verbes
//      pronominaux, ni la place à l'impératif. Le point express traite le
//      choix d'UN pronom entre deux familles, et rien d'autre. Le point
//      `deux-pronoms` (n5-s24) traite l'enfilade de deux ; celui-ci reste
//      volontairement en deçà, et ne montre jamais deux pronoms d'affilée.
//   2. INDUCTIF. L'élève range huit phrases AVANT qu'aucune règle ne soit
//      donnée, à l'oreille. La règle de l'écran 3 est écrite comme un constat
//      de ce qu'il vient de faire.
//   3. UN TEST, PAS UNE TABLE. Les mini-leçons donnent la table des pronoms.
//      Ici : une question qu'on pose AU VERBE — « je vois qui ? », « je parle
//      à qui ? » — qui marche sur un verbe qu'on n'a jamais vu. Une table
//      s'oublie ; une question se repose.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Complément direct » et « indirect » ne
//      sont écrits qu'à l'écran 3, une fois le tri fait. Les mini-leçons
//      ouvrent dessus.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS, JAMAIS À UN MODULE. Une note à
//      l'école, un message à un employeur, un texto, un comptoir. L'élève doit
//      reconnaître la faute partout, pas dans un scénario.
//
// Aucun média : la faute s'entend autant qu'elle s'écrit, et tout se corrige
// par comparaison de chaînes. Rien à faire juger par un modèle.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'le-lui-un-seul-pronom',
  titre:    "« Je le vois » ou « je lui parle » ?",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s22',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Deux phrases',
    titre: "Vous téléphonez à votre voisin ce soir. Une seule de ces phrases est juste.",
    consigne: "Répondez avec ce que vous savez déjà — ou à l'oreille. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Je le téléphone ce soir.",
        rat_t: "Le verbe refuse ce pronom-là.",
        rat: "C'est la faute la plus fréquente, et elle a une bonne raison&nbsp;: dans beaucoup "
           + "de langues, on téléphone <i>quelqu'un</i>. En français, on téléphone <b>à</b> "
           + "quelqu'un — et ce petit mot change le pronom. Regardez l'autre phrase." },
      { txt: "Je lui téléphone ce soir.", juste: true },
      { txt: "Les deux se disent.",
        rat_t: "Une seule est juste, et l'écart s'entend.",
        rat: "À l'oral, on vous comprendra dans les deux cas — c'est bien le problème&nbsp;: "
           + "personne ne vous reprend. Mais la première phrase signale tout de suite que le "
           + "français n'est pas votre première langue." },
    ],
    pourquoi: "«&nbsp;Je <b>lui</b> téléphone.&nbsp;» Retenez la phrase entière pour l'instant&nbsp;; "
            + "on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-verbes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases à finir. Laquelle des deux formes sonne juste ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Dites la phrase dans votre tête, "
            + "les deux fois, et gardez celle qui passe.",
    colonnes: [
      { id: 'le',  t: 'Je le, la, les…', b: 'le · la · les' },
      { id: 'lui', t: 'Je lui, leur…',   b: 'lui · leur' },
    ],
    items: [
      { txt: "Mon frère arrive vendredi.", sous: "Je ___ vois vendredi.", ok: 'le',
        rat: "«&nbsp;Je lui vois&nbsp;» ne se dit pas. On voit <b>quelqu'un</b>, tout court — "
           + "retenez-le, on y revient dans un écran.",
        pourquoi: "Je le vois vendredi. On voit quelqu'un." },
      { txt: "Ma propriétaire attend une réponse.", sous: "Je ___ réponds demain.", ok: 'lui',
        rat: "«&nbsp;Je la réponds&nbsp;» ne se dit pas&nbsp;: on répond <b>à</b> quelqu'un. "
           + "C'est ce petit mot qui décide.",
        pourquoi: "Je lui réponds demain. On répond à quelqu'un." },
      { txt: "L'autobus passe à sept heures.", sous: "Je ___ prends tous les matins.", ok: 'le',
        rat: "On prend quelque chose, sans rien devant&nbsp;: «&nbsp;je le prends&nbsp;». "
           + "«&nbsp;Je lui prends&nbsp;» voudrait dire qu'on prend une chose <i>à</i> lui.",
        pourquoi: "Je le prends. On prend quelque chose." },
      { txt: "Ma sœur habite au Maroc.", sous: "Je ___ écris chaque dimanche.", ok: 'lui',
        rat: "«&nbsp;Je l'écris&nbsp;» existe, mais ça veut dire qu'on écrit <i>la lettre</i>, "
           + "pas qu'on écrit à sa sœur. On écrit <b>à</b> une personne.",
        pourquoi: "Je lui écris chaque dimanche. On écrit à quelqu'un." },
      { txt: "Ma voisine a deux gros sacs.", sous: "Je ___ aide à monter.", ok: 'le',
        rat: "Celui-là est difficile&nbsp;: on <i>aide</i> quelqu'un, sans petit mot devant. "
           + "«&nbsp;Je lui aide&nbsp;» s'entend beaucoup, et c'est une faute.",
        pourquoi: "Je l'aide à monter. On aide quelqu'un." },
      { txt: "Le préposé m'a laissé un message.", sous: "Je ___ demande de rappeler.", ok: 'lui',
        rat: "On demande <b>quelque chose à quelqu'un</b>&nbsp;: la personne arrive après le "
           + "«&nbsp;à&nbsp;». «&nbsp;Je le demande&nbsp;» voudrait dire qu'on demande le préposé.",
        pourquoi: "Je lui demande de rappeler. On demande à quelqu'un." },
      { txt: "Les documents sont sur la table.", sous: "Je ___ apporte demain.", ok: 'le',
        rat: "On apporte <b>quelque chose</b>&nbsp;: rien ne vient se glisser entre le verbe et "
           + "les documents. Au pluriel, c'est «&nbsp;les&nbsp;».",
        pourquoi: "Je les apporte demain. On apporte quelque chose." },
      { txt: "Mes parents attendent des nouvelles.", sous: "Je ___ parle une fois par semaine.", ok: 'lui',
        rat: "On parle <b>à</b> quelqu'un, jamais «&nbsp;je les parle&nbsp;». Au pluriel, le "
           + "pronom devient <b>leur</b>&nbsp;: «&nbsp;je leur parle&nbsp;».",
        pourquoi: "Je leur parle. On parle à quelqu'un — et au pluriel, c'est « leur »." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'La question au verbe',
    titre: "Vous avez séparé les verbes qui prennent « à » des autres.",
    paras: [
      "Regardez votre colonne «&nbsp;lui&nbsp;»&nbsp;: <b>répondre à</b>, <b>écrire à</b>, "
      + "<b>demander à</b>, <b>parler à</b>. Et l'autre&nbsp;: <b>voir</b>, <b>prendre</b>, "
      + "<b>aider</b>, <b>apporter</b> — rien entre le verbe et ce qui suit. Voilà toute la "
      + "règle, et vous venez de la trouver sans qu'on vous la dise.",

      "<b>Le test, à poser sur n'importe quel verbe&nbsp;:</b> dites le verbe tout seul et "
      + "posez-lui la question. «&nbsp;Je vois <b>qui</b>&nbsp;?&nbsp;» → pas de "
      + "«&nbsp;à&nbsp;», donc <i>le, la, les</i>. «&nbsp;Je parle <b>à qui</b>&nbsp;?&nbsp;» → "
      + "il y a un «&nbsp;à&nbsp;», donc <i>lui, leur</i>.",

      "Votre enseignant appellera la première colonne le <b>complément direct</b> et la seconde "
      + "le <b>complément indirect</b>. Vous n'avez pas besoin des noms pour vous en servir, "
      + "mais vous les entendrez.",
    ],
    retenir: "Posez la question au verbe. <b>Un «&nbsp;à&nbsp;» dans la question → lui, leur.</b> "
           + "Sinon → le, la, les. Une question vaut mieux qu'une liste&nbsp;: elle marche sur "
           + "un verbe que vous n'avez jamais vu.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Deux verbes du même sens, deux constructions. ─────────────────────
  {
    id:   'appeler-telephoner',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Appeler, téléphoner',
    titre: "« Appeler » et « téléphoner » veulent dire la même chose. Pas le même pronom.",
    consigne: "Vous écrivez à votre employeur au sujet du client de ce matin. Quelle phrase "
            + "est entièrement juste&nbsp;?",
    options: [
      { txt: "Je l'ai appelé ce matin et je lui ai téléphoné encore à midi.", juste: true },
      { txt: "Je lui ai appelé ce matin et je lui ai téléphoné encore à midi.",
        rat_t: "Le deuxième est bon. C'est le premier qui glisse.",
        rat: "On appelle <b>quelqu'un</b>&nbsp;: «&nbsp;j'appelle qui&nbsp;?&nbsp;», pas de "
           + "«&nbsp;à&nbsp;». Comme les deux verbes veulent dire la même chose, on leur donne "
           + "le même pronom — et c'est exactement là que la faute se fabrique." },
      { txt: "Je l'ai appelé ce matin et je l'ai téléphoné encore à midi.",
        rat_t: "Le premier est bon, et vous avez copié sur lui.",
        rat: "«&nbsp;J'appelle qui&nbsp;?&nbsp;» — donc «&nbsp;je l'ai appelé&nbsp;», parfait. "
           + "Mais «&nbsp;je téléphone <b>à</b> qui&nbsp;?&nbsp;»&nbsp;: le petit mot revient, "
           + "et le pronom change. Deux verbes voisins ne se construisent pas forcément pareil." },
    ],
    pourquoi: "<b>Appeler quelqu'un</b>, mais <b>téléphoner à quelqu'un</b>. Le sens ne décide "
            + "rien&nbsp;: c'est la question posée au verbe qui décide. Même piège avec "
            + "<i>aider quelqu'un</i> et <i>nuire à quelqu'un</i>.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Ce qui change de forme, et ce qui n'en change pas. ────────────────
  {
    id:   'homme-ou-femme',
    type: 'notion',
    eye: "L'autre moitié",
    menu: 'Homme ou femme',
    titre: "« Lui » ne dit pas si c'est un homme ou une femme. « Le » et « la », oui.",
    paras: [
      "C'est ce qui surprend le plus&nbsp;: <b>lui</b> sert pour les deux. «&nbsp;Je lui "
      + "réponds&nbsp;» peut parler de votre propriétaire, de votre sœur ou du préposé. Rien "
      + "dans le pronom ne le dit, et personne ne trouve ça ambigu.",

      "De l'autre côté, la forme suit ce qu'on remplace&nbsp;: <b>le</b> pour un homme ou un "
      + "objet masculin, <b>la</b> pour une femme ou un objet féminin, <b>les</b> pour "
      + "plusieurs. Et devant une voyelle, <i>le</i> et <i>la</i> deviennent tous les deux "
      + "<b>l'</b>&nbsp;: «&nbsp;je l'aide&nbsp;», «&nbsp;je l'appelle&nbsp;».",

      "Le pluriel du côté «&nbsp;à&nbsp;» est <b>leur</b>, sans <i>s</i>&nbsp;: «&nbsp;je leur "
      + "parle&nbsp;». À ne pas confondre avec «&nbsp;leur<b>s</b> enfants&nbsp;», qui est un "
      + "autre mot.",
    ],
    retenir: "<b>lui</b> et <b>leur</b> ne changent jamais selon l'homme ou la femme. "
           + "<b>le · la · les</b> suivent ce qu'ils remplacent, et se réduisent à "
           + "<b>l'</b> devant une voyelle.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-phrases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Une seule chose à faire&nbsp;: posez la question au verbe, et regardez s'il y "
            + "a un «&nbsp;à&nbsp;».",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je lui ai envoyé mon certificat hier.", ok: 'ok',
        rat: "On envoie quelque chose <b>à</b> quelqu'un&nbsp;: la personne arrive derrière le "
           + "«&nbsp;à&nbsp;», donc <i>lui</i>. La phrase tient.",
        pourquoi: "Envoyer à quelqu'un : lui. Juste." },
      { txt: "Je lui remercie de son appel.", ok: 'faux',
        rat: "On remercie <b>quelqu'un</b>&nbsp;: «&nbsp;je remercie qui&nbsp;?&nbsp;», aucun "
           + "«&nbsp;à&nbsp;». Ce qui trompe, c'est qu'on remercie quelqu'un <i>de</i> quelque "
           + "chose — mais le «&nbsp;de&nbsp;» porte la chose, pas la personne. "
           + "«&nbsp;Je le remercie.&nbsp;»",
        pourquoi: "Il faut « je le remercie »." },
      { txt: "La directrice est absente, je la rappelle lundi.", ok: 'ok',
        rat: "On rappelle <b>quelqu'un</b>, sans «&nbsp;à&nbsp;» — et il s'agit d'une femme, "
           + "donc <i>la</i>. Les deux moitiés sont justes.",
        pourquoi: "Rappeler quelqu'un : la. Juste." },
      { txt: "Mes collègues sont partis, je les ai dit au revoir.", ok: 'faux',
        rat: "On dit quelque chose <b>à</b> quelqu'un&nbsp;: ce sont les paroles qui suivent le "
           + "verbe, et les personnes qui arrivent après le «&nbsp;à&nbsp;». "
           + "«&nbsp;Je leur ai dit au revoir.&nbsp;»",
        pourquoi: "Il faut « je leur ai dit au revoir »." },
      { txt: "Mon fils est malade, je l'ai gardé à la maison.", ok: 'ok',
        rat: "On garde <b>quelqu'un</b>, sans petit mot devant&nbsp;; et devant la voyelle de "
           + "«&nbsp;ai&nbsp;», <i>le</i> devient <b>l'</b>. Rien à corriger.",
        pourquoi: "Garder quelqu'un : le, réduit en l'. Juste." },
      { txt: "Le propriétaire n'a rien fait, je le ai écrit deux fois.", ok: 'faux',
        rat: "Deux choses&nbsp;: on écrit <b>à</b> quelqu'un, donc <i>lui</i> — et de toute "
           + "façon, <i>le</i> ne reste jamais entier devant une voyelle. "
           + "«&nbsp;Je lui ai écrit deux fois.&nbsp;»",
        pourquoi: "Il faut « je lui ai écrit »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le cas le plus fréquent dans une vraie production. ────────────────
  {
    id:   'la-note',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Une note à corriger',
    titre: "Une note à l'école. Une seule ligne est fautive.",
    consigne: "«&nbsp;<i>Bonjour, mon fils sera absent demain. Je l'ai amené à la clinique ce "
            + "matin. Le médecin lui a donné un billet. Je vous le apporte vendredi.</i>&nbsp;»",
    options: [
      { txt: "« Je vous le apporte vendredi. »", juste: true },
      { txt: "« Je l'ai amené à la clinique. »",
        rat_t: "Celle-là est juste.",
        rat: "On amène <b>quelqu'un</b> quelque part&nbsp;: «&nbsp;j'amène qui&nbsp;?&nbsp;», "
           + "mon fils, sans «&nbsp;à&nbsp;» devant lui. Le «&nbsp;à la clinique&nbsp;» est le "
           + "lieu, pas la personne. Rien à corriger." },
      { txt: "« Le médecin lui a donné un billet. »",
        rat_t: "Celle-là est juste aussi.",
        rat: "On donne quelque chose <b>à</b> quelqu'un&nbsp;: le billet suit le verbe, la "
           + "personne arrive derrière le «&nbsp;à&nbsp;». Donc <i>lui</i>, et le pronom se "
           + "place devant l'auxiliaire." },
    ],
    pourquoi: "«&nbsp;Je vous <b>l'</b>apporte vendredi.&nbsp;» Le pronom était le bon — c'est "
            + "l'écriture qui manquait&nbsp;: <i>le</i> ne survit pas devant une voyelle. "
            + "C'est la faute qui reste quand toutes les autres sont réglées.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La place, dite en dernier : c'est ce qui ne varie jamais. ─────────
  {
    id:   'la-place',
    type: 'notion',
    eye:  'Ce qui ne bouge jamais',
    menu: 'Devant le verbe',
    titre: "Le pronom passe devant le verbe. Toujours, et sans exception ici.",
    paras: [
      "On a gardé ceci pour la fin, parce qu'il n'y a <b>rien à décider</b>&nbsp;: le pronom se "
      + "place <b>avant</b> le verbe, et c'est l'inverse de beaucoup de langues. On dit "
      + "«&nbsp;je <b>le</b> vois&nbsp;», jamais «&nbsp;je vois le&nbsp;».",

      "Au passé, il passe devant le petit verbe qui porte le temps&nbsp;: «&nbsp;je <b>lui</b> "
      + "ai téléphoné&nbsp;». Avec deux verbes, il se colle à celui qui porte le sens&nbsp;: "
      + "«&nbsp;je vais <b>le</b> rappeler&nbsp;», et non «&nbsp;je le vais rappeler&nbsp;».",

      "À la forme négative, le <i>ne</i> passe encore avant lui&nbsp;: «&nbsp;je ne <b>lui</b> "
      + "ai pas répondu&nbsp;». Autrement dit, vous n'avez qu'une seule chose à choisir quand "
      + "vous écrivez&nbsp;: <b>lequel</b> des deux pronoms. Sa place, elle, ne se choisit pas.",
    ],
    retenir: "Une seule décision à prendre&nbsp;: <b>le · la · les</b> ou <b>lui · leur</b>. "
           + "La place est toujours la même — devant le verbe.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Un texto à une amie qui garde vos enfants. Quelle version tient d'un bout à l'autre ?",
    consigne: "Trois versions du même message. Une seule est correcte partout.",
    options: [
      { txt: "J'amène les à sept heures et je reprends les à midi. Je t'ai écrit hier pour prévenir.",
        rat_t: "Les pronoms sont les bons. Ils sont du mauvais côté du verbe.",
        rat: "«&nbsp;Les&nbsp;» est juste deux fois — on amène et on reprend <b>quelqu'un</b>, sans "
           + "«&nbsp;à&nbsp;». Mais en français, le pronom passe <b>devant</b> le verbe&nbsp;: "
           + "«&nbsp;je les amène&nbsp;». C'est l'ordre de beaucoup d'autres langues, et il "
           + "survit longtemps à l'écrit." },
      { txt: "Je les amène à sept heures et je les reprends à midi. Je t'ai écrit hier pour prévenir.",
        juste: true },
      { txt: "Je leur amène à sept heures et je leur reprends à midi. Je t'ai écrit hier pour prévenir.",
        rat_t: "Les deux verbes sont passés du mauvais côté.",
        rat: "«&nbsp;J'amène qui&nbsp;?&nbsp;» — les enfants, sans «&nbsp;à&nbsp;». "
           + "«&nbsp;Je reprends qui&nbsp;?&nbsp;» — pareil. Ce sont exactement les deux verbes "
           + "qui n'appellent pas de «&nbsp;à&nbsp;». Seul «&nbsp;je t'ai écrit&nbsp;» était au "
           + "bon endroit&nbsp;: on écrit <b>à</b> quelqu'un." },
    ],
    pourquoi: "Deux verbes sans «&nbsp;à&nbsp;» avec <i>les</i>, un verbe avec «&nbsp;à&nbsp;» "
            + "avec <i>te</i>. <b>C'est tout le point en une phrase</b> — et un seul pronom "
            + "à la fois.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au voisin du début. Cette fois, vous l'écrivez.",
    consigne: "Vous laissez un mot dans sa boîte aux lettres&nbsp;: vous allez lui téléphoner "
            + "ce soir et lui remettre son colis. Quelle phrase écrivez-vous&nbsp;?",
    options: [
      { txt: "« Je vous téléphone ce soir et je vous remets votre colis. »", juste: true },
      { txt: "« Je vous téléphone ce soir et je le remets votre colis. »",
        rat_t: "Le premier verbe est bon. Le second a perdu la personne.",
        rat: "«&nbsp;Je remets à qui&nbsp;?&nbsp;» — à vous. Le pronom doit désigner la "
           + "<b>personne</b>&nbsp;; «&nbsp;le&nbsp;» désignerait le colis, qui est déjà écrit "
           + "juste après. La phrase le nommerait deux fois." },
      { txt: "« Je le téléphone ce soir et je vous remets votre colis. »",
        rat_t: "C'est la phrase de l'écran 1.",
        rat: "On téléphone <b>à</b> quelqu'un&nbsp;: le pronom ne peut pas être «&nbsp;le&nbsp;». "
           + "Ici, comme vous vous adressez directement au voisin, c'est <b>vous</b> — la même "
           + "famille que <i>lui</i>, à la personne à qui l'on parle." },
    ],
    pourquoi: "«&nbsp;Je <b>vous</b> téléphone et je <b>vous</b> remets votre colis.&nbsp;» "
            + "Vous avez posé la question au verbe deux fois, et vous avez trouvé "
            + "«&nbsp;à&nbsp;» les deux fois.",
    attente: "Choisissez une réponse pour finir.",
  },

];
