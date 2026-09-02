#!/usr/bin/env python3
"""Les politiques de confidentialité de francis — une source, quatre sorties.

Un centre ne configure pas la plateforme comme un autre, et une politique qui
décrit des flux qui n'ont pas lieu chez lui est **fausse** — dans un sens comme
dans l'autre. Un centre en mode « sans assistance » ne doit pas publier une page
qui annonce des envois aux États-Unis ; un centre en mode complet ne doit pas
publier une page qui les tait.

D'où trois variantes. Et d'où ce script : trois fichiers de quatre-vingt-dix
pour cent identiques, écrits à la main, divergeraient à la première correction.
Le texte commun n'existe donc qu'ici, et les variantes ne sont que des
**différences déclarées** :

    python3 build/politiques.py            # écrit les quatre fichiers
    python3 build/politiques.py --verifier # compare sans écrire, code 1 sur écart

Les quatre sorties :

    confidentialite.html                             la page publiée (mode complet)
    assets/presentations/politique-complet.html      la même, pour le classeur
    assets/presentations/politique-sans-ia.html
    assets/presentations/politique-seance.html

`confidentialite.html` et `politique-complet.html` ont le même corps : la
première est celle que lisent les élèves, la seconde celle qu'on remet à une
direction. Les garder identiques est le rôle du script.
"""

import argparse
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
MAJ = "2 septembre 2026"

# ── Ce qui change d'un mode à l'autre ────────────────────────────────────
#
# Un mode se décrit par ce qu'il RETIRE, jamais par un texte complet à lui :
# une variante qui réécrirait tout le document annulerait l'intérêt d'avoir
# une source unique.

MODES = {
    "complet": {
        "nom": "Mode complet",
        "fichier": "politique-complet.html",
        "resume": "avec l'assistance automatisée, le micro et le dépôt des productions",
        "compte": True,        # l'élève a un code et un surnom durables
        "assistance": True,    # les textes partent au correcteur
        "oral": True,          # les enregistrements sont conservés
        "duree": True,         # il y a une durée de conservation à annoncer
    },
    "sans-ia": {
        "nom": "Mode sans assistance",
        "fichier": "politique-sans-ia.html",
        "resume": "sans aucune assistance automatisée : aucun texte d'élève ne quitte le serveur",
        "compte": True,
        "assistance": False,
        "oral": True,
        "duree": True,
    },
    "seance": {
        "nom": "Mode séance sans compte",
        "fichier": "politique-seance.html",
        "resume": "sans compte, sans nom, sans surnom : la séance expire le soir même",
        "compte": False,
        "assistance": False,
        "oral": False,
        "duree": False,
    },
}


def resume(m):
    """Le « En bref ». C'est ce que la plupart des gens liront en entier."""
    lignes = []
    if m["compte"]:
        lignes += [
            "<b>Nous ne demandons pas votre nom.</b> Vous entrez avec un code. Votre "
            "enseignant vous donne un surnom, comme « Épinette ».",
        ]
    else:
        lignes += [
            "<b>Vous n'avez pas de compte.</b> Vous entrez avec le code de la séance, "
            "et vous apparaissez comme « Participant 3 ». <b>Rien n'est rattaché à "
            "vous.</b>",
        ]
    lignes += [
        "<b>Nous ne demandons pas votre courriel</b>, ni votre téléphone, ni votre "
        "adresse, ni votre date de naissance.",
    ]
    if m["compte"]:
        lignes += ["<b>Nous gardons votre travail</b> : les exercices que vous faites, "
                   "vos réponses" + (", vos textes, et parfois votre voix." if m["oral"]
                                     else " et vos textes.")]
        lignes += ["<b>Votre enseignant voit votre travail.</b> C'est fait pour ça : il "
                   "vous aide à progresser."]
    else:
        lignes += ["<b>Ce que vous répondez sert à la classe</b>, pendant la séance. "
                   "Votre enseignant voit les réponses de « Participant 3 », sans savoir "
                   "que c'est vous."]
    if m["assistance"]:
        lignes += ["<b>Certains outils envoient votre texte à l'extérieur du Québec</b> "
                   "pour le corriger. Votre centre peut fermer ces outils."]
    else:
        lignes += ["<b>Vos textes ne sortent pas d'ici.</b> Votre centre a fermé les "
                   "outils de correction automatique."]
    lignes += ["<b>Nous ne vendons rien à personne.</b> Aucune publicité, aucun traceur."]
    return "\n".join("      <li>%s</li>" % x for x in lignes)


