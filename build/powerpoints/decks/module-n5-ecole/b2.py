# -*- coding: utf-8 -*-
"""B2 · La question glissée dans une phrase
Bloc B « Défi 1 · Prévenir de son absence » · couleur ambre · 75 min.
Source du module : exercices `t1int` et `t1tri`, mini-leçon `t1int`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="La question glissée dans une phrase",
        chapeau="« Est-ce que je garde ma place ? » n'a rien de fautif. Mais "
                "trois questions directes de suite, au comptoir, et le ton "
                "devient sec sans qu'on l'ait voulu. « Je voudrais savoir "
                "si je garde ma place » dit la même chose et laisse à "
                "l'autre le temps de chercher.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la plus rentable du module. L'interrogative "
                  "indirecte est le savoir du niveau 5 qui porte le plus de points, et "
                  "c'est aussi ce qui distingue une demande d'un interrogatoire.")

    d.objectifs([
        "transformer une question directe en question glissée dans une phrase ;",
        "remplacer « est-ce que » par « si » et « qu'est-ce que » par « ce que » ;",
        "supprimer l'inversion du sujet et le point d'interrogation ;",
        "employer quatre entrées : je voudrais savoir, pourriez-vous me dire, "
        "je ne sais pas, j'aimerais comprendre.",
    ], notes="Les quatre entrées sont à apprendre par cœur. Elles rendent la "
             "transformation automatique : dès qu'on a dit « je voudrais savoir », la "
             "suite se range toute seule.")

    d.regle("Deux transformations, et c'est tout",
            "« Est-ce que » devient « si ». « Qu'est-ce que » devient « ce que ».",
            precision="Les autres mots de question — quand, où, pourquoi, "
                      "comment, combien de — se replacent tels quels.",
            notes="Diapositive à photographier. Le groupe cherche toujours une troisième "
                  "règle : il n'y en a pas. Le dire clairement rassure et fait gagner "
                  "vingt minutes.")

    d.tableau('La même demande, deux fois', "Directe, puis glissée",
              ['Question directe', 'Question glissée'],
              [["Est-ce que je garde ma place ?",
                "Je voudrais savoir si je garde ma place."],
               ["Quand dois-je remettre le formulaire ?",
                "Pourriez-vous me dire quand je dois le remettre."],
               ["Qu'est-ce qu'il faut écrire ?",
                "Je ne sais pas ce qu'il faut écrire."],
               ["Le rattrapage se donne où ?",
                "J'aimerais comprendre où se donne le rattrapage."]],
              cle=1,
              notes="Faire produire la colonne de droite par le groupe, ligne par ligne, "
                    "avant de l'afficher. La deuxième ligne est celle où l'inversion "
                    "résiste : « quand dois-je » veut rester tel quel.")

    d.cartes("Les quatre entrées", "À savoir par cœur, comme quatre mots", [
        ("Je voudrais savoir…",
         "La plus neutre. Passe partout, à l'oral comme à l'écrit."),
        ("Pourriez-vous me dire…",
         "Plus polie. Elle finit par un point d'interrogation, exceptionnellement."),
        ("Je ne sais pas…",
         "Pour avouer qu'on ignore quelque chose sans avoir l'air perdu."),
        ("J'aimerais comprendre…",
         "Quand la réponse demande une explication, pas seulement un fait."),
    ], notes="Faire répéter les quatre debout, à voix haute, trois fois. Elles doivent "
             "sortir sans réfléchir au comptoir : c'est le seul moyen d'éviter le "
             "« est-ce que » qui traîne au milieu de la phrase.")

    d.pratique('Transformation', "Glissez la question dans la phrase",
               "À l'oral d'abord, puis à l'écrit.", [
        ("Est-ce que mon absence est autorisée ?",
         "Je voudrais savoir si mon absence est autorisée."),
        ("Quand est-ce que la réponse arrive ?",
         "Pourriez-vous me dire quand la réponse arrive."),
        ("Qu'est-ce qu'il faut mettre dans la case du motif ?",
         "Je ne sais pas ce qu'il faut mettre dans la case du motif."),
        ("Qu'est-ce qui manque dans mon dossier ?",
         "Dites-moi ce qui manque dans mon dossier."),
        ("Combien de jours ça prend ?",
         "Je voudrais savoir combien de jours ça prend."),
        ("Où se donne le rattrapage ?",
         "J'aimerais comprendre où se donne le rattrapage."),
    ], corrige=True,
       notes="Faire dire la phrase entière, jamais seulement le mot changé. La quatrième "
             "oppose « ce qui » à « ce que » : le mot fait l'action, donc « ce qui ».")

    d.regle("Trois signes de relecture",
            "Le point final. Le sujet devant son verbe. Aucun « est-ce que ».",
            precision="Un trait d'union entre le verbe et le pronom — « dois-je », "
                      "« avez-vous » — signale toujours une question directe.",
            notes="Diapositive à photographier. C'est le réflexe de relecture qui sert "
                  "en E2, quand chacun relira son propre courriel avant de l'envoyer.")

    d.piege("Laisser le « est-ce que » au milieu de la phrase",
            "Je voudrais savoir est-ce que je garde ma place.",
            "Je voudrais savoir si je garde ma place.",
            "Le « est-ce que » et le « si » font le même travail : il ne peut pas y "
            "en avoir deux. C'est la faute la plus visible du défi, et elle se "
            "corrige mécaniquement dès qu'on la repère.",
            notes="La faire produire volontairement par un ou deux élèves, puis corriger "
                  "ensemble. Une faute qu'on a dite exprès une fois se repère ensuite "
                  "beaucoup mieux dans sa propre production.")

    d.pratique('Tri', "Directe, ou glissée ?",
               "Levez la main gauche pour directe, la droite pour glissée.", [
        ("Est-ce que je garde ma place dans le groupe ?", "directe"),
        ("Je voudrais savoir si je garde ma place.", "glissée"),
        ("Quand dois-je remettre le formulaire ?", "directe"),
        ("Pourriez-vous me dire quand je dois le remettre ?",
         "glissée — le point d'interrogation est au « pourriez-vous »"),
        ("Qu'est-ce qu'il faut écrire dans la case ?", "directe"),
        ("J'aimerais comprendre où se donne le rattrapage.", "glissée"),
    ], corrige=True,
       notes="La quatrième ligne est le seul cas subtil du défi. Prendre le temps de "
             "l'expliquer : le point d'interrogation appartient à la phrase porteuse, "
             "pas à la question glissée.")

    d.billet(
        "Écrivez deux questions glissées que vous poserez au comptoir.",
        exemples=[
            "Une avec « si », une avec « quand » ou « combien de ».",
            "Relisez : point final, sujet devant, aucun « est-ce que ».",
        ],
        notes="Ramasser les billets et corriger les trois signes seulement. Ne pas "
              "corriger le reste : la séance porte sur un point, et un billet couvert "
              "de rouge décourage plus qu'il n'enseigne.")

    return d.save(dossier)
