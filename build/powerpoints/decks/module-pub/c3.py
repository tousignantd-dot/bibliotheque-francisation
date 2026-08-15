# -*- coding: utf-8 -*-
"""C3 · La négation au passé composé.
Bloc C · couleur ambre (écriture) · 60 min.
Source : exercice `t2negatif` et sa mini-leçon.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C3', section='ambre',
        titre='La négation au passé composé',
        chapeau="« Je n'ai pas entendu la capsule. » Les deux morceaux de la négation "
                "encadrent l'auxiliaire, pas le participe. Une question de place, et "
                "elle décide de toute la phrase.",
        duree='60 minutes')

    d.titre(notes="Écrire « je n'ai pas entendu » et « je n'ai entendu pas » au tableau. "
                  "Demander laquelle est correcte. Beaucoup hésiteront.")

    d.objectifs([
        "placer ne et pas autour de l'auxiliaire ;",
        "écrire n' devant une voyelle ;",
        "employer la négation avec avoir et avec être ;",
        "accorder le participe passé malgré la négation.",
    ])

    d.regle('La règle',
            "Ne et pas encadrent l'auxiliaire, jamais le participe.",
            precision="« Je n'ai pas entendu. » « Ils ne sont pas arrivés. » Le verbe "
                      "conjugué du passé composé, c'est l'auxiliaire : c'est donc lui "
                      "que la négation entoure. Le participe reste après, intact.",
            notes="Écrire la règle au tableau avec l'auxiliaire encadré par deux traits. "
                  "L'image visuelle vaut mieux que l'explication.")

    d.tableau('Analyse', "La place des trois morceaux",
              ['Sujet', 'Ne', 'Auxiliaire', 'Pas', 'Participe'],
              [["je", "n'", "ai", "pas", "entendu"],
               ["nous", "n'", "avons", "pas", "annoncé"],
               ["tu", "n'", "as", "pas", "gardé"],
               ["ils", "ne", "sont", "pas", "arrivés"]],
              cle=2,
              note="L'ordre ne change jamais. Seul l'auxiliaire varie, et « ne » devient "
                   "« n' » devant une voyelle.",
              notes="Faire lire le tableau colonne par colonne. La régularité est totale, "
                    "et c'est ce qui rend la règle facile.")

    d.cartes('En apprendre plus', "Quatre choses à savoir en plus", [
        ("« Ne » devient « n' »",
         "Devant ai, as, a, avons, avez, ont, est, êtes : toutes des voyelles. Seul "
         "« ne sont » et « ne suis » gardent le e."),
        ("L'accord se fait quand même",
         "« Elles ne sont pas arrivées » — le participe s'accorde comme d'habitude. La "
         "négation ne change rien à l'accord."),
        ("Avec un pronom complément",
         "« Je ne l'ai pas entendue. » Le pronom se glisse entre « ne » et "
         "l'auxiliaire. L'ordre reste : ne, pronom, auxiliaire, pas, participe."),
        ("« Ne… jamais », « ne… plus »",
         "Même construction : « je n'ai jamais entendu », « il n'est plus venu ». Seul "
         "le second mot change."),
    ], notes="La troisième carte est la plus difficile. La montrer sans l'exiger : elle "
             "apparaîtra en lecture bien avant d'être produite.")

    d.pratique('Pratique · 1 de 4', "Mettez à la forme négative",
               "Ne et pas autour de l'auxiliaire.", [
        ("J'ai entendu la capsule à la radio.", "Je n'ai pas entendu la capsule à la radio."),
        ("Nous avons annoncé l'atelier dans l'infolettre.",
         "Nous n'avons pas annoncé l'atelier dans l'infolettre."),
        ("Tu as gardé le texte de trente secondes.",
         "Tu n'as pas gardé le texte de trente secondes."),
        ("Les bénévoles sont arrivés avant neuf heures.",
         "Les bénévoles ne sont pas arrivés avant neuf heures."),
        ("Vous êtes venus à la clinique de vélo.",
         "Vous n'êtes pas venus à la clinique de vélo."),
    ], corrige=True,
       notes="Faire souligner l'auxiliaire avant d'ajouter la négation. C'est l'étape qui "
             "évite l'erreur.")

    d.piege("Le piège du participe encadré",
            "Je n'ai entendu pas la capsule.",
            "Je n'ai pas entendu la capsule.",
            "C'est l'auxiliaire qui est encadré, pas le participe. Au passé composé, le "
            "verbe conjugué est « ai », « as », « est » : c'est lui que la négation "
            "entoure. Le participe reste après, sans rien autour.",
            notes="Erreur logique : on entoure ce qu'on croit être le verbe principal. "
                  "Expliquer que l'auxiliaire est le verbe conjugué.")

    d.piege("Le piège du « ne » oublié",
            "J'ai pas entendu la capsule.",
            "Je n'ai pas entendu la capsule.",
            "À l'oral, le « ne » tombe presque toujours : « j'ai pas entendu » s'entend "
            "partout au Québec. À l'écrit, il faut le remettre. C'est la même différence "
            "que pour les consonnes finales du module 6.",
            notes="Le dire sans jugement : l'oral et l'écrit ne suivent pas les mêmes "
                  "règles, et les deux sont corrects dans leur usage.")

    d.pratique('Pratique · 2 de 4', "Ne ou n' ?",
               "L'élision se fait devant une voyelle.", [
        ("Je ___ ai pas entendu.", "n'"),
        ("Ils ___ sont pas arrivés.", "ne"),
        ("Nous ___ avons pas annoncé.", "n'"),
        ("Vous ___ êtes pas venus.", "n'"),
        ("Elle ___ est pas restée.", "n'"),
    ], corrige=True,
       notes="Quatre élisions sur cinq. Faire remarquer que « ne sont » est le seul cas "
             "sans élision dans cet exercice.")

    d.pratique('Pratique · 3 de 4', "Accordez malgré la négation",
               "Le participe s'accorde comme d'habitude avec être.", [
        ("Les bénévoles ne sont pas (arriver) ___.", "arrivés"),
        ("Solange n'est pas (venir) ___ à l'atelier.", "venue"),
        ("Elles ne sont pas (rester) ___ jusqu'à la fin.", "restées"),
        ("Nous n'avons pas (annoncer) ___ l'atelier.", "annoncé — pas d'accord avec avoir"),
    ], corrige=True,
       notes="Le quatrième item rappelle que l'auxiliaire avoir n'accorde pas. La "
             "négation n'y change rien.")

    d.pratique('Pratique · 4 de 4', "Écrivez le bilan de la campagne",
               "Quatre phrases négatives sur ce qui n'a pas été fait.", [
        ("L'infolettre", "Nous n'avons pas annoncé l'atelier dans l'infolettre."),
        ("La radio", "La capsule n'est pas passée à l'heure prévue."),
        ("Les affiches", "Nous n'avons pas posé d'affiche au dépanneur."),
        ("Les bénévoles", "Deux bénévoles ne sont pas venus samedi."),
    ], corrige=True,
       notes="Faire remarquer la deuxième phrase : « n'est pas passée » avec accord. "
             "C'est la synthèse des deux règles.")

    d.billet(
        "Écrivez trois phrases négatives au passé composé.",
        exemples=[
            "Une avec avoir, une avec être, une avec « ne… jamais ».",
            "Soulignez l'auxiliaire dans chacune.",
        ],
        notes="Corriger la place de la négation avant l'accord. C'est le savoir de la "
              "séance.")

    return d.save(dossier)
