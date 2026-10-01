#!/usr/bin/env python3
"""Le pilote d'« Une semaine à Toronto » : faire essayer avant de vendre.

    python3 build/toronto_pilote.py   # → assets/presentations/toronto/toronto-pilote.html

Étape 7 (1er oct. 2026). Même formule que Compostelle (build/compostelle_pilote.py) :
l'application reste ouverte sans code ; seule la semaine jouée (l'assistance) demande
un code, et les huit codes d'essai de la trousse « toronto » sont lus dans pelerins.py
(la page ne promet jamais un code qui n'existe plus). Trois sortes d'essayeurs : cinq
faux débutants observés à voix haute (la boucle didactique prédit, l'essai mesure), un
relecteur anglophone canadien, et quelqu'un qui part pour vrai. La page dit aussi
comment TRIER les avis : les règles de décision, écrites avant de lire les réponses.
"""
import html, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"
SORTIE = RACINE / "assets" / "presentations" / "toronto" / "toronto-pilote.html"
SITE = "https://portail.edufrancis.ca"
APP = SITE + "/modules-autonomes/toronto/"
E = html.escape
MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def main():
    fin = date_fr(pelerins.ESSAI_FIN)
    n_conv = pelerins.ESSAI_CONVERSATIONS
    codes = [(c, lib) for c, (lib, t) in pelerins.CODES_ESSAI_TROUSSES.items() if t == "toronto"]
    assert codes, "aucun code d'essai « toronto » dans pelerins.py"

    msg_fr = f"""Bonjour !

Je prépare une application pour apprendre l'anglais qu'il faut à un touriste francophone pour une semaine à Toronto : le métro, l'hôtel, commander, payer, le restaurant (avec une allergie), la pharmacie, et bavarder avec les gens.

J'aimerais ton avis avant de la lancer. Elle s'ouvre dans le navigateur du téléphone, sans compte ni mot de passe :
{APP}

Ce qui m'aiderait (environ 45 minutes, en deux fois si tu veux) :
- le test « Prêt à partir ? » (un quart d'heure) ;
- une série d'exercices, par exemple « Le total à payer » ou « L'allergie » ;
- deux situations de « La semaine » : le café, puis le restaurant (il faut un code, plus bas) ;
- un coup d'œil à « Ma poche ».

Pour donner ton avis : « Donner mon avis », au bas de chaque écran (un courriel déjà préparé s'ouvre).

Pour jouer les situations avec l'assistance, voici ton code : {{CODE}} — {n_conv} conversations, valable jusqu'au {fin}.

Merci !
Daniel"""

    msg_en = f"""Hi!

I'm building a phone app that teaches French-speaking tourists from Quebec the English they need for a week in Toronto: the subway, the hotel, ordering, paying, a restaurant with a food allergy, the pharmacy, and small talk.

Before launch, I'd love a Canadian English speaker to check it. It opens in the phone's browser, no account needed:
{APP}

The menus are in French, but everything you hear and say is in English. What helps me most:
- Is each English sentence correct and natural in Toronto? Would a Torontonian say it that way?
- Do the voices sound right? Any odd word, accent or price?
- Note the sentence and the screen (« Les exercices », « La semaine », « Ma poche »...).

Good places to look: « Les mots » (12 boards), « Les exercices » (« Ce qu'on me répond », « Les prix et les heures »), and « Ma poche ».

To try the role-play with the AI playing people in Toronto (« La semaine », then a place, then « Jouer la situation »), here is your code: {{CODE}} — {n_conv} conversations, valid until {pelerins.ESSAI_FIN}.

Send your notes to support@edufrancis.ca (or use « Donner mon avis » at the bottom of each screen).

Thanks so much!
Daniel"""

    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Toronto — le pilote</title>", tete)
    tete = tete.replace("</head>", """<style>
.liens{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
.lien{display:block;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:var(--body)}
.lien b{display:block;color:var(--ink);font-size:16.5px;margin-bottom:4px}.lien span{font-size:14.5px}
.lien code{display:block;margin-top:6px;font-size:12.5px;color:var(--muted);word-break:break-all}
.msg{white-space:pre-wrap;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;font-size:14.5px;line-height:1.5;max-height:340px;overflow:auto}
.rang{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.rang button{font:inherit;font-weight:800;border-radius:10px;border:1px solid var(--line);background:#C8102E;color:#fff;padding:8px 14px;cursor:pointer}
.rang button.sec{background:var(--card);color:var(--ink)}
table.codes{width:100%;border-collapse:collapse;font-size:15px}
table.codes td,table.codes th{border-bottom:1px solid var(--line);padding:8px 6px;text-align:left}
table.codes code{font-size:16px;font-weight:900;letter-spacing:.06em}
table.codes input{font:inherit;width:100%;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:#fff}
ol.etapes{counter-reset:e;list-style:none;padding:0;margin:0}
ol.etapes>li{counter-increment:e;position:relative;padding:12px 14px 12px 52px;background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0;font-size:15.5px}
ol.etapes>li::before{content:counter(e);position:absolute;left:14px;top:12px;width:26px;height:26px;border-radius:50%;background:#C8102E;color:#13233B;font-weight:900;display:grid;place-items:center;font-size:14px}
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
<p class="eyebrow">Voyage &middot; grand public &middot; anglais</p>
<h1>Une semaine à Toronto &mdash; le pilote</h1>
<p class="chapeau">La formule de Compostelle : <strong>l'application reste ouverte, sans code</strong>. Rien n'y est verrouillé
(le faux débutant peut sauter ce qu'il sait). Seule <strong>la semaine jouée</strong> &mdash; l'assistance qui joue les gens de Toronto,
et la relecture des cartes postales &mdash; demande un code, parce que chaque conversation coûte : les huit codes d'essai ci-dessous
sont gratuits. Un bouton <strong>« Donner mon avis »</strong> est au bas de chaque écran.</p>

<section class="premier">
  <h2>Les liens</h2>
  <div class="liens">
    <a class="lien" href="{APP}" target="_blank" rel="noopener"><b>L'application</b><span>Le lien à envoyer.</span><code>{APP}</code></a>
    <a class="lien" href="{APP}#semaine" target="_blank" rel="noopener"><b>La semaine jouée</b><span>L'album, les dix lieux et Maya ; le code s'entre dans chaque situation.</span><code>{APP}#semaine</code></a>
    <a class="lien" href="{APP}#poche" target="_blank" rel="noopener"><b>Ma poche</b><span>Les phrases hors ligne, les urgences, le total à payer.</span><code>{APP}#poche</code></a>
  </div>
</section>

<section>
  <h2>Qui fait l'essai</h2>
  <ol class="etapes">
    <li><b>Cinq faux débutants francophones, observés.</b> Vous êtes à côté ; ils pensent à voix haute ; vous notez où ils hésitent, sans aider.
      Le parcours : le test (15 min), une série « L'allergie », une série « Le total à payer », puis le café et le restaurant dans « La semaine ».
      Cinq suffisent pour voir la plupart des défauts d'usage ; au-delà, on revoit les mêmes.</li>
    <li><b>Un relecteur anglophone canadien</b> (le message en anglais plus bas). La boucle didactique juge la didactique, pas l'anglais :
      c'est lui qui dit si une phrase « ne se dit pas à Toronto ».</li>
    <li><b>Quelqu'un qui part pour vrai.</b> Avant le départ : les séances et la semaine jouée ; sur place : la poche. Au retour, une seule
      question : « Qu'est-ce qui vous a servi, et qu'est-ce qui vous a manqué ? »</li>
  </ol>
</section>

<section>
  <h2>Les codes d'essai</h2>
  <p style="font-size:14.5px;color:var(--muted)">Un code par personne : {n_conv} conversations chacun, jusqu'au {fin} inclusivement. Au pire, les huit épuisés :
  environ 16 $ US. Notez à qui vous l'avez donné : c'est gardé dans ce navigateur seulement. « Copier le message » met le message en français, avec ce code.</p>
  <table class="codes"><thead><tr><th>Code</th><th></th><th>Donné à</th><th></th></tr></thead><tbody>{lignes}</tbody></table>
</section>

<section>
  <h2>Les messages à envoyer</h2>
  <div class="rang"><button type="button" id="copFr">Copier le message en français</button><button type="button" class="sec" id="copEs">Copier le message en anglais (relecteur)</button></div>
  <div class="msg" id="msgFr">{E(msg_fr)}</div>
  <p style="font-size:14.5px;color:var(--muted);margin-top:8px">« {{CODE}} » est remplacé par un code libre quand vous copiez depuis le tableau ; sinon, la phrase du code est retirée.</p>
  <details style="margin-top:10px"><summary><b>Le message en anglais</b></summary><div class="msg" id="msgEs" style="margin-top:8px">{E(msg_en)}</div></details>
</section>

<section>
  <h2>En observant : ce qu'on note</h2>
  <ul class="simple">
    <li>Chaque hésitation de plus de dix secondes, et l'écran où elle arrive.</li>
    <li>Chaque fois qu'on répond <b>sans écouter</b> (au hasard, à la longueur, par élimination) : c'est le défaut que cinq tours d'audit ont chassé.</li>
    <li>Au restaurant : dit-on l'allergie <b>avant</b> de commander, et en anglais ? Le bilan a-t-il jugé juste ?</li>
    <li>Le micro : comprend-il ? À quel moment passe-t-on au clavier ?</li>
    <li>Le temps réel d'une séance (prévu : 15 min) et d'une situation jouée.</li>
  </ul>
</section>

<section>
  <h2>Comment trier les avis : les règles, écrites avant de lire</h2>
  <ul class="simple">
    <li><b>Une question ratée par la moitié des essayeurs accuse la question</b>, pas les essayeurs : on la réécrit.</li>
    <li><b>Un bilan que l'observateur contredit est une donnée</b> : on le note avec la conversation (le bilan est un modèle, il se trompe).</li>
    <li><b>Une phrase anglaise contestée par le relecteur</b> se change, et son son se refait (le feu vert des voix vaut pour ces reprises).</li>
    <li><b>Une hésitation chez trois personnes sur cinq</b> au même écran : la consigne change.</li>
    <li><b>L'allergie</b> : un seul essayeur qui commande le plat douteux sans être arrêté par le bilan, et c'est un bloquant.</li>
  </ul>
  <div class="garde" style="margin-top:12px"><b>Avant d'envoyer :</b> écrivez-vous un avis d'essai par « Donner mon avis » pour vérifier que
  support@edufrancis.ca reçoit bien. Les avis, transférez-les-moi : je les trie selon ces règles et je corrige, comme un tour de boucle.</div>
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
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), f"— {len(codes)} codes, jusqu'au {fin}")


if __name__ == "__main__":
    main()
