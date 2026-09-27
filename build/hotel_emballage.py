#!/usr/bin/env python3
"""L'emballage de l'Hôtel Rive-Claire (étape 6) — le guide du formateur et la
page de démonstration pour l'acheteur.

    python3 build/hotel_emballage.py
      → assets/presentations/hotellerie-guide-formateur.html (+ .pdf)
      → assets/presentations/hotellerie-demo.html

Produites, jamais éditées : chaque chiffre est lu dans le contenu, le catalogue
et le disque. Modèle : build/francoeur_emballage.py.

LE GUIDE DOIT FAIRE MARCHER LA TROUSSE SANS NOUS : mise en place, séance type,
test, comptoir, suivi, dépannage, données.

LA DÉMO NE PROMET QUE CE QUI EST FAIT : ce qui attend encore (le pilote réel, la
relecture de l'anglais et de l'espagnol, les lettres épelées) y est écrit. Les
prix viennent de `build/contenu/entreprise-hotel/prix.py`, le seul endroit où les
changer. La page reste PRIVÉE : elle vit au classeur, jamais au catalogue.
"""
import html, importlib.util, json, pathlib, re, subprocess

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-hotel"
PRES = RACINE / "assets" / "presentations"
GUIDE = PRES / "hotellerie-guide-formateur.html"
DEMO = PRES / "hotellerie-demo.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
APP = "/modules-autonomes/hotel-reception/index.html"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


LX = _charger("he_lexique", CONTENU / "lexique.py")
EX = _charger("he_exercices", CONTENU / "exercices.py")
TS = _charger("he_test", CONTENU / "test.py")
CL = _charger("he_clients", CONTENU / "clients.py")
PX = _charger("he_prix", CONTENU / "prix.py")
RIVE = _charger("he_rive", RACINE / "build" / "hotel_rive.py")


def chiffres():
    sons = RACINE / "assets" / "interactive" / "hotel" / "sons"
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "hotel-reception" in (a.get("interactive") or ""))
    ha = (RACINE / "build" / "hotel_audio.py").read_text(encoding="utf-8")
    return {
        "mots": len(LX.LEXIQUE), "planches": len(LX.PLANCHES),
        "croquis": len(list((RACINE / "assets/interactive/hotel/croquis").glob("*.jpg"))),
        "portraits": len(list((RACINE / "assets/interactive/hotel/clients").glob("*.webp"))),
        # Les prises de lettres (x/lettres) sont des pièces qui servent à assembler
        # les noms épelés, en deux prises chacune : elles ne s'entendent pas telles quelles.
        "voix": len([f for f in sons.rglob("*.mp3") if "lettres" not in f.parts]),
        "pieges": sum(1 for m in LX.LEXIQUE if m[6].startswith("PIÈGE")),
        "exercices": 9, "clients": len(CL.CLIENTS), "gestes": len(CL.GESTES),
        "items_test": len(TS.A[1]) + len(TS.B[1]) + len(TS.C[1]) + len(TS.D[1]),
        "fiches": len(list((PRES / "hotellerie-fiche").glob("*.pdf"))),
        "lettres": not re.search(r"^CHOIX_LETTRES = \{\}", ha, re.M),
        "activite": act["id"], "titre": act["title"], "niveau": act["level"],
    }


