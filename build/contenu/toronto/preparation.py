"""« Avant de partir » — les huit séances de préparation et le test « Prêt à partir ? ».

Étape 1 d'« Une semaine à Toronto » (1er oct. 2026). Le châssis est celui de
Compostelle (build/contenu/compostelle/preparation.py), réécrit pour l'anglais
et pour un FAUX DÉBUTANT (décision du plan) : le test se passe d'abord si l'on
veut, et qui le réussit peut sauter les séances. Rien n'est verrouillé.

Chaque séance a trois temps : J'ÉCOUTE (les phrases et les mots, avec leur
voix), JE RECONNAIS (on entend, on choisit), JE LE DIS (une situation en
français, on la dit au micro, puis le modèle).

Formats (les mêmes qu'à Compostelle) :
- `ecoute` : [(en, fr)] — dit par la narratrice (Clara, voix du Canada).
- `quiz`   : dicts. `type` = "rep" (on entend `en`, dit par `qui` ; on choisit
  le sens en français), "mot" (on entend `en` ; on choisit le mot écrit) ou
  "dire" (une situation `fr` ; on choisit ce qu'on dit, en anglais).
  `choix` = [(texte, rétroaction)] ; le PREMIER est le bon (rétroaction None),
  l'ordre affiché tourne. Chaque mauvais choix dit pourquoi il est faux.
- `dire`   : [(situation fr, modèle en, mots-clés attendus)] — `a|b` accepte
  l'un ou l'autre ; une clé qui commence par « ~ » est une expression
  régulière sur la transcription aplatie (minuscules, sans ponctuation,
  chiffres en lettres).
- `mots`   : identifiants du lexique réemployés (cartes dessinées).

Règle payée à l'hôtel (25 sept. 2026) : dans un choix de PRIX ou d'HEURE, le
vote majoritaire, position par position, ne doit pas désigner la bonne
réponse — sinon on réussit sans écouter. Les choix se bâtissent autour d'un
LEURRE (la vraie erreur d'oreille), et `verifier()` refuse l'item fautif.

    python3 build/contenu/toronto/preparation.py   # vérifie et compte
"""
import re

OBJECTIFS = {
    "P1": "Dire lisiblement les formules et les mots du voyage",
    "P2": "Comprendre un prix ou une heure",
    "P3": "Formuler une demande ou une question",
    "P4": "Se présenter et relancer",
    "P5": "Comprendre une réponse courte",
}

ORIGINE = "~(^| )(i m|i am|im) from( |$)|(^| )from (quebec|montreal|canada|france)"
SEJOUR = "~(^| )(week|weeks|weekend|day|days|night|nights|until|till)( |$)"  # la durée, dite n'importe comment
RELANCE = "~(^| )(and you|how about you|what about you)( |$)"

FIN = {
    "P1": "À la fin, vous direz ces formules au micro, sans les lire, et on vous comprendra du premier ou du deuxième coup — 8 fois sur 10.",
    "P2": "À la fin, vous comprendrez un prix ou une heure entendus une seule fois, sans confondre 13 et 30, ni « quarter to » et « quarter past » — 8 fois sur 10.",
    "P3": "À la fin, vous saurez demander ce qu'il vous faut, dans une situation que vous n'avez jamais vue.",
    "P4": "À la fin, vous vous présenterez en trois phrases — d'où vous venez, combien de temps vous restez, ce que vous faites — et vous relancerez la conversation.",
    "P5": "À la fin, vous saisirez le mot qui décide dans une réponse dite vite : oui, non, il n'en reste plus, à gauche, ce n'est pas compris.",
}
# Le lieu de la semaine où chaque objectif servira d'abord (lien du bilan du test).
LIEU = {"P1": "union", "P2": "cafe", "P3": "hotel", "P4": "cafe", "P5": "kensington"}

