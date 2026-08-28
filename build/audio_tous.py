#!/usr/bin/env python3
"""Lancer les générateurs audio, tous, sans brûler le quota pour rien.

    python3 build/audio_tous.py --essai      # les douze mots difficiles, d'abord
    python3 build/audio_tous.py --compter    # ce qui reste à produire, sans rien payer
    python3 build/audio_tous.py              # tout, un générateur à la fois
    python3 build/audio_tous.py module-n6    # seulement ceux dont le nom contient ça

Quatre-vingt-quatre générateurs, plus de huit mille extraits. Les lancer à la
main l'un après l'autre, c'est quatre-vingt-quatre occasions d'en oublier un.

**Le coupe-circuit est la raison d'être de ce script.** Un générateur ne
s'arrête pas quand l'API refuse : il enchaîne ses deux cents extraits et
signale deux cents échecs. Avec un jeton invalide ou un quota épuisé en pleine
nuit, ce sont des milliers d'appels inutiles — et si le quota se vide au
milieu, on ne le sait qu'au matin. Ici, deux générateurs consécutifs qui
échouent à l'authentification ou au quota arrêtent tout, immédiatement.

**Rien n'est repayé.** Chaque générateur saute les extraits déjà sur le
disque : relancer après une coupure reprend où l'on en était.

**Éprouver avant de payer.** `--essai` produit douze mots réputés difficiles,
avec et sans contexte français, à écouter côte à côte — c'est la vérification
du travail fait sur `build/voix.py` : ElevenLabs lit-il encore « pain » et
« dix » à l'anglaise quand le mot arrive nu ? Douze mots coûtent une
bagatelle ; huit mille sur une hypothèse non vérifiée, non.
"""
import os
import pathlib
import re
import subprocess
import sys
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent
# Comparés en minuscules : Azure rend « HTTP Error 401: Unauthorized », avec
# des majuscules qu'un motif en minuscules ne rattraperait pas — et un
# coupe-circuit qui ne coupe pas est pire que pas de coupe-circuit.
MOTIFS_FATALS = ('invalid_api_key', 'authentication_error', 'quota_exceeded',
                 'unauthorized', 'insufficient_credits',
                 'error 401', 'error 403', 'too many requests',
                 'azure_speech_key absente')


def generateurs(filtre=None):
    g = sorted(RACINE.glob('generer_audio_*.py'))
    if filtre:
        g = [f for f in g if filtre in f.name]
    return g


def a_produire(chemin):
    """Ce que ce générateur annonce, sans rien appeler : son relevé de sons."""
    nom = chemin.stem.replace('generer_audio_', '')
    releve = RACINE / ('sons_%s.json' % nom)
    if not releve.exists():
        return None
    import json
    try:
        d = json.loads(releve.read_text(encoding='utf-8'))
        return len(d) if isinstance(d, dict) else None
    except Exception:
        return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    filtre = args[0] if args else None

    if '--essai' in sys.argv:
        return subprocess.run([sys.executable, str(RACINE / 'build' / 'voix.py'),
                               '--essai']).returncode

    liste = generateurs(filtre)
    if not liste:
        print('aucun générateur ne correspond à %r' % filtre)
        return 2

    if '--compter' in sys.argv:
        total = 0
        for f in liste:
            n = a_produire(f)
            total += n or 0
            print('  %-52s %s' % (f.name, ('%d sons relevés' % n) if n else '—'))
        print('\n%d générateur(s) · %d son(s) relevés (hors répliques de dialogue)'
              % (len(liste), total))
        return 0

    # Les générateurs lisent la clé dans ~/Claude/.env par `build/azure_voix.py`.
    # On vérifie seulement qu'elle y est, avant de sonder.
    if not os.environ.get('AZURE_SPEECH_KEY', '').strip():
        env = pathlib.Path.home() / 'Claude' / '.env'
        if env.exists():
            for ligne in env.read_text(encoding='utf-8').splitlines():
                for nom in ('AZURE_SPEECH_KEY', 'AZURE_SPEECH_REGION'):
                    if ligne.strip().startswith(nom) and '=' in ligne:
                        os.environ.setdefault(
                            nom, ligne.split('=', 1)[1].strip().strip('"').strip("'"))
    if not os.environ.get('AZURE_SPEECH_KEY', '').strip():
        print('✗ AZURE_SPEECH_KEY introuvable, ni dans l’environnement '
              'ni dans ~/Claude/.env.')
        return 2

    # Une seule requête avant de lancer quoi que ce soit. Une clé invalide ou
    # une région fausse se voit ici, pour le prix d'un mot — au lieu de deux
    # cents échecs par générateur pendant cinq minutes, comme le 22 août.
    #
    # On sonde la SYNTHÈSE, pas l'abonnement : sonder autre chose que ce qu'on
    # va faire, c'est se faire refuser pour la mauvaise raison. La sonde suit
    # le fournisseur — elle interrogeait ElevenLabs, qui n'est plus appelé par
    # aucun générateur de module depuis la bascule du 26 août 2026.
    sonde = subprocess.run(
        [sys.executable, '-c',
         'import sys, pathlib, tempfile\n'
         'sys.path.insert(0, %r)\n'
         'from azure_voix import parle\n'
         'f = pathlib.Path(tempfile.mkdtemp()) / "sonde.mp3"\n'
         'parle("oui", "enseignante", f)\n'
         'print("OK — un mot synthétisé, %%.1f Ko" %% (f.stat().st_size/1024))\n'
         % str(RACINE / 'build')],
        capture_output=True, text=True, env=os.environ)
    print('Sonde de la synthèse : ' + (sonde.stdout or sonde.stderr).strip()[-200:])
    if sonde.returncode:
        print('✗ L’API refuse déjà un seul mot. Rien n’est lancé.')
        return 2

    print('%d générateur(s) à lancer.\n' % len(liste))
    faits, echoues, consecutifs = [], [], 0
    debut = time.time()
    for i, f in enumerate(liste, 1):
        print('── %2d/%d · %s' % (i, len(liste), f.name), flush=True)
        r = subprocess.run([sys.executable, str(f)], cwd=RACINE,
                           capture_output=True, text=True)
        sortie = (r.stdout or '') + (r.stderr or '')
        derniere = [l for l in sortie.strip().split('\n') if l.strip()][-1:] or ['']
        print('   ' + derniere[0][:120], flush=True)

        fatal = any(m in sortie.lower() for m in MOTIFS_FATALS)
        if r.returncode == 0 and not fatal:
            faits.append(f.name); consecutifs = 0
            continue
        echoues.append(f.name)
        if fatal:
            consecutifs += 1
            if consecutifs >= 2:
                print('\n✗ ARRÊT. Deux générateurs de suite refusés par l’API — '
                      'jeton invalide ou quota épuisé.\n'
                      '  Rien n’est perdu : les extraits déjà produits restent, '
                      'et relancer reprendra où l’on en est.')
                break
        else:
            consecutifs = 0

    minutes = (time.time() - debut) / 60
    print('\n%d générateur(s) terminé(s), %d en échec, en %.0f min'
          % (len(faits), len(echoues), minutes))
    for e in echoues:
        print('   ✗ ' + e)
    print('\nPensez à `python3 ~/Claude/generations/maj-mur.py` pour le mur.')
    return 1 if echoues else 0


if __name__ == '__main__':
    sys.exit(main())
