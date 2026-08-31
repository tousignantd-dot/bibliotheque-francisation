// ═══════════════════════════════════════════════════════════════════════════
// Point express — Deux choses en même temps, sans deux phrases
//
// Savoir n6-s12 (Phrases subordonnées participiales). Une ORDONNANCE :
// l'enseignant l'envoie à un élève dont la production montre qu'il empile les
// petites phrases, ou qu'il écrit « en » + -ant sans voir qui fait l'action.
// Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Huit modules portent une mini-leçon sur le gérondif, toutes au niveau 5 et
// toutes bâties pareil — la forme d'abord, un emploi ensuite :
//   · `module-n5-rendezvous` — « Le gérondif : « en me levant », la réponse à
//     « à quel moment ? » » : le gérondif y sert à dater une action.
//   · `module-n5-transport` — « Le gérondif : dire par où et comment ».
//   · `module-n5-saisons`, `-degat`, `-logement`, `-oeuvres`, `-quebec`,
//     `module-n8-habitation` — « en marchant », « en visitant », « en
//     rentrant » : chacune donne un emploi, aucune ne les met en concurrence.
// Un élève qui les a lues sait fabriquer la forme et croit qu'elle veut dire
// « pendant que ». Il écrit alors « En ouvrant la porte, le chat est sorti » —
// et personne ne lui a jamais dit que le chat n'ouvre pas les portes. Les cinq
// écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases en deux emplois AVANT qu'on lui
//      dise qu'il y en a deux. La règle de l'écran 3 est écrite comme un
//      constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau de conjugaison en tête. Un
//      TEST unique — qui fait l'action du mot en -ant ? — qui marche sur une
//      phrase jamais vue, et qui est précisément ce que les huit mini-leçons
//      ne posent pas.
//   3. LA FORME SE DIT EN DERNIER (écran 8), alors que c'est par elle que
//      commencent toutes les mini-leçons. La fabriquer d'entrée fait croire
//      que la difficulté est là ; elle est dans le sujet.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Gérondif » n'est écrit qu'à l'écran 3,
//      une fois la chose triée huit fois.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un courriel à un employeur,
//      une note à l'école, un texto, une consigne d'atelier, une affiche de
//      pharmacie. L'élève doit reconnaître la faute partout.
//
// Aucun média : la faute du sujet ne s'entend pas — « en ouvrant la porte, le
// chat est sorti » se dit très bien. Elle n'apparaît qu'à l'écrit, et c'est le
// sujet même du point.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'en-faisant',
  titre:    "Deux choses en même temps, sans deux phrases",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s12',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Une phrase',
    titre: "« Elle a trouvé un emploi en apprenant le français. » Que dit cette phrase ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "Apprendre le français lui a servi à trouver l'emploi.", juste: true },
      { txt: "Elle a appris le français après avoir trouvé l'emploi.",
        rat_t: "L'ordre n'est pas ce que ce mot indique.",
        rat: "Vous avez lu «&nbsp;en apprenant&nbsp;» comme un moment placé après. Or ce mot ne "
           + "range jamais deux actions l'une après l'autre&nbsp;: il les colle. Pour dire "
           + "«&nbsp;après&nbsp;», il faudrait écrire «&nbsp;<i>après avoir trouvé un emploi, elle "
           + "a appris le français</i>&nbsp;» — et ce n'est pas la même histoire." },
      { txt: "Deux choses sans rapport, arrivées la même année.",
        rat_t: "Le lien est justement ce que la phrase ajoute.",
        rat: "Si les deux faits n'avaient aucun rapport, on écrirait deux phrases&nbsp;: "
           + "«&nbsp;<i>Elle a appris le français. Elle a trouvé un emploi.</i>&nbsp;» En les "
           + "cousant avec ce mot, celui qui écrit dit qu'il y a un rapport — reste à savoir "
           + "lequel, et c'est l'écran suivant." },
    ],
    pourquoi: "La première. Gardez la phrase en tête&nbsp;: on y revient au dernier écran, dans "
            + "une situation où elle ne s'écrira plus tout à fait pareil.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-emploi',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases lues cette semaine. Le mot en -ant répond à quoi ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Posez-vous une seule question devant "
            + "chaque phrase&nbsp;: est-ce que ça dit <b>quand</b>, ou est-ce que ça dit "
            + "<b>comment</b>&nbsp;?",
    colonnes: [
      { id: 'quand',   t: "Ça dit quand",   b: "Ça dit quand" },
      { id: 'comment', t: "Ça dit comment", b: "Ça dit comment" },
    ],
    items: [
      { txt: "En sortant du métro, j'ai reçu votre message.", sous: "un texto à un collègue",
        ok: 'quand',
        rat: "Sortir du métro n'est pas une façon de recevoir un message. Ça dit seulement le "
           + "<b>moment</b>&nbsp;: pendant que je sortais du métro.",
        pourquoi: "Le moment : pendant que je sortais du métro." },
      { txt: "On économise en achetant les portions familiales.", sous: "une affiche d'épicerie",
        ok: 'comment',
        rat: "Personne ne dit ici <i>quand</i> on économise. On dit le <b>moyen</b>&nbsp;: la "
           + "façon d'économiser, c'est d'acheter les grands formats.",
        pourquoi: "Le moyen : c'est ainsi qu'on économise." },
      { txt: "Ma fille s'est blessée en jouant au parc.", sous: "un mot à l'école", ok: 'quand',
        rat: "Jouer n'est pas une méthode pour se blesser. C'est le <b>moment</b> et le contexte&nbsp;: "
           + "pendant qu'elle jouait.",
        pourquoi: "Le moment : pendant qu'elle jouait." },
      { txt: "Vous ouvrez la boîte en tirant sur la languette rouge.",
        sous: "une consigne de montage", ok: 'comment',
        rat: "C'est exactement la <b>manière</b> d'ouvrir la boîte&nbsp;: tirer sur la languette. "
           + "Une consigne ne dit presque jamais quand — elle dit comment.",
        pourquoi: "La manière : c'est ainsi qu'on ouvre." },
      { txt: "En rentrant du travail, j'ai trouvé un avis dans ma porte.",
        sous: "un message au propriétaire", ok: 'quand',
        rat: "Rentrer du travail n'a rien fait apparaître dans la porte. Ça situe le "
           + "<b>moment</b> de la découverte.",
        pourquoi: "Le moment : à mon retour." },
      { txt: "Il a réglé son problème en téléphonant au service à la clientèle.",
        sous: "un forum d'entraide", ok: 'comment',
        rat: "Voilà la <b>solution</b>, pas l'heure. Ce qu'il a fait pour régler le problème, "
           + "c'est appeler.",
        pourquoi: "Le moyen : c'est ainsi qu'il a réglé le problème." },
      { txt: "Prenez ce comprimé en mangeant.", sous: "une étiquette de pharmacie", ok: 'quand',
        rat: "Manger n'est pas une façon d'avaler un comprimé. La pharmacienne dit "
           + "<b>quand</b>&nbsp;: pendant le repas, pas à jeun.",
        pourquoi: "Le moment : pendant le repas." },
      { txt: "Vous améliorerez votre prononciation en écoutant la radio d'ici.",
        sous: "un conseil d'enseignante", ok: 'comment',
        rat: "Ce n'est pas un horaire, c'est une <b>méthode</b>. Remarquez qu'on pourrait "
           + "répondre&nbsp;: «&nbsp;de quelle façon&nbsp;?&nbsp;»",
        pourquoi: "La méthode : c'est ainsi qu'on progresse." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez séparé le moment de la méthode. Un seul mot fait les deux.",
    paras: [
      "«&nbsp;En&nbsp;» suivi d'un verbe en <b>-ant</b> ne dit jamais qu'une chose est arrivée "
      + "après l'autre. Il colle deux actions à la <b>même personne</b>, et il dit soit le "
      + "moment, soit le moyen. C'est le lecteur qui tranche entre les deux — et il y arrive "
      + "toujours, comme vous venez de le faire huit fois sans règle.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> demandez-vous "
      + "<b>qui fait l'action du mot en -ant</b>. La réponse doit être le sujet de la phrase, "
      + "toujours. «&nbsp;<i>Elle a trouvé un emploi en apprenant le français</i>&nbsp;»&nbsp;: "
      + "qui apprend&nbsp;? Elle. La phrase tient.",

      "Ce mot s'appelle un <b>gérondif</b>. Vous n'avez pas besoin du nom pour vous en servir, "
      + "mais votre enseignant l'emploiera — et il tient en une ligne&nbsp;: «&nbsp;en&nbsp;» plus "
      + "un verbe en -ant, dont l'auteur est le sujet de la phrase.",
    ],
    retenir: "Demandez&nbsp;: <b>qui fait l'action du mot en -ant&nbsp;?</b> Si ce n'est pas le "
           + "sujet de la phrase, la phrase est fausse.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège central : le sujet emprunté. ─────────────────────────────
  {
    id:   'qui-fait-quoi',
    type: 'verif',
    eye:  'Le piège du sujet',
    menu: 'Qui fait quoi',
    titre: "Farida écrit à son propriétaire. Elle a vu de l'eau au sous-sol en descendant.",
    consigne: "Trois versions du même fait. Appliquez le test&nbsp;: qui descend&nbsp;?",
    options: [
      { txt: "En descendant au sous-sol, j'ai vu de l'eau sur le plancher.", juste: true },
      { txt: "En descendant au sous-sol, l'eau était partout sur le plancher.",
        rat_t: "C'est la faute la plus fréquente, et elle passe presque inaperçue.",
        rat: "Appliquez le test&nbsp;: qui descend au sous-sol&nbsp;? Le sujet de la phrase est "
           + "«&nbsp;l'eau&nbsp;». L'eau ne descend pas l'escalier pour aller voir. À l'oral "
           + "personne ne vous reprendrait&nbsp;; à l'écrit, la phrase dit autre chose que ce que "
           + "Farida a vécu." },
      { txt: "En descendant au sous-sol, le plancher était couvert d'eau.",
        rat_t: "Même mécanique&nbsp;: c'est le plancher qui descend.",
        rat: "Le sujet est «&nbsp;le plancher&nbsp;», et c'est donc lui qui descendrait l'escalier. "
           + "La correction ne consiste pas à changer le début&nbsp;: elle consiste à <b>ramener "
           + "la personne</b> comme sujet — «&nbsp;<i>j'ai vu</i>&nbsp;», «&nbsp;<i>j'ai "
           + "trouvé</i>&nbsp;»." },
    ],
    pourquoi: "Le mot en -ant n'a pas de sujet à lui&nbsp;: il <b>emprunte</b> celui de la phrase. "
            + "Écrire «&nbsp;en descendant&nbsp;» oblige donc à faire commencer la suite par la "
            + "personne qui descend.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Une seule personne, et ce que ça permet de couper. ────────────────
  {
    id:   'un-seul-sujet',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: 'Une seule personne',
    titre: "Le gérondif ne sert qu'à une personne à la fois.",
    paras: [
      "C'est ce qui le rend utile et ce qui le rend piégeux. Utile&nbsp;: comme les deux actions "
      + "sont à la même personne, on n'a pas à la nommer deux fois. Trois petites phrases "
      + "deviennent une&nbsp;: «&nbsp;<i>J'ai attendu l'autobus. Je lisais vos consignes. Je les "
      + "ai comprises.</i>&nbsp;» → «&nbsp;<i>J'ai compris vos consignes en les lisant à l'arrêt "
      + "d'autobus.</i>&nbsp;»",

      "Piégeux&nbsp;: dès que les deux actions sont à <b>deux personnes différentes</b>, il est "
      + "interdit. Il faut alors une vraie subordonnée avec «&nbsp;pendant que&nbsp;» ou "
      + "«&nbsp;quand&nbsp;»&nbsp;: «&nbsp;<i>Pendant que je descendais, ma voisine sortait ses "
      + "poubelles.</i>&nbsp;» Deux personnes, donc deux sujets écrits.",

      "Un mot de plus, qu'on rencontre partout et qui ne change rien à la règle&nbsp;: "
      + "<b>tout</b> en faisant. «&nbsp;<i>Elle prend des notes tout en écoutant.</i>&nbsp;» Le "
      + "«&nbsp;tout&nbsp;» insiste sur le fait que les deux actions se mènent ensemble. Même "
      + "personne, même contrainte.",
    ],
    retenir: "Une seule personne&nbsp;: «&nbsp;en&nbsp;» + -ant. Deux personnes&nbsp;: "
           + "«&nbsp;<b>pendant que</b>&nbsp;» et un sujet écrit.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Une seule chose à vérifier&nbsp;: qui fait l'action du mot en -ant, et est-ce "
            + "bien le sujet de la phrase&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "En arrivant à la clinique, la porte était déjà fermée.", ok: 'faux',
        rat: "Qui arrive&nbsp;? Le sujet écrit est «&nbsp;la porte&nbsp;». Il faut ramener la "
           + "personne&nbsp;: «&nbsp;<i>en arrivant à la clinique, j'ai trouvé la porte "
           + "fermée</i>&nbsp;».",
        pourquoi: "La porte n'arrive pas : « j'ai trouvé la porte fermée »." },
      { txt: "J'ai perdu mes clés en déménageant.", ok: 'ok',
        rat: "Qui déménage&nbsp;? Je. Le sujet de la phrase est le même que celui du mot en -ant. "
           + "Rien à corriger.",
        pourquoi: "Même personne pour les deux actions. Juste." },
      { txt: "En signant ce formulaire, vous acceptez les conditions.", ok: 'ok',
        rat: "Qui signe&nbsp;? Vous. C'est la formule des contrats et des baux, et elle est "
           + "correctement bâtie&nbsp;: la personne qui signe est aussi celle qui accepte.",
        pourquoi: "Vous signez, vous acceptez. Juste." },
      { txt: "En travaillant le soir, mon horaire est devenu impossible.", ok: 'faux',
        rat: "Un horaire ne travaille pas le soir. La phrase veut dire «&nbsp;<i>en travaillant le "
           + "soir, j'ai fini avec un horaire impossible</i>&nbsp;» — c'est la personne qu'il faut "
           + "remettre en sujet.",
        pourquoi: "L'horaire ne travaille pas : « j'ai fini avec… »." },
      { txt: "Vous éviterez les frais en payant avant le 15 du mois.", ok: 'ok',
        rat: "Qui paie&nbsp;? Vous. Et le gérondif dit ici le <b>moyen</b> d'éviter les frais&nbsp;: "
           + "les deux emplois de l'écran 2 sont corrects, seul le sujet décide.",
        pourquoi: "Vous payez, vous évitez les frais. Juste." },
      { txt: "En ouvrant la porte, le chat s'est sauvé dans le corridor.", ok: 'faux',
        rat: "Celle-là fait sourire une fois qu'on la voit&nbsp;: le sujet est «&nbsp;le "
           + "chat&nbsp;», donc c'est lui qui ouvre la porte. «&nbsp;<i>Quand j'ai ouvert la "
           + "porte, le chat s'est sauvé</i>&nbsp;» — deux personnages, deux sujets.",
        pourquoi: "Le chat n'ouvre pas la porte : « quand j'ai ouvert… »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qu'on écrit, et où. ────────────────────────────────────────────
  {
    id:   'ce-quon-ecrit',
    type: 'verif',
    eye:  'Vérification',
    menu: "À l'écrit",
    titre: "Vous écrivez à une employeuse pour expliquer un retard de livraison.",
    consigne: "Deux faits&nbsp;: vous avez vérifié le colis, et vous avez découvert l'erreur. "
            + "C'est vous qui faites les deux.",
    options: [
      { txt: "«&nbsp;En vérifiant le colis ce matin, j'ai découvert l'erreur.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;En vérifiant le colis ce matin, l'erreur est apparue.&nbsp;»",
        rat_t: "La phrase est polie, et pourtant elle dit que l'erreur vérifie le colis.",
        rat: "C'est la version qui sort naturellement quand on veut éviter de dire "
           + "«&nbsp;je&nbsp;». Mais le gérondif oblige à nommer celui qui agit&nbsp;: si vous "
           + "voulez rester discret, changez de construction — «&nbsp;<i>une erreur est apparue "
           + "lors de la vérification</i>&nbsp;» — plutôt que de laisser un sujet qui ne peut pas "
           + "faire l'action." },
      { txt: "«&nbsp;J'ai vérifié le colis ce matin et après j'ai découvert l'erreur.&nbsp;»",
        rat_t: "Ce n'est pas une faute — c'est plus lourd, et ça dit autre chose.",
        rat: "Rien n'est incorrect ici. Mais «&nbsp;et après&nbsp;» range les deux actions l'une "
           + "derrière l'autre, alors que la découverte s'est faite <b>pendant</b> la "
           + "vérification. Le gérondif dit exactement ça, et en quatre mots de moins." },
    ],
    pourquoi: "Le gérondif est l'outil qui <b>resserre</b> un message professionnel. Son prix est "
            + "qu'il vous oblige à assumer le sujet&nbsp;: quelqu'un fait les deux actions, et ce "
            + "quelqu'un doit être écrit.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La forme, dite en dernier : c'est la partie facile. ───────────────
  {
    id:   'la-forme-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'La fabrication',
    titre: "La forme se fabrique en trois secondes, et c'est pour ça qu'on l'a gardée pour la fin.",
    paras: [
      "Prenez le verbe avec <b>nous</b>, au présent, enlevez «&nbsp;-ons&nbsp;», ajoutez "
      + "«&nbsp;-ant&nbsp;». Nous finiss<i>ons</i> → en finiss<b>ant</b>. Nous pren<i>ons</i> → en "
      + "pren<b>ant</b>. Nous fais<i>ons</i> → en fais<b>ant</b>. Nous appel<i>ons</i> → en "
      + "appel<b>ant</b>. Ça marche sur un verbe que vous n'avez jamais vu.",

      "<b>Trois verbes seulement</b> ne suivent pas&nbsp;: en <b>étant</b>, en <b>ayant</b>, en "
      + "<b>sachant</b>. Trois, pas quinze — il n'y a pas de liste à apprendre.",

      "Deux détails qui évitent des ratures. Le mot en -ant ne s'accorde jamais&nbsp;: ni "
      + "«&nbsp;<i>en descendantes</i>&nbsp;», ni «&nbsp;<i>en descendants</i>&nbsp;», quel que "
      + "soit le nombre de personnes. Et les pronoms se glissent entre «&nbsp;en&nbsp;» et le "
      + "verbe&nbsp;: «&nbsp;<i>en <b>me</b> levant</i>&nbsp;», «&nbsp;<i>en <b>les</b> "
      + "lisant</i>&nbsp;», «&nbsp;<i>en <b>lui</b> parlant</i>&nbsp;».",
    ],
    retenir: "Le radical de <b>nous</b> + -ant, invariable. La difficulté n'a jamais été la "
           + "forme&nbsp;: c'est de savoir <b>qui</b> fait l'action.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Un message à l'école. Quelle version tient d'un bout à l'autre ?",
    consigne: "Sandro explique que son fils s'est fait mal pendant qu'il courait dans la cour, et "
            + "qu'il l'a su en allant le chercher. Trois versions&nbsp;: une seule est correcte "
            + "partout.",
    options: [
      { txt: "Mon fils s'est blessé en courant dans la cour&nbsp;; je l'ai appris en allant le "
           + "chercher.",
        juste: true },
      { txt: "Mon fils s'est blessé en courant dans la cour&nbsp;; en allant le chercher, la "
           + "nouvelle m'a été donnée.",
        rat_t: "La première moitié est juste. C'est la seconde qui lâche.",
        rat: "«&nbsp;Il s'est blessé en courant&nbsp;»&nbsp;: c'est bien lui qui court, rien à "
           + "redire. Mais dans la seconde, le sujet est «&nbsp;la nouvelle&nbsp;», et une "
           + "nouvelle ne va chercher personne. Écrivez «&nbsp;<i>je l'ai appris</i>&nbsp;»." },
      { txt: "En courant dans la cour, une blessure est arrivée à mon fils&nbsp;; je l'ai appris "
           + "en allant le chercher.",
        rat_t: "Cette fois c'est la première moitié qui a lâché.",
        rat: "«&nbsp;Une blessure&nbsp;» ne court pas dans la cour. Vous aviez pourtant réglé la "
           + "seconde moitié correctement — c'est la preuve que la règle est comprise et que "
           + "seule l'attention manque. Relisez chaque gérondif en vous demandant qui agit." },
    ],
    pourquoi: "Deux gérondifs, deux sujets à vérifier, et le même test à chaque fois. "
            + "<b>C'est tout le point en une phrase.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « Elle a trouvé un emploi en apprenant le français. »",
    consigne: "Cette fois, c'est vous qui écrivez, dans une lettre de présentation, et vous "
            + "voulez dire que la formation en francisation vous a servi. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;J'ai gagné en assurance au téléphone en suivant cette formation.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;En suivant cette formation, mon assurance au téléphone s'est "
           + "améliorée.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 4, avec un autre décor.",
        rat: "Le sujet est «&nbsp;mon assurance&nbsp;», et une assurance ne suit pas de "
           + "formation. Dans une lettre de présentation, c'est justement l'endroit où l'on veut "
           + "être le sujet de ses propres progrès&nbsp;: écrivez «&nbsp;<i>j'ai gagné</i>&nbsp;»." },
      { txt: "«&nbsp;En suivant cette formation et après j'ai gagné en assurance.&nbsp;»",
        rat_t: "Le sujet est bon. C'est la charnière qui ne tient plus.",
        rat: "Vous avez ramené la personne comme sujet, ce qui était le plus difficile. Mais "
           + "«&nbsp;et après&nbsp;» ajoute une suite là où le gérondif dit déjà le lien&nbsp;: "
           + "il faut choisir l'un ou l'autre, jamais les deux." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître si le mot en -ant dit le moment "
            + "ou le moyen, vérifier que son auteur est le sujet de la phrase, et vous en servir "
            + "pour resserrer un message que quelqu'un va lire.",
    attente: "Choisissez une réponse pour finir.",
  },

];
