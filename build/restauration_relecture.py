#!/usr/bin/env python3
"""La relecture des onze langues d'appui de Chez Jocelyne, par des locuteurs.

    python3 build/restauration_relecture.py
      → assets/presentations/restauration/restauration-relecture.html   (pour Daniel : le courriel, le suivi)
      → modules-autonomes/restaurant-relecture/<langue>.html             (une page par langue, pour le relecteur)
    python3 build/restauration_relecture.py --appliquer retour.json        (pose les corrections d'un relecteur)

CE QUI CHANGE PAR RAPPORT À L'HÔTEL (build/hotel_relecture.py, le modèle) : là-bas,
l'anglais et l'espagnol étaient ÉCRITS dans leur langue, et le relecteur jugeait
leur naturel. Ici, ce sont des TRADUCTIONS du français, faites par un modèle
(l'API, puis des sous-agents quand le crédit a manqué). Le relecteur doit donc lire
le français pour juger : il est BILINGUE, et sa page est en français. Le français
d'origine n'est plus une aide grisée, c'est la référence.

L'ALLERGIE D'ABORD : la règle, les gestes, les « pourquoi », le critère de
gravité et la réponse de la cuisine forment une première partie, à relire en
priorité — c'est ce qu'un employé lit pour une décision éliminatoire. Le reste
(les mots, l'écran) vient ensuite, et peut se relire plus tard.

Les pages des relecteurs sont HORS du classeur (fermé par mot de passe), non liées,
« noindex », et ne portent que le contenu de la trousse, déjà public dans l'écran.
Chaque texte porte un identifiant stable (mots.<id>.mot, mots.<id>.note,
interface.<clé>) : l'export revient avec eux, `--appliquer` pose la correction à
sa place dans traductions.json, et une langue relue en entier perd sa mention
« non relue ».
"""
import html, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
TRAD = CONTENU / "traductions.json"
DEST = RACINE / "assets" / "presentations" / "restauration"
DEST_R = RACINE / "modules-autonomes" / "restaurant-relecture"
ADRESSE = "https://portail.edufrancis.ca/modules-autonomes/restaurant-relecture/{l}.html"
E = html.escape
sys.path.insert(0, str(CONTENU)); sys.path.insert(0, str(RACINE / "build"))
import lexique as LX  # noqa: E402
import identite as ID  # noqa: E402
from restaurant_traductions import INTERFACE, NOMS  # noqa: E402

NOM_FR = {"ar": "l'arabe", "es": "l'espagnol", "uk": "l'ukrainien", "fa": "le persan", "zh": "le chinois",
          "pt": "le portugais", "en": "l'anglais", "ro": "le roumain", "ur": "l'ourdou", "ru": "le russe",
          "ti": "le tigrigna"}
ALLERGIE = ("regle_", "critere_grave", "acte_", "pourquoi_", "rc_", "grave", "c_ratee", "c_reussie", "ex_allergie",
            "seuil_allergie", "partC")
PARTIES = [("allergie", "1. L'allergie — à relire en priorité"), ("mots", "2. Les mots du restaurant"),
           ("ecran", "3. Les textes de l'écran")]


def est_allergie(k):
    return any(k.startswith(p) for p in ALLERGIE)


def items(langue):
    """[(partie, id, traduction, français, contexte)]."""
    t = json.loads(TRAD.read_text(encoding="utf-8"))[langue]
    planches = {k: ti for k, ti, _ in LX.PLANCHES}
    out = []
    for k, fr in INTERFACE.items():
        if est_allergie(k):
            out.append(("allergie", f"interface.{k}", t["interface"][k], fr, None))
    for e in LX.LEXIQUE:
        m = t["mots"][e[0]]
        ctx = planches[e[1]] + (f" · on entend aussi « {e[3]} »" if e[3] else "")
        out.append(("mots", f"mots.{e[0]}.mot", m["mot"], e[2], ctx))
        if e[5]:
            out.append(("mots", f"mots.{e[0]}.note", m["note"], e[5], f"la note de « {e[2]} »"))
    for k, fr in INTERFACE.items():
        if not est_allergie(k):
            out.append(("ecran", f"interface.{k}", t["interface"][k], fr, None))
    return out


