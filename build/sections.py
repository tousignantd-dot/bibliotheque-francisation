#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération de `data/sections.json` · le découpage des modules
=============================================================

    python3 build/sections.py            → écrit data/sections.json
    python3 build/sections.py --verifier → contrôle sans écrire (code 1 si écart)

Ce fichier n'est **jamais écrit à la main**. Chaque module interactif porte
déjà son découpage dans la constante `SECTIONS` de son HTML — « Je découvre ·
Défi 1 · Défi 2 · Défi 3 · Je me lance · Je retiens des mots ». Recopier ces
listes dans le portail les ferait diverger dès la première réécriture d'un
module : le relevé est donc déduit des modules eux-mêmes.

Deux principes :

1. **Le module est la source.** On lit le fichier déclaré dans le champ
   `interactive` de `data/activities.json` — pas le premier HTML du dossier :
   `module-travail` en contient deux, et seul le catalogue sait lequel est
   l'activité.
2. **On lit, on n'exécute pas.** La constante est extraite comme du texte.
   Exécuter le module réclamerait un navigateur, et un module qui plante à
   l'ouverture doit quand même pouvoir être planifié.

Le portail enseignant se sert de ce relevé pour offrir une date par section
(`sectionId` dans `data/schedule.json`) ; le module, lui, s'en sert pour
n'ouvrir à l'élève que les sections dont la date est venue.
"""
import json
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, '..'))

ACTIVITES = os.path.join(RACINE, 'data', 'activities.json')
SORTIE = os.path.join(RACINE, 'data', 'sections.json')

# `const SECTIONS = [ … ];` — la liste s'arrête à un `];` en début de ligne,
# jamais aux crochets fermants qu'on trouve à l'intérieur des objets.
RE_LISTE = re.compile(r'(?:const|var)\s+SECTIONS\s*=\s*\[(.*?)\n\s*\];', re.S)

# Une entrée commence en début de ligne, à deux espaces d'indentation. Les
# `{id:'t2', …}` imbriqués dans un `next:` sont plus loin sur la ligne : c'est
# l'ancrage en début de ligne qui les écarte.
RE_ENTREE = re.compile(r"^ {2}\{id:'([^']+)'", re.M)

RE_TITRE = re.compile(r"title:\s*'((?:[^'\\]|\\.)*)'|title:\s*\"((?:[^\"\\]|\\.)*)\"")
RE_LEAD = re.compile(r"lead:\s*\"((?:[^\"\\]|\\.)*)\"|lead:\s*'((?:[^'\\]|\\.)*)'")


def dejs(texte):
    """Déséchappe une chaîne littérale JavaScript (\\' et \\" surtout)."""
    return re.sub(r'\\(.)', r'\1', texte).strip()


def premier(match):
    """Le groupe non vide d'une alternative « quotes simples | doubles »."""
    if not match:
        return ''
    return dejs(next((g for g in match.groups() if g), ''))


def sections_du_module(chemin):
    """[{id, titre, chapeau}] pour un fichier de module, [] s'il n'en a pas.

    Les activités qui ne sont pas des modules — les ateliers d'une seule
    page — n'ont pas de `SECTIONS` : elles ressortent avec une liste vide et
    restent planifiées d'un bloc, comme aujourd'hui."""
    if not os.path.exists(chemin):
        return []
    src = open(chemin, encoding='utf-8').read()
    liste = RE_LISTE.search(src)
    if not liste:
        return []
    corps = liste.group(1)

    # Découper la liste aux positions des entrées de premier niveau : chaque
    # tranche va d'un `{id:…}` au suivant, donc son `title` est bien le sien.
    debuts = [m.start() for m in RE_ENTREE.finditer(corps)]
    ids = [m.group(1) for m in RE_ENTREE.finditer(corps)]
    bornes = debuts + [len(corps)]

    out = []
    for i, sid in enumerate(ids):
        tranche = corps[bornes[i]:bornes[i + 1]]
        titre = premier(RE_TITRE.search(tranche))
        if not titre:
            continue
        out.append({
            'id': sid,
            'titre': titre,
            'chapeau': premier(RE_LEAD.search(tranche)),
        })
    return out


def relever():
    """{activiteId (str): [sections]} — les modules découpés, eux seuls."""
    activites = json.load(open(ACTIVITES, encoding='utf-8'))
    releve = {}
    for a in activites:
        interactif = (a.get('interactive') or '').strip()
        if not interactif:
            continue
        secs = sections_du_module(os.path.join(RACINE, interactif))
        if secs:
            releve[str(a['id'])] = secs
    return releve


def main(argv):
    verifier = '--verifier' in argv
    releve = relever()

    total = sum(len(s) for s in releve.values())
    print(f'{len(releve)} activité(s) découpée(s), {total} sections.')
    for aid, secs in sorted(releve.items(), key=lambda kv: int(kv[0])):
        print(f'  #{aid:>3} · ' + ' | '.join(s['titre'] for s in secs))

    if verifier:
        ancien = {}
        if os.path.exists(SORTIE):
            ancien = json.load(open(SORTIE, encoding='utf-8'))
        if ancien == releve:
            print('data/sections.json est à jour.')
            return 0
        print('ÉCART : data/sections.json ne correspond plus aux modules.')
        return 1

    with open(SORTIE, 'w', encoding='utf-8') as f:
        json.dump(releve, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'→ {os.path.relpath(SORTIE, RACINE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
