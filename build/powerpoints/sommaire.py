#!/usr/bin/env python3
"""Produit `assets/powerpoints/<slug>/presentations.html` — le sommaire des
séances d'un module, pour l'enseignante.

    python3 build/powerpoints/sommaire.py module-n3-epicerie
    python3 build/powerpoints/sommaire.py --tous
    python3 build/powerpoints/sommaire.py --verifier

Pourquoi ce fichier existe
--------------------------
`data/activities.json` annonce pour chaque module un lien « diaporamas » vers
`assets/powerpoints/<slug>/presentations.html`. Cette page n'existait que pour
`module-probleme`, écrite à la main — et elle portait « Module 9 » alors que
le registre disait 10. Les huit autres modules pointaient vers un fichier
absent : un 404 dans le catalogue de l'enseignante.

Tout vient d'ici : le registre `modules.py` pour le numéro, le niveau, le
titre et les blocs ; `data/materiel.json` pour la liste réelle des séances,
leur titre, leur durée, leur nombre de diapositives et le chemin de leur fiche
élève. Rien n'est écrit à la main, donc rien ne peut se périmer.

Le CSS reprend celui de la page écrite à la main, qui n'assemble que des
jetons du système de design (`assets/design-system/styles.css`).
"""
import argparse
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from modules import MODULES, ORDRE  # noqa: E402

MATERIEL = ROOT / 'data/materiel.json'

CSS = """
.som          { padding: var(--sp-8) 0 var(--sp-12); }
.som__bloc    { margin-top: var(--sp-12); }
.som__bloc:first-child { margin-top: 0; }
.som__head    { display: flex; flex-wrap: wrap; align-items: center; gap: var(--sp-4);
                margin-bottom: var(--sp-5); }
.som__lettre  { flex-shrink: 0; width: 44px; height: 44px; border-radius: var(--r-md);
                display: flex; align-items: center; justify-content: center;
                background: var(--accent-soft); color: var(--accent-ink);
                font-size: 19px; font-weight: var(--fw-black); }
.som__titre   { font-size: var(--fs-h3); font-weight: var(--fw-black); margin: 0; }
.som__rule    { flex: 1; height: 1px; background: var(--border); }
.som__compte  { background: var(--accent-soft); color: var(--accent-ink);
                padding: 6px var(--sp-3); border-radius: var(--r-pill);
                font-size: var(--fs-ui-sm); font-weight: var(--fw-bold);
                white-space: nowrap; }

.seance       { display: grid; grid-template-columns: 56px minmax(0, 1fr) auto;
                gap: var(--sp-4); align-items: start; }
.seance__code { grid-row: 1 / -1; width: 56px; height: 56px; border-radius: var(--r-md);
                display: flex; align-items: center; justify-content: center;
                border: 1px solid var(--border); background: var(--surface-sunken);
                color: var(--text-strong);
                font-size: var(--fs-lead); font-weight: var(--fw-black);
                letter-spacing: .02em; }
.seance__nom  { font-size: var(--fs-lead); font-weight: var(--fw-black);
                color: var(--text-strong); margin: 0 0 2px; line-height: var(--lh-title); }
.seance__quoi { font-size: var(--fs-body-sm); font-weight: var(--fw-medium);
                color: var(--text-body); line-height: var(--lh-body); margin: 0; }
.seance__meta { display: flex; flex-wrap: wrap; gap: var(--sp-3);
                margin-top: var(--sp-2);
                font-size: var(--fs-meta); font-weight: var(--fw-bold);
                letter-spacing: var(--ls-label); text-transform: uppercase;
                color: var(--text-muted); }
.seance__liens{ grid-column: 3; grid-row: 1 / -1;
                display: flex; flex-direction: column; gap: var(--sp-2);
                align-items: stretch; }
.seance__liens .btn { justify-content: center; white-space: nowrap; }

/* Sous 720 px : le code passe au-dessus, les liens en pleine largeur. */
@media (max-width: 720px) {
  .seance        { grid-template-columns: 56px minmax(0, 1fr); }
  .seance__liens { grid-column: 1 / -1; grid-row: auto; flex-direction: row;
                   flex-wrap: wrap; margin-top: var(--sp-4); }
  .seance__liens .btn { flex: 1 1 200px; }
}
"""


