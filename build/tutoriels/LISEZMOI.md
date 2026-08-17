# Tutoriels vidéo de l'espace enseignant

Sept capsules narrées et sous-titrées, **filmées dans le vrai portail** pendant
qu'un script s'en sert. Elles se refabriquent entièrement : quand un écran
change, on relance la chaîne plutôt que de retoucher une vidéo.

Sortie livrée : `assets/tutoriels/*.mp4`, `*.vtt` (sous-titres) et `*.jpg`
(affiches), plus la page `assets/outils/tutoriels-enseignant.html`, à laquelle
renvoie le bouton « Tutoriels » de la barre de groupe.

## Le manifeste est la source unique

`manifeste.json` porte, pour chaque plan, **les gestes à jouer, ce qu'il faut
surligner, et le texte que dit la voix**. Toutes les étapes le relisent : le
tournage y prend les gestes, la narration le texte, le montage les deux, et la
page de visionnement en tire sa transcription et ses sous-titres. Écrire le
texte ailleurs le ferait diverger de l'image au premier ajustement — une voix
qui parle d'un bouton que le plan ne montre pas.

## La chaîne, dans l'ordre

```
npm install puppeteer-core                     # une fois, dans ce dossier
./lancer_demo.sh                               # portail de démonstration
python3 peupler_demo.py <port>                 # groupes, élèves, dates inventés
python3 narrer.py                              # → voix/*.mp3   (ElevenLabs)
python3 aligner.py                             # → voix/*.json  (mot à mot)
node    enregistrer.js <port>                  # → films/<capsule>/*.jpg
python3 monter_film.py                         # → capsules/*.mp4 + *.vtt
python3 livrer.py                              # → assets/tutoriels/ + la page
```

**La narration se fait avant le tournage** : c'est sa durée qui commande
combien de temps chaque plan est tenu à l'écran.

Pour refaire **une seule** capsule :

```
node    enregistrer.js <port> 06-materiel
python3 monter_film.py 06-materiel
python3 livrer.py
```

`enregistrer.js` **rejoue quand même les gestes des capsules précédentes**,
sans filmer : l'écran d'une capsule dépend de celles d'avant (un onglet ouvert,
une case cochée). Repartir du portail neuf donnerait d'autres images.

## Comment le film est obtenu

- **`Page.startScreencast`** du protocole DevTools rend une image chaque fois
  que la page change, avec son horodatage. **Un écran immobile n'émet aucune
  image** : le montage donne donc à chaque image la durée relevée au tournage,
  au lieu de poser une cadence fixe. Une cadence fixe ferait défiler les
  mouvements trop vite et escamoterait les temps d'arrêt.
- **`scene.js` est injecté dans la page** : le pointeur, ses déplacements, le
  défilement doux, le surlignage en fondu. Animer depuis Node, un pas par
  appel, donnerait des saccades — il faut que ça tourne dans la page, à la
  cadence de l'écran.
- **Un plan dure au moins sa narration**, mesurée à l'`ffprobe` avant le
  tournage, plus une respiration. Sans ça, l'image changerait au milieu d'une
  phrase.

## La voix et l'image sont d'accord au mot près

Caler un plan sur son début ne suffit pas : la voix dit « une barre apparaît »
pendant que le pointeur est encore en route, et l'écart grandit jusqu'à la fin
du plan. Deux pièces règlent ça, et il faut les deux.

- **`aligner.py` relève quand chaque mot est prononcé.** Il passe les MP3 déjà
  produits à l'**alignement forcé** d'ElevenLabs, qui rend la position de
  chaque mot, et écrit `voix/<plan>.json`. La synthèse « with-timestamps »
  ferait la même chose, mais en refabriquant l'audio : on repaierait toutes
  les narrations et le son changerait sans raison. Comme `narrer.py`, il garde
  le texte à côté du relevé — un plan réécrit est réaligné, sinon on calerait
  des gestes sur d'anciens mots.
- **Un geste porte un repère : `"apres": "une barre apparait"`.** Le tournage
  cherche ce fragment dans la narration (accents et ponctuation ignorés),
  attend l'instant du mot **moins une avance** (`AVANCE`, 550 ms — le temps
  que le pointeur parte) et joue alors le geste. Un fragment introuvable
  **arrête le tournage** : mieux vaut une erreur qu'un repère silencieusement
  ignoré. Un repère raté de plus de 0,6 s s'affiche en avertissement — c'est
  qu'un geste précédent mord dessus ; raccourcissez-le ou découpez le plan.
- **Écrivez les gestes dans l'ordre de la phrase.** Le plan qui disait « dès la
  première case, une barre apparaît » cochait trois cases avant de montrer la
  barre : le repère arrivait forcément trop tard. Une case, la barre, puis les
  deux autres pendant « et vous suit ».

## Deux pièges de montage qui décalaient tout

Ils étaient la vraie cause du décalage voix/image, bien avant les repères.

- **Ne jamais imposer de durée plancher à une image.** Chrome n'émet une image
  que lorsque la page change, mais il les émet **par rafales** : dix images
  peuvent porter presque le même horodatage. Leur donner à chacune au moins
  1/30 s allongeait la rafale, et le film prenait du retard sur la voix —
  **jusqu'à 46 s** en fin de capsule 7, mesuré. Une rafale plus serrée que
  1/30 s ne peut de toute façon pas être montrée : on écarte les images
  surnuméraires, et la durée totale reste celle du tournage.
- **`concat` rejoue la tenue de la dernière image.** Elle doit être répétée en
  fin de liste, sinon sa durée est ignorée ; mais la répétition la rejoue une
  seconde fois — 17 s de rab sur une capsule. D'où le `-t` posé sur
  l'encodage du corps : c'est lui qui arrête le film à la durée réelle.
