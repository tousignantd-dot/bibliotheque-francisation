# -*- coding: utf-8 -*-
"""B3 · Ce que je ferai à mon retour
Bloc B « Défi 1 · Prévenir de son absence » · couleur ambre · 75 min.
Source du module : exercice `t1fut` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='B3', section='ambre',
        titre="Ce que je ferai à mon retour",
        chapeau="Quand on annonce qu'on part trois semaines, la première "
                "question de l'autre côté du comptoir n'est pas « pourquoi ? » "
                "mais « et après ? ». Trois phrases au futur, et une absence "
                "devient un plan.",
        duree='75 minutes')

    d.titre(notes="Séance de conjugaison, et elle a un but précis : rassurer un bureau. "
                  "L'annoncer ainsi dès le départ change complètement l'attention du "
                  "groupe — on ne conjugue pas pour conjuguer.")

    d.objectifs([
        "former le futur simple de tous les verbes réguliers ;",
        "employer les six radicaux irréguliers utiles au comptoir ;",
        "choisir entre futur simple et futur proche selon la situation ;",
        "distinguer « je voudrais » de « je voudrai » à l'oreille et à l'écrit.",
    ], notes="Le quatrième objectif fait le lien avec A2. Le rappeler : c'est le même "
             "point vu deux fois, une fois par l'oreille et une fois par la grammaire, "
             "et c'est ce qui le fait tenir.")

    d.regle("Une seule série de terminaisons",
            "On les colle à l'infinitif, et elles ne changent jamais : "
            "-ai, -as, -a, -ons, -ez, -ont.",
            precision="Le son du futur, c'est le « r » suivi d'un « é » fermé. "
                      "Quand vous ne l'entendez pas, ce n'est pas un futur.",
            notes="Diapositive à photographier. La remarque sur le « r » est ce qui "
                  "permet de corriger à l'oreille sans ouvrir un tableau de conjugaison.")

    d.cartes("Les six radicaux irréguliers", "Six mots, pas six règles", [
        ("être · avoir",
         "je serai · j'aurai"),
        ("aller · faire",
         "j'irai · je ferai"),
        ("venir · revenir",
         "je viendrai · je reviendrai"),
        ("pouvoir · recevoir",
         "je pourrai · vous recevrez"),
    ], notes="Ce sont exactement les six dont on se sert au comptoir. Les faire répéter "
             "en série, à voix haute, puis les faire réemployer dans une phrase du "
             "module. Ne pas en ajouter d'autres : la liste courte est ce qui la rend "
             "apprenable.")

    d.pratique('Conjugaison', "Mettez au futur simple",
               "À l'oral d'abord, puis à l'écrit.", [
        ("Je ___ (revenir) en classe le 30 mars.", "reviendrai"),
        ("Je vous ___ (apporter) la pièce justificative.", "apporterai"),
        ("Je ___ (être) absente du 9 au 27 mars.", "serai"),
        ("Je ___ (faire) le rattrapage du midi.", "ferai"),
        ("Vous ___ (recevoir) ma demande avant vendredi.", "recevrez"),
        ("Je ___ (pouvoir) reprendre les évaluations en avril.", "pourrai"),
    ], corrige=True,
       notes="Faire dire la phrase entière. La troisième oppose « je serai » à « je "
             "saurai » : le groupe les confond régulièrement, et ce n'est pas la même "
             "annonce du tout.")

    d.tableau('Deux futurs, deux endroits', "Ce qui se dit, ce qui s'écrit",
              ['Entre camarades', 'Au comptoir et par écrit'],
              [["Je vais revenir lundi.", "Je reviendrai le 30 mars."],
               ["Je vais m'inscrire au rattrapage.", "Je m'inscrirai au rattrapage."],
               ["Ça va prendre combien de temps ?",
                "Je voudrais savoir combien de temps cela prendra."],
               ["On va se rappeler.", "Je vous rappellerai la semaine prochaine."]],
              cle=1,
              notes="Aucune des deux colonnes n'est fautive. Ce qui change, c'est le "
                    "registre. Insister sur la tenue : dans une lettre, on choisit le "
                    "futur simple et on le garde du début à la fin.")

    d.piege("Confondre « je voudrais » et « je voudrai »",
            "Je voudrai savoir si je garde ma place.",
            "Je voudrais savoir si je garde ma place.",
            "Le premier annonce ce que vous voudrez la semaine prochaine, ce qui n'a "
            "aucun sens au comptoir. Le second demande poliment, maintenant — et il "
            "se dit avec un « è » ouvert, comme en A2.",
            notes="Faire dire les deux phrases à voix haute par deux élèves différents, "
                  "les yeux fermés pour le reste du groupe. La différence s'entend, et "
                  "c'est ce qui la rend mémorable.")

    d.pratique('Production', "Trois promesses, à votre tour",
               "Chacun écrit trois phrases au futur pour sa propre absence.", [
        ("Une phrase sur la date de retour.", "je reviendrai le..."),
        ("Une phrase sur ce que vous apporterez.", "je vous apporterai..."),
        ("Une phrase sur le rattrapage.", "je m'inscrirai... je ferai..."),
        ("Une quatrième, libre, avec un des six irréguliers.", "je serai, j'irai, je pourrai"),
    ], corrige=False,
       notes="Passer dans les rangées. L'erreur la plus fréquente est l'oubli du « r » "
             "des verbes en -re : « je remettai ». La corriger à l'oral, en faisant "
             "entendre la forme juste plutôt qu'en l'écrivant.")

    d.regle("Le futur, c'est une promesse",
            "Il ne décore pas la phrase : il engage la personne qui parle.",
            precision="C'est pour ça qu'un bureau garde une place. Pas à cause du "
                      "motif — à cause du plan de retour.",
            notes="Diapositive à photographier. Elle referme le lien entre la grammaire "
                  "et la situation, et elle revient en E1 : le message vocal se termine "
                  "toujours par ce que la personne fera.")

    d.billet(
        "Écrivez la phrase de retour que vous direz au comptoir, au futur simple.",
        exemples=[
            "Une date précise, pas « bientôt ».",
            "Ajoutez ce que vous apporterez en revenant.",
        ],
        notes="Ramasser les billets. Ils se joignent à ceux de B1 et de B2 : les trois "
              "ensemble forment déjà l'annonce complète qu'on assemblera en B4.")

    return d.save(dossier)
