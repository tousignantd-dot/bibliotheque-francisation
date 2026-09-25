"""Le test de positionnement de la réception (étape 3) — dans la langue APPRISE.

Il sert à UNE chose : régler le palier du jeu de rôle (étape 4). Ce n'est pas
un examen et il ne s'annonce pas comme tel. Dix à douze minutes, repassé à la
fin : l'écart entre les deux passations est la preuve d'apprentissage.

QUATRE PARTIES, alignées sur le cadrage (build/contenu/entreprise-hotel/boucle/cadrage.md) :
  A · comprendre la demande (O1) — le lit ET les nuits, au débit d'un client ;
                                    au cran 3, des dates, ou une phrase qui se reprend
  B · noter au téléphone (O2)     — la voix passe par le filtre du téléphone :
                                    numéro de chambre, puis prix et heure, puis
                                    un nom épelé, tapé
  C · qui décide? (O4)            — le client demande ; on choisit : je m'en occupe,
                                    je transmets au gérant, ou personne ne peut le
                                    promettre. Éliminatoire, et DIT AVANT : se
                                    charger soi-même de ce qui revient au gérant
                                    fait échouer la partie
  D · répondre à voix haute (O3)  — enregistré sur l'appareil, écouté et noté par
                                    le formateur, jamais envoyé

LA RÈGLE ADAPTATIVE, la même pour A et B (celle de Francœur) : on part au cran
1 ; trois bonnes réponses valident le cran et font monter ; deux erreurs
arrêtent la partie. Le niveau d'une partie est le dernier cran validé (0 à 3).
Quatre items par cran suffisent (3 justes, ou 2 erreurs, en au plus 4).

AUCUNE RÉTROACTION pendant le test : ni vert ni rouge.

DES PHRASES NEUVES : aucune demande, aucun nom, aucun nombre des exercices.

DEUX FORMES PARALLÈLES, mêmes crans, même difficulté : la première passation
prend la forme 1, la suivante la forme 2, puis on alterne.

LES CARTES DE A EN CARRÉ LATIN (leçon de Francœur) : (lit, nuits) (lit, nuits′)
(lit′, nuits) (lit′, nuits′) — chaque valeur paraît deux fois, la bonne n'est
majoritaire sur aucun trait. Au cran 3, lit′ et nuits′ sont ce que la phrase
ÉCARTE (le lit qu'elle corrige, le compte de nuits qu'on obtient en comptant
les jours au lieu des nuits).

LE PALIER se PROPOSE ; le formateur le confirme. Rien de nominatif : le
résultat vit sur l'appareil.
"""


def R(fr, en, es):
    return {"fr": fr, "en": en, "es": es}


LITS = ["lit-simple", "lit-double", "lit-queen", "lit-king"]

