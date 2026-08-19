#!/usr/bin/env python3
# Génère module-probleme à partir du gabarit module-consultation.
# Les régions de contenu sont lues depuis les fichiers .js de ce dossier.
import re, sys, pathlib

BUILD = pathlib.Path(__file__).parent
ROOT  = pathlib.Path('/Users/danieltousignant/Claude/bibliotheque-francisation')
SRC   = ROOT / 'assets/interactive/module-consultation/module-consultation-activite-interactive.html'
DST   = ROOT / 'assets/interactive/module-probleme/module-probleme-activite-interactive.html'

html = SRC.read_text(encoding='utf-8')
orig_len = len(html)

def region(html, const_name, new_text, end_marker):
    """Remplace `const X = ...` jusqu'au marqueur de fin le plus proche.
    Marqueur SANS \n (piège documenté dans le skill : un marqueur avec saut de
    ligne saute silencieusement jusqu'au bloc suivant)."""
    start = html.find('const %s = ' % const_name)
    if start < 0:
        sys.exit('!! const %s introuvable' % const_name)
    end = html.find(end_marker, start)
    if end < 0:
        sys.exit('!! marqueur de fin %r introuvable pour %s' % (end_marker, const_name))
    end += len(end_marker)
    return html[:start] + new_text.strip() + html[end:]

def read(name):
    return (BUILD / name).read_text(encoding='utf-8')

# ── 1. Régions de contenu ────────────────────────────────────────────
html = region(html, 'DIALOGUES',        read('dialogues.js'), '};')
html = region(html, 'SECTIONS',         read('sections.js'),  '];')
html = region(html, 'FC_CARDS',         read('fccards.js'),   '];')
html = region(html, 'EXOS',             read('exos.js'),      '];')
html = region(html, 'CARRIER_PHRASES',  read('carrier.js'),   '};')
html = region(html, 'PLUS',             read('plus.js'),      '};')

# Canari du piège de découpe : PLUS doit toujours exister après coup.
assert 'const PLUS = {' in html, '!! PLUS avalé par une découpe — marqueur de fin fautif'

# ── 2. Identité du module ────────────────────────────────────────────
html = html.replace(
    '<title>Consulter au bon endroit — Module Niveau 4</title>',
    '<title>Pouvez-vous régler le problème ? — Module Niveau 4</title>')
html = html.replace(
    '<div class="hdr-eye">Consulter au bon endroit</div>',
    '<div class="hdr-eye">Pouvez-vous régler le problème ?</div>')
html = html.replace("const MODULE_SLUG = 'module-consultation';",
                    "const MODULE_SLUG = 'module-probleme';")
html = html.replace('/assets/interactive/module-consultation/',
                    '/assets/interactive/module-probleme/')

# Couleur d'en-tête : violet graphie-phonie, distincte de module-logement
# (acier) qui est son voisin immédiat, et du gabarit consultation (acier).
html = html.replace('--hdr-accent:#1D6B8F; --hdr-accent-soft:#E7F0F6;',
                    '--hdr-accent:#6B4FBB; --hdr-accent-soft:#EFEAFA;')

# ── 3. Suivi LMS ─────────────────────────────────────────────────────
html = html.replace("fd.append('theme','Santé'); fd.append('taskId','module-consultation-po');",
                    "fd.append('theme','Logement'); fd.append('taskId','module-probleme-po');")

# ── 4. Consignes envoyées à l'IA de correction ───────────────────────
html = html.replace(
    'question:"L\'élève décrit oralement une douleur ou un problème de santé à un professionnel, en précisant depuis quand et à quel endroit."',
    'question:"L\'élève explique oralement un problème dans son logement à sa propriétaire ou à son concierge : il nomme le problème, dit depuis quand il dure (depuis, depuis que, ça fait... que), en explique la conséquence, puis formule une demande."')
