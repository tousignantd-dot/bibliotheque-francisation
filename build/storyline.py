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
- Le contenu, dans l'un des deux endroits, selon ce que le parcours est :
  - `build/parcours/<slug>.js` — un **parcours de remédiation**, rangé par
    savoir du programme et non par situation. Il ne dépend d'aucun module ;
    l'enseignant l'envoie à un élève chez qui il a constaté la lacune.
  - `build/contenu/<module>/storyline.js` — un parcours **attaché à un
    module**, qui en reprend une section.

  Les deux portent `const PARCOURS = {…}` (l'identité) et `const ECRANS = [ … ]`
  (les écrans). Un seul fichier à écrire pour un parcours de plus.
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
PARCOURS_DIR = ROOT / 'build' / 'parcours'
SORTIE = ROOT / 'modules-autonomes'
# Le registre que le serveur lit pour offrir l'étagère à l'enseignant. Produit,
# versionné, lu depuis BASE_DIR : il décrit ce que le code livre, comme
# `data/sections.json` et `data/materiel.json`. Jamais écrit à la main.
REGISTRE = ROOT / 'data' / 'points_express.json'

# Les types que le gabarit sait dessiner. Un type absent d'ici s'affiche chez
# l'élève comme une erreur visible — mais autant l'attraper à la construction.
#   notion — ce qu'il faut savoir, en un écran
#   verif  — une question, un rattrapage par mauvaise réponse
#   tri    — trancher des cas AVANT qu'aucune règle ne soit dite
TYPES = ('notion', 'verif', 'tri')

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
    """Le sous-ensemble de JavaScript ci-dessus, rendu en objet Python.

    Le texte se range en DEUX TAS : le code (accolades, virgules, clés nues) et
    les chaînes, déjà rendues en littéraux JSON. Les deux réécritures qui
    suivent — requoter les clés nues, retirer la virgule finale — ne touchent
    que le code.

    Les faire sur le texte entier corrompait le contenu, et silencieusement :
    un titre comme « ce, cet, cette : trois mots » porte une virgule, un mot et
    un deux-points, donc exactement le motif d'une clé nue. Il ressortait
    requoté au milieu de la phrase, et `json.loads` mourait sur un titre
    parfaitement valide — l'erreur montrait le titre, jamais la réécriture.
    """
    morceaux, code = [], []
    i, dans, ech, tampon = 0, None, False, []

    def vider_code():
        if code:
            morceaux.append(('code', ''.join(code)))
            del code[:]

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
                vider_code()
                morceaux.append(('chaine', json.dumps(''.join(tampon)
                                 .replace('\\"', '"').replace("\\'", "'"))))
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
        code.append(c)
        i += 1
    vider_code()

    bouts = []
    for quoi, t in morceaux:
        if quoi == 'code':
            t = re.sub(r'([{,]\s*)([A-Za-z_][A-Za-z0-9_]*)\s*:', r'\1"\2":', t)  # clés nues
            t = re.sub(r',\s*([}\]])', r'\1', t)                                 # virgule finale
        bouts.append(t)
    txt = ''.join(bouts)
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

        if e.get('type') == 'tri':
            cols = [c.get('id') for c in e.get('colonnes', [])]
            if len(cols) < 2:
                ecarts.append('%s : un tri veut au moins deux colonnes' % ou)
            if len(set(cols)) != len(cols):
                ecarts.append('%s : deux colonnes portent le même identifiant' % ou)
            if not e.get('items'):
                ecarts.append('%s : un tri sans cas à trancher' % ou)
            for it in e.get('items', []):
                if it.get('ok') not in cols:
                    ecarts.append('%s : le cas « %s » range dans une colonne qui n\'existe pas'
                                  % (ou, str(it.get('txt'))[:30]))
                if not it.get('rat'):
                    ecarts.append('%s : le cas « %s » n\'a pas de rattrapage'
                                  % (ou, str(it.get('txt'))[:30]))

        for im in e.get('images', []):
            if not module:
                ecarts.append('%s : une image, mais le parcours ne dit de quel module '
                              'il la tire (champ `module`)' % ou)
                continue
            f = ROOT / 'assets' / 'interactive' / module / im['fichier']
            if not f.exists():
                ecarts.append('%s : image absente du disque — %s' % (ou, im['fichier']))
            if not im.get('alt'):
                ecarts.append('%s : image sans texte de remplacement — %s'
                              % (ou, im['fichier']))

        for s in e.get('sons', []):
            if not module:
                ecarts.append('%s : un extrait sonore, mais le parcours ne dit de quel module '
                              'il le tire (champ `module`)' % ou)
                continue
            f = ROOT / 'assets' / 'interactive' / module / s['fichier']
            if not f.exists():
                ecarts.append('%s : extrait absent du disque — %s' % (ou, s['fichier']))
    return ecarts


def construire(js, verifier=False):
    if not js.exists():
        fatal('fichier de contenu introuvable : %s' % js)
    src = js.read_text(encoding='utf-8')

    parcours = lire_bloc(src, 'PARCOURS')
    ecrans = lire_bloc(src, 'ECRANS')
    if parcours is None or ecrans is None:
        fatal('%s : il faut `const PARCOURS = {…}` et `const ECRANS = [ … ]`' % js)

    # Un parcours de remédiation ne dépend d'aucun module : il n'a de `module`
    # que s'il rejoue les extraits de l'un d'eux.
    module = parcours.get('module') or ''
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
        '%%MEDIA%%':         ('/assets/interactive/%s/' % module) if module else '/',
        '%%RETOUR%%':        '../index.html',
        '%%ACCENT%%':        acc,
        '%%ACCENT_DOUX%%':   doux,
        '%%ACCENT_FONCE%%':  fonce,
        '%%ECRANS%%':        json.dumps(ecrans, ensure_ascii=False, indent=2),
        # Les langues d'appui, déclarées par le contenu. Vide par défaut : les
        # points express de la gamme scolaire n'en offrent aucune, et le
        # sélecteur ne se construit pas. Le contenu à apprendre ne bascule
        # jamais — seuls les champs d'appui d'un écran (`es`, `en`, …).
        '%%APPUI%%':         json.dumps(parcours.get('appui', []), ensure_ascii=False),
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


def registre(verifier=False):
    """Écrit `data/points_express.json` — l'étagère, telle que le serveur la voit.

    Seuls les **points express** y figurent : un parcours attaché à un module
    n'est pas une ordonnance, il ne s'envoie pas.
    """
    liste = []
    for f in sorted(PARCOURS_DIR.glob('*.js')) if PARCOURS_DIR.exists() else []:
        src = f.read_text(encoding='utf-8')
        p = lire_bloc(src, 'PARCOURS') or {}
        e = lire_bloc(src, 'ECRANS') or []
        liste.append({
            'slug': p.get('slug', f.stem),
            'titre': p.get('titre', f.stem),
            'savoir': p.get('savoir', ''),
            'niveau': p.get('niveau'),
            'ecrans': len(e),
            'minutes': 10,
            'fichier': 'modules-autonomes/%s/index.html' % p.get('slug', f.stem),
        })
    texte = json.dumps(liste, ensure_ascii=False, indent=2) + '\n'
    if verifier:
        actuel = REGISTRE.read_text(encoding='utf-8') if REGISTRE.exists() else ''
        return actuel != texte
    REGISTRE.parent.mkdir(parents=True, exist_ok=True)
    REGISTRE.write_text(texte, encoding='utf-8')
    return False


def fichiers():
    """Tous les contenus de parcours, les remédiations d'abord."""
    liste = sorted(PARCOURS_DIR.glob('*.js')) if PARCOURS_DIR.exists() else []
    liste += sorted(d / 'storyline.js' for d in CONTENU.iterdir()
                    if (d / 'storyline.js').exists())
    return liste


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

    cibles = fichiers()
    if not a.tous:
        cibles = [f for f in cibles
                  if f.stem == a.slug or f.parent.name == a.slug
                  or a.slug == (lire_bloc(f.read_text(encoding='utf-8'),
                                          'PARCOURS') or {}).get('slug', '')]
        if not cibles:
            fatal('aucun parcours nommé « %s »' % a.slug)

    print('Parcours autonomes :')
    ecart = False
    for d in cibles:
        ecart = construire(d, a.verifier) or ecart

    # Le registre se refait dès qu'on touche à un parcours : un envoi qui
    # pointerait vers un point disparu serait un cul-de-sac chez l'élève.
    if a.tous:
        if registre(a.verifier):
            print('  ÉCART  data/points_express.json est à refaire')
            ecart = True
        elif not a.verifier:
            print('  %-26s %2d point(s) express'
                  % ('data/points_express.json',
                     len(json.loads(REGISTRE.read_text(encoding='utf-8')))))
    sys.exit(1 if (a.verifier and ecart) else 0)


if __name__ == '__main__':
    main()
