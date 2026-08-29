#!/usr/bin/env python3
"""La page de tri des constats d'audit — un jugement par constat, à la souris.

    python3 build/audit_constats_page.py    # écrit assets/presentations/audit-constats.html

L'audit de contenu du 28 août 2026 a rendu 338 constats. Les lire dans une
conversation ne mène nulle part : il en faut un jugement chacun, et ce jugement
doit se garder quelque part. Cette page les présente un par un — citation
exacte, problème, correction proposée, avis du sceptique — avec trois boutons.

**Le document est GÉNÉRÉ**, jamais écrit à la main : les constats bougent à
chaque vague d'audit, et une page recopiée serait fausse le lendemain.

Les décisions vivent dans le `localStorage` du navigateur, donc sur le poste de
l'enseignant et nulle part ailleurs. Le bouton « Exporter » rend un JSON à
recoller dans une session : c'est ce fichier qui pilote la reprise, pas la
mémoire de la conversation.
"""
import html
import json
import pathlib
from collections import Counter

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "data" / "audit" / "constats.json"
SORTIE = RACINE / "assets" / "presentations" / "audit-constats.html"

ORDRE = {"bloquant": 0, "majeur": 1, "mineur": 2}
LIB = {"fait-faux": "fait faux", "quebec": "réalité québécoise", "niveau": "niveau",
       "corrige-discutable": "corrigé discutable", "consigne-ambigue": "consigne ambiguë",
       "langue": "faute de langue"}


def main():
    cons = json.loads(SOURCE.read_text(encoding="utf-8"))
    cons.sort(key=lambda c: (ORDRE.get(c.get("gravite"), 3), c.get("module", ""), c.get("fichier", "")))
    for i, c in enumerate(cons):
        c["id"] = "c%03d" % i
    g = Counter(c["gravite"] for c in cons)
    mods = sorted({c["module"] for c in cons})
    cats = sorted({c["categorie"] for c in cons})

    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "n": len(cons), "nmod": len(mods),
        "bloq": g.get("bloquant", 0), "maj": g.get("majeur", 0), "min": g.get("mineur", 0),
        "mods": "".join('<option>%s</option>' % html.escape(m) for m in mods),
        "cats": "".join('<option value="%s">%s</option>' % (html.escape(c), html.escape(LIB.get(c, c))) for c in cats),
        "data": json.dumps(cons, ensure_ascii=False),
        "libelles": json.dumps(LIB, ensure_ascii=False),
    }, encoding="utf-8")
    print("Écrit : %s (%d constats)" % (SORTIE.relative_to(RACINE), len(cons)))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tri des constats d'audit</title>
