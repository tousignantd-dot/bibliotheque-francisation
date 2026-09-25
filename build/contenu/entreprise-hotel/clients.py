"""Le comptoir de l'Hôtel Rive-Claire — les huit clients du jeu de rôle (étape 4).

SOURCE UNIQUE : `server.py` lit ce fichier au démarrage (scénarios
« comptoir-<apprend>-<parle> » de /api/jeu-de-role), `build/hotel_planches.py`
en tire les cartes de l'écran, `build/hotel_clients.py` les portraits. Rien ne
se recopie.

TROIS LANGUES À ÉGALITÉ. Le client parle la langue APPRISE (fr-CA, en
nord-américain, es du Mexique) ; la carte de la situation se lit dans la langue
de l'employé (c'est une consigne) ; la FICHE DE L'ÉCRAN — ce que le système de
l'hôtel affiche — est du contenu, donc dans la langue apprise. Le bilan parle
la langue de l'employé et propose la phrase à dire dans la langue apprise.
D'où six scénarios, un par direction : la consigne du client dépend de la
langue apprise, celle du bilan de la langue parlée.

L'employé est TOUJOURS le réceptionniste : il ne se voit pas. Le client est
dessiné debout de l'autre côté du comptoir, sur le décor fixe de l'étape 1
(croquis-sequence : le décor ne bouge pas, les clients changent). Au
téléphone, pas de visage : c'est la situation la plus dure à l'oreille.

LES HUIT SITUATIONS sont celles du plan (hotellerie-plan.html, volet 4). Chaque
client a un besoin, un caractère et un PIÈGE — ce qui fait rater le comptoir
quand on ne comprend pas, ou quand on promet ce qu'on ne peut pas tenir.

LA RÈGLE DU RELAIS n'est pas réécrite ici : elle est citée depuis
exercices.REGLE_RELAIS (leçon de Francœur — dite trois fois, elle se
contredisait). Une promesse hors règle est ÉLIMINATOIRE (O4) : le bilan la
relève à part, avec sa citation.

L'HUMEUR : le client commence chaque réplique par une étiquette — [neutre]
[contente] [hesitante] [impatiente], en français quelle que soit la langue du
jeu. L'écran la retire du texte et de la voix, et montre le visage.
"""
import importlib.util
import pathlib

_ICI = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("hotel_exercices_clients", _ICI / "exercices.py")
_EX = importlib.util.module_from_spec(_s)
_s.loader.exec_module(_EX)
REGLE_RELAIS = _EX.REGLE_RELAIS


def R(fr, en, es):
    return {"fr": fr, "en": en, "es": es}


LANGUES = ("fr", "en", "es")
HUMEURS = ["neutre", "contente", "hesitante", "impatiente"]
PALIERS = ["debutant", "fonctionnel", "aise"]

# Comment le client parle, selon la langue apprise (variétés décidées le 24 sept.).
PARLER = {
    "fr": "en français québécois courant, avec les mots d'ici (« une chambre à deux lits », "
          "« le déjeuner » pour le repas du matin, « la facture »)",
    "en": "in everyday North American English (« check-in », « a king bed », « the bill »)",
    "es": "en español de México cotidiano (« una habitación », « la cuenta », « usted »)",
}
NOM_LANGUE = {"fr": "français", "en": "anglais", "es": "espagnol"}
APPREND_ART = {"fr": "le français", "en": "l'anglais", "es": "l'espagnol"}
# La langue du bilan, telle qu'on la nomme au modèle.
LANGUE_BILAN = {"fr": "en français simple", "en": "in simple English", "es": "en español sencillo"}

# Le titre de civilité du client, dans la langue apprise (le nom ne change pas).
TITRE = {"f": R("Madame", "Ms.", "la señora"), "m": R("Monsieur", "Mr.", "el señor")}
VOIX = {"f": {l: f"hotel_{l}_f" for l in LANGUES}, "m": {l: f"hotel_{l}_m" for l in LANGUES}}

# Ce que le réceptionniste dit pour ouvrir : au comptoir, ou en décrochant.
OUVERTURE = {
    "comptoir": R("Bonjour, bienvenue à l'Hôtel Rive-Claire!",
                  "Hello, welcome to the Hôtel Rive-Claire!",
                  "Buenas tardes, bienvenido al Hotel Rive-Claire."),
    "telephone": R("Hôtel Rive-Claire, bonjour!",
                   "Hôtel Rive-Claire, good afternoon!",
                   "Hotel Rive-Claire, buenas tardes."),
}

