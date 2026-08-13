"""
Serveur — Bibliothèque d'activités pédagogiques
Gère les fichiers statiques + les opérations d'administration (ajout, modification, suppression).
"""

import http.server
import hashlib
import hmac
import json
import mimetypes
import os
import shutil
import threading
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
import uuid
from pathlib import Path
from datetime import date, datetime, timedelta

BASE_DIR = Path(__file__).parent.resolve()


def _charge_env_local():
    """En production, les clés viennent des variables Railway. En local, elles
    sont dans .env (non versionné). Lecture volontairement minimale : lignes
    CLE=valeur, rien d'autre. Une variable déjà définie dans l'environnement
    gagne toujours — sinon un .env oublié écraserait la vraie configuration."""
    fichier = BASE_DIR / ".env"
    if not fichier.exists():
        return
    try:
        for ligne in fichier.read_text(encoding="utf-8").splitlines():
            ligne = ligne.strip()
            if not ligne or ligne.startswith("#") or "=" not in ligne:
                continue
            cle, _, valeur = ligne.partition("=")
            cle = cle.strip()
            if cle and cle not in os.environ:
                os.environ[cle] = valeur.strip().strip('"').strip("'")
    except OSError as e:
        print(f"[WARN] .env illisible : {e}", flush=True)


_charge_env_local()

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
# Cache serveur des traductions : une paire mot/définition n'est traduite
# qu'une fois pour toute la classe. Le cache navigateur évite l'aller-retour ;
# celui-ci évite de payer deux fois le même appel quand l'élève change d'appareil.
VOCAB_TRANSLATIONS_FILE = STORAGE_DIR / "data" / "traductions.json"
# Journal des traductions signalées comme douteuses. Pas d'écran d'administration :
# le fichier se lit à la main quand on voudra constituer une liste révisée.
VOCAB_REPORTS_FILE = STORAGE_DIR / "data" / "traductions_douteuses.json"
# Cache de la barre d'outils élève (traduction d'un passage, reformulation).
# Séparé de traductions.json : celui-là est indexé par mot de vocabulaire,
# celui-ci par empreinte d'un passage quelconque du module.
OUTILS_CACHE_FILE = STORAGE_DIR / "data" / "outils_cache.json"
ORAL_SUBMISSIONS_FILE = STORAGE_DIR / "data" / "oral_submissions.json"
ORAL_AUDIO_DIR = STORAGE_DIR / "assets" / "oral-submissions"
# Multi-enseignants : chaque enseignant possède un ou plusieurs groupes.
# Le catalogue d'activités reste commun ; ce qui appartient au groupe, c'est la
# planification (dates), les élèves, la progression et les productions orales.
TEACHERS_FILE  = STORAGE_DIR / "data" / "teachers.json"
GROUPS_FILE    = STORAGE_DIR / "data" / "groups.json"
SCHEDULE_FILE  = STORAGE_DIR / "data" / "schedule.json"
SESSIONS_FILE  = STORAGE_DIR / "data" / "prof_sessions.json"

SESSION_DAYS = 30

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
    USER_FIELDS = ("dateVue", "datePrevue", "dateFin", "categorie")
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

CATEGORIES = ("cours", "atelier")


def normalize_categorie(value, interactive_path=""):
    """« cours » = les modules de 4 h du matin ; « atelier » = les activités
    de 2 h de l'après-midi. Les activités antérieures à ce champ sont classées
    d'après leur dossier : les modules vivent dans assets/interactive/module-*."""
    if value in CATEGORIES:
        return value
    return "cours" if "module-" in (interactive_path or "") else "atelier"


def load_activities():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            activities = json.load(f)
        for a in activities:
            a["categorie"] = normalize_categorie(a.get("categorie"), a.get("interactive", ""))
        return activities
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


# ── Enseignants, groupes, planification ─────────────────────────────────────

def _load_json_list(path):
    if path.exists():
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"[WARN] {path.name} illisible, repli sur une liste vide", flush=True)
    return []


def _save_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_teachers():
    return _load_json_list(TEACHERS_FILE)


def save_teachers(teachers):
    _save_json(TEACHERS_FILE, teachers)


def load_groups():
    return _load_json_list(GROUPS_FILE)


def save_groups(groups):
    _save_json(GROUPS_FILE, groups)


def load_schedule():
    """[{groupId, activityId, dateVue, datePrevue, dateFin}] — dates par groupe."""
    return _load_json_list(SCHEDULE_FILE)


def save_schedule(entries):
    _save_json(SCHEDULE_FILE, entries)


def schedule_for_group(group_id):
    """{activityId: {dateVue, datePrevue, dateFin}} pour un groupe donné."""
    return {
        e["activityId"]: {
            "dateVue": e.get("dateVue", ""),
            "datePrevue": e.get("datePrevue", ""),
            "dateFin": e.get("dateFin", ""),
        }
        for e in load_schedule()
        if e.get("groupId") == group_id
    }


def set_schedule_dates(group_id, activity_id, fields):
    """Écrit les dates d'une activité pour un groupe. `fields` peut ne contenir
    qu'une partie de dateVue/datePrevue/dateFin."""
    entries = load_schedule()
    target = next(
        (e for e in entries
         if e.get("groupId") == group_id and e.get("activityId") == activity_id),
        None,
    )
    if target is None:
        target = {"groupId": group_id, "activityId": activity_id,
                  "dateVue": "", "datePrevue": "", "dateFin": ""}
        entries.append(target)
    for key in ("dateVue", "datePrevue", "dateFin"):
        if key in fields:
            target[key] = fields[key] or ""
    save_schedule(entries)
    return target


def activities_for_group(group_id):
    """Le catalogue commun, avec les dates du groupe superposées."""
    sched = schedule_for_group(group_id)
    result = []
    for a in load_activities():
        entry = dict(a)
        dates = sched.get(a["id"], {})
        entry["dateVue"] = dates.get("dateVue", "")
        entry["datePrevue"] = dates.get("datePrevue", "")
        entry["dateFin"] = dates.get("dateFin", "")
        result.append(entry)
    return result


def is_offered(dates, today_str):
    """Une activité n'est offerte à un groupe que si l'enseignant lui a donné
    une date de disponibilité pour ce groupe. Un groupe neuf part donc vide :
    le catalogue est commun, mais rien n'est ouvert tant qu'on n'a pas planifié.
    """
    dp = dates.get("datePrevue", "")
    df = dates.get("dateFin", "")
    if not dp:
        return False
    if df and df < today_str:
        return False
    return dp <= today_str


def get_available_activity_ids(group_id):
    """Activités accessibles aujourd'hui aux élèves d'un groupe."""
    today_str = date.today().isoformat()
    sched = schedule_for_group(group_id)
    return {
        a["id"] for a in load_activities()
        if is_offered(sched.get(a["id"], {}), today_str)
    }


def get_student_vocab_pool(group_id):
    """Ne garde que les mots liés aux activités déjà accessibles à l'élève."""
    available_ids = get_available_activity_ids(group_id)
    return [
        w for w in VOCAB_BANK
        if not w.get("activityIds") or available_ids & set(w["activityIds"])
    ]


def find_group(group_id):
    return next((g for g in load_groups() if g["id"] == group_id), None)


def groups_of_teacher(teacher):
    """Un administrateur voit tous les groupes ; un enseignant, les siens."""
    groups = load_groups()
    if teacher.get("role") == "admin":
        return groups
    return [g for g in groups if g.get("teacherId") == teacher["id"]]


def teacher_can_access_group(teacher, group_id):
    if teacher.get("role") == "admin":
        return find_group(group_id) is not None
    g = find_group(group_id)
    return g is not None and g.get("teacherId") == teacher["id"]


# ── Mots de passe et sessions enseignants ───────────────────────────────────

def hash_password(password, salt=None, iterations=200_000):
    salt = salt or uuid.uuid4().hex
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations)
    return f"pbkdf2_sha256${iterations}${salt}${dk.hex()}"


def verify_password(password, stored):
    try:
        algo, iterations, salt, digest = stored.split("$")
    except (ValueError, AttributeError):
        return False
    if algo != "pbkdf2_sha256":
        return False
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), int(iterations))
    return hmac.compare_digest(dk.hex(), digest)