def tete(titre):
    t = (PRES / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    t = t[:t.index("<body")]
    return re.sub(r"<title>.*?</title>", f"<title>{E(titre)}</title>", t).replace("</style>", CSS + RIVE.CSS + "</style>", 1)


CSS = """
.captures{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:14px;margin:14px 0}
.captures figure{margin:0}
.captures img{width:100%;border-radius:14px;border:1px solid var(--line);display:block;background:#fff}
.captures figcaption{font-size:14px;margin-top:6px;color:var(--body)}
.captures figcaption b{display:block;color:var(--ink);font-size:15px}
.liens{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}
.liens a{font-size:14px;border:1px solid var(--line-fort);border-radius:8px;padding:5px 9px;text-decoration:none;color:var(--ink);background:var(--card)}
.formules{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px;margin:14px 0}
.formule{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:6px}
.formule.entree{border:2px solid var(--acier)}
.formule h3{margin:0;font-size:18px;color:var(--ink)}
.formule .montant{font-size:26px;font-weight:800;color:var(--ink);margin:4px 0 0;line-height:1.1}
.formule .unite{font-size:14px;color:var(--muted);font-weight:700}
.formule p{margin:0;font-size:15px}
.formule ul{margin:6px 0 0;padding-left:18px;font-size:14.5px}
.formule li{margin:3px 0}
.notes-prix{font-size:14.5px;color:var(--muted)}
.faq dt{font-weight:800;color:var(--ink);margin-top:12px}
.faq dd{margin:4px 0 0}
@media print{
  .retour,.liens{display:none}
  body{background:#fff;color:#000;font-size:11pt;border-top:0}
  section{break-inside:avoid-page}
}
"""

DIRECTIONS = [(p, a) for p in ("fr", "en", "es") for a in ("fr", "en", "es") if p != a]
NOM_L = {"fr": "français", "en": "anglais", "es": "espagnol"}


def guide(c):
    fiches = "".join(f'<a href="hotellerie-fiche/fiche-{p}-{a}.pdf">{NOM_L[p]} → {NOM_L[a]}</a>' for p, a in DIRECTIONS)
    nom_c = lambda k: f"{CL.TITRE[k[1]]['fr']} {k[2]}"
    nom_g = lambda i: next(g["nom"]["fr"] for g in CL.GESTES if g["id"] == i)
    clients = "".join(
        f"<tr><td><b>{E(nom_c(k))}</b>{' · téléphone' if k[4] == 'telephone' else ''}</td><td>{E(k[6]['fr'])}</td>"
        f"<td>★ {E(', '.join(nom_g(i) for i in CL.CLES[k[0]]))}</td></tr>" for k in CL.CLIENTS)
    gestes = "".join(f"<li><b>{E(g['nom']['fr'])}</b> — « {E(g['phrase']['fr'])} »</li>" for g in CL.GESTES)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Hôtel Rive-Claire &middot; pour le formateur</p>
<h1>Le guide du formateur</h1>
<p class="chapeau">Tout ce qu'il faut pour faire travailler un groupe de réceptionnistes <strong>sans personne
d'autre que vous</strong> : la mise en place, une séance type, le test, le comptoir, le suivi, et quoi faire quand ça
casse. L'employé travaille sur son téléphone ; vous travaillez dans le portail.</p>

<section class="premier">
  <h2>Ce que l'employé saura faire</h2>
  <table class="cmp"><tbody>
    <tr><td><b>O1</b></td><td><b>Entendre la demande</b> dite au débit d'un client (type de chambre, nuits, dates) et la saisir juste</td><td class="num">7 sur 8 en série</td></tr>
    <tr><td><b>O2</b></td><td><b>Faire épeler et noter</b> un nom, un numéro de chambre, un prix, une heure, au téléphone compris</td><td class="num">5 de suite sans erreur</td></tr>
    <tr><td><b>O3</b></td><td><b>Les gestes du comptoir</b> : accueillir, confirmer, refuser poliment, expliquer des frais, avec les formules de la langue apprise</td><td class="num">6 situations sur 8 au comptoir</td></tr>
    <tr><td><b>O4</b></td><td><b>Le relais au gérant</b> : garder pour le gérant ce qui lui revient, sans rien promettre</td><td class="num">éliminatoire, dit avant</td></tr>
    <tr><td></td><td colspan="2"><b>La règle du comptoir, la même partout</b> (fiche de poche, exercices, test, comptoir) : {E(EX.REGLE_RELAIS['fr'])}</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Ce que fait la trousse</h2>
  <p><b>Trois langues à égalité</b> — français du Québec, anglais d'Amérique du Nord, espagnol du Mexique. Chaque
  employé choisit la langue qu'il <b>parle</b> (l'écran) et celle qu'il <b>apprend</b> (ce qu'il entend et dit) :
  six directions. Sa langue reste cachée sous chaque mot tant qu'il ne la demande pas.</p>
  <ol class="actions">
    <li><p><b>Le comptoir dessiné</b> — les objets du poste à toucher, entendre, nommer.</p></li>
    <li><p><b>Les planches</b> — {c['planches']} planches, {c['mots']} mots, un croquis et une voix chacun ; les faux amis
      de la paire de langues sont signalés.</p></li>
    <li><p><b>Neuf exercices</b> — du mot entendu aux nombres et aux heures, aux noms épelés, à ce que le client veut
      et à « Ce que je réponds ».</p></li>
    <li><p><b>Mon niveau</b> — un test d'une quinzaine de minutes, deux formes parallèles, qui <b>propose</b> un niveau ;
      c'est vous qui le confirmez.</p></li>
    <li><p><b>Au comptoir</b> — {c['clients']} clients, dont un au téléphone, joués à voix haute ; un bilan par geste.</p></li>
  </ol>
