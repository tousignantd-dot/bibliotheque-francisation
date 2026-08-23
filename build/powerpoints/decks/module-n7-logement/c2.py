# -*- coding: utf-8 -*-
"""C2 · Qui fait quoi, et quoi leur demander
Bloc C « Défi 2 · La visite avec la courtière » · couleur teal · écoute et
réponds · 75 min.
Source : exercices `t2qui` et `t2prec` et leurs mini-leçons.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='C2', section='teal',
        titre="Qui fait quoi, et quoi leur demander",
        chapeau="Six personnes interviennent dans un achat. Toutes sont "
                "compétentes, aucune n'a le même intérêt que vous — et la "
                "réponse change les questions que vous devez poser.",
        duree='75 minutes')

    d.titre(notes="Séance orale. Reprendre les billets de C1 : les questions écrites "
                  "par le groupe serviront à l'exercice de tri, ce qui vaut mieux que "
                  "des exemples inventés par l'enseignante.")

    d.objectifs([
        "nommer six intervenants et dire pour qui chacun travaille ;",
        "distinguer une question précise d'une question vague ;",
        "poser une question qui appelle un chiffre, une date ou un document ;",
        "accepter « je ne sais pas, je vérifie » comme une bonne réponse.",
    ], notes="Le quatrième objectif est un objectif d'attitude, et il compte autant "
             "que les autres : c'est lui qui empêche de se contenter d'une impression.")

    d.tableau('Analyse', "Six personnes, six rôles",
              ['La personne', 'Ce quelle fait, et pour qui'],
              [["le courtier du vendeur", "il fait vendre ; il vous doit un traitement équitable"],
               ["le courtier de l'acheteur", "il cherche pour vous et discute le prix à votre place"],
               ["l'inspecteur en bâtiment", "il examine et vous remet un rapport écrit"],
               ["la conseillère hypothécaire", "elle établit ce que vous pouvez emprunter"],
               ["le notaire", "il vérifie les titres et reçoit l'acte de vente"]],
              cle=0,
              notes="Diapositive à photographier. Le syndicat de copropriété manque à "
                    "ce tableau faute de place : il vient dans les cartes suivantes.")

    d.cartes('Analyse', "Deux choses qui surprennent", [
        ("Le courtier du vendeur ne vous représente pas", "Il est lié par un contrat de courtage avec le vendeur et défend ses intérêts. Il doit néanmoins traiter équitablement l'acheteur non représenté et lui communiquer l'information de façon objective."),
        ("Il ne peut rien vous réclamer", "Sa rétribution est fixée dans le contrat signé par le vendeur. Dans la plupart des transactions résidentielles, avoir son propre courtier ne coûte donc rien de plus à l'acheteur."),
        ("Le syndicat de copropriété", "Il administre les parties communes, tient le fonds de prévoyance et fait faire les travaux. C'est à lui — par ses procès-verbaux — qu'on demande l'état du fonds."),
        ("La bonne question, en dix mots", "« Avec qui avez-vous un contrat, dans cette transaction ? » Elle se pose sans agressivité, et elle règle tout le reste."),
    ], notes="Faire poser la question de la quatrième carte à voix haute par plusieurs "
             "élèves, jusqu'à ce que le ton soit neutre. C'est un exercice de prosodie "
             "autant que de vocabulaire.")

    d.regle("Une question utile appelle un chiffre, une date ou un document",
            "Ce sont les trois seules réponses qu'on ne peut pas remplacer par « ça dépend ».",
            precision="« Est-ce que c'est un bon immeuble ? » n'a aucune réponse "
                      "vérifiable, et elle est posée à quelqu'un qui vend. « Quels "
                      "travaux majeurs ont été faits depuis dix ans ? » porte sur la "
                      "même curiosité et obtient une réponse qu'on peut noter. Les six "
                      "questions se préparent la veille, par écrit : sur place, on "
                      "regarde les armoires et on oublie le fonds de prévoyance.",
            notes="Diapositive à photographier. Faire écrire les six questions dans le "
                  "carnet, en fin de séance, comme une liste à emporter.")

    d.pratique('Écoute et réponds', "Question précise ou question vague ?",
               "Pour chacune, dites laquelle des deux, et pourquoi.", [
        ("Combien y a-t-il actuellement dans le fonds de prévoyance ?", "précise - un chiffre"),
        ("Est-ce que c'est un bon immeuble ?", "vague - une opinion, et au vendeur"),
        ("En quelle année le toit a-t-il été refait ?", "précise - une date"),
        ("Est-ce que les voisins sont tranquilles ?", "vague - invérifiable"),
        ("Pouvez-vous me remettre le procès-verbal de la dernière assemblée ?", "précise - un document"),
        ("Pensez-vous que je devrais faire une offre ?", "vague - la mauvaise personne"),
    ], corrige=True,
       notes="Six des huit items de `t2prec`. Pour chaque question vague, demander au "
             "groupe de la reformuler en question précise : c'est le vrai exercice.")

    d.pratique('Écoute et réponds', "À qui poser cette question ?",
               "Nommez la personne, puis dites pourquoi elle est la bonne.", [
        ("Quels sont les trois points les plus préoccupants du rapport ?", "l'inspecteur"),
        ("De quel montant serait mon paiement mensuel, tout compris ?", "la conseillère"),
        ("Y a-t-il quelque chose d'inhabituel dans les titres ?", "le notaire"),
        ("Une cotisation spéciale est-elle prévue cette année ?", "le syndicat"),
        ("Depuis combien de jours la propriété est-elle affichée ?", "le courtier du vendeur"),
    ], corrige=True,
       notes="Les cinq réponses viennent de l'exercice `t2qui`. Faire remarquer que la "
             "dernière question est parfaitement légitime à poser au courtier du "
             "vendeur : elle porte sur un fait, pas sur un avis.")

    d.billet(
        "Écris les trois questions que tu poserais en premier, dans l'ordre.",
        exemples=[
            "Chacune doit appeler un chiffre, une date ou un document.",
            "Trois lignes.",
        ],
        notes="Trois minutes. Cette liste est le livrable de la séance ; la faire "
              "recopier au propre dans le carnet avant de sortir.")

    return d.save(dossier)
