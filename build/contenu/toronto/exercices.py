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
- TOTAL : ce que ça coûte vraiment ; les quatre totaux (rien, taxe, pourboire, les deux)
  se CALCULENT ici, jamais à la main.
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
      ("Achetez une carte au guichet, et un billet aussi.", "Tap your credit card, no need : rien à acheter.")]),
    ("hotel", "marcus", "Vous arrivez à l'hôtel à 13 h.",
     "Your room won't be ready until three, but we can keep your bags.",
     [("Chambre prête à 15 h ; on peut garder vos bagages.", None),
      ("Chambre prête à 15 h ; gardez vos bagages avec vous.", "We can keep your bags : on vous les garde."),
      ("Chambre prête tout de suite ; on garde vos bagages.", "Won't be ready until three : pas avant 15 h."),
      ("Chambre prête tout de suite ; gardez vos bagages.", "Not until three : pas avant 15 h ; et on vous garde vos bagages.")]),
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
      ("Elle demande : un sac, ou le reçu par courriel ?", "The receipt in the bag : c'est le reçu qui va dans le sac."),
      ("Elle demande votre courriel pour vous inscrire à une liste.", "Email it to you : vous envoyer le reçu, rien de plus."),
      ("Elle demande si vous voulez un sac pour le café.", "Elle parle du reçu : in the bag, or email.")]),
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
      ("30 % de rabais, la fin de semaine seulement.", "Twenty percent, on weekdays : 20 %, en semaine.")]),
    ("marche", "wei", "Vous commandez du fromage au poids.",
     "That's half a pound. It comes to six eighty.",
     [("Une demi-livre ; ça fait 6,80 $.", None),
      ("Une demi-livre ; ça fait 6,18 $.", "Eighty finit court : 80, pas 18."),
      ("Une livre et demie ; ça fait 6,80 $.", "Half a pound : une demi-livre."),
      ("Une livre et demie ; ça fait 6,18 $.", "Half a pound : une demi-livre ; et six eighty, 6,80 $.")]),
    ("marche", "wei", "Vous demandez si vous pouvez payer par carte.",
     "Cash only at this counter, but there's a machine by the door.",
     [("Comptant seulement ; un guichet près de la porte.", None),
      ("Comptant seulement ; un guichet au fond du marché.", "By the door : près de la porte."),
      ("La carte est acceptée ; un guichet près de la porte.", "Cash only : comptant seulement."),
      ("La carte est acceptée ; un guichet au fond du marché.", "Cash only : comptant ; et la machine est by the door.")]),
    ("kensington", "raj", "Vous cherchez le tramway de Spadina.",
     "Walk down to Spadina, it's two blocks east, and take it going south.",
     [("Deux coins de rue vers l'est ; le prendre en direction sud.", None),
      ("Deux coins de rue vers l'ouest ; le prendre en direction sud.", "East : l'est. L'ouest, ce serait west."),
      ("Deux coins de rue vers l'est ; le prendre en direction nord.", "Going south : en direction sud."),
      ("Deux coins de rue vers l'ouest ; en direction nord.", "Two blocks EAST, going SOUTH : à l'est, vers le sud.")]),
    ("kensington", "raj", "Vous demandez si c'est loin.",
     "Not at all, it's a five-minute walk. You can't miss it.",
     [("Pas loin : cinq minutes à pied, impossible à manquer.", None),
      ("Pas loin : quinze minutes à pied, impossible à manquer.", "Five : cinq. Quinze, ce serait fifteen."),
      ("Pas loin : cinq minutes en autobus, impossible à manquer.", "A five-minute WALK : à pied."),
      ("Assez loin : quinze minutes en autobus.", "Not at all, a five-minute walk : pas loin du tout, à pied.")]),
    ("iles", "kevin", "Vous voulez louer un vélo sur l'île.",
     "Bikes are fifteen dollars an hour, and we need a piece of ID.",
     [("15 $ l'heure ; il faut laisser une pièce d'identité.", None),
      ("50 $ l'heure ; il faut laisser une pièce d'identité.", "Fifteen finit sur un « n » : 15, pas 50."),
      ("15 $ l'heure ; il faut laisser une carte de crédit.", "A piece of ID : une pièce d'identité."),
      ("50 $ l'heure ; il faut laisser une carte de crédit.", "Fifteen dollars, a piece of ID : 15 $, une pièce d'identité.")]),
    ("iles", "kevin", "Vous demandez l'heure du dernier traversier.",
     "The last ferry back to the city is at eleven forty-five tonight.",
     [("Le dernier retour vers la ville : 23 h 45.", None),
      ("Le dernier retour vers la ville : 11 h 45 du matin.", "Tonight : ce soir, donc 23 h 45."),
      ("Le dernier départ vers l'île : 23 h 45.", "Back to the city : le retour vers la ville."),
      ("Le dernier départ vers l'île : 11 h 45 du matin.", "Back to the city, tonight : le retour, à 23 h 45.")]),
    ("pharmacie", "tom", "Vous montrez votre coup de soleil.",
     "Put this cream on twice a day, and stay out of the sun for a couple of days.",
     [("La crème deux fois par jour ; évitez le soleil quelques jours.", None),
      ("La crème trois fois par jour ; évitez le soleil quelques jours.", "Twice : deux fois."),
      ("La crème deux fois par jour ; de l'écran solaire avant de sortir.", "Stay out of the sun : évitez le soleil."),
      ("La crème trois fois par jour ; de l'écran solaire avant de sortir.", "Twice a day, stay out of the sun : deux fois, et pas de soleil.")]),
    ("pharmacie", "tom", "Vous demandez s'il faut une ordonnance.",
     "You don't need a prescription for this, but don't take it with alcohol.",
     [("Sans ordonnance ; pas d'alcool avec ce médicament.", None),
      ("Sans ordonnance ; pas à jeun avec ce médicament.", "With alcohol : avec de l'alcool."),
      ("Il faut une ordonnance ; pas d'alcool avec ça.", "You DON'T need a prescription : pas besoin d'ordonnance."),
      ("Il faut une ordonnance ; pas à jeun avec ce médicament.", "Pas d'ordonnance, et pas d'alcool.")]),
    ("resto", "ada", "Vous dites que vous êtes allergique aux noix.",
     "The pasta is fine, but the dessert has almonds, so I'd skip it.",
     [("Les pâtes, ça va ; le dessert contient des amandes.", None),
      ("Les pâtes, ça va ; le dessert est sans noix.", "The dessert HAS almonds : il en contient — évitez-le."),
      ("Les pâtes contiennent des noix ; le dessert a des amandes.", "The pasta is FINE : les pâtes, ça va."),
      ("Les pâtes contiennent des noix ; le dessert est sans noix.", "C'est l'inverse : les pâtes, ça va ; le dessert, non.")]),
    ("resto", "ada", "Vous demandez une table pour deux.",
     "It's about a twenty-minute wait, or you can sit at the bar right now.",
     [("Environ 20 minutes d'attente, ou le bar tout de suite.", None),
      ("Environ 30 minutes d'attente, ou le bar tout de suite.", "Twenty : 20. Trente, ce serait thirty."),
      ("Environ 20 minutes d'attente, ou la terrasse tout de suite.", "At the bar : au bar."),
      ("Environ 30 minutes, ou la terrasse tout de suite.", "Twenty minutes, or the bar : 20 minutes, ou le bar.")]),
    ("depart", "marcus", "Vous contestez un frais de minibar sur votre facture.",
     "You're right, the minibar charge is a mistake. I'll take it off.",
     [("Vous avez raison : c'est une erreur, il l'enlève.", None),
      ("Vous avez raison : c'est une erreur, remboursée plus tard.", "I'll take it off : il l'enlève maintenant."),
      ("Ce n'est pas une erreur, mais il l'enlève quand même.", "You're right, a mistake : c'est bien une erreur."),
      ("Ce n'est pas une erreur ; on vous remboursera plus tard.", "You're right, I'll take it off : erreur reconnue, enlevée.")]),
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
    ("andrew", "It's seventy-five forty.", [("75,40 $", None), ("75,14 $", "Forty finit court : 40 cents."), ("17,40 $", "Seventy finit court : 70."), ("17,14 $", "Seventy-five forty : 75,40 $.")]),
    ("ezinne", "The bill is eighty-two thirteen.", [("82,13 $", None), ("82,30 $", "Thirteen finit sur un « n » : 13 cents."), ("18,13 $", "Eighty finit court : 80."), ("18,30 $", "Eighty-two thirteen : 82,13 $.")]),
    ("aarti", "It's thirty-three seventeen, with tax.", [("33,17 $", None), ("33,70 $", "Seventeen finit sur un « n » : 17 cents."), ("13,17 $", "Thirty finit court : 30."), ("13,70 $", "Thirty-three seventeen : 33,17 $.")]),
    ("harper", "The tour starts at quarter to seven, p.m.", [("18 h 45", None), ("19 h 15", "Quarter TO : moins quart."), ("6 h 45", "P.m. : le soir."), ("7 h 15", "Quarter to seven, p.m. : 18 h 45.")]),
    ("liam", "The gates open at quarter past nine, a.m.", [("9 h 15", None), ("8 h 45", "Quarter PAST : et quart."), ("21 h 15", "A.m. : le matin."), ("20 h 45", "Quarter past nine, a.m. : 9 h 15.")]),
    ("andrew", "Check-out is at half past eleven.", [("11 h 30", None), ("10 h 30", "Half past ELEVEN : onze heures et demie."), ("11 h 15", "Half past : et demie, pas et quart."), ("10 h 15", "Half past eleven : 11 h 30.")]),
    ("sam", "We close at twenty to ten tonight.", [("21 h 40", None), ("22 h 20", "Twenty TO ten : dix heures moins vingt."), ("9 h 40", "Tonight : ce soir."), ("10 h 20", "Twenty to ten, tonight : 21 h 40.")]),
    ("rosa", "Happy hour is from four to six.", [("De 16 h à 18 h", None), ("De 14 h à 16 h", "From FOUR : de quatre heures."), ("De 16 h à 19 h", "To SIX : jusqu'à six heures."), ("De 14 h à 19 h", "From four to six : de 16 h à 18 h.")]),
    ("arjun", "Platform eighteen, in about forty minutes.", [("Quai 18, dans environ 40 minutes", None), ("Quai 80, dans environ 40 minutes", "Eighteen finit sur un « n » : 18."), ("Quai 18, dans environ 14 minutes", "Forty finit court : 40."), ("Quai 80, dans environ 14 minutes", "Eighteen, forty : quai 18, 40 minutes.")]),
]