CSS = """
:root{--ground:#F5F0EA;--card:#FFFFFF;--ink:#241A14;--body:#3A2E26;--muted:#6B5D53;--line:#E4DAD0;
  --acier:#8A2E1C;--acier-bg:#F3E3DC;--ok:#0A7A4E;--ok-bg:#DDF2E7;--q:#9A5B00;--q-bg:#FBEEDC;--mod:#8A3A1E;--mod-bg:#F8E5DC}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--ground:#1A1411;--card:#241C17;--ink:#F3ECE6;
  --body:#D9CCC2;--muted:#A8998D;--line:#3A2E26;--acier:#E8957F;--acier-bg:#3A221A;--ok:#6FD3A6;--ok-bg:#12352A;
  --q:#F0B45C;--q-bg:#3A2A12;--mod:#F0A184;--mod-bg:#3A2019}}
:root[data-theme="dark"]{--ground:#1A1411;--card:#241C17;--ink:#F3ECE6;--body:#D9CCC2;--muted:#A8998D;--line:#3A2E26;
  --acier:#E8957F;--acier-bg:#3A221A;--ok:#6FD3A6;--ok-bg:#12352A;--q:#F0B45C;--q-bg:#3A2A12;--mod:#F0A184;--mod-bg:#3A2019}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);font-family:Nunito,-apple-system,'Segoe UI',sans-serif;
  font-size:16px;line-height:1.5;border-top:4px solid #8A2E1C}
.doc{max-width:860px;margin:0 auto;padding:32px 16px 80px}
h1{color:var(--ink);font-size:1.7rem;line-height:1.2;margin:0 0 8px}
h2{color:var(--ink);font-size:1.15rem;margin:34px 0 10px;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap;align-items:baseline}
h2 small{font-weight:600;color:var(--muted);font-size:.85rem}
.prio{border:2px solid var(--acier);border-radius:12px;padding:10px 14px;background:var(--acier-bg)}
.it{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin:8px 0}
.it[data-e=ok]{border-left:5px solid var(--ok)} .it[data-e=change]{border-left:5px solid var(--mod)}
.it[data-e=question]{border-left:5px solid var(--q)}
.fr{color:var(--ink);font-size:.95rem;overflow-wrap:anywhere}
.t{color:var(--ink);font-size:1.12rem;font-weight:700;white-space:pre-wrap;overflow-wrap:anywhere;margin-top:4px}
.t[dir=rtl]{text-align:right}
.ctx{color:var(--muted);font-size:.85rem;margin-top:4px}
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
    its = items(langue)
    rtl = NOMS[langue][2]
    d = ' dir="rtl"' if rtl else ""
    n_mots = sum(len(re.findall(r"\w+", it[3])) for it in its)
    n_prio = sum(1 for it in its if it[0] == "allergie")
    m_prio = sum(len(re.findall(r"\w+", it[3])) for it in its if it[0] == "allergie")
    heures = max(1, round(n_mots / 1000 + len(its) / 300))      # ~1 000 mots comparés à l'heure, et le geste par texte
    h_prio = max(1, round(m_prio / 1000 + n_prio / 300))
    nom_p = dict(PARTIES)
    corps, courante = "", None
    for part, i, texte, fr, ctx in its:
        if part != courante:
            nb = sum(1 for x in its if x[0] == part)
            corps += (f'<h2 id="p-{part}"><span>{E(nom_p[part])}</span><small>{nb} textes · '
                      f'<button type="button" class="tout" data-s="{part}">Tout est juste dans cette partie</button></small></h2>')
            courante = part
        corps += (f'<div class="it" data-id="{E(i)}" data-s="{part}"><div class="fr" lang="fr"><b>Français :</b> {E(fr)}</div>'
                  f'<div class="t" lang="{langue}"{d}>{E(texte)}</div>'
                  + (f'<div class="ctx">{E(ctx)}</div>' if ctx else "")
                  + '<div class="b"><button type="button" data-v="ok">Juste</button>'
                  '<button type="button" data-v="change">À corriger</button>'
                  '<button type="button" data-v="question">Question</button></div>'
                  f'<div class="zone c"><label>Votre version</label><textarea rows="2" data-c="{E(i)}"{d}></textarea></div>'
                  f'<div class="zone q"><label>Votre question</label><textarea rows="2" data-q="{E(i)}"></textarea></div></div>')
    originaux = {i: texte for _, i, texte, _, _ in its}
    loc = NOMS[langue][1]
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex">
<title>Relecture — {E(loc)} — {E(ID.NOM)}</title><style>{CSS}</style></head><body><div class="doc">
<h1>Relecture de {E(NOM_FR[langue])} <span lang="{langue}"{d}>({E(loc)})</span></h1>
<p><b>Merci de relire ceci.</b> {len(its)} textes courts, {n_mots} mots de français en tout : environ {heures} h.
<b>La première partie, l'allergie, est la plus importante</b> ({n_prio} textes, environ {h_prio} h) : si vous n'avez
le temps que pour elle, c'est déjà beaucoup. Votre travail se garde dans ce navigateur : vous pouvez fermer la page et revenir.</p>
<p><b>De quoi il s'agit.</b> Une formation pour des employés de restaurant au Québec (cuisine et salle) qui
<b>apprennent le français</b>. Votre langue s'affiche en petit, sous le français, pour les aider à comprendre. Le
restaurant, « {E(ID.NOM)} », est inventé. Ces traductions ont été faites par un programme : nous avons besoin d'une
personne qui lit le français et {E(NOM_FR[langue])} pour dire si elles sont justes et naturelles.</p>
<p><b>Ce que nous vous demandons.</b> Pour chaque texte : la traduction dit-elle la même chose que le français, dans
des mots simples qu'un employé comprend du premier coup ? Pour l'allergie, la justesse compte plus que tout : un
employé doit comprendre exactement ce qu'il doit faire.</p>
<p><b>Ne changez pas :</b> les mots français entre « guillemets » (c'est le français que l'employé doit reconnaître ou
dire), les noms de plats d'ici laissés en français (poutine, pâté chinois…), les nombres et les marques comme %n.</p>
<p><label><b>Votre prénom (facultatif)</b><input type="text" id="nom"></label></p>
<div class="prio"><p style="margin:0"><b>Commencez par la partie 1.</b> Le bouton « Tout est juste dans cette partie »
marque d'un coup ce qui reste ; vous pouvez ensuite changer un texte.</p></div>
{corps}
<h2>Remarques générales (facultatif)</h2><textarea id="general" rows="4"></textarea>
<div class="bas"><button type="button" class="pri" id="exporter">Envoyer ma relecture</button>
<button type="button" id="fichier">Télécharger le fichier</button><span class="etat" id="etat"></span></div>
</div>
<script>
(function(){{
var L='{langue}', CLE='restaurant-relecture-'+L, O={json.dumps(originaux, ensure_ascii=False)};
var s={{e:{{}},c:{{}},q:{{}},nom:'',general:''}};
try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.e)s=l;}}catch(e){{}}
function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
var its=[].slice.call(document.querySelectorAll('.it')), N=its.length;
function peindre(){{
  its.forEach(function(d){{var e=s.e[d.dataset.id]||'';d.dataset.e=e;
    d.querySelectorAll('.b button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.v===e);}});}});
  document.getElementById('etat').textContent=Object.keys(s.e).length+' sur '+N+' relus';
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
  var out={{page:'restaurant-relecture',langue:L,date:new Date().toISOString().slice(0,10),relecteur:s.nom||'',
    revus:Object.keys(s.e).length,total:N,ok:0,corrections:{{}},questions:{{}},general:s.general||''}};
  Object.keys(s.e).forEach(function(id){{var e=s.e[id];
    if(e==='ok')out.ok++;
    else if(e==='change'&&(s.c[id]||'')!==O[id])out.corrections[id]={{avant:O[id],apres:s.c[id]||''}};
    else if(e==='change')out.ok++;
    if(e==='question')out.questions[id]={{texte:O[id],question:s.q[id]||''}};}});
  return JSON.stringify(out,null,2);
}}
document.getElementById('exporter').onclick=function(){{var t=sortie();
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{document.getElementById('etat').textContent='Copié. Collez-le dans un courriel à Daniel, ou joignez le fichier téléchargé.';}},
  function(){{prompt('',t);}});}};
document.getElementById('fichier').onclick=function(){{var a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([sortie()],{{type:'application/json'}}));a.download='relecture-restaurant-'+L+'.json';a.click();}};
peindre();
}})();
</script></body></html>"""
    DEST_R.mkdir(parents=True, exist_ok=True)
    (DEST_R / f"{langue}.html").write_text(page, encoding="utf-8")
    return len(its), n_mots, heures, n_prio, h_prio


