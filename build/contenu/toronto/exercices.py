"""Les exercices d'« Une semaine à Toronto » — étape 4 (1er oct. 2026).

    python3 build/contenu/toronto/exercices.py   # vérifie et compte

Sept familles, plus la série des faux amis (étape 2). Les leçons de la boucle de
l'étape 1 s'appliquent d'emblée : quatre choix en CARRÉ COMPLET quand deux traits
décident (chaque valeur deux fois : ni la majorité ni l'exception ne désignent la
bonne) ; des choix de longueur voisine ; la place de la bonne TIRÉE AU HASARD à
l'affichage (dans la page) ; chaque mauvais choix dit pourquoi ; les clés orales
passent leurs propres modèles et les réponses témoins.

Familles :
- `entendre` et `souvenir` : tirées des planches par la page (lexique.py), rien à écrire ici.
- REPONSES : « Ce qu'on me répond » — la famille maîtresse : une vraie réponse, dite
  vite par la personne du lieu ; on choisit ce qu'elle veut dire. Deux par lieu.
- NOMBRES : un prix ou une heure, au débit d'un comptoir ; carré (teen/ty, past/to, a.m./p.m.).
- TOTAL : ce que ça coûte vraiment ; carré (prix bien ou mal entendu) × (la règle tenue ou
  non : la taxe, le pourboire — ou, quand l'anglais dit « included », ne pas l'ajouter). Les
  montants se CALCULENT ici, jamais à la main.
- CHEMIN : « Où je vais » ; quatre points sur un petit plan, carré (deux ou trois coins
  de rue) × (à gauche ou à droite).
- DIRE : « Je le dis » ; deux situations par lieu, au micro, puis le modèle.
"""
import importlib.util, pathlib, re

_ici = pathlib.Path(__file__).parent
_sp = importlib.util.spec_from_file_location("toronto_prep_cles", _ici / "preparation.py")
_PR = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_PR)
DEMANDE, REPETER, MAL, ORIGINE, SEJOUR, RELANCE = _PR.DEMANDE, _PR.REPETER, _PR.MAL, _PR.ORIGINE, _PR.SEJOUR, _PR.RELANCE

