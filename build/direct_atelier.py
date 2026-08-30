#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le direct de la classe, pour les ateliers de la banque.

    python3 build/direct_atelier.py --essai   # dit ce qu'il ferait
    python3 build/direct_atelier.py           # écrit dans les six générateurs
    python3 build/direct_atelier.py --retirer # revient en arrière

**Le manque.** Un enseignant qui ouvrait une séance sur un atelier — « Le
relevé de compte », par exemple — obtenait un direct vide. Les ateliers
n'envoyaient que des compteurs (`exercise_attempted`), jamais la réussite
d'une question, qui est la seule chose utile pendant qu'une classe répond.

**Ce qui rend le geste petit.** Le serveur n'a besoin d'aucun registre de
questions : `/api/direct` regroupe ce qu'il reçoit, et une carte paraît dès
la première réponse envoyée. Et les six générateurs ont chacun **un seul**
endroit où une réponse est jugée — la ligne `lmsTrack('exercise_attempted')`.
On pose donc une fonction commune et six appels, au lieu de réécrire 56
fichiers.

**L'identifiant d'une question est le `slug` de l'item.** Tous les items de
tous les contenus en portent un. C'est ce qui permet de regrouper les
réponses de la classe : un atelier tire ses items au hasard, l'ordre change
d'un élève à l'autre, et un numéro de tour ne voudrait donc rien dire.

**Ce qu'un atelier n'est pas.** Il tire sans fin, deux élèves ne voient pas
les mêmes questions, et rien ne signale « terminé ». Le direct d'un atelier
ne se lit pas comme celui d'un module : c'est « qui répond, à quel rythme,
et quels items font trébucher la classe » — pas une grille à remplir.

La charge utile est **celle des modules** (`build/greffe_direct.py`) : l'écran
de l'enseignant n'a pas deux formes à comprendre.

Idempotent, et se retire sans laisser de trace.
"""
import argparse
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUT = "/* DIRECT-ATELIER:début — posé par build/direct_atelier.py */"
FIN = "/* DIRECT-ATELIER:fin */"

# La fonction commune. Elle passe par `lmsTrack`, qui sait déjà lire le code
# de l'élève et le numéro d'activité dans l'adresse de la page parente : un
# atelier ne connaît donc toujours ni l'un ni l'autre.
FONCTION = DEBUT + """
/* Le direct de la classe : une tentative par question. Même charge utile que
   les modules — voir build/greffe_direct.py. L'identifiant de la question est
   le `slug` de l'item : l'ordre de tirage change d'un élève à l'autre, un
   numéro de tour ne regrouperait rien. */
