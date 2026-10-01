#!/usr/bin/env python3
"""L'emballage de Chez Jocelyne (étape 6) — le guide du formateur et la page de
démonstration pour l'acheteur.

    python3 build/restauration_emballage.py
      → assets/presentations/restauration/restauration-guide-formateur.html (+ .pdf)
      → assets/presentations/restauration/restauration-demo.html

Produites, jamais éditées : chaque chiffre est lu dans le contenu, le catalogue et
le disque. Modèle : build/hotel_emballage.py.

LE GUIDE DOIT FAIRE MARCHER LA TROUSSE SANS NOUS : mise en place, séance type,
test, service, suivi, dépannage, données.

LA DÉMO NE PROMET QUE CE QUI EST FAIT : ce qui attend encore (le pilote réel, la
relecture de l'espagnol et de l'anglais, les portraits, deux normes à vérifier)
y est écrit. Les prix viennent de `build/contenu/entreprise-restaurant/prix.py`,
le seul endroit où les changer — et la page dit qu'ils sont à confirmer tant que
Daniel ne l'a pas fait. La page reste PRIVÉE : elle vit au classeur, jamais au
catalogue.
"""
import html, importlib.util, json, pathlib, re, subprocess

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
PRES = RACINE / "assets" / "presentations" / "restauration"
GUIDE = PRES / "restauration-guide-formateur.html"
DEMO = PRES / "restauration-demo.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
APP = "/modules-autonomes/restaurant-planches/index.html"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


LX = _charger("re_lexique", CONTENU / "lexique.py")
EX = _charger("re_exercices", CONTENU / "exercices.py")
TS = _charger("re_test", CONTENU / "test.py")
SI = _charger("re_situations", CONTENU / "situations.py")
PX = _charger("re_prix", CONTENU / "prix.py")
ID = _charger("re_identite", CONTENU / "identite.py")
HE = _charger("re_hotel_emballage", RACINE / "build" / "hotel_emballage.py")   # sa feuille de style seulement


def chiffres():
    sons = RACINE / "assets" / "interactive" / "restaurant" / "sons"
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "restaurant-planches" in (a.get("interactive") or ""))
    return {
        "mots": len(LX.LEXIQUE), "planches": len(LX.PLANCHES),
        "croquis": len([f for f in (RACINE / "assets/interactive/restaurant/croquis").glob("*.jpg") if f.stem != "poste"]),
        "voix": len(list(sons.rglob("*.mp3"))),
        "pieges": sum(1 for m in LX.LEXIQUE if m[5].startswith("PIÈGE")),
        "consignes": len(EX.CONSIGNES), "commandes": len(EX.COMMANDES), "allergies": len(EX.ALLERGIES),
        "situations": len(SI.SITUATIONS), "gestes": len(SI.GESTES),
        "items_test": sum(len(TS.A[1][c]) for c in (1, 2, 3)) + len(TS.B_CHEF[1]) + len(TS.B_COMMANDE[1]) + len(TS.C[1]) + len(TS.D[1]),
        "fiches": len(list((PRES / "fiche").glob("*.pdf"))),
        "activite": act["id"], "titre": act["title"], "niveau": act["level"],
    }


def tete(titre):
    t = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    t = t[:t.index("<body")]
    return re.sub(r"<title>.*?</title>", f"<title>{E(titre)}</title>", t).replace("</style>", HE.CSS + "\n/* (audit de design, majeur) l'en-tête recopié pose table{min-width:640px} : au téléphone, toute la page dézoomait. */\ntable.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}\n" + "</style>", 1)


NIV = {"debutant": "débutant", "fonctionnel": "fonctionnel", "aise": "à l'aise"}


