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

## Construire un parcours

```
python3 build/storyline.py --tous          # tout reconstruire
python3 build/storyline.py n5-rendezvous-defi1
python3 build/storyline.py --tous --verifier   # code 1 si un parcours est à reconstruire
```

Le contrôle refuse d'écrire quand quelque chose casserait chez l'élève sans
casser la construction : un type d'écran inconnu, un identifiant en double, une
vérification sans bonne réponse ou sans rattrapage, un extrait sonore absent du
disque.

## État

**Deux écrans sur dix-huit**, livrés le 30 août 2026 — une *notion* et une
*vérification* avec son rattrapage. Le moteur porte déjà la jauge, le menu des
écrans vus, le lecteur d'extraits (ralenti, transcription), le verrou doux, le
point de reprise et le journal du suivi.

Vérifié **en le jouant**, par programme : les deux chemins de la vérification
(juste du premier coup / deux erreurs), l'ouverture du rattrapage, la réponse
donnée au second essai seulement, la reprise après rechargement, et les
événements du journal.

## Prochaine étape

Les **seize écrans qui restent**, et les sept types d'écran qu'ils demandent.
