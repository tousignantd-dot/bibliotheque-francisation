// ═══════════════════════════════════════════════════════════════════════════
// Point express — Les phrases avec « si » : trois façons, trois temps
//
// Savoirs n8-s11, n8-s12 et n8-s13 (Phrase · Jonction de phrases). Le
// programme cadre lui-même le point par ses trois exemples : « Si tu étais un
// fan de hockey, tu ne serais pas allé au cinéma hier », « Si cette entreprise
// était restée ici, l'économie de la ville se porterait mieux », « Si
// l'entreprise était restée ici, on n'aurait pas perdu d'emplois ».
// Une ORDONNANCE : dix minutes, dix écrans. C'est LA difficulté du niveau 8.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Cinq mini-leçons du dépôt traitent déjà « si » — trois au niveau 6
// (`module-n6-etablissement`, `module-n6-emploi`, `module-n6-oeuvres` :
// « Poser une condition avec si »), une au niveau 6 sur l'hypothèse
// (`module-n6-actualite`), et surtout `module-n8-habitation`, « L'hypothèse
// irréelle, l'arme tranquille », qui donne les deux montages en tableau, la
// condition sans « si », le gérondif, l'infinitif. Un élève envoyé ici l'a lue,
// et il refait quand même la faute. Les cinq écarts tenus :
//
//   1. INDUCTIF. L'élève range huit phrases selon CE QU'ELLES VEULENT DIRE —
//      encore possible, plus le cas, trop tard — AVANT qu'un seul nom de temps
//      soit prononcé. La mini-leçon du niveau 8 ouvre sur « si + imparfait,
//      conditionnel présent » ; ici, ces mots n'arrivent qu'à l'écran 5.
//   2. PARTIEL, JAMAIS LA LISTE. Aucun tableau des trois montages en tête.
//      Un TEST unique — regarder le verbe qui suit « si », et rien d'autre —
//      qui tranche les trois cas sur une phrase jamais vue. La condition sans
//      « si » (gérondif, infinitif), que la mini-leçon détaille, n'est pas
//      traitée : elle sert à écrire du soutenu, pas à sortir de la faute.
//   3. LE SENS D'ABORD, LE MONTAGE ENSUITE. Le fil du point n'est pas
//      grammatical : ce qui est encore possible, ce qui ne l'est plus, et le
//      regret. Un élève qui ne sait pas ce qu'il veut dire ne choisira jamais
//      le bon temps, même en connaissant le tableau par cœur.
//   4. LE « SI » QUI N'EST PAS UNE CONDITION EST DIT EN DERNIER (écran 8).
//      Le nommer d'entrée ferait croire à une règle de plus.
//   5. EXEMPLES VARIÉS, JAMAIS CEUX D'UN MODULE. Un texto à un ami, une
//      demande à un employeur, un mot à une enseignante, une conversation de
//      corridor. L'élève doit reconnaître le montage partout.
//
// Aucun média : « si j'avais su » et « si j'aurais su » se distinguent à
// l'oreille, mais la faute se fabrique dans la tête, pas dans l'oreille — et
// elle se corrige en comparant deux phrases écrites côte à côte.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'les-phrases-avec-si',
  titre:    "« Si… » : trois façons, trois temps",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s11 · n8-s12 · n8-s13',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois versions',
    titre: "Trois versions de la même idée. Laquelle dit qu'il est trop tard ?",
    consigne: "Répondez avec ce que vous savez déjà — ou au feeling. On expliquera après&nbsp;: "
            + "c'est fait exprès.",
    options: [
      { txt: "«&nbsp;Si j'avais su, je serais venu.&nbsp;»", juste: true },
      { txt: "«&nbsp;Si je sais, je viens.&nbsp;»",
        rat_t: "Celle-là ouvre la porte, elle ne la ferme pas.",
        rat: "Elle est tentante parce qu'elle est la plus simple des trois. Mais elle parle de la "
           + "<b>prochaine fois</b>&nbsp;: si on me le dit, je viendrai. Rien n'est terminé, tout "
           + "est encore possible." },
      { txt: "«&nbsp;Si je savais, je viendrais.&nbsp;»",
        rat_t: "Celle-là parle d'aujourd'hui, pas d'hier.",
        rat: "Elle dit&nbsp;: en ce moment, je ne sais pas — et tant que je ne saurai pas, je ne "
           + "viendrai pas. C'est un constat sur maintenant. Rien n'est encore fini&nbsp;: il "
           + "suffirait qu'on me le dise." },
    ],
    pourquoi: "La première. Gardez-la en tête&nbsp;: on revient dessus à la fin, et vous verrez "
            + "ce que les trois font exactement.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. C'est ici que le point se sépare. ────────
  {
    id:   'tri-sens',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Huit phrases',
    titre: "Huit phrases avec « si ». Qu'est-ce que chacune dit vraiment ?",
    consigne: "Aucune règle ne vous a été donnée — normal, et aucun nom de temps ne vous servirait "
            + "ici. Demandez-vous seulement&nbsp;: est-ce que ça peut encore arriver&nbsp;?",
    colonnes: [
      { id: 'poss',  t: "Ça peut encore arriver",    b: "Encore possible" },
      { id: 'auj',   t: "Ce n'est pas le cas aujourd'hui", b: "Pas le cas aujourd'hui" },
      { id: 'tard',  t: "C'est passé, c'est trop tard", b: "Trop tard" },
    ],
    items: [
      { txt: "Si tu finis avant six heures, appelle-moi.", sous: "un texto, en fin d'après-midi",
        ok: 'poss',
        rat: "Il n'est pas six heures. La personne peut très bien finir à temps&nbsp;: la porte "
           + "est ouverte, et la phrase attend une réponse.",
        pourquoi: "Il n'est pas six heures. Tout est encore possible." },
      { txt: "Si j'avais gardé le reçu, j'aurais été remboursée.", sous: "au comptoir, ce matin",
        ok: 'tard',
        rat: "Le reçu n'a pas été gardé, et le remboursement n'aura pas lieu. Les deux moitiés "
           + "sont fermées&nbsp;: c'est un constat sur du passé, pas une demande.",
        pourquoi: "Le reçu est perdu. Rien à rattraper." },
      { txt: "Si j'avais une voiture, je viendrais te chercher.", sous: "au téléphone",
        ok: 'auj',
        rat: "Cette personne n'a pas de voiture — aujourd'hui, en ce moment. Ce n'est pas une "
           + "histoire finie&nbsp;: c'est une situation actuelle qu'on imagine autrement.",
        pourquoi: "Pas de voiture aujourd'hui. Une situation, pas un souvenir." },
      { txt: "Si vous acceptez ma candidature, je peux commencer lundi.", sous: "un courriel à un employeur",
        ok: 'poss',
        rat: "Rien n'est décidé. C'est justement pour ça qu'on écrit&nbsp;: la personne offre "
           + "quelque chose au cas où la réponse serait oui.",
        pourquoi: "Rien n'est décidé. La porte est ouverte." },
      { txt: "Si l'usine était restée ici, mon père n'aurait pas déménagé.", sous: "en parlant du passé",
        ok: 'tard',
        rat: "L'usine est partie, le déménagement a eu lieu. On ne change plus rien&nbsp;: on "
           + "explique ce qui aurait été autrement.",
        pourquoi: "L'usine est partie. Le déménagement a eu lieu." },
      { txt: "Si tu parlais anglais, tu aurais eu le poste.", sous: "après une entrevue ratée",
        ok: 'tard',
        rat: "Celui-là est le plus difficile des huit&nbsp;: la première moitié ressemble à celle "
           + "de la voiture. Mais regardez la fin — «&nbsp;tu aurais eu&nbsp;»&nbsp;: l'entrevue "
           + "est passée, le poste est donné à quelqu'un d'autre. C'est fini.",
        pourquoi: "L'entrevue est passée. Le poste est donné." },
      { txt: "Si je gagnais mieux ma vie, je déménagerais.", sous: "une conversation de corridor",
        ok: 'auj',
        rat: "Le salaire d'aujourd'hui ne permet pas de déménager. Rien n'est terminé — c'est "
           + "l'état actuel des choses qu'on imagine autrement.",
        pourquoi: "Le salaire d'aujourd'hui. Une situation actuelle." },
      { txt: "Si l'école ferme demain, je resterai à la maison.", sous: "la veille d'une tempête",
        ok: 'poss',
        rat: "La tempête n'est pas passée, l'école n'a rien annoncé&nbsp;: la chose peut arriver "
           + "pour de vrai, et la phrase prépare la suite.",
        pourquoi: "La tempête n'est pas passée. Ça peut arriver." },
    ],
    attente: "Tranchez les huit phrases pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez pas regardé la grammaire. Et pourtant vous avez trié juste.",
    paras: [
      "Reprenez vos trois colonnes et regardez uniquement <b>le verbe qui suit «&nbsp;si&nbsp;»</b>. "
      + "Vous allez voir qu'il ne se répète jamais d'une colonne à l'autre&nbsp;: "
      + "<i>si tu <b>finis</b></i>, <i>si l'école <b>ferme</b></i> à gauche&nbsp;; "
      + "<i>si j'<b>avais</b></i>, <i>si je <b>gagnais</b></i> au milieu&nbsp;; "
      + "<i>si j'<b>avais gardé</b></i>, <i>si l'usine <b>était restée</b></i> à droite.",

      "<b>Le test, à appliquer sur n'importe quelle phrase&nbsp;:</b> regardez le verbe juste "
      + "après «&nbsp;si&nbsp;», et rien d'autre.<br>"
      + "· Un verbe au <b>présent</b> — <i>si tu finis</i> — ça peut encore arriver.<br>"
      + "· Un verbe en <b>-ais / -ait</b> — <i>si j'avais</i> — ce n'est pas le cas aujourd'hui.<br>"
      + "· Un verbe en <b>deux morceaux</b> — <i>si j'avais gardé</i>, <i>si elle était "
      + "restée</i> — c'est passé, c'est trop tard.",

      "Vous n'avez pas eu besoin des noms de ces temps pour trier huit phrases. Vous en aurez "
      + "besoin pour parler avec votre enseignant, et ils arrivent dans deux écrans.",
    ],
    retenir: "Tout se décide sur <b>le verbe qui suit «&nbsp;si&nbsp;»</b>. "
           + "Présent&nbsp;: encore possible. En <i>-ais</i>&nbsp;: pas aujourd'hui. "
           + "En deux morceaux&nbsp;: trop tard.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. La faute qui se remarque, et pourquoi elle est logique. ───────────
  {
    id:   'la-faute-connue',
    type: 'verif',
    eye:  'Le cas qui trompe',
    menu: 'La faute connue',
    titre: "Une seule de ces phrases s'écrit. Laquelle ?",
    consigne: "Miriam explique à son enseignante pourquoi elle n'était pas là mardi.",
    options: [
      { txt: "«&nbsp;Si j'avais su, je serais venue.&nbsp;»", juste: true },
      { txt: "«&nbsp;Si j'aurais su, je serais venue.&nbsp;»",
        rat_t: "C'est la faute la plus remarquée du français — et elle a une bonne raison.",
        rat: "Vous avez entendu que la phrase parlait de quelque chose d'imaginaire, et vous avez "
           + "mis la forme imaginaire <b>des deux côtés</b>. C'est logique. Mais ces formes en "
           + "<i>-rais</i> vivent seulement dans la <b>deuxième</b> moitié&nbsp;: "
           + "«&nbsp;je serais venue&nbsp;». Après «&nbsp;si&nbsp;», jamais." },
      { txt: "«&nbsp;Si j'avais su, je serai venue.&nbsp;»",
        rat_t: "La première moitié est juste. C'est la seconde qui a glissé.",
        rat: "«&nbsp;Je serai&nbsp;» annonce quelque chose à venir — or Miriam parle de mardi "
           + "dernier. Une seule lettre sépare <i>serai</i> de <i>serais</i>, et elle change le "
           + "temps de la phrase du futur vers l'imaginaire. Ici, il faut la seconde." },
    ],
    pourquoi: "<b>Jamais de forme en <i>-rais</i> après «&nbsp;si&nbsp;».</b> Elle appartient à "
            + "l'autre moitié de la phrase, et à elle seule. Si vous ne deviez retenir qu'une "
            + "chose de ce point, ce serait celle-là.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Le métalangage, une fois la chose manipulée cinq écrans. ──────────
  {
    id:   'les-deux-moities',
    type: 'notion',
    eye:  'Les noms des choses',
    menu: 'Les deux moitiés',
    titre: "Les deux moitiés vont ensemble, et elles ne se mélangent pas.",
    paras: [
      "Voici maintenant les noms — vous vous servez de ces formes depuis cinq écrans. "
      + "<b>Ce qui est encore possible&nbsp;:</b> <i>si</i> + <b>présent</b>, puis présent, futur "
      + "ou impératif. «&nbsp;<i>Si tu finis avant six heures, appelle-moi.</i>&nbsp;»",

      "<b>Ce qui n'est pas le cas aujourd'hui&nbsp;:</b> <i>si</i> + <b>imparfait</b>, puis "
      + "<b>conditionnel présent</b>. «&nbsp;<i>Si j'avais une voiture, je viendrais te "
      + "chercher.</i>&nbsp;» — <b>Ce qui est passé et ne se rattrape plus&nbsp;:</b> <i>si</i> + "
      + "<b>plus-que-parfait</b>, puis <b>conditionnel passé</b>. «&nbsp;<i>Si j'avais gardé le "
      + "reçu, j'aurais été remboursée.</i>&nbsp;»",

      "Une seule chose à surveiller&nbsp;: <b>les deux moitiés doivent appartenir au même "
      + "montage</b>. C'est là que se fait la faute de l'écran suivant — pas dans le choix du "
      + "montage, mais dans le fait d'en commencer un et d'en finir un autre.",
    ],
    retenir: "Trois montages, jamais mélangés. Et dans les trois, <b>rien en <i>-rais</i> après "
           + "«&nbsp;si&nbsp;»</b>.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des phrases écrites : les deux moitiés vont-elles ensemble ? ─
  {
    id:   'tri-moities',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six phrases',
    titre: "Six phrases écrites. Les deux moitiés vont-elles ensemble ?",
    consigne: "Regardez le verbe après «&nbsp;si&nbsp;», puis le verbe de l'autre moitié. "
            + "Ils doivent raconter le même moment.",
    colonnes: [
      { id: 'ok',   t: 'Correct',   b: 'Correct' },
      { id: 'faux', t: 'Ça ne va pas ensemble', b: 'Ça ne va pas' },
    ],
    items: [
      { txt: "Si vous avez besoin d'une attestation, écrivez-moi.", ok: 'ok',
        rat: "Présent après «&nbsp;si&nbsp;», impératif ensuite&nbsp;: c'est le montage de ce qui "
           + "peut encore arriver, et il tient d'un bout à l'autre.",
        pourquoi: "Encore possible, des deux côtés. Juste." },
      { txt: "Si je serais libre demain, je viendrais.", ok: 'faux',
        rat: "La forme en <i>-rais</i> est passée du mauvais côté. Ici, «&nbsp;demain&nbsp;» dit "
           + "que la chose est possible&nbsp;: «&nbsp;<b>si je suis</b> libre demain, je "
           + "viendrai&nbsp;».",
        pourquoi: "Il faut « si je suis libre demain, je viendrai »." },
      { txt: "Si l'entreprise était restée ici, on n'aurait pas perdu d'emplois.", ok: 'ok',
        rat: "Deux morceaux après «&nbsp;si&nbsp;», deux morceaux ensuite&nbsp;: l'usine est "
           + "partie, les emplois sont perdus. Le montage du trop tard, entier.",
        pourquoi: "Passé des deux côtés. Juste." },
      { txt: "Si tu m'avais prévenu, je change mon horaire.", ok: 'faux',
        rat: "La première moitié dit que c'est fini — vous n'avez pas prévenu. Et la seconde parle "
           + "d'aujourd'hui, comme si on pouvait encore agir. Il faut choisir&nbsp;: "
           + "«&nbsp;<b>j'aurais changé</b> mon horaire&nbsp;».",
        pourquoi: "Il faut « j'aurais changé mon horaire »." },
      { txt: "Si je gagnais mieux ma vie, je déménagerais dans ce quartier.", ok: 'ok',
        rat: "En <i>-ais</i> après «&nbsp;si&nbsp;», en <i>-rais</i> ensuite&nbsp;: le montage "
           + "d'aujourd'hui, complet. C'est celui qu'on emploie pour parler d'une situation qui "
           + "dure.",
        pourquoi: "Aujourd'hui, des deux côtés. Juste." },
      { txt: "Si j'avais su que c'était gratuit, j'y vais.", ok: 'faux',
        rat: "La première moitié est parfaite, et c'est ce qui rend la phrase tentante&nbsp;: on "
           + "l'entend souvent finir ainsi à l'oral. Mais «&nbsp;j'y vais&nbsp;» parle de "
           + "maintenant, alors que la chose est passée&nbsp;: «&nbsp;<b>j'y serais allé</b>&nbsp;».",
        pourquoi: "Il faut « j'y serais allé »." },
    ],
    attente: "Tranchez les six phrases pour continuer.",
  },

  // ── 7. Ce que le montage du passé sert vraiment à faire. ────────────────
  {
    id:   'le-reproche-poli',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Ce que ça dit vraiment',
    titre: "« Si vous m'aviez prévenue, j'aurais pu m'organiser. » Que dit cette phrase ?",
    consigne: "Une employée écrit à son gestionnaire, le lendemain d'un changement d'horaire "
            + "annoncé à la dernière minute.",
    options: [
      { txt: "Vous ne m'avez pas prévenue, et ça m'a coûté quelque chose. Elle le dit sans vous "
           + "accuser.", juste: true },
      { txt: "Elle demande à être prévenue la prochaine fois.",
        rat_t: "C'est ce qu'elle espère, mais ce n'est pas ce qu'elle a écrit.",
        rat: "Une demande pour la prochaine fois s'écrirait au montage du possible&nbsp;: "
           + "«&nbsp;<i>Si vous me prévenez à l'avance, je pourrai m'organiser.</i>&nbsp;» Là, "
           + "les deux moitiés sont fermées&nbsp;: elle parle uniquement d'hier. Les deux phrases "
           + "sont utiles, et elles ne font pas le même travail." },
      { txt: "Elle n'est pas sûre d'avoir été prévenue.",
        rat_t: "Elle en est très sûre — c'est justement pour ça qu'elle écrit.",
        rat: "Le montage du passé ne sert jamais à exprimer un doute&nbsp;: il constate ce qui "
           + "<b>n'a pas eu lieu</b>. Quand la phrase est montée ainsi, celui qui l'écrit sait "
           + "parfaitement ce qui s'est passé." },
    ],
    pourquoi: "C'est à ça que sert ce montage&nbsp;: <b>reprocher sans accuser</b>. Dit à "
            + "l'indicatif — «&nbsp;vous ne m'avez pas prévenue&nbsp;» — c'est une attaque. Dit "
            + "avec «&nbsp;si&nbsp;», c'est un constat, et il passe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Dit en dernier : le « si » qui n'est pas une condition. ───────────
  {
    id:   'lautre-si',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: "L'autre « si »",
    titre: "Un « si » sur trois n'a pas de deuxième moitié — et il ne suit aucune règle.",
    paras: [
      "On a gardé celui-ci pour la fin, et c'est volontaire&nbsp;: le nommer plus tôt aurait fait "
      + "croire à un quatrième montage à retenir. Il n'en est pas un. "
      + "«&nbsp;<i>Je ne sais pas <b>s'il</b> viendra.</i>&nbsp;» "
      + "«&nbsp;<i>Elle demande <b>si</b> le dossier est complet.</i>&nbsp;» "
      + "Ces phrases ne posent aucune condition&nbsp;: elles rapportent une question.",

      "<b>Comment le reconnaître en une seconde&nbsp;:</b> il n'y a pas de deuxième moitié. Après "
      + "«&nbsp;si tu finis, appelle-moi&nbsp;», il y a deux morceaux&nbsp;; après "
      + "«&nbsp;je ne sais pas s'il viendra&nbsp;», il n'y a rien. Et devant, il y a toujours un "
      + "verbe de question&nbsp;: <i>savoir, demander, se demander, vérifier</i>.",

      "C'est le seul «&nbsp;si&nbsp;» qui accepte tous les temps, futur compris — parce que ce "
      + "n'est pas une condition. Ailleurs, le test de l'écran 3 vaut toujours.",
    ],
    retenir: "Pas de deuxième moitié, un verbe de question devant&nbsp;: "
           + "<b>ce n'est pas une condition, et rien n'y est interdit.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Écrire, pas reconnaître. ──────────────────────────────────────────
  {
    id:   'a-vous-decrire',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Votre message',
    titre: "Amadou écrit à un employeur qui ne l'a pas rappelé. Quelle version tient ?",
    consigne: "Il veut dire deux choses&nbsp;: qu'il aurait accepté le poste, et qu'il reste "
            + "disponible. Une seule version tient d'un bout à l'autre.",
    options: [
      { txt: "«&nbsp;Si vous m'aviez rappelé en mai, j'aurais accepté le poste. Si une place "
           + "s'ouvre cet automne, je suis toujours disponible.&nbsp;»", juste: true },
      { txt: "«&nbsp;Si vous m'auriez rappelé en mai, j'aurais accepté le poste. Si une place "
           + "s'ouvre cet automne, je suis toujours disponible.&nbsp;»",
        rat_t: "La deuxième phrase est parfaite. C'est la première qui a lâché.",
        rat: "Vous avez le plus difficile&nbsp;: deux montages différents dans le même message, et "
           + "le second est juste. Mais «&nbsp;si vous m'auriez&nbsp;» met la forme en <i>-rais</i> "
           + "après «&nbsp;si&nbsp;»&nbsp;: c'est la seule chose que la langue refuse partout. "
           + "«&nbsp;<b>Si vous m'aviez rappelé</b>&nbsp;»." },
      { txt: "«&nbsp;Si vous m'aviez rappelé en mai, j'accepterais le poste. Si une place "
           + "s'ouvrait cet automne, je serais toujours disponible.&nbsp;»",
        rat_t: "Rien n'est interdit ici — mais le message ne dit plus la même chose.",
        rat: "Les deux phrases sont bien montées, sauf que la première mélange le passé et "
           + "aujourd'hui&nbsp;: le poste de mai n'existe plus, il faut "
           + "«&nbsp;<b>j'aurais accepté</b>&nbsp;». Et la seconde, en <i>-ait</i>, laisse "
           + "entendre qu'aucune place ne s'ouvrira&nbsp;: c'est exactement ce qu'Amadou ne veut "
           + "pas dire." },
    ],
    pourquoi: "Deux montages dans un seul message&nbsp;: le passé fermé pour ce qui est perdu, le "
            + "possible pour ce qui reste ouvert. <b>C'est tout le point en quatre lignes.</b>",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le même cas qu'à l'écran 1. ───────────────────────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient aux trois phrases du début.",
    consigne: "Teodora a manqué une rencontre de parents mardi soir&nbsp;: personne ne l'avait "
            + "avertie. Elle écrit à l'école <b>mercredi matin</b>. Que choisit-elle&nbsp;?",
    options: [
      { txt: "«&nbsp;Si j'avais su, je serais venue.&nbsp;»", juste: true },
      { txt: "«&nbsp;Si je savais, je viendrais.&nbsp;»",
        rat_t: "C'est la phrase de l'écran 1 — et elle parle du mauvais jour.",
        rat: "Ce montage dit&nbsp;: en ce moment je ne sais pas, et tant que ce sera le cas je ne "
           + "viendrai pas. Or la rencontre a eu lieu hier&nbsp;: elle est terminée. Il faut le "
           + "montage en deux morceaux&nbsp;: «&nbsp;<b>si j'avais su</b>&nbsp;»." },
      { txt: "«&nbsp;Si j'aurais su, je serais venue.&nbsp;»",
        rat_t: "Le sens est exactement le bon. C'est la forme qui coûte cher.",
        rat: "Vous avez choisi le bon moment — c'est le plus difficile, et c'est fait. Mais la "
           + "forme en <i>-rais</i> est passée après «&nbsp;si&nbsp;», et c'est la faute qu'une "
           + "enseignante remarque avant même de finir la phrase. Elle se corrige en une seconde&nbsp;: "
           + "«&nbsp;si j'<b>avais</b> su&nbsp;»." },
    ],
    pourquoi: "Vous avez fait les deux gestes du point&nbsp;: choisir le montage sur <b>ce que "
            + "vous voulez dire</b>, et ne jamais laisser une forme en <i>-rais</i> passer après "
            + "«&nbsp;si&nbsp;».",
    attente: "Choisissez une réponse pour finir.",
  },

];
