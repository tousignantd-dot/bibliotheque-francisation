#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génération de `data/materiel.json` · l'inventaire du dépôt de matériel
======================================================================

    python3 build/materiel.py            → écrit data/materiel.json
    python3 build/materiel.py --verifier → contrôle sans écrire (code 1 si écart)

Ce fichier n'est **jamais écrit à la main**. Il est le relevé de ce qui existe
vraiment sur le disque au moment du build : les présentations de
`assets/powerpoints/<slug>/`, les fiches de `assets/documents/`, les plans de
`assets/plans/`, les vignettes de `assets/vignettes/<slug>/`. Une fiche
inscrite ici mais absente du disque serait un lien mort dans le portail ; un
fichier produit mais non inscrit serait invisible. Le seul moyen de garder les
deux vrais est de les déduire l'un de l'autre.

Trois principes :

1. **Aucun titre d'activité n'est recopié.** Le dépôt ne connaît que des
   `activiteId` — les entiers de `data/activities.json`. Titre, niveau,
   domaine et mots-clés se lisent là-bas, une seule fois.
2. **La grille des séances a une seule source** : `SEANCES` de
   `build/powerpoints/build.py`, l'ordre d'enseignement. Un module sans
   dossier de séances hérite de la grille standard à seize.
3. **Rien de mutable ici.** Les dépôts des enseignants vivent dans
   `data/depots.json`, écrit par le serveur : régénérer l'inventaire ne doit
   jamais effacer le fichier qu'une enseignante a téléversé hier.
