#!/usr/bin/env python3
"""La proposition d'une version enfants de « Montréal en poche », au classeur.

    python3 build/montreal_enfants_plan.py   # → assets/presentations/montreal-enfants-proposition.html

Demande de Daniel, 30 septembre 2026 : « est-ce une idée de créer un guide
touristique, ou des personnages touristiques, pour les enfants ? à
réfléchir ». La page expose l'idée, montre trois mascottes candidates
(build/montreal_croquis.py, famille « mascotte »), une maquette de fiche en
mode famille, les garde-fous, et dix décisions à exporter (plan
« montreal-enfants »), comme le plan de Compostelle.
"""
import html, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "assets" / "presentations" / "montreal-enfants-proposition.html"
E = html.escape
M = "/assets/interactive/montreal/"

MASCOTTES = [
    ("raton", "Le raton laveur du mont Royal",
     "Un vrai habitant de la montagne — les familles le croisent au belvédère. Masque de bandit, curieux, un peu chapardeur : "
     "un caractère tout trouvé. Silhouette lisible à 40 px.", "Recommandé"),
    ("ecureuil", "L'écureuil noir des parcs",
     "Très montréalais (on le voit partout au parc La Fontaine), plus original. Mais à petite taille, il se lit comme « un écureuil » "
     "et perd ce qui le rend d'ici.", ""),
    ("castor", "Le castor",
     "Connu de tous les enfants, facile à aimer. Mais c'est le Canada plus que Montréal, et les boutiques de souvenirs l'ont déjà usé.", ""),
]

LIEUX_FAMILLE = [
    ("Déjà dans le guide", ["Vieux-Port", "Biosphère", "Jardin botanique et Insectarium", "Parc olympique et Biodôme",
                            "Parc du Mont-Royal", "Canal de Lachine", "Marché Jean-Talon", "Les bagels", "La Banquise"]),
    ("À ajouter pour les familles", ["Le Biodôme en fiche à part", "Le Centre des sciences", "Le Planétarium",
                                     "La plage du parc Jean-Drapeau", "La Ronde", "Les patinoires d'hiver"]),
]

DECISIONS = [
    ("forme", "La forme", [("famille", "Un « mode famille » dans la même application", True),
                           ("app", "Une application à part", False)],
     "Même adresse, mêmes croquis, même passeport : un bouton « En famille » bascule le ton et les contenus. Une seconde application doublerait tout."),
    ("mascotte", "La mascotte", [("raton", "Le raton laveur", True), ("ecureuil", "L'écureuil noir", False), ("castor", "Le castor", False)],
     "Voir plus haut."),
    ("age", "L'âge visé", [("6-11", "6 à 11 ans", True), ("4-7", "4 à 7 ans", False), ("8-12", "8 à 12 ans", False)],
     "À 6 ans on écoute une histoire, à 11 on résout une énigme : c'est la plage où une même fiche sert les deux, avec un parent qui lit."),
    ("ton", "Le ton de la mascotte", [("tu", "Elle tutoie l'enfant", True), ("vous", "Elle vouvoie", False)],
     "Au Québec comme en anglais et en espagnol, on tutoie un enfant."),
    ("langues", "Les langues", [("trois", "Les trois dès le départ", True), ("fr-en", "Français et anglais d'abord", False)],
     "Le contenu enfant est court (trois phrases par lieu) : les trois langues coûtent peu de plus."),
    ("enigmes", "Les énigmes", [("verifiee", "Réponse vérifiée dans l'application (choix)", True),
                                ("libre", "Sans vérification, on en parle en famille", False)],
     "Une réponse vérifiée donne l'autocollant ; sans elle, l'enfant ne sait pas s'il a trouvé."),
    ("recompense", "La récompense", [("diplome", "Autocollants + diplôme d'explorateur à imprimer", True),
                                     ("autocollants", "Autocollants seulement", False)],
     "Le diplôme porte le prénom, tapé et imprimé sur place : il ne quitte jamais le téléphone."),
    ("parler", "Le jeu de rôle enfant", [("oui", "Oui : quatre scènes simples, deux choix, des images", True),
                                         ("plus-tard", "Plus tard", False)],
     "Commander sa crème glacée, dire bonjour et merci, demander les toilettes, acheter un bagel : l'enfant qui parle français au comptoir, c'est le souvenir du voyage."),
    ("voix", "La voix de la mascotte", [("azure", "Une voix québécoise d'Azure, jouée plus vive", True),
                                        ("comedien", "Un comédien enregistré", False)],
     "Azure n'a pas de voix d'enfant au Québec ; Thierry ou Sylvie, avec une écriture vive, suffisent pour un pilote. Un comédien viendra si le produit prend."),
    ("lot", "Le premier lot", [("dix", "Dix lieux, puis on écoute les familles", True), ("vingt", "Vingt lieux d'un coup", False)],
     "Dix lieux se font en une journée ; on voit ce que les enfants font vraiment avant d'écrire le reste."),
]


