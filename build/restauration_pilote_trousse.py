#!/usr/bin/env python3
"""La trousse du pilote RÉEL de Chez Jocelyne : décider, préparer, imprimer.

    python3 build/restauration_pilote_trousse.py             # la page + les documents + leurs PDF
    python3 build/restauration_pilote_trousse.py --sans-pdf

Copie de build/hotel_pilote_trousse.py, adaptée : un restaurant, UN groupe (la
cuisine et la salle mêlées), le français appris avec l'espagnol ou l'anglais en
appui, et l'allergie au premier plan — c'est la seule erreur éliminatoire.

Sorties (produites, jamais éditées) :
  assets/presentations/restauration/restauration-pilote-trousse.html    décisions à exporter, calendrier, liens
  assets/presentations/restauration/pilote-docs/*.html (+ .pdf)         à imprimer, noir et blanc, format lettre :
    lettre-restaurant     la proposition à la direction du restaurant
    participants-fr|es|en ce que chaque employé doit savoir (Loi 25), dans sa langue
    feuille-de-route      les deux séances, pour le formateur
    rapport-employeur     le gabarit du rapport, sans aucun nom

Le protocole (le pourquoi, les règles de décision, la grille) reste
restauration-pilote.html ; cette trousse-ci est le comment. Les valeurs propres au
restaurant partenaire vivent dans build/contenu/entreprise-restaurant/pilote.py.

Répétition générale du 30 sept. 2026, sur un serveur jetable : un groupe de niveau
3, une séance sur l'atelier 239, deux participants entrés par le code ; 16 réponses,
16 envois ; le direct montre le premier essai et « erreur grave » à l'allergie. Elle
a trouvé un défaut, corrigé : retirer le code de l'adresse coupait le lien au direct
au rechargement en séance.
"""
import html, importlib.util, json, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
PAGE = RACINE / "assets" / "presentations" / "restauration" / "restauration-pilote-trousse.html"
DOCS = RACINE / "assets" / "presentations" / "restauration" / "pilote-docs"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
POLICE = "../../../design-system/fonts/nunito-latin.woff2"
LETTRE = (612, 792)
PAGES_MAX = {"lettre-restaurant": 1, "participants-fr": 1, "participants-en": 1, "participants-es": 1,
             "feuille-de-route": 2, "rapport-employeur": 2}
COURRIEL = "confidentialite@edufrancis.ca"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


PI = _charger("pt_pilote", CONTENU / "pilote.py")
PX = _charger("pt_prix", CONTENU / "prix.py")
LX = _charger("pt_lexique", CONTENU / "lexique.py")
SI = _charger("pt_situations", CONTENU / "situations.py")
EX = _charger("pt_exercices", CONTENU / "exercices.py")
ID = _charger("pt_identite", CONTENU / "identite.py")


def v(x, largeur=14):
    """Une valeur, ou la ligne à remplir à la main."""
    return E(x) if x else f'<span class="blanc">{"&nbsp;" * largeur}</span>'


def verifier_minutes():
    src = (RACINE / "build" / "restauration_pilote.py").read_text(encoding="utf-8")
    protocole = [int(n) for n in re.findall(r'<td class="num">(\d+)</td>', src)[:8]]
    ici = [m for _, etapes in PI.SEANCES for _, m, _ in etapes]
    if protocole != ici:
        raise SystemExit(f"Les minutes divergent : protocole {protocole}, pilote.py {ici}")


