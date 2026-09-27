#!/usr/bin/env python3
"""L'infographie du parcours d'apprentissage d'« En route vers Compostelle ».

    python3 build/compostelle_parcours.py   # → assets/presentations/compostelle-parcours.html

Demande de Daniel, 26 sept. 2026 : « une infographie qui m'explique la route à
suivre — comment se font les apprentissages ». Tout ce qui est compté (les
journées, leurs objectifs, les kilomètres, les objectifs du test) est relu dans
le contenu : rien n'est recopié à la main, pour que la page ne mente pas le jour
où une journée change.
"""
import html, math, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import compostelle_commun as C  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-parcours.html"
MEDIA = "../interactive/compostelle/"
E = html.escape

# Les sept temps d'une journée, dans l'ordre de l'application (TEMPS de
# compostelle_app.py). `phase` : découvrir · comprendre · agir.
TEMPS = [
    ("lieu", "Le lieu", "decouvrir", "Où je suis : l'histoire, ce qu'on y visite, les mots du tourisme — avec leur voix."),
    ("mots", "Les mots du jour", "decouvrir", "Des cartes dessinées. Je touche, j'entends ; la traduction reste cachée d'abord."),
    ("entends", "J'entends, je trouve", "decouvrir", "Un mot entendu, quatre images : je reconnais à l'oreille."),
    ("repond", "Ce qu'on me répond", "comprendre", "La personne du lieu répond à sa vitesse : que veut-elle dire ? Plus des rappels des jours passés."),
    ("scene", "La scène", "agir", "La situation jouée : j'écoute d'abord, je choisis ou je réponds à voix haute."),
    ("dire", "Je le dis", "agir", "Ce que je viens d'entendre, à moi de le dire au micro ; puis j'écoute le modèle."),
    ("soir", "Le soir, avec Marta", "agir", "Une conversation entre pèlerins. Marta se souvient de ce que j'ai dit la veille."),
]
TAMPON = ("repond", "dire", "scene", "soir")
PHASES = {
    "decouvrir": ("Découvrir", "je reçois"),
    "comprendre": ("Comprendre", "je reconnais ce qu'on me dit"),
    "agir": ("Agir", "je parle, je joue"),
}


