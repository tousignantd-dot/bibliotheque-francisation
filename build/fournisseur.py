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


# Les fréquences d'un en-tête de trame MPEG audio, par version puis par index.
_TAUX = {3: (44100, 48000, 32000), 2: (22050, 24000, 16000),
         0: (11025, 12000, 8000)}


def frequence(chemin):
    """La fréquence d'échantillonnage, lue dans l'en-tête du fichier.

    On ne passe **pas** par ffprobe : un sous-processus par fichier met plus de
    deux minutes sur les 5 962 répliques du cours, et l'inventaire est demandé
    à chaque régénération. L'en-tête d'une trame MPEG porte l'information dans
    deux bits ; il suffit de sauter l'étiquette ID3 et de trouver la synchro.
    `ffprobe` reste le recours si l'en-tête est illisible.
    """
    try:
        with open(chemin, 'rb') as f:
            tete = f.read(4096)
    except OSError:
        return 0
    i = 0
    if tete[:3] == b'ID3':                      # étiquette de longueur variable
        taille = 0
        for o in tete[6:10]:
            taille = (taille << 7) | (o & 0x7F)  # entier « synchsafe »
        i = 10 + taille
        if i >= len(tete):
            try:
                with open(chemin, 'rb') as f:
                    f.seek(i)
                    tete, i = f.read(64), 0
            except OSError:
                return 0
    while i + 3 < len(tete):
        if tete[i] == 0xFF and (tete[i + 1] & 0xE0) == 0xE0:
            version = (tete[i + 1] >> 3) & 0x03
            index = (tete[i + 2] >> 2) & 0x03
            if version != 1 and index != 3:      # 1 = réservé, 3 = invalide
                return _TAUX[version][index]
        i += 1
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
    """Vrai si le module porte **au moins un** fichier ElevenLabs."""
    return any(est_elevenlabs(f) for f in (INTER / slug).glob('*/line_*.mp3'))


def protege(chemins):
    """Sépare une liste de fichiers en (régénérables, protégés).

    La protection se décide **fichier par fichier**, et non par module : les
    modules sont mixtes. `module-n5-degat` en est l'exemple — les répliques de
    Kim sont déjà chez Azure, donc réglables, pendant que celles de ses
    partenaires viennent d'ElevenLabs et ne doivent pas bouger. Protéger le
    module entier bloquait Kim pour rien ; protéger le fichier laisse corriger
    ce qui est corrigible sans remplacer un seul enregistrement d'origine.
    """
    ok, bloques = [], []
    for c in chemins:
        (bloques if est_elevenlabs(c) else ok).append(c)
    return ok, bloques


def repliques_du_module(slug):
    """Les répliques d'un module, séparées : (régénérables, protégées).

    Rend des étiquettes « bloc/fichier.mp3 », la forme qu'attend `--only`.
    """
    fichiers = sorted((INTER / slug).glob('*/line_*.mp3'))
    ok, bloques = protege(fichiers)
    eti = lambda f: '%s/%s' % (f.parent.name, f.name)
    return [eti(f) for f in ok], [eti(f) for f in bloques]


def main():
    mods = sorted({f.parts[-3] for f in INTER.glob('*/*/line_*.mp3')})
    tot_ok = tot_bl = 0
    mixtes = []
    for m in mods:
        ok, bl = repliques_du_module(m)
        tot_ok += len(ok)
        tot_bl += len(bl)
        if ok and bl:
            mixtes.append((m, len(ok), len(bl)))
        elif bl:
            print('   tout protégé : %-26s %3d répliques' % (m, len(bl)))
    print('\n%d répliques · %d régénérables · %d protégées (ElevenLabs)'
          % (tot_ok + tot_bl, tot_ok, tot_bl))
    if mixtes:
        print('\nmodules mixtes — les deux fournisseurs cohabitent :')
        for m, a, b in mixtes:
            print('   %-28s %3d Azure · %3d protégées' % (m, a, b))


if __name__ == '__main__':
    main()