html = html.replace(
    'question:"L\'élève écrit un courriel à une clinique pour demander un rendez-vous, en décrivant son problème de santé et ses disponibilités."',
    'question:"L\'élève écrit un courriel à sa propriétaire pour signaler un problème dans son logement : il décrit le fait, précise depuis quand (depuis, ça fait... que), explique la conséquence et formule une demande claire. On attend un ton poli et ferme, et au moins une construction faire + infinitif."')

# ── 5. Zones de réponse : grille deux colonnes pour les réponses courtes ──
# Une réponse d'un ou deux mots occupait toute la largeur de l'écran. La
# grille auto-fit garde une seule colonne sous 300 px (mobile) et passe à
# deux dès qu'il y a la place — sans toucher aux jetons du design system.
html = html.replace(
    '.wlist{display:flex;flex-direction:column;gap:14px}',
    '.wlist{display:grid;grid-template-columns:1fr;gap:14px}\n'
    '.wlist.wcols2{grid-template-columns:repeat(2,minmax(0,1fr))}\n'
    '.wlist.wcols2 .winput{min-width:0}\n'
    '.wlist.wcols2 .wq{font-size:14.5px}\n'
    '@media(max-width:700px){.wlist.wcols2{grid-template-columns:1fr}}')
html = html.replace(
    "h+=aiBadge+'<div class=\"wlist\">';",
    "h+=aiBadge+'<div class=\"wlist'+(ex.cols===2?' wcols2':'')+'\">';")

# ── 5c. Tuiles Vrai/Faux : largeur adaptée à l'étiquette ─────────────
# Le gabarit fige les tuiles à 72 px : parfait pour VRAI/FAUX, mais
# « LOCATAIRE / PROPRIÉTAIRE » (Je me lance, exercice 1) débordait
# de la carte et l'en-tête se lisait « LOCATAIREPROPRIÉTAIRE ». On passe la
# largeur en variable CSS, calculée une fois par exercice d'après l'étiquette
# la plus longue ; l'en-tête et les boutons restent alignés puisqu'ils lisent
# la même variable.
html = html.replace(
    '.vf-head-opt{width:72px;flex:0 0 72px;',
    '.vf-head-opt{width:var(--vfw,72px);flex:0 0 var(--vfw,72px);')
html = html.replace(
    ".vf-opt{width:72px;flex:0 0 72px;",
    ".vf-opt{width:var(--vfw,72px);flex:0 0 var(--vfw,72px);padding:0 6px;")
# Sous 620 px, les tuiles passent sous l'énoncé plutôt que de le comprimer.
html = html.replace(
    '.vf-summary{font-size:13px;font-weight:800}',
    '@media(max-width:620px){\n'
    '  .vf-head{display:none}\n'
    '  .vf-opts{margin-left:0;width:100%}\n'
    '  .vf-opt{flex:1 1 0;width:auto}\n'
    '}\n'
    '.vf-summary{font-size:13px;font-weight:800}')
VF_W = ("      const _vfw=Math.max(72, Math.max.apply(null,"
        "ex.tiles.map(function(t){return t.length}))*8.5+28);\n"
        "      card.style.setProperty('--vfw', _vfw+'px');\n")
old_vf = "    if(ex.type==='vf'){\n"
if html.count(old_vf) != 1:
    sys.exit('!! ancre du rendu vf introuvable ou ambiguë')
html = html.replace(old_vf, old_vf + VF_W)

# ── 5b. Greffe du jeu de rôle depuis module-logement ─────────────────
# Le moteur de conversation (CSS + JS) est identique d'un module à l'autre ;
# seul le scénario change, et il vit dans server.py. On le recopie plutôt que
# de le réécrire, pour que les deux modules restent en phase.
LOG = ROOT / 'assets/interactive/module-logement/module-logement-activite-interactive.html'
log_html = LOG.read_text(encoding='utf-8')

def slice_between(text, start_marker, end_marker, label):
    a = text.find(start_marker)
    if a < 0:
        sys.exit('!! %s : début introuvable' % label)
    b = text.find(end_marker, a)
    if b < 0:
        sys.exit('!! %s : fin introuvable' % label)
    return text[a:b + len(end_marker)]

