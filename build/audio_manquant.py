#!/usr/bin/env python3
"""Où manque-t-il des pistes audio, et combien.

    python3 build/audio_manquant.py            # le relevé, par niveau puis par module
    python3 build/audio_manquant.py --detail   # + le détail par famille de sons
    python3 build/audio_manquant.py n3         # seulement les slugs contenant « n3 »
    python3 build/audio_manquant.py --json     # le même relevé, pour une page

Compte SANS RIEN APPELER : il lit le disque et les relevés, jamais l'API.

**Deux familles de fichiers, et il faut les deux.** `build/audio_tous.py
--compter` n'en voit qu'une — il additionne ce que les relevés annoncent,
sans retrancher ce qui est déjà produit ni regarder les dialogues. Un module
peut donc y paraître entier et n'avoir aucune réplique enregistrée : c'est
exactement le cas de `module-n3-voisins`, 244 sons sur 244 et pas une seule
ligne de dialogue.

- `assets/interactive/<slug>/sons/<id>.mp3` — les pastilles haut-parleur.
  Attendus = les clés de `sons_<slug>.json`, à la racine du dépôt.
- `assets/interactive/<slug>/<dialogue>/line_NN_<perso>.mp3` — le bouton
  « Écouter » de Je découvre. Attendues = les lignes de
  `build/contenu/<slug>/dialogues.js`.

**Les dix modules sans relevé JSON sont complets.** banque, consultation,
logement, meteo, nouvelles, procedure, pub, sante, travail, urgence : leur
audio a été produit avant que les relevés existent. Sans relevé, on ne sait
pas ce qui est attendu — le script le dit au lieu de compter zéro manquant
et de les déclarer bons.

Les minutes suivent la longueur du texte, à débit constant :
`durée ~ 0,58 s + 0,061 s x caractères`, ajusté sur les clips déjà produits.
C'est un ordre de grandeur pour décider, pas une facture.
"""
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
try:
    from modules import MODULES
except Exception:                                     # pragma: no cover
    MODULES = {}

SECONDES = lambda txt: 0.58 + 0.061 * len(txt)


def famille(cle):
    """À quoi sert ce son — c'est ce qui décide de ce qu'on produit d'abord."""
    if cle.startswith('plus_'):
        return 'mini-leçons'
    if '_savoir_' in cle:
        return 'bandeaux savoir'
    return 'cartes et exercices'


def lignes_de_dialogue(slug):
    """Les répliques déclarées dans build/contenu/<slug>/dialogues.js.

    Le fichier est du JavaScript : on ne l'interprète pas, on relève les
    identifiants de dialogue et on compte les paires ["PERSO","texte"].
    """
    f = RACINE / 'build' / 'contenu' / slug / 'dialogues.js'
    if not f.exists():
        return None
    src = f.read_text(encoding='utf-8')
    out = {}
    for bloc in re.finditer(r'(\w+)\s*:\s*\{\s*label\s*:.*?lines\s*:\s*\[(.*?)\]\s*,?\s*\}',
                            src, re.S):
        did, corps = bloc.group(1), bloc.group(2)
        repliques = re.findall(r'\[\s*"([^"]+)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\]', corps)
        if repliques:
            out[did] = repliques
    return out


def etat(slug):
    d = {'slug': slug, 'niveau': (MODULES.get(slug) or {}).get('niveau'),
         'titre': (MODULES.get(slug) or {}).get('titre', slug),
         'releve': False, 'sons_attendus': 0, 'sons_presents': 0,
         'sons_manquants': 0, 'par_famille': {}, 'sec_sons': 0.0,
         'dial_attendues': 0, 'dial_presentes': 0, 'dial_manquantes': 0,
         'sec_dial': 0.0, 'dial_trous': []}

    releve = RACINE / ('sons_%s.json' % slug.replace('-', '_'))
    dossier = RACINE / 'assets' / 'interactive' / slug
    presents = {p.stem for p in (dossier / 'sons').glob('*.mp3')} \
        if (dossier / 'sons').is_dir() else set()
    d['sons_presents'] = len(presents)

    if releve.exists():
        d['releve'] = True
        attendus = json.loads(releve.read_text(encoding='utf-8'))
        d['sons_attendus'] = len(attendus)
        for cle, txt in attendus.items():
            if cle in presents:
                continue
            d['sons_manquants'] += 1
            f = famille(cle)
            d['par_famille'][f] = d['par_famille'].get(f, 0) + 1
            d['sec_sons'] += SECONDES(txt if isinstance(txt, str) else '')

    dial = lignes_de_dialogue(slug)
    if dial is not None:
        for did, repliques in dial.items():
            d['dial_attendues'] += len(repliques)
            # Le numéro vient du NOM du fichier, jamais du compte : plusieurs
            # dossiers commencent à line_02 ou sautent une réplique, et
            # additionner les fichiers déclarerait complète une série trouée.
            rangs = set()
            if (dossier / did).is_dir():
                for f in (dossier / did).glob('line_*.mp3'):
                    m = re.match(r'line_(\d+)_', f.name)
                    if m:
                        rangs.add(int(m.group(1)))
            d['dial_presentes'] += len(rangs)
            for i, (_, txt) in enumerate(repliques, 1):
                if i not in rangs:
                    d['dial_manquantes'] += 1
                    d['sec_dial'] += SECONDES(txt)
                    d['dial_trous'].append('%s/line_%02d' % (did, i))
    return d


