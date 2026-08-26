#!/usr/bin/env python3
"""
Le manuel de l'élève d'un niveau : toutes ses fiches en un seul PDF relié.

    python3 build/manuel_eleve.py 4                      # format atelier
    python3 build/manuel_eleve.py 4 --format condense    # relié, 9,3 pt
    python3 build/manuel_eleve.py 4 --format serre       # relié, 8,6 pt
    python3 build/manuel_eleve.py 4 --ou X.pdf           # ailleurs que par défaut

Pourquoi ce fichier existe
--------------------------
Les fiches de séance existent une par une — `assets/documents/<slug>-<code>-…
.html`, 289 pour le seul niveau 4 — et rien ne les relie. Un élève qui perd sa
feuille n'a pas de recours ; un enseignant qui prend le groupe en cours de
route n'a pas de vue d'ensemble. Ce script en fait **un manuel** : couverture,
mode d'emploi, table des matières paginée, un intercalaire par module, les
fiches dans l'ordre d'enseignement, et les mini-leçons.

Les mini-leçons ne sont pas dans les fiches
-------------------------------------------
54 fiches sur 289 portent un bloc « Ouvrir la mini-leçon » ; les mini-leçons
complètes, elles, vivent dans le module interactif (`PLUS`). Les imprimer était
la moitié de la demande. `build/plus_json.js` les sort des deux origines — le
`plus.js` des modules générés, le `const PLUS` du HTML des neuf modules d'avant
le gabarit — et `mini_lecon_html()` les met en page pour le papier : ce qui
s'écoute à l'écran devient une phrase écrite, ce qui se clique devient un
tableau.

Comment la pagination est juste
-------------------------------
Chaque module est imprimé par Chrome en un PDF à lui, puis les PDF sont
assemblés. Les numéros de page de la table des matières ne sont donc pas
devinés : ils sont **lus dans le PDF produit**. Chaque fiche porte dans son
en-tête un repère blanc d'un point — invisible à l'impression, extractible par
`pypdf` —, ce qui donne la page exacte de chaque séance sans deviner à partir
du texte. La table des matières est composée après, et la couverture n'est
jamais numérotée.

Ce que le manuel ne contient pas
--------------------------------
Ni corrigé, ni notes d'enseignant : c'est le manuel de **l'élève**. Les fiches
sont reprises telles qu'elles sont livrées, sans retouche — une correction se
fait dans le deck de la séance, jamais ici.
"""
import argparse
import datetime
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile

RACINE = pathlib.Path(__file__).resolve().parent.parent
DOCUMENTS = RACINE / 'assets/documents'
PROGRAMME = pathlib.Path.home() / 'Claude/programme/programme-francisation.json'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
from modules import MODULES                                        # noqa: E402

MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
        'août', 'septembre', 'octobre', 'novembre', 'décembre']

# Les blocs d'une séance, dans l'ordre du registre : « a » = Je découvre,
# « e » = Je me lance. Le nom complet vient du registre, bloc par bloc.
NOMS_BLOCS = {'A': 'Je découvre', 'E': 'Je me lance'}

# Trois formats, un seul contenu — rien n'est jamais retiré d'un format à
# l'autre, sauf ce qui n'a de sens que sur une feuille volante : la ligne
# « Nom / Date » de chaque fiche (le manuel en porte une sur sa couverture) et
# le pied de page répété (le folio le remplace).
#
#   · `atelier` — la fiche telle qu'elle est photocopiée, une séance par page.
#   · `condense` — le même texte relié comme un livre : 9,3 pt, blocs
#     resserrés, les séances qui s'enchaînent, les listes courtes sur deux
#     colonnes, les longs exercices autorisés à se couper entre deux pages.
#   · `serre` — le condensé poussé d'un cran : 8,6 pt, marges de 9 mm, lignes
#     à écrire de 5 mm. La moitié des pages du format atelier.
#
# Le corps de 8,6 pt reste lisible mais il est petit : c'est un format de
# consultation, pas la feuille qu'on met devant un élève en classe.
FORMATS = ('atelier', 'condense', 'serre')
FORMAT = 'atelier'


def relie():
    """Vrai dès que le manuel est composé comme un livre."""
    return FORMAT in ('condense', 'serre')


# ───────────────────────────── les fiches ──────────────────────────────

def fiches_du_module(slug):
    """Les fiches de séance, dans l'ordre d'enseignement.

    Le nom d'un fichier est `<slug>-<code>-<titre-en-slug>.html` ; la grille du
    registre donne l'ordre des codes. Ce qui ne porte pas un code de la grille
    — la fiche de jeu de rôle de `module-logement`, par exemple — suit à la
    fin plutôt que d'être écarté en silence.
    """
    grille = MODULES[slug]['seances']
    trouvees, restantes = {}, []
    for f in sorted(DOCUMENTS.glob(slug + '-*.html')):
        if f.name.endswith('-fiches-eleves.html'):
            continue                       # le sommaire, pas une fiche
        m = re.match(re.escape(slug) + r'-([a-e]\d)-', f.name)
        if m and m.group(1) in grille:
            trouvees[m.group(1)] = f
        else:
            restantes.append(f)
    ordre = [(c, trouvees[c]) for c in grille if c in trouvees]
    return ordre + [(None, f) for f in restantes]


# Un défaut des fiches livrées, réparé à l'affichage et signalé plutôt que tu :
# 142 des 289 fiches du niveau 4 portent des `&lt;b&gt;` — du gras écrit par
# l'auteur du deck dans un champ que `fiche.py` échappe. La feuille photocopiée
# montre donc « c'est &lt;b&gt;reconnaître&lt;/b&gt; la forme ». Le manuel remet
# ces trois balises d'aplomb (536 fois pour `b`, 3 pour `u`, 1 pour `s`) ; la
# vraie correction est dans la chaîne des fiches, pas ici.
_BALISES_ECHAPPEES = re.compile(r'&lt;(/?)(b|i|u|s|em|strong|sup|sub)&gt;')


