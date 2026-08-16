# Tutoriels vidéo de l'espace enseignant

Six capsules narrées, filmées **dans le vrai portail** puis montées.
Elles se refabriquent entièrement : quand un écran change, on relance la
chaîne plutôt que de retoucher une vidéo.

Sortie livrée : `assets/tutoriels/*.mp4` + `*.jpg` (affiches), et la page
`assets/outils/tutoriels-enseignant.html`, à laquelle renvoie le bouton
« Tutoriels » de la barre de groupe.

## Le manifeste est la source unique

`manifeste.json` porte, pour chaque plan, **les gestes à jouer, ce qu'il faut
surligner, et le texte que dit la voix**. Les quatre étapes le relisent :
la capture y prend les gestes, la narration le texte, le montage les deux, et
la page de visionnement en tire sa transcription. Écrire le texte ailleurs le
ferait diverger de l'image au premier ajustement — une voix qui parle d'un
bouton que le plan ne montre pas.

## La chaîne, dans l'ordre

```
npm install puppeteer-core                     # une fois, dans ce dossier
./lancer_demo.sh                               # portail de démonstration
python3 peupler_demo.py <port>                 # groupes, élèves, dates inventés
node    capturer.js  <port>                    # → plans/*.png
python3 narrer.py                              # → voix/*.mp3   (ElevenLabs)
python3 monter.py                              # → capsules/*.mp4  (ffmpeg)
python3 livrer.py                              # → assets/tutoriels/ + la page
```

Pour refaire **une seule** capsule (les autres restent en place) :

```
node    capturer.js <port> 06-materiel
python3 narrer.py                              # ne refait que les textes changés
python3 monter.py 06-materiel
python3 livrer.py
```

`capturer.js` **rejoue quand même les gestes des capsules précédentes**, sans
capturer : l'écran d'une capsule dépend de celles d'avant (un onglet ouvert,
une case cochée). Repartir du portail neuf donnerait d'autres images.

## Ce qu'il ne faut pas défaire

- **L'instance de capture est jetable et isolée.** `lancer_demo.sh` impose un
  `STORAGE_DIR` hors du dépôt. `init_storage()` y recopie le catalogue, ce qui
  est voulu ; en revanche, si le bac à sable a déjà servi, **purgez
  `data/teachers.json`, `groups.json`, `students.json`, `schedule.json` avant
  de recommencer** — sinon vous filmez de vraies personnes. Tous les noms
  d'élèves des capsules sont inventés.
- **Aucun mot de passe dans le code.** `lancer_demo.sh` tire un secret au
  hasard au premier lancement et le dépose dans
  `$STORAGE_DIR/identifiants-demo.json`, hors du dépôt, en lecture pour vous
  seul. `peupler_demo.py` et `capturer.js` le relisent là (ou dans
  `PROF_COURRIEL` / `PROF_MOTDEPASSE`). Le fichier est **gardé** d'un
  lancement à l'autre : le compte a été créé avec l'empreinte du premier mot
  de passe, en tirer un neuf fermerait la porte. Pour repartir de zéro,
  effacez le bac à sable en entier.
- **`puppeteer-core`, jamais `puppeteer`** : le premier pilote le Chrome déjà
  installé sur le poste, le second téléchargerait un navigateur de 150 Mo dans
  le dépôt. `node_modules/` n'est pas versionné.
- **La durée d'un plan est celle de sa narration**, mesurée à l'`ffprobe`.
  Ne posez pas de durées à la main : elles dériveraient au premier mot changé.
- **Les captures sont prises en 3200 × 1800** (1600 × 900 au facteur 2) puis
  redescendues en 1080p. En capturant directement en 1080p, le texte de 15 px
  du portail devient illisible une fois compressé.
- **La voix est celle du « narrateur »** (`IPgYtHTNLjC7Bq7IPHrm`), distincte
  des voix de personnages des dialogues élèves — sinon l'enseignante entend le
  patron du module 3 lui expliquer son portail. Modèle
  `eleven_multilingual_v2`, comme le reste de la bibliothèque.
- **`narrer.py` ne repaie pas un plan déjà narré**, mais il détecte les
  textes réécrits : le texte dit est gardé en `voix/<plan>.txt` et comparé au
  manifeste. Se fier à la seule présence du MP3 laisserait un plan réécrit
  garder l'ancienne narration — une erreur qui ne s'entend qu'au visionnement
  final. ElevenLabs facture au caractère ; seuls les plans changés sont repayés.
- **Un cadrage se pose sur un élément (`cadreSel`), pas sur des pixels.**
  `cadre` reste possible et se lit **en coordonnées d'écran** — le script y
  reporte le défilement, parce que Puppeteer découpe en coordonnées de
  document. Un rectangle écrit à la main se décale dès qu'une rangée
  s'ajoute au-dessus.
- **Le catalogue rend les modules repliés** : leurs seize séances n'existent
  dans le document qu'après un clic sur « Voir le matériel ». Les gestes
  `ouvrir-module` / `ouvrir-seance` s'en chargent, et ne recliquent pas un
  module déjà ouvert — le bouton bascule, il le refermerait.
- **Les dépôts d'enseignant s'affichent dans la colonne de gauche**, section
  « Dépôts de l'équipe », et non dans le panneau de détail d'une séance.
- Le guide en diapositives (`assets/outils/guide-espace-enseignant.html`) dit
  la même chose en version lisible et imprimable. **Les deux doivent rester
  d'accord** : en changeant le manifeste, relisez-le.
