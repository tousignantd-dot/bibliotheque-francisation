const DIALOGUES = {
  // Niveau 6 — « des discours détaillés et structurés ». Quatre extraits, un
  // seul dossier : Farida Belkacem part six mois travailler à Sept-Îles et
  // veut sous-louer son quatre et demie de la rue de la Canardière, à
  // Limoilou, au lieu de le perdre.
  //
  // Le fil est le même dans les quatre, mais le genre et le rapport entre les
  // interlocuteurs changent à chaque fois : la conversation entre collègues à
  // la cuisine, l'appel au service de renseignements du Tribunal, la remise
  // d'un avis écrit au locateur sur le palier, la visite du logement avec la
  // personne proposée. L'élève doit reconnaître la même démarche sous les
  // quatre.
  //
  // Farida tutoie Gilles, son collègue depuis trois ans. Elle vouvoie Mylène
  // Poitras, Lucien Tardif et Nicolas Trudel. Le contraste est voulu :
  // « saisir les rapports entre des interlocuteurs » est un savoir du cours,
  // et il n'apparaît qu'au niveau 6.
  //
  // Le dialogue `t2b` n'a pas de section à lui : il est porté par l'exercice
  // `t2si`, qui est un `write` — le gabarit n'affiche un dialogue sur un
  // exercice que pour ce type-là.

  prep: {
    label: "Dialogue — Six mois à Sept-Îles",
    lines: [
      ["FARIDA","Gilles, je peux te déranger deux minutes ? J'ai reçu une nouvelle hier soir et je ne sais pas quoi en penser."],
      ["GILLES","Vas-y. Le temps que le four préchauffe, on a tout notre temps."],
      ["FARIDA","On m'offre un remplacement de six mois à Sept-Îles, à la cuisine du centre d'hébergement. Du six janvier au trente juin. Après, je reviens ici."],
      ["GILLES","Six mois, ce n'est pas rien. C'est payé combien de plus ?"],
      ["FARIDA","Trois dollars de l'heure de plus, et le logement du personnel est fourni là-bas. C'est justement ça, mon problème : le logement."],
      ["GILLES","Tu as ton quatre et demie sur la Canardière, si je me souviens bien."],
      ["FARIDA","Depuis trois ans. Huit cent quatre-vingt-quinze piastres par mois, chauffé, deux minutes de l'autobus. Tu sais ce que ça coûterait de retrouver ça en juillet ?"],
      ["GILLES","Je le sais trop bien. Ma fille cherche depuis le mois de mars et elle n'a rien trouvé sous mille deux cents."],
      ["FARIDA","Alors je ne veux pas le lâcher. Mais je ne vais pas payer huit cent quatre-vingt-quinze dollars pendant six mois pour un logement vide."],
      ["GILLES","Non, ça n'a pas de bon sens. Mon cousin avait fait la même chose il y a deux ans : il était parti travailler à Baie-Comeau et il avait sous-loué son appartement à un étudiant."],
      ["FARIDA","Sous-loué. C'est ça, le mot ? Parce que j'ai entendu quelqu'un parler de céder son bail aussi, et je ne vois pas la différence."],
      ["GILLES","La différence, c'est ce qui arrive après. Quand tu cèdes ton bail, tu t'en vas pour de bon : le bail continue avec l'autre personne, et toi tu es sorti du dossier."],
      ["FARIDA","Et quand je sous-loue ?"],
      ["GILLES","Tu prêtes ton logement pour un temps, mais le bail reste à ton nom. Si l'autre ne paie pas, c'est toi que le propriétaire va voir. Mon cousin s'était fait prendre là-dessus."],
      ["FARIDA","Donc je reste responsable. Ça, il faut que je le sache avant de choisir quelqu'un."],
      ["GILLES","En plein ça. Et il y a une démarche à suivre, avec des papiers. Tu ne peux pas juste donner tes clés à quelqu'un et t'en aller."],
      ["FARIDA","Monsieur Tardif ne serait pas content, c'est certain. Il a soixante-trois ans, il tient son immeuble comme son jardin, et il n'aime pas les surprises."],
      ["GILLES","Justement, ne va pas le voir les mains vides. Regarde d'abord sur le site du Tribunal administratif du logement : tout y est écrit, gratuitement, et ce n'est pas ton propriétaire qui l'a rédigé."],
      ["FARIDA","Le Tribunal administratif du logement. Tu me l'écris sur un papier ? Je vais lire ça ce soir, avant de dire quoi que ce soit à qui que ce soit."],
      ["GILLES","Tiens. Et lis-le au complet, pas juste le premier paragraphe. C'est toujours dans le milieu du texte qu'il y a le délai qui compte."],
    ]
  },

  t1: {
    label: "Dialogue — Le service de renseignements, un mardi matin",
    lines: [
      ["MYLÈNE","Tribunal administratif du logement, service de renseignements, Mylène Poitras. Bonjour."],
      ["FARIDA","Bonjour madame. Je m'appelle Farida Belkacem. J'ai lu votre page sur la sous-location hier soir et il me reste deux ou trois choses que je n'ai pas comprises."],
      ["MYLÈNE","C'est exactement pour ça que le service existe. Dites-moi d'abord votre situation, en gros, et on ira au précis après."],
      ["FARIDA","Je pars travailler six mois à l'extérieur, du six janvier au trente juin. Mon bail finit le trente juin. Je voudrais sous-louer mon logement pendant ce temps-là et le reprendre en juillet."],
      ["MYLÈNE","C'est une sous-location, effectivement. Vous restez locataire, et la personne qui habite chez vous devient votre sous-locataire. Votre bail, lui, ne change pas."],
      ["FARIDA","Sur la page, c'est écrit que je dois aviser mon locateur. Est-ce que je peux simplement lui en parler quand je le croise dans l'escalier ?"],
      ["MYLÈNE","Vous pouvez lui en parler, bien sûr, mais ça ne remplace pas l'avis. L'avis doit être écrit. Et il doit contenir deux renseignements précis : le nom et l'adresse de la personne à qui vous voulez sous-louer."],
      ["FARIDA","Donc il faut que j'aie déjà trouvé quelqu'un avant d'écrire."],
      ["MYLÈNE","Il le faut, oui. Beaucoup de gens font la démarche à l'envers : ils demandent la permission d'abord, en général, et on leur répond en général. Un avis sans nom ne fait courir aucun délai."],
      ["FARIDA","Quel délai ?"],
      ["MYLÈNE","Le locateur a quinze jours pour vous répondre à partir du moment où il reçoit votre avis. C'est le chiffre le plus important de toute la page, et c'est celui que les gens sautent."],
      ["FARIDA","Et s'il ne répond pas du tout ? S'il fait le mort pendant un mois ?"],
      ["MYLÈNE","S'il ne répond pas dans les quinze jours, il est réputé avoir consenti. Autrement dit, son silence vaut un oui. C'est pour ça que je vous conseille de garder une preuve de la date où il a reçu votre avis."],
      ["FARIDA","Une preuve, comment ? Je ne peux pas lui faire signer un papier de force."],
      ["MYLÈNE","Non, mais vous pouvez lui faire signer une copie s'il accepte, ou envoyer votre avis par un moyen qui laisse une trace. Ce que vous voulez pouvoir dire plus tard, c'est : le dix-huit novembre, il l'avait entre les mains."],
      ["FARIDA","Et il a le droit de refuser ?"],
      ["MYLÈNE","Il a le droit de refuser, mais pas pour n'importe quoi. Il lui faut un motif sérieux, et c'est à lui de le dire dans sa réponse. Il doit vous expliquer pourquoi, par écrit."],
      ["FARIDA","Qu'est-ce que c'est, un motif sérieux ? Parce que mon propriétaire, lui, il va trouver mille raisons."],
      ["MYLÈNE","Un motif sérieux regarde la personne proposée ou le logement, pas votre projet à vous. Une personne dont le dossier de paiement est mauvais, par exemple. Ce n'est pas un motif sérieux de dire qu'on préfère un couple à un étudiant, ou qu'on n'aime pas l'idée."],
      ["FARIDA","Et s'il me demande de l'argent pour accepter ?"],
      ["MYLÈNE","Il peut vous demander le remboursement des dépenses raisonnables que la sous-location lui occasionne — une vérification de crédit, par exemple, s'il en fait une. Il ne peut pas transformer ça en frais fixe qu'il décide tout seul. Si vous n'êtes pas d'accord, l'un comme l'autre peut s'adresser au Tribunal."],
      ["FARIDA","Bon. Alors j'ai compris l'ordre : je trouve quelqu'un, j'écris l'avis avec son nom et son adresse, je garde une preuve, et je compte quinze jours."],
      ["MYLÈNE","Voilà votre démarche, dans le bon ordre. Et gardez une copie de tout, madame Belkacem. Un dossier qui se défend, c'est un dossier qui a des dates."],
    ]
  },

  t2: {
    label: "Dialogue — L'avis, sur le palier du deuxième",
    lines: [
      ["FARIDA","Monsieur Tardif ? Bonjour. Vous avez deux minutes ? J'ai un papier à vous remettre et j'aimerais mieux vous l'expliquer moi-même."],
      ["LUCIEN","Un papier. Ça commence bien. Vous partez, c'est ça ? Tout le monde part cette année. Ne me dites pas que vous résiliez : le bail court jusqu'au trente juin."],
      ["FARIDA","Je ne résilie rien, monsieur Tardif. C'est le contraire : je veux garder mon logement. Je pars travailler six mois à Sept-Îles et je reviens le premier juillet."],
      ["LUCIEN","Six mois. Et le loyer, pendant ce temps-là, il tombe du ciel ?"],
      ["FARIDA","Non. C'est justement pour ça que je veux sous-louer. Le loyer continue d'être payé, le logement reste occupé et chauffé, et vous n'avez personne à chercher."],
      ["LUCIEN","Sous-louer. J'ai déjà donné, moi, la sous-location. Il y a six ans, au quatre, ç'a été un vrai cirque."],
      ["FARIDA","Je comprends que ça vous rende méfiant. C'est pour ça que je ne viens pas vous demander la permission en l'air : je viens avec un nom, une adresse et des dates."],
      ["LUCIEN","Un nom. Qui c'est ?"],
      ["FARIDA","Nicolas Trudel, vingt-quatre ans, étudiant en génie civil au cégep de Limoilou. Il travaille vingt heures par semaine dans une quincaillerie. Il habite présentement chez ses parents, à Beauport, et l'adresse est écrite sur l'avis."],
      ["LUCIEN","Un étudiant. Il va me faire des partys jusqu'à trois heures du matin, et c'est moi qui vais recevoir les appels."],
      ["FARIDA","Vous avez le droit de vérifier son dossier, et je vous encourage à le faire. Mais je vous dis tout de suite ce que j'ai lu sur le site du Tribunal : pour refuser, il faut un motif sérieux, et il doit regarder la personne, pas son âge."],
      ["LUCIEN","Vous êtes allée voir sur Internet, à ce que je vois."],
      ["FARIDA","Je suis allée voir avant de venir, oui. Je ne veux pas me chicaner avec vous, monsieur Tardif. Ça fait trois ans que je paie le premier du mois et que je n'ai jamais rien demandé."],
      ["LUCIEN","Ça, c'est vrai. Vous, je n'ai jamais eu à courir après."],
      ["FARIDA","Alors voici l'avis. Il est daté d'aujourd'hui, le dix-huit novembre. Il y a le nom de monsieur Trudel, son adresse, et les dates de la sous-location : du cinq janvier au vingt-huit juin."],
      ["LUCIEN","Et je fais quoi avec ça, moi ?"],
      ["FARIDA","Vous avez quinze jours pour me répondre par écrit. Si vous refusez, vous m'expliquez pourquoi. Et si vous ne répondez pas d'ici le trois décembre, la loi considère que vous avez consenti."],
      ["LUCIEN","Quinze jours. Vous avez tout appris par cœur, hein."],
      ["FARIDA","J'ai appris ce qui me concerne. Est-ce que vous accepteriez de me signer cette copie, juste pour dire que vous l'avez reçue aujourd'hui ? Ce n'est pas un accord, c'est une date."],
      ["LUCIEN","Donnez-moi votre stylo. Je signe la date, rien d'autre. Et je vous préviens : je vais le regarder de proche, votre étudiant."],
      ["FARIDA","Regardez-le de proche, monsieur Tardif. C'est exactement ce que je vous demande."],
    ]
  },

  t2b: {
    label: "Dialogue — La visite du logement, un samedi de novembre",
    lines: [
      ["NICOLAS","Bonjour madame Belkacem. Nicolas Trudel. On s'est parlé au téléphone jeudi."],
      ["FARIDA","Bonjour, entrez. Enlevez vos bottes, il y a un tapis. Alors, voilà : c'est un quatre et demie, deuxième étage, deux chambres."],
      ["NICOLAS","C'est plus grand que sur les photos. Et c'est clair."],
      ["FARIDA","Le soleil entre le matin, de ce côté-là. Avant de faire le tour, je veux être bien claire sur une chose : ce n'est pas une location, c'est une sous-location."],
      ["NICOLAS","C'est-à-dire ?"],
      ["FARIDA","Le bail reste à mon nom. Vous n'aurez pas de bail avec monsieur Tardif : vous en aurez un avec moi, pour six mois. Le premier juillet, je reviens, et vous, vous repartez."],
      ["NICOLAS","Ça me va. Ma session finit le vingt-deux juin, de toute façon."],
      ["FARIDA","Autre chose, et j'aime mieux le dire tout de suite : si vous ne payez pas, c'est moi que le propriétaire va poursuivre. Alors je vais vous demander des références, et je vais les appeler."],
      ["NICOLAS","C'est correct. Vous pouvez appeler mon patron à la quincaillerie et mon ancien propriétaire de Charlesbourg. Je vous laisse les numéros."],
      ["FARIDA","Parfait. Le loyer est de huit cent quatre-vingt-quinze dollars, chauffé, éclairé à part. Payable le premier du mois, dans mon compte."],
      ["NICOLAS","Il y a une laveuse ?"],
      ["FARIDA","Non, mais il y a une buanderie au sous-sol, et le local à vélos est là aussi. La case de stationnement, elle, n'est pas comprise : elle appartient au logement du trois."],
      ["NICOLAS","Je n'ai pas d'auto, donc ça ne me dérange pas. Le bruit, c'est comment ?"],
      ["FARIDA","Tranquille. Une dame seule en haut, un couple avec un bébé en bas. Si vous recevez du monde, ce n'est pas un problème, mais après onze heures on baisse le ton."],
      ["NICOLAS","Ça, je peux vivre avec."],
      ["FARIDA","Il reste une condition, et elle ne dépend pas de moi : monsieur Tardif a jusqu'au trois décembre pour répondre. S'il refuse avec un motif sérieux, la sous-location ne se fait pas."],
      ["NICOLAS","Et s'il ne répond pas ?"],
      ["FARIDA","S'il ne répond pas d'ici là, la loi considère qu'il a consenti, et on signe. Je vous appelle le quatre décembre au matin, dans un cas comme dans l'autre."],
      ["NICOLAS","Ça me convient. Je vous envoie mes références ce soir."],
    ]
  },
};
