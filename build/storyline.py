#!/usr/bin/env python3
"""
Produit un parcours autonome à partir du gabarit commun et de son contenu.

    python3 build/storyline.py n5-rendezvous-defi1
    python3 build/storyline.py --tous
    python3 build/storyline.py --tous --verifier   # ne réécrit rien, signale

Où vivent les choses
--------------------
- `build/gabarit/storyline.html` — le moteur, commun à tous les parcours, percé
  de jetons `%%NOM%%`. Il ne connaît que des écrans : une liste de données, un
  type par écran, une mise en page par type.
- `build/contenu/<module>/storyline.js` — le contenu : `const PARCOURS = {…}`
  (l'identité) et `const ECRANS = [ … ]` (les écrans). Un seul fichier à écrire
  pour un parcours de plus.
- `modules-autonomes/<slug>/index.html` — le produit.

**Ne jamais éditer le HTML produit** : la prochaine construction l'écrase. Une
refonte a déjà été perdue ainsi dans ce dépôt. Toute correction se fait dans
`build/`.

Les médias ne sont **jamais copiés**. Un parcours rejoue les extraits du module
de classe correspondant, par chemin absolu — `/assets/interactive/<module>/`.
C'est ce qui rend la démo gratuite : les 267 MP3 du module `rendezvous` sont
déjà produits, et le gel des MP3 tient.

Ce que le script fait, dans l'ordre
-----------------------------------
1. Lit `storyline.js`, en extrait `PARCOURS` et `ECRANS` — le JS est du JSON
   assez proche pour être relu par `json5_ish()`, qui ne sert qu'ici.
2. Contrôle ce qui casserait chez l'élève sans casser la construction :
   un type d'écran inconnu, un identifiant en double, une vérification sans
   bonne réponse, un extrait sonore absent du disque.
3. Remplit le gabarit, vérifie qu'aucun jeton ne survit, et écrit.
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GABARIT = ROOT / 'build' / 'gabarit' / 'storyline.html'
CONTENU = ROOT / 'build' / 'contenu'
SORTIE = ROOT / 'modules-autonomes'

# Les types que le gabarit sait dessiner. Un type absent d'ici s'affiche chez
# l'élève comme une erreur visible — mais autant l'attraper à la construction.
TYPES = ('notion', 'verif')

# La couleur d'un parcours est celle de son niveau, comme pour les modules :
# les jetons `--niv-N-line` / `--niv-N-bg` de assets/design-system/tokens/colors.css.
COULEURS = {
    1: ('#A5335F', '#FBE4EC', '#7C2145'),
    2: ('#B45309', '#FBEEDC', '#7A3806'),
    3: ('#7E3F98', '#F1E7F6', '#5B2A70'),
    4: ('#1D6B8F', '#E7F0F6', '#134F6B'),
    5: ('#0D7A6F', '#DCF2EF', '#08463F'),
    6: ('#1D6B8F', '#E7F0F6', '#134F6B'),
    7: ('#A5335F', '#FBE4EC', '#7C2145'),
    8: ('#17181A', '#EEEEEC', '#000000'),
}


def fatal(msg):
    sys.exit('!! %s' % msg)


def lire_bloc(js, nom):
    """Extrait `const NOM = …;` d'un fichier de contenu, en JSON.

    Le contenu est écrit en JavaScript — c'est plus lisible pour du texte
    pédagogique, ça accepte les commentaires et la concaténation de chaînes,
    et c'est la convention des sept fichiers de contenu d'un module. Ce qui se
    lit ici est donc un sous-ensemble : objets, tableaux, chaînes simples ou
    doubles, booléens, nombres, et `'a' + "b"` sur plusieurs lignes.
    """
    m = re.search(r'^const\s+%s\s*=\s*' % nom, js, re.M)
    if not m:
        return None
    i = m.end()
    ouvre = js[i]
    ferme = {'{': '}', '[': ']'}.get(ouvre)
    if not ferme:
        fatal('%s ne commence ni par { ni par [' % nom)

    # Balayage caractère par caractère : il faut ignorer ce qui est dans une
    # chaîne (les accolades d'un `<b>{`) et dans un commentaire.
    prof, j, dans, ech = 0, i, None, False
    while j < len(js):
        c = js[j]
        if dans:
            if ech:
                ech = False
            elif c == '\\':
                ech = True
            elif c == dans:
                dans = None
        elif c in '"\'':
            dans = c
        elif js.startswith('//', j):
            j = js.find('\n', j)
            if j == -1:
                break
            continue
        elif c == ouvre:
            prof += 1
        elif c == ferme:
            prof -= 1
            if prof == 0:
                return json_du_js(js[i:j + 1])
        j += 1
    fatal('%s n\'est pas refermé' % nom)


def json_du_js(src):
    """Le sous-ensemble de JavaScript ci-dessus, rendu en objet Python."""
    out, i, dans, ech, tampon = [], 0, None, False, []
    while i < len(src):
        c = src[i]
        if dans:
            if ech:
                tampon.append(c)
                ech = False
            elif c == '\\':
                tampon.append(c)
                ech = True
            elif c == dans:
                # Fin de chaîne : on regarde si un `+` la prolonge.
                reste = src[i + 1:]
                suite = re.match(r'\s*\+\s*(["\'])', reste)
                if suite:
                    dans = suite.group(1)
                    i += 1 + suite.end()
                    continue
                out.append(json.dumps(''.join(tampon)
                                      .replace('\\"', '"').replace("\\'", "'")))
                tampon, dans = [], None
            else:
                tampon.append(c)
            i += 1
            continue

        if src.startswith('//', i):
            i = src.find('\n', i)
            if i == -1:
                break
            continue
        if c in '"\'':
            dans, tampon = c, []
            i += 1
            continue
        out.append(c)
        i += 1

    txt = ''.join(out)
    txt = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', txt)  # clés nues
    txt = re.sub(r',\s*([}\]])', r'\1', txt)                                 # virgule finale
    try:
        return json.loads(txt)
    except json.JSONDecodeError as e:
        fatal('contenu illisible (%s)\n%s' % (e, txt[max(0, e.pos - 120):e.pos + 120]))


def controler(parcours, ecrans, module):
    """Ce qui casserait chez l'élève sans casser la construction."""
    ecarts = []
    vus = set()
    for k, e in enumerate(ecrans, 1):
        ou = 'écran %d (%s)' % (k, e.get('id', 'sans id'))
        if not e.get('id'):
            ecarts.append('%s : pas d\'identifiant — le suivi ne peut rien noter' % ou)
        elif e['id'] in vus:
            ecarts.append('%s : identifiant en double — le suivi confondrait les deux' % ou)
        else:
            vus.add(e['id'])

        if e.get('type') not in TYPES:
            ecarts.append('%s : type « %s » inconnu (connus : %s)'
                          % (ou, e.get('type'), ', '.join(TYPES)))

        if e.get('type') == 'verif':
            justes = [o for o in e.get('options', []) if o.get('juste')]
            if len(justes) != 1:
                ecarts.append('%s : %d bonne(s) réponse(s), il en faut exactement une'
                              % (ou, len(justes)))
            for o in e.get('options', []):
                if not o.get('juste') and not o.get('rat'):
                    ecarts.append('%s : l\'option « %s » n\'a pas de rattrapage'
                                  % (ou, o.get('txt', '')[:40]))
            if not e.get('pourquoi'):
                ecarts.append('%s : pas de `pourquoi` — la réponse tomberait sans explication' % ou)

        for s in e.get('sons', []):
            f = ROOT / 'assets' / 'interactive' / module / s['fichier']
            if not f.exists():
                ecarts.append('%s : extrait absent du disque — %s' % (ou, s['fichier']))
    return ecarts


