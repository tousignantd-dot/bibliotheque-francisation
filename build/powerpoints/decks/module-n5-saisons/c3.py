# -*- coding: utf-8 -*-
"""C3 · Parce que, comme, puisque
Bloc C « Défi 2 · La décision, et pourquoi » · couleur ambre · 75 min.
Source : exercice `t2cause` et sa mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Parce que, comme, puisque",
        chapeau="« Les gens acceptent presque tout quand ils comprennent "
                "pourquoi. » Six connecteurs pour dire la raison, et ils ne "
                "se placent pas au même endroit : choisir le bon, c'est "
                "décider ce que le lecteur entendra en premier.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire du texte. Ouvrir en écrivant la même décision de "
                  "six façons au tableau et en demandant laquelle le groupe préfère "
                  "recevoir. Les avis diffèrent, et c'est le sujet de la séance : le "
                  "choix du connecteur est un choix de destinataire.")

    d.objectifs([
        "employer « parce que » après la décision, et jamais en tête de phrase ;",
        "employer « comme » en tête de phrase, et jamais ailleurs ;",
        "distinguer « puisque » d'« étant donné que » par le registre ;",
        "employer « donc » et « c'est pourquoi » pour la conséquence.",
    ], notes="Les deux premiers objectifs suffisent à un élève pressé ; les deux autres "
             "sont ce qui distingue un message correct d'un avis affiché qui a l'air "
             "écrit par le Centre. Ne pas sacrifier les deux derniers : la production "
             "écrite de E2 en dépend.")

    d.declencheur(
        'Comparaison', "Deux phrases, la même décision. Laquelle préférez-vous "
                       "recevoir ?",
        pistes=[
            "« La sortie est reportée parce qu'un avertissement est en vigueur. »",
            "« Comme un avertissement est en vigueur, la sortie est reportée. »",
            "Qu'est-ce que vous entendez en premier, dans chacune ?",
            "Devant trente personnes déçues, laquelle passe le mieux ?",
        ],
        notes="Il n'y a pas de bonne réponse et il faut le dire. Ce qui compte est que le "
              "groupe entende la différence d'ordre : la décision d'abord, ou la "
              "situation d'abord.")

    d.regle("Parce que vient après ; comme vient avant",
            "« La sortie est reportée parce qu'un avis est en vigueur. » "
            "« Comme un avis est en vigueur, la sortie est reportée. »",
            precision="« Comme » de cause ne se place qu'en tête de phrase. Au "
                      "milieu, il veut dire « de la même façon que » — autre chose.",
            notes="Diapositive à photographier. C'est la règle qui règle la moitié des "
                  "fautes de ce point. La faire produire dans les deux sens, cinq fois "
                  "chacun, avant de passer à la suite.")

    d.cartes("Six connecteurs", "Où chacun se place, et pour qui", [
        ("Parce que",
         "Après la décision. Le plus neutre : dans le doute, prenez celui-là."),
        ("Comme",
         "En tête de phrase seulement. La situation d'abord, la décision ensuite."),
        ("Puisque",
         "Une raison que l'autre connaît déjà. Sinon, il sonne prétentieux."),
        ("Étant donné que",
         "Le registre de l'avis affiché et du courriel de service."),
        ("Donc",
         "La conséquence, à l'oral. « Il y a un avertissement, donc on reporte. »"),
        ("C'est pourquoi",
         "La conséquence, à l'écrit. Il vient après la cause, jamais avant."),
    ], cols=2,
       notes="Faire produire une phrase par carte, sur la situation de son choix. Six "
             "phrases par élève, c'est beaucoup et c'est le bon nombre : le connecteur "
             "s'installe par l'usage, pas par la définition.")

    d.tableau('Deux directions', "Cause et conséquence",
              ['Ils disent la cause', 'Ils disent la conséquence'],
              [["parce que", "donc"],
               ["comme", "c'est pourquoi"],
               ["puisque", "par conséquent"],
               ["étant donné que", "—"]],
              note="Un seul connecteur par relation : jamais « comme… , donc… ».",
              notes="La note en bas est la faute la plus fréquente après celle de "
                    "« comme » au milieu. Une seule relation, un seul mot : le dire, "
                    "l'écrire, et corriger sans discuter pendant l'exercice.")

    d.piege("Mettre « comme » au milieu de la phrase",
            "La sortie est reportée comme il y a du verglas.",
            "La sortie est reportée parce qu'il y a du verglas.",
            "« Comme » de cause ne se place qu'en tête. Au milieu, employez "
            "« parce que » — c'est une règle sans exception.",
            notes="Elle vient souvent d'une traduction directe de l'anglais « as » ou de "
                  "l'espagnol « como ». Le nommer aide : la faute est logique, elle n'est "
                  "pas de l'inattention.")

    d.piege("Employer « puisque » avec une information neuve",
            "Puisqu'il tombera cinq millimètres de glace, la sortie est reportée. (À quelqu'un qui l'ignore.)",
            "Parce qu'il tombera cinq millimètres de glace, la sortie est reportée.",
            "« Puisque » s'appuie sur ce que l'autre sait déjà. Devant une "
            "information neuve, il donne l'impression de reprocher à l'autre de "
            "ne pas être au courant.",
            notes="Nuance fine mais réelle, et les élèves la sentent quand on la leur "
                  "fait entendre. Faire dire la même phrase avec les deux connecteurs, "
                  "sur un ton neutre : la différence s'entend.")

    d.pratique('Grammaire', "Complétez avec le bon connecteur",
               "parce que · comme · puisque · étant donné que · donc · "
               "c'est pourquoi", [
        ("La sortie est reportée ___ un avertissement est en vigueur.", "parce qu'"),
        ("___ les trottoirs seront glacés, nous préférons attendre.", "Comme"),
        ("___ vous avez tous reçu l'alerte, vous savez de quoi je parle.", "Puisque"),
        ("___ un avertissement est en vigueur, l'activité du 8 est reportée.", "Étant donné qu'"),
        ("Le parc est fermé jusqu'au 20 ; ___ nous avons choisi le 22.", "c'est pourquoi"),
        ("Il y a de la glace partout, ___ on ne sort pas.", "donc"),
    ], corrige=True,
       notes="Ce sont les six items de l'exercice t2cause du module. Faire remarquer les "
             "élisions — « parce qu' », « étant donné qu' » — qui sont une deuxième "
             "difficulté cachée dans le même exercice.")

    d.billet(
        "Reprenez votre décision de C2 et réécrivez-la trois fois, avec trois connecteurs différents.",
        exemples=[
            "Une version avec « parce que », une avec « comme », une avec « c'est pourquoi ».",
            "Laquelle enverriez-vous vraiment ? Écrivez pourquoi en une ligne.",
        ],
        notes="La dernière question est l'essentiel de la séance : le connecteur se "
              "choisit, il ne se subit pas. Ramasser les billets et en lire trois au "
              "début de C4.")

    return d.save(dossier)
