const DIALOGUES = {
  prep: {
    label: "Dialogue — Je voudrais m'inscrire",
    lines: [
      ["YARA","Bonjour. Je voudrais m'inscrire au cours de français."],
      ["MME BOURGEOIS","Bonjour ! Vous êtes au bon endroit. C'est ici, le secrétariat."],
      ["YARA","C'est possible aujourd'hui ?"],
      ["MME BOURGEOIS","Oui. Voici le formulaire d'inscription."],
      ["YARA","Il y a beaucoup de cases…"],
      ["MME BOURGEOIS","On les remplit ensemble. Une case à la fois."],
      ["YARA","D'accord. Merci beaucoup, madame."],
      ["MME BOURGEOIS","Asseyez-vous. On commence par votre nom."]
    ]
  },

  t1: {
    label: "Dialogue — L'annonce sur le babillard",
    lines: [
      ["MARCO","Yara, regarde ce papier. C'est pour toi."],
      ["YARA","C'est quoi ?"],
      ["MARCO","Une annonce. Un cours de français, au Centre Delorme."],
      ["YARA","Ça commence quand ?"],
      ["MARCO","Le 7 septembre. Et ça finit le 11 décembre."],
      ["YARA","Et c'est à quelle heure ?"],
      ["MARCO","De 8 h 30 à 12 h 30, du lundi au vendredi."],
      ["YARA","Le matin, alors. C'est parfait."],
      ["MARCO","L'inscription, c'est au local 005. Écris ça."],
      ["YARA","J'écris la date, l'heure et le local. Merci, Marco !"]
    ]
  },

  t1b: {
    label: "Dialogue — J'appelle le secrétariat",
    lines: [
      ["YARA","Bonjour. C'est pour le cours de français."],
      ["MME BOURGEOIS","Bonjour. Oui, je vous écoute."],
      ["YARA","L'inscription, c'est quel jour ?"],
      ["MME BOURGEOIS","Du 24 au 28 août, de 9 h à 15 h."],
      ["YARA","Du 24 au 28 août. Et c'est où ?"],
      ["MME BOURGEOIS","Au local 005, au rez-de-chaussée."],
      ["YARA","J'apporte quelque chose ?"],
      ["MME BOURGEOIS","Une pièce d'identité. C'est tout."]
    ]
  },

  t2: {
    label: "Dialogue — Case par case",
    lines: [
      ["MME BOURGEOIS","Votre nom de famille, s'il vous plaît."],
      ["YARA","Haddad."],
      ["MME BOURGEOIS","Et votre prénom ?"],
      ["YARA","Yara."],
      ["MME BOURGEOIS","Votre date de naissance ?"],
      ["YARA","Le 7 mars 1994."],
      ["MME BOURGEOIS","Votre adresse ?"],
      ["YARA","3420, rue Papineau, à Montréal."],
      ["MME BOURGEOIS","Combien d'années d'école, dans votre pays ?"],
      ["YARA","Onze ans. Je mets onze dans la case ?"],
      ["MME BOURGEOIS","Oui, onze. C'est la case « scolarité »."]
    ]
  },

  t2b: {
    label: "Dialogue — Comment ça s'écrit ?",
    lines: [
      ["MME BOURGEOIS","Haddad… Comment ça s'écrit ?"],
      ["YARA","H, A, deux D, A, D."],
      ["MME BOURGEOIS","Deux D ? Doucement, s'il vous plaît."],
      ["YARA","H. A. D. D. A. D."],
      ["MME BOURGEOIS","B comme bonjour ou D comme dimanche ?"],
      ["YARA","D comme dimanche."],
      ["MME BOURGEOIS","Merci. Et votre rue ?"],
      ["YARA","Papineau. P, A, P, I, N, E, A, U."],
      ["MME BOURGEOIS","Papineau. C'est bien écrit ?"],
      ["YARA","Oui, c'est ça. Merci, madame."]
    ]
  },

  appli: {
    label: "Dialogue — C'est moi qui explique",
    lines: [
      ["HAMID","Yara, je ne comprends pas cette case."],
      ["YARA","Laquelle ? Montre-moi."],
      ["HAMID","Ici. « Scolarité »."],
      ["YARA","C'est le nombre d'années d'école. Toi, tu as fait combien d'années ?"],
      ["HAMID","Neuf ans."],
      ["YARA","Alors tu écris neuf. Dans la case."],
      ["HAMID","Et ici ? « Signature » ?"],
      ["YARA","Tu écris ton nom à la main, au bas de la page."],
      ["HAMID","Le cours commence quand ?"],
      ["YARA","Le 7 septembre, à 8 h 30. Au local 214."]
    ]
  },
};