# Les six gestes du comptoir (O2, O3, O4). Un nom court et la phrase qui le fait,
# dans chaque langue. Le bilan les juge un par un.
GESTES = [
    {"id": "accueil", "nom": R("Accueillir", "Greet the guest", "Recibir al cliente"),
     "phrase": R("Bonjour, comment puis-je vous aider?", "Hello, how can I help you?",
                 "Buenas tardes, ¿en qué le puedo ayudar?")},
    {"id": "epeler", "nom": R("Faire répéter ou épeler", "Ask to repeat or spell",
                              "Pedir que repita o deletree"),
     "phrase": R("Pouvez-vous épeler votre nom, s'il vous plaît?", "Could you spell your last name, please?",
                 "¿Me puede deletrear su apellido, por favor?")},
    {"id": "confirmer", "nom": R("Redire pour confirmer", "Repeat back to confirm",
                                 "Repetir para confirmar"),
     "phrase": R("Donc, deux nuits, du 14 au 16 octobre, c'est bien ça?",
                 "So that's two nights, October 14 to 16, correct?",
                 "Entonces, dos noches, del 14 al 16 de octubre, ¿correcto?")},
    {"id": "proposer", "nom": R("Refuser poliment et proposer", "Say no politely and offer something",
                                "Decir que no con cortesía y ofrecer algo"),
     "phrase": R("Je suis désolé, c'est complet ce soir. Je peux vous proposer…",
                 "I'm sorry, we're full tonight. What I can offer you is…",
                 "Lo siento, esta noche estamos llenos. Le puedo ofrecer…")},
    {"id": "frais", "nom": R("Expliquer un frais", "Explain a charge", "Explicar un cargo"),
     "phrase": R("Ce montant, c'est le stationnement : 15 $ par nuit, pour deux nuits.",
                 "That amount is for parking: $15 a night, for two nights.",
                 "Ese cargo es del estacionamiento: 15 dólares por noche, dos noches.")},
    {"id": "relais", "nom": R("Passer le relais au gérant, sans promettre",
                              "Hand it to the manager, without promising",
                              "Pasarlo al gerente, sin prometer"),
     "phrase": R("Ce n'est pas moi qui décide. Je transmets votre demande au gérant.",
                 "That's not my decision to make. I'll pass your request on to the manager.",
                 "No me corresponde decidirlo. Le paso su solicitud al gerente.")},
]

