"""Le test de positionnement de la réception (étape 3) — dans la langue APPRISE.

Il sert à UNE chose : régler le palier du jeu de rôle (étape 4). Ce n'est pas
un examen. Dix à douze minutes, repassé à la fin du parcours. Le test SITUE ;
il ne certifie pas les seuils du cadrage (7 sur 8, 5 de suite, 6 situations
sur 8), qui se vérifient au comptoir joué et au pilote — l'écran le dit.

QUATRE PARTIES, alignées sur le cadrage (build/contenu/entreprise-hotel/boucle/cadrage.md) :
  A · la demande (O1)      — ADAPTATIVE : le lit, puis le lit et les nuits, puis
                              des dates ou une phrase qui se reprend
  B · au téléphone (O2)    — TROIS SOUS-PARTIES passées par tous, sans arrêt
                              (audit du test, tour 1 : ce sont trois compétences,
                              pas trois crans) : numéros de chambre, prix et
                              heures, noms épelés tapés — trois items chacune
  C · qui décide? (O4)     — trois ACTES : je le fais moi-même, je transmets au
                              gérant sans rien promettre, je refuse poliment.
                              Accorder soi-même ce qui revient au gérant, ou ce
                              que personne ne peut accorder, fait échouer la
                              partie — et la règle entière est affichée AVANT
  D · répondre à voix haute (O3) — cinq gestes, dont confirmer ; enregistré sur
                              l'appareil (gardé jusqu'à la confirmation du
                              formateur), noté sur deux lignes : le geste et la langue

LA RÈGLE ADAPTATIVE (A seulement) : cran 1 au départ ; trois bonnes valident le
cran et font monter ; deux erreurs arrêtent ; quatre items par cran.

LES DISTRACTEURS NE SE DEVINENT PAS (audit du test, tour 1, bloquant) :
  - A : cartes en carré latin (lit, nuits) (lit, nuits′) (lit′, nuits)
    (lit′, nuits′), et nuits′ tantôt une de MOINS, tantôt une de PLUS ;
  - B : les choix se construisent autour d'un LEURRE — une vraie erreur
    d'oreille dans la langue apprise — et non autour de la bonne : le vote
    majoritaire, position par position, désigne le leurre. Le build le vérifie.

DES SITUATIONS NEUVES : ni les phrases, ni les situations de « Ce que je
réponds » (tour 1 : d1 reprenait r1 mot pour mot).

DEUX FORMES PARALLÈLES, nivelées (mêmes longueurs de noms, mêmes difficultés),
la première tirée AU HASARD (contrebalancement), l'autre à la passation suivante.
"""


def R(fr, en, es):
    return {"fr": fr, "en": en, "es": es}


LITS = ["lit-simple", "lit-double", "lit-queen", "lit-king"]
# Au cran 1, les cartes : la cible et trois autres de ce groupe — un seul lit
# « transparent » (queen, king) par forme (tour 1 : « queen » se comprend sans
# la langue).
LITS_C1 = ["lit-simple", "lit-double", "lit-appoint", "berceau"]

