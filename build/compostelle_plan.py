#!/usr/bin/env python3
"""Le plan de « En route vers Compostelle » — l'espagnol du pèlerin francophone.

    python3 build/compostelle_plan.py   # → assets/presentations/compostelle-plan.html

Demande de Daniel, 25 septembre 2026 : à l'image de la trousse de
l'hôtellerie, mais pour les PÈLERINS francophones du chemin de Compostelle qui
veulent se débrouiller en espagnol — manger, dormir, parler aux gens du pays —
toujours sous la marque francis, avec un jeu de rôle. Puis, en cours de route :
« quelque chose d'un peu ludique », les étapes du Camino francés en images,
de Saint-Jean-Pied-de-Port à Santiago.

La page reprend l'en-tête (styles, décisions) du plan de la Maison Francœur.
Les vignettes viennent de build/compostelle_croquis.py.
"""
import pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-plan.html"
IMG = "../interactive/compostelle/etapes/"

# Les lieux d'étape du Camino francés, en kilomètres CUMULÉS depuis
# Saint-Jean-Pied-de-Port (≈, d'après les guides courants ; les étapes varient
# d'un guide à l'autre de quelques kilomètres). (nom, km, région, grand?)
LIEUX = [
    ("Saint-Jean-Pied-de-Port", 0, "fr", True),
    ("Roncesvalles", 25, "na", True), ("Zubiri", 47, "na", False),
    ("Pamplona", 68, "na", True), ("Puente la Reina", 92, "na", True),
    ("Estella", 114, "na", False), ("Los Arcos", 135, "na", False),
    ("Logroño", 163, "ri", True), ("Nájera", 192, "ri", False),
    ("Santo Domingo de la Calzada", 213, "ri", False), ("Belorado", 236, "cl", False),
    ("Burgos", 285, "cl", True), ("Castrojeriz", 325, "cl", False),
    ("Frómista", 350, "cl", False), ("Carrión de los Condes", 369, "cl", False),
    ("Sahagún", 409, "cl", False), ("León", 463, "cl", True),
    ("Astorga", 514, "cl", True), ("Cruz de Ferro", 540, "cl", True),
    ("Ponferrada", 565, "cl", False), ("Villafranca del Bierzo", 589, "cl", False),
    ("O Cebreiro", 617, "ga", True), ("Sarria", 659, "ga", True),
    ("Portomarín", 681, "ga", False), ("Palas de Rei", 706, "ga", False),
    ("Arzúa", 735, "ga", False), ("Santiago de Compostela", 775, "ga", True),
]
REGIONS = [("France", 0, 20), ("Navarra", 20, 150), ("La Rioja", 150, 225),
           ("Castilla y León", 225, 612), ("Galicia", 612, 775)]
# Les dix situations du jeu de rôle, chacune à un lieu du chemin : un tampon
# sur la credencial par situation réussie.
TAMPONS = {"Roncesvalles": 1, "Pamplona": 2, "Puente la Reina": 3, "Logroño": 4,
           "Burgos": 5, "Carrión de los Condes": 6, "León": 7, "O Cebreiro": 8,
           "Sarria": 9, "Santiago de Compostela": 10}


def frise():
    """La frise du chemin, en SVG : les kilomètres de gauche à droite, les
    régions en bandes, les lieux en points, les tampons du jeu de rôle en
    coquilles numérotées. Une frise, pas une carte : on la lit comme une
    progression."""
    W, G, D = 1000, 30, 30
    x = lambda km: G + (W - G - D) * km / 775
    teintes = {"France": "#e8eef6", "Navarra": "#f6ecdc", "La Rioja": "#f3e2e2",
               "Castilla y León": "#f5efd2", "Galicia": "#e2f0e6"}
    s = [f'<svg class="frise" viewBox="0 0 {W} 330" role="img" aria-label="Le Camino francés, '
         f'de Saint-Jean-Pied-de-Port à Santiago, environ 775 km">']
    for nom, a, b in REGIONS:
        s.append(f'<rect x="{x(a):.1f}" y="118" width="{x(b)-x(a):.1f}" height="64" fill="{teintes[nom]}"/>')
        s.append(f'<text x="{(x(a)+x(b))/2:.1f}" y="196" class="reg">{nom}</text>')
    s.append(f'<line x1="{x(0):.1f}" y1="150" x2="{x(775):.1f}" y2="150" class="route"/>')
    # Quatre rangs d'étiquettes (deux au-dessus, deux au-dessous), en tournant :
    # sur deux rangs, Saint-Jean et Pamplona se chevauchaient (vu à l'écran).
    RANGS = [(104, 112, 139), (222, 188, 161), (64, 72, 139), (262, 248, 161)]
    rang = 0
    for nom, km, _, grand in LIEUX:
        cx = x(km)
        if nom in TAMPONS:
            s.append(f'<g class="tampon"><circle cx="{cx:.1f}" cy="150" r="11"/>'
                     f'<text x="{cx:.1f}" y="154.5">{TAMPONS[nom]}</text></g>')
        else:
            s.append(f'<circle cx="{cx:.1f}" cy="150" r="{4.5 if grand else 3}" class="pt"/>')
        if grand:
            y, t1, t2 = RANGS[rang % 4]
            haut = y < 150
            ancre = "start" if km == 0 else ("end" if km == 775 else "middle")
            s.append(f'<line x1="{cx:.1f}" y1="{t1}" x2="{cx:.1f}" y2="{t2}" class="tir"/>')
            court = {"Saint-Jean-Pied-de-Port": "St-Jean-Pied-de-Port",
                     "Santiago de Compostela": "Santiago"}.get(nom, nom)
            s.append(f'<text x="{cx:.1f}" y="{y}" text-anchor="{ancre}" class="lieu">{court}</text>')
            s.append(f'<text x="{cx:.1f}" y="{y + (-16 if haut else 16)}" text-anchor="{ancre}" '
                     f'class="km">km {km}</text>')
            rang += 1
    s.append(f'<text x="{x(0):.1f}" y="22" class="leg">→ vers l\'ouest, ≈ 775 km, une trentaine d\'étapes à pied</text>')
    s.append(f'<g class="tampon"><circle cx="{x(0)+8:.1f}" cy="312" r="9"/><text x="{x(0)+8:.1f}" y="316">n</text></g>'
             f'<text x="{x(0)+24:.1f}" y="317" class="leg">une situation du jeu de rôle — un tampon sur la credencial</text>')
    s.append("</svg>")
    return "\n".join(s)


