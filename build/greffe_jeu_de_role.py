#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pose sur les 78 modules à jeu de rôle le design remis par Claude Design.

    python3 build/greffe_jeu_de_role.py            # les 78 modules + le gabarit
    python3 build/greffe_jeu_de_role.py --essai module-n5-logement

La remise : ~/Downloads/design_handoff_jeu_de_role (version 4a).

CE QUI CHANGE, ET POURQUOI CE N'EST PAS QU'UNE FEUILLE DE STYLE
L'écran de départ portait cinq blocs empilés : les annonces en cartes d'affichage,
la liste des sujets à cocher, le rappel de langue, puis — après un filet — trois
rangées de pastilles pour choisir l'annonce, le rôle et le mode. Le même logement
était donc écrit deux fois : une fois pour être lu, une fois pour être choisi.
Le design fusionne les deux : la carte EST le bouton. D'où une réécriture du
balisage, et pas seulement des couleurs.

L'ordre devient : annonces → deux cartes de réglages → bande de départ → rappel
de langue. Les sujets à couvrir quittent leur liste à cocher pour entrer dans la
bande, en une phrase, à côté du bouton — c'est le choix de la remise.

LES IDENTIFIANTS NE BOUGENT PAS. `jrLogs`, `jrRoles`, `jrModes`, `jrStart` et la
classe `.jr-opt` sont le contrat que lisent `jrChoisir()`, `jrModeVoix()` et les
trois greffes déjà posées (écouter sans lire, verrou d'écoute, débit). Les tuiles
gardent donc `jr-opt` et gagnent une seconde classe : le nouveau dessin passe par
elle, l'ancien mécanisme continue de fonctionner sans qu'on y touche.

LE RETRAIT SE FAIT PAR GIT. La transformation n'est pas une insertion : elle
déplace et fusionne des blocs. Un `--retirer` fidèle serait un second greffon à
maintenir, et un `--retirer` approximatif rendrait des modules à moitié défaits.
L'arbre doit donc être propre avant de lancer : `git checkout` rend tout.

TROIS ADAPTATIONS ASSUMÉES — la remise dessine le module « logement » de niveau 5,
le greffon en sert 78 :
  1. La grille d'annonces est en `auto-fit` et non en trois colonnes fixes : le
     nombre de cas varie d'un module à l'autre.
  2. Les tuiles de rôle n'ont pas d'icône. La remise montre une personne et une
     clé — deux dessins qui ne veulent dire quelque chose que pour une visite de
     logement. Deux icônes identiques sur les 78 se liraient comme un défaut.
     Le crayon et le micro, eux, sont posés : ils sont vrais partout.
  3. La remise sépare le titre, le prix et le détail. Les modules n'ont que le
     titre et un texte d'annonce : la tuile porte donc deux lignes, pas trois.
"""
import re, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GABARIT = BASE / "build" / "gabarit" / "module.html"
INTER = BASE / "assets" / "interactive"

SENTINELLE = "/* JR-DESIGN-4A */"

# ── Les icônes de la remise, trait 1.8, `currentColor` : elles blanchissent
#    d'elles-mêmes sur la plaque encre d'une tuile choisie.
SVG = ('<svg viewBox="0 0 24 24" width="26" height="26" fill="none" stroke="currentColor"'
       ' stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>')
ICONE_CRAYON = SVG % '<path d="M4 20h4l10-10-4-4L4 16v4z"></path><path d="M14 6l4 4"></path>'
ICONE_MICRO = SVG % ('<rect x="9" y="3" width="6" height="11" rx="3"></rect>'
                     '<path d="M5.5 11.5a6.5 6.5 0 0013 0M12 18v3"></path>')
ICONE_COCHE = ('<svg viewBox="0 0 20 20" width="15" height="15" fill="none" stroke="currentColor"'
               ' stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
               '<path d="M4 10.5l4 4 8-9"></path></svg>')

CSS = SENTINELLE + r"""
/* ── Jeu de rôle · écran de départ (remise design_handoff_jeu_de_role, 4a) ──
   Les tuiles gardent `.jr-opt` — c'est ce que balaient jrChoisir() et
   jrModeVoix(). Ce bloc vient APRÈS `.jr-opt.on` dans la feuille : à
   spécificité égale, c'est lui qui gagne, et l'annonce choisie échappe donc à
   la plaque encre pour prendre le filet vert que demande la remise. */
.jr-annonces{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin:16px 0 0}
.jr-tuile{display:block;padding:0;min-height:0;border-radius:18px;overflow:hidden;text-align:left;
  border:1px solid var(--ws-line);background:var(--ws-card);font-weight:600;transition:border-color .14s}
.jr-tuile.on{background:var(--ws-card);color:var(--ws-ink);
  border:2px solid var(--sec-color,var(--ws-accent))}
.jr-tuile:hover{border-color:var(--sec-color,var(--ws-accent))}
.jr-band{display:flex;align-items:center;gap:8px;padding:12px 20px;font-size:13px;font-weight:900;
  letter-spacing:.14em;text-transform:uppercase;background:var(--surface-sunken,#FBFBFA);
  border-bottom:1px solid var(--ws-line);color:var(--ws-sub)}
.jr-tuile.on .jr-band{background:var(--sec-color,var(--ws-accent));color:#fff;border-bottom-color:transparent}
.jr-tuile .jr-band-on{display:none}
.jr-tuile.on .jr-band-on{display:flex;align-items:center;gap:8px}
.jr-tuile.on .jr-band-off{display:none}
.jr-tuile-c{display:flex;flex-direction:column;gap:8px;padding:20px}
.jr-tuile-t{font-size:24px;font-weight:900;color:var(--ws-ink);line-height:1.2}
.jr-tuile-d{font-size:17px;font-weight:600;color:var(--ws-sub);line-height:1.5}
.jr-tuile-d b{font-weight:900;color:var(--ws-ink)}
.jr-tuile.on .jr-tuile-d b{color:var(--sec-color,var(--ws-accent))}

.jr-reglages{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px}
.jr-carte{border:1px solid var(--ws-line);border-radius:18px;background:var(--ws-card);padding:20px}
.jr-champ-l{font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:.12em;
  color:var(--ws-sub);margin-bottom:12px}
.jr-tuiles{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.jr-tuiles .jr-opt{display:flex;flex-direction:column;align-items:center;justify-content:center;
  gap:8px;padding:16px;min-height:96px;border-radius:10px;text-align:center;font-size:17px;font-weight:700}
.jr-tuiles .jr-opt svg{flex-shrink:0}
/* La rangée « Écouter sans lire » est posée par greffe_ecouter_sans_lire.py
   juste après #jrModes : elle tombe donc dans la carte, sous les deux tuiles. */
.jr-carte #jrEcoute{margin-top:12px}
.jr-carte #jrEcoute .jr-opt{width:100%;min-height:44px;font-size:15px}
#jrMic svg{width:26px;height:26px}

.jr-bande{margin-top:16px;display:flex;align-items:center;justify-content:space-between;gap:24px;
  flex-wrap:wrap;padding:20px;border-radius:18px;background:var(--surface-band,#EDF6F1);
  border:1px solid var(--border-tint,var(--ws-line))}
.jr-bande-t{font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:.12em;
  color:var(--accent-ink,var(--ws-accent));margin-bottom:4px}
.jr-bande-p{font-size:17px;font-weight:600;color:var(--ws-ink);max-width:56ch;line-height:1.5}
.jr-bande .btn{flex-shrink:0;white-space:nowrap;min-height:52px;padding:0 24px;font-size:16px;font-weight:800}

.jr-rappel{margin-top:32px}
.jr-rappel-t{font-size:13px;font-weight:800;text-transform:uppercase;letter-spacing:.12em;
  color:var(--ws-sub);margin-bottom:12px}
.jr-rappel-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(45%,1fr));gap:20px 24px;padding:20px;border-radius:18px;
  background:var(--surface-band,#EDF6F1);border:1px solid var(--border-tint,var(--ws-line))}
.jr-rappel-l{font-size:17px;font-weight:600;color:var(--ws-sub)}
.jr-rappel-x{font-size:17px;font-weight:700;color:var(--ws-ink);margin-top:2px;line-height:1.45}
/* La structure visée était en gras ; la remise la veut en teinte acier. Le gras
   reste dans le contenu des modules — c'est la couleur qui porte le repérage. */
.jr-rappel-x b{font-weight:700;font-style:normal;color:var(--acier-600,#1D6B8F)}
@media(max-width:900px){
  .jr-annonces{grid-template-columns:1fr}
  .jr-reglages,.jr-rappel-g{grid-template-columns:1fr}
}
"""

ANCRE_CSS = ".jr-opt.on{background:var(--sel-bg);border-color:var(--sel-line);color:var(--sel-ink)}"


def minuscule(s):
    """Première lettre en bas de casse, pour enfiler les sujets en une phrase."""
    return s[:1].lower() + s[1:] if s else s


def region(t):
    """Les bornes du bloc de départ : de la grille d'annonces au bouton de départ."""
    d = t.find('<div class="jr-grid">')
    if d < 0:
        return None
    m = re.compile(r'<button class="btn btn-pri" id="jrStart"[^>]*>(?P<lbl>[^<]*)</button>\s*</div>').search(t, d)
    return (d, m.end(), m.group("lbl")) if m else None


def transforme(t, nom):
    r = region(t)
    if not r:
        return None, "pas d'écran de départ"
    deb, fin, label_depart = r
    bloc = t[deb:fin]

    # ── Les annonces : le titre et le texte se lisaient dans la carte
    #    d'affichage, l'identifiant et l'état choisi dans la pastille. La tuile
    #    de la remise a besoin des deux : on les prend là où ils sont.
    g = re.search(r'<div class="jr-grid">\s*\$\{(\w+)\.map\((\w+)=>`\s*'
                  r'<div class="jr-log">\s*<div class="jr-log-h">(.*?)</div>\s*'
                  r'<div class="jr-log-a">(.*?)</div>\s*</div>`\)\.join\(\'\'\)\}', bloc, re.S)
    b = re.search(r'id="jrLogs">\s*\$\{(\w+)\.map\(\((\w+),(\w+)\)=>`<button class="jr-opt\$\{(.*?)\?\' on\':\'\'\}"'
                  r' type="button" data-log="(.*?)" onclick="(.*?)">(.*?)</button>`\)\.join\(\'\'\)\}', bloc, re.S)
    if not g or not b:
        return None, "grille d'annonces ou rangée jrLogs hors norme"
    var, p_grille, expr_titre, expr_txt = g.group(1), g.group(2), g.group(3), g.group(4)
    p_btn, i_btn, sel, data, clic = b.group(2), b.group(3), b.group(4), b.group(5), b.group(6)
    # Les deux boucles n'ont pas forcément le même nom de paramètre.
    titre = expr_titre.replace("${%s." % p_grille, "${%s." % p_btn)
    detail = expr_txt.replace("${%s." % p_grille, "${%s." % p_btn)

    sujets = re.search(r'<div class="jr-sub">([^<]*)</div>\s*<div class="jr-sujets">\s*\$\{(\w+)\.map', bloc)
    if not sujets:
        return None, "liste de sujets hors norme"
    titre_sujets, var_sujets = sujets.group(1).strip(), sujets.group(2)

    gram = re.search(r'<div class="jr-gram">\s*<div class="jr-gram-t">([^<]*)</div>(.*?)\n\s*</div>', bloc, re.S)
    if not gram:
        return None, "rappel de langue hors norme"
    titre_gram, corps_gram = gram.group(1).strip(), gram.group(2)
    # « Étiquette : <span class='savoir-ex'>exemple</span> » — autant de paires
    # que le module en a écrit. Ni cinq ni quatre : ce qui s'y trouve.
    paires = re.findall(r'([^<>]*?)\s*:?\s*<span class=[\'"]savoir-ex[\'"]>(.*?)</span>', corps_gram, re.S)
    paires = [(" ".join(a.split()).rstrip(" :"), " ".join(x.split())) for a, x in paires]
    paires = [(a, x) for a, x in paires if a]
    if not paires:
        return None, "aucune paire étiquette/exemple dans le rappel"

    roles = re.search(r'<div class="jr-choix-l">([^<]*)</div>\s*<div class="jr-opts" id="jrRoles">(.*?)</div>', bloc, re.S)
    modes = re.search(r'<div class="jr-choix-l">([^<]*)</div>\s*<div class="jr-opts" id="jrModes">(.*?)</div>', bloc, re.S)
    if not modes:
        return None, "rangée des modes hors norme"
    intro = re.search(r'<div class="jr-sep"></div>\s*<div class="jr-sub">([^<]*)</div>', bloc)

    # Les deux boutons de mode perdent leurs émojis pour les icônes de la remise.
    b_modes = re.sub(r'>\s*✍️\s*[^<]*<', '>' + ICONE_CRAYON + "<span>J'écris</span><", modes.group(2))
    b_modes = re.sub(r'>\s*🎤\s*[^<]*<', '>' + ICONE_MICRO + '<span>Je parle</span><', b_modes)

    carte_roles = ""
    if roles:
        carte_roles = ('\n       <div class="jr-carte">\n'
                       '         <div class="jr-champ-l">%s</div>\n'
                       '         <div class="jr-tuiles" id="jrRoles">%s</div>\n'
                       '       </div>' % (roles.group(1).strip(), roles.group(2)))

    neuf = '''<div class="jr-annonces" id="jrLogs">
       ${%(var)s.map((%(p)s,%(i)s)=>`<button class="jr-opt jr-tuile${%(sel)s?' on':''}" type="button" data-log="%(data)s" onclick="%(clic)s">
         <span class="jr-band"><span class="jr-band-off">Choix ${%(i)s+1}</span><span class="jr-band-on">%(coche)s Votre choix</span></span>
         <span class="jr-tuile-c"><span class="jr-tuile-t">%(titre)s</span><span class="jr-tuile-d">%(detail)s</span></span>
       </button>`).join('')}
     </div>
     <div class="jr-reglages">%(roles)s
       <div class="jr-carte">
         <div class="jr-champ-l">%(lmodes)s</div>
         <div class="jr-tuiles" id="jrModes">%(modes)s</div>
       </div>
     </div>
     <div class="jr-bande">
       <div>
         <div class="jr-bande-t">%(tsujets)s</div>
         <p class="jr-bande-p">${%(vsujets)s.map((s,i)=>i?s.charAt(0).toLowerCase()+s.slice(1):s).join(', ')}.</p>
       </div>
       <button class="btn btn-pri" id="jrStart" type="button" onclick="jrDemarrer()">%(depart)s</button>
     </div>
     <div class="jr-rappel">
       <div class="jr-rappel-t">%(tgram)s</div>
       <div class="jr-rappel-g">%(gram)s
       </div>
     </div>''' % {
        "var": var, "p": p_btn, "i": i_btn, "sel": sel, "data": data, "clic": clic,
        "coche": ICONE_COCHE, "titre": titre, "detail": detail,
        "roles": carte_roles, "lmodes": modes.group(1).strip(), "modes": b_modes,
        "tsujets": titre_sujets, "vsujets": var_sujets, "depart": label_depart,
        "tgram": titre_gram,
        "gram": "".join(
            '\n         <div><div class="jr-rappel-l">%s</div>'
            '<div class="jr-rappel-x">%s</div></div>' % (a, x) for a, x in paires),
    }
    if intro:
        neuf = '<p class="lead">%s</p>\n     %s' % (intro.group(1).strip(), neuf)
    return t[:deb] + neuf + t[fin:], "%d annonce(s) dynamiques · %d paires de rappel" % (1, len(paires))


def pose(chemin, avec_css=True):
    """Le balisage se pose partout ; la feuille seulement là où elle vit.

    Un module livré porte les deux. `build/contenu/<slug>/custom.js` ne porte
    que le balisage — et c'est LUI que relit une reconstruction. Sans cette
    seconde passe, le premier `build/module.py` rendrait aux 77 modules
    reconstructibles leur ancien écran, sans que rien ne le signale.
    """
    t = chemin.read_text(encoding="utf-8")
    if 'id="jrModes"' not in t:
        return "sans jeu de rôle"
    if SENTINELLE in t or 'class="jr-annonces"' in t:
        return "déjà posé"
    if avec_css and t.count(ANCRE_CSS) != 1:
        return "ANCRE CSS introuvable"
    neuf, note = transforme(t, chemin.name)
    if neuf is None:
        return "REFUS : " + note
    if avec_css:
        neuf = neuf.replace(ANCRE_CSS, ANCRE_CSS + "\n" + CSS, 1)
    # L'émoji de l'oreille s'en va lui aussi : la remise n'en veut aucun.
    neuf = neuf.replace("'👂 Écoute seule — texte caché' : '👂 Écouter sans lire'",
                        "'Écoute seule — texte caché' : 'Écouter sans lire'")
    neuf = neuf.replace("+'👂 Écouter sans lire</button>'", "+'Écouter sans lire</button>'")
    # Le dernier émoji du jeu de rôle : le micro de l'écran de conversation.
    # La remise n'en veut aucun, et l'icône blanchit d'elle-même sur le rond
    # rouge — c'est le seul aplat rouge autorisé, celui de l'audio.
    neuf = neuf.replace('aria-label="Parler">🎤</button>',
                        'aria-label="Parler">' + ICONE_MICRO + '</button>')
    # `rec.onend` remet l'étiquette du bouton : en `textContent`, il aurait
    # effacé le SVG et rendu l'émoji au premier enregistrement. Le défaut ne se
    # serait vu qu'après avoir parlé une fois — jamais à la relecture du code.
    neuf = neuf.replace("btn.classList.remove('rec'); btn.textContent='🎤';",
                        "btn.classList.remove('rec'); btn.innerHTML=JR_MICRO;")
    if "JR_MICRO" in neuf and "const JR_MICRO" not in neuf:
        neuf = neuf.replace("const JR = {", "const JR_MICRO = '%s';\nconst JR = {"
                            % ICONE_MICRO.replace("'", "\\'"), 1)
    chemin.write_text(neuf, encoding="utf-8")
    return "posé — " + note


def main():
    seul = None
    if "--essai" in sys.argv:
        seul = sys.argv[sys.argv.index("--essai") + 1]
    cibles = [(c, True) for c in sorted(INTER.glob("module-*/module-*-activite-interactive.html"))]
    sources = [(c, False) for c in sorted((BASE / "build" / "contenu").glob("*/custom.js"))]
    if seul:
        cibles = [(c, k) for c, k in cibles if c.parent.name == seul]
        sources = [(c, k) for c, k in sources if c.parent.name == seul]
    cibles += sources
    bilan = {}
    for c, avec_css in cibles:
        r = pose(c, avec_css)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith("REFUS") or "introuvable" in r:
            print("  %-24s %-10s %s" % (c.parent.name, c.suffix, r))
    if not seul:
        g = GABARIT.read_text(encoding="utf-8")
        if SENTINELLE in g:
            bilan["gabarit : feuille déjà posée"] = 1
        elif g.count(ANCRE_CSS) == 1:
            GABARIT.write_text(g.replace(ANCRE_CSS, ANCRE_CSS + "\n" + CSS, 1), encoding="utf-8")
            bilan["gabarit : feuille posée"] = 1
        else:
            bilan["gabarit : ANCRE CSS introuvable"] = 1
    for k, v in sorted(bilan.items()):
        print("%4d  %s" % (v, k))


if __name__ == "__main__":
    main()
