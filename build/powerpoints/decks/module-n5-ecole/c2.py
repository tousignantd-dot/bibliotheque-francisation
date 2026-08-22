# -*- coding: utf-8 -*-
"""C2 · Lire l'avis jusqu'au bout
Bloc C « Défi 2 · Lire l'avis du centre » · couleur ambre · 75 min.
Compréhension écrite. Source du module : exercice `t2avis`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre="Lire l'avis jusqu'au bout",
        chapeau="L'avis reçu par Amelia, en entier : quatre paragraphes, un "
                "numéro de dossier, trois dates et une signature à donner. "
                "C'est l'intention de compréhension écrite du programme — "
                "lire un avis ou un document scolaire officiel — et elle se "
                "travaille sur un texte, pas sur un résumé.",
        duree='75 minutes')

    d.titre(notes="Séance de lecture. Prévoir de projeter l'avis long et de le laisser "
                  "affiché : le groupe doit pouvoir y revenir en répondant. Distribuer "
                  "aussi la fiche élève, qui le porte en entier.")

    d.objectifs([
        "lire un avis officiel de quatre paragraphes sans en sauter un ;",
        "y trouver l'échéance, la période et la date de retour ;",
        "comprendre la conséquence annoncée en cas de retard ;",
        "repérer ce que le paragraphe conditionnel demande.",
    ], notes="Le premier objectif est le plus difficile. Un avis se lit en diagonale par "
             "réflexe, et c'est précisément ce réflexe qui fait manquer le quatrième "
             "paragraphe.")

    d.cartes("L'avis, paragraphe par paragraphe", "Centre des Trois-Ponts · dossier 2026-0418", [
        ("Objet",
         "Confirmation d'une absence prévue. À l'attention de madame Amelia "
         "Dumitrescu, groupe 4, francisation, cours LAN-4059-8."),
        ("1 · Ce qui est confirmé",
         "Nous accusons réception de votre demande d'absence. Votre absence "
         "est autorisée du 9 mars au 27 mars inclusivement. Votre place dans "
         "le groupe 4 vous est conservée pendant cette période."),
        ("2 · Ce que vous devez faire",
         "Le formulaire d'absence prolongée, signé, doit nous parvenir d'ici "
         "le 6 mars. Passé cette date, la demande n'est plus recevable et "
         "l'absence sera inscrite comme non motivée."),
        ("3 · Votre retour",
         "Le retour en classe est prévu le lundi 30 mars, au local 214. Un "
         "rattrapage vous sera offert les mardis et jeudis midis, au local "
         "118, sur inscription au secrétariat."),
        ("4 · Si la situation change",
         "En cas de prolongation, veuillez communiquer avec le secrétariat "
         "avant le 27 mars. Toute pièce justificative peut être remise à "
         "votre retour. Veuillez signer cet avis et le rapporter au "
         "secrétariat."),
    ], cols=1,
       notes="Lire les cinq blocs à voix haute, une fois, sans commentaire. Puis "
             "demander au groupe de dire, sans relire, ce qu'il faut faire et pour "
             "quand. Presque personne ne retient les deux à la fois : c'est ce qui "
             "justifie la prise de notes de C4.")

    d.pratique('Compréhension écrite', "Vrai ou faux ?",
               "Répondez d'après l'avis, en montrant le paragraphe.", [
        ("L'absence est autorisée du 9 au 27 mars inclusivement.", "vrai — paragraphe 1"),
        ("Le formulaire signé doit arriver au plus tard le 6 mars.", "vrai — paragraphe 2"),
        ("Sa place dans le groupe 4 n'est pas conservée.", "faux — paragraphe 1"),
        ("Une demande arrivée le 9 mars serait encore recevable.",
         "faux — paragraphe 2"),
        ("Le retour en classe est prévu au local 214.", "vrai — paragraphe 3"),
        ("Le rattrapage se donne trois soirs par semaine.",
         "faux — deux midis, paragraphe 3"),
        ("En cas de prolongation, il faut appeler avant le 27 mars.",
         "vrai — paragraphe 4"),
        ("La pièce justificative doit être remise avant le départ.",
         "faux — au retour, paragraphe 4"),
    ], corrige=True,
       notes="Exiger le numéro de paragraphe à chaque réponse. C'est ce qui transforme "
             "l'exercice de compréhension en méthode de lecture : on ne répond pas de "
             "mémoire, on retourne au texte.")

    d.tableau('Les trois dates', "Laquelle oblige ?",
              ['La date', 'Son rôle'],
              [["Le 6 mars", "L'échéance — remettre le formulaire signé"],
               ["Du 9 au 27 mars", "La période autorisée — elle informe"],
               ["Le 30 mars", "Le retour en classe — un rappel"],
               ["Avant le 27 mars", "La limite si la situation change"]],
              cle=1,
              notes="Faire compléter la colonne de droite. La quatrième ligne est celle "
                    "que le groupe oublie : il y a en réalité deux dates qui obligent, "
                    "et la seconde n'oblige que si le cas se présente.")

    d.regle("Deux locaux, deux choses",
            "Le retour se fait au local 214. Le rattrapage se donne au local 118.",
            precision="Recopier un numéro approximativement vaut moins que rien : "
                      "il vous enverra à la mauvaise porte avec l'air d'être sûr.",
            notes="Diapositive à photographier. Elle a l'air anecdotique et elle ne "
                  "l'est pas : les numéros sont ce que les élèves recopient le plus "
                  "mal, parce qu'ils les lisent sans les dire.")

    d.piege("Sauter le paragraphe qui commence par « en cas de »",
            "Ça ne me concerne pas, ma situation ne changera pas.",
            "Je le lis quand même : c'est le seul qui prévoit l'imprévu.",
            "Une situation change toujours un peu. Ce paragraphe dit quoi faire, et "
            "surtout avant quand — et cette limite-là arrive souvent plus tôt que la "
            "fin de la période.",
            notes="Faire calculer au groupe combien de jours séparent le 27 mars du "
                  "retour du 30. Trois jours seulement : appeler « avant le 27 » veut "
                  "dire décider pendant qu'on est encore à l'étranger.")

    d.pratique('Repérage', "Trouvez la phrase exacte",
               "Sans reformuler : donnez les mots de l'avis.", [
        ("Quelle phrase dit que la place est gardée ?",
         "Votre place dans le groupe 4 vous est conservée pendant cette période."),
        ("Quelle phrase dit ce qui arrive après le 6 mars ?",
         "Passé cette date, la demande n'est plus recevable."),
        ("Quelle phrase dit où a lieu le rattrapage ?",
         "Un rattrapage vous sera offert... au local 118."),
        ("Quelle phrase dit quoi faire de l'avis lui-même ?",
         "Veuillez signer cet avis et le rapporter au secrétariat."),
    ], corrige=True,
       notes="Cet exercice-là est le plus formateur de la séance : citer plutôt que "
             "reformuler oblige à retourner au texte, ligne par ligne. Le faire deux "
             "par deux, à voix basse.")

    d.billet(
        "Écrivez les deux dates de l'avis qui obligent Amelia à faire quelque chose.",
        exemples=[
            "Pour chacune, dites ce qu'elle doit faire.",
            "Attention : il y en a deux, pas une.",
        ],
        notes="Ramasser les billets. Ceux qui n'en trouvent qu'une ont sauté le "
              "quatrième paragraphe, exactement comme le piège l'annonçait.")

    return d.save(dossier)
