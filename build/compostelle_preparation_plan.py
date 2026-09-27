#!/usr/bin/env python3
"""Le plan de « Avant de partir » — la préparation au voyage d'En route vers Compostelle.

    python3 build/compostelle_preparation_plan.py   # → assets/presentations/compostelle-preparation-plan.html

Demande de Daniel, 26 sept. 2026 : « il devrait y avoir, avant de partir, un
processus d'apprentissage d'un minimum de vocabulaire, d'utilisation d'un
verbe… une section préparation au voyage » ; et « un pèlerin fait 25 km par
jour : dix jours pour 775 km, ce n'est pas logique ». D'où deux chantiers sur
une page : huit séances à la maison avant le chemin, et les dix « journées »
rebaptisées haltes, avec les jours de marche qui les séparent.

Tout ce qui se compte est relu dans le contenu : les mots réemployés sont
vérifiés contre lexique.py (un identifiant inconnu arrête le build), les jours
de marche viennent des kilomètres d'etapes.py. La page finit par les décisions
à exporter.
"""
import html, json, math, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-preparation-plan.html"
E = html.escape
KM_PAR_JOUR = 25

# (n, titre, objectif visé, ce qu'on y apprend, tournures neuves à dire, mots du lexique réemployés, exercices, sons neufs estimés)
SEANCES = [
    (1, "Les sons de l'espagnol", "P1",
     "Les cinq voyelles toujours pleines ; le j et le g doux (<i>jamón, gente</i>) ; le ll et le y (<i>calle</i>) ; le ñ (<i>España</i>) ; "
     "le r roulé et le rr ; le z et le c doux à la castillane ; l'accent tonique et sa marque écrite.",
     ["Me llamo…", "España", "Galicia"],
     ["jamon", "llevar:lleva", "queso", "ducha", "almohada", "manana", "zumo", "cerrado", "iglesia", "vino"],
     "Écouter–répéter par paires (<i>pero / perro</i>), lire un mot à voix haute (micro es-ES), trouver la syllabe forte.", 24),
    (2, "Saluer, remercier, faire répéter", "P1",
     "Les formules qui ouvrent toutes les portes, et celles qui sauvent quand on ne comprend pas.",
     ["Hola, buenos días.", "Muchas gracias.", "¿Puede repetir, por favor?", "Más despacio, por favor."],
     ["buenos_dias", "buenas_tardes", "buenas_noches", "buen_camino", "vale", "perdone", "no_entiendo", "despacio",
      "repetir", "como_se_dice", "lo_siento", "de_nada"],
     "Qui dit quoi, et à quel moment de la journée ; « Je le dis » au micro ; réagir à une phrase dite trop vite.", 14),
    (3, "Les nombres et les prix", "P2",
     "De 1 à 100, puis les prix en euros tels qu'on les dit (<i>cuatro con cincuenta</i>) ; les pièges d'oreille (<i>seis / siete, "
     "trece / treinta</i>).",
     ["¿Cuánto es?", "Son doce euros.", "¿Puedo pagar con tarjeta?"],
     ["cuanto", "efectivo", "tarjeta", "cajero", "kilo", "cuenta", "propina"],
     "Prix entendu, quatre choix construits autour d'un leurre d'oreille ; dicter un prix ; payer au comptoir.", 30),
    (4, "L'heure et les jours", "P2",
     "Dire et comprendre l'heure (<i>a las ocho y media</i>), la journée espagnole (déjeuner tardif, siesta, souper à 21 h), les jours de la semaine.",
     ["¿A qué hora abre?", "Mañana a las siete.", "Hoy es domingo."],
     ["a_que_hora", "abierto", "cerrado", "manana", "por_la_tarde", "por_la_noche", "siesta",
      "hora_siete", "hora_ocho_media", "hora_diez", "hora_dos", "horario"],
     "Horloge entendue ; horaire d'une albergue à comprendre ; « ouvert ou fermé ? » à une heure donnée.", 22),
    (5, "Quatre verbes qui font presque tout", "P3",
     "<b>Quisiera</b> (je voudrais) · <b>¿Tiene…?</b> (avez-vous… ?) · <b>Necesito</b> (j'ai besoin de) · <b>Me duele</b> (j'ai mal à). "
     "Une mécanique à la fois, jamais la conjugaison entière : la forme qui sert, et une seule variante (<i>me duelen los pies</i>).",
     ["Quisiera una cama.", "¿Tiene agua?", "Necesito una farmacia.", "Me duele la rodilla."],
     ["litera", "agua", "farmacia", "tirita", "ampolla", "rodilla", "pie", "espalda", "me_duele", "ibuprofeno", "cafe_leche", "bocadillo"],
     "Construire la phrase avec des tuiles, puis la dire ; même besoin, quatre situations (albergue, bar, pharmacie, épicerie).", 26),
    (6, "Poser une question", "P3",
     "<b>¿Dónde está…?</b> · <b>¿Cuánto cuesta?</b> · <b>¿A qué hora…?</b> · <b>¿Hay…?</b> (y a-t-il ?) — et l'intonation qui monte.",
     ["¿Dónde está el albergue?", "¿Hay una farmacia cerca?", "¿Quedan camas?"],
     ["albergue", "farmacia", "supermercado", "panaderia", "parada", "quedan", "fuente", "iglesia", "ducha", "enchufe"],
     "Quelle question pour obtenir quoi ; dire la question ; entendre qu'on vous la pose.", 20),
    (7, "Parler de soi", "P4",
     "Se présenter en trois phrases : d'où l'on vient, pourquoi l'on marche, son allergie. Pèlerin ou pèlerine : l'accord se fait tout seul.",
     ["Soy de Quebec, en Canadá.", "Hago el Camino por…", "Soy alérgico / alérgica a…"],
     ["soy_de", "de_donde", "por_que", "desde_donde", "encantado", "alergico", "cansado", "peregrino"],
     "Composer sa présentation (elle rejoint la trousse, « Me présenter ») ; la dire ; répondre à « ¿De dónde eres? ».", 18),
    (8, "Comprendre la réponse", "P5",
     "Le plus dur n'est pas de demander, c'est d'entendre la réponse : <i>sí / no, hay / no hay, está completo, a la derecha, todo recto, "
     "lleva / no lleva</i>.",
     ["—", "(on n'y dit rien : on écoute)"],
     ["completo", "izquierda", "derecha", "recto", "lleva", "cruce", "subida", "bajada", "arriba", "abajo"],
     "Réponses dites vite, à la vitesse d'Espagne : que faut-il faire ? — la famille « Ce qu'on me répond », en version courte.", 24),
]

