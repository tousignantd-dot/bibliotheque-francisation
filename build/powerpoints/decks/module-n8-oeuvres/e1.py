# -*- coding: utf-8 -*-
"""E1 · Proposez une lecture devant le cercle
Bloc E « Je me lance » · couleur teal · production orale · 75 min.
Source : section `appli` (jeu de rôle et production orale).
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Proposez une lecture devant le cercle",
        chapeau="Deux ou trois minutes debout. Ne racontez pas l'œuvre : le "
                "cercle la connaît. Proposez-en une lecture, appuyez-la, et "
                "dites ce que l'autre lecture explique mieux.",
        duree='75 minutes')

    d.titre(notes="Avant-dernière séance. Rendre les billets annotés de B4 et de D1 : "
                  "les trois phrases y sont déjà, il ne reste qu'à les tenir debout "
                  "pendant deux minutes.")

    d.objectifs([
        "tenir deux ou trois minutes de parole suivie devant le groupe ;",
        "séparer les faits de la lecture, à voix haute et dans cet ordre ;",
        "appuyer sa lecture sur deux détails qu'on peut montrer ;",
        "nommer soi-même la lecture opposée, et ce qu'elle explique mieux.",
    ], notes="Le quatrième objectif est ce qui distingue cette production d'un exposé "
             "d'opinion. Il est aussi le plus difficile à tenir sous le regard du "
             "groupe : prévoir de le rappeler entre chaque passage.")

    d.declencheur(
        'Préparation', "Qu'est-ce qui rend une prise de parole écoutable ?",
        pistes=[
            "Commencer par ce que tout le monde peut vérifier.",
            "Annoncer sa lecture comme une lecture, pas comme un fait.",
            "Un détail précis vaut mieux que trois adjectifs.",
            "Dire soi-même ce qui joue contre soi : cela ne se retourne jamais contre vous.",
        ],
        notes="Quatre pistes, quatre minutes. Ce sont les quatre critères de "
              "correction ; les annoncer avant les passages, pas après.")

    d.tableau('Analyse', "Trois temps, deux ou trois minutes",
              ['Le temps', 'Ce qu\'on y fait'],
              [["Temps 1", "les faits seuls, trois ou quatre phrases"],
               ["Temps 2", "votre lecture, et deux indices qui l'appuient"],
               ["Temps 3", "l'autre lecture, ce qu'elle explique mieux"]],
              cle=0,
              note="Le troisième temps est le plus court, et c'est celui qu'on retient.",
              notes="Diapositive à photographier, et à laisser affichée pendant tous "
                    "les passages : c'est la grille que le groupe suit en écoutant.")

    d.cartes('Analyse', "Ce que le troisième temps peut donner", [
        ("Une concession", "Bien sûr, la corde reste attachée."),
        ("Ce que l'autre explique mieux", "Cette lecture rend mieux compte des six épisodes."),
        ("Une hypothèse irréelle", "Si elle avait détaché la corde, on n'en parlerait pas."),
        ("Un doute assumé", "Il se peut donc qu'elle soit prise et qu'elle l'accepte."),
        ("Une reprise de l'indice", "La corde n'est pas ce qui la retient."),
        ("Une conclusion sans trancher", "Ce qui, au fond, reste un choix."),
    ], notes="Six formules, tirées des six séances de langue du module. En faire "
             "choisir deux à chacun avant de passer : cela structure le troisième "
             "temps, qui sinon s'évapore.")

    d.regle("On ne cherche pas à avoir raison",
            "On cherche la lecture qui explique le plus de détails, et on le dit.",
            precision="C'est la règle depuis A1, et c'est celle qui sera évaluée. Une "
                      "prise de parole qui nie l'autre lecture perd des points ; une "
                      "prise de parole qui la nomme et lui reconnaît quelque chose en "
                      "gagne, même si elle défend l'inverse.",
            notes="Diapositive à photographier. Le dire avant le premier passage, "
                  "textuellement : personne ne perd rien à concéder.")

    d.pratique('Répétition', "Le jeu de rôle, en dyades",
               "Dix minutes, puis on inverse.", [
        ("Vous proposez", "une lecture, appuyée sur deux détails"),
        ("L'autre conteste", "il a un indice, et il ne cède pas au volume"),
        ("Vous reformulez", "si je vous suis bien, vous y voyez..."),
        ("Vous retournez son indice", "ce n'est pas ce qui la retient, c'est..."),
        ("Il demande", "qu'est-ce qui vous fait dire ça ?"),
        ("Vous concluez", "sans trancher, en disant ce qu'il explique mieux"),
    ], corrige=False,
       notes="Répétition générale, en dyades, avant les passages devant le groupe. "
             "Ceux qui le souhaitent peuvent le refaire avec l'assistant du module, "
             "qui joue Léandre Pinsonneault et ne cède jamais devant l'insistance.")

    d.pratique('Production', "Les passages devant le cercle",
               "Deux ou trois minutes chacun. Le groupe écoute avec la grille.", [
        ("Ce qu'on note", "les faits ont-ils précédé la lecture ?"),
        ("Ce qu'on note", "deux détails précis, ou des adjectifs ?"),
        ("Ce qu'on note", "l'autre lecture a-t-elle été nommée ?"),
        ("Ce qu'on note", "une concession, une mise en relief ?"),
        ("Ce qu'on note", "la mélodie de la voix : plate, ou variée ?"),
        ("Ce qu'on ne note pas", "l'accent, la vitesse, les hésitations"),
    ], corrige=False,
       notes="La dernière ligne compte autant que les cinq autres. Le dire au groupe "
             "avant le premier passage : on n'évalue pas la fluidité, on évalue la "
             "construction.")

    d.billet(
        "Enregistrez votre passage dans le module, écoutez-vous une fois, et "
        "envoyez la version que vous préférez.",
        exemples=[
            "Vous pouvez recommencer autant de fois que vous voulez.",
            "L'assistant vous rend une rétroaction avant l'envoi.",
        ],
        notes="Le dépôt se fait depuis la section « Je me lance ». Rappeler que la "
              "correction de l'assistant reste privée : seul l'envoi atteint "
              "l'enseignante.")

    return d.save(dossier)