def guide(c):
    nom_g = {g["id"]: g["nom"] for g in SI.GESTES}
    sits = "".join(f"<tr><td>{'Cuisine' if s[1] == 'cuisine' else 'Salle'}</td><td><b>{E(s[2])}</b> — {E(s[5])}</td>"
                   f"<td>{E(', '.join(nom_g[g] for g in s[6]))}</td><td>{E(', '.join(NIV[p] for p in s[4]))}</td></tr>"
                   for s in SI.SITUATIONS)
    gestes = "".join(f"<li><b>{E(g['nom'])}</b> — « {E(g['phrase'])} »</li>" for g in SI.GESTES)
    regle = "".join(f"<li>{E(l)}</li>" for l in EX.REGLE)
    TR = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    fiches = '<a href="fiche/fiche-fr.pdf">Français seulement</a>' + "".join(
        f'<a href="fiche/fiche-{l}.pdf">{E(TR[l]["loc"])}</a>' for l in ID.LANGUES_APPUI if l in TR)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{E(ID.NOM)} &middot; pour le formateur</p>
<h1>Le guide du formateur</h1>
<p class="chapeau">Tout ce qu'il faut pour faire travailler un groupe d'employés de restaurant — en cuisine et en
salle — <strong>sans personne d'autre que vous</strong> : la mise en place, une séance type, le test, le service joué,
le suivi, et quoi faire quand ça casse. L'employé travaille sur son téléphone ; vous travaillez dans le portail.</p>

<section class="premier">
  <h2>Ce que l'employé saura faire</h2>
  <table class="cmp"><tbody>
    <tr><td><b>O1</b></td><td><b>Exécuter une consigne du chef</b>, entendue une fois, au débit réel et dans le bruit, en la redisant (« Oui, chef : … »)</td><td class="num">7 sur 8</td></tr>
    <tr><td><b>O2</b></td><td><b>Traiter une allergie</b> : la faire répéter, l'écrire, la dire à la cuisine, vérifier — jamais affirmer qu'un allergène est absent</td><td class="num">éliminatoire, dit avant</td></tr>
    <tr><td><b>O3</b></td><td><b>Reconnaître</b> les objets, les aliments et les gestes du poste</td><td class="num">18 mots sur 20</td></tr>
    <tr><td><b>O4</b></td><td><b>Prendre une commande modifiée</b> (sans, avec, extra, à part, la cuisson) et la redire au client</td><td class="num">5 sur 6</td></tr>
  </tbody></table>
  <p><b>La règle d'allergie, la même partout</b> (fiche de poche, exercices, test, service) :</p>
  <ol class="simple">{regle}</ol>
  <p>{E(EX.REGLE_PREFERENCE)} {E(EX.REGLE_CUISINE)} <b>{E(EX.CRITERE_GRAVE)}</b></p>
</section>

<section>
  <h2>Ce que fait la trousse</h2>
  <p>On apprend le <b>français d'ici</b>. Chaque employé choisit une langue d'appui — français seulement, ou l'une des
  {len(ID.LANGUES_APPUI)} langues de l'outil (arabe, espagnol, ukrainien, persan, chinois, portugais, anglais, roumain, ourdou,
  russe, tigrigna) : elle s'écrit <b>sous</b> les consignes, et sous chaque mot tant qu'il ne la demande pas, elle reste cachée.</p>
  <ol class="actions">
    <li><p><b>Apprendre les mots</b> — le poste de cuisine dessiné (la ligne, le passe, la plonge…), puis
      {c['planches']} planches, {c['mots']} mots, un croquis et une voix ; {c['pieges']} mots d'ici qui piègent sont signalés.</p></li>
    <li><p><b>Je m'exerce</b> — huit exercices : le mot entendu, l'image, se souvenir, les pièges, <b>la consigne du
      chef dans le bruit</b> ({c['consignes']}), <b>la commande modifiée</b> ({c['commandes']}), <b>l'allergie</b>
      ({c['allergies']} cas, règle affichée avant), et « Je le redis » à voix haute.</p></li>
    <li><p><b>Mon niveau</b> — un test d'une douzaine de minutes ({c['items_test']} items), deux formes, qui
      <b>propose</b> un niveau ; c'est vous qui le confirmez.</p></li>
    <li><p><b>Le service</b> — {c['situations']} situations jouées à voix haute : le chef en cuisine, les clients en
      salle ; un bilan par geste, et l'erreur grave à l'allergie relevée à part.</p></li>
  </ol>
</section>

