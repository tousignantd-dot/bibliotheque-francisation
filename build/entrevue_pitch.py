#!/usr/bin/env python3
"""Le pitch de vente du prototype 07 — « L'entrevue, vue d'en face ».

POURQUOI UN PITCH AVANT LA PRODUCTION. La compétence le dit en cinq phases :
brief, cadrage, partis pris, témoin, production. On chiffre et on vend AVANT de
fabriquer, parce que c'est le seul moment où couper ne coûte rien.

LE FAIT QUI COMMANDE, ET IL EST DÉSAGRÉABLE. Depuis le 1er juillet 2026, la
francisation en milieu de travail est livrée GRATUITEMENT par 32 partenaires
publics mandatés. Vendre des cours de français à un employeur, c'est arriver
deuxième. Un pitch qui ne dit pas ça en premier se fait démolir à la première
rencontre par quelqu'un qui le sait.

Mais le relevé de marché du 31 août nomme aussi CINQ FAILLES du programme
public — et cette pièce-ci tombe dans les cinq. C'est là qu'est l'argument, et
nulle part ailleurs.

    python3 build/entrevue_pitch.py
"""
import pathlib

ICI = pathlib.Path(__file__).resolve().parent.parent
SRC = ICI / "assets" / "presentations" / "loi-25-entreprises.html"
DEST = ICI / "assets" / "presentations" / "entrevue-pitch.html"


def jetons():
    """Les jetons viennent d'une page voisine du classeur, jamais recopiés."""
    s = SRC.read_text(encoding="utf-8")
    d = s.index(":root{")
    bloc = s[d:s.index("*{", d)].rstrip()
    for j in ("--ink:", "--acier:", "--risq:", "--ground:"):
        if j not in bloc:
            raise SystemExit(f"les jetons de {SRC.name} n'ont plus la forme attendue : {j}")
    return bloc


# ── LES CINQ FAILLES, RELEVÉES LE 31 AOÛT 2026 ─────────────────────────────
# Chacune est une condition du programme public gratuit. Elles ne sont pas des
# défauts : ce sont les bornes de son mandat. Et chaque borne est un endroit
# où quelqu'un a un besoin que personne ne sert.
FAILLES = [
 ("Pas le poste",
  "Français <b>général</b>, niveaux 0 à 7 de l'Échelle québécoise. Le programme "
  "n'enseigne pas à passer une entrevue chez un manufacturier.",
  "La pièce ne travaille qu'un poste, et elle le nomme : journalier, quart de soir, "
  "charges de vingt kilos. Ce que le programme public ne peut pas faire par mandat."),
 ("40 heures à libérer",
  "Quatre heures par semaine, dix semaines, libérées et payées par l'employeur.",
  "<b>Huit minutes</b>, seul, sans formateur, sur la machine qu'on a. Aucune heure "
  "à libérer, donc aucune permission à demander."),
 ("Six personnes du même niveau",
  "Groupes d'au moins six travailleurs au même stade — la condition qui bloque le "
  "plus d'entreprises.",
  "Elle se joue à une personne. Le niveau de chacun n'a pas à être le même, "
  "puisqu'elle ne mesure pas un niveau."),
 ("À distance et inter-entreprises",
  "« Généralement à distance », des travailleurs de plusieurs employeurs mélangés.",
  "Hors ligne, sans compte et sans facture. Elle se transporte dans un courriel "
  "et s'ouvre sur un portable de plancher."),
 ("Rien au-dessus du niveau 8",
  "Le programme s'arrête là où commence l'employabilité réelle.",
  "Elle ne mesure pas une langue, elle mesure un <b>effet</b> : ce qui est arrivé "
  "chez l'autre, et quand. Un candidat parfaitement francisé peut y échouer."),
]

