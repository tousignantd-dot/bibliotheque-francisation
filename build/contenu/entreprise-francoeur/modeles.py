"""Les gestes du vendeur — modèles entendus, puis « Ce que je réponds ».

Audit de la boucle didactique, 24 septembre 2026 (C4, majeur, relevé deux
fois) : aucun exemple travaillé. On passait des mots isolés à une conversation
libre, sans jamais entendre un vendeur faire les gestes. D'où deux pièces,
dans l'ordre de l'estompage :

1. MODELES — cinq dialogues très courts, un par geste : le client, puis un
   vendeur qui fait le geste. La phrase clé est mise en évidence.
2. REPONSES — l'exercice 7 : on entend le client, on CHOISIT la réponse du
   vendeur parmi trois. Les deux mauvaises sont des erreurs réelles (promettre
   sans vérifier, faire semblant, insister, refuser à la place de la gérante),
   et chacune a SA rétroaction (E1) : ce qu'elle aurait provoqué.

Voix : le client en Sylvie HD, le vendeur en Thierry HD — toujours le même
vendeur modèle. `rapide` : le client parle vite (c'est ce qu'on fait répéter).
"""

# (id, geste, [(qui, texte)], phrase clé)   qui ∈ {"client", "vendeur", "client-rapide"}
MODELES = [
    ("m1", "Laisser la porte ouverte",
     [("client", "Non merci, je regarde."),
      ("vendeur", "Parfait. Je suis là si vous avez besoin.")],
     "Je suis là si vous avez besoin."),
    ("m2", "Faire préciser, une chose à la fois",
     [("client", "Je cherche un chandail."),
      ("vendeur", "Oui ! Quelle couleur ?"),
      ("client", "Gris."),
      ("vendeur", "Et quelle taille ?"),
      ("client", "Moyen.")],
     "Quelle couleur ? … Et quelle taille ?"),
    ("m3", "Redire, puis vérifier",
     [("client", "Le manteau noir, en moyen, vous l'avez ?"),
      ("vendeur", "Un manteau noir, en moyen. Je vais vérifier en arrière. Je reviens tout de suite.")],
     "Je vais vérifier en arrière."),
    ("m4", "Faire répéter",
     [("client-rapide", "Je voudrais le même en plus grand pis en bleu si vous l'avez."),
      ("vendeur", "Un instant, s'il vous plaît. Pouvez-vous répéter plus lentement ?"),
      ("client", "Le même. Plus grand. En bleu.")],
     "Pouvez-vous répéter plus lentement ?"),
    ("m5", "Passer le relais",
     [("client", "Je veux me faire rembourser, mais j'ai pas mon reçu."),
      ("vendeur", "Un instant. Je vais chercher la gérante.")],
     "Je vais chercher la gérante."),
]

# (id, qui, ce que dit le client, bonne réponse, [(mauvaise réponse, ce qu'elle provoque)], explication de la bonne)
REPONSES = [
    ("r01", "client", "Non merci, je fais juste regarder.",
     "Parfait. Je suis là si vous avez besoin.",
     [("Venez voir, les manteaux sont en solde !", "Il a dit qu'il regarde : insister le fait partir."),
      ("Quelle taille ?", "Il ne cherche rien encore : la question arrive trop tôt.")],
     "Vous le laissez regarder : il reviendra vers vous."),
    ("r02", "client", "Je cherche des jeans.",
     "Quelle taille ?",
     [("Oui, on a des jeans en grand.", "Vous devinez la taille : demandez-la."),
      ("Je vais chercher la gérante.", "Rien ici ne demande la gérante : c'est une demande simple.")],
     "Une question à la fois : il sait quoi répondre."),
    ("r03", "client", "Vous l'avez-tu en moyen, le manteau noir ?",
     "Un manteau noir, en moyen. Je vais vérifier en arrière.",
     [("Oui, oui, on l'a !", "Vous promettez sans vérifier : s'il n'y en a plus, le client est déçu."),
      ("Quelle couleur ?", "Il a déjà dit « noir » : redites plutôt ce qu'il demande.")],
     "Vous redites : s'il y a une erreur, il la corrige tout de suite."),
    ("r04", "client-rapide", "Je voudrais la même affaire en plus grand si vous l'avez.",
     "Un instant, s'il vous plaît. Pouvez-vous répéter plus lentement ?",
     [("Oui.", "Faire semblant de comprendre fait perdre la vente."),
      ("Je vais chercher la gérante.", "Faites d'abord répéter : c'est peut-être simple.")],
     "Faire répéter n'est pas une faute : c'est ce qui garde la vente."),
    ("r05", "client", "Je veux un remboursement. J'ai pas mon reçu.",
     "Un instant. Je vais chercher la gérante.",
     [("Oui, pas de problème, je vous rembourse.", "Sans reçu, vous ne pouvez pas promettre un remboursement."),
      ("Non, c'est impossible.", "Ce n'est pas à vous de refuser : la gérante décide.")],
     "Passer le relais n'est pas un échec : c'est la bonne personne qui décide."),
    ("r06", "client", "Bonjour !",
     "Bonjour ! Je peux vous aider ?",
     [("Qu'est-ce que vous voulez ?", "Trop direct : accueillez d'abord."),
      ("Je vais chercher la gérante.", "Il vient d'entrer : accueillez-le vous-même.")],
     "Une fois, poliment, et le client sait qu'il peut vous parler."),
    ("r07", "client", "Ce chandail-là, vous l'avez-tu en d'autres couleurs ?",
     "Quelle couleur voulez-vous ?",
     [("Non.", "Vous ne savez pas encore : faites préciser, puis vérifiez."),
      ("Oui, dans toutes les couleurs !", "Vous promettez sans savoir.")],
     "Vous faites préciser : ensuite, vous saurez quoi aller chercher."),
    ("r08", "client", "Mon manteau est décousu ! C'est de la mauvaise qualité !",
     "Je comprends. Un instant, je vais chercher la gérante.",
     [("C'est pas ma faute.", "La cliente se fâche davantage : vous vous défendez au lieu de l'aider."),
      ("Je vous en donne un autre tout de suite.", "Vous ne pouvez pas le décider : la gérante décide.")],
     "Vous l'écoutez, puis vous passez le relais : elle se calme."),
]
