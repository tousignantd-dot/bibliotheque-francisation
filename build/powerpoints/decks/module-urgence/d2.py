# -*- coding: utf-8 -*-
"""D2 · Poser une question polie.
Bloc D · couleur ambre (écriture) · 75 min.
Source : exercices `t3poli` et `t3reconf`.
"""
from theme import Deck


def build(dossier):
    d = Deck(
        code='D2', section='ambre',
        titre='Poser une question polie',
        chapeau="« Donnez-moi son numéro de chambre » et « Pourriez-vous me donner son "
                "numéro de chambre ? » demandent la même chose. Une seule des deux "
                "obtient une réponse aimable.",
        duree='75 minutes')

    d.titre(notes="Écrire les deux phrases au tableau et demander laquelle on préférerait "
                  "recevoir. Le groupe choisira la seconde sans hésiter : la leçon est "
                  "déjà à moitié faite.")

    d.objectifs([
        "transformer une demande directe en demande polie ;",
        "employer pourriez-vous, auriez-vous, je voudrais ;",
        "employer « est-ce que je pourrais » pour demander une permission ;",
        "écrire un message court à une personne blessée.",
    ])

    d.regle('La règle',
            "Le conditionnel transforme un ordre en demande.",
            precision="« Vous pouvez » devient « pourriez-vous ». « Je veux » devient "
                      "« je voudrais ». « Vous avez » devient « auriez-vous ». Le sens "
                      "ne change pas ; le rapport entre les deux personnes, oui.",
            notes="Écrire les trois transformations au tableau. Ce sont les seules "
                  "formes à connaître pour ce module : ne pas enseigner tout le "
                  "conditionnel.")

    d.tableau('Analyse', "Trois formules polies",
              ['Formule', 'Pour', 'Exemple'],
              [["Pourriez-vous…", "demander un service", "Pourriez-vous me donner son nom ?"],
               ["Auriez-vous…", "demander si ça existe", "Auriez-vous un endroit où attendre ?"],
               ["Je voudrais…", "dire ce qu'on veut", "Je voudrais voir ma sœur."]],
              cle=0,
              note="Les trois se placent au début de la phrase. Le reste ne change pas.",
              notes="Faire remarquer que « pourriez-vous » et « auriez-vous » sont à "
                    "l'inversion, comme les questions polies du module 1.")

    d.regle('Demander une permission',
            "Est-ce que je pourrais… — pour demander le droit de faire quelque chose.",
            precision="« Est-ce que je pourrais monter la rejoindre ? » Ce n'est pas une "
                      "question sur une capacité, c'est une demande d'autorisation. La "
                      "réponse attendue est oui ou non.",
            notes="Faire trouver au groupe cinq situations d'hôpital où on demande une "
                  "permission : monter, entrer, rester, téléphoner, apporter quelque "
                  "chose.")

    d.cartes('Ouvrir la mini-leçon', "Quatre degrés de politesse", [
        ("L'impératif · direct",
         "« Donnez-moi son nom. » Correct entre proches ou dans l'urgence. Trop sec "
         "avec un inconnu."),
        ("La question simple · neutre",
         "« Est-ce que vous pouvez me donner son nom ? » Toujours acceptable. C'est le "
         "niveau à maîtriser en premier."),
        ("Le conditionnel · poli",
         "« Pourriez-vous me donner son nom ? » Le niveau attendu avec un employé, un "
         "fonctionnaire, un propriétaire."),
        ("S'il vous plaît · en plus",
         "S'ajoute à n'importe lequel des trois et adoucit encore. À la fin de la "
         "phrase, jamais au début."),
    ], notes="Insister sur la deuxième carte : un élève qui ne maîtrise que « est-ce que "
             "vous pouvez » se débrouille très bien. Le conditionnel est un bonus, pas "
             "une obligation.")

    d.pratique('Pratique · 1 de 4', "Transformez en demande polie",
               "Employez pourriez-vous, auriez-vous ou je voudrais.", [
        ("Donnez-moi son numéro de chambre.",
         "Pourriez-vous me donner son numéro de chambre, s'il vous plaît ?"),
        ("Je veux voir ma sœur.", "Je voudrais voir ma sœur."),
        ("Où est la salle d'attente ?",
         "Pourriez-vous me dire où est la salle d'attente ?"),
        ("Vous avez un formulaire ?", "Auriez-vous un formulaire ?"),
        ("Répétez.", "Pourriez-vous répéter, s'il vous plaît ?"),
    ], corrige=True,
       notes="Accepter toute formulation polie correcte. Ce qui compte est le "
             "déplacement du registre, pas la formule exacte.")

    d.pratique('Pratique · 2 de 4', "Permission ou service ?",
               "Choisissez « est-ce que je pourrais » ou « pourriez-vous ».", [
        ("Vous voulez monter voir un patient.", "Est-ce que je pourrais monter ?"),
        ("Vous voulez que la personne répète.", "Pourriez-vous répéter ?"),
        ("Vous voulez rester après les heures de visite.", "Est-ce que je pourrais rester ?"),
        ("Vous voulez qu'on vous indique le chemin.", "Pourriez-vous m'indiquer le chemin ?"),
    ], corrige=True,
       notes="Le critère : est-ce que je demande quelque chose à la personne, ou est-ce "
             "que je demande le droit de faire quelque chose ? Le faire formuler par le "
             "groupe.")

    d.piege('Le piège du « je veux »',
            "Je veux voir ma sœur.",
            "Je voudrais voir ma sœur.",
            "« Je veux » est grammaticalement correct mais sonne comme une exigence. "
            "En français, on emploie presque toujours « je voudrais » pour demander "
            "quelque chose à un inconnu. Ce n'est pas une règle de grammaire, c'est un "
            "usage — et il est très fort.",
            notes="Erreur fréquente et très visible. Beaucoup d'élèves l'emploient sans "
                  "savoir qu'elle choque. Le dire sans dramatiser.")

    d.piege("Le piège du « s'il vous plaît » au début",
            "S'il vous plaît, donnez-moi son nom.",
            "Pourriez-vous me donner son nom, s'il vous plaît ?",
            "« S'il vous plaît » placé devant un impératif ne le rend pas beaucoup plus "
            "aimable : l'ordre reste un ordre. La politesse française passe d'abord par "
            "la forme du verbe, et « s'il vous plaît » s'ajoute à la fin.",
            notes="Nuance culturelle utile : dans plusieurs langues, l'ajout d'un mot "
                  "suffit. En français, c'est la construction entière qui change.")

    # ── seconde partie · le message de réconfort ───────────────────
    d.regle('Écrire à une personne blessée',
            "Prendre des nouvelles, souhaiter un rétablissement, offrir quelque chose de précis.",
            precision="Trois phrases suffisent. La troisième est la plus importante : "
                      "une offre concrète — « je peux faire ton quart de vendredi » — "
                      "vaut mieux que « dis-moi si tu as besoin de quelque chose ».",
            notes="Faire remarquer pourquoi l'offre vague ne marche pas : elle oblige la "
                  "personne blessée à demander, et personne n'ose demander.")

    d.pratique('Pratique · 3 de 4', "Écrivez le message",
               "Trois phrases : des nouvelles, un souhait, une offre concrète.", [
        ("Fatou est en congé de maladie pour trois jours.",
         "Salut Fatou, comment va ton bras aujourd'hui ? J'espère que la douleur "
         "diminue. Si tu veux, je peux faire ton quart de vendredi."),
        ("Un collègue s'est cassé le bras.",
         "Bonjour Marc, j'ai su pour ton bras. Bon rétablissement. Je passe au "
         "dépanneur ce soir, veux-tu que je t'apporte quelque chose ?"),
    ], corrige=True,
       notes="Vingt minutes d'écriture. Faire lire deux ou trois messages à voix haute : "
             "le groupe entendra ce qui sonne sincère et ce qui sonne formel.")

    d.pratique('Pratique · 4 de 4', "Vague ou concret ?",
               "Laquelle des deux offres est utile ?", [
        ("« Dis-moi si tu as besoin de quelque chose. »", "vague — elle oblige à demander"),
        ("« Je peux faire ton quart de vendredi. »", "concrète — elle se répond par oui ou non"),
        ("« N'hésite pas. »", "vague — elle ne propose rien"),
        ("« Je passe à la pharmacie ce soir, veux-tu ta crème ? »", "concrète"),
    ], corrige=True,
       notes="Exercice court mais formateur. Faire reformuler les deux offres vagues en "
             "offres concrètes.")

    d.billet(
        "Écrivez trois questions polies que vous poseriez à l'accueil d'un hôpital.",
        exemples=[
            "Une avec pourriez-vous, une avec auriez-vous, une avec est-ce que je "
            "pourrais.",
            "Ajoutez « s'il vous plaît » à la fin d'au moins une.",
        ],
        notes="Corriger la forme du verbe avant tout. Rendre avant E1, où ces questions "
              "seront posées à voix haute.")

    return d.save(dossier)
