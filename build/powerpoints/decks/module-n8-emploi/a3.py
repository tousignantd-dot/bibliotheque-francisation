# -*- coding: utf-8 -*-
"""A3 · Deux registres, un seul français.
Bloc A « Je découvre » · couleur ambre · 75 min.
Source : exercice `prReg` et sa mini-leçon ; fin du dialogue `prep`.
"""
from theme import Deck

IMG = ('/Users/danieltousignant/Claude/bibliotheque-francisation/'
       'assets/interactive/module-n8-emploi/images/')


def build(dossier):
    d = Deck(
        code='A3', section='ambre',
        titre="Deux registres, un seul français",
        chapeau="Le registre familier n'est pas impoli et le registre standard "
                "n'est pas poli. L'un est juste à la machine à café, l'autre "
                "dans un courriel qui sera transféré à la direction.",
        duree='75 minutes')

    d.titre(notes="Séance qui défait une idée reçue tenace. Commencer par demander au "
                  "groupe si « c'est plate » est un mot impoli. La discussion part "
                  "toute seule.")

    d.objectifs([
        "reconnaître les marques du registre familier à l'oral ;",
        "reformuler un énoncé familier en français standard ;",
        "choisir le registre selon l'interlocuteur et le support ;",
        "éviter le registre trop soutenu, qui sonne faux entre collègues.",
    ], notes="Le quatrième objectif compte autant que les autres : « Veuillez agréer » "
             "à un collègue crée une distance qu'on n'a pas voulue.")

    d.declencheur(
        'Observation', "Où est-ce qu'on parle autrement, chez vous ?",
        image=IMG + 'machine-cafe.jpg',
        pistes=[
            "Parlez-vous pareil à votre patron et à votre voisine de poste ?",
            "Qu'est-ce que vous n'écririez jamais dans un courriel ?",
            "Où avez-vous appris les mots du travail ?",
            "Y a-t-il des mots que vous comprenez sans les employer ?",
        ],
        notes="Le troisième piste est la plus productive : tout le monde a une réponse, "
              "et elle mène directement à la règle de la séance.")

    d.regle("La règle pratique",
            "Tout ce qui s'écrit passe au registre standard.",
            precision="Un courriel se transfère, se relit six mois plus tard, se retrouve "
                      "devant la direction. Ce qui se disait très bien à la machine à "
                      "café devient, sur un écran, la preuve qu'on ne sait pas écrire. À "
                      "l'oral, entre collègues, on suit le groupe : parler comme un livre "
                      "isole autant que mal parler.",
            notes="Diapositive à photographier. C'est le seul repère à retenir, et il "
                  "règle quatre-vingt-dix pour cent des cas.")

    d.tableau('Analyse · 1 de 2', "Ce qui change dans la phrase",
              ['Familier (oral)', 'Standard (écrit)'],
              [["Ça marche pas.", "Cela ne fonctionne pas."],
               ["Tu viens-tu ?", "Venez-vous ?"],
               ["Mon boss, lui, il dit que…", "Ma superviseure estime que…"]],
              cle=1,
              note="Le « ne » disparaît à l'oral. À l'écrit, l'omettre est une faute.",
              notes="Diapositive à photographier. Les trois marques : le « ne » absent, "
                    "la question en « -tu », le sujet repris par un pronom.")

    d.tableau('Analyse · 2 de 2', "Ce qui change dans les mots",
              ['Familier (oral)', 'Standard (écrit)'],
              [["Ça m'a pris deux ans.", "Il m'a fallu deux ans."],
               ["C'est plate à dire.", "C'est regrettable."],
               ["J'écoperais de ce travail-là.", "Ce travail me reviendrait."]],
              cle=1,
              note="Le familier est concret et imagé ; le standard nomme les choses.",
              notes="Faire produire trois autres paires par le groupe, tirées de leur "
                    "propre milieu de travail.")

    d.cartes("Trois niveaux, pas deux", "Et le troisième est un piège", [
        ("Familier",
         "une job · un gars · jaser · plate · le fun. Juste entre collègues, faux dans un courriel."),
        ("Standard",
         "un emploi · un employé · discuter · regrettable · agréable. C'est la colonne du travail écrit."),
        ("Soutenu",
         "un poste · un collaborateur · s'entretenir · déplorable. Réservé à la correspondance très formelle."),
        ("L'erreur de niveau 8",
         "Employer le soutenu partout, croyant bien faire. À un collègue : « Cordialement » suffit, jamais « Veuillez agréer »."),
    ], notes="Insister sur la quatrième carte : c'est l'erreur typique d'un élève avancé "
             "qui a appris la langue dans les livres.")

    d.piege("Traduire une formule de sa langue",
            "J'espère que cette lettre vous trouve en bonne santé.",
            "Bonjour Madame, je donne suite à notre conversation du 19 août.",
            "Les formules d'ouverture et de clôture ne se traduisent pas : elles se "
            "remplacent. Chaque langue a les siennes, et une formule traduite mot à mot "
            "signale immédiatement qu'on écrit dans une langue apprise. Le français "
            "d'affaires entre dans le sujet dès la deuxième ligne.",
            notes="Demander à chacun la formule d'ouverture de sa langue, puis la "
                  "remplacer ensemble. Exercice court et très apprécié.")

    d.pratique('Reformulation', "Du corridor au courriel",
               "Réécrivez la phrase en français standard.", [
        ("Ça marche pas, leur affaire.", "Leur système ne fonctionne pas."),
        ("Ça m'a pris deux ans avant de comprendre.", "Il m'a fallu deux ans pour comprendre."),
        ("C'est plate à dire.", "C'est regrettable."),
        ("Le gars de la découpe part à une heure.", "L'employé de la découpe termine à treize heures."),
        ("Elle t'a passé le grand portrait ?", "Vous a-t-elle présenté l'ensemble de vos tâches ?"),
        ("Ça se jase à la machine à café.", "Cela se transmet de façon informelle."),
        ("Tant qu'à faire, ajoutez-la.", "Par la même occasion, ajoutez-la."),
        ("J'écoperais de ce travail-là.", "Ce travail me reviendrait."),
    ], corrige=True,
       notes="Plusieurs réponses sont acceptables. Corriger le registre, pas le choix "
             "du synonyme.")

    d.billet(
        "Relisez le dernier courriel que vous avez écrit en français.",
        exemples=[
            "Y a-t-il une négation sans « ne » ?",
            "Y a-t-il un mot que vous n'écririez pas devant la direction ?",
        ],
        notes="Devoir de relecture, pas de rédaction. C'est sur son propre texte qu'on "
              "voit le registre, jamais sur celui d'un manuel.")

    return d.save(dossier)
