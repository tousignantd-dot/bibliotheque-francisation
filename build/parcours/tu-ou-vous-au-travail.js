// ═══════════════════════════════════════════════════════════════════════════
// Point express — Le même message pour un collègue, un patron, un ministère
//
// Savoir n8-s01 (Communication langagière : reconnaître la variété de langue —
// populaire, familière, standard, soutenue — et en tenir compte), avec
// n8-s56 (synonymes de variétés de langue différentes). Une ORDONNANCE :
// l'enseignant l'envoie à un élève dont les courriels professionnels portent
// des tournures de conversation, ou l'inverse — une note à un collègue écrite
// comme une lettre au ministre.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Cinq mini-leçons du dépôt touchent au registre :
//   · « Tu ou vous ? »
//   · « Tu, vous et les salutations d'usage »
//   · « Familier, standard, soutenu : choisir sans se tromper »
//   · « Familier, standard, soutenu — et lequel choisir »
//   · « Le registre : deux façons de dire vrai »
// Toutes procèdent par ÉCHELLE : voici trois ou quatre niveaux de langue,
// voici des exemples de chacun, choisissez le bon. Un élève qui les a lues
// sait nommer les registres — et écrit quand même « Salut, peux-tu me dire si
// ma demande est acceptée ? » au service de l'immigration.
//
// Les cinq écarts tenus :
//
//   1. LE SUJET N'EST PAS L'ÉCHELLE, C'EST LE DESTINATAIRE. Aucun écran ne
//      demande « quel registre est-ce ? ». On demande « à qui cela peut-il
//      être envoyé ? » — la question qu'on se pose vraiment avant d'écrire.
//   2. INDUCTIF. L'élève range six phrases par destinataire AVANT qu'aucun
//      nom de registre ne soit écrit. L'écran 3 constate.
//   3. UN TEST, JAMAIS LA LISTE. Une seule question, réutilisable devant
//      n'importe quel message : « est-ce que je peux nommer la personne qui
//      va me lire, et est-ce que quelqu'un d'autre pourrait me relire ? »
//   4. LE MÉTALANGAGE APRÈS. « Registre », « standard », « soutenu » ne sont
//      écrits qu'à l'écran 3, une fois six cas tranchés.
//   5. LE CAS PAR DÉFAUT EN DERNIER (écran 8) : le registre standard, celui
//      qui ne se remarque nulle part et qui règle neuf messages sur dix. Le
//      nommer d'entrée ferait croire qu'il faut choisir à chaque phrase.
//
// Aucun média : ce point porte sur des messages écrits, et la faute qu'il
// vise ne s'entend jamais — elle se lit, chez quelqu'un qu'on ne connaît pas.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'tu-ou-vous-au-travail',
  titre:    "Le même message pour un collègue, un patron, un ministère",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s01',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois versions',
    titre: "Vous demandez une journée de congé le 12. Trois façons de le dire.",
    consigne: "Le message part à la <b>directrice des ressources humaines</b>, que vous n'avez "
            + "rencontrée qu'une fois. Répondez avec ce que vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "Bonjour madame Tremblay, j'aimerais prendre congé le 12 septembre. "
           + "Est-ce que cette date vous convient&nbsp;?", juste: true },
      { txt: "Bonjour, est-ce que je pourrais avoir congé le 12&nbsp;? Merci&nbsp;!",
        rat_t: "Rien n'est fautif — mais il manque tout ce qui permet de traiter la demande.",
        rat: "La phrase est polie et se lit bien. Le problème est ailleurs&nbsp;: pas de nom, "
           + "pas de mois, pas de signature dans ce qu'on voit. Une personne des ressources "
           + "humaines reçoit quarante messages par jour&nbsp;; celui-ci lui coûte un aller-retour "
           + "pour savoir de quel 12 il s'agit." },
      { txt: "Je sollicite respectueusement l'autorisation de m'absenter en date du "
           + "12&nbsp;septembre prochain.",
        rat_t: "Trop haut pour la situation, et ça se remarque autant que trop bas.",
        rat: "C'est le ton d'une requête officielle adressée à une institution. Employé pour "
           + "demander une journée à une collègue de son propre établissement, il met une "
           + "distance que la situation ne demande pas — et il laisse penser que vous attendez "
           + "un refus." },
    ],
    pourquoi: "Gardez cette demande en tête&nbsp;: au dernier écran, elle partira ailleurs.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. Par destinataire, pas par registre. ──────
  {
    id:   'tri-destinataire',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six messages',
    titre: "Six phrases écrites au travail. À qui chacune peut-elle être envoyée ?",
    consigne: "Aucune règle ne vous a été donnée — normal. Ne cherchez pas à noter le niveau de "
            + "langue&nbsp;: demandez-vous simplement <b>qui peut recevoir cette phrase sans "
            + "sourciller</b>.",
    colonnes: [
      { id: 'coll', t: "Un collègue",    b: "Un collègue" },
      { id: 'chef', t: "Votre supérieur", b: "Votre supérieur" },
      { id: 'inst', t: "Un ministère",   b: "Un ministère" },
    ],
    items: [
      { txt: "Peux-tu me renvoyer le fichier&nbsp;? J'pense que j'ai effacé le mien.",
        sous: "message instantané, 9 h 40", ok: 'coll',
        rat: "Le tutoiement, la question directe et surtout «&nbsp;j'pense&nbsp;» — la façon "
           + "d'écrire comme on parle. Cela suppose une personne qu'on voit tous les jours et "
           + "qui n'a rien à décider sur votre sort.",
        pourquoi: "On écrit comme on parle : entre collègues." },
      { txt: "Je vous confirme que le dossier sera déposé avant vendredi.",
        sous: "courriel, après une réunion", ok: 'chef',
        rat: "Vouvoiement, phrase complète, engagement daté. C'est le ton d'un message qui peut "
           + "être relu plus tard&nbsp;: on y prend un engagement devant quelqu'un qui en "
           + "répondra.",
        pourquoi: "Un engagement daté, devant quelqu'un qui en répond." },
      { txt: "Veuillez trouver ci-joint les pièces demandées à l'appui de ma demande.",
        sous: "courriel avec pièces jointes", ok: 'inst',
        rat: "«&nbsp;Veuillez trouver ci-joint&nbsp;», «&nbsp;à l'appui de&nbsp;»&nbsp;: des "
           + "formules qu'on n'emploie jamais entre personnes qui se connaissent. Elles servent "
           + "quand on écrit à une <b>fonction</b>, pas à quelqu'un.",
        pourquoi: "On écrit à une fonction, pas à quelqu'un." },
      { txt: "Bonjour, je te reviens là-dessus demain, j'ai une réunion tout l'avant-midi.",
        sous: "réponse rapide, en fin de journée", ok: 'coll',
        rat: "«&nbsp;Je te reviens là-dessus&nbsp;» est courant et correct au travail, mais il "
           + "suppose le tutoiement et une conversation qui continue. On ne l'écrit pas à "
           + "quelqu'un qu'on n'a jamais vu.",
        pourquoi: "Une conversation qui continue : entre collègues." },
      { txt: "Je me permets de vous relancer au sujet de ma demande du 3 juin, restée sans "
           + "réponse.",
        sous: "deuxième courriel, un mois plus tard", ok: 'inst',
        rat: "Relancer une institution demande deux choses que cette phrase fait&nbsp;: rappeler "
           + "une date précise, et rester impeccablement neutre. Ni reproche, ni familiarité — "
           + "le message peut être versé au dossier.",
        pourquoi: "Une date, aucun reproche : le message ira au dossier." },
      { txt: "Auriez-vous quelques minutes cette semaine pour qu'on en discute&nbsp;?",
        sous: "courriel, demande de rencontre", ok: 'chef',
        rat: "Vouvoiement et conditionnel de politesse, mais la demande reste simple et directe. "
           + "C'est le ton de quelqu'un qui travaille avec vous et à qui vous pouvez demander du "
           + "temps.",
        pourquoi: "Vouvoyé, mais direct : on travaille ensemble." },
    ],
    attente: "Tranchez les six messages pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez jugé aucune phrase. Vous avez imaginé qui la recevait.",
    paras: [
      "Regardez ce qui sépare vos trois colonnes. Ce n'est ni la politesse — les six phrases sont "
      + "polies — ni la longueur. C'est <b>la distance</b>&nbsp;: est-ce que je connais la "
      + "personne, et est-ce que ce message risque d'être lu par quelqu'un d'autre que "
      + "moi&nbsp;?",

      "<b>Le test, avant d'envoyer n'importe quel message&nbsp;:</b> <i>est-ce que je peux nommer "
      + "la personne qui va me lire&nbsp;?</i> Si oui, et si elle me connaît, la conversation "
      + "peut ressembler à une conversation. Si non — un service, une adresse générale, un "
      + "dossier — j'écris à une <b>fonction</b>&nbsp;: vouvoiement, phrases entières, aucune "
      + "familiarité.",

      "<b>Et le deuxième volet&nbsp;: est-ce que ce message peut être relu plus tard&nbsp;?</b> "
      + "Un message instantané se perd&nbsp;; un courriel qui prend un engagement se retrouve. "
      + "C'est ce qui explique pourquoi une même personne — votre supérieur — reçoit un ton "
      + "détendu à l'oral et un ton plus tenu par écrit.",

      "Ce que vous venez de trier s'appelle le <b>registre</b>&nbsp;: familier avec les proches, "
      + "standard au travail, soutenu avec les institutions. Vous n'aviez pas besoin de ces "
      + "trois mots pour trancher, mais votre enseignant les emploiera.",
    ],
    retenir: "Deux questions&nbsp;: <b>puis-je nommer la personne&nbsp;?</b> et <b>ce message "
           + "peut-il être relu&nbsp;?</b> Elles décident du ton mieux qu'une échelle.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Le piège : le « tu » qui se glisse dans un écrit officiel. ────────
  {
    id:   'le-tu-qui-glisse',
    type: 'verif',
    eye:  'Le piège',
    menu: "Le « tu » qui glisse",
    titre: "Vous terminez une lettre à un organisme. Quelle dernière ligne ?",
    consigne: "Vous avez écrit trois paragraphes impeccables à un service de reconnaissance des "
            + "acquis. Il reste la phrase de clôture.",
    options: [
      { txt: "Je demeure disponible pour tout renseignement complémentaire.", juste: true },
      { txt: "N'hésite pas à me contacter si tu as besoin d'autre chose.",
        rat_t: "C'est la phrase qu'on tape sans y penser, parce qu'on l'écrit dix fois par jour.",
        rat: "Vous ne l'avez pas choisie&nbsp;: vous l'avez recopiée de vos messages à vos "
           + "collègues, où elle est parfaite. Après trois paragraphes vouvoyés, elle détonne — "
           + "et c'est <b>la dernière chose que la personne lit</b>. Les fautes de registre se "
           + "logent presque toujours dans la première et la dernière ligne." },
      { txt: "Merci d'avance de votre réponse rapide.",
        rat_t: "Vouvoyée, correcte — et pourtant elle vous dessert.",
        rat: "Remercier d'avance d'une réponse <i>rapide</i> demande quelque chose qu'on n'a pas "
           + "à demander&nbsp;: cela se lit comme une pression, dans un contexte où vous "
           + "n'êtes pas en position d'en exercer. «&nbsp;Je vous remercie de l'attention "
           + "portée à ma demande&nbsp;» dit la même chose sans presser personne." },
    ],
    pourquoi: "<b>Relisez toujours vos deux extrémités.</b> Le corps du message est écrit avec "
            + "attention&nbsp;; l'ouverture et la clôture sortent des doigts tout seules, et "
            + "c'est là que le mauvais ton s'installe.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 5. Ce qui change concrètement, ligne par ligne. ──────────────────────
  {
    id:   'les-trois-lignes',
    type: 'notion',
    eye:  'Ce qui change',
    menu: 'Trois lignes',
    titre: "Le même contenu, trois destinataires : trois lignes bougent, pas plus.",
    paras: [
      "<b>L'ouverture.</b> «&nbsp;Salut Marc&nbsp;» pour un collègue. «&nbsp;Bonjour madame "
      + "Tremblay&nbsp;» pour un supérieur. «&nbsp;Madame, Monsieur&nbsp;» quand on ignore qui "
      + "lira. On ne se trompe presque jamais en écrivant «&nbsp;Bonjour&nbsp;» suivi du nom de "
      + "famille&nbsp;: c'est l'usage le plus courant au travail au Québec.",

      "<b>La demande.</b> «&nbsp;Peux-tu…&nbsp;» entre collègues. «&nbsp;Est-ce que vous "
      + "pourriez…&nbsp;» ou «&nbsp;j'aimerais…&nbsp;» avec un supérieur. «&nbsp;Je vous saurais "
      + "gré de…&nbsp;» ou «&nbsp;je vous demande de bien vouloir…&nbsp;» avec une institution. "
      + "Le conditionnel monte à mesure que la distance augmente.",

      "<b>La clôture.</b> «&nbsp;Merci&nbsp;!&nbsp;» ou rien du tout entre collègues. "
      + "«&nbsp;Merci beaucoup&nbsp;» avec un supérieur. «&nbsp;Veuillez agréer mes salutations "
      + "distinguées&nbsp;» dans une lettre officielle — et cette formule-là ne s'emploie que "
      + "dans une vraie lettre, jamais dans un courriel courant.",

      "<b>Ce qui ne change pas&nbsp;:</b> les faits, les dates, les montants, la clarté. Un "
      + "message soutenu n'est pas un message vague. On monte le ton, on ne dilue jamais "
      + "l'information.",
    ],
    retenir: "Trois lignes bougent&nbsp;: l'ouverture, la demande, la clôture. <b>Le contenu, "
           + "lui, est le même pour tout le monde.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Trier des tournures : celles qui ne survivent pas à l'écrit. ──────
  {
    id:   'tri-oral-ecrit',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six tournures',
    titre: "Six tournures entendues au travail. Lesquelles s'écrivent aussi ?",
    consigne: "Toutes se disent, et aucune n'est fautive à l'oral. La question est "
            + "autre&nbsp;: <b>laquelle peut se retrouver dans un courriel professionnel&nbsp;?</b>",
    colonnes: [
      { id: 'oral',    t: "À l'oral seulement", b: "Oral seulement" },
      { id: 'partout', t: "À l'oral et à l'écrit", b: "Les deux" },
    ],
    items: [
      { txt: "Y a un problème avec la facture.", ok: 'oral',
        rat: "«&nbsp;Y a&nbsp;» pour «&nbsp;il y a&nbsp;» est courant et parfaitement clair "
           + "quand on parle. À l'écrit, il signale qu'on n'a pas relu&nbsp;: "
           + "«&nbsp;<b>Il y a</b> un problème avec la facture.&nbsp;»",
        pourquoi: "À l'écrit : « il y a »." },
      { txt: "Je n'ai pas encore reçu de réponse.", ok: 'partout',
        rat: "La négation complète, avec le <i>ne</i>. On l'entend moins souvent qu'on ne la "
           + "lit, mais elle passe partout&nbsp;: personne ne la trouvera guindée dans une "
           + "conversation.",
        pourquoi: "La négation complète passe partout." },
      { txt: "J'ai pas eu le temps de finir le rapport.", ok: 'oral',
        rat: "La négation sans <i>ne</i> est la façon normale de parler, y compris entre "
           + "professionnels. Dans un courriel à un supérieur, elle se lit comme un relâchement "
           + "— et l'ajout du <i>ne</i> ne coûte rien.",
        pourquoi: "À l'écrit : « je n'ai pas eu le temps »." },
      { txt: "Pourriez-vous me confirmer la date&nbsp;?", ok: 'partout',
        rat: "L'inversion et le conditionnel&nbsp;: c'est la demande polie standard. Elle se dit "
           + "au téléphone comme elle s'écrit, sans jamais paraître trop haute.",
        pourquoi: "La demande polie standard, dans les deux." },
      { txt: "C'est correct pour moi, on peut y aller de même.", ok: 'oral',
        rat: "«&nbsp;De même&nbsp;» pour «&nbsp;ainsi&nbsp;» est bien vivant au Québec et "
           + "parfaitement compris. Mais un courriel est souvent relu par quelqu'un qui n'était "
           + "pas dans la conversation&nbsp;: «&nbsp;Cela me convient&nbsp;; nous pouvons "
           + "procéder ainsi.&nbsp;»",
        pourquoi: "À l'écrit : « cela me convient, nous pouvons procéder ainsi »." },
      { txt: "Je vous reviens dès que j'ai l'information.", ok: 'partout',
        rat: "«&nbsp;Je vous reviens&nbsp;» est entré dans l'usage professionnel écrit, y "
           + "compris vers un supérieur. Il reste trop familier pour une lettre à une "
           + "institution, où l'on écrira «&nbsp;je vous informerai dès que…&nbsp;».",
        pourquoi: "Passe au travail ; à remonter d'un cran pour un ministère." },
    ],
    attente: "Tranchez les six tournures pour continuer.",
  },

  // ── 7. Le cas qu'on redoute : tutoyer ou non, le premier jour. ───────────
  {
    id:   'le-premier-jour',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le premier jour',
    titre: "Premier jour dans un nouvel emploi. Vos collègues se tutoient tous.",
    consigne: "Une collègue de votre équipe, que vous ne connaissez pas, vous demande quelque "
            + "chose en vous tutoyant. Que faites-vous&nbsp;?",
    options: [
      { txt: "Vous la tutoyez en retour, comme elle vient de le faire.", juste: true },
      { txt: "Vous la vouvoyez quand même, pour rester prudent les premières semaines.",
        rat_t: "La prudence est bonne, mais elle vise le mauvais moment.",
        rat: "Le vouvoiement s'impose <b>avant</b> qu'on vous ait parlé, quand vous ne savez pas "
           + "encore. Une fois qu'une personne vous a tutoyé, continuer à la vouvoyer crée une "
           + "distance qu'elle n'a pas demandée — et qui peut se lire comme un reproche. Dans "
           + "beaucoup de milieux de travail au Québec, le tutoiement entre collègues du même "
           + "niveau est l'usage courant." },
      { txt: "Vous lui demandez si elle préfère qu'on se vouvoie.",
        rat_t: "La question est courtoise, et elle est de trop.",
        rat: "Elle vient de trancher en vous tutoyant&nbsp;: reposer la question l'oblige à "
           + "reprendre une décision déjà prise. Cette question est utile dans l'autre sens — "
           + "vers quelqu'un de plus âgé, un client, un supérieur — où l'on attend simplement "
           + "qu'on vous propose le tutoiement." },
    ],
    pourquoi: "La règle de terrain tient en une ligne&nbsp;: <b>on vouvoie tant qu'on ne sait "
            + "pas, et on suit la personne dès qu'elle a choisi.</b> Avec un supérieur ou un "
            + "client, on attend qu'il propose — et à l'écrit officiel, on vouvoie même "
            + "quelqu'un qu'on tutoie en personne.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier. ────────────────────────────────
  {
    id:   'le-standard',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Le ton qui ne se voit pas',
    titre: "Il existe un ton qui ne se remarque nulle part, et il règle presque tout.",
    paras: [
      "On l'a gardé pour la fin exprès&nbsp;: le nommer d'entrée aurait fait croire qu'il faut "
      + "choisir à chaque message. Ce ton, c'est le <b>standard</b> — vouvoiement, phrases "
      + "entières, négation complète, aucune formule de cérémonie. «&nbsp;Bonjour madame "
      + "Tremblay, je n'ai pas encore reçu la confirmation. Pourriez-vous me dire où en est le "
      + "dossier&nbsp;? Merci beaucoup.&nbsp;»",

      "Sa qualité est de <b>ne rien signaler</b>. Personne, en le lisant, ne se dit «&nbsp;cette "
      + "personne écrit familièrement&nbsp;» ni «&nbsp;cette personne en fait trop&nbsp;». Il "
      + "passe chez un supérieur, chez un client, chez un collègue qu'on ne connaît pas encore, "
      + "et dans neuf messages sur dix il n'y a rien d'autre à choisir.",

      "Les deux extrémités sont les exceptions&nbsp;: le familier, entre gens qui se voient tous "
      + "les jours&nbsp;; le soutenu, quand on écrit à une institution ou qu'on dépose une "
      + "réclamation. <b>Dans le doute, revenez au milieu</b> — c'est là qu'on se trompe le "
      + "moins cher.",
    ],
    retenir: "Le standard est le ton par défaut, pas un compromis. <b>Familier et soutenu se "
           + "choisissent&nbsp;; le standard s'écrit quand on n'a rien à choisir.</b>",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Assembler un message entier, pas une phrase. ──────────────────────
  {
    id:   'le-courriel-entier',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le courriel',
    titre: "Un courriel de trois lignes à un ministère. Lequel envoyez-vous ?",
    consigne: "Vous relancez une demande déposée le 3 juin, restée sans réponse. Vous ne savez "
            + "pas qui la traite. Une seule version tient d'un bout à l'autre.",
    options: [
      { txt: "Madame, Monsieur, / Ma demande déposée le 3 juin est restée sans réponse à ce "
           + "jour. Pourriez-vous m'indiquer l'état du dossier&nbsp;? / Je vous remercie de "
           + "votre attention.", juste: true },
      { txt: "Madame, Monsieur, / Ma demande déposée le 3 juin est restée sans réponse à ce "
           + "jour. Pourriez-vous m'indiquer l'état du dossier&nbsp;? / N'hésitez pas à me "
           + "contacter si vous avez besoin d'autre chose&nbsp;!",
        rat_t: "Les deux premières lignes sont parfaites. C'est la clôture qui est tombée.",
        rat: "Le piège de l'écran 4, dans un vrai message&nbsp;: la dernière ligne sort des "
           + "doigts toute seule. Et elle inverse les rôles — c'est <b>vous</b> qui attendez "
           + "quelque chose, pas eux. Le point d'exclamation, lui, n'a pas sa place dans un "
           + "écrit officiel." },
      { txt: "Bonjour, / Je vous écris parce que j'ai fait une demande au mois de juin et j'ai "
           + "toujours pas eu de réponse. Ça fait longtemps. / Merci de me revenir "
           + "là-dessus rapidement.",
        rat_t: "Le ton et le contenu se sont dégradés ensemble.",
        rat: "Trois choses en même temps&nbsp;: la négation sans <i>ne</i>, «&nbsp;me revenir "
           + "là-dessus&nbsp;» qui suppose une conversation, et surtout la <b>perte de la "
           + "date</b>. «&nbsp;Au mois de juin&nbsp;» et «&nbsp;ça fait longtemps&nbsp;» "
           + "remplacent le seul renseignement qui permette de retrouver votre dossier. Le "
           + "registre a baissé, et l'information avec lui." },
    ],
    pourquoi: "Le ton monte, les faits restent. <b>Une date précise, une demande claire, une "
            + "clôture neutre</b> — et rien à relire deux fois.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : la demande de l'écran 1, autre destinataire. ──────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au congé du 12. Cette fois, vous écrivez à un collègue.",
    consigne: "Votre demande est acceptée. Vous écrivez maintenant à Marc, avec qui vous "
            + "travaillez tous les jours et qui devra couvrir votre poste ce jour-là. Que "
            + "choisissez-vous&nbsp;?",
    options: [
      { txt: "Salut Marc, je suis en congé le 12. Est-ce que tu peux prendre les appels ce "
           + "matin-là&nbsp;? Merci&nbsp;!", juste: true },
      { txt: "Bonjour Marc, j'aimerais prendre congé le 12 septembre. Est-ce que cette date te "
           + "convient&nbsp;?",
        rat_t: "C'est la bonne réponse de l'écran 1 — et elle ne dit plus ce qu'il faut.",
        rat: "Le ton est juste pour un collègue, mais le <b>contenu</b> a été recopié tel quel. "
           + "Marc n'autorise rien&nbsp;: le congé est déjà accordé. Lui demander si la date "
           + "«&nbsp;lui convient&nbsp;» lui donne un pouvoir qu'il n'a pas et laisse votre vraie "
           + "demande — couvrir les appels — hors du message." },
      { txt: "Marc, veuillez noter que je serai absent le 12 septembre. Merci de prendre les "
           + "appels en mon absence.",
        rat_t: "Le ton officiel, entre collègues, ne fait pas sérieux&nbsp;: il fait froid.",
        rat: "«&nbsp;Veuillez noter&nbsp;» et «&nbsp;merci de prendre&nbsp;» annoncent une "
           + "décision au lieu de demander un service. À quelqu'un qui devra réorganiser sa "
           + "matinée pour vous, cela se lit comme un ordre — et vous n'êtes pas son supérieur. "
           + "Le registre trop haut abîme une relation aussi sûrement que le registre trop bas." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: nommer la personne qui lit, régler les "
            + "trois lignes sur elle, et <b>refaire le contenu</b> plutôt que de le recopier. "
            + "Changer de destinataire, ce n'est jamais seulement changer de ton.",
    attente: "Choisissez une réponse pour finir.",
  },

];