# (id, genre, nom, paliers, lieu, gestes en jeu, carte (langue de l'employé),
#  écran (langue apprise), portrait (dessin), faits (ce que le client sait))
# Les faits s'écrivent en français : ce sont des consignes au modèle, qui PARLE
# la langue apprise (règle posée par `systeme()`).
CLIENTS = [
    ("arrivee", "f", "Bélanger", ["debutant", "fonctionnel", "aise"], "comptoir",
     ["accueil", "epeler", "confirmer"],
     R("Elle arrive avec une réservation. Trouvez-la, et confirmez les dates.",
       "She arrives with a booking. Find it and confirm the dates.",
       "Llega con una reservación. Encuéntrela y confirme las fechas."),
     R("Réservation : BÉLANGER · 14 → 16 oct. · 2 nuits · 2 lits queen · 338 $",
       "Booking: BÉLANGER · Oct 14 → 16 · 2 nights · 2 queen beds · $338",
       "Reservación: BÉLANGER · 14 → 16 oct. · 2 noches · 2 camas queen · 338 dólares"),
     "a woman in her fifties, short silver-blond hair, small round glasses, a teal rain jacket "
     "zipped halfway over a cream sweater, a travel bag strap on one shoulder",
     ["Tu es madame Bélanger. Tu arrives à l'hôtel avec une réservation pour deux nuits, du 14 au "
      "16 octobre, une chambre à deux lits queen.",
      "Au début, tu dis seulement que tu as une réservation et ton nom : « Bélanger ». Tu ne "
      "l'épelles QUE si le réceptionniste te le demande : B-É-L-A-N-G-E-R.",
      "Si le réceptionniste répète les dates et le type de chambre, tu confirmes, contente.",
      "S'il se trompe de dates ou de lits, tu le corriges poliment.",
      "Quand on te donne la carte-clé et le numéro de chambre, tu demandes l'heure du déjeuner, "
      "puis tu remercies et tu pars."]),

    ("sans-resa", "m", "Okafor", ["debutant", "fonctionnel", "aise"], "comptoir",
     ["accueil", "confirmer", "frais"],
     R("Il n'a pas de réservation. Il veut une chambre pour ce soir.",
       "He has no booking. He wants a room for tonight.",
       "No tiene reservación. Quiere una habitación para esta noche."),
     R("Ce soir : 1 chambre lit king libre, 189 $ · 2 chambres 2 lits queen libres, 169 $ · "
       "déjeuner non compris : 18 $",
       "Tonight: 1 king room available, $189 · 2 rooms with 2 queen beds available, $169 · "
       "breakfast not included: $18",
       "Esta noche: 1 habitación con cama king libre, 189 dólares · 2 habitaciones con 2 camas "
       "queen libres, 169 dólares · desayuno no incluido: 18 dólares"),
     "a tall man in his thirties, very short black hair, a neat short beard, a dark green "
     "bomber jacket over a grey t-shirt, a backpack strap on one shoulder",
     ["Tu es monsieur Okafor. Tu arrives sans réservation et tu veux une chambre pour UNE nuit, "
      "ce soir, avec un grand lit.",
      "Tu demandes le prix. Si on te dit 189 $, tu demandes si le déjeuner est compris.",
      "Si le réceptionniste te dit que le déjeuner est en plus (18 $), tu le prends quand même.",
      "Tu paies par carte de crédit. Si on te demande ton nom, tu dis « Okafor » et tu "
      "l'épelles si on te le demande : O-K-A-F-O-R.",
      "Si le réceptionniste répète le prix et le nombre de nuits avant de conclure, tu es "
      "content."]),

    ("complet", "f", "Hoang", ["fonctionnel", "aise"], "comptoir",
     ["accueil", "proposer"],
     R("Elle veut une chambre ce soir. L'hôtel est complet.",
       "She wants a room tonight. The hotel is full.",
       "Quiere una habitación esta noche. El hotel está lleno."),
     R("Ce soir : COMPLET · Demain : chambres libres · Hôtel du Parc (5 min à pied) : de la place ce soir",
       "Tonight: FULL · Tomorrow: rooms available · Hôtel du Parc (5-minute walk): rooms tonight",
       "Esta noche: LLENO · Mañana: habitaciones libres · Hôtel du Parc (a 5 minutos a pie): hay lugar esta noche"),
     "a woman in her twenties, long straight black hair with a fringe, a mustard-yellow wool "
     "coat, a grey knitted scarf, looking tired from travelling",
     ["Tu es madame Hoang. Tu arrives sans réservation, fatiguée, et tu veux une chambre pour "
      "trois nuits à partir de ce soir.",
      "Tu insistes une fois : « Il ne vous reste vraiment rien? »",
      "Si le réceptionniste refuse sèchement, sans rien proposer, tu deviens impatiente.",
      "S'il s'excuse et te propose une solution (un autre hôtel ce soir, puis revenir ici "
      "demain), tu acceptes et tu demandes comment te rendre à l'autre hôtel.",
      "S'il te promet une chambre qu'il n'a pas, tu le crois et tu attends."]),

    ("plainte", "m", "Tremblay", ["debutant", "fonctionnel", "aise"], "comptoir",
     ["accueil", "epeler", "relais"],
     R("Il revient au comptoir. Sa carte-clé ne marche pas.",
       "He comes back to the desk. His key card doesn't work.",
       "Regresa al mostrador. Su tarjeta llave no funciona."),
     R("Chambre 412 · TREMBLAY · 3 nuits · encodeur de cartes-clés sur le comptoir",
       "Room 412 · TREMBLAY · 3 nights · key card encoder on the desk",
       "Habitación 412 · TREMBLAY · 3 noches · codificador de tarjetas en el mostrador"),
     "a man in his sixties, bald on top with short white hair on the sides, a white moustache, "
     "a navy fleece jacket, holding nothing",
     ["Tu es monsieur Tremblay, chambre 412. Ta carte-clé ne marche plus : la porte ne s'ouvre "
      "pas. Tu es agacé : c'est la deuxième fois.",
      "Tu dis « quatre cent douze » vite. Tu répètes lentement si on te le demande.",
      "Si le réceptionniste refait ta carte (il peut le faire lui-même), tu te calmes un peu.",
      "Ensuite, tu demandes un rabais sur la chambre pour le dérangement.",
      "Un rabais, ce n'est pas le réceptionniste qui le décide. S'il te dit qu'il transmet ta "
      "demande au gérant, tu acceptes. S'il te promet lui-même un rabais, tu le remercies "
      "chaleureusement."]),

    ("facture", "f", "Castillo", ["fonctionnel", "aise"], "comptoir",
     ["frais", "relais"],
     R("Elle part. Elle ne comprend pas un montant sur sa facture.",
       "She is checking out. She doesn't understand an amount on her bill.",
       "Se va del hotel. No entiende un cargo en su cuenta."),
     R("Facture CASTILLO · chambre 2 nuits 338 $ · stationnement 2 × 15 $ = 30 $ · taxes · total 422,28 $",
       "Bill CASTILLO · room 2 nights $338 · parking 2 × $15 = $30 · taxes · total $422.28",
       "Cuenta CASTILLO · habitación 2 noches 338 dólares · estacionamiento 2 × 15 = 30 dólares · impuestos · total 422.28 dólares"),
     "a woman in her forties, dark wavy shoulder-length hair, gold hoop earrings, a red trench "
     "coat over a black top",
     ["Tu es madame Castillo. Tu pars ce matin. Sur ta facture, tu vois 30 $ que tu ne "
      "comprends pas.",
      "C'est le stationnement : 15 $ par nuit, deux nuits. Tu ne le sais pas.",
      "Si le réceptionniste t'explique clairement le montant, tu comprends, mais tu demandes "
      "qu'on l'enlève : personne ne t'avait dit que le stationnement était payant.",
      "Enlever un frais, c'est le gérant qui le décide. S'il transmet ta demande au gérant, tu "
      "acceptes d'attendre. S'il enlève lui-même le frais, tu es contente.",
      "Tu demandes aussi si les taxes peuvent être enlevées « tant qu'à y être » : elles ne "
      "s'enlèvent jamais."]),

    ("renseignement", "m", "Nakamura", ["debutant", "fonctionnel", "aise"], "comptoir",
     ["accueil", "confirmer"],
     R("Il veut des renseignements : le déjeuner et le Vieux-Port.",
       "He wants some information: breakfast and the Old Port.",
       "Quiere información: el desayuno y el Puerto Viejo."),
     R("Déjeuner : 6 h 30 à 10 h, salle à manger · Vieux-Port : 15 min à pied, tout droit par la "
       "rue Principale · plan de la ville sur le comptoir",
       "Breakfast: 6:30 to 10 a.m., dining room · Old Port: 15-minute walk, straight down Main "
       "Street · city map on the desk",
       "Desayuno: de 6:30 a 10, en el comedor · Puerto Viejo: 15 minutos a pie, todo derecho por "
       "la calle Principal · plano de la ciudad en el mostrador"),
     "a man in his seventies, neat white hair combed to the side, thin rectangular glasses, a "
     "beige cardigan over a light blue collared shirt, a camera strap around his neck",
     ["Tu es monsieur Nakamura. Tu es client de l'hôtel et tu es de bonne humeur.",
      "Tu demandes d'abord à quelle heure est le déjeuner. Tu confonds facilement 6 h 30 et "
      "7 h 30 : si le réceptionniste ne le redit pas clairement, tu répètes la mauvaise heure.",
      "Puis tu demandes comment aller au Vieux-Port à pied.",
      "Si le réceptionniste te montre le chemin sur le plan, tu es content et tu demandes "
      "combien de temps ça prend.",
      "Tu remercies et tu pars."]),

    ("telephone", "m", "Vuković", ["fonctionnel", "aise"], "telephone",
     ["epeler", "confirmer"],
     R("Au téléphone : il veut réserver. Pas de visage : faites répéter, épeler, confirmer.",
       "On the phone: he wants to book. No face: ask to repeat, spell and confirm.",
       "Por teléfono: quiere reservar. Sin cara: pida que repita, que deletree, y confirme."),
     R("Vendredi 17 et samedi 18 oct. : 1 chambre lit double libre, 159 $ la nuit",
       "Friday Oct 17 and Saturday Oct 18: 1 double-bed room available, $159 a night",
       "Viernes 17 y sábado 18 de oct.: 1 habitación con cama matrimonial libre, 159 dólares la noche"),
     "",
     ["Tu es monsieur Vuković et tu appelles l'hôtel au téléphone. Tu parles un peu vite.",
      "Tu veux réserver deux nuits, vendredi et samedi prochains (le 17 et le 18 octobre), une "
      "chambre avec un lit double.",
      "Ton nom est Vuković. Tu l'épelles si on te le demande : V-U-K-O-V-I-C, « avec un accent "
      "sur le c, mais ce n'est pas grave ».",
      "Ton numéro de téléphone : 514 555-0193. Tu le donnes si on te le demande.",
      "Si le réceptionniste ne redit pas les dates, le nom et le numéro avant de raccrocher, tu "
      "demandes : « Vous avez bien tout noté? »"]),

    ("hors-regle", "f", "Leblanc", ["debutant", "fonctionnel", "aise"], "comptoir",
     ["accueil", "proposer", "relais"],
     R("Elle demande deux faveurs pour son anniversaire de mariage.",
       "She asks for two favours for her wedding anniversary.",
       "Pide dos favores por su aniversario de bodas."),
     R("Chambre 208 · LEBLANC · départ : 11 h · départ tardif et surclassement : décision du gérant",
       "Room 208 · LEBLANC · check-out: 11 a.m. · late check-out and upgrades: manager's decision",
       "Habitación 208 · LEBLANC · salida: 11 a. m. · salida tardía y mejora de habitación: decide el gerente"),
     "a woman in her sixties, curly auburn hair, pearl stud earrings, a lilac blazer over a "
     "white blouse, smiling politely",
     ["Tu es madame Leblanc, chambre 208. C'est ton anniversaire de mariage.",
      "Tu demandes, gentiment mais avec insistance, une suite gratuite ce soir (un surclassement).",
      "Tu demandes aussi de partir à 16 h demain au lieu de 11 h, sans payer.",
      "Ces deux faveurs, c'est le gérant qui les décide. Si le réceptionniste dit qu'il "
      "transmet au gérant sans rien promettre, tu acceptes, un peu déçue.",
      "S'il te promet lui-même la suite ou le départ tardif, tu es ravie et tu le remercies.",
      "Tu essaies une fois : « Allez, vous pouvez bien faire ça pour moi! »"]),
]