# ── Ce qu'on me répond : (lieu, qui, contexte, en, [(choix, rétroaction)…]) — la bonne d'abord.
REPONSES = [
    ("union", "kevin", "Vous demandez où prendre le métro.",
     "Take the escalator down, then follow the yellow line to the left.",
     [("Escalier roulant vers le bas, puis la ligne jaune à gauche.", None),
      ("Escalier roulant vers le bas, puis la ligne jaune à droite.", "Down, oui ; mais to the LEFT : à gauche."),
      ("Escalier roulant vers le haut, puis la ligne jaune à gauche.", "À gauche, oui ; mais down : vers le bas."),
      ("Escalier roulant vers le haut, puis la ligne jaune à droite.", "Down : vers le bas ; left : à gauche.")]),
    ("union", "kevin", "Vous voulez payer votre passage.",
     "You can just tap your credit card at the gate. No need to buy a ticket.",
     [("Touchez votre carte au tourniquet ; pas besoin de billet.", None),
      ("Touchez votre carte au tourniquet ; prenez aussi un billet.", "No need to buy a ticket : pas besoin de billet."),
      ("Achetez une carte au guichet ; pas besoin de billet.", "Tap your credit card : votre propre carte de crédit suffit."),
      ("Achetez une carte au guichet ; prenez aussi un billet.", "Tap your credit card, no need : rien à acheter.")]),
    ("hotel", "marcus", "Vous arrivez à l'hôtel à 13 h.",
     "Your room won't be ready until three, but we can keep your bags.",
     [("Chambre prête seulement à 15 h ; on peut garder vos bagages.", None),
      ("Chambre prête seulement à 15 h ; gardez vos bagages avec vous.", "We can keep your bags : on vous les garde."),
      ("Chambre prête tout de suite ; on peut garder vos bagages.", "Won't be ready until three : pas avant 15 h."),
      ("Chambre prête tout de suite ; gardez vos bagages avec vous.", "Not until three : pas avant 15 h ; et on vous garde vos bagages.")]),
    ("hotel", "marcus", "Vous demandez où se prend le déjeuner.",
     "Breakfast is on the second floor, from six thirty to ten.",
     [("Un étage au-dessus de la rue, de 6 h 30 à 10 h.", None),
      ("Deux étages au-dessus de la rue, de 6 h 30 à 10 h.", "Au Canada, le first floor est le niveau de la rue : le second floor est juste au-dessus."),
      ("Un étage au-dessus de la rue, de 6 h à 10 h 30.", "Le thirty va avec six : de 6 h 30 à 10 h."),
      ("Deux étages au-dessus de la rue, de 6 h à 10 h 30.", "Second floor : un étage au-dessus de la rue ; et de 6 h 30 à 10 h.")]),
    ("cafe", "rosa", "Vous demandez un muffin aux bleuets.",
     "Sorry, we're out of blueberry, but we have banana.",
     [("Plus de muffins aux bleuets ; il en reste à la banane.", None),
      ("Plus de muffins aux bleuets ; il en reste aux carottes.", "But we have BANANA : à la banane."),
      ("Plus de muffins au chocolat ; il en reste à la banane.", "Out of BLUEBERRY : ce sont les bleuets qui manquent."),
      ("Plus de muffins au chocolat ; il en reste aux carottes.", "Out of blueberry, but banana : bleuets épuisés, banane disponible.")]),
    ("cafe", "rosa", "Vous payez votre café.",
     "Do you want the receipt in the bag, or should I email it to you?",
     [("Elle demande : le reçu dans le sac, ou par courriel ?", None),
      ("Elle demande : le reçu dans le sac, ou par message texte ?", "Email it to you : par courriel, pas par message texte."),
      ("Elle demande : un sac, ou le reçu par courriel ?", "The receipt in the bag : c'est le reçu qui va dans le sac."),
      ("Elle demande : un sac, ou le reçu par message texte ?", "The receipt in the bag, or email : le reçu, dans le sac ou par courriel.")]),
    ("cafe", "maya", "Maya, croisée au café, vous pose une question.",
     "So, what have you seen so far?",
     [("Ce que vous avez vu pendant le voyage.", None),
      ("Ce que vous avez vu aujourd'hui.", "So far : jusqu'ici, depuis le début du voyage."),
      ("Ce que vous allez voir pendant le voyage.", "What HAVE you seen : ce que vous avez vu, pas ce que vous verrez."),
      ("Ce que vous allez voir aujourd'hui.", "Have you seen, so far : ce que vous avez vu jusqu'ici.")]),
    ("tour", "priya", "Vous demandez deux billets pour la tour.",
     "The next available time is four fifteen. Would that work for you?",
     [("Prochaine montée à 16 h 15 ; ça vous va ?", None),
      ("Prochaine montée à 16 h 50 ; ça vous va ?", "Fifteen finit sur un « n » : 15, pas 50."),
      ("C'est complet jusqu'à 16 h 15.", "Next available time : elle vous propose une heure, ce n'est pas complet."),
      ("C'est complet jusqu'à 16 h 50.", "Elle propose 4 h 15 de l'après-midi : rien n'est complet.")]),
    ("tour", "priya", "Vous demandez s'il y a un rabais pour les aînés.",
     "Seniors get twenty percent off, but only on weekdays.",
     [("20 % de rabais pour les aînés, en semaine seulement.", None),
      ("30 % de rabais pour les aînés, en semaine seulement.", "Twenty : 20. Trente, ce serait thirty."),
      ("20 % de rabais pour les aînés, la fin de semaine seulement.", "Weekdays : les jours de semaine, du lundi au vendredi."),
      ("30 % de rabais pour les aînés, la fin de semaine seulement.", "Twenty percent, on weekdays : 20 %, en semaine.")]),
    ("marche", "wei", "Vous commandez du fromage au poids.",
     "That's half a pound. It comes to six eighty.",
     [("Une demi-livre ; ça fait 6,80 $.", None),
      ("Une demi-livre ; ça fait 6,18 $.", "Eighty finit court : 80, pas 18."),
      ("Une livre et demie ; ça fait 6,80 $.", "Half a pound : une demi-livre."),
      ("Une livre et demie ; ça fait 6,18 $.", "Half a pound : une demi-livre ; et six eighty, 6,80 $.")]),
    ("marche", "wei", "Vous demandez si vous pouvez payer par carte.",
     "Cash only at this counter, but there's a machine by the door.",
     [("Comptant seulement ; un guichet juste à côté de la porte.", None),
      ("Comptant seulement ; un guichet au fond du marché.", "By the door : près de la porte."),
      ("La carte est acceptée ; un guichet juste à côté de la porte.", "Cash only : comptant seulement."),
      ("La carte est acceptée ; un guichet au fond du marché.", "Cash only : comptant ; et la machine est by the door.")]),
    ("kensington", "raj", "Vous cherchez le tramway de Spadina.",
     "Walk over to Spadina — it's two blocks east — and take it southbound.",
     [("Deux coins de rue vers l'est ; le prendre en direction sud.", None),
      ("Deux coins de rue vers l'ouest ; le prendre en direction sud.", "East : l'est. L'ouest, ce serait west."),
      ("Deux coins de rue vers l'est ; le prendre en direction nord.", "Southbound : en direction sud."),
      ("Deux coins de rue vers l'ouest ; le prendre en direction nord.", "Two blocks EAST, southbound : à l'est, vers le sud.")]),
    ("kensington", "raj", "Vous demandez si c'est loin.",
     "Not at all, it's a five-minute walk. You can't miss it.",
     [("Pas loin : cinq petites minutes à pied, impossible à manquer.", None),
      ("Pas loin : quinze minutes à pied, impossible à manquer.", "Five : cinq. Quinze, ce serait fifteen."),
      ("Pas loin : cinq petites minutes en autobus, impossible à manquer.", "A five-minute WALK : à pied."),
      ("Pas loin : quinze minutes en autobus, impossible à manquer.", "A five-minute walk : cinq minutes, à pied.")]),
    ("iles", "kevin", "Vous voulez louer un vélo sur l'île.",
     "Bikes are fifteen dollars an hour, and we need a piece of ID.",
     [("15 $ l'heure ; il faut laisser une pièce d'identité.", None),
      ("50 $ l'heure ; il faut laisser une pièce d'identité.", "Fifteen finit sur un « n » : 15, pas 50."),
      ("15 $ l'heure ; il faut laisser une carte de crédit.", "A piece of ID : une pièce d'identité."),
      ("50 $ l'heure ; il faut laisser une carte de crédit.", "Fifteen dollars, a piece of ID : 15 $, une pièce d'identité.")]),
    ("iles", "kevin", "Vous demandez l'heure du dernier traversier.",
     "The last ferry back to the city is at eleven forty-five tonight.",
     [("Le dernier retour vers la ville : 23 h 45.", None),
      ("Le dernier retour vers la ville : 23 h 15.", "Forty-five, pas fifteen : 23 h 45."),
      ("Le dernier départ vers l'île : 23 h 45.", "Back to the city : le retour vers la ville."),
      ("Le dernier départ vers l'île : 23 h 15.", "Back to the city, at eleven forty-five : le retour, à 23 h 45.")]),
    ("pharmacie", "tom", "Vous montrez votre coup de soleil.",
     "Put this cream on twice a day, and stay out of the sun for a couple of days.",
     [("La crème deux fois par jour ; évitez le soleil quelques jours.", None),
      ("La crème une fois par jour ; évitez le soleil quelques jours.", "Twice : deux fois."),
      ("La crème deux fois par jour ; de l'écran solaire avant de sortir.", "Stay out of the sun : évitez le soleil."),
      ("La crème une fois par jour ; de l'écran solaire avant de sortir.", "Twice a day, stay out of the sun : deux fois, et pas de soleil.")]),
    ("pharmacie", "tom", "Vous demandez s'il faut une ordonnance.",
     "You don't need a prescription for this, but don't take it with alcohol.",
     [("Sans ordonnance ; pas d'alcool avec ce médicament.", None),
      ("Sans ordonnance ; pas à jeun avec ce médicament.", "With alcohol : avec de l'alcool."),
      ("Il faut une ordonnance ; pas d'alcool avec ce médicament.", "You DON'T need a prescription : pas besoin d'ordonnance."),
      ("Il faut une ordonnance ; pas à jeun avec ce médicament.", "Pas d'ordonnance, et pas d'alcool.")]),
    ("resto", "ada", "Vous dites que vous êtes allergique aux noix.",
     "The pasta is fine, but the dessert has almonds, so I'd skip it.",
     [("Les pâtes, ça va ; le dessert contient des amandes.", None),
      ("Les pâtes, ça va ; le dessert est sans noix.", "The dessert HAS almonds : il en contient — évitez-le."),
      ("Les pâtes contiennent des noix ; le dessert contient des amandes.", "The pasta is FINE : les pâtes, ça va."),
      ("Les pâtes contiennent des noix ; le dessert est sans noix.", "C'est l'inverse : les pâtes, ça va ; le dessert, non.")]),
    ("resto", "ada", "Vous demandez une table pour deux.",
     "It's about a twenty-minute wait, or you can sit at the bar right now.",
     [("Environ 20 minutes d'attente, ou le bar tout de suite.", None),
      ("Environ 30 minutes d'attente, ou le bar tout de suite.", "Twenty : 20. Trente, ce serait thirty."),
      ("Environ 20 minutes d'attente, ou la terrasse tout de suite.", "At the bar : au bar."),
      ("Environ 30 minutes d'attente, ou la terrasse tout de suite.", "Twenty minutes, or the bar : 20 minutes, ou le bar.")]),
    ("depart", "marcus", "Vous contestez des frais de minibar sur votre facture.",
     "You're right, the minibar charge is a mistake. I'll take it off.",
     [("C'est une erreur, vous avez raison ; il l'enlève tout de suite.", None),
      ("C'est une erreur, vous avez raison ; on vous remboursera plus tard.", "I'll take it off : il l'enlève maintenant."),
      ("Il doit d'abord vérifier ; il l'enlève tout de suite.", "You're right, a mistake : il reconnaît l'erreur, sans vérifier."),
      ("Il doit d'abord vérifier ; on vous remboursera plus tard.", "You're right, I'll take it off : erreur reconnue, enlevée.")]),
    ("depart", "marcus", "Vous demandez où prendre l'UP Express.",
     "Go back to Union. It's on the upper level, and trains leave every fifteen minutes.",
     [("À Union, au niveau du haut ; un train aux 15 minutes.", None),
      ("À Union, au niveau du haut ; un train aux 50 minutes.", "Fifteen finit sur un « n » : aux 15 minutes."),
      ("À Union, au sous-sol ; un train aux 15 minutes.", "The upper level : le niveau du haut."),
      ("À Union, au sous-sol ; un train aux 50 minutes.", "Upper level, every fifteen minutes : en haut, aux 15 minutes.")]),
]

