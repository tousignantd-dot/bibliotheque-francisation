# -*- coding: utf-8 -*-
"""C3 · « de », « à », ou rien.
Bloc C « Défi 2 · La demande » · couleur teal · 60 min.
Source : exercice `t2inf`, mini-leçon du même nom.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='teal',
        titre="« de », « à », ou rien",
        chapeau="« Je souhaite travailler », « je suis prête à apprendre », "
                "« j'accepte de commencer ». Trois constructions, et ce n'est "
                "pas le sens qui décide : c'est le verbe.",
        duree='60 minutes')

    d.titre(notes="Séance courte en explication, longue en répétition. Il n'y a rien à "
                  "comprendre : il y a trois listes à installer.")

    d.objectifs([
        "savoir que le verbe de départ décide du mot qui suit ;",
        "connaître les verbes qui demandent « de » ;",
        "connaître ceux qui demandent « à » ;",
        "connaître ceux qui ne demandent rien.",
    ])

    d.declencheur(
        'Observation', "Trois phrases de lettre de motivation.",
        pistes=[
            "« Je souhaite travailler chez vous. »",
            "« Je suis prête à apprendre votre logiciel. »",
            "« J'accepte de travailler le samedi. »",
            "Pourquoi trois constructions différentes ?",
        ],
        notes="Laisser chercher une logique de sens : le groupe n'en trouvera pas, et "
              "c'est exactement le point. La réponse est que le verbe porte son mot.")

    d.tableau('Les trois groupes', "Le verbe décide, pas le sens",
              ['Le mot qui suit', 'Les verbes'],
              [["de", "accepter · décider · essayer · oublier · refuser · demander · permettre"],
               ["à", "apprendre · commencer · continuer · hésiter · réussir · être prêt"],
               ["rien", "aimer · devoir · espérer · pouvoir · savoir · souhaiter · vouloir"]],
              cle=0,
              note="Devant une voyelle, « de » devient « d' » : j'essaie d'arriver tôt.",
              notes="Diapositive à photographier. Faire recopier les trois listes : "
                    "c'est de la mémorisation, et elle se fait par l'écriture.")

    d.regle("Les trois verbes de la lettre",
            "Souhaiter · être prêt à · vous demander de.",
            precision="Toute lettre de motivation ordinaire emploie ces trois-là : « Je "
                      "souhaite occuper le poste de… », « Je suis prête à commencer "
                      "dès… », « Je vous demande de bien vouloir examiner ma "
                      "candidature. » Trois formules apprises par cœur suffisent à "
                      "écrire la lettre du bloc C.",
            notes="Diapositive à photographier. Ces trois phrases seront réutilisées "
                  "telles quelles en C4.")

    d.pratique('Application', "de, à, ou rien ?",
               "Complétez. Certaines lignes ne prennent rien du tout.", [
        ("Je souhaite ___ travailler à temps plein.", "rien"),
        ("Je suis prête ___ apprendre votre logiciel.", "à"),
        ("Je vous demande ___ bien vouloir examiner ma candidature.", "de"),
        ("J'accepte ___ travailler un samedi sur deux.", "de"),
        ("J'ai commencé ___ suivre des cours en 2024.", "à"),
        ("Je peux ___ commencer dès le mois prochain.", "rien"),
    ], corrige=True,
       notes="Faire dire à voix haute le verbe de départ avant de répondre : c'est lui "
             "qui donne la réponse, jamais la suite de la phrase.")

    d.piege("« Je souhaite de travailler »",
            "Je souhaite de travailler chez vous.",
            "Je souhaite travailler chez vous.",
            "Souhaiter, vouloir, désirer, espérer, pouvoir, devoir et savoir ne prennent "
            "rien. C'est la faute la plus fréquente des lettres de motivation, et elle "
            "apparaît dès la première phrase — là où l'employeur est le plus attentif.",
            notes="Corriger cette faute-là en priorité absolue. Elle coûte plus cher que "
                  "n'importe quelle autre du module, parce qu'elle est en tête de lettre.")

    d.pratique('Rédaction', "Trois phrases pour votre lettre",
               "Écrivez-les avec le poste que vous visez.", [
        ("Avec « souhaiter »", "Je souhaite occuper le poste de…"),
        ("Avec « être prêt à »", "Je suis prêt(e) à…"),
        ("Avec « vous demander de »", "Je vous demande de bien vouloir…"),
    ], corrige=True,
       notes="Ramasser les trois phrases : ce sont les fondations de la lettre écrite "
             "en C4. Corriger les « de » en trop avant la séance suivante.")

    d.billet(
        "Apprenez les trois listes par cœur.",
        exemples=[
            "Sept verbes en « de », six en « à », sept sans rien.",
            "Le test : dites la phrase à voix haute. Si elle sonne mal, vérifiez la liste.",
        ],
        notes="Un devoir de mémorisation pure, assumé comme tel. Il n'y a pas d'autre "
              "chemin pour ce point de langue.")

    return d.save(dossier)
