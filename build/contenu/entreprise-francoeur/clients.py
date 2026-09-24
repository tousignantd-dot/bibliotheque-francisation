"""Le magasin de la Maison Francœur — les huit clients du jeu de rôle (étape 4).

SOURCE UNIQUE : `server.py` lit ce fichier au démarrage (scénario « magasin »
de /api/jeu-de-role), `build/francoeur_planches.py` en tire les cartes de
l'écran, `build/francoeur_clients.py` les portraits. Rien ne se recopie.

L'employé est TOUJOURS le vendeur : il ne se voit pas. L'avatar est le client,
face à lui. Chaque client a un caractère, un besoin et un piège — ce qui fait
échouer une vente quand on ne comprend pas.

LES PALIERS ne changent pas le scénario : ils changent la longueur des phrases
du client, sa patience, et le débit de sa voix (débutant = palier « lent » de
la voix). Le palier vient du test (étape 3), confirmé par le formateur.

L'HUMEUR : le client commence chaque réplique par une étiquette entre crochets
— [neutre] [contente] [hesitante] [impatiente]. L'écran la retire du texte et
de la voix, et montre le portrait correspondant. C'est ce qui fait voir à
l'employé l'effet de ce qu'il dit, sans qu'on le lui écrive.

Contenu inventé ; les cinq gestes sont ceux du bloc A de Chaussures Rivard :
arrêter · faire préciser une chose à la fois · redire · laisser la porte
ouverte · passer le relais.
"""

HUMEURS = ["neutre", "contente", "hesitante", "impatiente"]

