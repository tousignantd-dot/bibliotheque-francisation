#!/usr/bin/env python3
"""Le plan de la trousse Chaussures Rivard, sur la formule de la Maison Francœur.

    python3 build/chaussure_plan.py   # → assets/presentations/chaussure/chaussures-plan.html

Demande de Daniel, 30 septembre 2026 : « on travaille toujours dans la même
formule que la Maison Francœur […] dans le domaine de la chaussure, on avait déjà
commencé des trucs, mais garde la même formule que celui des vêtements. »

Ce qui existait (mémoire chantier-detail-chaussure) : le cadrage du 19 sept.
(le programme enseigne à ACHETER, jamais à vendre), le bloc A en point express
(cinq gestes, 15 voix, fiche de poche), cinq photos. Les chiffres de Francœur
sont relevés sur son contenu, pas estimés.
"""
import importlib.util, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from plan_trousse import ecrire

SORTIE = RACINE / "assets" / "presentations" / "chaussure" / "chaussures-plan.html"


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


FC = RACINE / "build" / "contenu" / "entreprise-francoeur"
LX = _charger("cp_lexique", FC / "lexique.py")
CL = _charger("cp_clients", FC / "clients.py")
PX = _charger("cp_prix", FC / "prix.py")
N_MOTS = len(LX.LEXIQUE)
N_CROQUIS = sum(1 for m in LX.LEXIQUE if m[4] == "croquis")
N_CLIENTS = len(CL.CLIENTS)
PILOTE = PX.FORMULES[0][1]

