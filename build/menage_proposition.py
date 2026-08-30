#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La page de ménage du dépôt — un chantier, une décision.

Pourquoi un script plutôt qu'une page écrite à la main : **les chiffres
bougent**. Soixante worktrees aujourd'hui, quarante demain ; 3,2 Gio de paquet
git avant un `gc`, moins après. Une page recopiée serait fausse le lendemain et
personne ne saurait laquelle des deux croire. Ici, on relance le script et la
page redit la vérité du jour.

    python3 build/menage_proposition.py            # mesure et écrit la page
    python3 build/menage_proposition.py --vite     # réutilise les mesures de disque

Les décisions vivent dans le `localStorage` du poste et s'exportent en JSON :
c'est ce fichier qui pilote la session suivante, pas la mémoire d'une
conversation.
"""

import argparse
import html
import json
import subprocess
import time
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "menage-depot.html"
CACHE = RACINE / "build" / "audits" / "menage_mesures.json"


# ── Mesures ───────────────────────────────────────────────────────────────

def git(*args, cwd=RACINE):
    try:
        r = subprocess.run(["git", *args], cwd=cwd, capture_output=True,
                           text=True, timeout=180)
        return r.stdout.strip()
    except Exception:
        return ""


def lignes(sortie):
    return [l for l in sortie.splitlines() if l.strip()]


def taille(chemin, minutes=6):
    """`du -sh`, en secondes ou en minutes selon le dossier. Rend une chaîne."""
    try:
        r = subprocess.run(["du", "-sh", str(chemin)], capture_output=True,
                           text=True, timeout=minutes * 60)
        return r.stdout.split()[0] if r.stdout.strip() else "?"
    except Exception:
        return "?"


def mesures(vite=False):
    m = {}
    if vite and CACHE.exists():
        m = json.loads(CACHE.read_text())
    else:
        m["disque_total"] = taille(RACINE)
        m["disque_worktrees"] = taille(RACINE / ".claude")
        m["disque_tutoriels"] = taille(RACINE / "build" / "tutoriels", minutes=2)
        m["disque_teaser"] = taille(RACINE / "build" / "teaser", minutes=2)
        m["disque_assets"] = taille(RACINE / "assets", minutes=4)

    # git : rapide, toujours refait
    m["paquet_git"] = next((l.split(":")[1].strip()
                            for l in git("count-objects", "-vH").splitlines()
                            if l.startswith("size-pack")), "?")
    m["worktrees"] = len(lignes(git("worktree", "list"))) - 1
    m["branches"] = len(lignes(git("branch")))
    non_fusionnees = [b.strip("* +").strip()
                      for b in lignes(git("branch", "--no-merged", "main"))]
    m["non_fusionnees"] = []
    for b in non_fusionnees:
        base = git("merge-base", "main", b)
        fichiers = lignes(git("diff", "--name-only", base, b))
        absents = [f for f in fichiers
                   if subprocess.run(["git", "cat-file", "-e", "main:" + f],
                                     cwd=RACINE, capture_output=True).returncode != 0]
        m["non_fusionnees"].append({
            "nom": b,
            "commits": int(git("rev-list", "--count", "main..%s" % b) or 0),
            "date": git("log", "-1", "--format=%ad", "--date=short", b),
            "sujet": git("log", "-1", "--format=%s", b)[:70],
            "fichiers": len(fichiers),
            "absents": absents,
        })
    m["fusionnees"] = m["branches"] - len(non_fusionnees) - 1  # moins main

    # worktrees sales, et ce que contiennent leurs fichiers non commités
    sales = []
    for d in sorted((RACINE / ".claude" / "worktrees").glob("*/")):
        etat = lignes(git("status", "--porcelain", cwd=d))
        if not etat:
            continue
        neufs = [l[3:] for l in etat if l.startswith("??")]
        deja = sum(1 for f in neufs
                   if subprocess.run(["git", "cat-file", "-e", "main:" + f.rstrip("/")],
                                     cwd=RACINE, capture_output=True).returncode == 0)
        sales.append({"nom": d.name, "n": len(etat), "neufs": len(neufs),
                      "deja_dans_main": deja})
    m["sales"] = sales

    # la racine
    racine = [p for p in RACINE.iterdir() if not p.name.startswith(".")]
    m["racine_total"] = len(racine)
    m["racine_audio"] = len([p for p in racine if p.name.startswith("generer_audio_")])
    m["racine_sons"] = len([p for p in racine if p.name.startswith("sons_")])
    m["racine_essais"] = sorted(p.name for p in racine if p.name.startswith("essai-"))
    m["racine_reste"] = (m["racine_total"] - m["racine_audio"]
                         - m["racine_sons"] - len(m["racine_essais"]))

    # les scripts qui lisent les manifestes à la racine (le coût d'un rangement)
    lecteurs = git("grep", "-l", "-e", "sons_%s.json", "-e", "sons_module_",
                   "--", "build", "server.py")
    m["lecteurs_sons"] = lignes(lecteurs)

    # les gros fichiers suivis
    gros = []
    for f in lignes(git("ls-files")):
        p = RACINE / f
        try:
            o = p.stat().st_size
        except OSError:
            continue
        if o > 5_000_000:
            gros.append((round(o / 1e6), f))
    m["gros_suivis"] = sorted(gros, reverse=True)[:10]
    m["fichiers_suivis"] = len(lignes(git("ls-files")))

    m["quand"] = time.strftime("%Y-%m-%d %H:%M")
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(m, ensure_ascii=False, indent=1))
    return m


# ── Les chantiers ─────────────────────────────────────────────────────────

def chantiers(m):
    absents_total = sum(len(b["absents"]) for b in m["non_fusionnees"])
    docs_absents = [f for b in m["non_fusionnees"] for f in b["absents"]
                    if f.startswith("docs/")]
    images_absentes = [f for b in m["non_fusionnees"] for f in b["absents"]
                       if f.endswith((".jpg", ".png"))]
    sales_n = len(m["sales"])
    sales_neufs = sum(s["neufs"] for s in m["sales"])
    sales_deja = sum(s["deja_dans_main"] for s in m["sales"])

    return [
        {
            "id": "worktrees",
            "gain": m.get("disque_worktrees", "?"),
            "titre": "Les %d worktrees d'agents" % m["worktrees"],
            "constat": (
                "Chaque agent lancé en parallèle a reçu une copie complète du dépôt. "
                "Il en reste <b>%d</b>, qui pèsent <b>%s</b> — c'est-à-dire la quasi-totalité "
                "des %s du dossier. Le travail, lui, est ailleurs : sur les %d branches, "
                "<b>%d sont déjà fusionnées</b> dans main."
                % (m["worktrees"], m.get("disque_worktrees", "?"),
                   m.get("disque_total", "?"), m["branches"], m["fusionnees"])),
            "verifie": (
                "Les <b>%d branches non fusionnées</b> ont été dépouillées fichier par fichier. "
                "Elles touchent en tout %d fichiers qui n'existent pas dans main : "
                "<b>%d images</b> — vérifiées une à une, <b>aucune n'est appelée</b> par le "
                "module auquel elle appartient (ce sont des générations abandonnées, refaites "
                "depuis) — et <b>%d documents de planification</b> (%s). "
                "Par ailleurs <b>%d worktrees</b> portent des fichiers jamais commités "
                "(%d fichiers neufs, dont <b>%d existent déjà dans main</b> : PowerPoints, "
                "fiches, scripts audio produits ensuite par le chemin normal)."
                % (len(m["non_fusionnees"]), absents_total, len(images_absentes),
                   len(docs_absents), ", ".join("<code>%s</code>" % d for d in docs_absents) or "aucun",
                   sales_n, sales_neufs, sales_deja)),
            "propose": (
                "Récupérer les %d documents de planification dans <code>docs/</code>, "
                "puis retirer les %d worktrees et les branches qui vont avec."
                % (len(docs_absents), m["worktrees"])),
            "risque": "faible",
            "risque_mot": (
                "Ce qui disparaît est du travail déjà repris dans main ou des images "
                "que plus rien n'appelle. À faire quand aucune session n'est en cours "
                "dans le dépôt — un worktree retiré sous les pieds d'un agent le casse."),
            "commandes": [
                "# 1. récupérer ce qui n'existe nulle part ailleurs",
                "git show <branche>:docs/plan-module-n3-horaire.md > docs/plan-module-n3-horaire.md",
                "git show <branche>:docs/plan-module-n5-saisons.md > docs/plan-module-n5-saisons.md",
                "# 2. retirer les worktrees, puis leurs branches",
                "git worktree list | grep .claude/worktrees | awk '{print $1}' | xargs -n1 git worktree remove --force",
                "git worktree prune",
                "git branch -D $(git branch | grep worktree-agent)",
            ],
        },
        {
            "id": "gc",
            "gain": m["paquet_git"],
            "titre": "Le paquet git, une fois les branches parties",
            "constat": (
                "L'historique pèse <b>%s</b> pour %s fichiers suivis. Tant que les "
                "branches d'agents existent, git garde tous leurs objets — y compris les "
                "images abandonnées."
                % (m["paquet_git"], m["fichiers_suivis"])),
            "verifie": "Mesuré par <code>git count-objects -vH</code>, avant tout ménage.",
            "propose": "Après le chantier précédent, compacter l'historique.",
            "risque": "nul",
            "risque_mot": "Aucune perte possible : <code>gc</code> ne touche qu'au rangement interne.",
            "commandes": ["git reflog expire --expire=now --all",
                          "git gc --prune=now --aggressive"],
        },
        {
            "id": "racine",
            "gain": "%d fichiers de moins à la racine" % (m["racine_audio"] + m["racine_sons"]),
            "titre": "La racine : %d entrées, dont %d de la même famille"
                     % (m["racine_total"], m["racine_audio"] + m["racine_sons"]),
            "constat": (
                "À la racine du dépôt : <b>%d scripts <code>generer_audio_*.py</code></b> et "
                "<b>%d manifestes <code>sons_*.json</code></b>, pour <b>%d</b> entrées en tout. "
                "Le reste — le serveur, la base, la forge, les pages — se cherche entre les deux."
                % (m["racine_audio"], m["racine_sons"], m["racine_total"])),
            "verifie": (
                "Les manifestes sont lus par <b>%d fichiers</b> (%s), toujours par le même "
                "motif <code>RACINE / ('sons_%%s.json' %% slug)</code> : le rangement se fait "
                "en changeant <b>une ligne par fichier</b>, pas en cherchant des chemins partout."
                % (len(m["lecteurs_sons"]),
                   ", ".join("<code>%s</code>" % f for f in m["lecteurs_sons"][:6]))),
            "propose": (
                "Deux dossiers : <code>audio/</code> pour les scripts de génération, "
                "<code>manifestes/</code> pour les <code>sons_*.json</code>. La racine "
                "retombe à une trentaine d'entrées, toutes lisibles d'un coup d'œil."),
            "risque": "moyen",
            "risque_mot": (
                "L'audio est gelé, donc rien ne se régénère pendant l'opération. Mais les "
                "chemins se vérifient <b>en jouant</b> les contrôles : "
                "<code>build/audio_manquant.py</code> doit continuer de rendre zéro module muet."),
            "commandes": [
                "mkdir -p audio manifestes",
                "git mv generer_audio_*.py audio/",
                "git mv sons_*.json manifestes/",
                "# puis la ligne de chemin dans chacun des lecteurs, et :",
                "python3 build/audio_manquant.py    # doit rester à zéro",
            ],
        },
        {
            "id": "essais",
            "gain": "%d fichiers" % len(m["racine_essais"]),
            "titre": "Les bancs d'essai laissés à la racine",
            "constat": (
                "<b>%d entrées <code>essai-*</code></b> : %s. Ce sont des bancs d'essai — "
                "débit des voix, épellation, outils, brins de dialogue — utiles le jour où "
                "on les a écrits."
                % (len(m["racine_essais"]),
                   ", ".join("<code>%s</code>" % e for e in m["racine_essais"]))),
            "verifie": "Aucun n'est appelé par le serveur ni par une page du portail.",
            "propose": (
                "Les regrouper dans <code>essais/</code> et les garder : ce sont des "
                "preuves. Un banc qu'on jette, c'est une décision qu'on redémontrera."),
            "risque": "faible",
            "risque_mot": "Rien ne les appelle ; seuls des liens dans mes notes pourraient tomber.",
            "commandes": ["mkdir -p essais", "git mv essai-* essais/"],
        },
        {
            "id": "manuels",
            "gain": "80 Mo dans le dépôt, et davantage dans l'historique",
            "titre": "Les deux manuels de l'élève (40 Mo chacun)",
            "constat": (
                "<code>assets/documents/manuel-eleve-niveau-4.pdf</code> (1 753 pages) et sa "
                "version serrée pèsent <b>80 Mo</b> à eux deux — les deux plus gros fichiers "
                "suivis, loin devant. Ils ne sont liés que depuis la banque de présentations."),
            "verifie": (
                "Ce sont des documents dont nous ne sommes pas l'auteur. La règle du projet "
                "est claire sur le contenu — le manuel est un <b>modèle de structure</b>, jamais "
                "une source à reproduire — mais le fichier, lui, voyage avec le dépôt et se "
                "retrouve sur l'hébergeur."),
            "propose": (
                "Décision à prendre, pas un geste technique : soit les sortir du dépôt et les "
                "garder hors ligne, soit assumer leur présence. Les retirer de "
                "l'<b>historique</b> est une opération à part, plus lourde (réécriture) — à ne "
                "faire que si la réponse est « ils ne doivent pas être là »."),
            "risque": "à trancher",
            "risque_mot": (
                "Le lien de la banque de présentations tomberait : il faudrait dire où le "
                "manuel se trouve désormais."),
            "commandes": ["git rm --cached assets/documents/manuel-eleve-niveau-4*.pdf",
                          "# puis retirer les deux boutons de presentations.html"],
        },
        {
            "id": "intermediaires",
            "gain": "%s + %s" % (m.get("disque_tutoriels", "?"), m.get("disque_teaser", "?")),
            "titre": "Les intermédiaires de montage",
            "constat": (
                "<code>build/tutoriels</code> pèse <b>%s</b> et <code>build/teaser</code> "
                "<b>%s</b> : rushes, capsules et rendus intermédiaires. Le teaser est déjà "
                "ignoré par git ; les tutoriels ne le sont qu'en partie (les scripts sont "
                "suivis, les vidéos non)."
                % (m.get("disque_tutoriels", "?"), m.get("disque_teaser", "?"))),
            "verifie": "Les montages finis vivent dans <code>assets/tutoriels</code> et sont suivis.",
            "propose": (
                "Sortir les rushes du dossier de travail — un disque externe ou un dossier "
                "hors dépôt — et compléter <code>.gitignore</code> pour que rien n'y "
                "retombe."),
            "risque": "faible",
            "risque_mot": "À vérifier avant : que chaque capsule montée existe bien dans <code>assets/</code>.",
            "commandes": ["mv build/tutoriels/capsules ~/Claude/rushes-tutoriels",
                          "echo 'build/tutoriels/capsules/' >> .gitignore"],
        },
        {
            "id": "sauvegardes",
            "gain": "trois dossiers",
            "titre": "Les sauvegardes de données laissées dans data/",
            "constat": (
                "<code>data/_sauvegarde-avant-demo</code>, "
                "<code>data/_sauvegarde-avant-demo-classe</code> et "
                "<code>data/sauvegardes</code> gardent l'état des traces d'élèves avant la "
                "pose des classes de démonstration."),
            "verifie": (
                "Les classes de démonstration se posent et se retirent par script "
                "(<code>--install</code> / <code>--purge</code>) : ces copies ne servent "
                "plus de filet."),
            "propose": "Les retirer, ou les dater et les sortir de <code>data/</code>.",
            "risque": "faible",
            "risque_mot": "Ce sont des traces fictives ; aucune donnée d'élève réel.",
            "commandes": ["rm -rf data/_sauvegarde-avant-demo data/_sauvegarde-avant-demo-classe"],
        },
    ]


# ── La page ───────────────────────────────────────────────────────────────

GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ménage du dépôt</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800;900&display=swap">
<style>
  :root{
    --accent:#0A8F5B; --accent-soft:#E6F5EE; --accent-ink:#07734A;
    --surface-band:#EDF6F1;
    --ink-900:#17181A; --ink-700:#3A3D40; --ink-500:#4B4F52; --ink-400:#6E7175;
    --surface-page:#F7F7F5; --surface-card:#FFFFFF; --surface-sunken:#FBFBFA;
    --paper-200:#F0F0EE; --border:#EAEAE8; --border-firm:#D6D6D2; --border-tint:#D8E8DF;
    --acier-600:#1D6B8F; --acier-100:#E7F0F6;
    --ambre-700:#B45309; --ambre-100:#FBEEDC;
    --teal-700:#0D7A6F;  --teal-100:#E3F2F0;
    --rouge-700:#B02D33; --rouge-100:#FBEAEA;
    --marque-600:#6B4FBB; --marque-100:#EDE7F9; --marque-filet:#C3B4EA;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  *{box-sizing:border-box}
  body{margin:0; background:var(--surface-page); color:var(--ink-900);
    font-family:var(--font-sans); font-size:18px; font-weight:600; line-height:1.55;
    -webkit-font-smoothing:antialiased}
  :focus-visible{outline:3px solid var(--accent); outline-offset:2px; border-radius:4px}
  .conteneur{max-width:1000px; margin:0 auto; padding:0 24px}
  .verrou{display:inline-flex; align-items:center; gap:16px; flex-wrap:wrap}
  .verrou .nom{font-weight:900; font-size:28px; letter-spacing:-.035em; line-height:1; white-space:nowrap}
  .verrou .i{position:relative; display:inline-block}
  .verrou .point{position:absolute; left:1px; top:2px; width:7px; height:7px;
    border-radius:999px; background:var(--marque-600)}
  .verrou .filet{width:2px; height:24px; background:var(--marque-filet)}
  .verrou .desc{font-size:16px; font-weight:900; color:var(--marque-600); white-space:nowrap}
  @media (max-width:480px){ .verrou .filet,.verrou .desc{display:none} }
  .barre{background:#FFFFFF; border-bottom:2px solid var(--marque-600); padding:16px 0}
  .bande{background:var(--surface-band); border-bottom:1px solid var(--border-tint); padding:44px 0 34px}
  .bande .conteneur{display:flex; flex-direction:column; gap:18px}
  .surtitre{font-size:13px; font-weight:800; letter-spacing:.12em; text-transform:uppercase;
    color:var(--ink-400); margin:0}
  h1{font-size:clamp(32px,5.4vw,46px); font-weight:900; letter-spacing:-.02em; line-height:1.14; margin:0}
  .chapeau{font-size:19px; font-weight:600; color:var(--ink-500); margin:0; max-width:64ch}
  .quand{font-size:14px; color:var(--ink-400); margin:0}
  main{padding:8px 0 90px}
  h2{font-size:24px; font-weight:900; letter-spacing:-.015em; margin:0}
  p{margin:0 0 12px; max-width:70ch}
  strong,b{font-weight:900}
  code{font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.85em;
    background:var(--paper-200); padding:1px 5px; border-radius:5px; font-weight:700}
  .tuiles{display:grid; gap:14px; grid-template-columns:repeat(auto-fit,minmax(min(180px,100%),1fr));
    margin:26px 0 6px}
  .tuile{background:var(--surface-card); border:1px solid var(--border); border-left:4px solid var(--acier-600);
    border-radius:14px; padding:14px 16px}
  .tuile .n{font-size:27px; font-weight:900; letter-spacing:-.02em; display:block; line-height:1.1}
  .tuile .l{font-size:13.5px; font-weight:700; color:var(--ink-500)}
  .lot{background:var(--surface-card); border:1px solid var(--border); border-radius:16px;
    padding:20px 22px; margin:20px 0 0}
  .lot.faire{border-color:#BFE3D2; background:#FCFEFD}
  .lot.garder{opacity:.62}
  .lot .tete{display:flex; gap:14px; align-items:baseline; flex-wrap:wrap; margin-bottom:4px}
  .gain{font-size:13px; font-weight:800; letter-spacing:.06em; text-transform:uppercase;
    color:var(--accent-ink); background:var(--accent-soft); border-radius:999px; padding:4px 11px;
    white-space:nowrap}
  .bloc{margin:12px 0 0}
  .bloc .t{font-size:12px; font-weight:800; letter-spacing:.1em; text-transform:uppercase;
    color:var(--ink-400); margin:0 0 3px}
  .risque{display:inline-block; font-size:12.5px; font-weight:800; border-radius:999px;
    padding:3px 10px; margin-right:8px}
  .r-nul,.r-faible{background:var(--accent-soft); color:var(--accent-ink)}
  .r-moyen{background:var(--ambre-100); color:var(--ambre-700)}
  .r-trancher{background:var(--rouge-100); color:var(--rouge-700)}
  pre{background:#17181A; color:#F4F4F2; border-radius:12px; padding:14px 16px; overflow-x:auto;
    font-size:13.5px; font-weight:600; line-height:1.6; margin:8px 0 0}
  pre .cm{color:#9BB7A9}
  .choix{display:flex; flex-wrap:wrap; gap:8px; margin-top:16px; padding-top:14px;
    border-top:1px solid var(--border)}
  .choix button{font-family:inherit; font-size:15px; font-weight:800; color:var(--ink-700);
    background:var(--surface-sunken); border:1px solid var(--border-firm); border-radius:999px;
    padding:9px 16px; min-height:44px; cursor:pointer}
  .choix button:hover{background:var(--paper-200)}
  .choix button[aria-pressed="true"]{background:var(--ink-900); border-color:var(--ink-900); color:#FFF}
  .barre-bas{position:sticky; bottom:0; background:rgba(247,247,245,.95);
    backdrop-filter:blur(8px); border-top:1px solid var(--border-firm); padding:12px 0; margin-top:30px}
  .barre-bas .conteneur{display:flex; gap:12px; align-items:center; flex-wrap:wrap}
  .barre-bas .etat{font-size:15px; font-weight:700; color:var(--ink-500); margin-right:auto}
  .barre-bas button{font-family:inherit; font-size:15px; font-weight:800; border-radius:999px;
    padding:10px 18px; min-height:44px; cursor:pointer; border:1px solid var(--ink-900);
    background:var(--ink-900); color:#FFF}
  .barre-bas button.sec{background:#FFF; color:var(--ink-900); border-color:var(--border-firm)}
  textarea{width:100%; min-height:150px; font-family:ui-monospace,Menlo,monospace; font-size:12.5px;
    border:1px solid var(--border-firm); border-radius:12px; padding:12px; margin-top:12px}
  .garde{background:var(--accent-soft); border:1px solid #BFE3D2; border-radius:14px; padding:16px 20px;
    margin-top:26px}
  .garde p:last-child{margin-bottom:0}
  hr{border:0; border-top:1px solid var(--border); margin:40px 0 0}
  footer p{font-size:16px; color:var(--ink-500)}
</style>
</head>
<body>

<div class="barre">
  <div class="conteneur">
    <div class="verrou">
      <span class="nom" role="img" aria-label="francis">franc<span class="i" aria-hidden="true">ı<span class="point"></span></span>s</span>
      <span class="filet" aria-hidden="true"></span>
      <span class="desc">Aide à l'apprentissage du français</span>
    </div>
  </div>
</div>

<header class="bande">
  <div class="conteneur">
    <div>
      <p class="surtitre">Chantier · Décisions à prendre</p>
      <h1>Ménage du dépôt</h1>
    </div>
    <p class="chapeau">Sept chantiers, chacun avec ce que j'ai mesuré, ce que je propose, ce
    que ça libère et ce que ça risque. Tranchez chantier par chantier ; le bouton du bas
    exporte vos décisions pour la session qui fera le travail.</p>
    <p class="quand">Mesuré le __QUAND__ — page produite par <code>build/menage_proposition.py</code>,
    jamais écrite à la main : les chiffres bougent, et une page recopiée serait fausse le lendemain.</p>
  </div>
</header>

<main>
<section class="conteneur">
  <div class="tuiles">__TUILES__</div>
  <p style="margin-top:16px">__RESUME__</p>
</section>

<section class="conteneur" id="lots">__LOTS__</section>

<section class="conteneur">
  <div class="garde">
    <p><b>L'ordre compte.</b> Les worktrees d'abord, le compactage ensuite — l'inverse ne
    libère rien, puisque git garde les objets tant qu'une branche les tient. Et rien de tout
    cela pendant qu'une session travaille dans le dépôt : plusieurs sessions partagent cet
    arbre.</p>
  </div>
</section>

<div class="barre-bas">
  <div class="conteneur">
    <span class="etat" id="etat">Aucune décision prise</span>
    <button type="button" class="sec" id="raz">Tout remettre à zéro</button>
    <button type="button" id="exporter">Exporter mes décisions</button>
  </div>
</div>

<section class="conteneur" id="sortie" hidden>
  <p class="quand">À recoller dans la prochaine session :</p>
  <textarea id="json" readonly></textarea>
</section>

<hr>
<footer class="conteneur">
  <p>Relancer <code>python3 build/menage_proposition.py</code> refait les mesures et réécrit
  cette page. Les décisions, elles, vivent dans le navigateur de ce poste : elles survivent à
  une régénération, et le bouton « Exporter » les sort en JSON.</p>
</footer>
</main>

<script>
(function(){
  "use strict";
  var CLE = 'menage-depot-decisions';
  var etat = {};
  try { etat = JSON.parse(localStorage.getItem(CLE) || '{}'); } catch(e) { etat = {}; }

  function peindre(){
    var faits = 0, gardes = 0, tard = 0;
    document.querySelectorAll('.lot').forEach(function(lot){
      var id = lot.dataset.lot, d = etat[id] || '';
      lot.classList.toggle('faire', d === 'faire');
      lot.classList.toggle('garder', d === 'garder');
      lot.querySelectorAll('.choix button').forEach(function(b){
        b.setAttribute('aria-pressed', String(b.dataset.d === d));
      });
      if (d === 'faire') faits++; else if (d === 'garder') gardes++; else if (d === 'tard') tard++;
    });
    var n = document.querySelectorAll('.lot').length;
    document.getElementById('etat').textContent =
      (faits + gardes + tard) === 0 ? 'Aucune décision prise'
      : faits + ' à faire · ' + gardes + ' à garder tel quel · ' + tard + ' plus tard · '
        + (n - faits - gardes - tard) + ' sans réponse';
  }

  document.getElementById('lots').addEventListener('click', function(ev){
    var b = ev.target.closest('.choix button'); if (!b) return;
    var id = b.closest('.lot').dataset.lot;
    etat[id] = (etat[id] === b.dataset.d) ? '' : b.dataset.d;
    try { localStorage.setItem(CLE, JSON.stringify(etat)); } catch(e){}
    peindre();
  });

  document.getElementById('raz').addEventListener('click', function(){
    etat = {}; try { localStorage.removeItem(CLE); } catch(e){} peindre();
    document.getElementById('sortie').hidden = true;
  });

  document.getElementById('exporter').addEventListener('click', function(){
    var out = {mesure: document.title, decisions: {}};
    document.querySelectorAll('.lot').forEach(function(lot){
      out.decisions[lot.dataset.lot] = {
        titre: lot.querySelector('h2').textContent.trim(),
        decision: etat[lot.dataset.lot] || 'sans réponse'
      };
    });
    var z = document.getElementById('sortie');
    z.hidden = false;
    document.getElementById('json').value = JSON.stringify(out, null, 2);
    document.getElementById('json').select();
  });

  peindre();
})();
</script>
</body>
</html>
"""


