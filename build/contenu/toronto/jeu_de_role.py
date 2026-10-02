"""La semaine jouée d'« Une semaine à Toronto » — l'assistance joue les gens de la ville, en anglais.

Étape 5 (1er oct. 2026). Même forme que le jeu de rôle de Compostelle
(build/contenu/compostelle/jeu_de_role.py) et que le comptoir de l'hôtel : un
scénario qui porte sa propre consigne (`systeme`), parce que le gabarit du
serveur suppose la francisation et le français. Chargé par server.py.

Trois sortes de cas, dans un seul scénario « toronto-en » :
- un cas par LIEU (semaine.py) : la personne du lieu, ce qu'elle sait (FAITS),
  les GESTES que le touriste doit accomplir ; le bilan dit si la carte est gagnée ;
- « maya-N » : le bavardage du jour avec Maya, la Torontoise qui revient ;
- « carte-<lieu> » : la relecture des deux lignes écrites au dos de la carte
  postale (un bilan seul, sans conversation).

Le régime végétarien (O3) est ÉLIMINATOIRE au restaurant et au marché : la carte
ne se gagne pas si le touriste n'a pas dit qu'il ne mange pas de viande avant de
commander, ou s'il a commandé un plat qui en contient ou dont on n'est pas sûr. La
règle est la même que dans les exercices (exercices.py). Il remplace l'allergie le
2 oct. 2026 (décision de Daniel : responsabilité civile).

    python3 build/contenu/toronto/jeu_de_role.py   # vérifie et montre une consigne
"""
import importlib.util, pathlib

_ICI = pathlib.Path(__file__).resolve().parent


