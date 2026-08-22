# -*- coding: utf-8 -*-
"""C3 · Mon billet, votre dossier.
Bloc C « Défi 2 · Le billet d'absence » · couleur ambre (écriture) · 60 min.
Source : exercice `t2poss`, mini-leçon `t2poss`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='Mon billet, votre dossier',
        chapeau="Au comptoir, il y a toujours deux personnes et beaucoup de "
                "papiers. Les mots qui disent à qui appartient quoi sont donc "
                "partout — et ils vont deux par deux.",
        duree='60 minutes')

    d.titre(notes="Séance d'écriture. Le point est simple, mais l'erreur qu'il corrige "
                  "est tenace : choisir le déterminant d'après la personne qui parle "
                  "plutôt que d'après le mot qui suit.")

    d.objectifs([
        "employer mon, ma, mes ;",
        "employer votre et vos ;",
        "accorder avec le nom qui suit, jamais avec la personne ;",
        "employer mon devant un nom féminin qui commence par une voyelle.",
    ])

    d.tableau('Analyse', "Ce qui est à moi",
              ["Devant quoi", "On dit"],
              [["un nom masculin", "mon billet, mon dossier, mon groupe"],
               ["un nom féminin", "ma fille, ma carte, ma journée"],
               ["plusieurs noms", "mes papiers, mes journées, mes enfants"],
               ["une voyelle", "mon absence, mon attestation, mon adresse"]],
              cle=1,
              note="La dernière ligne concerne des noms féminins : on dit "
                   "« mon » parce que « ma absence » serait trop dur à dire.",
              notes="Diapo à photographier. Faire lire la quatrième ligne deux fois : "
                    "c'est celle qui surprend, et elle contient deux mots du module.")

    d.regle("C'est le mot qui suit qui décide",
            "un homme dit « ma fille », une femme dit « mon billet »",
            precision="Le déterminant s'accorde avec le nom qui suit, jamais "
                      "avec la personne qui parle. C'est différent de "
                      "l'anglais, et c'est l'erreur la plus fréquente du "
                      "point.",
            notes="Diapo à photographier. Faire l'essai : demander à un homme de dire "
                  "« ma fille », à une femme de dire « mon billet ». Le groupe entend "
                  "que rien ne cloche.")

    d.tableau('Analyse', "Ce qui est à vous, et le miroir",
              ["Elle dit", "Vous répondez"],
              [["votre nom", "mon nom"],
               ["votre dossier", "mon dossier"],
               ["vos journées", "mes journées"],
               ["vos papiers", "mes papiers"]],
              cle=1,
              note="Votre ne change pas entre masculin et féminin : une forme "
                   "de moins à retenir.",
              notes="Diapo à photographier. Faire jouer les quatre échanges en paires, "
                    "debout. Le miroir se retient par le corps plus que par la règle.")

    d.pratique('Écriture', "Mon, ma, mes, votre ou vos ?",
               "Complétez chaque phrase.", [
        ("Voici ___ billet de la clinique.", "mon"),
        ("___ fille avait un rendez-vous jeudi.", "Ma"),
        ("La secrétaire écrit dans ___ dossier, madame Belkacem.", "votre"),
        ("Est-ce que ___ journées d'absence sont justifiées ?", "vos"),
        ("J'ai perdu ___ papiers dans l'autobus.", "mes"),
        ("Je viens chercher ___ attestation de fréquentation.", "mon"),
    ], corrige=True,
       notes="Faire écrire, puis faire dire qui parle à chaque ligne. La dernière est "
             "le piège de la voyelle : attestation est féminin.")

    d.piege("Choisir d'après la personne qui parle",
            "ma billet, parce que je suis une femme",
            "mon billet",
            "Le déterminant regarde le mot d'après, pas celui qui parle. « Billet » est "
            "masculin : tout le monde dit « mon billet ». « Fille » est féminin : tout "
            "le monde dit « ma fille ».",
            notes="Erreur logique, donc tenace. La nommer une fois clairement vaut mieux "
                  "que la corriger dix fois en passant.")

    d.cartes("Les mots du module qui prennent mon", "Trois féminins surprenants", [
        ("mon absence",
         "Le mot est féminin — une absence — mais il commence par une voyelle : on dit "
         "mon."),
        ("mon attestation",
         "Même chose. Et l'adjectif reste au féminin : « mon attestation est prête », "
         "jamais « prêt »."),
        ("mon enseignante",
         "Le genre n'a pas changé : c'est seulement la prononciation qui a choisi le "
         "déterminant."),
    ], cols=3,
       notes="Faire chercher d'autres exemples dans le vocabulaire du module et des "
             "modules précédents : mon adresse, mon école, mon amie.")

    d.billet(
        "Écrivez quatre phrases : deux avec mon ou ma, deux avec votre ou vos.",
        exemples=[
            "« Voici mon billet et ma carte d'élève. »",
            "« Est-ce que vos bureaux sont ouverts le vendredi ? »",
        ],
        notes="Devoir d'écriture. Ramasser : c'est un point qui se corrige bien à "
              "l'écrit et mal à l'oral.")

    return d.save(dossier)
