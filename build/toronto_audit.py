#!/usr/bin/env python3
"""Le journal de la boucle didactique d'« Une semaine à Toronto » — l'étape 1, « Avant de partir ».

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


def main():
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Toronto — la boucle didactique</title>", tete)
    tete = tete.replace("</head>", """<style>
.cst{background:var(--card);border:1px solid var(--line);border-radius:3px;padding:14px 16px;margin:10px 0}
.cst .t{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.cst .g-bloquant{color:#B91C1C}.cst .g-majeur{color:#8A5206}.cst .g-mineur{color:var(--muted)}
.cst p{margin:6px 0 0}.cst .fait{border-left:3px solid #0A8F5B;padding-left:10px}
ol.chaine li{margin:6px 0}
</style>
</head>""")
    tours = ""
    for t in TOURS:
        b, m, n = t["compte"]
        items = "".join(
            f'<div class="cst"><div class="t"><span class="g-{g}">{E(g)}</span> · {E(c)} · {E(o)}</div>'
            f'<p>{E(k)}</p><p class="fait"><b>Corrigé.</b> {E(f)}</p></div>' for c, g, o, k, f in t["constats"])
        tours += f"""<section><h2>Tour {t['tour']}</h2>
  <div class="chiffres"><div class="ch"><span class="n">{b}</span><span class="q">bloquant{'s' if b > 1 else ''}</span></div>
  <div class="ch"><span class="n">{m}</span><span class="q">majeur{'s' if m > 1 else ''}</span></div><div class="ch"><span class="n">{n}</span><span class="q">mineurs</span></div></div>
  <p style="margin-top:12px">{E(t['note'])}</p>{items}</section>"""
    suite = " → ".join(f"{b}/{m}/{n}" for b, m, n in (t["compte"] for t in TOURS))
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Une semaine à Toronto &middot; qualité</p>
<h1>La boucle didactique de « Avant de partir »</h1>
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
<div class="pied"><p>Produit par <code>build/toronto_audit.py</code> — ne pas l'éditer. Contenu audité :
<code>build/contenu/toronto/preparation.py</code> ; moteur : <code>build/toronto_app.py</code>.</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), "—", suite)


if __name__ == "__main__":
    main()
