const CARRIER_PHRASES = {
  // Une phrase porteuse par mot isolé à prononcer. Un mot envoyé seul à la
  // synthèse sort mal accentué ; la phrase le remet dans un contexte
  // français, et seul le mot est découpé.
  //
  // Les clés sont les mots **accentués**, tels qu'ils paraissent dans les
  // listes savoir[…][2] de exos.js — jamais en slug, sans quoi la pastille
  // lirait le mot seul sans que rien ne le signale.
  //
  // Vingt et une clés pour vingt et une pastilles, une par mot des quatre
  // bandeaux à speak:true. Aucun mot ne paraît dans deux bandeaux.

  // ── Je découvre : les mots du contrat signé ──
  'une étiquette':                     "L'étiquette du véhicule était collée dans la vitre arrière.",
  "l'odomètre":                        "Le chiffre inscrit à l'odomètre était de cent quatre mille kilomètres.",
  'les frais de crédit':               "Les frais de crédit s'élevaient à deux mille sept cent quarante et un dollars.",
  "l'obligation totale":               "L'obligation totale se lit dans la case du bas, à droite.",
  'le taux de crédit':                 "Le taux de crédit reste le même pendant toute la durée du contrat.",
  'une garantie prolongée':            "Une garantie prolongée se paie et comporte presque toujours des exclusions.",

  // ── Défi 1 : nommer une panne ──
  'un cognement':                      "Un cognement se fait entendre au passage des rapports, le matin.",
  'la transmission':                   "La transmission change les rapports pendant qu'on roule.",
  'une fuite':                         "Une fuite rouge sous l'auto vient de la transmission.",
  'un diagnostic':                     "Le diagnostic du garage tenait en deux lignes.",
  'un témoin lumineux':                "Aucun témoin lumineux ne s'était allumé au tableau de bord.",

  // ── Défi 2 : les mots de la réclamation ──
  'la garantie légale':                "La garantie légale ne s'achète pas : elle est déjà dans la loi.",
  'la garantie de bon fonctionnement': "La garantie de bon fonctionnement dépend de la catégorie du véhicule.",
  "l'usure normale":                   "L'usure normale est la première phrase qu'on entend au comptoir.",
  'une réclamation':                   "Sa réclamation portait sur les pièces et la main-d'œuvre.",
  'une exclusion':                     "Une exclusion se lit à la troisième page du contrat.",

  // ── Défi 3 : les mots de la lettre ──
  'une mise en demeure':               "La mise en demeure accordait un délai de dix jours.",
  'un délai raisonnable':              "Un délai raisonnable de dix jours est ce qu'on accorde le plus souvent.",
  'une pièce justificative':           "Elle a joint trois pièces justificatives à sa lettre.",
  'un accusé de réception':            "L'accusé de réception prouve la date, pas le contenu.",
  'la Division des petites créances':  "À la Division des petites créances, on se représente soi-même.",
};
