#!/usr/bin/env python3
"""Le protocole du pilote de Chez Jocelyne (étape 5).

    python3 build/restauration_pilote.py   # → assets/presentations/restauration/restauration-pilote.html

Produite, jamais éditée. Les chiffres (mots, exercices, items du test,
situations, gestes) sont LUS dans le contenu, pour que la page ne mente pas le
jour où l'un d'eux change. Modèle : build/hotel_pilote.py.

LE PILOTE EST UN DIAGNOSTIC DIDACTIQUE, pas une évaluation : on évalue le
MATÉRIEL par les réponses des employés. Un item raté au premier essai par la
moitié du groupe accuse l'item. Ce qui remonte à l'employeur est un constat sur
le matériel, jamais sur une personne.

CE QUI CHANGE PAR RAPPORT À L'HÔTEL : une seule langue apprise (le français),
mais DEUX POSTES — la cuisine et la salle. Le pilote réunit les deux dans un
même groupe (les exercices de mots sont communs) et lit le service par porte.
L'allergie est éliminatoire partout : c'est la première chose qu'on lit.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
SORTIE = RACINE / "assets" / "presentations" / "restauration" / "restauration-pilote.html"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def main():
    LX = _charger("rp_lexique", CONTENU / "lexique.py")
    EX = _charger("rp_exercices", CONTENU / "exercices.py")
    TS = _charger("rp_test", CONTENU / "test.py")
    SI = _charger("rp_situations", CONTENU / "situations.py")
    ID = _charger("rp_identite", CONTENU / "identite.py")
    HP = _charger("rp_hotel_pilote", RACINE / "build" / "hotel_pilote.py")
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "restaurant-planches" in (a.get("interactive") or ""))
    niveau = act["level"].split()[-1]
    n_test = sum(len(TS.A[1][c]) for c in (1, 2, 3)) + len(TS.B_CHEF[1]) + len(TS.B_COMMANDE[1]) + len(TS.C[1]) + len(TS.D[1])
    n_pieges = sum(1 for m in LX.LEXIQUE if m[5].startswith("PIÈGE"))
    sit = {p: [s for s in SI.SITUATIONS if s[1] == p] for p in ("cuisine", "salle")}
    nom_g = {g["id"]: g["nom"] for g in SI.GESTES}
    cles = "".join(f"<tr><td>{'Cuisine' if s[1] == 'cuisine' else 'Salle'}</td><td>{E(s[2])} — {E(s[5])}</td>"
                   f"<td>{E(', '.join(nom_g[g] for g in s[6]))}</td><td>{E(', '.join({'debutant': 'débutant', 'fonctionnel': 'fonctionnel', 'aise': 'à l’aise'}[p] for p in s[4]))}</td></tr>"
                   for s in SI.SITUATIONS)
    gestes = "".join(f"<li>{E(g['nom'])} — « {E(g['phrase'])} »</li>" for g in SI.GESTES)
    regle = "".join(f"<li>{E(l)}</li>" for l in EX.REGLE)

    avant = [
        ("Ajouter l'atelier au catalogue EN LIGNE",
         f"L'entrée « {E(act['title'])} » (atelier {act['id']}, niveau {E(niveau)}) est dans le dépôt, mais le catalogue "
         "du portail vit dans le volume de Railway : il faut l'ajouter par le portail (Ajouter une activité, lien "
         "<code>modules-autonomes/restaurant-planches/index.html</code>, catégorie atelier, niveau 3). Sans elle, "
         "la séance sans compte ne peut pas s'ouvrir sur la trousse.",
         "Vous. Cinq minutes."),
        ("L'essayer sur un vrai téléphone",
         "Avec un code d'élève : une situation en cuisine (le bruit « Fort », la voix du chef), une en salle, la dictée "
         "au micro. Personne n'a encore entendu le mélange de la voix et du bruit, ni essayé la dictée.",
         "Vous. Vingt minutes."),
        ("Faire relire les langues d'appui",
         "Au moins celles des employés du pilote. La règle d'allergie, le critère de gravité et les gestes d'abord : c'est "
         "ce qu'un employé lit pour une décision éliminatoire. Puis les mots et les consignes. Chaque langue est marquée "
         "« non relue » à l'écran.",
         "Un employé bilingue par langue, idéalement du pilote."),
        ("Faire vérifier deux normes",
         "Le hamburger (bœuf haché) toujours bien cuit, et la zone de danger des températures : écrites au lexique "
         "« à revérifier (MAPAQ) ». La trousse ne remplace pas la formation d'hygiène exigée.",
         "Le restaurant ou le formateur."),
        ("Créer le groupe et imprimer",
         f"Un groupe pilote <b>au niveau {E(niveau)}</b> — un groupe d'un autre niveau ne peut pas ouvrir la séance —, "
         "une séance sans compte, la feuille QR, et la grille d'observation plus bas, une par séance.",
         "Le formateur."),
    ]
    avant_html = "".join(f"<li><p><b>{E(t)}</b> — {d}</p><p class=\"qui\">{E(q)}</p></li>" for t, d, q in avant)

    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", f"<title>{E(ID.NOM)} — le pilote</title>", tete)
    tete = tete.replace("</style>", HP.CSS + "</style>", 1)

    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{E(ID.NOM)} &middot; étape 5</p>
<h1>Le pilote</h1>
<p class="chapeau">Faire jouer la trousse par de vrais employés de restaurant — en cuisine et en salle — et lire
<strong>ce que le matériel fait rater</strong>. Ce n'est pas une évaluation des personnes : c'est un diagnostic
didactique. Un item raté au premier essai par la moitié du groupe accuse l'item ; une situation que personne ne
réussit accuse la situation. <strong>L'allergie se lit en premier</strong> : c'est la seule erreur éliminatoire.</p>

<section class="premier">
  <h2>Avant le pilote</h2>
  <ol class="actions">{avant_html}</ol>
</section>

<section>
  <h2>Un groupe, deux postes</h2>
  <table class="cmp"><thead><tr><th></th><th>En cuisine</th><th>En salle</th></tr></thead><tbody>
    <tr><td><b>Qui</b></td><td>Commis, cuisiniers, plongeurs qui commencent</td><td>Serveurs, hôtes, caissiers qui commencent</td></tr>
    <tr><td><b>L'IA joue</b></td><td>Le chef Réal</td><td>Les clients</td></tr>
    <tr><td><b>Situations</b></td><td class="num">{len(sit['cuisine'])}</td><td class="num">{len(sit['salle'])}</td></tr>
    <tr><td><b>Ce qui compte d'abord</b></td><td>Redire la consigne, dire ce qui manque, l'allergie et la table</td><td>Redire la commande, faire préciser, l'allergie</td></tr>
  </tbody></table>
  <p><b>Quatre à huit personnes</b>, les deux postes mêlés : les mots et les exercices sont communs ; le service se
  choisit par porte. Langue d'appui : français seul, ou l'une des onze langues de l'outil, au choix de chacun. Encadrement : un
  formateur qui mène, un observateur qui ne parle pas et note. Matériel : leurs téléphones, des écouteurs (le chef
  se parle dans le bruit), la feuille QR. Durée : <b>deux séances de 90 minutes à une semaine d'écart</b> — le test
  se repasse à la fin, dans sa seconde forme.</p>
</section>

<section>
  <h2>Mise en place, dans le portail</h2>
  <ol class="actions">
    <li><p>Créer le groupe, puis ouvrir une <b>séance sans compte</b> sur « {E(act['title'])} » (atelier {act['id']}) :
      aucun nom, un code et un carré QR imprimés. Chaque réponse fermée remonte au <b>direct de la classe</b>
      (progression.html), au premier essai, question par question ; chaque situation du service, avec ses gestes et,
      s'il y a lieu, « erreur grave à l'allergie ». Ne remontent jamais : les phrases dites au service, l'oral du test,
      le test lui-même, la langue d'appui.</p></li>
    <li><p>Le service et ses voix passent par le serveur : <b>en séance, ils reçoivent le code de la séance</b>. Si le
      centre a refusé le mode avec assistance, le service ne s'ouvre pas — le vérifier avant.</p></li>
    <li><p>Le test garde son historique <b>sur l'appareil</b> : un téléphone par personne, jamais une tablette partagée.
      Le code du formateur ouvre la notation de l'oral, la confirmation du niveau et « Refaire ».</p></li>
  </ol>
</section>

<section>
  <h2>Le déroulé</h2>
  <table class="cmp"><thead><tr><th>Séance 1</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>Langue, puis le test (première forme)</td><td class="num">20</td><td>{n_test} items ; A adaptative, B entendue une seule fois, C l'allergie, D redire à voix haute. Le formateur note l'oral et confirme le niveau.</td></tr>
    <tr><td>Le poste de cuisine et les planches</td><td class="num">20</td><td>{len(LX.LEXIQUE)} mots, {n_pieges} pièges. Touchent-ils « voir dans ma langue » à chaque mot, ou jamais ?</td></tr>
    <tr><td>Les exercices : entendre, image, pièges, la consigne du chef</td><td class="num">35</td><td>{len(EX.CONSIGNES)} consignes dans le bruit : lesquelles tombent, et à quel réglage du bruit.</td></tr>
    <tr><td>Retour à chaud</td><td class="num">15</td><td>Deux questions, plus bas.</td></tr>
  </tbody></table>
  <table class="cmp" style="margin-top:14px"><thead><tr><th>Séance 2</th><th>Min.</th><th>Ce qu'on regarde</th></tr></thead><tbody>
    <tr><td>La commande modifiée, l'allergie, je le redis</td><td class="num">25</td><td>{len(EX.COMMANDES)} commandes, {len(EX.ALLERGIES)} cas d'allergie : les erreurs graves, une par une.</td></tr>
    <tr><td>Le service</td><td class="num">30</td><td>Chacun joue sa porte : deux ou trois situations, trois à cinq minutes chacune, dont l'allergie.</td></tr>
    <tr><td>Le test, repassé (seconde forme)</td><td class="num">20</td><td>« Avant → maintenant » à l'écran ; le formateur note l'oral.</td></tr>
    <tr><td>Entretien de groupe</td><td class="num">15</td><td>Les questions, plus bas.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Les règles de décision</h2>
  <div class="these"><p class="cle">On lit le direct de la classe item par item et on décide sur le matériel.</p></div>
  <p>La trousse n'envoie au direct que le <b>premier essai</b> de chaque item. La barre d'un item se lit donc ainsi :
  « 1<sup>er</sup> coup » = réussi d'emblée ; « encore faux » = <b>raté au premier essai</b> (l'employé a pu se reprendre
  ensuite, sur l'appareil). Le direct s'ouvre par groupe : Progression des élèves, bloc « Le direct de la classe ».</p>
  <table class="cmp"><thead><tr><th>Ce qu'on voit</th><th>Ce qu'on en conclut</th><th>Ce qu'on fait</th></tr></thead><tbody>
    <tr><td>Une <b>erreur grave à l'allergie</b>, même une seule</td><td>Soit l'item est trompeur, soit le geste n'est pas acquis</td><td>On relit l'item et son acte avec la personne ; au travail, elle ne sert pas seule une allergie avant de l'avoir reprise</td></tr>
    <tr><td>Un item <b>raté au premier essai par la moitié</b> du groupe ou plus</td><td>L'item est en cause : image ambiguë, voix mal dite, distracteur trop proche</td><td>On le réécoute, on le regarde, on le refait</td></tr>
    <tr><td>Un item <b>réussi par tous</b> au premier essai</td><td>Il n'apprend rien à ce groupe</td><td>On le garde pour les débutants, ou on le retire</td></tr>
    <tr><td>Une consigne du chef ratée <b>seulement au bruit « Fort »</b></td><td>Le bruit, pas la langue</td><td>On règle le bruit par défaut, pas la consigne</td></tr>
    <tr><td>Une situation du service que <b>personne ne réussit</b></td><td>Trop dure pour son palier, ou son geste mal annoncé</td><td>On relit ses faits et sa carte ; on ne baisse pas la règle</td></tr>
    <tr><td>Un bilan du service que <b>le formateur contredit</b></td><td>Le juge se trompe sur cette situation</td><td>On note la partie (situation, réplique, verdict) : c'est la donnée qui corrige le juge</td></tr>
    <tr><td>Le bouton de traduction <b>jamais touché</b>, ou <b>à chaque mot</b></td><td>La langue d'appui ne joue pas son rôle</td><td>On revoit sa place et sa promesse</td></tr>
  </tbody></table>
  <div class="reserve"><p><strong>Trois limites, à dire soi-même :</strong> quatre à huit personnes <b>révèlent</b>, elles ne
  prouvent pas ; un groupe qui se sait observé ne joue pas comme seul ; et <b>ce qui remonte à l'employeur est un constat
  sur le matériel, jamais sur une personne</b> — séance sans compte, aucun nom dans les traces. La trousse ne remplace
  pas la formation d'hygiène et de salubrité exigée.</p></div>
</section>

<section>
  <h2>La règle d'allergie, telle que la trousse l'enseigne</h2>
  <ol class="simple">{regle}</ol>
  <p>{E(EX.REGLE_PREFERENCE)} {E(EX.REGLE_CUISINE)}</p>
  <p><b>{E(EX.CRITERE_GRAVE)}</b></p>
</section>

<section>
  <h2>Les situations du service</h2>
  <table class="cmp"><thead><tr><th>Porte</th><th>La situation</th><th>Gestes jugés</th><th>Paliers</th></tr></thead><tbody>{cles}</tbody></table>
  <p><b>Les gestes</b>, à observer :</p>
  <ol class="simple">{gestes}</ol>
</section>

<section>
  <h2>Les questions</h2>
  <p><b>À chaud, fin de la séance 1</b> — dans leur langue si besoin :</p>
  <ol class="simple"><li>Qu'est-ce qui était difficile à entendre ?</li><li>Le bruit de cuisine vous a-t-il aidé ou gêné ?</li></ol>
  <p><b>Entretien, fin de la séance 2</b> :</p>
  <ol class="simple">
    <li>Au service, quelle situation était la plus dure ? Pourquoi ?</li>
    <li>Le bilan vous a-t-il dit quelque chose de juste ? De faux ?</li>
    <li>Une consigne ou une phrase apprise ici que vous avez déjà entendue au travail ?</li>
    <li>Qu'est-ce qui manque pour votre cuisine ou votre salle à vous ?</li>
    <li>Le recommanderiez-vous à un collègue ? Que lui diriez-vous ?</li>
  </ol>
</section>

<section class="grille-obs">
  <h2>Grille d'observation <small>— à imprimer, une par séance</small></h2>
  <p class="grille-tete">Séance : ☐ 1 &nbsp; ☐ 2 &nbsp;&nbsp;&nbsp; Date : ____________</p>
  <table class="cmp obs"><thead><tr><th>Repère (jamais un nom)</th><th>Poste</th><th>Où ça bloque</th><th>Allergie : geste vu</th><th>Bilan contesté ?</th><th>Citation</th></tr></thead>
  <tbody>{"".join("<tr><td>&nbsp;</td><td></td><td></td><td></td><td></td><td></td></tr>" for _ in range(8))}</tbody></table>
  <p><button type="button" class="btn-export" onclick="window.print()">Imprimer la grille</button></p>
</section>

<div class="pied"><p>Protocole produit par <code>build/restauration_pilote.py</code> — ne pas l'éditer.
Plan : <a href="restauration-plan.html">restauration-plan.html</a> · cadrage : <a href="restauration-etape0.html">restauration-etape0.html</a>
· l'écran : <a href="/modules-autonomes/restaurant-planches/index.html">restaurant-planches</a>.</p></div>
</div></body></html>"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — atelier {act['id']}, {n_test} items de test, {len(SI.SITUATIONS)} situations")


if __name__ == "__main__":
    main()