def _en_lettres(n):
    """« Les huit présentations », pas « Les 8 » : c'est un titre, pas un
    tableau de bord. Même table que `build_fiches.py`."""
    mots = {1: 'Une', 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq', 6: 'Six',
            7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix', 11: 'Onze',
            12: 'Douze', 13: 'Treize', 14: 'Quatorze', 15: 'Quinze',
            16: 'Seize', 17: 'Dix-sept', 18: 'Dix-huit'}
    return mots.get(n, str(n))


def fatal(msg):
    sys.exit('!! %s' % msg)


def porteurs():
    if not MATERIEL.exists():
        fatal('data/materiel.json absent — lancer d\'abord : python3 build/materiel.py')
    d = json.loads(MATERIEL.read_text(encoding='utf-8'))
    return {p['slug']: p for p in d.get('porteurs', []) if p.get('slug')}


def e(s):
    return html.escape(str(s), quote=True)


def heures(minutes):
    """« Environ 18 heures » — un ordre de grandeur, pas une comptabilité."""
    return 'Environ %d heures de classe' % round(minutes / 60)


def page(slug, p):
    m = MODULES[slug]
    seances = p.get('seances') or []
    if not seances:
        fatal('%s : aucune séance dans materiel.json' % slug)

    total_diapos = 0
    total_minutes = 0
    for s in seances:
        for f in s.get('fichiers', []):
            if f.get('type') == 'presentation':
                total_diapos += f.get('diapositives') or 0
        try:
            total_minutes += int(str(s.get('duree', '0')).split()[0])
        except (ValueError, IndexError):
            pass

    parts = []
    parts.append('<!DOCTYPE html>\n<html lang="fr"><head><meta charset="utf-8">')
    parts.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
    parts.append('<title>Module %d · Les %s présentations</title>'
                 % (m['numero'], _en_lettres(len(seances)).lower()))
    parts.append('<link rel="stylesheet" href="/assets/design-system/styles.css">')
    parts.append('<style>%s</style></head>' % CSS)
    parts.append('<body class="page">\n')
    parts.append('<header class="band">\n  <div class="container">')
    parts.append('    <p class="band__eyebrow">Module %d · Français niveau %d · '
                 'Matériel de l\'enseignant</p>' % (m['numero'], m.get('niveau', 4)))
    parts.append('    <h1 style="font-size:var(--fs-hero);font-weight:var(--fw-black);'
                 'line-height:var(--lh-hero);letter-spacing:var(--ls-hero);'
                 'margin:var(--sp-3) 0 0">%s</h1>' % e(m['titre']))
    parts.append('    <p class="band__lead">%s Chaque séance a sa fiche élève '
                 'correspondante, en noir et blanc, prête à photocopier.</p>'
                 % e(m.get('chapeau', '')))
    parts.append('    <p class="seance__meta" style="margin-top:var(--sp-5)">')
    parts.append('      <span>%d séances</span><span>%d diapositives</span>'
                 '<span>%s</span>' % (len(seances), total_diapos, heures(total_minutes)))
    parts.append('    </p>\n  </div>\n</header>\n')
    parts.append('<main class="container som">\n')

    par_bloc = {}
    for s in seances:
        par_bloc.setdefault(s.get('bloc', '?'), []).append(s)

    for lettre in sorted(par_bloc):
        groupe = par_bloc[lettre]
        minutes = 0
        for s in groupe:
            try:
                minutes += int(str(s.get('duree', '0')).split()[0])
            except (ValueError, IndexError):
                pass
        parts.append('  <section class="som__bloc">')
        parts.append('    <div class="som__head">')
        parts.append('      <span class="som__lettre">%s</span>' % e(lettre))
        parts.append('      <h2 class="som__titre">%s</h2>'
                     % e(m['blocs'].get(lettre, '')))
        parts.append('      <span class="som__rule"></span>')
        parts.append('      <span class="som__compte">%d séance%s · %d min</span>'
                     % (len(groupe), 's' if len(groupe) > 1 else '', minutes))
        parts.append('    </div>\n    <div class="stack">\n')

        for s in groupe:
            pptx = fiche = None
            diapos = 0
            resume = ''
            for f in s.get('fichiers', []):
                if f.get('type') == 'presentation':
                    pptx = f.get('chemin')
                    diapos = f.get('diapositives') or 0
                    resume = f.get('resume') or resume
                elif f.get('type') == 'fiche':
                    fiche = f.get('chemin')
            parts.append('      <article class="card seance">')
            parts.append('        <span class="seance__code">%s</span>' % e(s['code']))
            parts.append('        <div>')
            parts.append('          <h3 class="seance__nom">%s</h3>' % e(s.get('titre', '')))
            if resume:
                parts.append('          <p class="seance__quoi">%s</p>' % e(resume))
            parts.append('          <p class="seance__meta"><span>%s</span>'
                         '<span>%d diapositives</span></p>'
                         % (e(s.get('duree', '')), diapos))
            parts.append('        </div>')
            parts.append('        <div class="seance__liens">')
            if pptx:
                parts.append('          <a class="btn btn--pri" href="/%s">Présentation</a>'
                             % e(pptx))
            if fiche:
                parts.append('          <a class="btn btn--ghost" href="/%s" '
                             'target="_blank" rel="noopener">Fiche élève</a>' % e(fiche))
            parts.append('        </div>\n      </article>\n')
        parts.append('    </div>\n  </section>\n')

    parts.append('</main>\n</body></html>\n')
    return '\n'.join(parts)