# ── A · la demande ───────────────────────────────────────────────────────
# (id, cran, {langue: phrase}, lit, nuits, lit′, nuits′). Au cran 1, les
# cartes sont les quatre lits, sans nuits (nuits = None).
A = {
    1: [
        ("a11", 1, R("Un lit simple, s'il vous plaît.", "A twin bed, please.", "Una cama individual, por favor."), "lit-simple", None, None, None),
        ("a12", 1, R("Je voudrais un lit king.", "I'd like a king bed.", "Quisiera una cama king size."), "lit-king", None, None, None),
        ("a13", 1, R("Avez-vous une chambre avec un lit double?", "Do you have a room with a double bed?", "¿Tiene una habitación con cama matrimonial?"), "lit-double", None, None, None),
        ("a14", 1, R("Un lit queen, ce serait parfait.", "A queen bed would be perfect.", "Una cama queen estaría perfecto."), "lit-queen", None, None, None),
        ("a21", 2, R("Bonsoir, un lit queen pour trois nuits.", "Evening! A queen bed for three nights.", "Buenas noches, cama queen para tres noches."), "lit-queen", 3, "lit-king", 4),
        ("a22", 2, R("C'est pour deux nuits, dans un lit simple.", "It's for two nights, in a twin bed.", "Es para dos noches, en cama individual."), "lit-simple", 2, "lit-double", 3),
        ("a23", 2, R("On reste quatre nuits; un lit king, si possible.", "We're staying four nights; a king bed if possible.", "Nos quedamos cuatro noches; cama king size, si se puede."), "lit-king", 4, "lit-simple", 5),
        ("a24", 2, R("Une nuit, un lit double, c'est tout.", "One night, a double bed, that's all.", "Una noche, cama matrimonial, nada más."), "lit-double", 1, "lit-queen", 2),
        ("a31", 3, R("J'arrive mardi, je repars jeudi matin. Un lit king.", "I'm arriving Tuesday and leaving Thursday morning. A king bed.", "Llego el martes y me voy el jueves en la mañana. Cama king size."), "lit-king", 2, "lit-queen", 3),
        ("a32", 3, R("Deux nuits… non, attendez, trois nuits. Avec un lit double.", "Two nights… no, wait, three nights. With a double bed.", "Dos noches… no, espere, tres noches. Con cama matrimonial."), "lit-double", 3, "lit-queen", 2),
        ("a33", 3, R("Du dix au quinze juillet, un lit queen.", "From July tenth to July fifteenth, a queen bed.", "Del diez al quince de julio, cama queen."), "lit-queen", 5, "lit-king", 6),
        ("a34", 3, R("Un lit double… en fait non, un lit simple : c'est juste pour moi, pour ce soir.", "A double bed… actually no, a twin: it's just me, for tonight.", "Una cama matrimonial… bueno no, individual: es solo para mí, esta noche."), "lit-simple", 1, "lit-double", 2),
    ],
    2: [
        ("a41", 1, R("Un lit double, s'il vous plaît.", "A double bed, please.", "Una cama matrimonial, por favor."), "lit-double", None, None, None),
        ("a42", 1, R("Je voudrais un lit queen.", "I'd like a queen bed.", "Quisiera una cama queen."), "lit-queen", None, None, None),
        ("a43", 1, R("Avez-vous une chambre avec un lit simple?", "Do you have a room with a twin bed?", "¿Tiene una habitación con cama individual?"), "lit-simple", None, None, None),
        ("a44", 1, R("Un lit king, ce serait parfait.", "A king bed would be perfect.", "Una cama king size estaría perfecto."), "lit-king", None, None, None),
        ("a51", 2, R("Bonsoir, un lit double pour deux nuits.", "Evening! A double bed for two nights.", "Buenas noches, cama matrimonial para dos noches."), "lit-double", 2, "lit-simple", 3),
        ("a52", 2, R("C'est pour trois nuits, dans un lit king.", "It's for three nights, in a king bed.", "Es para tres noches, en cama king size."), "lit-king", 3, "lit-queen", 4),
        ("a53", 2, R("On reste une nuit; un lit queen, si possible.", "We're staying one night; a queen bed if possible.", "Nos quedamos una noche; cama queen, si se puede."), "lit-queen", 1, "lit-double", 2),
        ("a54", 2, R("Quatre nuits, un lit simple, c'est tout.", "Four nights, a twin bed, that's all.", "Cuatro noches, cama individual, nada más."), "lit-simple", 4, "lit-king", 5),
        ("a61", 3, R("J'arrive vendredi, je repars lundi matin. Un lit queen.", "I'm arriving Friday and leaving Monday morning. A queen bed.", "Llego el viernes y me voy el lunes en la mañana. Cama queen."), "lit-queen", 3, "lit-king", 4),
        ("a62", 3, R("Trois nuits… non, attendez, deux nuits. Avec un lit simple.", "Three nights… no, wait, two nights. With a twin bed.", "Tres noches… no, espere, dos noches. Con cama individual."), "lit-simple", 2, "lit-double", 3),
        ("a63", 3, R("Du vingt au vingt-quatre août, un lit king.", "From August twentieth to August twenty-fourth, a king bed.", "Del veinte al veinticuatro de agosto, cama king size."), "lit-king", 4, "lit-queen", 5),
        ("a64", 3, R("Un lit king… en fait non, un lit double : c'est juste pour ce soir.", "A king bed… actually no, a double: it's just for tonight.", "Una cama king size… bueno no, matrimonial: es solo por esta noche."), "lit-double", 1, "lit-king", 2),
    ],
}

