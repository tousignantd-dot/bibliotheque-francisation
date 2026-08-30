// ═══════════════════════════════════════════════════════════════════════════
// Point express — Poser une question : trois façons, et laquelle au téléphone
//
// Savoir n5-s07. Dix minutes, dix écrans.
//
// ── L'écart avec les mini-leçons ───────────────────────────────────────────
//   1. Les mini-leçons enseignent les formes (est-ce que / inversion). Ce
//      point express enseigne le CHOIX : les trois sont justes, elles ne se
//      disent pas aux mêmes personnes. C'est un savoir social, pas grammatical,
//      et rien dans le matériel ne le porte.
//   2. Il traite le « -tu » québécois, que le programme nomme explicitement
//      (n5-s07) et qu'aucun manuel n'explique — l'élève l'entend pourtant
//      dix fois par jour.
//   3. Inductif : on fait classer des questions entendues avant d'avoir donné
//      la moindre forme.
//
// Extraits : les vraies questions du module rendez-vous — celles de Manon au
// téléphone, celles de la médecin, celles de Nadia à la maison. Trois
// registres dans un seul module, ce qui est exactement le sujet. Aucun média
// neuf. Le « -tu » n'a pas d'extrait : il s'enseigne à l'écrit ici, et le
// point le dit à l'élève plutôt que de faire semblant.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'poser-une-question',
  module:   'module-n5-rendezvous',
  titre:    "Poser une question : trois façons",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'n5-s07',
};

