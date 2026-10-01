#!/usr/bin/env python3
"""La page des compétences : tout ce que Claude sait faire sur demande, au même endroit.

    python3 build/competences_page.py   # écrit assets/presentations/atelier/competences.html

Demandée par Daniel le 30 septembre 2026 (« une page avec tous les skills
disponibles »). Une compétence s'appelle par son nom (/francis) ou se déclenche
d'elle-même quand la demande lui correspond — encore faut-il savoir qu'elle
existe.

Trois sources, lues dans cet ordre :
  1. NOS compétences — ~/.claude/skills/*/SKILL.md, lues SUR LE DISQUE à chaque
     construction : une compétence écrite demain paraît au prochain passage,
     rangée sous « Autres » tant que FAMILLES ne la classe pas.
  2. Les extensions installées — ~/.claude/plugins/installed_plugins.json, puis
     les SKILL.md du dossier de chaque extension.
  3. Celles du compte claude.ai et celles intégrées à Claude Code — elles ne
     sont pas sur le disque ; leur liste est écrite ici (COMPTE, INTEGREES), à
     tenir à jour quand la liste de la session change.

Relancer après avoir écrit, installé ou retiré une compétence.
"""
import datetime
import html
import json
import pathlib
import re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "atelier" / "competences.html"
MAISON = pathlib.Path.home() / ".claude"

# Famille de chacune de NOS compétences. Une compétence absente d'ici va dans « Autres ».
FAMILLES = [
    ("francisation", "Francisation", "Les modules et le matériel de bibliotheque-francisation.",
     ["module-neuf", "module-parite", "module-sur-mesure"]),
    ("formations", "Formations et pièces", "Les trousses de métier, les pièces d'apprentissage et leur audit.",
     ["trousse-de-metier", "trousse-vente-detail", "piece-apprentissage", "boucle-didactique", "page-engendree"]),
    ("design", "Design et écriture", "Les deux systèmes, le ton, le réglage au curseur et l'audit visuel.",
     ["francis", "boucledidactique", "trame", "ton-francis", "tweak", "impeccable"]),
    ("medias", "Images, voix et séquences", "Ce qui se génère : images, vidéos, voix de personnages, suites de croquis.",
     ["generate", "croquis-sequence", "voix-jouee"]),
    ("session", "Conduite du travail", "Fermer une séance proprement.",
     ["session-handoff"]),
]
# Une phrase en français par compétence. La description d'origine, souvent longue
# ou en anglais, reste dépliable sous « Quand elle se déclenche ». Sans résumé
# ici, la première phrase de la description en tient lieu.
RESUMES = {
    "module-neuf": "Produire un module de francisation neuf à partir du programme et de rien d'autre.",
    "module-parite": "Mettre à niveau un module qui existe déjà : contenu original, mini-leçons, aide, audio.",
    "module-sur-mesure": "Bâtir un module et ses imprimés à partir des documents fournis par l'enseignant.",
    "trousse-de-metier": "La méthode d'une trousse de français pour un métier, de la demande jusqu'au pilote.",
    "trousse-vente-detail": "Le détail propre au commerce de détail : planches de croquis, exercices, jeu de rôle en magasin.",
    "piece-apprentissage": "Concevoir une formation courte en dessins narrés, qui finit par une partie jouée.",
    "boucle-didactique": "Auditer une formation sur 23 critères, réviser, réauditer jusqu'à zéro constat majeur.",
    "page-engendree": "Modifier une page autonome produite par gabarit, sans jamais toucher au HTML produit.",
    "francis": "Appliquer le système de design francis : jetons, logotype, téléphone, pièges payés.",
    "trame": "Abandonné le 1er oct. 2026, remplacé par boucledidactique.",
    "boucledidactique": "Appliquer le système de la maison : graphite et bleu, le logo du quart de tour, le mouvement.",
    "ton-francis": "Écrire dans la voix du projet, selon qui lit ; apprend de chaque correction.",
    "tweak": "Régler une page au curseur, puis figer un bloc CSS à reporter dans la source.",
    "impeccable": "Auditer et critiquer une interface (accessibilité, mise en page, typographie) ; le système l'emporte.",
    "generate": "Générer des images et des vidéos par les modèles d'IA.",
    "croquis-sequence": "Produire ou combler une suite de croquis qui tiennent ensemble d'une image à l'autre.",
    "voix-jouee": "Donner sa voix à un personnage : audition, synthèse, contrôle des tirages.",
    "session-handoff": "Fermer une séance par un bilan qui permet à une autre de reprendre sans rien perdre.",
    "figma:figma-use": "Agir dans un fichier Figma (préalable obligatoire à toute écriture).",
    "figma:figma-create-new-file": "Créer un fichier Figma, FigJam ou Slides vierge.",
    "figma:figma-generate-design": "Construire un écran ou une page dans Figma à partir du code.",
    "figma:figma-generate-library": "Bâtir un système de design dans Figma : variables, composants, thèmes.",
    "figma:figma-generate-diagram": "Dessiner un schéma dans FigJam (organigramme, séquence, architecture).",
    "figma:figma-code-connect": "Relier les composants Figma aux composants du code.",
    "figma:figma-swiftui": "Passer de Figma à SwiftUI, et l'inverse.",
    "figma:figma-use-figjam": "Agir dans un tableau FigJam.",
    "figma:figma-use-slides": "Agir dans une présentation Figma Slides.",
}
TIERCES = {"impeccable": "Tierce · installée par Daniel le 30 sept. 2026, sans son lanceur"}

