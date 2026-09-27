"""« Avant de partir » — les huit séances de préparation et le test « Prêt à partir ? ».

Décisions de Daniel du 26 sept. 2026 (compostelle-preparation-plan.html) :
huit séances de 15 minutes, conseillées et jamais verrouillées, gratuites ;
un encadré « la mécanique » par séance (la seule forme qui sert, jamais la
conjugaison entière) ; un test qui situe sans verrouiller.

Chaque séance a trois temps, dans l'ordre des haltes : J'ÉCOUTE (les phrases
et les mots, avec leur voix), JE RECONNAIS (on entend, on choisit), JE LE DIS
(une situation en français, on la dit au micro, puis le modèle).

Formats :
- `ecoute`  : [(es, fr)] — dit par la narratrice (Ximena).
- `quiz`    : dicts. `type` = "rep" (on entend `es`, dit par `qui` ; on choisit
  le sens en français), "mot" (on entend `es` ; on choisit le mot écrit) ou
  "dire" (une situation `fr` ; on choisit ce qu'on dit, en espagnol).
  `choix` = [(texte, rétroaction)] ; le PREMIER est le bon (rétroaction None),
  l'ordre affiché tourne. Chaque mauvais choix dit pourquoi il est faux.
- `dire`    : [(situation fr, modèle es, mots-clés attendus)] — `a|b` dans un
  mot-clé accepte l'un ou l'autre.
- `mots`    : identifiants du lexique réemployés (cartes dessinées).
`{o|a}` accorde au genre choisi ; `{alg:…}` à l'allergie (voir poche.py).

    python3 build/contenu/compostelle/preparation.py   # vérifie et compte
"""

OBJECTIFS = {
    "P1": "Dire lisiblement les formules et les mots du chemin",
    "P2": "Comprendre un prix ou une heure",
    "P3": "Formuler une demande ou une question",
    "P4": "Se présenter",
    "P5": "Comprendre une réponse courte",
}

FIN = {
    "P1": "À la fin, vous direz ces formules au micro, sans les lire, et on vous comprendra du premier ou du deuxième coup.",
    "P2": "À la fin, vous comprendrez un prix ou une heure entendus une seule fois, sans confondre les nombres qui se ressemblent.",
    "P3": "À la fin, vous saurez demander ce qu'il vous faut, dans une situation que vous n'avez jamais vue.",
    "P4": "À la fin, vous vous présenterez en trois phrases — d'où, pourquoi, votre allergie — sans aide.",
    "P5": "À la fin, vous saisirez le mot qui décide dans une réponse dite vite : oui, non, il en reste, à gauche, ça en contient.",
}
# La halte où chaque objectif servira d'abord (lien du bilan du test, F2).
HALTE = {"P1": "roncesvalles", "P2": "roncesvalles", "P3": "pamplona", "P4": "carrion", "P5": "puente-la-reina"}

