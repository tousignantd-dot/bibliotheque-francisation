// ═══════════════════════════════════════════════════════════════════════════
// Point express — Les nombres au téléphone
//
// Lexique et repère culturel. Dix minutes, dix écrans.
//
// ── Pourquoi celui-ci, et ce qui le distingue ──────────────────────────────
// C'est le seul point express qui ne porte sur aucune règle : il porte sur
// une PANNE. L'élève connaît ses chiffres — il les a appris au niveau 1 — et
// il rate quand même un numéro de carte dicté à vitesse normale, sans visage,
// sans possibilité de faire répéter trois fois. Ce n'est pas un savoir qui
// manque, c'est un automatisme.
//
// Conséquence sur la forme : ici, tout se corrige par comparaison de chaînes.
// Aucun jugement, aucune IA — le parcours entier fonctionne dans un centre en
// mode sans assistant.
//
// Les trois pièges traités sont ceux du Québec, et aucune mini-leçon ne les
// porte : soixante-dix / quatre-vingt-dix dits en bloc, les nombres groupés
// par deux dans un numéro de téléphone, et la lettre-chiffre d'une carte
// d'assurance maladie.
//
// Extraits : module-n5-rendezvous. Aucun média neuf.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'nombres-au-telephone',
  module:   'module-n5-rendezvous',
  titre:    "Les nombres au téléphone",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'lexique · repère culturel',
};

