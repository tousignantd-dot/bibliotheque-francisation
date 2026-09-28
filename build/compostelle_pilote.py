#!/usr/bin/env python3
"""Le pilote de Compostelle : faire relire l'outil par quelques amis avant de vendre.

    python3 build/compostelle_pilote.py   # → assets/presentations/compostelle-pilote.html

Daniel, 27 sept. 2026 : « il faut que je le fasse valider par des amis
pèlerins, entre autres, et espagnols […] trouve-moi la meilleure formule ».
La page vit au classeur (connexion exigée) parce qu'elle porte les codes
d'essai. Tout ce qui est compté (codes, fin, conversations) est relu dans
pelerins.py : la page ne peut pas promettre un code qui n'existe plus.
"""
import html, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "compostelle-pilote.html"
SITE = "https://portail.edufrancis.ca"
APP = SITE + "/modules-autonomes/compostelle/"
E = html.escape
MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def main():
    fin = date_fr(pelerins.ESSAI_FIN)
    n_conv = pelerins.ESSAI_CONVERSATIONS
    codes = list(pelerins.CODES_ESSAI.items())

    msg_fr = f"""Bonjour !

Je prépare une petite application pour apprendre l'espagnol du Camino francés, et j'aimerais ton avis avant de la lancer.

Elle s'ouvre dans le navigateur du téléphone, sans compte ni mot de passe :
{APP}#essai

Le lien ouvre le « mode essai » : tout est accessible dans l'ordre que tu veux. Un vrai pèlerin, lui, devra d'abord faire huit entraînements de 15 minutes.

Ce qui m'aiderait :
- faire un entraînement (par exemple le 1, « Les sons de l'espagnol ») et une étape (par exemple Roncesvalles) ;
- me dire ce qui est clair, ce qui bloque, et si les situations ressemblent au vrai chemin.

Pour donner ton avis : le lien « Donner mon avis », au bas de chaque écran (il ouvre un courriel déjà préparé).

Si tu veux essayer la conversation libre avec les personnages (« Parler librement », au bas de chaque étape), voici ton code : {{CODE}} — {n_conv} conversations, valable jusqu'au {fin}.

Pour voir en une page comment ça fonctionne : {APP}presentation.html

Merci, et ¡Buen Camino !
Daniel"""

    msg_es = f"""¡Hola!

Estoy preparando una pequeña aplicación para que los peregrinos francófonos aprendan el español del Camino francés, y me gustaría que revisaras el español antes de lanzarla.

Se abre en el navegador del móvil, sin cuenta ni contraseña:
{APP}#essai

La interfaz está en francés, pero todo lo que se oye y se dice está en español de España. Lo que más me ayuda:
- ¿Las frases son correctas y naturales en España?
- ¿Las voces pronuncian bien? ¿Algo suena raro?
- Anota la frase, la palabra y la pantalla donde la viste.

Para enviarme tus comentarios: el enlace « Donner mon avis » al pie de cada pantalla (abre un correo ya preparado), o escribe a support@edufrancis.ca.

Si quieres probar la conversación libre con los personajes (« Parler librement », al final de cada etapa), tu código es: {{CODE}} — {n_conv} conversaciones, válido hasta el {pelerins.ESSAI_FIN}.

¡Gracias y buen Camino!
Daniel"""

    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Compostelle — le pilote</title>", tete)
    tete = tete.replace("</head>", """<style>
.liens{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.lien{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--body)}
.lien b{display:block;color:var(--ink);font-size:16.5px;margin-bottom:4px}.lien span{font-size:14.5px}
.lien code{display:block;margin-top:6px;font-size:12.5px;color:var(--muted);word-break:break-all}
.msg{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:14.5px;line-height:1.5;max-height:340px;overflow:auto}
.rang{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.rang button{font:inherit;font-weight:800;border-radius:10px;border:1px solid var(--line);background:#F2C230;color:#13233B;padding:8px 14px;cursor:pointer}
.rang button.sec{background:var(--card);color:var(--ink)}
table.codes{width:100%;border-collapse:collapse;font-size:15px}
table.codes td,table.codes th{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left}
table.codes code{font-size:16px;font-weight:900;letter-spacing:.06em}
table.codes input{font:inherit;width:100%;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:#fff}
ol.etapes{counter-reset:e;list-style:none;padding:0;margin:0}
ol.etapes>li{counter-increment:e;position:relative;padding:12px 14px 12px 52px;background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0;font-size:15.5px}
ol.etapes>li::before{content:counter(e);position:absolute;left:14px;top:12px;width:26px;height:26px;border-radius:50%;background:#F2C230;color:#13233B;font-weight:900;display:grid;place-items:center;font-size:14px}
.garde{background:var(--decid-bg);border:1px solid var(--decid);border-radius:12px;padding:12px 16px;font-size:15px}
@media (max-width:760px){.liens{grid-template-columns:1fr}
 table.codes,table.codes tbody{display:block;min-width:0!important;width:100%} table.codes thead{display:none} table.codes tr{display:grid;grid-template-columns:auto 1fr;gap:6px 10px;padding:10px 0;border-bottom:1px solid var(--line)}
 table.codes td{border:0;padding:0} table.codes td:nth-child(3),table.codes td:nth-child(4){grid-column:1/-1}}
</style>
</head>""")

    lignes = "".join(f'<tr><td><code>{E(c)}</code></td><td>{E(lib)}</td>'
                     f'<td><input data-code="{E(c)}" placeholder="donné à… (un prénom ou un surnom)"></td>'
                     f'<td><button type="button" class="sec" data-msg="{E(c)}" style="font:inherit;border:1px solid var(--line);border-radius:8px;background:var(--card);padding:6px 10px;cursor:pointer">Copier le message</button></td></tr>'
                     for c, lib in codes)

    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Voyage &middot; grand public &middot; chemin de Saint-Jacques</p>
