#!/usr/bin/env python3
"""Cartes mémoire : la liste des mots à portée de main.

En plein écran, la carte mémoire cache la page — donc aussi la grille des
mots du dialogue. L'élève qui cherche un mot précis n'a que « Suivante »
pour l'atteindre, et celui qui bloque n'a plus la liste sous les yeux. On
ajoute donc dans l'encart le même appui que dans les trois pages de
vocabulaire : un bouton « Voir les mots » qui déplie tous les mots de la
série. Ici les mots sont cliquables — ils mènent à leur carte.

Onze modules, une seule surcouche écrite à l'identique : on la pose ici
plutôt qu'à la main onze fois. Trois substitutions exactes, refusées si le
texte attendu n'est pas trouvé tel quel.

  python3 build/cartes_memoire_liste.py            → tous les modules (sauf module-probleme)
  python3 build/cartes_memoire_liste.py --verifier  → dit qui est à jour, n'écrit rien

module-probleme est GÉNÉRÉ à partir de module-consultation : on le laisse de
côté et on relance `python3 build/module-probleme/build.py` après coup.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
GENERE = {'module-probleme'}

# ── 1. Le style ───────────────────────────────────────────────────────
# Rien en dur : les onze encarts partagent aujourd'hui le même bleu, mais la
# liste se peint quand même en blanc translucide, comme les boutons qui
# l'entourent — le jour où un module changera de teinte, elle suivra.
CSS_AV = "#fc-btns{display:flex;gap:14px;margin-top:6px;flex-wrap:wrap;justify-content:center}"
CSS_AP = ("#fc-btns{display:flex;gap:14px;margin-top:6px;flex-wrap:wrap;justify-content:center}\n"
          "/* ── La liste des mots de la série ──────────────────────────────────\n"
          "   Dépliée, elle reste dépliée d'une carte à l'autre : l'élève qui a\n"
          "   besoin de la liste en a besoin partout. Le mot affiché est marqué\n"
          "   par un cadre plein, jamais par la seule couleur. */\n"
          "#fc-liste{width:100%;max-height:34vh;overflow-y:auto;display:flex;flex-wrap:wrap;"
          "gap:8px;justify-content:center;padding-top:14px;border-top:1px solid rgba(255,255,255,.20)}\n"
          "#fc-liste.hidden{display:none}\n"
          ".fc-mot{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.30);color:#fff;"
          "border-radius:999px;padding:6px 14px;font-family:'Nunito',sans-serif;font-size:13px;"
          "font-weight:800;cursor:pointer}\n"
          ".fc-mot:hover{background:rgba(255,255,255,.24)}\n"
          ".fc-mot[aria-current=\"true\"]{background:rgba(255,255,255,.92);"
          "border-color:rgba(255,255,255,.92);color:#1a2733}")

# ── 2. Le balisage ────────────────────────────────────────────────────
HTML_AV = """      <button class="fc-btn" id="fc-close">✕ Fermer</button>
    </div>"""
HTML_AP = """      <button class="fc-btn" id="fc-liste-btn" aria-expanded="false" aria-controls="fc-liste">Voir les mots</button>
      <button class="fc-btn" id="fc-close">✕ Fermer</button>
    </div>
    <div id="fc-liste" class="hidden"></div>"""

# ── 3. Le script ──────────────────────────────────────────────────────
JS_AV = """  fcTradRaz();
}"""
JS_AP = """  fcTradRaz();
  fcListeMaj();
}
// La liste des mots : bâtie une fois, marquée à chaque carte.
const FC_CLE_LISTE='francisationCartesListeMots';
let fcListeOuverte=localStorage.getItem(FC_CLE_LISTE)==='1';
function fcListeBatir(){
  const z=document.getElementById('fc-liste');
  if(!z||z.childElementCount) return;
  FC_CARDS.forEach((c,i)=>{
    const b=document.createElement('button');
    b.type='button'; b.className='fc-mot'; b.textContent=c.word;
    b.addEventListener('click',()=>{fcIdx=i;fcShow()});
    z.appendChild(b);
  });
}
function fcListeMaj(){
  const b=document.getElementById('fc-liste-btn'), z=document.getElementById('fc-liste');
  if(!b||!z) return;
  fcListeBatir();
  b.setAttribute('aria-expanded',fcListeOuverte?'true':'false');
  b.textContent=fcListeOuverte?'Cacher les mots':'Voir les mots';
  z.classList.toggle('hidden',!fcListeOuverte);
  [...z.children].forEach((m,i)=>m.setAttribute('aria-current',i===fcIdx?'true':'false'));
}
document.getElementById('fc-liste-btn').addEventListener('click',()=>{
  fcListeOuverte=!fcListeOuverte;
  localStorage.setItem(FC_CLE_LISTE,fcListeOuverte?'1':'0');
  fcListeMaj();
});"""

PAIRES = [(CSS_AV, CSS_AP), (HTML_AV, HTML_AP), (JS_AV, JS_AP)]


def modules():
    for d in sorted(INTER.glob('module-*')):
        f = d / f'{d.name}-activite-interactive.html'
        if f.exists() and d.name not in GENERE:
            yield d.name, f


def main():
    verifier = '--verifier' in sys.argv
    souci = 0
    for nom, f in modules():
        t = f.read_text(encoding='utf-8')
        if 'fcListeMaj' in t:
            print(f'    {nom} : déjà à jour')
            continue
        manquants = [i for i, (av, _) in enumerate(PAIRES, 1) if t.count(av) != 1]
        if manquants:
            print(f'!!  {nom} : texte attendu introuvable ({manquants}) — non modifié')
            souci += 1
            continue
        if verifier:
            print(f'    {nom} : à mettre à jour')
            continue
        for av, ap in PAIRES:
            t = t.replace(av, ap, 1)
        f.write_text(t, encoding='utf-8')
        print(f'ok  {nom}')
    print('\nmodule-probleme est généré : relancer build/module-probleme/build.py')
    return 1 if souci else 0


if __name__ == '__main__':
    raise SystemExit(main())