# Le palier règle la façon de parler du client, jamais le scénario. Même
# principe que Francœur (audit E2 : le client débutant ne reformule pas de
# lui-même — il attend qu'on le lui demande).
PALIERS_JEU = {
    "debutant": ("Palier débutant : l'employé commence dans cette langue. Tes répliques font UNE "
                 "phrase courte, avec des mots simples et concrets. Donne UNE information à la "
                 "fois. Tu restes patient, mais tu ne reformules PAS de toi-même : tu répètes plus "
                 "lentement ou autrement SEULEMENT quand on te le demande. Si l'employé répond à "
                 "côté ou fait semblant d'avoir compris, montre-le avec [hesitante] et redis ta "
                 "demande telle quelle."),
    "fonctionnel": ("Palier fonctionnel : l'employé se débrouille. Tes répliques font une ou deux "
                    "phrases, au débit d'un client ordinaire. Tu es patient la première fois qu'on "
                    "te fait répéter, un peu moins la troisième."),
    "aise": ("Palier à l'aise : l'employé comprend bien. Tu parles comme un vrai client pressé : "
             "deux ou trois phrases, des expressions courantes, parfois deux demandes dans la "
             "même phrase. Tu montres ton impatience si on te fait attendre sans rien dire."),
}
DEBIT_JEU = {"debutant": "lent", "fonctionnel": None, "aise": None}