def depiece_fiche(chemin):
    """(code, titre, chapeau, corps HTML) d'une fiche livrée."""
    t = chemin.read_text(encoding='utf-8')
    corps = re.search(r'<body[^>]*>(.*)</body>', t, re.S)
    corps = corps.group(1).strip() if corps else ''
    corps = _BALISES_ECHAPPEES.sub(r'<\1\2>', corps)
    if relie():
        corps = deux_colonnes(corps)
    titre = re.search(r'<h1[^>]*>(.*?)</h1>', t, re.S)
    eye = re.search(r'<div class="eyebrow">(.*?)</div>', t, re.S)
    chap = re.search(r'<p class="chapeau">(.*?)</p>', t, re.S)
    denude = lambda s: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', s or '')).strip()
    return denude(titre and titre.group(1)), denude(eye and eye.group(1)), \
        denude(chap and chap.group(1)), corps


# Deux colonnes quand les items sont courts. Une question de vrai ou faux tient
# en quarante caractères et occupait toute la largeur de la page, sa ligne de
# réponse avec : la moitié droite de la feuille ne portait rien. Le nombre de
# colonnes ne se décide pas en CSS — il faut regarder le texte —, donc il se
# décide ici, liste par liste, et seulement en format condensé.
_LISTE = re.compile(r'<ol class="(ex|obj)">(.*?)</ol>', re.S)
_ITEM = re.compile(r'<li>(.*?)</li>', re.S)
_QUESTION = re.compile(r'<span class="q">(.*?)</span>', re.S)

# Un item qui repasse sur deux lignes dans une demi-colonne occupe la même
# hauteur qu'une ligne pleine largeur : la colonne ne perd donc rien tant que
# l'item ne déborde pas de beaucoup. Le seuil ne protège que contre les phrases
# à rallonge, qui casseraient mal. Mesuré sur les 2 189 listes du niveau 4 :
# 983 tiennent en 45 caractères, 2 018 en 70.
LARGEUR_COLONNE = 80
ITEMS_MINIMUM = 4

# Un bloc ne se coupe jamais entre deux pages — c'est la règle des fiches, et
# elle est juste sur une feuille volante. Dans un manuel, un exercice de dix
# items qui ne tient pas dans le bas d'une page laisse un quart de page blanc,
# et recommence à la page suivante. Au-delà de ce nombre d'items, on autorise
# la coupe : le titre reste attaché à son début (`h2.t{break-after:avoid}`).
ITEMS_SECABLES = 6


def deux_colonnes(corps):
    """Marque les listes assez courtes pour tenir sur deux colonnes."""
    def marque(m):
        classe, dedans = m.group(1), m.group(2)
        items = _ITEM.findall(dedans)
        if len(items) < ITEMS_MINIMUM:
            return m.group(0)
        textes = []
        for item in items:
            q = _QUESTION.search(item)
            textes.append(re.sub(r'\s+', ' ',
                                 re.sub(r'<[^>]+>', '', q.group(1) if q else item)).strip())
        if max((len(t) for t in textes), default=0) > LARGEUR_COLONNE:
            return m.group(0)
        return '<ol class="%s %s--2col">%s</ol>' % (classe, classe, dedans)
    return _SECABLE.sub(secable, _LISTE.sub(marque, corps))


# Le bloc d'un exercice long : on le rend sécable en le marquant à la source,
# faute de pouvoir compter ses items en CSS.
_SECABLE = re.compile(r'<section class="bloc card">(?=(?:(?!</section>).)*?'
                      r'<ol class="ex[ "])((?:(?!</section>).)*?)</section>', re.S)


def secable(m):
    dedans = m.group(1)
    if len(_ITEM.findall(dedans)) < ITEMS_SECABLES:
        return m.group(0)
    return '<section class="bloc card bloc--secable">%s</section>' % dedans


def feuille_des_fiches(slug):
    """La feuille de style commune aux fiches, lue dans l'une d'elles.

    288 des 289 fiches du niveau 4 portent le même `<style>`, à l'octet près :
    c'est `assets/design-system/fiche-imprimee.css`, recopié dans chaque
    document (un `<link>` relatif casserait quand la fiche déménage). On la lit
    donc plutôt que de la recopier une fois de plus ici.
    """
    for _, f in fiches_du_module(slug):
        t = f.read_text(encoding='utf-8')
        st = re.search(r'<style>(.*?)</style>', t, re.S)
        if st and '--paper' in st.group(1):
            return st.group(1)
    raise SystemExit('!! aucune fiche de %s ne porte la feuille commune' % slug)


# ──────────────────────────── les mini-leçons ───────────────────────────

def mini_lecons(slug):
    """Les mini-leçons d'un module, par `build/plus_json.js`."""
    sortie = subprocess.run(['node', str(RACINE / 'build/plus_json.js'), slug],
                            capture_output=True, text=True, cwd=str(RACINE))
    if sortie.returncode != 0:
        print('   ! mini-leçons de %s : %s' % (slug, sortie.stderr.strip()[:120]))
        return {}
    return json.loads(sortie.stdout)


def e(s):
    return html.escape(s or '', quote=False)


def _riche(s):
    """Le HTML permis dans les contenus : gras, italique, exposant, saut."""
    s = html.escape(s or '', quote=False)
    for balise in ('b', 'i', 'em', 'strong', 'sup', 'sub', 'u'):
        s = s.replace('&lt;%s&gt;' % balise, '<%s>' % balise)
        s = s.replace('&lt;/%s&gt;' % balise, '</%s>' % balise)
    s = s.replace('&lt;br&gt;', '<br>').replace('&lt;br/&gt;', '<br>')
    return s


def _accent(s):
    """`{mot}` marque ce que l'écran met en évidence ; le papier le met en gras."""
    return re.sub(r'\{([^}]*)\}', r'<b>\1</b>', _riche(s))