def _charger(nom):
    sp = importlib.util.spec_from_file_location(f"toronto_jr_{nom}", _ICI / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


SE = _charger("semaine")
EX = _charger("exercices")
LIEUX = {l[0]: l for l in SE.LIEUX}
GENS = {g[0]: g for g in SE.GENS}

# Ce que chaque personne sait, et que le touriste ignore. Inventé pour la trousse,
# accordé aux exercices (exercices.py) ; les faits réels changent.
FAITS = {
    "union": ["The subway is downstairs: take the escalator down, then follow the yellow line to the left.",
              "You can tap a credit or debit card at the gate; no ticket needed. One ride is $3.30.",
              "The train to the hotel's street, King, is one stop north, toward Finch."],
    "hotel": ["The guest has a reservation for three nights, a queen room, under the name they give (ask them to spell it).",
              "Check-in is at 3 p.m.; if they arrive early, the room may not be ready, but you can keep their bags.",
              "There is a $100 deposit held on the card, released at check-out. Do not end the check-in until the guest has handed you a card for the deposit.",
              "Breakfast is included, on the second floor, from 6:30 to 10. Do not mention breakfast or Wi-Fi unless the guest asks.",
              "The Wi-Fi network is 'Guest' and the password is on the key-card sleeve."],
    "cafe": ["Sizes: small, medium, large. Muffins: blueberry is sold out; there is banana and chocolate.",
             "A medium coffee is $2.75, a muffin $3.25, plus tax. You ask: for here or to go? Anything else?",
             "Payment at the terminal: tap; the terminal suggests a tip."],
    "tour": ["Timed entry: the next available time is 4:15 p.m.; 4:30 is full.",
             "Adult ticket $47, plus tax; seniors (65+) get 20% off on weekdays only.",
             "Bags bigger than a backpack go to the coat check.", "Today is Tuesday."],
    "marche": ["Peameal bacon sandwich $10, plus tax. Cheese is sold by the pound.",
               "This counter is cash only; there is a cash machine by the door.",
               "The market is closed on Mondays.",
               "Grilled cheese sandwich $8, plus tax: no meat at all.",
               "The soup of the day, by the register, is split pea soup made with ham. You never mention the ham unless the customer says they don't eat meat or asks."],
    "kensington": ["The Spadina streetcar is two blocks east; take it southbound to get back downtown.",
                   "It is a five-minute walk. You are a retired man who loves to give directions."],
    "iles": ["The ferry is $9.57 return for an adult. Bikes are $15 an hour and you need a piece of ID.",
             "The last ferry back to the city tonight is at 11:45 p.m.; in winter only Ward's Island is served."],
    "pharmacie": ["For a sunburn: an after-sun cream, twice a day, and stay out of the sun for a couple of days.",
                  "For a headache: ibuprofen or acetaminophen, no prescription needed; not with alcohol.",
                  "If there is a fever or blisters, go to a walk-in clinic."],
    "resto": ["Tonight: the penne with tomato sauce (no meat at all), the mushroom risotto (made with chicken stock: it has meat), the chicken parmigiana (meat). When you list the dishes, name them as on the menu; just don't add any warning about meat or broth.",
              "Soup of the day: minestrone (you are not sure whether the broth is vegetable or chicken). Dessert: tiramisu or ice cream.",
              "You never mention meat, broth or vegetarian options unless the customer says they don't eat meat or asks. If a customer orders a dish, you take the order as asked.",
              "If a customer says they are vegetarian, you answer honestly; if you are not sure, you say you will check with the kitchen.",
              "Separate bills are fine. Tip is not included."],
    "depart": ["The bill is $512.40 and includes a $14 minibar charge. Show the total; do not mention the minibar unless the guest does. It is a mistake if the guest says they did not use the minibar; you remove it.",
               "The UP Express to the airport leaves from Union Station, upper level, every 15 minutes; about 25 minutes to Pearson."],
}

# Les gestes qui font gagner la carte : ce que le touriste doit OBTENIR ou DIRE.
GESTES = {
    "union": ["trouver où est le métro", "savoir comment payer son passage"],
    "hotel": ["épeler lui-même son nom, lettre par lettre", "comprendre le dépôt ou l'heure de la chambre", "demander une information (déjeuner ou wifi)"],
    "cafe": ["commander une boisson avec sa grandeur", "répondre à « for here or to go? » ou à « anything else? »"],
    "tour": ["demander des billets", "comprendre l'heure de montée"],
    "marche": ["commander", "comprendre comment payer (comptant seulement)", "demander si la soupe contient de la viande, et ne pas en prendre"],
    "kensington": ["demander son chemin", "comprendre la direction (est, sud, à pied)"],
    "iles": ["louer un vélo ou acheter le passage", "comprendre l'heure du dernier traversier"],
    "pharmacie": ["décrire son problème", "comprendre comment prendre le produit"],
    "resto": ["dire en anglais « I'm vegetarian » ou « I don't eat meat » AVANT de commander", "ne pas commander un plat qui contient de la viande ou dont la serveuse n'est pas sûre", "commander un plat"],
    "depart": ["signaler poliment l'erreur sur la facture", "comprendre ce qu'on fait de la somme", "demander comment aller à l'aéroport (UP Express)"],
}
# La formule modèle du bilan, propre à chaque lieu (tour 2 : la formule du restaurant ne vaut pas au marché).
FORMULE = {"resto": "Before I order: I'm vegetarian, I don't eat meat.",
           "marche": "I'm vegetarian. Does the soup have any meat in it?"}
# La règle affichée avant de jouer, par lieu (la règle du restaurant ne vaut pas au marché).
REGLE_ELIM = {"resto": "dites en anglais que vous ne mangez pas de viande avant de commander, et ne demandez aucun plat qui en contient (même un bouillon de poulet) ou dont on n’est pas sûr.",
              "marche": "demandez en anglais si la soupe contient de la viande, et n’en prenez pas s’il y en a ou s’il y a un doute ; ne commandez rien qui contient de la viande."}
ELIMINATOIRE = {
    "resto": ("le touriste n'a pas dit EN ANGLAIS qu'il ne mange pas de viande (« I'm vegetarian ») avant la première "
              "commande d'un plat, ou il a DEMANDÉ un plat qui contient de la viande (y compris un bouillon de viande, "
              "comme le risotto au bouillon de poulet, ou le poulet) ou dont la serveuse n'est pas sûre — même si le "
              "touriste s'est repris ensuite"),
    "marche": ("le touriste a pris ou demandé de la soupe sans avoir demandé EN ANGLAIS si elle contient de la viande, "
               "ou l'a prise après avoir appris qu'elle est faite avec du jambon, ou a commandé un plat qui contient de "
               "la viande (comme le sandwich au bacon de dos)"),
}
# Ce que la carte du touriste lui dit avant d'entrer (en français).
CONSIGNE = {
    "union": "Vous arrivez en train à Union Station. Trouvez le métro et demandez comment payer votre passage.",
    "hotel": "Vous arrivez à l'hôtel, rue King. Vous avez une réservation à votre nom. Faites-vous enregistrer.",
    "cafe": "C'est le matin, au café. Commandez à boire (et à manger si vous voulez), puis payez.",
    "tour": "Au guichet de la tour CN. Achetez deux billets pour cet après-midi.",
    "marche": "Au marché St. Lawrence, au comptoir. Vous êtes végétarien ou végétarienne : vous ne mangez pas de viande. Commandez un sandwich, voyez si la soupe du jour près de la caisse est sans viande, et payez.",
    "kensington": "Vous ne trouvez plus votre chemin dans Kensington. Demandez comment rejoindre le tramway de Spadina pour rentrer au centre-ville.",
    "iles": "Au quai du traversier. Vous voulez aller sur les îles, et louer un vélo là-bas.",
    "pharmacie": "Lendemain des îles : un coup de soleil sur les épaules, et un mal de tête. Allez à la pharmacie.",
    "resto": "Au restaurant, le soir. Vous êtes végétarien ou végétarienne : vous ne mangez pas de viande. Commandez votre souper.",
    "depart": "Dernier jour, à la réception. Il y a 14 $ de minibar sur votre facture ; vous n'avez rien pris. Puis demandez comment aller à l'aéroport.",
}
# Le bavardage avec Maya : (cas, jour, lieu où on la croise, sujet).
MAYA = [
    ("maya-1", "Jour 2", "au café", "you meet the tourist for the FIRST time (never say 'again'); where they are from, what they do, how long they are staying"),
    ("maya-2", "Jour 3", "au marché", "food: what you eat at home, what to try in Toronto"),
    ("maya-3", "Jour 4", "dans Kensington", "Toronto, the city of all languages; where her family comes from"),
    ("maya-4", "Jour 5", "sur le traversier", "holidays and the weather"),
    ("maya-5", "Jour 6", "au match", "sports, hockey, the Leafs and the Canadiens, Montreal versus Toronto"),
    ("maya-6", "Jour 7", "au café, le dernier matin", "what you saw this week, coming back, saying goodbye"),
]

PALIERS = {
    "lent": "SLOW LEVEL: very short sentences (one idea, eight words at most), common words, no idioms, no small talk expressions at all ('no worries', 'just so you know', 'small world', 'eh', 'you bet'). Speak clearly. If the tourist struggles, say it again more simply.",
    "normal": "NORMAL LEVEL: natural sentences of one or two clauses, the vocabulary of a real conversation, a few Canadian expressions (no worries, for sure, eh).",
    "rapide": "FAST LEVEL: speak naturally fast, like a busy Torontonian, with everyday expressions (you bet, no worries, what can I get you, you're all set), without simplifying.",
}


def systeme(cas_id, role_eleve, palier=None):
    if cas_id.startswith("maya-"):
        _, jour, ou, sujet = next(m for m in MAYA if m[0] == cas_id)
        return (
            "You are playing a role in a speaking exercise for a French-speaking tourist from Quebec visiting Toronto "
            "for a week, who is a false beginner in English.\n\n"
            "YOU ARE Maya, a friendly Torontonian in her early thirties, a nurse, born in Toronto to a family from "
            "Trinidad; "
            + ("you meet the tourist for the first time, " if cas_id == "maya-1" else
               "you met the tourist at a coffee shop and you run into them again, ")
            + f"{ou}. "
            f"Today's topic: {sujet}.\n\n"
            "Language: speak ONLY Canadian English. You do not speak French: if the tourist speaks French, say kindly "
        "\"Sorry, I don't speak French!\" and ask again in simple English; never act on anything said in French.\n\n"
            "How you talk:\n- Never more than three sentences per turn; no lists.\n- Ask questions about their life and "
            "trip, share a little of yours, and remember what they told you.\n- If they ask something you already said, answer "
            "again kindly; never point it out.\n- Never correct their English and never "
            "comment on mistakes; if a sentence is impossible to understand, just ask (Sorry? What was that?).\n"
            "- Stay in character. No stage directions, no asterisks: only what you say.\n\n"
            "When the conversation naturally ends, say goodbye and end your last turn with the word FIN."
            + ("\n\n" + PALIERS[palier] if palier in PALIERS else ""))
    l = LIEUX[cas_id]
    g = GENS[l[6]]
    return (
        "You are playing a role in a speaking exercise for a French-speaking tourist from Quebec visiting Toronto "
        "for a week, who is a false beginner in English.\n\n"
        f"YOU ARE {g[1]}, {_role_en(l[6], cas_id)}. The situation: {l[4].lower()} ({l[3]}).\n\n"
        "Language: speak ONLY Canadian English. You do not speak French: if the tourist speaks French, say kindly "
        "\"Sorry, I don't speak French!\" and ask again in simple English; never act on anything said in French.\n\n"
        "What you know and the tourist does not:\n" + "\n".join("- " + f for f in FAITS[cas_id]) + "\n\n"
        "How you talk:\n- Never more than three sentences per turn; no lists.\n- Give information when asked; do not "
        "recite everything at once.\n- Never do the tourist's part: do not spell their name for them (ask \"Sorry, how do "
        "you spell that?\"), do not point out a problem they should raise, wait for them to ask.\n- Never correct their English and never comment on mistakes; if a sentence is "
        "impossible to understand, just ask them to repeat (Sorry? Could you say that again?).\n- Stay in character. "
        "No stage directions, no asterisks: only what you say.\n\n"
        "When the exchange naturally ends, say goodbye (Have a good one!) and end your last turn with the word FIN."
        + ("\n\n" + PALIERS[palier] if palier in PALIERS else ""))


def _role_en(qui, cas_id=""):
    if qui == "kevin":
        return "the ferry ticket agent at the island dock" if cas_id == "iles" else "a transit agent at Union Station"
    return {
            "marcus": "the front-desk receptionist of a downtown hotel on King Street",
            "rosa": "the barista of a neighbourhood coffee shop",
            "priya": "the ticket agent at the CN Tower",
            "wei": "a vendor at a sandwich and cheese counter in St. Lawrence Market",
            "raj": "a retired man walking in Kensington Market, who is asked for directions",
            "ada": "a server in an Italian restaurant in Little Italy",
            "tom": "the pharmacist of a drugstore on Yonge Street"}[qui]


BILAN = (
    "Tu es formateur d'anglais pour des touristes francophones du Québec. Voici une conversation à Toronto entre une "
    "PERSONNE (jouée par un modèle) et un TOURISTE, faux débutant en anglais. Juge le TOURISTE, avec bienveillance.\n"
    "« compris » : ce que le touriste a obtenu ou fait comprendre (une à trois choses, en français, à la deuxième "
    "personne : « Vous avez… »).\n"
    "« phrases » : jusqu'à trois phrases du touriste FAUTIVES ou peu naturelles en anglais du Canada — jamais une phrase "
    "correcte, même si on pourrait la tourner autrement, jamais pour une virgule ni une majuscule : « dit » (sa phrase) et "
    "« mieux » (la même idée, correcte, naturelle et courte). Liste vide si tout était juste.\n"
    "Ne reproche au touriste une réponse « à côté » que si la réplique de la PERSONNE juste avant le montre ; relis l'ordre "
    "des répliques avant de l'écrire.\n"
    "« conseil » : une phrase en français, et une formule utile en anglais entre guillemets.\n"
    "« resume » : une phrase simple, en français, adressée au touriste en le vouvoyant.\n"
    "« dit » est copié MOT POUR MOT d'une réplique du TOURISTE ; « mieux » dit exactement la même idée, sans rien "
    "ajouter. Une formule courte et juste n'est jamais fautive : « Thank you, bye. », « Yes. », « OK. », « No. ».\n"
    "« mieux » est DIFFÉRENT de « dit » et garde le sens exact ; si le sens est incertain, ne corrige pas. « I am » et "
    "« I'm » sont justes tous les deux : « I am a teacher. », « What do you have tonight? » ne se corrigent pas. Ne "
    "peaufine jamais la phrase qui commet une erreur éliminatoire.\n"
    "Une réplique en FRANÇAIS ne compte pour AUCUN geste : le but est de se débrouiller en anglais.\n"
    "Un geste ne compte que si le TOURISTE l'a fait LUI-MÊME, en anglais, dans ses répliques ; ce que la PERSONNE a dit "
    "ou fait à sa place ne compte pas. « Comprendre » se prouve : le touriste reformule, confirme (« 3 p.m.? ») ou agit "
    "en conséquence ; un « OK » seul ne suffit pas. « compris » ne contredit jamais « gestes ».\n"
    "Les répliques du TOURISTE viennent souvent d'un micro qui ne ponctue pas : ne corrige jamais la ponctuation ni "
    "les majuscules, et n'en parle jamais.\n"
    "Vouvoie dans TOUS les champs, jamais de tutoiement. Aucun verbe pronominal accordé : « Vous avez corrigé "
    "l'erreur », jamais « Vous vous êtes rattrapé ». Quand tu parles de l'anglais, dis « le passé (I went) », jamais "
    "« passé simple ».\n"
    "Tu ne connais PAS le genre du touriste : en français, n'écris aucun participe ni adjectif qui s'accorde à lui. Écris "
    "« Vous avez visité », jamais « Vous êtes allé » ; « Vous enseignez », jamais « Vous êtes enseignant » ; « Vous avez "
    "dit », jamais « Vous êtes prêt ».\n"
    "Toute formule anglaise que tu proposes doit être irréprochable et courte.\n"
)


def _accord(genre):
    """Le genre choisi dans la page (« f », « m ») ; sinon la règle neutre de la consigne."""
    if genre == "f":
        return "\nLa personne qui apprend est une FEMME : en français, accorde au féminin (« allée », « prête », « arrivée »)."
    if genre == "m":
        return "\nLa personne qui apprend est un HOMME : en français, accorde au masculin."
    return ""


def bilan(cas_id, genre=None):
    return _bilan(cas_id) + _accord(genre)


def _bilan(cas_id):
    if cas_id.startswith("carte-"):
        l = LIEUX[cas_id[6:]]
        return (
            "Tu es formateur d'anglais pour des touristes francophones du Québec. Le touriste a écrit deux lignes en "
            f"anglais au dos d'une carte postale de {l[3]}, à Toronto, pour un proche. Relis-les avec bienveillance.\n"
            "« compris » : ce que sa carte dit bien (une ou deux choses, en français, à la deuxième personne).\n"
            "« phrases » : jusqu'à deux phrases FAUTIVES — « dit » et « mieux » (la même idée, correcte et naturelle) ; "
            "liste vide si tout est juste. Une phrase correcte ne se corrige pas, même si on pourrait la tourner autrement : "
            "le passé (« It was great ») et le présent (« It is great ») sont justes tous les deux dans une carte. Ne réécris "
            "jamais toute la carte à sa place.\n"
            "« conseil » : une phrase en français, avec une formule de carte postale utile EN ANGLAIS entre guillemets "
            "(« Wish you were here! », « See you soon! ») — la carte est en anglais, jamais une formule française.\n"
            "« dit » est copié mot pour mot de la carte. Vouvoie dans tous les champs, jamais de tutoiement.\n"
            "« resume » : une phrase simple, en français, au vouvoiement. Tu ne connais PAS le genre du touriste : aucun "
            "participe ni adjectif accordé à lui (« Vous avez visité », jamais « Vous êtes allé »).\n"
            "Réponds UNIQUEMENT en JSON : {\"compris\": [\"…\"], \"phrases\": [{\"dit\": \"…\", \"mieux\": \"…\"}], "
            "\"conseil\": \"…\", \"resume\": \"…\"}.")
    if cas_id.startswith("maya-"):
        return (BILAN + "La PERSONNE est Maya, une femme. C'est une conversation libre : « reussi » vaut true si le "
                "touriste a répondu EN ANGLAIS à au moins une question de Maya. Ne compte PAS ses questions (la page "
                "les compte) et ne lui reproche jamais de ne pas avoir répondu à TOUTES les questions : Maya en pose à "
                "chaque tour. Une question redondante compte quand même. Tu peux parler des questions de Maya "
                "(« répondez à sa question… »), mais ne COMPTE jamais les questions du touriste (ni « une », ni « deux », "
                "ni « pas assez »). Écris toujours « reussi », true ou false.\n"
                "« questions » : cite MOT POUR MOT chaque réplique (ou partie de réplique) du TOURISTE qui est une vraie question "
                "posée à Maya sur elle ou sa vie, même sans point d'interrogation (« you like poutine », « and you »). N'y mets "
                "jamais une demande de répéter ou d'expliquer (« Sorry? », « What? », « Can you repeat? ») ni une politesse.\n"
                "Réponds UNIQUEMENT en JSON : {\"compris\": [\"…\"], \"phrases\": [{\"dit\": \"…\", \"mieux\": \"…\"}], "
                "\"questions\": [\"…\"], \"conseil\": \"…\", \"resume\": \"…\", \"reussi\": true}.")
    l = LIEUX[cas_id]; g = GENS[l[6]]
    gestes = GESTES[cas_id]
    elim = ELIMINATOIRE.get(cas_id)
    return (BILAN + f"La PERSONNE jouée s'appelle {g[1]} ({g[3].lower()}). N'écris dans « compris » que ce que le "
            "touriste a réellement dit ou obtenu ; n'invente rien.\n"
            "« gestes » : pour CHACUN de ces gestes, dans cet ordre, dis s'il a été accompli : "
            + " ; ".join(f"« {x} »" for x in gestes) + ".\n"
            + (f"ÉLIMINATOIRE : « reussi » vaut false si {elim}, quoi qu'il arrive par ailleurs ; dis-le dans "
               "« conseil ».\n" if elim else "")
            + "« reussi » vaut true si tous les gestes sont accomplis" + (" et que l'éliminatoire est évité" if elim else "")
            + ". Écris toujours « reussi », true ou false.\n"
            + (f"Formule modèle pour dire qu'on ne mange pas de viande : « {FORMULE[cas_id]} »\n" if cas_id in FORMULE else "")
            + "Réponds UNIQUEMENT en JSON : {\"compris\": [\"…\"], \"phrases\": [{\"dit\": \"…\", \"mieux\": \"…\"}], "
            "\"gestes\": [{\"geste\": \"…\", \"fait\": true}], \"conseil\": \"…\", \"resume\": \"…\", \"reussi\": true}.")


# Les voix de /api/voix (azure_voix.py, rôles toronto_*) : liste blanche du scénario.
VOIX = ["toronto_" + v for v in ("clara", "liam", "andrew", "harper", "aarti", "arjun", "rosa", "sam", "ezinne")]


def scenario_serveur():
    cas = {}
    for k, l in LIEUX.items():
        cas[k] = {"contexte": l[4], "client": FAITS[k], "touriste": []}
        cas["carte-" + k] = {"contexte": "La carte postale", "client": [], "touriste": []}
    for m in MAYA:
        cas[m[0]] = {"contexte": "Avec Maya", "client": [], "touriste": []}
    return {
        "cadre": "une semaine à Toronto",
        "contexte_label": "La situation",
        "cas": cas, "sujets": [], "cloture": "",
        "ouverture": {"touriste": "Hi!", "client": "Hi!"},
        "roles": {"client": {"qui": "", "conduite": ""}, "touriste": {"qui": "", "conduite": ""}},
        "paliers": PALIERS,
        "bilan": bilan,
        # Le modèle de conversation, comme le comptoir de l'hôtel : le petit modèle
        # accordait au masculin et corrigeait des phrases justes (essai du 1er oct. 2026).
        "bilan_modele": "conversation",
        "bilan_max": 2000,
        "systeme": systeme,
        "etiquettes": ("PERSONNE", "TOURISTE"),
        "voix": VOIX,
    }


def scenarios_serveur():
    return {"toronto-en": scenario_serveur()}


def verifier():
    assert set(FAITS) == set(LIEUX) == set(GESTES) == set(CONSIGNE), "un lieu sans faits, gestes ou consigne"
    for k in LIEUX:
        assert GESTES[k], k
    assert "viande" in CONSIGNE["resto"] and "resto" in ELIMINATOIRE, "la viande reste éliminatoire au restaurant"
    assert "marche" in ELIMINATOIRE and "viande" in CONSIGNE["marche"], "et au marché"
    for c in [*LIEUX, *("carte-" + k for k in LIEUX), *(m[0] for m in MAYA)]:
        assert bilan(c), c
    for c in [*LIEUX, *(m[0] for m in MAYA)]:
        assert "FIN" in systeme(c, "touriste", "lent"), c
    return True


if __name__ == "__main__":
    verifier()
    s = scenarios_serveur()["toronto-en"]
    print(len(s["cas"]), "cas")
    print(systeme("resto", "touriste", "normal")[:700])
