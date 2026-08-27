#!/usr/bin/env python3
"""
Produit le gabarit commun des modules : `build/gabarit/module.html`.

Pourquoi ce fichier existe
--------------------------
Jusqu'ici, chaque module neuf était fabriqué par un script à lui qui partait du
HTML de `module-consultation` et lui appliquait quatre-vingt-dix kilo-octets de
retouches — la section vocabulaire à trois exercices, le moteur de jeu de rôle,
les blocs de production refaits, la grille des réponses courtes, les tuiles
Vrai/Faux à largeur variable. Ces retouches n'ont rien de propre à un module :
elles valent pour tous. Les laisser captives du script d'un seul module
obligeait à les recopier à chaque fois, et une correction de design devait être
refaite dix-huit fois.

Ce script les applique **une fois** et fige le résultat en gabarit, avec des
jetons `%%NOM%%` là où le contenu et l'identité d'un module viennent se poser.
`build/module.py` n'a plus qu'à remplir les jetons.

    python3 build/gabarit.py            # régénère build/gabarit/module.html

À relancer seulement quand `module-consultation` reçoit une amélioration de
moteur qui doit profiter à tous les modules. Le contenu pédagogique de la
consultation ne passe jamais dans le gabarit : il est remplacé par des jetons.

Les ressources génériques que le gabarit incorpore (`production.css`,
`vocab.css`, `vocab.js`) vivent à côté de lui, dans `build/gabarit/`.
"""
import re
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
GAB = ROOT / 'build/gabarit'
SRC = ROOT / 'assets/interactive/module-consultation/module-consultation-activite-interactive.html'
LOG = ROOT / 'assets/interactive/module-logement/module-logement-activite-interactive.html'
DST = GAB / 'module.html'


def fatal(msg):
    sys.exit('!! %s' % msg)


def lire(nom):
    return (GAB / nom).read_text(encoding='utf-8')


def upgrade(text, old, new, label):
    """Applique une amélioration en tolérant qu'elle soit déjà faite.

    On teste la forme NEUVE en premier : plusieurs substitutions ajoutent du
    texte autour du repère, si bien que l'ancienne forme reste un fragment de
    la nouvelle. Dans l'autre ordre, on appliquerait deux fois une retouche
    déjà faite et on dupliquerait des définitions de fonctions.
    """
    if new in text:
        return text
    if text.count(old) == 1:
        return text.replace(old, new, 1)
    fatal('%s : ni l\'ancienne ni la nouvelle forme dans le gabarit' % label)


def retirer(text, ligne, label):
    """Supprime une ligne devenue inutile, en tolérant qu'elle soit déjà partie.

    `upgrade()` ne sait pas faire ça : elle teste `new in text` d'abord, et la
    chaîne vide est dans tout texte. Une suppression écrite avec elle ne
    s'exécute jamais.
    """
    n = text.count(ligne)
    if n == 0:
        return text
    if n > 1:
        fatal('%s : la ligne apparaît %d fois' % (label, n))
    return text.replace(ligne, '', 1)


def slice_between(text, start_marker, end_marker, label):
    a = text.find(start_marker)
    if a < 0:
        fatal('%s : début introuvable' % label)
    b = text.find(end_marker, a)
    if b < 0:
        fatal('%s : fin introuvable' % label)
    return text[a:b + len(end_marker)]


def remplacer_entre(text, debut, fin, nouveau, label):
    """Remplace la région [debut, fin). `fin` reste dans le texte : c'est le
    repère du bloc suivant, pas la fin de la région."""
    a = text.find(debut)
    if a < 0:
        fatal('%s : début introuvable (%r)' % (label, debut[:50]))
    b = text.find(fin, a)
    if b < 0:
        fatal('%s : fin introuvable (%r)' % (label, fin[:50]))
    return text[:a] + nouveau.strip() + '\n\n' + text[b:]


def region_jeton(html, const_name, end_marker, jeton):
    """Remplace `const X = ...` jusqu'au marqueur de fin par un jeton.

    Marqueur SANS saut de ligne : un marqueur qui en contient un saute
    silencieusement jusqu'au bloc suivant et avale la constante d'après.
    """
    start = html.find('const %s = ' % const_name)
    if start < 0:
        fatal('const %s introuvable' % const_name)
    end = html.find(end_marker, start)
    if end < 0:
        fatal('marqueur de fin %r introuvable pour %s' % (end_marker, const_name))
    return html[:start] + jeton + html[end + len(end_marker):]


# ══════════════════════════════════════════════════════════════════════
#  1. Améliorations de moteur, communes à tous les modules
# ══════════════════════════════════════════════════════════════════════

def ameliorer(html):
    # 1a. Réponses courtes sur deux colonnes : une réponse d'un ou deux mots
    # occupait toute la largeur de l'écran.
    html = upgrade(
        html,
        '.wlist{display:flex;flex-direction:column;gap:14px}',
        '.wlist{display:grid;grid-template-columns:1fr;gap:14px}\n'
        '.wlist.wcols2{grid-template-columns:repeat(2,minmax(0,1fr))}\n'
        '.wlist.wcols2 .winput{min-width:0}\n'
        '.wlist.wcols2 .wq{font-size:14.5px}\n'
        '@media(max-width:700px){.wlist.wcols2{grid-template-columns:1fr}}',
        'grille des réponses courtes')
    html = upgrade(
        html,
        "h+=aiBadge+'<div class=\"wlist\">';",
        "h+=aiBadge+'<div class=\"wlist'+(ex.cols===2?' wcols2':'')+'\">';",
        'classe wcols2')

    # 1b. Tuiles Vrai/Faux à largeur variable : figées à 72 px, une étiquette
    # longue débordait et se lisait « LOCATAIREPROPRIÉTAIRE ».
    html = upgrade(
        html,
        '.vf-head-opt{width:72px;flex:0 0 72px;',
        '.vf-head-opt{width:var(--vfw,72px);flex:0 0 var(--vfw,72px);',
        "largeur de l'en-tête Vrai/Faux")
    html = upgrade(
        html,
        '.vf-opt{width:72px;flex:0 0 72px;',
        '.vf-opt{width:var(--vfw,72px);flex:0 0 var(--vfw,72px);padding:0 6px;',
        'largeur des tuiles Vrai/Faux')
    html = upgrade(
        html,
        '.vf-summary{font-size:13px;font-weight:800}',
        '@media(max-width:620px){\n'
        '  .vf-head{display:none}\n'
        '  .vf-opts{margin-left:0;width:100%}\n'
        '  .vf-opt{flex:1 1 0;width:auto}\n'
        '}\n'
        '.vf-summary{font-size:13px;font-weight:800}',
        'tuiles Vrai/Faux sous 620 px')
    # 1c. Association d'images : le moteur ne lisait que `aid`, la clé de
    # `module-consultation`. Tous les modules assemblés depuis build/contenu
    # écrivent `ok` sur les rangées d'un `imgmatch` — la zone n'avait donc pas
    # de bonne réponse et aucune photo n'était jamais acceptée. On lit `ok`
    # d'abord, `aid` ensuite pour les deux modules historiques.
    html = upgrade(
        html,
        "  if (ex.type === 'imgmatch') ex.rows.forEach(r => ZONES[r.id] = "
        "{cv:r.aid, zcat:'id', exo:ex.id});",
        "  // imgmatch : la bonne image est sous `ok` (comme vf/rows) ; `aid` reste toléré,\n"
        "  // un module historique l'utilise. Ne pas confondre avec `match`, qui n'a que `aid`.\n"
        "  if (ex.type === 'imgmatch') ex.rows.forEach(r => ZONES[r.id] = "
        "{cv:(r.ok!==undefined?r.ok:r.aid), zcat:'id', exo:ex.id});",
        'bonne réponse des imgmatch')
    # Le second argument de mkImgZone n'a jamais servi : la fonction ignore
    # `im` et relit l'image placée dans ALL_IMAGES. C'est lui qui a fait croire
    # que `aid` était la clé.
    html = upgrade(
        html,
        "        const z=mkImgZone(r.id, ex.images.find(im=>im.id===r.aid));",
        "        const z=mkImgZone(r.id);",
        'appel de mkImgZone')
    html = upgrade(
        html,
        "function mkImgZone(zid, im){",
        "function mkImgZone(zid){",
        'signature de mkImgZone')

    VF_W = ("      const _vfw=Math.max(72, Math.max.apply(null,"
            "ex.tiles.map(function(t){return t.length}))*8.5+28);\n"
            "      card.style.setProperty('--vfw', _vfw+'px');\n")
    if VF_W not in html:
        old_vf = "    if(ex.type==='vf'){\n"
        if html.count(old_vf) != 1:
            fatal('ancre du rendu vf introuvable ou ambiguë')
        html = html.replace(old_vf, old_vf + VF_W)
    return html


