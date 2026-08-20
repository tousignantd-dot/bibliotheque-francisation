#!/usr/bin/env python3
"""Cartes mémoire : boutons plus discrets et traduction dans la langue de l'élève.

Les onze modules portent la même surcouche `#fc-overlay`, écrite à l'identique
dans chaque fichier. On la retouche donc ici plutôt qu'à la main onze fois :
trois substitutions exactes, refusées si le texte attendu n'est pas trouvé tel
quel — mieux vaut ne rien changer qu'écrire à l'aveugle dans un module qui
aurait divergé.

  python3 build/cartes_memoire.py            → tous les modules (sauf module-probleme)
  python3 build/cartes_memoire.py --verifier  → dit qui est à jour, n'écrit rien

module-probleme est GÉNÉRÉ à partir de module-consultation : on le laisse de
côté et on relance `python3 build/module.py module-probleme` après coup.
"""
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
GENERE = {'module-probleme'}

# ── 1. Les boutons de navigation ──────────────────────────────────────
# 15 px et 22 px de flanc dans une carte de 760 px : trois pavés qui pesaient
# plus lourd que le mot à apprendre. On garde la cible tactile (≥ 34 px de
# haut) mais on rend la place au vocabulaire.
CSS_AV = (".fc-btn{background:rgba(255,255,255,.15);border:2px solid rgba(255,255,255,.38);"
          "color:#fff;border-radius:10px;padding:10px 22px;font-family:'Nunito',sans-serif;"
          "font-size:15px;font-weight:800;cursor:pointer}")
CSS_AP = (".fc-btn{background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.38);"
          "color:#fff;border-radius:8px;padding:6px 14px;font-family:'Nunito',sans-serif;"
          "font-size:13px;font-weight:800;cursor:pointer}\n"
          "/* ── Traduction dans la langue de l'élève ───────────────────────────\n"
          "   Le français ne bouge pas : la traduction s'ajoute sous un filet,\n"
          "   comme le fait le rail « Mes outils ». */\n"
          "#fc-sep{width:100%;height:1px;background:rgba(255,255,255,.20);margin:2px 0}\n"
          "#fc-trad-btn{background:transparent;border:1px solid rgba(255,255,255,.45);color:#fff;"
          "border-radius:8px;padding:6px 14px;font-family:'Nunito',sans-serif;font-size:13px;"
          "font-weight:800;cursor:pointer}\n"
          "#fc-trad-btn:hover{background:rgba(255,255,255,.18)}\n"
          "#fc-trad-btn[disabled]{opacity:.5;cursor:default}\n"
          "#fc-trad-btn.hidden,#fc-trad.hidden{display:none}\n"
          "#fc-trad{width:100%;background:rgba(255,255,255,.12);border-radius:10px;padding:12px 16px;"
          "font-size:19px;font-weight:700;color:#fff;line-height:1.55;text-align:center}\n"
          "#fc-trad.att{font-size:14px;font-weight:600;color:rgba(255,255,255,.75);"
          "background:transparent;padding:4px}")

# ── 2. Le balisage ────────────────────────────────────────────────────
HTML_AV = """    <div id="fc-btns">"""
HTML_AP = """    <div id="fc-sep"></div>
    <button class="fc-btn" id="fc-trad-btn">Traduire</button>
    <div id="fc-trad" class="hidden"></div>
    <div id="fc-btns">"""

# ── 3. Le script ──────────────────────────────────────────────────────
JS_AV = """  document.getElementById('fc-reveal-btn').classList.remove('hidden');
}"""
JS_AP = """  document.getElementById('fc-reveal-btn').classList.remove('hidden');
  fcTradRaz();
}
// Chaque carte repart sans traduction : celle de la carte précédente,
// laissée à l'écran, se lirait comme la traduction du nouveau mot.
function fcTradRaz(){
  const b=document.getElementById('fc-trad-btn'), z=document.getElementById('fc-trad');
  if(!b||!z) return;
  z.className='hidden'; z.textContent=''; z.removeAttribute('dir');
  b.classList.remove('hidden'); b.disabled=false;
  const L=(window.Outils&&Outils.langue)?Outils.langue():null;
  b.textContent=L?('Traduire en '+L.n):'Traduire';
}
document.getElementById('fc-trad-btn').addEventListener('click',()=>{
  const c=FC_CARDS[fcIdx], b=document.getElementById('fc-trad-btn'), z=document.getElementById('fc-trad');
  if(!window.Outils||!Outils.traduire){
    z.className='att'; z.textContent="La traduction n'est pas disponible hors ligne."; return;
  }
  b.disabled=true; z.className='att'; z.textContent='Je traduis…';
  // La définition part en contexte, pas en texte à traduire : elle guide le
  // sens du mot sans dévoiler la réponse à l'élève qui n'a pas encore révélé.
  Outils.traduire(c.word, c.def).then(r=>{
    z.className=''; if(r.langue.rtl) z.setAttribute('dir','rtl');
    z.textContent=r.texte; b.classList.add('hidden');
  }).catch(e=>{ z.className='att'; z.textContent=e.message; b.disabled=false; });
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
        if CSS_AP.splitlines()[0] in t and 'fcTradRaz' in t:
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
    print('\nmodule-probleme est généré : relancer build/module.py module-probleme')
    return 1 if souci else 0


if __name__ == '__main__':
    raise SystemExit(main())
