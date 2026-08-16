# -*- coding: utf-8 -*-
"""C5 · Les quatre points, ensemble.
Bloc C « Défi 2 · La langue » · couleur teal (écoute et réponds) · 60 min.
Source du module : exercices `l1` à `l4` et leurs quatre mini-leçons — synthèse du défi 2.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C5', section='teal',
        titre='Les quatre points, ensemble',
        chapeau="Le futur proche, les verbes pronominaux, « avoir besoin de » et les "
                "adverbes d'intensité tiennent dans une seule phrase de patient. C'est "
                "aujourd'hui qu'on les assemble.",
        duree='60 minutes')

    d.titre(notes="Séance de synthèse du défi 2. Elle prépare directement E1 : les "
                  "phrases produites ici sont celles de l'appel enregistré.")

    d.objectifs([
        "employer les quatre points de langue dans un même échange ;",
        "se corriger et corriger un camarade ;",
        "préparer les phrases de l'appel de E1 ;",
        "repérer ses propres erreurs fréquentes.",
    ])

    d.tableau('Rappel', "Les quatre points du défi 2",
              ['Le point', 'La phrase modèle'],
              [["le futur proche", "je vais prendre un rendez-vous"],
               ["les verbes pronominaux", "je me sens fatiguée"],
               ["avoir besoin de", "j'ai besoin de me reposer"],
               ["les adverbes d'intensité", "je suis très fatiguée"]],
              cle=0,
              note="Les quatre viennent des dialogues des blocs A et B.",
              notes="Faire retrouver chaque phrase modèle dans un des deux dialogues. "
                    "Cinq minutes, et ça referme la boucle du module.")

    d.regle('La phrase complète du patient',
            "Je me sens… depuis… · j'ai besoin de… · je vais…",
            precision="« Je me sens très fatiguée depuis deux semaines. J'ai besoin d'un "
                      "rendez-vous. Je vais appeler la clinique demain matin. » Trois "
                      "phrases, quatre points de langue.",
            notes="La diapositive à photographier. C'est le modèle de l'appel de E1 : la "
                  "laisser au tableau toute la séance.")

    d.pratique('Pratique · 1 de 4', "Corrigez la phrase",
               "Une erreur par ligne. Laquelle ?", [
        ("Je vais prends un rendez-vous.", "je vais prendre — l'infinitif après aller"),
        ("Je sens fatiguée depuis lundi.", "je me sens — le pronom manque"),
        ("J'ai besoin un médicament.", "j'ai besoin d'un médicament — le « de »"),
        ("Je suis fatiguée très.", "je suis très fatiguée — l'adverbe devant"),
        ("Nous se reposons le week-end.", "nous nous reposons — le pronom suit le sujet"),
    ], corrige=True,
       notes="Les cinq erreurs sont celles vraiment relevées dans les billets de C1 à "
             "C4. Le dire : elles viennent du groupe, pas d'un manuel.")

    d.pratique('Pratique · 2 de 4', "Une phrase, deux points",
               "Employez les deux points de langue demandés.", [
        ("pronominal + intensité", "Je me sens très fatiguée."),
        ("besoin de + infinitif", "J'ai besoin de me reposer."),
        ("futur proche + besoin", "Je vais demander un rendez-vous parce que j'ai besoin "
                                  "de voir un médecin."),
        ("pronominal + futur proche", "Je vais me reposer ce week-end."),
    ], corrige=True,
       notes="La quatrième est la plus délicate : au futur proche, le pronom se place "
             "devant l'infinitif — « je vais me reposer ».")

    d.piege("Le piège du pronom au futur proche",
            "Je me vais reposer ce week-end.",
            "Je vais me reposer ce week-end.",
            "Le pronom reste collé au verbe auquel il appartient. Ici, c'est « reposer », "
            "pas « aller » : il se glisse donc entre les deux verbes.",
            notes="Point avancé, mais il sort naturellement de la pratique 2. Le traiter "
                  "seulement si le groupe suit ; sinon, y revenir en E1.")

    d.pratique('Pratique · 3 de 4', "L'appel complet",
               "À deux. Trois phrases, quatre points de langue.", [
        ("Vous vous présentez", "Bonjour, je m'appelle…"),
        ("Vous dites comment vous vous sentez", "Je me sens… depuis…"),
        ("Vous dites ce dont vous avez besoin", "J'ai besoin de…"),
        ("Vous proposez un moment", "Je vais être libre mardi après-midi."),
        ("Vous confirmez", "Donc c'est bien… ?"),
    ], corrige=False,
       notes="Vingt minutes. C'est la répétition générale de E1 : le dire, pour que "
             "l'exercice ait un enjeu.")

    d.pratique('Pratique · 4 de 4', "Votre fiche d'erreurs",
               "Quelles erreurs faites-vous, vous ?", [
        ("Le futur proche", "je conjugue le deuxième verbe ? j'ajoute « à » ?"),
        ("Les pronominaux", "j'oublie le pronom ? je mets « se » partout ?"),
        ("Avoir besoin de", "j'oublie le « de » ? j'oublie « avoir » ?"),
        ("Les adverbes", "je confonds très et trop ? je place après ?"),
    ], corrige=False,
       notes="Dix minutes, en silence, avec les billets rendus des quatre séances. "
             "Chacun repart avec sa propre liste — c'est ce qu'il relira avant E1.")

    d.billet(
        "Écrivez les trois phrases de votre appel : comment vous vous sentez, ce dont "
        "vous avez besoin, quand vous êtes libre.",
        exemples=[
            "Trois phrases, vraies, prêtes à dire au téléphone.",
            "Vous les enregistrerez en E1.",
        ],
        notes="Ramasser et rendre au début de E1. Personne ne doit arriver à "
              "l'enregistrement avec une page blanche.")

    return d.save(dossier)
