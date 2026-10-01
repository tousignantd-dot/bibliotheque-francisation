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

ORIGINE = "~^(?!.*(^| )(coming|come) from the )(?=.*((^| )(i m|i am|im|we re|we are|i come|we come|i m coming|we re coming|coming) from [a-z]+|(^| )(i|we) live in (?!toronto)[a-z]+|(^| )from (quebec|montreal|canada|france)|(^| )i m (quebecois|quebecoise|french canadian)( |$)|^(from )?(quebec|montreal|gatineau|sherbrooke|laval|canada)( |$)))"
SEJOUR = "~^(?!.*(^| )(since|depuis) (a|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|couple|few|last|yesterday|this|monday|tuesday|wednesday|thursday|friday|saturday|sunday)( |$))(?!.*(^| )(day|days|week|weeks|night|nights|weekend) ago( |$))(?!.*(^| )(i|we) (ve|have) been (here|in [a-z]+) (for|since)( |$)).*?(?:(^| )(for|until|till|leave|leaving|stay|staying|here|just|only|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fourteen|couple)( (?!since|ago)[a-z]+){0,3} (week|weeks|weekend|day|days|night|nights|month|monday|tuesday|wednesday|thursday|friday|saturday|sunday)(?! ago)( |$)|(^| )a (week|weekend|few days)( |$))"
RELANCE = "~(^| )(and you|and yourself|how about you|how about yourself|what about you|what about yourself|how are you|are you from|are you (here|staying)|how long are you|do you (live|work|like)|have you (ever )?been|what do you do|where do you live|what s your name)( |$)|^you$|(^| )(and|so|well|thanks|good|fine|great|quebec|montreal|canada|here|week|weeks|weekend|days|nights|monday|tuesday|wednesday|thursday|friday|saturday|sunday|toronto) you$"
# Les clés partagées (audit tour 1, M7) : une demande, dite de toutes les façons naturelles.
DEMANDE = "~^((hi|hello|hey|excuse me|good morning|yes|um|uh|okay|ok|so) )*(just )?(a|one) [a-z ]{0,12}(tea|coffee)( |$)|give me|(^| )(can|could|may) (i|we)( please)? (get|have)|(can|could) you( please)? (give|get) (me|us)|(i|we) d like|(i|we)d like|(i|we) would like|(i|we) ll (have|take|get|go with)|(i|we) want|do you have|^(?!.*(you want|don t want|you get (a|one|the|some) )).*(^| )please( |$)"
# Tour 3 : le cadre d'une plainte, dit de toutes les façons (I'm sunburned, my husband has a fever…).
MAL = "~(^| )(i|we|he|she|my [a-z]+) (have|ve got|got|has|need|had|ve had)( a| an| some)? (?!no )[a-z]+|(^| )(i|we|he|she) (m|am|re|are|is|s|feel|feels|m feeling|am feeling|re feeling)( (really|very|so|a bit|a little|all|badly|pretty|quite|kind of))? (sunburned|sunburnt|burned|burnt|feverish|sick|hot)( |$)|(^| )(i m|i am|we re|he s|she s) running a|(^| )my [a-z]+ (is|are)( (really|very|so|all|badly|pretty|quite))? (burned|burnt|sunburned|red)( |$)|something for|(^| )(i|we) (burned|burnt) (myself|ourselves|my [a-z]+)( |$)"
REPETER = "~(sorry what|didn t (catch|hear)|say (that|it) again|what did you say|what was that|repeat|^(sorry|excuse me|pardon( me)?)$|come again|^again( please)?$|(^| )(it|that) again|one more time|speak up|louder|(don t|didn t|do not|did not) (understand|get it|get that))"

FIN = {
    "P1": "À la fin, vous direz ces formules au micro, sans les lire, et on vous comprendra du premier ou du deuxième coup — même quand un son raté changerait le mot (three, tree).",
    "P2": "À la fin, vous comprendrez un prix ou une heure entendus une seule fois, sans confondre 13 et 30, ni « quarter to » et « quarter past » — au moins 3 fois sur 4.",
    "P3": "À la fin, vous saurez demander ce qu'il vous faut, dans une situation que vous n'avez jamais vue — compris au micro du premier ou du deuxième coup, 3 fois sur 3.",
    "P4": "À la fin, vous vous présenterez en trois phrases — d'où vous venez, combien de temps vous restez, et la question qui relance — sans les lire.",
    "P5": "À la fin, vous saisirez les mots qui décident dans une réponse dite vite (oui ou non, il n'en reste plus, à gauche, ce n'est pas compris, ce qu'on vous propose) — au moins 3 fois sur 4, entendue une seule fois.",
}
# Le lieu de la semaine où chaque objectif servira d'abord (lien du bilan du test).
LIEU = {"P1": "union", "P2": "cafe", "P3": "hotel", "P4": "cafe", "P5": "kensington"}