def bloc_html(b):
    """Un bloc de mini-leçon, mis en page pour le papier.

    Les six types viennent de l'écran, où trois d'entre eux s'écoutent ou se
    cliquent. Sur papier : `labo` devient le tableau de ses variantes, `check`
    garde ses questions et range ses réponses en fin de bloc, et tout ce qui
    était un bouton d'écoute redevient la phrase qu'il faisait entendre.
    """
    t = b.get('t')
    h = '<h3>%s</h3>' % _riche(b.get('h')) if b.get('h') else ''
    p = '<p class="mp">%s</p>' % _riche(b.get('p')) if b.get('p') else ''
    note = '<div class="note">%s</div>' % _riche(b.get('note')) if b.get('note') else ''

    if t == 'texte':
        return '<section class="bloc card ml">%s%s%s</section>' % (h, p, note)

    if t == 'ana':
        rangs = ''.join(
            '<tr><td>%s</td><td class="%s">%s</td></tr>'
            % (_riche(m[0]), 'cle' if len(m) > 2 and m[2] else '', _accent(m[1]))
            for m in b.get('mots', []))
        dit = ('<p class="dit"><span class="k">On dit</span> %s</p>'
               % _riche(b['say'])) if b.get('say') else ''
        return ('<section class="bloc card ml">%s%s<table class="ana">%s</table>%s%s</section>'
                % (h, p, rangs, dit, note))

    if t == 'labo':
        axes = b.get('axes', [])
        etiquettes = {}
        for ax in axes:
            for cle, lbl in ax.get('opts', []):
                etiquettes[cle] = lbl
        nu = lambda s: re.sub(r'[^a-zà-ÿ0-9]', '', (s or '').lower())
        rangs = []
        for rang, (cle, sortie) in enumerate((b.get('out') or {}).items(), 1):
            # La clé est la concaténation des options choisies sur chaque axe.
            morceaux = [etiquettes.get(c, c) for c in cle] if len(axes) > 1 \
                else [etiquettes.get(cle, cle)]
            choix = ' + '.join(morceaux)
            # À l'écran, l'option est un bouton et la phrase apparaît en dessous ;
            # sur papier les deux se retrouvent côte à côte, et quand l'option
            # EST la phrase, la colonne la répéterait mot pour mot. On met alors
            # la lettre de l'option — et non un rang inventé : les notes des
            # mini-leçons disent « la phrase c », et cette lettre doit se
            # retrouver dans le tableau.
            if nu(choix) == nu(sortie.get('say', '')):
                choix = '%s.' % cle
            tags = ' · '.join(_accent(w) for w in (sortie.get('w') or []))
            rangs.append('<tr><td class="cle">%s</td><td>%s%s</td><td>%s</td></tr>'
                         % (e(choix), _riche(sortie.get('say', '')),
                            '<span class="tags">%s</span>' % tags if tags else '',
                            _riche(sortie.get('n', ''))))
        titres = ' · '.join(e(a.get('lbl', '')) for a in axes)
        return ('<section class="bloc card ml">%s%s<table class="labo">'
                '<thead><tr><th>%s</th><th>Ce qui se dit</th><th>Ce qu’on observe</th>'
                '</tr></thead><tbody>%s</tbody></table>%s</section>'
                % (h, p, titres or 'Variante', ''.join(rangs), note))

    if t == 'ex':
        rangs = ''.join('<tr><td>%s</td><td>%s</td></tr>'
                        % (_riche(r[0]), _riche(r[1] if len(r) > 1 else ''))
                        for r in b.get('rows', []))
        return ('<section class="bloc card ml">%s%s<table class="ex2">%s</table>'
                '</section>' % (h, p, rangs))

    if t == 'piege':
        cartes = ''.join(
            '<div class="pg"><div class="k">Le piège</div><p class="ph">%s</p>'
            '<div class="k">Ce qui arrive</div><p class="ph">%s</p><p class="px">%s</p></div>'
            % (_riche(r[0]), _riche(r[1] if len(r) > 1 else ''),
               _riche(r[2] if len(r) > 2 else ''))
            for r in b.get('rows', []))
        return '<section class="bloc card ml">%s%s<div class="pieges">%s</div></section>' \
            % (h, p, cartes)

    if t == 'check':
        qs, reps = [], []
        for i, q in enumerate(b.get('qs', []), 1):
            opts = ''.join('<li>%s</li>' % _riche(o) for o in q.get('opts', []))
            qs.append('<li><span class="q">%s</span><ul class="opts">%s</ul></li>'
                      % (_riche(q.get('q', '')), opts))
            bonne = q.get('opts', [])[q.get('ok', 0)] if q.get('opts') else ''
            reps.append('<b>%d.</b> %s%s' % (i, _riche(bonne),
                                             ' — ' + _riche(q['fb']) if q.get('fb') else ''))
        return ('<section class="bloc card ml">%s%s<ol class="check">%s</ol>'
                '<div class="reps"><span class="k">Réponses</span> %s</div></section>'
                % (h, p, ''.join(qs), ' · '.join(reps)))

    return ''


def mini_lecons_html(slug, numero):
    """La section « Mini-leçons » d'un module."""
    plus = mini_lecons(slug)
    if not plus:
        return '', []
    morceaux, repertoire = [], []
    morceaux.append(
        '<article class="fiche intercalaire--doux">'
        '<span class="repere">[[SECTION:%s:plus]]</span>'
        '<div class="eyebrow">Module %d</div><h1 class="tt">Les mini-leçons</h1>'
        '<p class="chapeau">Ce que le module explique à l’écran quand on clique '
        '« Ouvrir la mini-leçon » : la règle, ses cas particuliers, les pièges et '
        'quatre questions pour vérifier qu’on a compris. Rien de tout cela n’est '
        'exigé en classe — c’est là pour la personne qui veut savoir pourquoi.</p>'
        '<ol class="sommaire-ml">%s</ol></article>'
        % (slug, numero,
           ''.join('<li>%s</li>' % e(v.get('tit', '')) for v in plus.values())))
    repertoire.append(('plus', 'Les mini-leçons', 'SECTION:%s:plus' % slug))
    for cle, ml in plus.items():
        blocs = ''.join(bloc_html(b) for b in ml.get('blocs', []))
        morceaux.append(
            '<article class="fiche">'
            '<span class="repere">[[ML:%s:%s]]</span>'
            '<header class="hdr"><div class="hdr-l">'
            '<div class="eyebrow">Mini-leçon · Module %d</div><h1>%s</h1>'
            '</div></header>%s'
            '<footer><span>Mini-leçon · %s</span><span>Manuel de l’élève</span></footer>'
            '</article>'
            % (slug, cle, numero, _riche(ml.get('tit', '')), blocs,
               e(MODULES[slug]['titre'])))
        repertoire.append(('ml', ml.get('tit', ''), 'ML:%s:%s' % (slug, cle)))
    return ''.join(morceaux), repertoire


