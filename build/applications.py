#!/usr/bin/env python3
"""L'onglet « Applications » du classeur : la dernière version de chaque
application, et, dessous, les codes d'essai qu'on peut donner.

POURQUOI. Demande de Daniel, 30 septembre 2026 : « un onglet sur la dernière
version de toutes les applications qui ont été développées », et pour celles
qui s'ouvrent par un code (Compostelle, Maison Francœur, Hôtel Rive-Claire),
« la liste des codes que je peux donner pour des tests ». Les fiches du
classeur racontent le chantier ; celle-ci répond à une seule question : quel
lien j'envoie, et avec quel code.

CE QUI N'EST PAS ÉCRIT À LA MAIN :
  - la date de chaque application est celle du dernier commit qui a touché la
    page servie (ou son dossier) — une date écrite ici serait fausse au
    prochain déploiement, et elle rassurerait à tort ;
  - les codes sont LUS dans `pelerins.py` (`CODES_ESSAI`, `CODES_ESSAI_TROUSSES`,
    `ESSAI_FIN`, `ESSAI_CONVERSATIONS`) : c'est lui qui les fait marcher, donc
    lui seul peut dire lesquels marchent. Retirer un code de `pelerins.py`, puis
    relancer ce script, le retire d'ici.
  - l'adresse complète est posée dans la page au chargement, à partir de
    l'adresse du classeur : aucun nom de domaine n'est écrit (même règle que
    la feuille de séance).

Ce qui EST écrit ici, et doit l'être : QUELLE page est la bonne version. Pour
le barista, c'est la formation qui commence par la tournée de la machine
(`tournee.html`) — dit par Daniel le 30 septembre 2026 ; la v10
(`avant-louverture-v10.html`) est une version antérieure.

    python3 build/applications.py            # repose le bloc dans la page
    python3 build/applications.py --essai    # dit ce qu'il poserait, sans écrire
"""
import html
import pathlib
import re
import subprocess
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
PAGE = RACINE / "presentations.html"
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402

MOIS = ("janvier février mars avril mai juin juillet août septembre octobre "
        "novembre décembre").split()

# (étagère, [(nom, chemin servi, ce que c'est, clé des codes ou None)])
# La clé des codes : "compostelle" pour CODES_ESSAI, sinon le nom de la trousse
# dans CODES_ESSAI_TROUSSES.
APPLICATIONS = [
    ("Voyage", [
        ("En route vers Compostelle", "modules-autonomes/compostelle/",
         "L'espagnol du pèlerin, du départ à Santiago. Tout est gratuit sauf "
         "« Parler librement », qui s'ouvre avec un code.", "compostelle"),
        ("Une semaine à Toronto", "modules-autonomes/toronto/",
         "L'anglais du touriste francophone : huit séances, le test, les mots, les "
         "exercices, la semaine jouée avec l'assistance (dix lieux et Maya, ouverte "
         "par un code) et la poche hors ligne.", "toronto"),
        ("Montréal en poche", "modules-autonomes/montreal/",
         "Le guide touristique de Montréal pour le téléphone, en trois "
         "langues. Tout est ouvert, aucun code.", None),
    ]),
    ("Formations en entreprise", [
        ("Hôtel Rive-Claire — la réception", "modules-autonomes/hotel-reception/",
         "L'écran de l'employé : les mots, les exercices, le test, puis le "
         "comptoir joué, qui s'ouvre avec un code.", "hotel"),
        ("Maison Francœur — la vente de vêtements", "modules-autonomes/francoeur-planches/",
         "Les planches, les exercices, le test de niveau, puis le magasin joué, "
         "qui s'ouvre avec un code.", "francoeur"),
        ("Belrive — le bloc 3", "modules-autonomes/belrive-bloc3/",
         "Le bloc jouable de la trousse d'usine. Aucun code.", None),
        ("Chaussures — le bloc A", "modules-autonomes/chaussure-blocA/",
         "« Un instant, s'il vous plaît » : le premier bloc de la vente de "
         "chaussures. Aucun code.", None),
    ]),
    ("Portfolio", [
        ("SimDEA — la formation au défibrillateur", "assets/presentations/formation-dea-v5.html",
         "La version 5 : quarante diapositives, la simulation « Vous. » en "
         "encart, et le simulateur au bout.", None),
        ("« Vous. » — la simulation seule", "assets/presentations/simdea-vous-anime-v5.html",
         "La pièce jouée, telle qu'elle est dans la formation v5.", None),
        ("SimDEA — le simulateur seul", "assets/presentations/simulateur-dea.html",
         "Le dispositif jouable, hors de la formation.", None),
        ("Avant l'ouverture — la formation pour barista",
         "assets/presentations/atelier-prototypes/banc-de-panne/tournee.html",
         "La bonne version : elle commence par la tournée de la machine, puis "
         "mène au jeu « Trouver la panne ».", None),
        ("Le courriel de trop", "assets/presentations/courriel-de-trop/le-courriel-de-trop.html",
         "Reconnaître un courriel d'hameçonnage.", None),
        ("À la main d'abord", "assets/presentations/a-la-main-dabord/a-la-main-dabord.html",
         "Remplacer les bougies d'allumage.", None),
        ("Le dernier millimètre", "assets/presentations/le-dernier-millimetre/le-dernier-millimetre.html",
         "Remplacer les plaquettes de frein avant.", None),
        ("La boucle diagnostic — la version qui se joue", "assets/presentations/boucle-animee.html",
         "La pièce maîtresse du portfolio, en mouvement.", None),
        ("L'atelier des prototypes", "assets/presentations/atelier-prototypes/index.html",
         "Les prototypes 01 à 05, chacun jouable depuis le dossier.", None),
        ("Le CV animé", "assets/presentations/cv/daniel-tousignant-cv.html",
         "Daniel Tousignant, concepteur pédagogique.", None),
    ]),
]

