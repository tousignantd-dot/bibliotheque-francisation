# -*- coding: utf-8 -*-
"""Fabrique les quatre autres « Place ce que j'entends » (niveau 2)."""
import collections, json, pathlib, shutil, sys
from PIL import Image
sys.path.insert(0, str(pathlib.Path.home()/"Claude/bibliotheque-francisation/build"))
from azure_voix import parle
from scenes import SCENES, BANQUES
from couleurs import COULEURS
import gabarit

BASE = pathlib.Path.home()/"Claude/bibliotheque-francisation/assets/interactive"
SEUIL = 150

def cadre(g, marge=0.03):
    bb = g.point(lambda v: 255 if v < 200 else 0).getbbox()
    if not bb: return None
    w,h = g.size; mx,my = int(w*marge), int(h*marge)
    return (max(0,bb[0]-mx), max(0,bb[1]-my), min(w,bb[2]+mx), min(h,bb[3]+my))

def masque_et_trait(chemin):
    """Le masque (alpha = l'intérieur) et le trait seul, recadrés pareil."""
    im = Image.open(chemin).convert("L"); w,h = im.size; px = im.load()
    vu = bytearray(w*h); f = collections.deque()
    def pousse(x,y):
        if px[x,y] > SEUIL and not vu[y*w+x]: vu[y*w+x]=1; f.append((x,y))
    for x in range(w): pousse(x,0); pousse(x,h-1)
    for y in range(h): pousse(0,y); pousse(w-1,y)
    while f:
        x,y = f.popleft()
        for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx,ny = x+dx,y+dy
            if 0<=nx<w and 0<=ny<h: pousse(nx,ny)
    m = Image.new("RGBA",(w,h),(255,255,255,0)); mp=m.load(); dedans=0
    for y in range(h):
        for x in range(w):
            if px[x,y] > SEUIL and not vu[y*w+x]: mp[x,y]=(255,255,255,255); dedans+=1
    t = Image.new("RGBA",(w,h),(0,0,0,0)); t.putalpha(im.point(lambda v:255-v))
    bb = cadre(im)
    if bb: m, t = m.crop(bb), t.crop(bb)
    return m, t, dedans/(w*h)

for slug, S in SCENES.items():
    print("\n══", slug)
    SRC = BASE/S["source"]
    OUT = pathlib.Path("places")/slug
    for d in ("masques","traits","audio","img","reveal"): (OUT/d).mkdir(parents=True, exist_ok=True)
    shutil.copy(SRC/S["base"],   OUT/S["base"])
    shutil.copy(SRC/S["reveal"], OUT/S["reveal"])

    # ── images : masque + trait, recadrés ──
    fin = []
    for mot, sl, genre in BANQUES[slug]:
        # Les « piece-… » sont découpées dans la scène elle-même par
        # `pieces_corps.py` : elles ne viennent pas du lexique.
        if sl.startswith("piece-"): continue
        m, t, part = masque_et_trait(SRC/"lexique"/(sl+".jpg"))
        m.save(OUT/"masques"/(sl+".png")); t.save(OUT/"traits"/(sl+".png"))
        if not (0.02 < part < 0.80): fin.append("%s (%.1f %%)" % (sl, 100*part))
    print("   images :", len(BANQUES[slug]), "· à l'œil :", fin or "rien à signaler")

    # ── audio : on reprend, on ne refait que ce qui manque ──
    repris = 0
    for f in (SRC/"audio").glob("couleur-*.mp3"):
        shutil.copy(f, OUT/"audio"/f.name); repris += 1
    for mot, sl, genre in BANQUES[slug]:
        src = SRC/"audio"/("mot-%s.mp3" % sl)
        if src.exists(): shutil.copy(src, OUT/"audio"/src.name); repris += 1
    neufs = 0
    for mot, sl, genre in BANQUES[slug]:
        d = OUT/"audio"/("mot-%s.mp3" % sl)
        if not d.exists(): parle(mot, "hd_feminin", d, palier="lent"); neufs += 1
    for c in COULEURS:
        d = OUT/"audio"/("couleur-%s.mp3" % c[0])
        if not d.exists(): parle(c[0], "hd_feminin", d, palier="lent"); neufs += 1
    for i, p in enumerate(S["phrases"], 1):
        d = OUT/"audio"/("desc-%02d.mp3" % i)
        if not d.exists(): parle(p, "hd_feminin", d, palier="lent"); neufs += 1
    if not (OUT/"audio/description-lent.mp3").exists():
        parle(" ".join(S["phrases"]), "hd_feminin", OUT/"audio/description-lent.mp3", palier="lent")
        parle(" ".join(S["phrases"]), "hd_feminin", OUT/"audio/description-normal.mp3")
        neufs += 2
    for f in OUT.rglob("*.ssml.xml"): f.unlink()
    print("   audio  : %d repris · %d fabriqués" % (repris, neufs))

    # ── la page ──
    D = {
     "titre": S["titre"],
     "zones": [{"id":z[0],"lib":z[1],"x1":z[2],"y1":z[3],"x2":z[4],"y2":z[5]} for z in S["zones"]],
     "couleurs": [{"nom":c[0],"hex":c[1],"f":c[2],"mp":c[3],"fp":c[4],
                   "audio":"audio/couleur-%s.mp3"%c[0]} for c in COULEURS],
     "banque": [{"mot":m,"slug":sl,"genre":g,
                 "masque": ("pieces/masque-%s.png" % sl[6:]) if sl.startswith("piece-")
                           else "masques/%s.png"%sl,
                 "trait":  ("pieces/trait-%s.png" % sl[6:]) if sl.startswith("piece-")
                           else "traits/%s.png"%sl,
                 "audio":"audio/mot-%s.mp3"%sl}
                for m,sl,g in BANQUES[slug]],
     "scene": [{"obj":o,"zone":z,"coul":c} for o,z,c in S["scene"]],
     "phrases": [{"t":p,"audio":"audio/desc-%02d.mp3"%(i+1)} for i,p in enumerate(S["phrases"])],
     "lent":"audio/description-lent.mp3", "normal":"audio/description-normal.mp3",
     "base":S["base"], "reveal":S["reveal"],
     "ajuste": S.get("ajuste","fixe"),
    }
    manquants=[]
    for e in D["couleurs"]+D["banque"]+D["phrases"]:
        for k in ("audio","masque","trait"):
            if k in e and not (OUT/e[k]).exists(): manquants.append(e[k])
    for k in ("lent","normal","base","reveal"):
        if not (OUT/D[k]).exists(): manquants.append(D[k])
    assert not manquants, (slug, "médias absents", manquants[:5])

    page = (gabarit.HTML
            .replace("__TITRE__", S["titre"])
            .replace("__N__", str(len(S["scene"])))
            .replace("Une table avec une nappe et une chaise", S["alt"])
            .replace("/*DONNEES*/", json.dumps(D, ensure_ascii=False))
            .replace("__SCRIPT__", gabarit.SCRIPT
                     .replace('slug:"n2-place-4-table"', 'slug:"%s"' % slug)
                     .replace('titre:"Place ce que j\'entends — La table"',
                              'titre:%s' % json.dumps(S["titre"], ensure_ascii=False))))
    (OUT/"activite.html").write_text(page, encoding="utf-8")
    print("   page   :", len(page)//1024, "Ko · charset:", page.count("charset"))
