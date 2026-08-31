#!/usr/bin/env python3
"""Écrit l'index des documents de travail de `docs/`.

    python3 build/releve_documents.py

Ces dix-huit fichiers sont des documents **sur le projet** : ils vont donc à
la banque de présentations. Mais dix-huit fiches pour dix-huit `.md` noieraient
la banque sous du texte qu'on ne lit pas en réunion. Une fiche, un index, et
chaque document reste à sa place — c'est le compromis retenu au ménage du
31 août 2026.

Titre et chapeau sont **lus dans les fichiers** : un index recopié à la main
serait faux au premier document réécrit.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOCS = RACINE / 'docs'
SORTIE = RACINE / 'assets' / 'presentations' / 'documents-de-travail.html'

FAMILLES = [
    ('Le protocole entre sessions',
     "Plusieurs conversations travaillent dans ce dépôt en même temps. Ces fichiers disent "
     "qui tient quoi, et comment reprendre après une interruption.",
     ['qui-fait-quoi', 'deux-agents-en-parallele', 'REPRISE-23-aout', 'etat-21-aout-soir']),
    ('Les plans de production',
     "Quoi produire, dans quel ordre, avec quels numéros. Ce sont eux qui ont survécu aux "
     "sessions et qui ont permis de reprendre un chantier sans le rejouer.",
     ['vagues-suivantes', 'chantier-tous-niveaux', 'chantier-modules-neufs',
      'consignes-a-coller', 'plan-banques-niveaux-2-8', 'plan-exercices-niveau-1',
      'schemas-banque-n1']),
    ('Les journaux de module',
     "Un par module produit : le scénario écrit avant le contenu, puis le journal de ce qui "
     "a été fait. Le plan est écrit d'abord pour que le scénario survive à la session.",
     ['plan-module-n5-logement', 'plan-module-n5-degat', 'plan-module-n5-emmenagement',
      'plan-module-n5-saisons', 'plan-module-n3-horaire']),
    ("Les contrats d'écriture et les mesures",
     "Ce qui fixe une façon d'écrire, et ce qui la vérifie.",
     ['brief-point-express', 'verification-originalite']),
]


def lire(nom):
    """(titre, chapeau, octets) d'un document, lus dans le fichier."""
    f = DOCS / (nom + '.md')
    if not f.exists():
        return None
    lignes = [l.rstrip() for l in f.read_text(errors='replace').split('\n')]
    titre = next((l.lstrip('# ').strip() for l in lignes if l.startswith('# ')), nom)
    chapeau, dedans = [], False
    for l in lignes:
        if l.startswith('# '):
            dedans = True
            continue
        if not dedans:
            continue
        if not l.strip():
            if chapeau:
                break
            continue
        if l.startswith(('#', '|', '- ', '* ', '```')):
            break
        chapeau.append(l.strip())
    texte = ' '.join(chapeau)
    texte = re.sub(r'`([^`]+)`', r'<code>\1</code>', texte)
    texte = re.sub(r'\*\*([^*]+)\*\*', r'<b>\1</b>', texte)
    return titre, texte, f.stat().st_size


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def page():
    src = (RACINE / 'assets' / 'presentations' / 'audio-manquant.html').read_text()
    style = src[src.index('<style>'):src.index('</style>') + 8]
    connus = {n for _, _, noms in FAMILLES for n in noms}
    tous = sorted(p.stem for p in DOCS.glob('*.md'))
    oublies = [n for n in tous if n not in connus]

    blocs, total = [], 0
    for titre, chapeau, noms in FAMILLES + ([('Non classés',
            "Trouvés dans <code>docs/</code> et non rangés par ce script : à classer, ou à "
            "retirer.", oublies)] if oublies else []):
        lignes = []
        for n in noms:
            d = lire(n)
            if not d:
                continue
            t, c, o = d
            total += 1
            lignes.append(
                '<article class="doc-l"><div><h3>%s</h3><p>%s</p>'
                '<div class="doc-m"><code>docs/%s.md</code><span>%.0f ko</span></div></div>'
                '<a class="doc-b" href="../../docs/%s.md" target="_blank" rel="noopener">Lire</a>'
                '</article>' % (esc(t), c or '<i>sans chapeau</i>', n, o / 1000, n))
        if lignes:
            blocs.append('<div class="bloc"><h2>%s</h2><p>%s</p><div class="docs">%s</div></div>'
                         % (esc(titre), chapeau, ''.join(lignes)))

    return '''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Les documents de travail</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600&family=Nunito:ital,wght@0,400;0,600;0,700;0,800&display=swap">
''' + style + '''
<style>
.docs{display:grid;gap:10px;margin:16px 0 0}
.doc-l{background:var(--card);border:1px solid var(--line);border-radius:11px;
  padding:15px 17px;display:flex;gap:14px;align-items:flex-start}
.doc-l h3{font-family:Newsreader,Georgia,serif;font-size:19px;font-weight:600;
  color:var(--ink);margin:0 0 5px}
.doc-l p{font-size:14.5px;margin:0}
.doc-m{display:flex;gap:12px;flex-wrap:wrap;margin:9px 0 0;font-size:12px;color:var(--muted)}
.doc-m code{font-family:var(--mono);font-size:12px}
.doc-b{margin-left:auto;flex:0 0 auto;align-self:center;font-size:13px;font-weight:800;
  color:var(--ok);border:1px solid var(--line-fort);border-radius:99px;padding:6px 14px;
  text-decoration:none;white-space:nowrap}
.bloc{margin:50px 0 0}
.bloc>p{margin:8px 0 0}
.note{background:var(--part-bg);border-left:3px solid var(--part);border-radius:0 8px 8px 0;
  padding:14px 16px;margin:20px 0 0;font-size:15px}
</style>
</head>
<body>
<div class="doc">
  <p class="eyebrow">Index · 31 août 2026</p>
  <h1>Les documents de travail</h1>
  <p class="chapeau">Les <strong>''' + str(total) + ''' fichiers de <code>docs/</code></strong> :
  plans de production, journaux de module, protocole entre sessions. Ce sont des documents
  <i>sur le projet</i>, donc ils appartiennent à la banque — mais dix-huit fiches noieraient
  la banque sous du texte qu'on ne lit pas en réunion. Une fiche, un index, et chaque
  document reste à sa place.</p>
  <div class="note">Ce sont des <b>documents de travail</b>, pas des présentations : écrits
  pour qu'une session puisse reprendre où une autre s'est arrêtée. On les ouvre quand on
  cherche <i>pourquoi</i> quelque chose a été fait ainsi, pas pour les montrer.</div>
''' + ''.join(blocs) + '''
  <div class="bloc">
    <h2>Où ça se fait</h2>
    <p>Cette page est <b>générée</b> par <b>python3 build/releve_documents.py</b> : les titres
    et les chapeaux sont lus dans les fichiers eux-mêmes. Un index recopié à la main serait
    faux au premier document réécrit — c'est exactement le défaut que le ménage du 31 août a
    trouvé dans les compteurs de la banque.</p>
  </div>
</div>
</body>
</html>
'''


def main():
    SORTIE.write_text(page())
    print('%d documents indexés → %s'
          % (len(list(DOCS.glob('*.md'))), SORTIE.relative_to(RACINE)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
