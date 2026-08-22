# -*- coding: utf-8 -*-
"""D1 · Quatre personnes, une seule décide
Bloc D « Défi 3 » · couleur acier · 75 min. Compréhension orale à plusieurs voix.
Source : dialogue `t3`, exercices `t3vf` et `t3rapports`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D1', section='acier',
        titre="Quatre personnes, une seule décide",
        chapeau="Autour d'une table, tout le monde parle sur le même ton. "
                "Rien, dans la voix, ne dit qui a le pouvoir : c'est dans "
                "les verbes que ça se voit.",
        duree='75 minutes')

    d.titre(notes="Ouverture du bloc D et séance la plus difficile du module : quatre "
                  "locuteurs dans un même extrait. Prévenir le groupe et prévoir "
                  "trois écoutes plutôt que deux.")

    d.objectifs([
        "suivre une rencontre où quatre personnes parlent du même dossier ;",
        "entendre qui explique, qui décide et qui témoigne ;",
        "distinguer une proposition, une règle et un engagement ;",
        "employer les trois mots de la rencontre avec leur article.",
    ], notes="Le troisième objectif est celui du programme : « saisir les rapports "
             "entre les interlocutrices ou les interlocuteurs ». Il n'apparaît qu'au "
             "niveau 6 et il ne s'exerce nulle part ailleurs.")

    d.declencheur(
        'Observation', "Avez-vous déjà assisté à une réunion à votre sujet ?",
        pistes=[
            "À l'école de vos enfants, au travail, dans un bureau ?",
            "Saviez-vous qui décidait, dans la pièce ?",
            "Avez-vous parlé, ou seulement écouté ?",
        ],
        notes="Beaucoup répondront « j'ai seulement écouté ». C'est exactement ce que "
              "les deux séances du bloc D viennent changer. Le dire tout de suite.")

    d.dialogue('Dialogue · 1 de 3', "Je résume en trois phrases", [
        ("PASCAL", "Merci d'être là. On a une heure. Madame Sangaré, je résume pour tout le monde en trois phrases, puis vous corrigerez si je me trompe.", True),
        ("PASCAL", "Bintou Sangaré termine sa francisation en février. Elle vise un diplôme d'études professionnelles. Elle a un avis d'admission conditionnelle, et la condition est la réussite du test.", True),
        ("BINTOU", "C'est exact. J'ajoute une chose : le test est le vingt-huit novembre, et je suis inscrite.", True),
        ("AMÉLIE", "C'est noté. De mon côté, je veux qu'une chose soit claire dès maintenant : le centre n'accorde aucun délai après le six février.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Deux choses à faire remarquer : « j'ajoute une chose », qui est la "
             "formule d'entrée de Bintou, et « c'est noté », qui veut dire qu'une "
             "chose vient d'entrer dans un dossier.")

    d.dialogue('Dialogue · 2 de 3', "Si je peux me permettre", [
        ("MARC-OLIVIER", "Si je peux me permettre — sur le français, je n'ai aucune inquiétude. Bintou lit des textes officiels depuis septembre et elle les lit mieux que la moitié du groupe.", True),
        ("AMÉLIE", "Ce n'est pas rien non plus. Nos consignes de laboratoire sont écrites comme cet avis-là.", True),
        ("BINTOU", "Est-ce que je peux poser une question ?", True),
        ("BINTOU", "Si je réussis le test le vingt-huit et que la preuve arrive en janvier, est-ce que ça suffit ?", True),
    ], notes="Trois formules de prise de parole en quatre répliques. Les faire "
             "relever par le groupe : « si je peux me permettre », « est-ce que je "
             "peux poser une question ? », et l'hypothèse en « si » qui suit.")

    d.dialogue('Dialogue · 3 de 3', "Pour ma part, je préférerais après", [
        ("AMÉLIE", "J'aimerais que madame Sangaré vienne visiter le laboratoire avant de décider. Beaucoup de gens s'inscrivent sans avoir vu la place où ils passeront neuf mois.", True),
        ("BINTOU", "Pour ma part, je préférerais y aller après le test. Si j'y vais avant, je vais penser à ça pendant l'épreuve.", True),
        ("AMÉLIE", "C'est raisonnable. Le trois décembre, alors.", True),
        ("MARC-OLIVIER", "Une dernière chose, et j'y tiens : que quelqu'un lui envoie le compte rendu de cette rencontre par écrit. On a dit quatre dates en une heure.", True),
    ], notes="Le moment le plus important du module : Bintou refuse sans refuser. "
             "Elle ne dit pas non, elle déplace la date et elle dit pourquoi. "
             "Personne ne perd la face. C'est le sujet de D2.")

    d.tableau('Analyse', "Qui peut quoi, autour de la table",
              ['La personne', 'Ce qu\'elle peut'],
              [["Le conseiller", "explique, calcule, propose — il n'admet personne"],
               ["La responsable", "tient le calendrier et décide de ce que le centre accepte"],
               ["L'enseignant", "dit où en est l'élève : son avis pèse, il ne tranche pas"],
               ["L'élève", "apporte ses documents, pose ses conditions, s'engage sur des dates"]],
              cle=0,
              note="Confondre une proposition et une règle, c'est repartir en croyant qu'une chose est réglée alors qu'elle a seulement été souhaitée.",
              notes="Diapositive à photographier. Faire retrouver dans le dialogue une "
                    "phrase de chacun des quatre. C'est le meilleur exercice "
                    "d'écoute du module.")

    d.regle("Écoutez le verbe, pas le ton",
            "« Je propose » n'engage rien ; « j'exige » engage l'établissement ; « c'est noté » veut dire qu'une chose vient d'entrer au dossier.",
            precision="Tout le monde parle poliment et sur le même ton. Ce sont les "
                      "verbes qui portent le pouvoir : je vous explique, je vous "
                      "propose, j'aimerais que, je veux que, aucun délai n'est "
                      "accordé, c'est noté.",
            notes="Diapositive à photographier. Faire classer six phrases entendues "
                  "en trois colonnes : propose, décide, témoigne.")

    d.vocabulaire('Vocabulaire', "Les trois mots de la rencontre", [
        ("une rencontre de suivi", "Un rendez-vous où plusieurs personnes font le point sur le dossier d'un seul élève."),
        ("un plan de formation", "L'ordre écrit des cours à suivre, avec le temps prévu et les dates à respecter."),
        ("un compte rendu", "Le texte court qui rapporte ce qui a été dit et décidé pendant une rencontre."),
    ], notes="Insister sur le compte rendu : le demander n'est ni impoli ni méfiant. "
             "C'est ce qui distingue une conversation d'un engagement.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la rencontre du 14 novembre.", [
        ("Pascal commence en résumant le dossier en trois phrases.", "vrai"),
        ("Amélie annonce qu'aucun délai n'est accordé après le 6 février.", "vrai"),
        ("Selon Marc-Olivier, c'est la langue qui arrête Bintou.", "faux - c'est le vocabulaire administratif"),
        ("Bintou accepte de visiter le laboratoire avant l'épreuve.", "faux - elle préfère y aller après"),
        ("C'est Marc-Olivier qui demande un compte rendu écrit.", "vrai"),
        ("La rencontre se termine sans qu'aucune date soit fixée.", "faux - quatre dates en une heure"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "est celui qui compte : Bintou n'a pas refusé, elle a déplacé.")

    d.billet(
        "Qui, dans cette rencontre, peut vraiment changer quelque chose ?",
        exemples=[
            "Nomme une personne et écris la phrase qui te l'a fait comprendre.",
        ],
        notes="Quatre minutes. Ramasser : les réponses montrent qui, dans le groupe, "
              "entend encore l'autorité dans le ton plutôt que dans les verbes.")

    return d.save(dossier)