# ── B · au téléphone ─────────────────────────────────────────────────────
# Crans 1 et 2 : (id, cran, {langue: phrase}, bonne, [voisines]) — choix écrits
# en chiffres. Cran 3 : un nom épelé (assemblé lettre par lettre), tapé.
B = {
    1: [
        ("b11", 1, R("Vous êtes à la chambre deux cent quatorze.", "You're in room two-fourteen.", "Está en la habitación doscientos catorce."), "214", ["241", "204", "314"]),
        ("b12", 1, R("C'est la chambre cinq cent sept.", "It's room five-oh-seven.", "Es la habitación quinientos siete."), "507", ["570", "705", "517"]),
        ("b13", 1, R("Votre chambre est la onze cent deux.", "Your room is eleven-oh-two.", "Su habitación es la mil ciento dos."), "1102", ["1120", "2101", "1112"]),
        ("b14", 1, R("La chambre trois cent dix-huit, au troisième.", "Room three-eighteen, on the third floor.", "La habitación trescientos dieciocho, en el tercer piso."), "318", ["381", "308", "813"]),
        ("b21", 2, R("Le total est de deux cent trente-neuf dollars.", "Your total is two hundred thirty-nine dollars.", "El total es de doscientos treinta y nueve dólares."), "239 $", ["293 $", "229 $", "139 $"]),
        ("b22", 2, R("Le déjeuner finit à dix heures et demie.", "Breakfast ends at ten thirty.", "El desayuno termina a las diez y media."), "10:30", ["10:15", "11:30", "22:30"]),
        ("b23", 2, R("La navette part à dix-sept heures quinze.", "The shuttle leaves at five fifteen p.m.", "La camioneta sale a las cinco y cuarto de la tarde."), "17:15", ["17:50", "7:15", "16:15"]),
        ("b24", 2, R("Ça fait cent soixante-quinze dollars et quarante.", "That's one seventy-five forty.", "Son ciento setenta y cinco dólares con cuarenta."), "175,40 $", ["175,14 $", "157,40 $", "165,40 $"]),
        ("b31", 3, "DUMONT"),
        ("b32", 3, "PATEL"),
        ("b33", 3, "RODRÍGUEZ"),
        ("b34", 3, "FORTIN"),
    ],
    2: [
        ("b41", 1, R("Vous êtes à la chambre deux cent seize.", "You're in room two-sixteen.", "Está en la habitación doscientos dieciséis."), "216", ["261", "206", "316"]),
        ("b42", 1, R("C'est la chambre quatre cent neuf.", "It's room four-oh-nine.", "Es la habitación cuatrocientos nueve."), "409", ["490", "904", "419"]),
        ("b43", 1, R("Votre chambre est la douze cent trois.", "Your room is twelve-oh-three.", "Su habitación es la mil doscientos tres."), "1203", ["1230", "3201", "1213"]),
        ("b44", 1, R("La chambre sept cent quinze, au septième.", "Room seven-fifteen, on the seventh floor.", "La habitación setecientos quince, en el séptimo piso."), "715", ["751", "705", "515"]),
        ("b51", 2, R("Le total est de trois cent quarante-huit dollars.", "Your total is three hundred forty-eight dollars.", "El total es de trescientos cuarenta y ocho dólares."), "348 $", ["384 $", "338 $", "248 $"]),
        ("b52", 2, R("La piscine ouvre à neuf heures et demie.", "The pool opens at nine thirty.", "La alberca abre a las nueve y media."), "9:30", ["9:15", "10:30", "21:30"]),
        ("b53", 2, R("Le souper est servi à dix-huit heures quarante-cinq.", "Dinner is served at six forty-five p.m.", "La cena se sirve a un cuarto para las siete de la tarde."), "18:45", ["18:15", "6:45", "17:45"]),
        ("b54", 2, R("Ça fait cent vingt-six dollars et soixante.", "That's one twenty-six sixty.", "Son ciento veintiséis dólares con sesenta."), "126,60 $", ["126,16 $", "162,60 $", "136,60 $"]),
        ("b61", 3, "LEBLANC"),
        ("b62", 3, "NAKAMURA"),
        ("b63", 3, "HERNÁNDEZ"),
        ("b64", 3, "BOUCHARD"),
    ],
}