# ── Le total à payer : (lieu, qui, contexte, en, prix, taxe?, pourboire %). Les quatre
# totaux (rien, taxe seule, pourboire seul, les deux) sont calculés par total().
TOTAL = [
    ("magasin", "rosa", "Au magasin, une tuque. Pas de pourboire au magasin.", "That's twenty-four, plus tax.", 24.00, True, 0),
    ("resto", "ada", "Au restaurant. Vous laissez 18 % de pourboire, calculé avant la taxe.", "Your bill is forty, before tax.", 40.00, True, 18),
    ("resto", "ada", "Au restaurant. Vous laissez 20 % de pourboire, calculé avant la taxe.", "That's sixty, before tax.", 60.00, True, 20),
    ("tour", "priya", "Au guichet de la tour : deux billets. Pas de pourboire.", "Two tickets, that's ninety-four, plus tax.", 94.00, True, 0),
    ("cafe", "rosa", "Au café, vous laissez 15 % au terminal, calculé avant la taxe.", "That's twelve, plus tax.", 12.00, True, 15),
    ("marche", "wei", "Au marché, un sandwich. Pas de pourboire au comptoir.", "Ten even, plus tax.", 10.00, True, 0),
]
TAXE = 0.13


def total(prix, taxe, pourboire):
    """Les quatre totaux d'un item, et l'indice du bon (rien, taxe, pourboire, les deux)."""
    t = round(prix * TAXE, 2); p = round(prix * pourboire / 100, 2) if pourboire else round(prix * 0.18, 2)
    valeurs = [prix, prix + t, prix + p, prix + t + p]
    bon = 3 if pourboire else 1
    return [round(v, 2) for v in valeurs], bon


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
    ("union", "Demandez où est le métro.", "Where is the subway?", ["~(where|is there|how (do|can) (i|we) get to|looking for|which way)", "subway|ttc|metro|station|train"]),
    ("union", "Demandez si vous pouvez payer avec votre carte de crédit.", "Can I pay with my credit card?", ["~(card|credit|visa|tap)", "~(can i|do you|is it|could i|okay|ok)"]),
    ("hotel", "Dites que vous avez une réservation au nom de Tremblay.", "I have a reservation under Tremblay.", ["reservation|booking|booked", "tremblay"]),
    ("hotel", "Demandez à quelle heure est le déjeuner.", "What time is breakfast?", ["what time|when", "breakfast"]),
    ("cafe", "Commandez un grand café pour emporter.", "Can I get a large coffee to go?", [DEMANDE, "large", "coffee"]),
    ("cafe", "On vous demande « Anything else? ». Répondez que c'est tout.", "That's it, thanks!", ["~(that s it|that s all|that is it|that is all|nothing else|no thanks|no thank you|i m good|im good)"]),
    ("tour", "Demandez deux billets pour adultes.", "Two adult tickets, please.", ["two|2", "ticket|tickets|adult|adults"]),
    ("tour", "Demandez s'il y a un rabais pour les aînés.", "Is there a discount for seniors?", ["discount|reduced|cheaper|deal", "senior|seniors|older"]),
    ("marche", "Commandez un sandwich au bacon de dos.", "Can I get a peameal bacon sandwich?", [DEMANDE, "sandwich"]),
    ("marche", "Demandez combien ça coûte.", "How much is it?", ["how much|what s the price|what is the price|price"]),
    ("kensington", "Dites que vous êtes perdu et demandez de l'aide.", "Excuse me, I'm lost. Can you help me?", ["lost", "~(help|can you|could you)"]),
    ("kensington", "Demandez si c'est loin à pied.", "Is it far to walk?", ["far|long|walk|walking"]),
    ("iles", "Demandez à louer un vélo pour deux heures.", "Can I rent a bike for two hours?", ["rent|get|borrow|have", "bike|bicycle", "two|2"]),
    ("iles", "Demandez à quelle heure est le dernier traversier.", "What time is the last ferry?", ["what time|when", "last", "ferry|boat"]),
    ("pharmacie", "Dites que vous avez un coup de soleil.", "I have a sunburn.", [MAL, "~(^| )(sunburn|sunburns|sunburned|sunburnt|burn|burned|burnt)( |$)"]),
    ("pharmacie", "Demandez combien de fois par jour.", "How many times a day?", ["~(how many times|how often)"]),
    ("resto", "Dites que vous êtes allergique aux noix.", "I'm allergic to nuts.", ["allergic|allergy", "nuts|nut|peanuts|peanut"]),
    ("resto", "Demandez des additions séparées.", "Can we get separate bills?", ["separate|split", "bill|bills|check|checks"]),
    ("depart", "Dites poliment qu'il y a une erreur sur la facture.", "Sorry, I think there's a mistake on my bill.", ["mistake|error|wrong", "bill|invoice|charge"]),
    ("depart", "Demandez où prendre le train pour l'aéroport.", "Where can I take the train to the airport?", ["~(where|how (do|can) (i|we) get|which way)", "airport|up express|train"]),
]