def greffer_jeu_de_role(html):
    """Le moteur de conversation vit dans module-logement. Il est identique
    d'un module à l'autre ; seul le scénario change, et il vit dans server.py.
    On le recopie plutôt que de le réécrire, pour que tout reste en phase."""
    if "// ── JEU DE RÔLE AVEC L'ASSISTANT" in html:
        return html                       # le gabarit l'a déjà
    log_html = LOG.read_text(encoding='utf-8')

    jr_css = slice_between(
        log_html, '/* ── Jeu de rôle du défi 1',
        '@media(max-width:640px){.jr-b{max-width:92%}}', 'CSS jeu de rôle')
    jr_js = slice_between(
        log_html, "// ── JEU DE RÔLE AVEC L'ASSISTANT",
        '// ── EXERCICES À ÉCRIRE', 'JS jeu de rôle')
    jr_js = jr_js[:jr_js.rfind('// ── EXERCICES À ÉCRIRE')].rstrip()

    jr_css = jr_css.replace('Jeu de rôle du défi 1', 'Jeu de rôle de « Je me lance »')
    # Le cas de départ, le scénario envoyé au serveur et la consigne de
    # correction deviennent des jetons : ils changent à chaque module.
    jr_js = jr_js.replace("const JR = {log:'A', role:'locataire',",
                          "const JR = {log:'%%JR_CAS%%', role:'%%JR_ROLE%%',")
    jr_js = jr_js.replace("logement:JR.log, role:JR.role",
                          "scenario:'%%JR_SCENARIO%%', cas:JR.log, role:JR.role")
    jr_js = jr_js.replace(
        'question:"L\'élève joue un rôle : il pose ou répond à des questions '
        'pour louer un logement, avec le pronom de reprise '
        '(Le chauffage est-il inclus ?)."',
        'question:"%%IA_JEU_DE_ROLE%%"')
    for repere in ['%%JR_CAS%%', '%%JR_ROLE%%', '%%JR_SCENARIO%%',
                   '%%IA_JEU_DE_ROLE%%']:
        if repere not in jr_js:
            fatal('adaptation du JS jeu de rôle incomplète : %s manquant' % repere)

    html = html.replace('/* Focus clavier visible partout (B.4) */',
                        jr_css + '\n\n/* Focus clavier visible partout (B.4) */')
    html = html.replace('// ── EXERCICES À ÉCRIRE',
                        jr_js + '\n\n// ── EXERCICES À ÉCRIRE', 1)
    return html


def refondre_production(html):
    """Les blocs de production orale et écrite : la consigne dépliée en cartes,
    le micro dans un panneau à trois étapes, le courriel en cadre de document.

    Cette refonte a déjà été perdue une fois (écrite à la main dans un HTML
    généré, effacée par la reconstruction suivante). Elle est donc ancrée ici,
    avec des repères qui arrêtent le build s'ils ne collent plus.
    """
    OLD_REC_CSS = (
        '.rec-zone{display:flex;flex-direction:column;align-items:center;gap:10px;margin:8px 0}\n'
        '#recBtn{width:78px;height:78px;border-radius:50%;border:none;background:#1D6B8F;'
        'color:#fff;font-size:30px;cursor:pointer;box-shadow:0 4px 16px rgba(15,118,110,.32)}\n'
        '#recBtn.recording{background:#E23D2E;animation:pulse 1.2s infinite}\n'
        '@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(226,61,46,.45)}'
        '70%{box-shadow:0 0 0 16px rgba(226,61,46,0)}100%{box-shadow:0 0 0 0 rgba(226,61,46,0)}}\n'
        '.rec-lbl{font-size:13px;font-weight:800;color:#4A6F68}\n'
    )
    html = upgrade(html, OLD_REC_CSS, lire('production.css'), 'CSS du bloc micro')

    # Le bouton devient un disque qui se change en carré : plus d'émoji dans
    # le texte du bouton, et un aria-label qui suit l'état.
    REC_PATCHES = [
        ("    document.getElementById('poPrev').classList.remove('hidden');\n  };",
         "    document.getElementById('poPrev').classList.remove('hidden');\n    recStep(2);\n  };"),
        ("  const btn=document.getElementById('recBtn'); btn.classList.add('recording'); "
         "btn.textContent='⏹';",
         "  const btn=document.getElementById('recBtn'); btn.classList.add('recording');\n"
         "  btn.setAttribute('aria-label',\"Arrêter l'enregistrement\");"),
        ("  const btn=document.getElementById('recBtn'); if(btn){ btn.classList.remove('recording'); "
         "btn.textContent='🎤'; }",
         "  const btn=document.getElementById('recBtn'); if(btn){ btn.classList.remove('recording'); "
         "btn.setAttribute('aria-label',\"Démarrer l'enregistrement\"); }"),
        ("function resetRec(){\n",
         "function recStep(n){\n"
         "  for(let i=1;i<=3;i++){ const s=document.getElementById('recStep'+i); "
         "if(s) s.classList.toggle('on', i===n); }\n"
         "}\n"
         "function peCount(){\n"
         "  const el=document.getElementById('peText'), lbl=document.getElementById('peCountLbl');\n"
         "  if(!el||!lbl) return;\n"
         "  const mn=el.dataset.min||'5', mx=el.dataset.max||'8';\n"
         "  const n=(el.value.match(/[.!?…]+(\\s|$)/g)||[]).length;\n"
         "  lbl.textContent = n+(n>1?' phrases':' phrase')+' sur '+mn+' à '+mx;\n"
         "}\n"
         "function resetRec(){\n  recStep(1);\n"),
        ("    document.getElementById('poSend').style.display='flex';",
         "    document.getElementById('poSend').style.display='flex'; recStep(3);"),
        ("btn.textContent='📨 Envoyer à mon enseignant'; return; }",
         "btn.textContent='Envoyer à mon enseignant'; return; }"),
        ("btn.textContent='📨 Envoyer à mon enseignant'; }",
         "btn.textContent='Envoyer à mon enseignant'; }"),
    ]
    for old, new in REC_PATCHES:
        html = upgrade(html, old, new, "moteur d'enregistrement (%r)" % old[:60])
    return html