OBJECTIFS = [
    ("P1", "Dire lisiblement les formules et les mots du chemin", "au micro, sans modèle sous les yeux",
     "reconnus par la reconnaissance vocale espagnole au premier ou au deuxième essai, pour 8 sur 10"),
    ("P2", "Comprendre un prix ou une heure", "dits à vitesse normale, une seule écoute",
     "8 sur 10, sans confondre les paires d'oreille"),
    ("P3", "Formuler une demande ou une question", "dans une situation nouvelle, avec quisiera, ¿tiene…?, necesito, me duele, ¿dónde está…?, ¿hay…?",
     "4 sur 5 dites et comprises"),
    ("P4", "Se présenter", "en trois phrases, au bon genre, allergie comprise",
     "les trois dites sans aide"),
    ("P5", "Comprendre une réponse courte", "oui / non, il y en a / il n'y en a pas, complet, gauche / droite / tout droit, ça en contient",
     "8 sur 10"),
]

DECISIONS = [
    ("nom", "Comment appeler les dix étapes de l'application ?",
     [("haltes", "« Halte 4 · Logroño »", False), ("etapes", "« Étape 4 · Logroño »", True), ("jours", "Garder « Jour 4 »", False)],
     "Halte dit juste : un lieu où l'on s'arrête, pas un jour de marche. « Étape » prête à la même confusion que « jour » : "
     "sur le Camino, une étape, c'est une journée de marche. — Révisé le 27 sept. 2026 : « étape », à la demande de Daniel ; "
     "l'ambiguïté se lève en disant « dix étapes choisies » sur une trentaine."),
    ("marche", "Afficher les jours de marche entre deux étapes ?",
     [("oui", "Oui : « 3 jours de marche jusqu'à Logroño »", True), ("non", "Non", False)],
     "C'est ce qui rend les 775 km lisibles : 10 étapes, mais environ {jours} jours de marche."),
    ("verrou", "La préparation doit-elle être faite avant d'ouvrir le chemin ?",
     [("conseillee", "Conseillée, jamais verrouillée", True), ("obligatoire", "Obligatoire", False)],
     "Un pèlerin qui parle déjà un peu l'espagnol ne doit pas être retenu à la maison. L'accueil propose d'abord la préparation ; "
     "le test « Prêt à partir ? » dit où il en est."),
    ("format", "Le format des séances",
     [("huit", "8 séances de 15 minutes", True), ("cinq", "5 séances de 25 minutes", False)],
     "Quinze minutes tiennent dans une pause ; huit séances sur deux à quatre semaines laissent le temps d'oublier et de revoir."),
    ("grammaire", "Expliquer la grammaire ?",
     [("mecanique", "Un encadré « la mécanique » par séance, la seule forme qui sert", True),
      ("aucune", "Aucune explication : des phrases toutes faites", False),
      ("tableaux", "Les conjugaisons complètes", False)],
     "Vous le demandiez : « l'utilisation d'un verbe ». Une forme à la fois (quisiera, me duele) suffit au chemin ; les tableaux "
     "complets découragent un débutant de 60 ans."),
    ("test", "Un test « Prêt à partir ? » à la fin de la préparation ?",
     [("oui", "Oui : il situe, il ne verrouille pas", True), ("non", "Non", False)],
     "Même règle que « Suis-je prêt ? » : des phrases nouvelles, deux formes, trois verdicts (Solide · En route · À reprendre)."),
    ("marcher", "Un petit exercice « En marchant », cinq minutes par jour de marche ?",
     [("apres", "Plus tard, après le pilote", True), ("maintenant", "Maintenant, avec la préparation", False), ("non", "Non", False)],
     "Il donnerait la continuité des 33 jours sans contenu neuf (il reprend les mots vus). Mais c'est le pilote qui dira si les "
     "pèlerins ouvrent l'application pendant la marche."),
    ("prix", "La préparation dans la vente",
     [("gratuite", "Gratuite, comme le chemin", True), ("payante", "Comprise dans l'accès payant", False)],
     "Elle attire sans rien coûter (aucune IA) ; ce qui se paie reste la conversation."),
]