SUJET = "Relecture d'une traduction en {nom} pour une formation en restauration (environ {h} h)"
COURRIEL = (
    "Bonjour,\n\n"
    "Je prépare une formation pour des employés de restaurant au Québec qui apprennent le français. Sous chaque phrase "
    "en français, une aide s'affiche dans leur langue. Ces aides ont été traduites par un programme, et avant de les "
    "montrer à des employés, j'ai besoin qu'une personne qui lit le français et {nom} vérifie qu'elles sont justes "
    "et faciles à comprendre.\n\n"
    "Tout est sur une page : pour chaque texte, vous voyez le français et la traduction, et vous cochez « Juste », "
    "« À corriger » ou « Question ». Votre travail se garde au fur et à mesure.\n{url}\n\n"
    "Il y a {n} textes courts (environ {h} h en tout). La première partie, sur les allergies, est la plus importante : "
    "{p} textes, environ {hp} h. Si vous n'avez le temps que pour elle, c'est déjà très précieux.\n\n"
    "À la fin, cliquez sur « Envoyer ma relecture » et collez le résultat dans une réponse à ce courriel (ou joignez "
    "le fichier téléchargé).\n\n"
    "Merci beaucoup !\nDaniel")


def page_daniel(chiffres):
    lignes, blocs = "", ""
    _n, _m, h, _p, hp = chiffres[ID.LANGUES_APPUI[0]]
    for l in ID.LANGUES_APPUI:
        n, m, h, p, hp = chiffres[l]
        url = ADRESSE.format(l=l)
        lignes += (f"<tr><td><b>{E(NOM_FR[l][0].upper() + NOM_FR[l][1:])}</b> <span lang=\"{l}\">({E(NOMS[l][1])})</span></td>"
                   f"<td class=\"num\">{p}</td><td class=\"num\">≈ {hp} h</td><td class=\"num\">{n}</td><td class=\"num\">≈ {h} h</td>"
                   f"<td><a href=\"/modules-autonomes/restaurant-relecture/{l}.html\" target=\"_blank\" rel=\"noopener\">page</a></td></tr>")
        texte = COURRIEL.format(nom=NOM_FR[l], url=url, n=n, h=h, p=p, hp=hp)
        sujet = SUJET.format(nom=NOM_FR[l], h=h)
        blocs += f"""<details class="dec2"><summary><b>{E(NOM_FR[l][0].upper() + NOM_FR[l][1:])}</b> — le courriel</summary>
<p><b>Objet :</b> <span id="s-{l}">{E(sujet)}</span> <button type="button" class="btn-export" data-copie="s-{l}">Copier l'objet</button></p>
<pre id="c-{l}" class="courriel">{E(texte)}</pre>
<p><button type="button" class="btn-export" data-copie="c-{l}">Copier le courriel</button> <span class="etat" id="e-c-{l}"></span></p>
</details>"""
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", f"<title>{E(ID.NOM)} — la relecture des langues</title>", tete)
    tete = tete.replace("</style>", """
.dec2{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:10px 0}
.dec2 summary{cursor:pointer;min-height:40px;display:flex;align-items:center}
.courriel{white-space:pre-wrap;background:var(--sunken,#F4F1EC);border:1px solid var(--line);border-radius:10px;padding:12px;
  font-family:inherit;font-size:15px;color:var(--body);overflow-wrap:anywhere}
.btn-export{font:inherit;font-weight:700;cursor:pointer;background:var(--acier);color:#fff;border:0;border-radius:10px;padding:8px 14px}
.etat{margin-left:10px;color:var(--muted);font-size:15px}
table.cmp{display:table;width:100%;min-width:0}
</style>""", 1)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{E(ID.NOM)} &middot; avant le pilote</p>
<h1>La relecture des onze langues</h1>
<p class="chapeau">Les onze langues d'appui ont été traduites par un modèle, sans locuteur. L'écran et les fiches le
disent (« non relue »). Une personne <b>bilingue — le français et sa langue</b> — relit, sur une page en français où
chaque texte montre l'original et sa traduction, et vous renvoie un fichier. <b>L'allergie vient en premier</b> : c'est
ce qu'un employé lit pour une décision éliminatoire.</p>