# ── LES OBJECTIONS, ET CE QU'ON RÉPOND ─────────────────────────────────────
# On les écrit soi-même, avant que l'acheteur les trouve. Une objection qu'on
# a nommée le premier cesse d'être une attaque.
OBJECTIONS = [
 ("« Vous jugez l'accent des immigrants. »",
  "Non, et ce n'est pas une politesse : c'est vérifiable dans le code. Aucun motif "
  "ne teste une forme correcte. « J'ai travailler deux ans dans usine » remplit "
  "exactement la même ligne que « j'ai travaillé deux ans en usine ». Le seul "
  "jugement porté est : le fait est-il arrivé, et à quel moment. "
  "<b>C'est la seule position défendable devant un comité, et il faut la construire "
  "avant de la promettre.</b>"),
 ("« Quarante mots d'attention, c'est arbitraire. »",
  "Oui. Et le chiffre est <b>affiché dans la pièce</b> plutôt que caché, justement "
  "pour qu'il soit discutable. Il ne prétend pas mesurer une attention réelle : il "
  "rend visible une chose que tout le monde sait et que personne ne montre — "
  "qu'elle s'épuise, et avant la fin de votre réponse."),
 ("« Un chatbot ferait la même chose. »",
  "Un modèle de langue reformule, encourage et complète. Il donnerait deux fiches "
  "différentes à deux personnes qui disent la même chose, et il détruirait la mesure "
  "en trois répliques. Ici le recruteur est un jeu de faits cherchés et de motifs "
  "écrits à la main — même parti pris que le prototype 05, et pour les mêmes raisons."),
 ("« Ça se vend combien ? »",
  "Aucune des quatre écoles privées vérifiées ne publie de tarif. On n'en met pas "
  "sur le dépliant. Ce qui se chiffre, c'est le coût de production : "
  "<b>trois jours</b>, et la plomberie orale existe déjà."),
]

GABARIT = r"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>L'entrevue, vue d'en face — le pitch</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
/*§JETONS§*/
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
 font-family:"Inter",ui-sans-serif,system-ui,sans-serif;line-height:1.6}
.enrobe{max-width:52rem;margin:0 auto;padding:3rem 1.5rem 5rem}
.eyebrow{font-size:.72rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;
 color:var(--acier);margin:0}
h1{font-size:2.1rem;font-weight:800;letter-spacing:-.028em;margin:.3rem 0 .8rem;color:var(--ink)}
.sous{font-size:1.05rem;color:var(--body);margin:0 0 2rem}
h2{font-size:1.3rem;font-weight:700;letter-spacing:-.02em;color:var(--ink);
 margin:2.6rem 0 .6rem;padding-top:1.4rem;border-top:1px solid var(--line)}
h3{font-size:1rem;font-weight:700;color:var(--ink);margin:1.4rem 0 .3rem}
p{margin:.6rem 0}
.mur{background:var(--risq-bg);border-left:3px solid var(--risq);padding:1rem 1.2rem;margin:1.2rem 0}
.mur b{color:var(--risq)}
.bon{background:var(--ok-bg);border-left:3px solid var(--ok);padding:1rem 1.2rem;margin:1.2rem 0}
.faille{background:var(--card);border:1px solid var(--line);margin:.8rem 0;padding:1rem 1.2rem}
.faille .no{font-family:var(--mono);font-size:.72rem;color:var(--muted)}
.faille h3{margin:.1rem 0 .4rem}
.faille .prog{color:var(--muted);font-size:.92rem;margin:.2rem 0 .7rem}
.faille .nous{color:var(--ink);font-size:.95rem;margin:0;padding-left:.9rem;
 border-left:2px solid var(--acier)}
.demo{background:var(--card);border:1px solid var(--line-fort);padding:1.2rem 1.4rem;margin:1.2rem 0}
.demo ol{margin:.4rem 0;padding-left:1.2rem}
.demo li{margin:.45rem 0}
.demo .coup{color:var(--risq);font-weight:700}
.obj{border-bottom:1px solid var(--line);padding:1rem 0}
.obj:last-child{border-bottom:0}
.obj .q{font-weight:700;color:var(--ink);margin:0 0 .3rem}
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(9rem,1fr));gap:1px;
 background:var(--line);border:1px solid var(--line);margin:1.2rem 0}
