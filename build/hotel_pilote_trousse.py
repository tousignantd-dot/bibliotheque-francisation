#!/usr/bin/env python3
"""La trousse du pilote RÉEL de l'Hôtel Rive-Claire : décider, préparer, imprimer.

    python3 build/hotel_pilote_trousse.py             # la page + les documents + leurs PDF
    python3 build/hotel_pilote_trousse.py --sans-pdf

Sorties (produites, jamais éditées) :
  assets/presentations/hotellerie-pilote-trousse.html        décisions à exporter, calendrier, liens
  assets/presentations/hotellerie-pilote-docs/*.html (+ .pdf) à imprimer, noir et blanc, format lettre :
    lettre-hotel         la proposition à la direction de l'hôtel
    participants-fr|en|es ce que chaque employé doit savoir (Loi 25), dans sa langue
    feuille-de-route     les deux séances, pour le formateur
    rapport-employeur    le gabarit du rapport, sans aucun nom

Le protocole (le pourquoi, les règles de décision, la grille) reste
hotellerie-pilote.html ; cette trousse-ci est le comment. Les valeurs propres à
l'hôtel partenaire vivent dans build/contenu/entreprise-hotel/pilote.py : tant
qu'elles manquent, les documents portent une ligne à remplir à la main.

Répétition générale du 27 sept. 2026, sur un serveur jetable : deux groupes de
niveau 3, deux séances sur l'atelier 238, des participants qui entrent par le
code, répondent, et paraissent au direct de leur groupe seulement. Elle a trouvé
deux défauts de la page (premier coup jamais compté, items illisibles au direct),
corrigés avant d'écrire cette trousse. Elle a aussi montré qu'un groupe qui n'est
pas au niveau 3 ne peut PAS ouvrir la séance : c'est dans la liste de vérification.
"""
import html, importlib.util, json, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
PAGE = RACINE / "assets" / "presentations" / "hotellerie-pilote-trousse.html"
DOCS = RACINE / "assets" / "presentations" / "hotellerie-pilote-docs"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
POLICE = "../../design-system/fonts/nunito-latin.woff2"
LETTRE = (612, 792)
PAGES_MAX = {"lettre-hotel": 1, "participants-fr": 1, "participants-en": 1, "participants-es": 1,
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
CL = _charger("pt_clients", CONTENU / "clients.py")


def v(x, largeur=14):
    """Une valeur, ou la ligne à remplir à la main."""
    return E(x) if x else f'<span class="blanc">{"&nbsp;" * largeur}</span>'


def verifier_minutes():
    src = (RACINE / "build" / "hotel_pilote.py").read_text(encoding="utf-8")
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
            f'<div class="pied"><span>{E(pied)}</span><span>Hôtel Rive-Claire · pilote</span></div></div></body></html>')


# ── Les documents ────────────────────────────────────────────────────────────