CSS_DOC = """
@page { size: letter; margin: 16mm 17mm 15mm; }
*{box-sizing:border-box}
@font-face{font-family:'Nunito';src:url('@@POLICE@@') format('woff2');font-weight:400 800}
html,body{margin:0;background:#FFF;color:#000}
body{font-family:'Nunito',-apple-system,'Segoe UI',sans-serif;font-size:10.5pt;line-height:1.42}
.f{max-width:180mm;margin:0 auto}
.tete{display:flex;justify-content:space-between;align-items:flex-end;gap:12px;border-bottom:2pt solid #000;padding-bottom:6px;margin-bottom:12px}
.tete h1{font-size:16pt;font-weight:800;margin:0;line-height:1.1}
.tete .ou{font-size:8pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;text-align:right}
h2{font-size:9pt;font-weight:800;text-transform:uppercase;letter-spacing:.1em;margin:14px 0 5px;border-bottom:.6pt solid #999;padding-bottom:2px}
p{margin:0 0 7px}
ul,ol{margin:0 0 7px;padding-left:18px} li{margin:2px 0}
table{border-collapse:collapse;width:100%;margin:4px 0 8px}
th,td{border:.6pt solid #888;padding:4px 6px;text-align:left;vertical-align:top;font-size:9.6pt}
th{font-size:8pt;text-transform:uppercase;letter-spacing:.06em}
td.n{text-align:right;width:12mm;font-weight:800}
.case{display:inline-block;width:10px;height:10px;border:1pt solid #000;margin-right:6px;vertical-align:-1px}
.blanc{display:inline-block;border-bottom:.8pt solid #000;min-width:30mm}
.zone{border:.8pt solid #000;min-height:22mm;margin:4px 0 10px}
.zone.haute{min-height:34mm}
.encadre{border:1.4pt solid #000;padding:7px 10px;margin:10px 0;break-inside:avoid}
.saut{break-before:page}
.pied{margin-top:12px;border-top:.6pt solid #999;padding-top:5px;font-size:8pt;color:#333;display:flex;justify-content:space-between;gap:10px}
.sig{margin-top:18px}
@media screen{body{background:#EDEDEA;padding:20px 0}.f{background:#FFF;padding:16mm 17mm;box-shadow:0 1px 3px rgba(0,0,0,.2)}}
""".replace("@@POLICE@@", POLICE)


def doc(titre, ou, corps, lang="fr", pied="francis — formation au poste"):
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{E(titre)}</title>'
            f'<style>{CSS_DOC}</style></head><body><div class="f">'
            f'<div class="tete"><h1>{E(titre)}</h1><div class="ou">{ou}</div></div>{corps}'
            f'<div class="pied"><span>{E(pied)}</span><span>{E(ID.NOM)} · pilote</span></div></div></body></html>')


# ── Les documents ────────────────────────────────────────────────────────────

