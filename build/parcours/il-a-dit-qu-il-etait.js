// ═══════════════════════════════════════════════════════════════════════════
// Point express — Répéter une parole ancienne sans en fausser la date
//
// Savoir n8-s26 (Indicatif conditionnel passé / présent employé comme avenir
// du passé), avec n8-s23 (plus-que-parfait). Une ORDONNANCE : l'enseignant
// l'envoie à un élève dont un compte rendu, un courriel de réclamation ou un
// résumé de réunion rapporte une parole ancienne avec les repères du jour où
// elle a été dite. Dix minutes, dix écrans.
//
// ── Ce qui le sépare des mini-leçons existantes ────────────────────────────
// Le dépôt en porte quatre sur ce sujet, et toutes quatre font la même chose :
//   · « Rapporter au passé : tout recule d'un cran »
//   · « Rapporter au passé : trois décalages, et rien de plus »
//   · « Rapporter des paroles quand le récit est au passé »
//   · « Rapporter ce qui a été dit : le discours indirect au passé »
// Elles donnent toutes le TABLEAU DES TEMPS — présent → imparfait, futur →
// conditionnel, passé composé → plus-que-parfait. Un élève envoyé ici l'a donc
// déjà lu deux fois, et il continue d'écrire « il a dit qu'il me rappellerait
// demain » trois semaines plus tard. Le tableau n'était pas le problème.
//
// Les cinq écarts tenus :
//
//   1. LE SUJET N'EST PAS LE TABLEAU, C'EST LE CALENDRIER. Les deux premiers
//      écrans ne parlent pas des verbes du tout : ils font trancher les MOTS DE
//      TEMPS — demain, ce soir, mardi prochain — que les quatre mini-leçons
//      mentionnent en fin de liste, quand elles les mentionnent.
//   2. INDUCTIF. L'élève range six repères, puis six verbes, AVANT qu'aucune
//      règle ne soit écrite. Les écrans 3 et 5 constatent ce qu'il vient de
//      faire.
//   3. UN TEST, JAMAIS LA LISTE. Pas de tableau de conversion. Une seule
//      question, qui marche sur un verbe jamais vu : « au moment où la personne
//      a parlé, est-ce que c'était encore à venir pour elle, ou déjà fait ? »
//   4. LE CAS PAR DÉFAUT EN DERNIER (écran 8) : celui où rien ne recule, parce
//      que la parole vaut encore. Le nommer d'entrée ferait croire à deux
//      règles concurrentes.
//   5. EXEMPLES VARIÉS, PRIS HORS DE TOUT MODULE : un rappel de fournisseur,
//      un compte rendu de réunion, une réclamation d'assurance, un message à
//      un conseiller pédagogique, un formulaire d'admission.
//
// Aucun média : ce point se joue entièrement à l'écrit, et la faute qu'il vise
// ne s'entend pas — elle se lit trois semaines après, dans un document.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:     'il-a-dit-qu-il-etait',
  titre:    "Répéter une parole ancienne sans en fausser la date",
  surtitre: "Point express · 10 minutes",
  niveau:   8,
  savoir:   'n8-s26',
};

