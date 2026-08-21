const DIALOGUES = {

  // ── Je découvre — la brochure de la Ville sur la table de cuisine ────────
  prep: {
    label: "Dialogue — Le papier qui vient de la Ville",
    lines: [
      ["LEÏLA","Pierre-Luc, tu as reçu ça, toi ? C'est arrivé dans ma boîte aux lettres hier."],
      ["PIERRE-LUC","Fais voir… Oui, c'est la brochure de la Ville. Ils l'envoient à tout le monde deux fois par année."],
      ["LEÏLA","Il y a trois bacs dessus. Trois. Chez moi, dans l'entrée, il y en a deux."],
      ["PIERRE-LUC","Le gris, c'est les ordures. Le vert, c'est le recyclage. Et le brun, c'est les restes de table."],
      ["LEÏLA","Les restes de table dans un bac ? Pour quoi faire ?"],
      ["PIERRE-LUC","Ça devient du compost. C'est ramassé une fois par semaine, mais pas le même jour que le reste."],
      ["LEÏLA","Et je le sais comment, le jour ?"],
      ["PIERRE-LUC","Tu entres ton code postal sur le site de la Ville, et il te sort ton horaire. Ça s'appelle Info-collectes."],
      ["LEÏLA","D'accord. Et ça, en bas de la page, « écocentre » ? Le mot ne me dit rien."],
      ["PIERRE-LUC","C'est un endroit où tu apportes ce qui n'entre dans aucun bac. Un vieux micro-ondes, de la peinture, des branches."],
      ["LEÏLA","C'est payant ?"],
      ["PIERRE-LUC","Pas pour les résidents, dans la plupart des cas. Mais il faut que tu apportes une preuve que tu habites la ville."],
      ["LEÏLA","Une preuve… comme quoi ?"],
      ["PIERRE-LUC","Un permis de conduire, une facture à ton nom, un bail. Quelque chose avec ton adresse dessus."],
      ["LEÏLA","Bon. Alors je garde le papier. Je pensais que c'était de la publicité, je l'avais mis avec les circulaires."],
      ["PIERRE-LUC","Beaucoup de monde fait ça. Puis après, on se demande pourquoi le bac reste plein."],
    ]
  },

  // ── Défi 1 — l'appel au 311 ─────────────────────────────────────────────
  t1: {
    label: "Dialogue — L'appel au 311",
    lines: [
      ["VOIX","Vous avez joint le service à la clientèle de la Ville. Pour le français, faites le un."],
      ["VOIX","Pour un problème de collecte, faites le trois. Pour parler à un préposé, restez en ligne. Le temps d'attente est d'environ quatre minutes."],
      ["MICHELINE","Bonjour, Micheline à l'appareil. Comment puis-je vous aider ?"],
      ["LEÏLA","Bonjour. Je vous appelle parce que mon bac brun n'a pas été ramassé depuis deux semaines."],
      ["MICHELINE","Deux semaines, d'accord. Vous êtes à quelle adresse ?"],
      ["LEÏLA","Au 7412, rue De Normanville, appartement 3. À Villeray."],
      ["MICHELINE","Et votre code postal, s'il vous plaît ?"],
      ["LEÏLA","H2R 2V8. Je peux vous l'épeler : H, deux, R, deux, V, huit."],
      ["MICHELINE","C'est bien noté. Alors, dans votre secteur, la collecte des résidus alimentaires se fait le mardi matin."],
      ["LEÏLA","Le mardi. Est-ce que vous pouvez me dire à quelle heure il faut que je sorte le bac ?"],
      ["MICHELINE","La veille au soir après vingt heures, ou avant sept heures le matin même."],
      ["LEÏLA","Ah. Moi, je le sortais le mardi vers midi, en revenant de mon cours."],
      ["MICHELINE","C'est ce qui explique tout, madame. Le camion était déjà passé."],
      ["LEÏLA","Je voudrais savoir si le bac va être vidé cette semaine quand même."],
      ["MICHELINE","J'ouvre une requête pour un ramassage supplémentaire. Le délai est de trois jours ouvrables."],
      ["LEÏLA","Trois jours ouvrables. Et comment est-ce que je fais pour suivre ma demande ?"],
      ["MICHELINE","Je vous donne un numéro de requête. Vous notez ? 24-118-7690."],
      ["LEÏLA","Vingt-quatre, cent dix-huit, sept mille six cent quatre-vingt-dix. C'est bien ça ?"],
      ["MICHELINE","C'est exact. Gardez-le : si personne ne passe d'ici vendredi, vous nous rappelez avec ce numéro-là."],
      ["LEÏLA","Parfait. Merci beaucoup, madame. Bonne journée."],
    ]
  },

  // ── Défi 2 — devant l'écran ─────────────────────────────────────────────
  t2: {
    label: "Dialogue — Devant l'écran, avec la page de l'écocentre",
    lines: [
      ["LEÏLA","Pierre-Luc, viens voir. J'ai trouvé la page dont tu m'avais parlé, mais je ne comprends pas la moitié."],
      ["PIERRE-LUC","Montre. Ah oui, c'est la page de l'écocentre. Elle est longue, mais elle est bien faite."],
      ["LEÏLA","Il y a deux colonnes. « Matières acceptées » et « Matières refusées ». Ça, ça va."],
      ["PIERRE-LUC","Lis la deuxième. C'est celle qui cause des problèmes : les gens chargent leur auto et ils repartent avec."],
      ["LEÏLA","« Matières refusées : les matières dangereuses non identifiées, les pneus de camion, les déchets qui viennent d'un chantier commercial. »"],
      ["PIERRE-LUC","Ta peinture, elle est encore dans son pot d'origine ?"],
      ["LEÏLA","Oui, avec l'étiquette."],
      ["PIERRE-LUC","Alors elle passe. C'est ce que veut dire « non identifiées » : un bidon sans étiquette, ils ne le prennent pas."],
      ["LEÏLA","D'accord. Et là, le petit encadré gris, en haut à droite ?"],
      ["PIERRE-LUC","« Avant de vous déplacer. » C'est toujours l'encadré le plus important d'une page comme celle-là."],
      ["LEÏLA","« Vérifiez le temps d'attente en direct. Apportez une preuve de résidence. Le nombre de visites gratuites est limité par année. »"],
      ["PIERRE-LUC","Trois phrases, et elles t'évitent trois voyages pour rien."],
      ["LEÏLA","Il y a un mot que je ne connais pas : « en vigueur ». « Tarifs en vigueur au 1er avril »."],
      ["PIERRE-LUC","Ça veut dire : les prix qui s'appliquent aujourd'hui. Une loi, un tarif, un horaire : ce qui est en vigueur, c'est ce qui compte maintenant."],
      ["LEÏLA","Donc si la page dit « en vigueur au 1er avril », les prix d'avant ne comptent plus."],
      ["PIERRE-LUC","Voilà. Tu viens d'apprendre le mot le plus utile de toute la page."],
    ]
  },

  // ── Défi 3 — au guichet ─────────────────────────────────────────────────
  t3: {
    label: "Dialogue — Au guichet, billet B-47",
    lines: [
      ["VOIX","Numéro B quarante-sept, au comptoir trois."],
      ["GAÉTAN","Bonjour ! Vous pouvez vous asseoir. Qu'est-ce qui vous amène ?"],
      ["LEÏLA","Bonjour. Je viens pour ma carte de citoyenne. J'ai commencé la demande en ligne, mais elle n'a pas fonctionné."],
      ["GAÉTAN","Elle n'a pas fonctionné comment ? Elle a été refusée, ou elle est restée bloquée ?"],
      ["LEÏLA","Elle est restée bloquée à la dernière page. J'avais rempli tout le formulaire et il me redemandait mon adresse."],
      ["GAÉTAN","Ah, ça arrive quand l'adresse est écrite autrement que dans notre système. Vous aviez mis « appartement » au long ?"],
      ["LEÏLA","Oui, j'avais écrit « appartement 3 »."],
      ["GAÉTAN","C'est ça. Le système veut « app. 3 ». Ce n'est pas votre faute, c'est une vraie faiblesse du formulaire."],
      ["LEÏLA","Bon. Alors je peux la faire ici ?"],
      ["GAÉTAN","Tout à fait. Il faut que vous me montriez deux pièces : une avec votre photo, et une avec votre adresse."],
      ["LEÏLA","J'ai mon permis de conduire, et j'ai apporté mon bail."],
      ["GAÉTAN","Le permis, parfait. Le bail… voyons voir. Il est à quel nom ?"],
      ["LEÏLA","Au mien et à celui de mon fils."],
      ["GAÉTAN","Alors il fait la job. Ce qui manque parfois, c'est une facture trop vieille — il faut qu'elle date de moins de trois mois."],
      ["LEÏLA","Je note. Combien de temps ça prend, après ?"],
      ["GAÉTAN","La carte est imprimée pendant que vous attendez. Vous repartez avec dans dix minutes."],
      ["LEÏLA","Dix minutes ! J'ai passé trois soirées sur le site Web."],
      ["GAÉTAN","Vous n'êtes pas la première à me dire ça. La prochaine fois, appelez-nous avant : on vous dit tout de suite si ça se règle en ligne ou non."],
    ]
  },

};