# ── C · qui décide? ──────────────────────────────────────────────────────
# (id, {langue: demande du client}, réponse juste parmi CHOIX_C). Se charger
# SOI-MÊME d'un item « gerant » ou « personne » est une promesse : la partie
# échoue, quel que soit le compte (O4, éliminatoire, annoncé avant).
CHOIX_C = {
    "moi": R("Je m'en occupe moi-même", "I handle it myself", "Me encargo yo mismo"),
    "gerant": R("Je transmets au gérant", "I pass it to the manager", "Se lo paso al gerente"),
    "personne": R("Personne ne peut le promettre : je l'explique poliment",
                  "No one can promise that: I explain it politely",
                  "Nadie puede prometerlo: lo explico con cortesía"),
}
C = {
    1: [
        ("c1", R("Ma carte-clé ne marche plus.", "My key card stopped working.", "Mi tarjeta llave ya no funciona."), "moi"),
        ("c2", R("Vous pouvez me faire un prix, pour trois nuits?", "Could you give me a better rate for three nights?", "¿Me puede hacer un descuento por tres noches?"), "gerant"),
        ("c3", R("C'est quoi, le mot de passe du wifi?", "What's the Wi-Fi password?", "¿Cuál es la contraseña del wifi?"), "moi"),
        ("c4", R("Le bruit m'a empêché de dormir; je veux un rabais sur ma facture.", "The noise kept me up; I want a discount on my bill.", "El ruido no me dejó dormir; quiero un descuento en mi cuenta."), "gerant"),
        ("c5", R("Pouvez-vous enlever les taxes de ma facture?", "Can you take the taxes off my bill?", "¿Me puede quitar los impuestos de la cuenta?"), "personne"),
        ("c6", R("Je peux garder la chambre jusqu'à dix-huit heures, sans frais?", "Can I keep the room until six p.m. at no charge?", "¿Puedo quedarme en la habitación hasta las seis de la tarde sin costo?"), "gerant"),
    ],
    2: [
        ("c7", R("Il n'y a plus de serviettes dans ma chambre.", "There are no more towels in my room.", "Ya no hay toallas en mi habitación."), "moi"),
        ("c8", R("Vous pourriez nous offrir le déjeuner? C'est notre anniversaire.", "Could you give us free breakfast? It's our anniversary.", "¿Nos podría regalar el desayuno? Es nuestro aniversario."), "gerant"),
        ("c9", R("À quelle heure est le départ?", "What time is check-out?", "¿A qué hora es la salida?"), "moi"),
        ("c10", R("Je veux annuler sans payer les frais, même si c'est trop tard.", "I want to cancel without paying the fee, even if it's too late.", "Quiero cancelar sin pagar el cargo, aunque sea tarde."), "gerant"),
        ("c11", R("Vous êtes complets? Donnez-moi une chambre quand même!", "You're full? Give me a room anyway!", "¿Están llenos? ¡Deme una habitación de todos modos!"), "personne"),
        ("c12", R("Je voudrais un surclassement gratuit, s'il vous plaît.", "I'd like a free upgrade, please.", "Quisiera un upgrade sin costo, por favor."), "gerant"),
    ],
}

