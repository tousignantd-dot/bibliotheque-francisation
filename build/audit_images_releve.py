#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le relevé qui ouvre un audit d'images : pour chacune des images générées
des modules, son chemin, le mot qu'elle doit faire deviner, l'énoncé de sa
carte et **le prompt qui l'a produite**.

Le prompt est le point d'appui de tout l'audit : sans lui, on juge une image
contre une devinette. Il se lit dans `build/contenu/<slug>/gen_images.py`, qui
porte `IMAGES = [(nom, dossier, page, prompt)]`. Le script exécute ces fichiers
pour résoudre les concaténations de constantes — sans réseau : `route_images`
est remplacé par un bouchon, et les scripts sautent ce qui existe déjà.

Il fabrique aussi une miniature de 384 px par image. C'est ce qui rend l'audit
abordable : un agent y lit dix fois moins de pixels, pour le même jugement.

    python3 build/audit_images_releve.py build/audits/<nom>

Voir `build/audits/images-2026-08/README.md` pour ce qu'un audit produit
ensuite, et `build/audit_images_page.py` pour la page de tri."""
import ast, json, pathlib, sys, types, traceback

BASE = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation')
RACINE = BASE / 'assets' / 'interactive'
SORTIE = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
MINI = SORTIE / 'mini'
EXT = {'.jpg', '.jpeg', '.png', '.webp'}

contexte = json.loads((BASE / 'build' / '_contexte_images.json').read_text())

def prompts_du_module(chemin):
    """Exécute gen_images.py sans réseau pour récupérer IMAGES tel quel."""
    faux = types.ModuleType('route_images')
    faux.generer_image = lambda *a, **k: None
    sys.modules['route_images'] = faux
    src = chemin.read_text()
    # On coupe tout ce qui suit la garde __main__ pour ne rien déclencher.
    g = {'__name__': 'gen_images_audit', '__file__': str(chemin)}
    try:
        exec(compile(src, str(chemin), 'exec'), g)
    except Exception:
        return {}
    im = g.get('IMAGES')
    if not isinstance(im, (list, tuple)):
        return {}
    out = {}
    for t in im:
        if not isinstance(t, (list, tuple)) or len(t) < 4:
            continue
        nom, dossier, page, prompt = t[0], t[1], t[2], t[3]
        if isinstance(nom, str) and isinstance(prompt, str):
            out[(str(dossier), nom)] = {'page': str(page), 'prompt': prompt}
    return out

travail = []
for dossier_mod in sorted(RACINE.iterdir()):
    if not dossier_mod.is_dir():
        continue
    slug = dossier_mod.name
    gen = BASE / 'build' / 'contenu' / slug / 'gen_images.py'
    pr = prompts_du_module(gen) if gen.exists() else {}
    for sous in ('images', 'vocab'):
        d = dossier_mod / sous
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.suffix.lower() not in EXT:
                continue
            tige = f.stem
            ctx = contexte.get(f'{slug}/{f.name}', {})
            p = pr.get((sous, tige), {})
            travail.append({
                'id': f'{slug}/{sous}/{f.name}',
                'module': slug,
                'dossier': sous,
                'fichier': f.name,
                'mot': tige.replace('-', ' '),
                'role': ctx.get('role', 'vocabulaire' if sous == 'vocab' else 'exercice'),
                'enonce': ctx.get('enonce', ''),
                'consigne': ctx.get('consigne', ''),
                'page': p.get('page', ''),
                'prompt': p.get('prompt', ''),
                'source': str(f.relative_to(BASE)),
            })

(SORTIE / 'travail.json').write_text(json.dumps(travail, ensure_ascii=False, indent=1))
avec_p = sum(1 for t in travail if t['prompt'])
avec_e = sum(1 for t in travail if t['enonce'])
print(f'{len(travail)} images · prompt d\'origine : {avec_p} · énoncé : {avec_e} · '
      f'ni l\'un ni l\'autre : {sum(1 for t in travail if not t["prompt"] and not t["enonce"])}')

# ── miniatures ────────────────────────────────────────────────────────────
from PIL import Image
MINI.mkdir(parents=True, exist_ok=True)
faites = 0
for t in travail:
    dest = MINI / t['id'].replace('/', '__')
    dest = dest.with_suffix('.jpg')
    t['mini'] = str(dest)
    if dest.exists():
        continue
    im = Image.open(BASE / t['source']).convert('RGB')
    h = round(im.height * 384 / im.width)
    im.resize((384, h), Image.LANCZOS).save(dest, 'JPEG', quality=72)
    faites += 1
(SORTIE / 'travail.json').write_text(json.dumps(travail, ensure_ascii=False, indent=1))
print(f'miniatures : {faites} fabriquées, {len(travail)} au total')
