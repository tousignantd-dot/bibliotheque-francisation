const DIALOGUES = {
  prep: {
    label: "Dialogue — Qui travaille ici ?",
    lines: [
      ["AMEL","Excusez-moi, monsieur. Je cherche le local 214."],
      ["MARC","Bonjour ! Le 214, c'est au deuxième étage."],
      ["AMEL","Au deuxième étage… Merci. Et le secrétariat ?"],
      ["MARC","Le secrétariat est ici, au rez-de-chaussée."],
      ["AMEL","À côté de la porte d'entrée ?"],
      ["MARC","Oui, à côté de l'entrée. Le comptoir est là."],
      ["AMEL","Merci beaucoup. Vous êtes l'enseignant ?"],
      ["MARC","Non, je suis le concierge. Moi, j'ouvre les portes."],
      ["AMEL","Ah ! Excusez-moi."],
      ["MARC","Ce n'est rien. Bonne journée, madame."]
    ]
  },

  t1: {
    label: "Dialogue — Au comptoir du secrétariat",
    lines: [
      ["AMEL","Bonjour, madame."],
      ["LINE","Bonjour ! Qu'est-ce que je peux faire pour vous ?"],
      ["AMEL","Je voudrais une attestation, s'il vous plaît."],
      ["LINE","Votre nom ?"],
      ["AMEL","Amel Tazi. T-A-Z-I."],
      ["LINE","Merci. Vous êtes dans le groupe de madame Dufresne ?"],
      ["AMEL","Oui. Le cours du matin, local 214."],
      ["LINE","Parfait. L'attestation est prête jeudi."],
      ["AMEL","Jeudi. À quelle heure ?"],
      ["LINE","Après neuf heures. Vous venez au comptoir."],
      ["AMEL","D'accord. Jeudi, après neuf heures. Merci beaucoup."],
      ["LINE","Bonne journée, madame Tazi."]
    ]
  },

  t1b: {
    label: "Dialogue — À quelle heure ouvre le secrétariat ?",
    lines: [
      ["AMEL","Madame, une question. Le secrétariat ouvre à quelle heure ?"],
      ["LINE","À huit heures, du lundi au vendredi."],
      ["AMEL","Et il ferme quand ?"],
      ["LINE","À seize heures. Mais le midi, c'est fermé."],
      ["AMEL","Le midi… De midi à treize heures ?"],
      ["LINE","C'est ça. Une heure."],
      ["AMEL","Et le samedi ?"],
      ["LINE","Le samedi, le centre est fermé."],
      ["AMEL","D'accord. Huit heures, seize heures, fermé le midi."],
      ["LINE","Voilà. C'est écrit sur la porte aussi."]
    ]
  },

  t2: {
    label: "Dialogue — Demain, je ne viens pas",
    lines: [
      ["AMEL","Bonjour, madame. Demain, je ne viens pas au cours."],
      ["LINE","Vous êtes malade ?"],
      ["AMEL","Non. J'ai un rendez-vous à la clinique."],
      ["LINE","D'accord. Votre nom et votre groupe ?"],
      ["AMEL","Amel Tazi, groupe de madame Dufresne."],
      ["LINE","Merci. J'écris votre absence."],
      ["AMEL","Est-ce que je dois écrire un papier ?"],
      ["LINE","Non, ce n'est pas nécessaire. Je préviens l'enseignante."],
      ["AMEL","Merci beaucoup, madame."],
      ["LINE","À jeudi, madame Tazi."]
    ]
  },

  t2b: {
    label: "Dialogue — L'avis sur la porte",
    lines: [
      ["AMEL","Monsieur Ouellet ! Il y a un papier sur la porte."],
      ["MARC","Oui, c'est un avis. Vous savez lire ça ?"],
      ["AMEL","Je lis… « Lundi 13 octobre : le centre est fermé. »"],
      ["MARC","C'est ça. Lundi, c'est un congé."],
      ["AMEL","Alors il n'y a pas de cours lundi ?"],
      ["MARC","Non. Pas de cours, et le secrétariat est fermé aussi."],
      ["AMEL","Et mardi ?"],
      ["MARC","Mardi, tout est ouvert. Soyez à l'heure !"],
      ["AMEL","Huit heures et demie. D'accord, merci."],
      ["MARC","Bonne fin de semaine, madame Tazi."]
    ]
  },

  appli: {
    label: "Dialogue — C'est moi qui explique",
    lines: [
      ["SAMI","Excusez-moi, c'est mon premier jour. Où est le secrétariat ?"],
      ["AMEL","Au rez-de-chaussée, à côté de l'entrée."],
      ["SAMI","Merci ! Et il ouvre à quelle heure ?"],
      ["AMEL","À huit heures. Mais le midi, c'est fermé."],
      ["SAMI","Et si je suis absent ?"],
      ["AMEL","Vous allez au comptoir et vous prévenez la secrétaire."],
      ["SAMI","Je dois écrire un papier ?"],
      ["AMEL","Non. Vous dites votre nom et votre groupe. C'est tout."],
      ["SAMI","Merci beaucoup !"],
      ["AMEL","Ce n'est rien. Votre local est au deuxième étage."]
    ]
  },
};
