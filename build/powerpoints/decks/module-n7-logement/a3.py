# -*- coding: utf-8 -*-
"""A3 · Le nom caché sous le verbe
Bloc A « Je découvre » · couleur ambre · formation des mots · 75 min.
Source : exercice `prMots` et sa mini-leçon ; le savoir « formation des mots »
du niveau 7.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Le nom caché sous le verbe",
        chapeau="« La modification des conditions du bail. » Les documents "
                "parlent en noms là où la vie parle en verbes. Refaire le "
                "chemin en sens inverse, c'est comprendre du premier coup.",
        duree='75 minutes')

    d.titre(notes="Séance de formation des mots. Commencer par relire à voix haute une "
                  "phrase de l'avis de A1, puis demander au groupe de la redire « comme "
                  "on parle ». L'écart entre les deux versions est toute la séance.")

    d.objectifs([
        "retrouver le verbe caché sous un nom de document ;",
        "fabriquer un nom en -tion et un nom en -ment à partir d'un verbe ;",
        "connaître le genre d'un nom d'après son suffixe ;",
        "comprendre ce que le préfixe contre- ajoute à un mot.",
    ], notes="Le troisième objectif règle un problème d'article que le groupe traîne "
             "depuis le niveau 5 : tous les -tion sont féminins, tous les -ment sont "
             "masculins, sans exception à retenir.")

    d.declencheur(
        'Observation', "Dis autrement : « la modification des conditions du bail »",
        pistes=[
            "Quel est le verbe caché dans « modification » ?",
            "Qui fait l'action, dans la phrase de l'avis ? Est-ce dit ?",
            "Pourquoi un document écrirait-il ça plutôt que « je change le bail » ?",
            "Est-ce plus poli, plus court, ou plus impersonnel ?",
        ],
        notes="La bonne réponse est « plus impersonnel » : le nom permet de parler de "
              "l'action sans nommer celui qui la fait. Le dire une fois, clairement.")

    d.tableau('Analyse', "Du verbe au nom, trois familles",
              ['Le verbe', 'Le nom'],
              [["modifier · fixer · inspecter", "la modification · la fixation · l'inspection"],
               ["négocier · reconduire", "la négociation · la reconduction"],
               ["financer · engager", "le financement · l'engagement"],
               ["rembourser · renouveler", "le remboursement · le renouvellement"],
               ["hausser · promettre · vendre", "une hausse · une promesse · une vente"]],
              cle=0,
              notes="Diapositive à photographier. Les trois premières rangées donnent "
                    "des féminins, les deux suivantes des masculins, la dernière des "
                    "noms courts sans suffixe. Le faire remarquer en montrant l'article.")

    d.regle("Deux suffixes, deux genres, aucune exception",
            "Les noms en -tion sont féminins, les noms en -ment sont masculins.",
            precision="C'est l'une des rares règles du français qui ne se paie pas "
                      "d'exceptions. Retenir le suffixe évite d'apprendre le genre mot "
                      "par mot : la modification, la fixation, l'inspection, la "
                      "négociation d'un côté ; le financement, l'engagement, le "
                      "remboursement, le renouvellement de l'autre.",
            notes="Diapositive à photographier. Attention à ne pas confondre avec les "
                  "adverbes en -ment (rapidement, seulement), qui viennent d'adjectifs "
                  "et ne sont pas des noms.")

    d.pratique('Écriture', "Complétez avec le nom de la même famille",
               "Un seul mot par trou. Attention à l'article.", [
        ("Le propriétaire veut modifier une condition : il envoie un avis de ___ .", "modification"),
        ("Le Tribunal peut fixer le loyer : on parle de ___ du loyer.", "la fixation"),
        ("Un professionnel inspecte la maison : c'est l'___ préachat.", "inspection"),
        ("La caisse accepte de financer l'achat : la condition de ___ est remplie.", "financement"),
        ("On rembourse le prêt chaque mois : le ___ s'étale sur vingt-cinq ans.", "remboursement"),
        ("Elle promet d'acheter à ce prix-là : elle dépose une ___ d'achat.", "promesse"),
    ], corrige=True,
       notes="Six des huit items de l'exercice prMots. Faire dire l'article à voix "
             "haute avec chaque réponse : c'est là que se joue l'apprentissage.")

    d.cartes('Analyse', "Le préfixe contre-, et ce qu'il ne dit pas", [
        ("de proposition à contre-proposition", "Une offre qui répond à une autre offre. Ce n'est pas une offre « contre vous » : c'est une offre en retour."),
        ("de partie à contrepartie", "Ce qu'on donne en échange de ce qu'on obtient. Le mot est le cœur de la négociation du bloc B."),
        ("Ce que le préfixe veut dire", "Contre- dit « qui répond à », « qui vient en retour ». Il n'y a aucune hostilité dans le mot, et c'est important de le savoir avant de l'employer."),
        ("Deux orthographes à retenir", "Contre-proposition prend un trait d'union ; contrepartie n'en prend pas. Rien ne le fait deviner : ces deux-là s'apprennent tels quels."),
    ], notes="Le dernier point agace toujours quelqu'un. Le reconnaître : c'est une "
             "irrégularité de l'usage, pas une logique à comprendre.")

    d.billet(
        "Écris une phrase avec un nom en -tion, puis la même avec le verbe.",
        exemples=[
            "« La modification du bail m'inquiète. »",
            "« Ça m'inquiète qu'il veuille modifier le bail. »",
        ],
        notes="Deux minutes. Faire lire trois billets à voix haute et demander au "
              "groupe laquelle des deux versions il emploierait dans une conversation.")

    return d.save(dossier)
