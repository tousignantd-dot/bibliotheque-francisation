# -*- coding: utf-8 -*-
"""C1 · Est-ce que je peux… ?
Bloc C « Défi 2 · Permission, retard, absence » · couleur acier · 75 min.
Source : dialogue `t2`, exercices `t2vf` et `t2peux`, mini-leçon `t2peux`.

La séance de production orale du Défi 2. Le programme du niveau 2 met
« pouvoir » et « devoir » parmi ses auxiliaires de modalité : la salle de
classe en fait un usage quotidien, et la même formule servira ensuite au
guichet, à la clinique et au bureau du secrétariat.

Une seule structure à installer, et elle ne varie pas : « Est-ce que je peux »
plus un verbe qui ne se conjugue jamais.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-classe/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Est-ce que je peux… ?",
        chapeau="Une seule formule, et elle sert partout : en classe, au "
                "guichet, à la clinique.",
        duree='75 minutes')

    d.titre(notes="Première séance du Défi 2. Commencer par demander au groupe ce qu'ils "
                  "n'osent pas demander en classe. La liste est toujours la même : "
                  "sortir, boire, emprunter un crayon.")

    d.objectifs([
        "demander une permission avec « est-ce que je peux » ;",
        "garder le deuxième verbe à l'infinitif ;",
        "reconnaître trois réponses possibles ;",
        "ajouter une raison en trois mots.",
    ])

    d.declencheur(
        'Observation', "Qu'est-ce qu'on demande ici ?",
        image=IMG + 'horloge-classe.jpg',
        pistes=[
            "Il est dix heures moins cinq. Que veut l'élève ?",
            "Comment est-ce qu'il le demande ?",
            "Qu'est-ce que l'enseignante peut répondre ?",
            "Et si elle dit « pas maintenant » ?",
        ],
        notes="La dernière piste évite un malentendu fréquent : « pas maintenant » n'est "
              "pas un refus, c'est « redemande dans deux minutes ». Beaucoup d'élèves "
              "l'entendent comme un non définitif et n'osent plus rien demander.")

    d.dialogue('Dialogue', "Trois demandes de suite", [
        ("TARIQ", "Madame, est-ce que je peux sortir deux minutes ?", True),
        ("MADAME LEDUC", "Oui, bien sûr. La pause est à dix heures.", True),
        ("TARIQ", "Merci. Est-ce que je peux prendre mon téléphone ?", True),
        ("MADAME LEDUC", "Non. En classe, le téléphone est interdit.", True),
        ("TARIQ", "D'accord. Et l'eau ?", True),
        ("MADAME LEDUC", "L'eau, c'est permis. Le café aussi.", True),
    ], consigne="Écoutez deux fois, puis comptez les oui et les non.",
       notes="Deux oui, un non, et la conversation continue quand même. Faire remarquer "
             "que Tariq ne se vexe pas : il dit « d'accord » et il demande autre chose.")

    d.tableau('Analyse', "La formule, en trois morceaux",
              ["Le morceau", "Ce qu'on met"],
              [["le début", "Est-ce que je peux"],
               ["le verbe", "sortir · ouvrir · prendre · boire"],
               ["la politesse", "s'il vous plaît"],
               ["plus court, à l'oral", "Je peux sortir ? — la voix monte"]],
              cle=2,
              note="Le deuxième verbe ne se conjugue jamais : il reste comme dans le "
                   "dictionnaire.",
              notes="Diapositive à photographier. Faire construire cinq demandes au "
                    "tableau en piochant dans la deuxième ligne.")

    d.regle("Le deuxième verbe ne bouge pas",
            "Après « je peux », le verbe reste tel quel.",
            precision="On dit « je peux <b>sortir</b> », jamais « je peux je sors ». "
                      "C'est vrai aussi après <b>devoir</b> et après <b>il faut</b> : "
                      "vous devez <b>téléphoner</b>, il faut <b>être</b> à l'heure.",
            notes="Diapositive à photographier. La règle vaut pour tout le reste du "
                  "programme : la nommer maintenant fait gagner des mois.")

    d.regle("Une raison en trois mots",
            "Elle fait presque toujours dire oui.",
            precision="« Est-ce que je peux ouvrir la fenêtre ? <b>Il fait chaud.</b> » "
                      "« Est-ce que je peux partir plus tôt ? <b>J'ai un "
                      "rendez-vous.</b> » Trois mots après la demande, jamais une "
                      "longue explication.",
            notes="Diapositive à photographier. Insister : au Québec, une raison courte "
                  "est polie ; une longue justification met l'interlocuteur mal à "
                  "l'aise.")

    d.pratique('Production orale', "Que dites-vous ?",
               "Formulez la demande à voix haute.", [
        ("Vous voulez sortir deux minutes.", "Est-ce que je peux sortir deux minutes ?"),
        ("Vous n'avez pas de crayon.", "Est-ce que je peux prendre un crayon ?"),
        ("Il fait chaud dans la classe.", "Est-ce que je peux ouvrir la fenêtre ?"),
        ("Vous voulez boire de l'eau.", "Est-ce que je peux boire de l'eau ?"),
        ("Vous n'avez pas compris.", "Pouvez-vous répéter, s'il vous plaît ?"),
    ], corrige=True, cols=1,
       notes="Ce sont les cinq énoncés de l'exercice 2 du module en ligne. Les faire à "
             "l'oral ici, chacun deux fois : la voix doit monter à la fin.")

    d.cartes("Les trois réponses qu'on entend", "À reconnaître tout de suite", [
        ("Oui, bien sûr.",
         "C'est un oui. On dit merci et on y va."),
        ("Oui, mais attends deux minutes.",
         "C'est un oui aussi. L'enseignante finit son explication."),
        ("Non, pas maintenant.",
         "Ce n'est pas un refus définitif : on redemande à la pause."),
    ], cols=3, notes="Trois cartes, et la troisième est la plus importante. La faire lire "
                     "à voix haute par trois élèves différents.")

    d.pratique('Pratique · à deux', "Dix demandes en dix minutes",
               "Deux par deux, l'un joue l'enseignante.", [
        ("Étape 1", "L'élève demande une permission, avec sa raison."),
        ("Étape 2", "L'enseignante répond par l'une des trois réponses."),
        ("Étape 3", "L'élève remercie, ou redemande autrement."),
        ("Étape 4", "On change de rôle après cinq demandes."),
    ], cols=1,
       notes="Vingt minutes. Compter les demandes à voix haute : dix par élève, et la "
             "formule est installée pour de bon.")

    d.billet(
        "Écrivez trois permissions que vous voulez demander cette semaine.",
        exemples=[
            "Est-ce que je peux sortir deux minutes ?",
            "Est-ce que je peux prendre une feuille ?",
            "Est-ce que je peux partir à midi ? J'ai un rendez-vous.",
        ],
        notes="Devoir court. Demander qu'ils les posent vraiment, et qu'ils racontent au "
              "cours suivant ce qu'on leur a répondu.")

    return d.save(dossier)