"""
import json
import os
import re
import sys
import zipfile
from datetime import datetime, timezone

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, '..'))

ACTIVITES = os.path.join(RACINE, 'data', 'activities.json')
SORTIE = os.path.join(RACINE, 'data', 'materiel.json')

D_PPTX = os.path.join(RACINE, 'assets', 'powerpoints')
D_DOCS = os.path.join(RACINE, 'assets', 'documents')
D_PLANS = os.path.join(RACINE, 'assets', 'plans')
D_VIGN = os.path.join(RACINE, 'assets', 'vignettes')

# Les cinq blocs, dans l'ordre d'enseignement. Ce sont les sections des
# modules (voir la nomenclature : « Je découvre · Défi N · Je me lance »),
# pas une invention du dépôt.
BLOCS = {'A': 'Je découvre', 'B': 'Défi 1', 'C': 'Défi 2',
         'D': 'Défi 3', 'E': 'Je me lance'}

# La grille standard d'un module de cours : seize séances réparties 4-4-4-2-2.
# Un module qui n'a pas encore de dossier de production est mesuré contre
# elle — c'est ce qui permet d'écrire « 0 séance sur 16 » plutôt que de le
# taire.
GRILLE_STANDARD = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4',
                   'C1', 'C2', 'C3', 'C4', 'D1', 'D2', 'E1', 'E2']


# ── Lecture des sources ──────────────────────────────────────────────────

def grille_du_build():
    """L'ordre d'enseignement tel que le build des présentations le connaît,
    pour chaque module : `{slug: ['A1', 'A2', …]}`.

    On importe `build/powerpoints/modules.py`, le registre : dupliquer les
    grilles ici les ferait diverger au premier ajout de séance. L'import
    n'exige pas python-pptx, que ce script n'a pas à charger — le registre ne
    contient que des données."""
    import importlib.util
    chemin = os.path.join(ICI, 'powerpoints', 'modules.py')
    if not os.path.exists(chemin):
        return {}
    spec = importlib.util.spec_from_file_location('_modules_pptx', chemin)
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)
    except Exception as e:                       # pragma: no cover
        print(f'  (registre des modules illisible : {e})')
        return {}
    return {slug: [c.upper() for c in m['seances']]
            for slug, m in mod.MODULES.items()}


_DECK_CACHE = {}


def meta_du_deck(slug, code):
    """Titre et chapeau d'une séance, lus dans le source de son deck.

    On lit le fichier comme du texte au lieu de l'exécuter : les decks font
    `from theme import Deck`, donc les exécuter réclamerait python-pptx et
    reconstruirait les présentations pour rien."""
    cle = (slug, code)
    if cle in _DECK_CACHE:
        return _DECK_CACHE[cle]
    chemin = os.path.join(ICI, 'powerpoints', 'decks', slug, code.lower() + '.py')
    meta = {}
    if os.path.exists(chemin):
        src = open(chemin, encoding='utf-8').read()
        t = re.search(r"titre=(['\"])(.+?)\1", src, re.S)
        d = re.search(r"duree=(['\"])(.+?)\1", src, re.S)
        # Le chapeau est écrit en chaînes juxtaposées sur plusieurs lignes.
        c = re.search(r"chapeau=(\"(?:[^\"\\]|\\.)*\"(?:\s*\"(?:[^\"\\]|\\.)*\")*)",
                      src, re.S)
        if t:
            meta['titre'] = re.sub(r'\s+', ' ', t.group(2)).strip()
        if d:
            meta['duree'] = d.group(2).strip()
        if c:
            morceaux = re.findall(r'"((?:[^"\\]|\\.)*)"', c.group(1), re.S)
            meta['chapeau'] = re.sub(r'\s+', ' ', ''.join(morceaux)).strip()
    _DECK_CACHE[cle] = meta
    return meta


def premiere_phrase(texte, maxi=120):
    """La ligne de résumé d'un fichier. On coupe à la première phrase du
    chapeau écrit par l'auteur plutôt que d'inventer une description.

    Le découpage ignore la ponctuation **à l'intérieur des guillemets** : les
    chapeaux citent souvent une réplique (« depuis quand ? »), et couper là
    donnerait une phrase amputée en plein milieu."""
    if not texte:
        return ''
    profondeur, fin = 0, None
    for i, c in enumerate(texte):
        if c == '«':
            profondeur += 1
        elif c == '»':
            profondeur = max(0, profondeur - 1)
        elif c in '.!?' and profondeur == 0:
            suite = texte[i + 1:i + 2]
            if suite in ('', ' ', '\n'):
                fin = i + 1
                break
    phrase = (texte[:fin] if fin else texte).strip()
    if len(phrase) > maxi:
        phrase = phrase[:maxi - 1].rsplit(' ', 1)[0] + '…'
    return phrase


# ── Mesure des fichiers ──────────────────────────────────────────────────

def maj_le(chemin):
    return datetime.fromtimestamp(os.path.getmtime(chemin)).strftime('%Y-%m-%d')


def nb_diapositives(chemin):
    """Compte les diapositives sans python-pptx : un `.pptx` est une archive
    zip, et chaque diapositive y est un `ppt/slides/slideN.xml`."""
    try:
        with zipfile.ZipFile(chemin) as z:
            return sum(1 for n in z.namelist()
                       if re.fullmatch(r'ppt/slides/slide\d+\.xml', n))
    except Exception:
        return None


def nb_blocs(chemin):
    """Le nombre d'exercices d'une fiche. On ne compte **pas** de pages : le
    nombre de pages d'un document HTML dépend de l'imprimante et du navigateur,
    l'annoncer serait une invention. Le bloc, lui, est écrit dans la fiche."""
    try:
        return open(chemin, encoding='utf-8').read().count('class="bloc card"')
    except Exception:
        return None


def rel(chemin):
    return os.path.relpath(chemin, RACINE).replace(os.sep, '/')


# ── Assemblage ───────────────────────────────────────────────────────────

def slug_de(activite):
    """Le slug d'un module se lit dans son chemin d'activité interactive :
    `assets/interactive/<slug>/…`. C'est la clé qui relie une activité à son
    dossier de production, sans nouveau champ à tenir à jour."""
    for champ in ('interactive', 'parcours'):
        m = re.search(r'assets/interactive/([^/]+)/', activite.get(champ) or '')
        if m:
            return m.group(1)
    return None


