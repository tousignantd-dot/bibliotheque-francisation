# Un premier module pour chaque niveau

Mandat du 20 août 2026. Le niveau 4 compte dix-huit modules ; les sept autres
niveaux n'en ont aucun. Ce chantier produit **un module par niveau** — le
premier — pour vérifier que la chaîne de production tient à tous les stades,
du débutant qui apprend à se présenter à l'avancé qui suit l'actualité.

## Ce que l'utilisateur a tranché

1. **Les situations sont choisies par moi**, une par niveau (tableau plus bas).
2. **Le format s'adapte aux niveaux 1 et 2** : huit séances, deux défis, deux
   blocs de quatre heures. Les niveaux 3 et 5 à 8 gardent le format du niveau
   4 : seize séances, trois défis.
3. **Médias et mise en ligne autorisés** : images fal.ai, MP3 ElevenLabs, et
   `git push` au fur et à mesure. Estimation : 25 $ à 40 $ pour les sept.

## Les sept modules

| Niveau | Situation retenue | Slug prévu | Format | Pourquoi elle |
|--------|-------------------|------------|--------|---------------|
| 1 | Relations sociales | `module-n1-presenter` | 8 séances | 4 intentions sur 9 ; se présenter est le premier besoin de tous |
| 2 | Déplacement dans une ville | `module-n2-autobus` | 8 séances | 4 intentions ; concret, visuel, immédiatement utile |
| 3 | Achat d'aliments ou de produits d'entretien | `module-n3-epicerie` | 16 séances | 8 intentions, la plus riche du niveau |
| 5 | Location d'un logement | `module-n5-logement` | 16 séances | 4 intentions ; la démarche la plus lourde d'une installation |
| 6 | Recherche d'emploi | `module-n6-emploi` | 16 séances | 4 intentions ; le tournant du stade intermédiaire |
| 7 | Suivi de l'actualité | `module-n7-actualite` | 16 séances | 6 intentions ; compréhension de discours longs |
| 8 | Emploi | `module-n8-emploi` | 16 séances | 10 intentions, de loin la plus dense du programme |

Les situations se répètent d'un niveau à l'autre dans le programme lui-même —
« Relations sociales » existe aux niveaux 1, 2, 3, 4 et 6. Ce n'est pas une
redite : les intentions de communication changent complètement. Au niveau 1 on
se présente ; au niveau 6 on exprime un désaccord dans un groupe.

## L'ordre de production, et pourquoi

1. **Niveau 3** — le voisin immédiat du 4. Aucune inconnue : c'est le format
   connu, à peine simplifié. Il donne un livrable rapidement et confirme que
   la chaîne accepte un autre niveau que le 4.
2. **Niveau 1** — la vraie inconnue du chantier : format court, stade
   débutant, très peu de lexique disponible. À affronter tôt plutôt que tard.
3. **Niveau 2** — profite de tout ce que le niveau 1 aura appris.
4. **Niveau 5**, puis **6**, **7**, **8** — de plus en plus longs et abstraits ;
   le lexique du programme s'amenuise à mesure qu'on monte, et le contenu
   s'invente davantage.

## Le socle technique à poser avant le niveau 1

- **Une grille de huit séances** dans `build/powerpoints/modules.py` :
  `GRILLE_COURTE = a1 a2 a3 b1 b2 c1 c2 e1`, deux blocs de quatre. Les deux
  grilles existantes (`GRILLE_3_DEFIS`, `GRILLE_2_DEFIS`) font seize séances
  chacune ; c'est une troisième, pas une modification.
- **La numérotation par niveau.** Aujourd'hui `numero` est unique et l'ordre
  d'affichage s'y fie. Sept modules qui portent tous le numéro 1 vont se
  télescoper : il faudra trier par `(niveau, numero)` dans `ORDRE` et vérifier
  le portail. C'est le seul point qui touche du code partagé.
- **Le nombre de sections n'est pas un problème** : il vit dans `sections.js`,
  donc dans le contenu. Un module à cinq sections ne demande rien au gabarit.

