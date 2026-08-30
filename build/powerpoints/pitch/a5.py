# -*- coding: utf-8 -*-
"""A5 · Les sept objections — celles qui viennent vraiment, et quoi répondre.

Section framboise · la moitié projetable de la trousse. Le déroulé de la
rencontre, lui, reste sur papier : ce sont les notes du présentateur, et les
projeter reviendrait à montrer à la salle qu'on la déroule.

**Les réponses complètes ne sont pas recopiées ici.** Elles vivent dans
`build/trousse.py`, qui écrit déjà la page et le PDF ; ce module les y lit et
les met dans les notes du présentateur. Ce qui est écrit ici, c'est seulement
la phrase courte qu'on projette — une réponse de sept lignes ne se lit pas au
fond d'une salle, et une réponse recopiée finirait par ne plus concorder avec
celle du document qu'on laisse sur la table.
"""
import pathlib
import re
import sys

from theme import Deck
from chiffres import CH, n
from vues import ecran, poser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / 'build'))
import trousse  # noqa: E402


def _texte(html_brut):
    """La réponse de la trousse, débarrassée de son balisage.

    Les notes du présentateur sont du texte : un `<b>` projeté dans le volet de
    notes de PowerPoint s'y afficherait tel quel.
    """
    t = re.sub(r'<[^>]+>', '', html_brut)
    return re.sub(r'\s+', ' ', t).strip()


def _reponses():
    """{question -> réponse en clair}, chiffres déjà substitués."""
    out = {}
    for q, r in trousse.QUESTIONS:
        if '%s' in r:
            r = r % (n(CH['decks']), n(CH['notes']), n(CH['heures']))
        out[_texte(q)] = _texte(r)
    return out


# La phrase qu'on projette, dans l'ordre de la trousse. La clé est le début de
# la question : elle sert à retrouver la réponse longue, et à faire échouer le
# build si la trousse réécrit une objection sans qu'on le sache.
#
# Le quatrième champ, facultatif, est **une copie d'écran qui répond mieux que
# la phrase**. Quatre objections sur sept en ont une ; les trois autres se
# règlent par un chiffre ou par un principe, et leur coller une image serait
# décoratif. On ne met pas d'écran pour meubler.
COURT = [
    ("Nous ne voulons pas d'intelligence",
     "Alors ne l'ouvrez pas.",
     "C'est un réglage, pas une négociation : le centre le pose une fois, et les "
     "87 modules se replient. Le même fichier, sans l'assistant.",
     ('cas', '08-module-sans-ia', "Le module, assistance fermée")),
    ("Où sont hébergées les données",
     "Rien d'identifiant n'a besoin d'exister.",
     "En mode séance, l'élève n'a ni compte, ni pseudonyme, ni trace qui lui "
     "survive à la soirée. La question de l'hébergement se pose alors sur du vide.",
     ('cas', '04-suivi-seance', "Une classe entière, sans un compte")),
    ("Il faut créer des comptes",
     "Non. Une feuille photocopiée suffit.",
     "Un code à six caractères, un code QR, et la classe travaille. Le suivi de "
     "l'enseignant est exactement le même écran.",
     ('cas', '05-feuille-seance', "Ce qu'on photocopie")),
    ("Combien ça coûte",
     "Ce qu'on mesure, pas ce qu'on estime.",
     "Chaque appel à un modèle est inscrit dans un registre, avec ses jetons. Un "
     "centre qui ferme l'assistant ne paie plus rien à l'usage."),
    ("Est-ce que ça remplace l'enseignant",
     "Il n'y a pas de cours sans lui.",
     "C'est l'enseignant qui ouvre un module, qui décide de la séance, qui lit les "
     "productions. Rien ne s'ouvre tout seul à un élève."),
    ("Qui a écrit le contenu",
     "Un enseignant de francisation.",
     "Le contenu est écrit à partir du programme du Ministère, situation par "
     "situation — jamais recopié d'un manuel existant."),
    ("Nos élèves n'ont pas d'ordinateur",
     "Le cours entier se fait sur un téléphone.",
     "Les sept familles d'exercices, l'enregistrement de la voix, le dépôt d'un "
     "texte. Et la fiche papier existe pour ceux qui n'ont rien.",
     ('tel', '02-portail-cours', "Le cours entier, sur un téléphone")),
]


def build(dossier):
    rep = _reponses()

    d = Deck(
        code='A5', section='framboise',
        titre="Les sept objections",
        chapeau="Celles qui viennent vraiment, dans l'ordre où elles viennent. Elles "
                "ne sont pas à désamorcer d'avance : les poser soi-même, avant que la "
                "salle les pose, est ce qui fait qu'on y répond calmement.",
        duree='7 minutes')

    d.titre(surtitre="ANNEXE  ·  LES OBJECTIONS",
            notes="Annexe. Deux usages : la relire seul avant la rencontre, ou la "
                  "projeter si la salle part dans les questions plus tôt que prévu.")

    d.regle("Comment s'en servir",
            "Poser l'objection avant que la salle la pose.",
            precision="Une objection qu'on formule soi-même se répond ; une objection "
                      "qu'on subit se défend. Les sept qui suivent ont toutes été "
                      "entendues en salle — aucune n'est inventée pour la forme.",
            notes="Ne pas projeter les sept d'affilée : c'est une réserve, pas un "
                  "chapitre. On y va chercher celle qui vient de tomber.")

    for entree in COURT:
        cle, courte, detail = entree[:3]
        vue = entree[3] if len(entree) > 3 else None
        longue = next((v for k, v in rep.items() if cle in k), None)
        if longue is None:
            raise SystemExit(
                "!! A5 : plus aucune objection de la trousse ne commence par\n"
                "   « %s ».\n"
                "   La trousse a été réécrite : reprendre la phrase courte ici."
                % cle)
        question = next(k for k in rep if cle in k)
        d.piege("Ce qu'on entend", question, courte, detail,
                notes="Réponse complète, telle qu'elle est dans la trousse :\n\n"
                      + longue)
        if vue:
            famille, nom, titre_vue = vue
            ecran(d, "La preuve", titre_vue, poser(famille, nom), courte,
                  notes="À projeter juste après la réponse, sans commenter. "
                        "Une objection tombe mieux devant un écran que devant "
                        "une phrase.")

    d.billet("Une objection qui ne vient pas est une objection qui n'a pas été dite. "
             "Demander : « qu'est-ce qui vous ferait dire non ? »",
             exemples=["Les sept réponses complètes sont dans la trousse.",
                       "Elles se relisent en cinq minutes, avant d'entrer."],
             notes="La vraie question de fin. Une salle silencieuse n'est pas une "
                   "salle convaincue.")

    return d.save(dossier)