def lettre_hotel():
    groupes = PI.GROUPES_TEXTE.get(PI.GROUPES) or PI.GROUPES_TEXTE["deux"]
    conditions = PI.CONDITIONS_TEXTE.get(PI.CONDITIONS)
    cond_html = (f"<p>{E(conditions)}</p>" if conditions else
                 '<p>Conditions : <span class="blanc" style="min-width:120mm">&nbsp;</span></p>')
    corps = f"""
<p>À l'attention de : {v(PI.CONTACT, 40)}<br>{v(PI.HOTEL, 40)}{(", " + E(PI.VILLE)) if PI.VILLE else ""}</p>
<p><b>Objet : un pilote de formation linguistique au comptoir de réception</b></p>
<p>Madame, Monsieur,</p>
<p>Nous avons conçu une formation courte pour les employés de réception : la langue <b>de leur poste</b>, apprise
sur les objets et les gestes du comptoir, en français, en anglais ou en espagnol. Avant de l'offrir, nous
voulons la voir travailler chez vous, avec quelques-uns de vos employés. C'est l'objet de ce pilote.</p>

<h2>Ce que c'est</h2>
<ul>
  <li>Sur le téléphone de l'employé, sans application à installer ni compte à créer.</li>
  <li>{len(LX.LEXIQUE)} mots du poste (arrivée, chambre, services, paiement, problèmes…), dits par des voix
  naturelles ; des exercices d'écoute (noms épelés, numéros de chambre, prix, heures) ; un test de niveau.</li>
  <li>Un comptoir joué : {len(CL.CLIENTS)} clients virtuels (une arrivée, une chambre complète, une plainte, une
  facture contestée, un appel…) à qui l'employé répond de vive voix, avec un bilan geste par geste.</li>
  <li>Une règle apprise dès le début : ce que le réceptionniste décide seul, et ce qu'il transmet au gérant.</li>
</ul>

<h2>Ce que nous vous demandons</h2>
<ul>
  <li>{E(groupes)} Trois à six personnes par groupe, volontaires.</li>
  <li>Deux séances de 90 minutes, à une semaine d'écart, sur les heures de travail :
  {v(PI.SEANCE_1, 24)} et {v(PI.SEANCE_2, 24)}.</li>
  <li>Une salle calme avec le wifi. Les employés utilisent leur téléphone et des écouteurs (nous en apportons
  au besoin).</li>
  <li>Une trentaine de minutes d'une personne de la direction, après la seconde séance, pour le bilan.</li>
</ul>

<h2>Ce que vous recevez</h2>
<ul>
  <li>La formation, pour les participants, pendant et après le pilote.</li>
  <li>Une fiche de poche par employé (les phrases du comptoir, les mots qui piègent, l'alphabet pour épeler).</li>
  <li>Un rapport sur ce que le pilote a montré : ce que le matériel fait réussir, ce qu'il fait rater, et ce que
  nous corrigeons.</li>
</ul>
{cond_html}

<h2>Les données de vos employés</h2>
<p>Personne n'écrit son nom : chacun entre par un code affiché en classe et devient « Participant 1, 2, 3… ».
Ce qui est noté, ce sont les réponses aux questions fermées, sans nom. Les enregistrements du test oral restent sur
le téléphone de l'employé. <b>Le rapport porte sur le matériel, jamais sur une personne</b> : vous n'y trouverez
ni nom, ni résultat individuel. Chaque participant reçoit une fiche qui le lui explique dans sa langue.</p>

<p>Mené par : {v(PI.FORMATEUR, 30)} · observateur : {v(PI.OBSERVATEUR, 30)}</p>
<p class="sig">Au plaisir d'en discuter,</p>
<p>Daniel Tousignant<br>francis — formation au poste · {E(COURRIEL)}</p>
"""
    # Une lettre tient sur une page : corps un cran plus petit que les autres documents.
    corps = '<style>body{font-size:9.8pt;line-height:1.36} h2{margin:10px 0 4px} ul{margin-bottom:5px}</style>' + corps
    return doc("Proposition de pilote", "Formation au poste<br>Réception d'hôtel", corps)


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
             "Au comptoir joué : quels gestes vous avez faits, sans vos phrases."),
            ("Votre voix.", "Au test oral, votre enregistrement reste sur votre téléphone ; il s'efface quand le "
             "formateur a confirmé votre niveau, ou après 30 jours. Au comptoir joué, le navigateur transforme votre "
             "voix en texte (dans Chrome, par un service de Google) ; ce texte est envoyé à un service d'intelligence "
             "artificielle qui fait répondre le client, puis n'est pas conservé."),
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
             "with no name. In the desk role-play: which skills you used, not your sentences."),
            ("Your voice.", "In the speaking test, your recording stays on your phone; it is deleted once the "
             "trainer confirms your level, or after 30 days. In the desk role-play, the browser turns your voice "
             "into text (in Chrome, through a Google service); that text is sent to an artificial intelligence "
             "service that makes the guest answer, and is not kept."),
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
             "sin nombre. En el mostrador simulado: qué gestos hizo, no sus frases."),
            ("Su voz.", "En la prueba oral, su grabación se queda en su teléfono; se borra cuando el formador "
             "confirma su nivel, o después de 30 días. En el mostrador simulado, el navegador convierte su voz en "
             "texto (en Chrome, mediante un servicio de Google); ese texto se envía a un servicio de inteligencia "
             "artificial que hace responder al cliente, y no se conserva."),
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
                 "→ atelier « Hôtel Rive-Claire ». Imprimer la feuille QR, ou la projeter.</li>"
                 "<li>Ouvrir le direct de la classe sur le même écran (bloc « Le direct de la classe »).</li>"
                 "<li>Son : faire écouter un mot à chacun avec ses écouteurs avant de commencer.</li>")
        if k == 0:
            avant += ("<li>Donner la fiche « ce que vous devez savoir » dans la langue de chacun ; la lire ensemble.</li>"
                      "<li>La page d'entrée de la séance est en français : montrer le bouton « Commencer ».</li>")
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
    corps = f"""<p>Formateur : {v(PI.FORMATEUR, 30)} · observateur : {v(PI.OBSERVATEUR, 30)} · hôtel : {v(PI.HOTEL, 30)}</p>
<div class="encadre"><p><b>Si ça ne marche pas.</b> Pas de son : vérifier le volume du téléphone, puis recharger la
page. Le code ne fait pas entrer : la séance est-elle ouverte, et le groupe est-il bien au <b>niveau 3</b> ? (Un
groupe d'un autre niveau ne peut pas ouvrir cette séance.) Le micro ne répond pas au comptoir : il faut Chrome, et
autoriser le micro ; sinon, l'employé écrit sa réponse.</p></div>
{blocs}"""
    return doc("Feuille de route du formateur", "Pilote<br>deux séances", corps)