SEANCES = [
  {"id": "p1", "titre": "Les sons de l'anglais qui trompent", "obj": "P1", "minutes": 15,
   "intro": "Vous connaissez déjà beaucoup de mots anglais. Ce qui vous trahit, ce sont cinq ou six sons que le français n'a pas, et la syllabe forte. Une fois ceux-là apprivoisés, on vous comprend du premier coup.",
   "meca": [
     "<b>th</b> : la langue entre les dents, jamais un s, un t, un z ni un d — <i>thanks</i>, <i>the</i>, <i>three</i>.",
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
   "ecoute": [("Sorry, I don't understand.", "Pardon, je ne comprends pas."), ("Hi! How are you?", "Bonjour ! Comment ça va ?"), ("Good, thanks! And you?", "Bien, merci ! Et vous ?"),
              ("Excuse me…", "Excusez-moi… (pour attirer l'attention)"), ("Sorry!", "Pardon ! Désolé !"),
              ("Thank you so much. — You're welcome.", "Merci beaucoup. — De rien."), ("No worries!", "C'est correct ! (pas de problème)"),
              ("Sorry, could you say that again?", "Pardon, pouvez-vous répéter ?"), ("More slowly, please.", "Plus lentement, s'il vous plaît."),
              ("Have a good one!", "Bonne journée ! (ou bonne soirée)")],
   "mots": ["hi", "thanks", "welcome", "sorry", "excuse_me", "again", "slowly", "dont_understand"],
   "quiz": [
     {"type": "rep", "qui": "liam", "en": "Hi there, how are you doing today?", "q": "Que répondez-vous ?",
      "choix": [("Good, thanks! And you?", None), ("I'm tired, I slept badly.", "C'est vrai, peut-être, mais la question est une salutation : on répond « Good, thanks! And you? »."), ("I'm doing the CN Tower today.", "Doing, ici, veut dire « comment ça va », pas « ce que vous faites ».")]},
     {"type": "dire", "fr": "Vous voulez attirer l'attention d'un employé du musée.",
      "choix": [("Excuse me…", None), ("Attention, please!", "C'est une annonce au haut-parleur ; pour un employé : « Excuse me… »."), ("Hello you!", "Trop brusque : « Excuse me… » est la porte polie.")]},
     {"type": "rep", "qui": "harper", "en": "No worries!", "choix": [("C'est correct ! (pas de problème)", None), ("Je suis inquiète.", "No worries, c'est le contraire : ce n'est rien, c'est correct."), ("Je n'ai pas compris.", "Elle a compris : no worries, c'est correct.")]},
     {"type": "dire", "fr": "On vous parle trop vite.",
      "choix": [("More slowly, please.", None), ("Speak French, please.", "C'est permis, mais rarement possible à Toronto. Demandez plutôt « More slowly, please »."), ("Faster, please.", "Faster, ce serait plus vite. Plus lentement : more slowly.")]},
     {"type": "rep", "qui": "andrew", "en": "Have a good one!", "choix": [("Bonne journée !", None), ("Prenez-en un bon !", "C'est une formule : have a good one, bonne journée (ou soirée)."), ("Vous en voulez un autre ?", "Il vous salue : have a good one, bonne journée.")]},
     {"type": "dire", "fr": "Vous n'avez pas compris la réponse. Demandez de répéter.",
      "choix": [("Sorry, could you say that again?", None), ("Sorry, can you say me that again?", "Say ne prend pas « me » : « say that again »."), ("Sorry, can you repeat me, please?", "Repeat ne prend pas « me » non plus : « could you say that again? ».")]},
   ],
   "dire": [("Répondez à « How are you? ».", "Good, thanks! And you?", ["good|fine|great|well|not bad", RELANCE]),
            ("Remerciez beaucoup.", "Thank you so much!", ["thank|thanks"]),
            ("Demandez de répéter, poliment.", "Sorry, could you say that again?", [REPETER]),
            ("Demandez de parler plus lentement.", "More slowly, please.", ["~slow"])]},

  {"id": "p3", "titre": "Les nombres et les prix", "obj": "P2", "minutes": 15,
   "intro": "Un café, un billet, un sandwich : tout a un prix, il se dit vite, et la taxe s'ajoute à la caisse. On apprend les nombres dont on a besoin, et surtout ceux qui se ressemblent à l'oreille.",
   "meca": [
     "<b>Les prix se disent en deux nombres</b> : 4,99 $ = <i>four ninety-nine</i> ; 12,50 $ = <i>twelve fifty</i>. Le mot « dollars » tombe souvent.",
     "<b>Les paires qui trompent</b> : <i>thirteen</i> (13) / <i>thirty</i> (30) · <i>fifteen</i> (15) / <i>fifty</i> (50). Écoutez la fin : -teen finit long, sur un « n » (thir-tiiin) ; -ty finit court, et au Canada le t s'adoucit presque en d après une voyelle ou un r (thir-di, for-di) ; fifty garde son t, mais finit court. Seul, 13 appuie sur la fin ; devant un autre nombre, l'accent peut remonter : fiez-vous au « n ».",
     "<b>La taxe</b> (13 % en Ontario) s'ajoute à la caisse : <i>plus tax</i>. Le prix affiché n'est presque jamais le prix payé.",
     "<b>Pour payer</b> : <i>Cash or card?</i> · <i>Debit or credit?</i> · <i>Tap or insert?</i> (touchez ou insérez la carte)."],
   "ecoute": [("thirteen, thirty", "13, 30 — le « n » de thirteen"), ("fifteen, fifty", "15, 50 — le « n » de fifteen"),
              ("four ninety-nine", "4,99 $"), ("twelve fifty", "12,50 $"),
              ("How much is it?", "C'est combien ?"), ("That's six twenty-five, plus tax.", "C'est 6,25 $, plus les taxes."),
              ("Cash or card?", "Comptant ou carte ?"), ("You can tap.", "Vous pouvez toucher le lecteur avec votre carte.")],
   "mots": ["how_much", "price_four99", "thirteen", "fifteen", "tax", "cash", "card", "terminal", "loonie", "toonie"],
   "quiz": [
     {"type": "rep", "qui": "liam", "en": "That's thirteen fifty.",
      "choix": [("13,50 $", None), ("30,50 $", "Ici, on entend le « n » de thirteen : 13."), ("30,15 $", "Thirty fifteen n'a pas été dit : thirteen fifty, 13,50 $.")]},
     {"type": "rep", "qui": "harper", "en": "It's fifty, plus tax.",
      "choix": [("50 $, plus les taxes", None), ("15 $, plus les taxes", "Fifteen finirait sur un « n ». Ici, fifty finit court : 50."), ("15 $, taxes comprises", "Ni 15 ni compris : fifty, plus tax.")]},
     {"type": "rep", "qui": "andrew", "en": "Four ninety-nine.",
      "choix": [("4,99 $", None), ("499 $", "Un prix se dit en deux nombres : four, puis ninety-nine — 4,99 $."), ("49,90 $", "Ce serait forty-nine ninety. Ici : four ninety-nine, 4,99 $.")]},
     {"type": "dire", "fr": "Le caissier dit « Tap or insert? ». Vous voulez toucher le lecteur avec votre carte.",
      "choix": [("Tap, please.", None), ("Cash, please.", "Cash, c'est comptant ; on vous demandait comment utiliser la carte."), ("Insert, please.", "Insert, c'est insérer la carte (la puce) dans le lecteur. Pour toucher : tap.")]},
     {"type": "rep", "qui": "liam", "en": "Your total is twenty-six thirteen.",
      "choix": [("26,13 $", None), ("26,30 $", "Ici, on entend le « n » de thirteen : 26,13 $."), ("36,30 $", "Ni trente-six ni trente : twenty-six thirteen, 26,13 $.")]},
     {"type": "mot", "en": "receipt", "choix": [("receipt", None), ("recipe", "Recipe (une recette) se dit en trois syllabes. Ici : re·CEIPT, le reçu, le p muet."), ("receive", "Receive (recevoir) finit par un v. Ici : receipt, le reçu.")]},
   ],
   "dire": [("Demandez combien c'est.", "How much is it?", ["how much"]),
            ("Demandez si vous pouvez payer par carte.", "Can I pay by card?", ["~(card|debit|credit|visa|tap)", "~(can i|do you|is it|could i|is (debit|credit|visa|card)|okay|ok)"]),
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
     {"type": "rep", "qui": "harper", "en": "Breakfast is from seven thirty to ten.",
      "choix": [("Le déjeuner est servi de 7 h 30 à 10 h.", None), ("Le déjeuner est servi de 7 h à 10 h 30.", "Le thirty va avec seven : de 7 h 30 à 10 h."), ("Le dîner est servi de 7 h 30 à 10 h.", "Breakfast, c'est notre déjeuner, le repas du matin."), ("Le dîner est servi de 7 h à 10 h 30.", "Breakfast, c'est le déjeuner ; et le thirty va avec seven.")]},
     {"type": "rep", "qui": "andrew", "en": "We're open until six.",
      "choix": [("C'est ouvert jusqu'à 18 h.", None), ("Ça ouvre à 18 h.", "Until, c'est « jusqu'à » : on ferme à six heures."), ("C'est ouvert dès 6 h.", "Until : jusqu'à. On ferme à 18 h.")]},
     {"type": "dire", "fr": "Demandez à quelle heure ferme le musée.",
      "choix": [("What time does the museum close?", None), ("What time does the museum closes?", "Après does, close reste sans s."), ("What time the museum closes?", "Il manque does : « What time does the museum close? ».")]},
   ],
   "dire": [("Demandez à quelle heure ça ouvre.", "What time does it open?", ["what time|when|hours", "open|opens|opening"]),
            ("Demandez l'heure.", "What time is it?", ["what time|the time"]),
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
   "mots": ["coffee", "the_bill", "room", "pharmacy", "help", "headache", "fever", "blister", "sunburn", "water", "towel"],
   "quiz": [
     {"type": "dire", "fr": "Au café, commandez un grand café.",
      "choix": [("Can I get a large coffee, please?", None), ("Can I get a coffee large, please?", "L'adjectif se place avant : a large coffee."), ("Can you get a large coffee, please?", "Can YOU : vous lui demanderiez d'aller en acheter un. Pour commander : Can I get…")]},
     {"type": "dire", "fr": "À la réception, demandez s'il reste une chambre pour ce soir.",
      "choix": [("Do you have a room for tonight?", None), ("I have a room for tonight.", "I have, c'est « j'ai » : vous affirmez avoir une chambre. Demandez : « Do you have…? »."), ("Do you have a room for this night?", "This night calque « cette nuit » ; pour ce soir, on dit « for tonight ».")]},
     {"type": "dire", "fr": "À la pharmacie, dites que vous avez mal à la tête.",
      "choix": [("I have a headache.", None), ("I am a headache.", "I am, c'est « je suis » : vous seriez un mal de tête ! On dit « I have a headache »."), ("My head is hurting me very.", "« Hurting me very » calque le français ; on dit « My head hurts » ou « I have a headache ».")]},
     {"type": "rep", "qui": "rosa", "en": "Do you need a bag?",
      "choix": [("Voulez-vous un sac ?", None), ("Avez-vous un sac ?", "Do you HAVE, ce serait « avez-vous ». Need : en avez-vous besoin ?"), ("Il vous faut payer le sac.", "Elle demande seulement : do you need a bag ?")]},
     {"type": "dire", "fr": "Au restaurant, demandez l'addition.",
      "choix": [("Could I have the bill, please?", None), ("Could I have the note?", "The note n'est pas l'addition au restaurant : « the bill »."), ("Could I have the addition, please?", "Addition, en anglais, c'est une somme ; l'addition du resto : « the bill ».")]},
     {"type": "dire", "fr": "Vous avez une ampoule au pied. Dites que votre pied vous fait mal.",
      "choix": [("My foot hurts.", None), ("My foot makes me hurt.", "C'est le calque de « mon pied me fait mal » : on dit « My foot hurts »."), ("I have hurt at the foot.", "C'est le calque de « j'ai mal au pied » : « My foot hurts ».")]},
   ],
   "dire": [("Commandez un café moyen.", "Can I get a medium coffee, please?", [DEMANDE, "coffee"]),
            ("Demandez s'ils ont une carte de la ville.", "Do you have a map?", ["~(do you have|have you got|can i (get|have)|could i (get|have)|is there)", "map"]),
            ("Dites que vous avez besoin d'une pharmacie.", "I need a pharmacy.", ["need", "pharmacy|drugstore"]),
            ("Dites que vous avez mal à la tête.", "I have a headache.", ["~(headache|head hurts|head is hurting)"])]},

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
      "choix": [("Where are the washrooms?", None), ("Where is the toilets?", "Toilets est au pluriel : where ARE ; et au Canada, on dit washrooms."), ("What are the washrooms?", "What, c'est « quoi ». Où : where.")]},
     {"type": "dire", "fr": "Demandez s'il y a une pharmacie près d'ici.",
      "choix": [("Is there a pharmacy near here?", None), ("Is it a pharmacy near here?", "Ce serait « est-ce une pharmacie ? ». Pour « y a-t-il » : Is there…?"), ("Is there a pharmacy near of here?", "Near, sans of : near here.")]},
     {"type": "dire", "fr": "Au tramway, demandez s'il va à Kensington.",
      "choix": [("Does this streetcar go to Kensington?", None), ("Does this streetcar goes to Kensington?", "Après does, le verbe reste go."), ("Is this streetcar go to Kensington?", "Is ne va pas avec go : « Does this streetcar go to Kensington? ».")]},
     {"type": "dire", "fr": "Demandez combien coûte un billet.",
      "choix": [("How much is a ticket?", None), ("How many is a ticket?", "How many compte des choses ; pour un prix : how much."), ("How is a ticket?", "Ce serait « comment va le billet ? » : how MUCH.")]},
     {"type": "dire", "fr": "Au café, vous voulez savoir si vous pouvez utiliser les toilettes.",
      "choix": [("Is there a washroom I could use?", None), ("Is it possible to use the washer?", "A washer est une laveuse ; les toilettes : a washroom."), ("Is there a washer I could use?", "A washer est une laveuse. Les toilettes, au Canada : a washroom.")]},
     {"type": "dire", "fr": "Demandez comment vous rendre à la tour CN.",
      "choix": [("How do I get to the CN Tower?", None), ("How do I get the CN Tower?", "Sans « to », ce serait « comment j'obtiens la tour » ! « How do I get TO the CN Tower? »."), ("Where do I go CN Tower?", "Il manque des mots : « How do I get to the CN Tower? ».")]},
   ],
   "dire": [("Demandez où est le métro.", "Where is the subway?", ["~(where|is there|how (do|can) (i|we) get to|looking for|which way)", "subway|ttc|metro|station"]),
            ("Demandez s'il y a une pharmacie près d'ici.", "Is there a pharmacy near here?", ["is there|where", "pharmacy|drugstore|drug store"]),
            ("Demandez combien coûte un billet.", "How much is a ticket?", ["how much", "ticket"]),
            ("Demandez si le déjeuner est inclus.", "Is breakfast included?", ["breakfast", "~(includ|come with|comes with)"])]},

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
      "choix": [("I'm from Quebec. How about you?", None), ("I'm Quebec. How about you?", "Ce serait « je suis le Québec » : I'm FROM Quebec."), ("Yes, I'm from. And you?", "Il manque le lieu : I'm from Quebec.")]},
     {"type": "rep", "qui": "harper", "en": "How long are you here for?",
      "choix": [("Combien de temps restez-vous ?", None), ("Depuis quand êtes-vous ici ?", "Depuis quand, ce serait « How long have you been here? ». Ici : combien de temps vous restez."), ("Êtes-vous ici pour longtemps, au travail ?", "Rien sur le travail : how long, combien de temps.")]},
     {"type": "dire", "fr": "On vous demande ce que vous faites dans la vie. Vous êtes à la retraite.",
      "choix": [("I'm retired.", None), ("I'm retreat.", "Retreat est une retraite fermée, spirituelle. À la retraite : retired."), ("I do retirement.", "On dit simplement « I'm retired ».")]},
     {"type": "rep", "qui": "harper", "en": "Is it your first time in Toronto?",
      "choix": [("C'est votre première fois à Toronto ?", None), ("C'est votre premier jour à Toronto ?", "First day, ce serait le premier jour. First time : la première fois."), ("Êtes-vous arrivé à temps à Toronto ?", "Time, ici, c'est « fois ».")]},
     {"type": "dire", "fr": "Vous venez de répondre d'où vous venez. Relancez la conversation.",
      "choix": [("And you? Where are you from?", None), ("And you? Where you are from?", "L'ordre de la question : where ARE you from?"), ("And you? From where you are?", "La question se construit : Where are you from?")]},
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
              ("Tax isn't included.", "La taxe n'est pas comprise."), ("Sorry, your card didn't go through.", "Désolé, votre carte n'est pas passée."), ("You're all set!", "C'est réglé !")],
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
     {"type": "rep", "qui": "andrew", "en": "The museum is closed on Monday, but it's open late on Thursday.",
      "choix": [("Fermé le lundi ; ouvert tard le jeudi.", None), ("Fermé le lundi ; ouvert tard le mardi.", "Thursday : jeudi. Mardi, ce serait Tuesday — écoutez le th."), ("Fermé le dimanche ; ouvert tard le jeudi.", "Monday : lundi. Dimanche, ce serait Sunday."), ("Fermé le dimanche ; ouvert tard le mardi.", "Monday, lundi ; et Thursday, jeudi : deux mots qui décident.")]},
     {"type": "rep", "qui": "rosa", "en": "Your room is ready, but the pool is closed today.",
      "choix": [("Chambre prête ; piscine fermée aujourd'hui.", None), ("Chambre pas prête ; piscine fermée aujourd'hui.", "Your room IS ready : elle est prête."), ("Chambre prête ; piscine ouverte aujourd'hui.", "But the pool is closed : la piscine est fermée."), ("Chambre pas prête ; piscine ouverte aujourd'hui.", "C'est l'inverse des deux : la chambre est prête, la piscine fermée.")]},
     {"type": "rep", "qui": "rosa", "en": "You're all set! Have a good one.",
      "choix": [("C'est réglé ! Bonne journée.", None), ("Asseyez-vous, s'il vous plaît.", "Set ne veut pas dire s'asseoir ici : you're all set, c'est réglé."), ("Il vous manque quelque chose.", "Au contraire : tout est réglé.")]},
   ],
   "dire": [("On vous dit que c'est complet. Demandez s'il y a un autre hôtel près d'ici.", "Is there another hotel near here?", ["another|other", "hotel"]),
            ("On vous indique la gauche. Dites « d'accord, merci beaucoup ».", "Okay, thank you so much!", ["thank|thanks"]),
            ("Vous n'avez pas compris la direction.", "Sorry, could you say that again?", [REPETER])]},
]

