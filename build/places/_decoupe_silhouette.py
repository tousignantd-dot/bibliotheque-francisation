# -*- coding: utf-8 -*-
"""Les pièces du personnage, découpées dans la silhouette elle-même.

L'idée est de l'enseignant : au lieu d'une icône générique de chandail, la
pièce à poser EST la portion de silhouette qu'elle habille. Posée dans sa
case, elle retombe au pixel près sur le corps, et la couleur habille
exactement la bonne surface.

Le piège : on ne peut pas découper d'abord et chercher l'intérieur ensuite.
Le remplissage part des bords de l'image ; sur un rectangle pris dans le
milieu du corps, il entrerait par les côtés coupés et l'intérieur serait
déclaré « dehors ». On calcule donc l'intérieur sur la silhouette ENTIÈRE,
puis on découpe le masque déjà calculé.
"""
import collections, pathlib
from PIL import Image
from scenes import SCENES

SRC = (pathlib.Path.home()/"Claude/bibliotheque-francisation/assets/interactive"
       /"n2-dessine-1-personnage/img/personnage.jpg")
OUT = pathlib.Path("places/n2-place-1-personnage")
SEUIL = 150

im = Image.open(SRC).convert("L"); W, H = im.size; px = im.load()

# ── l'intérieur du corps, sur l'image entière ──
vu = bytearray(W*H); f = collections.deque()
def pousse(x, y):
    if px[x, y] > SEUIL and not vu[y*W+x]: vu[y*W+x] = 1; f.append((x, y))
for x in range(W): pousse(x, 0); pousse(x, H-1)
for y in range(H): pousse(0, y); pousse(W-1, y)
while f:
    x, y = f.popleft()
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < W and 0 <= ny < H: pousse(nx, ny)

masque = Image.new("RGBA", (W, H), (255,255,255,0)); mp = masque.load()
dedans = 0
for y in range(H):
    for x in range(W):
        if px[x, y] > SEUIL and not vu[y*W+x]: mp[x, y] = (255,255,255,255); dedans += 1
print("  intérieur du corps : %.1f %% de l'image" % (100*dedans/(W*H)))

trait = Image.new("RGBA", (W, H), (0,0,0,0))
trait.putalpha(im.point(lambda v: 255 - v))

# ── une pièce par case ──
Z = {z[0]: z for z in SCENES["n2-place-1-personnage"]["zones"]}
(OUT/"pieces").mkdir(parents=True, exist_ok=True)
for zid, (_, lib, x1, y1, x2, y2) in Z.items():
    box = (int(x1*W), int(y1*H), int(x2*W), int(y2*H))
    m = masque.crop(box); t = trait.crop(box)
    part = sum(1 for p in m.getdata() if p[3]) / (m.width*m.height)
    m.save(OUT/"pieces"/("masque-%s.png" % zid))
    t.save(OUT/"pieces"/("trait-%s.png" % zid))
    drapeau = "" if part > 0.10 else "   ⚠ presque vide, case mal posée ?"
    print("  %-8s %-16s %3dx%-3d  corps : %4.1f %%%s"
          % (zid, lib, m.width, m.height, 100*part, drapeau))
