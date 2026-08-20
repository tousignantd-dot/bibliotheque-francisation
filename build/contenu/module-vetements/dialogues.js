const DIALOGUES = {
  prep: {
    label: "Dialogue — Je cherche un manteau d'hiver",
    lines: [
      ["VALÉRIE","Bonjour ! Je peux vous aider ?"],
      ["KOFI","Bonjour. Je cherche un manteau d'hiver. Un vrai, pas une veste."],
      ["VALÉRIE","D'accord. Vous voulez quelque chose pour quelle température ?"],
      ["KOFI","Je ne sais pas. Pour l'hiver d'ici. Je m'habille en trois couches depuis trois ans."],
      ["VALÉRIE","Alors il vous faut un manteau coté moins trente. C'est écrit sur l'étiquette, en petit."],
      ["KOFI","Moins trente ? Il fait vraiment moins trente ?"],
      ["VALÉRIE","Quelques jours par hiver, oui. Avec le vent, ça descend plus bas."],
      ["KOFI","Bon. Vous en avez de quelle taille ?"],
      ["VALÉRIE","Du petit au très grand. Vous faites quelle taille, d'habitude ?"],
      ["KOFI","Moyen, je pense. Mais je ne sais pas si c'est pareil ici."],
      ["VALÉRIE","Ça change d'une marque à l'autre. Le mieux, c'est d'essayer. Les cabines sont au fond."],
      ["KOFI","Je peux en essayer plusieurs ?"],
      ["VALÉRIE","Autant que vous voulez. Prenez-en trois, ça ira plus vite."],
    ]
  },

  t1: {
    label: "Dialogue — Dans la cabine d'essayage",
    lines: [
      ["VALÉRIE","Alors, le moyen ?"],
      ["KOFI","Il est un peu serré aux épaules. Je ne peux pas lever les bras."],
      ["VALÉRIE","Alors c'est trop petit. Un manteau d'hiver doit laisser de la place pour un chandail."],
      ["KOFI","Ah, je n'avais pas pensé à ça."],
      ["VALÉRIE","Essayez le grand. Il va vous sembler trop large, mais c'est normal."],
      ["KOFI","Celui-là est mieux. Les manches sont un peu longues, par exemple."],
      ["VALÉRIE","Elles doivent couvrir le poignet quand vous levez le bras. Montrez-moi… Non, c'est parfait."],
      ["KOFI","Et la longueur ?"],
      ["VALÉRIE","Aux genoux, c'est bien pour attendre l'autobus. Plus court, vous aurez froid aux jambes."],
      ["KOFI","Il est lourd, non ?"],
      ["VALÉRIE","C'est du duvet, il est plus léger qu'il n'en a l'air. Essayez de bouger un peu."],
      ["KOFI","D'accord. Il est chaud, ça c'est sûr."],
    ]
  },

  t2: {
    label: "Dialogue — Ça vous va bien",
    lines: [
      ["DIANE","Kofi ! Tu essaies des manteaux ?"],
      ["KOFI","Diane ! Oui, enfin. Qu'est-ce que tu en penses ?"],
      ["DIANE","Le noir te va bien. Il est sobre, tu pourras le porter au travail."],
      ["KOFI","Et le bleu ?"],
      ["DIANE","Franchement, il est trop grand aux épaules. Le noir tombe mieux."],
      ["KOFI","Tu trouves ? Moi, je le trouvais plus chaud."],
      ["DIANE","La couleur ne change rien à la chaleur. C'est le duvet qui compte."],
      ["KOFI","Bon. Et le capuchon, ça fait bizarre ?"],
      ["DIANE","Pas du tout. En janvier, tu seras content de l'avoir. Prends celui avec la fourrure autour."],
      ["KOFI","Pourquoi la fourrure ?"],
      ["DIANE","Elle coupe le vent sur le visage. Ce n'est pas décoratif, c'est utile."],
      ["KOFI","D'accord. Alors le noir, avec le capuchon."],
    ]
  },

  t2b: {
    label: "Dialogue — L'étiquette d'entretien",
    lines: [
      ["KOFI","Il y a une étiquette dans le col, avec des dessins."],
      ["VALÉRIE","C'est le mode d'entretien. Le bac d'eau avec un chiffre, c'est la température de lavage."],
      ["KOFI","Il y a trente dedans."],
      ["VALÉRIE","Trente degrés, à l'eau froide. Plus chaud, le duvet se tasse et le manteau perd sa chaleur."],
      ["KOFI","Et le triangle barré ?"],
      ["VALÉRIE","Pas d'eau de Javel. Jamais, sur un manteau."],
      ["KOFI","Le carré avec un cercle ?"],
      ["VALÉRIE","La sécheuse. Un point, c'est basse température. Pour le duvet, c'est important : ça le fait regonfler."],
      ["KOFI","Et le fer barré ?"],
      ["VALÉRIE","Pas de repassage. De toute façon, on ne repasse pas un manteau."],
      ["KOFI","Ça se lave combien de fois par hiver ?"],
      ["VALÉRIE","Une ou deux, pas plus. Trop de lavages, ça use le duvet."],
    ]
  },

  t3: {
    label: "Dialogue — Échanger les bottes",
    lines: [
      ["KOFI","Bonjour. J'ai acheté ces bottes pour mon fils, mais elles sont trop petites."],
      ["RÉMI","Bonjour. Vous avez la facture ?"],
      ["KOFI","Oui, la voici. C'était il y a douze jours."],
      ["RÉMI","Parfait, c'est dans les trente jours. Elles ont été portées dehors ?"],
      ["KOFI","Non, seulement essayées dans la maison."],
      ["RÉMI","Alors pas de problème. Vous voulez un échange ou un remboursement ?"],
      ["KOFI","Un échange, si vous avez la pointure au-dessus."],
      ["RÉMI","Je vérifie… Oui, il en reste deux paires. Même modèle, même prix."],
      ["KOFI","Parfait. Et si celles-là ne font pas non plus ?"],
      ["RÉMI","Vous revenez. Les trente jours comptent à partir de l'achat d'aujourd'hui, pas de l'ancien."],
      ["KOFI","Et si je ne trouvais rien, je pourrais être remboursé ?"],
      ["RÉMI","Sur la carte qui a servi à payer, oui. Comptant, c'est remboursé comptant."],
    ]
  },

  t3b: {
    label: "Dialogue — La mise de côté",
    lines: [
      ["DIANE","J'ai vu un manteau pour ma fille, mais je suis payée vendredi."],
      ["VALÉRIE","Vous pouvez le mettre de côté. On le garde quatorze jours."],
      ["DIANE","Il faut payer quelque chose maintenant ?"],
      ["VALÉRIE","Un dépôt, en général vingt pour cent. Le reste quand vous venez le chercher."],
      ["DIANE","Et si je change d'idée ?"],
      ["VALÉRIE","Le dépôt n'est pas remboursé, sauf si le magasin le décide. C'est écrit sur le reçu."],
      ["DIANE","Quatorze jours, c'est ferme ?"],
      ["VALÉRIE","Oui. Après, le vêtement retourne en magasin et le dépôt est perdu."],
      ["DIANE","Alors je viendrai vendredi. Vous notez mon nom ?"],
      ["VALÉRIE","Votre nom et votre numéro. On vous appelle si quelque chose change."],
    ]
  },

  appli: {
    label: "Dialogue — Des bottes pour l'hiver",
    lines: [
      ["KOFI","Bonjour. Je cherche des bottes d'hiver pour moi, cette fois."],
      ["VALÉRIE","Bonjour ! Vous faites quelle pointure ?"],
      ["KOFI","Neuf et demi. Mais mes souliers d'ici sont un peu serrés."],
      ["VALÉRIE","Prenez une demi-pointure de plus pour les bottes. Il faut de la place pour un bas épais."],
      ["KOFI","Ah oui, le bas de laine. Et pour la neige ?"],
      ["VALÉRIE","Cherchez « imperméable » sur l'étiquette, et une semelle avec du relief. Le verglas, c'est le vrai danger."],
      ["KOFI","Celles-ci sont comment ?"],
      ["VALÉRIE","Bonnes pour la ville. Cotées moins vingt, imperméables. Essayez-les avec un bas épais."],
      ["KOFI","Je peux les essayer en marchant ?"],
      ["VALÉRIE","Bien sûr, faites le tour du rayon. Mais pas dehors : après, on ne peut plus les échanger."],
      ["KOFI","Ah, c'est bon à savoir. Merci."],
    ]
  },
};
