"""Les conditions de vente des jeux de rôle vendus au public — BROUILLON à faire relire.

Demande de Daniel, 28 sept. 2026, avant d'ouvrir le compte Stripe : « est-ce qu'il
y a des chances que je puisse avoir des poursuites contre moi ? » Ce texte est un
point de départ pour l'avocat, pas un avis juridique. Il couvre les trois produits
vendus de la même façon (pelerins.PRODUITS) : « Parler librement » de Compostelle,
le magasin joué de la Maison Francœur, le comptoir joué de l'Hôtel Rive-Claire et
la semaine jouée d'Une semaine à Toronto (ajoutée le 1er oct. 2026).

Sources consultées (28 sept. 2026) : les pages de l'Office de la protection du
consommateur sur les contrats conclus à distance (renseignements avant le contrat,
contenu et transmission, moment du paiement, annulation). La page ne cite pas
d'article de loi qu'elle n'a pas lu : LégisQuébec refuse la lecture automatique.

Les montants, durées et plafonds ne sont PAS écrits ici : `{…}` est rempli par
build/vente_protection.py avec pelerins.offre(), pour que le texte ne contredise
jamais ce que la caisse facture. Les cases que seul Daniel peut remplir
(VENDEUR) restent visibles, en ambre, tant qu'elles sont vides.
"""

# À remplir par Daniel une fois l'entreprise immatriculée. Vide → « à remplir », en ambre.
VENDEUR = {
    # « Trame » était pris au Registraire. Immatriculée le 30 sept. 2026 sous ce nom-ci,
    # écrit en un seul mot, exactement comme au registre.
    "nom": "Boucledidactique",
    "neq": "2282619172",  # numéro d'entreprise du Québec
    "adresse": "6398, avenue des Érables, Montréal (Québec) H2G 2M8",
    "telephone": "514-240-4618",
    "courriel": "support@edufrancis.ca",
}
MISE_A_JOUR = "brouillon du 28 septembre 2026 (décisions prises ; relecture par un avocat à décider)"

