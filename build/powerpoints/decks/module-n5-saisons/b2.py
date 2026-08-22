# -*- coding: utf-8 -*-
"""B2 · Ce qui arrivera : le futur simple
Bloc B « Défi 1 · Ce que l'avertissement annonce » · couleur acier · 75 min.
Source : exercice `t1fut` et sa mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B2', section='acier',
        titre="Ce qui arrivera : le futur simple",
        chapeau="Un bulletin ne parle jamais du présent. La pluie débutera, "
                "les trottoirs deviendront glissants, le mercure remontera. "
                "C'est la langue de la prévision — et c'est aussi celle de la "
                "promesse : « je vous confirmerai vendredi à midi ».",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire. Ouvrir en réécoutant vingt secondes du bulletin "
                  "de B1 et en faisant relever tous les verbes : ils sont tous au futur. "
                  "La règle se découvre ainsi, dans un texte réel, avant d'être posée.")

    d.objectifs([
        "former le futur simple sur l'infinitif, aux six personnes ;",
        "employer les sept irréguliers du bulletin sans hésiter ;",
        "mettre le présent après « si » de condition, jamais le futur ;",
        "employer le futur simple pour une promesse faite à un groupe.",
    ], notes="Le troisième objectif est la faute la plus fréquente du niveau et elle "
             "s'entend tout de suite. Le quatrième est celui qui sert dans la production "
             "orale de E1 : le futur ne dit pas que la météo, il engage celui qui parle.")

    d.declencheur(
        'Relevé', "Réécoutez le bulletin. Combien de verbes au présent ?",
        pistes=[
            "Relevez cinq verbes du bulletin. À quel temps sont-ils ?",
            "Pourquoi un bulletin ne parle-t-il jamais du présent ?",
            "Que change « je vous confirmerai » par rapport à « je confirme » ?",
            "Et « la sortie est reportée » par rapport à « sera reportée » ?",
        ],
        notes="La quatrième piste anticipe C4 : pour une décision déjà prise, le présent "
              "est plus ferme que le futur. Ne pas la développer ici — la poser, et y "
              "revenir.")

    d.regle("L'infinitif, puis six terminaisons",
            "-ai, -as, -a, -ons, -ez, -ont, ajoutés à l'infinitif entier.",
            precision="Pour les verbes en -re, on enlève seulement le e final : "
                      "descendre donne « le mercure descendra ».",
            notes="Diapositive à photographier. C'est le temps le plus régulier du "
                  "français : toutes les personnes gardent le même radical. Ce qui se "
                  "travaille, ce ne sont pas les terminaisons, ce sont les irréguliers.")

    d.cartes("Sept irréguliers", "Ceux du bulletin, à savoir par cœur", [
        ("être : il sera", "« Une amélioration sera possible en après-midi. »"),
        ("avoir : il y aura", "« Il y aura de la poudrerie sur la route. »"),
        ("faire : il fera", "« Il fera moins douze demain matin. »"),
        ("aller : ça ira", "« Ça ira mieux à partir de samedi midi. »"),
        ("pouvoir : on pourra", "« On pourra sortir sans crampons lundi. »"),
        ("falloir : il faudra", "« Il faudra apporter des bottes. »"),
    ], cols=2,
       notes="Cinq des sept sont impersonnels dans un bulletin : il sera, il y aura, il "
             "fera, il faudra, il viendra. L'élève n'aura presque jamais à les conjuguer "
             "à une autre personne — le dire, ça allège l'apprentissage de moitié.")

    d.tableau('Deux moitiés', "Le si de condition ne prend jamais le futur",
              ['Après « si »', "Dans l'autre moitié"],
              [["Si l'avertissement est levé,", "nous maintiendrons la sortie."],
               ["Si la nouvelle date ne vous convient pas,", "appelez-moi avant jeudi."],
               ["S'il fait moins trente,", "nous partirons plus tard."],
               ["Présent, toujours", "Futur, ou impératif"]],
              note="Jamais « si l'avertissement sera levé ».",
              notes="Faire produire cinq phrases au tableau, par des élèves différents. "
                    "La règle se retient mieux par une phrase entière que par la formule "
                    "« présent après si ».")

    d.piege("Mettre le futur après « si »",
            "Si l'avertissement sera levé, nous maintiendrons la sortie.",
            "Si l'avertissement est levé, nous maintiendrons la sortie.",
            "Après « si » de condition, présent obligatoire. Le futur va dans "
            "l'autre moitié de la phrase, jamais dans les deux.",
            notes="C'est la faute la plus fréquente à ce niveau, et elle s'entend tout de "
                  "suite. La corriger ici en profondeur évite de la reprendre à chaque "
                  "production du reste du module.")

    d.pratique('Grammaire', "Mettez au futur simple",
               "Le verbe est entre parenthèses ; écrivez la forme du bulletin.", [
        ("La pluie verglaçante ___ (débuter) vendredi en soirée.", "débutera"),
        ("Elle ___ (se poursuivre) jusqu'à samedi matin.", "se poursuivra"),
        ("Les trottoirs ___ (devenir) très glissants pendant la nuit.", "deviendront"),
        ("Il ___ (faire) moins douze demain matin.", "fera"),
        ("Il y ___ (avoir) trente centimètres de neige au sol.", "aura"),
        ("Je vous ___ (confirmer) vendredi à midi.", "confirmerai"),
    ], corrige=True,
       notes="Ce sont les six items de l'exercice t1fut du module. Les faire ici sur "
             "papier, puis renvoyer au module pour la correction automatique et la "
             "mini-leçon. Le dernier n'est pas de la météo : c'est une promesse.")

    d.billet(
        "Écrivez trois phrases au futur simple sur le temps qu'il fera demain.",
        exemples=[
            "Une avec « il fera », une avec « il y aura », une libre.",
            "Ajoutez une quatrième phrase : ce que vous ferez, vous, si c'est le cas.",
        ],
        notes="La quatrième phrase force la construction avec « si » : c'est là qu'on "
              "voit si la règle a tenu. Ramasser les billets et relever les fautes pour "
              "les reprendre en B3.")

    return d.save(dossier)