def refondre_vocabulaire(html):
    """Le gabarit n'a qu'un exercice de vocabulaire — association mot/définition,
    toute la liste d'un coup. On le remplace par le bloc complet : six mots à la
    fois, rappel actif, mot/image, et la traduction en langue maternelle masquée
    par défaut. Le bloc ne lit que FC_CARDS : il vaut pour tout module."""
    if 'function vocabBuild()' in html:
        return html                       # déjà greffé

    html = remplacer_entre(html,
                           '// ── Association mot ↔ définition par CLIC',
                           'function toggleScript(btn, secId){',
                           lire('vocab.js'), 'moteur du vocabulaire')
    html = remplacer_entre(html,
                           'function toggleVocabExo(force){',
                           '// ── LOGIQUE DE PLACEMENT',
                           '', 'ancien toggleVocabExo')
    html = html.replace('/* Focus clavier visible partout (B.4) */',
                        lire('vocab.css') + '\n\n/* Focus clavier visible partout (B.4) */', 1)

    OLD_MOUNT = "  if(document.getElementById('vocab-words')) renderVocabPairs();"
    if html.count(OLD_MOUNT) != 1:
        fatal('ancre de montage du vocabulaire introuvable ou ambiguë')
    html = html.replace(OLD_MOUNT, "  if(document.getElementById('vocab-words')) vocabBuild();")

    OLD_PIED = ('      h+=\'<button class="btn btn-ghost" type="button" style="margin-top:14px" '
                'onclick="toggleVocabExo(false)">Fermer</button>\';')
    NEW_PIED = ('      h+=\'<div class="vc-actions" style="margin-top:14px">\';\n'
                '      h+=\'<button class="btn btn-pri" type="button" id="vocab-suite" '
                'onclick="vocabAutreGroupe()">Un autre groupe de mots</button>\';\n'
                '      h+=\'<button class="btn btn-ghost" type="button" '
                'onclick="toggleVocabExo(false)">Fermer</button>\';\n'
                '      h+=\'</div>\';')
    if html.count(OLD_PIED) != 1:
        fatal("pied de l'exercice de vocabulaire introuvable ou ambigu")
    html = html.replace(OLD_PIED, NEW_PIED)

    for repere in ['function vocabBuild()', 'function vocRappelRender()',
                   'function vocImageRender()', 'function toggleVocabExo(force)']:
        if html.count(repere) != 1:
            fatal('%s : absent ou en double après la greffe du vocabulaire' % repere)
    return html


# ══════════════════════════════════════════════════════════════════════
#  2. Percer les jetons : contenu, puis identité
# ══════════════════════════════════════════════════════════════════════