CORPS = f"""
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Formation en milieu de travail &middot; vente au détail &middot; chaussures</p>
<h1>Chaussures Rivard &mdash; le plan</h1>
<p class="chapeau">La deuxième enseigne du châssis « vendre au détail ». On reprend <strong>la formule
de la Maison Francœur telle quelle</strong> : des employés qui apprennent le français du plancher, une
langue d'appui dessous, des planches de croquis, des exercices, un test, puis un magasin où des clients
joués par l'IA arrivent. Ce qui change, c'est le lexique et les situations, <b>pas la mécanique</b> :
presque tout le code de Francœur se réemploie.</p>

<section class="premier">
  <h2>Ce qui existe déjà, et ce que ça devient</h2>
  <table class="cmp"><thead><tr><th>Pièce</th><th>Ce qu'elle est</th><th>Dans la trousse</th></tr></thead><tbody>
    <tr><td><b>Le cadrage</b> (19 sept.)</td><td>Le constat qui commande : le programme enseigne à <b>acheter</b>, jamais à
      vendre — la trousse est hors programme, et c'est le produit.</td><td>Repris tel quel à l'étape 0.</td></tr>
    <tr><td><b>Le bloc A</b></td><td>Un point express de huit écrans, jouable : les cinq gestes (arrêter, faire préciser,
      redire, tenir la porte ouverte, passer le relais), 15 voix, une fiche de poche.</td><td>Les cinq gestes deviennent
      <b>les gestes du magasin</b>, notés au bilan. Le bloc reste en <b>porte d'entrée</b> (décision 4).</td></tr>
    <tr><td><b>Le nom</b></td><td>« Chaussures Rivard », fictif.</td><td>À revérifier contre les commerces réels à
      l'étape 0, comme les autres noms.</td></tr>
    <tr><td><b>Cinq photos</b></td><td>Magasin, comptoir, essayage, réserve, fiche : le registre photo choisi pour le bloc A.</td>
      <td>Gardées pour le bloc A. Les planches demandent autre chose (décision 1).</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Ce qui change par rapport à la Maison Francœur</h2>
  <table class="cmp"><thead><tr><th></th><th>Maison Francœur</th><th>Chaussures Rivard</th></tr></thead><tbody>
    <tr><td>Les tailles</td><td>P · M · G · TG, et quelques numéros</td><td><b>Les pointures</b> : des nombres dits vite
      (« un huit et demi »), homme et femme, européennes (« un quarante-deux »), et <b>la largeur</b> (étroit, large) — le trait
      qui fait rater une vente</td></tr>
    <tr><td>Le geste physique</td><td>La cabine</td><td><b>Mesurer le pied</b>, chausser, aller en réserve : trois gestes où il
      faut redire avant de partir (le geste du bloc A)</td></tr>
    <tr><td>La saison</td><td>Les couleurs de la saison</td><td><b>L'hiver</b> : doublure, crampons, imperméable, « à
      moins trente » — la question qu'on pose au Québec et nulle part ailleurs</td></tr>
    <tr><td>L'erreur qui coûte</td><td>Promettre un remboursement</td><td>La même, plus une : <b>garantir qu'une botte de travail
      est homologuée</b> sans lire l'étiquette. Une erreur de santé et sécurité, <b>éliminatoire</b></td></tr>
    <tr><td>La paire</td><td>—</td><td>On vend par paire, on essaie un pied : « la paire », « l'autre soulier », « le gauche »</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Volet 1 &mdash; les mots (≈ 130, en neuf planches)</h2>
  <table class="cmp"><thead><tr><th>Planche</th><th>Ce qu'on y trouve</th></tr></thead><tbody>
    <tr><td>Les modèles</td><td>soulier, botte, bottillon, espadrille, sandale, pantoufle, escarpin, mocassin, soulier de course, botte de pluie</td></tr>
    <tr><td>Les parties</td><td>semelle, talon, bout, empeigne, languette, lacet, œillet, doublure, semelle intérieure, fermeture éclair</td></tr>
    <tr><td>Pointures et largeurs</td><td>la pointure (« la grandeur »), la demi-pointure, homme, femme, enfant, étroit, large, européen</td></tr>
    <tr><td>Matières et couleurs</td><td>cuir, suède, toile, caoutchouc, synthétique, verni — les couleurs en pastilles, comme à Francœur</td></tr>
    <tr><td>L'hiver</td><td>botte d'hiver, doublure chaude, crampons, imperméable, couvre-chaussures (« des claques »), la température</td></tr>
    <tr><td>Au travail</td><td>bout d'acier, semelle anti-perforation, antidérapant, le triangle vert, l'étiquette</td></tr>
    <tr><td>L'entretien</td><td>protecteur imperméabilisant, cirage, embauchoir, semelle orthopédique, lacets de rechange, bas</td></tr>
    <tr><td>L'essayage</td><td>banc, mesureur, chausse-pied, miroir, la boîte, la réserve (« en arrière »)</td></tr>
    <tr><td>La caisse</td><td>reçu, échange, remboursement, garantie, carte-cadeau, solde, commande</td></tr>
  </tbody></table>
  <p><b>Les pièges d'ici</b>, marqués comme à Francœur : <i>espadrilles</i> (des chaussures de sport ici, des souliers
  de toile en France), <i>souliers</i>, <i>bas</i>, <i>pantoufles</i>, <i>claques</i>, <i>suède</i> (le daim),
  <i>bottine</i>, et <i>la grandeur</i> qu'on entendra plus souvent que <i>la pointure</i>.</p>
</section>

<section>
  <h2>Volets 2 à 4 &mdash; les exercices, le test, le magasin</h2>
  <p><b>Les exercices</b> de Francœur, réglés sur la chaussure : j'entends et je trouve · le mot et son image ·
  je me souviens · la série des pièges · <b>ce que le client veut</b> (modèle, couleur, pointure <b>et largeur</b>),
  plus une famille neuve : <b>les pointures dites</b> (« un sept et demi en large »), là où l'oreille rate.</p>
  <p><b>Le test</b> garde ses quatre parties (les mots, le client, la gérante, parler), deux formes parallèles,
  et il règle le palier des clients.</p>
  <p><b>Le magasin</b> : {N_CLIENTS} clients, trois paliers, un visage à quatre expressions, un bilan par geste.</p>
  <table class="cmp"><thead><tr><th>Le client</th><th>Le geste qui compte</th></tr></thead><tbody>
    <tr><td>Il a vu un modèle en vitrine, le veut en huit et demi large</td><td>faire préciser la largeur, redire avant d'aller en réserve</td></tr>
    <tr><td>Une mère pressée, un enfant qui grandit</td><td>mesurer, conseiller une demi-pointure de plus</td></tr>
    <tr><td>Il cherche des bottes pour moins trente</td><td>poser la question de l'usage, proposer doublure et crampons</td></tr>
    <tr><td>Il lui faut des bottes de travail homologuées</td><td><b>lire l'étiquette ou passer le relais</b> — jamais affirmer (éliminatoire)</td></tr>
    <tr><td>La semelle a décollé après deux mois</td><td>écouter, ne rien promettre, passer le relais à la gérante</td></tr>
    <tr><td>« Je regarde »</td><td>tenir la porte ouverte sans insister</td></tr>
    <tr><td>Un cadeau, sans connaître la pointure</td><td>proposer la carte-cadeau et expliquer l'échange</td></tr>
    <tr><td>La pointure n'est pas en stock</td><td>proposer une autre largeur ou une commande, sans promettre de date</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le planning</h2>
  <p>Moins de séances que Francœur : l'écran, les exercices, le test, le magasin, le pilote et l'emballage
  existent. On écrit le contenu, on dessine, on règle.</p>
  <table class="cmp">
    <thead><tr><th>Étape</th><th>Ce qui sort</th><th>Séances</th></tr></thead>
    <tbody>
      <tr class="d"><td><b>0. Cadrage</b></td><td>Vos décisions (plus bas), les objectifs mesurables, le nom revérifié, le lexique arrêté, trois croquis témoins et une palette.</td><td class="num">1</td></tr>
      <tr><td><b>1. Les planches</b></td><td>≈ 100 croquis, les voix des mots, les traductions figées, l'écran.</td><td class="num">2</td></tr>
      <tr><td><b>2. Les exercices</b></td><td>Six familles, puis l'audit de la boucle (au moins trois tours). <b>Point d'arrêt : jouable par un vendeur.</b></td><td class="num">2</td></tr>
      <tr><td><b>3. Le test</b></td><td>Deux formes, quatre parties, puis l'audit.</td><td class="num">1</td></tr>
      <tr><td><b>4. Le magasin</b></td><td>{N_CLIENTS} clients, leurs portraits, le bilan par geste, puis l'audit.</td><td class="num">2</td></tr>
      <tr class="f"><td><b>5. Le pilote</b></td><td>Répété sur un serveur jetable, puis mené dans un vrai magasin.</td><td class="num">1</td></tr>
      <tr><td><b>6. L'emballage</b></td><td>Fiche de poche, guide du formateur, page acheteur, vente du jeu de rôle comme Francœur.</td><td class="num">1</td></tr>
    </tbody>
  </table>
  <div class="chiffres">
    <div class="ch"><span class="n">10</span><span class="q">séances de travail (Francœur en a pris 14)</span></div>
    <div class="ch"><span class="n">≈&nbsp;135</span><span class="q">images : ≈ 100 croquis et {N_CLIENTS} clients × 4 expressions, à 0,067 $ : ≈ 9 $</span></div>
    <div class="ch"><span class="n">≈&nbsp;500</span><span class="q">extraits de voix chez Azure : quelques dollars, avec votre feu vert</span></div>
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;¢</span><span class="q">par partie jouée au magasin, mesuré à Francœur</span></div>
  </div>
  <p>Repère : Francœur compte {N_MOTS} mots, dont {N_CROQUIS} dessinés, et {N_CLIENTS} clients. La formule
  « pilote » y est affichée à {PILOTE}.</p>
  <div class="reserve"><p><strong>Ce que je ne peux pas produire :</strong> une demi-journée d'écoute sur un vrai
  plancher de chaussures. Sans elle, j'invente les mots du métier — et les questions des clients sont ce qui
  s'invente le plus mal. Je la demande <b>avant l'étape 1</b> (décision 6).</p></div>
</section>
"""