<h1>Compostelle &mdash; le pilote avec vos amis</h1>
<p class="chapeau">La formule : <strong>l'application reste ouverte, sans code</strong>, pendant le pilote. Vos amis reçoivent un lien
qui ouvre le <strong>mode essai</strong> (tout est accessible, dans l'ordre qu'ils veulent), un bouton <strong>« Donner mon avis »</strong>
au bas de chaque écran, et, s'ils veulent essayer la conversation avec les personnages, un <strong>code d'essai gratuit</strong>.
Rien n'est vendu : la vente reste fermée tant que les clés Stripe ne sont pas posées.</p>

<section class="premier">
  <h2>Les trois liens</h2>
  <div class="liens">
    <a class="lien" href="{APP}#essai" target="_blank" rel="noopener"><b>L'application, en mode essai</b>
      <span>Le lien à envoyer. Tout s'ouvre ; un bandeau bleu le rappelle, avec « Donner mon avis » et « Quitter le mode essai ».</span><code>{APP}#essai</code></a>
    <a class="lien" href="{APP}" target="_blank" rel="noopener"><b>L'application, comme un vrai pèlerin</b>
      <span>Sans le mode essai : les huit entraînements d'abord, le chemin ensuite.</span><code>{APP}</code></a>
    <a class="lien" href="{APP}presentation.html" target="_blank" rel="noopener"><b>Le dépliant, public</b>
      <span>La même page que celle du classeur, ouverte à tous, sans le lien vers le classeur.</span><code>{APP}presentation.html</code></a>
  </div>
</section>