# ── A · la demande ───────────────────────────────────────────────────────
# (id, cran, {langue: phrase}, lit, nuits, lit′, nuits′)
A = {
    1: [
        ("a11", 1, R("Un lit simple, s'il vous plaît.", "A twin bed, please.", "Una cama individual, por favor."), "lit-simple", None, None, None),
        ("a12", 1, R("J'aurais besoin d'un lit d'appoint, s'il vous plaît.", "I'd need a rollaway bed, please.", "Necesitaría una cama extra, por favor."), "lit-appoint", None, None, None),
        ("a13", 1, R("Avez-vous une chambre avec un lit double?", "Do you have a room with a double bed?", "¿Tiene una habitación con cama matrimonial?"), "lit-double", None, None, None),
        ("a14", 1, R("Un lit queen, ce serait parfait.", "A queen bed would be perfect.", "Una cama queen sería perfecta."), "lit-queen", None, None, None),
        ("a21", 2, R("Bonsoir, un lit queen pour trois nuits.", "Evening! A queen bed for three nights.", "Buenas noches, cama queen para tres noches."), "lit-queen", 3, "lit-king", 2),
        ("a22", 2, R("C'est pour deux nuits, dans un lit simple.", "It's for two nights, in a twin bed.", "Es para dos noches, en cama individual."), "lit-simple", 2, "lit-double", 3),
        ("a23", 2, R("On reste quatre nuits; un lit king, si possible.", "We're staying four nights; a king bed if possible.", "Nos quedamos cuatro noches; cama king size, si se puede."), "lit-king", 4, "lit-simple", 3),
        ("a24", 2, R("Une nuit, un lit double, c'est tout.", "One night, a double bed, that's all.", "Una noche, cama matrimonial, nada más."), "lit-double", 1, "lit-queen", 2),
        ("a31", 3, R("J'arrive mardi, je repars jeudi matin. Un lit king.", "I'm arriving Tuesday and leaving Thursday morning. A king bed.", "Llego el martes y me voy el jueves en la mañana. Cama king size."), "lit-king", 2, "lit-queen", 1),
        ("a32", 3, R("Deux nuits… non, attendez, trois nuits. Avec un lit double.", "Two nights… no, wait, three nights. With a double bed.", "Dos noches… no, espere, tres noches. Con cama matrimonial."), "lit-double", 3, "lit-queen", 2),
        ("a33", 3, R("Du dix au quinze juillet, un lit queen.", "From July tenth to the fifteenth, a queen bed.", "Del diez al quince de julio, cama queen."), "lit-queen", 5, "lit-king", 6),
        ("a34", 3, R("Un lit double… en fait non, un lit simple : c'est juste pour moi, pour ce soir.", "A double bed… actually no, a twin: it's just me, for tonight.", "Una cama matrimonial… bueno no, individual: es solo para mí, esta noche."), "lit-simple", 1, "lit-double", 2),
    ],
    2: [
        ("a41", 1, R("Un lit double, s'il vous plaît.", "A double bed, please.", "Una cama matrimonial, por favor."), "lit-double", None, None, None),
        ("a42", 1, R("Avez-vous un lit de bébé pour la chambre?", "Do you have a crib for the room?", "¿Tiene una cuna para la habitación?"), "berceau", None, None, None),
        ("a43", 1, R("Avez-vous une chambre avec un lit simple?", "Do you have a room with a twin bed?", "¿Tiene una habitación con cama individual?"), "lit-simple", None, None, None),
        ("a44", 1, R("Un lit king, ce serait parfait.", "A king bed would be perfect.", "Una cama king size sería perfecta."), "lit-king", None, None, None),
        ("a51", 2, R("Bonsoir, un lit double pour deux nuits.", "Evening! A double bed for two nights.", "Buenas noches, cama matrimonial para dos noches."), "lit-double", 2, "lit-simple", 1),
        ("a52", 2, R("C'est pour trois nuits, dans un lit king.", "It's for three nights, in a king bed.", "Es para tres noches, en cama king size."), "lit-king", 3, "lit-queen", 4),
        ("a53", 2, R("On reste une nuit; un lit queen, si possible.", "We're staying one night; a queen bed if possible.", "Nos quedamos una noche; cama queen, si se puede."), "lit-queen", 1, "lit-double", 2),
        ("a54", 2, R("Quatre nuits, un lit simple, c'est tout.", "Four nights, a twin bed, that's all.", "Cuatro noches, cama individual, nada más."), "lit-simple", 4, "lit-king", 3),
        ("a61", 3, R("J'arrive mercredi, je repars samedi matin. Un lit queen.", "I'm arriving Wednesday and leaving Saturday morning. A queen bed.", "Llego el miércoles y me voy el sábado en la mañana. Cama queen."), "lit-queen", 3, "lit-king", 2),
        ("a62", 3, R("Trois nuits… non, attendez, deux nuits. Avec un lit simple.", "Three nights… no, wait, two nights. With a twin bed.", "Tres noches… no, espere, dos noches. Con cama individual."), "lit-simple", 2, "lit-double", 3),
        ("a63", 3, R("Du vingt au vingt-quatre août, un lit king.", "From August twentieth to the twenty-fourth, a king bed.", "Del veinte al veinticuatro de agosto, cama king size."), "lit-king", 4, "lit-queen", 5),
        ("a64", 3, R("Un lit king… en fait non, un lit double : c'est juste pour ce soir.", "A king bed… actually no, a double: it's just for tonight.", "Una cama king size… bueno no, matrimonial: es solo por esta noche."), "lit-double", 1, "lit-king", 2),
    ],
}