SEANCES = [
  {"id": "p1", "titre": "Les sons de l'anglais qui trompent", "obj": "P1", "minutes": 15,
   "intro": "Vous connaissez déjà beaucoup de mots anglais. Ce qui vous trahit, ce sont cinq ou six sons que le français n'a pas, et la syllabe forte. Une fois ceux-là apprivoisés, on vous comprend du premier coup.",
   "meca": [
     "<b>th</b> : la langue entre les dents, jamais un « z » ni un « d » — <i>thanks</i>, <i>the</i>.",
     "<b>h</b> se dit, comme un souffle : <i>hotel</i>, <i>help</i>. Sans lui, <i>hat</i> devient <i>at</i>.",
     "<b>i court, ee long</b> : <i>ship</i> (un bateau) n'est pas <i>sheep</i> (un mouton) ; <i>live</i> n'est pas <i>leave</i>.",
     "<b>La syllabe forte</b> : l'anglais en appuie une et avale les autres — <i>ho·TEL</i>, <i>DIN·ner</i>, <i>de·SSERT</i>.",
     "<b>Les lettres muettes</b> : le k de <i>knife</i>, le p de <i>receipt</i>, le s de <i>island</i>.",
     "<b>-ed</b> ne fait pas une syllabe de plus, sauf après t ou d : <i>closed</i> (une syllabe), <i>wanted</i> (deux)."],
   "ecoute": [("Thanks!", "Merci ! — la langue entre les dents"), ("the hotel", "l'hôtel — le h soufflé, ho·TEL"),
              ("a ship, a sheep", "un bateau, un mouton — i court, ee long"), ("to live, to leave", "habiter, partir"),
              ("dinner, dessert", "le souper, le dessert — DIN·ner, de·SSERT"), ("a knife", "un couteau — le k ne se dit pas"),
              ("the receipt", "le reçu — le p ne se dit pas"), ("the island", "l'île — le s ne se dit pas"),
              ("It's closed.", "C'est fermé — closed en une syllabe")],
   "mots": ["knife", "receipt", "island", "dessert", "closed", "dinner"],
   "quiz": [
     {"type": "mot", "en": "three", "choix": [("three", None), ("tree", "Tree (un arbre) commence par un t franc. Ici, la langue passait entre les dents : three, trois."), ("free", "Free commence par un f, les lèvres sur les dents. Ici : three, la langue entre les dents.")]},
     {"type": "mot", "en": "hat", "choix": [("hat", None), ("at", "At commence par une voyelle. Ici, on entendait un souffle avant : hat, le h se dit."), ("hut", "Hut a un son plus sourd, comme « eu ». Ici : hat, un chapeau.")]},
     {"type": "mot", "en": "leave", "choix": [("leave", None), ("live", "Live a un i court, bref. Ici, le son était long, tiré : leave, partir."), ("leaf", "Leaf finit par un f soufflé. Ici, la fin vibrait : leave.")]},
     {"type": "mot", "en": "ship", "choix": [("ship", None), ("sheep", "Sheep a un ee long. Ici, le i était court : ship, un bateau."), ("chip", "Chip commence par tch. Ici : ship, avec ch doux.")]},
     {"type": "mot", "en": "hotel", "q": "Où est la syllabe forte ?", "choix": [("ho·TEL", None), ("HO·tel", "En anglais, hotel appuie sur la fin : ho·TEL, comme en français."), ("les deux pareilles", "L'anglais n'égalise jamais : une syllabe est forte, l'autre s'efface. Ici : ho·TEL.")]},
     {"type": "mot", "en": "dinner", "q": "Où est la syllabe forte ?", "choix": [("DIN·ner", None), ("din·NER", "Dinner appuie sur le début : DIN·ner. La fin s'avale presque."), ("les deux pareilles", "Une syllabe est forte, l'autre s'efface : DIN·ner.")]},
     {"type": "mot", "en": "closed", "q": "Combien de syllabes ?", "choix": [("une", None), ("deux", "Après un s, -ed ne fait pas de syllabe : closed se dit en une seule."), ("trois", "Closed se dit d'un coup : une seule syllabe.")]},
   ],
   "dire": [("Dites « merci ».", "Thanks!", ["thanks|thank you|thank"]),
            ("Dites « l'hôtel ».", "The hotel.", ["hotel"]),
            ("Dites « trois ».", "Three.", ["three|3"]),
            ("Dites « un couteau ».", "A knife.", ["knife"])]},

  {"id": "p2", "titre": "Saluer, remercier, faire répéter", "obj": "P1", "minutes": 15,
   "intro": "Les formules qui ouvrent toutes les portes, et celles qui sauvent quand on ne comprend pas. Au Canada anglais, on les dit sans arrêt : bonjour, merci, désolé, bonne journée.",
   "meca": [
     "<b>Hi, how are you?</b> n'est pas une vraie question : on répond <i>Good, thanks! And you?</i>, même fatigué.",
     "<b>Excuse me</b> pour attirer l'attention ; <b>sorry</b> pour s'excuser — et les Canadiens le disent même quand c'est vous qui les bousculez.",
     "<b>You're welcome</b> répond à <i>thank you</i> ; on entend aussi <i>no problem</i>, <i>no worries</i>.",
     "Les phrases qui sauvent : <i>Sorry, could you say that again?</i> et <i>More slowly, please.</i>",
     "Pour partir : <i>Have a good one!</i> (bonne journée, bonne soirée — à toute heure)."],
   "ecoute": [("Hi! How are you?", "Bonjour ! Comment ça va ?"), ("Good, thanks! And you?", "Bien, merci ! Et vous ?"),
              ("Excuse me…", "Excusez-moi… (pour attirer l'attention)"), ("Sorry!", "Pardon ! Désolé !"),
              ("Thank you so much. — You're welcome.", "Merci beaucoup. — De rien."), ("No worries!", "Pas de souci !"),
              ("Sorry, could you say that again?", "Pardon, pouvez-vous répéter ?"), ("More slowly, please.", "Plus lentement, s'il vous plaît."),
              ("Have a good one!", "Bonne journée ! (ou bonne soirée)")],
   "mots": ["hi", "thanks", "welcome", "sorry", "excuse_me", "again", "slowly", "dont_understand"],
   "quiz": [
     {"type": "rep", "qui": "liam", "en": "Hi there, how are you doing today?", "q": "Que répondez-vous ?",
      "choix": [("Good, thanks! And you?", None), ("I'm tired, I slept badly.", "C'est vrai, peut-être, mais la question est une salutation : on répond « Good, thanks! And you? »."), ("I'm doing the CN Tower today.", "Doing, ici, veut dire « comment ça va », pas « ce que vous faites ».")]},
     {"type": "dire", "fr": "Vous voulez attirer l'attention d'un employé du musée.",
      "choix": [("Excuse me…", None), ("Sorry!", "Sorry s'excuse après coup. Pour attirer l'attention : « Excuse me… »."), ("Hello you!", "Trop brusque : « Excuse me… » est la porte polie.")]},
     {"type": "rep", "qui": "harper", "en": "No worries!", "choix": [("Pas de souci !", None), ("Ne vous inquiétez pas, c'est grave.", "No worries, c'est le contraire : ce n'est rien, pas de souci."), ("Je n'ai pas compris.", "Elle a compris : no worries, pas de souci.")]},
     {"type": "dire", "fr": "On vous parle trop vite.",
      "choix": [("More slowly, please.", None), ("Speak French, please.", "C'est permis, mais rarement possible à Toronto. Demandez plutôt « More slowly, please »."), ("Faster, please.", "Faster, ce serait plus vite. Plus lentement : more slowly.")]},
     {"type": "rep", "qui": "andrew", "en": "Have a good one!", "choix": [("Bonne journée !", None), ("Prenez-en un bon !", "C'est une formule : have a good one, bonne journée (ou soirée)."), ("Vous en voulez un autre ?", "Il vous salue : have a good one, bonne journée.")]},
     {"type": "dire", "fr": "Vous n'avez pas compris la réponse. Demandez de répéter.",
      "choix": [("Sorry, could you say that again?", None), ("Repeat!", "Un ordre sec : on ajoute « Sorry, could you say that again? »."), ("I don't speak.", "Ça ne veut rien dire : « Sorry, could you say that again? ».")]},
   ],
   "dire": [("Répondez à « How are you? ».", "Good, thanks! And you?", ["good|fine|great|well", "~(^| )(and you|how about you)( |$)"]),
            ("Remerciez beaucoup.", "Thank you so much!", ["thank|thanks"]),
            ("Demandez de répéter, poliment.", "Sorry, could you say that again?", ["~(say (that|it) again|repeat|pardon)"]),
            ("Demandez de parler plus lentement.", "More slowly, please.", ["slowly|slow"])]},

  {"id": "p3", "titre": "Les nombres et les prix", "obj": "P2", "minutes": 15,
   "intro": "Un café, un billet, un sandwich : tout a un prix, il se dit vite, et la taxe s'ajoute à la caisse. On apprend les nombres dont on a besoin, et surtout ceux qui se ressemblent à l'oreille.",
   "meca": [
     "<b>Les prix se disent en deux nombres</b> : 4,99 $ = <i>four ninety-nine</i> ; 12,50 $ = <i>twelve fifty</i>. Le mot « dollars » tombe souvent.",
     "<b>Les paires qui trompent</b> : <i>thirTEEN</i> (13) / <i>THIRty</i> (30) · <i>fifTEEN</i> (15) / <i>FIFty</i> (50). L'accent tombe à la fin pour 13 à 19, au début pour 30, 40, 50.",
     "<b>La taxe</b> (13 % en Ontario) s'ajoute à la caisse : <i>plus tax</i>. Le prix affiché n'est jamais le prix payé.",
     "<b>Pour payer</b> : <i>Cash or card?</i> · <i>Debit or credit?</i> · <i>Tap or insert?</i> (touchez ou insérez la carte)."],
   "ecoute": [("thirteen, thirty", "13, 30 — thirTEEN, THIRty"), ("fifteen, fifty", "15, 50 — fifTEEN, FIFty"),
              ("four ninety-nine", "4,99 $"), ("twelve fifty", "12,50 $"),
              ("How much is it?", "C'est combien ?"), ("That's six twenty-five, plus tax.", "C'est 6,25 $, plus les taxes."),
              ("Cash or card?", "Comptant ou carte ?"), ("You can tap.", "Vous pouvez toucher le lecteur avec votre carte.")],
   "mots": ["how_much", "price_four99", "thirteen", "fifteen", "tax", "cash", "card", "terminal", "loonie", "toonie"],
   "quiz": [
     {"type": "rep", "qui": "liam", "en": "That's thirteen fifty.",
      "choix": [("13,50 $", None), ("30,50 $", "Thirty, ce serait 30, accent au début. Ici : thirTEEN, accent à la fin — 13."), ("30,15 $", "Thirty fifteen n'a pas été dit : thirteen fifty, 13,50 $.")]},
     {"type": "rep", "qui": "harper", "en": "It's fifty, plus tax.",
      "choix": [("50 $, plus les taxes", None), ("15 $, plus les taxes", "Fifteen, ce serait 15, accent à la fin. Ici : FIFty, accent au début — 50."), ("15 $, taxes comprises", "Ni 15 ni compris : fifty, plus tax.")]},
     {"type": "rep", "qui": "andrew", "en": "Four ninety-nine.",
      "choix": [("4,99 $", None), ("499 $", "Un prix se dit en deux nombres : four, puis ninety-nine — 4,99 $."), ("49,90 $", "Ce serait forty-nine ninety. Ici : four ninety-nine, 4,99 $.")]},
     {"type": "dire", "fr": "Le caissier dit « Tap or insert? ». Vous voulez toucher le lecteur avec votre carte.",
      "choix": [("Tap, please.", None), ("Cash, please.", "Cash, c'est comptant ; on vous demandait comment utiliser la carte."), ("Insert, please.", "Insert, c'est glisser la carte dans le lecteur. Pour toucher : tap.")]},
     {"type": "rep", "qui": "liam", "en": "Your total is twenty-six thirteen.",
      "choix": [("26,13 $", None), ("26,30 $", "Thirty serait 30 cents. Ici : thirTEEN — 26,13 $."), ("36,30 $", "Ni trente-six ni trente : twenty-six thirteen, 26,13 $.")]},
     {"type": "mot", "en": "receipt", "choix": [("receipt", None), ("recipe", "Recipe (une recette) se dit en trois syllabes. Ici : re·CEIPT, le reçu, le p muet."), ("receive", "Receive (recevoir) finit par un v. Ici : receipt, le reçu.")]},
   ],
   "dire": [("Demandez combien c'est.", "How much is it?", ["how much"]),
            ("Demandez si vous pouvez payer par carte.", "Can I pay by card?", ["card"]),
            ("On vous annonce 13 $. Vérifiez en le répétant.", "Thirteen?", ["~(^| )(thirteen|13)( |$)"]),
            ("Commandez deux cafés.", "Two coffees, please.", ["two|2", "coffee|coffees"])]},

  {"id": "p4", "titre": "L'heure et les jours", "obj": "P2", "minutes": 15,
   "intro": "Le dernier traversier, l'entrée de la tour, la fermeture du musée : en voyage, beaucoup de choses se jouent à un quart d'heure près — et l'anglais compte les quarts autrement.",
   "meca": [
     "<b>Deux façons de dire l'heure</b> : <i>ten thirty</i> = <i>half past ten</i> (10 h 30).",
     "<b>Quarter past ten</b> = 10 h 15 ; <b>quarter to ten</b> = 9 h 45 (dix heures moins quart).",
     "<b>Pas de 21 h</b> : on dit <i>nine p.m.</i> (le soir) ou <i>nine a.m.</i> (le matin), ou <i>nine tonight</i>.",
     "<b>Until</b> = jusqu'à : <i>open until six</i>. <b>From… to…</b> : de… à…",
     "Les jours prennent la majuscule : <i>Monday, Tuesday…</i>"],
   "ecoute": [("What time is it?", "Quelle heure est-il ?"), ("It's ten thirty.", "Il est 10 h 30."),
              ("quarter past ten", "10 h 15"), ("quarter to ten", "9 h 45 — dix heures moins quart"),
              ("We close at nine p.m.", "Nous fermons à 21 h."), ("Open until six.", "Ouvert jusqu'à 18 h."),
              ("What time does it open?", "À quelle heure ça ouvre ?"), ("Monday, Tuesday, Wednesday, Thursday", "lundi, mardi, mercredi, jeudi"),
              ("Friday, Saturday, Sunday", "vendredi, samedi, dimanche")],
   "mots": ["oclock", "quarter_past", "half_past", "quarter_to", "am_pm", "open", "closed", "today", "tonight", "tomorrow"],
   "quiz": [
     {"type": "rep", "qui": "harper", "en": "The last ferry leaves at quarter to eleven.",
      "choix": [("Le dernier traversier part à 22 h 45.", None), ("Le dernier traversier part à 23 h 15.", "Quarter past, ce serait et quart. Quarter TO : moins quart — 22 h 45."), ("Le dernier traversier part à 23 h 45.", "Quarter to eleven, c'est onze heures moins quart : 22 h 45.")]},
     {"type": "rep", "qui": "liam", "en": "Your tour starts at quarter past two.",
      "choix": [("La visite commence à 14 h 15.", None), ("La visite commence à 13 h 45.", "Quarter to, ce serait moins quart. Quarter PAST : et quart — 14 h 15."), ("La visite commence à 14 h 45.", "Quarter past two, c'est deux heures et quart : 14 h 15.")]},
     {"type": "rep", "qui": "andrew", "en": "We're open until six.",
      "choix": [("C'est ouvert jusqu'à 18 h.", None), ("Ça ouvre à 18 h.", "Until, c'est « jusqu'à » : on ferme à six heures."), ("C'est ouvert dès 6 h.", "Until : jusqu'à. On ferme à 18 h.")]},
     {"type": "rep", "qui": "harper", "en": "Breakfast is from seven thirty to ten.",
      "choix": [("Le déjeuner est servi de 7 h 30 à 10 h.", None), ("Le déjeuner est servi de 7 h à 10 h 30.", "Le thirty va avec seven : de 7 h 30 à 10 h."), ("Le dîner est servi de 7 h à 10 h 30.", "Breakfast, c'est notre déjeuner, le repas du matin ; et le thirty va avec seven.")]},
     {"type": "dire", "fr": "Demandez à quelle heure ferme le musée.",
      "choix": [("What time does the museum close?", None), ("What time is the museum?", "Il manque le verbe : « What time does the museum close? »."), ("When the museum?", "Il manque le verbe : « What time does the museum close? ».")]},
   ],
   "dire": [("Demandez à quelle heure ça ouvre.", "What time does it open?", ["what time|when", "open|opens"]),
            ("Demandez l'heure.", "What time is it?", ["what time"]),
            ("Dites « à dix heures et demie ».", "At ten thirty.", ["ten|10", "thirty|30|half"]),
            ("Dites « demain matin ».", "Tomorrow morning.", ["tomorrow", "morning"])]},

  {"id": "p5", "titre": "Quatre formes qui font presque tout", "obj": "P3", "minutes": 15,
   "intro": "Pas besoin de grammaire pour se débrouiller : quatre débuts de phrase tout faits suffisent pour demander presque tout, au café, à l'hôtel, à la pharmacie.",
   "meca": [
     "<b>Can I get…?</b> ou <b>Could I have…?</b> + la chose : pour commander — <i>Can I get a coffee?</i> C'est poli au Canada.",
     "<b>Do you have…?</b> + la chose : vous avez… ? — <i>Do you have a map?</i>",
     "<b>I need…</b> : j'ai besoin de (l'urgence) — <i>I need a pharmacy.</i>",
     "<b>I have a…</b> + le mal : <i>I have a headache</i> (j'ai mal à la tête) ; ou <b>My … hurts</b> : <i>My foot hurts</i>.",
     "<b>Please</b> à la fin adoucit tout : <i>A large coffee, please.</i>"],
   "ecoute": [("Can I get a medium coffee?", "Je pourrais avoir un café moyen ?"), ("Could I have the bill, please?", "Pourrais-je avoir l'addition ?"),
              ("Do you have a map?", "Avez-vous une carte (de la ville) ?"), ("Do you have a room for tonight?", "Avez-vous une chambre pour ce soir ?"),
              ("I need a pharmacy.", "J'ai besoin d'une pharmacie."), ("I need help.", "J'ai besoin d'aide."),
              ("I have a headache.", "J'ai mal à la tête."), ("My foot hurts.", "J'ai mal au pied.")],
   "mots": ["coffee", "the_bill", "room", "pharmacy", "help", "headache", "blister", "sunburn", "water", "towel"],
   "quiz": [
     {"type": "dire", "fr": "Au café, commandez un grand café.",
      "choix": [("Can I get a large coffee, please?", None), ("I want coffee large.", "Compris, mais brusque et à l'envers : « Can I get a large coffee, please? »."), ("Do you need a large coffee?", "Need, c'est avoir besoin, et c'est vous qui le voudriez : « Can I get… »")]},
     {"type": "dire", "fr": "À la réception, demandez s'il reste une chambre pour ce soir.",
      "choix": [("Do you have a room for tonight?", None), ("I have a room for tonight.", "I have, c'est « j'ai » : vous affirmez avoir une chambre. Demandez : « Do you have…? »."), ("Can I get tonight?", "Il manque la chambre : « Do you have a room for tonight? ».")]},
     {"type": "dire", "fr": "À la pharmacie, dites que vous avez mal à la tête.",
      "choix": [("I have a headache.", None), ("I am a headache.", "I am, c'est « je suis » : vous seriez un mal de tête ! On dit « I have a headache »."), ("My head is hurting me very.", "Compris peut-être, mais « I have a headache » est la formule.")]},
     {"type": "rep", "qui": "rosa", "en": "Do you need a bag?",
      "choix": [("Voulez-vous un sac ?", None), ("Avez-vous un sac ?", "Do you HAVE, ce serait « avez-vous ». Need : en avez-vous besoin ?"), ("Il vous faut payer le sac.", "Elle demande seulement : do you need a bag ?")]},
     {"type": "dire", "fr": "Au restaurant, demandez l'addition.",
      "choix": [("Could I have the bill, please?", None), ("Could I have the note?", "The note n'est pas l'addition au restaurant : « the bill »."), ("I need the money.", "Ce serait « j'ai besoin d'argent » : demandez « the bill ».")]},
     {"type": "dire", "fr": "Vous avez une ampoule au pied. Dites que votre pied vous fait mal.",
      "choix": [("My foot hurts.", None), ("My foot is hurt you.", "La formule : « My foot hurts » (mon pied fait mal)."), ("I hurt your foot.", "Ce serait « je vous ai fait mal au pied » ! On dit « My foot hurts ».")]},
   ],
   "dire": [("Commandez un café moyen.", "Can I get a medium coffee, please?", ["~(can i get|could i have|can i have|i d like|id like|i would like)", "coffee"]),
            ("Demandez s'ils ont une carte de la ville.", "Do you have a map?", ["do you have", "map"]),
            ("Dites que vous avez besoin d'une pharmacie.", "I need a pharmacy.", ["need", "pharmacy|drugstore"]),
            ("Dites que vous avez mal à la tête.", "I have a headache.", ["headache"])]},

  {"id": "p6", "titre": "Poser une question", "obj": "P3", "minutes": 15,
   "intro": "Où, combien, à quelle heure, est-ce qu'il y a, comment je m'y rends : avec cinq débuts de question, on trouve presque tout dans une ville.",
   "meca": [
     "<b>Where is…?</b> où est… ? — <i>Where is the subway?</i>",
     "<b>How much is…?</b> combien coûte… ? · <b>What time…?</b> à quelle heure… ?",
     "<b>Is there a… near here?</b> y a-t-il un… près d'ici ? — <i>Is there a pharmacy near here?</i>",
     "<b>How do I get to…?</b> comment je me rends à… ? — <i>How do I get to the CN Tower?</i>",
     "<b>Does this… go to…?</b> est-ce que ce… va à… ? — <i>Does this streetcar go to Kensington?</i>"],
   "ecoute": [("Where is the subway?", "Où est le métro ?"), ("Where are the washrooms?", "Où sont les toilettes ?"),
              ("Is there a pharmacy near here?", "Y a-t-il une pharmacie près d'ici ?"), ("How much is a ticket?", "Combien coûte un billet ?"),
              ("What time is the last ferry?", "À quelle heure est le dernier traversier ?"), ("How do I get to the CN Tower?", "Comment je me rends à la tour CN ?"),
              ("Does this streetcar go to Kensington?", "Ce tramway va-t-il à Kensington ?"), ("Is breakfast included?", "Le déjeuner est-il inclus ?")],
   "mots": ["subway", "streetcar", "ticket", "pharmacy", "tower", "market", "ferry", "breakfast_incl", "exit", "bus_stop"],
   "quiz": [
     {"type": "dire", "fr": "Demandez où sont les toilettes.",
      "choix": [("Where are the washrooms?", None), ("Where is the toilet paper?", "Ce serait le papier de toilette ! « Where are the washrooms? » — au Canada, washroom."), ("What are the washrooms?", "What, c'est « quoi ». Où : where.")]},
     {"type": "dire", "fr": "Demandez s'il y a une pharmacie près d'ici.",
      "choix": [("Is there a pharmacy near here?", None), ("Is it a pharmacy here?", "Ce serait « est-ce que c'est une pharmacie, ici ? ». On dit « Is there… near here? »."), ("There is a pharmacy here.", "C'est une affirmation : pour demander, on retourne « Is there…? ».")]},
     {"type": "dire", "fr": "Au tramway, demandez s'il va à Kensington.",
      "choix": [("Does this streetcar go to Kensington?", None), ("Do you go Kensington?", "On vous comprendra peut-être, mais « Does this streetcar go to Kensington? » est sans risque."), ("Is Kensington this streetcar?", "La phrase est à l'envers : « Does this streetcar go to Kensington? ».")]},
     {"type": "dire", "fr": "Demandez combien coûte un billet.",
      "choix": [("How much is a ticket?", None), ("How many is a ticket?", "How many compte des choses ; pour un prix : how much."), ("How is a ticket?", "Ce serait « comment va le billet ? » : how MUCH.")]},
     {"type": "rep", "qui": "sam", "en": "Is there a washroom I could use?",
      "choix": [("Y a-t-il des toilettes que je pourrais utiliser ?", None), ("Y a-t-il une salle de bain à louer ?", "Rien n'est loué : could use, pourrais utiliser."), ("Y a-t-il une laveuse ?", "Washroom, au Canada : les toilettes. La laveuse : the washer.")]},
     {"type": "dire", "fr": "Demandez comment vous rendre à la tour CN.",
      "choix": [("How do I get to the CN Tower?", None), ("How do I get the CN Tower?", "Sans « to », ce serait « comment j'obtiens la tour » ! « How do I get TO the CN Tower? »."), ("Where do I go CN Tower?", "Il manque des mots : « How do I get to the CN Tower? ».")]},
   ],
   "dire": [("Demandez où est le métro.", "Where is the subway?", ["where", "subway"]),
            ("Demandez s'il y a une pharmacie près d'ici.", "Is there a pharmacy near here?", ["is there", "pharmacy|drugstore"]),
            ("Demandez combien coûte un billet.", "How much is a ticket?", ["how much", "ticket"]),
            ("Demandez si le déjeuner est inclus.", "Is breakfast included?", ["breakfast", "included|include"])]},

  {"id": "p7", "titre": "Parler de soi, et relancer", "obj": "P4", "minutes": 15,
   "intro": "À Toronto, on vous demandera d'où vous venez avant même de vous rendre la monnaie. Préparez vos trois phrases, et surtout la question qui relance : sans elle, la conversation s'arrête.",
   "meca": [
     "<b>I'm from…</b> pour l'origine : <i>I'm from Quebec</i>, <i>I'm from Montreal</i>.",
     "<b>I'm here for…</b> pour la durée : <i>for a week</i>, <i>for the weekend</i>, <i>for three days</i>.",
     "<b>I'm…</b> pour le métier : <i>I'm a nurse</i>, <i>I'm retired</i> (à la retraite). Attention : <i>a nurse</i>, avec « a ».",
     "<b>It's my first time in Toronto</b> : c'est ma première fois.",
     "<b>And you?</b> ou <b>How about you?</b> : la relance. Une réponse sans relance ferme la porte."],
   "ecoute": [("I'm from Quebec.", "Je viens du Québec."), ("I'm here for a week.", "Je suis ici pour une semaine."),
              ("It's my first time in Toronto.", "C'est ma première fois à Toronto."), ("I'm retired.", "Je suis à la retraite."),
              ("I'm a nurse.", "Je suis infirmière."), ("Where are you from?", "D'où venez-vous ?"),
              ("How about you?", "Et vous ?"), ("Nice to meet you!", "Enchanté !")],
   "mots": ["where_from", "from_quebec", "how_long", "first_time", "what_do_you_do", "and_you", "nice_to_meet"],
   "quiz": [
     {"type": "rep", "qui": "harper", "en": "So, where are you from?", "q": "Que répondez-vous ?",
      "choix": [("I'm from Quebec. How about you?", None), ("I'm Quebec.", "Ce serait « je suis le Québec » : I'm FROM Quebec."), ("Yes, I'm from.", "Il manque le lieu : I'm from Quebec — et la relance.")]},
     {"type": "rep", "qui": "harper", "en": "How long are you here for?",
      "choix": [("Combien de temps restez-vous ?", None), ("Depuis quand êtes-vous ici ?", "Depuis quand, ce serait « How long have you been here? ». Ici : combien de temps vous restez."), ("Êtes-vous ici pour longtemps, au travail ?", "Rien sur le travail : how long, combien de temps.")]},
     {"type": "dire", "fr": "On vous demande ce que vous faites dans la vie. Vous êtes à la retraite.",
      "choix": [("I'm retired.", None), ("I'm retreat.", "Retreat est une retraite fermée, spirituelle. À la retraite : retired."), ("I do retirement.", "On dit simplement « I'm retired ».")]},
     {"type": "rep", "qui": "harper", "en": "Is it your first time in Toronto?",
      "choix": [("C'est votre première fois à Toronto ?", None), ("C'est votre premier jour à Toronto ?", "First day, ce serait le premier jour. First time : la première fois."), ("Êtes-vous arrivé à temps à Toronto ?", "Time, ici, c'est « fois ».")]},
     {"type": "dire", "fr": "Vous venez de répondre d'où vous venez. Relancez la conversation.",
      "choix": [("And you? Are you from Toronto?", None), ("Okay.", "La conversation s'arrête là : relancez avec « And you? »."), ("Goodbye.", "Vous partez ! Relancez plutôt : « And you? ».")]},
   ],
   "dire": [("Dites d'où vous venez.", "I'm from Quebec.", [ORIGINE]),
            ("Dites combien de temps vous restez — par exemple, une semaine.", "I'm here for a week.", [SEJOUR]),
            ("Dites que c'est votre première fois à Toronto.", "It's my first time in Toronto.", ["first time"]),
            ("Présentez-vous en trois phrases : d'où vous venez, combien de temps vous restez, et relancez.",
             "I'm from Quebec. I'm here for a week. How about you?", [ORIGINE, SEJOUR, RELANCE])]},

  {"id": "p8", "titre": "Comprendre la réponse", "obj": "P5", "minutes": 15,
   "intro": "Le plus dur n'est pas de demander : c'est d'entendre la réponse, dite vite, parfois avec un accent. Le secret : guetter le mot qui décide, et laisser filer le reste.",
   "meca": [
     "<b>Sure</b>, <b>of course</b>, <b>absolutely</b> : oui. <b>Sorry, …</b> au début annonce souvent un non.",
     "<b>We're out of…</b> : il n'en reste plus · <b>We're full</b> : c'est complet.",
     "<b>On your left / on your right</b> : à votre gauche / droite · <b>right there</b> : juste là.",
     "<b>It's not included</b> : ce n'est pas compris · <b>It comes with…</b> : c'est servi avec…",
     "<b>You're all set!</b> : c'est réglé, vous pouvez y aller.",
     "Le reste de la phrase peut vous échapper : ce mot-là, non."],
   "ecoute": [("Sure, no problem.", "Oui, pas de problème."), ("Sorry, we're out of muffins.", "Désolé, il n'y a plus de muffins."),
              ("Sorry, we're full tonight.", "Désolé, c'est complet ce soir."), ("It's on your left.", "C'est à votre gauche."),
              ("It's right there.", "C'est juste là."), ("Two blocks down, then right.", "Deux coins de rue plus loin, puis à droite."),
              ("Tax isn't included.", "La taxe n'est pas comprise."), ("You're all set!", "C'est réglé !")],
   "mots": ["left", "right", "straight", "block", "corner", "north", "south", "anything_else", "tax", "line"],
   "quiz": [
     {"type": "rep", "qui": "aarti", "en": "Sorry, we're out of bagels, but we have muffins.",
      "choix": [("Plus de bagels, mais il y a des muffins.", None), ("Les bagels sont dehors, avec les muffins.", "Out of ne veut pas dire dehors : il n'en reste plus."), ("Plus de muffins, il reste des bagels.", "C'est l'inverse : out of bagels, il reste des muffins.")]},
     {"type": "rep", "qui": "liam", "en": "Go two blocks north, it's on your left.",
      "choix": [("Deux coins de rue vers le nord, à votre gauche.", None), ("Deux rues à gauche, puis vers le nord.", "On ne tourne pas : two blocks NORTH, puis c'est à gauche."), ("Deux coins de rue vers le nord, à votre droite.", "On your LEFT : à votre gauche.")]},
     {"type": "rep", "qui": "ezinne", "en": "Sorry, we're full tonight. Try the hotel across the street.",
      "choix": [("C'est complet ; essayez l'hôtel d'en face.", None), ("Il reste une chambre ce soir.", "Full : complet. Sorry, au début, annonçait un non."), ("C'est complet ; l'hôtel d'en face aussi.", "Rien n'est dit de l'autre hôtel, sinon d'essayer.")]},
     {"type": "rep", "qui": "andrew", "en": "Your room isn't ready yet. It'll be ready at three.",
      "choix": [("La chambre n'est pas prête ; elle le sera à 15 h.", None), ("La chambre est prête depuis 15 h.", "Isn't ready yet : pas encore prête."), ("Vous devez partir à 15 h.", "On parle de la chambre prête, pas du départ.")]},
     {"type": "rep", "qui": "arjun", "en": "The soup doesn't have any nuts.",
      "choix": [("La soupe ne contient pas de noix.", None), ("La soupe contient des noix.", "Doesn't have : ne contient pas."), ("Il n'y a plus de soupe.", "La soupe existe ; ce sont les noix qui n'y sont pas.")]},
     {"type": "rep", "qui": "rosa", "en": "You're all set! Have a good one.",
      "choix": [("C'est réglé ! Bonne journée.", None), ("Asseyez-vous, s'il vous plaît.", "Set ne veut pas dire s'asseoir ici : you're all set, c'est réglé."), ("Il vous manque quelque chose.", "Au contraire : tout est réglé.")]},
   ],
   "dire": [("On vous dit que c'est complet. Demandez s'il y a un autre hôtel près d'ici.", "Is there another hotel near here?", ["another|other", "hotel"]),
            ("On vous indique la gauche. Dites « d'accord, merci beaucoup ».", "Okay, thank you so much!", ["thank|thanks"]),
            ("Vous n'avez pas compris la direction.", "Sorry, could you say that again?", ["~(say (that|it) again|repeat|pardon|sorry)"])]},
]

