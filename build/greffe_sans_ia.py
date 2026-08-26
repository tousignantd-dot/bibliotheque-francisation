#!/usr/bin/env python3
"""Le module se replie en version sans assistant quand le centre l'a décidé.

Une direction peut refuser que ses élèves parlent à une IA. Le refus se pose
sur l'arbre des organisations (reseau.html → « Régler l'IA »), il descend du
CSS vers ses centres, et le serveur ferme les sept routes concernées. Cette
greffe est le côté élève de la même décision : le module demande son état au
chargement et, s'il est « interdite », il se replie.

Ce qui change, et ce qui ne change pas :

  production orale   — plus de rétroaction automatique ; le bouton « Envoyer à
                       mon enseignant » apparaît dès qu'il y a un
                       enregistrement, et part sans commentaire ;
  production écrite  — plus de « Vérifier mon message » ; l'envoi est toujours
                       là, et l'enseignant reçoit le texte NON corrigé ;
  jeu de rôle        — la partie « entraîne-toi seul avec l'assistant »
                       disparaît ; les fiches à imprimer, à faire à deux en
                       classe, restent ;
  aide après erreurs — le bouton « Pourquoi je me trompe ? » disparaît ; la
                       mini-leçon « Revoir l'explication », qui n'est que du
                       texte écrit d'avance, reste ;
  exercices écrits   — les réponses à réponse connue se corrigent comme avant
                       (c'est de la comparaison de chaînes, pas de l'IA) ; les
                       réponses ouvertes donnent la réponse attendue après
                       deux essais, au lieu d'un commentaire ;
  vocabulaire        — plus de « Voir dans ma langue », donc plus de choix de
                       langue maternelle ;
  barre « Mes outils » — « Traduire », « Simplifier » et « Demander à
                       l'assistant » disparaissent ; « Lire », « Prononcer »,
                       « Mon carnet » et « Réviser » restent (la lecture
                       retombe sur la voix du navigateur) ;
  audio et images    — inchangés : ce sont des fichiers, produits une fois et
                       livrés avec le module.

Le repli est cosmétique ; la vraie décision est côté serveur. Une page se
modifie avec deux touches, et une direction qui a dit non a dit non.

    python3 build/greffe_sans_ia.py            # gabarit + les onze modules
    python3 build/greffe_sans_ia.py --tous     # gabarit + les 87 modules
    python3 build/greffe_sans_ia.py --un module-sante
    python3 build/greffe_sans_ia.py --retirer  # revient en arrière

La greffe est idempotente et se retire sans laisser de trace.
"""

import argparse
import glob
import io
import re
import sys

GABARIT = "build/gabarit/module.html"
TOUS = "assets/interactive/module-*/module-*-activite-interactive.html"

ONZE = [
    "module-consultation", "module-urgence", "module-sante", "module-travail",
    "module-procedure", "module-nouvelles", "module-meteo", "module-pub",
    "module-logement", "module-probleme", "module-relations",
]

DEBUT = "<!-- SANS-IA:début — greffé par build/greffe_sans_ia.py -->"
FIN = "<!-- SANS-IA:fin -->"

