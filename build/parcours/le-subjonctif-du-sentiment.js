// ═══════════════════════════════════════════════════════════════════════════
// Point express — Dire ce qu'on ressent, sans faute après « que »
//
// Savoir n6-s29 (Subjonctif présent). Une ORDONNANCE : l'enseignant l'envoie à
// un élève qui écrit « je suis content que tu es venu », ou qui met un
// subjonctif partout depuis qu'il en a entendu parler. Dix minutes, dix écrans.
//
// ── Ce qui le sépare de ce qui existe déjà ─────────────────────────────────
// L'étagère porte au niveau 5 « Il faut que… : un seul emploi, six verbes » :
// un point express entièrement bâti sur l'OBLIGATION impersonnelle, avec une
// liste fermée de six verbes à mémoriser. Celui-ci ne le prolonge pas, il
// travaille ailleurs — le SENTIMENT et l'OPINION, où le déclencheur n'est pas
// une formule figée mais ce que la personne éprouve. Un élève qui a fait
// l'autre sait conjuguer « que je sois » et croit que le subjonctif est la
// langue des démarches administratives ; il écrit alors « je suis content que
// tu es venu » sans y voir de rapport.
//
// Et onze mini-leçons de modules traitent le subjonctif, toutes en listant les
// verbes introducteurs :
//   · `module-n7-emploi` — « Le subjonctif après le verbe qui introduit ».
//   · `module-n8-actualite` — « Le subjonctif de l'opinion et du doute ».
//   · `module-n8-emmenagement` — « Le subjonctif présent, et ce qui le
//     déclenche » ; et sept autres du même moule aux niveaux 5 à 8.
// Aucune ne pose la question qui décide vraiment — combien de personnes y
// a-t-il dans la phrase ? — alors que c'est elle qui départage « j'ai peur de
// ne pas réussir » et « j'ai peur que tu ne réussisses pas », les deux
// exemples que le programme donne lui-même au savoir n6-s29. Les cinq écarts :
//
//   1. INDUCTIF. L'élève range huit phrases selon le NOMBRE DE PERSONNES
//      avant qu'aucune règle ne soit dite. La règle de l'écran 3 est écrite
//      comme un constat de ce qu'il vient de faire.
//   2. PARTIEL, JAMAIS LA LISTE. Pas de tableau des verbes introducteurs. Un
//      TEST unique — une personne ou deux ? — qui marche sur un verbe jamais
//      vu, et qui choisit aussi la construction (« de » ou « que »).
//   3. LA CONJUGAISON EST DITE EN DERNIER (écran 8), alors que c'est par elle
//      que commencent les onze mini-leçons. La donner d'entrée fait croire
//      que la difficulté est la forme ; elle est dans le déclenchement.
//   4. LE MÉTALANGAGE ARRIVE APRÈS. « Subjonctif » n'est écrit qu'à l'écran 3.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un texto, un message à une
//      enseignante, une carte de félicitations, un courriel de travail, une
//      conversation de couloir.
//
// Aucun média : « que tu es venu » et « que tu sois venu » se distinguent très
// bien à l'oreille, mais la faute que l'élève commet est d'écrire l'un pour
// l'autre — c'est un point d'écrit, et rien à écouter n'y aiderait.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'le-subjonctif-du-sentiment',
  titre:    "Dire ce qu'on ressent, sans faute après « que »",
  surtitre: "Point express · 10 minutes",
  niveau:   6,
  savoir:   'n6-s29',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Une phrase',
    titre: "« Je suis contente que tu ___ venu à la fête. » Que met-on dans le trou ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "sois", juste: true },
      { txt: "es",
        rat_t: "C'est la forme qu'on emploie partout ailleurs, et c'est bien le problème.",
        rat: "«&nbsp;Tu es venu&nbsp;» est parfaitement correct tout seul&nbsp;: c'est ce qu'on "
           + "écrit dans un message pour raconter un fait. Ce qui change ici, c'est ce qu'il y a "
           + "<b>devant</b> — quelqu'un qui dit ce qu'il ressent. Le verbe qui suit se met alors "
           + "à une autre forme, et le reste du point sert à savoir quand." },
      { txt: "serais",
        rat_t: "Cette forme sert à autre chose&nbsp;: à ce qui n'est pas sûr.",
        rat: "«&nbsp;Tu serais venu&nbsp;» parle de quelque chose d'imaginé ou de conditionnel — "
           + "«&nbsp;<i>si je t'avais invité, tu serais venu</i>&nbsp;». Or il est venu pour de "
           + "vrai&nbsp;: le fait est certain, c'est le <b>sentiment de celle qui écrit</b> qui "
           + "commande la forme du verbe, pas un doute." },
    ],
    pourquoi: "«&nbsp;Sois&nbsp;». Gardez la phrase en tête&nbsp;: on y revient au dernier écran, "
            + "dans une situation où elle ne s'écrira plus tout à fait pareil.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-personnes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases entendues cette semaine. Combien de personnes y a-t-il dedans ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Ne regardez pas les verbes&nbsp;: "
            + "comptez les personnes. <b>Celle qui parle fait-elle les deux choses, ou est-ce "
            + "quelqu'un d'autre qui fait la seconde&nbsp;?</b>",
    colonnes: [
      { id: 'une',  t: "Une seule personne", b: "Une seule" },
      { id: 'deux', t: "Deux personnes",     b: "Deux personnes" },
    ],
    items: [
      { txt: "J'ai peur de ne pas réussir l'examen.", sous: "avant un test", ok: 'une',
        rat: "La même personne a peur et passe l'examen. Elle parle d'elle d'un bout à l'autre "
           + "de la phrase.",
        pourquoi: "Elle a peur, et c'est elle qui passe l'examen." },
      { txt: "J'ai peur que l'examen soit trop long.", sous: "avant un test", ok: 'deux',
        rat: "Celle qui a peur, c'est elle&nbsp;; ce qui sera long, c'est l'examen. Deux sujets "
           + "différents dans la même phrase — et remarquez le petit mot qui les sépare.",
        pourquoi: "Elle a peur ; c'est l'examen qui sera long." },
      { txt: "Je suis désolée d'arriver en retard.", sous: "en entrant dans une salle", ok: 'une',
        rat: "Celle qui est désolée est celle qui arrive en retard. Une personne, deux verbes, "
           + "aucun sujet à répéter.",
        pourquoi: "Elle est désolée, et c'est elle qui arrive en retard." },
      { txt: "Je suis désolée que la réunion ait été déplacée.", sous: "un courriel de travail",
        ok: 'deux',
        rat: "Elle est désolée&nbsp;; ce qui a été déplacé, c'est la réunion, et ce n'est pas "
           + "elle qui l'a fait. Deux choses différentes, donc deux sujets.",
        pourquoi: "Elle est désolée ; c'est la réunion qui a bougé." },
      { txt: "Nous sommes heureux de vous accueillir dans le quartier.",
        sous: "une carte des voisins", ok: 'une',
        rat: "Ceux qui sont heureux sont ceux qui accueillent. Le «&nbsp;vous&nbsp;» est celui "
           + "qu'on accueille, pas un second sujet qui ferait une seconde action.",
        pourquoi: "Ceux qui sont heureux sont ceux qui accueillent." },
      { txt: "Nous sommes heureux que vous ayez trouvé un logement.",
        sous: "une carte des voisins", ok: 'deux',
        rat: "Cette fois, celui qui a trouvé le logement, c'est vous&nbsp;; ceux qui sont heureux, "
           + "c'est nous. La joie appartient aux uns, l'action appartient à l'autre.",
        pourquoi: "Nous sommes heureux ; c'est vous qui avez trouvé." },
      { txt: "Je regrette de ne pas pouvoir venir jeudi.", sous: "un texto", ok: 'une',
        rat: "Une seule personne regrette et ne peut pas venir. C'est la façon polie et courte "
           + "de refuser une invitation.",
        pourquoi: "Une personne : elle regrette et ne peut pas venir." },
      { txt: "Je regrette que le cours finisse déjà.", sous: "un mot à l'enseignante", ok: 'deux',
        rat: "Elle regrette&nbsp;; ce qui finit, c'est le cours. Elle n'y peut rien, et c'est "
           + "précisément pour ça qu'il y a deux sujets.",
        pourquoi: "Elle regrette ; c'est le cours qui finit." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous avez trié sans regarder les verbes. Ce sont eux qui suivaient.",
    paras: [
      "Relisez votre colonne «&nbsp;une seule personne&nbsp;»&nbsp;: toutes les phrases y "
      + "enchaînent <b>de</b> + un verbe à l'infinitif — de ne pas réussir, d'arriver, de vous "
      + "accueillir. Dans l'autre colonne, toutes emploient <b>que</b>, suivi d'un nouveau sujet "
      + "et d'un verbe conjugué — que l'examen <i>soit</i>, que vous <i>ayez</i> trouvé, que le "
      + "cours <i>finisse</i>.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> comptez les personnes. Une "
      + "seule&nbsp;? Écrivez <b>de</b> et l'infinitif — c'est la forme la plus courte et elle "
      + "n'a aucun piège. Deux&nbsp;? Écrivez <b>que</b>, et le verbe qui suit prend une forme "
      + "particulière.",

      "Cette forme s'appelle le <b>subjonctif</b>. Elle apparaît uniquement parce que la première "
      + "moitié de la phrase dit un <b>sentiment</b> — content, désolé, heureux, déçu, surpris, "
      + "je regrette, j'ai peur, ça m'étonne. Ce n'est ni un temps du passé ni un temps du "
      + "futur&nbsp;: c'est la forme que réclame le verbe d'avant.",
    ],
    retenir: "Comptez les personnes. <b>Une</b>&nbsp;: «&nbsp;de&nbsp;» + infinitif. "
           + "<b>Deux</b>&nbsp;: «&nbsp;que&nbsp;» + subjonctif.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le premier piège : tout ce qui a un « que » n'en veut pas. ────────
  {
    id:   'esperer',
    type: 'verif',
    eye:  'Le piège du « que »',
    menu: 'Le piège',
    titre: "Farah écrit à sa sœur au sujet d'un entretien d'embauche. Que choisit-elle ?",
    consigne: "Elle veut dire qu'elle souhaite un rappel du bureau. Deux personnes&nbsp;: elle, "
            + "et le bureau.",
    options: [
      { txt: "J'espère qu'ils vont me rappeler cette semaine.", juste: true },
      { txt: "J'espère qu'ils me rappellent cette semaine.",
        rat_t: "Vous avez appliqué la règle des deux personnes — et c'est exactement le piège.",
        rat: "Il y a bien deux personnes et bien un «&nbsp;que&nbsp;». Mais "
           + "<b>«&nbsp;espérer&nbsp;» ne demande pas le subjonctif</b>&nbsp;: espérer, c'est "
           + "compter sur quelque chose, pas ressentir quelque chose. On écrit "
           + "«&nbsp;<i>j'espère qu'ils <b>vont</b> me rappeler</i>&nbsp;», comme on écrirait "
           + "«&nbsp;<i>je pense qu'ils vont me rappeler</i>&nbsp;»." },
      { txt: "J'espère qu'ils me rappelleraient cette semaine.",
        rat_t: "Cette forme suppose une condition qui n'est pas dans la phrase.",
        rat: "«&nbsp;Ils me rappelleraient&nbsp;» appelle un «&nbsp;si&nbsp;» quelque part — "
           + "«&nbsp;<i>si mon dossier était complet, ils me rappelleraient</i>&nbsp;». Farah ne "
           + "pose aucune condition&nbsp;: elle attend un rappel qu'elle croit possible." },
    ],
    pourquoi: "<b>Le sentiment déclenche&nbsp;; l'attente et l'opinion ne déclenchent pas.</b> "
            + "J'espère que, je pense que, je crois que, je trouve que, je suis sûre que&nbsp;: "
            + "verbe ordinaire derrière. Je suis contente que, j'ai peur que, je regrette "
            + "que&nbsp;: subjonctif.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Pourquoi cette frontière-là, et non une autre. ────────────────────
  {
    id:   'sentiment-ou-information',
    type: 'notion',
    eye:  'La deuxième moitié',
    menu: 'La frontière',
    titre: "La frontière n'est pas entre des verbes : elle est entre deux intentions.",
    paras: [
      "Une liste de verbes s'oublie. Ce qui se retient, c'est la question&nbsp;: "
      + "<b>est-ce que j'annonce un fait, ou est-ce que je dis ce qu'il me fait&nbsp;?</b>",

      "Si vous annoncez un fait — pour informer, pour affirmer, pour prévoir — le verbe qui suit "
      + "reste ordinaire&nbsp;: «&nbsp;<i>Je vous confirme que le colis <b>est</b> "
      + "arrivé.</i>&nbsp;» Si vous dites ce que le fait vous fait, il passe au subjonctif&nbsp;: "
      + "«&nbsp;<i>Je suis soulagé que le colis <b>soit</b> arrivé.</i>&nbsp;» Le colis est arrivé "
      + "dans les deux cas — la vérité du fait n'est jamais en cause.",

      "C'est ce qui explique un cas qui déroute tout le monde&nbsp;: le fait peut être "
      + "parfaitement certain et prendre quand même le subjonctif. «&nbsp;<i>Je suis désolé que "
      + "vous <b>ayez</b> attendu.</i>&nbsp;» Vous avez attendu, c'est incontestable. La forme du "
      + "verbe ne dit pas si c'est vrai&nbsp;: elle dit que la phrase parle d'un <b>sentiment</b> "
      + "et non d'une information.",
    ],
    retenir: "Le subjonctif ne dit jamais que le fait est douteux. Il dit que la phrase parle "
           + "d'un <b>sentiment</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Deux choses à vérifier&nbsp;: la première moitié dit-elle un sentiment&nbsp;? Et "
            + "y a-t-il une ou deux personnes&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "Je suis content que tu as trouvé un emploi.", ok: 'faux',
        rat: "Un sentiment, deux personnes&nbsp;: le verbe doit passer au subjonctif — "
           + "«&nbsp;<b>que tu aies trouvé</b>&nbsp;». C'est la faute la plus fréquente, parce "
           + "que «&nbsp;tu as trouvé&nbsp;» est juste dans toutes les autres phrases du monde.",
        pourquoi: "Il faut « que tu aies trouvé »." },
      { txt: "Je suis déçue de ne pas avoir eu la place.", ok: 'ok',
        rat: "Un sentiment, une seule personne&nbsp;: «&nbsp;de&nbsp;» et l'infinitif. Rien à "
           + "corriger, et rien à conjuguer.",
        pourquoi: "Une seule personne : « de » + infinitif. Juste." },
      { txt: "J'ai peur que le propriétaire ne réponde pas avant lundi.", ok: 'ok',
        rat: "Un sentiment, deux personnes, et le verbe au subjonctif. Les deux vérifications "
           + "passent.",
        pourquoi: "Sentiment, deux personnes, subjonctif. Juste." },
      { txt: "Je pense que ce soit une bonne idée.", ok: 'faux',
        rat: "Ici, c'est l'inverse&nbsp;: «&nbsp;je pense&nbsp;» donne une opinion, pas un "
           + "sentiment, donc pas de subjonctif — «&nbsp;<b>que c'est</b> une bonne idée&nbsp;». "
           + "C'est la faute de ceux qui viennent de comprendre la règle et l'appliquent partout.",
        pourquoi: "« Je pense » ne déclenche rien : « que c'est »." },
      { txt: "Nous sommes heureux que vous puissiez venir.", ok: 'ok',
        rat: "Un sentiment, deux personnes, et «&nbsp;puissiez&nbsp;» est bien la forme demandée. "
           + "C'est la phrase des invitations, et elle est correcte.",
        pourquoi: "Sentiment, deux personnes, subjonctif. Juste." },
      { txt: "Je suis surpris que vous n'avez pas reçu l'avis.", ok: 'faux',
        rat: "Un sentiment, deux personnes&nbsp;: «&nbsp;<b>que vous n'ayez pas reçu</b>&nbsp;». "
           + "Le fait est pourtant certain — vous n'avez rien reçu — et cela ne change rien&nbsp;: "
           + "c'est la surprise qui commande, pas le doute.",
        pourquoi: "Il faut « que vous n'ayez pas reçu »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce qu'on écrit, et à qui. ─────────────────────────────────────────
  {
    id:   'ce-quon-ecrit',
    type: 'verif',
    eye:  'Vérification',
    menu: "À l'écrit",
    titre: "Vous répondez à une cliente dont la commande est arrivée abîmée.",
    consigne: "Vous voulez vous excuser, puis annoncer ce que vous allez faire. Deux phrases, "
            + "deux intentions différentes.",
    options: [
      { txt: "«&nbsp;Je suis désolée que votre commande soit arrivée abîmée. Je vous confirme "
           + "qu'un remplacement part aujourd'hui.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Je suis désolée que votre commande est arrivée abîmée. Je vous confirme "
           + "qu'un remplacement part aujourd'hui.&nbsp;»",
        rat_t: "La seconde phrase est parfaite. C'est l'excuse qui manque sa forme.",
        rat: "«&nbsp;Je vous confirme que… part&nbsp;» est exactement juste&nbsp;: on annonce un "
           + "fait. Mais «&nbsp;je suis désolée&nbsp;» est un sentiment, avec deux personnes "
           + "derrière — il faut «&nbsp;<b>soit arrivée</b>&nbsp;». Dans une excuse écrite à une "
           + "cliente, c'est la phrase qu'elle lira en premier." },
      { txt: "«&nbsp;Je suis désolée que votre commande soit arrivée abîmée. Je vous confirme "
           + "qu'un remplacement parte aujourd'hui.&nbsp;»",
        rat_t: "L'excuse est réglée. C'est la promesse qui a pris la forme de trop.",
        rat: "Vous avez le plus difficile&nbsp;: «&nbsp;soit arrivée&nbsp;» après le sentiment. "
           + "Mais «&nbsp;je vous confirme&nbsp;» annonce un fait — le colis part, c'est une "
           + "information, pas une émotion. Un subjonctif là rend la promesse floue, comme si le "
           + "départ n'était pas décidé." },
    ],
    pourquoi: "<b>Deux phrases côte à côte, deux formes différentes, et c'est normal&nbsp;:</b> "
            + "on s'excuse d'abord, on informe ensuite. C'est la structure de presque tous les "
            + "courriels de service.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. La conjugaison, dite en dernier : c'est la partie mécanique. ──────
  {
    id:   'la-forme-en-dernier',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'La fabrication',
    titre: "La forme se fabrique à partir d'un verbe que vous employez tous les jours.",
    paras: [
      "Prenez le verbe avec <b>ils</b>, au présent, enlevez «&nbsp;-ent&nbsp;», ajoutez la "
      + "terminaison. Ils finiss<i>ent</i> → que je finiss<b>e</b>, que tu finiss<b>es</b>, qu'il "
      + "finiss<b>e</b>, qu'ils finiss<b>ent</b>. Ils écriv<i>ent</i> → que j'écriv<b>e</b>. Ils "
      + "répond<i>ent</i> → que je répond<b>e</b>. Pour <i>nous</i> et <i>vous</i>, c'est la forme "
      + "de l'imparfait&nbsp;: que nous finiss<b>ions</b>, que vous finiss<b>iez</b>.",

      "<b>Six verbes</b> ne suivent pas, et ce sont ceux qui reviennent partout&nbsp;: que je "
      + "<b>sois</b>, que j'<b>aie</b>, que je <b>fasse</b>, que j'<b>aille</b>, que je "
      + "<b>puisse</b>, que je <b>sache</b>. Six, pas trente.",

      "Un détail qui évite bien des ratures&nbsp;: au passé, on ne change pas de temps, on met "
      + "seulement l'auxiliaire au subjonctif. «&nbsp;<i>Tu es venu</i>&nbsp;» → «&nbsp;<i>que tu "
      + "<b>sois</b> venu</i>&nbsp;». «&nbsp;<i>Vous avez attendu</i>&nbsp;» → «&nbsp;<i>que vous "
      + "<b>ayez</b> attendu</i>&nbsp;». Le participe, lui, ne bouge pas.",
    ],
    retenir: "Le radical de <b>ils</b> + -e, -es, -e, -ions, -iez, -ent, et six irréguliers. La "
           + "difficulté n'a jamais été la forme&nbsp;: c'est de savoir <b>quand</b> elle est "
           + "demandée.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Un message à votre enseignante. Quelle version tient d'un bout à l'autre ?",
    consigne: "Kwame est content d'avoir réussi son examen, il regrette que le cours se termine, "
            + "et il pense revenir à la session d'automne. Trois versions&nbsp;: une seule est "
            + "correcte partout.",
    options: [
      { txt: "Je suis content d'avoir réussi l'examen. Je regrette que le cours se termine, mais "
           + "je pense que je reviendrai à l'automne.",
        juste: true },
      { txt: "Je suis content que j'aie réussi l'examen. Je regrette que le cours se termine, "
           + "mais je pense que je reviendrai à l'automne.",
        rat_t: "Les deux dernières sont justes. C'est la première qui se complique pour rien.",
        rat: "«&nbsp;Que le cours se termine&nbsp;» et «&nbsp;que je reviendrai&nbsp;» sont "
           + "exactement à leur place. Mais dans la première, c'est <b>la même personne</b> qui "
           + "est contente et qui a réussi&nbsp;: on écrit alors «&nbsp;<b>d'avoir "
           + "réussi</b>&nbsp;». La règle des deux personnes sert aussi à s'éviter du travail." },
      { txt: "Je suis content d'avoir réussi l'examen. Je regrette que le cours se termine, mais "
           + "je pense que je revienne à l'automne.",
        rat_t: "Les deux premières sont justes. C'est la troisième qui a pris la forme de trop.",
        rat: "Vous avez réglé le plus difficile&nbsp;: l'infinitif après «&nbsp;content&nbsp;», "
           + "le subjonctif après «&nbsp;je regrette&nbsp;». Reste "
           + "«&nbsp;je pense que&nbsp;»&nbsp;: c'est une opinion, pas un sentiment — "
           + "«&nbsp;<b>que je reviendrai</b>&nbsp;»." },
    ],
    pourquoi: "Une personne&nbsp;: infinitif. Deux personnes et un sentiment&nbsp;: subjonctif. "
            + "Une opinion&nbsp;: verbe ordinaire. <b>C'est tout le point en trois phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au début : « Je suis contente que tu sois venu. »",
    consigne: "Cette fois, ce n'est plus un texto à un ami&nbsp;: vous écrivez à une collègue "
            + "pour la remercier d'être passée à votre présentation. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "«&nbsp;Je suis heureuse que vous ayez pu assister à la présentation.&nbsp;»",
        juste: true },
      { txt: "«&nbsp;Je suis heureuse que vous avez pu assister à la présentation.&nbsp;»",
        rat_t: "Le ton est bon&nbsp;; c'est la forme du verbe qui a suivi l'habitude.",
        rat: "Le vouvoiement et la formule sont exactement ceux d'un courriel de travail. Mais "
           + "«&nbsp;je suis heureuse&nbsp;» reste un sentiment, et il y a deux personnes&nbsp;: "
           + "«&nbsp;<b>que vous ayez pu</b>&nbsp;». C'est la même phrase que celle de l'écran 1, "
           + "avec un autre pronom." },
      { txt: "«&nbsp;Je suis heureuse d'avoir pu assister à la présentation.&nbsp;»",
        rat_t: "La forme est irréprochable — mais elle remercie la mauvaise personne.",
        rat: "Rien n'est faux&nbsp;: une seule personne, «&nbsp;de&nbsp;» et l'infinitif. Sauf que "
           + "cette phrase dit que <b>vous</b> avez assisté à la présentation, alors que c'est "
           + "votre collègue qui est venue à la vôtre. Compter les personnes ne sert pas qu'à "
           + "conjuguer&nbsp;: ça décide aussi de qui fait quoi." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: reconnaître un sentiment, compter les "
            + "personnes, et écrire la forme que la phrase demandait — dans un message que "
            + "quelqu'un va lire.",
    attente: "Choisissez une réponse pour finir.",
  },

];