def main():
    masc = "".join(
        f'<figure class="masc{" reco" if r else ""}"><img src="{M}mascottes/{k}.jpg" alt="">'
        f'<figcaption><b>{E(n)}</b>{f"<span class=pas>{r}</span>" if r else ""}<p>{E(t)}</p></figcaption></figure>'
        for k, n, t, r in MASCOTTES)
    lieux = "".join(f"<div class=lf><h3>{E(t)}</h3><ul>{''.join(f'<li>{E(x)}</li>' for x in xs)}</ul></div>" for t, xs in LIEUX_FAMILLE)
    D = [{"k": k, "t": t, "o": [[v, l] for v, l, _ in o], "r": next(v for v, _, r in o if r), "p": p} for k, t, o, p in DECISIONS]

    page = f"""<!doctype html>
<html lang="fr-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>Montréal en famille — proposition</title>
<link rel="stylesheet" href="/assets/design-system/tokens/fonts.css">
<style>
:root{{--fond:#F6F1E7;--carte:#fff;--encre:#1E2733;--doux:#5D6572;--filet:#E2D9C6;--rouge:#B3262E;--or:#C9A227;--vert:#2F6B45}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--fond);color:var(--encre);font:17px/1.55 Nunito,system-ui,sans-serif}}
main{{max-width:980px;margin:0 auto;padding:28px 16px 60px}}
.eyebrow{{font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase;color:var(--rouge)}}
h1{{font-size:36px;line-height:1.1;margin:6px 0 10px;letter-spacing:-.02em}}
h2{{font-size:24px;margin:44px 0 12px}}
.lead{{font-size:19px;color:var(--doux);max-width:760px}}
.carte{{background:var(--carte);border-radius:14px;padding:16px 18px}}
.pourquoi{{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:12px}}
.pourquoi h3{{margin:0 0 4px;font-size:17px}}.pourquoi p{{margin:0;color:var(--doux);font-size:15.5px}}
.mascs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}}
.masc{{margin:0;background:var(--carte);border-radius:14px;padding:12px;border:2px solid transparent}}
.masc.reco{{border-color:var(--or)}}
.masc img{{width:100%;aspect-ratio:1;object-fit:contain}}
.masc b{{font-size:17px}}
.masc p{{margin:4px 0 0;color:var(--doux);font-size:15px}}
.pas{{display:inline-block;margin-left:8px;background:#FBF3D9;color:#7A5F0B;font-size:12px;font-weight:900;border-radius:999px;padding:2px 8px;vertical-align:2px}}
.maquette{{display:grid;grid-template-columns:minmax(0,340px) minmax(0,1fr);gap:24px;align-items:start}}
@media (max-width:720px){{.maquette{{grid-template-columns:1fr}}}}
.tel{{background:#fff;border:10px solid #1E2733;border-radius:34px;overflow:hidden;max-width:340px}}
.tel img.v{{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}}
.tel .c{{padding:12px 14px 16px}}
.tel .bande{{display:flex;gap:10px;align-items:center;background:#FFF8EC;border-radius:14px;padding:8px 10px;margin:-34px 0 10px;position:relative}}
.tel .bande img{{width:58px;height:58px;border-radius:50%;background:#fff;border:2px solid #EAD7B0;object-fit:cover;object-position:top}}
.tel .bande b{{font-size:15px}}
.tel h3{{margin:4px 0 6px;font-size:21px}}
.tel p{{margin:0 0 10px;font-size:15.5px}}
.bloc{{border-radius:12px;padding:10px 12px;margin:10px 0;font-size:15px}}
.bloc h4{{margin:0 0 4px;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase}}
.bloc.enigme{{background:#EEF3FA}}.bloc.enigme h4{{color:#1F4E79}}
.bloc.defi{{background:#EEF5F0}}.bloc.defi h4{{color:var(--vert)}}
.opts{{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:6px}}
.opts span{{background:#fff;border:2px solid #1E2733;border-radius:10px;text-align:center;font-weight:900;padding:6px 0}}
.opts span.ok{{background:#1E2733;color:#fff}}
.autocol{{display:flex;gap:10px;align-items:center;margin-top:10px;font-weight:800;font-size:14.5px}}
.autocol i{{width:54px;height:54px;border-radius:50%;background:#fff url({M}mascottes/raton.jpg) center 18%/140% no-repeat;border:3px dashed var(--rouge);transform:rotate(-8deg);flex:none}}
.notes li{{margin:0 0 8px}}
.lfs{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}
.lf{{background:var(--carte);border-radius:14px;padding:14px 18px}}
.lf h3{{margin:0 0 6px;font-size:17px}}.lf ul{{margin:0;padding-left:20px}}
.gardes{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}
.gardes div{{background:var(--carte);border-radius:14px;padding:14px 16px;border-left:4px solid var(--rouge)}}
.gardes h3{{margin:0 0 4px;font-size:16.5px}}.gardes p{{margin:0;color:var(--doux);font-size:15.5px}}
table.cout{{border-collapse:collapse;background:var(--carte);border-radius:14px;overflow:hidden;width:100%}}
table.cout td,table.cout th{{padding:9px 14px;border-bottom:1px solid var(--filet);text-align:left}}
.dec{{background:var(--carte);border-radius:14px;padding:14px 16px;margin:0 0 10px}}
.dec h3{{margin:0 0 8px;font-size:17px}}
.dec p{{margin:8px 0 0;color:var(--doux);font-size:15px}}
.opt{{border:2px solid var(--encre);background:#fff;border-radius:999px;padding:7px 14px;font:800 15px Nunito,system-ui,sans-serif;margin:0 6px 6px 0;cursor:pointer;min-height:40px}}
.opt[aria-pressed=true]{{background:var(--encre);color:#fff}}
.opt .r{{font-size:11.5px;font-weight:900;color:#7A5F0B;margin-left:6px}}
.opt[aria-pressed=true] .r{{color:#F1D98A}}
.btn-export{{background:var(--rouge);color:#fff;border:0;border-radius:12px;padding:13px 20px;font:900 16px Nunito,system-ui,sans-serif;cursor:pointer}}
.btn-sec{{background:#fff;color:var(--encre);border:2px solid var(--encre);border-radius:12px;padding:11px 18px;font:900 16px Nunito,system-ui,sans-serif;cursor:pointer;margin-left:8px}}
#etat{{color:var(--doux);margin-left:10px;font-weight:700}}
</style></head><body><main>
<span class="eyebrow">Proposition · Montréal en poche · 30 septembre 2026</span>
<h1>Montréal en famille</h1>
<p class="lead">Une mascotte qui guide les enfants d'un lieu à l'autre : trois phrases qu'elle leur raconte, une énigme à résoudre
<b>en regardant le lieu</b>, un défi, un autocollant dans le carnet d'explorateur — et, pour les familles qui ne parlent pas
français, le plaisir de commander soi-même sa crème glacée en français.</p>

<h2>Pourquoi ça tient</h2>
<div class="pourquoi">
  <div class="carte"><h3>Montréal est une ville de familles</h3><p>Biodôme, Insectarium, Biosphère, Vieux-Port, mont Royal, plage,
  patinoires : la moitié des lieux du guide parlent déjà aux enfants. Il leur manque une voix à leur hauteur.</p></div>
  <div class="carte"><h3>Le moteur existe</h3><p>Croquis, voix, passeport, scènes « Parler » : la version enfants est un
  ton et des contenus de plus dans la même application, pas un produit à bâtir.</p></div>
  <div class="carte"><h3>C'est le parent qui choisit</h3><p>Il tient le téléphone et cherche de quoi occuper ses enfants <i>sans</i>
  écran pendant la visite. D'où des énigmes qui font lever les yeux : l'écran pose la question, le lieu la répond.</p></div>
  <div class="carte"><h3>Le français, par le jeu</h3><p>Pour une famille anglophone ou hispanophone, l'enfant qui dit « Une
  crème glacée à la vanille, s'il vous plaît » au comptoir, c'est le souvenir du voyage — et la porte d'entrée de francis.</p></div>
</div>

<h2>Trois mascottes candidates</h2>
<p class="note" style="color:var(--doux)">Dessinées dans le même carnet que les lieux. Ma recommandation est encadrée d'or.
Le nom viendra après le choix.</p>
<div class="mascs">{masc}</div>

<h2>À quoi ressemble une fiche en mode famille</h2>
<div class="maquette">
  <div class="tel"><img class="v" src="{M}lieux/vieux-port.jpg" alt="">
    <div class="c">
      <div class="bande"><img src="{M}mascottes/raton.jpg" alt=""><span><b>Le raton te raconte</b><br><small>Écouter · 30 s</small></span></div>
      <h3>Le Vieux-Port</h3>
      <p>Il y a très longtemps, les grands bateaux arrivaient ici de l'autre côté de l'océan. Aujourd'hui, on y fait du vélo,
      on monte dans la Grande roue… et la tour de l'Horloge sonne encore l'heure pour tout le monde !</p>
      <div class="bloc enigme"><h4>Énigme — regarde autour de toi</h4>Trouve la tour de l'Horloge. De quelle couleur est-elle ?
        <div class="opts"><span class="ok">Blanche</span><span>Rouge</span><span>Verte</span></div></div>
      <div class="bloc defi"><h4>Défi</h4>Compte les voiliers que tu vois sur l'eau. Plus de cinq ? Tu as l'œil d'un capitaine !</div>
      <div class="autocol"><i></i>Autocollant gagné : « Capitaine du Vieux-Port »</div>
    </div></div>
  <div>
    <ul class="notes">
      <li><b>Trois phrases, pas trois paragraphes</b> : lues par la mascotte en 30 secondes, pendant que l'enfant regarde le lieu.</li>
      <li><b>L'énigme se résout sur place</b> — une couleur, un nombre, une forme. Elle ne se trouve pas sur Internet, et elle
      ne demande jamais d'aller au bord de l'eau ou de traverser.</li>
      <li><b>Le défi est libre</b> : compter, chercher, imiter. Pas de bonne réponse, juste un jeu en famille.</li>
      <li><b>L'autocollant</b> va dans le carnet d'explorateur (le passeport, en version enfant). Tous les autocollants : un diplôme
      à imprimer, avec le prénom tapé sur place.</li>
      <li>Même lieu, même croquis que la fiche adulte : le parent bascule entre les deux d'un geste.</li>
      <li>L'exemple est en français ; chaque fiche existe aussi en anglais et en espagnol.</li>
    </ul>
  </div>
</div>

<h2>Les lieux</h2>
<div class="lfs">{lieux}</div>

<h2>Les garde-fous</h2>
<div class="gardes">
  <div><h3>Sécurité</h3><p>Aucune énigme au bord de l'eau, dans la rue ou dans un escalier. On regarde, on ne grimpe pas. Chaque énigme
  est relue pour ça, comme on a rejoué l'allergie pour chaque aliment dans Compostelle.</p></div>
  <div><h3>Aucune donnée d'enfant</h3><p>Pas de compte, pas de photo, pas de micro. Le prénom du diplôme reste dans le téléphone.
  Avec des mineurs, la Loi 25 est plus stricte : le plus simple est de ne rien recueillir.</p></div>
  <div><h3>Moins d'écran, pas plus</h3><p>Chaque fiche finit sur une consigne qui fait lever les yeux. L'application ne propose
  aucun jeu qui se joue sans le lieu.</p></div>
  <div><h3>Ton et faits</h3><p>Une mascotte qui s'amuse, jamais qui se moque. Les faits racontés aux enfants sont ceux, vérifiés, de
  la fiche adulte — simplifiés, jamais inventés.</p></div>
</div>

<h2>Ce que ça coûte</h2>
<table class="cout"><tr><th>Poste</th><th>Pour dix lieux</th></tr>
<tr><td>Textes enfants (trois phrases, énigme, défi) en trois langues</td><td>écrits et relus par agents, vérifiés par vous</td></tr>
<tr><td>La mascotte : une vingtaine de poses (salut, loupe, surprise, bravo…)</td><td>≈ 1,50 $ d'images</td></tr>
<tr><td>Voix de la mascotte, trois langues</td><td>≈ 0,50 $</td></tr>
<tr><td>Quatre scènes « Parler » enfant</td><td>≈ 0,50 $ de voix</td></tr>
<tr><td>Temps</td><td>une journée de travail pour un pilote jouable</td></tr></table>

<h2>Dix décisions</h2>
<p style="color:var(--doux)">Ma recommandation est marquée. Choisissez, puis « Exporter mes décisions » et recollez le résultat dans la
conversation. « Tout recommandé » coche mes recommandations d'un coup.</p>
<div id="decisions"></div>
<p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button><button type="button"
class="btn-sec" id="reco">Tout recommandé</button><span id="etat"></span></p>
</main>
<script>
(function(){{
  var D={json.dumps(D, ensure_ascii=False)}, CLE='montreal-enfants-decisions', choix={{}};
  try{{ choix=JSON.parse(localStorage.getItem(CLE)||'{{}}'); }}catch(e){{}}
  var zone=document.getElementById('decisions');
  function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c];}});}}
  D.forEach(function(d,i){{
    var div=document.createElement('div'); div.className='dec';
    div.innerHTML='<h3>'+(i+1)+'. '+esc(d.t)+'</h3>'+d.o.map(function(o){{
      return '<button type="button" class="opt" data-k="'+d.k+'" data-v="'+o[0]+'">'+esc(o[1])+(o[0]===d.r?'<span class="r">recommandé</span>':'')+'</button>';
    }}).join('')+'<p>'+esc(d.p)+'</p>';
    zone.appendChild(div);
  }});
  function garder(){{ try{{ localStorage.setItem(CLE,JSON.stringify(choix)); }}catch(e){{}} }}
  function peindre(){{
    zone.querySelectorAll('.opt').forEach(function(b){{ b.setAttribute('aria-pressed', choix[b.dataset.k]===b.dataset.v?'true':'false'); }});
    var n=Object.keys(choix).length;
    document.getElementById('etat').textContent=n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }}
  zone.addEventListener('click',function(e){{
    var b=e.target.closest('.opt'); if(!b) return;
    if(choix[b.dataset.k]===b.dataset.v) delete choix[b.dataset.k]; else choix[b.dataset.k]=b.dataset.v;
    garder(); peindre();
  }});
  document.getElementById('reco').addEventListener('click',function(){{ D.forEach(function(d){{ choix[d.k]=d.r; }}); garder(); peindre(); }});
  document.getElementById('exporter').addEventListener('click',function(){{
    var out={{plan:'montreal-enfants', date:new Date().toISOString().slice(0,10), decisions:{{}}}};
    D.forEach(function(d){{ var o=d.o.filter(function(x){{return x[0]===choix[d.k];}})[0]; out.decisions[d.k]=o?o[1]:null; }});
    var t=JSON.stringify(out,null,2);
    var fin=function(){{ document.getElementById('etat').textContent='Copié — à recoller dans la conversation.'; }};
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}});
    else prompt('Copiez :',t);
  }});
  peindre();
}})();
</script>
</body></html>
"""
    SORTIE.write_text(page, encoding="utf-8")
    print(SORTIE.relative_to(RACINE))


if __name__ == "__main__":
    main()
