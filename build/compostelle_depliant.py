#!/usr/bin/env python3
"""Le dépliant client d'« En route vers Compostelle » : comment l'outil fonctionne.

    python3 build/compostelle_depliant.py   # → assets/presentations/compostelle-depliant.html

Daniel, 27 sept. 2026 : « un petit document très visuel qui va expliquer aux
futurs clients comment fonctionne l'outil ». Le public est le pèlerin qui
hésite, pas l'équipe : aucune donnée interne (coûts, audits), des captures
réelles de l'application au format téléphone (compostelle-depliant/*.jpg,
prises par le protocole de Chrome à 390 px), et tout ce qui est compté
(haltes, kilomètres, séances, prix) relu dans le contenu et dans pelerins.py.
Imprimable : une feuille lettre recto verso, les couleurs gardées.
"""
import html, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
sys.path.insert(0, str(RACINE))
import compostelle_commun as C  # noqa: E402
import pelerins  # noqa: E402

SORTIE = RACINE / "assets" / "presentations" / "compostelle-depliant.html"
PUBLIC = RACINE / "modules-autonomes" / "compostelle" / "depliant"
CAP = "compostelle-depliant/"
MEDIA = "../interactive/compostelle/"
APP = "/modules-autonomes/compostelle/"
E = html.escape
KM_JOUR = 25


MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def main():
    etapes = C.charger("etapes").ETAPES
    seances = C.charger("preparation").SEANCES
    o = pelerins.offre()
    prix = lambda c: f"{c / 100:.2f}".replace(".", ",") + " $"
    km = etapes[-1]["km"]
    # Le même compte que joursMarche() de l'application, halte par halte.
    import math
    jours = sum(max(1, math.ceil((e["km"] - (etapes[i - 1]["km"] if i else 0)) / KM_JOUR - 0.2))
                for i, e in enumerate(etapes))

    haltes = "".join(
        f'<li><img src="{MEDIA}etapes/{E(e["img"])}.jpg" alt="" loading="lazy">'
        f'<span class="n">{e["n"]}</span><b>{E(e["lieu"])}</b><small>km {e["km"]}</small>'
        f'<em>{E(e["titre"])}</em></li>' for e in etapes)
    seance_li = "".join(f"<li>{E(s['titre'])}</li>" for s in seances)

    page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>En route vers Compostelle — comment ça marche</title>
