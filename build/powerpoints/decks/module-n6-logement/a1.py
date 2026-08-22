# -*- coding: utf-8 -*-
"""A1 · Six mois ailleurs
Bloc A « Je découvre » · couleur acier · 75 min. Séance d'ouverture.
Source : dialogue `prep`, exercice `prVF`, six premiers mots de FC_CARDS.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='A1', section='acier',
        titre="Six mois ailleurs",
        chapeau="Un contrat de six mois à l'autre bout de la province, et un "
                "logement qu'on ne veut pas perdre. Tout le module tient dans "
                "ce nœud-là.",
        duree='75 minutes')

    d.titre(notes="Première séance du module. Ouvrir par une question au groupe : "
                  "combien de temps avez-vous mis à trouver votre logement ? "
                  "Presque tout le monde a une histoire, et elle est longue. "
                  "C'est ce qui rend la suite évidente.")

    d.objectifs([
        "comprendre pourquoi on peut vouloir garder un logement qu'on "
        "n'habite pas ;",
        "distinguer sous-louer, céder son bail et résilier ;",
        "nommer les six mots du contrat, avec leur article ;",
        "savoir où chercher une règle avant d'en parler à quelqu'un.",
    ], notes="Le quatrième objectif est celui du module entier. Le dire tout de "
             "suite : ici, on n'apprend pas à se défendre, on apprend à se "
             "renseigner avant de parler.")

    d.declencheur(
        'Observation', "Que feriez-vous de votre logement si vous deviez partir six mois ?",
        pistes=[
            "Combien de temps avez-vous cherché votre logement actuel ?",
            "Qu'est-ce que ça coûterait de le retrouver aujourd'hui ?",
            "Connaissez-vous quelqu'un qui a prêté son logement ?",
            "À qui poseriez-vous la question en premier ?",
        ],
        notes="Question sans mauvaise réponse. Laisser venir les récits : plusieurs "
              "élèves ont déjà sous-loué sans le savoir, ou ont hébergé quelqu'un. "
              "Noter au tableau les mots qu'ils emploient — ils reviendront corrigés "
              "en A2.")

    d.dialogue('Dialogue · 1 de 3', "Le contrat, et le problème", [
        ("FARIDA", "On m'offre un remplacement de six mois à Sept-Îles. Du six janvier au trente juin. Après, je reviens ici.", True),
        ("GILLES", "Six mois, ce n'est pas rien. C'est payé combien de plus ?", True),
        ("FARIDA", "Trois dollars de l'heure, et le logement est fourni là-bas. C'est justement ça, mon problème : le logement.", True),
        ("GILLES", "Tu as ton quatre et demie sur la Canardière, si je me souviens bien.", True),
    ], consigne="Écouter d'abord, diapositive masquée.",
       notes="Faire ressortir le paradoxe : elle a un logement de trop, pas un de "
             "moins. Beaucoup d'élèves n'ont jamais entendu poser le problème dans "
             "ce sens-là.")

    d.dialogue('Dialogue · 2 de 3', "Pourquoi elle ne veut pas le lâcher", [
        ("FARIDA", "Huit cent quatre-vingt-quinze piastres par mois, chauffé, deux minutes de l'autobus. Tu sais ce que ça coûterait de retrouver ça en juillet ?", True),
        ("GILLES", "Je le sais trop bien. Ma fille cherche depuis le mois de mars et elle n'a rien trouvé sous mille deux cents.", True),
        ("FARIDA", "Alors je ne veux pas le lâcher. Mais je ne vais pas payer huit cent quatre-vingt-quinze dollars pendant six mois pour un logement vide.", True),
        ("GILLES", "Non, ça n'a pas de bon sens. Mon cousin avait sous-loué son appartement à un étudiant quand il est parti à Baie-Comeau.", True),
    ], notes="La dernière réplique est au plus-que-parfait : le signaler sans "
             "l'expliquer, il sera travaillé en C4. Ici, on veut seulement que le "
             "mot « sous-loué » soit entendu en contexte.")

    d.dialogue('Dialogue · 3 de 3', "Prêter, ou passer à quelqu'un", [
        ("FARIDA", "Sous-loué. Parce que j'ai entendu parler de céder son bail aussi, et je ne vois pas la différence.", True),
        ("GILLES", "Quand tu cèdes, tu t'en vas pour de bon : le bail continue avec l'autre, et toi tu es sorti du dossier.", True),
        ("FARIDA", "Et quand je sous-loue ?", True),
        ("GILLES", "Tu prêtes pour un temps, mais le bail reste à ton nom. Si l'autre ne paie pas, c'est toi que le propriétaire va voir.", True),
    ], notes="C'est le cœur de la séance. Faire répéter la dernière réplique par deux "
             "élèves. La distinction sera reprise, exercée et corrigée en A2 : ici, "
             "elle est seulement posée.")

    d.tableau('Analyse', "Après, qui est encore au bail ?",
              ['La démarche', 'Ce qui se passe après'],
              [["Sous-louer", "je reste au bail et je reprends mon logement à la date prévue"],
               ["Céder", "l'autre personne prend ma place au bail, et je n'y suis plus"],
               ["Résilier", "le bail s'éteint, dans les cas que la loi permet"]],
              cle=0,
              note="Une seule question suffit à trancher les trois.",
              notes="Diapositive à photographier. C'est le tableau de référence du "
                    "module : il revient en A2, et il sert encore en C1 quand "
                    "monsieur Tardif croit qu'elle résilie.")

    d.regle("Une règle se cherche avant de se discuter",
            "On ne va pas voir son propriétaire les mains vides.",
            precision="Farida ne demande pas la permission : elle lit d'abord ce "
                      "que la loi prévoit, elle téléphone ensuite pour vérifier, "
                      "et elle arrive avec un nom, des dates et un papier. La "
                      "conversation du Défi 2 ne ressemble à rien de ce qu'elle "
                      "aurait été autrement.",
            notes="Diapositive à photographier. Insister : ce n'est pas de la "
                  "méfiance envers le propriétaire, c'est de la préparation. Un "
                  "locateur bien informé préfère, lui aussi, une demande complète.")

    d.vocabulaire('Vocabulaire', "Les six mots du contrat", [
        ("un locateur", "La personne qui loue son logement à quelqu'un d'autre et qui signe le bail de ce côté-là."),
        ("un bail", "Le contrat écrit qui dit qui occupe le logement, pour combien de temps et à quel prix."),
        ("une clause", "Une phrase du contrat qui pose une règle à part, souvent numérotée."),
        ("un avis", "Un papier écrit qu'on remet à l'autre partie pour l'informer officiellement."),
        ("un délai", "Le temps qu'une personne a pour agir avant qu'il soit trop tard."),
        ("la reconduction", "Le fait qu'un bail continue tout seul aux mêmes conditions."),
    ], notes="Faire répéter chaque mot avec son article. « Locateur » étonne "
             "toujours : la plupart disent « propriétaire ». Expliquer que les deux "
             "ne se recouvrent pas — on peut être propriétaire sans louer.")

    d.pratique('Compréhension', "Vrai ou faux ?",
               "Répondez d'après la conversation de Farida et de Gilles.", [
        ("Farida part six mois à Sept-Îles, du six janvier au trente juin.", "vrai"),
        ("Elle veut se débarrasser de son logement.", "faux - elle veut le garder pour juillet"),
        ("Son loyer est de huit cent quatre-vingt-quinze dollars, chauffé.", "vrai"),
        ("Quand on cède son bail, on reste responsable du loyer.", "faux - on sort du dossier"),
        ("Quand on sous-loue, le bail reste au nom du locataire de départ.", "vrai"),
        ("Gilles lui conseille de donner ses clés sans prévenir personne.", "faux - il l'envoie lire le site"),
    ], corrige=True,
       notes="Faire justifier chaque « faux » par la réplique exacte. Le quatrième "
             "énoncé est le seul qui résiste : la confusion entre céder et "
             "sous-louer est la plus répandue, et elle coûte cher dans la vraie vie.")

    d.billet(
        "Sous-louer ou céder : lequel des deux choisiriez-vous, et pourquoi ?",
        exemples=[
            "Deux phrases suffisent.",
            "Pensez à ce que vous voulez qu'il arrive dans six mois.",
        ],
        notes="Deux minutes. Les réponses servent en A2 : elles montrent qui a saisi "
              "que la question est celle du retour, et non celle du prix.")

    return d.save(dossier)