def fichier_presentation(slug, code):
    dossier = os.path.join(D_PPTX, slug)
    if not os.path.isdir(dossier):
        return None
    for nom in sorted(os.listdir(dossier)):
        if nom.endswith('.pptx') and nom.split('-', 1)[0].upper() == code:
            return os.path.join(dossier, nom)
    return None


def fichier_fiche(slug, code):
    if not os.path.isdir(D_DOCS):
        return None
    prefixe = f'{slug}-{code.lower()}-'
    for nom in sorted(os.listdir(D_DOCS)):
        if nom.startswith(prefixe) and nom.endswith('.html'):
            return os.path.join(D_DOCS, nom)
    return None


def bloc_fichier(id_, type_, chemin, resume, extra=None):
    f = {
        'id': id_,
        'type': type_,
        'chemin': rel(chemin),
        'format': os.path.splitext(chemin)[1].lstrip('.').lower(),
        'octets': os.path.getsize(chemin),
        'majLe': maj_le(chemin),
        'origine': 'officiel',
    }
    if resume:
        f['resume'] = resume
    f.update(extra or {})
    return f


def seance(slug, code, grille):
    meta = meta_du_deck(slug, code)
    fichiers = []

    pptx = fichier_presentation(slug, code)
    if pptx:
        extra = {}
        n = nb_diapositives(pptx)
        if n:
            extra['diapositives'] = n
        vign = os.path.join(D_VIGN, slug, code + '.png')
        if os.path.exists(vign):
            extra['vignette'] = rel(vign)
        fichiers.append(bloc_fichier(
            f'{slug}-{code}-pptx', 'presentation', pptx,
            premiere_phrase(meta.get('chapeau')), extra))

    fiche = fichier_fiche(slug, code)
    if fiche:
        extra = {'impression': 'lettre-nb'}
        n = nb_blocs(fiche)
        if n:
            extra['blocs'] = n
        # La fiche ne reprend pas le chapeau de la présentation : les deux
        # blocs se suivent à l'écran, et la même phrase deux fois n'apprend
        # rien. On décrit ce que la fiche est, avec un compte réel.
        resume = (f'Les exercices de la séance à imprimer, {n} blocs.' if n
                  else 'Les exercices de la séance, à imprimer.')
        fichiers.append(bloc_fichier(
            f'{slug}-{code}-fiche', 'fiche', fiche, resume, extra))

    s = {'code': code, 'bloc': code[0], 'fichiers': fichiers}
    if meta.get('titre'):
        s['titre'] = meta['titre']
    if meta.get('duree'):
        s['duree'] = meta['duree']
    return s


def plan_de(activite):
    chemin = activite.get('planCours') or ''
    complet = os.path.join(RACINE, chemin)
    if chemin and os.path.exists(complet):
        return bloc_fichier(f'act-{activite["id"]}-plan', 'plan', complet, '')
    return None


def porteur_cours(activite, grilles):
    slug = slug_de(activite)
    if not slug:
        return None
    grille = grilles.get(slug) or GRILLE_STANDARD
    seances = [seance(slug, c, grille) for c in grille]
    equipees = sum(1 for s in seances if s['fichiers'])

    if equipees == 0:
        etat = 'a-venir'
    elif equipees == len(grille):
        etat = 'complet'
    else:
        etat = 'partiel'

    p = {
        'activiteId': activite['id'],
        'slug': slug,
        'categorie': 'cours',
        'etat': etat,
        'seancesPrevues': len(grille),
        'seancesEquipees': equipees,
        # Un module en cours de production garde ses séances vides : c'est ce
        # qui permet à l'écran d'écrire « Rien encore » sur la rangée plutôt
        # que de la faire disparaître. Un module qui n'a rien du tout n'en
        # garde aucune — le compte « 0 sur 16 » dit déjà tout.
        'seances': seances if etat == 'partiel' else
                   [s for s in seances if s['fichiers']],
    }
    plan = plan_de(activite)
    if plan:
        p['plan'] = plan
    return p


