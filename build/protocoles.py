#!/usr/bin/env python3
"""Le registre des protocoles : tout ce qu'on s'est promis de faire, sur une page.

    python3 build/protocoles.py      # → assets/presentations/protocoles.html

Demandé le 3 septembre 2026 : « comment je pourrais faire pour me rappeler
tous les protocoles qu'on a développés ? » Ils vivent dans la mémoire des
conversations — une fiche par règle, type `feedback` — que l'assistant charge
au démarrage mais que personne d'autre ne lit. Cette page les **recopie** dans
la banque des présentations, groupés par domaine, avec la règle en tête et son
pourquoi en dessous. Elle est produite, jamais écrite à la main : relancer le
script après une séance qui a ajouté ou corrigé une règle.

Ce n'est pas une seconde source : la fiche de mémoire fait foi, la page est son
miroir. Si les deux divergent, c'est que le script n'a pas été relancé.
"""
import html
import pathlib
import re
from datetime import date

RACINE = pathlib.Path(__file__).resolve().parent.parent
MEMOIRE = pathlib.Path.home() / ".claude/projects/-Users-danieltousignant-Claude/memory"
SORTIE = RACINE / "assets/presentations/protocoles.html"

# Le domaine d'une fiche se lit dans son nom. L'ordre est celui de la page.
DOMAINES = [
    ("Façon de travailler ensemble",
     ("methode-de-travail", "ecrire-en-memoire", "efficacite-tokens", "decisions-sur-page",
      "tout-document", "onglet-entreprise", "ecoute-toujours", "serveur-local",
      "agents-paralleles", "couloirs")),
    ("Le dépôt et le code",
     ("git-add", "greffe-retrait", "artefacts-binaires", "cache-navigateur",
      "verifier-en-jouant")),
    ("Capsules vidéo et procéduriers",
     ("protocole-capsules", "methode-capsules", "procedurier-guide")),
    ("Voix et audio",
     ("gel-des-mp3", "audio-elevenlabs", "debit-se-regle", "epellation")),
    ("Contenu des modules",
     ("regle-contenu", "savoirs-explicites", "longueur-modules", "parcours-different",
      "diagnostic-reste", "diagnostic-didactique")),
    ("Images et documents",
     ("images-format", "prompts-images", "fiches-eleves", "controle-debordement",
      "logotype", "code-couleur")),
]


def fiches():
    """Les fiches de type feedback : (nom, description, corps)."""
    for f in sorted(MEMOIRE.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", t, re.S)
        if not m or "type: feedback" not in m.group(1):
            continue
        tete, corps = m.groups()
        nom = re.search(r"^name:\s*(.+)$", tete, re.M).group(1).strip()
        d = re.search(r"^description:\s*(.+)$", tete, re.M)
        desc = d.group(1).strip().strip('"') if d else ""
        yield nom, desc, corps.strip()


def domaine(nom):
    for titre, cles in DOMAINES:
        if any(nom.startswith(c) for c in cles):
            return titre
    return "Autres règles"


def en_ligne(s, noms):
    """Gras, code et liens [[…]] d'une ligne, texte échappé d'abord."""
    s = html.escape(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\[\[([^\]]+)\]\]",
               lambda m: ('<a href="#%s">%s</a>' % (m.group(1), m.group(1))
                          if m.group(1) in noms else "<i>%s</i>" % m.group(1)), s)
    return s


def rendre_corps(corps, noms):
    """Markdown minimal → HTML : paragraphes, listes, titres, tableaux."""
    out, para, liste = [], [], []

    def vider():
        nonlocal para, liste
        if para:
            out.append("<p>%s</p>" % en_ligne(" ".join(para), noms)); para = []
        if liste:
            out.append("<ul>%s</ul>" % "".join("<li>%s</li>" % en_ligne(x, noms) for x in liste))
            liste = []
    for ligne in corps.split("\n"):
        l = ligne.rstrip()
        if not l.strip():
            vider(); continue
        if l.startswith("#"):
            vider(); out.append("<h4>%s</h4>" % en_ligne(l.lstrip("# "), noms)); continue
        if l.startswith("|"):
            if "---" in l:
                continue
            cellules = [c.strip() for c in l.strip("|").split("|")]
            vider(); out.append("<p class='rangee'>%s</p>" % " · ".join(en_ligne(c, noms) for c in cellules))
            continue
        m = re.match(r"^\s*(?:[-·•]|\d+\.)\s+(.*)$", l)
        if m:
            if para:
                vider()
            liste.append(m.group(1)); continue
        if liste and l.startswith("  "):
            liste[-1] += " " + l.strip(); continue
        if liste:
            vider()
        para.append(l.strip())
    vider()
    return "\n".join(out)