<section>
  <h2>Avant la première séance</h2>
  <ol class="actions">
    <li><p>Dans le portail, créez un <b>groupe de {E(c['niveau'].lower())}</b> : la trousse est l'atelier
      « {E(c['titre'])} » (activité {c['activite']}), et le niveau du groupe décide de ce qu'il voit.</p></li>
    <li><p>Choisissez l'accès : une <b>séance sans compte</b> (un code et un carré QR imprimés, aucun nom) ou des
      <b>codes d'élèves</b> (pseudonymes seulement). Le service passe par le serveur : il reçoit le code de la séance
      ou de l'élève.</p></li>
    <li><p>Imprimez les <b>fiches de poche</b>, une par employé, dans sa langue d'appui :</p>
      <div class="liens">{fiches}</div></li>
    <li><p>Prévoyez des <b>écouteurs</b> : le chef se parle dans le bruit de cuisine (réglable : aucun, faible, fort).
      Le micro sert au test et au service ; le navigateur demandera l'autorisation la première fois. Sans micro, on
      écrit sa réponse au clavier.</p></li>
    <li><p><b>Un téléphone par personne.</b> Le test se garde sur l'appareil ; une tablette partagée mêlerait les employés.</p></li>
  </ol>
</section>

<section>
  <h2>Une séance type, 90 minutes</h2>
  <table class="cmp"><tbody>
    <tr><td class="num">10</td><td>Accueil. Chacun choisit sa langue d'appui.</td></tr>
    <tr><td class="num">15</td><td>La première fois : <b>Mon niveau</b>. Ensuite, le poste de cuisine et une ou deux planches.</td></tr>
    <tr><td class="num">35</td><td><b>Les exercices</b> : la consigne du chef (le bruit au « Faible », puis au « Fort »), la commande, l'allergie.</td></tr>
    <tr><td class="num">25</td><td><b>Le service</b> : deux situations chacun, à sa porte, au niveau confirmé. Lisez le bilan avec eux.</td></tr>
    <tr><td class="num">5</td><td>Le défi de la semaine, sur la fiche de poche.</td></tr>
  </tbody></table>
  <p><b>Après la formation</b> : à J+2, une série d'exercices et une situation ; à J+7, l'allergie ; à J+30, le test
  repassé (la forme alterne d'elle-même, et l'écran montre « Avant → maintenant »).</p>
</section>

<section>
  <h2>Le test « Mon niveau »</h2>
  <p>Quatre parties : <b>A</b> les mots (adaptative : trois bonnes montent d'un cran, deux erreurs arrêtent),
  <b>B</b> une seule écoute (quatre consignes du chef dans le bruit, quatre commandes), <b>C</b> l'allergie (une seule
  erreur grave fait échouer la partie, et la règle est affichée avant), <b>D</b> redire à voix haute (trois phrases,
  enregistrées sur l'appareil). <b>L'écran ne dit jamais si une réponse est juste.</b></p>
  <p>Le panneau « Pour le formateur », à la fin, s'ouvre avec le code <b>{E(TS.CODE_FORMATEUR)}</b>. Écoutez les trois
  réponses orales, notez chacune sur deux lignes — ce qui est redit, puis la langue — et <b>confirmez le niveau</b> :
  débutant, fonctionnel ou à l'aise. C'est lui qui règle la façon de parler du chef et des clients. Sans micro,
  l'écran le dit : faites redire les trois phrases de vive voix (la phrase est écrite, et s'écoute) et notez-les.
  Tant que l'oral n'est pas noté, le niveau reste <b>provisoire</b> et ne dépasse pas « fonctionnel ». Confirmer
  efface les enregistrements ; « Refaire le test » est dans votre panneau.</p>
  <div class="reserve"><p><strong>Le code est un frein, pas une serrure</strong> : il empêche l'employé pressé de se
  noter lui-même, pas un curieux qui lirait la source de la page.</p></div>
</section>