def porteur_atelier(activite):
    fichiers = []
    for champ, type_ in (('slideshow', 'presentation'),
                         ('studentDoc', 'fiche'),
                         ('planCours', 'plan')):
        chemin = activite.get(champ) or ''
        complet = os.path.join(RACINE, chemin)
        if not chemin or not os.path.exists(complet):
            continue
        extra = {}
        if complet.endswith('.pptx'):
            n = nb_diapositives(complet)
            if n:
                extra['diapositives'] = n
        if type_ == 'fiche' and complet.endswith('.html'):
            extra['impression'] = 'lettre-nb'
        fichiers.append(bloc_fichier(
            f'act-{activite["id"]}-{champ}', type_, complet, '', extra))

    return {
        'activiteId': activite['id'],
        'categorie': 'atelier',
        'etat': 'complet' if fichiers else 'a-venir',
        'seancesPrevues': 1,
        'seancesEquipees': 1 if fichiers else 0,
        'seances': [{'code': None, 'bloc': None, 'fichiers': fichiers}] if fichiers else [],
    }


def inventaire():
    activites = json.load(open(ACTIVITES, encoding='utf-8'))
    grilles = grille_du_build()
    porteurs = []
    for a in activites:
        if a.get('categorie') == 'cours':
            p = porteur_cours(a, grilles)
        else:
            p = porteur_atelier(a)
        if p:
            porteurs.append(p)

    cours = [p for p in porteurs if p['categorie'] == 'cours']
    ateliers = [p for p in porteurs if p['categorie'] == 'atelier']
    fichiers = sum(len(s['fichiers']) for p in porteurs for s in p['seances'])

    return {
        'genereLe': datetime.now(timezone.utc).astimezone().isoformat(
            timespec='seconds'),
        'blocs': BLOCS,
        'resume': {
            'cours': len(cours),
            'coursComplets': sum(1 for p in cours if p['etat'] == 'complet'),
            'coursPartiels': sum(1 for p in cours if p['etat'] == 'partiel'),
            'coursAVenir': sum(1 for p in cours if p['etat'] == 'a-venir'),
            'ateliers': len(ateliers),
            'ateliersEquipes': sum(1 for p in ateliers if p['etat'] == 'complet'),
            'fichiers': fichiers,
        },
        'porteurs': porteurs,
    }


def main(argv):
    inv = inventaire()
    texte = json.dumps(inv, ensure_ascii=False, indent=2) + '\n'

    if '--verifier' in argv:
        ancien = open(SORTIE, encoding='utf-8').read() if os.path.exists(SORTIE) else ''
        def sans_date(t):
            return re.sub(r'"genereLe": "[^"]*"', '', t)
        if sans_date(ancien) != sans_date(texte):
            print('ÉCART · data/materiel.json ne correspond plus au disque.')
            print('Relancez : python3 build/materiel.py')
            return 1
        print('materiel.json est à jour.')
        return 0

    open(SORTIE, 'w', encoding='utf-8').write(texte)

    r = inv['resume']
    print(f'Cours    : {r["cours"]} — {r["coursComplets"]} complet(s), '
          f'{r["coursPartiels"]} partiel(s), {r["coursAVenir"]} à venir')
    print(f'Ateliers : {r["ateliers"]} — {r["ateliersEquipes"]} équipé(s)')
    print(f'Fichiers : {r["fichiers"]}')
    for p in inv['porteurs']:
        if p['categorie'] == 'cours' and p['etat'] != 'a-venir':
            print(f'  {p["slug"]:22s} {p["seancesEquipees"]:2d} séance(s) '
                  f'sur {p["seancesPrevues"]}')
    print(f'\nÉcrit : {rel(SORTIE)} ({len(texte) // 1024} Ko)')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
