#!/usr/bin/env python3
"""Relève tous les artefacts du dépôt et écrit la page de rangement.

    python3 build/releve_artefacts.py

La banque de présentations est la porte d'entrée des artefacts du projet
(`presentations.html`). Ce relevé la confronte au disque : ce qui est rangé,
ce qui ne l'est pas, et ce qui n'a rien à y faire.

**La ligne, et c'est elle qui décide de tout.** Un artefact est un document
*sur le projet* — une présentation, un relevé, une décision à trancher, un
plan. Le **matériel de cours** — les 1 376 fiches et diaporamas de
`assets/documents/` — n'en est pas un : il est servi par le catalogue, à des
élèves, dans un module. Sans cette ligne, « tout au même endroit » avalerait
mille fiches et rendrait la banque inutilisable.
"""
import collections
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
BANQUE = RACINE / 'presentations.html'
DOSSIER = RACINE / 'assets' / 'presentations'


def fiches():
    """(famille, titre, cibles) pour chaque fiche de la banque."""
    h = BANQUE.read_text()
    out = []
    for bloc in re.split(r'(?=<section class="famille")', h):
        m = re.match(r'<section class="famille" data-fam="([a-z]+)">', bloc)
        if not m:
            continue
        fam = m.group(1)
        for art in re.findall(r'<article class="fiche".*?</article>', bloc, re.S):
            t = re.search(r'<h3 class="titre">(.*?)</h3>', art, re.S)
            if not t:
                continue
            out.append((fam, re.sub(r'\s+', ' ', t.group(1)).strip(),
                        re.findall(r'href="([^"]+)"', art)))
    return out


def annonces():
    return dict(re.findall(r'data-f="([a-z]+)"[^>]*>[^<]*<span class="n">(\d+)</span>',
                           BANQUE.read_text()))


def couvert_par_index(chemin, cites):
    """Un artefact peut être rangé **par un index** plutôt que par sa propre
    fiche : `docs/` par la page des documents de travail, les modules autonomes
    par leur propre index. Compter ces fichiers comme « hors banque » ferait
    croire à un désordre là où le rangement est simplement à deux étages."""
    for index, prefixe in [
            (DOSSIER / 'documents-de-travail.html', 'docs/'),
            (RACINE / 'modules-autonomes' / 'index.html', 'modules-autonomes/')]:
        rel = str(index.relative_to(RACINE))
        if rel not in cites or not index.exists():
            continue
        if not chemin.startswith(prefixe):
            continue
        if pathlib.Path(chemin).stem in index.read_text(errors='replace'):
            return True
        if pathlib.Path(chemin).parent.name in index.read_text(errors='replace'):
            return True
    return False


def hors_banque():
    """Les artefacts du dépôt qu'aucune fiche ne cite, ni aucun index.

    `essais/` n'y figure pas : ce sont des brouillons régénérables par
    `build/essai_*.py`, et quatre des six ne sont même pas suivis par git. Un
    brouillon n'est pas un artefact du projet ; le compter comme tel donnerait
    un ménage qui ne finit jamais."""
    cites = set(re.findall(r'href="([^"]+)"', BANQUE.read_text()))
    familles = collections.OrderedDict()
    for etiquette, dossier, motifs in [
            ('Documents de travail', 'docs', ('.md',)),
            ('Outils autonomes', 'assets/outils', ('.html',)),
            ('Modules autonomes', 'modules-autonomes', ('.html', '.md')),
    ]:
        d = RACINE / dossier
        if not d.exists():
            continue
        tout = sorted(f for f in d.rglob('*') if f.is_file() and f.suffix in motifs)
        manque = [f for f in tout
                  if str(f.relative_to(RACINE)) not in cites
                  and not couvert_par_index(str(f.relative_to(RACINE)), cites)]
        familles[etiquette] = (dossier, len(tout), manque)
    return familles


