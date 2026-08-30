# -*- coding: utf-8 -*-
"""Les diaporamas de la trousse, en HTML animé — le même contenu, l'autre sortie.

**Une seule source, deux formats.** Cette classe porte exactement les mêmes
méthodes que `theme.Deck` : `titre`, `chapitre`, `parcours`, `objectifs`,
`regle`, `tableau`, `cartes`, `dialogue`, `piege`, `billet`, plus `ecran` pour
les captures. Les dix fichiers de `pitch/` ne changent pas d'une ligne et
produisent les deux. C'est la seule façon d'éviter qu'une version dise une
chose et l'autre une autre — le défaut que ce dépôt paie ailleurs.

    python3 build/powerpoints/pitch.py --web        # les dix en HTML
    python3 build/powerpoints/pitch.py --web p1

**Pourquoi le HTML.** Le `.pptx` était fade, et pas par accident : son thème est
celui des diaporamas de **séance**, sobre exprès, lisible du fond d'une classe
pendant quatre heures. C'est faux pour capter une salle en vingt minutes. Ici
on peut animer, mettre une capture plein cadre, montrer un chiffre énorme — et
il n'y a pas de dialogue « PowerPoint doit réparer ce fichier » à craindre.

**Les cinq mouvements** viennent du canevas de Claude Design
(`travailler-avec-claude.html`) : monter, tomber, éclore, grandir, venir de
côté. Chaque bloc d'un écran entre à son tour, décalé de 90 ms — c'est le
décalage qui fait la vie, pas la durée.

**Ce qui est repris du guide existant** (`assets/outils/guide-espace-enseignant.html`,
vingt écrans écrits à la main) : écrans en `position:absolute` dont un seul est
visible, défilement quand un écran dépasse la hauteur, navigation au clavier,
sommaire en surimpression, et un `@media print` qui les déplie tous. Ces
décisions ont déjà été éprouvées ; les réinventer serait les repayer.

Trois choses en plus, que le papier et le `.pptx` ne savent pas faire :

  · **les notes du présentateur à l'écran** (touche `N`), sur l'appareil de
    celui qui parle — elles existaient déjà dans les blocs, personne ne les
    voyait pendant une projection ;
  · une **barre de progression** et le numéro d'écran, pour savoir où l'on en
    est sans compter ;
  · le **plein écran** (touche `F`), sans quoi la barre du navigateur mange le
    haut de la projection.
"""

import html
import os
import re

from theme import C, SECTIONS

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))


def e(t):
    """Échappe, mais laisse passer le gras et l'italique que les blocs écrivent.

    Les fichiers de contenu portent déjà `<b>` et `<em>` — c'est le balisage du
    dépôt, et `theme.fragments()` le lit de son côté pour le `.pptx`."""
    t = html.escape(str(t), quote=False)
    for balise in ('b', 'em', 'i', 'strong'):
        t = t.replace('&lt;%s&gt;' % balise, '<%s>' % balise)
        t = t.replace('&lt;/%s&gt;' % balise, '</%s>' % balise)
    return t


def slug(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower().replace("'", "-")
               .replace("é", "e").replace("è", "e").replace("ê", "e")
               .replace("à", "a").replace("ç", "c").replace("î", "i")
               .replace("ô", "o").replace("û", "u").replace("ù", "u"))
    return s.strip("-")