# Pas sur le disque : la liste de la session, résumée en français.
COMPTE = [
    ("anthropic-skills:docs", "Documents Claude modifiables et partageables (rapport, guide, lettre)."),
    ("anthropic-skills:docx", "Fichiers Word (.docx) : créer, lire, modifier, suivi des modifications."),
    ("anthropic-skills:pptx", "Fichiers PowerPoint (.pptx) : créer, lire, modifier."),
    ("anthropic-skills:xlsx", "Feuilles de calcul (.xlsx, .csv) : créer, nettoyer, convertir."),
    ("anthropic-skills:pdf", "PDF : lire, fusionner, découper, remplir, reconnaître le texte."),
    ("anthropic-skills:google-workspace", "Modifier un fichier Google Docs, Sheets ou Slides."),
    ("anthropic-skills:skill-creator", "Écrire, améliorer et mesurer une compétence."),
    ("anthropic-skills:consolidate-memory", "Faire le ménage de la mémoire : doublons, faits périmés, index."),
    ("anthropic-skills:import-memory", "Importer la mémoire d'un autre assistant."),
    ("anthropic-skills:schedule", "Créer une tâche qui revient (chaque matin, dans une heure)."),
    ("anthropic-skills:morning", "Le bilan du matin en page HTML."),
    ("anthropic-skills:explain-usage", "Où sont allés les jetons de la séance, en un graphique."),
    ("anthropic-skills:audit-design-system", "Auditer un écran Figma contre son système de design."),
    ("anthropic-skills:setup-claude", "Installation guidée : extensions, connecteurs, premier essai."),
]
INTEGREES = [
    ("code-review", "Relire un changement ou une PR pour trouver les bogues."),
    ("simplify", "Nettoyer le code changé : réemploi, simplification, efficacité."),
    ("security-review", "Revue de sécurité des changements en cours."),
    ("run", "Lancer l'application et voir le changement fonctionner."),
    ("init", "Écrire un CLAUDE.md pour un dépôt."),
    ("loop", "Répéter une commande à intervalle (surveiller, relancer)."),
    ("schedule", "Agents planifiés dans le nuage (cron)."),
    ("claude-api", "Référence de l'API Claude : modèles, prix, cache, outils."),
    ("dataviz", "Graphiques et tableaux de bord cohérents, clairs et accessibles."),
    ("artifact-design", "Règles de mise en page d'une page publiée (Artifact)."),
    ("artifact-diagramming", "Schémas en SVG dans une page publiée."),
    ("artifact-capabilities", "Ce qu'une page publiée peut faire : données, partage, fichiers."),
    ("workflow-authoring", "Écrire un enchaînement de plusieurs agents."),
    ("update-config", "Réglages de Claude Code : permissions, crochets, variables."),
    ("fewer-permission-prompts", "Moins de demandes d'autorisation, d'après l'historique."),
    ("keybindings-help", "Raccourcis clavier de Claude Code."),
]


def lire_skill(chemin):
    t = chemin.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = m.group(1) if m else ""
    nom = re.search(r"^name:\s*(.+)$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    return {
        "nom": (nom.group(1).strip() if nom else chemin.parent.name).strip('"'),
        "desc": (desc.group(1).strip().strip('"') if desc else ""),
        "date": datetime.date.fromtimestamp(chemin.stat().st_mtime),
        "dossier": str(chemin.parent).replace(str(pathlib.Path.home()), "~"),
    }


def coupe(desc):
    """La première phrase dit ce que fait la compétence ; le reste, quand elle se déclenche."""
    m = re.search(r"(?<=[.!?])\s+(?=[A-ZÀ-Ý«])", desc)
    return (desc[:m.start()], desc[m.end():]) if m and m.start() < 600 else (desc, "")


def nos_competences():
    return {s["nom"]: s for s in (lire_skill(p) for p in sorted((MAISON / "skills").glob("*/SKILL.md")))}


