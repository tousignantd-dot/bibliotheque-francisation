# -*- coding: utf-8 -*-
"""C2 · Les pronoms compléments.
Bloc C · couleur ambre (écriture) · 75 min.
Source : exercice `t2pcom` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Le, lui, en, y',
        chapeau="« Est-ce que tu changes le pansement ? — Oui, je le change. » Quatre "
                "petits mots qui évitent de répéter, et qui se placent tous au même "
                "endroit : devant le verbe.",
        duree='75 minutes')

    d.titre(notes="Écrire au tableau la question et les deux réponses possibles : « je "
                  "change le pansement » et « je le change ». Demander laquelle sonne "
                  "juste dans une conversation. Le groupe choisira la seconde.")

    d.objectifs([
        "remplacer un complément par le, la, les ;",
        "remplacer un complément avec « à » par lui ou leur ;",
        "employer « en » pour une quantité et « y » pour un lieu ;",
        "placer le pronom devant le verbe, y compris à la négative.",
    ])

    d.regle('La règle de place',
            "Le pronom complément se place devant le verbe conjugué.",
            precision="Je le change. Je lui parle. J'en ai besoin. J'y vais. Toujours "
                      "devant, jamais après — c'est l'inverse de plusieurs autres "
                      "langues, et c'est ce qui demande le plus d'entraînement.",
            notes="Écrire la règle au tableau et l'y laisser. Chaque exercice de la "
                  "séance la vérifie.")

    d.tableau('Analyse', "Quatre pronoms, quatre usages",
              ['Le pronom', 'Il remplace', 'Exemple'],
              [["le, la, les", "un nom sans préposition", "Je le change."],
               ["lui, leur", "un nom après « à »", "Je lui parle."],
               ["en", "un nom après « de »", "J'en ai besoin."],
               ["y", "un nom après « à » pour un lieu", "J'y vais."]],
              cle=0,
              note="Le tri se fait sur la préposition : rien, à, de. C'est elle qui "
                   "choisit le pronom, pas le sens.",
              notes="Faire chercher la préposition avant de choisir le pronom. C'est un "
                    "test mécanique, et il fonctionne.")

    d.tableau('Analyse', "Comment trouver le bon pronom",
              ['La question', 'Le pronom'],
              [["Je change quoi ? le pansement", "le"],
               ["Je parle à qui ? au médecin", "lui"],
               ["J'ai besoin de quoi ? de crème", "en"],
               ["Je vais où ? à l'urgence", "y"]],
              cle=1,
              note="Poser la question au verbe : quoi, à qui, de quoi, où. La réponse "
                   "donne le pronom.",
              notes="Faire poser la question à voix haute pour chaque phrase, avant "
                    "d'écrire. C'est la méthode de toute la séance.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("À la négative, le pronom reste devant",
         "« Je ne le change pas. » Le pronom se glisse entre « ne » et le verbe. Les "
         "deux morceaux de la négation encadrent l'ensemble."),
        ("Au passé composé, devant l'auxiliaire",
         "« Je l'ai changé. » Le pronom se place devant « ai », pas devant le "
         "participe. Le verbe conjugué, c'est l'auxiliaire."),
        ("Le devient l' devant une voyelle",
         "« Je l'ai vu. » « Je l'applique. » Comme « ne » devient « n' », c'est "
         "automatique."),
        ("« En » remplace aussi une quantité",
         "« Combien de comprimés ? — J'en prends deux. » Le nombre reste, le nom "
         "disparaît."),
    ], notes="La deuxième carte est celle qui pose le plus de difficulté. La traiter "
             "lentement, avec trois exemples au tableau.")

    d.pratique('Pratique · 1 de 4', "Quel pronom ?",
               "Posez la question au verbe : quoi, à qui, de quoi, où.", [
        ("Est-ce que tu changes le pansement ? Oui, je ___ change.", "le"),
        ("Est-ce que tu parles au médecin ? Oui, je ___ parle.", "lui"),
        ("Est-ce que tu vas à l'urgence ? Oui, j'___ vais.", "y"),
        ("Est-ce que tu as besoin de crème ? Oui, j'___ ai besoin.", "en"),
        ("Est-ce que tu appelles les secours ? Oui, je ___ appelle.", "les"),
        ("Est-ce que tu écris aux infirmières ? Oui, je ___ écris.", "leur"),
    ], corrige=True,
       notes="Faire dire la question complète à voix haute avant chaque réponse. C'est "
             "elle qui fait le travail.")

    d.piege('Le piège de la place',
            "Je change le.",
            "Je le change.",
            "Le pronom complément se met devant le verbe, jamais après. C'est l'ordre "
            "inverse de l'anglais et de plusieurs autres langues, ce qui explique la "
            "fréquence de l'erreur. Il n'y a pas d'exception à retenir : toujours "
            "devant.",
            notes="Faire répéter cinq phrases à voix haute, avec le pronom devant. "
                  "L'oreille finit par accepter ce que la règle explique.")

    d.piege('Le piège du passé composé',
            "Je ai le changé.",
            "Je l'ai changé.",
            "Au passé composé, le pronom se place devant l'auxiliaire, pas devant le "
            "participe. L'auxiliaire est le verbe conjugué : c'est lui que le pronom "
            "précède. Et « le » devient « l' » devant « ai ».",
            notes="Relier à B2 : le verbe conjugué du passé composé est l'auxiliaire. "
                  "C'est la même idée qui explique la place de la négation.")

    d.pratique('Pratique · 2 de 4', "Répondez avec un pronom",
               "Remplacez les mots répétés par le bon pronom.", [
        ("Est-ce que tu as changé le pansement ?", "Oui, je l'ai changé."),
        ("Est-ce que tu as parlé au médecin ?", "Oui, je lui ai parlé."),
        ("Est-ce que tu es allé à l'urgence ?", "Oui, j'y suis allé."),
        ("Est-ce que tu as pris de la crème ?", "Oui, j'en ai pris."),
    ], corrige=True,
       notes="Tous les items sont au passé composé : le pronom doit passer devant "
             "l'auxiliaire. C'est l'exercice le plus difficile de la séance.")

    d.pratique('Pratique · 3 de 4', "Répondez négativement",
               "Le pronom reste devant le verbe, entre « ne » et lui.", [
        ("Est-ce que tu changes le pansement ?", "Non, je ne le change pas."),
        ("Est-ce que tu parles au médecin ?", "Non, je ne lui parle pas."),
        ("Est-ce que tu vas à l'urgence ?", "Non, je n'y vais pas."),
        ("Est-ce que tu as besoin de crème ?", "Non, je n'en ai pas besoin."),
    ], corrige=True,
       notes="Faire souligner les trois éléments dans chaque réponse : ne, le pronom, le "
             "verbe. L'ordre est toujours le même.")

    d.pratique('Pratique · 4 de 4', "Conversation à deux",
               "Posez la question, répondez avec un pronom. Puis échangez.", [
        ("le pansement", "Est-ce que tu le changes ? — Oui, je le change chaque matin."),
        ("la crème", "Est-ce que tu l'appliques ? — Oui, je l'applique deux fois par jour."),
        ("le médecin", "Est-ce que tu lui as parlé ? — Oui, je lui ai parlé hier."),
        ("l'urgence", "Est-ce que tu y es retourné ? — Non, je n'y suis pas retourné."),
    ], corrige=True,
       notes="Dix minutes en dyades. Circuler et corriger uniquement la place du "
             "pronom : le reste viendra plus tard.")

    d.billet(
        "Écrivez quatre phrases, une avec chaque pronom : le, lui, en, y.",
        exemples=[
            "Toutes doivent parler des soins de Fatou.",
            "Soulignez le verbe et vérifiez que le pronom est bien devant.",
        ],
        notes="Corriger la place du pronom avant tout. C'est le savoir de la séance ; "
              "le choix du bon pronom viendra avec la pratique.")

    return d.save(dossier)