# ─────────────────────────── le cadre programme ─────────────────────────

def situation_des_modules(niveau):
    """Le libellé de la situation de vie de chaque module, par le tableau du
    prescrit — même rattachement, même table, une seule vérité."""
    try:
        sys.path.insert(0, str(RACINE / 'build'))
        import tableau_programme as tp
        prog = json.loads(PROGRAMME.read_text(encoding='utf-8'))
        niv = next(n for n in prog['niveaux'] if n['niveau'] == niveau)
        table = {}
        for slug, m in MODULES.items():
            if m.get('niveau') == niveau:
                table[slug] = tp.situation_du_module(slug, niv)[0]
        return niv, table
    except Exception as err:
        print('   ! cadre programme indisponible (%s)' % err)
        return None, {}


# ───────────────────────────── la mise en page ──────────────────────────

def part_module(slug, m, situation, feuille):
    """Le HTML d'un module : intercalaire, fiches, mini-leçons."""
    fiches = fiches_du_module(slug)
    lignes, repertoire = [], []

    seances = []
    for code, f in fiches:
        titre, eye, chapeau, corps = depiece_fiche(f)
        seances.append((code, titre))
        repertoire.append(('fiche', '%s · %s' % (code.upper() if code else '—', titre),
                           'FICHE:%s:%s' % (slug, code or f.stem)))
        lignes.append('<article class="fiche"><span class="repere">[[FICHE:%s:%s]]</span>%s</article>'
                      % (slug, code or f.stem, corps))

    blocs = MODULES[slug].get('blocs') or {}
    plan = ''.join('<li><span class="bl">%s</span>%s</li>' % (e(k), e(v))
                   for k, v in sorted(blocs.items()))
    sommaire = ''.join(
        '<li><span class="cd">%s</span>%s</li>'
        % (e(c.upper() if c else '—'), e(t)) for c, t in seances)

    inter = ('<article class="fiche intercalaire">'
             '<span class="repere">[[MODULE:%s]]</span>'
             '<div class="num">Module %d</div><h1 class="tt">%s</h1>'
             '<p class="chapeau">%s</p>'
             '%s'
             '<div class="deux"><div><div class="lbl">Les blocs du module</div>'
             '<ol class="plan">%s</ol></div>'
             '<div><div class="lbl">Les %d séances</div><ol class="som">%s</ol></div></div>'
             '</article>'
             % (slug, m['numero'], e(m['titre']), e(m.get('chapeau', '')),
                ('<div class="prog"><span class="k">Situation de vie du programme</span> %s</div>'
                 % e(situation)) if situation else '',
                plan, len(seances), sommaire))

    ml_html, ml_rep = mini_lecons_html(slug, m['numero'])
    corps = inter + ''.join(lignes) + ml_html
    repertoire = [('module', 'Module %d · %s' % (m['numero'], m['titre']),
                   'MODULE:%s' % slug)] + repertoire + ml_rep
    return page_html('Module %d — %s' % (m['numero'], m['titre']), corps, feuille), repertoire


def page_html(titre, corps, feuille):
    supplement = SUPPLEMENT
    if relie():
        supplement += CONDENSATION
    if FORMAT == 'serre':
        supplement += SERRAGE
    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>
