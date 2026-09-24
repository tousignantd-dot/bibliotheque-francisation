#!/usr/bin/env python3
"""Le protocole du pilote de la Maison Francœur (étape 5).

    python3 build/francoeur_pilote.py   # → assets/presentations/francoeur-pilote.html

Produite, jamais éditée : les chiffres (items, clients, voix douteuses) sont
lus dans le contenu et dans le relevé d'écoute, pour que la page ne mente pas
le jour où l'un d'eux change.

LE PILOTE EST UN DIAGNOSTIC DIDACTIQUE, pas une évaluation : on évalue le
MATÉRIEL par les réponses des employés. Un item raté par la moitié du groupe
accuse l'item. Ce qui remonte à l'employeur est un constat sur le matériel,
jamais sur une personne.
"""
import json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
from lexique import LEXIQUE  # noqa: E402
from demandes import DEMANDES  # noqa: E402
import test as TEST  # noqa: E402
from clients import CLIENTS, GESTES  # noqa: E402
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import francoeur_denim as DENIM  # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "francoeur-pilote.html"


def main():
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "francoeur-planches" in (a.get("interactive") or ""))
    ecoute = CONTENU / "ecoute.json"
    douteux = sum(r["douteux"] for r in json.loads(ecoute.read_text(encoding="utf-8"))) if ecoute.exists() else "?"
    n_test = sum(len(v) for v in (TEST.A_CRAN1, TEST.A_CRAN2, TEST.A_CRAN3)) + len(TEST.B) + len(TEST.C)
    trad = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    langues_sans_ui = [c for c, v in trad.items() if "magasin" not in v.get("interface", {})]

    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Maison Francœur — le pilote</title>", tete)
    tete = tete.replace("</style>", CSS + DENIM.CSS + "</style>", 1)
    gestes = "".join(f"<li>{g['nom']} — « {g['phrase']} »</li>" for g in GESTES)
    clients = " · ".join(c[1] for c in CLIENTS)

    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; étape 5</p>
<h1>Le pilote</h1>
<p class="chapeau">Faire jouer la trousse par quatre à huit employés du public visé, et lire <strong>ce que le
matériel fait rater</strong>. Ce n'est pas une évaluation des personnes : c'est un diagnostic didactique. Un item
raté par la moitié du groupe accuse l'item ; un item réussi par tous occupe une place que rien n'occupe.</p>

<section class="premier">
  <h2>Avant le pilote</h2>
  <ol class="actions">
    <li><p><b>Écouter les {douteux} voix douteuses</b> sur la <a href="francoeur-ecoute.html">page d'écoute</a>
      — retranscrites par Azure, elles s'écartent du texte attendu. La plupart sont des homophones sur un mot
      seul ; certaines méritent l'oreille.</p><p class="qui">Vous. Dix minutes.</p></li>
    <li><p><b>Essayer le magasin en ligne</b>, avec un code d'élève : le client annonce-t-il son humeur entre
      crochets sans qu'ils s'affichent ? Parle-t-il en phrases courtes au palier débutant ? Dit-il « FIN » ?
      Ce n'a été joué que contre un serveur simulé.</p><p class="qui">Vous. Vingt minutes, deux clients.</p></li>
    <li><p><b>Faire relire les langues du groupe</b> par un locuteur — chaque traduction est marquée « non relue »
      à l'écran tant que personne ne l'a validée.</p><p class="qui">Un employé bilingue, idéalement du pilote.</p></li>
  </ol>
</section>

<section>
  <h2>Qui, combien, quand</h2>
  <table class="cmp"><tbody>
    <tr><td><b>Employés</b></td><td>Quatre à huit, du public visé : ne parlent pas encore français, ou peu (niveaux 1 à 3).
      Des langues maternelles différentes si possible — c'est ce qui éprouve la langue d'appui.</td></tr>
    <tr><td><b>Encadrement</b></td><td>Un formateur, qui mène, et un observateur, qui ne parle pas et note.</td></tr>
    <tr><td><b>Matériel</b></td><td>Leurs téléphones, des écouteurs, la feuille QR de la séance, la grille d'observation
      (plus bas, imprimable).</td></tr>
    <tr><td><b>Durée</b></td><td>Deux séances de 90 minutes, à une semaine d'écart — le test se repasse à la fin.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Mise en place, dans le portail</h2>
  <ol class="actions">
    <li><p>Créer un <b>groupe pilote de niveau 3</b> — la trousse est inscrite au catalogue comme atelier de ce
      niveau (activité {act["id"]}), et le niveau du groupe borne ce qu'il voit.</p></li>
    <li><p>Ouvrir une <b>séance sans compte</b> sur « {act["title"]} » : aucun nom, un code et un carré QR
      imprimés. Chaque réponse fermée remonte au <b>direct de la classe</b> (progression.html), question par
      question — ni les phrases libres du magasin, ni l'oral, ni la langue choisie.</p></li>
    <li><p>Le magasin demande un code : en séance, il le reçoit du portail. Hors séance, un code d'élève.</p></li>
  </ol>
</section>

