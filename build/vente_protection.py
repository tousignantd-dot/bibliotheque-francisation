#!/usr/bin/env python3
"""Vendre au public sans s'exposer : la page de décision et le brouillon des conditions de vente.

    python3 build/vente_protection.py   # → assets/presentations/vente-protection.html

Question de Daniel, 28 sept. 2026, avant d'ouvrir le compte Stripe : « est-ce
qu'il y a des chances que je puisse avoir des poursuites contre moi ? […] une
structure à mettre en place […] pour que je n'aie pas de recours personnel ? »
Puis : « prépare la page de décision avec les conditions de vente », et « connais-
tu des assureurs ? ». Il a aussi décidé, le même jour, de retirer toute l'allergie
de Compostelle (« c'est la responsabilité de chacun »).

Ce n'est PAS un avis juridique : la page prépare la rencontre avec un avocat. Les
obligations de vente à distance viennent des pages de l'Office de la protection du
consommateur, lues le 28 sept. 2026 ; ce qui n'a pas été lu à la source est dit
« à faire confirmer ». Les montants du brouillon sont relus dans pelerins.offre().
"""
import html, importlib.util, json, pathlib, re, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

SOURCE = RACINE / "assets" / "presentations" / "hotellerie-prix.html"
SORTIE = RACINE / "assets" / "presentations" / "vente-protection.html"
E = html.escape
TROU = re.compile(r"\{(\w+)\}")
MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def prix(c):
    return f"{c / 100:.2f}".replace(".", ",") + " $"


def charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


