#!/usr/bin/env python3
"""L'essai auprès de proches des trousses de métier — la formule de Compostelle.

    python3 build/metier_essai.py   # → assets/presentations/francoeur-essai.html, hotellerie-essai.html

Daniel, 28 sept. 2026 : « un dépliant et la même formule » que Compostelle
pour la Maison Francœur et l'Hôtel Rive-Claire. La formule : l'application
reste publique et gratuite (tout sauf le jeu de rôle), chaque proche reçoit un
lien qui porte déjà son code d'essai (?code=…), « Votre avis » est au bas de
chaque écran, et le dépliant public dit en une page comment ça marche.

La page vit au classeur (connexion exigée) parce qu'elle porte les codes. Ne
pas confondre avec francoeur-pilote.html et hotellerie-pilote.html : ceux-là
sont le protocole du pilote EN ENTREPRISE, avec un formateur et un groupe.
Tout ce qui est compté (codes, fin, conversations) est relu dans pelerins.py.
"""
import html, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SITE = "https://portail.edufrancis.ca"
E = html.escape
MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()
# Les codes qui ont servi aux essais de Claude (capture d'une scène en ligne,
# 28 sept. 2026) : quelques conversations en moins. Les donner en dernier.
DEJA_SERVI = {"PCKN7EJ5": "a servi aux essais : 3 ou 4 conversations en moins"}


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def date_en(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
            "November", "December"][m - 1] + f" {j}, {a}"


