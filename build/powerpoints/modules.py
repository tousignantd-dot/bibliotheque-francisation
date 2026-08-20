# -*- coding: utf-8 -*-
"""
Le registre des modules produits par ce dossier
================================================

Un seul endroit dit, pour chaque module : son numéro, le titre affiché en pied
de page, l'ordre d'enseignement de ses séances et le nom de ses blocs. Tout le
reste — `build.py`, `build_fiches.py`, `theme.py`, `fiche.py`,
`build/materiel.py` — s'y rapporte au lieu de porter une constante à soi.

Le champ `niveau` dit à quel niveau du programme le module appartient. Il est
lu par `build/module.py` (qui le pose dans le HTML du module) et par
`build_fiches.py` (l'en-tête des fiches élèves) : aucun générateur ne doit
réécrire « niveau 4 » en dur. Les slugs restent **globalement uniques** — un
`module-sante` de niveau 6 devrait porter un autre slug, sinon il écraserait
celui du niveau 4, les dossiers de sortie étant à plat.

Le **slug** est la clé : c'est celui de `assets/interactive/<slug>/`, donc
celui de `assets/powerpoints/<slug>/` et le préfixe des fiches. C'est lui qui
relie un fichier produit à son activité dans le dépôt de matériel.

**Le nombre de séances suit le nombre de défis du module**, pas une grille
imposée : les modules à trois défis se répartissent 4-4-4-2-2, ceux à deux
défis 4-5-5-2. Seize séances dans les deux cas, mais un module qui n'a pas de
« Défi 3 » n'a pas de bloc D — inventer une séance sans contenu serait pire
que de n'en pas avoir.

Le module actif est posé par le script d'entrée (`choisir()`), avant que les
decks ne soient importés : ceux-ci font `from theme import Deck`, et `Deck`
lit ici son numéro et son titre.
"""

GRILLE_3_DEFIS = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4',
                  'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'e1', 'e2']
GRILLE_2_DEFIS = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'b5',
                  'c1', 'c2', 'c3', 'c4', 'c5', 'e1', 'e2']
# Huit séances, deux blocs de quatre heures — le format des niveaux 1 et 2.
# Les deux grilles ci-dessus en font seize : c'est trop long pour un débutant
# qui n'a pas encore l'alphabet, et l'utilisateur a tranché en ce sens le
# 20 août 2026. Un bloc A de découverte, deux défis courts, une séance de
# production. Pas de bloc « Je retiens des mots » séparé : le vocabulaire se
# révise dans la dernière séance.
GRILLE_COURTE = ['a1', 'a2', 'a3', 'b1', 'b2', 'c1', 'c2', 'e1']


def _blocs(defi1, defi2, defi3=None):
    b = {'A': 'Je découvre', 'B': f'Défi 1 · {defi1}', 'C': f'Défi 2 · {defi2}',
         'E': 'Je me lance'}
    if defi3:
        b['D'] = f'Défi 3 · {defi3}'
    return b