# ── Le type d'exercice `texte` ────────────────────────────────────────────
# Les six types du moteur — match, imgmatch, vf, write, blanks, rows —
# travaillent tous la **phrase isolée**. Or trois des quatre intentions de
# compréhension écrite du niveau 6 portent sur un **texte** : comprendre un
# article, comprendre un fait divers, lire le courrier des lecteurs. Idem aux
# niveaux 7 et 8. Jusqu'ici, le seul moyen de mettre un texte devant l'élève
# était de le loger dans le bandeau noir d'un `vf` — un détournement qui se lit
# bien mais qui interdit trois choses : faire cliquer l'élève DANS le texte,
# lui faire retrouver un référent en le surlignant, et garder le texte sous les
# yeux à côté des questions plutôt qu'au-dessus.
#
# Le pilote du niveau 6 (activité 99) a buté sur les trois et a écrit que
# c'était « le seul ajout au moteur qui vaudrait son coût ». Il sert aux
# vingt-quatre modules qui restent.
#
# La forme, dans exos.js :
#
#     {sec:'d1', id:'t1art', type:'texte', num:'Exercice 2',
#      tit:"Ce que dit l'article", color:'#3F6C51',
#      sub:"Cliquez dans le texte le mot qui répond à chaque question.",
#      paras:[
#        "La garantie légale protège l'acheteur [[ap|même après la fin de la "
#        "garantie du marchand]].",
#        "[[nb|Nadège]] a écrit une mise en demeure.",
#      ],
#      rows:[
#        {id:'q1', q:"Qui a écrit la lettre ?", ok:'nb'},
#        {id:'q2', q:"Qu'est-ce qui protège l'acheteur ?", ok:'ap'},
#      ]}
#
# `[[identifiant|le passage cliquable]]` marque un segment. L'élève choisit une
# question, puis clique le passage : le lien se voit des deux côtés. Bouton
# « Corriger » comme le vf, même barème, même aide après erreurs.
def ajouter_type_texte(html):
    """Greffe le style, l'état, le rendu et la correction du type `texte`."""
    if "ex.type==='texte'" in html:
        return html                                    # le gabarit l'a déjà

    # 1. Le style. Deux colonnes quand l'écran le permet — le texte reste sous
    #    les yeux pendant qu'on répond, ce qui est tout l'intérêt — et une
    #    seule colonne en dessous de 900 px, le texte d'abord.
    css = """
/* ── Exercice « texte » : un texte suivi et ses questions ─────────────── */
.tx-grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);
  gap:18px;align-items:start}
@media(max-width:900px){.tx-grid{grid-template-columns:1fr}}
.tx-texte{background:var(--surface-50,#F7F8FA);border:1px solid var(--line-200,#E4E8ED);
  border-radius:var(--radius-ctrl,10px);padding:16px 18px;line-height:1.75;
  font-size:var(--fs-body,17px);position:sticky;top:12px}
@media(max-width:900px){.tx-texte{position:static}}
.tx-texte p{margin:0 0 12px}
.tx-texte p:last-child{margin-bottom:0}
.tx-seg{cursor:pointer;border-radius:5px;padding:1px 3px;
  box-shadow:inset 0 -2px 0 var(--line-300,#D8DEE6);transition:background .12s}
.tx-seg:hover{background:var(--surface-100,#EEF1F5)}
.tx-seg.is-armed{background:var(--sec-color,#3F6C51);color:#fff;
  box-shadow:none}
.tx-seg.is-taken{background:var(--surface-200,#E4E8ED);box-shadow:none}
.tx-seg.ok{background:#DFF3E4;box-shadow:inset 0 -2px 0 #2F8F4E}
.tx-seg.no{background:#FBE3E3;box-shadow:inset 0 -2px 0 #C0392B}
.tx-q{border:1px solid var(--line-200,#E4E8ED);border-radius:var(--radius-ctrl,10px);
  padding:12px 14px;margin-bottom:10px;cursor:pointer;background:#fff}
.tx-q:hover{border-color:var(--line-300,#D8DEE6)}
.tx-q.is-active{border-color:var(--sec-color,#3F6C51);
  box-shadow:0 0 0 2px color-mix(in srgb,var(--sec-color,#3F6C51) 18%, transparent)}
.tx-q.ok{border-color:#2F8F4E;background:#F4FBF6}
.tx-q.no{border-color:#C0392B;background:#FDF5F5}
.tx-q-txt{font-size:var(--fs-body,17px);line-height:1.5}
.tx-q-rep{margin-top:8px;font-size:var(--fs-label,13px);font-weight:var(--fw-bold,700);
  letter-spacing:var(--ls-label,.04em);text-transform:uppercase;
  color:var(--text-600,#5A6472)}
.tx-q-rep.vide{font-weight:var(--fw-regular,400);text-transform:none;letter-spacing:0;
  font-style:italic}
"""
    i = html.find('.hdr-eye{')
    if i < 0:
        fatal('type texte : point d’insertion du style introuvable')
    fin = html.find('}', i) + 1
    html = html[:fin] + css + html[fin:]

    # 2. Les zones. Une question est une zone comme une autre : elle compte
    #    dans le total du module et dans l'étoile.
    ancre = "  if (ex.type === 'write')  ex.items.forEach((it,i) =>"
    zones = ("  if (ex.type === 'texte')  ex.rows.forEach(r => "
             "ZONES[r.id] = {cv:r.ok, zcat:'id', exo:ex.id});\n")
    html = html.replace(ancre, zones + ancre, 1)

    # 3. L'interaction et la correction, à côté de celles du vf, dont elles
    #    reprennent exactement le comportement : on répond, on corrige quand on
    #    veut, et l'aide se déclenche sur le nombre d'erreurs restantes.
    js = r"""
// ── Exercice « texte » : cliquer dans le texte ────────────────────────
// L'élève arme une question, puis clique le passage qui y répond. Les deux
// gestes sont réversibles : recliquer un passage déjà pris le libère, et
// changer de question n'efface rien. C'est ce qui permet de revenir sur une
// réponse sans tout reprendre, comme dans le vrai-faux.
function txArm(exId, qid){
  S.txQ[exId] = (S.txQ[exId] === qid) ? null : qid;
  render();
}
function txPick(exId, segId){
  const ex = EXOS.find(e => e.id === exId);
  if (!ex) return;
  const qid = S.txQ[exId];
  // Un passage déjà attribué se libère d'un clic, même sans question armée :
  // sinon un élève qui se trompe de segment doit deviner quoi faire.
  const dejaA = Object.keys(S.txSel).find(k => S.txSel[k] === segId
                  && ex.rows.some(r => r.id === k));
  if (dejaA && (!qid || dejaA === qid)) {
    delete S.txSel[dejaA]; delete S.fb[dejaA]; render(); return;
  }
  if (!qid) return;
  if (dejaA) delete S.txSel[dejaA];
  S.txSel[qid] = segId;
  delete S.fb[qid];
  S.txQ[exId] = null;
  render();
}
function txCheckAll(exId){
  const ex = EXOS.find(e => e.id === exId);
  if (!ex) return;
  let repondu = 0, justes = 0;
  ex.rows.forEach(r => {
    const seg = S.txSel[r.id];
    if (!seg) return;
    repondu++;
    const ok = seg === r.ok;
    if (ok) justes++;
    S.fb[r.id] = ok ? 'ok' : 'no';
    S.pl[r.id] = {iid:r.id, lbl:seg, cat:'id'};
    trackPlacement(r.id, ok);
  });
  if (repondu >= ex.rows.length) evaluerAide(exId, repondu - justes);
  const sum = document.getElementById('txsum-'+exId);
  if (sum) {
    if (repondu < ex.rows.length) {
      sum.className = 'vf-summary warn';
      sum.textContent = 'Réponds à toutes les questions avant de corriger ('
        + repondu + ' sur ' + ex.rows.length + ').';
    } else {
      sum.className = 'vf-summary ' + (justes === ex.rows.length ? 'ok' : 'warn');
      sum.textContent = justes + ' bonne(s) réponse(s) sur ' + ex.rows.length + '.';
    }
  }
  render();
}
// Le texte, segments compris. On échappe le texte AVANT de poser les balises :
// un article de journal contient des guillemets et des apostrophes, et un
// module qui les rendrait bruts casserait son propre script.
function txHtml(ex){
  const pris = {};
  ex.rows.forEach(r => { if (S.txSel[r.id]) pris[S.txSel[r.id]] = r.id; });
  return (ex.paras || []).map(p => {
    let out = '', reste = p, m;
    const re = /\[\[([A-Za-z0-9_-]+)\|([\s\S]*?)\]\]/;
    while ((m = re.exec(reste))) {
      out += esc(reste.slice(0, m.index));
      const id = m[1], mots = m[2];
      const qid = pris[id];
      let cls = 'tx-seg';
      if (qid) cls += (S.fb[qid] === 'ok') ? ' ok' : (S.fb[qid] === 'no') ? ' no' : ' is-taken';
      out += '<span class="' + cls + '" role="button" tabindex="0"'
           + ' onclick="txPick(\'' + ex.id + '\',\'' + id + '\')"'
           + ' onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();'
           + 'txPick(\'' + ex.id + '\',\'' + id + '\')}">' + esc(mots) + '</span>';
      reste = reste.slice(m.index + m[0].length);
    }
    return '<p>' + out + esc(reste) + '</p>';
  }).join('');
}
function txMotDuSegment(ex, segId){
  for (const p of (ex.paras || [])) {
    const m = new RegExp('\\[\\[' + segId + '\\|([\\s\\S]*?)\\]\\]').exec(p);
    if (m) return m[1];
  }
  return segId;
}
"""
    html = html.replace('function vfSelect(zid, lbl) {', js.strip() + '\nfunction vfSelect(zid, lbl) {', 1)

    # 4. L'état : la question armée et les réponses, par exercice.
    html = html.replace("vocabPick:null, vocabPairs:{}, vocabOrder:null}",
                        "vocabPick:null, vocabPairs:{}, vocabOrder:null, "
                        "txQ:{}, txSel:{}}", 1)

    # 5. Le rendu de la carte, juste avant celui du vrai-faux.
    carte = r"""    // ── Exercice « texte » : un texte suivi, ses questions à côté ──
    if(ex.type==='texte'){
      h+='<div class="c-hdr">'+exoNumBadge(ex.num)+'<span class="tag">'+esc(ex.num)+'</span><span class="exo-score" id="score-'+ex.id+'" aria-live="polite">0 / '+ex.rows.length+' répondu</span><span class="ctit">'+esc(ex.tit)+'</span><span class="csub">'+esc(ex.sub||'Choisissez une question, puis cliquez dans le texte le passage qui y répond.')+'</span></div>';
      h+='<div class="tx-grid"><div class="tx-texte" id="txt-'+ex.id+'"></div>';
      h+='<div id="txq-'+ex.id+'"></div></div>';
      h+='<div style="margin-top:14px;display:flex;align-items:center;gap:12px;flex-wrap:wrap">';
      h+='<button class="btn btn-pri" type="button" onclick="txCheckAll(\''+ex.id+'\')">✓ Corriger</button>';
      h+='<div class="vf-summary" id="txsum-'+ex.id+'" aria-live="polite"></div>';
      h+='</div>';
      card.innerHTML=h; host.appendChild(card); return;
    }
"""
    ancre_vf = "    // ── Exercice Vrai/Faux (ou 2 catégories) — colonnes + bouton Corriger ──"
    html = html.replace(ancre_vf, carte + ancre_vf, 1)

    # 6. Le montage à chaque rendu, dans la boucle de `render()`. Le texte et
    #    les questions se redessinent ensemble : un segment pris doit se voir
    #    du côté du texte comme du côté de la question, sinon l'élève ne sait
    #    plus ce qu'il a répondu.
    montage = r"""    const txT=document.getElementById('txt-'+ex.id);
    if(txT && ex.type==='texte'){
      txT.innerHTML = txHtml(ex);
      const arm = S.txQ[ex.id];
      const qh = document.getElementById('txq-'+ex.id);
      if(qh){
        qh.innerHTML = ex.rows.map(function(r){
          const seg = S.txSel[r.id];
          const fb = S.fb[r.id];
          let cls = 'tx-q' + (arm===r.id ? ' is-active' : '')
                  + (fb==='ok' ? ' ok' : fb==='no' ? ' no' : '');
          const rep = seg
            ? '<div class="tx-q-rep">« ' + esc(txMotDuSegment(ex, seg)) + ' »</div>'
            : '<div class="tx-q-rep vide">Cliquez ici, puis dans le texte.</div>';
          return '<div class="' + cls + '" role="button" tabindex="0"'
               + ' onclick="txArm(\'' + ex.id + '\',\'' + r.id + '\')"'
               + ' onkeydown="if(event.key===\'Enter\'||event.key===\' \'){event.preventDefault();'
               + 'txArm(\'' + ex.id + '\',\'' + r.id + '\')}">'
               + '<div class="tx-q-txt">' + esc(r.q) + '</div>' + rep + '</div>';
        }).join('');
      }
      const sc=document.getElementById('score-'+ex.id);
      if(sc){
        const n=ex.rows.filter(function(r){return S.txSel[r.id]}).length;
        sc.textContent = n + ' / ' + ex.rows.length + ' répondu';
      }
      return;
    }
"""
    ancre_m = "    const mount=document.getElementById('mount-'+ex.id);\n    if(!mount) return;"
    if ancre_m not in html:
        fatal('type texte : point de montage introuvable dans render()')
    html = html.replace(ancre_m, montage + ancre_m, 1)
    return html