# ── Les nombres, les prix, les heures : (qui, en, [(choix, rétroaction)…]) — carrés.
NOMBRES = [
    ("liam", "That's fourteen fifty.", [("14,50 $", None), ("40,50 $", "Fourteen finit sur un « n » : 14."), ("14,15 $", "Fifty finit court : 50 cents."), ("40,15 $", "Fourteen fifty : 14,50 $.")]),
    ("rosa", "Your total is sixteen thirty.", [("16,30 $", None), ("60,30 $", "Sixteen finit sur un « n » : 16."), ("16,13 $", "Thirty finit court : 30 cents."), ("60,13 $", "Sixteen thirty : 16,30 $.")]),
    ("sam", "That comes to nineteen ninety.", [("19,90 $", None), ("90,90 $", "Nineteen finit sur un « n » : 19."), ("19,19 $", "Ninety finit court : 90 cents."), ("90,19 $", "Nineteen ninety : 19,90 $.")]),
    ("andrew", "It's seventy forty.", [("70,40 $", None), ("70,14 $", "Forty finit court : 40 cents."), ("17,40 $", "Seventy finit court : 70."), ("17,14 $", "Seventy forty : 70,40 $.")]),
    ("ezinne", "The bill is eighty thirteen.", [("80,13 $", None), ("80,30 $", "Thirteen finit sur un « n » : 13 cents."), ("18,13 $", "Eighty finit court : 80."), ("18,30 $", "Eighty thirteen : 80,13 $.")]),
    ("aarti", "It's thirty seventeen, with tax.", [("30,17 $", None), ("30,70 $", "Seventeen finit sur un « n » : 17 cents."), ("13,17 $", "Thirty finit court : 30."), ("13,70 $", "Thirty seventeen : 30,17 $.")]),
    ("harper", "The tour starts at quarter to seven, p.m.", [("18 h 45", None), ("19 h 15", "Quarter TO : moins quart."), ("6 h 45", "P.m. : le soir."), ("7 h 15", "Quarter to seven, p.m. : 18 h 45.")]),
    ("liam", "The gates open at quarter past nine, a.m.", [("9 h 15", None), ("8 h 45", "Quarter PAST : et quart."), ("21 h 15", "A.m. : le matin."), ("20 h 45", "Quarter past nine, a.m. : 9 h 15.")]),
    ("andrew", "Check-out is at half past eleven.", [("11 h 30", None), ("11 h 50", "Half n'est pas fifty : half past, et demie."), ("11 h 15", "Half past : et demie, pas et quart."), ("11 h 45", "Half past eleven : 11 h 30.")]),
    ("sam", "We close at twenty to ten tonight.", [("21 h 40", None), ("22 h 20", "Twenty TO ten : dix heures moins vingt."), ("9 h 40", "Tonight : ce soir."), ("10 h 20", "Twenty to ten, tonight : 21 h 40.")]),
    ("rosa", "The kitchen closes at nine fifteen, and the bar at eleven.", [("Cuisine 21 h 15, bar 23 h", None), ("Cuisine 21 h 50, bar 23 h", "Fifteen finit sur un « n » : 15."), ("Cuisine 21 h 15, bar 1 h", "Eleven : onze, donc 23 h."), ("Cuisine 21 h 50, bar 1 h", "Nine fifteen, eleven : 21 h 15 et 23 h.")]),
    ("arjun", "Gate eighteen, boarding in about forty minutes.", [("Porte 18, embarquement dans environ 40 minutes", None), ("Porte 80, embarquement dans environ 40 minutes", "Eighteen finit sur un « n » : 18."), ("Porte 18, embarquement dans environ 14 minutes", "Forty finit court : 40."), ("Porte 80, embarquement dans environ 14 minutes", "Eighteen, forty : porte 18, 40 minutes.")]),
]