.chiffres div{background:var(--card);padding:.9rem 1rem}
.chiffres dt{font-size:.68rem;font-weight:700;letter-spacing:.11em;text-transform:uppercase;
 color:var(--muted);margin:0 0 .25rem}
.chiffres dd{margin:0;font-size:1.5rem;font-weight:700;color:var(--ink);font-variant-numeric:tabular-nums}
.chiffres dd small{font-size:.78rem;font-weight:500;color:var(--muted)}
.reste{background:var(--dec-bg);border-left:3px solid var(--dec);padding:1rem 1.2rem;margin:1.2rem 0}
.reste ul{margin:.4rem 0;padding-left:1.1rem}
.reste li{margin:.35rem 0}
.pied{margin-top:3rem;padding-top:1.2rem;border-top:1px solid var(--line);
 font-size:.85rem;color:var(--muted)}
a{color:var(--acier)}
</style></head><body><div class="enrobe">
<p class="eyebrow">Prototype 07 · pitch de vente</p>
<h1>L'entrevue, vue d'en face</h1>
<p class="sous">Une pièce de huit minutes où le candidat passe une entrevue — et où
le miroir n'est pas sa production, mais <b>la fiche que le recruteur remplit pendant
qu'il parle</b>.</p>

<h2>D'abord, la mauvaise nouvelle — avant que l'acheteur la dise</h2>
<div class="mur"><p><b>Depuis le 1<sup>er</sup> juillet 2026, la francisation en
milieu de travail est gratuite.</b> Elle est livrée par 32 partenaires publics
mandatés — 21 centres de services scolaires, 11 cégeps, aucun privé. L'entreprise
admissible ne paie rien, et touche même 1 200 $ par travailleur par session.</p>
<p>Vendre des cours de français à un employeur, c'est arriver deuxième. Un pitch qui
ne commence pas par là se fait démolir par le premier interlocuteur qui le sait.</p></div>

<h2>Mais le mandat public a cinq bornes — et la pièce tombe dans les cinq</h2>
<p>Ce ne sont pas des défauts du programme : ce sont les limites de ce qu'il a le
droit de faire. Chacune est un endroit où quelqu'un a un besoin que personne ne sert.</p>
§FAILLES§
<div class="bon"><p><b>Conséquence sur le client visé.</b> Ce n'est pas l'employeur.
Ce sont <b>les 32 partenaires</b> — ils ont le mandat, le financement et les groupes,
et c'est le matériel spécialisé qui leur manque — et les organismes d'employabilité,
qui préparent à l'entrevue sans rien pour la faire éprouver.</p></div>

<h2>La démonstration, en trente secondes</h2>
<p>C'est ce qu'on fait devant l'acheteur, et ça n'a jamais besoin de plus.</p>
<div class="demo"><ol>
<li>On lui fait répondre à la première question. Il parle une minute, bien.</li>
<li>La fiche du recruteur se remplit à droite — <b>deux lignes</b>.</li>
<li>Au bilan, sa propre réponse lui revient, avec un trait&nbsp;:
<span class="coup">il décroche</span> au quarantième mot.</li>
<li>Et sous le trait, en rayé&nbsp;: <b>ses deux meilleures informations</b>,
dites au cinquante-huitième et au soixante-treizième mot.</li>
</ol>
<p style="margin:.7rem 0 0">Un apprenant qui voit sa réponse de quarante secondes
produire une ligne et demie chez l'autre comprend en une fois ce que trois cours sur
la concision n'obtiennent pas.</p></div>

<h2>La mécanique, et pourquoi elle enseigne</h2>
<p>Le recruteur cherche quinze faits répartis sur six questions. Chacun finit dans
l'un de trois états, et les trois se calculent&nbsp;:</p>
<p><b>Retenu</b> — le fait arrive avant que l'attention lâche.<br>
<b>Rayé</b> — le fait est là, mais trop tard&nbsp;: dit après le décrochage.<br>
<b>Jamais dit</b> — il n'est pas venu.</p>
<p>La rature est le cœur de la pièce. Un candidat dont la meilleure information arrive
au soixantième mot n'a pas mal répondu&nbsp;: <b>il a répondu à quelqu'un qui
n'écoutait plus.</b></p>
<div class="bon"><p><b>Et elle se joue deux fois.</b> Le premier passage se fait à
l'aveugle, et il rate — c'est prévu. La leçon vient <b>après l'échec</b>, parce
qu'avant, on écoute poliment. Le second passage est celui qui mesure l'apprentissage,
et c'est le seul chiffre qu'on montre à un acheteur&nbsp;: <b>l'écart entre les
deux</b>.</p></div>

