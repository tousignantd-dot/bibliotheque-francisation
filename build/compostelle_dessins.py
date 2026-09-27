#!/usr/bin/env python3
"""La galerie des 78 croquis ajoutés au lexique de Compostelle le 26 sept. 2026.

    python3 build/compostelle_dessins.py   # → assets/presentations/compostelle-dessins.html

Demande de Daniel : « une page pour voir tous les nouveaux dessins ». Les
nouveaux sont les sujets écrits après le mot `etapa` dans sujets.py (le bloc
« les mots sans objet »). Classés par planche, comme dans l'application ;
un toucher agrandit le dessin.
"""
import html, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-dessins.html"
MEDIA = "../interactive/compostelle/croquis/"
E = html.escape
FAMILLES = {"objet": "objet", "scene": "scène", "corps": "corps", "geste": "geste"}


def main():
    LX, SJ = C.charger("lexique"), C.charger("sujets")
    cles = list(SJ.SUJETS)
    neufs = set(cles[cles.index("etapa"):])
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — les nouveaux dessins</title>", tete)
    tete = tete.replace("</head>", """<style>
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px}
.gal button{all:unset;cursor:pointer;display:block;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}
.gal button:focus-visible{outline:3px solid #0A8F5B;outline-offset:2px}
.gal img{display:block;width:100%;aspect-ratio:1/1;object-fit:contain;background:#fff}
.gal .leg{padding:8px 10px 10px;border-top:1px solid var(--line)}
.gal .es{display:block;font-weight:800;color:var(--body);line-height:1.25}
.gal .fr{display:block;font-size:13px;color:var(--muted);line-height:1.3;margin-top:2px}
.gal .fam{display:inline-block;margin-top:6px;font-size:11px;font-weight:800;letter-spacing:.04em;text-transform:uppercase;color:#6b5a2a;background:#fbf3dc;border-radius:99px;padding:2px 8px}
@media (max-width:420px){.gal{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}}
dialog{border:0;border-radius:12px;padding:0;max-width:min(92vw,720px);width:100%;background:var(--card);color:var(--body)}
dialog img{background:#fff}
dialog::backdrop{background:rgba(20,20,20,.72)}
dialog img{display:block;width:100%;height:auto}
dialog .leg{padding:12px 16px 16px}
dialog .es{font-weight:800;font-size:20px}
dialog .fr{color:var(--muted)}
dialog .sujet{font-size:13px;color:var(--muted);margin-top:8px;font-style:italic}
dialog form{position:absolute;top:8px;right:8px}
dialog form button{background:#fff;border:1px solid var(--line);border-radius:99px;width:36px;height:36px;font-size:20px;cursor:pointer}
</style>
</head>""")
    secs, n = [], 0
    for pid, nom_fr, nom_es in LX.PLANCHES:
        mots = [e for e in LX.LEXIQUE if e[1] == pid and e[0] in neufs]
        if not mots:
            continue
        cartes = []
        for i, pl, es, fr, dessin, note in mots:
            fam, sujet = SJ.SUJETS[i]
            n += 1
            cartes.append(
                f'<button type="button" data-img="{MEDIA}{i}.jpg" data-es="{E(es)}" data-fr="{E(fr)}" data-sujet="{E(sujet)}">'
                f'<img src="{MEDIA}{i}.jpg" alt="{E(fr)}" loading="lazy">'
                f'<span class="leg"><span class="es">{E(es)}</span><span class="fr">{E(fr)}</span>'
                f'<span class="fam">{FAMILLES[fam]}</span></span></button>')
        secs.append(f'<section><h2>{E(nom_fr)} <span style="color:var(--muted);font-weight:600">· {E(nom_es)} · {len(mots)}</span></h2>'
                    f'<div class="gal">{"".join(cartes)}</div></section>')
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; les nouveaux dessins</h1>
<p class="chapeau">Les <strong>{n} croquis</strong> ajoutés le 26 septembre 2026 aux mots qui n'avaient pas d'image : repas,
allergènes, heures, politesse, questions entre pèlerins. Classés par planche, comme dans l'application. Touchez un dessin pour
l'agrandir et lire ce qui a été demandé au modèle.</p>
<p style="font-size:14px;color:var(--muted)">Quatre familles : <b>objet</b> (la chose seule), <b>scène</b> (un lieu, un moment),
<b>corps</b> (la partie en rouge), <b>geste</b> (une ou deux personnes : le sens tient au geste — ce sont eux qu'il faut regarder
de près). Sept ont été refaits après inspection : du texte dans l'image ou un fond de papier gris.</p>
{"".join(secs)}
</div>
<dialog id="grand"><form method="dialog"><button aria-label="Fermer">&times;</button></form>
<img alt=""><div class="leg"><div class="es"></div><div class="fr"></div><div class="sujet"></div></div></dialog>
<script>
const d = document.getElementById('grand');
document.querySelectorAll('.gal button').forEach(b => b.addEventListener('click', () => {{
  d.querySelector('img').src = b.dataset.img;
  d.querySelector('img').alt = b.dataset.fr;
  d.querySelector('.es').textContent = b.dataset.es;
  d.querySelector('.fr').textContent = b.dataset.fr;
  d.querySelector('.sujet').textContent = 'Demandé : ' + b.dataset.sujet;
  d.showModal();
}}));
d.addEventListener('click', e => {{ if (e.target === d) d.close(); }});
</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {n} dessins")


if __name__ == "__main__":
    main()
