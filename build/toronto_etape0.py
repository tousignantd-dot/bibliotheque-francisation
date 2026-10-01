#!/usr/bin/env python3
"""La page de l'étape 0 d'« Une semaine à Toronto » — le cadrage.

    python3 build/toronto_etape0.py   # → assets/presentations/toronto/toronto-etape0.html

Produite, jamais éditée. Elle lit `build/contenu/toronto/lexique.py`, les
croquis de `assets/interactive/toronto/croquis/` (s'ils existent) et l'audition
de `assets/presentations/toronto/voix/` avec sa retranscription.

Le 1er octobre 2026, Daniel a pris toutes les recommandations du plan, puis il est
parti une heure en disant « prends les décisions » : chaque choix de cette page
porte donc déjà une décision PRISE (marquée « décidé »), qu'il peut renverser au
retour d'un clic. « Exporter » rend un JSON à recoller dans la séance suivante.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
_s = importlib.util.spec_from_file_location("toronto_lexique", RACINE / "build/contenu/toronto/lexique.py")
LX = importlib.util.module_from_spec(_s); _s.loader.exec_module(LX)

CROQUIS = RACINE / "assets" / "interactive" / "toronto" / "croquis"
VOIX = RACINE / "assets" / "presentations" / "toronto" / "voix"
SORTIE = RACINE / "assets" / "presentations" / "toronto" / "toronto-etape0.html"
TETE_DE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
E = html.escape

OBJECTIFS = [
    ("O1", "Comprendre la réponse",
     "une réponse de service entendue une fois, au débit normal (un prix, une heure, un « oui, mais »), avec un "
     "accent de Toronto au palier 3 — et en déduire ce qu'on paiera vraiment (taxe et pourboire compris)",
     "8 réponses sur 10 ; le total à 1 $ près, 4 fois sur 5"),
    ("O2", "Obtenir ce qu'on veut",
     "au comptoir, au guichet, à la réception : demander, faire répéter ou épeler au besoin, sans passer au "
     "français ni montrer son téléphone",
     "8 situations jouées sur 10 réussies, selon les gestes de leur bilan"),
    ("O3", "Dire une allergie et vérifier la réponse",
     "au restaurant et au comptoir du marché : la dire avant de commander, comprendre la réponse, refuser un plat "
     "dont on n'est pas sûr",
     "toutes — une seule erreur fait échouer (éliminatoire, dit d'avance)"),
    ("O4", "Tenir deux minutes de bavardage",
     "avec la Torontoise qui revient : répondre à « Where are you from? », « What have you seen? », et relancer",
     "au moins deux relances (« And you? ») par conversation, 4 conversations sur 6"),
]
ALIGNEMENT = [
    ("O1", "Ce qu'on me répond · Les nombres, les prix, les heures · Le total à payer",
     "Partie B · la réponse entendue", "Le café · La tour CN · Le marché · Les îles"),
    ("O2", "Je le dis · Où je vais · les planches de mots",
     "Partie A · les mots ; Partie D · je le dis", "Union · L'hôtel · Kensington · La pharmacie · Le départ"),
    ("O3", "La série de l'allergie (un contre-exemple par série)",
     "Partie C · l'allergie", "Le restaurant (et le comptoir du marché)"),
    ("O4", "Le petit bavardage (planche et « Je le dis ») · J'écris ma carte postale",
     "Partie D · une question de bavardage", "La Torontoise, chaque jour"),
]

# Les faits de la ville, cherchés le 1er octobre 2026 (sources officielles d'abord).
FAITS = [
    ("Le passage du TTC (métro, tramway, autobus)", "3,30 $ en touchant le lecteur (carte PRESTO, carte de crédit ou de "
     "débit, téléphone) ; 3,35 $ comptant. Correspondance de deux heures comprise quand on touche ; aucune pour le "
     "comptant. Enfants de 12 ans et moins : gratuit. Jetons et billets papier : finis depuis le 1er juin 2025.",
     "ttc.ca/Fares-and-passes"),
    ("Le tarif aîné du TTC", "2,25 $ avec une carte PRESTO seulement ; une carte bancaire touchée paie le plein tarif.",
     "ttc.ca/Fares-and-passes"),
    ("L'UP Express (Union ↔ Pearson)", "12,35 $ au billet, 9,25 $ en touchant une carte ; un train toutes les 15 minutes ; "
     "environ 25 minutes (25 ou 28 selon les sources).", "upexpress.com"),
    ("La taxe", "13 % (TVH : 5 % fédéral + 8 % de l'Ontario), ajoutée à la caisse : les prix affichés ne la comprennent pas.",
     "Agence du revenu du Canada"),
    ("Le pourboire", "18 à 20 % du montant avant taxe au restaurant ; les terminaux proposent 18, 20, 25 %, parfois plus. "
     "On ne dira pas que les serveurs sont payés sous le minimum : c'est fini en Ontario depuis 2022.",
     "guides de Toronto, CBC"),
    ("La tour CN", "Entrée générale adulte à heure fixe : 47 $ (taxes en sus) ; tous les billets sont datés et horodatés.",
     "cntower.ca"),
    ("Le traversier des îles", "9,57 $ aller-retour adulte ; en ligne ou au terminal Jack Layton. L'hiver (du 14 octobre à la "
     "mi-avril), seule l'île Ward est desservie.", "toronto.ca"),
    ("Le marché St. Lawrence", "Marché Sud du mardi au dimanche, fermé le lundi ; le sandwich au bacon de dos en est la spécialité.",
     "stlawrencemarket.com"),
    ("Le Musée royal de l'Ontario", "Prix variable selon le jour (environ 26 $ par adulte) ; gratuit le 3e mardi du mois en soirée, sur réservation.",
     "rom.on.ca"),
    ("La pharmacie", "Les pharmaciens de l'Ontario traitent 27 affections mineures ; gratuit avec la carte santé de l'Ontario, "
     "à ses frais pour un visiteur. Urgence : 911.", "ontario.ca/page/pharmacies"),
    ("Le train de Montréal", "VIA Rail, environ 5 h 20, arrivée à Union Station.", "viarail.ca"),
]

# L'audition : les choix, PRIS en l'absence de Daniel (« prends les décisions »).
ROLES = [
    ("mots", "Les mots", "Elle dit chaque mot et chaque phrase des planches : la voix qu'on entend le plus.",
     ["clara", "ava"], "clara",
     "Clara : la seule voix du Canada, et une voix neurale, donc stable d'un tirage à l'autre (la HD ne l'est pas). "
     "Ava (États-Unis, HD) est plus naturelle ; on la garde en réserve si Clara vous paraît raide."),
    ("comptoir", "Les gens au comptoir", "L'employé de la réception, le guichetier, le serveur.",
     ["liam", "andrew"], "liam+andrew",
     "Les deux : Liam (Canada) au palier normal, Andrew (HD) quand il faut une deuxième voix d'homme."),
    ("torontoise", "La Torontoise qui revient", "La connaissance du café : il lui faut des émotions (contente, surprise, taquine).",
     ["harper", "olivia"], "harper",
     "Harper : une voix MAI-Voice-2 à émotions, comme Marta à Compostelle ; plus chaleureuse qu'Olivia à la même phrase."),
    ("accents", "Les accents de Toronto (palier 3)", "Les gens de la ville au palier « rapide, avec l'accent ».",
     ["aarti", "arjun", "rosa", "sam", "ezinne", "ollie", "connor"], "aarti+arjun+rosa+sam+ezinne",
     "Cinq accents : l'Inde (Aarti, Arjun), les Philippines (Rosa), Hong Kong (Sam), le Nigeria (Ezinne) — les communautés "
     "nombreuses à Toronto. Ollie (Angleterre) et Connor (Irlande) restent en réserve. Il n'existe chez Azure aucune "
     "voix de la Jamaïque ni de Trinité."),
]
NOMS_VOIX = {"clara": "Clara · Canada", "ava": "Ava · États-Unis, HD", "liam": "Liam · Canada",
             "andrew": "Andrew · États-Unis, HD", "harper": "Harper · MAI-Voice-2, à émotions",
             "olivia": "Olivia · MAI-Voice-2, à émotions", "aarti": "Aarti · Inde, HD", "arjun": "Arjun · Inde, HD",
             "rosa": "Rosa · Philippines", "sam": "Sam · Hong Kong", "ezinne": "Ezinne · Nigeria",
             "ollie": "Ollie · Angleterre, HD", "connor": "Connor · Irlande"}

TEMOINS = [("streetcar", "Le tramway", "Un véhicule qui porte d'ordinaire un numéro de ligne et un logo : le bandeau doit rester vide."),
           ("terminal", "Le terminal de paiement", "Un écran qui porte d'ordinaire des chiffres : il doit rester gris et vide."),
           ("peameal", "Le sandwich au bacon de dos", "Une matière difficile (la chapelure de maïs, les tranches empilées) : il doit se reconnaître.")]


def img(e):
    ident, _, mot, _, dessin, _ = e
    if dessin == "croquis" and (CROQUIS / f"{ident}.jpg").exists():
        return f'<img class="img" src="/assets/interactive/toronto/croquis/{ident}.jpg" alt="{E(mot)}" loading="lazy">'
    if dessin == "croquis":
        return '<div class="img attente">croquis<br>à venir</div>'
    if dessin.startswith("picto:"):
        return '<div class="img attente">dessin<br>en SVG</div>'
    return '<div class="img rien">à l\'oreille</div>'


def carte(e):
    ident, _, mot, fr, dessin, note = e
    piege = note.startswith("PIÈGE")
    ph = ""
    if piege:
        p = LX.PIEGES[ident]
        ph = f'<p class="phrase">« {E(p[0])} »<br><span>{E(p[1])}</span></p>'
    return (f'<article class="mot{" piege" if piege else ""}" data-id="{ident}">{img(e)}'
            f'<p class="ici" lang="en">{E(mot)}</p><p class="autre">{E(fr)}</p>'
            + (f'<p class="note">{E(note)}</p>' if note else "") + ph
            + '<div class="choix"><button type="button" data-v="garder" aria-pressed="false">Garder</button>'
              '<button type="button" data-v="retirer" aria-pressed="false">Retirer</button>'
              '<button type="button" data-v="douteux" aria-pressed="false">À revoir</button></div></article>')


def option(groupe, val, titre, texte, decide):
    return (f'<button type="button" class="opt" data-g="{groupe}" data-v="{val}" data-defaut="{1 if decide else 0}" aria-pressed="false">'
            f'<b>{E(titre)}</b>{" <span class=tag>décidé</span>" if decide else ""}'
            f'<span class="det">{texte}</span></button>')


CSS = """
.doc.large{max-width:1180px}
.grille{display:grid;grid-template-columns:repeat(auto-fill,minmax(168px,1fr));gap:12px}
.mot{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:4px}
.mot.piege{border-color:#C8692A;box-shadow:inset 0 0 0 1px #C8692A}
.mot .img{width:100%;aspect-ratio:1;object-fit:contain;background:#fff;border-radius:8px}
.mot .attente,.mot .rien{display:grid;place-items:center;text-align:center;font-size:12px;color:var(--muted);background:var(--sunken)}
.mot .rien{aspect-ratio:3}
.mot .ici{margin:4px 0 0;font-weight:800;color:var(--ink);font-size:15px}
.mot .autre{margin:0;font-size:13px;color:var(--muted)}
.mot .note{margin:2px 0 0;font-size:12.5px;line-height:1.35;color:var(--body)}
.mot.piege .note{color:#a5521a}
.mot .phrase{margin:2px 0 0;font-size:12.5px;line-height:1.35;font-style:italic;color:var(--body)}
.mot .phrase span{font-style:normal;color:var(--muted)}
.choix{display:flex;gap:4px;margin-top:auto;padding-top:6px}
.choix button{flex:1;font:inherit;font-size:12px;font-weight:700;padding:6px 2px;min-height:36px;border-radius:8px;border:1px solid var(--line-fort);background:var(--sunken);color:var(--body);cursor:pointer}
.choix button[aria-pressed=true][data-v=garder]{background:#DCF2E6;border-color:#0A8F5B;color:#0b3d27}
.choix button[aria-pressed=true][data-v=retirer]{background:#FBE4E0;border-color:#B42318;color:#5c130c}
.choix button[aria-pressed=true][data-v=douteux]{background:#FBEEDC;border-color:#B45309;color:#5a2c05}
.planche h2 .compte{font-size:13px;font-weight:700;color:var(--muted);margin-left:8px}
.opts2{display:grid;gap:10px}
.opt{display:block;text-align:left;font:inherit;background:var(--card);border:1px solid var(--line-fort);border-radius:12px;padding:12px 14px;cursor:pointer;color:var(--body)}
.opt[aria-pressed=true]{border-color:#0A8F5B;box-shadow:inset 0 0 0 2px #0A8F5B}
.opt .det{display:block;font-size:14px;color:var(--muted);margin-top:4px}
.opt .tag{font-size:12px;color:#0A8F5B;font-weight:800}
.role{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px;margin:12px 0}
.role h3{margin:0 0 4px;font-size:17px}
.role .pq{margin:0 0 10px;color:var(--muted);font-size:14px}
.ecoute{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
.ecoute .v{border:1px solid var(--line);border-radius:10px;padding:10px;background:var(--sunken)}
.ecoute .v.pris{border-color:#0A8F5B;box-shadow:inset 0 0 0 2px #0A8F5B}
.ecoute .v b{display:block;color:var(--ink)} .ecoute .v .pris-tag{font-size:12px;font-weight:800;color:#0A8F5B}
.ecoute audio{width:100%;height:36px;margin-top:6px}
.ecoute .ent{font-size:12px;color:var(--muted);margin:4px 0 0;line-height:1.35}
.temoins{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
.temoins figure{margin:0;background:var(--card);border:1px dashed var(--line-fort);border-radius:12px;padding:12px}
.temoins img{width:100%;aspect-ratio:1;object-fit:contain;background:#fff}
.temoins figcaption{font-size:14px;color:var(--body)} .temoins figcaption b{display:block;color:var(--ink)}
.temoins .vide{aspect-ratio:1;display:grid;place-items:center;text-align:center;color:var(--muted);font-size:13px;background:var(--sunken);border-radius:8px;margin-bottom:8px;padding:10px}
textarea{width:100%;font:inherit;font-size:15px;padding:10px;border-radius:10px;border:1px solid var(--line-fort);background:var(--card);color:var(--ink);box-sizing:border-box}
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
@media (max-width:640px){.grille{grid-template-columns:repeat(2,1fr)}table.cmp{font-size:14px}table.cmp td{min-width:8em}}
"""


def main():
    LX.verifier()
    g = LX.par_planche()
    n = len(LX.LEXIQUE)
    n_c = sum(1 for e in LX.LEXIQUE if e[4] == "croquis")
    n_p = len(LX.PIEGES)
    entendu = {}
    if (VOIX / "retranscription.json").exists():
        entendu = json.loads((VOIX / "retranscription.json").read_text(encoding="utf-8"))
    n_v = len(list(VOIX.glob("*.mp3"))) if VOIX.exists() else 0

    tete = TETE_DE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Une semaine à Toronto — le cadrage</title>", tete)
    tete = tete.replace("</style>", CSS + "</style>", 1)

    obj = "".join(f"<tr><td><b>{o}</b></td><td><b>{E(v)}</b> — {E(c)}</td><td>{E(cr)}</td></tr>" for o, v, c, cr in OBJECTIFS)
    ali = "".join(f"<tr><td><b>{o}</b></td><td>{E(x)}</td><td>{E(t)}</td><td>{E(s)}</td></tr>" for o, x, t, s in ALIGNEMENT)
    faits = "".join(f"<tr><td><b>{E(q)}</b></td><td>{E(v)}</td><td>{E(s)}</td></tr>" for q, v, s in FAITS)

    def bloc_role(cle, titre, quoi, voix, pris, pourquoi):
        cases = []
        for v in voix:
            sel = v in pris.split("+")
            ext = "".join(f'<audio controls preload="none" src="/assets/presentations/toronto/voix/{v}-{i}.mp3"></audio>'
                          f'<p class="ent">Entendu : « {E(entendu.get(f"{v}-{i}.mp3", "—"))} »</p>' for i in (1, 2))
            cases.append(f'<div class="v{" pris" if sel else ""}"><b>{E(NOMS_VOIX[v])}</b>'
                         + ('<span class="pris-tag">retenue</span>' if sel else "") + ext + "</div>")
        return (f'<div class="role"><h3>{E(titre)}</h3><p class="pq">{E(quoi)}</p><div class="ecoute">{"".join(cases)}</div>'
                f'<p style="margin:10px 0 0"><b>Décidé :</b> {E(pourquoi)}</p>'
                f'<div class="opts2" style="margin-top:8px">{option("voix-" + cle, "ok", "Ce choix me va", "", True)}'
                f'{option("voix-" + cle, "changer", "À changer", "Dites laquelle dans « Ce qui manque ».", False)}</div></div>')
    roles = "".join(bloc_role(*r) for r in ROLES)

    temoins = "".join(
        (f'<figure><img src="/assets/interactive/toronto/croquis/{i}.jpg" alt="{E(t)}">' if (CROQUIS / f"{i}.jpg").exists()
         else f'<figure><div class="vide">à dessiner<br>dès que le crédit Google est rechargé</div>')
        + f'<figcaption><b>{E(t)}</b>{E(d)}</figcaption></figure>' for i, t, d in TEMOINS)
    sections = "".join(
        f'<section class="planche" id="p-{k}"><h2>{E(t)} <span lang="en" class="compte">{E(en)} · {len(g[k])}</span></h2>'
        f'<div class="grille">{"".join(carte(e) for e in g[k])}</div></section>'
        for k, t, en in LX.PLANCHES)
    n_choix = 2 + len(ROLES)  # objectifs, nom, et une par rôle de voix

    corps = f"""<body>
<div class="doc large">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Une semaine à Toronto &middot; étape 0</p>
<h1>Le cadrage</h1>
<p class="chapeau">Le plan est tranché : vous avez pris toutes les recommandations le 1er octobre, puis vous m'avez laissé
les décisions du cadrage. <b>Chaque choix ci-dessous est donc déjà pris</b> (marqué « décidé ») ; un clic sur l'autre option
le renverse. Restent pour vous : écouter les voix, et passer les <b>{n} mots</b> un par un.</p>

<div class="chiffres">
  <div class="ch"><span class="n">{n}</span><span class="q">mots en {len(LX.PLANCHES)} planches</span></div>
  <div class="ch"><span class="n">{n_c}</span><span class="q">croquis à produire, ≈&nbsp;{n_c * 0.067:.0f}&nbsp;$</span></div>
  <div class="ch"><span class="n">{n_p}</span><span class="q">pièges, chacun dans une phrase de voyage</span></div>
  <div class="ch"><span class="n">{n_v}</span><span class="q">extraits d'audition, 13 voix</span></div>
</div>

<section class="premier">
  <h2>1 · Le public, l'écart, les objectifs</h2>
  <p><b>Le public</b> : des Québécois, souvent de 40 à 70 ans, qui partent quelques jours à Toronto (en train, en voiture
  ou en avion depuis Montréal ou Québec) et qui ont des restes d'anglais de l'école ou de la télé. Ils préparent leur
  voyage à la maison, sur leur téléphone, par séances de 15 minutes, puis ils s'en servent sur place.</p>
  <p><b>L'écart</b> : ils savent dire « Can I have a coffee? », mais ils figent quand on leur répond vite (« For here or
  to go? Anything else? That's six twenty-five »). Ils hochent la tête sans avoir compris. Ils sont surpris par le total
  au terminal. Et ils ne savent pas quoi répondre au petit bavardage.</p>
  <table class="cmp"><thead><tr><th></th><th>Objectif — condition</th><th>Critère</th></tr></thead><tbody>{obj}</tbody></table>
  <p style="margin-top:14px"><b>L'alignement</b> : chaque objectif a son exercice, sa question de test et sa situation.</p>
  <table class="cmp"><thead><tr><th></th><th>Exercice</th><th>Test « Prêt à partir ? »</th><th>Situation jouée</th></tr></thead><tbody>{ali}</tbody></table>
  <div class="reserve"><p><strong>L'éliminatoire est dit avant</strong>, en une phrase affichée au début de la série, du
  test et du restaurant : « Une allergie se dit avant de commander. Si la réponse n'est pas claire, on ne mange pas le
  plat. » Chaque série garde un contre-exemple, où la question du serveur ne porte pas sur l'allergie.</p></div>
  <div class="opts2" style="margin-top:12px">
    {option("objectifs", "oui", "Ces objectifs", "On aligne les exercices et le test dessus.", True)}
    {option("objectifs", "ajuster", "À ajuster", "Dites quoi dans « Ce qui manque », en bas.", False)}
  </div>
</section>

<section>
  <h2>2 · Le nom</h2>
  <div class="these"><p class="cle"><b>Une semaine à Toronto</b> — cherché le 1er octobre, nom exact entre guillemets.</p></div>
  <p>Aucune application, aucun livre, cours ou guide de ce nom : l'expression ne paraît que dans des textes de voyagistes
  et de blogues. Rien non plus sous « A week in Toronto ». Ce n'est pas une recherche de marque de commerce, et les
  boutiques d'applications n'ont pas été fouillées.</p>
  <div class="opts2">
    {option("nom", "garder", "Une semaine à Toronto", "Il dit le voyage et sa durée, comme « En route vers Compostelle ».", True)}
    {option("nom", "autre", "Un autre nom", "Dites lequel en bas.", False)}
  </div>
</section>

<section>
  <h2>3 · Les faits de la ville, vérifiés le 1er octobre 2026</h2>
  <p>Ce que la trousse dira : tarifs, heures, usages. Chaque fait a sa source ; ils seront revérifiés avant le pilote, et
  la poche les datera.</p>
  <table class="cmp"><thead><tr><th>Quoi</th><th>Ce qu'on dira</th><th>Source</th></tr></thead><tbody>{faits}</tbody></table>
  <p style="margin-top:10px"><b>Trois changements par rapport au plan</b>, déjà reportés dans le plan et dans le lexique :
  le pourboire est de <b>18 à 20 %</b> (et non 15 à 20) ; le passage coûte <b>3,30 $</b> en touchant sa carte ; et l'hiver,
  le traversier ne va qu'à l'île Ward. La situation 9 (les îles) se jouera donc « au dernier traversier de l'automne ».</p>
</section>

<section>
  <h2>4 · Les voix</h2>
  <p>Le Canada n'a que <b>deux voix</b> chez Azure, Clara et Liam, et pas en HD. Voici les treize voix entendues, deux phrases
  chacune : des prix et des heures (« thirteen fifty », « quarter to eleven »), puis un nom québécois épelé (Tremblay).
  Sous chaque extrait, ce que la reconnaissance d'Azure en a compris : <b>les vingt-six tirages sont justes</b>. « Fairy »
  pour « ferry » et « for 12 » pour « 412 » sont des homophones, pas des fautes. L'épellation, elle, ne se juge qu'à
  l'oreille : c'est à vous.</p>
  {roles}
</section>

<section>
  <h2>5 · Le dessin</h2>
  <p>Le registre de Francœur et de Compostelle : trait noir égal, un aplat doux, fond blanc ; les lieux en vignettes 3:2
  de carnet de voyage, comme le chemin. Aucune enseigne, aucun numéro, aucune marque dans l'image. Trois témoins, choisis
  pour leurs risques :</p>
  <div class="temoins">{temoins}</div>
  <div class="reserve"><p><strong>Pas encore dessinés :</strong> le 1er octobre, Google refuse toujours (402, crédit épuisé).
  Les consignes sont écrites (<code>build/contenu/toronto/sujets.py</code>) ; il suffira de lancer
  <code>python3 build/toronto_croquis.py --temoins</code> une fois le crédit rechargé (0,20 $).</p></div>
</section>

<section>
  <h2>6 · Le lexique, mot par mot</h2>
  <p>En gras, l'anglais du Canada qu'on entendra ; dessous, le français du Québec. Les pièges sont encadrés, avec leur
  phrase de voyage. « À l'oreille » : une formule, sans image.
  <button type="button" class="btn-export" id="toutGarder" style="margin-left:8px">Tout garder ce qui n'est pas marqué</button></p>
  {sections}
</section>

<section>
  <h2>Ce qui manque</h2>
  <p>Des mots, des situations que vous avez vécues à Toronto, une voix à changer :</p>
  <textarea id="manque" rows="5"></textarea>
  <p style="margin-top:1.2rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied"><p>Produite par <code>build/toronto_etape0.py</code> — ne pas l'éditer. Lexique :
<code>build/contenu/toronto/lexique.py</code>. Audition : <code>build/toronto_voix_audition.py</code>.</p></div>
</div>
<script>
(function(){{
  var CLE='toronto-etape0', s={{mots:{{}},choix:{{}},manque:''}};
  try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.mots)s=l;}}catch(e){{}}
  // Les décisions prises en l'absence de Daniel sont cochées d'office ; un clic les renverse.
  document.querySelectorAll('.opt[data-defaut="1"]').forEach(function(b){{if(!s.choix[b.dataset.g])s.choix[b.dataset.g]=b.dataset.v;}});
  function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
  var N={n}, NC={n_choix};
  function peindre(){{
    document.querySelectorAll('.mot').forEach(function(m){{var v=s.mots[m.dataset.id];
      m.querySelectorAll('.choix button').forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.v===v);}});}});
    document.querySelectorAll('.opt').forEach(function(b){{b.setAttribute('aria-pressed',s.choix[b.dataset.g]===b.dataset.v);}});
    document.getElementById('etat').textContent=Object.keys(s.mots).length+' mots marqués sur '+N+' · '+Object.keys(s.choix).length+' choix sur '+NC;
  }}
  document.addEventListener('click',function(e){{
    var b=e.target.closest('.choix button');
    if(b){{var id=b.closest('.mot').dataset.id; if(s.mots[id]===b.dataset.v)delete s.mots[id]; else s.mots[id]=b.dataset.v; sv(); peindre(); return;}}
    var o=e.target.closest('.opt');
    if(o){{s.choix[o.dataset.g]=o.dataset.v; sv(); peindre();}}
  }});
  document.getElementById('toutGarder').onclick=function(){{document.querySelectorAll('.mot').forEach(function(m){{if(!s.mots[m.dataset.id])s.mots[m.dataset.id]='garder';}});sv();peindre();}};
  var t=document.getElementById('manque'); t.value=s.manque||''; t.oninput=function(){{s.manque=t.value;sv();}};
  document.getElementById('exporter').onclick=function(){{
    var r=[],d=[]; Object.keys(s.mots).forEach(function(k){{if(s.mots[k]==='retirer')r.push(k); if(s.mots[k]==='douteux')d.push(k);}});
    var out={{page:'toronto-etape0',date:new Date().toISOString().slice(0,10),choix:s.choix,
      gardes:Object.keys(s.mots).filter(function(k){{return s.mots[k]==='garder';}}).length,sur:N,retirer:r,a_revoir:d,manque:s.manque||''}};
    var txt=JSON.stringify(out,null,2),fin=function(){{document.getElementById('etat').textContent='Copié — à recoller dans la conversation.';}};
    if(navigator.clipboard)navigator.clipboard.writeText(txt).then(fin,function(){{prompt('Copiez :',txt);}});else prompt('Copiez :',txt);
  }};
  peindre();
}})();
</script>
</body></html>"""
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {n} mots, {n_c} croquis, {n_p} pièges, {n_v} extraits")


if __name__ == "__main__":
    main()
