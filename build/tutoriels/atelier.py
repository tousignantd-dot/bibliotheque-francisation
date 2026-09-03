#!/usr/bin/env python3
"""L'atelier du guide : relire et corriger une capsule dans le navigateur.

    python3 build/tutoriels/atelier.py            # http://localhost:5322
    python3 build/tutoriels/atelier.py 01-tour-du-portail

Le guide imprimé dit ce qui cloche ; il ne permet pas de le réparer. Cette
page-ci, si : chaque plan y montre ses copies d'écran à côté d'un champ de
texte **modifiable**, la durée se recalcule à mesure qu'on tape, et ce qu'on
écrit retourne dans `manifeste.json`. Plus de va-et-vient entre une remarque
dictée et un fichier édité à la main — c'est là que les quatre séries de
corrections du 2 septembre 2026 se sont perdues.

Trois choses se posent par plan :

· **le texte dit**, qui est aussi le texte du procédurier papier ;
· **une remarque sur l'image** — « il manque une capture ici », « on ne voit
  pas le bouton » — gardée à côté du manifeste, jamais dedans : le manifeste
  décrit le film, pas la conversation qu'on a eue dessus ;
· **un commentaire** — ce qui manque au plan et qu'il faut ajouter. Il ne se
  corrige pas soi-même comme le texte : il est adressé à quelqu'un, on repasse
  ensuite voir si c'est fait. D'où la case « réglé », qui garde la trace d'une
  passe à l'autre plutôt que de laisser deviner ce qui a été traité ;
· **une image de référence**, collée ou déposée. Ce n'est pas la capture
  finale : c'est le croquis qui dit ce qu'il faudrait montrer, et le tournage
  la refera proprement.

Rien n'est servi hors de la machine : `127.0.0.1` seulement. La page écrit
dans le dépôt, et une page ouverte au réseau qui écrit dans le dépôt est une
mauvaise idée même sur un poste de travail.
"""
import base64
import http.server
import json
import os
import pathlib
import re
import shutil
import socket
import socketserver
import subprocess
import sys
import time
import webbrowser

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import versions  # noqa: E402
GUIDE = ICI / "guide"
MANIFESTE = ICI / "manifeste.json"
NOTES = GUIDE / "notes.json"
DEMANDE = GUIDE / "demande.json"
PORT = 5322
PORT_DEMO = 5321

# La cadence des voix HD d'Azure, relevée sur les 54 narrations produites :
# 1 888 mots en 695,8 s. Elle sert à donner une durée sans rien synthétiser.
MOTS_PAR_SECONDE = 2.71
RESPIRATION = 0.7

# Posé ici et non dans `__main__` : le gestionnaire le lit à chaque requête.
SEULE = None


def secondes(texte):
    mots = len(re.findall(r"[\wÀ-ÿ'’-]+", texte or ""))
    return round(mots / MOTS_PAR_SECONDE + RESPIRATION, 1)


def charger():
    return json.loads(MANIFESTE.read_text(encoding="utf-8"))


def ecrire(doc):
    # `indent=1`, comme le fichier a toujours été écrit : un guide qui
    # reformate tout le manifeste rendrait chaque correction illisible en revue.
    MANIFESTE.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                         encoding="utf-8")


def notes():
    return json.loads(NOTES.read_text(encoding="utf-8")) if NOTES.exists() else {}


def etat(seule=None):
    doc = charger()
    captures = json.loads((GUIDE / "captures.json").read_text(encoding="utf-8")) \
        if (GUIDE / "captures.json").exists() else {}
    n = notes()
    capsules = []
    for rang, capsule in enumerate(doc["capsules"], 1):
        if seule and capsule["id"] != seule:
            continue
        releve = {p["plan"]: p for p in captures.get(capsule["id"], [])}
        plans = []
        for plan in capsule["plans"]:
            r = releve.get(plan["id"], {"images": []})
            cle = "%s/%s" % (capsule["id"], plan["id"])
            plans.append({
                "id": plan["id"],
                "texte": plan["texte"],
                "texteVoix": plan.get("texte_voix", ""),
                "surligne": plan.get("surligne") or "",
                "gestes": plan.get("gestes", []),
                "images": ["/img/" + im["fichier"].replace("guide/", "", 1)
                           for im in r["images"]],
                "legendes": [im["quand"] for im in r["images"]],
                "secondes": secondes(plan["texte"]),
                "note": n.get(cle, {}).get("note", ""),
                "commentaire": n.get(cle, {}).get("commentaire", ""),
                "regle": n.get(cle, {}).get("regle", False),
                "retirer": n.get(cle, {}).get("retirer", False),
                "croquis": n.get(cle, {}).get("croquis", []),
            })
        capsules.append({"id": capsule["id"], "rang": rang,
                         "titre": capsule["titre"], "plans": plans,
                         "version": versions.etat(capsule["id"])})
    return {"capsules": capsules}


