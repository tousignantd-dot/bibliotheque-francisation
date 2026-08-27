#!/usr/bin/env python3
"""L'état du projet, d'un coup d'œil — lu sur le disque, jamais déclaré.

    python3 build/tableau_bord.py           → écrit assets/presentations/tableau-de-bord.html
    python3 build/tableau_bord.py --texte   → le même état, en clair dans le terminal

Pourquoi cette page existe
--------------------------
Il y avait déjà trois façons de savoir où on en est, et aucune ne répondait à
la question entière : `build/chantier.py` ne parle que des banques d'ateliers,
`build/bilan_programme.py` que de la couverture des situations,
`build/couts_api.py` que de la facture. Le reste — combien de modules sont
vraiment sur le disque, lesquels n'ont pas leurs seize séances en PowerPoint,
lesquels n'ont pas une seule piste audio, quels liens du catalogue pointent
dans le vide — se recalculait de tête à chaque fois.

**Rien ici n'est écrit à la main.** Chaque compteur vient du disque :

  · les modules, du registre `build/powerpoints/modules.py` ;
  · les séances produites, des `.pptx` de `assets/powerpoints/<slug>/` ;
  · les fiches, des fichiers de `assets/documents/` préfixés du slug ;
  · l'audio, des `.mp3` sous `assets/interactive/<slug>/` ;
  · le catalogue, de `data/activities.json`, liens vérifiés un par un ;
  · les ateliers et les savoirs, du relevé de `build/chantier.py` ;
  · les situations couvertes, du bilan de `build/bilan_programme.py` ;
  · la dépense, du registre `data/appels_api.jsonl` via `journal_api`.

Deux réserves, écrites plutôt que masquées :

· **Le registre des appels lu ici est celui du poste.** Celui qui compte vit
  sur le volume Railway et se lit par `GET /api/admin/appels`. Un montant
  presque nul en local ne veut pas dire que la production ne coûte rien.
· **Seize séances est la grille des niveaux 3 à 8** ; les niveaux 1 et 2 en
  ont huit. La page compare toujours au nombre de séances déclaré par le
  module lui-même, jamais à seize en dur.
"""
import argparse
import datetime
import html
import json
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(RACINE / 'build'))
sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
SORTIE = RACINE / 'assets/presentations/tableau-de-bord.html'

COULEURS = {1: '#A5335F', 2: '#A83A22', 3: '#B45309', 4: '#8C6A07',
            5: '#0D7A6F', 6: '#1D6B8F', 7: '#3B49A0', 8: '#7E3F98'}
FONDS = {1: '#FCE9F0', 2: '#FBEAE4', 3: '#FBEEDC', 4: '#F7F0DA',
         5: '#DCF2EF', 6: '#E7F0F6', 7: '#E8EAFA', 8: '#F3E8F7'}
MOIS = ('janvier février mars avril mai juin juillet août septembre '
        'octobre novembre décembre').split()


def en_francais(d):
    return '%d %s %d, %dh%02d' % (d.day, MOIS[d.month - 1], d.year, d.hour, d.minute)


def nb(n):
    """1 234 — l'espace fine insécable, pour que les chiffres se lisent."""
    return '%s' % format(int(n), ',').replace(',', ' ')


# ── Ce que le disque dit ─────────────────────────────────────────────────

