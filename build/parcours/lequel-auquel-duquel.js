// ═══════════════════════════════════════════════════════════════════════════
// Point express — Enchaîner sans recommencer la phrase
//
// Savoir n7-s13 (phrases subordonnées relatives introduites par
// [préposition] + lequel). Une ORDONNANCE : l'enseignant l'envoie à l'élève
// qui écrit « le formulaire que j'ai inscrit mon numéro », ou qui recommence
// une phrase neuve à chaque fois qu'un petit mot devrait la raccorder.
// Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Quatre mini-leçons du dépôt traitent le sujet, et les quatre commencent par
// la liste des formes :
//   · « Auquel, dont, ce à quoi : le pronom porte la préposition »
//   · « Dont, auquel, sur laquelle : suivre le fil d'une phrase longue »
//   · « Le pronom relatif après une préposition »
//   · « Les relatives qui portent une préposition »
// Un élève qui les a lues connaît le tableau — auquel, à laquelle, auxquels —
// et bute toujours au même endroit : il ne sait pas QUEL petit mot mettre
// devant. Or ce petit mot n'est pas dans le tableau : il est dans le verbe de
// la deuxième phrase. Les cinq écarts tenus :
//
//   1. INDUCTIF, ET SUR UNE QUESTION QUI N'A RIEN À VOIR AVEC LES RELATIFS.
//      L'écran 2 fait trier huit verbes selon qu'ils appellent « à » ou
//      « de ». Aucun pronom n'y paraît. C'est pourtant la seule chose qui
//      décide de tout le reste, et c'est ce que l'élève ne cherche jamais.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des quatre genres et
//      nombres. Une MARCHE À SUIVRE en trois gestes — trouver le petit mot,
//      le poser en tête, choisir « qui » ou « lequel » selon qu'on parle
//      d'une personne ou d'une chose — qui marche sur un verbe jamais vu.
//   3. LE CAS PAR DÉFAUT EST DIT EN DERNIER. La sortie de secours de
//      l'écran 8 — couper en deux phrases — est ce qu'un rédacteur
//      professionnel fait la moitié du temps. La donner d'entrée aurait
//      dispensé l'élève de tout le reste.
//   4. LE MÉTALANGAGE APRÈS. « Pronom relatif » n'est écrit qu'à l'écran 3.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un formulaire d'école, un
//      collègue, un dossier au téléphone, une réclamation, une petite
//      annonce, un immeuble.
//
// Aucun média : « le formulaire que j'ai inscrit » passe très bien à
// l'oral — c'est même ce qu'on entend partout. La faute n'existe qu'écrite.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'lequel-auquel-duquel',
  titre:    "Enchaîner sans recommencer la phrase",
  surtitre: "Point express · 10 minutes",
  niveau:   7,
  savoir:   'n7-s13',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois phrases',
    titre: "Vous remettez une feuille au secrétariat. Une seule de ces phrases s'écrit.",
    consigne: "Vous avez inscrit votre numéro de dossier en haut du formulaire, et vous "
            + "l'expliquez. Répondez avec ce que vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Voici le formulaire sur lequel j'ai inscrit mon numéro de dossier.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Voici le formulaire que j'ai inscrit mon numéro de dossier.&nbsp;»",
        rat_t: "C'est ce qu'on entend partout, et ça ne s'écrit nulle part.",
        rat: "«&nbsp;Que&nbsp;» ne peut porter qu'une chose&nbsp;: ce qu'on inscrit. Or ici, vous "
           + "n'avez pas inscrit le formulaire — vous avez inscrit un numéro <b>sur</b> le "
           + "formulaire. Ce petit mot «&nbsp;sur&nbsp;» a disparu de la phrase, et le lecteur "
           + "doit la relire deux fois." },
      { txt: "«&nbsp;Voici le formulaire qui j'ai inscrit mon numéro de dossier.&nbsp;»",
        rat_t: "«&nbsp;Qui&nbsp;» désigne celui qui fait l'action.",
        rat: "Dans «&nbsp;la personne <b>qui</b> a inscrit&nbsp;», c'est la personne qui écrit. "
           + "Ici, la phrase fait donc du formulaire l'auteur de l'inscription, et vous "
           + "disparaissez. Le mot manquant n'est pas celui-là." },
    ],
    pourquoi: "La première. Gardez-la en tête&nbsp;: elle revient au dernier écran, avec une "
            + "personne de plus.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir, et sur autre chose que les relatifs. ─────
  {
    id:   'tri-a-ou-de',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit verbes',
    titre: "Huit phrases à trou. Quel petit mot le verbe demande-t-il ?",
    consigne: "Aucune règle ne vous a été donnée, et il n'est encore question d'aucun pronom. "
            + "Dites seulement ce qui se met dans le trou — vous le savez déjà, vous le dites "
            + "tous les jours.",
    colonnes: [
      { id: 'a',  t: "à",  b: "à" },
      { id: 'de', t: "de", b: "de" },
    ],
    items: [
      { txt: "Je pense ___ ce problème depuis un mois.", sous: "penser", ok: 'a',
        rat: "On pense <b>à</b> quelque chose. C'est le verbe qui l'impose&nbsp;: aucun autre "
           + "mot de la phrase n'a son mot à dire.",
        pourquoi: "penser à — le verbe décide." },
      { txt: "J'ai besoin ___ deux documents de plus.", sous: "avoir besoin", ok: 'de',
        rat: "On a besoin <b>de</b> quelque chose. Là encore, c'est l'expression elle-même qui "
           + "porte le petit mot, et elle ne le lâche jamais.",
        pourquoi: "avoir besoin de — l'expression le porte." },
      { txt: "Je me suis adressée ___ la conseillère du deuxième étage.", sous: "s'adresser", ok: 'a',
        rat: "On s'adresse <b>à</b> quelqu'un. Le verbe demande la même chose qu'il s'agisse d'une "
           + "personne ou d'un bureau.",
        pourquoi: "s'adresser à — personne ou bureau, pareil." },
      { txt: "Il m'a parlé ___ son ancien employeur.", sous: "parler", ok: 'de',
        rat: "Parler <b>de</b> quelqu'un, c'est en dire quelque chose. Attention&nbsp;: parler "
           + "<i>à</i> quelqu'un existe aussi, et ce n'est pas le même sens. Ici, la suite de la "
           + "phrase dit bien qu'il en a parlé.",
        pourquoi: "parler de — dire quelque chose sur lui." },
      { txt: "Je n'ai pas encore répondu ___ votre courriel de mardi.", sous: "répondre", ok: 'a',
        rat: "On répond <b>à</b> un courriel, à une lettre, à une question. Le verbe l'exige, et "
           + "on ne l'entend presque plus tellement il est court.",
        pourquoi: "répondre à — toujours." },
      { txt: "Elle s'est servie ___ son téléphone pour prendre la photo.", sous: "se servir", ok: 'de',
        rat: "Se servir <b>de</b> quelque chose. Celui-là trompe, parce qu'on «&nbsp;utilise&nbsp;» "
           + "sans petit mot du tout — deux verbes proches, deux constructions différentes.",
        pourquoi: "se servir de — et « utiliser » n'en veut aucun." },
      { txt: "Il a participé ___ toutes les rencontres du comité.", sous: "participer", ok: 'a',
        rat: "On participe <b>à</b> une rencontre, à un programme, à une réunion. C'est un des "
           + "verbes les plus fréquents des lettres officielles.",
        pourquoi: "participer à — fréquent dans les lettres." },
      { txt: "Plusieurs locataires se sont plaints ___ bruit du chantier.", sous: "se plaindre", ok: 'de',
        rat: "On se plaint <b>de</b> quelque chose, et <i>à</i> quelqu'un&nbsp;: "
           + "«&nbsp;ils se sont plaints du bruit <b>au</b> propriétaire&nbsp;». Ici, la phrase "
           + "ne nomme que la chose.",
        pourquoi: "se plaindre de quelque chose." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'la-marche-a-suivre',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Trois gestes',
    titre: "Vous n'avez pas choisi un pronom. Vous avez écouté le verbe.",
    paras: [
      "Ce petit mot que vous venez de trouver huit fois est <b>tout le point</b>. Quand vous "
      + "collez deux phrases en une, il ne disparaît pas&nbsp;: il vient se poser en tête de la "
      + "seconde. «&nbsp;<i>J'ai besoin <b>de</b> deux documents</i>&nbsp;» donne "
      + "«&nbsp;<i>les documents <b>dont</b> j'ai besoin</i>&nbsp;». "
      + "«&nbsp;<i>J'ai participé <b>à</b> ces rencontres</i>&nbsp;» donne "
      + "«&nbsp;<i>les rencontres <b>auxquelles</b> j'ai participé</i>&nbsp;».",

      "<b>Trois gestes, dans cet ordre&nbsp;:</b> "
      + "<b>1.</b> Dites la deuxième phrase toute seule, et repérez le petit mot que son verbe "
      + "demande — <i>à</i>, <i>de</i>, <i>sur</i>, <i>avec</i>, <i>pour</i>, <i>dans</i>. "
      + "<b>2.</b> Posez-le en tête. "
      + "<b>3.</b> Derrière lui, écrivez <b>qui</b> s'il s'agit d'une personne, "
      + "<b>lequel · laquelle · lesquels · lesquelles</b> s'il s'agit d'une chose.",

      "Ce mot de raccord s'appelle un <b>pronom relatif</b>. Ce qu'aucune liste de pronoms ne "
      + "vous dira, c'est le geste&nbsp;1&nbsp;: le petit mot ne se choisit pas, il se "
      + "<b>récupère</b> dans le verbe.",
    ],
    retenir: "<b>Le verbe donne le petit mot&nbsp;; le petit mot passe devant&nbsp;; puis "
           + "«&nbsp;qui&nbsp;» pour une personne, «&nbsp;lequel&nbsp;» pour une chose.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Les deux soudures : à + lequel, de + lequel. ──────────────────────
  {
    id:   'les-soudures',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Deux soudures',
    titre: "« À lequel » ne s'écrit jamais. Il y a deux mots qui se soudent, et deux seulement.",
    consigne: "Amadou raconte une formation à laquelle il s'est inscrit. Il applique les trois "
            + "gestes&nbsp;: le verbe est «&nbsp;s'inscrire <b>à</b>&nbsp;», et une formation est "
            + "une chose. Quelle phrase écrit-il&nbsp;?",
    options: [
      { txt: "«&nbsp;La formation <b>à laquelle</b> je me suis inscrit commence lundi.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;La formation <b>à lequel</b> je me suis inscrit commence lundi.&nbsp;»",
        rat_t: "Les trois gestes sont bons&nbsp;: c'est la fin du mot qui n'a pas suivi.",
        rat: "«&nbsp;Lequel&nbsp;» change de fin selon ce qu'il remplace, exactement comme un "
           + "adjectif&nbsp;: <b>une</b> formation, donc «&nbsp;à <b>laquelle</b>&nbsp;». Un truc "
           + "qui ne trompe jamais&nbsp;: dites d'abord «&nbsp;<i>la formation, <b>elle</b></i>&nbsp;» "
           + "ou «&nbsp;<i>le formulaire, <b>lui</b></i>&nbsp;» — le mot que vous venez de dire "
           + "vous donne la fin." },
      { txt: "«&nbsp;La formation <b>à laquelle</b> je me suis inscrit à commence lundi.&nbsp;»",
        rat_t: "Le petit mot a été écrit deux fois.",
        rat: "Vous l'avez bien récupéré <b>et</b> vous l'avez laissé à sa place d'origine. Il ne "
           + "s'écrit qu'une fois, en tête&nbsp;: une fois passé devant, il ne reste rien "
           + "derrière le verbe." },
    ],
    pourquoi: "<b>Deux soudures, et rien d'autre à retenir&nbsp;: à + lequel = "
            + "auquel&nbsp;; de + lequel = duquel</b> (et au pluriel, <i>auxquels</i>, "
            + "<i>desquelles</i>…). Au féminin singulier, rien ne bouge&nbsp;: <i>à laquelle</i>, "
            + "<i>de laquelle</i>.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Les personnes : un seul mot couvre tout. ──────────────────────────
  {
    id:   'les-personnes',
    type: 'notion',
    eye:  'La partie facile',
    menu: 'Les personnes',
    titre: "Devant une personne, un seul mot suffit après le petit mot : « qui ».",
    paras: [
      "«&nbsp;<i>La conseillère <b>à qui</b> je me suis adressée.</i>&nbsp;» "
      + "«&nbsp;<i>Le collègue <b>avec qui</b> je travaille.</i>&nbsp;» "
      + "«&nbsp;<i>La personne <b>pour qui</b> je fais la demande.</i>&nbsp;» "
      + "Aucune fin de mot à choisir, ni masculin, ni féminin, ni pluriel&nbsp;: <b>qui</b> ne "
      + "bouge jamais. C'est la moitié facile du point, et c'est la moitié que vous emploierez "
      + "le plus souvent.",

      "Ne confondez pas avec le «&nbsp;qui&nbsp;» de l'écran 1. Celui-là était seul en "
      + "tête — «&nbsp;<i>la personne <b>qui</b> a téléphoné</i>&nbsp;» — et il désignait celui "
      + "qui fait l'action. Ici, il y a toujours un petit mot devant lui&nbsp;: <i>à qui</i>, "
      + "<i>avec qui</i>, <i>chez qui</i>. Si rien ne le précède, ce n'est pas le même emploi.",

      "«&nbsp;Auquel&nbsp;» et «&nbsp;à laquelle&nbsp;» s'emploient aussi pour des "
      + "personnes — vous les rencontrerez dans des textes officiels. Vous n'avez aucune raison "
      + "de les écrire&nbsp;: <i>à qui</i> dit exactement la même chose et ne se trompe pas.",
    ],
    retenir: "<b>Une personne&nbsp;: le petit mot + «&nbsp;qui&nbsp;».</b> Une chose&nbsp;: le "
           + "petit mot + «&nbsp;lequel&nbsp;», accordé.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles sont correctes ?",
    consigne: "Pour chacune, dites la deuxième moitié toute seule et cherchez le petit mot que son "
            + "verbe demande. Comparez ensuite avec ce qui est écrit.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Le dossier auquel vous faites référence a été fermé en mai.", ok: 'ok',
        rat: "«&nbsp;Faire référence <b>à</b> un dossier&nbsp;», et un dossier est une chose "
           + "masculine&nbsp;: à + lequel = <b>auquel</b>. Les trois gestes sont faits.",
        pourquoi: "faire référence à + un dossier = auquel." },
      { txt: "Le collègue avec lequel je partage mon bureau part en congé.", ok: 'ok',
        rat: "«&nbsp;Avec lequel&nbsp;» est correct pour une personne — un peu plus écrit que "
           + "«&nbsp;avec qui&nbsp;», qui aurait aussi bien fait l'affaire.",
        pourquoi: "Correct. « avec qui » aurait été plus simple." },
      { txt: "La réunion que j'ai participé s'est terminée à midi.", ok: 'faux',
        rat: "Le petit mot du verbe a été avalé. On participe <b>à</b> une réunion&nbsp;: "
           + "«&nbsp;la réunion <b>à laquelle</b> j'ai participé&nbsp;».",
        pourquoi: "à laquelle j'ai participé." },
      { txt: "L'outil dont je me sers tous les jours est en réparation.", ok: 'ok',
        rat: "«&nbsp;Se servir <b>de</b>&nbsp;»&nbsp;: le petit mot est <i>de</i>, et un "
           + "<i>de</i> tout seul se dit «&nbsp;dont&nbsp;». On y revient à l'écran suivant.",
        pourquoi: "se servir de → dont." },
      { txt: "Les documents lesquels vous avez besoin sont au dossier.", ok: 'faux',
        rat: "Le pronom est là, le petit mot manque. «&nbsp;Avoir besoin <b>de</b>&nbsp;»&nbsp;: "
           + "il faut «&nbsp;les documents <b>dont</b> vous avez besoin&nbsp;». "
           + "«&nbsp;Lequel&nbsp;» ne s'emploie jamais seul.",
        pourquoi: "dont vous avez besoin." },
      { txt: "La personne à qui j'ai laissé le message ne m'a pas rappelée.", ok: 'ok',
        rat: "Une personne, un petit mot devant, et «&nbsp;qui&nbsp;» qui ne change jamais de "
           + "fin&nbsp;: c'est la forme la plus sûre de tout le point.",
        pourquoi: "à qui — invariable, et toujours juste." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. « Dont » : le cas le plus fréquent, et sa seule limite. ───────────
  {
    id:   'dont-ou-duquel',
    type: 'verif',
    eye:  'Vérification',
    menu: '« Dont »',
    titre: "Quand le petit mot est « de », le raccourci s'appelle « dont ».",
    consigne: "Karine décrit un immeuble dans une petite annonce. Elle veut dire deux choses&nbsp;: "
            + "l'immeuble a une cour, et le stationnement se trouve derrière la cour. Quelle "
            + "phrase écrit-elle&nbsp;?",
    options: [
      { txt: "«&nbsp;Un immeuble dont la cour est clôturée, et derrière laquelle se trouve le "
           + "stationnement.&nbsp;»", juste: true },
      { txt: "«&nbsp;Un immeuble duquel la cour est clôturée, et derrière laquelle se trouve le "
           + "stationnement.&nbsp;»",
        rat_t: "«&nbsp;Duquel&nbsp;» existe, mais pas quand le «&nbsp;de&nbsp;» est seul.",
        rat: "Ici, le petit mot n'a rien devant lui&nbsp;: c'est «&nbsp;la cour <b>de</b> "
           + "l'immeuble&nbsp;». Un <i>de</i> tout seul s'écrit <b>dont</b>, et c'est le cas "
           + "le plus fréquent — celui qu'on emploie dix fois par jour. Gardez "
           + "«&nbsp;duquel&nbsp;» pour ce que fait la deuxième moitié de cette phrase." },
      { txt: "«&nbsp;Un immeuble dont la cour est clôturée, et dont se trouve le "
           + "stationnement.&nbsp;»",
        rat_t: "La première moitié est parfaite. La seconde a perdu son petit mot.",
        rat: "Le stationnement n'est pas «&nbsp;de&nbsp;» la cour, il est <b>derrière</b> elle. "
           + "«&nbsp;Dont&nbsp;» ne peut porter que <i>de</i>&nbsp;; dès qu'un autre mot entre — "
           + "<i>derrière</i>, <i>à côté de</i>, <i>au bout de</i> — il faut la forme longue&nbsp;: "
           + "«&nbsp;derrière <b>laquelle</b>&nbsp;»." },
    ],
    pourquoi: "<b>«&nbsp;De&nbsp;» tout seul&nbsp;→ dont.</b> Un mot devant le "
            + "«&nbsp;de&nbsp;»&nbsp;→ la forme longue&nbsp;: <i>à côté duquel</i>, <i>au bout "
            + "de laquelle</i>, <i>à la suite desquels</i>.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La sortie de secours, gardée pour la fin. ─────────────────────────
  {
    id:   'couper-en-deux',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Couper en deux',
    titre: "Vous avez toujours le droit de faire deux phrases. Personne ne vous en tiendra rigueur.",
    paras: [
      "On a gardé ceci pour la fin exprès&nbsp;: donné au début, il vous aurait dispensé de tout "
      + "le reste. Mais maintenant que vous savez faire, il faut savoir quand ne pas le "
      + "faire. «&nbsp;<i>Voici le formulaire. J'ai inscrit mon numéro de dossier en haut.</i>&nbsp;» "
      + "Deux phrases courtes, aucun pronom, aucune faute possible — et c'est ainsi qu'écrivent "
      + "beaucoup de lettres officielles.",

      "Quand couper vaut mieux&nbsp;: quand la phrase dépasse deux lignes, quand vous devriez "
      + "enchaîner deux relatifs («&nbsp;<i>le dossier auquel j'ai répondu et dont vous "
      + "parlez</i>&nbsp;»), ou quand la forme ne vient pas et que vous alliez écrire "
      + "«&nbsp;que&nbsp;» faute de mieux. Un lecteur pressé ne remarquera jamais que vous avez "
      + "coupé&nbsp;; il remarquera toujours qu'il a dû relire.",

      "Quand raccorder vaut mieux&nbsp;: quand les deux phrases parlent de la même chose et que "
      + "la seconde ne tiendrait pas debout toute seule. «&nbsp;<i>La personne à qui j'ai laissé "
      + "le message.</i>&nbsp;» — coupée en deux, elle vous obligerait à répéter «&nbsp;cette "
      + "personne&nbsp;» à chaque phrase, et c'est là que le texte devient lourd.",
    ],
    retenir: "<b>Le pronom relatif est un outil, pas une obligation.</b> Deux phrases claires "
           + "valent mieux qu'une phrase longue dont vous n'êtes pas sûr.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre réclamation',
    titre: "Vous écrivez à un service à la clientèle. Quelle version tient d'un bout à l'autre ?",
    consigne: "Vous voulez dire trois choses&nbsp;: vous avez parlé à une agente le 12&nbsp;août, "
            + "elle vous a promis un remboursement, et vous n'avez toujours pas reçu le "
            + "formulaire nécessaire.",
    options: [
      { txt: "«&nbsp;L'agente à qui j'ai parlé le 12 août m'a promis un remboursement. Je n'ai "
           + "toujours pas reçu le formulaire dont j'ai besoin pour le demander.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;L'agente que j'ai parlé le 12 août m'a promis un remboursement. Je n'ai "
           + "toujours pas reçu le formulaire que j'ai besoin pour le demander.&nbsp;»",
        rat_t: "Les deux petits mots ont été avalés, et c'est la même faute deux fois.",
        rat: "Dites les deux moitiés toutes seules&nbsp;: «&nbsp;j'ai parlé <b>à</b> "
           + "l'agente&nbsp;», «&nbsp;j'ai besoin <b>de</b> ce formulaire&nbsp;». Les deux petits "
           + "mots existent, et «&nbsp;que&nbsp;» ne peut en porter aucun&nbsp;: il faut "
           + "«&nbsp;à qui&nbsp;» et «&nbsp;dont&nbsp;»." },
      { txt: "«&nbsp;L'agente à laquelle j'ai parlé le 12 août m'a promis un remboursement. Je "
           + "n'ai toujours pas reçu le formulaire duquel j'ai besoin pour le demander.&nbsp;»",
        rat_t: "La première moitié est correcte quoique lourde. La seconde ne s'écrit pas.",
        rat: "«&nbsp;À laquelle&nbsp;» pour une personne est juste, mais «&nbsp;à qui&nbsp;» "
           + "dit la même chose plus simplement. «&nbsp;Duquel&nbsp;», lui, est une faute&nbsp;: "
           + "le «&nbsp;de&nbsp;» d'«&nbsp;avoir besoin&nbsp;» est seul, donc c'est "
           + "<b>dont</b>." },
    ],
    pourquoi: "Le petit mot récupéré dans chaque verbe, «&nbsp;qui&nbsp;» pour la personne, "
            + "«&nbsp;dont&nbsp;» pour le <i>de</i> tout seul. <b>C'est tout le point en deux "
            + "lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au formulaire du début. Cette fois, une personne s'y ajoute.",
    consigne: "Vous écrivez au secrétariat. Vous avez inscrit votre numéro sur le formulaire, et "
            + "vous l'avez remis à une secrétaire que vous ne savez pas nommer. Que "
            + "choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Le formulaire sur lequel j'ai inscrit mon numéro a été remis à la personne "
           + "qui était au comptoir mardi.&nbsp;»", juste: true },
      { txt: "«&nbsp;Le formulaire sur lequel j'ai inscrit mon numéro a été remis à la personne à "
           + "qui était au comptoir mardi.&nbsp;»",
        rat_t: "La première moitié est exactement juste. C'est un petit mot de trop à la fin.",
        rat: "Dites la dernière moitié toute seule&nbsp;: «&nbsp;<i>cette personne <b>était</b> au "
           + "comptoir</i>&nbsp;». Le verbe ne demande rien du tout — la personne est celle qui "
           + "faisait l'action, donc «&nbsp;qui&nbsp;» tout seul. Le «&nbsp;à&nbsp;» de la phrase "
           + "appartient à «&nbsp;remis à&nbsp;», et il est déjà écrit." },
      { txt: "«&nbsp;Le formulaire que j'ai inscrit mon numéro a été remis à la personne qui était "
           + "au comptoir mardi.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1, et la fin de celle-ci est juste.",
        rat: "Vous avez bien vu que la personne du comptoir ne demandait aucun petit mot. Mais "
           + "«&nbsp;inscrire&nbsp;» en demandait un&nbsp;: on inscrit un numéro <b>sur</b> une "
           + "feuille. Le même geste des deux côtés&nbsp;: dire la moitié toute seule et écouter "
           + "le verbe." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: récupérer le petit mot dans le verbe, le "
            + "poser en tête, et choisir «&nbsp;qui&nbsp;» ou «&nbsp;lequel&nbsp;» selon qu'il "
            + "s'agit d'une personne ou d'une chose — sans en ajouter là où il n'y en a pas.",
    attente: "Choisissez une réponse pour finir.",
  },

];