def etapes_liste():
    lignes = []
    for i, (nom, km, reg, _) in enumerate(LIEUX):
        t = f' <span class="coq">{TAMPONS[nom]}</span>' if nom in TAMPONS else ""
        lignes.append(f"<li><span class=\"k\">{km}</span>{nom}{t}</li>")
    return "\n".join(lignes)


VIGNETTES = [
    ("sjpp", "Saint-Jean-Pied-de-Port", "Le départ, côté français. On y reçoit sa credencial."),
    ("roncesvalles", "Les Pyrénées", "La première journée, la plus dure : plus de 1&nbsp;200&nbsp;m de montée."),
    ("puente-la-reina", "Puente la Reina", "Le pont roman qui a donné son nom à la ville."),
    ("rioja", "La Rioja", "Les vignes : le vin du menú del peregrino vient de là."),
    ("burgos", "Burgos", "La cathédrale gothique, et le premier grand albergue complet."),
    ("meseta", "La Meseta", "Le blé jusqu'à l'horizon, et la flèche jaune."),
    ("cruz-de-ferro", "La Cruz de Ferro", "On y dépose une pierre apportée de chez soi."),
    ("o-cebreiro", "O Cebreiro", "L'entrée en Galice : les panneaux changent de langue."),
    ("santiago", "Santiago", "La place de l'Obradoiro, et la Compostela."),
]


def galerie():
    return "\n".join(
        f'<figure><img src="{IMG}{k}.jpg" alt="{t}" loading="lazy">'
        f'<figcaption><b>{t}</b> {q}</figcaption></figure>' for k, t, q in VIGNETTES)


STYLE = """<style>
.frise{width:100%;height:auto;display:block;margin:6px 0 4px}
.frise .route{stroke:#8a6d1f;stroke-width:3;stroke-dasharray:1 7;stroke-linecap:round}
.frise .pt{fill:var(--body,#222)}
.frise .tir{stroke:var(--line-fort,#bbb);stroke-width:1}
.frise .lieu{font:700 13px Nunito,system-ui,sans-serif;fill:var(--body,#222)}
.frise .km{font:600 11px Nunito,system-ui,sans-serif;fill:var(--muted,#666)}
.frise .reg{font:italic 12px Newsreader,Georgia,serif;fill:var(--muted,#666);text-anchor:middle}
.frise .leg{font:600 12.5px Nunito,system-ui,sans-serif;fill:var(--muted,#666)}
.frise .tampon circle{fill:#f2c230;stroke:#8a6d1f;stroke-width:1.5}
.frise .tampon text{font:800 11px Nunito,system-ui,sans-serif;fill:#3b2e06;text-anchor:middle}
.defile{overflow-x:auto;-webkit-overflow-scrolling:touch}
.defile .frise{min-width:720px}
.galerie{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:14px;margin-top:14px}
.galerie figure{margin:0;background:var(--card,#fff);border:1px solid var(--line,#ddd);border-radius:3px;overflow:hidden}
.galerie img{display:block;width:100%;aspect-ratio:3/2;object-fit:cover;background:#fff}
.galerie figcaption{padding:10px 12px 12px;font-size:14px;line-height:1.4;color:var(--muted,#555)}
.galerie figcaption b{display:block;color:var(--body,#222);font-size:15px}
ol.lieux{columns:3 200px;column-gap:24px;padding:0;margin:12px 0 0;list-style:none;font-size:14.5px}
ol.lieux li{break-inside:avoid;padding:3px 0;border-bottom:1px dotted var(--line,#ddd)}
ol.lieux .k{display:inline-block;min-width:3.2em;font-variant-numeric:tabular-nums;color:var(--muted,#666);font-weight:700}
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
@media (max-width:640px){table.cmp{font-size:14px}table.cmp th,table.cmp td{padding:10px 10px}
  table.cmp td{min-width:9em}}
.coq{display:inline-block;min-width:20px;height:20px;line-height:20px;border-radius:50%;background:#f2c230;
  color:#3b2e06;font-size:11px;font-weight:800;text-align:center;margin-left:4px}
</style>
"""

