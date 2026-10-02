#!/usr/bin/env python3
"""Le plan de « Une semaine à Toronto » — l'anglais du touriste francophone.

    python3 build/toronto_plan.py   # → assets/presentations/toronto/toronto-plan.html

Demande de Daniel, 1er octobre 2026 : « à l'image de Compostelle, mais cette
fois pour apprendre l'anglais. Une visite à Toronto. Visites, restaurant,
hôtel, etc. Tout pour qu'un touriste francophone apprenne à se débrouiller en
anglais. »

Temps 0a de la méthode `trousse-de-metier` : le plan et ses décisions, rien
d'autre. La page reprend l'en-tête du plan de la Maison Francœur, comme celui de
Compostelle (build/compostelle_plan.py), dont elle suit le découpage. Aucune
image payée : le crédit Google est épuisé depuis le 30 septembre ; le plan du
métro est dessiné en SVG.
"""
import pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "toronto" / "toronto-plan.html"

# Le plan schématique du centre-ville : la ligne 1 en U (Union au fond), la
# ligne 2 en travers sur Bloor, le tramway 510 sur Spadina, l'UP Express vers
# l'aéroport et le traversier des îles. Un schéma, pas une carte à l'échelle.
# (n°, lieu, x, y, ancre du texte, décalage x, décalage y)
CARTES = [
    (1, "Union Station", 470, 420, "start", 20, 24),
    (2, "L'hôtel, rue King", 560, 365, "start", 18, 5),
    (3, "Le café du matin", 560, 290, "start", 18, 5),
    (4, "La tour CN", 330, 448, "end", -18, 5),
    (5, "Le marché St. Lawrence", 650, 410, "start", 16, 5),
    (6, "Kensington et le quartier chinois", 255, 300, "end", -16, 5),
    (9, "Le restaurant, Little Italy", 255, 215, "end", -16, 5),
    (8, "La pharmacie, Yonge", 560, 200, "start", 18, 5),
    (7, "Les îles de Toronto", 560, 505, "start", 16, 5),
    (10, "Le départ, Pearson", 75, 352, "middle", 0, 32),
]
STATIONS_L1_OUEST = [("St George", 120), ("Museum", 170), ("Queen's Park", 215),
                     ("St Patrick", 265), ("Osgoode", 315), ("St Andrew", 365)]
STATIONS_L1_EST = [("Bloor-Yonge", 120), ("Wellesley", 200), ("College", 245),
                   ("Dundas", 290), ("Queen", 330), ("King", 365)]


def plan_metro():
    s = ['<svg class="plan" viewBox="0 0 1000 560" role="img" aria-label="Plan schématique du centre-ville de '
         'Toronto : la ligne 1 du métro en U autour d\'Union Station, la ligne 2 sur la rue Bloor, et les dix '
         'lieux des situations jouées">']
    s.append('<rect x="0" y="470" width="1000" height="90" class="lac"/>')
    s.append('<text x="980" y="545" text-anchor="end" class="eau">Lac Ontario</text>')
    s.append('<ellipse cx="540" cy="520" rx="120" ry="18" class="ile"/>')
    # Ligne 2, sur Bloor
    s.append('<line x1="110" y1="120" x2="900" y2="120" class="l2"/>')
    s.append('<text x="110" y="100" class="ligne">Ligne 2 · Bloor-Danforth</text>')
    s.append('<text x="900" y="100" text-anchor="end" class="rue">vers Danforth (Greektown)</text>')
    # Ligne 1 en U
    s.append('<path d="M380 120 V395 Q380 420 405 420 H535 Q560 420 560 395 V120" class="l1"/>')
    s.append('<text x="470" y="62" text-anchor="middle" class="ligne">Ligne 1 · Yonge-University</text>')
    for nom, y in STATIONS_L1_OUEST:
        ty = y - 14 if y == 120 else y + 4  # sur Bloor, le nom passe au-dessus de la ligne 2
        s.append(f'<circle cx="380" cy="{y}" r="5" class="st"/><text x="368" y="{ty}" text-anchor="end" class="nst">{nom}</text>')
    for nom, y in STATIONS_L1_EST:
        if y in (200, 290, 365):
            continue  # ces trois portent une carte postale
        ty = y - 14 if y == 120 else y + 4
        s.append(f'<circle cx="560" cy="{y}" r="5" class="st"/><text x="572" y="{ty}" class="nst">{nom}</text>')
    # Tramway 510 Spadina, UP Express, traversier
    s.append('<line x1="255" y1="120" x2="255" y2="430" class="tram"/>')
    s.append('<text x="243" y="150" text-anchor="end" class="rue">tramway 510 Spadina</text>')
    s.append('<path d="M450 420 C300 420 160 400 85 345" class="up"/>')
    s.append('<text x="95" y="425" class="rue">UP Express · ≈ 25 min</text>')
    s.append('<line x1="520" y1="470" x2="545" y2="505" class="bac"/>')
    s.append('<text x="508" y="492" text-anchor="end" class="rue eau-lieu">traversier</text>')
    for n, lieu, x, y, ancre, dx, dy in CARTES:
        s.append(f'<g class="carte"><rect x="{x-13}" y="{y-10}" width="26" height="20" rx="2"/>'
                 f'<text x="{x}" y="{y+4.5}">{n}</text></g>')
        sur_eau = " eau-lieu" if y >= 470 else ""  # le lac reste clair en mode sombre : texte foncé
        s.append(f'<text x="{x+dx}" y="{y+dy}" text-anchor="{ancre}" class="lieu{sur_eau}">{lieu}</text>')
    s.append('<g class="carte"><rect x="17" y="18" width="22" height="16" rx="2"/><text x="28" y="30">n</text></g>'
             '<text x="48" y="31" class="leg">une situation jouée — une carte postale à gagner, et à écrire</text>')
    s.append("</svg>")
    return "\n".join(s)


