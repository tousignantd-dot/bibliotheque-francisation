#!/usr/bin/env python3
"""La liste des mots dans les cartes mémoire des activités (hors modules).

Les onze modules ont reçu ce bouton par build/cartes_memoire_liste.py. Les
activités de la bibliothèque ont la même carte mémoire, mais pas le même
balisage : elles viennent de deux générations différentes.

  · « simple »  : le fichier HTML est lisible tel quel (3 activités).
  · « bundle »  : la page entière est une chaîne JSON dans un
    <script type="__bundler/template"> (12 activités). On n'y touche que par
    substitution du texte ÉCHAPPÉ : nos quelques octets changent, le reste du
    fichier (1,8 Mo d'images inlinées) n'est jamais réécrit.

Et les fonctions ne portent pas les mêmes noms d'une génération à l'autre
(fcShow, showCard, ou fcOpen qui rend et ouvre à la fois). Le script injecté
ne suppose donc rien : il n'utilise que FC_CARDS, fcOpen, et le mot affiché
à l'écran pour savoir quelle pastille marquer.

  python3 build/cartes_memoire_liste_activites.py            → écrit
  python3 build/cartes_memoire_liste_activites.py --verifier  → n'écrit rien

Les activités sans carte mémoire sont ignorées : il n'y a pas de liste de
mots à y montrer.
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTER = ROOT / 'assets/interactive'
HORS = ('module-', 'vocab-flash-', 'vocabulaire-flash')
TEMPLATE = re.compile(r'<script type="__bundler/template">')
TEMOIN = 'fc-liste-btn'

# ── 1. Le style ───────────────────────────────────────────────────────
# Posé juste avant la règle des boutons, en blanc translucide comme eux :
# l'encart n'a pas la même couleur partout, la liste ne peut donc pas
# choisir la sienne.
ANCRE_CSS = '#fc-btns{'
CSS = """/* ── La liste des mots de la série ──────────────────────────────────
   Dépliée, elle reste dépliée d'une carte à l'autre : l'élève qui a
   besoin de la liste en a besoin partout. Le mot affiché est marqué par
   un cadre plein, jamais par la seule couleur. */