def lettre_restaurant():
    postes = PI.POSTES_TEXTE.get(PI.POSTES) or PI.POSTES_TEXTE["deux"]
    conditions = PI.CONDITIONS_TEXTE.get(PI.CONDITIONS)
    cond_html = (f"<p>{E(conditions)}</p>" if conditions else
                 '<p>Conditions : <span class="blanc" style="min-width:120mm">&nbsp;</span></p>')
    sits = " · ".join(dict.fromkeys(s[5].rstrip(".").lower() for s in SI.SITUATIONS))
    corps = f"""
<p>À l'attention de : {v(PI.CONTACT, 40)}<br>{v(PI.RESTAURANT, 40)}{(", " + E(PI.VILLE)) if PI.VILLE else ""}</p>
<p><b>Objet : un pilote de formation en français pour vos employés de cuisine et de salle</b></p>
<p>Madame, Monsieur,</p>
<p>Nous avons conçu une formation courte pour les employés de restaurant qui commencent en français : la langue
<b>de leur poste</b>, apprise sur les objets, les plats et les consignes de la cuisine et de la salle. Avant de
l'offrir, nous voulons la voir travailler chez vous, avec quelques-uns de vos employés. C'est l'objet de ce pilote.</p>

<h2>Ce que c'est</h2>
<ul>
  <li>Sur le téléphone de l'employé, sans application à installer ni compte à créer ; une aide dans sa langue,
  au choix parmi onze (de l'arabe au tigrigna), écrite sous le français.</li>
  <li>{len(LX.LEXIQUE)} mots du poste (la cuisine, les ustensiles, les plats, les allergènes, la salle…), dits par des
  voix naturelles ; la consigne du chef à entendre dans le bruit de la cuisine ; la commande modifiée ; un test de niveau.</li>
  <li>Un service joué : {len(SI.SITUATIONS)} situations, le chef en cuisine et les clients en salle, auxquels l'employé
  répond de vive voix, avec un bilan geste par geste.</li>
  <li><b>Les allergies</b>, apprises dès le début avec une règle simple : faire répéter, l'écrire, le dire à la
  cuisine, vérifier — ne jamais dire « il n'y en a pas » sans vérifier.</li>
</ul>

<h2>Ce que nous vous demandons</h2>
<ul>
  <li>{E(postes)} Volontaires.</li>
  <li>Deux séances de 90 minutes, à une semaine d'écart, sur les heures de travail, hors des coups de feu :
  {v(PI.SEANCE_1, 24)} et {v(PI.SEANCE_2, 24)}.</li>
  <li>Une salle calme avec le wifi. Les employés utilisent leur téléphone et des écouteurs (nous en apportons au besoin).</li>
  <li>Une trentaine de minutes d'une personne de la direction, après la seconde séance, pour le bilan.</li>
</ul>

<h2>Ce que vous recevez</h2>
<ul>
  <li>La formation, pour les participants, pendant et après le pilote.</li>
  <li>Une fiche de poche par employé (les phrases de la cuisine et de la salle, la règle d'allergie, les mots d'ici qui piègent).</li>
  <li>Un rapport sur ce que le pilote a montré : ce que le matériel fait réussir, ce qu'il fait rater, et ce que nous corrigeons.</li>
</ul>
{cond_html}
<p><b>Elle ne remplace pas</b> la formation en hygiène et salubrité exigée des restaurants : elle donne la langue pour la suivre.</p>

<h2>Les données de vos employés</h2>
<p>Personne n'écrit son nom : chacun entre par un code affiché en classe et devient « Participant 1, 2, 3… ».
Ce qui est noté, ce sont les réponses aux questions fermées, sans nom. Les enregistrements du test oral restent sur
le téléphone de l'employé. <b>Le rapport porte sur le matériel, jamais sur une personne</b> : vous n'y trouverez
ni nom, ni résultat individuel. Chaque participant reçoit une fiche qui le lui explique dans sa langue.</p>

<p>Mené par : {v(PI.FORMATEUR, 30)} · observateur : {v(PI.OBSERVATEUR, 30)}</p>
<p class="sig">Au plaisir d'en discuter,</p>
<p>Daniel Tousignant<br>francis — formation au poste · {E(COURRIEL)}</p>
"""
    corps = '<style>body{font-size:9.6pt;line-height:1.34} h2{margin:9px 0 4px} ul{margin-bottom:5px}</style>' + corps
    return doc("Proposition de pilote", "Formation au poste<br>Restauration", corps)


