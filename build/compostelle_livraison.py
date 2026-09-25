#!/usr/bin/env python3
"""La page de livraison de l'application Compostelle — ce qui est fait, et ce qui reste à trancher.

    python3 build/compostelle_livraison.py   # → assets/presentations/compostelle-livraison.html

Daniel est parti le 25 sept. 2026 au soir en laissant carte blanche (« laisse-toi
aller »). Tout ce qui demande son jugement se rend sur une page du classeur,
jamais dans le fil : ce qui a été décidé à sa place, ce qui reste ouvert, et
les extraits que le contrôle signale — à écouter sur la page même.
"""
import html, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402
from qr import svg as qr_svg  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-livraison.html"
URL = "https://portail.edufrancis.ca/modules-autonomes/compostelle/"
MEDIA = "../interactive/compostelle/"
E = html.escape


def main():
    import re
    LX, ET, PS = C.charger("lexique"), C.charger("etapes"), C.charger("personnages")
    xs = list(C.extraits())
    releve = json.loads((C.CONTENU / "ecoute.json").read_text(encoding="utf-8"))
    douteux = [r for r in releve if r["douteux"]]
    n_croquis = sum(1 for e in LX.LEXIQUE if e[4] == "croquis")
    portraits = [(k, v) for k, v in PS.PERSONNAGES.items() if v[6]]
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — l'application</title>", tete)
    tete = tete.replace("</head>", """<style>
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
.qr{display:grid;grid-template-columns:200px minmax(0,1fr);gap:22px;align-items:center;background:var(--card);border:1px solid var(--line);border-radius:3px;padding:20px}
.qr svg{width:100%;height:auto}
@media (max-width:640px){.qr{grid-template-columns:1fr}.qr svg{max-width:220px}}
.portraits{display:grid;grid-template-columns:repeat(auto-fill,minmax(110px,1fr));gap:12px}
.portraits figure{margin:0;text-align:center}
.portraits img{width:100%;aspect-ratio:1/1;object-fit:cover;border-radius:50%;background:#fff;border:1px solid var(--line)}
.portraits figcaption{font-size:13px;line-height:1.3;color:var(--muted);margin-top:6px}
.portraits b{display:block;color:var(--body)}
.ecoute{display:flex;flex-direction:column;gap:10px}
.ecoute div{background:var(--card);border:1px solid var(--line);border-radius:3px;padding:12px 14px}
.ecoute audio{width:100%;margin-top:6px}
.ecoute small{color:var(--muted)}
.btn-app{display:inline-block;background:#0A8F5B;color:#fff;font-weight:800;text-decoration:none;padding:12px 18px;border-radius:10px}
</style>
</head>""")
    fiche_d = "".join(
        f"<div><b>{E(r['fichier'])}</b> — {E(PS.PERSONNAGES[r['perso']][0])}<br>"
        f"<small>attendu « {E(r['attendu'])} » · entendu par la reconnaissance « {E(r['entendu'])} » ({r['similitude']})</small>"
        f"<audio controls preload=\"none\" src=\"{MEDIA}sons/{E(r['fichier'])}\"></audio></div>" for r in douteux)
    gal = "".join(f'<figure><img src="{MEDIA}portraits/{v[6]}.jpg" alt="" loading="lazy"><figcaption><b>{E(v[0])}</b>{E(v[1])}'
                  + (f", {E(v[2])}" if v[2] and k != "marta" else "") + "</figcaption></figure>" for k, v in portraits)
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>En route vers Compostelle &mdash; l'application</h1>
<p class="chapeau">Construite pendant votre absence, le 25 septembre 2026, à partir du plan. Une application pour
<strong>téléphone</strong> : dix journées, une par étape du Camino francés, de Roncesvalles à Santiago ; une credencial
qui se remplit de tampons ; des voix d'Espagne ; et Marta, une pèlerine de Valladolid, qu'on retrouve chaque soir.</p>

