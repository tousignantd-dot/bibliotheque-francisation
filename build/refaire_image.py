#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Refaire UNE image d'un module qui n'a pas de `gen_images.py`.

Neuf modules — les plus anciens — ont vu leurs images produites à la main,
avant que la mécanique des `gen_images.py` existe : `module-banque`,
`module-consultation`, `module-logement`, `module-meteo`, `module-nouvelles`,
`module-travail`, `module-urgence`, et les deux flashs de vocabulaire. Quand
l'audit en condamne une, il n'y a nulle part où corriger le prompt. D'où cet
outil : il refait une image seule, et **inscrit son prompt** dans
`build/audits/prompts_hors_script.json`, pour que le prochain qui la juge
sache contre quoi la juger.

    python3 build/refaire_image.py assets/interactive/module-banque/images/comptoir.jpg \
        "Photographie réaliste, format paysage… Le comptoir d'une succursale…"

L'ancienne version reste dans l'historique git : `git checkout -- <chemin>`.
Passer `--garder-carre` pour un deck de flash, qui affiche en `contain` et ne
recadre pas ; par défaut on sort en 3:2, comme le gabarit des modules.
"""
import argparse
import io
import json
import pathlib
import sys
import urllib.request

BASE = pathlib.Path(__file__).resolve().parent.parent
ENV = pathlib.Path('/Users/danieltousignant/Claude/.env')
REGISTRE = BASE / 'build' / 'audits' / 'prompts_hors_script.json'


def cle(nom):
    if not ENV.exists():
        return ''
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''


def genere(prompt, ratio):
    fal = cle('FAL_KEY')
    if not fal:
        sys.exit('FAL_KEY absente de ~/Claude/.env')
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": ratio,
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + fal, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=240) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=240) as r:
        return r.read()


def main():
    a = argparse.ArgumentParser()
    a.add_argument('cible', help="chemin de l'image, relatif au dépôt")
    a.add_argument('prompt')
    a.add_argument('--garder-carre', action='store_true')
    a.add_argument('--largeur', type=int, default=1000)
    o = a.parse_args()

    from PIL import Image
    ratio = '1:1' if o.garder_carre else '3:2'
    data = genere(o.prompt, ratio)
    im = Image.open(io.BytesIO(data)).convert('RGB')
    h = o.largeur if o.garder_carre else round(o.largeur * 2 / 3)
    im = im.resize((o.largeur, h), Image.LANCZOS)
    cible = BASE / o.cible
    cible.parent.mkdir(parents=True, exist_ok=True)
    im.save(cible, 'JPEG', quality=85, optimize=True)

    REGISTRE.parent.mkdir(parents=True, exist_ok=True)
    reg = json.loads(REGISTRE.read_text()) if REGISTRE.exists() else {}
    reg[o.cible] = {'prompt': o.prompt, 'ratio': ratio, 'largeur': o.largeur}
    REGISTRE.write_text(json.dumps(reg, ensure_ascii=False, indent=1))
    print(f'✓ {o.cible} · {im.size[0]}×{im.size[1]} · '
          f'{cible.stat().st_size / 1024:.1f} Ko · environ 0.03 $')


if __name__ == '__main__':
    main()