PART = {
    "fr": dict(
        titre="Le pilote : ce que vous devez savoir", ou="Pour chaque participant",
        points=[
            ("C'est volontaire.", "Vous pouvez arrêter à tout moment, sans rien expliquer et sans conséquence."),
            ("On ne vous évalue pas.", "On évalue le matériel : si beaucoup de personnes ratent la même question, "
             "c'est la question qui est mauvaise, et nous la corrigeons."),
            ("Vous n'écrivez pas votre nom.", "Vous entrez avec le code affiché en classe ; vous devenez "
             "« Participant 1, 2, 3… » pour la séance."),
            ("Ce qui est noté.", "Vos réponses aux questions à choix (juste ou pas, au premier essai), sans nom. "
             "Au service joué : quels gestes vous avez faits, sans vos phrases. Et si une réponse à une allergie était une erreur grave."),
            ("Votre voix.", "Au test oral, votre enregistrement reste sur votre téléphone ; il s'efface quand le "
             "formateur a confirmé votre niveau. Au service joué, le navigateur transforme votre voix en texte (dans "
             "Chrome, par un service de Google) ; ce texte est envoyé à un service d'assistance automatique (un "
             "modèle d'intelligence artificielle) qui fait répondre le chef ou le client, puis n'est pas conservé."),
            ("Votre employeur.", "Il reçoit un rapport sur le matériel et sur le groupe. Jamais votre nom, jamais "
             "vos résultats."),
        ],
        q="Une question sur vos données, ou sur le pilote :", pol="Politique de confidentialité",
        fin="J'ai lu cette fiche."),
    "en": dict(
        titre="The pilot: what you need to know", ou="For each participant",
        points=[
            ("It's voluntary.", "You can stop at any time, without explaining why and without any consequence."),
            ("You are not being evaluated.", "The material is: if many people miss the same question, the question "
             "is bad, and we fix it."),
            ("You don't write your name.", "You enter with the code shown in class; you become \"Participant 1, "
             "2, 3…\" for the session."),
            ("What is recorded.", "Your answers to multiple-choice questions (right or not, on the first try), "
             "with no name. In the role-played service: which skills you used, not your sentences, and whether an answer about an allergy was a serious error."),
            ("Your voice.", "In the speaking test, your recording stays on your phone; it is deleted once the "
             "trainer confirms your level. In the role-played service, the browser turns your voice into text (in "
             "Chrome, through a Google service); that text is sent to an automatic assistance service (an artificial "
             "intelligence model) that makes the chef or the customer answer, and is not kept."),
            ("Your employer.", "They receive a report on the material and on the group. Never your name, never "
             "your results."),
        ],
        q="A question about your data, or about the pilot:", pol="Privacy policy (in French)",
        fin="I have read this sheet."),
    "es": dict(
        titre="El piloto: lo que debe saber", ou="Para cada participante",
        points=[
            ("Es voluntario.", "Puede detenerse en cualquier momento, sin dar explicaciones y sin consecuencias."),
            ("No se le evalúa a usted.", "Se evalúa el material: si muchas personas fallan la misma pregunta, la "
             "pregunta está mal, y la corregimos."),
            ("No escribe su nombre.", "Entra con el código que se muestra en clase; será «Participante 1, 2, 3…» "
             "durante la sesión."),
            ("Lo que se registra.", "Sus respuestas a las preguntas de opción (correcta o no, en el primer intento), "
             "sin nombre. En el servicio simulado: qué gestos hizo, no sus frases, y si una respuesta sobre una alergia fue un error grave."),
            ("Su voz.", "En la prueba oral, su grabación se queda en su teléfono; se borra cuando el formador "
             "confirma su nivel. En el servicio simulado, el navegador convierte su voz en texto (en Chrome, mediante "
             "un servicio de Google); ese texto se envía a un servicio de asistencia automática (un modelo de "
             "inteligencia artificial) que hace responder al chef o al cliente, y no se conserva."),
            ("Su empleador.", "Recibe un informe sobre el material y sobre el grupo. Nunca su nombre, nunca sus "
             "resultados."),
        ],
        q="Una pregunta sobre sus datos, o sobre el piloto:", pol="Política de privacidad (en francés)",
        fin="He leído esta hoja."),
}


def participants(l):
    P = PART[l]
    pts = "".join(f"<li><b>{E(t)}</b> {E(d)}</li>" for t, d in P["points"])
    corps = f"""<ol>{pts}</ol>
<div class="encadre"><p>{E(P["q"])} <b>{E(COURRIEL)}</b></p>
<p>{E(P["pol"])} : portail.edufrancis.ca/confidentialite.html</p></div>
<p style="margin-top:14px"><span class="case"></span>{E(P["fin"])}</p>"""
    return doc(P["titre"], E(P["ou"]), corps, lang=l, pied={"fr": "francis — formation au poste",
               "en": "francis — on-the-job training", "es": "francis — formación en el puesto"}[l])


