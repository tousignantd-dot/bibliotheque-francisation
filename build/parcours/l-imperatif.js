// ═══════════════════════════════════════════════════════════════════════════
// Point express — Se faire comprendre quand on dit quoi faire
//
// Savoir n3-s31 (Impératif présent) : « employer les terminaisons appropriées
// à la 2e personne ». Une ORDONNANCE : l'enseignant l'envoie à un élève qui
// écrit « Vous prenez deux comprimés » sur une note, ou « Prendre à droite »
// dans un message à une personne.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Sept mini-leçons du dépôt traitent l'impératif : « L'impératif : la forme
// qui commande », « … dire quoi faire sans commander », « … la langue des
// répondeurs », « … le mode de l'urgence », « Impératif ou infinitif »,
// « Donner une directive : l'impératif avec pronom », « Donnez-moi ».
// Toutes commencent par le TABLEAU DES TROIS PERSONNES (tu / nous / vous) et
// descendent ensuite vers les emplois. Un élève qui les a lues connaît le
// tableau et écrit quand même « Vous signez ici » sur un mot laissé à une
// collègue.
//
// Ce point-ci ne montre aucun tableau. Il donne UN SEUL GESTE — enlever le
// sujet — qui fabrique la forme sur un verbe jamais vu, et il fait d'abord
// RECONNAÎTRE une consigne dans huit phrases de la vraie vie. Les cinq écarts :
//
//   1. INDUCTIF. Écran 2 : huit phrases prises à des affiches, des lettres et
//      des messages, à ranger en « on me demande de faire » / « on me
//      décrit ». Aucune règle avant l'écran 3.
//   2. UN GESTE, PAS UNE LISTE. « Vous signez » → on retire « vous », il
//      reste « Signez ». Le geste marche sur un verbe qu'on n'a jamais
//      conjugué ; une liste de terminaisons s'oublie.
//   3. LA POLITESSE EST DITE EN DERNIER (écran 8). La placer d'entrée ferait
//      croire que l'impératif est brutal et qu'il faut l'éviter — c'est ce que
//      croient les élèves qui écrivent « Vous signez ici ».
//   4. LE MÉTALANGAGE ARRIVE APRÈS. Le mot « impératif » n'est écrit qu'à
//      l'écran 3, une fois la chose triée huit fois.
//   5. EXEMPLES VARIÉS : une affiche de stationnement, une lettre du CLSC, un
//      mot laissé à une gardienne, un cours de secourisme, un texto à son fils.
//
// Aucun média : la différence entre « vous signez » et « signez » s'entend
// parfaitement. Ce qui manque à l'élève, c'est de la produire.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'l-imperatif',
  titre:    "Se faire comprendre quand on dit quoi faire",
  surtitre: "Point express · 10 minutes",
  niveau:   3,
  savoir:   'n3-s31',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le mot sur la table',
    titre: "Vous laissez un mot à la personne qui garde votre fils ce soir.",
    consigne: "Le sirop se donne à huit heures. Répondez avec ce que vous savez déjà — ou au "
            + "feeling. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Donnez-lui le sirop à huit heures.&nbsp;»", juste: true },
      { txt: "«&nbsp;Vous donnez le sirop à huit heures.&nbsp;»",
        rat_t: "C'est la phrase la plus écrite par les élèves, et c'est celle-ci qu'on corrige.",
        rat: "Elle se comprend. Mais telle qu'elle est écrite, elle <b>décrit</b> ce que la "
           + "personne fait, comme si vous racontiez sa soirée. Sur un papier laissé sur la "
           + "table, on attend une demande, pas un récit — et la personne peut hésiter&nbsp;: "
           + "est-ce que je dois le faire, ou est-ce déjà prévu&nbsp;?" },
      { txt: "«&nbsp;Donner le sirop à huit heures.&nbsp;»",
        rat_t: "C'est la langue des étiquettes, pas celle d'un mot à quelqu'un.",
        rat: "Cette forme existe et elle est correcte — sur une boîte de médicament, dans un "
           + "mode d'emploi, une recette. Elle s'adresse à n'importe qui. Ici vous écrivez à "
           + "<b>une personne</b> que vous connaissez&nbsp;: lui parler comme à une étiquette "
           + "se remarque." },
    ],
    pourquoi: "«&nbsp;Donnez-lui…&nbsp;» Gardez la phrase en tête&nbsp;: on y revient au "
            + "dernier écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases lues cette semaine. Laquelle vous demande de faire quelque chose ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Fiez-vous à ce que vous feriez en "
            + "lisant la phrase&nbsp;: est-ce que vous vous levez, ou est-ce que vous "
            + "hochez la tête&nbsp;?",
    colonnes: [
      { id: 'faire',  t: "On me demande de faire", b: "On me demande" },
      { id: 'decrit', t: "On me décrit quelque chose", b: "On me décrit" },
    ],
    items: [
      { txt: "Composez le 9-1-1.", sous: "une affiche dans un couloir", ok: 'faire',
        rat: "L'affiche ne raconte rien&nbsp;: elle vous met le téléphone dans la main. Rien "
           + "devant le verbe, et le verbe arrive tout seul.",
        pourquoi: "Le verbe est seul en tête : on vous demande d'agir." },
      { txt: "Vous composez le 9-1-1 et vous restez en ligne.", sous: "une personne qui raconte sa soirée", ok: 'decrit',
        rat: "Le «&nbsp;vous&nbsp;» est écrit devant le verbe&nbsp;: quelqu'un dit ce qui s'est "
           + "passé, ou ce qui se passe d'habitude. Personne ne compose rien en lisant ça.",
        pourquoi: "« Vous » devant le verbe : c'est un récit." },
      { txt: "Apportez votre carte d'assurance maladie.", sous: "une lettre de rendez-vous", ok: 'faire',
        rat: "Le rendez-vous ne tiendra pas sans la carte. La lettre ne décrit pas votre "
           + "prochaine visite&nbsp;: elle vous dit quoi mettre dans votre poche.",
        pourquoi: "Le verbe seul en tête, et une chose à faire." },
      { txt: "Le stationnement est interdit devant l'entrée.", sous: "un avis dans un immeuble", ok: 'decrit',
        rat: "Celui-là trompe, parce qu'il a bien un effet sur vous&nbsp;: vous ne vous "
           + "stationnerez pas là. Mais la phrase, elle, <b>décrit un état</b> — elle dit ce "
           + "qui est interdit, elle ne s'adresse à personne.",
        pourquoi: "Elle décrit une règle, elle ne parle à personne." },
      { txt: "Ne stationnez pas devant l'entrée.", sous: "un carton sur une porte de garage", ok: 'faire',
        rat: "Même interdiction que la phrase précédente, mais dite <b>à vous</b>. Rien devant "
           + "le verbe, sinon la négation.",
        pourquoi: "Même règle, mais adressée à quelqu'un." },
      { txt: "Nous attendons votre réponse avant vendredi.", sous: "un courriel d'un employeur", ok: 'decrit',
        rat: "Il y a une attente, et même une échéance — mais l'employeur parle de "
           + "<b>lui</b>&nbsp;: «&nbsp;nous attendons&nbsp;». Il n'a pas écrit "
           + "«&nbsp;répondez avant vendredi&nbsp;».",
        pourquoi: "L'employeur parle de lui, pas de vous." },
      { txt: "Prends ta clé, je pars plus tôt.", sous: "un texto à son fils", ok: 'faire',
        rat: "Le verbe est seul devant, et la personne à qui on écrit doit faire un geste "
           + "avant de sortir.",
        pourquoi: "Un geste à faire, et le verbe seul en tête." },
      { txt: "Tu prends toujours ta clé, c'est bien.", sous: "un mot laissé sur le comptoir", ok: 'decrit',
        rat: "Le même verbe, la même personne — mais le «&nbsp;tu&nbsp;» est là, et le sens "
           + "bascule&nbsp;: on félicite une habitude au lieu de demander un geste.",
        pourquoi: "« Tu » devant le verbe : on décrit une habitude." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-geste',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le geste',
    titre: "Vous n'avez pas regardé le verbe. Vous avez regardé ce qu'il y avait devant.",
    paras: [
      "Dans votre colonne «&nbsp;on me demande de faire&nbsp;», il n'y a <b>rien</b> devant le "
      + "verbe. Dans l'autre, il y a un «&nbsp;vous&nbsp;», un «&nbsp;tu&nbsp;», un "
      + "«&nbsp;nous&nbsp;». C'est la seule différence, et elle suffit.",

      "<b>Le geste, sur n'importe quel verbe&nbsp;:</b> dites la phrase avec le sujet — "
      + "«&nbsp;vous signez ici&nbsp;» — puis <b>retirez le sujet</b>. Il reste "
      + "«&nbsp;Signez ici&nbsp;», et c'est la consigne. «&nbsp;Tu attends dehors&nbsp;» → "
      + "«&nbsp;Attends dehors&nbsp;». Ça marche sur un verbe que vous n'avez jamais conjugué.",

      "Cette forme s'appelle l'<b>impératif</b>. Un seul piège d'écriture, et il ne concerne "
      + "que le «&nbsp;tu&nbsp;» des verbes en <i>-er</i>&nbsp;: le «&nbsp;s&nbsp;» tombe. "
      + "«&nbsp;Tu ferme<b>s</b> la porte&nbsp;» → «&nbsp;<b>Ferme</b> la porte&nbsp;». Avec "
      + "«&nbsp;vous&nbsp;», rien ne change jamais.",
    ],
    retenir: "Dites la phrase avec le sujet, puis <b>retirez le sujet</b>. Ce qui reste est la "
           + "consigne.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : le petit mot qui reste collé au verbe. ─────────
  {
    id:   'le-pronom',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Le mot qui suit',
    titre: "Un cours de secourisme. L'instructrice écrit la consigne au tableau.",
    consigne: "La phrase de départ est «&nbsp;<i>vous vous approchez du blessé</i>&nbsp;». "
            + "Retirez le sujet — mais il y a deux «&nbsp;vous&nbsp;».",
    options: [
      { txt: "«&nbsp;Approchez-vous du blessé.&nbsp;»", juste: true },
      { txt: "«&nbsp;Vous approchez du blessé.&nbsp;»",
        rat_t: "Vous avez retiré le mauvais des deux.",
        rat: "Vous avez enlevé le second «&nbsp;vous&nbsp;» et gardé le premier, alors que "
           + "c'est le premier qui est le sujet. Le second appartient au verbe — "
           + "«&nbsp;s'approcher&nbsp;» ne va nulle part sans lui." },
      { txt: "«&nbsp;Approchez du blessé.&nbsp;»",
        rat_t: "Le sujet est bien parti — et sa moitié du verbe avec.",
        rat: "Vous avez retiré les deux «&nbsp;vous&nbsp;», mais l'un d'eux fait partie du "
           + "verbe&nbsp;: on dit «&nbsp;<i>s'</i>approcher&nbsp;», comme "
           + "«&nbsp;<i>s'</i>asseoir&nbsp;» ou «&nbsp;<i>se</i> lever&nbsp;». Il reste, et il "
           + "passe <b>derrière</b>, avec un trait d'union." },
    ],
    pourquoi: "Le sujet part, le petit mot du verbe reste — et il saute derrière&nbsp;: "
            + "«&nbsp;Asseyez-<b>vous</b>&nbsp;», «&nbsp;Lève-<b>toi</b>&nbsp;», "
            + "«&nbsp;Dépêchez-<b>vous</b>&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. La négation : tout revient devant. ────────────────────────────────
  {
    id:   'la-negation',
    type: 'notion',
    eye:  'Quand on dit de ne pas faire',
    menu: 'Ne … pas',
    titre: "Dès qu'on dit « ne … pas », le petit mot revient devant le verbe.",
    paras: [
      "C'est le seul endroit où la consigne change de forme. Comparez, sur le même verbe&nbsp;: "
      + "«&nbsp;<i>Asseyez-<b>vous</b>.</i>&nbsp;» mais «&nbsp;<i>Ne <b>vous</b> asseyez "
      + "pas là.</i>&nbsp;» Le trait d'union disparaît avec.",

      "Même chose pour «&nbsp;y&nbsp;» et «&nbsp;en&nbsp;»&nbsp;: «&nbsp;<i>Prenez-en "
      + "deux.</i>&nbsp;» mais «&nbsp;<i>N'en prenez pas plus de deux.</i>&nbsp;» Vous "
      + "n'avez rien de nouveau à apprendre&nbsp;: la négation remet simplement les choses "
      + "dans l'ordre habituel de la phrase.",

      "À l'oral, le «&nbsp;ne&nbsp;» tombe presque toujours — «&nbsp;<i>vous asseyez pas "
      + "là</i>&nbsp;», «&nbsp;<i>touche pas à ça</i>&nbsp;». C'est normal et personne ne vous "
      + "reprendra. Mais <b>à l'écrit, on l'écrit</b>, surtout sur une affiche ou dans une "
      + "note à un supérieur.",
    ],
    retenir: "Consigne affirmative&nbsp;: le petit mot passe derrière, avec un trait d'union. "
           + "Consigne négative&nbsp;: il revient devant, sans trait d'union.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six consignes écrites. Lesquelles tiennent ?",
    consigne: "Deux choses à regarder&nbsp;: le sujet est-il bien parti, et le petit mot du "
            + "verbe est-il du bon côté&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Signez au bas de la page et remettez-moi le formulaire.", ok: 'ok',
        rat: "Deux consignes de suite, sujet retiré dans les deux, et le petit mot derrière "
           + "avec son trait d'union. Rien à corriger.",
        pourquoi: "Deux consignes justes, à la suite." },
      { txt: "Vous attendez dans la salle, je vous appelle.", ok: 'faux',
        rat: "Le «&nbsp;vous&nbsp;» est resté devant le verbe&nbsp;: la phrase décrit au lieu "
           + "de demander. Sur un mot laissé au comptoir, l'usager ne sait pas s'il doit "
           + "s'asseoir. Il faut «&nbsp;Attendez dans la salle&nbsp;».",
        pourquoi: "Le sujet est resté : il faut « Attendez »." },
      { txt: "Ne vous inquiétez pas, je rappelle demain.", ok: 'ok',
        rat: "Une consigne négative&nbsp;: le petit mot est revenu devant le verbe et le trait "
           + "d'union a disparu. C'est exactement la règle de l'écran précédent.",
        pourquoi: "Négation : le petit mot revient devant." },
      { txt: "Assoyez vous ici, madame.", ok: 'faux',
        rat: "Le sujet est bien parti et le petit mot est du bon côté&nbsp;: il ne manque que "
           + "le trait d'union, qui n'est pas une décoration — c'est lui qui dit que le mot "
           + "appartient au verbe. «&nbsp;Assoyez-vous ici&nbsp;».",
        pourquoi: "Il manque le trait d'union : Assoyez-vous." },
      { txt: "Fermes la porte en sortant.", ok: 'faux',
        rat: "Le sujet est parti, et c'est déjà l'essentiel. Mais «&nbsp;tu ferme<b>s</b>&nbsp;» "
           + "perd son «&nbsp;s&nbsp;» quand on retire le sujet&nbsp;: "
           + "«&nbsp;<b>Ferme</b> la porte&nbsp;». Le piège ne touche que les verbes en "
           + "<i>-er</i>, au tutoiement.",
        pourquoi: "Au « tu », les verbes en -er perdent le s." },
      { txt: "N'oubliez pas votre carte de rendez-vous.", ok: 'ok',
        rat: "Négation complète, sujet retiré, verbe en tête. C'est la phrase qu'on lit sur "
           + "les avis de clinique, et elle est bien construite.",
        pourquoi: "Négation écrite en entier : correct." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Le tutoiement, et la faute qui reste. ─────────────────────────────
  {
    id:   'le-s-du-tu',
    type: 'verif',
    eye: 'Vérification',
    menu: 'Un texto à son fils',
    titre: "Vous écrivez à votre fils de quinze ans. Deux consignes, un seul message.",
    consigne: "Il doit prendre sa clé et fermer la porte. Vous le tutoyez.",
    options: [
      { txt: "«&nbsp;Prends ta clé et ferme la porte.&nbsp;»", juste: true },
      { txt: "«&nbsp;Prend ta clé et fermes la porte.&nbsp;»",
        rat_t: "Les deux «&nbsp;s&nbsp;» ont changé de place.",
        rat: "C'est la faute la plus fréquente, et elle vient d'une bonne intuition&nbsp;: on "
           + "sait qu'un «&nbsp;s&nbsp;» disparaît quelque part, on ne sait plus où. Il ne "
           + "disparaît que sur les verbes en <i>-er</i>&nbsp;: <i>ferme</i>. Les autres le "
           + "gardent&nbsp;: <i>prend<b>s</b></i>, <i>vien<b>s</b></i>, <i>fai<b>s</b></i>." },
      { txt: "«&nbsp;Tu prends ta clé et tu fermes la porte.&nbsp;»",
        rat_t: "Personne ne vous reprendrait — mais ce n'est pas ce que vous vouliez écrire.",
        rat: "Dite au téléphone, cette phrase passe très bien. Écrite dans un texto, elle "
           + "décrit une habitude&nbsp;: votre fils peut la lire comme «&nbsp;tu prends "
           + "toujours ta clé&nbsp;» et ne rien faire de particulier ce soir-là." },
    ],
    pourquoi: "Le «&nbsp;s&nbsp;» ne tombe qu'aux verbes en <i>-er</i>&nbsp;: "
            + "<b>ferme</b>, <b>regarde</b>, <b>écoute</b> — mais <b>prends</b>, "
            + "<b>viens</b>, <b>fais</b>.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La politesse, dite en dernier : c'est ce qui rend la forme utile. ─
  {
    id:   'la-politesse',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Sec ou poli ?',
    titre: "Une consigne n'est pas un ordre, et ce n'est pas la forme qui décide.",
    paras: [
      "On a gardé ceci pour la fin, parce que c'est la crainte qui fait écrire "
      + "«&nbsp;vous signez ici&nbsp;»&nbsp;: la peur d'avoir l'air de commander. Or ce qui "
      + "rend une phrase sèche n'est presque jamais la forme du verbe&nbsp;; c'est ce qu'il y "
      + "a autour.",

      "Trois mots suffisent&nbsp;: «&nbsp;<i>Signez ici, <b>s'il vous plaît</b>.</i>&nbsp;» "
      + "«&nbsp;<i>Rappelez-moi demain, <b>si possible</b>.</i>&nbsp;» "
      + "«&nbsp;<i><b>Merci de</b> laisser la porte fermée.</i>&nbsp;» Le verbe n'a pas changé "
      + "de forme — la phrase a changé de ton.",

      "Et quand la demande est lourde, on sort de la consigne pour poser une "
      + "question&nbsp;: «&nbsp;<i>Pourriez-vous me rappeler demain&nbsp;?</i>&nbsp;» C'est le "
      + "tour qu'on emploie avec un supérieur ou un inconnu. Mais sur une affiche, dans une "
      + "recette, dans un mot à un proche, la consigne nue est <b>ce qu'on attend</b>&nbsp;: "
      + "l'adoucir la rend floue.",
    ],
    retenir: "La forme dit ce qu'il faut faire&nbsp;; les mots autour disent sur quel ton. "
           + "Ne changez pas la forme pour être poli.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-note',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre note',
    titre: "Vous laissez une note à la voisine qui arrose vos plantes.",
    consigne: "Trois choses&nbsp;: arroser deux fois, ne pas ouvrir la fenêtre, se servir du "
            + "café. Une seule version tient d'un bout à l'autre.",
    options: [
      { txt: "«&nbsp;Arrosez deux fois par semaine. N'ouvrez pas la fenêtre du salon. "
           + "Servez-vous du café.&nbsp;»", juste: true },
      { txt: "«&nbsp;Vous arrosez deux fois par semaine. Vous n'ouvrez pas la fenêtre du "
           + "salon. Vous vous servez du café.&nbsp;»",
        rat_t: "Trois phrases, trois sujets restés en place.",
        rat: "Rien n'est mal écrit, et pourtant la note ne demande plus rien&nbsp;: elle "
           + "décrit ce que la voisine ferait. La troisième phrase est la pire — "
           + "«&nbsp;vous vous servez du café&nbsp;» peut se lire comme un reproche." },
      { txt: "«&nbsp;Arrosez deux fois par semaine. Ne ouvrez pas la fenêtre du salon. "
           + "Servez vous du café.&nbsp;»",
        rat_t: "Les trois sujets sont partis. Ce sont deux détails d'écriture qui accrochent.",
        rat: "Devant une voyelle, «&nbsp;ne&nbsp;» perd son «&nbsp;e&nbsp;»&nbsp;: "
           + "«&nbsp;<b>N'</b>ouvrez pas&nbsp;». Et le petit mot du verbe s'attache par un "
           + "trait d'union&nbsp;: «&nbsp;Servez-<b>vous</b>&nbsp;». La forme est bonne, "
           + "l'orthographe suit avec un peu d'attention." },
    ],
    pourquoi: "Sujet retiré partout, négation écrite en entier, trait d'union au petit mot. "
            + "<b>C'est tout le point en trois phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au mot laissé sur la table, pour le sirop de huit heures.",
    consigne: "Cette fois, il faut aussi dire de ne pas le réveiller s'il dort. Vouvoiement, "
            + "note écrite.",
    options: [
      { txt: "«&nbsp;Donnez-lui le sirop à huit heures. Ne le réveillez pas s'il dort.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Donnez-lui le sirop à huit heures. Ne réveillez-le pas s'il dort.&nbsp;»",
        rat_t: "La première phrase est juste. La seconde a gardé le trait d'union de trop.",
        rat: "Dès qu'on dit «&nbsp;ne … pas&nbsp;», le petit mot revient <b>devant</b> le "
           + "verbe et le trait d'union disparaît&nbsp;: «&nbsp;Ne <b>le</b> réveillez "
           + "pas&nbsp;». C'est exactement la bascule de l'écran 5, et c'est la seule que "
           + "l'impératif demande." },
      { txt: "«&nbsp;Vous lui donnez le sirop à huit heures et vous ne le réveillez pas s'il "
           + "dort.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, avec une consigne de plus.",
        rat: "Les deux sujets sont restés. Sur un papier, la personne lira le récit d'une "
           + "soirée au lieu de deux demandes — et c'est justement la nuit où votre fils est "
           + "malade que le doute coûte cher." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: retirer le sujet, placer le petit mot "
            + "derrière à l'affirmative, et le ramener devant à la négative.",
    attente: "Choisissez une réponse pour finir.",
  },

];