SEANCES = [
  {"id": "p1", "titre": "Les sons de l'espagnol", "obj": "P1", "minutes": 15,
   "intro": "En espagnol, chaque lettre se dit, et toujours de la même façon. Une fois les cinq ou six sons qui changent du français apprivoisés, vous pouvez lire à voix haute n'importe quel mot du chemin.",
   "meca": [
     '<b>Les voyelles</b> sont toujours pleines : a, e, i, o, u — jamais muettes, jamais « eu ».',
     '<b>j</b> se racle au fond de la gorge : <i>jamón</i>.',
     '<b>ll</b> se dit comme un y : <i>calle</i> ; <b>ñ</b> se dit gn : <i>España</i>.',
     '<b>r</b> est battu une fois, <b>rr</b> roule : <i>pero</i> (mais), <i>perro</i> (chien).',
     'En Espagne, <b>z, ce, ci</b> se disent la langue entre les dents : <i>gracias</i>.',
     "<b>La syllabe forte</b> : mot fini par une voyelle, n ou s → l'avant-dernière (<i>ca·MI·no</i>) ; par une autre consonne → la dernière (<i>pa·GAR, hos·TAL</i>) ; un accent écrit l'emporte (<i>ca·FÉ, MÉ·di·co</i>)."],
   "ecoute": [("jamón", "le jambon — le j raclé"), ("la calle", "la rue — ll comme un y"),
              ("España", "l'Espagne — ñ comme gn"), ("pero, perro", "mais, chien — r battu, rr roulé"),
              ("gracias", "merci — la langue entre les dents"), ("el camino", "le chemin — ca·MI·no"),
              ("el café", "le café — ca·FÉ, l'accent écrit"), ("la mochila", "le sac à dos — ch comme tch")],
   "mots": ["jamon", "ducha", "queso", "zumo", "cerrado", "almohada", "mochila", "iglesia"],
   "quiz": [
     {"type": "mot", "es": "perro", "choix": [("perro", None), ("pero", "Pero, avec un r battu, veut dire « mais ». Ici, le r roulait : perro, le chien."), ("pera", "Pera (la poire) finit par a. Écoutez la fin : perro.")]},
     {"type": "mot", "es": "caja", "choix": [("caja", None), ("casa", "Casa se dit avec un s doux. Ici, on entendait le j raclé : caja, la caisse."), ("cara", "Cara a un r battu. Ici, le son du milieu se raclait : caja.")]},
     {"type": "mot", "es": "pollo", "choix": [("pollo", None), ("polo", "Polo n'a qu'un l. Ici, le ll sonnait comme un y : pollo, le poulet."), ("bollo", "Bollo commence par un b. Ici : pollo, le poulet.")]},
     {"type": "mot", "es": "mañana", "choix": [("mañana", None), ("manzana", "Manzana (la pomme) a un z au milieu. Ici, on entendait gn : mañana."), ("mamá", "Mamá n'a que deux syllabes. Ici, il y en avait trois : ma·ÑA·na.")]},
     {"type": "mot", "es": "médico", "q": "Où est la syllabe forte ?", "choix": [("ME·di·co", None), ("me·DI·co", "Sans accent écrit, un mot fini par une voyelle serait fort sur l'avant-dernière ; mais médico porte un accent sur le é : ME·di·co."), ("me·di·CO", "Un mot fini par une voyelle n'est pas fort sur la dernière, sauf accent écrit. Ici, l'accent est sur le é : ME·di·co.")]},
     {"type": "mot", "es": "repetir", "q": "Où est la syllabe forte ?", "choix": [("re·pe·TIR", None), ("re·PE·tir", "Repetir finit par un r, une consonne autre que n ou s : la dernière syllabe est forte, re·pe·TIR."), ("RE·pe·tir", "Sans accent écrit, jamais la première ici : repetir finit par r, donc re·pe·TIR.")]},
     {"type": "mot", "es": "cerveza", "choix": [("cerveza", None), ("servesa", "Servesa n'existe pas : c'est la prononciation d'Amérique latine. En Espagne, ce et z se disent la langue entre les dents : cerveza."), ("cereza", "Cereza (la cerise) n'a pas de v. Ici : cer·VE·za, la bière.")]},
   ],
   "dire": [("Dites « merci ».", "Gracias.", ["gracias"]),
            ("Dites « le jambon ».", "El jamón.", ["jamon"]),
            ("Dites « la rue ».", "La calle.", ["calle"]),
            ("Dites « l'Espagne ».", "España.", ["espana"])]},

  {"id": "p2", "titre": "Saluer, remercier, faire répéter", "obj": "P1", "minutes": 15,
   "intro": "Les formules qui ouvrent toutes les portes — et celles qui sauvent quand on ne comprend pas. Avec elles, on peut commencer n'importe quelle conversation, et s'en sortir.",
   "meca": [
     "<b>Bonjour change avec l'heure</b> : <i>buenos días</i> jusqu'au dîner (vers 14 h).",
     "<i>Buenas tardes</i> jusqu'au souper, tard en Espagne ; <i>buenas noches</i> le soir, et pour dire bonne nuit.",
     '<b>Perdone</b> (vous) pour un commerçant ou une personne âgée ; <b>perdona</b> (tu) entre pèlerins.',
     '<b>De nada</b> répond à <i>gracias</i>.',
     'La phrase qui sauve : <i>más despacio, por favor</i>.'],
   "ecoute": [("Buenos días.", "Bonjour (le matin)."), ("Buenas tardes.", "Bonjour (l'après-midi, jusqu'au souper)."),
              ("Buenas noches.", "Bonsoir, bonne nuit."), ("¡Buen Camino!", "Bon chemin ! — le salut des pèlerins."),
              ("Muchas gracias. — De nada.", "Merci beaucoup. — De rien."), ("Perdone, no entiendo.", "Pardon, je ne comprends pas."),
              ("¿Puede repetir, por favor?", "Pouvez-vous répéter, s'il vous plaît ?"), ("Más despacio, por favor.", "Plus lentement, s'il vous plaît.")],
   "mots": ["buenos_dias", "buenas_tardes", "buenas_noches", "buen_camino", "vale", "perdone", "no_entiendo", "despacio", "repetir", "de_nada"],
   "quiz": [
     {"type": "dire", "fr": "Il est 10 h. Vous entrez à la boulangerie.", "choix": [("Buenos días.", None), ("Buenas tardes.", "Buenas tardes, c'est l'après-midi. À 10 h : buenos días."), ("Buenas noches.", "Buenas noches, c'est le soir, ou bonne nuit.")]},
     {"type": "dire", "fr": "Il est 18 h. Vous arrivez à l'albergue.", "choix": [("Buenas tardes.", None), ("Buenos días.", "Buenos días s'arrête vers le dîner, vers 14 h. À 18 h : buenas tardes."), ("Buenas noches.", "En Espagne, 18 h, c'est encore l'après-midi : buenas noches attend le souper.")]},
     {"type": "dire", "fr": "Un vieil homme vous explique le chemin, beaucoup trop vite.", "choix": [("Más despacio, por favor.", None), ("Más rápido, por favor.", "Rápido, c'est vite : vous lui demandez d'accélérer !"), ("Hasta luego, gracias.", "Vous partez sans avoir compris. Demandez-lui plutôt de ralentir.")]},
     {"type": "rep", "qui": "ainhoa", "es": "De nada. ¡Buen Camino!", "choix": [("Il n'y a pas de quoi. Bon chemin !", None), ("Je n'ai rien du tout. Bon chemin !", "De nada ne veut pas dire « rien du tout » : c'est la réponse à gracias, « de rien »."), ("Pas de chemin pour vous aujourd'hui.", "Buen Camino est le salut des pèlerins : bon chemin !")]},
     {"type": "dire", "fr": "Dans la file, vous bousculez quelqu'un sans le vouloir.", "choix": [("Perdone, lo siento.", None), ("De nada, gracias.", "De nada répond à un merci. Pour s'excuser : perdone, lo siento."), ("Vale, muy bien.", "Vale, c'est « d'accord ». Ici, il faut s'excuser : perdone.")]},
     {"type": "dire", "fr": "On vient de vous parler, et vous n'avez rien compris.", "choix": [("Perdone, no entiendo.", None), ("No, gracias, muy amable.", "No, gracias refuse quelque chose. Vous voulez dire que vous n'avez pas compris : no entiendo."), ("Vale, gracias, perfecto.", "Vale veut dire « d'accord » : on croira que vous avez compris.")]},
   ],
   "dire": [("Remerciez beaucoup.", "Muchas gracias.", ["muchas", "gracias"]),
            ("Demandez de répéter, poliment.", "¿Puede repetir, por favor?", ["repetir"]),
            ("Demandez de parler plus lentement.", "Más despacio, por favor.", ["despacio"]),
            ("Saluez un pèlerin sur le chemin.", "¡Hola! ¡Buen Camino!", ["buen camino"])]},

  {"id": "p3", "titre": "Les nombres et les prix", "obj": "P2", "minutes": 15,
   "intro": "Un lit, un café, un pansement : tout a un prix, et il se dit vite. On apprend les nombres dont on a besoin, et surtout ceux qui se ressemblent à l'oreille.",
   "meca": [
     '<b>Les prix</b> : les euros, puis les centimes avec <b>con</b> — <i>cuatro con cincuenta</i> = 4,50 €.',
     "<b>Les paires qui trompent l'oreille</b> : <i>dos</i> (2) / <i>doce</i> (12) · <i>seis</i> (6) / <i>siete</i> (7).",
     'Et encore : <i>trece</i> (13) / <i>treinta</i> (30) · <i>quince</i> (15) / <i>cincuenta</i> (50).',
     "<b>Pour payer</b> : <i>¿Cuánto es?</i> (c'est combien ?), <i>con tarjeta</i> (par carte), <i>en efectivo</i> (comptant)."],
   "ecoute": [("uno, dos, tres, cuatro, cinco", "1, 2, 3, 4, 5"), ("seis, siete, ocho, nueve, diez", "6, 7, 8, 9, 10"),
              ("once, doce, trece, catorce, quince", "11, 12, 13, 14, 15"), ("veinte, treinta, cuarenta, cincuenta", "20, 30, 40, 50"),
              ("¿Cuánto es?", "C'est combien ?"), ("Son cuatro con cincuenta.", "C'est 4,50 €."),
              ("¿Puedo pagar con tarjeta?", "Puis-je payer par carte ?"), ("Solo en efectivo.", "Comptant seulement.")],
   "mots": ["cuanto", "efectivo", "tarjeta", "cajero", "kilo", "cuenta", "propina"],
   "quiz": [
     {"type": "rep", "qui": "ainhoa", "es": "Son dos euros.", "choix": [("2 €", None), ("12 €", "Doce, ce serait 12. Ici : dos, deux."), ("20 €", "Veinte, ce serait 20. Ici : dos, deux.")]},
     {"type": "rep", "qui": "javier", "es": "Son doce euros la cama.", "choix": [("12 € le lit", None), ("2 € le lit", "Dos, ce serait 2. Doce, c'est 12."), ("20 € le lit", "Veinte, ce serait 20. Doce, c'est 12.")]},
     {"type": "rep", "qui": "manolo", "es": "Son seis con veinte.", "choix": [("6,20 €", None), ("7,20 €", "Siete, ce serait 7. Seis, c'est 6."), ("16,20 €", "Dieciséis, ce serait 16. Ici, seulement seis.")]},
     {"type": "rep", "qui": "alex", "es": "El menú son trece euros.", "choix": [("13 €", None), ("30 €", "Treinta, ce serait 30. Trece, c'est 13."), ("3 €", "Tres, ce serait 3. Trece, c'est 13.")]},
     {"type": "rep", "qui": "pilar", "es": "Son quince con cincuenta.", "choix": [("15,50 €", None), ("50,15 €", "L'ordre ne change pas : les euros d'abord, puis con et les centimes."), ("5,50 €", "Cinco, ce serait 5. Quince, c'est 15.")]},
     {"type": "rep", "qui": "ainhoa", "es": "Lo siento, solo en efectivo.", "choix": [("Désolée, comptant seulement.", None), ("Désolée, par carte seulement.", "Con tarjeta, ce serait par carte. En efectivo, c'est comptant."), ("Désolée, c'est gratuit.", "Gratis, ce serait gratuit. Efectivo, c'est de l'argent comptant.")]},
   ],
   "dire": [("Demandez combien c'est.", "¿Cuánto es?", ["cuanto"]),
            ("Demandez si vous pouvez payer par carte.", "¿Puedo pagar con tarjeta?", ["tarjeta"]),
            ("Commandez deux cafés.", "Dos cafés, por favor.", ["dos", "cafes|cafe"]),
            ("On vous annonce 12 € ; vérifiez en le répétant.", "¿Doce euros?", ["doce"])]},

  {"id": "p4", "titre": "L'heure et les jours", "obj": "P2", "minutes": 15,
   "intro": "Le souper, la porte de l'albergue, la messe, le magasin qui rouvre après la sieste : sur le chemin, beaucoup de choses se jouent à une heure près.",
   "meca": [
     "<b>L'heure</b> : <i>a la una</i>, puis <i>a las dos, a las tres</i>…",
     '<i>y media</i> (et demie), <i>y cuarto</i> (et quart), <i>menos cuarto</i> (moins le quart).',
     '<b>Antes de</b> = avant ; <b>después de</b> = après.',
     '<b>La journée espagnole</b> : on dîne vers 14 h, on soupe vers 21 h ; beaucoup de commerces ferment de 14 h à 17 h.',
     'Attention : <i>mañana</i> = demain, mais <i>por la mañana</i> = le matin.'],
   "ecoute": [("¿Qué hora es?", "Quelle heure est-il ?"), ("Es la una.", "Il est une heure."),
              ("Son las ocho y media.", "Il est huit heures et demie."), ("a las siete menos cuarto", "à sept heures moins le quart"),
              ("¿A qué hora abre?", "À quelle heure ça ouvre ?"), ("Abre a las cinco.", "Ça ouvre à cinq heures."),
              ("lunes, martes, miércoles, jueves", "lundi, mardi, mercredi, jeudi"), ("viernes, sábado, domingo", "vendredi, samedi, dimanche")],
   "mots": ["a_que_hora", "abierto", "cerrado", "manana", "por_la_tarde", "por_la_noche", "siesta", "hora_siete", "hora_ocho_media", "horario"],
   "quiz": [
     {"type": "rep", "qui": "javier", "es": "La cena es a las siete y media.", "choix": [("Le souper est à 19 h 30.", None), ("Le souper est à 17 h 30.", "Cinco, ce serait 5 (17 h). Siete, c'est 7 : 19 h 30."), ("Le souper est à 19 h 15.", "Y cuarto, ce serait et quart. Y media, c'est et demie.")]},
     {"type": "rep", "qui": "rocio", "es": "Cerramos la puerta a las diez.", "choix": [("On ferme la porte à 22 h.", None), ("On ferme la porte à 12 h.", "Doce, ce serait 12. Diez, c'est 10 — ici 22 h, le soir."), ("On ouvre la porte à 22 h.", "Abrimos, ce serait « on ouvre ». Cerramos : on ferme.")]},
     {"type": "rep", "qui": "manolo", "es": "Abrimos a las cinco, después de la siesta.", "choix": [("On ouvre à 17 h, après la sieste.", None), ("On ouvre à 15 h, après la sieste.", "Tres, ce serait 3 (15 h). Cinco, c'est 5 : 17 h."), ("On ferme à 17 h, pour la sieste.", "Abrimos : on ouvre. Et después de, c'est après.")]},
     {"type": "rep", "qui": "uxia", "es": "Mañana hay que salir antes de las ocho.", "choix": [("Demain, il faut partir avant 8 h.", None), ("Demain, il faut partir après 8 h.", "Después de, ce serait après. Antes de : avant."), ("Ce matin, il faut partir avant 8 h.", "Mañana, seul, c'est demain. Le matin, c'est por la mañana.")]},
     {"type": "rep", "qui": "carmen", "es": "La misa de los peregrinos es a las doce.", "choix": [("La messe des pèlerins est à midi.", None), ("La messe des pèlerins est à 2 h.", "Dos, ce serait 2. Doce, c'est 12 : midi."), ("La messe des pèlerins est à 10 h.", "Diez, ce serait 10. Doce, c'est 12.")]},
     {"type": "rep", "qui": "pilar", "es": "Mañana está cerrado, es domingo.", "choix": [("Demain c'est fermé : c'est dimanche.", None), ("Demain c'est ouvert : c'est dimanche.", "Abierto, ce serait ouvert. Cerrado : fermé."), ("Ce matin c'est fermé : c'est samedi.", "Mañana seul, c'est demain. Et domingo, c'est dimanche.")]},
   ],
   "dire": [("Demandez à quelle heure ça ouvre.", "¿A qué hora abre?", ["a que hora", "abre"]),
            ("Demandez l'heure.", "¿Qué hora es?", ["que hora"]),
            ("Dites « à huit heures et demie ».", "A las ocho y media.", ["ocho", "media"]),
            ("Dites « demain à sept heures ».", "Mañana a las siete.", ["manana", "siete"])]},

  {"id": "p5", "titre": "Quatre verbes qui font presque tout", "obj": "P3", "minutes": 15,
   "intro": "Pas besoin de conjuguer pour se débrouiller : quatre formes toutes faites suffisent pour demander presque tout ce dont on a besoin sur le chemin.",
   "meca": [
     '<b>Quisiera</b> + la chose : je voudrais (poli, pour commander) — <i>quisiera un café</i>.',
     '<b>¿Tiene…?</b> + la chose : vous avez… ? (ce qui existe ici) — <i>¿tiene agua?</i>',
     "<b>Necesito</b> + la chose : j'ai besoin de (l'urgence) — <i>necesito una farmacia</i>.",
     "<b>Me duele</b> + la partie du corps : j'ai mal à — <i>me duele la rodilla</i>.",
     'Une seule forme bouge : <b>me duelen</b>, avec un n, devant plusieurs choses — <i>me duelen los pies</i>.'],
   "ecoute": [("Quisiera una cama.", "Je voudrais un lit."), ("Quisiera un café con leche.", "Je voudrais un café au lait."),
              ("¿Tiene agua?", "Vous avez de l'eau ?"), ("¿Tiene tiritas?", "Vous avez des pansements ?"),
              ("Necesito una farmacia.", "J'ai besoin d'une pharmacie."), ("Necesito ayuda.", "J'ai besoin d'aide."),
              ("Me duele la rodilla.", "J'ai mal au genou."), ("Me duelen los pies.", "J'ai mal aux pieds.")],
   "mots": ["litera", "agua", "farmacia", "tirita", "ampolla", "rodilla", "pie", "espalda", "me_duele", "cafe_leche", "bocadillo"],
   "quiz": [
     {"type": "dire", "fr": "Au bar, vous commandez un sandwich.", "choix": [("Quisiera un bocadillo, por favor.", None), ("Me duele un bocadillo, por favor.", "Me duele, c'est « j'ai mal à ». Pour commander : quisiera."), ("Tengo un bocadillo, por favor.", "Tengo, c'est « j'ai » : vous annoncez que vous en avez déjà un. Pour commander : quisiera.")]},
     {"type": "dire", "fr": "À la pharmacie : vous avez mal au genou.", "choix": [("Me duele la rodilla.", None), ("Quisiera la rodilla.", "Quisiera, c'est « je voudrais » : vous demandez un genou ! Pour la douleur : me duele."), ("Me duelen la rodilla.", "Un seul genou : me duele. Me duelen, c'est pour plusieurs (los pies).")]},
     {"type": "dire", "fr": "Vous avez mal aux deux pieds.", "choix": [("Me duelen los pies.", None), ("Me duele los pies.", "Les pieds sont plusieurs : me duelen, avec un n."), ("Necesito los pies.", "Necesito, c'est « j'ai besoin de ». Pour la douleur : me duelen.")]},
     {"type": "dire", "fr": "Vous voulez savoir si l'épicerie a de l'eau.", "choix": [("¿Tiene agua?", None), ("¿Quisiera agua?", "Quisiera, c'est « je voudrais » : ici, vous posez une question sur ce qu'ils ont. ¿Tiene…?"), ("¿Me duele agua?", "Me duele, c'est « j'ai mal à ». La question : ¿tiene agua?")]},
     {"type": "dire", "fr": "Une ampoule vous fait souffrir : il vous faut une pharmacie.", "choix": [("Necesito una farmacia.", None), ("Tiene una farmacia.", "Sans le ton de la question, tiene veut dire « il a » : on ne comprend pas ce que vous voulez. Pour un besoin : necesito."), ("Me duele una farmacia.", "Me duele, c'est la douleur : c'est l'ampoule qui fait mal, pas la pharmacie.")]},
     {"type": "rep", "qui": "pilar", "es": "¿Le duele mucho?", "choix": [("Ça vous fait très mal ?", None), ("Vous en voulez beaucoup ?", "Querer, ce serait vouloir. Duele, c'est la douleur."), ("Vous avez besoin de beaucoup ?", "Necesitar, ce serait avoir besoin. Duele : ça fait mal.")]},
   ],
   "dire": [("Demandez un lit.", "Quisiera una cama, por favor.", ["quisiera", "cama"]),
            ("Demandez s'ils ont des pansements.", "¿Tiene tiritas?", ["tiene", "tiritas"]),
            ("Dites que vous avez mal au dos.", "Me duele la espalda.", ["duele", "espalda"]),
            ("Dites que vous avez besoin d'aide.", "Necesito ayuda.", ["necesito", "ayuda"])]},

  {"id": "p6", "titre": "Poser une question", "obj": "P3", "minutes": 15,
   "intro": "Où, combien, à quelle heure, est-ce qu'il y a : avec quatre mots, on peut trouver presque tout ce qu'on cherche dans un village.",
   "meca": [
     '<b>¿Dónde está…?</b> où est… ? — <i>¿dónde está el albergue?</i>',
     '<b>¿Cuánto cuesta?</b> combien ça coûte ? · <b>¿A qué hora…?</b> à quelle heure… ?',
     '<b>¿Hay…?</b> y a-t-il… ? — un seul petit mot, pour tout : <i>¿hay agua?</i>, <i>¿hay una farmacia?</i>',
     'Pour les lits : <i>¿quedan camas?</i> (il en reste ?).',
     "La voix <b>monte</b> à la fin ; à l'écrit, le <b>¿</b> à l'envers ouvre la question."],
   "ecoute": [("¿Dónde está el albergue?", "Où est l'albergue ?"), ("¿Dónde está la ducha?", "Où est la douche ?"),
              ("¿Hay una farmacia cerca?", "Y a-t-il une pharmacie près d'ici ?"), ("¿Hay agua potable?", "Y a-t-il de l'eau potable ?"),
              ("¿Cuánto cuesta?", "Combien ça coûte ?"), ("¿Quedan camas?", "Reste-t-il des lits ?"),
              ("¿A qué hora es la cena?", "À quelle heure est le souper ?"), ("¿Por dónde se va a la iglesia?", "Par où va-t-on à l'église ?")],
   "mots": ["albergue", "farmacia", "supermercado", "panaderia", "parada", "quedan", "fuente", "iglesia", "ducha", "enchufe"],
   "quiz": [
     {"type": "dire", "fr": "Vous cherchez l'albergue.", "choix": [("¿Dónde está el albergue?", None), ("¿Cuánto cuesta el albergue?", "Vous demandez le prix, pas le chemin. Pour trouver : ¿dónde está?"), ("¿A qué hora el albergue?", "À quelle heure… quoi ? Pour trouver l'endroit : ¿dónde está?")]},
     {"type": "dire", "fr": "Vous avez soif : y a-t-il une fontaine près d'ici ?", "choix": [("¿Hay una fuente por aquí?", None), ("¿Está una fuente por aquí?", "Está sert à situer une chose qu'on connaît (¿dónde está la fuente?). Pour savoir s'il en existe une : ¿hay…?"), ("¿Cuánto cuesta la fuente?", "La fontaine est gratuite ! Pour savoir s'il y en a une : ¿hay…?")]},
     {"type": "dire", "fr": "Vous voulez le prix du pain.", "choix": [("¿Cuánto cuesta el pan?", None), ("¿Dónde está el pan?", "Vous demandez où il est. Pour le prix : ¿cuánto cuesta?"), ("¿Hay el pan?", "¿Hay…? demande s'il y en a, et sans « el » : ¿hay pan? Pour le prix : ¿cuánto cuesta?")]},
     {"type": "dire", "fr": "À l'albergue : reste-t-il des lits ?", "choix": [("¿Quedan camas?", None), ("¿Cuánto camas?", "Cuánto demande une quantité — et il faudrait cuántas. La vraie question est plus simple : ¿quedan camas?"), ("¿Duelen camas?", "Duelen, c'est « font mal ». Pour les lits qui restent : ¿quedan camas?")]},
     {"type": "rep", "qui": "rocio", "es": "La ducha está al fondo, a la izquierda.", "choix": [("La douche est au fond, à gauche.", None), ("La douche est au fond, à droite.", "Derecha, ce serait à droite. Izquierda : à gauche."), ("La douche est en haut, à gauche.", "Arriba, ce serait en haut. Al fondo : au fond.")]},
     {"type": "rep", "qui": "fermin", "es": "No, aquí no hay farmacia. Hay una en el pueblo siguiente.", "choix": [("Pas de pharmacie ici ; au village suivant, oui.", None), ("Il y a une pharmacie ici, au bout du village.", "« Aquí no hay » : ici, il n'y en a pas. Elle est au pueblo siguiente, le village suivant."), ("La pharmacie du village est fermée aujourd'hui.", "Rien n'est fermé : il n'y en a pas ici, mais au village suivant.")]},
   ],
   "dire": [("Demandez où est la pharmacie.", "¿Dónde está la farmacia?", ["donde", "farmacia"]),
            ("Demandez s'il y a de l'eau potable.", "¿Hay agua potable?", ["hay", "agua"]),
            ("Demandez combien coûte le lit.", "¿Cuánto cuesta la cama?", ["cuanto", "cama"]),
            ("Demandez à quelle heure est le souper.", "¿A qué hora es la cena?", ["a que hora", "cena"])]},

  {"id": "p7", "titre": "Parler de soi", "obj": "P4", "minutes": 15,
   "intro": "Sur le chemin, la première question qu'on vous posera est d'où vous venez. La deuxième : pourquoi vous marchez. Préparez vos trois phrases — elles serviront tous les soirs.",
   "meca": [
     "<b>Soy de…</b> pour l'origine : <i>soy de Quebec, en Canadá</i>.",
     '<b>Hago el Camino por…</b> pour la raison : <i>por el deporte, por mi familia, por la fe</i> — ou <i>para pensar</i>.',
     "<b>Soy</b> pour ce qu'on est (<i>alérgic{<b>o</b>|<b>a</b>}</i>), <b>estoy</b> pour ce qui passe (<i>cansad{<b>o</b>|<b>a</b>}</i>).",
     'Entre pèlerins, on se tutoie : <i>¿De dónde eres? ¿Por qué haces el Camino?</i>'],
   "ecoute": [("Soy de Quebec, en Canadá.", "Je viens du Québec, au Canada."), ("Hago el Camino por el deporte.", "Je fais le Chemin pour le sport."),
              ("Hago el Camino por mi familia.", "Je fais le Chemin pour ma famille."), ("Soy alérgic{o|a} {alg:a}.", "Je suis allergique {alg:fr}."),
              ("Estoy cansad{o|a}.", "Je suis fatigué{|e}."), ("¿De dónde eres?", "D'où viens-tu ?"),
              ("¿Por qué haces el Camino?", "Pourquoi fais-tu le Chemin ?"), ("Encantad{o|a}.", "Enchanté{|e}.")],
   "mots": ["soy_de", "de_donde", "por_que", "desde_donde", "encantado", "alergico", "cansado", "peregrino"],
   "quiz": [
     {"type": "rep", "qui": "marta", "es": "¿De dónde eres?", "choix": [("D'où viens-tu ?", None), ("Où dors-tu ce soir ?", "Ce serait ¿dónde duermes? Ici : ¿de dónde eres?, d'où viens-tu."), ("Où vas-tu aujourd'hui ?", "Ce serait ¿hasta dónde vas? Ici, on te demande ton pays.")]},
     {"type": "rep", "qui": "marta", "es": "¿Y por qué haces el Camino?", "choix": [("Et pourquoi fais-tu le Chemin ?", None), ("Et depuis quand marches-tu ?", "Ce serait ¿desde cuándo? Por qué, c'est pourquoi."), ("Et combien de kilomètres fais-tu ?", "Ce serait ¿cuántos kilómetros? Por qué : pourquoi.")]},
     {"type": "dire", "fr": "Répondez : vous venez du Québec.", "choix": [("Soy de Quebec, en Canadá.", None), ("Estoy de Quebec, en Canadá.", "L'origine ne passe pas : soy de…"), ("Voy a Quebec, en Canadá.", "Voy a, c'est « je vais à » : on croira que vous rentrez chez vous !")]},
     {"type": "rep", "qui": "marta", "es": "Yo soy de Valladolid. Hago el Camino por mi marido.", "choix": [("Elle vient de Valladolid ; elle marche pour son mari.", None), ("Elle va à Valladolid avec son mari.", "Soy de : elle en vient. Por mi marido : pour lui, en pensant à lui."), ("Elle vient de Valladolid ; son mari marche aussi.", "Rien ne dit qu'il marche : elle fait le Chemin por mi marido, pour lui.")]},
     {"type": "dire", "fr": "Vous êtes fatigué{|e}.", "choix": [("Estoy cansad{o|a}.", None), ("Soy cansad{o|a}.", "La fatigue passe : estoy. Soy cansad{o|a}, ce serait être une personne fatigante !"), ("Tengo cansad{o|a}.", "Tengo, c'est « j'ai ». La fatigue : estoy cansad{o|a}.")]},
     {"type": "dire", "fr": "On vient de vous présenter quelqu'un.", "choix": [("Encantad{o|a}.", None), ("Cansad{o|a}.", "Cansad{o|a}, c'est fatigué{|e} : pas très aimable pour une présentation !"), ("De nada.", "De nada répond à un merci. Pour une rencontre : encantad{o|a}.")]},
   ],
   "dire": [("Dites d'où vous venez.", "Soy de Quebec, en Canadá.", ["soy de"]),
            ("Dites pourquoi vous marchez — par exemple, pour le sport.", "Hago el Camino por el deporte.", ["camino", "por|para"]),
            ("Dites votre allergie.", "Soy alérgic{o|a} {alg:a}.", ["alergic{o|a}", "{alg:sans}"]),
            ("Demandez à un pèlerin d'où il vient.", "¿De dónde eres?", ["de donde"])]},

  {"id": "p8", "titre": "Comprendre la réponse", "obj": "P5", "minutes": 15,
   "intro": "Le plus dur n'est pas de demander : c'est d'entendre la réponse, dite vite, avec l'accent d'ici. Le secret : guetter le mot qui décide, et laisser filer le reste.",
   "meca": [
     '<b>Sí</b> / <b>no</b> — souvent répété : <i>sí, sí</i>.',
     "<b>Hay</b> (il y en a) / <b>no hay</b> (il n'y en a pas).",
     "<b>Quedan</b> (il en reste) / <b>está completo</b> (c'est complet).",
     '<b>A la derecha</b> (à droite) / <b>a la izquierda</b> (à gauche) / <b>todo recto</b> (tout droit).',
     "<b>Lleva</b> (ça en contient) / <b>no lleva</b> (ça n'en contient pas).",
     'Le reste de la phrase peut vous échapper : ce mot-là, non.'],
   "ecoute": [("Sí, claro.", "Oui, bien sûr."), ("No, no hay.", "Non, il n'y en a pas."),
              ("Lo siento, está completo.", "Désolé, c'est complet."), ("Quedan tres camas.", "Il reste trois lits."),
              ("A la derecha.", "À droite."), ("A la izquierda.", "À gauche."),
              ("Todo recto.", "Tout droit."), ("Sí, lleva. — No, no lleva.", "Oui, ça en contient. — Non, ça n'en contient pas.")],
   "mots": ["completo", "izquierda", "derecha", "recto", "lleva", "cruce", "subida", "bajada", "arriba", "abajo"],
   "quiz": [
     {"type": "rep", "qui": "rocio", "es": "Lo siento, hoy está completo.", "choix": [("Désolée, aujourd'hui c'est complet.", None), ("Désolée, aujourd'hui c'est fermé.", "Cerrado, ce serait fermé. Completo : il n'y a plus de place."), ("Il reste une place aujourd'hui.", "Queda una cama, ce serait ça. Completo : plus rien.")]},
     {"type": "rep", "qui": "javier", "es": "Sí, sí, quedan tres camas.", "choix": [("Oui, il reste trois lits.", None), ("Oui, il y a trois douches.", "Duchas, ce serait des douches. Camas : des lits."), ("Non, il n'y a plus de lits.", "Il a dit sí, sí, et quedan : il en reste.")]},
     {"type": "rep", "qui": "fermin", "es": "Todo recto, y después a la derecha.", "choix": [("Tout droit, puis à droite.", None), ("Tout droit, puis à gauche.", "Izquierda, ce serait à gauche. Derecha : à droite."), ("À droite, puis tout droit.", "L'ordre compte : todo recto d'abord, después (ensuite) a la derecha.")]},
     {"type": "rep", "qui": "ainhoa", "es": "No, hoy no hay tortilla.", "choix": [("Non, pas de tortilla aujourd'hui.", None), ("Oui, la tortilla est prête, servez-vous.", "No hay : il n'y en a pas."), ("Il n'y a que de la tortilla aujourd'hui.", "No hay tortilla : il n'y en a pas du tout.")]},
     {"type": "rep", "qui": "alex", "es": "Sí, la ensalada lleva huevo.", "choix": [("Oui, la salade contient de l'œuf.", None), ("Non, la salade ne contient pas d'œuf.", "Il a dit sí, lleva : elle en contient. Le « no lleva » serait l'inverse."), ("Il n'y a plus de salade.", "Rien ne manque : la salade existe, et lleva huevo, elle contient de l'œuf.")]},
     {"type": "rep", "qui": "manolo", "es": "A la izquierda, al lado de la panadería.", "choix": [("À gauche, à côté de la boulangerie.", None), ("À droite, à côté de la boulangerie.", "Derecha, ce serait à droite. Izquierda : à gauche."), ("À gauche, en face de la boulangerie.", "Enfrente, ce serait en face. Al lado : à côté.")]},
   ],
   "dire": [("On vous dit que c'est complet. Demandez s'il y a une autre albergue.", "¿Hay otro albergue?", ["hay", "otro"]),
            ("On vous indique la droite. Dites « d'accord, merci beaucoup ».", "Vale, muchas gracias.", ["gracias"]),
            ("Vous n'avez pas compris la direction.", "Perdone, ¿puede repetir?", ["repetir"])]},
]