def construire(dossier, verifier=False):
    js = (dossier / 'storyline.js')
    if not js.exists():
        fatal('pas de storyline.js dans %s' % dossier)
    src = js.read_text(encoding='utf-8')

    parcours = lire_bloc(src, 'PARCOURS')
    ecrans = lire_bloc(src, 'ECRANS')
    if parcours is None or ecrans is None:
        fatal('%s : il faut `const PARCOURS = {…}` et `const ECRANS = [ … ]`' % js)

    module = parcours.get('module') or dossier.name
    ecarts = controler(parcours, ecrans, module)
    if ecarts:
        for e in ecarts:
            print('  ÉCART  %s' % e)
        fatal('%d écart(s) — rien n\'est écrit' % len(ecarts))

    acc, doux, fonce = COULEURS.get(parcours.get('niveau', 5), COULEURS[5])
    gab = GABARIT.read_text(encoding='utf-8')
    jetons = {
        '%%TITRE%%':         parcours['titre'],
        '%%SUR_TITRE%%':     parcours.get('surtitre', ''),
        '%%SLUG%%':          parcours['slug'],
        '%%MEDIA%%':         '/assets/interactive/%s/' % module,
        '%%RETOUR%%':        '../index.html',
        '%%ACCENT%%':        acc,
        '%%ACCENT_DOUX%%':   doux,
        '%%ACCENT_FONCE%%':  fonce,
        '%%ECRANS%%':        json.dumps(ecrans, ensure_ascii=False, indent=2),
    }
    for k, v in jetons.items():
        gab = gab.replace(k, v)

    reste = re.findall(r'%%[A-Z_]+%%', gab)
    if reste:
        fatal('jeton(s) non remplis : %s' % ', '.join(sorted(set(reste))))

    cible = SORTIE / parcours['slug'] / 'index.html'
    if verifier:
        etat = 'à jour' if cible.exists() and cible.read_text(encoding='utf-8') == gab \
               else 'À RECONSTRUIRE'
        print('  %-26s %2d écran(s)  %s' % (parcours['slug'], len(ecrans), etat))
        return etat != 'à jour'

    cible.parent.mkdir(parents=True, exist_ok=True)
    cible.write_text(gab, encoding='utf-8')
    print('  %-26s %2d écran(s)  → %s'
          % (parcours['slug'], len(ecrans), cible.relative_to(ROOT)))
    return False


def dossiers():
    """Les modules qui ont un parcours, dans l'ordre."""
    return sorted(d for d in CONTENU.iterdir() if (d / 'storyline.js').exists())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('slug', nargs='?', help='le slug du parcours, ou le module qui le porte')
    ap.add_argument('--tous', action='store_true')
    ap.add_argument('--verifier', action='store_true',
                    help='ne réécrit rien ; code 1 si un parcours est à reconstruire')
    a = ap.parse_args()

    if not a.tous and not a.slug:
        ap.error('donne un slug, ou --tous')

    cibles = dossiers()
    if not a.tous:
        cibles = [d for d in cibles
                  if d.name == a.slug
                  or a.slug in (lire_bloc((d / 'storyline.js').read_text(encoding='utf-8'),
                                          'PARCOURS') or {}).get('slug', '')]
        if not cibles:
            fatal('aucun parcours nommé « %s »' % a.slug)

    print('Parcours autonomes :')
    ecart = False
    for d in cibles:
        ecart = construire(d, a.verifier) or ecart
    sys.exit(1 if (a.verifier and ecart) else 0)


if __name__ == '__main__':
    main()
