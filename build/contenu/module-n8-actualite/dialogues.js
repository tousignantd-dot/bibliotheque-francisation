const DIALOGUES = {

  // Quatre personnages, quatre voix distinctes — aucun partage, donc aucune
  // contrainte de croisement à vérifier. MIRELA (féminine 2), RÉGINE
  // (enseignante, ralentie à 0,85), WILFRID (masculin 1), GRÉGOIRE
  // (narrateur, **non ralenti**).
  //
  // Le dépôt n'a que deux voix féminines : aucun extrait ne réunit plus de
  // deux femmes, et il n'y en a jamais eu trois dans le scénario. Compté
  // avant d'écrire.
  //
  // GRÉGOIRE porte le monologue du défi 2 — douze répliques d'affilée,
  // coupées par deux questions. C'est la forme que le programme appelle
  // « suivre le déroulement d'exposés bien structurés », et c'est exactement
  // pourquoi il ne prend pas la voix « enseignante » : douze répliques
  // ralenties d'affilée seraient interminables, et le débit rapide d'une
  // chronique de radio **est** l'objet de l'exercice.

  prep: {
    label: "Dialogue — Onze hectares, et deux façons de le dire",
    lines: [
      ["MIRELA","Madame Sauvé ? Vous avez oublié votre affiche sur le comptoir des retours."],
      ["RÉGINE","Merci. J'en ai posé quarante ce matin et j'en oublie une sur trois. Et appelez-moi Régine, on se voit toutes les semaines."],
      ["MIRELA","Alors Régine. J'ai lu le journal hier soir et je n'ai pas tout compris. Le boisé est vendu, ou pas encore ?"],
      ["RÉGINE","Pas encore. Le conseil a adopté le règlement lundi, à quatre voix contre trois. Il reste l'assemblée de consultation, puis le registre."],
      ["MIRELA","Le registre, c'est quoi exactement ? Le mot revient partout et personne ne l'explique."],
      ["RÉGINE","C'est un cahier qu'on ouvre à l'hôtel de ville pendant une journée. Les personnes habiles à voter y écrivent leur nom si elles veulent un référendum. Il en faut un certain nombre, sinon le règlement passe."],
      ["MIRELA","Et vous en êtes loin ?"],
      ["RÉGINE","Il nous faut sept cent quatre-vingt-douze signatures. On en a promis un peu plus de trois cents. C'est mince."],
      ["MIRELA","J'ai lu deux articles sur la même séance, et honnêtement, on dirait deux réunions différentes."],
      ["RÉGINE","Ah. Vous avez lu Le Courant et La Vigie."],
      ["MIRELA","Exactement. Le Courant parle d'un terrain vague, La Vigie parle d'un boisé mature. Lequel des deux ment ?"],
      ["RÉGINE","Aucun des deux, et c'est ça qui est difficile. Il y a quatre hectares d'érables de soixante ans, et il y a aussi trois hectares de remblai où plus rien ne pousse depuis l'ancienne cour de voirie. Chacun décrit sa moitié."],
      ["MIRELA","Donc les deux disent vrai, et je n'apprends rien."],
      ["RÉGINE","Vous apprenez quelque chose : vous apprenez ce que chacun trouve important. C'est déjà de l'information, à condition de lire les deux."],
      ["MIRELA","Et vous, votre comité, vous êtes contre le projet ou contre l'endroit ?"],
      ["RÉGINE","Contre l'endroit. Personne au comité n'est contre du logement abordable, ce serait indécent avec ce que coûte un quatre et demie ici. On dit qu'il y a onze hectares vacants derrière l'aréna, déjà déboisés, déjà desservis en égouts."],
      ["MIRELA","Ça, je ne l'ai lu nulle part."],
      ["RÉGINE","Parce que ce n'est pas dans le communiqué de la Ville, et que les deux journaux ont travaillé à partir du communiqué. C'est le travail d'un comité de citoyens : sortir ce qui n'est pas dans le communiqué."],
      ["MIRELA","Je vais aller à l'assemblée, alors. Est-ce qu'on a le droit de parler quand on n'est pas d'un comité ?"],
      ["RÉGINE","Tout le monde a le droit de parler, et presque personne ne le fait. Venez. Écoutez d'abord la chronique de Ferland, mercredi : il est contre nous, mais il est honnête."],
      ["MIRELA","Un journaliste contre vous, et vous me dites de l'écouter ?"],
      ["RÉGINE","Surtout lui. On ne prépare pas un argument en écoutant les gens qui pensent comme nous."],
    ]
  },

  t1: {
    label: "Reportage — Le même conseil, raconté deux fois",
    lines: [
      ["GRÉGOIRE","Ici Grégoire Ferland, il est huit heures dix, vous écoutez Le fil de la Rive. Retour ce matin sur la séance de lundi soir à l'hôtel de ville de Rivière-aux-Cèdres."],
      ["GRÉGOIRE","Le règlement numéro douze cent quatre a été adopté par quatre voix contre trois. Il autorise la cession du boisé Sainte-Perpétue à Habitations Verchères-Nord pour un dollar symbolique, en échange de quarante-cinq logements à loyer abordable sur les cent quatre-vingts prévus."],
      ["GRÉGOIRE","Nous avons demandé à deux personnes de nous raconter la même soirée. Wilfrid Chamberland, éditorialiste au Courant de la Rive, était dans la salle. Régine Sauvé y était aussi, pour le comité Le boisé, c'est à nous. Monsieur Chamberland, en une minute : qu'est-ce qui s'est passé lundi ?"],
      ["WILFRID","Il s'est passé qu'une ville de vingt-quatre mille habitants s'est donné quarante-cinq logements abordables sans dépenser un sou. Le terrain ne rapportait rien, il coûtait onze mille dollars par année en entretien, et il va maintenant produire du logement et des taxes."],
      ["GRÉGOIRE","Madame Sauvé, la même minute."],
      ["RÉGINE","Il s'est passé qu'un conseil a cédé un bien public pour un dollar, quatre jours après avoir reçu l'évaluation, et sans avoir regardé le seul autre terrain disponible. Le vote a été pris à vingt-deux heures cinquante, devant onze personnes."],
      ["GRÉGOIRE","Vous ne racontez pas la même chose, mais vous ne vous contredisez pas non plus. Monsieur Chamberland, le terrain derrière l'aréna, il existe ?"],
      ["WILFRID","Il existe, et il appartient à la Ville, c'est exact. Mais il est zoné industriel et il faudrait vingt et un mois pour le rezoner. Le promoteur, lui, a un financement qui expire en mars."],
      ["RÉGINE","Vingt et un mois, c'est le délai que la Ville avance. Elle ne l'a écrit nulle part. Et il faut le dire : c'est une estimation faite par le service de l'urbanisme, pas une règle de loi."],
      ["WILFRID","C'est une estimation, oui. Ça reste vingt et un mois pendant lesquels personne ne se loge."],
      ["GRÉGOIRE","Une question à vous deux. Est-ce que quelqu'un a compté combien d'arbres seront abattus ?"],
      ["WILFRID","Le promoteur parle de quatre-vingt-dix arbres sur les quatre hectares boisés, avec replantation à deux pour un."],
      ["RÉGINE","Le comité en a compté trois cent quarante-deux, un samedi, à six personnes. Nous avons remis nos feuilles à la Ville. Personne ne nous a répondu."],
      ["GRÉGOIRE","Quatre-vingt-dix contre trois cent quarante-deux. C'est un écart considérable et je ne peux pas le trancher ce matin. Ce que je peux dire, c'est que les deux comptes existent et que personne ne les a mis côte à côte."],
      ["WILFRID","On ne compte peut-être pas la même chose. Un arbre de quinze centimètres de diamètre, est-ce que c'est un arbre ?"],
      ["RÉGINE","Pour un érable, à quinze centimètres, c'est trente ans. Alors oui."],
      ["GRÉGOIRE","Vous voyez, chers auditeurs : le désaccord n'est pas sur le chiffre, il est sur la définition. Retenez ça, c'est souvent le cas."],
      ["GRÉGOIRE","L'assemblée publique de consultation a lieu jeudi, à dix-neuf heures, à la salle communautaire. Le registre s'ouvrira le mardi suivant. Il est huit heures dix-neuf."],
    ]
  },

  t2: {
    label: "Chronique — Ce que je pense, et pourquoi je peux me tromper",
    lines: [
      ["GRÉGOIRE","Ma chronique de la semaine. Elle sera longue, et je vous préviens tout de suite : je vais vous dire ce que je pense, ce qui n'est pas mon travail habituel."],
      ["GRÉGOIRE","Je suis pour le projet du boisé Sainte-Perpétue. Voilà. Vous savez maintenant dans quel sens lire ce qui suit, et vous avez le droit de fermer la radio."],
      ["GRÉGOIRE","Trois raisons. La première est un chiffre que personne ne conteste : le taux d'inoccupation des logements locatifs de la ville est de zéro virgule trois pour cent. Trois logements libres sur mille. À ce niveau-là, ce n'est plus un marché serré, c'est un marché fermé."],
      ["GRÉGOIRE","La deuxième raison, c'est que les quarante-cinq logements abordables sont écrits dans le règlement, avec une pénalité de deux millions si le promoteur ne les livre pas. J'ai lu le règlement. Ce n'est pas une promesse d'élection, c'est une clause."],
      ["GRÉGOIRE","La troisième raison est plus désagréable à dire. Depuis quinze ans, chaque fois qu'on a proposé du logement dense à Rivière-aux-Cèdres, un comité s'est formé, et le projet est mort. Cinq fois sur cinq. Il faut bien que ça arrive quelque part."],
      ["GRÉGOIRE","Maintenant, la partie où je me contredis, parce qu'un chroniqueur qui ne se contredit jamais est un chroniqueur qui ne lit rien."],
      ["GRÉGOIRE","Le comité Le boisé, c'est à nous a raison sur un point, et il a raison durement. La Ville a voté quatre jours après avoir reçu l'évaluation du terrain. Quatre jours. On ne vend pas un bien public en quatre jours, même pour une bonne cause, et surtout pas à vingt-deux heures cinquante devant onze personnes."],
      ["GRÉGOIRE","Il a raison sur un deuxième point : le terrain derrière l'aréna n'a jamais été étudié sérieusement. On nous répond vingt et un mois. Vingt et un mois, ce n'est pas une étude, c'est une phrase."],
      ["GRÉGOIRE","Alors voici où j'arrive, et ce n'est pas une position confortable. Je pense que le projet est bon et que la façon de l'adopter est mauvaise. Les deux à la fois."],
      ["GRÉGOIRE","Ce que je souhaite, c'est que le registre atteigne son nombre. Oui, vous avez bien entendu : je suis pour le projet et je souhaite qu'il y ait un référendum. Un projet qui passe de justesse à vingt-deux heures cinquante ne tiendra pas dix ans. Un projet approuvé par référendum, oui."],
      ["GRÉGOIRE","Bien que je sois d'accord avec la Ville sur le fond, je ne peux pas approuver qu'on tranche à la sauvette une question de cette taille."],
      ["GRÉGOIRE","Voilà. Vous pouvez appeler, la ligne est ouverte jusqu'à dix heures, et vous avez le droit de me dire que je me contredis. Je répondrai que oui, en partie, et que je préfère ça à faire semblant."],
      ["MIRELA","Bonjour, Mirela Petrescu, de la rue des Cèdres. Je voudrais comprendre une chose : vous dites que le projet est bon, mais vous voulez un référendum. Si le référendum le rejette, qu'est-ce que vous aurez gagné ?"],
      ["GRÉGOIRE","Excellente question, et je n'ai pas de bonne réponse. J'aurai perdu quarante-cinq logements et j'aurai gagné une ville où on ne décide pas à onze personnes. Je pense que ça vaut le risque. Je peux me tromper."],
      ["MIRELA","Merci. C'est la première fois que j'entends quelqu'un dire qu'il peut se tromper à la radio."],
      ["GRÉGOIRE","C'est parce que ça ne se dit pas assez. Bonne journée, madame."],
    ]
  },

  t3: {
    label: "Tribune téléphonique — La ligne est ouverte",
    lines: [
      ["GRÉGOIRE","Neuf heures cinq, la ligne est ouverte. Premier appel, madame Sauvé, du comité. Vous avez deux minutes."],
      ["RÉGINE","Merci. Je serai brève. Nous avons trois cent douze signatures promises sur les sept cent quatre-vingt-douze nécessaires, et six jours. Je ne viens pas demander à personne de signer : je viens demander à la Ville de reporter le registre de trente jours et de publier l'évaluation du terrain."],
      ["GRÉGOIRE","Pourquoi trente jours changeraient quelque chose ?"],
      ["RÉGINE","Parce que la moitié des gens que je rencontre ne savent pas ce qu'est un registre. Ce n'est pas de l'opposition, c'est de l'ignorance, et elle profite toujours au même camp."],
      ["GRÉGOIRE","Monsieur Chamberland, vous voulez répondre."],
      ["WILFRID","Je veux répondre, oui. Madame Sauvé demande trente jours et elle sait très bien que le financement du promoteur expire en mars. Trente jours, ici, ça veut dire non. Qu'on le dise franchement."],
      ["RÉGINE","Je le dis franchement : si le projet ne survit pas à trente jours de discussion publique, c'est qu'il ne tenait pas debout."],
      ["WILFRID","Ou c'est qu'un financement, ça ne se met pas en attente parce qu'une ville a besoin de réfléchir. Ce n'est pas une manœuvre, c'est un calendrier bancaire."],
      ["GRÉGOIRE","Un appel, ligne deux. Madame, vous êtes en ondes."],
      ["MIRELA","Bonjour. Mirela Petrescu, rue des Cèdres. Je suis pour le projet, et je vais quand même signer le registre."],
      ["GRÉGOIRE","Là, il faut expliquer, parce que ça a l'air contradictoire."],
      ["MIRELA","Certes le logement manque, et je le vois tous les jours : trois de mes collègues ont déménagé à Windsor faute de trouver ici. Mais je suis arrivée dans un pays où on votait sur des questions déjà réglées, et j'ai appris à me méfier de ça."],
      ["WILFRID","Madame, avec tout le respect que je vous dois, personne ici n'a rien réglé d'avance. Il y a eu un vote public."],
      ["MIRELA","Il y a eu un vote public à vingt-deux heures cinquante devant onze personnes, monsieur. Je ne dis pas qu'il est illégal, je dis qu'il est petit."],
      ["GRÉGOIRE","Qu'est-ce que vous demandez, concrètement ?"],
      ["MIRELA","Deux choses. Que l'évaluation du terrain soit publiée avant l'ouverture du registre, et que la Ville dise par écrit pourquoi le terrain de l'aréna a été écarté. Si j'avais eu ces deux documents la semaine dernière, je n'aurais peut-être pas eu besoin d'appeler ce matin."],
      ["WILFRID","Ça, je peux le soutenir. Publier une évaluation ne coûte rien à personne."],
      ["RÉGINE","Nous demandons la même chose depuis trois semaines, et c'est la première fois qu'on nous dit oui en ondes."],
      ["GRÉGOIRE","Ce que je retiens de cet appel, et je le dis pour tout le monde : madame Petrescu est pour le projet, elle va signer le registre, et elle vient de faire avancer la discussion plus que les trois d'entre nous en vingt minutes."],
      ["MIRELA","C'est parce que je n'ai rien à défendre, monsieur Ferland. C'est un avantage."],
    ]
  },

};