# Le test « Prêt à partir ? » (révisé au tour 1 de la boucle, A3/F1) : chaque
# objectif est mesuré comme son critère le dit. P1 et P3 : DITS au micro, deux
# essais au plus (« au 1er ou au 2e essai »). P2 et P5 : entendus UNE fois, au
# débit naturel. P4 : une seule tâche, se présenter en trois phrases, dont
# l'allergie et l'accord. Deux formes parallèles ; phrases surtout nouvelles
# (les formules figées de P1 sont, par nature, celles des séances).
TEST = [
  [
    {"obj": "P1", "type": "oral", "fr": "Demandez poliment de parler plus lentement.", "cles": ["despacio"], "modele": "Más despacio, por favor."},
    {"obj": "P1", "type": "oral", "fr": "Remerciez beaucoup.", "cles": ["muchas", "gracias"], "modele": "Muchas gracias."},
    {"obj": "P1", "type": "oral", "fr": "Dites que vous ne comprenez pas.", "cles": ["no entiendo"], "modele": "Perdone, no entiendo."},
    {"obj": "P2", "type": "rep", "qui": "alex", "es": "Son catorce con cincuenta.", "choix": [("14,50 €", None), ("40,50 €", "Cuarenta, ce serait 40. Catorce, c'est 14."), ("4,50 €", "Cuatro, ce serait 4. Catorce, c'est 14.")]},
    {"obj": "P2", "type": "rep", "qui": "uxia", "es": "El desayuno es a las siete menos cuarto.", "choix": [("Le déjeuner est à 6 h 45.", None), ("Le déjeuner est à 7 h 15.", "Y cuarto, ce serait et quart. Menos cuarto : moins le quart."), ("Le déjeuner est à 7 h 45.", "Siete menos cuarto, c'est sept heures moins le quart : 6 h 45.")]},
    {"obj": "P2", "type": "rep", "qui": "manolo", "es": "Son dieciséis euros.", "choix": [("16 €", None), ("6 €", "Seis, ce serait 6. Dieciséis, c'est 16."), ("60 €", "Sesenta, ce serait 60. Dieciséis, c'est 16.")]},
    {"obj": "P2", "type": "rep", "qui": "rocio", "es": "Cerramos a las nueve.", "choix": [("On ferme à 21 h.", None), ("On ferme à 22 h.", "Diez, ce serait 10. Nueve, c'est 9 — ici 21 h."), ("On ouvre à 21 h.", "Abrimos, ce serait « on ouvre ». Cerramos : on ferme.")]},
    {"obj": "P3", "type": "oral", "fr": "À la pharmacie, demandez de la crème solaire.", "cles": ["quisiera|tiene|necesito", "crema"], "modele": "Quisiera crema solar, por favor."},
    {"obj": "P3", "type": "oral", "fr": "Demandez où est la fontaine.", "cles": ["donde", "fuente"], "modele": "¿Dónde está la fuente?"},
    {"obj": "P3", "type": "oral", "fr": "Vous avez mal à l'épaule : dites-le à la pharmacienne.", "cles": ["duele", "hombro"], "modele": "Me duele el hombro."},
    {"obj": "P4", "type": "oral", "fr": "Présentez-vous en trois phrases : d'où vous venez, pourquoi vous marchez, et votre allergie.",
     "cles": ["soy de", "camino", "por|para", "alergic{o|a}", "{alg:sans}"],
     "parties": ["d'où vous venez (soy de…)", "le Chemin (hago el Camino…)", "la raison (por… ou para…)", "allergique, au bon genre", "l'aliment de votre allergie"],
     "modele": "Soy de Quebec, en Canadá. Hago el Camino por el deporte. Soy alérgic{o|a} {alg:a}."},
    {"obj": "P5", "type": "rep", "qui": "javier", "es": "No, ya no quedan camas. Hay un hostal en la plaza.", "choix": [("Plus de lits ; il y a un petit hôtel sur la place.", None), ("Il reste des lits, sur la place.", "Ya no quedan : il n'en reste plus. L'hostal, lui, est sur la place."), ("Plus de lits ; l'hôtel de la place est plein.", "Rien n'est dit de l'hôtel, sinon qu'il existe : hay un hostal.")]},
    {"obj": "P5", "type": "rep", "qui": "fermin", "es": "Sigue todo recto hasta el puente.", "choix": [("Continuez tout droit jusqu'au pont.", None), ("Tournez à droite au pont.", "Derecha n'a pas été dit : todo recto, tout droit."), ("Continuez tout droit jusqu'à l'église.", "La iglesia, ce serait l'église. El puente : le pont.")]},
    {"obj": "P5", "type": "rep", "qui": "rocio", "es": "Sí, sí, queda una cama.", "choix": [("Oui, il reste un lit.", None), ("Non, il ne reste plus de lit.", "Sí, sí, et queda : il en reste un."), ("Oui, il reste une douche.", "Ducha, ce serait une douche. Cama : un lit.")]},
    {"obj": "P5", "type": "rep", "qui": "alex", "es": "No, la sopa no lleva huevo.", "choix": [("La soupe ne contient pas d'œuf.", None), ("La soupe contient de l'œuf.", "No lleva : elle n'en contient pas."), ("Il n'y a pas de soupe ce soir.", "La soupe existe ; c'est l'œuf qui n'y est pas.")]},
  ],
  [
    {"obj": "P1", "type": "oral", "fr": "Demandez de répéter, poliment.", "cles": ["repetir"], "modele": "¿Puede repetir, por favor?"},
    {"obj": "P1", "type": "oral", "fr": "Il est 17 h : saluez en entrant dans une boutique.", "cles": ["buenas tardes"], "modele": "Buenas tardes."},
    {"obj": "P1", "type": "oral", "fr": "Excusez-vous : vous avez bousculé quelqu'un.", "cles": ["lo siento|perdone|perdona"], "modele": "Perdone, lo siento."},
    {"obj": "P2", "type": "rep", "qui": "manolo", "es": "Son siete con treinta.", "choix": [("7,30 €", None), ("6,30 €", "Seis, ce serait 6. Siete, c'est 7."), ("7,13 €", "Trece, ce serait 13. Treinta, c'est 30.")]},
    {"obj": "P2", "type": "rep", "qui": "rocio", "es": "Abrimos el albergue a la una y cuarto.", "choix": [("On ouvre l'albergue à 13 h 15.", None), ("On ouvre l'albergue à 12 h 45.", "Menos cuarto, ce serait moins le quart. Y cuarto : et quart."), ("On ferme l'albergue à 13 h 15.", "Abrimos : on ouvre.")]},
    {"obj": "P2", "type": "rep", "qui": "ainhoa", "es": "Son cuarenta euros.", "choix": [("40 €", None), ("14 €", "Catorce, ce serait 14. Cuarenta, c'est 40."), ("4 €", "Cuatro, ce serait 4. Cuarenta, c'est 40.")]},
    {"obj": "P2", "type": "rep", "qui": "carmen", "es": "La misa es a las ocho menos cuarto.", "choix": [("La messe est à 7 h 45.", None), ("La messe est à 8 h 15.", "Y cuarto, ce serait et quart. Menos cuarto : moins le quart, donc 7 h 45."), ("La messe est à 8 h 45.", "Ocho menos cuarto, c'est huit heures moins le quart : 7 h 45.")]},
    {"obj": "P3", "type": "oral", "fr": "Demandez s'il y a une pharmacie près d'ici.", "cles": ["hay", "farmacia"], "modele": "¿Hay una farmacia cerca?"},
    {"obj": "P3", "type": "oral", "fr": "Au bar, demandez un jus d'orange.", "cles": ["quisiera|tiene", "zumo"], "modele": "Quisiera un zumo de naranja."},
    {"obj": "P3", "type": "oral", "fr": "Il vous faut un taxi : dites-le à l'hospitalière.", "cles": ["necesito", "taxi"], "modele": "Necesito un taxi."},
    {"obj": "P4", "type": "oral", "fr": "Un pèlerin vous demande qui vous êtes. Répondez en trois phrases : d'où vous venez, pourquoi vous marchez, et votre allergie.",
     "cles": ["soy de", "camino", "por|para", "alergic{o|a}", "{alg:sans}"],
     "parties": ["d'où vous venez (soy de…)", "le Chemin (hago el Camino…)", "la raison (por… ou para…)", "allergique, au bon genre", "l'aliment de votre allergie"],
     "modele": "Soy de Quebec, en Canadá. Hago el Camino por el deporte. Soy alérgic{o|a} {alg:a}."},
    {"obj": "P5", "type": "rep", "qui": "alex", "es": "No, el postre no lleva leche.", "choix": [("Non, pas de lait dans le dessert.", None), ("Oui, le dessert contient du lait.", "No lleva : il n'en contient pas."), ("Il n'y a pas de dessert ce soir.", "Le dessert existe ; c'est le lait qui n'y est pas.")]},
    {"obj": "P5", "type": "rep", "qui": "fermin", "es": "La segunda calle a la izquierda.", "choix": [("La deuxième rue à gauche.", None), ("La deuxième rue à droite.", "Derecha, ce serait à droite. Izquierda : à gauche."), ("La première rue à gauche.", "Primera, ce serait la première. Segunda : la deuxième.")]},
    {"obj": "P5", "type": "rep", "qui": "manolo", "es": "Lo siento, hoy está cerrado.", "choix": [("Désolé, c'est fermé aujourd'hui.", None), ("Désolé, c'est complet aujourd'hui.", "Completo, ce serait complet. Cerrado : fermé."), ("Désolé, c'est ouvert demain seulement.", "Rien n'est dit de demain : hoy, aujourd'hui, está cerrado.")]},
    {"obj": "P5", "type": "rep", "qui": "uxia", "es": "Sí, hay agua en la fuente de la plaza.", "choix": [("Il y a de l'eau à la fontaine de la place.", None), ("Il n'y a pas d'eau à la fontaine.", "Sí, hay : il y en a."), ("L'eau de la place n'est pas potable.", "Rien n'est dit de la qualité : hay agua, il y a de l'eau.")]},
  ],
]
PAR_OBJECTIF = {"P1": 3, "P2": 4, "P3": 3, "P4": 1, "P5": 4}