def recueil(m):
    """Le tableau « ce que nous recueillons »."""
    r = []
    if m["compte"]:
        r += [("Un <b>code</b> et un <b>surnom</b>", "Pour vous reconnaître d'une fois à l'autre"),
              ("Votre <b>groupe</b>", "Pour montrer les bonnes activités")]
    else:
        r += [("Un <b>numéro de participant</b>, valable le temps de la séance",
               "Pour que vos réponses ne se mêlent pas à celles des autres")]
    r += [("Les <b>exercices faits</b>, les réponses, les scores, l'heure",
           "Pour suivre votre progression" if m["compte"]
           else "Pour que l'enseignant voie où en est la classe")]
    if m["compte"]:
        r += [("Les <b>textes</b> que vous écrivez"
               + (" et la correction reçue" if m["assistance"] else ""),
               "Pour que votre enseignant les lise et vous réponde")]
    if m["oral"] and m["compte"]:
        r += [("Les <b>enregistrements de votre voix</b>, si vous en envoyez",
               "Pour que votre enseignant écoute et vous réponde")]
    return "\n".join(
        "      <tr><td>%s</td>\n          <td>%s</td></tr>" % (a, b) for a, b in r)


def pas_recueilli(m):
    sup = ""
    if not m["compte"]:
        sup = (" Dans ce mode, il n'y a même <b>aucun surnom</b> : vous êtes un numéro, "
               "et ce numéro disparaît avec la séance.")
    if not m["oral"] and m["compte"]:
        sup = " Aucun <b>enregistrement de voix</b> n'est conservé dans ce mode."
    if not m["oral"] and not m["compte"]:
        sup += (" Vous pouvez vous enregistrer et vous réécouter pour vous exercer&nbsp;: "
                "<b>ce son ne quitte jamais votre appareil</b>.")
    return sup


def qui_voit(m):
    if m["compte"]:
        return ("    <li><b>Votre enseignant</b> voit le travail de son groupe.</li>\n"
                "    <li><b>La direction de votre centre</b> voit des chiffres "
                "d'ensemble : combien d'élèves travaillent, combien de temps. Elle ne "
                "lit pas vos textes.</li>\n"
                "    <li><b>Personne d'autre.</b> Nous ne vendons, ne louons et ne "
                "communiquons vos renseignements à personne.</li>")
    return ("    <li><b>Votre enseignant</b> voit les réponses de la séance, par "
            "numéro de participant.</li>\n"
            "    <li><b>La direction de votre centre</b> voit des chiffres "
            "d'ensemble, jamais le détail d'une personne.</li>\n"
            "    <li><b>Personne d'autre.</b> Nous ne vendons, ne louons et ne "
            "communiquons rien à personne.</li>")