def styler_repere(html):
    """La règle CSS du repère « Module 12 · Niveau 3 ».

    Elle se pose juste après `.hdr-eye`, dont elle hérite la ligne de base.
    Trois partis pris :

    · **Elle ne crie pas.** Le repère est un renseignement de service, pas le
      titre : il passe en graisse normale, sans majuscules forcées, et prend
      la couleur de texte discrète du système. Le titre garde son accent de
      niveau à lui seul.
    · **Un filet vertical plutôt qu'un point médian.** `.hdr-eye` est déjà un
      flex avec un `gap` : une bordure gauche sépare sans ajouter de caractère
      à ce que lit un lecteur d'écran.
    · **Elle disparaît sous 480 px.** Sur un téléphone tenu à la verticale, la
      place va au titre du module ; le numéro reste dans le `<title>` de
      l'onglet et dans le pied de page.
    """
    if '.hdr-ref{' in html:
        return html
    ancre = '.hdr-eye{'
    i = html.find(ancre)
    if i < 0:
        fatal('règle .hdr-eye introuvable : le repère n’aurait pas de style')
    fin = html.find('}', i) + 1
    regle = ("\n.hdr-ref{padding-left:8px;border-left:1px solid "
             "var(--line-300,#D8DEE6);font-weight:var(--fw-regular,400);"
             "text-transform:none;letter-spacing:0;color:var(--text-600,#5A6472);"
             "white-space:nowrap}"
             "\n@media(max-width:480px){.hdr-ref{display:none}}")
    return html[:fin] + regle + html[fin:]


def percer_contenu(html):
    """Les six régions de contenu et le bloc des sections personnalisées."""
    for const, fin, jeton in [
            ('DIALOGUES',       '};', '%%DIALOGUES%%'),
            ('SECTIONS',        '];', '%%SECTIONS%%'),
            ('FC_CARDS',        '];', '%%FC_CARDS%%'),
            ('EXOS',            '];', '%%EXOS%%'),
            ('CARRIER_PHRASES', '};', '%%CARRIER_PHRASES%%'),
            ('PLUS',            '};', '%%PLUS%%')]:
        html = region_jeton(html, const, fin, jeton)

    # Sections personnalisées : oral, jeu de rôle, écrit, bilan.
    a = html.find('  // JE ME LANCE')
    b = html.find('function rate(i,btn)')
    if a < 0 or b < 0:
        fatal('bloc injectCustom introuvable')
    return html[:a] + '%%CUSTOM%%\n' + html[b:]


RE_EYE = re.compile(r'<div class="hdr-eye">.*?</div>', re.S)
RE_ACCENT = re.compile(r'--hdr-accent:#[0-9A-Fa-f]{6}; --hdr-accent-soft:#[0-9A-Fa-f]{6};')