<section class="premier">
  <h2>L'ouvrir sur votre téléphone</h2>
  <div class="qr">{qr_svg(URL, cote=200)}
   <div><p>Visez le code avec l'appareil photo du téléphone, ou ouvrez :</p>
   <p><a class="btn-app" href="/modules-autonomes/compostelle/">Ouvrir l'application</a></p>
   <p style="font-size:14px;color:var(--muted)">{E(URL)} — aucune connexion, aucun code : tout reste dans le téléphone.
   La première fois, on choisit « pèlerin » ou « pèlerine » (l'espagnol accorde : <i>cansado</i>, <i>cansada</i>).</p></div></div>
</section>

<section>
  <h2>Ce qui est fait</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">10</span><span class="q">journées, sept temps chacune</span></div>
    <div class="ch"><span class="n">{len(LX.LEXIQUE)}</span><span class="q">mots en onze planches, {n_croquis} dessinés</span></div>
    <div class="ch"><span class="n">{len(xs)}</span><span class="q">sons, douze voix d'Espagne</span></div>
    <div class="ch"><span class="n">{len(LX.PIEGES)}</span><span class="q">faux amis, chacun dans sa phrase</span></div>
  </div>
  <table class="cmp"><thead><tr><th>Temps de la journée</th><th>Ce qu'on y fait</th></tr></thead><tbody>
    <tr><td>1. Le lieu</td><td>La vignette, trois paragraphes pour situer (histoire, tourisme), ce qu'on y visite — avec le mot espagnol et sa voix.</td></tr>
    <tr><td>2. Les mots du jour</td><td>Des cartes dessinées ; on touche, on entend, la traduction apparaît. Elle reste cachée d'abord.</td></tr>
    <tr><td>3. J'entends, je trouve</td><td>Un mot entendu, quatre images.</td></tr>
    <tr><td>4. Ce qu'on me répond</td><td>La famille maîtresse : la personne du lieu répond, à sa vitesse ; que veut-elle dire ? Chaque mauvais choix a sa rétroaction.</td></tr>
    <tr><td>5. Je le dis</td><td>La situation en français, on la dit au micro (reconnaissance es-ES du navigateur), puis le modèle.</td></tr>
    <tr><td>6. La scène</td><td>La situation jouée avec la personne du lieu : ses répliques en voix, nos choix, la rétroaction. À León, l'allergie est <b>éliminatoire</b> et le dit d'avance.</td></tr>
    <tr><td>7. Le soir, avec Marta</td><td>La conversation du lieu (les jambes, la nourriture, pourquoi on marche, la pierre de la Cruz de Ferro, l'au revoir). Sa voix porte une intention par réplique. Elle se souvient : la raison choisie sur la Meseta revient à Santiago.</td></tr>
  </tbody></table>
  <p style="margin-top:14px">Et autour : <b>la poche</b> (onze rubriques, les urgences, « Montrer » en grand, et « Préparer pour le chemin » qui met
  tout dans le téléphone pour marcher sans réseau), <b>tous les mots</b>, <b>les faux amis</b>, <b>le test « Suis-je prêt ? »</b> (deux formes,
  il situe sans noter), et une <b>Compostela</b> à imprimer à la fin — présentée clairement comme un souvenir, pas comme la vraie.</p>
</section>

<section>
  <h2>Les gens du chemin</h2>
  <div class="portraits">{gal}</div>
</section>

<section>
  <h2>Décidé à votre place</h2>
  <p>Vous n'aviez pas exporté les décisions du plan : j'ai pris <b>les onze recommandations</b>. Chacune se renverse.</p>
  <ul class="simple">
    <li>Espagnol d'Espagne ; <i>tú</i> entre pèlerins, <i>usted</i> au comptoir, <i>vosotros</i> reconnu seulement ; galicien reconnu.</li>
    <li>Le Camino francés seul ; la credencial à tampons comme fil ; les vignettes d'étape comme décors.</li>
    <li>La poche hors ligne ; voix Azure es-ES (production faite : environ 1 $ de voix) ; Marta, compagne de route récurrente.</li>
    <li>Le thème francis, le jaune de la flèche réservé à la progression.</li>
    <li>La diffusion : rien n'est promis au public ; l'application est en ligne mais n'est reliée qu'au classeur.</li>
  </ul>
</section>

<section>
  <h2>Ce qui reste, et qui vous revient</h2>
  <ol class="simple">
    <li><b>Le jeu de rôle libre avec l'assistant.</b> Les scènes écrites marchent sans IA et sans réseau. La suite « avec assistance »
    (la même personne, qui répond à ce qu'on dit vraiment) est écrite : <code>build/contenu/compostelle/jeu_de_role.py</code>, vingt situations,
    trois paliers, un bilan en français. Elle n'est <b>pas branchée</b> : <code>server.py</code> était tenu ce soir-là par la session de l'hôtel.
    Et elle pose une question qui vous revient : un public sans compte n'a pas de code, or le jeu de rôle en exige un. Des codes de pilote ?</li>
    <li><b>La relecture par une personne d'Espagne</b> : 519 répliques et phrases, écrites par moi.</li>
    <li><b>Les faits du chemin</b> (heures, prix, 2 tampons par jour depuis Sarria, questions du bureau du pèlerin) : vraisemblables, à vérifier et dater.</li>
    <li><b>Les onze extraits que le contrôle signale</b>, ci-dessous : tous s'expliquent (mots basques ou galiciens, un nom français dans une bouche espagnole,
    des chiffres écrits en chiffres par la reconnaissance), mais c'est votre oreille qui tranche.</li>
  </ol>
</section>

<section>
  <h2>À écouter : les {len(douteux)} extraits signalés</h2>
  <div class="ecoute">{fiche_d}</div>
</section>

<section>
  <h2>Ce que ça a coûté</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;$</span><span class="q">d'images : 82 mots, 10 portraits, 12 vignettes, et les reprises</span></div>
    <div class="ch"><span class="n">≈&nbsp;1&nbsp;$</span><span class="q">de voix chez Azure, retentatives comprises</span></div>
    <div class="ch"><span class="n">0</span><span class="q">par usage : aucune IA à l'exécution tant que le jeu de rôle libre n'est pas branché</span></div>
  </div>
</section>

<div class="pied">
  <p>Livraison du 25 septembre 2026 · « En route vers Compostelle ».</p>
  <p>Produit par <code>build/compostelle_livraison.py</code> — ne pas l'éditer. L'application : <code>build/compostelle_app.py</code>.</p>
</div>
</div>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE))


if __name__ == "__main__":
    main()
