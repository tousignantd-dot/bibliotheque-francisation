# -*- coding: utf-8 -*-
"""A2 · Des lettres qui ne se disent pas comme on croit
Bloc A « Je découvre » · couleur indigo · graphie-phonie · 75 min.
Source : exercice `prGraphie` et sa mini-leçon du même nom — les trois cas
que le programme du niveau 6 nomme : ch qui dit k, x qui dit s, sh et sch qui
disent ch.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Des lettres qui ne se disent pas comme on croit",
        chapeau="Trois cas seulement, mais fréquents : chorale, dix, "
                "shampoing. On les entend tous les jours et on ne les "
                "retrouve pas au dictionnaire.",
        duree='75 minutes')

    d.titre(notes="Séance de graphie-phonie. Commencer par écrire trois mots au "
                  "tableau — chorale, soixante, schéma — et demander au groupe de les "
                  "lire à voix haute. Ne rien corriger tout de suite : on y revient à "
                  "la fin de la séance.")

    d.objectifs([
        "entendre le son k dans chorale, technique, écho, psychologie ;",
        "entendre le son s dans dix, six, soixante, Bruxelles ;",
        "entendre le son ch dans short, schéma, shampoing ;",
        "retrouver un mot au dictionnaire quand la lettre entendue trompe.",
    ], notes="Le quatrième objectif est le vrai enjeu. Un mot entendu qu'on ne "
             "retrouve pas est un mot perdu ; la règle sert à le retrouver.")

    d.declencheur(
        'Observation', "Quel mot as-tu déjà cherché sans le trouver ?",
        pistes=[
            "Tu l'as entendu à la radio, dans un cours, chez le médecin ?",
            "Comment l'avais-tu écrit ?",
            "Est-ce qu'il commençait par un son k, un son s ou un son ch ?",
            "Qu'est-ce que tu as fini par faire ?",
        ],
        notes="Tout le monde a cette expérience. Elle rend la règle utile avant "
              "qu'elle soit énoncée.")

    d.tableau('Cas 1', "Les lettres ch qui se disent comme un k",
              ['On écrit', 'On entend'],
              [["une chorale", "co-rale — mot venu du grec"],
               ["la technique", "tec-nique — jamais te-chnique"],
               ["un écho", "é-co"],
               ["la psychologie", "psi-co-lo-gie"],
               ["une chronique", "cro-nique"]],
              cle=0,
              note="Chercher, chaque, chose, chignon gardent le son normal.",
              notes="Diapositive à photographier. Faire remarquer que ces mots ont "
                    "souvent un y ou un ph à côté : c'est le repère du mot savant.")

    d.tableau('Cas 2', "La lettre x qui se dit comme un s",
              ['On écrit', 'On entend'],
              [["dix", "dis, tout seul"],
               ["dix dollars", "di dollars — devant une consonne"],
               ["dix ans", "diz ans — devant une voyelle"],
               ["six", "sis, tout seul"],
               ["soixante", "soi-sante, jamais soi-ksante"],
               ["Bruxelles", "Bru-selles"]],
              cle=0,
              notes="Les trois formes de dix surprennent toujours. Insister : "
                    "personne ne reprendra un élève qui dit diz jours ; ce qui compte, "
                    "c'est de reconnaître les trois à l'écoute.")

    d.tableau('Cas 3', "Les lettres sh et sch qui se disent comme un ch",
              ['On écrit', 'On entend'],
              [["un short", "chort"],
               ["du shampoing", "cham-poin"],
               ["un schéma", "ché-ma"],
               ["un shérif", "ché-rif"]],
              cle=0,
              note="Des mots empruntés, souvent courts, devenus courants ici.",
              notes="Ce sont les mots qu'on prononce le plus souvent à l'anglaise sans "
                    "s'en rendre compte. Les faire répéter lentement, à la française.")

    d.regle("Chercher avec la lettre écrite, pas avec la lettre entendue",
            "Un mot entendu qui reste introuvable cache souvent un ch, un x ou un sh.",
            precision="Tu entends « co-rale » et tu cherches corale : rien. Essaie ch "
                      "à la place du k, et x à la place du s. Le mot apparaît presque "
                      "toujours du premier coup.",
            notes="Diapositive à photographier. C'est la règle la plus utile de la "
                  "séance : elle sert bien au-delà du module.")

    d.pratique('Écoute', "Quel son entends-tu ?",
               "Écoutez chaque mot, puis dites : comme k, comme s, ou comme ch.", [
        ("une chorale", "comme k"),
        ("la technique", "comme k"),
        ("un écho", "comme k"),
        ("dix", "comme s"),
        ("soixante", "comme s"),
        ("Bruxelles", "comme s"),
        ("un short", "comme ch"),
        ("un schéma", "comme ch"),
    ], corrige=True, cols=2,
       notes="Faire écouter deux fois avant de répondre. C'est l'oreille qu'on "
             "entraîne, pas la mémoire. Les élèves ouvriront ensuite le même exercice "
             "dans le module, avec les enregistrements.")

    d.piege('Prononciation', "Technique dit avec le son de chat",
            "Technique dit tec-nique",
            "Ces mots savants ne sont pas nombreux : ils s'apprennent un par un. "
            "Mais dits avec le son de chat, ils ne se comprennent pas du tout — "
            "ce qui est plus gênant qu'un accent.",
            notes="Dédramatiser : personne ne devine ces mots. Ils se retiennent par "
                  "l'usage, et la liste est courte.")

    d.billet(
        "Écris un mot du jour et note comment il se prononce.",
        exemples=[
            "Par exemple : chorale — co-rale.",
            "Choisis celui qui t'a le plus surpris.",
        ],
        notes="Deux minutes. Relire les billets avant A3 : ils disent quel cas reste "
              "à retravailler.")

    return d.save(dossier)
