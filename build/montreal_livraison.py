#!/usr/bin/env python3
"""La page de livraison de « Montréal en poche », au classeur.

    python3 build/montreal_livraison.py   # → assets/presentations/montreal-livraison.html

Ce qui a été bâti, ce qui a été décidé à la place de Daniel (et se renverse),
les faits qui restent à vérifier (relevés dans les listes `verifier` du
contenu, jamais recopiés), et l'audioguide à écouter : les trois langues de
chaque lieu, côte à côte.
"""
import html, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build")); sys.path.insert(0, str(RACINE))
import montreal_commun as M  # noqa: E402
from qr import svg as qr_svg  # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "montreal-livraison.html"
URL = "https://portail.edufrancis.ca/modules-autonomes/montreal/"
E = html.escape
CAT = {"voir": "À voir", "quartier": "Quartier", "manger": "Manger", "boire": "Café, bière"}

DECISIONS = [
    ("Le nom", "« Montréal en poche » · Montreal in Your Pocket · Montreal en el bolsillo. Sans la barre francis : ce n'est pas un produit d'apprentissage."),
    ("Les langues", "Français, anglais, espagnol. Chaque langue est écrite pour son lecteur, pas traduite mot à mot. L'espagnol est celui d'Amérique latine (usted), compréhensible en Espagne."),
    ("Les voix", "Azure HD : Sylvie (fr-CA — la ville parle québécois), Emma (anglais), Dalia (es-MX). Environ une minute par lieu."),
    ("Les 28 lieux", "13 à voir, 3 quartiers, 8 pour manger (smoked meat, bagels, poutine, Wilensky's, Orange Julep, Romados, deux marchés), 4 cafés et bières."),
    ("Le côté ludique", "Un passeport à tampons, comme la credencial : l'utilisateur tamponne lui-même le lieu visité (« J'y suis allé »), sans contrôle de position."),
    ("La carte", "Leaflet et OpenStreetMap, chargés en ligne. « Autour de moi » trie les lieux par distance ; la position ne quitte jamais le téléphone."),
    ("Les couleurs", "Crème, encre et rouge — le rouge de la croix du drapeau de Montréal. Chaque genre de lieu a sa couleur ET son mot."),
    ("En ligne", "Mise en ligne le 30 septembre 2026, à votre demande. Page non indexée (noindex) et liée de nulle part : on y entre par l'adresse ou le code QR."),
]


