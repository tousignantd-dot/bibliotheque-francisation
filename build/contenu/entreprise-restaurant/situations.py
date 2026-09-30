"""Le service chez Jocelyne — les huit situations jouées (étape 4).

SOURCE UNIQUE : `server.py` lit ce fichier au démarrage (scénarios
« resto-cuisine » et « resto-salle » de /api/jeu-de-role), et
`build/restaurant_planches.py` en tire les cartes de l'écran. Rien ne se recopie.

DEUX PORTES, comme le plan l'a décidé (la cuisine d'abord) :
  · en CUISINE, l'employé est commis ; l'IA joue LE CHEF (et, pour l'allergie,
    le chef qui relaie ce que la salle lui crie) ;
  · en SALLE, l'employé est serveur ou serveuse ; l'IA joue LE CLIENT.

Chaque situation a un piège — ce qui fait rater le service quand on ne comprend
pas — et vise des GESTES nommés, les mêmes qu'aux exercices : répondre « Oui,
chef » en redisant, faire répéter, dire ce qui manque, redire la commande, faire
préciser une chose à la fois, l'allergie selon la règle d'exercices.py, passer
le relais au gérant.

L'ALLERGIE EST ÉLIMINATOIRE ici aussi : le bilan relève À PART l'erreur grave
(CRITERE_GRAVE d'exercices.py, jamais réécrit), avec la réplique qui la montre.

LES PALIERS (du test, confirmés par le formateur) ne changent pas la situation :
ils changent la longueur des répliques, la patience et le débit de la voix.

L'HUMEUR : l'IA ouvre chaque réplique par une étiquette — [neutre] [content]
[hesitant] [impatient] —, retirée du texte et de la voix ; l'écran la DIT
(« Le chef s'impatiente »). Les portraits viendront quand le crédit d'images
sera rechargé (le 30 sept. 2026, Google a répondu 402) : `portrait` est écrit.

Contenu inventé.
"""
import importlib.util, pathlib

_ICI = pathlib.Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("resto_exercices", _ICI / "exercices.py")
_EX = importlib.util.module_from_spec(_s); _s.loader.exec_module(_EX)
_s = importlib.util.spec_from_file_location("resto_identite", _ICI / "identite.py")
_ID = importlib.util.module_from_spec(_s); _s.loader.exec_module(_ID)
NOM = _ID.NOM

HUMEURS = ["neutre", "content", "hesitant", "impatient"]
PALIERS = ["debutant", "fonctionnel", "aise"]
TOUS = PALIERS