def extensions():
    try:
        inst = json.loads((MAISON / "plugins" / "installed_plugins.json").read_text(encoding="utf-8"))["plugins"]
    except (OSError, ValueError, KeyError):
        return []
    out = []
    for cle, poses in sorted(inst.items()):
        for pose in poses:
            racine = pathlib.Path(pose["installPath"])
            nom_ext = cle.split("@")[0]
            for p in sorted(racine.glob("skills/*/SKILL.md")):
                s = lire_skill(p)
                s["nom"] = "%s:%s" % (nom_ext, s["nom"])
                s["ext"] = "%s %s" % (nom_ext, pose.get("version", ""))
                out.append(s)
    return out


MOIS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juill.", "août", "sept.", "oct.", "nov.", "déc."]


def date_fr(d):
    return "%d %s %d" % (d.day, MOIS[d.month - 1], d.year)


def carte(s, origine, etiquette=None):
    e = html.escape
    quoi, quand = coupe(s["desc"])
    if s["nom"] in RESUMES:
        quoi, quand = RESUMES[s["nom"]], s["desc"]
    cle = e((s["nom"] + " " + s["desc"]).lower())
    detail = ('<details><summary>Quand elle se déclenche</summary><p>%s</p></details>' % e(quand)) if quand else ""
    meta = []
    if s.get("dossier"):
        meta.append('<span class="ou">%s</span>' % e(s["dossier"]))
    if s.get("date"):
        meta.append('<span>modifiée le %s</span>' % date_fr(s["date"]))
    eti = '<span class="eti eti-%s">%s</span>' % (origine, e(etiquette)) if etiquette else ""
    return ('<article class="c" data-cle="%s"><div class="tete"><code>/%s</code>%s</div>'
            '<p class="quoi">%s</p>%s<div class="meta">%s</div></article>'
            % (cle, e(s["nom"]), eti, e(quoi), detail, " · ".join(meta)))


def section(cle, titre, chapeau, cartes):
    return ('<section class="fam" id="%s"><h2>%s <span class="n">%d</span></h2><p class="chap">%s</p>'
            '<div class="grille">%s</div></section>' % (cle, html.escape(titre), len(cartes), html.escape(chapeau), "".join(cartes)))


def main():
    nos = nos_competences()
    rangees, blocs = set(), []
    for cle, titre, chap, noms in FAMILLES:
        cartes = []
        for n in noms:
            if n in nos:
                rangees.add(n)
                cartes.append(carte(nos[n], "tierce" if n in TIERCES else "nous", TIERCES.get(n)))
        if cartes:
            blocs.append(section(cle, titre, chap, cartes))
    reste = [carte(nos[n], "nous") for n in sorted(nos) if n not in rangees]
    if reste:
        blocs.append(section("autres", "Autres", "Écrites depuis la dernière mise en ordre : à ranger dans FAMILLES.", reste))
    n_nos = len(nos)
    ext = extensions()
    if ext:
        blocs.append(section("extensions", "Extensions installées",
                             "Fournies avec une extension ; elles se mettent à jour avec elle.",
                             [carte(s, "ext", s["ext"]) for s in ext]))
    blocs.append(section("compte", "Compte claude.ai",
                         "Offertes par le compte ; elles suivent partout où l'on se connecte.",
                         [carte({"nom": n, "desc": d}, "ext") for n, d in COMPTE]))
    blocs.append(section("integrees", "Intégrées à Claude Code",
                         "Livrées avec Claude Code lui-même.",
                         [carte({"nom": n, "desc": d}, "ext") for n, d in INTEGREES]))
    total = n_nos + len(ext) + len(COMPTE) + len(INTEGREES)
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(GABARIT % {
        "blocs": "\n".join(blocs), "total": total, "nos": n_nos,
        "date": date_fr(datetime.date.today()),
    }, encoding="utf-8")
    print("Écrit : %s (%d compétences, dont %d à nous)" % (SORTIE.relative_to(RACINE), total, n_nos))


