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
#
# Audit de la boucle didactique, tour 2 (D4, majeur) : la bonne réponse était
# souvent la plus longue et la plus polie, et « Oui. », « Non. » étaient faux
# quel que soit le client — on faisait 5 sur 8 sans écouter. Désormais :
#   · les trois réponses ont des longueurs voisines (contrôlé au build) ;
#   · chaque mauvaise est POLIE et plausible, mais fait le MAUVAIS geste ;
#   · deux paires se répondent : la même phrase appelle un geste différent
#     selon un détail entendu — dite vite (r04, faire répéter) ou posément
#     (r09, vérifier) ; sans reçu (r05, la gérante) ou avec (r10, la caisse).
REPONSES = [
    ("r01", "client", "Non merci, je fais juste regarder.",
     "Parfait. Je suis là si vous avez besoin.",
     [("Venez voir, les manteaux sont en solde !", "Il a dit qu'il regarde : insister le fait partir."),
      ("Parfait. Quelle taille cherchez-vous ?", "Il ne cherche rien encore : la question arrive trop tôt.")],
     "Vous le laissez regarder : il reviendra vers vous."),
    ("r02", "client", "Je cherche des jeans.",
     "Oui ! Quelle taille cherchez-vous ?",
     [("Oui, on a des jeans en grand, ici.", "Vous devinez la taille : demandez-la."),
      ("Un instant. Je vais chercher la gérante.", "Rien ici ne demande la gérante : c'est une demande simple.")],
     "Une question à la fois : il sait quoi répondre."),
    ("r03", "client", "Vous l'avez-tu en moyen, le manteau noir ?",
     "Un manteau noir, en moyen. Je vais vérifier.",
     [("Oui, oui, il en reste en moyen, c'est sûr !", "Vous promettez sans vérifier : s'il n'y en a plus, le client est déçu."),
      ("D'accord. Quelle couleur voulez-vous ?", "Il a déjà dit « noir » : redites plutôt ce qu'il demande.")],
     "Vous redites : s'il y a une erreur, il la corrige tout de suite."),
    ("r04", "client-rapide", "Je voudrais la même affaire en plus grand si vous l'avez.",
     "Un instant. Pouvez-vous répéter plus lentement ?",
     [("Oui, bien sûr ! Je vous apporte ça tout de suite.", "Faire semblant de comprendre fait perdre la vente."),
      ("La même, en plus petit. Je vais vérifier.", "Il a dit « plus grand » : quand ça va trop vite, on entend mal. Faites d'abord répéter.")],
     "Faire répéter n'est pas une faute : c'est ce qui garde la vente."),
    ("r05", "client", "Je veux un remboursement. J'ai pas mon reçu.",
     "Un instant. Je vais chercher la gérante.",
     [("Pas de problème, je vous rembourse à la caisse.", "Sans reçu, vous ne pouvez pas promettre un remboursement."),
      ("Désolé, sans reçu, c'est impossible.", "Ce n'est pas à vous de refuser : la gérante décide.")],
     "Passer le relais n'est pas un échec : c'est la bonne personne qui décide."),
    ("r06", "client", "Bonjour !",
     "Bonjour ! Est-ce que je peux vous aider ?",
     [("Bonjour. Qu'est-ce que vous voulez acheter ?", "Trop direct : accueillez d'abord."),
      ("Bonjour ! Venez voir nos soldes, par ici !", "Il vient d'entrer : vous l'entraînez avant de savoir ce qu'il veut.")],
     "Une fois, poliment, et le client sait qu'il peut vous parler."),
    ("r07", "client", "Ce chandail-là, vous l'avez-tu en d'autres couleurs ?",
     "Je vais vérifier. Quelle couleur voulez-vous ?",
     [("Oui, on l'a dans toutes les couleurs !", "Vous promettez sans savoir."),
      ("Non, je pense qu'on l'a juste en gris.", "Vous devinez au lieu de vérifier.")],
     "Vous faites préciser, et vous vérifiez : ensuite, vous saurez quoi aller chercher."),
    ("r08", "client", "Mon manteau est décousu ! C'est de la mauvaise qualité !",
     "Je comprends. Je vais chercher la gérante.",
     [("Je comprends. Je vous en donne un autre.", "Vous ne pouvez pas le décider : la gérante décide."),
      ("C'est pas notre faute, c'est l'usure.", "La cliente se fâche davantage : vous vous défendez au lieu de l'aider.")],
     "Vous l'écoutez, puis vous passez le relais : elle se calme."),
    ("r09", "client", "Le même chandail, en moyen, s'il vous plaît.",
     "Le même, en moyen. Je vais vérifier.",
     [("Pouvez-vous répéter plus lentement ?", "Il a parlé clairement : faire répéter ici le fait attendre pour rien."),
      ("Oui, il en reste en moyen, c'est sûr.", "Vous promettez sans vérifier.")],
     "Il a été clair : vous redites, puis vous vérifiez. Faire répéter, c'est quand on n'a PAS compris."),
    ("r10", "client", "Je voudrais l'échanger pour un moyen. J'ai mon reçu.",
     "Avec le reçu, oui. Allons à la caisse.",
     [("Un instant. Je vais chercher la gérante.", "Avec le reçu, un échange est simple : inutile de déranger la gérante."),
      ("Désolé, on ne fait pas d'échanges ici.", "Vous refusez à la place du magasin, et à tort.")],
     "Il a son reçu : c'est la caisse qui fait l'échange. Sans reçu, ce serait la gérante."),
    # Audit, tour 3 (A3) : la mise de côté, pratiquée des deux côtés de la règle.
    ("r11", "client", "Pouvez-vous me mettre ce manteau de côté jusqu'à demain ?",
     "Oui. Votre nom et votre numéro, s'il vous plaît.",
     [("Un instant. Je vais chercher la gérante.", "Sans argent, une mise de côté, vous la faites vous-même."),
      ("Désolé, on ne met rien de côté ici.", "Vous refusez à la place du magasin, et à tort.")],
     "Sans argent, vous pouvez le faire : le nom et le numéro suffisent."),
    ("r12", "client", "Je vous laisse vingt piastres, pis vous me le gardez une semaine ?",
     "Un instant. Je demande à la gérante.",
     [("Oui. Votre nom et votre numéro, s'il vous plaît.", "Il y a de l'argent : c'est la gérante qui décide."),
      ("Parfait, je prends l'argent tout de suite.", "Vous acceptez un dépôt que vous ne pouvez pas décider.")],
     "Dès qu'il y a de l'argent, c'est la gérante : ce n'est pas un échec."),
]