# ── B · au téléphone : trois sous-parties ────────────────────────────────
# Choix à cocher : (id, sous-partie, {langue: phrase}, bonne, {langue: leurre}).
# Le leurre est une VRAIE erreur d'oreille dans la langue apprise ; les deux
# autres choix se fabriquent autour de lui (choix_b), si bien que le vote
# majoritaire désigne le leurre, jamais la bonne.
B = {
    1: [
        ("b11", "numero", R("Vous êtes à la chambre deux cent quatorze.", "You're in room two-fourteen.", "Está en la habitación doscientos catorce."),
         "214", R("204", "240", "204")),
        ("b12", "numero", R("C'est la chambre cinq cent sept.", "It's room five-oh-seven.", "Es la habitación quinientos siete."),
         "507", R("517", "517", "517")),
        ("b13", "numero", R("Votre chambre, c'est la trois cent dix-huit.", "Your room is three-eighteen.", "Su habitación es la trescientos dieciocho."),
         "318", R("308", "380", "308")),
        ("b21", "prix", R("Le total est de deux cent trente-neuf dollars.", "Your total is two hundred thirty-nine dollars.", "El total es de doscientos treinta y nueve dólares."),
         "239 $", R("229 $", "229 $", "229 $")),
        ("b22", "prix", R("La navette part à dix-sept heures quinze.", "The shuttle leaves at five fifteen p.m.", "La camioneta sale a las cinco y cuarto de la tarde."),
         "17:15", R("07:15", "17:50", "05:15")),
        ("b23", "prix", R("Ça fait cent soixante-quinze dollars quarante.", "That's one seventy-five forty.", "Son ciento setenta y cinco dólares con cuarenta."),
         "175,40 $", R("175,14 $", "175,14 $", "175,14 $")),
        ("b31", "nom", "PATEL"),
        ("b32", "nom", "BARRETT"),
        ("b33", "nom", "RODRÍGUEZ"),
    ],
    2: [
        ("b41", "numero", R("Vous êtes à la chambre deux cent seize.", "You're in room two-sixteen.", "Está en la habitación doscientos dieciséis."),
         "216", R("206", "260", "206")),
        ("b42", "numero", R("C'est la chambre quatre cent neuf.", "It's room four-oh-nine.", "Es la habitación cuatrocientos nueve."),
         "409", R("419", "419", "419")),
        ("b43", "numero", R("Votre chambre, c'est la sept cent quinze.", "Your room is seven-fifteen.", "Su habitación es la setecientos quince."),
         "715", R("705", "750", "705")),
        ("b51", "prix", R("Le total est de trois cent quarante-huit dollars.", "Your total is three hundred forty-eight dollars.", "El total es de trescientos cuarenta y ocho dólares."),
         "348 $", R("338 $", "338 $", "338 $")),
        ("b52", "prix", R("Le souper est servi à dix-huit heures quarante-cinq.", "Dinner is served at six forty-five p.m.", "La cena se sirve a un cuarto para las siete de la tarde."),
         "18:45", R("08:45", "06:45", "19:15")),
        ("b53", "prix", R("Ça fait cent vingt-six dollars soixante.", "That's one twenty-six sixty.", "Son ciento veintiséis dólares con sesenta."),
         "126,60 $", R("116,60 $", "126,16 $", "116,60 $")),
        ("b61", "nom", "MEHTA"),
        ("b62", "nom", "BENNETT"),
        ("b63", "nom", "HERNÁNDEZ"),
    ],
}
SOUS_B = ["numero", "prix", "nom"]


