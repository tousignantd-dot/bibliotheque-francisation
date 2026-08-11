# -*- coding: utf-8 -*-
"""
Fiches élèves imprimables · Bibliothèque de francisation
=========================================================

Deuxième moteur de rendu branché sur les MÊMES fichiers de contenu que les
présentations. `decks/b2.py` produit la séance B2 en PowerPoint quand il est
lu par `theme.Deck`, et la fiche élève B2 quand il est lu par `fiche.Deck`.
Un seul contenu, deux sorties : elles ne peuvent pas diverger.

Ce que la fiche fait autrement que la présentation
---------------------------------------------------
- **Les notes d'enseignant disparaissent.** Elles pilotent la classe ; elles
  n'ont rien à faire entre les mains de l'élève.
- **Les corrigés disparaissent aussi.** Un exercice devient un énoncé suivi
  d'une ligne à remplir. Les réponses restent dans le PowerPoint, sous les
  yeux de l'enseignant seulement.
- **Les déclencheurs disparaissent** : ce sont des questions à poser à l'oral
  avant d'ouvrir quoi que ce soit. Les imprimer les désamorcerait.
- **Les dialogues, les règles, les tableaux et le vocabulaire restent** : ce
  sont les traces que l'élève relit chez lui.

Format et fidélité au système de design
----------------------------------------
Format **lettre** (8,5 × 11 po), marges de 14 × 15 mm, un seul flux : les
blocs ne se coupent jamais entre deux pages. Contrairement au PowerPoint,
une page HTML peut charger **Nunito** : la police du système est respectée
ici, sans substitution. Rayons, filets et espacements descendent de
`assets/design-system/`.

Trois adaptations, propres au papier photocopié :

1. **Aucune couleur.** Les fiches sont tirées en noir et blanc : une teinte
   de section devient un gris indistinct, et deux teintes de rétroaction
   deviennent le même gris. Toute la hiérarchie passe donc par la graisse,
   les filets et les mots. C'est la règle du système — « jamais
   d'information portée par la couleur seule » — poussée à son terme.
2. **Aucun aplat foncé.** Le système en autorise un par page ; à
   l'impression il vide une cartouche. Le billet de sortie devient un
   encadré à filet épais.
3. **Corps de 11,5 pt.** La règle « jamais sous 17 px » vise un écran tenu à
   40 cm. Sur papier tenu à 30 cm, 11,5 pt donne une hauteur d'œil
   équivalente. Rien ne descend sous 9,5 pt, réservé aux sur-titres. Les
   gris sont assombris d'un cran par rapport à l'écran : une photocopieuse
   efface tout ce qui est plus clair que 15 % de noir.
"""

import os
import re
import unicodedata

# On lit les jetons dans le socle des présentations : une seule source.
from theme import C, SECTIONS


