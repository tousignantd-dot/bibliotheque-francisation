// ═══════════════════════════════════════════════════════════════════════════
// Parcours de remédiation — L'heure et la date au Québec
//
// Une ORDONNANCE, pas un cours : l'enseignant l'envoie à un élève chez qui il a
// vu la lacune. Dix minutes, dix écrans, un savoir.
//
// ── Ce qui le sépare d'une mini-leçon, et qui n'est pas négociable ─────────
// Six modules portent déjà une mini-leçon sur l'heure (n1-classe, n2-autobus,
// n3-loisirs, n3-recherche-emploi, n5-quebec, n5-transport). Un élève envoyé
// ici en a très probablement déjà lu deux. Le parcours ne les répète pas :
//
//   1. INDUCTIF. Aucune règle n'est énoncée avant que l'élève ait tranché des
//      cas. La mini-leçon fait l'inverse — « la règle tient en une phrase »,
//      puis des tableaux de formes.
//   2. PARTIEL. Jamais la table des vingt-quatre heures. Les quatre moments
//      qu'on donne vraiment au téléphone, et rien d'autre.
//   3. PAR L'ENJEU, pas par la forme. On ne classe pas des heures : on rate ou
//      on ne rate pas un rendez-vous. Chaque écran a une conséquence.
//   4. AUCUNE PHRASE REPRISE d'une mini-leçon. Les exemples sont ceux de
//      l'appel de Rachid, entendus, jamais lus dans un tableau.
//   5. LE MÉTALANGAGE ARRIVE APRÈS l'avoir manipulé, ou pas du tout.
//
// Extraits : ceux du module `module-n5-rendezvous`, rejoués par chemin absolu.
// Aucun média neuf. Les rangs sont ceux de `dialogues.js`, clé `t1`.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'heure-et-date',
  module:   'module-n5-rendezvous',   // d'où viennent les extraits, rien de plus
  titre:    "L'heure et la date au Québec",
  surtitre: "Parcours · 10 minutes",
  niveau:   5,
  savoir:   'lexique · repère culturel',
};