def choix_b(bonne, leurre, ident):
    """Quatre choix : la bonne, le leurre, et deux variantes DU LEURRE qui
    changent chacune un chiffre là où la bonne ne diffère pas du leurre. Le
    leurre est le centre : c'est lui que désigne le vote majoritaire. Tirage
    déterministe (sur l'identifiant), pour que les formes restent fixes ; une
    heure produite doit rester une heure (HH < 24, MM < 60)."""
    import random
    rnd = random.Random(ident)
    pos_b = [k for k, (x, y) in enumerate(zip(bonne, leurre)) if x != y]
    chiffres = [k for k, c in enumerate(leurre) if c.isdigit() and k not in pos_b]

    def valide(v):
        if ":" in v:
            h, m = v.split(":")
            return int(h) < 24 and int(m) < 60
        return not v.startswith("0")

    out, essais = [], 0
    while len(out) < 2 and essais < 500:
        essais += 1
        k = rnd.choice(chiffres)
        v = list(leurre)
        v[k] = rnd.choice([d for d in "0123456789" if d != leurre[k]])
        v = "".join(v)
        if v not in out and v not in (bonne, leurre) and valide(v):
            out.append(v)
    return [bonne, leurre] + out


def vote_majoritaire(choix):
    """La chaîne qu'on obtient en gardant, position par position, le caractère
    le plus fréquent — la ruse que l'audit a jouée (16 sur 16)."""
    from collections import Counter
    L = max(len(c) for c in choix)
    return "".join(Counter(c[k] for c in choix if k < len(c)).most_common(1)[0][0] for k in range(L))


# ── C · qui décide? ──────────────────────────────────────────────────────
# (id, {interface: contexte} ou None, {langue: demande}, réponse juste). Les
# réponses « moi » sont de VRAIES décisions de l'employé ; deux « personne »
# par forme.
CHOIX_C = {
    "moi": R("Je le fais moi-même", "I do it myself", "Lo hago yo mismo"),
    "gerant": R("Je transmets au gérant, sans rien promettre", "I pass it to the manager, promising nothing", "Se lo paso al gerente, sin prometer nada"),
    "personne": R("Je refuse poliment : personne ne peut l'accorder", "I decline politely: no one can grant that", "Me niego con cortesía: nadie puede concederlo"),
}
C = {
    1: [
        ("c1", None, R("Pouvez-vous m'expliquer les dix dollars de wifi sur ma facture?", "Can you explain the ten dollars for Wi-Fi on my bill?", "¿Me puede explicar los diez dólares de wifi en mi cuenta?"), "moi"),
        ("c2", None, R("Mon souper au restaurant de l'hôtel était froid; je veux être remboursé.", "My dinner at the hotel restaurant was cold; I want a refund.", "Mi cena en el restaurante del hotel estaba fría; quiero un reembolso."), "gerant"),
        ("c3", None, R("La réservation est au nom de mon mari, Tanguay. Pouvez-vous la trouver?", "The reservation is under my husband's name, Tanguay. Can you find it?", "La reservación está a nombre de mi esposo, Tanguay. ¿La puede encontrar?"), "moi"),
        ("c4", None, R("On arrive à huit heures du matin. La chambre peut-elle être prête sans frais?", "We're arriving at eight a.m. Can the room be ready at no charge?", "Llegamos a las ocho de la mañana. ¿Puede estar lista la habitación sin costo?"), "gerant"),
        ("c5", None, R("Faites-moi une facture au nom de ma compagnie, mais avec une autre date.", "Make me a receipt in my company's name, but with a different date.", "Hágame una factura a nombre de mi empresa, pero con otra fecha."), "personne"),
        ("c6", R("L'hôtel est entièrement non-fumeur.", "The whole hotel is non-smoking.", "Todo el hotel es de no fumar."),
         R("Je voudrais une chambre où je peux fumer.", "I'd like a room where I can smoke.", "Quisiera una habitación donde se pueda fumar."), "personne"),
    ],
    2: [
        ("c7", None, R("Pouvez-vous m'expliquer les vingt dollars pour le chien?", "Can you explain the twenty dollars for the dog?", "¿Me puede explicar los veinte dólares por el perro?"), "moi"),
        ("c8", None, R("Le lit d'appoint était brisé; je ne veux pas le payer.", "The rollaway bed was broken; I don't want to pay for it.", "La cama extra estaba rota; no la quiero pagar."), "gerant"),
        ("c9", None, R("Je voudrais changer pour une chambre à deux lits. Il vous en reste?", "I'd like to switch to a room with two beds. Do you have any left?", "Quisiera cambiarme a una habitación con dos camas. ¿Le quedan?"), "moi"),
        ("c10", None, R("On part un jour plus tôt. Pouvez-vous rembourser la dernière nuit?", "We're leaving a day early. Can you refund the last night?", "Nos vamos un día antes. ¿Me puede reembolsar la última noche?"), "gerant"),
        ("c11", None, R("Pouvez-vous écrire sur la facture que j'ai payé comptant? J'ai payé par carte.", "Can you write on the bill that I paid cash? I paid by card.", "¿Puede poner en la cuenta que pagué en efectivo? Pagué con tarjeta."), "personne"),
        ("c12", R("Le stationnement est complet ce soir.", "The parking lot is full tonight.", "El estacionamiento está lleno esta noche."),
         R("Réservez-moi une place de stationnement quand même.", "Book me a parking spot anyway.", "Apárteme un lugar de estacionamiento de todos modos."), "personne"),
    ],
}

