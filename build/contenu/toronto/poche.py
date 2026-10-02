"""La poche d'« Une semaine à Toronto » — ce qu'on garde dans le téléphone, même sans réseau.

Étape 6 (1er oct. 2026). Comme celle de Compostelle, la poche ne réécrit presque
rien : les rubriques par lieu reprennent les phrases « Je le dis » (DIRE) et ce
qu'on peut vous répondre (REPONSES) des exercices, avec LEURS sons. Seules deux
listes sont propres à la poche :
- URGENCES : elles ne se jouent dans aucune scène, et c'est pour ça qu'il faut les
  avoir sous la main ;
- A_MONTRER : les phrases qu'on TEND à quelqu'un, en grand (« plus lentement »,
  « je ne mange pas de viande ») — le plan les promettait (« un écran à montrer »).

2 oct. 2026 : plus aucune allergie dans l'application (décision de Daniel :
responsabilité civile). La réaction allergique cède sa place à la pharmacie la
plus proche, les deux cartes d'allergie à une seule phrase végétarienne.

(id, en, fr). Les sons : poche/<id>.mp3, voix de la narratrice (toronto_commun.py).
"""

URGENCES = [
    ("help", "Help! Please call 911!", "À l'aide ! Appelez le 911, s'il vous plaît !"),
    ("doctor", "I need a doctor, please.", "J'ai besoin d'un médecin, s'il vous plaît."),
    ("hospital", "Where is the nearest hospital?", "Où est l'hôpital le plus proche ?"),
    ("pharmacy", "Where is the nearest pharmacy?", "Où est la pharmacie la plus proche ?"),
    ("lost", "I'm lost. Can you show me on the map?", "Je ne trouve plus mon chemin. Pouvez-vous me montrer sur la carte ?"),
    ("passport", "I lost my passport.", "J'ai perdu mon passeport."),
    ("stolen", "Someone stole my wallet.", "On m'a volé mon portefeuille."),
    ("police", "Where is the police station?", "Où est le poste de police ?"),
]

A_MONTRER = [
    ("slowly", "Could you say that again, more slowly, please?", "Pourriez-vous répéter, plus lentement, s'il vous plaît ?"),
    ("write", "Sorry, my English is not very good. Could you write it down?", "Excusez-moi, mon anglais n'est pas très bon. Pourriez-vous l'écrire ?"),
    ("vegetarian", "I'm vegetarian. I don't eat meat, fish or chicken broth.", "Je suis végétarien ou végétarienne. Je ne mange pas de viande, de poisson ni de bouillon de poulet."),
    ("french", "Do you speak French?", "Parlez-vous français ?"),
]

# Le total à payer : les règles de l'Ontario, les mêmes que les exercices (TAXE dans exercices.py)
# et le cadrage (toronto-etape0.html, faits datés du 1er oct. 2026).
POURBOIRES = [("Restaurant, bar", 18, 20), ("Café, taxi, coiffeur", 10, 15)]


def verifier():
    ids = [i for i, _, _ in URGENCES + A_MONTRER]
    assert len(ids) == len(set(ids)), "deux phrases au même identifiant"
    for i, en, fr in URGENCES + A_MONTRER:
        assert en and fr and i.isidentifier(), i
    return True


if __name__ == "__main__":
    verifier()
    print(f"{len(URGENCES)} urgences, {len(A_MONTRER)} phrases à montrer")