# (id, nom affiché, voix, paliers ouverts, carte (ce que l'employé lit avant),
#  portrait (pour le dessin), faits (ce que le client sait et que l'employé ignore))
CLIENTS = [
    ("regarde", "Monsieur Gagnon", "jr_masculin", ["debutant", "fonctionnel", "aise"],
     "Il entre, il regarde. Il ne veut pas qu'on le pousse.",
     "a man in his sixties, short grey hair, grey moustache, glasses, a beige quilted vest over a "
     "blue checked shirt",
     ["Tu es monsieur Gagnon, retraité. Tu entres « juste pour regarder ».",
      "Si le vendeur insiste ou te propose trois choses d'affilée, tu deviens impatient et tu dis "
      "que tu vas repasser.",
      "Si le vendeur te laisse regarder et dit qu'il est là au besoin, tu reviens après deux "
      "répliques avec une vraie question : une chemise pour un souper de famille, en grand.",
      "Tu aimes le bleu. Tu n'aimes pas les motifs."]),

    ("taille", "Madame Ouellet", "jr_feminin", ["debutant", "fonctionnel", "aise"],
     "Elle cherche un chandail pour elle. Elle ne connaît pas sa taille ici.",
     "a woman in her forties, dark curly hair tied back, small gold earrings, a burgundy coat "
     "open over a white top",
     ["Tu es madame Ouellet. Tu cherches un chandail chaud pour l'hiver, pour toi.",
      "Tu ne sais pas ta taille dans ce magasin : chez toi, tu fais « du moyen, ou du grand, ça "
      "dépend ».",
      "Tu veux du gris ou du marine, pas de noir.",
      "Si le vendeur te propose d'essayer, tu acceptes et tu demandes où sont les cabines.",
      "Tu donnes UNE information à la fois : la couleur si on te la demande, la taille si on te "
      "la demande."]),

    ("cabine", "Monsieur Diallo", "jr_masculin", ["debutant", "fonctionnel", "aise"],
     "Il sort de la cabine. Le pantalon ne va pas.",
     "a man in his thirties, short black hair, trimmed beard, a navy hoodie, holding nothing",
     ["Tu es monsieur Diallo. Tu sors de la cabine d'essayage avec un pantalon beige.",
      "Le pantalon est trop serré à la taille et un peu long.",
      "Tu voudrais la même chose, une taille plus grande — tu portais du 32, il te faut du 34.",
      "Si le vendeur ne comprend pas « serré », tu montres ta taille et tu dis « trop petit, "
      "ici ».",
      "Tu demandes aussi si on peut faire l'ourlet ici."]),

    ("cadeau", "Madame Tremblay", "jr_feminin", ["fonctionnel", "aise"],
     "Elle cherche un cadeau pour quelqu'un d'autre.",
     "a woman in her fifties, short silver hair, red-framed glasses, a teal scarf over a grey coat",
     ["Tu es madame Tremblay. Tu cherches un cadeau pour ton petit-fils de seize ans.",
      "Tu ne connais pas sa taille exacte : « il est grand et mince ».",
      "Tu hésites entre un kangourou et une casquette.",
      "Tu demandes si on peut échanger si ça ne fait pas, et si le magasin fait des reçus-cadeaux "
      "(oui, trente jours, avec le reçu-cadeau).",
      "À la fin, tu demandes une carte-cadeau à la place si le vendeur n'a pas su t'aider."]),

    # Ouvert au débutant (audit, A3) : c'est lui qui doit apprendre à vérifier.
    ("rupture", "Monsieur Nguyen", "jr_masculin", ["debutant", "fonctionnel", "aise"],
     "Il veut un article qui n'est plus sur le plancher.",
     "a man in his twenties, straight black hair, a black puffer jacket, a small backpack strap on "
     "one shoulder",
     ["Tu es monsieur Nguyen. Tu veux le manteau d'hiver noir de la vitrine, en moyen.",
      "Sur le plancher, il ne reste que du petit et du très grand.",
      "Tu veux savoir s'il y en a en arrière, sinon dans une autre succursale, sinon quand il en "
      "rentrera.",
      "Si le vendeur promet sans vérifier, tu lui demandes s'il est sûr.",
      "Tu acceptes qu'on te le mette de côté si on prend ton nom et ton numéro, et tu épelles ton "
      "nom : N-G-U-Y-E-N."]),

    ("presse", "Madame Roy", "jr_feminin", ["fonctionnel", "aise"],
     "Elle est pressée. Elle parle vite.",
     "a woman in her thirties, long brown hair in a ponytail, a phone in her coat pocket, a "
     "camel trench coat",
     ["Tu es madame Roy. Tu as dix minutes avant ton autobus.",
      "Tu veux des bas de laine gris, deux paires, et des mitaines noires.",
      "Tu enchaînes les demandes vite, sans pause.",
      "Si le vendeur te demande de répéter poliment, tu répètes plus lentement, sans te fâcher.",
      "Si le vendeur fait semblant de comprendre et se trompe, tu deviens impatiente."]),

    # Ouvert au débutant (audit, A3) : passer le relais est son geste le plus utile.
    ("retour", "Monsieur Lavoie", "jr_masculin", ["debutant", "fonctionnel", "aise"],
     "Il veut rapporter un article, mais il n'a pas son reçu.",
     "a man in his forties, receding brown hair, a green fleece jacket, a paper shopping bag "
     "held up at chest height",
     ["Tu es monsieur Lavoie. Tu rapportes un coton ouaté acheté il y a trois semaines.",
      "Tu n'as pas le reçu. Tu as payé par carte.",
      "La politique : sans reçu, un échange ou une note de crédit, pas de remboursement ; avec le "
      "relevé de carte, la gérante peut vérifier.",
      "Tu insistes une fois pour être remboursé, poliment mais fermement.",
      "Tu acceptes la solution si le vendeur te l'explique clairement, ou s'il va chercher la "
      "gérante."]),

    ("mecontente", "Madame Pelletier", "jr_feminin", ["aise"],
     "Elle est fâchée : un manteau acheté ici s'est décousu.",
     "a woman in her fifties, short dark hair, a frown line between the eyebrows, a navy parka "
     "folded over one arm",
     ["Tu es madame Pelletier. Ton manteau acheté il y a deux mois s'est décousu à l'épaule.",
      "Tu es fâchée et tu parles fort au début. Tu dis que c'est de la mauvaise qualité.",
      "Tu veux parler à quelqu'un qui peut décider.",
      "Si le vendeur t'écoute, reformule ton problème et va chercher la gérante, tu te calmes.",
      "Si le vendeur essaie de régler lui-même ce qu'il ne peut pas promettre, tu te fâches "
      "davantage."]),
]

