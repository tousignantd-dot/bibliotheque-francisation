#!/usr/bin/env python3
"""Le plan de la trousse de restauration, sur la formule de la Maison Francœur.

    python3 build/restauration_plan.py   # → assets/presentations/restauration/restauration-plan.html

Demande de Daniel, 30 septembre 2026 : « même chose, vocabulaire, pour des gens
qui vont travailler en restauration ». Même formule que Francœur (on apprend le
français du poste, une langue d'appui dessous), mais un métier à deux postes que
tout sépare — la cuisine et la salle —, d'où la première décision.

Le programme a déjà le côté CLIENT (module-n3-restaurant, niveau 3 : commander,
payer). Comme pour la vente au détail, le côté employé est hors programme.
"""
import pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from plan_trousse import ecrire

SORTIE = RACINE / "assets" / "presentations" / "restauration" / "restauration-plan.html"

CORPS = """
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Formation en milieu de travail &middot; restauration</p>
<h1>La restauration &mdash; le plan</h1>
<p class="chapeau">Pour les gens qui commencent à travailler dans un restaurant sans parler encore
français — souvent à la <b>plonge</b> ou à la <b>préparation</b>, parfois en salle. Même formule que la
Maison Francœur : le français du poste, une langue d'appui dessous, des planches, des exercices, un test,
puis une situation jouée. <strong>Mais un restaurant, c'est deux métiers</strong> que tout sépare : la
cuisine, où l'on reçoit des consignes criées dans le bruit, et la salle, où l'on sert un client. La
première décision est là.</p>

<section class="premier">
  <h2>Ce qui fait rater, au restaurant</h2>
  <table class="cmp"><thead><tr><th>En cuisine</th><th>En salle</th></tr></thead><tbody>
    <tr><td>La <b>consigne du chef</b>, dite vite, de dos, dans le bruit : « deux burgers, un sans fromage, ça presse »</td>
      <td>La <b>commande modifiée</b> : « sans oignons, la sauce à part, bien cuit »</td></tr>
    <tr><td><b>« Chaud derrière ! »</b>, « attention, ça glisse » : les mots qui évitent un accident</td>
      <td>Les nombres : la table douze, deux couverts, l'addition séparée</td></tr>
    <tr><td>Dire <b>qu'il manque</b> quelque chose, avant le rush et pas pendant</td>
      <td>Le client pressé, le client mécontent, et savoir quand appeler le gérant</td></tr>
    <tr><td colspan="2"><b>Les allergies</b>, des deux côtés — l'erreur qui peut tuer. Répondre « il n'y en a pas »
      sans vérifier, ou ne pas transmettre une allergie à la cuisine, est <b>éliminatoire</b>, et la trousse le dit
      avant la première question.</td></tr>
  </tbody></table>
  <p>Même ressort qu'au magasin : ce n'est pas le mot <i>louche</i> qui manque, c'est la phrase dite vite. On
  livre le vocabulaire, et on fait <b>comprendre</b>.</p>
</section>

<section>
  <h2>Volet 1 &mdash; les mots (≈ 170, en onze planches)</h2>
  <table class="cmp"><thead><tr><th>Planche</th><th>Ce qu'on y trouve</th><th>Poste</th></tr></thead><tbody>
    <tr><td>La cuisine</td><td>la ligne, le passe, la plonge, la chambre froide, le congélateur, la réserve, le lave-vaisselle</td><td>cuisine</td></tr>
    <tr><td>Les ustensiles</td><td>couteau du chef, planche à découper, bol à mélanger, fouet, louche, pince, spatule, poêle, chaudron, plaque, bac</td><td>cuisine</td></tr>
    <tr><td>Couper, préparer</td><td>éplucher, trancher, émincer, hacher, en dés, en julienne, mariner, portionner</td><td>cuisine</td></tr>
    <tr><td>Cuire</td><td>bouillir, frire, griller, rôtir, réchauffer ; saignant, à point, bien cuit</td><td>les deux</td></tr>
    <tr><td>Les aliments</td><td>viandes, poissons, légumes, fruits, produits laitiers, pain et pâtes, épices — et les plats d'ici</td><td>les deux</td></tr>
    <tr><td>Les allergènes</td><td>arachides, noix, lait, œufs, blé, poisson, fruits de mer, soya, sésame, moutarde, sulfites</td><td>les deux</td></tr>
    <tr><td>L'hygiène et la sécurité</td><td>se laver les mains, les gants, le filet, le thermomètre, l'étiquette, la date, le désinfectant, « chaud derrière », « ça glisse »</td><td>les deux</td></tr>
    <tr><td>La vaisselle et le couvert</td><td>assiette, bol, verre, tasse, ustensiles, plateau, bac à vaisselle</td><td>les deux</td></tr>
    <tr><td>La salle</td><td>la table, le couvert, le menu, le spécial du jour, l'entrée, le plat, le dessert, pour emporter, l'addition, le pourboire</td><td>salle</td></tr>
    <tr><td>Les nombres et le temps</td><td>les tables, les couverts, les minutes (« dans cinq minutes »), les températures</td><td>les deux</td></tr>
    <tr><td>Le quart de travail</td><td>l'horaire, le quart, la pause, la fermeture, le rush, remplacer quelqu'un</td><td>les deux</td></tr>
  </tbody></table>
  <p><b>Les pièges d'ici</b> sont nombreux au restaurant, et ils trompent aussi les francophones d'ailleurs :
  <i>le déjeuner, le dîner, le souper</i> (le matin, le midi, le soir), <i>l'addition</i> et <i>la facture</i>,
  <i>un breuvage</i>, <i>la liqueur</i> (une boisson gazeuse), <i>les patates</i>, <i>le blé d'Inde</i>, <i>les
  bleuets</i>, <i>la crème glacée</i>, <i>un extra</i> (un supplément).</p>
</section>

<section>
  <h2>Volet 2 &mdash; le décor</h2>
  <p>Comme le comptoir de l'hôtel : <b>un grand dessin fixe, vu de la place de l'employé</b>, dont chaque objet
  se touche, se nomme et s'entend. En cuisine, <b>le poste de travail sur la ligne</b> (la planche, les bacs, la
  plaque, le passe, le chef de dos) ; en salle, <b>la salle vue du comptoir</b>. Le même dessin sert ensuite de
  décor à la situation jouée : le décor ne bouge pas, les personnes changent devant.</p>
</section>

<section>
  <h2>Volets 3 et 4 &mdash; les exercices, le test</h2>
  <p>Les familles de Francœur (j'entends et je trouve · le mot et son image · je me souviens · la série des
  pièges), plus trois qui n'existent qu'ici :</p>
  <ul class="simple">
    <li><b>La consigne du chef</b> — l'exercice-pont : une consigne entière, dite vite, avec le bruit de la
    cuisine dessous ; on choisit ce qu'on fait. Le « ce que le client veut » de Francœur, retourné vers la cuisine.</li>
    <li><b>La commande modifiée</b> — « sans », « avec », « à part », « bien cuit » : ce qui change l'assiette.</li>
    <li><b>L'allergie</b> — une série où la bonne réponse est parfois « je vérifie », jamais « il n'y en a pas » ;
    et un contre-exemple par série, où vérifier n'est pas nécessaire, pour que la règle soit discriminée.</li>
  </ul>
  <p><b>Le test</b> garde le châssis de Francœur : les mots, la consigne entendue, qui décide, parler — deux
  formes parallèles.</p>
</section>

<section>
  <h2>Volet 5 &mdash; les situations jouées</h2>
  <p>En cuisine, <b>l'IA joue le chef</b> ou un collègue ; en salle, <b>le client</b>. Même moteur que le magasin
  (humeur visible, trois paliers, un bilan par geste), un personnage qui parle au lieu d'un client qui achète.</p>
  <table class="cmp"><thead><tr><th>Situation</th><th>Poste</th><th>Le geste qui compte</th></tr></thead><tbody>
    <tr><td>Le premier quart : le chef montre le poste</td><td>cuisine</td><td>faire répéter, redire la consigne</td></tr>
    <tr><td>Le rush : trois consignes d'affilée</td><td>cuisine</td><td>confirmer (« oui, chef : deux burgers, un sans fromage »)</td></tr>
    <tr><td>Il n'y a plus de frites</td><td>cuisine</td><td>le dire au chef, tout de suite, avec la bonne quantité</td></tr>
    <tr><td>Une allergie arrive de la salle</td><td>cuisine</td><td><b>la faire répéter et la confirmer</b> (éliminatoire)</td></tr>
    <tr><td>La chambre froide : dates et rotation</td><td>cuisine</td><td>lire une étiquette, dire ce qui est périmé</td></tr>
    <tr><td>Une commande avec des changements</td><td>salle</td><td>redire la commande avant de l'envoyer</td></tr>
    <tr><td>« Est-ce qu'il y a des noix là-dedans ? »</td><td>salle</td><td><b>« je vérifie en cuisine »</b> — jamais affirmer (éliminatoire)</td></tr>
    <tr><td>Le plat est froid, l'attente est longue</td><td>salle</td><td>s'excuser, agir ou passer le relais au gérant</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le planning</h2>
  <table class="cmp">
    <thead><tr><th>Étape</th><th>Ce qui sort</th><th>Séances</th></tr></thead>
    <tbody>
      <tr class="d"><td><b>0. Cadrage</b></td><td>Vos décisions, les objectifs mesurables, le nom du restaurant fictif (trois candidats vérifiés), le lexique arrêté, trois croquis témoins et le décor.</td><td class="num">1</td></tr>
      <tr><td><b>1. Les planches et le décor</b></td><td>≈ 130 croquis, le décor de la cuisine (et de la salle), les voix, les traductions figées.</td><td class="num">3</td></tr>
      <tr><td><b>2. Les exercices</b></td><td>Sept familles, puis l'audit de la boucle (au moins trois tours). <b>Point d'arrêt : jouable par un vrai commis.</b></td><td class="num">2</td></tr>
      <tr><td><b>3. Le test</b></td><td>Deux formes, puis l'audit.</td><td class="num">1</td></tr>
      <tr><td><b>4. Les situations</b></td><td>Huit situations, le chef et les clients dessinés, le bilan, puis l'audit.</td><td class="num">3</td></tr>
      <tr class="f"><td><b>5. Le pilote</b></td><td>Répété sur un serveur jetable, puis mené dans une vraie cuisine.</td><td class="num">1</td></tr>
      <tr><td><b>6. L'emballage</b></td><td>Fiche de poche (à plastifier : elle vivra près de la plonge), guide du formateur, page acheteur, vente.</td><td class="num">1</td></tr>
    </tbody>
  </table>
  <div class="chiffres">
    <div class="ch"><span class="n">12</span><span class="q">séances de travail</span></div>
    <div class="ch"><span class="n">≈&nbsp;170</span><span class="q">images : ≈ 130 croquis, deux décors, 8 personnages × 4 expressions, à 0,067 $ : ≈ 12 $</span></div>
    <div class="ch"><span class="n">≈&nbsp;650</span><span class="q">extraits de voix chez Azure, dont les consignes « dans le bruit » : quelques dollars, avec votre feu vert</span></div>
    <div class="ch"><span class="n">≈&nbsp;8&nbsp;¢</span><span class="q">par partie jouée, mesuré à Francœur</span></div>
  </div>
  <div class="reserve"><p><strong>Trois limites à dire tout de suite :</strong> la trousse enseigne les
  <b>mots et les gestes</b> de l'hygiène, elle <b>ne remplace pas</b> la formation en hygiène et salubrité que le
  MAPAQ exige de certains employés (exigences exactes à vérifier au cadrage, sans les affirmer d'ici là). La
  liste des allergènes prioritaires est celle de Santé Canada, à revérifier au même moment. Et, comme pour la
  chaussure, <b>une visite en cuisine</b> vaut plus que tout ce que je peux écrire : les consignes réelles d'un
  chef ne s'inventent pas.</p></div>
</section>
"""

