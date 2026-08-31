// ═══════════════════════════════════════════════════════════════════════════
// Point express — L'accord du participe passé avec être
//
// Savoir n5-s37 (« Participe passé » — accorder le participe passé employé
// seul). Une ORDONNANCE : l'enseignant l'envoie à un élève dont un écrit
// montre « elle est allé », « ils sont parti ». Dix minutes, dix écrans.
//
// ── Ce dont il s'écarte, et comment ────────────────────────────────────────
// La mini-leçon de référence est `module-n4-etablissement` (bloc t3pc),
// « Le passé composé avec être, et son accord » : elle énonce la règle en une
// phrase, donne la quinzaine de verbes en trois colonnes, les quatre formes en
// tableau, les pronominaux, trois pièges et quatre questions. C'est une leçon
// complète, et elle se lit. Un élève envoyé ici l'a déjà lue. Les cinq écarts :
//
//   1. INDUCTIF, ET LE TRI NE PARLE PAS DE GRAMMAIRE. L'écran 2 fait ranger
//      six fins de phrase selon QUI a écrit — un homme, une femme, plusieurs.
//      Aucun sujet n'est donné : seule la fin du mot renseigne. La tâche est
//      faisable sans rien savoir, et la règle de l'écran 3 n'est que le
//      constat de ce tri.
//   2. AUCUNE LISTE DE VERBES. La mini-leçon en donne quinze en bloc ; ce
//      point n'en donne aucune. Le CHOIX de l'auxiliaire est le sujet d'un
//      autre point express (`passe-compose-etre-avoir`) : ici, l'auxiliaire
//      est toujours déjà écrit, et il n'y a qu'une chose à décider — la fin
//      du mot. Confondre les deux difficultés est précisément ce qui rend
//      celle-ci insurmontable alors qu'elle est simple.
//   3. UN TEST, ET IL EST TRIVIAL : remplacer le participe par « content ».
//      Ce qu'on écrirait pour « content » s'écrit pour le participe. C'est
//      aussi ce qui relie le passé composé au point du programme — le
//      participe employé seul (« une place réservée »), traité à l'écran 5 :
//      un seul mécanisme, deux emplois.
//   4. ON DIT FRANCHEMENT QUE C'EST FACILE. Avec être, l'accord est
//      systématique : il n'y a ni exception ni condition à vérifier. Le point
//      le répète (écrans 3, 8, 10) parce qu'un élève qui a entendu parler de
//      l'accord avec AVOIR croit que celui-ci est aussi compliqué, et se
//      met à douter là où il n'y a rien à décider. Ce point reste donc
//      FRANCHEMENT EN DEÇÀ de `accord-participe-avoir` (n8-s21) : ni « quoi ? »
//      posé après le verbe, ni complément direct, ni pronom antéposé, ni
//      relatif « que ». L'écran 8 borne le territoire en une phrase et
//      renvoie la suite à plus tard.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS. Un texto à une collègue, une
//      note à l'école, un courriel à un employeur, un avis de garage. Aucune
//      phrase, aucun personnage, aucun scénario d'un module.
//
// Aucun média, et c'est le sujet même : « allé » et « allée » se prononcent
// pareil. Un point qui ferait entendre la différence mentirait.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'participe-passe-avec-etre',
  titre:    "L'accord du participe passé avec être",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s37',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Un texto',
    titre: "Farida écrit à sa collègue. Une seule version s'écrit. Laquelle ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Je suis parti avant la fin de la réunion.&nbsp;»",
        rat_t: "Il manque une lettre, et elle ne s'entend pas.",
        rat: "Rien ne cloche à l'oreille&nbsp;: dit à voix haute, c'est exactement la bonne "
           + "phrase. C'est là tout le problème — la faute ne se voit qu'écrite, et personne "
           + "ne l'a jamais corrigée à l'oral. Regardez l'autre version&nbsp;: la différence "
           + "tient à un seul caractère." },
      { txt: "«&nbsp;Je suis partie avant la fin de la réunion.&nbsp;»", juste: true },
      { txt: "Les deux s'écrivent&nbsp;; c'est une question de style.",
        rat_t: "Ce n'est pas du style, c'est de l'information.",
        rat: "La lettre finale n'embellit rien&nbsp;: elle dit <b>qui écrit</b>. Enlevez-la et "
           + "la phrase annonce un homme. C'est pour cela qu'on ne peut pas choisir." },
    ],
    pourquoi: "«&nbsp;Je suis part<b>ie</b>&nbsp;», parce que Farida est une femme. Gardez la "
            + "phrase telle quelle&nbsp;; on va voir dans un instant que la décision est "
            + "beaucoup plus mécanique qu'elle n'en a l'air.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. Aucun sujet n'est donné. ─────────────────
  {
    id:   'qui-a-ecrit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six bouts de phrase',
    titre: "Six bouts de phrase, sans leur début. Qui a écrit chacun ?",
    consigne: "On a effacé le début&nbsp;: vous ne savez pas qui parle. La fin du mot, elle, "
            + "est restée. Aucune règle ne vous a été donnée — servez-vous de ce que vous "
            + "voyez.",
    colonnes: [
      { id: 'h',  t: 'Un homme',           b: 'Un homme' },
      { id: 'f',  t: 'Une femme',          b: 'Une femme' },
      { id: 'pl', t: 'Plusieurs personnes', b: 'Plusieurs' },
    ],
    items: [
      { txt: "…&nbsp;est descendue au sous-sol", sous: "un mot de plus à la fin", ok: 'f',
        rat: "Le mot se termine par un «&nbsp;e&nbsp;» et rien d'autre&nbsp;: pas de "
           + "«&nbsp;s&nbsp;», donc une seule personne. Ce «&nbsp;e&nbsp;» ne s'entend pas, "
           + "mais il se lit.",
        pourquoi: "Un « e » seul : une femme." },
      { txt: "…&nbsp;est monté à l'étage", sous: "rien après le « é »", ok: 'h',
        rat: "Le mot s'arrête net. Aucune lettre ajoutée&nbsp;: c'est la forme la plus courte, "
           + "et c'est celle d'un homme seul.",
        pourquoi: "Aucune lettre ajoutée : un homme." },
      { txt: "…&nbsp;sont entrés par la porte de côté", sous: "un « s » à la fin", ok: 'pl',
        rat: "Le «&nbsp;s&nbsp;» ne se prononce pas davantage que le «&nbsp;e&nbsp;», mais il "
           + "dit la même chose que dans «&nbsp;deux billets&nbsp;»&nbsp;: il y en a plusieurs.",
        pourquoi: "Un « s » : plusieurs personnes." },
      { txt: "…&nbsp;est restée deux jours à l'hôpital", sous: "« e » final", ok: 'f',
        rat: "Même fin que le premier, même conclusion. Le verbe a changé, la lettre non&nbsp;: "
           + "c'est ce qui devrait commencer à vous intriguer.",
        pourquoi: "« e » : une femme, quel que soit le verbe." },
      { txt: "…&nbsp;sont sorties vers midi", sous: "« e » puis « s »", ok: 'pl',
        rat: "Les deux lettres se cumulent&nbsp;: le «&nbsp;e&nbsp;» dit des femmes, le "
           + "«&nbsp;s&nbsp;» dit qu'elles sont plusieurs. La colonne demandée est le nombre.",
        pourquoi: "« es » : plusieurs, et ce sont des femmes." },
      { txt: "…&nbsp;est revenu chercher ses clés", sous: "rien après le « u »", ok: 'h',
        rat: "Rien n'a été ajouté au mot. C'est la forme nue&nbsp;: un homme, une personne.",
        pourquoi: "Forme nue : un homme." },
    ],
    attente: "Tranchez les six bouts de phrase pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat, et le test. ────────────────────
  {
    id:   'comme-content',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez lu la fin du mot, et vous ne vous êtes pas trompé.",
    paras: [
      "Vous n'aviez ni le sujet, ni le verbe à l'infinitif, ni aucune règle&nbsp;: seulement "
      + "trois fins possibles — rien, un «&nbsp;e&nbsp;», un «&nbsp;s&nbsp;», ou les deux. "
      + "Et ça a suffi. C'est exactement ce que fait un lecteur québécois quand il vous lit.",

      "Le mot qui porte cette fin s'appelle le <b>participe passé</b>&nbsp;; lui ajouter une "
      + "lettre s'appelle <b>l'accorder</b>. Le nom n'ajoute rien à ce que vous venez de "
      + "faire, mais votre enseignant l'emploiera.",

      "<b>Le test, à vous poser sur n'importe quelle phrase&nbsp;:</b> remplacez le participe "
      + "par le mot <b>content</b>. «&nbsp;Elle est <i>contente</i>&nbsp;» → «&nbsp;elle est "
      + "part<b>ie</b>&nbsp;». «&nbsp;Ils sont <i>contents</i>&nbsp;» → «&nbsp;ils sont "
      + "entr<b>és</b>&nbsp;». La lettre que vous écririez pour «&nbsp;content&nbsp;», "
      + "écrivez-la pour le participe.",

      "Et c'est tout. Avec <i>être</i>, il n'y a <b>ni exception, ni condition à vérifier</b>&nbsp;: "
      + "ça marche à tous les coups, sur tous les verbes, dans tous les textes.",
    ],
    retenir: "Après <b>être</b>, le participe se comporte comme <b>content</b>. "
           + "Une seule question&nbsp;: qui est-ce&nbsp;? Et vous écrivez la même lettre.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : se relire à voix haute ne trouve rien. ─────────────────
  {
    id:   'relire-a-voix-haute',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'Se relire',
    titre: "Pourquoi vous ne trouvez jamais cette faute en vous relisant",
    consigne: "Quatre personnes écrivent la même journée. Dans laquelle de ces phrases "
            + "entendrait-on la faute si on lisait à voix haute&nbsp;?",
    options: [
      { txt: "Dans aucune&nbsp;: toutes les fins se prononcent pareil.", juste: true },
      { txt: "Dans celles au féminin, parce que le «&nbsp;e&nbsp;» s'entend.",
        rat_t: "C'est vrai dans d'autres mots, pas dans ceux-là.",
        rat: "Le «&nbsp;e&nbsp;» final s'entend dans «&nbsp;grand / grande&nbsp;» ou "
           + "«&nbsp;petit / petite&nbsp;», parce qu'il réveille une consonne. Après une "
           + "voyelle — all<b>é</b>, part<b>i</b>, venu — il n'y a aucune consonne à "
           + "réveiller&nbsp;: on n'ajoute rien à l'oreille." },
      { txt: "Dans celles au pluriel, à cause du «&nbsp;s&nbsp;».",
        rat_t: "Le « s » du pluriel ne se prononce jamais.",
        rat: "«&nbsp;Il est entré&nbsp;» et «&nbsp;ils sont entrés&nbsp;» se distinguent par "
           + "le début de la phrase, pas par la fin du participe. Le «&nbsp;s&nbsp;» est muet "
           + "ici comme dans «&nbsp;des amis&nbsp;»." },
    ],
    pourquoi: "C'est la raison pour laquelle cette faute traverse des années&nbsp;: elle ne "
            + "s'attrape pas à l'oreille. <b>Elle se vérifie avec les yeux, une phrase à la "
            + "fois, avant d'envoyer.</b> Le conseil «&nbsp;relis-toi à voix haute&nbsp;» est "
            + "excellent pour tout le reste et sans aucun effet ici.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le participe sans verbe : le même mécanisme, autre emploi. ────────
  {
    id:   'sans-etre',
    type: 'notion',
    eye:  'Le même mot, ailleurs',
    menu: 'Sur une affiche',
    titre: "Vous connaissez déjà ces formes : elles sont sur les affiches.",
    paras: [
      "«&nbsp;Place <b>réservée</b>&nbsp;». «&nbsp;Documents <b>signés</b>&nbsp;». "
      + "«&nbsp;Porte <b>fermée</b>&nbsp;». «&nbsp;Rendez-vous <b>annulé</b>&nbsp;». Ce sont "
      + "les mêmes mots que tout à l'heure, sans le verbe <i>être</i> devant — et ils prennent "
      + "exactement les mêmes lettres.",

      "Le test ne change pas d'un mot&nbsp;: on dirait «&nbsp;une place <i>contente</i>&nbsp;», "
      + "donc «&nbsp;une place réserv<b>ée</b>&nbsp;»&nbsp;; on dirait «&nbsp;des documents "
      + "<i>contents</i>&nbsp;», donc «&nbsp;des documents sign<b>és</b>&nbsp;». Le participe "
      + "s'accorde avec le mot qu'il décrit, ici comme après <i>être</i>.",

      "Un garage vous écrit&nbsp;: «&nbsp;<i>Les pièces commandées sont arrivées, votre voiture "
      + "sera prête vendredi.</i>&nbsp;» Deux participes dans la même ligne&nbsp;: "
      + "<b>commandées</b> décrit les pièces, <b>arrivées</b> suit le verbe <i>sont</i>. Deux "
      + "emplois, une seule lettre à décider, et la même.",
    ],
    retenir: "Avec <i>être</i> ou tout seul devant un nom, c'est <b>le même mot et la même "
           + "fin</b>. Vous n'avez pas deux choses à apprendre.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites, avec le test en main. ──────────────────
  {
    id:   'tri-correct',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases prises dans de vrais messages. Lesquelles sont correctes ?",
    consigne: "Une seule chose à regarder&nbsp;: la fin du participe. Faites le test avec "
            + "«&nbsp;content&nbsp;» avant de trancher.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "«&nbsp;Ma fille est arrivée en retard ce matin.&nbsp;»", sous: "note à l'école",
        ok: 'ok',
        rat: "«&nbsp;Ma fille est <i>contente</i>&nbsp;» — donc «&nbsp;arriv<b>ée</b>&nbsp;». "
           + "La lettre est là, la phrase est bonne.",
        pourquoi: "« Ma fille est contente » : arrivée. Juste." },
      { txt: "«&nbsp;Mes deux collègues sont resté à la réunion.&nbsp;»", sous: "courriel interne",
        ok: 'faux',
        rat: "Le mot semble complet, et c'est ce qui trompe&nbsp;: il l'est au singulier. "
           + "«&nbsp;Mes collègues sont <i>contents</i>&nbsp;» — il faut donc "
           + "«&nbsp;rest<b>és</b>&nbsp;».",
        pourquoi: "Il manque le « s » : sont restés." },
      { txt: "«&nbsp;Je suis venue vous rencontrer vendredi.&nbsp;»", sous: "message d'une candidate",
        ok: 'ok',
        rat: "Une femme écrit&nbsp;: «&nbsp;je suis <i>contente</i>&nbsp;», donc "
           + "«&nbsp;ven<b>ue</b>&nbsp;». Rien d'autre à vérifier.",
        pourquoi: "Une femme écrit : venue. Juste." },
      { txt: "«&nbsp;Les colis sont livré depuis mardi.&nbsp;»", sous: "avis d'un commerce",
        ok: 'faux',
        rat: "Le participe est ici après <i>sont</i>, comme les autres. «&nbsp;Les colis sont "
           + "<i>contents</i>&nbsp;» sonne étrange, mais le test ne demande pas d'y croire&nbsp;: "
           + "il demande quelle lettre on écrirait. Un «&nbsp;s&nbsp;»&nbsp;: "
           + "«&nbsp;livr<b>és</b>&nbsp;».",
        pourquoi: "Il manque le « s » : sont livrés." },
      { txt: "«&nbsp;Nous sommes entrés par la porte de côté.&nbsp;»", sous: "texto à un voisin",
        ok: 'ok',
        rat: "«&nbsp;Nous&nbsp;», c'est plusieurs personnes&nbsp;: «&nbsp;nous sommes "
           + "<i>contents</i>&nbsp;», donc «&nbsp;entr<b>és</b>&nbsp;». Le «&nbsp;s&nbsp;» est "
           + "bien là.",
        pourquoi: "« Nous sommes contents » : entrés. Juste." },
      { txt: "«&nbsp;Ma sœur est tombé dans l'escalier.&nbsp;»", sous: "message à un ami",
        ok: 'faux',
        rat: "C'est la faute la plus fréquente de toutes&nbsp;: le sujet est féminin, mais on "
           + "écrit le mot comme on l'entend. «&nbsp;Ma sœur est <i>contente</i>&nbsp;» — donc "
           + "«&nbsp;tomb<b>ée</b>&nbsp;».",
        pourquoi: "Il manque le « e » : elle est tombée." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Une vraie production, une seule ligne fautive. ────────────────────
  {
    id:   'le-courriel',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un courriel à corriger',
    titre: "Rosalie écrit à son employeur. Une seule ligne est fautive.",
    consigne: "«&nbsp;<i>Bonjour, je suis passée à la clinique ce matin. Mes résultats sont "
            + "arrivés hier. Je suis rentré à la maison vers midi et je serai au travail "
            + "demain.</i>&nbsp;»",
    options: [
      { txt: "«&nbsp;Je suis rentré à la maison vers midi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je suis passée à la clinique ce matin.&nbsp;»",
        rat_t: "Celle-là est juste.",
        rat: "Rosalie est une femme et le «&nbsp;e&nbsp;» est écrit&nbsp;: "
           + "«&nbsp;pass<b>ée</b>&nbsp;». C'est justement la ligne qui montre qu'elle connaît "
           + "la règle — et qui rend l'autre oubli visible." },
      { txt: "«&nbsp;Mes résultats sont arrivés hier.&nbsp;»",
        rat_t: "Celle-là est juste aussi.",
        rat: "Ici le participe ne parle pas de Rosalie mais des résultats&nbsp;: plusieurs, "
           + "donc «&nbsp;arriv<b>és</b>&nbsp;». Attention à ce déplacement — la lettre suit "
           + "toujours <b>ce dont on parle</b>, pas la personne qui écrit." },
    ],
    pourquoi: "«&nbsp;Je suis rentr<b>ée</b>&nbsp;». Deux lignes sur trois étaient bonnes&nbsp;: "
            + "l'oubli n'est presque jamais une méconnaissance de la règle, c'est une "
            + "inattention en cours de texte. <b>C'est pourquoi la vérification se fait à la "
            + "fin, ligne par ligne.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier : avec avoir, on ne touche rien. ─
  {
    id:   'avec-avoir-rien',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "L'autre auxiliaire",
    titre: "Avec « avoir », vous ne touchez à rien.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est volontaire. Quand la phrase commence par "
      + "<i>j'ai</i>, <i>elle a</i>, <i>nous avons</i>, le participe <b>ne bouge pas</b>&nbsp;: "
      + "j'ai téléphoné, elle a téléphoné, nous avons téléphoné, elles ont téléphoné. Un seul "
      + "mot, jamais rien à ajouter.",

      "Autrement dit, vous n'avez <b>qu'une seule chose</b> à surveiller quand vous "
      + "écrivez&nbsp;: les phrases qui contiennent <i>suis, es, est, sommes, êtes, sont</i>. "
      + "Partout ailleurs, écrivez sans y penser.",

      "Il existe bien un cas où le participe s'accorde après <i>avoir</i>, mais il est rare, "
      + "il demande une vérification particulière, et <b>ce n'est pas votre affaire "
      + "aujourd'hui</b>. Le mêler à ce que vous venez de faire ne ferait que vous rendre "
      + "hésitant là où il n'y a rien à décider.",
    ],
    retenir: "Une seule règle&nbsp;: après <b>être</b>, on accorde, toujours. "
           + "Après <b>avoir</b>, on n'écrit rien de plus.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Une suite entière à tenir, pas une phrase isolée. ─────────────────
  {
    id:   'la-suite',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Trois lignes de suite',
    titre: "Trois versions du même message. Une seule tient d'un bout à l'autre.",
    consigne: "Amina raconte sa matinée à son groupe. Regardez chaque participe, l'un après "
            + "l'autre.",
    options: [
      { txt: "«&nbsp;Je suis arrivée à huit heures, j'ai attendu vingt minutes, et les autres "
           + "sont entrés après moi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je suis arrivé à huit heures, j'ai attendu vingt minutes, et les autres "
           + "sont entrés après moi.&nbsp;»",
        rat_t: "Le pluriel est bon. C'est Amina qui a disparu.",
        rat: "«&nbsp;Sont entr<b>és</b>&nbsp;» est parfaitement écrit — donc la règle est "
           + "acquise. Mais la première ligne parle d'Amina&nbsp;: «&nbsp;je suis "
           + "arriv<b>ée</b>&nbsp;». C'est l'oubli typique&nbsp;: on accorde ce qui est loin "
           + "de soi et on s'oublie soi-même." },
      { txt: "«&nbsp;Je suis arrivée à huit heures, j'ai attendue vingt minutes, et les autres "
           + "sont entrés après moi.&nbsp;»",
        rat_t: "Une lettre de trop, au milieu.",
        rat: "Les deux participes après <i>être</i> sont justes. Mais «&nbsp;j'<b>ai</b> "
           + "attendu&nbsp;» n'est pas de la même famille&nbsp;: après <i>avoir</i>, on "
           + "n'ajoute rien. C'est l'excès de zèle qui suit toujours une règle fraîchement "
           + "apprise." },
    ],
    pourquoi: "Deux participes après <i>être</i>, accordés chacun avec ce dont il parle&nbsp;; "
            + "un participe après <i>avoir</i>, laissé intact. <b>C'est tout le point express "
            + "en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au texto du début, avec deux personnes cette fois.",
    consigne: "Farida et sa collègue ont quitté la réunion ensemble. Farida écrit à leur "
            + "responsable&nbsp;: quelle version&nbsp;?",
    options: [
      { txt: "«&nbsp;Nous sommes parties avant la fin.&nbsp;»", juste: true },
      { txt: "«&nbsp;Nous sommes parti avant la fin.&nbsp;»",
        rat_t: "C'est la forme de l'écran 1, restée telle quelle.",
        rat: "Le sujet a changé — deux femmes maintenant — et le participe ne l'a pas suivi. "
           + "«&nbsp;Nous sommes <i>contentes</i>&nbsp;»&nbsp;: il faut le «&nbsp;e&nbsp;» "
           + "<b>et</b> le «&nbsp;s&nbsp;»." },
      { txt: "«&nbsp;Nous sommes partis avant la fin.&nbsp;»",
        rat_t: "Le pluriel y est. Il manque l'autre lettre.",
        rat: "Vous avez vu le plus difficile&nbsp;: «&nbsp;nous&nbsp;» demande un "
           + "«&nbsp;s&nbsp;». Mais ce sont deux femmes&nbsp;: «&nbsp;part<b>ies</b>&nbsp;». "
           + "Avec un seul homme dans le groupe, votre réponse aurait été la bonne." },
    ],
    pourquoi: "«&nbsp;Nous sommes part<b>ies</b>&nbsp;». Vous avez fait tout le trajet&nbsp;: "
            + "repérer <i>être</i>, regarder de qui on parle, écrire la lettre de "
            + "«&nbsp;content&nbsp;». <b>Aucune exception ne vous attend&nbsp;: c'est la même "
            + "opération à chaque fois.</b>",
    attente: "Choisissez une réponse pour finir.",
  },

];