def main():
    ET, LX = C.charger("etapes"), C.charger("lexique")
    ids = {e[0] for e in LX.LEXIQUE}
    es = {e[0]: e[2] for e in LX.LEXIQUE}
    mots = []
    for s in SEANCES:
        propres = [m.split(":")[-1] for m in s[5]]
        inconnus = [m for m in propres if m not in ids]
        if inconnus:
            raise SystemExit(f"séance {s[0]} : mots absents du lexique : {inconnus}")
        mots.append(propres)
    reemplois = len({m for l in mots for m in l})
    sons = sum(s[7] for s in SEANCES) + 30

    etapes = ET.ETAPES
    prec, lignes, total = 0, [], 0
    for e in etapes:
        j = max(1, math.ceil((e["km"] - prec) / KM_PAR_JOUR - 0.2))
        total += j
        lignes.append((e, j, e["km"] - prec))
        prec = e["km"]

    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — avant de partir</title>", tete)
    tete = tete.replace("</head>", """<style>
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
.deux-temps{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.temps{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.temps h3{margin:0 0 4px}.temps .q{color:var(--muted);font-size:14px;margin:0 0 8px}
.temps.avant{border-top:5px solid #F2C230}.temps.chemin{border-top:5px solid #1F4E9C}
.seance{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:10px 0}
.seance h3{margin:0 0 4px;display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
.seance h3 .n{display:inline-grid;place-items:center;width:28px;height:28px;border-radius:50%;background:#F2C230;color:#13233B;font-size:14px;flex:none}
.seance h3 .obj{font-size:12px;font-weight:900;color:var(--acier);background:var(--acier-bg);border-radius:99px;padding:2px 9px}
.seance p{margin:6px 0;font-size:15px}
.seance .dire{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}
.seance .dire span{background:#FFF6D6;color:#4A3A0A;border-radius:8px;padding:3px 9px;font-size:14px;font-weight:700}
.seance .mots{font-size:13.5px;color:var(--muted)}
.frise-marche{list-style:none;padding:0;margin:8px 0}
.frise-marche li{display:grid;grid-template-columns:130px minmax(0,1fr);gap:10px;align-items:center;padding:6px 0;border-bottom:1px dashed var(--line)}
.frise-marche .jm{font-size:13px;color:var(--muted)}
.frise-marche .barre{height:10px;border-radius:99px;background:repeating-linear-gradient(90deg,#1F4E9C 0 12px,transparent 12px 16px)}
.dec{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;margin:10px 0}
.dec h3{margin:0 0 8px;font-size:16.5px}
.dec .opts{display:flex;flex-wrap:wrap;gap:8px}
.dec label{display:flex;gap:7px;align-items:center;border:1px solid var(--line-fort);border-radius:10px;padding:8px 12px;cursor:pointer;font-size:14.5px}
.dec label.reco{border-color:var(--fait)}
.dec label small{font-size:11px;font-weight:900;color:var(--fait);text-transform:uppercase;letter-spacing:.05em}
.dec p{margin:8px 0 0;font-size:14px;color:var(--muted)}
textarea.note{width:100%;min-height:90px;font:inherit;border:1px solid var(--line-fort);border-radius:10px;padding:10px;background:var(--card);color:var(--body)}
.exporter{margin-top:10px;font:inherit;font-weight:800;background:#0A8F5B;color:#fff;border:0;border-radius:10px;padding:11px 18px;cursor:pointer}
pre.json{white-space:pre-wrap;background:var(--sunken);border-radius:10px;padding:12px;font-size:13px}
@media (max-width:760px){.deux-temps{grid-template-columns:1fr}.frise-marche li{grid-template-columns:1fr}}
</style>
</head>""")

    seances = "".join(
        f'<div class="seance"><h3><span class="n">{n}</span>{E(t)} <span class="obj">{o}</span></h3>'
        f'<p>{quoi}</p>'
        f'<div class="dire">{"".join(f"<span lang=es>{E(x)}</span>" for x in dire)}</div>'
        f'<p><b>On y fait :</b> {ex}</p>'
        f'<p class="mots">Mots du lexique réemployés ({len(mots[n - 1])}) : '
        + ", ".join(f"<i lang=es>{E(es[m])}</i>" for m in mots[n - 1]) + "</p></div>"
        for (n, t, o, quoi, dire, _m, ex, _s) in SEANCES)
    objectifs = "".join(f"<tr><td><b>{k}</b></td><td>{E(v)}</td><td>{E(c)}</td><td>{E(cr)}</td>"
                        f"<td>{', '.join(str(s[0]) for s in SEANCES if s[2] == k)}</td></tr>" for k, v, c, cr in OBJECTIFS)
    frise = "".join(
        f'<li><div><b>Étape {e["n"]}</b> · {E(e["lieu"])}<div class="jm">km {e["km"]} · {j} jour{"s" if j > 1 else ""} de marche depuis '
        f'{"Saint-Jean" if i == 0 else E(lignes[i - 1][0]["lieu"])}</div></div>'
        f'<div class="barre" style="width:{min(100, 100 * j / 7):.0f}%" aria-hidden="true"></div></li>'
        for i, (e, j, km) in enumerate(lignes))
    decisions = "".join(
        f'<div class="dec" data-cle="{k}"><h3>{E(q)}</h3><div class="opts">'
        + "".join(f'<label class="{"reco" if r else ""}"><input type="radio" name="{k}" value="{v}"{" checked" if r else ""}>'
                  f'{E(t)}{" <small>recommandé</small>" if r else ""}</label>' for v, t, r in opts)
        + f'</div><p>{E(pq.format(jours=total))}</p></div>' for k, q, opts, pq in DECISIONS)

    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; « Avant de partir » : le plan</h1>