def esc(t):
    return (str(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def _slug(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    s = re.sub(r'[^a-zA-Z0-9]+', '-', s).strip('-').lower()
    return re.sub(r'-+', '-', s)[:48]


CSS = """
/* ═══════════════════════════════════════════════════════════════
   FICHE ÉLÈVE · IMPRESSION LETTRE, NOIR ET BLANC
   ───────────────────────────────────────────────────────────────
   Aucune couleur : ces fiches sont photocopiées en noir et blanc.
   Toute la hiérarchie passe par la GRAISSE, les FILETS et les MOTS.
   C'est d'ailleurs la règle du système de design poussée à son
   terme : « jamais d'information portée par la couleur seule ».

   Les gris viennent des neutres du système (ink-900 à ink-400),
   qui sont déjà quasi neutres. Les filets sont volontairement plus
   sombres qu'à l'écran : une photocopieuse efface tout ce qui est
   plus clair que 15 % de noir.
   ═══════════════════════════════════════════════════════════════ */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --paper:#FFFFFF;
  --tint:#F0F0EE;          /* aplat le plus clair encore visible en photocopie */
  --line:#C9C9C6;          /* filet fin */
  --rule:#17181A;          /* filet structurant */
  --ink:#17181A;           /* titres */
  --body:#2B2E30;          /* texte courant, un cran plus sombre qu'à l'écran */
  --soft:#4B4F52;          /* texte secondaire */
  --muted:#5E6165;         /* sur-titres, méta */
}
html{background:#BBBBBB}
body{
  font-family:'Nunito','Trebuchet MS',sans-serif;
  font-size:11.5pt; line-height:1.5; color:var(--body);
  background:var(--paper);
  width:215.9mm;                    /* 8,5 po — format lettre */
  margin:0 auto; padding:14mm 15mm 16mm;
  -webkit-print-color-adjust:exact; print-color-adjust:exact;
}
h1,h2,h3{color:var(--ink); line-height:1.2; letter-spacing:-0.01em}

/* ── En-tête ── */
.hdr{border-bottom:2.5px solid var(--rule); padding-bottom:8px; margin-bottom:14px;
     display:flex; align-items:flex-end; gap:14px}
.hdr-l{flex:1}
.eyebrow{font-size:9.5pt; font-weight:800; text-transform:uppercase;
         letter-spacing:.12em; color:var(--muted)}
.hdr h1{font-size:22pt; font-weight:900; margin-top:3px}
.hdr-r{flex-shrink:0; display:flex; gap:10px; align-items:flex-end;
       font-size:9.5pt; font-weight:800; text-transform:uppercase;
       letter-spacing:.08em; color:var(--muted); padding-bottom:2px}
.nomline{display:inline-block; border-bottom:1.5px solid var(--rule);
         height:6mm; vertical-align:bottom; margin-left:5px}
.nomline--nom{width:48mm} .nomline--date{width:26mm}
.chapeau{font-size:12pt; font-weight:600; color:var(--soft); margin-bottom:16px}

/* ── Blocs ── */
.bloc{break-inside:avoid; page-break-inside:avoid; margin-bottom:13px}
.card{border:1px solid var(--line); border-radius:12px; padding:11px 14px 12px;
      background:var(--paper)}
.lbl{font-size:9.5pt; font-weight:800; text-transform:uppercase;
     letter-spacing:.12em; color:var(--muted); margin-bottom:5px}
h2.t{font-size:15pt; font-weight:900; margin-bottom:7px}
.consigne{font-size:11pt; font-weight:600; color:var(--soft); margin-bottom:8px}

/* ── Objectifs et exercices : pastille en cerne, jamais en aplat ── */
ol.obj,ol.ex{list-style:none}
ol.obj{counter-reset:o} ol.ex{counter-reset:e}
ol.obj li,ol.ex li{position:relative; padding-left:9mm; font-weight:600}
ol.obj li{counter-increment:o; margin-bottom:6px}
ol.ex li{counter-increment:e; margin-bottom:9px; break-inside:avoid}
ol.obj li::before,ol.ex li::before{
  position:absolute; left:0; top:0; width:6mm; height:6mm; border-radius:50%;
  border:1.5px solid var(--rule); color:var(--ink);
  font-size:9.5pt; font-weight:800;
  display:flex; align-items:center; justify-content:center}
ol.obj li::before{content:counter(o)}
ol.ex li::before{content:counter(e)}

/* ── Dialogue ── */
.rep{display:flex; gap:10px; padding:4px 0; border-top:1px solid var(--line)}
.rep:first-of-type{border-top:0}
.rep--key{background:var(--tint); border-radius:8px; padding:5px 8px;
          border-top:0; margin:2px 0}
.qui{flex:0 0 30mm; font-weight:800; color:var(--ink); font-size:10.5pt}

/* ── Règle : encadrée au filet épais, c'est elle qu'on repère de loin ── */
.regle{border:2.5px solid var(--rule); border-radius:12px; padding:12px 14px}
.regle .lbl{color:var(--ink)}
.regle p.r{font-size:14pt; font-weight:900; color:var(--ink); line-height:1.3}
.regle p.pr{margin-top:7px; font-weight:600; color:var(--soft)}

/* ── Tableau ── */
table{width:100%; border-collapse:collapse}
th{font-size:9.5pt; font-weight:800; text-transform:uppercase; letter-spacing:.1em;
   color:var(--muted); text-align:left; padding:0 8px 5px 0;
   border-bottom:1.5px solid var(--rule)}
td{padding:6px 8px 6px 0; border-top:1px solid var(--line); vertical-align:top;
   font-weight:600}
td.cle{font-weight:900; color:var(--ink)}   /* la colonne clé : en gras, pas en couleur */
.note{margin-top:8px; font-size:10.5pt; font-weight:600; color:var(--soft);
      background:var(--tint); border-radius:9px; padding:8px 11px}

/* ── Cartes ── */
.grid{display:grid; grid-template-columns:1fr 1fr; gap:9px}
.grid .card h3{font-size:11.5pt; font-weight:900; color:var(--ink); margin-bottom:3px}
.grid .card p{font-size:11pt}

/* ── Piège : le filet distingue les deux colonnes, pas la couleur ──
   À gauche, un filet TIRETÉ — ce qui ne tient pas.
   À droite, un filet PLEIN et épais — ce qu'il faut retenir.
   Les deux intitulés disent la même chose en mots.                */
.duo{display:grid; grid-template-columns:1fr 1fr; gap:10px}
.duo>div{border-radius:12px; padding:10px 13px}
.duo .no{border:1.5px dashed var(--muted)}
.duo .ok{border:2.5px solid var(--rule); background:var(--tint)}
.duo .k{font-size:9.5pt; font-weight:800; text-transform:uppercase;
        letter-spacing:.1em; margin-bottom:4px; color:var(--muted)}
.duo .ok .k{color:var(--ink)}
.duo p.ph{font-size:12pt; font-weight:800; color:var(--ink); line-height:1.3}
.duo .no p.ph{font-weight:600; font-style:italic; color:var(--soft)}

/* ── Vocabulaire ── */
.voc{width:100%; border-collapse:collapse}
.voc td{border-top:1px solid var(--line); padding:6px 8px 6px 0}
.voc td.mot{width:38%; font-weight:900; color:var(--ink)}
.voc td.def{color:var(--soft)}

/* ── Zones de réponse ── */
.ligne{display:block; border-bottom:1px dotted #8E8E8A; height:8mm; margin-top:2px}
.ligne--court{width:55%}

/* ── Billet de sortie ── */
.billet{border:2.5px solid var(--rule); border-radius:12px; padding:13px 15px}
.billet .k{font-size:9.5pt; font-weight:800; text-transform:uppercase;
           letter-spacing:.12em; color:var(--ink); margin-bottom:4px}
.billet p.c{font-size:14pt; font-weight:900; color:var(--ink); line-height:1.3}
.billet ul{list-style:none; margin-top:7px}
.billet li{font-weight:600; color:var(--soft); margin-bottom:3px}

/* ── Pied ── */
footer{margin-top:16px; padding-top:7px; border-top:1px solid var(--line);
       font-size:9.5pt; font-weight:700; color:var(--muted);
       display:flex; justify-content:space-between}

/* ── Impression ── */
@page{size:8.5in 11in; margin:14mm 15mm}
@media print{
  html{background:#FFFFFF}
  body{width:auto; padding:0}
  .bloc{break-inside:avoid; page-break-inside:avoid}
  h2.t,.lbl{break-after:avoid; page-break-after:avoid}
}
"""


class Deck:
    """Même interface que `theme.Deck`, sortie HTML imprimable."""

    MODULE = 'Pouvez-vous régler le problème ?'

    def __init__(self, code, section, titre, chapeau, duree):
        self.code, self.titre_deck = code, titre
        self.chapeau, self.duree = chapeau, duree
        sec, sec_soft = SECTIONS[section]
        self.sec, self.sec_soft = C[sec], C[sec_soft]
        self.blocs = []

    # ── helpers ─────────────────────────────────────────────────────
    def _add(self, html):
        self.blocs.append(html)

    def _tete(self, surtitre, titre):
        return (f'<div class="lbl">{esc(surtitre)}</div>'
                f'<h2 class="t">{esc(titre)}</h2>')

    # ── gabarits ────────────────────────────────────────────────────
    def titre(self, notes=''):
        """L'en-tête de la fiche. Rien à imprimer de plus : le chapeau et le
        titre sont déjà posés par `save()`."""
        return self

    def objectifs(self, items, notes=''):
        lis = ''.join(f'<li>{esc(i)}</li>' for i in items)
        self._add('<section class="bloc card">'
                  + self._tete('Objectifs', 'À la fin, je serai capable de…')
                  + f'<ol class="obj">{lis}</ol></section>')
        return self

    def declencheur(self, surtitre, question, image=None, pistes=None, notes=''):
        """Non imprimé : c'est une question posée à l'oral, avant d'ouvrir la
        fiche. L'imprimer donnerait la réponse d'avance."""
        return self

    def regle(self, surtitre, phrase, precision=None, notes=''):
        pr = f'<p class="pr">{esc(precision)}</p>' if precision else ''
        self._add(f'<section class="bloc regle"><div class="lbl">{esc(surtitre)}</div>'
                  f'<p class="r">{esc(phrase)}</p>{pr}</section>')
        return self

    def tableau(self, surtitre, titre, entetes, lignes, note=None, notes='',
                cle=None, props=None):
        th = ''.join(f'<th>{esc(e)}</th>' for e in entetes)
        tr = ''
        for lg in lignes:
            tds = ''.join(
                f'<td class="cle">{esc(c)}</td>' if cle is not None and i == cle
                else f'<td>{esc(c)}</td>' for i, c in enumerate(lg))
            tr += f'<tr>{tds}</tr>'
        nt = f'<div class="note">{esc(note)}</div>' if note else ''
        self._add('<section class="bloc card">' + self._tete(surtitre, titre)
                  + f'<table><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>'
                  + nt + '</section>')
        return self

    def cartes(self, surtitre, titre, items, cols=2, notes=''):
        cs = ''.join(f'<div class="card"><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
                     for h, p in items)
        self._add('<section class="bloc">' + self._tete(surtitre, titre)
                  + f'<div class="grid">{cs}</div></section>')
        return self

    def dialogue(self, surtitre, titre, repliques, consigne=None, notes=''):
        cg = f'<p class="consigne">{esc(consigne)}</p>' if consigne else ''
        rs = ''
        for qui, txt, evid in repliques:
            cl = 'rep rep--key' if evid else 'rep'
            rs += (f'<div class="{cl}"><div class="qui">{esc(qui)}</div>'
                   f'<div>{esc(txt)}</div></div>')
        self._add('<section class="bloc card">' + self._tete(surtitre, titre)
                  + cg + rs + '</section>')
        return self

    def piege(self, surtitre, faux, juste, explication, notes=''):
        # Sur une diapositive, le titre « Le piège le plus fréquent » sert de
        # signal. Sur une fiche qui en contient deux ou trois, il se répète
        # bêtement : c'est le sur-titre, propre à chaque piège, qui titre ici.
        self._add('<section class="bloc">'
                  + f'<div class="lbl">Attention</div><h2 class="t">{esc(surtitre)}</h2>'
                  + '<div class="duo">'
                  + f'<div class="no"><div class="k">On entend souvent</div>'
                    f'<p class="ph">{esc(faux)}</p></div>'
                  + f'<div class="ok"><div class="k">Il faut dire plutôt</div>'
                    f'<p class="ph">{esc(juste)}</p></div></div>'
                  + f'<div class="note">{esc(explication)}</div></section>')
        return self

    def pratique(self, surtitre, titre, consigne, items, corrige=None,
                 cols=1, notes=''):
        """L'exercice, sans sa réponse. La longueur de la ligne s'ajuste à la
        réponse attendue : une ligne courte pour « VRAI », une ligne pleine
        pour une phrase. C'est un indice utile, pas une fuite du corrigé."""
        lis = ''
        for it in items:
            rep = it[1] if len(it) > 1 else ''
            court = len(rep) <= 22
            cl = 'ligne ligne--court' if court else 'ligne'
            lis += (f'<li><span class="q">{esc(it[0])}</span>'
                    f'<span class="{cl}"></span></li>')
        self._add('<section class="bloc card">' + self._tete(surtitre, titre)
                  + f'<p class="consigne">{esc(consigne)}</p>'
                  + f'<ol class="ex">{lis}</ol></section>')
        return self

    def vocabulaire(self, surtitre, titre, mots, notes=''):
        tr = ''.join(f'<tr><td class="mot">{esc(m)}</td>'
                     f'<td class="def">{esc(d)}</td></tr>' for m, d in mots)
        self._add('<section class="bloc card">' + self._tete(surtitre, titre)
                  + f'<table class="voc"><tbody>{tr}</tbody></table></section>')
        return self

    def billet(self, consigne, exemples=None, notes=''):
        ex = ''
        if exemples:
            ex = '<ul>' + ''.join(f'<li>{esc(e)}</li>' for e in exemples) + '</ul>'
        lignes = '<span class="ligne"></span>' * 3
        self._add('<section class="bloc billet">'
                  '<div class="k">Billet de sortie</div>'
                  f'<p class="c">{esc(consigne)}</p>{ex}{lignes}</section>')
        return self

    # ── enregistrement ──────────────────────────────────────────────
    def save(self, dossier):
        # La feuille de style ne dépend plus d'aucun jeton de couleur :
        # la fiche est en noir et blanc, elle est donc la même pour les
        # seize séances.
        css = CSS
        html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(self.code)} · {esc(self.titre_deck)} — Fiche élève</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header class="hdr">
  <div class="hdr-l">
    <div class="eyebrow">Séance {esc(self.code)} · Module 9 · {esc(self.duree)}</div>
    <h1>{esc(self.titre_deck)}</h1>
  </div>
  <div class="hdr-r"><span>Nom<span class="nomline nomline--nom"></span></span><span>Date<span class="nomline nomline--date"></span></span></div>
</header>
<p class="chapeau">{esc(self.chapeau)}</p>
{''.join(self.blocs)}
<footer><span>{esc(self.code)} · {esc(self.MODULE)}</span><span>Fiche élève</span></footer>
</body>
</html>
"""
        nom = f'module-probleme-{self.code.lower()}-{_slug(self.titre_deck)}.html'
        chemin = os.path.join(dossier, nom)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(html)
        return chemin, len(self.blocs)
