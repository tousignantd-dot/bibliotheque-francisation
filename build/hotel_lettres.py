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

    python3 build/hotel_lettres.py --reprises   # les lettres « Aucune » : cinq candidats de plus
    python3 build/hotel_lettres.py --noms       # page d'écoute des noms assemblés

Reprises (HA.LETTRES_A_REPRENDRE, écoute du 27 sept. 2026) : c = nouveau tirage HD
du nom écrit ; d = HD, autre graphie ; e = voix neurale (non HD, déterministe), nom
écrit ; f = neurale, lettre nue ; g = neurale, phonème API. Page :
assets/presentations/hotel-lettres-reprises.html ; le choix va dans CHOIX_LETTRES.
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


HP_V = "12"   # = MEDIA_V de hotel_planches.py au dernier assemblage
NEURALE = {"fr": "fr-CA-ThierryNeural", "en": "en-US-AndrewNeural", "es": "es-MX-JorgeNeural"}
AUTRE_GRAPHIE = {"fr:A": "ah", "fr:I": "î", "fr:Q": "cu", "fr:R": "ère", "fr:T": "thé",
                 "en:M": "em", "en:V": "vee"}
API = {"fr:A": "a", "fr:I": "i", "fr:Q": "ky", "fr:R": "ɛʁ", "fr:T": "te",
       "en:M": "ɛm", "en:V": "viː"}
PAGE_R = RACINE / "assets" / "presentations" / "hotel-lettres-reprises.html"
QUOI = {"c": "nouveau tirage, nom écrit", "d": "autre graphie", "e": "voix neurale, nom écrit",
        "f": "voix neurale, lettre nue", "g": "voix neurale, phonème"}


def taches_reprises():
    """(langue, lettre, variante, ssml, voix)"""
    for k in HA.LETTRES_A_REPRENDRE:
        l, c = k.split(":")
        hd, nr = HA.VOIX_CLIENTS[l], NEURALE[l]
        yield l, c, "c", html.escape(EX.LETTRES[l][c]), hd
        yield l, c, "d", html.escape(AUTRE_GRAPHIE[k]), hd
        yield l, c, "e", html.escape(EX.LETTRES[l][c]), nr
        yield l, c, "f", f'<say-as interpret-as="characters">{c}</say-as>', nr
        yield l, c, "g", f'<phoneme alphabet="ipa" ph="{API[k]}">{c}</phoneme>', nr