DECISIONS = [
    {"k": "poste", "q": "Le poste",
     "o": [["deux-cuisine", "Les deux, une trousse à deux portes ; la cuisine d'abord", True],
           ["cuisine", "La cuisine seulement (plonge, préparation, commis)", False],
           ["salle", "La salle seulement (service, comptoir)", False]],
     "w": "C'est en cuisine qu'on embauche le plus de gens qui ne parlent pas encore français, et c'est là que "
          "rien n'existe. La salle demande plus de français et ressemble au magasin : elle vient ensuite, sur le "
          "même lexique d'aliments, d'allergènes et de nombres."},
    {"k": "type", "q": "Le restaurant fictif",
     "o": [["familial", "Un restaurant familial québécois : déjeuners, poutine, pâté chinois, commandes pour emporter", True],
           ["rapide", "Une restauration rapide, au comptoir", False],
           ["gastronomique", "Une table plus haut de gamme, en brigade", False]],
     "w": "C'est le lieu d'embauche le plus courant, et le seul où les trois repas et les pièges d'ici (déjeuner, "
          "dîner, souper) se rencontrent tous les jours."},
    {"k": "langues", "q": "Les langues",
     "o": [["francoeur", "La formule Francœur : on apprend le français, onze langues d'appui dessous", True],
           ["trois", "Trois langues à égalité, comme l'hôtel", False]],
     "w": "Une cuisine du Québec travaille en français ; c'est lui qu'on apprend. La formule à trois langues de "
          "l'hôtel répond à des clients étrangers, pas à une brigade."},
    {"k": "nom", "q": "Le nom du restaurant",
     "o": [["proposer", "Je vous en propose trois, vérifiés contre les restaurants réels", True],
           ["moi", "Je le donne moi-même", False]],
     "w": "Fictif et nommé, comme la Maison Francœur et l'Hôtel Rive-Claire."},
    {"k": "decor", "q": "Le décor",
     "o": [["dessin", "Un grand dessin fixe du poste de travail, objets à toucher, même trait que les planches", True],
           ["photo", "Une photo de cuisine", False]],
     "w": "Le dessin tient d'une situation à l'autre et se lit sur un téléphone ; une photo générée porterait des "
          "étiquettes et des marques illisibles partout (les cuisines en sont couvertes)."},
    {"k": "allergies", "q": "Les allergies",
     "o": [["eliminatoire", "Éliminatoires, dites avant, dans les exercices, le test et les situations", True],
           ["mention", "Un volet parmi d'autres, sans règle éliminatoire", False]],
     "w": "Une erreur qui peut tuer ne se compte pas en points. C'est la règle du relais de l'hôtel, appliquée à "
          "« je vérifie »."},
    {"k": "bruit", "q": "Le bruit de la cuisine",
     "o": [["oui", "Oui : un fond sonore réglable sous les consignes, qu'on peut couper", True],
           ["non", "Non : des voix nettes seulement", False]],
     "w": "On entend le chef dans le bruit, jamais au calme : c'est la difficulté réelle. Un bouton le coupe pour "
          "les premiers essais."},
    {"k": "visite", "q": "La visite en cuisine",
     "o": [["avant", "Avant l'étape 1 : un service observé, notes à me transmettre", True],
           ["apres", "Après le pilote", False],
           ["sans", "On s'en passe", False]],
     "w": "Les consignes d'un chef, ses abréviations et ses mots d'ordre ne s'inventent pas."},
    {"k": "vente", "q": "La vente",
     "o": [["pareil", "Comme Francœur et l'hôtel : tout gratuit sauf les situations jouées, même prix", True],
           ["autre", "Une autre formule", False]],
     "w": "Une seule grille de prix pour toutes les trousses."},
]


def main():
    s = ecrire(SORTIE, "La restauration — le plan", CORPS, DECISIONS, "plan-restauration", "restauration",
               "<p>Plan du 30 septembre 2026 · chantier « formation en milieu de travail », restauration.</p>"
               "<p>Produit par <code>build/restauration_plan.py</code> — ne pas l'éditer.</p>")
    print(s.relative_to(RACINE))


if __name__ == "__main__":
    main()