MODULES = {
    'module-consultation': {
        'numero': 1, 'activite': 35, 'niveau': 4,
        'titre': 'Consulter au bon endroit',
        'chapeau': "Décrire une douleur, choisir le bon service, comprendre "
                   "les conseils.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le triage', "L'examen", 'Le formulaire'),
    },
    'module-urgence': {
        'numero': 2, 'activite': 36, 'niveau': 4,
        'titre': 'Une urgence au travail',
        'chapeau': "Réagir vite, appeler le bon service, raconter ce qui est "
                   "arrivé.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("À l'urgence", 'Les soins', "À l'accueil"),
    },
    'module-sante': {
        'numero': 3, 'activite': 34, 'niveau': 4,
        'titre': 'Prendre rendez-vous et aller à la pharmacie',
        'chapeau': "Appeler une clinique, dire comment on se sent, comprendre "
                   "les consignes du pharmacien.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('À la pharmacie', 'La langue'),
    },
    'module-travail': {
        'numero': 4, 'activite': 39, 'niveau': 4,
        'titre': 'Absent ou en retard : que faire ?',
        'chapeau': "Prévenir son superviseur, justifier un retard, écrire un "
                   "courriel.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Le message', 'Le retard', 'Le courriel'),
    },
    'module-procedure': {
        'numero': 5, 'activite': 40, 'niveau': 4,
        'titre': 'Quelle est la procédure ?',
        'chapeau': "Comprendre une procédure, suivre des étapes, lire une "
                   "directive.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('La demande de remboursement', 'Soumettre sa demande',
                        'Avez-vous lu les directives ?'),
    },
    'module-nouvelles': {
        'numero': 6, 'activite': 41, 'niveau': 4,
        'titre': "C'est l'heure des nouvelles",
        'chapeau': "Comprendre un fait divers à l'oral et à l'écrit, puis en "
                   "raconter un.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('As-tu écouté les nouvelles ?',
                        "Qu'est-ce que tu lis ?"),
    },
    'module-meteo': {
        'numero': 7, 'activite': 42, 'niveau': 4,
        'titre': 'Quelles sont les prévisions ?',
        'chapeau': "Comprendre un bulletin, lire une alerte, décider d'une "
                   "journée de travail.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('Le bulletin de six heures',
                        'Lire une alerte avant de partir'),
    },
    'module-pub': {
        'numero': 8, 'activite': 43, 'niveau': 4,
        'titre': 'Des publicités efficaces',
        'chapeau': "Reconnaître les éléments et les valeurs d'une publicité, "
                   "puis en écrire une.",
        'seances': GRILLE_2_DEFIS,
        'blocs': _blocs('Trente secondes en ondes',
                        'Deux affiches sur le babillard'),
    },
    'module-logement': {
        'numero': 9, 'activite': 44, 'niveau': 4,
        'titre': 'Comment est le logement ?',
        'chapeau': "Visiter, poser les bonnes questions, comparer deux "
                   "logements.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Poser les bonnes questions', 'Ce qui compte pour moi',
                        'Un logement pour chaque besoin'),
    },
    'module-probleme': {
        'numero': 10, 'activite': 45, 'niveau': 4,
        'titre': 'Pouvez-vous régler le problème ?',
        'chapeau': "Signaler un problème, faire respecter ses droits, se "
                   "plaindre efficacement.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Un problème dans le logement',
                        "Des problèmes dans l'immeuble",
                        'Une situation inacceptable'),
    },
    'module-relations': {
        'numero': 11, 'activite': 48, 'niveau': 4,
        'titre': 'Des nouvelles à donner',
        'chapeau': "Parler de ses semaines, raconter une expérience "
                   "personnelle, donner des nouvelles par écrit.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Ce que je fais de mes semaines',
                        "Ce que j'ai vécu",
                        'Donner des nouvelles'),
    },
    'module-deplacement': {
        'numero': 12, 'activite': 49, 'niveau': 4,
        'titre': 'Trouver son chemin',
        'chapeau': "Demander un itinéraire, le suivre, l'expliquer à son tour, "
                   "et comprendre les annonces en chemin.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Demander son chemin',
                        'Expliquer le chemin',
                        "Les messages qu'on entend"),
    },
    'module-activite': {
        'numero': 13, 'activite': 50, 'niveau': 4,
        'titre': "S'inscrire à une activité",
        'chapeau': "S'informer sur une activité, comprendre les consignes du "
                   "moniteur, lire un dépliant et s'inscrire.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur une activité",
                        'Comprendre et donner des consignes',
                        "Le dépliant et l'inscription"),
    },
    'module-alimentation': {
        'numero': 14, 'activite': 51, 'niveau': 4,
        'titre': "Faire l'épicerie",
        'chapeau': "S'informer sur un produit, commander à un comptoir, lire "
                   "une étiquette et un mode d'emploi.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur un produit",
                        'Commander à un comptoir',
                        "L'étiquette et le mode d'emploi"),
    },
    'module-achat': {
        'numero': 15, 'activite': 52, 'niveau': 4,
        'titre': 'Acheter un appareil',
        'chapeau': "S'informer sur un appareil, comprendre la garantie, le "
                   "paiement et la livraison, puis lire le mode d'emploi.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs("S'informer sur l'appareil",
                        'La garantie et la livraison',
                        "Le mode d'emploi"),
    },
    'module-restaurant': {
        'numero': 16, 'activite': 53, 'niveau': 4,
        'titre': 'Au restaurant',
        'chapeau': "Lire un menu, commander en salle à manger, demander ce "
                   "qu'il faut pendant le repas, et payer.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Lire le menu et commander',
                        'Pendant le repas',
                        "L'addition"),
    },
    'module-vetements': {
        'numero': 18, 'activite': 54, 'niveau': 4,
        'titre': 'Acheter des vêtements',
        'chapeau': "S'informer sur un vêtement, l'essayer, comprendre son "
                   "entretien, et savoir comment l'échanger.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Trouver sa taille',
                        "L'avis et l'entretien",
                        "Échanger et se faire rembourser"),
    },

    # ── Niveau 3 ────────────────────────────────────────────────────
    'module-n3-epicerie': {
        'numero': 1, 'activite': 55, 'niveau': 3,
        'titre': "À l'épicerie",
        'chapeau': "Trouver un produit, comprendre un numéro d'allée, lire la "
                   "circulaire et vérifier sa facture.",
        'seances': GRILLE_3_DEFIS,
        'blocs': _blocs('Trouver le produit',
                        'Choisir',
                        'À la caisse'),
    },
}

# L'ordre d'affichage : par niveau, puis par numéro à l'intérieur du niveau.
# Les dix-huit modules du niveau 4 portaient des numéros uniques, et trier sur
# le seul numéro suffisait. À partir du moment où chaque niveau recommence à
# 1 — le chantier des sept autres niveaux, août 2026 —, sept modules portent le
# numéro 1 : sans le niveau en première clé, ils se mêlent aux modules du 4.
ORDRE = sorted(MODULES, key=lambda s: (MODULES[s].get('niveau', 4),
                                       MODULES[s]['numero']))

_ACTIF = None


def choisir(slug):
    """Pose le module actif. À appeler **avant** d'importer un deck : les
    decks construisent leur `Deck` à l'import de leur fonction `build`, et
    `Deck` lit ici le numéro et le titre à mettre en pied de page."""
    global _ACTIF
    if slug not in MODULES:
        raise SystemExit(
            f"Module inconnu : {slug}\nModules connus : "
            + ', '.join(ORDRE))
    _ACTIF = slug
    return MODULES[slug]


def slug_actif():
    if _ACTIF is None:
        raise RuntimeError(
            "Aucun module actif : appelez modules.choisir('<slug>') avant "
            "d'importer un deck.")
    return _ACTIF


def actif():
    return MODULES[slug_actif()]
