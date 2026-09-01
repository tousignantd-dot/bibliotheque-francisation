#!/usr/bin/env python3
"""
Le tableau du prescrit : ce que le programme demande, module par module.

    python3 build/tableau_programme.py          # écrit la page
    python3 build/tableau_programme.py --ou X   # ailleurs que par défaut

Pourquoi ce fichier existe
--------------------------
La question « qu'est-ce qu'il y a dans ce module, au juste — quels savoirs,
quels temps de verbes ? » se répondait jusqu'ici en rouvrant le manifeste du
module, puis `build/cadre.py`, puis le JSON du programme. Trois sources, trois
fenêtres, et rien à montrer à quelqu'un d'autre.

Cette page les met côte à côte, une ligne par module :

  · l'identité du module vient du registre `build/powerpoints/modules.py` —
    la colonne « N° » est le rang du module **dans son niveau** (`numero`), qui
    est aussi l'ordre d'enseignement ; le numéro d'activité du dépôt de
    matériel (`activite`), lui, est écrit sous le slug ;
  · la situation de vie vient du `theme` de son manifeste (les neuf modules
    d'avant le gabarit n'en ont pas : ils sont rattachés à la main, comme dans
    `build/bilan_programme.py`, dont la table est réutilisée telle quelle) ;
  · les intentions de communication, le lexique thématique, les savoirs, les
    attentes de fin de cours et les critères d'évaluation viennent du
    dépouillement `~/Claude/programme/programme-francisation.json`.

Ce que la page ne prétend pas être
----------------------------------
Les **savoirs du programme sont prescrits par niveau, pas par situation** : le
programme ne dit nulle part que tel module doit travailler le
plus-que-parfait. Ils sont donc affichés une fois par niveau, et la ligne d'un
module renvoie à ceux de son niveau — c'est exactement ce que dit le
programme, ni plus ni moins. Ce qu'un module a réellement retenu de ces
savoirs, et pourquoi, est écrit dans la **note de cadrage** de son manifeste :
elle est reprise en entier dans le détail de la ligne, repliée.

La page est **générée**. La retoucher à la main serait perdu à la prochaine
construction — voir la règle « les modules sont générés ».
"""
import argparse
import ast
import datetime
import html
import importlib.util
import json
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PROGRAMME = pathlib.Path.home() / 'Claude/programme/programme-francisation.json'
SORTIE = RACINE / 'assets/presentations/tableau-programme.html'

sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
sys.path.insert(0, str(RACINE / 'build'))
from modules import MODULES                                       # noqa: E402
from bilan_programme import RATTACHEMENTS, norme                  # noqa: E402

# La couleur d'un module est celle de son niveau — mêmes paires que
# `assets/design-system/tokens/colors.css`, lues plutôt que recopiées.
CSS_COULEURS = RACINE / 'assets/design-system/tokens/colors.css'

# Le lexique vient d'un autre document que le programme et nomme parfois les
# situations autrement (même table que `build/cadre.py`).
ALIAS_LEXIQUE = {
    'Consultation médicale': 'Consultation d’un professionnel de la santé',
    'Orientation dans l’établissement (de formation)':
        'Communication avec le personnel de l’établissement',
}
_PAS_DU_VOCABULAIRE = re.compile(
    r'^\s*[•·]|Orthographier|Reconnaître tous les caractères|'
    r'Connaître les termes qui servent')

# Ce qui, dans la hiérarchie des savoirs, désigne un temps ou un mode du
# verbe. Le programme les range tous sous « Verbes et GV ».
_TEMPS = re.compile(r'^(Indicatif|Subjonctif|Impératif|Infinitif|Participe|'
                    r'Conditionnel)\b')

NOMS_COMP = {'co': 'Compréhension orale', 'po': 'Production orale',
             'ce': 'Compréhension écrite', 'pe': 'Production écrite'}


def couleurs():
    css = CSS_COULEURS.read_text(encoding='utf-8')
    paires = {}
    for n in range(1, 9):
        line = re.search(r'--niv-%d-line:\s*(#[0-9A-Fa-f]{6})' % n, css)
        bg = re.search(r'--niv-%d-bg:\s*(#[0-9A-Fa-f]{6})' % n, css)
        paires[n] = (line.group(1), bg.group(1))
    return paires


def manifeste(slug):
    """Le thème et la note de cadrage d'un module généré, ou (None, None)."""
    f = RACINE / 'build' / 'contenu' / slug / 'manifest.py'
    if not f.exists():
        return None, None
    source = f.read_text(encoding='utf-8')
    note = ast.get_docstring(ast.parse(source))
    spec = importlib.util.spec_from_file_location('mf_' + slug.replace('-', '_'), f)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
        theme = mod.MANIFESTE.get('theme')
    except Exception:
        theme = None
    if theme:
        theme = theme.replace("\\'", "'")
    return theme, note


