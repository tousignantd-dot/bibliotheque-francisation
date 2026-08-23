const DIALOGUES = {

  // Quatre personnages, quatre voix, aucun partage — donc aucune vérification
  // de croisement à faire. Compté AVANT d'écrire une seule réplique, comme
  // CLAUDE.md le demande depuis module-n7-habitation :
  //
  //   AMIRA     → feminin_2    (femme)   présente dans les trois extraits
  //   DENIS     → narrateur    (homme)   prep seulement
  //   GHISLAIN  → masculin_1   (homme)   t1 seulement — porte le long exposé
  //   VERONIQUE → enseignante  (femme)   t2 seulement
  //
  // Deux femmes en tout, et jamais trois dans un même extrait : t2 réunit
  // AMIRA et VERONIQUE, soit exactement la limite du dépôt.
  //
  // Le long exposé du défi 1 est confié à GHISLAIN, c'est-à-dire à
  // `masculin_1`, et non à `enseignante` : `voix_lente.py` ralentit cette
  // dernière à 0,85, et quatorze répliques d'affilée ralenties seraient
  // interminables. C'est la consigne tirée du journal de l'activité 119.

  prep: {
    label: "Dialogue — Le camion est reparti à onze heures",
    lines: [
      ["AMIRA","Monsieur Ducharme ? Amira Benkirane. Vos hommes ont déménagé mon logement ce matin, rue Sainte-Ursule."],
      ["DENIS","Oui, madame Benkirane, je me souviens. Le deuxième étage avec l'escalier en colimaçon. Il y a un problème ?"],
      ["AMIRA","Il y en a trois. Je préfère vous les dire au téléphone avant de vous écrire quoi que ce soit."],
      ["DENIS","Allez-y, je vous écoute."],
      ["AMIRA","D'abord la rampe de l'escalier. Le coin de la remorque l'a accrochée en reculant, vers neuf heures et quart. Elle est tordue sur un mètre."],
      ["DENIS","Elle était déjà croche, cette rampe-là. C'est un triplex des années trente."],
      ["AMIRA","Elle était droite hier. J'ai des photos datées de la veille de la prise de possession, et j'en ai d'autres de ce matin."],
      ["DENIS","Bon. Ensuite ?"],
      ["AMIRA","Deux boîtes sont restées sur le balcon pendant l'averse de dix heures. Le carton s'est ouvert par le fond. Il y avait des livres et des albums de photos."],
      ["DENIS","On a demandé où les mettre. Il n'y avait personne en haut à ce moment-là."],
      ["AMIRA","J'étais dans le stationnement avec votre chauffeur. Ça, je vous l'accorde : personne ne surveillait le balcon, et j'aurais dû y penser."],
      ["DENIS","Voilà. Et le troisième ?"],
      ["AMIRA","Le vaisselier. Il est arrivé fendu sur tout le panneau de côté. Il appartenait à ma mère et il a traversé l'océan en 2019 sans une égratignure."],
      ["DENIS","Madame, un meuble ancien, ça travaille. On ne peut pas garantir un panneau collé il y a soixante ans."],
      ["AMIRA","Il n'était pas fendu quand il est entré dans votre camion. Vos hommes ont signé l'inventaire à huit heures, et rien n'y est noté."],
      ["DENIS","L'inventaire, c'est une formalité. Regardez le contrat que vous avez signé : notre responsabilité est limitée à soixante cents par livre par article. Pour un vaisselier de deux cents livres, ça fait cent vingt dollars."],
      ["AMIRA","Cent vingt dollars. Vous me dites que le meuble de ma mère vaut cent vingt dollars ?"],
      ["DENIS","Je vous dis ce que le contrat dit. Si vous vouliez plus, il fallait faire une déclaration de valeur avant le déménagement. On l'offre, c'est écrit sur le connaissement."],
      ["AMIRA","Personne ne me l'a offerte. Et je n'ai signé le connaissement qu'à la fin, dans le camion, sans le lire."],
      ["DENIS","Ça, madame, c'est votre affaire. Écoutez, faites une réclamation à votre assurance habitation. C'est à ça que ça sert."],
      ["AMIRA","Je vais faire les deux. Je vous envoie une lettre cette semaine avec les photos et l'inventaire signé."],
      ["DENIS","Faites donc ça. Bonne fin de journée."],
      ["AMIRA","Bonne fin de journée, monsieur Ducharme."],
    ]
  },

  t1: {
    label: "Dialogue — Ce que ma police couvre vraiment",
    lines: [
      ["AMIRA","Monsieur Marcotte ? Amira Benkirane. J'ai souscrit une assurance habitation chez vous il y a onze jours, avant d'emménager."],
      ["GHISLAIN","Bonjour madame Benkirane. Oui, j'ai votre dossier devant moi. Rue Sainte-Ursule, cinq et demie, prise d'effet le premier du mois. Qu'est-ce qui se passe ?"],
      ["AMIRA","J'ai eu des dommages le jour du déménagement. Avant de réclamer quoi que ce soit, j'aimerais comprendre ce que j'ai acheté. Je vous avoue que j'ai signé sans tout saisir."],
      ["GHISLAIN","C'est la meilleure question que vous puissiez me poser, et la plupart des gens la posent après le sinistre. Vous avez une police locataire de base, avec deux avenants."],
      ["AMIRA","Commençons par le début. Qu'est-ce qu'une police de base couvre ?"],
      ["GHISLAIN","Trois choses qui n'ont rien à voir entre elles, et c'est ce qui embrouille tout le monde. Un : vos biens. Deux : votre responsabilité civile. Trois : vos frais de subsistance supplémentaires si le logement devient inhabitable."],
      ["AMIRA","La responsabilité civile, c'est quand c'est moi qui cause le dommage ?"],
      ["GHISLAIN","Exactement. Si votre lave-vaisselle déborde et que le plafond du voisin d'en dessous tombe, c'est cette partie-là qui paie. Vous êtes couverte jusqu'à deux millions."],
      ["AMIRA","Et mes biens à moi ?"],
      ["GHISLAIN","Cinquante mille dollars, valeur à neuf, avec une franchise de cinq cents dollars par sinistre."],
      ["AMIRA","Attendez. « Valeur à neuf », « franchise » — pouvez-vous me redire ça autrement ? Je veux être certaine de bien vous suivre."],
      ["GHISLAIN","Bien sûr. La franchise, c'est la part qui reste toujours à votre charge. Si le dommage est de mille deux cents dollars, on vous verse sept cents. Si le dommage est de quatre cents dollars, on ne vous verse rien du tout : réclamer ne servirait à rien."],
      ["AMIRA","Et la valeur à neuf ?"],
      ["GHISLAIN","Deux façons d'indemniser existent. La valeur au jour du sinistre tient compte de la dépréciation : un téléviseur de huit ans vous est remboursé au prix d'un téléviseur de huit ans, c'est-à-dire presque rien. La valeur à neuf vous rembourse le prix d'un neuf équivalent. Vous avez la seconde, et c'est ce qui explique votre prime."],
      ["AMIRA","D'accord. Et mes deux avenants, ce sont lesquels ?"],
      ["GHISLAIN","Un avenant pour le refoulement d'égout, et un pour les bijoux au-delà du plafond du contrat de base. Un avenant, c'est une protection que le contrat de base n'offre pas et qu'on ajoute par écrit."],
      ["AMIRA","Il y a des choses que ça ne couvre jamais ?"],
      ["GHISLAIN","Il y en a, et c'est la partie du contrat qu'il faut lire en premier. Je vous explique comment fonctionne une réclamation, du premier appel jusqu'à la décision, parce que c'est là que vous êtes maintenant."],
      ["GHISLAIN","D'abord, vous appelez pour déclarer le sinistre. Pas pour réclamer : pour déclarer. Ce sont deux choses différentes, et la première n'engage à rien."],
      ["GHISLAIN","Vous donnez la date, l'heure, l'endroit et ce qui s'est passé, dans l'ordre. On vous attribue un numéro de dossier. Notez-le : tout ce qui suivra passera par ce numéro-là."],
      ["GHISLAIN","Ensuite, on vous demande un inventaire. C'est la pièce qui décide de tout. Chaque bien endommagé, avec sa description, son âge approximatif, son prix d'achat, et une preuve si vous en avez une."],
      ["GHISLAIN","Une preuve, ce n'est pas forcément une facture. Une photo datée, un relevé de carte, un courriel de confirmation, un témoignage écrit : tout cela se plaide."],
      ["GHISLAIN","Après, un expert en sinistre est assigné à votre dossier. Ce n'est pas votre adversaire, et ce n'est pas votre allié non plus : c'est la personne qui établit les faits pour l'assureur."],
      ["GHISLAIN","Il ou elle va vous rappeler, peut-être se déplacer, examiner les biens, comparer votre inventaire au contrat, et rendre une décision par écrit."],
      ["GHISLAIN","La décision comporte presque toujours trois parties : ce qui est accepté, ce qui est refusé, et le motif du refus avec la clause qui l'appuie. Exigez toujours la clause. Un refus sans clause n'est pas un refus, c'est une opinion."],
      ["AMIRA","Et si je ne suis pas d'accord avec la décision ?"],
      ["GHISLAIN","Vous demandez une révision, par écrit, en visant le numéro de dossier. Vous distinguez ce que vous acceptez de ce que vous contestez — jamais tout en bloc, ça se lit comme du refus de principe."],
      ["GHISLAIN","Vous appuyez chaque point contesté sur une pièce datée, et vous proposez quelque chose de chiffré. Une contestation sans proposition reste sur un bureau ; une contestation avec un chiffre se traite."],
      ["GHISLAIN","Si la révision ne donne rien, il reste l'ombudsman de l'assureur, puis l'Autorité des marchés financiers, qui reçoit les plaintes des consommateurs de produits financiers. Et les tribunaux, bien sûr, mais on n'en est jamais là."],
      ["GHISLAIN","Une dernière chose, et c'est la plus importante dans votre cas : quand le dommage a été causé par quelqu'un d'autre, l'assureur peut vous indemniser puis se retourner contre cette personne. Ça s'appelle la subrogation."],
      ["AMIRA","Donc si c'est le déménageur qui a fendu le meuble, je réclame quand même chez vous ?"],
      ["GHISLAIN","Vous réclamez chez nous, et vous mettez le déménageur en demeure en parallèle. Les deux démarches ne se nuisent pas. Ce qu'il faut éviter, c'est de vous entendre avec lui sur un montant avant que nous ayons vu le dossier."],
      ["AMIRA","Je résume, pour être certaine : je déclare le sinistre, je monte un inventaire avec des preuves datées, j'attends l'expert, j'exige la clause pour tout refus, et je n'accepte aucune entente avec le déménageur d'ici là."],
      ["GHISLAIN","C'est exactement ça. Appelez la ligne des sinistres ce matin, pas cet après-midi : plus la déclaration est proche des faits, moins elle se discute."],
      ["AMIRA","Merci, monsieur Marcotte. Je comprends enfin ce que j'ai signé."],
      ["GHISLAIN","C'est mon métier, madame. Rappelez-moi quand vous aurez le nom de votre expert."],
    ]
  },

  t2: {
    label: "Dialogue — Ce qui est accepté, ce qui est refusé",
    lines: [
      ["VERONIQUE","Madame Benkirane ? Véronique Chartier, experte en sinistre. Je vous appelle au sujet du dossier 8-4-1-7-2-6."],
      ["AMIRA","Bonjour madame Chartier. J'attendais votre appel. J'ai la lettre devant moi, je l'ai reçue hier."],
      ["VERONIQUE","Vous l'avez lue, alors. Je voulais vous l'expliquer de vive voix, parce qu'une lettre de décision se lit mal."],
      ["AMIRA","Je vous écoute, et j'aimerais qu'on prenne les trois points l'un après l'autre. J'ai l'inventaire sous les yeux."],
      ["VERONIQUE","Volontiers. Premier point : les livres et les albums de photos abîmés par la pluie. Accepté. Nous retenons neuf cent quarante dollars, moins votre franchise de cinq cents."],
      ["AMIRA","Donc quatre cent quarante dollars versés. C'est ce que j'avais compris. Et je ne conteste pas ce montant : les livres se remplacent, les photos, non, mais ça n'a pas de prix de marché."],
      ["VERONIQUE","Deuxième point : la rampe de l'escalier extérieur. Refusé, et je vais vous dire pourquoi."],
      ["AMIRA","Sur quelle clause vous appuyez-vous, exactement ?"],
      ["VERONIQUE","La rampe fait partie du bâtiment. Votre police est une police de locataire : elle couvre vos biens, pas l'immeuble. C'est l'assurance de votre propriétaire qui s'applique, ou la responsabilité du transporteur."],
      ["AMIRA","Celle-là, je l'accepte. Elle est logique et la clause est claire. Je transmettrai à mon propriétaire."],
      ["VERONIQUE","Troisième point : le vaisselier. Refusé également. Le motif est la clause d'exclusion des dommages survenus au cours d'un déménagement effectué par un tiers rémunéré."],
      ["AMIRA","Attendez. Est-ce que vous pouvez me relire cette clause-là ? Je veux les mots exacts."],
      ["VERONIQUE","« Sont exclus les dommages causés aux biens meubles pendant leur transport par un déménageur professionnel, la responsabilité de ce dernier étant régie par le contrat de transport. »"],
      ["AMIRA","Bon. Certes la clause existe, et je ne prétends pas qu'elle n'existe pas. Mais elle parle du transport, et le vaisselier n'a pas été fendu pendant le transport."],
      ["VERONIQUE","Qu'est-ce qui vous fait dire ça ?"],
      ["AMIRA","L'inventaire signé par le chauffeur à huit heures ne note aucun dommage. La photo prise à onze heures vingt-deux, dans mon salon, montre la fente. Entre les deux, il y a le portage dans un escalier en colimaçon, pas le transport."],
      ["VERONIQUE","Le portage fait partie du service de déménagement."],
      ["AMIRA","Il fait partie du service, je vous l'accorde. Mais votre clause ne dit pas « pendant le service » : elle dit « pendant leur transport ». Ce sont deux choses différentes, et c'est votre texte qui les distingue, pas moi."],
      ["VERONIQUE","C'est un argument. Je ne dis pas qu'il est gagnant, je dis que c'en est un."],
      ["AMIRA","Il y en a un second. Si le vaisselier avait été déclaré à sa valeur, nous discuterions du montant, pas du principe. Or personne ne m'a offert de déclaration de valeur, bien que le connaissement mentionne qu'elle est offerte."],
      ["VERONIQUE","Ça, madame, ça regarde le déménageur et non nous."],
      ["AMIRA","Justement. Monsieur Marcotte m'a parlé de la subrogation : si vous m'indemnisez, vous pouvez vous retourner contre Déménagement Ducharme. Ce que je vous propose, c'est cela plutôt qu'un refus sec."],
      ["VERONIQUE","Vous demandez donc quoi, précisément ?"],
      ["AMIRA","Ce que je conteste, c'est le refus complet, pas votre évaluation. Je demande la révision du troisième point seulement. Et je propose un compromis : la moitié de la valeur estimée, soit huit cent cinquante dollars, contre ma renonciation à toute autre réclamation dans ce dossier."],
      ["VERONIQUE","Huit cent cinquante. Sur quoi repose l'estimation ?"],
      ["AMIRA","Sur trois annonces de meubles comparables, datées de la semaine dernière, et sur l'évaluation écrite d'un ébéniste de la rue Bonaventure qui a examiné la fente lundi. Je vous envoie les quatre pièces aujourd'hui."],
      ["VERONIQUE","Envoyez-les. Je vous le dis franchement : si vous m'aviez appelée en criant, je vous aurais lu la clause et j'aurais raccroché. Là, je vais soumettre le dossier au réviseur."],
      ["AMIRA","J'aimerais que la décision me soit communiquée par écrit, avec le motif et la clause, comme la première fois."],
      ["VERONIQUE","Elle le sera. Comptez dix jours ouvrables. Et gardez votre numéro de dossier dans l'objet de tous vos courriels."],
      ["AMIRA","Entendu. Une dernière question : ma démarche auprès du déménageur nuit-elle à la révision ?"],
      ["VERONIQUE","Non, tant que vous n'acceptez aucun règlement de sa part avant notre décision. Si vous encaissez un chèque de sa part, le dossier se ferme tout seul."],
      ["AMIRA","Je ne l'encaisserai pas. Merci d'avoir pris le temps de m'expliquer, madame Chartier."],
      ["VERONIQUE","C'est normal. Bonne fin de journée, madame Benkirane."],
    ]
  },

};
