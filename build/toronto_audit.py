#!/usr/bin/env python3
"""Le journal de la boucle didactique d'« Une semaine à Toronto » — ses trois boucles.

    python3 build/toronto_audit.py   # → assets/presentations/toronto/toronto-audit.html

Chaque tour : l'audit d'un regard extérieur (sous-agent, grille de 23 critères de
la compétence boucle-didactique, contenu lu, moteur rejoué par script), puis la
révision. Chaque constat garde son code, sa gravité, et ce qui en a été fait.
Les mineurs sont regroupés : la page garde les bloquants, les majeurs et les
mineurs qui ont changé quelque chose de visible.
"""
import html, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "toronto" / "toronto-audit.html"
E = html.escape

# (code, gravité, endroit, constat, ce qui a été fait)
TOURS = [
 {"tour": 1, "commit": "3e300a666", "compte": (1, 9, 14),
  "note": "Audit de la version zéro : contenu lu en entier, comparé à Compostelle, bilan du moteur relu.",
  "constats": [
   ("D4/F1", "bloquant", "Test, compréhension (P5)",
    "La bonne réponse était toujours la plus longue, et chaque mauvais choix ne changeait qu'un trait : on obtenait « Solide » sans écouter, et on sautait la séance 8.",
    "Choix de même longueur, le leurre porté par deux mauvais choix ; contrôle ajouté : au test, la bonne n'est jamais nettement la plus longue."),
   ("A3", "majeur", "Test, prononciation (P1)",
    "Aucune clé ne dépendait des sons de la séance 1 : la reconnaissance corrige d'elle-même « tank you ».",
    "Une phrase par forme où le son raté change le mot (three/tree, leaving/living)."),
   ("C/E1", "majeur", "Séance 3, nombres",
    "La règle « thirTEEN, accent à la fin » est fausse devant un autre nombre (« thirteen fifty ») : la voix l'aurait contredite.",
    "On enseigne la fin du mot : -teen finit long sur un « n », -ty finit court."),
   ("F1/A1", "majeur", "Seuil",
    "« 80 % » sur trois ou quatre questions voulait dire 100 % ; la présentation comptait tout ou rien.",
    "Seuil dit en nombres (3 sur 3 au micro, 3 sur 4 à l'écoute), appliqué à 75 % ; présentation comptée par parties."),
   ("F1/A3", "majeur", "Test, forme 2",
    "Les mots qui décident (downstairs, last orders, up to you) n'étaient enseignés nulle part ; et plusieurs phrases du test reprenaient celles des séances.",
    "Items refaits sur des mots enseignés ; situations neuves."),
   ("clés", "majeur", "Micro",
    "Des réponses justes étaient refusées : « We're from Sherbrooke », « And yourself? », « I'll have a tea », « Sorry? ».",
    "Clés partagées DEMANDE, REPETER, ORIGINE, SEJOUR, RELANCE ; un contrôle exige que chaque modèle passe ses propres clés."),
   ("D4", "majeur", "Quiz « Que dites-vous ? »",
    "Des mauvais choix absurdes (« Okay. », « Goodbye. ») que personne ne choisirait.",
    "Remplacés par de vraies erreurs de francophones (« Where you are from? », « Does this streetcar goes… »)."),
 ]},
 {"tour": 2, "commit": "b65c4f37e", "compte": (1, 4, 12),
  "note": "Le motif de toute la boucle paraît ici : le bloquant naît de la correction du tour précédent.",
  "constats": [
   ("D4/F1", "bloquant", "Test, P2 et P5",
    "Le leurre porté par DEUX mauvais choix laissait la bonne seule de son côté : « prendre l'exception » réussissait la compréhension sans écouter. Et le mélange était une rotation : la bonne précédait toujours le leurre.",
    "Les items à deux traits passent au carré complet à quatre choix (chaque valeur deux fois) ; mélange à graine stable. Six stratégies aveugles calculées par script."),
   ("A1/F1", "majeur", "Test, P1",
    "« Three tickets » : le contexte suffit à la reconnaissance, « tree tickets » serait accepté.",
    "La paire minimale là où le contexte ne tranche pas : « Trois. » seul."),
   ("F1", "majeur", "Test, P3",
    "« Can you give me a tea? », « We'd like a tea » refusés ; un seul refus empêche « Solide ».",
    "DEMANDE accepte « we », « give me », « I want »."),
   ("F1/G2", "majeur", "Bilan",
    "Passer une question « sans micro » la retirait du compte : 2 sur 2 donnait « Solide ».",
    "Une question passée sans micro empêche « Solide »."),
 ]},
 {"tour": 3, "commit": "796e9e167", "compte": (1, 3, 13),
  "note": "L'auditeur rejoue la logique du moteur en Node et tire les ordres affichés.",
  "constats": [
   ("D4/F1", "bloquant", "Test, ordre des choix",
    "Le mélange à graine fixe mettait la bonne au troisième bouton 9 fois sur 16 : « dans le doute, C » donnait « Solide » en compréhension.",
    "Place de la bonne posée dans les données (permutation par objectif et par forme), décalée à chaque passage."),
   ("D4", "majeur", "Test, carte et pourboire",
    "Choisir l'option dont les mots reviennent le plus désignait la bonne : P(Solide) = 0,50 contre 0,05 au hasard.",
    "Choix refaits en carré sans convergence."),
   ("F1/A3", "majeur", "Clés du test",
    "« I'm sunburned », « My husband has a fever », « One week », « Do you live here? » refusés.",
    "Clé MAL (le cadre d'une plainte) ; SEJOUR et RELANCE élargies."),
   ("F1/D1", "majeur", "Présentation (P4)",
    "Après un premier essai raté, le message nommait la formule anglaise attendue : la réponse soufflée avant le second essai noté.",
    "Le message nomme la partie (« d'où vous venez »), jamais la formule."),
 ]},
 {"tour": 4, "commit": "bc0b33a92", "compte": (1, 2, 7),
  "note": "Troisième bloquant de la même famille : une place de réponse déterministe finit toujours par se lire.",
  "constats": [
   ("D4/F1", "bloquant", "Test, places",
    "La bonne s'affiche après chaque réponse : la permutation se déduisait par élimination (le 4e item, au bouton pas encore sorti) et par paires opposées (P = 0,62).",
    "Tirage au hasard à chaque affichage, au test comme en séance : ferme la famille des tours 2 à 4."),
   ("F1", "majeur", "Clés ORIGINE et SEJOUR",
    "« I'm in Toronto for a week » comptait comme une origine ; « I arrived two days ago », comme une durée.",
    "Clés resserrées ; 19 réponses témoins (refus et acceptations) vérifiées à chaque construction."),
   ("F1", "majeur", "Troisième passage",
    "Avec deux formes, le 3e passage refait une forme déjà vue, réponses montrées : il mesure la mémoire.",
    "Le bilan le dit au lieu d'autoriser à sauter les séances."),
 ]},
 {"tour": 5, "commit": "dab7f6787", "compte": (0, 2, 4),
  "note": "Premier tour sans bloquant. La place des réponses est confirmée uniforme et inexploitable (100 000 tirages).",
  "constats": [
   ("F1/E1", "majeur", "SEJOUR",
    "« I'm here since two days », le calque de « depuis deux jours », comptait encore comme une durée.",
    "Refusé, comme « I've been here for two days »."),
   ("F1/D2", "majeur", "Clés P3",
    "« I'm really sunburned », « I'm feeling feverish », « How do I get to the bus stop? » (la forme enseignée) refusés.",
    "MAL accepte adverbes, passé et « feeling » ; « où » accepte « How do I get to… »."),
   ("outillage", "mineur", "Contrôle",
    "Les réponses témoins ne prouvaient que la logique Python, pas celle de la page.",
    "Rejouées aussi dans la page (window.__toronto.controle) ; aplatir et cle_ok alignés sur plat et trouve."),
 ]},
 {"tour": 6, "commit": "ce tour", "compte": (0, 1, 6),
  "note": "Tour court, limité aux clés : environ 260 réponses passées dans la vraie logique de la page.",
  "constats": [
   ("F1", "majeur", "REPETER",
    "« What did you say? », calque direct de « Qu'est-ce que vous avez dit ? », refusé sur un item qui compte pour « Solide ».",
    "Accepté, avec « What was that? » ; « What? » seul reste refusé."),
   ("F1", "mineur", "SEJOUR, DEMANDE",
    "« since » refusé partout dans la phrase ; « please » faisait passer « Do you want a tea, please? ».",
    "Filtres ciblés ; les cas testés entrent dans les réponses témoins (47 en tout)."),
 ]},
]

