"""La rétroaction de l'assistant : lisible, et sans emojis.

Le bloc « Rétroaction privée » avait sa hiérarchie à l'envers. La phrase
corrigée — que l'élève n'a qu'à lire — était à 15 px ; la remarque qui explique
l'erreur, la seule partie qui apprenne quelque chose, était à 13 px et en brun
d'avertissement (`--warn-ink #8A5206`), c'est-à-dire la plus petite et la plus
sourde du bloc.

La greffe fait deux choses, décidées sur `essais/essai-retroaction.html` le
31 août 2026 :

  1. chaque remarque devient une carte à elle, sur le fond ambre du système,
     filet à gauche, à 16 px — la taille de la correction. Elle se relit une
     par une, ce qui compte quand il y en a trois ou quatre ;
  2. les emojis ✍️ ✅ ⚠️ cèdent la place à trois SVG monochromes en
     `currentColor` — crayon, loupe, coche — de la même famille que le
     haut-parleur et l'étoile de l'assistant. Ils prennent la couleur de la
     ligne qui les porte.

Les pictogrammes sont écrits DANS le module et non dans `icons/` : copier deux
fichiers dans 87 dossiers pour trois usages coûterait plus qu'il ne rapporte,
et un `<img>` ne peut pas hériter de la couleur du texte.

Le même bloc `.fb` sert à trois endroits — la correction du jeu de rôle, celle
de la production orale et celle du courriel. Les trois changent ensemble.

    python3 build/greffe_retroaction.py            # gabarit + 87 modules
    python3 build/greffe_retroaction.py --retirer  # revient en arrière
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

# Le seul pictogramme du bloc : quelqu'un qui vient de vous donner des
# conseils. Le crayon et la loupe ont été écartés à l'écoute du 31 août 2026 —
# le crayon disait « on écrit » là où c'est un conseil qu'on reçoit, la loupe
# disait « on cherche ». Le buste plutôt que la personne-dans-une-bulle : à
# 19 px, la bulle devient une tache, le buste se lit.
BUSTE = ('<svg class="fb-ic" viewBox="0 0 50 50" aria-hidden="true">'
         '<path d="M25 7a9 9 0 1 1 0 18 9 9 0 0 1 0-18z"/>'
         '<path d="M25 28c-8.5 0-15.5 5.2-17 12.4-.3 1.4.8 2.6 2.2 2.6h29.6'
         'c1.4 0 2.5-1.2 2.2-2.6C40.5 33.2 33.5 28 25 28z"/></svg>')

PAIRES = [
    # 1. Le CSS du bloc.
    (
        """.fb-c{font-size:15px;font-weight:800;color:#154F68;line-height:1.5}
.fb-e{font-size:13px;font-weight:700;color:var(--warn-ink);line-height:1.5;padding-left:14px;position:relative}
.fb-e::before{content:"•";position:absolute;left:2px}
""",
        """.fb-c{font-size:16px;font-weight:800;color:#154F68;line-height:1.5}
/* La remarque a la taille de la correction : c'est elle qui enseigne. Elle
   était à 13 px et en brun d'avertissement, soit la ligne la plus petite et
   la plus sourde du bloc — la hiérarchie était à l'envers. Sa carte ambre lui
   garde son statut de remarque, que l'encre neutre lui ferait perdre. */
.fb-e{font-size:16px;font-weight:700;color:#5F3803;line-height:1.55;
      background:var(--warn-bg,#FEF6E7);border-left:4px solid var(--warn-line,#D9880B);
      border-radius:0 10px 10px 0;padding:10px 13px}
/* Quand tout est déjà juste, c'est la couleur qui le dit — plus d'emoji. */
.fb-c.fb-bravo{color:var(--ok-ink,#0A6B46)}
/* Le buste signe le bloc, en tête : quelqu'un vient de vous donner des
   conseils, et tout ce qui suit est ce qu'il dit. Une personne se présente
   une fois, pas à chaque phrase. currentColor le met au teal du titre. */
/* Le titre est une étiquette, pas une parole : il descend au teal sourd du
   module (celui des lignes d'état) pour que la phrase corrigée, restée au
   #154F68 plein, soit la voix forte du bloc. Au même teal, les deux se
   disputaient le premier rang. */
.fb-t{display:flex;align-items:center;color:#45746C}
.fb-ic{width:17px;height:17px;flex:0 0 17px;fill:currentColor;margin-right:8px}
""",
    ),
    # 2. Le pictogramme, posé juste avant la fonction qui s'en sert.
    #    ATTENTION : ne jamais ancrer sur la ligne ICON_ASSISTANT — elle porte
    #    %%SLUG%% dans le gabarit et le vrai slug dans les 87 modules livrés,
    #    donc elle ne peut pas servir de texte commun. L'en-tête de renderCorr,
    #    lui, est identique partout.
    (
        """function renderCorr(elId,data,orig){
  const fb=document.getElementById(elId);
  const corr=data.corrige||data.corrected||'';
  const errs=data.erreurs||data.errors||[];
  let html='<div class="fb-t">Rétroaction privée</div>';
""",
        """/* Écrit ici et non dans icons/ : un <img> ne peut pas hériter de la couleur
   du texte, et copier un SVG dans 87 dossiers pour un seul usage coûterait
   plus qu'il ne rapporte. */
const ICON_ASSIST = '%%BUSTE%%';
function renderCorr(elId,data,orig){
  const fb=document.getElementById(elId);
  const corr=data.corrige||data.corrected||'';
  const errs=data.erreurs||data.errors||[];
  let html='<div class="fb-t">'+ICON_ASSIST+'<span>Rétroaction privée</span></div>';
""",
    ),
    # 3. Les emojis quittent les lignes : la carte ambre dit la remarque, la
    #    couleur dit la réussite, le buste dit qui parle.
    (
        """    if(cmt) html+='<div class="fb-c">'+(data.pertinent?'✅ ':'⚠️ ')+esc(cmt)+'</div>';
    else if(data.pertinent) html+='<div class="fb-c">✅ Ton courriel contient tout ce qui était demandé.</div>';
    html+='<div class="fb-c">✍️ '+esc(data.corpsCorrige)+'</div>';
""",
        """    if(cmt) html+= data.pertinent ? '<div class="fb-c fb-bravo">'+esc(cmt)+'</div>'
                                  : '<div class="fb-e">'+esc(cmt)+'</div>';
    else if(data.pertinent) html+='<div class="fb-c fb-bravo">Ton courriel contient tout ce qui était demandé.</div>';
    html+='<div class="fb-c">'+esc(data.corpsCorrige)+'</div>';
""",
    ),
    (
        """  if(data.memePhrase){ html+='<div class="fb-c">✅ Ton texte est déjà correct. Bravo !</div>'; }
  else{
    if(corr) html+='<div class="fb-c">✍️ '+esc(corr)+'</div>';
""",
        """  if(data.memePhrase){ html+='<div class="fb-c fb-bravo">Ton texte est déjà correct. Bravo !</div>'; }
  else{
    if(corr) html+='<div class="fb-c">'+esc(corr)+'</div>';
""",
    ),
]


def paires():
    """Les pictogrammes sont substitués tard : le fichier de la greffe reste
    lisible, et les trois chaînes SVG ne vivent qu'à un seul endroit."""
    out = []
    for avant, apres in PAIRES:
        apres = apres.replace("%%BUSTE%%", BUSTE)
        out.append((avant, apres))
    return out


def poser(chemin, retirer):
    s = io.open(chemin, encoding="utf-8").read()
    ps = [(b, a) for a, b in paires()] if retirer else paires()
    if all(avant not in s for avant, _ in ps):
        return "déjà fait" if all(apres in s for _, apres in ps) else "introuvable"
    for avant, apres in ps:
        if avant not in s:
            return "partiel"
        s = s.replace(avant, apres, 1)
    io.open(chemin, "w", encoding="utf-8").write(s)
    return "retiré" if retirer else "greffé"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--retirer", action="store_true", help="revenir en arrière")
    args = ap.parse_args()
    compte = {}
    for chemin in [GABARIT] + sorted(glob.glob(TOUS)):
        etat = poser(chemin, args.retirer)
        compte[etat] = compte.get(etat, 0) + 1
        if etat in ("introuvable", "partiel"):
            print("  ! {} — {}".format(chemin, etat))
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 1 if compte.get("introuvable") or compte.get("partiel") else 0


if __name__ == "__main__":
    sys.exit(main())
