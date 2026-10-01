"""Les voix d'« Une semaine à Toronto » — qui parle, avec quelle voix Azure.

Choisies au cadrage du 1er octobre 2026 (toronto-etape0.html), confirmées par
Daniel (« tout garder ») : Clara dit les mots et les phrases modèles ; Liam et
Andrew sont les gens au comptoir ; Harper est la Torontoise qui revient ; cinq
accents de Toronto pour le palier « rapide, avec l'accent ».

(id) → (prénom, voix Azure, locale, genre, rôle)
"""

VOIX = {
    "clara": ("Clara", "en-CA-ClaraNeural", "en-CA", "f", "la voix des mots et des modèles"),
    "liam": ("Liam", "en-CA-LiamNeural", "en-CA", "m", "au comptoir, au palier normal"),
    "andrew": ("Andrew", "en-US-Andrew:DragonHDLatestNeural", "en-US", "m", "au comptoir, la deuxième voix d'homme"),
    "harper": ("Harper", "en-US-Harper:MAI-Voice-2.1", "en-US", "f", "la Torontoise qui revient"),
    "aarti": ("Aarti", "en-IN-Aarti:DragonHDLatestNeural", "en-IN", "f", "accent de l'Inde"),
    "arjun": ("Arjun", "en-IN-Arjun:DragonHDLatestNeural", "en-IN", "m", "accent de l'Inde"),
    "rosa": ("Rosa", "en-PH-RosaNeural", "en-PH", "f", "accent des Philippines"),
    "sam": ("Sam", "en-HK-SamNeural", "en-HK", "m", "accent de Hong Kong"),
    "ezinne": ("Ezinne", "en-NG-EzinneNeural", "en-NG", "f", "accent du Nigeria"),
}
NARRATRICE = "clara"
ACCENTS = ["aarti", "arjun", "rosa", "sam", "ezinne"]
