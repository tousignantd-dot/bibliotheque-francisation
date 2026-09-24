"""Ce que la gérante demande — l'exercice 6 (objectif O5).

Audit de la boucle didactique, 24 septembre 2026 (A3, majeur) : comprendre une
consigne de la gérante était ÉVALUÉ par douze items du test (partie C) et
PRATIQUÉ nulle part. Voici seize consignes d'entraînement, toutes différentes de
celles du test : la gérante tutoie, parle au débit normal (Sylvie HD), nomme un
à trois objets ; les dernières demandent de trier — ce qu'il faut faire EN
DERNIER, ce qu'il ne faut PAS toucher. Les réponses se touchent en image.

(id, phrase de la gérante, question, bonne réponse, [distracteurs]) — des id du
lexique qui ont un croquis. Aux consignes à plusieurs objets, les distracteurs
COMPRENNENT les autres objets nommés : on ne réussit pas en reconnaissant un mot.
Audit, tour 3 (A3, majeur) : c'était écrit, pas fait — 12 consignes sur 16 se
réussissaient en repérant le seul mot connu. Le build le vérifie maintenant : au
moins la moitié des consignes met un autre objet nommé parmi les choix.
"""

CONSIGNES = [
    ("g01", "Apporte-moi le miroir, s'il te plaît.", "Qu'est-ce que la gérante veut ?",
     "miroir", ["cintre", "sac", "presentoir"]),
    ("g02", "Va plier les chandails sur le présentoir.", "Où faut-il aller ?",
     "presentoir", ["vitrine", "caisse", "cabine"]),
    ("g03", "Mets des sacs à la caisse.", "Qu'est-ce qu'il faut mettre à la caisse ?",
     "sac", ["caisse", "recu", "cintre"]),
    ("g04", "La cliente veut une carte-cadeau. Occupe-t'en.", "Que veut la cliente ?",
     "carte-cadeau", ["recu", "sac", "etiquette-prix"]),
    ("g05", "Il y a du linge dans la cabine trois. Va le ramasser.", "Où faut-il aller ?",
     "cabine", ["vitrine", "caisse", "presentoir"]),
    ("g06", "Change le manteau du mannequin, dans la vitrine.", "Où est le mannequin ?",
     "vitrine", ["manteau", "cabine", "caisse"]),
    ("g07", "Le client a oublié son reçu sur le comptoir. Rattrape-le !", "Qu'est-ce que le client a oublié ?",
     "recu", ["sac", "carte-cadeau", "portefeuille"]),
    ("g08", "Mets des étiquettes de prix sur les tuques.", "Qu'est-ce qu'il faut mettre sur les tuques ?",
     "etiquette-prix", ["tuque", "antivol", "cintre"]),
    ("g09", "Range les foulards, pis ensuite, va à la caisse.", "Où faut-il aller à la fin ?",
     "caisse", ["foulard", "cabine", "presentoir"]),
    ("g10", "Les bottes, mets-les pas dans la vitrine : mets-les sur le présentoir.", "Où vont les bottes ?",
     "presentoir", ["vitrine", "cabine", "caisse"]),
    ("g11", "Avant la caisse, passe par les cabines pis rapporte les cintres.", "Qu'est-ce qu'il faut rapporter ?",
     "cintre", ["caisse", "cabine", "sac"]),
    ("g12", "Oublie le miroir. Ce qui presse, c'est la vitrine.", "Qu'est-ce qui presse ?",
     "vitrine", ["miroir", "cabine", "caisse"]),
    ("g13", "Le monsieur veut payer. Va à la caisse, pas aux cabines.", "Où faut-il aller ?",
     "caisse", ["cabine", "vitrine", "presentoir"]),
    ("g14", "Enlève les antivols des manteaux en solde.", "Qu'est-ce qu'il faut enlever ?",
     "antivol", ["manteau", "etiquette-prix", "cintre"]),
    ("g15", "Donne-lui un reçu-cadeau avec son sac.", "Qu'est-ce qu'il faut donner en plus du sac ?",
     "recu", ["sac", "carte-cadeau", "etiquette-prix"]),
    ("g16", "Laisse faire les cintres. Va plutôt aider la dame au miroir.", "Où est la dame ?",
     "miroir", ["cintre", "cabine", "caisse"]),
]
