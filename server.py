"""
Serveur — Bibliothèque d'activités pédagogiques
Gère les fichiers statiques + les opérations d'administration (ajout, modification, suppression).
"""

import http.server
import json
import mimetypes
import os
import shutil
import cgi
import urllib.parse
import urllib.request
import urllib.error
import unicodedata
import re
import zipfile
import io
import random
import string
from pathlib import Path
from datetime import date, datetime, timedelta

BASE_DIR = Path(__file__).parent.resolve()

# STORAGE_DIR : répertoire persistant (volume Railway en production, BASE_DIR en local)
_storage_raw = os.environ.get('STORAGE_DIR', str(BASE_DIR))
# Valider que STORAGE_DIR est un chemin absolu simple (pas de '=' parasite)
if '=' in _storage_raw or not os.path.isabs(_storage_raw):
    print(f"[WARN] STORAGE_DIR invalide ({_storage_raw!r}), repli sur BASE_DIR", flush=True)
    STORAGE_DIR = BASE_DIR
else:
    STORAGE_DIR = Path(_storage_raw)

DATA_FILE       = STORAGE_DIR / "data" / "activities.json"
STUDENTS_FILE   = STORAGE_DIR / "data" / "students.json"
ACCESS_LOG_FILE = STORAGE_DIR / "data" / "access_log.json"
PROGRESS_FILE   = STORAGE_DIR / "data" / "progress.json"
VOCAB_PROGRESS_FILE = STORAGE_DIR / "data" / "vocab_progress.json"

PORT = int(os.environ.get('PORT', 5173))


# ── Initialisation du stockage ──────────────────────────────────────────────

def init_storage():
    """Crée les répertoires nécessaires et migre les données initiales si besoin."""
    if STORAGE_DIR == BASE_DIR:
        return

    data_dst = STORAGE_DIR / "data"
    assets_dst = STORAGE_DIR / "assets"

    # Première exécution : copier data/ depuis BASE_DIR
    if not data_dst.exists():
        src = BASE_DIR / "data"
        if src.exists():
            shutil.copytree(str(src), str(data_dst))
        else:
            data_dst.mkdir(parents=True)

    # Première exécution : copier assets/ depuis BASE_DIR (sauf interactive/)
    if not assets_dst.exists():
        src = BASE_DIR / "assets"
        if src.exists():
            shutil.copytree(str(src), str(assets_dst))
        else:
            assets_dst.mkdir(parents=True)

    data_dst.mkdir(parents=True, exist_ok=True)
    assets_dst.mkdir(parents=True, exist_ok=True)

    # Toujours synchroniser assets/interactive/ depuis BASE_DIR à chaque démarrage
    # (les fichiers interactifs évoluent avec chaque déploiement)
    src_interactive = BASE_DIR / "assets" / "interactive"
    dst_interactive = STORAGE_DIR / "assets" / "interactive"
    if src_interactive.exists():
        if dst_interactive.exists():
            shutil.rmtree(str(dst_interactive))
        shutil.copytree(str(src_interactive), str(dst_interactive))

    # Fusionner les activités intégrées au code dans le volume :
    #  - les ids présents dans git mais absents du volume sont ajoutés ;
    #  - pour les ids présents dans les deux, les chemins de fichiers et
    #    métadonnées définis dans le code font autorité (ils évoluent avec
    #    chaque déploiement), tandis que les dates saisies par l'utilisateur
    #    dans le volume sont préservées.
    src_acts = BASE_DIR / "data" / "activities.json"
    dst_acts = STORAGE_DIR / "data" / "activities.json"
    # Champs dont le volume (choix de l'utilisateur) fait autorité
    USER_FIELDS = ("dateVue", "datePrevue", "dateFin")
    if src_acts.exists() and dst_acts.exists():
        try:
            with open(src_acts, encoding="utf-8") as f:
                builtin = json.load(f)
            with open(dst_acts, encoding="utf-8") as f:
                current = json.load(f)
            current_by_id = {a["id"]: a for a in current}
            changed = False
            merged = []
            for a in builtin:
                vol = current_by_id.get(a["id"])
                if vol is None:
                    # Nouvelle activité : ajout intégral depuis le code
                    merged.append(a)
                    changed = True
                else:
                    # Activité existante : le code fait autorité, sauf les
                    # dates saisies par l'utilisateur qui sont conservées.
                    entry = dict(a)
                    for field in USER_FIELDS:
                        if vol.get(field):
                            entry[field] = vol[field]
                    if entry != vol:
                        changed = True
                    merged.append(entry)
            # Préserver les activités du volume absentes du code (créées via admin)
            builtin_ids = {a["id"] for a in builtin}
            for a in current:
                if a["id"] not in builtin_ids:
                    merged.append(a)
            if changed:
                with open(dst_acts, "w", encoding="utf-8") as f:
                    json.dump(merged, f, ensure_ascii=False, indent=2)
                print("[init] activities.json du volume resynchronisé avec le code", flush=True)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"[WARN] Fusion activities.json échouée : {e}", flush=True)

    # Synchroniser les fichiers ajoutés au code (fiches, plans, diaporamas,
    # vignettes, autres) sans écraser les uploads faits depuis l'admin en
    # production. Sans ceci, un fichier ajouté par git dans ces dossiers reste
    # invisible tant que le volume Railway existe déjà (le copytree initial
    # à la ligne ~60 ne s'exécute qu'à la toute première création du volume).
    for subdir in ("thumbnails", "documents", "slideshows", "plans", "autres"):
        src_dir = BASE_DIR / "assets" / subdir
        dst_dir = STORAGE_DIR / "assets" / subdir
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        for f in src_dir.iterdir():
            if f.is_file() and not (dst_dir / f.name).exists():
                shutil.copy2(str(f), str(dst_dir / f.name))


# ── Helpers données ─────────────────────────────────────────────────────────

def load_activities():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_activities(activities):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)


def load_students():
    if STUDENTS_FILE.exists():
        with open(STUDENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_students(students):
    STUDENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STUDENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=2)


def load_access_log():
    if ACCESS_LOG_FILE.exists():
        with open(ACCESS_LOG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_access_log(log):
    ACCESS_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ACCESS_LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)