def percer_identite(html):
    """Tout ce qui nomme, colore ou adresse le module de la consultation."""
    remplacements = [
        ('<title>Consulter au bon endroit — Module Niveau 4</title>',
         '<title>%%TITRE%% — %%REPERE%%</title>'),
        # Le titre du module, puis son repère : « Module 12 · Niveau 3 ».
        # L'élève arrive ici par un signet ou par l'adresse qu'un voisin lui a
        # passée ; rien à l'écran ne lui disait lequel des cinquante-huit il
        # ouvrait. Le repère est un `<span>` séparé plutôt qu'un bout du même
        # texte, pour que le titre reste lisible seul par un lecteur d'écran
        # et que le repère puisse passer à la ligne sur un téléphone.
        #
        # Cherché par sa FORME, et pour une raison qui s'est vérifiée le jour
        # même : module-consultation est à la fois un module en ligne et la
        # source du gabarit. La greffe qui a posé le repère dans les
        # cinquante-huit modules l'a donc posé dans la source aussi, et le
        # gabarit, qui attendait le `<div>` nu, a cessé de se construire.
        (RE_EYE,
         '<div class="hdr-eye">%%TITRE%%'
         '<span class="hdr-ref">%%REPERE%%</span></div>'),
        ("const MODULE_SLUG = 'module-consultation';",
         "const MODULE_SLUG = '%%SLUG%%';"),
        ('/assets/interactive/module-consultation/',
         '/assets/interactive/%%SLUG%%/'),
        # Les deux couleurs d'en-tête sont cherchées par leur FORME, pas par
        # leur valeur. La consultation est passée du bleu à l'ambre du niveau
        # 4 le jour où la couleur a été rattachée au niveau, et le gabarit,
        # qui attendait encore `#1D6B8F`, a cessé de se construire — sans que
        # personne s'en aperçoive, puisqu'on ne le régénère qu'en le
        # modifiant. Une constante recopiée dans deux fichiers finit toujours
        # par diverger ; un motif, non.
        (RE_ACCENT,
         '--hdr-accent:%%ACCENT%%; --hdr-accent-soft:%%ACCENT_DOUX%%;'),
        ("fd.append('theme','Santé'); fd.append('taskId','module-consultation-po');",
         "fd.append('theme','%%THEME%%'); fd.append('taskId','%%SLUG%%-po');"),
        ('question:"L\'élève décrit oralement une douleur ou un problème de santé '
         'à un professionnel, en précisant depuis quand et à quel endroit."',
         'question:"%%IA_ORAL%%"'),
        # Pas de jeton pour la consigne de la production ÉCRITE : elle ne vit
        # pas dans le gabarit. C'est `build/greffe_depot_ecrit.py` qui la pose,
        # en la lisant du module. L'ancien script de module-probleme croyait la
        # remplacer ici — la chaîne cherchée n'existait pas et le `replace`
        # était silencieusement sans effet.
        # L'en-tête de commentaire du script portait encore le titre et le
        # découpage d'avant la réécriture de la consultation — invisible pour
        # l'élève, mais recopié tel quel dans chaque module engendré.
        ('//  LA VISITE CHEZ LE MÉDECIN — Module interactif Niveau 4 (FLS)\n'
         '//  Sections : Je découvre · Chez le médecin · La langue · Je parle ·\n'
         "//             J'écris · Je m'évalue — suivi LMS intégré",
         '//  %%TITRE_MAJ%% — Module interactif Niveau %%NIVEAU%% (FLS)\n'
         '//  Sections : Je découvre · Défi 1 · … · Je me lance ·\n'
         '//             Je retiens des mots — suivi LMS intégré'),
        ('🎉 Bravo, tu as terminé le module « Consulter au bon endroit » !',
         '%%BRAVO%%'),
        ("Tu peux revenir sur n\\'importe quel onglet pour pratiquer encore.",
         '%%RELANCE%%'),
    ]
    for old, new in remplacements:
        if hasattr(old, 'sub'):
            html, n = old.subn(new.replace('\\', '\\\\'), html)
            if not n:
                fatal('identité : motif introuvable — %s' % old.pattern)
            continue
        if old not in html:
            fatal('identité : repère introuvable — %r' % old[:70])
        html = html.replace(old, new)
    return html


def corriger_envoi_oral(html):
    """L'envoi de l'oral annonçait toujours la tâche de la consultation.

    `fd.append('taskLabel', 'Production orale — décrire une douleur')` était
    écrit en dur dans le module d'origine : tout module bâti sur le gabarit
    déposait ses enregistrements sous le libellé d'un autre, et l'enseignante
    lisait « décrire une douleur » sur une production de magasinage. Le dépôt
    de l'écrit, lui, lit le titre et la consigne dans le DOM (`libelle()` /
    `consigne()` de `greffe_depot_ecrit`) — l'oral fait maintenant pareil, avec
    ses propres fonctions, celles de la greffe vivant dans une fermeture.
    """
    OLD = ("  fd.append('taskLabel','Production orale — décrire une douleur'); "
           "fd.append('question','Décrire une douleur à un professionnel de la santé');")
    NEW = "  fd.append('taskLabel', poLibelle()); fd.append('question', poConsigne());"
    html = upgrade(html, OLD, NEW, "libellé de l'envoi oral")

    OLD_FN = "async function poSend(){"
    NEW_FN = (
        "function poCarte(){ const t=document.getElementById('poText');"
        " return t?t.closest('.card'):null; }\n"
        "function poLibelle(){ const c=poCarte(), h=c&&c.querySelector('.prod-tit');\n"
        "  return h?h.textContent.trim():'Production orale'; }\n"
        "function poConsigne(){ const c=poCarte(), p=c&&c.querySelector('.prod-lead');\n"
        "  return p?p.textContent.trim():''; }\n"
        "async function poSend(){")
    html = upgrade(html, OLD_FN, NEW_FN, "fonctions de libellé de l'oral")
    return html


def images_en_paysage(html):
    """Les images d'exercice passent du carré au 3:2.

    La zone de glisser-déposer mesure 223 x 132 px, soit un rapport de 1,7 :
    une image carrée y est recadrée par `object-fit:cover` et perd le haut et
    le bas. Les images se génèrent désormais en 3:2 (voir le journal
    `docs/chantier-tous-niveaux.md`), et les trois cadres qui les reçoivent
    prennent le même rapport — sans quoi on ne ferait que déplacer le
    recadrage vers la banque.

    Les images déjà produites, elles, sont carrées : dans un cadre paysage,
    `object-fit:cover` leur couperait le tiers du haut et du bas. Les trois
    cadres passent donc à `contain`, qui montre l'image entière et laisse au
    besoin une bande de fond sur les côtés. Aucune régression sur les dix-huit
    modules existants, et les images 3:2 des modules neufs rempliront le cadre
    exactement.
    """
    PATCHES = [
        # La vignette qu'on prend dans la banque.
        (".imgtile{width:100px;height:100px;border-radius:10px;",
         ".imgtile{width:150px;aspect-ratio:3/2;border-radius:10px;"),
        # La zone où on la dépose : elle annonce la forme attendue.
        (".imgzone{width:100%;min-height:110px;border-radius:10px;",
         ".imgzone{width:100%;aspect-ratio:3/2;border-radius:10px;"),
        # « Le mot et son image », dans le banc de vocabulaire.
        ("  aspect-ratio:1/1;object-fit:cover;border-radius:var(--r-md);",
         "  aspect-ratio:3/2;object-fit:contain;border-radius:var(--r-md);"),
        # Montrer l'image entière plutôt que de la recadrer : les images déjà
        # produites sont carrées, les neuves seront en 3:2.
        (".imgtile img{width:100%;height:100%;object-fit:cover;display:block;",
         ".imgtile img{width:100%;height:100%;object-fit:contain;display:block;"),
        (".imgzone img{width:100%;height:100%;object-fit:cover;display:block;",
         ".imgzone img{width:100%;height:100%;object-fit:contain;display:block;"),
    ]
    for old, new in PATCHES:
        html = upgrade(html, old, new, "cadre d'image (%r)" % old[:28])
    return html


# ── Confinement de la reconnaissance vocale ───────────────────────────────
# Les repères sont ceux du gabarit ASSEMBLÉ (jeu de rôle greffé, production
# refondue) : l'étape tourne en dernier dans main().