def rapport_employeur():
    corps = f"""<div class="encadre"><p><b>Ce rapport porte sur le matériel, jamais sur une personne.</b> Aucun nom,
aucun résultat individuel. Un résultat se donne par groupe, et seulement si le groupe compte au moins trois
personnes.</p></div>
<p>Hôtel : {v(PI.HOTEL, 30)} · séances : {v(PI.SEANCE_1, 22)} et {v(PI.SEANCE_2, 22)}</p>
<h2>1. Qui a participé</h2>
<table><thead><tr><th>Groupe</th><th>Apprend</th><th>Inscrits</th><th>Présents aux 2 séances</th></tr></thead><tbody>
<tr><td>A</td><td>l'anglais</td><td></td><td></td></tr><tr><td>B</td><td>le français</td><td></td><td></td></tr></tbody></table>
<h2>2. Au comptoir joué</h2>
<table><thead><tr><th>Groupe</th><th>Situations réussies (moyenne sur {len(CL.CLIENTS)})</th><th>Du premier coup</th><th>Geste le plus souvent oublié</th></tr></thead><tbody>
<tr><td>A</td><td></td><td></td><td></td></tr><tr><td>B</td><td></td><td></td><td></td></tr></tbody></table>
<h2>3. Le test, avant et après</h2>
<table><thead><tr><th>Groupe</th><th>Niveaux à la 1<sup>re</sup> séance (combien par palier)</th><th>À la 2<sup>e</sup></th></tr></thead><tbody>
<tr><td>A</td><td></td><td></td></tr><tr><td>B</td><td></td><td></td></tr></tbody></table>
<h2>4. Ce que le matériel a fait rater</h2>
<p>Les items ratés au premier essai par la moitié du groupe ou plus, lus au direct de la classe.</p>
<table><thead><tr><th>Item</th><th>Groupe</th><th>Ce qu'on en conclut</th><th>Ce que nous corrigeons</th></tr></thead><tbody>
{"<tr><td>&nbsp;</td><td></td><td></td><td></td></tr>" * 5}</tbody></table>
<h2>5. Ce que les employés en ont dit</h2><div class="zone"></div>
<h2>6. Ce que nous recommandons</h2><div class="zone"></div>
<p class="sig">Préparé par : {v(PI.FORMATEUR, 30)} · date : <span class="blanc">&nbsp;</span></p>"""
    return doc("Rapport du pilote", "Pour la direction<br>de l'hôtel", corps)


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
    {"k": "hotel", "q": "L'hôtel partenaire", "champ": "Nom de l'hôtel, ville, et à qui écrire (titre)",
     "o": [], "w": "Un hôtel où vous connaissez quelqu'un. La trousse est bâtie sur un hôtel fictif ; le pilote, lui, "
     "se fait dans un vrai."},
    {"k": "conditions", "q": "Les conditions du premier pilote",
     "o": [["validation", "Offert, contre le droit de nommer l'hôtel et un témoignage écrit", True],
           ["reduit", "À moitié prix, contre les mêmes contreparties", False],
           ["plein", f"Au prix de la formule pilote ({PX.FORMULES[0][1]})", False]],
     "w": "Le premier pilote est une validation : il sert à prouver, pas à vendre. Le présenter comme tel garde "
          "intact le prix affiché — la règle « le premier prix devient le plancher » vaut pour une vente, pas pour "
          "un essai offert et nommé comme tel."},
    {"k": "groupes", "q": "Les groupes",
     "o": [["deux", "Deux groupes : A fr → en et B es → fr (le protocole)", True],
           ["A", "Le groupe A seulement (fr → en)", False],
           ["B", "Le groupe B seulement (es → fr)", False]],
     "w": "Deux directions valident deux fois plus de matériel. Un seul groupe se justifie si l'hôtel n'a pas "
          "d'employés hispanophones."},
    {"k": "formateur", "q": "Qui mène les séances",
     "o": [["daniel", "Vous, avec un observateur de l'hôtel", True],
           ["hotel", "Un formateur de l'hôtel, avec vous en observateur", False]],
     "w": "Au premier pilote, mener vous-même montre ce que la trousse demande à un formateur. Au second, l'inverse "
          "vérifiera que le guide suffit. Un formateur de l'hôtel aurait besoin d'un compte enseignant (code et mot "
          "de passe temporaires, remis en main propre).",
     "champ": "Nom de l'observateur (facultatif)"},
    {"k": "dates", "q": "Les deux séances", "champ": "Séance 1 et séance 2 (jour, date, heure), à une semaine d'écart",
     "o": [], "w": "Deux fois 90 minutes, sur les heures de travail, hors des pointes d'arrivée (souvent 15 h – 18 h)."},
]


