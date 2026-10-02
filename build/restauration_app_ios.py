"""La page de décision « Chez Jocelyne en application iPhone » — produite, jamais éditée.

Daniel, 1er oct. 2026 : « si on décidait d'en faire une app iOS ? », puis « oui, fais cela »
(la mettre sur une page du classeur). Trois voies, ce qu'Apple exige, le paiement, six décisions
et un export. Sortie : assets/presentations/restauration/restauration-app-ios.html.

Les règles d'Apple citées (4.2 fonctionnalité minimale, 3.1.1 achat intégré, 3.1.3(c) services
aux entreprises, programme des petites entreprises à 15 %, applications sur mesure par Apple
Business Manager) sont celles de l'App Store Review Guidelines ; elles changent : la page dit
« à vérifier avant de lancer », comme pour le financement public des trousses.
"""
import html, importlib.util, json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
PAGE = RACINE / "assets" / "presentations" / "restauration" / "restauration-app-ios.html"
E = html.escape


def _charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


ID = _charger("ai_identite", CONTENU / "identite.py")
LX = _charger("ai_lexique", CONTENU / "lexique.py")
SI = _charger("ai_situations", CONTENU / "situations.py")

# Les chiffres se lisent sur le disque, jamais écrits à la main.
N_MOTS = len(LX.LEXIQUE)
N_SIT = len(SI.SITUATIONS) if hasattr(SI, "SITUATIONS") else 8
# Ce que l'application emporterait : l'écran ET ses médias (servis depuis assets/interactive/restaurant/).
_DOSSIERS = [RACINE / "modules-autonomes" / "restaurant-planches", RACINE / "assets" / "interactive" / "restaurant"]
_FICHIERS = [f for d in _DOSSIERS if d.exists() for f in d.rglob("*") if f.is_file() and not f.name.endswith(".png")]
N_MP3 = sum(1 for f in _FICHIERS if f.suffix == ".mp3")
MO = round(sum(f.stat().st_size for f in _FICHIERS) / 1e6)

VOIES = [
    ("1. Ce qu'on a déjà : le site installable",
     "« Ajouter à l'écran d'accueil » dans Safari : une icône, le plein écran, le même écran que sur le Web.",
     "0 $", "Aucun travail.",
     "Rien dans l'App Store : il faut montrer le geste à chaque employé. Safari limite la place gardée hors ligne, "
     "et la dictée du navigateur est la partie la plus fragile sur iPhone."),
    ("2. Une coquille autour de la page (recommandé)",
     "Le même écran, emballé par Capacitor : les mots, les voix et les images dans l'application, le micro et la "
     "reconnaissance vocale d'Apple branchés en natif. Le même emballage sort une application Android.",
     "99 $ US par an (compte Apple) + 25 $ US une fois (Google)", "Quelques jours, puis la révision d'Apple.",
     "Apple refuse une page web simplement emballée (règle 4.2) : le hors-ligne complet et la dictée native sont "
     "ce qui la justifie. Une mise à jour du contenu passe par une nouvelle version, sauf si l'application va "
     "chercher le contenu au serveur."),
    ("3. Une application native (SwiftUI)",
     "Réécrire l'écran, les exercices, le test et le service en Swift.",
     "99 $ US par an", "Des semaines, puis chaque correction faite deux fois.",
     "Deux versions de la trousse à tenir à jour pour toujours, et rien pour Android. Ce que la méthode des trousses "
     "évite partout ailleurs : deux sources pour une même idée."),
]

