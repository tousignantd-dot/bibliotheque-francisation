# -*- coding: utf-8 -*-
"""A4 · Les cinq questions d'une nouvelle.
Bloc A · couleur acier (compréhension) · 60 min.
Source : exercice `aFait1` — le cycliste secouru, lu selon qui, quoi, où, quand.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A4', section='acier',
        titre='Les cinq questions',
        chapeau="Qui, quoi, où, quand, pourquoi. Un journaliste répond à ces cinq "
                "questions dans ses deux premières phrases. Les chercher, c'est "
                "comprendre une nouvelle sans tout comprendre.",
        duree='60 minutes')

    d.titre(notes="Écrire les cinq questions au tableau et les y laisser tout le module. "
                  "Cette séance est la méthode de lecture et d'écoute de tout le reste.")

    d.objectifs([
        "repérer les cinq informations essentielles d'une nouvelle ;",
        "les trouver dans les deux premières phrases ;",
        "distinguer l'essentiel du détail ;",
        "résumer une nouvelle en une phrase.",
    ])

    d.tableau('Analyse', "Les cinq questions et ce qu'elles cherchent",
              ['La question', 'Ce qu\'on cherche'],
              [["qui ?", "les personnes concernées"],
               ["quoi ?", "l'événement, en un verbe"],
               ["où ?", "la ville, le lieu précis"],
               ["quand ?", "le jour, l'heure si elle compte"],
               ["pourquoi ?", "la cause, quand elle est connue"]],
              cle=0,
              note="La cinquième manque souvent : la cause d'un événement n'est pas "
                   "toujours connue au moment où la nouvelle est publiée.",
              notes="Insister : « pourquoi » est la seule des cinq qui peut légitimement "
                    "manquer. Les quatre autres sont toujours là.")

    d.regle('La règle de lecture',
            "Les cinq réponses sont dans les deux premières phrases.",
            precision="Un journaliste écrit du plus important au moins important. La "
                      "première phrase répond à qui, quoi, où, quand. La suite ajoute "
                      "des détails, des témoignages, des conséquences.",
            notes="C'est le principe de la pyramide inversée. Ne pas employer le terme, "
                  "mais l'expliquer : on peut arrêter de lire quand on veut, on aura "
                  "l'essentiel.")

    d.cartes('Le texte', "Un cycliste secouru par des passants", [
        ("Ce qui est arrivé",
         "À Trois-Pistoles, un cycliste de 42 ans a fait une chute importante sur la "
         "piste cyclable hier après-midi."),
        ("Qui a aidé",
         "Deux passants qui marchaient à proximité ont porté secours à l'homme et ont "
         "appelé les services d'urgence."),
        ("Ce qui a suivi",
         "L'ambulance est arrivée en moins de dix minutes. Le cycliste, blessé à "
         "l'épaule, a été transporté à l'hôpital de Rivière-du-Loup."),
        ("La cause et la suite",
         "Un nid-de-poule mal signalé serait à l'origine de l'accident. La Ville a "
         "annoncé qu'elle inspecterait la piste dès cette semaine."),
    ], notes="Faire lire les quatre cartes dans l'ordre, puis demander laquelle on "
             "pourrait retirer sans perdre l'essentiel. La réponse est la quatrième — et "
             "c'est la structure du texte.")

    d.pratique('Pratique · 1 de 4', "Les quatre questions du texte",
               "D'après le fait divers sur le cycliste.", [
        ("Qui ?", "un cycliste de 42 ans et deux passants qui l'ont aidé"),
        ("Quoi ?", "il a fait une chute et a été blessé à l'épaule"),
        ("Où ?", "à Trois-Pistoles, sur une piste cyclable"),
        ("Quand ?", "hier après-midi"),
        ("Pourquoi ?", "un nid-de-poule mal signalé, selon les autorités"),
    ], corrige=True,
       notes="Faire pointer, pour chaque réponse, la phrase exacte du texte. La "
             "cinquième arrive tard : c'est normal.")

    d.regle('Le mot qui prévient',
            "« Selon », « serait », « aurait » : l'information n'est pas confirmée.",
            precision="« Un nid-de-poule serait à l'origine de l'accident. » Le "
                      "conditionnel et le mot « selon » disent que c'est une hypothèse. "
                      "Le journaliste ne l'affirme pas.",
            notes="Notion importante de lecture critique. La montrer une fois ici, y "
                  "revenir en C1 avec le texte du concours.")

    d.pratique('Pratique · 2 de 4', "Confirmé ou non confirmé ?",
               "Cherchez « selon », « serait », « aurait », « on croit ».", [
        ("Le cycliste a été transporté à l'hôpital.", "confirmé"),
        ("Un nid-de-poule serait à l'origine de l'accident.", "non confirmé"),
        ("L'ambulance est arrivée en moins de dix minutes.", "confirmé"),
        ("Selon les autorités, la piste sera inspectée cette semaine.",
         "annoncé par quelqu'un, pas encore fait"),
    ], corrige=True,
       notes="Exercice court et décisif. Faire chercher ces mots dans un vrai journal "
             "s'il y en a un en classe.")

    d.piege("Le piège du détail retenu",
            "Je retiens « 42 ans » et j'oublie « chute sur la piste cyclable ».",
            "L'événement d'abord, les chiffres ensuite.",
            "Les chiffres et les noms propres attirent l'attention parce qu'ils sont "
            "difficiles. Mais ce qu'il faut retenir, c'est le verbe : qu'est-ce qui est "
            "arrivé ? Un détail sans événement ne sert à rien.",
            notes="Faire l'expérience : demander au groupe ce qu'il a retenu du texte "
                  "après une seule lecture. Les chiffres dominent souvent.")

    d.pratique('Pratique · 3 de 4', "Résumez en une phrase",
               "Qui, quoi, où, quand — en une seule phrase.", [
        ("Le cycliste de Trois-Pistoles",
         "Hier, à Trois-Pistoles, un cycliste a été blessé dans une chute et secouru "
         "par deux passants."),
        ("La collecte de mitaines",
         "Des élèves de Longueuil ont amassé plus de deux cents paires de mitaines pour "
         "les enfants du quartier."),
        ("Le chat retrouvé",
         "À Gatineau, une fillette a retrouvé son chat disparu grâce à une affiche."),
    ], corrige=True,
       notes="Résumer en une phrase est plus difficile que répondre à cinq questions. "
             "Laisser cinq minutes et faire lire trois versions.")

    d.pratique('Pratique · 4 de 4', "Trouvez ce qui manque",
               "Chaque résumé oublie une des quatre questions.", [
        ("« Un cycliste a été blessé hier après-midi. »", "où — le lieu manque"),
        ("« À Trois-Pistoles, un cycliste a été blessé. »", "quand — le moment manque"),
        ("« Hier, à Trois-Pistoles, il y a eu un accident. »", "qui — la personne manque"),
        ("« Hier, à Trois-Pistoles, un cycliste de 42 ans. »", "quoi — l'événement manque"),
    ], corrige=True,
       notes="Le dernier item est le plus révélateur : une phrase sans verbe ne dit "
             "rien, même avec trois informations sur quatre.")

    d.billet(
        "Résumez en une phrase une nouvelle entendue cette semaine.",
        exemples=[
            "Qui, quoi, où, quand — dans une seule phrase.",
            "Ajoutez en dessous : est-ce que la cause est connue ?",
        ],
        notes="Ces résumés serviront de matière première en B5, où chacun racontera sa "
              "nouvelle à voix haute.")

    return d.save(dossier)
