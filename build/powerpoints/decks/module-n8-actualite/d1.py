# -*- coding: utf-8 -*-
"""D1 · La tribune, et ce qu'on répond quand on vous contredit
Bloc D « Défi 3 · Prendre position » · couleur acier · 75 min.
Source : dialogue `t3` (tribune téléphonique de CIRC), exercices `t31` et
`t3repli`, et la mini-leçon `t3repli`.
Tout le dossier est inventé : Rivière-aux-Cèdres, le boisé Sainte-Perpétue,
Habitations Verchères-Nord, la radio communautaire CIRC.
"""
from theme import Deck

import pathlib

IMG = str(pathlib.Path(__file__).resolve().parents[4]
          / 'assets' / 'interactive' / 'module-n8-actualite' / 'images') + '/'


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Deux minutes d'antenne, et quelqu'un qui vous contredit",
        chapeau="Le défi 3 ne travaille plus la lecture : il travaille le "
                "désaccord tenu à voix haute. Concéder, rectifier, esquiver — "
                "et l'auditoire entend toujours laquelle des trois vous avez "
                "choisie.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D. Dire d'emblée que la séance ne porte pas sur "
                  "qui a raison dans le dossier du boisé : elle porte sur la façon de "
                  "répondre. Les deux camps du dialogue sont défendables, et c'est "
                  "voulu.")

    d.objectifs([
        "suivre une tribune téléphonique à quatre voix et dire qui demande quoi ;",
        "reconnaître ce que fait une réponse : concéder, rectifier ou esquiver ;",
        "concéder un point exact, puis avancer le sien dans la phrase suivante ;",
        "refuser une rumeur qu'on vous tend, sans se fâcher et sans la répéter.",
    ], notes="Le quatrième objectif est le plus difficile et le plus utile : il sera "
             "rejoué en E1, où l'assistant tend une rumeur au moins une fois.")

    d.declencheur(
        'Discussion', "Qu'est-ce qui vous ferait appeler une radio ?",
        image=IMG + 'micro-allee.jpg',
        pistes=[
            "Avez-vous déjà entendu une tribune téléphonique, ici ou ailleurs ?",
            "Qu'est-ce qui vous retiendrait d'appeler : la langue, le sujet, le direct ?",
            "Deux minutes d'antenne : par quoi commenceriez-vous ?",
            "Qu'est-ce qu'on retient d'un appel, une heure plus tard ?",
        ],
        notes="Laisser venir « je ne saurais pas quoi dire ». C'est exactement ce que "
              "la séance outille : on ne s'organise pas en direct, on s'organise "
              "avant. La dernière question annonce la règle du mot de la fin.")

    d.dialogue('Dialogue 1 de 4', "Ce que le comité demande, et pourquoi", [
        ("GRÉGOIRE", "Neuf heures cinq, la ligne est ouverte. Madame Sauvé, vous avez deux minutes.", True),
        ("RÉGINE", "Trois cent douze signatures promises sur sept cent quatre-vingt-douze, et six jours. Je ne viens demander à personne de signer.", True),
        ("RÉGINE", "Je viens demander à la Ville de reporter le registre de trente jours et de publier l'évaluation du terrain.", True),
        ("GRÉGOIRE", "Pourquoi trente jours changeraient quelque chose ?", True),
        ("RÉGINE", "Parce que la moitié des gens que je rencontre ne savent pas ce qu'est un registre. Ce n'est pas de l'opposition, c'est de l'ignorance.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire relever l'ordre : le chiffre, la demande, la raison. Et surtout "
             "la phrase « je ne viens demander à personne de signer » — Régine "
             "désamorce l'objection avant qu'on la lui pose.")

    d.dialogue('Dialogue 2 de 4', "L'éditorialiste répond, et le désaccord est net", [
        ("WILFRID", "Madame Sauvé demande trente jours et elle sait très bien que le financement du promoteur expire en mars.", True),
        ("WILFRID", "Trente jours, ici, ça veut dire non. Qu'on le dise franchement.", True),
        ("RÉGINE", "Je le dis franchement : si le projet ne survit pas à trente jours de discussion publique, c'est qu'il ne tenait pas debout.", True),
        ("WILFRID", "Ou c'est qu'un financement ne se met pas en attente parce qu'une ville a besoin de réfléchir. Ce n'est pas une manœuvre, c'est un calendrier bancaire.", True),
    ], notes="Deux personnes qui ne mentent ni l'une ni l'autre. Le faire dire au "
             "groupe : le désaccord porte sur ce qu'un délai signifie, pas sur un "
             "fait. C'est la matière de tout le défi 3.")

    d.dialogue('Dialogue 3 de 4', "Un appel qu'on n'attendait pas", [
        ("MIRELA", "Mirela Petrescu, rue des Cèdres. Je suis pour le projet, et je vais quand même signer le registre.", True),
        ("GRÉGOIRE", "Là, il faut expliquer, parce que ça a l'air contradictoire.", True),
        ("MIRELA", "Certes le logement manque, et je le vois tous les jours : trois de mes collègues ont déménagé faute de trouver ici.", True),
        ("MIRELA", "Mais je suis arrivée dans un pays où on votait sur des questions déjà réglées, et j'ai appris à me méfier de ça.", True),
    ], notes="La position annoncée en une phrase, avant toute explication : c'est le "
             "modèle de la production orale de E1. Faire remarquer le « certes… "
             "mais » — la concession vient avant l'argument, pas après.")

    d.dialogue('Dialogue 4 de 4', "Rectifier, puis demander", [
        ("WILFRID", "Madame, personne ici n'a rien réglé d'avance. Il y a eu un vote public.", True),
        ("MIRELA", "Il y a eu un vote public à vingt-deux heures cinquante devant onze personnes, monsieur. Je ne dis pas qu'il est illégal, je dis qu'il est petit.", True),
        ("GRÉGOIRE", "Qu'est-ce que vous demandez, concrètement ?", True),
        ("MIRELA", "Que l'évaluation soit publiée avant l'ouverture du registre, et que la Ville dise par écrit pourquoi le terrain de l'aréna a été écarté.", True),
        ("WILFRID", "Ça, je peux le soutenir. Publier une évaluation ne coûte rien à personne.", True),
    ], notes="Le sommet du dialogue. Mirela rectifie sans contredire — elle accepte "
             "le mot « public » et déplace la discussion sur « petit ». Puis elle "
             "termine par une demande, et son adversaire l'appuie. Faire mesurer ce "
             "que la précision a obtenu en deux phrases.")

    d.tableau('Analyse', "Trois réponses possibles quand on vous contredit",
              ['La réponse', 'Ce qu\'elle fait'],
              [["Concéder",
                "reconnaître le point exact où l'autre a raison, puis avancer"],
               ["Rectifier",
                "corriger un fait faux, calmement, en donnant la source"],
               ["Esquiver",
                "changer de sujet, ou attaquer la personne — cela s'entend toujours"]],
              cle=0,
              note="Rectifier ce qui est faux et vérifiable, concéder ce qui est juste, et ne jamais esquiver.",
              notes="Diapositive à photographier. Insister : concéder puis se taire "
                    "est une défaite ; la seconde phrase est obligatoire. Et on ne "
                    "rectifie jamais une opinion, seulement un fait vérifiable.")

    d.pratique('Pratique 1 de 2', "Que fait cette réponse ?",
               "Concéder, rectifier ou esquiver ?", [
        ("« Vous avez raison sur la rapidité du vote. Cela ne change rien au besoin de logements. »", "concéder - et la suite arrive"),
        ("« Le délai de vingt et un mois est une estimation du service, pas une règle de loi. »", "rectifier - avec la nature de la source"),
        ("« Et vous, où étiez-vous quand on a fermé l'usine ? »", "esquiver - en attaquant"),
        ("« Le terrain n'a pas été vendu : il a été cédé pour un dollar. »", "rectifier - un fait vérifiable"),
        ("« Je ne suis pas ici pour parler de ça. »", "esquiver - en ayant l'air de recadrer"),
        ("« Tout le monde sait très bien pourquoi ce terrain-là a été choisi. »", "esquiver - et insinuer"),
    ], corrige=True,
       notes="Reprend l'exercice t3repli du module. Faire nommer, pour chaque "
             "« concéder », la phrase qui devrait suivre : sans elle, la concession "
             "est une reddition.")

    d.cartes('Analyse', "La rumeur qu'on vous tend", [
        ("Ce qu'on vous dit",
         "« On dit que le promoteur serait un ami du maire. » Personne ne "
         "l'affirme : on vous la tend pour que vous la repreniez."),
        ("La mauvaise réponse",
         "« Ça, je ne peux pas le confirmer. » Elle a l'air prudente et elle "
         "ne l'est pas : elle laisse la rumeur exister, et vous en devenez la "
         "deuxième source."),
        ("La bonne réponse",
         "« Je n'en sais rien, et ce n'est pas mon argument. » Vous refusez "
         "la rumeur et vous ramenez la discussion sur votre terrain, en une "
         "phrase."),
        ("Pourquoi ça compte ici",
         "Vos meilleurs arguments sont vérifiables. Une seule rumeur reprise "
         "les rend tous suspects, et c'est ce que cherche celui qui vous la "
         "tend."),
    ], notes="Le cas particulier de la séance. Faire apprendre la bonne réponse mot "
             "pour mot : en direct, on n'invente pas. L'assistant du jeu de rôle, "
             "en E1, la tendra à chacun au moins une fois.")

    d.pratique('Pratique 2 de 2', "Concédez, puis avancez",
               "Une phrase de concession, une phrase d'argument.", [
        ("« Le comité veut simplement bloquer le projet. »", "C'est vrai que nous demandons un délai. Nous demandons aussi une évaluation, et elle ne bloque rien."),
        ("« Quarante-cinq logements abordables, c'est énorme pour la ville. »", "Certes, et je ne le conteste pas. Mais rien n'oblige la Ville à les obtenir en une soirée."),
        ("« Le vote était parfaitement légal. »", "Il l'était, oui. Il a été pris devant onze personnes, et c'est autre chose."),
        ("« Vous n'êtes pas experte en évaluation foncière. »", "Non, et c'est pour ça que je demande celle de la Ville."),
    ], corrige=True,
       notes="Deux phrases obligatoires : la concession, puis l'avancée. Faire dire "
             "les réponses debout, à voix haute, en gardant le ton bas. Celui qui "
             "monte le ton perd, à la radio comme en assemblée.")

    d.piege('Piège', "terminer sur ce qu'on dénonce",
            "terminer sur ce qu'on demande",
            "La dernière phrase est souvent la seule que l'auditoire "
            "retiendra. « C'est inacceptable » ne se répond pas et ne "
            "s'accorde pas. « Publiez l'évaluation avant mardi » se répond "
            "par oui ou par non — et un oui en ondes est un engagement "
            "public. C'est exactement ce que Mirela obtient de Wilfrid.",
            notes="Reprendre le dialogue 4 : la demande précise a obtenu en deux "
                  "phrases ce que trois semaines d'indignation n'avaient pas obtenu.")

    d.billet(
        "Écrivez votre concession et votre demande, deux phrases chacune.",
        exemples=[
            "La concession nomme le point exact : « vous avez raison sur… ».",
            "La demande s'adresse à quelqu'un qui peut agir, et porte une date.",
        ],
        notes="Devoir court, à relire à voix haute au début de D2. Ces deux phrases "
              "serviront telles quelles au jeu de rôle de E1 et à la lettre de E2.")

    return d.save(dossier)
