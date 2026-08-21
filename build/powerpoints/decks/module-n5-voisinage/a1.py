# -*- coding: utf-8 -*-
"""A1 · « Trois ans dans le même escalier »
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `pr1`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-voisinage/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="« Trois ans dans le même escalier »",
        chapeau="Marisol Vergara habite au deuxième du 7412, rue De "
                "Normanville, depuis trois ans. Elle monte cet escalier tous "
                "les jours et elle ne connaît personne. Un jeudi, son voisin "
                "du rez-de-chaussée lui parle enfin d'autre chose que de la "
                "météo.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : combien "
                  "de personnes habitent votre immeuble, et combien en connaissez-vous par "
                  "leur nom ? Laisser le silence s'installer : la réponse est presque "
                  "toujours embarrassante, et c'est exactement le point de départ du "
                  "module. Ne juger personne — dans un immeuble de six logements, ne "
                  "connaître personne est la norme, pas une faute.")

    d.objectifs([
        "nommer les lieux d'un immeuble et d'une ruelle montréalaise ;",
        "comprendre une conversation d'escalier entre deux voisins ;",
        "reconnaître ce qui se demande à un voisin et ce qui ne se demande pas ;",
        "comprendre pourquoi une invitation demande une réponse claire.",
    ], notes="Le troisième objectif est le plus culturel des quatre et il fera parler : "
             "ce qui est une marque d'intérêt dans un pays est une intrusion dans un "
             "autre. Prévoir dix minutes de discussion, elles serviront en A4.")

    d.declencheur(
        'Observation', "Un escalier que vous montez tous les jours. Qui "
                       "habite en haut ? Qui habite en bas ?",
        image=IMG + 'escalier-exterieur.jpg',
        pistes=[
            "Combien de personnes habitent votre immeuble ?",
            "Combien en connaissez-vous par leur nom ?",
            "À qui diriez-vous bonjour dans l'escalier ?",
            "Qui arroserait vos plantes si vous partiez deux semaines ?",
        ],
        notes="Les quatre pistes annoncent tout le module : le voisinage au bloc A, "
              "l'invitation au bloc B, le message qu'on laisse au bloc C, le service "
              "qu'on demande au bloc E. La dernière fait comprendre l'enjeu : on ne "
              "confie pas ses clés à quelqu'un dont on ignore le nom.")

    d.dialogue('Dialogue · 1 de 3', "Deux voisins qui se croisent", [
        ("RÉJEAN", "Madame Vergara ! Vous arrivez du travail ?", True),
        ("MARISOL", "Bonjour monsieur Deslauriers. Oui, je finis à trois "
                    "heures maintenant.", True),
        ("RÉJEAN", "Ah bon ? Vous avez changé d'horaire ?", True),
        ("MARISOL", "Depuis le mois de mars. Je commence à six heures, mais "
                    "mes après-midi sont à moi.", True),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="Faire remarquer deux choses : ils s'appellent par leur nom de famille, et "
             "ils se vouvoient. Demander au groupe si c'est froid. La réponse — non, "
             "c'est la norme entre voisins — surprend, et elle prépare la séance A4.")

    d.dialogue('Dialogue · 2 de 3', "La ruelle, et douze ans de tomates", [
        ("MARISOL", "Elle est belle, votre ruelle. Chez nous, au Chili, on "
                    "appelait ça un passage.", True),
        ("RÉJEAN", "Ici on dit une ruelle verte. C'est l'arrondissement qui a "
                   "fait ça avec nous, il y a douze ans.", True),
        ("MARISOL", "Douze ans ! Vous étiez déjà là ?", True),
        ("RÉJEAN", "J'habite au rez-de-chaussée depuis trente ans, madame. "
                   "J'ai vu passer tout le monde.", True),
    ], notes="Le mot « ruelle verte » est neuf pour la moitié du groupe. Expliquer en une "
             "phrase : une ruelle aménagée avec l'arrondissement par les gens qui "
             "habitent autour. Demander qui en a une derrière chez lui.")

    d.dialogue('Dialogue · 3 de 3', "Un « peut-être » ne se met pas sur une liste", [
        ("RÉJEAN", "On organise une fête dans la ruelle, au mois de juin. "
                   "Toutes les portes sont invitées.", True),
        ("MARISOL", "Il faut que j'y pense. Je vous réponds cette semaine ?", True),
        ("RÉJEAN", "Prenez votre temps. Mais répondez-moi, hein. Un "
                   "« peut-être », ça ne se met pas sur une liste.", False),
    ], notes="La dernière réplique est la phrase à retenir de la séance, et c'est tout le "
             "défi 1. Beaucoup d'élèves viennent de cultures où un refus direct est "
             "impoli et où « peut-être » veut dire non. Le dire explicitement, sans "
             "jugement : ici, « peut-être » veut dire « peut-être », et on vous attendra.")

    d.regle("Répondre est déjà une forme de politesse",
            "Entre voisins, un oui ou un non clair rend plus service qu'un "
            "« peut-être » qui ne devient jamais rien.",
            precision="Celui qui organise doit compter les chaises, les tables et "
                      "les plats. Un « on verra » l'oblige à revenir vous chercher, "
                      "et souvent il n'ose pas.",
            notes="Diapositive à photographier. Elle reviendra en B2, quand on "
                  "travaillera les trois réponses possibles à une invitation.")

    d.cartes("Quatre lieux", "Le vocabulaire de l'immeuble", [
        ("La ruelle",
         "Le passage derrière les immeubles. Verte quand elle est aménagée."),
        ("Le hangar",
         "La construction de bois au fond de la cour. Aucune auto dedans."),
        ("Le balcon d'en arrière",
         "Celui qui donne sur la ruelle, pas sur la rue."),
        ("La corvée",
         "Un travail que plusieurs personnes font ensemble, la même journée."),
    ], notes="Ces quatre mots ne s'apprennent pas dans un livre : ils s'entendent dans la "
             "cour. Faire répéter avec l'article. Demander l'équivalent dans les langues "
             "du groupe : la ruelle n'existe pas partout.")

    d.tableau('Deux façons de vivre', "Avant, et après la conversation",
              ['Avant le jeudi', 'Après le jeudi'],
              [["Je dis bonjour dans l'escalier", "Je connais le nom de mon voisin"],
               ["J'ignore qui habite en haut", "Je sais qui travaille de nuit"],
               ["La ruelle est un passage", "La ruelle est un lieu commun"],
               ["Personne ne m'invite nulle part", "Je suis invitée le 7 juin"],
               ["Je n'ai rien à répondre", "Je dois donner une réponse claire"]],
              cle=1,
              notes="Faire compléter la colonne de droite par le groupe avant de "
                    "l'afficher. C'est une conversation de trois minutes qui change tout, "
                    "et le module montre que ces trois minutes s'apprennent.")

    d.piege("Croire qu'il faut bien parler pour parler à un voisin",
            "Je vais attendre de mieux parler français.",
            "Je dis bonjour, et je pose une question sur l'immeuble.",
            "Une conversation de voisinage tient en trois phrases, et elle porte sur "
            "des choses qu'on partage : la ruelle, le bac brun, les travaux dans la "
            "rue. Personne n'attend un discours.",
            notes="Ce piège est réel et il coûte des années aux élèves. Faire trouver au "
                  "groupe la phrase la plus courte qui ouvre une conversation. « Il y a "
                  "longtemps que vous habitez ici ? » suffit.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Marisol habite l'immeuble depuis trois ans.", "vrai"),
        ("Réjean habite au troisième étage.", "faux — au rez-de-chaussée, depuis trente ans"),
        ("La ruelle verte a été aménagée avec l'arrondissement.", "vrai"),
        ("Réjean connaît très bien madame Faye.", "faux — elle travaille de nuit, il la voit peu"),
        ("La fête aura lieu au mois de juin.", "vrai"),
        ("Réjean se contente d'un « peut-être ».", "faux — il demande une réponse claire"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. La dernière prépare "
             "toute la séance B2.")

    d.billet(
        "Écrivez le nom d'une personne de votre immeuble, et une chose que vous savez d'elle.",
        exemples=[
            "Si vous ne connaissez aucun nom, écrivez la question que vous poseriez demain.",
            "Ajoutez où vous la croisez : l'escalier, l'entrée, la ruelle, la buanderie.",
        ],
        notes="Ramasser les billets. Ceux qui n'ont aucun nom à écrire sont exactement le "
              "public du module : leur question servira d'exemple en A4.")

    return d.save(dossier)