def main():
    ET, TS = C.charger("etapes"), C.charger("test")
    etapes = ET.ETAPES
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — le parcours</title>", tete)
    tete = tete.replace("</head>", """<style>
:root{--fleche:#F2C230;--fleche-ink:#5C4400;--ph-decouvrir:var(--acier);--ph-decouvrir-bg:var(--acier-bg);
 --ph-comprendre:var(--decid);--ph-comprendre-bg:var(--decid-bg);--ph-agir:var(--fait);--ph-agir-bg:var(--fait-bg)}
.devise{font-size:21px;font-weight:800;color:var(--ink);line-height:1.35;margin:18px 0 6px}
.devise span{background:linear-gradient(transparent 62%,rgba(242,194,48,.45) 62%)}
.etape-num{display:inline-grid;place-items:center;width:30px;height:30px;border-radius:50%;background:var(--fleche);color:#2B2100;font-weight:900;font-size:15px;margin-right:10px;vertical-align:-6px}
section.bloc{margin-top:40px}
section.bloc>h2{display:flex;align-items:center}
.duo{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}
.carte{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px 18px}
.carte h3{margin:0 0 6px;font-size:17px;color:var(--ink)}
.carte p{margin:0;font-size:15px;line-height:1.45}
.carte .fleche{color:var(--muted);font-size:14px;margin-top:10px}
/* la journée : trois phases, sept temps */
.phases{display:flex;flex-direction:column;gap:0}
.phase{border-radius:12px;padding:14px;border:1px solid var(--line);display:grid;grid-template-columns:150px minmax(0,1fr);gap:14px;align-items:start}
.phase+.phase{margin-top:26px;position:relative}
.phase+.phase::before{content:"";position:absolute;left:50%;top:-22px;width:0;height:0;border-left:9px solid transparent;border-right:9px solid transparent;border-top:12px solid var(--fleche)}
.phase>header{font-size:13px;font-weight:900;letter-spacing:.08em;text-transform:uppercase}
.phase>header small{display:block;text-transform:none;letter-spacing:0;font-weight:700;font-size:14px;opacity:.85;margin-top:2px}
.phase.decouvrir{background:var(--ph-decouvrir-bg)}.phase.decouvrir>header{color:var(--ph-decouvrir)}
.phase.comprendre{background:var(--ph-comprendre-bg)}.phase.comprendre>header{color:var(--ph-comprendre)}
.phase.agir{background:var(--ph-agir-bg)}.phase.agir>header{color:var(--ph-agir)}
.temps{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:8px}
.t{background:var(--card);border-radius:10px;padding:10px 11px;border:1px solid var(--line);position:relative}
.t b{display:block;font-size:14.5px;color:var(--ink);line-height:1.25}
.t .n{font-size:11px;font-weight:900;color:var(--muted)}
.t p{font-size:13.5px;line-height:1.35;margin:4px 0 0;color:var(--body)}
.t .sceau{position:absolute;top:8px;right:8px;width:18px;height:18px;border-radius:50%;border:2px solid #B3261E;display:grid;place-items:center;color:#B3261E;font-size:10px;font-weight:900}
.apres{display:flex;gap:10px;align-items:center;margin-top:12px;flex-wrap:wrap}
.tampon{display:flex;gap:12px;align-items:center;background:var(--card);border:1px dashed #B3261E;border-radius:12px;padding:12px 14px;flex:1 1 320px}
.tampon svg{flex:none}
.bonus{flex:1 1 260px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px;font-size:14.5px}
/* le chemin */
.chemin{position:relative;margin:6px 0 0;padding:0;list-style:none}
.chemin::before{content:"";position:absolute;left:47px;top:10px;bottom:10px;border-left:3px dotted var(--fleche)}
.chemin li{display:grid;grid-template-columns:96px minmax(0,1fr);gap:14px;align-items:start;padding:8px 0;position:relative}
.chemin .img{width:96px;height:64px;border-radius:8px;object-fit:cover;background:#fff;border:2px solid var(--card);box-shadow:0 0 0 1px var(--line);position:relative;z-index:1}
.chemin .jour{font-size:12px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.chemin h3{margin:1px 0 3px;font-size:17px;color:var(--ink)}
.chemin h3 small{font-weight:700;color:var(--muted);font-size:13px}
.chemin p{margin:0;font-size:14.5px;line-height:1.4}
.chemin .elim{display:inline-block;margin-top:6px;font-size:12px;font-weight:900;color:var(--loi);background:var(--loi-bg);border-radius:99px;padding:3px 10px}
.chemin .rappel{display:inline-block;margin-top:6px;font-size:12px;font-weight:800;color:var(--fleche-ink);background:#FFF6D6;border-radius:99px;padding:3px 10px}
.progression{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:14px 0 4px}
.progression div{background:var(--sunken);border-radius:10px;padding:10px 12px;font-size:14px}
.progression b{display:block;color:var(--ink)}
/* l'arrivée */
.verdicts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:12px}
.verdicts div{border-radius:10px;padding:10px 12px;font-size:14px;background:var(--card);border:1px solid var(--line)}
.verdicts b{display:block;font-size:16px}
.v1 b{color:var(--fait)}.v2 b{color:var(--decid)}.v3 b{color:var(--loi)}
.objectifs{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0;padding:0;list-style:none}
.objectifs li{background:var(--sunken);border-radius:99px;padding:5px 12px;font-size:14px}
.objectifs li b{color:var(--ink)}
.principes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.principes .carte h3::before{content:"➜ ";color:var(--fleche)}
@media (max-width:760px){
 .phase{grid-template-columns:1fr;gap:10px}
 .duo,.principes{grid-template-columns:1fr}
 .verdicts,.progression{grid-template-columns:1fr}
 .chemin::before{left:35px}
 .chemin li{grid-template-columns:72px minmax(0,1fr);gap:12px}
 .chemin .img{width:72px;height:54px}
}
</style>
</head>""")

    def temps_html(ph):
        out = []
        for i, (k, nom, p, quoi) in enumerate(TEMPS, 1):
            if p != ph:
                continue
            sceau = '<span class="sceau" title="compte pour le tampon">✓</span>' if k in TAMPON else ""
            out.append(f'<div class="t">{sceau}<span class="n">{i}</span><b>{E(nom)}</b><p>{E(quoi)}</p></div>')
        return "".join(out)

    phases = "".join(
        f'<div class="phase {ph}"><header>{E(PHASES[ph][0])}<small>{E(PHASES[ph][1])}</small></header>'
        f'<div class="temps">{temps_html(ph)}</div></div>' for ph in PHASES)

    li = []
    leon = next(i for i, e in enumerate(etapes) if e.get("eliminatoire"))
    avant, total_jours = 0, 0
    for i, e in enumerate(etapes):
        j = max(1, math.ceil((e["km"] - avant) / 25 - 0.2)); avant = e["km"]; total_jours += j
        marque = ""
        if e.get("eliminatoire"):
            marque = '<span class="elim">Éliminatoire : l\'allergie</span>'
        elif i > leon:
            marque = '<span class="rappel">+ rappel de l\'allergie</span>'
        elif i >= 1:
            marque = '<span class="rappel">+ rappels des jours passés</span>'
        li.append(
            f'<li><img class="img" src="{MEDIA}etapes/{E(e["img"])}.jpg" alt="" loading="lazy">'
            f'<div><span class="jour">Halte {e["n"]} · km {e["km"]} · {j} jour{"s" if j > 1 else ""} de marche</span>'
            f'<h3>{E(e["lieu"])} <small>· {E(e["scene"]["titre"])}</small></h3>'
            f'<p>{E(e["objectif"])}</p>{marque}</div></li>')

    PR = C.charger("preparation")
    prep_cartes = "".join(f'<div class="carte"><h3>{i}. {E(x["titre"])}</h3><p>{E(PR.OBJECTIFS[x["obj"]])}</p></div>'
                          for i, x in enumerate(PR.SEANCES, 1))
    objectifs = "".join(f"<li><b>{k}</b> {E(v)}</li>" for k, v in TS.OBJECTIFS.items())
    n_items = len(next(iter(TS.FORMES.values()))) if isinstance(TS.FORMES, dict) else len(TS.FORMES[0])
    n_formes = len(TS.FORMES)
    km = etapes[-1]["km"]

    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>En route vers Compostelle &mdash; comment on apprend</h1>
