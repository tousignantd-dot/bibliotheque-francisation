"""
Serveur — Bibliothèque d'activités pédagogiques
Gère les fichiers statiques + les opérations d'administration (ajout, modification, suppression).
"""

import http.server
import hashlib
import importlib
import sys
import hmac
import json
import mimetypes
import os
import shutil
import threading
import cgi
import smtplib
from email.message import EmailMessage
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

try:
    import forge
except ImportError:
    # La forge est un module optionnel du poste de travail. Un import raté ne
    # doit jamais emporter le serveur avec lui : sans ce filet, un fichier
    # oublié dans un commit tue le conteneur à la deuxième ligne et le
    # healthcheck attend cinq minutes dans le vide. Le repli répond ce que
    # `disponible()` répondrait de toute façon en ligne — la forge est absente.
    class _ForgeAbsente:
        COMMANDES = Path(__file__).resolve().parent / "_forge-absente"

        @staticmethod
        def disponible():
            return False, "La forge n'est pas installée sur ce serveur."

        @staticmethod
        def lister():
            return []

        @staticmethod
        def creer(*args, **kwargs):
            raise RuntimeError("La forge n'est pas installée sur ce serveur.")

        @staticmethod
        def lire(*args, **kwargs):
            return None

        @staticmethod
        def annuler(*args, **kwargs):
            return False

    forge = _ForgeAbsente()
    print("[WARN] forge.py absent : la forge d'activités est désactivée", flush=True)

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
# Cache des voix ElevenLabs, facturées au caractère : trente élèves font lire
# la même consigne, on paie une fois. Les MP3 vont sur le disque et non dans un
# JSON comme outils_cache.json — ce fichier-là est réécrit en entier à chaque
# entrée, ce qui est sans conséquence pour du texte et ruineux pour de l'audio.
# Sous data/ et non assets/ : le second est servi tel quel par le serveur de
# fichiers, ce qui rendrait les MP3 téléchargeables sans code élève.
VOIX_CACHE_DIR = STORAGE_DIR / "data" / "voix-cache"
# Plafond du cache : les répliques du jeu de rôle sont uniques, donc écrites
# une fois et jamais relues. Sans borne, elles rempliraient le volume. Au-delà,
# on élague les fichiers les moins récemment servis jusqu'aux 80 % du plafond.
VOIX_CACHE_MAX_OCTETS = int(os.environ.get("VOIX_CACHE_MAX_MO", "300")) * 1024 * 1024
ORAL_SUBMISSIONS_FILE = STORAGE_DIR / "data" / "oral_submissions.json"
ORAL_AUDIO_DIR = STORAGE_DIR / "assets" / "oral-submissions"
# « Corrige-moi ! » : pratique orale libre, sans enregistrement audio ni date
# d'échéance. Un cumul par (élève, thème) — combien de réponses, combien de
# justes du premier coup, quand pour la dernière fois. Fichier distinct de
# oral_submissions.json, qui garde les productions déposées avec leur audio.
CORRIGE_MOI_FILE = STORAGE_DIR / "data" / "corrige_moi.json"
# Productions écrites déposées. Symétrique de oral_submissions.json, sans le
# fichier joint : le texte de l'élève tient dans l'enregistrement. La
# correction, elle, ne passe pas par ici — /api/correct-french répond à l'écran
# de l'élève et n'écrit rien. Ce qui arrive à l'enseignant, c'est ce que
# l'élève lui envoie.
WRITTEN_SUBMISSIONS_FILE = STORAGE_DIR / "data" / "written_submissions.json"
# Ce que l'assistant a répondu quand l'élève a demandé « pourquoi je me suis
# trompé ». L'analyse était calculée puis jetée avec la page ; elle est
# maintenant gardée, parce qu'un patron d'erreur qui revient chez six élèves
# est précisément ce qu'un enseignant ne peut pas voir autrement. Ne contient
# que du travail de module — jamais une correction privée d'oral ou d'écrit,
# qui reste la propriété de l'élève.
ANALYSES_ERREURS_FILE = STORAGE_DIR / "data" / "analyses_erreurs.json"
# Plafond du journal des analyses : le fichier est réécrit en entier à chaque
# ajout. Au-delà, on jette les plus anciennes.
ANALYSES_ERREURS_MAX = 3000
# Le parcours de l'aide après erreurs : proposée, acceptée, analysée, refusée,
# et l'ouverture d'une mini-leçon « En apprendre plus ». Les modules émettaient
# déjà ces cinq signaux ; le serveur les refusait et l'erreur était avalée par
# le .catch() de lmsTrack. Un cumul par (élève, activité, exercice), comme
# corrige_moi.json : ce qui compte est la fréquence, pas l'horodatage.
SIGNAUX_AIDE_FILE = STORAGE_DIR / "data" / "signaux_aide.json"
# Signalements des enseignants : l'outil est en développement, et la personne
# qui trouve le défaut est celle qui l'a sous les yeux. Un seul fichier, écrit
# en entier à chaque ajout — le volume attendu se compte en dizaines.
SIGNALEMENTS_FILE = STORAGE_DIR / "data" / "signalements.json"
SIGNALEMENTS_MAX = 2000
# Les événements que /api/student/progress accepte. Les trois premiers font
# l'avancement dans progress.json ; les cinq suivants font le journal de l'aide.
ALLOWED_EVENTS = {"dialogue_listened", "exercise_completed", "file_opened"}
SIGNAUX_AIDE = {"aide_proposee", "aide_acceptee", "aide_analysee",
                "aide_refusee", "plus_open"}
# Multi-enseignants : chaque enseignant possède un ou plusieurs groupes.
# Le catalogue d'activités reste commun ; ce qui appartient au groupe, c'est la
# planification (dates), les élèves, la progression et les productions orales.
TEACHERS_FILE  = STORAGE_DIR / "data" / "teachers.json"
GROUPS_FILE    = STORAGE_DIR / "data" / "groups.json"
SCHEDULE_FILE  = STORAGE_DIR / "data" / "schedule.json"
SESSIONS_FILE  = STORAGE_DIR / "data" / "prof_sessions.json"
# Fichiers partagés par l'enseignant à un groupe (notes de cours, grilles,
# corrigés). Ils ne sont pas des activités : ils ont leur propre période de
# parution et l'élève ne les voit que pendant celle-ci.
DOCUMENTS_FILE = STORAGE_DIR / "data" / "documents.json"
GROUP_DOCS_DIR = STORAGE_DIR / "assets" / "documents-groupe"

# Dépôt de matériel. L'inventaire est **produit par le build**
# (`python3 build/materiel.py`) : il décrit ce que le code livre, donc il se
# lit depuis BASE_DIR et jamais depuis le volume, que la prochaine génération
# écraserait de toute façon.
MATERIEL_FILE = BASE_DIR / "data" / "materiel.json"
# Le découpage des modules en sections (« Je découvre · Défi 1 · … »). Produit
# lui aussi par le build (`python3 build/sections.py`), qui le déduit de la
# constante `SECTIONS` de chaque module : même raison que l'inventaire, il
# décrit ce que le code livre et se lit donc depuis BASE_DIR.
SECTIONS_FILE = BASE_DIR / "data" / "sections.json"
# Les fichiers téléversés par les enseignants, eux, sont mutables : ils vivent
# dans le volume, à part de l'inventaire. Les mêler reviendrait à effacer le
# dépôt d'une collègue à chaque build.
DEPOTS_FILE = STORAGE_DIR / "data" / "depots.json"
DEPOTS_DIR = STORAGE_DIR / "assets" / "depots"
# Promotions : quel dépôt tient lieu de fichier officiel. Une décision
# d'administration, pas un fichier — voir `load_promotions()`.
PROMOTIONS_FILE = STORAGE_DIR / "data" / "promotions.json"

SESSION_DAYS = 30

PORT = int(os.environ.get('PORT', 5173))


# ── Initialisation du stockage ──────────────────────────────────────────────

def _meme_contenu(a, b, morceau=1 << 16):
    """Deux fichiers ont-ils le même contenu ? Compare la taille d'abord —
    elle suffit à écarter la quasi-totalité des cas — puis les octets, par
    morceaux : certaines présentations pèsent plusieurs mégaoctets."""
    try:
        if a.stat().st_size != b.stat().st_size:
            return False
        with open(a, "rb") as fa, open(b, "rb") as fb:
            while True:
                ma, mb = fa.read(morceau), fb.read(morceau)
                if ma != mb:
                    return False
                if not ma:
                    return True
    except OSError:
        return False


def _sync_interactive(src, dst):
    """Recopie `assets/interactive/` dans le volume, fichier par fichier.

    Avant, c'était `rmtree` puis `copytree` : tout le magasin était effacé et
    réécrit à chaque démarrage — 200 Mo d'écritures pour quelques fichiers
    changés. Et surtout, la moindre erreur en cours de route (volume plein,
    fichier verrouillé) laissait le magasin **à moitié copié**, sans que rien
    ne le signale : le 20 août 2026, la copie s'est arrêtée juste avant
    `module-vetements`, dernier dossier dans l'ordre alphabétique, et le
    module a répondu 404 en production alors qu'il était bien dans le code.

    Ici, chaque fichier est comparé avant d'être copié (taille et date), les
    erreurs sont comptées et journalisées, et un échec sur un fichier
    n'empêche pas les suivants. Un magasin incomplet reste possible si le
    volume est plein — mais il se voit dans les journaux au lieu de se
    deviner.
    """
    copies = ignores = 0
    echecs = []
    for chemin_src in src.rglob('*'):
        rel = chemin_src.relative_to(src)
        chemin_dst = dst / rel
        try:
            if chemin_src.is_dir():
                chemin_dst.mkdir(parents=True, exist_ok=True)
                continue
            if chemin_dst.exists():
                s, d = chemin_src.stat(), chemin_dst.stat()
                if s.st_size == d.st_size and int(s.st_mtime) <= int(d.st_mtime):
                    ignores += 1
                    continue
            chemin_dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(chemin_src), str(chemin_dst))
            copies += 1
        except OSError as e:
            echecs.append("%s : %s" % (rel, e))

    # Les fichiers que le code ne porte plus : on les retire, sinon un module
    # renommé laisserait sa version d'avant en ligne.
    for chemin_dst in list(dst.rglob('*')):
        if chemin_dst.is_file() and not (src / chemin_dst.relative_to(dst)).exists():
            try:
                chemin_dst.unlink()
            except OSError as e:
                echecs.append("%s (retrait) : %s" % (chemin_dst.relative_to(dst), e))

    print("[init] interactive : %d copié(s), %d inchangé(s), %d échec(s)"
          % (copies, ignores, len(echecs)), flush=True)
    for e in echecs[:20]:
        print("[WARN] interactive " + e, flush=True)
    if len(echecs) > 20:
        print("[WARN] interactive : %d autres échecs" % (len(echecs) - 20), flush=True)


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
        _sync_interactive(src_interactive, dst_interactive)

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
    # Matériel téléversé depuis le catalogue. Le code garde l'autorité quand il
    # porte lui-même un fichier — une fiche régénérée par git doit repartir —,
    # mais un emplacement vide dans le code laisse la place au dépôt du volume.
    # Sans cette nuance, un corrigé ajouté en ligne disparaissait au premier
    # redéploiement, et le catalogue ne servirait plus à rien.
    FICHIER_FIELDS = ("thumbnail", "interactive", "studentDoc", "slideshow",
                      "planCours", "corrige", "autres")
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
                    for field in FICHIER_FIELDS:
                        if vol.get(field) and not entry.get(field):
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
    #
    # Un fichier AJOUTÉ n'est pas le seul cas : un fichier MODIFIÉ doit
    # repartir aussi. La renumérotation des modules (2026-08-16) a régénéré
    # 120 fiches sous le même nom ; ne copier que les absents a laissé la
    # production imprimer « Module 3 » sur des séances devenues le module 4.
    # On compare donc le contenu, et le code gagne quand il diffère.
    #
    # Ça n'écrase pas les téléversements de l'admin : un fichier téléversé
    # n'existe que dans le volume, jamais dans BASE_DIR, donc il n'entre
    # jamais dans cette boucle. Et remplacer un officiel par un dépôt passe
    # par `promotions.json` (voir materiel_promu), pas par le disque.
    for subdir in ("thumbnails", "documents", "slideshows", "plans", "corriges", "autres"):
        src_dir = BASE_DIR / "assets" / subdir
        dst_dir = STORAGE_DIR / "assets" / subdir
        if not src_dir.exists():
            continue
        dst_dir.mkdir(parents=True, exist_ok=True)
        rafraichis = 0
        for f in src_dir.iterdir():
            if not f.is_file():
                continue
            cible = dst_dir / f.name
            try:
                if cible.exists() and _meme_contenu(f, cible):
                    continue
                if cible.exists():
                    rafraichis += 1
                shutil.copy2(str(f), str(cible))
            except OSError as e:
                print(f"[WARN] copie {subdir}/{f.name} échouée : {e}", flush=True)
        if rafraichis:
            print(f"[init] {subdir} : {rafraichis} fichier(s) rafraîchi(s) depuis le code", flush=True)


# ── Helpers données ─────────────────────────────────────────────────────────

CATEGORIES = ("cours", "atelier")


def normalize_categorie(value, interactive_path=""):
    """« cours » = les modules de 4 h du matin ; « atelier » = les activités
    de 2 h de l'après-midi.

    Le dossier prime sur la valeur enregistrée : une activité qui vit dans
    assets/interactive/module-* est un module, point. Sans cette priorité, un
    « atelier » écrit dans le volume — d'avant l'existence du champ, ou d'un
    faux clic dans le catalogue — survit à tous les déploiements, puisque
    `categorie` fait partie des USER_FIELDS de init_storage() : le module
    tombait alors au bas de la liste de planification, parmi les ateliers.
    Ailleurs, la valeur choisie dans le catalogue fait foi comme avant."""
    if "module-" in (interactive_path or ""):
        return "cours"
    if value in CATEGORIES:
        return value
    return "atelier"


# Les huit niveaux du programme de francisation. Le libellé « Niveau N » est
# la forme déjà écrite dans activities.json et lue partout ailleurs
# (js/app.js, js/materiel.js) : on ne change pas de forme en chemin.
NIVEAUX = tuple(f"Niveau {n}" for n in range(1, 9))
NIVEAU_DEFAUT = "Niveau 4"


def normalize_level(value):
    """Le catalogue accueillera des activités de tous les niveaux. Une valeur
    inconnue retombe sur le niveau 4, le cours pour lequel tout a été écrit."""
    value = (value or "").strip()
    return value if value in NIVEAUX else NIVEAU_DEFAUT


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


SCHEDULE_FIELDS = ("dateVue", "datePrevue", "dateFin", "lien")


def _section_id(entry):
    """La section visée par une entrée de planification, '' pour le module.

    Les entrées écrites avant le découpage n'ont pas de clé `sectionId` : elles
    valent pour le module entier, et c'est la chaîne vide qui les désigne."""
    return (entry.get("sectionId") or "").strip()


def schedule_for_group(group_id):
    """{activityId: {dateVue, datePrevue, dateFin, lien}} pour un groupe.

    Les dates du module entier, uniquement — les entrées de section sont
    laissées à `sections_schedule_for_group()`. Tout le portail existant lit
    cette table : y mêler les sections avancerait ou reculerait la date d'une
    activité selon celle de son dernier défi."""
    return {
        e["activityId"]: {key: e.get(key, "") for key in SCHEDULE_FIELDS}
        for e in load_schedule()
        if e.get("groupId") == group_id and not _section_id(e)
    }


def sections_schedule_for_group(group_id):
    """{activityId: {sectionId: {dateVue, datePrevue, dateFin, lien}}}."""
    out = {}
    for e in load_schedule():
        sid = _section_id(e)
        if e.get("groupId") != group_id or not sid:
            continue
        out.setdefault(e["activityId"], {})[sid] = {
            key: e.get(key, "") for key in SCHEDULE_FIELDS
        }
    return out


def set_schedule_dates(group_id, activity_id, fields, section_id=""):
    """Écrit les dates d'une activité pour un groupe. `fields` peut ne contenir
    qu'une partie de dateVue/datePrevue/dateFin/lien.

    Avec un `section_id`, ce sont les dates d'une section du module (« Défi 2 »)
    qui sont posées, sans toucher à celles du module."""
    section_id = (section_id or "").strip()
    entries = load_schedule()
    target = next(
        (e for e in entries
         if e.get("groupId") == group_id and e.get("activityId") == activity_id
         and _section_id(e) == section_id),
        None,
    )
    if target is None:
        target = {"groupId": group_id, "activityId": activity_id}
        if section_id:
            target["sectionId"] = section_id
        target.update({key: "" for key in SCHEDULE_FIELDS})
        entries.append(target)
    for key in SCHEDULE_FIELDS:
        if key in fields:
            target[key] = fields[key] or ""
    # Une section sans aucune date ne vaut plus rien : la garder ferait grossir
    # le fichier d'entrées vides, et « retirer les dates » doit vraiment
    # ramener la section au régime de son module.
    if section_id and not any(target.get(key) for key in SCHEDULE_FIELDS):
        entries = [e for e in entries if e is not target]
    save_schedule(entries)
    return target


def copy_schedule(source_group_id, target_group_id, decalage=0):
    """Reprend la planification d'un groupe pour un autre, décalée de N jours.

    Les dates déjà posées sur le groupe cible sont remplacées : l'enseignant
    part de la planification du groupe modèle, puis ajuste. La date « vue en
    classe » n'est pas copiée — c'est la trace de cours du groupe source.
    """
    def decale(valeur):
        if not valeur:
            return ""
        try:
            return (date.fromisoformat(valeur) + timedelta(days=decalage)).isoformat()
        except ValueError:
            return ""

    source = schedule_for_group(source_group_id)
    sections_source = sections_schedule_for_group(source_group_id)
    entries = [e for e in load_schedule() if e.get("groupId") != target_group_id]
    copiees = 0
    for activity_id, dates in source.items():
        if not dates.get("datePrevue"):
            continue
        entries.append({
            "groupId": target_group_id,
            "activityId": activity_id,
            "dateVue": "",
            "datePrevue": decale(dates.get("datePrevue")),
            "dateFin": decale(dates.get("dateFin")),
            "lien": dates.get("lien", ""),
        })
        copiees += 1
        # Le découpage suit son module : reprendre la planification d'un groupe
        # sans ses sections rouvrirait d'un coup des défis que le groupe modèle
        # ouvre un par un.
        for section_id, sdates in sections_source.get(activity_id, {}).items():
            if not sdates.get("datePrevue"):
                continue
            entries.append({
                "groupId": target_group_id,
                "activityId": activity_id,
                "sectionId": section_id,
                "dateVue": "",
                "datePrevue": decale(sdates.get("datePrevue")),
                "dateFin": decale(sdates.get("dateFin")),
                "lien": sdates.get("lien", ""),
            })
    save_schedule(entries)
    return copiees


# ── Fichiers partagés au groupe ─────────────────────────────────────────────

def load_documents():
    """[{id, groupId, nom, fichier, taille, ouverture, fermeture}]."""
    return _load_json_list(DOCUMENTS_FILE)


def save_documents(documents):
    _save_json(DOCUMENTS_FILE, documents)


def documents_for_group(group_id):
    return [d for d in load_documents() if d.get("groupId") == group_id]


def is_published(doc, today_str):
    """Même règle que pour les activités : sans date d'ouverture, rien ne paraît."""
    return is_offered(
        {"datePrevue": doc.get("ouverture", ""), "dateFin": doc.get("fermeture", "")},
        today_str,
    )


def published_documents(group_id):
    today_str = date.today().isoformat()
    return [d for d in documents_for_group(group_id) if is_published(d, today_str)]


# ── Dépôt de matériel ───────────────────────────────────────────────────────
# L'inventaire est en lecture seule (produit par `build/materiel.py`) ; les
# dépôts des enseignants sont en écriture. Les deux ne se touchent jamais.

def load_materiel():
    """L'inventaire produit par le build. Absent tant que le build n'a pas
    tourné : on répond alors un dépôt vide plutôt qu'une erreur, pour que
    l'écran affiche « rien encore » au lieu de casser."""
    try:
        with open(MATERIEL_FILE, encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"genereLe": "", "blocs": {}, "resume": {}, "porteurs": []}


def regenerer_materiel():
    """Réécrit `data/materiel.json` après une publication.

    L'inventaire se déduit du disque et du catalogue (`build/materiel.py`) ;
    publier une activité sans le refaire la laisserait au catalogue et absente
    du dépôt. En ligne, le dossier du code est en lecture seule et la forge
    n'existe pas : l'échec est sans conséquence et se dit dans la réponse.
    """
    try:
        sys.path.insert(0, str(BASE_DIR / "build"))
        import materiel as _materiel
        importlib.reload(_materiel)
        inv = _materiel.inventaire()
        MATERIEL_FILE.write_text(
            json.dumps(inv, ensure_ascii=False, indent=2), encoding="utf-8")
        return {"refait": True, "porteurs": len(inv.get("porteurs", []))}
    except Exception as e:  # noqa: BLE001 — la publication, elle, a réussi
        return {"refait": False, "raison": str(e)}


def load_depots():
    """[{id, activiteId, seanceCode, type, chemin, format, octets, auteur,
    note, deposeLe, origine}]."""
    return _load_json_list(DEPOTS_FILE)


def save_depots(depots):
    _save_json(DEPOTS_FILE, depots)


def load_promotions():
    """[{fichierId, depotId, parId, parNom, leQuand}].

    Une promotion **ne remplace pas le fichier sur le disque** : elle note
    qu'un dépôt tient lieu d'officiel, et la substitution se fait à la
    lecture. Écraser le `.pptx` officiel serait défait au prochain
    `build.py`, qui le régénère depuis `decks/` — la classe se retrouverait
    devant l'ancienne version sans que personne l'ait demandé. Enregistrée,
    la promotion survit aux builds, se défait d'un clic, et le système peut
    dire quand le fichier officiel a changé sous elle."""
    return _load_json_list(PROMOTIONS_FILE)


def save_promotions(promotions):
    _save_json(PROMOTIONS_FILE, promotions)


def mesurer_fichier(chemin_rel, type_):
    """Le nombre de diapositives ou de blocs du fichier réellement servi.

    Sans ça, un fichier promu hériterait des mesures de l'officiel : le
    panneau annoncerait « 17 diapositives » devant une version qui en a
    douze. Même méthode que `build/materiel.py` — un `.pptx` est un zip."""
    reel = chemin_reel(chemin_rel)
    if not reel:
        return {}
    try:
        if type_ == "presentation" and reel.suffix.lower() == ".pptx":
            with zipfile.ZipFile(reel) as z:
                n = sum(1 for x in z.namelist()
                        if re.fullmatch(r"ppt/slides/slide\d+\.xml", x))
            return {"diapositives": n} if n else {}
        if type_ == "fiche" and reel.suffix.lower() in (".html", ".htm"):
            n = reel.read_text(encoding="utf-8").count('class="bloc card"')
            return {"blocs": n} if n else {}
    except Exception:
        return {}
    return {}


