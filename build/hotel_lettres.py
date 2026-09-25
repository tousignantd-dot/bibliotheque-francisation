#!/usr/bin/env python3
"""Les lettres de l'alphabet, une à une, dans les trois langues — à valider à l'oreille.

    python3 build/hotel_lettres.py          # produit ce qui manque, puis la page d'écoute

POURQUOI : faire épeler un nom entier à la voix HD a raté 7 noms sur 8 en
français à l'écoute de Daniel (25 sept. 2026) ; en espagnol, le Y. La HD choisit
sa langue mot à mot et n'est pas déterministe. On enregistre donc chaque lettre
SEULE, de deux façons, Daniel choisit la bonne, et les noms s'ASSEMBLENT ensuite
à partir des lettres validées (build/hotel_audio.py) : exact, et le rythme se
règle au montage.

  a — le nom de la lettre écrit dans la langue (« emme », « erre », « i griega ») ;
  b — la lettre nue en <say-as interpret-as="characters">.

Sortie : assets/interactive/hotel/sons/x/lettres/<langue>/<L>-<a|b>.mp3 et
assets/presentations/hotel-lettres.html (produite, jamais éditée).
"""
import html, importlib.util, pathlib, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
_s = importlib.util.spec_from_file_location("hotel_audio", RACINE / "build/hotel_audio.py")
HA = importlib.util.module_from_spec(_s); _s.loader.exec_module(HA)
EX = HA.EX
DEST = HA.SONS / "x" / "lettres"
PAGE = RACINE / "assets" / "presentations" / "hotel-lettres.html"
NOM_L = {"fr": "Français — Thierry", "es": "Espagnol — Jorge", "en": "Anglais — Andrew"}


def taches():
    for l in ("fr", "es", "en"):
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            yield l, c, "a", html.escape(EX.LETTRES[l][c])
            yield l, c, "b", f'<say-as interpret-as="characters">{c}</say-as>'


