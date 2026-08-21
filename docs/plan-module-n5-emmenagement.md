# Module n5 · Emménager dans un nouveau logement — plan et journal

Activité **63**, niveau 5, `numero` 3, seize séances. Slug et numéro réservés
d'avance dans `docs/vagues-suivantes.md` ; ils n'ont pas été choisis ici.

## Ce que le programme demande

`python3 build/cadre.py 5 "Emménagement dans un nouveau logement"` rend une
situation maigre en apparence : **deux intentions seulement**, en compréhension
et en production orales — *s'informer pour louer un véhicule ou recourir aux
services de déménagement*, et *échanger avec ses voisins* — et **aucune entrée
de lexique**. Tout le vocabulaire du module s'invente donc à partir des
savoirs et des attentes de fin de cours.

Les deux intentions donnent les deux moitiés du module : le camion d'un côté,
les voisins de l'autre. Le défi 2 (l'adresse et les branchements) vient des
attentes de fin de cours plutôt que des intentions, où il n'apparaît pas.

## Ce qui le distingue de ses voisins

La situation est **absente du niveau 4** : elle commence au 5. Il n'y a donc
aucun module de niveau inférieur dont s'écarter. Les deux voisins réels sont
au même niveau :

- **`module-n5-logement` (58)** s'arrête à la signature du bail : on téléphone
  pour une annonce, on visite, on lit son bail. Ici le bail est **déjà signé**,
  et tout ce qui suit reste à faire.
- **`module-n5-degat` (62)** répare un dégât dans un logement qu'on habite
  déjà. Ici on **arrive**.

En une phrase : le 58 choisit un logement, le 62 en répare un, le 63 s'y
installe.

Un troisième voisinage était à éviter, celui de `module-n5-services` (64,
« Utilisation des services publics »). Le branchement d'électricité est traité
ici sous le seul angle de l'emménagement — ouvrir un compte à son nom, fermer
l'ancien, changer son adresse partout — et non sous celui de l'usage courant
d'un service public.

## Le scénario, inventé

Rien n'est copié d'un manuel. **Amadou Sow**, 38 ans, vient de signer un bail
pour un 4 ½ au deuxième étage du 1287, rue des Peupliers, à Limoilou. Il
emménage le premier juillet avec son garçon. Trois autres voix :

- **Thérèse Guillemette**, 72 ans, le logement 3, dans l'immeuble depuis 1998.
  Elle apprend à Amadou l'état des lieux, puis les usages de l'immeuble.
- **Patricia Dumouchel**, répartitrice chez Déménagement Cap-Rouge, au
  téléphone puis chef d'équipe le jour du déménagement.
- **Claudine Béliveau**, agente au service à la clientèle d'Hydro-Québec.

Patricia et Claudine partagent une voix : elles n'apparaissent jamais dans le
même dialogue. Thérèse porte la voix « enseignante », ralentie à 0,85 — ce qui
convient à une dame de 72 ans qui explique.

## La progression grammaticale

Choisie pour ne **pas répéter `module-n5-logement`**, qui a déjà pris
l'interrogation indirecte, le gérondif, les relatifs, l'impersonnel et le
futur simple :

| Section | Point de langue |
|---|---|
| Je découvre | les deux voyelles nasales « an » / « on » ; écrire un état des lieux |
| Défi 1 · Le camion | lire un tarif ; les pronoms conjoints ; l'impératif avec pronom |
| Défi 2 · La nouvelle adresse | les démonstratifs ; les prépositions de temps |
| Défi 3 · Les voisins | passé composé / imparfait pour raconter ; répondre à une invitation |

Neuf mini-leçons, une par point, plus celle du tarif. Vingt-deux exercices,
seize mots de vocabulaire, six dialogues.

## Le jeu de rôle

Aucun scénario existant ne convenait : `louer` sert à visiter avant de signer,
`probleme` à faire réparer. Le scénario **`demenagement`** a été ajouté à
`server.py`, avec trois cas — un 3 ½ au deuxième sans ascenseur, un 4 ½ avec un
piano et un congélateur, la location d'un camion sans chauffeur. Les tarifs
restent côté serveur : l'élève doit aller les chercher en posant des questions.

## État de la livraison

Livré : les huit fichiers de contenu, le module interactif construit, les 15
images (fal.ai, 0,51 $), les 16 présentations (185 diapositives), les 16 fiches
élèves, les vignettes, le sommaire, l'entrée de catalogue, le scénario de jeu
de rôle. Cinq des six contrôles passent ; le sixième ne signalait plus que le
module d'une autre session.

**Reste** : l'audio. Le manifeste compte 255 extraits (88 répliques de dialogue
et 167 mots, phrases et mini-leçons) ; une cinquantaine était produite au
moment d'écrire ces lignes. Deux obstacles, tous deux documentés dans
`docs/deux-agents-en-parallele.md` : le bac à sable réseau bloque
`api.elevenlabs.io`, et le Python 3.9 du système (LibreSSL 2.8.3) tombe en
`SSLEOFError` — d'où le transport `curl` dans `parle()`. L'API coupe ensuite
par vagues de plusieurs minutes. Le script est relançable et saute ce qui
existe :

    python3 generer_audio_module_n5_emmenagement.py

Les extraits manquants ne cassent rien chez l'élève : le moteur retombe sur la
synthèse vocale du navigateur.