def materiel_promu():
    """L'inventaire, avec les fichiers promus substitués.

    Sert autant l'écran que les archives : promouvoir n'aurait aucun sens si
    « Tout prendre » continuait de descendre la version officielle."""
    inv = load_materiel()
    promos = {p["fichierId"]: p for p in load_promotions()}
    if not promos:
        return inv

    depots = {d["id"]: d for d in load_depots()}
    for porteur in inv.get("porteurs", []):
        for seance in porteur.get("seances", []):
            for f in seance.get("fichiers", []):
                promo = promos.get(f.get("id"))
                depot = depots.get(promo["depotId"]) if promo else None
                if not depot:
                    continue
                # Le fichier officiel a-t-il changé depuis la promotion ? Si
                # oui, la substitution cache une production plus récente : on
                # le dit au lieu de la laisser agir en silence.
                perimee = str(f.get("majLe", "")) > str(promo["leQuand"])[:10]
                f["cheminOfficiel"] = f.get("chemin")
                f["chemin"] = depot["chemin"]
                f["octets"] = depot["octets"]
                f["format"] = depot.get("format", f.get("format"))
                # Le dépôt est stocké sous `dep-0001.pptx` pour que deux
                # fichiers du même nom cohabitent, mais c'est son nom d'origine
                # qui doit entrer dans une archive : personne ne veut trouver
                # un identifiant technique dans son dossier de téléchargements.
                f["nomOriginal"] = depot.get("nom") or ""
                f["majLe"] = str(depot.get("deposeLe", ""))[:10] or f.get("majLe")
                f["origine"] = "depot-promu"
                # Les mesures et la vignette décrivaient l'officiel : elles ne
                # valent plus rien pour ce fichier-ci. On remesure ce qu'on
                # peut, et on retire ce qu'on ne peut pas produire.
                for cle in ("diapositives", "blocs", "vignette"):
                    f.pop(cle, None)
                f.update(mesurer_fichier(f["chemin"], f.get("type")))
                f["promotion"] = {**promo, "auteur": depot.get("auteur"),
                                  "note": depot.get("note", ""),
                                  "perimee": perimee}
    return inv


def fichier_du_materiel(file_id):
    """Retrouve un fichier de l'inventaire par son identifiant, avec le
    porteur et la séance auxquels il appartient. Sert de garde : seuls les
    chemins **inscrits à l'inventaire** peuvent être mis dans une archive,
    donc aucun paramètre d'URL ne peut désigner un fichier arbitraire."""
    for porteur in load_materiel().get("porteurs", []):
        for seance in porteur.get("seances", []):
            for f in seance.get("fichiers", []):
                if f.get("id") == file_id:
                    return porteur, seance, f
    return None, None, None


def chemin_reel(rel_path):
    """Le fichier sur le disque, volume d'abord puis code — même règle que
    `_serve_from_storage`. Renvoie None si le chemin sort des assets ou
    n'existe pas."""
    rel_path = (rel_path or "").lstrip("/")
    if not rel_path.startswith("assets/") or ".." in rel_path:
        return None
    for racine in (STORAGE_DIR, BASE_DIR):
        p = racine / rel_path
        if p.exists() and p.is_file():
            return p
    return None


def fichiers_pour_archive(portee, porteur, codes=None, type_voulu=None):
    """Les fichiers à mettre dans une archive, dans l'ordre d'enseignement.

    `portee` : `module` (tout), `presentations`, `fiches`, `seances`.
    `codes` restreint aux séances demandées."""
    voulus = []
    for seance in porteur.get("seances", []):
        if codes and (seance.get("code") or "") not in codes:
            continue
        for f in seance.get("fichiers", []):
            if type_voulu and f.get("type") != type_voulu:
                continue
            reel = chemin_reel(f.get("chemin", ""))
            if reel:
                voulus.append((seance.get("code"), f, reel))
    if portee == "module" and porteur.get("plan"):
        reel = chemin_reel(porteur["plan"].get("chemin", ""))
        if reel:
            voulus.append((None, porteur["plan"], reel))
    return voulus


def nom_archive(porteur, activite, portee, codes):
    """Un nom d'archive doit rester lisible par un humain : pas d'identifiant
    technique, pas d'UUID. C'est le nom que l'enseignant retrouvera dans son
    dossier de téléchargements dans trois semaines."""
    base = porteur.get("slug") or slugify(activite.get("title", "")) or "materiel"
    if codes:
        liste = sorted(codes)
        tete = "-".join(liste[:4])
        suffixe = f"-et-{len(liste) - 4}-autres" if len(liste) > 4 else ""
        # La portée entre dans le nom quand elle restreint le contenu : sans
        # elle, « les présentations de B3-C1 » et « les fiches de B3-C1 »
        # arriveraient sous le même nom dans le dossier de téléchargements.
        genre = f"_{portee}" if portee in ("presentations", "fiches") else ""
        return f"{base}_{tete}{suffixe}{genre}.zip"
    return f"{base}_{portee}.zip"


DOSSIERS_ARCHIVE = {"presentation": "presentations", "fiche": "fiches",
                    "plan": "plan-de-cours", "annexe": "annexes"}


def construire_archive(fichiers, slug=None):
    """Fabrique le zip en mémoire. Rien n'est écrit sur disque : une archive
    pré-construite serait périmée au prochain build, et les 16 présentations
    d'un module se compressent en une fraction de seconde.

    Deux soins pour que l'archive s'ouvre bien dans le Finder : le nom du
    module est retiré de chaque fichier (il est déjà dans le nom de
    l'archive), et les types sont rangés en dossiers dès qu'il y en a
    plusieurs — sans quoi seize présentations et seize fiches arrivent en
    vrac dans la même liste alphabétique."""
    types = {f.get("type") for _, f, _ in fichiers}
    ranger = len(types) > 1

    tampon = io.BytesIO()
    with zipfile.ZipFile(tampon, "w", zipfile.ZIP_DEFLATED) as z:
        for code, f, reel in fichiers:
            interne = f.get("nomOriginal") or reel.name
            if slug and interne.lower().startswith(slug.lower() + "-"):
                interne = interne[len(slug) + 1:]
            if code and not interne.upper().startswith(code.upper()):
                interne = f"{code}-{interne}"
            if ranger:
                interne = f"{DOSSIERS_ARCHIVE.get(f.get('type'), 'autres')}/{interne}"
            z.write(reel, interne)
    return tampon.getvalue()


def activities_for_group(group_id):
    """Le catalogue commun, avec les dates du groupe superposées."""
    sched = schedule_for_group(group_id)
    result = []
    for a in load_activities():
        entry = dict(a)
        dates = sched.get(a["id"], {})
        for key in SCHEDULE_FIELDS:
            entry[key] = dates.get(key, "")
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


def load_sections_catalogue():
    """{activiteId (int): [{id, titre, chapeau}]} — le découpage des modules.

    Produit par `build/sections.py`. Absent tant que le build n'a pas tourné :
    on répond alors un découpage vide, et tout se comporte comme avant, c'est-
    à-dire un module planifié d'un seul bloc."""
    try:
        with open(SECTIONS_FILE, encoding="utf-8") as f:
            brut = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    return {int(k): v for k, v in brut.items()}


def sections_of_activity(activity_id):
    return load_sections_catalogue().get(activity_id, [])


def is_section_offered(module_dates, section_dates, today_str):
    """Une section n'est ouverte que si son module l'est.

    Sans date propre, la section suit son module — c'est ce qui laisse les
    modules déjà planifiés s'ouvrir en entier comme avant. Avec une date, elle
    s'ouvre à son tour : le module devient une coquille qui se remplit."""
    if not is_offered(module_dates, today_str):
        return False
    dp = section_dates.get("datePrevue", "")
    df = section_dates.get("dateFin", "")
    if not dp:
        return True
    if df and df < today_str:
        return False
    return dp <= today_str


def sections_state_for_student(group_id, activity_id, today_str=None):
    """[{id, titre, chapeau, datePrevue, dateFin, ouverte}] pour un élève.

    Liste vide si le module n'a pas de découpage : le module ouvre alors tout,
    ce qui est exactement son comportement d'avant."""
    today_str = today_str or date.today().isoformat()
    sections = sections_of_activity(activity_id)
    if not sections:
        return []
    module_dates = schedule_for_group(group_id).get(activity_id, {})
    planif = sections_schedule_for_group(group_id).get(activity_id, {})
    out = []
    for s in sections:
        dates = planif.get(s["id"], {})
        out.append({
            "id": s["id"],
            "titre": s.get("titre", ""),
            "chapeau": s.get("chapeau", ""),
            "datePrevue": dates.get("datePrevue", ""),
            "dateFin": dates.get("dateFin", ""),
            "ouverte": is_section_offered(module_dates, dates, today_str),
        })
    return out


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


def founder_id(teachers=None):
    """L'identifiant du compte fondateur.

    Le fondateur est le compte du premier démarrage — celui que crée
    `/api/prof/setup` ou l'amorce par variables d'environnement. Les deux
    chemins lui donnent l'`id` 1 ; on prend malgré tout le plus petit `id`
    présent, pour ne pas dépendre d'un nombre écrit en dur.

    `PROF_FONDATEUR` (un courriel) permet de désigner un autre compte sans
    toucher au code — utile si le compte du premier démarrage n'est pas celui
    de la personne qui tient l'installation.
    """
    teachers = load_teachers() if teachers is None else teachers
    if not teachers:
        return None
    voulu = normalize_email(os.environ.get("PROF_FONDATEUR", ""))
    if voulu:
        for t in teachers:
            if normalize_email(t.get("courriel")) == voulu:
                return t["id"]
    return min(t["id"] for t in teachers)


def is_founder(teacher, teachers=None):
    """Seul le fondateur ouvre des comptes « administrateur ».

    Un administrateur ordinaire gère les enseignants et leurs groupes ; il ne
    fabrique pas ses pairs, et ne peut pas non plus s'emparer du compte
    fondateur en lui réinitialisant son mot de passe.
    """
    return bool(teacher) and teacher.get("id") == founder_id(teachers)


def public_teacher(teacher, teachers=None):
    """Vue d'un enseignant sans son empreinte de mot de passe."""
    return {
        "id": teacher["id"],
        "nom": teacher.get("nom", ""),
        "courriel": teacher.get("courriel", ""),
        "role": teacher.get("role", "prof"),
        "createdAt": teacher.get("createdAt", ""),
        "fondateur": is_founder(teacher, teachers),
    }


def normalize_email(value):
    return (value or "").strip().lower()


def normalize_lien(value):
    """Un lien de rencontre est une URL http(s) ou rien. Refuser le reste évite
    qu'un « javascript: » se retrouve dans le portail des élèves."""
    lien = (value or "").strip()
    if not lien:
        return ""
    return lien[:500] if lien.lower().startswith(("http://", "https://")) else ""


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
# Sérialise le seul moment où deux requêtes se marcheraient dessus : l'élagage.
# Lire et écrire un MP3 ne se verrouille pas — chaque fichier a son propre nom.
_VOIX_CACHE_LOCK = threading.Lock()


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


def voix_cache_chemin(voix, texte):
    """Fichier où dort le MP3 d'un texte dit par une voix. La voix entre dans
    la clé : la même réplique lue par la propriétaire et par le visiteur sont
    deux enregistrements. Espaces normalisés, comme pour outils_key()."""
    empreinte = hashlib.sha1(" ".join(texte.split()).encode("utf-8")).hexdigest()[:20]
    return VOIX_CACHE_DIR / ("%s-%s.mp3" % (voix, empreinte))


def voix_cache_lire(chemin):
    """Rend les octets du MP3, ou None. Touche le fichier au passage : c'est la
    date de dernier service qui décide de ce que l'élagage garde."""
    try:
        audio = chemin.read_bytes()
    except OSError:
        return None
    if not audio:
        return None
    try:
        os.utime(chemin, None)
    except OSError:
        pass          # cache en lecture seule : on sert quand même
    return audio


def voix_cache_ecrire(chemin, audio):
    """Range un MP3. Écriture par fichier temporaire puis renommage : un élève
    qui recharge pendant l'écriture ne doit jamais lire un MP3 tronqué."""
    try:
        VOIX_CACHE_DIR.mkdir(parents=True, exist_ok=True)
        provisoire = chemin.with_suffix(".mp3.part-%s" % uuid.uuid4().hex[:8])
        provisoire.write_bytes(audio)
        provisoire.replace(chemin)
    except OSError as e:
        print(f"[WARN] cache voix non écrit : {e}", flush=True)
        return
    _voix_cache_elaguer()


def _voix_cache_elaguer():
    """Ramène le cache sous son plafond en retirant les fichiers les moins
    récemment servis. Le cache n'est jamais une source de vérité : tout ce
    qu'on jette sera régénéré au prochain appel."""
    with _VOIX_CACHE_LOCK:
        try:
            fichiers = [(f.stat().st_mtime, f.stat().st_size, f)
                        for f in VOIX_CACHE_DIR.glob("*.mp3")]
        except OSError:
            return
        total = sum(taille for _, taille, _ in fichiers)
        if total <= VOIX_CACHE_MAX_OCTETS:
            return
        cible = int(VOIX_CACHE_MAX_OCTETS * 0.8)
        for _, taille, f in sorted(fichiers):
            if total <= cible:
                break
            try:
                f.unlink()
                total -= taille
            except OSError:
                pass
        print(f"[voix] cache élagué à {total / (1024 * 1024):.1f} Mo", flush=True)


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


