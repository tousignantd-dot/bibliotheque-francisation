"""Le jeu de rôle libre d'« En route vers Compostelle » — l'assistant joue les gens du chemin.

La scène et le soir de chaque journée (etapes.py) sont ÉCRITS : ils marchent
sans réseau et sans IA. Le jeu de rôle libre en est la suite « avec
assistance » : la même personne, au même endroit, mais qui répond à ce que le
pèlerin dit vraiment. Même forme que les scénarios du comptoir de l'hôtel
(build/contenu/entreprise-hotel/clients.py), lue par /api/jeu-de-role :
une consigne propre (`systeme`), parce que le gabarit du serveur suppose la
francisation et le français.

    python3 build/contenu/compostelle/jeu_de_role.py   # vérifie et montre une consigne

À BRANCHER dans server.py (tenu par la session de l'hôtel le 25 sept. 2026,
donc pas branché ce jour-là) : les quatre lignes du bloc « comptoir », avec
ce fichier et `scenarios_serveur()`.
"""
import importlib.util, pathlib

_ICI = pathlib.Path(__file__).resolve().parent


def _charger(nom):
    sp = importlib.util.spec_from_file_location(f"compostelle_jr_{nom}", _ICI / f"{nom}.py")
    m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    return m


ET = _charger("etapes")
PS = _charger("personnages").PERSONNAGES

# Ce que chaque personne sait, et que le pèlerin ignore — le moteur de la
# conversation libre. Inventé pour la trousse ; les faits réels changent.
FAITS = {
    "roncesvalles": ["Il reste des lits : le 82 et le 84, en haut.", "C'est 14 € ; le déjeuner du matin (5 €) se paie à part.",
                     "Le souper est à 19 h au restaurant d'à côté ; la messe des pèlerins à 20 h.",
                     "La porte ferme à 22 h ; il faut partir avant 8 h.", "Les bottes restent en bas, au range-chaussures."],
    "pamplona": ["Il y a café au lait, cortado, jus d'orange pressé, rôties (tomate, ou beurre et confiture), tortilla.",
                 "La tortilla vient d'être finie ; il y en aura d'autre dans vingt minutes.",
                 "Un café au lait et une rôtie : 4,50 €. On peut payer par carte.",
                 "Les toilettes sont au fond, à droite."],
    "puente-la-reina": ["Le chemin : tout droit jusqu'à l'église, à gauche, traverser le pont roman, puis la flèche jaune à droite.",
                        "La fontaine à vin d'Irache est à environ 20 km, après Estella.",
                        "Il y a une boulangerie ouverte sur la place jusqu'à 14 h."],
    "logrono": ["Pour une ampoule fermée : un pansement spécial, à garder trois jours ; ne pas la percer.",
                "Pour le genou : ibuprofène, un comprimé toutes les 8 h, après avoir mangé.",
                "Si la douleur continue demain : le centre de santé, près de la cathédrale.",
                "Le pansement et l'ibuprofène : 11,20 €."],
    "burgos": ["L'albergue municipal est complet depuis 15 h.", "La pension Gómez, au coin de la rue, a encore une chambre simple à 35 €, sans déjeuner.",
               "La cathédrale ouvre à 9 h 30 ; tarif réduit pour les pèlerins avec credencial."],
    "carrion": ["Marta marche pour son mari, mort il y a deux ans ; elle porte sa photo dans son sac.",
                "Elle fait environ 25 km par jour.", "Ce soir, les religieuses de l'albergue chantent avec les pèlerins."],
    "leon": ["Menu du pèlerin : 12 € tout compris (pain, boisson, dessert).",
             "Entrées : soupe castillane, ou salade de la maison — la salade CONTIENT DES NOIX.",
             "Plats : truite à la navarraise ou poulet rôti. Desserts : flan, fruits, crème glacée.",
             "Le flan ne contient pas de noix ; la crème glacée du jour est à la noix."],
    "o-cebreiro": ["Demain : pluie toute la matinée, brouillard l'après-midi.", "La descente vers Triacastela est boueuse et glissante.",
                   "Transport des sacs : 5 € par étape, sac déposé ici avant 8 h avec l'étiquette.",
                   "En galicien : grazas (merci), rúa (rue), igrexa (église)."],
    "sarria": ["Bananes : 1,20 € le kilo ; pommes : 2 € le kilo ; fromage d'Arzúa : 9 € le kilo.",
               "L'épicerie tamponne les credencials ; depuis Sarria il en faut deux par jour.",
               "À Melide, le poulpe se mange chez les pulperías de la rue principale."],
    "santiago": ["Il faut la credencial, avec deux tampons par jour depuis Sarria.",
                 "Questions posées : d'où l'on est parti, à pied ou à vélo, la raison du chemin.",
                 "La messe des pèlerins est à midi à la cathédrale."],
}

PALIERS = {
    "lent": "PALIER LENT : phrases très courtes (une idée, huit mots au plus), mots courants, aucune expression idiomatique. Si le pèlerin a du mal, reformule plus simplement.",
    "normal": "PALIER NORMAL : phrases naturelles de une ou deux propositions, le vocabulaire d'une vraie conversation, quelques formules d'Espagne (vale, venga, ¿qué tal?).",
    "rapide": "PALIER RAPIDE : parle comme en Espagne, naturellement vite, avec les expressions du quotidien (¿qué te pongo?, vale, venga, madre mía, hombre) et sans simplifier.",
}