def main():
    lieux = M.lieux()
    ex = M.charger("extras")
    audio = M.MEDIA / "audio"
    sons = sum((audio / g / f"{l['id']}.mp3").exists() for l in lieux for g in M.LANGUES)
    mots_sons = sum((audio / "mots" / f"{i:02d}.mp3").exists() for i in range(len(ex.MOTS)))
    scenes = M.scenes()
    fam = M.enfants()
    a_verifier = [(l, v) for l in lieux for v in l.get("verifier", [])]
    a_verifier += [({"nom": {"fr": "Circuits et guide pratique"}}, v) for v in getattr(ex, "VERIFIER", [])]

    rangs = []
    for l in lieux:
        cells = "".join(
            f'<td><audio controls preload="none" src="/assets/interactive/montreal/audio/{g}/{l["id"]}.mp3?v=1"></audio></td>'
            if (audio / g / f"{l['id']}.mp3").exists() else "<td class=manque>à produire</td>"
            for g in M.LANGUES)
        rangs.append(f'<tr><th><img src="/assets/interactive/montreal/lieux/{l["id"]}.jpg" alt="" loading="lazy">'
                     f'<span>{E(l["nom"]["fr"])}<small>{CAT[l["cat"]]}</small></span></th>{cells}</tr>')
    ver = "".join(f"<li><b>{E(l['nom']['fr'])}</b> — {E(v)}</li>" for l, v in a_verifier) or "<li>Rien : tout a été vérifié.</li>"
    dec = "".join(f"<div class=dec><h3>{E(t)}</h3><p>{E(p)}</p></div>" for t, p in DECISIONS)

    page = f"""<!doctype html>
<html lang="fr-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Montréal en poche — la livraison</title>
<link rel="stylesheet" href="/assets/design-system/tokens/fonts.css">
<style>
:root{{--fond:#F6F1E7;--carte:#fff;--encre:#1E2733;--doux:#5D6572;--filet:#E2D9C6;--rouge:#B3262E}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--fond);color:var(--encre);font:17px/1.55 Nunito,system-ui,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:28px 16px 60px}}
.eyebrow{{font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--rouge)}}
h1{{font-size:36px;line-height:1.1;margin:6px 0 10px;letter-spacing:-.02em}}
h2{{font-size:24px;margin:40px 0 12px}}
.lead{{font-size:19px;color:var(--doux);max-width:760px}}
.chiffres{{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:22px 0}}
.chiffres div{{background:var(--carte);border-radius:14px;padding:14px 16px}}
.chiffres b{{display:block;font-size:30px;font-weight:900}}
.chiffres span{{color:var(--doux);font-size:15px}}
.qr{{display:grid;grid-template-columns:200px minmax(0,1fr);gap:22px;align-items:center;background:var(--carte);border-radius:14px;padding:20px}}
.qr svg{{width:100%;height:auto}}
@media (max-width:640px){{.qr{{grid-template-columns:1fr}}.qr svg{{max-width:220px}}}}
.btn{{display:inline-block;background:var(--rouge);color:#fff;text-decoration:none;font-weight:900;padding:12px 18px;border-radius:12px;margin:6px 8px 0 0}}
.btn.sec{{background:#fff;color:var(--encre);border:2px solid var(--encre)}}
.decs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}
.dec{{background:var(--carte);border-radius:14px;padding:14px 16px}}
.dec h3{{margin:0 0 4px;font-size:16px}}.dec p{{margin:0;color:var(--doux);font-size:15.5px}}
.table{{overflow-x:auto;background:var(--carte);border-radius:14px}}
table{{border-collapse:collapse;width:100%;min-width:760px}}
th,td{{padding:8px 10px;border-bottom:1px solid var(--filet);text-align:left;vertical-align:middle}}
thead th{{font-size:13px;text-transform:uppercase;letter-spacing:.06em;color:var(--doux)}}
tbody th{{display:flex;gap:10px;align-items:center;font-weight:800;min-width:230px}}
tbody th img{{width:72px;aspect-ratio:3/2;object-fit:cover;border-radius:6px}}
tbody th small{{display:block;color:var(--doux);font-weight:700;font-size:13px}}
audio{{width:200px;height:36px}}
td.manque{{color:var(--doux);font-style:italic}}
ul.ver{{background:var(--carte);border-radius:14px;padding:16px 16px 16px 36px;margin:0}}
ul.ver li{{margin:0 0 6px}}
.note{{color:var(--doux);font-size:15px}}
</style></head><body><main>
<span class="eyebrow">Nouveau projet · 29 septembre 2026</span>
<h1>Montréal en poche</h1>
<p class="lead">Un guide touristique de Montréal pour le téléphone, en français, en anglais et en espagnol — même famille que
Compostelle : des croquis de carnet de voyage, une voix qui guide, un passeport qui se remplit de tampons. Bâti pendant votre heure d'absence.</p>
<div class="chiffres">
  <div><b>{len(lieux)}</b><span>lieux, chacun avec son croquis</span></div>
  <div><b>3</b><span>langues, tout bascule d'un geste</span></div>
  <div><b>{sons}/{len(lieux) * 3}</b><span>textes lus (audioguide)</span></div>
  <div><b>{len(ex.CIRCUITS)}</b><span>circuits à pied</span></div>
  <div><b>{len(scenes)}</b><span>scènes « Parler » pour se débrouiller en français</span></div>
  <div><b>{len(ex.PRATIQUE)}</b><span>fiches pratiques</span></div>
  <div><b>{len(ex.MOTS)}</b><span>mots d'ici ({mots_sons} lus)</span></div>
</div>
<div class="qr">{qr_svg(URL, cote=200)}
  <div><p style="margin:0 0 6px"><b>Sur le téléphone</b> — le code QR mène à <code>{E(URL)}</code>.</p>
  <a class="btn" href="/modules-autonomes/montreal/" target="_blank" rel="noopener">Ouvrir l'application</a></div></div>

<h2>Ce qu'il y a dedans</h2>
<p><b>Découvrir</b> : les 28 lieux en cartes, filtrés par genre (à voir, quartiers, manger, cafés et bières) ou triés « autour de moi ».
<b>Le lieu</b> : son croquis, l'audioguide dans la langue choisie (trois vitesses), le texte du guide, quoi commander et la phrase à dire
au comptoir, « le saviez-vous ? », le conseil d'ici, l'itinéraire dans Google Maps, le tampon.
<b>La carte</b> des 28 épingles. <b>Quatre circuits</b> — le Vieux-Montréal, le Plateau et le Mile End gourmands, la montagne, de
l'Olympique au fleuve — avec leur carte, leurs étapes et le chemin entre elles. <b>Le passeport</b>. <b>Pratique</b> : métro, pourboire,
taxes, saisons, « Bonjour-Hi »… et <b>les mots d'ici</b> (dépanneur, tuque, il fait frette), avec leur phrase dite en québécois.</p>

<h2>« Parler » — ajouté le 30 septembre 2026</h2>
<p>Pour les touristes anglophones et hispanophones qui veulent se débrouiller en français (votre choix du 30 septembre).
{len(scenes)} scènes de la vie montréalaise : {", ".join(E(sc["titre"]["fr"]) for sc in scenes)}. Le personnage parle en
français québécois (Sylvie, Thierry, Jean — Azure) ; l'apprenant choisit sa réponse parmi trois, reçoit une explication dans sa
langue quand il se trompe (faux amis, calques, registre, mots d'ici), entend la bonne réplique et la redit à voix haute. Étoiles au
passeport, phrases à retenir, note culturelle. Chaque lieu qui a sa scène l'offre sous son audioguide. Onglet « Parler » ; les
circuits sont passés dans « Découvrir ».</p>
<p class="note">Pas de reconnaissance vocale pour l'instant : l'apprenant dit la phrase sans être écouté — rien ne part du téléphone.
L'étage suivant, « Parler librement » avec l'assistant, reprendrait la route et la vente de Compostelle.</p>

<h2>« En famille avec Filou » — le pilote, 30 septembre 2026</h2>
<p>Toutes les recommandations de la proposition, et l'habit A « Bonbon ». Un bouton sur l'accueil bascule l'application : Filou, le raton
du mont Royal, guide les 6 à 11 ans dans {len(fam)} lieux — il raconte, pose une énigme qui se résout en regardant le lieu (vérifiée en
ligne, lieu par lieu), lance un défi ; la bonne réponse colle un autocollant dans le carnet, et le carnet complet donne un diplôme à
imprimer (le prénom reste dans le téléphone). Quatre scènes « Parle français comme un grand ! » à deux choix. La carte n'a plus que les
dix lieux, et « La fiche des grands » reste à un geste.</p>
<p class="note"><b>Les voix de Filou ne sont pas encore produites</b> : Azure refuse la clé depuis le 30 septembre (401, « invalid
subscription key »), alors qu'elle servait une heure plus tôt. D'ici là, la voix du téléphone lit tout. Une fois la clé réglée :
<code>python3 build/montreal_audio.py</code> fait les 159 sons qui manquent, puis <code>python3 build/montreal_app.py</code>.</p>

<h2>Décidé à votre place</h2>
<p class="note">Vous étiez parti ; j'ai pris la recommandation chaque fois. Tout se renverse sans rien casser.</p>
<div class="decs">{dec}</div>

<h2>L'audioguide, à écouter</h2>
<p class="note">Les trois langues de chaque lieu, côte à côte. Un son qui sonne mal se refait seul si son texte change
(<code>python3 build/montreal_audio.py</code>).</p>
<div class="table"><table><thead><tr><th>Lieu</th><th>Français</th><th>English</th><th>Español</th></tr></thead>
<tbody>{''.join(rangs)}</tbody></table></div>

<h2>Faits encore à vérifier</h2>
<p class="note">Relevés dans le contenu lui-même. Tout le reste a été vérifié en ligne par un second agent, qui a corrigé les trois langues
ensemble. Heures et prix ne sont jamais écrits : l'application dit de vérifier avant de se déplacer.</p>
<ul class="ver">{ver}</ul>

<h2>La suite possible</h2>
<ul>
<li>Une relecture par un Montréalais anglophone et un hispanophone.</li>
<li>D'autres lieux (le Marché Bonsecours, la Grande Bibliothèque, le Village, la plage de Verdun…), d'autres langues (mandarin, portugais, allemand).</li>
<li>Le mode hors ligne complet, comme « Préparer pour le chemin » de Compostelle.</li>
<li>Un jeu : une chasse aux indices dans le Vieux-Montréal, un tampon par énigme résolue.</li>
</ul>
<p class="note">Sources : <code>build/contenu/montreal/</code> · application <code>build/montreal_app.py</code> · croquis
<code>build/montreal_croquis.py</code> · voix <code>build/montreal_audio.py</code> · cette page <code>build/montreal_livraison.py</code>.</p>
</main></body></html>
"""
    SORTIE.write_text(page, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} : {sons} sons, {len(a_verifier)} faits à vérifier")


if __name__ == "__main__":
    main()