HELPER_RECO = """// ── RECONNAISSANCE VOCALE : GARDE-FOU « SUR L'APPAREIL » ──────────────
// webkitSpeechRecognition n'est PAS un moteur local : Chrome expédie l'audio
// capté à ses serveurs, Safari aux siens. Pour une classe de francisation cela
// veut dire la voix d'élèves nouvellement arrivés qui sort du Québec à chaque
// exercice oral — sans passer par notre serveur ni par nos clés, donc sans
// qu'aucun choix d'hébergeur n'y change quoi que ce soit.
//
// La Web Speech API sait maintenant travailler hors ligne : available() dit si
// le paquet de langue est présent, install() le télécharge, et processLocally
// interdit tout envoi réseau. TOUT passe par reconnaissanceLocale() — aucun
// « new SpeechRecognition() » ne doit reparaître ailleurs dans ce fichier.
//
// Strict = pas de reconnaissance locale possible ⇒ pas de reconnaissance du
// tout. Un centre qui préfère le service au confinement peut le lever, et la
// voix repart alors chez l'éditeur du navigateur, en connaissance de cause.
//
// La décision vient du SERVEUR, pas du build : la greffe « sans IA » pose
// window.RECO_STRICTE au chargement, d'après le centre de l'élève. Tant que
// la réponse n'est pas là — et si elle n'arrive jamais — on reste strict.
// C'est le contraire du choix fait pour les routes d'IA, qui ne se replient
// pas sur une panne de réseau : celles-là sont gardées côté serveur de toute
// façon, alors que ce flux-ci ne le traverse pas. Un silence ne doit pas
// ouvrir le micro.
if (window.RECO_STRICTE === undefined) window.RECO_STRICTE = true;
const RECO_LANGS = ['fr-CA'];
const RECO_SRC = () => window.SpeechRecognition || window.webkitSpeechRecognition;
// Le paquet de langue ne se télécharge qu'une fois par appareil, mais il pèse
// lourd : on ne relance pas l'installation à chaque touche de micro.
let _recoInstall = false;

// quality : 'command' pour un mot répété, 'dictation' pour une production
// suivie. Le moteur local ne charge pas le même modèle selon le cas.
async function recoEtat(quality){
  const SRC = RECO_SRC();
  if(!SRC) return 'sans-api';
  // Navigateur d'avant l'API sur appareil : available() n'existe pas, donc
  // rien ne garantit que l'audio reste ici. En mode strict, on renonce.
  if(typeof SRC.available !== 'function') return window.RECO_STRICTE ? 'sans-local' : 'distant';
  let dispo;
  try{ dispo = await SRC.available({langs:RECO_LANGS, quality, processLocally:true}); }
  catch(e){ return window.RECO_STRICTE ? 'sans-local' : 'distant'; }
  if(dispo === 'available') return 'local';
  if(dispo === 'downloadable' || dispo === 'downloading'){
    if(!_recoInstall){
      _recoInstall = true;
      Promise.resolve(SRC.install({langs:RECO_LANGS, processLocally:true}))
        .catch(()=>{}).then(()=>{ _recoInstall = false; });
    }
    return 'telechargement';
  }
  return window.RECO_STRICTE ? 'sans-local' : 'distant';
}

// Rend {rec, etat}. rec vaut null dès que l'exercice ne peut pas écouter.
async function reconnaissanceLocale(quality){
  const etat = await recoEtat(quality);
  if(etat !== 'local' && etat !== 'distant') return {rec:null, etat};
  const rec = new (RECO_SRC())();
  rec.lang = RECO_LANGS[0]; rec.maxAlternatives = 1;
  // processLocally n'est lu qu'au start() : le poser après ne servirait à rien.
  if(etat === 'local'){ try{ rec.processLocally = true; }catch(e){} }
  return {rec, etat};
}

// Un seul texte par état, pour que les trois exercices disent la même chose.
function recoMessage(etat){
  if(etat === 'sans-api')       return "Ce navigateur ne fait pas la reconnaissance vocale. Essaie avec Chrome, Edge ou Safari.";
  if(etat === 'telechargement') return "Préparation de la reconnaissance vocale sur cet appareil — réessaie dans un moment.";
  if(etat === 'sans-local')     return "La reconnaissance vocale hors ligne n'est pas disponible sur cet appareil.";
  return "";
}

"""

OLD_PRON = """function pronCheck(btn, expected){
  const SRC = window.SpeechRecognition || window.webkitSpeechRecognition;
  let fb = btn.nextElementSibling && btn.nextElementSibling.classList.contains('pron-fb') ? btn.nextElementSibling : null;
  if(!fb){ fb=document.createElement('span'); fb.className='pron-fb'; fb.setAttribute('aria-live','polite'); btn.insertAdjacentElement('afterend', fb); }
  if(!SRC){ fb.className='pron-fb warn'; fb.textContent='Reconnaissance vocale non supportée (utilise Chrome).'; return; }
  const old = btn.innerHTML;
  btn.classList.remove('fb-ok','fb-no');
  btn.disabled=true; btn.innerHTML=ICON_MIC+' …';
  fb.className='pron-fb'; fb.textContent='Écoute en cours…';
  const reset=()=>{ btn.disabled=false; btn.innerHTML=old; };
  const target = normPron(expected);
  let done=false, lastInterim='';
  const rec = new SRC();
  // interimResults:true — les mots très courts ("tôt", "mer"...) sont parfois
  // coupés par la détection de silence avant qu'un résultat final n'arrive ;
  // on garde le dernier résultat provisoire comme filet de secours.
  rec.lang='fr-CA'; rec.interimResults=true; rec.maxAlternatives=1;
"""

NEW_PRON = """async function pronCheck(btn, expected){
  let fb = btn.nextElementSibling && btn.nextElementSibling.classList.contains('pron-fb') ? btn.nextElementSibling : null;
  if(!fb){ fb=document.createElement('span'); fb.className='pron-fb'; fb.setAttribute('aria-live','polite'); btn.insertAdjacentElement('afterend', fb); }
  const old = btn.innerHTML;
  btn.classList.remove('fb-ok','fb-no');
  btn.disabled=true; btn.innerHTML=ICON_MIC+' …';
  const reset=()=>{ btn.disabled=false; btn.innerHTML=old; };
  // Un mot répété : le modèle 'command' suffit, et il se télécharge plus vite.
  fb.className='pron-fb'; fb.textContent='Préparation…';
  const {rec, etat} = await reconnaissanceLocale('command');
  if(!rec){ reset(); fb.className='pron-fb warn'; fb.textContent=recoMessage(etat); return; }
  fb.className='pron-fb'; fb.textContent='Écoute en cours…';
  const target = normPron(expected);
  let done=false, lastInterim='';
  // interimResults:true — les mots très courts ("tôt", "mer"...) sont parfois
  // coupés par la détection de silence avant qu'un résultat final n'arrive ;
  // on garde le dernier résultat provisoire comme filet de secours.
  rec.interimResults=true;
"""

