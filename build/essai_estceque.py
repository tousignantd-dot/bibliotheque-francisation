#!/usr/bin/env python3
"""Page d'écoute : tous les « est-ce que » enregistrés dans les modules.

ElevenLabs découpe parfois « est-ce que » en trois morceaux au lieu de le
lire comme un seul mot (/ɛskə/). Cette page rassemble, module par module,
chaque MP3 déjà produit dont le texte contient la locution, pour qu'on
puisse repérer à l'oreille lesquels sont saccadés.

Le texte lu ne vit pas au même endroit selon le son, et il faut les trois
sources pour ne rien manquer :

  · sons_module_<slug>.json ........ manifeste des sons d'un module récent
  · generer_audio_module_<slug>{,_plus,_sons}.py .. dict CLIPS des modules
      plus anciens, qui n'ont jamais eu de manifeste (consultation, meteo,
      travail, urgence, sante, pub, logement, banque, nouvelles, procedure)
  · DIALOGUES dans ces mêmes scripts et dans generer_audio_dialogues.py ..
      les répliques, rangées hors de sons/ en <module>/<bloc>/line_NN_x.mp3

Les scripts sont lus par `ast`, jamais importés : aucune clé d'API en jeu.

    python3 build/essai_estceque.py

Écrit essai-estceque.html à la racine. Ne touche à aucun module.
"""
import ast
import glob
import html
import json
import os
import re
import unicodedata

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOCUTION = re.compile(r"(est-ce\s+qu[a-zéêè’']*)", re.I)


def titres():
    """slug de module -> (titre, niveau), lu du catalogue."""
    out = {}
    chemin = os.path.join(RACINE, "data", "activities.json")
    with open(chemin, encoding="utf-8") as f:
        for a in json.load(f):
            inter = a.get("interactive") or ""
            m = re.search(r"assets/interactive/([^/]+)/", inter)
            if m:
                out[m.group(1)] = (a.get("title") or m.group(1), a.get("level") or "")
    return out


def _slug_module(chemin):
    """generer_audio_module_n3_poste_plus.py -> module-n3-poste"""
    nom = os.path.basename(chemin)[len("generer_audio_module_"):-len(".py")]
    for suffixe in ("_plus", "_sons"):
        if nom.endswith(suffixe):
            nom = nom[: -len(suffixe)]
    return "module-" + nom.replace("_", "-")


def _litteraux(chemin, noms):
    """Les dicts de haut niveau nommés `noms`, lus sans exécuter le script."""
    with open(chemin, encoding="utf-8") as f:
        arbre = ast.parse(f.read(), filename=chemin)
    out = {}
    for noeud in arbre.body:
        if not isinstance(noeud, ast.Assign):
            continue
        for cible in noeud.targets:
            if isinstance(cible, ast.Name) and cible.id in noms:
                try:
                    out[cible.id] = ast.literal_eval(noeud.value)
                except ValueError:
                    pass
    return out


def _slugs_personnage(nom):
    """Les deux règles de nommage en usage : avec et sans accents retirés."""
    brut = nom.lower().replace(" ", "_")
    sans = unicodedata.normalize("NFD", nom.lower())
    sans = "".join(c for c in sans if unicodedata.category(c) != "Mn")
    sans = sans.replace("'", "").replace(" ", "_")
    return [sans, brut]


def _des_manifestes():
    for f in sorted(glob.glob(os.path.join(RACINE, "sons_module_*.json"))):
        base = os.path.basename(f)
        slug = "module-" + base[len("sons_module_"):-len(".json")].replace("_", "-")
        with open(f, encoding="utf-8") as fh:
            sons = json.load(fh)
        for sid, texte in sons.items():
            if isinstance(texte, str):
                yield slug, f"assets/interactive/{slug}/sons/{sid}.mp3", sid, texte


