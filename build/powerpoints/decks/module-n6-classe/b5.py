# -*- coding: utf-8 -*-
"""B5 · De, à, ou rien — et donne-le-moi
Bloc B « Défi 1 » · couleur ambre · 75 min. Grammaire de la phrase.
Source du module : exercices `t1inf` et `t1imper`, et leurs deux mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B5', section='ambre',
        titre="De, à, ou rien — et donne-le-moi",
        chapeau="Deux points de grammaire, et les deux sortent de la même "
                "feuille : une consigne est pleine de verbes qui en appellent "
                "d'autres, et une équipe passe ses journées à se demander "
                "des choses.",
        duree='75 minutes')

    d.titre(notes="Deux savoirs distincts dans la même séance, mais le lien "
                  "est réel : le premier sert à lire la consigne, le second à "
                  "travailler avec les autres.")

    d.objectifs([
        "employer « de », « à » ou rien devant un verbe à l'infinitif ;",
        "reconnaître les huit verbes qui ne veulent aucune préposition ;",
        "donner un ordre avec deux pronoms : donne-le-moi ;",
        "savoir que tout change de place à la forme négative.",
    ], notes="Le premier savoir a huit points au programme du niveau 6, le "
             "second un seul. Répartir le temps en conséquence : quarante "
             "minutes, puis vingt-cinq.")

    d.declencheur(
        'Observation', "Pourquoi dit-on « réussir à » et « décider de » ?",
        pistes=[
            "Est-ce qu'il y a une logique ?",
            "Comment faites-vous, vous, pour vous en souvenir ?",
            "Que se passe-t-il quand on se trompe ?",
        ],
        notes="La réponse honnête à la première question est : il n'y en a "
              "pas. Le dire tout de suite soulage le groupe et évite une "
              "demi-heure de recherche d'une règle inexistante.")

    d.tableau('Analyse', "Trois familles de verbes",
              ['La famille', 'Les verbes'],
              [["avec de", "demander, oublier, choisir, décider, accepter, éviter"],
               ["avec à", "réussir, apprendre, commencer, aider, hésiter, arriver"],
               ["avec rien", "espérer, vouloir, pouvoir, devoir, savoir, aimer"]],
              cle=0,
              note="Le choix appartient au verbe, comme le genre appartient au nom. On l'apprend avec lui.",
              notes="Diapositive à photographier. Faire lire les trois listes "
                    "à voix haute, chacune d'un trait : c'est l'oreille qui "
                    "les retiendra, pas la logique.")

    d.regle("Devant une voyelle, « de » devient « d' » ; « à » ne change jamais",
            "Il a oublié d'écrire son nom. · Ils ont commencé à écrire.",
            precision="Dites la phrase à voix haute : « de écrire » ne se "
                      "prononce pas, la bouche le refuse avant que l'œil le "
                      "voie.",
            notes="Diapositive à photographier. C'est la faute d'orthographe "
                  "la plus facile à éliminer de toutes, et elle compte dans "
                  "la ligne « langue » de la grille.")

    d.pratique('Pratique', "De, à, ou rien ?",
               "Écrivez le verbe entre parenthèses avec ce qu'il faut devant.", [
        ("Elle demande ... le plan avec le texte. (remettre)", "de remettre"),
        ("Il a oublié ... les verbes de la consigne. (souligner)", "de souligner"),
        ("Ils ont réussi ... une troisième source. (trouver)", "à trouver"),
        ("Marisol a appris ... une source. (juger)", "à juger"),
        ("Ils espèrent ... avant le 24 novembre. (finir)", "finir"),
        ("Ils ont commencé ... le lundi soir. (écrire)", "à écrire"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t1inf` du module, en cols:1 comme lui : les "
             "items font deux phrases et deux colonnes les rendraient "
             "illisibles.")

    d.regle("Verbe, puis la chose, puis la personne",
            "Donne-le-moi. Montre-les-moi. Envoyez-la-nous.",
            precision="L'ordre ne bouge jamais. Le verbe en -er garde sa "
                      "forme sans « s » : donne-le-moi, jamais "
                      "« donnes-le-moi ».",
            notes="Diapositive à photographier. « Donne-moi-le » s'entend ici "
                  "et là ; dire que c'est l'autre forme qui s'écrit, sans "
                  "porter de jugement sur celle qu'ils entendent dehors.")

    d.piege('Grammaire',
            "employer la même forme à la négative",
            "apprendre les deux formes séparément",
            "À la négative, tout change de place : « Ne me le donne pas. » "
            "Les pronoms repassent devant le verbe et leur ordre s'inverse. "
            "N'essayez pas de relier les deux formes par une règle : "
            "apprenez-les comme deux phrases différentes.",
            notes="Ne pas s'attarder : la forme négative n'est pas au "
                  "programme du niveau, elle est ici pour qu'on ne la "
                  "construise pas par analogie.")

    d.pratique('Pratique', "Redites-le en trois mots",
               "Récrivez la demande à l'impératif, avec les deux pronoms.", [
        ("Vous devez me remettre le plan.", "Remettez-le-moi."),
        ("Tu dois me montrer les trois sources.", "Montre-les-moi."),
        ("Vous devez nous envoyer la grille.", "Envoyez-la-nous."),
        ("Tu dois me rendre le cahier.", "Rends-le-moi."),
        ("Vous devez nous expliquer les étapes.", "Expliquez-les-nous."),
        ("Tu dois me redire la date.", "Redis-la-moi."),
    ], corrige=True, cols=2,
       notes="C'est l'exercice `t1imper` du module. Faire dire à voix haute "
             "avant d'écrire : les traits d'union viennent tout seuls une "
             "fois que le rythme est là.")

    d.billet(
        "Écris une demande que tu vas faire à ton équipe cette semaine.",
        exemples=[
            "Avec deux pronoms : envoie-les-moi, montre-le-moi, redis-la-nous.",
            "Une seule phrase.",
        ],
        notes="Deux minutes. Les demandes écrites sont souvent réelles — "
              "s'en servir pour lancer la rencontre d'équipe de la séance E1.")

    return d.save(dossier)