%s
%s
</style>
</head>
<body>
%s
</body>
</html>
""" % (e(titre), feuille, supplement, corps)


# La feuille des fiches est reprise telle quelle ; ce qui suit n'ajoute que ce
# qu'un manuel demande et qu'une fiche isolée n'a pas : la coupe de page entre
# deux fiches, les intercalaires, la couverture, la table des matières et la
# mise en page des mini-leçons. Aucune couleur : le manuel se photocopie.
SUPPLEMENT = """
/* ── le manuel ── */
body{width:215.9mm; margin:0 auto; padding:0}
.fiche{padding:14mm 15mm 16mm; break-after:page; page-break-after:always}
.fiche:last-child{break-after:auto; page-break-after:auto}
.repere{font-size:1pt; color:#FFFFFF; line-height:0}
@media print{ body{width:auto} .fiche{padding:0} }

/* ── couverture ── */
.couv{display:flex; flex-direction:column; min-height:245mm; padding-top:26mm}
.couv .pilule{display:inline-flex; align-items:center; justify-content:center;
  border:3px solid var(--rule); border-radius:999px; padding:7px 22px;
  font-size:26pt; font-weight:900; letter-spacing:.02em; color:var(--ink)}
.couv .desc{margin-top:9px; font-size:11pt; font-weight:800; color:var(--muted);
  text-transform:uppercase; letter-spacing:.1em}
.couv h1{font-size:44pt; font-weight:900; line-height:1.02; margin-top:32mm;
  letter-spacing:-0.02em}
.couv .niv{font-size:20pt; font-weight:800; color:var(--soft); margin-top:10px}
.couv .code{font-size:11pt; font-weight:800; color:var(--muted); margin-top:6px;
  text-transform:uppercase; letter-spacing:.1em}
.couv .compte{margin-top:auto; border-top:2.5px solid var(--rule); padding-top:10px;
  display:flex; gap:18px; flex-wrap:wrap; font-size:11pt; font-weight:800; color:var(--ink)}
.couv .compte span{white-space:nowrap}
.couv .pied{margin-top:12px; font-size:10pt; font-weight:600; color:var(--muted)}
.couv .nomcarte{margin-top:18mm; border:2.5px solid var(--rule); border-radius:12px;
  padding:12px 16px; font-size:12pt; font-weight:800; color:var(--ink)}
.couv .nomcarte .nomline{width:70mm}

/* ── intercalaire de module ── */
.intercalaire{display:flex; flex-direction:column}
.intercalaire .num{font-size:11pt; font-weight:800; text-transform:uppercase;
  letter-spacing:.14em; color:var(--muted)}
.intercalaire h1.tt, .intercalaire--doux h1.tt{font-size:34pt; font-weight:900;
  line-height:1.05; margin:6px 0 10px; letter-spacing:-0.02em}
.intercalaire .prog{border-left:3px solid var(--rule); padding:6px 0 6px 12px;
  margin:14px 0 6px; font-weight:700; color:var(--ink)}
.intercalaire .prog .k, .reps .k, .dit .k{display:block; font-size:9.5pt; font-weight:800;
  text-transform:uppercase; letter-spacing:.12em; color:var(--muted)}
.deux{display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-top:16px}
ol.plan, ol.som, ol.sommaire-ml{list-style:none; font-weight:600}
ol.plan li, ol.som li{margin-bottom:5px; display:flex; gap:8px; align-items:baseline}
ol.plan .bl, ol.som .cd{flex:0 0 12mm; font-weight:900; color:var(--ink);
  font-size:10pt; letter-spacing:.06em}
.intercalaire--doux{padding-top:26mm}
ol.sommaire-ml{margin-top:14px; columns:2; column-gap:16px}
ol.sommaire-ml li{margin-bottom:6px; break-inside:avoid; font-weight:700; color:var(--ink)}
ol.sommaire-ml li::before{content:"· "; color:var(--muted)}

/* ── table des matières ── */
.tdm h1{font-size:30pt; font-weight:900; margin-bottom:4px}
.tdm .intro{font-size:11pt; font-weight:600; color:var(--soft); margin-bottom:14px}
.tdm .cols{columns:2; column-gap:14px}
.tdm .mod{margin-top:11px; break-inside:avoid; page-break-inside:avoid}
.tdm .mod:first-child{margin-top:0}
.tdm .mod-t{display:flex; align-items:baseline; gap:8px; border-bottom:1.5px solid var(--rule);
  padding-bottom:3px; font-size:12.5pt; font-weight:900; color:var(--ink)}
.tdm .mod-t{flex-wrap:nowrap}
.tdm .mod-t .n{flex:0 0 auto; white-space:nowrap; font-size:10pt; letter-spacing:.06em;
  color:var(--muted); text-transform:uppercase}
.tdm .mod-t>span:nth-child(2){flex:1}
.tdm .mod-t .p{margin-left:auto; font-variant-numeric:tabular-nums}
.tdm ol{list-style:none; margin-top:4px}
.tdm ol li{display:flex; align-items:baseline; gap:8px; font-size:10.5pt; font-weight:600;
  color:var(--body); padding:1.5px 0}
.tdm ol li .c{flex:0 0 16mm; font-weight:900; color:var(--ink); font-size:9.5pt;
  letter-spacing:.06em}
.tdm ol li .f{flex:1; border-bottom:1px dotted var(--line); margin:0 4px 3px}
.tdm ol li .p{font-variant-numeric:tabular-nums; font-weight:800; color:var(--ink)}
.tdm li.ml{color:var(--soft)}
.tdm li.ml .c::before{content:'·'; color:var(--muted)}

/* ── mode d'emploi ── */
.mode h1{font-size:30pt; font-weight:900; margin-bottom:10px}
.mode .card{margin-bottom:10px}
.mode .card h3{font-size:12.5pt; font-weight:900; color:var(--ink); margin-bottom:3px}

/* ── mini-leçons ── */
.ml h3{font-size:13pt; font-weight:900; color:var(--ink); margin-bottom:5px}
.ml p.mp{font-weight:600; margin-bottom:7px}
table.ana td, table.ex2 td, table.labo td{padding:5px 8px 5px 0;
  border-top:1px solid var(--line); vertical-align:top; font-weight:600}
table.ana td:first-child, table.ex2 td:nth-child(2), table.labo td:first-child{
  color:var(--muted); font-size:10pt; font-weight:800}
table.ana td.cle{font-weight:900; color:var(--ink)}
table.labo th{font-size:9pt}
.tags{display:block; font-size:10pt; font-weight:800; color:var(--muted); margin-top:2px}
.dit{margin-top:8px; background:var(--tint); border-radius:9px; padding:7px 11px;
  font-weight:700; color:var(--ink)}
.pieges{display:grid; grid-template-columns:1fr 1fr 1fr; gap:9px}
.pg{border:1.5px dashed var(--muted); border-radius:12px; padding:9px 11px}
.pg .k{font-size:9pt; font-weight:800; text-transform:uppercase; letter-spacing:.1em;
  color:var(--muted); margin-top:5px}
.pg .k:first-child{margin-top:0}
.pg .ph{font-weight:800; color:var(--ink); font-size:10.5pt}
.pg .px{margin-top:6px; font-weight:600; font-size:10pt; color:var(--soft)}
ol.check{list-style:none; counter-reset:c}
ol.check li{counter-increment:c; position:relative; padding-left:9mm; margin-bottom:8px;
  break-inside:avoid}
ol.check li::before{content:counter(c); position:absolute; left:0; top:0; width:6mm;
  height:6mm; border-radius:50%; border:1.5px solid var(--rule); font-size:9.5pt;
  font-weight:800; color:var(--ink); display:flex; align-items:center; justify-content:center}
ol.check .q{font-weight:800; color:var(--ink)}
ul.opts{list-style:none; margin-top:3px; display:flex; gap:10px; flex-wrap:wrap}
ul.opts li{font-weight:600; border:1px solid var(--line); border-radius:999px;
  padding:2px 11px; font-size:10.5pt}
.reps{margin-top:8px; border-top:1px solid var(--line); padding-top:6px;
  font-size:10pt; font-weight:600; color:var(--soft)}
"""


CONDENSATION = """
/* ── format condensé : le même texte, relié comme un livre ── */
@page{margin:11mm 12mm}
body{font-size:9.3pt; line-height:1.36}
.fiche{padding:11mm 12mm; break-after:auto; page-break-after:auto}
.fiche + .fiche{border-top:2.5px solid var(--rule); margin-top:10px; padding-top:10px}
.intercalaire, .intercalaire--doux, .couv, .mode, .tdm{break-before:page; page-break-before:always}
.couv{break-before:auto; page-break-before:auto}
@media print{ .fiche{padding:0} .fiche + .fiche{padding-top:8px} }

/* La feuille volante demandait un nom : le manuel le porte sur sa couverture.
   Le pied de fiche répétait le titre du module à chaque séance : le folio et
   l'en-tête de la séance disent déjà où l'on est. */
.hdr-r, .fiche > footer{display:none}

.hdr{padding-bottom:5px; margin-bottom:8px; border-bottom-width:2px}
.hdr h1{font-size:15pt}
.chapeau{font-size:10pt; margin-bottom:9px}
.bloc{margin-bottom:7px}
.card, .regle, .billet{padding:7px 10px 8px}
.lbl{font-size:8.5pt; margin-bottom:3px}
h2.t{font-size:11.5pt; margin-bottom:4px}
.consigne{font-size:9.3pt; margin-bottom:5px}
ol.obj li{margin-bottom:3px} ol.ex li{margin-bottom:5px}
ol.ex--2col, ol.obj--2col{columns:2; column-gap:10mm}
ol.ex--2col li, ol.obj--2col li{break-inside:avoid; page-break-inside:avoid}
/* Une ligne de réponse en demi-largeur reste une ligne de réponse : c'est le
   blanc à droite d'une question de six mots qui disparaît, pas la place où
   l'élève écrit. */
ol.ex--2col .ligne--court{width:80%}
.bloc--secable{break-inside:auto; page-break-inside:auto}
.bloc--secable h2.t, .bloc--secable .lbl, .bloc--secable .consigne{
  break-after:avoid; page-break-after:avoid}
ol.obj li, ol.ex li{padding-left:7mm}
ol.obj li::before, ol.ex li::before{width:5mm; height:5mm; font-size:8pt}
.ligne{height:6mm}
table td, .voc td{padding:3.5px 8px 3.5px 0}
th{padding-bottom:3px; font-size:8.5pt}
.note{margin-top:5px; padding:6px 9px; font-size:9pt}
.duo>div{padding:7px 10px} .duo p.ph{font-size:10.5pt}
.regle p.r{font-size:11.5pt} .billet p.c{font-size:11.5pt}
.grid{gap:6px} .grid .card h3{font-size:10pt} .grid .card p{font-size:9.3pt}

/* mini-leçons */
.ml h3{font-size:11pt; margin-bottom:3px}
.ml p.mp{margin-bottom:5px}
.pieges{gap:6px} .pg{padding:7px 9px} .pg .ph{font-size:9.5pt}
.dit{padding:5px 9px; margin-top:5px}
ol.check li{margin-bottom:5px; padding-left:7mm}
ol.check li::before{width:5mm; height:5mm; font-size:8pt}
.reps{font-size:9pt; padding-top:4px}

/* intercalaire : un bandeau en tête de module, plus une page à lui tout seul */
.intercalaire{padding-top:11mm}
.intercalaire h1.tt, .intercalaire--doux h1.tt{font-size:24pt}
.deux{gap:12px; margin-top:11px}
ol.plan li, ol.som li{margin-bottom:3px}
.intercalaire--doux{padding-top:11mm}
ol.sommaire-ml{columns:3}

/* table des matières */
.tdm .cols{columns:3; column-gap:12px}
.tdm h1{font-size:22pt} .tdm .intro{font-size:9.5pt; margin-bottom:10px}
.tdm .mod-t{font-size:10.5pt} .tdm ol li{font-size:9pt; padding:0.5px 0}
"""


# Le cran de plus. Mesuré sur `module-consultation` : 58 pages en condensé,
# 51 en serré. Ce qui reste hors de cette feuille — deux colonnes, blocs
# sécables — appartient au condensé et vaut pour les deux.
SERRAGE = """
/* ── format serré ── */
@page{margin:9mm 10mm}
body{font-size:8.6pt; line-height:1.3}
.fiche{padding:9mm 10mm}
@media print{ .fiche{padding:0} }
.card, .regle, .billet{padding:5px 8px 6px}
.bloc{margin-bottom:5px}
.ligne{height:5mm}
h2.t{font-size:10.5pt; margin-bottom:3px}
.hdr{padding-bottom:4px; margin-bottom:6px}
.chapeau{font-size:9.4pt; margin-bottom:7px}
"""


def couverture_html(niv, niveau, compte, feuille, date_fr):
    titre_niv = e(niv['titre']) if niv else ''
    code = ('%s · stade %s' % (niv['code'], niv['stade'])) if niv else ''
    corps = """
<article class="fiche couv"><span class="repere">[[COUV]]</span>
  <div><span class="pilule">SAAF</span>
  <div class="desc">Système d’aide à l’apprentissage du français</div></div>
  <h1>Manuel<br>de l’élève</h1>
  <div class="niv">Niveau %d — %s</div>
  <div class="code">%s</div>
  <div class="nomcarte">Ce manuel appartient à<span class="nomline nomline--nom"></span></div>
  <div class="compte">
    <span>%d modules</span><span>%d séances</span><span>%d mini-leçons</span>
  </div>
  <p class="pied">Francisation · Programme d’études Francisation (ministère de
  l’Éducation du Québec, 2015). Édition du %s.</p>
</article>
<article class="fiche mode"><span class="repere">[[MODE]]</span>
  <h1>Comment se servir de ce manuel</h1>
  <p class="chapeau">Tout ce que le cours donne sur papier, dans l’ordre où on
  le voit en classe. Rien n’oblige à le lire seul : c’est un manuel de cours,
  pas un livre d’exercices à faire chez soi.</p>
  <section class="bloc card"><h3>Un module par intercalaire</h3>
  <p>Chaque module s’ouvre sur une page qui dit son titre, ce qu’on y apprend,
  la situation de vie du programme dont il vient, et la liste de ses séances.
  Les séances portent un code — A1, B3, E2 — qui est aussi celui qu’annonce
  l’enseignante.</p></section>
  <section class="bloc card"><h3>Une fiche par séance</h3>
  <p>La fiche porte les objectifs, les explications, les tableaux et les
  exercices de la séance, avec les lignes pour écrire. C’est la même feuille
  que celle distribuée en classe : celui qui perd la sienne la retrouve ici.</p></section>
  <section class="bloc card"><h3>Les mini-leçons, à la fin de chaque module</h3>
  <p>Ce sont les explications que le module donne à l’écran quand on clique
  « Ouvrir la mini-leçon » : la règle, ses cas particuliers, les pièges les plus
  fréquents et quatre questions pour vérifier. Les réponses sont écrites juste
  en dessous. Personne n’est obligé de les lire ; elles sont là pour qui veut
  comprendre pourquoi.</p></section>
  <section class="bloc card"><h3>Ce qui n’est pas ici</h3>
  <p>L’audio, la correction automatique et le jeu de rôle vivent dans le module
  en ligne : le papier ne peut pas les porter. Le corrigé des exercices n’y est
  pas non plus — il appartient à l’enseignante.</p></section>
</article>""" % (niveau, titre_niv, code, compte['modules'], compte['seances'],
                 compte['mini'], date_fr)
    return page_html('Manuel de l’élève — Niveau %d' % niveau, corps, feuille)


def tdm_html(niveau, entrees, feuille):
    """La table des matières, une fois les pages connues."""
    morceaux = []
    for mod in entrees:
        lignes = ''.join(
            '<li class="%s"><span class="c">%s</span><span class="t">%s</span>'
            '<span class="f"></span><span class="p">%s</span></li>'
            % (cls, e(code), e(titre), page)
            for cls, code, titre, page in mod['lignes'])
        morceaux.append(
            '<div class="mod"><div class="mod-t"><span class="n">Module %d</span>'
            '<span>%s</span><span class="p">%s</span></div><ol>%s</ol></div>'
            % (mod['numero'], e(mod['titre']), mod['page'], lignes))
    corps = ('<article class="fiche tdm"><span class="repere">[[TDM]]</span>'
             '<h1>Table des matières</h1>'
             '<p class="intro">Les modules dans l’ordre d’enseignement. Sous chacun, '
             'ses séances par leur code, puis ses mini-leçons.</p>'
             '<div class="cols">%s</div></article>'
             % ''.join(morceaux))
    return page_html('Table des matières', corps, feuille)


# ────────────────────────────── l'impression ────────────────────────────

def imprimer(html_source, pdf_cible):
    """Chrome sans interface, comme `programme/outils/fiche_pdf.py`.

    Le format ne se règle pas en ligne de commande : c'est la règle `@page` de
    la feuille des fiches qui décide, et elle dit lettre.
    """
    cmd = [CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer',
           '--run-all-compositor-stages-before-draw', '--virtual-time-budget=20000',
           '--print-to-pdf=%s' % pdf_cible, pathlib.Path(html_source).as_uri()]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    if not pathlib.Path(pdf_cible).exists():
        raise SystemExit('!! Chrome n’a produit aucun PDF.\n' + (p.stderr or '')[:600])
    return pathlib.Path(pdf_cible)


def cle_repere(r):
    """La forme d'un repère qui survit à l'extraction de texte.

    `pypdf` rend « MODULE:module-restaurant » en « MODULE:modulerestaurant » :
    le trait d'union tombe. Plutôt que de bricoler le repère pour lui plaire, on
    compare les deux côtés réduits à leurs lettres et à leurs chiffres.
    """
    return re.sub(r'[^A-Za-z0-9]', '', r or '')


def pages_des_reperes(pdf):
    """{repère réduit: numéro de page (0 = première)} — lu dans le PDF produit."""
    from pypdf import PdfReader
    trouve = {}
    for i, page in enumerate(PdfReader(str(pdf)).pages):
        for r in re.findall(r'\[\[([^\]]+)\]\]', page.extract_text() or ''):
            trouve.setdefault(cle_repere(r), i)
    return trouve


def poser_folios(writer, premier_numerote, depart=1):
    """Écrit le numéro de page au bas de chaque page, en Helvetica du lecteur.

    Deux voies étaient possibles et une seule tient à cette échelle. Superposer
    un PDF de folios produit par Chrome — comme le fait la chaîne des séances —
    duplique la police du folio **sur chacune des 1 763 pages** : le manuel
    passait ainsi de 30 à 172 Mo. On écrit donc le numéro directement dans le
    flux de la page, avec l'une des quatorze polices que tout lecteur PDF porte
    déjà : rien à incorporer, une centaine d'octets par page.

    Les pages liminaires — couverture, mode d'emploi, table des matières — ne
    sont pas numérotées : `premier_numerote` dit où commence le folio 1.
    """
    from pypdf.generic import (ArrayObject, DecodedStreamObject, DictionaryObject,
                               NameObject)
    police = writer._add_object(DictionaryObject({
        NameObject('/Type'): NameObject('/Font'),
        NameObject('/Subtype'): NameObject('/Type1'),
        NameObject('/BaseFont'): NameObject('/Helvetica-Bold'),
    }))
    for i, page in enumerate(writer.pages):
        n = i - premier_numerote + depart
        if n < depart:
            continue
        texte = str(n)
        # Helvetica-Bold : un chiffre fait 556 millièmes de cadratin.
        largeur = len(texte) * 0.556 * 9
        boite = page.mediabox
        x = (float(boite.width) - largeur) / 2
        flux = DecodedStreamObject()
        flux.set_data(('Q q 0.37 0.38 0.40 rg BT /FolioSAAF 9 Tf 1 0 0 1 %.1f 24 Tm '
                       '(%s) Tj ET Q' % (x, texte)).encode('latin-1'))
        ouvre = DecodedStreamObject()
        ouvre.set_data(b'q')                    # le contenu d'origine reste isolé
        ressources = page.get('/Resources')
        if ressources is None:
            ressources = DictionaryObject()
            page[NameObject('/Resources')] = ressources
        polices = ressources.get('/Font')
        if polices is None:
            polices = DictionaryObject()
            ressources[NameObject('/Font')] = polices
        polices[NameObject('/FolioSAAF')] = police
        contenu = page.get('/Contents')
        anciens = list(contenu) if isinstance(contenu, ArrayObject) else [contenu]
        page[NameObject('/Contents')] = ArrayObject(
            [writer._add_object(ouvre)] + anciens + [writer._add_object(flux)])


def assembler(parties, sortie, plan):
    """Les parties bout à bout, les folios posés, les signets écrits.

    `append()` et non une boucle de `add_page()` : celle-ci recopie les
    ressources de chaque page — la police Nunito des fiches se retrouvait
    incorporée mille sept cent soixante-trois fois.
    """
    from pypdf import PdfWriter
    w = PdfWriter()
    for p in parties:
        w.append(str(p))
    poser_folios(w, plan['premier_numerote'])
    parents = {}
    for niveau, titre, page in plan['signets']:
        if niveau == 0:
            parents[0] = w.add_outline_item(titre, page)
        else:
            w.add_outline_item(titre, page, parent=parents.get(0))
    with open(sortie, 'wb') as f:
        w.write(f)
    return sortie


# ──────────────────────────────── le manuel ─────────────────────────────

def construire(niveau, sortie, garder_html=False):
    aujourdhui = datetime.date.today()
    date_fr = '%d %s %d' % (aujourdhui.day, MOIS[aujourdhui.month - 1], aujourdhui.year)

    liste = sorted(((m['numero'], s, m) for s, m in MODULES.items()
                    if m.get('niveau') == niveau))
    if not liste:
        raise SystemExit('!! aucun module de niveau %d dans le registre' % niveau)
    feuille = feuille_des_fiches(liste[0][1])
    niv, situations = situation_des_modules(niveau)

    travail = pathlib.Path(tempfile.mkdtemp(prefix='manuel-n%d-' % niveau))
    print('· atelier : %s' % travail)

    parties, repertoires = [], []
    for numero, slug, m in liste:
        html_mod, repertoire = part_module(slug, m, situations.get(slug), feuille)
        src = travail / ('%02d-%s.html' % (numero, slug))
        src.write_text(html_mod, encoding='utf-8')
        pdf = imprimer(src, travail / ('%02d-%s.pdf' % (numero, slug)))
        reperes = pages_des_reperes(pdf)
        from pypdf import PdfReader
        n = len(PdfReader(str(pdf)).pages)
        parties.append({'slug': slug, 'numero': numero, 'titre': m['titre'],
                        'pdf': pdf, 'pages': n, 'reperes': reperes,
                        'repertoire': repertoire})
        print('  %2d. %-24s %3d pages · %d repères' % (numero, slug, n, len(reperes)))
        repertoires.append(repertoire)

    compte = {'modules': len(parties),
              'seances': sum(1 for r in repertoires for t, _, _ in r if t == 'fiche'),
              'mini': sum(1 for r in repertoires for t, _, _ in r if t == 'ml')}

    src_couv = travail / 'couverture.html'
    src_couv.write_text(couverture_html(niv, niveau, compte, feuille, date_fr),
                        encoding='utf-8')
    couv = imprimer(src_couv, travail / 'couverture.pdf')
    from pypdf import PdfReader
    n_couv = len(PdfReader(str(couv)).pages)

    # La table des matières est composée deux fois : sa propre longueur décale
    # tout ce qui la suit, et la deuxième passe part de la longueur mesurée.
    n_tdm, tdm_pdf, entrees = 1, None, None
    for passe in range(4):
        depart = n_couv + n_tdm                      # première page numérotée = 1
        entrees, courant = [], depart
        for part in parties:
            base = courant
            lignes = []
            for genre, titre, repere in part['repertoire']:
                page = part['reperes'].get(cle_repere(repere))
                folio = (base + page) - depart + 1 if page is not None else ''
                if genre == 'module':
                    page_module = folio
                elif genre == 'fiche':
                    code, _, t = titre.partition(' · ')
                    lignes.append(('', code, t, folio))
                elif genre == 'plus':
                    lignes.append(('ml', '', 'Les mini-leçons', folio))
                elif genre == 'ml':
                    lignes.append(('ml', '', titre, folio))
            entrees.append({'numero': part['numero'], 'titre': part['titre'],
                            'page': page_module, 'lignes': lignes})
            courant += part['pages']
        src = travail / 'tdm.html'
        src.write_text(tdm_html(niveau, entrees, feuille), encoding='utf-8')
        tdm_pdf = imprimer(src, travail / 'tdm.pdf')
        mesure = len(PdfReader(str(tdm_pdf)).pages)
        if mesure == n_tdm:
            break
        n_tdm = mesure
    print('· table des matières : %d pages (passe %d)' % (n_tdm, passe + 1))

    total = n_couv + n_tdm + sum(p['pages'] for p in parties)

    signets = [(0, 'Couverture', 0), (0, 'Table des matières', n_couv)]
    curseur = n_couv + n_tdm
    for part in parties:
        signets.append((0, 'Module %d · %s' % (part['numero'], part['titre']), curseur))
        for genre, titre, repere in part['repertoire']:
            page = part['reperes'].get(cle_repere(repere))
            if page is None or genre == 'module':
                continue
            signets.append((1, titre, curseur + page))
        curseur += part['pages']

    plan = {'premier_numerote': n_couv + n_tdm, 'signets': signets}
    assembler([couv, tdm_pdf] + [p['pdf'] for p in parties], sortie, plan)

    manquants = sum(1 for p in parties for g, _, r in p['repertoire']
                    if cle_repere(r) not in p['reperes'])
    print('✓ %s — %d pages, %d modules, %d séances, %d mini-leçons'
          % (sortie, total, compte['modules'], compte['seances'], compte['mini']))
    if manquants:
        print('  ! %d repères introuvables dans le PDF : ces lignes de la table '
              'des matières sortent sans numéro de page.' % manquants)
    if garder_html:
        print('  HTML de travail conservé : %s' % travail)
    return sortie


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('niveau', type=int, nargs='?', default=4)
    ap.add_argument('--ou', default=None, help='fichier PDF de sortie')
    ap.add_argument('--format', choices=FORMATS, default='atelier',
                    help='atelier (défaut) · condense · serre')
    ap.add_argument('--html', action='store_true',
                    help='garder le HTML de travail (débogage)')
    args = ap.parse_args()
    if not pathlib.Path(CHROME).exists():
        raise SystemExit('!! Chrome est introuvable : %s' % CHROME)
    global FORMAT
    FORMAT = args.format
    suffixe = '' if args.format == 'atelier' else '-' + args.format
    sortie = pathlib.Path(args.ou) if args.ou else DOCUMENTS / (
        'manuel-eleve-niveau-%d%s.pdf' % (args.niveau, suffixe))
    construire(args.niveau, sortie, garder_html=args.html)
    return 0


if __name__ == '__main__':
    sys.exit(main())