- **Contrôle** : la durée d'une capsule doit valoir la fin du dernier plan,
  plus la respiration et les deux cartons. Un écart de plus d'une seconde
  signale que l'un de ces deux pièges est revenu.

## Ce qu'il ne faut pas défaire

- **L'instance de capture est jetable et isolée.** `lancer_demo.sh` impose un
  `STORAGE_DIR` hors du dépôt. `init_storage()` y recopie le catalogue, ce qui
  est voulu ; en revanche, si le bac à sable a déjà servi, **purgez
  `data/teachers.json`, `groups.json`, `students.json`, `schedule.json` avant
  de recommencer** — sinon vous filmez de vraies personnes. Tous les noms
  d'élèves des capsules sont inventés.
- **Aucun mot de passe dans le code.** Le dépôt est public. `lancer_demo.sh`
  tire un secret au hasard au premier lancement et le dépose dans
  `$STORAGE_DIR/identifiants-demo.json`, hors du dépôt, en lecture pour vous
  seul. `peupler_demo.py` et `enregistrer.js` le relisent là (ou dans
  `PROF_COURRIEL` / `PROF_MOTDEPASSE`). Le fichier est **gardé** d'un
  lancement à l'autre : le compte a été créé avec l'empreinte du premier mot
  de passe, en tirer un neuf fermerait la porte. Pour repartir de zéro,
  effacez le bac à sable en entier.
- **`puppeteer-core`, jamais `puppeteer`** : le premier pilote le Chrome déjà
  installé sur le poste, le second téléchargerait un navigateur de 150 Mo dans
  le dépôt. `node_modules/` n'est pas versionné.
- **Les gestes doivent se voir.** Un clic passe par le pointeur animé
  (`__scene.clic`), jamais par un `element.click()` direct — sinon la voix dit
  « cliquez ici » et rien ne bouge à l'écran. Même chose pour le défilement :
  `__scene.defiler`, pas `scrollIntoView`.
- **Le tournage se fait à vitesse réelle** : compter environ une minute de
  tournage par minute de capsule. On ne peut pas l'accélérer sans rendre les
  mouvements ridicules.
- **Le tournage est en 3200 × 1800** (1600 × 900 au facteur 2) puis redescendu
  en 1080p. En filmant directement en 1080p, le texte de 15 px du portail
  devient illisible une fois compressé.
- **La voix est celle du « narrateur »** (`IPgYtHTNLjC7Bq7IPHrm`), distincte
  des voix de personnages des dialogues élèves — sinon l'enseignante entend le
  patron du module 3 lui expliquer son portail. Modèle
  `eleven_multilingual_v2`, comme le reste de la bibliothèque.
- **`narrer.py` ne repaie pas un plan déjà narré**, mais il détecte les textes
  réécrits : le texte dit est gardé en `voix/<plan>.txt` et comparé au
  manifeste. Se fier à la seule présence du MP3 laisserait un plan réécrit
  garder l'ancienne narration — une erreur qui ne s'entend qu'au visionnement
  final. ElevenLabs facture au caractère ; seuls les plans changés sont repayés.
- **Les sous-titres sont un fichier à part** (`.vtt`), pas une incrustation :
  on peut les couper, et les corriger sans réencoder la vidéo.
- **Attention au volume qui masque le code.** `/assets/` est servi depuis
  `STORAGE_DIR` d'abord, et `init_storage()` ne copie `assets/` qu'au **premier**
  démarrage (seul `assets/interactive/` est resynchronisé ensuite). Un bac à
  sable déjà lancé sert donc l'ancienne page même après un `livrer.py` : on
  croit à un bogue de la chaîne, c'est une copie figée. Effacez
  `$STORAGE_DIR/assets/outils/tutoriels-enseignant.html` et
  `$STORAGE_DIR/assets/tutoriels/` avant de vérifier. En production le volume
  est antérieur à ces fichiers, donc rien ne les masque — mais **vérifiez la
  durée d'une capsule après déploiement** plutôt que son seul code 200.
- **Le catalogue rend les modules repliés** : leurs seize séances n'existent
  dans le document qu'après un clic sur « Voir le matériel ». Les gestes
  `ouvrir-module` / `ouvrir-seance` s'en chargent, et ne recliquent pas un
  module déjà ouvert — le bouton bascule, il le refermerait.
- **Les dépôts d'enseignant s'affichent dans la colonne de gauche**, section
  « Dépôts de l'équipe », et non dans le panneau de détail d'une séance.
- Le guide en diapositives (`assets/outils/guide-espace-enseignant.html`) dit
  la même chose en version lisible et imprimable. **Les deux doivent rester
  d'accord** : en changeant le manifeste, relisez-le.

## Fichiers

| | |
|---|---|
| `manifeste.json` | le scénario — gestes, surlignage, texte dit |
| `lancer_demo.sh` | l'instance jetable et son secret |
| `peupler_demo.py` | groupes, élèves, dates et dépôts inventés |
| `scene.js` | le pointeur et les gestes, injectés dans la page |
| `enregistrer.js` | pilote Chrome et filme par le protocole DevTools |
| `narrer.py` | la voix off (ElevenLabs) |
| `aligner.py` | à quel instant chaque mot est dit (alignement forcé) |
| `monter_film.py` | cartons, montage, mixage, sous-titres (ffmpeg) |
| `livrer.py` | copie dans `assets/` et produit la page de visionnement |

`capturer.js` et `monter.py`, qui produisaient l'ancienne version en captures
fixes, ont été retirés : la chaîne filmée les remplace entièrement.
