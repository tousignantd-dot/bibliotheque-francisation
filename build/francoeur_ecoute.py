#!/usr/bin/env python3
"""Le contrôle des voix de la Maison Francœur — retranscrire, comparer, écouter.

    python3 build/francoeur_ecoute.py          # retranscrit tout, écrit la page
    python3 build/francoeur_ecoute.py --page   # réécrit la page sans rien retranscrire

POURQUOI : les voix sont en Azure HD (décision du 24 septembre 2026), et la HD
n'est pas déterministe — deux tirages du même texte ne sonnent pas pareil — et
choisit sa langue mot à mot. On ne peut pas tout réécouter à chaque tirage.
Alors on fait RETRANSCRIRE chaque MP3 par la reconnaissance d'Azure (fr-CA,
audio court) et on compare au texte attendu. Ce qui s'écarte, ou dont la
confiance est basse, monte en tête de la page d'écoute.

LIMITE, à dire : la reconnaissance écrit en français ce qu'elle entend. Un
« rose » dit à l'anglaise peut encore s'écrire « rose ». La confiance basse
attrape une partie de ces cas, pas tous — la page sert à ÉCOUTER, le chiffre
ne fait que trier.

Sortie : build/contenu/entreprise-francoeur/ecoute.json (le relevé) et
assets/presentations/francoeur-ecoute.html (produite, jamais éditée).
"""
import difflib, html, json, pathlib, re, subprocess, sys, tempfile, unicodedata
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
import azure_voix  # noqa: E402
from lexique import LEXIQUE  # noqa: E402
from demandes import DEMANDES  # noqa: E402
import test as TEST  # noqa: E402

SONS = RACINE / "assets" / "interactive" / "francoeur" / "sons"
RELEVE = CONTENU / "ecoute.json"
PAGE = RACINE / "assets" / "presentations" / "francoeur-ecoute.html"
SEUIL_SIMILITUDE, SEUIL_CONFIANCE = 0.75, 0.60


def attendus():
    """Tout ce que produit le script des voix — la même liste, une seule source.
    On compare au texte AFFICHÉ (le lexique), pas à la graphie de prononciation
    envoyée à la voix (« rôse » se retranscrit « rose »)."""
    import audio_francoeur as AF
    affiche = {f"{e[0]}.mp3": e[2] for e in LEXIQUE}
    out = []
    for chemin, texte, _role, _taux in AF.travaux():
        famille = chemin.split("/")[0] if "/" in chemin else "mot"
        out.append((f"sons/{chemin}", famille, affiche.get(chemin, texte)))
    return out


def plat(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t.replace("'", " ")).split()


def retranscrire(mp3, cle, region):
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp3), "-ac", "1",
                        "-ar", "16000", "-sample_fmt", "s16",
                        # Un mot seul est trop court pour la reconnaissance : sans
                        # silence autour, elle ne rend souvent rien du tout.
                        "-af", "adelay=500:all=1,apad=pad_dur=0.5", w.name], check=True)
        out = subprocess.run(
            ["curl", "-s", "-m", "60", "-X", "POST",
             "-H", "Ocp-Apim-Subscription-Key: %s" % cle,
             "-H", "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000",
             "--data-binary", "@%s" % w.name,
             "https://%s.stt.speech.microsoft.com/speech/recognition/conversation/"
             "cognitiveservices/v1?language=fr-CA&format=detailed" % region],
            capture_output=True, text=True, check=True)
    d = json.loads(out.stdout or "{}")
    best = (d.get("NBest") or [{}])[0]
    return d.get("DisplayText", ""), float(best.get("Confidence", 0) or 0)


def controle():
    cle, region = azure_voix.cle_region()

    def un(a):
        chemin, famille, texte = a
        entendu, conf = retranscrire(SONS.parent / chemin, cle, region)
        sim = difflib.SequenceMatcher(None, plat(texte), plat(entendu)).ratio()
        return {"fichier": chemin, "famille": famille, "attendu": texte, "entendu": entendu,
                "similitude": round(sim, 2), "confiance": round(conf, 2),
                "douteux": sim < SEUIL_SIMILITUDE or conf < SEUIL_CONFIANCE}

    with ThreadPoolExecutor(6) as pool:
        rel = list(pool.map(un, attendus()))
    RELEVE.write_text(json.dumps(rel, ensure_ascii=False, indent=1), encoding="utf-8")
    return rel


