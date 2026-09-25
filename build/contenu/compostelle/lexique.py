"""Le lexique d'« En route vers Compostelle » — l'espagnol du pèlerin francophone.

    python3 build/contenu/compostelle/lexique.py      # compte et vérifie

UNE SOURCE, UN TUPLE : (id, planche, es, fr, dessin, note)

- es : l'espagnol d'ESPAGNE (castillan), décision du 25 sept. 2026 — móvil,
  zumo, billete, coger. Ce qui est entre parenthèses est une glose, pas un
  texte à dire.
- fr : le français du QUÉBEC, celui de l'apprenant : le déjeuner est le repas
  du matin, le dîner celui du midi, le souper celui du soir ; une rôtie.
- dessin : `croquis` (engendré par build/compostelle_croquis.py),
  `picto:<nom>` (dessiné en SVG dans la page : flèches, horloges), `""` (sans
  image — une formule, une phrase : elle se joue à l'oreille).
- note : une note qui commence par `PIÈGE` est un faux ami ; sa phrase de
  contexte vit dans PIEGES, plus bas (règle payée à l'hôtel : jamais un faux
  ami montré seul, il est souvent vrai aussi).

Le contenu est INVENTÉ pour la trousse, jamais recopié d'un guide ou d'un
manuel.
"""

PLANCHES = [
    ("camino", "Le chemin", "El camino"),
    ("albergue", "L'albergue", "El albergue"),
    ("comer", "Manger et boire", "Comer y beber"),
    ("horas", "Les heures d'Espagne", "Las horas"),
    ("comprar", "Acheter", "Comprar"),
    ("cuerpo", "Le corps et la pharmacie", "El cuerpo y la farmacia"),
    ("tiempo", "Le temps qu'il fait", "El tiempo"),
    ("moverse", "Se déplacer", "Moverse"),
    ("gente", "Les gens, la politesse", "La gente"),
    ("visitar", "Visiter", "Visitar"),
    ("peregrinos", "Entre pèlerins", "Entre peregrinos"),
]