# Le test « Prêt à partir ? » : chaque objectif mesuré comme son critère le dit.
# P1 et P3 : DITS au micro, deux essais au plus. P2 et P5 : entendus UNE fois,
# au débit naturel. P4 : une seule tâche, se présenter et relancer. Deux formes
# parallèles, la première tirée au hasard ; situations NEUVES — en P1, les
# formules figées (Three., Sorry, could you say that again?) sont par nature
# celles des séances : c'est leur emploi dans une situation neuve qui se mesure.
# La place de la bonne réponse est tirée AU HASARD à chaque affichage (tour 4) :
# une graine fixe la mettait au même bouton (tour 3), une permutation posée dans
# les données se déduisait par élimination des places déjà montrées (tour 4). Un faux débutant qui le réussit (« Solide » partout) peut sauter
# les séances — décision du plan du 1er oct. 2026.
_P4_PARTIES = ["d'où vous venez", "combien de temps vous restez", "la question qui relance"]
# Révisé au tour 1 de la boucle (1er oct. 2026) : choix de même longueur, le leurre
# porté par DEUX mauvais choix (B1), phrases neuves (M6), un son raté qui change
# le mot (M1 : three/tree, leaving/living), le mot qui décide toujours enseigné (M4).
TEST = [
  [
    {"obj": "P1", "type": "oral", "fr": "Une passante vous tient la porte : remerciez-la.", "cles": ["thank|thanks"], "modele": "Thank you!"},
    {"obj": "P1", "type": "oral", "fr": "Le caissier demande combien de billets. Répondez d'un seul mot : trois.", "cles": ["three|3"], "modele": "Three."},
    {"obj": "P1", "type": "oral", "fr": "Dites que vous ne comprenez pas.", "cles": ["~(do not|dont|don t|did not|didnt|didn t|can t|cannot|can not) (understand|get it|get that|catch that)"], "modele": "Sorry, I don't understand."},
    {"obj": "P2", "type": "rep", "qui": "liam", "en": "That's thirty forty.",
     "choix": [("30,40 $", None), ("13,40 $", "Thirteen finirait sur un « n ». Ici, thirty finit court : 30."), ("13,14 $", "Ni treize ni quatorze : thirty forty, 30,40 $."), ("30,14 $", "Thirty, oui ; mais forty finit court : 40, pas 14.")]},
    {"obj": "P2", "type": "rep", "qui": "harper", "en": "The museum closes at quarter to six.",
     "choix": [("Le musée ferme à 17 h 45.", None), ("Le musée ferme à 18 h 15.", "Quarter past serait et quart. Quarter TO : moins quart, 17 h 45."), ("Le musée ouvre à 18 h 15.", "Closes : ferme ; et quarter to six, 17 h 45."), ("Le musée ouvre à 17 h 45.", "Closes : il ferme ; l'heure, elle, est juste.")]},
    {"obj": "P2", "type": "rep", "qui": "andrew", "en": "That'll be fifteen fifty, plus tax.",
     "choix": [("15,50 $, plus les taxes", None), ("50,15 $, plus les taxes", "Les deux nombres sont inversés : fifteen d'abord, puis fifty."), ("50,50 $, plus les taxes", "Fifteen finit sur un « n » : 15, puis fifty, 50."), ("15,15 $, plus les taxes", "Fifteen d'abord, oui ; puis fifty, qui finit court : 50.")]},
    {"obj": "P2", "type": "rep", "qui": "rosa", "en": "Check-out is at eleven a.m.",
     "choix": [("Départ à 11 h du matin.", None), ("Départ à 11 h du soir.", "A.m. : le matin. Le soir, ce serait p.m."), ("Arrivée à 11 h du soir.", "Check-out, c'est le départ ; et a.m., le matin."), ("Arrivée à 11 h du matin.", "A.m., oui ; mais check-out, c'est le départ.")]},
    {"obj": "P3", "type": "oral", "fr": "Au café, commandez un thé.", "cles": [DEMANDE, "tea"], "modele": "Can I get a tea, please?"},
    {"obj": "P3", "type": "oral", "fr": "Demandez où est l'arrêt d'autobus.", "cles": ["~(where|is there|how (do|can) (i|we) get to|looking for|which way)", "bus"], "modele": "Where is the bus stop?"},
    {"obj": "P3", "type": "oral", "fr": "Vous avez un coup de soleil : dites-le au pharmacien.", "cles": [MAL, "~(^| )(sunburn|sunburns|sunburned|sunburnt|burn|burned|burnt)( |$)"], "modele": "I have a sunburn."},
    {"obj": "P4", "type": "oral", "fr": "Une Torontoise vous demande qui vous êtes. Répondez : d'où vous venez, combien de temps vous restez, et relancez.",
     "cles": [ORIGINE, SEJOUR, RELANCE], "parties": _P4_PARTIES,
     "modele": "I'm from Quebec. I'm here for a week. How about you?"},
    {"obj": "P5", "type": "rep", "qui": "aarti", "en": "Sorry, the tower is closed today because of the wind.",
     "choix": [("La tour est fermée aujourd'hui à cause du vent.", None), ("La tour est fermée aujourd'hui à cause de la pluie.", "Closed, oui ; mais because of the WIND : le vent."), ("La tour est ouverte aujourd'hui, malgré le vent.", "Sorry, au début, annonçait un non : closed, fermée."), ("La tour est ouverte aujourd'hui, malgré la pluie.", "Closed : fermée ; et the wind : le vent.")]},
    {"obj": "P5", "type": "rep", "qui": "sam", "en": "Take the second right, then it's straight ahead.",
     "choix": [("Deuxième rue à droite, puis tout droit.", None), ("Deuxième rue à gauche, puis tout droit.", "Right : à droite."), ("Deuxième rue à gauche, puis c'est juste là.", "Right : à droite ; et straight ahead, tout droit."), ("Deuxième rue à droite, puis c'est juste là.", "À droite, oui ; mais straight ahead : tout droit.")]},
    {"obj": "P5", "type": "rep", "qui": "ezinne", "en": "We're out of the fish tonight, but the chicken is great.",
     "choix": [("Plus de poisson ce soir ; le poulet est très bon.", None), ("Plus de poulet ce soir ; le poisson est très bon.", "C'est l'inverse : out of the FISH."), ("Plus de poulet ce soir ; prenez plutôt le poisson.", "Out of the fish : c'est le poisson qui manque."), ("Plus de poisson ce soir ; le poulet aussi est fini.", "Le poisson manque, oui ; mais the chicken is great : le poulet est très bon.")]},
    {"obj": "P5", "type": "rep", "qui": "liam", "en": "Breakfast isn't included with this rate.",
     "choix": [("Le déjeuner n'est pas compris dans ce tarif.", None), ("Le déjeuner est bien compris dans le prix de la chambre.", "Isn't : n'est pas."), ("Le déjeuner est compris, mais pas le café.", "Isn't included : le déjeuner lui-même n'est pas compris."), ("Le déjeuner n'est pas compris, ni le café.", "Rien n'est dit du café : seulement le déjeuner, qui n'est pas compris.")]},
  ],
  [
    {"obj": "P1", "type": "oral", "fr": "Au comptoir, le serveur a parlé trop bas : faites-le répéter.", "cles": [REPETER], "modele": "Sorry, could you say that again?"},
    {"obj": "P1", "type": "oral", "fr": "Saluez en entrant au café, et demandez comment ça va.", "cles": ["hi|hello|hey|good morning|good afternoon|good evening|morning", "how are you|how s it going|how is it going|how you doing|how are things"], "modele": "Hi! How are you?"},
    {"obj": "P1", "type": "oral", "fr": "À l'hôtel, dites que vous partez demain — avec le verbe « leave ».", "cles": ["~(^| )(leave|leaving|leaves)( |$)"], "modele": "I'm leaving tomorrow."},
    {"obj": "P2", "type": "rep", "qui": "andrew", "en": "It's forty-three fifteen.",
     "choix": [("43,15 $", None), ("43,50 $", "Fifty finirait court ; ici, on entend le « n » de fifteen : 15."), ("33,50 $", "Ni trente-trois ni cinquante : forty-three fifteen, 43,15 $."), ("33,15 $", "Fifteen, oui ; mais forty-three : 43.")]},
    {"obj": "P2", "type": "rep", "qui": "liam", "en": "The next train is at quarter past eight.",
     "choix": [("Le prochain train est à 8 h 15.", None), ("Le prochain train est à 7 h 45.", "Quarter to serait moins quart. Quarter PAST : et quart, 8 h 15."), ("Le prochain train est à 8 h 45.", "Quarter past eight, c'est huit heures et quart : 8 h 15."), ("Le prochain train est à 7 h 15.", "Quarter PAST eight : huit heures et quart, 8 h 15.")]},
    {"obj": "P2", "type": "rep", "qui": "harper", "en": "Tickets are thirteen thirty.",
     "choix": [("13,30 $", None), ("30,13 $", "Les deux nombres sont inversés : thirteen d'abord, puis thirty."), ("30,30 $", "Thirteen finit sur un « n » : 13 d'abord."), ("13,13 $", "Thirteen d'abord, oui ; puis thirty, qui finit court : 30.")]},
    {"obj": "P2", "type": "rep", "qui": "rosa", "en": "Last entry is at eight p.m.",
     "choix": [("Dernière entrée à 8 h du soir.", None), ("Dernière entrée à 8 h du matin.", "P.m. : le soir. Le matin, ce serait a.m."), ("Première entrée à 8 h du matin.", "Last : la dernière ; et p.m., le soir."), ("Première entrée à 8 h du soir.", "Le soir, oui ; mais last, c'est la dernière.")]},
    {"obj": "P3", "type": "oral", "fr": "À la réception, demandez le mot de passe du wifi.", "cles": ["wifi|wi fi|wireless|internet", "password|code"], "modele": "Can I get the Wi-Fi password?"},
    {"obj": "P3", "type": "oral", "fr": "À l'hôtel, demandez où est l'ascenseur.", "cles": ["~(where|is there|do you have|how (do|can) (i|we) get to|looking for|which way)", "elevator|lift"], "modele": "Where is the elevator?"},
    {"obj": "P3", "type": "oral", "fr": "Vous avez de la fièvre : dites-le au pharmacien.", "cles": [MAL, "~(^| )(fever|feverish|temperature)( |$)"], "modele": "I have a fever."},
    {"obj": "P4", "type": "oral", "fr": "Au marché, un vendeur vous demande d'où vous êtes. Répondez : d'où vous venez, combien de temps vous restez, et relancez.",
     "cles": [ORIGINE, SEJOUR, RELANCE], "parties": _P4_PARTIES,
     "modele": "I'm from Montreal. I'm here for the weekend. And you? Are you from here?"},
    {"obj": "P5", "type": "rep", "qui": "liam", "en": "The washrooms are right there, on your left.",
     "choix": [("Les toilettes sont juste là, à votre gauche.", None), ("Les toilettes sont juste là, à votre droite.", "Right there veut dire juste là ; la direction, c'est on your LEFT."), ("Les toilettes sont plus loin, à votre droite.", "Right there : juste là ; et à gauche, on your left."), ("Les toilettes sont plus loin, à votre gauche.", "À gauche, oui ; mais right there : juste là.")]},
    {"obj": "P5", "type": "rep", "qui": "sam", "en": "Your card didn't go through. Do you want to try again?",
     "choix": [("Carte refusée ; voulez-vous réessayer ?", None), ("Carte refusée ; voulez-vous annuler ?", "Refusée, oui ; mais try again : on vous propose de réessayer, pas d'annuler."), ("Carte acceptée ; voulez-vous signer ?", "Didn't go through : elle n'est pas passée ; on vous propose de réessayer."), ("Carte acceptée ; voulez-vous votre reçu ?", "Didn't go through : refusée ; et try again, réessayer.")]},
    {"obj": "P5", "type": "rep", "qui": "arjun", "en": "The kitchen closes at ten, so this is your last chance to order.",
     "choix": [("La cuisine ferme à 22 h ; c'est le moment de commander.", None), ("La cuisine ouvre à 22 h ; vous pourrez commander plus tard.", "Closes : ferme."), ("La cuisine ouvre à 22 h ; c'est le moment de réserver.", "Closes : ferme ; et order, c'est commander."), ("La cuisine ferme à 22 h ; c'est le moment de réserver.", "Ferme, oui ; mais order, c'est commander.")]},
    {"obj": "P5", "type": "rep", "qui": "ezinne", "en": "The tip isn't included. It's up to you.",
     "choix": [("Pourboire non compris ; le montant est à votre choix.", None), ("Pourboire compris ; vous n'avez rien de plus à ajouter.", "Isn't included : n'est pas compris."), ("Pourboire compris ; ajoutez-en si vous voulez.", "Isn't included : il n'est pas compris ; c'est à vous de choisir."), ("Pourboire non compris ; le montant est fixé à 15 %.", "Non compris, oui ; mais it's up to you : c'est vous qui choisissez le montant.")]},
  ],
]
PAR_OBJECTIF = {"P1": 3, "P2": 4, "P3": 3, "P4": 1, "P5": 4}