const ECRANS = [

  // ── 1. La panne, montrée avant d'être expliquée. ─────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Le numéro de carte',
    titre: "Rachid donne son numéro de carte. Écoutez, et dites combien de chiffres vous avez saisis.",
    consigne: "Une seule écoute avant de répondre, comme au téléphone. Vous pourrez réécouter "
            + "après.",
    sons: [
      { fichier: 't1/line_08_rachid.mp3', qui: 'Rachid, à l\'agente',
        texte: "BENR soixante-quatorze onze zéro quatre douze." },
    ],
    options: [
      { txt: "Huit chiffres, précédés de quatre lettres.", juste: true },
      { txt: "Quatre nombres : 74, 11, 04, 12.",
        rat_t: "Vous avez entendu juste — et c'est exactement le piège.",
        rat: "Il a bien dit quatre <i>nombres</i>&nbsp;: soixante-quatorze, onze, zéro quatre, "
           + "douze. Mais un numéro de carte se <b>écrit en chiffres</b>&nbsp;: 74 11 04 12, "
           + "donc <b>huit</b> chiffres. Entendre des nombres et écrire des chiffres, c'est la "
           + "conversion qu'il faut faire en une seconde." },
      { txt: "Je n'ai pas eu le temps de compter.",
        rat_t: "C'est la réponse la plus honnête, et c'est pour ça qu'on est ici.",
        rat: "Personne ne compte les chiffres en écoutant. Ce qu'on fait, c'est <b>écrire au fur "
           + "et à mesure</b>, deux par deux, sans attendre la fin — et c'est ce que ce point "
           + "va vous faire pratiquer." },
    ],
    pourquoi: "Quatre lettres, puis <b>huit chiffres groupés deux par deux</b>. Le format est "
            + "toujours le même&nbsp;: c'est ce qui vous permet de savoir, avant même d'écouter, "
            + "combien de cases vous avez à remplir.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. Le format connu d'avance. ─────────────────────────────────────────
  {
    id:   'les-formats',
    type: 'notion',
    eye:  'Ce qu\'il faut savoir avant d\'écouter',
    menu: 'Les quatre formats',
    titre: "On ne retient pas un numéro. On remplit un format qu'on connaît déjà.",
    paras: [
      "C'est la seule technique qui marche, et elle n'a rien à voir avec la mémoire&nbsp;: "
      + "<b>avant</b> d'écouter, vous savez combien de cases vous avez à remplir. Il n'y a que "
      + "quatre formats au Québec.",
      "<b>Téléphone</b> — 10 chiffres&nbsp;: 3 + 3 + 4. <i>(514) 555-0134.</i><br>"
      + "<b>Carte d'assurance maladie</b> — 4 lettres + 8 chiffres, par deux.<br>"
      + "<b>Code postal</b> — lettre chiffre lettre, espace, chiffre lettre chiffre. "
      + "<i>H2X 1Y4.</i><br>"
      + "<b>Adresse</b> — le numéro civique se dit souvent par blocs&nbsp;: 3120 se dit "
      + "«&nbsp;trente et un vingt&nbsp;».",
      "Tracez vos cases sur le papier <b>avant</b> l'appel. Vous n'écoutez plus un nombre&nbsp;: "
      + "vous cochez des cases.",
    ],
    retenir: "Un numéro se <b>reçoit</b> dans un format, il ne se retient pas. "
           + "Dix cases pour un téléphone, huit pour une carte.",
    attente: "Lisez, puis continuez.",
  },

  // ── 3. Trier : combien de cases. ─────────────────────────────────────────
  {
    id:   'tri-cases',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Combien de cases',
    titre: "Vous allez recevoir ces informations. Combien de cases tracez-vous ?",
    consigne: "Sans écouter quoi que ce soit&nbsp;: le format se sait d'avance.",
    colonnes: [
      { id: 'six',  t: '6',  b: '6 cases' },
      { id: 'huit', t: '8',  b: '8 cases' },
      { id: 'dix',  t: '10', b: '10 cases' },
    ],
    items: [
      { txt: "Un numéro de téléphone", ok: 'dix',
        rat: "Indicatif régional (3) + 3 + 4 = <b>dix</b>. Au Québec, on donne toujours "
           + "l'indicatif, même pour un appel local.",
        pourquoi: "3 + 3 + 4 = dix chiffres." },
      { txt: "Un numéro de carte d'assurance maladie", ok: 'huit',
        rat: "Quatre lettres, puis <b>huit</b> chiffres groupés deux par deux. Les lettres "
           + "viennent de votre nom&nbsp;: elles sont plus faciles à vérifier que les chiffres.",
        pourquoi: "Huit chiffres, après les quatre lettres." },
      { txt: "Un code postal", ok: 'six',
        rat: "<b>Six</b> caractères en tout, en alternance lettre-chiffre-lettre / "
           + "chiffre-lettre-chiffre. Aucun autre format ne mélange ainsi.",
        pourquoi: "Six caractères, en alternance." },
      { txt: "Un numéro de dossier à la clinique", ok: 'huit',
        rat: "Le plus souvent <b>huit</b> chiffres, comme la carte — mais celui-là, il faut "
           + "<b>le demander</b>&nbsp;: « c'est combien de chiffres ? » est une question tout à "
           + "fait normale, et elle vous évite de recommencer.",
        pourquoi: "Huit le plus souvent — mais demandez." },
    ],
    attente: "Tranchez les quatre formats pour continuer.",
  },

  // ── 4. Le piège d'ici : 70 et 90. ────────────────────────────────────────
  {
    id:   'soixante-dix',
    type: 'notion',
    eye:  'Le piège du français',
    menu: '70, 80, 90',
    titre: "« Soixante-quatorze » ne commence pas par soixante.",
    paras: [
      "C'est le piège qui coûte le plus de numéros ratés, et il n'a rien à voir avec votre "
      + "niveau&nbsp;: entre <b>soixante</b> et <b>quatre-vingts</b>, le français compte "
      + "<i>soixante-dix, soixante et onze, soixante-douze…</i> — et quand vous entendez "
      + "«&nbsp;soixante&nbsp;», il vous reste une demi-seconde pour savoir si le nombre est "
      + "60 ou 74.",
      "La parade est de <b>ne rien écrire avant la fin du mot</b>. Un chiffre écrit trop tôt "
      + "est un chiffre à raturer&nbsp;— et pendant qu'on rature, on perd le suivant.",
      "Réécoutez Rachid&nbsp;: son numéro commence justement par soixante-quatorze.",
    ],
    sons: [
      { fichier: 't1/line_08_rachid.mp3', qui: 'Rachid',
        texte: "BENR soixante-quatorze onze zéro quatre douze." },
    ],
    retenir: "<b>60 ou 74&nbsp;? 80 ou 97&nbsp;?</b> Attendez la fin du mot avant d'écrire. "
           + "Toujours.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 5. Vérification sur 70/90. ───────────────────────────────────────────
  {
    id:   'verif-70-90',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Quatre-vingt-dix-sept',
    titre: "L'agente dit : « quatre-vingt-dix-sept ». Vous écrivez quoi ?",
    consigne: "Comptez avant de répondre, sans deviner.",
    options: [
      { txt: "97", juste: true },
      { txt: "80-10-7, donc trois cases.",
        rat_t: "Trois mots, mais <b>un seul</b> nombre.",
        rat: "Le français fabrique 97 avec trois mots — quatre-vingt, dix, sept — mais ça reste "
           + "<b>deux chiffres</b>&nbsp;: 9 et 7. C'est exactement là que les cases dérapent&nbsp;: "
           + "on écrit un chiffre par mot entendu, et le numéro se retrouve trop long." },
      { txt: "4-20-17",
        rat_t: "Vous avez traduit les mots un par un.",
        rat: "«&nbsp;Quatre-vingt&nbsp;» n'est pas 4 et 20&nbsp;: c'est <b>80</b>, d'un bloc. "
           + "Le français dit 80 en deux mots pour des raisons anciennes&nbsp;; il faut "
           + "l'apprendre comme un bloc, jamais le calculer." },
    ],
    pourquoi: "<b>Un nombre, deux chiffres</b>, quel que soit le nombre de mots pour le dire. "
            + "Comptez les <i>chiffres</i> à écrire, jamais les mots entendus.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 6. Épeler et faire épeler. ───────────────────────────────────────────
  {
    id:   'epeler',
    type: 'notion',
    eye:  'Les lettres',
    menu: 'Épeler au téléphone',
    titre: "Six lettres se confondent au téléphone. La parade tient en trois mots.",
    paras: [
      "Sans visage et sans lèvres, ces paires deviennent presque identiques&nbsp;: "
      + "<b>E et I</b>, <b>G et J</b>, <b>M et N</b>. Elles suffisent à faire écrire un nom de "
      + "travers, et personne ne s'en aperçoit avant le rendez-vous.",
      "La parade est de <b>donner un mot</b> après la lettre&nbsp;: «&nbsp;M comme "
      + "Montréal&nbsp;», «&nbsp;E comme école&nbsp;». Ce n'est ni long ni prétentieux&nbsp;: "
      + "les agentes le font entre elles toute la journée.",
      "Écoutez Rachid épeler son nom, et remarquez qu'il le fait <b>sans qu'on le lui "
      + "demande</b> — il n'attend pas qu'on se trompe.",
    ],
    sons: [
      { fichier: 't1/line_06_rachid.mp3', qui: 'Rachid s\'identifie',
        texte: "Oui. Rachid Benali, B, E, N, A, L, I." },
    ],
    retenir: "Épelez <b>avant</b> qu'on vous le demande, et donnez un mot pour E, I, G, J, M, N.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 7. Trier : quelles lettres demandent un mot. ─────────────────────────
  {
    id:   'tri-lettres',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Lesquelles se confondent',
    titre: "Sur lesquelles faut-il donner un mot ?",
    consigne: "Dites-les à voix basse, deux fois, comme si vous ne voyiez pas la personne.",
    colonnes: [
      { id: 'oui', t: 'Un mot est utile', b: 'Un mot' },
      { id: 'non', t: 'Elle passe seule', b: 'Elle passe' },
    ],
    items: [
      { txt: "M et N", ok: 'oui',
        rat: "Les deux se disent «&nbsp;èmm&nbsp;» et «&nbsp;ènn&nbsp;»&nbsp;: une seule "
           + "consonne les sépare, et le téléphone la mange. La paire la plus coûteuse des trois.",
        pourquoi: "M comme Montréal, N comme Nicolas." },
      { txt: "E et I", ok: 'oui',
        rat: "«&nbsp;Euh&nbsp;» et «&nbsp;i&nbsp;»&nbsp;: distinctes à l'oreille en face, "
           + "beaucoup moins dans un combiné — surtout dites vite, au milieu d'un nom.",
        pourquoi: "E comme école, I comme Isabelle." },
      { txt: "B et P", ok: 'non',
        rat: "Elles se ressemblent dans plusieurs langues, mais en français leurs noms de "
           + "lettres sont assez différents — «&nbsp;bé&nbsp;» et «&nbsp;pé&nbsp;» — pour "
           + "passer. Donner un mot ne nuit jamais, mais ce n'est pas la priorité.",
        pourquoi: "Assez distinctes en français." },
      { txt: "G et J", ok: 'oui',
        rat: "«&nbsp;Jé&nbsp;» et «&nbsp;ji&nbsp;»&nbsp;: c'est la paire qui piège aussi les "
           + "personnes qui viennent de l'anglais, où les deux lettres sont inversées par "
           + "rapport au français.",
        pourquoi: "G comme Gaspé, J comme Julie." },
      { txt: "O et Zéro", ok: 'oui',
        rat: "Ce ne sont même pas deux lettres&nbsp;: l'une est une lettre, l'autre un chiffre. "
           + "Dans un code postal ou un numéro de dossier, l'erreur est fréquente et invisible "
           + "à la relecture.",
        pourquoi: "Dites « la lettre O » ou « le chiffre zéro »." },
    ],
    attente: "Tranchez les cinq paires pour continuer.",
  },

  // ── 8. Le montant. ───────────────────────────────────────────────────────
  {
    id:   'montants',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Un montant',
    titre: "« Ça vous fera quarante-deux et cinquante. » Vous payez combien ?",
    consigne: "C'est la façon la plus courante de dire un prix ici — et elle n'est écrite "
            + "nulle part.",
    options: [
      { txt: "42,50 $", juste: true },
      { txt: "42 $ et 50 $, donc 92 $.",
        rat_t: "Le «&nbsp;et&nbsp;» ne veut pas dire «&nbsp;plus&nbsp;».",
        rat: "Il sépare les dollars des cents&nbsp;: c'est la virgule, dite à voix haute. "
           + "«&nbsp;Quarante-deux et cinquante&nbsp;» est la forme courte de "
           + "«&nbsp;quarante-deux dollars et cinquante cents&nbsp;»." },
      { txt: "4 250 $",
        rat_t: "Vous avez collé les deux nombres.",
        rat: "Un montant en dollars ne se lit pas comme un numéro. Le repère qui sauve&nbsp;: "
           + "le second nombre d'un prix est <b>toujours inférieur à cent</b> — ce sont des "
           + "cents." },
    ],
    pourquoi: "«&nbsp;<b>Et</b>&nbsp;» est la virgule. Quarante-deux dollars, cinquante cents.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Reformuler : la seule vérification qui marche. ────────────────────
  {
    id:   'reformuler',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Vérifier sans vexer',
    titre: "Vous avez noté un numéro et vous n'êtes pas sûr. Vous dites quoi ?",
    consigne: "L'agente est pressée, et vous ne voulez pas la faire répéter trois fois.",
    options: [
      { txt: "« Je relis pour être sûr : cinq un quatre, cinq cinq cinq, zéro un trois quatre. »",
        juste: true },
      { txt: "« Pouvez-vous répéter, s'il vous plaît ? »",
        rat_t: "Ça marche — une fois.",
        rat: "C'est juste et poli, mais on repart de zéro&nbsp;: vous réécoutez dix chiffres au "
           + "lieu de vérifier ceux que vous avez. Et si vous ratez le même, il faudra le "
           + "demander une troisième fois." },
      { txt: "« Oui, oui, c'est bon. »",
        rat_t: "C'est la phrase qui coûte le rendez-vous.",
        rat: "Personne ne saura que le numéro est faux — ni vous, ni elle — jusqu'au jour où le "
           + "rappel n'arrivera pas. Le silence coûte toujours plus cher que la question." },
    ],
    pourquoi: "<b>Relire chiffre par chiffre</b> vaut mieux que faire répéter&nbsp;: l'autre "
            + "n'a plus qu'à corriger un chiffre, et vous gardez le reste. C'est exactement ce "
            + "que Rachid fait avec sa date de rendez-vous.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. Fermeture. ───────────────────────────────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On vous dit : « Rappelez au quatre-cent-cinquante, deux-vingt-neuf, zéro-huit-quatorze. »",
    consigne: "Combien de cases avez-vous à remplir, et quel est le premier bloc&nbsp;?",
    options: [
      { txt: "Dix cases, et le premier bloc est 450 — l'indicatif régional.", juste: true },
      { txt: "Neuf cases : je compte trois blocs de trois.",
        rat_t: "Le dernier bloc en a quatre.",
        rat: "Un numéro nord-américain fait toujours 3 + 3 + <b>4</b>. Si vous n'avez que neuf "
           + "cases remplies, c'est qu'il vous manque un chiffre — et c'est un signal fiable "
           + "pour redemander tout de suite." },
      { txt: "Je ne peux pas savoir avant d'avoir tout entendu.",
        rat_t: "Justement si, et c'est tout l'intérêt.",
        rat: "«&nbsp;Rappelez au…&nbsp;» annonce un <b>numéro de téléphone</b>&nbsp;: dix cases, "
           + "toujours. Vous les tracez avant qu'elle ait fini sa phrase, et vous n'avez plus "
           + "qu'à les remplir." },
    ],
    pourquoi: "<b>450 · 229 · 0814.</b> Le format se sait d'avance, les chiffres arrivent après. "
            + "C'est ce qui transforme une écoute impossible en une écoute ordinaire.",
    attente: "Choisissez une réponse pour finir.",
  },

];
