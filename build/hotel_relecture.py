#!/usr/bin/env python3
"""La relecture de l'anglais et de l'espagnol de la trousse de l'hôtel, par un locuteur.

    python3 build/hotel_relecture.py
      → assets/presentations/hotellerie-relecture.html      (pour Daniel : les deux courriels, le suivi)
      → modules-autonomes/hotel-relecture/en.html   (pour la personne qui relit l'anglais, en anglais)
      → modules-autonomes/hotel-relecture/es.html   (pour la personne qui relit l'espagnol, en espagnol)

Les pages des relecteurs sont HORS du classeur : celui-ci est fermé par mot de
passe en ligne (verrou du classeur, server.py), et une personne de l'extérieur
ne doit pas en recevoir la clé. Elles ne portent que le contenu de la trousse,
déjà public dans modules-autonomes/hotel-reception/.

Produites, jamais éditées. Tout texte relu est LU dans build/contenu/entreprise-hotel/ :
les mots du lexique, puis chaque dictionnaire {fr, en, es} (ou {fr, en} / {fr, es}
pour les notes de pièges) des cinq fichiers de contenu. Chaque texte porte un
identifiant stable (fichier.VARIABLE[chemin].langue) : l'export du relecteur
revient avec ces identifiants, et la correction se pose à la bonne place.

Sont écartés : ce qui n'est pas un texte à lire (noms de voix), les noms de
langue écrits en français, et les consignes données au modèle du jeu de rôle
(PARLER, LANGUE_BILAN, CADRAGE) — ce ne sont pas des phrases que l'employé voit.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
DEST = RACINE / "assets" / "presentations"
DEST_R = RACINE / "modules-autonomes" / "hotel-relecture"
E = html.escape
FICHIERS = ("interface", "exercices", "test", "clients", "fiche")
ECARTES = {"VOIX", "NOM_LANGUE", "APPREND_ART", "DESCRIPTEUR", "PARLER", "LANGUE_BILAN", "CADRAGE"}
ADRESSE = "https://portail.edufrancis.ca/modules-autonomes/hotel-relecture/{l}.html"

# Les sections, dans l'ordre où l'employé les rencontre, nommées dans la langue du relecteur.
SECTIONS = [
    ("lexique", "The words (picture boards)", "Las palabras (las láminas)"),
    ("interface.PLANCHES", "Names of the picture boards", "Nombres de las láminas"),
    ("interface.UI", "Screen texts", "Textos de la pantalla"),
    ("interface.PIEGES", "Tricky words: the notes", "Palabras engañosas: las notas"),
    ("exercices.UI", "Practice: screen texts", "Ejercicios: textos de la pantalla"),
    ("exercices.NOMBRES", "Numbers and times (spoken)", "Números y horas (se escuchan)"),
    ("exercices.ERREURS_NOMBRES", "Numbers: feedback", "Números: retroalimentación"),
    ("exercices.EPELER_INTRO", "Spelling (spoken)", "Deletrear (se escucha)"),
    ("exercices.DEMANDES", "What the guest wants (a guest speaking, fast)", "Lo que quiere el cliente (habla un cliente, rápido)"),
    ("exercices.REPONSES", "What I answer (the guest, then the receptionist's answers and feedback)",
     "Qué respondo (el cliente, luego las respuestas del recepcionista y la retroalimentación)"),
    ("exercices.REGLE_RELAIS", "The desk rule", "La regla del mostrador"),
    ("exercices.PROMESSE", "The desk rule: feedback", "La regla del mostrador: retroalimentación"),
    ("test.UI", "Placement test: screen texts", "Prueba de ubicación: textos de la pantalla"),
    ("test.A", "Test, part A: words", "Prueba, parte A: palabras"),
    ("test.B", "Test, part B: on the phone", "Prueba, parte B: por teléfono"),
    ("test.C", "Test, part C: who decides", "Prueba, parte C: quién decide"),
    ("test.CHOIX_C", "Test, part C: the choices", "Prueba, parte C: las opciones"),
    ("test.D", "Test, part D: speaking", "Prueba, parte D: hablar"),
    ("test.GESTES", "Test: the desk skills", "Prueba: los gestos del mostrador"),
    ("test.ORAL_GESTE", "Test: trainer's rating (skill)", "Prueba: nota del formador (gesto)"),
    ("test.ORAL_LANGUE", "Test: trainer's rating (language)", "Prueba: nota del formador (lengua)"),
    ("clients.UI_JEU", "At the desk (role-play): screen texts", "En el mostrador (juego de roles): textos de la pantalla"),
    ("clients.OUVERTURE", "At the desk: the receptionist's first line", "En el mostrador: la primera frase del recepcionista"),
    ("clients.GESTES", "At the desk: the six skills and their phrases", "En el mostrador: los seis gestos y sus frases"),
    ("clients.TITRE", "At the desk: how guests are addressed", "En el mostrador: cómo se nombra al cliente"),
    ("clients.CLIENTS", "At the desk: the eight guests (task card, screen)", "En el mostrador: los ocho clientes (tarjeta, pantalla)"),
    ("clients.REGLE_RELAIS", "At the desk: the rule", "En el mostrador: la regla"),
    ("clients.EXEMPLE_CONSEIL", "At the desk: example of advice", "En el mostrador: ejemplo de consejo"),
    ("fiche.UI", "Pocket card (printed)", "Tarjeta de bolsillo (impresa)"),
]

TXT = {
    "en": {
        "titre": "Review of the English — Hôtel Rive-Claire",
        "chapeau": "Thank you for reviewing this. It takes about {h}: {n} short texts, {m} words in all.",
        "quoi": "<p><b>What this is.</b> A training kit for front-desk employees of a hotel in Quebec. Some of them "
                "speak French and are <b>learning English</b>. They hear the English lines, answer guests in role-plays, "
                "and read the screen in their own language. The hotel, the guests and their names are invented.</p>"
                "<p><b>What we need from you.</b> For each text: does it sound like something a real person would say or "
                "read, in <b>North American English</b>, at a hotel front desk? Guests speak casually and fast; the "
                "receptionist is polite and professional. Screen texts should be short and plain.</p>"
                "<p><b>Please keep as is:</b> names, numbers, <code>{…}</code> placeholders, the <code>|</code> line "
                "separators, and French words in « quotes » (they are the French the learner must recognize). The "
                "French original is shown in grey only to help — you don't need to review it.</p>",
                "ok": "OK", "change": "Change", "question": "Question", "tout_ok": "All OK in this section",
        "fr": "French original", "note": "Note (in French)", "ctx": "Context",
        "nom": "Your name", "general": "General comments (optional)",
        "exporter": "Send my review", "fichier": "Download as a file",
        "fin": "Copied. Paste it into an email to Daniel, or attach the downloaded file.",
        "etat": "{f} of {n} reviewed", "garde": "Your work is saved in this browser: you can close the page and come back.",
        "corr": "Your version", "quest": "Your question",
    },
    "es": {
        "titre": "Revisión del español — Hôtel Rive-Claire",
        "chapeau": "Gracias por revisar esto. Toma unas {h}: {n} textos cortos, {m} palabras en total.",
        "quoi": "<p><b>De qué se trata.</b> Un material de formación para recepcionistas de un hotel en Quebec. Algunos "
                "hablan español y <b>aprenden francés</b>; otros hablan francés y aprenden español. Leen la pantalla en "
                "su idioma, escuchan frases y responden a clientes en juegos de roles. El hotel, los clientes y sus "
                "nombres son inventados.</p>"
                "<p><b>Lo que necesitamos.</b> Para cada texto: ¿suena como algo que una persona real diría o leería, "
                "en <b>español de México</b>, en la recepción de un hotel? Se trata de <b>usted</b>. Los clientes hablan "
                "de manera natural y rápida; el recepcionista es cortés y profesional. Los textos de pantalla deben ser "
                "cortos y claros.</p>"
                "<p><b>Por favor, no cambie:</b> los nombres, los números, los marcadores <code>{…}</code>, los "
                "separadores <code>|</code>, ni las palabras francesas entre « comillas » (son el francés que el alumno "
                "debe reconocer). El original francés aparece en gris solo como ayuda: no hace falta revisarlo.</p>",
        "ok": "Bien", "change": "Cambiar", "question": "Pregunta", "tout_ok": "Todo bien en esta sección",
        "fr": "Original en francés", "note": "Nota (en francés)", "ctx": "Contexto",
        "nom": "Su nombre", "general": "Comentarios generales (opcional)",
        "exporter": "Enviar mi revisión", "fichier": "Descargar como archivo",
        "fin": "Copiado. Péguelo en un correo para Daniel, o adjunte el archivo descargado.",
        "etat": "{f} de {n} revisados", "garde": "Su trabajo se guarda en este navegador: puede cerrar la página y volver.",
        "corr": "Su versión", "quest": "Su pregunta",
    },
}


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def _texte(o):
    return isinstance(o, dict) and o and set(o) <= {"fr", "en", "es"} and ({"en", "es"} & set(o)) \
        and all(isinstance(v, str) for v in o.values())


def items(langue):
    """[(section, id, texte, français, contexte)] pour une langue."""
    LX = _charger("hr_lexique", CONTENU / "lexique.py")
    planches = dict(LX.PLANCHES)
    col = {"en": 3, "es": 4}[langue]
    out = [("lexique", f"lexique.{m[0]}.{langue}", m[col], m[2], (planches.get(m[1], m[1]), m[6]))
           for m in LX.LEXIQUE]
    for f in FICHIERS:
        mod = _charger(f"hr_{f}", CONTENU / f"{f}.py")
        for var, val in vars(mod).items():
            if var.startswith("_") or var in ECARTES or callable(val) or not var.isupper():
                continue
            vus = set()

            def walk(o, chemin):
                if id(o) in vus:
                    return
                if _texte(o):
                    if langue in o and o[langue].strip():
                        out.append((f"{f}.{var}", f"{f}.{var}{chemin}.{langue}", o[langue], o.get("fr", ""), None))
                    return
                if isinstance(o, dict):
                    vus.add(id(o))
                    for k, v in o.items():
                        walk(v, f"{chemin}[{k}]")
                elif isinstance(o, (list, tuple)):
                    vus.add(id(o))
                    for i, v in enumerate(o):
                        walk(v, f"{chemin}[{i}]")
            walk(val, "")
    ordre = {s[0]: i for i, s in enumerate(SECTIONS)}
    inconnues = sorted({it[0] for it in out} - set(ordre))
    if inconnues:
        raise SystemExit(f"Sections sans nom dans SECTIONS : {inconnues}")
    return sorted(out, key=lambda it: ordre[it[0]])


CSS = """
:root{--ground:#F3EFE6;--card:#FFFFFF;--ink:#132A2C;--body:#223A3C;--muted:#5A6A6B;--line:#DFD8C9;
  --acier:#0F5E63;--acier-bg:#DDEDEC;--ok:#0A7A4E;--ok-bg:#DDF2E7;--q:#9A5B00;--q-bg:#FBEEDC;--mod:#8A3A1E;--mod-bg:#F8E5DC}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ground:#0F1A1B;--card:#152324;--ink:#EEF3F2;
  --body:#C6D3D2;--muted:#93A5A4;--line:#26393A;--acier:#7CC4C4;--acier-bg:#13302F;--ok:#6FD3A6;--ok-bg:#12352A;
  --q:#F0B45C;--q-bg:#3A2A12;--mod:#F0A184;--mod-bg:#3A2019}}
:root[data-theme="dark"]{--ground:#0F1A1B;--card:#152324;--ink:#EEF3F2;--body:#C6D3D2;--muted:#93A5A4;--line:#26393A;
  --acier:#7CC4C4;--acier-bg:#13302F;--ok:#6FD3A6;--ok-bg:#12352A;--q:#F0B45C;--q-bg:#3A2A12;--mod:#F0A184;--mod-bg:#3A2019}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);font-family:Nunito,-apple-system,'Segoe UI',sans-serif;
  font-size:16px;line-height:1.5;border-top:4px solid #C4613A}
.doc{max-width:860px;margin:0 auto;padding:32px 16px 80px}
h1{color:var(--ink);font-size:1.7rem;line-height:1.2;margin:0 0 8px}
h2{color:var(--ink);font-size:1.15rem;margin:34px 0 10px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:baseline}
h2 small{font-weight:600;color:var(--muted);font-size:.85rem}
code{font-size:.9em;background:var(--acier-bg);padding:0 4px;border-radius:4px}
.it{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:8px 0}
.it[data-e=ok]{border-left:5px solid var(--ok)} .it[data-e=change]{border-left:5px solid var(--mod)}
.it[data-e=question]{border-left:5px solid var(--q)}
.t{color:var(--ink);font-size:1.05rem;font-weight:700;white-space:pre-wrap;overflow-wrap:anywhere}
.fr,.ctx{color:var(--muted);font-size:.88rem;margin-top:4px;overflow-wrap:anywhere}
.b{display:flex;gap:8px;flex-wrap:wrap;margin-top:10px}
button{font:inherit;font-weight:700;cursor:pointer;border:1px solid var(--line);background:var(--ground);color:var(--body);
  border-radius:10px;padding:6px 12px;min-height:40px}
button[aria-pressed=true][data-v=ok]{background:var(--ok-bg);border-color:var(--ok);color:var(--ink)}
button[aria-pressed=true][data-v=change]{background:var(--mod-bg);border-color:var(--mod);color:var(--ink)}
button[aria-pressed=true][data-v=question]{background:var(--q-bg);border-color:var(--q);color:var(--ink)}
button.tout{font-size:.85rem;min-height:34px;padding:4px 10px}
textarea,input[type=text]{font:inherit;width:100%;padding:8px 10px;border:1px solid var(--line);border-radius:8px;
  background:var(--card);color:var(--ink);margin-top:8px}
.zone{display:none}.it[data-e=change] .zone.c,.it[data-e=question] .zone.q{display:block}
.zone label{font-size:.85rem;font-weight:700;color:var(--muted)}
.bas{position:sticky;bottom:0;background:var(--ground);border-top:1px solid var(--line);padding:10px 0;margin-top:30px}
.pri{background:var(--acier);color:#fff;border-color:var(--acier)}
.etat{color:var(--muted);margin-left:8px}
"""


def page_relecteur(langue):
    T = TXT[langue]
    its = items(langue)
    n_mots = sum(len(re.findall(r"\w+", it[2])) for it in its)
    heures = max(1, round(n_mots / 1400 + len(its) / 400))   # ~1 400 mots relus à l'heure, et le geste par texte
    h = (f"{heures} hour{'s' if heures > 1 else ''}" if langue == "en" else f"{heures} hora{'s' if heures > 1 else ''}")
    nom_s = {s[0]: (s[1] if langue == "en" else s[2]) for s in SECTIONS}
    corps, courante = "", None
    for sec, i, texte, fr, ctx in its:
        if sec != courante:
            nb = sum(1 for x in its if x[0] == sec)
            corps += (f'<h2 id="s-{E(sec)}"><span>{E(nom_s[sec])}</span><small>{nb} · '
                      f'<button type="button" class="tout" data-s="{E(sec)}">{E(T["tout_ok"])}</button></small></h2>')
            courante = sec
        extra = ""
        if ctx:
            extra = f'<div class="ctx">{E(T["ctx"])} : {E(ctx[0])}{" · " + E(T["note"]) + " : " + E(ctx[1]) if ctx[1] else ""}</div>'
        fr_html = f'<div class="fr" lang="fr">{E(T["fr"])} : {E(fr)}</div>' if fr else ""
        corps += (f'<div class="it" data-id="{E(i)}" data-s="{E(sec)}"><div class="t" lang="{langue}">{E(texte)}</div>'
                  f'{fr_html}{extra}'
                  f'<div class="b"><button type="button" data-v="ok">{E(T["ok"])}</button>'
                  f'<button type="button" data-v="change">{E(T["change"])}</button>'
                  f'<button type="button" data-v="question">{E(T["question"])}</button></div>'
                  f'<div class="zone c"><label>{E(T["corr"])}</label><textarea rows="2" data-c="{E(i)}"></textarea></div>'
                  f'<div class="zone q"><label>{E(T["quest"])}</label><textarea rows="2" data-q="{E(i)}"></textarea></div></div>')
    originaux = {i: texte for _, i, texte, _, _ in its}
    page = f"""<!doctype html><html lang="{langue}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>{E(T["titre"])}</title><style>{CSS}</style></head><body><div class="doc">
<h1>{E(T["titre"])}</h1>
<p><b>{E(T["chapeau"].format(h=h, n=len(its), m=n_mots))}</b> {E(T["garde"])}</p>
{T["quoi"]}
<p><label><b>{E(T["nom"])}</b><input type="text" id="nom"></label></p>
{corps}
<h2>{E(T["general"])}</h2><textarea id="general" rows="4"></textarea>
<div class="bas"><button type="button" class="pri" id="exporter">{E(T["exporter"])}</button>
<button type="button" id="fichier">{E(T["fichier"])}</button><span class="etat" id="etat"></span></div>
</div>
<script>
(function(){{
var L='{langue}', CLE='hotellerie-relecture-'+L, O={json.dumps(originaux, ensure_ascii=False)}, T={json.dumps(T, ensure_ascii=False)};
var s={{e:{{}},c:{{}},q:{{}},nom:'',general:''}};
try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.e)s=l;}}catch(e){{}}
function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
var its=[].slice.call(document.querySelectorAll('.it')), N=its.length;
function peindre(){{
  its.forEach(function(d){{var e=s.e[d.dataset.id]||'';d.dataset.e=e;
    d.querySelectorAll('.b button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.v===e);}});}});
  document.getElementById('etat').textContent=T.etat.replace('{{f}}',Object.keys(s.e).length).replace('{{n}}',N);
}}
document.addEventListener('click',function(ev){{
  var b=ev.target.closest('.b button');
  if(b){{var d=b.closest('.it'),id=d.dataset.id;
    if(s.e[id]===b.dataset.v)delete s.e[id];else{{s.e[id]=b.dataset.v;
      if(b.dataset.v==='change'&&!s.c[id]){{s.c[id]=O[id];d.querySelector('[data-c]').value=O[id];}}}}
    sv();peindre();return;}}
  var t=ev.target.closest('button.tout');
  if(t){{its.forEach(function(d){{if(d.dataset.s===t.dataset.s&&!s.e[d.dataset.id])s.e[d.dataset.id]='ok';}});sv();peindre();}}
}});
document.querySelectorAll('[data-c]').forEach(function(x){{x.value=s.c[x.dataset.c]||'';x.oninput=function(){{s.c[x.dataset.c]=x.value;sv();}};}});
document.querySelectorAll('[data-q]').forEach(function(x){{x.value=s.q[x.dataset.q]||'';x.oninput=function(){{s.q[x.dataset.q]=x.value;sv();}};}});
['nom','general'].forEach(function(k){{var x=document.getElementById(k);x.value=s[k]||'';x.oninput=function(){{s[k]=x.value;sv();}};}});
function sortie(){{
  var out={{page:'hotellerie-relecture',langue:L,date:new Date().toISOString().slice(0,10),relecteur:s.nom||'',
    revus:Object.keys(s.e).length,total:N,ok:0,corrections:{{}},questions:{{}},general:s.general||''}};
  Object.keys(s.e).forEach(function(id){{var e=s.e[id];
    if(e==='ok')out.ok++;
    else if(e==='change'&&(s.c[id]||'')!==O[id])out.corrections[id]={{avant:O[id],apres:s.c[id]||''}};
    else if(e==='change')out.ok++;
    if(e==='question')out.questions[id]={{texte:O[id],question:s.q[id]||''}};}});
  return JSON.stringify(out,null,2);
}}
document.getElementById('exporter').onclick=function(){{var t=sortie();
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{document.getElementById('etat').textContent=T.fin;}},
  function(){{prompt('',t);}});}};
document.getElementById('fichier').onclick=function(){{var a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([sortie()],{{type:'application/json'}}));a.download='review-hotel-'+L+'.json';a.click();}};
peindre();
}})();
</script></body></html>"""
    DEST_R.mkdir(parents=True, exist_ok=True)
    (DEST_R / f"{langue}.html").write_text(page, encoding="utf-8")
    return len(its), n_mots, heures


COURRIEL = {
    "en": ("Review of English phrases for a hotel training kit (about {h} h)",
           "Hi,\n\nI'm building a training kit for hotel front-desk employees in Quebec: some of them are learning "
           "English. Before it is used, I need a native speaker to check that the English sounds natural "
           "(North American, at a hotel front desk).\n\nThere are {n} short texts, about {m} words in all — roughly "
           "{h} hours. Everything is on one page; you mark each text OK, Change or Question, and your work is saved "
           "as you go:\n{url}\n\nWhen you're done, click \"Send my review\" and paste the result into a reply to this "
           "email (or attach the downloaded file).\n\nThank you!\nDaniel"),
    "es": ("Revisión de frases en español para un material de formación hotelera (unas {h} h)",
           "Hola:\n\nEstoy preparando un material de formación para recepcionistas de hotel en Quebec; algunos "
           "hablan español. Antes de usarlo, necesito que un hablante nativo revise que el español suene natural "
           "(español de México, en la recepción de un hotel, de usted).\n\nSon {n} textos cortos, unas {m} palabras "
           "en total: aproximadamente {h} horas. Todo está en una sola página; usted marca cada texto Bien, Cambiar o "
           "Pregunta, y su trabajo se guarda a medida que avanza:\n{url}\n\nAl terminar, haga clic en «Enviar mi "
           "revisión» y pegue el resultado en una respuesta a este correo (o adjunte el archivo descargado).\n\n"
           "¡Muchas gracias!\nDaniel"),
}


def page_daniel(chiffres):
    blocs = ""
    for l, nom in (("en", "l'anglais"), ("es", "l'espagnol")):
        n, m, h = chiffres[l]
        url = ADRESSE.format(l=l)
        sujet, texte = COURRIEL[l]
        texte = texte.format(n=n, m=m, h=h, url=url)
        sujet = sujet.format(h=h)
        blocs += f"""<section class="dec2"><h2>Relire {nom}</h2>
<p>{n} textes, {m} mots, environ {h} h de travail. Page du relecteur :
<a href="/modules-autonomes/hotel-relecture/{l}.html" target="_blank" rel="noopener">{url}</a>.</p>
<p><b>Objet :</b> <span id="s-{l}">{E(sujet)}</span> <button type="button" class="btn-export" data-copie="s-{l}">Copier l'objet</button></p>
<pre id="c-{l}" class="courriel">{E(texte)}</pre>
<p><button type="button" class="btn-export" data-copie="c-{l}">Copier le courriel</button> <span class="etat" id="e-c-{l}"></span></p>
</section>"""
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Hôtel Rive-Claire — la relecture</title>", tete)
    RIVE = _charger("hr_rive", RACINE / "build" / "hotel_rive.py")
    tete = tete.replace("</style>", RIVE.CSS + """
.dec2{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.courriel{white-space:pre-wrap;background:var(--sunken);border:1px solid var(--line);border-radius:10px;padding:12px;
  font-family:inherit;font-size:15px;color:var(--body);overflow-wrap:anywhere}
.btn-export{font:inherit;font-weight:700;cursor:pointer;background:var(--acier);color:#fff;border:0;border-radius:10px;padding:8px 14px}
.etat{margin-left:10px;color:var(--muted);font-size:15px}
</style>""", 1)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; avant la vente</p>
<h1>La relecture de l'anglais et de l'espagnol</h1>
<p class="chapeau">Tous les textes anglais et espagnols de la trousse ont été écrits sans locuteur. L'écran et les
fiches le disent (« non relu »). Une personne par langue relit tout, sur une page dans <b>sa</b> langue, et vous
renvoie un fichier.</p>

<section>
  <h2>Qui chercher</h2>
  <ul class="simple">
    <li><b>Anglais</b> : une personne dont c'est la langue maternelle, <b>nord-américaine</b> ; idéalement quelqu'un qui a
    travaillé à l'accueil (hôtel, restaurant, service à la clientèle).</li>
    <li><b>Espagnol</b> : une personne <b>mexicaine</b> (la variété choisie pour la trousse), à l'aise avec le vouvoiement
    (« usted ») du service.</li>
    <li>Un étudiant ou un collègue fait l'affaire. La relecture porte sur le naturel des phrases, pas sur la pédagogie.
    Prévoir une rétribution ou un échange : c'est une demi-journée.</li>
  </ul>
</section>

{blocs}

<section>
  <h2>Au retour</h2>
  <ol class="simple">
    <li>Recollez-moi le texte reçu (ou le fichier). Chaque correction porte l'identifiant exact du texte : elle se pose
    à sa place dans <code>build/contenu/entreprise-hotel/</code>, sans chercher.</li>
    <li>Je vous montre les corrections qui touchent <b>une phrase dite</b> (mots, clients, répliques, test) : ces phrases
    ont leur voix, qu'il faudra refaire. C'est votre feu vert pour les voix, extrait par extrait.</li>
    <li>La mention « non relu » tombe pour cette langue, sur l'écran et sur les fiches de poche.</li>
  </ol>
  <div class="reserve"><p><strong>Les pages de relecture sont hors du classeur</strong>, qui est fermé par mot de passe :
  le relecteur les ouvre sans rien demander. Elles ne sont liées nulle part sur le site, demandent aux moteurs de
  recherche de ne pas les indexer, et ne portent que le contenu de la trousse — déjà public dans l'écran de
  l'employé —, aucun nom réel.</p></div>
</section>

<div class="pied"><p>Pages produites par <code>build/hotel_relecture.py</code> — ne pas les éditer.</p></div>
</div>
<script>
document.addEventListener('click',function(e){{var b=e.target.closest('[data-copie]');if(!b)return;
  var t=document.getElementById(b.dataset.copie).textContent, et=document.getElementById('e-'+b.dataset.copie);
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{if(et)et.textContent='Copié.';}},function(){{prompt('Copiez :',t);}});}});
</script></body></html>"""
    (DEST / "hotellerie-relecture.html").write_text(tete + corps, encoding="utf-8")


def main():
    chiffres = {l: page_relecteur(l) for l in ("en", "es")}
    page_daniel(chiffres)
    for l, (n, m, h) in chiffres.items():
        print(f"  {l} : {n} textes, {m} mots, ~{h} h")
    print("assets/presentations/hotellerie-relecture.html + modules-autonomes/hotel-relecture/{en,es}.html")


if __name__ == "__main__":
    main()
