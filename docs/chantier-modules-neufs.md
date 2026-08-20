# Chantier des modules neufs — niveau 4

Journal d'avancement, tenu à jour à chaque étape. **Après une interruption,
c'est ce fichier qui dit où reprendre.**

Méthode : skill `module-neuf` (`~/.claude/skills/module-neuf/`).
Mandat d'autonomie du 20 août 2026 : numérotation séquentielle, médias
générés, poussé en production au fur et à mesure.

Les six étapes par module : **cadrer · inventer · contenu · build · médias ·
livrer**.

| N° | Slug | Situation | Étape atteinte |
|----|------|-----------|----------------|
| 11 | `module-relations` | Relations sociales | contenu ✔ · build ✔ · médias… |
| 12 | `module-deplacement` | Déplacement dans une ville | — |
| 13 | `module-activite` | Participation à une activité culturelle ou sportive | — |
| 14 | `module-alimentation` | Achat d'aliments ou de produits d'entretien | — |
| 15 | `module-achat` | Achat de biens de consommation durables | — |
| 16 | `module-restaurant` | Service de restauration | — |
| 18 | `module-vetements` | Achat de vêtements | — |

Le 17 est pris par `module-banque`, d'où le saut.

## Module 11 — Relations sociales

- **Scénario** : Mariama (Guinée, arrivée il y a 14 mois) rejoint la ligue de
  volleyball du centre communautaire et se lie avec Chantal. Fatou, la sœur
  restée au pays, annonce une naissance.
- **Sections** : Je découvre (au vestiaire) · Défi 1 · Ce que je fais de mes
  semaines · Défi 2 · Ce que j'ai vécu · Défi 3 · Donner des nouvelles ·
  Je me lance.
- **Grammaire** : accent d'insistance · pronoms relatifs qui/que/où ·
  imparfait et passé composé · y et là · la carte postale et la carte de vœux ·
  grâce à / à cause de. Aucun de ces six points n'est déjà traité dans les
  onze modules existants — vérifié en relevant les titres de toutes les
  mini-leçons produites.
- **Couleur** : teal `#0D7A6F` / `#DCF2EF` (rotation à cinq couleurs du
  projet). **Activité** : 48.

### Fait

- Jeu de rôle : le serveur n'acceptait que la paire de rôles
  locataire/propriétaire, écrite en dur à trois endroits. Généralisée aux
  rôles déclarés par le scénario, plus une clé `adresse` pour qu'un échange
  informel se tutoie. Les deux scénarios existants produisent une consigne
  système **identique au caractère près** (346 lignes comparées).

- Contenu écrit : 7 dialogues (86 répliques), 15 mots de vocabulaire,
  25 exercices, 7 mini-leçons (34 combinaisons de laboratoire), 18 phrases
  porteuses. Module construit : 285 776 octets.
- Le gabarit a gagné un vingt-et-unième jeton, `%%JR_ROLE%%` : le rôle de
  départ du jeu de rôle était écrit en dur (`role:'locataire'`) et aurait
  envoyé un rôle inexistant au serveur. `module-probleme` se reconstruit
  toujours à l'octet près (md5 inchangé).
- Vérifié dans le navigateur : 6 sections rendues sans erreur, 25 exercices,
  les 7 mini-leçons s'ouvrent, **34 combinaisons de laboratoire toutes
  pourvues**, aucune clé de `PLUS` orpheline, aucun dialogue inutilisé ni
  manquant, 95 identifiants d'audio relevés.
- Une faute de fabrication attrapée là : une virgule doublée dans
  `dialogues.js`, produite par le script d'ajout du septième dialogue. Elle
  cassait tout le script de la page — et la page continuait de s'afficher,
  muette. Le contrôle utile n'est pas « la page s'affiche » mais « les
  constantes existent ».
- **Médias faits.** 21 images (fal.ai / Nano Banana 2, 0,71 $) : huit
  illustrations d'exercice à 1024 px et treize photos de vocabulaire réduites à
  800 px / qualité 82. 213 MP3 (ElevenLabs) : 82 répliques sur sept dialogues
  et 131 mots, phrases et mini-leçons. Contrôle : les **213 URL d'audio et les
  22 URL d'images que la page peut demander répondent toutes** — aucune n'est
  manquante.
- Le générateur d'audio de ce module **ne recopie plus les dialogues** : il lit
  `build/contenu/module-relations/dialogues.js`. Les générateurs précédents en
  gardaient une copie, qui divergeait du module à la première correction.
- Nouvel outil : `build/collecte_sons.py`. Le relevé des identifiants d'audio
  se collait jusqu'ici à la main depuis la console du navigateur ; il est
  maintenant reçu directement et écrit dans `sons_<slug>.json`.
- Piège aligné juste à temps : le calcul du nom de fichier d'une réplique doit
  reproduire `charSlug()` du moteur **au caractère près**. Une expression
  régulière « propre » aurait écrit `jean_philippe` là où le moteur demande
  `jean-philippe`.
