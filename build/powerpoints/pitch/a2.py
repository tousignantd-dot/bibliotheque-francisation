# -*- coding: utf-8 -*-
"""A2 · Le cours sur un téléphone — l'adaptation, exercice par exercice.

Section indigo · l'annexe qui répond à la question posée dans toutes les salles :
« et sur un téléphone, ça donne quoi ? ». La réponse n'est pas « c'est
responsive » : c'est de montrer les sept familles d'exercices, au doigt.

Dix-huit captures existent dans le document papier ; le diaporama en projette
onze — les sept familles, plus l'entrée, les outils et les deux productions.
Projeter les dix-huit ferait une annexe plus longue que le pitch.

Source : `assets/presentations/captures-telephone.html`.
"""
from theme import Deck
from vues import ecran, poser


def build(dossier):
    d = Deck(
        code='A2', section='indigo',
        titre="Le cours sur un téléphone",
        chapeau="Beaucoup d'élèves en francisation n'ont pas d'ordinateur à la maison — "
                "ils ont un téléphone. Le cours entier s'y fait : les sept familles "
                "d'exercices, l'enregistrement de la voix, le dépôt d'un texte.",
        duree='6 minutes')

    d.titre(surtitre="ANNEXE  ·  LE TÉLÉPHONE",
            notes="Annexe. Elle sert surtout devant une direction qui connaît son "
                  "public : demander d'abord combien de leurs élèves ont un ordinateur "
                  "chez eux, et laisser la salle répondre.")

    d.regle("Ce qui a été refait, et ce qui ne l'a pas été",
            "Rien n'est rapetissé pour faire entrer plus de choses.",
            precision="Le texte garde ses 17 pixels, les boutons leurs 44. Ce qui "
                      "change, c'est la disposition : les colonnes s'empilent, le banc "
                      "de réponses vient sous le pouce, et le glisser-déposer se fait "
                      "au doigt.",
            notes="C'est la diapositive à laisser pendant les questions. Un cours "
                  "illisible sur téléphone n'est pas un cours qu'on donne à moitié : "
                  "c'est un cours que la moitié de la classe ne fait pas.")

    ecran(d, "Entrer", "Le portail de l'élève",
          poser('tel', '01-portail'),
          "Il entre avec son code à six caractères. Le bilan et les modules "
          "s'empilent, dans l'ordre où l'enseignant les a ouverts.",
          notes="Montrer que la première chose visible est « votre prochaine étape » : "
                "l'élève ne choisit pas dans un catalogue, on lui dit où reprendre.")

    ecran(d, "Entrer", "Sa langue, s'il en a besoin",
          poser('tel', '03-langue'),
          "L'élève choisit sa langue une fois. Elle sert à traduire un mot sous le "
          "français — jamais à remplacer le français.",
          notes="Le point qui rassure les enseignants : on n'a pas fait un traducteur. "
                "La traduction s'ajoute sous la phrase, elle ne la remplace pas.")

    # ── Les sept familles ────────────────────────────────────────────
    ecran(d, "Famille 1 sur 7", "Vrai ou faux",
          poser('tel', '07-vrai-faux'),
          "Des tuiles à toucher, larges. La rétroaction porte un mot autant qu'une "
          "couleur : jamais l'information par la couleur seule.",
          notes="Si une seule famille doit être montrée, c'est celle-là : elle dit la "
                "règle d'accessibilité que toutes suivent.")

    ecran(d, "Famille 2 sur 7", "Associer",
          poser('tel', '08-association'),
          "Le banc de réponses devient un bandeau collant, juste au-dessus des "
          "outils. La réponse reste sous le pouce pendant qu'on fait défiler.",
          notes="Le geste : un appui simple suffit — choisir l'étiquette, puis toucher "
                "la case. Le glisser au doigt reste possible, il n'est pas obligatoire.")

    ecran(d, "Famille 3 sur 7", "Des cases à écrire",
          poser('tel', '09-cases-ecrire'),
          "Une case par réponse, avec le clavier du téléphone. La correction "
          "accepte plusieurs formulations, pas une seule chaîne exacte.",
          notes="Précision utile si on la demande : ces cases-là se corrigent sans "
                "aucun modèle. C'est de la comparaison de chaînes.")

    ecran(d, "Famille 4 sur 7", "Un texte à trous",
          poser('tel', '10-texte-a-trous'),
          "La phrase reste entière autour du trou : l'élève lit ce qu'il complète, "
          "il ne remplit pas une grille.",
          notes="Différence avec un exercice papier : le trou est dans une phrase "
                "qu'on vient d'entendre dans le dialogue.")

    ecran(d, "Famille 5 sur 7", "Des images",
          poser('tel', '11-images'),
          "Les images sont produites pour la scène du module — jamais une banque "
          "d'images décorative, et aucun texte dedans.",
          notes="Le « aucun texte dans l'image » est une règle du projet : un modèle "
                "écrit du charabia dès qu'un panneau porte une inscription, et l'élève "
                "le lit comme du français.")

    ecran(d, "Famille 6 sur 7", "Une question ouverte",
          poser('tel', '17-question-ouverte'),
          "L'élève écrit sa réponse. C'est la seule famille qui demande une "
          "relecture — et donc la seule que le mode sans assistance change.",
          notes="Sans assistance, la réponse attendue s'affiche après deux essais. "
                "L'exercice reste faisable, il perd sa relecture.")

    ecran(d, "Famille 7 sur 7", "Un tableau à remplir",
          poser('tel', '18-tableau'),
          "Sur téléphone, le tableau se déplie en rangées empilées : on ne fait "
          "jamais défiler un tableau latéralement.",
          notes="Détail d'artisan, mais c'est celui que les enseignants remarquent : "
                "personne ne remplit un tableau qui déborde de l'écran.")

    # ── Ce qui n'est pas un exercice ─────────────────────────────────
    ecran(d, "Produire", "Sa voix, puis son texte",
          poser('tel', '12-production-orale'),
          "L'élève s'enregistre, se réécoute, recommence autant qu'il veut. Rien "
          "ne part avant qu'il appuie sur envoyer.",
          notes="Insister : la correction est privée, l'envoi est un geste. C'est ce "
                "qui fait qu'un élève ose recommencer douze fois.")

    ecran(d, "Ses outils", "Sept, au bas de l'écran",
          poser('tel', '14-outils'),
          "Traduire, lire, simplifier, prononcer, demander, son carnet, réviser. "
          "Une barre repliable d'un geste.",
          notes="Sur ordinateur c'est un rail vertical à droite ; sur téléphone une "
                "barre en bas. Mêmes sept outils, même code.")

    d.billet("La question à poser à la salle : combien de vos élèves feraient leurs "
             "exercices ce soir, s'il fallait un ordinateur ?",
             exemples=["Les dix-huit captures sont dans le document papier.",
                       "Il tient sur douze pages, en couleur."],
             notes="C'est la question qui transforme « joli » en « utile ». Laisser "
                   "répondre avant d'enchaîner.")

    return d.save(dossier)