<p class="chapeau">Deux constats de votre relecture. <strong>Il manque une préparation</strong> : l'application jette le pèlerin à
Roncesvalles sans lui avoir appris à prononcer, à entendre un prix, ni les quelques tournures qui servent partout. Et <strong>dix
« journées » pour 775 km, ce n'est pas crédible</strong> : à {KM_PAR_JOUR} km par jour, le Camino francés prend environ {total} jours.
Ce plan propose deux temps — la maison, puis le chemin — et rebaptise les journées en haltes. Rien n'est encore écrit : les choix sont au bas de la page.</p>
<div class="maj" style="background:#FBEFC4;border:1px solid #E7C75A;border-radius:12px;padding:12px 16px;margin:14px 0;font-size:15px">
<b>Mise à jour du 27 septembre 2026 — ce plan est réalisé, avec trois changements de vocabulaire.</b>
Les séances s'appellent <b>entraînements</b> (on prépare son sac, chacun y met un objet) ; les haltes s'appellent <b>étapes</b>
(« dix étapes choisies » sur une trentaine, une tous les trois jours de marche) ; chaque entraînement commence par une <b>leçon narrée</b>.
Plus bas, le texte suit ce vocabulaire ; la décision sur le nom est gardée telle qu'elle a été prise, avec sa révision.</div>

