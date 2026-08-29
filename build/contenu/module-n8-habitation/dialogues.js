const DIALOGUES = {

  // Quatre personnages, quatre voix distinctes — aucun partage, donc aucune
  // contrainte de croisement. TEODORA (féminine 2), MARJOLAINE (enseignante,
  // ralentie à 0,85), NORMAND (masculin 1), FABIEN (narrateur, non ralenti).
  //
  // Aucun extrait ne réunit plus de deux personnes, et jamais deux femmes
  // autres que Teodora et Marjolaine : le dépôt n'a que deux voix féminines,
  // et c'est compté avant d'écrire, pas après.
  //
  // Le choix de qui prend `enseignante` n'est pas neutre : c'est la seule
  // voix que `voix_lente` ralentit. Elle va à MARJOLAINE, dont les répliques
  // sont courtes et administratives. Elle ne pouvait surtout pas aller à
  // FABIEN, qui porte le monologue du défi 3 : quinze répliques d'affilée
  // ralenties seraient interminables — la note de l'activité 119 le dit.

  prep: {
    label: "Dialogue — « Votre réclamation est refusée »",
    lines: [
      ["MARJOLAINE","Mutuelle Saint-Maurice, règlement des sinistres, Marjolaine Pelchat à l'appareil."],
      ["TEODORA","Bonjour madame. Teodora Vlaicu, dossier 2026-41837. J'ai reçu une lettre hier."],
      ["MARJOLAINE","Un instant, je l'ouvre. Refoulement d'égout, rue Sainte-Julie, Trois-Rivières, sinistre du 14 septembre. C'est bien ça ?"],
      ["TEODORA","C'est ça. La lettre dit que la réclamation est refusée. Je voudrais comprendre pourquoi."],
      ["MARJOLAINE","Le dossier a été fermé la semaine dernière, après le rapport de l'expert. Le motif retenu est le défaut d'entretien du drain de plancher."],
      ["TEODORA","Le défaut d'entretien. C'est-à-dire ?"],
      ["MARJOLAINE","C'est une exclusion prévue au contrat, à l'article 7.3. L'assureur ne couvre pas les dommages qui résultent d'un manque d'entretien d'un élément dont l'assuré a la charge."],
      ["TEODORA","Attendez. Vous me dites que le drain n'a pas été entretenu ?"],
      ["MARJOLAINE","C'est ce que le rapport conclut, oui."],
      ["TEODORA","Il a été nettoyé au mois de mai. Par une entreprise. J'ai la facture."],
      ["MARJOLAINE","Cette information n'apparaît pas au dossier. Vous l'aviez transmise ?"],
      ["TEODORA","Personne ne me l'a demandée. L'expert est venu, il a regardé le sous-sol vingt minutes, et je ne l'ai jamais revu."],
      ["MARJOLAINE","Je comprends. Ce que je peux faire aujourd'hui, c'est noter votre appel au dossier. Je ne peux pas rouvrir une décision moi-même."],
      ["TEODORA","Qui peut le faire ?"],
      ["MARJOLAINE","Une demande de révision doit être adressée par écrit. Le service qui l'examine n'est pas le mien."],
      ["TEODORA","D'accord. Avant d'écrire quoi que ce soit, j'aimerais avoir le rapport de l'expert. Le rapport complet, pas le résumé de la lettre."],
      ["MARJOLAINE","Vous y avez droit. Je vous l'envoie par courriel aujourd'hui. Comptez quatre pages."],
      ["TEODORA","Et l'avenant ? Ma lettre parle d'un avenant « eau du sol et égout ». Je l'ai, cet avenant ?"],
      ["MARJOLAINE","Vous l'avez depuis le renouvellement de 2023, avec une franchise de mille dollars. Ce n'est pas la protection qui manque, madame Vlaicu. C'est l'exclusion qui a été appliquée."],
      ["TEODORA","Donc je suis couverte, mais on refuse de payer."],
      ["MARJOLAINE","Formulé comme ça, oui. Le contrat couvre le refoulement ; il ne couvre pas un refoulement causé par un défaut d'entretien."],
      ["TEODORA","Très bien. Envoyez-moi le rapport. Je vais le lire, et je vous rappelle."],
    ]
  },

  t1: {
    label: "Dialogue — Quatre pages, ligne par ligne",
    lines: [
      ["NORMAND","Normand Lauzière, expert en sinistre. Assoyez-vous. Vous avez apporté le rapport ?"],
      ["TEODORA","Les quatre pages. Et la facture du nettoyage du drain, celle de mai."],
      ["NORMAND","Commençons par le rapport. Avant de le lire, une chose : un rapport d'expertise contient trois sortes de phrases, et elles n'ont pas du tout la même valeur."],
      ["TEODORA","Lesquelles ?"],
      ["NORMAND","Ce que l'expert a vu de ses yeux, ce qu'on lui a dit, et ce qu'il en déduit. Le premier bloc est presque impossible à contester. Le troisième se discute toujours."],
      ["TEODORA","Comment je les distingue ?"],
      ["NORMAND","Par les verbes. « J'ai constaté », « j'ai mesuré », « j'ai photographié » : ça, c'est vu. « Selon l'assurée », « il m'a été rapporté » : ça, c'est dit. Et puis « il appert que », « tout indique que », « la cause probable est » : ça, c'est déduit. Regardez la page trois."],
      ["TEODORA","« Il appert que l'obstruction s'est formée progressivement, ce qui laisse supposer une absence d'entretien. »"],
      ["NORMAND","Voilà. « Il appert », « laisse supposer ». Deux précautions dans une seule phrase. Un homme qui aurait vu quelque chose n'écrirait pas comme ça."],
      ["TEODORA","Il y a aussi cette phrase, page deux : « Le drain n'aurait pas été entretenu depuis plusieurs années. »"],
      ["NORMAND","Celle-là est intéressante. Vous voyez ce qui manque ?"],
      ["TEODORA","Le nom. On ne dit pas qui n'a pas entretenu."],
      ["NORMAND","Exactement. C'est le passif, et dans ce métier il travaille tout le temps. « Le drain n'a pas été entretenu » ne met personne en cause à voix haute, mais l'exclusion, elle, s'applique à vous."],
      ["TEODORA","Et la facture de mai ? Elle règle la question, non ?"],
      ["NORMAND","Elle règle une partie de la question. Vous prouvez un entretien, à une date, par une entreprise. C'est beaucoup. Mais leur rapport parle d'une obstruction formée sur plusieurs années, dans le drain de fondation, pas dans le drain de plancher."],
      ["TEODORA","Ce n'est pas la même chose ?"],
      ["NORMAND","Pas du tout. Le drain de fondation est dehors, au pied des murs. Le drain de plancher est dedans. La lettre de refus parle du drain de plancher, le rapport parle du drain de fondation. Vous avez remarqué ?"],
      ["TEODORA","Non. Je n'avais pas fait attention."],
      ["NORMAND","C'est là qu'est votre dossier, madame Vlaicu. Deux documents du même assureur qui ne parlent pas du même tuyau. C'est le genre de chose sur laquelle une révision se gagne."],
      ["TEODORA","Vous êtes prêt à l'écrire ?"],
      ["NORMAND","Je vais faire une contre-expertise. J'y vais jeudi, je photographie les deux drains, je fais passer une caméra dans le drain de fondation, et j'écris ce que j'ai vu — rien d'autre. Six cents dollars."],
      ["TEODORA","Et si votre rapport leur donne raison ?"],
      ["NORMAND","Alors je l'écrirai aussi, et vous saurez à quoi vous en tenir. Un expert que vous payez n'est pas un expert qui vous approuve."],
    ]
  },

  t2: {
    label: "Dialogue — L'appel qui conteste",
    lines: [
      ["MARJOLAINE","Mutuelle Saint-Maurice, Marjolaine Pelchat."],
      ["TEODORA","Bonjour madame Pelchat. Teodora Vlaicu, dossier 2026-41837. Je vous avais dit que je rappellerais après avoir lu le rapport."],
      ["MARJOLAINE","Je vous écoute."],
      ["TEODORA","Je conteste le refus, et je voudrais vous dire sur quoi. Trois points, ce sera court."],
      ["MARJOLAINE","Allez-y."],
      ["TEODORA","Premièrement, votre lettre invoque le défaut d'entretien du drain de plancher. Le rapport de votre expert, lui, décrit une obstruction du drain de fondation. Ce ne sont pas les mêmes tuyaux."],
      ["MARJOLAINE","Un instant… Effectivement, la lettre dit « drain de plancher ». Je le note."],
      ["TEODORA","Deuxièmement, le drain de plancher a été nettoyé le 3 mai par Plomberie Chartier. J'ai la facture acquittée, et l'entreprise accepte de confirmer l'intervention."],
      ["MARJOLAINE","Cette pièce ne figure pas au dossier. Vous pouvez me l'envoyer aujourd'hui ?"],
      ["TEODORA","Elle part dans l'heure. Troisièmement, j'ai fait faire une contre-expertise. Monsieur Lauzière a passé une caméra dans le drain de fondation jeudi dernier. Il n'y a aucune racine, aucun affaissement, et l'écoulement est libre sur toute la longueur."],
      ["MARJOLAINE","Vous avez son rapport par écrit ?"],
      ["TEODORA","Onze pages et vingt-deux photographies datées. Je vous l'envoie avec la facture."],
      ["MARJOLAINE","Madame Vlaicu, je dois vous dire une chose : ce n'est pas moi qui décide. Je transmets."],
      ["TEODORA","Je le sais, et je ne vous en tiens pas rigueur. Certes, ce n'est pas vous qui avez fermé le dossier — il n'en reste pas moins que c'est à vous que je peux parler aujourd'hui."],
      ["MARJOLAINE","C'est juste."],
      ["TEODORA","Et permettez-moi une dernière remarque. Si le drain avait vraiment été bouché par des années de négligence, l'eau ne serait pas montée en une seule soirée d'orage. Elle serait remontée bien avant, un peu à chaque grosse pluie. Ça ne s'est jamais produit en sept ans."],
      ["MARJOLAINE","Je note l'argument. Qu'est-ce que vous demandez, exactement ?"],
      ["TEODORA","Trois choses. Que le dossier soit rouvert. Que la contre-expertise soit examinée par quelqu'un qui n'a pas rendu la première décision. Et que la réponse me soit donnée par écrit, avec ses motifs."],
      ["MARJOLAINE","La demande de révision doit être écrite. Je peux ouvrir la plainte à votre nom aujourd'hui, mais vous devrez confirmer par écrit."],
      ["TEODORA","J'écris ce soir. Une dernière question : dans combien de temps aurai-je une réponse ?"],
      ["MARJOLAINE","Une réponse finale par écrit dans les soixante jours de la réception de votre plainte. Au-delà, on doit vous en donner la raison."],
      ["TEODORA","Soixante jours. Bien. Vous aurez ma lettre demain matin, madame Pelchat. Merci de m'avoir écoutée jusqu'au bout."],
      ["MARJOLAINE","C'est mon travail. Envoyez tout au même courriel, et gardez une copie de ce que vous envoyez."],
    ]
  },

  t3: {
    label: "Capsule d'information — Ce qu'on peut faire quand on n'est pas d'accord",
    lines: [
      ["FABIEN","Bonjour. Fabien Courtemanche, du service de renseignements de l'Autorité des marchés financiers. Cette capsule dure une quinzaine de minutes et porte sur une seule question : que faire quand une institution financière rend une décision avec laquelle vous n'êtes pas d'accord."],
      ["FABIEN","Je vais procéder en quatre temps. D'abord, ce qu'est une plainte au sens de la loi. Ensuite, ce que l'entreprise doit faire une fois qu'elle l'a reçue. Puis ce que vous pouvez faire de sa réponse. Et enfin, ce que nous pouvons faire, nous, et surtout ce que nous ne pouvons pas faire."],
      ["FABIEN","Premier temps. Beaucoup de gens croient qu'une plainte doit obligatoirement être écrite. Ce n'est pas cela. Une plainte, au sens du règlement, c'est un reproche ou une insatisfaction que vous communiquez à l'entreprise, en demandant une mesure correctrice. Vous pouvez la formuler verbalement : l'entreprise doit alors vous aider à la mettre par écrit et la consigner à son registre."],
      ["FABIEN","Ce qui suit est important. Même faite au téléphone, votre plainte compte : le dossier s'ouvre et les délais commencent à courir. Écrivez tout de même, ou demandez une confirmation écrite de votre appel. Le jour où il faudra prouver la date de réception, c'est vous qui devrez le faire."],
      ["TEODORA","Est-ce qu'un courriel suffit, ou est-ce qu'il faut une lettre par la poste ?"],
      ["FABIEN","Un courriel suffit. Ce qui compte, c'est d'avoir une trace de la date d'envoi et une copie de ce que vous avez écrit. Gardez les deux, toujours."],
      ["FABIEN","Deuxième temps : ce que l'entreprise doit faire. Elle doit accuser réception de votre plainte, la consigner dans un registre, et vous transmettre une réponse finale par écrit dans les soixante jours qui suivent la réception. Ce délai peut aller jusqu'à quatre-vingt-dix jours, mais seulement dans des circonstances exceptionnelles, et elle doit alors vous en informer et vous en donner la raison."],
      ["FABIEN","Notez bien l'expression « réponse finale ». Elle ne veut pas dire « réponse définitive pour vous ». Elle veut dire : c'est la dernière position de l'entreprise, elle a fini d'examiner votre dossier, et elle vous dit sur quoi elle s'appuie. Cette réponse doit être motivée — nommer la disposition du contrat, le fait retenu, et la conclusion qui en découle."],
      ["FABIEN","Une décision qui ne dit que « votre demande est refusée » n'est pas une décision motivée, et vous êtes en droit de demander qu'on la complète."],
      ["FABIEN","Troisième temps : ce que vous pouvez faire de cette réponse. Deux choses. Vous pouvez l'accepter — c'est parfois la bonne décision, et personne n'a à en juger à votre place. Ou vous pouvez nous demander le transfert de votre dossier. Ce transfert se demande une fois que vous avez reçu la réponse finale, ou une fois le délai écoulé si vous n'avez rien reçu."],
      ["FABIEN","Quand nous aurons reçu le dossier, nous l'examinerons et nous pourrons vous proposer, si les deux parties y consentent, un service de règlement des différends — une conciliation ou une médiation."],
      ["TEODORA","Et si l'entreprise refuse la conciliation ?"],
      ["FABIEN","Elle en a le droit, et c'est le moment de dire ce que nous ne pouvons pas faire. Nous ne sommes pas un tribunal. Nous ne renversons pas une décision, nous n'ordonnons à personne de vous indemniser, et nous ne représentons pas les consommateurs devant les tribunaux. Ce que nous faisons, c'est examiner, surveiller, et intervenir auprès de l'entreprise quand ses pratiques ne sont pas conformes."],
      ["FABIEN","Si vous voulez qu'une décision soit renversée par une autorité qui en a le pouvoir, c'est aux tribunaux civils qu'il faut vous adresser. La division des petites créances entend les demandes jusqu'à un certain montant, sans avocat, et beaucoup de dossiers d'assurance s'y règlent."],
      ["FABIEN","Quatrième temps, et j'insiste parce que c'est ce qu'on oublie le plus : ne confondez pas les portes. Un différend avec votre assureur relève de nous. Un différend avec votre locataire ou avec votre propriétaire relève du Tribunal administratif du logement, et une décision de ce tribunal se conteste autrement — par une demande de rétractation, ou par une permission d'appeler à la Cour du Québec, dans les trente jours."],
      ["FABIEN","Ce sont deux systèmes distincts, avec des délais distincts. Frapper à la mauvaise porte fait perdre des semaines, et parfois un droit."],
      ["FABIEN","Je répète donc l'essentiel, parce que c'est la seule chose à retenir de ces quinze minutes : écrivez, demandez quelque chose de précis, gardez copie, comptez soixante jours, et adressez-vous à la bonne porte. Merci de votre attention."],
    ]
  },
};