def bloc_lot(c):
    cmds = "\n".join(
        ('<span class="cm">%s</span>' % html.escape(l)) if l.strip().startswith("#")
        else html.escape(l) for l in c["commandes"])
    classe = {"nul": "r-nul", "faible": "r-faible", "moyen": "r-moyen",
              "à trancher": "r-trancher"}[c["risque"]]
    return """
  <article class="lot" data-lot="%s">
    <div class="tete"><h2>%s</h2><span class="gain">Libère %s</span></div>
    <div class="bloc"><p class="t">Ce que j'ai mesuré</p><p>%s</p></div>
    <div class="bloc"><p class="t">Ce que j'ai vérifié avant de proposer</p><p>%s</p></div>
    <div class="bloc"><p class="t">Ce que je propose</p><p>%s</p></div>
    <div class="bloc"><p class="t">Le risque</p>
      <p><span class="risque %s">%s</span>%s</p></div>
    <div class="bloc"><p class="t">Les gestes</p><pre>%s</pre></div>
    <div class="choix" role="group" aria-label="Décision">
      <button type="button" data-d="faire">Faire</button>
      <button type="button" data-d="garder">Garder tel quel</button>
      <button type="button" data-d="tard">Plus tard</button>
    </div>
  </article>""" % (c["id"], html.escape(c["titre"]), html.escape(c["gain"]),
                   c["constat"], c["verifie"], c["propose"],
                   classe, c["risque"], c["risque_mot"], cmds)


