#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""La trousse de présentation — tout ce qu'on ouvre pendant une rencontre.

« Trousse » et non « kit » : c'est le mot que le projet emploie, comme il écrit
« courriel ». Elle sert à une seule chose — ne pas chercher un document devant
une direction pendant que douze personnes regardent l'écran.

La page tient trois choses : **le déroulé** (quel document à quelle minute),
**les chiffres** qu'on doit pouvoir dire sans les lire, et **les questions qui
reviennent** avec leur réponse courte. Les chiffres sont comptés sur le dépôt,
jamais recopiés : c'est le seul moyen qu'ils soient encore vrais dans un mois.

    python3 build/trousse.py
"""

import collections
import html
import json
import pathlib
import re
import time
import zipfile

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "trousse-presentation.html"

MOIS = {"January": "janvier", "February": "février", "March": "mars", "April": "avril",
        "May": "mai", "June": "juin", "July": "juillet", "August": "août",
        "September": "septembre", "October": "octobre", "November": "novembre",
        "December": "décembre"}


def nb(v):
    return "{:,}".format(v).replace(",", " ") if isinstance(v, int) else str(v)


def mesures():
    m = {}
    quand = time.strftime("%-d %B %Y")
    for en, fr in MOIS.items():
        quand = quand.replace(en, fr)
    m["quand"] = quand

    acts = json.loads((RACINE / "data" / "activities.json").read_text())
    cat = collections.Counter(a.get("categorie") for a in acts)
    m["activites"] = len(acts)
    m["cours"] = cat.get("cours", 0)
    m["ateliers"] = cat.get("atelier", 0)
    m["niveaux"] = len({a.get("level") for a in acts if a.get("level")})

    docs = list((RACINE / "assets" / "documents").glob("*.html"))
    m["fiches"] = len([p for p in docs if re.search(r"-[a-e][1-5]-", p.name)])

    decks = list((RACINE / "assets" / "powerpoints").rglob("*.pptx"))
    m["decks"] = len(decks)
    diapos = 0
    for d in decks:
        try:
            with zipfile.ZipFile(d) as z:
                diapos += len([n for n in z.namelist()
                               if re.match(r"ppt/slides/slide\d+\.xml$", n)])
        except Exception:
            pass
    m["diapos"] = diapos

    minutes, notes = 0, 0
    for p in (RACINE / "build" / "powerpoints" / "decks").rglob("*.py"):
        t = p.read_text(errors="ignore")
        d = re.search(r"duree='(\d+)", t)
        if d:
            minutes += int(d.group(1))
        notes += len(re.findall(r"notes=", t))
    m["heures"] = round(minutes / 60)
    m["notes"] = notes

    # Le plafond d'une séance se lit dans le serveur : l'écrire ici en dur, ce
    # serait promettre quarante appareils le jour où il en accepte trente.
    srv = (RACINE / "server.py").read_text(errors="ignore")
    mm = re.search(r"SEANCE_PLAFOND_DEFAUT\s*=\s*(\d+)", srv)
    m["plafond"] = int(mm.group(1)) if mm else 40

    m["mp3"] = len(list((RACINE / "assets" / "interactive").rglob("*.mp3")))
    m["images"] = sum(len(list((RACINE / "assets" / "interactive").rglob(e)))
                      for e in ("*.jpg", "*.png", "*.webp"))
    m["modules_interactifs"] = len([d for d in (RACINE / "assets" / "interactive").iterdir()
                                    if d.is_dir()])
    return m


# ── Le contenu éditorial ──────────────────────────────────────────────────

# ── Ce qu'il y a dans la trousse ─────────────────────────────────────
# Une ligne par document, et **trois formes possibles** : la page qu'on ouvre
# dans un onglet, le diaporama qu'on projette, la feuille qu'on laisse sur la
# table. Le premier jet de cette page rangeait les documents par forme — les
# PPTX dans une section, les PDF dans une autre, les pages dans le déroulé :
# le même document paraissait à trois endroits et nulle part en entier, et on
# ne pouvait pas savoir d'un coup d'œil ce qui existait.
#
# Les cases se remplissent **en regardant le disque** (`formes()`), jamais de
# mémoire : une case qui annonce un fichier absent est pire qu'une case vide,
# parce qu'on ne s'en aperçoit que devant la salle.
TROUSSE = [
    ("Le déroulé de la rencontre",
     "Vingt minutes, sept temps, et la question par laquelle on finit.",
     "trousse-presentation", None),
    ("Le point express",
     "La version courte, quand on a dix minutes dans un corridor.",
     "point-express", "P4"),
    ("La logique pédagogique",
     "Sur quoi le cours est bâti : le contenu, l'ordre, ce que la machine refuse.",
     None, "F1"),
    ("Ce qu'il y a dans la boîte",
     "Le matériel, en chiffres et en structure. Le premier temps du pitch.",
     None, "P1"),
    ("Ce que la direction décide",
     "Les quatre interrupteurs, et ce que chacun change à l'écran.",
     "bac-a-sable-cas-de-figure", "P2"),
    ("Les questions de conformité",
     "Loi 25, hébergement, conservation — ce que le centre décide lui-même.",
     "guide-direction", "P3"),
    ("Les écrans, cas par cas",
     "Treize captures du portail en marche, selon la décision prise.",
     "captures-cas-de-figure", "A1"),
    ("Le cours sur un téléphone",
     "Les sept familles d'exercices, au doigt. Dix-huit captures.",
     "captures-telephone", "A2"),
    ("Les fiches de l'élève",
     "Ce qu'on lui met dans les mains, sur papier.",
     "fiches-eleve", "A3"),
    ("Les diaporamas de séance",
     "Ce que l'enseignant projette en classe, bloc par bloc.",
     "powerpoints-enseignant", "A4"),
    ("Les sept objections",
     "Celles qui viennent vraiment, et quoi répondre.",
     None, "A5"),
    ("Le prix d'un module",
     "Le coût par élève, mesuré sur le registre des appels.",
     "prix-dun-module", None),
]

PRES = RACINE / "assets" / "presentations"
DIAPOS = PRES / "diaporamas"


def formes(base, code):
    """(page, web, pptx, papier, vignette) — chacun un chemin relatif, ou None.

    Ne rend que ce qui est **sur le disque**. Le jour où une autre session
    renomme un diaporama, la case se vide au lieu de pointer dans le vide.

    `web` est la version **HTML animée**, celle qu'on projette ; `pptx` la
    même chose en PowerPoint, pour qui en veut un. Les deux sortent des mêmes
    fichiers de contenu — voir `build/powerpoints/pitch/web.py`.
    """
    page = ("%s.html" % base) if base and (PRES / ("%s.html" % base)).exists() else None
    pdf = ("%s.pdf" % base) if base and (PRES / ("%s.pdf" % base)).exists() else None
    web = pptx = vign = None
    if code:
        for f in sorted(DIAPOS.glob("%s-*.html" % code)):
            web = "diaporamas/%s" % f.name
            break
        for f in sorted(DIAPOS.glob("%s-*.pptx" % code)):
            pptx = "diaporamas/%s" % f.name
            break
        if (DIAPOS / "apercus" / ("%s.png" % code)).exists():
            vign = "diaporamas/apercus/%s.png" % code
    return page, web, pptx, pdf, vign


def orphelins():
    """Les diaporamas que le catalogue ne nomme pas.

    Sans ce contrôle, un diaporama ajouté par une autre session existerait sur
    le disque sans jamais paraître dans la trousse — et personne ne le saurait,
    puisque rien ne manque à l'écran.
    """
    connus = {c for _, _, _, c in TROUSSE if c}
    return sorted({f.name.split("-")[0] for f in DIAPOS.glob("*.pptx")
                   if f.name.split("-")[0] not in connus})


DEROULE = [
    ("0-2 min", "Le problème, pas le produit",
     "Une classe de francisation, seize personnes, huit niveaux de français dans la même "
     "salle, et une enseignante qui photocopie la veille au soir. On ne parle pas encore "
     "d'outil.", None, None),
    ("2-5 min", "Ce que l'élève voit",
     "Ouvrir un module sur un téléphone — le vôtre, pas une capture. Puis leur faire "
     "sortir le leur : le code QR de la séance est sur la feuille, ils entrent sans "
     "compte et ils ont l'assistance. C'est le moment qui vend.",
     "captures-telephone.html", "Le cours sur un téléphone"),
    ("5-8 min", "Ce que l'enseignant voit",
     "Le direct de la classe : quatorze élèves sur seize en ligne, question par question. "
     "Puis le dossier d'un élève. Dire tout de suite que les noms sont des pseudonymes.",
     "captures-cas-de-figure.html", "Les écrans, cas par cas"),
    ("8-11 min", "Ce qu'il y a dans la boîte",
     "Les chiffres du matériel — et surtout : une fiche par séance et un diaporama par "
     "séance, sortis du même fichier. C'est ce qui répond à « qui va préparer tout ça ? ».",
     "fiches-eleve.html", "Les fiches de l'élève"),
    ("11-14 min", "Ce que la direction décide",
     "Les quatre interrupteurs, joués en direct : l'assistant, le micro, le dépôt de la "
     "voix, les séances sans compte. Laisser la direction choisir une combinaison et "
     "montrer ce qu'elle change.", "bac-a-sable-cas-de-figure.html",
     "Le bac à sable des cas de figure"),
    ("14-17 min", "Les questions de conformité",
     "Ne pas attendre qu'on les pose. Loi 25, hébergement, conservation, ce que le centre "
     "doit décider lui-même. Avoir le guide ouvert dans un onglet.",
     "guide-direction.html", "Guide pour la direction"),
    ("17-20 min", "Le coût et la suite",
     "Le prix par élève et par module, puis une seule question : « qui essaie, et avec "
     "quel groupe ? ». Repartir avec un nom et une date, pas avec un accord de principe.",
     "prix-dun-module.html", "Le prix d'un module"),
]

QUESTIONS = [
    ("« Nous ne voulons pas d'intelligence artificielle avec nos élèves. »",
     "C'est un réglage, pas une négociation. Le centre le pose une fois sur l'arbre des "
     "organisations et les 87 modules se replient : plus de rail d'outils, plus de "
     "correction avant l'envoi, la réponse attendue après deux essais. Les dialogues, les "
     "exercices, les mini-leçons ne bougent pas — ils ne dépendent d'aucun modèle. "
     "<b>Le montrer plutôt que le dire</b> : c'est la paire d'écrans 07 et 08 des captures."),
    ("« Où sont hébergées les données ? Faut-il que ce soit au Québec ? »",
     "Non, et il y a trois conditions — elles sont écrites dans le guide pour la direction. "
     "Dire aussi ce qui n'est jamais gardé : les corrections de l'assistant s'affichent et "
     "ne s'écrivent nulle part, et le registre des appels compte des jetons sans jamais "
     "garder un texte."),
    ("« Il faut créer des comptes pour tous nos élèves ? »",
     "Pas nécessairement. Le mode séance ouvre une classe avec une feuille photocopiée et "
     "un code de six caractères : aucun compte, aucun pseudonyme, aucune donnée "
     "identifiante — et l'enseignant a quand même son tableau, participant par participant."),
    ("« Combien ça coûte ? »",
     "Le coût réel par élève et par module est dans « Le prix d'un module », avec la part "
     "qui vient des appels aux modèles. Un centre qui ferme l'assistant ne paie plus rien à "
     "l'usage : les voix sont enregistrées d'avance et les exercices se corrigent sur "
     "l'appareil."),
    ("« Est-ce que ça remplace l'enseignant ? »",
     "Non, et le matériel le prouve mieux qu'un discours : %s diaporamas de séance avec "
     "%s notes de présentateur, c'est-à-dire %s heures de classe <i>à donner</i>. "
     "L'outil prépare, il ne fait pas le cours."),
    ("« Qui a écrit le contenu ? »",
     "Nous. Chaque module part du programme d'études, avec sa situation de vie, ses "
     "intentions de communication et ses savoirs — rien n'est recopié d'un manuel. C'est "
     "ce qui permet d'y toucher : un module qui ne convient pas se réécrit."),
    ("« Nos élèves n'ont pas d'ordinateur. »",
     "Ils ont un téléphone, et c'est le cas d'usage principal, pas une adaptation : barre "
     "d'outils en bas de l'écran, banc de réponses sous le pouce, glisser-déposer au doigt. "
     "Aucune application à installer, aucun compte d'App Store."),
]

LIMITES = [
    "Le module ne corrige pas une production orale libre sans assistant : sans lui, "
    "l'enseignant écoute. Ne pas laisser croire l'inverse.",
    "La reconnaissance vocale appartient au navigateur : sur certains appareils, elle "
    "n'est pas confinée. C'est écrit dans le bac à sable, autant le dire soi-même.",
    "Le suivi dit ce que l'élève a fait, jamais ce qu'il a compris. C'est un tableau de "
    "bord, pas une évaluation.",
    "Il n'y a pas d'application mobile, et il n'y en aura pas : c'est un site. Le dire "
    "avant qu'on le découvre.",
]

AVANT = [
    "Ouvrir la <b>séance de démonstration</b> avant la rencontre et imprimer sa feuille — "
    "le code QR à faire scanner fait plus d'effet que n'importe quelle diapositive.",
    "Avoir <b>un téléphone chargé</b>, déjà connecté au bon réseau, avec le module ouvert.",
    "Vérifier que le portail répond, la veille — pas dans le corridor.",
    "Imprimer la liasse ci-dessous <b>en couleur</b>, et l'apporter en double : celui qui "
    "repart avec le papier y revient.",
    "Connaître trois chiffres par cœur et ne pas lire les autres.",
]


# ── La page ───────────────────────────────────────────────────────────────

def page(m):
    tuiles = [
        (m["cours"], "modules de cours"),
        (m["ateliers"], "ateliers"),
        (m["niveaux"], "niveaux couverts"),
        (m["fiches"], "fiches de l'élève"),
        (m["decks"], "diaporamas de séance"),
        (m["diapos"], "diapositives"),
        (m["heures"], "heures de classe préparées"),
        (m["mp3"], "pistes audio enregistrées"),
        (m["images"], "images produites"),
    ]
    h_tuiles = "".join(
        '<div class="tuile"><span class="n">%s</span><span class="l">%s</span></div>'
        % (html.escape(nb(v)), l) for v, l in tuiles)

    h_deroule = "".join(
        '<article class="etape"><div class="quand">%s</div><div class="quoi">'
        '<h3>%s</h3><p>%s</p>%s</div></article>'
        % (q, t, p, ('<a class="lien" href="%s">%s</a>' % (l, n)) if l else "")
        for q, t, p, l, n in DEROULE)

    h_questions = "".join(
        '<article class="qr"><h3>%s</h3><p>%s</p></article>'
        % (q, (r % (nb(m["decks"]), nb(m["notes"]), nb(m["heures"]))) if "%s" in r else r)
        for q, r in QUESTIONS)

    h_limites = "".join("<li>%s</li>" % l for l in LIMITES)
    h_avant = "".join("<li>%s</li>" % a for a in AVANT)

    # Le tableau unique : une ligne par document, trois formes possibles. Les
    # cellules se remplissent en regardant le disque — voir `formes()`.
    def cellule(chemin, mot):
        return ('<a href="%s">%s</a>' % (chemin, mot)) if chemin else '<span class="rien">—</span>'

    rangs = []
    for titre, phrase, base, code in TROUSSE:
        page, web, pptx, pdf, _ = formes(base, code)
        # « À projeter » montre d'abord le HTML animé — c'est ce qu'on projette.
        # Le PowerPoint reste offert en second, plus petit : il existe pour qui
        # en veut un, il n'est pas la version de référence.
        proj = cellule(web, code or "")
        if pptx:
            proj += ' <span class="sous">· <a href="%s">pptx</a></span>' % pptx
        rangs.append(
            '<tr><td><b>%s</b><br><span class="sous">%s</span></td>'
            '<td>%s</td><td>%s</td><td>%s</td></tr>'
            % (titre, phrase, cellule(page, "la page"), proj,
               cellule(pdf, "le PDF")))
    h_trousse = "".join(rangs)

    # La galerie : on ne montre que les documents qui ont un diaporama, dans
    # l'ordre du catalogue — donc le pitch avant les annexes.
    vign = []
    for titre, phrase, base, code in TROUSSE:
        page, web, deck, pdf, image = formes(base, code)
        if not deck:
            continue
        deck = web or deck      # la vignette ouvre la version projetable
        vign.append(
            '<figure><img src="%s" alt="Première diapositive de %s" loading="lazy">'
            '<figcaption><span class="code">%s</span>'
            '<a class="nom" href="%s">%s</a><p>%s</p></figcaption></figure>'
            % (image or deck, titre, code, deck, titre, phrase)
            if image else
            '<figure><figcaption><span class="code">%s</span>'
            '<a class="nom" href="%s">%s</a><p>%s</p></figcaption></figure>'
            % (code, deck, titre, phrase))
    h_vignettes = "".join(vign)

    manquants = orphelins()
    if manquants:
        print("  !! diaporama(s) hors catalogue : %s" % ", ".join(manquants))
        print("     Ajoutez-les à TROUSSE, sinon ils n'apparaissent nulle part.")

    return """<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>La trousse de présentation</title>
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
    --indigo-600:#3B49A0; --indigo-100:#E8EAFA;
    --marque-600:#6B4FBB; --marque-100:#EDE7F9; --marque-filet:#C3B4EA;
    --font-sans:"Nunito",system-ui,-apple-system,"Segoe UI",sans-serif;
  }
  *{box-sizing:border-box}
  body{margin:0; background:var(--surface-page); color:var(--ink-900);
    font-family:var(--font-sans); font-size:18px; font-weight:600; line-height:1.55;
    -webkit-font-smoothing:antialiased; -webkit-text-size-adjust:100%}
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
  .quand-page{font-size:14px; color:var(--ink-400); margin:0}
  main{padding:8px 0 80px}
  section{padding:42px 0 0}
  h2{font-size:27px; font-weight:900; letter-spacing:-.015em; margin:0 0 8px}
  p{margin:0 0 14px; max-width:70ch}
  .eyebrow{display:inline-block; font-size:12px; font-weight:800; letter-spacing:.12em;
    text-transform:uppercase; padding:4px 10px; border-radius:999px; margin:0 0 10px}
  .e-acier{background:var(--acier-100); color:var(--acier-600)}
  .e-ambre{background:var(--ambre-100); color:var(--ambre-700)}
  .e-teal{background:var(--teal-100); color:var(--teal-700)}
  .e-indigo{background:var(--indigo-100); color:var(--indigo-600)}
  strong,b{font-weight:900}
  code{font-family:ui-monospace,Menlo,Consolas,monospace; font-size:.86em;
    background:var(--paper-200); padding:1px 5px; border-radius:5px; font-weight:700}
  .lien{display:inline-block; font-size:14.5px; font-weight:800; text-decoration:none;
    color:var(--ink-900); background:#FFFFFF; border:1px solid var(--border-firm);
    border-radius:999px; padding:7px 13px; margin-top:6px}
  .lien:hover{background:var(--paper-200)}
  .tuiles{display:grid; gap:12px; grid-template-columns:repeat(auto-fit,minmax(min(150px,100%),1fr));
    margin:22px 0 0}
  .tuile{background:var(--surface-card); border:1px solid var(--border);
    border-left:4px solid var(--accent); border-radius:12px; padding:12px 14px}
  .tuile .n{font-size:24px; font-weight:900; letter-spacing:-.02em; display:block; line-height:1.12}
  .tuile .l{font-size:13px; font-weight:700; color:var(--ink-500)}
  .etape{display:grid; grid-template-columns:110px 1fr; gap:18px; align-items:start;
    background:var(--surface-card); border:1px solid var(--border); border-radius:14px;
    padding:16px 18px; margin-top:12px}
  .etape .quand{font-size:14px; font-weight:900; color:var(--accent-ink);
    background:var(--accent-soft); border-radius:999px; padding:5px 0; text-align:center}
  .etape h3{font-size:19px; font-weight:900; margin:0 0 4px}
  .etape p{font-size:16px; color:var(--ink-500); margin:0}
  .qr{background:var(--surface-card); border:1px solid var(--border); border-radius:14px;
    padding:16px 18px; margin-top:12px; border-left:4px solid var(--acier-600)}
  .qr h3{font-size:17.5px; font-weight:900; margin:0 0 6px; color:var(--ink-900)}
  .qr p{font-size:16px; color:var(--ink-500); margin:0; max-width:none}
  ul.liste{margin:12px 0 0; padding-left:22px}
  ul.liste li{margin-bottom:9px; max-width:70ch}
  .cadre-table{overflow-x:auto; border:1px solid var(--border); border-radius:14px;
    background:var(--surface-card); margin-top:14px}
  table{border-collapse:collapse; width:100%; font-size:16px}
  th,td{text-align:left; padding:11px 14px; border-bottom:1px solid var(--border)}
  thead th{font-size:12px; font-weight:800; letter-spacing:.08em; text-transform:uppercase;
    color:var(--ink-400); background:var(--surface-sunken)}
  tbody tr:last-child td{border-bottom:0}
  td a{color:var(--ink-900); font-weight:800}
  /* Trois vignettes de front sur un portable, une seule sur un téléphone.
     `minmax(min(280px,100%,1fr))` plutôt que `minmax(280px,1fr)` : sous 280 px
     la seconde forme déborde de la colonne au lieu de se replier. */
  .sous{color:var(--ink-400); font-size:14px;}
  .rien{color:var(--ink-400);}
  .vign{display:grid; gap:18px; margin-top:20px;
    grid-template-columns:repeat(auto-fill,minmax(min(280px,100%),1fr));}
  .vign figure{margin:0; background:var(--surface-card);
    border:1px solid var(--border); border-radius:14px; overflow:hidden;}
  .vign img{display:block; width:100%; height:auto; border-bottom:1px solid var(--border);}
  .vign figcaption{padding:12px 16px 14px;}
  .vign .code{font-size:12px; font-weight:800; letter-spacing:.10em;
    text-transform:uppercase; color:var(--ink-400);}
  .vign .nom{display:block; font-weight:800; margin:2px 0 4px; color:var(--ink-900);
    text-decoration:none;}
  .vign a.nom:hover{text-decoration:underline;}
  .vign p{margin:0; font-size:14px; color:var(--ink-500);}
  .garde{background:var(--accent-soft); border:1px solid #BFE3D2; border-radius:14px; padding:16px 20px}
  .garde p:last-child{margin-bottom:0}
  .alerte{background:var(--ambre-100); border:1px solid #E8D7B8; border-radius:14px; padding:16px 20px}
  hr{border:0; border-top:1px solid var(--border); margin:44px 0 0}
  footer p{font-size:16px; color:var(--ink-500)}

  @media print{
    @page{ size:letter; margin:14mm 14mm 16mm; }
    *{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }
    html,body{ background:#FFFFFF; font-size:10.5pt; }
    .conteneur{ max-width:none; padding:0; }
    .barre{ padding:0 0 4mm; border-bottom-width:1.2pt; }
    .bande{ background:#FFFFFF; border-bottom:1px solid var(--border); padding:0 0 5mm; }
    h1{ font-size:24pt; } h2{ font-size:14pt; } h3{ font-size:11.5pt; }
    .chapeau{ font-size:11.5pt; }
    section{ padding:6mm 0 0; }
    section > h2, section > .eyebrow{ break-after:avoid; }
    .etape, .qr, .tuiles, .garde, .alerte, .cadre-table{ break-inside:avoid; }
    .vign figure{ break-inside:avoid; }
    .etape{ margin-top:3mm; padding:10px 12px; }
    .qr{ margin-top:3mm; padding:10px 12px; }
    .lien{ display:none; }
    a[href]{ color:inherit; text-decoration:none; }
    p{ max-width:none; }
  }
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
      <p class="surtitre">Pour moi · Avant et pendant une rencontre</p>
      <h1>La trousse de présentation</h1>
    </div>
    <p class="chapeau">Tout ce qui s'ouvre pendant un pitch, dans l'ordre où on l'ouvre —
    plus les chiffres qu'il faut pouvoir dire sans les lire, les questions qui reviennent
    à chaque fois, et ce qu'il ne faut pas promettre. Une seule page à garder ouverte
    dans un onglet.</p>
    <p class="quand-page">Chiffres comptés sur le dépôt le __QUAND__ par
    <code>build/trousse.py</code>. Cette page s'adresse à moi, pas au client.</p>
  </div>
</header>

<main>

<section class="conteneur" id="tout">
  <p class="eyebrow e-indigo">Tout d'un coup d'œil</p>
  <h2>Ce qu'il y a dans la trousse</h2>
  <p>__NDOCS__ documents, et trois formes possibles pour chacun : la <b>page</b> qu'on
  ouvre dans un onglet, le <b>diaporama</b> qu'on projette, la <b>feuille</b> qu'on laisse
  sur la table. Un tiret veut dire que cette forme n'existe pas — pas qu'elle est
  ailleurs.</p>
  <div class="cadre-table"><table>
    <thead><tr><th>Document</th><th>À l'écran</th><th>À projeter</th><th>Sur papier</th></tr></thead>
    <tbody>__TROUSSE__</tbody>
  </table></div>
  <div class="garde" style="margin-top:16px">
    <p><b>Ce tableau est relevé sur le disque</b>, pas écrit à la main : une case ne
    s'affiche que si le fichier existe vraiment. Le jour où un diaporama est renommé, la
    case se vide au lieu de pointer dans le vide — on l'apprend en relançant le script,
    pas devant la salle.</p>
  </div>
</section>

<section class="conteneur">
  <p class="eyebrow e-teal">À projeter</p>
  <h2>Les diaporamas, en images</h2>
  <p>Trois familles. <b>P</b>, le pitch, dans l'ordre où on le projette — vingt minutes en
  tout. <b>A</b>, les annexes, qu'on ouvre seulement quand la salle demande à voir.
  <b>F</b>, les fondements : celui-là ne vend rien, il explique sur quoi le cours est
  bâti, et il se projette devant des gens qui connaissent le métier. Tous sortent du
  même système de design que les diaporamas de séance : c'est le produit qui se présente
  lui-même.</p>
  <div class="vign">__VIGNETTES__</div>
  <div class="garde" style="margin-top:18px">
    <p><b>Ils se refabriquent :</b>
    <code>python3 build/powerpoints/pitch.py --vignettes</code> recompte les chiffres,
    réécrit les neuf fichiers et refait les images ci-dessus. Un diaporama de vente qui
    annonce un chiffre périmé se retourne contre celui qui le projette.</p>
  </div>
  <p style="margin-top:16px">Pour une formation plutôt qu'un pitch, le canevas
  <a href="travailler-avec-claude.html"><b>Travailler avec Claude</b></a> (29 écrans,
  animés, six temps) se projette directement dans le navigateur.</p>
</section>

<section class="conteneur">
  <p class="eyebrow e-acier">Vingt minutes</p>
  <h2>Le déroulé</h2>
  <p>L'ordre compte plus que le contenu : on montre l'élève avant l'enseignant, et
  l'enseignant avant l'institution. Personne n'a jamais acheté un tableau de bord.</p>
  __DEROULE__
</section>

<section class="conteneur">
  <p class="eyebrow e-teal">À dire sans lire</p>
  <h2>Les chiffres</h2>
  <p>Trois suffisent pour une rencontre. Les autres sont là pour répondre, pas pour être
  récités.</p>
  <div class="tuiles">__TUILES__</div>
  <div class="garde" style="margin-top:18px">
    <p><b>Les trois à connaître par cœur :</b> __TROIS__. Le reste se retrouve sur cette
    page en deux secondes, et il vaut mieux chercher devant quelqu'un que réciter faux.</p>
  </div>
</section>

<section class="conteneur">
  <p class="eyebrow e-ambre">Elles reviennent toutes</p>
  <h2>Les sept questions</h2>
  __QUESTIONS__
</section>

<section class="conteneur">
  <p class="eyebrow e-indigo">Honnêteté</p>
  <h2>Ce qu'il ne faut pas promettre</h2>
  <p>Une limite dite par soi-même est un argument ; découverte par l'autre, c'est un
  problème.</p>
  <div class="alerte"><ul class="liste" style="margin:0">__LIMITES__</ul></div>
</section>

<section class="conteneur">
  <p class="eyebrow e-acier">La veille</p>
  <h2>Avant de partir</h2>
  <ul class="liste">__AVANT__</ul>
</section>

<section class="conteneur">
  <p class="eyebrow e-ambre">Le moment qui vend</p>
  <h2>Faire essayer la salle, sur leurs téléphones</h2>
  <p>Douze personnes qui regardent une démonstration se souviennent d'une démonstration.
  Douze personnes qui <b>font l'exercice</b> se souviennent de l'exercice. Le mode séance
  est fait pour ça : une feuille photocopiée, un code QR, et personne n'a de compte à
  créer.</p>
  <div class="cadre-table"><table>
    <thead><tr><th>Quand</th><th>Le geste</th></tr></thead>
    <tbody>
      <tr><td>La veille</td><td>Dans le portail, onglet <b>Élèves</b> → « Séance sans
        compte » : choisir un groupe de démonstration et un module court. Le serveur rend
        un code de six caractères.</td></tr>
      <tr><td>La veille</td><td>Ouvrir <b>la feuille</b> et l'imprimer — code QR, code en
        gros, adresse en toutes lettres, noir et blanc. En apporter une dizaine, ou une
        seule à projeter.</td></tr>
      <tr><td>Pendant</td><td>« Sortez votre téléphone, visez le carré. » Ils entrent en
        deux secondes, sans compte et sans nom.</td></tr>
      <tr><td>Après</td><td>Projeter <b>le direct de la classe</b> : leurs réponses
        arrivent, question par question, sous « Participant 1 » à « Participant N ».</td></tr>
    </tbody>
  </table></div>
  <div class="garde" style="margin-top:16px">
    <p><b>Ils auront l'assistance</b> — traduire, simplifier, demander, « Corrige-moi ! » —
    parce qu'une séance hérite des réglages de son centre, et que l'assistance est
    autorisée par défaut. C'est justement ce qu'il faut leur faire toucher : la salle
    essaie exactement ce que la direction s'apprête à autoriser ou non.</p>
    <p style="margin-top:10px"><b>Deux bornes à connaître :</b> la séance <b>expire le
    soir même</b> et accepte <b>__PLAFOND__ appareils</b>. Pour une rencontre, c'est large ; pour
    une journée portes ouvertes, en ouvrir une par demi-journée.</p>
  </div>
  <p style="margin-top:16px"><b>Vous avez déjà le code ?</b> Ouvrez la feuille
  directement : <a href="/feuille-seance.html">feuille-seance.html?code=XXXXXX</a> —
  remplacez les six X. La feuille se fabrique côté serveur, code QR compris : aucun
  service tiers ne voit l'adresse de votre classe.</p>
</section>

<hr>
<footer class="conteneur">
  <p>Cette page est <b>générée</b> : relancer <code>build/trousse.py</code> recompte les
  modules, les fiches, les diapositives et les pistes audio. Un chiffre faux dans une
  rencontre coûte plus cher que trois chiffres manquants — et un chiffre recopié devient
  faux tout seul.</p>
</footer>
</main>
</body>
</html>
""".replace("__PLAFOND__", str(m["plafond"])).replace("__QUAND__", m["quand"]).replace("__TUILES__", h_tuiles) \
   .replace("__DEROULE__", h_deroule).replace("__QUESTIONS__", h_questions) \
   .replace("__LIMITES__", h_limites).replace("__AVANT__", h_avant) \
   .replace("__TROUSSE__", h_trousse).replace("__VIGNETTES__", h_vignettes) \
   .replace("__NDOCS__", str(len(TROUSSE))) \
   .replace("__TROIS__", "<b>%s modules de cours</b> sur %d niveaux, "
                         "<b>%s heures de classe préparées</b>, "
                         "<b>une fiche et un diaporama pour chacune des %s séances</b>"
                         % (nb(m["cours"]), m["niveaux"], nb(m["heures"]), nb(m["decks"])))


if __name__ == "__main__":
    import argparse
    import sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
    from imprimer import imprimer

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sans-pdf", action="store_true",
                    help="n'écrit que la page HTML")
    a = ap.parse_args()

    m = mesures()
    SORTIE.write_text(page(m))
    print("écrit :", SORTIE.relative_to(RACINE))
    print("%d cours · %d ateliers · %s fiches · %s diaporamas · %s h"
          % (m["cours"], m["ateliers"], m["fiches"], m["decks"], m["heures"]))

    # Le PDF est ce qu'on laisse sur la table : une page réorganisée au-dessus
    # d'un PDF resté à l'ancienne organisation ne signale rien, et c'est le
    # papier que la direction relit une semaine plus tard.
    if not a.sans_pdf:
        pdf = SORTIE.with_suffix(".pdf")
        n = imprimer(SORTIE, pdf)
        print("  %-30s %s" % (pdf.name, ("%d pages" % n) if n else "produit"))
