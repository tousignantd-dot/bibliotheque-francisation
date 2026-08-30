#!/usr/bin/env python3
"""
Produit un module interactif à partir du gabarit commun et de son contenu.

    python3 build/module.py module-probleme
    python3 build/module.py --tous

Où vivent les choses
--------------------
- `build/gabarit/module.html` — le moteur, commun aux dix-huit modules, percé
  de jetons `%%NOM%%`. Produit par `build/gabarit.py`, jamais écrit à la main.
- `build/contenu/<slug>/manifest.py` — l'identité du module : couleur, thème
  LMS, consignes de correction, scénario du jeu de rôle. **Ni le titre ni le
  niveau** : ils viennent du registre `build/powerpoints/modules.py`.
- `build/contenu/<slug>/*.js` — le contenu pédagogique : `dialogues`,
  `sections`, `fccards`, `exos`, `carrier`, `plus`, `custom`.

**Ne jamais éditer le HTML produit** : la prochaine construction l'écrase. Une
refonte a déjà été perdue ainsi. Toute correction se fait dans `build/`.

Ce que le script fait, dans l'ordre
-----------------------------------
1. Lit le gabarit et remplit ses jetons avec le manifeste et les fichiers `.js`.
2. Applique les cinq greffes partagées — barre d'outils, dépôt de l'écrit,
   verrou des sections datées, reprise de séance, identité de marque. Chacune
   commence par retirer celle du gabarit, qui porte le slug de la consultation.
3. Vérifie qu'aucun résidu du gabarit ne survit, puis écrit le fichier.
"""
import argparse
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / 'build'
GABARIT_DIR = BUILD / 'gabarit'
GABARIT = GABARIT_DIR / 'module.html'
CONTENU = BUILD / 'contenu'

sys.path.insert(0, str(BUILD))

# Les régions de contenu : jeton → fichier qui le remplit.
REGIONS = {
    '%%DIALOGUES%%':       ('dialogues.js', 'const DIALOGUES = '),
    '%%SECTIONS%%':        ('sections.js',  'const SECTIONS = '),
    '%%FC_CARDS%%':        ('fccards.js',   'const FC_CARDS = '),
    '%%EXOS%%':            ('exos.js',      'const EXOS = '),
    '%%CARRIER_PHRASES%%': ('carrier.js',   'const CARRIER_PHRASES = '),
    '%%PLUS%%':            ('plus.js',      'const PLUS = '),
    '%%CUSTOM%%':          ('custom.js',    ''),
}


def fatal(msg):
    sys.exit('!! %s' % msg)


def repere(man):
    """« Module 12 · Niveau 3 », le repère de l'en-tête.

    L'élève ouvre son module depuis le portail, depuis un signet, ou parce
    qu'un voisin lui a passé l'adresse : rien à l'écran ne lui disait jusqu'ici
    lequel des cinquante-huit il a sous les yeux, ni à quel niveau il se
    trouve. L'enseignant non plus, quand il projette.

    Le numéro et le niveau viennent du registre `build/powerpoints/modules.py`,
    qui fait foi — jamais du manifeste, qui ferait une source de plus. Un
    module absent du registre n'a pas encore de numéro : on affiche alors le
    seul niveau plutôt que rien.

    **Conséquence à connaître** : le numéro est désormais écrit *dans* le
    module. Renuméroter un niveau obligeait déjà à régénérer les PowerPoints ;
    il faut maintenant régénérer les modules aussi.
    """
    niveau = 'Niveau %s' % man['niveau']
    numero = man.get('numero')
    return ('Module %s · %s' % (numero, niveau)) if numero else niveau


