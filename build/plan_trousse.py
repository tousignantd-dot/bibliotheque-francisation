"""Le châssis commun des plans de trousse de métier (temps 0a de la méthode).

Troisième plan après la Maison Francœur (écrit à la main) et la réception d'hôtel
(`hotellerie_plan.py`, qui en garde une copie) : on industrialise. Un plan fournit
son titre, son corps HTML et ses décisions ; ce module pose l'en-tête du plan
Francœur (styles, cartes de décision), le correctif des tableaux sur téléphone,
et le script des décisions avec son export.

    from plan_trousse import ecrire
    ecrire(sortie, titre="…", corps="<section>…</section>", decisions=[…], cle="plan-x", plan="x")

Une décision : {"k": clé, "q": question, "o": [[valeur, libellé, recommandé?], …], "w": pourquoi}.
"""
import json, pathlib, re

RACINE = pathlib.Path(__file__).resolve().parent.parent
SOURCE = RACINE / "assets" / "presentations" / "magasin-vetements-plan.html"

# L'en-tête de Francœur pose table{min-width:640px} : à 375 px, les tableaux
# débordaient. Ils défilent dans leur propre cadre.
CSS_TELEPHONE = ("<style>table.cmp{display:block;max-width:100%;min-width:0;overflow-x:auto}"
                 "@media (max-width:640px){table.cmp{font-size:14px}table.cmp th,table.cmp td{padding:10px}"
                 "table.cmp td{min-width:9em}}</style>\n</head>")

SCRIPT = """<script>
(function(){
  var D = @@D@@;
  var CLE='@@CLE@@', choix={};
  try{ choix=JSON.parse(localStorage.getItem(CLE)||'{}'); }catch(e){}
  var zone=document.getElementById('decisions');
  D.forEach(function(d,i){
    var div=document.createElement('div'); div.className='dec2';
    var h='<p class="dq"><span class="dn">'+(i+1)+'</span>'+d.q+'</p><div class="opts">';
    d.o.forEach(function(o){
      h+='<button type="button" class="opt'+(o[2]?' reco':'')+'" data-k="'+d.k+'" data-v="'+o[0]+'" aria-pressed="false">'
        +o[1]+(o[2]?' <span class="tag">recommandé</span>':'')+'</button>';
    });
    div.innerHTML=h+'</div><p class="dw">'+d.w+'</p>';
    zone.appendChild(div);
  });
  function peindre(){
    zone.querySelectorAll('.opt').forEach(function(b){
      b.setAttribute('aria-pressed', choix[b.dataset.k]===b.dataset.v ? 'true':'false');
    });
    var n=Object.keys(choix).length;
    document.getElementById('etat').textContent = n+' décision'+(n>1?'s':'')+' sur '+D.length;
  }
  zone.addEventListener('click',function(e){
    var b=e.target.closest('.opt'); if(!b) return;
    if(choix[b.dataset.k]===b.dataset.v) delete choix[b.dataset.k]; else choix[b.dataset.k]=b.dataset.v;
    try{ localStorage.setItem(CLE,JSON.stringify(choix)); }catch(e){}
    peindre();
  });
  var note=document.getElementById('note');
  if(note){ try{ note.value=localStorage.getItem(CLE+'-note')||''; }catch(e){}
    note.addEventListener('input',function(){ try{ localStorage.setItem(CLE+'-note',note.value); }catch(e){} }); }
  document.getElementById('exporter').addEventListener('click',function(){
    var out={plan:'@@PLAN@@', date:new Date().toISOString().slice(0,10), decisions:{}, note:note?note.value:''};
    D.forEach(function(d){
      var v=choix[d.k]; var o=d.o.filter(function(x){return x[0]===v;})[0];
      out.decisions[d.k]= o ? o[1] : null;
    });
    var t=JSON.stringify(out,null,2);
    var fin=function(){ document.getElementById('etat').textContent='Copié — à recoller dans la conversation.'; };
    if(navigator.clipboard) navigator.clipboard.writeText(t).then(fin,function(){prompt('Copiez :',t);});
    else prompt('Copiez :',t);
  });
  peindre();
})();
</script>"""

BLOC_DECISIONS = """<section>
  <h2>Les décisions</h2>
  <p>Chacune a une recommandation ; un clic la retient. Le bouton du bas rend un texte à recoller dans
  la conversation : c'est lui qui pilote la suite.</p>
  <div id="decisions"></div>
  <p style="margin-top:1rem"><b>Ce qui manque au plan</b> (facultatif) :</p>
  <textarea id="note" rows="3" style="width:100%;font:inherit;font-size:15px;padding:10px;border-radius:10px;border:1px solid var(--line-fort);background:var(--card);color:var(--ink);box-sizing:border-box"></textarea>
  <p style="margin-top:1.2rem"><button type="button" class="btn-export" id="exporter">Exporter mes décisions</button>
  <span id="etat" class="etat"></span></p>
</section>"""


def ecrire(sortie, titre, corps, decisions, cle, plan, pied):
    tete = SOURCE.read_text(encoding="utf-8")
    tete = tete[:tete.index("<body")]
    tete = re.sub(r"<title>.*?</title>", f"<title>{titre}</title>", tete)
    tete = tete.replace("</head>", CSS_TELEPHONE, 1)
    for d in decisions:
        assert sum(1 for o in d["o"] if o[2]) == 1, f"{d['k']} : il faut exactement une recommandation"
    script = (SCRIPT.replace("@@D@@", json.dumps(decisions, ensure_ascii=False))
              .replace("@@CLE@@", cle).replace("@@PLAN@@", plan))
    html = (tete + '<body>\n<div class="doc">\n' + corps + BLOC_DECISIONS
            + f'\n<div class="pied">{pied}</div>\n</div>\n' + script + "\n</body>\n</html>\n")
    sortie = pathlib.Path(sortie)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    sortie.write_text(html, encoding="utf-8")
    return sortie