<meta name="description" content="L’espagnol du Camino francés, dix étapes choisies, dans votre téléphone.">
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
:root{{--beige:#F3ECDD;--papier:#FBF7EE;--bleu:#1F4E9C;--bleu-f:#13233B;--jaune:#F2C230;--tampon:#9B2C2C;
 --texte:#2B2A26;--doux:#6B665C;--filet:#E2D8C3}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--beige);color:var(--texte);font:17px/1.5 Nunito,system-ui,sans-serif}}
.cadre{{max-width:1040px;margin:0 auto;padding:0 20px}}
a{{color:var(--bleu)}}
.retour{{display:inline-block;margin:14px 0 0;font-size:14px;color:var(--doux);text-decoration:none}}
.retour:hover{{color:var(--bleu)}}
.fr-barre{{background:#fff;border-bottom:3px solid var(--bleu)}}
.fr-barre__in{{max-width:1040px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}}
.secteur{{text-align:right;line-height:1.2}}
.secteur small{{display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--doux);font-weight:800}}
.secteur b{{color:var(--bleu);font-size:17px}}

/* la une */
.une{{display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:center;padding:34px 0 10px}}
.sur{{font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:900;color:var(--tampon);margin:0 0 8px}}
h1{{font-size:clamp(34px,5.4vw,56px);line-height:1.02;margin:0 0 14px;color:var(--bleu-f);letter-spacing:-.01em}}
h1 span{{background:linear-gradient(transparent 60%,rgba(242,194,48,.7) 60%)}}
.chapeau{{font-size:20px;line-height:1.45;margin:0 0 18px;color:#3A372F}}
.cta{{display:inline-block;background:var(--jaune);color:var(--bleu-f);font-weight:900;text-decoration:none;padding:13px 22px;border-radius:12px;font-size:17px}}
.cta:hover{{filter:brightness(.96)}}
.une .visuel{{position:relative;min-height:400px}}
.tel{{width:100%;max-width:250px;border-radius:30px;background:#111;padding:9px;box-shadow:0 18px 40px rgba(19,35,59,.25)}}
.tel img{{display:block;width:100%;border-radius:22px;aspect-ratio:390/760;object-fit:cover;object-position:top}}
.une .tel{{position:absolute}}
.une .tel.a{{left:0;top:0;transform:rotate(-4deg);max-width:230px}}
.une .tel.b{{right:0;top:40px;transform:rotate(4deg);max-width:230px}}
.tampon{{position:absolute;left:38%;bottom:-6px;width:120px;height:120px;border-radius:50%;border:4px solid var(--tampon);
 color:var(--tampon);display:grid;place-items:center;text-align:center;font-weight:900;font-size:13px;line-height:1.15;
 transform:rotate(-12deg);background:rgba(251,247,238,.9);letter-spacing:.06em;text-transform:uppercase;z-index:2}}
.tampon b{{display:block;font-size:30px;letter-spacing:0}}

/* chiffres */
.chiffres{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:34px 0 8px}}
.chiffres div{{background:var(--papier);border:1px solid var(--filet);border-radius:14px;padding:14px 16px}}
.chiffres b{{display:block;font-size:34px;line-height:1;color:var(--bleu);font-weight:900}}
.chiffres span{{font-size:14.5px;color:var(--doux)}}

section{{margin-top:58px}}
h2{{font-size:clamp(26px,3.6vw,36px);line-height:1.1;margin:0 0 8px;color:var(--bleu-f)}}
.intro{{font-size:18px;color:#3A372F;max-width:720px;margin:0 0 22px}}
.num{{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%;background:var(--jaune);color:var(--bleu-f);
 font-weight:900;font-size:19px;margin-right:12px;vertical-align:4px}}

/* trois temps */
.temps{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;counter-reset:t}}
.temps article{{background:var(--papier);border:1px solid var(--filet);border-radius:18px;padding:18px;position:relative}}
.temps article img.croq{{width:84px;height:84px;object-fit:contain;float:right;margin:-4px -4px 6px 8px;mix-blend-mode:multiply}}
.temps h3{{margin:0 0 4px;font-size:21px;color:var(--bleu-f)}}
.temps .quand{{font-size:13px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--tampon);margin:0 0 6px}}
.temps p{{margin:0;font-size:15.5px}}
.temps ul{{margin:10px 0 0;padding-left:18px;font-size:14.5px;color:#4A463D}}
.temps .fleche{{position:absolute;right:-17px;top:50%;width:18px;height:18px;color:var(--jaune);z-index:1}}

/* la halte */
.halte{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}}
.ecran{{text-align:center}}
.ecran .tel{{margin:0 auto 14px;max-width:236px}}
.phase{{display:inline-block;font-size:12.5px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;border-radius:99px;padding:4px 11px;margin-bottom:6px}}
.ph-1{{background:#E2EAF6;color:var(--bleu)}}
.ph-2{{background:#FBEFC4;color:#6B4E00}}
.ph-3{{background:#F4DEDC;color:var(--tampon)}}
.ecran h3{{margin:2px 0 4px;font-size:19px;color:var(--bleu-f)}}
.ecran p{{margin:0 auto;font-size:15px;max-width:290px;color:#4A463D}}
.sept{{display:flex;flex-wrap:wrap;gap:8px;margin:26px 0 0;padding:0;list-style:none;justify-content:center}}
.sept li{{background:#fff;border:1px solid var(--filet);border-radius:99px;padding:6px 13px 6px 6px;font-size:14.5px;font-weight:700;display:flex;align-items:center;gap:7px}}
.sept li i{{font-style:normal;display:grid;place-items:center;width:24px;height:24px;border-radius:50%;background:var(--bleu);color:#fff;font-size:12.5px;font-weight:900}}

/* parler */
.tels{{display:flex;gap:16px;justify-content:center}}
.bande{{background:var(--bleu-f);color:#EDE6D6;border-radius:24px;padding:32px;display:grid;grid-template-columns:1fr auto;gap:26px;align-items:center}}
.bande h2{{color:#fff}}
.bande .intro{{color:#D6CFBF}}
.bande ul{{margin:0;padding:0;list-style:none}}
.bande li{{padding:8px 0 8px 34px;position:relative;font-size:16px}}
.bande li::before{{content:"";position:absolute;left:0;top:10px;width:22px;height:22px;border-radius:50%;background:var(--jaune);
 -webkit-mask:url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><circle cx="12" cy="12" r="12"/></svg>')}}
.bande li::after{{content:"✓";position:absolute;left:5px;top:9px;color:var(--bleu-f);font-weight:900;font-size:14px}}
.bande .tel{{max-width:200px;box-shadow:0 14px 34px rgba(0,0,0,.4)}}

/* deux cartes */
.duo{{display:grid;grid-template-columns:1fr 1fr;gap:20px}}
.carte{{background:var(--papier);border:1px solid var(--filet);border-radius:20px;padding:22px;display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:start}}
.carte .tel{{max-width:170px;padding:7px;border-radius:24px}}
.carte .tel img{{border-radius:18px}}
.carte h3{{margin:4px 0 6px;font-size:22px;color:var(--bleu-f)}}
.carte p{{margin:0 0 10px;font-size:15.5px}}
.carte ul{{margin:0;padding-left:18px;font-size:15px;color:#4A463D}}

/* le chemin */
.chemin{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(5,1fr);gap:12px}}
.chemin li{{background:#fff;border:1px solid var(--filet);border-radius:14px;overflow:hidden;position:relative;display:flex;flex-direction:column}}
.chemin img{{width:100%;aspect-ratio:3/2;object-fit:cover;display:block}}
.chemin .n{{position:absolute;top:8px;left:8px;width:28px;height:28px;border-radius:50%;background:var(--jaune);color:var(--bleu-f);font-weight:900;display:grid;place-items:center;font-size:14px;box-shadow:0 1px 3px rgba(0,0,0,.25)}}
.chemin b{{padding:8px 10px 0;font-size:15px;color:var(--bleu-f);line-height:1.2}}
.chemin small{{padding:0 10px;font-size:12.5px;color:var(--doux);font-weight:700}}
.chemin em{{padding:2px 10px 10px;font-size:13.5px;font-style:normal;color:#4A463D;line-height:1.3}}

/* prix */
.prix{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.offre{{border-radius:20px;padding:24px;border:2px solid var(--filet);background:var(--papier)}}
.offre.plus{{border-color:var(--bleu);background:#fff}}
.offre .etiq{{font-size:13px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--doux)}}
.offre .montant{{font-size:46px;font-weight:900;color:var(--bleu-f);line-height:1.1;margin:4px 0 2px}}
.offre .montant small{{font-size:16px;color:var(--doux);font-weight:700}}
.offre ul{{margin:12px 0 0;padding-left:20px;font-size:15.5px}}
.offre .barre{{font-size:26px;color:var(--doux);font-weight:700}}
.lancement{{display:inline-block;background:#FBEFC4;color:#5C4400;border:1px solid #E7C75A;border-radius:99px;padding:4px 12px;font-size:14px;font-weight:800;margin:4px 0 0}}
.besoin{{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0;padding:0;list-style:none}}
.besoin li{{background:#fff;border:1px solid var(--filet);border-radius:12px;padding:10px 14px;font-size:15px}}
.besoin b{{color:var(--bleu-f)}}

.fin{{margin:60px 0 0;background:var(--jaune);border-radius:24px;padding:30px;text-align:center}}
.fin h2{{margin-bottom:6px}}
.fin p{{margin:0 0 16px;font-size:18px}}
.fin .cta{{background:var(--bleu-f);color:#fff}}
footer{{text-align:center;font-size:13px;color:var(--doux);padding:26px 0 40px}}

@media (max-width:860px){{
 .une{{grid-template-columns:1fr}} .une .visuel{{min-height:360px;max-width:420px;margin:0 auto;width:100%}}
 .chiffres{{grid-template-columns:repeat(2,1fr)}}
 .temps,.halte,.duo,.prix{{grid-template-columns:1fr}} .temps .fleche{{display:none}}
 .bande{{grid-template-columns:1fr;padding:24px}} .bande .tel{{max-width:46%}}
 .chemin{{grid-template-columns:repeat(2,1fr)}}
 .carte{{grid-template-columns:1fr}} .carte .tel{{margin:0 auto}}
}}
@media (max-width:420px){{
 .une .tel.a,.une .tel.b{{max-width:175px}} .tampon{{width:96px;height:96px;font-size:11px}} .tampon b{{font-size:24px}}
 .une .visuel{{min-height:300px}}
}}
@media print{{
 @page{{size:letter;margin:12mm}}
 body{{-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:12px}}
 .retour,.cta{{display:none}} section{{margin-top:22px;break-inside:avoid}}
 .une .visuel{{min-height:300px}} .tel{{box-shadow:none}}
}}
</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">Aide à l'apprentissage de l'espagnol</span></span>
  <span class="secteur"><small>Voyage · chemin de Saint-Jacques</small><b>En route vers Compostelle</b></span>
</div></div>

<div class="cadre">
<a class="retour" href="/presentations.html">&#8592; Le classeur</a>

<header class="une">
  <div>
    <p class="sur">Pour les pèlerins francophones</p>
    <h1>L'espagnol du Camino, <span>là où vous en aurez besoin</span>.</h1>
    <p class="chapeau">Trouver un lit, commander le menu du pèlerin, expliquer une ampoule à la pharmacie, demander son chemin,
    parler avec les autres le soir : vous apprenez chaque phrase <b>la veille du jour où vous en aurez besoin</b>, dans votre téléphone.
    Le chemin compte une trentaine d'étapes de marche : nous en avons retenu <b>dix</b>, environ une tous les trois jours, chacune avec une situation nouvelle.</p>
    <a class="cta" href="{APP}" target="_blank" rel="noopener">Essayer gratuitement</a>
  </div>
  <div class="visuel" aria-hidden="true">
    <div class="tel a"><img src="{CAP}accueil.jpg" alt=""></div>
    <div class="tel b"><img src="{CAP}scene.jpg" alt=""></div>
    <div class="tampon"><span><b>{len(etapes)}</b>étapes<br>choisies</span></div>
  </div>
</header>

<div class="chiffres">
  <div><b>{len(seances)}</b><span>entraînements de 15 min, à la maison, pour préparer son sac</span></div>
  <div><b>{len(etapes)}</b><span>étapes choisies sur une trentaine, de Roncesvalles à Santiago ({km} km)</span></div>
  <div><b>7</b><span>petits temps par étape : écouter, comprendre, parler</span></div>
  <div><b>0 $</b><span>pour tout le chemin ; aucune inscription, aucun courriel</span></div>
</div>

<section>
  <h2><span class="num">1</span>Trois temps, comme le voyage</h2>
  <p class="intro">On ne vous apprend pas « l'espagnol » : on vous apprend <b>celui du chemin</b>, dans l'ordre où vous le rencontrerez.</p>
  <div class="temps">
    <article>
      <img class="croq" src="{MEDIA}croquis/mochila.jpg" alt="">
      <p class="quand">Les semaines d'avant</p>
      <h3>Préparer son sac</h3>
      <p>Avant le Camino, on prépare son sac et on s'entraîne à marcher. Ici aussi : huit entraînements de quinze minutes, à la maison. Chacun met un outil dans votre sac :</p>
      <ul>{seance_li}</ul>
      <p style="margin-top:10px">Puis la marche d'essai : « Prêt à partir ? ».</p>
      <svg class="fleche" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 2l16 10L4 22z"/></svg>
    </article>
    <article>
      <img class="croq" src="{MEDIA}croquis/flecha.jpg" alt="">
      <p class="quand">Sur le chemin · environ {jours} jours de marche</p>
      <h3>Dix étapes choisies</h3>
      <p>Chacune prépare la situation qui vous attend ce soir-là : l'albergue complet, le bar du matin, la pharmacie, la pluie à O Cebreiro…</p>
      <p style="margin-top:10px">Une étape se fait d'une traite ou en morceaux : le soir à l'albergue, ou pendant la pause.</p>
      <svg class="fleche" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 2l16 10L4 22z"/></svg>
    </article>
    <article>
      <img class="croq" src="{MEDIA}croquis/credencial.jpg" alt="">
      <p class="quand">À chaque arrivée</p>
      <h3>Un tampon sur la credencial</h3>
      <p>Comme le vrai carnet du pèlerin : chaque étape réussie ajoute son tampon. Au bout, le test du chemin vous dit ce que vous savez faire.</p>
    </article>
  </div>
</section>

<section>
  <h2><span class="num">2</span>Une étape, de l'oreille à la voix</h2>
  <p class="intro">Toujours le même rythme : on <b>découvre</b>, on <b>comprend</b> ce qu'on nous répond, puis on <b>agit</b>. La traduction reste cachée tant que vous n'avez pas cherché.</p>
  <div class="halte">
    <div class="ecran"><div class="tel"><img src="{CAP}mots.jpg" alt="Les mots du jour : des cartes dessinées"></div>
      <span class="phase ph-1">Découvrir</span><h3>Les mots, en dessins</h3>
      <p>Vous touchez une carte, vous entendez le mot dit par une voix d'Espagne. Aucune liste à apprendre par cœur.</p></div>
    <div class="ecran"><div class="tel"><img src="{CAP}scene.jpg" alt="La scène : Don Fermín vous répond"></div>
      <span class="phase ph-2">Comprendre</span><h3>Les gens du lieu vous répondent</h3>
      <p>À leur vitesse, avec leur accent. Vous écoutez d'abord ; le texte ne s'affiche qu'après votre réponse.</p></div>
    <div class="ecran"><div class="tel"><img src="{CAP}dire.jpg" alt="Je le dis : le micro"></div>
      <span class="phase ph-3">Agir</span><h3>À vous de le dire</h3>
      <p>Au micro, à voix haute. Vous cherchez d'abord, puis vous comparez avec le modèle.</p></div>
  </div>
  <ul class="sept" aria-label="Les sept temps d'une étape">
    <li><i>1</i>Le lieu</li><li><i>2</i>Les mots du jour</li><li><i>3</i>J'entends, je trouve</li>
    <li><i>4</i>Ce qu'on me répond</li><li><i>5</i>La scène</li><li><i>6</i>Je le dis</li><li><i>7</i>Le soir, avec Marta</li>
  </ul>
</section>

<section>
  <div class="bande">
    <div>
      <h2>Vous parlez, pour vrai</h2>
      <p class="intro">Le chemin ne se fait pas en cochant des cases. Chaque étape finit par une conversation.</p>
      <ul>
        <li><b>La scène</b> : les gens du lieu, à l'albergue, au bar, à la pharmacie — vous choisissez ou vous répondez à voix haute.</li>
        <li><b>Le soir, avec Marta</b> : une pèlerine de Valladolid qui se souvient de ce que vous lui avez dit la veille.</li>
        <li><b>Voix plus lentes</b>, <b>français sous chaque réplique</b> : deux interrupteurs, pour les jours difficiles.</li>
      </ul>
    </div>
    <div class="tels">
      <div class="tel"><img src="{CAP}soir.jpg" alt="Le soir, avec Marta"></div>
      <div class="tel"><img src="{CAP}lieu.jpg" alt="Le lieu : Puente la Reina"></div>
    </div>
  </div>
</section>

<section>
  <h2><span class="num">3</span>Toujours sur vous</h2>
  <div class="duo">
    <div class="carte">
      <div class="tel"><img src="{CAP}trousse.jpg" alt="Ma trousse"></div>
      <div><h3>Ma trousse</h3>
        <p>La trousse de secours pour se débrouiller : les phrases utiles, rangées par situation, avec leur voix.</p>
        <ul><li>les urgences (le 112, l'ambulance, « au secours ») ;</li>
        <li>votre carte d'allergie, en grand, à montrer au serveur ;</li>
        <li>« Montrer » : la phrase plein écran, à tendre à quelqu'un ;</li>
        <li><b>sans réseau</b> sur la Meseta : tout se garde dans le téléphone.</li></ul></div>
    </div>
    <div class="carte">
      <div class="tel"><img src="{CAP}credencial.jpg" alt="La credencial"></div>
      <div><h3>Ma credencial</h3>
        <p>Votre carnet de route, avec une case par étape. La borne vous dit combien il reste de kilomètres, les tampons ce que vous avez fait.</p>
        <ul><li>on reprend où on s'était arrêté ;</li>
        <li>rien à créer : pas de compte, pas de mot de passe ;</li>
        <li>vos réponses restent <b>dans votre téléphone</b>.</li></ul></div>
    </div>
  </div>
</section>

<section>
  <h2><span class="num">4</span>Les dix étapes choisies</h2>
  <p class="intro">Environ {jours} jours de marche, à {KM_JOUR} km par jour. Sur la trentaine d'étapes du chemin, nous en avons retenu dix, réparties tout le long : environ une tous les trois jours de marche, et chacune vous fait vivre une situation nouvelle. Assez pour tout couvrir, sans alourdir le sac.</p>
  <ol class="chemin">{haltes}</ol>
</section>

<section>
  <h2><span class="num">5</span>Ce que ça coûte</h2>
  <div class="prix">
    <div class="offre">
      <p class="etiq">Le chemin</p>
      <p class="montant">Gratuit</p>
      <ul><li>les huit entraînements « Avant de partir » et la marche d'essai ;</li><li>les dix étapes, leurs scènes et leurs voix ;</li>
      <li>Ma trousse, hors ligne ;</li><li>le test du chemin.</li></ul>
    </div>
    <div class="offre plus">
      <p class="etiq">En option · Parler librement</p>
      <p class="montant">{f'<s class="barre">{prix(o["prixRegulier"])}</s> ' if o["promo"] else ""}{prix(o["prix"])} <small>une fois, pour {o["jours"] // 30} mois</small></p>
      {f'<p class="lancement">Prix de lancement, pour un temps limité{" — jusqu’au " + date_fr(o["promoFin"]) + " inclusivement" if o["promoFin"] else ""}.</p>' if o["promo"] else ""}
      <ul><li>{o["conversations"]} conversations libres avec les personnages du chemin, sur le sujet de votre choix ;</li>
      <li>ils vous répondent et vous relancent, comme sur le chemin ;</li>
      <li>au besoin, {o["rechargeConversations"]} conversations de plus pour {prix(o["recharge"])}.</li></ul>
    </div>
  </div>
  <ul class="besoin">
    <li><b>Un téléphone</b> (ou une tablette), dans le navigateur — rien à installer</li>
    <li><b>Des écouteurs</b>, pour l'autobus ou l'albergue</li>
    <li><b>Un micro</b> : celui du téléphone suffit</li>
    <li><b>Quinze minutes</b> par jour</li>
  </ul>
</section>

<div class="fin">
  <h2>Buen Camino !</h2>
  <p>Commencez par le premier entraînement : quinze minutes, ce soir.</p>
  <a class="cta" href="{APP}" target="_blank" rel="noopener">Ouvrir En route vers Compostelle</a>
</div>

<footer>francis · En route vers Compostelle · portail.edufrancis.ca{APP}</footer>
</div>
</body>
</html>
"""
    SORTIE.write_text(page, encoding="utf-8")
    # La copie publique (pilote du 27 sept. 2026) : le classeur demande une
    # connexion, les amis pèlerins n'en ont pas. Même page, à côté de
    # l'application (publique), sans le lien vers le classeur, non indexée.
    pub = (page.replace(f'src="{CAP}', 'src="depliant/')
               .replace(f'src="{MEDIA}', 'src="/assets/interactive/compostelle/')
               .replace('<a class="retour" href="/presentations.html">&#8592; Le classeur</a>', '')
               .replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">'))
    assert CAP not in pub and "../interactive" not in pub
    PUBLIC.mkdir(parents=True, exist_ok=True)
    for f in (RACINE / "assets" / "presentations" / "compostelle-depliant").glob("*.jpg"):
        (PUBLIC / f.name).write_bytes(f.read_bytes())
    (PUBLIC.parent / "presentation.html").write_text(pub, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), f"— {len(etapes)} étapes, {len(seances)} entraînements, {prix(o['prix'])}")


if __name__ == "__main__":
    main()
