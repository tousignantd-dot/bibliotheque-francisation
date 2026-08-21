# -*- coding: utf-8 -*-
"""B1 · Trente secondes, six morceaux
Bloc B « Défi 1 · La boîte vocale et la note » · couleur acier · 75 min.
Source : dialogue `t1` (première partie), exercices `t1a` et `t1acc`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-travail/images/')


def build(dossier):
    d = Deck(
        code='B1', section='acier',
        titre="Trente secondes, six morceaux",
        chapeau="Un message d'accueil n'est pas une conversation : c'est un "
                "texte enregistré une fois, qui parlera à votre place cent "
                "fois. C'est pour ça qu'on l'écrit avant de l'enregistrer.",
        duree='75 minutes')

    d.titre(notes="Ouverture du défi 1. Faire écouter, si possible, le message d'accueil "
                  "d'un vrai service public au haut-parleur — celui d'une clinique, d'une "
                  "école. Demander au groupe combien de choses différentes y sont dites. "
                  "La réponse est presque toujours six.")

    d.objectifs([
        "reconnaître les six morceaux d'un message d'accueil ;",
        "les mettre dans l'ordre attendu ;",
        "dire qu'on n'est pas disponible sans dire pourquoi ;",
        "annoncer un rappel au futur simple, sans promettre une heure.",
    ])

    d.declencheur(
        'Observation', "Un voyant rouge clignote. Quatre messages vous "
                       "attendent. Qu'est-ce que les gens ont entendu avant "
                       "de parler ?",
        image=IMG + 'telephone-poste.jpg',
        pistes=[
            "Est-ce qu'un message d'accueil dit pourquoi vous n'êtes pas là ?",
            "Combien de choses peut-on demander à quelqu'un de pressé ?",
            "Que fait quelqu'un qui ne peut pas attendre votre rappel ?",
            "Que devient votre message le jour où vous partez en congé ?",
        ],
        notes="La quatrième piste est celle qui reste. Un message enregistré ne vieillit "
              "pas tout seul : il continue de promettre un rappel « dans la journée » "
              "pendant toute une semaine de vacances.")

    d.dialogue('Dialogue · 1 de 2', "Le message que Dorine a enregistré", [
        ("DORINE", "« Bonjour, vous êtes bien à la Coopérative d'aide à domicile de "
                   "Rosemont. Ici Dorine Kabeya, à l'accueil. Je ne suis pas "
                   "disponible en ce moment. Laissez-moi votre nom, votre numéro de "
                   "téléphone et la raison de votre appel : je vous rappellerai dans "
                   "la journée. Pour une urgence, faites le poste onze. Merci et "
                   "bonne journée. »", True),
        ("GHISLAIN", "C'est bon. Vous vous nommez, vous nommez la coopérative, vous "
                     "demandez les trois choses, vous dites quand vous rappelez, et "
                     "vous donnez une porte de sortie. Une seule remarque.", True),
        ("DORINE", "Laquelle ?", True),
        ("GHISLAIN", "« Dans la journée. » Si vous êtes en congé jeudi, ce n'est plus "
                     "vrai, et le message continue de le dire.", True),
    ], consigne="Écoutez d'abord, diapositive masquée. Comptez les morceaux.",
       notes="Faire compter les morceaux à l'écoute, sans le texte. Les élèves en "
             "trouvent quatre ou cinq ; le sixième — la porte de sortie — est celui "
             "qu'on n'entend pas parce qu'on ne l'attend pas.")

    d.dialogue('Dialogue · 2 de 2', "Ce qu'il faut mettre à la place", [
        ("GHISLAIN", "Mettez « dans les meilleurs délais » et changez le message "
                     "quand vous partez plus d'une journée.", True),
        ("DORINE", "Je note. Maintenant, j'ai quatre messages dans la boîte.", True),
        ("GHISLAIN", "Écoutons le premier ensemble. Vous écrivez, je me tais.", False),
    ], notes="La deuxième moitié du dialogue passe à la note d'appel : elle sera "
             "travaillée en B4. Arrêter ici et le dire au groupe, sinon les élèves "
             "cherchent la suite.")

    d.cartes("Les six morceaux", "Toujours dans cet ordre", [
        ("1 · L'établissement, puis vous",
         "Vous êtes bien à la Coopérative. Ici Dorine Kabeya, à l'accueil."),
        ("2 · L'absence, sans la raison",
         "Je ne suis pas disponible en ce moment."),
        ("3 · Les trois choses demandées",
         "Votre nom, votre numéro de téléphone et la raison de votre appel."),
        ("4 · Le rappel, au futur simple",
         "Je vous rappellerai dans les meilleurs délais."),
        ("5 · La porte de sortie",
         "Pour une urgence, faites le poste onze."),
        ("6 · La politesse",
         "Merci et bonne journée."),
    ], notes="Le cinquième morceau est celui qu'on oublie, et le seul qui rende service "
             "à quelqu'un de pressé. Le faire remarquer : sans lui, un message d'accueil "
             "est un mur poli.")

    d.regle("Trois choses, pas cinq",
            "On demande le nom, le numéro et la raison de l'appel. C'est tout "
            "ce qu'une personne pressée peut retenir.",
            precision="Si une quatrième information est vraiment nécessaire, elle se "
                      "dit en dernier et seule : « et, si vous en avez un, votre numéro "
                      "de dossier ».",
            notes="Demander au groupe ce qu'il ajouterait. Les propositions sont "
                  "raisonnables une à une, et ridicules mises bout à bout : c'est la "
                  "démonstration.")

    d.piege("Dire pourquoi on n'est pas disponible",
            "Je suis en réunion jusqu'à trois heures.",
            "Je ne suis pas disponible en ce moment.",
            "La raison ne regarde personne, et elle vieillit : le message la répétera "
            "demain encore, quand la réunion sera finie depuis longtemps.",
            notes="C'est la faute la plus fréquente et la plus facile à corriger. Faire "
                  "chercher au groupe d'autres raisons qu'on entend souvent : « je suis "
                  "en congé », « je suis au dîner », « je suis débordée ».")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Dorine a enregistré son message la veille au soir.", "vrai"),
        ("Ghislain trouve que le message est trop court.", "faux — il le trouve bon"),
        ("Il lui reproche d'avoir promis de rappeler « dans la journée ».", "vrai"),
        ("Un message d'accueil doit durer environ trois minutes.", "faux — trente secondes"),
        ("La porte de sortie est le poste onze.", "vrai"),
        ("On explique dans le message pourquoi on est absent.", "faux — jamais"),
    ], corrige=True,
       notes="Faire justifier chaque réponse par la réplique exacte. La cinquième oblige "
             "à réécouter : le numéro est dit une seule fois.")

    d.pratique('Mise en ordre', "Remettez les six morceaux dans l'ordre",
               "Numérotez de 1 à 6.", [
        ("Merci et bonne journée.", "6"),
        ("Je ne suis pas disponible en ce moment.", "2"),
        ("Pour une urgence, faites le poste onze.", "5"),
        ("Vous êtes bien à la Coopérative. Ici Dorine, à l'accueil.", "1"),
        ("Je vous rappellerai dans les meilleurs délais.", "4"),
        ("Laissez-moi votre nom, votre numéro et la raison de votre appel.", "3"),
    ], corrige=True,
       notes="Exercice à faire en équipes de deux, à l'oral, avant d'écrire. La "
             "discussion sur la place du morceau 5 est celle qui apprend le plus.")

    d.billet(
        "Écrivez les six morceaux de votre propre message d'accueil.",
        exemples=[
            "Employez le nom de votre lieu de travail, ou d'un lieu que vous connaissez.",
            "Lisez-le à voix haute et chronométrez : visez trente secondes.",
        ],
        notes="Garder ce billet : c'est le brouillon de la production orale de la séance "
              "E1. Le dire aux élèves, ils l'écrivent alors plus sérieusement.")

    return d.save(dossier)