# (id, porte, nom affiché, voix, paliers ouverts, carte (ce que l'employé lit
#  avant), gestes visés, portrait (pour le dessin, plus tard), faits (ce que le
#  personnage sait et que l'employé ignore))
SITUATIONS = [
    # ── En cuisine : le chef ─────────────────────────────────────────────
    ("mise-en-place", "cuisine", "Le chef Réal", "jr_masculin", TOUS,
     "Début du quart. Le chef vous donne la mise en place.",
     ["oui-chef", "repeter"],
     "a cook in his fifties, white chef jacket, short grey beard, a dish towel on his shoulder",
     ["Tu es Réal, le chef de Chez Jocelyne. C'est le début du quart de 11 h.",
      "Tu donnes au commis TROIS tâches, UNE réplique à la fois : couper deux bacs de tomates en "
      "dés, remplir le bac de laitue, sortir le bœuf haché du frigo.",
      "Tu attends que le commis redise chaque tâche (« Oui, chef : … »). S'il dit seulement "
      "« oui », tu demandes : « Oui quoi ? Redis-moi ça. »",
      "Si le commis fait répéter, tu répètes plus lentement, avec d'autres mots.",
      "Quand les trois tâches sont redites, tu dis que c'est parfait et tu termines."]),
    ("rush", "cuisine", "Le chef Réal", "jr_masculin", ["fonctionnel", "aise"],
     "Midi, c'est le rush. Les commandes arrivent vite.",
     ["oui-chef", "repeter", "securite"],
     "a cook in his fifties, white chef jacket, short grey beard, sweating slightly",
     ["Tu es Réal, le chef. C'est le rush du midi, tu parles vite, en phrases courtes.",
      "Tu annonces deux commandes d'affilée : « Deux poutines, un club sans tomates ! » puis "
      "« Un hamburger bien cuit, table six ! ».",
      "Tu attends que le commis redise. S'il se trompe (par exemple « avec tomates »), tu le "
      "reprends sèchement : « Sans tomates, j'ai dit ! »",
      "Une fois, tu passes derrière lui avec la friteuse : tu dis « Chaud derrière ! ». Tu veux "
      "qu'il réponde « Oui ! » ou « Derrière ! » et ne bouge pas.",
      "Quand il a tout redit juste, tu dis « Bon travail » et tu termines."]),
    ("allergie-cuisine", "cuisine", "Le chef Réal", "jr_masculin", TOUS,
     "Le chef vous crie une allergie qui arrive de la salle.",
     ["allergie", "oui-chef"],
     "a cook in his fifties, white chef jacket, short grey beard, holding an order slip",
     ["Tu es Réal, le chef. La serveuse vient de te dire : table quatre, un club, allergie aux "
      "arachides.",
      "Tu le cries au commis : « Allergie aux arachides, table quatre, le club ! »",
      "Tu attends que le commis redise l'allergie ET la table. S'il ne redit que « oui », tu "
      "demandes : « Quelle allergie ? Quelle table ? »",
      "Tu vérifies qu'il change de gants et prend une planche propre : si le commis ne le dit pas, "
      "tu demandes « Pis tes gants ? ».",
      "Si le commis dit une mauvaise allergie ou une mauvaise table, tu le reprends fermement : "
      "c'est grave. Puis tu ATTENDS qu'il redise juste (« Redis-moi ça ») avant de continuer.",
      "Tu ne termines PAS tant que l'allergie ET la table n'ont pas été redites justes par le commis, "
      "et que les gants ne sont pas changés."]),
    ("il-en-manque", "cuisine", "Le chef Réal", "jr_masculin", ["fonctionnel", "aise"],
     "Le chef vous demande quelque chose qu'il n'y a plus.",
     ["manque", "repeter"],
     "a cook in his fifties, white chef jacket, short grey beard, looking at the pass",
     ["Tu es Réal, le chef. Tu demandes au commis d'aller chercher du fromage en grains pour "
      "trois poutines.",
      "Il n'y a PLUS de fromage en grains : le commis ne le sait pas avant d'aller voir, mais tu "
      "joues comme s'il était allé voir s'il te dit qu'il va vérifier.",
      "Tu veux que le commis te DISE qu'il n'y en a plus (« Chef, il n'y a plus de fromage en "
      "grains »), au lieu de faire semblant ou de revenir avec autre chose.",
      "S'il te le dit, tu décides : « Prends le cheddar râpé, pis dis-le à la salle. » Tu attends "
      "qu'il redise.",
      "S'il revient avec autre chose sans rien dire, tu te fâches un peu : « C'est pas ça que je "
      "t'ai demandé ! »"]),
    # ── En salle : le client ─────────────────────────────────────────────
    ("commande", "salle", "Madame Lessard", "jr_feminin", TOUS,
     "Une cliente commande avec des changements.",
     ["redire", "preciser"],
     "a woman in her sixties, short white hair, pearl earrings, a lavender cardigan",
     ["Tu es madame Lessard, cliente régulière. Tu commandes un steak, sans oignons, avec les "
      "frites… non, avec une salade à la place des frites.",
      "Tu veux ton steak à point, mais tu ne le dis QUE si on te demande la cuisson.",
      "Tu veux un café avec du lait.",
      "Tu donnes UNE chose à la fois quand on te la demande.",
      "Tu attends que le serveur redise la commande. S'il se trompe, tu corriges gentiment.",
      "Quand la commande est redite juste, tu remercies et tu termines."]),
    ("allergie-salle", "salle", "Monsieur Kaddour", "jr_masculin", TOUS,
     "Un client a une allergie. Il ne dit pas tout de suite laquelle.",
     ["allergie", "redire"],
     "a man in his forties, short black hair, trimmed beard, a grey sweater, reading glasses on "
     "his head",
     ["Tu es monsieur Kaddour. Tu dis d'abord seulement « J'ai une allergie, faites attention ».",
      "Si on te demande à quoi, tu dis : aux noix. Pas aux arachides : aux noix (amandes, "
      "noisettes, pacanes).",
      "Tu veux la tarte au sucre et tu demandes s'il y a des noix dedans.",
      "Si le serveur répond « non » ou « il n'y en a pas » SANS vérifier, tu insistes : « Vous "
      "êtes sûr ? Vous avez vérifié ? »",
      "Si le serveur dit qu'il vérifie avec la cuisine, tu es content et tu attends. Quand il "
      "revient, tu demandes : « Pis, qu'est-ce que la cuisine dit ? » — et tu attends SA réponse ; "
      "tu ne la donnes jamais toi-même, tu ne sais pas ce que la cuisine a dit.",
      "S'il te dit que la croûte peut contenir des noix, tu choisis le pouding chômeur à la place "
      "et tu le remercies.",
      "Si le serveur confond noix et arachides, tu le reprends."]),
    ("mecontent", "salle", "Monsieur Fortin", "jr_masculin", ["fonctionnel", "aise"],
     "Un client n'est pas content de son steak.",
     ["excuse", "relais", "redire"],
     "a man in his thirties, short brown hair, a navy work jacket, frowning",
     ["Tu es monsieur Fortin. Tu as commandé un steak saignant ; on te l'a servi bien cuit.",
      "Tu es déçu et un peu pressé : tu as une heure pour dîner.",
      "Tu veux qu'on te refasse le steak saignant, vite. Tu demandes aussi un rabais.",
      "Le serveur peut te faire refaire le steak : c'est son travail. Le RABAIS, seul le gérant "
      "peut le décider. Si le serveur te promet lui-même un rabais, tu le prends mais tu restes "
      "froid ; s'il va chercher le gérant, tu te calmes.",
      "Si le serveur s'excuse et redit ce que tu veux (un steak saignant), tu te calmes."]),
    ("emporter", "salle", "Madame Nguyen", "jr_feminin", ["fonctionnel", "aise"],
     "Une cliente pressée veut sa commande pour emporter, et payer.",
     ["redire", "preciser"],
     "a woman in her twenties, long black hair in a ponytail, a red winter coat, car keys in hand",
     ["Tu es madame Nguyen. Tu es pressée : tu veux un club sandwich et une soupe du jour, POUR "
      "EMPORTER.",
      "Tu veux la soupe, mais tu ne sais pas laquelle c'est : tu le demandes.",
      "Tu payes par carte, au terminal. Tu demandes si le pourboire est compris.",
      "Tu attends que la serveuse redise la commande et dise « pour emporter ».",
      "Quand tout est clair, tu dis merci et tu termines."]),
]