def load_sessions():
    if SESSIONS_FILE.exists():
        try:
            with open(SESSIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return {}


def save_sessions(sessions):
    _save_json(SESSIONS_FILE, sessions)


def create_session(teacher_id):
    sessions = load_sessions()
    now = datetime.now()
    # Purge des jetons expirés à chaque connexion : pas de tâche de fond à gérer.
    sessions = {
        t: s for t, s in sessions.items()
        if s.get("expiresAt", "") > now.isoformat(timespec="seconds")
    }
    token = uuid.uuid4().hex + uuid.uuid4().hex
    sessions[token] = {
        "teacherId": teacher_id,
        "createdAt": now.isoformat(timespec="seconds"),
        "expiresAt": (now + timedelta(days=SESSION_DAYS)).isoformat(timespec="seconds"),
    }
    save_sessions(sessions)
    return token


def destroy_session(token):
    sessions = load_sessions()
    if token in sessions:
        del sessions[token]
        save_sessions(sessions)


def teacher_from_token(token):
    if not token:
        return None
    session = load_sessions().get(token)
    if not session:
        return None
    if session.get("expiresAt", "") <= datetime.now().isoformat(timespec="seconds"):
        destroy_session(token)
        return None
    return next((t for t in load_teachers() if t["id"] == session["teacherId"]), None)


def public_teacher(teacher):
    """Vue d'un enseignant sans son empreinte de mot de passe."""
    return {
        "id": teacher["id"],
        "nom": teacher.get("nom", ""),
        "courriel": teacher.get("courriel", ""),
        "role": teacher.get("role", "prof"),
        "createdAt": teacher.get("createdAt", ""),
    }


def normalize_email(value):
    return (value or "").strip().lower()


# ── Migration vers le multi-groupes ─────────────────────────────────────────

def migrate_multi_groupes():
    """Fait passer une installation mono-groupe au modèle enseignants/groupes.

    Idempotent : ne fait rien si les fichiers existent déjà. Les dates
    actuellement portées par les activités deviennent la planification du
    groupe historique, et les élèves existants y sont rattachés.
    """
    groups = load_groups()
    if not groups:
        groups = [{
            "id": 1,
            "nom": "Niveau 4",
            "teacherId": None,
            "createdAt": date.today().isoformat(),
        }]
        save_groups(groups)
        print("[migration] Groupe historique « Niveau 4 » créé", flush=True)

    default_group_id = groups[0]["id"]

    # Dates portées par les activités → planification du groupe historique.
    #
    # Avant le multi-groupes, une activité sans date était visible de tous les
    # élèves ; désormais il faut une date de disponibilité (un groupe neuf part
    # vide). Pour ne rien retirer à la classe en cours, on ouvre explicitement
    # au groupe historique tout ce qui lui était déjà visible : sa date prévue
    # si elle existe, sinon la date où l'activité a été vue, sinon aujourd'hui.
    if not SCHEDULE_FILE.exists():
        today_str = date.today().isoformat()
        entries = []
        for a in load_activities():
            date_fin = a.get("dateFin", "")
            date_vue = a.get("dateVue", "")
            entries.append({
                "groupId": default_group_id,
                "activityId": a["id"],
                "dateVue": date_vue,
                "datePrevue": a.get("datePrevue", "") or date_vue or today_str,
                "dateFin": date_fin,
            })
        save_schedule(entries)
        print(f"[migration] {len(entries)} activités ouvertes au groupe {default_group_id} "
              "(état d'avant le multi-groupes conservé)", flush=True)

    # Élèves sans groupe → groupe historique
    students = load_students()
    orphans = [s for s in students if not s.get("groupId")]
    if orphans:
        for s in orphans:
            s["groupId"] = default_group_id
        save_students(students)
        print(f"[migration] {len(orphans)} élèves rattachés au groupe {default_group_id}", flush=True)

    # Premier administrateur : semé par variables d'environnement si fournies,
    # sinon créé par l'écran d'installation au premier lancement.
    teachers = load_teachers()
    if not teachers:
        email = normalize_email(os.environ.get("PROF_COURRIEL", ""))
        password = os.environ.get("PROF_MOTDEPASSE", "")
        if email and password:
            teachers = [{
                "id": 1,
                "nom": os.environ.get("PROF_NOM", "Enseignant"),
                "courriel": email,
                "motDePasse": hash_password(password),
                "role": "admin",
                "createdAt": date.today().isoformat(),
            }]
            save_teachers(teachers)
            print(f"[migration] Compte administrateur créé pour {email}", flush=True)
        else:
            print("[migration] Aucun enseignant — l'écran d'installation "
                  "(/prof.html) créera le premier compte", flush=True)

    # Le groupe historique appartient au premier enseignant connu
    teachers = load_teachers()
    if teachers:
        groups = load_groups()
        changed = False
        for g in groups:
            if not g.get("teacherId"):
                g["teacherId"] = teachers[0]["id"]
                changed = True
        if changed:
            save_groups(groups)


def load_vocab_progress():
    if VOCAB_PROGRESS_FILE.exists():
        with open(VOCAB_PROGRESS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_vocab_progress(data):
    VOCAB_PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(VOCAB_PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# Le serveur est multi-thread : deux élèves peuvent demander une traduction en
# même temps. Sans verrou, la deuxième écriture écraserait la première.
_VOCAB_TR_LOCK = threading.Lock()


def translation_key(langue, mot, definition):
    """Clé de cache. La définition entre dans la clé (par son empreinte) parce
    que deux modules peuvent définir le même mot différemment : sans elle, la
    traduction du module 9 s'afficherait sous la définition du module 6."""
    empreinte = hashlib.sha1(definition.strip().encode("utf-8")).hexdigest()[:10]
    return "%s|%s|%s" % (langue.strip().lower(), mot.strip().lower(), empreinte)


def load_translations():
    if VOCAB_TRANSLATIONS_FILE.exists():
        try:
            with open(VOCAB_TRANSLATIONS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_translation(key, value):
    with _VOCAB_TR_LOCK:
        cache = load_translations()
        cache[key] = value
        VOCAB_TRANSLATIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(VOCAB_TRANSLATIONS_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)


_OUTILS_LOCK = threading.Lock()


def outils_key(genre, langue, texte):
    """Clé de cache d'un passage. Le genre entre dans la clé : la traduction et
    la reformulation d'une même phrase sont deux résultats différents."""
    empreinte = hashlib.sha1(" ".join(texte.split()).encode("utf-8")).hexdigest()[:16]
    return "%s|%s|%s" % (genre, (langue or "").strip().lower(), empreinte)


def load_outils_cache():
    if OUTILS_CACHE_FILE.exists():
        try:
            with open(OUTILS_CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_outils_entry(key, value):
    with _OUTILS_LOCK:
        cache = load_outils_cache()
        cache[key] = value
        OUTILS_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTILS_CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)


def log_translation_report(entry):
    with _VOCAB_TR_LOCK:
        journal = []
        if VOCAB_REPORTS_FILE.exists():
            try:
                with open(VOCAB_REPORTS_FILE, "r", encoding="utf-8") as f:
                    journal = json.load(f)
            except (json.JSONDecodeError, OSError):
                journal = []
        journal.append(entry)
        VOCAB_REPORTS_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(VOCAB_REPORTS_FILE, "w", encoding="utf-8") as f:
            json.dump(journal, f, ensure_ascii=False, indent=2)


def load_oral_submissions():
    if ORAL_SUBMISSIONS_FILE.exists():
        with open(ORAL_SUBMISSIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_oral_submissions(data):
    ORAL_SUBMISSIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ORAL_SUBMISSIONS_FILE, "w", encoding="utf-8") as f:
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


def strip_tags(value):
    """Retire les balises HTML d'un texte venu du navigateur. Les phrases
    d'exemple des modules contiennent <strong> autour du mot vedette."""
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", "", value)).strip()


def json_response(handler, data, status=200):
    body = json.dumps(data, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Access-Control-Allow-Origin", "*")
    handler.end_headers()
    handler.wfile.write(body)


# ── Jeu de rôle « louer un logement » (module 8) ─────────────────────────────
# Les fiches vivent ici, jamais dans le HTML du module : ce que chaque rôle
# ignore est tout l'intérêt de l'exercice, et un « afficher le code source »
# suffirait à le lire si c'était côté client. Les mêmes contenus existent en
# version papier dans assets/documents/module-logement-jeu-de-role.html.

# Voix ElevenLabs du personnage joué par l'assistant. Mêmes identifiants que
# les scripts de génération audio du module, pour que la visite sonne comme
# les dialogues déjà enregistrés.
VOIX_JEU_DE_ROLE = {
    "proprietaire": "WW0JfNPk5DgcQdM0d6X6",   # féminine #2 — la propriétaire
    "locataire":    "93nuHbke4dTER9x2pDwE",   # masculine #1 — le visiteur
}

# Voix de lecture de la barre d'outils élève (« Lire à voix haute »,
# « Écouter le modèle »). Fixe, sans rapport avec les personnages.
VOIX_LECTURE = "WW0JfNPk5DgcQdM0d6X6"

JEU_DE_ROLE_SUJETS = [
    "ce qui est inclus dans le loyer",
    "le chauffage et l'électricité",
    "les électroménagers et la buanderie",
    "le stationnement",
    "les animaux",
    "le bruit et le voisinage",
    "la date et la durée du bail",
]

JEU_DE_ROLE_LOGEMENTS = {
    "A": {
        "lieu": "centre-ville",
        "annonce": (
            "2 ½ meublé au troisième étage, rue Wellington Nord, en plein centre-ville. "
            "Fenêtres neuves. Arrêt d'autobus devant la porte. Épicerie et pharmacie à "
            "deux minutes de marche. Libre le 1er octobre. 690 $ par mois."
        ),
        "proprietaire": [
            "Le chauffage et l'électricité sont inclus. Internet n'est pas inclus.",
            "Meublé : un lit, une table, deux chaises, une commode. Pas de vaisselle.",
            "Aucune buanderie dans l'immeuble ; il y a une laverie à trois rues.",
            "Pas de stationnement : dans la rue seulement, avec une vignette de la Ville.",
            "Aucun animal accepté, parce que la voisine du deuxième est allergique.",
            "Bail de 12 mois, du 1er octobre au 30 septembre.",
            "Il y a un bar au rez-de-chaussée : on entend la musique jusqu'à minuit les vendredis et samedis.",
            "Le logement n'a pas de balcon.",
        ],
        "locataire": [
            "Tu es étudiante, tu arrives à Sherbrooke en septembre et tu vis seule.",
            "Ton budget est de 750 $ par mois tout compris, donc tu dois savoir ce qui s'ajoute au loyer.",
            "Tu travailles les fins de semaine et tu étudies le soir : le calme compte beaucoup.",
            "Tu n'as aucun meuble et pas les moyens d'en acheter.",
            "Tu n'as pas d'auto, tu prends l'autobus.",
            "Tu veux savoir où laver ton linge.",
        ],
    },
    "B": {
        "lieu": "Fleurimont",
        "annonce": (
            "Grand 5 ½ dans un quartier familial de Fleurimont, à dix minutes du CHUS. "
            "Trois chambres, sous-sol fini, grande cour arrière. Deux stationnements. "
            "Libre le 1er juillet. 1 390 $ par mois."
        ),
        "proprietaire": [
            "Le chauffage est électrique et aux frais du locataire : environ 150 $ par mois en hiver.",
            "Aucun électroménager n'est fourni, mais les entrées pour la laveuse et la sécheuse sont prêtes au sous-sol.",
            "Les petits chiens sont acceptés. Pas de chat : tu es allergique et tu habites au rez-de-chaussée.",
            "École primaire à cinq minutes à pied, garderie au coin de la rue.",
            "Bail de 12 mois, renouvelable.",
            "Le déneigement de l'entrée est à la charge du locataire.",
            "Il n'y a pas de climatiseur, mais les fenêtres donnent au nord et le logement reste frais l'été.",
            "Le sous-sol fini peut servir de quatrième chambre ou de bureau.",
        ],
        "locataire": [
            "Vous êtes quatre : deux adultes et deux enfants de 7 et 10 ans.",
            "Ton conjoint travaille de nuit au CHUS et dort le jour.",
            "Vous avez un petit chien très tranquille.",
            "Vous possédez déjà une laveuse et une sécheuse, mais aucun autre électroménager.",
            "Votre budget est de 1 500 $ par mois chauffage compris, donc tu dois savoir ce que coûte le chauffage l'hiver.",
            "Tu veux savoir où est l'école la plus proche.",
        ],
    },
    "C": {
        "lieu": "Vieux-Nord",
        "annonce": (
            "4 ½ au rez-de-chaussée d'une maison centenaire, quartier du Vieux-Nord. "
            "Planchers de bois, grandes fenêtres, balcon avant. Près du lac des Nations "
            "et de la piste cyclable. Non-fumeur. Libre le 1er août. 1 050 $ par mois."
        ),
        "proprietaire": [
            "Le chauffage et l'eau chaude sont inclus. L'électricité est aux frais du locataire.",
            "Le réfrigérateur et la cuisinière sont fournis. Il y a une laveuse et une sécheuse dans le logement.",
            "Une place de stationnement dans la cour, en arrière.",
            "Un chat accepté, pas de chien.",
            "La maison a cent ans : les planchers craquent, les fenêtres sont simples et il fait un peu froid en janvier près des fenêtres.",
            "Bail du 1er août au 31 juillet.",
            "Tu habites à l'étage, au-dessus du logement.",
            "Le locataire peut repeindre, mais doit remettre les couleurs d'origine à la fin du bail.",
        ],
        "locataire": [
            "Vous êtes un couple à la retraite et vous avez un chat.",
            "Vous vous déplacez à pied et à vélo : la piste cyclable compte beaucoup.",
            "Vous avez une auto et il vous faut une place pour la stationner.",
            "Votre budget est de 1 200 $ par mois tout compris.",
            "Vous êtes frileux : vous voulez savoir si le logement est chaud en janvier.",
            "Vous aimeriez repeindre le salon en bleu.",
        ],
    },
}


JEU_DE_ROLE_PROBLEMES = {
    "chauffage": {
        "contexte": (
            "Le calorifère du salon d'un logement au dernier étage ne chauffe plus. "
            "Il fait 14 °C. Le disjoncteur du circuit retombe chaque fois qu'on le remonte. "
            "On est au début du mois de novembre."
        ),
        "proprietaire": [
            "Tu possèdes l'immeuble de six logements et tu t'occupes toi-même de la gestion.",
            "Tu ignorais complètement le problème : personne ne t'a appelée avant aujourd'hui.",
            "Ton électricien passe déjà dans l'immeuble jeudi matin ; tu peux lui demander de monter.",
            "Tu gardes deux chauffages d'appoint au sous-sol et tu peux en prêter un le soir même.",
            "Le chauffage et les réparations sont à ta charge, pas à celle du locataire.",
            "Tu veux savoir depuis quand le problème dure et s'il y a du danger immédiat.",
            "Si le locataire te parle d'un disjoncteur qui retombe, tu demandes qu'on n'y touche plus.",
            "Tu refuses d'envoyer quelqu'un avant jeudi, sauf si on te démontre qu'il y a un danger.",
        ],
        "locataire": [
            "Tu habites le logement du dernier étage depuis huit mois et tu travailles de soir.",
            "Il fait 14 °C chez toi depuis avant-hier et ta fille de six ans tousse.",
            "Tu as vérifié le panneau électrique : le disjoncteur retombe chaque fois.",
            "Tu as pris une photo de ton thermomètre avec la date.",
            "Tu veux une date précise de réparation, pas une réponse vague.",
            "Tu aimerais un chauffage d'appoint en attendant.",
        ],
    },
    "moisissure": {
        "contexte": (
            "De la moisissure noire revient dans le coin de la salle de bain, malgré les nettoyages. "
            "Le miroir reste embué très longtemps après la douche. Il n'y a pas de ventilateur "
            "dans la pièce et la fenêtre est petite."
        ),
        "proprietaire": [
            "Tu es propriétaire de l'immeuble depuis quatre ans.",
            "Tu crois d'abord que le locataire aère mal la pièce et tu le dis poliment.",
            "Tu sais qu'il n'y a jamais eu de ventilateur dans cette salle de bain.",
            "Faire installer un ventilateur te coûterait environ 400 $ et tu hésites.",
            "Tu acceptes de venir constater toi-même si le locataire insiste avec des faits précis.",
            "Tu connais un installateur qui pourrait passer dans les deux semaines.",
            "Tu demandes des photos avant de te déplacer.",
        ],
        "locataire": [
            "Ça fait trois mois que la moisissure revient, même après un grand ménage.",
            "Tu laves le mur au vinaigre chaque semaine et elle réapparaît en quatre ou cinq jours.",
            "Tu ouvres la fenêtre après chaque douche, sauf en hiver.",
            "Un de tes enfants fait de l'asthme et tu t'inquiètes pour sa santé.",
            "Tu as lu qu'un ventilateur de salle de bain règle souvent ce genre de problème.",
            "Tu veux une réponse claire : qui fait installer quoi, et quand.",
        ],
    },
    "bruit": {
        "contexte": (
            "Les voisins du logement du dessous reçoivent des amis presque tous les vendredis. "
            "La musique et les conversations sur le balcon durent jusqu'à deux heures du matin. "
            "La situation dure depuis cinq semaines."
        ),
        "proprietaire": [
            "Tu es propriétaire de l'immeuble et tu n'habites pas sur place.",
            "C'est la première plainte que tu reçois au sujet de ces voisins-là.",
            "Tu es mal à l'aise d'intervenir : ce sont de bons payeurs depuis six ans.",
            "Tu proposes d'abord au locataire d'aller en parler lui-même aux voisins.",
            "Si on insiste avec des dates précises, tu acceptes d'envoyer un avis écrit.",
            "Tu rappelles que le bail interdit le bruit excessif après 23 h.",
            "Tu veux savoir quels soirs exactement et depuis combien de temps.",
        ],
        "locataire": [
            "Tu commences à travailler à sept heures du matin et tu ne dors plus le vendredi.",
            "Ça dure depuis cinq semaines, tous les vendredis, parfois le samedi.",
            "Tu as noté les dates des six derniers épisodes dans ton téléphone.",
            "Tu es déjà allé cogner une fois : on t'a répondu poliment, mais rien n'a changé.",
            "Tu ne veux pas te fâcher avec tes voisins, mais tu ne peux plus tolérer la situation.",
            "Tu veux que la propriétaire envoie un avis écrit.",
        ],
    },
}

# Un scénario décrit tout ce qui change d'un jeu de rôle à l'autre : les cas
# jouables, les sujets à couvrir, et la façon dont chaque rôle se comporte.
# Ajouter un module = ajouter une entrée ici, sans toucher au reste du serveur.
JEU_DE_ROLE_SCENARIOS = {
    "louer": {
        "cadre": "une visite de logement",
        "contexte_label": "L'annonce que vous avez tous les deux sous les yeux",
        "cas": JEU_DE_ROLE_LOGEMENTS,
        "sujets": JEU_DE_ROLE_SUJETS,
        "cloture": "Quand les sujets sont couverts, dis-le simplement et termine poliment la visite.",
        # Première réplique, dite par l'élève selon le rôle qu'il joue.
        "ouverture": {
            "proprietaire": "Bonjour, entrez, je vous en prie.",
            "locataire": "Bonjour, je viens pour l'annonce.",
        },
        "roles": {
            "proprietaire": {
                "qui": ("Tu es le ou la propriétaire du logement et tu le fais visiter. "
                        "L'élève est la personne qui vient le visiter."),
                "conduite": ("Réponds honnêtement aux questions, mais ne donne jamais un renseignement "
                             "avant qu'on te le demande — c'est à l'élève d'aller le chercher. "
                             "Si l'élève ne pose pas de question, accueille-le et invite-le à en poser une."),
            },
            "locataire": {
                "qui": ("Tu es la personne qui vient visiter le logement. "
                        "L'élève est le ou la propriétaire et fait visiter."),
                "conduite": ("Pose tes questions une à la fois, en commençant par ce qui compte le plus "
                             "pour ta situation. Réagis brièvement à chaque réponse avant de passer à la suite."),
            },
        },
    },
    "probleme": {
        "cadre": "un appel téléphonique au sujet d'un problème dans un logement loué",
        "contexte_label": "La situation que vous connaissez tous les deux",
        "cas": JEU_DE_ROLE_PROBLEMES,
        "sujets": [
            "la nature exacte du problème",
            "depuis quand il dure (depuis, depuis que, ça fait… que)",
            "la conséquence concrète sur la vie du locataire",
            "ce qui a déjà été tenté",
            "qui va faire faire la réparation et par quel professionnel",
            "la date de l'intervention",
            "ce qui se passe en attendant",
        ],
        "cloture": ("Quand les sujets sont couverts et qu'une entente est prise, "
                    "récapitule l'entente en une phrase et termine poliment l'appel."),
        "ouverture": {
            "locataire": "Bonjour, je vous appelle au sujet d'un problème dans mon logement.",
            "proprietaire": "Bonjour, oui, j'écoute ?",
        },
        "roles": {
            "proprietaire": {
                "qui": ("Tu es le ou la propriétaire de l'immeuble. L'élève est ton locataire "
                        "et t'appelle pour te signaler un problème dans son logement."),
                "conduite": ("Ne propose pas la solution tout de suite : commence par poser des questions "
                             "sur le problème, depuis quand il dure et ce qui a déjà été essayé. "
                             "Sois de bonne foi mais pas trop facile — c'est à l'élève de bien expliquer "
                             "et de formuler une demande claire avant que tu acceptes. Si l'élève reste "
                             "vague, demande des précisions plutôt que de deviner à sa place."),
            },
            "locataire": {
                "qui": ("Tu es le ou la locataire et tu appelles pour signaler un problème dans ton "
                        "logement. L'élève joue la personne propriétaire et te répond."),
                "conduite": ("Expose ton problème en une ou deux phrases, puis laisse l'élève poser "
                             "ses questions. Donne tes renseignements au fur et à mesure qu'on te les "
                             "demande. Insiste poliment si aucune date ne t'est proposée."),
            },
        },
    },
}


def jeu_de_role_system(scenario_id, cas_id, role_eleve):
    """Consigne système du personnage joué par l'assistant.

    `role_eleve` est le rôle de l'ÉLÈVE ; l'assistant joue l'autre. Le texte
    est volontairement stable d'un tour à l'autre — c'est lui qu'on met en
    cache, donc la moindre variation (heure, prénom) coûterait le bénéfice.
    """
    scenario = JEU_DE_ROLE_SCENARIOS[scenario_id]
    cas = scenario["cas"][cas_id]
    ia_role = "proprietaire" if role_eleve == "locataire" else "locataire"
    faits = "\n".join("- " + f for f in cas[ia_role])
    # Les cas de « louer » nomment leur contexte « annonce » depuis l'origine ;
    # les scénarios plus récents utilisent « contexte ».
    contexte = cas.get("contexte") or cas["annonce"]
    role_def = scenario["roles"][ia_role]

    return (
        "Tu joues un rôle dans un exercice oral de francisation au Québec, niveau 4 "
        "(débutant-intermédiaire). Ton interlocuteur est un adulte immigrant qui apprend "
        f"le français. La situation est {scenario['cadre']}.\n\n"
        f"{role_def['qui']}\n\n"
        f"{scenario['contexte_label']} :\n{contexte}\n\n"
        f"Ce que tu sais et que l'élève ignore :\n{faits}\n\n"
        "Comment tu parles :\n"
        "- Deux ou trois phrases maximum par réplique. Jamais de paragraphe.\n"
        "- Français québécois courant et simple, phrases courtes, vocabulaire de tous les jours.\n"
        "- Vouvoie l'élève.\n"
        "- Reste dans ton personnage quoi qu'il arrive. Si l'élève sort du jeu, ramène-le "
        "dans la conversation avec naturel.\n"
        "- Ne corrige jamais le français de l'élève et ne commente jamais ses fautes : "
        "la correction vient à la fin, ailleurs. Si une phrase est incompréhensible, "
        "demande simplement de répéter autrement.\n"
        "- N'écris jamais de balise XML interne ou système dans ta réponse.\n\n"
        f"{role_def['conduite']}\n\n"
        "Les sujets que la conversation doit couvrir : "
        + " · ".join(scenario["sujets"]) + ".\n"
        + scenario["cloture"]
    )


def jeu_de_role_messages(historique, role_eleve, scenario_id="louer"):
    """Normalise l'historique reçu du navigateur en messages pour l'API.

    L'historique vient du client : on ne lui fait confiance ni sur la longueur,
    ni sur les rôles, ni sur la taille des contenus. On garde les 24 derniers
    tours, et l'API exige que la conversation commence par un tour utilisateur.
    """
    messages = []
    for m in (historique or [])[-24:]:
        if not isinstance(m, dict):
            continue
        r = "assistant" if m.get("role") == "assistant" else "user"
        contenu = str(m.get("contenu", "")).strip()[:600]
        if contenu:
            messages.append({"role": r, "content": contenu})

    while messages and messages[0]["role"] == "assistant":
        messages.pop(0)

    if not messages:
        # Premier tour : l'API veut un tour utilisateur pour démarrer, donc on
        # écrit la salutation d'ouverture à la place de l'élève. Elle doit
        # correspondre au rôle qu'il joue — le locataire arrive, le
        # propriétaire accueille — et le handler la renvoie au client pour
        # qu'il l'affiche et la garde dans son historique.
        ouvertures = JEU_DE_ROLE_SCENARIOS[scenario_id]["ouverture"]
        messages = [{"role": "user", "content": ouvertures[role_eleve]}]
    return messages


# ── Gestionnaire HTTP ────────────────────────────────────────────────────────

class Handler(http.server.SimpleHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        pass  # silencieux

    def end_headers(self):
        # Les pages HTML (activités, portail élève, admin) changent à chaque
        # déploiement. Sans Cache-Control, le navigateur applique son cache
        # « heuristique » et peut resservir une vieille copie pendant des heures
        # sans jamais redemander au serveur — un élève voyait alors l'activité
        # d'avant la mise en ligne. « no-cache » n'interdit pas le cache : il
        # force seulement une revalidation, donc un 304 léger si rien n'a changé.
        # Les feuilles de style et les scripts suivent la même règle : depuis
        # le multi-groupes, un app.js périmé appellerait les anciennes routes
        # et casserait la page au lieu de simplement mal l'habiller.
        path = urllib.parse.urlparse(self.path).path
        if path.endswith((".html", ".css", ".js")) or path.endswith("/") or path == "":
            self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PATCH, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Prof-Token")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        params = urllib.parse.parse_qs(parsed.query)

        # Sonde de santé Railway : doit rester publique et sans effet de bord.
        if path == "/api/health":
            json_response(self, {"ok": True})
            return
        if path == "/api/prof/me":
            self._handle_prof_me()
            return
        if path == "/api/prof/groupes":
            self._handle_groups_list()
            return
        if path == "/api/prof/enseignants":
            self._handle_teachers_list()
            return

        if path == "/api/debug":
            if not self._require_teacher():
                return
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
            # Catalogue commun, mais les dates sont celles du groupe demandé.
            teacher = self._require_teacher()
            if not teacher:
                return
            group_id = self._group_from_params(teacher, params)
            if group_id is None:
                return
            json_response(self, activities_for_group(group_id))
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
        if path in ("/api/admin/students", "/api/admin/access-log", "/api/admin/progress"):
            teacher = self._require_teacher()
            if not teacher:
                return
            group_id = self._group_from_params(teacher, params)
            if group_id is None:
                return
            if path == "/api/admin/students":
                json_response(self, [s for s in load_students()
                                     if s.get("groupId") == group_id])
                return
            # Journal et progression : filtrés par les élèves du groupe, avec
            # repli sur le groupId inscrit dans l'entrée pour les élèves partis.
            student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
            source = load_access_log() if path == "/api/admin/access-log" else load_progress()
            json_response(self, [
                e for e in source
                if e.get("studentId") in student_ids or e.get("groupId") == group_id
            ])
            return
        if path == "/api/admin/oral-submissions":
            self._handle_oral_submissions_list(params)
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
        elif path == "/api/prof/setup":
            self._handle_prof_setup()
        elif path == "/api/prof/login":
            self._handle_prof_login()
        elif path == "/api/prof/logout":
            self._handle_prof_logout()
        elif path == "/api/prof/motdepasse":
            self._handle_prof_password()
        elif path == "/api/prof/groupes":
            self._handle_group_add()
        elif path == "/api/prof/enseignants":
            self._handle_teacher_add()
        elif path == "/api/student/access":
            self._handle_log_access()
        elif path == "/api/admin/students":
            self._handle_add_student()
        elif path == "/api/admin/clear-log":
            self._handle_clear_log()
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
        elif path == "/api/vocab/signaler":
            self._handle_vocab_report()
        elif path == "/api/vocab/check-answer":
            self._handle_vocab_check_answer()
        elif path == "/api/analyze-grammar":
            self._handle_analyze_grammar()
        elif path == "/api/check-written":
            self._handle_check_written()
        elif path == "/api/jeu-de-role":
            self._handle_jeu_de_role()
        elif path == "/api/voix":
            self._handle_voix()
        elif path == "/api/outils/traduire":
            self._handle_outil_traduire()
        elif path == "/api/outils/simplifier":
            self._handle_outil_simplifier()
        elif path == "/api/outils/assistant":
            self._handle_outil_assistant()
        elif path == "/api/analyser-erreurs":
            self._handle_analyser_erreurs()
        elif path == "/api/oral/submit":
            self._handle_oral_submit()
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
            teacher = self._require_teacher()
            if not teacher:
                return
            try:
                student_id = int(path.split("/")[4])
            except (ValueError, IndexError):
                self.send_error(400, "ID invalide")
                return
            body = self._read_json_body()
            students = load_students()
            target = next((s for s in students if s["id"] == student_id), None)
            if target is None:
                json_response(self, {"error": "Élève introuvable"}, 404)
                return
            if self._require_group(teacher, target.get("groupId")) is None:
                return
            if "prenom" in body:
                target["prenom"] = body["prenom"]
            if "groupId" in body:
                # Déplacer un élève : le groupe d'arrivée doit aussi être à soi
                if self._require_group(teacher, body["groupId"]) is None:
                    return
                target["groupId"] = int(body["groupId"])
            save_students(students)
            json_response(self, {"success": True})
        elif re.match(r"^/api/prof/groupes/\d+$", path):
            self._handle_group_update(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/enseignants/\d+$", path):
            try:
                self._handle_teacher_update(int(path.rsplit("/", 1)[1]))
            except ValueError:
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
        elif re.match(r"^/api/admin/oral-submissions/[\w-]+$", path):
            self._handle_oral_submission_delete(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/groupes/\d+$", path):
            self._handle_group_delete(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/enseignants/\d+$", path):
            try:
                self._handle_teacher_delete(int(path.rsplit("/", 1)[1]))
            except ValueError:
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
        if not self._require_teacher():
            return
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
            "categorie": normalize_categorie(form.getvalue("categorie", "")),
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
        if not self._require_teacher():
            return
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

        categorie = form.getvalue("categorie", "")
        if categorie in CATEGORIES:
            target["categorie"] = categorie

        save_activities(activities)
        json_response(self, {"success": True, "activity": target})

    def _handle_dates(self, activity_id):
        """Les dates n'appartiennent plus à l'activité mais au groupe : deux
        enseignants planifient la même activité à des moments différents."""
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        group_id = self._require_group(teacher, body.get("groupId"))
        if group_id is None:
            return

        if not any(a["id"] == activity_id for a in load_activities()):
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        entry = set_schedule_dates(group_id, activity_id, body)
        json_response(self, {"success": True, "dates": entry})

    def _handle_clear_log(self):
        """Ne vide que le journal du groupe demandé."""
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._require_group(teacher, self._read_json_body().get("groupId"))
        if group_id is None:
            return
        student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
        save_access_log([
            e for e in load_access_log()
            if not (e.get("studentId") in student_ids or e.get("groupId") == group_id)
        ])
        json_response(self, {"success": True})

    def _handle_clear_file(self, activity_id):
        if not self._require_teacher():
            return
        body = self._read_json_body()
        field = body.get("field", "")

        allowed = ("thumbnail", "interactive", "studentDoc", "slideshow", "planCours", "autres", "parcours")
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
        if not self._require_teacher():
            return
        body = self._read_json_body()
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
        if not self._require_teacher():
            return
        activities = load_activities()
        target = next((a for a in activities if a["id"] == activity_id), None)

        if not target:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        for key in ("thumbnail", "interactive", "studentDoc", "slideshow", "planCours", "autres", "parcours"):
            self._delete_file(target.get(key, ""), key)

        activities = [a for a in activities if a["id"] != activity_id]
        save_activities(activities)
        # La planification de tous les groupes suit la suppression
        save_schedule([e for e in load_schedule() if e.get("activityId") != activity_id])
        json_response(self, {"success": True})

    # ── Comptes enseignants ───────────────────────────────────────────────

    def _read_json_body(self):
        length = int(self.headers.get("Content-Length", 0))
        if not length:
            return {}
        try:
            return json.loads(self.rfile.read(length))
        except json.JSONDecodeError:
            return {}

    def _current_teacher(self):
        token = self.headers.get("X-Prof-Token", "")
        return teacher_from_token(token)

    def _require_teacher(self, admin=False):
        """Renvoie l'enseignant connecté, ou None après avoir répondu 401/403."""
        teacher = self._current_teacher()
        if not teacher:
            json_response(self, {"error": "Connexion enseignante requise"}, 401)
            return None
        if admin and teacher.get("role") != "admin":
            json_response(self, {"error": "Réservé à l'administrateur"}, 403)
            return None
        return teacher

    def _require_group(self, teacher, group_id):
        """Valide que le groupe demandé existe et appartient à l'enseignant."""
        try:
            group_id = int(group_id)
        except (TypeError, ValueError):
            json_response(self, {"error": "Groupe manquant"}, 400)
            return None
        if not teacher_can_access_group(teacher, group_id):
            json_response(self, {"error": "Ce groupe ne vous appartient pas"}, 403)
            return None
        return group_id

    def _group_from_params(self, teacher, params):
        return self._require_group(teacher, params.get("groupId", [None])[0])

    def _handle_prof_setup(self):
        """Création du tout premier compte. Refusée dès qu'un compte existe."""
        if load_teachers():
            json_response(self, {"error": "L'installation est déjà faite"}, 409)
            return
        body = self._read_json_body()
        email = normalize_email(body.get("courriel"))
        password = body.get("motDePasse", "")
        nom = (body.get("nom", "") or "").strip()
        if not email or "@" not in email:
            json_response(self, {"error": "Courriel invalide"}, 400)
            return
        if len(password) < 8:
            json_response(self, {"error": "Le mot de passe doit faire au moins 8 caractères"}, 400)
            return
        teacher = {
            "id": 1,
            "nom": nom or email.split("@")[0],
            "courriel": email,
            "motDePasse": hash_password(password),
            "role": "admin",
            "createdAt": date.today().isoformat(),
        }
        save_teachers([teacher])
        # Le groupe historique créé par la migration n'avait pas de titulaire
        groups = load_groups()
        for g in groups:
            if not g.get("teacherId"):
                g["teacherId"] = teacher["id"]
        save_groups(groups)
        token = create_session(teacher["id"])
        json_response(self, {
            "success": True,
            "token": token,
            "enseignant": public_teacher(teacher),
            "groupes": groups_of_teacher(teacher),
        }, 201)

    def _handle_prof_login(self):
        body = self._read_json_body()
        email = normalize_email(body.get("courriel"))
        password = body.get("motDePasse", "")
        teacher = next((t for t in load_teachers()
                        if normalize_email(t.get("courriel")) == email), None)
        if not teacher or not verify_password(password, teacher.get("motDePasse", "")):
            json_response(self, {"error": "Courriel ou mot de passe invalide"}, 401)
            return
        token = create_session(teacher["id"])
        json_response(self, {
            "success": True,
            "token": token,
            "enseignant": public_teacher(teacher),
            "groupes": groups_of_teacher(teacher),
        })

    def _handle_prof_logout(self):
        destroy_session(self.headers.get("X-Prof-Token", ""))
        json_response(self, {"success": True})

    def _handle_prof_me(self):
        teacher = self._current_teacher()
        if not teacher:
            # Pas une erreur : la page de connexion s'en sert pour savoir s'il
            # faut afficher l'écran d'installation ou celui de connexion.
            json_response(self, {
                "connecte": False,
                "installationRequise": not load_teachers(),
            })
            return
        json_response(self, {
            "connecte": True,
            "installationRequise": False,
            "enseignant": public_teacher(teacher),
            "groupes": groups_of_teacher(teacher),
        })

    def _handle_prof_password(self):
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        if not verify_password(body.get("ancien", ""), teacher.get("motDePasse", "")):
            json_response(self, {"error": "Mot de passe actuel invalide"}, 403)
            return
        nouveau = body.get("nouveau", "")
        if len(nouveau) < 8:
            json_response(self, {"error": "Le nouveau mot de passe doit faire au moins 8 caractères"}, 400)
            return
        teachers = load_teachers()
        for t in teachers:
            if t["id"] == teacher["id"]:
                t["motDePasse"] = hash_password(nouveau)
        save_teachers(teachers)
        json_response(self, {"success": True})

    # ── Groupes ───────────────────────────────────────────────────────────

    def _handle_groups_list(self):
        teacher = self._require_teacher()
        if not teacher:
            return
        groups = groups_of_teacher(teacher)
        students = load_students()
        teachers_by_id = {t["id"]: t for t in load_teachers()}
        enriched = []
        for g in groups:
            titulaire = teachers_by_id.get(g.get("teacherId"))
            enriched.append({
                **g,
                "nbEleves": sum(1 for s in students if s.get("groupId") == g["id"]),
                "titulaire": titulaire.get("nom", "") if titulaire else "",
            })
        json_response(self, enriched)

    def _handle_group_add(self):
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        nom = (body.get("nom", "") or "").strip()
        if not nom:
            json_response(self, {"error": "Le nom du groupe est requis"}, 400)
            return
        # Un administrateur peut créer un groupe pour un autre enseignant
        titulaire_id = teacher["id"]
        if teacher.get("role") == "admin" and body.get("teacherId"):
            try:
                candidat = int(body["teacherId"])
            except (TypeError, ValueError):
                json_response(self, {"error": "Enseignant invalide"}, 400)
                return
            if not any(t["id"] == candidat for t in load_teachers()):
                json_response(self, {"error": "Enseignant introuvable"}, 404)
                return
            titulaire_id = candidat
        groups = load_groups()
        group = {
            "id": max((g["id"] for g in groups), default=0) + 1,
            "nom": nom[:80],
            "teacherId": titulaire_id,
            "createdAt": date.today().isoformat(),
        }
        groups.append(group)
        save_groups(groups)
        json_response(self, {"success": True, "groupe": group}, 201)

    def _handle_group_update(self, group_id):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._require_group(teacher, group_id)
        if group_id is None:
            return
        body = self._read_json_body()
        groups = load_groups()
        for g in groups:
            if g["id"] == group_id:
                if "nom" in body:
                    nom = (body["nom"] or "").strip()
                    if not nom:
                        json_response(self, {"error": "Le nom du groupe est requis"}, 400)
                        return
                    g["nom"] = nom[:80]
                # Seul un administrateur peut réaffecter un groupe
                if "teacherId" in body and teacher.get("role") == "admin":
                    g["teacherId"] = body["teacherId"]
        save_groups(groups)
        json_response(self, {"success": True})

    def _handle_group_delete(self, group_id):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._require_group(teacher, group_id)
        if group_id is None:
            return
        students = load_students()
        if any(s.get("groupId") == group_id for s in students):
            json_response(self, {
                "error": "Ce groupe contient encore des élèves. "
                         "Supprimez-les ou déplacez-les d'abord."
            }, 409)
            return
        save_groups([g for g in load_groups() if g["id"] != group_id])
        save_schedule([e for e in load_schedule() if e.get("groupId") != group_id])
        json_response(self, {"success": True})

    # ── Gestion des enseignants (administrateur) ──────────────────────────

    def _handle_teachers_list(self):
        teacher = self._require_teacher(admin=True)
        if not teacher:
            return
        groups = load_groups()
        json_response(self, [
            {**public_teacher(t),
             "nbGroupes": sum(1 for g in groups if g.get("teacherId") == t["id"])}
            for t in load_teachers()
        ])

    def _handle_teacher_add(self):
        admin = self._require_teacher(admin=True)
        if not admin:
            return
        body = self._read_json_body()
        email = normalize_email(body.get("courriel"))
        password = body.get("motDePasse", "")
        nom = (body.get("nom", "") or "").strip()
        if not email or "@" not in email:
            json_response(self, {"error": "Courriel invalide"}, 400)
            return
        teachers = load_teachers()
        if any(normalize_email(t.get("courriel")) == email for t in teachers):
            json_response(self, {"error": "Ce courriel est déjà utilisé"}, 409)
            return
        if len(password) < 8:
            json_response(self, {"error": "Le mot de passe doit faire au moins 8 caractères"}, 400)
            return
        teacher = {
            "id": max((t["id"] for t in teachers), default=0) + 1,
            "nom": nom or email.split("@")[0],
            "courriel": email,
            "motDePasse": hash_password(password),
            "role": "admin" if body.get("role") == "admin" else "prof",
            "createdAt": date.today().isoformat(),
        }
        teachers.append(teacher)
        save_teachers(teachers)
        json_response(self, {"success": True, "enseignant": public_teacher(teacher)}, 201)

    def _handle_teacher_update(self, teacher_id):
        admin = self._require_teacher(admin=True)
        if not admin:
            return
        body = self._read_json_body()
        teachers = load_teachers()
        target = next((t for t in teachers if t["id"] == teacher_id), None)
        if target is None:
            json_response(self, {"error": "Enseignant introuvable"}, 404)
            return
        if "nom" in body:
            target["nom"] = (body["nom"] or "").strip() or target["nom"]
        if "role" in body:
            # Ne jamais laisser l'installation sans administrateur
            if body["role"] != "admin" and target.get("role") == "admin" \
                    and sum(1 for t in teachers if t.get("role") == "admin") <= 1:
                json_response(self, {"error": "Il doit rester au moins un administrateur"}, 409)
                return
            target["role"] = "admin" if body["role"] == "admin" else "prof"
        if body.get("motDePasse"):
            if len(body["motDePasse"]) < 8:
                json_response(self, {"error": "Le mot de passe doit faire au moins 8 caractères"}, 400)
                return
            target["motDePasse"] = hash_password(body["motDePasse"])
        save_teachers(teachers)
        json_response(self, {"success": True, "enseignant": public_teacher(target)})

    def _handle_teacher_delete(self, teacher_id):
        admin = self._require_teacher(admin=True)
        if not admin:
            return
        if teacher_id == admin["id"]:
            json_response(self, {"error": "Vous ne pouvez pas supprimer votre propre compte"}, 409)
            return
        teachers = load_teachers()
        target = next((t for t in teachers if t["id"] == teacher_id), None)
        if target is None:
            json_response(self, {"error": "Enseignant introuvable"}, 404)
            return
        if any(g.get("teacherId") == teacher_id for g in load_groups()):
            json_response(self, {
                "error": "Cet enseignant a encore des groupes. "
                         "Réaffectez-les ou supprimez-les d'abord."
            }, 409)
            return
        save_teachers([t for t in teachers if t["id"] != teacher_id])
        # Déconnexion immédiate du compte supprimé
        sessions = {tok: s for tok, s in load_sessions().items()
                    if s.get("teacherId") != teacher_id}
        save_sessions(sessions)
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
        group = find_group(student.get("groupId"))
        json_response(self, {
            "success": True,
            "studentId": student["id"],
            "label": student.get("label", ""),
            "prenom": student.get("prenom", ""),
            "groupId": student.get("groupId"),
            "groupe": group.get("nom", "") if group else "",
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

        available_pool = get_student_vocab_pool(student.get("groupId"))
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
        """Traduit un mot, sa définition et — si elle est fournie — sa phrase
        d'exemple.

        Deux façons de désigner le mot :
        - `wordId` : un mot de VOCAB_BANK (vocabulaire-flash, historique) ;
        - `mot` + `definition` (+ `exemple`) : n'importe quel mot d'un module,
          ce qui permet au gabarit de vocabulaire de servir tous les modules
          sans que leur liste ait à être recopiée côté serveur.
        Le résultat est mis en cache sur disque, partagé par toute la classe.
        """
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        language = (body.get("language") or body.get("langue") or "").strip()[:60]
        if not language:
            json_response(self, {"error": "Langue non précisée"}, 400)
            return

        word_id = body.get("wordId", "")
        if word_id:
            word = next((w for w in VOCAB_BANK if w["id"] == word_id), None)
            if word is None:
                json_response(self, {"error": "Mot inconnu"}, 400)
                return
            mot, definition, exemple = word["mot"], word["definition"], word["exemple"]
        else:
            # Les modules stockent la phrase d'exemple en HTML (<strong>) : on la
            # nettoie avant de l'envoyer, sinon le modèle traduit les balises.
            mot = strip_tags(body.get("mot", ""))[:120]
            definition = strip_tags(body.get("definition", ""))[:400]
            exemple = strip_tags(body.get("exemple", ""))[:400]
            if not mot or not definition:
                json_response(self, {"error": "Mot ou définition manquant"}, 400)
                return

        cache_key = translation_key(language, mot, definition)
        cached = load_translations().get(cache_key)
        if cached:
            json_response(self, dict(cached, cache=True))
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
            "de la phrase d'exemple complète, ou une chaîne vide s'il n'y a pas "
            "d'exemple. Utilise une traduction naturelle et courante, pas littérale."
        )
        user_content = "Mot : %s\nDéfinition : %s" % (mot, definition)
        if exemple:
            user_content += "\nExemple : %s" % exemple

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=300)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        traduction = {
            "traduction": parsed.get("traduction", ""),
            "definitionTraduite": parsed.get("definitionTraduite", ""),
            "exempleTraduit": parsed.get("exempleTraduit", "") if exemple else "",
        }
        if traduction["traduction"] or traduction["definitionTraduite"]:
            save_translation(cache_key, traduction)
        json_response(self, traduction)

    def _handle_vocab_report(self):
        """Journalise une traduction jugée douteuse par un élève. Pas d'écran :
        le fichier sert plus tard à constituer une liste révisée à la main."""
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        log_translation_report({
            "date": datetime.now().isoformat(timespec="seconds"),
            "module": strip_tags(body.get("module", ""))[:80],
            "mot": strip_tags(body.get("mot", ""))[:120],
            "langue": strip_tags(body.get("langue", ""))[:60],
            "traduction": strip_tags(body.get("traduction", ""))[:400],
        })
        json_response(self, {"success": True})

    def _handle_student_dashboard(self, params):
        code = params.get("code", [""])[0].strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        group_id = student.get("groupId")
        available_ids = get_available_activity_ids(group_id)
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
        pool_ids = {w["id"] for w in get_student_vocab_pool(group_id)}
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
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        today = date.today().isoformat()
        # Le catalogue est commun, mais les dates viennent du groupe de l'élève.
        activities = activities_for_group(student.get("groupId"))
        result = []
        for a in activities:
            dp = a.get("datePrevue", "")
            df = a.get("dateFin", "")
            # Sans date de disponibilité, l'activité n'est pas offerte à ce
            # groupe : l'élève ne la voit pas du tout, même pas « à venir ».
            if not dp:
                continue
            # Masquer les activités dont la période est terminée
            if df and df < today:
                continue
            available = dp <= today
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
                "categorie": a.get("categorie", "atelier"),
                "nouveauDesign": bool(a.get("nouveauDesign")),
                "nouveauDesignColor": a.get("nouveauDesignColor", ""),
                "nouveauDesignTint": a.get("nouveauDesignTint", ""),
                "files": {
                    # « parcours » : variante diapositive par diapositive d'une
                    # activité interactive. Pas de téléversement depuis l'admin —
                    # le chemin est écrit dans data/activities.json.
                    "parcours": a.get("parcours", "") if available else "",
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
            "groupId": student.get("groupId"),
            "activityId": body.get("activityId"),
            "activityTitle": body.get("activityTitle", ""),
            "file": body.get("file", ""),
            "timestamp": datetime.now().isoformat(timespec="seconds"),
        }
        log.append(entry)
        save_access_log(log)
        json_response(self, {"success": True})

    def _call_anthropic_dialogue(self, system_prompt, messages, max_tokens=300):
        """Appelle l'API Anthropic pour une conversation à plusieurs tours et
        renvoie (texte, None) ou (None, (message d'erreur, code)).

        Diffère de _call_anthropic_json sur trois points : l'historique complet
        est envoyé (et non un seul message), la réponse est du texte libre, et
        la consigne système est marquée pour la mise en cache — elle ne change
        pas d'un tour à l'autre, donc à partir du deuxième échange elle est
        facturée au dixième au lieu du plein tarif.
        """
        api_key = os.environ.get("ANTHROPIC_API_KEY", "")
        if not api_key:
            return None, ("Clé API non configurée sur le serveur", 503)

        payload = json.dumps({
            "model": "claude-opus-5",
            "max_tokens": max_tokens,
            # Une réplique de deux phrases n'a rien à gagner d'une longue
            # réflexion, et la classe attend la réponse : effort au minimum.
            # On garde la réflexion adaptative plutôt que de la désactiver —
            # désactivée, ce modèle laisse parfois échapper des balises
            # internes dans le texte visible.
            "thinking": {"type": "adaptive"},
            "output_config": {"effort": "low"},
            "system": [{
                "type": "text",
                "text": system_prompt,
                "cache_control": {"type": "ephemeral"},
            }],
            "messages": messages,
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
            with urllib.request.urlopen(req, timeout=40) as resp:
                result = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            print(f"[WARN] Anthropic API HTTPError {e.code}: {detail[:300]}", flush=True)
            return None, ("L'assistant est momentanément indisponible", 502)
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"[WARN] Anthropic API injoignable : {e}", flush=True)
            return None, ("L'assistant est momentanément indisponible", 502)

        # Le refus est un 200 avec un contenu vide : à vérifier avant de lire
        # les blocs, sinon on plante sur une liste vide.
        if result.get("stop_reason") == "refusal":
            return None, ("L'assistant ne peut pas répondre à ce message", 400)

        texte = " ".join(
            b.get("text", "") for b in result.get("content", [])
            if b.get("type") == "text"
        ).strip()
        if not texte:
            return None, ("Réponse vide de l'assistant", 502)

        usage = result.get("usage", {})
        print("[jeu-de-role] entrée %s · cache lu %s · sortie %s" % (
            usage.get("input_tokens"), usage.get("cache_read_input_tokens"),
            usage.get("output_tokens")), flush=True)
        return texte, None

    def _handle_jeu_de_role(self):
        """Un tour de conversation du jeu de rôle « louer un logement ».

        Corps attendu : {code, scenario, cas, role: 'locataire'|'proprietaire',
        historique: [{role:'user'|'assistant', contenu}]}.
        `role` est celui que joue l'ÉLÈVE ; l'assistant prend l'autre.

        `scenario` vaut 'louer' par défaut et `cas` accepte l'ancien nom
        `logement` : les modules déjà en ligne continuent de fonctionner sans
        être modifiés.
        """
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return

        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        scenario = body.get("scenario") or "louer"
        cas = body.get("cas") or body.get("logement", "")
        role = body.get("role", "")
        if scenario not in JEU_DE_ROLE_SCENARIOS:
            json_response(self, {"error": "Scénario inconnu"}, 400)
            return
        if cas not in JEU_DE_ROLE_SCENARIOS[scenario]["cas"] or role not in ("locataire", "proprietaire"):
            json_response(self, {"error": "Cas ou rôle inconnu"}, 400)
            return

        recu = body.get("historique")
        messages = jeu_de_role_messages(recu, role, scenario)
        premier_tour = not recu

        texte, err = self._call_anthropic_dialogue(
            jeu_de_role_system(scenario, cas, role), messages)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        out = {"reponse": texte}
        if premier_tour:
            # La salutation qu'on a écrite pour l'élève : le client l'affiche
            # et la range dans son historique, sinon elle serait perdue au
            # tour suivant et l'assistant se présenterait deux fois.
            out["ouverture"] = messages[0]["content"]
        json_response(self, out)

    def _handle_voix(self):
        """Lit une réplique du jeu de rôle avec une voix ElevenLabs.

        Corps attendu : {code, texte, role}. `role` est celui de l'ÉLÈVE ; la
        voix rendue est donc celle du personnage joué par l'assistant. Renvoie
        du MP3 brut ; le client retombe sur la voix du navigateur en cas
        d'échec, donc une panne ici dégrade le son sans casser l'exercice.
        """
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return

        if not validate_student_code(body.get("code", "").strip().upper()):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
        if not api_key:
            json_response(self, {"error": "Voix non configurée sur le serveur"}, 503)
            return

        # Borne de coût : ElevenLabs facture au caractère, et une réplique du
        # jeu de rôle tient largement sous cette limite.
        texte = str(body.get("texte", "")).strip()[:400]
        if not texte:
            json_response(self, {"error": "Texte vide"}, 400)
            return

        if body.get("voix") == "lecture":
            # La barre d'outils lit un passage du module : aucun rôle en jeu,
            # une voix fixe pour que la lecture ne change pas de timbre.
            voix = VOIX_LECTURE
        else:
            # L'assistant joue l'autre rôle : propriétaire si l'élève est locataire.
            voix = (VOIX_JEU_DE_ROLE["proprietaire"]
                    if body.get("role") == "locataire"
                    else VOIX_JEU_DE_ROLE["locataire"])

        payload = json.dumps({
            "text": texte,
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.75},
        }).encode("utf-8")
        req = urllib.request.Request(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
            data=payload,
            headers={"xi-api-key": api_key, "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                audio = resp.read()
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="replace")
            print(f"[WARN] ElevenLabs HTTPError {e.code}: {detail[:200]}", flush=True)
            json_response(self, {"error": "La voix est momentanément indisponible"}, 502)
            return
        except (urllib.error.URLError, TimeoutError) as e:
            print(f"[WARN] ElevenLabs injoignable : {e}", flush=True)
            json_response(self, {"error": "La voix est momentanément indisponible"}, 502)
            return

        print(f"[voix] {len(texte)} caractères → {len(audio)} octets", flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "audio/mpeg")
        self.send_header("Content-Length", str(len(audio)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(audio)

    # ══ BARRE D'OUTILS ÉLÈVE ══════════════════════════════════════════════
    # Trois routes qui servent les outils permanents d'un module : traduire un
    # passage quelconque, le reformuler en français plus simple, et répondre
    # aux questions de l'élève. Les deux premières sont mises en cache sur
    # disque : trente élèves surlignent les mêmes consignes, on paie une fois.

    def _outil_corps(self, cle_texte="texte", maxi=900):
        """Lecture et contrôle communs aux trois routes. Renvoie
        (body, texte) ou (None, None) après avoir déjà répondu en erreur."""
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return None, None
        if not validate_student_code(body.get("code", "").strip().upper()):
            json_response(self, {"error": "Non autorisé"}, 401)
            return None, None
        texte = strip_tags(str(body.get(cle_texte, ""))).strip()[:maxi]
        if not texte:
            json_response(self, {"error": "Texte vide"}, 400)
            return None, None
        return body, texte

    def _handle_outil_traduire(self):
        """Traduit un passage du module vers la langue maternelle de l'élève.
        Corps : {code, langue, texte, contexte?}. Le français n'est jamais
        remplacé côté client : la traduction s'ajoute sous le passage."""
        body, texte = self._outil_corps()
        if body is None:
            return

        langue = strip_tags(str(body.get("langue", ""))).strip()[:60]
        if not langue:
            json_response(self, {"error": "Langue non précisée"}, 400)
            return

        cle = outils_key("trad", langue, texte)
        cached = load_outils_cache().get(cle)
        if cached:
            json_response(self, {"traduction": cached, "cache": True})
            return

        system_prompt = (
            "Tu traduis pour des élèves adultes en francisation au Québec "
            f"(niveau débutant-intermédiaire). Langue cible : {langue}. "
            "Traduis le passage français qu'on te donne, fidèlement mais dans "
            "une langue courante et naturelle — pas de calque mot à mot. "
            "Garde les noms propres tels quels. Si le passage est une consigne "
            "d'exercice, traduis-la comme une consigne. Réponds UNIQUEMENT "
            'avec un objet JSON valide : {"traduction": "..."} — rien avant, '
            "rien après, aucun commentaire."
        )
        contexte = strip_tags(str(body.get("contexte", ""))).strip()[:200]
        user_content = texte if not contexte else (
            "Contexte (ne pas traduire) : %s\n\nPassage à traduire :\n%s" % (contexte, texte))

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=900)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        traduction = str(parsed.get("traduction", "")).strip()
        if not traduction:
            json_response(self, {"error": "Traduction vide"}, 502)
            return
        save_outils_entry(cle, traduction)
        json_response(self, {"traduction": traduction})

    def _handle_outil_simplifier(self):
        """Reformule un passage en français plus simple — SANS traduire. C'est
        la moitié du travail de la traduction, mais l'élève reste dans la
        langue cible. Corps : {code, texte}."""
        body, texte = self._outil_corps()
        if body is None:
            return

        cle = outils_key("simp", "", texte)
        cached = load_outils_cache().get(cle)
        if cached:
            json_response(self, dict(cached, cache=True))
            return

        system_prompt = (
            "Tu es enseignant de francisation (FLS) au Québec, niveau 4. Tu "
            "réécris un passage en français PLUS SIMPLE, pour un adulte qui "
            "apprend la langue. Règles : phrases courtes (une idée par "
            "phrase), vocabulaire courant, présent de l'indicatif quand c'est "
            "possible, pas de tournure passive, pas de subordonnée longue. Tu "
            "gardes TOUT le sens — tu ne résumes pas, tu ne commentes pas, tu "
            "ne traduis pas. Tu restes en français. Repère aussi le mot le "
            "plus difficile du passage et explique-le en une courte phrase "
            "simple. Réponds UNIQUEMENT avec un objet JSON valide : "
            '{"simple": "...", "mot": "...", "explication": "..."} — '
            '"mot" et "explication" peuvent être des chaînes vides s\'il n\'y '
            "a pas de mot difficile."
        )

        parsed, err = self._call_anthropic_json(system_prompt, texte, max_tokens=700)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        out = {
            "simple": str(parsed.get("simple", "")).strip(),
            "mot": str(parsed.get("mot", "")).strip(),
            "explication": str(parsed.get("explication", "")).strip(),
        }
        if not out["simple"]:
            json_response(self, {"error": "Reformulation vide"}, 502)
            return
        save_outils_entry(cle, out)
        json_response(self, out)

    def _handle_outil_assistant(self):
        """Répond aux questions de l'élève sur le module en cours.

        Corps : {code, langue?, module?, section?, contexte?, historique}.
        `historique` est la liste complète des tours ({role, content}) : la
        conversation n'est pas stockée côté serveur, c'est le client qui la
        porte, comme pour le jeu de rôle.

        La consigne système tient en trois interdits — répondre simple, ne
        jamais donner la réponse d'un exercice, rester sur le module. Sans le
        deuxième, l'outil devient un distributeur de corrigés.
        """
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return
        if not validate_student_code(body.get("code", "").strip().upper()):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        recu = body.get("historique")
        if not isinstance(recu, list) or not recu:
            json_response(self, {"error": "Question manquante"}, 400)
            return
        # On ne garde que les douze derniers tours : au-delà, la conversation
        # coûte cher et n'aide plus. Le contenu est borné, un élève ne peut pas
        # faire passer un long texte pour de l'historique.
        messages = []
        for tour in recu[-12:]:
            if not isinstance(tour, dict):
                continue
            role = "assistant" if tour.get("role") == "assistant" else "user"
            contenu = strip_tags(str(tour.get("content", ""))).strip()[:600]
            if contenu:
                messages.append({"role": role, "content": contenu})
        if not messages or messages[-1]["role"] != "user":
            json_response(self, {"error": "Question manquante"}, 400)
            return

        langue = strip_tags(str(body.get("langue", ""))).strip()[:60]
        titre = strip_tags(str(body.get("section", ""))).strip()[:120]
        contexte = strip_tags(str(body.get("contexte", ""))).strip()[:6000]

        system_prompt = (
            "Tu es un assistant d'apprentissage intégré à un module de "
            "francisation (FLS) au Québec, niveau 4 — des adultes immigrants "
            "débutants-intermédiaires. Tu aides UN élève pendant qu'il "
            "travaille.\n\n"
            "TROIS RÈGLES ABSOLUES :\n"
            "1. Tu écris en français SIMPLE : phrases courtes, vocabulaire "
            "courant, présent quand c'est possible. Deux ou trois phrases par "
            "réponse, pas davantage. Tu peux mettre un mot important en gras "
            "avec **deux astérisques**.\n"
            "2. Tu ne donnes JAMAIS la réponse d'un exercice. Si l'élève la "
            "demande, tu refuses gentiment et tu donnes un indice : tu "
            "reformules la question, tu renvoies à la phrase du dialogue où se "
            "trouve l'information, ou tu poses une question plus facile. "
            "Expliquer un mot, une règle ou une consigne, ça, tu le fais "
            "volontiers.\n"
            "3. Tu restes sur le module. Si on te parle d'autre chose, tu "
            "réponds une phrase et tu ramènes vers la tâche.\n\n"
            "Tu tutoies l'élève avec « vous » (usage québécois en classe "
            "d'adultes). Tu es chaleureux, jamais condescendant. Tu ne "
            "corriges pas les fautes de la question de l'élève : il écrit pour "
            "se faire comprendre, pas pour être évalué."
        )
        if langue:
            system_prompt += (
                f"\n\nLa langue maternelle de l'élève est : {langue}. Tu "
                "réponds TOUJOURS en français d'abord. Tu ajoutes une "
                "traduction dans sa langue seulement s'il la demande, ou si "
                "un mot est vraiment intraduisible autrement — dans ce cas, "
                "mets la traduction sur une dernière ligne, précédée de « 🌐 »."
            )
        if titre:
            system_prompt += f"\n\nL'élève travaille en ce moment sur : {titre}."
        if contexte:
            system_prompt += (
                "\n\nVoici le texte du module que l'élève a sous les yeux. "
                "Appuie-toi dessus, c'est ta seule source sur le contenu :\n\n"
                f"{contexte}"
            )

        texte, err = self._call_anthropic_dialogue(system_prompt, messages, max_tokens=400)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return
        json_response(self, {"reponse": texte})

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

    def _handle_check_written(self):
        """Évalue une réponse écrite d'élève (conjugaison, question, phrase
        négative, réponse de compréhension…) et renvoie une rétroaction
        bienveillante. Corps attendu : {code, consigne, reponse, attendu?}."""
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return

        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        consigne = body.get("consigne", "").strip()[:400]
        reponse = body.get("reponse", "").strip()[:600]
        attendu = body.get("attendu", "").strip()[:400]
        if not reponse:
            json_response(self, {"error": "Réponse vide"}, 400)
            return

        system_prompt = (
            "Tu es un enseignant de francisation (FLS) au Québec, niveau 4 "
            "(débutant-intermédiaire). Tu évalues UNE réponse écrite d'un élève "
            "adulte immigrant. Sois bienveillant, encourageant et bref. "
            "Vérifie si la réponse respecte la consigne ET si le français est "
            "correct (orthographe, conjugaison, accords, syntaxe). "
            "Accepte les réponses courtes ou différentes si elles sont correctes "
            "et pertinentes. Ne pénalise pas les majuscules ni la ponctuation "
            "finale manquantes.\n"
            "Réponds UNIQUEMENT par un objet JSON strict, sans texte autour :\n"
            '{\"correct\": true|false, \"feedback\": \"une phrase courte, en '
            'tutoyant l\'élève, qui explique ce qui va ou ce qui cloche\", '
            '\"correction\": \"la réponse corrigée si besoin, sinon la même '
            'réponse\"}'
        )
        user_content = (
            f"Consigne de l'exercice : « {consigne} »\n"
            + (f"Réponse attendue (indice) : « {attendu} »\n" if attendu else "")
            + f"Réponse de l'élève : « {reponse} »"
        )

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=250)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return
        json_response(self, {
            "correct": bool(parsed.get("correct", False)),
            "feedback": parsed.get("feedback", ""),
            "correction": parsed.get("correction", ""),
        })

    def _handle_analyser_erreurs(self):
        """Analyse le PATRON derrière les erreurs d'un élève sur un exercice
        complet, plutôt qu'une réponse isolée. Le module connaît déjà les bonnes
        réponses : l'IA n'évalue rien, elle explique seulement ce qui se répète.
        Corps attendu : {code, exercice, notion, items:[{enonce, choix, bonne}]}."""
        length = int(self.headers.get("Content-Length", 0))
        try:
            body = json.loads(self.rfile.read(length)) if length else {}
        except json.JSONDecodeError:
            json_response(self, {"error": "Requête invalide"}, 400)
            return

        code = body.get("code", "").strip().upper()
        if not validate_student_code(code):
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        exercice = body.get("exercice", "").strip()[:200]
        notion = body.get("notion", "").strip()[:200]
        items = body.get("items", [])
        if not isinstance(items, list) or not items:
            json_response(self, {"error": "Aucune réponse à analyser"}, 400)
            return

        # Plafond dur : un exercice du module compte au plus une douzaine de
        # lignes. Au-delà, c'est un appel malformé, pas un élève en difficulté.
        lignes = []
        for it in items[:15]:
            if not isinstance(it, dict):
                continue
            lignes.append("- « {} » → l'élève a répondu « {} », la bonne réponse était « {} »{}".format(
                str(it.get("enonce", ""))[:200],
                str(it.get("choix", ""))[:100],
                str(it.get("bonne", ""))[:100],
                "" if str(it.get("choix", "")) != str(it.get("bonne", "")) else "  (réussi)",
            ))
        if not lignes:
            json_response(self, {"error": "Aucune réponse à analyser"}, 400)
            return

        system_prompt = (
            "Tu es un enseignant de francisation (FLS) au Québec, niveau 4 "
            "(débutant-intermédiaire). On te donne TOUTES les réponses d'un élève "
            "adulte immigrant à un exercice, avec les bonnes réponses. "
            "Les bonnes réponses sont déjà connues et déjà affichées à l'élève : "
            "ne les répète pas et ne recorrige rien. "
            "Ton seul travail est de trouver le POINT COMMUN entre les erreurs — "
            "la règle mal comprise, le critère mal appliqué, la confusion de sens "
            "ou de son — et de l'expliquer simplement.\n"
            "Tutoie l'élève. Sois bref, concret et encourageant, jamais moralisateur. "
            "Utilise un français simple, des phrases courtes. Aucun jargon "
            "grammatical non expliqué. Aucun émoji.\n"
            "Si les erreurs semblent dispersées, sans point commun, dis-le "
            "honnêtement dans patron plutôt que d'inventer une règle.\n"
            "Réponds UNIQUEMENT par un objet JSON strict, sans texte autour :\n"
            '{"patron": "ce qui revient dans les erreurs, une phrase", '
            '"explication": "deux ou trois phrases qui expliquent la règle ou le '
            'critère en cause, avec un exemple tiré de l\'exercice", '
            '"conseil": "une seule action concrète à faire la prochaine fois"}'
        )
        user_content = (
            f"Exercice : « {exercice} »\n"
            + (f"Notion travaillée : {notion}\n" if notion else "")
            + "Réponses de l'élève :\n" + "\n".join(lignes)
        )

        parsed, err = self._call_anthropic_json(system_prompt, user_content, max_tokens=500)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return
        json_response(self, {
            "patron": parsed.get("patron", ""),
            "explication": parsed.get("explication", ""),
            "conseil": parsed.get("conseil", ""),
        })

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

    def _handle_analyze_grammar(self):
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
        if len(text) > 800:
            text = text[:800]

        system_prompt = (
            "Tu es un professeur de grammaire française pour des élèves adultes "
            "de Niveau 4 en francisation au Québec (niveau intermédiaire). "
            "L'élève te donne une ou plusieurs phrases en français. Découpe le "
            "texte en phrases, puis pour chaque phrase, découpe-la en groupes "
            "syntaxiques (pas mot par mot, mais par groupe : groupe sujet, "
            "groupe verbal, compléments, etc.) et identifie pour chaque groupe "
            "sa fonction ET sa nature dominante. Réponds UNIQUEMENT avec un "
            "objet JSON valide, sans texte avant ni après, exactement dans ce "
            'format : {"phrases": [{"texte": "...", "groupes": [{"mots": "...", '
            '"fonction": "...", "nature": "..."}]}]} — '
            '"mots" est le groupe de mots exact tiré de la phrase (les groupes '
            "mis bout à bout, séparés par des espaces, doivent reconstituer "
            'exactement la phrase originale, ponctuation incluse). "fonction" '
            "est une des valeurs suivantes : \"Sujet\", \"Verbe\", \"Complément "
            "direct\", \"Complément indirect\", \"Complément de phrase\", "
            "\"Attribut du sujet\", \"Autre\". \"nature\" est une des valeurs "
            "suivantes : \"Groupe nominal\", \"Groupe verbal\", \"Groupe "
            "adjectival\", \"Groupe adverbial\", \"Groupe prépositionnel\", "
            "\"Pronom\", \"Autre\". Ne saute aucun mot de la phrase originale."
        )

        parsed, err = self._call_anthropic_json(system_prompt, text, max_tokens=1400)
        if err:
            json_response(self, {"error": err[0]}, err[1])
            return

        json_response(self, {
            "original": text,
            "phrases": parsed.get("phrases", []),
        })

    # ── Cabine d'enregistrement (production orale) ───────────────────────────

    def _handle_oral_submit(self):
        form = self._parse_multipart()
        if form is None:
            json_response(self, {"error": "multipart requis"}, 400)
            return

        def field(name, default=""):
            if name in form:
                val = form[name]
                if not getattr(val, "filename", None):
                    return (val.value or "").strip()
            return default

        code = field("code").upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        if "audio" not in form or not form["audio"].filename:
            json_response(self, {"error": "Aucun enregistrement fourni"}, 400)
            return

        audio_item = form["audio"]
        audio_bytes = audio_item.file.read()
        if not audio_bytes:
            json_response(self, {"error": "Enregistrement vide"}, 400)
            return
        if len(audio_bytes) > 8 * 1024 * 1024:  # garde-fou : 8 Mo max
            json_response(self, {"error": "Enregistrement trop volumineux"}, 400)
            return

        mime = (audio_item.type or "audio/webm").split(";")[0]
        ext = {
            "audio/webm": "webm", "audio/ogg": "ogg", "audio/mp4": "m4a",
            "audio/mpeg": "mp3", "audio/wav": "wav",
        }.get(mime, "webm")

        sub_id = uuid.uuid4().hex
        ORAL_AUDIO_DIR.mkdir(parents=True, exist_ok=True)
        audio_name = f"{sub_id}.{ext}"
        (ORAL_AUDIO_DIR / audio_name).write_bytes(audio_bytes)

        record = {
            "id": sub_id,
            "studentId": student["id"],
            "studentCode": code,
            "groupId": student.get("groupId"),
            "prenom": student.get("prenom", ""),
            "theme": field("theme"),
            "taskId": field("taskId"),
            "taskLabel": field("taskLabel"),
            "question": field("question")[:400],
            "transcription": field("transcription")[:2000],
            "feedback": field("feedback")[:2000],
            "audioUrl": f"/assets/oral-submissions/{audio_name}",
            "createdAt": datetime.now().isoformat(timespec="seconds"),
        }
        subs = load_oral_submissions()
        subs.append(record)
        save_oral_submissions(subs)

        json_response(self, {"success": True, "id": sub_id})

    def _handle_oral_submissions_list(self, params):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
        subs = sorted(
            (s for s in load_oral_submissions()
             if s.get("groupId") == group_id or s.get("studentId") in student_ids),
            key=lambda s: s.get("createdAt", ""), reverse=True)
        json_response(self, subs)

    def _handle_oral_submission_delete(self, sub_id):
        if not self._require_teacher():
            return
        subs = load_oral_submissions()
        target = next((s for s in subs if s["id"] == sub_id), None)
        if target is None:
            json_response(self, {"error": "Introuvable"}, 404)
            return
        audio_url = target.get("audioUrl", "")
        if audio_url:
            fp = STORAGE_DIR / audio_url.lstrip("/")
            try:
                if fp.exists():
                    fp.unlink()
            except OSError:
                pass
        subs = [s for s in subs if s["id"] != sub_id]
        save_oral_submissions(subs)
        json_response(self, {"success": True})

    def _handle_add_student(self):
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        group_id = self._require_group(teacher, body.get("groupId"))
        if group_id is None:
            return
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
                "groupId": group_id,
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
                "groupId": student.get("groupId"),
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
        teacher = self._require_teacher()
        if not teacher:
            return
        students = load_students()
        target = next((s for s in students if s["id"] == student_id), None)
        if target is None:
            json_response(self, {"error": "Élève introuvable"}, 404)
            return
        if self._require_group(teacher, target.get("groupId")) is None:
            return
        save_students([s for s in students if s["id"] != student_id])
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
        # Doit suivre init_storage() : la migration lit les activités et les
        # élèves déjà présents dans le volume.
        try:
            migrate_multi_groupes()
        except Exception as e:
            print(f"[WARN] migrate_multi_groupes a échoué : {e}", flush=True)

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