# ── D · répondre à voix haute : cinq gestes ──────────────────────────────
# (id, {interface: contexte} ou None, {apprise: phrase du client}, geste,
# {apprise: exemple de réponse}). L'exemple ne s'affiche qu'au formateur, et
# n'est la réplique d'aucun exercice.
GESTES = {
    "epeler": R("Accueillir et faire épeler le nom", "Greet and have the name spelled", "Recibir y pedir que deletree el apellido"),
    "refuser": R("Refuser poliment et proposer une solution", "Decline politely and offer a solution", "Rechazar con cortesía y ofrecer una solución"),
    "frais": R("Expliquer les frais", "Explain the charge", "Explicar el cargo"),
    "relais": R("Passer le relais au gérant, sans promettre", "Hand it to the manager, without promising", "Pasarlo al gerente, sin prometer"),
    "confirmer": R("Confirmer en redisant la demande", "Confirm by restating the request", "Confirmar repitiendo la solicitud"),
}
D = {
    1: [
        ("d1", None, R("Bonsoir, j'ai une réservation; c'est Ouellette.", "Good evening, I have a reservation; it's Ouellette.", "Buenas noches, tengo una reservación; es Ouellette."), "epeler",
         R("Bonsoir! Pouvez-vous me l'épeler, s'il vous plaît?", "Good evening! Could you spell that for me, please?", "¡Buenas noches! ¿Me lo puede deletrear, por favor?")),
        ("d2", R("La navette va seulement à l'aéroport.", "The shuttle only goes to the airport.", "La camioneta solo va al aeropuerto."),
         R("Est-ce que la navette peut nous amener au centre-ville?", "Can the shuttle take us downtown?", "¿La camioneta nos puede llevar al centro?"), "refuser",
         R("Désolé, la navette va seulement à l'aéroport. Je peux vous appeler un taxi.", "Sorry, the shuttle only goes to the airport. I can call you a cab.", "Lo siento, la camioneta solo va al aeropuerto. Le puedo llamar un taxi.")),
        ("d3", R("Lit d'appoint : 15 $ par nuit, pendant deux nuits.", "Rollaway bed: $15 a night, for two nights.", "Cama extra: 15 dólares por noche, por dos noches."),
         R("C'est quoi, ces trente dollars?", "What's this thirty dollars?", "¿Qué son estos treinta dólares?"), "frais",
         R("C'est le lit d'appoint : quinze dollars par nuit, pour deux nuits.", "That's the rollaway bed: fifteen dollars a night, for two nights.", "Es la cama extra: quince dólares por noche, por dos noches.")),
        ("d4", None, R("Le déjeuner était froid; je veux être remboursé.", "Breakfast was cold; I want my money back.", "El desayuno estaba frío; quiero que me devuelvan el dinero."), "relais",
         R("Désolé pour le déjeuner. Je ne peux pas décider d'un remboursement : j'en parle au gérant.", "Sorry about breakfast. I can't decide on a refund: I'll talk to the manager.", "Lamento lo del desayuno. No puedo decidir un reembolso: lo hablo con el gerente.")),
        ("d5", None, R("Je voudrais une chambre pour trois nuits, à partir de jeudi.", "I'd like a room for three nights, starting Thursday.", "Quisiera una habitación por tres noches, a partir del jueves."), "confirmer",
         R("Trois nuits, du jeudi au dimanche : c'est bien ça?", "Three nights, Thursday to Sunday: is that right?", "Tres noches, del jueves al domingo: ¿es correcto?")),
    ],
    2: [
        ("d6", None, R("Bonjour, c'est au nom de Nkemelu.", "Hello, it's under Nkemelu.", "Buenos días, está a nombre de Nkemelu."), "epeler",
         R("Bonjour! Pouvez-vous m'épeler le nom, s'il vous plaît?", "Hello! Could you spell the name for me, please?", "¡Buenos días! ¿Me deletrea el apellido, por favor?")),
        ("d7", R("L'hôtel est entièrement non-fumeur.", "The whole hotel is non-smoking.", "Todo el hotel es de no fumar."),
         R("On peut fumer sur le balcon de la chambre?", "Can we smoke on the room's balcony?", "¿Se puede fumar en el balcón de la habitación?"), "refuser",
         R("Désolé, tout l'hôtel est non-fumeur, balcons compris. Il y a un espace à l'extérieur.", "Sorry, the whole hotel is non-smoking, balconies included. There's an area outside.", "Lo siento, todo el hotel es de no fumar, balcones incluidos. Hay un área afuera.")),
        ("d8", R("Coffre-fort : 5 $ par nuit, pendant quatre nuits.", "In-room safe: $5 a night, for four nights.", "Caja fuerte: 5 dólares por noche, por cuatro noches."),
         R("C'est quoi, ces vingt dollars?", "What's this twenty dollars?", "¿Qué son estos veinte dólares?"), "frais",
         R("C'est le coffre-fort : cinq dollars par nuit, pour quatre nuits.", "That's the safe: five dollars a night, for four nights.", "Es la caja fuerte: cinco dólares por noche, por cuatro noches.")),
        ("d9", None, R("On part un jour plus tôt; remboursez-moi la dernière nuit.", "We're leaving a day early; refund me the last night.", "Nos vamos un día antes; devuélvame la última noche."), "relais",
         R("Je comprends. Je ne peux pas le décider moi-même; je transmets votre demande au gérant.", "I understand. I can't decide that myself; I'll pass your request to the manager.", "Entiendo. No puedo decidirlo yo; le paso su solicitud al gerente.")),
        ("d10", None, R("Deux personnes, deux nuits, à partir du douze.", "Two people, two nights, starting on the twelfth.", "Dos personas, dos noches, a partir del doce."), "confirmer",
         R("Deux personnes, deux nuits, du 12 au 14 : c'est exact?", "Two people, two nights, the 12th to the 14th: is that correct?", "Dos personas, dos noches, del 12 al 14: ¿es correcto?")),
    ],
}