# Audit tour 1 (M3) : « 80 % » sur 3 ou 4 questions voulait dire 100 %. Le seuil se dit en nombres, et
# la page l'applique à 75 % ; la présentation (P4) se compte par parties.
SEUIL = ("Solide : 3 sur 3 au micro, au moins 3 sur 4 à l'écoute, et les trois parties de la présentation ; En route : "
         "au moins la moitié ; À reprendre : moins de la moitié. Au micro, deux essais au plus ; les phrases entendues ne "
         "s'écoutent qu'une fois. Une question passée sans micro empêche « Solide ». « Solide » partout : vous pouvez sauter les séances.")
SEUIL_SOLIDE = 0.75
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
        if col.count(top) <= len(col) / 2:   # une égalité n'est pas une majorité (carré latin à 4 choix)
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
    for cle, t in REFUS:
        assert not cle_ok(cle, aplatir(t)), ("la clé accepte une réponse fausse", t)
    for cle, t in ACCEPTE:
        assert cle_ok(cle, aplatir(t)), ("la clé refuse une réponse juste", t)
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
                bonne, autres = len(it["choix"][0][0]), [len(c) for c, _ in it["choix"][1:]]
                assert bonne <= max(autres), ("au test, la bonne réponse est seule la plus longue", f, it["en"])
                # Tour 2 (bloquant) : à trois choix, le leurre sur deux choix laisse la bonne seule — l'exception
                # la trahit. Un item à deux traits prend le carré complet : chaque valeur deux fois.
                assert len(it["choix"]) == 4 or len(_nombres(it["choix"][0][0])) == 1, ("au test, quatre choix", f, it["en"])
    return True


