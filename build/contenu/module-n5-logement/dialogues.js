const DIALOGUES = {
  prep: {
    label: "Dialogue — L'avis dans la boîte aux lettres",
    lines: [
      ["NADÈGE","Bonjour. J'ai reçu un papier de mon propriétaire et je ne suis pas certaine de le comprendre."],
      ["SAMUEL","Assoyez-vous. Vous permettez que je le regarde ? … D'accord. C'est un avis de modification du bail."],
      ["NADÈGE","Modification, ça veut dire qu'il me met dehors ?"],
      ["SAMUEL","Non, pas du tout. Il vous annonce ce qu'il veut changer pour l'année prochaine. Ici, il demande soixante-quinze dollars de plus par mois."],
      ["NADÈGE","Et là, en bas ? Il y a une ligne sur le stationnement."],
      ["SAMUEL","Il veut aussi vous enlever la case de stationnement. Ça, c'est un deuxième changement, et il doit l'écrire séparément."],
      ["NADÈGE","Est-ce que je suis obligée de dire oui ?"],
      ["SAMUEL","Vous avez un mois pour répondre. Vous pouvez accepter, ou refuser par écrit. Si vous refusez, c'est lui qui doit s'adresser au Tribunal administratif du logement."],
      ["NADÈGE","Un mois. Et si je ne réponds rien du tout ?"],
      ["SAMUEL","Si vous ne répondez pas, la loi considère que vous avez accepté. C'est pour ça qu'il ne faut jamais laisser cet avis sur la table de cuisine."],
      ["NADÈGE","De toute façon, ma fille dort dans le salon. Je pense que je vais chercher un quatre et demie."],
      ["SAMUEL","Alors commençons par là. Regardez les annonces, notez tout ce qu'on vous dit au téléphone, et rappelez-moi avant de signer quoi que ce soit."]
    ]
  },

  t1: {
    label: "Dialogue — Je vous appelle pour l'annonce",
    lines: [
      ["HÉLÈNE","Oui, allô ?"],
      ["NADÈGE","Bonjour, madame. Je vous appelle pour le quatre et demie de la rue Bowen. Est-ce qu'il est encore libre ?"],
      ["HÉLÈNE","Il est encore libre, oui. Le premier juillet."],
      ["NADÈGE","Parfait. J'aimerais vous poser quelques questions, si vous avez deux minutes. Je prends des notes."],
      ["HÉLÈNE","Allez-y."],
      ["NADÈGE","Le loyer est de mille cinquante dollars. Est-ce que le chauffage est inclus ?"],
      ["HÉLÈNE","Le chauffage n'est pas inclus. C'est électrique, et c'est à la charge du locataire. Comptez à peu près cent dollars par mois l'hiver."],
      ["NADÈGE","Cent dollars l'hiver, d'accord. Et les électroménagers ?"],
      ["HÉLÈNE","Le poêle et le réfrigérateur sont fournis. La laveuse et la sécheuse, non, mais il y a une buanderie au sous-sol."],
      ["NADÈGE","Excusez-moi, vous pouvez répéter le dernier mot ?"],
      ["HÉLÈNE","Une buanderie. Deux laveuses et deux sécheuses, au sous-sol de l'immeuble, deux dollars la brassée."],
      ["NADÈGE","Merci. Et pour le stationnement ?"],
      ["HÉLÈNE","Il y a une case derrière l'immeuble, incluse dans le loyer. Une seule, par exemple."],
      ["NADÈGE","Une seule, ça me suffit. Dernière question : est-ce que je peux visiter cette semaine ?"],
      ["HÉLÈNE","Jeudi soir, dix-huit heures ? L'adresse, c'est le quatre cent douze, rue Bowen, appartement trois."],
      ["NADÈGE","Jeudi dix-huit heures, quatre cent douze Bowen, appartement trois. C'est noté. Merci beaucoup, madame."]
    ]
  },

  t1b: {
    label: "Dialogue — Qu'est-ce qu'elle vous a dit ?",
    lines: [
      ["SAMUEL","Puis, cet appel ? Vous avez pris des notes ?"],
      ["NADÈGE","J'ai tout écrit. Elle me dit que le logement est libre le premier juillet et que le loyer est de mille cinquante dollars."],
      ["SAMUEL","Est-ce que vous lui avez demandé si le chauffage était compris ?"],
      ["NADÈGE","C'est la première chose que j'ai demandée. Elle m'explique que le chauffage est électrique et qu'il n'est pas inclus."],
      ["SAMUEL","Donc il faut ajouter cent dollars par mois à votre calcul, au moins l'hiver."],
      ["NADÈGE","Elle me dit aussi qu'il y a une buanderie au sous-sol et qu'une case de stationnement vient avec le loyer."],
      ["SAMUEL","Et vous savez ce qui n'est pas fourni ?"],
      ["NADÈGE","La laveuse et la sécheuse. Le poêle et le réfrigérateur, eux, sont là."],
      ["SAMUEL","Vous avez posé les bonnes questions. Il vous manque juste ce que personne ne pense à demander : le bruit, l'isolation, et depuis quand le loyer n'a pas augmenté."],
      ["NADÈGE","Ça, je le demanderai jeudi, pendant la visite."]
    ]
  },

  t2: {
    label: "Dialogue — La visite du quatre et demie",
    lines: [
      ["HÉLÈNE","Entrez, entrez. Vous enlevez vos bottes, si ça ne vous dérange pas."],
      ["NADÈGE","Bien sûr. Oh, c'est clair, ici."],
      ["HÉLÈNE","C'est la pièce que tout le monde aime. Les fenêtres donnent au sud, alors le salon est ensoleillé jusqu'à quatre heures."],
      ["NADÈGE","Et le plancher, c'est du bois franc ?"],
      ["HÉLÈNE","Du bois franc dans le salon et dans le corridor. Les chambres, c'est du flottant, refait l'an dernier."],
      ["NADÈGE","Il y a deux chambres ?"],
      ["HÉLÈNE","Deux vraies chambres, oui. Celle-ci donne sur la cour, donc c'est la plus tranquille. En arrivant, vous avez vu la ruelle : c'est de ce côté-là qu'il y a du passage."],
      ["NADÈGE","Ma fille prendrait celle qui donne sur la cour, alors. Est-ce que c'est insonorisé entre les logements ?"],
      ["HÉLÈNE","Honnêtement, on entend marcher au-dessus. Ce n'est pas un immeuble neuf. Les voisins d'en haut sont un couple retraité, très tranquilles."],
      ["NADÈGE","Merci de me le dire. Et la cuisine, la hotte fonctionne ?"],
      ["HÉLÈNE","Elle fonctionne. Le poêle et le réfrigérateur restent. Là, derrière la porte, c'est une remise : c'est petit, mais ça prend deux vélos."],
      ["NADÈGE","Ça, c'est utile. Une dernière chose, madame : depuis quand le loyer n'a pas augmenté ?"],
      ["HÉLÈNE","Bonne question. Le locataire actuel payait mille vingt dollars, et il est ici depuis trois ans. Je vais l'écrire dans le bail, c'est obligatoire."],
      ["NADÈGE","Je vous remercie. En regardant les autres logements cette semaine, je vais comparer, mais je vous rappelle vendredi."],
      ["HÉLÈNE","Prenez le temps qu'il faut. Je garde votre numéro."]
    ]
  },

  t3: {
    label: "Dialogue — Avant de signer",
    lines: [
      ["HÉLÈNE","Voilà le bail. C'est le formulaire officiel, le même pour tout le monde au Québec."],
      ["NADÈGE","Je vais le lire au complet, si vous permettez. … Ici, la section G, c'est quoi ?"],
      ["HÉLÈNE","C'est l'avis au nouveau locataire. Je dois y écrire le loyer le plus bas payé dans les douze derniers mois. Mille vingt dollars, comme je vous l'ai dit."],
      ["NADÈGE","Et moi, qu'est-ce que je peux faire avec cette information ?"],
      ["HÉLÈNE","Si vous trouvez que l'augmentation est trop forte, vous avez dix jours après la signature pour demander une révision au Tribunal."],
      ["NADÈGE","Dix jours. Je le note. Le bail se termine quand ?"],
      ["HÉLÈNE","Le trente juin de l'année prochaine. Après, il se renouvellera tout seul aux mêmes conditions, sauf si l'un de nous deux envoie un avis."],
      ["NADÈGE","Donc si je ne dis rien, je reste."],
      ["HÉLÈNE","C'est exactement ça. Au Québec, le bail se renouvelle automatiquement. C'est une protection pour le locataire."],
      ["NADÈGE","Et cette feuille-là, avec les règlements de l'immeuble ?"],
      ["HÉLÈNE","C'est l'annexe. Elle fait partie du bail : pas de tapis dans l'escalier, les poubelles le mardi, et pas de barbecue sur le balcon. C'est le règlement de l'assureur, pas le mien."],
      ["NADÈGE","Une dernière chose : si je dois partir avant la fin, est-ce que j'ai le droit de sous-louer ?"],
      ["HÉLÈNE","Vous avez le droit de sous-louer ou de céder votre bail. Vous devez m'aviser par écrit, et je ne peux refuser sans un motif sérieux."],
      ["NADÈGE","C'est clair. Alors je signe."]
    ]
  },
};
