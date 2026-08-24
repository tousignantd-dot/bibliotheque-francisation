#!/usr/bin/env python3
"""La page de chantier des banques d'exercices — l'état réel, lu sur le disque.

    python3 build/chantier.py            → écrit assets/presentations/chantier-banques.html
    python3 build/chantier.py --texte    → le même état, en clair dans le terminal

Pourquoi cette page existe
--------------------------
Écrite le 24 août 2026, pendant la production des banques des niveaux 2 à 8,
pour une raison simple : l'utilisateur est parti pour quelques heures et
voulait suivre les travaux depuis son téléphone. Le fil des commits dit ce qui
est poussé ; il ne dit pas où on en est.

**Rien ici n'est écrit à la main, sauf le plan.** Les compteurs viennent du
disque à chaque construction :

  · les modules, du registre `build/powerpoints/modules.py` ;
  · les ateliers, du registre de `build/banque.py`, qui balaie les contenus ;
  · les savoirs prescrits, du dépouillement du programme ;
  · les savoirs touchés, des clés `savoirs` des contenus d'ateliers.

Le seul morceau déclaratif est `VAGUES` — l'ordre de production décidé. Son
avancement, lui, est calculé : une vague est faite quand ses ateliers sont sur
le disque, pas quand quelqu'un l'a cochée.
"""
import argparse
import datetime
import html
import json
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
PROGRAMME = (pathlib.Path.home() / 'Claude' / 'programme'
             / 'programme-francisation.json')
SORTIE = RACINE / 'assets/presentations/chantier-banques.html'

# Le plan de production, et lui seul. Chaque vague dit les niveaux qu'elle
# couvre et la cible d'ateliers par niveau ; l'avancement est compté sur le
# disque, jamais coché ici.
#
# La cible a été ramenée de dix à six par niveau après la première vague : à
# six ateliers, le niveau 2 touchait déjà 27 de ses 49 savoirs, et les quatre
# suivants seraient tombés sur des savoirs que ses dix modules drainent déjà.
# Le raisonnement est dans docs/plan-banques-niveaux-2-8.md.
VAGUES = [
    ('Temps 0', 'Le registre commun',
     "Les quatre générateurs débranchés du niveau 1 : un atelier se déclare "
     "lui-même, le repérage suit son niveau.", [], 0),
    ('Temps 1', 'Les deux formes neuves',
     "« Lire un texte » et « conjuguer » — les deux formes que le profil des "
     "savoirs réclame à partir du niveau 5, où le lexique triple et la "
     "phonétique disparaît.", [], 0),
    ('Vague 1', 'Niveaux 2 et 3',
     "Les formes du niveau 1 s'y appliquent telles quelles : c'est le test le "
     "moins cher de la généralisation. Quatre savoirs phonétiques chacun, "
     "donc la famille B sert une dernière fois.", [2, 3], 6),
    ('Vague 2', 'Niveaux 7 et 8',
     "Les plus éloignés du niveau 1, donc ceux qui valident vraiment la "
     "famille « lire un texte ». Un seul savoir phonétique de chaque côté.",
     [7, 8], 6),
    ('Vague 3', 'Niveaux 5 et 6',
     "Le niveau 5 porte 78 savoirs, le plus lourd des huit, dont 34 lexicaux.",
     [5, 6], 6),
    ('Vague 4', 'Rattrapage du niveau 4',
     "Le niveau 4 a déjà cinquante et une activités, mais aucune banque "
     "raisonnée : quelques ateliers sur ses savoirs orphelins.", [4], 6),
]


def programme():
    d = json.loads(PROGRAMME.read_text(encoding='utf-8'))
    return {lv['niveau']: lv for lv in d['niveaux']}


def modules_par_niveau():
    from modules import MODULES
    compte = {}
    for fiche in MODULES.values():
        compte[fiche.get('niveau', 4)] = compte.get(fiche.get('niveau', 4), 0) + 1
    return compte


