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
MOTIFS_FATALS = ('invalid_api_key', 'authentication_error', 'quota_exceeded',
                 'unauthorized', 'insufficient_credits')


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

    # Les générateurs lisent la clé dans l'environnement, mais l'utilisateur la
    # dépose dans ~/Claude/.env, où vivent déjà celles des images. On la charge
    # ici plutôt que de lui demander de l'exporter à la main chaque fois.
    if not os.environ.get('ELEVENLABS_API_KEY', '').strip():
        env = pathlib.Path.home() / 'Claude' / '.env'
        if env.exists():
            for ligne in env.read_text(encoding='utf-8').splitlines():
                if ligne.strip().startswith('ELEVENLABS_API_KEY') and '=' in ligne:
                    os.environ['ELEVENLABS_API_KEY'] = (
                        ligne.split('=', 1)[1].strip().strip('"').strip("'"))
    if not os.environ.get('ELEVENLABS_API_KEY', '').strip():
        print('✗ ELEVENLABS_API_KEY introuvable, ni dans l’environnement '
              'ni dans ~/Claude/.env.')
        return 2

    # Une seule requête avant de lancer quoi que ce soit. Un jeton invalide ou
    # un quota à zéro se voit ici, pour le prix d'un mot — au lieu de deux
    # cents échecs par générateur pendant cinq minutes, comme le 22 août.
    #
    # On sonde la SYNTHÈSE, pas l'abonnement : une clé restreinte au
    # text-to-speech ne peut pas lire /v1/user/subscription et renvoie 401
    # alors qu'elle parle très bien. Sonder autre chose que ce qu'on va faire,
    # c'est se faire refuser pour la mauvaise raison.
    sonde = subprocess.run(
        [sys.executable, '-c',
         'import os, sys, json, urllib.request, urllib.error\n'
         'sys.path.insert(0, %r)\n'
         'from voix import charge_utile, url\n'
         'voix = "21m00Tcm4TlvDq8ikWAM"\n'
         'req = urllib.request.Request(url(voix),\n'
         '    data=json.dumps(charge_utile("oui", voix)).encode(),\n'
         '    headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"],\n'
         '             "Content-Type": "application/json"})\n'
         'try:\n'
         '    n = len(urllib.request.urlopen(req, timeout=60).read())\n'
         '    print("OK — un mot synthétisé, %%.1f Ko" %% (n/1024))\n'
         'except urllib.error.HTTPError as e:\n'
         '    print("HTTP %%s %%s" %% (e.code, e.read()[:160].decode("utf-8","replace")))\n'
         '    sys.exit(1)\n' % str(RACINE / 'build')],
        capture_output=True, text=True, env=os.environ)
    print('Sonde de la synthèse : ' + (sonde.stdout or sonde.stderr).strip())
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

        fatal = any(m in sortie for m in MOTIFS_FATALS)
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