<section>
  <h2>Le service joué</h2>
  <p>En cuisine, l'employé est commis et <b>le chef Réal</b> lui parle ; dès le niveau fonctionnel, le texte du chef
  est caché et le bruit de cuisine joue — il faut l'entendre. En salle, l'employé sert et <b>un client</b> lui parle.
  L'humeur du personnage s'écrit sous la scène. Quand l'employé va vérifier à la cuisine, un bouton lui donne la
  réponse de la cuisine : il la transmet, il ne l'invente pas.</p>
  <table class="cmp"><thead><tr><th>Porte</th><th>La situation</th><th>Gestes jugés</th><th>Niveaux</th></tr></thead><tbody>{sits}</tbody></table>
  <p>Le bilan dit, geste par geste, ce qui a été fait, avec la phrase à dire ; un geste que le personnage a dû
  souffler (« Redis-moi ça ») ne compte pas. <b>L'erreur grave à l'allergie</b> — dire qu'un plat est sûr sans
  vérifier, redire la mauvaise allergie ou la mauvaise table — est relevée à part, en tête. Les gestes :</p>
  <ol class="simple">{gestes}</ol>
  <p><b>Le bilan peut se tromper</b> : c'est un modèle de langue qui juge. S'il accuse à tort ou laisse passer une
  faute, dites-le à l'employé, et notez la partie (situation, réplique, verdict) : c'est ce qui corrige le juge.</p>
</section>

<section>
  <h2>Suivre le groupe</h2>
  <p>Dans <b>Progression des élèves</b>, le direct de la classe montre chaque question des exercices au premier essai
  (une allergie ratée porte « erreur grave »), et chaque situation du service avec ses gestes. <b>Ne remontent
  jamais</b> : les phrases dites au service, le test, les enregistrements oraux, la langue d'appui. Un item raté par la
  moitié du groupe accuse l'item, pas le groupe — signalez-le. <b>Une erreur grave à l'allergie, même une seule</b> :
  reprenez le cas avec la personne avant qu'elle serve seule.</p>
</section>

<section>
  <h2>Quand ça ne marche pas</h2>
  <dl class="faq">
    <dt>Pas de son.</dt><dd>Volume du téléphone, écouteurs branchés, et sur iPhone le bouton silence. Si la voix du
      chef ou du client ne vient pas, l'écran le dit ; touchez « Écouter sans lire » pour voir la réplique.</dd>
    <dt>« Le micro n'est pas disponible ».</dt><dd>L'autorisation a été refusée : réglages du navigateur, site,
      micro. On peut toujours écrire sa réponse au clavier ; au test, l'oral se fait avec vous.</dd>
    <dt>« Ce code n'est pas reconnu ».</dt><dd>Code mal recopié, ou séance fermée. Redonnez le code, ou rouvrez la séance.</dd>
    <dt>« Problème de connexion ».</dt><dd>Touchez « Réessayer » : la conversation reprend là où elle était.</dd>
    <dt>Le service refuse de démarrer.</dt><dd>Si votre centre a choisi le mode <b>sans assistance</b>, le service et son
      bilan sont fermés. Tout le reste fonctionne. Jouez alors le chef ou le client vous-même, à partir du tableau
      ci-dessus ; l'employé garde sa fiche de poche en main.</dd>
    <dt>Le bilan dit « pas évalué cette fois ».</dt><dd>Le juge n'a pas rendu ce geste : rejouez la situation, ou
      jugez-le vous-même.</dd>
  </dl>
</section>

<section>
  <h2>Les données</h2>
  <div class="reserve"><p><strong>Rien de nominatif ne quitte la classe.</strong> Pseudonymes ou séance sans compte. Ce
  que l'employé dit ou écrit au service part au service d'assistance qui répond, et n'est pas gardé chez nous ; la
  dictée du navigateur, elle, passe par le fournisseur du navigateur. Les enregistrements du test restent sur le
  téléphone et s'effacent à la confirmation du niveau. Ce qui remonte au portail, ce sont les réponses aux questions
  fermées et les gestes du service — jamais une voix ni une phrase libre. Ce que l'employeur reçoit, s'il reçoit
  quelque chose, est un constat sur le matériel ou sur le groupe — jamais sur une personne.</p></div>
  <div class="reserve"><p><strong>La trousse ne remplace pas la formation en hygiène et salubrité</strong> exigée des
  restaurants ; deux normes citées (le hamburger toujours bien cuit, la zone de danger) sont à confirmer auprès du
  MAPAQ.</p></div>
