#!/usr/bin/env python3
"""« Dernière mise à jour » en tête de chaque famille du classeur.

LE PROBLÈME, dit à l'usage : cent trente et une fiches, chacune datée dans son
bloc `.meta` en PIED de fiche. Pour savoir laquelle est la plus récente d'une
famille, il fallait les ouvrir toutes. La date existait ; elle n'était pas
trouvable.

LA GREFFE EST POSÉE ENTRE MARQUEURS et se retire d'un marqueur à l'autre —
jamais par chaîne exacte : l'échec d'un remplacement exact est SILENCIEUX, et
il a déjà coûté soixante-dix-sept modules dans ce dépôt.

`presentations.html` n'est pas engendré : c'est une source éditée à la main.
On n'y touche donc que par cette greffe, qui est idempotente.

    python3 build/dernieres_versions.py --essai
    python3 build/dernieres_versions.py
    python3 build/dernieres_versions.py --retirer
"""
import re, sys, pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "presentations.html"
MOIS = {m: i for i, m in enumerate(
    "janvier février mars avril mai juin juillet août septembre octobre "
    "novembre décembre".split(), 1)}

def quand(txt):
    m = re.match(r"(\d+)(?:er)?\s+(\S+)\s+(\d{4})", txt.strip())
    if not m: return None
    j, mo, a = m.groups()
    if mo not in MOIS: return None
    return (int(a), MOIS[mo], int(j))

def familles(s):
    """(nom, début, fin) de chaque section — bornes calculées, pas devinées."""
    out = []
    for m in re.finditer(r'<section class="famille" data-fam="([^"]+)"', s):
        fin = s.find('<section class="famille"', m.end())
        out.append((m.group(1), m.start(), fin if fin > 0 else len(s)))
    return out

def fiches(bloc):
    """(titre, date, ancre) de chaque fiche de la section."""
    out = []
    for m in re.finditer(r'<article class="fiche"(.*?)</article>', bloc, re.S):
        f = m.group(0)
        t = re.search(r'<h3[^>]*>(.*?)</h3>', f, re.S)
        d = re.search(r'<span class="date">([^<]+)</span>', f)
        a = re.search(r'<a class="btn" href="([^"]+)"', f)
        if not (t and d): continue
        titre = re.sub(r"<[^>]+>", "", t.group(1)).strip()
        out.append((titre, d.group(1).strip(), quand(d.group(1)), a.group(1) if a else None))
    return out

DEBUT, FIN = "<!--<<DERNIERE>>-->", "<!--<</DERNIERE>>-->"

def retirer(s):
    return re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN), "", s, flags=re.S)

STYLE_DEBUT, STYLE_FIN = "/*<<DERNIERE-CSS>>*/", "/*<</DERNIERE-CSS>>*/"
CSS = f"""{STYLE_DEBUT}
  .derniere{{display:flex;flex-wrap:wrap;align-items:baseline;gap:.5rem;
    margin:.9rem 0 0;padding:.55rem .8rem;border:1px solid var(--line);
    border-left:3px solid var(--accent,#0f766e);border-radius:4px;
    font-size:var(--fs-ui-sm);background:var(--surface-2,#fafafa)}}
  .derniere .lab{{font-weight:800;letter-spacing:.06em;text-transform:uppercase;
    color:var(--ink-400)}}
  .derniere .quoi{{font-weight:700}}
  .derniere .q{{color:var(--ink-400)}}
  .derniere a{{color:inherit}}
{STYLE_FIN}"""

def poser(s):
    s = retirer(s)
    s = re.sub(re.escape(STYLE_DEBUT) + r".*?" + re.escape(STYLE_FIN), "", s, flags=re.S)
    # le style, juste avant la fin de la première feuille
    i = s.index("</style>")
    s = s[:i] + CSS + "\n" + s[i:]
    # puis chaque famille, de la DERNIÈRE à la première : insérer par la fin
    # garde valides les décalages de celles qu'on n'a pas encore traitées.
    for nom, a, b in reversed(familles(s)):
        bloc = s[a:b]
        fs = [f for f in fiches(bloc) if f[2]]
        if not fs: continue
        titre, date, _, lien = max(fs, key=lambda f: f[2])
        t = re.search(r'</p>\s*</div>', bloc)          # fin du chapeau de la tête
        if not t: continue
        quoi = (f'<a href="{lien}" target="_blank" rel="noopener">{titre}</a>'
                if lien else titre)
        ligne = (f'{DEBUT}<p class="derniere">'
                 f'<span class="lab">Dernière mise à jour</span>'
                 f'<span class="quoi">{date}</span>'
                 f'<span class="q">— {quoi}</span></p>{FIN}')
        s = s[:a + t.end() - len("</div>")] + ligne + s[a + t.end() - len("</div>"):]
    return s

if __name__ == "__main__":
    s = PAGE.read_text(encoding="utf-8")
    if "--retirer" in sys.argv:
        n = re.sub(re.escape(STYLE_DEBUT) + r".*?" + re.escape(STYLE_FIN), "",
                   retirer(s), flags=re.S)
        PAGE.write_text(n, encoding="utf-8"); print("greffe retirée"); raise SystemExit
    for nom, a, b in familles(s):
        fs = [f for f in fiches(s[a:b]) if f[2]]
        if not fs: print(f"  {nom:16} aucune date lisible"); continue
        t, d, _, _ = max(fs, key=lambda f: f[2])
        print(f"  {nom:16} {len(fs):3} fiches · dernière : {d:22} {t[:44]}")
    if "--essai" in sys.argv:
        print("\n  À BLANC — la page n'est pas modifiée."); raise SystemExit
    PAGE.write_text(poser(s), encoding="utf-8")
    print(f"\n  greffe posée · {PAGE.stat().st_size//1024} ko")