DECISIONS = [
    {"k": "registre", "q": "Le dessin des planches",
     "o": [["croquis", "Des croquis « à plat » de catalogue, comme Francœur (trait noir, aplat de couleur)", True],
           ["photo", "Des photos, comme le bloc A", False]],
     "w": "Une planche montre un objet par image, toujours de face, à la même échelle : c'est ce que le croquis de "
          "catalogue garantit, et ce qu'une photo générée ne tient pas d'un tirage à l'autre. Les photos du bloc A "
          "restent au bloc A, où elles montrent des scènes."},
    {"k": "langues", "q": "Les langues d'appui",
     "o": [["onze", "Les onze langues de l'outil, figées et marquées « non relues », comme Francœur", True],
           ["trois", "Espagnol et anglais seulement, relus avant la vente", False]],
     "w": "C'est la formule de Francœur. Le prix d'une langue de plus est un fichier ; celui de la relecture vient "
          "quand un magasin la demande."},
    {"k": "palette", "q": "Les couleurs de la trousse",
     "o": [["propre", "Une palette propre, choisie parmi quatre propositions à l'étape 0", True],
           ["denim", "La palette Denim de Francœur", False],
           ["francis", "Le thème francis", False]],
     "w": "Deux enseignes différentes vendues au même réseau doivent se distinguer d'un coup d'œil. La page de "
          "propositions existe déjà pour Francœur ; on la refait."},
    {"k": "blocA", "q": "Le bloc A déjà fait",
     "o": [["entree", "La porte d'entrée : on le joue avant les planches, ses gestes deviennent ceux du magasin", True],
           ["fondre", "Le fondre dans les exercices", False],
           ["retirer", "Le retirer", False]],
     "w": "Il est jouable et vérifié. Il installe les cinq gestes en dix minutes, avant le vocabulaire : c'est "
          "exactement l'ordre « la compréhension d'abord » qu'il défendait."},
    {"k": "travail", "q": "Les chaussures de travail",
     "o": [["oui", "Oui : une planche et un client, avec l'erreur éliminatoire", True],
           ["non", "Non : un magasin grand public seulement", False]],
     "w": "C'est là qu'une phrase de trop coûte le plus cher : un employé qui affirme une homologation qu'il n'a "
          "pas lue. Et c'est un rayon qu'une chaîne a presque toujours."},
    {"k": "plancher", "q": "La visite de plancher",
     "o": [["avant", "Avant l'étape 1 : une demi-journée dans un vrai magasin, notes à me transmettre", True],
           ["apres", "Après le pilote, pour corriger", False],
           ["sans", "On s'en passe", False]],
     "w": "Le compte exact du lexique sort du magasin, pas du fichier. Une page de notes suffit : les questions "
          "entendues, les mots des vendeurs, ce qui revient."},
    {"k": "vente", "q": "La vente",
     "o": [["pareil", "Comme Francœur : tout gratuit sauf le magasin, ouvert par un code acheté, même prix", True],
           ["autre", "Une autre formule", False]],
     "w": "Une seule grille de prix pour toutes les trousses ; il suffit d'ajouter la trousse à la liste blanche "
          "des produits vendus."},
]


def main():
    s = ecrire(SORTIE, "Chaussures Rivard — le plan", CORPS, DECISIONS, "plan-chaussures", "chaussures",
               "<p>Plan du 30 septembre 2026 · chantier « formation en milieu de travail », vente au détail.</p>"
               "<p>Produit par <code>build/chaussure_plan.py</code> — ne pas l'éditer.</p>")
    print(s.relative_to(RACINE))


if __name__ == "__main__":
    main()
