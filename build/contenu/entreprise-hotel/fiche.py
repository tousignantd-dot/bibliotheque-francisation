"""La fiche de poche de la réception — ses textes (étape 6).

Lue par build/hotel_fiche.py. Le reste de la fiche vient d'ailleurs, rien n'est
recopié : les six phrases et leurs noms de `clients.GESTES`, la règle du relais
d'`exercices.REGLE_RELAIS`, les pièges du `lexique` (notes par paire via
`hotel_planches.donnees()`), l'alphabet d'`exercices.LETTRES`.

Les lettres de l'anglais n'ont pas de graphie parlée dans exercices.LETTRES (la
voix les dit d'elle-même) : leurs noms usuels sont ici, pour la fiche seulement.
"""


def R(fr, en, es):
    return {"fr": fr, "en": en, "es": es}


NOMS_LETTRES_EN = {
    "A": "ay", "B": "bee", "C": "see", "D": "dee", "E": "ee", "F": "ef", "G": "jee", "H": "aitch",
    "I": "eye", "J": "jay", "K": "kay", "L": "el", "M": "em", "N": "en", "O": "oh", "P": "pee",
    "Q": "cue", "R": "ar", "S": "ess", "T": "tee", "U": "you", "V": "vee", "W": "double-u", "X": "ex",
    "Y": "why", "Z": "zee",
}

UI = {
    "titre": R("Au comptoir : les phrases du réceptionniste", "At the desk: the receptionist's phrases",
               "En el mostrador: las frases del recepcionista"),
    "apprend": R("J'apprends {l}", "I'm learning {l}", "Aprendo {l}"),
    "langues": {"fr": R("le français", "French", "francés"), "en": R("l'anglais", "English", "inglés"),
                "es": R("l'espagnol", "Spanish", "español")},
    "six": R("Six phrases, dans l'ordre d'un accueil", "Six phrases, in the order of a check-in",
             "Seis frases, en el orden de una llegada"),
    "regle": R("La règle du comptoir", "The desk rule", "La regla del mostrador"),
    "eliminatoire": R("Une promesse hors règle fait échouer.", "A promise outside the rule is a fail.",
                      "Una promesa fuera de la regla es un fallo."),
    "pieges": R("Les mots qui piègent", "Words that trick you", "Palabras que engañan"),
    "alphabet": R("Épeler : l'alphabet", "Spelling: the alphabet", "Deletrear: el alfabeto"),
    "signes": R("Pour dire l'écriture", "Saying how it's written", "Para decir cómo se escribe"),
    "defi": R("Cette semaine : faites épeler trois noms au téléphone, et redites-les avant de raccrocher.",
              "This week: have three callers spell their names, and repeat them back before you hang up.",
              "Esta semana: pida a tres personas que deletreen su nombre por teléfono, y repítalo antes de colgar."),
    "fait": R("Je l'ai fait", "Done", "Lo hice"),
    "vu": R("Vu par le formateur", "Seen by the trainer", "Visto por el formador"),
    "date": R("Date", "Date", "Fecha"),
    "note": R("Les phrases se disent en {l} ; votre langue, dessous, aide à comprendre.",
              "Say the phrases in {l}; your language, underneath, helps you understand.",
              "Las frases se dicen en {l}; su idioma, debajo, ayuda a entender."),
    "non_relu": R("L'anglais et l'espagnol n'ont pas encore été relus par un locuteur.",
                  "The English and Spanish have not yet been checked by a native speaker.",
                  "El inglés y el español aún no han sido revisados por un hablante nativo."),
    "pied": R("francis — formation au poste", "francis — on-the-job training", "francis — formación en el puesto"),
}