**Fait le 20 août 2026.** `GRILLE_COURTE` (huit séances : a1 a2 a3, b1 b2,
c1 c2, e1) est dans le registre ; `ORDRE` trie par `(niveau, numero)` ;
`build_fiches.py` sait écrire « Huit fiches » et non « 8 fiches ».

**La convention de slug change**, et c'est une décision du chantier : le slug
porte le niveau, `module-n3-epicerie`. Sans lui, le premier module du niveau 1
sur les relations sociales entrerait en collision avec `module-relations` du
niveau 4 — la même situation revient à cinq niveaux dans le programme. Le
préfixe `module-` reste : huit scripts balaient `assets/interactive/module-*`
et le perdre les rendrait aveugles.

## Ce que le programme donne, et ce qu'il faut chercher ailleurs

Le programme donne la spécification complète : intentions, savoirs, lexique,
critères. Il ne donne aucun fait du monde réel. Pour les modules qui reposent
sur une procédure — le bail du niveau 5, l'assurance emploi du niveau 8 — il
faut vérifier les faits québécois (montants, délais, noms d'organismes) plutôt
que les inventer. Ces vérifications se font au coup par coup, sur les sites
officiels, et se notent ici.

## Le format des images, changé pour ce chantier

Les images des exercices étaient carrées. Mesure faite dans le navigateur sur
`module-vetements` : la zone de glisser-déposer (`.imgzone`) fait **223 × 132
px**, soit un rapport de 1,7 — un rectangle paysage. Une image carrée y est
recadrée par `object-fit:cover`, et le tiers du haut et du bas disparaît.

Décision : générer les prochaines images en **3:2 paysage** (1536 × 1024 chez
fal.ai), et aligner le CSS pour ne plus recadrer :

- `.imgtile` (la vignette de la banque) : 100 × 100 → `aspect-ratio:3/2`,
  largeur 150 px ;
- `.vc-photo` (le mot et son image) : `aspect-ratio:1/1` → `3/2` ;
- `.imgzone` : déjà un rectangle, à fixer en `aspect-ratio:3/2` pour que la
  zone vide annonce la forme de ce qu'elle attend.

**Ces trois retouches vivent dans le gabarit**, qu'une autre session est en
train de modifier (l'identité de marque SAAF). Elles se feront quand elle aura
commité — avant la génération d'images du premier module, pas après.

## Le suivi des images sur le mur

Toutes les images produites sont déjà versées dans `~/Claude/generations`, à
plat, avec leur fichier `.json` de traçabilité (prompt, modèle, coût). Le mur
`le-mur.html` les lit par `mur-data.js`, régénéré par `maj-mur.py`. État au
20 août 2026 : 210 médias, 6,94 $ cumulés. **Refaire `python3 maj-mur.py`
après chaque module**, sinon le mur montre l'état précédent.

## Journal

_(une section par module, remplie à mesure)_

## Niveau 3 — `module-n3-epicerie` · À l'épicerie · **livré**

Situation « Achat d'aliments ou de produits d'entretien », huit intentions.
Distinct du module 14 du niveau 4, qui porte sur le comptoir et l'étiquette :
ici, on **trouve** un produit, on **choisit** avec la circulaire, et on
**paie**.

**Scénario.** Marisol, arrivée du Guatemala il y a huit mois, fait ses courses
seule dans une grande épicerie. Elle cherche de la farine de maïs qui n'est pas
avec les farines ; sa voisine Ginette lui montre la circulaire et les mises en
garde des produits d'entretien ; au comptoir, Stéphane lui rembourse un spécial
qui n'était pas passé.

**Six mini-leçons** : treize ou trente · dire où c'est · demander de l'aide ·
les mots qui mesurent · les dessins qui avertissent · lire une facture.

**Médias.** 19 images (0,64 $), **les premières en 3:2**. 204 MP3. Contrôle des
URL : 227 demandées, 227 présentes.

**Défauts trouvés et corrigés.**

- Deux tableaux trop pleins pour une diapositive projetée (A4, C2) : coupés en
  deux. `theme.py` refuse proprement, c'est le bon comportement.
- Un item de type `write` sans `accept` est corrigé **par l'IA** — c'est ce
  qu'il fallait pour « Ma fiche », dont les réponses sont libres. Les `accept`
  y avaient été mis par réflexe et auraient rendu l'exercice impossible.
- La caissière est devenue **un caissier** : la banque ElevenLabs ne compte que
  deux voix féminines, déjà prises par Marisol et Ginette.

## Niveau 1 — `module-n1-presenter` · Je me présente · **livré**

Premier module **court** du projet : huit séances, deux défis, cinq sections au
lieu de six. Le moteur ne bronche pas — le nombre de sections vit dans
`sections.js`, donc dans le contenu.

**Scénario.** Amina, arrivée d'Algérie il y a deux semaines, passe son premier
jour au centre : on lui demande son nom et de l'épeler, elle se présente à Lin,
elle apprend à dire qu'elle ne comprend pas.

**Quatre mini-leçons** : épeler son nom · les cinq phrases pour se présenter ·
de, du, d' devant le pays · saluer, remercier, faire répéter.

**Médias.** 14 images (0,47 $). L'audio a été interrompu par une panne d'API.

**Le défaut que la panne a révélé.** `generer_audio_*.py` s'arrêtait sur la
trace d'une exception à la première coupure réseau, au milieu de deux cents
extraits. Une panne passagère du fournisseur n'est pas une erreur du
programme : `parle()` réessaie maintenant cinq fois, en doublant l'attente, et
traite aussi les 429 et les 5xx. À reporter dans les prochains générateurs.

**Livré.** Commit `3d2724d`. L'audio a été repris après la panne et le module
est en ligne.


## Niveau 2 — `module-n2-autobus` · Prendre l'autobus · **livré**

Deuxième module **court** : huit séances, deux défis, cinq sections. Distinct
de `module-deplacement` (niveau 4), qui porte sur le trajet complet et le
métro ; ici, on demande son chemin et on lit un horaire d'autobus.

**Scénario.** Hassan, arrivé de Syrie il y a huit mois, cherche la
bibliothèque de son quartier, puis apprend à lire un horaire, à comprendre un
avis affiché et à demander une correspondance.

**Quatre mini-leçons** : où on va — à la, au, à l' · les mots de la direction ·
répéter pour être sûr · l'heure de l'autobus.

**Le jeu de rôle a demandé un scénario neuf.** Le manifeste appelait
`jr_scenario: 'autobus'`, qui n'existait pas dans `server.py` — le scénario
`chemin` du niveau 4 était le seul voisin, et il est trop lourd pour un niveau
2 (six étapes, noms de terminus). `JEU_DE_ROLE_AUTOBUS` a donc été ajouté :
trois cas — dans la rue, à l'arrêt, dans l'autobus —, deux rôles, `passager` et
`habitant`, et une conduite qui impose une information à la fois.

**Médias.** 14 images (0,48 $) et 143 extraits audio. Le décor n'est pas le
centre de formation, contrairement aux modules précédents : c'est la rue, et
les six photos de l'exercice doivent se reconnaître sans légende.

**Huit séances.** 87 diapositives. La séance de graphie-phonie (A2) ne porte
pas sur des lettres mais sur les chiffres de l'heure : c'est là que l'oreille
d'un élève de niveau 2 décroche à l'arrêt. B2 n'apprend aucun mot nouveau —
elle apprend ce qu'on fait quand les mots manquent.


## La couleur d'un module est devenue celle de son niveau

Décidé par l'utilisateur le 20 août 2026, au milieu de ce chantier, et
appliqué à tout le dépôt avant de reprendre le niveau 2. Deux échelles
vivaient pour une seule idée : une pastille ambre au catalogue, un en-tête
forêt en ouvrant le module. Elles n'en font plus qu'une, et le vert en est
sorti — l'olive du niveau 3 et la forêt du niveau 4 ont disparu, l'ambre est
descendu du 2 au 3, la brique a pris le 2 et l'or le 4.

Deux scripts tiennent la règle, tous deux avec `--verifier` :

    python3 build/couleurs_niveau.py --verifier
    python3 build/couleurs_sections.py --verifier

Conséquence pour la suite du chantier : **un module neuf n'a plus de couleur à
choisir.** Lui donner son niveau dans `build/powerpoints/modules.py` suffit, et
`sections.js` ne doit contenir ni `#166534` ni `#0F766E`.