</section>

<section>
  <h2>Avant la première séance</h2>
  <ol class="actions">
    <li><p>Dans le portail, créez un <b>groupe de {E(c['niveau'].lower())}</b> : la trousse est l'atelier
      « {E(c['titre'])} » (activité {c['activite']}), et le niveau du groupe décide de ce qu'il voit.</p></li>
    <li><p>Choisissez l'accès : une <b>séance sans compte</b> (un code et un carré QR imprimés, aucun nom) ou des
      <b>codes d'élèves</b> (pseudonymes seulement). Le comptoir, lui, passe par le serveur : il reçoit le code de la
      séance ou de l'élève.</p></li>
    <li><p>Imprimez les <b>fiches de poche</b>, une par employé, dans sa direction :</p>
      <div class="liens">{fiches}</div></li>
    <li><p>Prévoyez des <b>écouteurs</b> : tout s'écoute, et le téléphone est la situation la plus dure à l'oreille. Le
      micro sert au test et au comptoir ; le navigateur demandera l'autorisation la première fois.</p></li>
    <li><p><b>Un téléphone par personne.</b> Le test et les résultats du comptoir se gardent sur l'appareil ; une
      tablette partagée mêlerait les employés.</p></li>
  </ol>
</section>

<section>
  <h2>Une séance type, 90 minutes</h2>
  <table class="cmp"><tbody>
    <tr><td class="num">10</td><td>Accueil. Chacun choisit sa langue et la langue apprise.</td></tr>
    <tr><td class="num">15</td><td>La première fois : <b>Mon niveau</b>. Ensuite, le comptoir dessiné et une ou deux planches.</td></tr>
    <tr><td class="num">35</td><td><b>Les exercices</b> : entendre, nombres et heures, épeler, ce que le client veut, ce que je réponds.</td></tr>
    <tr><td class="num">25</td><td><b>Au comptoir</b> : deux clients chacun, au niveau confirmé. Lisez le bilan avec eux.</td></tr>
    <tr><td class="num">5</td><td>Le défi de la semaine, sur la fiche de poche.</td></tr>
  </tbody></table>
  <p><b>Après la formation</b> : à J+2, une série d'exercices et un client ; à J+7, le téléphone ; à J+30, le test
  repassé (la forme alterne d'elle-même).</p>
</section>

<section>
  <h2>Le test « Mon niveau »</h2>
  <p>Quatre parties : <b>A</b> la demande (adaptative : trois bonnes montent d'un cran, deux erreurs arrêtent),
  <b>B</b> au téléphone (numéros, prix et heures, noms épelés, tout se tape), <b>C</b> qui décide (je le fais,
  je transmets au gérant, je refuse poliment — accorder soi-même ce qui revient au gérant fait échouer la partie,
  et la règle est affichée avant), <b>D</b> répondre à voix haute (cinq gestes, enregistrés sur l'appareil).
  <b>L'écran ne dit jamais si une réponse est juste.</b></p>
  <p>Une nouvelle passation, et le panneau « Pour le formateur » à la fin, s'ouvrent avec le code <b>{E(TS.CODE_FORMATEUR)}</b>.
  Écoutez les cinq réponses orales, notez chacune sur deux lignes — le geste, puis la langue — et <b>confirmez le
  niveau</b> : débutant, fonctionnel ou à l'aise. C'est ce niveau qui règle la façon de parler des clients du
  comptoir. Confirmer efface les enregistrements (ils ne quittent jamais l'appareil) ; l'écran avertit si l'oral
  n'est pas entièrement noté.</p>
  <div class="reserve"><p><strong>Le code est un frein, pas une serrure</strong> : il empêche l'employé pressé de se
  noter lui-même ou de relancer le test, pas un curieux qui lirait la source de la page. Trois essais faux bloquent
  une minute.</p></div>
</section>

<section>
  <h2>Au comptoir</h2>
  <p>L'employé est le réceptionniste ; <b>c'est lui qui parle le premier</b>. Le client parle la langue apprise ;
  son visage change avec son humeur, et l'humeur s'écrit dessous. Au téléphone, pas de visage, et la voix passe par
  le filtre du téléphone. Chaque situation a un <b>geste clé ★</b>, obligatoire pour la réussir :</p>
  <table class="cmp"><thead><tr><th>Client</th><th>La situation</th><th>Geste clé</th></tr></thead><tbody>{clients}</tbody></table>
  <p>Le bilan dit, geste par geste, ce qui a été fait, avec la phrase à dire dans la langue apprise ; il vérifie ce
  qui a été noté (nom, dates, numéro) contre la vérité du client ; il relève à part toute <b>promesse hors règle</b>,
  qui fait échouer la situation. Une situation est <b>réussie</b> sans promesse, sans erreur de saisie, avec son
  geste clé et les autres gestes attendus (un seul peut manquer s'il en reste au moins deux). L'écran compte les
  situations réussies sur huit, et celles réussies du premier coup. Les six gestes :</p>
  <ol class="simple">{gestes}</ol>
  <p><b>Le bilan peut se tromper</b> : c'est un modèle de langue qui juge. S'il accuse à tort ou laisse passer une
  faute, dites-le à l'employé, et notez la partie (client, réplique, verdict) : c'est ce qui corrige le juge.</p>
</section>

<section>
  <h2>Suivre le groupe</h2>
  <p>Dans <b>Progression des élèves</b>, le direct de la classe montre chaque question des exercices et du test au
  premier essai, et chaque situation du comptoir avec ses gestes, séparés par langue apprise. <b>Ne remontent
  jamais</b> : les phrases dites au comptoir, les enregistrements oraux, la langue de l'employé. Un item raté par la
  moitié du groupe accuse l'item, pas le groupe — signalez-le.</p>
</section>

<section>
  <h2>Quand ça ne marche pas</h2>
  <dl class="faq">
    <dt>Pas de son.</dt><dd>Volume du téléphone, écouteurs branchés, et sur iPhone le bouton silence. Si la voix du
      client ne vient pas au comptoir, l'écran le dit : la réplique reste lisible (touchez « Écouter sans lire »
      pour la voir).</dd>
    <dt>« Le micro n'est pas disponible ».</dt><dd>L'autorisation a été refusée : réglages du navigateur, site,
      micro. On peut toujours écrire sa réponse au clavier.</dd>
    <dt>« Ce code n'est pas accepté ».</dt><dd>Code mal recopié, ou séance fermée. La conversation en cours n'est pas
      perdue : rouvrez la séance ou redonnez le code.</dd>
    <dt>Le comptoir refuse de démarrer.</dt><dd>Si votre centre a choisi le mode <b>sans assistance</b>, le comptoir et
      son bilan sont fermés — ils demandent un modèle de langue. Tout le reste fonctionne. En classe, jouez le client
      vous-même à partir du tableau ci-dessus ; l'employé garde sa fiche de poche en main.</dd>
    <dt>« Trop d'essais. Attendez une minute. »</dt><dd>Le code du formateur a été mal tapé trois fois ; attendez une
      minute, puis retapez-le.</dd>
    <dt>Le bilan ne vient pas.</dt><dd>Touchez « Réessayer le bilan ». La situation n'est comptée qu'une fois le bilan
      rendu.</dd>
  </dl>
</section>

<section>
  <h2>Les données</h2>
  <div class="reserve"><p><strong>Rien de nominatif ne quitte la classe.</strong> Pseudonymes ou séance sans compte.
  Les enregistrements oraux du test restent sur le téléphone et s'effacent à la confirmation du niveau, ou après
  trente jours. Ce qui remonte au portail, ce sont les réponses aux questions fermées et les gestes du comptoir ;
  jamais une voix ni une phrase libre. Ce que l'employeur reçoit, s'il reçoit quelque chose, est un constat sur le
  matériel ou sur le groupe — jamais sur une personne.</p></div>
</section>

<div class="pied"><p>Guide produit par <code>build/hotel_emballage.py</code> — ne pas l'éditer. Imprimable.</p></div>
</div></body></html>"""
    GUIDE.write_text(tete("Hôtel Rive-Claire — guide du formateur") + corps, encoding="utf-8")


CAPTURES = [
    ("langue", "Deux langues à choisir", "Celle qu'on parle, celle qu'on apprend : six directions."),
    ("comptoir", "Le comptoir dessiné", "Les objets du poste, vus de la place du réceptionniste ; toucher fait entendre le mot."),
    ("planche", "Une planche", "Le mot dans la langue apprise, sa voix, et sa langue cachée dessous."),
    ("pieges", "Les faux amis de la paire", "« Embarazada », « la facture », « un cargo » : chaque paire a les siens."),
    ("client", "Ce que le client veut", "La demande au débit d'un client : le lit et les nuits font la différence."),
    ("jeu", "Au comptoir", "Huit clients, un visage qui réagit, une vraie conversation, un bilan par geste."),
]
CAPTURES_V = "1"   # refaites par `node build/hotel_captures.mjs` ; monter ce numéro après


def demo(c):
    caps = "".join(f'<figure><img src="hotellerie-captures/{i}.png?v={CAPTURES_V}" alt="{E(t)}" loading="lazy">'
                   f'<figcaption><b>{E(t)}</b>{E(l)}</figcaption></figure>' for i, t, l in CAPTURES)
    essais = "".join(f'<a href="{APP}?{q}" target="_blank" rel="noopener">{E(t)}</a>' for t, q in [
        ("Le choix des langues", "#langue"),
        ("Le comptoir, en anglais", "parle=fr&apprend=en#comptoir"),
        ("Les faux amis, espagnol → français", "parle=es&apprend=fr#x-pieges"),
        ("Au téléphone : les nombres", "parle=fr&apprend=en#x-nombres"),
        ("Au comptoir (demande un code)", "parle=es&apprend=fr#jeu")])
    formules = "".join(
        f'<div class="formule{" entree" if n == 0 else ""}"><h3>{E(t)}</h3>'
        f'<p class="montant">{E(m)}</p><span class="unite">{E(u)}</span><p>{E(pq)}</p>'
        f'<ul>{"".join(f"<li>{E(x)}</li>" for x in inc)}</ul></div>'
        for n, (t, m, u, pq, inc) in enumerate(PX.FORMULES))
    notes = "".join(f"<li>{E(x)}</li>" for x in PX.NOTES)
    reste = ["un pilote avec deux petits groupes de vrais réceptionnistes",
             "la relecture de l'anglais et de l'espagnol par un locuteur de chaque langue"]
    if not c["lettres"]:
        reste.append("le choix, à l'oreille, de la prise de quelques lettres épelées")
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#hotellerie"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Formation au poste &middot; hôtellerie</p>
<h1>Hôtel Rive-Claire : la langue du comptoir</h1>
<p class="chapeau">Vos réceptionnistes reçoivent des clients qui ne parlent pas leur langue. Ce qui fait rater
une arrivée, ce n'est pas d'ignorer le mot <em>king</em> : c'est de mal entendre un nom au téléphone, de noter
le 14 pour le 15, ou de promettre un rabais qui ne leur revient pas. <strong>Cette trousse leur apprend les mots du
comptoir, à entendre le client dit à vitesse réelle, à faire épeler et confirmer — et à passer au gérant ce qui
lui revient.</strong></p>

<section class="premier">
  <h2>Ce que l'employé voit, sur son téléphone</h2>
  <div class="captures">{caps}</div>
  <p>Essayer, sans compte :</p><div class="liens">{essais}</div>
</section>

<section>
  <h2>Ce qu'il y a dedans</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">3</span><span class="q">langues à égalité, six directions : français du Québec, anglais nord-américain, espagnol du Mexique</span></div>
    <div class="ch"><span class="n">{c['mots']}</span><span class="q">mots du comptoir, en {c['planches']} planches</span></div>
    <div class="ch"><span class="n">{c['voix']}</span><span class="q">extraits de voix, Azure HD, six voix</span></div>
    <div class="ch"><span class="n">{c['clients']}</span><span class="q">clients au comptoir, dont un au téléphone</span></div>
  </div>
  <table class="cmp"><tbody>
    <tr><td><b>Apprendre les mots</b></td><td>{c['croquis']} croquis, dont un grand comptoir dessiné vu de la place du réceptionniste ; {c['pieges']} faux amis signalés, chacun dans sa paire de langues.</td></tr>
    <tr><td><b>S'exercer</b></td><td>Neuf exercices : le mot entendu, les nombres et les heures, les noms épelés au téléphone, ce que le client veut, « Ce que je réponds ».</td></tr>
    <tr><td><b>Mesurer</b></td><td>Un test d'une quinzaine de minutes, en deux formes parallèles, qui propose un niveau ; le formateur écoute l'oral et confirme.</td></tr>
    <tr><td><b>Pratiquer</b></td><td>Un jeu de rôle à voix haute dans la langue apprise ; le client réagit ; le bilan dit quels gestes ont été faits, vérifie ce qui a été noté, et relève toute promesse hors règle.</td></tr>
    <tr><td><b>Garder en poche</b></td><td>Une fiche imprimable par direction : six phrases du comptoir, la règle du relais, les faux amis, l'alphabet pour épeler.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Comment ça se déploie</h2>
  <ol class="actions">
    <li><p><b>Sur le téléphone de l'employé</b>, par un carré QR : aucun compte à créer, aucune application à installer.</p></li>
    <li><p><b>Avec un formateur</b>, qui a son guide : deux à quatre séances de 90 minutes, puis en libre-service.</p></li>
    <li><p><b>Sans données personnelles</b> : aucun nom, l'oral reste sur l'appareil. Ce qui remonte est un constat sur
      le matériel ou sur le groupe, jamais sur une personne (Loi 25).</p></li>
  </ol>
</section>

<section>
  <h2>Les prix</h2>
  <div class="formules">{formules}</div>
  <ul class="simple notes-prix">{notes}</ul>
</section>

<section>
  <h2>Où nous en sommes</h2>
  <div class="reserve"><p><strong>La trousse est construite et jouable</strong>, et chacune de ses étapes est passée par
  la boucle didactique jusqu'à zéro défaut majeur. Il lui reste : {E(' ; '.join(reste))}. Le premier contrat se
  construit donc avec vous, à votre réception.</p></div>
  <p>La même méthode se transpose à un autre poste d'accueil — restaurant, clinique, location d'autos : on change
  le lexique, le décor et les clients ; le reste suit.</p>
</section>

<div class="pied"><p>Page produite par <code>build/hotel_emballage.py</code> — chaque chiffre est lu dans le contenu.</p></div>
</div></body></html>"""
    DEMO.write_text(tete("Hôtel Rive-Claire — la langue du comptoir") + corps, encoding="utf-8")


def main():
    c = chiffres()
    guide(c)
    demo(c)
    if pathlib.Path(CHROME).exists():
        pdf = GUIDE.with_suffix(".pdf")
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", "http://localhost:5412/assets/presentations/" + GUIDE.name],
                       capture_output=True, timeout=120)
        print(f"  {pdf.name} {pdf.stat().st_size // 1024 if pdf.exists() else 0} ko")
    print(f"  guide et démo — {c['mots']} mots, {c['voix']} voix, {c['clients']} clients, {c['fiches']} fiches, "
          f"atelier {c['activite']}, lettres {'tranchées' if c['lettres'] else 'à trancher'}")


if __name__ == "__main__":
    main()