STYLE = """<style>
.plan{width:100%;height:auto;display:block;margin:8px 0 4px}
.plan .lac{fill:#dbe8f1}.plan .ile{fill:#e4efdc;stroke:#9fbf8f}
.plan .eau{font:italic 14px Newsreader,Georgia,serif;fill:#4d6a80}
.plan .l1{fill:none;stroke:#e8b400;stroke-width:9;stroke-linejoin:round}
.plan .l2{stroke:#1b8a4c;stroke-width:9}
.plan .tram{stroke:#c8102e;stroke-width:3;stroke-dasharray:2 6;stroke-linecap:round}
.plan .up{fill:none;stroke:#6b7a88;stroke-width:3;stroke-dasharray:8 6}
.plan .bac{stroke:#4d6a80;stroke-width:2.5;stroke-dasharray:4 5}
.plan .st{fill:#fff;stroke:#333;stroke-width:2}
.plan .nst{font:600 11.5px Nunito,system-ui,sans-serif;fill:var(--muted,#666)}
.plan .ligne{font:800 13px Nunito,system-ui,sans-serif;fill:var(--body,#222)}
.plan .rue{font:italic 12px Newsreader,Georgia,serif;fill:var(--muted,#666)}
.plan .lieu{font:700 13px Nunito,system-ui,sans-serif;fill:var(--body,#222)}
.plan .eau-lieu{fill:#1f3346}
.plan .leg{font:600 12.5px Nunito,system-ui,sans-serif;fill:var(--muted,#666)}
.plan .carte rect{fill:#fff;stroke:#7a3b1d;stroke-width:1.6}
.plan .carte text{font:800 12px Nunito,system-ui,sans-serif;fill:#7a3b1d;text-anchor:middle}
.defile{overflow-x:auto;-webkit-overflow-scrolling:touch}
.defile .plan{min-width:720px}
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
@media (max-width:640px){table.cmp{font-size:14px}table.cmp th,table.cmp td{padding:10px 10px}
  table.cmp td{min-width:9em}}
.cp{display:inline-block;min-width:22px;height:18px;line-height:16px;border:1.5px solid #7a3b1d;border-radius:2px;
  color:#7a3b1d;font-size:11px;font-weight:800;text-align:center;margin-right:4px;background:#fff}
</style>
"""

