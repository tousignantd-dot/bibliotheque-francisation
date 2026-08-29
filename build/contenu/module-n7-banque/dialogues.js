const DIALOGUES = {
  // Quatre dialogues longs : au niveau 7, la compétence porte sur des
  // discours étendus et structurés, et les trois intentions de la situation
  // sont « s'informer » — c'est-à-dire écouter longtemps quelqu'un qui
  // explique. Ils se travaillent en écoutes successives : une fois pour le
  // sujet, une fois pour les chiffres, une fois pour ce qui n'a pas été dit.
  //
  // Cinq personnages, cinq timbres. MARLÈNE parle dans les quatre ;
  // HUGUETTE, DAMIEN, NATHALIE et STEVE ne se rencontrent jamais, ce qui
  // laisse le générateur audio partager des voix sans qu'on l'entende.
  //
  // Un seul dialogue est au tutoiement, celui des deux collègues.
  prep: {
    label: "Dialogue — La pause de dix heures",
    lines: [
      ["MARLÈNE","Huguette, tu es bonne dans les chiffres, toi. Regarde ce papier-là deux minutes."],
      ["HUGUETTE","Ton relevé de carte ? Attends que je mette mes lunettes. Ah. Neuf mille quatre cents."],
      ["MARLÈNE","Neuf mille quatre cent douze. Et je paie tous les mois, Huguette. Je n'ai jamais sauté un paiement en trois ans."],
      ["HUGUETTE","Tu paies quoi, tous les mois ? Le montant en bas, dans la case ?"],
      ["MARLÈNE","Oui, le montant en bas. Le paiement minimum. Quatre cent soixante-dix dollars, à peu près."],
      ["HUGUETTE","C'est bien ce que je pensais. Regarde le solde de l'an passé, à côté. Il était de combien ?"],
      ["MARLÈNE","Neuf mille huit cents. Donc en un an, j'ai baissé de… quatre cents dollars ?"],
      ["HUGUETTE","Quatre cents dollars en douze paiements, Marlène, et tu as versé près de six mille dollars dans l'année. Une partie est partie en frais de crédit, et le reste dans ce que tu as continué d'acheter avec la carte. Ton taux est écrit là, dans le petit encadré : dix-neuf et quatre-vingt-dix."],
      ["MARLÈNE","Dix-neuf et quatre-vingt-dix, ça veut dire dix-neuf dollars par mois ?"],
      ["HUGUETTE","Par année, ma belle. Dix-neuf dollars et quatre-vingt-dix cents par cent dollars, par année. Sur neuf mille, calcule."],
      ["MARLÈNE","Attends. Attends. Tu me dis que je paie mille huit cents dollars par année juste pour avoir la dette ?"],
      ["HUGUETTE","À peu près, oui. Et le pire, c'est que tu as de l'argent dans ton compte. Tu me l'as dit le mois passé."],
      ["MARLÈNE","Six mille deux cents. C'est pour le cégep de Jessie. Elle commence dans deux ans, je n'y touche pas."],
      ["HUGUETTE","Six mille deux cents qui te rapportent zéro, pendant que neuf mille te coûtent dix-neuf pour cent. Marlène, ton argent travaille contre toi."],
      ["MARLÈNE","Dit comme ça… Mais je ne veux pas vider le compte de ma fille pour une carte de crédit."],
      ["HUGUETTE","Je ne te dis pas de le vider. Je te dis d'aller t'asseoir avec quelqu'un à la caisse et de poser trois questions."],
      ["MARLÈNE","Quelles questions ? C'est ça, mon problème. Quand ils parlent, je comprends un mot sur deux et je fais oui de la tête."],
      ["HUGUETTE","Alors arrête de faire oui de la tête. Quand tu ne comprends pas un mot, tu le répètes et tu demandes ce que ça veut dire. Personne n'est fâché pour ça."],
      ["MARLÈNE","« Quand vous dites capitalisé, ça veut dire quoi exactement ? » Comme ça ?"],
      ["HUGUETTE","Exactement comme ça. Et tu ne signes rien pendant le rendez-vous. Tu demandes le papier, tu rentres chez vous, tu le lis à la table de cuisine."],
      ["MARLÈNE","Je vais prendre un rendez-vous vendredi. Il faut que j'arrête de payer pour rien."],
    ]
  },

  t1: {
    label: "Dialogue — Trois façons d'emprunter",
    lines: [
      ["DAMIEN","Bonjour madame Saint-Preux, entrez. Damien Rouillard, conseiller en finances personnelles. Vous vouliez parler d'une carte de crédit, si j'ai bien lu la note."],
      ["MARLÈNE","Oui. J'ai neuf mille quatre cents dollars sur une carte à dix-neuf et quatre-vingt-dix, et je paie le minimum depuis trois ans. Ma collègue m'a dit que je payais pour rien."],
      ["DAMIEN","Votre collègue a raison. Le paiement minimum sert à garder le compte en règle, pas à rembourser la dette. Vous avez trois façons de sortir de là, et elles ne coûtent pas la même chose."],
      ["MARLÈNE","Trois façons ? Je pensais qu'il y avait juste payer plus vite."],
      ["DAMIEN","Payer plus vite est la quatrième, et c'est la meilleure quand on peut. Les trois autres, c'est de remplacer une dette chère par une dette moins chère. Première façon : la marge de crédit."],
      ["MARLÈNE","La marge de crédit. Excusez-moi, c'est quoi la différence avec la carte ?"],
      ["DAMIEN","La marge, c'est une réserve d'argent à laquelle vous piochez quand vous voulez, et vous payez de l'intérêt seulement sur ce que vous avez pris. Ici, elle serait à neuf et quarante-cinq."],
      ["MARLÈNE","Neuf et quarante-cinq au lieu de dix-neuf et quatre-vingt-dix. C'est la moitié."],
      ["DAMIEN","C'est la moitié. Le piège de la marge, c'est qu'elle ne vous oblige à rien. Vous pouvez payer cinquante dollars par mois pendant quinze ans sans que personne vous appelle."],
      ["MARLÈNE","Et la deuxième façon ?"],
      ["DAMIEN","Le prêt personnel. Onze et vingt, un peu plus cher que la marge, mais avec une date de fin. Quatre-vingts mensualités fixes, et le dernier jour est écrit dans le contrat."],
      ["MARLÈNE","Donc la marge est moins chère, mais le prêt me force à finir. Vous, vous me conseilleriez lequel ?"],
      ["DAMIEN","Je vous poserais une question avant : est-ce que vous avez déjà remboursé une marge au complet dans votre vie ?"],
      ["MARLÈNE","Non. Jamais eu de marge."],
      ["DAMIEN","Alors le prêt est probablement plus prudent. Ce n'est pas une question de taux, c'est une question de discipline, et ça ne se calcule pas."],
      ["MARLÈNE","Et la troisième façon ?"],
      ["DAMIEN","Prendre l'argent que vous avez déjà. Vous m'avez dit six mille deux cents dollars dans un compte chèque, qui ne rapportent rien. Ces six mille-là vous coûtent dix-neuf pour cent tant que la carte n'est pas payée."],
      ["MARLÈNE","C'est l'argent du cégep de ma fille. Ça, je ne veux pas y toucher."],
      ["DAMIEN","Je le comprends, et c'est votre décision. Je vous demande seulement de la prendre en sachant qu'elle vous coûte à peu près mille deux cents dollars par année."],
      ["MARLÈNE","Mille deux cents par année. Vous pouvez me le mettre sur un papier, ce calcul-là ?"],
      ["DAMIEN","Bien sûr. Une dernière chose, avant que vous partiez : je vais vous demander la permission de regarder votre dossier de crédit. C'est lui qui décide du taux que je peux vous offrir."],
      ["MARLÈNE","Mon dossier de crédit. Je n'ai jamais vu le mien."],
      ["DAMIEN","Vous pouvez le demander vous-même, gratuitement, aux deux agences. Faites-le avant de revenir : ça ne change rien à votre pointage, et vous saurez ce que je vois."],
    ]
  },

  t2: {
    label: "Dialogue — Où mettre l'argent qui reste",
    lines: [
      ["NATHALIE","Bonjour madame Saint-Preux. Nathalie Pomerleau, planificatrice financière. Mon collègue m'a dit que vous aviez réglé la question de la carte."],
      ["MARLÈNE","Presque. J'ai pris le prêt personnel à onze et vingt, quatre-vingts mensualités. Et j'ai gardé les six mille deux cents pour ma fille."],
      ["NATHALIE","C'est de ça que je voulais vous parler. Ces six mille deux cents-là sont dans un compte chèque. Vous savez ce qu'ils vous rapportent ?"],
      ["MARLÈNE","Rien du tout, je pense."],
      ["NATHALIE","À peu près rien, oui. Il y a trois façons courantes de les faire travailler, et le choix dépend d'une seule chose : quand est-ce que vous en avez besoin ?"],
      ["MARLÈNE","Dans deux ans. Jessie commence le cégep en août dans deux ans, et il y a un ordinateur portable à acheter avant."],
      ["NATHALIE","Deux ans, c'est court. Ça élimine tout de suite les placements qui montent et qui descendent. Il vous reste le compte d'épargne, le dépôt à terme et le CELI."],
      ["MARLÈNE","Le CELI, j'en entends parler. Mais je n'ai jamais compris si c'est un compte ou si c'est un placement."],
      ["NATHALIE","Excellente question, et personne ne l'explique jamais. Le CELI n'est pas un placement : c'est un abri. Vous mettez ce que vous voulez dedans, et ce qui pousse à l'intérieur n'est pas imposé."],
      ["MARLÈNE","Donc je peux mettre un dépôt à terme dans un CELI ?"],
      ["NATHALIE","Vous pouvez, et c'est souvent ce qu'on fait pour un projet à deux ans. Le dépôt à terme vous donne un taux connu d'avance, trois et dix ici, et le CELI fait que les intérêts ne sont pas imposables."],
      ["MARLÈNE","Et le REER, c'est la même chose ?"],
      ["NATHALIE","Non, et c'est là que les gens se trompent. Le REER, vous déduisez ce que vous y mettez, mais vous payez de l'impôt quand vous le sortez. Pour l'argent du cégep de votre fille, ce serait une mauvaise idée."],
      ["MARLÈNE","Attendez. Vous avez dit « déduisez ». Ça veut dire que je paie moins d'impôt cette année ?"],
      ["NATHALIE","Cette année, oui. Et vous en payez plus l'année où vous retirez. Le REER n'efface pas l'impôt : il le déplace vers un moment où vous gagnez moins, comme la retraite."],
      ["MARLÈNE","D'accord. Et si la caisse fait faillite, moi, je perds mon argent ?"],
      ["NATHALIE","Non. Les dépôts sont protégés par l'Autorité des marchés financiers, jusqu'à cent mille dollars par catégorie de dépôts, par personne et par institution. Ça ne coûte rien et ça se fait tout seul."],
      ["MARLÈNE","Cent mille. Je suis loin du compte."],
      ["NATHALIE","Vous êtes loin du compte, et c'est très bien. Une dernière chose, parce que ça revient souvent : si quelqu'un vous appelle pour vous offrir un placement garanti à douze pour cent, c'est une fraude."],
      ["MARLÈNE","Comment est-ce qu'on fait pour le savoir ?"],
      ["NATHALIE","Deux choses. Un rendement élevé sans risque, ça n'existe pas. Et avant d'investir un sou, on vérifie la personne dans le registre de l'Autorité des marchés financiers. C'est public et c'est gratuit."],
      ["MARLÈNE","Je vais noter ça. Est-ce que je peux repartir avec la documentation et la lire chez nous ?"],
      ["NATHALIE","Je vous la prépare. Prenez le temps de la lire : personne n'a jamais perdu d'argent en attendant une semaine."],
    ]
  },

  t3: {
    label: "Dialogue — Sept cent quatre-vingts dollars",
    lines: [
      ["STEVE","Service de la sécurité des cartes, Steve Dumouchel, bonjour."],
      ["MARLÈNE","Bonjour. J'appelle parce qu'il y a une opération sur mon relevé que je n'ai pas faite. Sept cent quatre-vingts dollars, le quatorze."],
      ["STEVE","D'accord. Avant tout : est-ce que vous avez encore votre carte en main ?"],
      ["MARLÈNE","Oui, elle est dans mon portefeuille. Je ne l'ai jamais perdue."],
      ["STEVE","Donc c'est un achat à distance. Le commerçant apparaît comme un magasin en ligne, c'est bien ça ? Vous n'avez rien acheté chez eux ?"],
      ["MARLÈNE","Rien. Je n'ai jamais entendu ce nom-là de ma vie."],
      ["STEVE","Je bloque la carte immédiatement et je vous en fais émettre une nouvelle. Vous devriez la recevoir dans cinq jours ouvrables."],
      ["MARLÈNE","Attendez, vous la bloquez tout de suite ? Et mes paiements automatiques ?"],
      ["STEVE","Bonne question, et il faut y penser. Les paiements automatiques rattachés à cette carte vont tomber. Vous devrez donner le nouveau numéro à chaque commerçant. Je préfère vous le dire maintenant plutôt que de vous laisser le découvrir."],
      ["MARLÈNE","Bon. Bloquez-la. Mais les sept cent quatre-vingts dollars, je les paie ou je ne les paie pas ?"],
      ["STEVE","Vous ne les payez pas. Une opération non autorisée, ce n'est pas la vôtre. J'ouvre un dossier de contestation aujourd'hui, et le montant est retiré de votre solde pendant l'enquête."],
      ["MARLÈNE","Et si l'enquête dit que c'est moi ?"],
      ["STEVE","Alors le montant reviendrait sur votre relevé, et vous pourriez contester à nouveau par écrit. Mais dans un cas comme le vôtre, où la carte est restée en votre possession, c'est rare."],
      ["MARLÈNE","Il y a autre chose qui me chicote. La semaine passée, j'ai reçu un message texte qui disait que ma carte était bloquée et qu'il fallait cliquer."],
      ["STEVE","Est-ce que vous avez cliqué ?"],
      ["MARLÈNE","J'ai cliqué, oui. Il y avait une page qui demandait mon numéro de carte. Je l'ai fermée avant d'écrire quoi que ce soit, mais j'ai cliqué."],
      ["STEVE","Le lien seul ne donne pas votre numéro. Mais ça s'appelle de l'hameçonnage, et ça explique peut-être comment ils ont su à quelle banque écrire. Nous ne demandons jamais un numéro de carte par message."],
      ["MARLÈNE","Jamais ?"],
      ["STEVE","Jamais. Ni le numéro, ni le NIP, ni le code de trois chiffres derrière. Si quelqu'un vous les demande, c'est qu'il n'est pas de chez nous."],
      ["MARLÈNE","Est-ce que je peux avoir quelque chose par écrit ? Un numéro de dossier, quelque chose ?"],
      ["STEVE","Je vous donne le numéro de dossier tout de suite, et je vous envoie la confirmation par la poste. Notez aussi l'heure de cet appel-ci et mon nom."],
      ["MARLÈNE","C'est noté. Steve Dumouchel, onze heures vingt."],
      ["STEVE","Une dernière chose, madame Saint-Preux. Si le montant n'a pas disparu de votre relevé dans trente jours, écrivez-nous une lettre plutôt que de rappeler. Un écrit laisse une trace ; un appel, non."],
    ]
  },
};