CORPS = r"""<body>
<div class="doc">

<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>En route vers Compostelle &mdash; le plan</h1>
<p class="chapeau">Pour les <strong>pèlerins francophones</strong> qui partent sur le Camino francés et
veulent se débrouiller en espagnol : trouver un lit, manger, se soigner une ampoule, demander son
chemin, visiter ce qu'il y a à voir d'une étape à l'autre, et parler avec les gens du pays et avec les autres marcheurs. Même châssis que la trousse
de la réception d'hôtel &mdash; planches de mots, exercices, test, jeu de rôle &mdash; mais
l'apprenant change de côté du comptoir : <strong>c'est lui, le client</strong>. Et le jeu de rôle
devient un voyage : dix situations, dix lieux du chemin, un tampon sur la credencial à chaque fois,
jusqu'à Santiago.</p>

<section class="premier">
  <h2>L'idée, en une ligne</h2>
  <div class="these"><p class="cle"><b>Je parle</b> français &nbsp;→&nbsp; <b>j'apprends</b>
  l'espagnol du Chemin. Une direction, un voyage, une credencial à remplir.</p></div>
  <p>L'écran parle français (consignes, explications, rétroactions) ; tout ce qu'on <b>entend</b>
  et qu'on <b>dit</b> est en espagnol. La marque reste francis, le descripteur suit la langue apprise :
  <i>francis &middot; Aide à l'apprentissage de l'espagnol</i>, avec l'étiquette « En route vers Compostelle ».</p>
</section>

<section>
  <h2>Le Camino francés, de Saint-Jean-Pied-de-Port à Santiago</h2>
  <p>Le fil de toute la trousse. Le chemin part de France, au pied des Pyrénées, et passe presque
  tout entier en Espagne : Navarre, La Rioja, Castille-et-León, Galice. Les coquilles jaunes marquent
  les dix situations du jeu de rôle.</p>
  <div class="defile">
FRISE
  </div>
  <div class="galerie">
GALERIE
  </div>
  <details style="margin-top:16px"><summary><b>Les lieux d'étape, kilomètre par kilomètre</b> (≈, selon les guides)</summary>
  <ol class="lieux">
LIEUX
  </ol></details>
</section>

<section>
  <h2>Le chemin, étape par étape : voir, dire, parler</h2>
  <p>Le chemin n'est pas qu'une suite d'albergues. Chaque grand lieu apporte <b>ce qu'on y visite</b>
  (et les mots pour le visiter), <b>une phrase du lieu</b>, et <b>le sujet dont parlent les pèlerins ce
  soir-là</b> — car les conversations du chemin changent avec les kilomètres : les jambes au début, le
  pourquoi sur la Meseta, l'après en arrivant.</p>
  <table class="cmp"><thead><tr><th>Lieu</th><th>À voir</th><th>Ce qu'on y dit</th><th>Entre pèlerins, ce soir-là</th></tr></thead><tbody>
    <tr><td>Saint-Jean-Pied-de-Port</td><td>la rue de la Citadelle, l'accueil des pèlerins</td><td><i>¡Buen Camino!</i> — la première fois</td><td>le sac trop lourd, la peur de la montagne</td></tr>
    <tr><td>Roncesvalles</td><td>la collégiale, la messe des pèlerins ; Roncevaux, où tomba Roland</td><td><i>¿Hay misa del peregrino?</i></td><td>la montée, les jambes, d'où l'on vient</td></tr>
    <tr><td>Pamplona</td><td>la place du Château, le parcours des San Fermín, les <i>pintxos</i> du vieux quartier</td><td><i>Uno de estos, por favor</i></td><td>la nourriture, ce qu'on n'ose pas goûter</td></tr>
    <tr><td>Puente la Reina · Estella</td><td>le pont roman ; la fontaine à vin du monastère d'Irache</td><td><i>¿Es gratis?</i></td><td>le vin, les habitudes de chez soi</td></tr>
    <tr><td>Logroño</td><td>la rue Laurel et ses bars à tapas, le vin de la Rioja</td><td><i>¿Qué me recomienda?</i></td><td>le métier qu'on a laissé, la famille</td></tr>
    <tr><td>Santo Domingo de la Calzada</td><td>le coq et la poule vivants dans la cathédrale, et leur légende</td><td><i>¿Cuál es la historia?</i></td><td>les légendes, les croyances, la foi ou pas</td></tr>
    <tr><td>Burgos</td><td>la cathédrale gothique, le tombeau du Cid</td><td><i>Una entrada, ¿hay descuento para peregrinos?</i></td><td>prendre un jour de repos ou non</td></tr>
    <tr><td>La Meseta</td><td>Castrojeriz, l'église romane de Frómista, le ciel</td><td><i>¡Qué calor!</i></td><td><b>pourquoi on marche</b> ; le silence, la solitude</td></tr>
    <tr><td>León</td><td>les vitraux de la cathédrale, San Isidoro, la maison de Gaudí</td><td><i>¿A qué hora abre la catedral?</i></td><td>les blessures, les tendinites, continuer ou pas</td></tr>
    <tr><td>Astorga</td><td>le palais épiscopal de Gaudí, le chocolat, le <i>cocido maragato</i></td><td><i>¿Qué es el cocido?</i></td><td>la cuisine de chez soi</td></tr>
    <tr><td>Cruz de Ferro</td><td>la croix sur son mât, la pierre qu'on a apportée de chez soi</td><td>—</td><td>ce qu'on laisse derrière soi (le sujet le plus intime du chemin)</td></tr>
    <tr><td>Ponferrada</td><td>le château des Templiers</td><td><i>¿Se puede visitar?</i></td><td>l'histoire, les Templiers</td></tr>
    <tr><td>O Cebreiro</td><td>les <i>pallozas</i>, l'entrée en Galice, la brume</td><td><i>¿Cómo se dice en gallego?</i></td><td>la météo, les langues qu'on parle</td></tr>
    <tr><td>Sarria · Melide</td><td>le départ des « cent kilomètres » ; le poulpe de Melide (<i>pulpo a feira</i>)</td><td><i>Una ración de pulpo para compartir</i></td><td>les nouveaux arrivés, le rythme de chacun</td></tr>
    <tr><td>Santiago</td><td>l'Obradoiro, le Portique de la Gloire, l'étreinte de l'apôtre, le <i>botafumeiro</i> quand il vole ; puis Finisterre</td><td><i>¡Lo hemos conseguido!</i></td><td><b>et après ?</b> Le retour, ce qu'on a appris, se dire au revoir</td></tr>
  </tbody></table>
  <p>Les faits de ce tableau (heures, tarifs, jours du <i>botafumeiro</i>) se <b>vérifient et se datent au
  cadrage</b> : ils changent, et un pèlerin qui se fie à la trousse ne doit pas trouver porte close.</p>
</section>

<section>
  <h2>Ce qui change par rapport à la réception d'hôtel</h2>
  <table class="cmp"><thead><tr><th></th><th>La réception</th><th>En route vers Compostelle</th></tr></thead><tbody>
    <tr><td>Qui apprend</td><td>Un employé, au travail, payé par l'hôtel</td><td>Un voyageur, souvent 50-70 ans, <b>débutant complet</b>, qui a une date de départ : il apprend chez lui, avant, puis sur le chemin</td></tr>
    <tr><td>Son rôle</td><td>Il sert : il accueille, il explique</td><td>Il demande : ce qui compte le plus, c'est de <b>comprendre la réponse</b>, dite vite, avec l'accent du pays</td></tr>
    <tr><td>Langues</td><td>Trois à égalité, six directions</td><td>Une seule direction : français → espagnol d'Espagne. Quelques mots de galicien et de basque à <b>reconnaître</b> sur les panneaux, sans les apprendre</td></tr>
    <tr><td>Le lieu</td><td>Un comptoir, décor fixe</td><td>Une <b>route</b> : cinq ou six décors (l'albergue, le bar, la pharmacie, le sentier, le restaurant, le bureau du pèlerin), et la frise pour avancer</td></tr>
    <tr><td>Où ça sert</td><td>Au poste, avec du réseau</td><td>Sur le chemin, souvent <b>sans réseau</b> : une « poche » hors ligne (phrases et sons dans le téléphone)</td></tr>
    <tr><td>Ce qu'on réutilise</td><td>—</td><td>La mécanique entière ; l'espagnol de l'hôtel est du <b>Mexique</b> (<i>cuarto, boleto, celular, jugo</i>) : le lexique s'écrit à neuf en espagnol d'Espagne (<i>habitación, billete, móvil, zumo</i>)</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le parcours du pèlerin</h2>
  <ol class="simple">
    <li><b>Avant le départ</b>, à la maison, 20 minutes par jour pendant quelques semaines :</li>
    <li style="list-style:none;margin-left:1rem"><b>les mots</b> en planches de croquis, avec la voix et la traduction ; <b>les exercices</b> ; un <b>test</b> « Suis-je prêt ? » ;</li>
    <li style="list-style:none;margin-left:1rem"><b>le chemin joué</b> : dix situations, de Roncesvalles à Santiago, un tampon chaque fois ; une situation manquée se rejoue.</li>
    <li><b>Sur le chemin</b>, dans la poche : les phrases de chaque lieu, avec leur son, sans réseau ; la frise où l'on coche l'étape du jour.</li>
  </ol>
</section>

<section>
  <h2>Volet 1 &mdash; les mots (≈ 190, en onze planches)</h2>
  <table class="cmp"><thead><tr><th>Planche</th><th>Ce qu'on y trouve</th></tr></thead><tbody>
    <tr><td>Le chemin</td><td>la flèche jaune, la coquille, la borne, la credencial, le tampon, l'étape, le bâton, le sac, la montée, la fontaine (eau potable ou non), à gauche, à droite, tout droit</td></tr>
    <tr><td>L'albergue</td><td>albergue municipal ou privé, l'hospitalero, le lit superposé, en haut ou en bas (<i>litera</i>), le sac de couchage, la douche, le casier, la laveuse et la sécheuse, l'étendoir, l'heure de fermeture, <i>completo</i>, la pension, l'hostal</td></tr>
    <tr><td>Manger et boire</td><td>le déjeuner, le <i>menú del peregrino</i>, le <i>menú del día</i> (entrée, plat, dessert), le pain, le vin, l'eau, la bière, le café au lait, le <i>bocadillo</i>, la tortilla, la <i>ración</i>, le <i>pincho</i>, l'addition</td></tr>
    <tr><td>Les heures d'Espagne</td><td>le dîner à 14 h, le souper à 21 h, la sieste, ouvert, fermé, les jours, « ¿a qué hora…? »</td></tr>
    <tr><td>Acheter</td><td>l'épicerie, la boulangerie, le supermarché, combien, les euros, comptant, la carte, le guichet automatique</td></tr>
    <tr><td>Le corps et la pharmacie</td><td>l'ampoule, le pansement, le genou, la cheville, la tendinite, la douleur, la crème, l'ibuprofène, la pharmacie de garde, le centre de santé, le 112</td></tr>
    <tr><td>Le temps qu'il fait</td><td>la pluie, la chaleur, la boue, le brouillard, l'imperméable, le poncho</td></tr>
    <tr><td>Se déplacer</td><td>l'autobus, le taxi, le transport des sacs, la gare, le billet</td></tr>
    <tr><td>Les gens</td><td>« ¡Buen Camino! », se présenter, remercier, s'excuser, demander de l'aide, faire répéter, « más despacio, por favor »</td></tr>
    <tr><td>Visiter</td><td>la cathédrale, le cloître, le musée, le château, le pont, la place principale, l'entrée, le tarif réduit, la visite guidée, l'horaire, la messe, la fête, le marché, la cave à vin</td></tr>
    <tr><td>Entre pèlerins</td><td>d'où tu viens, pourquoi tu marches, depuis quand, jusqu'où, ton métier, ta famille, les ampoules et les genoux, l'étape de demain, où tu dors ce soir, ce que tu as vu, la foi, le retour — au <i>tú</i>, avec les questions qui relancent (<i>¿y tú?</i>)</td></tr>
  </tbody></table>
  <p><b>Les pièges d'un Québécois</b> y ont leur série : <i>la comida</i> est le repas de midi (notre
  dîner), <i>la cena</i> le souper ; <i>constipado</i> veut dire enrhumé ; <i>embarazada</i>, enceinte ;
  <i>largo</i>, long ; <i>la carta</i>, le menu, alors que <i>el menú</i> est le menu du jour ;
  <i>el vaso</i>, un verre ; <i>la propina</i>, le pourboire.</p>
</section>

<section>
  <h2>Volet 2 &mdash; les exercices</h2>
  <ul class="simple">
    <li><b>Je l'entends, je le trouve</b> · <b>Le mot et son image</b> · <b>Je me souviens</b> · <b>La série des pièges</b> — repris de la réception</li>
    <li><b>Ce qu'on me répond</b> — la famille maîtresse : une vraie réponse, dite vite (« Está completo, pero hay una pensión a la vuelta »), et l'on choisit ce qu'elle veut dire</li>
    <li><b>Les nombres, les prix, les heures</b> — « son doce con cincuenta », « cerramos a las diez » ; les leurres construits sur les vraies erreurs d'oreille de l'espagnol (<i>doce</i> / <i>dos</i>, <i>seis</i> / <i>siete</i>)</li>
    <li><b>Où je vais</b> — des indications de chemin, et une petite carte où l'on suit le trajet dit</li>
    <li><b>Je le dis</b> — la situation en français, on la dit en espagnol, puis on écoute le modèle</li>
  </ul>
</section>

<section>
  <h2>Volet 3 &mdash; le test « Suis-je prêt ? »</h2>
  <p>Deux formes parallèles, comme à l'hôtel, la première tirée au hasard. Il ne note pas : il règle
  <b>la vitesse et l'accent</b> des gens du pays au jeu de rôle, et dit ce qu'il reste à travailler avant le départ.</p>
</section>

<section>
  <h2>Volet 4 &mdash; le chemin joué</h2>
  <p>Dix situations, dix lieux, dans l'ordre du chemin. L'IA joue la personne du pays en espagnol ; le
  décor dessiné ne bouge pas, les gens changent devant ; le bilan, en français, dit ce qui a été fait.
  Chaque situation réussie met un <b>tampon sur la credencial</b> ; à Santiago, la Compostela.</p>
  <table class="cmp"><thead><tr><th>Lieu</th><th>Situation</th><th>Le geste qui compte</th></tr></thead><tbody>
    <tr><td><span class="coq">1</span> Roncesvalles</td><td>L'albergue du premier soir</td><td>présenter sa credencial, obtenir une <i>litera</i>, comprendre le prix et l'heure de fermeture</td></tr>
    <tr><td><span class="coq">2</span> Pamplona</td><td>Le bar du matin</td><td>commander le déjeuner, comprendre le total, payer</td></tr>
    <tr><td><span class="coq">3</span> Puente la Reina</td><td>Perdu à la sortie du village</td><td>demander son chemin à un vieil homme qui répond vite, et le suivre</td></tr>
    <tr><td><span class="coq">4</span> Logroño</td><td>La pharmacie</td><td>décrire une ampoule et un genou qui fait mal, comprendre la posologie</td></tr>
    <tr><td><span class="coq">5</span> Burgos</td><td>« Completo »</td><td>l'albergue est plein : comprendre la solution proposée, puis <b>téléphoner</b> à une pension, sans visage</td></tr>
    <tr><td><span class="coq">6</span> Carrión de los Condes</td><td>Une pèlerine sur la Meseta</td><td>tenir deux minutes de conversation : se présenter, d'où, pourquoi, au <i>tú</i></td></tr>
    <tr><td><span class="coq">7</span> León</td><td>Le menú del peregrino</td><td>choisir entrée, plat, dessert ; <b>dire une allergie</b> et comprendre la réponse ; l'addition</td></tr>
    <tr><td><span class="coq">8</span> O Cebreiro</td><td>La pluie et le sac</td><td>comprendre la météo annoncée, faire transporter son sac à l'étape suivante</td></tr>
    <tr><td><span class="coq">9</span> Sarria</td><td>Les cent derniers kilomètres</td><td>les deux tampons par jour, l'épicerie pour le pique-nique, les prix au poids</td></tr>
    <tr><td><span class="coq">10</span> Santiago</td><td>Le bureau du pèlerin</td><td>répondre aux questions pour la Compostela : son nom, d'où l'on est parti, pourquoi</td></tr>
  </tbody></table>
  <p><b>Un compagnon de route.</b> Entre les situations, une même pèlerine, rencontrée à Roncesvalles,
  revient d'étape en étape — au souper de l'albergue, sur un banc, à la fontaine. Chaque fois, deux
  minutes de conversation sur <b>le sujet du lieu</b> (colonne « Entre pèlerins » plus haut) : les
  jambes, la nourriture, pourquoi on marche, ce qu'on laisse à la Cruz de Ferro, et, à Santiago, se dire
  au revoir. Elle se souvient de ce qu'on lui a dit la fois d'avant. Et à chaque ville, une petite
  question de visite (une entrée, un horaire) s'ajoute à la situation du jour.</p>
  <p>Trois paliers de gens du pays, réglés par le test : <b>lent et patient</b> (une autre pèlerine,
  étrangère elle aussi), <b>normal</b>, et <b>rapide, avec l'accent</b> (le vieil homme du village).
  Une erreur y est éliminatoire, et le dira d'avance : <b>l'allergie</b> non dite, ou la réponse du
  serveur mal comprise.</p>
</section>

<section>
  <h2>Volet 5 &mdash; la poche, sans réseau</h2>
  <p>Sur le chemin, le réseau manque souvent. Le site s'installe déjà sur le téléphone (il est
  installable) ; la poche y ajoute, gardés en mémoire : les phrases de chaque lieu avec leur son, la
  frise où l'on coche l'étape du jour, et un bouton « Dites-le plus lentement » en espagnol à montrer
  à l'écran. Le jeu de rôle, lui, a besoin du réseau : il se fait avant le départ.</p>
</section>

<section>
  <h2>Le planning</h2>
  <table class="cmp">
    <thead><tr><th>Étape</th><th>Ce qui sort</th><th>Séances</th></tr></thead>
    <tbody>
      <tr class="d"><td><b>0. Cadrage</b></td><td>Vos décisions (plus bas), les objectifs mesurables, le lexique arrêté, les voix d'Espagne auditionnées, trois croquis témoins, les faits du chemin vérifiés.</td><td class="num">1</td></tr>
      <tr><td><b>1. Les mots</b></td><td>≈ 190 croquis, onze planches, voix, traduction.</td><td class="num">3</td></tr>
      <tr><td><b>2. Les décors</b></td><td>Six décors du chemin, les gens du pays (cinq visages, quatre expressions), la frise et la credencial.</td><td class="num">2</td></tr>
      <tr><td><b>3. Les exercices</b></td><td>Les huit familles. <b>Point d'arrêt : jouable par un pèlerin.</b></td><td class="num">2</td></tr>
      <tr><td><b>4. Le test</b></td><td>Deux formes nivelées.</td><td class="num">1</td></tr>
      <tr><td><b>5. Le chemin joué</b></td><td>Dix situations en trois paliers, les conversations du compagnon de route, le bilan en français.</td><td class="num">3</td></tr>
      <tr><td><b>6. La poche</b></td><td>Le mode hors ligne, la frise à cocher.</td><td class="num">1</td></tr>
      <tr class="f"><td><b>7. Audit et pilote</b></td><td>La boucle didactique (au moins trois tours), puis quelques pèlerins qui partent pour vrai.</td><td class="num">2</td></tr>
      <tr><td><b>8. L'emballage</b></td><td>Le carnet de poche à imprimer, la page de présentation, la fiche au classeur.</td><td class="num">1</td></tr>
    </tbody>
  </table>
  <div class="chiffres">
    <div class="ch"><span class="n">16</span><span class="q">séances de travail</span></div>
    <div class="ch"><span class="n">≈&nbsp;240</span><span class="q">images : 190 objets et lieux, 6 décors, les gens, les vignettes ≈ 16&nbsp;$</span></div>
    <div class="ch"><span class="n">≈&nbsp;1&nbsp;100</span><span class="q">extraits de voix d'Espagne chez Azure, quelques dollars</span></div>
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;¢</span><span class="q">par situation jouée, mesure de Francœur</span></div>
  </div>
  <div class="reserve"><p><strong>Trois limites à dire tout de suite :</strong> l'espagnol doit être
  <b>relu par une personne d'Espagne</b> avant d'être offert. Les faits du chemin (heures, règles du
  bureau du pèlerin, les deux tampons par jour des cent derniers kilomètres) se vérifient au cadrage
  et se datent : ils changent. Et c'est la première trousse <b>grand public</b> : elle ne se vend pas
  comme une formation en entreprise &mdash; la question de sa diffusion est la dernière décision.</p></div>
</section>

<section>
  <h2>Les décisions</h2>
  <p>Chacune a une recommandation ; un clic la retient. Le bouton du bas rend un texte à recoller dans
  la conversation : c'est lui qui pilote la suite.</p>
  <div id="decisions"></div>
  <p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied">
  <p>Plan du 25 septembre 2026 · « En route vers Compostelle ».</p>
  <p>Produit par <code>build/compostelle_plan.py</code> — ne pas l'éditer.</p>
</div>

</div>
<script>
(function(){
  var D = [
    {k:'variete', q:"L'espagnol enseigné",
     o:[['espagne',"L'espagnol d'Espagne (castillan) : habitación, móvil, zumo ; les voix d'Espagne",true],
        ['neutre','Un espagnol « neutre », compris partout',false],
        ['hotel',"Reprendre l'espagnol du Mexique de la trousse d'hôtel",false]],
     w:"C'est celui qu'on entend sur le chemin. Le lexique de l'hôtel ne se reprend pas tel quel : ses mots et ses voix sont mexicains."},
    {k:'registre', q:'Tú, usted, vosotros',
     o:[['tu-usted','Le tú entre pèlerins, l\'usted avec les aînés et au comptoir ; le vosotros reconnu à l\'oreille, pas exercé',true],
        ['usted','Tout à l\'usted, pour simplifier',false],
        ['tout','Les trois, exercés',false]],
     w:"En Espagne, le tú est partout ; l'hospitalero dira « ¿Vosotros dos venís juntos? » : il faut le comprendre, pas le produire."},
    {k:'galicien', q:'Le galicien et le basque',
     o:[['reconnaitre','Reconnaître une vingtaine de mots sur les panneaux (rúa, igrexa, praza…), sans les apprendre',true],
        ['ignorer','Les ignorer',false]],
     w:"Les cent derniers kilomètres sont en Galice, où les panneaux sont d'abord en galicien ; en Navarre, on croise le basque."},
    {k:'chemin', q:'Le chemin',
     o:[['frances','Le Camino francés seul, de Saint-Jean-Pied-de-Port à Santiago',true],
        ['plusieurs','Aussi le chemin portugais et le chemin du Nord',false]],
     w:"Le plus fréquenté, et celui des départs du Québec. Les situations servent sur les autres chemins espagnols ; seul le décor changerait."},
    {k:'progression', q:'Le fil ludique',
     o:[['credencial','La credencial : un tampon dessiné par situation réussie, la Compostela à la fin',true],
        ['frise','La frise seule, cochée étape par étape',false],
        ['aucun','Une liste simple',false]],
     w:"C'est l'objet que tout pèlerin connaît et collectionne ; il donne au jeu de rôle un but qui a du sens hors de l'écran."},
    {k:'decors', q:'Les décors du jeu de rôle',
     o:[['six','Six décors dessinés (albergue, bar, pharmacie, sentier, restaurant, bureau du pèlerin), les gens changent devant',true],
        ['un','Un seul décor pour tout',false],
        ['voix','Sans décor, la voix seule',false]],
     w:"Chaque lieu a sa façon de parler ; six scènes à la croquis-sequence coûtent peu (≈ 0,40 $) et tiennent d'un plan à l'autre."},
    {k:'poche', q:'La poche hors ligne',
     o:[['oui','Oui : phrases et sons gardés dans le téléphone, la frise à cocher',true],
        ['non','Non : tout se fait avant le départ',false]],
     w:"Sur la Meseta ou en Galice, le réseau manque ; c'est au moment de parler qu'on en a besoin."},
    {k:'compagnon', q:'Le compagnon de route',
     o:[['oui','Une même pèlerine revient d\'étape en étape, avec le sujet de conversation du lieu, et se souvient de la fois d\'avant',true],
        ['divers','Un pèlerin différent à chaque étape',false],
        ['non','Pas de conversation entre pèlerins hors de la situation 6',false]],
     w:"C'est ce que racontent les pèlerins au retour : les gens qu'on retrouve. Et la conversation qui revient est la meilleure pratique orale de la trousse."},
    {k:'voix', q:'Les voix',
     o:[['azure','Azure HD, voix d\'Espagne (es-ES), auditionnées au cadrage',true],['autre','Un autre fournisseur',false]],
     w:"La même chaîne que l'hôtel, avec la vérification par retranscription ; il faut votre feu vert pour les ≈ 1 100 extraits."},
    {k:'couleurs', q:'Les couleurs',
     o:[['francis-jaune','Le thème francis, avec le jaune de la flèche comme seul accent (coquilles, tampons)',true],
        ['francis','Le thème francis tel quel',false],
        ['propre','Une palette propre au chemin, à proposer comme pour l\'hôtel',false]],
     w:"Le jaune de la flèche est le signe du chemin ; réservé à la progression, il ne se confond avec rien d'autre."},
    {k:'diffusion', q:'Pour qui, et comment',
     o:[['pilote','D\'abord un pilote gratuit avec quelques pèlerins qui partent ce printemps ; le modèle d\'affaires ensuite',true],
        ['vente','Une vente directe au public dès la sortie',false],
        ['associations','Une offre aux associations de pèlerins, qui la donnent à leurs membres',false]],
     w:"Première trousse grand public : on apprend ce qui sert vraiment avant de fixer un prix. Les associations viennent naturellement après le pilote."}
  ];
  var CLE='plan-compostelle', choix={};
  try{ choix=JSON.parse(localStorage.getItem(CLE)||'{}'); }catch(e){}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){
    var div=document.createElement('div'); div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p><div class="opts">';
    d.o.forEach(function(o){
      h+='<button type="button" class="opt'+(o[2]?' reco':'')+'" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'
        +o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';
    });
    div.innerHTML=h+'</div><p class="dw">'+d.w+'</p>';
    zone.appendChild(div);
  });
  function peindre(){
    zone.querySelectorAll('.opt').forEach(function(b){
      b.setAttribute('aria-pressed', choix[b.dataset.k]===b.dataset.v ? 'true':'false');
    });
    var n=Object.keys(choix).length;
    document.getElementById('etat').textContent = n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }
  zone.addEventListener('click',function(e){
    var b=e.target.closest('.opt'); if(!b) return;
    if(choix[b.dataset.k]===b.dataset.v) delete choix[b.dataset.k]; else choix[b.dataset.k]=b.dataset.v;
    try{ localStorage.setItem(CLE,JSON.stringify(choix)); }catch(e){}
    peindre();
  });
  document.getElementById('exporter').addEventListener('click',function(){
    var out={plan:'compostelle', date:new Date().toISOString().slice(0,10), decisions:{}};
    D.forEach(function(d){
      var v=choix[d.k]; var o=d.o.filter(function(x){return x[0]===v;})[0];
      out.decisions[d.k]= o ? o[1] : null;
    });
    var t=JSON.stringify(out,null,2);
    var fin=function(){ document.getElementById('etat').textContent='Copié — à recoller dans la conversation.'; };
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){prompt('Copiez :',t);});
    else prompt('Copiez :',t);
  });
  peindre();
})();
</script>
</body>
</html>
"""


def main():
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>En route vers Compostelle — le plan</title>", tete)
    tete = tete.replace("</head>", STYLE + "</head>")
    corps = (CORPS.replace("FRISE", frise()).replace("GALERIE", galerie())
             .replace("LIEUX", etapes_liste()))
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
