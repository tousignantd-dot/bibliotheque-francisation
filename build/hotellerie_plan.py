#!/usr/bin/env python3
"""Le plan de la trousse d'hôtellerie (réception), trilingue français · anglais · espagnol.

    python3 build/hotellerie_plan.py   # → assets/presentations/hotellerie-plan.html

Demande de Daniel, 24 septembre 2026 : une trousse pour les gens de la
RÉCEPTION d'un hôtel, sous le thème francis, qui se termine à un COMPTOIR
D'ACCUEIL où tout se joue ; et trois langues à égalité — un francophone y
apprend l'anglais ou l'espagnol, un hispanophone le français ou l'anglais, etc.
La page reprend l'en-tête (styles, décisions) du plan de la Maison Francœur.
"""
import pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "hotellerie-plan.html"

CORPS = r"""<body>
<div class="doc">

<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Formation en milieu de travail &middot; hôtellerie &middot; réception</p>
<h1>La réception d'hôtel, en trois langues &mdash; le plan</h1>
<p class="chapeau">Pour les gens qui travaillent au comptoir d'un hôtel. <strong>Trois langues à
égalité</strong> &mdash; français, anglais, espagnol : l'employé choisit la langue qu'il parle et
celle qu'il apprend, et la même trousse sert un francophone qui apprend l'anglais, une hispanophone
qui apprend le français, un anglophone qui apprend l'espagnol. Tout le vocabulaire tourne autour de
la chambre, de la réservation et des vacances. Et tout mène au même endroit : <strong>un comptoir
de réception dessiné</strong>, où l'on apprend les objets du poste, puis où les clients arrivent.</p>

<section class="premier">
  <h2>L'idée, en une ligne</h2>
  <div class="these"><p class="cle"><b>Je parle</b> français · anglais · espagnol &nbsp;→&nbsp;
  <b>J'apprends</b> l'une des deux autres. Six parcours, un seul contenu.</p></div>
  <table class="cmp"><thead><tr><th>Je parle</th><th>J'apprends</th><th>Pour qui, par exemple</th></tr></thead><tbody>
    <tr><td>Français</td><td>Anglais · espagnol</td><td>La réceptionniste de Québec qui reçoit des touristes américains et mexicains</td></tr>
    <tr><td>Espagnol</td><td>Français · anglais</td><td>Un employé arrivé d'Amérique latine, au poste de nuit d'un hôtel de Montréal</td></tr>
    <tr><td>Anglais</td><td>Français · espagnol</td><td>Une employée anglophone d'un hôtel des Laurentides</td></tr>
  </tbody></table>
  <p>L'écran parle la langue de l'employé (consignes, explications, rétroactions) ; tout ce qu'on
  <b>entend</b> et qu'on <b>dit</b> est dans la langue apprise. C'est la règle de francis retournée
  dans les trois sens : la langue d'appui ne remplace jamais la langue apprise, elle l'accompagne dessous.</p>
</section>

<section>
  <h2>Ce qui change par rapport à la Maison Francœur</h2>
  <table class="cmp"><thead><tr><th></th><th>Maison Francœur</th><th>La réception</th></tr></thead><tbody>
    <tr><td>Langues</td><td>On apprend le français ; onze langues d'appui, traduites après coup</td><td>Trois langues <b>écrites et voisées à égalité</b> : chaque mot, chaque phrase existe en trois versions pensées, pas traduites l'une de l'autre</td></tr>
    <tr><td>Voix</td><td>Deux voix québécoises</td><td>Deux voix par langue : français du Québec, anglais nord-américain, espagnol latino-américain</td></tr>
    <tr><td>Pièges</td><td>Faux amis France / Québec</td><td>Faux amis <b>par paire de langues</b> — une « caution » n'est pas « caution », une « location » n'est pas une « location », « constipado » n'est pas « constipé », « embarazada » n'est pas « embarrassed »</td></tr>
    <tr><td>Le lieu</td><td>Un magasin, vu de loin</td><td><b>Le comptoir</b>, vu de derrière, comme le voit le réceptionniste — le décor de l'apprentissage ET du jeu de rôle</td></tr>
    <tr><td>Au serveur</td><td>La correction et le jeu de rôle parlent français</td><td>Ils doivent parler la langue apprise, et rendre le bilan dans la langue de l'employé (voir « Ce qu'il faut bâtir »)</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le parcours de l'employé</h2>
  <ol class="simple">
    <li><b>Deux choix</b> : je parle… / j'apprends… (six combinaisons, une seule page).</li>
    <li><b>Une tâche d'entrée</b> : un client s'approche du comptoir et dit une phrase ; on touche ce qu'il demande (la carte-clé, le reçu, le plan de la ville).</li>
    <li><b>Les mots</b>, en planches de croquis, dans la langue apprise, avec la voix et la traduction dessous.</li>
    <li><b>Le comptoir</b> : chaque objet du poste se touche, se nomme, s'entend.</li>
    <li><b>Les exercices</b>, puis <b>les gestes du réceptionniste</b> (dialogues modèles).</li>
    <li><b>Le test</b> de niveau, dans la langue apprise.</li>
    <li><b>Au comptoir</b> : les clients arrivent — l'IA joue le client dans la langue apprise, le visage réagit, le bilan dit ce qui a été fait.</li>
  </ol>
</section>

<section>
  <h2>Volet 1 &mdash; les mots (≈ 130, en huit planches)</h2>
  <table class="cmp"><thead><tr><th>Planche</th><th>Ce qu'on y trouve</th></tr></thead><tbody>
    <tr><td>L'arrivée</td><td>réservation, confirmation, pièce d'identité, passeport, carte de crédit, carte-clé, formulaire, signature, bagages</td></tr>
    <tr><td>La chambre</td><td>lit simple, double, grand lit, lit d'appoint, vue, étage, ascenseur, climatisation, coffre-fort, minibar, serviettes</td></tr>
    <tr><td>Les services</td><td>petit-déjeuner, stationnement, voiturier, wifi et mot de passe, piscine, salle d'entraînement, navette, appel de réveil, bagagiste</td></tr>
    <tr><td>Le paiement</td><td>tarif, taxes, dépôt, frais, facture, remboursement, annulation, carte refusée</td></tr>
    <tr><td>Les heures et les dates</td><td>arrivée 15 h, départ 11 h, nuitée, les jours, les mois, les nombres de chambre (« la 412 »)</td></tr>
    <tr><td>Les problèmes</td><td>bruit, clé qui ne fonctionne pas, pas d'eau chaude, chambre pas prête, hôtel complet, surréservation</td></tr>
    <tr><td>Les vacances</td><td>plage, excursion, musée, restaurant, location de voiture, plan de la ville, météo</td></tr>
    <tr><td>La politesse</td><td>les formules du comptoir, et le registre : <i>vous</i>, <i>usted</i>, les formes polies de l'anglais</td></tr>
  </tbody></table>
  <p>Même dessin que la Maison Francœur (trait noir, aplat discret), mais des <b>objets et des
  situations</b> plutôt que des vêtements. Les mots sans image (les dates, les formules) se jouent à l'oreille.</p>
</section>

<section>
  <h2>Volet 2 &mdash; le comptoir</h2>
  <p><b>La pièce maîtresse.</b> Un grand dessin du comptoir de réception, vu de derrière : l'écran,
  le terminal de paiement, les cartes-clés et l'encodeur, la sonnette, le présentoir de dépliants,
  le plan de la ville, les horloges, le téléphone, la porte du bureau du gérant. Chaque objet se
  touche : son nom dans la langue apprise, sa voix, sa traduction dessous.</p>
  <p>Le <b>même dessin</b> sert de décor au jeu de rôle : le décor ne bouge pas, les clients
  changent devant. C'est la compétence <code>croquis-sequence</code> (même cadre, mêmes objets, d'un
  plan à l'autre) — ce qu'on a appris à faire avec le simulateur de défibrillateur.</p>
</section>

<section>
  <h2>Volet 3 &mdash; les exercices</h2>
  <p>Les familles qui ont tenu à la Maison Francœur, réglées sur la langue apprise, plus deux qui
  n'existent qu'à la réception :</p>
  <ul class="simple">
    <li><b>Je l'entends, je le trouve</b> · <b>Le mot et son image</b> · <b>Je me souviens</b> · <b>La série des pièges</b> (faux amis de la paire choisie)</li>
    <li><b>Ce que le client veut</b> : le type de chambre, le nombre de nuits, les dates — le « trait qui décide » de Francœur, transposé</li>
    <li><b>Les nombres et les heures</b> — un numéro de chambre, un prix, une heure de départ mal entendus coûtent cher</li>
    <li><b>Épeler un nom</b> — l'alphabet dans la langue apprise, le geste le plus fréquent du comptoir</li>
    <li><b>Ce que je réponds</b> : choisir la réponse du réceptionniste, chaque mauvaise ayant sa rétroaction</li>
  </ul>
</section>

<section>
  <h2>Volet 4 &mdash; le test, puis le comptoir</h2>
  <p><b>Un test par langue apprise</b>, en deux formes parallèles, comme à Francœur : il règle le
  palier des clients. <b>Au comptoir</b>, huit situations :</p>
  <table class="cmp"><thead><tr><th>Situation</th><th>Le geste qui compte</th></tr></thead><tbody>
    <tr><td>Arrivée avec réservation</td><td>accueillir, retrouver la réservation, faire épeler, confirmer les dates</td></tr>
    <tr><td>Arrivée sans réservation</td><td>vérifier la disponibilité, proposer, donner le tarif</td></tr>
    <tr><td>Hôtel complet</td><td>refuser poliment, proposer une solution</td></tr>
    <tr><td>Une plainte (bruit, clé)</td><td>écouter, s'excuser, agir ou passer le relais</td></tr>
    <tr><td>Le départ et la facture</td><td>expliquer un frais, sans promettre un remboursement</td></tr>
    <tr><td>Un renseignement touristique</td><td>indiquer, sur le plan</td></tr>
    <tr><td>Au téléphone</td><td>sans visage : faire répéter, faire épeler, confirmer</td></tr>
    <tr><td>Une demande hors règle</td><td>savoir ce qu'on décide seul, et ce qui revient au gérant</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Ce qu'il faut bâtir, et qui n'existe pas encore</h2>
  <ul class="simple">
    <li><b>Une source trilingue</b> : chaque entrée du lexique porte ses trois langues, ses trois voix, et ses pièges par paire. Le lexique de Francœur n'en portait qu'une.</li>
    <li><b>Le serveur dans la langue apprise</b> : la correction (<code>/api/correct-french</code> ne corrige que le français), le client joué par l'IA et le bilan doivent recevoir la langue apprise et la langue de l'employé.</li>
    <li><b>La reconnaissance vocale</b> dans la langue apprise (fr-CA, en-US, es-MX) — le micro continu de Francœur se reprend tel quel.</li>
    <li><b>Six voix Azure HD</b>, à vérifier au cadrage : le catalogue HD n'offre pas les mêmes timbres dans les trois langues.</li>
  </ul>
</section>

<section>
  <h2>Le planning</h2>
  <table class="cmp">
    <thead><tr><th>Étape</th><th>Ce qui sort</th><th>Séances</th></tr></thead>
    <tbody>
      <tr class="d"><td><b>0. Cadrage</b></td><td>Vos décisions (plus bas), les objectifs mesurables, le lexique arrêté dans les trois langues, les six voix auditionnées, trois croquis d'essai.</td><td class="num">1</td></tr>
      <tr><td><b>1. Les mots</b></td><td>≈ 130 croquis, huit planches, trois langues voisées, l'écran « je parle / j'apprends ».</td><td class="num">3</td></tr>
      <tr><td><b>2. Le comptoir</b></td><td>Le dessin du comptoir, ses objets à toucher ; les visages des clients (quatre expressions).</td><td class="num">2</td></tr>
      <tr><td><b>3. Les exercices</b></td><td>Les sept familles, dans les six directions. <b>Point d'arrêt : jouable par un collègue.</b></td><td class="num">2</td></tr>
      <tr><td><b>4. Le test</b></td><td>Trois banques (une par langue apprise), deux formes chacune.</td><td class="num">2</td></tr>
      <tr><td><b>5. Au comptoir</b></td><td>Huit situations en trois paliers, le serveur trilingue, le bilan par geste.</td><td class="num">3</td></tr>
      <tr class="f"><td><b>6. Audit et pilote</b></td><td>La boucle didactique (deux regards, jusqu'à zéro majeur), puis un petit groupe réel.</td><td class="num">2</td></tr>
      <tr><td><b>7. L'emballage</b></td><td>Fiche de poche trilingue, guide du formateur, démo, fiche au classeur.</td><td class="num">1</td></tr>
    </tbody>
  </table>
  <div class="chiffres">
    <div class="ch"><span class="n">16</span><span class="q">séances de travail</span></div>
    <div class="ch"><span class="n">≈&nbsp;160</span><span class="q">images : 130 objets, le comptoir, 8 clients × 4 expressions ≈ 11&nbsp;$</span></div>
    <div class="ch"><span class="n">≈&nbsp;1&nbsp;300</span><span class="q">extraits de voix (3 langues) chez Azure, quelques dollars</span></div>
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;¢</span><span class="q">par partie jouée au comptoir, mesure de Francœur</span></div>
  </div>
  <div class="reserve"><p><strong>Deux limites à dire tout de suite :</strong> j'écris l'anglais et
  l'espagnol aussi bien que le français, mais une trousse vendue à un hôtel doit être <b>relue par un
  locuteur de chaque langue</b> — comme les traductions de Francœur, marquées « non relues » d'ici là.
  Et six directions, c'est six fois plus de cas à éprouver à l'audit : je propose de construire les
  trois langues dès le départ, mais de piloter d'abord deux directions.</p></div>
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
  <p>Plan du 24 septembre 2026 · chantier « formation en milieu de travail », hôtellerie.</p>
  <p>Produit par <code>build/hotellerie_plan.py</code> — ne pas l'éditer.</p>
</div>

</div>
<script>
(function(){
  var D = [
    {k:'nom', q:"Le nom de l'hôtel fictif",
     o:[['proposer','Je vous en propose trois, vérifiés contre les hôtels réels',true],['moi','Je le donne moi-même',false]],
     w:"Comme la Maison Francœur : fictif, nommé, et qui se dit bien dans les trois langues."},
    {k:'varietes', q:'Les variétés de langue',
     o:[['amerique','Français du Québec, anglais nord-américain, espagnol latino-américain (Mexique)',true],
        ['espagne','Espagnol d\'Espagne',false],['neutre','Des variétés « neutres », sans accent marqué',false]],
     w:"Ce sont les clients qu'un hôtel du Québec reçoit. La variété fixe les voix, les mots (« habitación », « cuarto ») et les pièges."},
    {k:'directions', q:'Les six directions',
     o:[['toutes-pilote-deux','Les trois langues dès le départ ; on pilote d\'abord deux directions',true],
        ['toutes','Les six directions éprouvées ensemble',false],
        ['fr-en','Français ↔ anglais d\'abord, l\'espagnol ensuite',false]],
     w:"Le contenu coûte peu à tripler s'il naît trilingue ; ce qui coûte, c'est l'audit et le pilote de chaque direction."},
    {k:'marque', q:'La marque francis, quand on apprend l\'anglais ou l\'espagnol',
     o:[['suit','Le descripteur suit la langue apprise (« Aide à l\'apprentissage de l\'anglais »)',true],
        ['langues','Un descripteur commun : « Aide à l\'apprentissage des langues »',false],
        ['garde','On garde « du français », plus l\'étiquette « Hôtellerie · Réception »',false]],
     w:"« Aide à l'apprentissage du français » serait faux pour un francophone qui apprend l'espagnol. C'est une décision de marque : elle vous revient."},
    {k:'palette', q:'Les couleurs',
     o:[['francis','Le thème francis, tel quel (comme vous l\'avez demandé)',true],
        ['propre','Une palette propre à l\'hôtellerie, comme Denim pour Francœur',false]],
     w:"Vous avez dit « sous le thème francis ». L'étiquette de secteur, à droite de la marque, suffit à distinguer la trousse."},
    {k:'comptoir', q:'Le comptoir',
     o:[['dessin','Un grand dessin fixe, objets à toucher, même trait que les planches',true],
        ['photo','Une image photoréaliste',false],['3d','Une scène en 3D qu\'on fait tourner',false]],
     w:"Le dessin tient d'un plan à l'autre (croquis-sequence) et se lit sur un téléphone. La 3D coûte cher et se manipule mal au doigt."},
    {k:'telephone', q:'Les appels téléphoniques',
     o:[['oui','Oui : une situation sans visage, la plus dure à l\'oreille',true],['non','Non, seulement le comptoir',false]],
     w:"Au comptoir, la moitié des demandes arrivent au téléphone, et c'est là qu'on fait épeler."},
    {k:'voix', q:'Les voix',
     o:[['azure','Azure HD : deux voix par langue, auditionnées au cadrage',true],['autre','Un autre fournisseur',false]],
     w:"La même chaîne que Francœur (vérification par retranscription comprise) ; il faut votre feu vert pour les ≈ 1 300 extraits."}
  ];
  var CLE='plan-hotellerie', choix={};
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
    var out={plan:'hotellerie', date:new Date().toISOString().slice(0,10), decisions:{}};
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
    tete = re.sub(r"<title>.*?</title>", "<title>La réception d'hôtel — le plan</title>", tete)
    # L'en-tête de Francœur pose table{min-width:640px} : à 375 px, les tableaux
    # débordaient de la page. Ils défilent maintenant dans leur propre cadre.
    tete = tete.replace("</head>", "<style>table.cmp{display:block;max-width:100%;min-width:0;"
                        "overflow-x:auto}@media (max-width:640px){table.cmp{font-size:14px}"
                        "table.cmp th,table.cmp td{padding:10px}table.cmp td{min-width:9em}}"
                        "</style>\n</head>")
    SORTIE.write_text(tete + CORPS, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
