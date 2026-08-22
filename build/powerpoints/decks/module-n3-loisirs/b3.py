# -*- coding: utf-8 -*-
"""B3 · Je voudrais, j'aimerais, vous pourriez.
Bloc B « Défi 1 · Quand, combien, quoi apporter ? » · ambre · 75 min.
Source du module : exercice `t1poli`, mini-leçon `t1poli`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Je voudrais, j'aimerais, vous pourriez",
        chapeau="« Je veux des renseignements » est juste, mais sec. Trois "
                "lettres de plus — la terminaison en -rais — et la demande "
                "devient celle qu'on attend au comptoir et au téléphone.",
        duree='75 minutes')

    d.titre(notes="Séance d'écriture, mais le point se travaille d'abord à l'oreille : "
                  "la différence entre « je veux » et « je voudrais » s'entend avant de "
                  "s'expliquer. Faire dire les deux, et demander laquelle surprend.")

    d.objectifs([
        "employer « je voudrais » et « j'aimerais » pour dire ce que je veux ;",
        "employer « je pourrais » pour demander une permission ;",
        "employer « vous pourriez » pour demander un service ;",
        "reconnaître « il faut » et « il faudrait », et ce qui les sépare.",
    ])

    d.regle("La forme polie, en une phrase",
            "Le verbe se termine en -rais, et la demande s'adoucit.",
            precision="« Je voudrais », « j'aimerais », « je pourrais », « vous "
                      "pourriez », « il faudrait ». La terminaison s'entend « rè » dans "
                      "tous les cas. C'est la forme du comptoir, du téléphone et de tous "
                      "les services.",
            notes="Diapo à photographier. Le nom savant — le conditionnel de politesse — "
                  "peut être donné, mais il n'aide personne : c'est la terminaison qui "
                  "compte, et elle est régulière.")

    d.tableau('Analyse', "Quatre emplois, quatre phrases",
              ["Ce qu'on veut faire", "La phrase"],
              [["dire ce qu'on veut", "Je voudrais des renseignements, s'il vous plaît."],
               ["dire un souhait", "J'aimerais essayer le badminton."],
               ["demander une permission", "Est-ce que je pourrais venir voir une fois ?"],
               ["demander un service", "Vous pourriez répéter, s'il vous plaît ?"],
               ["dire ce qui est nécessaire", "Il faudrait apporter une preuve d'adresse."]],
              cle=0,
              note="Les deux premières lignes ouvrent la conversation ; la quatrième la sauve.",
              notes="Diapo à photographier. Les deux phrases à apprendre par cœur sont "
                    "la première et la quatrième. Les faire recopier, puis les faire "
                    "dire les yeux fermés.")

    d.cartes("Les deux phrases à savoir par cœur", "Elles ouvrent et elles sauvent", [
        ("Je voudrais des renseignements, s'il vous plaît.",
         "La phrase d'ouverture de n'importe quelle conversation de service : au centre "
         "communautaire, à la bibliothèque, au bureau de poste, à la caisse. Elle dit "
         "qu'on vient chercher de l'information, et rien de plus."),
        ("Vous pourriez répéter, s'il vous plaît ?",
         "La phrase qui sauve toutes les conversations où ça va trop vite. Elle ne dit "
         "pas « je ne comprends rien » : elle demande simplement une deuxième écoute, "
         "ce que tout le monde accorde volontiers."),
    ], cols=1,
       notes="Prendre cinq minutes entières là-dessus. Faire dire les deux phrases par "
             "chaque élève, une par une, à voix haute. C'est le contenu le plus "
             "directement utile de la semaine.")

    d.piege('Le piège', "je voudrai", "je voudrais",
            "Une seule lettre, et deux sens différents. « Je voudrai » sans s parle du "
            "futur : plus tard, je voudrai. « Je voudrais » avec s est la demande polie. "
            "À l'oral, on entend « rè » pour le second et « ré » pour le premier — mais "
            "beaucoup de gens ne font plus la différence en parlant, alors c'est à "
            "l'écrit que le s compte.",
            notes="Faire écrire les deux formes au tableau, l'une sous l'autre. La faute "
                  "revient dans le message écrit du bloc E : la signaler maintenant coûte "
                  "moins cher que de la corriger là.")

    d.pratique('Écriture · 1 de 2', "Complétez la demande",
               "Complétez avec « je voudrais », « j'aimerais », « je pourrais », "
               "« vous pourriez » ou « il faudrait ».", [
        ("Bonjour. ___ des renseignements sur le badminton, s'il vous plaît.",
         "Je voudrais"),
        ("___ essayer la danse en ligne, mais je n'ai jamais dansé.",
         "J'aimerais"),
        ("Est-ce que ___ venir voir une fois avant de payer ?", "je pourrais"),
        ("Excusez-moi, ___ répéter le prix, s'il vous plaît ?", "vous pourriez"),
        ("Pour le tarif du quartier, ___ apporter une preuve d'adresse.", "il faudrait"),
        ("___ inscrire ma fille au samedi matin.", "J'aimerais · Je voudrais"),
    ], corrige=True,
       notes="C'est l'exercice t1poli du module. Faire remarquer que la dernière ligne "
             "accepte deux réponses : les deux verbes disent la même chose.")

    d.pratique('Écriture · 2 de 2', "Adoucissez la phrase",
               "Récrivez chaque phrase à la forme polie.", [
        ("Je veux des renseignements.", "Je voudrais des renseignements, s'il vous plaît."),
        ("Répétez.", "Vous pourriez répéter, s'il vous plaît ?"),
        ("Je viens essayer jeudi.", "Est-ce que je pourrais venir essayer jeudi ?"),
        ("Il faut une preuve d'adresse.", "Il faudrait une preuve d'adresse."),
        ("Donnez-moi un feuillet.", "Est-ce que je pourrais avoir un feuillet ?"),
    ], corrige=True,
       notes="Faire lire la colonne de gauche puis celle de droite, à voix haute. La "
             "différence de ton s'entend immédiatement, et c'est ce qui convainc.")

    d.billet(
        "Écrivez trois demandes polies que vous pourriez faire cette semaine.",
        exemples=[
            "Une au centre communautaire, une ailleurs — à l'école, dans un commerce.",
            "Employez « je voudrais », « je pourrais » et « vous pourriez ».",
        ],
        notes="Devoir court. Ramasser : ce sont les phrases que la production orale du "
              "bloc E réclamera, et les corriger maintenant évite d'y revenir.")

    return d.save(dossier)