GABARIT = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Les protocoles</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&family=Nunito:wght@400;600;700;800&display=swap">
<style>
:root{--ink:#17181A;--muted:#5A5C60;--paper:#FAFAF8;--rule:#E4E4E0;--sunken:#F1F1EE;--accent:#0A8F5B}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 'Nunito','Helvetica Neue',Arial,sans-serif}
.page{max-width:900px;margin:0 auto;padding:40px 24px 80px}
h1{font:600 38px/1.15 'Newsreader',Georgia,serif;margin:0 0 6px}
.sous{color:var(--muted);margin:0 0 28px;max-width:640px}
.sommaire{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:18px 22px;margin-bottom:40px;columns:2;column-gap:32px}
.sommaire h3{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);margin:0 0 6px;break-after:avoid}
.sommaire ul{margin:0 0 16px;padding-left:18px;break-inside:avoid}
.sommaire li{margin:2px 0;font-size:15px}
.sommaire a{color:var(--ink);text-decoration:none}.sommaire a:hover{text-decoration:underline}
h2{font:600 28px/1.2 'Newsreader',Georgia,serif;margin:48px 0 18px;padding-top:24px;border-top:2px solid var(--ink)}
article{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:20px 24px;margin:0 0 18px}
article h3{margin:0 0 4px;font-size:19px}
article .regle{margin:0 0 14px;color:var(--ink);font-weight:600;border-left:3px solid var(--accent);padding-left:12px}
article .corps{color:#2D2F33;font-size:15px}
article .corps p{margin:8px 0}article .corps ul{margin:6px 0;padding-left:20px}
article .corps h4{margin:14px 0 4px;font-size:15px}
article .corps code{font:13px ui-monospace,Menlo,monospace;background:var(--sunken);padding:1px 5px;border-radius:4px}
article .corps .rangee{font-size:14px;color:var(--muted)}
details summary{cursor:pointer;color:var(--muted);font-size:14px;margin-top:6px}
.pied{color:var(--muted);font-size:14px;margin-top:48px;border-top:1px solid var(--rule);padding-top:14px}
@media (max-width:640px){.sommaire{columns:1}}
@media print{article{break-inside:avoid;border:none;padding:0 0 8px}details{display:none}}
</style></head><body><div class="page">
<h1>Les protocoles</h1>
<p class="sous">Tout ce qu'on s'est promis de faire en travaillant ensemble — %(n)d règles, une fiche chacune,
groupées par domaine. La règle est en tête ; son pourquoi et sa façon de l'appliquer se déplient dessous.
Page produite le %(date)s par <code>build/protocoles.py</code> depuis la mémoire des conversations, qui fait foi.</p>
<nav class="sommaire">%(sommaire)s</nav>
%(corps)s
<p class="pied">Relancer <code>python3 build/protocoles.py</code> après toute séance qui ajoute ou corrige une règle :
la page ne se met pas à jour toute seule.</p>
</div></body></html>
"""


def main():
    toutes = list(fiches())
    noms = {n for n, _, _ in toutes}
    par_dom = {}
    for n, d, c in toutes:
        par_dom.setdefault(domaine(n), []).append((n, d, c))
    ordre = [t for t, _ in DOMAINES] + ["Autres règles"]
    sommaire, corps = [], []
    for dom in ordre:
        if dom not in par_dom:
            continue
        # Quelques fiches ont une description qui ne dit rien (« Règle
        # permanente ») : le sommaire prend alors leur nom, qui dit toujours
        # de quoi il s'agit.
        def accroche(n, d):
            court = d.split(" — ")[0].split(" ; ")[0]
            return court if len(court) >= 35 else n.replace("-", " ")
        sommaire.append("<h3>%s</h3><ul>%s</ul>" % (html.escape(dom), "".join(
            '<li><a href="#%s">%s</a></li>' % (n, en_ligne(accroche(n, d), noms))
            for n, d, _ in par_dom[dom])))
        corps.append("<h2>%s</h2>" % html.escape(dom))
        for n, d, c in par_dom[dom]:
            corps.append(
                '<article id="%s"><h3>%s</h3><p class="regle">%s</p>'
                '<details><summary>Le pourquoi, et comment l\'appliquer</summary>'
                '<div class="corps">%s</div></details></article>'
                % (n, html.escape(n.replace("-", " ")), en_ligne(d, noms), rendre_corps(c, noms)))
    quand = date.today()
    mois = ("janvier février mars avril mai juin juillet août septembre octobre novembre décembre").split()
    page = GABARIT % {"n": len(toutes), "date": "%d %s %d" % (quand.day, mois[quand.month - 1], quand.year),
                      "sommaire": "".join(sommaire), "corps": "\n".join(corps)}
    SORTIE.write_text(page, encoding="utf-8")
    print("%d règles → %s" % (len(toutes), SORTIE.relative_to(RACINE)))
    for dom in ordre:
        if dom in par_dom:
            print("  %-34s %d" % (dom, len(par_dom[dom])))


if __name__ == "__main__":
    main()