LEXIQUE = [
    # --- Le chemin -----------------------------------------------------------
    ("flecha", "camino", "la flecha amarilla", "la flèche jaune", "croquis", ""),
    ("concha", "camino", "la concha", "la coquille", "croquis", ""),
    ("mojon", "camino", "el mojón", "la borne (du chemin)", "croquis", ""),
    ("credencial", "camino", "la credencial", "la credencial (le carnet du pèlerin)", "croquis", ""),
    ("sello", "camino", "el sello", "le tampon", "croquis", ""),
    ("baston", "camino", "el bastón", "le bâton", "croquis", ""),
    ("mochila", "camino", "la mochila", "le sac à dos", "croquis", ""),
    ("botas", "camino", "las botas", "les bottes de marche", "croquis", ""),
    ("fuente", "camino", "la fuente", "la fontaine", "croquis", ""),
    ("puente", "camino", "el puente", "le pont", "croquis", ""),
    ("cruce", "camino", "el cruce", "le croisement", "croquis", ""),
    ("subida", "camino", "la subida", "la montée", "croquis", ""),
    ("bajada", "camino", "la bajada", "la descente", "croquis", ""),
    ("peregrino", "camino", "el peregrino, la peregrina", "le pèlerin, la pèlerine", "croquis", ""),
    ("izquierda", "camino", "a la izquierda", "à gauche", "picto:gauche", ""),
    ("derecha", "camino", "a la derecha", "à droite", "picto:droite", ""),
    ("recto", "camino", "todo recto", "tout droit", "picto:droit", ""),
    ("etapa", "camino", "la etapa", "l'étape", "", ""),
    ("pueblo", "camino", "el pueblo", "le village", "croquis", ""),

    # --- L'albergue ----------------------------------------------------------
    ("albergue", "albergue", "el albergue", "l'albergue (le gîte des pèlerins)", "croquis", ""),
    ("litera", "albergue", "la litera", "le lit superposé", "croquis", ""),
    ("arriba", "albergue", "arriba", "en haut", "picto:haut", ""),
    ("abajo", "albergue", "abajo", "en bas", "picto:bas", ""),
    ("saco", "albergue", "el saco de dormir", "le sac de couchage", "croquis", ""),
    ("almohada", "albergue", "la almohada", "l'oreiller", "croquis", ""),
    ("manta", "albergue", "la manta", "la couverture", "croquis", ""),
    ("ducha", "albergue", "la ducha", "la douche", "croquis", ""),
    ("toalla", "albergue", "la toalla", "la serviette", "croquis", ""),
    ("taquilla", "albergue", "la taquilla", "le casier", "croquis", ""),
    ("lavadora", "albergue", "la lavadora", "la laveuse", "croquis", ""),
    ("secadora", "albergue", "la secadora", "la sécheuse", "croquis", ""),
    ("tendedero", "albergue", "el tendedero", "la corde à linge", "croquis", ""),
    ("enchufe", "albergue", "el enchufe", "la prise de courant", "croquis", ""),
    ("cargador", "albergue", "el cargador", "le chargeur", "croquis", ""),
    ("tapones", "albergue", "los tapones", "les bouchons d'oreilles", "croquis", ""),
    ("hospitalero", "albergue", "el hospitalero, la hospitalera", "la personne qui tient l'albergue", "", ""),
    ("completo", "albergue", "completo", "complet", "", ""),
    ("donativo", "albergue", "el donativo", "le don (on donne ce qu'on veut)", "", ""),
    ("pension", "albergue", "la pensión, el hostal", "la pension, le petit hôtel", "", ""),
    ("quedan", "albergue", "¿Quedan camas?", "Reste-t-il des lits ?", "", ""),

    # --- Manger et boire -----------------------------------------------------
    ("desayuno", "comer", "el desayuno", "le déjeuner (le repas du matin)", "", ""),
    ("comida", "comer", "la comida", "le dîner (le repas du midi)",
     "", "PIÈGE : en Espagne, la comida est le repas de midi, vers 14 h — notre dîner. Et « comida » veut aussi dire la nourriture."),
    ("cena", "comer", "la cena", "le souper",
     "", "PIÈGE : la cena, c'est le repas du soir, vers 21 h. Rien à voir avec la Cène."),
    ("menu_peregrino", "comer", "el menú del peregrino", "le menu du pèlerin (entrée, plat, dessert, pain, vin)", "", ""),
    ("primero", "comer", "de primero", "en entrée", "", ""),
    ("segundo", "comer", "de segundo", "comme plat principal", "", ""),
    ("postre", "comer", "el postre", "le dessert", "croquis", ""),
    ("carta", "comer", "la carta", "le menu (la liste des plats)",
     "", "PIÈGE : la carta est la liste des plats ; el menú est le menu du jour à prix fixe. La carte de crédit, c'est la tarjeta."),
    ("cafe_leche", "comer", "un café con leche", "un café au lait", "croquis", ""),
    ("cortado", "comer", "un cortado", "un espresso avec un nuage de lait", "croquis", ""),
    ("zumo", "comer", "un zumo de naranja", "un jus d'orange", "croquis", ""),
    ("agua", "comer", "una botella de agua", "une bouteille d'eau", "croquis", ""),
    ("cana", "comer", "una caña", "une petite bière en fût", "croquis", ""),
    ("vino", "comer", "un vino tinto", "un verre de vin rouge", "croquis", ""),
    ("tostada", "comer", "una tostada", "une rôtie", "croquis", ""),
    ("mantequilla", "comer", "la mantequilla", "le beurre",
     "croquis", "PIÈGE : « burro » ressemble à beurre, mais c'est un âne."),
    ("tortilla", "comer", "la tortilla", "l'omelette espagnole (aux pommes de terre)", "croquis", ""),
    ("bocadillo", "comer", "un bocadillo", "un sandwich sur baguette", "croquis", ""),
    ("pintxo", "comer", "un pintxo", "une bouchée sur pain, au comptoir", "croquis", ""),
    ("pulpo", "comer", "el pulpo", "la pieuvre (le poulpe)", "croquis", ""),
    ("pan", "comer", "el pan", "le pain", "croquis", ""),
    ("vaso", "comer", "un vaso", "un verre",
     "croquis", "PIÈGE : un vaso est un verre à boire ; un vase se dit un jarrón."),
    ("cuenta", "comer", "la cuenta", "l'addition", "", ""),
    ("propina", "comer", "la propina", "le pourboire",
     "", "PIÈGE : la propina n'a rien de propre : c'est le pourboire."),
    ("alergico", "comer", "soy alérgico, soy alérgica", "je suis allergique", "", ""),
    ("sin_gluten", "comer", "sin gluten", "sans gluten", "", ""),
    ("vegetariano", "comer", "vegetariano, vegetariana", "végétarien, végétarienne", "", ""),
    ("frutos_secos", "comer", "los frutos secos", "les noix (les fruits à coque)", "croquis", ""),

    # --- Les heures d'Espagne ------------------------------------------------
    ("a_que_hora", "horas", "¿A qué hora…?", "À quelle heure… ?", "", ""),
    ("abierto", "horas", "abierto", "ouvert", "", ""),
    ("cerrado", "horas", "cerrado", "fermé", "", ""),
    ("manana", "horas", "mañana", "demain",
     "", "PIÈGE : mañana veut dire demain… et « por la mañana », le matin. « Mañana por la mañana » : demain matin."),
    ("por_la_tarde", "horas", "por la tarde", "l'après-midi", "", ""),
    ("por_la_noche", "horas", "por la noche", "le soir, la nuit", "", ""),
    ("siesta", "horas", "la siesta", "la sieste", "", ""),
    ("hora_siete", "horas", "a las siete", "à 7 h", "picto:h7", ""),
    ("hora_ocho_media", "horas", "a las ocho y media", "à 8 h 30", "picto:h830", ""),
    ("hora_diez", "horas", "a las diez", "à 10 h", "picto:h10", ""),
    ("hora_dos", "horas", "a las dos", "à 2 h (à 14 h)", "picto:h2", ""),

    # --- Acheter -------------------------------------------------------------
    ("tienda", "comprar", "la tienda", "le magasin, l'épicerie", "", ""),
    ("supermercado", "comprar", "el supermercado", "le supermarché", "", ""),
    ("panaderia", "comprar", "la panadería", "la boulangerie", "", ""),
    ("cajero", "comprar", "el cajero automático", "le guichet automatique", "croquis", ""),
    ("efectivo", "comprar", "en efectivo", "comptant (en argent)", "croquis", ""),
    ("tarjeta", "comprar", "la tarjeta", "la carte (de crédit, de débit)", "croquis", ""),
    ("cuanto", "comprar", "¿Cuánto cuesta?", "Combien ça coûte ?", "", ""),
    ("bolsa", "comprar", "la bolsa", "le sac", "croquis", ""),
    ("fruta", "comprar", "la fruta", "les fruits", "croquis", ""),
    ("platano", "comprar", "el plátano", "la banane", "croquis", ""),
    ("queso", "comprar", "el queso", "le fromage", "croquis", ""),
    ("jamon", "comprar", "el jamón", "le jambon", "croquis", ""),
    ("kilo", "comprar", "un kilo, medio kilo", "un kilo, un demi-kilo", "", ""),

    # --- Le corps et la pharmacie ------------------------------------------
    ("farmacia", "cuerpo", "la farmacia", "la pharmacie", "croquis", ""),
    ("ampolla", "cuerpo", "la ampolla", "l'ampoule (au pied)", "croquis", ""),
    ("pie", "cuerpo", "el pie", "le pied", "croquis", ""),
    ("rodilla", "cuerpo", "la rodilla", "le genou", "croquis", ""),
    ("tobillo", "cuerpo", "el tobillo", "la cheville", "croquis", ""),
    ("espalda", "cuerpo", "la espalda", "le dos", "croquis", ""),
    ("hombro", "cuerpo", "el hombro", "l'épaule", "croquis", ""),
    ("tirita", "cuerpo", "la tirita", "le pansement", "croquis", ""),
    ("aguja", "cuerpo", "la aguja y el hilo", "l'aiguille et le fil", "croquis", ""),
    ("crema", "cuerpo", "la crema", "la crème", "croquis", ""),
    ("crema_solar", "cuerpo", "la crema solar", "la crème solaire", "croquis", ""),
    ("ibuprofeno", "cuerpo", "el ibuprofeno", "l'ibuprofène", "", ""),
    ("me_duele", "cuerpo", "me duele…, me duelen…", "j'ai mal à…", "", ""),
    ("tendinitis", "cuerpo", "la tendinitis", "la tendinite", "", ""),
    ("constipado", "cuerpo", "estoy constipado, estoy constipada", "je suis enrhumé, enrhumée",
     "", "PIÈGE : constipado veut dire enrhumé ! Constipé se dit estreñido."),
    ("guardia", "cuerpo", "la farmacia de guardia", "la pharmacie de garde", "", ""),
    ("centro_salud", "cuerpo", "el centro de salud", "la clinique (le centre de santé)", "", ""),
    ("emergencias", "cuerpo", "el 112", "le 112 (les urgences, partout en Europe)", "", ""),

    # --- Le temps qu'il fait -------------------------------------------------
    ("lluvia", "tiempo", "la lluvia", "la pluie", "croquis", ""),
    ("sol", "tiempo", "el sol", "le soleil", "croquis", ""),
    ("calor", "tiempo", "hace calor", "il fait chaud", "", ""),
    ("frio", "tiempo", "hace frío", "il fait froid", "", ""),
    ("niebla", "tiempo", "la niebla", "le brouillard", "croquis", ""),
    ("viento", "tiempo", "el viento", "le vent", "croquis", ""),
    ("barro", "tiempo", "el barro", "la boue", "croquis", ""),
    ("chubasquero", "tiempo", "el chubasquero", "l'imperméable", "croquis", ""),
    ("gorra", "tiempo", "la gorra", "la casquette", "croquis", ""),

    # --- Se déplacer ---------------------------------------------------------
    ("autobus", "moverse", "el autobús", "l'autobus", "croquis", ""),
    ("taxi", "moverse", "el taxi", "le taxi", "croquis", ""),
    ("parada", "moverse", "la parada", "l'arrêt", "", ""),
    ("billete", "moverse", "el billete", "le billet", "", ""),
    ("transporte", "moverse", "el transporte de mochilas", "le transport des sacs (d'une étape à l'autre)", "croquis", ""),
    ("salida", "moverse", "la salida", "la sortie",
     "", "PIÈGE : la sortie, c'est la salida. « El éxito », c'est le succès !"),

    # --- Les gens, la politesse ---------------------------------------------
    ("buenos_dias", "gente", "buenos días", "bonjour (le matin)", "", ""),
    ("buenas_tardes", "gente", "buenas tardes", "bonjour (l'après-midi et jusqu'au souper)", "", ""),
    ("buenas_noches", "gente", "buenas noches", "bonsoir, bonne nuit", "", ""),
    ("buen_camino", "gente", "¡Buen Camino!", "Bon chemin ! (le salut des pèlerins)", "", ""),
    ("vale", "gente", "vale", "d'accord, correct", "", ""),
    ("perdone", "gente", "perdone, perdona", "pardon, excusez-moi", "", ""),
    ("no_entiendo", "gente", "no entiendo", "je ne comprends pas", "", ""),
    ("despacio", "gente", "más despacio, por favor", "plus lentement, s'il vous plaît", "", ""),
    ("repetir", "gente", "¿Puede repetir?", "Pouvez-vous répéter ?", "", ""),
    ("como_se_dice", "gente", "¿Cómo se dice…?", "Comment dit-on… ?", "", ""),
    ("lo_siento", "gente", "lo siento", "je suis désolé, désolée", "", ""),
    ("de_nada", "gente", "de nada", "de rien, bienvenue", "", ""),

    # --- Visiter -------------------------------------------------------------
    ("catedral", "visitar", "la catedral", "la cathédrale", "croquis", ""),
    ("iglesia", "visitar", "la iglesia", "l'église", "croquis", ""),
    ("claustro", "visitar", "el claustro", "le cloître", "croquis", ""),
    ("castillo", "visitar", "el castillo", "le château", "croquis", ""),
    ("plaza_mayor", "visitar", "la plaza mayor", "la place principale", "croquis", ""),
    ("vidriera", "visitar", "la vidriera", "le vitrail", "croquis", ""),
    ("mercado", "visitar", "el mercado", "le marché", "croquis", ""),
    ("bodega", "visitar", "la bodega", "la cave à vin", "croquis", ""),
    ("entrada", "visitar", "la entrada", "le billet d'entrée ; l'entrée", "", ""),
    ("horario", "visitar", "el horario", "l'horaire, les heures d'ouverture", "", ""),
    ("visita_guiada", "visitar", "la visita guiada", "la visite guidée", "", ""),
    ("misa", "visitar", "la misa", "la messe", "", ""),
    ("descuento", "visitar", "el descuento para peregrinos", "le tarif réduit des pèlerins", "", ""),

    # --- Entre pèlerins ------------------------------------------------------
    ("de_donde", "peregrinos", "¿De dónde eres?", "D'où viens-tu ?", "", ""),
    ("soy_de", "peregrinos", "Soy de Quebec, de Canadá.", "Je suis du Québec, au Canada.", "", ""),
    ("por_que", "peregrinos", "¿Por qué haces el Camino?", "Pourquoi fais-tu le Chemin ?", "", ""),
    ("desde_donde", "peregrinos", "¿Desde dónde caminas?", "D'où es-tu parti, partie ?", "", ""),
    ("hasta_donde", "peregrinos", "¿Hasta dónde vas hoy?", "Jusqu'où vas-tu aujourd'hui ?", "", ""),
    ("kilometros", "peregrinos", "¿Cuántos kilómetros haces al día?", "Combien de kilomètres fais-tu par jour ?", "", ""),
    ("cansado", "peregrinos", "estoy cansado, estoy cansada", "je suis fatigué, fatiguée", "", ""),
    ("donde_duermes", "peregrinos", "¿Dónde duermes esta noche?", "Où dors-tu ce soir ?", "", ""),
    ("estas_bien", "peregrinos", "¿Estás bien?", "Ça va ? (Tu vas bien ?)", "", ""),
    ("encantado", "peregrinos", "encantado, encantada", "enchanté, enchantée", "", ""),
    ("nos_vemos", "peregrinos", "¡Nos vemos!", "On se revoit ! (À plus tard !)", "", ""),
    ("embarazada", "peregrinos", "me da vergüenza", "je suis gêné, gênée",
     "", "PIÈGE : « estoy embarazada », c'est « je suis enceinte ». Gêné : me da vergüenza."),
]