# Le test « Prêt à partir ? » : chaque objectif mesuré comme son critère le dit.
# P1 et P3 : DITS au micro, deux essais au plus. P2 et P5 : entendus UNE fois,
# au débit naturel. P4 : une seule tâche, se présenter et relancer. Deux formes
# parallèles, la première tirée au hasard ; phrases NEUVES, jamais celles des
# séances. Un faux débutant qui le réussit (« Solide » partout) peut sauter
# les séances — décision du plan du 1er oct. 2026.
_P4_PARTIES = ["d'où vous venez (I'm from…)", "combien de temps vous restez (for a week…)", "la relance (And you?)"]
TEST = [
  [
    {"obj": "P1", "type": "oral", "fr": "Demandez poliment de parler plus lentement.", "cles": ["slowly|slow"], "modele": "More slowly, please."},
    {"obj": "P1", "type": "oral", "fr": "Remerciez beaucoup.", "cles": ["thank|thanks"], "modele": "Thank you so much!"},
    {"obj": "P1", "type": "oral", "fr": "Dites que vous ne comprenez pas.", "cles": ["~(do not|dont|don t) understand"], "modele": "Sorry, I don't understand."},
    {"obj": "P2", "type": "rep", "qui": "liam", "en": "That's thirty-five forty.",
     "choix": [("35,40 $", None), ("13,40 $", "Thirteen serait 13 ; ici, THIRty-five : 35."), ("13,14 $", "Ni treize ni quatorze : thirty-five forty, 35,40 $.")]},
    {"obj": "P2", "type": "rep", "qui": "harper", "en": "The museum closes at quarter to six.",
     "choix": [("Le musée ferme à 17 h 45.", None), ("Le musée ferme à 18 h 15.", "Quarter past serait et quart. Quarter TO : moins quart, 17 h 45."), ("Le musée ouvre à 18 h 15.", "Closes : ferme ; et quarter to six, 17 h 45.")]},
    {"obj": "P2", "type": "rep", "qui": "andrew", "en": "That'll be fifteen fifty, plus tax.",
     "choix": [("15,50 $, plus les taxes", None), ("50,15 $, plus les taxes", "Les deux nombres sont inversés : fifteen d'abord, puis fifty."), ("50,50 $, taxes comprises", "Ni cinquante dollars ni taxes comprises : fifteen fifty, plus tax.")]},
    {"obj": "P2", "type": "rep", "qui": "rosa", "en": "Check-out is at eleven a.m.",
     "choix": [("Il faut quitter la chambre à 11 h du matin.", None), ("Il faut quitter la chambre à 23 h.", "A.m. : le matin. Le soir, ce serait p.m."), ("On peut arriver à 11 h du matin.", "Check-out : le départ, quitter la chambre.")]},
    {"obj": "P3", "type": "oral", "fr": "Au café, commandez un thé.", "cles": ["~(can i get|could i have|can i have|i d like|id like|i would like|please)", "tea"], "modele": "Can I get a tea, please?"},
    {"obj": "P3", "type": "oral", "fr": "Demandez où est l'arrêt d'autobus.", "cles": ["where", "bus"], "modele": "Where is the bus stop?"},
    {"obj": "P3", "type": "oral", "fr": "Vous avez un coup de soleil : dites-le au pharmacien.", "cles": ["sunburn|sunburned|sunburnt|burn"], "modele": "I have a sunburn."},
    {"obj": "P4", "type": "oral", "fr": "Une Torontoise vous demande qui vous êtes. Répondez : d'où vous venez, combien de temps vous restez, et relancez.",
     "cles": [ORIGINE, SEJOUR, RELANCE], "parties": _P4_PARTIES,
     "modele": "I'm from Quebec. I'm here for a week. How about you?"},
    {"obj": "P5", "type": "rep", "qui": "aarti", "en": "Sorry, the tower is closed today because of the wind.",
     "choix": [("La tour est fermée aujourd'hui, à cause du vent.", None), ("La tour ferme tôt aujourd'hui.", "Rien n'est dit de l'heure : closed today, fermée aujourd'hui."), ("La tour est ouverte malgré le vent.", "Sorry, au début, annonçait un non : closed.")]},
    {"obj": "P5", "type": "rep", "qui": "sam", "en": "Take the second right, then it's straight ahead.",
     "choix": [("Prenez la deuxième à droite, puis c'est tout droit.", None), ("Prenez la deuxième à gauche, puis tout droit.", "Right : à droite."), ("C'est la deuxième maison à droite.", "Second right : la deuxième rue à droite.")]},
    {"obj": "P5", "type": "rep", "qui": "ezinne", "en": "We're out of the fish tonight, but the chicken is great.",
     "choix": [("Il n'y a plus de poisson ; le poulet est très bon.", None), ("Le poisson est servi dehors ce soir.", "Out of : il n'en reste plus."), ("Il n'y a plus de poulet ; prenez le poisson.", "C'est l'inverse : out of the FISH.")]},
    {"obj": "P5", "type": "rep", "qui": "liam", "en": "Breakfast isn't included with this rate.",
     "choix": [("Le déjeuner n'est pas compris dans ce tarif.", None), ("Le déjeuner est compris dans ce tarif.", "Isn't : n'est pas."), ("Le dîner n'est pas compris.", "Breakfast : le déjeuner, le repas du matin.")]},
  ],
  [
    {"obj": "P1", "type": "oral", "fr": "Demandez de répéter, poliment.", "cles": ["~(say (that|it) again|repeat|pardon)"], "modele": "Sorry, could you say that again?"},
    {"obj": "P1", "type": "oral", "fr": "Saluez en entrant au café, et demandez comment ça va.", "cles": ["hi|hello|hey|good morning", "how are you|how s it going|how is it going"], "modele": "Hi! How are you?"},
    {"obj": "P1", "type": "oral", "fr": "Excusez-vous : vous avez bousculé quelqu'un.", "cles": ["sorry|excuse me|pardon"], "modele": "Oh, sorry!"},
    {"obj": "P2", "type": "rep", "qui": "andrew", "en": "It's forty-three fifteen.",
     "choix": [("43,15 $", None), ("43,50 $", "Fifty serait 50 cents ; ici, fifTEEN, accent à la fin : 15."), ("33,50 $", "Ni trente-trois ni cinquante : forty-three fifteen, 43,15 $.")]},
    {"obj": "P2", "type": "rep", "qui": "liam", "en": "The next train is at quarter past eight.",
     "choix": [("Le prochain train est à 8 h 15.", None), ("Le prochain train est à 7 h 45.", "Quarter to serait moins quart. Quarter PAST : et quart, 8 h 15."), ("Le prochain train est à 8 h 45.", "Quarter past eight, c'est huit heures et quart : 8 h 15.")]},
    {"obj": "P2", "type": "rep", "qui": "harper", "en": "Tickets are thirteen dollars.",
     "choix": [("13 $", None), ("30 $", "Thirty serait 30, accent au début. Ici : thirTEEN — 13."), ("3 $", "Three serait 3. Ici : thirteen — 13.")]},
    {"obj": "P2", "type": "rep", "qui": "rosa", "en": "We close at nine p.m.",
     "choix": [("On ferme à 21 h.", None), ("On ferme à 9 h du matin.", "P.m. : l'après-midi ou le soir. Le matin, ce serait a.m."), ("On ouvre à 21 h.", "Close : fermer.")]},
    {"obj": "P3", "type": "oral", "fr": "À la réception, demandez le mot de passe du wifi.", "cles": ["wifi|wi fi|wireless|internet", "password|code"], "modele": "Can I get the Wi-Fi password?"},
    {"obj": "P3", "type": "oral", "fr": "Demandez si ce tramway va au marché St. Lawrence.", "cles": ["does|is|go|going", "market|st lawrence|saint lawrence"], "modele": "Does this streetcar go to St. Lawrence Market?"},
    {"obj": "P3", "type": "oral", "fr": "Vous avez de la fièvre : dites-le au pharmacien.", "cles": ["fever|temperature"], "modele": "I have a fever."},
    {"obj": "P4", "type": "oral", "fr": "Au marché, un vendeur vous demande d'où vous êtes. Répondez : d'où vous venez, combien de temps vous restez, et relancez.",
     "cles": [ORIGINE, SEJOUR, RELANCE], "parties": _P4_PARTIES,
     "modele": "I'm from Montreal. I'm here for the weekend. And you? Are you from here?"},
    {"obj": "P5", "type": "rep", "qui": "arjun", "en": "Sorry, the kitchen closes at ten, so last orders now.",
     "choix": [("La cuisine ferme à 22 h : dernières commandes maintenant.", None), ("La cuisine ouvre à 22 h.", "Closes : ferme."), ("La cuisine est fermée depuis 22 h.", "Last orders NOW : on peut encore commander.")]},
    {"obj": "P5", "type": "rep", "qui": "liam", "en": "The washrooms are downstairs, on your right.",
     "choix": [("Les toilettes sont en bas, à votre droite.", None), ("Les toilettes sont en haut, à droite.", "Downstairs : en bas."), ("Les toilettes sont en bas, à gauche.", "On your RIGHT : à droite.")]},
    {"obj": "P5", "type": "rep", "qui": "sam", "en": "Your card didn't go through. Do you want to try again?",
     "choix": [("Votre carte n'est pas passée ; voulez-vous réessayer ?", None), ("Votre carte est passée ; voulez-vous un reçu ?", "Didn't go through : n'est pas passée."), ("Votre carte est expirée ; il faut payer comptant.", "Rien n'est dit de l'expiration : on vous propose de réessayer.")]},
    {"obj": "P5", "type": "rep", "qui": "ezinne", "en": "The tip isn't included. It's up to you.",
     "choix": [("Le pourboire n'est pas compris ; c'est à vous de voir.", None), ("Le pourboire est compris.", "Isn't included : n'est pas compris."), ("Le pourboire doit être de 20 %.", "It's up to you : c'est à vous de décider.")]},
  ],
]
PAR_OBJECTIF = {"P1": 3, "P2": 4, "P3": 3, "P4": 1, "P5": 4}

