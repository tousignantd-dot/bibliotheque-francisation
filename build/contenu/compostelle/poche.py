"""La poche — ce qu'on garde dans le téléphone pour le chemin, même sans réseau.

La poche ne réécrit rien : elle regroupe les phrases « Je le dis » des dix
journées et les formules du lexique, par situation. Seules les URGENCES sont
propres à la poche — elles ne se jouent dans aucune scène, et c'est justement
pour ça qu'il faut les avoir sous la main.

(id, es, fr) ; `{o|a}` comme ailleurs.
"""

URGENCES = [
    ("ayuda", "¡Socorro! ¡Ayuda, por favor!", "Au secours ! À l'aide, s'il vous plaît !"),
    ("ambulancia", "Llame a una ambulancia, por favor.", "Appelez une ambulance, s'il vous plaît."),
    ("perdido", "Me he perdido. ¿Dónde está el Camino?", "Je me suis perdu. Où est le chemin ?"),
    ("pasaporte", "He perdido el pasaporte.", "J'ai perdu mon passeport."),
    ("hospital", "¿Dónde está el hospital más cercano?", "Où est l'hôpital le plus proche ?"),
    ("caido", "Me he caído y me duele mucho el tobillo.", "Je suis tombé et j'ai très mal à la cheville."),
    ("medicamento", "Tomo este medicamento todos los días.", "Je prends ce médicament tous les jours."),
    ("alergia_grave", "Tengo una alergia grave. Es urgente.", "J'ai une allergie grave. C'est urgent."),
    ("robo", "Me han robado la cartera.", "On m'a volé mon portefeuille."),
    ("policia", "¿Dónde está la comisaría?", "Où est le poste de police ?"),
]

# L'ordre des rubriques de la poche : (clé, titre, source)
# source : "etape:<id>" (ses phrases « Je le dis »), "planche:<id>" (les
# formules sans image de cette planche), "urgences".
RUBRIQUES = [
    ("urgences", "Urgences", "urgences"),
    ("comprendre", "Comprendre et se faire comprendre", "planche:gente"),
    ("albergue", "À l'albergue", "etape:roncesvalles"),
    ("bar", "Au bar", "etape:pamplona"),
    ("restaurant", "Au restaurant", "etape:leon"),
    ("chemin", "Trouver son chemin", "etape:puente-la-reina"),
    ("pharmacie", "À la pharmacie", "etape:logrono"),
    ("ailleurs", "Dormir ailleurs, téléphoner", "etape:burgos"),
    ("meteo", "La météo et le sac", "etape:o-cebreiro"),
    ("acheter", "Acheter", "etape:sarria"),
    ("pelerins", "Entre pèlerins", "planche:peregrinos"),
    ("santiago", "À Santiago", "etape:santiago"),
]

# « Mon allergie » (audit tour 1, bloquant A3/F2 : on ne pouvait dire que les
# noix). Le pèlerin choisit la sienne dans les réglages ; elle alimente sa
# carte « Montrer », le « Je le dis » de León et le test.
# (code, « a + article », « sans article », fr)
ALERGENOS = [
    ("frutos_secos", "a los frutos secos", "frutos secos", "aux noix (fruits à coque)"),
    ("cacahuetes", "a los cacahuetes", "cacahuetes", "aux arachides"),
    ("marisco", "al marisco", "marisco", "aux fruits de mer"),
    ("pescado", "al pescado", "pescado", "au poisson"),
    ("huevo", "al huevo", "huevo", "aux œufs"),
    ("leche", "a la leche", "leche", "au lait"),
    ("gluten", "al gluten", "gluten", "au gluten"),
    ("sesamo", "al sésamo", "sésamo", "au sésame"),
]
# Pour les phrases de la scène de León et du test (audit tour 2, A3/D2 :
# l'allergie choisie doit traverser la scène éliminatoire, pas seulement la
# poche) : « des noix » en français, et ce que la salade contient, dit de
# façon à ce qu'on y reconnaisse l'allergène.
FORMES_ALG = {
    "frutos_secos": {"frde": "des noix", "ens": "nueces"},
    "cacahuetes": {"frde": "des arachides", "ens": "cacahuetes"},
    "marisco": {"frde": "des fruits de mer", "ens": "gambas, que son marisco"},
    "pescado": {"frde": "du poisson", "ens": "atún, que es pescado"},
    "huevo": {"frde": "des œufs", "ens": "huevo duro"},
    "leche": {"frde": "du lait", "ens": "queso, que es de leche"},
    "gluten": {"frde": "du gluten", "ens": "picatostes, que llevan gluten"},
    "sesamo": {"frde": "du sésame", "ens": "semillas de sésamo"},
}


def formes(code):
    """Les remplacements de {alg:…} pour un allergène."""
    c, a, sans, fr = next(x for x in ALERGENOS if x[0] == code)
    return {"a": a, "sans": sans, "fr": fr, **FORMES_ALG[code]}


def phrase_alergia(code):
    _, a, sans, _ = next(x for x in ALERGENOS if x[0] == code)
    return f"Tengo alergia grave {a}. ¿Este plato lleva {sans}?"