def _client(ident):
    return next(c for c in CLIENTS if c[0] == ident)


def systeme(apprend):
    """La consigne système du client, pour une langue apprise.

    Stable d'un tour à l'autre (elle est mise en cache) : le palier va à la fin.
    Appelée par `jeu_de_role_system()` de server.py quand le scénario la porte.
    """
    def construire(cas_id, role_eleve, palier=None):
        ident, genre, nom, _p, lieu, _g, carte, ecran, _portrait, faits = _client(cas_id)
        qui = f"{TITRE[genre][apprend]} {nom}"
        tel = lieu == "telephone"
        return (
            "Tu joues un rôle dans un exercice oral de langue au travail. Ton interlocuteur est un "
            f"employé de la réception d'un hôtel du Québec, l'Hôtel Rive-Claire, qui apprend "
            f"{APPREND_ART[apprend]}. Tu joues un CLIENT : {qui}.\n\n"
            f"LANGUE : tu parles UNIQUEMENT {PARLER[apprend]}, du début à la fin, même si l'employé "
            "te parle dans une autre langue. S'il change de langue, tu fais comme un vrai client : "
            "tu ne comprends pas bien et tu redis ta demande dans ta langue.\n\n"
            + ("LE LIEU : tu APPELLES l'hôtel au téléphone. Vous ne vous voyez pas. Tu ne dis "
               "jamais « regardez » ni « ici ».\n\n" if tel else
               "LE LIEU : tu es debout devant le comptoir de la réception.\n\n")
            + "Ce que tu sais et que l'employé ignore :\n"
            + "\n".join("- " + f for f in faits) + "\n\n"
            "La règle de l'hôtel, que tu ne connais pas mais que l'employé doit suivre : "
            + REGLE_RELAIS["fr"] + "\n\n"
            "Comment tu parles :\n"
            "- La longueur de chaque réplique suit le palier indiqué à la fin, et ne dépasse "
            "jamais trois phrases. Jamais de paragraphe, jamais de liste.\n"
            "- Tu vouvoies l'employé (usted en espagnol, poli en anglais), comme un client.\n"
            "- Reste dans ton personnage quoi qu'il arrive. Si l'employé sort du jeu, ramène-le "
            "dans la conversation avec naturel.\n"
            "- Ne corrige jamais la langue de l'employé et ne commente jamais ses fautes. Si une "
            "phrase est incompréhensible, demande simplement de répéter.\n"
            "- N'écris jamais de balise XML, d'astérisque ni de didascalie : seulement ce que tu dis.\n"
            "- Commence CHAQUE réplique par UNE étiquette d'humeur entre crochets, EN FRANÇAIS, "
            "parmi exactement : [neutre] [contente] [hesitante] [impatiente] — puis ta réplique. "
            "L'écran la retire et montre ton visage. [contente] quand l'employé t'a compris ou "
            "bien aidé ; [hesitante] quand tu ne sais pas ou que tu as mal compris ; [impatiente] "
            "quand on te fait répéter sans avancer ou qu'on te refuse sèchement ; sinon [neutre]. "
            "Au masculin comme au féminin, l'étiquette s'écrit ainsi.\n\n"
            "Quand ta demande est réglée, ou quand tu décides de partir"
            + (" ou de raccrocher" if tel else "") + ", dis-le en une phrase, remercie ou salue, et "
            "termine ta dernière réplique par le mot FIN."
            + ("\n\n" + PALIERS_JEU[palier] if palier in PALIERS_JEU else "")
        )
    return construire