const ECRANS = [

  // ── 1. Trois formes, aucune fautive. ─────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois façons',
    titre: "Trois façons de demander la même chose. Laquelle est fautive ?",
    consigne: "«&nbsp;Est-ce que vous avez une place jeudi&nbsp;?&nbsp;» · "
            + "«&nbsp;Avez-vous une place jeudi&nbsp;?&nbsp;» · "
            + "«&nbsp;Vous avez une place jeudi&nbsp;?&nbsp;»",
    options: [
      { txt: "Aucune. Les trois se disent.", juste: true },
      { txt: "La troisième : il manque « est-ce que ».",
        rat_t: "C'est celle qu'on entend le plus.",
        rat: "Sans <i>est-ce que</i> ni inversion, c'est <b>l'intonation</b> qui fait la "
           + "question&nbsp;— la voix monte à la fin. C'est la forme la plus courante à l'oral, "
           + "et la seule qu'on n'apprend jamais en classe." },
      { txt: "La deuxième : on ne dit plus « avez-vous ».",
        rat_t: "On le dit encore, et souvent.",
        rat: "L'inversion est bien vivante — au comptoir, au téléphone, dans un formulaire. "
           + "Elle sonne simplement plus soignée que les deux autres." },
    ],
    pourquoi: "<b>Les trois sont justes.</b> Toute la question est de savoir <i>à qui</i> on "
            + "parle — et c'est ce que personne n'enseigne.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. Écouter trois vraies questions. ───────────────────────────────────
  {
    id:   'trois-voix',
    type: 'notion',
    eye:  'Écoutez',
    menu: 'Trois vraies questions',
    titre: "La même personne n'est pas questionnée de la même façon par tout le monde.",
    paras: [
      "Trois questions, tirées d'un seul appel et d'une seule journée. Écoutez-les l'une après "
      + "l'autre, et remarquez ce qui change&nbsp;: ce n'est pas la politesse, c'est la "
      + "<b>distance</b> entre les deux personnes.",
      "Sa fille lui parle d'une façon. L'agente de la clinique, d'une autre. La médecin, "
      + "d'une troisième.",
    ],
    sons: [
      { fichier: 'prep/line_03_nadia.mp3', qui: 'Nadia, sa fille, à la maison',
        texte: "Ça fait combien de temps que ça t'arrive&nbsp;?" },
      { fichier: 't1/line_05_manon.mp3', qui: "Manon, l'agente, au téléphone",
        texte: "Certainement. Vous êtes inscrit chez elle&nbsp;?" },
      { fichier: 't2/line_03_dre_fongang.mp3', qui: 'La docteure Fongang, en consultation',
        texte: "Quelques secondes. Et ça arrive à quel moment, exactement&nbsp;?" },
    ],
    retenir: "Trois personnes, trois façons. <b>La forme dit la relation</b>, pas le degré de "
           + "politesse.",
    attente: "Écoutez les trois extraits, puis continuez.",
  },

  // ── 3. Trier : à qui on dit quoi. ────────────────────────────────────────
  {
    id:   'tri-registre',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'À qui on le dit',
    titre: "Six questions. À qui les diriez-vous ?",
    consigne: "Toutes sont correctes. Choisissez celle des deux situations où elle passe "
            + "le mieux.",
    colonnes: [
      { id: 'proche',  t: 'À un proche',           b: 'À un proche' },
      { id: 'inconnu', t: 'À un inconnu, au comptoir', b: 'À un inconnu' },
    ],
    items: [
      { txt: "« Tu viens avec moi ? »", ok: 'proche',
        rat: "Le <i>tu</i> tranche tout seul&nbsp;: on ne tutoie pas un préposé qu'on ne connaît "
           + "pas. Au Québec, on se tutoie vite entre collègues, mais rarement à un guichet.",
        pourquoi: "Le « tu » : entre proches." },
      { txt: "« Auriez-vous une place plus tôt ? »", ok: 'inconnu',
        rat: "L'inversion <i>plus</i> le conditionnel <i>auriez</i>&nbsp;: c'est la forme la plus "
           + "soignée des six. Entre proches, elle sonnerait cérémonieuse, presque ironique.",
        pourquoi: "Inversion et conditionnel : le plus soigné." },
      { txt: "« Vous avez fini à quelle heure ? »", ok: 'proche',
        rat: "Le <i>vous</i> est poli, mais la construction est celle de l'oral courant — le mot "
           + "interrogatif est rejeté à la fin. Ça passe entre collègues&nbsp;; au comptoir, "
           + "c'est un peu direct.",
        pourquoi: "Poli, mais très oral. Entre collègues." },
      { txt: "« Est-ce que je peux avoir un reçu ? »", ok: 'inconnu',
        rat: "<i>Est-ce que</i> est la forme neutre&nbsp;: elle ne choque nulle part et convient "
           + "partout. C'est celle à employer <b>quand on hésite</b>.",
        pourquoi: "Neutre. Passe partout — la valeur sûre." },
      { txt: "« Ça te dérange-tu ? »", ok: 'proche',
        rat: "Le <i>-tu</i> québécois. On l'entend partout entre proches et entre collègues, "
           + "jamais dans un écrit ni dans une demande officielle.",
        pourquoi: "Le « -tu » d'ici : à l'oral, entre proches." },
      { txt: "« Pourriez-vous répéter, s'il vous plaît ? »", ok: 'inconnu',
        rat: "C'est <b>la</b> phrase du comptoir et du téléphone — celle qu'il faut savoir dire "
           + "sans y penser quand on n'a pas compris.",
        pourquoi: "La phrase à savoir par cœur au téléphone." },
    ],
    attente: "Rangez les six questions pour continuer.",
  },

  // ── 4. La règle, tirée du tri. ───────────────────────────────────────────
  {
    id:   'la-regle',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Ce qui décide',
    titre: "Vous n'avez pas trié des formes. Vous avez trié des relations.",
    paras: [
      "Les trois façons se rangent sur une seule échelle, du plus courant au plus soigné&nbsp;:",
      "<b>1. L'intonation seule</b> — «&nbsp;Vous avez une place jeudi&nbsp;?&nbsp;» La voix "
      + "monte à la fin, et c'est tout. Entre proches, entre collègues.<br>"
      + "<b>2. «&nbsp;Est-ce que&nbsp;»</b> — «&nbsp;Est-ce que vous avez une place&nbsp;?&nbsp;» "
      + "Neutre. Passe partout, à l'oral comme à l'écrit. <b>Employez celle-là quand vous "
      + "hésitez.</b><br>"
      + "<b>3. L'inversion</b> — «&nbsp;Avez-vous une place&nbsp;?&nbsp;» Soignée. Au comptoir, "
      + "au téléphone, dans une lettre.",
      "Ce qui décide n'est pas le respect — les trois sont respectueuses — mais la "
      + "<b>distance</b>. Trop soigné avec un ami sonne froid&nbsp;; trop courant avec un "
      + "inconnu sonne brusque.",
    ],
    retenir: "Dans le doute, <b>«&nbsp;est-ce que&nbsp;»</b>. Elle ne détonne jamais nulle part.",
    attente: "Lisez, puis continuez.",
  },

  // ── 5. Le « -tu » québécois, que personne n'explique. ────────────────────
  {
    id:   'le-tu',
    type: 'notion',
    eye:  "Ce qu'on entend ici",
    menu: 'Le « -tu » d\'ici',
    titre: "« Ça marche-tu, ton affaire ? » — ce petit « tu » n'est pas un tutoiement.",
    paras: [
      "Vous l'entendrez dix fois par jour, et aucun manuel ne vous le dira&nbsp;: au Québec, on "
      + "ajoute souvent <b>-tu</b> après le verbe pour poser une question. "
      + "«&nbsp;Ça marche-tu&nbsp;?&nbsp;» «&nbsp;Il est-tu arrivé&nbsp;?&nbsp;» "
      + "«&nbsp;Vous en voulez-tu&nbsp;?&nbsp;»",
      "Le piège est là&nbsp;: ce <b>-tu</b> ne s'adresse à personne. Ce n'est pas le pronom "
      + "«&nbsp;tu&nbsp;». On peut très bien dire «&nbsp;<b>vous</b> en voulez-<b>tu</b>&nbsp;» "
      + "— vouvoyer et employer <i>-tu</i> dans la même phrase, sans aucune contradiction.",
      "Le programme du niveau 5 le nomme explicitement. On ne vous demande pas de le "
      + "produire&nbsp;: on vous demande de <b>le reconnaître</b> pour ne pas croire qu'on vous "
      + "tutoie, ni chercher un mot qui manque.",
    ],
    retenir: "<b>Le «&nbsp;-tu&nbsp;» d'ici pose la question&nbsp;; il ne désigne personne.</b> "
           + "À comprendre, pas à écrire.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Vérification sur le -tu. ──────────────────────────────────────────
  {
    id:   'verif-tu',
    type: 'verif',
    eye:  'Vérification',
    menu: 'On vous tutoie ?',
    titre: "Au comptoir de la pharmacie : « Vous l'avez-tu, votre carte ? » On vous tutoie ?",
    consigne: "Répondez d'après ce que vous venez de lire.",
    options: [
      { txt: "Non. Le « vous » vouvoie ; le « -tu » pose la question.", juste: true },
      { txt: "Oui, et c'est impoli.",
        rat_t: "Le <i>vous</i> est pourtant là, juste avant.",
        rat: "Si la personne vous tutoyait, elle dirait «&nbsp;tu l'as-tu&nbsp;?&nbsp;». Elle dit "
           + "<b>vous</b>&nbsp;: elle vous vouvoie. Le <i>-tu</i> qui suit le verbe ne s'adresse "
           + "à personne, c'est une marque de question." },
      { txt: "C'est une faute de français.",
        rat_t: "C'est du français d'ici, et le programme le nomme.",
        rat: "Ce n'est pas de la langue soignée — on ne l'écrit pas dans une lettre — mais c'est "
           + "une construction régulière du français québécois parlé, que le programme du "
           + "niveau 5 demande de <b>reconnaître</b>. La juger ne vous aide pas à comprendre." },
    ],
    pourquoi: "Deux choses différentes dans la même phrase&nbsp;: <b>vous</b> désigne la "
            + "personne, <b>-tu</b> pose la question. Les entendre séparément, c'est cesser de "
            + "trébucher dessus.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 7. Le mot interrogatif, et où il se met. ─────────────────────────────
  {
    id:   'ou-se-met',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Où se met le mot',
    titre: "Où se met le mot qui pose la question — quand, où, combien, comment ?",
    consigne: "Les deux places existent. Dites laquelle sonne <b>soignée</b> et laquelle sonne "
            + "<b>courante</b>.",
    colonnes: [
      { id: 'soigne',  t: 'Soigné',  b: 'Soigné' },
      { id: 'courant', t: 'Courant', b: 'Courant' },
    ],
    items: [
      { txt: "« Quand est-ce que vous fermez ? »", ok: 'soigne',
        rat: "Le mot interrogatif est <b>en tête</b>, suivi de <i>est-ce que</i>&nbsp;: c'est la "
           + "construction complète, celle qu'on écrit.",
        pourquoi: "Le mot en tête : la forme complète." },
      { txt: "« Vous fermez quand ? »", ok: 'courant',
        rat: "Le mot est <b>rejeté à la fin</b>. Très fréquent à l'oral, jamais à l'écrit — et "
           + "c'est souvent la seule forme que l'élève entend, d'où sa surprise en lisant "
           + "l'autre.",
        pourquoi: "Le mot à la fin : l'oral courant." },
      { txt: "« Combien de temps ça dure ? »", ok: 'courant',
        rat: "Le mot est en tête, mais sans <i>est-ce que</i> ni inversion. C'est la forme "
           + "intermédiaire, très employée à l'oral&nbsp;: on la comprend partout, on ne "
           + "l'écrit pas dans une lettre.",
        pourquoi: "En tête, mais rien après : de l'oral." },
      { txt: "« Où dois-je me présenter ? »", ok: 'soigne',
        rat: "Mot en tête <i>plus</i> inversion&nbsp;: la forme la plus soignée des quatre. "
           + "C'est celle d'un formulaire ou d'un courriel.",
        pourquoi: "Mot en tête + inversion : le plus soigné." },
    ],
    attente: "Rangez les quatre questions pour continuer.",
  },

  // ── 8. La question qu'on n'ose pas poser. ────────────────────────────────
  {
    id:   'faire-repeter',
    type: 'notion',
    eye:  'La plus utile de toutes',
    menu: 'Faire répéter',
    titre: "La question la plus utile n'est pas dans les manuels : « Pouvez-vous répéter ? »",
    paras: [
      "Au téléphone, la difficulté n'est presque jamais de <i>poser</i> une question. C'est "
      + "d'oser en poser une <b>deuxième</b> quand on n'a pas compris la réponse.",
      "Trois formules, de la plus courte à la plus sûre&nbsp;: "
      + "«&nbsp;<b>Pardon&nbsp;?</b>&nbsp;» · «&nbsp;<b>Pouvez-vous répéter, s'il vous "
      + "plaît&nbsp;?</b>&nbsp;» · «&nbsp;<b>Je répète pour être sûr&nbsp;: jeudi 19, dix-sept "
      + "heures. C'est bien ça&nbsp;?</b>&nbsp;»",
      "La troisième est la meilleure, et c'est celle qu'on emploie le moins&nbsp;: vous ne "
      + "demandez pas de répéter, vous <b>reformulez</b>. L'autre corrige si c'est faux, et "
      + "personne n'a l'air d'avoir mal compris.",
    ],
    sons: [
      { fichier: 't1/line_22_rachid.mp3', qui: 'Rachid, avant de raccrocher',
        texte: "Vingt-quatre heures. Alors jeudi 19 juin, dix-sept heures, arriver à seize "
             + "heures quarante-cinq. C'est bien ça&nbsp;?" },
    ],
    retenir: "«&nbsp;<b>C'est bien ça&nbsp;?</b>&nbsp;» — trois mots qui rattrapent tout un "
           + "appel mal entendu.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 9. Écrire une question. ──────────────────────────────────────────────
  {
    id:   'ecrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Écrire à la clinique',
    titre: "Vous écrivez un courriel à la clinique. Quelle question écrivez-vous ?",
    consigne: "C'est un <b>écrit</b>, à quelqu'un que vous ne connaissez pas.",
    options: [
      { txt: "« Est-ce que je dois apporter ma carte d'assurance maladie ? »", juste: true },
      { txt: "« Je dois-tu apporter ma carte ? »",
        rat_t: "Le «&nbsp;-tu&nbsp;» ne s'écrit pas.",
        rat: "Il s'entend partout et ne s'écrit nulle part — sauf pour transcrire une parole. "
           + "Dans un courriel à une clinique, il ferait le même effet qu'une phrase relâchée "
           + "dans une lettre officielle." },
      { txt: "« J'apporte ma carte ? »",
        rat_t: "Trop court pour un écrit.",
        rat: "L'intonation fait la question à l'oral&nbsp;; à l'écrit, il ne reste que le point "
           + "d'interrogation, et la phrase paraît sèche. Ajoutez <i>est-ce que</i>&nbsp;: deux "
           + "mots, et le ton change." },
    ],
    pourquoi: "À l'écrit, à un inconnu&nbsp;: <b>«&nbsp;est-ce que&nbsp;»</b> ou l'inversion. "
            + "L'intonation ne s'écrit pas, et le «&nbsp;-tu&nbsp;» encore moins.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. Fermeture. ───────────────────────────────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "Vous téléphonez à la clinique et vous ne savez pas à qui vous parlez.",
    consigne: "Première question de l'appel. Vous employez laquelle&nbsp;?",
    options: [
      { txt: "« Est-ce que vous avez une place cette semaine ? »", juste: true },
      { txt: "« Vous avez une place cette semaine ? »",
        rat_t: "Ça se dit — mais c'est un pari.",
        rat: "L'intonation seule passe très bien avec quelqu'un qu'on connaît. Au premier mot "
           + "d'un appel à un inconnu, elle peut sonner brusque, et vous n'avez aucun moyen de "
           + "le savoir&nbsp;: vous ne voyez pas le visage en face." },
      { txt: "« Auriez-vous par hasard une place cette semaine ? »",
        rat_t: "Trop, et ça se remarque aussi.",
        rat: "Le conditionnel plus «&nbsp;par hasard&nbsp;»&nbsp;: on s'excuse d'appeler. C'est "
           + "juste, mais ça vous met en position basse dès la première phrase, et ce n'est pas "
           + "la meilleure façon d'obtenir un rendez-vous." },
    ],
    pourquoi: "<b>«&nbsp;Est-ce que&nbsp;» est la valeur sûre&nbsp;:</b> ni trop familière, ni "
            + "trop cérémonieuse. Gardez l'inversion pour l'écrit, et l'intonation pour les gens "
            + "que vous connaissez.",
    attente: "Choisissez une réponse pour finir.",
  },

];
