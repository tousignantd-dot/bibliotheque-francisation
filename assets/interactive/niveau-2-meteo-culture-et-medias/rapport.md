# RAPPORT DE PRODUCTION

**Commande :** activité de francisation, niveau 2 (LAN-2029-4 « Des mots de tous les jours »),
compréhension orale et production orale, 30 min, en dyade.
**Thématique :** Culture et médias · la météo · qu'est-ce qu'une tornade.

---

## CE QUE J'AI PRODUIT

| Fichier | Contenu |
|---|---|
| `activite.html` | Page interactive autonome, ouvrable par double-clic. Un seul fichier : le système de design de la bibliothèque (jetons + composants) y est recopié tel quel, aucune feuille de style inventée. |
| `fiche-eleve.html` + `.pdf` | Fiche élève imprimable, format lettre, noir et blanc. Hiérarchie portée par la graisse et les filets horizontaux. Aucune couleur. |
| `corrige.html` + `.pdf` | Corrigé, fichier distinct. Question par question, dans l'ordre exact de l'énoncé, avec le passage du texte qui justifie chaque réponse. |
| `notes-enseignant.html` + `.pdf` | Consignes de passation, minutage détaillé, points de langue, aide au déblocage, évaluation. |
| 21 fichiers `.mp3` | Voix enregistrées, à côté de la page, appelées en liens relatifs. |
| `generer_audio.py`, `textes.py` | Le script qui a produit les MP3, gardé pour permettre de les régénérer. |

### Structure de l'activité (30 min exactement)

Les mots de la tornade (5) · Ex. 1 le bon mot (4) · Ex. 2 le bulletin (7) ·
Ex. 3 le dialogue (6) · Ex. 4 les phrases (4) · Ex. 5 je parle en dyade (4) = **30 min**.

Les exercices 1 à 4 valent 21 points et se corrigent seuls à l'écran, avec rétroaction
immédiate : « ✓ Juste » ou « ✕ La bonne réponse est … ». L'exercice 5 est la production
orale en dyade ; il n'est pas noté et porte une liste d'auto-vérification.

### Audio

Toutes les voix sont enregistrées (synthèse vocale ElevenLabs, `eleven_multilingual_v2`) :
8 mots isolés (voix ralentie à 85 % pour le stade débutant), le bulletin de météo lu par
une voix de météorologue, et le dialogue Nadia–Marc en deux voix distinctes — assemblé en
un fichier suivi (`dialogue.mp3`) et gardé aussi phrase par phrase, pour la réécoute
ligne à ligne dans la transcription. Aucun bouton muet.

### Vérifications faites avant de livrer

- Chaque question du corrigé a été relue contre son énoncé : même ordre, même formulation,
  réponse trouvable dans le bulletin ou le dialogue, jamais ailleurs.
- Exercice 4 : chaque trou n'accepte qu'un seul mot de la banque. Les cinq autres mots ont
  été testés dans chaque phrase — genre, nombre et sens en écartent toujours cinq sur six.
- Le total des minutages (5 + 4 + 7 + 6 + 4 + 4) donne bien 30 min.
- Le total des points (6 + 5 + 4 + 6) donne bien 21.
- Tous les liens `.mp3` de la page pointent vers un fichier qui existe dans le dossier.
- Contenu entièrement original : aucun extrait de manuel.

---

## AJOUTÉ APRÈS COUP

Les trois imprimés avaient d'abord été livrés en markdown. Ils ont été remis en page
en HTML d'impression puis convertis en PDF format lettre (612 × 792 pt) par
`programme/outils/fiche_pdf.py`, et les versions `.md` ont été supprimées pour
qu'il n'en subsiste qu'une seule version. Les renvois des notes de passation, qui
désignaient encore `activite.md` et `corrige.md`, pointent maintenant vers les PDF.

---

## CE QUE JE N'AI PAS PU FAIRE

- **Aucune image n'a été produite.** Le système de design de la bibliothèque proscrit
  l'illustration décorative, et la commande n'en demandait aucune. La compétence `generate`
  n'a donc pas été appelée, et rien n'a été écrit dans `/Users/danieltousignant/Claude/generations`.
- **Les voix sont synthétiques, pas humaines.** C'est la seule voix enregistrée disponible
  ici (clé ElevenLabs du projet, mêmes voix que les autres modules de la bibliothèque).
- **La police Nunito se charge depuis Google Fonts.** Ouverte hors ligne, la page reste
  entièrement lisible mais tombe sur la police système. C'est le seul lien distant du fichier.
- **Aucun résultat n'est envoyé à l'enseignant.** La page est autonome, sans serveur : le
  score s'affiche à l'écran et doit être noté avant de fermer la page.

Pour le reste de la commande : rien à signaler.
