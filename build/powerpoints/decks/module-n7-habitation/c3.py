# -*- coding: utf-8 -*-
"""C3 · Ce que dit la ville, ce que dit le bail
Bloc C « Défi 2 · Redire ce qui a été dit » · couleur ambre · compréhension
écrite · 75 min.
Source : exercice de type `texte` `t2regl` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Ce que dit la ville, ce que dit le bail",
        chapeau="Deux textes, deux autorités, et presque tout le monde les "
                "confond. La ville donne une amende ; le bail règle ce qui se "
                "passe entre vous, le voisin et la propriétaire.",
        duree='75 minutes')

    d.titre(notes="Séance de compréhension écrite. Les faits énoncés ici ont été "
                  "vérifiés le 23 août 2026 auprès du Tribunal administratif du "
                  "logement, du Code civil du Québec et du règlement sur le bruit de "
                  "la Ville de Québec. Ils ne s'inventent pas.")

    d.objectifs([
        "distinguer ce qui relève de la ville et ce qui relève du bail ;",
        "trouver dans un règlement l'heure et la définition qui servent ;",
        "distinguer le locateur du locataire ;",
        "dire pourquoi la propriétaire est concernée par un bruit qu'elle ne fait pas.",
    ], notes="Le quatrième objectif est le pivot du module : il explique pourquoi la "
             "lettre du bloc D s'adresse à la propriétaire.")

    d.declencheur(
        'Observation', "À qui te plaindrais-tu d'abord : à la ville ou au propriétaire ?",
        pistes=[
            "Qu'est-ce que la ville peut faire, à ton avis ?",
            "Et le propriétaire ?",
            "Lequel des deux peut faire déplacer un appareil ?",
            "Lequel des deux peut donner une amende ?",
        ],
        notes="Le groupe se partage toujours en deux, et les deux camps ont "
              "partiellement raison. Ne pas trancher : le tableau suivant le fait.")

    d.tableau('Analyse', "Deux voies, jamais dans la même lettre",
              ['La ville', 'Le bail'],
              [["Une amende de 2 000 $ à 10 000 $", "Une diminution de loyer"],
               ["Un bruit excessif ou insolite", "Un trouble à la jouissance paisible"],
               ["La plainte se porte au 311", "La demande se porte au Tribunal"],
               ["Le jour, le soir, la nuit", "La durée du bail"],
               ["Personne ne vous rembourse", "Des dommages-intérêts sont possibles"]],
              cle=1,
              notes="Diapositive à photographier. Les deux voies peuvent servir le même "
                    "mois — mais jamais dans la même lettre, et pas auprès des mêmes "
                    "personnes.")

    d.regle("Les trois périodes du règlement",
            "Le jour de 7 h à 19 h, le soir de 19 h à 23 h, la nuit de 23 h à 7 h.",
            precision="C'est la vraie utilité du règlement de la ville : il fournit un "
                      "vocabulaire précis que personne ne peut discuter. Écrire « à "
                      "5 h 45, c'est-à-dire pendant la période de nuit au sens du "
                      "règlement » vaut mieux que « très tôt le matin ». Un bruit "
                      "excessif ou insolite qui trouble la paix constitue une nuisance.",
            notes="Diapositive à photographier. Faire écrire les trois périodes au "
                  "tableau et les y laisser : elles servent dans la lettre du bloc D.")

    d.regle("Locateur et locataire",
            "Le locateur loue son logement à quelqu'un ; le locataire l'habite.",
            precision="Les deux mots se ressemblent et disent le contraire, et les "
                      "documents officiels n'emploient que le premier. Le moyen de ne "
                      "plus se tromper : locateur, comme donateur — celui qui donne à "
                      "louer.",
            notes="Diapositive à photographier. C'est la confusion la plus fréquente du "
                  "domaine du logement, et elle rend un texte officiel incompréhensible "
                  "dès la première ligne.")

    d.tableau('Analyse', "Quatre obligations, et à qui elles s'appliquent",
              ['Qui', "Ce qu'il doit"],
              [["Le locateur", "procurer la jouissance paisible pendant tout le bail"],
               ["Le locateur", "répondre du trouble si le tiers est son locataire"],
               ["Le locataire", "ne pas troubler la jouissance normale des autres"],
               ["Le locataire troublé", "aviser d'abord, demander ensuite"]],
              note="Si le voisin bruyant habitait la maison d'à côté, la propriétaire "
                   "n'y pourrait rien. C'est parce qu'il habite son immeuble qu'elle "
                   "est dans le dossier.",
              cle=0,
              notes="Diapositive à photographier. La deuxième rangée est celle qui "
                    "surprend, et c'est celle qui justifie la mise en demeure du bloc D.")

    d.piege('Méthode',
            "Appeler la ville en premier",
            "Parler au voisin en premier",
            "Un constat de la ville arrive après le fait, il ne fait rien déplacer, et "
            "il transforme le voisin en adversaire pour des années. Il se garde pour "
            "quand le reste a échoué. La première démarche reste celle du bloc B : "
            "monter, frapper, et dire bonjour.",
            notes="Faire relever la contradiction apparente : on vient d'apprendre le "
                  "règlement, et on dit de ne pas s'en servir. Le règlement donne des "
                  "mots, pas une solution.")

    d.pratique('Compréhension', "Trouvez dans les textes",
               "Répondez d'après le règlement et la fiche de renseignements.", [
        ("À quelle heure commence la nuit, selon le règlement ?", "à 23 h, et elle finit à 7 h"),
        ("Qui peut être tenu responsable du bruit d'un appareil ?", "celui qui l'émet, celui qui le possède, celui qui le tolère"),
        ("Combien coûte une première infraction ?", "de 2 000 $ à 10 000 $"),
        ("À quoi la propriétaire s'est-elle engagée en signant le bail ?", "à procurer la jouissance paisible du logement"),
        ("Dans quel cas répond-elle du bruit d'un autre ?", "quand ce tiers est aussi son locataire"),
        ("Que peut demander la locataire si rien n'est fait après l'avis ?", "une diminution de loyer ou des dommages-intérêts"),
    ], corrige=True,
       notes="Faire retrouver chaque réponse dans le texte, à voix haute, avant de "
             "montrer la correction. C'est un exercice de repérage, pas de mémoire.")

    d.billet(
        "À qui écrirais-tu, et pourquoi à cette personne-là ?",
        exemples=[
            "Une phrase suffit.",
            "Pense à ce que chacune peut faire, et à ce qu'elle ne peut pas.",
        ],
        notes="Deux minutes. Les réponses annoncent le bloc D, où l'on écrit deux "
              "lettres à deux personnes différentes.")

    return d.save(dossier)
