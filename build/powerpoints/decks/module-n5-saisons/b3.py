# -*- coding: utf-8 -*-
"""B3 · Il neige, il ventera, il faudra
Bloc B « Défi 1 · Ce que l'avertissement annonce » · couleur ambre · 75 min.
Source : exercice `t1imp` et sa mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Il neige, il ventera, il faudra",
        chapeau="« Il pleut. » Qui, il ? Personne. Ce sujet qui ne désigne "
                "rien est la forme normale du français pour parler du temps — "
                "et beaucoup de langues s'en passent, d'où la faute la plus "
                "visible du niveau.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Le mot « impersonnel » fait peur et la chose est "
                  "simple : un sujet obligatoire qui ne désigne rien. Le dire ainsi dès "
                  "la première minute, et ne plus employer le mot savant qu'une fois "
                  "l'idée acquise.")

    d.objectifs([
        "employer les verbes de météo avec « il » : il pleut, il neige, il vente ;",
        "employer « il y a » et « il y aura » sans les accorder ;",
        "employer « il faut » pour dire une obligation sans nommer personne ;",
        "employer « il est possible que » avec le subjonctif.",
    ], notes="Le troisième objectif rend un service inattendu : devant un groupe, "
             "« il faut apporter » passe beaucoup mieux que « vous devez apporter ». "
             "C'est de la politesse, autant que de la grammaire.")

    d.declencheur(
        'Comparaison', "« Il fait froid. » Est-ce qu'on dit la même chose "
                       "dans votre première langue ?",
        pistes=[
            "Y a-t-il un sujet devant le verbe, dans votre langue ?",
            "Que désigne le « il » de « il fait froid » ?",
            "Que se passe-t-il si on l'enlève : « fait froid » ?",
            "Connaissez-vous d'autres phrases françaises avec ce « il » ?",
        ],
        notes="Faire répondre plusieurs langues différentes : l'espagnol, l'arabe, le "
              "créole et le mandarin n'ont pas ce sujet, l'anglais l'a. Le groupe "
              "comprend alors que la difficulté est réelle et pas personnelle.")

    d.regle("Un sujet qui ne désigne personne",
            "« Il » est là parce qu'un verbe conjugué, en français, a besoin "
            "d'un sujet devant lui.",
            precision="Il ne remplace aucun nom. On ne peut ni le supprimer, ni "
                      "le remplacer par « le ciel » ou « le temps ».",
            notes="Diapositive à photographier. Faire produire dix phrases en série — il "
                  "pleut, il neige, il vente, il grêle, il gèle, il fait froid — jusqu'à "
                  "ce que le « il » vienne tout seul.")

    d.cartes("Quatre familles", "Les tournures impersonnelles du module", [
        ("Les verbes de météo",
         "il pleut · il neige · il vente · il grêle · il gèle"),
        ("Faire + la température",
         "il fait froid · il fait moins douze · il fera beau"),
        ("Il y a, à tous les temps",
         "il y a · il y aura · il y a eu — jamais d'accord"),
        ("Il faut, il est possible que",
         "il faut apporter… · il est possible que la sortie soit reportée"),
    ], notes="La troisième carte mérite un arrêt : « il y a » ne s'accorde jamais, quel "
             "que soit le nombre. Il y a une personne, il y a trente personnes. C'est un "
             "des rares endroits du français sans question d'accord.")

    d.tableau('Le sujet rejeté', "Deux façons de dire la même chose",
              ['La forme normale', 'La forme impersonnelle'],
              [["Trente centimètres de neige tomberont.", "Il tombera trente centimètres de neige."],
               ["Cinq millimètres de glace se déposeront.", "Il se déposera cinq millimètres de glace."],
               ["Deux personnes manquent.", "Il manque deux personnes."],
               ["Personne ne parle comme ça.", "C'est la forme qu'on entend."]],
              cle=1,
              notes="La colonne de gauche est correcte et personne ne l'emploie. Le dire "
                    "franchement : l'élève doit produire la colonne de droite, et "
                    "seulement reconnaître celle de gauche.")

    d.piege("Laisser tomber le « il »",
            "Fait froid dehors. Pleut depuis ce matin.",
            "Il fait froid dehors. Il pleut depuis ce matin.",
            "Le sujet est obligatoire même quand il ne désigne rien. C'est la "
            "faute la plus visible du niveau, et la plus vite corrigée.",
            notes="Ne pas la traiter comme une étourderie : elle vient de la première "
                  "langue de l'élève, où la phrase est complète sans sujet. Le nommer "
                  "enlève la honte et accélère la correction.")

    d.piege("Mettre l'indicatif après « il est possible que »",
            "Il est possible que la sortie est reportée.",
            "Il est possible que la sortie soit reportée.",
            "Après « il est possible que », le subjonctif. Apprenez la formule "
            "entière — il est possible que… soit — plutôt que la règle.",
            notes="C'est la phrase de la veille météo, exactement : possible, pas "
                  "certain. La faire dire dix fois telle quelle ; le subjonctif "
                  "s'installera plus tard, par d'autres formules.")

    d.pratique('Grammaire', "Complétez la tournure",
               "Il fera, il tombera, il y aura, il ventera, il faut, "
               "il est possible que.", [
        ("___ moins douze demain matin, avec du vent.", "Il fera"),
        ("___ de trois à cinq millimètres de glace sur les surfaces.", "Il tombera"),
        ("___ de la poudrerie sur la route 132 en soirée.", "Il y aura"),
        ("___ fort toute la nuit, entre 60 et 80 kilomètres à l'heure.", "Il ventera"),
        ("___ apporter des crampons : les trottoirs seront glacés.", "Il faut"),
        ("___ la sortie soit reportée ; je vous confirme vendredi.", "Il est possible que"),
    ], corrige=True,
       notes="Ce sont les six items de l'exercice t1imp du module. Les faire ici sur "
             "papier, puis renvoyer au module. Faire relire chaque phrase à voix haute : "
             "le « il » doit s'entendre.")

    d.billet(
        "Écrivez le bulletin de demain en cinq phrases impersonnelles.",
        exemples=[
            "Une avec « il fera », une avec « il y aura », une avec « il faut ».",
            "Terminez par une phrase avec « il est possible que ».",
        ],
        notes="Ramasser les billets : ils servent de brouillon au message du groupe, en "
              "E1. Les phrases avec « il est possible que » montrent d'un coup d'œil qui "
              "a compris le subjonctif de la formule.")

    return d.save(dossier)
