"""La fiche de poche de la Maison Francœur — ce qui reste dans le tablier.

Six phrases du vendeur, dans l'ordre d'une vente : elles RESTENT en français —
c'est ce qu'on dit sur le plancher. La langue d'appui, en petit, dessous, dit
QUAND s'en servir ; elle ne remplace jamais la phrase. Les pièges, couleurs et
tailles de la fiche sont lus dans le lexique et ses traductions : rien n'est
recopié.

Les traductions de `quand` se font par
`python3 build/francoeur_traductions.py --fiche` et se rangent dans
traductions.json sous `fiche` ; tant qu'elles manquent, la fiche imprime le
français seul pour ces lignes, et le dit.
"""

# Audit, tour 3 (A3, majeur) : ce que le vendeur décide seul n'était écrit
# nulle part, et la mise de côté recevait trois verdicts. LA RÈGLE, écrite une
# fois, reprise par la phrase « relais » ci-dessous, le guide, les clients du
# magasin et « Ce que je réponds ».
# Simplifiée le 2 oct. 2026 (Daniel, après la partie C de l'hôtel : « fais quelque
# chose de simple ») : une question, qui décide, l'exception. Avant : « Mettre de
# côté sans argent : vous, avec le nom et le numéro. Argent, remboursement,
# exception : la gérante. »
REGLE_RELAIS = ("Qui décide ? S'il y a de l'argent, un remboursement, une plainte ou une exception, "
                "c'est la gérante. Une mise de côté sans argent, c'est vous : prenez le nom et le numéro.")

# (id, la phrase à dire, quand s'en servir)
PHRASES = [
    ("accueil", "Bonjour ! Je peux vous aider ?",
     "Quand un client entre. Une fois, pas trois."),
    ("porte", "Je suis là si vous avez besoin.",
     "Quand le client dit « je regarde ». Vous le laissez, il revient."),
    ("preciser", "Quelle couleur ? … Et quelle taille ?",
     "Une question à la fois. Le client sait quoi répondre."),
    ("redire", "Un manteau noir, en moyen. Je vais vérifier en arrière.",
     "Redire avant d'aller chercher : s'il y a une erreur, le client la corrige tout de suite."),
    ("repeter", "Un instant, s'il vous plaît. Pouvez-vous répéter plus lentement ?",
     "Quand ça va trop vite. Faire semblant de comprendre fait perdre la vente."),
    ("relais", "Un instant. Je vais chercher la gérante.",
     REGLE_RELAIS),
]
DEFI = ("Cette semaine, dites une fois « Je vais vérifier en arrière » au lieu de promettre.",)