# ── Le total à payer : (lieu, qui, contexte, en, prix entendu, prix mal entendu, pourboire %, mot du prix, inclus).
# Tour 1 (majeur) : le contexte ne dit plus « pas de pourboire » et l'anglais décide. Les quatre choix
# forment un carré (prix bien ou mal entendu, teen/ty) × (la règle tenue ou non). Tout se CALCULE dans total().
# Tour 2 (majeur) : sans écouter, « le plus grand de la paire » gagnait 6 sur 6 (la règle ne faisait
# qu'ajouter), et le prix mal entendu se rejetait au bon sens (70 $ un sandwich). Les deux lectures sont
# maintenant vraisemblables, et deux items disent ce qui est DÉJÀ compris (« included », « no tax ») :
# la règle tenue n'ajoute rien, l'erreur ajoute deux fois.
TOTAL = [
    ("magasin", "rosa", "Une tuque.", "That's fourteen, plus tax.", 14.00, 40.00, 0, "fourteen", ""),
    ("magasin", "priya", "Un chandail.", "That's ninety, plus tax.", 90.00, 19.00, 0, "ninety", ""),
    ("resto", "ada", "Vous laissez 18 % du prix avant taxe.", "Your bill is fifty, before tax.", 50.00, 15.00, 18, "fifty", ""),
    ("resto", "ada", "Vous laissez 20 % du prix avant taxe.", "That's sixteen, before tax.", 16.00, 60.00, 20, "sixteen", ""),
    ("marche", "wei", "Du fromage au poids, pour une fête.", "That's eighteen. No tax on cheese.", 18.00, 80.00, 0, "eighteen", "taxe"),
    ("resto", "ada", "En groupe. D'habitude, vous laissez 18 % du prix avant taxe.", "That's one-forty, tip included, plus tax.", 140.00, 114.00, 18, "forty", "pourboire"),
]
TAXE = 0.13
# Un seul texte pour teen/ty, le même que les pièges du lexique (mineur du tour 2 : deux indices différents).
TEEN_TY = "-teen : l'accent tombe sur TEEN, et le « n » s'entend ; -ty : l'accent au début, la fin est brève"


def total(prix, mal, pb, mot, inclus=""):
    """Les quatre choix (montant, rétroaction), la bonne d'abord, et le calcul de la bonne."""
    def m(prix_, tenue):
        t = round(prix_ * TAXE, 2); p = round(prix_ * pb / 100, 2)
        if inclus == "taxe":                       # pas de taxe : l'erreur est de l'ajouter
            return round(prix_ + (0 if tenue else t), 2)
        if inclus == "pourboire":                  # pourboire compris : l'erreur est de l'ajouter encore
            return round(prix_ + t + (0 if tenue else p), 2)
        if tenue:
            return round(prix_ + t + p, 2)
        return round(prix_ + t, 2) if pb else round(prix_, 2)   # oublié : le pourboire (resto, café), la taxe (ailleurs)
    if inclus == "taxe":
        faute = "« No tax » : pas de taxe sur ce produit, il ne faut pas l'ajouter."
    elif inclus == "pourboire":
        faute = f"« Tip included » : le pourboire est déjà compris, il ne faut pas ajouter {pb} % de plus."
    else:
        faute = "il manque " + (f"le pourboire de {pb} %, calculé sur le prix avant taxe" if pb else "la taxe de 13 %, ajoutée à la caisse") + "."
    oreille = f"« {mot} » : {prix:.0f} $, pas {mal:.0f} $ ({TEEN_TY})."
    choix = [(m(prix, True), None),
             (m(mal, True), oreille),
             (m(prix, False), f"Le prix est juste ; mais {faute}" if not inclus else f"Le prix est juste ; mais {faute}"),
             (m(mal, False), f"{oreille} Et {faute[0].lower() + faute[1:] if not inclus else faute}")]
    t = round(prix * TAXE, 2); p = round(prix * pb / 100, 2)
    if inclus == "taxe":
        calcul = f"{prix:.2f} $, sans taxe = {prix:.2f} $"
    elif inclus == "pourboire":
        calcul = f"{prix:.2f} $ + {t:.2f} $ de taxe, pourboire déjà compris = {m(prix, True):.2f} $"
    else:
        calcul = f"{prix:.2f} $ + {t:.2f} $ de taxe" + (f" + {p:.2f} $ de pourboire" if pb else "") + f" = {m(prix, True):.2f} $"
    return choix, calcul.replace(".", ",")


# ── L'allergie (O3, éliminatoire) : la série JOUÉE EN ENTIER (bloquant du tour 1 : elle n'existait pas).
# Carré (allergène ou non) × (elle en est sûre ou elle va vérifier), et un contre-exemple : le plat sans
# danger qu'on peut commander (piège connu « seulement le geste prudent »). La règle est affichée avant.
# Ce que dit le micro quand une GARDE rate (une clé vraie sur la phrase vide : elle refuse un geste faux).
# Tour 4 (majeur) : « Presque. Il manque : I'll » répondait à qui commandait le saumon douteux.
GARDES = {"La serveuse n'est pas sûre": "Vous commandez le saumon, et elle n'est pas sûre qu'il soit sans noix. Prenez autre chose.",
          "Dites que vous êtes allergique": "Votre phrase dit que vous n'êtes PAS allergique.",
          "Dites que vous avez une réservation": "C'est vous qui avez la réservation : « I have a reservation… »."}


def garde(fr):
    return next((v for k, v in GARDES.items() if fr.startswith(k)), "")


REGLE_ALLERGIE = ("Une allergie se dit avant de commander. On commande seulement si la réponse est sûre : pas "
                  "d'allergène. S'il y en a, s'il peut y en avoir des traces, ou si la personne n'est pas sûre : on "
                  "attend la vérification, ou on prend autre chose.")
# Les deux moitiés de même longueur dans chaque colonne : aucune ne se trahit par la taille.
_SAUMON = ["Saumon sans noix ; elle en est tout à fait certaine.", "Saumon sans noix ; elle va vérifier en cuisine.",
           "Saumon avec noix ; elle en est tout à fait certaine.", "Saumon avec noix ; elle va vérifier en cuisine."]