# La grille du formateur, sur DEUX lignes par item (tour 1 : trois cases sans
# critère de langue). Un geste « autre, acceptable » compte comme fait.
ORAL_GESTE = R("Geste fait|Autre geste acceptable|Promesse|Rien",
               "Gesture done|Other acceptable gesture|Promise|Nothing",
               "Gesto hecho|Otro gesto aceptable|Promesa|Nada")
ORAL_LANGUE = R("Formule attendue|Compréhensible|Incompréhensible",
                "Expected phrasing|Understandable|Not understandable",
                "Fórmula esperada|Comprensible|Incomprensible")
CODE_FORMATEUR = "2413"

# ── Le palier, en données, appliqué une seule fois ───────────────────────
#   s = A (0-3) + B (sous-parties réussies, 2 sur 3 ou mieux : 0-3)
#   s <= DEBUTANT_MAX ou A == 0                                → débutant
#   s >= AISE_MIN et C réussie et (oral pas noté, ou ≥ ORAL_AISE gestes faits
#                                   sans promesse)             → à l'aise
#   sinon                                                       → fonctionnel
# Le formateur note l'oral ; le palier se recalcule sous ses yeux.
DEBUTANT_MAX, AISE_MIN, ORAL_AISE = 2, 5, 3
C_SEUIL = 5
PALIERS = ["debutant", "fonctionnel", "aise"]
# Les seuils du cadrage, CITÉS à l'écran : le test ne les mesure pas.
CADRAGE = R("Le test situe le niveau ; il ne vérifie pas les seuils du cadrage (7 demandes sur 8, 5 noms de suite, "
            "6 situations sur 8), qui se vérifient au comptoir joué.",
            "The test places your level; it doesn't check the course targets (7 requests out of 8, 5 names in a row, "
            "6 situations out of 8), which are checked in the desk role-play.",
            "La prueba ubica su nivel; no verifica las metas del curso (7 solicitudes de 8, 5 apellidos seguidos, "
            "6 situaciones de 8), que se verifican en el mostrador simulado.")

