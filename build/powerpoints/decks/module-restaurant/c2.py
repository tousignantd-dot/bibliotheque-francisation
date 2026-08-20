# -*- coding: utf-8 -*-
"""C2 · Demander et signaler.
Bloc C · couleur ambre (écriture) · 75 min.
Source : mini-leçon `t2demander`, exercice `t2demander`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='ambre',
        titre='Demander et signaler',
        chapeau="Deux formules suffisent : une pour les petites choses, une "
                "pour ce qui demande du travail. Et un mot pour attirer "
                "l'attention.",
        duree='75 minutes')

    d.titre(notes="Séance de production orale déguisée en grammaire. Prévoir beaucoup de "
                  "temps de pratique à deux.")

    d.objectifs([
        "employer « est-ce que je pourrais avoir » pour une petite chose ;",
        "employer « est-ce que ce serait possible de » pour une correction ;",
        "attirer l'attention avec « excusez-moi » ;",
        "distinguer ce qui se signale de ce qui ne se signale pas.",
    ])

    d.tableau('Analyse', "Deux formules, deux usages",
              ['Pour', 'La formule'],
              [["Du sel, de l'eau, un couvert", "Est-ce que je pourrais avoir… ?"],
               ["Réchauffer, refaire, changer", "Est-ce que ce serait possible de… ?"],
               ["Attirer l'attention", "Excusez-moi, quand vous aurez un moment."]],
              cle=1,
              note="La deuxième est plus douce parce qu'elle fait bouger la cuisine.",
              notes="Diapo centrale. Faire recopier. Deux formules couvrent tout un repas.")

    d.regle("Pour attirer l'attention",
            "Un mot, un regard, une main légèrement levée.",
            precision="« Excusez-moi » suffit. On ne claque pas des doigts, on ne dit pas "
                      "« eh ! », on n'appelle pas à voix haute d'un bout à l'autre de la "
                      "salle. Si le serveur est occupé, « quand vous aurez un moment » dit "
                      "que ce n'est pas urgent — et il revient dès qu'il peut.",
            notes="Diapo à photographier. Les gestes varient beaucoup d'un pays à l'autre : "
                  "en parler ouvertement évite des malaises.")

    d.cartes("Ce qui se signale", "Quatre cas, tous ordinaires", [
        ("Un plat froid",
         "Il se réchauffe en deux minutes. C'est le cas le plus fréquent et le plus simple."),
        ("Une erreur de commande",
         "Une sauce non demandée, un plat qui n'est pas le vôtre. On le dit — la cuisine "
         "note l'erreur."),
        ("Un verre ou un couvert sale",
         "Question d'hygiène. On le dit sans hésiter, et on ne s'excuse pas de le dire."),
        ("Une attente anormale",
         "Quarante minutes sans plat, ce n'est pas normal. « Excusez-moi, nous avons "
         "commandé il y a quarante minutes » suffit — c'est un fait, pas un reproche."),
    ], notes="Faire remarquer la formulation de la quatrième carte : on donne un fait et une "
             "durée, sans accusation. C'est ce qui fait avancer les choses.")

    d.regle("Ce qui ne se signale pas",
            "Ce qui relève du goût personnel, ou du prix.",
            precision="« Je n'aime pas le goût » n'est pas un problème de service : le plat "
                      "est bien fait, il ne vous plaît pas. Et le prix ne se discute pas "
                      "avec le serveur, qui ne le fixe pas. La règle simple : si le "
                      "restaurant peut y faire quelque chose, on le dit.",
            notes="Cette limite est aussi importante que la permission. Elle évite des "
                  "situations désagréables pour tout le monde.")

    d.piege("S'excuser longuement",
            "Je suis vraiment désolé de vous déranger, je sais que vous êtes très occupé, mais…",
            "Excusez-moi, est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?",
            "Une demande ordinaire n'a pas besoin d'être justifiée. Trois mots et la "
            "demande : c'est plus rapide pour vous et pour le serveur, et cela met tout le "
            "monde à l'aise.",
            notes="Beaucoup d'élèves surcompensent par crainte de mal faire. Le dire "
                  "explicitement soulage.")

    d.pratique('Pratique · 1 de 2', "Quelle formule ?",
               "Écrivez la demande.", [
        ("Vous voulez du sel.", "Est-ce que je pourrais avoir un peu de sel, s'il vous plaît ?"),
        ("Votre plat est froid.", "Est-ce que ce serait possible de le réchauffer ?"),
        ("Vous voulez de l'eau.", "Pourriez-vous nous apporter de l'eau, s'il vous plaît ?"),
        ("Il manque une fourchette.", "Excusez-moi, il manque un couvert."),
        ("Vous voulez l'addition.", "Pourriez-vous m'apporter l'addition ?"),
    ], corrige=True, cols=1,
       notes="Plusieurs formulations sont bonnes. Vérifier que la forme est adoucie et que "
             "« s'il vous plaît » y est.")

    d.pratique('Pratique · 2 de 2', "Est-ce qu'on le dit ?",
               "Dans un restaurant d'ici, signale-t-on cela ?", [
        ("Mon plat est froid.", "oui"),
        ("J'avais demandé sans sauce et il y en a.", "oui"),
        ("Je n'aime pas le goût.", "non — c'est un goût personnel"),
        ("Mon verre est sale.", "oui"),
        ("Le restaurant est bruyant.", "non — le restaurant n'y peut rien"),
        ("Ma commande n'est pas arrivée après quarante minutes.", "oui"),
    ], corrige=True,
       notes="Faire appliquer la règle : le restaurant peut-il y faire quelque chose ?")

    d.cartes("Jouer la scène", "Trois situations à deux", [
        ("Le plat froid",
         "L'un joue le client, l'autre le serveur. Le serveur s'excuse et propose de le "
         "réchauffer."),
        ("La sauce non demandée",
         "Le client signale sans exiger. Le serveur propose de refaire le plat ; le client "
         "peut refuser."),
        ("L'attente",
         "Le client donne un fait et une durée. Le serveur va vérifier en cuisine."),
    ], notes="Vingt minutes de pratique à deux. C'est la partie la plus utile de la séance "
             "— faire tourner les rôles.")

    d.billet(
        "Écrivez un court échange : vous signalez quelque chose, le serveur répond.",
        exemples=[
            "Quatre répliques : vous, lui, vous, lui.",
            "Employez « excusez-moi » et une des deux formules.",
        ],
        notes="Corriger individuellement. Ces échanges préparent le cas « repas » du jeu de "
              "rôle de E1.")

    return d.save(dossier)
