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
· **une remarque** — « il manque une capture ici », « on ne voit pas le
  bouton » — gardée à côté du manifeste, jamais dedans : le manifeste décrit
  le film, pas la conversation qu'on a eue dessus ;
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
import pathlib
import re
import socketserver
import sys
import webbrowser

ICI = pathlib.Path(__file__).resolve().parent
GUIDE = ICI / "guide"
MANIFESTE = ICI / "manifeste.json"
NOTES = GUIDE / "notes.json"
PORT = 5322

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
                "retirer": n.get(cle, {}).get("retirer", False),
                "croquis": n.get(cle, {}).get("croquis", []),
            })
        capsules.append({"id": capsule["id"], "rang": rang,
                         "titre": capsule["titre"], "plans": plans})
    return {"capsules": capsules}


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
            for champ in ("note", "retirer"):
                if champ in corps:
                    fiche[champ] = corps[champ]
            NOTES.write_text(json.dumps(n, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            self._rendre({"ok": True})
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
.resume{margin:0 0 18px;color:var(--muted);font-size:13px;font-weight:800;
  letter-spacing:.05em;text-transform:uppercase}
.plan{display:grid;grid-template-columns:44px minmax(0,1fr) minmax(0,1fr);gap:18px;
  padding:18px 0;border-top:1px solid var(--line)}
.plan.retire{opacity:.42}
.cle{font-family:var(--mono);font-size:13px;color:var(--muted);font-weight:700;padding-top:8px}
textarea{width:100%;min-height:120px;resize:vertical;font:inherit;color:var(--ink);
  background:#FCFCFB;border:1px solid var(--line);border-radius:9px;padding:11px 12px}
textarea:focus{outline:2px solid var(--accent);outline-offset:1px;background:#fff}
.note{min-height:60px;background:var(--ambre-fond);border-color:#E8D3A0;color:#4A3706}
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
</div>
<script>
const $ = (s, r) => (r || document).querySelector(s);
const el = (t, c, x) => { const n = document.createElement(t); if (c) n.className = c;
  if (x !== undefined) n.textContent = x; return n; };
const LEGENDE = { debut: 'au début', milieu: 'en cours', fin: 'à la fin' };

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

  const microTexte = micro(zone, enregistrerTexte);
  if (microTexte) sous.insertBefore(microTexte, retirer);
  const microNote = micro(remarque, enregistrerNote);
  if (microNote) {
    const barre = el('div', 'sous');
    barre.appendChild(microNote);
    gauche.appendChild(barre);
  }
  case_.addEventListener('change', () => {
    rang.classList.toggle('retire', case_.checked);
    poster('note', { capsule: capsule.id, plan: plan.id, retirer: case_.checked });
  });

  const droite = el('div');
  plan.images.forEach((src, i) => {
    const f = el('figure');
    const img = el('img'); img.src = src; img.loading = 'lazy';
    f.appendChild(img);
    f.appendChild(el('figcaption', null, LEGENDE[plan.legendes[i]] || plan.legendes[i]));
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

fetch('/api/etat').then((r) => r.json()).then((etat) => {
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