def releve():
    """Ce que le disque dit, niveau par niveau."""
    from banque import registre, audio_complet, SONORES
    prog = programme()
    mods = modules_par_niveau()
    acts = json.loads((RACINE / 'data/activities.json').read_text(encoding='utf-8'))
    au_catalogue = set()
    for a in acts:
        c = a.get('interactive') or ''
        if c.startswith('assets/interactive/'):
            au_catalogue.add(c.split('/')[2])

    lignes = {}
    for niv in range(1, 9):
        entrees = registre(niveau=niv)
        savoirs_vus = set()
        jouables = catalogues = 0
        ateliers = []
        for e in entrees:
            savoirs_vus |= set(e['savoirs'])
            son = audio_complet(e['slug'], e['items'])
            pret = son or e['generateur'] not in SONORES
            jouables += 1 if pret else 0
            catalogues += 1 if e['slug'] in au_catalogue else 0
            ateliers.append({
                'slug': e['slug'], 'titre': e['titre'] or e['slug'],
                'famille': e['generateur'], 'items': len(e['items']),
                'activite': e['activite'], 'pret': pret,
                'catalogue': e['slug'] in au_catalogue,
                'savoirs': e['savoirs'],
            })
        prescrits = [s['id'] for s in prog[niv]['savoirs']]
        lignes[niv] = {
            'niveau': niv,
            'titre': prog[niv]['titre'],
            'stade': prog[niv]['stade'],
            'situations': len(prog[niv]['situations']),
            'modules': mods.get(niv, 0),
            'ateliers': ateliers,
            'jouables': jouables,
            'catalogue': catalogues,
            'prescrits': len(prescrits),
            'touches': len(savoirs_vus & set(prescrits)),
            'manquants': [s for s in prescrits if s not in savoirs_vus],
        }
    return lignes


def etat_vagues(lignes):
    """L'avancement d'une vague, compté sur le disque."""
    faites = []
    for code, titre, quoi, niveaux, cible in VAGUES:
        if not niveaux:
            # Les deux temps de socle : faits quand leur générateur existe.
            fait = (code == 'Temps 0'
                    and (RACINE / 'build/banque.py').exists()) or \
                   (code == 'Temps 1'
                    and (RACINE / 'build/texte.py').exists()
                    and (RACINE / 'build/conjugaison.py').exists())
            faites.append((code, titre, quoi, niveaux, cible,
                           1.0 if fait else 0.0, ''))
            continue
        total = sum(len(lignes[n]['ateliers']) for n in niveaux)
        vise = cible * len(niveaux)
        faites.append((code, titre, quoi, niveaux, cible,
                       min(1.0, total / vise) if vise else 0.0,
                       '%d / %d ateliers' % (total, vise)))
    return faites


COULEURS = {1: '#A5335F', 2: '#A83A22', 3: '#B45309', 4: '#8C6A07',
            5: '#0D7A6F', 6: '#1D6B8F', 7: '#3B49A0', 8: '#7E3F98'}
FONDS = {1: '#FCE9F0', 2: '#FBEAE4', 3: '#FBEEDC', 4: '#F7F0DA',
         5: '#DCF2EF', 6: '#E7F0F6', 7: '#E8EAFA', 8: '#F3E8F7'}
NOMS_FAMILLE = {'appariement': 'apparier', 'oreille': 'écouter',
                'phrase': 'construire', 'graphie': 'écrire',
                'texte': 'lire un texte', 'conjugaison': 'conjuguer',
                'polices': 'apparier'}
MOIS = ('janvier février mars avril mai juin juillet août septembre '
        'octobre novembre décembre').split()


def en_francais(d):
    return '%d %s %d, %dh%02d' % (d.day, MOIS[d.month - 1], d.year, d.hour, d.minute)


def texte(lignes):
    for niv in sorted(lignes):
        l = lignes[niv]
        print('Niveau %d — %d modules · %d ateliers (%d jouables, %d au catalogue) '
              '· %d/%d savoirs'
              % (niv, l['modules'], len(l['ateliers']), l['jouables'],
                 l['catalogue'], l['touches'], l['prescrits']))
    total = sum(len(l['ateliers']) for l in lignes.values())
    print('\n%d ateliers en tout.' % total)
    return 0


