#!/usr/bin/env python3
"""Une planche de contact numérotée de toutes les images des modules.

Sert à une seule chose : permettre de dire « refais la 47, la 112 et la 213 »
au lieu de « certaines images ne sont pas adéquates ». Chaque image reçoit un
**numéro global stable** — l'ordre est celui du chemin, trié, donc il ne bouge
pas tant qu'aucune image n'est ajoutée ni retirée. Après un ajout, les numéros
qui suivent glissent : c'est pourquoi la page affiche aussi, sous chaque
vignette, le module et le nom de fichier, qui, eux, ne glissent jamais.

La page se coche : un clic sur une vignette la marque « à refaire », et la
barre du bas tient la liste à jour, prête à être copiée. Les choix survivent
au rechargement (localStorage).

    python3 build/planche_images.py           # écrit planche-images.html
    python3 build/planche_images.py --module module-n6-sante

Puis, le serveur local tournant :  http://localhost:5173/planche-images.html
"""

import argparse
import html
import json
import pathlib

BASE = pathlib.Path(__file__).resolve().parent.parent
RACINE = BASE / "assets" / "interactive"
SORTIE = BASE / "planche-images.html"
# Deux dossiers par module, deux natures : `images/` sert les exercices
# d'association, `vocab/` illustre les cartes de vocabulaire. Les juger
# ensemble mais les distinguer à l'écran — une carte de vocabulaire se lit
# contre un mot, une image d'exercice contre une phrase à associer.
DOSSIERS = ("images", "vocab")
CONTEXTES = BASE / "build" / "_contexte_images.json"
EXT = {".jpg", ".jpeg", ".png", ".webp"}

# Les quatre défauts relevés le 22 août 2026. Ils ne se réparent pas de la
# même façon : « texte » veut un prompt qui interdit toute écriture, « mains »
# veut un cadrage qui les sort du champ, « décor » veut des repères québécois
# nommés, et « hors sujet » veut un prompt réécrit depuis l'énoncé — l'image
# est bonne, elle ne montre simplement pas ce que la phrase demande. D'où le
# motif demandé à la vignette plutôt qu'une simple croix.
MOTIFS = ("texte", "mains", "décor", "hors sujet")


def recenser(filtre=None):
    """Rend la liste [(module, chemin_relatif_au_depot)], triée, stable."""
    trouvees = []
    for module in sorted(d.name for d in RACINE.iterdir() if d.is_dir()):
        if filtre and filtre != module:
            continue
        for nom in DOSSIERS:
            dossier = RACINE / module / nom
            if not dossier.is_dir():
                continue
            for f in sorted(dossier.iterdir()):
                if f.suffix.lower() in EXT:
                    trouvees.append((module, f.relative_to(BASE).as_posix()))
    return trouvees


def contextes():
    """Ce que chaque image est censée montrer, relevé par le script node.

    Son absence n'empêche rien : la planche s'affiche alors sans énoncés, et
    le dit plutôt que de laisser croire qu'aucune image n'a de contexte.
    """
    if not CONTEXTES.exists():
        return {}
    brut = json.loads(CONTEXTES.read_text(encoding="utf-8"))
    # La clé du relevé est « module/fichier.jpg » ; celle de la planche est le
    # chemin complet. On croise sur le nom de fichier, dans le bon module.
    return {c.split("/", 1)[0] + "/" + c.rsplit("/", 1)[-1]: v
            for c, v in brut.items()}


