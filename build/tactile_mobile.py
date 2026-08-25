#!/usr/bin/env python3
"""Rend le glisser-déposer utilisable au doigt, sur un téléphone.

Trois défauts mesurés le 24 août 2026 en émulation iPhone (390 px de large),
sur `module-achat`, et corrigés ensemble parce qu'ils se combinent : chacun
seul serait supportable, les trois ensemble rendent l'exercice impraticable.

1. **Le glisser volait le défilement.** Dès 8 px de mouvement, le doigt posé
   sur une tuile créait le fantôme de glisser et le gestionnaire appelait
   `preventDefault()`. Or sur téléphone le banc de réponses est une bande qui
   défile **horizontalement** : le seul geste qui la ferait défiler était
   précisément celui qui déclenchait un glisser. L'élève ne pouvait donc pas
   atteindre les réponses au-delà de la première, et le moindre tremblement
   du doigt transformait une sélection en glisser avorté.
2. **Une réponse ne tenait pas dans la bande.** Bande visible de 245 px pour
   des tuiles allant jusqu'à 370 px : le texte de la réponse était coupé à
   droite, et il fallait défiler *dans* la tuile pour la lire.
3. **Les gouttières ne se réduisaient pas.** 32 px de page plus 22 px de
   carte de chaque côté : 108 px des 390 px de l'écran, soit 28 %, avant même
   d'afficher quoi que ce soit.

Ce que le script change, dans le gabarit et dans les dix modules écrits à la
main (les autres se reconstruisent depuis le gabarit) :

- le glisser ne part plus que sur un mouvement **à dominante verticale** —
  les zones de dépôt sont au-dessus du banc, donc c'est la direction du geste
  qui dit l'intention — ou après un **appui maintenu** de 250 ms, le geste
  appris de l'iPhone. Un balayage horizontal redevient un défilement. Le seuil
  passe de 8 à 12 px, pour qu'une main qui tremble ne perde pas son tap ;
- le banc revient **à la ligne** au lieu de défiler en file, et se borne à
  40 % de la hauteur de l'écran : la réponse se lit en entier ;
- les gouttières tombent à 16 px sous 640 px de large.

    python3 build/tactile_mobile.py            # applique
    python3 build/tactile_mobile.py --verifier  # dit où ça en est, n'écrit rien

Les substitutions sont **exactes** : un fichier qui a divergé est signalé et
laissé tel quel, jamais rafistolé à l'aveugle. Le script est idempotent — il
reconnaît ce qu'il a déjà posé et le compte comme fait.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GABARIT = ROOT / 'build' / 'gabarit' / 'module.html'
# Les dix modules antérieurs à la chaîne gabarit/contenu. Les 77 autres ont un
# manifeste dans build/contenu/ et reçoivent le correctif à la reconstruction.
ECRITS_A_LA_MAIN = ['banque', 'consultation', 'logement', 'meteo', 'nouvelles',
                    'procedure', 'pub', 'sante', 'travail', 'urgence']

# ── 1. Le geste ────────────────────────────────────────────────────────────
JS_AVANT = """function tch(el, iid, lbl, cat, from) {
  el.addEventListener('touchstart', e => { const t=e.touches[0]; ts={x:t.clientX,y:t.clientY,iid,lbl,cat,from:from||null,el,moved:false}; }, {passive:true});
}
document.addEventListener('touchmove', e => {
  if(!ts) return;
  const t=e.touches[0], dx=t.clientX-ts.x, dy=t.clientY-ts.y;
  if(!ts.moved && Math.sqrt(dx*dx+dy*dy)>8){
    ts.moved=true;"""

JS_APRES = """// Sur un téléphone, le doigt posé sur une tuile veut le plus souvent faire
// défiler la page — le banc de réponses occupe la bande du bas, c'est de là
// qu'on pousse l'écran. Prendre tout mouvement pour un glisser confisquait
// ce geste : plus moyen d'atteindre les réponses suivantes, et le moindre
// tremblement transformait une sélection en glisser avorté.
//
// D'où l'appui maintenu, la convention de l'iPhone : on glisse ce qu'on a
// d'abord tenu. Un mouvement immédiat reste un défilement, quelle que soit
// sa direction ; un appui bref sans mouvement reste une sélection ; et
// sélectionner puis toucher la case reste le chemin le plus simple.
const TCH_SEUIL = 12;   // px avant de décider — 8 px, c'était un tremblement
const TCH_TENUE = 250;  // ms d'appui maintenu avant qu'un glisser puisse partir
function tch(el, iid, lbl, cat, from) {
  el.addEventListener('touchstart', e => { const t=e.touches[0]; ts={x:t.clientX,y:t.clientY,t0:Date.now(),iid,lbl,cat,from:from||null,el,moved:false,rendu:false}; }, {passive:true});
}
document.addEventListener('touchmove', e => {
  if(!ts || ts.rendu) return;
  const t=e.touches[0], dx=t.clientX-ts.x, dy=t.clientY-ts.y;
  if(!ts.moved && Math.sqrt(dx*dx+dy*dy)>TCH_SEUIL){
    if((Date.now() - ts.t0) < TCH_TENUE){
      ts.rendu = true;   // parti tout de suite : c'est un défilement
      return;
    }
    ts.moved=true;"""

# ── 2. Le banc lisible ─────────────────────────────────────────────────────
CSS_AVANT = """  /* Les tuiles s'alignent en file et défilent horizontalement plutôt que
     d'empiler une colonne qui mangerait tout l'écran. */
  .bsec.b1 .btiles,.bsec.b1 .btiles.vert{
    flex-direction:row; flex-wrap:nowrap;
    overflow-x:auto; overflow-y:hidden;
    justify-content:flex-start;
    gap:8px; padding-bottom:4px;
    -webkit-overflow-scrolling:touch;
  }
  .bsec.b1 .btiles > *{flex:0 0 auto}"""

CSS_APRES = """  /* Les tuiles reviennent à la ligne. La file horizontale coupait la réponse
     à droite — 245 px de bande visible pour des tuiles de 370 px — et son
     défilement était le seul geste que le glisser-déposer confisquait. Le
     banc se borne à 40 % de l'écran pour ne pas manger l'exercice ; au-delà,
     il défile verticalement, comme le reste de la page. */
  .bsec.b1 .btiles,.bsec.b1 .btiles.vert{
    flex-direction:row; flex-wrap:wrap;
    overflow-x:hidden; overflow-y:auto;
    max-height:40vh;
    justify-content:flex-start;
    gap:8px; padding-bottom:4px;
    -webkit-overflow-scrolling:touch;
  }
  .bsec.b1 .btiles > *{flex:0 1 auto; max-width:100%}"""

# La saignée du banc doit suivre le padding de la carte, qui se réduit sous
# 640 px : écrite en dur à -22px, le banc laissait deux bandes blanches.
BLEED_AVANT = "    margin:0 -22px -22px;"
BLEED_APRES = "    margin:0 calc(-1 * var(--pad-card)) calc(-1 * var(--pad-card));"

# ── 3. Les gouttières ──────────────────────────────────────────────────────
# Ancrage : le bloc du banc collant se termine juste avant cette règle.
ANCRE_GOUTTIERES = "@media(prefers-reduced-motion:no-preference){\n  .bsec.b1{scroll-behavior:smooth}\n}"

GOUTTIERES = """/* ── Gouttières d'un téléphone ─────────────────────────────────────────
   32 px de page plus 22 px de carte de chaque côté, c'était 108 px des
   390 px d'un iPhone — 28 % de l'écran perdus avant d'afficher un mot. Les
   valeurs de la page (--pad-x) sont écrites en dur dans les blocs de section
   depuis l'origine : on les reprend ici plutôt que de les refactoriser dans
   les quatre-vingt-sept modules. */
@media(max-width:640px){
  body{--pad-x:16px; --pad-card:16px; --bleed:-17px}
  #hdr{padding:20px 16px 24px}
  #tabs{padding:10px 16px}
  #sel-banner{padding:10px 16px}
  .dial-sec{padding:16px}
  .intro{padding:14px 16px}
  .exs{padding:18px 16px 40px}
  .vocab-sec{padding:14px 16px 18px}
  .cta{padding:22px 18px; margin:0 16px 24px}
  .card{padding:16px}
}
"""

TEMOIN = 'const TCH_SEUIL'   # marque d'un fichier déjà corrigé


def corriger(html):
    """Renvoie (html, etat). `etat` vaut 'fait', 'deja' ou un message d'écart."""
    if TEMOIN in html:
        return html, 'deja'
    manquants = [nom for nom, aiguille in (
        ('geste', JS_AVANT), ('banc', CSS_AVANT), ('saignée', BLEED_AVANT),
        ('ancre des gouttières', ANCRE_GOUTTIERES)) if aiguille not in html]
    if manquants:
        return html, 'a divergé : ' + ', '.join(manquants) + ' introuvable(s)'
    html = html.replace(JS_AVANT, JS_APRES, 1)
    html = html.replace(CSS_AVANT, CSS_APRES, 1)
    html = html.replace(BLEED_AVANT, BLEED_APRES, 1)
    html = html.replace(ANCRE_GOUTTIERES, ANCRE_GOUTTIERES + '\n\n' + GOUTTIERES, 1)
    return html, 'fait'


def fichiers():
    yield GABARIT
    for nom in ECRITS_A_LA_MAIN:
        yield ROOT / 'assets' / 'interactive' / ('module-' + nom) / ('module-%s-activite-interactive.html' % nom)


def main(argv):
    verifier = '--verifier' in argv
    ecarts = 0
    for f in fichiers():
        if not f.exists():
            print('!! introuvable : %s' % f.relative_to(ROOT))
            ecarts += 1
            continue
        html = f.read_text(encoding='utf-8')
        neuf, etat = corriger(html)
        if etat not in ('fait', 'deja'):
            print('!! %-52s %s' % (f.relative_to(ROOT), etat))
            ecarts += 1
            continue
        if etat == 'deja':
            print('   %-52s déjà corrigé' % f.relative_to(ROOT))
            continue
        if verifier:
            print('~~ %-52s à corriger' % f.relative_to(ROOT))
            ecarts += 1
        else:
            f.write_text(neuf, encoding='utf-8')
            print('   %-52s corrigé' % f.relative_to(ROOT))
    if verifier and ecarts:
        print('\n%d fichier(s) à corriger — relancer sans --verifier.' % ecarts)
    if not verifier and ecarts:
        print('\n%d fichier(s) laissés tels quels.' % ecarts)
    return 1 if ecarts else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
