#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération des fiches élèves imprimables
=========================================

    python3 build_fiches.py module-probleme          → les fiches du module
    python3 build_fiches.py module-probleme b2 c3    → deux fiches seulement
    python3 build_fiches.py --tous                   → tous les modules

Les fiches sortent dans `assets/documents/`, toutes ensemble, sous le nom
`<slug>-<code>-<titre>.html` — le slug les distingue d'un module à l'autre.
Le sommaire d'un module est `<slug>-fiches-eleves.html` : c'est lui qu'on
donne au premier cours, et lui qui sert de `studentDoc` à l'activité.

Elles sont produites à partir des MÊMES fichiers `decks/<slug>/*.py` que les
présentations. Le contenu est donc écrit une seule fois : corriger une
coquille dans `decks/module-probleme/b2.py` corrige à la fois le PowerPoint
et la fiche.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

# Les fichiers de contenu font « from theme import Deck ». On charge d'abord
# le vrai `theme` — `fiche` y lit les jetons de couleur — puis on met `fiche`
# à sa place dans la table des modules. Les decks importent alors le moteur
# HTML sans qu'une seule ligne de contenu ait à changer.
import theme            # noqa: F401,E402  (chargé pour ses jetons)
import fiche            # noqa: E402
sys.modules['theme'] = fiche

import modules          # noqa: E402
import build            # noqa: E402  (pour `charger()`, l'import d'un deck)

SORTIE = os.path.abspath(os.path.join(ICI, '..', '..', 'assets', 'documents'))


def _en_lettres(n):
    """« Seize fiches », pas « 16 fiches » : le sommaire est une page de texte
    qu'on lit, pas un tableau de bord."""
    mots = {1: 'Une', 2: 'Deux', 3: 'Trois', 4: 'Quatre', 5: 'Cinq',
            6: 'Six', 7: 'Sept', 8: 'Huit', 9: 'Neuf', 10: 'Dix',
            11: 'Onze', 12: 'Douze', 13: 'Treize', 14: 'Quatorze',
            15: 'Quinze', 16: 'Seize', 17: 'Dix-sept', 18: 'Dix-huit'}
    return mots.get(n, str(n))


def sommaire(slug, m, faits):
    """Une page de garde qui rassemble les fiches du module. C'est elle qu'on
    donne à l'élève au premier cours, et elle qui sert de `studentDoc`."""
    lignes, bloc_courant = '', None
    for code, titre, duree, nom in faits:
        b = code[0]
        if b != bloc_courant:
            bloc_courant = b
            lignes += (f'<tr class="grp"><td colspan="3">Bloc {b} · '
                       f'{fiche.esc(m["blocs"].get(b, ""))}</td></tr>')
        lignes += (f'<tr><td class="c">{fiche.esc(code)}</td>'
                   f'<td><a href="{fiche.esc(nom)}">{fiche.esc(titre)}</a></td>'
                   f'<td class="d">{fiche.esc(duree)}</td></tr>')
    css = fiche.CSS
    n, titre_mod, niveau = m['numero'], m['titre'], m['niveau']
    html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Module {n} · Les {_en_lettres(len(faits)).lower()} fiches élèves</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{css}
table.som{{width:100%;border-collapse:collapse}}
table.som td{{padding:7px 8px 7px 0;border-top:1px solid var(--line);font-weight:600}}
table.som tr.grp td{{border-top:0;padding-top:16px;font-size:9.5pt;font-weight:800;
  text-transform:uppercase;letter-spacing:.12em;color:var(--ink)}}