def releve(filtre=None):
    dossiers = sorted(p.name for p in (RACINE / 'assets' / 'interactive').iterdir()
                      if p.is_dir() and p.name.startswith('module-'))
    if filtre:
        dossiers = [s for s in dossiers if filtre in s]
    return [etat(s) for s in dossiers]


def mn(sec):
    return '%d min' % round(sec / 60) if sec >= 60 else '%d s' % round(sec)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    detail = '--detail' in sys.argv
    tout = releve(args[0] if args else None)

    if '--json' in sys.argv:
        print(json.dumps(tout, ensure_ascii=False, indent=1))
        return 0

    troues = [d for d in tout if d['sons_manquants'] or d['dial_manquantes']]
    sans_releve = [d for d in tout if not d['releve']]

    par_niveau = {}
    for d in troues:
        n = d['niveau'] or 0
        c = par_niveau.setdefault(n, {'mods': 0, 'sons': 0, 'dial': 0, 'sec': 0.0})
        c['mods'] += 1
        c['sons'] += d['sons_manquants']
        c['dial'] += d['dial_manquantes']
        c['sec'] += d['sec_sons'] + d['sec_dial']

    print('%d module(s) sur %d ont de l\'audio manquant.\n' % (len(troues), len(tout)))
    print('  %-9s %6s %10s %10s %9s' % ('niveau', 'mods', 'sons', 'répliques', 'durée'))
    tot = {'mods': 0, 'sons': 0, 'dial': 0, 'sec': 0.0}
    for n in sorted(par_niveau):
        c = par_niveau[n]
        for k in tot:
            tot[k] += c[k]
        print('  niveau %-2s %6d %10d %10d %9s'
              % (n or '?', c['mods'], c['sons'], c['dial'], mn(c['sec'])))
    print('  %-9s %6d %10d %10d %9s'
          % ('TOTAL', tot['mods'], tot['sons'], tot['dial'], mn(tot['sec'])))

    fam = {}
    for d in troues:
        for f, n in d['par_famille'].items():
            fam[f] = fam.get(f, 0) + n
    if fam:
        print('\n  Les sons manquants, par famille :')
        for f, n in sorted(fam.items(), key=lambda x: -x[1]):
            print('    %-22s %6d' % (f, n))
        print('    %-22s %6d' % ('répliques de dialogue', tot['dial']))

    print('\n  Les modules, du plus troué au moins troué :')
    for d in sorted(troues, key=lambda x: -(x['sons_manquants'] + x['dial_manquantes'])):
        etiquette = []
        if d['sons_manquants']:
            etiquette.append('%d/%d sons' % (d['sons_manquants'], d['sons_attendus']))
        if d['dial_manquantes']:
            etiquette.append('%d/%d répliques' % (d['dial_manquantes'], d['dial_attendues']))
        print('    %-30s n%-2s %-28s %s'
              % (d['slug'], d['niveau'] or '?', ' · '.join(etiquette),
                 mn(d['sec_sons'] + d['sec_dial'])))
        if detail and d['par_famille']:
            for f, n in sorted(d['par_famille'].items(), key=lambda x: -x[1]):
                print('        %-24s %5d' % (f, n))

    if sans_releve:
        print('\n  %d module(s) sans relevé de sons — on ne sait pas ce qui y est '
              'attendu :' % len(sans_releve))
        print('    ' + ', '.join(d['slug'] for d in sans_releve))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
