const DIALOGUES = {
  prep: {
    label: "Dialogue — C'est ma première fois",
    lines: [
      ["AMADOU","Bonjour, monsieur. C'est ma première fois."],
      ["CLAUDE","Bonjour ! Vous voulez retirer de l'argent ?"],
      ["AMADOU","Oui. Quarante dollars."],
      ["CLAUDE","Vous avez votre carte ?"],
      ["AMADOU","Oui, elle est là. Et j'ai mon NIP."],
      ["CLAUDE","Parfait. Ne dites jamais votre NIP à voix haute."],
      ["AMADOU","Ah ! D'accord. Merci."],
      ["CLAUDE","Le guichet est libre. Je reste ici."]
    ]
  },

  t1: {
    label: "Dialogue — L'écran parle, Amadou répond",
    lines: [
      ["ÉCRAN","Bonjour. Entrez votre NIP."],
      ["AMADOU","Quatre chiffres. Un, deux, trois, quatre… non, je ne dis rien."],
      ["ÉCRAN","Choisissez une opération : retrait, dépôt, solde."],
      ["AMADOU","Retrait. J'appuie sur retrait."],
      ["ÉCRAN","Choisissez un montant : vingt, quarante, soixante dollars."],
      ["AMADOU","Quarante dollars."],
      ["ÉCRAN","Prenez votre carte. Prenez votre argent."],
      ["AMADOU","Ma carte. Mon argent. Deux billets de vingt."],
      ["ÉCRAN","Voulez-vous un relevé ?"],
      ["AMADOU","Oui. Je prends le relevé."]
    ]
  },

  t1b: {
    label: "Dialogue — Attention aux frais",
    lines: [
      ["AMADOU","Monsieur Fontaine, l'écran écrit « des frais ». C'est quoi ?"],
      ["CLAUDE","C'est de l'argent en plus. Vous payez pour le retrait."],
      ["AMADOU","Pourquoi ? Ici, c'est ma caisse."],
      ["CLAUDE","Ici, non. Mais dans un magasin, oui : ce guichet n'est pas à nous."],
      ["AMADOU","Alors je paie deux fois ?"],
      ["CLAUDE","Un peu, oui. L'écran écrit le montant avant."],
      ["AMADOU","Et je peux dire non ?"],
      ["CLAUDE","Oui. Vous appuyez sur « annuler » et vous reprenez la carte."],
      ["AMADOU","D'accord. Je lis l'écran avant."],
      ["CLAUDE","C'est ça. Toujours lire avant d'appuyer."]
    ]
  },

  t2: {
    label: "Dialogue — Le centre ne prend pas le comptant",
    lines: [
      ["MONIQUE","Bonjour ! Le cours de natation, c'est quarante-cinq dollars."],
      ["AMADOU","Bonjour. J'ai l'argent comptant."],
      ["MONIQUE","Nous ne prenons pas le comptant. Un chèque ou la carte."],
      ["AMADOU","J'ai des chèques. Mais je ne sais pas écrire un chèque."],
      ["MONIQUE","C'est facile. La date d'abord, en haut."],
      ["AMADOU","Le 14 mars 2026."],
      ["MONIQUE","Après, le nom : Centre sportif Sainte-Cécile."],
      ["AMADOU","Et le montant ?"],
      ["MONIQUE","Deux fois : 45,00 en chiffres, et en lettres en dessous."],
      ["AMADOU","Et je signe en bas ?"],
      ["MONIQUE","Oui. Vous signez en bas, à droite."]
    ]
  },

  t2b: {
    label: "Dialogue — Il manque quelque chose",
    lines: [
      ["MONIQUE","Attendez. Il manque une chose sur votre chèque."],
      ["AMADOU","Ah bon ? J'ai écrit la date et le nom."],
      ["MONIQUE","Oui, mais le montant en lettres n'est pas là."],
      ["AMADOU","Quarante-cinq… ça s'écrit comment ?"],
      ["MONIQUE","Quarante-cinq dollars. Avec un trait entre les deux mots."],
      ["AMADOU","D'accord. Et après le mot, je fais un trait ?"],
      ["MONIQUE","Oui, un trait jusqu'au bout de la ligne."],
      ["AMADOU","Pourquoi ?"],
      ["MONIQUE","Pour que personne n'ajoute un mot après."],
      ["AMADOU","Ah ! Je comprends. Voilà, c'est fini."]
    ]
  },

  appli: {
    label: "Dialogue — Cette fois, c'est Amadou qui explique",
    lines: [
      ["LEÏLA","Amadou, tu m'aides ? Je n'ai jamais fait de retrait."],
      ["AMADOU","Oui. Regarde : tu mets ta carte ici."],
      ["LEÏLA","Après ?"],
      ["AMADOU","Tu tapes ton NIP. Quatre chiffres. Tu ne dis rien."],
      ["LEÏLA","Et pour l'argent ?"],
      ["AMADOU","Tu choisis « retrait », puis un montant. Vingt, quarante, soixante."],
      ["LEÏLA","Moi, je veux soixante dollars."],
      ["AMADOU","Alors tu appuies sur soixante. Trois billets de vingt."],
      ["LEÏLA","Et c'est fini ?"],
      ["AMADOU","Non ! Tu prends ta carte, ton argent et ton relevé."]
    ]
  },
};
