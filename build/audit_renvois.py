#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ce que les fiches élèves montrent du doigt sans le porter.

    python3 build/audit_renvois.py            # relève + page du classeur
    python3 build/audit_renvois.py --releve   # relève seule, à l'écran

Une fiche de séance est une **feuille volante** : l'élève la relit chez lui,
sans le diaporama et sans la classe. Elle ne devrait donc jamais renvoyer à
quelque chose qu'elle ne porte pas. Ce contrôle balaie les 1 265 fiches de
`assets/documents/` et sépare trois cas, qui ne se règlent pas de la même
façon :

1. **Le document source n'est pas sur la feuille.** L'exercice est
   inapplicable seul. Cinq fiches — à trancher une par une, parce que la
   réponse dépend de la taille du document.
2. **Le renvoi nomme un écran, mais le contenu est là.** « Les trois derniers
   sujets sont sur la diapositive suivante » : ils sont juste dessous, dans un
   bloc « (suite) ». Le mot ment, le document non.
3. **Une consigne de classe imprimée sur la feuille de l'élève.** « Écoutez
   d'abord, diapositive masquée » s'adresse à la classe, pas au lecteur.

Le balayage lit **le corps** des fiches, jamais leur feuille de style : le CSS
des fiches contient lui-même « qu'à l'écran », et le compter donnait 2 537
fausses alertes sur 1 264 fiches.

