#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La page de tri de l'audit des images.

Deux passages d'agents ont jugé les 1 502 images des modules : un lecteur, qui
ratisse tout et lève la main, puis un vérificateur, qui ne regarde que les
images levées et confirme ou blanchit. Cette page ne montre que ce qui reste
en doute après les deux, avec les deux avis côte à côte — c'est là que
l'humain tranche.

    python3 build/audit_images_page.py <dossier-audit>
        → assets/presentations/audit-images.html

Puis, le serveur local tournant :
http://localhost:5173/assets/presentations/audit-images.html

Chaque image se tranche en un clic — « à refaire », « à revoir », « je garde ».
Les choix tiennent dans le localStorage et la barre du bas rend la liste des
images à refaire, prête à être collée dans une consigne de régénération.
"""
import html
import json
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = BASE / 'assets' / 'presentations' / 'audit-images.html'

# ── Une décision prise à la main, le 29 août 2026 ─────────────────────────
# Le vérificateur du lot 13 a blanchi sept images de `module-restaurant` et
# `module-vetements` au motif que l'autobus qu'on y voit est « le décor
# demandé par le prompt ». C'est exact, et c'est précisément le défaut : la
# ligne de décor « Rue ou transport en commun d'une ville québécoise
# ordinaire » a été recopiée telle quelle dans six modules du niveau 4 —
# 121 images en tout — alors qu'elle ne convient qu'à `module-deplacement`.
# Une assiette de poulet servie sur un siège d'autobus est fidèle à son
# prompt et inutilisable en classe. On les remet donc en doute, en le disant.
DECOR_FAUTIF = {
    'module-restaurant/vocab/plat.jpg',
    'module-restaurant/vocab/table-hote.jpg',
    'module-vetements/images/capuchon-fourrure.jpg',
    'module-vetements/images/facture-sac.jpg',
    'module-vetements/vocab/cabine.jpg',
    'module-vetements/vocab/manche.jpg',
    'module-vetements/vocab/mise-de-cote.jpg',
}
NOTE_DECOR = ("Décor d'autobus, fidèle au prompt — et c'est le prompt qui est "
              "fautif : sa ligne de décor vient de module-deplacement.")

ORDRE = {'bloquant': 0, 'genant': 1, 'mineur': 2, '': 3}
LIBELLE = {'bloquant': 'à refaire', 'genant': 'à revoir', 'mineur': 'mineur'}


def charger(dossier):
    """Fusionne la liste de travail, les verdicts du lecteur et ceux du
    vérificateur. Une image sans verdict de vérificateur n'a pas été levée par
    le lecteur : elle ne paraît pas sur la page."""
    travail = {t['id']: t for t in json.loads((dossier / 'travail.json').read_text())}
    lecteur, verif = {}, {}
    for f in sorted((dossier / 'verdicts').glob('lot-*.json')):
        for v in json.loads(f.read_text()):
            lecteur[v['id']] = v
    d2 = dossier / 'verifications'
    if d2.is_dir():
        for f in sorted(d2.glob('*.json')):
            for v in json.loads(f.read_text()):
                verif[v['id']] = v
    # Le troisième passage n'a vu que les bloquants. Il tranche en dernier
    # ressort — il rétrograde beaucoup — et rend en plus la correction de
    # prompt à appliquer, qui est la seule chose vraiment actionnable ici.
    arb = {}
    d3 = dossier / 'arbitrages'
    if d3.is_dir():
        for f in sorted(d3.glob('*.json')):
            for v in json.loads(f.read_text()):
                arb[v['id']] = v
    lignes = []
    for ident, v in lecteur.items():
        if v.get('verdict') != 'doute':
            continue
        w = verif.get(ident, {})
        force = ident in DECOR_FAUTIF
        if w.get('verdict') == 'ok' and not force:   # le vérificateur a blanchi
            continue
        a = arb.get(ident, {})
        if a and not (a.get('gravite') or '').strip():   # l'arbitre a blanchi
            continue
        t = travail.get(ident, {})
        lignes.append({
            'id': ident,
            'module': t.get('module', ''),
            'dossier': t.get('dossier', ''),
            'mot': t.get('mot', ''),
            'enonce': t.get('enonce', ''),
            'prompt': t.get('prompt', ''),
            'src': '/' + t.get('source', ''),
            'motifs': (['decor'] if force else (w.get('motifs') or v.get('motifs') or [])),
            'gravite': (a.get('gravite') if a else
                        ('bloquant' if force else (w.get('gravite') or v.get('gravite') or ''))),
            'lecteur': v.get('note', ''),
            'verif': (NOTE_DECOR if force else w.get('note', '') or w.get('pourquoi', '')),
            'arbitre': a.get('pourquoi', ''),
            'correction': a.get('correction', ''),
            'accord': ('arbitré' if a else 'remis en doute à la main' if force
                       else 'confirmé' if w else 'non vérifié'),
        })
    # Les images déjà reprises n'ont plus à être jugées ici : elles portaient
    # la critique de l'image d'AVANT, sous la photo d'APRÈS, ce qui trompe le
    # lecteur. Elles se jugent sur la page avant/après, qui montre les deux.
    faites = set()
    f = dossier / 'reprise.json'
    if f.exists():
        faites = {x['id'] for x in json.loads(f.read_text())}
    reprises = sum(1 for L in lignes if L['id'] in faites)
    lignes = [L for L in lignes if L['id'] not in faites]
    lignes.sort(key=lambda x: (ORDRE.get(x['gravite'], 3), x['module'], x['mot']))
    leves = sum(1 for v in lecteur.values() if v.get('verdict') == 'doute')
    return lignes, len(travail), leves, reprises


STYLE = """
:root { --encre:#101418; --gris:#5b6672; --trait:#d8dee5; --rouge:#b3261e;
        --ambre:#8a6100; --vert:#1f6b3a; --fond:#fbfcfd; }
* { box-sizing:border-box; }
body { margin:0; padding:0 24px 140px; background:#fff; color:var(--encre);
       font:15px/1.5 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; }
header { position:sticky; top:0; background:#fff; padding:18px 0 12px;
         border-bottom:1px solid var(--trait); z-index:5; }
h1 { margin:0 0 4px; font-size:20px; letter-spacing:-.01em; }
header p { margin:0; color:var(--gris); font-size:13px; }
.filtres { margin-top:10px; display:flex; gap:8px; flex-wrap:wrap; }
.filtres button { border:1px solid var(--trait); background:#fff; color:var(--gris);
       font-size:12px; padding:5px 11px; border-radius:999px; cursor:pointer; }
.filtres button.on { background:var(--encre); border-color:var(--encre); color:#fff; }
.grille { display:grid; gap:18px; margin-top:22px;
          grid-template-columns:repeat(auto-fill,minmax(330px,1fr)); }
figure { margin:0; border:1px solid var(--trait); border-radius:10px;
         overflow:hidden; background:var(--fond); display:flex; flex-direction:column; }
figure img { width:100%; aspect-ratio:3/2; object-fit:cover; display:block;
             background:#eef1f4; }
.corps { padding:11px 13px 13px; display:flex; flex-direction:column; gap:7px; flex:1; }
.tete { display:flex; align-items:baseline; justify-content:space-between; gap:8px; }
.mot { font-weight:600; }
.grav { font-size:11px; text-transform:uppercase; letter-spacing:.04em;
        padding:2px 7px; border-radius:4px; white-space:nowrap; }
.g-bloquant { background:#fdeceb; color:var(--rouge); }
.g-genant   { background:#fdf4e3; color:var(--ambre); }
.g-mineur   { background:#eef1f4; color:var(--gris); }
.ou { font-size:11px; color:var(--gris); text-transform:uppercase; letter-spacing:.04em; }
.motifs { display:flex; gap:5px; flex-wrap:wrap; }
.motifs span { font-size:11px; border:1px solid var(--trait); background:#fff;
       border-radius:4px; padding:1px 6px; color:var(--gris); }
.note { font-size:13px; color:var(--encre); }
.note b { font-weight:600; color:var(--gris); font-size:11px;
          text-transform:uppercase; letter-spacing:.04em; display:block; }
.note.v { color:var(--gris); }
.corr { font-size:13px; margin:0; padding:8px 10px; border-radius:6px;
        background:#eef4ee; border:1px solid #cfe0d2; color:#1d4a2c; }
.corr b { display:block; font-size:11px; text-transform:uppercase;
          letter-spacing:.04em; color:#3d6b4c; font-weight:600; }
details { font-size:12px; color:var(--gris); }
details summary { cursor:pointer; }
details p { margin:6px 0 0; line-height:1.45; }
.choix { display:flex; gap:6px; margin-top:auto; padding-top:4px; }
.choix button { flex:1; border:1px solid var(--trait); background:#fff;
       color:var(--gris); font-size:12px; padding:6px 0; border-radius:6px;
       cursor:pointer; }
.choix button.on.refaire { background:var(--rouge); border-color:var(--rouge); color:#fff; }
.choix button.on.revoir  { background:var(--ambre); border-color:var(--ambre); color:#fff; }
.choix button.on.garde   { background:var(--vert);  border-color:var(--vert);  color:#fff; }
figure.tranche { opacity:.55; }
footer { position:fixed; left:0; right:0; bottom:0; background:#fff;
         border-top:1px solid var(--trait); padding:11px 24px;
         display:flex; align-items:center; gap:14px; font-size:13px; }
footer textarea { flex:1; height:44px; font:12px/1.4 ui-monospace,SFMono-Regular,Menlo,monospace;
         border:1px solid var(--trait); border-radius:6px; padding:6px 8px; resize:none; }
footer button { border:1px solid var(--trait); background:#fff; border-radius:6px;
         padding:7px 12px; cursor:pointer; font-size:12px; }
"""


def page(lignes, total, leves, reprises=0):
    cartes = []
    for L in lignes:
        motifs = ''.join(f'<span>{html.escape(m)}</span>' for m in L['motifs'])
        prompt = html.escape(L['prompt'][:900]) if L['prompt'] else \
            '<i>aucun prompt d’origine retrouvé pour cette image</i>'
        verif = (f'<p class="note v"><b>Vérificateur</b>{html.escape(L["verif"])}</p>'
                 if L['verif'] else '')
        arbitre = (f'<p class="note v"><b>Arbitre</b>{html.escape(L["arbitre"])}</p>'
                   if L.get('arbitre') else '')
        corr = (f'<p class="corr"><b>À corriger au prompt</b>{html.escape(L["correction"])}</p>'
                if L.get('correction') else '')
        cartes.append(f'''
<figure data-id="{html.escape(L['id'])}" data-grav="{L['gravite']}"
        data-motifs="{html.escape(','.join(L['motifs']))}">
  <img loading="lazy" src="{html.escape(L['src'])}" alt="">
  <div class="corps">
    <div class="tete"><span class="mot">{html.escape(L['mot'])}</span>
      <span class="grav g-{L['gravite'] or 'mineur'}">{LIBELLE.get(L['gravite'],'—')}</span></div>
    <div class="ou">{html.escape(L['module'])} · {html.escape(L['dossier'])} · {html.escape(L['accord'])}</div>
    <div class="motifs">{motifs}</div>
    <p class="note"><b>Lecteur</b>{html.escape(L['lecteur'])}</p>
    {verif}
    {arbitre}
    {corr}
    <details><summary>l’énoncé et le prompt d’origine</summary>
      <p>{html.escape(L['enonce']) or '<i>pas d’énoncé</i>'}</p><p>{prompt}</p></details>
    <div class="choix">
      <button class="refaire" data-c="refaire">à refaire</button>
      <button class="revoir"  data-c="revoir">à revoir</button>
      <button class="garde"   data-c="garde">je garde</button>
    </div>
  </div>
</figure>''')
    compte = {}
    for L in lignes:
        compte[L['gravite']] = compte.get(L['gravite'], 0) + 1
    resume = ' · '.join(f'{compte.get(g,0)} {LIBELLE[g]}' for g in ('bloquant', 'genant', 'mineur'))
    return f'''<!doctype html>
<html lang="fr"><meta charset="utf-8">
<title>Audit des images — ce qui reste en doute</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>{STYLE}</style>
<header>
  <h1>Audit des images — ce qui reste en doute</h1>
  <p>{total} images passées en revue, {leves} levées au premier passage,
     <strong>{len(lignes)}</strong> restent à trancher : {resume}.
     {reprises} autres ont déjà été refaites — leur prompt avait été corrigé —
     et se jugent sur la page <a href="audit-avant-apres.html">avant et après</a>,
     qui montre l’ancienne et la neuve côte à côte. Celles qui sont ici ont un
     prompt inchangé : les régénérer telles quelles reviendrait à relancer le
     même dé. Les images blanchies en cours de route n’y sont pas non plus.</p>
  <div class="filtres">
    <button class="on" data-f="tout">tout</button>
    <button data-f="bloquant">à refaire</button>
    <button data-f="genant">à revoir</button>
    <button data-f="mineur">mineur</button>
    <button data-f="reste">pas encore tranchées</button>
  </div>
</header>
<div class="grille">{''.join(cartes)}</div>
<footer>
  <span id="compte"></span>
  <textarea id="liste" readonly placeholder="les images marquées « à refaire » s’écrivent ici"></textarea>
  <button id="copier">copier</button>
  <button id="vider">tout oublier</button>
</footer>
<script>
const CLE = 'audit-images-v1';
let choix = JSON.parse(localStorage.getItem(CLE) || '{{}}');
const figs = [...document.querySelectorAll('figure')];

function peindre() {{
  figs.forEach(f => {{
    const c = choix[f.dataset.id];
    f.classList.toggle('tranche', !!c);
    f.querySelectorAll('.choix button').forEach(b =>
      b.classList.toggle('on', b.dataset.c === c));
  }});
  const refaire = figs.filter(f => choix[f.dataset.id] === 'refaire').map(f => f.dataset.id);
  const faits = figs.filter(f => choix[f.dataset.id]).length;
  document.getElementById('liste').value = refaire.join('\\n');
  document.getElementById('compte').textContent =
    faits + ' / ' + figs.length + ' tranchées · ' + refaire.length + ' à refaire';
}}
document.querySelector('.grille').addEventListener('click', e => {{
  const b = e.target.closest('.choix button'); if (!b) return;
  const f = b.closest('figure');
  choix[f.dataset.id] = (choix[f.dataset.id] === b.dataset.c) ? undefined : b.dataset.c;
  if (!choix[f.dataset.id]) delete choix[f.dataset.id];
  localStorage.setItem(CLE, JSON.stringify(choix)); peindre();
}});
document.querySelector('.filtres').addEventListener('click', e => {{
  const b = e.target.closest('button'); if (!b) return;
  document.querySelectorAll('.filtres button').forEach(x => x.classList.toggle('on', x === b));
  const f = b.dataset.f;
  figs.forEach(fig => {{
    const ok = f === 'tout' ? true
             : f === 'reste' ? !choix[fig.dataset.id]
             : fig.dataset.grav === f;
    fig.style.display = ok ? '' : 'none';
  }});
}});
document.getElementById('copier').onclick = () => {{
  const t = document.getElementById('liste'); t.select();
  navigator.clipboard.writeText(t.value);
}};
document.getElementById('vider').onclick = () => {{
  if (!confirm('Oublier toutes les décisions prises sur cette page ?')) return;
  choix = {{}}; localStorage.removeItem(CLE); peindre();
}};
peindre();
</script>
</html>'''


def main():
    dossier = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else pathlib.Path('.')
    lignes, total, leves, reprises = charger(dossier)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page(lignes, total, leves, reprises), encoding='utf-8')
    print(f'{SORTIE} · {total} images · {leves} levées · {reprises} déjà refaites · '
          f'{len(lignes)} à trancher')


if __name__ == '__main__':
    main()
