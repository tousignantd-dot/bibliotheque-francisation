#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération des fiches élèves imprimables du module 9
=====================================================

    python3 build_fiches.py            → les 16 fiches
    python3 build_fiches.py b2 c3      → deux fiches seulement

Les fiches sortent dans `assets/documents/`, à côté des fiches des autres
modules, sous le nom `module-probleme-<code>-<titre>.html`.

Elles sont produites à partir des MÊMES fichiers `decks/*.py` que les
présentations. Le contenu est donc écrit une seule fois : corriger une
coquille dans `decks/b2.py` corrige à la fois le PowerPoint et la fiche.
"""
import importlib
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [ICI, os.path.join(ICI, 'decks')]

# Les fichiers de contenu font « from theme import Deck ». On charge d'abord
# le vrai `theme` — `fiche` y lit les jetons de couleur — puis on met `fiche`
# à sa place dans la table des modules. Les decks importent alors le moteur
# HTML sans qu'une seule ligne de contenu ait à changer.
import theme            # noqa: F401  (chargé pour ses jetons)
import fiche
sys.modules['theme'] = fiche

from build import SEANCES  # noqa: E402  (l'ordre d'enseignement, une seule fois)

SORTIE = os.path.abspath(os.path.join(ICI, '..', '..', 'assets', 'documents'))


BLOCS_LABEL = {'A': 'Je me prépare', 'B': 'Tâche 1 · Un problème dans le logement',
               'C': "Tâche 2 · Des problèmes dans l'immeuble",
               'D': 'Tâche 3 · Une situation inacceptable',
               'E': 'Je mets en application'}


def sommaire(faits):
    """Une page de garde qui rassemble les seize fiches. C'est elle qu'on
    donne à l'élève au premier cours, et elle qui peut servir de `studentDoc`
    pour l'activité 45."""
    lignes, bloc_courant = '', None
    for code, titre, duree, nom in faits:
        b = code[0]
        if b != bloc_courant:
            bloc_courant = b
            lignes += (f'<tr class="grp"><td colspan="3">Bloc {b} · '
                       f'{fiche.esc(BLOCS_LABEL[b])}</td></tr>')
        lignes += (f'<tr><td class="c">{fiche.esc(code)}</td>'
                   f'<td><a href="{fiche.esc(nom)}">{fiche.esc(titre)}</a></td>'
                   f'<td class="d">{fiche.esc(duree)}</td></tr>')
    css = fiche.CSS
    html = f"""<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Module 9 · Les seize fiches élèves</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{css}
table.som{{width:100%;border-collapse:collapse}}
table.som td{{padding:7px 8px 7px 0;border-top:1px solid var(--line);font-weight:600}}
table.som tr.grp td{{border-top:0;padding-top:16px;font-size:9.5pt;font-weight:800;
  text-transform:uppercase;letter-spacing:.12em;color:var(--accent-ink)}}
table.som td.c{{width:16mm;font-weight:800;color:var(--ink)}}
table.som td.d{{width:24mm;text-align:right;color:var(--muted)}}
table.som a{{color:var(--ink);text-decoration:none}}
table.som a:hover{{text-decoration:underline}}
</style></head><body>
<header class="hdr"><div class="hdr-l">
<div class="eyebrow">Module 9 · Français niveau 4</div>
<h1>Pouvez-vous régler le problème ?</h1></div>
<div class="hdr-r"><span>Nom<span class="nomline nomline--nom"></span></span></div></header>
<p class="chapeau">Seize fiches, une par séance. Gardez-les dans l'ordre : chacune
reprend ce que la précédente a installé.</p>
<section class="bloc card"><table class="som"><tbody>{lignes}</tbody></table></section>
<footer><span>Module 9 · Pouvez-vous régler le problème ?</span><span>Sommaire</span></footer>
</body></html>
"""
    chemin = os.path.join(SORTIE, 'module-probleme-fiches-eleves.html')
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


def main(argv):
    cibles = [a.lower() for a in argv if not a.startswith('--')] or SEANCES
    os.makedirs(SORTIE, exist_ok=True)
    total, faits = 0, []
    for code in cibles:
        mod = importlib.import_module(code)
        chemin, nblocs = mod.build(SORTIE)
        total += nblocs
        ko = os.path.getsize(chemin) // 1024
        print(f'  {code.upper():3s}  {nblocs:2d} blocs  {ko:3d} Ko  '
              f'{os.path.basename(chemin)}')
        faits.append((code.upper(), _titre(mod), _duree(mod),
                      os.path.basename(chemin)))
    produits = [os.path.join(SORTIE, f[3]) for f in faits]
    if cibles == SEANCES:
        som = sommaire(faits)
        produits.append(som)
        print(f'  SOM       {os.path.basename(som)}')

    couleurs = {os.path.basename(p): verifier_noir_et_blanc(p) for p in produits}
    couleurs = {k: v for k, v in couleurs.items() if v}
    if couleurs:
        for nom, cs in couleurs.items():
            print(f'COULEUR  {nom} — {", ".join(cs)}')
        print(f'\n{len(couleurs)} fiche(s) contiennent de la couleur : à corriger.')
        sys.exit(1)

    print(f'\nOK · {len(cibles)} fiche(s) · {total} blocs')
    print('Contrôle noir et blanc : aucune couleur.')
    print(f'Sortie : {SORTIE}')


def _titre(mod):
    return _meta(mod)['titre']


def _duree(mod):
    return _meta(mod)['duree']


_CACHE = {}


def _meta(mod):
    """Relit `titre=` et `duree=` dans le source du deck, sans le réexécuter."""
    if mod.__name__ not in _CACHE:
        import inspect
        import re as _re
        src = inspect.getsource(mod)
        t = _re.search(r"titre=(['\"])(.+?)\1", src, _re.S)
        d = _re.search(r"duree=(['\"])(.+?)\1", src, _re.S)
        _CACHE[mod.__name__] = {'titre': t.group(2) if t else mod.__name__,
                                'duree': d.group(2) if d else ''}
    return _CACHE[mod.__name__]


if __name__ == '__main__':
    main(sys.argv[1:])