def feuille_de_route():
    blocs = ""
    for k, (nom, etapes) in enumerate(PI.SEANCES):
        date = PI.SEANCE_1 if k == 0 else PI.SEANCE_2
        lignes = "".join(f"<tr><td>{E(t)}</td><td class=\"n\">{m}</td><td>{E(d)}</td></tr>" for t, m, d in etapes)
        total = sum(m for _, m, _ in etapes)
        avant = ("<li>Ouvrir la séance sans compte : Progression des élèves → groupe du pilote → « Séance sans compte » "
                 "→ atelier « Chez Jocelyne ». Imprimer la feuille QR, ou la projeter.</li>"
                 "<li>Ouvrir le direct de la classe sur le même écran (bloc « Le direct de la classe »).</li>"
                 "<li>Son : faire écouter un mot à chacun avec ses écouteurs avant de commencer.</li>")
        if k == 0:
            avant += ("<li>Donner la fiche « ce que vous devez savoir » dans la langue de chacun ; la lire ensemble.</li>"
                      "<li>Dire la règle d'allergie à voix haute avant de commencer : c'est la seule erreur éliminatoire.</li>"
                      "<li>La page d'entrée de la séance a un choix de langue en haut à droite (English, Español) : "
                      "la traduction se pose sous le français. Le montrer au groupe.</li>")
        else:
            avant += "<li>Le même appareil que la semaine passée : chacun retrouve son numéro de participant.</li>"
        blocs += f"""<section{' class="saut"' if k else ''}>
<h2>{E(nom)} — {v(date, 26)} · {total} minutes</h2>
<p><b>Avant (15 minutes plus tôt)</b></p><ul>{avant}</ul>
<table><thead><tr><th>Temps</th><th>Min.</th><th>Ce qu'on fait, ce qu'on regarde</th></tr></thead><tbody>{lignes}</tbody></table>
<p><b>Pendant</b> : le formateur mène, l'observateur ne parle pas et remplit la grille (une par séance, dans le
protocole). On note un <b>repère</b> (place, couleur de chandail), jamais un nom.</p>
<p><b>Après</b> : fermer la séance (le code ne fait plus entrer personne). Photographier ou exporter le direct du
groupe {'et noter le niveau confirmé de chacun, par repère' if k == 0 else ', puis garder les grilles pour le rapport'}.</p>
<p>Notes :</p><div class="zone haute"></div>
</section>"""
    corps = f"""<p>Formateur : {v(PI.FORMATEUR, 30)} · observateur : {v(PI.OBSERVATEUR, 30)} · restaurant : {v(PI.RESTAURANT, 30)}</p>
<div class="encadre"><p><b>Si ça ne marche pas.</b> Pas de son : vérifier le volume du téléphone, puis recharger la
page. Le code ne fait pas entrer : la séance est-elle ouverte, et le groupe est-il bien au <b>niveau 3</b> ? (Un
groupe d'un autre niveau ne peut pas ouvrir cette séance.) Le micro ne répond pas au service : il faut Chrome, et
autoriser le micro ; sinon, l'employé écrit sa réponse. Le service refuse de démarrer : le centre est-il en mode
« avec assistance » ?</p></div>
{blocs}"""
    return doc("Feuille de route du formateur", "Pilote<br>deux séances", corps)


def rapport_employeur():
    corps = f"""<div class="encadre"><p><b>Ce rapport porte sur le matériel, jamais sur une personne.</b> Aucun nom,
aucun résultat individuel. Un résultat se donne pour le groupe, et seulement s'il compte au moins trois personnes.</p></div>
<p>Restaurant : {v(PI.RESTAURANT, 30)} · séances : {v(PI.SEANCE_1, 22)} et {v(PI.SEANCE_2, 22)}</p>
<h2>1. Qui a participé</h2>
<table><thead><tr><th>Poste</th><th>Inscrits</th><th>Présents aux 2 séances</th><th>Langue d'appui (combien)</th></tr></thead><tbody>
<tr><td>Cuisine</td><td></td><td></td><td></td></tr><tr><td>Salle</td><td></td><td></td><td></td></tr></tbody></table>
<h2>2. L'allergie</h2>
<table><thead><tr><th>Où</th><th>Erreurs graves (nombre, sans nom)</th><th>Sur quels cas</th><th>Ce que nous corrigeons</th></tr></thead><tbody>
<tr><td>Exercices</td><td></td><td></td><td></td></tr><tr><td>Test</td><td></td><td></td><td></td></tr><tr><td>Service joué</td><td></td><td></td><td></td></tr></tbody></table>
<h2>3. Le service joué</h2>
<table><thead><tr><th>Porte</th><th>Situations réussies (sur celles jouées)</th><th>Geste le plus souvent oublié</th></tr></thead><tbody>
<tr><td>Cuisine</td><td></td><td></td></tr><tr><td>Salle</td><td></td><td></td></tr></tbody></table>
<h2>4. Le test, avant et après</h2>
<table><thead><tr><th>Niveaux à la 1<sup>re</sup> séance (combien par palier)</th><th>À la 2<sup>e</sup></th></tr></thead><tbody>
<tr><td>&nbsp;</td><td></td></tr></tbody></table>
<h2>5. Ce que le matériel a fait rater</h2>
<p>Les items ratés au premier essai par la moitié du groupe ou plus, lus au direct de la classe.</p>
<table><thead><tr><th>Item</th><th>Ce qu'on en conclut</th><th>Ce que nous corrigeons</th></tr></thead><tbody>
{"<tr><td>&nbsp;</td><td></td><td></td></tr>" * 5}</tbody></table>
<h2>6. Ce que les employés en ont dit</h2><div class="zone"></div>
<h2>7. Ce que nous recommandons</h2><div class="zone"></div>
<p class="sig">Préparé par : {v(PI.FORMATEUR, 30)} · date : <span class="blanc">&nbsp;</span></p>"""
    return doc("Rapport du pilote", "Pour la direction<br>du restaurant", corps)


