"""Le test « Suis-je prêt ? » — deux formes PARALLÈLES, sur des items INÉDITS.

Audit tour 1 (bloquant F1) : le premier test reprenait les items mêmes de la
pratique, et chaque forme ne couvrait que la moitié des objectifs — une
pèlerine pouvait lire « Solide » sans avoir été interrogée sur l'allergie.
Ici, chaque forme porte les cinq objectifs, avec des phrases qu'on n'a jamais
entendues dans les journées (mêmes structures, autres valeurs), et l'allergie
y est ÉLIMINATOIRE : un item `elim` raté donne « Pas encore prête : l'allergie »,
quel que soit le reste. La règle est affichée avant de commencer.

Types :
- `rep`    : la personne dit une phrase ; on choisit ce qu'elle veut dire (fr).
- `dire`   : une situation en français ; on choisit ce qu'on DIT (es).
- `repondre` : la personne pose une question ; on choisit sa réponse (es).
Le premier choix est le bon ; l'ordre affiché tourne.
"""

OBJECTIFS = {
    "O1": "Obtenir un lit et comprendre prix, heures, règles",
    "O2": "Dire son allergie et comprendre la réponse",
    "O3": "Comprendre comment prendre un médicament",
    "O4": "Comprendre un chemin indiqué",
    "O5": "Répondre à un autre pèlerin",
}