Trouvé le 7 septembre 2026 à partir d'une question de l'utilisateur sur la
fiche B2 du module 1 du niveau 6 — « est-ce en lien avec une offre qu'on ne
voit pas ? ». La réponse était non pour B2 (le devoir de A4 la demande) et oui
pour B1, qui est dans la liste ci-dessous.
"""
import argparse
import glob
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(RACINE, 'assets', 'documents')
PAGE = os.path.join(RACINE, 'assets', 'presentations', 'renvois-des-fiches.html')

# Ce qui manque, pour les cinq fiches du premier cas. Écrit à la main : c'est
# un jugement sur le document, pas quelque chose qui se déduit du texte.
MANQUE = {
    'module-n6-recherche-b1': ("l’offre d’emploi Boisverte",
        "Les six énoncés restent répondables depuis les trois dialogues et la "
        "règle, qui sont sur la feuille. C’est la consigne qui renvoie à côté."),
    'module-n2-couloirs-b1': ("le plan du centre",
        "Le plan est un document visuel : sans lui, aucun des six énoncés ne "
        "peut être tranché. C’est la fiche la plus cassée des cinq."),
    'module-n7-emploi-a4': ("l’ordre du jour du 8 septembre",
        "Un ordre du jour tient en quinze lignes : c’est le plus facile des "
        "trois à imprimer sur la feuille."),
    'module-n7-emploi-c4': ("l’extrait de la loi sur le programme de prévention",
        "Un texte de loi cité au long alourdirait la feuille ; un extrait de "
        "cinq lignes suffirait aux questions posées."),
    'module-n7-emploi-d1': ("la note de service d’Aïcha",
        "Une note de service est courte et c’est le genre même que la séance "
        "enseigne : la lire sur papier vaut mieux que la lire projetée."),
}

CAS1 = re.compile(r"(?:d'après|regardant)[^.]{0,60}(?:projet[ée]e?|diapositive)", re.I)
CAS2 = re.compile(r"(?:diapositive (?:précédente|suivante)|tableau suivant)", re.I)
CAS3 = re.compile(r"diapositive masquée", re.I)


def corps_et_titre(chemin):
    brut = io.open(chemin, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', brut, re.S)
    titre = re.sub(r'\s*—\s*Fiche élève\s*$', '', (m.group(1).strip() if m else ''))
    # Après la dernière feuille de style : le CSS parle lui-même d’écran.
    corps = brut.split('</style>')[-1]
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', corps)), titre


def cle(nom):
    """« module-n7-emploi-a4-la-note… » → « module-n7-emploi-a4 »."""
    m = re.match(r'(.*?-[a-e]\d+)(?:-|$)', nom)
    return m.group(1) if m else nom


def relever():
    un, deux, trois = [], [], []
    total = 0
    for f in sorted(glob.glob(os.path.join(DOCS, 'module-*.html'))):
        nom = os.path.basename(f)[:-5]
        if '-fiches-eleves' in nom:
            continue
        total += 1
        texte, titre = corps_et_titre(f)
        m1 = CAS1.search(texte)
        if m1:
            un.append((cle(nom), titre, texte[max(0, m1.start() - 60):m1.end() + 40].strip()))
            continue           # le cas 1 absorbe son propre « diapositive »
        m2 = CAS2.search(texte)
        if m2:
            deux.append((cle(nom), titre,
                         texte[max(0, m2.start() - 70):m2.end() + 60].strip()))
        if CAS3.search(texte):
            trois.append((cle(nom), titre, ''))
    return total, un, deux, trois


def e(s):
    return (s or '').replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _mille(n):
    """« 1 265 », avec l'espace insécable du français — la même règle que les
    fiches viennent de recevoir dans `fiche.esc()`."""
    return '\u00a0'.join(re.findall(r'\d{1,3}', '%d' % n)[::-1][::-1]) if n < 1000 \
        else '%d\u00a0%03d' % (n // 1000, n % 1000)


def rendre(total, un, deux, trois):
    def lignes(items, avec_manque=False):
        out = []
        for c, titre, ctx in items:
            manque = MANQUE.get(c)
            out.append(
                '<tr><td class="q"><code>%s</code><small>%s</small></td>'
                '<td>%s%s</td></tr>'
                % (e(c), e(titre),
                   ('<b>%s</b><small>%s</small>' % (e(manque[0]), e(manque[1])))
                   if avec_manque and manque else '',
                   ('<span class="cit">…%s…</span>' % e(ctx)) if ctx else ''))
        return ''.join(out)

    modules3 = sorted({c.rsplit('-', 1)[0] for c, _, _ in trois})
    with io.open(PAGE, 'w', encoding='utf-8') as f:
        f.write(GABARIT
                .replace('{{TOTAL}}', _mille(total))
                .replace('{{N1}}', str(len(un)))
                .replace('{{N2}}', str(len(deux)))
                .replace('{{N3}}', str(len(trois)))
                .replace('{{M3}}', str(len(modules3)))
                .replace('{{TABLE1}}', lignes(un, avec_manque=True))
                .replace('{{TABLE2}}', lignes(deux))
                .replace('{{LISTE3}}', ' · '.join('<code>%s</code>' % e(m) for m in modules3)))
    print('✓ %s' % os.path.relpath(PAGE, RACINE))



GABARIT = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ce que les fiches montrent sans le porter</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,500;6..72,600&family=Nunito:wght@400;600;700;800&display=swap">
<style>
:root{
  --ground:#F7F7F5; --card:#FFFFFF; --sunken:#FBFBFA;
  --ink:#17181A; --body:#3A3D40; --muted:#6E7175;
  --line:#E4E4E0; --line-fort:#D2D2CD;
  --acier:#1D6B8F; --acier-bg:#E7F0F6;
  --fait:#0A8F5B; --fait-bg:#E6F5EE;
  --decid:#C07A08; --decid-bg:#FBF2E2;
  --loi:#C7302B; --loi-bg:#FBEDEC;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --ground:#151618; --card:#1D1F22; --sunken:#212326;
  --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
  --line:#2E3135; --line-fort:#3D4146;
  --acier:#6DAFD2; --acier-bg:#14242C;
  --fait:#4BC48D; --fait-bg:#12291F;
  --decid:#E0A63F; --decid-bg:#2C2213;
  --loi:#EE7A73; --loi-bg:#2E1917;
}}
:root[data-theme="dark"]{
  --ground:#151618; --card:#1D1F22; --sunken:#212326;
  --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
  --line:#2E3135; --line-fort:#3D4146;
  --acier:#6DAFD2; --acier-bg:#14242C;
  --fait:#4BC48D; --fait-bg:#12291F;
  --decid:#E0A63F; --decid-bg:#2C2213;
  --loi:#EE7A73; --loi-bg:#2E1917;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:Nunito,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased}
.doc{max-width:900px;margin:0 auto;padding:26px 24px 90px}
.retour{display:inline-flex;gap:8px;font-size:13px;font-weight:700;color:var(--muted);
  text-decoration:none;margin-bottom:30px}
.retour:hover{color:var(--acier)}
.eyebrow{font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;
  color:var(--acier);margin:0 0 12px}
h1{font-family:Newsreader,Georgia,serif;font-size:clamp(34px,5.6vw,50px);line-height:1.05;
  font-weight:500;letter-spacing:-.02em;color:var(--ink);margin:0 0 18px;text-wrap:balance}
h2{font-family:Newsreader,Georgia,serif;font-size:27px;line-height:1.2;font-weight:600;
  color:var(--ink);margin:0 0 6px;text-wrap:balance}
.chapeau{font-size:19px;line-height:1.6;margin:0;max-width:64ch}
.chapeau strong{color:var(--ink);font-weight:700}
p{margin:0;max-width:68ch}
section{display:flex;flex-direction:column;gap:15px;padding:42px 0 0;margin:42px 0 0;
  border-top:1px solid var(--line)}
section.premier{border-top:none;margin-top:0;padding-top:34px}
code{font-family:var(--mono);font-size:.85em;background:var(--sunken);
  border:1px solid var(--line);border-radius:4px;padding:1px 5px;color:var(--ink)}
ul.simple{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:7px}
ul.simple li{max-width:66ch}
.these{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acier);
  border-radius:3px;padding:24px 26px;display:flex;flex-direction:column;gap:11px}
.these .cle{font-family:Newsreader,Georgia,serif;font-size:22px;line-height:1.3;
  font-weight:500;color:var(--ink);font-style:italic}
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:2px;
  background:var(--line);border:1px solid var(--line);border-radius:3px;overflow:hidden}
.chiffres div{background:var(--card);padding:16px 18px}
.chiffres b{display:block;font-family:Newsreader,Georgia,serif;font-size:30px;font-weight:500;
  color:var(--ink);line-height:1;font-variant-numeric:tabular-nums}
.chiffres span{font-size:12.5px;color:var(--muted);display:block;margin-top:7px;line-height:1.35}
.defile{overflow-x:auto;border:1px solid var(--line);border-radius:3px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:560px}
th,td{padding:13px 15px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);background:var(--sunken);white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
td.q{font-weight:700;color:var(--ink);white-space:nowrap}
td small{display:block;color:var(--muted);font-size:13px;line-height:1.45;margin-top:4px;
  font-weight:600;white-space:normal;max-width:34ch}
.cit{display:block;margin-top:6px;font-size:13.5px;color:var(--muted);font-style:italic;
  line-height:1.5}
.badge{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:.05em;
  text-transform:uppercase;padding:3px 9px;border-radius:2px;white-space:nowrap}
.b-loi{background:var(--loi-bg);color:var(--loi)}
.b-dec{background:var(--decid-bg);color:var(--decid)}
.b-fait{background:var(--fait-bg);color:var(--fait)}
.tete{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}
.reserve{border:1px dashed var(--line-fort);border-radius:3px;padding:19px 22px;
  font-size:15px;color:var(--muted);display:flex;flex-direction:column;gap:8px}
.reserve strong{color:var(--body)}
.pied{margin-top:48px;padding-top:20px;border-top:1px solid var(--line);font-size:13.5px;
  color:var(--muted);display:flex;flex-direction:column;gap:5px}
@media (max-width:620px){ .doc{padding:22px 17px 70px} }
</style>
</head>
<body>
<div class="doc">
<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>
<p class="eyebrow">Bibliothèque de francisation · 7 septembre 2026 · relevé</p>
<h1>Ce que les fiches montrent sans le porter</h1>
<p class="chapeau">Une fiche de séance est une <strong>feuille volante</strong> : l'élève la
relit chez lui, sans le diaporama et sans la classe. Elle ne devrait donc jamais renvoyer à
quelque chose qu'elle ne porte pas. Les <strong>{{TOTAL}} fiches</strong> ont été balayées.
Trois cas en sortent, et ils ne se règlent pas de la même façon.</p>

<section class="premier">
  <div class="these">
    <p class="cle">Le renvoi n'est presque jamais un document manquant. Il est presque
    toujours un mot d'écran resté sur du papier.</p>
    <p>Cinq fiches sur {{TOTAL}} sont réellement inapplicables seules. Les autres portent bien
    ce dont elles parlent — elles l'appellent seulement « la diapositive suivante » au lieu de
    « ci-dessous ». La distinction compte, parce que la première liste demande votre jugement
    document par document, et les deux autres se règlent d'un seul geste.</p>
  </div>
  <div class="chiffres">
    <div><b>{{N1}}</b><span>fiches où le document source n'est pas sur la feuille</span></div>
    <div><b>{{N2}}</b><span>fiches où le renvoi nomme un écran, mais le contenu est là</span></div>
    <div><b>{{N3}}</b><span>fiches portant une consigne de classe</span></div>
    <div><b>{{TOTAL}}</b><span>fiches balayées, tous niveaux</span></div>
  </div>
</section>

<section>
  <div class="tete"><h2>1 · Le document n'est pas sur la feuille</h2>
    <span class="badge b-loi">À trancher une par une</span></div>
  <p>Ces cinq-là sont de vrais trous : la consigne renvoie à un document projeté ou affiché,
  et la feuille ne contient <strong>ni image ni texte source</strong>. Un élève qui reprend sa
  fiche seul ne peut pas refaire l'exercice.</p>
  <div class="defile">
  <table>
    <thead><tr><th>La fiche</th><th>Ce qui manque, et ce que ça coûte</th></tr></thead>
    <tbody>{{TABLE1}}</tbody>
  </table>
  </div>
  <p><strong>Deux façons de refermer, et elles ne se valent pas :</strong></p>
  <ul class="simple">
    <li><strong>Imprimer le document sur la fiche.</strong> La feuille devient autonome —
    c'est ce qu'on veut d'une feuille volante. Coût : la place, et pour le plan du centre,
    une image dans une fiche qui n'en a aucune aujourd'hui.</li>
    <li><strong>Réécrire la consigne.</strong> « Répondez d'après le dialogue » au lieu de
    « d'après le dialogue et l'offre projetée ». Gratuit, honnête, mais la fiche reste
    dépendante de la classe pour les trois de <code>module-n7-emploi</code>, dont les
    questions portent vraiment sur le document.</li>
  </ul>
  <div class="reserve">
    <strong>Ce que le relevé ne dit pas.</strong>
    <p>Il ne vérifie pas que les <em>questions</em> sont répondables sans le document — il
    dit seulement que le document est absent. Je l'ai fait à la main pour
    <code>module-n6-recherche-b1</code> : les six énoncés y passent sans l'offre. Pour les
    quatre autres, ça reste à regarder, et c'est justement ce qui décide entre imprimer et
    réécrire.</p>
  </div>
</section>

<section>
  <div class="tete"><h2>2 · Le mot ment, le document non</h2>
    <span class="badge b-dec">Un seul geste</span></div>
  <p>« Les trois derniers sujets sont sur la <em>diapositive suivante</em> » — ils sont juste
  dessous, dans un bloc « (suite) ». Le contenu est là ; c'est le vocabulaire du diaporama
  qui a survécu au passage sur papier. Même chose pour « quatre autres au
  <em>tableau suivant</em> ».</p>
  <div class="defile">
  <table>
    <thead><tr><th>La fiche</th><th>Ce qu'elle dit</th></tr></thead>
    <tbody>{{TABLE2}}</tbody>
  </table>
  </div>
  <p>Ces renvois viennent des fichiers de contenu, qui servent aux deux sorties — le
  PowerPoint et la fiche. Le mot est juste à l'écran et faux sur papier. La correction
  appartient donc à <code>fiche.py</code>, qui sait déjà retirer les notes d'enseignant et les
  corrigés : « diapositive suivante » et « tableau suivant » y deviendraient « ci-dessous »,
  sans toucher au diaporama.</p>
</section>

<section>
  <div class="tete"><h2>3 · Une consigne de classe sur la feuille de l'élève</h2>
    <span class="badge b-dec">Un seul geste</span></div>
  <p><strong>{{N3}} fiches</strong>, dans {{M3}} modules, portent « Écoutez d'abord,
  <em>diapositive masquée</em> ». C'est une consigne adressée à la classe : l'enseignant
  masque la diapositive pour qu'on écoute avant de lire. Sur la feuille, elle ne veut rien
  dire — et pire, elle décrit un geste que l'élève ne peut pas faire, puisque le texte du
  dialogue est imprimé juste en dessous.</p>
  <p>Même endroit que le cas 2, même geste. Deux options : la retirer, ou la remplacer par ce
  qu'elle veut vraiment dire à un lecteur seul — <em>« Écoutez l'enregistrement avant de lire
  le texte. »</em> La seconde garde l'intention pédagogique, qui est bonne.</p>
  <p style="font-size:14.5px;color:var(--muted)">Les modules touchés : {{LISTE3}}</p>
</section>

<section>
  <div class="reserve">
    <strong>Ce qui a lancé ce relevé, et l'erreur qu'il a corrigée.</strong>
    <p>Une question sur la fiche B2 du module 1 du niveau 6 : « <em>sur votre offre,
    soulignez les exigences</em> — est-ce en lien avec une offre qu'on ne voit pas ? » La
    réponse est <strong>non</strong> pour B2 : le billet de sortie de A4 demande à l'élève de
    trouver une offre réelle, et le dit sur sa feuille. J'avais d'abord conclu le contraire en
    cherchant le mot « apporter » — la consigne est écrite avec « trouvez ». Un balayage par
    mot-clé se trompe dans le sens le plus coûteux : il déclare un trou là où il n'y en a pas.</p>
    <p>Le même balayage, refait sur les 59 modules dont les notes parlent d'un apport, ne
    trouve <strong>aucun</strong> cas où l'élève doit apporter quelque chose sans en être
    averti sur une fiche. Tous les autres sont du matériel que l'enseignant apporte — un ruban
    à mesurer, des emballages vides, un vrai journal — et l'élève n'a pas à en être averti.</p>
  </div>
</section>

<div class="pied">
  <p>Refait par <code>python3 build/audit_renvois.py</code> — le relevé est calculé, pas
  recopié.</p>
  <p>Le balayage lit le <strong>corps</strong> des fiches, jamais leur feuille de style : le
  CSS des fiches contient lui-même « qu'à l'écran », et le compter donnait 2 537 fausses
  alertes sur 1 264 fiches.</p>
</div>
</div>
</body>
</html>
"""



def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--releve', action='store_true')
    args = ap.parse_args()
    total, un, deux, trois = relever()
    print('%d fiches balayées' % total)
    print('  1 · document absent de la feuille   : %d' % len(un))
    for c, t, _ in un:
        print('        %-28s %s' % (c, t))
    print('  2 · renvoi à un écran, contenu présent : %d' % len(deux))
    print('  3 · consigne de classe imprimée        : %d' % len(trois))
    if not args.releve:
        rendre(total, un, deux, trois)
    return 0


if __name__ == '__main__':
    sys.exit(main())
