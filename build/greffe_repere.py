#!/usr/bin/env python3
"""Poser « Module 12 · Niveau 3 » dans les modules qui ne sont pas engendrés.

    python3 build/greffe_repere.py --essai
    python3 build/greffe_repere.py

Depuis le 22 août 2026, l'en-tête de chaque module porte son numéro et son
niveau : l'élève arrive par un signet ou par l'adresse qu'un voisin lui a
passée, et rien à l'écran ne lui disait lequel des cinquante-huit il ouvrait.
`build/gabarit.py` pose le repère, et `build/module.py` le remplit depuis le
registre — donc les quarante-neuf modules engendrés l'ont eu en une commande.

Restent **neuf modules du niveau 4** écrits avant le gabarit : ils n'ont pas
de manifeste et ne se régénèrent pas. `module-consultation` est même la source
dont le gabarit est tiré — le régénérer n'aurait aucun sens. Pour eux, la
greffe est la façon de faire du dépôt, comme `greffe_outils.py` ou
`greffe_sections.py`.

Elle est **idempotente** : un module déjà greffé est sauté, et le repère est
relu depuis le registre à chaque passage, donc renuméroter puis relancer
suffit à corriger.

**Conséquence à connaître** : le numéro est maintenant écrit dans le module.
Renuméroter un niveau obligeait déjà à régénérer les PowerPoints ; il faut
désormais régénérer les modules et relancer cette greffe.
"""
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build' / 'powerpoints'))
from modules import MODULES                                  # noqa: E402

REGLE = ("\n.hdr-ref{padding-left:8px;border-left:1px solid "
         "var(--line-300,#D8DEE6);font-weight:var(--fw-regular,400);"
         "text-transform:none;letter-spacing:0;color:var(--text-600,#5A6472);"
         "white-space:nowrap}"
         "\n@media(max-width:480px){.hdr-ref{display:none}}")

RE_EYE = re.compile(r'(<div class="hdr-eye">)(.*?)(</div>)', re.S)


def greffer(html, repere):
    if 'class="hdr-ref"' in html:
        return html, 'déjà greffé'
    m = RE_EYE.search(html)
    if not m:
        return html, 'en-tête .hdr-eye introuvable'
    if '<span' in m.group(2) or '<div' in m.group(2):
        return html, 'en-tête inattendu, laissé tel quel'
    html = (html[:m.end(2)]
            + '<span class="hdr-ref">%s</span>' % repere
            + html[m.end(2):])
    if '.hdr-ref{' not in html:
        i = html.find('.hdr-eye{')
        if i < 0:
            return html, 'règle .hdr-eye introuvable'
        fin = html.find('}', i) + 1
        html = html[:fin] + REGLE + html[fin:]
    return html, None


def main():
    essai = '--essai' in sys.argv
    faits, sautes, ecarts = [], [], []
    for slug, m in sorted(MODULES.items()):
        fichiers = list((RACINE / 'assets' / 'interactive' / slug)
                        .glob('*activite-interactive.html'))
        if not fichiers:
            ecarts.append((slug, 'aucun module construit')); continue
        f = fichiers[0]
        html = f.read_text(encoding='utf-8')
        repere = 'Module %s · Niveau %s' % (m['numero'], m['niveau'])
        neuf, souci = greffer(html, repere)
        if souci == 'déjà greffé':
            sautes.append(slug); continue
        if souci:
            ecarts.append((slug, souci)); continue
        if not essai:
            f.write_text(neuf, encoding='utf-8')
        faits.append((slug, repere))
    print('%s%d greffé(s), %d déjà fait(s), %d écart(s)'
          % ('[essai] ' if essai else '', len(faits), len(sautes), len(ecarts)))
    for slug, repere in faits:
        print('    · %-28s %s' % (slug, repere))
    for slug, souci in ecarts:
        print('    ✗ %-28s %s' % (slug, souci))
    return 1 if ecarts else 0


if __name__ == '__main__':
    sys.exit(main())