FORMES = [
  [
    {"obj": "O1", "type": "rep", "qui": "javier",
     "es": "Quedan dos camas, arriba. Son doce euros y cerramos a las diez y media.",
     "choix": [("Il reste deux lits, en haut ; 12 € ; on ferme à 22 h 30.", None),
               ("Il reste deux lits, en bas ; 12 € ; on ferme à 22 h 30.", "Arriba = en haut. En bas : abajo."),
               ("Il reste deux lits, en haut ; 2 € ; on ferme à 22 h 30.", "Doce = 12. Dos = 2.")]},
    {"obj": "O2", "type": "rep", "qui": "alex", "elim": True,
     "es": "La tarta lleva almendras, pero el flan no lleva nada de frutos secos.",
     "choix": [("Le gâteau contient des amandes ; le flan, aucune noix.", None),
               ("Le gâteau et le flan contiennent tous deux des noix.", "« El flan no lleva nada » : le flan n'en contient aucune."),
               ("Le gâteau n'a pas d'amandes ; le flan contient des noix.", "Lleva = contient. C'est le gâteau (la tarta) qui a des amandes.")]},
    {"obj": "O2", "type": "dire", "elim": True,
     "fr": "Vous êtes allergique aux noix. Que dites-vous au serveur ?",
     "choix": [("Tengo alergia a los frutos secos. ¿Este plato los lleva?", None),
               ("Me gustan los frutos secos. ¿Este plato los lleva?", "Me gustan = j'aime ! Pour l'allergie : tengo alergia a…"),
               ("Tengo alergia a las frutas. ¿Este plato las lleva?", "Las frutas = les fruits. Les noix : los frutos secos.")]},
    {"obj": "O3", "type": "rep", "qui": "pilar",
     "es": "Tómese dos pastillas al día: una por la mañana y otra por la noche.",
     "choix": [("Deux comprimés par jour : un le matin, un le soir.", None),
               ("Deux comprimés le matin, et deux autres le soir.", "« Dos al día » : deux en tout — una… y otra."),
               ("Deux comprimés par jour : un le midi, un le soir.", "Por la mañana = le matin.")]},
    {"obj": "O4", "type": "rep", "qui": "fermin",
     "es": "Baje por esta calle, cruce la plaza y siga la flecha a la izquierda.",
     "choix": [("Descendez la rue, traversez la place, suivez la flèche à gauche.", None),
               ("Montez la rue, traversez la place, suivez la flèche à gauche.", "Baje = descendez. Montez : suba."),
               ("Descendez la rue, traversez la place, suivez la flèche à droite.", "Izquierda = gauche.")]},
    {"obj": "O5", "type": "repondre", "qui": "marta",
     "es": "¿Y tú, cuántos kilómetros haces al día?",
     "choix": [("Unos veinte, más o menos.", None),
               ("Unos veinte años, más o menos.", "Años = ans. Elle demande des kilomètres."),
               ("Desde Pamplona, más o menos.", "Elle demande combien, pas d'où.")]},
  ],
  [
    {"obj": "O1", "type": "rep", "qui": "rocio",
     "es": "Queda una cama abajo. Son quince euros, y la cena es a las ocho.",
     "choix": [("Il reste un lit, en bas ; 15 € ; souper à 20 h.", None),
               ("Il reste un lit, en haut ; 15 € ; souper à 20 h.", "Abajo = en bas. En haut : arriba."),
               ("Il reste un lit, en bas ; 50 € ; souper à 20 h.", "Quince = 15. Cincuenta = 50.")]},
    {"obj": "O2", "type": "rep", "qui": "ainhoa", "elim": True,
     "es": "El bocadillo vegetal no lleva frutos secos, pero la ensalada sí.",
     "choix": [("Le sandwich végétarien n'a pas de noix ; la salade, oui.", None),
               ("Ni le sandwich ni la salade ne contiennent de noix.", "« La ensalada sí » : la salade, elle, en contient."),
               ("Le sandwich végétarien a des noix ; la salade, non.", "No lleva = n'en contient pas : c'est le sandwich qui est sûr.")]},
    {"obj": "O2", "type": "dire", "elim": True,
     "fr": "Vous êtes allergique aux fruits de mer. Que dites-vous au serveur ?",
     "choix": [("Tengo alergia al marisco. ¿Este plato lo lleva?", None),
               ("Tengo alergia al mar. ¿Este plato lo lleva?", "El mar, c'est la mer ! Les fruits de mer : el marisco."),
               ("Me encanta el marisco. ¿Este plato lo lleva?", "Me encanta = j'adore ! Pour l'allergie : tengo alergia a…")]},
    {"obj": "O3", "type": "rep", "qui": "pilar",
     "es": "Tómese una pastilla cada doce horas, siempre con comida.",
     "choix": [("Un comprimé toutes les douze heures, toujours en mangeant.", None),
               ("Un comprimé toutes les deux heures, toujours en mangeant.", "Doce = 12. Dos = 2."),
               ("Douze comprimés par jour, toujours en mangeant.", "Cada doce horas : toutes les douze heures, un seul à la fois.")]},
    {"obj": "O4", "type": "rep", "qui": "fermin",
     "es": "Suba hasta la fuente y, después del puente, gire a la derecha.",
     "choix": [("Montez jusqu'à la fontaine et, après le pont, tournez à droite.", None),
               ("Montez jusqu'au pont et, après la fontaine, tournez à droite.", "Fuente = fontaine ; puente = pont. L'ordre compte."),
               ("Montez jusqu'à la fontaine et, après le pont, tournez à gauche.", "Derecha = droite.")]},
    {"obj": "O5", "type": "repondre", "qui": "marta",
     "es": "¿Y tú, dónde duermes esta noche?",
     "choix": [("En el albergue municipal.", None),
               ("A las diez de la noche.", "Elle demande où, pas quand."),
               ("Muy bien, gracias.", "Elle demande où vous dormez, pas comment vous allez.")]},
  ],
]


def verifier():
    for f in FORMES:
        assert {i["obj"] for i in f} == set(OBJECTIFS), "chaque forme porte les cinq objectifs"
        assert any(i.get("elim") for i in f), "chaque forme a un item éliminatoire"
        for i in f:
            assert i["choix"][0][1] is None and all(c[1] for c in i["choix"][1:]), i
    assert [i["obj"] + i["type"] for i in FORMES[0]] == [i["obj"] + i["type"] for i in FORMES[1]], "formes parallèles"
    return True