SEUIL = ("Solide : 80 % ou plus ; En route : au moins la moitié ; À reprendre : moins de la moitié. Au micro, deux essais "
         "au plus ; les phrases entendues ne s'écoutent qu'une fois. « Solide » partout : vous pouvez sauter les séances.")
CONSEILS = {"P1": "Reprenez les séances 1 et 2, au micro.", "P2": "Reprenez les séances 3 et 4, voix plus lentes d'abord.",
            "P3": "Reprenez les séances 5 et 6.", "P4": "Reprenez la séance 7, et préparez vos trois phrases.",
            "P5": "Reprenez la séance 8 : guettez le mot qui décide."}


# ── La règle du leurre : dans un choix de prix ou d'heure, la majorité ne
# doit pas désigner la bonne réponse. On découpe chaque choix en nombres ;
# si chaque position a une valeur majoritaire et que leur assemblage est la
# bonne réponse, l'item se réussit sans écouter.
def _nombres(t):
    return re.findall(r"\d+", t)


def majorite_trahit(choix):
    vals = [_nombres(t) for t, _ in choix]
    if len(vals[0]) < 2 or any(len(v) != len(vals[0]) for v in vals):
        return False
    maj = []
    for i in range(len(vals[0])):
        col = [v[i] for v in vals]
        top = max(set(col), key=col.count)
        if col.count(top) < 2:
            return False
        maj.append(top)
    return maj == vals[0]