jr_css = slice_between(log_html,
    '/* ── Jeu de rôle du défi 1',
    '@media(max-width:640px){.jr-b{max-width:92%}}', 'CSS jeu de rôle')
jr_js = slice_between(log_html,
    "// ── JEU DE RÔLE AVEC L'ASSISTANT",
    '// ── EXERCICES À ÉCRIRE', 'JS jeu de rôle')
jr_js = jr_js[:jr_js.rfind('// ── EXERCICES À ÉCRIRE')].rstrip()

jr_css = jr_css.replace('Jeu de rôle du défi 1',
                        'Jeu de rôle de « Je me lance »')
# Le cas de départ et le scénario envoyé au serveur.
jr_js = jr_js.replace("const JR = {log:'A',", "const JR = {log:'chauffage',")
jr_js = jr_js.replace("logement:JR.log, role:JR.role",
                      "scenario:'probleme', cas:JR.log, role:JR.role")
jr_js = jr_js.replace(
    'question:"L\'élève joue un rôle : il pose ou répond à des questions pour louer un logement, avec le pronom de reprise (Le chauffage est-il inclus ?)."',
    'question:"L\'élève joue un rôle au téléphone : il explique un problème dans son logement à sa propriétaire, dit depuis quand il dure (depuis, depuis que, ça fait... que), en donne la conséquence et demande une réparation (faire + infinitif)."')
if 'scenario:' not in jr_js or "log:'chauffage'" not in jr_js:
    sys.exit('!! adaptation du JS jeu de rôle incomplète')

html = html.replace('/* Focus clavier visible partout (B.4) */',
                    jr_css + '\n\n/* Focus clavier visible partout (B.4) */')
html = html.replace('// ── EXERCICES À ÉCRIRE',
                    jr_js + '\n\n// ── EXERCICES À ÉCRIRE', 1)

# ── 5c. Refonte des deux blocs de production (Claude Design) ─────────
# Le gabarit de consultation présente le micro en gros bouton à émoji et la
# consigne en un seul paragraphe. Module 9 déplie la consigne en cartes, met
# le micro dans un panneau à trois étapes et donne au courriel la forme d'un
# courriel. Le balisage vit dans custom.js ; le CSS et les retouches du
# moteur d'enregistrement vivent ici, parce qu'ils viennent du gabarit.
#
# Cette refonte a déjà été perdue une fois (commit 4b64a3b, écrite à la main
# dans le HTML généré, effacée par la reconstruction suivante). Elle est donc
# ancrée ici, avec des repères qui arrêtent le build s'ils ne collent plus.
#
# Depuis que le gabarit lui-même a reçu la refonte, ces substitutions n'ont
# plus rien à faire — d'où `upgrade`, qui accepte les deux états du gabarit et
# ne s'arrête que si l'on ne reconnaît ni l'ancien ni le nouveau.
# On teste la forme NEUVE en premier : plusieurs substitutions ajoutent du
# texte autour du repère, si bien que l'ancienne forme reste un fragment de la
# nouvelle. Dans l'autre ordre, le build appliquerait une deuxième fois une
# retouche déjà faite et dupliquerait des définitions de fonctions.
def upgrade(text, old, new, label):
    if new in text:
        return text                      # le gabarit est déjà à jour
    if text.count(old) == 1:
        return text.replace(old, new, 1)
    sys.exit('!! %s : ni l\'ancienne ni la nouvelle forme dans le gabarit' % label)

OLD_REC_CSS = (
    '.rec-zone{display:flex;flex-direction:column;align-items:center;gap:10px;margin:8px 0}\n'
    '#recBtn{width:78px;height:78px;border-radius:50%;border:none;background:#1D6B8F;'
    'color:#fff;font-size:30px;cursor:pointer;box-shadow:0 4px 16px rgba(15,118,110,.32)}\n'
    '#recBtn.recording{background:#E23D2E;animation:pulse 1.2s infinite}\n'
    '@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(226,61,46,.45)}'
    '70%{box-shadow:0 0 0 16px rgba(226,61,46,0)}100%{box-shadow:0 0 0 0 rgba(226,61,46,0)}}\n'
    '.rec-lbl{font-size:13px;font-weight:800;color:#4A6F68}\n'
)
html = upgrade(html, OLD_REC_CSS, read('production.css'), 'CSS du bloc micro')