def _perso_de(cas_id):
    if cas_id.startswith("marta-"):
        return "marta", cas_id[6:]
    et = next(e for e in ET.ETAPES if e["id"] == cas_id)
    return et["local"], cas_id


def systeme(cas_id, role_eleve, palier=None):
    qui, etape = _perso_de(cas_id)
    et = next(e for e in ET.ETAPES if e["id"] == etape)
    nom, role, ou, genre, *_ = PS[qui]
    faits = FAITS.get(etape, [])
    marta = qui == "marta"
    situation = (f"C'est le soir, à {et['lieu']}. Vous parlez comme deux pèlerins qui se retrouvent. "
                 f"Sujet du soir : {et['soir']['titre'].lower()}." if marta else
                 f"La situation : {et['scene']['titre'].lower()}, à {et['lieu']}.")
    return (
        "Tu joues un rôle dans un exercice oral d'espagnol pour un pèlerin francophone du Québec qui "
        "marche sur le chemin de Compostelle (Camino francés) et qui débute en espagnol.\n\n"
        f"TU ES {nom}, {role}" + (f", à {ou}" if ou and not marta else "") + ". "
        + ("Tu es une pèlerine espagnole de Valladolid, 58 ans, professeure de musique à la retraite, "
           "chaleureuse et curieuse ; tu tutoies le pèlerin, comme tous les pèlerins entre eux. " if marta else
           "Tu parles au pèlerin comme on le fait en Espagne : poliment, souvent en le tutoyant s'il est jeune ou "
           "si l'ambiance est détendue, sinon en usted. ")
        + situation + "\n\n"
        "LANGUE : tu parles UNIQUEMENT l'espagnol d'ESPAGNE (castillan : vosotros, vale, móvil, zumo), du début "
        "à la fin. Si le pèlerin parle français ou anglais, tu fais comme une vraie personne du pays : tu "
        "comprends à moitié, tu souris, et tu redis en espagnol simple.\n\n"
        + ("Ce que tu sais et que le pèlerin ignore :\n" + "\n".join("- " + f for f in faits) + "\n\n" if faits else "")
        + "Comment tu parles :\n"
        "- Jamais plus de trois phrases par réplique ; jamais de liste ni de paragraphe.\n"
        "- Ne corrige jamais la langue du pèlerin et ne commente pas ses fautes ; si une phrase est "
        "incompréhensible, demande simplement de répéter (¿Perdona? ¿Cómo?).\n"
        "- Reste dans ton personnage quoi qu'il arrive.\n"
        "- Pas de balise, pas d'astérisque, pas de didascalie : seulement ce que tu dis.\n"
        + ("- Pose des questions sur sa vie, son chemin, ses raisons ; raconte un peu la tienne.\n" if marta else
           "- Donne les informations quand on te les demande ; ne récite pas tout d'un coup.\n")
        + "\nQuand la conversation arrive naturellement à sa fin, salue (¡Buen Camino!) et termine ta dernière "
          "réplique par le mot FIN."
        + ("\n\n" + PALIERS[palier] if palier in PALIERS else "")
    )


BILAN = (
    "Tu es formateur d'espagnol pour des pèlerins francophones du Québec. Voici une conversation sur le "
    "chemin de Compostelle entre une PERSONNE (jouée par un modèle) et un PÈLERIN qui débute en espagnol. "
    "Juge le PÈLERIN, avec bienveillance.\n"
    "« compris » : ce que le pèlerin a obtenu ou fait comprendre (une à trois choses, en français).\n"
    "« phrases » : jusqu'à trois phrases du pèlerin qui gagneraient à être dites autrement en espagnol "
    "d'Espagne (sens, formule naturelle), jamais pour un accent ou une virgule : « dit » (sa phrase) et "
    "« mieux » (la même idée, correcte et naturelle).\n"
    "« conseil » : une phrase en français, et une formule utile en espagnol entre guillemets.\n"
    "« resume » : une phrase simple, en français, sur ce qui a marché.\n"
    "Réponds UNIQUEMENT en JSON : {\"compris\": [\"…\"], \"phrases\": [{\"dit\": \"…\", \"mieux\": \"…\"}], "
    "\"conseil\": \"…\", \"resume\": \"…\"}."
)


def scenario_serveur():
    cas = {}
    for et in ET.ETAPES:
        cas[et["id"]] = {"contexte": et["scene"]["titre"], "client": FAITS.get(et["id"], []), "pelerin": []}
        cas["marta-" + et["id"]] = {"contexte": et["soir"]["titre"], "client": FAITS.get(et["id"], []), "pelerin": []}
    return {
        "cadre": "le chemin de Compostelle",
        "contexte_label": "La situation",
        "cas": cas, "sujets": [], "cloture": "",
        "ouverture": {"pelerin": "¡Hola! ¡Buen Camino!", "client": "¡Hola! ¡Buen Camino!"},
        "roles": {"client": {"qui": "", "conduite": ""}, "pelerin": {"qui": "", "conduite": ""}},
        "paliers": PALIERS,
        "bilan": BILAN,
        "systeme": systeme,
        "etiquettes": ("PERSONNE", "PÈLERIN"),
        "voix": [],
    }


def scenarios_serveur():
    return {"camino-es-fr": scenario_serveur()}


if __name__ == "__main__":
    s = scenarios_serveur()["camino-es-fr"]
    print(len(s["cas"]), "situations")
    print(systeme("leon", "pelerin", "lent")[:900])