<h2>Ce qu'elle refuse de juger — et pourquoi c'est un argument de vente</h2>
<p>Ni l'accent, ni la grammaire, ni le vocabulaire. Ce n'est pas une précaution
morale&nbsp;: c'est <b>vérifiable dans le code</b>, et c'est la seule position tenable
devant un comité. Aucun motif de reconnaissance ne teste une forme correcte.</p>
<p>Le seul jugement porté est&nbsp;: le fait est-il arrivé, et à quel moment.</p>

<h2>Les objections qu'on va vous faire</h2>
§OBJECTIONS§

<h2>Ce que ça coûte</h2>
<dl class="chiffres">
<div><dt>Production</dt><dd>3 <small>jours</small></dd></div>
<div><dt>Médias à payer</dt><dd>0 <small>$</small></dd></div>
<div><dt>Durée jouée</dt><dd>8 <small>min</small></dd></div>
<div><dt>Le squelette</dt><dd>fait</dd></div>
</dl>
<p>Zéro dollar de médias parce que la pièce ne demande ni dessin ni tournage&nbsp;: le
recruteur est du texte, et sa voix se pré-synthétise une fois, les questions étant
fixes. La plomberie orale — micro, synthèse, débit — existe déjà et sert 87 modules.</p>
<p>Le squelette jouable est écrit et tourne&nbsp;: six questions, quinze faits,
l'analyse et le bilan. Ce qui reste est du contenu et de l'épreuve, pas de
l'invention.</p>

<h2>Ce qu'il reste à décider — et ce sont vos décisions</h2>
<div class="reste"><ul>
<li><b>Le second passage.</b> Il double la valeur pédagogique et allonge la pièce
d'un tiers. À trancher avant de produire, pas après.</li>
<li><b>À qui on montre ça en premier.</b> Un des 32 partenaires que vous connaissez
de l'intérieur, ou un organisme d'employabilité&nbsp;? Les deux n'ont pas le même
argument d'entrée.</li>
<li><b>Les quarante mots.</b> Le chiffre est assumé et affiché. S'il doit être
défendu autrement que par l'honnêteté, il faut une source — et il n'y en a pas
encore.</li>
<li><b>Le poste.</b> Journalier en usine est retenu. Un deuxième poste doublerait
la démonstration&nbsp;; il coûterait une journée de plus.</li>
</ul></div>

<p class="pied">Les chiffres du marché viennent du relevé du 31 août 2026 sur
Québec.ca et l'OQLF — voir <a href="analyse-marche.html">l'analyse de marché</a>,
écrite à la main exprès pour que ses chiffres vieillissent visiblement.
Le prototype vit dans l'atelier&nbsp;: <a href="atelier-prototypes/index.html">les
cinq prototypes construits</a>.</p>
</div></body></html>
"""

failles = "".join(
    f'<div class="faille"><span class="no">Faille {i+1} sur 5</span>'
    f"<h3>{t}</h3><p class=\"prog\">{p}</p><p class=\"nous\">{n}</p></div>"
    for i, (t, p, n) in enumerate(FAILLES))

objections = "".join(
    f'<div class="obj"><p class="q">{q}</p><p>{r}</p></div>' for q, r in OBJECTIONS)

page = (GABARIT.replace("/*§JETONS§*/", jetons())
               .replace("§FAILLES§", failles)
               .replace("§OBJECTIONS§", objections))
DEST.write_text(page, encoding="utf-8")
print(f"{DEST.name} — {DEST.stat().st_size/1024:.0f} Ko — "
      f"{len(FAILLES)} failles · {len(OBJECTIONS)} objections")
