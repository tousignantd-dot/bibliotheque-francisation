#!/usr/bin/env python3
"""
Produit un module interactif à partir du gabarit commun et de son contenu.

    python3 build/module.py module-probleme
    python3 build/module.py --tous

Où vivent les choses
--------------------
- `build/gabarit/module.html` — le moteur, commun aux dix-huit modules, percé
  de jetons `%%NOM%%`. Produit par `build/gabarit.py`, jamais écrit à la main.
- `build/contenu/<slug>/manifest.py` — l'identité du module : titre, niveau,
  couleur, thème LMS, consignes de correction, scénario du jeu de rôle.
- `build/contenu/<slug>/*.js` — le contenu pédagogique : `dialogues`,
  `sections`, `fccards`, `exos`, `carrier`, `plus`, `custom`.

**Ne jamais éditer le HTML produit** : la prochaine construction l'écrase. Une
refonte a déjà été perdue ainsi. Toute correction se fait dans `build/`.

Ce que le script fait, dans l'ordre
-----------------------------------
1. Lit le gabarit et remplit ses jetons avec le manifeste et les fichiers `.js`.
2. Applique les quatre greffes partagées — barre d'outils, dépôt de l'écrit,
   verrou des sections datées, reprise de séance. Chacune commence par retirer
   celle du gabarit, qui porte le slug de la consultation.
3. Vérifie qu'aucun résidu du gabarit ne survit, puis écrit le fichier.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
BUILD = ROOT / 'build'
GABARIT = BUILD / 'gabarit/module.html'
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


def charger_manifeste(slug):
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
    return m


def construire(slug, verbeux=True):
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
        '%%TITRE%%':         man['titre'],
        '%%THEME%%':         man['theme'],
        '%%ACCENT%%':        man['accent'],
        '%%ACCENT_DOUX%%':   man['accent_doux'],
        '%%IA_ORAL%%':       man['ia_oral'],
        '%%JR_CAS%%':        man['jr_cas'],
        '%%JR_SCENARIO%%':   man['jr_scenario'],
        '%%IA_JEU_DE_ROLE%%': man['ia_jeu_de_role'],
        '%%BRAVO%%':         man['bravo'],
        '%%RELANCE%%':       man['relance'],
    }
    for jeton, valeur in valeurs.items():
        html = html.replace(jeton, valeur)

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

    ids = activites_par_slug()
    if slug not in ids:
        fatal('%s est absent de data/activities.json : le verrou des sections '
              'ne saurait pas quoi demander au serveur' % slug)

    for nom, fonction, argument in [
            ("barre d'outils",      greffe_outils,      slug),
            ("dépôt de l'écrit",    greffe_depot_ecrit, slug),
            ('verrou des sections', greffe_sections,    ids[slug]),
            ('reprise de séance',   greffe_reprise,     slug)]:
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
    a = p.parse_args()

    if a.tous:
        dispo = modules_disponibles()
        if not dispo:
            fatal('aucun module dans %s' % CONTENU)
        for slug in dispo:
            construire(slug)
        print('\n%d modules construits.' % len(dispo))
    elif a.slug:
        construire(a.slug)
    else:
        print(__doc__)
        print('Modules disponibles : %s' % (', '.join(modules_disponibles()) or '(aucun)'))


if __name__ == '__main__':
    main()