def imprimer(f):
    pdf = f.with_suffix(".pdf")
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", f.as_uri()], capture_output=True, timeout=120)
    brut = pdf.read_bytes() if pdf.exists() else b""
    m = re.search(rb"/MediaBox\s*\[\s*0\s+0\s+([\d.]+)\s+([\d.]+)", brut)
    return ((round(float(m.group(1))), round(float(m.group(2)))) if m else None,
            len(re.findall(rb"/Type\s*/Page[^s]", brut)))


# ── La page du classeur ──────────────────────────────────────────────────────

DECISIONS = [
    {"k": "restaurant", "q": "Le restaurant partenaire", "champ": "Nom du restaurant, ville, et à qui écrire (titre)",
     "o": [], "w": "Un restaurant où vous connaissez quelqu'un, idéalement familial (déjeuners, plats d'ici), comme "
     "Chez Jocelyne. La trousse est bâtie sur un restaurant fictif ; le pilote, lui, se fait dans un vrai."},
    {"k": "conditions", "q": "Les conditions du premier pilote",
     "o": [["validation", "Offert, contre le droit de nommer le restaurant et un témoignage écrit", True],
           ["reduit", "À moitié prix, contre les mêmes contreparties", False],
           ["plein", f"Au prix de la formule pilote ({PX.FORMULES[0][1]})", False]],
     "w": "Le premier pilote est une validation : il sert à prouver, pas à vendre. Le présenter comme tel garde "
          "intact le prix affiché — la règle « le premier prix devient le plancher » vaut pour une vente, pas pour "
          "un essai offert et nommé comme tel."},
    {"k": "postes", "q": "Les postes du groupe",
     "o": [["deux", "La cuisine et la salle, dans un même groupe (le protocole)", True],
           ["cuisine", "La cuisine seulement", False],
           ["salle", "La salle seulement", False]],
     "w": "Les deux postes valident tout le matériel, et les mots et les exercices leur sont communs. Un seul poste "
          "se justifie si le restaurant n'embauche de nouveaux employés que d'un côté."},
    {"k": "formateur", "q": "Qui mène les séances",
     "o": [["daniel", "Vous, avec un observateur du restaurant", True],
           ["restaurant", "Un formateur du restaurant, avec vous en observateur", False]],
     "w": "Au premier pilote, mener vous-même montre ce que la trousse demande à un formateur. Au second, l'inverse "
          "vérifiera que le guide suffit.",
     "champ": "Nom de l'observateur (facultatif)"},
    {"k": "dates", "q": "Les deux séances", "champ": "Séance 1 et séance 2 (jour, date, heure), à une semaine d'écart",
     "o": [], "w": "Deux fois 90 minutes, sur les heures de travail, hors des coups de feu : souvent entre 14 h et 16 h 30."},
]


def pdf_lien(k):
    return f' · <a href="pilote-docs/{k}.pdf" target="_blank" rel="noopener">PDF</a>'


