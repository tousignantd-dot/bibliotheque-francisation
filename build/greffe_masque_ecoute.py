#!/usr/bin/env python3
"""Masque l'énoncé des exercices d'écoute dont la réponse se lit dans l'énoncé.

Un exercice comme « Sur, dans ou à ? » (module 1 du niveau 5) fait écouter une
phrase et demande quelle préposition on a entendue — mais il écrit la phrase
sous le bouton d'écoute, préposition comprise. L'élève lit et répond sans
jamais écouter.

La greffe remplace le texte par une étiquette neutre — « Phrase 3 », « Mot 5 » —
tant que l'exercice n'est pas corrigé, puis **rend le texte** dès la correction :
il faut voir ce qu'on vient d'entendre pour apprendre quelque chose de sa
propre erreur. L'audio n'est pas touché.

    python3 build/greffe_masque_ecoute.py            # tous les modules visés
    python3 build/greffe_masque_ecoute.py n5-logement
    python3 build/greffe_masque_ecoute.py --retirer

**Ce qui n'est pas visé, et pourquoi.** Les exercices de phonétique où le mot
écrit est le point de départ — « psychologie : les lettres marquées, c'est
comme K ? » ou « [e] ou [ɛ] dans "chèque" ? » — gardent leur texte : la réponse
est un son, elle n'est pas écrite, et cacher le mot ferait disparaître la leçon
au lieu de l'indice. Le critère retenu est celui-ci : **masquer quand un élève
qui n'appuie jamais sur écouter peut répondre juste en lisant.**

**Deux chemins, et un seul à la fois.** Le gabarit reconnaît `masque:true` sur
un exercice, et les `build/contenu/<slug>/exos.js` visés le portent : un module
reconstruit masque donc tout seul, sans cette greffe — c'est pourquoi elle
n'est PAS inscrite à `build/module.py`. La greffe sert aux fichiers déjà
produits, qu'on ne reconstruit pas. Les deux se croisent sans dégât : le bloc
greffé laisse tranquille un texte que le gabarit a déjà masqué (`.ph-cache`).
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
INTERACTIF = ROOT / 'assets' / 'interactive'

DEBUT = '<!-- MASQUE-ECOUTE:début — greffé par build/greffe_masque_ecoute.py -->'
FIN = '<!-- MASQUE-ECOUTE:fin -->'

# Les identifiants d'exercice sont **gravés** ici, module par module : le bloc
# greffé ne devine rien. Relevé le 30 août 2026 sur les cent exercices `listen`
# des quatre-vingt-sept modules.
CIBLES = {
    'module-activite':           ['prChiffres'],   # moins de 100 $ ou plus
    'module-n1-classe':          ['prNombres'],    # deux ou douze
    'module-n1-inscription':     ['prSons'],       # treize ou trente
    'module-n2-autobus':         ['prHeure'],      # l'heure juste ou non
    'module-n2-bonjour':         ['prSons'],       # question ou réponse
    'module-n2-couloirs':        ['prSons'],       # avant 10 ou après 10
    'module-n2-guichet':         ['prSon'],        # treize ou trente
    'module-n3-electro':         ['t2mesures'],    # un prix ou une mesure
    'module-n3-epicerie':        ['prNombres'],    # treize ou trente
    'module-n3-horaire':         ['t1ecoute',      # matin ou après-midi
                                  't2ecoute',      # permission ou aide
                                  't3ecoute'],     # c'est fait ou pas
    'module-n3-pharmacie':       ['t1qui'],        # qui parle
    'module-n3-poste':           ['t1qui'],        # qui parle
    'module-n3-recherche-emploi': ['t1qui', 'aQui'],
    'module-n3-restaurant':      ['t2qui'],
    'module-n3-vetements':       ['t3montant'],    # au-dessus de 50 $ ou non
    'module-n3-voisins':         ['t1qui', 'aQui'],
    'module-n5-degat':           ['prSon'],        # eau, au ou o : c'est écrit
    'module-n5-logement':        ['prPhon'],       # sur, dans ou à
    'module-n5-voisinage':       ['prPhon'],       # la voix monte ou descend
    'module-n7-banque':          ['prChiffres'],   # taux, montant ou durée
    'module-n7-emploi':          ['prProso'],      # la voix continue ou finit
    'module-n8-emploi':          ['prProso'],      # idem
    'module-relations':          ['prPhon'],       # on insiste ou pas
    'module-vetements':          ['prPhon'],       # masculin ou féminin
}

GABARIT = DEBUT + """
<script>
(function () {
  var CIBLES = %(cibles)s;

  var css = document.createElement('style');
  css.textContent = '.ph-word.masque-ecoute,.stxt.masque-ecoute{font-size:17px;'
    + 'font-weight:700;font-style:italic;color:var(--ws-ink-3,#6B6F76)}';
  document.head.appendChild(css);

  /* Une étiquette, et pas rien : sans elle la carte n'est plus qu'un bouton et
     l'élève ne sait plus laquelle il vient d'écouter. */
  function etiquette(txt, i) {
    return (/\\s/.test(String(txt).trim()) ? 'Phrase ' : 'Mot ') + (i + 1);
  }

  /* Les cartes sont créées dans l'ordre de `ex.rows` par le rendu du module :
     la i-ième carte est la i-ième ligne. On repasse après chaque `render()`
     parce que le rendu recrée les nœuds à chaque fois. */
  function masquer() {
    if (typeof EXOS === 'undefined' || typeof S === 'undefined') return;
    for (var k = 0; k < CIBLES.length; k++) {
      var ex = null;
      for (var e = 0; e < EXOS.length; e++) {
        if (EXOS[e] && EXOS[e].id === CIBLES[k]) { ex = EXOS[e]; break; }
      }
      var mount = document.getElementById('mount-' + CIBLES[k]);
      if (!ex || !ex.rows || !mount) continue;
      var textes = mount.querySelectorAll('.ph-card .ph-word, .vf-row .stxt');
      for (var i = 0; i < textes.length; i++) {
        var el = textes[i], r = ex.rows[i];
        if (!r) continue;
        // Déjà masqué par le gabarit : on ne masque pas un masque.
        if (el.classList.contains('ph-cache')) continue;
        // Corrigé : le texte revient, c'est là qu'il sert.
        if (S.fb && S.fb[r.id]) continue;
        el.textContent = etiquette(el.textContent, i);
        el.classList.add('masque-ecoute');
      }
    }
  }

  function poser() {
    if (typeof render === 'function') {
      var rendreOrig = render;
      render = function () {
        var res = rendreOrig.apply(this, arguments);
        masquer();
        return res;
      };
    }
    masquer();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', poser);
  } else {
    poser();
  }
})();
</script>
""" + FIN


def degreffe(html):
    return re.sub(re.escape(DEBUT) + r'.*?' + re.escape(FIN) + r'\n?', '',
                  html, flags=re.S)


def greffe(html, ids):
    """Repose le bloc juste avant `</body>` : `render` doit exister pour être
    enveloppé, donc après le script du module."""
    html = degreffe(html)
    if '</body>' not in html:
        raise ValueError('</body> introuvable')
    liste = '[' + ', '.join("'%s'" % i for i in ids) + ']'
    return html.replace('</body>', GABARIT % {'cibles': liste} + '\n</body>', 1)


def page_du_module(dossier, ids):
    """La page de l'activité, et pas la première venue : un dossier de module
    peut contenir plusieurs HTML (module-travail en a quatre). On prend celle
    qui déclare les exercices visés."""
    candidates = sorted(dossier.glob('*.html'))
    for p in candidates:
        t = p.read_text(errors='replace')
        if 'const EXOS = [' in t and all(("id:'%s'" % i) in t or ('id: \'%s\'' % i) in t for i in ids):
            return p
    return None


def main(argv):
    retirer = '--retirer' in argv
    voulus = [a for a in argv if not a.startswith('--')]
    faits, manquants = 0, []
    for nom in sorted(CIBLES):
        court = nom.replace('module-', '')
        if voulus and nom not in voulus and court not in voulus:
            continue
        dossier = INTERACTIF / nom
        if not dossier.is_dir():
            manquants.append(nom + ' (dossier absent)')
            continue
        page = page_du_module(dossier, CIBLES[nom])
        if page is None:
            manquants.append(nom + ' (exercices introuvables)')
            continue
        avant = page.read_text(errors='replace')
        apres = degreffe(avant) if retirer else greffe(avant, CIBLES[nom])
        if apres != avant:
            page.write_text(apres)
            print(('dégreffé  ' if retirer else 'greffé    ') + nom
                  + '  (' + ', '.join(CIBLES[nom]) + ')')
        else:
            print('inchangé  ' + nom)
        faits += 1
    if manquants:
        print('\nNon greffés : ' + ', '.join(manquants))
    if voulus and not faits:
        print('Aucun module visé de ce nom.')
        return 1
    print('\n%d module(s), %d exercice(s).'
          % (faits, sum(len(CIBLES[n]) for n in CIBLES
                        if not voulus or n in voulus
                        or n.replace('module-', '') in voulus)))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
