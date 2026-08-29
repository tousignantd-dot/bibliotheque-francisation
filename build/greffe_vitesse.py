#!/usr/bin/env python3
"""Un bouton d'en-tête qui ralentit toutes les voix du module.

    python3 build/greffe_vitesse.py
    python3 build/greffe_vitesse.py --retirer

Le débit des MP3 est fixé à la production : `voix_lente.py` ralentit la voix
enseignante à 0,85 avec `atempo`, une fois pour toutes, et les voix de
dialogue sortent à leur débit d'origine. C'est un compromis figé — trop lent
pour l'élève de mars, trop rapide pour celui de septembre, et personne ne peut
rien y faire pendant l'écoute.

Cette greffe rend le débit réglable *à la lecture*, sans toucher aux fichiers
et sans un octet de synthèse en plus : `playbackRate` sur l'élément `Audio`,
avec `preservesPitch` pour que la voix ne descende pas dans les graves. Trois
crans — normal et lent — dans un bouton de l'en-tête, à côté de
« Réinitialiser ». Le choix est gardé dans `localStorage` et vaut pour tous
les modules : l'élève qui a besoin de lent en a besoin partout.

Les six points de lecture sont touchés ensemble — les répliques de dialogue,
les pastilles de mots, la voix du jeu de rôle, et les trois replis en synthèse
vocale du navigateur (là, c'est `u.rate` qui porte le réglage). Un seul de ces
points laissé de côté et l'élève entend le module changer de vitesse tout seul.

La greffe est idempotente : elle se repose sans dommage. Elle est posée sur le
gabarit comme sur les modules déjà produits, pour ne pas attendre le prochain
build.
"""

import argparse
import glob
import io
import sys

MODULES = "assets/interactive/module-*/module-*-activite-interactive.html"
GABARIT = "build/gabarit/module.html"

DEBUT = "/* VITESSE-VOIX:début — greffé par build/greffe_vitesse.py */"
FIN = "/* VITESSE-VOIX:fin */"

# ── 1. Le style du bouton ────────────────────────────────────────────────
CSS_ANCRE = "#btn-reset:hover{background:rgba(255,255,255,.28)}"
CSS = CSS_ANCRE + """
/* VITESSE-VOIX:début — greffé par build/greffe_vitesse.py */
#btn-vitesse{background:var(--surface-card);color:var(--text-strong);border:1px solid var(--border);border-radius:999px;padding:10px 18px;font-family:'Nunito',sans-serif;font-size:15px;font-weight:800;cursor:pointer;white-space:nowrap;transition:background .15s}
#btn-vitesse:hover{background:var(--paper-100)}
#btn-vitesse[data-cran="1"],#btn-vitesse[data-cran="2"]{background:var(--hdr-accent-soft,var(--accent-soft));border-color:var(--hdr-accent,var(--accent-ink));color:var(--hdr-accent,var(--accent-ink))}
/* VITESSE-VOIX:fin */"""

# ── 2. Le bouton lui-même, avant « Réinitialiser » ───────────────────────
HTML_ANCRE = '    <button id="btn-reset"'
HTML = """    <!-- VITESSE-VOIX:début — greffé par build/greffe_vitesse.py -->
    <button id="btn-vitesse" data-cran="0" data-info="Ralentit toutes les voix du module — les dialogues, les mots et le jeu de rôle. Deux crans : normal et lent. Votre choix est gardé d'un module à l'autre.">Débit normal</button>
    <!-- VITESSE-VOIX:fin -->
""" + HTML_ANCRE