def _des_scripts():
    motifs = ["generer_audio_module_*.py", "generer_audio_dialogues.py"]
    for motif in motifs:
        for f in sorted(glob.glob(os.path.join(RACINE, motif))):
            trouve = _litteraux(f, {"CLIPS", "DIALOGUES"})

            for sid, texte in (trouve.get("CLIPS") or {}).items():
                if isinstance(texte, str):
                    slug = _slug_module(f)
                    yield slug, f"assets/interactive/{slug}/sons/{sid}.mp3", sid, texte

            for dial_id, data in (trouve.get("DIALOGUES") or {}).items():
                # Selon le script, la valeur est {"lines": [...]} ou la
                # liste des répliques elle-même.
                lignes = data.get("lines") if isinstance(data, dict) else data
                lignes = lignes or []
                slug = dial_id.split("/")[0]
                for i, ligne in enumerate(lignes, 1):
                    if not (isinstance(ligne, (list, tuple)) and len(ligne) >= 2):
                        continue
                    perso, texte = ligne[0], ligne[1]
                    if not isinstance(texte, str):
                        continue
                    rel = None
                    for s_perso in _slugs_personnage(perso):
                        essai = f"assets/interactive/{dial_id}/line_{i:02d}_{s_perso}.mp3"
                        if os.path.exists(os.path.join(RACINE, essai)):
                            rel = essai
                            break
                    if rel is None:
                        rel = (f"assets/interactive/{dial_id}/"
                               f"line_{i:02d}_{_slugs_personnage(perso)[0]}.mp3")
                    yield slug, rel, f"{dial_id.split('/')[-1]} · {perso}", texte


def releve():
    """[(slug, chemin mp3, étiquette, texte, existe)] pour chaque son visé.

    Un même MP3 peut être décrit par deux sources (manifeste et script) :
    le chemin sert de clé, la première description gagne.
    """
    vus = {}
    for source in (_des_manifestes(), _des_scripts()):
        for slug, rel, etiq, texte in source:
            if not LOCUTION.search(texte) or rel in vus:
                continue
            vus[rel] = (slug, rel, etiq, texte,
                        os.path.exists(os.path.join(RACINE, rel)))
    return sorted(vus.values(), key=lambda r: (r[0], r[1]))


def surligne(texte):
    return LOCUTION.sub(lambda m: f"<mark>{html.escape(m.group(1))}</mark>",
                        html.escape(texte))


CSS = """
 :root{--enc:#e4e9ee;--gris:#5b6672;--fond:#fafcfd}
 *{box-sizing:border-box}
 body{background:#fff;color:#101418;margin:0;padding:26px 22px 70px;
      max-width:1000px;font:16px/1.55 -apple-system,"Segoe UI",Roboto,sans-serif}
 h1{font-size:22px;margin:0 0 8px}
 h2{font-size:16px;margin:30px 0 4px;padding-top:16px;border-top:1px solid var(--enc)}
 h2 span{font-weight:400;color:var(--gris);font-size:13px}
 p.intro{color:var(--gris);margin:0 0 18px}
 .rappel{background:#fbf7ee;border-left:3px solid #B8860B;padding:11px 15px;margin:0 0 20px;font-size:14px}
 .barre{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:0 0 18px;
        padding:11px 14px;border:1px solid var(--enc);border-radius:8px;background:var(--fond)}
 .barre label{font-size:13px;color:var(--gris)}
 input[type=search]{flex:1;min-width:180px;padding:7px 10px;border:1px solid var(--enc);
        border-radius:6px;font:inherit;font-size:14px}
 .son{display:grid;grid-template-columns:minmax(0,1fr) 260px;gap:14px;align-items:center;
      padding:10px 12px;border:1px solid var(--enc);border-radius:8px;background:var(--fond);
      margin:0 0 8px}
 .son.attente{opacity:.55;background:#fff}
 .txt{font-size:15px;min-width:0}
 mark{background:#ffe9a8;padding:1px 2px;border-radius:3px}
 .id{display:block;font-size:11.5px;color:var(--gris);margin-top:3px;font-family:ui-monospace,Menlo,monospace}
 audio{height:34px;width:100%}
 .vide{font-size:12.5px;color:var(--gris);text-align:center}
 .bilan{font-size:13.5px;color:var(--gris);margin:22px 0 0;padding-top:14px;border-top:1px solid var(--enc)}
 @media (max-width:640px){.son{grid-template-columns:1fr}}
"""