<p class="chapeau">L'application suit le Camino francés : <strong>{len(etapes)} haltes</strong>, de Roncesvalles à Santiago
({km} km, environ {total_jours} jours de marche). Chaque halte est une situation dont le pèlerin aura besoin ce soir-là, et chacune se déroule de la même façon,
en sept temps. Le pèlerin avance de lieu en lieu ; ce qui a été appris revient plus loin, sans prévenir.</p>
<p class="devise"><span>Comprendre avant de dire. Dire avant de jouer. Jouer avant d'y aller seul.</span></p>

<section class="bloc">
  <h2><span class="etape-num">1</span>Avant de partir : deux réglages</h2>
  <div class="duo">
    <div class="carte"><h3>Pèlerin ou pèlerine</h3><p>L'espagnol accorde : <i>cansado</i>, <i>cansada</i> ; <i>alérgico</i>,
      <i>alérgica</i>. Chaque modèle, chaque phrase à dire, chaque réponse attendue est au bon genre.</p></div>
    <div class="carte"><h3>Mon allergie, parmi huit</h3><p>Noix, arachides, gluten, lait, œufs, poisson, fruits de mer,
      sésame. Elle traverse tout : la scène de León, le comptoir de Pamplona, la trousse, le test, et un son par allergène.</p>
      <p class="fleche">➜ Le même parcours, mais c'est <b>son</b> allergie qu'on apprend à dire.</p></div>
  </div>
</section>

<section class="bloc">
  <h2><span class="etape-num">1b</span>À la maison : « Avant de partir »</h2>
  <p>Huit séances de quinze minutes, dans les semaines qui précèdent le départ — conseillées, jamais obligatoires. On y apprend
  <b>les outils</b> qu'on emploiera ensuite en situation :</p>
  <div class="duo">{prep_cartes}</div>
  <p style="font-size:14.5px;color:var(--muted);margin-top:8px">Chaque séance : j'écoute (les phrases et les mots, avec leur voix), je
  reconnais (on entend, on choisit, chaque erreur dit pourquoi), je le dis (au micro, puis le modèle). Un encadré « la mécanique » donne
  la seule forme qui sert — jamais la conjugaison entière. À la fin, le test « Prêt à partir ? » situe, deux formes de dix questions.</p>
</section>

