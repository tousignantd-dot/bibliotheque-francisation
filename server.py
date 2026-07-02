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
import unicodedata
import re
import zipfile
import io
import random
import string
from pathlib import Path
from datetime import date, datetime

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
        json_response(self, {"success": True, "studentId": student["id"], "label": student.get("label", "")})

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
        # Évite les doublons : un seul enregistrement par (élève, activité, événement)
        exists = any(
            p["studentId"] == student["id"]
            and p["activityId"] == body.get("activityId")
            and p["event"] == event
            for p in progress
        )
        if not exists:
            entry = {
                "studentId": student["id"],
                "studentLabel": student.get("label", ""),
                "activityId": body.get("activityId"),
                "activityTitle": body.get("activityTitle", ""),
                "event": event,
                "score": body.get("score"),
                "zones": body.get("zones"),
                "firstTry": body.get("firstTry"),
                "totalErrors": body.get("totalErrors"),
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            progress.append(entry)
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
    init_storage()
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serveur démarré sur http://localhost:{PORT}", flush=True)
        print(f"STORAGE_DIR = {STORAGE_DIR}", flush=True)
        httpd.serve_forever()
