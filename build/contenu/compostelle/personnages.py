"""Les gens du chemin — qui parle, avec quelle voix.

(id, nom, qui, où, genre, voix Azure, débit, portrait)

LES VOIX : l'Espagne n'a que deux voix HD (Ximena, Tristan) ; les autres sont
des voix neurales, déterministes. Marta, la compagne de route, parle avec la
voix MAI-Voice-2 d'Espagne qui porte des INTENTIONS (friendlycheerful,
caringempathy, reflective, nostalgic…) : l'émotion appartient à la RÉPLIQUE,
jamais au personnage (mémoire voix-emotives-azure-mai) — elle se déclare donc
réplique par réplique, dans etapes.py.

LE DÉBIT suit le rôle, pas le niveau : don Fermín, le vieil homme du village,
parle vite (c'est l'exercice) ; Marta ralentit pour vous (elle le dit).

`narratrice` dit les mots, les phrases à imiter et vos répliques modèles.
"""

PERSONNAGES = {
    "narratrice": ("Ximena", "la voix des mots", "", "f", "es-ES-Ximena:DragonHDLatestNeural", "-10%", ""),
    "marta": ("Marta", "pèlerine de Valladolid, 58 ans, professeure de musique à la retraite", "sur le chemin", "f",
              "es-ES-Marta:MAI-Voice-2", "-8%", "marta"),
    "javier": ("Javier", "hospitalier bénévole", "Roncesvalles", "m", "es-ES-Tristan:DragonHDLatestNeural", "+0%", "javier"),
    "ainhoa": ("Ainhoa", "serveuse au comptoir d'un bar", "Pamplona", "f", "es-ES-ElviraNeural", "+5%", "ainhoa"),
    "fermin": ("Don Fermín", "vieil homme du village", "Puente la Reina", "m", "es-ES-AlvaroNeural", "+12%", "fermin"),
    "pilar": ("Pilar", "pharmacienne", "Logroño", "f", "es-ES-IreneNeural", "+0%", "pilar"),
    "rocio": ("Rocío", "hospitalière de l'albergue municipal", "Burgos", "f", "es-ES-AbrilNeural", "+5%", "rocio"),
    "gomez": ("Señor Gómez", "patron d'une pension, au téléphone", "Burgos", "m", "es-ES-DarioNeural", "+5%", ""),
    "alex": ("Álex", "serveur de restaurant", "León", "m", "es-ES-TeoNeural", "+5%", "alex"),
    "uxia": ("Uxía", "hospitalière galicienne", "O Cebreiro", "f", "es-ES-EstrellaNeural", "+0%", "uxia"),
    "manolo": ("Manolo", "épicier", "Sarria", "m", "es-ES-SaulNeural", "+8%", "manolo"),
    "carmen": ("Carmen", "employée du bureau du pèlerin", "Santiago", "f", "es-ES-VeraNeural", "+0%", "carmen"),
}

# Les portraits : un buste au trait, même registre que les vignettes d'étape.
PORTRAITS = {
    "marta": "a friendly Spanish woman of about 58 with short grey hair, a sun hat pushed back, a light "
             "hiking shirt and a small scallop shell hanging from her backpack strap, warm smile",
    "javier": "a Spanish man of about 45 with a short beard and glasses, a simple polo shirt, calm and "
              "welcoming expression, a volunteer at a pilgrims' hostel",
    "ainhoa": "a young Basque woman of about 28, dark hair in a ponytail, a black apron over a white shirt, "
              "a lively expression, a bar waitress",
    "fermin": "an old Spanish villager of about 80, flat cap (boina), weathered face, a cardigan, pointing "
              "with one hand to his right, kind but hurried expression",
    "pilar": "a Spanish pharmacist of about 50, short dark hair, a white coat, reading glasses on a cord, "
             "attentive expression",
    "rocio": "a Spanish woman of about 35, curly hair tied back, a fleece vest, a slightly apologetic smile, "
             "a hostel receptionist",
    "alex": "a Spanish waiter of about 30, short hair, a white shirt and black waistcoat, a notepad held "
            "at his chest (blank), friendly expression",
    "uxia": "a Galician woman of about 60, grey hair in a bun, a thick wool cardigan, rosy cheeks, "
            "a warm, motherly expression",
    "manolo": "a Spanish grocer of about 55, round face, moustache, a green apron, jovial expression",
    "carmen": "a Spanish office clerk of about 40, dark bob haircut, a lanyard with a blank badge, "
              "a professional but warm smile",
}