# (titre, [paragraphes]) — {placeholders} remplis au build.
SECTIONS = [
    ("Qui vend", [
        "Ces conditions s'appliquent à l'achat d'un code d'accès aux jeux de rôle de francis, vendus par "
        "{vendeur_nom} ({vendeur_neq}), {vendeur_adresse}, téléphone {vendeur_telephone}, courriel {vendeur_courriel}.",
    ]),
    ("Ce que vous achetez", [
        "Un code d'accès personnel à UN des produits suivants, selon la page où vous l'achetez :",
        "• « Parler librement », dans En route vers Compostelle : des conversations en espagnol avec les personnages du chemin ;",
        "• le magasin joué, dans la Maison Francœur : des clients à servir en français ;",
        "• le comptoir joué, dans l'Hôtel Rive-Claire : des clients à accueillir en français, en anglais ou en espagnol ;",
        "• la semaine jouée, dans Une semaine à Toronto : des gens de Toronto à qui parler en anglais, et la relecture "
        "des cartes postales que vous écrivez.",
        "Le code donne droit à {conversations} conversations pendant {mois} mois à compter du paiement. Une conversation "
        "compte au plus {tours} échanges ; on peut en commencer au plus {parjour} par jour. Tout le reste de chaque "
        "application (mots, exercices, tests, fiches) est gratuit et ne demande aucun code.",
        "Les personnages sont animés par un modèle d'intelligence artificielle (Anthropic). Ils peuvent se tromper "
        "ou mal comprendre ; ils servent à pratiquer une langue, pas à donner un renseignement fiable.",
    ]),
    ("Le prix", [
        "{prix_ligne} Des conversations supplémentaires peuvent être ajoutées au même code : {recharge_conv} "
        "conversations pour {recharge}, sans prolonger la durée.",
        "{taxes}",
        "Le paiement se fait par carte de crédit seulement, chez Stripe ; les cartes de débit et prépayées ne sont pas "
        "acceptées. Stripe vous demande votre nom, votre adresse et votre courriel : le contrat doit les porter, et ils "
        "figurent sur votre reçu. Nous ne recevons ni votre carte, ni votre nom, ni votre adresse.",
    ]),
    ("Quand vous recevez votre code", [
        "Tout de suite : il s'affiche à l'écran au retour du paiement et s'enregistre dans votre navigateur. "
        "Il est aussi écrit sur le reçu que Stripe vous envoie par courriel, qui vaut exemplaire de ce contrat, avec "
        "le lien vers ces conditions. Gardez ce reçu : c'est lui qui permet de retrouver le code sur un autre appareil.",
    ]),
    ("Remboursement", [
        "{remboursement}",
        "Pour le demander : écrivez à {vendeur_courriel} en indiquant votre code. Le remboursement est fait sur la "
        "carte utilisée, dans les 15 jours.",
        "Ces conditions n'enlèvent aucun des droits que vous accorde la Loi sur la protection du consommateur, "
        "notamment celui d'annuler si nous ne respectons pas nos obligations.",
    ]),
    ("Achat pour une équipe", [
        "Un employeur peut acheter de 2 à {lot_max} codes en un seul paiement, au prix d'un code multiplié par le nombre. "
        "Chaque code se donne à une personne. Un code de suivi est remis avec le lot, sur l'écran et sur le reçu.",
        "Le code de suivi montre à l'acheteur, pour chaque code : s'il a servi, le nombre de conversations et la date de la "
        "dernière. Jamais leur contenu, qui n'est pas gardé, ni le nom de personne. L'acheteur informe les personnes à qui "
        "il remet un code de ce qu'il pourra voir.",
        "Un lot se rembourse en entier dans les 14 jours suivant l'achat, si aucun de ses codes n'a servi à plus de 3 "
        "conversations.",
    ]),
    ("Si le service s'arrête", [
        "Si nous cessons d'offrir un produit avant la fin de la durée d'un code, nous remboursons la part non utilisée, "
        "au prorata des conversations restantes. Une panne passagère n'est pas un arrêt : une conversation qui échoue "
        "n'est pas décomptée.",
    ]),
    ("Ce que l'outil ne fait pas", [
        "Les applications de francis aident à apprendre une langue. Elles ne donnent aucun conseil médical, juridique "
        "ou de sécurité, et ne remplacent ni un interprète ni un professionnel. En cas d'urgence, appelez les services "
        "d'urgence du pays où vous êtes.",
    ]),
    ("Votre code, votre usage", [
        "Le code est pour une personne. Il ne se revend pas. Un usage automatisé ou abusif (par exemple, faire tenir au "
        "personnage des propos haineux ou illégaux) peut entraîner la suspension du code, avec remboursement de la part "
        "non utilisée.",
        "{age}",
    ]),
    ("Vos renseignements", [
        "Nous ne gardons que le code, ses dates et son compteur de conversations ; ils sont effacés {conservation} jours "
        "après l'expiration. Le détail est dans la page de confidentialité de chaque application.",
    ]),
    ("Si ces conditions changent", [
        "Un changement ne s'applique pas à un code déjà acheté, sauf s'il vous est plus favorable.",
    ]),
    ("Loi applicable et langue", [
        "Ces conditions sont régies par les lois du Québec. Elles sont rédigées en français ; une traduction peut être "
        "offerte pour faciliter la lecture, et la version française prévaut.",
    ]),
]

# Les formulations qui dépendent d'une décision (clé → option → texte).
VARIANTES = {
    "remboursement": {
        "14j-peu-utilise": "Vous pouvez demander le remboursement complet dans les 14 jours suivant l'achat, si vous avez "
                           "utilisé au plus 3 conversations.",
        "30j": "Satisfait ou remboursé : vous pouvez demander le remboursement complet dans les 30 jours suivant l'achat, "
               "quel que soit l'usage.",
        "loi-seulement": "Le code n'est pas remboursable, sauf dans les cas prévus par la loi.",
    },
    "age": {
        "18-ou-parent": "L'achat est réservé aux personnes majeures ; une personne mineure doit avoir l'accord d'un parent.",
        "aucune": "",
    },
    "taxes": {
        "petit-fournisseur": "Le prix ne comprend aucune taxe : le vendeur est un petit fournisseur non inscrit aux "
                             "fichiers de la TPS et de la TVQ.",
        "inscrit": "Le prix affiché comprend la TPS et la TVQ, détaillées sur le reçu (numéros d'inscription : {tps} / {tvq}).",
    },
}


def verifier():
    assert VENDEUR["courriel"].endswith("@edufrancis.ca")
    import re
    trous = set()
    for _, ps in SECTIONS:
        for p in ps:
            trous |= set(re.findall(r"\{(\w+)\}", p))
    connus = {"vendeur_nom", "vendeur_neq", "vendeur_adresse", "vendeur_telephone", "vendeur_courriel", "conversations",
              "mois", "tours", "parjour", "prix_ligne", "recharge_conv", "recharge", "taxes", "remboursement", "age",
              "conservation", "lot_max"}
    assert trous <= connus, trous - connus
    return True


if __name__ == "__main__":
    verifier()
    print("ok —", len(SECTIONS), "sections")