# Le bouton devient un disque qui se change en carré : plus d'émoji dans le
# texte du bouton, et un aria-label qui suit l'état.
REC_PATCHES = [
    # le fil des trois étapes suit l'avancement
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
    # les deux fonctions nouvelles s'installent devant resetRec
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
    html = upgrade(html, old, new, 'moteur d\'enregistrement (%r)' % old[:60])

# ── 5d. Section vocabulaire (trois exercices + traduction) ───────────
# Le gabarit n'a qu'un exercice de vocabulaire (association mot/définition,
# toute la liste d'un coup). On le remplace par le bloc complet : six mots à
# la fois, rappel actif, mot/image, et la traduction en langue maternelle
# masquée par défaut. Le bloc ne lit que FC_CARDS : il vaut pour tout module.
def remplacer_entre(text, debut, fin, nouveau, label):
    """Remplace la région [debut, fin) par `nouveau`. `fin` reste dans le
    texte : c'est le repère du bloc suivant, pas la fin de la région."""
    a = text.find(debut)
    if a < 0:
        sys.exit('!! %s : début introuvable (%r)' % (label, debut[:50]))
    b = text.find(fin, a)
    if b < 0:
        sys.exit('!! %s : fin introuvable (%r)' % (label, fin[:50]))
    return text[:a] + nouveau.strip() + '\n\n' + text[b:]

# Le moteur : renderVocabPairs et toggleVocabExo du gabarit sont remplacés
# par ceux de vocab.js, qui vivent dans la même région.
html = remplacer_entre(html,
    '// ── Association mot ↔ définition par CLIC',
    'function toggleScript(btn, secId){',
    read('vocab.js'), 'moteur du vocabulaire')
html = remplacer_entre(html,
    'function toggleVocabExo(force){',
    '// ── LOGIQUE DE PLACEMENT',
    '', 'ancien toggleVocabExo')

html = html.replace('/* Focus clavier visible partout (B.4) */',
                    read('vocab.css') + '\n\n/* Focus clavier visible partout (B.4) */', 1)

# Le montage des deux nouvelles cartes remplace l'appel direct au rendu.
OLD_MOUNT = "  if(document.getElementById('vocab-words')) renderVocabPairs();"
if html.count(OLD_MOUNT) != 1:
    sys.exit('!! ancre de montage du vocabulaire introuvable ou ambiguë')
html = html.replace(OLD_MOUNT, "  if(document.getElementById('vocab-words')) vocabBuild();")

# Le pied de l'exercice 1 gagne le bouton « Un autre groupe de mots ».
OLD_PIED = ('      h+=\'<button class="btn btn-ghost" type="button" style="margin-top:14px" '
            'onclick="toggleVocabExo(false)">Fermer</button>\';')
NEW_PIED = ('      h+=\'<div class="vc-actions" style="margin-top:14px">\';\n'
            '      h+=\'<button class="btn btn-pri" type="button" id="vocab-suite" '
            'onclick="vocabAutreGroupe()">Un autre groupe de mots</button>\';\n'
            '      h+=\'<button class="btn btn-ghost" type="button" '
            'onclick="toggleVocabExo(false)">Fermer</button>\';\n'
            '      h+=\'</div>\';')
if html.count(OLD_PIED) != 1:
    sys.exit('!! pied de l\'exercice de vocabulaire introuvable ou ambigu')
html = html.replace(OLD_PIED, NEW_PIED)

for repere in ['function vocabBuild()', 'function vocRappelRender()',
               'function vocImageRender()', 'function toggleVocabExo(force)']:
    if html.count(repere) != 1:
        sys.exit('!! %s : absent ou en double après la greffe du vocabulaire' % repere)

# ── 6. Sections personnalisées : oral, jeu de rôle IA, écrit, bilan ──
old_start = html.find("  // JE ME LANCE")
old_end   = html.find("function rate(i,btn)")
if old_start < 0 or old_end < 0:
    sys.exit('!! bloc injectCustom introuvable')
html = html[:old_start] + read('custom.js').strip() + '\n' + html[old_end:]

html = html.replace(
    "🎉 Bravo, tu as terminé le module « Consulter au bon endroit » !",
    "🎉 Bravo, vous avez terminé le module « Pouvez-vous régler le problème ? » !")
html = html.replace(
    "Tu peux revenir sur n\\'importe quel onglet pour pratiquer encore.",
    "Vous pouvez revenir sur n\\'importe quel onglet pour pratiquer encore.")

# ── 6 bis. Barre d'outils élève ──────────────────────────────────────
# Le rail « Mes outils » vient du système de design, pas du gabarit. La greffe
# est celle de build/greffe_outils.py, partagée par les onze modules : une
# seule source, sinon le module 9 dérive des dix autres.
#
# greffe() commence par retirer toute greffe existante : le gabarit
# module-consultation porte la sienne, avec SON slug. Sans ce nettoyage, le
# module 9 hériterait du carnet de la consultation.
sys.path.insert(0, str(BUILD.parent))
from greffe_outils import greffe as greffe_outils   # noqa: E402

try:
    html = greffe_outils(html, 'module-probleme')
except ValueError as e:
    sys.exit('!! greffe de la barre d\'outils impossible : %s' % e)

# ── 6 bis bis. Dépôt de la production écrite ─────────────────────────
# Même règle que la barre d'outils : la greffe est celle des dix autres
# modules, et son dégreffage préalable retire celle du gabarit — qui porte le
# slug de la consultation dans son taskId.
from greffe_depot_ecrit import greffe as greffe_depot_ecrit   # noqa: E402

try:
    html = greffe_depot_ecrit(html, 'module-probleme')
except ValueError as e:
    sys.exit('!! greffe du dépôt de l\'écrit impossible : %s' % e)

# ── 6 ter. Verrou des sections datées ────────────────────────────────
# Même raison : la greffe de build/greffe_sections.py est celle des dix autres
# modules, et elle commence elle aussi par retirer celle du gabarit — qui porte
# le numéro d'activité de la consultation, pas celui du module 9.
from greffe_sections import (greffe as greffe_sections,      # noqa: E402
                             activites_par_slug)

_ids = activites_par_slug()
if 'module-probleme' not in _ids:
    sys.exit('!! module-probleme est absent de data/activities.json : '
             'le verrou des sections ne saurait pas quoi demander au serveur')
try:
    html = greffe_sections(html, _ids['module-probleme'])
except ValueError as e:
    sys.exit('!! greffe du verrou des sections impossible : %s' % e)

# ── 6 quater. Reprise de la séance ───────────────────────────────────
# Même règle encore : la mémoire locale est celle de build/greffe_reprise.py.
# Sa clé se construit à partir de MODULE_SLUG, déjà remplacé plus haut — le
# module 9 garde donc son propre avancement, sans confusion avec le gabarit.
from greffe_reprise import greffe as greffe_reprise   # noqa: E402

try:
    html = greffe_reprise(html, 'module-probleme')
except ValueError as e:
    sys.exit('!! greffe de la reprise de séance impossible : %s' % e)

# ── 7. Filet de sécurité ─────────────────────────────────────────────
leftovers = []
for bad in ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu', 'tendinite',
            'Consulter au bon endroit', 'physiothérapie']:
    n = html.count(bad)
    if n:
        leftovers.append('%s (%d)' % (bad, n))
if leftovers:
    sys.exit('!! résidus du gabarit : ' + ', '.join(leftovers))

DST.parent.mkdir(parents=True, exist_ok=True)
DST.write_text(html, encoding='utf-8')
print('OK  %s' % DST)
print('    gabarit %d octets → module %d octets' % (orig_len, len(html)))
