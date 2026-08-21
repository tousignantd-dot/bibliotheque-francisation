const CARRIER_PHRASES = {
  // Les clés sont les mots **exactement tels qu'ils sont écrits** dans les
  // listes `savoir[…][2]` de exos.js — accents et espaces compris. Le gabarit
  // fait `CARRIER_PHRASES[w]` sur le mot affiché : une clé en forme de slug
  // (`allee` pour « allée ») n'est jamais trouvée, et la pastille lit alors le
  // mot seul, mal prononcé. Corrigé le 21 août 2026 ; douze clés étaient des
  // slugs.

  // Les lieux et le matériel du magasin
  'allée':           "La farine est dans l'allée douze.",
  'affichette':      "Lisez l'affichette au-dessus de l'allée.",
  'tablette':        "Les grands sacs sont sur la tablette du bas.",
  'panier':          "Prends un panier, on achète peu de choses.",
  'dépanneur':       "L'épicerie est fermée : va au dépanneur.",

  // Les prix et les quantités
  'circulaire':      "La circulaire arrive le mercredi.",
  'spécial':         "Le poulet est en spécial cette semaine.",
  'livre':           "C'est trois dollars la livre.",
  'kilo':            "Un kilo de pommes, s'il vous plaît.",
  'paquet':          "Prends un paquet de pâtes.",
  'conserve':        "Deux boîtes de conserve, s'il vous plaît.",
  'treize':          "Treize dollars, pas trente.",
  'quinze':          "Allée quinze, tout au fond.",
  'rabais':          "Avec la carte, vous avez un rabais.",

  // Les avertissements
  'mise en garde':   "Cette bouteille a une mise en garde.",
  'gants':           "Mettez des gants pour ce produit.",

  // La caisse
  'caisse':          "Il y a trois personnes à la caisse.",
  'facture':         "Vérifiez votre facture avant de partir.",
  'sac':             "Les sacs réutilisables sont à deux dollars.",
  'carte de points': "Vous avez la carte de points ?",
};
