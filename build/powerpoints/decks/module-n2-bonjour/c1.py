# -*- coding: utf-8 -*-
"""C1 · Pouvez-vous m'aider ?
Bloc C « Défi 2 · Merci et bonne fête » · couleur acier · 75 min.
Source : dialogue `t2`, exercice `t2aide`, mini-leçon `t2aide`.

La séance qui répond à l'intention de compréhension orale du programme :
« comprendre une demande d'aide ». Elle se travaille dans les deux sens —
comprendre celle qu'on nous fait, et savoir faire la sienne — parce qu'un
élève de niveau 2 en a besoin tous les jours.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n2-bonjour/images/')


def build(dossier):
    d = Deck(
        code='C1', section='acier',
        titre="Pouvez-vous m'aider ?",
        chapeau="Trois morceaux, toujours dans le même ordre : j'appelle, "
                "je demande, je dis quoi.",
        duree='75 minutes')

    d.titre(notes="Séance la plus utile du module hors de la classe. Faire jouer beaucoup, "
                  "expliquer peu. Chaque élève doit dire la phrase au moins dix fois.")

    d.objectifs([
        "comprendre une personne qui demande de l'aide ;",
        "demander de l'aide avec « pouvez-vous » ;",
        "dire son besoin avec « j'ai besoin de » ;",
        "accepter, et répondre à un merci.",
    ])

    d.declencheur(
        'Observation', "De quoi cette personne a-t-elle besoin ?",
        image=IMG + 'porte-tenue.jpg',
        pistes=[
            "Que porte cette personne ?",
            "Que fait l'autre main sur la porte ?",
            "Qu'est-ce qu'on dit dans ce cas ?",
            "Vous est-il déjà arrivé de ne pas savoir quoi dire ?",
        ],
        notes="La dernière question ramène presque toujours une histoire vraie. La "
              "laisser se raconter : c'est la meilleure entrée en matière possible.")

    d.dialogue('Dialogue · 1 de 2', "Mes sacs sont lourds", [
        ("GILBERTE", "Nadia ! Excuse-moi… Peux-tu m'aider ?", True),
        ("NADIA", "Oui, madame Roy. Qu'est-ce qu'il y a ?", True),
        ("GILBERTE", "Mes sacs sont lourds. J'ai besoin d'aide.", True),
        ("NADIA", "Je prends un sac. Pouvez-vous tenir la porte ?", True),
    ], consigne="Écoutez deux fois avant de lire.",
       notes="Faire entendre les deux formes dans le même échange : madame Roy tutoie "
             "(« peux-tu »), Nadia vouvoie (« pouvez-vous »). C'est le rappel de B1.")

    d.dialogue('Dialogue · 2 de 2', "Ce n'est rien", [
        ("GILBERTE", "Oui, bien sûr. Merci beaucoup.", True),
        ("NADIA", "L'ascenseur est là. Deuxième étage ?", True),
        ("GILBERTE", "Oui, deuxième. Tu es gentille.", True),
        ("NADIA", "Ce n'est rien, madame Roy.", True),
    ], notes="« Ce n'est rien » est la réponse à retenir. La faire répéter en chœur trois "
             "fois : elle sert dans toutes les situations du reste du module.")

    d.tableau('Analyse', "Une demande en trois morceaux",
              ['Le morceau', 'Ce qu\'on dit'],
              [["j'appelle", "Excusez-moi…"],
               ["je demande", "Pouvez-vous… ?"],
               ["je dis quoi", "…m'aider · …tenir la porte · …répéter"],
               ["on répond", "Oui, bien sûr."]],
              cle=2,
              note="Toujours dans cet ordre. Ça marche dans l'immeuble, au magasin, au "
                   "centre.",
              notes="Diapositive à photographier. Faire construire trois demandes "
                    "complètes au tableau, en pigeant une ligne à la fois.")

    d.vocabulaire('Vocabulaire', "Demander et répondre", [
        ("de l'aide", "Ce qu'on donne à une personne qui n'y arrive pas seule."),
        ("une porte", "Ce qu'on ouvre pour entrer dans un immeuble."),
        ("lourd", "Difficile à porter."),
        ("gentil", "Qui aide et qui fait plaisir aux autres."),
    ], notes="Diapositive à photographier. « Gentil » revient dans le dialogue et dans la "
             "carte de vœux de C2 : le placer maintenant.")

    d.regle("« m' » se met avant le verbe",
            "Pouvez-vous <b>m'</b>aider ? — jamais « aider moi ».",
            precision="Le petit mot qui dit « à moi » se colle devant le verbe : "
                      "pouvez-vous <b>m'</b>aider, pouvez-vous <b>me</b> répondre, "
                      "pouvez-vous <b>m'</b>ouvrir. Devant une voyelle, « me » devient "
                      "« m' ».",
            notes="Diapositive à photographier. C'est la faute la plus fréquente à ce "
                  "niveau, et elle vient de l'ordre des mots de plusieurs langues du "
                  "groupe.")

    d.pratique('Compréhension', "Que dites-vous ?",
               "Écrivez la phrase qui convient.", [
        ("Vos sacs sont lourds, vous parlez à une voisine.", "Pouvez-vous m'aider ?"),
        ("La même chose, à un ami.", "Peux-tu m'aider ?"),
        ("Vous avez les mains pleines devant la porte.", "Pouvez-vous tenir la porte ?"),
        ("Vous n'avez pas compris.", "Pouvez-vous répéter ?"),
        ("On vous dit merci.", "Ce n'est rien."),
    ], corrige=True, cols=1,
       notes="Faire dire chaque phrase à voix haute avant de l'écrire. La quatrième est "
             "celle qu'ils utiliseront le plus souvent.")

    d.piege('Le piège', "Hé ! Aidez-moi !", "Excusez-moi, pouvez-vous m'aider ?",
            "Sans « excusez-moi », la demande arrive trop vite et surprend. Le mot ne "
            "veut pas dire « pardon, j'ai fait une faute » : il veut dire « je vous "
            "parle ». Il ouvre la porte, et il coûte une seconde.",
            notes="Faire jouer les deux versions et demander au groupe laquelle il "
                  "préfère recevoir. La réponse est immédiate.")

    d.pratique('Pratique · à deux', "Les mains pleines",
               "Deux par deux, avec de vrais sacs si possible.", [
        ("Étape 1", "L'un a les mains pleines et demande de l'aide."),
        ("Étape 2", "L'autre accepte : « oui, bien sûr »."),
        ("Étape 3", "Le premier remercie ; l'autre répond « ce n'est rien »."),
        ("Étape 4", "Changez de rôle et changez de demande."),
    ], cols=1,
       notes="Vingt minutes. Apporter deux sacs de tissu et quelques livres : la situation "
             "physique change complètement la qualité de la production.")

    d.billet(
        "Écrivez trois demandes que vous pourriez faire cette semaine.",
        exemples=[
            "Excusez-moi, pouvez-vous m'aider ?",
            "Pouvez-vous répéter, s'il vous plaît ?",
            "Pouvez-vous parler plus lentement ?",
        ],
        notes="Devoir court. Les deux dernières valent pour tous les cours, pas seulement "
              "pour celui-ci : le dire.")

    return d.save(dossier)