def bilan(apprend, parle):
    """La consigne du bilan : juger les gestes, relever la promesse, reprendre trois phrases."""
    gestes = " · ".join(f"{g['id']} ({g['nom']['fr']})" for g in GESTES)
    return (
        "Tu es formateur en réception hôtelière. Voici la transcription d'un échange à la réception "
        f"de l'Hôtel Rive-Claire : un CLIENT (joué par un modèle) et un RÉCEPTIONNISTE, un employé "
        f"qui apprend {APPREND_ART[apprend]}. Juge le RÉCEPTIONNISTE, geste par geste.\n"
        f"Les gestes : {gestes}.\n"
        "La règle de l'hôtel : " + REGLE_RELAIS["fr"] + "\n"
        "Pour CHAQUE geste, dis s'il était « necessaire » dans cet échange, s'il a été « fait », "
        "cite la réplique du réceptionniste qui le montre (ou vide), et donne un « conseil » d'une "
        f"phrase courte, écrit {LANGUE_BILAN[parle]}, suivi de la phrase à dire, en "
        f"{NOM_LANGUE[apprend]}, entre guillemets.\n"
        "Relève à part toute PROMESSE HORS RÈGLE : le réceptionniste accorde lui-même ce qui revient "
        "au gérant (rabais, frais enlevé, service gratuit, exception) ou ce que personne ne peut "
        "accorder (taxe enlevée, chambre qu'on n'a pas, document faux). C'est éliminatoire. "
        "Transmettre au gérant sans rien promettre n'est PAS une promesse ; refaire une carte-clé "
        "ou expliquer un frais non plus.\n"
        f"Reprends enfin jusqu'à trois phrases du réceptionniste qui gagneraient à être dites "
        f"autrement en {NOM_LANGUE[apprend]} (sens, formule polie du comptoir), jamais pour une "
        "virgule : « dit » (sa phrase) et « mieux » (la même idée, correcte et naturelle).\n"
        f"« resume » : une phrase simple, {LANGUE_BILAN[parle]}, sur ce qui a marché.\n"
        "Réponds UNIQUEMENT en JSON : {\"gestes\": [{\"id\": \"accueil\", \"necessaire\": true, "
        "\"fait\": false, \"citation\": \"…\", \"conseil\": \"…\"}, …], \"promesse\": {\"faite\": "
        "false, \"citation\": \"\"}, \"phrases\": [{\"dit\": \"…\", \"mieux\": \"…\"}], "
        "\"resume\": \"…\"}."
    )


