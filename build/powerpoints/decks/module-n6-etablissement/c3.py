# -*- coding: utf-8 -*-
"""C3 · Quand personne n'est nommé
Bloc C « Défi 2 » · couleur ambre · 75 min. Grammaire de la phrase.
Source : exercices `t2passif` et `t2futur`, et leurs deux mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Quand personne n'est nommé",
        chapeau="« Les documents se déposent au secrétariat. » Les documents "
                "ne se déposent pas tout seuls. Deux tournures suffisent à "
                "cacher qui doit bouger — et c'est presque toujours vous.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, mais la grammaire y sert directement : "
                  "chaque phrase du tableau vient d'un document réel que les élèves "
                  "recevront. Le dire d'entrée de jeu.")

    d.objectifs([
        "comprendre un verbe pronominal à sens passif et nommer qui agit ;",
        "former « se » plus un verbe au présent, accordé avec la chose ;",
        "reconnaître un futur simple qui donne un ordre ;",
        "traduire ce futur à l'impératif pour en saisir l'obligation.",
    ], notes="Les deux points forment un couple : ils sont les deux façons dont "
             "l'administration évite de dire « faites ceci ».")

    d.declencheur(
        'Observation', "« Les documents se déposent au secrétariat. » Qui les dépose ?",
        pistes=[
            "Le secrétariat ? Les documents eux-mêmes ?",
            "Comment auriez-vous écrit cette phrase, vous ?",
            "Pourquoi croyez-vous qu'on écrit comme ça ?",
        ],
        notes="Laisser le groupe hésiter. La réponse « le secrétariat » est très "
              "fréquente et elle explique bien des enveloppes jamais apportées.")

    d.tableau('Analyse', "Le verbe qui ne nomme personne",
              ['Ce qui est écrit', 'Ce que ça veut dire'],
              [["Les demandes se déposent", "vous devez les apporter là, en personne"],
               ["Le formulaire se remplit en ligne", "vous le remplissez vous-même"],
               ["Ce papier s'obtient au comptoir", "allez le demander, il n'arrivera pas seul"],
               ["Les résultats s'envoient", "là, c'est le centre qui agit : vous attendez"],
               ["Les places se prennent vite", "personne n'agit, sauf les autres candidats"]],
              cle=0,
              note="Une seule question, chaque fois : par qui ? Neuf fois sur dix, par vous.",
              notes="Diapositive à photographier. Faire poser la question à voix "
                    "haute après chaque ligne : « par qui ? » Le réflexe s'installe "
                    "en cinq minutes et il reste.")

    d.regle("Se plus le verbe au présent, accordé avec la chose",
            "La demande se dépose ; les demandes se déposent. Devant une voyelle, « se » devient « s' ».",
            precision="Le verbe ne s'accorde pas avec vous, mais avec ce qui subit "
                      "l'action : « les places se prennent vite », même si c'est vous "
                      "qui les prenez. Et « ce papier s'obtient », jamais « se "
                      "obtient ».",
            notes="Diapositive à photographier. L'apostrophe est la faute la plus "
                  "fréquente à l'écrit ; l'accord est la plus fréquente à l'oral.")

    d.piege('Grammaire',
            "elle se lave, donc ce papier se demande veut dire la même chose",
            "c'est le sens du verbe qui tranche, jamais la forme",
            "« Elle se lave » : le « se » veut bien dire elle-même. « Ce "
            "papier se demande au comptoir » : personne ne se demande "
            "lui-même. La forme est identique, le sens ne l'est pas — et "
            "seule la question « par qui ? » les distingue.",
            notes="Donner quatre phrases à trier oralement. Deux minutes. Ne pas "
                  "entrer dans la terminologie : le tri suffit.")

    d.pratique('Pratique', "Récrivez le verbe à la forme des documents",
               "Employez « se » plus le verbe au présent.", [
        ("Les demandes ... au secrétariat. (déposer)", "se déposent"),
        ("Le formulaire ... en ligne, en douze minutes. (remplir)", "se remplit"),
        ("Ce papier ... au comptoir, jamais par courriel. (obtenir)", "s'obtient"),
        ("Les résultats ... par la poste. (envoyer)", "s'envoient"),
        ("Le test ... deux fois par année. (donner)", "se donne"),
        ("Les places du groupe de mars ... vite. (prendre)", "se prennent"),
    ], corrige=True, cols=2,
       notes="Faire dire à voix haute, avant d'écrire, qui agit dans chaque phrase. "
             "Le quatrième et le sixième sont les deux seuls où ce n'est pas l'élève.")

    d.tableau('Analyse', "Le futur qui donne un ordre",
              ['L\'ordre ordinaire', 'La version officielle'],
              [["Présentez-vous au local 118.", "Vous vous présenterez au local 118."],
               ["Fournissez la preuve.", "La candidate fournira la preuve."],
               ["Déposez vos documents.", "Vous déposerez vos documents au pavillon B."],
               ["Signez le formulaire.", "Vous signerez le formulaire au bas de la page."],
               ["Soyez à jeun.", "Le patient sera à jeun le matin de l'examen."]],
              cle=1,
              note="Ni « peut-être », ni « probablement » : ce futur-là n'annonce rien, il oblige.",
              notes="Diapositive à photographier. Faire lire les deux colonnes en "
                    "alternance. Le groupe entend le changement de distance avant de "
                    "comprendre la règle.")

    d.pratique('Pratique', "Récrivez la consigne au futur",
               "Écrivez seulement le verbe, à la forme des documents officiels.", [
        ("Présentez-vous au local 118. Vous ... au local 118 à 8 h.", "vous présenterez"),
        ("Fournissez la preuve. La candidate ... la preuve avant le 6 février.", "fournira"),
        ("Déposez vos documents. Vous ... vos documents au pavillon B.", "déposerez"),
        ("Apportez une pièce d'identité. Vous ... une pièce d'identité avec photo.", "apporterez"),
        ("Signez le formulaire. Vous ... le formulaire au bas de la page.", "signerez"),
        ("Soyez à jeun. Le patient ... à jeun le matin de l'examen.", "sera"),
    ], corrige=True, cols=2,
       notes="Le dernier item est irrégulier : le signaler avant, pas après. "
             "Rappeler que l'élève n'a pas à écrire ainsi : il doit seulement "
             "comprendre qu'on lui donne un ordre.")

    d.billet(
        "Récris deux phrases officielles en phrases ordinaires.",
        exemples=[
            "Choisis-en une avec « se », une avec un futur.",
            "Commence par « Ça veut dire : … ».",
        ],
        notes="Cinq minutes. C'est la vérification la plus honnête du cours : un "
              "élève qui traduit une phrase officielle en phrase ordinaire l'a "
              "comprise, même s'il ne sait pas la nommer.")

    return d.save(dossier)