def date_es(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{j} de " + "enero febrero marzo abril mayo junio julio agosto septiembre octubre noviembre diciembre".split()[m - 1] + f" de {a}"


def trousses(fin, n):
    fin_en, fin_es = date_en(pelerins.ESSAI_FIN), date_es(pelerins.ESSAI_FIN)
    fr_code = f"Ce lien contient ton code d'essai, {{CODE}} : il ouvre aussi {{JEU}}, {n} conversations, jusqu'au {fin}."
    return [
        {"cle": "francoeur", "sortie": "francoeur-essai.html", "app": SITE + "/modules-autonomes/francoeur-planches/",
         "titre": "Maison Francœur — l'essai avec vos proches", "eyebrow": "Vente au détail &middot; Vêtements &middot; vente directe",
         "jeu": "le magasin joué", "jeu_long": "le magasin joué (les huit clients, au bas de l'accueil : « Le magasin »)",
         "msgs": [
            ("fr", "français", f"""Bonjour !

Je prépare une petite application pour apprendre le français de la vente de vêtements (mots, exercices, puis de vrais clients qui répondent), et j'aimerais ton avis avant de la lancer.

Elle s'ouvre dans le navigateur du téléphone, sans compte ni mot de passe :
{{LIEN}}

{fr_code.replace('{JEU}', 'le magasin, où les clients te parlent')}

Ce qui m'aiderait :
- choisir une langue d'appui, faire le petit test, puis un rayon et un exercice ;
- servir deux ou trois clients dans « Le magasin » ;
- me dire ce qui est clair, ce qui bloque, et si ça ressemble au vrai plancher.

Pour donner ton avis : l'adresse support@edufrancis.ca, au bas de chaque écran.
Pour voir en une page comment ça fonctionne : {{DEPLIANT}}

Merci !
Daniel"""),
            ("en", "anglais", f"""Hi!

I'm building a small app to learn the French of clothing retail (words, exercises, then real customers who answer back), and I'd love your opinion before launching it.

It opens in your phone's browser, no account, no password:
{{LIEN}}

This link carries your trial code, {{CODE}}: it also opens the shop role-play, {n} conversations, until {fin_en}. You can pick English as your help language.

What would help me:
- do the short test, one department and one exercise;
- serve two or three customers in « Le magasin »;
- tell me what's clear, what gets in the way, and whether it feels like a real store.

Feedback: support@edufrancis.ca (the address is at the bottom of every screen).
How it works, in one page: {{DEPLIANT}}

Thanks!
Daniel"""),
            ("es", "espagnol", f"""¡Hola!

Estoy preparando una pequeña aplicación para aprender el francés de la venta de ropa (palabras, ejercicios y luego clientes de verdad que responden), y me gustaría tu opinión antes de lanzarla.

Se abre en el navegador del móvil, sin cuenta ni contraseña:
{{LIEN}}

Este enlace lleva tu código de prueba, {{CODE}}: también abre la tienda con clientes, {n} conversaciones, hasta el {fin_es}. Puedes elegir el español como idioma de apoyo.

Lo que más me ayuda:
- hacer la pequeña prueba, una sección y un ejercicio;
- atender a dos o tres clientes en « Le magasin »;
- decirme qué está claro, qué bloquea y si se parece a una tienda de verdad.

Comentarios: support@edufrancis.ca (la dirección está al pie de cada pantalla).
Cómo funciona, en una página: {{DEPLIANT}}

¡Gracias!
Daniel"""),
         ],
         "faire": ["<b>Tous</b> : une langue d'appui, le test « Mon niveau », un rayon, un exercice, puis deux ou trois clients du magasin.",
                   "<b>Ceux qui ont travaillé en magasin</b> : les situations et les phrases ressemblent-elles au vrai plancher ? Qu'est-ce qui manque ?",
                   "<b>Ceux qui apprennent le français</b> : l'aide dans leur langue est-elle juste ? Les voix se comprennent-elles ?"]},
        {"cle": "hotel", "sortie": "hotellerie-essai.html", "app": SITE + "/modules-autonomes/hotel-reception/",
         "titre": "Hôtel Rive-Claire — l'essai avec vos proches", "eyebrow": "Hôtellerie &middot; Réception &middot; vente directe",
         "jeu": "le comptoir joué", "jeu_long": "le comptoir joué (les huit clients, au bas de l'accueil)",
         "msgs": [
            ("fr", "français", f"""Bonjour !

Je prépare une petite application pour apprendre la langue de la réception d'hôtel — en français, en anglais ou en espagnol — et j'aimerais ton avis avant de la lancer.

Elle s'ouvre dans le navigateur du téléphone, sans compte ni mot de passe :
{{LIEN}}

{fr_code.replace('{JEU}', 'le comptoir, où les clients te parlent')}

Ce qui m'aiderait :
- choisir la langue que tu parles et celle que tu apprends ;
- toucher le comptoir, faire une série d'exercices, puis accueillir deux ou trois clients ;
- me dire ce qui est clair, ce qui bloque, et si ça ressemble à une vraie réception.

Pour donner ton avis : l'adresse support@edufrancis.ca, au bas de chaque écran.
Pour voir en une page comment ça fonctionne : {{DEPLIANT}}

Merci !
Daniel"""),
            ("en", "anglais", f"""Hi!

I'm building a small app to learn the language of the hotel front desk — in French, English or Spanish — and I'd love your opinion before launching it. The English voices and phrases are the part I most need a native speaker to check.

It opens in your phone's browser, no account, no password:
{{LIEN}}

This link carries your trial code, {{CODE}}: it also opens the front-desk role-play, {n} conversations, until {fin_en}.

What would help me:
- choose "I speak" and "I'm learning" (for example French → English);
- tap the desk, do one exercise series, then check in two or three guests;
- note any sentence that sounds wrong or unnatural, and on which screen.

Feedback: support@edufrancis.ca (the address is at the bottom of every screen).
How it works, in one page: {{DEPLIANT}}

Thanks!
Daniel"""),
            ("es", "espagnol", f"""¡Hola!

Estoy preparando una pequeña aplicación para aprender el idioma de la recepción de hotel — en francés, inglés o español — y me gustaría tu opinión antes de lanzarla. Lo que más necesito es que un hispanohablante revise el español (de México).

Se abre en el navegador del móvil, sin cuenta ni contraseña:
{{LIEN}}

Este enlace lleva tu código de prueba, {{CODE}}: también abre el mostrador con clientes, {n} conversaciones, hasta el {fin_es}.

Lo que más me ayuda:
- elegir « Hablo » y « Aprendo » (por ejemplo español → francés, o francés → español);
- tocar el mostrador, hacer una serie de ejercicios y atender a dos o tres clientes;
- anotar la frase que suena rara o incorrecta, y en qué pantalla.

Comentarios: support@edufrancis.ca (la dirección está al pie de cada pantalla).
Cómo funciona, en una página: {{DEPLIANT}}

¡Gracias!
Daniel"""),
         ],
         "faire": ["<b>Tous</b> : leurs deux langues, le comptoir, une série d'exercices, puis deux ou trois clients du comptoir joué.",
                   "<b>Les anglophones et les hispanophones</b> : l'anglais et l'espagnol sont-ils justes et naturels, les voix bien prononcées ? Ils notent la phrase et l'écran.",
                   "<b>Ceux qui ont travaillé en hôtellerie</b> : les situations sont-elles celles d'une vraie réception ?"]},
    ]


def construire(t, fin, n, tete_src):
    app = t["app"]
    codes = [(c, l) for c, (l, tr) in pelerins.CODES_ESSAI_TROUSSES.items() if tr == t["cle"]]
    codes.sort(key=lambda x: x[0] in DEJA_SERVI)
    tete = re.sub(r"<title>.*?</title>", f"<title>{E(t['titre'])}</title>", tete_src)
    tete = tete.replace("</head>", """<style>
.liens{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.lien{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--body)}
.lien b{display:block;color:var(--ink);font-size:16.5px;margin-bottom:4px}.lien span{font-size:14.5px}
.lien code{display:block;margin-top:6px;font-size:12.5px;color:var(--muted);word-break:break-all}
.msg{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:14.5px;line-height:1.5;max-height:340px;overflow:auto}
.rang{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.rang button,table.codes button{font:inherit;font-weight:800;border-radius:10px;border:1px solid var(--line);background:var(--card);color:var(--ink);padding:7px 12px;cursor:pointer}
.rang button[aria-pressed=true]{background:var(--ink);color:#fff}
table.codes{width:100%;border-collapse:collapse;font-size:15px}
table.codes td,table.codes th{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left;vertical-align:middle}
table.codes code{font-size:16px;font-weight:900;letter-spacing:.06em}
table.codes small{display:block;color:var(--muted);font-size:12.5px}
table.codes input{font:inherit;width:100%;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:#fff}
ol.etapes{counter-reset:e;list-style:none;padding:0;margin:0}
ol.etapes>li{counter-increment:e;position:relative;padding:12px 14px 12px 52px;background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0;font-size:15.5px}
ol.etapes>li::before{content:counter(e);position:absolute;left:14px;top:12px;width:26px;height:26px;border-radius:50%;background:var(--ink);color:#fff;font-weight:900;display:grid;place-items:center;font-size:14px}
.garde{background:var(--decid-bg);border:1px solid var(--decid);border-radius:12px;padding:12px 16px;font-size:15px}
@media (max-width:760px){.liens{grid-template-columns:1fr}
 table.codes,table.codes tbody{display:block;min-width:0!important;width:100%} table.codes thead{display:none} table.codes tr{display:grid;grid-template-columns:auto 1fr;gap:6px 10px;padding:10px 0;border-bottom:1px solid var(--line)}
 table.codes td{border:0;padding:0} table.codes td:nth-child(3),table.codes td:nth-child(4){grid-column:1/-1}}
</style>
</head>""")
    lignes = "".join(
        f'<tr><td><code>{E(c)}</code><small>{E(lib)}{" · " + E(DEJA_SERVI[c]) if c in DEJA_SERVI else ""}</small></td>'
        f'<td><input data-code="{E(c)}" placeholder="donné à… (un prénom ou un surnom)"></td>'
        f'<td><button type="button" data-msg="{E(c)}">Copier le message</button></td>'
        f'<td><button type="button" data-lien="{E(c)}">Copier le lien seul</button></td></tr>' for c, lib in codes)
    boutons = "".join(f'<button type="button" data-l="{l}" aria-pressed="{str(i == 0).lower()}">en {nom}</button>'
                      for i, (l, nom, _) in enumerate(t["msgs"]))
    msgs = "".join(f'<div class="msg" data-texte="{l}"{"" if i == 0 else " hidden"}>{E(m.replace("{DEPLIANT}", app + "presentation.html"))}</div>'
                   for i, (l, _, m) in enumerate(t["msgs"]))
    faire = "".join(f"<li>{x}</li>" for x in t["faire"])
    corps = f"""<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{t['eyebrow']}</p>
<h1>{E(t['titre'])}</h1>
<p class="chapeau">La formule de Compostelle : <strong>l'application est publique et gratuite</strong>, sauf {E(t['jeu'])}.
Chaque proche reçoit un lien qui porte déjà son <strong>code d'essai</strong> (le jeu de rôle s'ouvre sans rien taper),
l'adresse d'avis est au bas de chaque écran, et le <strong>dépliant public</strong> explique l'outil en une page.
Rien n'est vendu tant que les clés Stripe ne sont pas posées : l'offre d'achat ne paraît pas.</p>

<section class="premier">
  <h2>Les trois liens</h2>
  <div class="liens">
    <a class="lien" href="{app}" target="_blank" rel="noopener"><b>L'application</b>
      <span>Ouverte à tous, sans compte. Sans code, tout marche sauf {E(t['jeu'])}.</span><code>{app}</code></a>
    <a class="lien" href="{app}?code={E(codes[0][0])}" target="_blank" rel="noopener"><b>L'application, avec un code</b>
      <span>Le lien à envoyer : <code style="display:inline">?code=</code> ouvre {E(t['jeu'])} directement. Chaque proche a le sien.</span><code>{app}?code=…</code></a>
    <a class="lien" href="{app}presentation.html" target="_blank" rel="noopener"><b>Le dépliant, public</b>
      <span>Comment ça marche, en une page, avec le prix. La même page que celle du classeur.</span><code>{app}presentation.html</code></a>
  </div>
</section>

<section>
  <h2>Faut-il un code ?</h2>
  <ul class="simple">
    <li><b>Non, pour presque tout</b> : les mots, les exercices, le test, la fiche. Aucun compte, aucun mot de passe.</li>
    <li><b>Oui, pour {E(t['jeu_long'])}</b>, parce que chaque conversation coûte. Les huit codes ci-dessous sont gratuits :
      {n} conversations chacun, jusqu'au {fin} inclusivement, voix comprises. Au pire, tous épuisés : environ 16 $ US.</li>
    <li>Après le lancement, le même jeu de rôle s'achète dans l'application, comme « Parler librement » de Compostelle, au même prix.</li>
  </ul>
</section>

<section>
  <h2>Les codes d'essai</h2>
  <p style="font-size:14.5px;color:var(--muted)">Un code par personne. Notez à qui vous l'avez donné : c'est gardé dans ce navigateur seulement.
  « Copier le message » copie le message dans la langue choisie plus bas, avec le lien et le code déjà écrits.</p>
  <table class="codes"><thead><tr><th>Code</th><th>Donné à</th><th></th><th></th></tr></thead><tbody>{lignes}</tbody></table>
</section>

<section>
  <h2>Le message à envoyer</h2>
  <div class="rang">{boutons}</div>
  {msgs}
  <p style="font-size:14.5px;color:var(--muted);margin-top:8px">« {{LIEN}} » et « {{CODE}} » sont remplis quand vous copiez depuis le tableau.</p>
</section>

<section>
  <h2>Ce que vos proches ont à faire</h2>
  <ol class="etapes">{faire}</ol>
</section>

<section>
  <h2>Où arrivent les avis, et après</h2>
  <ul class="simple">
    <li>Les avis arrivent à <b>support@edufrancis.ca</b>, redirigée vers votre Gmail. <b>Gmail ne montre pas un courriel que vous vous
      envoyez à vous-même</b> par une redirection : pour vérifier, écrivez depuis une autre adresse.</li>
    <li>L'application n'est <b>pas indexée</b> par les moteurs de recherche pendant l'essai.</li>
    <li>Les codes cessent de fonctionner après le {fin}. Pour en couper un plus tôt, dites-le-moi.</li>
    <li>Transférez-moi les avis : je les trie et je corrige, comme une boucle d'audit.</li>
  </ul>
  <div class="garde" style="margin-top:12px"><b>À ne pas confondre :</b> le pilote <em>en entreprise</em> (un formateur, un groupe
  d'employés, deux séances) a sa propre page au classeur. Celle-ci ne sert qu'à faire essayer l'outil à des proches.</div>
</section>
</div>
<script>
(function(){{
  const APP = {app!r}, T = {{}};
  document.querySelectorAll('.msg[data-texte]').forEach(m => T[m.dataset.texte] = m.textContent);
  let l = 'fr';
  document.querySelectorAll('.rang button[data-l]').forEach(b => b.onclick = () => {{
    l = b.dataset.l;
    document.querySelectorAll('.rang button[data-l]').forEach(x => x.setAttribute('aria-pressed', String(x === b)));
    document.querySelectorAll('.msg[data-texte]').forEach(m => m.hidden = m.dataset.texte !== l);
  }});
  const copier = (t, b) => navigator.clipboard.writeText(t).then(() => {{ const o = b.textContent; b.textContent = 'Copié ✓'; setTimeout(() => b.textContent = o, 1500); }});
  const lien = c => APP + '?code=' + c;
  document.querySelectorAll('button[data-msg]').forEach(b => b.onclick = () => copier(T[l].split('{{LIEN}}').join(lien(b.dataset.msg)).split('{{CODE}}').join(b.dataset.msg), b));
  document.querySelectorAll('button[data-lien]').forEach(b => b.onclick = () => copier(lien(b.dataset.lien), b));
  document.querySelectorAll('input[data-code]').forEach(i => {{
    const k = 'essai-metier:' + i.dataset.code;
    try {{ i.value = localStorage.getItem(k) || ''; }} catch(e) {{}}
    i.oninput = () => {{ try {{ localStorage.setItem(k, i.value); }} catch(e) {{}} }};
  }});
}})();
</script>
</body>
</html>
"""
    sortie = RACINE / "assets" / "presentations" / t["sortie"]
    sortie.write_text(tete + corps, encoding="utf-8")
    print(sortie.relative_to(RACINE), f"— {len(codes)} codes, {len(t['msgs'])} messages, jusqu'au {fin}")


def main():
    fin, n = date_fr(pelerins.ESSAI_FIN), pelerins.ESSAI_CONVERSATIONS
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    for t in trousses(fin, n):
        construire(t, fin, n, tete)


if __name__ == "__main__":
    main()
