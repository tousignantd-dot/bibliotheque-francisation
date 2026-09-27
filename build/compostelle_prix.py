#!/usr/bin/env python3
"""Vendre « En route vers Compostelle » aux pèlerins : ce que ça coûte, et une proposition de prix.

    python3 build/compostelle_prix.py   # → assets/presentations/compostelle-prix.html

Question de Daniel, 26 sept. 2026 : « si je vends un accès pendant un certain
temps, en tenant compte des jeux de rôle, combien ça risque de me coûter, et
devrais-je limiter le temps ? Fais-moi une proposition. »

Le coût d'une conversation vient de la MESURE du 26 sept. (registre des appels
du bac à sable, scénario camino-es-fr, claude-sonnet-5 + bilan haiku) : chaque
tour relit toute la conversation, donc son prix monte avec la longueur. Les
autres postes (paiement, trafic) sont des tarifs publics, à revérifier le jour
de la décision. La page porte un calculateur : les hypothèses d'usage sont des
hypothèses, et c'est Daniel qui les règle.
"""
import html, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-prix.html"
E = html.escape

# Mesuré le 26 sept. 2026 : trois conversations de trois tours, puis le bilan.
# (tour, jetons d'entrée, jetons de sortie, coût $ US)
MESURE_TOURS = [(1, 821, 40, .003063), (2, 901, 70, .003753), (3, 993, 41, .003594),
                (1, 844, 40, .003132), (2, 905, 53, .003510), (3, 997, 60, .003891),
                (1, 824, 28, .002892), (2, 893, 33, .003174), (3, 937, 29, .003246)]
MESURE_BILAN = [.001633, .001639]
PRIX_ENTREE, PRIX_SORTIE = 3 / 1e6, 15 / 1e6       # claude-sonnet-5, $ US par jeton (TARIFS de journal_api)


def cout_conversation(tours):
    """Coût modèle d'une conversation de `tours` tours, extrapolé de la mesure :
    l'entrée croît d'environ 85 jetons par tour (la conversation relue), la sortie
    reste vers 45 jetons ; un bilan plus long à mesure que la conversation grandit."""
    base = sum(t[1] for t in MESURE_TOURS if t[0] == 1) / 3
    pente = (sum(t[1] for t in MESURE_TOURS if t[0] == 3) / 3 - base) / 2
    sortie = sum(t[2] for t in MESURE_TOURS) / len(MESURE_TOURS)
    total = sum((base + pente * k) * PRIX_ENTREE + sortie * PRIX_SORTIE for k in range(tours))
    bilan = sum(MESURE_BILAN) / 2 * (1 + tours / 6)
    return total + bilan


def main():
    c3, c10, c16 = (cout_conversation(n) for n in (3, 10, 16))
    mesure_moy = sum(t[3] for t in MESURE_TOURS) / len(MESURE_TOURS)
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — le prix</title>", tete)
    tete = tete.replace("</head>", """<style>
table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}
.formules{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.formule{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.formule.reco{border:2px solid var(--fait);box-shadow:0 0 0 3px var(--fait-bg)}
.formule .prix{font-size:28px;font-weight:900;color:var(--ink);line-height:1.1}
.formule .prix small{font-size:14px;font-weight:700;color:var(--muted)}
.formule h3{margin:0;font-size:17px}
.formule ul{margin:4px 0 0;padding-left:18px;font-size:14.5px}.formule li{margin:4px 0}
.formule .badge{align-self:flex-start;font-size:11.5px;font-weight:900;letter-spacing:.06em;text-transform:uppercase;color:var(--fait);background:var(--fait-bg);border-radius:99px;padding:2px 10px}
.calc{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:16px}
.calc .champs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 18px}
.calc label{display:flex;flex-direction:column;gap:4px;font-size:14px;font-weight:700;color:var(--ink)}
.calc label span{font-weight:600;color:var(--muted);font-size:13px}
.calc input{font:inherit;font-size:16px;padding:8px 10px;border:1px solid var(--line-fort);border-radius:8px;background:var(--ground);color:var(--ink);width:100%}
.res{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:14px}
.res div{background:var(--sunken);border-radius:10px;padding:10px 12px;font-size:13.5px}
.res b{display:block;font-size:22px;color:var(--ink)}
.res .net b{color:var(--fait)}
.garde{background:var(--decid-bg);border:1px solid var(--decid);border-radius:12px;padding:12px 16px;font-size:15px}
@media (max-width:760px){.formules,.res{grid-template-columns:1fr}.calc .champs{grid-template-columns:1fr}}
</style>
</head>""")
    tours_html = "".join(f"<tr><td>{t}</td><td>{e:,}".replace(",", " ") + f"</td><td>{s}</td><td>{c * 100:.2f} ¢</td></tr>"
                         for t, e, s, c in MESURE_TOURS[:3])
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; le vendre aux pèlerins</h1>
<p class="chapeau">Ce que coûte un pèlerin, mesuré ; pourquoi limiter <strong>les conversations</strong> plutôt que le temps ; et
trois formules, dont une recommandée. Un calculateur au bas de la page refait les marges avec vos hypothèses.</p>

