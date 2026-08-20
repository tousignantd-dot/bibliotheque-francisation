#!/usr/bin/env python3
"""Refait une image de mot d'un flash vocabulaire (Nano Banana 2).

Suit la compétence /generate : routage Google AI Studio puis fal.ai, sortie à
plat dans ~/Claude/generations avec son journal .json adjacent, puis mise à
jour du mur. La copie vers le deck est le pas en plus : ici l'image a une
destination dans le dépôt.

Ici on **refait** une image jugée irréaliste : la cible existe déjà, elle est
donc écrasée. L'ancienne reste dans ~/Claude/generations si elle en vient.

  python3 build/vocab_flash_images.py                # toutes celles listées
  python3 build/vocab_flash_images.py le_fromage_en_grains
"""
import io, json, pathlib, sys, time, urllib.request, urllib.error

RACINE = pathlib.Path(__file__).resolve().parent.parent
GEN    = pathlib.Path('/Users/danieltousignant/Claude/generations')
ENV    = pathlib.Path('/Users/danieltousignant/Claude/.env')

def cle(nom):
    if not ENV.exists():
        return ''
    for ligne in ENV.read_text(encoding='utf-8').splitlines():
        ligne = ligne.strip()
        if ligne.startswith(nom + '='):
            return ligne.split('=', 1)[1].strip().strip('"\'')
    return ''

GOOGLE, FAL = cle('GOOGLE_KEY'), cle('FAL_KEY')
if not (GOOGLE or FAL):
    sys.exit('Ni GOOGLE_KEY ni FAL_KEY dans ~/Claude/.env — /generate ne peut pas router.')

STYLE = ("Photographie réaliste, format carré, lumière naturelle douce, faible "
         "profondeur de champ. Palette sobre. Aucun texte, aucune écriture, "
         "aucun logo, aucune marque, aucun filigrane, aucune personne.")

# (deck, slug du mot, prompt)
IMAGES = [
 ('vocab-flash-conso', 'le_fromage_en_grains', STYLE + " Gros plan sur du fromage en "
  "grains cheddar frais du Québec, tel qu'on le vend en sac à l'épicerie : de gros "
  "morceaux blancs crème de la taille d'une bouchée, deux à quatre centimètres, aux "
  "formes molles, bombées et irrégulières, aux bords arrondis et déchiquetés, sans "
  "aucune arête droite. Surfaces fermes et légèrement luisantes. Les morceaux sont "
  "bien distincts les uns des autres, en vrac dans un petit bol de bois clair posé "
  "sur une table de cuisine. Ce ne sont ni des cubes, ni des dés taillés au couteau, "
  "ni des billes, ni des granules, ni de la poudre, ni du fromage râpé."),
]

def par_google(prompt):
    """Route la moins chère quand la clé Google marche ; elle a déjà rendu 403."""
    import base64
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           "gemini-3.1-flash-lite-image:generateContent?key=" + GOOGLE)
    corps = json.dumps({"contents": [{"parts": [{"text": prompt}]}]}).encode()
    req = urllib.request.Request(url, data=corps,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    for part in d["candidates"][0]["content"]["parts"]:
        if "inline_data" in part or "inlineData" in part:
            bloc = part.get("inline_data") or part["inlineData"]
            return base64.b64decode(bloc["data"])
    raise RuntimeError('réponse Google sans image')

def par_fal(prompt):
    corps = json.dumps({"prompt": prompt, "num_images": 1, "aspect_ratio": "1:1",
                        "resolution": "1K", "output_format": "jpeg"}).encode()
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=corps,
        headers={"Authorization": "Key " + FAL, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as r:
        d = json.loads(r.read())
    with urllib.request.urlopen(d["images"][0]["url"], timeout=180) as r:
        return r.read()

def genere(prompt):
    """Rend (données, fournisseur). Une route qui échoue passe la main, en le disant."""
    routes = ([('Google AI Studio', par_google)] if GOOGLE else []) \
           + ([('fal.ai', par_fal)] if FAL else [])
    dernier = None
    for nom, appel in routes:
        try:
            return appel(prompt), nom
        except Exception as e:
            detail = e.read()[:180] if isinstance(e, urllib.error.HTTPError) else e
            print('  … %s écarté : %s' % (nom, detail), flush=True)
            dernier = e
    raise dernier

def a_900(data):
    """Les six autres images du deck font 900 px : la neuve doit s'y ranger."""
    try:
        from PIL import Image
    except ImportError:
        return data
    im = Image.open(io.BytesIO(data)).convert('RGB')
    if im.size != (900, 900):
        im = im.resize((900, 900), Image.LANCZOS)
    tampon = io.BytesIO()
    im.save(tampon, 'JPEG', quality=86, optimize=True)
    return tampon.getvalue()

voulus = set(sys.argv[1:])
GEN.mkdir(parents=True, exist_ok=True)
horodatage = time.strftime('%Y%m%d-%H%M%S')
faits, echecs = [], []

for deck, slug, prompt in IMAGES:
    if voulus and slug not in voulus:
        continue
    cible = RACINE / 'assets/interactive' / deck / 'images' / (slug + '.jpg')
    try:
        brut, fournisseur = genere(prompt)
        data = a_900(brut)
    except urllib.error.HTTPError as e:
        echecs.append('%s : HTTP %s %s' % (slug, e.code, e.read()[:180])); continue
    except Exception as e:
        echecs.append('%s : %s' % (slug, e)); continue

    base = '%s_%s_%s' % (deck, slug, horodatage)
    (GEN / (base + '.jpg')).write_bytes(data)
    (GEN / (base + '.json')).write_text(json.dumps({
        "model": "fal-ai/nano-banana-2",
        "prompt": prompt,
        "refs": [],
        "params": {"num_images": 1, "aspect_ratio": "1:1",
                   "resolution": "1K", "output_format": "jpeg"},
        "provider": fournisseur,
        "cost_estimate_usd": 0.034,
        "created": time.strftime('%Y-%m-%dT%H:%M:%S+00:00', time.gmtime()),
        "projet": "bibliotheque-francisation",
        "module": deck,
        "page": "Je découvre · la carte du mot",
        "destination": "assets/interactive/%s/images/%s.jpg" % (deck, slug),
    }, ensure_ascii=False, indent=2), encoding='utf-8')
    cible.write_bytes(data)
    faits.append(slug)
    print('  ✓ %-24s %6.1f Ko' % (slug, len(data) / 1024), flush=True)

print('\n%d refaites, %d en échec' % (len(faits), len(echecs)))
for e in echecs:
    print('  ✗ ' + e)
print('coût estimé : %.2f $' % (len(faits) * 0.034))

if faits:  # le mur relit les journaux : sans ça la nouvelle image n'y paraît pas
    import subprocess
    subprocess.run(['python3', str(GEN / 'maj-mur.py')], check=False)