DECISIONS = [
    {"k": "voie", "q": "La voie",
     "o": [["pwa", "Rester au site installable", False],
           ["coquille", "Une coquille autour de la page (iPhone et Android)", True],
           ["natif", "Une application native en Swift", False]],
     "w": "La coquille garde une seule source : les générateurs produisent l'écran, l'application l'emporte tel quel."},
    {"k": "quand", "q": "Le moment",
     "o": [["apres", "Après le pilote réel, une fois connus les téléphones des employés", True],
           ["maintenant", "Maintenant, en parallèle du pilote", False]],
     "w": "Une question au pilote (« iPhone ou Android ? ») décide si l'iPhone vaut le premier effort. Le pilote peut "
          "se faire sur le site installable, sans attendre Apple.",
     "champ": "Ce que vous savez déjà des téléphones de vos employés (facultatif)"},
    {"k": "plateformes", "q": "Les plateformes",
     "o": [["deux", "iPhone et Android, du même emballage", True],
           ["ios", "iPhone seulement", False]],
     "w": "En cuisine, beaucoup d'employés ont un téléphone Android. L'emballage est le même ; Android coûte surtout "
          "un second passage de vérification."},
    {"k": "distribution", "q": "Comment les employés l'obtiennent",
     "o": [["surmesure", "Application sur mesure : l'employeur l'installe (Apple Business Manager, Play géré)", True],
           ["public", "Dans l'App Store public, visible de tous", False],
           ["testflight", "Par TestFlight, pour le pilote seulement", False]],
     "w": "La trousse se vend aux employeurs : l'application sur mesure n'est visible que de l'entreprise qui l'a "
          "achetée. L'App Store public demanderait un achat dans l'application pour quiconque la télécharge seul."},
    {"k": "paiement", "q": "Le paiement",
     "o": [["employeur", "Vendu à l'employeur, hors de l'application, comme aujourd'hui", True],
           ["apple", "Achat dans l'application chez Apple (15 % prélevés)", False],
           ["les_deux", "Les deux : l'employeur hors de l'application, la personne seule chez Apple", False]],
     "w": "Apple exige son propre paiement pour un contenu numérique acheté par une personne (règle 3.1.1). Une "
          "application vendue directement à une organisation pour ses employés y échappe (règle 3.1.3(c)). Les "
          "codes « PC » vendus aux pèlerins de Compostelle, eux, tomberaient sous la règle d'Apple."},
    {"k": "contenu", "q": "La mise à jour du contenu",
     "o": [["serveur", "Les mots et les voix dans l'application, les corrections tirées du serveur", True],
           ["embarque", "Tout dans l'application : une correction = une nouvelle version", False]],
     "w": "La relecture des onze langues va corriger des textes après la sortie : sans le serveur, chaque correction "
          "attendrait la révision d'Apple (un à deux jours)."},
]


def page():
    voies = "".join(
        f'<div class="dec2"><p class="dq">{E(t)}</p><p>{E(quoi)}</p>'
        f'<table class="cmp"><tbody><tr><td><b>Coût</b></td><td>{E(cout)}</td></tr>'
        f'<tr><td><b>Travail</b></td><td>{E(trav)}</td></tr>'
        f'<tr><td><b>Ce qui coince</b></td><td>{E(pb)}</td></tr></tbody></table></div>'
        for t, quoi, cout, trav, pb in VOIES)
    tete = (RACINE / "assets" / "presentations" / "magasin-vetements-plan.html").read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", f"<title>{E(ID.NOM)} en application</title>", tete)
    tete = tete.replace("</style>", """
.champ{font:inherit;font-size:15px;width:100%;padding:8px 10px;border:1px solid var(--line-fort);border-radius:8px;
  background:var(--card);color:var(--ink);margin-top:10px;box-sizing:border-box}
table.cmp{display:table;width:100%;min-width:0}
.cmp td{overflow-wrap:anywhere;vertical-align:top}
.cmp td:first-child{width:9em}
</style>""", 1)
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html#restauration"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">{E(ID.NOM)} &middot; une application ?</p>
<h1>En faire une application iPhone</h1>
<p class="chapeau">L'écran des planches marche déjà sur un téléphone, dans le navigateur. La question est de savoir
si une vraie application vaut l'effort : trois voies, ce qu'Apple exige, puis six décisions.</p>

<section>
  <h2>Ce que l'application emporterait</h2>
  <p>L'écran tel que les générateurs le produisent : {N_MOTS} mots, {N_MP3} fichiers de voix, les croquis et
  le décor, environ {MO} Mo en tout. Hors ligne, les mots, les exercices et le test marchent entièrement.
  <b>Le service (le jeu de rôle) a toujours besoin du réseau</b> : les clients et le bilan passent par le serveur.</p>
</section>

<section>
  <h2>Les trois voies</h2>
  {voies}
</section>