PALIERS_JEU = {
    # Audit (E2, majeur) : le client débutant reformulait de lui-même et ne
    # s'impatientait jamais — deviner ne coûtait rien, et faire répéter (O3)
    # n'était jamais nécessaire. Il reste simple et patient, mais il ATTEND
    # qu'on lui demande de répéter, et il montre quand on répond à côté.
    "debutant": ("Palier débutant : l'employé commence à parler français. Tes répliques font UNE "
                 "phrase courte, avec des mots simples et concrets. Si ton personnage a plusieurs "
                 "besoins, n'en garde qu'UN. Tu restes patient, mais tu ne reformules PAS de toi-"
                 "même : tu répètes plus lentement ou autrement SEULEMENT quand le vendeur te le "
                 "demande (« Pouvez-vous répéter ? », « Quelle taille ? »). Si le vendeur répond à "
                 "côté ou fait semblant d'avoir compris, montre-le avec [hesitante] et redis ta "
                 "demande telle quelle. S'il promet sans vérifier, demande-lui s'il est sûr."),
    "fonctionnel": ("Palier fonctionnel : l'employé se débrouille. Tes répliques font une ou "
                    "deux phrases, en français québécois courant. Tu es patient la première "
                    "fois qu'il te fait répéter, un peu moins la troisième."),
    "aise": ("Palier à l'aise : l'employé comprend bien. Tu parles comme un vrai client : deux ou "
             "trois phrases, des expressions québécoises, parfois deux demandes dans la même "
             "phrase. Tu montres ton impatience si on te fait attendre sans rien dire."),
}

# Le débit de la voix, par palier (paliers de /api/voix : None, « lent »).
DEBIT_JEU = {"debutant": "lent", "fonctionnel": None, "aise": None}

# Les cinq gestes : un nom court (≤ 8 mots, audit C5) et la phrase qui le fait.
# Le bilan du magasin les juge un par un (serveur, `bilan` ci-dessous).
GESTES = [
    {"id": "porte",    "nom": "Laisser la porte ouverte",       "phrase": "Je suis là si vous avez besoin."},
    {"id": "preciser", "nom": "Faire préciser une chose à la fois", "phrase": "Quelle couleur ? Quelle taille ?"},
    {"id": "repeter",  "nom": "Faire répéter",                   "phrase": "Pouvez-vous répéter plus lentement ?"},
    {"id": "verifier", "nom": "Redire et vérifier",              "phrase": "Je vais vérifier en arrière."},
    {"id": "relais",   "nom": "Passer le relais",                "phrase": "Je vais chercher la gérante."},
]

