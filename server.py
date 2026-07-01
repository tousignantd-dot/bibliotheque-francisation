"""
Serveur local — Bibliothèque d'activités pédagogiques
Gère les fichiers statiques + les opérations d'administration (ajout, modification, suppression).
"""

import http.server
import json
import os
import shutil
import cgi
import urllib.parse
import unicodedata
import re
import zipfile
import io
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DATA_FILE = BASE_DIR / "data" / "activities.json"
PORT = 5173


def load_activities():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_activities(activities):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(activities, f, ensure_ascii=False, indent=2)


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
    """Normalise un nom de fichier : supprime accents, espaces et caractères spéciaux."""
    stem = Path(filename).stem
    ext = Path(filename).suffix.lower()
    return slugify(stem) + ext


def json_response(handler, data, status=200):
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)


def save_file(form, field, dest_path):
    """Sauvegarde un fichier uploadé vers dest_path. Retourne True si réussi."""
    if field not in form or not form[field].filename:
        return False
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    dest_path.write_bytes(form[field].file.read())
    return True


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
        if self.path == "/api/activities":
            json_response(self, load_activities())
            return
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/activities":
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

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if re.match(r"^/api/activities/\d+$", path):
            try:
                activity_id = int(path.split("/")[3])
                self._handle_delete(activity_id)
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
        else:
            self.send_error(404)

    # ------------------------------------------------------------------
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

    def _upload_thumbnail(self, form, slug):
        if "thumbnail" not in form or not form["thumbnail"].filename:
            return ""
        f = form["thumbnail"]
        ext = Path(f.filename).suffix.lower()
        dest = BASE_DIR / "assets" / "thumbnails" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/thumbnails/{slug}{ext}"

    def _upload_interactive(self, form, slug):
        if "interactive" not in form or not form["interactive"].filename:
            return ""
        f = form["interactive"]
        ext = Path(f.filename).suffix.lower()
        dest_dir = BASE_DIR / "assets" / "interactive" / slug
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
        safe_name = safe_filename(f.filename)
        dest = BASE_DIR / "assets" / "documents" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/documents/{slug}{ext}"

    def _upload_slideshow(self, form, slug):
        if "slideshow" not in form or not form["slideshow"].filename:
            return ""
        f = form["slideshow"]
        ext = Path(f.filename).suffix.lower()
        dest = BASE_DIR / "assets" / "slideshows" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/slideshows/{slug}{ext}"

    def _upload_plan_cours(self, form, slug):
        if "planCours" not in form or not form["planCours"].filename:
            return ""
        f = form["planCours"]
        safe_name = safe_filename(f.filename)
        dest = BASE_DIR / "assets" / "plans" / safe_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/plans/{safe_name}"

    def _upload_autres(self, form, slug):
        if "autres" not in form or not form["autres"].filename:
            return ""
        f = form["autres"]
        safe_name = safe_filename(f.filename)
        dest = BASE_DIR / "assets" / "autres" / safe_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/autres/{safe_name}"

    def _delete_file(self, rel_path, key=""):
        if not rel_path:
            return
        p = BASE_DIR / rel_path
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
        if key == "interactive":
            parent = p.parent
            if parent.exists() and parent != BASE_DIR / "assets" / "interactive":
                try:
                    parent.rmdir()
                except OSError:
                    pass

    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
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

        # Titre
        new_title = form.getvalue("title", "").strip()
        if new_title:
            target["title"] = new_title
            slug = slugify(new_title)

        # Remplacer chaque fichier si un nouveau est fourni
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

    # ------------------------------------------------------------------
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

        save_activities(activities)
        json_response(self, {"success": True})

    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
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

    # ------------------------------------------------------------------
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


if __name__ == "__main__":
    import socketserver
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serveur démarré sur http://localhost:{PORT}")
        httpd.serve_forever()
