const DIALOGUES = {

  prep: {
    label: "Dialogue — Tu n'es jamais sortie de Montréal ?",
    lines: [
      ["CAMILLE","Une semaine de congé à la fin septembre ! Tu t'en vas où ?"],
      ["THUY","Nulle part. Je vais dormir, je pense. Ranger l'appartement."],
      ["CAMILLE","Thuy. Trois ans au Québec et tu n'es jamais sortie de l'île ?"],
      ["THUY","Je suis allée à Laval une fois. Chez la cousine de mon mari."],
      ["CAMILLE","Laval, ce n'est pas sortir de l'île, c'est changer de pont. Moi je viens de Rimouski."],
      ["THUY","C'est loin, ça ?"],
      ["CAMILLE","Cinq cent trente kilomètres. Sept heures d'autocar, huit avec les arrêts. C'est dans le Bas-Saint-Laurent, sur la rive sud du fleuve."],
      ["THUY","Sept heures. Et il y a quoi, là-bas ?"],
      ["CAMILLE","Le fleuve, d'abord. Chez nous il fait quarante kilomètres de large : tu ne vois pas l'autre bord, on dirait la mer. Et il y a le parc du Bic, à vingt minutes de la ville."],
      ["THUY","Un parc comme le parc Jarry ?"],
      ["CAMILLE","Non, non. Un parc national. Des caps, des baies, des îles, des sentiers dans la montagne. Les phoques se couchent sur les roches à marée basse."],
      ["THUY","Des phoques. Au Québec."],
      ["CAMILLE","À trois cents mètres du stationnement. En septembre il n'y a plus personne, l'air est frais, les couleurs commencent. C'est le plus beau moment de l'année."],
      ["THUY","Mais je n'ai pas d'auto, Camille."],
      ["CAMILLE","Tu n'en as pas besoin. L'autocar part de la gare, rue Berri, et il te laisse en plein centre de Rimouski. Après, le gîte va te chercher. Je vais te donner le nom : ma tante y travaille."],
      ["THUY","Attends. Tu es en train de me dire que je pars lundi ?"],
      ["CAMILLE","Je suis en train de te dire que tu vas te renseigner cet après-midi. Le reste, tu décideras après."],
    ]
  },

  t1: {
    label: "Dialogue — Au comptoir, rue Berri",
    lines: [
      ["SERGE","Bonjour ! Je peux vous aider ?"],
      ["THUY","Bonjour. Je voudrais aller à Rimouski, dans le Bas-Saint-Laurent. Je partirais le lundi 28 septembre et je reviendrais le dimanche suivant. Une personne."],
      ["SERGE","Parfait, c'est clair. Rimouski, aller-retour, une personne, du 28 septembre au 4 octobre. Le lundi, j'ai trois départs : sept heures, midi trente et dix-huit heures quinze."],
      ["THUY","Pourriez-vous me dire combien de temps ça prend ?"],
      ["SERGE","Le départ de sept heures arrive à quinze heures dix. Huit heures dix, avec les arrêts. Trois-Rivières, Québec, La Pocatière, Rivière-du-Loup, et Rimouski."],
      ["THUY","Est-ce qu'il faut changer d'autocar ?"],
      ["SERGE","Non, celui-là est direct. Si vous prenez celui de midi trente, il y a une correspondance à Québec, avec quarante minutes d'attente."],
      ["THUY","Alors je préfère le direct. Je voudrais savoir si je peux apporter une grosse valise."],
      ["SERGE","Deux, même. Deux bagages en soute par personne, plus un bagage à main que vous gardez avec vous. Le bagage à main, c'est cinq kilos maximum."],
      ["THUY","Et si j'en ai plus ?"],
      ["SERGE","Là, ça passe par le service de messagerie et ça se paie au poids. Pour une semaine, vous n'en serez pas là."],
      ["THUY","Une dernière chose : est-ce que je peux changer la date du retour, si jamais ?"],
      ["SERGE","Sur ce tarif-ci, oui, moyennant des frais. Sur le tarif économique, non : c'est ferme. La différence est de dix-huit dollars."],
      ["THUY","Je prends celui qui se change. Je ne connais pas la région, je ne sais pas ce que je vais vouloir faire."],
      ["SERGE","Sage. Ça vous fait un aller-retour, départ lundi sept heures, quai 12. Présentez-vous vingt minutes avant : les valises se chargent avant le départ, pas après."],
      ["THUY","Vingt minutes avant, quai 12. Merci beaucoup."],
      ["SERGE","Bon voyage, madame. Vous allez aimer ça."],
    ]
  },

  t2: {
    label: "Dialogue — Ce qui est écrit, et ce qui ne l'est pas",
    lines: [
      ["CAMILLE","Montre-moi. Tu as trouvé la page du parc ?"],
      ["THUY","Oui. C'est écrit : « caps, baies, anses, îles et montagnes, sur trente-trois kilomètres carrés ». Je ne connais pas la moitié de ces mots-là."],
      ["CAMILLE","Un cap, c'est une pointe de roche qui avance dans l'eau. Une anse, c'est un petit creux de la côte, où l'eau est calme. Tu les verras, ça ira mieux."],
      ["THUY","Il y a une liste de sentiers. Celui du bord de l'eau fait cinq kilomètres, celui de la montagne fait sept."],
      ["CAMILLE","Prends celui du bord de l'eau le premier jour. Il est plus long que ce que tu penses, à cause des roches."],
      ["THUY","Et pour dormir, il y a du camping. Quatre secteurs. Et du prêt-à-camper."],
      ["CAMILLE","Le prêt-à-camper, c'est déjà monté : les lits, la vaisselle, tout est là. Mais fin septembre, la nuit, il fait cinq degrés au bord du fleuve."],
      ["THUY","Cinq degrés ! Ce n'est pas écrit, ça."],
      ["CAMILLE","Ce n'est jamais écrit. C'est pour ça que tu me demandes. Prends le gîte : c'est plus cher que le camping, mais c'est chauffé, et le déjeuner est compris."],
      ["THUY","Le gîte demande cent dix dollars la nuit en haute saison, et quatre-vingt-dix après le 15 septembre."],
      ["CAMILLE","Tu y seras le 28. Tu paies le tarif de basse saison, donc. Six nuits à quatre-vingt-dix."],
      ["THUY","J'ai regardé le train aussi. L'Océan passe à Rimouski, mais seulement trois jours par semaine : le mercredi, le vendredi et le dimanche."],
      ["CAMILLE","Et il part de Montréal à dix-huit heures trente, donc tu arrives en pleine nuit. L'autocar est moins romantique, mais il part le matin et il te laisse au centre-ville à trois heures."],
      ["THUY","Alors l'autocar est plus pratique que le train, même s'il est moins confortable."],
      ["CAMILLE","Exactement. Et une dernière chose qui n'est écrite nulle part : les heures de marée. Regarde-les avant de marcher jusqu'à l'île. Des gens se font prendre chaque été."],
      ["THUY","Comment on les trouve ?"],
      ["CAMILLE","À l'accueil du parc, sur une feuille, chaque matin. Demande-la. C'est la première chose que je demanderais."],
    ]
  },

  t3: {
    label: "Dialogue — Le gîte, puis le sentier",
    lines: [
      ["ROSE-AIMÉE","Bienvenue ! Vous avez fait bon voyage ?"],
      ["THUY","Bonjour madame. Oui, très bon. Huit heures, mais je n'ai pas vu le temps passer : je regardais dehors tout le long."],
      ["ROSE-AIMÉE","C'est la première fois que vous descendez par ici ?"],
      ["THUY","La première fois que je sors de Montréal, en fait. Je suis arrivée du Viêt Nam il y a trois ans."],
      ["ROSE-AIMÉE","Eh bien vous commencez par le bon bout. Vous restez combien de temps ?"],
      ["THUY","Six nuits. Je repars dimanche matin."],
      ["ROSE-AIMÉE","Parfait. Le déjeuner est servi de sept heures à neuf heures, en bas. Demain il va faire beau et frais, quatorze degrés. La marée descend vers dix heures : c'est le bon moment pour aller voir les phoques."],
      ["THUY","Je peux y aller à pied depuis ici ?"],
      ["ROSE-AIMÉE","En marchant, comptez quarante minutes. En passant par le petit chemin derrière l'église, vous coupez dix minutes et c'est plus joli."],
      ["THUY","Merci beaucoup. Je vais essayer ça demain."],
      ["DENIS","Bonjour ! Belle journée, hein ?"],
      ["THUY","Bonjour. Oui, magnifique. Je n'avais jamais vu le fleuve comme ça."],
      ["DENIS","Vous n'êtes pas du coin, vous non plus ? Moi je viens de Sherbrooke. On monte ici tous les automnes, ma femme et moi."],
      ["THUY","J'arrive de Montréal. C'est ma première fois dans la région."],
      ["DENIS","Et vous êtes montée jusqu'au belvédère ? C'est là-haut, à vingt minutes. Vous voyez les îles, et par temps clair vous voyez l'autre rive."],
      ["THUY","Pas encore. J'ai fait le sentier du bord de l'eau ce matin, et hier j'ai visité le phare pendant qu'il pleuvait."],
      ["DENIS","Le phare, c'est bien. Mais montez au belvédère avant de repartir. C'est ce qu'on vient chercher ici."],
      ["THUY","J'y vais cet après-midi, d'abord. Merci du conseil !"],
      ["DENIS","Bon séjour, madame. Et bienvenue chez nous."],
    ]
  },

};