def lexique_par_situation(niv):
    """Le lexique rangé par situation, règle de continuation appliquée."""
    par_situation, courante = {}, None
    for bloc in niv.get('lexique', []):
        brute = bloc.get('situation')
        rattachee = brute is None
        if brute:
            courante = ALIAS_LEXIQUE.get(brute, brute)
        if courante is None:
            continue
        for entree in bloc.get('entrees', []):
            if not _PAS_DU_VOCABULAIRE.search(entree):
                par_situation.setdefault(courante, []).append((entree, rattachee))
    return par_situation


def situation_du_module(slug, niv):
    """Le libellé exact du programme, ou None si le rattachement échoue."""
    theme, note = manifeste(slug)
    libelle = RATTACHEMENTS.get(slug) or theme
    if not libelle:
        return None, note
    table = {norme(s): s for s in niv['situations']}
    return table.get(norme(libelle)), note


# ─────────────────────────────── rendu ────────────────────────────────

def e(s):
    return html.escape(s or '', quote=True)


def puces(items, classe='liste-points'):
    if not items:
        return ''
    return ('<ul class="%s">' % classe
            + ''.join('<li>%s</li>' % e(x) for x in items) + '</ul>')


def note_html(note):
    """La note de cadrage du manifeste, en paragraphes.

    Ce sont des docstrings écrites à la main : titres soulignés par des tirets,
    listes à puces « · », paragraphes séparés par une ligne vide. On garde ces
    trois-là et rien de plus — reformater davantage trahirait le texte.
    """
    if not note:
        return '<p class="rien">Ce module est d’avant le gabarit : il n’a pas de note de cadrage.</p>'
    blocs, out = re.split(r'\n\s*\n', note.strip()), []
    for bloc in blocs:
        lignes = [l.rstrip() for l in bloc.split('\n')]
        # Titre souligné par une ligne de tirets ou d'égales.
        if len(lignes) >= 2 and re.fullmatch(r'[-=]{3,}', lignes[1].strip()):
            out.append('<h5>%s</h5>' % e(lignes[0].strip()))
            reste = '\n'.join(lignes[2:]).strip()
            if reste:
                blocs.append(reste)
            continue
        if lignes and re.match(r'\s*[·•]\s', lignes[0]):
            items, courant = [], ''
            for l in lignes:
                if re.match(r'\s*[·•]\s', l):
                    if courant:
                        items.append(courant)
                    courant = re.sub(r'^\s*[·•]\s*', '', l)
                else:
                    courant += ' ' + l.strip()
            if courant:
                items.append(courant)
            out.append(puces(items, 'liste-note'))
            continue
        out.append('<p>%s</p>' % e(' '.join(l.strip() for l in lignes)))
    return ''.join(out)


def bloc_savoirs(niv):
    """Les savoirs du niveau, par catégorie, repliés."""
    noms_cat = {'texte': 'Grammaire du texte', 'phrase': 'Grammaire de la phrase',
                'phonetique': 'Éléments de phonétique', 'lexique': 'Lexique'}
    par_cat = {}
    for s in niv['savoirs']:
        par_cat.setdefault(s['categorie'], []).append(s)
    out = []
    for cid in ('texte', 'phrase', 'phonetique', 'lexique'):
        liste = par_cat.get(cid)
        if not liste:
            continue
        total = sum(len(s.get('points', [])) for s in liste)
        corps = []
        for s in liste:
            chemin = ' › '.join(s['chemin'][:-1])
            points = []
            for p in s.get('points', []):
                t = p['texte']
                if p.get('portee'):
                    t += ' [%s]' % ('oral' if p['portee'] == 'oral' else 'écrit')
                if p.get('exemples'):
                    t += ' — ex. : ' + ' ; '.join(p['exemples'])
                points.append(t)
            corps.append(
                '<div class="savoir"><div class="savoir-tete">'
                '<span class="savoir-titre">%s</span>'
                '<span class="savoir-chemin">%s</span></div>%s</div>'
                % (e(s['titre']), e(chemin), puces(points)))
        out.append('<details class="pli"><summary>%s <span class="compte">%d savoirs · '
                   '%d points</span></summary><div class="pli-corps">%s</div></details>'
                   % (e(noms_cat.get(cid, cid)), len(liste), total, ''.join(corps)))
    return ''.join(out)