# ── 3. Le réglage, et son bouton ─────────────────────────────────────────
JS_ANCRE = "function playAudioQueue(urls, idx, btn, dialId, allowFallback){"
JS = """/* VITESSE-VOIX:début — greffé par build/greffe_vitesse.py */
/* Le cran « très lent » (0,65) a été retiré le 29 août 2026 : à ce facteur,
   l'étirement s'entend plus qu'il n'aide, et le résultat est franchement
   mauvais. Deux crans suffisent — normal et lent.

   Le débit des MP3 est figé à la production ; celui de la lecture ne l'est
   pas. `playbackRate` étire le son sans le régénérer — et `preservesPitch`
   empêche la voix de descendre dans les graves en ralentissant, ce qui la
   rendrait plus difficile à comprendre, pas plus facile. Le choix suit
   l'élève d'un module à l'autre : celui qui a besoin de lent en a besoin
   partout. */
const VIT_CRANS = [
  {v:1,    lbl:'Débit normal'},
  {v:0.8,  lbl:'Débit lent'},
];
let vitCran = 0;
try{ vitCran = Math.min(1, Math.max(0, parseInt(localStorage.getItem('saaf-vitesse'),10) || 0)); }catch(e){}
const vitFacteur = ()=> VIT_CRANS[vitCran].v;
/* Le facteur d'un `Audio`, posé à la création — et reposé sur celui qui joue
   déjà, pour que le réglage s'entende tout de suite plutôt qu'au prochain
   extrait. */
function vitAudio(a){
  if(!a) return a;
  try{ a.preservesPitch = a.mozPreservesPitch = a.webkitPreservesPitch = true; }catch(e){}
  try{ a.playbackRate = vitFacteur(); }catch(e){}
  return a;
}
/* Les replis en synthèse vocale ont leur propre échelle de débit : le facteur
   s'y multiplie au lieu de s'y substituer, sinon le repli parlerait plus vite
   que le MP3 qu'il remplace. */
const vitTaux = base => Math.max(0.1, base * vitFacteur());
function vitAppliquer(){
  const b = document.getElementById('btn-vitesse');
  if(b){ b.textContent = VIT_CRANS[vitCran].lbl; b.setAttribute('data-cran', String(vitCran)); }
  if(typeof dlgAudio !== 'undefined' && dlgAudio) vitAudio(dlgAudio);
  if(typeof jrAudio !== 'undefined' && jrAudio) vitAudio(jrAudio);
}
document.addEventListener('DOMContentLoaded', ()=>{
  const b = document.getElementById('btn-vitesse');
  if(!b) return;
  b.addEventListener('click', ()=>{
    vitCran = (vitCran + 1) % VIT_CRANS.length;
    try{ localStorage.setItem('saaf-vitesse', String(vitCran)); }catch(e){}
    vitAppliquer();
  });
  vitAppliquer();
});
/* VITESSE-VOIX:fin */
""" + JS_ANCRE

# ── 4. Les six points de lecture ─────────────────────────────────────────
# (avant, après). Les trois derniers n'existent pas dans les neuf modules les
# plus anciens : leur absence n'est pas une erreur.
POINTS = [
    # les répliques du dialogue
    ("dlgAudio=new Audio(urls[idx]);",
     "dlgAudio=vitAudio(new Audio(urls[idx]));"),
    # les pastilles de mots
    ("const a=new Audio(url);\n  a.onended=reset;",
     "const a=vitAudio(new Audio(url));\n  a.onended=reset;"),
    # le repli en synthèse vocale du dialogue
    ("u.lang='fr-CA'; u.rate=0.95; u.pitch=",
     "u.lang='fr-CA'; u.rate=vitTaux(0.95); u.pitch="),
    # le repli en synthèse vocale d'un mot
    ("u.lang='fr-CA'; u.rate=0.9;\n",
     "u.lang='fr-CA'; u.rate=vitTaux(0.9);\n"),
    # la voix du jeu de rôle
    ("const a=new Audio(url); jrAudio=a;",
     "const a=vitAudio(new Audio(url)); jrAudio=a;"),
    # son repli en synthèse vocale
    ("u.lang='fr-CA'; u.rate=0.95;\n",
     "u.lang='fr-CA'; u.rate=vitTaux(0.95);\n"),
]


def poser(chemin):
    s = io.open(chemin, encoding="utf-8").read()
    nom = chemin.split("/")[-2] if "/module-" in chemin else "gabarit"
    if DEBUT in s:
        return nom, False
    for ancre, remplacement in ((CSS_ANCRE, CSS), (HTML_ANCRE, HTML), (JS_ANCRE, JS)):
        if s.count(ancre) != 1:
            print("   !! %s : ancre absente ou multiple, laissé tel quel" % nom)
            return nom, False
        s = s.replace(ancre, remplacement, 1)
    for avant, apres in POINTS:
        s = s.replace(avant, apres, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return nom, True


def retirer(chemin):
    s = io.open(chemin, encoding="utf-8").read()
    nom = chemin.split("/")[-2] if "/module-" in chemin else "gabarit"
    if DEBUT not in s:
        return nom, False
    for apres, avant in ((CSS, CSS_ANCRE), (HTML, HTML_ANCRE), (JS, JS_ANCRE)):
        s = s.replace(apres, avant, 1)
    for avant, apres in POINTS:
        s = s.replace(apres, avant, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return nom, True


def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--retirer", action="store_true",
                   help="remettre les modules dans leur état d'avant la greffe")
    args = p.parse_args()

    action = retirer if args.retirer else poser
    fichiers = sorted(glob.glob(MODULES)) + [GABARIT]
    if len(fichiers) < 2:
        sys.exit("!! aucun module trouvé — lancer depuis la racine du projet")

    faits, laisses = [], []
    for chemin in fichiers:
        nom, change = action(chemin)
        (faits if change else laisses).append(nom)

    verbe = "dégreffés" if args.retirer else "greffés"
    etat = "déjà propres" if args.retirer else "déjà greffés"
    print("%s : %d  %s" % (verbe, len(faits), " ".join(faits)))
    if laisses:
        print("%s : %s" % (etat, " ".join(laisses)))


if __name__ == "__main__":
    main()
