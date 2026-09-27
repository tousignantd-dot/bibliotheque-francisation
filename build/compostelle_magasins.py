#!/usr/bin/env python3
"""« En faire une application à télécharger ? » — la comparaison, pour Compostelle.

    python3 build/compostelle_magasins.py   # → assets/presentations/compostelle-magasins.html

Question de Daniel, 26 sept. 2026 : est-il pensable d'en faire une app à
télécharger, avec les côtés positifs et négatifs. La réponse générale pour les
élèves de francisation existe déjà (application-ou-navigateur.html, 31 août) ;
celle-ci est propre à Compostelle : un public grand public, hors de toute
classe, qui marche sans réseau. Le poids des médias est mesuré sur le disque au
moment du build ; les tarifs des magasins sont ceux connus au 26 sept. 2026 et
se revérifient le jour d'une décision.
"""
import html, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-magasins.html"
MEDIA = RACINE / "assets" / "interactive" / "compostelle"
PAGE = RACINE / "modules-autonomes" / "compostelle" / "index.html"
E = html.escape


def poids():
    """(nombre de fichiers, octets) des médias servis : sons, croquis, vignettes, portraits."""
    n = o = 0
    for d, ext in (("sons", ".mp3"), ("croquis", ".jpg"), ("etapes", ".jpg"), ("portraits", ".jpg")):
        for f in (MEDIA / d).rglob("*" + ext):
            if ".orig" not in f.name:
                n += 1; o += f.stat().st_size
    return n, o + PAGE.stat().st_size


def main():
    n, octets = poids()
    mo = f"{octets / 1048576:.0f}".replace(".", ",")
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — app ou site</title>", tete)
    tete = tete.replace("</head>", """<style>
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
.deux{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.col{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px}
.col h3{margin:0 0 8px;font-size:17px}
.col.pour h3{color:var(--fait)}.col.contre h3{color:var(--loi)}
.col ul{margin:0;padding-left:18px}.col li{margin:7px 0;font-size:15px;line-height:1.45}
.reco{background:var(--fait-bg);border:1px solid var(--fait);border-radius:12px;padding:14px 16px}
.reco ol{margin:6px 0 0;padding-left:20px}.reco li{margin:6px 0}
.garde{background:var(--decid-bg);border:1px solid var(--decid);border-radius:12px;padding:12px 16px;font-size:15px}
.voie-reco{font-weight:900;color:var(--fait)}
@media (max-width:760px){.deux{grid-template-columns:1fr}}
</style>
</head>""")
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; en faire une app à télécharger ?</h1>
<p class="chapeau">C'est faisable, mais c'est un autre métier que celui d'aujourd'hui. Et c'est déjà presque une application :
elle s'installe sur l'écran d'accueil, avec son icône et en plein écran, et une fois « préparée pour le chemin », elle marche
sans réseau. La vraie question est donc : <strong>que gagnerait-on à passer par l'App Store et Google Play, et à quel prix ?</strong></p>

<section class="premier">
  <h2>Où on en est</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">0 $</span><span class="q">par an : le site installable ne coûte rien de plus</span></div>
    <div class="ch"><span class="n">{mo} Mo</span><span class="q">tout compris : {n} sons et images, plus la page (mesuré)</span></div>
    <div class="ch"><span class="n"><span class="n">5 min</span><span class="q">entre une correction et sa mise en ligne</span>lt; 10 min</span><span class="q">entre une correction et sa mise en ligne</span></div>
  </div>
  <p>Ce qui manque au site, et à lui seul : <b>être trouvé</b> dans un magasin, <b>s'installer sans explication</b>, et, sur
  iPhone, <b>garder les tampons à coup sûr</b> (voir plus bas).</p>
</section>