def pdf_lien(k):
    return f' · <a href="hotellerie-pilote-docs/{k}.pdf" target="_blank" rel="noopener">PDF</a>'


def page(docs_ok):
    calendrier = [
        ("J − 21", "Écrire à l'hôtel : la lettre (ci-dessous), après un premier appel."),
        ("J − 14", "Confirmer les dates, la salle, le nombre de participants par groupe. Envoyer à la relecture "
                   "l'anglais et l'espagnol si ce n'est pas fait (la fiche le signale « non relu » sinon)."),
        ("J − 7", "Portail : créer les groupes du pilote <b>au niveau 3</b> — sinon la séance sur l'atelier 238 est "
                  "refusée. Jouer vous-même deux clients en ligne dans la direction de chaque groupe."),
        ("J − 1", "Imprimer : les fiches « ce que vous devez savoir » (une par personne, dans sa langue), la feuille "
                  "de route, deux grilles d'observation par séance, les fiches de poche. Charger les téléphones de "
                  "rechange ; prévoir des écouteurs."),
        ("J", "Séance 1, selon la feuille de route. Fermer la séance à la fin."),
        ("J + 7", "Séance 2. Fermer la séance ; exporter le direct de chaque groupe."),
        ("J + 10", "Le rapport (gabarit ci-dessous), puis les corrections du matériel — la boucle reprend."),
    ]
    cal = "".join(f"<tr><td><b>{E(j)}</b></td><td>{t}</td></tr>" for j, t in calendrier)
    liens = [("lettre-hotel", "La lettre à l'hôtel", "la proposition, les données, ce que l'hôtel reçoit"),
             ("participants-fr", "Ce que vous devez savoir — français", "une page par employé (Loi 25)"),
             ("participants-en", "What you need to know — English", "idem, en anglais"),
             ("participants-es", "Lo que debe saber — español", "idem, en espagnol"),
             ("feuille-de-route", "La feuille de route du formateur", "les deux séances, avant, pendant, après"),
             ("rapport-employeur", "Le rapport à l'hôtel (gabarit)", "par groupe, jamais par personne")]
    docs = "".join(
        f'<tr><td><b>{E(t)}</b><br><span style="color:var(--muted)">{E(d)}</span></td>'
        f'<td><a href="hotellerie-pilote-docs/{k}.html" target="_blank" rel="noopener">page</a>'
        f'{pdf_lien(k) if docs_ok.get(k) else ""}</td></tr>'
        for k, t, d in liens)
    manque = [n for n, x in (("l'hôtel", PI.HOTEL), ("les dates", PI.SEANCE_1), ("le formateur", PI.FORMATEUR),
                             ("les conditions", PI.CONDITIONS)) if not x]
    etat = (f"Les documents s'impriment déjà ; il leur manque {', '.join(manque)} — des lignes à remplir à la main, "
            "ou vos réponses ci-dessous, et je les refais remplis." if manque else
            "Tout est rempli : les documents sont prêts à imprimer.")
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Hôtel Rive-Claire — préparer le pilote</title>", tete)
    RIVE = _charger("pt_rive", RACINE / "build" / "hotel_rive.py")
    tete = tete.replace("</style>", RIVE.CSS + """
.champ{font:inherit;font-size:15px;width:100%;padding:8px 10px;border:1px solid var(--line-fort);border-radius:8px;
  background:var(--card);color:var(--ink);margin-top:10px;box-sizing:border-box}
table.cmp{display:table;width:100%;min-width:0}
.cmp td{overflow-wrap:anywhere}
</style>""", 1)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; étape 5, pour de vrai</p>
<h1>Préparer le pilote</h1>
<p class="chapeau">Le <a href="hotellerie-pilote.html">protocole</a> dit pourquoi et comment on lit les résultats.
Cette page-ci sert à le <b>mener</b> : cinq décisions, un calendrier, et les documents à imprimer. {E(etat)}</p>

