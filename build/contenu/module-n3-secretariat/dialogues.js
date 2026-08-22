const DIALOGUES = {
  prep: {
    label: "Dialogue — Il faut le dire au secrétariat",
    lines: [
      ["NAWEL","Tariq, je ne serai pas là jeudi. Ma fille a un rendez-vous à la clinique."],
      ["TARIQ","Tu l'as dit à l'enseignante ?"],
      ["NAWEL","Non, pas encore. Je vais lui dire jeudi matin, en arrivant."],
      ["TARIQ","Jeudi matin, tu ne seras pas là ! Il faut le dire avant."],
      ["NAWEL","Avant ? À qui ?"],
      ["TARIQ","Au secrétariat. C'est le bureau en bas, à côté de la porte d'entrée."],
      ["NAWEL","Le grand comptoir avec la dame ?"],
      ["TARIQ","Oui. La secrétaire s'appelle madame Cloutier. Elle est très gentille."],
      ["NAWEL","Et je dis quoi ?"],
      ["TARIQ","Ton nom, ton prénom, ton groupe, et le jour où tu vas être absente."],
      ["NAWEL","Mon groupe… je suis dans le groupe 12, l'avant-midi."],
      ["TARIQ","C'est ça. Elle écrit ton absence dans ton dossier et elle prévient l'enseignante."],
      ["NAWEL","Et si je ne dis rien ?"],
      ["TARIQ","Ton absence reste dans le dossier, mais sans raison. Ce n'est pas pareil."]
    ]
  },

  t1: {
    label: "Dialogue — Je vais être absente jeudi",
    lines: [
      ["NAWEL","Bonjour, madame."],
      ["GINETTE","Bonjour ! Qu'est-ce que je peux faire pour vous ?"],
      ["NAWEL","Je vais être absente jeudi. Je viens le dire avant."],
      ["GINETTE","Merci de venir avant, c'est ce qu'il faut faire. Votre nom, s'il vous plaît ?"],
      ["NAWEL","Nawel Belkacem. B, E, L, K, A, C, E, M."],
      ["GINETTE","Et votre groupe ?"],
      ["NAWEL","Groupe 12, l'avant-midi."],
      ["GINETTE","Parfait. Jeudi… le 12 mars. Toute la journée ou l'avant-midi seulement ?"],
      ["NAWEL","L'avant-midi seulement. Le rendez-vous est à neuf heures."],
      ["GINETTE","La raison, en une phrase ?"],
      ["NAWEL","Ma fille a un rendez-vous à la clinique et je dois y aller avec elle."],
      ["GINETTE","D'accord. J'écris : absence prévenue, jeudi 12 mars, avant-midi."],
      ["NAWEL","Est-ce que je dois apporter un papier ?"],
      ["GINETTE","Pour une demi-journée, non. Mais si la clinique vous en donne un, apportez-le."],
      ["NAWEL","Merci beaucoup, madame. Bonne journée."],
      ["GINETTE","Bonne journée. Et demandez à une camarade ce que vous avez manqué."]
    ]
  },

  t2: {
    label: "Dialogue — J'apporte mon billet",
    lines: [
      ["NAWEL","Bonjour, madame Cloutier. J'ai été absente la semaine passée."],
      ["GINETTE","Bonjour. Votre nom et votre groupe, s'il vous plaît ?"],
      ["NAWEL","Nawel Belkacem, groupe 12."],
      ["GINETTE","Quelles journées avez-vous manquées ?"],
      ["NAWEL","Lundi, mardi et mercredi. J'avais la grippe."],
      ["GINETTE","Trois journées. Vous avez un papier ?"],
      ["NAWEL","Oui, un billet de la clinique. Le voici."],
      ["GINETTE","Voyons voir… Il y a la date, votre nom, la signature de la médecin. C'est complet."],
      ["NAWEL","Est-ce que le billet est bon pour les trois jours ?"],
      ["GINETTE","Oui. Il dit « du 3 au 5 mars ». Les trois journées sont justifiées."],
      ["NAWEL","Est-ce que je peux garder l'original ?"],
      ["GINETTE","Bien sûr. Je fais une photocopie et je vous rends le papier."],
      ["NAWEL","Merci. Et mon enseignante, est-ce qu'elle va le savoir ?"],
      ["GINETTE","Elle le verra dans le dossier. Passez la voir avant le cours : elle va vous dire ce qu'il faut reprendre."]
    ]
  },

  t3: {
    label: "Dialogue — Je dois arrêter le cours",
    lines: [
      ["NAWEL","Bonjour, monsieur. C'est vous qui remplacez madame Cloutier ?"],
      ["MARC","Oui, ce matin. Marc Ferland, à l'accueil. Je vous écoute."],
      ["NAWEL","Nawel Belkacem, groupe 12. Je dois arrêter le cours."],
      ["MARC","Je vous écoute jusqu'au bout. Prenez votre temps."],
      ["NAWEL","Je commence un travail à temps plein le premier avril. Le matin, je ne pourrai plus venir."],
      ["MARC","Je comprends. Quel est votre dernier jour de cours ?"],
      ["NAWEL","Le vendredi 28 mars."],
      ["MARC","Vendredi 28 mars. Vous arrêtez pour un temps, ou vous abandonnez le cours ?"],
      ["NAWEL","Quelle est la différence ?"],
      ["MARC","Si vous arrêtez pour un temps, je note la date et le dossier reste ouvert. Si vous abandonnez, je ferme le dossier."],
      ["NAWEL","Alors j'abandonne. Je ne pourrai pas revenir avant l'automne."],
      ["MARC","D'accord. Voulez-vous en parler à votre enseignante avant de partir ?"],
      ["NAWEL","Oui, je vais aller la voir. Est-ce que je peux avoir un papier qui prouve que j'ai suivi le cours ?"],
      ["MARC","Une attestation de fréquentation. Elle est prête en trois jours. Il faut la demander avant de partir, jamais après."],
      ["NAWEL","Je la demande aujourd'hui, alors. Où est-ce que je la prends ?"],
      ["MARC","Ici, au comptoir, vendredi prochain. Vous signez le formulaire et je vous la remets en main propre."]
    ]
  },

  appli: {
    label: "Dialogue — Tariq annonce son absence",
    lines: [
      ["TARIQ","Bonjour, madame. Je m'appelle Tariq Haddad, groupe 12."],
      ["GINETTE","Bonjour, monsieur Haddad. Qu'est-ce qui vous amène ?"],
      ["TARIQ","Je vais être absent lundi et mardi prochains."],
      ["GINETTE","Les deux journées complètes ?"],
      ["TARIQ","Oui. Je déménage, et le camion vient lundi matin."],
      ["GINETTE","J'inscris : absence prévenue, lundi et mardi, journées complètes."],
      ["TARIQ","Est-ce que j'apporte un papier ?"],
      ["GINETTE","Pour un déménagement, il n'y en a pas. Votre parole suffit, monsieur Haddad."]
    ]
  },
};