<section>
  <h2>Le déroulé</h2>
  <table class="cmp"><thead><tr><th>Séance 1</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>Accueil, choix de la langue</td><td class="num">10</td><td>Trouvent-ils seuls leur langue, ou « sans traduction » ?</td></tr>
    <tr><td>Le test « Mon niveau »</td><td class="num">15</td><td>{n_test} items possibles, adaptatif. Qui abandonne, où.</td></tr>
    <tr><td>Les planches</td><td class="num">20</td><td>Touchent-ils « Voir dans ma langue » à chaque mot, ou jamais ?</td></tr>
    <tr><td>Les exercices (sept, dont les pièges)</td><td class="num">40</td><td>Quel exercice ils refont d'eux-mêmes ; lequel ils fuient.</td></tr>
    <tr><td>Retour à chaud</td><td class="num">5</td><td>Deux questions, plus bas.</td></tr>
  </tbody></table>
  <table class="cmp" style="margin-top:14px"><thead><tr><th>Séance 2</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>Exercices, dont « Ce que le client veut »</td><td class="num">20</td><td>{len(DEMANDES)} demandes : lesquelles ratées par tous.</td></tr>
    <tr><td>Les gestes du vendeur, puis le magasin</td><td class="num">40</td><td>Les dialogues modèles, « Ce que je réponds », puis {len(CLIENTS)} clients — {clients}. Qui arrive à faire repartir le client content.</td></tr>
    <tr><td>Le test, repassé (seconde forme)</td><td class="num">15</td><td>L'écart avec la première passation, sur des questions nouvelles.</td></tr>
    <tr><td>Entretien de groupe</td><td class="num">15</td><td>Les cinq questions, plus bas.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Les règles de décision</h2>
  <div class="these"><p class="cle">On lit le direct de la classe item par item, et on décide sur le matériel.</p></div>
  <table class="cmp"><thead><tr><th>Ce qu'on voit</th><th>Ce qu'on en conclut</th><th>Ce qu'on fait</th></tr></thead><tbody>
    <tr><td>Un item <b>raté au premier essai par la moitié</b> du groupe ou plus</td><td>L'item est en cause : image ambiguë, voix mal dite, distracteur trop proche</td><td>On le réécoute, on le regarde, on le refait</td></tr>
    <tr><td>Un item <b>réussi par tous</b> au premier essai</td><td>Il n'apprend rien à ce groupe</td><td>On le garde au cran 1, ou on le retire</td></tr>
    <tr><td>Un cran du test que <b>personne ne franchit</b></td><td>Le cran est trop haut, ou mal construit</td><td>On relit ses items avant de toucher à la règle</td></tr>
    <tr><td>Un client que <b>personne ne fait repartir content</b></td><td>Le client est trop dur pour son palier</td><td>On le remonte d'un palier, ou on adoucit ses faits</td></tr>
    <tr><td>Le bouton de traduction <b>jamais touché</b>, ou <b>à chaque mot</b></td><td>La langue d'appui ne joue pas son rôle</td><td>On revoit sa place et sa promesse</td></tr>
  </tbody></table>
  <div class="reserve"><p><strong>Trois limites, à dire soi-même :</strong> huit personnes <b>révèlent</b>, elles ne prouvent pas ;
  un groupe qui se sait observé ne joue pas comme seul ; et <b>ce qui remonte à l'employeur est un constat sur le
  matériel, jamais sur une personne</b> — pseudonymes, séance sans compte, aucun nom dans les traces.</p></div>
</section>

<section>
  <h2>Les questions</h2>
  <p><b>À chaud, fin de la séance 1</b> — deux questions, dans leur langue si besoin :</p>
  <ol class="simple"><li>Qu'est-ce qui était difficile ?</li><li>Qu'est-ce que vous voulez refaire ?</li></ol>
  <p><b>Entretien, fin de la séance 2</b> :</p>
  <ol class="simple">
    <li>Au magasin, quel client était le plus dur ? Pourquoi ?</li>
    <li>Avez-vous utilisé la traduction ? Quand ?</li>
    <li>Un mot que vous avez appris ici et que vous avez entendu au travail ?</li>
    <li>Qu'est-ce qui manque pour votre travail à vous ?</li>
    <li>Le recommanderiez-vous à un collègue ? Que lui diriez-vous ?</li>
  </ol>
  <p><b>Les cinq gestes du vendeur</b>, à observer au magasin :</p>
  <ol class="simple">{gestes}</ol>
</section>

<section class="grille-obs">
  <h2>Grille d'observation <small>— à imprimer, une par séance</small></h2>
  <table class="cmp obs"><thead><tr><th>Pseudonyme</th><th>Langue</th><th>Où ça bloque</th><th>Traduction</th><th>Geste observé</th><th>Citation</th></tr></thead>
  <tbody>{"".join("<tr><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(8))}</tbody></table>
  <p><button type="button" class="btn-export" onclick="window.print()">Imprimer la grille</button></p>
</section>

<div class="pied"><p>Protocole produit par <code>build/francoeur_pilote.py</code> — ne pas l'éditer.
Plan : <a href="magasin-vetements-plan.html">magasin-vetements-plan.html</a>.</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — activité {act['id']}, {douteux} voix douteuses")


CSS = """
.obs td{height:44px}
.obs th,.obs td{border:1px solid var(--line-fort)}
.btn-export{font:inherit;font-weight:700;cursor:pointer;background:var(--acier);color:#fff;border:0;border-radius:10px;padding:10px 16px}
@media print{
  body *{visibility:hidden}
  .grille-obs,.grille-obs *{visibility:visible}
  .grille-obs{position:absolute;inset:0;padding:0 12px}
  .grille-obs button{display:none}
  .obs td{height:70px}
}
"""

if __name__ == "__main__":
    main()