const ECRANS = [

  // ── 1. Une décision, sans aucune règle donnée. ───────────────────────────
  {
    id:   'depart',
    type: 'verif',
    eye:  'Une question, pour commencer',
    menu: 'Trois semaines plus tard',
    titre: "Lundi le 3, un fournisseur vous dit : « Je vous rappelle demain. »",
    consigne: "Nous sommes le 24. Vous écrivez à votre gestionnaire pour expliquer que "
            + "l'appel n'est jamais venu. Quelle phrase écrivez-vous&nbsp;? Répondez avec ce que "
            + "vous savez déjà — c'est fait exprès.",
    options: [
      { txt: "Il m'a dit qu'il me rappellerait le lendemain.", juste: true },
      { txt: "Il m'a dit qu'il me rappellerait demain.",
        rat_t: "Le verbe est juste. C'est le mot «&nbsp;demain&nbsp;» qui a été oublié en route.",
        rat: "Vous avez bien reculé le verbe. Mais «&nbsp;demain&nbsp;», pour la personne qui "
           + "vous lit aujourd'hui, veut dire <b>le 25</b>. Votre gestionnaire comprend qu'on "
           + "attend encore un appel, alors que celui-ci était promis pour le 4." },
      { txt: "Il m'a dit qu'il me rappelle demain.",
        rat_t: "Celle-là garde la parole telle quelle, comme si elle venait d'être dite.",
        rat: "C'est la phrase qu'on écrit quand on rapporte quelque chose entendu il y a dix "
           + "minutes, et elle est parfaite dans ce cas-là. Trois semaines plus tard, elle donne "
           + "à la promesse une date qui n'a jamais existé." },
    ],
    pourquoi: "Gardez cette phrase en tête&nbsp;: on y revient au dernier écran, dans une autre "
            + "situation.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 2. On trie AVANT de savoir. Et on trie le calendrier, pas les verbes. ─
  {
    id:   'tri-reperes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six repères',
    titre: "Six paroles à rapporter longtemps après. Quel mot peut rester tel quel ?",
    consigne: "Chaque phrase a été dite il y a des semaines et vous la rapportez "
            + "aujourd'hui. Regardez le mot souligné&nbsp;: pour la personne qui vous lira, "
            + "veut-il encore dire la même chose&nbsp;?",
    colonnes: [
      { id: 'garder',   t: "Il reste tel quel", b: "Il reste tel quel" },
      { id: 'deplacer', t: "Il doit changer",   b: "Il doit changer" },
    ],
    items: [
      { txt: "«&nbsp;Je vous envoie le contrat <b>demain</b>.&nbsp;»",
        sous: "dit il y a trois semaines", ok: 'deplacer',
        rat: "«&nbsp;Demain&nbsp;» se compte à partir du jour où l'on parle. Trois semaines "
           + "après, il désigne un jour qui n'a rien à voir avec la promesse&nbsp;: il faut "
           + "écrire <b>le lendemain</b>, ou donner la date.",
        pourquoi: "Il devient « le lendemain ». Le jour a bougé." },
      { txt: "«&nbsp;Le bureau ferme à <b>16&nbsp;h</b>.&nbsp;»",
        sous: "dit le mois dernier, au téléphone", ok: 'garder',
        rat: "Une heure d'horloge ne dépend pas du jour où on la dit. Seize heures, c'était "
           + "seize heures, et ce le sera encore quand on vous relira.",
        pourquoi: "Une heure d'horloge ne bouge jamais." },
      { txt: "«&nbsp;Je te rappelle <b>ce soir</b>.&nbsp;»",
        sous: "dit un lundi, rapporté le jeudi", ok: 'deplacer',
        rat: "«&nbsp;Ce soir&nbsp;», jeudi, veut dire jeudi soir. La promesse portait sur le "
           + "lundi&nbsp;: on écrit <b>le soir même</b>, ou on nomme le jour.",
        pourquoi: "Il devient « le soir même »." },
      { txt: "«&nbsp;J'ai commencé en <b>2019</b>.&nbsp;»",
        sous: "dit à une entrevue, rapporté dans un rapport", ok: 'garder',
        rat: "Une année est une date absolue&nbsp;: elle ne se compte pas à partir du moment où "
           + "l'on parle. Tout ce qui porte un chiffre de calendrier — 2019, le 14 mars, "
           + "juin — se recopie sans y toucher.",
        pourquoi: "Une date de calendrier se recopie telle quelle." },
      { txt: "«&nbsp;La réunion est <b>mardi prochain</b>.&nbsp;»",
        sous: "dit il y a un mois", ok: 'deplacer',
        rat: "«&nbsp;Prochain&nbsp;» veut dire «&nbsp;le premier à venir <i>à partir "
           + "d'aujourd'hui</i>&nbsp;». Un mois après, ce n'est plus le même mardi&nbsp;: "
           + "<b>le mardi suivant</b>, ou la date.",
        pourquoi: "Il devient « le mardi suivant »." },
      { txt: "«&nbsp;Le cours dure <b>deux heures</b>.&nbsp;»",
        sous: "dit à l'inscription, rapporté en classe", ok: 'garder',
        rat: "C'est une durée, pas un moment. Deux heures restent deux heures, peu importe "
           + "quand on le dit ou quand on le répète.",
        pourquoi: "Une durée n'a pas de point de départ à déplacer." },
    ],
    attente: "Tranchez les six cas pour continuer.",
  },

  // ── 3. La règle, écrite comme un constat de ce qu'il vient de faire. ─────
  {
    id:   'deux-calendriers',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Deux calendriers',
    titre: "Vous avez séparé ce qui se compte à partir d'aujourd'hui du reste.",
    paras: [
      "Regardez votre colonne «&nbsp;il reste tel quel&nbsp;»&nbsp;: une heure, une année, une "
      + "durée. Aucun de ces mots n'a besoin de savoir quel jour on est. Dans l'autre colonne, "
      + "chaque mot compte les jours <b>à partir de celui qui parle</b> — et celui qui parle "
      + "n'est plus vous.",

      "Quand vous rapportez une parole ancienne, il y a donc <b>deux calendriers</b> dans la "
      + "phrase&nbsp;: celui de la personne, le jour où elle a parlé, et celui de votre lecteur, "
      + "aujourd'hui. Tout le travail consiste à traduire les repères du premier dans le second.",

      "<b>Le plus sûr, dans un document de travail, est de donner la date.</b> "
      + "«&nbsp;Il m'a dit qu'il rappellerait <b>le 4 mars</b>&nbsp;» ne laisse aucun doute, se "
      + "relit dans six mois, et se vérifie. «&nbsp;Le lendemain&nbsp;» est correct, mais il "
      + "oblige votre lecteur à retrouver de quel jour on part.",
    ],
    retenir: "Demain, ce soir, la semaine prochaine se comptent depuis celui qui parle. Une "
           + "heure, une date, une durée ne se comptent depuis personne&nbsp;: elles ne bougent "
           + "pas.",
    attente: "Lisez, puis continuez.",
  },

  // ── 4. Deuxième tri : les verbes, toujours sans règle donnée. ────────────
  {
    id:   'tri-verbes',
    type: 'tri',
    eye:  'À vous de trancher',
    menu: 'Six verbes',
    titre: "Mêmes paroles, autre question : au moment où elle a parlé, était-ce fait ?",
    consigne: "Ne pensez pas encore aux temps de verbe. Replacez-vous simplement <b>au moment où "
            + "la personne a parlé</b>, et demandez-vous ce qu'elle avait devant elle.",
    colonnes: [
      { id: 'venir', t: "C'était encore à venir", b: "Encore à venir" },
      { id: 'fait',  t: "C'était déjà fait",      b: "Déjà fait" },
    ],
    items: [
      { txt: "«&nbsp;Je vous rappellerai jeudi.&nbsp;»",
        sous: "un fournisseur, au téléphone", ok: 'venir',
        rat: "Jeudi n'était pas encore arrivé quand elle a dit cette phrase&nbsp;: l'appel était "
           + "devant elle. C'est une promesse, et une promesse est toujours à venir.",
        pourquoi: "Devant elle : « il a dit qu'il rappellerait »." },
      { txt: "«&nbsp;J'ai déposé la demande la semaine passée.&nbsp;»",
        sous: "une collègue, en réunion", ok: 'fait',
        rat: "Elle raconte ce qu'elle a fait avant de parler. Le dépôt est derrière elle, et il "
           + "l'est doublement pour vous qui le rapportez aujourd'hui.",
        pourquoi: "Derrière elle : « elle a dit qu'elle avait déposé »." },
      { txt: "«&nbsp;Je pars à six heures demain matin.&nbsp;»",
        sous: "un chauffeur, la veille d'une livraison", ok: 'venir',
        rat: "Le verbe est au présent, et c'est ce qui trompe&nbsp;: le présent sert souvent à "
           + "parler de tout de suite après. Le départ n'avait pas eu lieu quand il l'a annoncé.",
        pourquoi: "Devant lui, malgré le présent : « il a dit qu'il partirait »." },
      { txt: "«&nbsp;Le colis est parti mardi.&nbsp;»",
        sous: "le service à la clientèle, un vendredi", ok: 'fait',
        rat: "Mardi précédait le vendredi où la phrase a été dite. Ce qui était déjà passé pour "
           + "la personne l'est encore plus pour votre lecteur.",
        pourquoi: "Derrière : « on m'a dit que le colis était parti »." },
      { txt: "«&nbsp;Je vais vous écrire une lettre.&nbsp;»",
        sous: "une conseillère, à la fin d'un rendez-vous", ok: 'venir',
        rat: "«&nbsp;Je vais&nbsp;» annonce ce qui vient. Rien n'était écrit au moment où elle "
           + "l'a dit&nbsp;: c'est une intention, donc du devant.",
        pourquoi: "Devant elle : « elle a dit qu'elle allait écrire »." },
      { txt: "«&nbsp;Je n'ai jamais reçu votre courriel.&nbsp;»",
        sous: "un employeur, deux mois avant votre plainte", ok: 'fait',
        rat: "Elle parle de tout ce qui s'est passé jusqu'au moment où elle parle. Une absence "
           + "de réception constatée est un fait déjà accompli, même si le verbe est à la forme "
           + "négative.",
        pourquoi: "Derrière : « il a dit qu'il n'avait jamais reçu »." },
    ],
    attente: "Tranchez les six cas pour continuer.",
  },

  // ── 5. La règle des verbes, en une question réutilisable. ────────────────
  {
    id:   'le-test',
    type: 'notion',
    eye:  'Ce que vous venez de faire',
    menu: 'Le test',
    titre: "Vous n'avez conjugué aucun verbe. Vous avez seulement regardé où la personne était.",
    paras: [
      "<b>Le test, sur n'importe quelle parole à rapporter&nbsp;:</b> replacez-vous au moment où "
      + "elle a été dite, et posez une seule question — <i>pour cette personne, à cet "
      + "instant-là, est-ce que c'était encore à venir, ou déjà fait&nbsp;?</i>",

      "Encore à venir&nbsp;: le verbe prend la terminaison en <b>-rait</b>. «&nbsp;Il a dit "
      + "qu'il <b>rappellerait</b>&nbsp;», «&nbsp;elle a dit qu'elle <b>allait</b> "
      + "écrire&nbsp;». Déjà fait&nbsp;: le verbe prend <b>avait</b> ou <b>était</b> plus le "
      + "participe. «&nbsp;Elle a dit qu'elle <b>avait déposé</b>&nbsp;», «&nbsp;on m'a dit que "
      + "le colis <b>était parti</b>&nbsp;».",

      "Ce que vous venez d'employer porte des noms&nbsp;: la forme en -rait est le "
      + "<b>conditionnel</b>, et <i>avait</i> + participe le <b>plus-que-parfait</b>. Vous n'avez "
      + "pas eu besoin de ces noms pour trancher les six cas, mais votre enseignant les emploiera "
      + "et un correcteur les écrira dans la marge.",

      "Et le reste — ce qui se passait autour, sans début ni fin nette — reste à l'imparfait, "
      + "comme dans un récit&nbsp;: «&nbsp;il a dit qu'il <b>était</b> en congé cette "
      + "semaine-là&nbsp;».",
    ],
    retenir: "Une seule question&nbsp;: à venir pour elle, ou déjà fait&nbsp;? À venir → "
           + "<b>-rait</b>. Déjà fait → <b>avait</b> ou <b>était</b> + participe.",
    attente: "Lisez, puis continuez.",
  },

  // ── 6. Le piège : ce que la phrase rapportée ne dit PAS. ─────────────────
  {
    id:   'ce-quon-ne-sait-pas',
    type: 'verif',
    eye:  'Le piège',
    menu: 'Ce qu\'on ne sait pas',
    titre: "« Le 2 février, il a dit qu'il était en arrêt de travail. » Il l'est encore ?",
    consigne: "Vous lisez cette phrase dans un dossier, aujourd'hui. Que pouvez-vous en "
            + "conclure&nbsp;?",
    options: [
      { txt: "Rien sur aujourd'hui&nbsp;: la phrase ne parle que du 2 février.", juste: true },
      { txt: "Qu'il est encore en arrêt de travail.",
        rat_t: "C'est la lecture la plus naturelle, et c'est pour ça qu'elle est dangereuse.",
        rat: "La phrase rapporte l'état des choses <b>au moment où il a parlé</b>, et rien "
           + "d'autre. Ce qui s'est passé depuis n'y est pas. Dans un dossier d'assurance ou de "
           + "ressources humaines, c'est exactement la conclusion qu'il ne faut pas tirer." },
      { txt: "Qu'il ne l'est plus, sinon on aurait écrit «&nbsp;est&nbsp;».",
        rat_t: "Vous lisez une information là où il n'y en a pas.",
        rat: "L'imparfait dit seulement que l'on rapporte&nbsp;: il ne dit ni que ça continue, "
           + "ni que ça s'est arrêté. Pour savoir où il en est aujourd'hui, il faut une source "
           + "d'aujourd'hui — un appel, un document daté." },
    ],
    pourquoi: "<b>Une parole rapportée est datée.</b> Elle vous dit ce qui était vrai ce "
            + "jour-là&nbsp;; elle ne dit jamais ce qui est vrai maintenant. C'est ce qui la rend "
            + "utile dans un dossier — et ce qui la rend trompeuse quand on l'oublie.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 7. Le cas fréquent : la réclamation écrite. ──────────────────────────
  {
    id:   'la-reclamation',
    type: 'verif',
    eye:  'Vérification',
    menu: 'La réclamation',
    titre: "Vous écrivez à l'assureur, six semaines après l'appel. Quelle phrase ?",
    consigne: "Le 12 janvier, une agente vous a dit&nbsp;: «&nbsp;Nous avons reçu votre "
            + "formulaire et vous serez remboursé dans dix jours.&nbsp;» Rien n'est arrivé.",
    options: [
      { txt: "Le 12 janvier, une agente m'a confirmé que vous aviez reçu mon formulaire et que "
           + "je serais remboursé dans les dix jours.", juste: true },
      { txt: "Le 12 janvier, une agente m'a confirmé que vous avez reçu mon formulaire et que je "
           + "serai remboursé dans dix jours.",
        rat_t: "Les deux verbes sont restés au moment de l'appel.",
        rat: "Écrit ainsi, le délai de dix jours semble courir <b>à partir d'aujourd'hui</b>, "
           + "et votre lettre perd son argument&nbsp;: c'est justement parce que ces dix jours "
           + "sont écoulés depuis longtemps que vous écrivez. «&nbsp;Aviez reçu&nbsp;», "
           + "«&nbsp;serais remboursé&nbsp;»." },
      { txt: "Le 12 janvier, une agente m'a confirmé&nbsp;: «&nbsp;Nous avons reçu votre "
           + "formulaire et vous serez remboursé dans dix jours.&nbsp;»",
        rat_t: "Elle n'est pas fautive — mais elle ne fait pas le travail que vous attendez.",
        rat: "Citer entre guillemets est permis, et parfois utile. Mais vous n'avez pas "
           + "l'enregistrement de l'appel&nbsp;: présenter de mémoire une citation mot pour mot "
           + "vous expose à ce qu'on la conteste. Le rapporter en vos mots, avec la date, est "
           + "plus solide." },
    ],
    pourquoi: "Une lettre de réclamation vaut par ses dates. La date de l'appel, écrite en tête, "
            + "et les verbes reculés qui montrent que le délai promis <b>est déjà passé</b>.",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 8. Le cas par défaut, dit en dernier. ────────────────────────────────
  {
    id:   'quand-rien-ne-recule',
    type: 'notion',
    eye:  'Ce qui reste',
    menu: 'Quand rien ne recule',
    titre: "Il y a un cas où l'on ne recule rien du tout, et il est fréquent.",
    paras: [
      "On l'a gardé pour la fin exprès&nbsp;: le nommer d'entrée aurait fait croire à deux règles "
      + "à retenir. Quand vous rapportez une parole <b>qui vaut encore</b>, ou que vous rapportez "
      + "tout de suite, rien ne bouge&nbsp;: «&nbsp;<i>La secrétaire dit que le bureau ferme à "
      + "midi.</i>&nbsp;» Elle le dit, c'est vrai maintenant, on n'a rien à reculer.",

      "Le déclencheur est le verbe qui introduit&nbsp;: <i>elle <b>dit</b> que</i> laisse tout en "
      + "place, <i>elle <b>a dit</b> que</i> ouvre le calendrier de l'autre. C'est votre premier "
      + "mot qui décide de toute la suite de la phrase.",

      "Et même après «&nbsp;a dit&nbsp;», on garde le présent pour ce qui ne dépend d'aucune "
      + "date&nbsp;: «&nbsp;<i>Le conseiller m'a expliqué que la formation <b>dure</b> huit "
      + "mois.</i>&nbsp;» La durée d'un programme n'appartient pas au 12 janvier. Reculer ce "
      + "verbe-là laisserait entendre qu'elle a changé depuis.",
    ],
    retenir: "Regardez d'abord votre verbe d'introduction. <b>Au présent, rien ne bouge&nbsp;;</b> "
           + "au passé, tout se traduit — sauf ce qui reste vrai aujourd'hui.",
    attente: "Lisez, puis continuez.",
  },

  // ── 9. Choisir une version entière, pas une forme isolée. ────────────────
  {
    id:   'le-compte-rendu',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Le compte rendu',
    titre: "Le compte rendu de la réunion du 5 mai, écrit le 30. Quelle version tient ?",
    consigne: "En réunion, la directrice a dit&nbsp;: «&nbsp;J'ai rencontré le comité hier. Je "
            + "vous donne ma réponse la semaine prochaine.&nbsp;» Trois versions&nbsp;: une seule "
            + "est juste d'un bout à l'autre.",
    options: [
      { txt: "La directrice a indiqué qu'elle avait rencontré le comité la veille et qu'elle "
           + "donnerait sa réponse la semaine suivante.", juste: true },
      { txt: "La directrice a indiqué qu'elle avait rencontré le comité hier et qu'elle "
           + "donnerait sa réponse la semaine prochaine.",
        rat_t: "Les deux verbes sont bons. Ce sont les deux repères de temps qui sont restés au 5 mai.",
        rat: "Vous avez le plus difficile&nbsp;: <i>avait rencontré</i> et <i>donnerait</i> sont "
           + "exacts. Mais «&nbsp;hier&nbsp;» et «&nbsp;la semaine prochaine&nbsp;» se comptent "
           + "depuis le lecteur, qui lit le 30&nbsp;: <b>la veille</b>, <b>la semaine "
           + "suivante</b>." },
      { txt: "La directrice a indiqué qu'elle a rencontré le comité la veille et qu'elle donne "
           + "sa réponse la semaine suivante.",
        rat_t: "Les repères sont bons. Ce sont les verbes qui sont restés au 5 mai.",
        rat: "C'est l'inverse de l'autre piège, et il est plus visible&nbsp;: "
           + "«&nbsp;elle donne sa réponse la semaine suivante&nbsp;» n'a pas de sens en "
           + "français. Une fois «&nbsp;a indiqué&nbsp;» posé, les deux verbes suivent&nbsp;: "
           + "<b>avait rencontré</b>, <b>donnerait</b>." },
    ],
    pourquoi: "Les deux moitiés se règlent ensemble&nbsp;: <b>les verbes</b> par la question "
            + "«&nbsp;à venir ou déjà fait&nbsp;?&nbsp;», <b>les repères</b> par la question "
            + "«&nbsp;depuis quel jour se comptent-ils&nbsp;?&nbsp;».",
    attente: "Choisissez une réponse pour continuer.",
  },

  // ── 10. La fermeture : le cas de l'écran 1, dans une autre situation. ────
  {
    id:   'fermeture',
    type: 'verif',
    eye:  'La dernière',
    menu: 'Pour finir',
    titre: "On revient au fournisseur du 3 : « Je vous rappelle demain. »",
    consigne: "Cette fois, vous n'écrivez pas trois semaines après&nbsp;: vous envoyez un message "
            + "à votre collègue <b>le 3, en sortant de l'appel</b>, pour qu'il ne le relance pas "
            + "en double. Que choisissez-vous&nbsp;?",
    options: [
      { txt: "Il dit qu'il nous rappelle demain — n'écris rien avant jeudi.", juste: true },
      { txt: "Il a dit qu'il nous rappellerait le lendemain — n'écris rien avant jeudi.",
        rat_t: "C'est la bonne réponse de l'écran 1 — et elle n'est pas fautive ici non plus.",
        rat: "Elle est simplement plus lourde que la situation ne le demande. Vous et votre "
           + "collègue êtes le 3 tous les deux&nbsp;: «&nbsp;demain&nbsp;» veut dire la même "
           + "chose pour vous deux, il n'y a aucun calendrier à traduire. Le recul sert à "
           + "franchir une distance&nbsp;; ici, il n'y en a pas." },
      { txt: "Il dit qu'il nous rappellerait le lendemain — n'écris rien avant jeudi.",
        rat_t: "Les deux moitiés viennent de deux situations différentes.",
        rat: "«&nbsp;Il dit&nbsp;» annonce qu'on ne recule rien, puis «&nbsp;rappellerait&nbsp;» "
           + "et «&nbsp;le lendemain&nbsp;» reculent quand même. C'est le verbe d'introduction "
           + "qui commande&nbsp;: une fois qu'il est posé, la phrase entière le suit." },
    ],
    pourquoi: "Vous avez fait les trois choses&nbsp;: regarder le verbe d'introduction, demander "
            + "«&nbsp;à venir ou déjà fait&nbsp;?&nbsp;» pour chaque verbe, et traduire les "
            + "repères de temps — <b>ou constater qu'il n'y avait rien à traduire</b>.",
    attente: "Choisissez une réponse pour finir.",
  },

];
