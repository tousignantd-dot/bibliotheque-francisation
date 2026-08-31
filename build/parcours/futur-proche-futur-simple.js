// ═══════════════════════════════════════════════════════════════════════════
// Point express — « Je vais aller » ou « j'irai » ?
//
// Savoir n3-s30 (indicatif futur simple, en reconnaissance). Dix minutes,
// dix écrans. Une ORDONNANCE : l'enseignant l'envoie à un élève qui bute sur
// les avis écrits, ou qui écrit à un bureau comme il parle à un voisin.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Onze mini-leçons portent sur l'un des deux futurs. Les trois plus proches :
// `module-n3-electro` (« Le futur proche : ce qui va arriver samedi »),
// `module-n3-voisins` (« Ce qui va arriver, et ce qui aura lieu ») et surtout
// `module-n5-saisons` (« Futur proche ou futur simple ? »), qui pose la même
// question deux niveaux plus haut, avec le « si » de condition et la
// conjugaison à produire. Les cinq écarts tenus :
//
//   1. RECONNAÎTRE, PAS CONJUGUER. Le programme du niveau 3 ne demande que
//      de « reconnaître quelques verbes en contexte formel ». Aucune
//      terminaison à apprendre, aucun tableau -rai/-ras/-ra : le point
//      express n'exige jamais de l'élève qu'il produise un futur simple.
//      C'est la mini-leçon du niveau 5 qui fera ça.
//   2. INDUCTIF. L'élève range huit phrases selon un critère qui n'est pas
//      grammatical — ça se dit, ou ça s'écrit — AVANT qu'aucun nom de temps
//      ne soit prononcé.
//   3. UN TEST DE FORME, PAS UNE LISTE DE VERBES. Deux mots avec « aller » →
//      c'est ce que je dis. Un seul mot, et un « r » juste avant la fin → ce
//      que je lis. Ce test marche sur « viendra » ou « recevrez », des verbes
//      qu'aucune leçon n'a montrés.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Futur proche » et « futur simple » ne
//      sont écrits qu'à l'écran 3, une fois le tri fait.
//   5. EXEMPLES PRIS À PLUSIEURS SITUATIONS, JAMAIS À UN MODULE. Un avis sur
//      une porte, un texto, une lettre d'un bureau, un message à un
//      employeur. Le point ne dépend d'aucun scénario.
//
// Aucun média : la différence se voit sur du papier autant qu'elle s'entend,
// et l'élève a besoin de la LIRE. Tout se corrige par comparaison de chaînes.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'futur-proche-futur-simple',
  titre:    "« Je vais aller » ou « j'irai » ?",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s30',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Au téléphone',
    titre: "Vous appelez la clinique pour annuler. Qu'est-ce qui sort de votre bouche ?",
    consigne: "Répondez avec ce que vous avez déjà entendu autour de vous — c'est fait exprès.",
    options: [
      { txt: "« Je vais annuler mon rendez-vous de jeudi. »", juste: true },
      { txt: "« J'annulerai mon rendez-vous de jeudi. »",
        rat_t: "Ce n'est pas une faute. C'est le mauvais endroit.",
        rat: "La phrase est correcte, et c'est pour ça qu'elle trompe. Mais au téléphone, au "
           + "Québec, presque personne ne dit ça&nbsp;: elle sonne comme une lettre lue à voix "
           + "haute. Regardez l'autre&nbsp;: c'est celle qu'on entend au comptoir toute la "
           + "journée." },
      { txt: "« J'annule mon rendez-vous de jeudi. »",
        rat_t: "Celle-là parle de maintenant.",
        rat: "Au présent, elle dit que vous êtes en train d'annuler — ce qui n'est pas faux au "
           + "téléphone, d'ailleurs. Mais la question portait sur ce qui n'est pas encore "
           + "arrivé&nbsp;: jeudi." },
    ],
    pourquoi: "«&nbsp;Je <b>vais annuler</b>.&nbsp;» Retenez la phrase entière pour "
            + "l'instant&nbsp;; on va voir pourquoi juste après.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir, et sur un critère non grammatical. ───────
  {
    id:   'tri-bouche-papier',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases qui parlent de plus tard. Où les avez-vous rencontrées ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Une seule question&nbsp;: est-ce "
            + "qu'on vous <b>dit</b> cette phrase, ou est-ce que vous la <b>lisez</b> quelque "
            + "part&nbsp;?",
    colonnes: [
      { id: 'dit',   t: 'On me le dit',  b: 'On me le dit' },
      { id: 'ecrit', t: 'Je le lis',     b: 'Je le lis' },
    ],
    items: [
      { txt: "Je vais te rappeler dans cinq minutes.", sous: "au téléphone", ok: 'dit',
        rat: "Personne n'écrit ça sur une affiche. C'est une phrase de conversation, et sa "
           + "forme le montre — on y reviendra.",
        pourquoi: "Une phrase de conversation. Deux mots : vais + rappeler." },
      { txt: "Le bureau sera fermé le 24 décembre.", sous: "sur une porte", ok: 'ecrit',
        rat: "C'est un avis affiché. On ne dirait pas ça à quelqu'un dans le corridor&nbsp;: "
           + "on lui dirait plutôt «&nbsp;ça va être fermé le 24&nbsp;».",
        pourquoi: "Un avis affiché. Un seul mot : sera." },
      { txt: "On va manger vers six heures.", sous: "à la maison", ok: 'dit',
        rat: "Aucune chance de lire ça sur un papier officiel. C'est de la parole ordinaire.",
        pourquoi: "De la parole ordinaire. Deux mots : va + manger." },
      { txt: "Vous recevrez votre carte dans dix jours.", sous: "dans une lettre", ok: 'ecrit',
        rat: "C'est la phrase type des lettres d'un bureau. Au comptoir, la même personne vous "
           + "dirait «&nbsp;vous allez la recevoir dans dix jours&nbsp;».",
        pourquoi: "Une lettre officielle. Un seul mot : recevrez." },
      { txt: "Je vais aller chercher les enfants.", sous: "en partant du travail", ok: 'dit',
        rat: "Six mots de tous les jours. On ne les écrit nulle part, on les dit.",
        pourquoi: "Tous les jours. Deux mots : vais + aller." },
      { txt: "La rencontre aura lieu le 3 mai à 19 h.", sous: "dans un courriel de l'école", ok: 'ecrit',
        rat: "«&nbsp;Aura lieu&nbsp;» ne se dit à peu près jamais&nbsp;: c'est de l'écrit "
           + "d'annonce, une convocation, un avis.",
        pourquoi: "Un courriel d'annonce. Un seul mot : aura." },
      { txt: "Ça va être long ?", sous: "dans la file d'attente", ok: 'dit',
        rat: "Une question qu'on pose à voix haute, à quelqu'un qui est devant nous. Elle "
           + "n'existe pas à l'écrit.",
        pourquoi: "Une question posée à voix haute. Deux mots : va + être." },
      { txt: "L'autobus 55 ne circulera pas dimanche.", sous: "sur un panneau à l'arrêt", ok: 'ecrit',
        rat: "Un panneau. Le chauffeur, lui, vous dirait «&nbsp;il va pas passer dimanche&nbsp;».",
        pourquoi: "Un panneau. Un seul mot : circulera." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Un mot ou deux',
    titre: "Vous n'avez pas trié de la grammaire. Vous avez trié des endroits.",
    paras: [
      "Et pourtant, regardez les formes. Dans la colonne «&nbsp;on me le dit&nbsp;», toutes les "
      + "phrases ont <b>deux mots</b>&nbsp;: <i>vais rappeler</i>, <i>va manger</i>, <i>vais "
      + "aller</i>, <i>va être</i>. Le premier est toujours une forme d'<b>aller</b>.",

      "Dans la colonne «&nbsp;je le lis&nbsp;», toutes ont <b>un seul mot</b>, et ce mot a un "
      + "<b>r</b> juste avant la fin&nbsp;: se<b>r</b>a, recev<b>r</b>ez, au<b>r</b>a, "
      + "circule<b>r</b>a. C'est le signe le plus fiable qu'il existe, et il ne vous "
      + "demande de connaître aucun verbe.",

      "Votre enseignant appelle le premier le <b>futur proche</b> et le second le <b>futur "
      + "simple</b>. Au Québec, le futur proche occupe presque tout l'oral&nbsp;; le futur "
      + "simple vit dans les avis, les lettres et les courriels d'un bureau.",
    ],
    retenir: "<b>Deux mots avec «&nbsp;aller&nbsp;» → ce que je dis.</b> "
           + "<b>Un seul mot, avec un «&nbsp;r&nbsp;» avant la fin → ce que je lis.</b> "
           + "Un signe se réemploie&nbsp;; une liste de verbes s'oublie.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le test à l'épreuve d'une lettre réelle. ──────────────────────────
  {
    id:   'la-lettre',
    type: 'verif',
    eye:  'Le cas qui compte',
    menu: 'Une lettre',
    titre: "Une lettre vous dit : « Vous recevrez votre carte dans dix jours. »",
    consigne: "Qu'est-ce que ça veut dire pour vous&nbsp;?",
    options: [
      { txt: "La carte n'est pas encore arrivée. Elle arrivera plus tard.", juste: true },
      { txt: "La carte est déjà partie, vous l'avez sûrement reçue.",
        rat_t: "«&nbsp;Recevrez&nbsp;» ressemble à «&nbsp;reçu&nbsp;», et c'est le piège.",
        rat: "Les deux mots viennent du même verbe, mais l'un regarde en arrière et l'autre en "
           + "avant. Le <b>r</b> avant la fin — recev<b>r</b>ez — dit que la chose n'a pas "
           + "encore eu lieu. C'est une erreur qui coûte cher&nbsp;: on attend une carte qu'on "
           + "croit perdue." },
      { txt: "Vous devez aller la chercher au comptoir dans dix jours.",
        rat_t: "La lettre ne vous demande rien.",
        rat: "Rien dans la phrase ne vous donne de tâche&nbsp;: le sujet est «&nbsp;vous&nbsp;», "
           + "mais l'action est celle de recevoir, pas d'aller. Une lettre qui demande quelque "
           + "chose le dit autrement — «&nbsp;veuillez&nbsp;», «&nbsp;vous devez&nbsp;»." },
    ],
    pourquoi: "Le <b>r</b> avant la terminaison est votre repère&nbsp;: la chose est annoncée, "
            + "elle n'est pas faite. Vous n'avez pas eu besoin de connaître le verbe "
            + "<i>recevoir</i> pour le savoir.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le même signe sur les verbes qui changent de forme. ───────────────
  {
    id:   'les-irreguliers',
    type: 'notion',
    eye:  'Les mots qui changent',
    menu: 'Six mots à reconnaître',
    titre: "Certains verbes changent tellement qu'on ne les reconnaît plus. Le « r », lui, reste.",
    paras: [
      "<b>Être</b> donne <i>sera</i>. <b>Avoir</b> donne <i>aura</i>. <b>Aller</b> donne "
      + "<i>ira</i>. <b>Faire</b> donne <i>fera</i>. <b>Venir</b> donne <i>viendra</i>. "
      + "<b>Pouvoir</b> donne <i>pourra</i>. Le mot ne ressemble plus à rien de connu — mais "
      + "le <b>r</b> avant la fin est toujours là.",

      "Ce sont exactement les six que vous lirez le plus&nbsp;: «&nbsp;le bureau <b>sera</b> "
      + "fermé&nbsp;», «&nbsp;la réunion <b>aura</b> lieu&nbsp;», «&nbsp;un employé <b>ira</b> "
      + "vous voir&nbsp;», «&nbsp;nous <b>ferons</b> le suivi&nbsp;», «&nbsp;quelqu'un "
      + "<b>viendra</b> vendredi&nbsp;», «&nbsp;vous <b>pourrez</b> nous rappeler&nbsp;».",

      "Vous n'avez pas à savoir les fabriquer. Vous avez seulement à comprendre, en les lisant, "
      + "que la chose <b>n'est pas encore arrivée</b>. C'est tout ce que le niveau 3 vous "
      + "demande, et c'est déjà ce qui décide si vous manquez un rendez-vous ou non.",
    ],
    retenir: "Six mots courants&nbsp;: <b>sera · aura · ira · fera · viendra · pourra</b>. "
           + "Tous portent le <b>r</b>, et tous parlent de plus tard.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier : maintenant ou plus tard. ──────────────────────────────────
  {
    id:   'tri-quand',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases lues',
    titre: "Six phrases lues quelque part. Elles parlent de quand ?",
    consigne: "Un seul mot change d'une paire à l'autre. Regardez la fin du verbe.",
    colonnes: [
      { id: 'now',   t: 'Maintenant',  b: 'Maintenant' },
      { id: 'plus',  t: 'Plus tard',   b: 'Plus tard' },
    ],
    items: [
      { txt: "Le bureau est fermé.", sous: "affiché sur la porte", ok: 'now',
        rat: "«&nbsp;Est&nbsp;» n'a pas de <b>r</b> avant la fin. La porte est fermée "
           + "aujourd'hui&nbsp;: vous repartez.",
        pourquoi: "Est : aujourd'hui. Vous repartez." },
      { txt: "Le bureau sera fermé du 24 au 27.", sous: "affiché sur la même porte", ok: 'plus',
        rat: "Se<b>r</b>a&nbsp;: la fermeture est annoncée, elle n'a pas commencé. Aujourd'hui, "
           + "vous pouvez entrer.",
        pourquoi: "Sera : c'est annoncé, pas commencé." },
      { txt: "Il y a une réunion des parents.", sous: "dans un courriel", ok: 'now',
        rat: "«&nbsp;Il y a&nbsp;» ne dit rien de plus tard. Sans date, cette phrase parle de "
           + "ce qui existe.",
        pourquoi: "Il y a : ce qui existe." },
      { txt: "Il y aura une réunion des parents le 3 mai.", sous: "dans le même courriel", ok: 'plus',
        rat: "Au<b>r</b>a&nbsp;: la réunion est à venir, et la date le confirme. C'est une "
           + "convocation.",
        pourquoi: "Aura : à venir. C'est une convocation." },
      { txt: "On commence à huit heures.", sous: "dit par un contremaître", ok: 'now',
        rat: "C'est l'horaire habituel, la règle du chantier. Aucun <b>r</b>, aucune forme "
           + "d'<i>aller</i>&nbsp;: rien n'annonce un changement.",
        pourquoi: "L'horaire habituel, tous les jours." },
      { txt: "On va commencer à huit heures demain.", sous: "dit par le même contremaître", ok: 'plus',
        rat: "«&nbsp;Va commencer&nbsp;»&nbsp;: deux mots, avec une forme d'<i>aller</i>. C'est "
           + "l'autre façon de dire plus tard — celle qu'on emploie en parlant.",
        pourquoi: "Va commencer : plus tard, à l'oral." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qui arrive quand on se trompe d'endroit. ───────────────────────
  {
    id:   'lavis',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un avis à corriger',
    titre: "Vous affichez un avis dans l'entrée de votre immeuble. Lequel écrivez-vous ?",
    consigne: "L'eau sera coupée mardi entre 9 h et midi. Trois façons de l'écrire&nbsp;; une "
            + "seule a l'air d'un avis.",
    options: [
      { txt: "« L'eau sera coupée mardi, de 9 h à midi. »", juste: true },
      { txt: "« L'eau va être coupée mardi, de 9 h à midi. »",
        rat_t: "Rien de faux. Mais ça ne ressemble pas à un avis.",
        rat: "La phrase est correcte et tout le monde la comprend&nbsp;: c'est exactement ce "
           + "que vous <b>diriez</b> à un voisin dans l'escalier. Affichée sur un mur, elle "
           + "sonne comme une note prise à la hâte. L'écrit d'annonce emploie l'autre forme." },
      { txt: "« L'eau est coupée mardi, de 9 h à midi. »",
        rat_t: "Celle-là inquiète tout le monde.",
        rat: "Au présent, on lit que l'eau est coupée <i>en ce moment</i> — et la date qui suit "
           + "rend la phrase confuse. C'est la faute qui fait descendre trois voisins vérifier "
           + "leur robinet." },
    ],
    pourquoi: "«&nbsp;L'eau <b>sera</b> coupée.&nbsp;» Un seul mot, un <b>r</b> avant la fin&nbsp;: "
            + "c'est la forme que tout le monde s'attend à lire sur un mur.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier. ────────────────────────────────
  {
    id:   'par-defaut',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Ce que vous dites',
    titre: "Quand vous parlez, vous n'avez rien à choisir.",
    paras: [
      "On a gardé ceci pour la fin, et c'est volontaire&nbsp;: dans une conversation, il n'y a "
      + "<b>rien à décider</b>. «&nbsp;Je vais&nbsp;» plus le verbe, et c'est réglé — au "
      + "téléphone, au comptoir, à la maison, avec un ami comme avec un patron. Personne ne "
      + "vous trouvera négligent.",

      "Vous n'avez donc qu'<b>une seule chose</b> à surveiller&nbsp;: le moment où vous "
      + "<b>écrivez à un bureau</b> — une école, un propriétaire, un employeur, un service. Là, "
      + "l'autre forme fait sérieux, et c'est celle qu'on attend de vous.",

      "Et si vous ne savez pas la fabriquer&nbsp;? Écrivez au futur proche&nbsp;: on vous "
      + "comprendra parfaitement. Le contresens grave n'est pas de mal écrire, c'est de "
      + "<b>mal lire</b> une lettre qui annonce quelque chose.",
    ],
    retenir: "À l'oral&nbsp;: <b>je vais…</b>, sans réfléchir. À l'écrit à un bureau&nbsp;: "
           + "l'autre forme. Et surtout, savoir la <b>reconnaître</b> quand on vous écrit.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Choisir la forme dans un message entier. ──────────────────────────
  {
    id:   'le-courriel',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre courriel',
    titre: "Vous écrivez à l'école au sujet de l'absence de votre fille. Quelle version ?",
    consigne: "Trois messages qui disent la même chose. Un seul est à sa place dans un "
            + "courriel à une secrétaire.",
    options: [
      { txt: "« Bonjour, ma fille sera absente vendredi. Elle reprendra ses cours lundi. »",
        juste: true },
      { txt: "« Bonjour, ma fille va être absente vendredi. Elle va reprendre ses cours lundi. »",
        rat_t: "Vous vous êtes fait comprendre. Vous n'avez pas écrit comme on écrit.",
        rat: "Rien n'est faux, et une secrétaire ne vous reprendra pas. Mais vous venez de "
           + "poser à l'écrit ce que vous auriez dit au téléphone — deux fois. Dans un "
           + "courriel à un bureau, la forme en un seul mot est celle qu'on attend." },
      { txt: "« Bonjour, ma fille est absente vendredi. Elle reprendra ses cours lundi. »",
        rat_t: "La seconde phrase est bonne. C'est la première qui recule.",
        rat: "«&nbsp;Reprendra&nbsp;» est exactement ce qu'il faut. Mais «&nbsp;est "
           + "absente&nbsp;» dit aujourd'hui, alors que l'absence est vendredi&nbsp;: la "
           + "secrétaire peut la noter au mauvais jour." },
    ],
    pourquoi: "«&nbsp;<b>Sera</b> absente&nbsp;», «&nbsp;<b>reprendra</b>&nbsp;». Deux mots à un "
            + "seul mot, tous les deux avec leur <b>r</b>. <b>C'est tout le point en deux "
            + "lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1, écrit cette fois. ─────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient à la clinique du début. Cette fois, vous écrivez.",
    consigne: "La clinique ne répond pas au téléphone. Vous laissez un message dans son "
            + "formulaire en ligne pour annuler jeudi et reprendre plus tard. Quelle "
            + "phrase&nbsp;?",
    options: [
      { txt: "« Je ne pourrai pas venir jeudi. Je rappellerai pour un autre rendez-vous. »",
        juste: true },
      { txt: "« Je vais pas pouvoir venir jeudi. Je vais rappeler pour un autre rendez-vous. »",
        rat_t: "C'est la phrase de l'écran 1 — mais elle n'est plus au bon endroit.",
        rat: "Au téléphone, c'était la bonne réponse et ça le reste. Dans un formulaire écrit "
           + "à une clinique, elle sonne parlée — et le «&nbsp;je vais pas&nbsp;», sans "
           + "«&nbsp;ne&nbsp;», appartient à l'oral seulement." },
      { txt: "« Je ne peux pas venir jeudi. Je rappellerai pour un autre rendez-vous. »",
        rat_t: "La seconde phrase est parfaite. La première parle d'aujourd'hui.",
        rat: "Vous avez le plus difficile&nbsp;: «&nbsp;rappelle<b>r</b>ai&nbsp;», un seul mot, "
           + "le <b>r</b> à sa place. Mais «&nbsp;je ne peux pas&nbsp;» dit maintenant&nbsp;; "
           + "l'empêchement, lui, est jeudi. C'est la faute qui reste quand les autres sont "
           + "réglées." },
    ],
    pourquoi: "«&nbsp;Je ne <b>pourrai</b> pas&nbsp;», «&nbsp;je <b>rappellerai</b>&nbsp;». Vous "
            + "avez reconnu l'endroit, puis la forme&nbsp;: c'est exactement l'ordre dans lequel "
            + "on décide.",
    attente: "Choisissez une réponse pour finir.",
  },

];
