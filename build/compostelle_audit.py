#!/usr/bin/env python3
"""Le journal de la boucle didactique d'« En route vers Compostelle ».

    python3 build/compostelle_audit.py   # → assets/presentations/compostelle-audit.html

Chaque tour : l'audit d'un regard extérieur (sous-agent, grille de 23 critères
de la compétence boucle-didactique, page servie et jouée), puis la révision.
Chaque constat garde son code, sa gravité, et ce qui en a été fait — un
changement sans code serait un goût, pas une correction de la boucle.
"""
import html, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-audit.html"
E = html.escape

# (code, gravité, endroit, constat, ce qui a été fait, statut)
TOURS = [
 {"tour": 1, "date": "25 septembre 2026", "compte": (2, 8, 6),
  "note": "Audit de la version livrée le soir même : page servie à 375 et 1280 px, journée 7 jouée, arrêt éliminatoire vérifié.",
  "constats": [
   ("F1", "bloquant", "Test « Suis-je prêt ? »",
    "Chaque forme ne couvrait que la moitié des objectifs ; l'allergie n'y était pas, ou pas éliminatoire : « Solide » possible sans une question sur l'allergie.",
    "Test réécrit (test.py) : deux formes parallèles, les cinq objectifs dans chacune, deux items d'allergie éliminatoires (comprendre ET dire), règle affichée avant ; verdict « Pas encore prêt·e : l'allergie ».", "corrigé"),
   ("A3/F2", "bloquant", "León, poche",
    "Seule l'allergie aux noix se disait : un pèlerin allergique aux œufs ou aux fruits de mer finissait sans pouvoir dire la sienne.",
    "« Mon allergie » (8 allergènes) dans les réglages et la poche ; carte « Montrer » personnelle, avec sa voix ; la phrase dite à León est la sienne.", "corrigé"),
   ("D2", "majeur", "Scènes et soirs",
    "L'espagnol de la personne s'affichait dès qu'elle parlait : on réussissait en lisant, alors que l'écart est d'entendre.",
    "Écouter d'abord : le texte s'affiche après la réponse, ou avec « Lire » ; avant une réponse qui compte double, ni « Lire » ni « Français ».", "corrigé"),
   ("D1/A2", "majeur", "Je le dis",
    "Se sautait entièrement ; félicitait sans une phrase dite ; le tampon ne l'exigeait pas.",
    "Le modèle ne s'ouvre qu'après une tentative (micro ou « Je l'ai dit ») ; compte réel des phrases dites ; la moitié exigée ; le tampon exige « Je le dis ».", "corrigé"),
   ("F1", "majeur", "Test",
    "Les items du test étaient ceux de la pratique : il mesurait la mémoire, pas le transfert.",
    "Items inédits (mêmes structures, autres valeurs) ; la reprise prend l'autre forme.", "corrigé"),
   ("A1", "majeur", "Accueil, journées",
    "Ni les objectifs, ni l'erreur éliminatoire n'étaient annoncés.",
    "Un objectif en tête de chaque journée ; à l'accueil, « Au bout du chemin, vous saurez… » et la règle de l'allergie.", "corrigé"),
   ("D3", "majeur", "León, Puente la Reina, Logroño",
    "L'allergie, les directions, la posologie n'étaient pratiquées qu'une journée, sans contre-exemple.",
    "Entrelacés : « no lleva » à Pamplona (manger est la bonne réponse), « lleva nueces » à Sarria, une direction à Burgos et à O Cebreiro, une posologie à O Cebreiro ; l'allergie revient en rappel après León.", "corrigé"),
   ("F3/D1", "majeur", "Structure de la journée",
    "Aucun rappel des journées précédentes.",
    "« Ce qu'on me répond » s'ouvre sur deux rappels : la veille, et une journée plus ancienne (l'allergie après León). La reprise la veille du départ : le test, sur des items neufs.", "corrigé"),
   ("A3", "majeur", "O5 — parler de soi",
    "Se présenter, dire son métier, sa raison de marcher : seulement en choisissant une phrase écrite.",
    "Trois « Je le dis » personnels (d'où vous venez, ce que vous faites, pourquoi vous marchez) ; au test, une réponse à un pèlerin dans chaque forme.", "corrigé"),
   ("D4", "majeur", "León, reprise après l'arrêt",
    "La reprise remettait les choix dans le même ordre : on repassait de mémoire de position.",
    "Chaque arrêt change la graine de l'ordre de la scène.", "corrigé"),
   ("B1/C2", "mineur", "Le lieu",
    "~137 mots de tourisme par journée, sans lien avec un objectif ; la situation arrive tard.",
    "Conservé : le tourisme des étapes est une demande expresse de Daniel. L'objectif du jour s'affiche désormais avant.", "conservé"),
   ("E1", "mineur", "Test", "Après une erreur, seule la phrase ou l'explication générique.",
    "La rétroaction propre au choix fait s'affiche.", "corrigé"),
   ("E2", "mineur", "Scènes", "Une erreur de sens n'a pas de suite dans le dialogue.",
    "Reporté : demande une réplique de conséquence par erreur, donc de nouveaux sons.", "reporté"),
   ("D4", "mineur", "Distracteurs",
    "Des plaisanteries qu'aucun débutant ne choisirait (« en gallina », « nadar más »…).",
    "Cinq remplacés par de vraies erreurs de francophone (accord, ser, pluriel, « nada mucho »…).", "corrigé"),
   ("F2", "mineur", "Poche", "Seulement ce qu'on dit, jamais ce qu'on entendra en retour.",
    "Chaque rubrique d'étape a « Ce qu'on peut vous répondre », avec la voix.", "corrigé"),
   ("G1", "mineur", "Scènes, images",
    "Boutons de 32 px, textes de 12 px, images sans nom pour un lecteur d'écran.",
    "Boutons de 44 px, textes à 13,5 px au moins, images nommées par leur mot français.", "corrigé"),
  ]},
]