def modules():
    """Un module, une ligne : ce qui est déclaré et ce qui est produit."""
    from modules import MODULES
    acts = json.loads((RACINE / 'data/activities.json').read_text(encoding='utf-8'))
    par_id = {a['id']: a for a in acts}
    docs = RACINE / 'assets/documents'
    noms_docs = [p.name for p in docs.iterdir()] if docs.is_dir() else []

    lignes = []
    for slug, m in sorted(MODULES.items(), key=lambda kv: (kv[1].get('niveau', 4),
                                                           kv[1].get('numero', 0))):
        dossier = RACINE / 'assets/interactive' / slug
        pptx = RACINE / 'assets/powerpoints' / slug
        attendues = len(m.get('seances') or [])
        produites = len(list(pptx.glob('*.pptx'))) if pptx.is_dir() else 0
        mp3 = len(list(dossier.rglob('*.mp3'))) if dossier.is_dir() else 0
        fiches = sum(1 for n in noms_docs if n.startswith(slug + '-'))
        act = par_id.get(m.get('activite'))
        lignes.append({
            'slug': slug, 'niveau': m.get('niveau', 4), 'numero': m.get('numero', 0),
            'titre': m.get('titre') or slug, 'activite': m.get('activite'),
            'joue': dossier.is_dir() and any(dossier.glob('*.html')),
            'seances': attendues, 'pptx': produites, 'fiches': fiches, 'mp3': mp3,
            'catalogue': act is not None,
            'vue': (act or {}).get('dateVue') or '',
        })
    return lignes


def catalogue():
    """Les activités du dépôt, et les liens qui pointent dans le vide."""
    acts = json.loads((RACINE / 'data/activities.json').read_text(encoding='utf-8'))
    casses = []
    for a in acts:
        for champ in ('interactive', 'studentDoc', 'planCours', 'slideshow', 'thumbnail'):
            chemin = a.get(champ) or ''
            if not chemin or chemin.startswith('http'):
                continue
            if not (RACINE / chemin).exists():
                casses.append((a.get('id'), a.get('title') or '?', champ, chemin))
    par_categorie = {}
    for a in acts:
        c = a.get('categorie') or 'sans catégorie'
        par_categorie[c] = par_categorie.get(c, 0) + 1
    return acts, par_categorie, casses


def depense():
    """Le registre des appels payants — celui du poste, pas celui de Railway."""
    import journal_api
    fichier = RACINE / 'data/appels_api.jsonl'
    if not fichier.exists():
        return None
    lignes = journal_api.lire(fichier=fichier)
    if not lignes:
        return {'appels': 0, 'cout': 0.0, 'routes': [], 'depuis': ''}
    total = 0.0
    routes = {}
    for d in lignes:
        c = d.get('cout_usd') or 0
        total += c
        r = routes.setdefault(d.get('route') or '?', {'appels': 0, 'cout': 0.0})
        r['appels'] += 1
        r['cout'] += c
    return {
        'appels': len(lignes), 'cout': total,
        'depuis': (lignes[0].get('quand') or '')[:10],
        'routes': sorted(({'route': k, **v} for k, v in routes.items()),
                         key=lambda r: -r['cout']),
    }


def git():
    """Les derniers commits et ce qui n'est pas encore poussé."""
    def cmd(*a):
        try:
            return subprocess.run(a, cwd=RACINE, capture_output=True,
                                  text=True, timeout=10).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            return ''
    log = [l for l in cmd('git', 'log', '--pretty=%h\t%ad\t%s',
                          '--date=short', '-8').splitlines() if '\t' in l]
    sales = [l for l in cmd('git', 'status', '--porcelain').splitlines() if l]
    devant = cmd('git', 'rev-list', '--count', '@{u}..HEAD') or '0'
    return {
        'commits': [l.split('\t', 2) for l in log],
        'sales': len(sales),
        'devant': int(devant) if devant.isdigit() else 0,
    }