# Le marché : un carré (traces ou non) × (on en prend ou non), les mêmes quatre choix pour les deux items.
_MARCHE = ["Faits là où il y a des arachides : on n'en prend pas.", "Faits là où il y a des arachides : on peut en prendre.",
           "Sans aucune arachide : on n'en prend pas.", "Sans aucune arachide : on peut en prendre."]
ALLERGIE = [
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "The salmon is fine, there are no nuts in it.", 0, "Elle en est sûre : ici, vous pouvez commander le saumon.",
     {1: "No nuts : aucune ; et elle n'a pas à vérifier, elle le sait.", 2: "There are NO nuts : il n'y en a pas.",
      3: "The salmon is fine : pas de noix, et elle en est sûre."}),
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "I don't think there are pecans in the salmon, but let me check with the kitchen.", 1,
     "Elle n'en est pas sûre : on attend la réponse de la cuisine, ou on prend autre chose.",
     {0: "I don't THINK there are pecans, let me check : elle croit, mais elle va vérifier.", 2: "No pecans, I think : elle croit qu'il n'y en a pas.",
      3: "I don't think there are pecans : elle croit qu'il n'y en a PAS."}),
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "The salmon has a pecan crust, so I wouldn't order it.", 2, "Des pacanes, ce sont des noix : on ne le commande pas.",
     {0: "A pecan crust : une croûte de pacanes, ce sont des noix.", 1: "Elle est sûre : la croûte est faite de pacanes.",
      3: "Elle n'a rien à vérifier : la croûte est aux pacanes."}),
    # Tour 2 (majeur) : trois saumons aux mêmes choix, et la quatrième case jamais juste — le troisième se
    # déduisait des deux autres. Six réponses couvrent les quatre cases ; la page en tire trois par série.
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "I think the sauce has pecans in it, but let me check with the kitchen.", 3,
     "Elle croit qu'il y en a, et va vérifier : on ne le commande pas pour l'instant.",
     {0: "I think the sauce HAS pecans : elle croit qu'il y en a.", 1: "Has pecans : elle croit qu'il y a des noix, pas l'inverse.",
      2: "I think, let me check : elle n'en est pas sûre, elle va vérifier."}),
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "No almonds, no pecans in the salmon. The chef just told me.", 0, "Elle en est sûre, le chef vient de le lui dire : vous pouvez le commander.",
     {1: "The chef just told me : elle n'a plus à vérifier, elle le sait.", 2: "No almonds, no pecans : aucune noix.",
      3: "No pecans, the chef told me : aucune, et c'est certain."}),
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "Yes, the salmon comes with sliced almonds on top.", 2, "Des amandes, ce sont des noix : on ne le commande pas.",
     {0: "Sliced almonds : des amandes tranchées, ce sont des noix.", 1: "Yes, it comes with almonds : elle en est sûre.",
      3: "Elle n'a rien à vérifier : les amandes sont sur le saumon."}),
    ("wei", "Au marché, vous êtes allergique aux arachides. Vous demandez pour les biscuits.",
     "These cookies are made in a bakery that uses peanuts.", None,
     "Uses peanuts : des traces sont possibles. La règle : un doute ou des traces, on n'en prend pas.",
     [(_MARCHE[0], None),
      (_MARCHE[1], "A bakery that USES peanuts : il peut y en avoir des traces."),
      (_MARCHE[2], "That uses peanuts : la boulangerie en utilise ; les biscuits peuvent en contenir des traces."),
      (_MARCHE[3], "Uses peanuts : il y en a là où on les fait.")]),
    # Tour 3 (majeur) : le marché était toujours « on n'en prend pas » — seul le geste prudent. Un second
    # marché où l'on PEUT en prendre ; la page tire un des deux par série. Deux saumons de plus : deux par case.
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "There shouldn't be any pecans in the salmon, but I'll ask the chef to be sure.", 1,
     "Elle n'en est pas sûre : on attend la réponse du chef, ou on prend autre chose.",
     {0: "Shouldn't be, I'll ask : elle croit, mais elle va demander.", 2: "There SHOULDN'T be any : elle croit qu'il n'y en a pas.",
      3: "Shouldn't be any pecans : elle croit qu'il n'y en a PAS."}),
    ("ada", "Vous êtes allergique aux noix. Vous demandez si le saumon en contient.",
     "I think the glaze has pecans on it, but I'll ask the chef.", 3,
     "Elle croit qu'il y en a, et va demander : on ne le commande pas pour l'instant.",
     {0: "I think the glaze HAS pecans : elle croit qu'il y en a.", 1: "Has pecans : elle croit qu'il y a des noix, pas l'inverse.",
      2: "I think, I'll ask : elle n'en est pas sûre, elle va demander."}),
    ("wei", "Au marché, vous êtes allergique aux arachides. Vous demandez pour les biscuits.",
     "These come from our peanut-free bakery. No peanuts ever go in there.", None,
     "Peanut-free : sans arachides, ni traces. Vous pouvez en prendre.",
     [(_MARCHE[3], None),
      (_MARCHE[2], "Peanut-free, no peanuts ever : aucune arachide, rien n'empêche d'en prendre."),
      (_MARCHE[1], "Peanut-free : la boulangerie n'en utilise jamais."),
      (_MARCHE[0], "No peanuts EVER : aucune arachide, aucune trace.")]),
]


def choix_allergie(it):
    """Les quatre choix d'un item d'allergie, la bonne d'abord."""
    qui, ctx, en, bon, apres, retro = it
    if bon is None:
        return retro
    return [(_SAUMON[bon], None)] + [(_SAUMON[i], retro[i]) for i in range(4) if i != bon]


# ── Où je vais : (qui, en, blocs, tourner) — on part de l'étoile, face au nord ; après le virage,
# toujours UN coin de rue de plus (le plan le montre ainsi : sans ce « one more block », la phrase
# désignait le coin du virage, et la bonne lecture menait au mauvais point).
# Les quatre points : (2 ou 3 coins de rue) × (à gauche ou à droite) → carré complet.
CHEMIN = [
    ("arjun", "Go straight two blocks, then turn left and go one more block. It's on that corner.", 2, "gauche"),
    ("liam", "Go up three blocks, turn right, and walk one more block. It's on the corner.", 3, "droite"),
    ("harper", "Walk two blocks north, turn right, then one more block. It's right there.", 2, "droite"),
    ("arjun", "Three blocks straight ahead, then left for one block. It's on the corner.", 3, "gauche"),
    ("sam", "Go two blocks, turn left, go one more block, and it's right in front of you.", 2, "gauche"),
    ("ezinne", "Keep going three blocks, then make a right and go one block. It's on the corner.", 3, "droite"),
]