var DZ_ESSAIS = {};
function directZone(z) {
  if (!z || !z.slug) return;
  var faits = DZ_ESSAIS[z.slug] || 0;
  lmsTrack('zone_repondue', {
    zone: String(z.slug),
    exo: (typeof CONTENU !== 'undefined' && CONTENU.slug) || 'atelier',
    exoTitre: (typeof CONTENU !== 'undefined' && CONTENU.titre) || '',
    type: (typeof CONTENU !== 'undefined' && (CONTENU.mode || CONTENU.generateur)) || '',
    enonce: String(z.enonce == null ? '' : z.enonce).slice(0, 400),
    bonne: String(z.bonne == null ? '' : z.bonne),
    reponse: String(z.reponse == null ? '' : z.reponse),
    ok: !!z.ok,
    /* Les essais déjà ratés sur CETTE question, avant celui-ci : c'est ce
       qui sépare « juste du premier coup » de « juste après essai » dans le
       direct. Un item revient plus tard dans le tirage, donc le compte se
       tient par slug et non par tour. */
    essais: faits
  });
  if (!z.ok) DZ_ESSAIS[z.slug] = faits + 1;
}
""" + FIN + "\n"

# Un générateur = où poser la fonction, et l'appel à glisser après la ligne
# qui juge déjà la réponse. L'ancre est cette ligne elle-même : elle est
# unique dans chaque fichier, et c'est exactement l'endroit où le verdict
# vient d'être calculé.
ANCRE = "  lmsTrack('exercise_attempted', { correct: %s });"

GENERATEURS = {
    # texte : « questions » pose une question sur un extrait, « trous » fait
    # choisir le mot qui manque. Les deux ont `choisi` et `courant.ok`.
    'texte': (ANCRE % "juste ? 1 : 0", """  directZone({ slug: courant.slug, ok: juste,
    enonce: courant.q || ('Le trou ' + courant.numero), bonne: courant.ok, reponse: choisi });"""),
    # phrase : « choix » remplit un trou, « ordre » remet les mots en ordre —
    # la réponse est alors la phrase reconstruite par l'élève.
    'phrase': (ANCRE % "juste ? 1 : 0", """  directZone({ slug: courant.slug, ok: juste,
    enonce: courant.phrase, bonne: MODE === 'ordre' ? courant.mots.join(' ') : courant.ok,
    reponse: MODE === 'ordre' ? posees.map(i => courant.mots[i]).join(' ') : choisi });"""),
    # conjugaison : « ecrire » compare une forme saisie, « choisir » un choix.
    'conjugaison': (ANCRE % "juste ? 1 : 0", """  directZone({ slug: x.slug, ok: juste,
    enonce: x.phrase || (x.infinitif + ' · ' + x.temps), bonne: x.ok,
    reponse: MODE === 'ecrire' ? ecrit : choisi });"""),
    # graphie : une dictée de caractères. L'énoncé est l'étiquette montrée.
    'graphie': (ANCRE % "juste ? 1 : 0", """  directZone({ slug: x.slug, ok: juste,
    enonce: x.etiquette || x.valeur, bonne: attendu, reponse: ecrit });"""),
    # oreille : « barrer » raye ce qui n'a pas été dit, les autres choisissent.
    'oreille': (ANCRE % "juste ? 1 : 0", """  directZone({ slug: courant.slug, ok: juste,
    enonce: courant.dit || courant.indice || courant.sens || '', bonne: courant.ok,
    reponse: MODE === 'barrer' ? '' : choisi });"""),
    # appariement : le jugement est dans le gestionnaire d'un bouton, un cran
    # plus indenté que les cinq autres. `rEnonce` et `rBonne` sont les deux
    # REGISTRES appariés (l'heure en chiffres, l'heure en lettres…), pas des
    # réponses : ce que l'élève a touché, c'est `opt.item`. L'énoncé dit donc
    # l'item ET le sens de l'appariement, sans quoi deux tours du même item
    # dans deux sens se confondraient dans le direct.
    'appariement': ("      lmsTrack('exercise_attempted', { correct: opt.bonne ? 1 : 0 });",
                    """      directZone({ slug: cibleCourante.slug, ok: !!opt.bonne,
        enonce: cibleCourante.nom + ' (' + rEnonce.nom + ' → ' + rBonne.nom + ')',
        bonne: cibleCourante.nom, reponse: opt.item.nom });"""),
}


class Ecart(Exception):
    pass


def poser(src, appel):
    if DEBUT in src:
        return src, False
    ancre, ligne = appel
    if src.count(ancre) != 1:
        raise Ecart("%d ancre(s) au lieu d'une : %s" % (src.count(ancre), ancre.strip()[:48]))
    # La fonction se pose juste après lmsTrack, dont elle se sert.
    m = re.search(r"^function lmsTrack\(event, data\) \{.*?^\}\n", src, re.S | re.M)
    if not m:
        raise Ecart("lmsTrack introuvable")
    src = src[:m.end()] + FONCTION + src[m.end():]
    return src.replace(ancre, ancre + "\n" + ligne, 1), True


def retirer(src, appel):
    ancre, ligne = appel
    if DEBUT not in src:
        return src, False
    i, j = src.index(DEBUT), src.index(FIN) + len(FIN) + 1
    src = src[:i] + src[j:]
    return src.replace(ancre + "\n" + ligne, ancre, 1), True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--essai', action='store_true')
    ap.add_argument('--retirer', action='store_true')
    a = ap.parse_args()
    faits = sautes = 0
    for nom, appel in sorted(GENERATEURS.items()):
        chemin = os.path.join(RACINE, 'build', nom + '.py')
        src = io.open(chemin, encoding='utf-8').read()
        try:
            neuf, change = (retirer if a.retirer else poser)(src, appel)
        except Ecart as e:
            print('  ÉCART  %-14s %s' % (nom, e))
            return 1
        if not change:
            sautes += 1
            continue
        if not a.essai:
            io.open(chemin, 'w', encoding='utf-8').write(neuf)
        faits += 1
        print('  %-14s %s' % (nom, 'retiré' if a.retirer else 'posé'))
    print('%s%d générateur(s) %s, %d déjà fait(s)'
          % ('[essai] ' if a.essai else '', faits,
             'retiré(s)' if a.retirer else 'posé(s)', sautes))
    print('Relancez ensuite `python3 build/banque.py` pour réécrire les ateliers.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
