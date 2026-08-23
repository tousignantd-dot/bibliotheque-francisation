# -*- coding: utf-8 -*-
"""C4 · Redire sans répéter, et tenir les phrases ensemble
Bloc C « Défi 2 » · couleur ambre · 75 min.
Source : exercices `t2subst`, `t2refor` et `t2garde` ; mini-leçons du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Redire sans répéter, et tenir les phrases ensemble",
        chapeau="Un texte où le même mot revient six fois paraît pauvre. Un "
                "texte sans connecteurs est une liste. Deux outils, une "
                "séance, et le résumé de l'équipe est écrit à la fin.",
        duree='75 minutes')

    d.titre(notes="Dernière séance du Défi 2, et séance de production : les trente "
                  "dernières minutes servent à écrire le résumé de l'équipe. Prévoir "
                  "le temps, ne pas déborder sur la théorie.")

    d.objectifs([
        "reprendre une idée avec un autre mot que celui de la phrase d'avant ;",
        "employer autrement dit, quant à, en somme, par conséquent ;",
        "trier ce qui entre dans un résumé et ce qui en sort ;",
        "écrire le résumé de son équipe, en dix lignes.",
    ], notes="Les trois premiers objectifs sont les outils, le quatrième est le "
             "produit. Si le temps manque, sacrifier le troisième : il a été vu en "
             "C2.")

    d.declencheur(
        'Observation', "Le mot qui revient six fois",
        pistes=[
            "« Les arbres… ces arbres… les arbres de la rue… »",
            "Comment feriez-vous pour ne pas répéter ?",
            "Est-ce qu'un synonyme dit toujours exactement la même chose ?",
            "Que se passe-t-il si le lecteur ne sait plus de quoi on parle ?",
        ],
        notes="La quatrième piste est la limite de l'exercice : reprendre, oui ; "
              "devenir vague, non. Elle prépare le piège de la séance.")

    d.tableau('Analyse', "Quatre façons de reprendre",
              ['Le procédé', 'Un exemple'],
              [["Un mot plus général",
                "quatre cents érables, puis ces arbres"],
               ["Un mot voisin",
                "le relevé aérien, puis cette mesure"],
               ["Le nom de l'action",
                "on a planté, puis cette plantation"],
               ["Une description",
                "le stationnement, puis ce secteur minéralisé"]],
              cle=0,
              note="Presque toujours avec ce, cette, ces : le démonstratif dit « je reprends ».",
              notes="Diapositive à photographier. Le troisième procédé vient de C3 : "
                    "la nominalisation sert deux fois, à raccourcir et à reprendre.")

    d.pratique('Grammaire', "Quel procédé ?",
               "Dites comment la deuxième phrase reprend la première.", [
        ("« quatre cents érables » puis « ces arbres »", "un mot plus général"),
        ("« le relevé aérien » puis « cette mesure »", "un mot voisin"),
        ("« on a planté » puis « cette plantation »", "le nom de l'action"),
        ("« le stationnement » puis « ce secteur minéralisé »", "une description"),
        ("« Youssouf voulait compter » puis « sa proposition »", "le nom de l'action"),
    ], corrige=True,
       notes="Aller vite. L'objectif n'est pas de nommer les procédés dans un examen, "
             "c'est d'en avoir quatre sous la main en écrivant.")

    d.tableau('Analyse', "Six connecteurs, six promesses",
              ['Le connecteur', 'Ce qu\'il promet'],
              [["autrement dit", "la même idée, en plus simple"],
               ["c'est-à-dire", "la précision de ce qui vient d'être nommé"],
               ["quant à", "un nouveau point, sans lien avec le précédent"],
               ["en ce qui concerne", "la même chose, un ton plus soigné"],
               ["par conséquent", "ce qui suit découle de ce qui précède"],
               ["en somme", "la fin : tout tient dans cette phrase"]],
              cle=0,
              notes="Diapositive à photographier. « En somme » ne s'emploie qu'une "
                    "fois par texte : le dire, sinon il paraîtra trois fois dans les "
                    "résumés remis.")

    d.piege('Écrit',
            "« Ces éléments ont été mesurés. »",
            "« Ces deux rues ont été mesurées. »",
            "Si le paragraphe parle d'arbres et de trottoirs, « ces "
            "éléments » ne désigne plus rien. Le lecteur s'arrête, relit, et "
            "vous l'avez perdu. Une reprise doit n'avoir qu'un seul "
            "candidat possible.",
            notes="Le piège de la reprise, et le plus fréquent. Faire chercher dans "
                  "les résumés déjà écrits : il y a presque toujours un « ces "
                  "éléments » ou un « ils » sans antécédent.")

    d.pratique('Production', "Complétez avec le bon connecteur",
               "Chacun n'est employé qu'une fois.", [
        ("L'arbre rejette de l'eau, et cela consomme de la chaleur. ___, il refroidit l'air.", "Autrement dit"),
        ("___ l'arrosage, la ville demande l'aide des résidents.", "En ce qui concerne"),
        ("Les trois quarts du sol sont minéralisés ; ___, le secteur chauffe.", "par conséquent"),
        ("Nous avons le chiffre de la ville. ___ notre secteur, nous n'avons rien.", "Quant à"),
        ("Le nombre ne dit rien, l'âge change tout. ___, c'est la canopée qui compte.", "En somme"),
    ], corrige=True,
       notes="Faire lire la phrase entière à voix haute après correction. Le "
             "connecteur s'entend autant qu'il se lit.")

    d.pratique('Production écrite', "Le résumé de votre équipe",
               "Dix lignes, à écrire pendant la séance.", [
        ("En haut de la feuille", "votre question de départ, écrite en entier"),
        ("Chaque phrase", "doit pouvoir se rattacher à cette question"),
        ("Au moins deux noms d'action", "la plantation, l'arrosage, la mesure"),
        ("Deux reprises", "sans répéter le même mot"),
        ("Trois connecteurs", "pas davantage dans dix lignes"),
        ("Une citation, au plus", "entre guillemets, avec sa source"),
    ], corrige=False,
       notes="Le produit du Défi 2. Ramasser à la fin de la séance : ces dix lignes "
             "sont la matière de l'exposé du bloc E, et l'enseignante a besoin de "
             "les avoir lues avant.")

    d.billet(
        "Quelle phrase avez-vous enlevée de votre résumé, et pourquoi ?",
        exemples=[
            "La phrase, puis la raison, en une ligne.",
            "Une phrase vraie et hors sujet compte double.",
        ],
        notes="Billet de sortie du Défi 2. Les réponses disent qui a compris que "
              "résumer, c'est jeter. Ceux qui n'ont rien enlevé n'ont pas résumé.")

    return d.save(dossier)