class Deck:
    """Même interface que `theme.Deck`, sortie HTML."""

    def __init__(self, code, section, titre, chapeau, duree):
        self.code = code
        self.section = section
        self.titre_deck = titre
        self.chapeau = chapeau
        self.duree = duree
        self.sec_600, self.sec_100 = SECTIONS[section]
        self.ecrans = []          # [(html, titre_sommaire, notes)]

    # ── plomberie ────────────────────────────────────────────────────
    def _poser(self, corps, titre_sommaire, notes='', classe=''):
        self.ecrans.append((corps, titre_sommaire, notes or '', classe))

    def _entete(self, surtitre, titre):
        return ('<p class="sur" data-anim="1">%s</p>'
                '<h2 data-anim="2">%s</h2>' % (e(surtitre.upper()), e(titre)))

    # ── gabarit 1 · page de titre ────────────────────────────────────
    def titre(self, notes='', surtitre=None):
        corps = ('<div class="dia--titre">'
                 '<p class="sur" data-anim="1">%s</p>'
                 '<h1 data-anim="2">%s</h1>'
                 '<p class="chapeau" data-anim="3">%s</p>'
                 '<p class="duree" data-anim="4">%s</p>'
                 '</div>'
                 % (e((surtitre or self.code).upper()), e(self.titre_deck),
                    e(self.chapeau), e(self.duree)))
        self._poser(corps, self.titre_deck, notes, 'est-titre')

    # ── gabarit 2 · jalon plein cadre ────────────────────────────────
    def chapitre(self, numero, titre, phrase=None, notes=''):
        corps = ('<div class="dia--jalon">'
                 '<p class="num" data-anim="1">%s</p>'
                 '<h2 data-anim="2">%s</h2>%s</div>'
                 % (e(numero), e(titre),
                    ('<p class="phrase" data-anim="3">%s</p>' % e(phrase))
                    if phrase else ''))
        self._poser(corps, titre, notes, 'est-jalon')

    # ── gabarit 3 · barre de parcours ────────────────────────────────
    def parcours(self, etapes, courant, titre='Le parcours', notes=''):
        pas = []
        for i, (nom, duree) in enumerate(etapes):
            etat = 'fait' if i < courant else ('ici' if i == courant else 'suite')
            pas.append('<li class="%s" style="--i:%d"><span class="pastille">%d</span>'
                       '<span class="nom">%s</span><span class="min">%s</span></li>'
                       % (etat, i + 3, i + 1, e(nom), e(duree)))
        corps = (self._entete('Le parcours', titre)
                 + '<ol class="parcours">%s</ol>' % ''.join(pas))
        self._poser(corps, titre, notes)

    # ── gabarit 4 · objectifs ────────────────────────────────────────
    def objectifs(self, items, notes=''):
        li = ''.join('<li style="--i:%d">%s</li>' % (i + 3, e(t))
                     for i, t in enumerate(items))
        corps = (self._entete('Objectifs', "Ce que vous saurez en sortant")
                 + '<ul class="objectifs">%s</ul>' % li)
        self._poser(corps, "Objectifs", notes)

    # ── gabarit 5 · la règle ─────────────────────────────────────────
    def regle(self, surtitre, phrase, precision=None, notes=''):
        corps = (self._entete(surtitre, phrase)
                 + ('<p class="precision" data-anim="3">%s</p>' % e(precision)
                    if precision else ''))
        self._poser(corps, phrase, notes, 'est-regle')

    # ── gabarit 6 · tableau ──────────────────────────────────────────
    def tableau(self, surtitre, titre, entetes, lignes, note=None, notes='',
                cle=None):
        th = ''.join('<th>%s</th>' % e(x) for x in entetes)
        tr = []
        for i, ln in enumerate(lignes):
            tds = ''.join('<td%s>%s</td>' % (' class="cle"' if cle == j else '', e(v))
                          for j, v in enumerate(ln))
            tr.append('<tr style="--i:%d">%s</tr>' % (i + 3, tds))
        corps = (self._entete(surtitre, titre)
                 + '<div class="cadre"><table><thead><tr>%s</tr></thead>'
                   '<tbody>%s</tbody></table></div>' % (th, ''.join(tr))
                 + ('<p class="note">%s</p>' % e(note) if note else ''))
        self._poser(corps, titre, notes)

    # ── gabarit 7 · cartes ───────────────────────────────────────────
    def cartes(self, surtitre, titre, items, cols=2, notes=''):
        cs = ''.join('<article style="--i:%d"><h3>%s</h3><p>%s</p></article>'
                     % (i + 3, e(t), e(p)) for i, (t, p) in enumerate(items))
        corps = (self._entete(surtitre, titre)
                 + '<div class="cartes" style="--cols:%d">%s</div>' % (cols, cs))
        self._poser(corps, titre, notes)

    # ── gabarit 8 · dialogue ─────────────────────────────────────────
    def dialogue(self, surtitre, titre, repliques, consigne=None, notes=''):
        li = ''.join('<li class="%s" style="--i:%d"><b>%s</b><span>%s</span></li>'
                     % ('fort' if fort else '', i + 4, e(qui), e(txt))
                     for i, (qui, txt, fort) in enumerate(repliques))
        corps = (self._entete(surtitre, titre)
                 + ('<p class="consigne" data-anim="3">%s</p>' % e(consigne)
                    if consigne else '')
                 + '<ul class="dialogue">%s</ul>' % li)
        self._poser(corps, titre, notes)

    # ── gabarit 9 · le piège ─────────────────────────────────────────
    def piege(self, surtitre, faux, juste, explication, notes=''):
        corps = (self._entete(surtitre, faux)
                 + '<p class="juste" data-anim="3">%s</p>' % e(juste)
                 + '<p class="precision" data-anim="4">%s</p>' % e(explication))
        self._poser(corps, faux, notes, 'est-piege')

    # ── gabarit 10 · une capture plein cadre ─────────────────────────
    def ecran(self, surtitre, titre, code, consigne, notes=''):
        """Une capture. **La disposition suit la forme de l'image.**

        Une capture de téléphone fait trois fois sa largeur en hauteur : posée
        au milieu d'un écran 16:9, elle laisse deux tiers de la surface vides et
        déborde quand même par le bas. Debout, on la met à côté du texte ; à
        plat, elle passe dessous, pleine largeur.
        """
        from vues import chemin_web, taille
        src = chemin_web(code)
        w, h = taille(code)
        debout = h > w * 1.15
        corps = ('<div class="bloc">%s%s</div>'
                 '<figure class="ecran" data-anim="4" style="--ar:%d/%d">'
                 '<img src="%s" alt="%s" loading="lazy"></figure>'
                 % (self._entete(surtitre, titre),
                    '<p class="consigne" data-anim="3">%s</p>' % e(consigne),
                    w, h, src, e(titre)))
        self._poser(corps, titre, notes,
                    'est-ecran' + (' debout' if debout else ''))

    # ── gabarit 11 · le billet de sortie ─────────────────────────────
    def billet(self, consigne, exemples=None, notes=''):
        ex = ''.join('<li style="--i:%d">%s</li>' % (i + 3, e(x))
                     for i, x in enumerate(exemples or []))
        corps = ('<div class="dia--billet">'
                 '<p class="sur" data-anim="1">POUR FINIR</p>'
                 '<p class="grand" data-anim="2">%s</p>'
                 '%s</div>'
                 % (e(consigne), ('<ul class="ex">%s</ul>' % ex) if ex else ''))
        self._poser(corps, "Pour finir", notes, 'est-billet')

    # ── écriture ─────────────────────────────────────────────────────
    def save(self, dossier):
        nom = '%s-%s.html' % (self.code, slug(self.titre_deck))
        chemin = os.path.join(dossier, nom)
        with open(chemin, 'w', encoding='utf-8') as f:
            f.write(self._page())
        return chemin, len(self.ecrans)

    def _page(self):
        dias = []
        for i, (corps, _, notes, classe) in enumerate(self.ecrans):
            dias.append(
                '<section class="dia %s" data-n="%d" aria-hidden="%s">%s'
                '<div class="notes" hidden>%s</div></section>'
                % (classe, i + 1, 'false' if i == 0 else 'true', corps,
                   e(notes) if notes else
                   '<em>Aucune note pour cet écran.</em>'))
        som = ''.join('<li><button data-va="%d"><span>%d</span>%s</button></li>'
                      % (i + 1, i + 1, e(t))
                      for i, (_, t, _, _) in enumerate(self.ecrans))
        return GABARIT % {
            'titre': e(self.titre_deck), 'code': e(self.code),
            'sec600': C[self.sec_600], 'sec100': C[self.sec_100],
            'ink900': C['ink_900'], 'ink700': C['ink_700'],
            'ink500': C['ink_500'], 'ink400': C['ink_400'],
            'line100': C['line_100'], 'line200': C['line_200'],
            'line300': C['line_300'], 'paper50': C['paper_50'],
            'paper100': C['paper_100'],
            'n': len(self.ecrans), 'dias': ''.join(dias), 'sommaire': som,
        }


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(code)s · %(titre)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<style>
  :root{
    --sec:#%(sec600)s; --sec-doux:#%(sec100)s;
    --ink-900:#%(ink900)s; --ink-700:#%(ink700)s; --ink-500:#%(ink500)s;
    --ink-400:#%(ink400)s; --line-100:#%(line100)s; --line-200:#%(line200)s;
    --line-300:#%(line300)s; --paper-50:#%(paper50)s; --paper-100:#%(paper100)s;
    /* **Les tailles suivent la hauteur autant que la largeur.** Un écran de
       1280x600 — la forme d'un portable très ordinaire — est large mais bas :
       en ne dimensionnant que sur `vw`, cinq écrans de F1 débordaient de 12 à
       79 px et devenaient défilants. En projection, ce qui défile est ce que
       la salle ne voit pas. Mesuré dans la page à trois formats, pas deviné. */
    --marge: clamp(20px, min(4.4vw, 6.2vh), 78px);
  }
  *{box-sizing:border-box}
  html,body{height:100%%; margin:0}
  body{background:var(--paper-100); color:var(--ink-900); overflow:hidden;
    font-family:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
    font-size:clamp(14px, min(1.5vw, 2.5vh), 21px); line-height:1.42;}

  /* Un seul écran visible. Le suivant est en place, prêt, mais retiré du flux
     et de l'ordre de tabulation — sans quoi la touche Tab visiterait les
     quinze écrans du diaporama. */
  .scene{position:absolute; inset:0}
  .dia{position:absolute; inset:0; overflow-y:auto;
    padding:var(--marge) var(--marge) calc(var(--marge) + 42px);
    opacity:0; visibility:hidden; pointer-events:none;
    display:flex; flex-direction:column; justify-content:center;}
  .dia.ici{opacity:1; visibility:visible; pointer-events:auto}

  /* Les cinq mouvements du canevas. Le décalage fait la vie, pas la durée :
     90 ms entre deux blocs, jamais plus — au-delà, la salle attend. */
  @keyframes monte{from{opacity:0; transform:translateY(18px)} to{opacity:1; transform:none}}
  @keyframes tombe{from{opacity:0; transform:translateY(-14px)} to{opacity:1; transform:none}}
  @keyframes eclot{from{opacity:0; transform:scale(.94)} to{opacity:1; transform:none}}
  @keyframes grandit{from{opacity:0; transform:scale(.86)} to{opacity:1; transform:none}}
  @keyframes cote{from{opacity:0; transform:translateX(-22px)} to{opacity:1; transform:none}}

  .dia.ici [data-anim]{animation:monte .42s both;
    animation-delay:calc((var(--d,0) + 0) * 90ms)}
  .dia.ici [data-anim="1"]{--d:0; animation-name:tombe}
  .dia.ici [data-anim="2"]{--d:1}
  .dia.ici [data-anim="3"]{--d:2}
  .dia.ici [data-anim="4"]{--d:3; animation-name:eclot}
  .dia.ici li[style*="--i"], .dia.ici article[style*="--i"],
  .dia.ici tr[style*="--i"]{animation:monte .42s both;
    animation-delay:calc(var(--i, 3) * 90ms)}
  .dia.ici .est-grand{animation-name:grandit}
  @media (prefers-reduced-motion: reduce){
    .dia.ici *{animation:none !important}
  }

  h1,h2,h3{margin:0; line-height:1.1; letter-spacing:-.02em}
  h1{font-size:clamp(34px, min(6.2vw, 10vh), 86px); font-weight:900}
  h2{font-size:clamp(24px, min(3.8vw, 6.4vh), 54px); font-weight:900;
    max-width:22ch}
  h3{font-size:1.02em; font-weight:800; color:var(--sec)}
  p{margin:0}
  .sur{font-size:.66em; font-weight:800; letter-spacing:.14em;
    text-transform:uppercase; color:var(--sec); margin-bottom:.7em}
  .chapeau{margin-top:.9em; font-size:1.06em; color:var(--ink-700); max-width:56ch}
  .duree{margin-top:1.6em; font-size:.8em; color:var(--ink-400)}
  .precision{margin-top:1.1em; font-size:.98em; color:var(--ink-700); max-width:64ch}
  .consigne{margin:.9em 0 0; font-size:.9em; color:var(--ink-400); max-width:72ch}
  .note{margin-top:1em; font-size:.82em; color:var(--ink-400)}

  .dia--titre h1{margin-top:.1em}
  .est-jalon{background:var(--ink-900); color:#fff}
  .est-jalon .num{font-size:.66em; font-weight:800; letter-spacing:.14em;
    text-transform:uppercase; color:var(--sec-doux); margin-bottom:.8em}
  .est-jalon h2{color:#fff; font-size:clamp(28px, min(5.2vw, 8.6vh), 72px);
    max-width:18ch}
  .est-jalon .phrase{margin-top:.9em; color:#C9CBCE; font-size:1.05em; max-width:52ch}

  .est-regle h2{font-size:clamp(26px, min(4.4vw, 7.4vh), 62px); max-width:19ch}
  .est-piege h2{color:var(--ink-500); font-weight:700}
  .juste{margin-top:.8em; font-size:clamp(21px, min(3.1vw, 5.2vh), 42px);
    font-weight:900;
    color:var(--sec); max-width:22ch; line-height:1.14}

  .parcours{list-style:none; margin:2em 0 0; padding:0; display:grid; gap:14px;
    max-width:44ch}
  .parcours li{display:flex; align-items:center; gap:14px; padding:12px 16px;
    border:1px solid var(--line-200); border-radius:12px; background:#fff}
  .parcours li.ici{border-color:var(--sec); background:var(--sec-doux)}
  .parcours li.fait{opacity:.5}
  .parcours .pastille{width:1.9em; height:1.9em; flex:0 0 auto; border-radius:50%%;
    display:grid; place-items:center; font-weight:800; font-size:.8em;
    background:var(--line-100); color:var(--ink-500)}
  .parcours li.ici .pastille{background:var(--sec); color:#fff}
  .parcours .nom{font-weight:700; flex:1}
  .parcours .min{color:var(--ink-400); font-size:.86em}

  .objectifs{list-style:none; margin:1.6em 0 0; padding:0; display:grid; gap:12px;
    max-width:58ch}
  .objectifs li{padding-left:1.6em; position:relative; color:var(--ink-700)}
  .objectifs li::before{content:""; position:absolute; left:0; top:.55em;
    width:.6em; height:.6em; border-radius:50%%; background:var(--sec)}

  .cadre{margin-top:1.5em; border:1px solid var(--line-200); border-radius:14px;
    overflow:auto; background:#fff}
  table{border-collapse:collapse; width:100%%; font-size:.92em}
  th,td{text-align:left; padding:12px 16px; border-bottom:1px solid var(--line-100)}
  th{font-size:.74em; font-weight:800; letter-spacing:.1em; text-transform:uppercase;
    color:var(--ink-400); background:var(--paper-50)}
  tbody tr:last-child td{border-bottom:0}
  td.cle{font-weight:800}

  .cartes{margin-top:1.5em; display:grid; gap:16px;
    grid-template-columns:repeat(auto-fit,minmax(min(280px,100%%),1fr))}
  .cartes article{background:#fff; border:1px solid var(--line-200);
    border-radius:14px; padding:18px 20px}
  .cartes p{margin-top:.45em; color:var(--ink-700); font-size:.93em}

  .dialogue{list-style:none; margin:1.3em 0 0; padding:0; display:grid; gap:10px;
    max-width:74ch}
  .dialogue li{display:grid; grid-template-columns:minmax(90px,auto) 1fr; gap:16px;
    padding:10px 14px; border-radius:10px}
  .dialogue li.fort{background:var(--sec-doux)}
  .dialogue b{color:var(--sec); font-weight:800; font-size:.86em;
    letter-spacing:.04em; text-transform:uppercase}

  /* `flex:1 1 0` et non `1 1 auto` : avec `auto`, la base est la hauteur de
     l'image, donc une capture haute pousse le bloc et déborde par le bas au
     lieu de se réduire. Vu à l'écran, pas en relisant. */
  /* **Le cadre porte le rapport de l'image**, connu à la génération. Sans lui,
     `max-height:100%%` ne mord pas : la boîte est dimensionnée par son contenu,
     la contrainte tourne en rond et le navigateur la laisse tomber — une
     capture de 782 px tenait dans un cadre de 550 et débordait. Mesuré dans la
     page, pas deviné. Avec `aspect-ratio`, le cadre se réduit à la hauteur
     disponible et la largeur suit : le filet épouse l'image, sans bande vide. */
  .est-ecran{gap:0}
  .ecran{margin:1.1em auto 0; aspect-ratio:var(--ar, 16/9);
    max-height:100%%; max-width:100%%; min-height:0; height:auto;
    border:1px solid var(--line-300); border-radius:12px; overflow:hidden;
    background:#fff; box-shadow:0 18px 44px rgba(0,0,0,.09)}
  .ecran img{display:block; width:100%%; height:100%%; object-fit:contain}
  /* Capture debout : le texte à gauche, l'écran à droite, sur toute la
     hauteur. C'est la seule façon d'employer un 16:9 avec une image 9:19. */
  @media (min-width: 860px){
    /* `stretch` et non `center` : avec `center`, la figure prend la hauteur de
       son contenu, `height:100%%` ne résout contre rien, et `overflow:hidden`
       rogne le bas de la capture. Vu à l'écran. */
    .est-ecran.debout{flex-direction:row; align-items:stretch;
      gap:clamp(24px,4vw,64px)}
    .est-ecran.debout .bloc{flex:1 1 auto; max-width:52ch;
      display:flex; flex-direction:column; justify-content:center}
    .est-ecran.debout .ecran{margin:0; flex:0 1 auto; align-self:center}
  }

  .est-billet{background:var(--ink-900); color:#fff}
  .est-billet .sur{color:var(--sec-doux)}
  .est-billet .grand{font-size:clamp(23px, min(3.6vw, 6vh), 50px); font-weight:900;
    line-height:1.14; max-width:26ch}
  .est-billet .ex{list-style:none; margin:1.6em 0 0; padding:0; display:grid;
    gap:10px; max-width:52ch; color:#C9CBCE}
  .est-billet .ex li{padding-left:1.4em; position:relative}
  .est-billet .ex li::before{content:""; position:absolute; left:0; top:.62em;
    width:.5em; height:.5em; border-radius:50%%; background:var(--sec-doux)}

  /* — la barre du bas — */
  .barre{position:fixed; left:0; right:0; bottom:0; height:42px; display:flex;
    align-items:center; gap:14px; padding:0 var(--marge);
    background:rgba(255,255,255,.86); backdrop-filter:blur(8px);
    border-top:1px solid var(--line-100); font-size:13px; color:var(--ink-400)}
  .est-jalon ~ .barre, body.sombre .barre{background:rgba(23,24,26,.8);
    border-top-color:#2A2C2F; color:#9A9DA1}
  .barre button{font:inherit; font-weight:700; color:inherit; background:none;
    border:0; cursor:pointer; padding:6px 8px; border-radius:8px}
  .barre button:hover{background:var(--line-100); color:var(--ink-900)}
  .barre .cpt{margin-left:auto; font-variant-numeric:tabular-nums}
  .jauge{position:fixed; left:0; bottom:42px; height:3px; background:var(--sec);
    transition:width .3s ease; z-index:5}

  /* — notes du présentateur — */
  .panneau{position:fixed; right:0; top:0; bottom:42px; width:min(420px,86vw);
    background:#17181A; color:#E7E8EA; padding:26px 24px; overflow-y:auto;
    transform:translateX(101%%); transition:transform .25s ease; z-index:6;
    font-size:15px; line-height:1.6; border-left:1px solid #2A2C2F}
  body.notes .panneau{transform:none}
  .panneau h3{color:#9A9DA1; font-size:11px; letter-spacing:.12em;
    text-transform:uppercase; margin-bottom:12px}

  /* — sommaire — */
  .som{position:fixed; inset:0; background:rgba(23,24,26,.55); z-index:8;
    display:grid; place-items:center; padding:24px}
  .som[hidden]{display:none}
  .som ol{list-style:none; margin:0; padding:22px; background:#fff;
    border-radius:16px; max-height:80vh; overflow-y:auto; min-width:min(560px,92vw)}
  .som button{display:flex; gap:14px; width:100%%; text-align:left; font:inherit;
    background:none; border:0; padding:9px 12px; border-radius:9px; cursor:pointer}
  .som button:hover{background:var(--paper-50)}
  .som span{color:var(--ink-400); font-variant-numeric:tabular-nums; min-width:2ch}

  /* — à l'impression, tous les écrans se déplient — */
  @media print{
    @page{size:landscape; margin:12mm}
    html,body{height:auto; overflow:visible; background:#fff}
    .barre,.jauge,.panneau,.som{display:none !important}
    .scene{position:static}
    .dia{position:static; opacity:1 !important; visibility:visible !important;
      break-after:page; min-height:auto; padding:0 0 10mm;
      border-bottom:1px solid #DDD; margin-bottom:10mm}
    .dia *{animation:none !important}
    .est-jalon,.est-billet{background:#fff; color:#000}
    .est-jalon h2,.est-billet .grand{color:#000}
    .notes{display:block !important; margin-top:8mm; font-size:10pt; color:#555}
  }
</style>
</head>
<body>
<div class="scene">%(dias)s</div>
<div class="jauge" style="width:0"></div>
<nav class="barre">
  <button id="prec" aria-label="Écran précédent">&#8592;</button>
  <button id="suiv" aria-label="Écran suivant">&#8594;</button>
  <button id="bsom">Sommaire</button>
  <button id="bnotes">Notes</button>
  <button id="bplein">Plein écran</button>
  <span class="cpt"><b id="ici">1</b> / %(n)d &nbsp;·&nbsp; %(code)s</span>
</nav>
<aside class="panneau"><h3>Notes du présentateur</h3><div id="lesnotes"></div></aside>
<div class="som" id="som" hidden><ol>%(sommaire)s</ol></div>
<script>
(function(){
  var dias = [].slice.call(document.querySelectorAll('.dia'));
  var n = dias.length, i = 0;
  var jauge = document.querySelector('.jauge');
  var som = document.getElementById('som');

  function montrer(k){
    i = Math.max(0, Math.min(n - 1, k));
    dias.forEach(function(d, j){
      d.classList.toggle('ici', j === i);
      d.setAttribute('aria-hidden', j === i ? 'false' : 'true');
    });
    document.getElementById('ici').textContent = i + 1;
    jauge.style.width = ((i + 1) / n * 100) + '%%';
    /* Le fond du jalon et du billet est sombre : la barre du bas doit suivre,
       sinon elle reste blanche par-dessus du noir. */
    var d = dias[i];
    document.body.classList.toggle('sombre',
      d.classList.contains('est-jalon') || d.classList.contains('est-billet'));
    var nt = d.querySelector('.notes');
    document.getElementById('lesnotes').innerHTML = nt ? nt.innerHTML : '';
    d.scrollTop = 0;
    try{ history.replaceState(null, '', '#' + (i + 1)); }catch(e){}
  }

  document.getElementById('suiv').onclick = function(){ montrer(i + 1); };
  document.getElementById('prec').onclick = function(){ montrer(i - 1); };
  document.getElementById('bnotes').onclick = function(){
    document.body.classList.toggle('notes'); };
  document.getElementById('bplein').onclick = function(){
    if (document.fullscreenElement) document.exitFullscreen();
    else document.documentElement.requestFullscreen(); };
  document.getElementById('bsom').onclick = function(){ som.hidden = false; };
  som.onclick = function(ev){
    if (ev.target === som) { som.hidden = true; return; }
    var b = ev.target.closest('button[data-va]');
    if (b) { som.hidden = true; montrer(parseInt(b.dataset.va, 10) - 1); }
  };

  document.addEventListener('keydown', function(ev){
    if (ev.metaKey || ev.ctrlKey || ev.altKey) return;
    if (!som.hidden) { if (ev.key === 'Escape') { som.hidden = true; } return; }
    var k = ev.key;
    if (k === 'ArrowRight' || k === 'PageDown' || k === ' ') { ev.preventDefault(); montrer(i + 1); }
    else if (k === 'ArrowLeft' || k === 'PageUp') { ev.preventDefault(); montrer(i - 1); }
    else if (k === 'Home') { ev.preventDefault(); montrer(0); }
    else if (k === 'End') { ev.preventDefault(); montrer(n - 1); }
    else if (k === 'n' || k === 'N') { document.body.classList.toggle('notes'); }
    else if (k === 'f' || k === 'F') { document.getElementById('bplein').click(); }
    else if (k === 's' || k === 'S') { som.hidden = false; }
  });

  var depart = parseInt((location.hash || '').replace('#', ''), 10);
  montrer(isNaN(depart) ? 0 : depart - 1);
})();
</script>
</body>
</html>
"""
