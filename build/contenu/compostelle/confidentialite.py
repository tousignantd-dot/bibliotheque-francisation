"""La confidentialité d'« En route vers Compostelle » — la page #confidentialite.

Demande de Daniel, 27 sept. 2026 (Loi 25, avant la vente au public). La
politique du portail (confidentialite.html) vise les élèves et les centres ;
celle-ci vise un pèlerin qui achète seul. Même principe : une page en langue
simple, un « En bref », et les cases qu'il reste à remplir VISIBLES en ambre
plutôt que tues (mémoire politique-confidentialite).

Règle : la page ne promet que ce qui a lieu. L'effacement des codes est fait
par pelerins.Pelerins.menage() (COMPOSTELLE_CONSERVATION_JOURS) ; si la durée
change dans Railway, la page la relit par /api/pelerins/offre.
"""

# À remplir par Daniel : la loi veut le titre et les coordonnées de la
# personne responsable. None → « à désigner », en ambre.
RESPONSABLE = None            # ex. ("Prénom Nom", "responsable de la protection des renseignements personnels")
COURRIEL = "confidentialite@edufrancis.ca"
MISE_A_JOUR = "27 septembre 2026"

EN_BREF = [
    "Pas de compte, pas de mot de passe, pas de courriel : l'application ne vous demande pas qui vous êtes.",
    "Votre progression, le nom de votre Compostela, votre genre et votre allergie restent <b>dans votre téléphone</b>. Nous ne les recevons pas.",
    "Le micro passe par la reconnaissance vocale de <b>votre navigateur</b> : votre voix va chez Google, Apple ou Microsoft, selon le navigateur — pas chez nous.",
    "« Parler librement » (payant) envoie vos phrases à notre serveur puis à Anthropic, aux États-Unis, pour que le personnage vous réponde. Nous ne gardons pas la conversation.",
    "Le paiement se fait chez Stripe. Nous ne voyons ni votre nom, ni votre courriel, ni votre carte.",
    "Vous pouvez tout effacer vous-même, à tout moment, dans les réglages.",
]

# (quoi, où c'est, qui le voit, combien de temps)
DONNEES = [
    ("Votre progression, vos tampons, vos réponses aux exercices", "dans votre téléphone (stockage du navigateur)",
     "vous seul", "jusqu'à ce que vous effaciez (Réglages → recommencer) ou videz le navigateur"),
    ("Le nom écrit sur votre Compostela, pèlerin ou pèlerine, votre allergie", "dans votre téléphone",
     "vous seul — l'allergie est un renseignement de santé : elle ne quitte jamais le téléphone",
     "jusqu'à ce que vous effaciez (Réglages → recommencer) ou videz le navigateur"),
    ("Votre voix, quand vous touchez le micro", "chez le fournisseur de votre navigateur (voir plus bas)",
     "ce fournisseur, pour la transcrire ; nous ne recevons que le texte, dans votre téléphone, et ne le gardons pas", "selon ce fournisseur"),
    ("Vos phrases dans « Parler librement »", "notre serveur (hébergeur Railway), puis Anthropic (États-Unis)",
     "le modèle qui fait parler le personnage ; aucun humain de notre côté", "rien n'est gardé chez nous ; Anthropic, selon ses conditions commerciales"),
    ("Votre code d'accès, ses dates, son compteur de conversations, l'identifiant Stripe du paiement", "notre serveur (hébergeur Railway)",
     "nous, pour faire marcher le code", "{conservation}"),
    ("Votre nom, votre courriel, votre carte", "chez Stripe",
     "Stripe, pour le paiement et votre reçu", "selon Stripe (obligations fiscales)"),
]

HORS_QUEBEC = [
    ("Google (Chrome, Android)", "la voix, quand vous utilisez le micro dans Chrome", "États-Unis"),
    ("Apple (Safari, iPhone)", "la voix, quand vous utilisez le micro dans Safari", "États-Unis"),
    ("Microsoft (Edge)", "la voix, quand vous utilisez le micro dans Edge", "États-Unis"),
    ("Anthropic", "vos phrases de « Parler librement », pour que le personnage réponde", "États-Unis"),
    ("Stripe", "votre nom, votre courriel et votre carte, au paiement", "États-Unis"),
]

NE_FAIT_PAS = [
    "aucune publicité, aucun traceur, aucun outil de statistiques ;",
    "aucune vente ni aucun partage de renseignements ;",
    "aucune décision prise automatiquement à votre sujet : le « test » vous situe, il ne vous classe pas ;",
    "aucun enregistrement de votre voix de notre côté.",
]


def verifier():
    assert COURRIEL.endswith("@edufrancis.ca")
    assert all(len(d) == 4 for d in DONNEES)
    assert sum("{conservation}" in d[3] for d in DONNEES) == 1
    return True


if __name__ == "__main__":
    verifier()
    print("ok —", "responsable à désigner" if RESPONSABLE is None else RESPONSABLE[0])