<section class="bloc">
  <h2><span class="etape-num">2</span>Une halte : trois mouvements, sept temps</h2>
  <p>On reçoit, on reconnaît, puis on agit. L'ordre ne change jamais : le pèlerin sait toujours où il en est.</p>
  <div class="phases">{phases}</div>
  <div class="apres">
    <div class="tampon">
      <svg width="54" height="54" viewBox="0 0 54 54" aria-hidden="true"><circle cx="27" cy="27" r="24" fill="none" stroke="#B3261E" stroke-width="3"/><circle cx="27" cy="27" r="19" fill="none" stroke="#B3261E" stroke-width="1.2" stroke-dasharray="2 3"/><path d="M27 14c-6 0-10 5-10 10 0 7 10 16 10 16s10-9 10-16c0-5-4-10-10-10z" fill="#B3261E" opacity=".85"/></svg>
      <div><b>Le tampon sur la credencial</b><br><span style="font-size:14.5px">Il se gagne quand les quatre temps marqués
      <span style="color:#B3261E;font-weight:900">✓</span> sont faits : comprendre, jouer la scène, dire, parler le soir. Lire et écouter
      ne suffisent pas.</span></div>
    </div>
    <div class="bonus"><b>Et puis, librement</b><br>« Parler librement » : la même personne, au même endroit, mais qui répond
      à ce que le pèlerin dit vraiment (l'assistant). Trois vitesses, micro ou clavier, un bilan en français. Avec un code de groupe.</div>
  </div>
</section>

<section class="bloc">
  <h2><span class="etape-num">3</span>Le chemin : dix haltes, du plus urgent au plus riche</h2>
  <div class="progression">
    <div><b>D'abord survivre</b>un lit, un repas, son chemin, une pharmacie (jours 1 à 4)</div>
    <div><b>Puis se débrouiller</b>« complet », le téléphone, l'allergie qui ne pardonne pas (jours 5 à 7)</div>
    <div><b>Enfin, parler</b>la météo, le marché, le bureau du pèlerin, et les autres (jours 8 à 10)</div>
  </div>
  <ol class="chemin">{"".join(li)}</ol>
  <p style="font-size:14.5px;color:var(--muted);margin-top:8px">Les rappels : dans « Ce qu'on me répond », une ou deux
  réponses d'une halte passée reviennent, mêlées aux nouvelles. Après León, c'est l'allergie qui revient chaque jour —
  l'erreur qui coûte le plus est aussi celle qu'on revoit le plus.</p>
</section>

<section class="bloc">
  <h2><span class="etape-num">4</span>L'arrivée : « Suis-je prêt ? »</h2>
  <div class="carte">
    <p>Un quart d'heure, <b>{n_items} situations nouvelles</b> — jamais celles des haltes. {n_formes} formes équivalentes, tirées au hasard, pour qu'une reprise ne soit pas une récitation. Cinq objectifs :</p>
    <ul class="objectifs">{objectifs}</ul>
    <p style="margin-top:12px">L'allergie y est <b>éliminatoire</b>, et le test le dit avant de commencer. Il situe, il ne note pas :</p>
    <div class="verdicts">
      <div class="v1"><b>Solide</b>tout est juste pour cet objectif</div>
      <div class="v2"><b>En route</b>au moins une réponse juste</div>
      <div class="v3"><b>À reprendre</b>aucune réponse juste</div>
    </div>
    <p style="margin-top:12px">Au bout : une <b>Compostela</b> à imprimer, présentée pour ce qu'elle est — un souvenir.</p>
  </div>
</section>

<section class="bloc">
  <h2><span class="etape-num">5</span>Toujours dans la trousse</h2>
  <div class="duo">
    <div class="carte"><h3>Ma trousse, hors ligne</h3><p>Les phrases du chemin en onze rubriques, les urgences (112),
      la carte d'allergie en grand à montrer, « Me présenter ». « Préparer pour le chemin » met tout dans le téléphone :
      on marche sans réseau.</p></div>
    <div class="carte"><h3>Les mots et les faux amis</h3><p>Tous les mots en onze planches, chacun avec son dessin et sa voix.
      Les faux amis dans leur phrase : <i>constipado</i> (enrhumé), <i>embarazada</i> (enceinte), <i>la comida</i> (le dîner).</p></div>
  </div>
</section>

<section class="bloc">
  <h2><span class="etape-num">6</span>Les règles qui font que ça marche</h2>
  <div class="principes">
    <div class="carte"><h3>L'oreille d'abord</h3><p>Les scènes s'écoutent avant de se lire : le texte reste fermé jusqu'à ce qu'on le demande.
      Sur le chemin, personne n'affiche ses répliques.</p></div>
    <div class="carte"><h3>On essaie avant le modèle</h3><p>« Je le dis » exige une tentative avant de faire entendre la bonne phrase ;
      la phrase d'allergie ne compte que dite juste.</p></div>
    <div class="carte"><h3>Chaque erreur a sa réponse</h3><p>Aucun « Bravo ! » vide : chaque mauvais choix dit ce qu'il aurait
      fait comprendre, et ce qui se serait passé.</p></div>
    <div class="carte"><h3>Rien ne quitte le téléphone</h3><p>Aucun compte, aucune connexion : l'avancement vit dans l'appareil.
      Seul « Parler librement » passe par le serveur, avec un code.</p></div>
  </div>
</section>
</div>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {len(etapes)} haltes")


if __name__ == "__main__":
    main()
