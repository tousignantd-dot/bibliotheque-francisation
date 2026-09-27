#!/usr/bin/env python3
"""La vente de Compostelle : ce qui est branché, où le voir, et comment l'ouvrir.

    python3 build/compostelle_vente.py   # → assets/presentations/compostelle-vente.html

Daniel, 26 sept. 2026 : « où as-tu mis le lien pour que je puisse le vérifier ? ».
Le paiement (pelerins.py, formule B) est en production mais fermé tant que les
clés Stripe manquent : sans cette page, rien ne se voit. Elle réunit les liens
à ouvrir (le mode d'emploi, « Parler librement »), les étapes que Daniel seul
peut faire (compte Stripe, clés dans Railway) et l'essai en mode test.
"""
import pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-vente.html"
APP = "/modules-autonomes/compostelle/"


def main():
    o = pelerins.offre()
    d = lambda c: f"{c / 100:.2f}".replace(".", ",") + " $"
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — la vente</title>", tete)
    tete = tete.replace("</head>", """<style>
.liens{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.lien{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--body)}
.lien b{display:block;color:var(--ink);font-size:16.5px;margin-bottom:4px}
.lien span{font-size:14.5px}
.lien code{font-size:12.5px;color:var(--muted);word-break:break-all}
ol.etapes{counter-reset:e;list-style:none;padding:0;margin:0}
ol.etapes>li{counter-increment:e;position:relative;padding:12px 14px 12px 52px;background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0;font-size:15.5px}
ol.etapes>li::before{content:counter(e);position:absolute;left:14px;top:12px;width:26px;height:26px;border-radius:50%;background:#F2C230;color:#13233B;font-weight:900;display:grid;place-items:center;font-size:14px}
.etat{display:inline-block;font-weight:900;font-size:13px;border-radius:99px;padding:3px 10px;background:var(--decid-bg);color:var(--decid)}
.garde{background:var(--decid-bg);border:1px solid var(--decid);border-radius:12px;padding:12px 16px;font-size:15px}
@media (max-width:760px){.liens{grid-template-columns:1fr}}
</style>
</head>""")
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; la vente, et où tout voir</h1>
<p class="chapeau">La formule B est branchée : le chemin gratuit, « Parler librement » à <strong>{d(o["prix"])}</strong> pour
{o["jours"] // 30} mois et {o["conversations"]} conversations, recharge de {o["rechargeConversations"]} à {d(o["recharge"])}.
État aujourd'hui : <span class="etat">en ligne, vente fermée</span> — elle s'ouvre dès que les clés Stripe sont posées.</p>

<section class="premier">
  <h2>Les liens à ouvrir</h2>
  <div class="liens">
    <a class="lien" href="{APP}#guide" target="_blank" rel="noopener"><b>Le mode d'emploi, pour le pèlerin</b>
      <span>« Comment ça marche ? » : le bouton est sous « Reprendre la route », sur l'accueil, et sur l'écran de bienvenue.</span><br><code>{APP}#guide</code></a>
    <a class="lien" href="{APP}#jour/pamplona/libre" target="_blank" rel="noopener"><b>« Parler librement », où se vend l'accès</b>
      <span>Au bas de chaque journée. Tant que la vente est fermée, on n'y voit que le champ du code ; ouverte, la rubrique
      « Pas encore de code ? » s'ajoute.</span><br><code>{APP}#jour/pamplona/libre</code></a>
    <a class="lien" href="compostelle-parcours.html"><b>L'infographie du parcours</b><span>La même route que le mode d'emploi, pour vous et vos partenaires.</span></a>
    <a class="lien" href="compostelle-prix.html"><b>La proposition de prix</b><span>Les coûts mesurés, les trois formules, le calculateur.</span></a>
  </div>
</section>

<section>
  <h2>Ce que vit le pèlerin, une fois la vente ouverte</h2>
  <ol class="etapes">
    <li>Dans « Parler librement », « Pas encore de code ? » : {o["conversations"]} conversations pendant {o["jours"] // 30} mois, {d(o["prix"])}. Les journées restent gratuites.</li>
    <li>« Obtenir mon code » ouvre la page de paiement de Stripe (carte). Nous ne recevons ni son nom ni sa carte.</li>
    <li>Au retour, son code en gros (« PC » + six caractères), à copier. Il est gardé dans le téléphone et écrit sur le reçu de Stripe.</li>
    <li>« Il vous reste 97 conversations, jusqu'au … ». Sous dix, un bouton « Ajouter {o["rechargeConversations"]} conversations — {d(o["recharge"])} ».</li>
    <li>Une conversation se décompte après la première réponse — une panne ne se paie pas. {o["toursMax"]} tours au plus par conversation, {o["parJour"]} conversations par jour au plus.</li>
  </ol>
</section>

<section>
  <h2>Pour ouvrir la vente — ce que vous seul pouvez faire</h2>
  <ol class="etapes">
    <li><b>Créer un compte sur stripe.com</b> (identité, compte bancaire pour les versements).</li>
    <li><b>Déclarer l'avis de paiement.</b> Dans Stripe : Développeurs → Webhooks → ajouter
      <code>https://portail.edufrancis.ca/api/pelerins/stripe</code>, événement <code>checkout.session.completed</code>.
      Stripe donne un secret de signature qui commence par <code>whsec_</code>.</li>
    <li><b>Poser deux variables dans Railway</b> (onglet Variables) : <code>STRIPE_SECRET_KEY</code> (la clé secrète,
      <code>sk_…</code>) et <code>STRIPE_WEBHOOK_SECRET</code> (le <code>whsec_…</code>). Ne jamais les coller dans une conversation.</li>
    <li><b>Activer les reçus par courriel</b> (Paramètres → Courriels clients) : c'est ce qui envoie le code par écrit.</li>
    <li><b>Commencer en mode test</b> (<code>sk_test_…</code>, carte 4242 4242 4242 4242, n'importe quelle date future) : dites-le-moi,
      et je fais l'essai complet en ligne. Puis passer aux clés réelles.</li>
  </ol>
  <p style="margin-top:10px">Le prix, le quota et la durée se changent dans les mêmes variables Railway
  (<code>COMPOSTELLE_PRIX_CENTS</code>, <code>COMPOSTELLE_CONVERSATIONS</code>, <code>COMPOSTELLE_DUREE_JOURS</code>,
  <code>COMPOSTELLE_RECHARGE_CENTS</code>…), sans toucher au code.</p>
</section>

<section>
  <h2>Ce qui a été vérifié</h2>
  <ul class="simple">
    <li>34 vérifications sans réseau (<code>build/controles/pelerins.py</code>) : signatures fausses ou périmées refusées, paiement
      crédité une seule fois, code non payé, expiré, épuisé ou hors de Compostelle refusé.</li>
    <li>Par le serveur : un code payé ouvre une vraie conversation (le compteur passe de 100 à 99), et il est refusé par toutes les autres routes d'IA du portail.</li>
    <li>Au téléphone, contre un faux Stripe local : achat, retour, code, conversation, conversations épuisées, recharge.</li>
    <li><b>Pas encore</b> contre le vrai Stripe : c'est l'essai de l'étape 5.</li>
  </ul>
  <div class="garde" style="margin-top:12px"><b>Avant de vendre au public :</b> la relecture de l'espagnol par une personne d'Espagne,
  et, avec un comptable, les taxes (TPS/TVQ) et la vente hors Québec.</div>
</section>
</div>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE))


if __name__ == "__main__":
    main()