# ── Je le dis : (lieu, situation fr, modèle en, clés) — deux par lieu.
DIRE = [
    ("union", "Demandez où est le métro.", "Where is the subway?", ["~(^| )(where|which way|how (do|can) (i|we) get to|is there|looking for)", "subway|ttc|metro|station|train"]),
    ("union", "Vous n'avez pas compris l'agent. Demandez-lui de répéter.", "Sorry, could you say that again?", [REPETER]),
    ("union", "Demandez si vous pouvez payer avec votre carte de crédit.", "Can I pay with my credit card?", ["~(card|credit|visa|tap)", "~(can i|do you|is it|could i|okay|ok)"]),
    ("hotel", "Dites que vous avez une réservation au nom de Tremblay.", "I have a reservation under Tremblay.", ["~(^| )(reservation|booking|booked|reserved)( |$)", "~(^| )(trembl|trambl|tremble)[a-z]*( |$)", "~^(?!.*(^| )do you have a reservation)"]),
    ("hotel", "Demandez à quelle heure est le déjeuner.", "What time is breakfast?", ["what time|when", "breakfast"]),
    ("cafe", "Commandez un grand café pour emporter.", "Can I get a large coffee to go?", [DEMANDE, "large", "coffee", "~(to go|takeout|take out)"]),
    ("cafe", "On vous demande « Anything else? ». Répondez que c'est tout.", "That's it, thanks!", ['~^(?!.*(^| )but( |$))(?!.*(^| )(yes|yeah|also|plus|and (a|an|one|two|some|the)|can i (get|have)|i ll (have|take)|i d like)( |$))(?!.*(^| )(a|an|one|two|some) ([a-z]+ )?(muffin|cookie|bagel|donut|croissant|sandwich|tea|coffee|water|juice|scone|lemonade|cake|pastry)).*(that s it|that s all|that s everything|that is it|that is all|that is everything|that ll be all|that will be all|that ll do|that s fine|it s fine|nothing else|(^| )nothing( |$)|no thanks|no thank you|(i m|im|we re) (good|ok|okay|fine|all set)|all good|all set|just (the|my|this|that)( [a-z]+){0,2}( thanks| thank you| please)?$|^no (thanks )?just (the|my|this|that)|just that|^(no|nope|nah)( sorry)?$)']),
    ("cafe", "Maya vous demande « Where are you from? ». Répondez, puis relancez.", "I'm from Quebec. And you?", [ORIGINE, RELANCE]),
    ("tour", "Demandez deux billets pour adultes.", "Two adult tickets, please.", ["two|2", "adult|adults"]),
    ("tour", "Demandez s'il y a un rabais pour les aînés.", "Is there a discount for seniors?", ["discount|reduced|cheaper|deal|price|rate|special", "senior|seniors|older"]),
    ("tour", "Maya vous demande combien de temps vous restez. Répondez, puis relancez.", "We're here for a week. How about you?", [SEJOUR, RELANCE]),
    ("marche", "Commandez un sandwich au bacon de dos.", "Can I get a peameal bacon sandwich?", [DEMANDE, "sandwich", "peameal|bacon"]),
    ("marche", "Demandez combien ça coûte.", "How much is it?", ["how much|what s the price|what is the price|price"]),
    ("kensington", "Dites que vous êtes perdu et demandez de l'aide.", "Excuse me, I'm lost. Can you help me?", ["lost", "~(help|can you|could you)"]),
    ("kensington", "Demandez si c'est loin à pied.", "Is it far to walk?", ["~(^| )(is it|is that) (far|close|near)( |$)|(^| )how (far|long (does it take|is the walk|to walk))|(^| )(can|could) (i|we) walk( |$)|walking distance"]),
    ("iles", "Demandez à louer un vélo pour deux heures.", "Can I rent a bike for two hours?", ["rent|get|borrow|have|want|like|need|take", "bike|bicycle", "two|2"]),
    ("iles", "Demandez à quelle heure est le dernier traversier.", "What time is the last ferry?", ["what time|when", "last", "ferry|boat"]),
    ("pharmacie", "Dites que vous avez un coup de soleil.", "I have a sunburn.", [MAL, "~(^| )(sunburn|sunburns|sunburned|sunburnt|burn|burned|burnt)( |$)"]),
    ("pharmacie", "Demandez combien de fois par jour mettre la crème.", "How many times a day?", ["~(how many times|how often)"]),
    ("resto", "Dites que vous êtes allergique aux noix.", "I'm allergic to nuts.", ["allergic|allergy|allergies", '~^(?!.*(^| )(not|n t|no|don t have|do not have|never)( (a|an|any))?( [a-z]+)? (allergic|allergy|allergies)( |$))', 'nuts|nut|tree nut|almond|walnut|cashew|pecan|hazelnut|pistachio']),
    ("resto", "Demandez s'il y a des noix dans ce plat.", "Does this have any nuts in it?", ['~^(?!.*(^| )(i|we|my [a-z]+) (have|has|m|am|re|are|got)( |$))(?!.*(^| )(do you|you) (like|sell)( |$))(?=.*(^| )(does|do|is|are|any|contain|contains|safe)( |$))', 'nuts|nut|tree nut|almond|walnut|cashew|pecan|hazelnut|pistachio']),
    ("resto", "La serveuse n'est pas sûre pour le saumon. Dites que vous prendrez autre chose.", "I'll have something else, then.", ['~(something else|something different|(^| )instead( |$)|(^| )other( |$)|skip|(^| )pass( on)?( |$)|(not|don t|do not|won t|will not) (take|have|order|get|want|eat)|(^| )avoid|no (thanks|thank you)|never mind|forget it|(^| )menu( |$)|(^| )not the|no salmon|(^| )(i ll|i will|i d|i would|let s|can i|could i|may i|give me|i want|i prefer|i d prefer|i d rather|i would rather|maybe|then|go for|go with)( [a-z]+){0,3} (the|a|an|some) (?!salmon( |$))[a-z]+|(^| )(the|a) (?!salmon( |$))[a-z]+ (instead|then|please)( |$))', '~^(?!.*(^| )(salmon|fish)( |$))|(^| )(no|not|don t|do not|skip|without|pass on|won t|will not|avoid)( [a-z]+){0,2} (the )?(salmon|fish)( |$)']),
    ("resto", "Demandez des additions séparées.", "Can we get separate bills?", ["separate|split|separately", "~(bill|check|pay)"]),
    ("depart", "Dites poliment qu'il y a une erreur sur la facture.", "Sorry, I think there's a mistake on my bill.", ["mistake|error|wrong", "bill|invoice|charge"]),
    ("depart", "Demandez où prendre le train pour l'aéroport.", "Where can I take the train to the airport?", ["~(^| )(where|which way|how (do|can) (i|we) get)", "airport|up express|train|pearson"]),
]