def scenario_serveur(apprend, parle):
    """Le scénario « comptoir-<apprend>-<parle> » tel que /api/jeu-de-role l'attend."""
    cas = {c[0]: {"contexte": c[6]["fr"], "client": c[9], "receptionniste": []} for c in CLIENTS}
    return {
        "cadre": "la réception de l'Hôtel Rive-Claire",
        "contexte_label": "La situation",
        "cas": cas,
        "sujets": [],
        "cloture": "",
        "ouverture": {"receptionniste": OUVERTURE["comptoir"][apprend],
                      "client": OUVERTURE["comptoir"][apprend]},
        "roles": {"client": {"qui": "", "conduite": ""},
                  "receptionniste": {"qui": "", "conduite": ""}},
        "paliers": PALIERS_JEU,
        "bilan": bilan(apprend, parle),
        # Ce que le serveur lit à la place de son gabarit français (server.py).
        "systeme": systeme(apprend),
        "etiquettes": ("CLIENT", "RÉCEPTIONNISTE"),
        "voix": sorted({v for g in VOIX.values() for v in g.values()}),
    }


def scenarios_serveur():
    """Les six directions : {« comptoir-en-fr »: …, …}."""
    return {f"comptoir-{a}-{p}": scenario_serveur(a, p) for a in LANGUES for p in LANGUES if a != p}


def verifier():
    ids = [c[0] for c in CLIENTS]
    assert len(ids) == len(set(ids)) == 8, ids
    gestes = {g["id"] for g in GESTES}
    for ident, genre, nom, paliers, lieu, g, carte, ecran, portrait, faits in CLIENTS:
        assert genre in ("f", "m") and lieu in ("comptoir", "telephone"), ident
        assert set(paliers) <= set(PALIERS) and paliers, ident
        assert set(g) <= gestes and g, ident
        assert all(carte[l] and ecran[l] for l in LANGUES), ident
        assert (lieu == "telephone") == (not portrait), ident
        assert len(faits) >= 4, ident
    # Chaque palier ouvre au moins cinq situations, dont le relais (O4 se pratique partout).
    for p in PALIERS:
        ouverts = [c for c in CLIENTS if p in c[3]]
        assert len(ouverts) >= 5, p
        assert any("relais" in c[5] for c in ouverts), p
    # Chaque geste est en jeu au moins deux fois.
    for g in gestes:
        assert sum(g in c[5] for c in CLIENTS) >= 2, g
    return len(CLIENTS)


if __name__ == "__main__":
    n = verifier()
    s = scenarios_serveur()
    print(f"{n} clients, {len(GESTES)} gestes, {len(s)} scénarios")
    print(s["comptoir-en-fr"]["systeme"]("plainte", "receptionniste", "debutant")[:600])


