# -*- coding: utf-8 -*-
"""D1 · Le message de Fatou.
Bloc D « Défi 3 · Donner des nouvelles » · couleur acier · 60 min.
Source : dialogue `t3`, exercice `t3vf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre='Le message de Fatou',
        chapeau="Fatou, la sœur de Mariama, laisse un message vocal depuis la "
                "Guinée. Le bébé est né. Recevoir une nouvelle, c'est déjà une "
                "compétence : comprendre, et savoir qu'il faut répondre.",
        duree='60 minutes')

    d.titre(notes="Ouverture du bloc D. Annoncer le plan : aujourd'hui on reçoit des "
                  "nouvelles, à la séance suivante on en donne par écrit.")

    d.objectifs([
        "comprendre un message vocal personnel du début à la fin ;",
        "repérer l'information essentielle : qui, quoi, quand ;",
        "reconnaître les formules qui annoncent une nouvelle importante ;",
        "savoir ce qu'on répond, et à quelle vitesse.",
    ])

    d.declencheur(
        'Mise en situation', "Comment annoncez-vous une grande nouvelle à quelqu'un de loin ?",
        pistes=[
            "Par message écrit, par message vocal, par appel ? Pourquoi ?",
            "Qui prévenez-vous en premier ?",
            "Combien de temps attendez-vous avant d'annoncer ?",
            "Est-ce que ça se fait de la même façon dans votre pays et ici ?",
        ],
        notes="Cinq minutes. Fatou a choisi le message vocal en disant « je ne voulais pas "
              "te l'écrire » : le groupe reconnaîtra ce réflexe. C'est une bonne entrée en "
              "matière interculturelle.")

    d.dialogue('Message vocal · 1 de 2', 'Une grande nouvelle', [
        ("FATOU", "Mariama, c'est ta sœur. J'ai une grande nouvelle et je ne voulais pas te l'écrire.", True),
        ("FATOU", "Le bébé est arrivé mardi matin. Une petite fille. Trois kilos deux.", True),
        ("FATOU", "Tout s'est bien passé. J'étais fatiguée, mais je vais bien, et elle mange déjà comme quatre.", False),
    ], consigne="Écoutez le message en entier, diapo masquée, avant de lire.",
       notes="Faire écouter deux fois. À la deuxième écoute, demander de noter trois "
             "informations. Comparer ensuite en groupe.")

    d.dialogue('Message vocal · 2 de 2', 'Le nom, et la demande', [
        ("FATOU", "Maman est restée avec nous toute la semaine. Elle dit qu'elle te ressemble quand tu étais bébé.", False),
        ("FATOU", "On a choisi son nom hier soir : Aminata, comme grand-mère.", True),
        ("FATOU", "Envoie-moi des photos de la neige. Je veux les lui montrer quand elle sera grande.", True),
        ("FATOU", "Écris-moi vite. Tu me manques.", False),
    ], notes="« Écris-moi vite » est une demande explicite : c'est ce qui déclenche la "
             "production écrite de D2. Le souligner.")

    d.cartes("Ce qu'un message de nouvelles contient", "Quatre choses, presque toujours", [
        ("Qui parle",
         "« C'est ta sœur. » On se nomme, même à quelqu'un qui nous connaît : le message "
         "vocal ne montre pas toujours le nom."),
        ("La nouvelle, tout de suite",
         "« Le bébé est arrivé mardi matin. » On ne fait pas attendre. La nouvelle vient "
         "dans les deux premières phrases."),
        ("Les détails qui rassurent",
         "« Tout s'est bien passé. » Après une naissance, une opération, un déménagement, "
         "c'est ce que la personne au loin veut entendre en premier."),
        ("Une demande",
         "« Envoie-moi des photos. » · « Écris-moi vite. » Un message de nouvelles finit "
         "presque toujours par une demande de réponse."),
    ], notes="Faire retrouver les quatre parties dans le message. C'est le plan que les "
             "élèves suivront s'ils enregistrent eux-mêmes un message.")

    d.tableau('Analyse', "Les mots des évènements de la vie",
              ['Le mot', 'Ce que ça désigne'],
              [["une naissance", "l'arrivée d'un bébé"],
               ["un mariage", "l'union de deux personnes"],
               ["un déménagement", "le changement de logement"],
               ["un décès", "la mort de quelqu'un"],
               ["des nouvelles", "ce qu'on raconte de sa vie"]],
              cle=4,
              notes="« Des nouvelles » est toujours au pluriel dans ce sens. Le signaler : "
                    "« une nouvelle » désigne une seule information.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le message.", [
        ("Elle a préféré annoncer la nouvelle par écrit.", "faux — elle ne voulait pas l'écrire"),
        ("Le bébé est né un mardi matin.", "vrai"),
        ("C'est un garçon.", "faux — une petite fille"),
        ("Leur mère est restée avec eux toute la semaine.", "vrai"),
        ("Le nom du bébé n'est pas encore choisi.", "faux — Aminata, choisi hier soir"),
        ("Elle dit à Mariama de ne pas se presser pour répondre.", "faux — « écris-moi vite »"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la phrase exacte du message. Réécouter "
             "au besoin.")

    d.regle("Ce qu'il faut retenir",
            "Une nouvelle personnelle appelle une réponse, et vite.",
            precision="Ne pas répondre à l'annonce d'une naissance, d'un mariage ou d'un "
                      "décès se remarque, ici comme ailleurs. Trois lignes suffisent — "
                      "c'est justement l'objet de la séance suivante.",
            notes="Diapo à photographier. Elle fait le pont vers D2.")

    d.billet(
        "Notez la dernière grande nouvelle que vous avez reçue de votre pays.",
        exemples=[
            "Qui vous l'a annoncée ? Comment ? Avez-vous répondu ?",
            "Trois phrases suffisent. Vous n'aurez pas à la lire à voix haute.",
        ],
        notes="Sujet possiblement sensible. Préciser que le billet est lu par vous seul et "
              "que personne n'aura à le partager.")

    return d.save(dossier)