# (clé, question, [(valeur, libellé, recommandé)], pourquoi)
DECISIONS = [
    ("forme", "La forme juridique pour vendre",
     [("ei", "Une entreprise individuelle immatriculée (environ 41 $), sous un nom neutre", True),
      ("societe", "Une société par actions tout de suite", False),
      ("nom-propre", "En mon nom, sans immatriculer", False)],
     "Une société protège des dettes et des contrats, <b>pas de votre propre faute</b> : si c'est vous qui avez "
     "écrit le contenu fautif, on peut vous poursuivre personnellement, société ou pas. Contre ce risque-là, c'est "
     "l'assurance qui protège. L'entreprise individuelle donne un nom au vendeur, sur le reçu et dans Stripe, pour le "
     "centième du coût d'une société. Déclencheur pour passer en société (analyse du 1er septembre) : un deuxième "
     "produit ou un premier client privé — trois produits au public s'en approchent, question à poser à l'avocat."),
    ("nom", "Le nom de l'entité (celui du reçu)",
     [("trame", "Trame", True), ("cordee", "Cordée", False), ("tuilage", "Tuilage", False), ("autre", "Un autre nom", False)],
     "Les trois candidats du 1er septembre, choisis pour ne pas dire le produit. Trame : la structure sous le tissu, "
     "donc le moteur commun ; « trama » a le même sens en espagnol. Avant de l'immatriculer : le registre des "
     "entreprises (nom trop proche refusé) et la base des marques de commerce."),
    ("assurance", "L'assurance, avant la première vente",
     [("trois", "Générale, professionnelle et cyber — la professionnelle et la cyber chez le même assureur", True),
      ("pro-cyber", "Professionnelle et cyber seulement", False),
      ("plus-tard", "Plus tard, après les premières ventes", False)],
     "2 000 à 4 000 $ par année pour les trois (relevé du 2 septembre). Deux pièges : la <b>date de rétroactivité</b> "
     "(elle doit couvrir le début réel de la plateforme, pas le jour de la signature) et l'intervalle entre deux "
     "assureurs quand une faute de programmation cause une fuite. Aucune police ne paie une amende ni une faute "
     "intentionnelle."),
    ("remboursement", "La politique de remboursement",
     [("14j-peu-utilise", "14 jours, si 3 conversations ou moins ont servi", True),
      ("30j", "Satisfait ou remboursé, 30 jours, quel que soit l'usage", False),
      ("loi-seulement", "Aucun remboursement hors des cas prévus par la loi", False)],
     "La loi laisse libre de fixer sa politique, à condition de l'annoncer <b>avant</b> l'achat et de la respecter. "
     "À 9,99 $, une contestation de carte coûte plus cher en temps que le remboursement ; une politique claire et "
     "généreuse évite les rétrofacturations. Le seuil de 3 conversations empêche d'utiliser tout le code puis de "
     "se faire rembourser."),
    ("paiement", "Les moyens de paiement acceptés",
     [("credit", "Carte de crédit seulement", True), ("tout", "Tout ce que Stripe offre (débit, portefeuilles…)", False)],
     "Selon l'Office, dans un contrat à distance, on ne peut percevoir un paiement avant de fournir le service "
     "<b>que par carte de crédit</b>. Le code est fourni à l'instant du paiement, ce qui peut suffire ; à faire "
     "confirmer. En attendant, la carte de crédit seule est le choix sûr, et elle ouvre la rétrofacturation, que la "
     "loi prévoit."),
    ("acheteur", "Le nom et l'adresse de l'acheteur, que le contrat doit porter",
     [("stripe", "Stripe les demande au paiement et les porte sur le reçu ; nous ne les recevons pas", True),
      ("nous", "Nous les recevons et les gardons", False)],
     "L'Office dit que le contrat à distance doit porter <b>le nom et l'adresse du consommateur</b>, et qu'un "
     "exemplaire doit lui être transmis dans les 15 jours. Stripe Checkout peut exiger l'adresse de facturation et "
     "envoyer le reçu. Nous tenons ainsi la promesse de la page de confidentialité (« nous ne voyons ni votre nom, "
     "ni votre courriel ») : à faire confirmer par l'avocat, c'est le point le plus délicat."),
    ("accepter", "L'acceptation des conditions",
     [("case", "Une case « J'ai lu les conditions » obligatoire au paiement (Stripe), et le lien sous l'offre", True),
      ("lien", "Le lien sous l'offre seulement", False)],
     "L'Office demande que les renseignements soient portés <b>expressément</b> à la connaissance du consommateur, "
     "par exemple en le faisant passer par une page qui les contient. La case de Stripe Checkout (conditions "
     "d'utilisation) fait exactement ça, sans rien coder chez nous."),
    ("age", "L'âge",
     [("18-ou-parent", "Réservé aux majeurs, ou avec l'accord d'un parent", True), ("aucune", "Aucune mention", False)],
     "Un contrat avec une personne mineure peut être annulé pour lésion. La mention coûte une ligne."),
    ("taxes", "La TPS et la TVQ",
     [("petit-fournisseur", "Petit fournisseur : pas d'inscription tant que les ventes restent sous 30 000 $ par année", True),
      ("inscrit", "S'inscrire tout de suite", False)],
     "Sous 30 000 $ de ventes taxables sur quatre trimestres, l'inscription est facultative. Le seuil compte "
     "<b>toutes</b> vos ventes, pilotes en entreprise compris : à surveiller dès qu'un contrat d'entreprise se signe. "
     "La page de vente doit dire si les taxes s'appliquent."),
    ("avocat", "La relecture par un avocat",
     [("avant", "Une heure avec un avocat avant d'ouvrir la vente, ce brouillon en main", True),
      ("apres", "Après les premières ventes", False)],
     "Le brouillon ci-dessous et les questions de la dernière section tiennent en une rencontre. Le Barreau du "
     "Québec a un service de référence ; certains avocats offrent une première consultation à prix fixe."),
]

ASSUREURS = [
    ("Passer par un courtier en assurance de dommages des entreprises", "le chemin recommandé",
     "Un courtier compare plusieurs assureurs et place les risques moins courants — une plateforme éducative qui vend en "
     "ligne et fait parler une IA en est un. Vérifiez qu'il est inscrit au registre de l'Autorité des marchés financiers "
     "(AMF). Demandez-lui : responsabilité civile générale, erreurs et omissions « technologie » et cyberrisque, "
     "idéalement dans une même police « Tech E&O », avec une date de rétroactivité qui couvre le début de la plateforme."),
    ("Les grands assureurs d'entreprises au Québec", "par un courtier ou en direct",
     "Intact Assurance, Desjardins Assurances (entreprises), Northbridge, Travelers Canada, Chubb, Aviva Canada. "
     "Tous ont des produits pour petites entreprises de services ; la cyber et les erreurs et omissions « technologie » "
     "ne sont pas offertes partout ni à tout profil."),
    ("Les spécialistes technologie et cyber", "presque toujours par un courtier",
     "CFC Underwriting (erreurs et omissions technologie et cyber, très présent au Canada), Coalition (cyber), "
     "Beazley. Ce sont souvent eux qui assurent les petites entreprises de logiciel."),
    ("Les courtiers en ligne pour petites entreprises", "rapide pour une première soumission",
     "Zensurance, APOLLO Insurance : une soumission en ligne en quelques minutes, surtout pour la générale et les "
     "erreurs et omissions. Vérifiez qu'ils sont inscrits à l'AMF pour le Québec, et lisez les exclusions liées à "
     "l'IA et aux données."),
]