<section class="premier">
  <h2>Ce qui coûte, et ce qui ne coûte rien</h2>
  <div class="chiffres">
    <div class="ch"><span class="n">0 $</span><span class="q">les dix journées, la trousse, le test : tout se joue dans le téléphone</span></div>
    <div class="ch"><span class="n">≈ {c10 * 100:.1f} ¢</span><span class="q">US, une conversation « Parler librement » de 10 tours, bilan compris</span></div>
    <div class="ch"><span class="n">≈ 0,2 ¢</span><span class="q">le téléchargement complet (38 Mo à 0,05 $ US le Go)</span></div>
  </div>
  <p><b>Le seul coût qui grandit avec l'usage, c'est l'assistant</b> de « Parler librement ». Tout le reste est déjà payé : les voix
  ont été produites une fois (environ 1 $ pour les 692 sons), les dessins aussi, et un pèlerin de plus ne les refait pas payer.
  Dans « Parler librement », la personne parle avec la voix du téléphone : pas de synthèse facturée.</p>
</section>

<section>
  <h2>La mesure</h2>
  <p>Trois conversations d'essai du 26 septembre, rejouées contre le serveur (scénario du chemin, modèle
  claude-sonnet-5, bilan par claude-haiku-4-5). Chaque tour relit toute la conversation : le prix d'un tour monte donc avec la
  longueur, d'environ 85 jetons par tour.</p>
  <table class="cmp"><thead><tr><th>Tour</th><th>Jetons lus</th><th>Jetons écrits</th><th>Coût ($ US)</th></tr></thead>
  <tbody>{tours_html}<tr><td>Bilan</td><td colspan="2">une fois par conversation</td><td>{sum(MESURE_BILAN) / 2 * 100:.2f} ¢</td></tr></tbody></table>
  <p style="margin-top:10px">Extrapolé : <b>{c3 * 100:.1f} ¢</b> pour 3 tours, <b>{c10 * 100:.1f} ¢</b> pour 10, <b>{c16 * 100:.1f} ¢</b> pour 16
  (tout en $ US). Un tour coûte en moyenne {mesure_moy * 100:.2f} ¢ au début. Arrondissons : <b>5 ¢ la conversation</b>, soit
  environ <b>7 ¢ canadiens</b>.</p>
</section>