# ── Les exercices (étape 4) : six tours, 1er oct. 2026.
TOURS_EXOS = [
 {"tour": 1, "commit": "e368a2fb1", "compte": (1, 5, 12),
  "note": "Audit de la version zéro : chaque famille jouée par script, stratégies aveugles calculées, clés rejouées dans la page.",
  "constats": [
   ("A3", "bloquant", "Alignement",
    "La série de l'allergie, promise au cadrage pour l'objectif éliminatoire (O3), n'existait pas.",
    "Série « L'allergie » : la règle affichée avant, un carré (allergène ou non × sûr ou à vérifier), un contre-exemple où l'on peut commander."),
   ("D4", "majeur", "Le total à payer",
    "Le contexte français donnait la règle (« pas de pourboire ») : l'anglais n'était plus nécessaire.",
    "Carré : le prix bien ou mal entendu (teen/ty) × la règle tenue ou oubliée ; tout se calcule."),
   ("D3", "majeur", "Faux amis",
    "Tous les choix qui ressemblaient étaient faux : « éviter la ressemblance » gagnait toujours.",
    "Des vrais amis (souvenir, menu, terminal) mêlés à la série."),
   ("D4", "majeur", "Carrés",
    "Un quatrième choix qui perdait un segment se repérait comme « l'opposé du plus court ».",
    "Le quatrième se compose des segments EXACTS des choix 2 et 3."),
   ("A3", "majeur", "Je le dis",
    "Le bavardage et « faire répéter » manquaient aux situations à dire.",
    "Ajoutés, avec leurs clés et leurs réponses témoins."),
 ]},
 {"tour": 2, "commit": "9a2672d2c", "compte": (0, 5, 12),
  "note": "Quatre des cinq majeurs viennent des corrections du tour 1.",
  "constats": [
   ("D4", "majeur", "Le total à payer",
    "La règle ne faisait qu'ajouter : « le plus grand de la paire » gagnait 6 fois sur 6 ; et le prix mal entendu se rejetait au bon sens (70 $ un sandwich).",
    "Deux lectures vraisemblables, et des items « tip included », « no tax » où l'erreur est d'ajouter."),
   ("D4/D3", "majeur", "L'allergie",
    "Trois saumons aux mêmes quatre choix : le troisième se déduisait des deux autres ; la série ne changeait jamais.",
    "Une banque qui couvre les quatre cases, trois réponses tirées par série."),
   ("E1/F1", "majeur", "Relance",
    "La clé acceptait « I'm from Quebec, thank you » comme une relance.",
    "La clôture refusée ; les formules de politesse entrent dans les réponses témoins."),
   ("E1", "majeur", "« Autre chose »",
    "« I'll take the salmon » était accepté sur l'item où commander le saumon est la faute éliminatoire.",
    "Le plat refusé nommé dans la consigne, une clé qui refuse le saumon."),
   ("A3", "majeur", "Lexique",
    "« the third floor » traduit « le troisième étage » contredisait le piège « first floor ».",
    "« le 3e étage (deux étages au-dessus de la rue) »."),
 ]},
 {"tour": 3, "commit": "ec6f39701", "compte": (0, 6, 10),
  "note": "Les six majeurs naissent tous du tour 2.",
  "constats": [
   ("E1", "majeur", "Relance",
    "La liste noire fuyait (« Nice meeting you », « I'll call you » passaient).",
    "Une liste blanche des mots qui précèdent un « you » nu."),
   ("E1", "majeur", "« Anything else? »",
    "Exclure par une liste d'aliments refusait les vraies réponses (« Just the coffee, thanks »).",
    "Reconnaître une commande en plus par sa forme."),
   ("E1/D2", "majeur", "Noix et arachides",
    "La clé acceptait « I'm allergic to peanuts » pour les noix, que la série du marché distingue ; les négations passaient.",
    "Arachide retirée de la clé des noix, négations et affirmations refusées."),
   ("D3/D1", "majeur", "L'allergie, marché",
    "La seule question où l'on décide revenait toujours à « on n'en prend pas » : seulement le geste prudent.",
    "Un second marché où l'on PEUT en prendre ; un des deux tiré par série ; deux saumons par case."),
   ("D2", "majeur", "Sons",
    "La voix de la serveuse faisait entendre « knots » pour « nuts », le mot de l'allergène.",
    "« pecans », que la retranscription rend juste ; chaque son neuf vérifié avant de commiter."),
   ("D4", "mineur", "Nombres",
    "Un nombre composé (« seventy-five ») exclut la lecture en -teen : le carré tombait à deux choix.",
    "Nombres simples (« seventy forty »)."),
 ]},
 {"tour": 4, "commit": "acb701b58", "compte": (0, 1, 8),
  "note": "Aucune stratégie aveugle ne dépasse plus le hasard.",
  "constats": [
   ("E1/E2", "majeur", "Je le dis, les gardes",
    "Une clé qui refuse une faute comptait comme « la moitié » : qui commandait le saumon douteux lisait « Presque. Il manque : I'll ».",
    "Une garde se reconnaît par programme (vraie sur la phrase vide) et passe d'abord, avec un message propre à l'item."),
 ]},
 {"tour": 5, "commit": "7a4a18570", "compte": (0, 2, 3),
  "note": "Les deux majeurs naissent du tour 4.",
  "constats": [
   ("E1/G2", "majeur", "Je le dis",
    "Après une garde ratée, ni le modèle ni « Suivant » ne s'ouvraient : une impasse sur 14 fautes sur 14.",
    "La branche de garde finit comme les autres : le modèle au 2e essai, puis « Suivant »."),
   ("E1", "majeur", "Le saumon",
    "« Instead of the salmon, I'll have the chicken » était accusé de la faute éliminatoire.",
    "Clé élargie (instead of, rather than, forget) ; plus aucune phrase juste accusée."),
 ]},
 {"tour": 6, "commit": "vérification", "compte": (0, 0, 6),
  "note": "Sortie de boucle : 231 essais au micro sans impasse, aucune faute éliminatoire acceptée, aucune stratégie aveugle au-dessus du hasard.",
  "constats": [
   ("D4", "mineur", "Restes consignés",
    "Quelques tournures improbables au restaurant (« Not the pasta, the salmon » accepté ; « no fish for me » refusé) ; les faux amis gardent un léger avantage par convergence (0,43 contre 0,33).",
    "Consignés, sans correction."),
 ]},
]

