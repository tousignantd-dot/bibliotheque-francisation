# Modules autonomes

La section du dépôt où vit l'**autre forme** de nos modules : un parcours qui
s'apprend **sans personne à côté** — un écran à la fois, l'explication au moment
où elle sert, un début et une fin, et un suivi qui montre le trajet plutôt qu'un
pourcentage.

Ouverte le **30 août 2026**. Elle ne remplace rien : les 87 modules de classe du
catalogue ne bougent pas.

- **La page de la section** : [`index.html`](index.html) — l'état du chantier,
  les décisions prises, l'arborescence.
- **Le plan de la démo** : [`plan-storyline.html`](plan-storyline.html) — la
  grammaire des neuf types d'écran et le storyboard des dix-huit écrans.

## Module de classe / module autonome

| | Module de classe | Module autonome |
|---|---|---|
| On fait quoi | on **défile** | on **avance** |
| L'explication | à côté, repliée | dans l'écran, au moment de l'erreur |
| Le rythme | celui de l'enseignant | celui de l'élève |
| Le suivi | des résultats | un trajet |
| Fait pour | la matinée en groupe | le soir, le téléphone, seul |

## Les décisions du 30 août 2026

| Question | Réponse |
|---|---|
| Module de démo | **`module-n5-rendezvous`** — l'appel à la clinique |
| Place du storyline | **on décide après la démo** — aucun module de classe touché |
| Longueur | **un défi, 18 écrans**, 20-25 min |
| Circulation | **verrou doux** — on avance quand on a agi, on revient toujours |
| Narration | **écrite, pas parlée** — aucun MP3 neuf |
| Suivi | **local pour la démo**, branchement serveur ensuite |
| Format de l'écran | **16:9 figé au-dessus de 900 px**, pleine hauteur de fenêtre en dessous |

## Les règles

1. **Généré, jamais édité.** Le HTML d'un parcours sort de
   `build/gabarit/storyline.html` + `build/storyline.py` +
   `build/contenu/<slug>/storyline.js`. Retoucher le HTML produit, c'est perdre
   le travail à la construction suivante.
2. **Les médias se réutilisent.** Un parcours rejoue les MP3 et les images du
   module de classe correspondant, par chemin absolu
   (`/assets/interactive/<slug>/…`). Rien n'est copié ni resynthétisé — le gel
   des MP3 tient.
3. **Aucune IA nécessaire.** Chaque vérification se corrige sans modèle : un
   centre en mode sans assistant joue le parcours entier.
4. **Le pseudo, jamais le nom**, et aucun enregistrement vocal ne part sans que
   l'élève l'envoie.
5. **Vérifié en le jouant** — par programme, écran par écran, bonne réponse et
   mauvaise. Une capture d'écran ne prouve rien.
6. **Inscrit aux présentations.** Tout document produit ici reçoit sa fiche sur
   `presentations.html`.
7. **La hauteur du cadre 16:9 est calculée, jamais laissée à `aspect-ratio`.**
   Avec le rapport seul, un rattrapage qui s'ouvre fait grandir le cadre —
   mesuré à 1,63 au lieu de 1,78. C'est le corps qui défile, pas la page.

## L'arborescence

```
modules-autonomes/
├── index.html              la page de la section
├── README.md               ce fichier
├── plan-storyline.html     le plan et les six décisions
└── n5-rendezvous-defi1/    le parcours construit — 2 écrans sur 18

build/
├── gabarit/storyline.html  la coquille : jauge, navigation, les mises en page
├── storyline.py            le moteur
└── contenu/module-n5-rendezvous/storyline.js   les écrans, en données
```

## Un parcours est une ordonnance, pas un cours

Il traite **un savoir**, pas une situation ; l'enseignant l'**envoie** à un élève
chez qui il a constaté la lacune. Dix minutes, huit à douze écrans.

**Le diagnostic reste à l'enseignant.** Rien ne se déclenche tout seul, et ce
n'est pas une étape en attendant mieux : c'est une décision, prise le
30 août 2026. Ne pas proposer de suggestion automatique.

### Ce qui sépare un parcours d'une mini-leçon

Huit modules portent déjà une mini-leçon sur le passé composé, six sur l'heure.
Un élève envoyé sur un parcours en a probablement lu deux : **le redire
autrement ne sert à rien**. Cinq écarts, à tenir dans chaque parcours neuf.

| | La mini-leçon | Le parcours |
|---|---|---|
| L'ordre | la règle, puis l'application | des cas tranchés, **puis** la règle |
| L'étendue | exhaustive, consultable | **partielle** : un test réutilisable, les cas fréquents |
| Le métalangage | en tête | **après** avoir manipulé la chose |
| Les exemples | ceux du module | pris à **plusieurs** situations |
| Le geste | elle se lit | il **se traverse** — chaque écran demande une décision |

L'écran `tri` est ce qui rend le premier écart possible : l'élève range des cas
sans qu'aucune règle ne lui ait été donnée, et chaque erreur explique **ce
cas-là**, jamais la règle entière.

## Construire un parcours

```
python3 build/storyline.py --tous          # tout reconstruire
python3 build/storyline.py heure-et-date
python3 build/storyline.py --tous --verifier   # code 1 si un parcours est à reconstruire
```

Le contenu d'un parcours de remédiation vit dans **`build/parcours/<slug>.js`**
— un seul fichier, `const PARCOURS` et `const ECRANS`. Un parcours attaché à un
module vit, lui, dans `build/contenu/<module>/storyline.js`.

Trois types d'écran : **`notion`** (ce qu'il faut savoir, en un écran),
**`verif`** (une question, un rattrapage par mauvaise réponse, la réponse au
second essai) et **`tri`** (trancher des cas, un bouton par colonne — pas de
glisser-déposer : un doigt ne traîne pas une étiquette sur un téléphone).

Le contrôle refuse d'écrire quand quelque chose casserait chez l'élève sans
casser la construction : un type d'écran inconnu, un identifiant en double, une
vérification sans bonne réponse ou sans rattrapage, un extrait sonore absent du
disque.

## État — 30 août 2026

**Deux parcours de remédiation, dix écrans chacun**, plus les deux écrans de la
démo d'origine.

| Parcours | Savoir | Sons |
|---|---|---|
| `heure-et-date` | lexique, repère culturel | 4 extraits de `module-n5-rendezvous`, rejoués |
| `passe-compose-etre-avoir` | `n5-s31` | aucun — la faute n'existe qu'à l'écrit |
| `n5-rendezvous-defi1` | la démo de forme, 2 écrans sur 18 | 3 extraits |

Vérifiés **en les jouant**, par programme, écran par écran et dans les deux
chemins : chaque mauvaise réponse ouvre son rattrapage, la réponse n'est donnée
qu'au second essai, chaque tri se verrouille cas par cas, « Continuer » ne se
déverrouille qu'une fois l'écran fait, et les quatre extraits répondent 200.

## Prochaine étape

Les faire essayer. Puis **l'envoi** : le bouton chez l'enseignant, la bande
« votre enseignant vous a envoyé » chez l'élève, et le retour du résultat.
Écrire douze parcours de plus avant d'avoir vu un envoi aller au bout serait
refaire l'erreur qu'évite le calcul de `deux-modeles.html`.