# Les réponses témoins des clés neuves (leçon de l'étape 1 : une clé se prouve dans les deux sens).
REFUS = [
    (DIRE[5][3][0], "Yes, I want more"),
    (DIRE[16][3][0], "I like nuts"),
]
ACCEPTE = [
    (DIRE[5][3][0], "No thanks, that's all"),
    (DIRE[5][3][0], "I'm good, thanks"),
    (DIRE[16][3][1], "I have a peanut allergy"),
    (DIRE[17][3][1], "Can we split the bill?"),
]


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
    for l, q, ctx, en, prix, taxe, pb in TOTAL:
        vals, bon = total(prix, taxe, pb)
        assert len(set(vals)) == 4, (en, vals)
    for q, en, blocs, tourner in CHEMIN:
        assert q in qui_ok and blocs in (2, 3) and tourner in ("gauche", "droite"), en
    from collections import Counter
    assert Counter((b, t) for _, _, b, t in CHEMIN) == Counter({(2, "gauche"): 2, (3, "droite"): 2, (2, "droite"): 1, (3, "gauche"): 1}), "chemins variés"
    for l, fr, en, cles in DIRE:
        assert l in lieux, l
        t = _PR.aplatir(en)
        rates = [c for c in cles if not _PR.cle_ok(c, t)]
        assert not rates, ("le modèle ne passe pas ses clés", en, rates)
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


if __name__ == "__main__":
    def charge(n):
        sp = importlib.util.spec_from_file_location(f"toronto_{n}", _ici / f"{n}.py")
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
    se, ps = charge("semaine"), charge("personnages")
    verifier({l[0] for l in se.LIEUX} | {"magasin"}, ps.VOIX, {g[0] for g in se.GENS})
    print(f"{len(REPONSES)} réponses, {len(NOMBRES)} nombres, {len(TOTAL)} totaux, {len(CHEMIN)} chemins, {len(DIRE)} à dire")