<section class="premier">
  <h2>Deux temps</h2>
  <div class="deux-temps">
    <div class="temps avant"><h3>Avant de partir</h3><p class="q">À la maison · deux à quatre semaines · gratuit</p>
      <p>Huit entraînements de quinze minutes : les sons, la politesse, les nombres, l'heure, quatre verbes, les questions, se présenter,
      comprendre la réponse. Un test « Prêt à partir ? » pour finir.</p>
      <p style="font-size:14px;color:var(--muted);margin:0">On y apprend <b>les outils</b> ; on ne s'en sert pas encore en situation.</p></div>
    <div class="temps chemin"><h3>Sur le chemin</h3><p class="q">Les dix étapes · les scènes · Marta · « Parler librement »</p>
      <p>Ce qui existe aujourd'hui : chaque étape met les outils en situation (un lit, un comptoir, la pharmacie, l'allergie…), puis la
      conversation libre les exerce avec quelqu'un qui répond vraiment.</p>
      <p style="font-size:14px;color:var(--muted);margin:0">On y <b>réemploie</b> ; la trousse reste l'outil de secours.</p></div>
  </div>
</section>

<section>
  <h2>Ce que le pèlerin saura faire avant de partir</h2>
  <p>Cinq objectifs, chacun avec sa condition et son critère — c'est ce que le test « Prêt à partir ? » vérifiera.</p>
  <table class="cmp"><thead><tr><th></th><th>Objectif</th><th>Condition</th><th>Critère</th><th>Entraînements</th></tr></thead><tbody>{objectifs}</tbody></table>
</section>

<section>
  <h2>Les huit entraînements</h2>
  <p>Chaque entraînement suit le même ordre que les étapes : la leçon, j'écoute, je reconnais, je le dis. Un encadré « la mécanique » par entraînement
  explique la seule forme qui sert (décision 5). Les mots viennent du lexique existant : <b>{reemplois} mots déjà dessinés et
  enregistrés</b> sont réemployés.</p>
  {seances}
