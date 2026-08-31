#!/usr/bin/env python3
"""Monte la capsule vidéo d'un module à partir de ses propres images et voix.

    python3 build/video_module.py

**Rien n'est synthétisé.** Les répliques sont les MP3 déjà produits pour le
dialogue du module : la voix de la capsule est donc exactement celle que
l'élève entendra deux écrans plus loin, et la capsule ne coûte pas une
seconde de synthèse. C'est aussi ce qui la garde vraie — une narration écrite
pour la vidéo aurait fini par diverger du dialogue.

**Sans sous-titres, décidé par l'utilisateur.** Deux conséquences assumées :
la capsule ne rouvre pas la transcription qu'un enseignant vient de fermer
(elle n'écrit rien), et elle n'est pas accessible à un élève sourd — la
transcription du dialogue, elle, reste à sa place habituelle.

Sortie : `assets/interactive/<slug>/video/<slug>.mp4` et son affiche `.jpg`.
"""
import pathlib
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SLUG = 'module-n5-logement'
BASE = RACINE / 'assets' / 'interactive' / SLUG
SORTIE = BASE / 'video'

# Un plan par réplique, plus l'ouverture et la fermeture. L'image est choisie
# pour **montrer ce dont la voix parle** — la boîte aux lettres pendant qu'on
# dit « j'ai reçu un papier », le formulaire pendant qu'on le nomme.
PLANS = [
    ('images/boite-aux-lettres.jpg',   None,                        2.4),
    ('images/boite-aux-lettres.jpg',   'prep/line_01_nadege.mp3',   None),
    ('vocab/avis-modification.jpg',    'prep/line_02_samuel.mp3',   None),
    ('vocab/bail.jpg',                 'prep/line_03_nadege.mp3',   None),
    ('vocab/loyer.jpg',                'prep/line_04_samuel.mp3',   None),
    ('images/panneau-a-louer.jpg',     None,                        2.6),
]
SILENCE = 0.45          # un souffle entre deux répliques
L, H = 1264, 712        # 16:9 pris dans l'image d'origine (1264 × 848)


def duree(chemin):
    out = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
         '-of', 'csv=p=0', str(chemin)], capture_output=True, text=True, check=True)
    return float(out.stdout.strip())


def zoom(i):
    """Un lent rapprochement, alterné pour que deux plans voisins ne bougent
    pas pareil. Sans mouvement, une suite d'images fixes se lit comme un
    diaporama en panne plutôt que comme une capsule."""
    return ('zoompan=z=\'min(zoom+0.0006,1.10)\':x=\'iw/2-(iw/zoom/2)\':'
            "y='ih/2-(ih/zoom/2)'" if i % 2 == 0 else
            'zoompan=z=\'if(lte(zoom,1.0),1.10,max(1.001,zoom-0.0006))\':'
            "x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'")


def main():
    SORTIE.mkdir(exist_ok=True)
    travail = SORTIE / '.travail'
    travail.mkdir(exist_ok=True)

    morceaux, sons, total = [], [], 0.0
    for i, (image, son, fixe) in enumerate(PLANS):
        d = (duree(BASE / son) + SILENCE) if son else fixe
        total += d
        clip = travail / ('plan_%02d.mp4' % i)
        subprocess.run([
            'ffmpeg', '-y', '-loglevel', 'error', '-loop', '1', '-i', str(BASE / image),
            '-t', '%.3f' % d, '-r', '25',
            '-vf', ('scale=%d:-1,crop=%d:%d,%s:d=%d:s=%dx%d:fps=25,format=yuv420p'
                    % (L, L, H, zoom(i), int(d * 25), L, H)),
            '-c:v', 'libx264', '-preset', 'medium', '-crf', '26', str(clip)],
            check=True)
        morceaux.append(clip)
        sons.append((son, d))

    liste = travail / 'plans.txt'
    liste.write_text(''.join("file '%s'\n" % c.name for c in morceaux))
    muet = travail / 'muet.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat',
                    '-safe', '0', '-i', str(liste), '-c', 'copy', str(muet)], check=True)

    # La bande sonore : chaque réplique posée à l'instant de son plan.
    entrees, filtres, t = [], [], 0.0
    n = 0
    for son, d in sons:
        if son:
            entrees += ['-i', str(BASE / son)]
            filtres.append('[%d:a]adelay=%d|%d[a%d]' % (n, int(t * 1000), int(t * 1000), n))
            n += 1
        t += d
    piste = travail / 'bande.m4a'
    subprocess.run(
        ['ffmpeg', '-y', '-loglevel', 'error'] + entrees +
        ['-filter_complex', ';'.join(filtres) + ';' +
         ''.join('[a%d]' % i for i in range(n)) +
         # `apad` **dans** le graphe, pas en `-af` : ffmpeg refuse de mêler un
         # filtre simple à un filtre complexe sur le même flux. Sans ce
         # remplissage la bande s'arrête à la dernière réplique (27,4 s au lieu
         # de 30,4) et le `-shortest` du montage final tranche le plan de
         # fermeture avec elle. Le défaut ne se voit pas au montage : il se
         # voit en regardant la fin, et c'est ainsi qu'il a été trouvé.
         'amix=inputs=%d:normalize=0,apad[out]' % n,
         '-map', '[out]', '-t', '%.3f' % total,
         '-c:a', 'aac', '-b:a', '96k', str(piste)],
        check=True)

    film = SORTIE / ('%s.mp4' % SLUG)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', str(muet), '-i', str(piste),
                    '-c:v', 'copy', '-c:a', 'copy', '-shortest',
                    '-movflags', '+faststart', str(film)], check=True)

    # L'affiche : la première image, cadrée comme la vidéo. Elle tient la place
    # tant que personne n'a cliqué — rien ne se télécharge avant.
    affiche = SORTIE / ('%s.jpg' % SLUG)
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error',
                    '-i', str(BASE / PLANS[0][0]),
                    '-vf', 'scale=%d:-1,crop=%d:%d' % (L, L, H),
                    '-q:v', '4', str(affiche)], check=True)

    for f in travail.iterdir():
        f.unlink()
    travail.rmdir()
    print('%s — %.1f s, %.1f Mo' % (film.relative_to(RACINE), duree(film),
                                    film.stat().st_size / 1e6))
    print('%s — %.0f ko' % (affiche.relative_to(RACINE), affiche.stat().st_size / 1e3))
    return 0


if __name__ == '__main__':
    sys.exit(main())
