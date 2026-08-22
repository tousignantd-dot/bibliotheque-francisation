# -*- coding: utf-8 -*-
"""C3 · Le passé simple : le lire, jamais l'écrire
Bloc C « Défi 2 · La biographie de la réalisatrice » · couleur ambre · 75 min.
Source : exercice `t2ps` et sa mini-leçon « Le passé simple : le lire, jamais
l'écrire ».
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre="Le passé simple : le lire, jamais l'écrire",
        chapeau="Un temps qu'on lit toute sa vie et qu'on ne dit jamais. Le "
                "programme du niveau 6 en demande une seule chose : le "
                "reconnaître, et l'associer au passé composé.",
        duree='75 minutes')

    d.titre(notes="Troisième séance du Défi 2. Ouvrir en rassurant : personne ne "
                  "demandera jamais d'écrire au passé simple, ni dans cette classe ni "
                  "à l'examen. La séance sert à lire, et à lire seulement.")

    d.objectifs([
        "reconnaître un passé simple à la 3e personne ;",
        "le traduire en passé composé dans sa tête ;",
        "nommer les quatre terminaisons qui reviennent ;",
        "ne pas confondre « elle vint » et « elle vient ».",
    ], notes="Le quatrième objectif est le seul vrai piège de la séance, et il coûte "
             "cher : une lettre, et quarante ans d'écart.")

    d.declencheur(
        'Observation', "Ces verbes, tu les dirais comment ?",
        pistes=[
            "elle naquit · elle entra · il fut · le public revint",
            "Est-ce que ces actions sont finies ?",
            "Est-ce qu'elles sont plus anciennes que « elle est née » ?",
            "Où as-tu déjà rencontré ces formes ?",
        ],
        notes="La troisième piste est celle qui surprend : non, ce n'est pas plus "
              "ancien. La différence est de registre, pas de sens, et beaucoup "
              "d'élèves croient le contraire.")

    d.tableau('Analyse', "Quatre terminaisons, à la 3e personne",
              ['La terminaison', 'Les verbes'],
              [["-a", "elle tourna, elle quitta, elle entra"],
               ["-it", "elle partit, il finit, elle sortit"],
               ["-ut", "il fut, elle put, il voulut"],
               ["-int", "elle vint, il tint, elle revint"],
               ["au pluriel", "elles tournèrent, ils partirent, ils furent"]],
              cle=0,
              note="La 3e personne suffit : c'est la seule qu'on rencontre vraiment dans un texte.",
              notes="Diapositive à photographier. Ne pas donner le tableau complet de "
                    "conjugaison : il découragerait sans rien apporter.")

    d.regle("Le sens, exactement",
            "Le passé simple dit la même chose que le passé composé.",
            precision="Une action finie, à un moment précis du passé. Rien de plus "
                      "ancien, rien de plus solennel. La différence est de registre : "
                      "l'un s'écrit, l'autre se parle. « Elle naquit » et « elle est "
                      "née » racontent exactement le même fait.",
            notes="Diapositive à photographier. C'est la phrase qui débloque la "
                  "séance : les élèves cherchent une nuance de sens qui n'existe pas.")

    d.regle("Ce qu'on en demande",
            "Le reconnaître et le traduire. Jamais l'écrire.",
            precision="Écrire un passé simple à ce stade est exactement ce qu'il ne "
                      "faut pas faire : une forme inventée se voit tout de suite, et "
                      "le passé composé est juste partout, tout le temps. Dans un "
                      "courriel, un message ou une consigne, le passé simple ne "
                      "s'emploie jamais.",
            notes="Diapositive à photographier. Le redire au moment de la production "
                  "écrite de E2 : un résumé de film s'écrit au présent ou au passé "
                  "composé, jamais au passé simple.")

    d.pratique('Grammaire', "Traduisez en passé composé",
               "Récrivez chaque verbe comme on le dirait à voix haute.", [
        ("elle naquit à Rimouski", "elle est née à Rimouski"),
        ("elle quitta la Gaspésie", "elle a quitté la Gaspésie"),
        ("elle entra dans une salle de montage", "elle est entrée dans une salle de montage"),
        ("le film sortit en 1994", "le film est sorti en 1994"),
        ("la critique fut sévère", "la critique a été sévère"),
        ("le public revint", "le public est revenu"),
        ("elle y vint", "elle y est venue"),
        ("elle refusa de parler", "elle a refusé de parler"),
    ], corrige=True, cols=2,
       notes="Les items 3, 6 et 7 prennent l'auxiliaire « être » : les regrouper à la "
             "correction pour que la règle se voie trois fois de suite.")

    d.piege("Lire « elle vint » comme « elle vient »",
            "Elle vint à la rétrospective : elle vient à la rétrospective.",
            "Elle vint à la rétrospective : elle est venue à la rétrospective.",
            "Une seule lettre, et quarante ans d'écart. Dans une biographie, c'est "
            "presque toujours le passé — mais la seule façon d'en être sûr est de "
            "regarder la date de la phrase. Ici, 2016 : elle est venue, et c'est "
            "fini.",
            notes="Écrire les deux formes l'une sous l'autre au tableau. La différence "
                  "se voit mal à l'écran et bien sur un tableau.")

    d.cartes("Où vous le rencontrerez", "Et où vous ne le verrez jamais", [
        ("Dans les biographies",
         "celle de la feuille verte en est pleine, du premier au dernier verbe."),
        ("Dans les romans et les contes",
         "c'est le temps du récit écrit, en français comme dans les traductions."),
        ("Dans les documentaires",
         "la voix hors champ le lit ; elle ne l'improvise jamais."),
        ("Jamais dans un courriel",
         "ni dans un message, ni dans une consigne, ni dans une conversation."),
    ], notes="La quatrième carte est celle qui rassure le plus. La lire à voix haute "
             "et passer à la suite.")

    d.billet(
        "Recopie un verbe au passé simple de la feuille verte, et traduis-le.",
        exemples=[
            "Un verbe, et sa version parlée.",
            "Par exemple : « elle apprit » - « elle a appris ».",
        ],
        notes="Deux minutes. Les billets faux portent presque tous sur un verbe en "
              "-int : les reprendre en C4, en trente secondes.")

    return d.save(dossier)