</section>

<section>
  <h2>Le chemin : dix étapes choisies, environ {total} jours de marche</h2>
  <p>Les dix étapes de l'application ne sont pas des jours : ce sont les <b>étapes choisies</b> où se joue une situation. Entre deux étapes,
  on marche — calculé ici à {KM_PAR_JOUR} km par jour, à partir des kilomètres de l'application.</p>
  <ol class="frise-marche">{frise}</ol>
  <p style="font-size:14.5px;color:var(--muted)">Faire les {total} étapes une à une n'apprendrait rien de plus : les situations se
  répéteraient (un lit, un repas, un lit, un repas), pour trois fois plus de contenu à écrire, enregistrer et faire relire.</p>
</section>

<section>
  <h2>Ce que ça demande</h2>
  <table class="cmp"><thead><tr><th>Poste</th><th>Estimation</th></tr></thead><tbody>
    <tr><td>Écriture (huit entraînements, le test, le renommage)</td><td>deux à trois séances de travail</td></tr>
    <tr><td>Sons neufs (Azure, voix d'Espagne)</td><td>environ {sons}, soit moins de 1 $</td></tr>
    <tr><td>Dessins neufs</td><td>presque aucun : les mots sont déjà illustrés ; quelques pictogrammes composés en HTML (horloges, prix)</td></tr>
    <tr><td>Boucle didactique</td><td>au moins trois tours, comme pour le chemin</td></tr>
    <tr><td>Relecture espagnole</td><td>à ajouter au lot déjà prévu (les tournures neuves)</td></tr>
  </tbody></table>
</section>

<section id="decisions">
  <h2>Vos décisions</h2>
  <p>Les recommandations sont cochées d'avance. Changez ce que vous voulez, ajoutez une note, puis exportez et collez le texte dans la conversation.</p>
  {decisions}
  <textarea class="note" id="note" placeholder="Ce qui manque, ce qui est de trop, un entraînement à changer…"></textarea>
  <button class="exporter" id="exp" type="button">Exporter mes décisions</button>
  <pre class="json" id="sortie" hidden></pre>
</section>
</div>
<script>
const CLE = 'compostelle-preparation:decisions';
function lire(){{ try {{ return JSON.parse(localStorage.getItem(CLE) || '{{}}'); }} catch (e) {{ return {{}}; }} }}
function ecrire(v){{ try {{ localStorage.setItem(CLE, JSON.stringify(v)); }} catch (e) {{}} }}
const etat = lire();
for (const [k, v] of Object.entries(etat.choix || {{}})) {{ const r = document.querySelector(`input[name="${{k}}"][value="${{v}}"]`); if (r) r.checked = true; }}
if (etat.note) document.getElementById('note').value = etat.note;
function releve(){{ const c = {{}}; document.querySelectorAll('.dec').forEach(d => {{ const r = d.querySelector('input:checked'); c[d.dataset.cle] = r ? r.value : null; }}); return c; }}
document.querySelectorAll('.dec input').forEach(r => r.addEventListener('change', () => {{ etat.choix = releve(); ecrire(etat); }}));
document.getElementById('note').addEventListener('input', e => {{ etat.note = e.target.value; ecrire(etat); }});
document.getElementById('exp').addEventListener('click', async () => {{
  const txt = JSON.stringify({{page: 'compostelle-preparation-plan', date: new Date().toLocaleDateString('fr-CA'),
    decisions: releve(), note: document.getElementById('note').value}}, null, 2);
  const s = document.getElementById('sortie'); s.textContent = txt; s.hidden = false;
  try {{ await navigator.clipboard.writeText(txt); document.getElementById('exp').textContent = 'Copié — collez-le dans la conversation'; }}
  catch (e) {{ document.getElementById('exp').textContent = 'Sélectionnez le texte ci-dessous et copiez-le'; }}
}});
</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {reemplois} mots réemployés, ~{sons} sons, {total} jours de marche")


if __name__ == "__main__":
    main()