DEBUT, FIN = "<!--<<APPLICATIONS>>-->", "<!--<</APPLICATIONS>>-->"


def date_de(chemin):
    """Le dernier commit qui a touché la page servie (ou son dossier)."""
    cible = RACINE / chemin
    if not cible.exists():
        raise SystemExit("%s : introuvable — rien n'est écrit." % chemin)
    iso = subprocess.run(["git", "log", "-1", "--format=%ad", "--date=short", "--", chemin],
                         cwd=RACINE, capture_output=True, text=True).stdout.strip()
    if not iso:
        raise SystemExit("%s : aucun commit — la page n'est pas publiée." % chemin)
    a, m, j = (int(x) for x in iso.split("-"))
    return "%d%s %s %d" % (j, "er" if j == 1 else "", MOIS[m - 1], a)


def codes(cle):
    if cle == "compostelle":
        return [(c, e) for c, e in pelerins.CODES_ESSAI.items()]
    return [(c, e) for c, (e, t) in pelerins.CODES_ESSAI_TROUSSES.items() if t == cle]


def quand(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return "%d%s %s %d" % (j, "er" if j == 1 else "", MOIS[m - 1], a)


def bloc():
    e = html.escape
    fin = quand(pelerins.ESSAI_FIN)
    n = pelerins.ESSAI_CONVERSATIONS
    h = ['<section class="applis" id="vueApplis" hidden aria-label="Les applications, dernière version">',
         '      <div class="tete">',
         '        <span class="eyebrow e-teal">Un lien par application</span>',
         '        <h2>Applications</h2>',
         '        <p>La dernière version de chaque application, prête à envoyer. La date '
         'est celle du dernier changement de la page. Quand une application s\'ouvre '
         'par un code, les codes d\'essai sont dessous : chacun donne %d conversations '
         'jusqu\'au %s.</p>' % (n, fin),
         '      </div>']
    for etagere, apps in APPLICATIONS:
        h += ['      <div class="ap-groupe">',
              '        <h3 class="ch-titre">%s</h3>' % e(etagere),
              '        <div class="ap-liste">']
        for nom, chemin, quoi, cle in apps:
            lien = "/" + chemin
            h += ['          <article class="ap" data-chemin="%s">' % e(lien),
                  '            <div class="ap-tete">',
                  '              <h4 class="ap-nom"><a href="%s" target="_blank" rel="noopener">%s</a></h4>'
                  % (e(chemin), e(nom)),
                  '              <span class="ap-date">%s</span>' % date_de(chemin),
                  '            </div>',
                  '            <p class="ap-quoi">%s</p>' % e(quoi),
                  '            <div class="ap-actions">',
                  '              <a class="btn" href="%s" target="_blank" rel="noopener">Ouvrir</a>' % e(chemin),
                  '              <button type="button" class="ap-copier" data-copier="lien">Copier le lien</button>',
                  '              <code class="ap-url"></code>',
                  '            </div>']
            if cle:
                cs = codes(cle)
                if not cs:
                    raise SystemExit("%s : aucun code d'essai dans pelerins.py." % nom)
                h += ['            <details class="ap-codes">',
                      '              <summary>%d codes d\'essai</summary>' % len(cs),
                      '              <p class="ap-note">Un code par personne : il se consomme. '
                      '« Copier pour envoyer » met le lien et le code ensemble, prêts à coller '
                      'dans un courriel ou un texto.</p>',
                      '              <ul>']
                h += ['                <li><code>%s</code><span>%s</span>'
                      '<button type="button" class="ap-copier" data-copier="envoi" data-code="%s">'
                      'Copier pour envoyer</button></li>' % (c, e(etiq), c) for c, etiq in cs]
                h += ['              </ul>',
                      '              <button type="button" class="ap-copier" data-copier="tous">'
                      'Copier les %d codes</button>' % len(cs),
                      '            </details>']
            h.append('          </article>')
        h += ['        </div>', '      </div>']
    h.append('    </section>')
    return "\n".join(h)


def main(argv):
    neuf = bloc()
    if "--essai" in argv:
        for etagere, apps in APPLICATIONS:
            print(etagere)
            for nom, chemin, _, cle in apps:
                print("  %-48s %-18s %s" % (nom[:48], date_de(chemin),
                                           "%d codes" % len(codes(cle)) if cle else ""))
        return 0
    s = PAGE.read_text(encoding="utf-8")
    if DEBUT not in s or FIN not in s:
        raise SystemExit("marqueurs APPLICATIONS absents — rien n'est écrit.")
    i, j = s.index(DEBUT) + len(DEBUT), s.index(FIN)
    s = s[:i] + "\n    " + neuf + "\n    " + s[j:]
    PAGE.write_text(s, encoding="utf-8")
    print("  %d applications posées" % sum(len(a) for _, a in APPLICATIONS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