<section>
  <h2>Limiter le temps, ou les conversations ?</h2>
  <p><b>Le temps ne protège de rien.</b> Un pèlerin qui a six mois d'accès peut faire dix conversations ou mille : c'est le nombre
  de conversations qui fait la facture, pas la durée. À l'inverse, les journées ne coûtent rien : les limiter dans le temps ne
  ferait que fâcher un pèlerin qui revient en mars préparer son chemin de mai.</p>
  <p>La proposition tient donc en trois bornes :</p>
  <ul class="simple">
    <li><b>Une durée large</b>, qui couvre la préparation et la marche : <b>12 mois</b>. On prépare le Camino deux à six mois
      avant, on marche cinq semaines, et plusieurs reviennent l'année suivante.</li>
    <li><b>Un nombre de conversations</b> inclus — c'est la vraie borne de coût.</li>
    <li><b>Une longueur de conversation</b> : 16 tours au plus (la personne conclut d'elle-même, « ¡Buen Camino! »), et
      30 conversations par jour au plus, contre un code qui circulerait.</li>
  </ul>
</section>

<section>
  <h2>Trois formules</h2>
  <div class="formules">
    <div class="formule"><h3>A · Tout payant</h3><div class="prix">24,99 $ <small>12 mois</small></div>
      <ul><li>les dix journées, la trousse, le test</li><li>100 conversations</li><li>recharge : 50 conversations, 4,99 $</li></ul>
      <p style="font-size:13.5px;color:var(--muted);margin:4px 0 0">Il faut alors fermer l'application derrière un code : aujourd'hui, elle est ouverte à tous.</p></div>
    <div class="formule reco"><span class="badge">Recommandée</span><h3>B · Le chemin libre, la conversation payante</h3>
      <div class="prix">19,99 $ <small>12 mois</small></div>
      <ul><li>gratuit : les dix journées, la trousse, le test — tel quel</li><li>payant : « Parler librement », 100 conversations</li>
      <li>recharge : 50 conversations, 4,99 $</li></ul>
      <p style="font-size:13.5px;color:var(--muted);margin:4px 0 0">Rien à fermer : le code sert déjà à « Parler librement ».
      Le gratuit fait connaître, et ne coûte rien.</p></div>
    <div class="formule"><h3>C · À la conversation</h3><div class="prix">9,99 $ <small>40 conversations</small></div>
      <ul><li>gratuit : les dix journées, la trousse, le test</li><li>40 conversations, sans date limite</li><li>recharge au même prix</li></ul>
      <p style="font-size:13.5px;color:var(--muted);margin:4px 0 0">La plus simple à comprendre ; la moins rentable par vente, à cause des frais fixes du paiement.</p></div>
  </div>
  <p style="margin-top:12px"><b>Pourquoi B.</b> Elle vend la seule chose qui coûte et qui ne s'obtient nulle part ailleurs : parler
  avec quelqu'un qui répond vraiment. Le reste attire les pèlerins sans rien coûter, et la marge tient même pour celui qui épuise
  ses 100 conversations. Et techniquement, elle est presque là : le code existe, il suffit qu'un paiement le crée.</p>
</section>

<section>
  <h2>Pour un pèlerin de la formule B</h2>
  <table class="cmp"><thead><tr><th></th><th>Usage léger (20 conv.)</th><th>Usage plein (100 conv.)</th></tr></thead><tbody>
    <tr><td>Prix payé</td><td>19,99 $</td><td>19,99 $</td></tr>
    <tr><td>Frais de paiement (≈ 2,9 % + 0,30 $)</td><td>− 0,88 $</td><td>− 0,88 $</td></tr>
    <tr><td>Assistant (5 ¢ US ≈ 7 ¢ CA la conversation)</td><td>− 1,40 $</td><td>− 7,00 $</td></tr>
    <tr><td>Trafic</td><td>≈ 0 $</td><td>≈ 0 $</td></tr>
    <tr><td><b>Reste, avant impôts et frais fixes</b></td><td><b>≈ 17,70 $</b></td><td><b>≈ 12,10 $</b></td></tr>
  </tbody></table>
  <p style="margin-top:10px">Vendu dans l'App Store ou Google Play, le magasin prend 15 % (petite entreprise) à 30 % : sur 19,99 $,
  de 3 $ à 6 $ de plus. Voir <a href="compostelle-magasins.html">« En faire une app à télécharger ? »</a>.</p>
</section>

<section>
  <h2>Les frais qui ne dépendent pas des ventes</h2>
  <ul class="simple">
    <li><b>La relecture par une personne d'Espagne</b> — à faire avant de vendre quoi que ce soit ; un coût unique.</li>
    <li><b>Le serveur</b> : il sert déjà le portail ; les pèlerins y ajoutent peu (surtout du trafic, à 0,05 $ US le Go).</li>
    <li><b>Le paiement en ligne</b> à brancher (Stripe, par exemple) : quelques jours de travail — la page de paiement, puis le serveur
      qui crée le code et le montre au pèlerin, avec son compteur de conversations.</li>
    <li><b>Le soutien</b> : un pèlerin qui a perdu son code, un remboursement. C'est du temps, pas de l'argent.</li>
    <li><b>Si magasins d'applications</b> : 99 $ US par an (Apple), 25 $ US une fois (Google).</li>
  </ul>
</section>

<section>
  <h2>Refaire le calcul</h2>
  <div class="calc">
    <div class="champs">
      <label>Prix de vente ($ CA)<span>la formule B propose 19,99 $</span><input id="p" type="number" step="0.01" value="19.99"></label>
      <label>Conversations incluses<span>la borne de coût</span><input id="q" type="number" value="100"></label>
      <label>Conversations faites en moyenne<span>hypothèse ; un pèlerin en fait rarement toutes</span><input id="m" type="number" value="30"></label>
      <label>Coût d'une conversation (¢ US)<span>mesuré ≈ {c10 * 100:.1f} ¢ pour 10 tours</span><input id="c" type="number" step="0.1" value="5"></label>
      <label>Taux de change ($ CA pour 1 $ US)<span>à revérifier</span><input id="x" type="number" step="0.01" value="1.38"></label>
      <label>Ventes par année<span>hypothèse</span><input id="v" type="number" value="200"></label>
      <label>Commission du magasin (%)<span>0 sur le site ; 15 ou 30 dans un magasin</span><input id="k" type="number" value="0"></label>
      <label>Frais fixes par année ($ CA)<span>magasins, part du serveur…</span><input id="f" type="number" value="300"></label>
    </div>
    <div class="res">
      <div><b id="r1">—</b>coût moyen de l'assistant par pèlerin</div>
      <div><b id="r2">—</b>reste par pèlerin (usage moyen)</div>
      <div><b id="r3">—</b>reste par pèlerin qui épuise tout</div>
      <div class="net"><b id="r4">—</b>reste sur l'année, frais fixes déduits</div>
      <div><b id="r5">—</b>ventes pour couvrir les frais fixes</div>
      <div><b id="r6">—</b>part du prix qui part à l'assistant (usage moyen)</div>
    </div>
  </div>
</section>

<div class="garde"><b>À revérifier le jour d'une décision.</b> Les tarifs du modèle, des magasins et du paiement changent ; le taux
de change aussi. La taxe de vente (TPS/TVQ) et ce que la loi demande pour vendre à des gens hors du Québec sont à valider avec un
comptable. Le coût de l'assistant est mesuré sur des conversations d'essai courtes, puis extrapolé : le pilote avec cinq
pèlerins donnera le vrai nombre de tours et de conversations — c'est lui qui doit fixer le quota.</div>
</div>
<script>
const $ = id => document.getElementById(id), fmt = n => n.toLocaleString('fr-CA', {{style:'currency', currency:'CAD'}});
function calc(){{
  const p = +$('p').value, q = +$('q').value, m = Math.min(+$('m').value, q), c = +$('c').value / 100 * +$('x').value,
        v = +$('v').value, k = +$('k').value / 100, f = +$('f').value;
  const paiement = k > 0 ? p * k : p * 0.029 + 0.30;
  const moyen = m * c, plein = q * c;
  $('r1').textContent = fmt(moyen);
  $('r2').textContent = fmt(p - paiement - moyen);
  $('r3').textContent = fmt(p - paiement - plein);
  $('r4').textContent = fmt(v * (p - paiement - moyen) - f);
  const marge = p - paiement - moyen;
  $('r5').textContent = marge > 0 ? Math.ceil(f / marge) + ' ventes' : 'jamais';
  $('r6').textContent = p > 0 ? Math.round(100 * moyen / p) + ' %' : '—';
}}
document.querySelectorAll('.calc input').forEach(i => i.addEventListener('input', calc)); calc();
</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(f"{SORTIE.relative_to(RACINE)} — {c3*100:.1f} / {c10*100:.1f} / {c16*100:.1f} ¢ US")


if __name__ == "__main__":
    main()
