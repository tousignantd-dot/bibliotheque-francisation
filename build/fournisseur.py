#!/usr/bin/env python3
"""Reconnaître d'où vient un MP3 — ElevenLabs ou Azure — et protéger le premier.

    python3 build/fournisseur.py            # l'inventaire du dépôt

Le 29 août 2026, l'utilisateur a retiré son autorisation de remplacer l'audio
ElevenLabs. Ces fichiers ne sont **pas** régénérables : la maison a fermé la
porte au réglage de vitesse, et surtout ce sont d'autres comédiens. Les
écraser change la voix des personnages, ce qui ne se répare pas par un simple
retirage.

La reconnaissance se lit sur la **fréquence d'échantillonnage** : Azure produit
du 24 kHz (`audio-24khz-160kbitrate-mono-mp3`), ElevenLabs rendait du 44,1 kHz.
C'est un signe sûr et gratuit — pas de registre à tenir à jour, pas de date de
production à deviner.

Les drivers de régénération appellent `protege()` avant d'écrire. Ne jamais le
contourner sans un accord explicite, écrit, pour ces fichiers-là.
"""
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
INTER = RACINE / 'assets' / 'interactive'


def frequence(chemin):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                        'stream=sample_rate', '-of', 'csv=p=0', str(chemin)],
                       capture_output=True, text=True)
    try:
        return int(r.stdout.strip().splitlines()[0])
    except (ValueError, IndexError):
        return 0


def est_elevenlabs(chemin):
    """Vrai si ce fichier vient d'ElevenLabs — donc intouchable."""
    return frequence(chemin) == 44100


def module_elevenlabs(slug):
    """Vrai si le module porte encore de l'audio ElevenLabs.

    On regarde le fichier le plus ancien : c'est celui qui n'a pas été refait,
    donc celui qui dit d'où vient le module. Un module partiellement migré
    compte comme ElevenLabs — il reste des voix à protéger dedans.
    """
    fichiers = sorted((INTER / slug).glob('*/line_*.mp3'),
                      key=lambda p: p.stat().st_mtime)
    return bool(fichiers) and est_elevenlabs(fichiers[0])


def protege(slugs):
    """Sépare les modules en (régénérables, protégés)."""
    ok, bloques = [], []
    for s in slugs:
        (bloques if module_elevenlabs(s) else ok).append(s)
    return ok, bloques


def main():
    mods = sorted({f.parts[-3] for f in INTER.glob('*/*/line_*.mp3')})
    ok, bloques = protege(mods)
    print('%d modules · %d chez Azure · %d encore chez ElevenLabs (protégés)'
          % (len(mods), len(ok), len(bloques)))
    for b in bloques:
        n = len(list((INTER / b).glob('*/line_*.mp3')))
        print('   protégé : %-28s %3d répliques' % (b, n))


if __name__ == '__main__':
    main()