def page(images, ctx):
    """La planche. Aucun style importé : elle doit s'ouvrir seule, partout."""
    par_module = {}
    for i, (module, chemin) in enumerate(images, start=1):
        par_module.setdefault(module, []).append((i, chemin))

    sans_contexte = 0
    blocs = []
    for module, lot in par_module.items():
        vignettes = []
        for numero, chemin in lot:
            nom = html.escape(chemin.rsplit("/", 1)[-1])
            c = ctx.get(module + "/" + chemin.rsplit("/", 1)[-1], {})
            if not c.get("enonce"):
                sans_contexte += 1
            attendu = (
                '<p class="attendu"><span class="ou">%s</span>%s</p>'
                % (html.escape(c.get("exercice") or
                               ("vocabulaire" if c.get("role") == "vocabulaire"
                                else "contexte non relevé")),
                   html.escape(c.get("enonce", "")))
            )
            vignettes.append(
                '<figure class="v" data-n="%d" data-chemin="%s">'
                '<span class="n">%d</span>'
                '<img loading="lazy" src="%s" alt="">'
                '%s'
                '<figcaption>%s</figcaption>'
                '<div class="motifs">%s</div></figure>'
                % (numero, html.escape(chemin), numero,
                   html.escape(chemin), attendu, nom,
                   "".join('<button data-motif="%s">%s</button>' % (m, m)
                           for m in MOTIFS)))
        blocs.append(
            '<section><h2>%s <small>%d images · n° %d à %d</small></h2>'
            '<div class="grille">%s</div></section>'
            % (html.escape(module), len(lot), lot[0][0], lot[-1][0],
               "".join(vignettes)))

    index = {str(i): {"module": m, "chemin": c}
             for i, (m, c) in enumerate(images, start=1)}

    return """<!doctype html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Planche des images — %(total)d</title>
<style>
  :root { --encre:#101418; --gris:#5b6672; --trait:#d8dee5; --rouge:#b3261e; }
  * { box-sizing:border-box; }
  body { margin:0; padding:0 24px 120px; background:#fff; color:var(--encre);
         font:15px/1.5 -apple-system, "Segoe UI", Roboto, sans-serif; }
  header { position:sticky; top:0; background:#fff; padding:20px 0 12px;
           border-bottom:1px solid var(--trait); z-index:5; }
  h1 { margin:0 0 4px; font-size:20px; }
  header p { margin:0; color:var(--gris); }
  h2 { margin:32px 0 10px; font-size:16px; }
  h2 small { color:var(--gris); font-weight:400; margin-left:8px; }
  .grille { display:grid; gap:14px;
            grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); }
  .v { margin:0; position:relative; cursor:pointer; border:2px solid transparent;
       border-radius:8px; padding:4px; background:#f6f8fa; }
  .v img { width:100%%; aspect-ratio:3/2; object-fit:cover; display:block;
           border-radius:5px; }
  .n { position:absolute; top:8px; left:8px; background:rgba(16,20,24,.82);
       color:#fff; font-size:12px; font-weight:600; padding:2px 7px;
       border-radius:99px; }
  .attendu { margin:7px 0 0; font-size:12px; line-height:1.35; }
  .attendu .ou { display:block; font-size:10px; letter-spacing:.04em;
       text-transform:uppercase; color:var(--gris); margin-bottom:2px; }
  figcaption { font-size:11px; color:var(--gris); margin-top:5px;
               word-break:break-all; }
  .v.refaire { border-color:var(--rouge); background:#fdeceb; }
  .v.refaire .n { background:var(--rouge); }
  .motifs { display:none; gap:5px; margin-top:6px; flex-wrap:wrap; }
  .v.refaire .motifs { display:flex; }
  .motifs button { flex:1 1 40%%; border:1px solid var(--trait); background:#fff;
       color:var(--gris); font-size:11px; padding:4px 0; border-radius:5px;
       cursor:pointer; }
  .motifs button.choisi { background:var(--rouge); border-color:var(--rouge);
       color:#fff; font-weight:600; }
  footer { position:fixed; bottom:0; left:0; right:0; background:#101418;
           color:#fff; padding:12px 24px; display:flex; gap:16px;
           align-items:center; flex-wrap:wrap; }
  footer textarea { flex:1; min-height:44px; font:12px/1.4 ui-monospace,
           Menlo, monospace; padding:8px; border-radius:6px; border:0;
           resize:vertical; }
  footer button { background:#fff; color:#101418; border:0; padding:9px 14px;
           border-radius:6px; font-weight:600; cursor:pointer; }
  footer .compte { font-weight:600; white-space:nowrap; }
</style></head><body>
<header>
  <h1>Planche des images — %(total)d images, %(modules)d modules</h1>
  <p>Sous chaque image, <strong>ce qu'elle est censée montrer</strong> :
     l'exercice et la phrase que l'élève doit lui associer, ou le mot qu'elle
     illustre. Clique une vignette qui ne correspond pas, puis dis pourquoi.
     La liste du bas se tient à jour ; copie-la et colle-la-moi.
     %(note)s</p>
</header>
%(blocs)s
<footer>
  <span class="compte" id="compte">0 à refaire</span>
  <textarea id="liste" readonly placeholder="Aucune image marquée."></textarea>
  <button id="copier">Copier</button>
  <button id="vider">Tout décocher</button>
</footer>
<script>
const INDEX = %(index)s;
const CLE = "planche-images-a-refaire";
// { "47": "texte" } — la valeur vide veut dire « à refaire, motif non dit ».
const choix = JSON.parse(localStorage.getItem(CLE) || "{}");

function rendre() {
  document.querySelectorAll(".v").forEach(v => {
    const n = v.dataset.n, marque = n in choix;
    v.classList.toggle("refaire", marque);
    v.querySelectorAll(".motifs button").forEach(b => {
      b.classList.toggle("choisi", marque && choix[n] === b.dataset.motif);
    });
  });
  const tri = Object.keys(choix).sort((a, b) => a - b);
  document.getElementById("compte").textContent = tri.length + " à refaire";
  document.getElementById("liste").value = tri.length
    ? tri.map(n => n + "  " + (choix[n] || "—").padEnd(6) + "  "
                 + INDEX[n].chemin).join("\\n")
    : "";
  localStorage.setItem(CLE, JSON.stringify(choix));
}

document.querySelectorAll(".v").forEach(v => {
  const n = v.dataset.n;
  v.addEventListener("click", e => {
    // Un clic sur une pastille choisit le motif ; ailleurs, il bascule.
    const pastille = e.target.closest(".motifs button");
    if (pastille) {
      choix[n] = choix[n] === pastille.dataset.motif
        ? "" : pastille.dataset.motif;
    } else if (n in choix) {
      delete choix[n];
    } else {
      choix[n] = "";
    }
    rendre();
  });
});
document.getElementById("copier").addEventListener("click", () => {
  const t = document.getElementById("liste");
  t.select();
  navigator.clipboard.writeText(t.value);
});
document.getElementById("vider").addEventListener("click", () => {
  Object.keys(choix).forEach(n => delete choix[n]);
  rendre();
});
rendre();
</script>
</body></html>
""" % {"total": len(images), "modules": len(par_module),
       "blocs": "\n".join(blocs),
       "note": ("<em>%d images sans contexte relevé.</em>" % sans_contexte
                if sans_contexte else ""),
       "index": json.dumps(index, ensure_ascii=False)}


def main():
    a = argparse.ArgumentParser(description=__doc__)
    a.add_argument("--module", help="ne prendre qu'un module")
    a.add_argument("--liste", action="store_true",
                   help="écrire la table numéro → chemin sur la sortie")
    opt = a.parse_args()

    images = recenser(opt.module)
    if not images:
        raise SystemExit("aucune image trouvée")
    ctx = contextes()
    if not ctx:
        print("  (aucun contexte : lancer d'abord"
              " node build/contexte_images.js > build/_contexte_images.json)")

    if opt.liste:
        for i, (module, chemin) in enumerate(images, start=1):
            print("%4d  %-28s %s" % (i, module, chemin))
        return

    SORTIE.write_text(page(images, ctx), encoding="utf-8")
    modules = len({m for m, _ in images})
    print("✓ %d images · %d modules · %s" % (len(images), modules, SORTIE))
    print("  http://localhost:5173/planche-images.html")


if __name__ == "__main__":
    main()