def temps_de_verbes(niv):
    """Les temps et modes prescrits au niveau, et les autres savoirs du verbe."""
    temps, autres = [], []
    for s in niv['savoirs']:
        if 'Verbes et GV' not in s['chemin']:
            continue
        if _TEMPS.match(s['titre']):
            temps.append(s)
        elif s['titre'] != 'Verbes et GV':
            autres.append(s)
    return temps, autres


def bloc_verbes(niv):
    temps, autres = temps_de_verbes(niv)
    if not temps and not autres:
        return ('<p class="rien">Aucun temps de verbe n’est prescrit à ce niveau : '
                'le programme n’y nomme pas encore la conjugaison.</p>')
    chips = ''.join('<span class="jeton">%s</span>' % e(s['titre']) for s in temps)
    detail = []
    for s in temps + autres:
        points = []
        for p in s.get('points', []):
            t = p['texte']
            if p.get('exemples'):
                t += ' — ex. : ' + ' ; '.join(p['exemples'])
            points.append(t)
        detail.append('<div class="savoir"><div class="savoir-tete">'
                      '<span class="savoir-titre">%s</span></div>%s</div>'
                      % (e(s['titre']), puces(points)))
    return ('<div class="jetons">%s</div>'
            '<details class="pli"><summary>Ce que le programme en dit '
            '<span class="compte">%d entrées</span></summary>'
            '<div class="pli-corps">%s</div></details>'
            % (chips, len(temps) + len(autres), ''.join(detail)))


def bloc_attentes(niv):
    out = []
    for cle, titre in (('attentesFinDeCours', 'Attentes de fin de cours'),
                       ('criteresEvaluation', 'Critères d’évaluation')):
        blocs = niv.get(cle) or []
        if not blocs:
            continue
        items = []
        for b in blocs:
            for p in (b.get('points') or [b.get('texte', '')]):
                if p:
                    items.append(p)
        out.append('<details class="pli"><summary>%s <span class="compte">%d</span>'
                   '</summary><div class="pli-corps">%s</div></details>'
                   % (titre, len(items), puces(items)))
    return ''.join(out)


def ligne_module(slug, m, niv, lex, index):
    situation, note = situation_du_module(slug, niv)
    intentions = [i for i in niv['intentions'] if i.get('situation') == situation]
    domaine = next((i['domaine'] for i in intentions if i.get('domaine')), '—')
    entrees = lex.get(situation, []) if situation else []

    par_comp = {}
    for i in intentions:
        for c in i['competences']:
            par_comp.setdefault(c, []).append(i['intention'])
    pastilles = ''.join(
        '<span class="comp c-%s" title="%s">%s<span class="n">%d</span></span>'
        % (cid, e(NOMS_COMP[cid]), cid.upper(), len(par_comp[cid]))
        for cid in ('co', 'po', 'ce', 'pe') if cid in par_comp) or \
        '<span class="rien-inline">—</span>'

    detail_intentions = ''
    for cid in ('co', 'po', 'ce', 'pe'):
        if cid in par_comp:
            detail_intentions += ('<div class="par-comp"><span class="comp c-%s">%s</span>%s</div>'
                                  % (cid, cid.upper(), puces(par_comp[cid])))
    if not detail_intentions:
        detail_intentions = ('<p class="rien">Aucune intention rattachée : le module ne se '
                             'rattache pas à une situation du niveau.</p>')

    if entrees:
        lex_html = puces([x + (' (rattachée)' if r else '') for x, r in entrees],
                         'liste-lex')
    else:
        lex_html = ('<p class="rien">Le lexique thématique ne couvre pas cette situation. '
                    'Les mots du module s’inventent à partir des savoirs lexicaux du '
                    'niveau.</p>')

    lien = '../interactive/%s/%s-activite-interactive.html' % (slug, slug)
    cle = ' '.join([slug, m['titre'], m.get('chapeau', ''), situation or '', domaine,
                    ' '.join(i['intention'] for i in intentions)]).lower()

    return """
      <tbody class="ligne" data-cle="%(cle)s">
        <tr class="rang">
          <td class="num">%(numero)s</td>
          <td class="mod">
            <a href="%(lien)s" target="_blank" rel="noopener">%(titre)s</a>
            <span class="slug">%(slug)s · activité %(activite)s</span>
          </td>
          <td class="sit">%(situation)s<span class="dgf">%(domaine)s</span></td>
          <td class="ints">%(pastilles)s</td>
          <td class="lex">%(nlex)s</td>
          <td class="plus">
            <button type="button" class="ouvrir" aria-expanded="false"
                    aria-controls="d%(index)d">Détail</button>
          </td>
        </tr>
        <tr class="detail" id="d%(index)d" hidden>
          <td colspan="6">
            <div class="grille-detail">
              <section>
                <h4>Intentions de communication</h4>
                %(detail_intentions)s
              </section>
              <section>
                <h4>Lexique thématique de la situation <span class="compte">%(nlex)s</span></h4>
                %(lex_html)s
              </section>
            </div>
            <details class="pli note-cadrage">
              <summary>Note de cadrage — pourquoi ce module est construit ainsi</summary>
              <div class="pli-corps prose">%(note)s</div>
            </details>
          </td>
        </tr>
      </tbody>""" % {
        'cle': e(cle), 'numero': m.get('numero', '—'),
        'activite': m.get('activite', '—'), 'lien': e(lien),
        'titre': e(m['titre']), 'slug': e(slug),
        'situation': e(situation or 'hors situation du niveau'),
        'domaine': e(domaine), 'pastilles': pastilles, 'nlex': len(entrees),
        'index': index, 'detail_intentions': detail_intentions,
        'lex_html': lex_html, 'note': note_html(note)}