def charger_manifeste(slug):
    """Le manifeste du module, complété par le registre.

    `titre` et `niveau` viennent de `build/powerpoints/modules.py`, qui se
    déclare source unique et les porte déjà. Un manifeste qui les redéfinirait
    ferait une source de plus — c'est exactement le défaut de numérotation à
    trois sources que ce projet traîne déjà. Le manifeste ne les porte donc que
    pour un module absent du registre, et le build refuse une redéfinition qui
    contredirait celui-ci.
    """
    chemin = CONTENU / slug / 'manifest.py'
    if not chemin.exists():
        fatal('%s : manifeste introuvable (%s)' % (slug, chemin))
    espace = {}
    exec(compile(chemin.read_text(encoding='utf-8'), str(chemin), 'exec'), espace)
    m = espace.get('MANIFESTE')
    if not isinstance(m, dict):
        fatal('%s : le manifeste ne définit pas MANIFESTE' % slug)
    if m.get('slug') != slug:
        fatal('%s : le manifeste annonce le slug %r' % (slug, m.get('slug')))

    sys.path.insert(0, str(BUILD / 'powerpoints'))
    from modules import MODULES
    entree = MODULES.get(slug)
    for champ in ('titre', 'niveau', 'numero'):
        if entree and champ in entree:
            if champ in m and m[champ] != entree[champ]:
                fatal('%s : le manifeste dit %s=%r, le registre %r — '
                      'retirer le champ du manifeste, le registre fait foi'
                      % (slug, champ, m[champ], entree[champ]))
            m[champ] = entree[champ]
        elif champ not in m:
            if champ == 'numero':
                # Un module qu'on est en train d'écrire n'est pas encore au
                # registre. Il se construit quand même : l'en-tête se passera
                # de son numéro plutôt que d'empêcher l'aperçu.
                continue
            fatal('%s : %s absent du manifeste et du registre '
                  'build/powerpoints/modules.py' % (slug, champ))
    return m