<section>
  <h2>Trois voies, pas deux</h2>
  <p>Le mot « application » cache trois choses de coûts très différents.</p>
  <table class="cmp"><thead><tr><th></th><th>1. Le site installable <span class="voie-reco">(aujourd'hui)</span></th>
    <th>2. Une coquille dans les magasins</th><th>3. Une réécriture pour chaque téléphone</th></tr></thead><tbody>
    <tr><td>Ce que c'est</td><td>La page actuelle, ajoutée à l'écran d'accueil</td><td>La même application, emballée pour l'App Store et Google Play</td><td>Deux applications écrites de zéro, iPhone et Android</td></tr>
    <tr><td>Travail</td><td>Fait</td><td>Quelques semaines au départ, puis un peu d'entretien chaque année</td><td>Des mois, et deux programmes à tenir</td></tr>
    <tr><td>Coût fixe</td><td>0 $</td><td>99 $ US par an (Apple) + 25 $ US une fois (Google)</td><td>Idem, plus le développement</td></tr>
    <tr><td>Mises à jour</td><td>En ligne en quelques minutes</td><td>Le contenu peut rester chargé du site ; le programme passe par l'examen des magasins</td><td>Tout passe par l'examen</td></tr>
    <tr><td>On la trouve…</td><td>si on reçoit l'adresse</td><td>en cherchant dans le magasin</td><td>en cherchant dans le magasin</td></tr>
    <tr><td>Le générateur</td><td>Intact</td><td>Intact : la coquille affiche ce qu'il produit</td><td><b>Jeté</b> — or c'est lui qui a produit les 10 étapes, les sons, les dessins</td></tr>
  </tbody></table>
  <p style="margin-top:10px">La voie 3 est à écarter : elle jetterait ce qui fait la valeur du projet. Le vrai choix est entre 1 et 2.</p>
</section>

<section>
  <h2>La coquille dans les magasins : le pour et le contre</h2>
  <div class="deux">
    <div class="col pour"><h3>Ce qu'elle apporterait</h3><ul>
      <li><b>On la trouve.</b> Un pèlerin qui cherche « Camino espagnol » tombe dessus ; aujourd'hui, il faut qu'on lui donne l'adresse.</li>
      <li><b>La confiance.</b> Pour le grand public, une app dans un magasin est un produit ; un lien, beaucoup moins.</li>
      <li><b>L'installation va de soi.</b> « Ajouter à l'écran d'accueil » est caché dans les menus (sur iPhone : Partager, puis
        « Sur l'écran d'accueil ») ; beaucoup ne le trouvent jamais.</li>
      <li><b>Les tampons ne se perdent pas.</b> Voir « Le cas de l'iPhone », ci-dessous.</li>
      <li><b>Tout est dans le téléphone dès l'installation</b> : les {mo} Mo de sons et d'images, sans le geste « Préparer pour le chemin ».</li>
      <li><b>Un moyen de paiement</b> tout fait, si l'outil se vend un jour.</li>
    </ul></div>
    <div class="col contre"><h3>Ce qu'elle coûterait</h3><ul>
      <li><b>De l'argent, chaque année</b> : 99 $ US par an chez Apple ; 25 $ US une fois chez Google.</li>
      <li><b>Du travail</b> : quelques semaines au départ, puis de l'entretien — chaque nouvelle version d'iOS ou d'Android peut demander une retouche.</li>
      <li><b>Plus de correction instantanée.</b> Chaque nouvelle version du programme passe par l'examen (souvent un à deux jours chez Apple).
        Une coquille qui charge son contenu depuis le site garde en bonne partie la mise à jour immédiate.</li>
      <li><b>Un refus possible chez Apple.</b> Apple refuse les apps qui ne sont « qu'un site emballé ». La nôtre a de quoi passer
        (hors ligne, audio, micro, credencial), mais rien n'est garanti.</li>
      <li><b>La commission, si on vend.</b> Un contenu numérique payant doit passer par le paiement du magasin : 15 % (petite entreprise) à 30 % du prix.</li>
      <li><b>Des formalités</b> : politique de confidentialité, fiche du magasin, captures d'écran, déclarations sur les données, et un
        compte de développeur au nom de la maison plutôt qu'au vôtre.</li>
    </ul></div>
  </div>
</section>

<section>
  <h2>Le cas de l'iPhone</h2>
  <p>Safari efface ce qu'un site a gardé dans le téléphone s'il n'a pas été visité depuis <b>sept jours d'utilisation de Safari</b>.
  Pour Compostelle, ce sont les tampons, les réglages et l'allergie choisie. Un pèlerin qui prépare son chemin en janvier et le
  reprend en mars peut retrouver une credencial vide.</p>
  <p><b>Une page ajoutée à l'écran d'accueil n'est pas touchée par cette règle</b>, ni une app des magasins. D'où l'importance,
  dès le pilote, de montrer le geste d'installation, et de le rappeler dans le mode d'emploi (c'est fait : « Comment ça marche ? »).</p>
</section>

<section>
  <h2>Recommandation</h2>
  <div class="reco"><ol>
    <li><b>Maintenant</b> : garder le site installable, qui ne coûte rien. Faire le pilote avec les cinq pèlerins, et leur
      <b>montrer en personne</b> comment l'ajouter à l'écran d'accueil.</li>
    <li><b>Si le pilote montre que ça vaut la peine de le vendre au grand public</b> : emballer la même application dans une coquille
      pour les deux magasins — quelques semaines, sans rien réécrire, puisque tout le contenu sort déjà d'un générateur.</li>
    <li><b>À éviter</b> : la réécriture pour chaque téléphone.</li>
  </ol></div>
  <h3 style="margin-top:18px">Ce qui ferait rouvrir la question</h3>
  <ul class="simple">
    <li>la décision de <b>vendre</b> l'outil au grand public (le magasin devient alors le comptoir) ;</li>
    <li>au pilote, des pèlerins qui <b>n'arrivent pas à l'installer</b>, ou qui <b>perdent leurs tampons</b> ;</li>
    <li>un partenaire (agence de voyage, association jacquaire) qui veut <b>la distribuer sous son nom</b>.</li>
  </ul>
  <div class="garde" style="margin-top:14px"><b>À revérifier le jour d'une décision.</b> Les tarifs et les règles de paiement des
  deux magasins changent, et diffèrent selon les pays (au Canada, aux États-Unis, en Europe). Les chiffres de cette page sont ceux
  connus au 26 septembre 2026. La réponse générale, pour les élèves de francisation, est sur
  <a href="application-ou-navigateur.html">« Application ou navigateur ? »</a>.</div>
</section>
</div>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {n} fichiers, {mo} Mo")


if __name__ == "__main__":
    main()
