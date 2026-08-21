# -*- coding: utf-8 -*-
"""D2 · Le futur simple et les phrases impersonnelles.
Bloc D « Défi 3 · Le bail » · couleur ambre · 75 min.
Source : exercices `t3futur`, `t3impersonnel` et `t3lettre`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre="La langue des documents",
        chapeau="« Le bail se terminera le 30 juin. » « Il est interdit "
                "d'installer un barbecue. » Deux tournures, et un contrat "
                "devient lisible.",
        duree='75 minutes')

    d.titre(notes="Séance de grammaire, la dernière avant les productions. Elle réunit "
                  "deux savoirs du niveau 5 parce qu'ils vivent au même endroit : dans un "
                  "document officiel.")

    d.objectifs([
        "former le futur simple des verbes courants ;",
        "mettre le futur après « quand » ;",
        "comprendre les phrases impersonnelles d'un bail ;",
        "choisir entre « de » et « que » après « c'est + adjectif ».",
    ])

    d.declencheur(
        'Lecture', "Qu'est-ce que ces trois phrases ont en commun ?",
        pistes=[
            "« Le bail se terminera le 30 juin. »",
            "« Il est interdit d'installer un barbecue sur le balcon. »",
            "« Il revient au locataire de payer l'électricité. »",
            "Qui fait l'action, dans la deuxième et la troisième ?",
        ],
        notes="Réponse attendue : personne n'est nommé. C'est la marque des documents — la "
              "règle vaut pour tout le monde, alors le sujet reste vide. Faire chercher la "
              "même chose dans les baux apportés en classe.")

    d.regle("Le futur simple : l'infinitif + les terminaisons d'avoir",
            "parler → je parlerai, tu parleras, il parlera, nous parlerons, vous parlerez, "
            "ils parleront.",
            precision="Ces six terminaisons sont celles du verbe avoir au présent, et elles "
                      "ne changent jamais, pour aucun verbe de la langue. Les verbes en "
                      "-re perdent seulement leur e final : prendre → je prendrai.",
            notes="Diapositive à photographier. Faire remarquer qu'il y a toujours un r "
                  "avant la terminaison : c'est la marque du futur, et un outil de "
                  "vérification.")

    d.tableau('Sept radicaux irréguliers', "Les terminaisons, elles, ne bougent pas",
              ['Le verbe', 'Le futur'],
              [["être", "je serai"],
               ["avoir", "j'aurai"],
               ["aller", "j'irai"],
               ["faire", "je ferai"],
               ["venir", "je viendrai"],
               ["pouvoir", "je pourrai"],
               ["devoir", "je devrai"]],
              cle=0,
              note="Tous finissent par un r. C'est la marque du futur, sans exception.",
              notes="Diapositive à photographier. Sept formes à apprendre par cœur : c'est "
                    "peu, et elles couvrent l'essentiel de ce qu'on lit dans un bail.")

    d.piege("Le présent après « quand »",
            "Quand vous signez, vous recevrez une copie.",
            "Quand vous signerez, vous recevrez une copie.",
            "En français, les deux verbes vont au futur. Beaucoup de langues mettent le "
            "présent dans la première moitié de la phrase, et c'est une des erreurs les "
            "plus tenaces à ce niveau.",
            notes="Vaut aussi pour « dès que » et « aussitôt que ». Faire produire trois "
                  "phrases avec « quand » avant de passer à la suite.")

    d.pratique('Futur', "Écrivez le verbe au futur simple",
               "Le verbe est entre parenthèses.", [
        ("Le bail … (se terminer) le trente juin.", "se terminera"),
        ("Ensuite, il … (se renouveler) aux mêmes conditions.", "se renouvellera"),
        ("Vous … (recevoir) une copie signée du bail.", "recevrez"),
        ("Si vous refusez, le Tribunal … (fixer) le loyer.", "fixera"),
        ("Je vous … (envoyer) l'avis par écrit.", "enverrai"),
        ("Nous … (être) là le premier juillet.", "serons"),
        ("Elle … (avoir) dix jours pour demander une révision.", "aura"),
        ("Quand vous … (signer), vous recevrez une copie.", "signerez"),
    ], corrige=True,
       notes="La dernière ligne rejoue le piège. La garder pour la fin et la faire "
             "commenter.")

    d.regle("Un « il » ou un « ce » qui ne désigne personne",
            "« Il faut aviser le propriétaire. » — ce « il » ne remplace rien du tout.",
            precision="Il occupe la place du sujet parce que le français en exige un, et "
                      "c'est tout. C'est la tournure des règlements et des contrats : la "
                      "règle vaut pour tout le monde, alors le sujet reste vide. Chercher "
                      "qui est « il », c'est ne plus comprendre la phrase.",
            notes="Diapositive à photographier. Question fréquente et légitime : « il, "
                  "qui ? » La réponse est : personne. Le dire clairement.")

    d.tableau('De ou que ?', "Regardez ce qui suit",
              ['Ce qui suit', 'Le mot'],
              [["un infinitif", "DE — c'est obligatoire de remettre une copie"],
               ["un sujet et un verbe conjugué", "QUE — c'est important que vous répondiez"],
               ["devant une voyelle", "D' — il est interdit d'installer un barbecue"],
               ["une déclaration", "QUE — il est entendu que le stationnement est inclus"]],
              cle=0,
              note="À l'oral d'ici, le « il » de « il faut » tombe souvent : « Faut répondre avant la fin du mois. »",
              notes="Diapositive à photographier. La note du bas est un savoir du niveau 5 "
                    "— la chute du sujet impersonnel avec falloir. Correct à l'oral, à "
                    "éviter dans une lettre.")

    d.pratique('Application', "de, d' ou que ?",
               "Complétez chaque phrase de bail.", [
        ("C'est obligatoire … remettre une copie du bail.", "de"),
        ("C'est important … vous répondiez dans le mois.", "que"),
        ("Il est interdit … installer un barbecue sur le balcon.", "d'"),
        ("Il est entendu … le stationnement est inclus.", "que"),
        ("C'est plus prudent … écrire que de téléphoner.", "d'"),
        ("Il revient au locataire … payer l'électricité.", "de"),
    ], corrige=True,
       notes="Faire dire à chaque fois ce qui suit : un infinitif ou un sujet. Le "
             "raisonnement est le même que pour « ce que / ce qui » et pour les relatifs.")

    d.pratique('Écriture', "La lettre de réponse au propriétaire",
               "Complétez la lettre de Nadège, qui refuse la hausse et le retrait du "
               "stationnement.", [
        ("La date", "Sherbrooke, le 12 février 2026"),
        ("L'objet", "Réponse à votre avis de modification du bail"),
        ("Le refus", "Je refuse l'augmentation de loyer que vous proposez."),
        ("Le second refus", "Je refuse également le retrait de la case de stationnement."),
        ("La suite", "Il vous appartient de vous adresser au Tribunal administratif du logement."),
        ("La salutation", "Veuillez recevoir, Madame, mes salutations distinguées."),
    ], corrige=True,
       notes="Reprise de la séance A4, cette fois avec la grammaire en main. Faire relever "
             "la tournure impersonnelle de l'avant-dernière ligne : « il vous appartient "
             "de ».")

    d.billet(
        "Écrivez quatre phrases sur votre logement dans un an.",
        exemples=[
            "« Mon bail se terminera… », « Je devrai… », « Je pourrai… »",
            "Employez au moins un futur irrégulier.",
        ],
        notes="Devoir d'écriture. Il prépare la production écrite du bloc E et fait "
              "réemployer les sept radicaux irréguliers dans un contexte personnel.")

    return d.save(dossier)
