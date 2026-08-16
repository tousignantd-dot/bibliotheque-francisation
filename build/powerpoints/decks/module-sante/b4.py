# -*- coding: utf-8 -*-
"""B4 · Quand on n'a pas compris.
Bloc B « Défi 1 · À la pharmacie » · couleur teal (écoute et réponds) · 55 min.
Source du module : dialogue `t1` (les questions de Lina), exercice `co3`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre="Quand on n'a pas compris",
        chapeau="Le pharmacien parle vite, il y a du monde derrière vous, et vous "
                "hochez la tête. C'est le moment le plus fréquent — et le plus risqué — "
                "de tout le module.",
        duree='55 minutes')

    d.titre(notes="Séance courte et libératrice. Beaucoup d'élèves croient que demander "
                  "de répéter est impoli ou humiliant. C'est le contraire, et c'est ce "
                  "qu'il faut leur dire d'entrée.")

    d.objectifs([
        "demander de répéter, poliment et sans s'excuser longuement ;",
        "reformuler pour vérifier ce qu'on a compris ;",
        "demander d'écrire ce qui est important ;",
        "oser dire qu'on n'a pas compris.",
    ])

    d.declencheur(
        'Question d\'ouverture', "Vous n'avez pas compris la posologie. Qu'est-ce que vous faites ?",
        pistes=[
            "Est-ce qu'on ose demander une deuxième fois ? Une troisième ?",
            "Est-ce qu'on peut demander qu'on l'écrive ?",
            "Que risque-t-on à ne pas demander ?",
            "Est-ce qu'on peut rappeler la pharmacie plus tard ?",
        ],
        notes="La dernière question mérite une vraie réponse : oui, on peut rappeler, "
              "et c'est gratuit. Beaucoup l'ignorent.")

    d.regle('La règle du doute',
            "Un médicament mal compris ne se devine pas.",
            precision="Demander trois fois coûte trente secondes. Se tromper de dose "
                      "coûte beaucoup plus. Le pharmacien est payé pour expliquer, et il "
                      "préfère répéter.",
            notes="La diapositive à photographier. Le deuxième argument est celui qui "
                  "convainc : ce n'est pas une faveur qu'on demande.")

    d.tableau('Analyse', "Quatre façons de dire qu'on n'a pas compris",
              ['La formule', 'Ce qu\'elle obtient'],
              [["Pardon, pouvez-vous répéter ?", "la même phrase, une deuxième fois"],
               ["Est-ce que vous pouvez parler plus lentement ?",
                "la même phrase, plus lentement"],
               ["Donc c'est bien un comprimé le matin ?",
                "une confirmation, et la correction si on s'est trompé"],
               ["Est-ce que vous pouvez me l'écrire ?",
                "la consigne sur papier, à relire chez soi"]],
              cle=0,
              note="La troisième est la plus efficace : elle montre ce qu'on a compris.",
              notes="Faire remarquer que la quatrième est toujours acceptée en "
                    "pharmacie : l'étiquette est justement faite pour ça.")

    d.piege("Le piège du hochement de tête",
            "(On hoche la tête et on sort.)",
            "Pardon, je n'ai pas bien compris. Un comprimé, deux fois par jour ?",
            "Hocher la tête met fin à la conversation et laisse le pharmacien croire que "
            "tout est clair. Il n'a alors aucune raison de reformuler — et l'erreur de "
            "dose se découvre à la maison, le soir.",
            notes="Ne pas culpabiliser : ce réflexe est universel quand on apprend une "
                  "langue. Le nommer suffit à le désamorcer.")

    d.pratique('Pratique · 1 de 3', "Reformulez pour vérifier",
               "Transformez la consigne en question de confirmation.", [
        ("« Un comprimé deux fois par jour, matin et soir. »",
         "Donc un le matin et un le soir, c'est bien ça ?"),
        ("« Pendant sept jours, avec de la nourriture. »",
         "Donc toute la semaine, pendant les repas ?"),
        ("« Pas d'alcool pendant le traitement. »",
         "Donc pas de vin ni de bière pendant sept jours ?"),
        ("« Revenez si la fièvre ne baisse pas en deux jours. »",
         "Donc je reviens jeudi si j'ai encore de la fièvre ?"),
    ], corrige=True,
       notes="Le mot « donc » ouvre les quatre. C'est le mot outil de la séance : "
             "l'écrire au tableau et le laisser.")

    d.pratique('Pratique · 2 de 3', "Choisissez votre formule",
               "Quelle phrase employez-vous dans chaque cas ?", [
        ("Il a parlé trop vite, vous n'avez rien saisi.",
         "Pardon, pouvez-vous répéter plus lentement ?"),
        ("Vous avez compris, mais vous voulez être sûr.",
         "Donc c'est bien deux comprimés par jour ?"),
        ("Vous avez compris, mais vous allez oublier.",
         "Est-ce que vous pouvez me l'écrire ?"),
        ("Vous êtes déjà rentré chez vous et vous doutez.",
         "Je rappelle la pharmacie — c'est gratuit."),
    ], corrige=True,
       notes="Les quatre situations sont différentes et appellent des formules "
             "différentes. C'est le point de la séance : choisir, pas réciter.")

    d.pratique('Pratique · 3 de 3', "Le pharmacien pressé",
               "À deux. Le pharmacien parle vite ; le client fait ce qu'il faut.", [
        ("Le pharmacien débite la posologie", "vite, en une seule phrase"),
        ("Le client demande de répéter", "poliment, sans longues excuses"),
        ("Le pharmacien répète", "un peu plus lentement"),
        ("Le client reformule", "« Donc c'est bien… »"),
        ("Le client demande l'écrit", "si c'est compliqué"),
    ], corrige=False,
       notes="Vingt minutes, puis on échange. Demander à celui qui joue le pharmacien de "
             "parler VRAIMENT vite : c'est ce qui rend l'exercice utile.")

    d.billet(
        "Écrivez la formule que vous allez employer la prochaine fois.",
        exemples=[
            "Une seule phrase, celle que vous vous sentez capable de dire.",
            "Apprenez-la par cœur : elle doit sortir sans réfléchir.",
        ],
        notes="Ramasser. À la séance suivante, commencer par faire dire ces phrases "
              "debout, une par élève : trente secondes, et elles s'installent.")

    return d.save(dossier)
