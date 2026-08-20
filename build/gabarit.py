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


def percer_identite(html):
    """Tout ce qui nomme, colore ou adresse le module de la consultation."""
    remplacements = [
        ('<title>Consulter au bon endroit — Module Niveau 4</title>',
         '<title>%%TITRE%% — Module Niveau %%NIVEAU%%</title>'),
        ('<div class="hdr-eye">Consulter au bon endroit</div>',
         '<div class="hdr-eye">%%TITRE%%</div>'),
        ("const MODULE_SLUG = 'module-consultation';",
         "const MODULE_SLUG = '%%SLUG%%';"),
        ('/assets/interactive/module-consultation/',
         '/assets/interactive/%%SLUG%%/'),
        ('--hdr-accent:#1D6B8F; --hdr-accent-soft:#E7F0F6;',
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
        if old not in html:
            fatal('identité : repère introuvable — %r' % old[:70])
        html = html.replace(old, new)
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
    html = percer_contenu(html)
    html = percer_identite(html)

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