table.som td.c{{width:16mm;font-weight:800;color:var(--ink)}}
table.som td.d{{width:24mm;text-align:right;color:var(--muted)}}
table.som a{{color:var(--ink);text-decoration:none}}
table.som a:hover{{text-decoration:underline}}
</style></head><body>
<header class="hdr"><div class="hdr-l">
<div class="eyebrow">Module {n} · Français niveau {niveau}</div>
<h1>{fiche.esc(titre_mod)}</h1></div>
<div class="hdr-r"><span>Nom<span class="nomline nomline--nom"></span></span></div></header>
<p class="chapeau">{_en_lettres(len(faits))} fiches, une par séance. Gardez-les dans
l'ordre : chacune reprend ce que la précédente a installé.</p>
<section class="bloc card"><table class="som"><tbody>{lignes}</tbody></table></section>
<footer><span>Module {n} · {fiche.esc(titre_mod)}</span><span>Sommaire</span></footer>
</body></html>
"""
    chemin = os.path.join(SORTIE, f'{slug}-fiches-eleves.html')
    with open(chemin, 'w', encoding='utf-8') as f:
        f.write(html)
    return chemin


def verifier_noir_et_blanc(chemin):
    """Refuse toute couleur dans une fiche. Les fiches sont photocopiées en
    noir et blanc : une couleur qui s'y glisse ne se voit pas ici, mais elle
    devient un gris indistinct sur le papier de l'enseignant — et l'écart
    qu'elle portait disparaît sans prévenir.

    Est considérée comme neutre toute valeur dont les trois composantes ne
    s'écartent pas de plus de 8 sur 255. Les neutres chauds du système
    (#17181A, #F0F0EE) passent ; le vert d'accent et les rouges de
    rétroaction, non."""
    import re as _re
    fautifs = []
    for hexa in set(_re.findall(r'#([0-9A-Fa-f]{6})\b', open(chemin, encoding='utf-8').read())):
        r, v, b = (int(hexa[i:i + 2], 16) for i in (0, 2, 4))
        if max(r, v, b) - min(r, v, b) > 8:
            fautifs.append('#' + hexa.upper())
    return sorted(fautifs)


def produire(slug, codes=None):
    m = modules.choisir(slug)
    cibles = [c.lower() for c in (codes or m['seances'])]
    os.makedirs(SORTIE, exist_ok=True)

    print(f"Module {m['numero']} · {m['titre']}  ({slug})")
    total, faits = 0, []
    for code in cibles:
        mod = build.charger(slug, code)
        chemin, nblocs = mod.build(SORTIE)
        total += nblocs
        ko = os.path.getsize(chemin) // 1024
        print(f'  {code.upper():3s}  {nblocs:2d} blocs  {ko:3d} Ko  '
              f'{os.path.basename(chemin)}')
        faits.append((code.upper(), _titre(mod), _duree(mod),
                      os.path.basename(chemin)))

    produits = [os.path.join(SORTIE, f[3]) for f in faits]
    if cibles == m['seances']:
        som = sommaire(slug, m, faits)
        produits.append(som)
        print(f'  SOM       {os.path.basename(som)}')

    couleurs = {os.path.basename(p): verifier_noir_et_blanc(p) for p in produits}
    couleurs = {k: v for k, v in couleurs.items() if v}
    if couleurs:
        for nom, cs in couleurs.items():
            print(f'COULEUR  {nom} — {", ".join(cs)}')
        print(f'\n{len(couleurs)} fiche(s) contiennent de la couleur : à corriger.')
        sys.exit(1)
    print(f'  → {len(cibles)} fiche(s) · {total} blocs · noir et blanc vérifié\n')
    return total


def main(argv):
    tous = '--tous' in argv
    argv = [a for a in argv if not a.startswith('--')]

    if tous:
        cibles_mod, codes = modules.ORDRE, None
    else:
        if not argv:
            raise SystemExit(
                'Usage : python3 build_fiches.py <module> [codes…]\n'
                '        python3 build_fiches.py --tous\n'
                'Modules : ' + ', '.join(modules.ORDRE))
        cibles_mod, codes = [argv[0]], (argv[1:] or None)

    total = 0
    for slug in cibles_mod:
        if not os.path.isdir(build.dossier_decks(slug)):
            print(f'{slug} · pas encore de decks — ignoré\n')
            continue
        total += produire(slug, codes)
    print(f'OK · {total} blocs au total')
    print(f'Sortie : {SORTIE}')


def _titre(mod):
    return _meta(mod)['titre']


def _duree(mod):
    return _meta(mod)['duree']


_CACHE = {}


def _meta(mod):
    """Relit `titre=` et `duree=` dans le source du deck, sans le réexécuter."""
    cle = mod.__file__
    if cle not in _CACHE:
        import inspect
        import re as _re
        src = inspect.getsource(mod)
        t = _re.search(r"titre=(['\"])(.+?)\1", src, _re.S)
        d = _re.search(r"duree=(['\"])(.+?)\1", src, _re.S)
        _CACHE[cle] = {'titre': t.group(2) if t else mod.__name__,
                       'duree': d.group(2) if d else ''}
    return _CACHE[cle]


if __name__ == '__main__':
    main(sys.argv[1:])
