"""Les textes de l'écran, dans les trois langues de l'interface.

L'employé lit l'écran dans la langue qu'il PARLE ; ce qu'il entend et les
mots qu'il apprend sont dans la langue qu'il APPREND. Ces textes-ci sont donc
écrits trois fois — à la main, relus par un locuteur avant la vente.
"""

HOTEL = "Hôtel Rive-Claire"   # décision du 25 sept. 2026 (recommandation acceptée)

NOM_LANGUE = {  # comment chaque interface nomme chaque langue
    "fr": {"fr": "français", "en": "anglais", "es": "espagnol"},
    "en": {"fr": "French", "en": "English", "es": "Spanish"},
    "es": {"fr": "francés", "en": "inglés", "es": "español"},
}
# Le descripteur de la marque suit la langue apprise (décision du 24 sept.).
DESCRIPTEUR = {
    "fr": {"fr": "Aide à l'apprentissage du français", "en": "Aide à l'apprentissage de l'anglais",
           "es": "Aide à l'apprentissage de l'espagnol"},
    "en": {"fr": "Helping you learn French", "en": "Helping you learn English",
           "es": "Helping you learn Spanish"},
    "es": {"fr": "Apoyo para aprender francés", "en": "Apoyo para aprender inglés",
           "es": "Apoyo para aprender español"},
}

UI = {
    "surtitre": {"fr": "Formation en milieu de travail", "en": "Workplace training", "es": "Formación en el trabajo"},
    "secteur": {"fr": "Hôtellerie · Réception", "en": "Hospitality · Front desk", "es": "Hotelería · Recepción"},
    "secteur_court": {"fr": "Réception d'hôtel", "en": "Hotel front desk", "es": "Recepción de hotel"},
    "je_parle": {"fr": "Je parle", "en": "I speak", "es": "Hablo"},
    "j_apprends": {"fr": "J'apprends", "en": "I'm learning", "es": "Aprendo"},
    "commencer": {"fr": "Commencer", "en": "Start", "es": "Empezar"},
    "bienvenue_tit": {"fr": "Bienvenue à la réception", "en": "Welcome to the front desk", "es": "Bienvenido a la recepción"},
    "intro": {
        "fr": "Les mots du comptoir, en images. Touchez un mot pour l'entendre ; votre langue reste cachée tant que vous ne la demandez pas.",
        "en": "The words of the front desk, in pictures. Tap a word to hear it; your own language stays hidden until you ask for it.",
        "es": "Las palabras del mostrador, en imágenes. Toque una palabra para escucharla; su idioma queda oculto hasta que lo pida."},
    "comptoir_tit": {"fr": "Le comptoir", "en": "The front desk", "es": "El mostrador"},
    "comptoir_sous": {
        "fr": "Votre poste, vu de votre place. Touchez chaque objet.",
        "en": "Your station, seen from where you stand. Tap each object.",
        "es": "Su puesto, visto desde su lugar. Toque cada objeto."},
    "les_planches": {"fr": "Les mots, par thème", "en": "Words by topic", "es": "Palabras por tema"},
    "mots": {"fr": "mots", "en": "words", "es": "palabras"},
    "retour": {"fr": "Retour", "en": "Back", "es": "Volver"},
    "ecouter": {"fr": "Écouter", "en": "Listen", "es": "Escuchar"},
    "voir": {"fr": "Voir dans ma langue", "en": "Show in my language", "es": "Ver en mi idioma"},
    "cacher": {"fr": "Cacher", "en": "Hide", "es": "Ocultar"},
    "piege": {"fr": "Piège", "en": "Trap", "es": "Trampa"},
    "changer": {"fr": "Changer de langue", "en": "Change language", "es": "Cambiar de idioma"},
    "touchez": {"fr": "Touchez un objet du comptoir.", "en": "Tap an object on the desk.", "es": "Toque un objeto del mostrador."},
    "liste_objets": {"fr": "Les objets du comptoir", "en": "Objects on the desk", "es": "Objetos del mostrador"},
    "non_relu": {
        "fr": "Version d'essai : l'anglais et l'espagnol n'ont pas encore été relus par un locuteur.",
        "en": "Trial version: English and Spanish have not yet been reviewed by a native speaker.",
        "es": "Versión de prueba: el inglés y el español aún no han sido revisados por un hablante nativo."},
}