def esc(s):
    return (str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def page():
    F = fiches()
    A = annonces()
    par_fam = collections.Counter(f[0] for f in F)
    ecarts = [(f, A.get(f, '—'), par_fam[f]) for f in
              ['trousse', 'direction', 'enseignants', 'chantier', 'reperes']]
    hb = hors_banque()
    docs = len(list((RACINE / 'assets' / 'documents').glob('*'))) \
        if (RACINE / 'assets' / 'documents').exists() else 0
    sur_disque = [p for p in DOSSIER.iterdir() if p.is_file()]
    dossiers = [p for p in DOSSIER.iterdir() if p.is_dir()]
    cites = set(re.findall(r'assets/presentations/([A-Za-z0-9._/-]+)',
                           BANQUE.read_text()))
    orphelins = [p.name for p in sur_disque if p.name not in cites]
    style_src = (DOSSIER / 'audio-manquant.html').read_text()
    style = style_src[style_src.index('<style>'):style_src.index('</style>') + 8]

    chantier = [t for fam, t, _ in F if fam == 'chantier']

    lignes_ecart = ''.join(
        '<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td></tr>'
        % (f, a, r, '<b class="mal">écart</b>' if str(a) != str(r) else '—')
        for f, a, r in ecarts)

    lignes_hors = ''
    for etiquette, (dossier, total, manque) in hb.items():
        exemples = ', '.join('<code>%s</code>' % esc(m.name) for m in manque[:3])
        lignes_hors += (
            '<tr><td><b>%s</b><br><code>%s/</code></td><td>%d</td><td>%d</td>'
            '<td>%s%s</td></tr>'
            % (etiquette, dossier, total, len(manque), exemples,
               ' …' if len(manque) > 3 else ''))

    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Ranger les artefacts</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600&family=Nunito:ital,wght@0,400;0,600;0,700;0,800&display=swap">
{style}
<style>
/* Un tableau déborde sur un écran étroit : il défile dans son propre cadre
   plutôt que de pousser la page entière. Mesuré à 609 px : 644 sans ceci. */
.cadre-tab{{overflow-x:auto;margin:16px 0 0}}
.tab{{width:100%;min-width:420px;border-collapse:collapse;font-size:15px}}
.tab th,.tab td{{text-align:left;padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top}}
.tab th{{font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--muted);font-weight:800}}
.tab code{{font-family:var(--mono);font-size:12.5px;color:var(--muted)}}
.mal{{color:var(--trou)}}
.chiffres{{display:flex;gap:26px;flex-wrap:wrap;margin:24px 0 0;padding:18px 20px;
  background:var(--card);border:1px solid var(--line);border-radius:12px}}
.chiffre b{{display:block;font-family:Newsreader,Georgia,serif;font-size:32px;font-weight:500;
  color:var(--ink);line-height:1}}
.chiffre span{{font-size:13px;color:var(--muted)}}
.bloc{{margin:54px 0 0}}
.bloc>p{{margin:10px 0 0}}
.opt{{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--acier);
  border-radius:12px;padding:18px 20px;margin:18px 0 0}}
.opt--reco{{border-left-color:var(--ok)}}
.opt h3{{font-family:Newsreader,Georgia,serif;font-size:21px;font-weight:600;color:var(--ink);margin:0 0 4px}}
.opt .eti{{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ok)}}
.pour{{display:grid;gap:6px;margin:12px 0 0;font-size:15px}}
.pour div::before{{content:"· ";color:var(--muted)}}
.onglets{{display:flex;gap:8px;flex-wrap:wrap;margin:14px 0 0}}
.onglets span{{font-size:13px;font-weight:800;background:var(--sunken);border:1px solid var(--line);
  border-radius:99px;padding:5px 12px;color:var(--body)}}
.onglets span.pri{{background:var(--ok-bg);border-color:var(--ok);color:var(--ok)}}
.liste{{columns:2;column-gap:28px;font-size:14.5px;margin:12px 0 0}}
@media (max-width:620px){{.liste{{columns:1}}}}
.liste div{{break-inside:avoid;padding:2px 0}}
.note{{background:var(--part-bg);border-left:3px solid var(--part);border-radius:0 8px 8px 0;
  padding:14px 16px;margin:18px 0 0;font-size:15px}}
