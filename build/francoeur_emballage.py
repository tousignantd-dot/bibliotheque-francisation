#!/usr/bin/env python3
"""L'emballage de la Maison Francœur (étape 6) — le guide du formateur et la
page de démonstration pour l'acheteur.

    python3 build/francoeur_emballage.py
      → assets/presentations/francoeur-guide-formateur.html (+ .pdf)
      → assets/presentations/francoeur-demo.html

Produites, jamais éditées : chaque chiffre est lu dans le contenu, le
catalogue et le disque. Une page de vente qui annonce « 149 mots » le jour où
il y en a 151 est une page qui ment.

LE GUIDE DOIT FAIRE MARCHER LA TROUSSE SANS NOUS : le réseau qui l'achète la
livre lui-même (mémoire chantier-detail-chaussure). Il dit donc aussi quoi faire
quand ça casse — pas de son, micro refusé, code refusé, centre sans assistance.

LA DÉMO NE PROMET QUE CE QUI EST FAIT : ce qui attend encore (le pilote réel,
la relecture des langues) y est écrit. Les prix viennent de `prix.py`, le seul
endroit où les changer (ajoutés à la demande de Daniel, 24 septembre 2026).
"""
import html, json, pathlib, re, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-francoeur"
sys.path.insert(0, str(CONTENU))
from lexique import LEXIQUE, PLANCHES  # noqa: E402
from demandes import DEMANDES  # noqa: E402
import test as TEST  # noqa: E402
from clients import CLIENTS, GESTES  # noqa: E402
from prix import FORMULES, NOTES  # noqa: E402

PRES = RACINE / "assets" / "presentations"
GUIDE = PRES / "francoeur-guide-formateur.html"
DEMO = PRES / "francoeur-demo.html"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
APP = "/modules-autonomes/francoeur-planches/index.html"
E = html.escape


def chiffres():
    trad = json.loads((CONTENU / "traductions.json").read_text(encoding="utf-8"))
    sons = RACINE / "assets" / "interactive" / "francoeur" / "sons"
    act = next(a for a in json.load(open(RACINE / "data" / "activities.json", encoding="utf-8"))
               if "francoeur-planches" in (a.get("interactive") or ""))
    return {
        "mots": len(LEXIQUE), "rayons": len(PLANCHES),
        "croquis": len(list((RACINE / "assets/interactive/francoeur/croquis").glob("*.jpg"))),
        "portraits": len(list((RACINE / "assets/interactive/francoeur/clients").glob("*.jpg"))),
        # Les candidats des reprises (sons/_candidats/) ne sont pas des voix de la
        # trousse : les compter faisait annoncer 219 voix au lieu de 197.
        "voix": len([f for f in sons.rglob("*.mp3") if "_candidats" not in f.parts]),
        "langues": len(trad),
        "relues": sum(1 for v in trad.values() if v.get("relu")),
        "demandes": len(DEMANDES), "clients": len(CLIENTS),
        "items_test": len(TEST.A_CRAN1) + len(TEST.A_CRAN2) + len(TEST.A_CRAN3) + len(TEST.B) + len(TEST.C),
        "fiches": len(list((PRES / "francoeur-fiche").glob("*.pdf"))),
        "activite": act["id"], "titre": act["title"], "niveau": act["level"],
        "trad": trad,
    }