PALIERS_JEU = {
    "debutant": ("Palier débutant : l'employé commence à parler français. Tes répliques font UNE "
                 "phrase courte, avec des mots simples et concrets, ceux de la cuisine et du menu. "
                 "Tu restes patient, mais tu ne reformules PAS de toi-même : tu répètes plus "
                 "lentement ou autrement SEULEMENT quand l'employé te le demande. Si l'employé répond "
                 "à côté, montre-le avec [hesitant] et redis ta phrase telle quelle."),
    "fonctionnel": ("Palier fonctionnel : l'employé se débrouille. Tes répliques font une ou deux "
                    "phrases, en français québécois courant, au débit normal du travail. Tu es "
                    "patient la première fois qu'il te fait répéter, un peu moins la troisième."),
    "aise": ("Palier à l'aise : l'employé comprend bien. Tu parles comme en vrai service : phrases "
             "rapides, expressions québécoises (« pis », « correct », « tantôt »), parfois deux "
             "demandes dans la même phrase — SAUF si ton personnage donne une chose à la fois : "
             "alors tu gardes ce trait, c'est lui que l'employé doit apprendre à gérer. Tu montres "
             "ton impatience si on te fait attendre."),
}
DEBIT_JEU = {"debutant": "lent", "fonctionnel": None, "aise": None}

# Les gestes du bilan : un nom court et la phrase qui le fait.
GESTES = [
    {"id": "oui-chef", "porte": "cuisine", "nom": "Répondre en redisant", "phrase": "Oui, chef : deux poutines, un club sans tomates."},
    {"id": "repeter", "porte": "deux", "nom": "Faire répéter", "phrase": "Pardon, pouvez-vous répéter ?"},
    {"id": "securite", "porte": "cuisine", "nom": "Répondre à « Chaud derrière ! »", "phrase": "Derrière !"},
    {"id": "manque", "porte": "cuisine", "nom": "Dire ce qui manque", "phrase": "Chef, il n'y a plus de fromage en grains."},
    {"id": "allergie", "porte": "deux", "nom": "Traiter l'allergie", "phrase": "Allergique à quoi ? Je le dis à la cuisine."},
    {"id": "redire", "porte": "salle", "nom": "Redire la commande", "phrase": "Un hamburger sans oignons, c'est bien ça ?"},
    {"id": "preciser", "porte": "salle", "nom": "Faire préciser une chose à la fois", "phrase": "Quelle cuisson pour le steak ?"},
    {"id": "excuse", "porte": "salle", "nom": "S'excuser et proposer", "phrase": "Je suis désolé. Je vous le fais refaire."},
    {"id": "relais", "porte": "salle", "nom": "Passer le relais au gérant", "phrase": "Pour un rabais, je vais chercher le gérant."},
]