JS = """
 const champ = document.getElementById('filtre');
 const seulAudio = document.getElementById('seul');
 function filtrer(){
   const q = champ.value.trim().toLowerCase();
   document.querySelectorAll('section').forEach(sec => {
     let visibles = 0;
     sec.querySelectorAll('.son').forEach(el => {
       const ok = (!q || el.dataset.t.includes(q))
               && (!seulAudio.checked || el.dataset.a === '1');
       el.hidden = !ok; if (ok) visibles++;
     });
     sec.hidden = visibles === 0;
   });
 }
 champ.addEventListener('input', filtrer);
 seulAudio.addEventListener('change', filtrer);
 filtrer();  // la case est cochée au chargement : on applique tout de suite.
 // Une seule lecture à la fois : on compare vite en enchaînant.
 document.addEventListener('play', e => {
   document.querySelectorAll('audio').forEach(a => { if (a !== e.target) a.pause(); });
 }, true);
"""


def main():
    noms = titres()
    lignes = releve()
    avec = [l for l in lignes if l[4]]
    modules = sorted({l[0] for l in lignes},
                     key=lambda s: (0 if any(x[0] == s and x[4] for x in lignes) else 1, s))

    out = ["<!doctype html>", '<html lang="fr"><head><meta charset="utf-8">',
           '<meta name="viewport" content="width=device-width,initial-scale=1">',
           "<title>Est-ce que — écoute</title>", f"<style>{CSS}</style></head><body>",
           "<h1>« Est-ce que » dans les modules</h1>",
           '<p class="intro">Chaque phrase déjà enregistrée qui contient la locution, '
           'module par module — répliques de dialogue, mots isolés et mini-leçons. '
           'La locution est surlignée dans le texte.</p>',
           '<div class="rappel"><strong>Ce qu\'on cherche :</strong> « est-ce que » doit '
           's\'entendre comme un seul mot, <em>èss-ke</em>, en une seule émission. '
           'Notez les extraits où les trois morceaux se détachent — '
           '« est · ce · que » — pour qu\'on les régénère.</div>',
           '<div class="barre"><label for="filtre">Chercher</label>'
           '<input type="search" id="filtre" placeholder="un mot de la phrase…">'
           '<label><input type="checkbox" id="seul" checked> seulement ce qui a un MP3</label>'
           "</div>"]

    for slug in modules:
        titre, niveau = noms.get(slug, (slug, ""))
        sons = [l for l in lignes if l[0] == slug]
        n_audio = sum(1 for l in sons if l[4])
        etiq = f"{n_audio} extrait{'s' if n_audio > 1 else ''}" if n_audio else "audio pas encore produit"
        out.append(f"<section><h2>{html.escape(titre)} "
                   f"<span>· {html.escape(niveau)} · {etiq} · {len(sons)} phrase"
                   f"{'s' if len(sons) > 1 else ''}</span></h2>")
        for _, rel, ident, texte, ok in sons:
            lecteur = (f'<audio controls preload="none" src="{rel}"></audio>' if ok
                       else '<div class="vide">MP3 pas encore produit</div>')
            out.append(f'<div class="son{"" if ok else " attente"}" '
                       f'data-t="{html.escape(texte.lower(), quote=True)}" data-a="{1 if ok else 0}">'
                       f'<div class="txt">{surligne(texte)}'
                       f'<span class="id">{html.escape(ident)}</span></div>'
                       f"{lecteur}</div>")
        out.append("</section>")

    out.append(f'<p class="bilan">{len(lignes)} phrases contiennent « est-ce que » dans '
               f'{len(modules)} modules ; {len(avec)} sont déjà enregistrées, '
               f'{len(lignes) - len(avec)} attendent leur audio.</p>')
    out.append(f"<script>{JS}</script></body></html>")

    dest = os.path.join(RACINE, "essai-estceque.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"{dest} — {len(lignes)} phrases, {len(avec)} avec MP3, {len(modules)} modules")


if __name__ == "__main__":
    main()