def page(docs_ok):
    calendrier = [
        ("J − 21", "Écrire au restaurant : la lettre (ci-dessous), après un premier appel."),
        ("J − 14", "Confirmer les dates, la salle, le nombre de participants. Envoyer à la relecture l'espagnol et "
                   "l'anglais — la règle d'allergie d'abord — si ce n'est pas fait. Faire vérifier les deux normes (MAPAQ)."),
        ("J − 7", "Portail : ajouter l'atelier 239 au catalogue en ligne s'il n'y est pas ; créer le groupe du pilote "
                  "<b>au niveau 3</b>. Jouer vous-même une situation en cuisine et une en salle, sur votre téléphone."),
        ("J − 1", "Imprimer : les fiches « ce que vous devez savoir » (une par personne, dans sa langue), la feuille "
                  "de route, deux grilles d'observation par séance, les fiches de poche. Prévoir des écouteurs."),
        ("J", "Séance 1, selon la feuille de route. Fermer la séance à la fin."),
        ("J + 7", "Séance 2. Fermer la séance ; exporter le direct du groupe."),
        ("J + 10", "Le rapport (gabarit ci-dessous), puis les corrections du matériel — la boucle reprend."),
    ]
    cal = "".join(f"<tr><td><b>{E(j)}</b></td><td>{t}</td></tr>" for j, t in calendrier)
    liens = [("lettre-restaurant", "La lettre au restaurant", "la proposition, les allergies, les données, ce que le restaurant reçoit"),
             ("participants-fr", "Ce que vous devez savoir — français", "une page par employé (Loi 25)"),
             ("participants-en", "What you need to know — English", "idem, en anglais"),
             ("participants-es", "Lo que debe saber — español", "idem, en espagnol"),
             ("feuille-de-route", "La feuille de route du formateur", "les deux séances, avant, pendant, après"),
             ("rapport-employeur", "Le rapport au restaurant (gabarit)", "par poste, jamais par personne")]
    docs = "".join(
        f'<tr><td><b>{E(t)}</b><br><span style="color:var(--muted)">{E(d)}</span></td>'
        f'<td><a href="pilote-docs/{k}.html" target="_blank" rel="noopener">page</a>'
        f'{pdf_lien(k) if docs_ok.get(k) else ""}</td></tr>'
        for k, t, d in liens)
    manque = [n for n, x in (("le restaurant", PI.RESTAURANT), ("les dates", PI.SEANCE_1), ("le formateur", PI.FORMATEUR),
                             ("les conditions", PI.CONDITIONS)) if not x]
    etat = (f"Les documents s'impriment déjà ; il leur manque {', '.join(manque)} — des lignes à remplir à la main, "
            "ou vos réponses ci-dessous, et je les refais remplis." if manque else
            "Tout est rempli : les documents sont prêts à imprimer.")
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", f"<title>{E(ID.NOM)} — préparer le pilote</title>", tete)
    tete = tete.replace("</style>", """
.champ{font:inherit;font-size:15px;width:100%;padding:8px 10px;border:1px solid var(--line-fort);border-radius:8px;
  background:var(--card);color:var(--ink);margin-top:10px;box-sizing:border-box}
table.cmp{display:table;width:100%;min-width:0}
.cmp td{overflow-wrap:anywhere}
</style>""", 1)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{E(ID.NOM)} &middot; étape 5, pour de vrai</p>
<h1>Préparer le pilote</h1>
<p class="chapeau">Le <a href="restauration-pilote.html">protocole</a> dit pourquoi et comment on lit les résultats.
Cette page-ci sert à le <b>mener</b> : cinq décisions, un calendrier, et les documents à imprimer. {E(etat)}</p>

<section>
  <h2>La répétition générale</h2>
  <p>Jouée le 30 septembre 2026 sur un serveur jetable, avec des personnes inventées : un groupe de niveau 3, une
  séance sur l'atelier 239, deux employés qui entrent par le code et répondent ; le direct montre chaque item au
  premier essai, et l'allergie ratée porte « erreur grave ».</p>
  <div class="reserve"><p><strong>Elle a trouvé un défaut, corrigé :</strong> retirer le code de l'adresse (une
  précaution pour la vie privée) faisait perdre le lien avec le direct quand on rechargeait la page en pleine séance.
  Et deux contraintes à connaître : un groupe qui n'est pas au <b>niveau 3</b> ne peut pas ouvrir la séance, et
  <b>l'atelier 239 doit être ajouté au catalogue en ligne</b> par le portail.</p></div>
</section>

<section>
  <h2>Cinq décisions</h2>
  <div id="decisions"></div>
  <p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<section>
  <h2>Le calendrier</h2>
  <table class="cmp"><tbody>{cal}</tbody></table>
</section>