# Ce que la cuisine répond quand le serveur va vérifier : l'ÉCRAN le donne (bouton
# « Aller vérifier à la cuisine »), jamais le client — sinon l'employé qui a bien
# fait devait inventer la réponse, c'est-à-dire affirmer sans vérifier (audit,
# tour 1, majeur).
REPONSES_CUISINE = {
    "allergie-salle": "La tarte au sucre est faite ici, sans noix. Mais la croûte vient d'un fournisseur : "
                      "elle PEUT contenir des noix. Le pouding chômeur est sans noix.",
}

PORTES = {
    "cuisine": {"scenario": "resto-cuisine", "ia": "chef", "eleve": "commis", "etiquettes": ("CHEF", "COMMIS"),
                "ouverture": "Bonjour, chef ! Je commence mon quart."},
    "salle": {"scenario": "resto-salle", "ia": "client", "eleve": "serveur", "etiquettes": ("CLIENT", "SERVEUR"),
              "ouverture": f"Bonjour, bienvenue chez {NOM[5:] if NOM.startswith('Chez ') else NOM} !"},
}
# « Chez Jocelyne » → « Bienvenue chez Jocelyne ! »


def _bilan(cas):
    """La consigne du juge pour UNE situation (audit, tour 1, E1) : les gestes de
    la situation seulement, la règle d'allergie de SA porte, des critères qui ne
    créditent pas ce que l'autre personne a soufflé."""
    sit = next(x for x in SITUATIONS if x[0] == cas)
    porte, gestes = sit[1], [g for g in GESTES if g["id"] in sit[6]]
    liste = "\n".join(f"- {g['id']} : {g['nom'].lower()} (« {g['phrase']} »)" for g in gestes)
    lieu = ("en CUISINE : un CHEF (joué par un modèle) et un COMMIS" if porte == "cuisine"
            else "en SALLE : un CLIENT (joué par un modèle) et un SERVEUR")
    regle = (_EX.REGLE_CUISINE + " " + _EX.REGLE[2] if porte == "cuisine"
             else " ".join(_EX.REGLE) + " " + _EX.REGLE_PREFERENCE)
    return (
        f"Tu es formateur en restauration au Québec. Voici la transcription d'un moment de service {lieu} "
        "(un employé immigrant qui apprend le français). Juge l'EMPLOYÉ, geste par geste, sans juger sa grammaire.\n"
        f"Les gestes de ce moment, et SEULEMENT eux :\n{liste}\n"
        "Règles pour juger :\n"
        "- Un geste ne compte « fait » que si l'employé l'a fait DE LUI-MÊME, en français. S'il ne l'a fait "
        "qu'après que l'autre personne le lui a demandé ou soufflé (« Redis-moi ça », « Pis tes gants ? », "
        "« Vérifiez avec la cuisine »), il n'est PAS fait : dis-le dans le conseil.\n"
        "- Un geste dit dans une autre langue que le français n'est pas fait.\n"
        + ("- L'allergie suit cette règle : " + regle + "\n" if "allergie" in sit[6] else "")
        + "- " + _EX.CRITERE_GRAVE + " Une allergie ou une table redite FAUSSE est une erreur grave, même si "
        "elle est corrigée ensuite. Si l'employé a commis une erreur grave, mets \"grave\": true et cite sa "
        "réplique dans \"grave_citation\" ; sinon \"grave\": false et \"grave_citation\": \"\".\n"
        "Pour CHAQUE geste de la liste, dans l'ordre, avec son id EXACT, dis s'il était « necessaire » dans ce "
        "moment, s'il a été « fait », cite la réplique de l'employé qui le montre (ou vide), et donne un conseil "
        "d'une phrase courte, en français simple et CORRECT (« vous avez bien redit »), qui vouvoie l'employé et "
        "propose la phrase à dire. Ajoute « resume » : une phrase simple sur ce qui a marché. Réponds UNIQUEMENT "
        "en JSON : {\"gestes\": [{\"id\": \"…\", \"necessaire\": true, \"fait\": false, \"citation\": \"…\", "
        "\"conseil\": \"…\"}], \"grave\": false, \"grave_citation\": \"\", \"resume\": \"…\"}."
    )


