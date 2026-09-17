# -*- coding: utf-8 -*-
"""Les zones de chaque scène, en % de l'image, avec la réponse attendue.

Les zones ne se devinent pas : elles ont été posées sur l'image, tracées, puis
regardées. Elles doivent tomber sur ce qu'elles nomment — une case « sur la
table » qui mord sur la nappe qui tombe enseigne le contraire de ce qu'on veut.
"""

SCENES = {
"n2-place-1-personnage": dict(
  titre="Place ce que j'entends — 1 · Le personnage",
  source="n2-dessine-1-personnage", base="img/personnage.jpg",
  reveal="reveal/personnage-decrit.jpg",
  domaine="Vie personnelle et citoyenneté",
  alt="La silhouette d'une personne, sans vêtements",
  # Ici le vêtement doit HABILLER : la case dit où il va **et quelle place il
  # prend**. Un pantalon à taille fixe, posé au milieu des jambes, ne
  # ressemblait à rien. Les cases épousent donc la surface réelle du vêtement.
  ajuste="zone",
  zones=[
   ("tete",   "sur la tête",    0.360,0.030, 0.600,0.150),
   ("corps",  "sur le corps",   0.283,0.155, 0.717,0.470),
   ("jambes", "sur les jambes", 0.360,0.472, 0.620,0.855),
   ("pieds",  "aux pieds",      0.345,0.850, 0.635,0.962),
   ("maing",  "à gauche",       0.175,0.420, 0.345,0.640),
   ("maind",  "à droite",       0.635,0.420, 0.805,0.640),
  ],
  # Les vêtements sont les croquis du lexique, pas des découpes du corps :
  # une découpe étiquetée « des souliers » montrait des pieds nus. Chaque
  # croquis remplit sa case, donc il habille la bonne surface.
  scene=[("une-casquette","tete","rouge"), ("un-manteau","corps","bleu"),
         ("des-pantalons","jambes","brun"), ("des-souliers","pieds","noir"),
         ("un-parapluie","maing","vert"),   ("un-sac-a-dos","maind","orange")],
  phrases=[
   "Écoutez bien. Je décris une personne. Placez les vêtements sur l'image.",
   "Sur la tête, il y a une casquette rouge.",
   "Sur le corps, il y a un manteau bleu.",
   "Sur les jambes, il y a des pantalons bruns.",
   "Aux pieds, il y a des souliers noirs.",
   "À gauche, il y a un parapluie vert.",
   "À droite, il y a un sac à dos orange.",
   "C'est fini. Touchez « Vérifier ».",
  ]),

"n2-place-2-classe": dict(
  titre="Place ce que j'entends — 2 · La classe",
  source="n2-dessine-2-classe", base="img/classe-vide.jpg", reveal="reveal/classe.jpg",
  domaine="Éducation et monde du travail",
  alt="Une classe vide, avec une fenêtre au fond et une porte à droite",
  # L'ORDRE DES CASES PORTE LA PROFONDEUR : elles se dessinent de l'arrière
  # vers l'avant, donc ce qui est devant masque ce qui est derrière. Ne pas
  # les réordonner sans y penser.
  # La septième valeur, facultative, met l'objet à l'échelle de sa distance :
  # une chaise derrière le bureau doit être plus petite que le sac devant,
  # sinon « devant » et « derrière » ne se voient pas.
  zones=[
   ("fond",    "sur le mur du fond",     0.310,0.290, 0.430,0.500),
   ("fenetre", "à côté de la fenêtre",   0.580,0.300, 0.690,0.480),
   ("derriere","derrière le bureau",     0.415,0.585, 0.545,0.690, 0.72),
   ("gauche",  "à gauche",               0.130,0.640, 0.300,0.830),
   ("droite",  "à droite",               0.690,0.640, 0.850,0.830),
   ("milieu",  "au milieu de la classe", 0.400,0.660, 0.560,0.830),
   ("devant",  "devant le bureau",       0.375,0.820, 0.585,0.955, 1.25),
  ],
  scene=[("un-tableau","fond","vert"),      ("une-horloge","fenetre","blanc"),
         ("une-chaise","derriere","noir"),  ("une-table","gauche","jaune"),
         ("une-poubelle","droite","bleu"),  ("un-bureau-de-classe","milieu","brun"),
         ("un-sac-a-dos","devant","rouge")],
  phrases=[
   "Écoutez bien. Je décris une classe. Placez les objets sur l'image.",
   "Sur le mur du fond, il y a un tableau vert.",
   "À côté de la fenêtre, il y a une horloge blanche.",
   "Au milieu de la classe, il y a un bureau brun.",
   "Derrière le bureau, il y a une chaise noire.",
   "Devant le bureau, il y a un sac à dos rouge.",
   "À gauche, il y a une table jaune.",
   "À droite, il y a une poubelle bleue.",
   "C'est fini. Touchez « Vérifier ».",
  ]),

"n2-place-3-meteo": dict(
  titre="Place ce que j'entends — 3 · La météo",
  source="n2-dessine-3-meteo", base="img/paysage.jpg", reveal="reveal/meteo.jpg",
  domaine="Vie personnelle et citoyenneté",
  alt="Un paysage vide, avec une montagne à gauche et un chemin",
  zones=[
   ("cielg",  "dans le ciel, à gauche",  0.055,0.055, 0.215,0.200),
   ("cield",  "dans le ciel, à droite",  0.760,0.070, 0.930,0.230),
   ("montagne","sur la montagne",       0.170,0.180, 0.330,0.330),
   ("colline","sur la colline",          0.700,0.415, 0.870,0.560),
   ("chemin", "à droite du chemin",      0.790,0.610, 0.945,0.790),
   ("bas",    "en bas, à gauche",        0.080,0.660, 0.250,0.830),
  ],
  scene=[("un-nuage","cielg","blanc"),   ("le-soleil","cield","jaune"),
         ("la-neige","montagne","blanc"),("une-maison","colline","rouge"),
         ("un-arbre","chemin","vert"),   ("des-fleurs","bas","orange")],
  phrases=[
   "Écoutez bien. Je décris un paysage. Placez les images.",
   "Dans le ciel, à gauche, il y a un nuage blanc.",
   "Dans le ciel, à droite, il y a un soleil jaune.",
   "Sur la montagne, il y a de la neige blanche.",
   "Sur la colline, il y a une maison rouge.",
   "À droite du chemin, il y a un arbre vert.",
   "En bas, à gauche, il y a des fleurs orange.",
   "C'est fini. Touchez « Vérifier ».",
  ]),

"n2-place-4-table": dict(
  titre="Place ce que j'entends — 4 · La table",
  source="n2-dessine-4-table", base="img/table.jpg", reveal="reveal/table.jpg",
  domaine="Consommation et environnement",
  alt="Une table avec une nappe et une chaise",
  zones=[
   ("gauche", "sur la table, à gauche", 0.255,0.335, 0.395,0.435),
   ("milieu", "sur la table, au milieu", 0.425,0.295, 0.565,0.400),
   ("droite", "sur la table, à droite", 0.600,0.320, 0.745,0.425),
   ("sous", "sous la table", 0.330,0.665, 0.700,0.790),
   ("chaise", "sur la chaise", 0.605,0.115, 0.740,0.250),
   ("acote", "à côté de la table", 0.040,0.580, 0.175,0.790),
  ],
  scene=[
         ("une-assiette","milieu","blanc"),
         ("une-fourchette","gauche","noir"),
         ("une-pomme","droite","rouge"),
         ("une-bouteille","sous","vert"),
         ("une-banane","chaise","jaune"),
         ("une-tasse","acote","bleu"),
  ],
  phrases=[
   "Écoutez bien. Je décris une table. Placez les objets sur l'image.",
   "Sur la table, au milieu, il y a une assiette blanche.",
   "Sur la table, à gauche, il y a une fourchette noire.",
   "Sur la table, à droite, il y a une pomme rouge.",
   "Sous la table, il y a une bouteille verte.",
   "Sur la chaise, il y a une banane jaune.",
   "À côté de la table, il y a une tasse bleue.",
   "C'est fini. Touchez « Vérifier ».",
  ]),

"n2-place-5-rue": dict(
  titre="Place ce que j'entends — 5 · La rue",
  source="n2-dessine-5-rue", base="img/rue.jpg", reveal="reveal/rue.jpg",
  domaine="Consommation et environnement",
  alt="Une rue avec quatre magasins vides, un banc et un lampadaire",
  zones=[
   ("m1", "le premier magasin",   0.075,0.435, 0.200,0.560),
   ("m2", "le deuxième magasin",  0.360,0.435, 0.485,0.560),
   ("m3", "le troisième magasin", 0.520,0.435, 0.640,0.560),
   ("m4", "le quatrième magasin", 0.740,0.435, 0.865,0.560),
   ("trottoir", "sur le trottoir", 0.240,0.700, 0.380,0.830),
   ("rue", "dans la rue",          0.560,0.840, 0.760,0.975),
  ],
  scene=[("une-boulangerie","m1","brun"), ("une-pharmacie","m2","vert"),
         ("une-banque","m3","bleu"),      ("une-epicerie","m4","orange"),
         ("un-chien","trottoir","noir"),  ("une-auto","rue","rouge")],
  phrases=[
   "Écoutez bien. Je décris une rue. Placez les images.",
   "Le premier magasin, c'est une boulangerie brune.",
   "Le deuxième magasin, c'est une pharmacie verte.",
   "Le troisième magasin, c'est une banque bleue.",
   "Le quatrième magasin, c'est une épicerie orange.",
   "Sur le trottoir, il y a un chien noir.",
   "Dans la rue, il y a une auto rouge.",
   "C'est fini. Touchez « Vérifier ».",
  ]),
}

