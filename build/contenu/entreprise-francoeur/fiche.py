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
     "Un retour, une plainte, une promesse que vous ne pouvez pas faire : ce n'est pas un échec."),
]
DEFI = ("Cette semaine, dites une fois « Je vais vérifier en arrière » au lieu de promettre.",)