const ECRANS = [

  // ── 1. On tranche AVANT de savoir. ───────────────────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Seize heures',
    titre: "Vous finissez de travailler à seize heures. On vous propose « quatorze heures dix ». Vous pouvez y aller ?",
    consigne: "Répondez avec ce que vous savez déjà. On expliquera après — c'est fait exprès.",
    options: [
      { txt: "Oui, c'est après mon travail.",
        rat_t: "Quatorze heures, c'est avant seize heures.",
        rat: "Le nombre est plus petit&nbsp;: <b>14</b> vient avant <b>16</b>. C'est aussi simple que ça, "
           + "et c'est tout ce que la journée de vingt-quatre heures demande — comparer deux nombres." },
      { txt: "Non, je travaille encore.", juste: true },
      { txt: "Ça dépend du jour.",
        rat_t: "Le jour ne change pas l'heure.",
        rat: "Quatorze heures dix, c'est quatorze heures dix le lundi comme le jeudi. "
           + "La seule question est&nbsp;: est-ce avant ou après seize heures&nbsp;?" },
    ],
    pourquoi: "Quatorze heures dix arrive <b>deux heures avant</b> la fin de votre journée. "
            + "Vous ne pouvez pas y être.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. La règle, formulée à partir de ce qu'il vient de faire. ───────────
  {
    id:   'apres-midi',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: "Après midi, on continue",
    titre: "Vous n'avez pas converti. Vous avez comparé deux nombres.",
    paras: [
      "C'est toute la différence. On vous a peut-être appris à traduire «&nbsp;quatorze heures&nbsp;» "
      + "en «&nbsp;deux heures de l'après-midi&nbsp;». Au téléphone, vous n'avez pas le temps&nbsp;: "
      + "l'agente dit un nombre, vous le comparez au vôtre.",

      "<b>Après midi, on ne recommence pas à un&nbsp;: on continue.</b> Treize, quatorze, quinze… "
      + "jusqu'à vingt-trois. Vous finissez à seize&nbsp;? Tout ce qui est plus petit que seize est "
      + "hors de portée. Vous n'avez rien d'autre à calculer.",
    ],
    retenir: "Ne traduisez pas. <b>Comparez.</b> Votre heure de fin est un nombre&nbsp;; "
           + "celle qu'on vous propose en est un autre.",
    attente: "Lisez, puis continuez.",
  },

  // ── 3. Trier : on tranche encore, sur des cas, sans table de conversion. ─
  {
    id:   'tri-portee',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six propositions',
    titre: "Vous finissez à seize heures. Lesquelles pouvez-vous prendre ?",
    consigne: "Six moments, six décisions. Rien à convertir&nbsp;: comparez au seize.",
    colonnes: [
      { id: 'oui', t: 'Je peux', b: 'Je peux' },
      { id: 'non', t: 'Je ne peux pas', b: 'Je ne peux pas' },
    ],
    items: [
      { txt: "Dix-sept heures", ok: 'oui',
        rat: "Dix-sept est plus grand que seize&nbsp;: c'est une heure après la fin de votre journée.",
        pourquoi: "Une heure après votre travail." },
      { txt: "Onze heures trente", ok: 'non',
        rat: "Onze heures trente, c'est le matin — vous êtes au travail depuis longtemps.",
        pourquoi: "Le matin. Trop tôt." },
      { txt: "Dix-huit heures quinze", ok: 'oui',
        rat: "Dix-huit est plus grand que seize. C'est le début de la soirée.",
        pourquoi: "Début de soirée." },
      { txt: "Quinze heures quarante-cinq", ok: 'non',
        rat: "Quinze, c'est plus petit que seize — et quarante-cinq minutes n'y changent rien&nbsp;: "
           + "il vous manque encore un quart d'heure de travail.",
        pourquoi: "Quinze minutes trop tôt. Le piège." },
      { txt: "Seize heures", ok: 'non', sous: "l'heure exacte où vous finissez",
        rat: "Vous <i>finissez</i> à seize heures&nbsp;: vous êtes encore à l'école, pas à la clinique. "
           + "Il faut aussi le temps de vous y rendre.",
        pourquoi: "On ne peut pas être à deux endroits." },
      { txt: "Vingt heures", ok: 'oui', sous: "la clinique ferme à vingt et une heures",
        rat: "Vingt est plus grand que seize. Le soir est possible quand la clinique est ouverte.",
        pourquoi: "Le soir, si c'est ouvert." },
    ],
    attente: "Tranchez les six cas pour continuer.",
  },

  // ── 4. Ce que les gens disent vraiment, à la place d'un nombre. ──────────
  {
    id:   'fin-de-journee',
    type: 'notion',
    eye:  'Ce qu'
        + "'on vous dira à la place",
    menu: "« En fin de journée »",
    titre: "La moitié du temps, on ne vous donnera pas de nombre.",
    paras: [
      "Une agente administrative parle vite et emploie des mots flous&nbsp;: <b>en avant-midi</b>, "
      + "<b>sur l'heure du dîner</b>, <b>en fin de journée</b>, <b>en début de soirée</b>. "
      + "Ces mots ont un sens précis, et personne ne vous le dit.",

      "Écoutez celui-ci. Le nombre exact arrive <i>après</i> le mot flou — c'est presque toujours "
      + "l'ordre&nbsp;: le mot d'abord, l'heure ensuite.",
    ],
    sons: [
      { fichier: 't1/line_13_manon.mp3', qui: 'Manon, agente administrative',
        texte: "J'ai le mardi 17 juin à quatorze heures dix, ou le jeudi 19 en fin de journée, "
             + "à dix-sept heures." },
    ],
    retenir: "«&nbsp;En fin de journée&nbsp;» annonce l'heure&nbsp;: elle vient juste après. "
           + "<b>Attendez le nombre, ne devinez pas.</b>",
    attente: "Écoutez l'extrait, puis continuez.",
  },

  // ── 5. Le tri des mots flous. ────────────────────────────────────────────
  {
    id:   'tri-moments',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Les mots du temps',
    titre: "Chacun de ces mots couvre un moment. Lequel ?",
    consigne: "Ce sont les quatre qu'on entend au téléphone. Pas les autres — il n'y en a pas d'autres.",
    colonnes: [
      { id: 'am', t: 'Avant midi', b: 'Avant midi' },
      { id: 'pm', t: 'Après midi', b: 'Après midi' },
      { id: 'soir', t: 'Le soir', b: 'Le soir' },
    ],
    items: [
      { txt: "En avant-midi", ok: 'am', sous: "« Je vous mets en avant-midi. »",
        rat: "Le mot le dit&nbsp;: <b>avant</b> midi. Entre l'ouverture et midi.",
        pourquoi: "De l'ouverture à midi." },
      { txt: "Sur l'heure du dîner", ok: 'pm', sous: "au Québec, le dîner est le repas du midi",
        rat: "Attention&nbsp;: au Québec, le <b>dîner</b> est le repas du <b>midi</b>, et le repas du "
           + "soir s'appelle le <b>souper</b>. «&nbsp;Sur l'heure du dîner&nbsp;» veut donc dire "
           + "autour de midi — pas le soir.",
        pourquoi: "Autour de midi — le dîner, ici, c'est le midi." },
      { txt: "En fin de journée", ok: 'pm', sous: "vers seize ou dix-sept heures",
        rat: "C'est la fin des heures de bureau, pas la nuit&nbsp;: seize, dix-sept heures. "
           + "La journée de travail finit, pas la journée.",
        pourquoi: "Seize, dix-sept heures. La fin du bureau." },
      { txt: "En début de soirée", ok: 'soir', sous: "dix-huit, dix-neuf heures",
        rat: "Après le souper&nbsp;: dix-huit, dix-neuf heures. C'est le créneau des cliniques "
           + "ouvertes le soir.",
        pourquoi: "Dix-huit, dix-neuf heures." },
    ],
    attente: "Rangez les quatre moments pour continuer.",
  },

  // ── 6. La date : le jour tout seul. ──────────────────────────────────────
  {
    id:   'le-19',
    type: 'notion',
    eye:  'La date',
    menu: "« Le 19 »",
    titre: "On vous donnera un chiffre seul. Il faut savoir de quel mois.",
    paras: [
      "«&nbsp;Le jeudi 19&nbsp;», dit l'agente — sans le mois. Ce n'est pas de la négligence&nbsp;: "
      + "au téléphone, on donne <b>le jour de la semaine et le quantième</b>, et le mois est celui "
      + "où l'on est. Si c'est un autre mois, on le dit.",

      "L'ordre québécois est presque toujours&nbsp;: <b>le jour de la semaine, puis le nombre, "
      + "puis le mois s'il le faut, puis l'heure.</b> Jeudi 19 juin, dix-sept heures. "
      + "Retenez l'ordre plutôt que les mots&nbsp;: c'est lui qui vous dit ce qui s'en vient.",
    ],
    sons: [
      { fichier: 't1/line_15_manon.mp3', qui: 'Manon confirme le rendez-vous',
        texte: "Jeudi 19 juin, dix-sept heures, avec la docteure Fongang. "
             + "Présentez-vous quinze minutes avant, à l'accueil." },
    ],
    retenir: "Jour · nombre · mois · heure. <b>Dans cet ordre</b>, et l'heure vient toujours en dernier.",
    attente: "Écoutez, puis continuez.",
  },

  // ── 7. La conséquence : arriver quinze minutes avant. ────────────────────
  {
    id:   'quinze-avant',
    type: 'verif',
    eye:  'Vérification',
    menu: 'À quelle heure partir',
    titre: "Rendez-vous à dix-sept heures. On vous demande d'arriver quinze minutes avant. Vous vous présentez à quelle heure ?",
    consigne: "Réécoutez la phrase de l'écran précédent si vous voulez&nbsp;: elle contient les deux informations.",
    sons: [
      { fichier: 't1/line_22_rachid.mp3', qui: 'Rachid reformule, à la fin de l\'appel',
        texte: "Vingt-quatre heures. Alors jeudi 19 juin, dix-sept heures, arriver à seize heures "
             + "quarante-cinq. C'est bien ça&nbsp;?" },
    ],
    options: [
      { txt: "Seize heures quarante-cinq.", juste: true },
      { txt: "Dix-sept heures quinze.",
        rat_t: "C'est quinze minutes <i>après</i>, pas avant.",
        rat: "Dix-sept heures quinze, c'est le quart passé — vous arriveriez en retard de quinze "
           + "minutes à un rendez-vous où l'on vous attendait un quart d'heure plus tôt. "
           + "Un demi-heure d'écart en tout." },
      { txt: "Seize heures quinze.",
        rat_t: "Vous avez retiré une heure de trop.",
        rat: "Quinze minutes avant dix-sept heures, c'est <b>seize heures quarante-cinq</b>&nbsp;: "
           + "on recule d'un quart d'heure, pas d'une heure et quart." },
    ],
    pourquoi: "Quinze minutes avant dix-sept heures&nbsp;: <b>seize heures quarante-cinq</b>. "
            + "Rachid le redit à voix haute avant de raccrocher — c'est exactement ce qu'il faut faire.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le délai : une durée, pas un moment. ──────────────────────────────
  {
    id:   'delai',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Vingt-quatre heures',
    titre: "« Appelez-nous au moins vingt-quatre heures à l'avance. » Votre rendez-vous est jeudi à dix-sept heures.",
    consigne: "Jusqu'à quand pouvez-vous annuler sans payer&nbsp;?",
    sons: [
      { fichier: 't1/line_21_manon.mp3', qui: 'Manon',
        texte: "Vous nous appelez au moins vingt-quatre heures à l'avance. Après ce délai, "
             + "la clinique facture des frais d'absence." },
    ],
    options: [
      { txt: "Jusqu'à mercredi, dix-sept heures.", juste: true },
      { txt: "Jusqu'à jeudi matin.",
        rat_t: "Jeudi matin, il ne reste plus vingt-quatre heures.",
        rat: "Entre jeudi matin et jeudi dix-sept heures, il y a une demi-journée, pas une journée. "
           + "Vingt-quatre heures avant jeudi dix-sept heures, c'est <b>mercredi</b> dix-sept heures." },
      { txt: "Jusqu'à mercredi soir.",
        rat_t: "Presque — mais «&nbsp;le soir&nbsp;» n'est pas une heure.",
        rat: "Un délai se compte d'heure à heure, pas de moment à moment. Vingt-quatre heures avant "
           + "dix-sept heures, c'est dix-sept heures la veille. Mercredi vingt heures serait déjà "
           + "trop tard." },
    ],
    pourquoi: "Un délai est une <b>durée</b>, pas un moment&nbsp;: on la retire de l'heure du "
            + "rendez-vous. Vingt-quatre heures avant jeudi dix-sept heures&nbsp;: mercredi, "
            + "dix-sept heures.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 9. Ce qu'on fait quand on n'a pas compris. ───────────────────────────
  {
    id:   'faire-repeter',
    type: 'notion',
    eye:  'La phrase à garder',
    menu: 'Faire répéter',
    titre: "Vous n'avez pas saisi l'heure. Ne raccrochez pas là-dessus.",
    paras: [
      "C'est le vrai risque, et il n'a rien de grammatical&nbsp;: on n'ose pas faire répéter, "
      + "on dit «&nbsp;oui, oui&nbsp;», et on note quelque chose de faux.",

      "La sortie tient en une phrase, et elle est polie&nbsp;: "
      + "<b>«&nbsp;Je répète pour être sûr&nbsp;: jeudi 19, dix-sept heures. C'est bien ça&nbsp;?&nbsp;»</b> "
      + "Vous ne demandez pas de répéter — vous <i>reformulez</i>, et l'autre corrige si c'est faux. "
      + "Personne ne se vexe de ça&nbsp;; les agentes le font entre elles.",
    ],
    retenir: "Redites l'heure à voix haute avant de raccrocher. <b>Toujours.</b> "
           + "C'est ce qui rattrape tout le reste.",
    attente: "Lisez, puis continuez.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "Dernier appel. « Je peux vous prendre mercredi en fin de journée, à seize heures trente. »",
    consigne: "Vous finissez toujours à seize heures, et il vous faut vingt minutes pour vous y rendre. "
            + "Vous dites quoi&nbsp;?",
    options: [
      { txt: "« C'est trop juste. Auriez-vous quelque chose après dix-sept heures ? »", juste: true },
      { txt: "« Parfait, je serai là. »",
        rat_t: "Vous arriveriez à seize heures vingt… pour seize heures trente.",
        rat: "En apparence ça passe&nbsp;: vous finissez à seize, vous arrivez à seize heures vingt. "
           + "Mais on vous demande d'être là <b>quinze minutes avant</b>, donc à seize heures quinze. "
           + "Vous seriez en retard avant même de partir." },
      { txt: "« Le mercredi, je ne peux jamais. »",
        rat_t: "Ce n'est pas le jour qui coince, c'est l'heure.",
        rat: "Vous fermez une porte qui était ouverte&nbsp;: mercredi à dix-huit heures vous "
           + "conviendrait très bien. Dites ce qui ne va pas — l'heure — et l'agente cherchera autre "
           + "chose le même jour." },
    ],
    pourquoi: "Seize heures trente, moins quinze minutes d'avance, c'est être à l'accueil à seize "
            + "heures quinze — quinze minutes après la fin de votre travail, plus vingt minutes de "
            + "route. <b>Dire ce qui coince, et proposer autre chose</b>&nbsp;: c'est ça, mener un appel.",
    attente: "Choisissez une réponse pour finir.",
  },

];
