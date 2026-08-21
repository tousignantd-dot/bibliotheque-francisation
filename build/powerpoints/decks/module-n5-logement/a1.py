# -*- coding: utf-8 -*-
"""A1 · L'avis dans la boîte aux lettres.
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercices `pr1` et `prAvis`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n5-logement/images/')


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="L'avis dans la boîte aux lettres",
        chapeau="Un papier arrive du propriétaire : le loyer monte et le "
                "stationnement disparaît. Beaucoup de locataires paient une "
                "hausse qu'ils avaient le droit de refuser.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Demander d'abord qui, dans le groupe, loue "
                  "son logement, et qui a déjà reçu un papier du propriétaire sans le "
                  "comprendre. Les réponses ouvrent la séance et disent le niveau réel de "
                  "connaissance des droits.")

    d.objectifs([
        "reconnaître un avis de modification du bail ;",
        "savoir qu'on a un mois pour y répondre ;",
        "comprendre que ne rien répondre, c'est accepter ;",
        "nommer les quatre papiers d'un locataire.",
    ])

    d.declencheur(
        'Observation', "Vous trouvez ce papier dans votre boîte aux lettres. "
                       "Que faites-vous ?",
        image=IMG + 'boite-aux-lettres.jpg',
        pistes=[
            "Vous le lisez tout de suite ?",
            "Vous le mettez sur la table de cuisine ?",
            "Est-ce que vous devez répondre ?",
            "Avez-vous le droit de dire non ?",
        ],
        notes="La réponse la plus fréquente est « je le mets sur la table ». C'est "
              "exactement ce qu'il ne faut pas faire, et c'est le point de départ du "
              "module. Ne pas corriger tout de suite : laisser le dialogue le faire.")

    d.dialogue('Dialogue · 1 de 3', "Un papier qu'on ne comprend pas", [
        ("NADÈGE", "Bonjour. J'ai reçu un papier de mon propriétaire et je ne suis "
                   "pas certaine de le comprendre.", True),
        ("SAMUEL", "Assoyez-vous. Vous permettez que je le regarde ? … D'accord. "
                   "C'est un avis de modification du bail.", True),
        ("NADÈGE", "Modification, ça veut dire qu'il me met dehors ?", True),
        ("SAMUEL", "Non, pas du tout. Il vous annonce ce qu'il veut changer pour "
                   "l'année prochaine. Ici, il demande soixante-quinze dollars de "
                   "plus par mois.", False),
    ], consigne="Écoutez d'abord, diapositive masquée.",
       notes="La peur de Nadège — « il me met dehors » — est la peur réelle de beaucoup "
             "d'élèves. La nommer ouvertement, puis la démonter avec la suite.")

    d.dialogue('Dialogue · 2 de 3', "Deux changements, pas un", [
        ("NADÈGE", "Et là, en bas ? Il y a une ligne sur le stationnement.", True),
        ("SAMUEL", "Il veut aussi vous enlever la case de stationnement. Ça, c'est "
                   "un deuxième changement, et il doit l'écrire séparément.", True),
        ("NADÈGE", "Est-ce que je suis obligée de dire oui ?", True),
        ("SAMUEL", "Vous avez un mois pour répondre. Vous pouvez accepter, ou "
                   "refuser par écrit. Si vous refusez, c'est lui qui doit "
                   "s'adresser au Tribunal administratif du logement.", True),
    ], notes="Deux informations capitales ici : chaque modification se compte à part, et "
             "le refus se fait par écrit. Les écrire au tableau au fur et à mesure.")

    d.dialogue('Dialogue · 3 de 3', "Le silence vaut un oui", [
        ("NADÈGE", "Un mois. Et si je ne réponds rien du tout ?", True),
        ("SAMUEL", "Si vous ne répondez pas, la loi considère que vous avez "
                   "accepté. C'est pour ça qu'il ne faut jamais laisser cet avis "
                   "sur la table de cuisine.", True),
        ("NADÈGE", "De toute façon, ma fille dort dans le salon. Je pense que je "
                   "vais chercher un quatre et demie.", True),
        ("SAMUEL", "Alors commençons par là. Regardez les annonces, notez tout ce "
                   "qu'on vous dit au téléphone, et rappelez-moi avant de signer "
                   "quoi que ce soit.", True),
    ], notes="La dernière réplique annonce le plan du module : les annonces, l'appel et "
             "les notes, puis le bail. Le dire au groupe.")

    d.regle("Le silence vaut acceptation",
            "Ne pas répondre à un avis de modification, c'est l'accepter.",
            precision="C'est la règle qui surprend le plus et qui coûte le plus cher. "
                      "Le délai d'un mois commence le jour où vous recevez l'avis. Il ne "
                      "recommence pas si vous étiez en voyage, à l'hôpital ou à "
                      "l'extérieur du pays.",
            notes="Diapositive à photographier. Si les élèves ne retiennent qu'une chose "
                  "du module, c'est celle-là.")

    d.cartes("Les quatre papiers d'un locataire", "À ne pas confondre", [
        ("Le bail",
         "Le contrat de départ. Un formulaire officiel, le même pour tout le Québec."),
        ("L'avis de modification",
         "Ce que le propriétaire veut changer l'année prochaine : le loyer, un service."),
        ("La réponse du locataire",
         "Votre lettre. Un mois pour l'écrire, et elle décide de tout."),
        ("L'annexe",
         "Les règlements de l'immeuble, agrafés au bail — et qui font partie du bail."),
    ], notes="Faire nommer, pour chacun, qui l'écrit : le propriétaire pour deux, le "
             "locataire pour un, et les deux ensemble pour le bail.")

    d.tableau('Vos trois réponses possibles', "Refuser n'oblige pas à déménager",
              ['Votre décision', 'Ce que vous faites'],
              [["Accepter", "vous écrivez oui — ou vous ne faites rien"],
               ["Refuser et rester", "vous écrivez non, et vous restez chez vous"],
               ["Quitter", "vous avisez que vous partirez à la fin du bail"]],
              cle=0,
              note="Après un refus, c'est le propriétaire qui doit s'adresser au Tribunal.",
              notes="La deuxième ligne est celle qu'on ignore le plus. Insister : refuser "
                    "une hausse n'est pas un conflit, c'est une étape prévue par la loi.")

    d.piege("Croire qu'un papier officiel ne se discute pas",
            "C'est écrit, donc je dois payer.",
            "J'ai un mois pour répondre, et j'ai le droit de refuser.",
            "Un avis de modification est une proposition, pas une décision. Des milliers "
            "de locataires refusent une hausse chaque printemps, et le Tribunal fixe "
            "souvent un loyer plus bas que celui qui était demandé.",
            notes="Beaucoup d'élèves nouvellement arrivés n'osent pas répondre à un "
                  "propriétaire. Nommer cette gêne et dire qu'elle coûte de l'argent.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après le dialogue.", [
        ("Le propriétaire de Nadège veut la mettre dehors.", "faux — il propose un changement"),
        ("L'avis annonce une hausse de soixante-quinze dollars par mois.", "vrai"),
        ("Il veut aussi retirer la case de stationnement.", "vrai — un deuxième changement"),
        ("Nadège a une semaine pour répondre.", "faux — un mois"),
        ("Si elle ne répond rien, la loi considère qu'elle a accepté.", "vrai"),
        ("C'est le locataire qui doit s'adresser au Tribunal en cas de refus.",
         "faux — c'est le propriétaire"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte du dialogue.")

    d.billet(
        "Cherchez dans vos papiers : avez-vous une copie de votre bail ?",
        exemples=[
            "Si oui, apportez-la la semaine prochaine (cachez votre nom si vous préférez).",
            "Si non, notez qu'un propriétaire doit vous en remettre une copie.",
        ],
        notes="Devoir concret. Il prépare le défi 3 et donne des documents réels à lire en "
              "classe. Prévoir que plusieurs élèves n'auront pas leur copie : c'est en soi "
              "une information à traiter.")

    return d.save(dossier)