# ── D · répondre à voix haute ────────────────────────────────────────────
# (id, {interface: contexte} ou None, {apprise: phrase du client}, geste
# {interface}, {apprise: exemple de réponse}). La clé et l'exemple ne
# s'affichent qu'au formateur (code).
GESTES = {
    "epeler": R("Accueillir et faire épeler le nom", "Greet and have the name spelled", "Recibir y pedir que deletree el apellido"),
    "refuser": R("Refuser poliment et proposer une solution", "Decline politely and offer a solution", "Rechazar con cortesía y ofrecer una solución"),
    "frais": R("Expliquer les frais", "Explain the charge", "Explicar el cargo"),
    "relais": R("Passer le relais au gérant, sans promettre", "Hand it to the manager, without promising", "Pasarlo al gerente, sin prometer"),
}
D = {
    1: [
        ("d1", None, R("Bonjour! J'ai réservé une chambre au nom de Vasquez.", "Hi! I booked a room under Vasquez.", "¡Hola! Reservé una habitación a nombre de Vásquez."), "epeler",
         R("Bienvenue! Pouvez-vous m'épeler votre nom de famille?", "Welcome! Could you spell your last name, please?", "¡Bienvenido! ¿Me puede deletrear su apellido?")),
        ("d2", R("L'hôtel est complet ce soir.", "The hotel is fully booked tonight.", "El hotel está lleno esta noche."),
         R("Il vous reste une chambre pour ce soir?", "Do you have a room left for tonight?", "¿Le queda una habitación para esta noche?"), "refuser",
         R("Je suis désolé, nous sommes complets. Je peux appeler un hôtel voisin pour vous.", "I'm sorry, we're fully booked. I can call a nearby hotel for you.", "Lo siento, estamos llenos. Le puedo llamar a un hotel cercano.")),
        ("d3", R("Le client a pris deux consommations au minibar : 25 $.", "The guest took two items from the minibar: $25.", "El cliente tomó dos cosas del frigobar: 25 dólares."),
         R("Pourquoi il y a vingt-cinq dollars de plus sur ma facture?", "Why is there an extra twenty-five dollars on my bill?", "¿Por qué hay veinticinco dólares más en mi cuenta?"), "frais",
         R("Ce sont les deux consommations du minibar, vingt-cinq dollars en tout.", "Those are the two minibar items, twenty-five dollars in total.", "Son las dos cosas del frigobar, veinticinco dólares en total.")),
        ("d4", None, R("Je veux partir sans payer la dernière nuit : la climatisation ne marchait pas.", "I want to leave without paying for the last night: the A/C didn't work.", "Me quiero ir sin pagar la última noche: el aire acondicionado no funcionaba."), "relais",
         R("Je suis désolé. Je ne peux pas le décider moi-même : j'en parle au gérant tout de suite.", "I'm sorry. I can't decide that myself: I'll speak to the manager right away.", "Lo siento. No puedo decidirlo yo: lo hablo con el gerente ahora mismo.")),
    ],
    2: [
        ("d5", None, R("Bonsoir, la réservation est au nom de Kowalczyk.", "Good evening, the reservation is under Kowalczyk.", "Buenas noches, la reservación está a nombre de Kowalczyk."), "epeler",
         R("Bonsoir, bienvenue! Pouvez-vous m'épeler ce nom, s'il vous plaît?", "Good evening, welcome! Could you spell that name for me, please?", "¡Buenas noches, bienvenido! ¿Me puede deletrear el apellido, por favor?")),
        ("d6", R("L'hôtel est complet ce soir.", "The hotel is fully booked tonight.", "El hotel está lleno esta noche."),
         R("On aurait besoin de deux chambres pour ce soir.", "We'd need two rooms for tonight.", "Necesitaríamos dos habitaciones para esta noche."), "refuser",
         R("Je suis désolé, c'est complet ce soir. Voulez-vous que j'appelle un autre hôtel?", "I'm sorry, we're full tonight. Would you like me to call another hotel?", "Lo siento, estamos llenos esta noche. ¿Quiere que llame a otro hotel?")),
        ("d7", R("Deux nuits de stationnement, à 20 $ la nuit.", "Two nights of parking, $20 a night.", "Dos noches de estacionamiento, a 20 dólares la noche."),
         R("C'est quoi, ces quarante dollars?", "What's this forty dollars?", "¿Qué son estos cuarenta dólares?"), "frais",
         R("C'est le stationnement : deux nuits à vingt dollars.", "That's the parking: two nights at twenty dollars.", "Es el estacionamiento: dos noches a veinte dólares.")),
        ("d8", None, R("Je voudrais que vous enleviez les frais d'annulation, s'il vous plaît.", "I'd like you to waive the cancellation fee, please.", "Quisiera que me quitara el cargo de cancelación, por favor."), "relais",
         R("Je comprends. Je ne peux pas le faire moi-même; je transmets votre demande au gérant.", "I understand. I can't do that myself; I'll pass your request to the manager.", "Entiendo. Yo no puedo hacerlo; le paso su solicitud al gerente.")),
    ],
}