GABARIT = r"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Compétences de Claude</title>
<style>
@font-face{font-family:"Nunito";src:url("../../design-system/fonts/nunito-latin.woff2") format("woff2");font-weight:200 1000;font-display:swap}
:root{--paper:#F7F7F5;--card:#fff;--ink:#17181A;--ink-2:#4A4D52;--line:#E4E3DE;--accent:#0A8F5B;--accent-bg:#E7F4EE;
      --ambre:#9A5B00;--ambre-bg:#FBF1E0;--gris:#6B6E73;--gris-bg:#EFEFEC}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%%}
body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.55 "Nunito",system-ui,-apple-system,"Segoe UI",sans-serif}
.cadre{max-width:1080px;margin:0 auto;padding:32px 16px 96px}
.sur{font-weight:800;font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--gris)}
h1{font-size:34px;line-height:1.15;margin:6px 0 12px;font-weight:900;letter-spacing:-.01em}
.chapeau{font-size:18px;color:var(--ink-2);max-width:66ch;margin:0 0 20px}
.mode{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--accent);border-radius:12px;padding:14px 18px;margin:0 0 20px}
.mode p{margin:4px 0}
.barre{position:sticky;top:0;z-index:5;background:var(--paper);padding:12px 0;border-bottom:1px solid var(--line);margin-bottom:8px;display:flex;flex-wrap:wrap;gap:12px;align-items:center}
.barre input{flex:1 1 260px;min-height:44px;font:inherit;font-size:16px;padding:0 14px;border:1px solid var(--line);border-radius:10px;background:var(--card);color:var(--ink)}
.barre nav{display:flex;flex-wrap:wrap;gap:8px}
.barre a{font-size:14px;font-weight:700;color:var(--ink);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:8px 12px;background:var(--card);min-height:44px;display:inline-flex;align-items:center}
.cpt{font-size:14px;color:var(--ink-2);font-variant-numeric:tabular-nums}
input:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--accent);outline-offset:2px}
.fam{margin-top:28px}
.fam h2{font-size:22px;margin:0 0 2px;font-weight:900}
.fam h2 .n{font-size:14px;color:var(--gris);font-weight:800;margin-left:6px}
.chap{color:var(--ink-2);margin:0 0 12px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:12px}
.c{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px;display:flex;flex-direction:column}
.c[hidden],.fam[hidden]{display:none}
.tete{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.tete code{font:800 16px/1.3 ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--ink);word-break:break-all}
.eti{font-size:12px;font-weight:800;padding:2px 9px;border-radius:999px}
.eti-tierce{color:var(--ambre);background:var(--ambre-bg)}
.eti-ext{color:var(--gris);background:var(--gris-bg)}
.quoi{margin:8px 0 6px}
details{font-size:15px;color:var(--ink-2)}
summary{cursor:pointer;font-weight:700;color:var(--ink);min-height:32px;display:flex;align-items:center}
details p{margin:4px 0 0}
.meta{margin-top:auto;padding-top:8px;font-size:13px;color:var(--gris)}
.ou{font-family:ui-monospace,Menlo,monospace}
.vide{display:none;color:var(--ink-2);margin-top:24px}
.source{font-size:14px;color:var(--gris);margin-top:40px}
@media (max-width:640px){h1{font-size:28px}.grille{grid-template-columns:1fr}}
@media print{.barre{display:none}.c{break-inside:avoid}}
</style></head>
<body><div class="cadre">
<div class="sur">La maison · L'atelier</div>
<h1>Les compétences de Claude</h1>
<p class="chapeau">%(total)d compétences disponibles, dont %(nos)d écrites pour nos projets. Une compétence est une méthode rangée : Claude la charge et la suit au lieu d'improviser.</p>
<div class="mode">
  <p><b>Deux façons de s'en servir.</b> Taper <code>/nom</code> dans Claude Code pour l'appeler, ou simplement décrire la tâche : la compétence qui correspond se déclenche d'elle-même.</p>
  <p>« Quand elle se déclenche » dit les mots et les situations qui la font partir.</p>
</div>
<div class="barre">
  <input type="search" id="q" placeholder="Chercher : voix, module, icône, PowerPoint…" aria-label="Chercher une compétence">
  <nav aria-label="Familles"><a href="#francisation">Francisation</a><a href="#formations">Formations</a><a href="#design">Design</a><a href="#medias">Médias</a><a href="#compte">Compte</a><a href="#integrees">Intégrées</a></nav>
  <span class="cpt" id="cpt"></span>
</div>
<main>
%(blocs)s
</main>
<p class="vide" id="vide">Aucune compétence ne correspond à cette recherche.</p>
<p class="source">Page engendrée le %(date)s par build/competences_page.py, qui relit ~/.claude/skills et les extensions installées. La relancer après avoir écrit, installé ou retiré une compétence.</p>
</div>
<script>
(function(){
  var q=document.getElementById("q"), cartes=[].slice.call(document.querySelectorAll(".c")), fams=[].slice.call(document.querySelectorAll(".fam"));
  function plat(t){return t.normalize("NFD").replace(/[̀-ͯ]/g,"").toLowerCase()}
  cartes.forEach(function(c){c._k=plat(c.dataset.cle)});
  function filtrer(){
    var mots=plat(q.value).split(/\s+/).filter(Boolean), n=0;
    cartes.forEach(function(c){var ok=mots.every(function(m){return c._k.indexOf(m)>=0}); c.hidden=!ok; if(ok)n++;});
    fams.forEach(function(f){f.hidden=!f.querySelector(".c:not([hidden])")});
    document.getElementById("cpt").textContent=n+" / "+cartes.length;
    document.getElementById("vide").style.display=n?"none":"block";
  }
  q.addEventListener("input",filtrer); filtrer();
})();
</script>
</body></html>
"""

if __name__ == "__main__":
    main()
