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
    import unicodedata, re
    text = unicodedata.normalize("NFD", text)
    text = "".join(c for c in text if unicodedata.category(c) != "Mn")
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:60]


def json_response(handler, data, status=200):
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)


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
        # API : liste des activités
        if self.path == "/api/activities":
            json_response(self, load_activities())
            return
        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        # ---- Ajouter une activité ----
        if path == "/api/activities":
            self._handle_add()

        # ---- Modifier une activité ----
        elif path.startswith("/api/activities/") and path.endswith("/rename"):
            activity_id = int(path.split("/")[3])
            self._handle_rename(activity_id)

        else:
            self.send_error(404)

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path.startswith("/api/activities/"):
            try:
                activity_id = int(path.split("/")[3])
                self._handle_delete(activity_id)
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
        else:
            self.send_error(404)

    # ------------------------------------------------------------------
    def _handle_add(self):
        content_type = self.headers.get("Content-Type", "")

        if "multipart/form-data" not in content_type:
            json_response(self, {"error": "multipart requis"}, 400)
            return

        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={"REQUEST_METHOD": "POST", "CONTENT_TYPE": content_type},
        )

        title = form.getvalue("title", "").strip()
        if not title:
            json_response(self, {"error": "Titre requis"}, 400)
            return

        slug = slugify(title)
        activities = load_activities()
        new_id = next_id(activities)

        thumb_path = ""
        interactive_path = ""
        doc_path = ""

        # Thumbnail
        if "thumbnail" in form and form["thumbnail"].filename:
            f = form["thumbnail"]
            ext = Path(f.filename).suffix.lower()
            dest = BASE_DIR / "assets" / "thumbnails" / f"{slug}{ext}"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(f.file.read())
            thumb_path = f"assets/thumbnails/{slug}{ext}"

        # Fichier interactif (ZIP ou HTML)
        if "interactive" in form and form["interactive"].filename:
            f = form["interactive"]
            ext = Path(f.filename).suffix.lower()
            dest_dir = BASE_DIR / "assets" / "interactive" / slug
            dest_dir.mkdir(parents=True, exist_ok=True)
            if ext == ".zip":
                import zipfile, io
                with zipfile.ZipFile(io.BytesIO(f.file.read())) as zf:
                    zf.extractall(dest_dir)
                interactive_path = f"assets/interactive/{slug}/index.html"
            else:
                dest = dest_dir / f.filename
                dest.write_bytes(f.file.read())
                interactive_path = f"assets/interactive/{slug}/{f.filename}"

        # Document élève
        if "studentDoc" in form and form["studentDoc"].filename:
            f = form["studentDoc"]
            ext = Path(f.filename).suffix.lower()
            dest = BASE_DIR / "assets" / "documents" / f"{slug}{ext}"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(f.file.read())
            doc_path = f"assets/documents/{slug}{ext}"

        # Diaporama PPT
        slideshow_path = ""
        if "slideshow" in form and form["slideshow"].filename:
            f = form["slideshow"]
            ext = Path(f.filename).suffix.lower()
            dest = BASE_DIR / "assets" / "slideshows" / f"{slug}{ext}"
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(f.file.read())
            slideshow_path = f"assets/slideshows/{slug}{ext}"

        activity = {
            "id": new_id,
            "title": title,
            "level": "Niveau 4",
            "thumbnail": thumb_path,
            "interactive": interactive_path,
            "studentDoc": doc_path,
            "slideshow": slideshow_path,
            "keywords": [],
        }

        activities.append(activity)
        save_activities(activities)
        json_response(self, {"success": True, "activity": activity}, 201)

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

        # Supprimer les fichiers associés
        for key in ("thumbnail", "interactive", "studentDoc", "slideshow"):
            rel = target.get(key, "")
            if rel:
                p = BASE_DIR / rel
                if p.exists():
                    if p.is_dir():
                        shutil.rmtree(p)
                    else:
                        p.unlink()
                # Dossier parent interactive
                if key == "interactive":
                    parent = p.parent
                    if parent.exists() and not any(parent.iterdir()):
                        parent.rmdir()

        activities = [a for a in activities if a["id"] != activity_id]
        save_activities(activities)
        json_response(self, {"success": True})


if __name__ == "__main__":
    import socketserver
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serveur démarré sur http://localhost:{PORT}")
        httpd.serve_forever()