def load_progress():
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_progress(data):
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_available_activity_ids():
    today_str = date.today().isoformat()
    ids = set()
    for a in load_activities():
        dp = a.get("datePrevue", "")
        df = a.get("dateFin", "")
        if df and df < today_str:
            continue
        if not dp or dp <= today_str:
            ids.add(a["id"])
    return ids


def get_student_vocab_pool():
    """Ne garde que les mots liés aux activités déjà accessibles à l'élève."""
    available_ids = get_available_activity_ids()
    return [
        w for w in VOCAB_BANK
        if not w.get("activityIds") or available_ids & set(w["activityIds"])
    ]


def load_vocab_progress():
    if VOCAB_PROGRESS_FILE.exists():
        with open(VOCAB_PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_vocab_progress(data):
    VOCAB_PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(VOCAB_PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Boîtes de répétition espacée (système Leitner) : plus la boîte est haute,
# plus l'intervalle avant la prochaine révision est grand.
VOCAB_INTERVALS_DAYS = [0, 1, 3, 7, 14, 30, 60]

VOCAB_BANK = [
    {"id": "w1", "activityIds": [4, 8, 17],  "mot": "un rendez-vous", "domaine": "Santé", "definition": "Un moment fixé à l'avance pour voir quelqu'un.", "exemple": "J'ai un rendez-vous à dix heures avec le docteur."},
    {"id": "w2", "activityIds": [4, 8, 17],  "mot": "la salle d'attente", "domaine": "Santé", "definition": "L'endroit où on attend avant de voir le médecin.", "exemple": "Prenez un siège dans la salle d'attente."},
    {"id": "w3", "activityIds": [4, 8, 17],  "mot": "la carte d'assurance maladie", "domaine": "Santé", "definition": "Le document qui donne accès aux soins de santé gratuits au Québec.", "exemple": "Avez-vous votre carte d'assurance maladie avec vous ?"},
    {"id": "w4", "activityIds": [4, 8, 17],  "mot": "tousser", "domaine": "Santé", "definition": "Faire un bruit sec avec la gorge à cause d'une irritation.", "exemple": "Est-ce que vous toussez beaucoup ?"},
    {"id": "w5", "activityIds": [4, 8, 17],  "mot": "un sirop", "domaine": "Santé", "definition": "Un médicament liquide et sucré.", "exemple": "Je vais vous prescrire un sirop pour la gorge."},
    {"id": "w6", "activityIds": [4, 8, 17],  "mot": "un antibiotique", "domaine": "Santé", "definition": "Un médicament qui combat une infection.", "exemple": "Le docteur m'a mis sous antibiotique."},
    {"id": "w7", "activityIds": [4, 8, 17],  "mot": "la fièvre", "domaine": "Santé", "definition": "Une température du corps plus élevée que la normale.", "exemple": "Vous n'avez pas de fièvre."},
    {"id": "w8", "activityIds": [4, 8, 17],  "mot": "empirer", "domaine": "Santé", "definition": "Devenir pire.", "exemple": "J'ai peur que ma toux empire."},
    {"id": "w9", "activityIds": [4, 8, 17],  "mot": "un symptôme", "domaine": "Santé", "definition": "Un signe qui indique une maladie.", "exemple": "Quels sont vos symptômes ?"},
    {"id": "w10", "activityIds": [4, 8, 17], "mot": "un spécialiste", "domaine": "Santé", "definition": "Un médecin expert dans un domaine précis.", "exemple": "Le médecin m'a référé à un spécialiste."},
    {"id": "w11", "activityIds": [4, 8, 17], "mot": "la prévention", "domaine": "Santé", "definition": "Les actions pour éviter une maladie.", "exemple": "La prévention est importante pour rester en santé."},
    {"id": "w12", "activityIds": [5, 7], "mot": "fraîches", "domaine": "Consommation", "definition": "Récemment récoltées ou préparées, pas vieilles.", "exemple": "Les fraises sont très fraîches."},
    {"id": "w13", "activityIds": [5, 7], "mot": "un rabais", "domaine": "Consommation", "definition": "Une réduction de prix.", "exemple": "Les fraises sont en rabais cette semaine."},
    {"id": "w14", "activityIds": [5, 7], "mot": "un produit local", "domaine": "Consommation", "definition": "Un aliment cultivé ou fabriqué dans la région.", "exemple": "Ce sont des produits locaux du Québec."},
    {"id": "w15", "activityIds": [5, 7], "mot": "un kilo", "domaine": "Consommation", "definition": "Une unité de poids (1000 grammes).", "exemple": "Je prends un kilo de pommes."},
    {"id": "w16", "activityIds": [7], "mot": "le réfrigérateur", "domaine": "Consommation", "definition": "L'appareil qui garde les aliments au froid.", "exemple": "Gardez-les au réfrigérateur."},
    {"id": "w17", "activityIds": [6], "mot": "le fromage en grains", "domaine": "Consommation", "definition": "Un fromage frais utilisé dans la poutine.", "exemple": "La poutine, c'est des frites, du fromage en grains et de la sauce."},
    {"id": "w18", "activityIds": [5], "mot": "un kiosque", "domaine": "Consommation", "definition": "Un petit comptoir de vente au marché.", "exemple": "On peut parler avec les gens aux kiosques du marché."},
    {"id": "w19", "activityIds": [11, 16], "mot": "le loyer", "domaine": "Logement", "definition": "Le montant payé chaque mois pour habiter un logement.", "exemple": "Le loyer est de 950 $ par mois."},
    {"id": "w20", "activityIds": [11, 16], "mot": "un quatre et demi", "domaine": "Logement", "definition": "Un appartement avec quatre pièces plus la salle de bain.", "exemple": "C'est un beau quatre et demi."},
    {"id": "w21", "activityIds": [11, 16], "mot": "le bail", "domaine": "Logement", "definition": "Le contrat de location d'un logement.", "exemple": "J'ai signé le bail hier."},
    {"id": "w22", "activityIds": [11, 16], "mot": "le chauffage", "domaine": "Logement", "definition": "Le système qui réchauffe un logement.", "exemple": "Le chauffage ne fonctionne plus."},
    {"id": "w23", "activityIds": [11, 16], "mot": "un dépôt", "domaine": "Logement", "definition": "Une somme d'argent versée en garantie.", "exemple": "Le propriétaire demande un dépôt."},
    {"id": "w24", "activityIds": [11, 16], "mot": "déménager", "domaine": "Logement", "definition": "Changer de logement.", "exemple": "Je déménage la semaine prochaine."},
    {"id": "w25", "activityIds": [11, 16], "mot": "les meubles", "domaine": "Logement", "definition": "Les objets comme une table, un lit, une chaise.", "exemple": "On a acheté de nouveaux meubles."},
    {"id": "w26", "activityIds": [12], "mot": "une tâche", "domaine": "Monde du travail", "definition": "Un travail précis à faire.", "exemple": "Voici tes tâches pour aujourd'hui."},
    {"id": "w27", "activityIds": [12], "mot": "un superviseur", "domaine": "Monde du travail", "definition": "La personne qui dirige les employés.", "exemple": "Mon superviseur m'a expliqué mon horaire."},
    {"id": "w28", "activityIds": [12], "mot": "un horaire", "domaine": "Monde du travail", "definition": "La liste des heures de travail.", "exemple": "Est-ce qu'il y a une pause dans mon horaire ?"},
    {"id": "w29", "activityIds": [12], "mot": "accueillir", "domaine": "Monde du travail", "definition": "Recevoir quelqu'un avec politesse.", "exemple": "Tu accueilles les clients à la porte."},
    {"id": "w30", "activityIds": [12], "mot": "une pause", "domaine": "Monde du travail", "definition": "Un moment de repos pendant le travail.", "exemple": "Il y a une pause à dix heures."},
    {"id": "w31", "activityIds": [13], "mot": "une équipe", "domaine": "Loisirs", "definition": "Un groupe de personnes qui jouent ensemble.", "exemple": "Je joue au hockey en équipe."},
    {"id": "w32", "activityIds": [13], "mot": "individuel", "domaine": "Loisirs", "definition": "Qui se pratique seul.", "exemple": "La natation est un sport individuel."},
    {"id": "w33", "activityIds": [13], "mot": "disputer un match", "domaine": "Loisirs", "definition": "Jouer une partie sportive.", "exemple": "On dispute un match tous les samedis."},
    {"id": "w34", "activityIds": [14], "mot": "le métro", "domaine": "Vie citoyenne — orientation", "definition": "Un train souterrain de transport en commun.", "exemple": "Vous prenez la ligne verte du métro."},
    {"id": "w35", "activityIds": [14], "mot": "une correspondance", "domaine": "Vie citoyenne — orientation", "definition": "Un changement de ligne de métro ou d'autobus.", "exemple": "À Berri-UQAM, vous faites une correspondance."},
    {"id": "w36", "activityIds": [14], "mot": "une station", "domaine": "Vie citoyenne — orientation", "definition": "Un arrêt de métro.", "exemple": "Descendez à la station Champ-de-Mars."},
    {"id": "w37", "activityIds": [9], "mot": "un belvédère", "domaine": "Culture / histoire", "definition": "Un endroit en hauteur pour admirer la vue.", "exemple": "Du belvédère, on voit toute la ville."},
    {"id": "w38", "activityIds": [18], "mot": "un explorateur", "domaine": "Culture / histoire", "definition": "Une personne qui découvre de nouveaux lieux.", "exemple": "Jacques Cartier était un explorateur."},
    {"id": "w39", "activityIds": [9, 15], "mot": "le fleuve", "domaine": "Culture / histoire", "definition": "Un grand cours d'eau qui se jette dans la mer.", "exemple": "On voit le fleuve Saint-Laurent."},
    {"id": "w40", "activityIds": [15], "mot": "une croisière", "domaine": "Culture / loisirs", "definition": "Une promenade en bateau.", "exemple": "Il y a une croisière sur le fleuve."},
    {"id": "w41", "activityIds": [15], "mot": "un pédalo", "domaine": "Culture / loisirs", "definition": "Un petit bateau à pédales.", "exemple": "On peut faire du pédalo au Vieux-Port."},
    {"id": "w42", "activityIds": [15], "mot": "un spectacle", "domaine": "Culture / loisirs", "definition": "Une présentation artistique devant un public.", "exemple": "Le Cirque du Soleil présente un nouveau spectacle."},
    {"id": "w43", "activityIds": [10], "mot": "une exposition", "domaine": "Culture / histoire", "definition": "Une présentation d'objets à voir dans un musée.", "exemple": "Il y a une nouvelle exposition au musée."},
    {"id": "w44", "activityIds": [10], "mot": "un athlète", "domaine": "Culture / histoire", "definition": "Une personne qui pratique un sport de haut niveau.", "exemple": "L'athlète a gagné une médaille."},
    {"id": "w45", "activityIds": [10], "mot": "une médaille", "domaine": "Culture / histoire", "definition": "Une récompense donnée aux gagnants d'une compétition.", "exemple": "Il a gagné la médaille d'argent."},
    {"id": "w46", "activityIds": [10], "mot": "un exploit", "domaine": "Culture / histoire", "definition": "Une action remarquable et difficile à réaliser.", "exemple": "L'exposition présente un grand exploit sportif."},
    {"id": "w47", "activityIds": [18], "mot": "une basilique", "domaine": "Culture / histoire", "definition": "Une très grande église importante.", "exemple": "La basilique Notre-Dame est magnifique."},
    {"id": "w48", "activityIds": [18], "mot": "pavée", "domaine": "Culture / histoire", "definition": "Couverte de pierres, en parlant d'une rue.", "exemple": "Les rues du Vieux-Montréal sont pavées."},
    {"id": "w49", "activityIds": [15], "mot": "un attrait", "domaine": "Culture / loisirs", "definition": "Un lieu ou une chose qui attire les visiteurs.", "exemple": "Le Vieux-Port est un attrait touristique."},
    {"id": "w50", "activityIds": [18], "mot": "fonder", "domaine": "Culture / histoire", "definition": "Créer une ville ou une organisation pour la première fois.", "exemple": "Montréal a été fondée en 1642."},
]


def generate_code(existing_codes):
    chars = [c for c in string.ascii_uppercase + string.digits if c not in "OI01"]
    for _ in range(100):
        code = ''.join(random.choices(chars, k=6))
        if code not in existing_codes:
            return code
    return ''.join(random.choices(chars, k=8))


def validate_student_code(code):
    for s in load_students():
        if s.get("code") == code:
            return s
    return None


def next_id(activities):
    return max((a["id"] for a in activities), default=0) + 1


def slugify(text):
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:60]


def safe_filename(filename):
    name = Path(filename).name
    name = re.sub(r'[/\\:*?"<>|]', '_', name)
    name = name.lstrip('.')
    return name or "fichier"


def json_response(handler, data, status=200):
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)