CORPS = r"""<body>
<div class="doc">

<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Voyage &middot; grand public &middot; anglais</p>
<h1>Une semaine à Toronto &mdash; le plan</h1>
<p class="chapeau">Pour les <strong>touristes francophones</strong> qui partent quelques jours à Toronto et
veulent se débrouiller en anglais : arriver, prendre le métro, s'installer à l'hôtel, commander un café,
visiter, manger au restaurant, se soigner, demander son chemin, et parler avec les gens de la ville. Même
châssis que Compostelle &mdash; la préparation à la maison, les mots, les exercices, le test, le jeu de
rôle &mdash; avec la même idée de fond : <strong>l'apprenant est le client</strong>. Le chemin devient une
semaine en ville : dix situations, dix lieux, une carte postale à chaque fois.</p>

<section class="premier">
  <h2>L'idée, en une ligne</h2>
  <div class="these"><p class="cle"><b>Je parle</b> français &nbsp;→&nbsp; <b>j'apprends</b>
  l'anglais d'une semaine à Toronto. Une direction, une ville, dix cartes postales à gagner.</p></div>
  <p>L'écran parle français (consignes, explications, rétroactions) ; tout ce qu'on <b>entend</b> et qu'on
  <b>dit</b> est en anglais. La marque reste francis, le descripteur suit la langue apprise :
  <i>francis &middot; Aide à l'apprentissage de l'anglais</i>, avec l'étiquette « Une semaine à Toronto ».</p>
</section>

<section>
  <h2>La ville, en dix lieux</h2>
  <p>Le fil de toute la trousse. On arrive à Union Station, on loge au centre-ville, et la semaine rayonne le
  long de la ligne 1 du métro, du tramway de Spadina et du traversier des îles. Les cartes postales numérotées
  marquent les dix situations jouées.</p>
  <div class="defile">
PLAN
  </div>
</section>

<section>
  <h2>La semaine, jour par jour : voir, dire, parler</h2>
  <p>Chaque journée apporte <b>ce qu'on y visite</b> (et les mots pour le visiter), <b>une phrase du lieu</b>,
  et <b>le sujet de conversation du jour</b> avec les gens de la ville. Le petit bavardage
  (<i>small talk</i>) est une institution au Canada anglais : savoir y répondre est la moitié du voyage.</p>
  <table class="cmp"><thead><tr><th>Jour</th><th>À voir</th><th>Ce qu'on y dit</th><th>On parle de…</th></tr></thead><tbody>
    <tr><td>1 · L'arrivée</td><td>Union Station, le quartier financier, le PATH (la ville souterraine)</td><td><i>Which way to the subway?</i></td><td>d'où l'on vient, le voyage</td></tr>
    <tr><td>2 · Le centre</td><td>la tour CN, l'aquarium, le Rogers Centre, la rue King</td><td><i>Two adults, please. Is there a timed entry?</i></td><td>la météo (le sujet canadien par excellence)</td></tr>
    <tr><td>3 · Le vieux Toronto</td><td>le marché St. Lawrence et son sandwich au bacon de dos, le quartier de la Distillerie</td><td><i>Can I get a peameal bacon sandwich?</i></td><td>la nourriture, ce qu'on mange chez soi</td></tr>
    <tr><td>4 · Les quartiers</td><td>Kensington Market, le quartier chinois de Spadina, Queen Street West</td><td><i>Does this streetcar go to Kensington?</i></td><td>la ville de toutes les langues : la moitié des Torontois sont nés ailleurs</td></tr>
    <tr><td>5 · Les îles</td><td>le traversier, les îles, la ville vue du lac, le vélo</td><td><i>Can I rent a bike for two hours?</i></td><td>les vacances, ce qu'on aime faire</td></tr>
    <tr><td>6 · Le musée et le soir</td><td>le Musée royal de l'Ontario, Yorkville, un match (les Blue Jays, les Maple Leafs)</td><td><i>Do you have a table for two?</i></td><td>le sport, le hockey, Montréal et Toronto</td></tr>
    <tr><td>7 · Le départ</td><td>la facture, l'UP Express vers l'aéroport, ou le train de VIA vers Montréal</td><td><i>I think there's a mistake on my bill.</i></td><td>ce qu'on a vu, revenir, se dire au revoir</td></tr>
  </tbody></table>
  <p>Les faits de ce tableau (tarifs du métro, heures, prix d'entrée) se <b>vérifient et se datent au
  cadrage</b> : ils changent, et un touriste qui se fie à la trousse ne doit pas trouver porte close.</p>
</section>

<section>
  <h2>Ce qui change par rapport à Compostelle</h2>
  <table class="cmp"><thead><tr><th></th><th>Compostelle</th><th>Une semaine à Toronto</th></tr></thead><tbody>
    <tr><td>Qui apprend</td><td>Un pèlerin, débutant complet en espagnol</td><td>Un touriste qui a souvent <b>des restes d'anglais</b> (l'école, la télé) mais qui fige quand on lui répond vite : un faux débutant, le plus souvent</td></tr>
    <tr><td>Le voyage</td><td>Un mois à pied, 775 km, sans réseau par moments</td><td>Un week-end ou une semaine en ville, avec du réseau presque partout ; la poche hors ligne sert surtout dans le métro</td></tr>
    <tr><td>La langue</td><td>L'espagnol d'Espagne, une seule variété</td><td>L'anglais du Canada (<i>washroom, toque, loonie</i>, l'orthographe <i>colour, centre</i>), et <b>les accents de Toronto</b> : la ville de toutes les langues, où l'on entend l'anglais avec l'accent de l'Inde, de la Jamaïque, de la Chine, du Portugal</td></tr>
    <tr><td>Les pièges</td><td>Ceux d'un Québécois en espagnol</td><td>Les <b>faux amis</b> du français, nombreux en anglais, et les pièges d'oreille des nombres (<i>thirteen / thirty</i>)</td></tr>
    <tr><td>Le fil ludique</td><td>La credencial à tampons</td><td>Des <b>cartes postales</b> : une par situation réussie, dessinée, et qu'on écrit soi-même en deux lignes d'anglais</td></tr>
    <tr><td>Ce qu'on réutilise</td><td>—</td><td>Toute la mécanique de Compostelle (préparation, planches, exercices, test, jeu de rôle, vente par code) ; le <b>lexique anglais nord-américain</b> de la réception d'hôtel et ses voix anglaises ; les textes anglais de Montréal en poche</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le parcours du touriste</h2>
  <ol class="simple">
    <li><b>Avant de partir</b>, à la maison, 15 minutes par séance, comme pour Compostelle : les sons de
    l'anglais qui trompent un francophone (<i>th</i>, le <i>h</i> qu'on prononce, <i>ship / sheep</i>), les nombres
    et les prix, l'heure, les questions qui servent partout (<i>Can I…? Where is…? How much…?</i>), se présenter,
    et surtout <b>comprendre la réponse</b>. Un test « Prêt à partir ? » règle la suite.</li>
    <li><b>Les mots</b> en planches de croquis, avec la voix et la traduction ; <b>les exercices</b>.</li>
    <li><b>La semaine jouée</b> : dix situations, de l'arrivée à Union Station au départ, une carte postale chaque fois ;
    une situation manquée se rejoue.</li>
    <li><b>Sur place</b>, dans la poche : les phrases de chaque lieu avec leur son, l'aide-mémoire du pourboire
    et des taxes, et un écran « <i>Could you say that again, more slowly?</i> » à montrer.</li>
  </ol>
</section>

<section>
  <h2>Volet 1 &mdash; les mots (≈ 200, en douze planches)</h2>
  <table class="cmp"><thead><tr><th>Planche</th><th>Ce qu'on y trouve</th></tr></thead><tbody>
    <tr><td>Arriver et se déplacer</td><td>la gare, le quai, le métro, le tramway, l'autobus, la correspondance, la carte de transport, payer en touchant sa carte, le traversier, le taxi, la sortie, l'intersection (<i>Queen and Spadina</i>), nord, sud, est, ouest, un coin de rue (<i>a block</i>)</td></tr>
    <tr><td>L'hôtel</td><td>la réservation, l'arrivée et le départ, la chambre, le lit double ou deux lits, la carte-clé, le dépôt, le wifi, le déjeuner inclus, la serviette, la femme de chambre, l'ascenseur, le hall</td></tr>
    <tr><td>Le café</td><td>les grandeurs (<i>small, medium, large</i>), le lait, le sucre, sur place ou pour emporter, le muffin, le bagel, <i>double-double</i>, l'eau, la paille, le reçu</td></tr>
    <tr><td>Le restaurant</td><td>la table, le menu, l'entrée (<i>appetizer</i>), le plat principal, le dessert, l'eau du robinet, la cuisson, sans gluten, végétarien, la viande, le bouillon, l'addition, payer séparément, le pourboire</td></tr>
    <tr><td>Payer</td><td>les prix (<i>four ninety-nine</i>), la taxe ajoutée à la caisse (la TVH de l'Ontario), le <i>loonie</i> et le <i>toonie</i>, comptant, la carte, débit ou crédit, le terminal qu'on vous tend, « <i>Do you need a bag?</i> »</td></tr>
    <tr><td>Visiter</td><td>le billet, l'entrée à heure fixe, le tarif réduit, aîné, enfant, la visite guidée, l'audioguide, le vestiaire, la boutique, ouvert, fermé, le musée, la galerie, le marché</td></tr>
    <tr><td>Magasiner</td><td>la taille, essayer, la cabine, plus grand, plus petit, l'échange, le remboursement, en solde, la caisse</td></tr>
    <tr><td>Le corps et la pharmacie</td><td>la tête, le ventre, la gorge, la fièvre, le coup de soleil, l'ampoule, le comprimé, sans ordonnance, deux fois par jour, la pharmacie, la clinique sans rendez-vous, le 911</td></tr>
    <tr><td>Le temps qu'il fait</td><td>chaud, froid, humide, la pluie, la neige, le vent, les degrés (Celsius, comme chez nous), « <i>Nice day, eh?</i> »</td></tr>
    <tr><td>L'heure et les jours</td><td><i>quarter past, half past, quarter to</i>, a.m. et p.m., aujourd'hui, demain, ce soir, les jours de la semaine</td></tr>
    <tr><td>Les gens</td><td>saluer, remercier, s'excuser (<i>sorry</i>, dit à tout propos), faire répéter, épeler son nom, demander de l'aide, « <i>No worries</i> », « <i>You're welcome</i> »</td></tr>
    <tr><td>Le petit bavardage</td><td>d'où tu viens, combien de temps tu restes, ce que tu as vu, ce que tu fais dans la vie, la météo, le sport, la nourriture, et les questions qui relancent (<i>And you? How about you?</i>)</td></tr>
  </tbody></table>
  <p><b>Les pièges d'un francophone</b> y ont leur série, chacun dans une phrase de voyage :
  <i>actually</i> veut dire « en fait » et non « actuellement » ; <i>eventually</i>, « finalement » ;
  <i>a library</i>, une bibliothèque ; <i>to attend</i>, assister à ; <i>to assist</i>, aider ;
  <i>sensible</i>, raisonnable ; <i>a location</i>, un endroit ; <i>deception</i>, une tromperie ;
  <i>a bill</i>, l'addition ou un billet de banque. Et celui d'un Québécois : <b>le <i>dinner</i>, c'est le
  souper</b>, et notre dîner se dit <i>lunch</i>.</p>
</section>

<section>
  <h2>Volet 2 &mdash; les exercices</h2>
  <ul class="simple">
    <li><b>Je l'entends, je le trouve</b> · <b>Le mot et son image</b> · <b>Je me souviens</b> · <b>La série des pièges</b> — repris de Compostelle</li>
    <li><b>Ce qu'on me répond</b> — la famille maîtresse : une vraie réponse, dite vite (« <i>We're full tonight, but there's a spot at the bar</i> »), et l'on choisit ce qu'elle veut dire</li>
    <li><b>Les nombres, les prix, les heures</b> — « <i>that's twelve fifty</i> », « <i>we close at quarter to ten</i> » ; les leurres bâtis sur les vraies erreurs d'oreille (<i>thirteen / thirty, fifteen / fifty</i>)</li>
    <li><b>Où je vais</b> — des indications dites en coins de rue (« <i>two blocks north, then left on Queen</i> »), sur un petit plan où l'on suit le trajet</li>
    <li><b>Le total à payer</b> — un prix affiché, la taxe ajoutée, le pourboire choisi au terminal : combien ça coûte vraiment</li>
    <li><b>Je le dis</b> — la situation en français, on la dit en anglais, puis on écoute le modèle</li>
    <li><b>J'écris ma carte postale</b> — deux lignes au dos de la carte gagnée ; l'assistance les relit, sans les réécrire à la place</li>
  </ul>
</section>

<section>
  <h2>Volet 3 &mdash; le test « Prêt à partir ? »</h2>
  <p>Deux formes parallèles, la première tirée au hasard, comme pour Compostelle. Il ne note pas : il règle
  <b>la vitesse et l'accent</b> des gens de la ville au jeu de rôle, et dit ce qu'il reste à travailler.
  Un faux débutant qui le réussit saute la préparation ; un débutant y est renvoyé.</p>
</section>

<section>
  <h2>Volet 4 &mdash; la semaine jouée</h2>
  <p>Dix situations, dix lieux, dans l'ordre de la semaine. L'assistance joue la personne de la ville en
  anglais ; le décor dessiné ne bouge pas, les gens changent devant ; le bilan, en français, dit ce qui a été
  fait. Chaque situation réussie donne une <b>carte postale</b> du lieu, qu'on écrit soi-même.</p>
  <table class="cmp"><thead><tr><th>Lieu</th><th>Situation</th><th>Le geste qui compte</th></tr></thead><tbody>
    <tr><td><span class="cp">1</span>Union Station</td><td>L'arrivée</td><td>trouver le métro, payer son passage, comprendre l'annonce du quai</td></tr>
    <tr><td><span class="cp">2</span>L'hôtel</td><td>L'arrivée à la réception</td><td>donner son nom et <b>l'épeler</b>, comprendre le dépôt, l'heure du déjeuner, le code du wifi</td></tr>
    <tr><td><span class="cp">3</span>Le café</td><td>Le café du matin</td><td>commander vite, comprendre « <i>Anything else? For here or to go?</i> », payer au terminal</td></tr>
    <tr><td><span class="cp">4</span>La tour CN</td><td>Les billets</td><td>acheter deux billets à heure fixe, comprendre l'heure de montée et le tarif</td></tr>
    <tr><td><span class="cp">5</span>Le marché St. Lawrence</td><td>Au comptoir</td><td>commander au poids, comprendre le total <b>taxe comprise</b></td></tr>
    <tr><td><span class="cp">6</span>Kensington</td><td>Perdu dans les quartiers</td><td>demander son chemin à quelqu'un qui répond vite, avec un accent, et le suivre en coins de rue</td></tr>
    <tr><td><span class="cp">7</span>Les îles</td><td>Le traversier et le vélo</td><td>acheter le passage, louer un vélo, comprendre l'heure du dernier bateau</td></tr>
    <tr><td><span class="cp">8</span>La pharmacie</td><td>Un coup de soleil, au lendemain des îles</td><td>décrire, comprendre la posologie</td></tr>
    <tr><td><span class="cp">9</span>Le restaurant</td><td>Le souper</td><td>avoir une table, commander, <b>dire qu'on ne mange pas de viande</b> et comprendre la réponse, payer séparément, laisser le pourboire</td></tr>
    <tr><td><span class="cp">10</span>Le départ</td><td>Une erreur sur la facture</td><td><b>contester poliment</b> un montant, comprendre la solution, demander le chemin de l'UP Express</td></tr>
  </tbody></table>
  <p><b>Une connaissance de la ville.</b> Entre les situations, une même Torontoise, croisée au café le
  premier matin, revient de jour en jour &mdash; au marché, sur le traversier, au match. Chaque fois, deux
  minutes de bavardage sur <b>le sujet du jour</b> (colonne « On parle de… » plus haut), et elle se souvient de
  ce qu'on lui a dit la fois d'avant. Le dernier jour, on se dit au revoir.</p>
  <p>Trois paliers, réglés par le test : <b>lent et patient</b>, <b>normal</b>, et <b>rapide, avec les
  accents de Toronto</b>. Une erreur y est éliminatoire, et le dira d'avance : <b>« je ne mange pas de viande »</b> non dit, ou
  la réponse du serveur mal comprise (l'allergie de la première version a été remplacée par le régime végétarien le 2 oct. 2026).</p>
</section>

<section>
  <h2>Volet 5 &mdash; la poche</h2>
  <p>Gardés dans le téléphone, sans réseau : les phrases de chaque lieu avec leur son, l'aide-mémoire « ce que
  ça coûte vraiment » (le prix affiché, plus 13 % de taxe, plus le pourboire de 18 à 20 % au restaurant), et
  l'écran « Dites-le plus lentement » en anglais. Le jeu de rôle, lui, a besoin du réseau.</p>
</section>

<section>
  <h2>Le planning</h2>
  <table class="cmp">
    <thead><tr><th>Étape</th><th>Ce qui sort</th><th>Séances</th></tr></thead>
    <tbody>
      <tr class="d"><td><b>0. Cadrage</b></td><td>Vos décisions (plus bas), les objectifs mesurables, le lexique arrêté, les voix anglaises auditionnées, trois croquis témoins, les faits de la ville vérifiés et datés.</td><td class="num">1</td></tr>
      <tr><td><b>1. Avant de partir</b></td><td>Les huit séances de préparation, reprises de Compostelle et réécrites pour l'anglais.</td><td class="num">2</td></tr>
      <tr><td><b>2. Les mots</b></td><td>≈ 200 croquis, douze planches, voix, traduction.</td><td class="num">3</td></tr>
      <tr><td><b>3. Les décors</b></td><td>Dix décors de la ville, les gens de Toronto (six visages, quatre expressions), le plan et les cartes postales.</td><td class="num">2</td></tr>
      <tr><td><b>4. Les exercices</b></td><td>Les dix familles. <b>Point d'arrêt : jouable par un vrai touriste.</b></td><td class="num">2</td></tr>
      <tr><td><b>5. Le test</b></td><td>Deux formes nivelées.</td><td class="num">1</td></tr>
      <tr><td><b>6. La semaine jouée</b></td><td>Dix situations en trois paliers, la connaissance qui revient, le bilan en français, les cartes à écrire.</td><td class="num">3</td></tr>
      <tr><td><b>7. La poche</b></td><td>Le mode hors ligne, l'aide-mémoire du total à payer.</td><td class="num">1</td></tr>
      <tr class="f"><td><b>8. Audit et pilote</b></td><td>La boucle didactique (au moins trois tours), puis quelques touristes qui partent pour vrai.</td><td class="num">2</td></tr>
      <tr><td><b>9. L'emballage</b></td><td>La vente par code, le dépliant, la fiche au classeur et à l'onglet Applications.</td><td class="num">1</td></tr>
    </tbody>
  </table>
  <div class="chiffres">
    <div class="ch"><span class="n">18</span><span class="q">séances de travail</span></div>
    <div class="ch"><span class="n">≈&nbsp;250</span><span class="q">images : 200 objets, 10 décors, les gens, les cartes postales ≈ 17&nbsp;$</span></div>
    <div class="ch"><span class="n">≈&nbsp;1&nbsp;200</span><span class="q">extraits de voix anglaises chez Azure, quelques dollars</span></div>
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;¢</span><span class="q">par situation jouée, mesure de Francœur</span></div>
  </div>
  <div class="reserve"><p><strong>Trois limites à dire tout de suite :</strong> l'anglais doit être
  <b>relu par une personne anglophone du Canada</b> avant d'être offert. Les faits de la ville (tarifs du
  métro, heures, prix d'entrée, la façon de payer son passage) se vérifient au cadrage et se datent : ils
  changent. Et les images attendent : <b>le crédit Google est épuisé</b> depuis le 30 septembre ; les
  croquis témoins se feront quand vous l'aurez rechargé.</p></div>
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
  <p>Plan du 1er octobre 2026 · « Une semaine à Toronto ».</p>
  <p>Produit par <code>build/toronto_plan.py</code> — ne pas l'éditer.</p>
</div>

</div>
<script>
(function(){
  var D = [
    {k:'public', q:'Pour qui, d\'abord',
     o:[['quebec','Les Québécois : on arrive en train ou en voiture, sans douane ; les Européens suivent avec une situation de plus à l\'aéroport',true],
        ['europe','Les francophones d\'Europe d\'abord : la douane à Pearson, le pourboire et les taxes comme surprises',false],
        ['tous','Les deux à égalité dès le départ',false]],
     w:"C'est votre public, et le plus nombreux à Toronto. La douane, le pourboire et la taxe ajoutée sont des surprises pour un Européen, pas pour un Québécois : une situation « Arrivée à Pearson » peut s'ajouter sans rien défaire."},
    {k:'niveau', q:'Le niveau visé',
     o:[['faux','Le faux débutant : il a des restes d\'anglais mais fige devant une réponse rapide ; « Avant de partir » pour qui part de zéro',true],
        ['debutant','Le débutant complet, comme Compostelle',false],
        ['inter','Un niveau intermédiaire seulement',false]],
     w:"La plupart des francophones ont appris un peu d'anglais à l'école. Ce qui leur manque, c'est de comprendre la réponse dite vite ; le test règle les paliers, et la préparation reste là pour les autres."},
    {k:'anglais', q:'L\'anglais enseigné',
     o:[['canada','L\'anglais du Canada (washroom, toque, colour) ; les autres façons de dire en note',true],
        ['us','L\'anglais des États-Unis, plus répandu en ligne',false]],
     w:"C'est celui qu'on entend à Toronto ; la différence avec les États-Unis est mince, mais les mots du quotidien (washroom, loonie, two-four) et l'orthographe en font partie."},
    {k:'accents', q:'Les voix',
     o:[['varies','Azure : voix du Canada pour les mots ; au palier 3, les accents de Toronto (Inde, Jamaïque, Chine…), auditionnés au cadrage',true],
        ['canada','Seulement des voix du Canada',false],
        ['autre','Un autre fournisseur',false]],
     w:"Toronto est la ville de toutes les langues ; un touriste y entend l'anglais avec dix accents dès le premier jour. Azure en offre la plupart, contrôlés par retranscription. Il faudra votre feu vert pour les ≈ 1 200 extraits."},
    {k:'fil', q:'Le fil ludique',
     o:[['cartes','Des cartes postales : une par situation réussie, dessinée, qu\'on écrit soi-même en deux lignes d\'anglais',true],
        ['metro','Le plan du métro, coché station par station',false],
        ['aucun','Une liste simple',false]],
     w:"L'équivalent de la credencial de Compostelle, avec un plus : écrire sa carte est une vraie petite production écrite, relue par l'assistance."},
    {k:'connaissance', q:'Une connaissance qui revient',
     o:[['oui','Une même Torontoise, croisée au café, revient chaque jour avec le sujet du jour, et se souvient de la fois d\'avant',true],
        ['divers','Un passant différent chaque jour',false],
        ['non','Pas de bavardage hors des situations',false]],
     w:"Le compagnon de route a été le meilleur moment de Compostelle ; ici, c'est le petit bavardage canadien, qui fait figer bien des touristes."},
    {k:'preparation', q:'La préparation « Avant de partir »',
     o:[['oui','Oui : huit séances de 15 minutes reprises de Compostelle, sautées par qui réussit le test',true],
        ['non','Non : on commence directement par les mots',false]],
     w:"Elle a été demandée pour Compostelle après coup ; ici, on la prévoit dès le plan, mais facultative pour le faux débutant."},
    {k:'decors', q:'Les décors du jeu de rôle',
     o:[['dix','Dix décors dessinés, un par lieu, les gens changent devant',true],
        ['six','Six décors seulement (gare, hôtel, café, comptoir, restaurant, pharmacie)',false],
        ['voix','Sans décor, la voix seule',false]],
     w:"Une ville se reconnaît à ses lieux ; dix scènes à la croquis-sequence coûtent moins d'un dollar. Aucune enseigne ni aucun texte dans l'image, comme toujours."},
    {k:'poche', q:'La poche hors ligne',
     o:[['oui','Oui : les phrases et leurs sons, l\'aide-mémoire du total à payer',true],
        ['non','Non : tout se fait en ligne',false]],
     w:"Le réseau manque dans le métro, et c'est souvent là qu'on prépare sa phrase."},
    {k:'nom', q:'Le nom',
     o:[['semaine','« Une semaine à Toronto »',true],
        ['poche','« Toronto en poche » (trop proche de Montréal en poche, qui est un guide et non une trousse d\'apprentissage)',false],
        ['hello','« Hello Toronto! »',false]],
     w:"Il dit le voyage et sa durée, comme « En route vers Compostelle ». À vérifier au cadrage, sans que ce soit une recherche de marque de commerce."},
    {k:'diffusion', q:'La vente',
     o:[['compostelle','Comme Compostelle : tout gratuit sauf le jeu de rôle, ouvert par un code acheté (même prix, même page de vente)',true],
        ['pilote','Un pilote gratuit d\'abord, le prix ensuite',false],
        ['autre','Une autre formule',false]],
     w:"La vente par code est déjà bâtie et éprouvée (pelerins.py) ; une trousse de plus n'y ajoute qu'une ligne à la liste des produits."}
  ];
  var CLE='plan-toronto', choix={};
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
    var out={plan:'toronto', date:new Date().toISOString().slice(0,10), decisions:{}};
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
    tete = re.sub(r"<title>.*?</title>", "<title>Une semaine à Toronto — le plan</title>", tete)
    tete = tete.replace("</head>", STYLE + "</head>")
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(tete + CORPS.replace("PLAN", plan_metro(), 1), encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
