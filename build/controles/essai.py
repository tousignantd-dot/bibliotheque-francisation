#!/usr/bin/env python3
"""Contrôle de la période d'essai d'un centre.

    python3 build/controles/essai.py

Ce que le contrôle vérifie, et qui ne se voit pas à l'écran : la règle
elle-même (deux cours par niveau, tous les ateliers), la **remontée par
l'arbre** (le premier réglage explicite tranche), et le fait que l'entonnoir
`activities_for_group` borne réellement — c'est lui qui sert les quatre
écrans, donc c'est lui qu'il faut prendre en défaut.
"""
import importlib.util
import json
import os
import pathlib
import shutil
import sys
import tempfile

RACINE = pathlib.Path(__file__).resolve().parent.parent.parent


def charger(volume):
    os.environ['STORAGE_DIR'] = str(volume)
    spec = importlib.util.spec_from_file_location('srv_essai_%s' % volume.name,
                                                  RACINE / 'server.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def banc(essai_centre):
    """Un volume jetable : un réseau, un CSS, un centre, un groupe."""
    v = pathlib.Path(tempfile.mkdtemp())
    (v / 'data').mkdir()
    for f in ('activities.json',):
        shutil.copy(RACINE / 'data' / f, v / 'data' / f)
    orgs = [{"id": 1, "type": "reseau", "parentId": None, "nom": "réseau", "actif": True},
            {"id": 2, "type": "css", "parentId": 1, "nom": "CSS", "actif": True},
            {"id": 3, "type": "centre", "parentId": 2, "nom": "Centre d'essai",
             "actif": True}]
    if essai_centre is not None:
        orgs[2]["essai"] = essai_centre
    (v / 'data' / 'organisations.json').write_text(json.dumps(orgs))
    (v / 'data' / 'groups.json').write_text(json.dumps(
        [{"id": 1, "nom": "Niveau 5", "niveau": "Niveau 5", "teacherId": 1, "centreId": 3}]))
    (v / 'data' / 'schedule.json').write_text('[]')
    return v


def controle():
    echecs = []

    def verifier(nom, obtenu, attendu):
        if obtenu != attendu:
            echecs.append('%s : attendu %r, obtenu %r' % (nom, attendu, obtenu))
        print('%-58s %s' % (nom, 'ok' if obtenu == attendu else 'ÉCHEC'))

    # ── 1. Sans essai : le catalogue entier ────────────────────────────
    v = banc(None)
    srv = charger(v)
    tout = srv.activities_for_group(1)
    total = len(json.load(open(RACINE / 'data' / 'activities.json')))
    verifier('centre ordinaire : le catalogue entier', len(tout), total)
    verifier('centre ordinaire : pas en essai', srv.essai_effective(3)[0], False)
    shutil.rmtree(v)

    # ── 2. En essai : deux cours par niveau, tous les ateliers ─────────
    v = banc('oui')
    srv = charger(v)
    offert = srv.activities_for_group(1)
    cours = [a for a in offert if a.get('categorie') == 'cours']
    ateliers = [a for a in offert if a.get('categorie') != 'cours']
    tous = json.load(open(RACINE / 'data' / 'activities.json'))
    ateliers_total = [a for a in tous if a.get('categorie') != 'cours']
    niveaux = {}
    for a in cours:
        niveaux.setdefault(a.get('level'), []).append(srv.numero_de_module(a))
    verifier('en essai : aucun cours au-delà du deuxième',
             sorted({n for v_ in niveaux.values() for n in v_}), [1, 2])
    verifier('en essai : tous les ateliers restent',
             len(ateliers), len(ateliers_total))
    verifier('en essai : huit niveaux servis', len(niveaux), 8)
    verifier('en essai : deux cours par niveau',
             sorted({len(v_) for v_ in niveaux.values()}), [2])

    # ── 3. Un cours sans numéro lisible est fermé ──────────────────────
    verifier('cours sans numéro : fermé',
             srv.ouverte_en_essai({'categorie': 'cours', 'title': 'Sans numéro'}), False)
    verifier('atelier sans numéro : ouvert',
             srv.ouverte_en_essai({'categorie': 'atelier', 'title': 'Sans numéro'}), True)
    shutil.rmtree(v)

    # ── 4. La remontée : le CSS décide pour un centre qui hérite ───────
    v = banc(None)
    orgs = json.loads((v / 'data' / 'organisations.json').read_text())
    orgs[1]['essai'] = 'oui'          # le CSS
    (v / 'data' / 'organisations.json').write_text(json.dumps(orgs))
    srv = charger(v)
    verifier('héritage : le CSS met son centre en essai',
             srv.essai_effective(3)[0], True)
    verifier('héritage : le décideur est nommé',
             srv.essai_effective(3)[1]['nom'], 'CSS')
    shutil.rmtree(v)

    # ── 5. Le centre tranche contre son CSS ────────────────────────────
    v = banc('non')
    orgs = json.loads((v / 'data' / 'organisations.json').read_text())
    orgs[1]['essai'] = 'oui'
    (v / 'data' / 'organisations.json').write_text(json.dumps(orgs))
    srv = charger(v)
    verifier('le premier réglage explicite tranche : le centre gagne',
             srv.essai_effective(3)[0], False)
    shutil.rmtree(v)

    print()
    if echecs:
        print('%d ÉCHEC(S)' % len(echecs))
        for e in echecs:
            print('  ·', e)
        return 1
    print('Tout passe.')
    return 0


if __name__ == '__main__':
    sys.exit(controle())