def construire(slug, tous_porteurs, verbeux=True):
    if slug not in MODULES:
        fatal('%s absent du registre build/powerpoints/modules.py' % slug)
    p = tous_porteurs.get(slug)
    if not p:
        fatal('%s absent de data/materiel.json — lancer python3 build/materiel.py' % slug)
    dst = ROOT / 'assets/powerpoints' / slug / 'presentations.html'
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(page(slug, p), encoding='utf-8')
    if verbeux:
        print('OK  %-24s %d séances' % (slug, len(p.get('seances') or [])))
    return dst


def verifier(tous_porteurs):
    """Le lien « diaporamas » de chaque module mène-t-il quelque part ?"""
    acts = json.loads((ROOT / 'data/activities.json').read_text(encoding='utf-8'))
    par_activite = {m.get('activite'): s for s, m in MODULES.items()}
    manquants = []
    for a in acts:
        chemin = a.get('slideshow')
        if chemin and not (ROOT / chemin).exists():
            manquants.append((a['id'], par_activite.get(a['id'], '?'), chemin))
    for i, slug, chemin in manquants:
        print('!! activité %-3s %-24s %s' % (i, slug, chemin))
    print('%d lien(s) « diaporamas » cassé(s)' % len(manquants))
    return 1 if manquants else 0


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('slug', nargs='?')
    p.add_argument('--tous', action='store_true')
    p.add_argument('--verifier', action='store_true')
    a = p.parse_args()

    tous = porteurs()
    if a.verifier:
        sys.exit(verifier(tous))
    if a.tous:
        faits = [construire(s, tous) for s in ORDRE if s in tous]
        print('\n%d sommaire(s) produit(s).' % len(faits))
    elif a.slug:
        construire(a.slug, tous)
    else:
        print(__doc__)


if __name__ == '__main__':
    main()
