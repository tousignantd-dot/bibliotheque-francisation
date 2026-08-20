const DIALOGUES = {
  prep: {
    label: "Dialogue — Au comptoir du centre sportif",
    lines: [
      ["ROSA","Bonjour. Je voudrais inscrire mon garçon à un cours de natation. Il a neuf ans."],
      ["LOUISE","Bonjour. Neuf ans, parfait. On a deux groupes : le samedi matin et le mardi après l'école."],
      ["ROSA","Le samedi matin, ce serait mieux. À quelle heure exactement ?"],
      ["LOUISE","De neuf heures à dix heures. Douze semaines, de septembre à décembre."],
      ["ROSA","Et ça coûte combien ?"],
      ["LOUISE","Quatre-vingt-cinq dollars pour les résidents de la ville. Cent dix pour les autres."],
      ["ROSA","J'habite ici depuis un an. Qu'est-ce que je dois apporter comme preuve ?"],
      ["LOUISE","Une facture d'électricité ou un bail à votre nom. N'importe quel document récent avec l'adresse."],
      ["ROSA","D'accord. Et il faut apporter quoi, pour le cours ?"],
      ["LOUISE","Maillot, serviette, et des sandales pour le bord de la piscine. Le bonnet de bain est obligatoire."],
      ["ROSA","Le bonnet est obligatoire. Vous en vendez ici ?"],
      ["LOUISE","Oui, cinq dollars au comptoir. Prenez-en un tout de suite, ça évite un retour."],
      ["ROSA","Alors : samedi neuf heures, quatre-vingt-cinq dollars, une preuve d'adresse, et le bonnet."],
      ["LOUISE","C'est exactement ça. Vous pouvez vous inscrire en ligne ou ici, comme vous voulez."],
    ]
  },

  t1: {
    label: "Dialogue — Il faut que je sache quoi apporter",
    lines: [
      ["ROSA","Je rappelle pour le cours de natation. Il y a des choses que je n'ai pas notées."],
      ["LOUISE","Allez-y, je vous écoute."],
      ["ROSA","Est-ce qu'il faut que mon garçon sache déjà nager ?"],
      ["LOUISE","Non. Le groupe du samedi, c'est le niveau débutant. Il est important qu'il n'ait pas peur de l'eau, c'est tout."],
      ["ROSA","Et s'il manque un cours ?"],
      ["LOUISE","Il n'y a pas de reprise, mais ce n'est pas grave : chaque cours reprend ce qui a été vu."],
      ["ROSA","Est-ce que je peux rester pour regarder ?"],
      ["LOUISE","Il est préférable que les parents restent dans la salle d'attente. Les enfants écoutent mieux."],
      ["ROSA","Je comprends. Il y a une fenêtre pour voir ?"],
      ["LOUISE","Oui, une grande vitre du côté du corridor. Plusieurs parents s'installent là."],
      ["ROSA","Parfait. Et pour l'inscription, il faut que je vienne en personne ?"],
      ["LOUISE","Pas nécessairement. Mais si vous payez en ligne, il faut quand même apporter la preuve d'adresse au premier cours."],
    ]
  },

  t2: {
    label: "Dialogue — Les consignes du moniteur",
    lines: [
      ["KEVIN","Tout le monde s'assoit au bord ! Les pieds dans l'eau, on ne saute pas."],
      ["KEVIN","Mateo, mets-toi à côté de Sofia. Non, ne te lève pas, reste assis."],
      ["KEVIN","Prenez la planche à deux mains. Tenez-la bien devant vous, ne la lâchez pas."],
      ["KEVIN","On y va doucement. Poussez avec les jambes, une fois, deux fois."],
      ["KEVIN","Mateo, regarde-moi. Souffle dans l'eau, comme ça. Ne ferme pas les yeux."],
      ["KEVIN","Très bien ! Recommence, mais plus lentement cette fois."],
      ["KEVIN","On se replace en ligne. Laissez la planche au bord, ne la jetez pas dans l'eau."],
      ["KEVIN","Dernier tour, et après on sort. Sortez par l'échelle, pas par le bord."],
    ]
  },

  t2b: {
    label: "Dialogue — Rosa donne un coup de main",
    lines: [
      ["DENIS","Rosa, tu peux m'aider deux minutes ? Il me manque quelqu'un pour les petits."],
      ["ROSA","Oui, bien sûr. Qu'est-ce que je fais ?"],
      ["DENIS","Assieds-toi au bout, là. Compte-les quand ils entrent dans l'eau."],
      ["ROSA","Je les compte, d'accord. Et s'il en manque un ?"],
      ["DENIS","Tu me le dis tout de suite, tu ne le cherches pas toi-même."],
      ["ROSA","Compris. Et les serviettes ?"],
      ["DENIS","Donne-les-leur à la sortie, pas avant. Sinon elles traînent par terre."],
      ["ROSA","Ne pas les donner avant. Autre chose ?"],
      ["DENIS","Si un enfant a froid, envoie-le à la douche chaude. N'attends pas qu'il pleure."],
      ["ROSA","D'accord. Compter, garder les serviettes, envoyer à la douche."],
      ["DENIS","C'est ça. Merci, ça m'aide beaucoup."],
    ]
  },

  t3: {
    label: "Dialogue — Le dépliant de la ville",
    lines: [
      ["ROSA","J'ai reçu le dépliant de la ville. Il y a une trentaine d'activités là-dedans."],
      ["DENIS","Regarde d'abord la colonne de gauche : c'est le nom de l'activité et l'âge."],
      ["ROSA","Et les chiffres à droite ?"],
      ["DENIS","Le premier, c'est le prix pour les résidents. Le deuxième, pour les autres. Le troisième, c'est le nombre de semaines."],
      ["ROSA","Il y a des petites étoiles à côté de certaines activités."],
      ["DENIS","Ça veut dire qu'il reste peu de places. En bas de la page, la légende l'explique."],
      ["ROSA","La chorale du jeudi soir a une étoile. C'est celle qui m'intéresse le plus."],
      ["DENIS","Alors inscris-toi cette semaine. Les places partent vite quand il y a une étoile."],
      ["ROSA","C'est la moins chère de toutes, en plus. Trente dollars pour dix semaines."],
      ["DENIS","C'est le tarif des activités sans matériel. La natation coûte plus cher à cause de la piscine."],
    ]
  },

  t3b: {
    label: "Dialogue — Deux façons de dire la même chose",
    lines: [
      ["KEVIN","Envoye, embarque ! On commence dans deux minutes !"],
      ["ROSA","Pardon ? Je n'ai pas compris."],
      ["KEVIN","Excusez-moi. Je voulais dire : entrez dans l'eau, s'il vous plaît. On commence bientôt."],
      ["ROSA","Ah, d'accord. Merci."],
      ["LOUISE","Kevin parle vite quand il est au bord de la piscine. Avec les parents, il est plus tranquille."],
      ["ROSA","Ce n'est pas la même façon de parler ?"],
      ["LOUISE","Non. Au comptoir, on vouvoie et on parle lentement. Au bord de la piscine, c'est court et direct."],
      ["ROSA","Alors les deux sont corrects ?"],
      ["LOUISE","Les deux sont corrects, mais pas dans la même situation. C'est ça qu'il faut apprendre."],
    ]
  },

  appli: {
    label: "Dialogue — S'inscrire à la chorale",
    lines: [
      ["ROSA","Bonjour, je voudrais m'inscrire à la chorale du jeudi soir."],
      ["LOUISE","Bonjour. Il reste trois places. C'est de dix-neuf à vingt et une heures, dix semaines."],
      ["ROSA","Est-ce qu'il faut savoir lire la musique ?"],
      ["LOUISE","Pas du tout. Il est important d'avoir envie de chanter, c'est tout."],
      ["ROSA","Et il faut apporter quelque chose ?"],
      ["LOUISE","Une bouteille d'eau et un crayon. Les partitions sont fournies."],
      ["ROSA","Trente dollars, c'est bien ça ?"],
      ["LOUISE","Trente pour les résidents. Avez-vous votre preuve d'adresse avec vous ?"],
      ["ROSA","Oui, j'ai une facture d'électricité. Donnez-moi une minute, je la cherche."],
      ["LOUISE","Prenez votre temps. Je remplis le formulaire pendant ce temps-là."],
    ]
  },
};
