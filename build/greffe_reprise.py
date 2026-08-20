#!/usr/bin/env python3
"""Greffe la reprise de séance dans les modules interactifs.

L'élève ouvrait un module, s'arrêtait, retournait à sa fiche, revenait — et
repartait de la première section avec tout effacé. Rien n'était gardé : l'état
vit dans des variables JavaScript (S, TR, curSec) et le serveur ne reçoit que
des compteurs (zonesDone, firstTry…), jamais les réponses elles-mêmes. Cette
greffe pose une mémoire locale, une clé par élève et par module, plus la
bannière « Tu reprends où tu étais » et son bouton pour tout recommencer.

Comme greffe_outils.py, elle est idempotente : elle retire une greffe existante
avant de la reposer.

    python3 build/greffe_reprise.py            # tous les modules
    python3 build/greffe_reprise.py travail    # un ou plusieurs modules
    python3 build/greffe_reprise.py --retirer  # dégreffe tout

module-probleme est **généré** par build/module.py module-probleme : le greffer
ici serait écrasé à la reconstruction suivante. Le script le saute quand on ne
le nomme pas explicitement.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

# Cinq régions marquées : le style, l'appel dans render(), le moteur, puis les
# deux points d'accroche du démarrage. Chaque paire se retire d'un bloc, ce qui
# rend la greffe réversible sans toucher au module d'origine.
MARQUES = [
    ('/* REPRISE-CSS:début — greffé par build/greffe_reprise.py */',
     '/* REPRISE-CSS:fin */'),
    ('/* REPRISE-APPEL:début — greffé par build/greffe_reprise.py */',
     '/* REPRISE-APPEL:fin */'),
    ('// ── REPRISE:début — greffé par build/greffe_reprise.py ──',
     '// ── REPRISE:fin ──'),
    ('/* REPRISE-GO:début — greffé par build/greffe_reprise.py */',
     '/* REPRISE-GO:fin */'),
    ('/* REPRISE-MARQUES:début — greffé par build/greffe_reprise.py */',
     '/* REPRISE-MARQUES:fin */'),
]

# ── 1. Le style de la bannière ────────────────────────────────────────
# Posé juste après le bouton « Réinitialiser », dans le même bloc <style>.
ANCRE_CSS = '#btn-reset:hover{background:rgba(255,255,255,.28)}\n'

CSS = MARQUES[0][0] + """
#re-banniere{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin:14px auto 0;max-width:1180px;padding:12px 18px;background:var(--surface-card,#fff);border:2px solid var(--border,#D9DCE0);border-left:6px solid var(--hdr-accent,var(--accent-ink,#0A8F5B));border-radius:14px;font-family:'Nunito',sans-serif;font-size:15px;font-weight:800;color:var(--text-strong,#17181A)}
#re-banniere .re-txt{flex:1;min-width:200px}
#re-banniere .re-quand{display:block;font-weight:700;font-size:13px;color:var(--text-soft,#6E7175)}
#re-banniere button{font-family:'Nunito',sans-serif;font-size:14px;font-weight:800;border-radius:999px;cursor:pointer;padding:9px 16px;background:var(--surface-card,#fff);color:var(--text-strong,#17181A);border:1px solid var(--border,#D9DCE0)}
#re-banniere button:hover{background:var(--paper-100,#F2F4F5)}
#re-banniere #re-fermer{padding:9px 13px}
""" + MARQUES[0][1] + '\n'

# ── 2. L'appel de sauvegarde ──────────────────────────────────────────
# Tout ce qui change l'état du module finit par render() : un seul point
# d'accroche suffit pour les placements, les vrai/faux et la section courante.
ANCRE_APPEL = """  updateChip();
}
function updateChip(){"""

APPEL = """  updateChip();
  """ + MARQUES[1][0] + """
  reSauver();   // toute modification de l'état passe par render()
  """ + MARQUES[1][1] + """
}
function updateChip(){"""

# ── 3. Le moteur, juste avant le démarrage ────────────────────────────
ANCRE_GO = '// ── GO ────────────────────────────────────────────────────────────────\nbuildStatic();\nrender();\n'

MOTEUR = MARQUES[2][0] + """
// L'élève ouvre le module, s'arrête, retourne à sa fiche, puis revient ici.
// Sans mémoire locale il repartait de la première section avec tout effacé :
// l'état vit dans des variables JavaScript, et le serveur ne garde que des
// compteurs (zonesDone, firstTry…), jamais les réponses elles-mêmes. On garde
// donc l'avancement dans le navigateur, une clé par élève et par module.
const RE_CLE = MODULE_SLUG + ':' + (studentCode || 'anonyme') + ':etat';
const RE_VERSION = 1;
let reMinuteur = null;
let reGel = false;   // vrai pendant la restauration : on n'écrase pas la sauvegarde

// Les réponses écrites vivent dans le DOM, pas dans S : on les relève à part.
function reChamps(){
  const out = {};
  document.querySelectorAll('.winput, textarea').forEach((el, i) => {
    if (el.value) out[el.id || ('champ' + i)] = el.value;
  });
  return out;
}

function reEtat(){
  return {
    v: RE_VERSION, quand: Date.now(), curSec: curSec,
    pl: S.pl, vfSel: S.vfSel, fb: S.fb,
    vocabPairs: S.vocabPairs, vocabOrder: S.vocabOrder,
    attempts: TR.attempts, correct: TR.correct,
    champs: reChamps(),
  };
}

function reEcrire(){
  try { localStorage.setItem(RE_CLE, JSON.stringify(reEtat())); } catch(e) {}
}

// render() est appelé à chaque clic : on regroupe les écritures.
function reSauver(){
  if (reGel) return;
  clearTimeout(reMinuteur);
  reMinuteur = setTimeout(reEcrire, 300);
}

function reEffacer(){
  clearTimeout(reMinuteur);
  try { localStorage.removeItem(RE_CLE); } catch(e) {}
}

function reLire(){
  try {
    const d = JSON.parse(localStorage.getItem(RE_CLE) || 'null');
    return (d && d.v === RE_VERSION) ? d : null;
  } catch(e) { return null; }
}

function reprendre(){
  const d = reLire();
  if (!d) return null;
  reGel = true;
  S.pl = d.pl || {};
  S.vfSel = d.vfSel || {};
  S.fb = d.fb || {};
  if (d.vocabPairs) S.vocabPairs = d.vocabPairs;
  if (d.vocabOrder) S.vocabOrder = d.vocabOrder;
  TR.attempts = d.attempts || {};
  TR.correct = d.correct || {};
  // Une section disparue depuis la dernière visite ne doit pas bloquer
  // l'ouverture ; la greffe des sections peut encore déplacer l'élève si
  // celle-ci a été refermée par l'enseignant.
  if (d.curSec && SECTIONS.some(s => s.id === d.curSec)) curSec = d.curSec;
  const champs = d.champs || {};
  document.querySelectorAll('.winput, textarea').forEach((el, i) => {
    const val = champs[el.id || ('champ' + i)];
    if (val != null) el.value = val;
  });
  if (typeof peCount === 'function') peCount();
  reGel = false;
  return d;
}

// Une réponse écrite déjà validée reste verte — et verrouillée quand la bonne
// réponse était connue d'avance, comme au moment de la validation.
function reMarquerEcrits(){
  EXOS.filter(e => e.type === 'write').forEach(ex => {
    ex.items.forEach((it, i) => {
      if (!TR.correct['w_' + ex.id + '_' + i]) return;
      const inp = document.getElementById('wi_' + ex.id + '_' + i);
      if (!inp) return;
      inp.classList.add('good');
      if (it.accept) inp.disabled = true;
    });
  });
}

// Le pointage des vrai/faux est recalculé : on ne réaffiche le total qu'aux
// exercices que l'élève avait réellement corrigés (S.fb rempli partout).
function reMarquerVf(){
  EXOS.filter(e => e.type === 'vf').forEach(ex => {
    const repondu = ex.rows.filter(r => S.vfSel[r.id]).length;
    if (!repondu) return;
    const corrige = ex.rows.every(r => S.fb[r.id]);
    updateVfScore(ex, corrige);
    if (!corrige) return;
    const bons = ex.rows.filter(r => S.vfSel[r.id] === r.ok).length;
    const sum = document.getElementById('vfsum-' + ex.id);
    if (sum) {
      sum.className = 'vf-summary ok';
      sum.textContent = bons + ' / ' + ex.rows.length + ' bonnes réponses';
    }
  });
}

function reQuand(ms){
  if (Date.now() - ms < 3600e3) return 'il y a moins d’une heure';
  const j = new Date(ms);
  const h = String(j.getHours()).padStart(2, '0') + ' h ' + String(j.getMinutes()).padStart(2, '0');
  if (j.toDateString() === new Date().toDateString()) return 'plus tôt aujourd’hui, à ' + h;
  const mois = ['janvier','février','mars','avril','mai','juin','juillet',
                'août','septembre','octobre','novembre','décembre'];
  return 'le ' + j.getDate() + ' ' + mois[j.getMonth()] + ', à ' + h;
}

// La reprise ne doit jamais être une prison : le bouton remet tout à zéro.
function reBanniere(d){
  const chrome = document.getElementById('chrome');
  if (!chrome || !chrome.parentNode) return;
  const el = document.createElement('div');
  el.id = 're-banniere';
  el.setAttribute('role', 'status');
  const n = Object.keys(TR.correct).length;
  el.innerHTML = '<span class="re-txt">↩︎ Tu reprends où tu étais : '
    + (n ? n + ' réponse' + (n > 1 ? 's' : '') + ' déjà juste' + (n > 1 ? 's' : '')
         : 'ton travail est retrouvé')
    + '.<span class="re-quand">Dernier passage ' + reQuand(d.quand) + '.</span></span>'
    + '<button type="button" id="re-recommencer">↺ Recommencer le module</button>'
    + '<button type="button" id="re-fermer" aria-label="Masquer ce message">✕</button>';
  chrome.parentNode.insertBefore(el, chrome.nextSibling);
  document.getElementById('re-recommencer').addEventListener('click', () => {
    if (!confirm('Recommencer le module depuis le début ? Tes réponses seront effacées.')) return;
    reGel = true;   // le rechargement ne doit pas réécrire ce qu'on vient d'effacer
    reEffacer();
    location.reload();
  });
  document.getElementById('re-fermer').addEventListener('click', () => el.remove());
}

// Les champs de texte ne passent pas par render() : ils se sauvent seuls.
document.addEventListener('input', e => {
  const t = e.target;
  if (t && (t.tagName === 'TEXTAREA' || t.classList.contains('winput'))) reSauver();
});
// Onglet fermé : on écrit tout de suite au lieu d'attendre la temporisation.
addEventListener('pagehide', () => { if (!reGel) reEcrire(); });

""" + MARQUES[2][1] + """
// ── GO ────────────────────────────────────────────────────────────────
buildStatic();
""" + MARQUES[3][0] + """
const reReprise = reprendre();
""" + MARQUES[3][1] + """
render();
""" + MARQUES[4][0] + """
if (reReprise) { reMarquerEcrits(); reMarquerVf(); reBanniere(reReprise); }
""" + MARQUES[4][1] + '\n'


def degreffe(html):
    # Chaque région occupe des lignes entières : on retire depuis son marqueur
    # d'ouverture jusqu'à la fin de la ligne du marqueur de fermeture. Manger
    # en plus le saut de ligne qui la précède laisserait une ligne vide de trop
    # à chaque passage, et la greffe cesserait d'être réversible à l'octet près.
    for debut, fin in MARQUES:
        html = re.sub(r'[ \t]*' + re.escape(debut) + r'.*?' + re.escape(fin) + r'[ \t]*\n',
                      '', html, flags=re.S)
    return html


def greffe(html, slug):
    """Renvoie le HTML greffé, ou lève ValueError si un ancrage manque : mieux
    vaut un échec bruyant qu'un module qui ne garde rien."""
    html = degreffe(html)
    for ancre, quoi in ((ANCRE_CSS, 'le bouton « Réinitialiser » du <style>'),
                        (ANCRE_APPEL, 'la fin de render() avant updateChip()'),
                        (ANCRE_GO, 'le bloc de démarrage « ── GO ── »')):
        if html.count(ancre) != 1:
            raise ValueError('ancrage introuvable ou en double : ' + quoi)
    for nom in ('const MODULE_SLUG', 'const studentCode', 'const S = {pl:',
                'const TR = {attempts:', 'function updateVfScore('):
        if nom not in html:
            raise ValueError('%s introuvable — le moteur s’appuie dessus' % nom)

    html = html.replace(ANCRE_CSS, ANCRE_CSS + CSS, 1)
    html = html.replace(ANCRE_APPEL, APPEL, 1)
    html = html.replace(ANCRE_GO, MOTEUR, 1)
    return html


def fichier_du_module(dossier):
    fichiers = list(dossier.glob('*-activite-interactive.html'))
    return fichiers[0] if fichiers else None


def main(argv):
    retirer = '--retirer' in argv
    noms = [a for a in argv if not a.startswith('--')]

    dossiers = sorted(d for d in INTERACTIF.glob('module-*') if d.is_dir())
    if noms:
        voulus = {n if n.startswith('module-') else 'module-' + n for n in noms}
        dossiers = [d for d in dossiers if d.name in voulus]
        introuvables = voulus - {d.name for d in dossiers}
        if introuvables:
            sys.exit('!! module(s) introuvable(s) : ' + ', '.join(sorted(introuvables)))

    faits, sautes = 0, []
    for dossier in dossiers:
        if dossier.name == 'module-probleme' and not noms:
            sautes.append('module-probleme (généré — voir son build.py)')
            continue
        f = fichier_du_module(dossier)
        if f is None:
            sautes.append(dossier.name + ' (aucun fichier interactif)')
            continue
        html = f.read_text(encoding='utf-8')
        try:
            neuf = degreffe(html) if retirer else greffe(html, dossier.name)
        except ValueError as e:
            sautes.append('%s (%s)' % (dossier.name, e))
            continue
        if neuf != html:
            f.write_text(neuf, encoding='utf-8')
            faits += 1
            print('%-24s %s' % (dossier.name, 'dégreffé' if retirer else 'greffé'))
        else:
            print('%-24s inchangé' % dossier.name)

    print('\n%d module(s) modifié(s)' % faits)
    for s in sautes:
        print('  sauté : ' + s)


if __name__ == '__main__':
    main(sys.argv[1:])