def main():
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — la boucle didactique</title>", tete)
    tete = tete.replace("</head>", """<style>
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
.cst{background:var(--card);border:1px solid var(--line);border-radius:3px;padding:14px 16px;margin:10px 0}
.cst .t{font-size:12px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.cst .g-bloquant{color:#B91C1C}.cst .g-majeur{color:#8A5206}.cst .g-mineur{color:var(--muted)}
.cst p{margin:6px 0 0}.cst .fait{border-left:3px solid #0A8F5B;padding-left:10px}
.cst .fait.reporté,.cst .fait.conservé{border-left-color:#D9880B}
</style>
</head>""")
    tours = ""
    for t in TOURS:
        b, m, n = t["compte"]
        items = "".join(
            f'<div class="cst"><div class="t"><span class="g-{g}">{E(g)}</span> · {E(c)} · {E(o)}</div>'
            f'<p>{E(k)}</p><p class="fait {E(st)}"><b>{E(st.capitalize())}.</b> {E(f)}</p></div>'
            for c, g, o, k, f, st in t["constats"])
        tours += f"""<section><h2>Tour {t['tour']} — {E(t['date'])}</h2>
  <div class="chiffres"><div class="ch"><span class="n">{b}</span><span class="q">bloquants</span></div>
  <div class="ch"><span class="n">{m}</span><span class="q">majeurs</span></div><div class="ch"><span class="n">{n}</span><span class="q">mineurs</span></div></div>
  <p style="margin-top:12px">{E(t['note'])}</p>{items}</section>"""
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">En route vers Compostelle &middot; qualité</p>
<h1>La boucle didactique</h1>
<p class="chapeau">L'application passée à la grille de 23 critères, par un regard qui ne l'a pas écrite : page servie, jouée,
mesurée au téléphone. Sortie de boucle : zéro bloquant, zéro majeur. Ce que la boucle ne vérifie pas : l'exactitude de l'espagnol
(relu à part), et l'essai auprès de vrais pèlerins — cinq personnes qui pensent à voix haute, avant toute diffusion.</p>
{tours}
<div class="pied"><p>Produit par <code>build/compostelle_audit.py</code> — ne pas l'éditer.</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE))


if __name__ == "__main__":
    main()