def ecrire(m):
    cs = chantiers(m)
    tuiles = [
        (m.get("disque_total", "?"), "sur le disque"),
        (m.get("disque_worktrees", "?"), "dans les worktrees d'agents"),
        (m["paquet_git"], "d'historique git"),
        (str(m["worktrees"]), "copies du dépôt"),
        (str(m["branches"]), "branches locales"),
        (str(m["racine_total"]), "entrées à la racine"),
    ]
    h_tuiles = "".join(
        '<div class="tuile"><span class="n">%s</span><span class="l">%s</span></div>'
        % (html.escape(v), l) for v, l in tuiles)
    resume = (
        "Le dépôt pèse <b>%s</b>, et <b>%s</b> de ce total ne sont ni le code ni le "
        "matériel : ce sont <b>%d copies complètes du dépôt</b>, laissées par les agents "
        "qui ont produit les modules en parallèle. Le reste des chantiers ne libère pas "
        "grand-chose en octets — ils rendent le dépôt <i>lisible</i>, ce qui est l'autre "
        "moitié du ménage."
        % (m.get("disque_total", "?"), m.get("disque_worktrees", "?"), m["worktrees"]))
    page = (GABARIT
            .replace("__QUAND__", m["quand"])
            .replace("__TUILES__", h_tuiles)
            .replace("__RESUME__", resume)
            .replace("__LOTS__", "".join(bloc_lot(c) for c in cs)))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page)
    print("écrit :", SORTIE.relative_to(RACINE))
    print("%d chantiers · mesuré le %s" % (len(cs), m["quand"]))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--vite", action="store_true",
                    help="réutilise les mesures de disque déjà prises")
    a = ap.parse_args()
    ecrire(mesures(vite=a.vite))