# ── Les textes de l'écran du test, trois fois ────────────────────────────
UI = {
    "test_tit": R("Le test de positionnement", "The placement test", "La prueba de ubicación"),
    "test_carte": R("10 à 12 minutes, pour régler le niveau des clients au comptoir.",
                    "10 to 12 minutes, to set the level of the guests at the desk.",
                    "De 10 a 12 minutos, para ajustar el nivel de los clientes en el mostrador."),
    "test_intro": R("Quatre parties, dans la langue que vous apprenez. Il n'y a ni vert ni rouge : ce n'est pas un examen. "
                    "Les questions s'ajustent : si c'est trop difficile, la partie s'arrête d'elle-même.",
                    "Four parts, in the language you're learning. There's no green or red: it's not an exam. "
                    "The questions adjust: if it gets too hard, the part stops by itself.",
                    "Cuatro partes, en el idioma que aprende. No hay verde ni rojo: no es un examen. "
                    "Las preguntas se ajustan: si es demasiado difícil, la parte se detiene sola."),
    "regle_c": R("À savoir avant de commencer : dans la partie C, accorder vous-même ce qui revient au gérant, "
                 "ou ce que personne ne peut accorder, fait échouer la partie — comme au comptoir.",
                 "Know this before you start: in part C, granting yourself what belongs to the manager, "
                 "or what no one can grant, fails the part — just like at the desk.",
                 "Antes de empezar: en la parte C, conceder usted mismo lo que le toca al gerente, "
                 "o lo que nadie puede conceder, hace fallar la parte, como en el mostrador."),
    "passation": R("Passation", "Attempt", "Intento"),
    "forme": R("forme", "form", "forma"),
    "commencer_test": R("Commencer le test", "Start the test", "Empezar la prueba"),
    "partie": R("Partie", "Part", "Parte"),
    "pA": R("Ce que le client demande", "What the guest asks for", "Lo que pide el cliente"),
    "pA_c": R("Écoutez le client. Touchez la chambre qu'il demande.", "Listen to the guest. Tap the room they ask for.", "Escuche al cliente. Toque la habitación que pide."),
    "pB": R("Au téléphone", "On the phone", "Por teléfono"),
    "pB_c": R("Écoutez, puis touchez ce que vous devez noter. On note l'heure sur 24 heures (17:15) et le prix avec une virgule (175,40 $).",
              "Listen, then tap what you need to write down. Times go on the 24-hour clock (17:15), prices with a comma (175,40 $).",
              "Escuche y toque lo que debe anotar. La hora se anota en 24 horas (17:15) y el precio con coma (175,40 $)."),
    "b_numero": R("Numéros de chambre", "Room numbers", "Números de habitación"),
    "b_prix": R("Prix et heures", "Prices and times", "Precios y horas"),
    "b_nom": R("Noms épelés", "Spelled names", "Apellidos deletreados"),
    "une_reecoute": R("Une seule réécoute, comme au comptoir.", "Only one replay, like at the desk.", "Solo se puede volver a escuchar una vez, como en el mostrador."),
    "bonnes": R("bonnes sur", "right out of", "correctas de"),
    "c_vise": R("visé : 5, sans promesse", "target: 5, with no promise", "meta: 5, sin promesas"),
    "ligne_geste": R("Le geste", "The gesture", "El gesto"),
    "ligne_langue": R("La langue", "The language", "El idioma"),
    "palier_oral": R("Le niveau tient compte de l'oral dès que le formateur l'a noté.", "The level includes the oral part once the trainer has rated it.", "El nivel toma en cuenta la parte oral en cuanto el formador la califica."),
    "reprise": R("Résultats de la dernière passation, pas encore confirmés par le formateur.", "Results of the last attempt, not yet confirmed by the trainer.", "Resultados del último intento, aún sin confirmar por el formador."),
    "pB_nom": R("Le client épelle son nom. Tapez-le.", "The guest spells their name. Type it.", "El cliente deletrea su apellido. Escríbalo."),
    "pC": R("Qui décide?", "Who decides?", "¿Quién decide?"),
    "pC_c": R("Écoutez le client. Que faites-vous?", "Listen to the guest. What do you do?", "Escuche al cliente. ¿Qué hace?"),
    "pD": R("Répondre à voix haute", "Answer out loud", "Responder en voz alta"),
    "pD_c": R("Écoutez le client, puis enregistrez votre réponse. Elle reste sur cet appareil : votre formateur l'écoutera.",
              "Listen to the guest, then record your answer. It stays on this device: your trainer will listen to it.",
              "Escuche al cliente y grabe su respuesta. Se queda en este aparato: su formador la escuchará."),
    "enregistrer": R("Enregistrer", "Record", "Grabar"),
    "arreter": R("Arrêter", "Stop", "Detener"),
    "reecouter_moi": R("Réécouter ma réponse", "Play my answer", "Escuchar mi respuesta"),
    "sans_micro": R("Pas de micro sur cet appareil : répondez à voix haute à votre formateur, puis passez à la suite.",
                    "No microphone on this device: answer out loud to your trainer, then go on.",
                    "No hay micrófono en este aparato: responda en voz alta a su formador y siga."),
    "valider": R("Valider", "Confirm", "Confirmar"),
    "suivant": R("Suivant", "Next", "Siguiente"),
    "nuits": R("nuit|nuits", "night|nights", "noche|noches"),
    "fini_tit": R("Le test est terminé", "The test is done", "La prueba terminó"),
    "fini_c": R("Montrez cet écran à votre formateur. Ne le quittez pas avant qu'il ait écouté vos réponses.",
                "Show this screen to your trainer. Don't leave it before they have listened to your answers.",
                "Muestre esta pantalla a su formador. No la cierre antes de que escuche sus respuestas."),
    "niveau": R("niveau", "level", "nivel"),
    "atteint": R("objectif atteint", "goal reached", "objetivo alcanzado"),
    "pas_encore": R("pas encore", "not yet", "todavía no"),
    "visé": R("visé", "target", "meta"),
    "promesse_c": R("Une demande qui revient au gérant a été prise en charge : la partie C échoue.",
                    "A request that belongs to the manager was handled alone: part C fails.",
                    "Se atendió solo una solicitud que le toca al gerente: la parte C falla."),
    "palier_propose": R("Niveau proposé pour les clients du comptoir", "Suggested level for the guests at the desk", "Nivel sugerido para los clientes del mostrador"),
    "debutant": R("Débutant", "Beginner", "Principiante"),
    "fonctionnel": R("Fonctionnel", "Functional", "Funcional"),
    "aise": R("À l'aise", "Confident", "Con soltura"),
    "formateur": R("Pour le formateur", "For the trainer", "Para el formador"),
    "code": R("Code du formateur", "Trainer code", "Código del formador"),
    "ouvrir": R("Ouvrir", "Open", "Abrir"),
    "code_faux": R("Ce n'est pas le code.", "That's not the code.", "Ese no es el código."),
    "geste": R("Geste attendu", "Expected gesture", "Gesto esperado"),
    "exemple": R("Exemple de réponse", "Sample answer", "Ejemplo de respuesta"),
    "confirmer": R("Confirmer ce niveau", "Confirm this level", "Confirmar este nivel"),
    "confirme": R("Niveau confirmé :", "Level confirmed:", "Nivel confirmado:"),
    "refaire_test": R("Refaire le test", "Take the test again", "Repetir la prueba"),
    "retour_accueil": R("Retour à l'accueil", "Back to home", "Volver al inicio"),
    "precedent": R("Passation précédente", "Previous attempt", "Intento anterior"),
}