OLD_ORAL = """  mediaRecorder.start();
  if(SR){
    recognition=new SR(); recognition.lang='fr-CA'; recognition.continuous=true; recognition.interimResults=false;
    let tr='';
    recognition.onresult=e=>{ for(let i=e.resultIndex;i<e.results.length;i++){ if(e.results[i].isFinal)tr+=e.results[i][0].transcript+' '; } const b=document.getElementById('poText'); if(b)b.value=tr.trim(); };
    try{ recognition.start(); }catch(e){}
  }
  isRec=true;"""

NEW_ORAL = """  // Préparé AVANT mediaRecorder.start() : lancer la reconnaissance après coup
  // lui ferait manquer les premiers mots de l'élève.
  const reco = await reconnaissanceLocale('dictation');
  if(!reco.rec){
    showErr('poErr', recoMessage(reco.etat)+" L'enregistrement fonctionne quand même : écris ton texte à la main.");
  }
  mediaRecorder.start();
  if(reco.rec){
    recognition=reco.rec; recognition.continuous=true; recognition.interimResults=false;
    let tr='';
    recognition.onresult=e=>{ for(let i=e.resultIndex;i<e.results.length;i++){ if(e.results[i].isFinal)tr+=e.results[i][0].transcript+' '; } const b=document.getElementById('poText'); if(b)b.value=tr.trim(); };
    try{ recognition.start(); }catch(e){}
  }
  isRec=true;"""

OLD_MODE = """function jrModeVoix(on){
  if(on && !jrSRC()){
    showErr('jrErr',"Ce navigateur ne fait pas la reconnaissance vocale. Essaie avec Chrome, Edge ou Safari.");
    return;
  }"""

NEW_MODE = """async function jrModeVoix(on){
  // Le refus se dit ici, au moment où l'élève choisit le mode — pas plus tard,
  // micro en main, quand il a déjà commencé à parler.
  if(on){
    const etat = await recoEtat('dictation');
    if(etat !== 'local' && etat !== 'distant'){ showErr('jrErr', recoMessage(etat)); return; }
  }"""

OLD_PARLER = """function jrParler(){
  const SRC=jrSRC();
  if(!SRC){ showErr('jrErr',"Ce navigateur ne fait pas la reconnaissance vocale."); return; }
  if(JR.rec){ try{ JR.rec.stop(); }catch(e){} return; }   // deuxième touche = arrêter
  jrTaire();                    // sinon le micro réentend la voix de l'assistant
  hideErr('jrErr');
  const inp=document.getElementById('jrInput');
  const btn=document.getElementById('jrMic');
  const lbl=document.getElementById('jrMicLbl');
  inp.value='';
  const rec=new SRC(); JR.rec=rec;
  rec.lang='fr-CA'; rec.interimResults=true; rec.continuous=true; rec.maxAlternatives=1;"""

NEW_PARLER = """async function jrParler(){
  if(JR.rec){ try{ JR.rec.stop(); }catch(e){} return; }   // deuxième touche = arrêter
  jrTaire();                    // sinon le micro réentend la voix de l'assistant
  hideErr('jrErr');
  const inp=document.getElementById('jrInput');
  const btn=document.getElementById('jrMic');
  const lbl=document.getElementById('jrMicLbl');
  inp.value='';
  lbl.textContent='Préparation…';
  const {rec, etat} = await reconnaissanceLocale('dictation');
  if(!rec){ lbl.textContent='Touche pour parler'; showErr('jrErr', recoMessage(etat)); return; }
  // Deux touches rapides pendant la préparation : la première a déjà gagné.
  if(JR.rec){ return; }
  JR.rec=rec;
  rec.interimResults=true; rec.continuous=true;"""


def confiner_reconnaissance(html):
    """Oblige la reconnaissance vocale à rester sur l'appareil de l'élève.

    Trois exercices ouvrent le micro — vérification de prononciation,
    production orale, jeu de rôle en mode voix — et chacun construisait son
    propre SpeechRecognition. Ils passent maintenant tous par un portail
    unique, reconnaissanceLocale(), qui exige processLocally avant d'écouter.
    Les deux constantes qui donnaient un accès direct au constructeur
    disparaissent : sinon un module futur reprendrait l'ancien geste sans que
    personne le voie.

    Posée en DERNIER dans main() : ses repères sont ceux du gabarit assemblé.
    """
    html = upgrade(html, OLD_PRON, HELPER_RECO + NEW_PRON,
                   'confinement : pronCheck')
    html = upgrade(html, OLD_ORAL, NEW_ORAL,
                   'confinement : production orale')
    # PAS `upgrade()` ici : sa première ligne est `if new in text: return text`,
    # et la chaîne vide est contenue dans n'importe quel texte. Les deux appels
    # rendaient donc le HTML inchangé, en silence, et les déclarations
    # restaient en code mort — exactement le geste qu'on prétendait fermer.
    html = retirer(html,
                   'const SR = window.SpeechRecognition || window.webkitSpeechRecognition;\n',
                   'confinement : constante SR devenue inutile')
    html = retirer(html,
                   'const jrSRC = () => window.SpeechRecognition || window.webkitSpeechRecognition;\n',
                   'confinement : constante jrSRC devenue inutile')
    html = upgrade(html, OLD_MODE, NEW_MODE, 'confinement : jrModeVoix')
    html = upgrade(html, OLD_PARLER, NEW_PARLER, 'confinement : jrParler')

    # Filet : plus aucun constructeur direct ne doit subsister.
    reste = html.count('new SRC()') + html.count('new SR()')
    if reste:
        fatal('confinement : %d constructeur(s) de reconnaissance hors du '
              'portail reconnaissanceLocale()' % reste)
    return html


def main():
    html = SRC.read_text(encoding='utf-8')
    src_len = len(html)
    if '%%' in html:
        fatal('le module source contient déjà « %% » : changer la syntaxe des jetons')

    html = ameliorer(html)
    html = greffer_jeu_de_role(html)
    html = refondre_production(html)
    html = refondre_vocabulaire(html)
    html = corriger_envoi_oral(html)
    html = images_en_paysage(html)
    html = ajouter_type_texte(html)
    html = styler_repere(html)
    html = percer_contenu(html)
    html = percer_identite(html)
    html = confiner_reconnaissance(html)

    # Filet : plus rien de la consultation ne doit rester en dehors des
    # greffes (barre d'outils, dépôt, verrou), qui portent son slug et que
    # `build/module.py` dégreffe avant de poser celles du module.
    residus = []
    for mot in ['Yannick', 'Rosalie', 'Beaulieu', 'tendinite',
                'Consulter au bon endroit', 'physiothérapie']:
        n = html.count(mot)
        if n:
            residus.append('%s (%d)' % (mot, n))
    if residus:
        fatal('résidus de contenu de la consultation dans le gabarit : '
              + ', '.join(residus))

    jetons = sorted(set(__import__('re').findall(r'%%[A-Z_]+%%', html)))
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_text(html, encoding='utf-8')
    print('OK  %s' % DST)
    print('    module-consultation %d octets → gabarit %d octets' % (src_len, len(html)))
    print('    %d jetons : %s' % (len(jetons), ' '.join(jetons)))


if __name__ == '__main__':
    main()