def releve():
    """Tout l'état, en un seul objet."""
    from chantier import releve as banques
    niveaux = banques()                     # modules, ateliers, savoirs, situations
    mods = modules()
    acts, par_categorie, casses = catalogue()

    for niv, l in niveaux.items():
        siens = [m for m in mods if m['niveau'] == niv]
        l['mods'] = siens
        l['seances_dues'] = sum(m['seances'] for m in siens)
        l['seances_faites'] = sum(min(m['pptx'], m['seances']) for m in siens)
        l['mp3'] = sum(m['mp3'] for m in siens)
        l['fiches'] = sum(m['fiches'] for m in siens)

    try:
        from bilan_programme import bilan
        par_niveau, couvert, hors = bilan()
        situations = {n: (len(couvert.get(n, set())), len(s))
                      for n, s in par_niveau.items()}
    except Exception as e:                  # le programme peut ne pas être là
        situations, hors = {}, [('—', '—', 'bilan indisponible : %s' % e)]

    return {
        'niveaux': niveaux, 'mods': mods, 'activites': acts,
        'categories': par_categorie, 'casses': casses, 'situations': situations,
        'hors': hors, 'depense': depense(), 'git': git(),
    }


# ── Les alertes : ce qui manque, et seulement ça ─────────────────────────

def _extrait(items, rendu, n=8):
    """Quelques exemples, et le compte de ce qu'on ne montre pas."""
    tete = ', '.join(rendu(x) for x in items[:n])
    reste = len(items) - n
    return tete + (' … et %d autre%s' % (reste, 's' if reste > 1 else '')
                   if reste > 0 else '')


def alertes(e):
    """Ce qui appelle une action. Une liste vide est une bonne nouvelle."""
    a = []
    sans_pptx = [m for m in e['mods'] if m['pptx'] == 0]
    partiels = [m for m in e['mods'] if 0 < m['pptx'] < m['seances']]
    sans_audio = [m for m in e['mods'] if m['mp3'] == 0]
    sans_jeu = [m for m in e['mods'] if not m['joue']]
    if sans_jeu:
        a.append(('grave', '%d module(s) sans fichier interactif sur le disque'
                  % len(sans_jeu), _extrait(sans_jeu, lambda m: m['slug'])))
    if sans_pptx:
        a.append(('grave', '%d module(s) sans aucune séance en PowerPoint'
                  % len(sans_pptx), _extrait(sans_pptx, lambda m: m['slug'])))
    if partiels:
        a.append(('tiede', '%d module(s) aux séances incomplètes' % len(partiels),
                  _extrait(partiels, lambda m: '%s (%d/%d)'
                           % (m['slug'], m['pptx'], m['seances']))))
    if sans_audio:
        a.append(('tiede', '%d module(s) sans une seule piste audio' % len(sans_audio),
                  _extrait(sans_audio, lambda m: m['slug'])))
    if e['casses']:
        a.append(('grave', '%d lien(s) du catalogue pointent dans le vide'
                  % len(e['casses']),
                  _extrait(e['casses'], lambda c: '#%s %s' % (c[0], c[3]), 5)))
    orphelins = sum(len(l['manquants']) for l in e['niveaux'].values())
    if orphelins:
        a.append(('tiede', '%d savoir(s) du programme ne sont touchés par aucun '
                  'atelier' % orphelins,
                  ' · '.join('niveau %d : %d' % (n, len(l['manquants']))
                             for n, l in sorted(e['niveaux'].items())
                             if l['manquants'])))
    if e['hors']:
        a.append(('tiede', '%d module(s) ne se rattachent à aucune situation du '
                  'programme' % len(e['hors']),
                  _extrait(e['hors'], lambda h: '%s — %s' % (h[0], h[2]), 4)))
    if e['git']['sales']:
        a.append(('tiede', '%d fichier(s) modifiés et non commités'
                  % e['git']['sales'], 'donc absents de la production'))
    if e['git']['devant']:
        a.append(('tiede', '%d commit(s) non poussés' % e['git']['devant'],
                  'Railway déploie sur push : ce travail n’est pas en ligne'))
    return a


# ── La sortie en clair ───────────────────────────────────────────────────

