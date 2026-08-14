# Module 9 · présentations et fiches élèves

Seize séances qui couvrent tout le contenu du module « Pouvez-vous régler le problème ? »
(`assets/interactive/module-probleme/`). Chaque séance existe en **deux sorties** :

| Sortie | Où | Pour qui |
|---|---|---|
| PowerPoint 16:9 | `assets/powerpoints/module-probleme/` | l'enseignant, à projeter |
| Fiche imprimable | `assets/documents/` | l'élève, en noir et blanc |

Les présentations sortent dans un **sous-dossier au nom du module** (constante
`MODULE` de `build.py`) : `A1-….pptx` n'est unique qu'à l'intérieur d'un module,
et le `A1` du prochain module écraserait celui-ci s'ils partageaient un dossier.

**Les deux sont produites à partir des mêmes fichiers `decks/*.py`.** Le contenu est écrit
une seule fois : corriger une coquille dans `decks/b2.py` corrige à la fois la présentation
et la fiche. Ne modifiez jamais un `.pptx` ni un `.html` à la main, ils seraient écrasés.

---

## Régénérer

```bash
python3 build.py                # les 16 présentations
python3 build.py b2 c3          # deux séances seulement
python3 build.py --apercu b2    # + les épreuves PNG et le contrôle de débordement
python3 build_fiches.py         # les 16 fiches élèves + le sommaire
```

Puis, depuis la racine du projet, les deux étapes qui alimentent le **dépôt de
matériel** de l'espace enseignant — à relancer après toute production :

```bash
python3 build/vignettes.py      # la vignette de 1re diapositive de chaque séance
python3 build/materiel.py       # l'inventaire, data/materiel.json
```

**Dépendances :** `python-pptx` et `Pillow`. `fontTools` est optionnel mais recommandé — il
active le contrôle des glyphes. Le poste n'a ni Node, ni LibreOffice : installez ces trois
paquets dans un environnement virtuel.

```bash
python3 -m venv venv && ./venv/bin/pip install python-pptx Pillow fonttools
./venv/bin/python build.py --apercu
```

---

## Organisation

| Fichier | Rôle |
|---|---|
| `decks/<code>.py` | le contenu d'une séance — **c'est ici qu'on écrit** |
| `theme.py` | moteur PowerPoint : jetons du système de design, échelle projetée, onze gabarits |
| `fiche.py` | moteur fiche élève : même interface, sortie HTML imprimable |
| `build.py` | construit les présentations ; lance le contrôle si `--apercu` |
| `build_fiches.py` | construit les fiches et leur sommaire ; contrôle qu'aucune couleur ne s'y glisse |
| `apercu.py` | relit un `.pptx` produit et le redessine en PNG (remplace LibreOffice, absent du poste) |
| `controle.py` | relit les PNG et signale tout texte sorti de sa boîte |

**Pour changer un contenu**, modifiez `decks/`. **Pour changer un visuel**, modifiez `theme.py`
ou `fiche.py`. Jamais l'inverse : c'est cette séparation qui garde les seize séances cohérentes.

### Comment un même deck produit deux sorties

`decks/b2.py` fait `from theme import Deck` et appelle `d.regle(...)`, `d.pratique(...)`, etc.
`build_fiches.py` remplace `theme` par `fiche` dans la table des modules avant d'importer les
decks : ceux-ci reçoivent alors le moteur HTML sans qu'une seule ligne de contenu change.

Les deux moteurs ne rendent pas tout : la fiche **retire** les notes d'enseignant, les corrigés
et les déclencheurs, et **transforme** chaque exercice en énoncé suivi d'une ligne à remplir.

---

## Les seize séances

| Bloc | Code | Titre | Durée | Section du module |
|---|---|---|---|---|
| **A** Je découvre | A1 | Un problème dans mon logement | 75 min | dialogue `prep`, `prVocab`, `pr1` |
| | A2 | Les deux façons de dire « eu » | 60 min | `prPhon` |
| | A3 | Qui faut-il appeler ? | 60 min | `prPro` |
| | A4 | Nommer et classer un problème | 50 min | `prImg`, `prType` |
| **B** Défi 1 | B1 | Oksana appelle madame Rioux | 75 min | dialogue `t1`, `t1vf`, `t1sens` |
| | B2 | Leur ou leurs | 75 min | `t1leur`, `t1leurGN` |
| | B3 | Dire depuis quand un problème dure | 90 min | `t1depuis`, `t1duree` |
| | B4 | Mes droits comme locataire | 60 min | `t1trib` |
| **C** Défi 2 | C1 | Samir monte au troisième | 60 min | dialogue `t2`, `t2vf` |
| | C2 | Avant de, après avoir | 75 min | `t2avant`, `t2ordre` |
| | C3 | Faire réparer | 75 min | `t2faire`, `t2par`, `t2qui` |
| | C4 | Trois façons d'habiter au Québec | 55 min | `t2coop` |
| **D** Défi 3 | D1 | Quatre situations inacceptables | 55 min | dialogues `t3`/`t3b`, `t3q`, `t3assoc` |
| | D2 | Se plaindre efficacement | 75 min | `t3plainte`, `t3form` |
| **E** Application | E1 | À toi : le téléphone et le courriel | 90 min | dialogue `appli`, `aQui`, `aComp` |
| | E2 | Je retiens des mots | 60 min | cartes mémoire, bilan |

248 diapositives · environ 18 heures de classe.

Chaque diapositive porte une **note de l'enseignant** (volet Commentaires de PowerPoint) :
quoi faire écouter, quoi laisser deviner, où le groupe se trompe habituellement.

---

## Fidélité au système de design

Toutes les valeurs descendent de `assets/design-system/`. En particulier :

