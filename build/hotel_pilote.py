#!/usr/bin/env python3
"""Le protocole du pilote de l'Hôtel Rive-Claire (étape 5).

    python3 build/hotel_pilote.py   # → assets/presentations/hotellerie-pilote.html

Produite, jamais éditée. Les chiffres (mots, items, clients, gestes, ce qui
reste à trancher) sont LUS dans le contenu, pour que la page ne mente pas le
jour où l'un d'eux change. Modèle : build/francoeur_pilote.py.

LE PILOTE EST UN DIAGNOSTIC DIDACTIQUE, pas une évaluation : on évalue le
MATÉRIEL par les réponses des employés. Un item raté au premier essai par la
moitié du groupe accuse l'item. Ce qui remonte à l'employeur est un constat sur
le matériel, jamais sur une personne.

CE QUI CHANGE PAR RAPPORT À FRANCŒUR : trois langues à égalité, donc DEUX
petits groupes pour les deux directions du pilote (décision du 24 sept. :
fr→en et es→fr), qui ne se comparent pas entre eux ; et un comptoir dont le
bilan est rendu par un modèle — le formateur le contredit quand il le faut, et
ce désaccord est une donnée du pilote.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
SORTIE = RACINE / "assets" / "presentations" / "hotellerie-pilote.html"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def main():
    LX = _charger("hp_lexique", CONTENU / "lexique.py")
    EX = _charger("hp_exercices", CONTENU / "exercices.py")
    TS = _charger("hp_test", CONTENU / "test.py")
    CL = _charger("hp_clients", CONTENU / "clients.py")
    HA_src = (RACINE / "build" / "hotel_audio.py").read_text(encoding="utf-8")
    lettres_faites = not re.search(r"^CHOIX_LETTRES = \{\}", HA_src, re.M)
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "hotel-reception" in (a.get("interactive") or ""))
    n_test = len(TS.A[1]) + len(TS.B[1]) + len(TS.C[1]) + len(TS.D[1])
    pieges = {p: sum(1 for m in LX.LEXIQUE if m[6].startswith(f"PIÈGE ({p})")) for p in ("fr·en", "fr·es")}
    nom_c = lambda c: f"{CL.TITRE[c[1]]['fr']} {c[2]}"
    clients = " · ".join(nom_c(c) + (" (téléphone)" if c[4] == "telephone" else "") for c in CL.CLIENTS)
    gestes = "".join(f"<li>{'★ ' if any(g['id'] in CL.CLES[c[0]] for c in CL.CLIENTS) else ''}"
                     f"{E(g['nom']['fr'])} — « {E(g['phrase']['fr'])} »</li>" for g in CL.GESTES)
    cles = "".join(f"<tr><td>{E(nom_c(c))}</td><td>{E(c[6]['fr'])}</td><td>"
                   f"{E(', '.join(next(g['nom']['fr'] for g in CL.GESTES if g['id'] == k) for k in CL.CLES[c[0]]))}</td></tr>"
                   for c in CL.CLIENTS)

    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Hôtel Rive-Claire — le pilote</title>", tete)
    RIVE = _charger("hp_rive", RACINE / "build" / "hotel_rive.py")
    tete = tete.replace("</style>", CSS + RIVE.CSS + "</style>", 1)

    avant = [
        ("Trancher les lettres épelées" if not lettres_faites else "Lettres épelées : tranché",
         ("Sur la <a href=\"hotel-lettres.html\">page des lettres</a>, choisir la prise de chaque lettre qui sonne "
          "mal, puis exporter : les noms épelés des exercices et du test se réassemblent à partir de ce choix. "
          "C'est le seul média de la trousse qui attend encore votre oreille." if not lettres_faites else
          "Les prises choisies sont posées ; les noms épelés ont été réassemblés."),
         "Vous. Quinze minutes."),
        ("Jouer deux clients en ligne",
         "Avec un code d'élève, sur le vrai serveur : un client au comptoir, un au téléphone, dans la direction "
         "de chaque groupe. Le comptoir a été joué par l'audit sur un serveur local jetable, jamais en production.",
         "Vous. Vingt minutes."),
        ("Faire relire l'anglais et l'espagnol",
         "Par un locuteur de chaque langue : les mots, les phrases des exercices, les répliques-modèles. Les "
         "variétés sont celles décidées au cadrage (Amérique du Nord, Mexique) ; le français d'ici a été écrit "
         "d'ici. L'audit didactique ne vérifie pas la justesse de la langue.",
         "Un employé bilingue par langue, idéalement du pilote."),
        ("Créer les deux groupes et imprimer",
         f"Deux groupes pilotes de niveau {E(act['level'].split()[-1])} (la trousse est l'atelier {act['id']}), "
         "une séance sans compte par groupe, la feuille QR, et la grille d'observation plus bas, une par séance.",
         "Le formateur."),
    ]
    avant_html = "".join(f"<li><p><b>{E(t)}</b> — {d}</p><p class=\"qui\">{E(q)}</p></li>" for t, d, q in avant)

    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; étape 5</p>
<h1>Le pilote</h1>
<p class="chapeau">Faire jouer la trousse par de vrais employés de réception, et lire <strong>ce que le matériel fait
rater</strong>. Ce n'est pas une évaluation des personnes : c'est un diagnostic didactique. Un item raté au premier
essai par la moitié du groupe accuse l'item ; une situation que personne ne réussit accuse la situation.</p>

<section class="premier">
  <h2>Avant le pilote</h2>
  <ol class="actions">{avant_html}</ol>
</section>

<section>
  <h2>Deux groupes, deux directions</h2>
  <table class="cmp"><thead><tr><th></th><th>Groupe A · fr → en</th><th>Groupe B · es → fr</th></tr></thead><tbody>
    <tr><td><b>Qui</b></td><td>Réceptionnistes francophones qui reçoivent des clients anglophones</td>
      <td>Réceptionnistes hispanophones qui apprennent le français d'ici</td></tr>
    <tr><td><b>Combien</b></td><td>Trois à six</td><td>Trois à six</td></tr>
    <tr><td><b>L'écran</b></td><td>En français, contenu en anglais</td><td>En espagnol, contenu en français</td></tr>
    <tr><td><b>Pièges de la paire</b></td><td class="num">{pieges['fr·en']}</td><td class="num">{pieges['fr·es']}</td></tr>
  </tbody></table>
  <p>Les deux groupes <b>ne se comparent pas</b> : la langue, les pièges et les voix diffèrent. Chacun sert à
  juger sa direction. Encadrement : un formateur qui mène, un observateur qui ne parle pas et note. Matériel :
  leurs téléphones, des écouteurs (l'écoute est au cœur de tout), la feuille QR. Durée : <b>deux séances de
  90 minutes à une semaine d'écart</b> — le test se repasse à la fin, dans sa seconde forme.</p>
</section>

<section>
  <h2>Mise en place, dans le portail</h2>
  <ol class="actions">
    <li><p>Créer le groupe, puis ouvrir une <b>séance sans compte</b> sur « {E(act['title'])} » (atelier {act['id']}) :
      aucun nom, un code et un carré QR imprimés. Chaque réponse fermée remonte au <b>direct de la classe</b>
      (progression.html), au premier essai, question par question, et chaque situation du comptoir avec ses gestes.
      Ne remontent jamais : les phrases dites au comptoir, l'oral du test, la langue de l'employé.</p></li>
    <li><p>Le comptoir et ses voix passent par le serveur : <b>en séance, ils reçoivent le code de la séance</b>.
      Si le centre a refusé le mode avec assistance, le comptoir ne s'ouvre pas — le vérifier avant.</p></li>
    <li><p>Chaque employé choisit sa langue et la langue apprise au premier écran. Le test garde son historique
      <b>sur l'appareil</b> : un téléphone par personne, jamais une tablette partagée.</p></li>
  </ol>
</section>

<section>
  <h2>Le déroulé</h2>
  <table class="cmp"><thead><tr><th>Séance 1</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>Langues, puis le test (première forme)</td><td class="num">20</td><td>{n_test} items, adaptatif en A ; le code du formateur ouvre la passation, le formateur note l'oral et confirme le niveau.</td></tr>
    <tr><td>Le comptoir dessiné et les planches</td><td class="num">20</td><td>{len(LX.LEXIQUE)} mots. Touchent-ils « voir dans ma langue » à chaque mot, ou jamais ?</td></tr>
    <tr><td>Les exercices : entendre, image, pièges, nombres</td><td class="num">35</td><td>{len(EX.NOMBRES)} nombres et heures, {len(EX.PIEGES)} pièges : lesquels tombent.</td></tr>
    <tr><td>Retour à chaud</td><td class="num">15</td><td>Deux questions, plus bas.</td></tr>
  </tbody></table>
  <table class="cmp" style="margin-top:14px"><thead><tr><th>Séance 2</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>Épeler, ce que le client veut, ce que je réponds</td><td class="num">20</td><td>{len(EX.NOMS)} noms, {len(EX.DEMANDES)} demandes, {len(EX.REPONSES)} répliques ; la règle du relais tient-elle ?</td></tr>
    <tr><td>Au comptoir</td><td class="num">35</td><td>{len(CL.CLIENTS)} clients — {E(clients)}. Trois à cinq minutes chacun ; le compte « réussies sur 8 » et « du premier coup ».</td></tr>
    <tr><td>Le test, repassé (seconde forme)</td><td class="num">20</td><td>L'écart avec la première passation, sur des items nouveaux ; le formateur note l'oral.</td></tr>
    <tr><td>Entretien de groupe</td><td class="num">15</td><td>Les questions, plus bas.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Les règles de décision</h2>
  <div class="these"><p class="cle">On lit le direct de la classe item par item, par groupe, et on décide sur le matériel.</p></div>
  <p>La trousse n'envoie au direct que le <b>premier essai</b> de chaque item. La barre d'un item se lit donc ainsi :
  « 1<sup>er</sup> coup » = réussi d'emblée ; « encore faux » = <b>raté au premier essai</b> (l'employé a pu se
  reprendre ensuite, sur l'appareil). Le direct est à ouvrir par groupe : Progression des élèves, bloc « Le direct de
  la classe », module Hôtel Rive-Claire.</p>
  <table class="cmp"><thead><tr><th>Ce qu'on voit</th><th>Ce qu'on en conclut</th><th>Ce qu'on fait</th></tr></thead><tbody>
    <tr><td>Un item <b>raté au premier essai par la moitié</b> du groupe ou plus</td><td>L'item est en cause : image ambiguë, voix mal dite, distracteur trop proche</td><td>On le réécoute, on le regarde, on le refait</td></tr>
    <tr><td>Un item <b>réussi par tous</b> au premier essai</td><td>Il n'apprend rien à ce groupe</td><td>On le garde pour les débutants, ou on le retire</td></tr>
    <tr><td>Un cran du test que <b>personne ne franchit</b></td><td>Le cran est trop haut, ou mal construit</td><td>On relit ses items avant de toucher à la règle</td></tr>
    <tr><td>Une situation du comptoir que <b>personne ne réussit</b></td><td>La situation est trop dure pour son palier, ou son geste clé mal annoncé</td><td>On relit ses faits et son écran ; on ne baisse pas la règle</td></tr>
    <tr><td>Une <b>promesse hors règle</b> faite par la moitié</td><td>La règle du relais est mal enseignée, pas mal apprise</td><td>On revoit « Ce que je réponds » et la carte de la règle</td></tr>
    <tr><td>Un bilan du comptoir que <b>le formateur contredit</b></td><td>Le juge se trompe sur cette situation</td><td>On note la partie (client, réplique, verdict) : c'est la donnée qui corrige le juge</td></tr>
    <tr><td>Le bouton de traduction <b>jamais touché</b>, ou <b>à chaque mot</b></td><td>La langue d'appui ne joue pas son rôle</td><td>On revoit sa place et sa promesse</td></tr>
  </tbody></table>
  <div class="reserve"><p><strong>Trois limites, à dire soi-même :</strong> trois à six personnes par direction <b>révèlent</b>,
  elles ne prouvent pas ; un groupe qui se sait observé ne joue pas comme seul ; et <b>ce qui remonte à l'employeur est
  un constat sur le matériel, jamais sur une personne</b> — séance sans compte, aucun nom dans les traces.</p></div>
</section>

<section>
  <h2>Le geste clé de chaque situation</h2>
  <p>Une situation est réussie sans promesse hors règle, sans erreur de saisie, avec son geste clé, et les autres
  gestes attendus (un seul peut manquer s'il en reste au moins deux). C'est ce que l'observateur regarde aussi.</p>
  <table class="cmp"><thead><tr><th>Client</th><th>La situation</th><th>★ Geste clé</th></tr></thead><tbody>{cles}</tbody></table>
</section>

<section>
  <h2>Les questions</h2>
  <p><b>À chaud, fin de la séance 1</b> — dans leur langue si besoin :</p>
  <ol class="simple"><li>Qu'est-ce qui était difficile à entendre ?</li><li>Qu'est-ce que vous voulez refaire ?</li></ol>
  <p><b>Entretien, fin de la séance 2</b> :</p>
  <ol class="simple">
    <li>Au comptoir, quel client était le plus dur ? Pourquoi ?</li>
    <li>Le bilan vous a-t-il dit quelque chose de juste ? De faux ?</li>
    <li>Un mot ou une phrase appris ici que vous avez déjà entendu au travail ?</li>
    <li>Qu'est-ce qui manque pour votre comptoir à vous ?</li>
    <li>Le recommanderiez-vous à un collègue ? Que lui diriez-vous ?</li>
  </ol>
  <p><b>Les six gestes du comptoir</b>, à observer (★ : geste clé d'au moins une situation) :</p>
  <ol class="simple">{gestes}</ol>
</section>

<section class="grille-obs">
  <h2>Grille d'observation <small>— à imprimer, une par séance</small></h2>
  <p class="grille-tete">Groupe : ☐ A · fr → en &nbsp;&nbsp; ☐ B · es → fr &nbsp;&nbsp;&nbsp; Séance : ☐ 1 &nbsp; ☐ 2 &nbsp;&nbsp;&nbsp; Date : ____________</p>
  <table class="cmp obs"><thead><tr><th>Repère (jamais un nom)</th><th>Où ça bloque</th><th>Traduction</th><th>Au comptoir : geste vu</th><th>Bilan contesté ?</th><th>Citation</th></tr></thead>
  <tbody>{"".join("<tr><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(6))}</tbody></table>
  <p><button type="button" class="btn-export" onclick="window.print()">Imprimer la grille</button></p>
</section>

<div class="pied"><p>Protocole produit par <code>build/hotel_pilote.py</code> — ne pas l'éditer.
Plan : <a href="hotellerie-plan.html">hotellerie-plan.html</a> · cadrage : <a href="hotellerie-etape0.html">hotellerie-etape0.html</a>.</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — atelier {act['id']}, lettres {'tranchées' if lettres_faites else 'à trancher'}")


CSS = """
.obs td{height:44px}
.obs th,.obs td{border:1px solid #9aa0a6}
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