def frontiere(m):
    """Ce qui sort du Québec. La section qui change le plus d'un mode à l'autre."""
    if m["assistance"]:
        rangs = [
            ("Correction de vos phrases et de vos textes, jeu de rôle, aide à la "
             "traduction", "Le texte que vous avez écrit", "États-Unis"),
            ("Le micro, quand vous parlez dans un exercice", "Votre voix",
             "Chez l'éditeur de votre navigateur (Google, Apple)"),
            ("Lecture des textes à voix haute" + (", transcription d'un enregistrement"
                                                  if m["oral"] else ""),
             "Le texte du module" + ("&nbsp;; votre enregistrement s'il y a lieu"
                                     if m["oral"] else ""),
             "Toronto, au Canada"),
        ]
        intro = ("<p>Certains outils fonctionnent grâce à des services situés à "
                 "l'extérieur du Québec. Voici lesquels, et ce qu'ils reçoivent.</p>")
        fin = ("<p><b>Votre centre peut fermer ces outils.</b> S'il le fait, la "
               "plateforme continue de fonctionner et vos textes ne sortent plus. "
               "Demandez à votre enseignant ce qui est activé chez vous.</p>")
    else:
        rangs = [
            ("Le micro, quand vous parlez dans un exercice", "Votre voix",
             "Chez l'éditeur de votre navigateur (Google, Apple)"),
            ("Lecture des textes à voix haute", "Le texte du module — <b>aucune donnée "
             "vous concernant</b>", "Toronto, au Canada"),
        ]
        intro = ("<p><b>Votre centre a fermé l'assistance automatisée.</b> Aucun de vos "
                 "textes, aucune de vos réponses ne quitte le serveur. Il reste deux "
                 "choses, et elles ne dépendent pas de nous.</p>")
        fin = ("<p>Le micro dépend du <b>navigateur</b> que vous utilisez, pas de la "
               "plateforme : c'est lui qui envoie le son. <b>Votre centre peut aussi "
               "fermer le micro</b> — demandez à votre enseignant.</p>")
    corps = "\n".join(
        "      <tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in rangs)
    return intro, corps, fin


def conservation(m):
    if not m["duree"]:
        return ("""  <p><b>La séance expire le soir même.</b> Votre numéro de participant
  n'existe plus le lendemain, et rien ne permet de relier vos réponses à vous.</p>
  <p>Votre enseignant garde ce que la classe a répondu, par numéro, pour préparer son
  cours suivant.</p>""")
    return ("""  <p><b>Trente jours.</b> Passé ce délai, ce que vous avez produit est effacé
  automatiquement&nbsp;:</p>
  <ul>
    %s
    <li>vos <b>textes</b> et la correction que vous avez reçue ;</li>
    <li>les <b>analyses de vos erreurs</b>.</li>
  </ul>
  <p>Ce qui reste, parce qu'il ne dit rien de personnel&nbsp;: votre <b>avancement</b>
  dans les modules, le nombre d'exercices faits, et vos listes de vocabulaire. Sans
  cela, vous perdriez votre progression chaque mois.</p>
  <p class="cf-maj">Conséquence à connaître&nbsp;: un texte%s de plus de trente jours
  <b>ne peut plus être relu</b>, ni par vous, ni par votre enseignant. Pensez à
  télécharger ce que vous voulez garder.</p>""" % (
        "<li>vos <b>enregistrements de voix</b> — le fichier son lui-même ;</li>"
        if m["oral"] else "",
        " ou un enregistrement" if m["oral"] else ""))


def droits(m):
    if m["compte"]:
        return ("""  <p>Vous pouvez, en tout temps :</p>
  <ul>
    <li><b>Demander ce que nous savons de vous</b> et en recevoir une copie.</li>
    <li><b>Faire corriger</b> un renseignement inexact.</li>
    <li><b>Demander l'effacement</b> de vos productions.</li>
    <li><b>Retirer votre accord</b> pour les outils qui envoient du texte à
        l'extérieur.</li>
    <li><b>Porter plainte</b> à la Commission d'accès à l'information du Québec si vous
        n'êtes pas satisfait de notre réponse.</li>
  </ul>

  <p>Écrivez au responsable indiqué plus haut, ou parlez-en à votre enseignant, qui
  transmettra. Nous répondons dans les meilleurs délais.</p>""")
    return ("""  <p>Dans ce mode, <b>rien n'est rattaché à votre identité</b> : il n'y a donc
  rien à vous montrer, à corriger ou à effacer. C'est le point de ce mode.</p>
  <p>Si vous voulez que vos réponses de la séance soient retirées, dites-le à votre
  enseignant pendant le cours&nbsp;: lui seul sait quel numéro est le vôtre, et il peut
  fermer la séance. Vous pouvez aussi <b>porter plainte</b> à la Commission d'accès à
  l'information du Québec.</p>""")


# ── Le gabarit commun ────────────────────────────────────────────────────

GABARIT = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>%(titre)s</title>
  <link rel="stylesheet" href="%(base)sassets/design-system/styles.css" />
  <link rel="stylesheet" href="%(base)sassets/design-system/marque-francis.css" />
  <link rel="icon" type="image/svg+xml" href="%(base)sassets/design-system/marque-francis-favicon.svg" />
  <style>
    /* PRODUIT PAR build/politiques.py — ne pas modifier à la main.
       Toute correction se fait dans le script, puis on régénère les quatre.

       Deux publics dans une seule page : un élève de niveau 4 doit pouvoir la
       lire, un service juridique doit y trouver ce qu'il cherche. D'où le
       résumé en tête, en phrases courtes, et le détail en dessous.

       Aucune couleur en dur : uniquement des jetons du système de design. */
    body { margin: 0; background: var(--surface-page); }
    .cf-page { max-width: 46rem; margin: 0 auto;
      padding: var(--sp-6) var(--sp-4) var(--sp-12); }
    .cf-titre { margin: 0 0 var(--sp-2); }
    .cf-maj { color: var(--text-muted); font-size: var(--fs-ui-sm);
      margin: 0 0 var(--sp-6); }
    .cf-mode { display: inline-block; font-size: var(--fs-meta);
      font-weight: var(--fw-black); text-transform: uppercase;
      letter-spacing: .07em; color: var(--text-muted);
      border: 1px solid var(--border); border-radius: 99px;
      padding: .15em .7em; margin-bottom: var(--sp-3); }
    .cf-resume { background: var(--surface-card); border: 1px solid var(--border);
      border-radius: var(--r-lg); padding: var(--sp-4) var(--sp-5);
      margin-bottom: var(--sp-8); }
    .cf-resume h2 { margin-top: 0; }
    .cf-resume ul { margin: 0; padding-left: 1.2rem; }
    .cf-resume li { margin: var(--sp-2) 0; }
    .cf-page h2 { margin: var(--sp-8) 0 var(--sp-2); }
    .cf-page h3 { margin: var(--sp-5) 0 var(--sp-1); font-size: var(--fs-ui); }
    .cf-page p, .cf-page li { line-height: 1.65; }
    .cf-page ul, .cf-page ol { padding-left: 1.2rem; }
    .cf-tab { width: 100%%; border-collapse: collapse; margin: var(--sp-3) 0;
      font-size: var(--fs-ui-sm); }
    .cf-tab th, .cf-tab td { text-align: left; vertical-align: top;
      padding: var(--sp-2); border-bottom: 1px solid var(--border); }
    .cf-tab th { font-size: var(--fs-meta); text-transform: uppercase;
      letter-spacing: .06em; color: var(--text-muted);
      font-weight: var(--fw-black); }
    .cf-enveloppe { overflow-x: auto; }
    /* Ce qui reste à remplir se voit, plutôt que de se lire comme un fait. */
    .cf-aremplir { background: var(--ambre-100);
      border: 1px solid var(--ambre-700);
      border-left-width: 4px; border-radius: var(--r-md);
      padding: var(--sp-3) var(--sp-4); margin: var(--sp-4) 0; }
    .cf-aremplir p { margin: var(--sp-1) 0; }
    .cf-trou { font-weight: var(--fw-black); color: var(--ambre-700);
      border-bottom: 1px solid currentColor; }
    .cf-contact { background: var(--surface-card); border: 1px solid var(--border);
      border-radius: var(--r-lg); padding: var(--sp-4) var(--sp-5);
      margin: var(--sp-4) 0; }
    .cf-pied { margin-top: var(--sp-12); padding-top: var(--sp-4);
      border-top: 1px solid var(--border); color: var(--text-muted);
      font-size: var(--fs-ui-sm); }
    .cf-retour { display: inline-block; margin-bottom: var(--sp-5);
      font-size: var(--fs-ui-sm); font-weight: var(--fw-bold);
      color: var(--text-muted); text-decoration: none; }
    .cf-retour:hover { color: var(--text); }
    @media print {
      .fr-barre, .cf-retour { display: none; }
      .cf-page { max-width: none; padding: 0; }
    }
  </style>
</head>
<body>

<div class="fr-barre">
  <div class="fr-barre__in">
    <span class="fr-lockup">
      <span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span>
      <span class="fr-trait" aria-hidden="true"></span>
      <span class="fr-desc">Aide à l'apprentissage du français</span>
    </span>
  </div>
</div>

<main class="cf-page">
%(retour)s
%(bandeau)s
  <h1 class="cf-titre">Protection de vos renseignements personnels</h1>
  <p class="cf-maj">Mise à jour : %(maj)s</p>

  <section class="cf-resume">
    <h2>En bref</h2>
    <ul>
%(resume)s
    </ul>
  </section>

  <h2>1. Qui est responsable</h2>

  <p>La plateforme <b>francis</b> est fournie à votre centre de formation. Votre centre
  décide de ce qui est recueilli et de ce qui est conservé ; nous agissons pour son
  compte.</p>

  <div class="cf-contact">
    <p><b>Responsable de la protection des renseignements personnels</b></p>
    <p><b>Daniel Tousignant</b><br>
       Responsable de la plateforme francis<br>
       <a href="mailto:confidentialite@edufrancis.ca">confidentialite@edufrancis.ca</a></p>
    <p>Vous pouvez écrire à cette personne pour toute question sur vos renseignements,
    pour y accéder, les corriger ou les faire effacer. Vous pouvez aussi passer par
    votre enseignant, qui transmettra.</p>
  </div>

  <h2>2. Ce que nous recueillons</h2>

  <div class="cf-enveloppe">
  <table class="cf-tab">
    <thead><tr><th>Ce que c'est</th><th>Pourquoi</th></tr></thead>
    <tbody>
%(recueil)s
    </tbody>
  </table>
  </div>

  <h3>Ce que nous ne recueillons pas</h3>
  <p>Ni votre <b>vrai nom</b>, ni votre <b>courriel</b>, ni votre <b>téléphone</b>, ni
  votre <b>adresse</b>, ni votre <b>date de naissance</b>, ni rien sur votre statut
  d'immigration ou votre santé. Aucun de ces renseignements n'a de case dans notre
  système.%(pas_recueilli)s</p>

  <h3>Attention à ce que vous écrivez</h3>
  <p>Quand vous écrivez un texte libre, écrivez seulement ce qui est demandé.
  <b>N'écrivez pas votre nom, votre adresse, votre numéro de téléphone ni rien de
  personnel</b> — ni sur vous, ni sur quelqu'un d'autre.</p>

  <h2>3. Qui voit vos renseignements</h2>

  <ul>
%(qui_voit)s
  </ul>

  <h2>4. Ce qui sort du Québec</h2>

  %(front_intro)s

  <div class="cf-enveloppe">
  <table class="cf-tab">
    <thead><tr><th>Outil</th><th>Ce qui est envoyé</th><th>Où</th></tr></thead>
    <tbody>
%(front_corps)s
    </tbody>
  </table>
  </div>

  %(front_fin)s

  <p class="cf-maj">Ces services sont tenus, par leur contrat, de ne pas utiliser ce
  qu'ils reçoivent pour autre chose que de rendre le service demandé — notamment pas
  pour entraîner leurs modèles.</p>

  <h2>5. Combien de temps nous gardons vos renseignements</h2>

%(conservation)s

  <h2>6. Vos droits</h2>

%(droits)s

  <h2>7. Décisions automatisées</h2>

  <p><b>Aucune décision vous concernant n'est prise automatiquement.</b> La plateforme
  %(decision)s, mais elle ne vous donne aucune note officielle, ne décide d'aucun
  classement et ne décide d'aucun parcours. C'est votre enseignant qui décide.</p>

  <h2>8. Sécurité</h2>

  <ul>
    <li>Les échanges avec le site sont <b>chiffrés</b>.</li>
    <li>Les mots de passe du personnel sont conservés sous une forme <b>impossible à
        relire</b>.</li>
    <li>Chaque personne ne voit que ce qui la concerne : un enseignant, ses groupes ;
        une direction, son centre.</li>
    <li>Les gestes d'administration sont <b>consignés</b> avec leur auteur et leur
        date.</li>
    <li>Il n'y a <b>aucun traceur publicitaire</b> et aucun outil de mesure d'audience
        d'un tiers.</li>
  </ul>

  <h3>S'il arrive un incident</h3>
  <p>Si des renseignements étaient perdus ou consultés sans autorisation, nous
  tenons un registre de l'incident, nous avertissons votre centre sans délai, et les
  personnes concernées sont informées lorsque la loi l'exige.</p>

  <h2>9. Changements à cette page</h2>

  <p>Nous pouvons modifier cette page. La date de mise à jour, en haut, dit quand. Un
  changement important vous sera signalé dans la plateforme.</p>

%(fin)s

  <p class="cf-pied">Cette page est rédigée en langue simple pour être lue par les
  personnes qui apprennent le français. Une version détaillée du dossier technique
  existe pour les directions et leurs conseillers juridiques ; demandez-la au
  responsable indiqué plus haut.</p>

</main>
</body>
</html>
"""

BANDEAU = """  <span class="cf-mode">%(nom)s</span>
"""

AVERT_CLASSEUR = """  <div class="cf-aremplir">
    <p><b>Ce texte est la variante « %(nom)s ».</b> Il décrit la plateforme telle
    qu'elle fonctionne <b>%(resume)s</b>. Un centre publie la variante qui
    correspond à sa configuration — les trois autres décriraient des flux qui
    n'ont pas lieu chez lui, ou tairaient ceux qui ont lieu.</p>
    <p><b>Produit par <code>build/politiques.py</code></b>, jamais écrit à la main :
    les trois variantes partagent leur texte commun et ne peuvent pas diverger.</p>
  </div>
"""

FIN_PUBLIEE = ""

RETOUR = ('  <a class="cf-retour" href="/presentations.html">'
          '<span aria-hidden="true">&#8592;</span> Le classeur</a>\n')


def rendre(cle, pour_classeur):
    m = MODES[cle]
    intro, corps, fin_front = frontiere(m)
    return GABARIT % {
        "titre": ("Protection des renseignements personnels — francis"
                  if not pour_classeur
                  else "Politique de confidentialité — %s" % m["nom"]),
        "base": "" if not pour_classeur else "../../",
        "retour": RETOUR if pour_classeur else "",
        "bandeau": (BANDEAU % m) + (AVERT_CLASSEUR % m) if pour_classeur else "",
        "maj": MAJ,
        "resume": resume(m),
        "recueil": recueil(m),
        "pas_recueilli": pas_recueilli(m),
        "qui_voit": qui_voit(m),
        "front_intro": intro,
        "front_corps": corps,
        "front_fin": fin_front,
        "conservation": conservation(m),
        "droits": droits(m),
        "decision": ("corrige vos phrases et vous propose des exercices"
                     if m["assistance"] else "corrige vos exercices"),
        "fin": FIN_PUBLIEE if not pour_classeur else "",
    }


def sorties():
    """(chemin, contenu) pour les quatre fichiers."""
    yield RACINE / "confidentialite.html", rendre("complet", False)
    for cle, m in MODES.items():
        yield (RACINE / "assets" / "presentations" / m["fichier"],
               rendre(cle, True))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--verifier", action="store_true",
                    help="compare sans écrire ; sort en 1 au premier écart")
    a = ap.parse_args()
    ecarts = 0
    for chemin, contenu in sorties():
        rel = chemin.relative_to(RACINE)
        if a.verifier:
            actuel = chemin.read_text(encoding="utf-8") if chemin.exists() else None
            if actuel != contenu:
                print("écart : %s" % rel)
                ecarts += 1
            continue
        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_text(contenu, encoding="utf-8")
        print("→ %s (%d octets)" % (rel, len(contenu.encode())))
    if a.verifier:
        print("%d écart(s)" % ecarts)
        return 1 if ecarts else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
