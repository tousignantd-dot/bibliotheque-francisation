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
     "fr": "Au restaurant. Vous êtes allergique {alg:fr}. Que dites-vous au serveur ?",
     "choix": [("Soy alérgic{o|a} {alg:a}. ¿Este plato lleva {alg:sans}?", None),
               ("Me encanta la comida de aquí. ¿Este plato está bueno?", "Vous n'avez rien dit de votre allergie : soy alérgico, alérgica…"),
               ("Soy alérgic{o|a} {alg:a}. ¿Este plato es muy grande?", "Vous avez dit votre allergie, sans demander si le plat en contient : ¿lleva…?")]},
    {"obj": "O2", "type": "oral",
     "fr": "Au micro : dites au serveur votre allergie, et demandez si le plat en contient.",
     "cles": ["alergia|alérgico|alérgica|alergico|alergica", "{alg:sans}", "lleva"]},
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
    {"obj": "O1", "type": "rep", "qui": "javier",
     "es": "Lo siento, estamos completos, pero hay otro albergue al final de la calle.",
     "choix": [("Désolé, c'est complet, mais il y a un autre albergue au bout de la rue.", None),
               ("Désolé, c'est complet, et il n'y a pas d'autre albergue.", "« Pero hay otro albergue » : mais il y en a un autre."),
               ("Il reste des lits, au bout du couloir.", "Completos = complets : il n'y a plus de place ici.")]},
    {"obj": "O3", "type": "rep", "qui": "pilar",
     "es": "Si le duele la rodilla, póngase hielo diez minutos, tres veces al día.",
     "choix": [("Pour le genou : de la glace dix minutes, trois fois par jour.", None),
               ("Pour le genou : de la glace trois minutes, dix fois par jour.", "Diez minutos, tres veces : dix minutes, trois fois."),
               ("Pour la cheville : de la glace dix minutes, trois fois par jour.", "La rodilla = le genou. La cheville : el tobillo.")]},
    {"obj": "O4", "type": "rep", "qui": "fermin",
     "es": "El albergue está detrás de la iglesia, a mano izquierda.",
     "choix": [("L'albergue est derrière l'église, sur la gauche.", None),
               ("L'albergue est devant l'église, sur la gauche.", "Detrás = derrière. Devant : delante."),
               ("L'albergue est derrière l'église, sur la droite.", "Izquierda = gauche.")]},
    {"obj": "O5", "type": "repondre", "qui": "marta",
     "es": "¿Y desde dónde empezaste a caminar?",
     "choix": [("Desde Saint-Jean, en Francia.", None),
               ("Hasta Santiago, en Galicia.", "Desde = depuis. Elle demande d'où vous êtes parti."),
               ("Hace dos semanas, más o menos.", "Elle demande d'où, pas depuis quand.")]},
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
     "fr": "Au bar, vous voulez un bocadillo. Vous êtes allergique {alg:fr}. Que dites-vous ?",
     "choix": [("Perdone, soy alérgic{o|a} {alg:a}. ¿El bocadillo lleva {alg:sans}?", None),
               ("Perdone, ¿el bocadillo es grande o pequeño?", "La taille ne vous protège pas : dites votre allergie, et demandez s'il en contient."),
               ("Perdone, soy alérgic{o|a} {alg:a}. ¿Cuánto cuesta el bocadillo?", "Le prix ne vous protège pas : demandez s'il en contient — ¿lleva…?")]},
    {"obj": "O2", "type": "oral",
     "fr": "Au micro : dites à la serveuse votre allergie, et demandez si le sandwich en contient.",
     "cles": ["alergia|alérgico|alérgica|alergico|alergica", "{alg:sans}", "lleva"]},
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
    {"obj": "O1", "type": "rep", "qui": "rocio",
     "es": "El desayuno es a las siete, y hay que dejar la habitación antes de las ocho.",
     "choix": [("Le déjeuner est à 7 h ; il faut libérer la chambre avant 8 h.", None),
               ("Le déjeuner est à 8 h ; il faut libérer la chambre avant 7 h.", "L'ordre : el desayuno a las siete ; dejar la habitación antes de las ocho."),
               ("Le déjeuner est à 7 h ; on peut garder la chambre jusqu'à 8 h du soir.", "Antes de las ocho : avant 8 h, le matin.")]},
    {"obj": "O3", "type": "rep", "qui": "pilar",
     "es": "Póngase la crema dos veces al día: por la mañana y por la noche.",
     "choix": [("La crème deux fois par jour : le matin et le soir.", None),
               ("La crème deux fois par jour : le midi et le soir.", "Por la mañana = le matin."),
               ("La crème douze fois par jour.", "Dos veces = deux fois.")]},
    {"obj": "O4", "type": "rep", "qui": "fermin",
     "es": "La farmacia está enfrente de la fuente, a mano derecha.",
     "choix": [("La pharmacie est en face de la fontaine, sur la droite.", None),
               ("La pharmacie est en face du pont, sur la droite.", "Fuente = fontaine ; puente = pont."),
               ("La pharmacie est à côté de la fontaine, sur la gauche.", "Enfrente = en face ; derecha = droite.")]},
    {"obj": "O5", "type": "repondre", "qui": "marta",
     "es": "Oye, ¿y por qué haces el Camino?",
     "choix": [("Para pensar un poco en mi vida.", None),
               ("Desde Pamplona, con una amiga.", "Elle demande pourquoi, pas d'où."),
               ("A las siete de la mañana.", "Elle demande pourquoi, pas à quelle heure.")]},
  ],
]


SEUIL = "2 sur 2 : « Solide » ; 1 sur 2 : « En route » ; 0 : « À reprendre »."


def verifier():
    for f in FORMES:
        from collections import Counter
        assert all(n >= 2 for n in Counter(i["obj"] for i in f).values()), "deux items au moins par objectif"
        assert {i["obj"] for i in f} == set(OBJECTIFS), "chaque forme porte les cinq objectifs"
        assert any(i.get("elim") for i in f), "chaque forme a un item éliminatoire"
        for i in f:
            if i["type"] == "oral":
                continue
            assert i["choix"][0][1] is None and all(c[1] for c in i["choix"][1:]), i
    assert sorted(i["obj"] + i["type"] for i in FORMES[0]) == sorted(i["obj"] + i["type"] for i in FORMES[1]), "formes parallèles"
    return True