# Les réponses témoins des clés neuves (leçon de l'étape 1 : une clé se prouve dans les deux sens).
def _cle(fr_debut, i):
    """La i-e clé de la phrase à dire dont la situation commence ainsi (les indices bougent ; le texte, non)."""
    return next(d[3][i] for d in DIRE if d[1].startswith(fr_debut))


REFUS = [
    (_cle("On vous demande « Anything", 0), "Yes, a muffin"),
    (_cle("Dites que vous êtes allergique", 0), "I like nuts"),
    (_cle("Dites que vous êtes allergique", 1), "I'm not allergic to nuts"),
    (_cle("Demandez si c'est loin", 0), "I want to walk"),
    (_cle("Demandez si c'est loin", 0), "How long is the movie?"),
    (_cle("Dites que vous avez une réservation", 2), "Do you have a reservation for Tremblay?"),
    (_cle("Demandez deux billets", 1), "Two tickets for kids"),
    (_cle("Demandez où est le métro", 0), "I'd like to go somewhere by subway"),
    (_cle("Commandez un grand café", 3), "Can I get a large coffee for here?"),
    (_cle("Demandez s'il y a des noix", 1), "I like it"),
    (_cle("La serveuse n'est pas sûre", 0), "I'll take it"),
    (_cle("La serveuse n'est pas sûre", 0), "I'll take the salmon."),
    (_cle("La serveuse n'est pas sûre", 0), "I'll have the salmon, please."),
    (_cle("On vous demande « Anything", 0), "Nothing, but a muffin please"),
    (_cle("Demandez s'il y a des noix", 0), "Do you like nuts?"),
    # Tour 3 : le saumon avec un adjectif, l'arachide prise pour la noix, les négations, les affirmations.
    (_cle("La serveuse n'est pas sûre", 1), "Never mind, I'll take the salmon."),
    (_cle("La serveuse n'est pas sûre", 1), "I'll have the grilled salmon, please."),
    (_cle("La serveuse n'est pas sûre", 1), "No thanks, I'll have the salmon."),
    (_cle("La serveuse n'est pas sûre", 1), "I'll have the smoked salmon."),
    (_cle("La serveuse n'est pas sûre", 1), "I'll have the salmon instead"),
    (_cle("La serveuse n'est pas sûre", 1), "I'd rather have the salmon"),
    (_cle("La serveuse n'est pas sûre", 1), "Give me the salmon"),
    (_cle("On vous demande « Anything", 0), "No, a muffin"),
    (_cle("Dites que vous êtes allergique", 2), "I'm allergic to peanuts."),
    (_cle("Dites que vous êtes allergique", 1), "I don't have a nut allergy."),
    (_cle("Dites que vous êtes allergique", 1), "I have no nut allergy."),
    (_cle("Demandez s'il y a des noix", 0), "I have a nut allergy."),
    (_cle("Demandez s'il y a des noix", 0), "Do you sell nuts?"),
    (_cle("Demandez s'il y a des noix", 1), "Are there any peanuts in it?"),
    (_cle("On vous demande « Anything", 0), "An orange juice, and that's all."),
    (_cle("On vous demande « Anything", 0), "Yes please, a lemonade, that's it."),
]
ACCEPTE = [
    (_cle("On vous demande « Anything", 0), "No thanks, that's all"),
    (_cle("On vous demande « Anything", 0), "Nothing, thanks"),
    (_cle("On vous demande « Anything", 0), "Nope, all good"),
    (_cle("Dites que vous êtes allergique", 2), "I have an allergy to almonds"),
    (_cle("Demandez des additions", 0), "Can we pay separately?"),
    (_cle("Demandez si c'est loin", 0), "Is it close?"),
    (_cle("Demandez si c'est loin", 0), "Is it near here?"),
    (_cle("Dites que vous avez une réservation", 1), "I have a reservation under Trembley"),
    (_cle("Demandez s'il y a un rabais", 0), "Senior price?"),
    (_cle("Demandez à louer un vélo", 0), "I want a bike for two hours"),
    (_cle("Demandez où prendre le train", 1), "How can we get to Pearson?"),
    (_cle("Demandez s'il y a des noix", 0), "Are there any almonds in it?"),
    (_cle("Demandez s'il y a des noix", 0), "Is it nut-free?"),
    (_cle("Demandez s'il y a des noix", 0), "Is it safe for a nut allergy?"),
    (_cle("La serveuse n'est pas sûre", 0), "I'll have something else"),
    (_cle("La serveuse n'est pas sûre", 0), "I don't want it"),
    (_cle("La serveuse n'est pas sûre", 0), "Never mind, I'll have the pasta"),
    (_cle("On vous demande « Anything", 0), "That's everything"),
    (_cle("On vous demande « Anything", 0), "I'm all set."),
    (_cle("On vous demande « Anything", 0), "Just the coffee, thanks."),
    (_cle("On vous demande « Anything", 0), "No, that's fine."),
    (_cle("La serveuse n'est pas sûre", 0), "I'd like the pasta."),
    (_cle("La serveuse n'est pas sûre", 0), "I prefer the chicken."),
    (_cle("La serveuse n'est pas sûre", 0), "Give me the pasta."),
    (_cle("La serveuse n'est pas sûre", 1), "I'll pass on the salmon."),
    (_cle("La serveuse n'est pas sûre", 1), "I won't take the salmon."),
    (_cle("On vous demande « Anything", 0), "Nope."),
    (_cle("La serveuse n'est pas sûre", 0), "I'll skip the salmon."),
    (_cle("La serveuse n'est pas sûre", 1), "No salmon for me, then."),
]
# Les voisins trop proches, exclus des familles « entendre » et « souvenir » : deux choix vrais à la fois
# (bloc et coin, médicament et comprimé), ou un choix qui se trouve sans comprendre (le nom propre, le prix).
PROCHES = [{"block", "corner", "intersection"}, {"drug", "pill", "pharmacy"}, {"museum", "gallery"},
           {"coffee", "double_double"}, {"room", "double_bed", "two_beds"}, {"cash", "change"},
           {"check_in", "reservation"}, {"to_go", "bag"}]
