# -*- coding: utf-8 -*-
"""A1 · Trois personnes dans un deux et demie.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='Trois personnes dans un deux et demie',
        chapeau="Au Québec, un logement se compte en pièces et demies. Savoir "
                "lire ce chiffre, c'est savoir si une annonce vous concerne ou "
                "non.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander au groupe qui a déjà cherché un "
                  "logement ici, et comment ça s'est passé. La plupart raconteront "
                  "qu'ils ont demandé à quelqu'un de traduire, ou qu'ils ont pris le "
                  "premier logement trouvé. C'est exactement la situation de Dilnoza, "
                  "et c'est le point de départ du module.")

    d.objectifs([
        "comprendre ce que veut dire un trois et demie, un quatre et demie ;",
        "nommer les pièces d'un logement avec leur article ;",
        "dire combien de personnes habitent un logement ;",
        "savoir où trouver des petites annonces de logement.",
    ])

    d.declencheur(
        'Observation', "Combien de pièces a votre logement ?",
        pistes=[
            "Est-ce que vous savez comment on l'appelle : un trois et demie, un quatre et demie ?",
            "Combien de personnes y habitent ?",
            "Est-ce que quelqu'un dort dans le salon ?",
            "Qui vous a aidé à trouver ce logement-là ?",
        ],
        notes="Laisser venir les réponses dans n'importe quelle langue, puis les "
              "traduire ensemble au tableau. Ne pas commenter les situations "
              "difficiles : plusieurs élèves vivent à cinq dans un trois et demie et "
              "n'ont pas envie d'en parler devant le groupe.")

    d.dialogue('Dialogue · 1 de 3', "Tu cherches un logement ?", [
        ("DILNOZA", "Rachid, tu as déjà déménagé au Québec, toi ?", True),
        ("RACHID", "Deux fois. Pourquoi ? Tu cherches un logement ?", True),
        ("DILNOZA", "Oui. Nous sommes trois dans un deux et demie. C'est trop petit.", True),
        ("RACHID", "Trois personnes dans un deux et demie ? Il te faut un quatre et demie.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer la première phrase de Rachid : il demande d'abord, il "
             "conseille ensuite. C'est ce que fait toute personne qui aide quelqu'un à "
             "chercher. Ne pas donner encore le sens de « quatre et demie ».")

    d.dialogue('Dialogue · 2 de 3', "Et le demi, c'est quelle pièce ?", [
        ("DILNOZA", "Un quatre et demie, c'est combien de pièces ?", True),
        ("RACHID", "Deux chambres fermées, un salon, une cuisine et une salle de bain.", True),
        ("DILNOZA", "Et le demi, c'est quelle pièce ?", True),
        ("RACHID", "C'est la salle de bain. On l'appelle le demi. C'est comme ça ici.", True),
    ], notes="C'est le cœur de la séance. Dessiner au tableau un plan très simple de "
             "quatre pièces plus la salle de bain, et faire compter le groupe à voix "
             "haute. Le demi surprend tout le monde la première fois.")

    d.dialogue('Dialogue · 3 de 3', "Regarde les petites annonces", [
        ("DILNOZA", "Il a six ans. Il veut sa chambre à lui.", True),
        ("RACHID", "Regarde les petites annonces. Il y en a sur le babillard, en bas.", True),
        ("DILNOZA", "Je les ai regardées. Je ne comprends pas la moitié des mots.", True),
        ("RACHID", "C'est normal. Elles sont écrites en abrégé. Viens, on va en lire une ensemble.", True),
    ], notes="La dernière réplique annonce tout le bloc B. Insister : ce n'est pas le "
             "français de Dilnoza qui est en cause, c'est la façon dont les annonces "
             "sont écrites. Beaucoup d'élèves croient le contraire.")

    d.tableau('Analyse', "Compter les pièces d'un logement",
              ["On dit", "Ce que ça veut dire"],
              [["un un et demie", "une seule pièce, avec un coin cuisine"],
               ["un trois et demie", "une chambre fermée, un salon, une cuisine"],
               ["un quatre et demie", "deux chambres fermées, un salon, une cuisine"],
               ["le demi", "la salle de bain, jamais une chambre"]],
              cle=1,
              note="Le chiffre compte toutes les pièces, pas les chambres.",
              notes="Diapositive à photographier. C'est la confusion la plus coûteuse du "
                    "module : un élève qui croit qu'un quatre et demie a quatre chambres "
                    "va visiter des logements trop petits pendant des semaines.")

    d.regle("La question à se poser avant de chercher",
            "« De combien de chambres est-ce que nous avons besoin ? »",
            precision="C'est la première question qu'on vous posera au "
                      "téléphone, et c'est elle qui décide du chiffre à "
                      "chercher dans les annonces. Une chambre par couple, une "
                      "chambre par enfant qui grandit.",
            notes="Diapositive à photographier. Faire répondre chacun pour lui-même, à "
                  "voix haute, en une phrase complète. C'est la phrase du billet de "
                  "sortie.")

    d.cartes("Les pièces du logement", "Cinq mots", [
        ("un logement",
         "L'endroit où on habite : un appartement dans un immeuble, ou une "
         "maison. Au Québec, la plupart des gens louent un logement dans un "
         "immeuble de deux ou trois étages."),
        ("un salon",
         "La grande pièce ouverte, sans porte, où on reçoit. Ce n'est pas une "
         "chambre : une annonce ne le compte jamais comme une chambre."),
        ("une chambre à coucher",
         "La pièce fermée, avec une porte, où on met son lit. C'est ce que "
         "l'annonce appelle une chambre fermée."),
        ("une salle de bain",
         "La pièce du bain, du lavabo et de la toilette. C'est elle, le demi "
         "de « trois et demie »."),
    ], notes="Faire dire chaque mot avec son article : un logement, un salon, une "
             "chambre, une salle de bain. L'article fait partie du mot et il sera "
             "travaillé à la séance A4.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Dilnoza habite un deux et demie avec deux autres personnes.", "vrai"),
        ("Son garçon dort dans le salon.", "vrai"),
        ("Un quatre et demie a deux chambres fermées.", "vrai"),
        ("Le demi est une petite chambre.", "faux — c'est la salle de bain"),
        ("Rachid n'a jamais déménagé au Québec.", "faux — deux fois"),
        ("Les petites annonces sont écrites en abrégé.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue. C'est "
             "l'exercice 1 de la section « Je découvre » de l'activité interactive.")

    d.billet(
        "Écrivez combien de pièces a votre logement et combien de personnes y habitent.",
        exemples=[
            "J'habite un ___ et demie.",
            "Nous sommes ___ personnes.",
        ],
        notes="Devoir court. Les réponses servent au bloc B : chacun cherchera dans les "
              "annonces le chiffre qui lui convient. Ramasser les billets et les garder "
              "pour la séance B1.")

    return d.save(dossier)