# Le bilan de la visite, par geste (audit E1, majeur : le bilan corrigeait la
# grammaire et jamais les gestes, qui sont le but). Le serveur envoie la
# transcription au modèle avec cette consigne et rend du JSON.
BILAN = (
    "Tu es formateur en vente au détail. Voici la transcription d'une visite dans un magasin de "
    "vêtements : un CLIENT (joué par un modèle) et un VENDEUR (un employé immigrant qui apprend le "
    "français). Juge le VENDEUR, geste par geste, sans juger sa grammaire.\n"
    "Les gestes : porte (laisser la porte ouverte quand le client regarde) · preciser (faire préciser "
    "UNE chose à la fois) · repeter (faire répéter au lieu de deviner) · verifier (redire la demande "
    "et vérifier au lieu de promettre) · relais (passer le relais à la gérante pour ce qu'il ne peut "
    "pas décider : argent, dépôt, remboursement, exception ; une mise de côté SANS argent, avec le nom "
    "et le numéro, le vendeur la fait lui-même et ce n'est pas un relais manqué).\n"
    "Pour CHAQUE geste, dis s'il était « necessaire » dans cette visite, s'il a été « fait », cite la "
    "réplique du vendeur qui le montre (ou vide), et donne un conseil d'une phrase courte et simple, "
    "en français facile, qui propose la phrase à dire. Ajoute « resume » : une phrase simple sur ce "
    "qui a marché. Réponds UNIQUEMENT en JSON : {\"gestes\": [{\"id\": \"porte\", \"necessaire\": "
    "true, \"fait\": false, \"citation\": \"…\", \"conseil\": \"…\"}, …], \"resume\": \"…\"}."
)


def scenario_serveur():
    """Le scénario « magasin » tel que /api/jeu-de-role l'attend."""
    cas = {}
    for ident, nom, voix, paliers, carte, portrait, faits in CLIENTS:
        cas[ident] = {
            "contexte": ("La Maison Francœur, un magasin de vêtements de quartier. Un client "
                         "s'adresse à un vendeur ou une vendeuse. " + carte),
            "client": faits,
            "vendeur": ["Tu travailles au plancher de la Maison Francœur."],
        }
    return {
        "cadre": "une conversation au plancher d'un magasin de vêtements, la Maison Francœur",
        # Audit, tour 2 (A2) : la consigne commune disait « niveau 4 » et « deux
        # ou trois phrases », contre le palier débutant ajouté à la fin.
        "niveau": "niveaux 1 à 3 (débutant) ; le palier indiqué à la fin règle ta façon de parler",
        "longueur": "La longueur de chaque réplique suit le palier indiqué à la fin, et ne dépasse jamais deux phrases.",
        "contexte_label": "La situation",
        "cas": cas,
        "adresse": ("Vouvoie le vendeur, comme un client le fait. Le vendeur te vouvoie aussi."),
        "sujets": ["dire ce que tu cherches", "répondre à ce qu'on te demande (couleur, taille)",
                   "réagir à ce que le vendeur propose", "conclure : acheter, essayer, revenir ou "
                   "partir"],
        "cloture": ("Quand ta demande est réglée — tu achètes, tu vas essayer, on te met l'article "
                    "de côté, la gérante arrive — ou quand tu décides de partir, dis-le en une "
                    "phrase, remercie ou salue, et termine ta dernière réplique par le mot FIN."),
        "ouverture": {"vendeur": "Bonjour, bienvenue à la Maison Francœur !",
                      "client": "Bonjour !"},
        "roles": {
            "client": {
                "qui": ("Tu es un client ou une cliente de la Maison Francœur. Le personnage "
                        "précis — nom, besoin, caractère — est dans ce que tu sais, plus bas."),
                "conduite": ("L'élève joue le VENDEUR : c'est un employé immigrant qui apprend "
                             "le français au travail. Tu ne lui fais jamais la leçon. "
                             "Commence CHAQUE réplique par UNE étiquette d'humeur entre "
                             "crochets, parmi exactement : [neutre] [contente] [hesitante] "
                             "[impatiente] — puis ta réplique. Ce n'est pas une balise : "
                             "l'écran la retire et montre ton visage. [contente] quand le "
                             "vendeur t'a compris ou t'a bien aidé ; [hesitante] quand tu ne "
                             "sais pas ou que tu as mal compris ; [impatiente] quand on te fait "
                             "répéter sans avancer ou qu'on insiste ; sinon [neutre]."),
            },
            "vendeur": {
                "qui": "Tu es vendeur ou vendeuse à la Maison Francœur.",
                "conduite": "Tu accueilles poliment et tu aides le client.",
            },
        },
        "paliers": PALIERS_JEU,
        "bilan": BILAN,
    }