def aplatir(t):
    """Comme la page aplatira la transcription : minuscules, sans ponctuation, chiffres en lettres."""
    import unicodedata
    t = "".join(c for c in unicodedata.normalize("NFD", t) if unicodedata.category(c) != "Mn")
    un = ("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
          "seventeen eighteen nineteen").split()
    diz = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    nb = lambda n: un[n] if n < 20 else (diz[n // 10] + (" " + un[n % 10] if n % 10 else "")) if n < 100 else str(n)
    # Comme la page (plat/enLettres) : « 10:30 », « $13.50 », puis tout nombre en lettres.
    t = re.sub(r"(\d{1,2}):(\d{2})", lambda m: nb(int(m.group(1))) + (" " + nb(int(m.group(2))) if int(m.group(2)) else ""), t)
    t = re.sub(r"\$\s*(\d+)\.(\d{2})", lambda m: nb(int(m.group(1))) + " " + nb(int(m.group(2))), t)
    t = re.sub(r"\d+", lambda m: " " + nb(int(m.group(0))) + " ", t.lower())
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", t.replace("'", " "))).strip()


def cle_ok(cle, t):
    if cle.startswith("~"):
        return re.search(cle[1:], t) is not None
    # Comme la page : une clé simple tolère le pluriel (s|es).
    return any(re.search(r"(^| )" + re.escape(aplatir(a)) + r"(s|es)?( |$)", t) for a in cle.split("|"))


# Ce que les clés de la présentation doivent REFUSER (tour 4 : elles créditaient le lieu où l'on est,
# et « depuis quand » pour « combien de temps »).
REFUS = [(ORIGINE, "I'm in Toronto for a week. And you?"), (ORIGINE, "I live in Toronto for a week. How about you?"),
         (SEJOUR, "I'm from Quebec. I arrived two days ago. And you?"), (SEJOUR, "I'm from Quebec. I'm here since Monday. And you?"),
         (SEJOUR, "Have a nice day"), (MAL, "I am a sunburn"), (MAL, "I'm fever"), (MAL, "I have no fever"),
         (MAL, "My name is sunburn"), (MAL, "I'm not sunburned"),
         (SEJOUR, "I'm from Quebec. I'm here since two days. And you?"), (SEJOUR, "I've been here for two days"),
         (DEMANDE, "Do you want a tea?"), (DEMANDE, "Can you get a medium coffee"),
         (DEMANDE, "Do you want a tea, please?"), (DEMANDE, "Can you get a tea, please?"), (DEMANDE, "I don't want tea, please"),
         (MAL, "I had no fever"), (MAL, "I didn't have a fever"), (SEJOUR, "I'm here since a week"), (SEJOUR, "I came two days ago"),
         (REPETER, "What?"),
         # Tour 2 des exercices : la relance acceptait les formules de clôture, « faire répéter » toute
         # phrase qui commençait par « sorry ».
         (RELANCE, "I'm from Quebec, thank you."), (RELANCE, "I'm from Quebec. Nice to meet you."), (RELANCE, "See you!"),
         (RELANCE, "We're here for a week, thank you."), (REPETER, "Sorry, I'm lost."), (REPETER, "Excuse me, where is the subway?"),
         # Tour 3 : la liste noire de la relance fuyait ; « coming from the hotel » passait pour l'origine.
         (RELANCE, "I'm from Quebec. Nice meeting you."), (RELANCE, "It was nice meeting you!"), (RELANCE, "Glad I met you."),
         (RELANCE, "I'll call you."), (ORIGINE, "I'm coming from the hotel. And you?"), (REPETER, "Thanks again!")]
ACCEPTE = [(ORIGINE, "We're from Sherbrooke"), (ORIGINE, "I live in Montreal"), (SEJOUR, "One week."), (SEJOUR, "Just the weekend"),
           (MAL, "I'm sunburned"), (MAL, "My husband has a fever"), (MAL, "I'm running a fever"), (MAL, "My skin is burned"),
           (DEMANDE, "A tea, please"), (DEMANDE, "Give me a tea"), (DEMANDE, "Do you have tea?"),
           (MAL, "I'm really sunburned"), (MAL, "I've had a fever since yesterday"), (MAL, "I'm feeling feverish"),
           (ORIGINE, "I'm Québécois"), (RELANCE, "What's your name?"), (REPETER, "Could you speak up?"),
           (REPETER, "What did you say?"), (REPETER, "What was that?"),
           (SEJOUR, "I'm from Quebec. Since I'm on vacation, I'm here for a week. And you?"), (SEJOUR, "I'm here for one week since it's my vacation"),
           (DEMANDE, "Can you get me a tea, please?"), (DEMANDE, "Tea, please"), (DEMANDE, "I take a tea, please"),
           (MAL, "I had a fever all night"),
           (RELANCE, "We leave Saturday. You?"), (RELANCE, "Quebec. And you?"), (ORIGINE, "Quebec. And you?"),
           (REPETER, "Sorry?"), (REPETER, "Pardon me?"), (REPETER, "Sorry, could you say that again?"),
           (RELANCE, "We're staying for a week. How long are you staying?"), (RELANCE, "Saguenay. And you?"),
           (REPETER, "Sorry, what?"), (REPETER, "Sorry, I didn't catch that."), (REPETER, "I didn't hear you")]


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