def demo_repond():
    try:
        with socket.create_connection(("127.0.0.1", PORT_DEMO), 1):
            return True
    except OSError:
        return False


def lever_demo(journal):
    """Lance le portail de démonstration s'il ne répond pas.

    Les captures sortent de ce portail-là, jamais des données réelles. Le
    bouton serait inutilisable sans ça : il faudrait ouvrir un terminal entre
    deux corrections, et c'est exactement le va-et-vient qu'on essaie de
    supprimer.
    """
    if demo_repond():
        journal.append("portail de démonstration : déjà en écoute")
        return True
    journal.append("portail de démonstration : démarrage…")
    subprocess.Popen(["/bin/zsh", str(ICI / "lancer_demo.sh")],
                     cwd=str(ICI.parent.parent),
                     env={**os.environ, "PORT": str(PORT_DEMO)},
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(60):
        time.sleep(1)
        if demo_repond():
            journal.append("portail de démonstration : prêt")
            return True
    journal.append("le portail de démonstration n'a pas démarré — "
                   "lancez-le à la main : PORT=5321 ./build/tutoriels/lancer_demo.sh")
    return False


CONSIGNE = """Tu retouches le storyboard d'une capsule vidéo qui montre l'espace
enseignant de « francis », un portail de francisation au Québec. La voix off
s'adresse à une enseignante, au vouvoiement, en français du Québec, sans jargon.

On te donne les plans de la capsule et, pour certains, ce que l'utilisateur
demande d'y changer. Deux sortes de demandes :
· « commentaire » — ce qui manque et qu'il faut écrire dans le texte dit ;
· « image » — ce qui cloche dans ce qu'on montre ; cela se règle en changeant
  les gestes ou le surlignage, jamais en le racontant dans le texte.

Règles :
· Ne touche QUE les plans qui portent une demande. Les autres sortent inchangés.
· N'invente aucune fonction du portail. Si une demande suppose un écran ou un
  bouton dont rien ne prouve l'existence, laisse le plan tel quel et dis-le
  dans le résumé.
· Garde le ton et la longueur : un plan fait de 8 à 20 secondes de parole,
  soit 20 à 55 mots. Une phrase courte vaut mieux qu'une subordonnée.
· Les gestes gardent la forme qu'ils ont déjà. Un repère « apres » doit citer
  des mots réellement présents dans le nouveau texte du plan.

Réponds UNIQUEMENT par un objet JSON, sans texte avant ni après :
{"plans": [{"id": "...", "texte": "...", "gestes": [...]}],
 "resume": "une phrase disant ce que tu as changé"}
Omets « gestes » quand ils ne changent pas."""


def traiter_commentaires(capsule, journal):
    """Fait écrire les corrections demandées, et les pose dans le manifeste.

    C'est ce que le bouton « Mettre à jour » ne pouvait pas faire jusqu'ici :
    les commentaires sont des demandes d'écriture, et l'écriture se délègue au
    CLI de Claude Code — le même que la forge d'activités emploie déjà sur ce
    poste. Un appel par clic, sans outil ni écriture par le modèle : il rend du
    JSON, et c'est **ce script** qui valide et qui écrit. Un modèle qui
    éditerait le manifeste directement pourrait le casser en silence.
    """
    cli = os.environ.get("CLAUDE_CLI") or shutil.which("claude")
    if not cli:
        journal.append("Claude Code n'est pas installé : les commentaires "
                       "restent en attente (npm i -g @anthropic-ai/claude-code)")
        return None
    doc = charger()
    bloc = next((c for c in doc["capsules"] if c["id"] == capsule), None)
    if bloc is None:
        return None
    n = notes()
    demandes = []
    for plan in bloc["plans"]:
        fiche = n.get("%s/%s" % (capsule, plan["id"]), {})
        if fiche.get("regle") or not (fiche.get("commentaire") or fiche.get("note")):
            continue
        demandes.append({"id": plan["id"],
                         "commentaire": fiche.get("commentaire", ""),
                         "image": fiche.get("note", "")})
    if not demandes:
        journal.append("aucun commentaire en attente : le texte ne bouge pas")
        return None

    entree = json.dumps({
        "titre": bloc["titre"],
        "plans": [{"id": p["id"], "texte": p["texte"],
                   "gestes": p.get("gestes", []),
                   "surligne": p.get("surligne", "")} for p in bloc["plans"]],
        "demandes": demandes,
    }, ensure_ascii=False, indent=1)
    journal.append("%d commentaire(s) confiés à Claude…" % len(demandes))
    r = subprocess.run([cli, "-p", "--output-format", "text"],
                       input=CONSIGNE + "\n\n" + entree,
                       capture_output=True, text=True, timeout=600)
    brut = (r.stdout or "").strip()
    debut, fin = brut.find("{"), brut.rfind("}")
    if r.returncode or debut < 0:
        journal.append("Claude n'a rien rendu d'exploitable : "
                       + ((r.stderr or brut)[-200:] or "sortie vide"))
        return None
    try:
        reponse = json.loads(brut[debut:fin + 1])
    except json.JSONDecodeError as e:
        journal.append("réponse illisible (%s) — le texte n'a pas été touché" % e)
        return None

    # Sauvegarde avant d'écrire : le manifeste est le scénario de sept films.
    shutil.copy2(MANIFESTE, MANIFESTE.with_suffix(".json.avant"))
    # Seuls les plans qui portaient une demande sont écrits. Le modèle rend la
    # capsule entière, et un plan qu'on ne lui a rien demandé de changer
    # revenait avec un retour à la ligne en plus — un diff pour rien dans le
    # scénario de sept films.
    vises = {d["id"] for d in demandes}
    touches = []
    for neuf in reponse.get("plans", []):
        plan = next((p for p in bloc["plans"] if p["id"] == neuf.get("id")), None)
        if plan is None or not neuf.get("texte") or neuf["id"] not in vises:
            continue
        neuf["texte"] = neuf["texte"].strip()
        if neuf["texte"] != plan["texte"] or neuf.get("gestes") is not None:
            if neuf["texte"] != plan["texte"]:
                plan["texte"] = neuf["texte"]
            if isinstance(neuf.get("gestes"), list):
                plan["gestes"] = neuf["gestes"]
            touches.append(plan["id"])
    if not touches:
        journal.append("Claude n'a rien trouvé à changer")
        return None
    ecrire(doc)
    journal.append("plans réécrits : " + ", ".join(touches))
    return reponse.get("resume") or ("plans " + ", ".join(touches) + " réécrits")


def mettre_a_jour(capsule):
    """Refait les copies d'écran du guide, et note que la passe est remise.

    Ce que ce bouton fait : rejouer les gestes et reprendre les images. Ce
    qu'il ne fait pas, et ne peut pas faire : écrire le texte qui manque. Les
    commentaires sont adressés à quelqu'un — ils sont rassemblés dans
    `guide/demande.json`, et c'est de là qu'ils se traitent.
    """
    journal = []
    # L'écriture d'abord : les gestes peuvent changer, et il faut alors
    # photographier le nouvel écran, pas l'ancien.
    resume = traiter_commentaires(capsule, journal) if capsule else None
    if not lever_demo(journal):
        return {"ok": False, "journal": journal}
    journal.append("captures : les gestes se rejouent…")
    cmd = ["node", str(ICI / "guide_captures.js"), str(PORT_DEMO)]
    if capsule:
        cmd.append(capsule)
    r = subprocess.run(cmd, cwd=str(ICI.parent.parent),
                       capture_output=True, text=True, timeout=900)
    for ligne in (r.stdout or "").strip().splitlines()[-40:]:
        journal.append(ligne.strip())
    if r.returncode:
        journal.append((r.stderr or "").strip()[-300:] or "les captures ont échoué")
        return {"ok": False, "journal": journal}

    n = notes()
    attente = [{"plan": cle, **fiche} for cle, fiche in n.items()
               if (fiche.get("commentaire") or fiche.get("note"))
               and not fiche.get("regle")]
    DEMANDE.write_text(json.dumps(
        {"remise": time.strftime("%Y-%m-%d %H:%M"), "capsule": capsule,
         "enAttente": attente}, ensure_ascii=False, indent=1), encoding="utf-8")
    journal.append("%d remarque(s) en attente, notées dans guide/demande.json"
                   % len(attente))
    # Rang **majeur** dès que le texte a bougé : c'est une version à relire.
    # Mineur quand seules les images ont été reprises — le compter comme une
    # version à relire ferait mentir le repère.
    fiche = versions.poser(capsule or "toutes",
                           resume or "copies d'écran refaites",
                           majeure=bool(resume))
    journal.append("storyboard %s · %s" % (fiche["version"], fiche["quand"]))
    return {"ok": True, "journal": journal, "enAttente": len(attente)}


class Poste(http.server.BaseHTTPRequestHandler):
    def _rendre(self, corps, type_="application/json", code=200):
        if isinstance(corps, (dict, list)):
            corps = json.dumps(corps, ensure_ascii=False).encode()
        elif isinstance(corps, str):
            corps = corps.encode()
        self.send_response(code)
        self.send_header("Content-Type", type_ + ("; charset=utf-8"
                                                  if "image" not in type_ else ""))
        self.send_header("Content-Length", str(len(corps)))
        self.end_headers()
        self.wfile.write(corps)

    def log_message(self, *a):
        pass

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            self._rendre(PAGE, "text/html")
        elif self.path == "/api/etat":
            self._rendre(etat(SEULE))
        elif self.path.startswith("/img/"):
            f = GUIDE / self.path[5:].split("?")[0]
            if not f.resolve().is_relative_to(GUIDE.resolve()) or not f.exists():
                self._rendre({"error": "introuvable"}, code=404)
                return
            self._rendre(f.read_bytes(), "image/jpeg")
        else:
            self._rendre({"error": "inconnu"}, code=404)

    def do_POST(self):
        corps = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if self.path == "/api/texte":
            doc = charger()
            capsule = next(c for c in doc["capsules"] if c["id"] == corps["capsule"])
            plan = next(p for p in capsule["plans"] if p["id"] == corps["plan"])
            plan["texte"] = corps["texte"]
            ecrire(doc)
            self._rendre({"secondes": secondes(corps["texte"])})
        elif self.path == "/api/note":
            n = notes()
            cle = "%s/%s" % (corps["capsule"], corps["plan"])
            fiche = n.setdefault(cle, {})
            for champ in ("note", "retirer", "commentaire", "regle"):
                if champ in corps:
                    fiche[champ] = corps[champ]
            NOTES.write_text(json.dumps(n, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            self._rendre({"ok": True})
        elif self.path == "/api/majour":
            self._rendre(mettre_a_jour(SEULE))
        elif self.path == "/api/croquis":
            # Le croquis est collé dans la page : il arrive en base64 et se pose
            # à côté des captures, sous un nom qui dit d'où il vient.
            n = notes()
            cle = "%s/%s" % (corps["capsule"], corps["plan"])
            fiche = n.setdefault(cle, {})
            dossier = GUIDE / corps["capsule"]
            dossier.mkdir(parents=True, exist_ok=True)
            rang = len(fiche.get("croquis", [])) + 1
            nom = "%s-croquis-%d.png" % (corps["plan"], rang)
            (dossier / nom).write_bytes(base64.b64decode(corps["donnees"].split(",", 1)[1]))
            fiche.setdefault("croquis", []).append("/img/%s/%s" % (corps["capsule"], nom))
            NOTES.write_text(json.dumps(n, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            self._rendre({"croquis": fiche["croquis"]})
        else:
            self._rendre({"error": "inconnu"}, code=404)


PAGE = r"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Atelier du guide</title>
<style>
:root{
  --ground:#F7F7F5; --card:#fff; --ink:#17181A; --body:#3A3D40; --muted:#6E7175;
  --line:#E4E4E0; --accent:#0A8F5B; --ambre:#B45309; --ambre-fond:#FBF2E2;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:'Nunito',-apple-system,'Helvetica Neue',Arial,sans-serif;font-size:15px;line-height:1.5}
.wrap{max-width:1280px;margin:0 auto;padding:36px 24px 120px}
h1{font-size:30px;color:var(--ink);margin:0 0 6px;letter-spacing:-.02em}
.chapeau{max-width:70ch;margin:0 0 26px;color:var(--body)}
.capsule{background:var(--card);border:1px solid var(--line);border-radius:14px;
  padding:20px 22px;margin:0 0 20px}
h2{font-size:20px;color:var(--ink);margin:0 0 2px;display:flex;align-items:center;gap:11px}
.num{display:inline-grid;place-items:center;width:29px;height:29px;border-radius:999px;
  background:var(--accent);color:#fff;font-size:15px}
.resume{margin:0 0 4px;color:var(--muted);font-size:13px;font-weight:800;
  letter-spacing:.05em;text-transform:uppercase}
/* Le repère de version : « est-ce que tu as mis à jour le storyboard ? » ne
   doit pas être une question qu'on pose, mais une ligne qu'on lit. */
.version{display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;
  margin:0 0 18px;padding:9px 13px;border-radius:9px;background:#E7F0F6;
  border:1px solid #BBD3E2;color:#173B4F;font-size:13px}
.version .rang{font-weight:900;font-size:15px}
.version .quoi{color:#3B6B87}
.version details{width:100%;margin-top:6px}
.version summary{cursor:pointer;color:#3B6B87;font-size:12.5px}
.version ol{margin:8px 0 0;padding-left:20px;font-size:12.5px;color:#3B6B87}
.plan{display:grid;grid-template-columns:44px minmax(0,1fr) minmax(0,1fr);gap:18px;
  padding:18px 0;border-top:1px solid var(--line)}
.plan.retire{opacity:.42}
.cle{font-family:var(--mono);font-size:13px;color:var(--muted);font-weight:700;padding-top:8px}
textarea{width:100%;min-height:120px;resize:vertical;font:inherit;color:var(--ink);
  background:#FCFCFB;border:1px solid var(--line);border-radius:9px;padding:11px 12px}
textarea:focus{outline:2px solid var(--accent);outline-offset:1px;background:#fff}
.note{min-height:60px;background:var(--ambre-fond);border-color:#E8D3A0;color:#4A3706}
/* Deux cases, deux couleurs : l'ambre parle de l'image, l'acier me parle à
   moi. Mêlées, on ne sait plus laquelle attend une action de qui. */
.commentaire{min-height:60px;background:#E7F0F6;border-color:#BBD3E2;color:#173B4F}
.regle{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;
  color:var(--muted);cursor:pointer}
.plan.fait .commentaire{opacity:.5}
.sous{display:flex;align-items:center;gap:14px;margin-top:8px;font-size:12.5px;color:var(--muted)}
.duree{font-family:var(--mono);font-weight:700;color:var(--ink)}
.etiq{font-size:11px;letter-spacing:.07em;text-transform:uppercase;font-weight:800;
  color:var(--muted);margin:14px 0 5px}
.enregistre{color:var(--accent);font-weight:800;opacity:0;transition:opacity .2s}
.enregistre.vu{opacity:1}
figure{margin:0 0 10px}
figure img{width:100%;border:1px solid var(--line);border-radius:7px;display:block}
figcaption{font-size:11px;color:var(--muted);margin-top:3px;letter-spacing:.05em;
  text-transform:uppercase;font-weight:800}
.croquis img{border:2px dashed var(--ambre)}
.depot{border:2px dashed var(--line);border-radius:9px;padding:12px;text-align:center;
  color:var(--muted);font-size:12.5px;cursor:pointer}
.depot:hover,.depot.survol{border-color:var(--accent);color:var(--accent)}
label.retirer{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;
  color:var(--muted);cursor:pointer}
.micro{display:inline-flex;align-items:center;gap:7px;font:inherit;font-size:12.5px;
  font-weight:800;color:var(--accent);background:#fff;border:1px solid var(--accent);
  border-radius:999px;padding:4px 12px;cursor:pointer}
.micro .pastille{width:8px;height:8px;border-radius:999px;background:var(--accent)}
.micro.ecoute{color:#B4090C;border-color:#B4090C;background:#FBECEC}
.micro.ecoute .pastille{background:#B4090C;animation:pouls 1.1s ease-in-out infinite}
@keyframes pouls{0%,100%{opacity:1}50%{opacity:.25}}
.micro:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.dictee{color:var(--muted);font-style:italic}
/* La barre de pied colle en bas : le bouton se cherchait au fond d'un
   document de six écrans de haut. */
.pied{position:sticky;bottom:0;background:rgba(247,247,245,.96);
  backdrop-filter:blur(6px);border-top:1px solid var(--line);
  margin:0 -24px;padding:14px 24px;display:flex;align-items:center;gap:16px;
  flex-wrap:wrap}
.compte{font-size:13px;color:var(--muted);font-weight:700}
.compte b{color:var(--ink)}
.majour{font:inherit;font-weight:800;font-size:14px;color:#fff;background:var(--accent);
  border:0;border-radius:999px;padding:10px 20px;cursor:pointer}
.majour:disabled{opacity:.5;cursor:progress}
.majour:focus-visible{outline:2px solid var(--ink);outline-offset:2px}
.journal{width:100%;font-family:var(--mono);font-size:12px;color:var(--muted);
  white-space:pre-wrap;margin:0;max-height:150px;overflow:auto}
.gestes{font-family:var(--mono);font-size:11.5px;color:var(--muted);margin-top:8px;
  word-break:break-word}
</style>
</head>
<body>
<div class="wrap">
<h1>Atelier du guide</h1>
<p class="chapeau">Le texte se corrige ici et repart dans <code>manifeste.json</code> — la durée
se recalcule à mesure. La remarque et le croquis, eux, restent à côté : ils disent ce qu'il
faudrait montrer, et le tournage le refera proprement. <b>Rien n'est synthétisé ni enregistré
tant que vous n'en donnez pas le signal.</b></p>
<p class="chapeau dictee">« Dicter » écrit à la fin du champ. La reconnaissance de Chrome passe
par Google — ce sont des textes de tutoriel, jamais des données d'élèves — et elle ne pose
presque pas de ponctuation : dictez, puis relisez. La dictée du système (deux fois la touche
Fn) reste disponible dans n'importe quel champ et, elle, ne sort pas du Mac.</p>
<div id="tout"></div>
<div class="pied">
  <button class="majour" id="majour" type="button">Mettre à jour le storyboard</button>
  <span class="compte" id="compte"></span>
  <pre class="journal" id="journal"></pre>
</div>
</div>
<script>
const $ = (s, r) => (r || document).querySelector(s);
const el = (t, c, x) => { const n = document.createElement(t); if (c) n.className = c;
  if (x !== undefined) n.textContent = x; return n; };
const LEGENDE = { debut: 'au début', fin: 'à la fin' };
/* « après le geste 3 » : le storyboard prend une image après chaque geste, et
   leur nombre change d'un plan à l'autre — pas de table possible. */
const legende = (c) => (c.startsWith('geste') ? 'après le geste ' + c.slice(5)
  : (LEGENDE[c] || c));

/* — La dictée —

   `webkitSpeechRecognition` : Chrome et Safari le portent, et la page est
   servie depuis localhost, ce qui suffit à l'autorisation du micro. Deux
   choses à savoir, et elles sont dites dans le chapeau plutôt que cachées
   ici : la reconnaissance de Chrome **passe par Google** — ce sont des textes
   de tutoriel, pas des données d'élèves, mais ça se sait avant de parler — et
   elle ne pose presque aucune ponctuation. On dicte, on relit, on ponctue.

   Le texte dicté s'ajoute **à la fin** du champ, jamais au curseur : la
   reconnaissance rend des morceaux à retardement, et viser une position qui a
   bougé entre-temps produisait des phrases emboîtées. */
const Reconnaissance = window.SpeechRecognition || window.webkitSpeechRecognition;

function micro(zone, auChangement) {
  if (!Reconnaissance) return null;
  const bouton = el('button', 'micro');
  bouton.type = 'button';
  bouton.appendChild(el('span', 'pastille'));
  const mot = el('span', null, 'Dicter');
  bouton.appendChild(mot);

  let reco = null, base = '', dit = '', voulu = false;
  const poser = (encours) => {
    zone.value = (base ? base.replace(/\s+$/, '') + ' ' : '') + dit + encours;
    auChangement();
  };

  bouton.addEventListener('click', () => {
    if (voulu) { voulu = false; if (reco) reco.stop(); return; }
    voulu = true;
    base = zone.value; dit = '';
    bouton.classList.add('ecoute'); mot.textContent = 'J’écoute — cliquer pour arrêter';
    reco = new Reconnaissance();
    reco.lang = 'fr-CA';
    reco.continuous = true;
    reco.interimResults = true;
    reco.onresult = (e) => {
      let encours = '';
      for (let i = e.resultIndex; i < e.results.length; i += 1) {
        const t = e.results[i][0].transcript;
        if (e.results[i].isFinal) dit += (dit ? ' ' : '') + t.trim();
        else encours += t;
      }
      poser(encours ? (dit ? ' ' : '') + encours : '');
    };
    /* Chrome coupe tout seul après un silence. Tant que le bouton dit
       « j'écoute », on repart — sinon la dictée s'arrête au milieu d'une
       phrase sans que rien ne le signale. */
    reco.onend = () => {
      if (voulu) { try { reco.start(); } catch (e) { /* déjà repartie */ } }
      else { bouton.classList.remove('ecoute'); mot.textContent = 'Dicter'; poser(''); }
    };
    reco.onerror = (e) => {
      voulu = false;
      bouton.classList.remove('ecoute');
      mot.textContent = e.error === 'not-allowed' ? 'Micro refusé' : 'Dicter';
    };
    reco.start();
  });
  return bouton;
}

const poster = (route, corps) => fetch('/api/' + route, {
  method: 'POST', headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(corps) }).then((r) => r.json());

function ligne(capsule, plan) {
  const rang = el('div', 'plan' + (plan.retirer ? ' retire' : ''));
  rang.appendChild(el('div', 'cle', plan.id));

  const gauche = el('div');
  const zone = el('textarea');
  zone.value = plan.texte;
  gauche.appendChild(zone);

  const sous = el('div', 'sous');
  const duree = el('span', 'duree', plan.secondes + ' s');
  const vu = el('span', 'enregistre', 'enregistré');
  const retirer = el('label', 'retirer');
  const case_ = el('input'); case_.type = 'checkbox'; case_.checked = plan.retirer;
  retirer.appendChild(case_); retirer.appendChild(el('span', null, 'retirer ce plan'));
  sous.append(duree, vu, retirer);
  gauche.appendChild(sous);

  if (plan.texteVoix) {
    const dit = el('div', 'gestes', 'dit à la voix : ' + plan.texteVoix);
    gauche.appendChild(dit);
  }
  if (plan.gestes && plan.gestes.length) {
    gauche.appendChild(el('div', 'gestes', 'gestes : ' + JSON.stringify(plan.gestes)));
  }

  gauche.appendChild(el('div', 'etiq', 'Ce qu\'il faudrait changer à l\'écran'));
  const remarque = el('textarea', 'note');
  remarque.placeholder = 'ex. il manque une capture du bouton Enregistrer, en bas de la barre';
  remarque.value = plan.note;
  gauche.appendChild(remarque);

  gauche.appendChild(el('div', 'etiq', 'Commentaire — ce qu\'il faut ajouter'));
  const commentaire = el('textarea', 'commentaire');
  commentaire.placeholder = 'ex. il manque de dire que le groupe se choisit avant tout le reste';
  commentaire.value = plan.commentaire;
  gauche.appendChild(commentaire);

  let minuteur;
  const enregistrerTexte = () => {
    clearTimeout(minuteur);
    minuteur = setTimeout(async () => {
      const r = await poster('texte', { capsule: capsule.id, plan: plan.id, texte: zone.value });
      duree.textContent = r.secondes + ' s';
      vu.classList.add('vu'); setTimeout(() => vu.classList.remove('vu'), 1200);
    }, 500);
  };
  zone.addEventListener('input', enregistrerTexte);
  let m2;
  const enregistrerNote = () => {
    clearTimeout(m2);
    m2 = setTimeout(() => poster('note', { capsule: capsule.id, plan: plan.id,
      note: remarque.value }), 500);
  };
  remarque.addEventListener('input', enregistrerNote);
  let m3;
  const enregistrerCommentaire = () => {
    clearTimeout(m3);
    m3 = setTimeout(() => poster('note', { capsule: capsule.id, plan: plan.id,
      commentaire: commentaire.value }), 500);
  };
  commentaire.addEventListener('input', enregistrerCommentaire);

  const microTexte = micro(zone, enregistrerTexte);
  if (microTexte) sous.insertBefore(microTexte, retirer);
  const microNote = micro(remarque, enregistrerNote);
  if (microNote) {
    const barre = el('div', 'sous');
    barre.appendChild(microNote);
    gauche.insertBefore(barre, commentaire.previousSibling);
  }
  const barreBas = el('div', 'sous');
  const microCom = micro(commentaire, enregistrerCommentaire);
  if (microCom) barreBas.appendChild(microCom);
  const regle = el('label', 'regle');
  const caseRegle = el('input');
  caseRegle.type = 'checkbox'; caseRegle.checked = plan.regle;
  regle.appendChild(caseRegle);
  regle.appendChild(el('span', null, 'réglé'));
  caseRegle.addEventListener('change', () => {
    rang.classList.toggle('fait', caseRegle.checked);
    poster('note', { capsule: capsule.id, plan: plan.id, regle: caseRegle.checked });
  });
  barreBas.appendChild(regle);
  gauche.appendChild(barreBas);
  if (plan.regle) rang.classList.add('fait');
  case_.addEventListener('change', () => {
    rang.classList.toggle('retire', case_.checked);
    poster('note', { capsule: capsule.id, plan: plan.id, retirer: case_.checked });
  });

  const droite = el('div');
  plan.images.forEach((src, i) => {
    const f = el('figure');
    const img = el('img'); img.src = src; img.loading = 'lazy';
    f.appendChild(img);
    f.appendChild(el('figcaption', null, legende(plan.legendes[i])));
    droite.appendChild(f);
  });
  const croquis = el('div');
  const poserCroquis = (src) => {
    const f = el('figure', 'croquis');
    const img = el('img'); img.src = src;
    f.appendChild(img);
    f.appendChild(el('figcaption', null, 'croquis — à refaire au tournage'));
    croquis.appendChild(f);
  };
  (plan.croquis || []).forEach(poserCroquis);
  droite.appendChild(croquis);

  const depot = el('div', 'depot',
    'Collez (⌘V) ou déposez ici une capture de ce qu\'il faudrait montrer');
  const avaler = async (fichier) => {
    const donnees = await new Promise((res) => {
      const l = new FileReader(); l.onload = () => res(l.result); l.readAsDataURL(fichier);
    });
    const r = await poster('croquis', { capsule: capsule.id, plan: plan.id, donnees });
    poserCroquis(r.croquis[r.croquis.length - 1] + '?' + Date.now());
  };
  depot.addEventListener('dragover', (e) => { e.preventDefault(); depot.classList.add('survol'); });
  depot.addEventListener('dragleave', () => depot.classList.remove('survol'));
  depot.addEventListener('drop', (e) => {
    e.preventDefault(); depot.classList.remove('survol');
    const f = e.dataTransfer.files[0]; if (f) avaler(f);
  });
  depot.addEventListener('click', () => depot.focus());
  depot.tabIndex = 0;
  depot.addEventListener('paste', (e) => {
    const it = [...e.clipboardData.items].find((x) => x.type.startsWith('image/'));
    if (it) avaler(it.getAsFile());
  });
  droite.appendChild(depot);

  rang.append(gauche, droite);
  return rang;
}

function compter(etat) {
  let com = 0, rem = 0, croquis = 0, retires = 0;
  for (const c of etat.capsules) for (const p of c.plans) {
    if (p.commentaire && !p.regle) com += 1;
    if (p.note && !p.regle) rem += 1;
    croquis += (p.croquis || []).length;
    if (p.retirer) retires += 1;
  }
  const bouts = [];
  if (com) bouts.push('<b>' + com + '</b> commentaire' + (com > 1 ? 's' : ''));
  if (rem) bouts.push('<b>' + rem + '</b> remarque' + (rem > 1 ? 's' : '') + ' sur l’image');
  if (croquis) bouts.push('<b>' + croquis + '</b> croquis');
  if (retires) bouts.push('<b>' + retires + '</b> plan' + (retires > 1 ? 's' : '') + ' à retirer');
  $('#compte').innerHTML = bouts.length
    ? bouts.join(' · ') + ' en attente'
    : 'rien en attente';
}

$('#majour').addEventListener('click', async () => {
  const b = $('#majour'), j = $('#journal');
  b.disabled = true; b.textContent = 'Mise à jour…';
  j.textContent = 'Le portail de démonstration se lève, les gestes se rejouent.\n'
    + 'Une à deux minutes. Rien n’est synthétisé ni enregistré.';
  try {
    const r = await poster('majour', {});
    j.textContent = r.journal.join('\n');
    if (r.ok) {
      j.textContent += '\n\nNouvelle version prête — la page se recharge.';
      setTimeout(() => location.reload(), 1400);
      return;
    }
  } catch (e) {
    j.textContent = 'échec : ' + e.message;
  }
  b.disabled = false; b.textContent = 'Mettre à jour le storyboard';
});

fetch('/api/etat').then((r) => r.json()).then((etat) => {
  compter(etat);
  const tout = $('#tout');
  for (const capsule of etat.capsules) {
    const bloc = el('div', 'capsule');
    const titre = el('h2');
    titre.appendChild(el('span', 'num', capsule.rang));
    titre.appendChild(el('span', null, capsule.titre));
    bloc.appendChild(titre);
    const total = capsule.plans.reduce((s, p) => s + p.secondes, 0);
    bloc.appendChild(el('p', 'resume',
      capsule.plans.length + ' plans · environ ' + Math.round(total) + ' s'));
    const v = capsule.version || {};
    const bandeau = el('div', 'version');
    bandeau.appendChild(el('span', 'rang', 'Storyboard ' + (v.version || 'v1.0')));
    bandeau.appendChild(el('span', null, v.quand || 'jamais mis à jour'));
    if (v.quoi) bandeau.appendChild(el('span', 'quoi', '— ' + v.quoi));
    if ((v.historique || []).length > 1) {
      const d = document.createElement('details');
      d.appendChild(el('summary', null, 'les versions précédentes'));
      const ol = document.createElement('ol');
      v.historique.slice(1).forEach((h) => ol.appendChild(
        el('li', null, h.version + ' · ' + h.quand + ' — ' + h.quoi)));
      d.appendChild(ol);
      bandeau.appendChild(d);
    }
    bloc.appendChild(bandeau);
    capsule.plans.forEach((p) => bloc.appendChild(ligne(capsule, p)));
    tout.appendChild(bloc);
  }
});
</script>
</body>
</html>
"""


if __name__ == "__main__":
    SEULE = sys.argv[1] if len(sys.argv) > 1 else None
    GUIDE.mkdir(exist_ok=True)
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("127.0.0.1", PORT), Poste) as poste:
        print("Atelier du guide : http://localhost:%d  (Ctrl-C pour arrêter)" % PORT)
        webbrowser.open("http://localhost:%d" % PORT)
        poste.serve_forever()