def page():
    lignes = ""
    for l in ("fr", "es", "en"):
        lignes += f"<h2>{NOM_L[l]}</h2><table>"
        for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            ecrit = html.escape(EX.LETTRES[l][c])
            lecteurs = "".join(
                f'<td><span class="lab">{v.upper()}</span><audio controls preload="none" src="/assets/interactive/hotel/sons/x/lettres/{l}/{c}-{v}.mp3"></audio></td>'
                for v in ("a", "b"))
            lignes += (f'<tr><td class="L"><b>{c}</b><br><small>a = « {ecrit} »</small></td>{lecteurs}'
                       f'<td><div class="v" data-k="{l}:{c}"><button data-v="a">A</button><button data-v="b">B</button>'
                       f'<button data-v="aucune">Aucune</button></div></td></tr>')
        lignes += "</table>"
    PAGE.write_text(f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Les lettres épelées</title>
<style>body{{font-family:Nunito,system-ui,sans-serif;max-width:980px;margin:0 auto;padding:16px;background:#fff;color:#17181A}}
table{{width:100%;border-collapse:collapse}}td{{padding:6px;border-bottom:1px solid #ddd;vertical-align:middle}}td.L{{width:110px}}
small{{color:#555}}audio{{width:180px;height:34px;vertical-align:middle}}.lab{{font-weight:800;margin-right:4px}}
button{{font:inherit;font-weight:700;cursor:pointer;border:1px solid #bbb;background:#f5f5f3;border-radius:10px;padding:6px 10px;min-height:40px}}
.v{{display:flex;gap:12px}}.v button[aria-pressed=true]{{background:#DCF2E6;border-color:#0A8F5B}}
.v button[aria-pressed=true][data-v=aucune]{{background:#FBEEDC;border-color:#B45309}}
#exporter{{background:#0A8F5B;color:#fff;border-color:#0A8F5B}}
@media (max-width:700px){{table,tr,td{{display:block}}td{{border:0}}tr{{border-bottom:1px solid #ddd;padding:8px 0}}audio{{width:100%}}}}</style></head>
<body><h1>Les lettres, une à une</h1>
<p>Chaque lettre est dite de deux façons : <b>A</b>, son nom écrit dans la langue (« emme ») ; <b>B</b>, la lettre seule,
laissée à la voix. Choisissez celle qui est juste — ou « Aucune ». Les noms épelés seront ensuite <b>assemblés</b>
à partir des lettres choisies : plus de surprise d'un nom à l'autre.</p>
<p>Les lettres que vous ne marquez pas gardent la façon A, si elle vous a paru juste dans les noms.</p>
{lignes}
<p style="margin-top:24px">Un mot (facultatif) :</p><textarea id="note" rows="3" style="width:100%;font:inherit"></textarea>
<p><button id="exporter">Exporter mes choix</button> <span id="etat"></span></p>
<script>
(function(){{var C='hotel-lettres',s={{}};try{{s=JSON.parse(localStorage.getItem(C)||'{{}}')}}catch(e){{}}
var n=document.getElementById('note');n.value=s.__note||'';n.oninput=function(){{s.__note=n.value;sv()}};
function sv(){{try{{localStorage.setItem(C,JSON.stringify(s))}}catch(e){{}}}}
function p(){{document.querySelectorAll('.v').forEach(function(d){{d.querySelectorAll('button').forEach(function(b){{b.setAttribute('aria-pressed',s[d.dataset.k]===b.dataset.v)}})}});
 document.getElementById('etat').textContent=(Object.keys(s).length-(s.__note!==undefined?1:0))+' lettres marquées sur 78';}}
document.addEventListener('click',function(e){{var b=e.target.closest('.v button');if(!b)return;var k=b.parentNode.dataset.k;if(s[k]===b.dataset.v)delete s[k];else s[k]=b.dataset.v;sv();p();}});
document.getElementById('exporter').onclick=function(){{var o={{page:'hotel-lettres',choix:{{}},note:s.__note||''}};Object.keys(s).forEach(function(k){{if(k!=='__note')o.choix[k]=s[k]}});
 var t=JSON.stringify(o,null,2);(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{document.getElementById('etat').textContent='Copié — recolle-le-moi.'}},function(){{prompt('Copiez :',t)}});}};
p();}})();
</script></body></html>''', encoding="utf-8")


if __name__ == "__main__":
    cle, region = HA.cle_region()
    a_faire = [t for t in taches() if not (DEST / t[0] / f"{t[1]}-{t[2]}.mp3").exists()]
    import subprocess

    def duree(f):
        return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                     "-of", "csv=p=0", str(f)], capture_output=True, text=True).stdout or 0)

    def une(t):
        # La HD déraille parfois sur une lettre seule : 12 s, 31 s de bruit ou de
        # répétition (K espagnol, K et I français, 25 sept. 2026). Une lettre
        # dure moins d'une seconde et demie ; au-delà de 2,5 s, on la refait.
        f = DEST / t[0] / f"{t[1]}-{t[2]}.mp3"
        for _ in range(4):
            HA.synth(t[0], t[3], f, cle, region, HA.VOIX_CLIENTS[t[0]], "0%", True)
            if duree(f) <= 2.5:
                return
        print(f"  {f.name} ({t[0]}) reste à {duree(f):.1f} s après quatre tirages")

    # Les lettres déjà sur le disque mais aberrantes repassent aussi.
    a_faire += [t for t in taches() if (DEST / t[0] / f"{t[1]}-{t[2]}.mp3").exists()
                and duree(DEST / t[0] / f"{t[1]}-{t[2]}.mp3") > 2.5]
    with ThreadPoolExecutor(6) as pool:
        list(pool.map(une, a_faire))
    page()
    print(f"{len(a_faire)} lettres produites ; {PAGE.relative_to(RACINE)}")
