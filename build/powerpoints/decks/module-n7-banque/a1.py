# -*- coding: utf-8 -*-
"""A1 · La pause de dix heures
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF` et son bandeau de quatre mots.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre='La pause de dix heures',
        chapeau="Marlène paie tous les mois depuis trois ans. Sa dette n'a "
                "baissé que de quatre cents dollars. Sa collègue lui explique "
                "pourquoi en trois minutes.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : qui "
                  "a déjà payé le montant écrit en bas de son relevé sans savoir à quoi "
                  "il correspondait ? Presque tout le monde. C'est exactement le sujet "
                  "du bloc, et il ne s'agit pas de faire la morale à personne.")

    d.objectifs([
        "trouver sur un relevé le solde, le minimum et le taux ;",
        "dire ce que le paiement minimum fait, et ce qu'il ne fait pas ;",
        "comprendre qu'un taux annoncé vaut pour une année ;",
        "employer quatre mots du relevé avec leur article.",
    ], notes="Le troisième objectif est celui qui surprend le plus : beaucoup d'élèves "
             "entendent « dix-neuf et quatre-vingt-dix » comme un montant mensuel. Le "
             "poser dès la première séance.")

    d.declencheur(
        'Observation', "Quand tu reçois un papier de ta banque, qu'est-ce que tu "
                       "regardes en premier ?",
        pistes=[
            "Le montant à payer, ou le total que tu dois ?",
            "Est-ce que tu lis les petits caractères en bas ?",
            "Sais-tu quel taux ta carte applique ?",
            "Qu'est-ce que tu fais du papier après ?",
        ],
        notes="Question sans mauvaise réponse. Personne ne lit les petits caractères, "
              "et le dire ouvertement met le groupe à l'aise. Ne rien corriger ici : "
              "le dialogue le fera.")

    d.dialogue('Dialogue · 1 de 3', "Neuf mille quatre cent douze", [
        ("MARLÈNE", "Huguette, tu es bonne dans les chiffres, toi. Regarde ce papier-là deux minutes.", True),
        ("HUGUETTE", "Ton relevé de carte ? Attends que je mette mes lunettes. Ah. Neuf mille quatre cents.", True),
        ("MARLÈNE", "Neuf mille quatre cent douze. Et je paie tous les mois. Je n'ai jamais sauté un paiement en trois ans.", True),
        ("HUGUETTE", "Tu paies quoi, tous les mois ? Le montant en bas, dans la case ?", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Écrire au tableau les trois nombres du module et les y laisser toute la "
             "séance : 9 412, 470, 19,90. Ils reviennent dans les quatre blocs.")

    d.dialogue('Dialogue · 2 de 3', "Quatre cents dollars en douze paiements", [
        ("MARLÈNE", "Oui, le montant en bas. Le paiement minimum. Quatre cent soixante-dix dollars, à peu près.", True),
        ("HUGUETTE", "Regarde le solde de l'an passé, à côté. Il était de combien ?", True),
        ("MARLÈNE", "Neuf mille huit cents. Donc en un an, j'ai baissé de quatre cents dollars ?", True),
        ("HUGUETTE", "Quatre cents dollars en douze paiements. Le reste est parti en frais de crédit.", True),
    ], notes="Faire calculer au tableau : douze fois 470 font 5 640 dollars versés, et "
             "la dette a baissé de 400. La différence est le coeur du module.")

    d.dialogue('Dialogue · 3 de 3', "Par année, ma belle", [
        ("MARLÈNE", "Dix-neuf et quatre-vingt-dix, ça veut dire dix-neuf dollars par mois ?", True),
        ("HUGUETTE", "Par année, ma belle. Dix-neuf dollars et quatre-vingt-dix cents par cent dollars, par année.", True),
        ("MARLÈNE", "Tu me dis que je paie mille huit cents dollars par année juste pour avoir la dette ?", True),
        ("HUGUETTE", "À peu près, oui. Et tu as six mille deux cents dollars dans ton compte qui ne rapportent rien.", True),
    ], notes="Faire répéter la deuxième réplique par deux élèves. C'est la règle la plus "
             "importante de la séance : un taux est toujours annuel.")

    d.tableau('Analyse', "Les quatre chiffres du relevé",
              ['Sur le papier', 'Ce que ça veut dire'],
              [['le solde', "ce qui reste à devoir aujourd'hui"],
               ['le minimum', "la plus petite somme acceptée ce mois-ci"],
               ['le taux annuel', "le prix de l'argent, pour une année"],
               ["l'échéance", "la date après laquelle des frais courent"],
               ['les frais de crédit', "ce que le mois écoulé a coûté"]],
              cle=0,
              notes="Diapositive à photographier. C'est le tableau de référence du bloc "
                    "A, et il revient en B2 sur un document complet.")

    d.regle("Un taux est toujours annuel",
            "Dix-neuf et quatre-vingt-dix pour cent veut dire 19,90 $ par tranche de "
            "100 $ empruntés, par année.",
            precision="Personne ne dit le mot « annuel » : c'est la convention, et "
                      "c'est ce qui trompe le plus de monde. Sur un solde de 9 000 $, "
                      "un taux de 19,90 % coûte environ 1 800 $ par année, soit à peu "
                      "près 150 $ par mois qui ne remboursent rien du tout.",
            notes="Diapositive à photographier. Faire le calcul au tableau avec le "
                  "groupe plutôt que de l'annoncer : 9 000 fois 0,199.")

    d.vocabulaire('Vocabulaire', "Quatre mots du relevé", [
        ("un relevé de compte", "Le document que l'institution envoie chaque mois et qui montre tout ce qui est entré et sorti."),
        ("le solde", "Ce qui reste à devoir, ou ce qui reste dans le compte, à un moment donné."),
        ("le paiement minimum", "La plus petite somme qu'il faut verser dans le mois pour que le compte reste en règle."),
        ("les frais de crédit", "Ce que coûte l'argent emprunté, en plus de la somme empruntée elle-même."),
    ], notes="Faire répéter chaque mot avec son article. « Les frais de crédit » ne "
             "s'emploie qu'au pluriel : le faire remarquer, c'est une faute fréquente.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Marlène et d'Huguette.", [
        ("Marlène doit neuf mille quatre cent douze dollars sur sa carte.", "vrai"),
        ("Elle a sauté deux paiements depuis trois ans.", "faux - elle n'en a jamais sauté un seul"),
        ("En un an, son solde a baissé d'environ quatre cents dollars.", "vrai"),
        ("Le taux de dix-neuf et quatre-vingt-dix se calcule par mois.", "faux - par année"),
        ("Huguette lui conseille de vider le compte de sa fille.", "faux - elle lui conseille d'aller poser des questions"),
        ("Marlène a six mille deux cents dollars qui ne rapportent rien.", "vrai"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le deuxième "
             "compte : Marlène n'a rien fait de mal, et il faut que le groupe l'entende.")

    d.billet("Écris en deux phrases ce que le paiement minimum fait, et ce qu'il ne "
             "fait pas.",
             exemples=["Le paiement minimum garde mon compte en règle.",
                       "Il ne rembourse presque pas ma dette."],
             notes="Ramasser les billets. Ils disent en une minute qui a compris la "
                   "distinction, et c'est elle qui porte tout le bloc B.")

    return d.save(dossier)
