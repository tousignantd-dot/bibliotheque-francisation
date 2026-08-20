# -*- coding: utf-8 -*-
"""C1 · Pendant le repas.
Bloc C « Défi 2 · Pendant le repas » · couleur acier · 60 min.
Source : dialogue `t2`, exercices `t2vf` et `t2accomp`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-restaurant/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre='Pendant le repas',
        chapeau="Le serveur passe : « est-ce que tout va bien ? ». Le poisson "
                "d'Andrés est un peu froid. Faut-il le dire ? Il n'ose pas.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc C. Question d'entrée : « avez-vous déjà mangé un plat "
                  "froid sans rien dire ? ». Beaucoup de mains, et souvent des sourires "
                  "gênés.")

    d.objectifs([
        "demander une petite chose pendant le repas ;",
        "comprendre la question « est-ce que tout va bien ? » ;",
        "signaler un plat froid ou une erreur ;",
        "savoir que signaler n'est pas se plaindre.",
    ])

    d.declencheur(
        'Observation', "Votre plat arrive. Il est un peu froid. Que faites-vous ?",
        image=IMG + 'assiette-plat.jpg',
        pistes=[
            "Vous le mangez comme ça, ou vous le dites ?",
            "Qu'est-ce qui vous retient ?",
            "Que se passerait-il si vous le disiez ?",
            "Et dans votre pays, est-ce qu'on le dirait ?",
        ],
        notes="Cinq à dix minutes. La dernière piste ouvre une vraie discussion "
              "interculturelle : les usages varient beaucoup, et il vaut la peine de les "
              "comparer sans hiérarchie.")

    d.dialogue('Dialogue · 1 de 3', "Demander une petite chose", [
        ("VINCENT", "Est-ce que tout va bien ?", True),
        ("MANON", "Très bien, merci.", False),
        ("ANDRÉS", "Excusez-moi, est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?", True),
        ("VINCENT", "Tout de suite. Autre chose ?", True),
    ], consigne="Écoutez d'abord, diapo masquée.",
       notes="« Est-ce que tout va bien ? » est une question de service, posée à toutes les "
             "tables. On peut y répondre par « très bien, merci » — ou en profiter pour "
             "demander quelque chose.")

    d.dialogue('Dialogue · 2 de 3', "L'hésitation", [
        ("MANON", "Andrés, ton poisson est comment ?", False),
        ("ANDRÉS", "Très bon. Un peu froid, par exemple.", True),
        ("MANON", "Dis-le. Ils vont le réchauffer, ça arrive tout le temps.", True),
        ("ANDRÉS", "Je n'ose pas trop.", True),
    ], notes="« Par exemple » à la fin d'une phrase est un usage d'ici : il veut dire "
             "« cependant », « par contre ». Le signaler, il surprend souvent.")

    d.dialogue('Dialogue · 3 de 3', "Signaler", [
        ("MANON", "Ce n'est pas se plaindre, c'est normal. Regarde, je l'appelle.", True),
        ("ANDRÉS", "Excusez-moi, mon poisson est un peu froid. Est-ce que ce serait possible de le réchauffer ?", True),
        ("VINCENT", "Bien sûr, je suis désolé. Je vous le rapporte dans deux minutes.", True),
    ], notes="Le serveur s'excuse et corrige en deux minutes. C'est la réponse normale — et "
             "c'est ce qui rassure le plus les élèves.")

    d.tableau('Analyse', "Trois façons de demander",
              ['Pour', 'La formule'],
              [["Une petite chose", "Est-ce que je pourrais avoir…"],
               ["Une correction", "Est-ce que ce serait possible de…"],
               ["Attirer l'attention", "Excusez-moi…"]],
              cle=1,
              note="Le sel, l'eau, un couvert : rien de tout cela ne dérange.",
              notes="Diapo à photographier. Trois formules pour tout le repas.")

    d.regle("Signaler n'est pas se plaindre",
            "Le restaurant préfère le savoir.",
            precision="Un plat froid signalé se règle en deux minutes. Non signalé, il "
                      "gâche le repas — et le restaurant ne saura jamais pourquoi vous "
                      "n'êtes pas revenu. Ce n'est pas une plainte, c'est une information.",
            notes="Diapo à photographier. C'est la phrase de Manon, et c'est le cœur du "
                  "bloc C.")

    d.piege("Ne rien dire pour ne pas déranger",
            "C'est bon, je vais le manger comme ça.",
            "Mon poisson est un peu froid. Est-ce que ce serait possible de le réchauffer ?",
            "Le serveur a passé la table exprès pour poser la question. Ne rien dire ne le "
            "protège de rien : cela l'empêche seulement de faire son travail. Et vous "
            "mangez un plat froid que vous avez payé.",
            notes="Le dire sans jugement : cette retenue est très répandue, y compris chez "
                  "les gens d'ici.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le serveur vient demander si tout va bien.", "vrai"),
        ("Andrés demande du sel sèchement.", "faux — il emploie une forme polie"),
        ("Son poisson est trop chaud.", "faux — un peu froid"),
        ("Il veut le dire tout de suite.", "faux — il n'ose pas"),
        ("Manon lui dit que ce n'est pas se plaindre.", "vrai"),
        ("Le serveur refuse de le réchauffer.", "faux — il s'excuse et le fait"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte.")

    d.cartes("Ce qu'on demande pendant le repas", "Quatre choses ordinaires", [
        ("Du sel, du poivre",
         "Apportés en moins d'une minute. Personne ne s'en formalise."),
        ("De l'eau",
         "La carafe se remplit sans qu'on la paie. « Est-ce qu'on pourrait avoir de l'eau, "
         "s'il vous plaît ? »"),
        ("Un couvert, une serviette",
         "S'il en manque un, on le dit. C'est une erreur de dressage, pas une exigence."),
        ("Du pain",
         "Souvent renouvelé gratuitement si on le demande."),
    ], notes="Ces quatre demandes reviennent à chaque repas. Les faire répéter, avec la "
             "formule complète.")

    d.billet(
        "Écrivez quatre demandes pour pendant le repas.",
        exemples=[
            "Deux petites choses, une correction, une façon d'attirer l'attention.",
            "Employez les formules du tableau.",
        ],
        notes="Ramasser. Ces phrases servent au jeu de rôle de E1, cas « repas ».")

    return d.save(dossier)