def verifier(lexique_ids=None, personnages=None):
    ids = set()
    for s in SEANCES:
        assert s["id"] not in ids, s["id"]; ids.add(s["id"])
        assert s["obj"] in OBJECTIFS, s["id"]
        assert len(s["ecoute"]) >= 6 and len(s["quiz"]) >= 5 and len(s["dire"]) >= 3, s["id"]
        if lexique_ids is not None:
            manque = [m for m in s["mots"] if m not in lexique_ids]
            assert not manque, (s["id"], manque)
        for q in s["quiz"]:
            _item(q, s["id"], personnages)
        for d in s["dire"]:
            fr, en, cles = d[:3]
            assert fr and en and cles, s["id"]
            _cles(cles, en, s["id"])
    for f, forme in enumerate(TEST):
        objs = [it["obj"] for it in forme]
        for o in OBJECTIFS:
            assert objs.count(o) == PAR_OBJECTIF[o], (f, o)
        for it in forme:
            if it["type"] == "oral":
                assert it["cles"] and it["modele"], it
                assert "parties" not in it or len(it["parties"]) == len(it["cles"]), it
                _cles(it["cles"], it["modele"], f"test{f}")
            else:
                _item(it, f"test{f}", personnages)
    return True


def aplatir(t):
    """Comme la page aplatira la transcription : minuscules, sans ponctuation, chiffres en lettres."""
    unites = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen".split()
    t = re.sub(r"\b(\d{1,2})\b", lambda m: unites[int(m.group(1))] if int(m.group(1)) < 16 else m.group(1), t.lower())
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.replace("'", " "))).strip()