# La banque de chaque scène : six objets utiles et quelques leurres, sans quoi
# l'élève placerait juste en éliminant. Le genre sert à l'accord de la couleur.
BANQUES = {
"n2-place-1-personnage": [
 ("une casquette","une-casquette","f"), ("un manteau","un-manteau","m"),
 ("des pantalons","des-pantalons","mp"), ("des souliers","des-souliers","mp"),
 ("un parapluie","un-parapluie","m"),   ("un sac à dos","un-sac-a-dos","m"),
 ("un chandail","un-chandail","m"),     ("des bottes","des-bottes","fp"),
 ("des lunettes","des-lunettes","fp"),  ("une montre","une-montre","f")],
# Quatrième valeur : la taille de l'objet posé, en multiple de la taille de
# base. Un tableau et un crayon n'ont pas la même taille dans une classe ;
# une seule taille pour tous donnait une horloge aussi grande qu'un bureau.
# Réglages dictés par l'enseignant, 17 septembre 2026.
"n2-place-2-classe": [
 ("un tableau","un-tableau","m",1.0),        ("une horloge","une-horloge","f",0.55),
 ("un bureau","un-bureau-de-classe","m",1.6),("une table","une-table","f",1.45),
 ("une poubelle","une-poubelle","f",0.65),   ("un sac à dos","un-sac-a-dos","m",0.65),
 ("une chaise","une-chaise","f",1.0),        ("un cahier","un-cahier","m",0.75),
 ("des crayons","des-crayons","mp",0.7),     ("un stylo","un-stylo","m",0.7)],
"n2-place-3-meteo": [
 ("un nuage","un-nuage","m"),           ("le soleil","le-soleil","m"),
 ("la neige","la-neige","f"),           ("une maison","une-maison","f"),
 ("un arbre","un-arbre","m"),           ("des fleurs","des-fleurs","fp"),
 ("un sapin","un-sapin","m"),           ("la pluie","la-pluie","f"),
 ("une montagne","une-montagne","f")],
"n2-place-4-table": [
 ("une assiette","une-assiette","f"),
 ("une fourchette","une-fourchette","f"),
 ("un couteau","un-couteau","m"),
 ("un verre","un-verre","m"),
 ("une pomme","une-pomme","f"),
 ("une banane","une-banane","f"),
 ("une bouteille","une-bouteille","f"),
 ("une tasse","une-tasse","f"),
 ("du pain","du-pain","m"),
 ("du fromage","du-fromage","m"),
 ("du lait","du-lait","m"),
 ("des carottes","des-carottes","fp"),
],
"n2-place-5-rue": [
 ("une boulangerie","une-boulangerie","f"), ("une pharmacie","une-pharmacie","f"),
 ("une banque","une-banque","f"),       ("une épicerie","une-epicerie","f"),
 ("un chien","un-chien","m"),           ("une auto","une-auto","f"),
 ("une librairie","une-librairie","f"), ("un autobus","un-autobus","m"),
 ("un vélo","un-velo","m"),             ("un banc","un-banc","m")],
}