</section>

<div class="pied"><p>Guide produit par <code>build/restauration_emballage.py</code> — ne pas l'éditer. Imprimable.</p></div>
</div></body></html>"""
    GUIDE.write_text(tete(f"{ID.NOM} — guide du formateur") + corps, encoding="utf-8")


CAPTURES = [
    ("accueil", "Quatre portes", "Apprendre les mots, s'exercer, mon niveau, le service."),
    ("poste", "Le poste de cuisine", "Vu de la place du commis : on touche la ligne, le passe, la plonge pour entendre leur nom."),
    ("planche", "Un mot, ses pièges", "« La poêle » n'est pas « le poêle » : le mot d'ici, sa voix, sa langue cachée dessous."),
    ("chef", "La consigne du chef", "Dite au débit réel, dans le bruit de cuisine réglable : où vont les assiettes sales ?"),
    ("allergie", "L'allergie, éliminatoire", "La règle en trois gestes, lue à voix haute, avant chaque série."),
    ("service", "Le service joué", "Le chef en cuisine, les clients en salle, une vraie conversation, un bilan par geste."),
]
CAPTURES_V = "1"   # refaites par `node build/restauration_captures.mjs` ; monter ce numéro après


def demo(c):
    caps = "".join(f'<figure><img src="captures/{i}.png?v={CAPTURES_V}" alt="{E(t)}" loading="lazy">'
                   f'<figcaption><b>{E(t)}</b>{E(l)}</figcaption></figure>' for i, t, l in CAPTURES)
    essais = "".join(f'<a href="{APP}?{q}" target="_blank" rel="noopener">{E(t)}</a>' for t, q in [
        ("Le poste de cuisine", "langue=es&planche=poste"),
        ("Les mots d'ici qui piègent", "langue=en&ex=pieges"),
        ("La consigne du chef", "langue=es&ex=chef"),
        ("L'allergie", "langue=en&ex=allergie"),
        ("Le service (demande un code)", "langue=es&ecran=service")])
    formules = "".join(
        f'<div class="formule{" entree" if n == 0 else ""}"><h3>{E(t)}</h3>'
        f'<p class="montant">{E(m)}</p><span class="unite">{E(u)}</span><p>{E(pq)}</p>'
        f'<ul>{"".join(f"<li>{E(x)}</li>" for x in inc)}</ul></div>'
        for n, (t, m, u, pq, inc) in enumerate(PX.FORMULES))
    notes = "".join(f"<li>{E(x)}</li>" for x in PX.NOTES)
    a_confirmer = "" if PX.CONFIRME else ('<div class="reserve"><p><strong>Prix à confirmer.</strong> Ces montants reprennent '
                                          'ceux de la Maison Francœur (une langue apprise, un groupe pilote) ; ils ne sont '
                                          'pas encore confirmés pour la restauration.</p></div>')
    reste = ["un pilote avec un groupe de vrais employés de cuisine et de salle",
             "la relecture de l'espagnol et de l'anglais par un locuteur de chaque langue",
             "les portraits du chef et des clients (la scène montre le décor en attendant)",
             "la vérification de deux normes d'hygiène citées (MAPAQ)"]
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Formation au poste &middot; restauration</p>
<h1>{E(ID.NOM)} : la langue de la cuisine et de la salle</h1>
<p class="chapeau">Vos nouveaux employés comprennent le français de la classe. Ce qui fait rater un service, c'est
autre chose : une consigne du chef criée dans le bruit, une commande qui se reprend (« une poutine… non, des frites »),
et surtout une allergie mal entendue ou rassurée trop vite. <strong>Cette trousse leur apprend les mots du poste, à
entendre le chef et le client à vitesse réelle, à redire avant d'agir — et à traiter une allergie sans jamais
affirmer ce qu'ils n'ont pas vérifié.</strong></p>

<section class="premier">
  <h2>Ce que l'employé voit, sur son téléphone</h2>
  <div class="captures">{caps}</div>
  <p>Essayer, sans compte :</p><div class="liens">{essais}</div>
</section>

<section>
  <h2>Ce qu'il y a dedans</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">{c['mots']}</span><span class="q">mots de la cuisine et de la salle, en {c['planches']} planches et un poste dessiné</span></div>
    <div class="ch"><span class="n">{c['voix']}</span><span class="q">extraits de voix, Azure HD</span></div>
    <div class="ch"><span class="n">{c['situations']}</span><span class="q">situations jouées : le chef en cuisine, les clients en salle</span></div>
    <div class="ch"><span class="n">{len(ID.LANGUES_APPUI)}</span><span class="q">langues d'appui, de l'arabe au tigrigna, sous le français ; ou le français seul</span></div>
  </div>
  <table class="cmp"><tbody>
    <tr><td><b>Apprendre les mots</b></td><td>{c['croquis']} croquis, dont un poste de cuisine vu de la place du commis ; {c['pieges']} mots d'ici qui piègent (le poêle et la poêle, une liqueur, le dîner…).</td></tr>
    <tr><td><b>S'exercer</b></td><td>Huit exercices : la consigne du chef dans un bruit de cuisine réglable, la commande modifiée, l'allergie et sa règle, redire à voix haute.</td></tr>
    <tr><td><b>Mesurer</b></td><td>Un test d'une douzaine de minutes, en deux formes, qui propose un niveau ; le formateur écoute l'oral et confirme. Repassé à la fin : « avant → maintenant ».</td></tr>
    <tr><td><b>Pratiquer</b></td><td>Un jeu de rôle à voix haute : le chef ou le client réagit ; le bilan dit quels gestes ont été faits, et relève à part toute erreur grave à l'allergie.</td></tr>
    <tr><td><b>Garder en poche</b></td><td>Une fiche imprimable par langue d'appui : les phrases de la cuisine et de la salle, la règle d'allergie, ce qu'on crie, les pièges.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Comment ça se déploie</h2>
  <ol class="actions">
    <li><p><b>Sur le téléphone de l'employé</b>, par un carré QR : aucun compte à créer, aucune application à installer.</p></li>
    <li><p><b>Avec un formateur</b>, qui a son guide : deux à quatre séances de 90 minutes, puis en libre-service.</p></li>
    <li><p><b>Sans données personnelles</b> : aucun nom, l'oral du test reste sur l'appareil. Ce qui remonte est un
      constat sur le matériel ou sur le groupe, jamais sur une personne (Loi 25).</p></li>
    <li><p><b>Elle ne remplace pas</b> la formation en hygiène et salubrité exigée : elle donne la langue pour la suivre.</p></li>
  </ol>
</section>

<section>
  <h2>Les prix</h2>
  {a_confirmer}
  <div class="formules">{formules}</div>
  <ul class="simple notes-prix">{notes}</ul>
</section>

<section>
  <h2>Où nous en sommes</h2>
  <div class="reserve"><p><strong>La trousse est construite et jouable</strong>, et ses exercices, son test et son service
  sont passés par la boucle didactique jusqu'à zéro défaut majeur. Il lui reste : {E(' ; '.join(reste))}. Le premier
  contrat se construit donc avec vous, dans votre restaurant.</p></div>
</section>

<div class="pied"><p>Page produite par <code>build/restauration_emballage.py</code> — chaque chiffre est lu dans le contenu.</p></div>
</div></body></html>"""
    DEMO.write_text(tete(f"{ID.NOM} — la langue de la cuisine et de la salle") + corps, encoding="utf-8")


def main():
    c = chiffres()
    guide(c)
    demo(c)
    if pathlib.Path(CHROME).exists():
        pdf = GUIDE.with_suffix(".pdf")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", "http://localhost:5412/assets/presentations/restauration/" + GUIDE.name],
                       capture_output=True, timeout=120)
        print(f"  {pdf.name} {pdf.stat().st_size // 1024 if pdf.exists() else 0} ko")
    print(f"  guide et démo — {c['mots']} mots, {c['voix']} voix, {c['situations']} situations, {c['fiches']} fiches, "
          f"atelier {c['activite']}, prix {'confirmés' if PX.CONFIRME else 'à confirmer'}")


if __name__ == "__main__":
    main()
