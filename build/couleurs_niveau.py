#!/usr/bin/env python3
"""
Aligne la couleur d'en-tête de chaque module sur son niveau.

    python3 build/couleurs_niveau.py             # applique
    python3 build/couleurs_niveau.py --verifier  # signale les écarts, n'écrit rien

Pourquoi ce fichier existe
--------------------------
Jusqu'au 20 août 2026, la couleur d'en-tête d'un module se choisissait à la
main parmi quatre teintes, en évitant seulement de répéter celle du module
voisin dans le catalogue. Le repérage par niveau, lui, vivait dans une échelle
séparée — les jetons `--niv-N-line` / `--niv-N-bg` de
`assets/design-system/tokens/colors.css`. Deux échelles pour une seule idée :
un élève voyait une pastille ambre au catalogue et un en-tête forêt en ouvrant
le module.

Les deux échelles n'en font plus qu'une. **La couleur d'un module est celle de
son niveau**, et rien d'autre ne la décide. Ce script est ce qui le garantit :
il lit les jetons dans `colors.css`, le niveau dans le registre
`build/powerpoints/modules.py`, et pose la paire dans le manifeste du module.

Où il écrit
-----------
- Modules **générés** (ceux qui ont un `build/contenu/<slug>/manifest.py`) :
  il corrige `accent` et `accent_doux` dans le manifeste. Le HTML suit à la
  prochaine construction — `python3 build/module.py --tous`.
- Modules **écrits à la main** (les plus anciens, sans dossier de contenu) :
  il corrige `--hdr-accent` / `--hdr-accent-soft` directement dans le HTML,
  qui est leur seule source.

`--verifier` regarde les deux : les manifestes *et* le HTML produit. C'est ce
qui attrape un module généré dont le manifeste est juste mais qui n'a pas été
reconstruit.
"""
import argparse
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CSS = ROOT / 'assets/design-system/tokens/colors.css'
CONTENU = ROOT / 'build/contenu'
INTERACTIF = ROOT / 'assets/interactive'
ACTIVITES = ROOT / 'data/activities.json'

sys.path.insert(0, str(ROOT / 'build'))


def palette():
    """Les huit paires de l'arc-en-ciel, lues dans colors.css."""
    css = CSS.read_text(encoding='utf-8')
    paires = {}
    for n in range(1, 9):
        line = re.search(r'--niv-%d-line:\s*(#[0-9A-Fa-f]{6})' % n, css)
        bg = re.search(r'--niv-%d-bg:\s*(#[0-9A-Fa-f]{6})' % n, css)
        if not line or not bg:
            sys.exit("!! colors.css : jetons du niveau %d introuvables" % n)
        paires[n] = (line.group(1).upper(), bg.group(1).upper())
    return paires


def registre():
    from powerpoints.modules import MODULES
    return {slug: fiche.get('niveau', 4) for slug, fiche in MODULES.items()}


def activites():
    """Numéro d'activité → niveau, pour la plaquette du portail."""
    from powerpoints.modules import MODULES
    return {fiche['activite']: fiche.get('niveau', 4)
            for fiche in MODULES.values() if 'activite' in fiche}


def pose_plaquette(ecrire, paires, par_activite):
    """Corrige `nouveauDesignColor` / `nouveauDesignTint` dans activities.json.

    La plaquette du portail répète la couleur de l'en-tête. Les deux ont
    toujours dû concorder, et rien ne le garantissait : une couleur changée
    dans le manifeste et oubliée ici faisait mentir le portail. On écrit ligne
    à ligne plutôt que par un aller-retour JSON, pour ne pas reformater les
    seize cents lignes du fichier au passage.
    """
    lignes = ACTIVITES.read_text(encoding='utf-8').split('\n')
    id_courant = None
    ecarts = []
    for i, ligne in enumerate(lignes):
        trouve = re.match(r'\s*"id":\s*(\d+)', ligne)
        if trouve:
            id_courant = int(trouve.group(1))
            continue
        niveau = par_activite.get(id_courant)
        if niveau is None:
            continue
        accent, doux = paires[niveau]
        for cle, valeur in (('nouveauDesignColor', accent),
                            ('nouveauDesignTint', doux)):
            trouve = re.match(r'(\s*"%s":\s*")(#[0-9A-Fa-f]{6})(".*)$' % cle, ligne)
            if trouve and trouve.group(2).upper() != valeur:
                lignes[i] = '%s%s%s' % (trouve.group(1), valeur, trouve.group(3))
                ecarts.append('activité %d — %s (niveau %d → %s)'
                              % (id_courant, cle, niveau, valeur))
    if ecarts and ecrire:
        ACTIVITES.write_text('\n'.join(lignes), encoding='utf-8')
    return ecarts


