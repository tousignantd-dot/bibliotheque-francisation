"""Couper la voix de l'assistant n'est pas une panne de la voix de l'assistant.

Constaté en classe le 31 août 2026 : l'élève touche le micro pendant que la
propriétaire parle — geste normal, on lui coupe la parole — et c'est la voix
du navigateur qui reprend la réplique depuis le début, en anglais de synthèse.

Le chemin exact. `jrParler()` appelle `jrTaire()` en premier, sinon le micro
réentend l'assistant. Si `a.play()` était encore en vol, cette pause le fait
**rejeter** (AbortError), le `catch` de `jrDire` s'exécute — et ce catch n'a
qu'une réponse : `jrDireNavigateur(texte)`, le repli prévu pour une panne de
serveur. Un arrêt voulu était donc traité comme une panne.

La greffe donne un numéro à chaque lecture. `jrTaire()` l'incrémente, ce qui
rend caduque toute lecture en vol ; `jrDire` ne se replie sur la voix du
navigateur que si SON numéro est encore le courant. Une vraie panne de serveur
garde donc son repli, une interruption volontaire se tait.

Au passage : la réponse qui revient d'un fetch devenu caduc n'est plus jouée du
tout. Sans ça, l'élève pouvait entendre démarrer une réplique qu'il venait
d'interrompre.

    python3 build/greffe_voix_interrompue.py            # gabarit + 78 modules
    python3 build/greffe_voix_interrompue.py --retirer  # revient en arrière
"""

import argparse
import glob
import io
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

PAIRES = [
    (
        """let jrAudio=null;

function jrTaire(){
  try{ speechSynthesis.cancel(); }catch(e){}
  if(jrAudio){ try{ jrAudio.pause(); }catch(e){} jrAudio=null; }
}
""",
        """let jrAudio=null;
// Numéro de la lecture en cours. Il sert à distinguer un arrêt VOULU — l'élève
// touche le micro pendant que l'assistant parle — d'une panne de serveur : les
// deux se présentent au code sous la même forme, une promesse rejetée.
let jrDireNo=0;

function jrTaire(){
  jrDireNo++;                 // toute lecture en vol devient caduque
  try{ speechSynthesis.cancel(); }catch(e){}
  if(jrAudio){ try{ jrAudio.pause(); }catch(e){} jrAudio=null; }
}
""",
    ),
    # L'ancien texte reprend la ligne du palier, posée par
    # greffe_debit_jeu_de_role : sans elle il serait un préfixe du nouveau, et
    # la greffe se croirait à refaire à chaque passage.
    (
        """async function jrDire(texte){
  jrTaire();
  // Cette voix-ci se fabrique en direct : son débit se règle donc à la
""",
        """async function jrDire(texte){
  jrTaire();
  const no=jrDireNo;          // posé APRÈS jrTaire, qui vient d'incrémenter
  // Cette voix-ci se fabrique en direct : son débit se règle donc à la
""",
    ),
    (
        """    if(!res.ok) throw new Error('voix serveur indisponible');
    const url=URL.createObjectURL(await res.blob());
    const a=new Audio(url);
""",
        """    if(!res.ok) throw new Error('voix serveur indisponible');
    const blob=await res.blob();
    // L'élève a repris la parole pendant que le serveur synthétisait : ne rien
    // jouer du tout, plutôt que de démarrer une réplique qu'il vient de couper.
    if(no!==jrDireNo) return;
    const url=URL.createObjectURL(blob);
    const a=new Audio(url);
""",
    ),
    (
        """  }catch(e){
    jrDireNavigateur(texte);
  }
}
""",
        """  }catch(e){
    // Le repli n'a de sens que pour une vraie panne. Si un jrTaire() est passé
    // par là, c'est que l'élève a coupé la parole : on se tait.
    if(no===jrDireNo) jrDireNavigateur(texte);
  }
}
""",
    ),
]


def cibles():
    fichiers = [GABARIT] + sorted(glob.glob(TOUS))
    return [c for c in fichiers
            if "async function jrDire(" in io.open(c, encoding="utf-8").read()]


def poser(chemin, retirer):
    s = io.open(chemin, encoding="utf-8").read()
    ps = [(b, a) for a, b in PAIRES] if retirer else PAIRES
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
    for chemin in cibles():
        etat = poser(chemin, args.retirer)
        compte[etat] = compte.get(etat, 0) + 1
        if etat in ("introuvable", "partiel"):
            print("  ! {} — {}".format(chemin, etat))
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 1 if compte.get("introuvable") or compte.get("partiel") else 0


if __name__ == "__main__":
    sys.exit(main())