# ── La semaine jouée (étape 5) : cinq tours, 1er oct. 2026.
TOURS_JEU = [
 {"tour": 1, "commit": "ac9c70f79", "compte": (2, 7, 12),
  "note": "13 conversations réelles sur un serveur jetable, et un parcours dans la page à 375 px.",
  "constats": [
   ("A3/F1", "bloquant", "Le français",
    "Une situation jouée entièrement en français gagnait la carte : la personne « comprenait un peu ».",
    "La personne ne parle pas français (« Sorry, I don't speak French! ») ; une réplique en français ne compte pour aucun geste."),
   ("F1/E2", "bloquant", "L'allergie au restaurant",
    "L'éliminatoire se contournait : la serveuse avertissait d'elle-même et refusait la tarte aux amandes.",
    "Elle ne parle d'allergène que si on le demande et prend la commande telle quelle ; demander le plat douteux est éliminatoire, même repris."),
   ("E1/F1", "majeur", "Le bilan",
    "Des gestes cochés sans preuve, ou faits par la personne (Marcus épelait le nom à la place du touriste).",
    "Un geste ne compte que fait par le touriste, en anglais ; la page exige chaque geste coché pour donner la carte."),
   ("A3", "majeur", "Alignement",
    "L'objectif de l'allergie nommait aussi le marché ; Maya ne demandait qu'une question, l'objectif deux.",
    "Les arachides au marché, avec leur éliminatoire ; deux relances pour Maya."),
 ]},
 {"tour": 2, "commit": "60d4853a8", "compte": (1, 4, 11),
  "note": "Le modèle ne suit pas toutes les consignes : ce qui se compte passe dans la page.",
  "constats": [
   ("A3/F1", "bloquant", "Maya",
    "Jamais réussie : le modèle exigeait qu'on ait répondu à TOUTES ses questions, alors qu'elle en pose une à chaque réplique.",
    "Les relances comptées par la page ; le modèle ne juge plus que la réponse en anglais."),
   ("E1", "majeur", "Corrections",
    "Des phrases justes « corrigées » à l'identique ou réécrites (« OK bye » → « I haven't eaten yet… »).",
    "La page écarte les corrections identiques ou qui réécrivent au lieu de corriger."),
   ("B3", "majeur", "Accords",
    "« Vous vous êtes débrouillé » sans genre choisi.",
    "Un second tirage du bilan quand un accord masculin paraît sans genre choisi."),
   ("O3/E1", "majeur", "Le marché",
    "La formule « I'm allergic to nuts » proposée là où il s'agit d'arachides.",
    "Formule et règle de l'éliminatoire propres à chaque lieu."),
 ]},
 {"tour": 3, "commit": "8c1da619c", "compte": (1, 4, 7),
  "note": "Le défaut le plus grave naît de la correction du tour 2.",
  "constats": [
   ("F1", "bloquant", "Maya",
    "Deviner une question à sa forme comptait « Yes I do, thank you » et ratait « you like poutine ».",
    "Le bilan CITE les questions du touriste ; la page vérifie chaque citation, écarte clarifications et politesses, puis compte."),
   ("E1", "majeur", "Corrections",
    "« I am allergy at the peanuts → I'm allergic to peanuts », la correction la plus utile, était jetée.",
    "Comparaison sur les mots pleins, contractions dépliées."),
   ("E1/D2", "majeur", "Lieu éliminatoire raté",
    "Le bilan peaufinait la commande du plat dangereux (« I'll have the salmon, please »).",
    "Rien ne corrige la phrase qui commande le produit dangereux."),
 ]},
 {"tour": 4, "commit": "0f703c39d", "compte": (1, 2, 7),
  "note": "Rejoué sur les six conversations de Maya enregistrées par l'auditeur avant de commiter.",
  "constats": [
   ("F1/E1", "bloquant", "Maya",
    "« And you? » dit deux fois ne comptait qu'une fois : qui ne connaissait que cette formule ne pouvait jamais réussir.",
    "On compte les répliques qui relancent ; une citation courte ne vaut qu'en fin de réplique, jamais après « thank you »."),
   ("F1/E2", "majeur", "Maya",
    "« Réussie » sans avoir répondu à une seule question.",
    "La page vérifie qu'il y a une vraie réponse en anglais."),
   ("E1", "majeur", "Bilan de Maya",
    "Retirer toute phrase contenant « question » vidait le résumé et le conseil.",
    "Seules les phrases qui chiffrent les questions sont retirées."),
 ]},
 {"tour": 5, "commit": "60bba6dce", "compte": (0, 2, 6),
  "note": "Sortie de boucle, vérifiée avec les batteries de l'auditeur : 62 répliques sur 63 jugées comme attendu (l'écart est une attente contradictoire), 19 commandes sur 19, toutes les conversations rejugées.",
  "constats": [
   ("F1/E1", "majeur", "Maya",
    "« Quebec. », « Yes. », « No, first time. » ne comptaient pas comme réponses : les élèves les plus faibles échouaient.",
    "Une réponse brève en anglais est une réponse ; seules les clarifications, saluts et politesses n'en sont pas."),
   ("E1/A3", "majeur", "Le plat dangereux",
    "« The salmon, please » échappait au filtre, alors que « I will start with the soup » était jeté (« start » contient « tart »).",
    "Le produit en mots entiers, dans une réplique qui n'est ni une question ni un refus."),
 ]},
 {"tour": "6 · sortie", "commit": "vérification", "compte": (0, 0, 6),
  "note": "Les corrections du tour 5 vérifiées avec les batteries que l'auditeur avait écrites pour son tour 6 : la boucle est fermée.",
  "constats": [
   ("E1", "mineur", "Restes consignés",
    "Le bilan reformule encore parfois une formule juste (« Bye » → « Bye, see you later ») ; le modèle peut louer « de bonnes questions » quand la page refuse faute de réponse ; à la pharmacie, la posologie arrive parfois dans la réplique de clôture.",
    "Consignés, sans correction ; à observer au pilote."),
 ]},
]


