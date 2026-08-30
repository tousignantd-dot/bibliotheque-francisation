#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La page avant/après de la reprise des images.

Les images refaites ne valent que si on les compare à celles qu'elles
remplacent. L'ancienne version n'est plus sur le disque — elle est dans
l'historique git, et c'est de là qu'on la sort : `git show HEAD:<chemin>`.

    python3 build/audit_avant_apres.py <dossier-audit>
        → assets/presentations/audit-avant-apres.html

Les vignettes « avant » sont écrites dans `assets/presentations/audit-avant/`,
qui n'a pas à être versionné : c'est un échafaudage, il se jette une fois le
tri fait. La page se coche — bonne, à refaire encore, revenir à l'ancienne —
et la barre du bas rend les deux listes.
"""
import hashlib
import html
import io
import json
import pathlib
import subprocess
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent
AVANT = BASE / 'assets' / 'presentations' / 'audit-avant'
SORTIE = BASE / 'assets' / 'presentations' / 'audit-avant-apres.html'


def vignette_avant(source, dest, largeur=460):
    """L'image telle qu'elle était au dernier commit, réduite."""
    from PIL import Image
    p = subprocess.run(['git', 'show', f'HEAD:{source}'], cwd=BASE,
                       capture_output=True)
    if p.returncode != 0 or not p.stdout:
        return False
    im = Image.open(io.BytesIO(p.stdout)).convert('RGB')
    h = round(im.height * largeur / im.width)
    dest.parent.mkdir(parents=True, exist_ok=True)
    im.resize((largeur, h), Image.LANCZOS).save(dest, 'JPEG', quality=78)
    return True


STYLE = """
:root { --encre:#101418; --gris:#5b6672; --trait:#d8dee5; --rouge:#b3261e;
        --vert:#1f6b3a; --ambre:#8a6100; --fond:#fbfcfd; }
* { box-sizing:border-box; }
body { margin:0; padding:0 24px 130px; background:#fff; color:var(--encre);
       font:15px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; }
header { position:sticky; top:0; background:#fff; padding:18px 0 12px;
         border-bottom:1px solid var(--trait); z-index:5; }
h1 { margin:0 0 4px; font-size:20px; }
header p { margin:0; color:var(--gris); font-size:13px; max-width:70ch; }
.filtres { margin-top:10px; display:flex; gap:8px; flex-wrap:wrap; }
.filtres button { border:1px solid var(--trait); background:#fff; color:var(--gris);
       font-size:12px; padding:5px 11px; border-radius:999px; cursor:pointer; }
.filtres button.on { background:var(--encre); border-color:var(--encre); color:#fff; }
article { border:1px solid var(--trait); border-radius:10px; margin-top:18px;
          background:var(--fond); overflow:hidden; }
.paire { display:grid; grid-template-columns:1fr 1fr; gap:1px; background:var(--trait); }
.vue { background:#eef1f4; position:relative; }
.vue img { width:100%; display:block; }
.vue span { position:absolute; top:8px; left:8px; font-size:11px;
       text-transform:uppercase; letter-spacing:.05em; padding:3px 8px;
       border-radius:4px; background:rgba(16,20,24,.78); color:#fff; }
.bas { padding:12px 14px 14px; display:flex; flex-direction:column; gap:8px; }
.tete { display:flex; align-items:baseline; justify-content:space-between; gap:10px; }
.mot { font-weight:600; font-size:16px; }
.ou { font-size:11px; color:var(--gris); text-transform:uppercase; letter-spacing:.04em; }
.motifs span { font-size:11px; border:1px solid var(--trait); background:#fff;
       border-radius:4px; padding:1px 6px; color:var(--gris); margin-right:4px; }
.note { font-size:13px; margin:0; }
.note b { display:block; font-size:11px; text-transform:uppercase;
          letter-spacing:.04em; color:var(--gris); font-weight:600; }
details { font-size:12px; color:var(--gris); }
details p { margin:6px 0 0; line-height:1.45; }
.choix { display:flex; gap:6px; }
.choix button { flex:1; border:1px solid var(--trait); background:#fff; color:var(--gris);
       font-size:12px; padding:7px 0; border-radius:6px; cursor:pointer; }
.choix button.on.bonne   { background:var(--vert);  border-color:var(--vert);  color:#fff; }
.choix button.on.encore  { background:var(--ambre); border-color:var(--ambre); color:#fff; }
.choix button.on.revenir { background:var(--rouge); border-color:var(--rouge); color:#fff; }
article.tranche { opacity:.6; }
footer { position:fixed; left:0; right:0; bottom:0; background:#fff;
         border-top:1px solid var(--trait); padding:10px 24px; display:flex;
         gap:12px; align-items:center; font-size:13px; }
footer textarea { flex:1; height:46px; font:12px/1.4 ui-monospace,Menlo,monospace;
         border:1px solid var(--trait); border-radius:6px; padding:6px 8px; resize:none; }
footer button { border:1px solid var(--trait); background:#fff; border-radius:6px;
         padding:7px 12px; cursor:pointer; font-size:12px; }
"""


def page(cartes):
    blocs = []
    for c in cartes:
        motifs = ''.join(f'<span>{html.escape(m)}</span>' for m in c['motifs'])
        blocs.append(f'''
<article data-id="{html.escape(c['id'])}" data-grav="{c['gravite']}">
  <div class="paire">
    <div class="vue"><span>avant</span><img loading="lazy" src="{html.escape(c['avant'])}" alt=""></div>
    <div class="vue"><span>après</span><img loading="lazy" src="{html.escape(c['apres'])}" alt=""></div>
  </div>
  <div class="bas">
    <div class="tete"><span class="mot">{html.escape(c['mot'])}</span>
      <span class="ou">{html.escape(c['module'])} · {html.escape(c['dossier'])} · {c['gravite']}</span></div>
    <div class="motifs">{motifs}</div>
    <p class="note"><b>Ce qui clochait</b>{html.escape(c['diagnostic'])}</p>
    <details><summary>le prompt réécrit</summary><p>{html.escape(c['prompt'])}</p></details>
    <div class="choix">
      <button class="bonne"   data-c="bonne">bonne</button>
      <button class="encore"  data-c="encore">à refaire encore</button>
      <button class="revenir" data-c="revenir">revenir à l’ancienne</button>
    </div>
  </div>
</article>''')
    return f'''<!doctype html>
<html lang="fr"><meta charset="utf-8">
<title>Reprise des images — avant et après</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{STYLE}</style>
<header>
  <h1>Reprise des images — avant et après</h1>
  <p><strong>{len(cartes)}</strong> images refaites après l’audit, chacune à côté de celle
     qu’elle remplace. L’ancienne version vient de l’historique git : rien n’est perdu,
     « revenir à l’ancienne » se fait par <code>git checkout</code>. Le prompt réécrit est
     dépliable sous chaque paire.</p>
  <div class="filtres">
    <button class="on" data-f="tout">tout</button>
    <button data-f="bloquant">bloquantes</button>
    <button data-f="genant">gênantes</button>
    <button data-f="mineur">mineures</button>
    <button data-f="reste">pas encore tranchées</button>
  </div>
</header>
{''.join(blocs)}
<footer>
  <span id="compte"></span>
  <textarea id="liste" readonly placeholder="les images à refaire encore, puis celles à restaurer"></textarea>
  <button id="copier">copier</button>
  <button id="vider">tout oublier</button>
</footer>
<script>
const CLE='audit-avant-apres-v1';
let choix=JSON.parse(localStorage.getItem(CLE)||'{{}}');
const arts=[...document.querySelectorAll('article')];
function peindre(){{
  arts.forEach(a=>{{ const c=choix[a.dataset.id];
    a.classList.toggle('tranche',!!c);
    a.querySelectorAll('.choix button').forEach(b=>b.classList.toggle('on',b.dataset.c===c)); }});
  const enc=arts.filter(a=>choix[a.dataset.id]==='encore').map(a=>a.dataset.id);
  const rev=arts.filter(a=>choix[a.dataset.id]==='revenir').map(a=>a.dataset.id);
  const faits=arts.filter(a=>choix[a.dataset.id]).length;
  document.getElementById('liste').value =
    (enc.length?'# à refaire encore\\n'+enc.join('\\n'):'') +
    (rev.length?(enc.length?'\\n\\n':'')+'# revenir à l\\'ancienne\\n'+rev.join('\\n'):'');
  document.getElementById('compte').textContent =
    faits+' / '+arts.length+' tranchées · '+enc.length+' à refaire · '+rev.length+' à restaurer';
}}
document.body.addEventListener('click',e=>{{
  const b=e.target.closest('.choix button'); if(!b) return;
  const a=b.closest('article');
  choix[a.dataset.id]=(choix[a.dataset.id]===b.dataset.c)?undefined:b.dataset.c;
  if(!choix[a.dataset.id]) delete choix[a.dataset.id];
  localStorage.setItem(CLE,JSON.stringify(choix)); peindre();
}});
document.querySelector('.filtres').addEventListener('click',e=>{{
  const b=e.target.closest('button'); if(!b) return;
  document.querySelectorAll('.filtres button').forEach(x=>x.classList.toggle('on',x===b));
  const f=b.dataset.f;
  arts.forEach(a=>{{ const ok = f==='tout' ? true
    : f==='reste' ? !choix[a.dataset.id] : a.dataset.grav===f;
    a.style.display = ok?'':'none'; }});
}});
document.getElementById('copier').onclick=()=>{{
  const t=document.getElementById('liste'); t.select(); navigator.clipboard.writeText(t.value); }};
document.getElementById('vider').onclick=()=>{{
  if(!confirm('Oublier toutes les décisions ?')) return;
  choix={{}}; localStorage.removeItem(CLE); peindre(); }};
peindre();
</script>
</html>'''


def main():
    d = pathlib.Path(sys.argv[1])
    lot = json.loads((d / 'reprise.json').read_text())
    # Le prompt d'après, relu sur le disque : celui du rapport pourrait mentir.
    reprises = {}
    for f in sorted((d / 'reprises').glob('*.json')):
        for r in json.loads(f.read_text()):
            reprises[r['id']] = r
    cartes, sans_avant = [], []
    for x in lot:
        plat = x['id'].replace('/', '__')
        dest = AVANT / plat
        if not dest.exists() and not vignette_avant(x['source'], dest):
            sans_avant.append(x['id'])
            continue
        cartes.append({
            'id': x['id'], 'module': x['module'], 'dossier': x['dossier'],
            'mot': x['mot'], 'gravite': x['gravite'], 'motifs': x['motifs'],
            'diagnostic': x['diagnostic'],
            'prompt': reprises.get(x['id'], {}).get('apres', '') or '(réécrit à la main)',
            'avant': '/assets/presentations/audit-avant/' + plat,
            # Le nom du fichier n'a pas changé, donc le navigateur sert sa
            # copie en cache et montre l'ANCIENNE image en face de l'ancienne.
            # L'empreinte du fichier neuf dans l'URL force le rechargement —
            # même piège, même parade que AUDIO_V pour le son.
            'apres': '/' + x['source'] + '?v=' + hashlib.sha1(
                (BASE / x['source']).read_bytes()).hexdigest()[:10],
        })
    ordre = {'bloquant': 0, 'genant': 1, 'mineur': 2}
    cartes.sort(key=lambda c: (ordre.get(c['gravite'], 3), c['module'], c['mot']))
    SORTIE.write_text(page(cartes), encoding='utf-8')
    print(f'{SORTIE} · {len(cartes)} paires'
          + (f" · sans version antérieure : {sans_avant}" if sans_avant else ''))


if __name__ == '__main__':
    main()