<section>
  <h2>Les documents à imprimer</h2>
  <p>Noir et blanc, format lettre. La grille d'observation est dans le <a href="restauration-pilote.html">protocole</a> ;
  les <a href="fiche/fiche-es.pdf">fiches de poche</a> (aussi <a href="fiche/fiche-fr.pdf">en français seul</a> et
  <a href="fiche/fiche-en.pdf">avec l'anglais</a>), dans le classeur.</p>
  <table class="cmp"><tbody>{docs}</tbody></table>
</section>

<div class="pied"><p>Page produite par <code>build/restauration_pilote_trousse.py</code> — ne pas l'éditer. Les valeurs
du restaurant vivent dans <code>build/contenu/entreprise-restaurant/pilote.py</code>.</p></div>
</div>
<script>
(function(){{
  var D={json.dumps(DECISIONS, ensure_ascii=False)};
  var CLE='restauration-pilote-trousse', s={{choix:{{}},champ:{{}}}};
  try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.choix)s=l;}}catch(e){{}}
  function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){{
    var div=document.createElement('div');div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p>';
    if(d.o.length){{h+='<div class="opts">';d.o.forEach(function(o){{h+='<button type="button" class="opt" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'+o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';}});h+='</div>';}}
    if(d.champ)h+='<input class="champ" type="text" data-c="'+d.k+'" placeholder="'+d.champ+'">';
    div.innerHTML=h+'<p class="dw">'+d.w+'</p>';zone.appendChild(div);
  }});
  zone.querySelectorAll('[data-c]').forEach(function(x){{x.value=s.champ[x.dataset.c]||'';x.oninput=function(){{s.champ[x.dataset.c]=x.value;sv();peindre();}};}});
  function peindre(){{
    zone.querySelectorAll('.opt').forEach(function(b){{b.setAttribute('aria-pressed',s.choix[b.dataset.k]===b.dataset.v?'true':'false');}});
    var n=D.filter(function(d){{return s.choix[d.k]||(s.champ[d.k]||'').trim();}}).length;
    document.getElementById('etat').textContent=n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }}
  zone.addEventListener('click',function(e){{var b=e.target.closest('.opt');if(!b)return;
    if(s.choix[b.dataset.k]===b.dataset.v)delete s.choix[b.dataset.k];else s.choix[b.dataset.k]=b.dataset.v;sv();peindre();}});
  document.getElementById('exporter').addEventListener('click',function(){{
    var out={{page:'restauration-pilote-trousse',date:new Date().toISOString().slice(0,10),decisions:{{}}}};
    D.forEach(function(d){{var o=d.o.filter(function(x){{return x[0]===s.choix[d.k];}})[0];
      out.decisions[d.k]={{choix:o?o[0]:null,libelle:o?o[1]:null,texte:(s.champ[d.k]||'').trim()||null}};}});
    var t=JSON.stringify(out,null,2),fin=function(){{document.getElementById('etat').textContent='Copié — recolle-le-moi.';}};
    if(navigator.clipboard)navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}});else prompt('Copiez :',t);
  }});
  peindre();
}})();
</script>
</body></html>"""
    PAGE.write_text(tete + corps, encoding="utf-8")


def main():
    verifier_minutes()
    DOCS.mkdir(parents=True, exist_ok=True)
    pieces = {"lettre-restaurant": lettre_restaurant(), "feuille-de-route": feuille_de_route(),
              "rapport-employeur": rapport_employeur(),
              **{f"participants-{l}": participants(l) for l in ("fr", "es", "en")}}
    ok, ecarts = {}, 0
    for k, h in pieces.items():
        f = DOCS / f"{k}.html"
        f.write_text(h, encoding="utf-8")
        ligne = f"  {k}"
        if "--sans-pdf" not in sys.argv:
            taille, n = imprimer(f)
            bon = taille == LETTRE and 1 <= n <= PAGES_MAX[k]
            ok[k] = bon; ecarts += not bon
            ligne += f" · PDF {taille} {n} p. {'✓' if bon else '✗ (max ' + str(PAGES_MAX[k]) + ')'}"
        print(ligne)
    page(ok)
    print(PAGE.relative_to(RACINE))
    sys.exit(1 if ecarts else 0)


if __name__ == "__main__":
    main()