BLOC = DEBUT + """
<style>
/* Le repli ne s'applique qu'une fois la réponse du serveur arrivée : sans la
   classe sur <body>, la page reste exactement celle d'avant. */
body.sans-ia #voc-head { display: none; }
body.sans-ia .vc-actions:has(button[id^="voctr"]) { display: none; }
body.sans-ia .sans-ia-mot {
  margin-top: 12px; padding: 10px 14px; border-radius: 10px;
  background: #f1f3f6; border-left: 4px solid #9aa3af;
  font-size: 14px; line-height: 1.5; color: #35404f;
}
</style>
<script>
(function () {
  'use strict';

  /* ── Ce que le module devient sans assistant ─────────────────────────── */

  function note(texte) {
    var d = document.createElement('div');
    d.className = 'sans-ia-mot';
    d.textContent = texte;
    return d;
  }

  /* Production orale — l'envoi n'attend plus une rétroaction qui ne viendra
     pas. Dès qu'il y a un enregistrement, le bouton est là. */
  function replierOral() {
    var btn = document.getElementById('poFbBtn');
    if (btn) btn.style.display = 'none';
    var prev = document.getElementById('poPrev');
    if (prev && !prev.querySelector('.sans-ia-mot')) {
      prev.appendChild(note("Écoute-toi, corrige ta transcription si besoin, "
        + "puis envoie ton enregistrement à ton enseignant."));
    }
    if (typeof stopRec === 'function') {
      var orig = stopRec;
      stopRec = function () {
        var r = orig.apply(this, arguments);
        var zone = document.getElementById('poSend');
        if (zone) zone.style.display = 'flex';
        if (typeof recStep === 'function') recStep(3);
        return r;
      };
    }
  }

  /* Production écrite — le dépôt est ouvert tout de suite, et il part sans
     commentaire : `peSend` lit le champ, pas une correction. L'enseignant
     reçoit le texte tel que l'élève l'a écrit. */
  function replierEcrit() {
    var btn = document.getElementById('peBtn');
    if (btn) btn.style.display = 'none';
    var zone = document.getElementById('peSend');
    if (zone) zone.style.display = 'flex';
    var champ = document.getElementById('peText');
    var carte = champ && champ.closest('.card');
    if (carte && zone && !carte.querySelector('.sans-ia-mot')) {
      zone.parentNode.insertBefore(
        note("Relis ton message, puis envoie-le à ton enseignant. "
           + "C'est lui qui te le corrigera."), zone);
    }
  }

  /* Jeu de rôle — seule la moitié « avec l'assistant » tombe. Ce qui précède
     le séparateur est l'activité de classe : les situations, les sujets à
     couvrir, le rappel de grammaire, et parfois des fiches à découper. Les
     78 modules à jeu de rôle en ont tous, et ça ne doit rien à l'IA.

     Deux corrections indispensables une fois l'assistant parti. D'abord la
     phrase d'ouverture, qui le promet dans 77 modules sur 78 : la laisser,
     c'est annoncer à l'élève quelque chose qui n'arrivera pas. Ensuite le mot
     qui explique ce que devient l'exercice — et il ne peut pas parler de
     fiches à imprimer, puisqu'un seul module en a. */
  function replierJeuDeRole() {
    var depart = document.getElementById('jrStart');
    if (!depart) return;
    var carte = depart.closest('.card') || depart.parentElement;
    var sep = carte && carte.querySelector('.jr-sep');
    if (!sep) { carte.style.display = 'none'; return; }

    var fiches = null;
    for (var n = sep; n; ) {
      var suivant = n.nextElementSibling;
      n.style.display = 'none';
      n = suivant;
    }
    fiches = carte.querySelector('.jr-print');
    var aDesFiches = !!(fiches && fiches.style.display !== 'none');

    /* On ne réécrit aucune phrase : on retire celles qui ne sont plus vraies.
       Un « bloc de texte » est un élément dont les enfants sont tous en ligne
       (gras, italique, saut de ligne). Se limiter aux feuilles ne suffisait
       pas : la phrase d'ouverture porte presque toujours un <b>, et elle
       restait affichée dans les 77 modules qu'il fallait corriger. Un bloc
       qui contient d'autres blocs, lui, n'est jamais retiré — il emporterait
       les situations avec lui. */
    var mort = /assistant/i;
    var EN_LIGNE = /^(B|I|EM|STRONG|SPAN|BR|A|CODE|SMALL|U|SUP|SUB)$/;
    [].slice.call(carte.querySelectorAll('p, div, span, li')).forEach(function (e) {
      if (e.classList.contains('sans-ia-mot')) return;
      if (!mort.test(e.textContent || '')) return;
      for (var i = 0; i < e.children.length; i++)
        if (!EN_LIGNE.test(e.children[i].tagName)) return;
      e.style.display = 'none';
    });

    var tete = carte.querySelector('.c-hdr');
    var mot = note(aDesFiches
      ? "Cet entraînement se fait à deux, en classe, avec les fiches à imprimer."
      : "Cet entraînement se fait à deux, en classe : la situation et les sujets "
        + "à couvrir sont ci-dessous.");
    if (tete && tete.nextSibling) carte.insertBefore(mot, tete.nextSibling);
    else carte.insertBefore(mot, sep);
  }

  /* Aide après erreurs — « Pourquoi je me trompe ? » part, « Revoir
     l'explication » reste : une mini-leçon est du texte écrit d'avance. Un
     panneau qui n'aurait plus que « Plus tard » à offrir est un reproche, pas
     une aide : on le retire au lieu de l'afficher vide. */
  function replierAide() {
    if (typeof analyserErreurs === 'function') analyserErreurs = function () {};
    if (typeof proposerAide !== 'function') return;
    var orig = proposerAide;
    proposerAide = function (exId) {
      var r = orig.apply(this, arguments);
      var el = document.getElementById('aide-' + exId);
      if (!el) return r;
      var ia = el.querySelector('button[onclick^="analyserErreurs"]');
      if (ia) ia.remove();
      var reste = el.querySelector('.aide-btns button[onclick^="accepterAide"]');
      if (!reste) el.remove();
      return r;
    };
  }

  /* Exercices écrits — la correction par comparaison de chaînes (`it.accept`)
     n'a jamais rien eu d'une IA : elle reste, telle quelle. Seule la réponse
     ouverte change : plus d'appel, et la réponse attendue après deux essais,
     le même rythme que la version avec assistant. */
  function replierExercicesEcrits() {
    if (typeof checkWrite !== 'function' || typeof EXOS === 'undefined') return;
    var orig = checkWrite;
    var essais = {};
    checkWrite = function (exId, i) {
      var ex = EXOS.find(function (e) { return e.id === exId; });
      if (!ex) return;
      var it = ex.items[i];
      if (it && it.accept) return orig.apply(this, arguments);

      var inp = document.getElementById('wi_' + exId + '_' + i);
      var fb = document.getElementById('wf_' + exId + '_' + i);
      if (!inp || !fb) return;
      var val = (inp.value || '').trim();
      if (!val) { fb.className = 'wfb no'; fb.textContent = "✏️ Écris ta réponse d'abord."; return; }

      var k = exId + '_' + i;
      var n = essais[k] = (essais[k] || 0) + 1;
      var attendu = (it && it.hint) || '';

      if (!attendu) {
        /* Rien à comparer et personne pour lire : le dire franchement vaut
           mieux qu'un ✅ qui ne vérifie rien. */
        fb.className = 'wfb';
        fb.innerHTML = "📝 Ta réponse est notée. Vous la corrigerez en classe.";
        if (typeof trackPlacement === 'function') trackPlacement('w_' + exId + '_' + i, false);
        return;
      }

      /* WSOL et WFB appartiennent à la greffe « deux essais » : quand elle est
         là, on s'en sert pour que « Montrez-moi la réponse » se comporte
         exactement comme dans l'autre version. */
      if (typeof WSOL !== 'undefined') WSOL[k] = attendu;
      if (typeof WFB !== 'undefined') WFB[k] = '';

      fb.className = 'wfb no';
      if (n < 2 && typeof wBoutonReponse === 'function') {
        fb.innerHTML = "💡 Relis ta phrase et vérifie chaque mot."
                     + wBoutonReponse(exId, i);
      } else {
        fb.innerHTML = "💡 <b>La réponse attendue :</b> "
                     + (typeof esc === 'function' ? esc(attendu) : attendu)
                     + '<br><span style="font-weight:600">Compare-la avec la tienne, '
                     + 'puis réécris-la dans la case.</span>';
      }
      if (typeof trackPlacement === 'function') trackPlacement('w_' + exId + '_' + i, false);
      if (typeof evaluerAide === 'function') {
        var rates = ex.items.reduce(function (s, _, j) {
          return s + (essais[exId + '_' + j] || 0);
        }, 0);
        evaluerAide(exId, rates);
      }
    };
  }

  /* La barre « Mes outils » porte la plus grosse part d'IA du module :
     traduire, simplifier, demander. Elle sait se replier elle-même — elle est
     partagée par les 87 modules, et la règle doit vivre à un seul endroit. */
  function replierOutils() {
    if (window.Outils && typeof Outils.sansIA === 'function') Outils.sansIA();
  }

  function replier() {
    document.body.classList.add('sans-ia');
    window.MODE_IA = false;
    replierOral();
    replierEcrit();
    replierJeuDeRole();
    replierAide();
    replierExercicesEcrits();
    replierOutils();
  }

  /* ── La question, posée une seule fois ───────────────────────────────── */

  async function demander() {
    var code = (typeof studentCode !== 'undefined' && studentCode) ? studentCode : '';
    try {
      var res = await fetch('/api/student/ia?code=' + encodeURIComponent(code));
      var data = await res.json();
      /* Une panne de réseau ne coupe rien : les routes IA sont gardées côté
         serveur de toute façon, et replier sur un délai d'attente ferait
         clignoter le module d'une classe à l'autre. */
      if (data && data.ia === false) replier();
    } catch (e) { /* on laisse le module tel quel */ }
  }

  /* On passe APRÈS l'initialisation de la barre d'outils, qui se fait au
     chargement du module : sinon il n'y aurait encore rien à retirer. */
  function departer() { setTimeout(demander, 0); }
  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', departer);
  else departer();
})();
</script>
""" + FIN + "\n"