# ── Gestionnaire HTTP ────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        pass  # silencieux

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        if path == "/api/debug":
            import os as _os
            interactive_dir = BASE_DIR / "assets" / "interactive"
            files = []
            if interactive_dir.exists():
                for root, dirs, fs in _os.walk(str(interactive_dir)):
                    for f in fs:
                        files.append(_os.path.join(root, f).replace(str(BASE_DIR), ''))
            json_response(self, {
                "BASE_DIR": str(BASE_DIR),
                "STORAGE_DIR": str(STORAGE_DIR),
                "interactive_exists": interactive_dir.exists(),
                "files": files[:20],
            })
            return
        if path == "/api/activities":
            json_response(self, load_activities())
            return
        if path == "/api/student/activities":
            self._handle_student_activities(params)
            return
        if path == "/api/student/dashboard":
            self._handle_student_dashboard(params)
            return
        if path == "/api/vocab/session":
            self._handle_vocab_session(params)
            return
        if path == "/api/admin/students":
            json_response(self, load_students())
            return
        if path == "/api/admin/access-log":
            json_response(self, load_access_log())
            return
        if path == "/api/admin/progress":
            json_response(self, load_progress())
            return

        # Fichiers interactifs intégrés au code : servir directement depuis BASE_DIR
        if path.startswith("/assets/interactive/"):
            super().do_GET()
            return

        # Autres assets uploadés (thumbnails, docs, slideshows) : servir depuis STORAGE_DIR
        if STORAGE_DIR != BASE_DIR and path.startswith("/assets/"):
            self._serve_from_storage(path)
            return

        super().do_GET()

    def _serve_from_storage(self, url_path):
        rel = url_path.lstrip("/")
        file_path = STORAGE_DIR / rel
        # Fallback vers BASE_DIR si le fichier n'est pas dans le volume (assets intégrés au déploiement)
        if not file_path.exists() or not file_path.is_file():
            file_path = BASE_DIR / rel
        if not file_path.exists() or not file_path.is_file():
            self.send_error(404)
            return
        mime = mimetypes.guess_type(str(file_path))[0] or "application/octet-stream"
        data = file_path.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/auth":
            self._handle_auth()
        elif path == "/api/student/access":
            self._handle_log_access()
        elif path == "/api/admin/students":
            self._handle_add_student()
        elif path == "/api/admin/clear-log":
            save_access_log([])
            json_response(self, {"success": True})
        elif path == "/api/student/progress":
            self._handle_student_progress()
        elif path == "/api/correct-french":
            self._handle_correct_french()
        elif path == "/api/correct-email":
            self._handle_correct_email()
        elif path == "/api/vocab/answer":
            self._handle_vocab_answer()
        elif path == "/api/vocab/translate":
            self._handle_vocab_translate()
        elif path == "/api/vocab/check-answer":
            self._handle_vocab_check_answer()
        elif path == "/api/activities":
            self._handle_add()
        elif re.match(r"^/api/activities/\d+/update$", path):
            activity_id = int(path.split("/")[3])
            self._handle_update(activity_id)
        elif re.match(r"^/api/activities/\d+/dates$", path):
            activity_id = int(path.split("/")[3])
            self._handle_dates(activity_id)
        elif re.match(r"^/api/activities/\d+/clear-file$", path):
            activity_id = int(path.split("/")[3])
            self._handle_clear_file(activity_id)
        elif re.match(r"^/api/activities/\d+/rename$", path):
            activity_id = int(path.split("/")[3])
            self._handle_rename(activity_id)
        else:
            self.send_error(404)

    def do_PATCH(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        if re.match(r"^/api/admin/students/\d+$", path):
            try:
                student_id = int(path.split("/")[4])
                length = int(self.headers.get("Content-Length", 0))
                body = json.loads(self.rfile.read(length)) if length else {}
                students = load_students()
                for s in students:
                    if s["id"] == student_id:
                        if "prenom" in body:
                            s["prenom"] = body["prenom"]
                        break
                save_students(students)
                json_response(self, {"success": True})
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
        else:
            self.send_error(404)

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if re.match(r"^/api/admin/students/\d+$", path):
            try:
                student_id = int(path.split("/")[4])
                self._handle_delete_student(student_id)
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
        elif re.match(r"^/api/activities/\d+$", path):
            try:
                activity_id = int(path.split("/")[3])
                self._handle_delete(activity_id)
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
        else:
            self.send_error(404)

    # ── Multipart ──────────────────────────────────────────────────────────

    def _parse_multipart(self):
        content_type = self.headers.get("Content-Type", "")
        if "multipart/form-data" not in content_type:
            return None
        content_length = self.headers.get("Content-Length", "0")
        return cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={
                "REQUEST_METHOD": "POST",
                "CONTENT_TYPE": content_type,
                "CONTENT_LENGTH": content_length,
            },
        )

    # ── Upload ─────────────────────────────────────────────────────────────

    def _upload_thumbnail(self, form, slug):
        if "thumbnail" not in form or not form["thumbnail"].filename:
            return ""
        f = form["thumbnail"]
        ext = Path(f.filename).suffix.lower()
        dest = STORAGE_DIR / "assets" / "thumbnails" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/thumbnails/{slug}{ext}"

    def _upload_interactive(self, form, slug):
        if "interactive" not in form or not form["interactive"].filename:
            return ""
        f = form["interactive"]
        ext = Path(f.filename).suffix.lower()
        dest_dir = STORAGE_DIR / "assets" / "interactive" / slug
        dest_dir.mkdir(parents=True, exist_ok=True)
        if ext == ".zip":
            with zipfile.ZipFile(io.BytesIO(f.file.read())) as zf:
                zf.extractall(dest_dir)
            return f"assets/interactive/{slug}/index.html"
        else:
            safe_name = safe_filename(f.filename)
            dest = dest_dir / safe_name
            dest.write_bytes(f.file.read())
            return f"assets/interactive/{slug}/{safe_name}"

    def _upload_doc(self, form, slug):
        if "studentDoc" not in form or not form["studentDoc"].filename:
            return ""
        f = form["studentDoc"]
        ext = Path(f.filename).suffix.lower()
        dest = STORAGE_DIR / "assets" / "documents" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/documents/{slug}{ext}"

    def _upload_slideshow(self, form, slug):
        if "slideshow" not in form or not form["slideshow"].filename:
            return ""
        f = form["slideshow"]
        ext = Path(f.filename).suffix.lower()
        dest = STORAGE_DIR / "assets" / "slideshows" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/slideshows/{slug}{ext}"

    def _upload_plan_cours(self, form, slug):
        if "planCours" not in form or not form["planCours"].filename:
            return ""
        f = form["planCours"]
        safe_name = safe_filename(f.filename)
        dest = STORAGE_DIR / "assets" / "plans" / safe_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/plans/{safe_name}"

    def _upload_autres(self, form, slug):
        if "autres" not in form or not form["autres"].filename:
            return ""
        f = form["autres"]
        safe_name = safe_filename(f.filename)
        dest = STORAGE_DIR / "assets" / "autres" / safe_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/autres/{safe_name}"

    def _delete_file(self, rel_path, key=""):
        if not rel_path:
            return
        p = STORAGE_DIR / rel_path
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
        if key == "interactive":
            parent = p.parent
            if parent.exists() and parent != STORAGE_DIR / "assets" / "interactive":
                try:
                    parent.rmdir()
                except OSError:
                    pass

    # ── Handlers activités ────────────────────────────────────────────────

    def _handle_add(self):
        form = self._parse_multipart()
        if form is None:
            json_response(self, {"error": "multipart requis"}, 400)
            return

        title = form.getvalue("title", "").strip()
        if not title:
            json_response(self, {"error": "Titre requis"}, 400)
            return

        slug = slugify(title)
        activities = load_activities()
        new_id = next_id(activities)

        activity = {
            "id": new_id,
            "title": title,
            "level": "Niveau 4",
            "thumbnail": self._upload_thumbnail(form, slug),
            "interactive": self._upload_interactive(form, slug),
            "studentDoc": self._upload_doc(form, slug),
            "slideshow": self._upload_slideshow(form, slug),
            "planCours": self._upload_plan_cours(form, slug),
            "autres": self._upload_autres(form, slug),
            "keywords": [],
        }

        activities.append(activity)
        save_activities(activities)
        json_response(self, {"success": True, "activity": activity}, 201)

    def _handle_update(self, activity_id):
        form = self._parse_multipart()
        if form is None:
            json_response(self, {"error": "multipart requis"}, 400)
            return

        activities = load_activities()
        target = next((a for a in activities if a["id"] == activity_id), None)
        if not target:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        slug = slugify(target["title"])
        new_title = form.getvalue("title", "").strip()
        if new_title:
            target["title"] = new_title
            slug = slugify(new_title)

        new_thumb = self._upload_thumbnail(form, slug)
        if new_thumb:
            self._delete_file(target.get("thumbnail"))
            target["thumbnail"] = new_thumb

        new_interactive = self._upload_interactive(form, slug)
        if new_interactive:
            self._delete_file(target.get("interactive"), "interactive")
            target["interactive"] = new_interactive

        new_doc = self._upload_doc(form, slug)
        if new_doc:
            self._delete_file(target.get("studentDoc"))
            target["studentDoc"] = new_doc

        new_slideshow = self._upload_slideshow(form, slug)
        if new_slideshow:
            self._delete_file(target.get("slideshow"))
            target["slideshow"] = new_slideshow

        new_plan = self._upload_plan_cours(form, slug)
        if new_plan:
            self._delete_file(target.get("planCours"))
            target["planCours"] = new_plan

        new_autres = self._upload_autres(form, slug)
        if new_autres:
            self._delete_file(target.get("autres"))
            target["autres"] = new_autres

        save_activities(activities)
        json_response(self, {"success": True, "activity": target})

    def _handle_dates(self, activity_id):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))

        activities = load_activities()
        target = next((a for a in activities if a["id"] == activity_id), None)
        if not target:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        if "dateVue" in body:
            target["dateVue"] = body["dateVue"]
        if "datePrevue" in body:
            target["datePrevue"] = body["datePrevue"]
        if "dateFin" in body:
            target["dateFin"] = body["dateFin"]

        save_activities(activities)
        json_response(self, {"success": True})

    def _handle_clear_file(self, activity_id):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        field = body.get("field", "")

        allowed = ("thumbnail", "interactive", "studentDoc", "slideshow", "planCours", "autres")
        if field not in allowed:
            json_response(self, {"error": "Champ invalide"}, 400)
            return

        activities = load_activities()
        target = next((a for a in activities if a["id"] == activity_id), None)
        if not target:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        self._delete_file(target.get(field, ""), field)
        target[field] = ""
        save_activities(activities)
        json_response(self, {"success": True})

    def _handle_rename(self, activity_id):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        new_title = body.get("title", "").strip()

        if not new_title:
            json_response(self, {"error": "Titre requis"}, 400)
            return

        activities = load_activities()
        for a in activities:
            if a["id"] == activity_id:
                a["title"] = new_title
                save_activities(activities)
                json_response(self, {"success": True, "activity": a})
                return

        json_response(self, {"error": "Activité introuvable"}, 404)

    def _handle_delete(self, activity_id):
        activities = load_activities()
        target = next((a for a in activities if a["id"] == activity_id), None)

        if not target:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        for key in ("thumbnail", "interactive", "studentDoc", "slideshow", "planCours", "autres"):
            self._delete_file(target.get(key, ""), key)

        activities = [a for a in activities if a["id"] != activity_id]
        save_activities(activities)
        json_response(self, {"success": True})

    # ── Handlers élèves / LMS ─────────────────────────────────────────────

    def _handle_auth(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Code invalide"}, 401)
            return
        json_response(self, {
            "success": True,
            "studentId": student["id"],
            "label": student.get("label", ""),
            "prenom": student.get("prenom", ""),
        })

    def _handle_vocab_session(self, params):
        code = params.get("code", [""])[0].strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        domain = params.get("domain", [""])[0]
        try:
            n = max(1, min(30, int(params.get("n", ["10"])[0])))
        except ValueError:
            n = 10

        available_pool = get_student_vocab_pool()
        pool = [w for w in available_pool if not domain or w["domaine"] == domain]
        progress = load_vocab_progress()
        by_word = {
            p["wordId"]: p for p in progress if p["studentId"] == student["id"]
        }

        today = date.today().isoformat()
        due = []
        new = []
        for w in pool:
            p = by_word.get(w["id"])
            if p is None:
                new.append(w)
            elif p["dueDate"] <= today:
                due.append((p["box"], w))

        due.sort(key=lambda pair: pair[0])
        selected = [w for _, w in due[:n]]
        if len(selected) < n:
            selected += new[: n - len(selected)]
        random.shuffle(selected)

        json_response(self, {
            "cards": selected,
            "domaines": sorted(set(w["domaine"] for w in available_pool)),
            "dueCount": len(due),
            "newCount": len(new),
        })

    def _handle_vocab_answer(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        word_id = body.get("wordId", "")
        quality = body.get("quality", "")
        if quality not in ("encore", "difficile", "facile"):
            json_response(self, {"error": "Valeur invalide"}, 400)
            return
        if not any(w["id"] == word_id for w in VOCAB_BANK):
            json_response(self, {"error": "Mot inconnu"}, 400)
            return

        progress = load_vocab_progress()
        entry = next(
            (p for p in progress
             if p["studentId"] == student["id"] and p["wordId"] == word_id),
            None,
        )
        if entry is None:
            entry = {"studentId": student["id"], "wordId": word_id, "box": 0, "dueDate": "", "lastReview": None}
            progress.append(entry)

        box = entry["box"]
        if quality == "encore":
            box = 0
        elif quality == "facile":
            box = min(box + 1, len(VOCAB_INTERVALS_DAYS) - 1)
        # "difficile" garde la même boîte

        entry["box"] = box
        entry["dueDate"] = (date.today() + timedelta(days=VOCAB_INTERVALS_DAYS[box])).isoformat()
        entry["lastReview"] = datetime.now().isoformat(timespec="seconds")
        save_vocab_progress(progress)

        json_response(self, {"success": True, "box": box, "dueDate": entry["dueDate"]})

    def _handle_vocab_check_answer(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        word_id = body.get("wordId", "")
        guess = body.get("guess", "").strip()[:100]
        word = next((w for w in VOCAB_BANK if w["id"] == word_id), None)
        if word is None:
            json_response(self, {"error": "Mot inconnu"}, 400)
            return
        if not guess:
            json_response(self, {"correct": False})
            return

        system_prompt = (
            "Tu corriges un exercice de vocabulaire pour des élèves adultes "
            "en francisation au Québec (Niveau 4). Le mot à trouver est : "
            f"« {word['mot']} ». Définition : « {word['definition']} ». "
            "L'élève a écrit une réponse qui ne correspond pas exactement au "
            "mot attendu (accents/majuscules déjà ignorés). Détermine si sa "
            "réponse est quand même acceptable : une variante orthographique "
            "raisonnable, une expression équivalente (ex. « médecin "
            "spécialiste » pour « spécialiste »), un synonyme correct, ou "
            "l'oubli/l'ajout d'un article. Refuse si c'est un mot différent "
            "ou clairement incorrect. Réponds UNIQUEMENT avec un objet JSON "
            'valide, sans texte avant ni après : {"correct": true} ou '
            '{"correct": false}.'
        )
        user_content = f"Réponse de l'élève : {guess}"

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=20)
        if err:
            # Le service IA est indisponible : on retombe sur le refus strict
            # déjà appliqué côté client plutôt que de bloquer l'élève.
            json_response(self, {"correct": False, "aiUnavailable": True})
            return

        json_response(self, {"correct": bool(parsed.get("correct", False))})

    def _handle_vocab_translate(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        word_id = body.get("wordId", "")
        language = body.get("language", "").strip()[:60]
        word = next((w for w in VOCAB_BANK if w["id"] == word_id), None)
        if word is None:
            json_response(self, {"error": "Mot inconnu"}, 400)
            return
        if not language:
            json_response(self, {"error": "Langue non précisée"}, 400)
            return

        system_prompt = (
            "Tu es un assistant de traduction pour des élèves adultes en "
            "francisation au Québec. Traduis un mot de vocabulaire français, "
            "sa définition et sa phrase d'exemple vers cette langue : "
            f"{language}. Réponds UNIQUEMENT avec un objet JSON valide, sans "
            'texte avant ni après, exactement dans ce format : {"traduction": '
            '"...", "definitionTraduite": "...", "exempleTraduit": "..."} — '
            '"traduction" est la traduction du mot seul (garde un article si '
            'naturel dans la langue cible). "definitionTraduite" est la '
            'traduction de la définition. "exempleTraduit" est la traduction '
            "de la phrase d'exemple complète. Utilise une traduction "
            "naturelle et courante, pas littérale."
        )
        user_content = f"Mot : {word['mot']}\nDéfinition : {word['definition']}\nExemple : {word['exemple']}"

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=300)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        json_response(self, {
            "traduction": parsed.get("traduction", ""),
            "definitionTraduite": parsed.get("definitionTraduite", ""),
            "exempleTraduit": parsed.get("exempleTraduit", ""),
        })

    def _handle_student_dashboard(self, params):
        code = params.get("code", [""])[0].strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        available_ids = get_available_activity_ids()
        available_activities = [a for a in load_activities() if a["id"] in available_ids]

        progress = [p for p in load_progress() if p["studentId"] == student["id"]]
        started_ids = {p["activityId"] for p in progress}
        completed_ids = {p["activityId"] for p in progress if p["event"] == "exercise_completed"}

        next_activity = None
        for a in available_activities:
            if a["id"] not in started_ids:
                next_activity = {"id": a["id"], "title": a["title"]}
                break
        if next_activity is None:
            for a in available_activities:
                if a["id"] not in completed_ids:
                    next_activity = {"id": a["id"], "title": a["title"]}
                    break

        # ── Série de jours consécutifs (streak) ─────────────────────────
        dates_done = set()
        for p in progress:
            ts = p.get("timestamp", "")
            if ts:
                try:
                    dates_done.add(datetime.fromisoformat(ts).date())
                except ValueError:
                    pass
        streak = 0
        cursor = date.today()
        if cursor not in dates_done:
            cursor = cursor - timedelta(days=1)
        while cursor in dates_done:
            streak += 1
            cursor = cursor - timedelta(days=1)

        # ── Maîtrise du vocabulaire (mots des activités déjà au dossier) ──
        pool_ids = {w["id"] for w in get_student_vocab_pool()}
        vocab_progress = [
            p for p in load_vocab_progress()
            if p["studentId"] == student["id"] and p["wordId"] in pool_ids
        ]
        total_words = len(pool_ids)
        reviewed_words = len(vocab_progress)
        mastered_words = sum(1 for p in vocab_progress if p["box"] >= 4)
        learning_words = reviewed_words - mastered_words
        new_words = total_words - reviewed_words

        json_response(self, {
            "activitiesTotal": len(available_activities),
            "activitiesStarted": len(started_ids & {a["id"] for a in available_activities}),
            "activitiesCompleted": len(completed_ids & {a["id"] for a in available_activities}),
            "nextActivity": next_activity,
            "streak": streak,
            "vocab": {
                "total": total_words,
                "mastered": mastered_words,
                "learning": learning_words,
                "new": new_words,
            },
        })

    def _handle_student_activities(self, params):
        code = params.get("code", [""])[0].strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        today = date.today().isoformat()
        activities = load_activities()
        result = []
        for a in activities:
            dp = a.get("datePrevue", "")
            df = a.get("dateFin", "")
            # Masquer les activités dont la période est terminée
            if df and df < today:
                continue
            available = (not dp or dp <= today)
            result.append({
                "id": a["id"],
                "title": a["title"],
                "thumbnail": a.get("thumbnail", ""),
                "datePrevue": dp,
                "dateVue": a.get("dateVue", ""),
                "available": available,
                "competences": a.get("competences", []),
                "tempsVerbaux": a.get("tempsVerbaux", []),
                "domaineDeVie": a.get("domaineDeVie", ""),
                "files": {
                    "interactive": a.get("interactive", "") if available else "",
                    "studentDoc": a.get("studentDoc", "") if available else "",
                    "slideshow": a.get("slideshow", "") if available else "",
                    "planCours": a.get("planCours", "") if available else "",
                    "autres": a.get("autres", "") if available else "",
                },
            })
        json_response(self, result)

    def _handle_log_access(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        log = load_access_log()
        entry = {
            "studentId": student["id"],
            "studentLabel": student.get("label", ""),
            "activityId": body.get("activityId"),
            "activityTitle": body.get("activityTitle", ""),
            "file": body.get("file", ""),
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
        log.append(entry)
        save_access_log(log)
        json_response(self, {"success": True})

    def _call_anthropic_json(self, system_prompt, user_content, max_tokens=400):
        """Appelle l'API Anthropic et retourne (parsed_dict, None) en cas de
        succès, ou (None, (error_message, status_code)) en cas d'échec. Le
        modèle doit répondre avec un objet JSON pur (voir prompts appelants)."""
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            return None, ("Clé API non configurée sur le serveur", 503)

        payload = json.dumps({
            "model": "claude-haiku-4-5-20251001",
            "max_tokens": max_tokens,
            "system": system_prompt,
            "messages": [{"role": "user", "content": user_content}],
        }).encode("utf-8")

        req = urllib.request.Request(
            "https://api.anthropic.com/v1/messages",
            data=payload,
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                result = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            print(f"[WARN] Anthropic API HTTPError {e.code}: {detail}", flush=True)
            return None, ("Le service de correction est momentanément indisponible", 502)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"[WARN] Anthropic API injoignable : {e}", flush=True)
            return None, ("Le service de correction est momentanément indisponible", 502)

        try:
            raw_text = result["content"][0]["text"].strip()
            if raw_text.startswith("```"):
                raw_text = re.sub(r"^```(json)?\n?", "", raw_text)
                raw_text = re.sub(r"\n?```$", "", raw_text)
            return json.loads(raw_text), None
        except (KeyError, IndexError, json.JSONDecodeError) as e:
            print(f"[WARN] Réponse IA non structurée : {e}", flush=True)
            return None, ("Réponse inattendue du service de correction", 502)

    def _handle_correct_french(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        text = body.get("text", "").strip()
        if not text:
            json_response(self, {"error": "Aucun texte fourni"}, 400)
            return
        if len(text) > 500:
            text = text[:500]

        question = body.get("question", "").strip()[:300]
        context_line = (
            f"\n\nContexte : l'élève répond à cette question posée dans un "
            f"dialogue : « {question} ». Corrige sa réponse comme une réplique "
            "naturelle dans cette conversation (les réponses courtes et "
            "elliptiques sont normales à l'oral, ne les pénalise pas si elles "
            "sont grammaticalement correctes dans ce contexte)."
            if question else ""
        )

        system_prompt = (
            "Tu es un tuteur de francisation pour des élèves adultes de Niveau 4 "
            "au Québec (niveau intermédiaire). L'élève a dit une phrase à voix "
            "haute, transcrite automatiquement (elle peut donc contenir des "
            "erreurs de transcription en plus d'erreurs de langue). Corrige la "
            "phrase en français correct et naturel (français québécois standard "
            "accepté)." + context_line + " Réponds UNIQUEMENT avec un objet "
            "JSON valide, sans texte avant ni après, exactement dans ce "
            'format : {"corrige": "...", "erreurs": [{"explication": "..."}], '
            '"memePhrase": true} — "memePhrase" est true si la phrase était déjà '
            'correcte. "erreurs" contient au maximum 3 explications courtes '
            "(une phrase chacune), en français simple adapté à un élève de "
            "Niveau 4. Ne commente jamais les erreurs de transcription probables "
            "(ex. homophones) — corrige comme si la transcription reflétait "
            "fidèlement l'intention de l'élève."
        )

        parsed, err = self._call_anthropic_json(system_prompt, text)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        json_response(self, {
            "original": text,
            "corrige": parsed.get("corrige", text),
            "erreurs": parsed.get("erreurs", []),
            "memePhrase": parsed.get("memePhrase", False),
        })

    def _handle_correct_email(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        scenario = body.get("scenario", "").strip()[:1500]
        subject = body.get("subject", "").strip()[:200]
        text = body.get("text", "").strip()
        if not text:
            json_response(self, {"error": "Aucun texte fourni"}, 400)
            return
        if len(text) > 3000:
            text = text[:3000]

        system_prompt = (
            "Tu es un tuteur de francisation pour des élèves adultes de Niveau 4 "
            "au Québec (niveau intermédiaire). L'élève rédige un courriel en "
            "réponse à une mise en situation, généralement au passé composé "
            "pour raconter les faits. Voici la mise en situation : "
            f'"{scenario}"\n\n'
            "Analyse le courriel de l'élève (objet et corps fournis par "
            "l'utilisateur) et réponds UNIQUEMENT avec un objet JSON valide, "
            "sans texte avant ni après, exactement dans ce format : "
            '{"pertinent": true, "commentairePertinence": "...", '
            '"objetCorrige": "...", "corpsCorrige": "...", '
            '"erreurs": [{"explication": "..."}]} — '
            '"pertinent" indique si le contenu répond bien à la situation '
            "donnée. \"commentairePertinence\" est une phrase courte (adaptée "
            "Niveau 4) qui explique pourquoi, ou ce qui manque si pertinent "
            "est false. \"objetCorrige\" et \"corpsCorrige\" sont l'objet et le "
            "corps du courriel corrigés en français correct et naturel "
            "(français québécois standard accepté), avec un registre "
            "professionnel adapté à un courriel (formules de politesse). "
            "\"erreurs\" contient au maximum 5 explications courtes (une "
            "phrase chacune) des principales erreurs de grammaire, "
            "conjugaison (surtout passé composé) ou syntaxe, en français "
            "simple adapté à un élève de Niveau 4."
        )

        user_content = f"Objet : {subject}\n\n{text}"
        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=900)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        json_response(self, {
            "originalSubject": subject,
            "originalText": text,
            "pertinent": parsed.get("pertinent", True),
            "commentairePertinence": parsed.get("commentairePertinence", ""),
            "objetCorrige": parsed.get("objetCorrige", subject),
            "corpsCorrige": parsed.get("corpsCorrige", text),
            "erreurs": parsed.get("erreurs", []),
        })

    def _handle_add_student(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        students = load_students()
        existing_codes = {s["code"] for s in students}
        count = max(1, int(body.get("count", 1)))
        added = []
        for _ in range(count):
            label = body.get("label", "").strip()
            new_id = max((s["id"] for s in students + added), default=0) + 1
            student = {
                "id": new_id,
                "code": generate_code(existing_codes),
                "label": label or f"Élève {new_id}",
                "createdAt": date.today().isoformat(),
            }
            existing_codes.add(student["code"])
            added.append(student)
        students.extend(added)
        save_students(students)
        json_response(self, {"success": True, "students": added}, 201)

    def _handle_student_progress(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        allowed_events = {"dialogue_listened", "exercise_completed", "file_opened"}
        event = body.get("event", "")
        if event not in allowed_events:
            json_response(self, {"error": "Événement invalide"}, 400)
            return
        progress = load_progress()
        # Un seul enregistrement par (élève, activité, événement).
        # Pour exercise_completed, on met à jour l'enregistrement avec les
        # dernières statistiques cumulées (progression partielle en temps réel).
        existing = next(
            (p for p in progress
             if p["studentId"] == student["id"]
             and p["activityId"] == body.get("activityId")
             and p["event"] == event),
            None,
        )
        if existing is None:
            entry = {
                "studentId": student["id"],
                "studentLabel": student.get("label", ""),
                "activityId": body.get("activityId"),
                "activityTitle": body.get("activityTitle", ""),
                "event": event,
                "score": body.get("score"),
                "zones": body.get("zones"),
                "zonesDone": body.get("zonesDone"),
                "firstTry": body.get("firstTry"),
                "totalErrors": body.get("totalErrors"),
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            progress.append(entry)
            save_progress(progress)
        elif event == "exercise_completed":
            existing["score"] = body.get("score")
            existing["zones"] = body.get("zones")
            existing["zonesDone"] = body.get("zonesDone")
            existing["firstTry"] = body.get("firstTry")
            existing["totalErrors"] = body.get("totalErrors")
            existing["timestamp"] = datetime.now().isoformat(timespec="seconds")
            save_progress(progress)
        json_response(self, {"success": True})

    def _handle_delete_student(self, student_id):
        students = load_students()
        students = [s for s in students if s["id"] != student_id]
        save_students(students)
        json_response(self, {"success": True})


# ── Point d'entrée ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    import socketserver
    import threading

    # init_storage() peut copier plusieurs Mo vers le volume Railway, ce qui
    # dépasse parfois le délai du healthcheck. On lie d'abord le serveur au
    # port (le healthcheck passe immédiatement), puis on initialise le stockage
    # en arrière-plan sans jamais faire planter le serveur.
    def _init_storage_safe():
        try:
            init_storage()
            print("[init] Stockage initialisé", flush=True)
        except Exception as e:
            print(f"[WARN] init_storage a échoué : {e}", flush=True)

    threading.Thread(target=_init_storage_safe, daemon=True).start()

    class ThreadingServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
        # Un serveur mono-thread bloquerait tous les élèves pendant chaque
        # appel réseau (ex. correction IA, qui prend 1-3 s) ; daemon_threads
        # évite que des requêtes lentes empêchent l'arrêt propre du serveur.
        daemon_threads = True
        allow_reuse_address = True

    with ThreadingServer(("", PORT), Handler) as httpd:
        print(f"Serveur démarré sur http://localhost:{PORT}", flush=True)
        print(f"STORAGE_DIR = {STORAGE_DIR}", flush=True)
        httpd.serve_forever()
