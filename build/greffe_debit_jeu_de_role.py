"""Le débit du jeu de rôle se règle à la synthèse, plus dans le navigateur.

Le jeu de rôle est la seule voix du cours qui se fabrique en direct : sa
réplique n'existe pas avant d'être demandée. Le bouton « Débit lent » la
traitait pourtant comme un MP3 de module — `playbackRate = 0,8` sur un son
déjà produit, ce qui l'abîme. Depuis le 31 août 2026, le module envoie son
palier à `/api/voix`, Azure applique un `<prosody rate="-20%">` exact, et le
serveur répond `X-Palier` pour dire ce qu'il a fait.

Le navigateur n'étire donc plus que si le serveur n'a pas honoré le palier —
un serveur d'avant ce jour, ou la voix de secours du navigateur. Sans cet
en-tête, un module greffé posé devant un serveur ancien rendrait un « débit
lent » qui parle vite, et un module non greffé devant un serveur neuf
ralentirait deux fois.

La greffe accompagne le passage des deux rôles du jeu de rôle au modèle
DragonHD (`build/azure_voix.py`, rôles `jr_feminin` et `jr_masculin`) : c'est
le même chantier, la voix HD étant justement celle qu'on ne veut pas étirer.

    python3 build/greffe_debit_jeu_de_role.py            # gabarit + 87 modules
    python3 build/greffe_debit_jeu_de_role.py --retirer  # revient en arrière

Idempotente. Les neuf modules sans jeu de rôle ne reçoivent que la retouche de
`vitAppliquer`, qui les concerne aussi.
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

PAIRES = [
    # 1. La demande porte le palier ; l'étirement local devient un repli.
    (
        """async function jrDire(texte){
  jrTaire();
  try{
    const res=await fetch('/api/voix',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({code:studentCode, texte:texte, role:JR.role})});
    if(!res.ok) throw new Error('voix serveur indisponible');
    const url=URL.createObjectURL(await res.blob());
    const a=vitAudio(new Audio(url)); jrAudio=a;
""",
        """async function jrDire(texte){
  jrTaire();
  // Cette voix-ci se fabrique en direct : son débit se règle donc à la
  // SYNTHÈSE, où Azure rend un <prosody rate> exact, et non par un
  // playbackRate qui étire un son déjà produit. Le serveur répond X-Palier ;
  // on n'étire ici que s'il n'a pas honoré la demande.
  const palier = vitCran ? 'lent' : 'normal';
  try{
    const res=await fetch('/api/voix',{method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({code:studentCode, texte:texte, role:JR.role, palier:palier})});
    if(!res.ok) throw new Error('voix serveur indisponible');
    const url=URL.createObjectURL(await res.blob());
    const a=new Audio(url);
    if(res.headers.get('X-Palier')===palier) a.dataset.palier=palier; else vitAudio(a);
    jrAudio=a;
""",
    ),
    # 2. Le bouton ne repasse pas sur un son que le serveur a déjà ralenti.
    (
        """  if(typeof jrAudio !== 'undefined' && jrAudio) vitAudio(jrAudio);
""",
        """  // `dataset.palier` marque un son déjà ralenti à la synthèse : y ajouter
  // un playbackRate le ralentirait deux fois.
  if(typeof jrAudio !== 'undefined' && jrAudio && !jrAudio.dataset.palier) vitAudio(jrAudio);
""",
    ),
]


def poser(chemin, retirer):
    s = io.open(chemin, encoding="utf-8").read()
    paires = [(b, a) for a, b in PAIRES] if retirer else PAIRES
    faits = 0
    for avant, apres in paires:
        if avant in s:
            s = s.replace(avant, apres, 1)
            faits += 1
        elif apres not in s:
            # Ni l'un ni l'autre : le module n'a pas de jeu de rôle.
            continue
    if not faits:
        return "déjà fait"
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
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 0


if __name__ == "__main__":
    sys.exit(main())