# Les textes de l'écran du comptoir joué, dans la langue de l'employé.
UI_JEU = {
    "jeu_tit": R("Au comptoir : les clients arrivent", "At the desk: the guests arrive", "En el mostrador: llegan los clientes"),
    "jeu_carte": R("Huit clients, en personne ou au téléphone. Vous leur parlez dans la langue que vous apprenez ; le bilan dit ce que vous avez fait.",
                   "Eight guests, in person or on the phone. You speak to them in the language you are learning; the review tells you what you did.",
                   "Ocho clientes, en persona o por teléfono. Usted les habla en el idioma que aprende; el resumen le dice lo que hizo."),
    "code_aide": R("Le comptoir joué passe par le serveur. Entrez le code que votre formateur vous a donné.",
                   "The desk role-play goes through the server. Enter the code your trainer gave you.",
                   "El mostrador pasa por el servidor. Escriba el código que le dio su formador."),
    "code": R("Code d'accès", "Access code", "Código de acceso"),
    "entrer": R("Entrer", "Enter", "Entrar"),
    "code_refuse": R("Ce code n'est pas accepté. Vérifiez-le avec votre formateur.", "This code is not accepted. Check it with your trainer.",
                     "Este código no es válido. Verifíquelo con su formador."),
    "niveau": R("Niveau des clients", "Guest level", "Nivel de los clientes"),
    "niveau_test": R("proposé par votre test", "suggested by your test", "sugerido por su prueba"),
    "niveau_sans": R("faites d'abord le test, ou choisissez un niveau", "take the test first, or choose a level", "haga primero la prueba, o elija un nivel"),
    "choisir": R("Choisissez un client", "Choose a guest", "Elija un cliente"),
    "au_tel": R("Au téléphone", "On the phone", "Por teléfono"),
    "regle_tit": R("La règle du comptoir", "The desk rule", "La regla del mostrador"),
    "gestes_tit": R("Les gestes du comptoir", "The desk moves", "Los gestos del mostrador"),
    "ecran": R("Ce que dit votre écran", "What your screen says", "Lo que dice su pantalla"),
    "parler": R("Parler", "Speak", "Hablar"),
    "arreter": R("Arrêter", "Stop", "Detener"),
    "ecrire": R("ou écrivez votre réponse…", "or type your answer…", "o escriba su respuesta…"),
    "envoyer": R("Envoyer", "Send", "Enviar"),
    "terminer": R("Terminer", "Finish", "Terminar"),
    "voir_bilan": R("Voir le bilan", "See the review", "Ver el resumen"),
    "sans_lire": R("Écouter sans lire", "Listen without reading", "Escuchar sin leer"),
    "attente": R("Le client parle…", "The guest is speaking…", "El cliente habla…"),
    "vous": R("Vous", "You", "Usted"),
    "client": R("Client", "Guest", "Cliente"),
    "reecouter": R("Réécouter", "Replay", "Volver a escuchar"),
    "voix_indispo": R("La voix du client ne répond pas : lisez sa réplique.", "The guest's voice is not responding: read the line.",
                      "La voz del cliente no responde: lea su frase."),
    "micro_refuse": R("Le micro n'est pas disponible : écrivez votre réponse.", "The microphone is not available: type your answer.",
                      "El micrófono no está disponible: escriba su respuesta."),
    "erreur": R("Le serveur ne répond pas. Réessayez.", "The server is not responding. Try again.", "El servidor no responde. Inténtelo de nuevo."),
    "bilan_tit": R("Le bilan", "The review", "El resumen"),
    "bilan_attente": R("Le bilan se prépare…", "Preparing the review…", "Preparando el resumen…"),
    "fait": R("fait", "done", "hecho"),
    "manque": R("à faire la prochaine fois", "to do next time", "para la próxima vez"),
    "inutile": R("pas nécessaire ici", "not needed here", "no hacía falta aquí"),
    "promesse_tit": R("Promesse hors règle — éliminatoire", "Promise outside the rule — this fails", "Promesa fuera de la regla — es eliminatoria"),
    "sans_promesse": R("Aucune promesse hors règle.", "No promise outside the rule.", "Ninguna promesa fuera de la regla."),
    "phrases_tit": R("Dit autrement", "Said another way", "Dicho de otra forma"),
    "autre": R("Un autre client", "Another guest", "Otro cliente"),
    "rien_dit": R("Vous n'avez rien dit au client : pas de bilan.", "You said nothing to the guest: no review.", "No le dijo nada al cliente: no hay resumen."),
    # L'humeur DITE, pas seulement dessinée (audit E2 de Francœur).
    "hum_neutre_f": R("attend", "is waiting", "espera"), "hum_neutre_m": R("attend", "is waiting", "espera"),
    "hum_contente_f": R("est contente", "is pleased", "está contenta"), "hum_contente_m": R("est content", "is pleased", "está contento"),
    "hum_hesitante_f": R("hésite", "is unsure", "duda"), "hum_hesitante_m": R("hésite", "is unsure", "duda"),
    "hum_impatiente_f": R("s'impatiente", "is getting impatient", "se impacienta"), "hum_impatiente_m": R("s'impatiente", "is getting impatient", "se impacienta"),
    "fin_ok_f": R("repart satisfaite.", "leaves satisfied.", "se va satisfecha."),
    "fin_ok_m": R("repart satisfait.", "leaves satisfied.", "se va satisfecho."),
    "fin_ko_f": R("repart sans être satisfaite.", "leaves unsatisfied.", "se va sin estar satisfecha."),
    "fin_ko_m": R("repart sans être satisfait.", "leaves unsatisfied.", "se va sin estar satisfecho."),
}
