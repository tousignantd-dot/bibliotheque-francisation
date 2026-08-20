const DIALOGUES = {
  prep: {
    label: "Dialogue — Il fait quatorze degrés au 4B",
    lines: [
      ["OKSANA","Bertrand, il fait quatorze degrés chez moi. Le calorifère du salon est resté froid toute la nuit."],
      ["BERTRAND","Quatorze ? En novembre, c'est beaucoup trop bas. Est-ce que les autres pièces chauffent ?"],
      ["OKSANA","La cuisine et la chambre, oui. C'est seulement celui du salon qui ne réagit plus, même quand je monte le thermostat à vingt-deux."],
      ["BERTRAND","Avant d'appeler ta propriétaire, descends au panneau électrique. Cherche un disjoncteur qui n'est pas dans le même sens que les autres."],
      ["OKSANA","Attends, je regarde… Oui, il y en a un qui est arrêté au milieu."],
      ["BERTRAND","Pousse-le à fond vers « arrêt », puis ramène-le vers « marche ». S'il retombe tout de suite, ne le touche plus."],
      ["OKSANA","Il vient de retomber. Deux fois."],
      ["BERTRAND","Alors ce n'est pas le thermostat, c'est le circuit. Tu appelles madame Rioux aujourd'hui, pas la semaine prochaine."],
      ["OKSANA","Je n'aime pas déranger les gens pour ça."],
      ["BERTRAND","Tu ne déranges personne : le chauffage fait partie du logement que tu paies. Prends une photo de ton thermomètre avec la date, et note l'heure de ton appel."],
      ["OKSANA","Pourquoi noter tout ça ?"],
      ["BERTRAND","Parce que si elle tarde, tes notes deviennent ta preuve. Et ne t'en fais pas : dans neuf cas sur dix, ça se règle en un coup de fil."],
    ]
  },
  t1: {
    label: "Dialogue — Oksana appelle sa propriétaire",
    lines: [
      ["OKSANA","Bonjour madame Rioux, c'est Oksana Kravets, au 4B. Je vous appelle parce que le calorifère du salon ne chauffe plus depuis avant-hier."],
      ["MME RIOUX","Depuis avant-hier ? Il fallait me prévenir tout de suite, voyons. Il fait combien chez vous ce matin ?"],
      ["OKSANA","Quatorze degrés. J'ai vérifié le panneau électrique : le disjoncteur retombe chaque fois que je le remonte."],
      ["MME RIOUX","Ne le remontez plus, c'est dangereux. Je vais faire venir mon électricien. Il passe déjà chez les locataires du deuxième jeudi matin ; je vais lui demander de monter chez vous après avoir terminé leur installation."],
      ["OKSANA","Jeudi, c'est dans trois jours. Est-ce que je peux avoir un chauffage d'appoint en attendant ?"],
      ["MME RIOUX","Bien sûr. J'en garde deux au sous-sol, dans le local d'entretien. Passez en chercher un ce soir, le concierge vous ouvrira."],
      ["OKSANA","Merci beaucoup. Il y a autre chose, aussi. Il y a une tache brune au plafond de la chambre, et elle grossit."],
      ["MME RIOUX","Une tache brune ? Ça fait combien de temps qu'elle est là ?"],
      ["OKSANA","Ça fait deux semaines. Au début, elle était grande comme une pièce de deux dollars ; maintenant, elle fait la taille d'une assiette."],
      ["MME RIOUX","Vous êtes au dernier étage… ça vient probablement de la toiture. Envoyez-moi une photo par courriel : ça me permettra de constater l'ampleur du dégât avant de faire venir le couvreur."],
      ["OKSANA","Je vous l'envoie ce midi. Est-ce que ces réparations-là sont à ma charge ?"],
      ["MME RIOUX","Pas du tout. Vous payez le loyer ; l'entretien de l'immeuble, c'est ma part du contrat. Vous, tenez-moi seulement au courant si la tache change encore."],
    ]
  },
  t2: {
    label: "Dialogue — Le concierge et le locataire du 3A",
    lines: [
      ["SAMIR","Jean-Philippe, je peux vous parler deux minutes ? C'est au sujet du corridor du troisième."],
      ["JEAN-PHILIPPE","Mes vélos, je suppose. Il y en a trois, je sais. Mais mon logement fait deux pièces et demie, je n'ai aucun rangement."],
      ["SAMIR","Je comprends très bien. Seulement, ce n'est plus une question de place. Les voisins du 3B se plaignent depuis un mois : il y a de la graisse sur le plancher et leurs enfants marchent dedans."],
      ["JEAN-PHILIPPE","De la graisse ? Je fais pourtant mes réparations sur un grand carton."],
      ["SAMIR","Le carton glisse quand on ouvre la porte. Et depuis que vous avez ajouté le troisième vélo, la porte du local à ordures n'ouvre plus au complet."],
      ["JEAN-PHILIPPE","Ah ça, je ne l'avais pas remarqué. Vous savez, ces vélos-là, c'est mon gagne-pain : je les répare le soir et je les revends."],
      ["SAMIR","Personne ne vous demande d'arrêter. Mais avant d'occuper une partie commune, il faut me le demander : ce corridor est une sortie de secours, je dois le garder libre."],
      ["JEAN-PHILIPPE","Qu'est-ce que vous proposez, d'abord ?"],
      ["SAMIR","Il reste deux cases vides au sous-sol. Je peux vous en faire attribuer une par la propriétaire, sans frais, si vous descendez vos vélos avant vendredi."],
      ["JEAN-PHILIPPE","Et pour les taches sur le plancher ?"],
      ["SAMIR","Après avoir descendu les vélos, vous lavez le plancher avec un dégraissant. Sinon, je vais devoir le faire nettoyer par la compagnie d'entretien, et là, c'est facturé au locataire."],
      ["JEAN-PHILIPPE","Bon. Je fais ça jeudi soir en revenant de l'atelier. Merci d'être venu m'en parler au lieu d'écrire une lettre."],
    ]
  },
  t3: {
    label: "Quatre situations dans l'immeuble",
    lines: [
      ["CAMILLE","Le local à ordures est au bout du corridor du sous-sol. Depuis que le bac de recyclage est plein, les gens déposent leurs boîtes par terre, devant la porte. Il y a des restes de nourriture dans le tas et ça sent mauvais jusque dans l'escalier. Je pense que ça peut attirer de la vermine."],
      ["OKSANA","Mes voisins du dessous reçoivent des amis presque tous les vendredis. Ils mettent la musique très fort et ils rient sur le balcon jusqu'à deux heures du matin. Moi, je commence à sept heures à la pharmacie. Ça fait cinq semaines que ça dure et je ne peux plus le tolérer."],
      ["JEAN-PHILIPPE","Les visiteurs du 2C se stationnent dans les cases réservées aux locataires. La semaine passée, j'ai dû laisser mon auto dans la rue trois soirs de suite. Je demande à la propriétaire de faire installer une affiche à l'entrée du stationnement."],
      ["SAMIR","L'atelier de vélos du rez-de-chaussée utilise un produit dégraissant très fort. L'odeur monte par la cage d'escalier et entre dans les logements du premier étage. Les fenêtres du corridor ne s'ouvrent pas. C'est vraiment désagréable, surtout le samedi matin."],
    ]
  },
  t3b: {
    label: "Se plaindre ou décrire ?",
    lines: [
      ["CAMILLE","Le bac de recyclage déborde tous les mardis matin."],
      ["OKSANA","Je ne peux plus tolérer le bruit après minuit, c'est inacceptable."],
      ["JEAN-PHILIPPE","La porte d'entrée reste ouverte quand il vente très fort."],
      ["SAMIR","Cette situation est vraiment dérangeante et elle doit se terminer."],
      ["MME RIOUX","Je suis très déçue de la façon dont le corridor est laissé."],
    ]
  },
  appli: {
    label: "Dialogue — Une tache au plafond",
    lines: [
      ["MME RIOUX","Bonjour Oksana, j'ai bien reçu votre photo. Ça fait longtemps que la tache est là ?"],
      ["OKSANA","Ça fait deux semaines. Elle a doublé de grandeur depuis la pluie de dimanche."],
      ["MME RIOUX","Je vais aller la voir moi-même demain avant-midi. Est-ce que dix heures vous convient ?"],
      ["OKSANA","Oui, parfait. Je commence à treize heures, je serai là."],
      ["MME RIOUX","Est-ce qu'il y a de l'humidité ailleurs dans le logement ?"],
      ["OKSANA","Dans la salle de bain, oui. Le miroir reste embué très longtemps après la douche."],
      ["MME RIOUX","Est-ce que vous avez un ventilateur dans cette pièce-là ?"],
      ["OKSANA","Non, il n'y en a pas. J'ouvre la fenêtre, mais en hiver, c'est difficile."],
      ["MME RIOUX","Alors je vais faire installer un ventilateur en même temps que la réparation du plafond. C'est important : sans ventilation, la moisissure revient toujours."],
      ["OKSANA","Merci beaucoup. Ça m'inquiétait pour la santé de ma fille."],
    ]
  },
};