<section>
  <h2>Faut-il un code ?</h2>
  <ul class="simple">
    <li><b>Non, pour tout le parcours</b> : les huit entraînements, les leçons, les dix étapes, les scènes, Marta le soir, Ma trousse, les tests. Aucun compte, aucun mot de passe.</li>
    <li><b>Oui, seulement pour « Parler librement »</b> (la conversation libre avec l'assistant, au bas de chaque étape), parce que chaque conversation coûte.
      Les douze codes ci-dessous sont gratuits : {n_conv} conversations chacun, jusqu'au {fin} inclusivement. Au pire, tous épuisés : environ 24 $ US.</li>
  </ul>
</section>

<section>
  <h2>Les codes d'essai</h2>
  <p style="font-size:14.5px;color:var(--muted)">Un code par personne. Notez à qui vous l'avez donné : c'est gardé dans ce navigateur seulement, rien ne part ailleurs.
  « Copier le message » copie le message en français avec ce code déjà écrit.</p>
  <table class="codes"><thead><tr><th>Code</th><th></th><th>Donné à</th><th></th></tr></thead><tbody>{lignes}</tbody></table>
</section>

<section>
  <h2>Le message à envoyer</h2>
  <div class="rang"><button type="button" id="copFr">Copier le message en français</button><button type="button" class="sec" id="copEs">Copier le message en espagnol (pour les hispanophones)</button></div>
  <div class="msg" id="msgFr">{E(msg_fr)}</div>
  <p style="font-size:14.5px;color:var(--muted);margin-top:8px">« {{CODE}} » est remplacé par un code libre quand vous copiez depuis le tableau ; sinon, retirez la phrase du code.</p>
  <details style="margin-top:10px"><summary><b>Le message en espagnol</b></summary><div class="msg" id="msgEs" style="margin-top:8px">{E(msg_es)}</div></details>
</section>

<section>
  <h2>Ce que vos amis ont à faire</h2>
  <ol class="etapes">
    <li><b>Les pèlerins</b> : un entraînement (le 1, avec sa leçon), puis l'étape 1 (Roncesvalles) et une étape plus loin (León, l'allergie). Les situations sont-elles celles du vrai chemin ?</li>
    <li><b>Les hispanophones</b> : les leçons, la trousse, et deux ou trois étapes. L'espagnol est-il juste, naturel, bien prononcé ? Ils notent la phrase et l'écran.</li>
    <li><b>Tous</b> : « Donner mon avis », au bas de chaque écran. Le courriel s'ouvre avec cinq questions déjà écrites, et l'écran où ils étaient.</li>
  </ol>
</section>

<section>
  <h2>Où arrivent les avis, et après</h2>
  <ul class="simple">
    <li>Les courriels arrivent à <b>support@edufrancis.ca</b>. Vérifiez que vous recevez bien cette boîte : écrivez-vous un avis d'essai avant d'envoyer le lien.</li>
    <li>L'application n'est <b>pas indexée</b> par les moteurs de recherche pendant le pilote : seuls ceux qui ont le lien la trouvent.</li>
    <li>Les codes d'essai cessent de fonctionner après le {fin}. Pour en couper un plus tôt, dites-le-moi.</li>
    <li>Envoyez-moi les avis (ou transférez les courriels) : je les trie et je corrige, comme une boucle d'audit.</li>
  </ul>
  <div class="garde" style="margin-top:12px"><b>À savoir :</b> le mode essai reste possible pour n'importe qui connaît « #essai ». Pour le lancement, je le retire
  (ou je le limite aux codes d'essai) : c'est ce qui rend les huit entraînements vraiment obligatoires.</div>
</section>
</div>
<script>
(function(){{
  const FR = document.getElementById('msgFr').textContent, ES = document.getElementById('msgEs').textContent;
  const copier = (t, b) => navigator.clipboard.writeText(t).then(() => {{ const o = b.textContent; b.textContent = 'Copié ✓'; setTimeout(() => b.textContent = o, 1500); }});
  const sansCode = t => t.split('\\n').filter(l => !l.includes('{{CODE}}')).join('\\n');
  document.getElementById('copFr').onclick = e => copier(sansCode(FR), e.target);
  document.getElementById('copEs').onclick = e => copier(sansCode(ES), e.target);
  document.querySelectorAll('button[data-msg]').forEach(b => b.onclick = () => copier(FR.replace('{{CODE}}', b.dataset.msg), b));
  document.querySelectorAll('input[data-code]').forEach(i => {{
    const k = 'pilote:' + i.dataset.code;
    try {{ i.value = localStorage.getItem(k) || ''; }} catch(e) {{}}
    i.oninput = () => {{ try {{ localStorage.setItem(k, i.value); }} catch(e) {{}} }};
  }});
}})();
</script>
</body>
</html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), f"— {len(codes)} codes, jusqu'au {fin}")


if __name__ == "__main__":
    main()