def page_reprises():
    lignes = ""
    for k in HA.LETTRES_A_REPRENDRE:
        l, c = k.split(":")
        lect = "".join(
            f'<div class="c"><span class="lab">{v.upper()}</span> <small>{QUOI[v]}'
            f'{" « " + html.escape(AUTRE_GRAPHIE[k]) + " »" if v == "d" else ""}</small><br>'
            f'<audio controls preload="none" src="/assets/interactive/hotel/sons/x/lettres/{l}/{c}-{v}.mp3"></audio></div>'
            for v in "cdefg")
        boutons = "".join(f'<button data-v="{v}">{v.upper()}</button>' for v in "cdefg")
        lignes += (f'<section><h2>{NOM_L[l].split(" —")[0]} · <b>{c}</b></h2><div class="g">{lect}</div>'
                   f'<div class="v" data-k="{k}">{boutons}<button data-v="aucune">Aucune</button></div></section>')
    PAGE_R.write_text(f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lettres à reprendre</title>
<style>body{{font-family:Nunito,system-ui,sans-serif;max-width:980px;margin:0 auto;padding:16px;background:#fff;color:#17181A}}
section{{border-bottom:1px solid #ddd;padding:10px 0 14px}}h2{{font-size:1.1rem;margin:6px 0}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px}}.c small{{color:#555}}
audio{{width:100%;height:34px}}.lab{{font-weight:800}}
button{{font:inherit;font-weight:700;cursor:pointer;border:1px solid #bbb;background:#f5f5f3;border-radius:10px;padding:6px 12px;min-height:40px}}
.v{{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}}.v button[aria-pressed=true]{{background:#DCF2E6;border-color:#0A8F5B}}
.v button[aria-pressed=true][data-v=aucune]{{background:#FBEEDC;border-color:#B45309}}
#exporter{{background:#0A8F5B;color:#fff;border-color:#0A8F5B}}</style></head>
<body><h1>Les sept lettres à reprendre</h1>
<p>Vous avez refusé A et B pour ces lettres. Voici cinq autres façons de les dire. <b>C</b> et <b>D</b> gardent la voix
des noms (HD) ; <b>E</b>, <b>F</b> et <b>G</b> passent par la voix neurale du même comédien, plus stable, mais d'un timbre
un peu différent : écoutez-la aussi dans son rang, entre deux lettres HD, avant de la retenir.</p>
{{lignes}}
<p style="margin-top:24px">Un mot (facultatif) :</p><textarea id="note" rows="3" style="width:100%;font:inherit"></textarea>
<p><button id="exporter">Exporter mes choix</button> <span id="etat"></span></p>
<script>
(function(){{var C='hotel-lettres-reprises',s={{}};try{{s=JSON.parse(localStorage.getItem(C)||'{{}}')}}catch(e){{}}
var n=document.getElementById('note');n.value=s.__note||'';n.oninput=function(){{s.__note=n.value;sv()}};
function sv(){{try{{localStorage.setItem(C,JSON.stringify(s))}}catch(e){{}}}}
function p(){{document.querySelectorAll('.v').forEach(function(d){{d.querySelectorAll('button').forEach(function(b){{b.setAttribute('aria-pressed',s[d.dataset.k]===b.dataset.v)}})}});
 document.getElementById('etat').textContent=(Object.keys(s).length-(s.__note!==undefined?1:0))+' lettres marquées sur {len(HA.LETTRES_A_REPRENDRE)}';}}
document.addEventListener('click',function(e){{var b=e.target.closest('.v button');if(!b)return;var k=b.parentNode.dataset.k;if(s[k]===b.dataset.v)delete s[k];else s[k]=b.dataset.v;sv();p();}});
document.getElementById('exporter').onclick=function(){{var o={{page:'hotel-lettres-reprises',choix:{{}},note:s.__note||''}};Object.keys(s).forEach(function(k){{if(k!=='__note')o.choix[k]=s[k]}});
 var t=JSON.stringify(o,null,2);(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){{document.getElementById('etat').textContent='Copié — recolle-le-moi.'}},function(){{prompt('Copiez :',t)}});}};
p();}})();
</script></body></html>'''.replace("{lignes}", lignes), encoding="utf-8")


PAGE_N = RACINE / "assets" / "presentations" / "hotel-noms-epeles.html"


def page_noms():
    """Les noms tels qu'ils sortent de l'assemblage : exercices, puis test (partie B)."""
    s = importlib.util.spec_from_file_location("hotel_test", RACINE / "build/contenu/entreprise-hotel/test.py")
    T = importlib.util.module_from_spec(s); s.loader.exec_module(T)
    racine = "/assets/interactive/hotel/sons/"
    lignes = ""
    for l in ("fr", "en", "es"):
        lignes += f"<h2>{NOM_L[l].split(' —')[0]}</h2><table>"
        for nom in EX.NOMS:
            lignes += (f'<tr><td class="L">{html.escape(nom)}{" <small>(téléphone)</small>" if nom in EX.TELEPHONE else ""}'
                       f'<br><small>exercices</small></td><td><audio controls preload="none" '
                       f'src="{racine}x/epeler/{l}/{HA.slug_nom(nom)}.mp3?v={HP_V}"></audio></td></tr>')
        for forme in (1, 2):
            for item in T.B[forme]:
                if item[1] == "nom":
                    lignes += (f'<tr><td class="L">{html.escape(item[2])}<br><small>test, forme {forme}</small></td>'
                               f'<td><audio controls preload="none" src="{racine}test/b/{l}/{item[0]}.mp3?v={HP_V}"></audio></td></tr>')
        lignes += "</table>"
    PAGE_N.write_text(f'''<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Noms épelés assemblés</title>
<style>body{{font-family:Nunito,system-ui,sans-serif;max-width:760px;margin:0 auto;padding:16px;background:#fff;color:#17181A}}
table{{width:100%;border-collapse:collapse}}td{{padding:6px;border-bottom:1px solid #ddd;vertical-align:middle}}td.L{{width:45%;font-weight:700}}
small{{color:#555;font-weight:400}}audio{{width:100%;height:34px}}</style></head>
<body><h1>Les noms épelés, assemblés</h1>
<p>Chaque nom est maintenant monté à partir des lettres que vous avez choisies à l'oreille (27 septembre 2026).
Si un nom sonne faux, dites-moi lequel et dans quelle langue : on remontera à la lettre en cause.</p>
{{lignes}}</body></html>'''.replace("{lignes}", lignes), encoding="utf-8")


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

    if "--noms" in sys.argv:
        page_noms(); print(PAGE_N.relative_to(RACINE)); sys.exit(0)
    if "--reprises" in sys.argv:
        faire = [t for t in taches_reprises() if not (DEST / t[0] / f"{t[1]}-{t[2]}.mp3").exists()]

        def reprise(t):
            f = DEST / t[0] / f"{t[1]}-{t[2]}.mp3"
            for _ in range(4):
                HA.synth(t[0], t[3], f, cle, region, t[4], "0%", True)
                if duree(f) <= 2.5:
                    return
            print(f"  {f.name} ({t[0]}) reste à {duree(f):.1f} s")
        with ThreadPoolExecutor(6) as pool:
            list(pool.map(reprise, faire))
        page_reprises()
        print(f"{len(faire)} candidats ; {PAGE_R.relative_to(RACINE)}")
        sys.exit(0)
    # Les lettres déjà sur le disque mais aberrantes repassent aussi.
    a_faire += [t for t in taches() if (DEST / t[0] / f"{t[1]}-{t[2]}.mp3").exists()
                and duree(DEST / t[0] / f"{t[1]}-{t[2]}.mp3") > 2.5]
    with ThreadPoolExecutor(6) as pool:
        list(pool.map(une, a_faire))
    page()
    print(f"{len(a_faire)} lettres produites ; {PAGE.relative_to(RACINE)}")