<section>
  <h2>La répétition générale</h2>
  <p>Jouée le 27 septembre 2026 sur un serveur jetable, avec des personnes inventées : deux groupes de niveau 3,
  une séance chacun sur l'atelier 238, des employés qui entrent par le code, répondent, et paraissent au direct
  <b>de leur groupe seulement</b> ; revenir du même téléphone rend le même participant ; fermer la séance coupe les
  téléphones déjà entrés.</p>
  <div class="reserve"><p><strong>Elle a trouvé deux défauts, corrigés :</strong> aucune bonne réponse n'aurait été
  comptée « du premier coup » au direct (la règle du pilote se serait lue de travers), et les items y paraissaient
  sous leur code (« lit-appoint ») au lieu du mot. Et une contrainte à connaître : un groupe qui n'est pas au
  <b>niveau 3</b> ne peut pas ouvrir la séance.</p></div>
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
  <p>Noir et blanc, format lettre. La grille d'observation est dans le <a href="hotellerie-pilote.html">protocole</a> ;
  les fiches de poche, dans le classeur.</p>
  <table class="cmp"><tbody>{docs}</tbody></table>
</section>

<div class="pied"><p>Page produite par <code>build/hotel_pilote_trousse.py</code> — ne pas l'éditer. Les valeurs
de l'hôtel vivent dans <code>build/contenu/entreprise-hotel/pilote.py</code>.</p></div>
</div>
<script>
(function(){{
  var D={json.dumps(DECISIONS, ensure_ascii=False)};
  var CLE='hotellerie-pilote-trousse', s={{choix:{{}},champ:{{}}}};
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
    var out={{page:'hotellerie-pilote-trousse',date:new Date().toISOString().slice(0,10),decisions:{{}}}};
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
    pieces = {"lettre-hotel": lettre_hotel(), "feuille-de-route": feuille_de_route(),
              "rapport-employeur": rapport_employeur(),
              **{f"participants-{l}": participants(l) for l in ("fr", "en", "es")}}
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