def page(rel):
    E = html.escape
    rel = sorted(rel, key=lambda r: (not r["douteux"], r["similitude"], r["confiance"]))
    n = sum(r["douteux"] for r in rel)
    tete = (RACINE / "assets" / "presentations" / "francoeur-etape0.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Maison Francœur — écoute des voix</title>", tete)
    lignes = "".join(
        f'<tr class="{"d" if r["douteux"] else ""}" data-f="{E(r["fichier"])}"><td>{E(r["famille"])}</td>'
        f'<td><b>{E(r["attendu"])}</b><br><small>entendu : « {E(r["entendu"]) or "—"} »</small></td>'
        f'<td class="num">{r["similitude"]:.2f}<br><small>conf. {r["confiance"]:.2f}</small></td>'
        f'<td><audio controls preload="none" src="/assets/interactive/francoeur/{E(r["fichier"])}?v=hd"></audio>'
        f'<div class="choix"><button type="button" data-v="ok" aria-pressed="false">Bon</button>'
        f'<button type="button" data-v="refaire" aria-pressed="false">À refaire</button></div></td></tr>'
        for r in rel)
    corps = f"""<body><div class="doc large">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; voix Azure HD</p>
<h1>Écouter les voix</h1>
<p class="chapeau"><strong>{len(rel)} enregistrements</strong> refaits en Azure HD, chacun retranscrit par la
reconnaissance d'Azure et comparé au texte attendu. <strong>{n} douteux</strong> en tête : écart au texte
(sous {SEUIL_SIMILITUDE:.2f}) ou confiance basse (sous {SEUIL_CONFIANCE:.2f}). La reconnaissance écrit en
français ce qu'elle entend : un mot dit à l'anglaise peut passer. Le chiffre trie, l'oreille décide.</p>
<table class="cmp"><thead><tr><th>Famille</th><th>Texte</th><th>Écart</th><th>Écoute</th></tr></thead><tbody>{lignes}</tbody></table>
<p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes verdicts</button>
<span id="etat" class="etat"></span></p>
<div class="pied"><p>Produite par <code>build/francoeur_ecoute.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
(function(){{
  var CLE='francoeur-ecoute', v={{}};
  try{{ v=JSON.parse(localStorage.getItem(CLE)||'{{}}'); }}catch(e){{}}
  function peindre(){{ document.querySelectorAll('tr[data-f]').forEach(function(tr){{
    tr.querySelectorAll('.choix button').forEach(function(b){{ b.setAttribute('aria-pressed', v[tr.dataset.f]===b.dataset.v?'true':'false'); }}); }});
    document.getElementById('etat').textContent=Object.keys(v).length+' verdicts'; }}
  document.addEventListener('click',function(e){{ var b=e.target.closest('.choix button'); if(!b) return;
    var f=b.closest('tr').dataset.f; if(v[f]===b.dataset.v) delete v[f]; else v[f]=b.dataset.v;
    try{{ localStorage.setItem(CLE,JSON.stringify(v)); }}catch(x){{}} peindre(); }});
  document.getElementById('exporter').onclick=function(){{
    var t=JSON.stringify({{ecoute:'francoeur',a_refaire:Object.keys(v).filter(function(k){{return v[k]==='refaire';}})}},null,2);
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(function(){{ document.getElementById('etat').textContent='Copié.'; }}); else prompt('Copiez :',t); }};
  peindre();
}})();
</script></body></html>"""
    css = """
tr.d td{background:var(--decid-bg)}
.choix{display:flex;gap:6px;margin-top:6px}
.choix button{font:inherit;font-size:13px;cursor:pointer;border:1px solid var(--line-fort);background:var(--sunken);border-radius:8px;padding:4px 8px;color:var(--body)}
.choix button[aria-pressed=true][data-v=ok]{background:var(--fait-bg);border-color:var(--fait)}
.choix button[aria-pressed=true][data-v=refaire]{background:var(--loi-bg);border-color:var(--loi)}
audio{width:220px;max-width:100%}
.doc.large{max-width:1100px}
"""
    PAGE.write_text(tete.replace("</style>", css + "</style>", 1) + corps, encoding="utf-8")
    return n


if __name__ == "__main__":
    rel = (json.loads(RELEVE.read_text(encoding="utf-8")) if "--page" in sys.argv else controle())
    n = page(rel)
    print(f"{len(rel)} enregistrements, {n} douteux → {PAGE.relative_to(RACINE)}")
    for r in sorted(rel, key=lambda r: r["similitude"])[:12]:
        if r["douteux"]:
            print(f"  {r['similitude']:.2f} {r['confiance']:.2f}  {r['attendu'][:50]:50} ← {r['entendu'][:50]}")
