# Bibliothèque Francisation

Bibliothèque d'activités pédagogiques FLS (Niveau 4) pour enseignant en francisation au Québec. Serveur Python simple (`server.py`, stdlib seulement) + fichiers statiques HTML.

## Déploiement (Railway)

- Push sur `main` → redéploiement automatique sur Railway
  (https://bibliotheque-francisation-production.up.railway.app)
- **Python épinglé à 3.12** via `.python-version` — le module `cgi` utilisé par server.py a été supprimé en Python 3.13. Ne pas retirer ce fichier.
- Builder : Railpack (`railway.toml`) — ne pas remettre Nixpacks (buggé).
- Healthcheck : `/api/activities`. `init_storage()` tourne en arrière-plan au démarrage pour ne pas bloquer le healthcheck.

## Flux de travail important

- Quand l'utilisateur ajoute des fichiers via **admin.html en local**, ils arrivent dans le working tree mais ne sont PAS en ligne tant qu'on n'a pas fait `git add + commit + push`. « Mettre en ligne » = pousser sur main.
- Le serveur Railway utilise un **volume persistant** (`STORAGE_DIR`). Les fichiers `assets/interactive/` sont servis depuis le code (BASE_DIR) ; les autres assets uploadés depuis le volume. Au démarrage, `init_storage()` resynchronise les chemins des activités intégrées au code dans le volume (les dates saisies par l'utilisateur sont préservées).

## Règles sur les fichiers

- **Jamais d'espaces ni de parenthèses** dans les noms de fichiers (ex. `Fichier (1).html` → renommer en kebab-case). Ça casse le build/les URLs.
- Fichiers interactifs HTML : viser < 1 Mo. Les exports « bundler » de ~4 Mo avec assets en base64 font planter le navigateur (FILE_ERROR_NO_SPACE).
- Chaque activité dans `data/activities.json` : vérifier que `interactive`, `studentDoc`, `planCours` pointent vers des fichiers existants. Valider le JSON avant de pousser : `python3 -c "import json; json.load(open('data/activities.json'))"`.

## Correction assistée par IA (« Corrige-moi ! »)

- `assets/interactive/corrige-moi/` appelle `/api/correct-french` (server.py), qui relaie vers l'API Anthropic (modèle `claude-haiku-4-5-20251001`) pour corriger une phrase d'élève.
- Nécessite la variable d'environnement `ANTHROPIC_API_KEY` sur Railway (Variables). Sans elle, l'endpoint répond 503 proprement (pas de crash).
- Le serveur tourne en **multi-thread** (`ThreadingMixIn`) depuis l'ajout de cet appel réseau, pour ne pas bloquer les autres élèves pendant un appel API.
- `viewer.html` relaie le `code` élève à l'iframe via `?code=...` sur l'URL de l'activité — nécessaire pour que l'activité authentifie ses appels à `/api/correct-french`.
- Ne jamais coder la clé API en dur dans le code ou la partager dans le chat.

## Structure

- `data/activities.json` — métadonnées des activités (source de vérité côté code)
- `assets/documents/` — fiches élèves (HTML imprimables)
- `assets/interactive/<slug>/` — activités interactives (HTML autonomes)
- `assets/plans/` — plans de cours
- `admin.html` / `eleve.html` — interfaces enseignant / élève

## Langue

Répondre en français à l'utilisateur.