QUESTIONS_AVOCAT = [
    "Le reçu de Stripe, avec le lien vers les conditions et le nom et l'adresse que Stripe demande, suffit-il comme "
    "« exemplaire du contrat » transmis dans les 15 jours, sans que nous recevions nous-mêmes le nom et l'adresse ?",
    "Un code fourni à l'instant du paiement est-il un service « fourni » avant le paiement, ce qui permettrait le "
    "débit ? Sinon, la carte de crédit seule suffit-elle ?",
    "L'entreprise individuelle suffit-elle pour vendre trois produits au public, ou faut-il la société dès maintenant ?",
    "La phrase « ne donnent aucun conseil médical, juridique ou de sécurité » est-elle utile, sachant qu'on ne peut "
    "pas exclure sa responsabilité pour sa propre faute envers un consommateur ?",
    "Les personnages animés par une IA : faut-il une mention de plus, au Québec, ou pour des acheteurs d'Europe "
    "(pèlerins français, par exemple) ?",
    "Les conditions offertes en anglais et en espagnol à côté du français (Hôtel Rive-Claire) : la mention « la "
    "version française prévaut » est-elle suffisante au regard de la Charte de la langue française ?",
]


def main():
    CV = charger("vp_conditions", RACINE / "build" / "contenu" / "vente" / "conditions.py")
    CV.verifier()
    o = pelerins.offre()
    trou = lambda nom: f'<mark class="trou">à remplir : {E(nom)}</mark>'
    v = CV.VENDEUR
    promo = (f"{prix(o['prix'])} au lieu de {prix(o['prixRegulier'])}, prix de lancement jusqu'au {date_fr(o['promoFin'])} inclusivement."
             if o["promo"] else f"{prix(o['prix'])}.")
    recommande = {k: next(val for val, _, r in opts if r) for k, _, opts, _ in DECISIONS}
    remplir = {
        "vendeur_nom": E(v["nom"]) or trou("nom de l'entreprise"), "vendeur_neq": ("NEQ " + E(v["neq"])) if v["neq"] else trou("NEQ"),
        "vendeur_adresse": E(v["adresse"]) or trou("adresse postale"), "vendeur_telephone": E(v["telephone"]) or trou("téléphone"),
        "vendeur_courriel": E(v["courriel"]),
        "conversations": str(o["conversations"]), "mois": str(o["jours"] // 30), "tours": str(o["toursMax"]),
        "parjour": str(o["parJour"]), "prix_ligne": "Le prix d'un code est de " + E(promo),
        "recharge_conv": str(o["rechargeConversations"]), "recharge": prix(o["recharge"]),
        "conservation": str(o["conservation"]),
        "taxes": E(CV.VARIANTES["taxes"][recommande["taxes"]]),
        "remboursement": E(CV.VARIANTES["remboursement"][recommande["remboursement"]]),
        "age": E(CV.VARIANTES["age"][recommande["age"]]),
    }
    sections = ""
    for i, (titre, ps) in enumerate(CV.SECTIONS, 1):
        poser = lambda t: TROU.sub(lambda m: remplir[m.group(1)], t)
        corps = "".join("<p>" + poser(E(p)) + "</p>" for p in ps if poser(p).strip())
        sections += f"<h3>{i}. {E(titre)}</h3>{corps}"
    manque = [k for k in ("nom", "neq", "adresse", "telephone") if not v[k]]

    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", "<title>Vendre au public — se protéger</title>", tete)
    tete = tete.replace("</head>", """<style>
.conditions{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:18px 22px;font-size:15.5px}
.conditions h3{font-size:16.5px;margin:18px 0 6px;color:var(--ink)} .conditions h3:first-child{margin-top:0}
.conditions p{margin:0 0 8px;max-width:72ch}
mark.trou{background:var(--decid-bg);color:var(--decid);border:1px dashed var(--decid);border-radius:6px;padding:0 5px;font-weight:700}
.risques{counter-reset:r;list-style:none;padding:0;margin:0}
.risques li{counter-increment:r;position:relative;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px 12px 50px;margin:8px 0;font-size:15.5px}
.risques li::before{content:counter(r);position:absolute;left:14px;top:12px;width:24px;height:24px;border-radius:50%;background:var(--decid-bg);color:var(--decid);font-weight:900;display:grid;place-items:center;font-size:13px}
.risques li.fait::before{content:"✓";background:var(--fait-bg);color:var(--fait)}
.assur{display:grid;gap:10px}
.assur div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;font-size:15px}
.assur b{color:var(--ink)} .assur em{font-style:normal;color:var(--muted);font-size:13.5px;margin-left:6px}
</style>
</head>""")
    corps = f"""<body><div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Vente au public &middot; Compostelle, Maison Francœur, Hôtel Rive-Claire</p>
<h1>Vendre au public sans s'exposer</h1>
<div class="these"><p class="cle">Ce qui protège le plus une personne qui vend seule, c'est l'assurance, un contenu vérifié et des
conditions de vente claires. Une société protège des dettes, pas de sa propre faute ; elle viendra plus tard.</p></div>
<p class="chapeau">Page préparée pour décider avant d'ouvrir le compte Stripe, et pour une heure avec un avocat. <b>Ce n'est pas un avis
juridique.</b> Les règles de la vente à distance viennent des pages de l'Office de la protection du consommateur, lues le
28 septembre 2026 ; le reste est à faire confirmer.</p>

<section>
  <h2>D'où viendrait une poursuite</h2>
  <ol class="risques">
    <li class="fait"><b>Un tort causé par le contenu</b> — le plus sérieux, et surtout la carte d'allergie de Compostelle : une phrase fausse, et
      c'est un préjudice corporel. <b>Décidé le 28 septembre : l'allergie est retirée</b> de l'application. Restent les urgences (le 112) et la
      pharmacie, à faire relire par un hispanophone.</li>
    <li><b>Les renseignements personnels (Loi 25)</b> — déjà très réduit : aucun compte, aucun courriel, rien de la personne chez nous ; Stripe
      tient la carte. C'est aussi un argument pour baisser la prime d'assurance.</li>
    <li><b>Les litiges d'achat</b> — remboursements et contestations de carte : petits montants, évités par une politique claire, annoncée avant.</li>
    <li><b>Ce qu'un personnage animé par l'IA dirait de travers</b> — faible, encadré par les consignes ; les conditions le disent.</li>
    <li><b>Une vente non conforme à la loi</b> — des renseignements manquants avant l'achat permettent au client d'annuler pendant 30 jours ;
      un exemplaire du contrat non transmis dans les 15 jours, en tout temps avant d'avoir reçu le service. Le brouillon ci-dessous y répond.</li>
  </ol>
</section>

<section>
  <h2>Ce que la loi demande avant l'achat</h2>
  <p>Selon l'Office, avant un contrat conclu par Internet, le commerçant donne, de façon évidente et avant le paiement :</p>
  <ul class="simple">
    <li>son nom, son adresse, son téléphone et son courriel — <b>d'où l'immatriculation et une adresse postale</b> ;</li>
    <li>une description détaillée du service, le prix, les taxes, le total, les modalités de paiement ;</li>
    <li>la date où le service est fourni, et les conditions d'annulation et de remboursement ;</li>
    <li>toute autre restriction (durée, plafond de conversations, par jour).</li>
  </ul>
  <p style="margin-top:10px">Le contrat doit ensuite porter le nom et l'adresse du consommateur et la date, et un exemplaire lui être transmis dans les
  15 jours, qu'il peut garder et imprimer. Le paiement d'avance n'est permis que par carte de crédit. Les décisions 5 à 7 règlent ces trois points.</p>
</section>

<section>
  <h2>Des assureurs pour la responsabilité</h2>
  <p>Je ne peux pas vous dire qui acceptera ce profil ni à quel prix : c'est le courtier qui le trouve. Voici où chercher.</p>
  <div class="assur">{"".join(f"<div><b>{E(t)}</b><em>{E(q)}</em><br>{E(d)}</div>" for t, q, d in ASSUREURS)}</div>
  <div class="reserve" style="margin-top:12px"><p><strong>À dire au courtier :</strong> trois applications d'apprentissage des langues, vendues au
  public par code (environ 10 $), aucun compte ni courriel, renseignements minimaux (effacés après expiration), paiement chez Stripe,
  personnages animés par une IA d'Anthropic, hébergement Railway. Moins on détient de dossiers, plus la prime baisse.</p></div>
</section>

<section>
  <h2>Les décisions</h2>
  <div id="decisions"></div>
  <p style="margin-top:14px"><b>Un mot</b> (facultatif) — une réponse de l'avocat, un nom d'assureur, une réserve :</p>
  <textarea id="note" rows="3"></textarea>
  <p style="margin-top:1.4rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>

<section>
  <h2>Le brouillon des conditions de vente</h2>
  <p>Écrit avec les options recommandées ; les montants sont ceux que la caisse facture aujourd'hui. {"Il manque " + str(len(manque)) + " renseignement" + ("s" if len(manque) > 1 else "") + " sur le vendeur, en ambre : ils arrivent avec l'immatriculation." if manque else ""}
  Une fois relu, il deviendra une page publique liée sous chaque offre d'achat.</p>
  <div class="conditions">{sections}<p style="color:var(--muted);font-size:13.5px;margin-top:14px">Conditions de vente — {E(CV.MISE_A_JOUR)}.</p></div>
</section>

<section>
  <h2>Les questions pour l'avocat</h2>
  <ol class="risques">{"".join(f"<li>{E(q)}</li>" for q in QUESTIONS_AVOCAT)}</ol>
</section>

<div class="pied"><p>Page produite par <code>build/vente_protection.py</code> — ne pas l'éditer. Le brouillon vit dans
<code>build/contenu/vente/conditions.py</code> ; les montants viennent de <code>pelerins.offre()</code>.</p></div>
</div>
<script>
(function(){{
  var D={json.dumps([{"k": k, "q": q, "o": [[v2, l, r] for v2, l, r in opts], "w": w} for k, q, opts, w in DECISIONS], ensure_ascii=False)};
  var CLE='vente-protection', s={{choix:{{}},montant:{{}},note:''}};
  try{{ var l=JSON.parse(localStorage.getItem(CLE)||'null'); if(l&&l.choix) s=l; }}catch(e){{}}
  function sv(){{ try{{ localStorage.setItem(CLE,JSON.stringify(s)); }}catch(e){{}} }}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){{
    var div=document.createElement('div'); div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p><div class="opts">';
    d.o.forEach(function(o){{
      h+='<button type="button" class="opt" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'+o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';
    }});
    h+='</div>';
    if(d.o.some(function(o){{return o[0]==='autre';}}))
      h+='<div class="autre" data-k="'+d.k+'"><label>Lequel : <input type="text" data-k="'+d.k+'"></label></div>';
    div.innerHTML=h+'<p class="dw">'+d.w+'</p>'; zone.appendChild(div);
  }});
  var note=document.getElementById('note'); note.value=s.note||'';
  note.addEventListener('input',function(){{ s.note=note.value; sv(); }});
  zone.querySelectorAll('input').forEach(function(i){{ i.value=s.montant[i.dataset.k]||''; i.addEventListener('input',function(){{ s.montant[i.dataset.k]=i.value; sv(); }}); }});
  function peindre(){{
    zone.querySelectorAll('.opt').forEach(function(b){{ b.setAttribute('aria-pressed', s.choix[b.dataset.k]===b.dataset.v?'true':'false'); }});
    zone.querySelectorAll('.autre').forEach(function(a){{ a.classList.toggle('ouvert', s.choix[a.dataset.k]==='autre'); }});
    var n=Object.keys(s.choix).length; document.getElementById('etat').textContent=n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }}
  zone.addEventListener('click',function(e){{
    var b=e.target.closest('.opt'); if(!b) return;
    if(s.choix[b.dataset.k]===b.dataset.v) delete s.choix[b.dataset.k]; else s.choix[b.dataset.k]=b.dataset.v;
    sv(); peindre();
  }});
  document.getElementById('exporter').addEventListener('click',function(){{
    var out={{page:'vente-protection', date:new Date().toISOString().slice(0,10), decisions:{{}}, note:s.note||''}};
    D.forEach(function(d){{ var v=s.choix[d.k], o=d.o.filter(function(x){{return x[0]===v;}})[0];
      out.decisions[d.k]= !o ? null : (v==='autre' ? {{choix:'autre', valeur:s.montant[d.k]||''}} : o[1]); }});
    var t=JSON.stringify(out,null,2);
    var fin=function(){{ document.getElementById('etat').textContent='Copié — recolle-le-moi.'; }};
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){{prompt('Copiez :',t);}}); else prompt('Copiez :',t);
  }});
  peindre();
}})();
</script>
</body></html>
"""
    SORTIE.write_text(tete + corps, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), f"— {len(DECISIONS)} décisions, {len(CV.SECTIONS)} sections de conditions, {len(manque)} trous")


if __name__ == "__main__":
    main()
