#!/usr/bin/env python3
"""Un lien direct vers un onglet du classeur : /presentations.html#defibrillateur

LE PROBLÈME, dit à l'usage : « je ne la trouve pas ». Le classeur ouvre
toujours sur « Tout », cent trente et une fiches, et il n'existait aucune
adresse qui désigne une famille. On ne pouvait ni l'ajouter aux favoris, ni
l'envoyer à quelqu'un, ni y revenir.

La greffe fait deux choses, et la seconde compte autant : elle LIT le hash au
chargement, et elle l'ÉCRIT quand on change d'onglet — sinon l'adresse ment
sur ce qu'on regarde, et copier l'URL ramène ailleurs.

Posée entre marqueurs, retirable d'un marqueur à l'autre : un remplacement de
chaîne exact échoue en SILENCE, et cela a déjà coûté soixante-dix-sept modules
dans ce dépôt.

    python3 build/lien_onglet.py [--essai|--retirer]
"""
import re, sys, pathlib

PAGE = pathlib.Path(__file__).resolve().parent.parent / "presentations.html"
DEBUT, FIN = "/*<<LIEN-ONGLET>>*/", "/*<</LIEN-ONGLET>>*/"

GREFFE = DEBUT + """
  // ── Lien direct vers un onglet ──────────────────────────────────────
  // Le hash désigne la famille : #defibrillateur, #entreprise, #portfolio…
  // On réutilise le clic plutôt que de refaire le filtrage : une seconde
  // implémentation du même choix finit toujours par diverger de la première.
  (function () {
    function onglet(nom) {
      for (var i = 0; i < onglets.length; i++) {
        if (onglets[i].dataset.f === nom) return onglets[i];
      }
      return null;
    }
    function suivre() {
      var b = onglet((location.hash || '').replace(/^#/, ''));
      if (b && b.getAttribute('aria-pressed') !== 'true') b.click();
    }
    onglets.forEach(function (b) {
      b.addEventListener('click', function () {
        // history.replaceState : on ne veut pas empiler une entrée par clic,
        // sinon « retour » redéfile tous les onglets visités un par un.
        var h = b.dataset.f === 'tout' ? location.pathname : '#' + b.dataset.f;
        try { history.replaceState(null, '', h); } catch (e) {}
      });
    });
    addEventListener('hashchange', suivre);
    suivre();
  }());
""" + FIN

def retirer(s):
    return re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN), "", s, flags=re.S)

if __name__ == "__main__":
    s = PAGE.read_text(encoding="utf-8")
    if "--retirer" in sys.argv:
        PAGE.write_text(retirer(s), encoding="utf-8"); print("greffe retirée"); raise SystemExit
    s = retirer(s)
    # Le point d'ancrage : juste après le brancheur des onglets, là où
    # `onglets` et `appliquer` sont tous deux dans la portée.
    m = re.search(r"\n  q\.addEventListener\('input', appliquer\);\n", s)
    if not m:
        raise SystemExit("point d'ancrage introuvable — le script du classeur a changé. "
                         "Vérifier AVANT de poser à l'aveugle.")
    familles = re.findall(r'<button type="button" class="onglet" data-f="([^"]+)"', s)
    if "--essai" in sys.argv:
        print("  À BLANC — la page n'est pas modifiée.")
        print(f"  ancrage trouvé à l'octet {m.start()}")
        print("  adresses qui fonctionneront :")
        for f in familles:
            print(f"    /presentations.html{'' if f == 'tout' else '#' + f}")
        raise SystemExit
    PAGE.write_text(s[:m.end()] + "\n" + GREFFE + "\n" + s[m.end():], encoding="utf-8")
    print(f"  greffe posée · {len(familles)} onglets adressables")