def construire(slug, verbeux=True, gabarit=None):
    """`gabarit` permet de bâtir sur une autre copie du moteur que celle du
    dépôt — utile quand une autre session est en train d'en modifier une, pour
    ne pas embarquer son travail en cours dans un commit."""
    global GABARIT
    if gabarit:
        GABARIT = pathlib.Path(gabarit)
    if not GABARIT.exists():
        fatal('gabarit absent — lancer d\'abord : python3 build/gabarit.py')
    html = GABARIT.read_text(encoding='utf-8')
    gab_len = len(html)
    man = charger_manifeste(slug)
    dossier = CONTENU / slug

    # ── 1. Contenu ───────────────────────────────────────────────────
    for jeton, (fichier, prefixe) in REGIONS.items():
        if jeton not in html:
            fatal('%s : jeton %s absent du gabarit' % (slug, jeton))
        chemin = dossier / fichier
        if not chemin.exists():
            fatal('%s : %s manquant' % (slug, fichier))
        texte = chemin.read_text(encoding='utf-8').strip()
        if prefixe and not texte.startswith(prefixe):
            fatal('%s : %s ne commence pas par %r' % (slug, fichier, prefixe))
        html = html.replace(jeton, texte)

    # ── 2. Identité ──────────────────────────────────────────────────
    valeurs = {
        '%%SLUG%%':          man['slug'],
        '%%NIVEAU%%':        str(man['niveau']),
        '%%REPERE%%':        repere(man),
        '%%TITRE%%':         man['titre'],
        '%%TITRE_MAJ%%':     man['titre'].upper(),
        '%%THEME%%':         man['theme'],
        '%%ACCENT%%':        man['accent'],
        '%%ACCENT_DOUX%%':   man['accent_doux'],
        '%%IA_ORAL%%':       man['ia_oral'],
        '%%JR_CAS%%':        man['jr_cas'],
        '%%JR_ROLE%%':       man.get('jr_role', 'locataire'),
        '%%JR_SCENARIO%%':   man['jr_scenario'],
        '%%IA_JEU_DE_ROLE%%': man['ia_jeu_de_role'],
        '%%BRAVO%%':         man['bravo'],
        '%%RELANCE%%':       man['relance'],
    }
    for jeton, valeur in valeurs.items():
        html = html.replace(jeton, valeur)

    # Certaines valeurs du manifeste finissent dans une chaîne JavaScript à
    # guillemets simples (`fd.append('theme','%%THEME%%')`, l'écran de fin…).
    # Une apostrophe non échappée y casse tout le script du module — et la page
    # continue de s'afficher, muette. Plutôt que de tenir une liste de champs à
    # la main, on regarde le gabarit : si le jeton y est entouré de guillemets
    # simples, la valeur doit être échappée.
    gabarit_src = GABARIT.read_text(encoding='utf-8')
    for jeton, valeur in valeurs.items():
        if not isinstance(valeur, str):
            continue
        entre_apostrophes = False
        for m in re.finditer(re.escape(jeton), gabarit_src):
            avant = gabarit_src[m.start() - 1:m.start()]
            apres = gabarit_src[m.end():m.end() + 1]
            if avant == "'" and apres == "'":
                entre_apostrophes = True
                break
        if entre_apostrophes and re.search(r"(?<!\\)'", valeur):
            fatal("%s : la valeur de %s contient une apostrophe non échappée "
                  "— écrire \\\\' dans le manifeste. Le gabarit place ce jeton "
                  "dans une chaîne JavaScript à guillemets simples." % (slug, jeton))

    restants = sorted(set(re.findall(r'%%[A-Z_]+%%', html)))
    if restants:
        fatal('%s : jetons non remplis — %s' % (slug, ' '.join(restants)))

    # ── 3. Greffes partagées ─────────────────────────────────────────
    # Chacune retire d'abord celle du gabarit, qui porte le slug — ou le
    # numéro d'activité — de la consultation. Sans ce dégreffage, le module
    # hériterait du carnet, du dépôt et du verrou d'un autre.
    from greffe_outils import greffe as greffe_outils
    from greffe_depot_ecrit import greffe as greffe_depot_ecrit
    from greffe_sections import greffe as greffe_sections, activites_par_slug
    from greffe_reprise import greffe as greffe_reprise
    from greffe_marque import greffe as greffe_marque
    from greffe_transcription import greffe as greffe_transcription

    ids = activites_par_slug()
    if slug not in ids:
        fatal('%s est absent de data/activities.json : le verrou des sections '
              'ne saurait pas quoi demander au serveur' % slug)

    for nom, fonction, argument in [
            ("barre d'outils",      greffe_outils,      slug),
            ("dépôt de l'écrit",    greffe_depot_ecrit, slug),
            ('verrou des sections', greffe_sections,    ids[slug]),
            ('reprise de séance',   greffe_reprise,     slug),
            ('identité de marque',  greffe_marque,      slug),
            ('verrou de transcription', greffe_transcription, slug)]:
        try:
            html = fonction(html, argument)
        except ValueError as e:
            fatal('%s : greffe « %s » impossible — %s' % (slug, nom, e))

    # ── 4. Filet de sécurité ─────────────────────────────────────────
    residus = []
    for mot in man.get('residus_interdits', []):
        n = html.count(mot)
        if n:
            residus.append('%s (%d)' % (mot, n))
    if residus:
        fatal('%s : résidus du gabarit — %s' % (slug, ', '.join(residus)))

    dst = ROOT / 'assets/interactive' / slug / ('%s-activite-interactive.html' % slug)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(html, encoding='utf-8')

    # Les icônes vont avec le moteur, pas avec le contenu : le gabarit les
    # appelle par `/assets/interactive/<slug>/icons/…`, un chemin qu'il
    # fabrique à partir du slug. Sans cette copie, chaque agent doit y penser
    # — et le 23 août 2026 deux d'entre eux ont signalé les mêmes trois 404,
    # qu'un troisième module traîne depuis sa livraison. Rien ne les montre à
    # l'écran : le bouton reste cliquable, l'image seule manque, et ni le
    # build, ni `coherence.js`, ni le `node --check` ne regardent là.
    for icone in sorted((GABARIT_DIR / 'icons').glob('*.svg')):
        cible = dst.parent / 'icons' / icone.name
        cible.parent.mkdir(parents=True, exist_ok=True)
        if not cible.exists() or cible.read_bytes() != icone.read_bytes():
            shutil.copyfile(icone, cible)
    if verbeux:
        print('OK  %s' % dst)
        print('    gabarit %d octets → module %d octets' % (gab_len, len(html)))
    return dst


def modules_disponibles():
    if not CONTENU.exists():
        return []
    return sorted(d.name for d in CONTENU.iterdir()
                  if (d / 'manifest.py').exists())


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('slug', nargs='?', help='le module à construire')
    p.add_argument('--tous', action='store_true',
                   help='construire tous les modules de build/contenu/')
    p.add_argument('--gabarit',
                   help='bâtir sur une autre copie du moteur que build/gabarit/module.html')
    a = p.parse_args()

    if a.tous:
        dispo = modules_disponibles()
        if not dispo:
            fatal('aucun module dans %s' % CONTENU)
        for slug in dispo:
            construire(slug, gabarit=a.gabarit)
        print('\n%d modules construits.' % len(dispo))
    elif a.slug:
        construire(a.slug, gabarit=a.gabarit)
    else:
        print(__doc__)
        print('Modules disponibles : %s' % (', '.join(modules_disponibles()) or '(aucun)'))


if __name__ == '__main__':
    main()