# La clé du formateur : ni l'exemple ni le geste ne s'affichent à l'employé.
CODE_FORMATEUR = "2413"
ORAL = R("A fait le geste|A deviné ou promis|Pas de réponse",
         "Did the gesture|Guessed or promised|No answer",
         "Hizo el gesto|Adivinó o prometió|Sin respuesta")

# ── Les seuils (objectif atteint) et le palier ───────────────────────────
#   A · cran 3 — la demande, dates et reprises comprises (O1)
#   B · cran 3 — le nom épelé au téléphone (O2)
#   C · 5 sur 6, et aucune promesse (O4)
SEUILS = {"A": 3, "B": 3, "C": 5}
# Le palier, sur A + B (0 à 6), écrit ici en données, appliqué une seule fois :
#   A + B <= DEBUTANT_MAX ou A == 0              → débutant
#   A + B >= AISE_MIN et C réussie (sans promesse) → à l'aise
#   sinon                                         → fonctionnel
DEBUTANT_MAX, AISE_MIN = 2, 5
PALIERS = ["debutant", "fonctionnel", "aise"]

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
    "regle_c": R("À savoir avant de commencer : dans la partie C, vous charger vous-même de ce qui revient au gérant "
                 "(un rabais, une exception, un service gratuit) fait échouer la partie, comme au comptoir.",
                 "Know this before you start: in part C, handling yourself what belongs to the manager "
                 "(a discount, an exception, anything free) fails the part, just like at the desk.",
                 "Antes de empezar: en la parte C, encargarse usted mismo de lo que le toca al gerente "
                 "(un descuento, una excepción, algo gratis) hace fallar la parte, como en el mostrador."),
    "passation": R("Passation", "Attempt", "Intento"),
    "forme": R("forme", "form", "forma"),
    "commencer_test": R("Commencer le test", "Start the test", "Empezar la prueba"),
    "partie": R("Partie", "Part", "Parte"),
    "pA": R("Ce que le client demande", "What the guest asks for", "Lo que pide el cliente"),
    "pA_c": R("Écoutez le client. Touchez la chambre qu'il demande.", "Listen to the guest. Tap the room they ask for.", "Escuche al cliente. Toque la habitación que pide."),
    "pB": R("Au téléphone", "On the phone", "Por teléfono"),
    "pB_c": R("Écoutez, puis touchez ce que vous devez noter.", "Listen, then tap what you need to write down.", "Escuche y toque lo que debe anotar."),
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
