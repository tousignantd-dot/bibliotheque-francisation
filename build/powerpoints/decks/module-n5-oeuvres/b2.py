# -*- coding: utf-8 -*-
"""B2 · Raconter au présent
Bloc B « Défi 1 · Ce que raconte l'histoire » · couleur ambre · 75 min.
Source : exercice `t1pres`, mini-leçon `t1pres`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='ambre',
        titre="Raconter au présent",
        chapeau="Le livre est écrit au passé, l'autrice l'a fini il y a "
                "trois ans — et tout le monde le raconte au présent. Ce "
                "n'est pas une règle de grammaire : c'est ce qui place la "
                "personne qui écoute à l'intérieur de la scène, au moment "
                "où ça arrive.",
        duree='75 minutes')

    d.titre(notes="Séance de langue. Faire l'expérience dès le début : dire au groupe "
                  "« elle est arrivée au village, elle a ouvert la maison, elle a trouvé "
                  "une boîte », puis la même chose au présent. Demander laquelle des deux "
                  "donne envie. Le groupe choisit toujours la seconde, sans savoir "
                  "pourquoi. La séance le dit.")

    d.objectifs([
        "employer le présent pour raconter ce qui arrive dans une œuvre ;",
        "distinguer l'action en cours de l'action habituelle ;",
        "dire deux choses en même temps sans changer de temps ;",
        "tenir le présent jusqu'au bout, sans glisser au passé composé.",
    ], notes="Le quatrième objectif est le vrai travail de la séance. Passer au présent "
             "est facile ; y rester pendant cinq phrases l'est moins, et le mélange est "
             "la faute la plus audible d'une présentation.")

    d.declencheur(
        'Comparaison', "« Elle arrive au village » ou « elle est arrivée au "
                       "village » ? Les deux sont corrects. Lequel préférez-vous ?",
        pistes=[
            "Lequel vous met dans l'histoire ? Lequel vous en tient dehors ?",
            "Regardez le dos d'un livre : à quel temps est le résumé ?",
            "Et une bande-annonce de film, elle parle à quel temps ?",
            "Est-ce que ça change quelque chose à ce qui est raconté ?",
        ],
        notes="Apporter deux ou trois livres et faire lire les quatrièmes de couverture à "
              "voix haute. Elles sont toutes au présent, sans exception — c'est la preuve "
              "la plus rapide, et elle ne vient pas de l'enseignante.")

    d.regle("Le présent place l'autre dans la scène",
            "Au passé, votre récit devient un rapport. Au présent, il devient "
            "une scène.",
            precision="« Elle arrive. Elle ouvre la maison. Elle trouve une boîte de "
                      "lettres. » Trois verbes, trois moments, et la personne en face "
                      "avance avec le personnage. C'est le temps de tous les résumés "
                      "du monde, et il ne demande aucune conjugaison difficile.",
            notes="Diapositive à photographier. Le présent est aussi le temps le plus "
                  "simple à conjuguer, ce qui est un cadeau à ce niveau-ci : l'élève peut "
                  "penser à ce qu'il raconte plutôt qu'à sa grammaire.")

    d.tableau('Deux emplois, un seul temps', "Ce qui décide, c'est le mot devant",
              ['Ce qui arrive maintenant', 'Ce qui se répète'],
              [["Elle arrive au village.", "Tous les soirs, elle marche jusqu'au quai."],
               ["Elle ouvre la maison.", "Chaque matin, elle ouvre les volets."],
               ["Le personnage hésite.", "D'habitude, il ne répond pas."],
               ["La porte s'ouvre.", "Le dimanche, personne ne travaille."],
               ["Aucun mot devant", "Tous les soirs · chaque matin · d'habitude"]],
              cle=1,
              notes="La dernière rangée est la règle : le verbe ne change pas, seul le "
                    "repère de temps change. C'est un savoir du programme de niveau 5 — "
                    "distinguer l'action en cours de l'action habituelle. Le français les "
                    "met au même temps, et laisse le repère faire le travail.")

    d.cartes("Les verbes de tous les résumés", "À la troisième personne, au présent", [
        ("il s'appelle · elle vit",
         "On présente le personnage : qui il est, où il vit."),
        ("il rencontre · elle découvre",
         "L'évènement qui met l'histoire en marche."),
        ("elle veut · il refuse",
         "Le désir et l'obstacle : le cœur du temps 3."),
        ("elle décide · il part",
         "Le moment du choix — c'est là qu'on s'arrête."),
    ], notes="Ces huit verbes couvrent presque tous les résumés. Les faire apprendre comme "
             "du vocabulaire, à la troisième personne du présent, plutôt que comme une "
             "conjugaison complète : c'est la seule forme dont l'élève aura besoin.")

    d.pratique('Conjugaison', "Mettez le verbe au présent",
               "Le verbe est entre parenthèses. Restez au présent partout.", [
        ("Une femme ___ (revenir) au village après vingt ans.", "revient"),
        ("Elle ___ (vouloir) repartir le jour même.", "veut"),
        ("Le personnage principal ___ (ouvrir) la maison de sa mère.", "ouvre"),
        ("Dans le grenier, elle ___ (découvrir) une boîte de lettres.", "découvre"),
        ("Tous les soirs, elle ___ (marcher) jusqu'au quai.", "marche"),
        ("Pendant qu'elle range la maison, elle ___ (relire) les lettres.", "relit"),
    ], corrige=True,
       notes="C'est l'exercice `t1pres` du module interactif. Les cinquième et sixième "
             "lignes sont les plus instructives : la cinquième est une habitude, la "
             "sixième deux actions au même moment. Les faire justifier.")

    d.regle("Deux choses en même temps, deux présents",
            "Pendant qu'elle range la maison, elle relit les lettres.",
            precision="Les deux verbes restent au présent : rien n'est décalé, tout se "
                      "passe au même moment de l'histoire. C'est la façon la plus simple "
                      "de dire la simultanéité, et elle suffit largement pour deux "
                      "minutes. Le gérondif — « en rangeant la maison » — dit la même "
                      "chose en moins de mots, et un seul par présentation fait bon effet.",
            notes="Le gérondif est au programme du niveau 5 pour la simultanéité et la "
                  "manière. L'introduire ici sans l'exiger : les élèves rapides s'en "
                  "empareront, les autres garderont « pendant que », qui est juste.")

    d.piege("Changer de temps au milieu du résumé",
            "Elle arrive au village et elle a trouvé une boîte de lettres.",
            "Elle arrive au village et elle trouve une boîte de lettres.",
            "Une fois au présent, il faut y rester jusqu'à la fin. Le mélange est la "
            "faute la plus audible d'une présentation : l'auditeur ne sait plus s'il "
            "est dans l'histoire ou dans votre souvenir de l'histoire.",
            notes="Exercice de correction : lire au groupe un court résumé où deux verbes "
                  "sur six sont au passé composé, et demander de les attraper. Ils les "
                  "entendent, même quand ils font eux-mêmes la faute.")

    d.pratique('À l\'oral', "Trois phrases de suite, au présent",
               "Racontez le début de votre œuvre. Trois verbes, trois moments.", [
        ("Phrase 1 — ce que fait le personnage en premier.",),
        ("Phrase 2 — ce qui arrive ensuite.",),
        ("Phrase 3 — ce qui complique tout.",),
        ("Redites les trois d'affilée, sans vous arrêter entre elles.",),
    ], notes="Deux par deux d'abord, puis trois ou quatre passages devant le groupe. "
             "L'auditeur a une seule tâche : lever la main s'il entend un passé composé. "
             "C'est le meilleur exercice d'écoute de la séance.")

    d.billet(
        "Écrivez trois phrases au présent qui racontent le début de votre œuvre.",
        exemples=[
            "Trois verbes différents, trois moments qui se suivent.",
            "Ajoutez une quatrième phrase avec « tous les soirs » ou « chaque matin ».",
        ],
        notes="Le billet complète les temps 1 à 3 écrits en B1 : l'élève a maintenant la "
              "moitié de sa présentation. La quatrième phrase vérifie l'habitude, qui est "
              "le point du programme le plus vite oublié.")

    return d.save(dossier)
