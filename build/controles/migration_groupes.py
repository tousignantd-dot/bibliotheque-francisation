#!/usr/bin/env python3
"""Contrôle de la migration vers le multi-groupes.

    python3 build/controles/migration_groupes.py

`migrate_multi_groupes()` tourne à **chaque démarrage** du serveur. Elle est
censée ne rien faire une fois passée, et son garde décide de tout : quand il
s'ouvre à tort, elle date les 177 activités au premier groupe et remplace la
planification de tous les autres — d'un seul `save_schedule()`.

Ce contrôle prend le garde en défaut sous les trois formes où il a échoué, ou
pouvait échouer. Aucune ne se voit à l'écran : l'enseignante retrouve son
tableau vide et n'a aucune raison de soupçonner un redémarrage.

1. **Installation neuve.** Un groupe créé à la main, aucune date héritée : la
   migration ne doit rien écrire. Sinon elle ouvre les huit niveaux du
   catalogue à un groupe qui n'a rien d'historique.
2. **La forme Postgres.** En production `schedule.json` vit dans la base et
   **pas** sur le volume — il est dans `.gitignore`, donc absent du dépôt que
   recopie `init_storage`, et Postgres ne l'écrit jamais. Un garde qui
   interroge le disque est donc ouvert en permanence : c'est le défaut du
   31 août 2026. Le garde doit interroger la couche de stockage.
3. **Installation réellement historique.** Une activité porte encore une date
   d'avant le multi-groupes : la migration doit faire son travail, exactement
   comme avant. La corriger ne doit pas la désarmer.

Il vérifie aussi que `data/activities.json` — le catalogue **versionné** — ne
porte aucune date d'utilisateur. Ces champs appartiennent au volume (voir
`USER_FIELDS` dans `init_storage`) ; trois d'entre eux traînaient dans le
dépôt, et il a suffi de ces trois-là pour que toute installation neuve se
fasse passer pour une installation historique.
"""
import importlib.util
import json
import os
import pathlib
import shutil
import sys
import tempfile

RACINE = pathlib.Path(__file__).resolve().parent.parent.parent
CHAMPS_UTILISATEUR = ('dateVue', 'datePrevue', 'dateFin')


def charger(volume):
    os.environ['STORAGE_DIR'] = str(volume)
    spec = importlib.util.spec_from_file_location('srv_mig_%s' % volume.name,
                                                  RACINE / 'server.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def banc(dates_heritees=False):
    """Un volume jetable : le catalogue, un groupe, et rien d'autre.

    Pas de `schedule.json` : c'est l'état du volume en production, et c'est
    précisément ce que le garde ne doit plus prendre pour une planification
    vide.
    """
    v = pathlib.Path(tempfile.mkdtemp())
    (v / 'data').mkdir()
    activites = json.loads((RACINE / 'data' / 'activities.json').read_text(encoding='utf-8'))
    if dates_heritees:
        activites[0]['dateVue'] = '2026-05-01'
    (v / 'data' / 'activities.json').write_text(json.dumps(activites, ensure_ascii=False))
    (v / 'data' / 'groups.json').write_text(json.dumps(
        [{"id": 1, "nom": "Niveau 4", "niveau": "Niveau 4", "teacherId": 1},
         {"id": 2, "nom": "Niveau 4 — groupe 2", "niveau": "Niveau 4", "teacherId": 1}]))
    (v / 'data' / 'students.json').write_text('[]')
    return v


def controle():
    echecs = []

    def verifier(nom, obtenu, attendu):
        if obtenu != attendu:
            echecs.append('%s : attendu %r, obtenu %r' % (nom, attendu, obtenu))
        print('%-58s %s' % (nom, 'ok' if obtenu == attendu else 'ÉCHEC'))

    # ── 0. Le catalogue versionné ne porte aucune date d'utilisateur ───
    catalogue = json.loads((RACINE / 'data' / 'activities.json').read_text(encoding='utf-8'))
    residu = [a['id'] for a in catalogue
              if any(a.get(c) for c in CHAMPS_UTILISATEUR)]
    verifier('dépôt : aucune date d’utilisateur dans le catalogue', residu, [])

    # ── 1. Installation neuve : la migration ne doit rien écrire ───────
    v = banc()
    srv = charger(v)
    srv.migrate_multi_groupes()
    verifier('installation neuve : aucune planification écrite',
             len(srv.load_schedule()), 0)
    shutil.rmtree(v)

    # ── 2. Forme Postgres : le garde interroge la couche, pas le disque ─
    #
    # On reproduit le découplage exact de la production — une planification
    # réelle dans la couche de stockage, aucun fichier sur le volume.
    v = banc(dates_heritees=True)          # le pire cas : elle *aurait* migré
    srv = charger(v)
    couche = [
        {"groupId": 1, "activityId": 12, "datePrevue": "2026-09-02",
         "dateVue": "", "dateFin": ""},
        {"groupId": 2, "activityId": 15, "datePrevue": "2026-09-03",
         "dateVue": "", "dateFin": ""},
    ]
    srv.load_schedule = lambda: list(couche)
    srv.save_schedule = lambda entrees: (couche.clear(), couche.extend(entrees))
    if srv.SCHEDULE_FILE.exists():
        srv.SCHEDULE_FILE.unlink()
    srv.migrate_multi_groupes()
    verifier('forme Postgres : la planification n’est pas écrasée',
             len(couche), 2)
    verifier('forme Postgres : le groupe 2 garde la sienne',
             sum(1 for e in couche if e['groupId'] == 2), 1)
    shutil.rmtree(v)

    # ── 3. Installation historique : la migration fait son travail ─────
    v = banc(dates_heritees=True)
    srv = charger(v)
    srv.migrate_multi_groupes()
    plan = srv.load_schedule()
    verifier('installation historique : tout le catalogue est daté',
             len(plan), len(catalogue))
    verifier('installation historique : daté au premier groupe',
             sorted({e['groupId'] for e in plan}), [1])
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
