# -*- coding: utf-8 -*-
"""C4 · Concéder, puis avancer
Bloc C « Défi 2 · Faire valoir sa réclamation » · couleur ambre · 75 min.
Écriture. Source du module : l'exercice `t2conc` et la mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C4', section='ambre',
        titre="Concéder, puis avancer",
        chapeau="Toute l'argumentation du module tient dans un mouvement à "
                "deux temps : on reconnaît ce qui est vrai chez l'autre, "
                "puis on pose ce qui est vrai chez soi.",
        duree='75 minutes')

    d.titre(notes="Le programme du niveau 8 consacre vingt et un points de "
                  "savoir aux connecteurs. Ceux de cette séance sont "
                  "sélectionnés sur un seul critère : servent-ils à soutenir "
                  "un discours devant quelqu'un qui décide ?")

    d.objectifs([
        "construire une concession en deux temps, sans réserve ;",
        "choisir le mode après « bien que » et après « même si » ;",
        "employer « or » pour introduire le fait qui décide ;",
        "annoncer ses arguments avant de les donner.",
    ], notes="« Or » est le mot le plus utile de la séance et le moins "
             "employé par les élèves. Y consacrer un quart du temps.")

    d.declencheur(
        'Pour commencer', "Quelqu'un vous dit : « vous avez signé le "
                          "contrat ». Que répondez-vous ?",
        pistes=[
            "« Non, pas vraiment » — que se passe-t-il ensuite ?",
            "« Oui, c'est vrai, mais… » — et ensuite ?",
            "Laquelle des deux réponses fait gagner du temps ?",
        ],
        notes="Faire mesurer le coût de la première : l'autre va passer cinq "
              "minutes à prouver un point que la seconde règle en trois "
              "secondes.")

    d.regle("Concéder franchement, puis retourner",
            "Certes la clause existe, et je ne prétends pas le contraire. Or elle parle du transport, et le meuble a été fendu dans l'escalier.",
            precision="Une concession à moitié faite ne compte pas : « c'est "
                      "peut-être vrai, mais » n'est pas une concession, c'est "
                      "une contestation déguisée.",
            notes="Diapositive à photographier. Faire répéter la phrase "
                  "entière à voix haute, avec la mélodie descendante de la "
                  "séance A2 sur la seconde moitié.")

    d.tableau('Analyse', "Les connecteurs, rangés par registre",
              ['Le connecteur', 'Où il vit'],
              [["je vous l'accorde · c'est vrai", "parlé, chaleureux, efficace au téléphone"],
               ["certes · il est vrai que", "écrit et parlé soutenu, la valeur sûre"],
               ["bien que · quoique (+ subjonctif)", "écrit, et il se suffit à lui-même"],
               ["en revanche · par contre", "oppose deux choses distinctes"],
               ["il n'en demeure pas moins que", "le plus formel : une fois par lettre, jamais deux"]],
              cle=0,
              note="En écrit d'affaires québécois, « en revanche » est attendu là où « par contre » passe à l'oral.",
              notes="Diapositive à photographier. Faire choisir deux "
                    "connecteurs par personne : on n'en emploie jamais plus "
                    "dans une même conversation.")

    d.cartes('Analyse', "« Or », le mot qui fait tourner un raisonnement", [
        ("Ce qu'il n'est pas", "« or » n'oppose pas deux opinions."),
        ("Ce qu'il fait", "il introduit le fait qui rend la conclusion inévitable."),
        ("Le raisonnement complet", "La clause vise le transport. Or le meuble a été fendu dans l'escalier. Donc elle ne s'applique pas."),
        ("Sa limite", "une fois par raisonnement. Deux « or » et le lecteur ne sait plus lequel porte la conclusion."),
    ], cols=2,
       notes="Il n'existe pas d'équivalent parlé exact : au téléphone, on dit "
             "« et justement », ou on marque un temps. Le préciser, sinon les "
             "élèves l'emploient à l'oral et ça sonne écrit.")

    d.piege('Attention',
            "« Bien que la clause soit claire, mais elle vise le transport. »",
            "« Bien que la clause soit claire, elle vise le transport. »",
            "« Bien que » porte déjà l'opposition. Y ajouter « mais » double "
            "le connecteur et alourdit la phrase sans rien apporter. Même "
            "vigilance avec « malgré », qui se fait suivre d'un nom : "
            "« malgré l'existence de cette clause », jamais « malgré que ».",
            notes="Faire corriger trois phrases doublées, à l'oral. L'erreur "
                  "est très fréquente chez les élèves qui maîtrisent bien "
                  "« mais » et découvrent « bien que ».")

    d.pratique('Pratique', "Complétez avec le connecteur qui convient",
               "certes · bien que · même si · or · en revanche", [
        ("___ la clause existe ; mais elle vise le transport.", "Certes"),
        ("___ la clause soit claire, elle ne recouvre pas le portage.", "Bien que"),
        ("___ la clause est claire, elle ne recouvre pas le portage.", "Même si"),
        ("La clause vise le transport. ___, le meuble a été fendu dans l'escalier.", "Or"),
        ("J'accepte le refus sur la rampe ; ___, je conteste celui du vaisselier.", "en revanche"),
        ("___ l'existence de cette clause, la garde était au transporteur.", "Malgré"),
    ], corrige=True, cols=1,
       notes="C'est l'exercice `t2conc` du module, dans sa version projetée. "
             "Les deuxième et troisième items sont la même phrase à deux "
             "modes : les corriger l'un après l'autre, sans commentaire "
             "entre les deux.")

    d.billet(
        "Écris ta concession et ton retournement, en deux phrases, avec « or ».",
        exemples=[
            "Première phrase : certes… ou je vous l'accorde…",
            "Deuxième phrase : Or… suivi d'un fait daté, pas d'une opinion.",
        ],
        notes="Cinq minutes. Ramasser : le test est simple, ce qui suit « or » "
              "doit être un fait vérifiable. Si c'est une opinion, le "
              "connecteur est mal employé.")

    return d.save(dossier)