def cle_ok(cle, t):
    if cle.startswith("~"):
        return re.search(cle[1:], t) is not None
    return any(re.search(r"(^| )" + re.escape(a) + r"( |$)", t) for a in cle.split("|"))


def _cles(cles, modele, ou):
    """Le modèle lui-même doit passer ses propres clés : sinon la bonne réponse est refusée."""
    t = aplatir(modele)
    rates = [c for c in cles if not cle_ok(c, t)]
    assert not rates, (ou, modele, rates)


def _item(q, ou, personnages):
    assert q["type"] in ("rep", "mot", "dire"), (ou, q)
    assert len(q["choix"]) >= 3, (ou, q)
    assert q["choix"][0][1] is None, (ou, q)
    assert all(r for _, r in q["choix"][1:]), ("rétroaction manquante", ou, q)
    assert len({c for c, _ in q["choix"]}) == len(q["choix"]), ("deux choix identiques", ou, q)
    if q["type"] == "rep":
        assert q["en"] and q.get("qui"), (ou, q)
        if personnages is not None:
            assert q["qui"] in personnages, (ou, q["qui"])
    assert not majorite_trahit(q["choix"]), ("la majorité désigne la bonne réponse", ou, q)


if __name__ == "__main__":
    import importlib.util, pathlib
    ici = pathlib.Path(__file__).parent
    def charge(n):
        sp = importlib.util.spec_from_file_location(f"toronto_{n}", ici / f"{n}.py")
        m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
    lx, ps = charge("lexique"), charge("personnages")
    verifier({e[0] for e in lx.LEXIQUE}, ps.VOIX)
    n_ec = sum(len(s["ecoute"]) for s in SEANCES)
    n_q = sum(len(s["quiz"]) for s in SEANCES)
    n_d = sum(len(s["dire"]) for s in SEANCES)
    print(f"{len(SEANCES)} séances : {n_ec} phrases à écouter, {n_q} questions, {n_d} à dire ; "
          f"test en 2 formes de {len(TEST[0])}")