<section>
  <h2>Qui chercher</h2>
  <ul class="simple">
    <li>Une personne qui lit <b>le français et la langue</b> : il faut comparer, pas seulement juger le naturel. Un
    employé bilingue, un collègue, un étudiant, un organisme d'accueil des personnes immigrantes.</li>
    <li>D'abord les langues <b>des employés du pilote</b> : inutile de payer onze relectures avant de savoir qui viendra.</li>
    <li>Le temps : l'allergie seule, environ {hp} h ; tout, environ {h} h (estimation : un millier de mots comparés à
    l'heure). La rétribution est à convenir ; elle reste un ordre de grandeur à vérifier.</li>
  </ul>
</section>

<section>
  <h2>Les onze pages</h2>
  <table class="cmp"><thead><tr><th>Langue</th><th>Allergie</th><th></th><th>Tout</th><th></th><th></th></tr></thead>
  <tbody>{lignes}</tbody></table>
</section>

<section>
  <h2>Les courriels, prêts à copier</h2>
  <p>En français, puisque la personne doit lire le français. Un par langue, avec son lien.</p>
  {blocs}
</section>

<section>
  <h2>Au retour</h2>
  <ol class="simple">
    <li>Recollez-moi le texte reçu (ou le fichier). Chaque correction porte l'identifiant exact du texte
    (<code>mots.poele.mot</code>, <code>interface.regle_1</code>…) : <code>python3 build/restauration_relecture.py --appliquer</code>
    la pose à sa place dans <code>traductions.json</code>, sans chercher.</li>
    <li>Je vous montre les questions du relecteur, qui demandent souvent votre avis sur le français lui-même.</li>
    <li>Une langue relue <b>en entier</b> perd sa mention « non relue », à l'écran et sur sa fiche de poche. Rien à
    refaire côté voix : seul le français se dit.</li>
  </ol>
  <div class="reserve"><p><strong>Les pages de relecture sont hors du classeur</strong>, qui est fermé par mot de passe :
  le relecteur les ouvre sans rien demander. Elles ne sont liées nulle part sur le site, demandent aux moteurs de
  recherche de ne pas les indexer, et ne portent que le contenu de la trousse — déjà public dans l'écran de
  l'employé —, aucun nom réel.</p></div>