<section>
  <h2>Ce qu'Apple exige</h2>
  <table class="cmp"><tbody>
  <tr><td><b>Plus qu'une page</b></td><td>Une page web emballée est refusée (règle 4.2). Le hors-ligne complet et la
  dictée native en font une application.</td></tr>
  <tr><td><b>Le paiement</b></td><td>Un contenu numérique acheté par une personne passe par Apple (règle 3.1.1),
  15 % prélevés pour une petite entreprise. Vendu à une organisation pour ses employés, il peut se payer ailleurs
  (règle 3.1.3(c)).</td></tr>
  <tr><td><b>La vie privée</b></td><td>Une fiche à remplir chez Apple : le micro, la voix envoyée au service
  d'assistance, ce qui est gardé. La <a href="/confidentialite.html">politique de confidentialité</a> existe ; elle
  devra nommer l'application (Loi 25).</td></tr>
  <tr><td><b>La révision</b></td><td>Chaque version est relue par Apple, en général en un à deux jours.</td></tr>
  </tbody></table>
  <div class="reserve"><p><strong>À vérifier avant de lancer :</strong> les règles d'Apple changent, et la
  distinction entre une vente à une organisation et une vente à une personne s'apprécie au cas par cas. Relire les
  règles en vigueur le jour où l'on soumet.</p></div>
</section>

<section>
  <h2>Six décisions</h2>
  <div id="decisions"></div>
  <p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<div class="pied"><p>Page produite par <code>build/restauration_app_ios.py</code> — ne pas l'éditer.</p></div>
</div>
<script>
(function(){{
  var D={json.dumps(DECISIONS, ensure_ascii=False)};
  var CLE='restauration-app-ios', s={{choix:{{}},champ:{{}}}};
  try{{var l=JSON.parse(localStorage.getItem(CLE)||'null');if(l&&l.choix)s=l;}}catch(e){{}}
  function sv(){{try{{localStorage.setItem(CLE,JSON.stringify(s));}}catch(e){{}}}}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){{
    var div=document.createElement('div');div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p>';
    if(d.o.length){{h+='<div class="opts">';d.o.forEach(function(o){{h+='<button type="button" class="opt" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'+o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';}});h+='</div>';}}
    if(d.champ)h+='<input class="champ" type="text" data-c="'+d.k+'" placeholder="'+d.champ+'">';
    div.innerHTML=h+'<p class="dw">'+d.w+'</p>';zone.appendChild(div);
  }});
  zone.querySelectorAll('[data-c]').forEach(function(x){{x.value=s.champ[x.dataset.c]||'';x.oninput=function(){{s.champ[x.dataset.c]=x.value;sv();peindre();}};}});
  function peindre(){{
    zone.querySelectorAll('.opt').forEach(function(b){{b.setAttribute('aria-pressed',s.choix[b.dataset.k]===b.dataset.v?'true':'false');}});
    var n=D.filter(function(d){{return s.choix[d.k];}}).length;
    document.getElementById('etat').textContent=n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }}
  zone.addEventListener('click',function(e){{var b=e.target.closest('.opt');if(!b)return;
    if(s.choix[b.dataset.k]===b.dataset.v)delete s.choix[b.dataset.k];else s.choix[b.dataset.k]=b.dataset.v;sv();peindre();}});
  document.getElementById('exporter').addEventListener('click',function(){{
    var out={{page:'restauration-app-ios',date:new Date().toISOString().slice(0,10),decisions:{{}}}};
    D.forEach(function(d){{var o=d.o.filter(function(x){{return x[0]===s.choix[d.k];}})[0];
      out.decisions[d.k]={{choix:o?o[0]:null,libelle:o?o[1]:null,texte:(s.champ[d.k]||'').trim()||null}};}});
    var t=JSON.stringify(out,null,2),fin=function(){{document.getElementById('etat').textContent='Copié — recollez-le-moi.';}};
    if(navigator.clipboard)navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}});else prompt('Copiez :',t);
  }});
  peindre();
}})();
</script>
</body></html>"""
    PAGE.write_text(tete + corps, encoding="utf-8")


if __name__ == "__main__":
    page()
    print(f"{PAGE.relative_to(RACINE)} — {N_MOTS} mots, {N_MP3} MP3, ~{MO} Mo, {len(DECISIONS)} décisions")