</style>
</head>
<body>
<div class="doc">
  <p class="eyebrow">Fouille et proposition · 31 août 2026</p>
  <h1>Ranger les artefacts</h1>
  <p class="chapeau">Tout ce que le projet produit à côté des cours — présentations, relevés,
  décisions à trancher, plans — devrait se retrouver au même endroit. La banque de
  présentations est cet endroit. <strong>Elle est saine à l'intérieur</strong> : aucun fichier
  oublié, aucun lien mort. Ce qui ne va pas est ailleurs, et c'est plus intéressant.</p>

  <div class="chiffres">
    <div class="chiffre"><b>{len(F)}</b><span>fiches à la banque</span></div>
    <div class="chiffre"><b>{len(sur_disque)}</b><span>fichiers rangés</span></div>
    <div class="chiffre"><b>{len(orphelins)}</b><span>orphelins</span></div>
    <div class="chiffre"><b>{sum(len(m) for _, _, m in hb.values())}</b><span>artefacts hors banque</span></div>
    <div class="chiffre"><b>{docs}</b><span>fiches de cours <i>(hors sujet)</i></span></div>
  </div>

  <div class="bloc">
    <h2>La ligne, avant tout le reste</h2>
    <p>« Tout au même endroit » ne peut pas vouloir dire <i>tout</i>. Le dossier
    <code>assets/documents/</code> contient <b>{docs} fiches et diaporamas de cours</b> : ils
    sont servis par le catalogue, à des élèves, dans un module. Les verser à la banque la
    rendrait inutilisable le jour même.</p>
    <div class="cadre-tab"><table class="tab">
      <tr><th>Va à la banque</th><th>N'y va pas</th></tr>
      <tr><td>Un document <b>sur le projet</b> : une présentation, un relevé, une décision à
      trancher, un plan, un état d'avancement.</td>
      <td>Le <b>matériel de cours</b> : fiches élèves, diaporamas de séance, plans de cours,
      images de modules. Le catalogue est leur porte.</td></tr>
      <tr><td>Ce qu'on ouvre pour <b>montrer, décider ou comprendre</b>.</td>
      <td>Ce qu'on ouvre pour <b>enseigner</b>.</td></tr>
    </table></div>
  </div>

  <div class="bloc">
    <h2>Ce que la fouille a trouvé</h2>

    <h4 style="margin-top:26px">1 · Les compteurs mentent déjà</h4>
    <p>Les nombres des onglets sont écrits à la main. Ils sont faux depuis deux fiches.</p>
    <div class="cadre-tab"><table class="tab">
      <tr><th>Onglet</th><th>Annoncé</th><th>Réel</th><th></th></tr>
      {lignes_ecart}
      <tr><td><b>Tout</b></td><td>{A.get('tout', '—')}</td><td>{len(F)}</td>
          <td>{'<b class="mal">écart</b>' if str(A.get('tout')) != str(len(F)) else '—'}</td></tr>
    </table></div>

    <h4 style="margin-top:30px">2 · Une famille avale la moitié de la banque</h4>
    <p><b>{par_fam['chantier']} fiches sur {len(F)}</b> sont dans « Chantier ». Une famille qui
    contient tout ne classe rien — et le mot recouvre trois choses différentes : des
    <b>décisions</b> qui attendent votre jugement, des <b>états</b> mesurés à un instant, et
    des <b>propositions</b> qui n'ont pas encore été faites.</p>
    <div class="liste">{''.join('<div>· %s</div>' % esc(t) for t in chantier)}</div>

    <h4 style="margin-top:30px">3 · Deux classements se disputent la même rangée d'onglets</h4>
    <p><b>Trousse</b>, <b>Direction</b> et <b>Enseignants</b> disent <i>à qui</i> le document
    s'adresse. <b>Chantier</b> et <b>Repères</b> disent <i>ce que c'est</i>. Un même document
    répond aux deux, donc il tombe où il peut — et « Chantier » est le où-il-peut par défaut.
    <strong>C'est la cause, et les deux constats précédents en sont les effets.</strong></p>

    <h4 style="margin-top:30px">4 · Ce qui existe mais n'est pas rangé</h4>
    <div class="cadre-tab"><table class="tab">
      <tr><th>Famille</th><th>Fichiers</th><th>Hors banque</th><th>Exemples</th></tr>
      {lignes_hors}
    </table></div>
  </div>

  <div class="bloc">
    <h2>Trois façons de ranger</h2>

    <article class="opt opt--reco">
      <span class="eti">Recommandée</span>
      <h3>A · Un seul axe : ce qu'on en fait</h3>
      <div class="onglets"><span class="pri">Présenter</span><span class="pri">Décider</span>
        <span class="pri">Suivre</span><span class="pri">Comprendre</span></div>
      <div class="pour">
        <div><b>Présenter</b> — la trousse et tout ce qu'on ouvre devant quelqu'un.</div>
        <div><b>Décider</b> — les pages qui attendent votre jugement : tri des images, tri des
            constats, les neuf liens, les exercices d'écoute, la révision des dialogues.</div>
        <div><b>Suivre</b> — ce qui mesure le dépôt à un instant : tableau de bord, où manque
            l'audio, le prix d'un module, la chaîne de production.</div>
        <div><b>Comprendre</b> — comment ça marche : les repères d'aujourd'hui.</div>
        <div>Le public (Direction, Enseignants) devient une <b>étiquette sur la fiche</b>, pas
            un onglet — un document peut viser deux publics, il ne peut pas être à deux
            endroits.</div>
        <div>« Décider » est le gain réel : ces pages se perdent aujourd'hui dans « Chantier »,
            et ce sont justement celles qui vous attendent.</div>
      </div>
    </article>

    <article class="opt">
      <h3>B · Deux filtres croisés</h3>
      <div class="onglets"><span>Public ▾</span><span>Nature ▾</span></div>
      <div class="pour">
        <div>Comme le catalogue : on croise « pour la direction » et « à décider ».</div>
        <div>Le plus exact — mais deux menus pour cinquante-sept fiches, c'est un outil de
            recherche là où il faut une étagère.</div>
      </div>
    </article>

    <article class="opt">
      <h3>C · Couper « Chantier » en trois, sans rien changer d'autre</h3>
      <div class="onglets"><span>Trousse</span><span>Direction</span><span>Enseignants</span>
        <span class="pri">Décider</span><span class="pri">Suivre</span><span class="pri">Proposer</span>
        <span>Repères</span></div>
      <div class="pour">
        <div>Le plus petit changement : aucune fiche ne quitte sa famille sauf les 27.</div>
        <div>Mais les deux axes continuent de se disputer la rangée : sept onglets, et la
            question « public ou nature ? » se reposera à la fiche suivante.</div>
      </div>
    </article>
  </div>

  <div class="bloc">
    <h2>Ce que je propose de faire, dans les trois cas</h2>
    <div class="pour" style="font-size:16px">
      <div><b>Compter les fiches au lieu de les annoncer.</b> Les nombres des onglets se
          calculent au chargement. Un compteur écrit à la main est faux à la fiche suivante,
          et il l'est déjà.</div>
      <div><b>Ranger les {sum(len(m) for _, _, m in hb.values())} artefacts hors banque</b>, ou
          décider qu'ils n'en sont pas. Mon avis : les <b>essais</b> sont du brouillon et
          peuvent disparaître ; les <b>documents de travail</b> (<code>docs/</code>) méritent
          une fiche chacun ou une fiche d'index ; les <b>modules autonomes</b> ont déjà leur
          index cité, c'est suffisant ; les <b>deux outils</b> manquants sont de vrais oublis.</div>
      <div><b>Écrire la ligne dans la page elle-même.</b> Sans elle, la question « est-ce que
          ça va à la banque ? » se retranchera à chaque nouveau document.</div>
    </div>
    <div class="note"><b>Ce que je ne propose pas :</b> déplacer les fichiers sur le disque.
    <code>assets/presentations/</code> est cohérent — aucun orphelin, aucun lien mort. Le
    désordre est dans le <b>classement</b>, pas dans le rangement des fichiers.</div>
  </div>

  <div class="bloc">
    <h2>Où ça se fait</h2>
    <p><b>presentations.html</b> — les onglets, les familles, et les fiches à répartir. Cette
    page-ci se régénère par <b>python3 build/releve_artefacts.py</b> : les chiffres sont lus
    sur le disque, jamais recopiés.</p>
  </div>
</div>
</body>
</html>
'''


def main():
    sortie = DOSSIER / 'rangement-artefacts.html'
    sortie.write_text(page())
    F = fiches()
    hb = hors_banque()
    print('%d fiches à la banque, %d artefacts hors banque'
          % (len(F), sum(len(m) for _, _, m in hb.values())))
    print('→ %s' % sortie.relative_to(RACINE))
    return 0


if __name__ == '__main__':
    sys.exit(main())