def load_corrige_moi():
    if CORRIGE_MOI_FILE.exists():
        with open(CORRIGE_MOI_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_corrige_moi(data):
    CORRIGE_MOI_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CORRIGE_MOI_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_written_submissions():
    if WRITTEN_SUBMISSIONS_FILE.exists():
        with open(WRITTEN_SUBMISSIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_written_submissions(data):
    WRITTEN_SUBMISSIONS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(WRITTEN_SUBMISSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_analyses_erreurs():
    if ANALYSES_ERREURS_FILE.exists():
        with open(ANALYSES_ERREURS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_analyses_erreurs(data):
    ANALYSES_ERREURS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(ANALYSES_ERREURS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_signaux_aide():
    if SIGNAUX_AIDE_FILE.exists():
        with open(SIGNAUX_AIDE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_signaux_aide(data):
    SIGNAUX_AIDE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNAUX_AIDE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ── Signalements (« J'ai vu un problème ») ───────────────────────────────────
# L'outil est en développement et les enseignantes sont les seules à voir ses
# défauts en situation. Trois temps, dans cet ordre : on écrit le signalement
# (rien ne doit pouvoir le perdre), on demande à l'IA un premier tri, on envoie
# le courriel. Les deux derniers se font dans un fil séparé : l'enseignante a
# déjà sa confirmation, elle n'attend ni l'API ni le serveur de courriel.

def load_signalements():
    if SIGNALEMENTS_FILE.exists():
        with open(SIGNALEMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_signalements(data):
    SIGNALEMENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SIGNALEMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def maj_signalement(sid, champs):
    """Relit, modifie une fiche, réécrit. Le fil de fond est seul à écrire
    après coup, mais l'enseignante peut en envoyer un deuxième entre-temps :
    on ne réécrit jamais à partir d'une liste gardée en mémoire."""
    with _VERROU_SIGNALEMENTS:
        entries = load_signalements()
        for e in entries:
            if e.get("id") == sid:
                e.update(champs)
                break
        save_signalements(entries)


_VERROU_SIGNALEMENTS = threading.Lock()


def _envoyer_par_resend(sujet, corps, destinataire):
    """Envoie par l'API HTTPS de Resend. Renvoie (ok, raison), où ok vaut
    None si Resend n'est pas configuré — auquel cas l'appelant essaie le SMTP.
    La raison est écrite pour être lue par l'administrateur à l'écran : c'est
    elle qui a fait gagner les heures de dépannage que les journaux de
    l'hébergeur coûtaient.

    Pourquoi une API plutôt que SMTP : Gmail refuse les mots de passe
    d'application aux comptes scolaires et à ceux qui n'ont pas la double
    validation, et un hébergeur bloque volontiers le port 465 sortant. Une
    requête HTTPS ne rencontre ni l'un ni l'autre.
    """
    api_key = os.environ.get("RESEND_API_KEY", "").strip()
    if not api_key:
        return None, "RESEND_API_KEY absente"
    # Sans domaine vérifié chez Resend, seule l'adresse de bac à sable est
    # acceptée — elle n'écrit qu'au propriétaire du compte, ce qui est
    # exactement l'usage ici.
    expediteur = (os.environ.get("RESEND_EXPEDITEUR", "").strip()
                  or "Signalements <onboarding@resend.dev>")
    payload = json.dumps({
        "from": expediteur,
        "to": [destinataire],
        "subject": sujet,
        "text": corps,
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            # Sans cet en-tête, urllib s'annonce « Python-urllib/3.x » et le
            # pare-feu devant l'API répond 403 « error code: 1010 » — un
            # refus de Cloudflare, pas de Resend : la requête n'arrive même
            # pas jusqu'à eux, et la clé n'y est pour rien. Symptôme
            # trompeur, à ne pas réintroduire en nettoyant les en-têtes.
            "User-Agent": "bibliotheque-francisation/1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            resp.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")[:300]
        print(f"[signalement] Resend a refusé ({e.code}) : {detail}", flush=True)
        return False, f"Resend a refusé ({e.code}) : {detail}"
    except Exception as e:                      # noqa: BLE001 — jamais fatal
        print(f"[signalement] Resend injoignable : {e}", flush=True)
        return False, f"Resend injoignable : {e}"
    print(f"[signalement] note envoyée à {destinataire} par Resend", flush=True)
    return True, f"Envoyée à {destinataire} par Resend"


def envoyer_courriel(sujet, corps):
    """Envoie une note au responsable du projet. Deux chemins, essayés dans
    cet ordre : l'API Resend, puis un serveur SMTP. Sans configuration ni de
    l'un ni de l'autre, ne fait rien et le dit dans le journal — le
    signalement reste enregistré.

    Resend : RESEND_API_KEY, RESEND_EXPEDITEUR (à défaut, l'adresse de bac à
    sable, qui n'écrit qu'au propriétaire du compte Resend).
    SMTP : SMTP_HOTE, SMTP_PORT (465 par défaut, SSL ; 587 bascule en
    STARTTLS), SMTP_USER, SMTP_MOTDEPASSE. Avec Gmail, SMTP_MOTDEPASSE est un
    « mot de passe d'application », jamais le mot de passe du compte.
    Destination, dans les deux cas : SIGNALEMENT_DESTINATAIRE.

    Renvoie (ok, raison). La raison ne porte jamais de clé ni de mot de
    passe : elle nomme la variable manquante, ou répète ce que le service a
    répondu.
    """
    destinataire = (os.environ.get("SIGNALEMENT_DESTINATAIRE", "").strip()
                    or os.environ.get("SMTP_USER", "").strip())
    if not destinataire:
        raison = ("aucune adresse de destination : posez "
                  "SIGNALEMENT_DESTINATAIRE")
        print(f"[signalement] {raison}", flush=True)
        return False, raison

    ok, raison = _envoyer_par_resend(sujet, corps, destinataire)
    if ok is not None:
        return ok, raison

    hote = os.environ.get("SMTP_HOTE", "").strip()
    user = os.environ.get("SMTP_USER", "").strip()
    motdepasse = os.environ.get("SMTP_MOTDEPASSE", "")
    if not (hote and user and motdepasse):
        raison = ("aucun envoi configuré : ni RESEND_API_KEY, ni le trio "
                  "SMTP_HOTE / SMTP_USER / SMTP_MOTDEPASSE")
        print(f"[signalement] {raison}", flush=True)
        return False, raison

    message = EmailMessage()
    message["Subject"] = sujet
    message["From"] = user
    message["To"] = destinataire
    message.set_content(corps)

    port = int(os.environ.get("SMTP_PORT", "465"))
    try:
        if port == 587:
            with smtplib.SMTP(hote, port, timeout=20) as serveur:
                serveur.starttls()
                serveur.login(user, motdepasse)
                serveur.send_message(message)
        else:
            with smtplib.SMTP_SSL(hote, port, timeout=20) as serveur:
                serveur.login(user, motdepasse)
                serveur.send_message(message)
    except Exception as e:                      # noqa: BLE001 — jamais fatal
        print(f"[signalement] envoi du courriel impossible : {e}", flush=True)
        return False, f"SMTP : {e}"
    print(f"[signalement] note envoyée à {destinataire} par SMTP", flush=True)
    return True, f"Envoyée à {destinataire} par SMTP"


def _prompt_triage(entry):
    return (
        "Un enseignant de francisation vient de signaler un problème dans le "
        "portail enseignant (outil maison, en développement). Fais un premier "
        "tri, en français, en trois lignes exactement et rien d'autre :\n"
        "Gravité : bloquant | gênant | cosmétique | demande d'amélioration\n"
        "Nature : ce qui semble en cause (interface, données, contenu "
        "pédagogique, performance, malentendu d'usage…), en une phrase.\n"
        "À corriger : oui / non / à voir — suivi d'une phrase qui dit "
        "pourquoi, et où regarder si tu peux le deviner.\n\n"
        f"Écran : {entry.get('ecran') or '(non précisé)'}\n"
        f"Adresse : {entry.get('url') or '(inconnue)'}\n"
        f"Description : {entry.get('description', '')}"
    )


def triage_signalement(entry):
    """Premier tri par l'IA. Renvoie le texte, ou None si l'appel échoue."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return None
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 400,
        "messages": [{"role": "user", "content": _prompt_triage(entry)}],
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
    except Exception as e:                      # noqa: BLE001 — jamais fatal
        print(f"[signalement] triage impossible : {e}", flush=True)
        return None
    texte = " ".join(
        b.get("text", "") for b in result.get("content", [])
        if b.get("type") == "text"
    ).strip()
    return texte or None


def traiter_signalement(entry):
    """Fil de fond : trier, garder l'analyse, puis prévenir par courriel.

    Tout est rattrapé et écrit dans la fiche. Un fil de fond qui meurt ne
    laisse aucune trace visible : l'enseignante a eu son bandeau vert, et le
    courriel n'arrive jamais sans que rien ne dise pourquoi. Le redémarrage
    du conteneur pendant un déploiement suffit à provoquer ce silence.
    """
    try:
        _traiter_signalement(entry)
    except Exception as e:                      # noqa: BLE001 — jamais fatal
        print(f"[signalement] traitement interrompu : {e}", flush=True)
        maj_signalement(entry["id"],
                        {"courrielRaison": f"traitement interrompu : {e}"})


def _traiter_signalement(entry):
    analyse = triage_signalement(entry)
    if analyse:
        entry["analyse"] = analyse
        maj_signalement(entry["id"], {"analyse": analyse})

    corps = (
        f"Signalement de {entry.get('enseignantNom') or 'un enseignant'}"
        f" ({entry.get('enseignantCourriel') or 'courriel inconnu'})\n"
        f"Reçu le {entry.get('timestamp', '')}\n"
        f"Écran : {entry.get('ecran') or '(non précisé)'}\n"
        f"Adresse : {entry.get('url') or '(inconnue)'}\n"
        f"Navigateur : {entry.get('agent') or '(inconnu)'}\n"
        f"\n--- Ce qui est décrit ---\n{entry.get('description', '')}\n"
        f"\n--- Premier tri par l'IA ---\n"
        f"{analyse or '(indisponible : clé API absente ou appel échoué)'}\n"
        f"\nFiche complète : data/signalements.json (identifiant {entry.get('id')})\n"
    )
    envoie, raison = envoyer_courriel(
        f"[Francisation] Signalement — {(entry.get('ecran') or 'portail enseignant')}",
        corps,
    )
    maj_signalement(entry["id"], {"courrielEnvoye": bool(envoie),
                                  "courrielRaison": raison})


# Boîtes de répétition espacée (système Leitner) : plus la boîte est haute,
# plus l'intervalle avant la prochaine révision est grand.
VOCAB_INTERVALS_DAYS = [0, 1, 3, 7, 14, 30, 60]

# Un mot est « maîtrisé » à partir de la boîte 4, soit un intervalle de quinze
# jours : quatre rappels réussis sans rechute. Le seuil est ici et nulle part
# ailleurs — la fiche de l'élève et l'écran des listes doivent compter pareil.
VOCAB_BOITE_MAITRISE = 4

VOCAB_BANK = [
    {"id": "w1", "activityIds": [4, 8, 17],  "mot": "un rendez-vous", "domaine": "Santé", "definition": "Un moment fixé à l'avance pour voir quelqu'un.", "exemple": "J'ai un rendez-vous à dix heures avec le docteur."},
    {"id": "w2", "activityIds": [4, 8, 17, 34, 36],  "mot": "la salle d'attente", "domaine": "Santé", "definition": "L'endroit où on attend avant de voir le médecin.", "exemple": "Prenez un siège dans la salle d'attente."},
    {"id": "w3", "activityIds": [4, 8, 17, 34, 35],  "mot": "la carte d'assurance maladie", "domaine": "Santé", "definition": "Le document qui donne accès aux soins de santé gratuits au Québec.", "exemple": "Avez-vous votre carte d'assurance maladie avec vous ?"},
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
    {"id": "w19", "activityIds": [11, 16, 44], "mot": "le loyer", "domaine": "Logement", "definition": "Le montant payé chaque mois pour habiter un logement.", "exemple": "Le loyer est de 950 $ par mois."},
    {"id": "w20", "activityIds": [11, 16], "mot": "un quatre et demi", "domaine": "Logement", "definition": "Un appartement avec quatre pièces plus la salle de bain.", "exemple": "C'est un beau quatre et demi."},
    {"id": "w21", "activityIds": [11, 16, 44, 45], "mot": "le bail", "domaine": "Logement", "definition": "Le contrat de location d'un logement.", "exemple": "J'ai signé le bail hier."},
    {"id": "w22", "activityIds": [11, 16], "mot": "le chauffage", "domaine": "Logement", "definition": "Le système qui réchauffe un logement.", "exemple": "Le chauffage ne fonctionne plus."},
    {"id": "w23", "activityIds": [11, 16], "mot": "un dépôt", "domaine": "Logement", "definition": "Une somme d'argent versée en garantie.", "exemple": "Le propriétaire demande un dépôt."},
    {"id": "w24", "activityIds": [11, 16], "mot": "déménager", "domaine": "Logement", "definition": "Changer de logement.", "exemple": "Je déménage la semaine prochaine."},
    {"id": "w25", "activityIds": [11, 16], "mot": "les meubles", "domaine": "Logement", "definition": "Les objets comme une table, un lit, une chaise.", "exemple": "On a acheté de nouveaux meubles."},
    {"id": "w26", "activityIds": [12], "mot": "une tâche", "domaine": "Monde du travail", "definition": "Un travail précis à faire.", "exemple": "Voici tes tâches pour aujourd'hui."},
    {"id": "w27", "activityIds": [12, 40], "mot": "un superviseur", "domaine": "Monde du travail", "definition": "La personne qui dirige les employés.", "exemple": "Mon superviseur m'a expliqué mon horaire."},
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

    # Les cartes « Je retiens des mots » des modules. L'identifiant reprend le
    # nom du module plutôt qu'un numéro : la renumérotation des modules ne doit
    # pas casser la progression déjà enregistrée dans vocab_progress.json.
    # ── module-banque (activité 46) ──
    {"id": "banque-01", "activityIds": [46], "mot": "un compte chèque", "domaine": "Consommation", "definition": "Le compte qui sert aux opérations de tous les jours.", "exemple": "Sa paie entre dans son compte chèque."},
    {"id": "banque-02", "activityIds": [46], "mot": "un compte épargne", "domaine": "Consommation", "definition": "Le compte où on laisse de l'argent de côté.", "exemple": "Elle met cent dollars par mois dans son compte épargne."},
    {"id": "banque-03", "activityIds": [46], "mot": "le dépôt direct", "domaine": "Consommation", "definition": "Le versement de la paie directement dans le compte.", "exemple": "Son employeur exige le dépôt direct."},
    {"id": "banque-04", "activityIds": [46], "mot": "un spécimen de chèque", "domaine": "Consommation", "definition": "Un chèque annulé qui montre les numéros du compte.", "exemple": "Elle apporte un spécimen de chèque au bureau."},
    {"id": "banque-05", "activityIds": [46], "mot": "un virement", "domaine": "Consommation", "definition": "De l'argent envoyé d'un compte à un autre.", "exemple": "Elle fait un virement à sa sœur."},
    {"id": "banque-06", "activityIds": [46], "mot": "un retrait", "domaine": "Consommation", "definition": "L'argent qu'on sort de son compte.", "exemple": "Le retrait au guichet est de quarante dollars."},
    {"id": "banque-07", "activityIds": [46], "mot": "le solde", "domaine": "Consommation", "definition": "L'argent qui reste dans le compte.", "exemple": "Vérifie ton solde avant un gros achat."},
    {"id": "banque-08", "activityIds": [46], "mot": "un NIP", "domaine": "Consommation", "definition": "Le code secret de quatre chiffres de la carte.", "exemple": "On ne note jamais son NIP sur un papier."},
    {"id": "banque-09", "activityIds": [46], "mot": "un prélèvement automatique", "domaine": "Consommation", "definition": "Un paiement qui sort du compte à date fixe.", "exemple": "Le loyer part par prélèvement automatique."},
    {"id": "banque-10", "activityIds": [46], "mot": "être à découvert", "domaine": "Consommation", "definition": "Avoir retiré plus d'argent qu'on en avait.", "exemple": "Elle est à découvert depuis vendredi."},
    {"id": "banque-11", "activityIds": [46], "mot": "des frais mensuels", "domaine": "Consommation", "definition": "Le montant payé chaque mois pour le forfait.", "exemple": "Le forfait de base coûte quatre dollars de frais mensuels."},
    {"id": "banque-12", "activityIds": [46], "mot": "un relevé de compte", "domaine": "Consommation", "definition": "La liste des opérations du mois.", "exemple": "Son relevé de compte arrive le premier du mois."},

    # ── module-consultation (activité 35) ──
    {"id": "consultation-01", "activityIds": [35], "mot": "une clinique sans rendez-vous", "domaine": "Santé", "definition": "Une clinique où on peut consulter sans avoir réservé.", "exemple": "Il va à la clinique sans rendez-vous du quartier."},
    {"id": "consultation-02", "activityIds": [35], "mot": "le triage", "domaine": "Santé", "definition": "L'étape où une infirmière évalue la gravité des cas.", "exemple": "L'infirmière du triage pose des questions."},
    {"id": "consultation-03", "activityIds": [35], "mot": "enflé", "domaine": "Santé", "definition": "Qui a augmenté de volume à cause d'une blessure.", "exemple": "Son genou est enflé depuis la nuit."},
    {"id": "consultation-04", "activityIds": [35], "mot": "une inflammation", "domaine": "Santé", "definition": "Une réaction du corps qui cause douleur et enflure.", "exemple": "Il a une inflammation du tendon."},
    {"id": "consultation-05", "activityIds": [35], "mot": "un tendon", "domaine": "Santé", "definition": "La partie qui attache un muscle à un os.", "exemple": "Le tendon du genou est irrité."},
    {"id": "consultation-06", "activityIds": [35], "mot": "soulever une charge", "domaine": "Santé", "definition": "Lever un objet lourd.", "exemple": "Il doit éviter de soulever une charge."},
    {"id": "consultation-07", "activityIds": [35], "mot": "la physiothérapie", "domaine": "Santé", "definition": "Des soins avec des exercices pour retrouver ses mouvements.", "exemple": "La docteure le réfère en physiothérapie."},
    {"id": "consultation-08", "activityIds": [35], "mot": "un billet de repos", "domaine": "Santé", "definition": "Un papier du médecin qui autorise à ne pas travailler.", "exemple": "Elle lui donne un billet de repos de quatre jours."},
    {"id": "consultation-09", "activityIds": [34, 35], "mot": "une ordonnance", "domaine": "Santé", "definition": "Le papier du médecin pour obtenir un médicament.", "exemple": "Le pharmacien demande votre ordonnance."},
    {"id": "consultation-10", "activityIds": [35], "mot": "élancer", "domaine": "Santé", "definition": "Faire une douleur vive et répétée.", "exemple": "Ça élance quand il plie la jambe."},
    {"id": "consultation-11", "activityIds": [35], "mot": "un quart de travail", "domaine": "Santé", "definition": "La période de travail d'un employé.", "exemple": "Son quart de travail finit à minuit."},

    # ── module-logement (activité 44) ──
    {"id": "logement-01", "activityIds": [44], "mot": "un locataire", "domaine": "Logement", "definition": "La personne qui loue un logement et qui y habite.", "exemple": "Le locataire paie lui-même l'électricité."},
    {"id": "logement-02", "activityIds": [44], "mot": "un propriétaire", "domaine": "Logement", "definition": "La personne à qui appartient le logement loué.", "exemple": "La propriétaire fournit la peinture."},
    {"id": "logement-03", "activityIds": [44], "mot": "chauffé et éclairé", "domaine": "Logement", "definition": "Se dit d'un logement dont le chauffage et l'électricité sont compris dans le loyer.", "exemple": "Le 3 ½ du rez-de-chaussée est chauffé et éclairé."},
    {"id": "logement-04", "activityIds": [44], "mot": "insonorisé", "domaine": "Logement", "definition": "Protégé contre le bruit de la rue ou des voisins.", "exemple": "La chambre est bien insonorisée : elle donne sur la cour."},
    {"id": "logement-05", "activityIds": [44], "mot": "lumineux", "domaine": "Logement", "definition": "Qui reçoit beaucoup de lumière du jour.", "exemple": "La cuisine est petite, mais très lumineuse."},
    {"id": "logement-06", "activityIds": [44], "mot": "la buanderie", "domaine": "Logement", "definition": "Le local où se trouvent la laveuse et la sécheuse.", "exemple": "La buanderie est au sous-sol de l'immeuble."},
    {"id": "logement-07", "activityIds": [44], "mot": "les électroménagers", "domaine": "Logement", "definition": "Les gros appareils de la maison : réfrigérateur, cuisinière, laveuse…", "exemple": "Dans cette annonce, les électroménagers ne sont pas fournis."},
    {"id": "logement-08", "activityIds": [44], "mot": "emménager", "domaine": "Logement", "definition": "S'installer dans un nouveau logement.", "exemple": "Ibrahim va emménager le 1er septembre."},
    {"id": "logement-09", "activityIds": [44], "mot": "un quartier", "domaine": "Logement", "definition": "Une partie d'une ville, avec ses commerces et ses services.", "exemple": "Le quartier est tranquille après vingt heures."},
    {"id": "logement-10", "activityIds": [44], "mot": "l'état des lieux", "domaine": "Logement", "definition": "La description du logement (neuf, rénové, à réparer) au début du bail.", "exemple": "On fait l'état des lieux avant de signer."},

    # ── module-meteo (activité 42) ──
    {"id": "meteo-01", "activityIds": [42], "mot": "la poudrerie", "domaine": "Vie quotidienne", "definition": "De la neige déjà tombée que le vent soulève.", "exemple": "La poudrerie efface les lignes de la route."},
    {"id": "meteo-02", "activityIds": [42], "mot": "la pluie verglaçante", "domaine": "Vie quotidienne", "definition": "Une pluie qui gèle dès qu'elle touche une surface.", "exemple": "La pluie verglaçante a couvert les échelles de glace."},
    {"id": "meteo-03", "activityIds": [42], "mot": "le grésil", "domaine": "Vie quotidienne", "definition": "De petits grains de glace qui tombent du ciel.", "exemple": "Du grésil frappait les fenêtres de l'atelier."},
    {"id": "meteo-04", "activityIds": [42], "mot": "une rafale", "domaine": "Vie quotidienne", "definition": "Une hausse brusque du vent, qui dure quelques secondes.", "exemple": "Les rafales nous ont fait descendre du toit."},
    {"id": "meteo-05", "activityIds": [42], "mot": "le facteur éolien", "domaine": "Vie quotidienne", "definition": "L'effet du vent, qui fait ressentir un froid plus intense.", "exemple": "Avec le facteur éolien, on ressent moins vingt-huit."},
    {"id": "meteo-06", "activityIds": [42], "mot": "un redoux", "domaine": "Vie quotidienne", "definition": "Un réchauffement court au milieu de l'hiver.", "exemple": "Le redoux de jeudi fera fondre la glace du stationnement."},
    {"id": "meteo-07", "activityIds": [42], "mot": "la chaussée", "domaine": "Vie quotidienne", "definition": "La partie de la route où roulent les véhicules.", "exemple": "La chaussée reste glissante malgré le sel."},
    {"id": "meteo-08", "activityIds": [42], "mot": "la visibilité", "domaine": "Vie quotidienne", "definition": "La distance à laquelle on distingue encore ce qui nous entoure.", "exemple": "La visibilité tombe à deux cents mètres."},
    {"id": "meteo-09", "activityIds": [42], "mot": "un avertissement", "domaine": "Vie quotidienne", "definition": "Un message officiel qui signale un danger à venir.", "exemple": "Un avertissement de poudrerie vise l'autoroute 10."},
    {"id": "meteo-10", "activityIds": [42], "mot": "le mercure", "domaine": "Vie quotidienne", "definition": "Une autre façon de nommer la température.", "exemple": "Le mercure descendra à moins six degrés."},
    {"id": "meteo-11", "activityIds": [42], "mot": "une éclaircie", "domaine": "Vie quotidienne", "definition": "Un moment où les nuages s'ouvrent et laissent passer le soleil.", "exemple": "Une éclaircie est prévue en fin de journée."},
    {"id": "meteo-12", "activityIds": [42], "mot": "un chasse-neige", "domaine": "Vie quotidienne", "definition": "Un camion qui pousse la neige hors de la route.", "exemple": "Les chasse-neige circulent en continu depuis minuit."},

    # ── module-nouvelles (activité 41) ──
    {"id": "nouvelles-01", "activityIds": [41], "mot": "un fait divers", "domaine": "Culture / médias", "definition": "Une nouvelle relative à des faits quotidiens qui attire la curiosité.", "exemple": "Ce fait divers parle d'une fillette qui a retrouvé son chat."},
    {"id": "nouvelles-02", "activityIds": [41], "mot": "une nouvelle régionale", "domaine": "Culture / médias", "definition": "Une nouvelle qui touche une région de la province.", "exemple": "La collecte de mitaines à Longueuil, c'est une nouvelle régionale."},
    {"id": "nouvelles-03", "activityIds": [41], "mot": "une nouvelle nationale", "domaine": "Culture / médias", "definition": "Une nouvelle qui touche la province ou le pays.", "exemple": "Voici une nouvelle nationale importante."},
    {"id": "nouvelles-04", "activityIds": [41], "mot": "une nouvelle internationale", "domaine": "Culture / médias", "definition": "Une nouvelle qui provient de l'extérieur du pays.", "exemple": "C'est une nouvelle internationale."},
    {"id": "nouvelles-05", "activityIds": [41], "mot": "un témoin", "domaine": "Culture / médias", "definition": "Une personne qui a vu un événement.", "exemple": "La voisine a été témoin du retour du chat."},
    {"id": "nouvelles-06", "activityIds": [41], "mot": "un reportage", "domaine": "Culture / médias", "definition": "Un texte ou une émission qui présente une nouvelle en détail.", "exemple": "Le reportage montrait la classe de Noah."},
    {"id": "nouvelles-07", "activityIds": [41], "mot": "un organisme", "domaine": "Culture / médias", "definition": "Un groupe organisé qui offre un service ou mène une cause.", "exemple": "L'organisme Les Cœurs d'hiver a aidé la classe."},
    {"id": "nouvelles-08", "activityIds": [41], "mot": "amasser", "domaine": "Culture / médias", "definition": "Réunir, accumuler peu à peu.", "exemple": "Les élèves ont amassé des mitaines."},
    {"id": "nouvelles-09", "activityIds": [41], "mot": "un franc succès", "domaine": "Culture / médias", "definition": "Une vraie réussite, un grand succès.", "exemple": "Le concours a été un franc succès."},
    {"id": "nouvelles-10", "activityIds": [41], "mot": "un concours", "domaine": "Culture / médias", "definition": "Une compétition organisée pour désigner un gagnant.", "exemple": "Elle a gagné le concours de sculptures sur neige."},
    {"id": "nouvelles-11", "activityIds": [41], "mot": "avertir", "domaine": "Culture / médias", "definition": "Informer quelqu'un d'un danger ou d'une nouvelle importante.", "exemple": "La voisine a averti la famille tout de suite."},
    {"id": "nouvelles-12", "activityIds": [41], "mot": "à ce jour", "domaine": "Culture / médias", "definition": "Jusqu'à maintenant, jusqu'à aujourd'hui.", "exemple": "À ce jour, personne n'a battu ce record."},

    # ── module-probleme (activité 45) ──
    {"id": "probleme-01", "activityIds": [45], "mot": "un calorifère", "domaine": "Logement", "definition": "L'appareil fixé au mur qui chauffe une pièce.", "exemple": "Le calorifère du salon est resté froid toute la nuit."},
    {"id": "probleme-02", "activityIds": [45], "mot": "un disjoncteur", "domaine": "Logement", "definition": "L'interrupteur du panneau électrique qui coupe le courant en cas de danger.", "exemple": "Le disjoncteur retombe chaque fois qu'elle le remonte."},
    {"id": "probleme-03", "activityIds": [45], "mot": "un chauffage d'appoint", "domaine": "Logement", "definition": "Un petit appareil de chauffage qu'on ajoute temporairement.", "exemple": "Elle emprunte un chauffage d'appoint en attendant l'électricien."},
    {"id": "probleme-04", "activityIds": [45], "mot": "une infiltration", "domaine": "Logement", "definition": "De l'eau qui entre par le toit ou par un mur.", "exemple": "La tache au plafond vient d'une infiltration."},
    {"id": "probleme-05", "activityIds": [45], "mot": "la moisissure", "domaine": "Logement", "definition": "Des taches noires ou vertes causées par l'humidité.", "exemple": "Sans ventilation, la moisissure revient toujours."},
    {"id": "probleme-06", "activityIds": [45], "mot": "l'ampleur", "domaine": "Logement", "definition": "La grandeur, l'importance d'un problème.", "exemple": "La photo permet de constater l'ampleur du dégât."},
    {"id": "probleme-07", "activityIds": [45], "mot": "une partie commune", "domaine": "Logement", "definition": "Un espace de l'immeuble partagé par tous les locataires.", "exemple": "Le corridor est une partie commune, pas un rangement."},
    {"id": "probleme-08", "activityIds": [45], "mot": "encombrer", "domaine": "Logement", "definition": "Occuper une place et gêner le passage.", "exemple": "Trois vélos encombrent le corridor du troisième."},
    {"id": "probleme-09", "activityIds": [45], "mot": "une sortie de secours", "domaine": "Logement", "definition": "Le chemin à garder libre pour évacuer en cas d'incendie.", "exemple": "Une sortie de secours doit toujours rester dégagée."},
    {"id": "probleme-10", "activityIds": [45], "mot": "se plaindre", "domaine": "Logement", "definition": "Dire qu'on n'accepte plus une situation et demander qu'elle change.", "exemple": "Les voisins se plaignent depuis un mois."},
    {"id": "probleme-11", "activityIds": [45], "mot": "l'insalubrité", "domaine": "Logement", "definition": "L'état d'un logement malpropre ou dangereux pour la santé.", "exemple": "Des déchets laissés dehors peuvent mener à l'insalubrité."},
    {"id": "probleme-12", "activityIds": [45], "mot": "un avis écrit", "domaine": "Logement", "definition": "Une lettre ou un courriel qui garde une trace d'une demande.", "exemple": "Un avis écrit est plus solide qu'un appel téléphonique."},
    {"id": "probleme-13", "activityIds": [45], "mot": "un recours", "domaine": "Logement", "definition": "Le moyen légal de faire régler un problème qui traîne.", "exemple": "Le dernier recours, c'est le Tribunal administratif du logement."},
    {"id": "probleme-14", "activityIds": [45], "mot": "un couvreur", "domaine": "Logement", "definition": "La personne qui répare les toitures.", "exemple": "La propriétaire fait venir un couvreur pour le toit."},
    {"id": "probleme-15", "activityIds": [45], "mot": "un dégraissant", "domaine": "Logement", "definition": "Un produit fort qui enlève l'huile et la graisse.", "exemple": "L'odeur du dégraissant monte par la cage d'escalier."},

    # ── module-procedure (activité 40) ──
    {"id": "procedure-01", "activityIds": [40], "mot": "une procédure", "domaine": "Monde du travail", "definition": "La façon officielle de faire une demande ou une tâche.", "exemple": "Il y a une procédure à suivre pour un remboursement."},
    {"id": "procedure-02", "activityIds": [40], "mot": "un remboursement", "domaine": "Monde du travail", "definition": "L'argent qu'on redonne à quelqu'un pour une dépense.", "exemple": "Il demande un remboursement pour ses lunettes de sécurité."},
    {"id": "procedure-03", "activityIds": [40], "mot": "une directive", "domaine": "Monde du travail", "definition": "Une instruction précise à suivre.", "exemple": "Lisez bien les directives avant de commencer."},
    {"id": "procedure-04", "activityIds": [40], "mot": "approuver", "domaine": "Monde du travail", "definition": "Donner son accord officiel à une demande.", "exemple": "Le superviseur doit approuver la demande."},
    {"id": "procedure-05", "activityIds": [40], "mot": "un reçu", "domaine": "Monde du travail", "definition": "Le papier qui prouve un achat.", "exemple": "Gardez votre reçu original."},
    {"id": "procedure-06", "activityIds": [40], "mot": "joindre", "domaine": "Monde du travail", "definition": "Ajouter un document à un envoi.", "exemple": "N'oubliez pas de joindre votre reçu."},
    {"id": "procedure-07", "activityIds": [40], "mot": "un onglet", "domaine": "Monde du travail", "definition": "Une section cliquable dans une application ou un site.", "exemple": "Cliquez sur l'onglet Dépenses."},
    {"id": "procedure-08", "activityIds": [40], "mot": "un jour ouvrable", "domaine": "Monde du travail", "definition": "Un jour de la semaine où l'entreprise est ouverte.", "exemple": "Comptez dix jours ouvrables."},
    {"id": "procedure-09", "activityIds": [40], "mot": "un bris d'équipement", "domaine": "Monde du travail", "definition": "Un équipement qui casse ou cesse de fonctionner.", "exemple": "Signalez tout bris d'équipement rapidement."},
    {"id": "procedure-10", "activityIds": [40], "mot": "un véhicule de service", "domaine": "Monde du travail", "definition": "Un véhicule appartenant à l'entreprise, utilisé pour le travail.", "exemple": "Réservez le véhicule de service à l'avance."},
    {"id": "procedure-11", "activityIds": [40], "mot": "un formulaire", "domaine": "Monde du travail", "definition": "Un document à remplir avec des informations précises.", "exemple": "Remplissez le formulaire en ligne."},

    # ── module-pub (activité 43) ──
    {"id": "pub-01", "activityIds": [43], "mot": "un slogan", "domaine": "Culture / médias", "definition": "Une phrase courte et facile à retenir, placée le plus souvent à la fin d'une publicité.", "exemple": "Son slogan tient en cinq mots."},
    {"id": "pub-02", "activityIds": [43], "mot": "l'émetteur", "domaine": "Culture / médias", "definition": "La personne ou l'organisme qui envoie le message publicitaire.", "exemple": "L'émetteur de la capsule est un organisme du quartier."},
    {"id": "pub-03", "activityIds": [43], "mot": "le récepteur", "domaine": "Culture / médias", "definition": "Les gens à qui le message publicitaire est destiné.", "exemple": "Le récepteur visé, ce sont les voisins qui réparent eux-mêmes."},
    {"id": "pub-04", "activityIds": [43], "mot": "le canal", "domaine": "Culture / médias", "definition": "Le moyen choisi pour diffuser le message.", "exemple": "La radio communautaire est le canal de cette annonce."},
    {"id": "pub-05", "activityIds": [43], "mot": "une valeur morale", "domaine": "Culture / médias", "definition": "Ce qu'une personne ou une société considère comme important et bien.", "exemple": "Le partage est la valeur mise en avant."},
    {"id": "pub-06", "activityIds": [43], "mot": "un préfixe", "domaine": "Culture / médias", "definition": "Un élément placé devant un mot pour en changer le sens.", "exemple": "Avec le préfixe « ré- », on obtient « réutiliser »."},
    {"id": "pub-07", "activityIds": [43], "mot": "un suffixe", "domaine": "Culture / médias", "definition": "Un élément placé à la fin d'un mot pour former un nouveau mot.", "exemple": "Le suffixe « -able » donne « réparable »."},
    {"id": "pub-08", "activityIds": [43], "mot": "une capsule", "domaine": "Culture / médias", "definition": "Une très courte annonce diffusée à la radio.", "exemple": "Sa capsule dure trente secondes."},
    {"id": "pub-09", "activityIds": [43], "mot": "une infolettre", "domaine": "Culture / médias", "definition": "Un courriel envoyé régulièrement aux personnes inscrites.", "exemple": "L'atelier est aussi annoncé dans l'infolettre du quartier."},
    {"id": "pub-10", "activityIds": [43], "mot": "un bénévole", "domaine": "Culture / médias", "definition": "Une personne qui donne son temps sans être payée.", "exemple": "Dix bénévoles répareront les objets samedi."},

    # ── module-sante (activité 34) ──
    {"id": "sante-01", "activityIds": [34], "mot": "prendre un rendez-vous", "domaine": "Santé", "definition": "Fixer un moment pour voir un médecin.", "exemple": "Je voudrais prendre un rendez-vous."},
    {"id": "sante-02", "activityIds": [34], "mot": "une clinique", "domaine": "Santé", "definition": "Un endroit où on consulte des médecins.", "exemple": "La clinique ouvre à huit heures."},
    {"id": "sante-03", "activityIds": [34, 36], "mot": "Info-Santé (811)", "domaine": "Santé", "definition": "Un service téléphonique de conseils de santé, jour et nuit.", "exemple": "J'ai appelé Info-Santé pour un conseil."},
    {"id": "sante-04", "activityIds": [34], "mot": "la posologie", "domaine": "Santé", "definition": "La façon de prendre un médicament (combien et quand).", "exemple": "Suivez bien la posologie."},
    {"id": "sante-05", "activityIds": [34], "mot": "un comprimé", "domaine": "Santé", "definition": "Un petit médicament solide à avaler.", "exemple": "Prenez un comprimé le matin."},
    {"id": "sante-06", "activityIds": [34], "mot": "le traitement", "domaine": "Santé", "definition": "L'ensemble des soins pour guérir.", "exemple": "Le traitement dure sept jours."},
    {"id": "sante-07", "activityIds": [34], "mot": "se sentir", "domaine": "Santé", "definition": "Percevoir son état physique ou moral.", "exemple": "Je me sens mieux aujourd'hui."},
    {"id": "sante-08", "activityIds": [34], "mot": "un pharmacien", "domaine": "Santé", "definition": "La personne qui prépare et vend les médicaments.", "exemple": "Le pharmacien explique la posologie."},
    {"id": "sante-09", "activityIds": [34], "mot": "une urgence", "domaine": "Santé", "definition": "Une situation grave qui demande des soins immédiats.", "exemple": "En cas d'urgence, appelez le 911."},

    # ── module-travail (activité 39) ──
    {"id": "travail-01", "activityIds": [39], "mot": "un retard", "domaine": "Monde du travail", "definition": "Le fait d'arriver après un moment fixé.", "exemple": "J'aurai un retard ce matin."},
    {"id": "travail-02", "activityIds": [39], "mot": "une absence", "domaine": "Monde du travail", "definition": "Le fait de ne pas se trouver à un endroit où on est attendu.", "exemple": "Je vous écris pour justifier mon absence."},
    {"id": "travail-03", "activityIds": [39], "mot": "un abandon", "domaine": "Monde du travail", "definition": "Le fait de renoncer à une chose (un cours, un travail).", "exemple": "Il a dû faire un abandon de son cours."},
    {"id": "travail-04", "activityIds": [39], "mot": "une boîte vocale", "domaine": "Monde du travail", "definition": "Le système qui enregistre un message quand personne ne répond.", "exemple": "J'ai laissé un message dans sa boîte vocale."},
    {"id": "travail-05", "activityIds": [39], "mot": "remplacer", "domaine": "Monde du travail", "definition": "Prendre la place de quelqu'un.", "exemple": "Je dois remplacer ma collègue malade."},
    {"id": "travail-06", "activityIds": [39], "mot": "un dégât d'eau", "domaine": "Monde du travail", "definition": "Un dommage causé par de l'eau dans un logement.", "exemple": "J'ai un dégât d'eau dans mon appartement."},
    {"id": "travail-07", "activityIds": [39], "mot": "un billet médical", "domaine": "Monde du travail", "definition": "Un document du médecin qui confirme une consultation.", "exemple": "J'ai apporté un billet médical."},
    {"id": "travail-08", "activityIds": [39], "mot": "une superviseure", "domaine": "Monde du travail", "definition": "La personne responsable des employés.", "exemple": "Ma superviseure m'a appelé ce matin."},
    {"id": "travail-09", "activityIds": [39], "mot": "une pièce d'identité", "domaine": "Monde du travail", "definition": "Un document officiel qui prouve qui on est.", "exemple": "Apportez une pièce d'identité pour l'inscription."},
    {"id": "travail-10", "activityIds": [39], "mot": "le télétravail", "domaine": "Monde du travail", "definition": "Travailler depuis la maison.", "exemple": "Je serai en télétravail aujourd'hui."},
    {"id": "travail-11", "activityIds": [39], "mot": "une entrevue d'embauche", "domaine": "Monde du travail", "definition": "Une rencontre pour obtenir un emploi.", "exemple": "Elle a une entrevue d'embauche à 13 h 30."},
    {"id": "travail-12", "activityIds": [39], "mot": "une orthopédagogue", "domaine": "Monde du travail", "definition": "La personne qui aide les élèves ayant des difficultés d'apprentissage.", "exemple": "L'orthopédagogue rencontre mon fils demain."},

    # ── module-urgence (activité 36) ──
    {"id": "urgence-01", "activityIds": [36], "mot": "une brûlure", "domaine": "Santé", "definition": "Une blessure causée par la chaleur, le feu ou un liquide chaud.", "exemple": "Elle a une brûlure à l'avant-bras."},
    {"id": "urgence-02", "activityIds": [36], "mot": "l'urgence", "domaine": "Santé", "definition": "Le service de l'hôpital pour les cas qui ne peuvent pas attendre.", "exemple": "Rendez-vous à l'urgence aujourd'hui."},
    {"id": "urgence-03", "activityIds": [36], "mot": "une cloque", "domaine": "Santé", "definition": "Une petite poche de liquide sur la peau brûlée.", "exemple": "Il ne faut jamais percer une cloque."},
    {"id": "urgence-04", "activityIds": [36], "mot": "un pansement", "domaine": "Santé", "definition": "Ce qu'on pose sur une plaie pour la protéger.", "exemple": "Le médecin pose un pansement propre."},
    {"id": "urgence-05", "activityIds": [36], "mot": "une plaie", "domaine": "Santé", "definition": "Une blessure ouverte sur la peau.", "exemple": "On nettoie la plaie avant le pansement."},
    {"id": "urgence-06", "activityIds": [36], "mot": "le deuxième degré", "domaine": "Santé", "definition": "Le niveau d'une brûlure avec des cloques.", "exemple": "C'est une brûlure du deuxième degré."},
    {"id": "urgence-07", "activityIds": [36], "mot": "une cicatrice", "domaine": "Santé", "definition": "La marque qui reste sur la peau après une blessure.", "exemple": "Il ne devrait pas garder de cicatrice."},
    {"id": "urgence-08", "activityIds": [36], "mot": "un congé de maladie", "domaine": "Santé", "definition": "Des jours autorisés pour ne pas travailler quand on est blessé.", "exemple": "Elle reçoit un congé de maladie de trois jours."},
    {"id": "urgence-09", "activityIds": [36], "mot": "éclabousser", "domaine": "Santé", "definition": "Projeter un liquide en gouttes.", "exemple": "L'huile chaude a éclaboussé son bras."},
    {"id": "urgence-10", "activityIds": [36], "mot": "désinfecter", "domaine": "Santé", "definition": "Nettoyer pour éliminer les microbes.", "exemple": "L'infirmière va désinfecter la plaie."},
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
# ── Jeu de rôle « relations sociales » (module-relations) ────────────────────
# Faire connaissance dans une activité de loisir. Les deux rôles sont
# « nouveau » et « membre » : c'est le scénario qui a obligé à sortir la paire
# locataire/propriétaire du code.
JEU_DE_ROLE_RENCONTRES = {
    "volleyball": {
        "contexte": (
            "La ligue de volleyball du centre communautaire, le jeudi soir, avant "
            "l'entraînement. Les gens arrivent au vestiaire les uns après les autres. "
            "Une nouvelle personne s'est inscrite cette semaine."
        ),
        "membre": [
            "Tu joues dans cette ligue depuis six ans ; c'est ta voisine qui t'avait amenée.",
            "Tu travailles de jour et tu arrives toujours à la dernière minute.",
            "Il y a un tournoi de deux jours à Drummondville en avril, et il reste des places.",
            "L'équipe cherche quelqu'un qui sait servir : la moitié des joueuses ratent leur service.",
            "Tu fais du covoiturage avec deux autres joueuses et tu pourrais en prendre une de plus.",
            "Tu as un bébé de trois mois à la maison ; tu ne dors plus mais tu ne manques jamais un jeudi.",
            "Tu es curieuse de savoir ce que la personne faisait avant d'arriver ici.",
        ],
        "nouveau": [
            "Tu t'es inscrit cette semaine, tu ne connais encore personne.",
            "Tu jouais régulièrement dans ton pays, puis tu as arrêté pendant un an en arrivant.",
            "Ton horaire de travail t'empêche de venir les autres soirs.",
            "Tu cherches surtout à rencontrer du monde ; le sport est une raison de sortir.",
            "Tu hésites à demander comment fonctionne la ligue, de peur de déranger.",
        ],
    },
    "cuisine": {
        "contexte": (
            "La cuisine collective du quartier, un samedi matin. Six personnes préparent "
            "ensemble des plats à rapporter chez elles. C'est la première fois que l'une "
            "d'elles y participe."
        ),
        "membre": [
            "Tu viens à la cuisine collective une fois par mois, depuis deux ans.",
            "Chacun repart avec quatre portions ; la contribution est de cinq dollars.",
            "Le groupe choisit les recettes ensemble, le mois d'avant.",
            "Tu cuisines déjà pour la semaine le dimanche et tu trouves que ça sauve du temps.",
            "Il y a aussi un groupe de marche le dimanche matin, parti de la même place.",
            "Tu veux savoir ce que la personne cuisine chez elle et ce qu'elle mangeait dans son pays.",
        ],
        "nouveau": [
            "C'est ta première fois ; une collègue t'en a parlé.",
            "Tu cuisines en grande quantité chez toi et tu congèles.",
            "Tu ne sais pas si tu dois apporter quelque chose ni combien ça coûte.",
            "Tu travailles cinq jours sur sept et tes soirées sont courtes.",
        ],
    },
    "marche": {
        "contexte": (
            "Le groupe de marche du dimanche matin, dans un parc du quartier. Le groupe "
            "part à neuf heures et marche une heure et demie. Quelqu'un s'est joint au "
            "groupe pour la première fois ce matin."
        ),
        "membre": [
            "Tu marches avec ce groupe chaque dimanche depuis trois ans, beau temps mauvais temps.",
            "Le groupe part à neuf heures pile et personne n'attend les retardataires.",
            "En hiver, le groupe marche quand même ; il faut des crampons sous les bottes.",
            "Tu as déménagé neuf fois avant d'avoir trente ans et tu connais tous les quartiers.",
            "Après la marche, la moitié du groupe va déjeuner au restaurant du coin.",
            "Tu veux savoir depuis quand la personne habite le quartier.",
        ],
        "nouveau": [
            "Tu viens pour la première fois ; tu as vu l'affiche au centre communautaire.",
            "Tu habites le quartier depuis quatorze mois et tu connais peu de monde.",
            "Tu travailles la semaine et le dimanche est ton seul matin libre.",
            "Tu ne sais pas jusqu'où le groupe marche ni combien de temps ça dure.",
        ],
    },
}


# ── Jeu de rôle « trouver son chemin » (module-deplacement) ──────────────────
# Demander ou expliquer un itinéraire. Rôles « perdu » et « guide ».
JEU_DE_ROLE_ITINERAIRES = {
    "metro": {
        "contexte": (
            "Un terminus d'autobus au-dessus d'une station de métro, en fin d'avant-midi. "
            "Quelqu'un cherche son quai et tourne en rond depuis plusieurs minutes."
        ),
        "guide": [
            "Tu travailles dans ce terminus depuis des années et tu connais chaque quai.",
            "Les quais 1 à 10 sont à cet étage ; les quais 11 à 18 sont derrière, en bas.",
            "On y va par le corridor vitré, à gauche, puis l'escalier au bout.",
            "L'autobus 90 part du quai 12 et va vers Saint-Hubert.",
            "Le prochain départ est dans une dizaine de minutes ; il y en a un aux vingt minutes.",
            "Le plancher du corridor vient d'être lavé : tu préviens qu'il est glissant.",
            "Tu ne donnes jamais tout d'un coup : tu réponds à ce qu'on te demande.",
        ],
        "perdu": [
            "Tu cherches le quai 12 et tu tournes en rond depuis dix minutes.",
            "Ton autobus part bientôt et tu as peur de le manquer.",
            "Tu ne sais pas qu'il y a un deuxième étage de quais.",
            "Tu répètes ce qu'on te dit pour être sûr d'avoir compris.",
        ],
    },
    "rue": {
        "contexte": (
            "Un coin de rue d'un quartier résidentiel, en après-midi. Quelqu'un vient de "
            "descendre de l'autobus et cherche une adresse à quelques rues de là."
        ),
        "guide": [
            "Tu habites le quartier et tu connais toutes les rues.",
            "La rue cherchée est à dix minutes à pied : tout droit jusqu'au feu, puis à gauche.",
            "Après avoir tourné, il faut marcher deux coins de rue.",
            "On passe devant une pharmacie et une caisse ; la rue est juste après la caisse.",
            "La rue est petite et facile à manquer.",
            "Les numéros pairs sont du côté droit en marchant dans ce sens.",
        ],
        "perdu": [
            "Tu cherches le 340 d'une rue que tu n'as jamais vue.",
            "Tu es à pied et tu as un rendez-vous dans vingt minutes.",
            "Tu ne sais pas si les numéros montent ou descendent de ce côté-ci.",
            "Tu répètes l'itinéraire à voix haute pour le retenir.",
        ],
    },
    "edifice": {
        "contexte": (
            "L'entrée d'un centre de formation, le matin. Quelqu'un doit se rendre à pied "
            "à un bureau situé à une dizaine de minutes, de l'autre côté d'un parc."
        ),
        "guide": [
            "Tu as fait ce trajet la semaine passée et tu t'en souviens bien.",
            "Il faut sortir par la porte principale, tourner à droite et marcher jusqu'au parc.",
            "On traverse le parc par le sentier du milieu et on arrive sur la rue Victoria.",
            "Là, on tourne à gauche ; l'édifice est le troisième, celui à la porte vitrée.",
            "L'enseigne est petite, au-dessus de la porte : il n'y a pas de grande affiche.",
            "Le trajet prend douze minutes ; s'il pleut, le sentier du parc devient de la boue.",
        ],
        "perdu": [
            "Tu dois te rendre à ce bureau demain matin et tu n'y es jamais allé.",
            "Tu veux savoir combien de temps ça prend, pour partir à la bonne heure.",
            "Tu demandes des repères visuels : tu n'es pas sûr de reconnaître l'édifice.",
            "Tu poses tes questions une à la fois.",
        ],
    },
}


# ── Jeu de rôle « s'inscrire à une activité » (module-activite) ──────────────
# S'informer sur une activité de loisir offerte par une ville. Rôles « parent »
# (la personne qui s'informe) et « prepose » (le comptoir).
JEU_DE_ROLE_ACTIVITES = {
    "natation": {
        "contexte": (
            "Le comptoir d'un centre sportif municipal, en fin d'avant-midi. Une personne "
            "veut inscrire son enfant de neuf ans à un cours de natation pour la session "
            "d'automne."
        ),
        "prepose": [
            "Deux groupes sont offerts pour cet âge : le samedi de 9 h à 10 h, et le mardi après l'école.",
            "La session dure douze semaines, de septembre à décembre.",
            "Le tarif est de 85 $ pour les résidents de la ville, 110 $ pour les autres.",
            "Une facture récente ou un bail au nom du parent sert de preuve de résidence.",
            "Il faut un maillot, une serviette, des sandales, et le bonnet de bain est obligatoire.",
            "Le bonnet se vend 5 $ au comptoir.",
            "Le groupe du samedi est de niveau débutant : l'enfant n'a pas besoin de savoir nager.",
            "Il est préférable que les parents restent dans la salle d'attente ; une vitre permet de voir.",
            "Il n'y a pas de reprise si un cours est manqué, mais chaque cours revoit ce qui précède.",
        ],
        "parent": [
            "Ton enfant a neuf ans et ne sait pas nager.",
            "Tu travailles le mardi après-midi : seul le samedi te convient.",
            "Tu habites la ville depuis un an mais tu ignores ce qui sert de preuve.",
            "Tu veux savoir ce qu'il faut apporter, et combien ça coûte en tout.",
            "Tu répètes les informations avant de partir, pour être sûr.",
        ],
    },
    "chorale": {
        "contexte": (
            "Le comptoir d'un centre communautaire, en début de soirée. Une personne "
            "s'intéresse à la chorale du jeudi soir, annoncée dans le dépliant de la ville."
        ),
        "prepose": [
            "La chorale a lieu le jeudi de 19 h à 21 h, dix semaines.",
            "Il reste trois places seulement ; le dépliant portait une étoile pour cette raison.",
            "Le tarif est de 30 $ pour les résidents, 45 $ pour les autres.",
            "Il n'est pas nécessaire de savoir lire la musique ni d'avoir de l'expérience.",
            "Il faut apporter une bouteille d'eau et un crayon ; les partitions sont fournies.",
            "L'inscription se fait au comptoir ou en ligne, mais la preuve de résidence doit être présentée.",
            "Le premier cours a lieu la semaine prochaine.",
        ],
        "parent": [
            "Tu cherches une activité pour toi, pas pour un enfant.",
            "Tu n'as jamais chanté dans une chorale et tu ne lis pas la musique.",
            "Tu veux savoir s'il reste des places et combien ça coûte.",
            "Tu as une facture d'électricité dans ton sac, mais tu ne sais pas si elle convient.",
        ],
    },
    "soccer": {
        "contexte": (
            "Le comptoir du service des loisirs d'une ville, un samedi matin. Une personne "
            "veut inscrire sa fille de onze ans au soccer pour la saison d'été."
        ),
        "prepose": [
            "La saison va de mai à août, une pratique le mercredi soir et un match le samedi.",
            "Le tarif est de 120 $ pour les résidents, 160 $ pour les autres, chandail inclus.",
            "Il faut des souliers à crampons, des protège-tibias et une bouteille d'eau.",
            "Les inscriptions se terminent le 15 avril ; après, l'enfant est mis sur une liste d'attente.",
            "Une preuve de résidence et la carte d'assurance maladie de l'enfant sont demandées.",
            "Les parents bénévoles sont bienvenus : il manque toujours des accompagnateurs.",
            "En cas de pluie, les matchs sont reportés et l'information est envoyée par courriel.",
        ],
        "parent": [
            "Ta fille a onze ans et joue déjà au soccer à l'école.",
            "Tu ne sais pas quel équipement il faut acheter ni combien ça coûte.",
            "Tu travailles certains samedis et tu veux savoir si c'est un problème.",
            "Tu demandes s'il est trop tard pour s'inscrire.",
        ],
    },
}


# ── Jeu de rôle « faire l'épicerie » (module-alimentation) ───────────────────
# Commander à un comptoir d'épicerie. Rôles « client » et « commis ».
JEU_DE_ROLE_EPICERIE = {
    "boucherie": {
        "contexte": (
            "Le comptoir de la boucherie d'une épicerie de quartier, en fin d'après-midi. "
            "Un client attend son tour ; il y a du monde derrière lui."
        ),
        "commis": [
            "Les poitrines de poulet sont à 6,50 $ la livre ; quatre poitrines font environ une livre et demie.",
            "Le bœuf haché maigre est à 7 $ la livre ; il en reste environ trois livres.",
            "Le poulet vient du Québec ; le bœuf vient de l'Ontario.",
            "Le bœuf haché se garde deux jours au réfrigérateur, trois mois au congélateur.",
            "Tu peux emballer séparément si on te le demande, mais tu ne le proposes pas.",
            "Il y a un spécial sur les cuisses de poulet cette semaine : 3,50 $ la livre.",
            "Tu demandes toujours « autre chose ? » avant de conclure.",
        ],
        "client": [
            "Tu veux du poulet pour quatre personnes et du bœuf haché pour un plat.",
            "Tu ne sais pas combien de poids représentent quatre poitrines.",
            "Tu veux savoir d'où vient la viande et combien de temps elle se garde.",
            "Tu voudrais que le poulet soit emballé en deux paquets, mais tu hésites à le demander.",
        ],
    },
    "poisson": {
        "contexte": (
            "Le comptoir du poisson d'une épicerie, un jeudi matin. Le poisson frais du jour "
            "est disposé sur la glace."
        ),
        "commis": [
            "Il y a de la truite d'élevage du Québec à 12 $ la livre, et du saumon de l'Atlantique à 16 $.",
            "Le poisson frais se garde deux jours au réfrigérateur, trois mois au congélateur s'il est bien emballé.",
            "Il faut le sortir de son papier et le mettre dans un contenant fermé, dans le bas du frigo.",
            "La truite est plus délicate que le saumon : dix minutes de cuisson suffisent.",
            "Tu peux le vider et l'écailler sur demande, sans supplément.",
            "Il reste aussi des filets surgelés, moins chers, dans le congélateur de l'allée voisine.",
        ],
        "client": [
            "Tu veux du poisson frais, mais tu ne le cuisineras pas ce soir.",
            "Tu ne sais pas combien de temps ça se garde ni comment le conserver.",
            "Tu n'as jamais cuisiné de truite et tu veux savoir si c'est difficile.",
            "Tu compares le prix avec le saumon avant de choisir.",
        ],
    },
    "charcuterie": {
        "contexte": (
            "Le comptoir de la charcuterie d'une épicerie, en avant-midi. Les jambons et les "
            "fromages sont derrière la vitre."
        ),
        "commis": [
            "Il y a un jambon du Québec à 2,70 $ les cent grammes, et un autre importé à 1,90 $.",
            "L'importé est nettement plus salé ; tu le dis si on te le demande.",
            "Deux cents grammes de jambon tranché mince font environ une douzaine de tranches.",
            "Une fois ouvert, le jambon tranché se garde trois jours dans un contenant fermé.",
            "Tu demandes toujours si on veut tranché mince ou épais.",
            "Il y a aussi du fromage en spécial cette semaine, mais tu ne le proposes que si on demande autre chose.",
        ],
        "client": [
            "Tu veux du jambon pour les sandwichs de la semaine.",
            "Tu ne sais pas combien de grammes commander pour une douzaine de tranches.",
            "Tu veux savoir d'où il vient et s'il se garde longtemps.",
            "Tu regardes le prix : deux jambons, deux prix différents.",
        ],
    },
}


# ── Jeu de rôle « acheter un appareil » (module-achat) ───────────────────────
# S'informer sur un électroménager en magasin. Rôles « acheteur » et « vendeur ».
JEU_DE_ROLE_APPAREILS = {
    "laveuse": {
        "contexte": (
            "Le rayon des électroménagers d'un grand magasin, un samedi après-midi. Trois "
            "laveuses presque identiques sont alignées ; un client les regarde depuis un "
            "moment."
        ),
        "vendeur": [
            "Le premier modèle fait 76 cm de large porte ouverte ; le deuxième, 68 cm.",
            "Le deuxième est le plus vendu, justement parce qu'il entre partout.",
            "Il fait 52 décibels à l'essorage — une conversation normale en fait 60.",
            "Le troisième est plus grand, plus cher, et consomme 30 litres de moins par brassée.",
            "La garantie est d'un an, pièces et main-d'œuvre, sur tous les modèles.",
            "La garantie prolongée coûte 120 $ pour trois ans de plus et couvre le déplacement.",
            "La livraison coûte 60 $, gratuite au-dessus de 1000 $ ; l'installation est à part, 40 $.",
            "Le spécial sur le deuxième modèle se termine dimanche.",
            "Tu demandes toujours l'espace disponible avant de parler de prix.",
        ],
        "acheteur": [
            "Ton local de sous-sol fait environ un mètre de large.",
            "Tu fais trois brassées par semaine, pour une famille de trois.",
            "Tu ne sais pas ce que veut dire « capacité » ni si 52 décibels est beaucoup.",
            "Tu veux comprendre ce qui justifie l'écart de prix entre deux modèles.",
            "Tu ignores que l'installation n'est pas comprise dans la livraison.",
        ],
    },
    "refrigerateur": {
        "contexte": (
            "Le même rayon, devant les petits réfrigérateurs. Un client cherche un appareil "
            "pour un sous-sol, avec un espace limité."
        ),
        "vendeur": [
            "Le modèle proposé fait 145 cm de haut sur 55 cm de large.",
            "Il consomme 300 kilowattheures par année, un des plus économes de sa catégorie.",
            "La garantie est d'un an complet et de cinq ans sur le compresseur.",
            "Le compresseur est la pièce la plus chère : c'est pour ça qu'il est garanti plus longtemps.",
            "La livraison coûte 60 $ et n'est pas incluse à ce prix-là.",
            "L'appareil entre dans une voiture ; le magasin aide à le charger mais ne le déballe pas.",
            "Il faut le laisser debout douze heures avant de le brancher, après transport couché.",
        ],
        "acheteur": [
            "Ton espace fait un mètre cinquante de haut et soixante centimètres de large.",
            "Tu veux savoir ce qu'il coûtera en électricité chaque année.",
            "Tu hésites entre payer la livraison et le transporter toi-même.",
            "Tu ne sais pas qu'un réfrigérateur transporté couché doit reposer avant d'être branché.",
        ],
    },
    "cuisiniere": {
        "contexte": (
            "Le rayon des cuisinières. Un client remplace un appareil brisé et doit décider "
            "rapidement, mais veut comprendre ce qu'il paie."
        ),
        "vendeur": [
            "Les cuisinières standard font 76 cm de large : c'est l'ouverture prévue dans presque toutes les cuisines.",
            "Il existe des modèles à éléments serpentins, moins chers, et à surface vitrocéramique, plus chers et plus faciles à nettoyer.",
            "La garantie est d'un an complet ; les éléments sont garantis cinq ans sur certains modèles.",
            "La livraison est de 60 $ ; l'installation d'une cuisinière électrique est de 40 $ et demande une prise à 240 volts.",
            "Le magasin reprend l'ancien appareil sans frais si c'est noté sur le bon de livraison.",
            "Il faut vérifier que la prise existante est bien à 240 volts avant l'achat.",
        ],
        "acheteur": [
            "Ta cuisinière est brisée depuis trois jours et tu cuisines tous les jours.",
            "Tu ne sais pas si ta prise est à 240 volts.",
            "Tu veux savoir ce que le magasin fait de l'ancien appareil.",
            "Tu compares deux modèles et tu veux comprendre ce qui justifie 200 $ d'écart.",
        ],
    },
}


# ── Jeu de rôle « au restaurant » (module-restaurant) ────────────────────────
# Commander en salle à manger. Rôles « client » et « serveur ».
JEU_DE_ROLE_RESTAURANT = {
    "commande": {
        "contexte": (
            "Un restaurant de quartier, en début de soirée. Le client est assis, la carte "
            "devant lui, et le serveur vient prendre la commande."
        ),
        "serveur": [
            "La table d'hôte est à 32 $ : soupe ou salade, poisson du jour ou poulet, dessert au choix.",
            "Le poisson du jour est de la truite, servie avec des légumes et du riz.",
            "À la carte, le poulet est à 24 $ et la truite à 27 $.",
            "L'eau du robinet est gratuite ; on la sert en carafe.",
            "Le dessert du jour est un gâteau aux noix — tu vérifies en cuisine si on te pose une question d'allergie.",
            "Le service prend environ vingt minutes pour le plat principal.",
            "Tu demandes toujours si le client veut quelque chose à boire.",
        ],
        "client": [
            "Tu n'as jamais mangé dans ce restaurant et tu ne connais pas les formules.",
            "Tu hésites entre la table d'hôte et un plat seul.",
            "Tu as une allergie aux arachides et tu dois le dire avant le dessert.",
            "Tu veux savoir ce qu'il y a dans le plat du jour avant de choisir.",
        ],
    },
    "repas": {
        "contexte": (
            "Le repas est servi depuis quelques minutes. Le serveur passe voir si tout va "
            "bien ; le client a une demande à faire."
        ),
        "serveur": [
            "Tu passes voir les tables toutes les dix minutes environ.",
            "Le sel, le poivre et l'eau sont apportés sans discussion, en moins d'une minute.",
            "Un plat froid se réchauffe en cuisine en deux minutes ; tu t'excuses et tu le fais.",
            "Une erreur de commande — une sauce non demandée — se refait, mais cela prend vingt minutes.",
            "Tu proposes toujours de refaire le plat, même si le client dit que ce n'est pas nécessaire.",
            "Tu notes les erreurs pour la cuisine.",
        ],
        "client": [
            "Ton plat est un peu froid et tu hésites à le dire.",
            "Tu voudrais aussi du sel et un peu d'eau.",
            "Tu ne veux pas déranger, mais tu préfères que ce soit corrigé.",
            "Tu ne connais pas les formules polies et tu commences par des phrases trop directes.",
        ],
    },
    "addition": {
        "contexte": (
            "La fin du repas. Le client demande l'addition ; deux personnes ont mangé et il "
            "faut décider comment payer."
        ),
        "serveur": [
            "Le total est de 58,40 $, taxes comprises.",
            "Tu demandes toujours « ensemble ou séparé ? » avant d'imprimer.",
            "Une fois l'addition imprimée ensemble, la séparer prend plusieurs minutes.",
            "Le terminal demande le pourboire avant le code ; il propose 15, 18 et 20 %.",
            "Les pourcentages proposés sont calculés après taxes ; « autre montant » est en bas de l'écran.",
            "Tu acceptes le comptant, le débit et le crédit.",
        ],
        "client": [
            "Vous êtes deux et tu ne sais pas s'il vaut mieux payer ensemble ou séparément.",
            "Tu ne sais pas si le pourboire est déjà sur l'addition.",
            "Tu ne sais pas combien laisser ni comment le calculer.",
            "Tu veux payer par débit.",
        ],
    },
}


# ── Jeu de rôle « acheter des vêtements » (module-vetements) ─────────────────
# S'informer sur un vêtement, l'essayer, l'échanger. Rôles « client » et
# « conseiller ».
JEU_DE_ROLE_PRESENTER = {
    "accueil": {
        "contexte": (
            "L'accueil d'un centre de francisation, un lundi matin. Une personne "
            "arrive pour la première fois. Le stade est celui du grand débutant."
        ),
        "accueillant": [
            "Tu demandes le prénom, puis le nom de famille — l'un après l'autre.",
            "Tu demandes d'épeler le nom de famille, une lettre à la fois.",
            "Tu répètes ce que tu as compris pour vérifier.",
            "Les cours du matin commencent à huit heures trente.",
            "Tu dis « bienvenue » à la fin.",
        ],
        "eleve": [
            "C'est ton premier jour. Tu dis bonjour et tu donnes ton nom.",
            "On te demande d'épeler ton nom de famille.",
            "Tu ne comprends pas toujours : tu demandes de parler plus lentement.",
            "Tu remercies avant de partir.",
        ],
    },
    "classe": {
        "contexte": (
            "Une salle de classe de francisation, avant le début du cours. Deux "
            "personnes qui ne se connaissent pas s'assoient côte à côte."
        ),
        "accueillant": [
            "Tu es un élève de la classe, arrivé il y a quelques semaines.",
            "Tu dis ton prénom, ton pays et ta langue — et tu poses les mêmes "
            "questions en retour.",
            "Tu tutoies : entre élèves, on se tutoie.",
            "Tu parles lentement, avec des phrases très courtes.",
        ],
        "eleve": [
            "Tu es nouveau dans la classe.",
            "Tu dis ton prénom, d'où tu viens et quelle langue tu parles.",
            "Tu demandes la même chose à l'autre personne.",
            "Tu peux dire si tu as des enfants.",
        ],
    },
    "secretariat": {
        "contexte": (
            "Le comptoir du secrétariat. On remplit la fiche d'un nouvel élève : "
            "nom, adresse, langues parlées."
        ),
        "accueillant": [
            "Tu demandes une information à la fois : le nom, puis l'adresse, "
            "puis les langues.",
            "Tu fais épeler le nom de famille et le nom de la rue.",
            "Si on ne comprend pas, tu répètes plus lentement — sans hausser la voix.",
            "Tu ne demandes jamais deux choses dans la même phrase.",
        ],
        "eleve": [
            "Tu donnes ton nom, ton adresse et tes langues.",
            "Tu ne comprends pas le mot « adresse » du premier coup.",
            "Tu demandes de répéter plus lentement.",
            "Tu épelles le nom de ta rue.",
        ],
    },
}

JEU_DE_ROLE_ALLEES = {
    "farine": {
        "contexte": (
            "Les allées d'une grande épicerie, un samedi matin. Un client cherche un "
            "produit qu'il ne trouve pas là où il s'attendait à le voir."
        ),
        "commis": [
            "La farine de maïs n'est pas avec les farines : elle est dans l'allée des "
            "produits du monde, l'allée douze, tout au fond.",
            "Les farines ordinaires sont dans l'allée quatre, avec le sucre.",
            "L'allée douze rassemble les produits d'Amérique latine, d'Asie et d'Afrique.",
            "Il y a deux formats : un sac d'un kilo à 4,29 $ et un sac de cinq kilos "
            "à 15,99 $.",
            "Les grands sacs sont sur la tablette du bas ; ils sont lourds.",
            "Si le client ne trouve pas, tu lui dis de revenir te voir.",
        ],
        "client": [
            "Tu veux de la farine de maïs pour faire des tortillas.",
            "Tu as déjà cherché avec les autres farines et tu n'as rien trouvé.",
            "Tu ne connais pas l'expression « produits du monde ».",
            "Tu voudrais le grand format, mais tu veux d'abord savoir le prix.",
        ],
    },
    "special": {
        "contexte": (
            "L'allée de la viande, un jeudi. La circulaire de la semaine vient de "
            "sortir et le client a une photo sur son téléphone."
        ),
        "commis": [
            "Le poulet entier est bien à 3 $ la livre cette semaine ; le prix régulier "
            "est de 4,79 $.",
            "Le spécial finit le mercredi soir ; les nouveaux spéciaux commencent le "
            "jeudi.",
            "Il y a une limite de quatre par famille.",
            "Les poitrines, elles, ne sont pas en spécial : 6,50 $ la livre.",
            "Si l'étiquette du rayon montre encore l'ancien prix, c'est la caisse qui "
            "fait foi — et il faut le signaler au service à la clientèle.",
        ],
        "client": [
            "Tu as vu le poulet à 3 $ la livre dans la circulaire.",
            "Tu veux vérifier que c'est le bon prix et jusqu'à quand ça dure.",
            "Tu ne sais pas si le spécial vaut aussi pour les poitrines.",
            "Tu veux savoir combien tu peux en acheter.",
        ],
    },
    "entretien": {
        "contexte": (
            "L'allée des produits d'entretien. Le client tient une bouteille et "
            "regarde les petits dessins sur l'étiquette."
        ),
        "commis": [
            "Les produits pour le plancher sont dans l'allée dix, au milieu.",
            "Le nettoyant fort porte un dessin de main percée : il est corrosif, il "
            "faut des gants.",
            "Il existe une version douce, sans mise en garde, un peu plus chère.",
            "Il ne faut jamais mélanger deux produits d'entretien.",
            "Tu ne fais pas de sermon : tu réponds à ce qu'on te demande, simplement.",
        ],
        "client": [
            "Tu cherches un produit pour laver le plancher.",
            "Tu as vu un dessin sur la bouteille et tu ne sais pas ce qu'il veut dire.",
            "Tu as de jeunes enfants à la maison.",
            "Tu veux savoir s'il existe quelque chose de moins dangereux.",
        ],
    },
}

JEU_DE_ROLE_VETEMENTS = {
    "manteau": {
        "contexte": (
            "Le rayon des manteaux d'hiver d'un magasin de vêtements, en octobre. Un "
            "client regarde les modèles sans savoir par où commencer."
        ),
        "conseiller": [
            "Les manteaux vont du petit au très grand ; la taille varie beaucoup d'une marque à l'autre.",
            "Un manteau d'hiver se prend une taille de plus : il faut de la place pour un chandail.",
            "La cote de température est écrite en petit sur l'étiquette : moins vingt, moins trente.",
            "Le duvet est plus chaud et plus léger que la fibre, mais il craint l'humidité.",
            "La bonne longueur pour attendre l'autobus, c'est aux genoux.",
            "Un capuchon bordé de fourrure coupe le vent sur le visage : ce n'est pas décoratif.",
            "Les cabines d'essayage sont au fond ; on peut essayer autant de modèles qu'on veut.",
            "Tu demandes toujours pour quelle température le client veut son manteau.",
        ],
        "client": [
            "Tu passes tes hivers avec trois couches de vêtements et tu veux enfin un vrai manteau.",
            "Tu ne connais pas ta taille dans les marques d'ici.",
            "Tu ne sais pas ce que veut dire « coté moins trente ».",
            "Tu hésites entre deux couleurs et tu voudrais un avis.",
        ],
    },
    "bottes": {
        "contexte": (
            "Le rayon des chaussures d'hiver. Un client cherche des bottes et ne connaît "
            "pas les usages d'ici."
        ),
        "conseiller": [
            "Pour des bottes d'hiver, on prend une demi-pointure de plus : il faut la place d'un bas épais.",
            "Il faut chercher « imperméable » sur l'étiquette et une semelle avec du relief.",
            "Le verglas est plus dangereux que la neige : c'est la semelle qui compte.",
            "Les bottes sont cotées elles aussi : moins vingt, moins quarante.",
            "On peut les essayer en marchant dans le magasin, mais jamais dehors.",
            "Une fois portées dehors, elles ne peuvent plus être échangées.",
            "Tu demandes toujours la pointure habituelle avant de proposer un modèle.",
        ],
        "client": [
            "Tu fais du neuf et demi, mais tes souliers d'ici te semblent serrés.",
            "Tu ne sais pas qu'il faut prévoir la place d'un bas de laine.",
            "Tu veux savoir ce qui compte pour la neige et pour le verglas.",
            "Tu veux les essayer sérieusement avant de décider.",
        ],
    },
    "echange": {
        "contexte": (
            "Le comptoir du service à la clientèle. Un client rapporte un article acheté "
            "il y a moins de deux semaines."
        ),
        "conseiller": [
            "Le délai d'échange ou de remboursement est de trente jours avec la facture.",
            "L'article doit être en état : étiquettes en place, jamais porté dehors.",
            "Un remboursement se fait sur le moyen de paiement utilisé — carte sur carte, comptant sur comptant.",
            "Après un échange, les trente jours repartent à partir de la nouvelle date.",
            "Les articles marqués « vente finale » ne sont ni repris ni échangés.",
            "La mise de côté dure quatorze jours et demande un dépôt d'environ vingt pour cent.",
            "Tu demandes toujours la facture en premier.",
        ],
        "client": [
            "Tu rapportes un article qui ne fait pas la bonne taille.",
            "Tu as la facture, l'achat date d'une douzaine de jours.",
            "Tu ne sais pas si tu préfères un échange ou un remboursement.",
            "Tu veux savoir ce qui se passe si le nouvel article ne convient pas non plus.",
        ],
    },
}


# Trois situations pour le module de niveau 2 « Prendre l'autobus ». Elles sont
# volontairement plus courtes que celles des modules de niveau 4 : un élève de
# niveau 2 tient une phrase à la fois, et l'assistant doit s'y tenir aussi.
JEU_DE_ROLE_AUTOBUS = {
    "chemin": {
        "contexte": (
            "Un trottoir de quartier, en fin d'avant-midi. Quelqu'un cherche la "
            "bibliothèque et arrête un passant."
        ),
        "habitant": [
            "Tu habites le quartier depuis longtemps et tu connais les rues.",
            "La bibliothèque est sur la rue Bélanger, à dix minutes à pied.",
            "Le chemin tient en trois étapes : tout droit, à droite au feu, au coin à gauche.",
            "Tu donnes UNE étape à la fois et tu attends que l'autre la répète.",
            "Tu emploies des repères qui se voient : le feu, la pharmacie, l'école.",
            "Si on te le demande, tu dis que ce n'est pas loin et qu'on ne peut pas la manquer.",
        ],
        "passager": [
            "Tu cherches la bibliothèque et tu ne connais pas le quartier.",
            "Tu répètes chaque étape à voix haute pour être sûr d'avoir compris.",
            "Si on parle vite, tu demandes « plus lentement, s'il vous plaît ».",
            "Avant de partir, tu redis tout le chemin et tu demandes « c'est ça ? ».",
        ],
    },
    "arret": {
        "contexte": (
            "Un arrêt d'autobus, tôt le matin. Deux personnes attendent. L'une "
            "des deux prend cette ligne tous les jours."
        ),
        "habitant": [
            "Tu prends le 51 chaque matin et tu connais l'horaire par cœur.",
            "C'est bien l'arrêt du 51, et il passe aux quinze minutes.",
            "Le prochain est à huit heures dix — dans cinq minutes.",
            "Le dernier du soir passe à onze heures et quart ; après, il n'y en a plus.",
            "L'autobus qui va vers l'est est de l'autre côté de la rue.",
            "Tu réponds à la question posée, sans ajouter trois informations de plus.",
        ],
        "passager": [
            "Tu ne sais pas si c'est le bon arrêt et tu veux vérifier.",
            "Tu demandes l'heure du prochain passage, puis celle du dernier.",
            "Tu confonds parfois « huit heures dix » et « huit heures et demie » : tu fais répéter.",
            "Tu remercies avant de conclure.",
        ],
    },
    "correspondance": {
        "contexte": (
            "À bord d'un autobus, en début d'après-midi. Quelqu'un doit se rendre "
            "à l'hôpital et n'est pas sûr d'être dans le bon véhicule."
        ),
        "habitant": [
            "Tu prends souvent cette ligne et tu sais où elle va.",
            "Cet autobus va vers l'est ; pour l'hôpital, il faut le 32.",
            "L'arrêt du 32 est de l'autre côté de la rue, devant la pharmacie.",
            "Le trajet prend une vingtaine de minutes.",
            "Tu rappelles de garder la correspondance : le deuxième autobus est alors gratuit.",
            "Tu expliques ce qu'est une correspondance si on ne connaît pas le mot.",
        ],
        "passager": [
            "Tu vas à l'hôpital et tu n'es pas sûr d'avoir pris le bon autobus.",
            "Tu ne connais pas le mot « correspondance » et tu demandes ce que c'est.",
            "Tu veux savoir combien de temps ça prend.",
            "Tu répètes le numéro de l'autobus et l'endroit de l'arrêt pour les retenir.",
        ],
    },
}


JEU_DE_ROLE_SCENARIOS = {
    "autobus": {
        "cadre": "une demande d'information dans la rue ou à un arrêt d'autobus",
        "contexte_label": "L'endroit où vous vous trouvez tous les deux",
        "cas": JEU_DE_ROLE_AUTOBUS,
        "adresse": "Vouvoie l'élève : on ne se connaît pas, on se croise dans un lieu public.",
        "sujets": [
            "le lieu ou la ligne d'autobus qu'on cherche",
            "la direction, avec un repère qui se voit",
            "l'heure du prochain passage, et celle du dernier",
            "le temps que ça prend",
            "la répétition de ce qui a été compris, pour vérifier",
            "un merci pour finir",
        ],
        "cloture": ("Quand l'information est donnée, demande à l'autre de la répéter "
                    "dans ses mots, confirme d'un mot, et souhaite bonne journée."),
        "ouverture": {
            "passager": "Excusez-moi, madame. Je cherche la bibliothèque.",
            "habitant": "Bonjour. Vous cherchez quelque chose ?",
        },
        "roles": {
            "habitant": {
                "qui": ("Tu connais le quartier et les autobus. L'élève est la personne "
                        "qui demande."),
                "conduite": ("Niveau 2 : phrases courtes, une information à la fois, "
                             "jamais deux questions dans la même réplique. Emploie des "
                             "repères visibles plutôt que des noms de rue. Attends que "
                             "l'élève répète avant de continuer, et reformule plus "
                             "lentement s'il te le demande, sans jamais te fâcher."),
            },
            "passager": {
                "qui": ("Tu cherches ton chemin ou ton autobus. L'élève connaît les "
                        "lieux et te renseigne."),
                "conduite": ("Pose une seule question à la fois. Répète ce qu'on te dit "
                             "pour vérifier. Si l'explication va trop vite ou donne trois "
                             "choses d'un coup, demande de reprendre plus lentement — "
                             "c'est exactement ce que le module apprend à faire."),
            },
        },
    },
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
    "relations": {
        "cadre": "une rencontre informelle dans une activité de loisir du quartier",
        "contexte_label": "L'activité où vous vous trouvez tous les deux",
        "cas": JEU_DE_ROLE_RENCONTRES,
        "adresse": "Tutoie l'élève : on se tutoie entre participants d'une activité de loisir.",
        "sujets": [
            "ce que chacun fait de ses semaines (travail, horaire, ménage, repas)",
            "depuis quand chacun participe à l'activité",
            "comment chacun a connu l'activité et qui l'y a amené",
            "une expérience personnelle du passé (une arrivée, un déménagement, un voyage)",
            "ce qui a changé depuis ce moment-là",
            "une prochaine occasion de se revoir",
        ],
        "cloture": ("Quand les sujets sont couverts, propose une prochaine occasion de se "
                    "revoir et termine la conversation chaleureusement."),
        "ouverture": {
            "nouveau": "Bonjour, c'est ma première fois ici.",
            "membre": "Salut ! Toi, je ne t'ai jamais vue ici.",
        },
        "roles": {
            "membre": {
                "qui": ("Tu participes à cette activité depuis des années. L'élève est une "
                        "personne qui vient pour la première fois."),
                "conduite": ("Accueille-la, mais ne raconte pas tout d'un coup : pose des "
                             "questions sur ses semaines, son horaire, ce qu'elle faisait "
                             "avant d'arriver ici. Réagis à ce qu'elle raconte avant "
                             "d'enchaîner. Si elle reste sur des réponses d'un mot, relance "
                             "avec une question ouverte."),
            },
            "nouveau": {
                "qui": ("Tu viens pour la première fois à cette activité. L'élève y participe "
                        "depuis longtemps et t'accueille."),
                "conduite": ("Pose tes questions une à la fois : comment ça marche, à quelle "
                             "heure, combien ça coûte, qui vient. Raconte un peu de ta propre "
                             "vie quand on t'en demande, sans monopoliser la parole."),
            },
        },
    },
    "chemin": {
        "cadre": "une demande d'itinéraire dans une ville",
        "contexte_label": "L'endroit où vous vous trouvez tous les deux",
        "cas": JEU_DE_ROLE_ITINERAIRES,
        "adresse": "Vouvoie l'élève : on ne se connaît pas, on se croise dans un lieu public.",
        "sujets": [
            "le point de départ et la destination",
            "les étapes du trajet, dans l'ordre, à l'impératif",
            "les repères visuels qui confirment qu'on est sur le bon chemin",
            "la direction à prendre (le nom du terminus, le côté de la rue)",
            "la durée du trajet",
            "ce qu'il ne faut pas faire ou ne pas manquer",
        ],
        "cloture": ("Quand l'itinéraire est complet, demande à l'autre de le répéter dans "
                    "ses mots, confirme, et souhaite bonne route."),
        "ouverture": {
            "perdu": "Excusez-moi, je cherche mon chemin.",
            "guide": "Bonjour, vous avez l'air de chercher quelque chose ?",
        },
        "roles": {
            "guide": {
                "qui": ("Tu connais bien l'endroit et tu expliques le chemin. L'élève est "
                        "la personne qui cherche."),
                "conduite": ("Donne une ou deux étapes à la fois, jamais tout l'itinéraire "
                             "d'un coup — personne ne retient six étapes. Emploie "
                             "l'impératif et des repères visuels. Attends que l'élève "
                             "confirme avant de continuer, et corrige gentiment s'il "
                             "répète de travers."),
            },
            "perdu": {
                "qui": ("Tu cherches ton chemin et tu ne connais pas l'endroit. L'élève "
                        "connaît les lieux et t'explique."),
                "conduite": ("Pose tes questions une à la fois : où, de quel côté, combien "
                             "de temps. Répète ce qu'on te dit pour vérifier. Si "
                             "l'explication va trop vite ou saute une étape, demande de "
                             "reprendre — c'est exactement ce qu'il faut apprendre à faire."),
            },
        },
    },
    "activite": {
        "cadre": "une demande de renseignements au comptoir d'un centre de loisirs municipal",
        "contexte_label": "L'activité dont il est question",
        "cas": JEU_DE_ROLE_ACTIVITES,
        "adresse": "Vouvoie l'élève : c'est un comptoir de service, on ne se connaît pas.",
        "sujets": [
            "le jour, l'heure et la durée de la session",
            "le tarif, et la différence entre résidents et non-résidents",
            "les documents à fournir pour l'inscription",
            "le matériel à apporter, et ce qui est obligatoire",
            "les conditions d'admission (âge, niveau, expérience)",
            "la façon de s'inscrire et de payer",
        ],
        "cloture": ("Quand tout a été demandé, invite l'autre à récapituler ce qu'il a "
                    "retenu, confirme, et termine poliment."),
        "ouverture": {
            "parent": "Bonjour, je voudrais des renseignements sur une activité.",
            "prepose": "Bonjour, qu'est-ce que je peux faire pour vous ?",
        },
        "roles": {
            "prepose": {
                "qui": ("Tu travailles au comptoir du centre et tu renseignes le public. "
                        "L'élève est la personne qui s'informe."),
                "conduite": ("Réponds à ce qu'on te demande, sans dérouler toute la fiche "
                             "d'un coup : c'est à l'élève d'aller chercher chaque "
                             "renseignement. S'il oublie une information importante — le "
                             "matériel obligatoire, la preuve de résidence — ne la donne "
                             "pas d'office ; attends, et mentionne-la seulement à la fin "
                             "s'il n'y a pas pensé."),
            },
            "parent": {
                "qui": ("Tu viens t'informer sur une activité. L'élève travaille au "
                        "comptoir et te renseigne."),
                "conduite": ("Pose tes questions une à la fois : l'horaire, le prix, le "
                             "matériel, les documents. Réagis à chaque réponse. Si une "
                             "réponse est vague, demande une précision — un chiffre, une "
                             "heure, un nom de document."),
            },
        },
    },
    "epicerie": {
        "cadre": "une commande à un comptoir d'épicerie",
        "contexte_label": "Le comptoir où vous vous trouvez",
        "cas": JEU_DE_ROLE_EPICERIE,
        "adresse": "Vouvoie l'élève : c'est un commerce, on ne se connaît pas.",
        "sujets": [
            "le produit demandé et sa sorte ou sa coupe",
            "la quantité, avec une unité (livre, grammes, nombre de morceaux)",
            "la provenance du produit",
            "combien de temps ça se garde, et comment le conserver",
            "le prix, vérifié avant de repartir",
            "une demande particulière : emballer à part, trancher mince",
        ],
        "cloture": ("Quand la commande est complète, annonce le prix, demande « autre "
                    "chose ? », puis salue."),
        "ouverture": {
            "client": "Bonjour, je voudrais commander quelque chose, s'il vous plaît.",
            "commis": "Bonjour ! Qu'est-ce que je vous sers ?",
        },
        "roles": {
            "commis": {
                "qui": ("Tu travailles au comptoir et tu sers les clients. L'élève est le "
                        "client."),
                "conduite": ("Demande ce qu'il veut, puis la quantité — l'une après "
                             "l'autre, jamais les deux d'un coup. Si la quantité est "
                             "vague, propose un poids et demande si ça convient. Ne donne "
                             "la provenance et la durée de conservation que si on te les "
                             "demande. Annonce le prix à la fin."),
            },
            "client": {
                "qui": ("Tu commandes à un comptoir. L'élève travaille derrière et te "
                        "sert."),
                "conduite": ("Dis ce que tu veux, puis attends qu'on te demande la "
                             "quantité. Pose une question sur la provenance et une sur la "
                             "conservation. Si l'élève oublie d'annoncer le prix, demande-le "
                             "avant de partir."),
            },
        },
    },
    "appareil": {
        "cadre": "une demande de renseignements au rayon des électroménagers d'un magasin",
        "contexte_label": "Le rayon où vous vous trouvez",
        "cas": JEU_DE_ROLE_APPAREILS,
        "adresse": "Vouvoie l'élève : c'est un commerce, on ne se connaît pas.",
        "sujets": [
            "les dimensions de l'appareil et l'espace disponible",
            "la capacité et la consommation",
            "la différence entre deux modèles, et ce qui justifie l'écart de prix",
            "ce que couvre la garantie, et ce qu'elle ne couvre pas",
            "le paiement : taxes, versements",
            "la livraison, l'installation, et la reprise de l'ancien appareil",
        ],
        "cloture": ("Quand tout a été demandé, récapitule le prix total — appareil, taxes, "
                    "livraison, installation — puis laisse l'autre décider sans le presser."),
        "ouverture": {
            "acheteur": "Bonjour, je cherche un appareil et j'aurais quelques questions.",
            "vendeur": "Bonjour ! Je peux vous aider ?",
        },
        "roles": {
            "vendeur": {
                "qui": ("Tu vends des électroménagers et tu connais bien tes modèles. "
                        "L'élève est le client."),
                "conduite": ("Commence par demander l'espace disponible : c'est ce qui "
                             "élimine le plus de modèles. Réponds à ce qu'on te demande, "
                             "un point à la fois. Ne mentionne ni la livraison, ni "
                             "l'installation, ni la garantie prolongée avant qu'on te les "
                             "demande — mais si le client conclut sans avoir parlé de "
                             "l'installation, préviens-le à la toute fin."),
            },
            "acheteur": {
                "qui": ("Tu veux acheter un appareil. L'élève est le vendeur et te "
                        "renseigne."),
                "conduite": ("Pose tes questions une à la fois : les dimensions, la "
                             "capacité, la consommation, puis la garantie et la livraison. "
                             "Demande une précision chaque fois qu'on te donne un chiffre "
                             "sans point de comparaison — « 52 décibels, c'est beaucoup ? »"),
            },
        },
    },
    "restaurant": {
        "cadre": "un repas dans un restaurant avec service aux tables",
        "contexte_label": "Le moment du repas où vous êtes",
        "cas": JEU_DE_ROLE_RESTAURANT,
        "adresse": "Vouvoie l'élève : c'est un service, on ne se connaît pas.",
        "sujets": [
            "les formules du menu : carte, menu du jour, table d'hôte, à la carte",
            "ce que contient un plat, et ce qui est servi avec",
            "une allergie ou une restriction alimentaire",
            "les boissons, et ce qui est gratuit",
            "signaler poliment ce qui ne va pas",
            "l'addition, les taxes et le pourboire",
        ],
        "cloture": ("Quand le repas est réglé, remercie et souhaite une bonne fin de "
                    "journée ou de soirée."),
        "ouverture": {
            "client": "Bonsoir. Nous sommes prêts à commander, je crois.",
            "serveur": "Bonsoir ! Vous avez fait votre choix ?",
        },
        "roles": {
            "serveur": {
                "qui": ("Tu es serveur ou serveuse dans un restaurant de quartier. L'élève "
                        "est le client."),
                "conduite": ("Réponds à ce qu'on te demande, sans réciter tout le menu. Si "
                             "on te pose une question sur un plat, réponds précisément. Si "
                             "on te signale un problème, excuse-toi et propose une "
                             "solution. Ne mentionne le pourboire que si on te pose la "
                             "question."),
            },
            "client": {
                "qui": ("Tu manges au restaurant. L'élève est le serveur ou la serveuse et "
                        "s'occupe de toi."),
                "conduite": ("Pose tes questions une à la fois : les formules, le contenu "
                             "d'un plat, les boissons. Emploie des formes polies. Si un "
                             "problème survient, signale-le sans agressivité — et laisse "
                             "l'élève proposer la solution."),
            },
        },
    },
    "presenter": {
        "cadre": "une première rencontre, où l'on se présente",
        "contexte_label": "L'endroit où vous vous trouvez",
        "cas": JEU_DE_ROLE_PRESENTER,
        "adresse": ("Vouvoie l'élève à l'accueil et au secrétariat ; tutoie-le dans "
                    "la classe, où l'on se tutoie entre élèves."),
        "sujets": [
            "le prénom et le nom de famille",
            "épeler le nom, une lettre à la fois",
            "le pays d'où l'on vient",
            "la ville où l'on habite",
            "les langues que l'on parle",
            "les enfants, s'il y en a",
        ],
        "cloture": "Quand la fiche est complète, remercie et souhaite la bienvenue.",
        "ouverture": {
            "eleve": "Bonjour. Je m'appelle…",
            "accueillant": "Bonjour ! Comment vous appelez-vous ?",
        },
        "roles": {
            "accueillant": {
                "qui": ("Tu accueilles une personne qui arrive pour la première fois. "
                        "L'élève est cette personne."),
                "conduite": ("Niveau grand débutant : phrases de cinq mots au plus, une "
                             "question à la fois, jamais deux dans la même phrase. "
                             "Répète ce que tu as compris pour vérifier. Si l'élève ne "
                             "comprend pas, redis la même phrase plus lentement, avec "
                             "d'autres mots plus simples — sans jamais lui reprocher."),
            },
            "eleve": {
                "qui": ("Tu es la personne qui arrive. L'élève joue celle qui "
                        "t'accueille."),
                "conduite": ("Réponds par des phrases courtes. Épelle ton nom si on te "
                             "le demande. Si la question est longue, dis « pardon ? » ou "
                             "« plus lentement, s'il vous plaît »."),
            },
        },
    },
    "allees": {
        "cadre": "la recherche d'un produit dans une grande épicerie",
        "contexte_label": "L'endroit du magasin où vous vous trouvez",
        "cas": JEU_DE_ROLE_ALLEES,
        "adresse": "Vouvoie l'élève : c'est un commerce, on ne se connaît pas.",
        "sujets": [
            "ce que le client cherche",
            "le numéro d'allée, et la façon de le faire répéter",
            "la position : au fond, près de l'entrée, en face des caisses",
            "la hauteur : en haut, au milieu, en bas",
            "le format et la quantité",
            "le prix, et le spécial de la semaine s'il y en a un",
        ],
        "cloture": ("Quand le client a ce qu'il cherchait, dis-lui de revenir te voir "
                    "s'il ne trouve pas, et salue."),
        "ouverture": {
            "client": "Excusez-moi, je cherche quelque chose.",
            "commis": "Bonjour ! Je peux vous aider ?",
        },
        "roles": {
            "commis": {
                "qui": ("Tu travailles dans les allées de l'épicerie et tu places la "
                        "marchandise. L'élève est le client."),
                "conduite": ("Réponds vite et court, comme quelqu'un qui répond à cette "
                             "question cent fois par jour : un numéro d'allée, et une "
                             "précision. Ne répète pas de toi-même — si l'élève n'a pas "
                             "compris, attends qu'il te le demande, puis répète plus "
                             "lentement et compte les allées à voix haute. Ne donne le "
                             "prix ou le format que si on te le demande."),
            },
            "client": {
                "qui": ("Tu cherches un produit dans une épicerie que tu connais mal. "
                        "L'élève travaille au magasin."),
                "conduite": ("Dis ce que tu cherches, sans donner tous les détails d'un "
                             "coup. Si on te donne un numéro d'allée, répète-le pour "
                             "vérifier — « allée cinq ou allée quinze ? ». Demande le "
                             "prix ou le format avant de partir, et remercie."),
            },
        },
    },
    "vetement": {
        "cadre": "un achat de vêtements dans un magasin",
        "contexte_label": "Le rayon où vous vous trouvez",
        "cas": JEU_DE_ROLE_VETEMENTS,
        "adresse": "Vouvoie l'élève : c'est un commerce, on ne se connaît pas.",
        "sujets": [
            "ce que le client cherche, et pour quel usage",
            "la taille ou la pointure, et l'essayage",
            "ce qui ne va pas : serré, large, trop court",
            "la matière, la couleur et la coupe",
            "l'entretien : comment le laver sans l'abîmer",
            "l'échange, le remboursement et les délais",
        ],
        "cloture": ("Quand tout a été demandé, récapitule ce que le client emporte et "
                    "rappelle-lui de garder sa facture."),
        "ouverture": {
            "client": "Bonjour, je cherche quelque chose et j'aurais besoin d'aide.",
            "conseiller": "Bonjour ! Je peux vous aider ?",
        },
        "roles": {
            "conseiller": {
                "qui": ("Tu conseilles les clients au rayon des vêtements. L'élève est le "
                        "client."),
                "conduite": ("Commence par demander pour quel usage et quelle taille. "
                             "Réponds à ce qu'on te demande, un point à la fois. Ne parle "
                             "de l'entretien ni de la politique d'échange que si on te le "
                             "demande — mais si le client conclut sans avoir posé de "
                             "question sur l'échange, rappelle-le-lui à la fin."),
            },
            "client": {
                "qui": ("Tu achètes un vêtement. L'élève travaille au magasin et te "
                        "conseille."),
                "conduite": ("Dis ce que tu cherches, puis attends qu'on te demande ta "
                             "taille. En essayant, décris ce qui ne va pas avec un adjectif "
                             "et un endroit : « c'est serré aux épaules ». Demande un avis "
                             "avant de décider."),
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
    # Chaque scénario nomme ses deux rôles ; l'assistant prend celui que
    # l'élève ne joue pas. La paire locataire/propriétaire était écrite en dur
    # ici : un scénario aux rôles différents n'aurait rien trouvé dans `cas`.
    roles = list(scenario["roles"])
    ia_role = roles[0] if role_eleve == roles[1] else roles[1]
    faits = "\n".join("- " + f for f in cas[ia_role])
    # Les cas de « louer » nomment leur contexte « annonce » depuis l'origine ;
    # les scénarios plus récents utilisent « contexte ».
    contexte = cas.get("contexte") or cas["annonce"]
    role_def = scenario["roles"][ia_role]
    # Un échange informel entre coéquipières ne se vouvoie pas. Les scénarios
    # qui ne disent rien gardent le vouvoiement d'origine.
    adresse = scenario.get("adresse", "Vouvoie l'élève.")

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
        "- " + adresse + "\n"
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
        if path == "/api/prof/documents":
            self._handle_documents_list(params)
            return
        if path == "/api/materiel":
            self._handle_materiel(params)
            return
        if path == "/api/materiel/archive":
            self._handle_materiel_archive(params)
            return
        if path == "/api/forge/etat":
            self._handle_forge_etat()
            return
        if path == "/api/forge/commande":
            self._handle_forge_lire(params)
            return
        if path == "/api/forge/fichier":
            self._handle_forge_fichier(params)
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
            # `?catalogue=1` rend le fonds tel quel, sans aucune date : c'est
            # ce que demande catalogue.html, qui montre tout ce qui existe,
            # tous niveaux confondus, et ne planifie rien. Le drapeau est
            # explicite pour que rien ne change ailleurs — un groupId vide
            # reste une erreur, comme avant.
            teacher = self._require_teacher()
            if not teacher:
                return
            if params.get("catalogue", [""])[0]:
                json_response(self, load_activities())
                return
            group_id = self._group_from_params(teacher, params)
            if group_id is None:
                return
            json_response(self, activities_for_group(group_id))
            return
        if path == "/api/sections":
            self._handle_sections(params)
            return
        if path == "/api/student/sections":
            self._handle_student_sections(params)
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
        if path == "/api/vocab/listes":
            self._handle_vocab_listes(params)
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
        if path == "/api/admin/written-submissions":
            self._handle_written_submissions_list(params)
            return
        if path == "/api/admin/corrige-moi":
            self._handle_corrige_moi_list(params)
            return
        if path in ("/api/admin/analyses-erreurs", "/api/admin/signaux-aide"):
            self._handle_journal_list(path, params)
            return
        if path == "/api/signalements":
            self._handle_signalements_list()
            return

        # Fichiers interactifs intégrés au code : servir directement depuis BASE_DIR
        if path.startswith("/assets/interactive/"):
            super().do_GET()
            return

        # Autres assets uploadés (thumbnails, docs, slideshows) : servir depuis STORAGE_DIR
        if STORAGE_DIR != BASE_DIR and path.startswith("/assets/"):
            self._serve_from_storage(path)
            return

        # La racine est la porte des élèves : ils sont trente pour un
        # enseignant, qui entre par /prof.html et travaille dans
        # /enseignant.html. L'adresse à donner à la classe reste donc courte.
        if path == "/":
            self.path = "/eleve.html"
            super().do_GET()
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
        elif path == "/api/prof/documents":
            self._handle_document_add()
        elif path == "/api/forge/commande":
            self._handle_forge_creer()
        elif path == "/api/forge/annuler":
            self._handle_forge_annuler()
        elif path == "/api/forge/publier":
            self._handle_forge_publier()
        elif path == "/api/materiel/depot":
            self._handle_materiel_depot_add()
        elif path == "/api/materiel/visite":
            self._handle_materiel_visite()
        elif path == "/api/materiel/promotion":
            self._handle_materiel_promotion()
        elif path == "/api/prof/planification/copier":
            self._handle_schedule_copy()
        elif path == "/api/student/access":
            self._handle_log_access()
        elif path == "/api/admin/students":
            self._handle_add_student()
        elif path == "/api/admin/clear-log":
            self._handle_clear_log()
        elif path == "/api/signalement":
            self._handle_signalement()
        elif path == "/api/signalement/essai":
            self._handle_signalement_essai()
        elif path == "/api/student/progress":
            self._handle_student_progress()
        elif path == "/api/correct-french":
            self._handle_correct_french()
        elif path == "/api/corrige-moi/seance":
            self._handle_corrige_moi_seance()
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
        elif path == "/api/ecrit/submit":
            self._handle_written_submit()
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
            # `label` est le nom affiché partout (portail enseignant, journal,
            # progression) ; `prenom` n'est qu'une annotation de l'ancien
            # écran `lms.html`. Renommer sans toucher au code d'accès.
            if "label" in body:
                nouveau = str(body["label"]).strip()
                if nouveau:
                    target["label"] = nouveau
            if "groupId" in body:
                # Déplacer un élève : le groupe d'arrivée doit aussi être à soi
                if self._require_group(teacher, body["groupId"]) is None:
                    return
                target["groupId"] = int(body["groupId"])
            save_students(students)
            json_response(self, {"success": True})
        elif re.match(r"^/api/prof/groupes/\d+$", path):
            self._handle_group_update(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/documents/\d+$", path):
            self._handle_document_update(int(path.rsplit("/", 1)[1]))
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
        elif re.match(r"^/api/admin/written-submissions/[\w-]+$", path):
            self._handle_written_submission_delete(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/groupes/\d+$", path):
            self._handle_group_delete(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/prof/documents/\d+$", path):
            self._handle_document_delete(int(path.rsplit("/", 1)[1]))
        elif re.match(r"^/api/materiel/depot/[\w-]+$", path):
            self._handle_materiel_depot_delete(path.rsplit("/", 1)[1])
        elif re.match(r"^/api/materiel/promotion/[\w:-]+$", path):
            self._handle_materiel_promotion_delete(
                urllib.parse.unquote(path.rsplit("/", 1)[1]))
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

    def _upload_corrige(self, form, slug):
        if "corrige" not in form or not form["corrige"].filename:
            return ""
        f = form["corrige"]
        ext = Path(f.filename).suffix.lower()
        dest = STORAGE_DIR / "assets" / "corriges" / f"{slug}{ext}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(f.file.read())
        return f"assets/corriges/{slug}{ext}"

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
            "level": normalize_level(form.getvalue("level", "")),
            "categorie": normalize_categorie(form.getvalue("categorie", "")),
            "thumbnail": self._upload_thumbnail(form, slug),
            "interactive": self._upload_interactive(form, slug),
            "studentDoc": self._upload_doc(form, slug),
            "slideshow": self._upload_slideshow(form, slug),
            "planCours": self._upload_plan_cours(form, slug),
            "corrige": self._upload_corrige(form, slug),
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

        new_corrige = self._upload_corrige(form, slug)
        if new_corrige:
            self._delete_file(target.get("corrige"))
            target["corrige"] = new_corrige

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

        if "lien" in body:
            body["lien"] = normalize_lien(body["lien"])

        # Une date peut viser une section du module (« Défi 2 ») plutôt que le
        # module entier. On refuse une section inconnue : une faute de frappe
        # créerait une entrée que plus rien ne lit ni n'efface.
        section_id = (body.get("sectionId") or "").strip()
        if section_id:
            connues = {s["id"] for s in sections_of_activity(activity_id)}
            if section_id not in connues:
                json_response(self, {"error": "Section introuvable"}, 404)
                return

        entry = set_schedule_dates(group_id, activity_id, body, section_id)
        json_response(self, {"success": True, "dates": entry})

    def _handle_sections(self, params):
        """Le découpage des modules, avec les dates de section du groupe.

        `{"35": {"sections": [{id, titre, chapeau}], "dates": {sectionId: {…}}}}`
        — le catalogue est commun, les dates appartiennent au groupe."""
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        planif = sections_schedule_for_group(group_id)
        json_response(self, {
            str(aid): {"sections": secs, "dates": planif.get(aid, {})}
            for aid, secs in load_sections_catalogue().items()
        })

    def _handle_student_sections(self, params):
        """Ce qui est ouvert, pour le module lui-même : c'est lui qui verrouille
        ses onglets, l'élève ouvrant le fichier directement."""
        code = params.get("code", [""])[0].strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        try:
            activity_id = int(params.get("activityId", [""])[0])
        except (ValueError, IndexError):
            json_response(self, {"error": "activityId manquant"}, 400)
            return
        sections = sections_state_for_student(student.get("groupId"), activity_id)
        json_response(self, {
            "activityId": activity_id,
            "decoupe": bool(sections),
            "sections": sections,
        })

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

    # ── Forge d'activités ────────────────────────────────────────────────────
    # Le compositeur assemble un prompt ; la forge le fait exécuter par le CLI
    # Claude Code du poste. Voir forge.py. Deux verrous : la session enseignante
    # comme partout ailleurs, et la boucle locale — la forge lance un processus,
    # elle ne doit répondre qu'à quelqu'un assis devant la machine.

    def _forge_locale(self):
        """Refuse toute requête qui ne vient pas de la machine elle-même."""
        hote = self.client_address[0]
        if hote not in ("127.0.0.1", "::1", "localhost"):
            json_response(self, {"error": "La forge ne répond qu'en local"}, 403)
            return False
        return True

    def _handle_forge_etat(self):
        if not self._forge_locale() or not self._require_teacher():
            return
        oui, raison = forge.disponible()
        json_response(self, {"disponible": oui, "raison": raison,
                             "commandes": forge.lister() if oui else []})

    def _handle_forge_creer(self):
        if not self._forge_locale() or not self._require_teacher():
            return
        body = self._read_json_body()
        try:
            fiche = forge.creer(body.get("prompt", ""), body.get("titre", ""),
                                body.get("criteres"))
        except ValueError as e:
            json_response(self, {"error": str(e)}, 400)
            return
        except RuntimeError as e:
            json_response(self, {"error": str(e)}, 503)
            return
        json_response(self, fiche, 201)

    def _handle_forge_lire(self, params):
        if not self._forge_locale() or not self._require_teacher():
            return
        fiche = forge.lire(params.get("id", [""])[0])
        if not fiche:
            json_response(self, {"error": "Commande introuvable"}, 404)
            return
        json_response(self, fiche)

    def _handle_forge_annuler(self):
        if not self._forge_locale() or not self._require_teacher():
            return
        arrete = forge.annuler(self._read_json_body().get("id", ""))
        json_response(self, {"arrete": arrete})

    def _handle_forge_publier(self):
        """Fait entrer une activité générée dans le catalogue et dans le dépôt.

        Le catalogue (`activities.json`) et le dépôt de matériel ne sont pas la
        même chose : le premier dit qu'une activité existe, le second relève les
        fichiers qui la servent. Le second se déduit du premier — d'où la
        régénération de l'inventaire à la fin, sans quoi l'activité serait au
        catalogue mais invisible au dépôt.

        Publiée en atelier, jamais en cours : un cours se découpe en seize
        séances outillées, et une commande n'en produit pas.
        """
        if not self._forge_locale() or not self._require_teacher():
            return
        teacher = self._current_teacher()
        body = self._read_json_body()
        cid = body.get("id", "")
        fiche = forge.lire(cid)
        if not fiche:
            json_response(self, {"error": "Commande introuvable"}, 404)
            return
        if fiche.get("etat") != "fait":
            json_response(self, {"error": "Cette commande n'est pas terminée"}, 409)
            return
        if fiche.get("publieeEn"):
            json_response(self, {"error": "Cette commande est déjà publiée"}, 409)
            return

        activities = load_activities()
        titre = (body.get("titre") or fiche.get("titre") or "").strip() or "Activité générée"
        slug = slugify(titre) or f"activite-{cid}"
        # Deux commandes sur la même situation donneraient le même slug, donc le
        # même dossier : la seconde écraserait la première.
        pris = {slugify(a.get("title", "")) for a in activities}
        if slug in pris or (STORAGE_DIR / "assets" / "interactive" / slug).exists():
            slug = f"{slug}-{cid[:6]}"

        dossier = STORAGE_DIR / "assets" / "interactive" / slug
        try:
            roles, copies = forge.copier_vers(cid, dossier)
        except ValueError as e:
            json_response(self, {"error": str(e)}, 409)
            return

        base = f"assets/interactive/{slug}"
        criteres = fiche.get("criteres") or {}
        niveau = criteres.get("niveau")
        activity = {
            "id": next_id(activities),
            "title": titre,
            "level": f"Niveau {niveau}" if niveau else "Niveau 4",
            "categorie": "atelier",
            "thumbnail": "",
            "interactive": f"{base}/{roles['interactive']}" if "interactive" in roles else "",
            "studentDoc": f"{base}/{roles['fiche']}" if "fiche" in roles else "",
            "slideshow": "",
            "planCours": "",
            # Le catalogue a un emplacement « Corrigé » et un emplacement
            # « Autres » (voir MATERIEL dans catalogue.html) ; la publication
            # les laissait vides et n'envoyait ces fichiers qu'au dépôt. Une
            # enseignante qui cherchait le corrigé à sa place habituelle ne le
            # trouvait donc pas. `eleve.html` n'affiche ni l'un ni l'autre :
            # les remplir ne les met pas sous les yeux de l'élève.
            "corrige": f"{base}/{roles['corrige']}" if "corrige" in roles else "",
            "autres": f"{base}/{roles['notes']}" if "notes" in roles else "",
            "keywords": [],
            "domaineDeVie": criteres.get("domaine") or "",
            "datePrevue": "",
            "origine": {"forge": cid, "publieLe": datetime.now().isoformat(timespec="seconds")},
        }
        activities.append(activity)
        save_activities(activities)

        # Le corrigé, les notes et le rapport ne sont pas l'activité : ils se
        # rangent à côté d'elle, comme n'importe quel fichier déposé par une
        # enseignante. C'est aussi ce qui les tient hors de la vue de l'élève.
        depots = load_depots()
        numero = max((int(str(d.get("id", "0")).rsplit("-", 1)[-1] or 0)
                      for d in depots), default=0)
        # La page interactive y figure aussi : l'inventaire du dépôt ne relève
        # que `slideshow`, `studentDoc` et `planCours` (voir
        # `build/materiel.py`), donc une activité générée qui n'a qu'une page
        # web paraîtrait au dépôt comme « rien encore ».
        etiquettes = {"interactive": "Activité interactive (page web)",
                      "corrige": "Corrigé", "notes": "Notes pour l'enseignant",
                      "rapport": "Rapport de génération"}
        ajoutes = []
        for role, etiquette in etiquettes.items():
            rel = roles.get(role)
            if not rel:
                continue
            numero += 1
            chemin = dossier / rel
            depot = {
                "id": f"dep-{numero:04d}",
                "activiteId": activity["id"],
                "seanceCode": None,
                "type": "fiche",
                "nom": Path(rel).name,
                "chemin": f"{base}/{rel}",
                "format": Path(rel).suffix.lstrip("."),
                "octets": chemin.stat().st_size,
                "auteur": {"id": teacher["id"], "nom": teacher.get("nom", "")},
                "note": etiquette + " — produit par la forge",
                "deposeLe": datetime.now().isoformat(timespec="seconds"),
                "origine": "depot",
            }
            depots.append(depot)
            ajoutes.append(depot)
        if ajoutes:
            save_depots(depots)

        inventaire = regenerer_materiel()
        forge.marquer_publiee(cid, activity["id"])
        json_response(self, {"success": True, "activite": activity,
                             "fichiers": copies, "depots": len(ajoutes),
                             "inventaire": inventaire}, 201)

    def _handle_forge_fichier(self, params):
        """Sert un fichier produit. Le chemin est validé contre la liste des
        fichiers réellement produits : rien d'autre n'est servable."""
        if not self._forge_locale() or not self._require_teacher():
            return
        cid = params.get("id", [""])[0]
        nom = params.get("nom", [""])[0]
        fiche = forge.lire(cid)
        if not fiche or nom not in {f["nom"] for f in fiche["fichiers"]}:
            self.send_error(404)
            return
        chemin = forge.COMMANDES / cid / nom
        data = chemin.read_bytes()
        mime = mimetypes.guess_type(str(chemin))[0] or "text/plain; charset=utf-8"
        self.send_response(200)
        self.send_header("Content-Type", mime)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(data)

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
            "teams": normalize_lien(body.get("teams")),
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
                if "teams" in body:
                    g["teams"] = normalize_lien(body["teams"])
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
        for doc in documents_for_group(group_id):
            self._delete_group_doc_file(doc)
        save_documents([d for d in load_documents() if d.get("groupId") != group_id])
        json_response(self, {"success": True})

    def _handle_schedule_copy(self):
        """Reprend la planification d'un autre groupe de l'enseignant."""
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        group_id = self._require_group(teacher, body.get("groupId"))
        if group_id is None:
            return
        source_id = self._require_group(teacher, body.get("sourceGroupId"))
        if source_id is None:
            return
        if source_id == group_id:
            json_response(self, {"error": "Choisissez un autre groupe"}, 400)
            return
        try:
            decalage = int(body.get("decalage") or 0)
        except (TypeError, ValueError):
            json_response(self, {"error": "Décalage invalide"}, 400)
            return
        copiees = copy_schedule(source_id, group_id, decalage)
        json_response(self, {"success": True, "copiees": copiees})

    # ── Fichiers partagés au groupe ───────────────────────────────────────

    def _delete_group_doc_file(self, doc):
        chemin = doc.get("fichier", "")
        if not chemin:
            return
        cible = STORAGE_DIR / chemin
        try:
            cible.relative_to(GROUP_DOCS_DIR)
        except ValueError:
            return
        if cible.exists():
            cible.unlink()

    # ── Dépôt de matériel ───────────────────────────────────────────────

    def _handle_materiel(self, params):
        """L'inventaire, les dépôts de l'équipe et la date de dernière visite.

        La date sert au repère « nouveau » : elle est renvoyée telle qu'elle
        était, et **n'est pas remise à jour ici**. Si elle l'était, un simple
        rafraîchissement effacerait les repères avant que l'enseignant ait pu
        les lire. C'est `POST /api/materiel/visite` qui l'avance, quand
        l'écran a fini de les afficher."""
        teacher = self._require_teacher()
        if not teacher:
            return
        json_response(self, {
            "materiel": materiel_promu(),
            "depots": load_depots(),
            "promotions": load_promotions(),
            "derniereVisite": teacher.get("derniereVisiteMateriel", ""),
            "role": teacher.get("role", "prof"),
        })

    def _handle_materiel_visite(self):
        """Avance la date de dernière visite du dépôt. Conservée sur le
        compte, pas dans le `localStorage` : l'enseignant qui passe de son
        poste de classe à son portable doit retrouver les mêmes repères."""
        teacher = self._require_teacher()
        if not teacher:
            return
        maintenant = datetime.now().isoformat(timespec="seconds")
        teachers = load_teachers()
        for t in teachers:
            if t["id"] == teacher["id"]:
                t["derniereVisiteMateriel"] = maintenant
        save_teachers(teachers)
        json_response(self, {"success": True, "derniereVisite": maintenant})

    def _handle_materiel_archive(self, params):
        """Fabrique et renvoie une archive. Les fichiers viennent tous de
        l'inventaire : le paramètre d'URL choisit *parmi* eux, il ne désigne
        jamais un chemin."""
        teacher = self._require_teacher()
        if not teacher:
            return

        try:
            activite_id = int(params.get("activiteId", [""])[0])
        except (TypeError, ValueError):
            json_response(self, {"error": "Activité manquante"}, 400)
            return

        portee = params.get("portee", ["module"])[0]
        if portee not in ("module", "presentations", "fiches", "seances"):
            json_response(self, {"error": "Portée inconnue"}, 400)
            return

        codes = [c.strip().upper()
                 for c in (params.get("codes", [""])[0] or "").split(",")
                 if c.strip()]
        if portee == "seances" and not codes:
            json_response(self, {"error": "Aucune séance choisie"}, 400)
            return

        # Inventaire promu : une archive doit descendre ce que l'enseignant
        # voit à l'écran, sinon « Tout prendre » ramènerait l'officiel que
        # l'administration a justement remplacé.
        porteur = next((p for p in materiel_promu().get("porteurs", [])
                        if p.get("activiteId") == activite_id), None)
        activite = next((a for a in load_activities()
                         if a.get("id") == activite_id), None)
        if not porteur or not activite:
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        type_voulu = {"presentations": "presentation",
                      "fiches": "fiche"}.get(portee)
        fichiers = fichiers_pour_archive(portee, porteur, codes, type_voulu)
        if not fichiers:
            json_response(self, {"error": "Aucun fichier à mettre dans l'archive"}, 404)
            return

        donnees = construire_archive(fichiers, porteur.get("slug"))
        nom = nom_archive(porteur, activite, portee, codes)
        self.send_response(200)
        self.send_header("Content-Type", "application/zip")
        self.send_header("Content-Length", str(len(donnees)))
        self.send_header("Content-Disposition", f'attachment; filename="{nom}"')
        self.end_headers()
        self.wfile.write(donnees)

    def _handle_materiel_depot_add(self):
        """Le fichier retravaillé d'un enseignant. Il se place **à côté** du
        fichier officiel, jamais à sa place : c'est une entrée de plus dans
        `depots.json`, et l'inventaire n'est pas touché."""
        teacher = self._require_teacher()
        if not teacher:
            return
        form = self._parse_multipart()
        if form is None:
            json_response(self, {"error": "Aucun fichier reçu"}, 400)
            return
        champ = form["fichier"] if "fichier" in form else None
        if champ is None or not getattr(champ, "filename", ""):
            json_response(self, {"error": "Aucun fichier reçu"}, 400)
            return

        try:
            activite_id = int(form.getvalue("activiteId", ""))
        except (TypeError, ValueError):
            json_response(self, {"error": "Activité manquante"}, 400)
            return
        if not any(a.get("id") == activite_id for a in load_activities()):
            json_response(self, {"error": "Activité introuvable"}, 404)
            return

        depots = load_depots()
        numero = max((int(str(d.get("id", "0")).rsplit("-", 1)[-1] or 0)
                      for d in depots), default=0) + 1
        dep_id = f"dep-{numero:04d}"

        nom = safe_filename(champ.filename)
        suffixe = Path(nom).suffix.lower()
        contenu = champ.file.read()
        DEPOTS_DIR.mkdir(parents=True, exist_ok=True)
        (DEPOTS_DIR / f"{dep_id}{suffixe}").write_bytes(contenu)

        depot = {
            "id": dep_id,
            "activiteId": activite_id,
            "seanceCode": (form.getvalue("seanceCode", "") or "").upper() or None,
            "type": form.getvalue("type", "presentation"),
            "nom": nom,
            "chemin": f"assets/depots/{dep_id}{suffixe}",
            "format": suffixe.lstrip("."),
            "octets": len(contenu),
            "auteur": {"id": teacher["id"], "nom": teacher.get("nom", "")},
            "note": (form.getvalue("note", "") or "").strip(),
            "deposeLe": datetime.now().isoformat(timespec="seconds"),
            "origine": "depot",
        }
        depots.append(depot)
        save_depots(depots)
        json_response(self, {"success": True, "depot": depot}, 201)

    def _handle_materiel_promotion(self):
        """Un dépôt tient désormais lieu de fichier officiel.

        Rien n'est écrasé : la substitution est enregistrée et se fait à la
        lecture. Le fichier officiel reste sur le disque, et `build.py`
        continue de le régénérer sans que personne ait à s'en soucier."""
        teacher = self._require_teacher(admin=True)
        if not teacher:
            return
        body = self._read_json_body() or {}
        fichier_id = body.get("fichierId", "")
        depot_id = body.get("depotId", "")

        porteur, seance, fichier = fichier_du_materiel(fichier_id)
        if not fichier:
            json_response(self, {"error": "Fichier officiel introuvable"}, 404)
            return
        depot = next((d for d in load_depots() if d.get("id") == depot_id), None)
        if not depot:
            json_response(self, {"error": "Dépôt introuvable"}, 404)
            return
        if depot.get("activiteId") != porteur.get("activiteId"):
            json_response(self, {"error": "Ce dépôt n'appartient pas à cette activité"}, 400)
            return

        promotions = [p for p in load_promotions() if p.get("fichierId") != fichier_id]
        promotions.append({
            "fichierId": fichier_id,
            "depotId": depot_id,
            "parId": teacher["id"],
            "parNom": teacher.get("nom", ""),
            "leQuand": datetime.now().isoformat(timespec="seconds"),
        })
        save_promotions(promotions)
        json_response(self, {"success": True, "promotions": promotions}, 201)

    def _handle_materiel_promotion_delete(self, fichier_id):
        """Retour au fichier officiel. Rien à restaurer : il n'a jamais
        bougé."""
        teacher = self._require_teacher(admin=True)
        if not teacher:
            return
        promotions = load_promotions()
        if not any(p.get("fichierId") == fichier_id for p in promotions):
            json_response(self, {"error": "Aucune promotion sur ce fichier"}, 404)
            return
        save_promotions([p for p in promotions if p.get("fichierId") != fichier_id])
        json_response(self, {"success": True})

    def _handle_materiel_depot_delete(self, dep_id):
        """Retrait d'un dépôt. Réservé à l'administration, et le rôle est
        revalidé ici : l'absence du bouton à l'écran n'est pas une garde."""
        teacher = self._require_teacher(admin=True)
        if not teacher:
            return
        depots = load_depots()
        cible = next((d for d in depots if d.get("id") == dep_id), None)
        if not cible:
            json_response(self, {"error": "Dépôt introuvable"}, 404)
            return
        fichier = STORAGE_DIR / cible.get("chemin", "")
        if fichier.exists() and fichier.is_file():
            fichier.unlink()
        save_depots([d for d in depots if d.get("id") != dep_id])
        # Retirer un dépôt promu défait sa promotion : sans ça, l'inventaire
        # pointerait vers un fichier qui n'existe plus.
        promotions = load_promotions()
        restantes = [p for p in promotions if p.get("depotId") != dep_id]
        if len(restantes) != len(promotions):
            save_promotions(restantes)
        json_response(self, {"success": True})

    def _handle_documents_list(self, params):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        json_response(self, documents_for_group(group_id))

    def _handle_document_add(self):
        """Dépôt d'un fichier : il paraît dès aujourd'hui, sans date de retrait.
        L'enseignant ajuste la période ensuite, dans la rangée du fichier."""
        teacher = self._require_teacher()
        if not teacher:
            return
        form = self._parse_multipart()
        if form is None:
            json_response(self, {"error": "Aucun fichier reçu"}, 400)
            return
        group_id = self._require_group(teacher, form.getvalue("groupId", ""))
        if group_id is None:
            return
        champ = form["fichier"] if "fichier" in form else None
        if champ is None or not getattr(champ, "filename", ""):
            json_response(self, {"error": "Aucun fichier reçu"}, 400)
            return

        documents = load_documents()
        doc_id = max((d.get("id", 0) for d in documents), default=0) + 1
        nom = safe_filename(champ.filename)
        dossier = GROUP_DOCS_DIR / str(group_id)
        dossier.mkdir(parents=True, exist_ok=True)
        # Préfixe par l'identifiant : deux fichiers du même nom cohabitent.
        stocke = f"{doc_id}-{slugify(Path(nom).stem) or 'fichier'}{Path(nom).suffix.lower()}"
        contenu = champ.file.read()
        (dossier / stocke).write_bytes(contenu)

        doc = {
            "id": doc_id,
            "groupId": group_id,
            "nom": nom,
            "fichier": f"assets/documents-groupe/{group_id}/{stocke}",
            "taille": len(contenu),
            "ouverture": date.today().isoformat(),
            "fermeture": "",
            "createdAt": date.today().isoformat(),
        }
        documents.append(doc)
        save_documents(documents)
        json_response(self, {"success": True, "document": doc}, 201)

    def _handle_document_update(self, doc_id):
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        documents = load_documents()
        target = next((d for d in documents if d.get("id") == doc_id), None)
        if target is None:
            json_response(self, {"error": "Fichier introuvable"}, 404)
            return
        if self._require_group(teacher, target.get("groupId")) is None:
            return
        for key in ("ouverture", "fermeture"):
            if key in body:
                target[key] = (body[key] or "").strip()
        save_documents(documents)
        json_response(self, {"success": True, "document": target})

    def _handle_document_delete(self, doc_id):
        teacher = self._require_teacher()
        if not teacher:
            return
        documents = load_documents()
        target = next((d for d in documents if d.get("id") == doc_id), None)
        if target is None:
            json_response(self, {"error": "Fichier introuvable"}, 404)
            return
        if self._require_group(teacher, target.get("groupId")) is None:
            return
        self._delete_group_doc_file(target)
        save_documents([d for d in documents if d.get("id") != doc_id])
        json_response(self, {"success": True})

    # ── Gestion des enseignants (administrateur) ──────────────────────────

    def _handle_teachers_list(self):
        teacher = self._require_teacher(admin=True)
        if not teacher:
            return
        groups = load_groups()
        teachers = load_teachers()
        json_response(self, [
            {**public_teacher(t, teachers),
             "nbGroupes": sum(1 for g in groups if g.get("teacherId") == t["id"])}
            for t in teachers
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
        if body.get("role") == "admin" and not is_founder(admin, teachers):
            json_response(self, {
                "error": "Seul le compte fondateur peut ouvrir un compte "
                         "administrateur. Créez un compte « enseignant », "
                         "ou demandez-lui de le faire."
            }, 403)
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
        # Le compte fondateur ne se modifie que par lui-même : sans cette
        # barrière, un administrateur ordinaire s'en emparerait en lui
        # réinitialisant son mot de passe, et la règle du dessus ne tiendrait
        # plus.
        if is_founder(target, teachers) and not is_founder(admin, teachers):
            json_response(self, {
                "error": "Le compte fondateur ne peut être modifié que par lui-même."
            }, 403)
            return
        if "nom" in body:
            target["nom"] = (body["nom"] or "").strip() or target["nom"]
        if "role" in body:
            # Promouvoir ou rétrograder un administrateur revient à en créer
            # un : même réserve que l'ouverture de compte.
            if not is_founder(admin, teachers):
                json_response(self, {
                    "error": "Seul le compte fondateur peut changer le rôle d'un compte."
                }, 403)
                return
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
        if is_founder(target, teachers):
            json_response(self, {
                "error": "Le compte fondateur ne peut pas être supprimé."
            }, 403)
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
        # `activityId` choisit la liste d'un module ; `domain` reste pour la
        # session « tout ce qui est dû », qui traverse les modules.
        try:
            activity_id = int(params.get("activityId", [""])[0])
        except ValueError:
            activity_id = 0

        pool = [
            w for w in available_pool
            if (not domain or w["domaine"] == domain)
            and (not activity_id or activity_id in (w.get("activityIds") or []))
        ]
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

    def _handle_vocab_listes(self, params):
        """L'état de chaque liste de mots offerte à l'élève.

        Une liste, c'est le vocabulaire d'une activité : les mots portent déjà
        leurs `activityIds`, il n'y a donc rien à tenir à jour quand un module
        est réécrit. Un mot enseigné par deux modules compte dans les deux
        listes — c'est le même mot, la même boîte, vu de deux endroits.
        """
        code = params.get("code", [""])[0].strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        pool = get_student_vocab_pool(student.get("groupId"))
        offertes = get_available_activity_ids(student.get("groupId"))
        by_word = {
            p["wordId"]: p for p in load_vocab_progress()
            if p["studentId"] == student["id"]
        }
        today = date.today().isoformat()

        def etat(word):
            p = by_word.get(word["id"])
            if p is None:
                return "new"
            return "mastered" if p["box"] >= VOCAB_BOITE_MAITRISE else "learning"

        listes = {}
        for w in pool:
            for aid in w.get("activityIds") or []:
                if aid not in offertes:
                    continue
                liste = listes.setdefault(
                    aid, {"activityId": aid, "total": 0, "mastered": 0,
                          "learning": 0, "new": 0, "due": 0})
                liste["total"] += 1
                liste[etat(w)] += 1
                p = by_word.get(w["id"])
                if p is not None and p["dueDate"] <= today:
                    liste["due"] += 1

        # Le titre et la catégorie viennent du catalogue : le banc de mots ne
        # recopie aucun libellé d'activité, qui changerait sans lui.
        activites = {a["id"]: a for a in load_activities()}

        # Le rail « Mes outils » d'un module demande sa propre liste en donnant
        # son slug : un module ne connaît pas son numéro d'activité, et c'est
        # le chemin `interactive` du catalogue qui fait la correspondance.
        slug = params.get("module", [""])[0].strip()
        id_courant = 0
        if slug:
            id_courant = next(
                (a["id"] for a in activites.values()
                 if (a.get("interactive") or "").startswith(
                     f"assets/interactive/{slug}/")),
                0,
            )

        for aid, liste in listes.items():
            a = activites.get(aid, {})
            liste["titre"] = a.get("title") or f"Activité {aid}"
            liste["categorie"] = a.get("categorie") or "atelier"
            liste["courante"] = aid == id_courant

        # « Module 10 » suit « Module 9 » : un tri alphabétique le placerait
        # entre le 1 et le 2.
        ordre = {"cours": 0, "atelier": 1}

        def rang(liste):
            m = re.match(r"Module (\d+)", liste["titre"])
            return (ordre.get(liste["categorie"], 9),
                    int(m.group(1)) if m else 999, liste["titre"])

        json_response(self, {
            "listes": sorted(listes.values(), key=rang),
            "dueTotal": sum(
                1 for w in pool
                if (p := by_word.get(w["id"])) is not None and p["dueDate"] <= today
            ),
            "newTotal": sum(1 for w in pool if w["id"] not in by_word),
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

        # ── Progression activité par activité (tuiles du portail élève) ──
        # « exercise_completed » porte les compteurs cumulés zones/zonesDone :
        # c'est la seule source d'un pourcentage par activité.
        par_activite = {}
        for p in progress:
            fiche = par_activite.setdefault(str(p.get("activityId")), {
                "pct": 0, "faite": False, "zones": 0, "zonesDone": 0, "date": "",
            })
            ts = p.get("timestamp", "")
            if ts > fiche["date"]:
                fiche["date"] = ts
            if p.get("event") != "exercise_completed":
                continue
            zones = p.get("zones") or 0
            faites = p.get("zonesDone") or 0
            fiche["zones"] = zones
            fiche["zonesDone"] = faites
            if zones:
                fiche["pct"] = min(100, round(faites / zones * 100))
                fiche["faite"] = faites >= zones
            else:
                # Activité sans découpage en zones : l'événement vaut « terminée ».
                fiche["pct"] = 100
                fiche["faite"] = True

        # ── Régularité des sept derniers jours ───────────────────────────
        debut = date.today() - timedelta(days=6)
        traces = [p.get("timestamp", "") for p in progress]
        traces += [e.get("timestamp", "") for e in load_access_log()
                   if e.get("studentId") == student["id"]]
        moments = []
        for ts in traces:
            try:
                moment = datetime.fromisoformat(ts)
            except ValueError:
                continue
            if moment.date() >= debut:
                moments.append(moment)
        moments.sort()
        # Minutes estimées : on additionne les écarts de moins de trente
        # minutes entre deux traces, et on compte trois minutes par trace
        # isolée. Rien ne mesure le temps réel passé dans une activité.
        minutes = 3.0 if moments else 0.0
        for avant, apres in zip(moments, moments[1:]):
            ecart = (apres - avant).total_seconds() / 60
            minutes += ecart if ecart <= 30 else 3

        # ── Maîtrise du vocabulaire (mots des activités déjà au dossier) ──
        pool_ids = {w["id"] for w in get_student_vocab_pool(group_id)}
        vocab_progress = [
            p for p in load_vocab_progress()
            if p["studentId"] == student["id"] and p["wordId"] in pool_ids
        ]
        total_words = len(pool_ids)
        reviewed_words = len(vocab_progress)
        mastered_words = sum(
            1 for p in vocab_progress if p["box"] >= VOCAB_BOITE_MAITRISE)
        learning_words = reviewed_words - mastered_words
        new_words = total_words - reviewed_words

        json_response(self, {
            "activitiesTotal": len(available_activities),
            "activitiesStarted": len(started_ids & {a["id"] for a in available_activities}),
            "activitiesCompleted": len(completed_ids & {a["id"] for a in available_activities}),
            "nextActivity": next_activity,
            "streak": streak,
            "parActivite": par_activite,
            "semaine": {
                "jours": len({m.date() for m in moments}),
                "sur": 7,
                "minutes": round(minutes),
            },
            "vocab": {
                "total": total_words,
                "mastered": mastered_words,
                "learning": learning_words,
                "new": new_words,
            },
            # Le lien de rencontre et les fichiers appartiennent au groupe, pas
            # à l'élève : ils apparaissent et disparaissent avec leur période.
            "teams": (find_group(group_id) or {}).get("teams", ""),
            "documents": [
                {"nom": d.get("nom", ""), "fichier": d.get("fichier", ""),
                 "taille": d.get("taille", 0)}
                for d in published_documents(group_id)
            ],
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

        Corps attendu : {code, scenario, cas, role, historique:
        [{role:'user'|'assistant', contenu}]}.
        `role` est celui que joue l'ÉLÈVE ; l'assistant prend l'autre. Les
        rôles valides sont ceux du scénario demandé — ils ne sont plus
        forcément locataire/propriétaire.

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
        if (cas not in JEU_DE_ROLE_SCENARIOS[scenario]["cas"]
                or role not in JEU_DE_ROLE_SCENARIOS[scenario]["roles"]):
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

        # Le cache passe avant la clé d'API : une classe garde la voix des
        # passages déjà lus même si la clé vient à manquer.
        chemin = voix_cache_chemin(voix, texte)
        audio = voix_cache_lire(chemin)
        if audio is not None:
            print(f"[voix] cache : {len(texte)} caractères", flush=True)
            self._envoyer_mp3(audio)
            return

        api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
        if not api_key:
            json_response(self, {"error": "Voix non configurée sur le serveur"}, 503)
            return

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
        voix_cache_ecrire(chemin, audio)
        self._envoyer_mp3(audio)

    def _envoyer_mp3(self, audio):
        """Rend du MP3 brut. `no-store` reste : le cache est celui du serveur,
        partagé par la classe, pas celui du navigateur d'un élève."""
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
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        exercice = body.get("exercice", "").strip()[:200]
        notion = body.get("notion", "").strip()[:200]
        # Le module lit son activité dans l'adresse du parent et la joint
        # depuis la greffe de build/greffe_activite_analyse.py. Les analyses
        # d'avant cette greffe n'en ont pas : le tableau de bord les traite
        # comme non rattachées plutôt que de les perdre.
        try:
            activity_id = int(body.get("activityId"))
        except (TypeError, ValueError):
            activity_id = None
        activity_title = str(body.get("activityTitle", ""))[:120]
        items = body.get("items", [])
        if not isinstance(items, list) or not items:
            json_response(self, {"error": "Aucune réponse à analyser"}, 400)
            return

        # Plafond dur : un exercice du module compte au plus une douzaine de
        # lignes. Au-delà, c'est un appel malformé, pas un élève en difficulté.
        lignes = []
        nb_erreurs = 0
        for it in items[:15]:
            if not isinstance(it, dict):
                continue
            if str(it.get("choix", "")) != str(it.get("bonne", "")):
                nb_erreurs += 1
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
        analyse = {
            "patron": parsed.get("patron", ""),
            "explication": parsed.get("explication", ""),
            "conseil": parsed.get("conseil", ""),
        }

        # L'analyse a coûté un appel et dit quelque chose de vrai sur la classe :
        # on la garde. Sans les réponses de l'élève — le patron suffit, et le
        # détail des fautes ne regarde que lui.
        try:
            entrees = load_analyses_erreurs()
            entrees.append(dict(analyse, **{
                "studentId": student["id"],
                "studentLabel": student.get("label", ""),
                "groupId": student.get("groupId"),
                "activityId": activity_id,
                "activityTitle": activity_title,
                "exercice": exercice,
                "notion": notion,
                "items": len(lignes),
                "erreurs": nb_erreurs,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }))
            if len(entrees) > ANALYSES_ERREURS_MAX:
                entrees = entrees[-ANALYSES_ERREURS_MAX:]
            save_analyses_erreurs(entrees)
        except (OSError, ValueError):
            # Un journal qui ne s'écrit pas ne doit pas priver l'élève de son
            # explication : elle est déjà calculée, elle part quand même.
            pass

        json_response(self, analyse)

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

        # Le type de texte est facultatif et vaut « courriel » par défaut : sans
        # lui, la consigne pousserait un bulletin météo ou une affiche vers les
        # formules de politesse d'un courriel. Les modules le tirent du titre
        # de leur liste de critères (« Ton bulletin doit contenir »).
        type_texte = body.get("typeTexte", "").strip()[:40] or "courriel"
        courriel = type_texte == "courriel"

        if courriel:
            amorce = ("L'élève rédige un courriel en réponse à une mise en "
                      "situation, généralement au passé composé pour raconter "
                      "les faits. ")
            registre = ("avec un registre professionnel adapté à un courriel "
                        "(formules de politesse). ")
            conjugaison = "conjugaison (surtout passé composé)"
        else:
            amorce = (f"L'élève rédige un texte du type « {type_texte} » en "
                      "réponse à une mise en situation. ")
            registre = "dans un registre adapté à ce type de texte. "
            conjugaison = "conjugaison"

        system_prompt = (
            "Tu es un tuteur de francisation pour des élèves adultes de Niveau 4 "
            "au Québec (niveau intermédiaire). " + amorce +
            "Voici la mise en situation : "
            f'"{scenario}"\n\n'
            "Analyse le texte de l'élève (objet et corps fournis par "
            "l'utilisateur) et réponds UNIQUEMENT avec un objet JSON valide, "
            "sans texte avant ni après, exactement dans ce format : "
            '{"pertinent": true, "commentairePertinence": "...", '
            '"objetCorrige": "...", "corpsCorrige": "...", '
            '"erreurs": [{"explication": "..."}]} — '
            '"pertinent" indique si le contenu répond bien à la situation '
            "donnée : il est false dès qu'un des éléments exigés par la mise "
            "en situation manque, ou que la contrainte de langue n'est pas "
            "respectée. \"commentairePertinence\" est une phrase courte "
            "(adaptée Niveau 4) qui explique pourquoi, ou qui nomme "
            "précisément ce qui manque si pertinent est false. "
            # Elle est lue par l'élève, pas par l'enseignante : sans cette
            # consigne le modèle écrit « L'élève a oublié de… ».
            "Elle s'adresse directement à l'élève et le tutoie "
            "(« Tu n'as pas dit… »), jamais à la troisième personne. "
            "\"objetCorrige\" et \"corpsCorrige\" sont l'objet et le "
            "corps du texte corrigés en français correct et naturel "
            "(français québécois standard accepté), " + registre +
            "\"erreurs\" contient au maximum 5 explications courtes (une "
            "phrase chacune) des principales erreurs de grammaire, "
            f"{conjugaison} ou syntaxe, en français "
            "simple adapté à un élève de Niveau 4. "
            # Sans cette phrase, un texte sans faute revient avec des
            # felicitations dans "erreurs" — que l'écran affiche en encre
            # d'avertissement, devant un élève qui n'a rien à corriger.
            "N'y mets QUE des erreurs à corriger : si le texte n'en contient "
            "aucune, \"erreurs\" est un tableau vide. Jamais de remarque "
            "positive ni de félicitations dans \"erreurs\"."
        )

        # Un bulletin ou une affiche n'a pas d'objet : la ligne vide ferait
        # inventer un objet à corriger.
        user_content = f"Objet : {subject}\n\n{text}" if subject else text
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

    def _handle_written_submit(self):
        """Une production écrite déposée par l'élève.

        Le pendant de _handle_oral_submit, en plus simple : pas de fichier
        joint, donc du JSON et non du multipart. Comme pour l'oral, rien ne
        part sans le geste de l'élève — la correction seule reste privée.
        """
        body = self._read_json_body()
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        texte = str(body.get("texte", "")).strip()
        if not texte:
            json_response(self, {"error": "Aucun texte fourni"}, 400)
            return

        record = {
            "id": uuid.uuid4().hex,
            "studentId": student["id"],
            "studentCode": code,
            "groupId": student.get("groupId"),
            "prenom": student.get("prenom", ""),
            "theme": str(body.get("theme", ""))[:80],
            "taskId": str(body.get("taskId", ""))[:60],
            "taskLabel": str(body.get("taskLabel", ""))[:120],
            "question": str(body.get("question", ""))[:400],
            # Plafond large : un courriel de niveau 4 fait quelques lignes, mais
            # on ne veut pas tronquer le texte d'un élève qui s'applique.
            "texte": texte[:4000],
            "feedback": str(body.get("feedback", ""))[:2000],
            "createdAt": datetime.now().isoformat(timespec="seconds"),
        }
        subs = load_written_submissions()
        subs.append(record)
        save_written_submissions(subs)

        json_response(self, {"success": True, "id": record["id"]})

    def _handle_written_submissions_list(self, params):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
        subs = sorted(
            (s for s in load_written_submissions()
             if s.get("groupId") == group_id or s.get("studentId") in student_ids),
            key=lambda s: s.get("createdAt", ""), reverse=True)
        json_response(self, subs)

    def _handle_written_submission_delete(self, sub_id):
        if not self._require_teacher():
            return
        subs = load_written_submissions()
        if not any(s["id"] == sub_id for s in subs):
            json_response(self, {"error": "Introuvable"}, 404)
            return
        save_written_submissions([s for s in subs if s["id"] != sub_id])
        json_response(self, {"success": True})

    def _handle_corrige_moi_seance(self):
        """Une réponse corrigée dans « Corrige-moi ! ».

        L'atelier est une pratique libre : ce qui intéresse l'enseignant, ce
        n'est pas chaque réplique mais le cumul par thème. On tient donc un
        seul enregistrement par (élève, thème), mis à jour à chaque réponse.
        """
        body = self._read_json_body()
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return

        theme_id = str(body.get("themeId", "")).strip()[:40]
        if not theme_id:
            json_response(self, {"error": "Thème manquant"}, 400)
            return
        theme_label = str(body.get("themeLabel", "")).strip()[:80]

        entries = load_corrige_moi()
        entry = next(
            (e for e in entries
             if e.get("studentId") == student["id"] and e.get("themeId") == theme_id),
            None,
        )
        if entry is None:
            entry = {
                "studentId": student["id"],
                "studentLabel": student.get("label", ""),
                "groupId": student.get("groupId"),
                "themeId": theme_id,
                "themeLabel": theme_label,
                "answers": 0,
                "firstTryOk": 0,
            }
            entries.append(entry)
        if theme_label:
            entry["themeLabel"] = theme_label
        # Le groupe peut avoir changé depuis la dernière séance.
        entry["studentLabel"] = student.get("label", entry.get("studentLabel", ""))
        entry["groupId"] = student.get("groupId")
        entry["answers"] = entry.get("answers", 0) + 1
        if body.get("memePhrase"):
            entry["firstTryOk"] = entry.get("firstTryOk", 0) + 1
        entry["lastSeen"] = datetime.now().isoformat(timespec="seconds")
        save_corrige_moi(entries)

        json_response(self, {"success": True})

    def _handle_journal_list(self, path, params):
        """Les analyses d'erreurs et les signaux de l'aide, pour un groupe.

        Deux journaux, une seule lecture : même filtre, même tri, et l'un
        comme l'autre ne portent que du travail de module.
        """
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
        source = (load_analyses_erreurs() if path == "/api/admin/analyses-erreurs"
                  else load_signaux_aide())
        cle = "timestamp" if path == "/api/admin/analyses-erreurs" else "lastSeen"
        json_response(self, sorted(
            (e for e in source
             if e.get("groupId") == group_id or e.get("studentId") in student_ids),
            key=lambda e: e.get(cle, ""), reverse=True))

    def _handle_signalement(self):
        """Un enseignant signale un défaut de l'outil.

        On répond dès que la fiche est écrite : le tri par l'IA et le courriel
        partent dans un fil de fond. Un serveur de courriel lent ne doit pas
        faire croire que le signalement n'est pas passé.
        """
        teacher = self._require_teacher()
        if not teacher:
            return
        body = self._read_json_body()
        description = (body.get("description") or "").strip()
        if not description:
            json_response(self, {"error": "Décrivez ce que vous avez vu"}, 400)
            return

        entry = {
            "id": uuid.uuid4().hex[:12],
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "enseignantNom": teacher.get("nom", ""),
            "enseignantCourriel": teacher.get("courriel", teacher.get("email", "")),
            "ecran": (body.get("ecran") or "").strip()[:120],
            "url": (body.get("url") or "").strip()[:400],
            "agent": (self.headers.get("User-Agent") or "")[:300],
            # 4000 caractères : de quoi coller un message d'erreur entier sans
            # laisser un copier-coller accidentel gonfler le fichier.
            "description": description[:4000],
            "analyse": "",
            "courrielEnvoye": False,
        }
        with _VERROU_SIGNALEMENTS:
            entries = load_signalements()
            entries.append(entry)
            save_signalements(entries[-SIGNALEMENTS_MAX:])

        threading.Thread(target=traiter_signalement, args=(entry,),
                         daemon=True).start()
        json_response(self, {"success": True, "id": entry["id"]})

    def _handle_signalements_list(self):
        """Les signalements déjà envoyés, du plus récent au plus ancien.

        Chacun ne voit que les siens : un signalement porte le nom de la
        personne et sa façon de dire les choses.
        """
        teacher = self._require_teacher()
        if not teacher:
            return
        courriel = normalize_email(teacher.get("courriel", teacher.get("email", "")))
        est_admin = teacher.get("role") == "admin"
        entries = [
            e for e in load_signalements()
            if est_admin or normalize_email(e.get("enseignantCourriel", "")) == courriel
        ]
        json_response(self, sorted(entries, key=lambda e: e.get("timestamp", ""),
                                   reverse=True))

    def _handle_signalement_essai(self):
        """Essai d'envoi, ouvert à toute session enseignante.

        Les journaux de l'hébergeur disent pourquoi un courriel n'est pas
        parti, mais il faut les ouvrir, et le message se perd au milieu du
        reste. Ce bouton pose la question et rapporte la réponse à l'écran,
        avec l'état des variables — leur présence, jamais leur valeur.

        Il a d'abord été réservé à l'administrateur, et c'était une fausse
        prudence : elle cachait le bouton à la personne même qui dépannait,
        les rôles n'étant pas les mêmes d'un compte à l'autre. La réponse ne
        porte aucune clé, aucun mot de passe, et la destination est fixée par
        l'hébergeur — un enseignant curieux ne peut qu'écrire au responsable
        du projet.
        """
        teacher = self._require_teacher()
        if not teacher:
            return
        ok, raison = envoyer_courriel(
            "[Francisation] Essai d'envoi",
            "Ceci est un essai déclenché depuis l'espace enseignant.\n"
            "S'il vous parvient, les signalements vous parviendront aussi.\n",
        )
        json_response(self, {
            "ok": ok,
            "raison": raison,
            "config": {
                # Présence seulement : une clé ne s'affiche pas, même à
                # l'administrateur, même sur sa propre page.
                "resend": bool(os.environ.get("RESEND_API_KEY", "").strip()),
                "smtp": bool(os.environ.get("SMTP_HOTE", "").strip()),
                "destinataire": (os.environ.get("SIGNALEMENT_DESTINATAIRE", "").strip()
                                 or os.environ.get("SMTP_USER", "").strip()),
            },
        })

    def _handle_corrige_moi_list(self, params):
        teacher = self._require_teacher()
        if not teacher:
            return
        group_id = self._group_from_params(teacher, params)
        if group_id is None:
            return
        student_ids = {s["id"] for s in load_students() if s.get("groupId") == group_id}
        entries = sorted(
            (e for e in load_corrige_moi()
             if e.get("groupId") == group_id or e.get("studentId") in student_ids),
            key=lambda e: e.get("lastSeen", ""), reverse=True)
        json_response(self, entries)

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
        # Plafonné : un groupe se remplit une classe à la fois, et un client
        # qui demanderait mille codes en fabriquerait mille pour de bon.
        try:
            count = min(30, max(1, int(body.get("count", 1))))
        except (TypeError, ValueError):
            count = 1
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

    def _enregistrer_signal_aide(self, student, event, body):
        """Un cumul par (élève, activité, exercice) plutôt qu'une ligne par clic.

        Ce qu'on veut savoir d'un exercice, c'est combien de fois l'aide a été
        proposée et combien de fois elle a été prise — pas à quelle seconde.
        """
        try:
            activity_id = int(body.get("activityId"))
        except (TypeError, ValueError):
            activity_id = None
        # « plus_open » nomme son bloc `savoir`, les quatre autres `exercice` :
        # c'est le même identifiant d'exercice des deux côtés.
        exercice = str(body.get("exercice") or body.get("savoir") or "")[:80]

        entrees = load_signaux_aide()
        entree = next(
            (e for e in entrees
             if e.get("studentId") == student["id"]
             and e.get("activityId") == activity_id
             and e.get("exercice") == exercice),
            None,
        )
        if entree is None:
            entree = {
                "studentId": student["id"],
                "studentLabel": student.get("label", ""),
                "groupId": student.get("groupId"),
                "activityId": activity_id,
                "activityTitle": str(body.get("activityTitle", ""))[:120],
                "exercice": exercice,
            }
            entrees.append(entree)
        # Le groupe et le nom peuvent avoir changé depuis le dernier passage.
        entree["studentLabel"] = student.get("label", entree.get("studentLabel", ""))
        entree["groupId"] = student.get("groupId")
        entree[event] = entree.get(event, 0) + 1
        try:
            entree["erreurs"] = int(body.get("erreurs"))
        except (TypeError, ValueError):
            pass
        entree["lastSeen"] = datetime.now().isoformat(timespec="seconds")
        save_signaux_aide(entrees)

    def _handle_student_progress(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length))
        code = body.get("code", "").strip().upper()
        student = validate_student_code(code)
        if not student:
            json_response(self, {"error": "Non autorisé"}, 401)
            return
        event = body.get("event", "")
        if event not in ALLOWED_EVENTS and event not in SIGNAUX_AIDE:
            json_response(self, {"error": "Événement invalide"}, 400)
            return
        # Les cinq signaux de l'aide vont dans leur propre journal : progress.json
        # porte l'avancement dans le module, et les écrans de progression
        # compteraient ces lignes-là comme des activités faites.
        if event in SIGNAUX_AIDE:
            self._enregistrer_signal_aide(student, event, body)
            json_response(self, {"success": True})
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