def cibles(args):
    if args.un:
        return ["assets/interactive/{0}/{0}-activite-interactive.html".format(args.un)]
    if args.tous:
        return [GABARIT] + sorted(glob.glob(TOUS))
    return [GABARIT] + [
        "assets/interactive/{0}/{0}-activite-interactive.html".format(s) for s in ONZE
    ]


def poser(chemin, retirer):
    try:
        s = io.open(chemin, encoding="utf-8").read()
    except IOError:
        return "absent"
    deja = DEBUT in s
    if retirer:
        if not deja:
            return "déjà retiré"
        s = re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN) + r"\n?", "", s,
                   flags=re.S)
        io.open(chemin, "w", encoding="utf-8").write(s)
        return "retiré"
    if deja:
        return "déjà fait"
    if "</body>" not in s:
        return "introuvable"
    io.open(chemin, "w", encoding="utf-8").write(s.replace("</body>", BLOC + "</body>", 1))
    return "greffé"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tous", action="store_true",
                    help="poser sur les 87 modules, pas seulement les onze")
    ap.add_argument("--un", metavar="SLUG",
                    help="un seul module, sans toucher au gabarit")
    ap.add_argument("--retirer", action="store_true", help="revenir en arrière")
    args = ap.parse_args()

    compte = {}
    for chemin in cibles(args):
        etat = poser(chemin, args.retirer)
        compte[etat] = compte.get(etat, 0) + 1
        if etat in ("introuvable", "absent"):
            print("  ! {} — {}".format(chemin, etat))
    for etat in sorted(compte):
        print("{:>4}  {}".format(compte[etat], etat))
    return 1 if compte.get("introuvable") or compte.get("absent") else 0


if __name__ == "__main__":
    sys.exit(main())
