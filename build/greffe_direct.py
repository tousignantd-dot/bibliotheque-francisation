#!/usr/bin/env python3
"""Le direct de la classe : le module rapporte chaque tentative, zone par zone.

`/api/student/progress` n'envoyait que des compteurs — `zonesDone`, `firstTry`,
`totalErrors` — et jamais les réponses. L'enseignante voyait donc l'avancement
d'un élève, mais **jamais la réussite d'une question**, ce qui est la seule
chose utile pendant qu'une classe répond sur ses téléphones. Cette greffe ajoute
l'événement `zone_repondue` : un envoi par tentative, avec l'énoncé de la zone
et la réponse donnée quand elle a une bonne réponse connue.

Trois choses la rendent sûre là où elle est posée :

  **Elle enveloppe `trackPlacement()`, elle ne la modifie pas.** Même parti pris
  que `greffe_depot_ecrit.py` avec `renderCorr()` : le module garde son code, et
  les sept endroits qui appellent `trackPlacement` — vrai/faux, glisser-déposer,
  vocabulaire, texte, cases à écrire — sont couverts d'un coup. Une fonction
  déclarée au premier niveau d'un script classique est une propriété de
  `window` : la remplacer change ce que voient les appels suivants.

  **Elle ne connaît ni slug ni numéro d'activité.** Le code de l'élève et
  l'identifiant de l'activité se lisent dans l'adresse de la page parente,
  exactement comme le fait déjà `lmsTrack()`. C'est ce qui permet de la poser
  sur le gabarit sans qu'un module généré hérite de l'identité d'un autre.

  **Le texte d'une réponse ouverte ne part pas.** Une case corrigée par
  l'assistant (`item` sans `accept`) n'envoie que juste/faux et le nombre
  d'essais. Les corrections de l'IA restent privées, ici comme partout ailleurs
  dans ce dépôt — et le serveur le revérifie de son côté.

    python3 build/greffe_direct.py            # gabarit + les onze modules
    python3 build/greffe_direct.py --tous     # gabarit + les 87 modules
    python3 build/greffe_direct.py --un module-sante
    python3 build/greffe_direct.py --retirer  # revient en arrière

Idempotente, et se retire sans laisser de trace.
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

DEBUT = "<!-- DIRECT-CLASSE:début — greffé par build/greffe_direct.py -->"
FIN = "<!-- DIRECT-CLASSE:fin -->"

BLOC = DEBUT + """
<script>
(function () {
  'use strict';

  /* Ce que le module sait de l'adresse : le code de l'élève et le numéro de
     l'activité. Sans les deux, on ne rapporte rien — un module ouvert par
     double-clic ne doit pas essayer de parler à un serveur. */
  function contexte() {
    try {
      var p = new URLSearchParams(window.parent.location.search);
      var code = p.get('code');
      var id = parseInt(p.get('activityId'), 10);
      if (!code || !id) return null;
      return { code: code, activityId: id, title: p.get('title') || '' };
    } catch (e) { return null; }
  }

  var CTX = contexte();
  if (!CTX) return;

  function exoDe(exId) {
    try { return EXOS.find(function (e) { return e.id === exId; }) || null; }
    catch (e) { return null; }
  }

  /* L'étiquette visible d'une réponse du banc. `cv` d'une zone de placement est
     un identifiant ; l'enseignante a besoin des mots. */
  function etiquetteBanc(ex, id) {
    if (!ex || !ex.bank) return '';
    var b = ex.bank.find(function (t) { return t.id === id; });
    return b ? String(b.l || '') : '';
  }

  /* L'énoncé de la zone, pris là où le module le tient déjà — jamais recopié
     dans une table à tenir à jour. */
  function enonceDe(ex, zid, z) {
    if (!ex) return '';
    try {
      if (ex.type === 'vf' || ex.type === 'match' || ex.type === 'imgmatch'
          || ex.type === 'rows' || ex.type === 'texte') {
        var r = (ex.rows || []).find(function (x) { return x.id === zid; });
        if (r) return String(r.txt || r.q || r.l || '').replace(/<[^>]+>/g, '');
      }
      if (ex.type === 'blanks') {
        return (ex.segs || []).map(function (s) {
          return s.k === 'b' ? ' ____ ' : String(s.t || '');
        }).join('').replace(/\\s+/g, ' ').trim();
      }
      if (ex.type === 'write') {
        var i = parseInt(String(zid).split('_').pop(), 10);
        var it = (ex.items || [])[i];
        if (it) return String(it.q || '').replace(/<[^>]+>/g, '');
      }
    } catch (e) {}
    return '';
  }

  /* La réponse donnée et la bonne réponse, dans les mots que l'enseignante lit.
     Rendre une chaîne vide pour `bonne` suffit à ce que le serveur jette le
     texte : c'est la garantie que porte une réponse ouverte. */
  function reponseDe(ex, zid, z) {
    var vide = { reponse: '', bonne: '' };
    if (!ex) return vide;
    try {
      if (ex.type === 'write') {
        var i = parseInt(String(zid).split('_').pop(), 10);
        var it = (ex.items || [])[i];
        var inp = document.getElementById('wi_' + ex.id + '_' + i);
        // Sans `accept`, c'est l'assistant qui corrige : rien ne monte.
        if (!it || !it.accept || !it.accept.length) return vide;
        return { reponse: inp ? String(inp.value || '').trim() : '',
                 bonne: String(it.accept[0] || '') };
      }
      // Une image ne se compte pas en mots : on garde le juste/faux et on
      // laisse tomber la répartition, qui n'aurait rien à afficher.
      if (ex.type === 'imgmatch') return vide;
      if (z && (z.zcat === 'vf' || z.zcat === 'lbl')) {
        var choix = (S.pl[zid] && S.pl[zid].lbl) || S.vfSel[zid] || '';
        return { reponse: String(choix), bonne: String(z.cv || '') };
      }
      if (z) {
        var mis = (S.pl[zid] && S.pl[zid].lbl) || etiquetteBanc(ex, S.pl[zid] && S.pl[zid].iid);
        return { reponse: String(mis || ''), bonne: etiquetteBanc(ex, z.cv) };
      }
    } catch (e) {}
    return vide;
  }

  function rapporter(zid, ok) {
    var z = null;
    try { z = ZONES[zid] || null; } catch (e) {}
    var ex = exoDe(z ? z.exo : null);
    var r = reponseDe(ex, zid, z);
    var essais = 0;
    try { essais = TR.attempts[zid] || 0; } catch (e) {}
    var corps = {
      code: CTX.code, activityId: CTX.activityId, activityTitle: CTX.title,
      event: 'zone_repondue',
      zone: zid,
      exo: (ex && ex.id) || (z && z.exo) || '',
      exoNum: (ex && ex.num) || '',
      exoTitre: (ex && ex.tit) || '',
      section: (ex && ex.sec) || '',
      type: (ex && ex.type) || '',
      enonce: enonceDe(ex, zid, z),
      bonne: r.bonne,
      reponse: r.reponse,
      ok: !!ok,
      essais: essais
    };
    fetch('/api/student/progress', {
      method: 'POST', headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(corps)
    }).catch(function () {});
  }

  /* L'enveloppe. Elle ne se pose qu'une fois, et jamais avant que le module ait
     déclaré sa fonction — d'où l'attente du chargement complet. */
  function envelopper() {
    if (typeof window.trackPlacement !== 'function') return false;
    if (window.trackPlacement.__direct) return true;
    var origine = window.trackPlacement;
    var enveloppe = function (zid, ok) {
      var sortie = origine.apply(this, arguments);
      // Le rapport ne doit jamais empêcher l'exercice de se corriger : ce que
      // l'élève voit passe avant ce que l'enseignante voit.
      try { rapporter(zid, ok); } catch (e) {}
      return sortie;
    };
    enveloppe.__direct = true;
    window.trackPlacement = enveloppe;
    return true;
  }

  function departer() {
    if (envelopper()) return;
    // Un module dont le script n'a pas encore tourné : on repasse, sans
    // s'acharner.
    var restes = 20;
    var iv = setInterval(function () {
      if (envelopper() || --restes <= 0) clearInterval(iv);
    }, 250);
  }

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