- **Couleurs** : copie exacte de `tokens/colors.css`. Une seule couleur d'accent, le vert.
  Les cinq couleurs de section servent au repérage seulement, aux quatre endroits permis :
  pastille numérotée, sur-titre, filet gauche de 4 px, point de parcours.
- **Fonds** : aplats uniquement, aucun dégradé. Le bandeau de titre n'est jamais noir.
  Un seul bloc foncé par présentation — le billet de sortie, en toute fin de séance.
- **Structure** : filets de 1 px et alignement, pas d'ombres. Les ombres par défaut de
  PowerPoint sont retirées du XML de chaque forme.
- **Aucun émoji**, aucun caractère décoratif.
- **Rétroaction** : brève et factuelle, jamais de félicitation exagérée. La couleur ne porte
  jamais l'information seule — chaque état est doublé d'un mot.

### Deux écarts, assumés et documentés

**1. Verdana au lieu de Nunito.** Le système impose Nunito. PowerPoint n'embarque pas les
polices sur macOS, et Nunito n'est installée ni sur ce poste ni sur celui de l'enseignant :
un fichier livré avec Nunito s'afficherait avec une police de remplacement arbitraire et la
mise en page bougerait. Verdana est présente sur tout poste Windows et macOS, et c'est la
police système la plus proche des critères qui avaient fait retenir Nunito — formes très
ouvertes, `a` et `g` à un seul étage, chasse large.

**2. Les glyphes ✓ et ✕.** Verdana ne les possède pas. Là où le système les prescrit, c'est
le **mot** qui double la couleur — ce que le système autorise explicitement (« un glyphe **ou**
un mot »). Un contrôle au moment de l'enregistrement refuse tout caractère absent de Verdana,
pour qu'aucun carré vide n'apparaisse chez l'enseignant.

### Échelle typographique

Les corps du système visent un écran tenu à 40 cm ; une diapositive se lit à 6 m. Un facteur
constant d'environ 1,6 est appliqué à toute l'échelle, sans en changer les rapports :
62 → 40 pt, 30 → 28 pt, 19 → 20 pt, 18 → 19 pt, 17 → 18 pt. Le plancher est 14 pt, ce qui
transpose la règle « jamais sous 17 px ».

---

## Les fiches élèves

Format **lettre** (8,5 × 11 po), marges 14 × 15 mm, **strictement noir et blanc** : elles sont
photocopiées, et une couleur y devient un gris indistinct. Toute la hiérarchie passe donc par
la graisse, les filets et les mots — la règle du système « jamais d'information portée par la
couleur seule », poussée à son terme.

- La colonne clé d'un tableau est en **gras**, plus en couleur.
- Le piège oppose un filet **tireté** (ce qui ne tient pas) à un filet **plein et épais**
  (ce qu'il faut retenir) — et chaque colonne dit son rôle en toutes lettres.
- Le billet de sortie, aplat noir dans la présentation, devient un encadré à filet épais :
  un aplat vide une cartouche et ressort illisible en photocopie.
- Les gris sont assombris d'un cran par rapport à l'écran : une photocopieuse efface tout ce
  qui est plus clair que 15 % de noir.
- Contrairement au PowerPoint, une page HTML charge **Nunito** : ici, aucune substitution de
  police.

Aucun bloc ne dépasse une page, donc rien ne se coupe entre deux feuilles. Comptez de **4 à 5
pages par séance**, soit environ **70 pages** pour le module complet.

`module-probleme-fiches-eleves.html` est le sommaire des seize fiches : c'est lui qu'on donne
au premier cours, et c'est lui qui peut servir de `studentDoc` pour l'activité 45.

---

## Les garde-fous

Quatre contrôles automatiques. Le build échoue plutôt que de livrer un document cassé.

1. **Aucun débordement.** Chaque bloc de texte est mesuré avec les métriques réelles de
   Verdana avant d'être posé, et le corps est réduit jusqu'à ce qu'il tienne. `apercu.py`
   encadre en magenta tout texte qui sortirait quand même de sa boîte, et `controle.py`
   relit les PNG : `build.py --apercu` sort en erreur s'il en reste un.
2. **Aucun glyphe manquant.** `Deck._verifier_glyphes()` compare chaque caractère au `cmap`
   de Verdana et nomme la diapositive fautive.
3. **Aucun tableau surchargé.** Quand un tableau ne tient pas même au corps plancher, le
   gabarit lève une erreur explicite : c'est le contenu qu'il faut couper, pas la mise en
   page qu'il faut forcer.
4. **Aucune couleur dans une fiche.** `build_fiches.py` relit chaque HTML produit et rejette
   toute valeur dont les trois composantes s'écartent de plus de 8 sur 255. Les neutres chauds
   du système passent ; le vert d'accent et les rouges de rétroaction, non.

---

## Les gabarits de `theme.py`

| Méthode | Ce que c'est |
|---|---|
| `titre()` | page de titre, bandeau clair |
| `objectifs()` | « À la fin, je serai capable de… » |
| `declencheur()` | question d'ouverture, avec photo du module au besoin |
| `regle()` | la règle en une phrase, en grand — la diapo qu'on photographie |
| `tableau()` | analyse en colonnes ; `props` règle leur largeur, `cle` met une colonne en évidence |
| `cartes()` | grille de 2 ou 3 colonnes, corps communs à toutes les cartes |
| `dialogue()` | répliques, avec mise en évidence des passages clés |
| `piege()` | deux colonnes : ce qu'on entend souvent, ce qu'il faut dire |
| `pratique()` | exercice projeté ; `corrige=True` ajoute la diapo de correction, géométrie identique |
| `vocabulaire()` | mot et définition, l'article compris dans le mot |
| `billet()` | billet de sortie — le seul bloc foncé de la présentation |

Toutes acceptent `notes=` : la note de l'enseignant.