def main():
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Toronto — la boucle didactique</title>", tete)
    tete = tete.replace("</head>", """<style>
.cst{background:var(--card);border:1px solid var(--line);border-radius:3px;padding:14px 16px;margin:10px 0}
.cst .t{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.cst .g-bloquant{color:#B91C1C}.cst .g-majeur{color:#8A5206}.cst .g-mineur{color:var(--muted)}
.cst p{margin:6px 0 0} h3.tour{font-size:20px;margin:28px 0 6px} .partie{margin-top:46px;padding-top:10px;border-top:3px solid var(--ink,#222)}
.sommaire a{display:inline-block;margin:4px 10px 4px 0}.cst .fait{border-left:3px solid #0A8F5B;padding-left:10px}
ol.chaine li{margin:6px 0}
</style>
</head>""")
    def rendre(liste):
      tours = ""
      for t in liste:
        b, m, n = t["compte"]
        items = "".join(
            f'<div class="cst"><div class="t"><span class="g-{g}">{E(g)}</span> · {E(c)} · {E(o)}</div>'
            f'<p>{E(k)}</p><p class="fait"><b>Corrigé.</b> {E(f)}</p></div>' for c, g, o, k, f in t["constats"])
        tours += f"""<section><h3 class="tour">Tour {t['tour']}</h3>
  <div class="chiffres"><div class="ch"><span class="n">{b}</span><span class="q">bloquant{'s' if b > 1 else ''}</span></div>
  <div class="ch"><span class="n">{m}</span><span class="q">majeur{'s' if m > 1 else ''}</span></div><div class="ch"><span class="n">{n}</span><span class="q">mineurs</span></div></div>
  <p style="margin-top:12px">{E(t['note'])}</p>{items}</section>"""
      return tours
    suite_de = lambda L: " → ".join(f"{b}/{m}/{n}" for b, m, n in (t["compte"] for t in L))
    suite = suite_de(TOURS)
    tours = rendre(TOURS)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Une semaine à Toronto &middot; qualité</p>