SEUIL = "Solide : 80 % ou plus ; En route : au moins la moitié ; À reprendre : moins de la moitié. Au micro, deux essais au plus ; les phrases entendues ne s'écoutent qu'une fois."
CONSEILS = {"P1": "Reprenez les séances 1 et 2, au micro.", "P2": "Reprenez les séances 3 et 4, voix plus lentes d'abord.",
            "P3": "Reprenez les séances 5 et 6.", "P4": "Reprenez la séance 7, et préparez vos trois phrases.",
            "P5": "Reprenez la séance 8 : guettez le mot qui décide."}


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
        for fr, es, cles in s["dire"]:
            assert fr and es and cles, s["id"]
    for f, forme in enumerate(TEST):
        objs = [it["obj"] for it in forme]
        for o in OBJECTIFS:
            assert objs.count(o) == PAR_OBJECTIF[o], (f, o)
        for it in forme:
            if it["type"] == "oral":
                assert it["cles"] and it["modele"], it
                assert "parties" not in it or len(it["parties"]) == len(it["cles"]), it
            else:
                _item(it, f"test{f}", personnages)
    return True


def _item(q, ou, personnages):
    assert q["type"] in ("rep", "mot", "dire"), (ou, q)
    assert len(q["choix"]) >= 3, (ou, q)
    assert q["choix"][0][1] is None, (ou, q)
    assert all(r for _, r in q["choix"][1:]), ("rétroaction manquante", ou, q)
    if q["type"] == "rep":
        assert q.get("qui") and (personnages is None or q["qui"] in personnages), (ou, q)
    if q["type"] in ("rep", "mot"):
        assert q.get("es"), (ou, q)
    else:
        assert q.get("fr"), (ou, q)


if __name__ == "__main__":
    import importlib.util, pathlib
    ici = pathlib.Path(__file__).resolve().parent
    def charger(n):
        sp = importlib.util.spec_from_file_location("x_" + n, ici / f"{n}.py"); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
    lx = {e[0] for e in charger("lexique").LEXIQUE}
    verifier(lx, charger("personnages").PERSONNAGES)
    n_q = sum(len(s["quiz"]) for s in SEANCES); n_e = sum(len(s["ecoute"]) for s in SEANCES); n_d = sum(len(s["dire"]) for s in SEANCES)
    print(f"{len(SEANCES)} séances : {n_e} phrases à écouter, {n_q} questions, {n_d} phrases à dire ; test : {sum(len(f) for f in TEST)} items")
    longue = sum(1 for s in SEANCES for q in s["quiz"] if len(q["choix"][0][0]) >= max(len(c[0]) for c in q["choix"]))
    print(f"la bonne réponse est la plus longue dans {longue} questions sur {n_q}")