#fc-liste{width:100%;max-height:34vh;overflow-y:auto;display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding-top:14px;margin-top:4px;border-top:1px solid rgba(255,255,255,.20)}
#fc-liste.hidden{display:none}
.fc-mot{background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.30);color:#fff;border-radius:999px;padding:6px 14px;font-family:'Nunito',sans-serif;font-size:13px;font-weight:800;cursor:pointer}
.fc-mot:hover{background:rgba(255,255,255,.24)}
.fc-mot[aria-current="true"]{background:rgba(255,255,255,.92);border-color:rgba(255,255,255,.92);color:#1a2733}
"""

# ── 2. Le balisage ────────────────────────────────────────────────────
ANCRE_BTNS = '<div id="fc-btns">'
BOUTON = '<button class="fc-btn" id="fc-liste-btn" aria-expanded="false" aria-controls="fc-liste">Voir les mots</button>'
PANNEAU = '\n    <div id="fc-liste" class="hidden"></div>'

# ── 3. Le script ──────────────────────────────────────────────────────
# Ajouté en fin de body : les fonctions fc* sont des déclarations, donc
# déjà posées sur window, et FC_CARDS — un const de premier niveau — est
# visible depuis tout script classique suivant.
ANCRE_BODY = '</body>'
SCRIPT = """<script>
/* ── La liste des mots dans la carte mémoire ─────────────────────────
   Écrit par build/cartes_memoire_liste_activites.py — ne pas éditer ici.
   Le mot courant est lu à l'écran plutôt que dans un compteur interne :
   c'est le seul repère que les trois générations de cartes partagent. */
(function(){
  var btn=document.getElementById('fc-liste-btn'), box=document.getElementById('fc-liste');
  if(!btn||!box||typeof FC_CARDS==='undefined'||typeof fcOpen!=='function') return;
  var CLE='francisationCartesListeMots';
  var ouverte=localStorage.getItem(CLE)==='1';
  FC_CARDS.forEach(function(c,i){
    var m=document.createElement('button');
    m.type='button'; m.className='fc-mot'; m.textContent=c.word;
    m.addEventListener('click',function(){ fcOpen(i); });
    box.appendChild(m);
  });
  function maj(){
    btn.setAttribute('aria-expanded',ouverte?'true':'false');
    btn.textContent=ouverte?'Cacher les mots':'Voir les mots';
    box.classList.toggle('hidden',!ouverte);
    var mot=(document.getElementById('fc-word')||{}).textContent||'';
    [].forEach.call(box.children,function(m){
      m.setAttribute('aria-current',m.textContent===mot?'true':'false');
    });
  }
  btn.addEventListener('click',function(){
    ouverte=!ouverte;
    localStorage.setItem(CLE,ouverte?'1':'0');
    maj();
  });
  // Selon la génération, la carte est peinte par fcShow, par showCard, ou
  // par fcOpen lui-même. On enveloppe celles qui existent — marquer deux
  // fois ne coûte rien, ne pas marquer laisserait la liste mentir.
  ['fcShow','showCard','fcOpen'].forEach(function(n){
    if(typeof window[n]!=='function') return;
    var o=window[n];
    window[n]=function(){ var r=o.apply(this,arguments); maj(); return r; };
  });
  maj();
})();
</script>
"""


def echapper(s):
    """Le même texte, écrit comme il le serait dans la chaîne JSON.

    Seul `</script>` est traité, et il sort en `<\\/script>` — exactement ce
    que fait le gabarit. Nu, il refermerait la balise qui porte toute la page
    et couperait le fichier en deux. Les autres balises fermantes restent
    telles quelles : le gabarit ne les échappe pas non plus, et les échapper
    ferait rater les ancres.
    """
    return json.dumps(s, ensure_ascii=False)[1:-1].replace('</script>', r'<\/script>')


def poser(t, esc, dans_rangee):
    """Les trois insertions, sur du texte nu ou sur du texte échappé."""
    a_css, a_btns, a_body = esc(ANCRE_CSS), esc(ANCRE_BTNS), esc(ANCRE_BODY)
    for a in (a_css, a_btns):
        if t.count(a) != 1:
            return None, f'ancre {a[:24]!r} vue {t.count(a)} fois'
    # Un fichier bundle a deux </body> : celui de la page emballée et celui
    # de l'emballage, tout à la fin. Le nôtre est le premier qui suit la
    # rangée de boutons — l'autre fermerait la coquille, pas l'activité.
    fin = t.find(a_body, t.index(a_btns))
    if fin < 0:
        return None, 'aucun </body> après #fc-btns'

    # Le style, juste avant la règle des boutons.
    t = t.replace(a_css, esc(CSS) + a_css, 1)

    # Le panneau se pose juste après la rangée de boutons. La rangée n'a pas
    # de div imbriqué : le premier </div> est bien le sien.
    i = t.index(a_btns) + len(a_btns)
    ferme = esc('</div>')
    j = t.index(ferme, i)
    if esc('<div') in t[i:j]:
        return None, 'div imbriqué dans #fc-btns'
    t = t[:j + len(ferme)] + esc(PANNEAU) + t[j + len(ferme):]

    # Le bouton, lui, dépend de la génération. Dans la deuxième, la rangée
    # reste cachée tant que la définition n'est pas révélée : un bouton posé
    # dedans serait hors d'atteinte au moment précis où l'élève le cherche.
    # On le met alors juste avant la rangée, sous « Révéler la définition ».
    if dans_rangee:
        t = t[:j] + esc('      ' + BOUTON + '\n    ') + t[j:]
    else:
        k = t.index(a_btns)
        t = t[:k] + esc(BOUTON + '\n    ') + t[k:]

    # Le script, en fin de body. On recale la position : les insertions
    # ci-dessus ont décalé le texte.
    fin = t.find(a_body, t.index(a_btns))
    t = t[:fin] + esc(SCRIPT) + t[fin:]
    return t, None


def fichiers():
    for d in sorted(INTER.iterdir()):
        if not d.is_dir() or d.name.startswith(HORS):
            continue
        for f in sorted(d.glob('*.html')):
            yield d.name, f
            break


def main():
    verifier = '--verifier' in sys.argv
    faits = souci = sans = deja = 0
    for nom, f in fichiers():
        t = f.read_text(encoding='utf-8')
        bundle = bool(TEMPLATE.search(t))
        esc = echapper if bundle else (lambda s: s)
        if esc(ANCRE_BTNS) not in t:
            sans += 1
            continue
        if TEMOIN in t:
            print(f'    {nom} : déjà à jour')
            deja += 1
            continue
        if verifier:
            print(f'    {nom} ({"bundle" if bundle else "simple"}) : à mettre à jour')
            faits += 1
            continue
        neuf, err = poser(t, esc, dans_rangee=not bundle)
        if err:
            print(f'!!  {nom} : {err} — non modifié')
            souci += 1
            continue
        f.write_text(neuf, encoding='utf-8')
        print(f'ok  {nom} ({"bundle" if bundle else "simple"})')
        faits += 1
    print(f'\n{faits} activité(s) · {deja} déjà à jour · {sans} sans carte mémoire · {souci} refus')
    return 1 if souci else 0


if __name__ == '__main__':
    raise SystemExit(main())
