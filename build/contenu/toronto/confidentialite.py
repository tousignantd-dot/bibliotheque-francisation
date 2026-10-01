"""La confidentialité d'« Une semaine à Toronto » — la page #confidentialite.

Étape 8 (1er oct. 2026), Loi 25, avant la vente au public. Même forme que Compostelle
(build/contenu/compostelle/confidentialite.py) : une page en langue simple, un « En bref »,
et la page ne promet que ce qui a lieu. Ce qui diffère : les répliques des gens de
Toronto sont DITES par Azure (Microsoft, région Canada central) ; la relecture des cartes
postales envoie le texte écrit ; l'avis part par le courriel de la personne.
"""

RESPONSABLE = ("", "le fondateur de francis")   # titre exigé par la loi (P-39.1, art. 3.1), pas le nom
COURRIEL = "confidentialite@edufrancis.ca"
MISE_A_JOUR = "1er octobre 2026"

EN_BREF = [
    "Pas de compte, pas de mot de passe, pas de courriel : l'application ne vous demande pas qui vous êtes.",
    "Votre progression, vos cartes postales et ce que vous y écrivez restent <b>dans votre téléphone</b>. Nous ne les recevons pas.",
    "Le micro passe par la reconnaissance vocale de <b>votre navigateur</b> : votre voix va chez Google, Apple ou Microsoft, selon le navigateur — pas chez nous.",
    "La semaine jouée (payante) envoie vos phrases à notre serveur puis à Anthropic, aux États-Unis, pour que la personne vous réponde ; sa réponse est dite par une voix d'Azure (Microsoft, au Canada). Nous ne gardons pas la conversation.",
    "Le paiement se fait chez Stripe, qui vous demande votre nom, votre adresse et votre courriel pour le reçu. Nous ne voyons rien de tout cela, ni votre carte.",
    "Vous pouvez tout effacer vous-même, à tout moment, dans les réglages.",
]

# (quoi, où c'est, qui le voit, combien de temps)
DONNEES = [
    ("Votre progression, vos réponses aux exercices, vos cartes postales gagnées et écrites, le genre choisi pour le bilan",
     "dans votre téléphone (stockage du navigateur)", "vous seul",
     "jusqu'à ce que vous effaciez (Réglages → tout recommencer) ou videz le navigateur"),
    ("Votre voix, quand vous touchez le micro", "chez le fournisseur de votre navigateur (voir plus bas)",
     "ce fournisseur, pour la transcrire ; nous ne recevons que le texte, dans votre téléphone", "selon ce fournisseur"),
    ("Vos phrases dans la semaine jouée, et le texte d'une carte postale que vous faites relire",
     "notre serveur (hébergeur Railway), puis Anthropic (États-Unis)",
     "le modèle qui fait parler la personne et qui écrit le bilan ; aucun humain de notre côté",
     "rien n'est gardé chez nous ; Anthropic, selon ses conditions commerciales"),
    ("Les répliques de la personne, pour les faire dire à voix haute", "notre serveur, puis Azure (Microsoft, Canada)",
     "le service qui fabrique la voix", "une copie du son peut être gardée en cache sur notre serveur pour ne pas la refaire ; elle ne contient rien de vous"),
    ("Votre code d'accès, ses dates, son compteur de conversations, l'identifiant Stripe du paiement",
     "notre serveur (hébergeur Railway)", "nous, pour faire marcher le code", "{conservation}"),
    ("Votre nom, votre adresse, votre courriel, votre carte", "chez Stripe",
     "Stripe, pour le paiement et votre reçu (qui vaut exemplaire du contrat)", "selon Stripe (obligations fiscales)"),
    ("Votre avis, si vous l'envoyez", "votre propre logiciel de courriel, vers support@edufrancis.ca",
     "nous, pour améliorer l'application", "le temps de le traiter"),
]

HORS_QUEBEC = [
    ("Google (Chrome, Android)", "la voix, quand vous utilisez le micro dans Chrome", "États-Unis"),
    ("Apple (Safari, iPhone)", "la voix, quand vous utilisez le micro dans Safari", "États-Unis"),
    ("Microsoft (Edge)", "la voix, quand vous utilisez le micro dans Edge", "États-Unis"),
    ("Anthropic", "vos phrases de la semaine jouée et le texte des cartes postales relues", "États-Unis"),
    ("Microsoft Azure", "les répliques des gens de Toronto, pour les dire à voix haute", "Canada, hors Québec"),
    ("Stripe", "votre nom, votre adresse, votre courriel et votre carte, au paiement", "États-Unis"),
]

NE_FAIT_PAS = [
    "aucune publicité, aucun traceur, aucun outil de statistiques ;",
    "aucune vente ni aucun partage de renseignements ;",
    "aucune décision prise automatiquement à votre sujet : le test vous situe, il ne vous classe pas ; le bilan conseille, il ne note pas ;",
    "aucun enregistrement de votre voix de notre côté.",
]


def verifier():
    assert COURRIEL.endswith("@edufrancis.ca")
    assert all(len(d) == 4 for d in DONNEES)
    assert sum("{conservation}" in d[3] for d in DONNEES) == 1
    return True


if __name__ == "__main__":
    verifier()
    print("ok")
