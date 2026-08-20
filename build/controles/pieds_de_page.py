#!/usr/bin/env python3
"""Le numéro réellement inscrit dans chaque .pptx livré, comparé au registre.

python-pptx découpe « MODULE 10 » en plusieurs runs XML : recoller les <a:t>
est indispensable, sinon le contrôle échoue toujours, pour la mauvaise raison.
"""
import glob
import pathlib
import re
import sys
import zipfile

ROOT = pathlib.Path.home() / 'Claude/bibliotheque-francisation'
sys.path.insert(0, str(ROOT / 'build/powerpoints'))
from modules import MODULES, ORDRE  # noqa: E402

ecarts = []
for slug in ORDRE:
    attendu = str(MODULES[slug]['numero'])
    vus = set()
    fichiers = glob.glob(str(ROOT / 'assets/powerpoints' / slug / '*.pptx'))
    for f in fichiers:
        z = zipfile.ZipFile(f)
        for n in z.namelist():
            if n.endswith('.xml') and '/slides/slide' in n:
                x = z.read(n).decode('utf-8', 'ignore')
                # Recoller les runs est indispensable — python-pptx découpe
                # « MODULE 10 » en plusieurs <a:t>. Mais les recoller *sans
                # séparateur* invente des numéros : dans module-urgence, le
                # pied « MODULE 2 » précède le titre « 911, 811 ou clinique »
                # et donne « MODULE 2911 ». D'où le \x00 : il ne casse pas un
                # numéro coupé en deux runs, mais il arrête la capture avant
                # le run suivant.
                txt = '\x00'.join(re.findall(r'<a:t>([^<]*)</a:t>', x))
                vus |= set(re.findall(r'MODULE[\s\x00]*(\d+)', txt))
    etat = 'OK ' if vus == {attendu} else '!! '
    if vus != {attendu}:
        ecarts.append((slug, attendu, sorted(vus)))
    print('%s%-24s niveau %s · numéro %-3s · %2d pptx · vus %s'
          % (etat, slug, MODULES[slug].get('niveau', '?'), attendu,
             len(fichiers), sorted(vus) or '—'))

print()
print('%d écart(s)' % len(ecarts))
for e in ecarts:
    print('   ', e)