def page(prog):
    pal = couleurs()
    aujourdhui = datetime.date.today()
    mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
            'août', 'septembre', 'octobre', 'novembre', 'décembre']
    date_fr = '%d %s %d' % (aujourdhui.day, mois[aujourdhui.month - 1],
                            aujourdhui.year)

    par_niveau = {}
    for slug, m in MODULES.items():
        par_niveau.setdefault(m.get('niveau'), []).append((slug, m))

    sections, onglets, index = [], [], 0
    total_modules = total_intentions = 0
    for niv in prog['niveaux']:
        n = niv['niveau']
        liste = sorted(par_niveau.get(n, []),
                       key=lambda x: (x[1].get('numero') or 0))
        if not liste:
            continue
        lex = lexique_par_situation(niv)
        lignes = []
        for slug, m in liste:
            index += 1
            lignes.append(ligne_module(slug, m, niv, lex, index))
            situation, _ = situation_du_module(slug, niv)
            total_intentions += len([i for i in niv['intentions']
                                     if i.get('situation') == situation])
        total_modules += len(liste)
        onglets.append('<button type="button" class="onglet" data-f="n%d" '
                       'aria-pressed="false">Niveau %d <span class="n">%d</span></button>'
                       % (n, n, len(liste)))
        sections.append("""
    <section class="niveau" data-niv="n%(n)d" style="--niv:%(line)s; --niv-doux:%(bg)s">
      <div class="tete">
        <span class="eyebrow">Niveau %(n)d · %(code)s · stade %(stade)s</span>
        <h2>%(titre)s</h2>
        <p>%(nmod)d module%(s)s · %(nsit)d situations de vie et %(nint)d intentions au
        programme · %(nsav)d savoirs prescrits, communs à tout le niveau.</p>
      </div>

      <div class="prescrit">
        <div class="carte">
          <h3>Temps et modes du verbe prescrits</h3>
          %(verbes)s
        </div>
        <div class="carte">
          <h3>Savoirs du cours</h3>
          <p class="fin">Le programme les prescrit <b>par niveau</b>, jamais par
          situation : ils valent pour tous les modules de cette section.</p>
          %(savoirs)s
        </div>
        <div class="carte">
          <h3>Ce qui est attendu à la fin</h3>
          %(attentes)s
        </div>
      </div>

      <table class="modules">
        <thead>
          <tr>
            <th class="num">N<sup>o</sup></th><th>Module</th><th>Situation de vie · domaine</th>
            <th>Intentions</th><th>Lexique</th><th></th>
          </tr>
        </thead>
        %(lignes)s
      </table>
    </section>""" % {
            'n': n, 'line': pal[n][0], 'bg': pal[n][1], 'code': e(niv['code']),
            'stade': e(niv['stade']), 'titre': e(niv['titre']),
            'nmod': len(liste), 's': 's' if len(liste) > 1 else '',
            'nsit': len(niv['situations']), 'nint': len(niv['intentions']),
            'nsav': len(niv['savoirs']),
            'verbes': bloc_verbes(niv), 'savoirs': bloc_savoirs(niv),
            'attentes': bloc_attentes(niv), 'lignes': ''.join(lignes)})

    return GABARIT % {
        'onglets': ''.join(onglets), 'sections': ''.join(sections),
        'total': total_modules, 'date': date_fr,
        'total_intentions': total_intentions}


GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ce que le programme prescrit, module par module — francis</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<link rel="stylesheet" href="../design-system/marque-francis.css">
<link rel="icon" type="image/svg+xml" href="../design-system/marque-francis-favicon.svg">
<style>
  /* Page générée par build/tableau_programme.py — ne pas retoucher à la main.
     Système de design Francisation / francis, thème clair unique. Le violet
     appartient à la marque : la couleur d'une section est celle de son niveau. */
  :root{
    --accent:#0A8F5B; --accent-soft:#E6F5EE; --accent-ink:#07734A;
    --surface-band:#EDF6F1;
    --ink-900:#17181A; --ink-700:#3A3D40; --ink-500:#4B4F52; --ink-400:#6E7175;
    --surface-page:#F7F7F5; --surface-card:#FFFFFF; --surface-sunken:#FBFBFA;
    --paper-200:#F0F0EE;
    --border:#EAEAE8; --border-firm:#D6D6D2; --border-tint:#D8E8DF;
    --ambre-700:#B45309;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
    --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:20px;
    --sp-6:24px; --sp-8:32px; --sp-12:48px;
    --content-max:1180px; --gutter:32px;
    --fs-hero:clamp(34px,5vw,50px); --fs-h2:28px; --fs-h3:19px; --fs-lead:19px;
    --fs-body:17px; --fs-body-sm:16px; --fs-ui:15px; --fs-ui-sm:14px;
    --fs-label:13px; --fs-meta:12px;
    --lh-title:1.2; --ls-title:-0.015em; --ls-label:0.12em;
    --r-sm:10px; --r-md:14px; --r-lg:18px; --r-pill:999px;
    --sh-card:0 1px 2px rgba(20,20,20,.04);
    --dur:140ms; --ease:cubic-bezier(.2,.7,.3,1);
    --tap-comfort:44px;
  }
  *{box-sizing:border-box}
  body{margin:0; background:var(--surface-page); color:var(--ink-900);
    font-family:var(--font-sans); font-size:var(--fs-body); font-weight:600;
    line-height:1.5; -webkit-font-smoothing:antialiased}
  :focus-visible{outline:3px solid var(--accent); outline-offset:2px; border-radius:4px}
  .conteneur{max-width:var(--content-max); margin:0 auto; padding:0 var(--gutter)}

  .bande{background:var(--surface-band); border-bottom:1px solid var(--border-tint);
    padding:var(--sp-12) 0 var(--sp-8)}
  .bande .conteneur{display:flex; flex-direction:column; gap:var(--sp-6)}
  .surtitre{font-size:var(--fs-label); font-weight:800; letter-spacing:var(--ls-label);
    text-transform:uppercase; color:var(--marque-600)}
  h1{font-size:var(--fs-hero); font-weight:900; letter-spacing:-0.02em;
    line-height:1.05; margin:0; max-width:20ch; text-wrap:balance}
  .chapeau{font-size:var(--fs-lead); font-weight:600; color:var(--ink-700);
    margin:0; max-width:70ch}

  .tri{position:sticky; top:0; z-index:20; background:rgba(247,247,245,.94);
    backdrop-filter:blur(8px); border-bottom:1px solid var(--border);
    padding:var(--sp-3) 0}
  .tri .conteneur{display:flex; flex-wrap:wrap; align-items:center; gap:var(--sp-3)}
  .onglets{display:flex; flex-wrap:wrap; gap:var(--sp-2); margin-right:auto}
  .onglet{appearance:none; font:inherit; font-size:var(--fs-ui-sm); font-weight:800;
    padding:7px 14px; min-height:36px; border-radius:var(--r-pill);
    border:1px solid var(--border-firm); background:var(--surface-card);
    color:var(--ink-700); cursor:pointer; display:inline-flex; align-items:center; gap:6px}
  .onglet:hover{background:var(--paper-200)}
  .onglet[aria-pressed="true"]{background:var(--ink-900); border-color:var(--ink-900); color:#FFF}
  .onglet .n{font-size:var(--fs-meta); font-weight:800; color:var(--ink-400);
    font-variant-numeric:tabular-nums}
  .onglet[aria-pressed="true"] .n{color:rgba(255,255,255,.72)}
  .recherche{appearance:none; font:inherit; font-size:var(--fs-ui); font-weight:600;
    min-height:38px; padding:0 var(--sp-4); border-radius:var(--r-pill);
    border:1px solid var(--border-firm); background:var(--surface-card); width:300px}

  main{padding-bottom:var(--sp-12)}
  .niveau{padding:var(--sp-12) 0 0}
  .niveau[hidden]{display:none}
  .tete{border-left:4px solid var(--niv); padding-left:var(--sp-5); margin-bottom:var(--sp-6)}
  .eyebrow{font-size:var(--fs-label); font-weight:800; letter-spacing:var(--ls-label);
    text-transform:uppercase; color:var(--niv); display:block; margin-bottom:var(--sp-2)}
  h2{font-size:var(--fs-h2); font-weight:900; letter-spacing:var(--ls-title);
    line-height:var(--lh-title); margin:0}
  .tete p{font-size:var(--fs-body-sm); font-weight:600; color:var(--ink-400);
    max-width:78ch; margin:var(--sp-2) 0 0}

  .prescrit{display:grid; grid-template-columns:repeat(3,1fr); gap:var(--sp-4);
    margin-bottom:var(--sp-6); align-items:start}
  .carte{background:var(--surface-card); border:1px solid var(--border);
    border-top:3px solid var(--niv); border-radius:var(--r-lg);
    box-shadow:var(--sh-card); padding:var(--sp-5)}
  .carte h3{font-size:var(--fs-h3); font-weight:900; letter-spacing:var(--ls-title);
    margin:0 0 var(--sp-3)}
  .fin{font-size:var(--fs-ui-sm); font-weight:600; color:var(--ink-400);
    margin:0 0 var(--sp-3)}
  .jetons{display:flex; flex-wrap:wrap; gap:6px; margin-bottom:var(--sp-3)}
  .jeton{display:inline-flex; align-items:center; padding:4px 11px;
    border-radius:var(--r-pill); background:var(--niv-doux); color:var(--niv);
    font-size:var(--fs-ui-sm); font-weight:800}
  .rien{font-size:var(--fs-ui-sm); font-weight:600; color:var(--ink-400); margin:0}
  .rien-inline{color:var(--ink-400)}

  details.pli{border-top:1px solid var(--border)}
  details.pli summary{cursor:pointer; list-style:none; padding:10px 0;
    font-size:var(--fs-ui); font-weight:800; display:flex; align-items:center;
    justify-content:space-between; gap:var(--sp-3)}
  details.pli summary::-webkit-details-marker{display:none}
  details.pli summary::after{content:"+"; font-weight:900; color:var(--ink-400)}
  details.pli[open] summary::after{content:"–"}
  .compte{font-size:var(--fs-meta); font-weight:800; color:var(--ink-400);
    font-variant-numeric:tabular-nums; text-transform:none; letter-spacing:0}
  .pli-corps{padding:0 0 var(--sp-4)}
  .savoir{margin-bottom:var(--sp-3)}
  .savoir-tete{display:flex; flex-wrap:wrap; align-items:baseline; gap:var(--sp-2)}
  .savoir-titre{font-size:var(--fs-ui); font-weight:900}
  .savoir-chemin{font-size:var(--fs-meta); font-weight:700; color:var(--ink-400)}
  ul.liste-points, ul.liste-lex, ul.liste-note{margin:var(--sp-2) 0 0; padding-left:18px}
  ul.liste-points li, ul.liste-lex li, ul.liste-note li{font-size:var(--fs-ui-sm);
    font-weight:600; color:var(--ink-700); margin-bottom:5px}
  ul.liste-lex{columns:2; column-gap:var(--sp-6)}

  table.modules{width:100%%; border-collapse:collapse; background:var(--surface-card);
    border:1px solid var(--border); border-radius:var(--r-lg); overflow:hidden}
  table.modules thead th{text-align:left; font-size:var(--fs-label); font-weight:800;
    letter-spacing:.06em; text-transform:uppercase; color:var(--ink-400);
    padding:var(--sp-3) var(--sp-4); border-bottom:1px solid var(--border-firm);
    background:var(--surface-sunken)}
  tbody.ligne{border-bottom:1px solid var(--border)}
  tbody.ligne[hidden]{display:none}
  tbody.ligne td{padding:var(--sp-3) var(--sp-4); vertical-align:top;
    font-size:var(--fs-body-sm)}
  td.num, th.num{width:56px; font-variant-numeric:tabular-nums; font-weight:800;
    color:var(--ink-400)}
  td.mod a{font-weight:900; color:var(--ink-900); text-decoration:none;
    text-decoration-color:var(--niv)}
  td.mod a:hover{text-decoration:underline}
  .slug{display:block; font-size:var(--fs-meta); font-weight:700; color:var(--ink-400)}
  td.sit{max-width:22ch}
  .dgf{display:block; font-size:var(--fs-meta); font-weight:800; color:var(--niv);
    text-transform:uppercase; letter-spacing:.05em; margin-top:2px}
  .comp{display:inline-flex; align-items:center; gap:5px; padding:3px 9px;
    border-radius:var(--r-pill); font-size:var(--fs-meta); font-weight:900;
    background:var(--paper-200); color:var(--ink-700); margin:0 4px 4px 0}
  .comp .n{font-variant-numeric:tabular-nums; color:var(--ink-400)}
  .c-co{background:#E7F0F6; color:#1D6B8F} .c-po{background:#DCF2EF; color:#0D7A6F}
  .c-ce{background:#F7F0DA; color:#8C6A07} .c-pe{background:#FBEEDC; color:#B45309}
  td.lex{font-variant-numeric:tabular-nums; font-weight:800; color:var(--ink-400)}
  .ouvrir{appearance:none; font:inherit; font-size:var(--fs-ui-sm); font-weight:800;
    padding:6px 14px; min-height:34px; border-radius:var(--r-pill);
    border:1px solid var(--border-firm); background:var(--surface-card);
    color:var(--ink-700); cursor:pointer; white-space:nowrap}
  .ouvrir:hover{background:var(--paper-200)}
  tr.detail td{background:var(--surface-sunken); border-top:1px solid var(--border)}
  .grille-detail{display:grid; grid-template-columns:1fr 1fr; gap:var(--sp-6)}
  .grille-detail h4{font-size:var(--fs-ui); font-weight:900; margin:0 0 var(--sp-2);
    display:flex; gap:var(--sp-2); align-items:baseline}
  .par-comp{margin-bottom:var(--sp-3)}
  .note-cadrage{margin-top:var(--sp-4)}
  .prose p{font-size:var(--fs-ui-sm); font-weight:600; color:var(--ink-700);
    margin:0 0 var(--sp-3); max-width:80ch}
  .prose h5{font-size:var(--fs-ui); font-weight:900; margin:var(--sp-4) 0 var(--sp-2)}

  .vide{display:none; background:var(--surface-sunken); border:1px solid var(--border);
    border-radius:var(--r-lg); padding:var(--sp-6); color:var(--ink-400);
    font-size:var(--fs-body-sm); font-weight:600; margin-top:var(--sp-8)}
  .vide[data-on="oui"]{display:block}
  .note{margin-top:var(--sp-12); background:var(--surface-card); border:1px solid var(--border);
    border-left:4px solid var(--ambre-700); border-radius:var(--r-lg);
    padding:var(--sp-5) var(--sp-6)}
  .note b.tit{display:block; font-size:var(--fs-body-sm); font-weight:900;
    margin-bottom:var(--sp-2)}
  .note p{margin:0 0 var(--sp-2); font-size:var(--fs-body-sm); font-weight:600;
    color:var(--ink-700); max-width:78ch}
  .note p:last-child{margin-bottom:0}
  footer{border-top:1px solid var(--border); background:var(--surface-band);
    padding:var(--sp-8) 0; margin-top:var(--sp-12)}
  footer .conteneur{display:flex; align-items:center; gap:var(--sp-4); flex-wrap:wrap}
  footer p{font-size:var(--fs-ui); font-weight:700; color:var(--ink-400); margin:0}
  footer a{color:var(--accent-ink)}

  @media (max-width:980px){
    .prescrit{grid-template-columns:1fr}
    .grille-detail{grid-template-columns:1fr}
    ul.liste-lex{columns:1}
    table.modules, table.modules thead, tbody.ligne, tbody.ligne tr, tbody.ligne td{display:block}
    table.modules thead{display:none}
    tbody.ligne td{padding:var(--sp-2) var(--sp-4)}
    tbody.ligne td:first-child{padding-top:var(--sp-4)}
    td.sit{max-width:none}
  }
  @media (max-width:720px){ :root{--gutter:20px} .recherche{width:100%%} }
  @media print{ .tri, .ouvrir{display:none} details.pli{border-color:#CCC} }
</style>
</head>
<body>

<div class="fr-barre">
  <div class="fr-barre__in">
    <div class="fr-lockup fr-lockup--grand">
      <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
      <span class="fr-trait" aria-hidden="true"></span>
      <span class="fr-desc">Aide à l'apprentissage du français</span>
    </div>
  </div>
</div>

<header class="bande">
  <div class="conteneur">
    <div class="surtitre">Repères · Le prescrit derrière chaque module</div>


    <h1>Ce que le programme prescrit, module par module</h1>
    <p class="chapeau">%(total)d modules, des huit niveaux du <b>Programme d'études
    Francisation</b> (MEQ, 2015). Pour chacun : la situation de vie et son domaine
    général de formation, les intentions de communication par compétence, le lexique
    thématique rattaché — et, pour son niveau, les savoirs prescrits, les temps de
    verbes, les attentes de fin de cours et les critères d'évaluation.</p>
  </div>
</header>

<nav class="tri" aria-label="Filtrer les modules">
  <div class="conteneur">
    <div class="onglets" role="group" aria-label="Filtrer par niveau">
      <button type="button" class="onglet" data-f="tout" aria-pressed="true">Tous les niveaux <span class="n">%(total)d</span></button>
      %(onglets)s
    </div>
    <input type="search" class="recherche" id="q" placeholder="Chercher un module, une situation…"
           aria-label="Chercher un module, une situation ou une intention">
  </div>
</nav>

<main>
  <div class="conteneur">
%(sections)s

    <p class="vide" id="vide">Aucun module ne correspond à cette recherche.</p>

    <div class="note">
      <b class="tit">Ce que cette page dit, et ce qu'elle ne dit pas</b>
      <p>Les <b>savoirs</b> — grammaire du texte, grammaire de la phrase, temps de
      verbes, phonétique, lexique — sont prescrits <b>par niveau</b> : le programme
      ne les rattache à aucune situation en particulier. Ils sont donc affichés une
      fois par niveau et valent pour tous ses modules. Ce que chaque module a
      réellement retenu de ces savoirs, et pourquoi, est écrit dans sa <b>note de
      cadrage</b>, reprise en entier dans le détail de sa ligne.</p>
      <p>Les <b>intentions de communication</b> et le <b>lexique thématique</b>, eux,
      sont bien rattachés à la situation de vie du module : ce sont les lignes du
      programme qui ont décidé de ce que le module fait faire.</p>
      <p>Le lexique vient d'un <b>autre document</b> que le programme — la Progression
      du lexique du CSS de Laval, juin 2020. Il ne couvre pas toutes les situations :
      là où il est vide, les mots du module ont été composés à partir des savoirs
      lexicaux du niveau. Une entrée marquée « rattachée » continue la situation
      précédente dans le tableau d'origine.</p>
      <p>Aucun contenu de module n'est repris d'un manuel : le programme donne la
      spécification, jamais le scénario.</p>
    </div>

  </div>
</main>

<footer>
  <div class="conteneur">
    <span class="fr-lockup fr-lockup--courriel"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span></span>
    <p>Page générée par <code>build/tableau_programme.py</code> · %(date)s ·
    <a href="../../catalogue.html">Catalogue des activités</a> ·
    <a href="../../presentations.html">Le classeur</a></p>
  </div>
</footer>

<script>
(function () {
  var onglets = Array.prototype.slice.call(document.querySelectorAll('.onglet'));
  var niveaux = Array.prototype.slice.call(document.querySelectorAll('.niveau'));
  var lignes  = Array.prototype.slice.call(document.querySelectorAll('tbody.ligne'));
  var q = document.getElementById('q');
  var vide = document.getElementById('vide');
  var filtre = 'tout';

  function texte(l) { return ((l.dataset.cle || '') + ' ' + l.textContent).toLowerCase(); }

  function appliquer() {
    var m = (q.value || '').trim().toLowerCase();
    var visibles = 0;
    niveaux.forEach(function (niv) {
      var garde = (filtre === 'tout' || niv.dataset.niv === filtre);
      var restant = 0;
      Array.prototype.slice.call(niv.querySelectorAll('tbody.ligne')).forEach(function (l) {
        var ok = garde && (!m || texte(l).indexOf(m) !== -1);
        l.hidden = !ok;
        if (ok) { restant++; visibles++; }
      });
      niv.hidden = (restant === 0);
    });
    vide.setAttribute('data-on', visibles === 0 ? 'oui' : 'non');
  }

  onglets.forEach(function (b) {
    b.addEventListener('click', function () {
      filtre = b.dataset.f;
      onglets.forEach(function (o) {
        o.setAttribute('aria-pressed', o === b ? 'true' : 'false');
      });
      appliquer();
    });
  });
  q.addEventListener('input', appliquer);

  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('.ouvrir');
    if (!b) return;
    var d = document.getElementById(b.getAttribute('aria-controls'));
    var ouvert = b.getAttribute('aria-expanded') === 'true';
    b.setAttribute('aria-expanded', ouvert ? 'false' : 'true');
    b.textContent = ouvert ? 'D\\u00e9tail' : 'Fermer';
    d.hidden = ouvert;
  });
})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--ou', default=str(SORTIE), help='fichier de sortie')
    args = ap.parse_args()
    if not PROGRAMME.exists():
        sys.exit('!! programme introuvable : %s' % PROGRAMME)
    prog = json.loads(PROGRAMME.read_text(encoding='utf-8'))
    cible = pathlib.Path(args.ou)
    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(page(prog), encoding='utf-8')
    print('✓ %s (%d modules)' % (cible, len(MODULES)))
    return 0


if __name__ == '__main__':
    sys.exit(main())