HORS_SERIE = {"intersection", "hockey", "price_four99", "thirteen", "fifteen", "peameal"}


def verifier(lieux, voix, gens):
    """Ce qui casse un exercice sans lever d'erreur."""
    qui_ok = set(voix)   # NOMBRES et CHEMIN nomment des VOIX ; REPONSES et TOTAL, des personnes de semaine.py
    for l, q, ctx, en, ch in REPONSES:
        assert l in lieux and q in gens, (l, q)
        _choix(ch, en, carre=True)
    for q, en, ch in NOMBRES:
        assert q in qui_ok, q
        _choix(ch, en, carre=True)
        assert not _PR.majorite_trahit(ch), ("la majorité désigne la bonne", en)
    for l, q, ctx, en, prix, mal, pb, mot, inclus in TOTAL:
        ch, calcul = total(prix, mal, pb, mot, inclus)
        assert len({v for v, _ in ch}) == 4, (en, ch)
        assert mot in en, (en, mot)
        assert "pourboire" not in ctx or pb, ("le contexte ne souffle pas la règle", ctx)
    # Le plus grand montant ne doit pas être toujours le bon (tour 1 : 6 sur 6 sans écouter).
    rangs = [sorted([v for v, _ in total(*it[4:])[0]], reverse=True).index(total(*it[4:])[0][0][0]) for it in TOTAL]
    assert len(set(rangs)) > 1, ("la bonne est toujours au même rang de grandeur", rangs)
    # Tour 2 : la règle tenue n'ajoute pas toujours — la bonne n'est pas toujours la plus grande de sa paire.
    assert any(total(*it[4:])[0][0][0] < total(*it[4:])[0][2][0] for it in TOTAL), "la bonne est toujours la plus grande de sa paire"
    from collections import Counter as _C
    assert _C(it[3] for it in ALLERGIE if it[0] == "ada") == {0: 2, 1: 2, 2: 2, 3: 2}, "deux saumons par case"
    marches = [choix_allergie(it) for it in ALLERGIE if it[0] == "wei"]
    assert len(marches) == 2 and {m[0][0] for m in marches} == {_MARCHE[0], _MARCHE[3]}, "un marché pour chaque geste"
    for m in marches:
        assert sorted(c for c, _ in m) == sorted(_MARCHE), "les mêmes quatre choix au marché"
    longs = [len(ch[0][0]) < min(len(c) for c, _ in ch[1:]) for _, _, _, _, ch in REPONSES]
    assert sum(longs) <= len(REPONSES) // 4, ("la bonne est trop souvent la plus courte", sum(longs))
    for it in ALLERGIE:
        ch = choix_allergie(it)
        assert it[0] in gens, it[0]
        _choix(ch, it[2], carre=True)
    for q, en, blocs, tourner in CHEMIN:
        assert q in qui_ok and blocs in (2, 3) and tourner in ("gauche", "droite"), en
    from collections import Counter
    assert Counter((b, t) for _, _, b, t in CHEMIN) == Counter({(2, "gauche"): 2, (3, "droite"): 2, (2, "droite"): 1, (3, "gauche"): 1}), "chemins variés"
    for l, fr, en, cles in DIRE:
        assert l in lieux, l
        t = _PR.aplatir(en)
        rates = [c for c in cles if not _PR.cle_ok(c, t)]
        assert not rates, ("le modèle ne passe pas ses clés", en, rates)
    for k in GARDES:
        assert any(d[1].startswith(k) for d in DIRE), ("garde sans phrase", k)
    for l, fr, en, cles in DIRE:   # une garde (vraie sur la phrase vide) doit avoir son message
        assert all(not _PR.cle_ok(c, "") for c in cles) or garde(fr), ("garde sans message", fr)
    for c, t in REFUS:
        assert not _PR.cle_ok(c, _PR.aplatir(t)), ("accepte à tort", t)
    for c, t in ACCEPTE:
        assert _PR.cle_ok(c, _PR.aplatir(t)), ("refuse à tort", t)
    return True


def _choix(ch, en, carre):
    assert len(ch) == 4 and ch[0][1] is None and all(r for _, r in ch[1:]), en
    assert len({c for c, _ in ch}) == 4, ("deux choix identiques", en)
    bonne, autres = len(ch[0][0]), [len(c) for c, _ in ch[1:]]
    assert bonne <= max(autres), ("la bonne est seule la plus longue", en)
    # Un carré à deux moitiés (« A ; B ») : chaque moitié revient deux fois (tour 2 : une moitié unique
    # désignait la bonne comme l'exception).
    from collections import Counter
    if carre and all(c.count(" ; ") == 1 for c, _ in ch):
        for k in (0, 1):
            n = Counter(c.split(" ; ")[k] for c, _ in ch)
            assert set(n.values()) == {2}, ("moitié non appariée", en, dict(n))


if __name__ == "__main__":
    def charge(n):
        sp = importlib.util.spec_from_file_location(f"toronto_{n}", _ici / f"{n}.py")
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
    se, ps = charge("semaine"), charge("personnages")
    verifier({l[0] for l in se.LIEUX} | {"magasin"}, ps.VOIX, {g[0] for g in se.GENS})
    print(f"{len(REPONSES)} réponses, {len(NOMBRES)} nombres, {len(TOTAL)} totaux, {len(CHEMIN)} chemins, {len(DIRE)} à dire")
