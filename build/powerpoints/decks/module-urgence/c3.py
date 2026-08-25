# -*- coding: utf-8 -*-
"""C3 · Dire à qui c'est.
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2app` — le lien d'appartenance.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Dire à qui c'est",
        chapeau="« Le dossier de Fatou », « sa sœur », « leur quart de travail ». Trois "
                "façons de dire l'appartenance — et une quatrième, que le français "
                "réserve aux parties du corps.",
        duree='60 minutes')

    d.titre(notes="Ouvrir en demandant comment on dit, dans la langue maternelle des "
                  "élèves, « le bras de Fatou ». Les constructions varient beaucoup : "
                  "c'est ce qui explique les erreurs.")

    d.objectifs([
        "employer mon, ma, mes, son, sa, ses correctement ;",
        "construire un lien d'appartenance avec « de » ;",
        "employer leur pour plusieurs possesseurs ;",
        "savoir pourquoi on dit « elle s'est brûlé le bras » et non « son bras ».",
    ])

    d.tableau('Analyse', "Trois façons de dire à qui c'est",
              ['La construction', 'Exemple', 'Quand'],
              [["déterminant possessif", "sa sœur", "on connaît la personne"],
               ["de + nom", "le dossier de Fatou", "on nomme la personne"],
               ["leur, leurs", "leur quart de travail", "plusieurs possesseurs"]],
              cle=0,
              note="Les trois disent la même chose. Le choix dépend de ce qu'on veut "
                   "mettre en avant : la personne, ou l'objet.",
              notes="Faire produire les trois formes pour un même contenu : « le "
                    "pansement de Fatou », « son pansement », et si elles sont "
                    "plusieurs, « leur pansement ».")

    d.tableau('Analyse', "Le déterminant s'accorde avec l'objet, pas avec le possesseur",
              ['Le possesseur', "L'objet", 'La forme'],
              [["Fatou (une femme)", "un bras (masculin)", "son bras"],
               ["Fatou (une femme)", "une sœur (féminin)", "sa sœur"],
               ["Mathieu (un homme)", "une sœur (féminin)", "sa sœur"],
               ["Mathieu (un homme)", "des gants (pluriel)", "ses gants"]],
              cle=2,
              note="« Son » et « sa » ne disent rien du genre du possesseur. C'est "
                   "l'objet qui décide.",
              notes="Erreur très fréquente chez les anglophones et les hispanophones. "
                    "Le dire clairement : « son bras » peut désigner le bras d'un homme "
                    "ou d'une femme.")

    d.regle('La règle des parties du corps',
            "Avec une partie du corps, le français emploie l'article, pas le possessif.",
            precision="« Elle s'est brûlé le bras », pas « son bras ». « Il s'est coupé "
                      "le doigt », pas « son doigt ». Le verbe pronominal dit déjà à qui "
                      "c'est : le répéter serait lourd.",
            notes="Relier à B3 : c'est le pronom « se » qui porte l'appartenance. Le "
                  "montrer en enlevant le pronom : « on lui a brûlé son bras » redevient "
                  "possible.")

    d.cartes('Ouvrir la mini-leçon', "Quatre choses à savoir en plus", [
        ("Mon, ton, son devant une voyelle",
         "Au féminin, devant une voyelle, on dit « mon » et non « ma » : mon épaule, "
         "mon ordonnance. C'est une question de son, pas de genre."),
        ("Leur, sans s devant un nom singulier",
         "« Leur quart de travail » — un seul quart pour toute l'équipe. « Leurs "
         "gants » — un pour chacun. C'est le nom qui décide, pas le nombre de "
         "personnes."),
        ("Le pronom « leur » ne prend jamais de s",
         "« Je leur ai parlé » : ici, leur remplace « à eux ». Devant un verbe, jamais "
         "de s ; devant un nom, il peut en prendre un."),
        ("« De » se contracte",
         "De + le donne du, de + les donne des : le dossier du patient, les gants des "
         "infirmières."),
    ], notes="La deuxième et la troisième carte se ressemblent et se confondent. Les "
             "traiter ensemble, avec le critère : qu'est-ce qui suit ?")

    d.pratique('Pratique · 1 de 3', "Complétez",
               "Choisissez le déterminant ou la préposition.", [
        ("C'est le dossier ___ Fatou.", "de"),
        ("Aminata vient chercher ___ sœur.", "sa"),
        ("Elle s'est brûlé ___ avant-bras.", "l'"),
        ("Les infirmières ont fini ___ quart de travail.", "leur"),
        ("Mathieu a oublié ___ gants dans la cuisine.", "ses"),
        ("C'est la sœur ___ patiente du 4B.", "de la"),
    ], corrige=True,
       notes="Le troisième item est le piège de la séance : la partie du corps prend "
             "l'article. Le corriger en dernier, après les autres.")

    d.piege('Le piège de la partie du corps',
            "Elle s'est brûlé son bras.",
            "Elle s'est brûlé le bras.",
            "Le pronom « se » dit déjà que c'est son propre bras. Ajouter « son » "
            "revient à le dire deux fois. Le français préfère l'article dans ce cas, "
            "alors que beaucoup d'autres langues gardent le possessif.",
            notes="Faire écouter la phrase fautive : elle est compréhensible mais elle "
                  "sonne étrangère. C'est le genre d'erreur qui subsiste longtemps.")

    d.piege("Le piège du genre du possesseur",
            "Fatou est arrivée avec sa frère.",
            "Fatou est arrivée avec son frère.",
            "« Son » et « sa » s'accordent avec l'objet possédé, jamais avec la personne "
            "qui possède. « Frère » est masculin, donc « son frère » — même si c'est "
            "Fatou qui a un frère.",
            notes="Faire produire cinq exemples au tableau, en alternant le genre du "
                  "possesseur et celui de l'objet. Le motif apparaît vite.")

    d.pratique('Pratique · 2 de 3', "Son, sa ou ses ?",
               "Regardez l'objet, pas la personne.", [
        ("Fatou et ___ pansement (masculin singulier)", "son pansement"),
        ("Fatou et ___ crème (féminin singulier)", "sa crème"),
        ("Mathieu et ___ gants (pluriel)", "ses gants"),
        ("Mathieu et ___ ordonnance (féminin, voyelle)", "son ordonnance"),
        ("Aminata et ___ sœur (féminin singulier)", "sa sœur"),
    ], corrige=True,
       notes="Le quatrième item introduit « mon, ton, son » devant une voyelle. Le "
             "signaler à la correction : c'est une exception de son, pas de genre.")

    d.pratique('Pratique · 3 de 3', "Réécrivez avec « de »",
               "Passez du déterminant possessif à la construction avec « de ».", [
        ("son dossier (celui de Fatou)", "le dossier de Fatou"),
        ("ses gants (ceux de Mathieu)", "les gants de Mathieu"),
        ("leur quart (celui des infirmières)", "le quart des infirmières"),
        ("sa sœur (celle d'Aminata)", "la sœur d'Aminata"),
    ], corrige=True,
       notes="La troisième et la quatrième demandent une contraction : « des » et "
             "« d' ». Les corriger ensemble.")

    d.billet(
        "Écrivez trois phrases sur les affaires de vos collègues.",
        exemples=[
            "Une avec un déterminant possessif, une avec « de », une avec « leur ».",
            "Ajoutez une quatrième phrase avec une partie du corps.",
        ],
        notes="La quatrième phrase est le vrai test : y a-t-il l'article ou le "
              "possessif ? C'est ce qu'il faut corriger en priorité.")

    return d.save(dossier)
