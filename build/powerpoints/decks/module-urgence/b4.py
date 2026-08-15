# -*- coding: utf-8 -*-
"""B4 · Raconter un accident.
Bloc B · couleur teal (écoute et réponds) · 60 min.
Source : exercices `t1img` et `t1desc` — quatre récits d'accidents.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/assets/'
       'interactive/module-urgence/images/')


def build(dossier):
    d = Deck(
        code='B4', section='teal',
        titre='Raconter un accident',
        chapeau="Quatre accidents, quatre récits. Ce qui les distingue n'est pas la "
                "gravité : c'est ce qu'il fallait faire dans les premières minutes.",
        duree='60 minutes')

    d.titre(notes="Séance de production orale. Prévoir la disposition en dyades. Les "
                  "billets de B1 servent de matière première : les rendre au début.")

    d.objectifs([
        "raconter un accident à voix haute, au passé composé ;",
        "reconnaître un accident grave à sa description ;",
        "dire ce qu'on a fait et ce qu'on n'a pas fait ;",
        "poser les questions qu'un témoin doit poser.",
    ])

    d.declencheur(
        'Mise en situation', "Qu'est-ce qui est arrivé, et qu'est-ce qu'il fallait faire ?",
        image=IMG + 'cheville-foulee.jpg',
        pistes=[
            "Racontez ce que vous voyez, au passé composé.",
            "Quel a été le premier geste à faire ?",
            "Est-ce un cas pour le 911, le 811, ou la clinique ?",
            "Quelle question poseriez-vous à la personne blessée ?",
        ],
        notes="Cinq minutes en grand groupe. Faire raconter par trois élèves différents "
              "et comparer les récits : l'ordre change, les informations aussi.")

    d.tableau('Analyse', "Quatre accidents et le bon service",
              ['La situation', 'Le service'],
              [["une douleur à la poitrine et au bras gauche", "le 911, sans attendre"],
               ["une cheville tordue qui a enflé tout de suite", "la clinique, aujourd'hui"],
               ["un genou bloqué après un coup au soccer", "la clinique ou l'urgence"],
               ["un enfant qui a touché un bouton de cuisinière", "le 811, pour un conseil"]],
              cle=0, props=[0.6, 0.4],
              notes="Faire justifier chaque choix par la question de A3 : est-ce que la "
                    "vie est en danger maintenant ?")

    d.cartes('Le modèle', "Le récit en quatre phrases", [
        ("Ce que je faisais",
         "À l'imparfait ou au passé composé simple : « je travaillais en cuisine », "
         "« je descendais l'escalier ». C'est le décor."),
        ("Ce qui est arrivé",
         "Au passé composé : « l'huile a éclaboussé », « j'ai glissé ». C'est "
         "l'événement, et il est bref."),
        ("Ce que ça m'a fait",
         "Verbe pronominal, au passé composé : « je me suis brûlé le bras », « je me "
         "suis tordu la cheville »."),
        ("Ce que j'ai fait",
         "Les premiers soins, au passé composé : « j'ai mis mon bras sous l'eau », "
         "« j'ai appelé le 811 »."),
    ], notes="Les quatre étiquettes sont celles de B1 ; les temps verbaux sont ceux de "
             "B2 et B3. Cette séance ne fait que les mettre ensemble.")

    d.regle("La phrase qu'on oublie toujours",
            "Dites aussi ce que vous n'avez PAS fait.",
            precision="« Je n'ai pas percé les cloques. » « Je n'ai rien mis sur la "
                      "peau. » Ces phrases négatives rassurent le soignant et évitent "
                      "des questions. C'est exactement ce que Fatou dit au médecin.",
            notes="Relier à la négation du module 1. Faire produire trois phrases "
                  "négatives sur les premiers soins.")

    d.pratique('Pratique · 1 de 3', "Associez le récit et l'accident",
               "Quatre récits, quatre situations.", [
        ("Il est devenu pâle et a serré sa poitrine. La douleur est descendue dans son bras gauche.",
         "une possible crise cardiaque — le 911"),
        ("J'ai mal posé le pied pendant ma course. Ma cheville a enflé tout de suite.",
         "une entorse — la clinique"),
        ("Un joueur m'a frappé la jambe. Je suis tombé et mon genou a bloqué.",
         "une blessure au genou — la clinique ou l'urgence"),
        ("Mon petit s'est approché de la cuisinière et a touché un bouton.",
         "une peur sans blessure — le 811 au besoin"),
    ], corrige=True,
       notes="Le quatrième récit se termine par « il ne s'est pas brûlé ». Faire "
             "remarquer que la phrase négative est ce qui change tout le diagnostic.")

    d.pratique('Pratique · 2 de 3', "Racontez, en quatre phrases",
               "Ce que je faisais · ce qui est arrivé · ce que ça m'a fait · ce que j'ai fait.", [
        ("Fatou, en cuisine",
         "Je travaillais en cuisine. L'huile a éclaboussé. Je me suis brûlé "
         "l'avant-bras. J'ai mis mon bras sous l'eau froide quinze minutes."),
        ("Une chute dans un escalier mouillé",
         "Je descendais l'escalier. J'ai glissé sur une marche mouillée. Je me suis "
         "tordu la cheville. J'ai mis de la glace et j'ai appelé le 811."),
        ("Une coupure en déchargeant un camion",
         "Je déchargeais un camion. Une caisse a glissé. Je me suis coupé la main. "
         "J'ai comprimé avec un linge propre."),
    ], corrige=True,
       notes="Faire dire chaque récit debout, sans notes. Corriger uniquement les "
             "auxiliaires : c'est le point de contrôle de la séance.")

    d.piege("Le piège du présent",
            "Je travaille en cuisine et l'huile éclabousse mon bras.",
            "Je travaillais en cuisine et l'huile a éclaboussé mon bras.",
            "Raconter un accident au présent est très fréquent chez les élèves, parce "
            "que c'est le temps qu'on maîtrise le mieux. Mais le médecin a besoin de "
            "savoir que c'est fini : le passé composé le dit, le présent ne le dit pas.",
            notes="Erreur systématique en début de module. La corriger doucement mais "
                  "chaque fois : c'est par la répétition qu'elle disparaît.")

    d.pratique('Pratique · 3 de 3', "Jeu de rôle · le témoin et le blessé",
               "À deux. L'un est blessé, l'autre pose les questions et appelle le 811.", [
        ("Le témoin ouvre", "Qu'est-ce qui s'est passé ?"),
        ("Le blessé raconte", "les quatre phrases, au passé composé"),
        ("Le témoin vérifie", "Est-ce que tu as mis quelque chose sur la peau ?"),
        ("Le témoin appelle", "il répète le récit à l'infirmière du 811"),
    ], corrige=False,
       notes="Le quatrième temps est le plus formateur : répéter le récit d'une autre "
             "personne oblige à l'avoir compris. Quinze minutes, puis on échange.")

    d.billet(
        "Racontez un accident en quatre phrases, au passé composé.",
        exemples=[
            "Une des quatre doit être négative : ce que vous n'avez pas fait.",
            "Soulignez les auxiliaires : avoir ou être.",
        ],
        notes="Ramasser. Ces billets préparent directement E1, où le même récit sera "
              "raconté au téléphone puis écrit dans un message.")

    return d.save(dossier)