<style>
:root{--fond:#faf9f7;--carte:#fff;--encre:#1c1a17;--doux:#6b6560;--trait:#e2ddd6;
      --bloq:#a3231b;--maj:#b06a12;--min:#5a6b58;--ok:#0d7a6f;--non:#8a8a8a;--vedette:#3b49a0}
@media (prefers-color-scheme:dark){:root{--fond:#16151a;--carte:#1e1d24;--encre:#eceaf0;
      --doux:#a09aa8;--trait:#332f3b;--bloq:#e8776d;--maj:#e0a84e;--min:#8fb08b;--ok:#4fc4b3;--non:#7a7a7a;--vedette:#8b96e8}}
*{box-sizing:border-box}
body{margin:0;background:var(--fond);color:var(--encre);
     font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--fond);border-bottom:1px solid var(--trait);
       padding:16px 20px 12px}
h1{margin:0 0 4px;font-size:19px;letter-spacing:-.01em}
.sous{color:var(--doux);font-size:13px;margin-bottom:12px}
.barre{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
select,button{font:inherit;font-size:13px;padding:6px 10px;border:1px solid var(--trait);
        border-radius:7px;background:var(--carte);color:var(--encre);cursor:pointer}
button.pri{background:var(--encre);color:var(--fond);border-color:var(--encre)}
.cpt{margin-left:auto;color:var(--doux);font-size:13px;font-variant-numeric:tabular-nums}
main{padding:16px 20px 80px;max-width:1000px;margin:0 auto}
.c{background:var(--carte);border:1px solid var(--trait);border-left-width:4px;
   border-radius:10px;padding:14px 16px;margin-bottom:12px}
.c[data-g=bloquant]{border-left-color:var(--bloq)}
.c[data-g=majeur]{border-left-color:var(--maj)}
.c[data-g=mineur]{border-left-color:var(--min)}
.c[data-d=corriger]{outline:2px solid var(--ok);outline-offset:1px}
.c[data-d=rejeter]{opacity:.42}
.c[data-d=plus-tard]{outline:2px dashed var(--doux);outline-offset:1px}
.hdr{display:flex;gap:8px;align-items:baseline;flex-wrap:wrap;margin-bottom:8px}
.et{font-size:11px;text-transform:uppercase;letter-spacing:.07em;font-weight:700}
.et.bloquant{color:var(--bloq)}.et.majeur{color:var(--maj)}.et.mineur{color:var(--min)}
.mod{font-weight:650}
.fic{color:var(--doux);font-size:12.5px;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;
     word-break:break-all}
.cit{background:color-mix(in srgb,var(--vedette) 8%%,transparent);border-radius:6px;padding:8px 10px;
     margin:8px 0;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:12.5px;
     white-space:pre-wrap;word-break:break-word;max-height:9em;overflow:auto}
.lbl{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--doux);
     font-weight:700;margin-top:10px}
p{margin:3px 0 0}
details{margin-top:8px}summary{cursor:pointer;font-size:13px;color:var(--doux)}
details p{font-size:14px;color:var(--doux);margin-top:6px}
.act{display:flex;gap:6px;margin-top:12px;flex-wrap:wrap}
.act button{font-size:12.5px}
.act button[aria-pressed=true]{background:var(--encre);color:var(--fond);border-color:var(--encre)}
.vide{color:var(--doux);text-align:center;padding:40px}
textarea{width:100%%;height:180px;font-family:ui-monospace,monospace;font-size:12px;
         border:1px solid var(--trait);border-radius:8px;padding:10px;background:var(--carte);color:var(--encre)}
dialog{border:1px solid var(--trait);border-radius:12px;background:var(--carte);color:var(--encre);
       max-width:760px;width:92vw;padding:18px}
dialog::backdrop{background:rgba(0,0,0,.45)}
</style></head><body>
<header>
  <h1>Tri des constats d'audit</h1>
  <div class="sous">%(n)d constats sur %(nmod)d modules —
    <b>%(bloq)d bloquants</b>, %(maj)d majeurs, %(min)d mineurs.
    Chacun a survécu à un réfutateur. Vos décisions restent sur ce poste.</div>
  <div class="barre">
    <select id="fg"><option value="">Toutes gravités</option>
      <option>bloquant</option><option>majeur</option><option>mineur</option></select>
    <select id="fc"><option value="">Toutes catégories</option>%(cats)s</select>
    <select id="fm"><option value="">Tous les modules</option>%(mods)s</select>
    <select id="fd"><option value="">Tous les états</option>
      <option value="">—</option><option value="a-juger">À juger</option>
      <option value="corriger">À corriger</option><option value="rejeter">Rejetés</option>
      <option value="plus-tard">Plus tard</option></select>
    <button id="exp" class="pri">Exporter mes décisions</button>
    <span class="cpt" id="cpt"></span>
  </div>
</header>
<main id="liste"></main>
<dialog id="dlg">
  <b>Vos décisions</b>
  <p style="font-size:13.5px;color:var(--doux)">Copiez ce texte et collez-le dans une session :
     il dit quoi corriger, quoi laisser, et dans quel ordre.</p>
  <textarea id="json" readonly></textarea>
  <div class="act"><button class="pri" id="copier">Copier</button>
    <button onclick="dlg.close()">Fermer</button></div>
</dialog>
<script>
const CONSTATS = %(data)s;
const LIB = %(libelles)s;
const CLE = 'audit-constats-decisions';
let D = {};
try { D = JSON.parse(localStorage.getItem(CLE) || '{}'); } catch (e) { D = {}; }
const sauver = () => { try { localStorage.setItem(CLE, JSON.stringify(D)); } catch (e) {} };
const esc = s => String(s == null ? '' : s).replace(/[&<>"]/g, c =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

function carte(c) {
  const d = D[c.id] || '';
  const b = (v, t) => `<button data-id="${c.id}" data-v="${v}" aria-pressed="${d === v}">${t}</button>`;
  return `<article class="c" data-g="${c.gravite}" data-d="${d}" id="${c.id}">
    <div class="hdr"><span class="et ${c.gravite}">${c.gravite}</span>
      <span class="mod">${esc(c.module)}</span>
      <span class="fic">${esc(c.fichier)}</span></div>
    <div class="cit">${esc(c.citation)}</div>
    <div class="lbl">Le problème — ${esc(LIB[c.categorie] || c.categorie)}</div><p>${esc(c.probleme)}</p>
    <div class="lbl">Correction proposée</div><p>${esc(c.correction)}</p>
    ${c.motifSceptique ? `<details><summary>Ce qu'en dit le sceptique</summary><p>${esc(c.motifSceptique)}</p></details>` : ''}
    <div class="act">${b('corriger', '✓ À corriger')}${b('rejeter', '✕ Rejeter')}${b('plus-tard', '⏳ Plus tard')}</div>
  </article>`;
}

function rendre() {
  const g = fg.value, k = fc.value, m = fm.value, e = fd.value;
  const vus = CONSTATS.filter(c =>
    (!g || c.gravite === g) && (!k || c.categorie === k) && (!m || c.module === m) &&
    (!e || (e === 'a-juger' ? !D[c.id] : D[c.id] === e)));
  liste.innerHTML = vus.length ? vus.map(carte).join('') :
    '<div class="vide">Rien ne correspond à ces filtres.</div>';
  const juges = CONSTATS.filter(c => D[c.id]).length;
  cpt.textContent = `${vus.length} affichés · ${juges} jugés sur ${CONSTATS.length}`;
}

liste.addEventListener('click', ev => {
  const b = ev.target.closest('button[data-id]'); if (!b) return;
  const id = b.dataset.id, v = b.dataset.v;
  if (D[id] === v) delete D[id]; else D[id] = v;
  sauver(); rendre();
  const el = document.getElementById(id); if (el) el.scrollIntoView({ block: 'nearest' });
});
[fg, fc, fm, fd].forEach(s => s.addEventListener('change', rendre));

exp.onclick = () => {
  const par = v => CONSTATS.filter(c => D[c.id] === v)
    .map(c => ({ module: c.module, fichier: c.fichier, gravite: c.gravite,
                 citation: c.citation, correction: c.correction }));
  json.value = JSON.stringify({
    aCorriger: par('corriger'), plusTard: par('plus-tard'),
    rejetes: par('rejeter').map(x => ({ module: x.module, citation: x.citation })),
    nonJuges: CONSTATS.filter(c => !D[c.id]).length
  }, null, 1);
  dlg.showModal();
};
copier.onclick = async () => {
  try { await navigator.clipboard.writeText(json.value); copier.textContent = 'Copié'; }
  catch (e) { json.select(); copier.textContent = 'Sélectionné — ⌘C'; }
  setTimeout(() => copier.textContent = 'Copier', 1600);
};
rendre();
</script></body></html>
"""

if __name__ == "__main__":
    main()
