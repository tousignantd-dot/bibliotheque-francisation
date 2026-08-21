# -*- coding: utf-8 -*-
"""E1 · Je me lance.
Bloc E « Je me lance » · couleur teal · 60 min. Dernière séance du module.
Source : dialogue `appli`, jeu de rôle `panier`, productions orale et écrite.

Séance de production. Tout ce que le module a montré revient ici, et rien de
neuf n'y est introduit — sauf une situation, la caisse, où l'élève doit pour
la première fois faire valoir ce qu'il a lu dans la circulaire.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-panier/images/')


def build(dossier):
    d = Deck(
        code='E1', section='teal',
        titre="Je me lance",
        chapeau="Demander un produit et son prix à voix haute, puis écrire "
                "sa liste d'épicerie.",
        duree='60 minutes')

    d.titre(notes="Dernière séance. Prévoir que la moitié du temps se passe en production "
                  "réelle : jeu de rôle, enregistrement, écriture. Les diapositives ne "
                  "sont qu'un cadre.")

    d.objectifs([
        "demander un produit dans une vraie conversation ;",
        "répéter un prix pour le vérifier ;",
        "s'enregistrer et s'écouter ;",
        "écrire sa liste d'épicerie de la semaine.",
    ])

    d.declencheur(
        'Observation', "Que se passe-t-il à la caisse ?",
        image=IMG + 'caisse-epicerie.jpg',
        pistes=[
            "Qu'est-ce qu'on dit à la caisse ?",
            "Que faire si le prix n'est pas celui de la circulaire ?",
            "Est-ce qu'on a le droit de le dire ?",
            "Comment le dire poliment ?",
        ],
        notes="Beaucoup d'élèves n'oseront pas. Dire clairement que c'est normal de le "
              "signaler, et que le commis corrige sans discuter quand le spécial est "
              "encore bon.")

    d.dialogue('Dialogue', "À la caisse", [
        ("DENIS", "Bonjour. Ça fait vingt-six dollars quinze.", True),
        ("AMINATA", "Attendez. Le poulet est en spécial. J'ai la circulaire.", True),
        ("DENIS", "Montrez-moi, s'il vous plaît.", True),
        ("AMINATA", "Ici : « 2 pour 9 $ ». J'ai deux paquets.", True),
        ("DENIS", "Vous avez raison. Je corrige le prix.", True),
        ("AMINATA", "Merci. Ça fait combien maintenant ?", True),
    ], consigne="Écoutez, puis comptez ce qu'Aminata a réussi à faire.",
       notes="Trois choses en six répliques : elle arrête l'échange, elle montre sa "
             "preuve, elle redemande le nouveau total. Faire compter par le groupe.")

    d.tableau('Analyse', "Ce qui revient de tout le module",
              ['Ce qu\'on dit', 'Vu en'],
              [["« 2 pour 9 $ ». J'ai deux paquets.", "B1 — lire un prix"],
               ["Le poulet est en spécial.", "A1 — la circulaire et le mot rouge"],
               ["Ça fait combien maintenant ?", "C1 — la question courte"],
               ["Deux kilos, un litre, une douzaine", "C2 — la mesure et « de »"]],
              cle=2,
              note="Rien de neuf dans cette colonne : le module entier tient dans ces "
                   "quatre lignes.",
              notes="Diapositive à photographier. Elle sert de révision de tout le module "
                    "en une seule page.")

    d.regle("Faire valoir un spécial",
            "Montrer la circulaire vaut mieux que discuter.",
            precision="« Attendez, s'il vous plaît. Le poulet est <b>en spécial</b>. "
                      "J'ai la circulaire. » On montre la page, on montre le prix. La "
                      "date, en haut de la circulaire, dit si le spécial est encore bon.",
            notes="Insister sur « attendez, s'il vous plaît » : c'est la phrase qui donne "
                  "le temps de sortir le papier, et elle est parfaitement polie.")

    d.cartes("Trois situations pour le jeu de rôle", "Choisissez la vôtre", [
        ("Dans l'allée",
         "Vous cherchez du savon à vaisselle. Vous ne savez pas dans quelle allée il est."),
        ("Devant les fruits",
         "Deux affichettes se touchent. Vous ne savez pas laquelle va avec les oranges."),
        ("À la caisse",
         "Le prix de la caisse n'est pas celui de la circulaire. Vous avez le papier "
         "dans la main."),
    ], cols=3, notes="Ce sont les trois situations du jeu de rôle en ligne. L'élève y joue "
                     "avec l'assistant, qui parle lentement et donne une information à la "
                     "fois.")

    d.pratique('Production orale', "Demandez un produit et son prix",
               "Trois temps. Enregistrez-vous, écoutez-vous, recommencez.", [
        ("TEMPS 1", "Bonjour. Je cherche le savon à vaisselle."),
        ("TEMPS 2", "C'est dans quelle allée ? … C'est combien ?"),
        ("TEMPS 3", "Quatre dollars vingt-neuf. C'est ça ? Merci beaucoup."),
    ], cols=1,
       notes="Vingt minutes. Laisser recommencer autant de fois qu'il le faut : c'est "
             "l'écoute de soi qui fait progresser, pas la première prise.")

    d.pratique('Production écrite', "Écrivez votre liste d'épicerie",
               "De quatre à six phrases sur ce que vous achetez cette semaine.", [
        ("À écrire", "Quatre produits au moins."),
        ("À écrire", "Un format pour chacun : le kilo, le litre, le sac, la douzaine."),
        ("À écrire", "Un prix au moins, écrit avec une virgule."),
        ("À écrire", "Un produit d'entretien."),
    ], cols=1,
       notes="Vingt minutes. Rappeler d'employer « un », « une », « des » et le mot « de » "
             "après la mesure : c'est ce qui sera regardé.")

    d.billet(
        "Faites votre épicerie en français, dans votre tête, avant d'y aller.",
        exemples=[
            "Je prends un litre de lait.",
            "Je prends un kilo de riz : je n'ai pas de riz.",
            "Le savon à vaisselle, c'est dans quelle allée ?",
        ],
        notes="Dernier devoir du module. Beaucoup diront que c'est la première fois qu'ils "
              "font leur liste en français plutôt que de la traduire.")

    return d.save(dossier)