<h1>La boucle didactique d'« Une semaine à Toronto »</h1>
<p class="chapeau">Trois boucles, un regard extérieur à chaque tour, jusqu'à zéro bloquant et zéro majeur.</p>
<p class="sommaire"><a href="#prep">« Avant de partir » — {E(suite)}</a><a href="#exos">Les exercices — {E(suite_de(TOURS_EXOS))}</a><a href="#jeu">La semaine jouée — {E(suite_de(TOURS_JEU))}</a></p>
<h2 class="partie" id="prep">1. « Avant de partir »</h2>
<p class="chapeau">Les huit séances et le test « Prêt à partir ? », passés à la grille de 23 critères par un regard qui ne les a
pas écrits, six fois. Bloquants / majeurs / mineurs : <b>{suite}</b>, puis zéro bloquant et zéro majeur, confirmés par
47 réponses témoins rejouées dans la page. Ce que la boucle ne vérifie pas : l'exactitude de l'anglais (à faire relire par
une personne anglophone du Canada), et l'essai auprès de vrais touristes — cinq personnes qui pensent à voix haute,
avant toute diffusion.</p>

<section class="premier">
  <h2>Ce que la boucle a appris : chaque parade crée la devinette suivante</h2>
  <p>Un faux débutant qui obtient « Solide » au test peut sauter les séances. Il fallait donc que le test ne se réussisse
  pas sans écouter. Quatre tours de suite, la correction d'un tour a ouvert le défaut du suivant :</p>
  <ol class="chaine">
    <li>la bonne réponse était <b>la plus longue</b> → on fait porter le leurre par deux mauvais choix ;</li>
    <li>la bonne devient <b>l'exception</b>, seule de son côté → carré complet à quatre choix, mélange à graine fixe ;</li>
    <li>la graine met la bonne <b>au même bouton</b> → on pose les places dans les données ;</li>
    <li>les places <b>se déduisent</b> de celles déjà montrées → tirage au hasard à chaque affichage.</li>
  </ol>
  <p>Ce qui ferme la famille : des choix de même longueur, un carré complet quand deux traits décident, et la place tirée au
  hasard. La leçon est entrée dans la méthode de la boucle pour les trousses suivantes.</p>