def texte(e):
    print('%d modules · %d séances produites sur %d · %s MP3 · %d activités au '
          'catalogue' % (len(e['mods']),
                         sum(l['seances_faites'] for l in e['niveaux'].values()),
                         sum(l['seances_dues'] for l in e['niveaux'].values()),
                         nb(sum(m['mp3'] for m in e['mods'])), len(e['activites'])))
    for niv, l in sorted(e['niveaux'].items()):
        couv = e['situations'].get(niv, (0, l['situations']))
        print('Niveau %d — %d modules · %d/%d séances · %d ateliers · '
              'situations %d/%d · savoirs %d/%d'
              % (niv, l['modules'], l['seances_faites'], l['seances_dues'],
                 len(l['ateliers']), couv[0], couv[1], l['touches'], l['prescrits']))
    print()
    for gravite, quoi, detail in alertes(e):
        print('%s %s — %s' % ('!!' if gravite == 'grave' else ' ·', quoi, detail))
    if not alertes(e):
        print('Rien à signaler.')
    return 0


# ── La page ──────────────────────────────────────────────────────────────

def page(e):
    niveaux = e['niveaux']
    seances_f = sum(l['seances_faites'] for l in niveaux.values())
    seances_d = sum(l['seances_dues'] for l in niveaux.values())
    mp3 = sum(m['mp3'] for m in e['mods'])
    ateliers = sum(len(l['ateliers']) for l in niveaux.values())
    touches = sum(l['touches'] for l in niveaux.values())
    prescrits = sum(l['prescrits'] for l in niveaux.values())
    sit_f = sum(v[0] for v in e['situations'].values()) or 0
    sit_d = sum(v[1] for v in e['situations'].values()) or \
        sum(l['situations'] for l in niveaux.values())

    tuiles = [
        (nb(len(e['mods'])), 'modules', '%d niveaux' % len(niveaux)),
        ('%s / %s' % (nb(seances_f), nb(seances_d)), 'séances en PowerPoint',
         '%d %%' % round(100 * seances_f / seances_d) if seances_d else '—'),
        (nb(len(e['activites'])), 'activités au catalogue',
         ' · '.join('%d %s' % (v, k) for k, v in sorted(e['categories'].items()))),
        (nb(ateliers), 'ateliers de banque',
         '%d savoirs touchés' % touches),
        (nb(mp3), 'pistes audio des modules',
         '%s fiches élèves' % nb(sum(m['fiches'] for m in e['mods']))),
        ('%d / %d' % (sit_f, sit_d), 'situations du programme couvertes',
         '%d %%' % round(100 * sit_f / sit_d) if sit_d else '—'),
    ]
    html_tuiles = ''.join(
        '<div class="tuile"><b>%s</b><span>%s</span><i>%s</i></div>'
        % (html.escape(v), html.escape(t), html.escape(d)) for v, t, d in tuiles)

    liste = alertes(e)
    if liste:
        html_alertes = ''.join(
            '<li class="al %s"><span class="al-m">%s</span><div>'
            '<p class="al-t">%s</p><p class="al-d">%s</p></div></li>'
            % (g, '!' if g == 'grave' else '·', html.escape(q), html.escape(d))
            for g, q, d in liste)
    else:
        html_alertes = ('<li class="al calme"><span class="al-m">✓</span><div>'
                        '<p class="al-t">Rien à signaler.</p><p class="al-d">Tous '
                        'les modules ont leurs séances, leur audio et leur entrée '
                        'au catalogue ; aucun lien cassé.</p></div></li>')

    cartes = []
    for niv, l in sorted(niveaux.items()):
        pct_s = round(100 * l['seances_faites'] / l['seances_dues']) \
            if l['seances_dues'] else 0
        pct_sav = round(100 * l['touches'] / l['prescrits']) if l['prescrits'] else 0
        sit = e['situations'].get(niv, (0, l['situations']))
        rangs = ''.join(
            '<tr class="%s"><td class="n">%d</td><td>%s<i>%s</i></td>'
            '<td class="n">%d/%d</td><td class="n">%s</td><td class="n">%d</td></tr>'
            % ('' if m['pptx'] >= m['seances'] and m['mp3'] else 'creux',
               m['numero'], html.escape(m['titre']), html.escape(m['slug']),
               m['pptx'], m['seances'], nb(m['mp3']), m['fiches'])
            for m in l['mods'])
        if not rangs:
            rangs = ('<tr><td colspan="5" class="vide">Aucun module à ce niveau.'
                     '</td></tr>')
        cartes.append("""
        <article class="niv" style="--c:%s;--f:%s">
          <header>
            <p class="niv-e">Niveau %d · %s</p>
            <h3>%s</h3>
          </header>
          <div class="chiffres">
            <div><b>%d</b><span>modules</span></div>
            <div><b>%d</b><span>ateliers</span></div>
            <div><b>%d/%d</b><span>situations</span></div>
            <div><b>%s</b><span>MP3</span></div>
          </div>
          <p class="jauge-l">Séances en PowerPoint — %d sur %d</p>
          <div class="jauge"><div class="jauge-in" style="width:%d%%"></div></div>
          <p class="jauge-l">Savoirs du programme touchés par un atelier — %d sur %d</p>
          <div class="jauge"><div class="jauge-in" style="width:%d%%"></div></div>
          <details>
            <summary>Les %d modules du niveau</summary>
            <table>
              <thead><tr><th class="n">N°</th><th>Module</th><th class="n">Séances</th>
                <th class="n">MP3</th><th class="n">Fiches</th></tr></thead>
              <tbody>%s</tbody>
            </table>
          </details>
        </article>""" % (COULEURS[niv], FONDS[niv], niv, html.escape(l['stade']),
                         html.escape(l['titre']), l['modules'], len(l['ateliers']),
                         sit[0], sit[1], nb(l['mp3']), l['seances_faites'],
                         l['seances_dues'], pct_s, l['touches'], l['prescrits'],
                         pct_sav, len(l['mods']), rangs))

    d = e['depense']
    if d is None:
        html_depense = ('<p class="note">Aucun registre d’appels sur ce poste '
                        '(<code>data/appels_api.jsonl</code>).</p>')
    else:
        routes = ''.join(
            '<tr><td>%s</td><td class="n">%s</td><td class="n">%.4f $</td></tr>'
            % (html.escape(r['route']), nb(r['appels']), r['cout'])
            for r in d['routes']) or \
            '<tr><td colspan="3" class="vide">Registre vide.</td></tr>'
        html_depense = ("""
          <p class="note">%s appels payants enregistrés%s, pour <b>%.4f $</b>
            estimés. <b>C’est le registre de ce poste</b> : celui qui compte vit
            sur le volume Railway et se lit par <code>GET /api/admin/appels</code>.</p>
          <table class="plate">
            <thead><tr><th>Route</th><th class="n">Appels</th><th class="n">Coût</th></tr></thead>
            <tbody>%s</tbody>
          </table>""" % (nb(d['appels']),
                         ' depuis le %s' % d['depuis'] if d['depuis'] else '',
                         d['cout'], routes))

    g = e['git']
    commits = ''.join(
        '<li><code>%s</code> <span class="date">%s</span> %s</li>'
        % (html.escape(c[0]), html.escape(c[1]), html.escape(c[2]))
        for c in g['commits']) or '<li class="vide">Aucun commit lisible.</li>'

    return GABARIT % {
        'maintenant': en_francais(datetime.datetime.now()),
        'tuiles': html_tuiles, 'alertes': html_alertes, 'cartes': ''.join(cartes),
        'depense': html_depense, 'commits': commits,
        'sales': g['sales'], 'devant': g['devant'],
    }


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le tableau de bord du projet — francis</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<link rel="stylesheet" href="../design-system/marque-francis.css">
<link rel="icon" type="image/svg+xml" href="../design-system/marque-francis-favicon.svg">
<style>
  /* Page générée par build/tableau_bord.py — ne pas retoucher à la main.
     Téléphone d'abord : une colonne, des chiffres gros, les alertes en haut. */
  :root{
    --ink-900:#17181A; --ink-700:#3A3D40; --ink-500:#4B4F52; --ink-400:#6E7175;
    --surface-page:#F7F7F5; --surface-card:#FFFFFF;
    --border:#EAEAE8; --border-firm:#D6D6D2;
    --grave:#A8321F; --grave-f:#FBEAE6; --tiede:#8C6A07; --tiede-f:#F7F0DA;
    --calme:#0D7A6F; --calme-f:#DCF2EF;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:var(--font-sans);background:var(--surface-page);
       color:var(--ink-900);line-height:1.5;-webkit-text-size-adjust:100%%}
  .wrap{max-width:900px;margin:0 auto;padding:24px 16px 64px}
  .eyebrow{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
           color:var(--ink-400);margin:0 0 6px}
  h1{font-size:28px;font-weight:900;letter-spacing:-.02em;margin:0 0 8px}
  .sous{color:var(--ink-500);margin:0 0 4px}
  .quand{color:var(--ink-400);font-size:14px;margin:0 0 24px}
  h2.sect{font-size:15px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;
          color:var(--ink-400);margin:32px 0 12px}
  .tuiles{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}
  .tuile{background:var(--surface-card);border:1px solid var(--border);
         border-radius:14px;padding:14px 16px}
  .tuile b{display:block;font-size:26px;font-weight:900;letter-spacing:-.02em;
           font-variant-numeric:tabular-nums}
  .tuile span{display:block;font-size:13px;color:var(--ink-500);font-weight:700}
  .tuile i{display:block;font-style:normal;font-size:12px;color:var(--ink-400);
           margin-top:2px}
  ul.alertes{list-style:none;padding:0;margin:0}
  .al{display:flex;gap:12px;background:var(--surface-card);border:1px solid var(--border);
      border-left:5px solid var(--border-firm);border-radius:14px;
      padding:12px 16px;margin:0 0 8px}
  .al-m{font-size:18px;font-weight:900;line-height:1.4;color:var(--ink-400)}
  .al.grave{border-left-color:var(--grave);background:var(--grave-f)}
  .al.grave .al-m{color:var(--grave)}
  .al.tiede{border-left-color:var(--tiede);background:var(--tiede-f)}
  .al.tiede .al-m{color:var(--tiede)}
  .al.calme{border-left-color:var(--calme);background:var(--calme-f)}
  .al.calme .al-m{color:var(--calme)}
  .al-t{margin:0;font-weight:800;font-size:15px}
  .al-d{margin:2px 0 0;font-size:13px;color:var(--ink-500);word-break:break-word}
  .niv{background:var(--surface-card);border:1px solid var(--border);
       border-left:5px solid var(--c);border-radius:14px;padding:16px;margin:0 0 12px}
  .niv-e{margin:0 0 2px;font-size:12px;font-weight:800;letter-spacing:.06em;
         text-transform:uppercase;color:var(--c)}
  .niv h3{font-size:19px;font-weight:900;margin:0 0 12px;letter-spacing:-.01em}
  .chiffres{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:0 0 14px}
  .chiffres div{background:var(--f);border-radius:10px;padding:8px 10px}
  .chiffres b{display:block;font-size:19px;font-weight:900;color:var(--c);
              font-variant-numeric:tabular-nums}
  .chiffres span{font-size:11px;color:var(--ink-500)}
  .jauge{height:8px;background:var(--f);border-radius:99px;overflow:hidden;margin:0 0 10px}
  .jauge-in{height:100%%;background:var(--c);border-radius:99px}
  .jauge-l{font-size:13px;color:var(--ink-500);margin:0 0 4px}
  details{margin-top:6px}
  summary{cursor:pointer;font-size:13px;font-weight:800;color:var(--c);
          padding:6px 0;list-style:none}
  summary::-webkit-details-marker{display:none}
  summary::before{content:"▸ ";}
  details[open] summary::before{content:"▾ ";}
  table{border-collapse:collapse;width:100%%;margin-top:6px}
  th,td{text-align:left;padding:7px 8px;border-bottom:1px solid var(--border);
        font-size:13px;vertical-align:top}
  thead th{font-size:11px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;
           color:var(--ink-400);white-space:nowrap}
  td i{display:block;font-style:normal;font-size:11px;color:var(--ink-400)}
  .n{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
  tr.creux td{background:#FCFBF6}
  td.vide{color:var(--ink-400);text-align:center}
  table.plate{background:var(--surface-card);border:1px solid var(--border);
              border-radius:14px;overflow:hidden}
  table.plate th,table.plate td{padding:10px 14px}
  .note{font-size:14px;color:var(--ink-500);margin:0 0 10px}
  ul.commits{list-style:none;padding:0;margin:0;background:var(--surface-card);
             border:1px solid var(--border);border-radius:14px}
  ul.commits li{padding:9px 14px;border-bottom:1px solid var(--border);font-size:14px}
  ul.commits li:last-child{border-bottom:0}
  .date{color:var(--ink-400);font-size:12px;margin:0 6px}
  code{background:#EFEFED;border-radius:6px;padding:1px 5px;font-size:12px}
  footer{margin-top:36px;padding-top:16px;border-top:1px solid var(--border);
         color:var(--ink-400);font-size:13px}
  @media(min-width:700px){.tuiles{grid-template-columns:repeat(3,1fr)}h1{font-size:34px}}
</style>
</head>
<body>
<div class="fr-barre">
  <div class="fr-barre__in">
    <span class="fr-lockup">
      <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
      <span class="fr-trait" aria-hidden="true"></span>
      <span class="fr-desc">Aide à l'apprentissage du français</span>
    </span>
  </div>
</div>
<div class="wrap">
  <header>
    <p class="eyebrow">Francisation · État de la production</p>
    <h1>Le tableau de bord du projet</h1>
    <p class="sous">Tout l’état de la production sur une page : ce qui est
      produit, ce qui manque, ce que ça coûte. Aucun chiffre n’est saisi à la
      main — ils sont relus sur le disque à chaque construction.</p>
    <p class="quand">État lu le %(maintenant)s.</p>
  </header>

  <div class="tuiles">%(tuiles)s</div>

  <h2 class="sect">Ce qui demande une action</h2>
  <ul class="alertes">%(alertes)s</ul>

  <h2 class="sect">Niveau par niveau</h2>
  %(cartes)s

  <h2 class="sect">La dépense</h2>
  %(depense)s

  <h2 class="sect">Les derniers commits</h2>
  <p class="note">%(sales)d fichier(s) modifiés non commités · %(devant)d commit(s)
    non poussés. Railway déploie sur <code>push</code> : ce qui n’est pas poussé
    n’est pas en ligne.</p>
  <ul class="commits">%(commits)s</ul>

  <footer>
    <p>Page générée par <code>python3 build/tableau_bord.py</code>, et l’état en
      clair dans un terminal par <code>python3 build/tableau_bord.py --texte</code>.</p>
    <p>Les détails d’un chantier restent dans leur page :
      <a href="chantier-banques.html">les banques d’exercices</a>,
      <code>build/bilan_programme.py</code> pour la couverture du programme,
      <code>build/couts_api.py</code> pour le registre des appels.</p>
  </footer>
</div>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--texte', action='store_true', help="l'état en clair, sans écrire")
    ap.add_argument('--ou', default=str(SORTIE))
    a = ap.parse_args()
    etat = releve()
    if a.texte:
        return texte(etat)
    cible = pathlib.Path(a.ou)
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(page(etat), encoding='utf-8')
    print('→ %s (%d octets)' % (cible, cible.stat().st_size))
    return 0


if __name__ == '__main__':
    sys.exit(main())
