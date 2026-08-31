// ═══════════════════════════════════════════════════════════════════════════
// Point express — Désigner sans redire le nom, et sans pointer du doigt
//
// Savoir n4-s25 (Pronoms démonstratifs) : « accorder en genre et en nombre les
// pronoms démonstratifs complexes — Je vais prendre celui-là », « associer des
// pronoms démonstratifs complexes déictiques à leur référent — Ceux-là, les
// aimez-vous ? ». Une ORDONNANCE : l'enseignant l'envoie à un élève qui dit
// « je prends celui » tout court, ou qui écrit « ce que j'ai visité hier » là
// où il faut « celui que ».
//
// ── Ce qui le sépare de ce qui existe déjà ─────────────────────────────────
// L'étagère porte « ce, cet, cette — trois mots, un seul son » (niveau 3),
// qui traite les DÉTERMINANTS : les mots qui accompagnent un nom. Ce point-ci
// traite les mots qui le REMPLACENT. Ce n'est pas la suite du même sujet,
// c'est le geste inverse, et c'est précisément là que l'élève se perd.
//
// Cinq mini-leçons existent : « Celui, celle, ceux », « Celui, celle, ceux,
// celles — et ce qui suit », « Ce modèle-ci, celui-là », « À quoi renvoie
// "celui-ci" ? », « Un matelas en général, ou ce matelas-là ». Toutes donnent
// le TABLEAU DES QUATRE FORMES (celui / celle / ceux / celles), suivi des
// suffixes -ci et -là. Un élève qui les a lues récite le tableau et dit quand
// même « je prends celui » — parce que le tableau ne dit pas la seule chose qui
// compte : que ce mot ne se tient jamais debout tout seul.
//
// Les cinq écarts tenus :
//
//   1. INDUCTIF. Écran 2 : huit phrases à trou, à ranger selon qu'un nom est
//      écrit après le trou ou non. Aucune règle avant l'écran 3.
//   2. UN TEST, PAS UN TABLEAU. « Le nom est-il écrit juste après ? » Oui →
//      ce / cette. Non → celui / celle. Le test marche sur un nom jamais vu.
//   3. LA VRAIE FAUTE EST TRAITÉE COMME LE SUJET : ce mot est toujours suivi
//      de quelque chose — « -là », « de… », « qui… ». Trois écrans y passent.
//   4. LE MÉTALANGAGE ARRIVE APRÈS, à l'écran 3, une fois la chose triée huit
//      fois. Le tableau des quatre formes n'est donné qu'à l'écran 5, et
//      seulement comme une question d'accord.
//   5. EXEMPLES VARIÉS : un rayon de quincaillerie, deux logements visités, un
//      classeur de bureau, une bibliothèque, un texto entre sœurs.
//
// Aucun média : « celui » et « ceux » se distinguent mal à l'oreille pour un
// apprenant, mais ce point porte sur l'écrit et sur le choix — pas sur
// l'écoute. Un point de graphie-phonie serait un autre point express.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'celui-celle-ceux',
  titre:    "Désigner sans redire le nom, et sans pointer du doigt",
  surtitre: "Point express · 10 minutes",
  niveau:   4,
  savoir:   'n4-s25',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Au comptoir',
    titre: "Trois modèles de balais sur le comptoir. Le commis : « Lequel vous voulez ? »",
    consigne: "Vous voulez celui du milieu, et vous ne connaissez pas son nom. Répondez avec ce "
            + "que vous savez déjà — ou au feeling. On expliquera après&nbsp;: c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Celui-là, s'il vous plaît.&nbsp;»", juste: true },
      { txt: "«&nbsp;Celui, s'il vous plaît.&nbsp;»",
        rat_t: "C'est la faute que ce point vient corriger, et elle est très fréquente.",
        rat: "Le mot est le bon. Mais il ne peut pas rester seul&nbsp;: il annonce toujours "
           + "quelque chose derrière lui — «&nbsp;celui-<b>là</b>&nbsp;», «&nbsp;celui "
           + "<b>du milieu</b>&nbsp;», «&nbsp;celui <b>que vous m'avez montré</b>&nbsp;». "
           + "Employé tout seul, il laisse le commis attendre la suite de votre phrase." },
      { txt: "«&nbsp;Ce-là, s'il vous plaît.&nbsp;»",
        rat_t: "Vous avez pris le mot qui accompagne un nom, sans mettre le nom.",
        rat: "«&nbsp;Ce&nbsp;» ne voyage jamais sans un nom collé derrière&nbsp;: "
           + "«&nbsp;<b>ce balai</b>-là&nbsp;». Si vous ne dites pas le nom, il vous faut "
           + "l'autre mot, celui qui prend la place du nom." },
    ],
    pourquoi: "«&nbsp;Celui-là.&nbsp;» Gardez la scène en tête&nbsp;: on y revient au dernier "
            + "écran.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. ──────────────────────────────────────────
  {
    id:   'tri-huit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit trous',
    titre: "Huit phrases à trou. Faut-il un mot qui accompagne le nom, ou un mot qui le remplace ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Regardez seulement ce qui vient "
            + "<b>juste après le trou</b>&nbsp;: y a-t-il un nom, oui ou non&nbsp;?",
    colonnes: [
      { id: 'avec', t: "Un nom suit : ce, cette, ces", b: "ce, cette, ces" },
      { id: 'sans', t: "Pas de nom : celui, celle, ceux", b: "celui, celle, ceux" },
    ],
    items: [
      { txt: "___ manteau-là est trop grand pour moi.", sous: "dans une friperie", ok: 'avec',
        rat: "Le nom «&nbsp;manteau&nbsp;» est écrit juste après le trou&nbsp;: il faut donc "
           + "le mot qui l'accompagne, pas celui qui le remplace.",
        pourquoi: "« manteau » est écrit : ce manteau-là." },
      { txt: "Je préfère ___ que j'ai essayé hier.", sous: "la même friperie, dix secondes après", ok: 'sans',
        rat: "Le manteau vient d'être nommé dans la phrase d'avant&nbsp;: on ne le redit pas. "
           + "Après le trou, il n'y a pas de nom — il y a un verbe.",
        pourquoi: "Aucun nom après : celui que j'ai essayé." },
      { txt: "Prenez ___ formulaire et remplissez-le.", sous: "au comptoir d'un centre", ok: 'avec',
        rat: "«&nbsp;Formulaire&nbsp;» suit le trou. Le nom est là, le mot qui l'accompagne "
           + "aussi.",
        pourquoi: "Le nom suit : ce formulaire." },
      { txt: "Le dossier de mon mari et ___ de ma fille sont prêts.", sous: "une clinique", ok: 'sans',
        rat: "«&nbsp;Dossier&nbsp;» a déjà été dit une fois&nbsp;; le répéter alourdirait la "
           + "phrase. Après le trou vient «&nbsp;de ma fille&nbsp;», pas un nom.",
        pourquoi: "On ne redit pas « dossier » : celui de ma fille." },
      { txt: "___ appartement-ci donne sur la ruelle.", sous: "une visite de logement", ok: 'avec',
        rat: "Le nom est collé au trou. Attention seulement à l'écriture&nbsp;: devant une "
           + "voyelle, le mot qui accompagne change de forme — c'est un autre sujet.",
        pourquoi: "Le nom suit : cet appartement-ci." },
      { txt: "Des deux logements, je garde ___ qui a un balcon.", sous: "un texto à sa sœur", ok: 'sans',
        rat: "Après le trou vient «&nbsp;qui a un balcon&nbsp;»&nbsp;: une description, pas un "
           + "nom. Le mot remplace «&nbsp;logement&nbsp;», déjà dit au début de la phrase.",
        pourquoi: "Pas de nom, une description : celui qui…" },
      { txt: "___ chaussures-là me font mal.", sous: "un magasin", ok: 'avec',
        rat: "«&nbsp;Chaussures&nbsp;» suit le trou. Le pluriel ne change rien au tri&nbsp;: la "
           + "question reste «&nbsp;y a-t-il un nom&nbsp;?&nbsp;»",
        pourquoi: "Le nom suit : ces chaussures-là." },
      { txt: "Mes clés sont là, mais je ne trouve pas ___ de la boîte aux lettres.", sous: "dans une entrée", ok: 'sans',
        rat: "Celui-là trompe, parce qu'il y a bien un nom dans la phrase — «&nbsp;boîte aux "
           + "lettres&nbsp;». Mais ce nom-là appartient à «&nbsp;de&nbsp;», pas au trou. Juste "
           + "après le trou, il n'y a rien à accompagner.",
        pourquoi: "« de la boîte » suit : celle de la boîte." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat. ────────────────────────────────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas cherché le sens. Vous avez regardé un seul endroit.",
    paras: [
      "Vous avez regardé <b>juste après le trou</b>. Un nom&nbsp;? Alors le mot accompagne "
      + "— <b>ce</b>, <b>cette</b>, <b>ces</b>. Pas de nom&nbsp;? Alors le mot remplace — "
      + "<b>celui</b>, <b>celle</b>, <b>ceux</b>, <b>celles</b>. Vous n'avez pas eu besoin de "
      + "savoir de quoi parlait la phrase.",

      "Ces mots-là s'appellent des <b>pronoms démonstratifs</b>&nbsp;: ils tiennent la place "
      + "d'un nom pour qu'on ne le redise pas trois fois de suite. Votre enseignant emploiera "
      + "le nom&nbsp;; vous n'en avez pas besoin pour vous en servir.",

      "Et il y a une seconde chose, que vous avez peut-être remarquée sans y penser&nbsp;: "
      + "dans les quatre phrases de votre colonne, le mot était toujours <b>suivi de quelque "
      + "chose</b> — «&nbsp;que j'ai essayé&nbsp;», «&nbsp;de ma fille&nbsp;», «&nbsp;qui a un "
      + "balcon&nbsp;». Jamais seul. C'est l'écran suivant.",
    ],
    retenir: "Un nom juste après&nbsp;? → <b>ce, cette, ces</b>. Pas de nom&nbsp;? → "
           + "<b>celui, celle, ceux, celles</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. La vraie faute : le mot laissé seul. ──────────────────────────────
  {
    id:   'jamais-seul',
    type: 'verif',
    eye:  'Le défaut à corriger',
    menu: 'Jamais seul',
    titre: "Au bureau, une collègue demande : « Quel dossier je te sors ? »",
    consigne: "Vous voulez le dossier de madame Roy. Trois réponses&nbsp;: une seule est une "
            + "phrase complète.",
    options: [
      { txt: "«&nbsp;Celui de madame Roy.&nbsp;»", juste: true },
      { txt: "«&nbsp;Celui, madame Roy.&nbsp;»",
        rat_t: "Le mot est resté seul, et la phrase se casse en deux.",
        rat: "Votre collègue entend un mot qui annonce une suite, puis un nom de personne sans "
           + "lien avec lui — elle peut croire que vous vous adressez à madame Roy. Le petit "
           + "mot «&nbsp;<b>de</b>&nbsp;» est ce qui rattache les deux moitiés." },
      { txt: "«&nbsp;Celui-là de madame Roy.&nbsp;»",
        rat_t: "Vous avez mis deux suites au lieu d'une.",
        rat: "«&nbsp;-là&nbsp;» sert à <b>montrer</b> quelque chose qu'on a devant soi&nbsp;; "
           + "«&nbsp;de madame Roy&nbsp;» sert à <b>préciser</b> lequel. Il en faut une, pas "
           + "les deux&nbsp;: le dossier n'est pas sur la table, donc c'est la précision qui "
           + "s'impose." },
    ],
    pourquoi: "Ce mot est toujours suivi de <b>l'une de ces trois choses</b>&nbsp;: "
            + "«&nbsp;-là&nbsp;» ou «&nbsp;-ci&nbsp;», «&nbsp;de…&nbsp;», ou "
            + "«&nbsp;qui / que…&nbsp;». Jamais rien d'autre, jamais rien de moins.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. L'accord, et où le lire. ──────────────────────────────────────────
  {
    id:   'laccord',
    type: 'notion',
    eye:  "L'accord",
    menu: 'Quatre formes',
    titre: "Le mot prend la forme de la chose qu'il remplace, jamais celle de qui parle.",
    paras: [
      "Quatre formes, et elles se lisent dans le nom qu'on ne dit pas&nbsp;: un dossier → "
      + "<b>celui</b>&nbsp;; une clé → <b>celle</b>&nbsp;; des dossiers → <b>ceux</b>&nbsp;; "
      + "des clés → <b>celles</b>. Un homme qui parle de sa clé dit «&nbsp;celle-là&nbsp;», "
      + "une femme qui parle de son dossier dit «&nbsp;celui-là&nbsp;».",

      "<b>Comment retrouver la forme quand on hésite&nbsp;:</b> redites mentalement le nom "
      + "avec son petit mot. «&nbsp;<i>La</i> facture&nbsp;» → <b>celle</b> de mars. "
      + "«&nbsp;<i>Les</i> reçus&nbsp;» → <b>ceux</b> de l'an dernier. Le petit mot du nom et "
      + "la forme du pronom vont toujours ensemble.",

      "Le piège est ailleurs, et il est fréquent&nbsp;: on emploie ces mots quand le nom vient "
      + "d'être dit — donc <b>plusieurs phrases plus haut</b>. Il faut remonter le chercher. "
      + "Si vous ne le retrouvez pas en deux secondes, votre lecteur non plus&nbsp;: écrivez le "
      + "nom.",
    ],
    retenir: "La forme se lit dans le nom remplacé&nbsp;: <i>la</i> facture → <b>celle</b>, "
           + "<i>les</i> reçus → <b>ceux</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites. ────────────────────────────────────────
  {
    id:   'tri-ecrites',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Lesquelles tiennent ?",
    consigne: "Trois choses&nbsp;: le mot remplace-t-il bien un nom absent, est-il suivi de "
            + "quelque chose, et est-il de la bonne forme&nbsp;?",
    colonnes: [
      { id: 'ok',   t: 'Correcte',  b: 'Correcte' },
      { id: 'faux', t: 'Une faute', b: 'Une faute' },
    ],
    items: [
      { txt: "J'ai deux factures : celle de mars est payée.", ok: 'ok',
        rat: "Le nom est dit une fois, puis remplacé. Le mot est au féminin comme "
           + "«&nbsp;facture&nbsp;», et il est suivi de «&nbsp;de mars&nbsp;».",
        pourquoi: "Féminin, et suivi de « de mars »." },
      { txt: "Prenez ce formulaire-là, pas celui.", ok: 'faux',
        rat: "La première moitié est parfaite. Dans la seconde, le mot est resté seul&nbsp;: "
           + "on ne sait pas lequel vous écartez. Il faut «&nbsp;pas celui<b>-ci</b>&nbsp;» ou "
           + "«&nbsp;pas celui <b>du dessus</b>&nbsp;».",
        pourquoi: "Le mot est seul : il lui faut une suite." },
      { txt: "Les élèves d'hier et ceux d'aujourd'hui ont le même exercice.", ok: 'ok',
        rat: "Pluriel des deux côtés, et le mot est suivi de «&nbsp;d'aujourd'hui&nbsp;». On "
           + "évite de répéter «&nbsp;élèves&nbsp;» sans rien perdre.",
        pourquoi: "Pluriel, suivi de « d'aujourd'hui »." },
      { txt: "Ma sœur a visité deux appartements ; elle a pris celle du deuxième étage.", ok: 'faux',
        rat: "Le mot est bien suivi, et la phrase se comprend&nbsp;: c'est la forme qui "
           + "cloche. Le mot remplace «&nbsp;appartement&nbsp;», pas «&nbsp;ma sœur&nbsp;» — "
           + "donc <b>celui</b>. La forme suit la chose, jamais la personne.",
        pourquoi: "Il remplace « appartement » : celui." },
      { txt: "Je cherche mes clés. Celles de l'auto sont sur la table.", ok: 'ok',
        rat: "Le nom est dans la phrase d'avant, et le lecteur le retrouve sans effort. "
           + "Féminin pluriel des deux côtés.",
        pourquoi: "Le nom est juste au-dessus : rien à corriger." },
      { txt: "Cette boîte est à moi, celui-là est à mon voisin.", ok: 'faux',
        rat: "Les deux moitiés parlent de boîtes, et la première le dit au féminin. La seconde "
           + "aurait dû suivre&nbsp;: «&nbsp;<b>celle</b>-là&nbsp;». C'est l'accord le plus "
           + "souvent raté, parce qu'on n'entend pas la différence quand on relit vite.",
        pourquoi: "Une boîte, donc celle-là." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Choisir la suite : « de » ou « qui / que ». ───────────────────────
  {
    id:   'la-suite',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Quelle suite',
    titre: "À la bibliothèque : « Quel livre je vous réserve ? »",
    consigne: "Vous parlez du livre <b>que la bibliothécaire vous a montré la semaine "
            + "dernière</b>. Vous ne connaissez ni son titre ni son auteur.",
    options: [
      { txt: "«&nbsp;Celui que vous m'aviez montré la semaine dernière.&nbsp;»", juste: true },
      { txt: "«&nbsp;Celui de vous m'aviez montré la semaine dernière.&nbsp;»",
        rat_t: "Vous avez pris la suite qui sert à nommer, devant une suite qui décrit.",
        rat: "«&nbsp;De&nbsp;» s'emploie devant un <b>nom</b>&nbsp;: celui <i>de</i> madame "
           + "Roy, celui <i>du</i> deuxième étage. Devant un <b>verbe</b>, il faut "
           + "«&nbsp;qui&nbsp;» ou «&nbsp;que&nbsp;»&nbsp;: celui <i>que</i> vous m'aviez "
           + "montré." },
      { txt: "«&nbsp;Celui-là que vous m'aviez montré la semaine dernière.&nbsp;»",
        rat_t: "Une suite de trop, et elle vous fait montrer du doigt un livre absent.",
        rat: "«&nbsp;-là&nbsp;» sert quand la chose est devant vous. Le livre est rangé "
           + "quelque part&nbsp;: vous ne pouvez pas le montrer, vous ne pouvez que le "
           + "décrire. Une seule suite à la fois." },
    ],
    pourquoi: "Un <b>nom</b> derrière&nbsp;→ «&nbsp;de&nbsp;». Un <b>verbe</b> "
            + "derrière&nbsp;→ «&nbsp;qui&nbsp;» ou «&nbsp;que&nbsp;». La chose devant "
            + "vous&nbsp;→ «&nbsp;-là&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. « -ci » et « -là », dits en dernier : c'est de l'usage. ───────────
  {
    id:   'ci-et-la',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: '-ci et -là',
    titre: "Au Québec, on dit « -là » presque tout le temps.",
    paras: [
      "On a gardé ceci pour la fin parce que ce n'est pas une règle de grammaire, c'est un "
      + "usage — et il vaut mieux le connaître que l'apprendre par cœur. À l'oral, "
      + "«&nbsp;celui-là&nbsp;», «&nbsp;celle-là&nbsp;», «&nbsp;ceux-là&nbsp;» servent pour "
      + "tout ce qu'on montre, proche ou loin. «&nbsp;Celui-ci&nbsp;» est rare dans la "
      + "conversation.",

      "Vous n'avez donc <b>pas</b> à choisir entre les deux quand vous parlez&nbsp;: prenez "
      + "«&nbsp;-là&nbsp;» et vous serez juste. Ce qui distingue deux objets, c'est le geste "
      + "et le regard, pas le suffixe — «&nbsp;<i>celui-là, à côté du bleu</i>&nbsp;».",

      "À l'écrit, en revanche, la paire redevient utile parce qu'il n'y a plus de doigt pour "
      + "montrer&nbsp;: «&nbsp;<i>J'ai reçu deux avis. <b>Celui-ci</b> concerne le loyer, "
      + "<b>celui-là</b> l'électricité.</i>&nbsp;» «&nbsp;Celui-ci&nbsp;» désigne alors le "
      + "dernier nommé, «&nbsp;celui-là&nbsp;» le premier — et si la phrase devient difficile "
      + "à suivre, <b>écrivez les noms</b>&nbsp;: la clarté passe avant l'élégance.",
    ],
    retenir: "À l'oral&nbsp;: «&nbsp;-là&nbsp;» partout. À l'écrit&nbsp;: les deux servent, et "
           + "quand ça devient confus, on redit le nom.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'votre-message',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Deux logements',
    titre: "Vous écrivez à votre sœur après deux visites. Quelle version tient d'un bout à l'autre ?",
    consigne: "Le logement de la rue Bélanger a un balcon&nbsp;; celui de la rue Fabre est plus "
            + "grand. Vous gardez le premier.",
    options: [
      { txt: "«&nbsp;J'ai visité deux logements. Je garde celui qui a un balcon, pas celui de "
           + "la rue Fabre.&nbsp;»", juste: true },
      { txt: "«&nbsp;J'ai visité deux logements. Je garde celui a un balcon, pas celui rue "
           + "Fabre.&nbsp;»",
        rat_t: "Les deux suites manquent, et ce ne sont pas les mêmes.",
        rat: "Devant un verbe, il faut «&nbsp;<b>qui</b> a un balcon&nbsp;». Devant un nom, il "
           + "faut «&nbsp;<b>de</b> la rue Fabre&nbsp;». Sans ces deux petits mots, les deux "
           + "moitiés de chaque phrase ne tiennent plus ensemble." },
      { txt: "«&nbsp;J'ai visité deux logements. Je garde celle qui a un balcon, pas celui-là "
           + "de la rue Fabre.&nbsp;»",
        rat_t: "Une forme et une suite en trop.",
        rat: "«&nbsp;Logement&nbsp;» est masculin&nbsp;: <b>celui</b> qui a un balcon. Et "
           + "«&nbsp;celui-là de la rue Fabre&nbsp;» empile deux suites&nbsp;: votre sœur n'a "
           + "rien devant les yeux, donc «&nbsp;<b>celui de</b> la rue Fabre&nbsp;» suffit." },
    ],
    pourquoi: "Une forme prise sur le nom, une suite par pronom, et le nom dit une seule fois. "
            + "<b>C'est tout le point en deux phrases.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1. ──────────────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au comptoir, avec les trois balais.",
    consigne: "Cette fois, ce n'est plus vous qui montrez&nbsp;: vous téléphonez au magasin pour "
            + "faire mettre de côté celui du milieu, le seul qui a un manche en bois.",
    options: [
      { txt: "«&nbsp;Je voudrais celui qui a un manche en bois.&nbsp;»", juste: true },
      { txt: "«&nbsp;Je voudrais celui-là.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle était parfaite là-bas.",
        rat: "Rien n'est faux dedans. Mais «&nbsp;-là&nbsp;» montre du doigt, et vous êtes au "
           + "téléphone&nbsp;: le commis ne voit pas votre main. La suite doit devenir une "
           + "description — «&nbsp;celui <b>qui</b>…&nbsp;»." },
      { txt: "«&nbsp;Je voudrais celui de manche en bois.&nbsp;»",
        rat_t: "La bonne intention, la mauvaise suite.",
        rat: "Vous avez bien vu qu'il fallait décrire l'objet. Mais «&nbsp;de&nbsp;» annonce un "
           + "nom qui <b>appartient</b> ou qui <b>situe</b> — celui de madame Roy, celui du "
           + "deuxième étage. Pour décrire une pièce de l'objet, on emploie un verbe&nbsp;: "
           + "«&nbsp;celui <b>qui a</b> un manche en bois&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: remplacer le nom au lieu de le redire, "
            + "prendre la forme sur la chose, et choisir la suite selon la situation.",
    attente: "Choisissez une réponse pour finir.",
  },

];
