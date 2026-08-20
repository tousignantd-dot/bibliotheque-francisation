const DIALOGUES = {
  prep: {
    label: "Dialogue — Excusez-moi, je cherche la rue Sainte-Hélène",
    lines: [
      ["NOUR","Excusez-moi, madame. Je cherche la rue Sainte-Hélène. C'est loin d'ici ?"],
      ["MARIE-JOSÉE","Sainte-Hélène… Non, c'est à dix minutes à pied. Vous êtes à pied ou en autobus ?"],
      ["NOUR","À pied. Je suis descendue de l'autobus au coin, là-bas."],
      ["MARIE-JOSÉE","D'accord. Continuez tout droit jusqu'au feu, puis tournez à gauche sur Chambly."],
      ["NOUR","Jusqu'au feu, puis à gauche. Et après ?"],
      ["MARIE-JOSÉE","Après, marchez deux coins de rue. Vous allez passer devant une pharmacie et une caisse."],
      ["NOUR","Une pharmacie et une caisse. D'accord."],
      ["MARIE-JOSÉE","Sainte-Hélène est la rue juste après la caisse. Ne la manquez pas, elle est petite."],
      ["NOUR","Et le numéro 340, il est de quel côté ?"],
      ["MARIE-JOSÉE","Les numéros pairs sont du côté droit. Le 340 devrait être à votre droite."],
      ["NOUR","Merci beaucoup. Alors : tout droit jusqu'au feu, à gauche, deux coins de rue, après la caisse."],
      ["MARIE-JOSÉE","C'est exactement ça. Vous avez bien écouté."],
    ]
  },

  t1: {
    label: "Dialogue — Quelle ligne, quelle direction ?",
    lines: [
      ["NOUR","Bonjour. Je dois aller à l'hôpital Charles-Le Moyne. Est-ce que je peux y aller en métro ?"],
      ["GILLES","En métro puis en autobus. Prenez la ligne jaune jusqu'à Longueuil, c'est le terminus."],
      ["NOUR","La ligne jaune. Et je monte de quel côté ?"],
      ["GILLES","Du côté « direction Longueuil ». Faites attention : l'autre quai va vers Berri, dans le sens contraire."],
      ["NOUR","Comment je sais que c'est le bon quai ?"],
      ["GILLES","Regardez le panneau au-dessus de l'escalier. Le nom du terminus est toujours écrit dessus."],
      ["NOUR","D'accord. Et après Longueuil ?"],
      ["GILLES","Sortez du métro, montez au terminus d'autobus. Prenez celui qui va vers Gaétan-Boucher."],
      ["NOUR","Celui qui va vers Gaétan-Boucher. Il passe souvent ?"],
      ["GILLES","Aux quinze minutes. Descendez au troisième arrêt, l'hôpital est juste en face."],
      ["NOUR","Ça prend combien de temps en tout ?"],
      ["GILLES","Comptez quarante minutes, une heure si vous manquez l'autobus. Partez d'avance."],
    ]
  },

  t2: {
    label: "Dialogue — À ton tour d'expliquer",
    lines: [
      ["PATRICE","Nour, tu connais le chemin pour aller au centre d'emploi ? Je dois y aller demain matin."],
      ["NOUR","Oui, j'y suis allée la semaine passée. Tu pars d'ici, du centre de formation ?"],
      ["PATRICE","Oui, à huit heures."],
      ["NOUR","Alors sors par la porte principale et tourne à droite. Marche jusqu'au parc."],
      ["PATRICE","Le parc avec les jeux d'enfants ?"],
      ["NOUR","Celui-là, oui. Traverse le parc, il y a un sentier au milieu. Tu arrives sur la rue Victoria."],
      ["PATRICE","Et là, à droite ou à gauche ?"],
      ["NOUR","À gauche. L'édifice est le troisième, celui qui a une grande porte vitrée."],
      ["PATRICE","Il y a une enseigne ?"],
      ["NOUR","Une petite, au-dessus de la porte. Ne cherche pas une grande affiche, il n'y en a pas."],
      ["PATRICE","Ça me prend combien de temps ?"],
      ["NOUR","Douze minutes à pied. Mais s'il pleut, ne traverse pas le parc : le sentier devient de la boue."],
    ]
  },

  t2b: {
    label: "Dialogue — Je me suis trompée de direction",
    lines: [
      ["NOUR","Je me suis trompée hier. J'ai pris l'autobus dans le mauvais sens."],
      ["PATRICE","Comment tu t'en es aperçue ?"],
      ["NOUR","Les noms des rues montaient au lieu de descendre. Au bout de dix minutes, j'ai compris."],
      ["PATRICE","Tu as fait quoi ?"],
      ["NOUR","Je suis descendue au premier arrêt et j'ai traversé la rue. L'arrêt d'en face allait dans l'autre sens."],
      ["PATRICE","C'est le bon réflexe. Le même numéro d'autobus, mais de l'autre côté de la rue."],
      ["NOUR","J'ai perdu vingt minutes, mais je suis arrivée."],
      ["PATRICE","La prochaine fois, demande au chauffeur avant de monter. Ils répondent toujours."],
    ]
  },

  t3: {
    label: "Annonces — Ce qu'on entend dans le transport",
    lines: [
      ["VOIX","Prochain arrêt : boulevard Curé-Poirier. Correspondance avec la ligne 8."],
      ["VOIX","En raison de travaux, l'autobus 45 ne dessert pas l'arrêt Sainte-Foy aujourd'hui."],
      ["VOIX","Attention à l'espace entre le quai et la voiture. Laissez descendre avant de monter."],
      ["VOIX","Le service est interrompu entre Longueuil et Berri. Un service d'autobus est offert à la sortie."],
      ["VOIX","Terminus. Tous les passagers doivent descendre. Merci d'avoir voyagé avec nous."],
      ["VOIX","Dernier appel pour l'autobus 90, quai 12, à destination de Saint-Hubert."],
    ]
  },

  t3b: {
    label: "Dialogue — Lire un plan et un horaire",
    lines: [
      ["PATRICE","Je n'arrive pas à lire cet horaire. Il y a deux colonnes de chiffres."],
      ["NOUR","La première colonne, c'est la semaine. La deuxième, c'est la fin de semaine."],
      ["PATRICE","Et les lettres à côté des heures ?"],
      ["NOUR","Un petit « a », ça veut dire que l'autobus ne va pas jusqu'au terminus. Il s'arrête avant."],
      ["PATRICE","Alors celui de 7 h 42 ne me sert à rien."],
      ["NOUR","Non. Prends celui de 7 h 51, il fait tout le trajet."],
      ["PATRICE","Et sur le plan, les lignes de couleur, c'est quoi ?"],
      ["NOUR","Chaque couleur est une ligne. Les cercles blancs sont les arrêts, les cercles noirs les correspondances."],
      ["PATRICE","Donc je change de ligne seulement aux cercles noirs."],
      ["NOUR","C'est ça. Et regarde toujours le nom du terminus : c'est lui qui donne la direction."],
    ]
  },

  appli: {
    label: "Dialogue — Perdue au terminus",
    lines: [
      ["NOUR","Excusez-moi, je cherche le quai 12. Je tourne en rond depuis dix minutes."],
      ["GILLES","Vous êtes au bon étage, mais du mauvais côté. Les quais 1 à 10 sont ici, les autres sont derrière."],
      ["NOUR","Derrière ? Je passe par où ?"],
      ["GILLES","Passez par le corridor vitré, à votre gauche, et descendez l'escalier au bout."],
      ["NOUR","Par le corridor vitré, puis l'escalier. Et le quai 12 est en bas ?"],
      ["GILLES","En bas, à droite. Vous allez voir les numéros au-dessus de chaque porte."],
      ["NOUR","Mon autobus part à 9 h 05. J'ai le temps ?"],
      ["GILLES","Largement. Comptez trois minutes. Mais ne courez pas, le plancher est mouillé."],
      ["NOUR","Merci. Corridor vitré, escalier, en bas à droite."],
      ["GILLES","C'est ça. Bon voyage."],
    ]
  },
};