def page(lignes):
    maintenant = en_francais(datetime.datetime.now())
    total = sum(len(l['ateliers']) for l in lignes.values())
    jouables = sum(l['jouables'] for l in lignes.values())
    catalogue = sum(l['catalogue'] for l in lignes.values())
    touches = sum(l['touches'] for l in lignes.values())
    prescrits = sum(l['prescrits'] for l in lignes.values())

    cartes = []
    for niv in sorted(lignes):
        l = lignes[niv]
        pct = round(100 * l['touches'] / l['prescrits']) if l['prescrits'] else 0
        ats = ''.join(
            '<li class="at %s"><span class="at-t">%s</span>'
            '<span class="at-m">%s · %d items · %s</span></li>'
            % ('ok' if a['catalogue'] else ('pret' if a['pret'] else 'attente'),
               html.escape(a['titre']),
               NOMS_FAMILLE.get(a['famille'], a['famille']), a['items'],
               ('activité %s' % a['activite'] if a['catalogue']
                else ('prêt, hors catalogue' if a['pret'] else 'attend son audio')))
            for a in l['ateliers'])
        if not ats:
            ats = '<li class="at vide">Aucun atelier — la banque de ce niveau reste à faire.</li>'
        cartes.append("""
        <article class="niv" style="--c:%s;--f:%s">
          <header>
            <p class="niv-e">Niveau %d · %s</p>
            <h2>%s</h2>
          </header>
          <div class="chiffres">
            <div><b>%d</b><span>situations</span></div>
            <div><b>%d</b><span>modules</span></div>
            <div><b>%d</b><span>ateliers</span></div>
            <div><b>%d</b><span>au catalogue</span></div>
          </div>
          <div class="jauge" title="%d savoirs touchés sur %d">
            <div class="jauge-in" style="width:%d%%"></div>
          </div>
          <p class="jauge-l">%d des %d savoirs du programme sont touchés par la
             banque — %d %%</p>
          <ul class="ats">%s</ul>
        </article>""" % (COULEURS[niv], FONDS[niv], niv, html.escape(l['stade']),
                         html.escape(l['titre']), l['situations'], l['modules'],
                         len(l['ateliers']), l['catalogue'], l['touches'],
                         l['prescrits'], pct, l['touches'], l['prescrits'], pct, ats))

    vagues = []
    for code, titre, quoi, niveaux, cible, avance, detail in etat_vagues(lignes):
        etat = 'fait' if avance >= 1 else ('encours' if avance > 0 else 'attente')
        marque = '✓' if avance >= 1 else ('◐' if avance > 0 else '○')
        vagues.append("""
        <li class="vague %s">
          <span class="v-m">%s</span>
          <div>
            <p class="v-t"><b>%s</b> — %s <span class="v-d">%s</span></p>
            <p class="v-q">%s</p>
          </div>
        </li>""" % (etat, marque, html.escape(code), html.escape(titre),
                    html.escape(detail), html.escape(quoi)))

    return GABARIT % {
        'maintenant': maintenant, 'total': total, 'jouables': jouables,
        'catalogue': catalogue, 'touches': touches, 'prescrits': prescrits,
        'cartes': ''.join(cartes), 'vagues': ''.join(vagues),
    }


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Le chantier des banques d'exercices — SAAF</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<link rel="stylesheet" href="../design-system/marque-saaf.css">
<link rel="icon" type="image/svg+xml" href="../design-system/marque-saaf-favicon.svg">
<style>
  /* Page générée par build/chantier.py — ne pas retoucher à la main.
     Pensée pour un téléphone d'abord : une colonne, des chiffres gros. */
  :root{
    --ink-900:#17181A; --ink-700:#3A3D40; --ink-500:#4B4F52; --ink-400:#6E7175;
    --surface-page:#F7F7F5; --surface-card:#FFFFFF;
    --border:#EAEAE8; --border-firm:#D6D6D2;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:var(--font-sans);background:var(--surface-page);
       color:var(--ink-900);line-height:1.5;-webkit-text-size-adjust:100%%}
  .wrap{max-width:820px;margin:0 auto;padding:24px 16px 64px}
  header.top{padding:8px 0 4px}
  .eyebrow{font-size:13px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;
           color:var(--ink-400);margin:0 0 6px}
  h1{font-size:28px;font-weight:900;letter-spacing:-.02em;margin:0 0 8px}
  .sous{color:var(--ink-500);margin:0 0 4px}
  .quand{color:var(--ink-400);font-size:14px;margin:0 0 24px}
  .bilan{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin:0 0 28px}
  .bilan div{background:var(--surface-card);border:1px solid var(--border);
             border-radius:14px;padding:14px 16px}
  .bilan b{display:block;font-size:26px;font-weight:900;letter-spacing:-.02em}
  .bilan span{font-size:13px;color:var(--ink-500)}
  h2.sect{font-size:15px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;
          color:var(--ink-400);margin:32px 0 12px}
  ul.vagues{list-style:none;padding:0;margin:0}
  .vague{display:flex;gap:12px;background:var(--surface-card);border:1px solid var(--border);
         border-radius:14px;padding:14px 16px;margin:0 0 8px}
  .vague .v-m{font-size:20px;line-height:1.2;color:var(--ink-400)}
  .vague.fait .v-m{color:#0D7A6F}
  .vague.encours .v-m{color:#B45309}
  .v-t{margin:0 0 4px;font-size:15px}
  .v-d{color:var(--ink-400);font-weight:600;font-size:13px;margin-left:6px}
  .v-q{margin:0;color:var(--ink-500);font-size:14px}
  .niv{background:var(--surface-card);border:1px solid var(--border);border-left:5px solid var(--c);
       border-radius:14px;padding:16px;margin:0 0 12px}
  .niv-e{margin:0 0 2px;font-size:12px;font-weight:800;letter-spacing:.06em;
         text-transform:uppercase;color:var(--c)}
  .niv h2{font-size:19px;font-weight:900;margin:0 0 12px;letter-spacing:-.01em}
  .chiffres{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:0 0 14px}
  .chiffres div{background:var(--f);border-radius:10px;padding:8px 10px}
  .chiffres b{display:block;font-size:20px;font-weight:900;color:var(--c)}
  .chiffres span{font-size:11px;color:var(--ink-500)}
  .jauge{height:8px;background:var(--f);border-radius:99px;overflow:hidden}
  .jauge-in{height:100%%;background:var(--c);border-radius:99px}
  .jauge-l{font-size:13px;color:var(--ink-500);margin:6px 0 12px}
  ul.ats{list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:4px}
  .at{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;
      padding:7px 10px;border-radius:10px;background:#FBFBFA;border:1px solid var(--border)}
  .at-t{font-weight:700;font-size:14px}
  .at-m{font-size:12px;color:var(--ink-400)}
  .at.ok{border-color:var(--border-firm)}
  .at.attente{opacity:.72}
  .at.vide{color:var(--ink-400);font-size:14px;background:transparent;border-style:dashed}
  footer{margin-top:36px;padding-top:16px;border-top:1px solid var(--border);
         color:var(--ink-400);font-size:13px}
  footer code{background:#EFEFED;border-radius:6px;padding:1px 5px;font-size:12px}
  @media(min-width:640px){.bilan{grid-template-columns:repeat(4,1fr)}h1{font-size:34px}}
</style>
</head>
<body>
<div class="wrap">
  <header class="top">
    <p class="eyebrow">Francisation · SAAF</p>
    <h1>Le chantier des banques d'exercices</h1>
    <p class="sous">Les modules couvrent les 85 situations des huit niveaux. Ce qui
      s'ajoute ici, ce sont les <b>savoirs qu'un module ne peut pas drainer</b> —
      les sons, la graphie, la phrase, le texte — sous forme d'ateliers courts,
      toujours ouverts, sans date ni séance.</p>
    <p class="quand">État lu sur le disque le %(maintenant)s.</p>
  </header>

  <div class="bilan">
    <div><b>%(total)d</b><span>ateliers</span></div>
    <div><b>%(jouables)d</b><span>jouables</span></div>
    <div><b>%(catalogue)d</b><span>au catalogue</span></div>
    <div><b>%(touches)d / %(prescrits)d</b><span>savoirs touchés</span></div>
  </div>

  <h2 class="sect">Le plan, et où il en est</h2>
  <ul class="vagues">%(vagues)s</ul>

  <h2 class="sect">Niveau par niveau</h2>
  %(cartes)s

  <footer>
    <p>Page générée par <code>python3 build/chantier.py</code>. Rien n'y est
      écrit à la main sauf l'ordre des vagues : les compteurs sont relus sur le
      disque à chaque construction, et l'avancement d'une vague est le nombre
      d'ateliers réellement présents.</p>
    <p>L'état en clair, dans un terminal :
      <code>python3 build/banque.py --etat</code>.</p>
  </footer>
</div>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--texte', action='store_true', help="l'état en clair, sans écrire")
    ap.add_argument('--ou', default=str(SORTIE))
    a = ap.parse_args()
    lignes = releve()
    if a.texte:
        return texte(lignes)
    cible = pathlib.Path(a.ou)
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(page(lignes), encoding='utf-8')
    print('→ %s (%d octets)' % (cible, cible.stat().st_size))
    return 0


if __name__ == '__main__':
    sys.exit(main())