PLANCHES = {
    "arrivee":   {"fr": "L'arrivée", "en": "Check-in", "es": "La llegada"},
    "chambre":   {"fr": "La chambre", "en": "The room", "es": "La habitación"},
    "services":  {"fr": "Les services", "en": "Services", "es": "Los servicios"},
    "paiement":  {"fr": "Le paiement", "en": "Payment", "es": "El pago"},
    "temps":     {"fr": "Les heures et les dates", "en": "Times and dates", "es": "Horas y fechas"},
    "problemes": {"fr": "Les problèmes", "en": "Problems", "es": "Los problemas"},
    "vacances":  {"fr": "Les vacances", "en": "Vacation", "es": "Las vacaciones"},
    "politesse": {"fr": "La politesse du comptoir", "en": "Desk courtesy", "es": "La cortesía del mostrador"},
    "comptoir":  {"fr": "Le comptoir", "en": "The front desk", "es": "El mostrador"},
}

# Les pièges, dans les deux langues de LEUR paire (la note française est au
# lexique). Une interface ne montre que les pièges de la paire choisie, donc
# chacun n'a besoin que des deux langues qui le voient.
PIEGES = {
    # fr·en — la note anglaise
    "lit-double":    {"en": "TRAP: « une chambre double » is a room for two — not necessarily a full bed. Ask: « un lit double ou deux lits? »"},
    "etage":         {"en": "TRAP: « le premier étage » can mean the ground floor (Québec) or the floor above it (France). « Le rez-de-chaussée » is always the ground floor."},
    "dejeuner":      {"en": "TRAP: in Québec, « le déjeuner » is BREAKFAST. Lunch is « le dîner »; dinner is « le souper »."},
    "souper":        {"en": "TRAP: « le souper » is the evening meal. In Québec, « le dîner » is lunch."},
    "depot":         {"en": "TRAP: French « une caution » is a security deposit, not caution (« la prudence »)."},
    "date":          {"en": "TRAP: 04/05 is May 4 in Québec (day first), not April 5. Say the month in words."},
    "location-auto": {"en": "TRAP: French « la location » means RENTAL. A place is « un endroit »."},
    "billet":        {"en": "TRAP: « un billet » is a ticket (or a banknote). A bill to pay is « la facture »."},
    # fr·es — la nota en español
    "stylo":      {"es": "TRAMPA: en francés el bolígrafo es « un stylo ». « Une plume » es una pluma de ave."},
    "prenom":     {"es": "TRAMPA: en francés « le nom » es el APELLIDO. El nombre de pila es « le prénom »."},
    "serviettes": {"es": "TRAMPA: « des serviettes » son TOALLAS. La servilleta de mesa es « une serviette de table »."},
    "diner":      {"es": "TRAMPA: en Quebec « le dîner » es la comida del mediodía, y « le déjeuner » es el desayuno."},
    "frais":      {"es": "TRAMPA: un cargo en la cuenta se dice « des frais ». « Un cargo » en francés es un barco de carga."},
    "facture":    {"es": "TRAMPA: « la facture » es la cuenta del hotel. En México « la factura » es el comprobante fiscal con RFC: no es lo mismo."},
    "autobus":    {"es": "TRAMPA: el camión de pasajeros es « l'autobus ». « Un camion » en francés es un camión de carga."},
    "tout-droit": {"es": "TRAMPA: « tout droit » es derecho, de frente; « à droite » es a la derecha."},
    # es·en — les deux
    "sortie":     {"es": "TRAMPA: « exit » es la salida; « éxito » en inglés es « success ».",
                   "en": "TRAP: Spanish « éxito » means success, not exit. Exit is « la salida »."},
    "maintenant": {"es": "TRAMPA: « actually » significa « en realidad », no « actualmente » (= « right now »).",
                   "en": "TRAP: Spanish « actualmente » means right now, not « actually » (= « en realidad »)."},
    "malade":     {"es": "TRAMPA: « constipated » significa estreñido. Un resfriado es « a cold ».",
                   "en": "TRAP: Spanish « estoy constipado » means I have a cold, not constipated."},
    "embarrasse": {"es": "TRAMPA: « embarrassed » es « me da pena ». « Embarazada » es « pregnant ».",
                   "en": "TRAP: Spanish « embarazada » means pregnant. Embarrassed is « me da pena »."},
    "dossier":    {"es": "TRAMPA: « carpet » es una alfombra. Una carpeta es « a folder ».",
                   "en": "TRAP: Spanish « carpeta » is a folder; a carpet is « una alfombra »."},
}