</section>
{tours}

<h2 class="partie" id="exos">2. Les exercices</h2>
<p class="chapeau">Neuf familles, passées six fois : chaque série jouée par script, les stratégies qui répondent sans écouter
calculées contre le hasard, les clés du micro rejouées dans la page sur des centaines de phrases. Bloquants / majeurs /
mineurs : <b>{E(suite_de(TOURS_EXOS))}</b>.</p>
<section class="premier"><h2>Ce que la boucle a appris</h2>
  <ol class="chaine">
    <li><b>Une règle qui ne fait qu'ajouter se juge sans calcul</b> : le total le plus grand gagnait ; il a fallu des items où l'erreur est d'ajouter.</li>
    <li><b>Une liste noire fuit, une liste d'exclusion refuse le juste</b> : les clés du micro se sont fermées par la forme de la phrase, éprouvées sur des batteries.</li>
    <li><b>Une garde qui refuse une faute doit avoir son propre message</b>, et finir comme les autres : sinon elle accuse ou enferme.</li>
    <li><b>Un son se vérifie avant de partir</b> : la retranscription a trouvé « knots » pour « nuts », le mot de l'allergène.</li>
  </ol></section>
{rendre(TOURS_EXOS)}

<h2 class="partie" id="jeu">3. La semaine jouée</h2>
<p class="chapeau">Dix lieux et Maya, avec l'assistance qui joue les gens de Toronto. Cinq tours, des conversations réelles sur un
serveur jetable (jamais la production), les logiques de la page rejouées hors ligne. Bloquants / majeurs / mineurs :
<b>{E(suite_de(TOURS_JEU))}</b>.</p>
<section class="premier"><h2>Ce que la boucle a appris</h2>
  <ol class="chaine">
    <li><b>La personne ne parle pas la langue de l'apprenant</b>, et ne fait jamais sa part (épeler, avertir, signaler l'erreur).</li>
    <li><b>Ce qui se compte se compte dans la page</b>, pas par le modèle : chaque geste coché, les relances de Maya.</li>
    <li><b>Chaque règle écrite pour juger à la place du modèle a produit le défaut inverse au tour suivant</b> : trop large, puis trop étroite.
      Ce qui a fermé la boucle : faire CITER le modèle, vérifier la citation, et des batteries de phrases au verdict écrit d'avance, rejouées avant chaque commit.</li>
  </ol></section>
{rendre(TOURS_JEU)}
<div class="pied"><p>Produit par <code>build/toronto_audit.py</code> — ne pas l'éditer. Contenu audité :
<code>build/contenu/toronto/preparation.py</code>, <code>exercices.py</code>, <code>jeu_de_role.py</code> ; moteur : <code>build/toronto_app.py</code>.
Restent hors de portée de la boucle : l'exactitude de l'anglais (relecteur canadien) et l'essai auprès de vrais touristes (le pilote).</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), "—", suite)


if __name__ == "__main__":
    main()
