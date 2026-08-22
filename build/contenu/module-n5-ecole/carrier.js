const CARRIER_PHRASES = {
  // La clé est le mot LITTÉRAL, tel qu'il paraît dans FC_CARDS et dans la
  // troisième colonne des rangées `savoir` de exos.js : le gabarit fait
  // `CARRIER_PHRASES[w]` sans rien normaliser. Une clé écrite en slug, sans
  // article ou sans accent, ne serait jamais trouvée — la pastille lirait
  // alors le mot tout seul, mal accentué, et rien ne le signalerait avant
  // l'écoute.
  //
  // Sept clés portent un accent qui compte : « le secrétariat », « une
  // conseillère », « une pièce justificative », « une échéance », « un
  // relevé », « un délai », « un motif ». Elles sont écrites ici exactement
  // comme dans fccards.js.
  //
  // Les seize mots servent tous de pastille au moins une fois dans un bloc
  // `savoir` à `speak:true` — relevé croisé fait sur exos.js, dans les deux
  // sens : aucun mot sans phrase porteuse, aucune clé inutilisée.

  // Je découvre — l'établissement et son monde
  'le secrétariat':          "Le secrétariat est ouvert de huit heures à seize heures.",
  'une conseillère':         "La conseillère reçoit sur rendez-vous, au local 112.",
  'un local':                "Le rattrapage se fait au local 118, deux midis par semaine.",
  'une session':             "La session d'hiver se termine à la fin du mois de juin.",

  // Défi 1 — l'absence annoncée d'avance
  'une absence':             "Une absence annoncée d'avance ne coûte pas sa place.",
  'un motif':                "Le formulaire demande les dates, puis le motif en une phrase.",
  'une pièce justificative': "Elle apportera sa pièce justificative à son retour.",
  'un rattrapage':           "Le rattrapage a lieu le midi, sur inscription au secrétariat.",

  // Défi 2 — l'avis officiel et ses dates
  'un avis':                 "L'avis arrive par courriel et il faut le signer.",
  'une échéance':            "L'échéance est écrite en gras, tout en haut de la page.",
  'un formulaire':           "Ce formulaire se remet au secrétariat avant le départ.",
  'une prolongation':        "En cas de prolongation, il faut appeler avant la fin de l'absence.",

  // Défi 3 — le changement et la preuve
  'un transfert':            "Son transfert au groupe du soir prend effet lundi prochain.",
  'une attestation':         "Son employeur demande une attestation de fréquentation scolaire.",
  'un relevé':               "Le relevé des apprentissages arrive après la fin du cours.",
  'un délai':                "Le délai est de dix jours ouvrables pour un changement de groupe.",
};