def tete(titre):
    t = (PRES / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    t = t[:t.index("<body")]
    return re.sub(r"<title>.*?</title>", f"<title>{E(titre)}</title>", t).replace("</style>", CSS + "</style>", 1)


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
  body{background:#fff;color:#000;font-size:11pt}
  section{break-inside:avoid-page}
}
"""


def guide(c):
    fiches = "".join(f'<a href="francoeur-fiche/fiche-{code}.pdf">{E(nom)}</a>'
                     for code, nom in [("fr", "Français seulement")] + [(k, v["loc"]) for k, v in c["trad"].items()])
    clients = "".join(f"<tr><td><b>{E(n)}</b></td><td>{E(carte)}</td><td>{', '.join(dict(debutant='débutant', fonctionnel='fonctionnel', aise='à l’aise')[p] for p in pal)}</td></tr>"
                      for _i, n, _v, pal, carte, _p, _f in CLIENTS)
    gestes = "".join(f"<li><b>{E(g['nom'])}</b> — « {E(g['phrase'])} »</li>" for g in GESTES)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Maison Francœur &middot; pour le formateur</p>
<h1>Le guide du formateur</h1>
<p class="chapeau">Tout ce qu'il faut pour faire travailler un groupe d'employés <strong>sans personne d'autre
que vous</strong> : la mise en place, une séance type, le test, le magasin, le suivi, et quoi faire quand ça
casse. L'employé travaille sur son téléphone ; vous travaillez dans le portail.</p>

<section class="premier">
  <h2>Ce que l'employé saura faire</h2>
  <p>Cinq objectifs, chacun avec son seuil. Les bilans des exercices et le résultat du test se lisent contre eux.</p>
  <table class="cmp"><tbody>
    <tr><td><b>O1</b></td><td>Devant un mot du plancher dit à voix haute, <b>désigner</b> l'article, sans traduction</td><td class="num">8 sur 10</td></tr>
    <tr><td><b>O2</b></td><td>Devant une demande de client dite vite (article, couleur, taille), <b>choisir</b> l'article exact</td><td class="num">7 sur 10</td></tr>
    <tr><td><b>O3</b></td><td>Quand il n'a pas compris, <b>faire répéter</b> ou <b>faire préciser</b> au lieu de deviner</td><td class="num">chaque fois</td></tr>
    <tr><td><b>O4</b></td><td>Devant ce qu'il ne peut pas garantir, <b>vérifier</b> ou <b>passer le relais</b> à la gérante, sans promettre</td><td class="num">chaque fois</td></tr>
    <tr><td><b>O5</b></td><td>Devant une consigne de la gérante, <b>désigner</b> l'objet ou le lieu visé</td><td class="num">7 sur 10</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Ce que fait la trousse</h2>
  <p>Un employé qui ne parle pas encore français apprend les mots de son magasin et à comprendre ses clients.
  Il choisit sa langue d'appui — ou aucune — puis avance dans quatre espaces :</p>
  <ol class="actions">
    <li><p><b>Apprendre les mots</b> — {c['rayons']} rayons, {c['mots']} mots, un croquis et une voix pour chacun ; la
      traduction se révèle au toucher, jamais d'emblée.</p></li>
    <li><p><b>Je m'exerce</b> — sept exercices, du mot entendu à la demande du client dite à vitesse réelle,
      aux consignes de la gérante et à « Ce que je réponds ». Une série « Les pièges » met les faux amis côte à côte.</p></li>
    <li><p><b>Les gestes du vendeur</b> — cinq dialogues modèles : on entend un vendeur faire chaque geste, avant de le faire soi-même.</p></li>
    <li><p><b>Mon niveau</b> — un test de dix minutes qui <b>propose</b> un niveau ; c'est vous qui le confirmez. Deux formes
      équivalentes : la seconde passation ne reprend pas les questions de la première.</p></li>
    <li><p><b>Le magasin</b> — {c['clients']} clients, un visage qui réagit, une conversation à voix haute.</p></li>
  </ol>
</section>

<section>
  <h2>Avant la première séance</h2>
  <ol class="actions">
    <li><p>Dans le portail, créez un <b>groupe de {E(c['niveau'].lower())}</b> : la trousse est l'atelier
      « {E(c['titre'])} » (activité {c['activite']}), et le niveau du groupe décide de ce qu'il voit.</p></li>
    <li><p>Choisissez l'accès : une <b>séance sans compte</b> (un code et un carré QR imprimés, aucun nom) ou des
      <b>codes d'élèves</b> (pseudonymes seulement, jamais le vrai nom).</p></li>
    <li><p>Imprimez les <b>fiches de poche</b>, une par employé, dans sa langue :</p>
      <div class="liens">{fiches}</div></li>
    <li><p>Prévoyez des <b>écouteurs</b> : tout s'écoute. Le micro sert au test et au magasin ; le navigateur
      demandera l'autorisation la première fois.</p></li>
  </ol>
</section>

<section>
  <h2>Les rappels, après la formation</h2>
  <p>Un geste appris une fois ne tient pas une semaine. L'écran propose de lui-même une <b>série de rappel</b> quand
  l'employé revient après deux jours ou plus, avec les mots qu'il a ratés en tête. Prévoyez aussi :</p>
  <table class="cmp"><tbody>
    <tr><td><b>J+2</b></td><td>une série de rappel (huit mots, dont ceux à revoir) et « Ce que le client veut ».</td></tr>
    <tr><td><b>J+7</b></td><td>« Ce que je réponds », puis un client au magasin ; le défi de la semaine de la fiche de poche.</td></tr>
    <tr><td><b>J+30</b></td><td>le test « Mon niveau », repassé — il prend la seconde forme, et compare avec la première passation.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Une séance type, 90 minutes</h2>
  <table class="cmp"><tbody>
    <tr><td class="num">10</td><td>Accueil. Chacun ouvre la trousse et choisit sa langue d'appui — ou « Français seulement ».</td></tr>
    <tr><td class="num">15</td><td>La première fois : <b>Mon niveau</b>. Ensuite, un rayon par séance dans <b>Apprendre les mots</b>.</td></tr>
    <tr><td class="num">35</td><td><b>Je m'exerce</b>, filtré sur le rayon du jour. Terminez par « Ce que le client veut » et « Ce que la gérante demande ».</td></tr>
    <tr><td class="num">10</td><td><b>Les gestes du vendeur</b> : écouter les dialogues modèles, puis « Ce que je réponds ».</td></tr>
    <tr><td class="num">15</td><td><b>Le magasin</b> : un ou deux clients chacun, au niveau confirmé. Le bilan dit quels gestes ont été faits.</td></tr>
    <tr><td class="num">5</td><td>Le défi de la semaine, sur la fiche de poche.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Le test « Mon niveau »</h2>
  <p>Quatre parties — les mots, le client, la gérante, parler. Il s'adapte : trois bonnes réponses montent d'un
  cran, deux erreurs arrêtent la partie. <b>L'écran ne dit jamais si une réponse est juste.</b> Au résultat, chaque
  partie est comparée au seuil de son objectif. La partie « Parler » met l'employé devant quatre situations qui
  exigent chacune un geste — faire répéter, faire préciser, vérifier, passer le relais : vous notez si le geste est
  fait, pas la grammaire.</p>
  <p>À la fin, sous « Pour le formateur » : écoutez les deux réponses orales avec l'employé, notez-les, et
  <b>confirmez le niveau</b> — débutant, fonctionnel ou à l'aise. C'est ce niveau qui ouvre les clients du
  magasin. Refaites le test à la dernière séance : l'écran compare avec la première passation.</p>
</section>

<section>
  <h2>Le magasin</h2>
  <table class="cmp"><thead><tr><th>Client</th><th>Ce qui l'attend</th><th>Niveaux</th></tr></thead><tbody>{clients}</tbody></table>
  <p>Le visage du client change avec son humeur, et l'humeur s'écrit dessous. Au bout, le bilan dit, geste par
  geste, ce qui a été fait et ce qui reste à faire, avec la phrase à dire ; la correction des phrases vient en
  second. Les cinq gestes :</p>
  <ol class="simple">{gestes}</ol>
</section>

<section>
  <h2>Suivre le groupe</h2>
  <p>Dans <b>Progression des élèves</b>, le direct de la classe montre chaque question des exercices et du test,
  avec le taux de réussite du premier coup, ainsi que chaque visite au magasin. <b>Ne remontent jamais</b> : les
  phrases libres du magasin, les enregistrements oraux, la langue choisie. Un item raté par la moitié du groupe
  accuse l'item, pas le groupe — signalez-le.</p>
</section>

<section>
  <h2>Quand ça ne marche pas</h2>
  <dl class="faq">
    <dt>Pas de son.</dt><dd>Volume du téléphone, écouteurs branchés, et sur iPhone le bouton silence. Si la voix
      du client ne vient pas au magasin, l'écran le dit : la réplique reste lisible.</dd>
    <dt>« Le micro n'est pas disponible ».</dt><dd>L'autorisation a été refusée : réglages du navigateur, site,
      micro. On peut toujours écrire sa réponse au clavier.</dd>
    <dt>« Ce code n'est pas reconnu ».</dt><dd>Code mal recopié, ou séance fermée. Rouvrez la séance ou
      redonnez le code.</dd>
    <dt>Le magasin refuse de démarrer.</dt><dd>Si votre centre a choisi le mode <b>sans assistance</b>, le magasin
      et son bilan sont fermés — ils demandent un modèle de langue. Tout le reste fonctionne. En classe, jouez le
      client vous-même à partir du tableau ci-dessus : l'employé garde sa fiche de poche en main.</dd>
    <dt>Pas de traduction pour une langue.</dt><dd>« Voir dans ma langue » n'apparaît pas en mode « Français
      seulement ». Pour une langue choisie, l'écran signale une traduction pas encore relue.</dd>
  </dl>
</section>

<section>
  <h2>Les données</h2>
  <div class="reserve"><p><strong>Rien de nominatif ne quitte la classe.</strong> Pseudonymes ou séance sans
  compte ; les résultats du test et l'oral restent sur le téléphone ; ce qui remonte au portail, ce sont des
  réponses à des questions fermées. Ce que l'employeur reçoit, s'il reçoit quelque chose, est un constat sur le
  matériel ou sur le groupe — jamais sur une personne.</p></div>
</section>

<div class="pied"><p>Guide produit par <code>build/francoeur_emballage.py</code> — ne pas l'éditer. Imprimable.</p></div>
</div></body></html>"""
    GUIDE.write_text(tete("Maison Francœur — guide du formateur") + corps, encoding="utf-8")


CAPTURES = [
    ("langue", "Sa langue, ou aucune", "« Français seulement » en tête ; onze langues d'appui dessous."),
    ("rayons", "Les rayons du magasin", "Rangés comme un magasin est rangé ; la consigne dans sa langue, sous le français."),
    ("planche", "Une planche", "Des croquis de catalogue, numérotés ; toucher fait entendre le mot."),
    ("fiche", "Le piège, expliqué", "« Une veste » n'a pas de manches au Québec — ici en arabe, de droite à gauche."),
    ("client", "Ce que le client veut", "La demande à vitesse réelle ; la couleur et la taille font la différence."),
    ("magasin", "Le magasin", "Huit clients, un visage qui réagit, une vraie conversation."),
]


def demo(c):
    caps = "".join(f'<figure><img src="francoeur-captures/{i}.png" alt="{E(t)}" loading="lazy">'
                   f'<figcaption><b>{E(t)}</b>{E(l)}</figcaption></figure>' for i, t, l in CAPTURES)
    essais = "".join(f'<a href="{APP}?{q}" target="_blank" rel="noopener">{E(t)}</a>' for t, q in [
        ("Le choix de langue", "ecran=langue"), ("Un rayon, en espagnol", "langue=es&ecran=planche&p=exterieur"),
        ("Un piège, en arabe", "langue=ar&ecran=planche&p=hauts&a=veste&voir=1"),
        ("Ce que le client veut", "langue=es&ecran=exercice&x=client"),
        ("Les clients du magasin", "langue=fr&ecran=magasin&niveau=aise")])
    formules = "".join(
        f'<div class="formule{" entree" if n == 0 else ""}"><h3>{E(t)}</h3>'
        f'<p class="montant">{E(m)}</p><span class="unite">{E(u)}</span><p>{E(pq)}</p>'
        f'<ul>{"".join(f"<li>{E(x)}</li>" for x in inc)}</ul></div>'
        for n, (t, m, u, pq, inc) in enumerate(FORMULES))
    notes = "".join(f"<li>{E(x)}</li>" for x in NOTES)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Formation au poste &middot; commerce de détail</p>
<h1>Maison Francœur : le français du plancher</h1>
<p class="chapeau">Vos employés vendent des vêtements et ne parlent pas encore français. Ce qui leur fait
rater une vente, ce n'est pas d'ignorer le mot <em>cardigan</em> : c'est de ne pas comprendre la question
du client, dite vite, avec une couleur et une taille dans la même phrase. <strong>Cette trousse leur apprend
les mots du rayon, puis à comprendre le client — et à dire « un instant, s'il vous plaît ».</strong></p>

<section class="premier">
  <h2>Ce que l'employé voit, sur son téléphone</h2>
  <div class="captures">{caps}</div>
  <p>Essayer, sans compte :</p><div class="liens">{essais}</div>
</section>

<section>
  <h2>Ce qu'il y a dedans</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">{c['mots']}</span><span class="q">mots du magasin, en {c['rayons']} rayons</span></div>
    <div class="ch"><span class="n">{c['langues']}</span><span class="q">langues d'appui — ou aucune</span></div>
    <div class="ch"><span class="n">{c['voix']}</span><span class="q">voix enregistrées, Azure HD, français du Québec</span></div>
    <div class="ch"><span class="n">{c['clients']}</span><span class="q">clients au magasin, sur trois niveaux</span></div>
  </div>
  <table class="cmp"><tbody>
    <tr><td><b>Apprendre les mots</b></td><td>{c['croquis']} croquis de catalogue ; le mot d'ici en tête (« chandail »), l'autre dessous (« pull ») ; huit pièges France-Québec signalés.</td></tr>
    <tr><td><b>S'exercer</b></td><td>Sept exercices, dont {c['demandes']} demandes de clients à vitesse réelle, les consignes de la gérante et « Ce que je réponds ».</td></tr>
    <tr><td><b>Voir faire</b></td><td>Cinq dialogues modèles : on entend un vendeur faire chaque geste avant de le faire soi-même.</td></tr>
    <tr><td><b>Mesurer</b></td><td>Un test de dix minutes, adaptatif, en deux formes équivalentes : repassé à la fin sur des questions nouvelles, il montre ce qui a été appris, objectif par objectif.</td></tr>
    <tr><td><b>Pratiquer</b></td><td>Un jeu de rôle à voix haute ; le visage du client montre l'effet de ce qu'on lui dit, et le bilan dit quels gestes ont été faits.</td></tr>
    <tr><td><b>Garder en poche</b></td><td>Une fiche imprimable par langue : six phrases du vendeur, les pièges, les tailles, les couleurs.</td></tr>
  </tbody></table>
</section>

<section>
  <h2>Comment ça se déploie</h2>
  <ol class="actions">
    <li><p><b>Sur le téléphone de l'employé</b>, par un carré QR : aucun compte à créer, aucune application à installer.</p></li>
    <li><p><b>Avec un formateur</b>, qui a son guide : deux à quatre séances de 90 minutes, puis en libre-service.</p></li>
    <li><p><b>Sans données personnelles</b> : aucun nom, l'oral reste sur l'appareil. Ce qui remonte est un
      constat sur le matériel ou sur le groupe, jamais sur une personne (Loi 25).</p></li>
  </ol>
</section>

<section>
  <h2>Les prix</h2>
  <div class="formules">{formules}</div>
  <ul class="simple notes-prix">{notes}</ul>
</section>

<section>
  <h2>Où nous en sommes</h2>
  <div class="reserve"><p><strong>La trousse est construite et jouable.</strong> Il lui reste l'épreuve qui
  compte : un pilote avec un petit groupe de vrais employés, dont nous lirons ce que le matériel fait rater
  avant de le déclarer terminé. Les traductions sont faites dans les {c['langues']} langues et attendent la
  relecture d'une personne qui parle chacune ({c['relues']} relue{'s' if c['relues'] > 1 else ''} à ce jour).
  Le premier contrat se construit donc avec vous, sur votre plancher.</p></div>
  <p>La même méthode se transpose à une autre enseigne — chaussures, quincaillerie, épicerie : on change le
  lexique, les croquis et les clients ; le reste suit.</p>
</section>

<div class="pied"><p>Page produite par <code>build/francoeur_emballage.py</code> — chaque chiffre est lu dans le contenu.</p></div>
</div></body></html>"""
    DEMO.write_text(tete("Maison Francœur — le français du plancher") + corps, encoding="utf-8")


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
    print(f"  guide et démo — {c['mots']} mots, {c['voix']} voix, {c['langues']} langues, "
          f"{c['fiches']} fiches, activité {c['activite']}")


if __name__ == "__main__":
    main()