</section>

<div class="pied"><p>Pages produites par <code>build/restauration_relecture.py</code> — ne pas les éditer.</p></div>
</div>
<script>
document.addEventListener('click',function(e){{var b=e.target.closest('[data-copie]');if(!b)return;
  var t=document.getElementById(b.dataset.copie).textContent, et=document.getElementById('e-'+b.dataset.copie);
  (navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{if(et)et.textContent='Copié.';}},function(){{prompt('Copiez :',t);}});}});
</script></body></html>"""
    (DEST / "restauration-relecture.html").write_text(tete + corps, encoding="utf-8")


def appliquer(chemin):
    r = json.loads(pathlib.Path(chemin).read_text(encoding="utf-8"))
    l = r["langue"]
    data = json.loads(TRAD.read_text(encoding="utf-8"))
    t = data[l]
    n = 0
    for i, c in r.get("corrections", {}).items():
        parts = i.split(".")
        if parts[0] == "interface":
            t["interface"][parts[1]] = c["apres"].strip(); n += 1
        elif parts[0] == "mots":
            t["mots"][parts[1]][parts[2]] = c["apres"].strip(); n += 1
    if r.get("revus") == r.get("total") and not r.get("questions"):
        t["relu"] = True
    t.setdefault("relectures", []).append({"date": r.get("date"), "revus": r.get("revus"), "total": r.get("total"),
                                           "corrections": n, "questions": len(r.get("questions", {}))})
    TRAD.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  {l} : {n} corrections posées · relue en entier : {t['relu']}")
    for i, q in r.get("questions", {}).items():
        print(f"  ? {i} — {q['question']}")


def main():
    if "--appliquer" in sys.argv:
        return appliquer(sys.argv[sys.argv.index("--appliquer") + 1])
    chiffres = {l: page_relecteur(l) for l in ID.LANGUES_APPUI}
    page_daniel(chiffres)
    for l, (n, m, h, p, hp) in chiffres.items():
        print(f"  {l} : {n} textes ({p} sur l'allergie), {m} mots, ~{h} h (allergie ~{hp} h)")


if __name__ == "__main__":
    main()