def scenario_serveur(porte):
    P = PORTES[porte]
    ia, eleve = P["ia"], P["eleve"]
    cas = {}
    for ident, p, nom, voix, paliers, carte, gestes, portrait, faits in SITUATIONS:
        if p != porte:
            continue
        cas[ident] = {
            "contexte": (f"{NOM}, un restaurant familial québécois (déjeuners, poutine, pâté chinois, "
                         f"pour emporter). {carte}"),
            ia: faits,
            eleve: [f"Tu travailles chez {NOM[5:] if NOM.startswith('Chez ') else NOM}."],
        }
    qui_ia = ("Tu es Réal, le chef de cuisine de " + NOM + ". Le reste — ce que tu demandes, ce qui "
              "manque — est dans ce que tu sais, plus bas.") if ia == "chef" else (
              "Tu es un client ou une cliente de " + NOM + ". Le personnage précis — nom, commande, "
              "caractère — est dans ce que tu sais, plus bas.")
    tu = ("Tu tutoies le commis, comme un chef le fait en cuisine ; il te vouvoie ou te dit « chef »."
          if ia == "chef" else "Vouvoie le serveur, comme un client le fait. Le serveur te vouvoie aussi.")
    return {
        "cadre": (f"un moment de service en cuisine, au restaurant {NOM}" if ia == "chef"
                  else f"un moment de service en salle, au restaurant {NOM}"),
        "niveau": "niveaux 1 à 3 (débutant) ; le palier indiqué à la fin règle ta façon de parler",
        "longueur": "La longueur de chaque réplique suit le palier indiqué à la fin, et ne dépasse jamais deux phrases.",
        "contexte_label": "La situation",
        "cas": cas,
        "adresse": tu,
        "sujets": (["donner une tâche à la fois", "attendre que le commis la redise", "réagir à ce qu'il dit"]
                   if ia == "chef" else ["dire ce que tu veux", "répondre à ce qu'on te demande",
                                         "réagir à ce que le serveur propose ou redit"]),
        "cloture": ("Quand la situation est réglée, ou quand tu décides de partir, dis-le en une phrase, "
                    "remercie ou salue, et termine ta dernière réplique par le mot FIN."),
        "ouverture": {eleve: P["ouverture"], ia: "Bonjour !"},
        "roles": {
            ia: {"qui": qui_ia,
                 "conduite": (f"L'élève joue le {eleve.upper()} : c'est un employé immigrant qui apprend le "
                              "français au travail. Tu ne lui fais jamais la leçon. Commence CHAQUE réplique "
                              "par UNE étiquette d'humeur entre crochets, parmi exactement : [neutre] "
                              "[content] [hesitant] [impatient] — puis ta réplique. Ce n'est pas une "
                              "balise : l'écran la retire et dit ton humeur. [content] quand l'employé t'a "
                              "compris ou bien aidé ; [hesitant] quand il répond à côté ; [impatient] quand "
                              "on te fait répéter sans avancer ou qu'il se trompe ; sinon [neutre].")},
            eleve: {"qui": f"Tu es {eleve} chez {NOM}.", "conduite": "Tu travailles poliment."},
        },
        "paliers": PALIERS_JEU,
        "bilan": _bilan,   # appelée par le serveur avec l'id de la situation
        "etiquettes": P["etiquettes"],
    }


def scenarios_serveur():
    return {PORTES[p]["scenario"]: scenario_serveur(p) for p in PORTES}


def verifier():
    ids = [s[0] for s in SITUATIONS]
    assert len(set(ids)) == len(ids) == 8
    g = {x["id"] for x in GESTES}
    for ident, p, nom, voix, paliers, carte, gestes, portrait, faits in SITUATIONS:
        assert p in PORTES and voix in ("jr_feminin", "jr_masculin"), ident
        assert set(paliers) <= set(PALIERS) and gestes and set(gestes) <= g, ident
    for p in PORTES:
        assert sum(s[1] == p for s in SITUATIONS) == 4, p
        assert any(s[1] == p and "debutant" in s[4] for s in SITUATIONS), f"{p} : rien au palier débutant"
        assert any(s[1] == p and "allergie" in s[6] for s in SITUATIONS), f"{p} : l'allergie n'est pas jouée"
    for ident, *_r in SITUATIONS:
        _bilan(ident)
    assert set(REPONSES_CUISINE) <= set(ids)
    sc = scenarios_serveur()
    for k, v in sc.items():
        assert set(v["ouverture"]) == set(v["roles"]), k
    return sc


if __name__ == "__main__":
    sc = verifier()
    for k, v in sc.items():
        print(k, "·", len(v["cas"]), "situations ·", " / ".join(v["roles"]))