# Les faux amis, chacun posé dans une phrase du chemin (règle de l'hôtel :
# « a ticket » est aussi une contravention — un faux ami montré seul trompe
# sur ce qu'il trompe). (id, phrase entendue, bonne lecture, fausse lecture,
# second choix, explication)
PIEGES = {
    "comida": ("La comida se sirve a las dos.", "Le dîner est servi à 14 h.",
               "La nourriture est servie à 2 h du matin.", "Le souper est servi à 20 h.",
               "La comida, c'est le repas de midi — servi tard en Espagne, vers 14 h. « A las dos » de l'après-midi."),
    "cena": ("¿A qué hora es la cena?", "À quelle heure est le souper ?",
             "À quelle heure est la messe ?", "À quelle heure est le dîner (le midi) ?",
             "La cena est le repas du soir. La messe se dit la misa."),
    "carta": ("¿Me trae la carta, por favor?", "Vous m'apportez le menu, s'il vous plaît ?",
              "Vous me rapportez ma carte, s'il vous plaît ?", "Vous m'apportez l'addition, s'il vous plaît ?",
              "La carta est la liste des plats. La carte de crédit : la tarjeta. L'addition : la cuenta."),
    "mantequilla": ("¿La tostada, con mantequilla?", "La rôtie, avec du beurre ?",
                    "La rôtie, avec de la moutarde ?", "La rôtie, avec du miel ?",
                    "Mantequilla = beurre. Et si vous dites « burro », vous demandez un âne."),
    "vaso": ("¿Me pone un vaso de agua?", "Vous me servez un verre d'eau ?",
             "Vous me donnez un vase avec de l'eau ?", "Vous me servez une bouteille d'eau ?",
             "Un vaso est un verre. Une bouteille : una botella."),
    "propina": ("La propina no es obligatoria.", "Le pourboire n'est pas obligatoire.",
                "La propreté n'est pas obligatoire.", "La réservation n'est pas obligatoire.",
                "La propina, c'est le pourboire. En Espagne, on laisse souvent un peu de monnaie, rien de plus."),
    "manana": ("Mañana salimos a las siete.", "Demain, on part à 7 h.",
               "Ce matin, on part à 7 h.", "Demain, on arrive à 7 h.",
               "Mañana seul veut dire demain. Le matin : por la mañana. Et salir = partir, sortir."),
    "constipado": ("Estoy un poco constipado, ¿tiene algo?", "Je suis un peu enrhumé, avez-vous quelque chose ?",
                   "Je suis un peu constipé, avez-vous quelque chose ?", "Je suis un peu fatigué, avez-vous quelque chose ?",
                   "Constipado = enrhumé. À la pharmacie, le malentendu serait gênant…"),
    "salida": ("La salida del pueblo está a la derecha.", "La sortie du village est à droite.",
               "Le succès du village est à droite.", "L'entrée du village est à droite.",
               "Salida = sortie. Éxito = succès. Entrada = entrée."),
    "embarazada": ("Estoy embarazada de cuatro meses.", "Je suis enceinte de quatre mois.",
                   "Je suis gênée depuis quatre mois.", "Je suis en voyage depuis quatre mois.",
                   "Embarazada = enceinte. Pour dire que vous êtes gêné : me da vergüenza."),
}


def verifier():
    ids = [e[0] for e in LEXIQUE]
    assert len(ids) == len(set(ids)), "identifiant en double"
    planches = {p[0] for p in PLANCHES}
    for e in LEXIQUE:
        assert len(e) == 6, e
        assert e[1] in planches, f"{e[0]} : planche inconnue {e[1]}"
        assert e[4] in ("croquis", "") or e[4].startswith("picto:"), e
        if e[5].startswith("PIÈGE"):
            assert e[0] in PIEGES, f"{e[0]} : piège sans phrase"
    for i, t in PIEGES.items():
        assert i in ids, f"piège {i} absent du lexique"
        assert len(t) == 5 and all(t), f"{i} : phrase, bonne, fausse, seconde, explication"
    return True


if __name__ == "__main__":
    verifier()
    from collections import Counter
    c = Counter(e[1] for e in LEXIQUE)
    for p, fr, _ in PLANCHES:
        print(f"  {fr:28} {c[p]:3}")
    print(f"{len(LEXIQUE)} mots, {sum(1 for e in LEXIQUE if e[4]=='croquis')} croquis, "
          f"{len(PIEGES)} pièges")
