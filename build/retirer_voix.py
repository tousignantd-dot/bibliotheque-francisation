#!/usr/bin/env python3
"""Effacer les extraits d'un rôle de voix, pour que les générateurs les refassent.

    python3 build/retirer_voix.py                 # simulation, rien n'est effacé
    python3 build/retirer_voix.py --effacer       # pour de vrai
    python3 build/retirer_voix.py --role narrateur --effacer

Le 23 août 2026, la voix « enseignante » a changé d'identifiant. Or les
générateurs **sautent ce qui est déjà sur le disque** — c'est ce qui permet de
reprendre après une coupure sans repayer. Conséquence : sans effacer, la
nouvelle voix ne serait jamais produite, et le module garderait l'ancienne.
Effacer tout, à l'inverse, ferait repayer les huit mille extraits des trois
autres voix, qui n'ont pas bougé.

Ce script efface **exactement** ce que le rôle nommé a produit, en relisant
les générateurs — la seule source qui sache l'attribution :

· `sons/` — les mots isolés et les mini-leçons, produits par `VOIX_MOTS` ;
· `line_NN_<personnage>.mp3` — les répliques, dont `VOIX_PERSO` donne le rôle.

Le nom de fichier d'une réplique vient du nom du personnage mis en minuscules,
espaces en tirets bas. On refait ici la même transformation plutôt que de la
deviner : « MME RIOUX » donne `mme_rioux`, et un module qui nommerait ses
fichiers autrement ne verrait rien effacé — ce qui est le bon échec, puisqu'il
vaut mieux un extrait de trop que le module d'une classe amputé.
"""
import argparse
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RACINE / 'assets' / 'interactive'


def slug_perso(nom):
    """« MME RIOUX » → `mme_rioux`, comme le font les générateurs."""
    return nom.lower().replace(' ', '_')


def module_du_generateur(src):
    """Le dossier d'assets que ce générateur alimente."""
    m = re.search(r'assets/interactive/([\w-]+)', src)
    return m.group(1) if m else None


def analyser(role):
    """Rend [(module, mots_isoles, [personnages])] pour le rôle demandé."""
    trouve = []
    for gen in sorted(RACINE.glob('generer_audio_*.py')):
        src = gen.read_text(encoding='utf-8', errors='replace')
        module = module_du_generateur(src)
        if not module:
            continue
        mots = bool(re.search(
            r'VOIX_MOTS\s*=\s*VOIX\[\s*["\']%s["\']\s*\]' % role, src))
        bloc = re.search(r'VOIX_PERSO\s*=\s*\{(.*?)^\}', src, re.S | re.M)
        persos = []
        if bloc:
            persos = [n for n, v in re.findall(
                r'["\']([^"\']+)["\']\s*:\s*["\'](\w+)["\']', bloc.group(1))
                if v == role]
        if mots or persos:
            trouve.append((gen.name, module, mots, persos))
    return trouve


def main():
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument('--role', default='enseignante',
                   help="le rôle de voix à effacer (défaut : enseignante)")
    a.add_argument('--effacer', action='store_true',
                   help="effacer pour de vrai ; sans lui, on ne fait que compter")
    opt = a.parse_args()

    total, manquants = 0, []
    for gen, module, mots, persos in analyser(opt.role):
        dossier = ASSETS / module
        if not dossier.exists():
            manquants.append(module)
            continue
        cibles = []
        if mots:
            cibles += sorted((dossier / 'sons').glob('*.mp3')) \
                if (dossier / 'sons').exists() else []
        for p in persos:
            motif = 'line_*_%s.mp3' % slug_perso(p)
            cibles += sorted(dossier.rglob(motif))
        if not cibles:
            continue
        total += len(cibles)
        print('%-34s %4d extraits%s' % (module, len(cibles),
              '  (' + ', '.join(persos) + ')' if persos else ''))
        if opt.effacer:
            for c in cibles:
                c.unlink()

    if manquants:
        print('\nSans dossier d\'assets, laissés tels quels : %s'
              % ', '.join(sorted(set(manquants))))
    print('\n%d extrait(s) %s pour le rôle « %s ».'
          % (total, 'effacés' if opt.effacer else 'à effacer', opt.role))
    if not opt.effacer and total:
        print('Relancer avec --effacer, puis `python3 build/audio_tous.py`.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