def html_du_module(slug):
    return INTERACTIF / slug / ('%s-activite-interactive.html' % slug)


def pose_manifeste(slug, accent, doux, ecrire):
    """Corrige `accent` / `accent_doux` dans le manifeste. Rend True si écart."""
    chemin = CONTENU / slug / 'manifest.py'
    texte = chemin.read_text(encoding='utf-8')
    neuf = texte
    for cle, valeur in (('accent', accent), ('accent_doux', doux)):
        motif = re.compile(r"('%s':\s*)'#[0-9A-Fa-f]{6}'" % cle)
        if not motif.search(neuf):
            sys.exit("!! %s : clé '%s' introuvable dans le manifeste" % (slug, cle))
        neuf = motif.sub(lambda m: "%s'%s'" % (m.group(1), valeur), neuf)
    if neuf == texte:
        return False
    if ecrire:
        chemin.write_text(neuf, encoding='utf-8')
    return True


def pose_html(slug, accent, doux, ecrire):
    """Corrige --hdr-accent dans le HTML. Rend True si écart."""
    chemin = html_du_module(slug)
    if not chemin.exists():
        return False
    texte = chemin.read_text(encoding='utf-8')
    motif = re.compile(r'--hdr-accent:\s*#[0-9A-Fa-f]{6};\s*--hdr-accent-soft:\s*#[0-9A-Fa-f]{6};')
    if not motif.search(texte):
        sys.exit("!! %s : --hdr-accent introuvable dans le HTML" % slug)
    neuf = motif.sub('--hdr-accent:%s; --hdr-accent-soft:%s;' % (accent, doux), texte)
    if neuf == texte:
        return False
    if ecrire:
        chemin.write_text(neuf, encoding='utf-8')
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--verifier', action='store_true',
                    help="signale les écarts sans rien écrire")
    args = ap.parse_args()
    ecrire = not args.verifier

    paires = palette()
    niveaux = registre()
    ecarts = pose_plaquette(ecrire, paires, activites())

    for slug in sorted(niveaux):
        niveau = niveaux[slug]
        accent, doux = paires[niveau]
        genere = (CONTENU / slug / 'manifest.py').exists()

        if genere:
            if pose_manifeste(slug, accent, doux, ecrire):
                ecarts.append('%s — manifeste (niveau %d → %s)' % (slug, niveau, accent))
            # Le HTML d'un module généré n'est jamais écrit ici : il se
            # reconstruit. On se contente de dire qu'il est en retard.
            chemin = html_du_module(slug)
            if chemin.exists():
                trouve = re.search(r'--hdr-accent:\s*(#[0-9A-Fa-f]{6})',
                                   chemin.read_text(encoding='utf-8'))
                if trouve and trouve.group(1).upper() != accent:
                    ecarts.append('%s — HTML en retard, à reconstruire' % slug)
        else:
            if pose_html(slug, accent, doux, ecrire):
                ecarts.append('%s — HTML écrit à la main (niveau %d → %s)'
                              % (slug, niveau, accent))

    # Les modules présents sur le disque mais absents du registre n'ont pas de
    # niveau : personne ne peut leur donner une couleur.
    orphelins = sorted(d.name for d in INTERACTIF.iterdir()
                       if d.is_dir() and d.name.startswith('module-')
                       and d.name not in niveaux)

    verbe = 'à corriger' if args.verifier else 'corrigé(s)'
    print('%d module(s) au registre, %d %s.' % (len(niveaux), len(ecarts), verbe))
    for e in ecarts:
        print('  · %s' % e)
    if orphelins:
        print('Hors registre, sans niveau, laissés tels quels :')
        for o in orphelins:
            print('  · %s' % o)
    if args.verifier and ecarts:
        sys.exit(1)


if __name__ == '__main__':
    main()
