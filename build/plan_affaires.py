#!/usr/bin/env python3
"""Le plan d'affaires et la stratégie de communication — deux pages, une source.

    python3 build/plan_affaires.py              # les deux pages
    python3 build/plan_affaires.py --plan       # le plan seul
    python3 build/plan_affaires.py --com        # la stratégie seule
    python3 build/plan_affaires.py --texte      # les chiffres, sans rien écrire

Sorties : assets/presentations/plan-affaires.html
          assets/presentations/strategie-communication.html

**Un seul script pour les deux pages**, parce qu'elles citent le même
inventaire. Deux scripts finiraient par annoncer deux nombres de modules, et
ce dépôt sait ce que « deux sources pour une idée » finit par coûter.

**Les chiffres sont comptés sur le disque, jamais recopiés.** C'est la règle
de la trousse et du point express, et elle vaut doublement ici : un plan
d'affaires dont les chiffres vieillissent est pire qu'un plan sans chiffres,
parce qu'on le montre à quelqu'un qui, lui, va vérifier.

**Trois choses ne sont pas dans ces pages, et c'est délibéré :**

  · **aucun prix**. Il se décide, il se négocie, il dépend du nombre de
    groupes. Le plan donne les leviers du prix, pas un montant.
  · **aucune taille de marché**. On ne la connaît pas. Un nombre inventé
    dans un plan d'affaires est repéré par la première personne du métier
    qui le lit, et il emporte le reste de la crédibilité avec lui.
  · **aucun rendement promis**. Le dépliant l'écrit déjà : on mesure une
    tendance, on ne prouve pas une cause.

Les cases à remplir par une personne — nom, coordonnées, tarifs — sont
laissées entre crochets et signalées à l'écran à chaque exécution.
"""
import argparse
import json
import pathlib
import re
import subprocess
import time

RACINE = pathlib.Path(__file__).resolve().parent.parent
PRES = RACINE / 'assets' / 'presentations'
MODELE = PRES / 'programme-belrive.html'      # la famille partage un seul habillage
PLAN = PRES / 'plan-affaires.html'
COM = PRES / 'strategie-communication.html'

MOIS = {"January": "janvier", "February": "février", "March": "mars",
        "April": "avril", "May": "mai", "June": "juin", "July": "juillet",
        "August": "août", "September": "septembre", "October": "octobre",
        "November": "novembre", "December": "décembre"}


def nb(v):
    """Un nombre lisible : 21 416 plutôt que 21416."""
    return "{:,}".format(v).replace(",", " ") if isinstance(v, int) else str(v)


def mesures():
    """Ce que les deux pages affichent, relevé sur le disque."""
    m = {}
    quand = time.strftime("%-d %B %Y")
    for en, fr in MOIS.items():
        quand = quand.replace(en, fr)
    m["quand"] = quand

    inter = RACINE / 'assets' / 'interactive'
    m["modules"] = len([d for d in inter.iterdir()
                        if d.is_dir() and d.name.startswith('module-')])
    m["mp3"] = len(list(inter.rglob('*.mp3')))
    m["images"] = len(list(inter.rglob('*.jpg'))) + len(list(inter.rglob('*.png')))
    m["pptx"] = len(list((RACINE / 'assets' / 'powerpoints').rglob('*.pptx')))
    m["fiches"] = len(list((RACINE / 'assets' / 'documents').glob('*fiches-eleves.html')))

    act = json.loads((RACINE / 'data' / 'activities.json').read_text(encoding='utf-8'))
    m["activites"] = len(act)
    m["cours"] = sum(1 for a in act if a.get('categorie') == 'cours')
    m["ateliers"] = m["activites"] - m["cours"]

    m["express"] = len(json.loads(
        (RACINE / 'data' / 'points_express.json').read_text(encoding='utf-8')))

    voc = (RACINE / 'build' / 'gabarit' / 'vocab.js').read_text(encoding='utf-8')
    m["langues"] = len(re.findall(r"\{c:'", voc))

    # Les situations du programme couvertes, niveau par niveau : c'est le
    # chiffre qui dit « le programme est fait », et il vient du registre des
    # modules, pas d'un compte à la main.
    import sys
    sys.path.insert(0, str(RACINE / 'build'))
    try:
        from powerpoints.modules import MODULES
        niveaux = {}
        for slug, d in MODULES.items():
            niveaux.setdefault(d.get('niveau'), []).append(slug)
        m["niveaux"] = len([k for k in niveaux if k])
        m["par_niveau"] = {k: len(v) for k, v in sorted(niveaux.items()) if k}
    except Exception:
        m["niveaux"] = 8
        m["par_niveau"] = {}

    m["banque"] = len(list(PRES.glob('*.html')))
    return m


def entete(titre, resume):
    """L'habillage de la famille, pris sur la page modèle plutôt que recopié."""
    if not MODELE.exists():
        raise SystemExit('page modèle absente : %s' % MODELE)
    tete = MODELE.read_text(encoding='utf-8').split('</head>')[0] + '</head>\n'
    tete = re.sub(r'<title>.*?</title>', '<title>%s</title>' % titre, tete, count=1)
    tete = tete.replace("""   HUIT HEURES CHEZ BELRIVE
   Le programme de démonstration : une usine fictive de
   transformation alimentaire, huit blocs d'une heure.""", '   ' + resume)
    return tete


# ═══════════════════════════════════════════════════════════════════════
#  LE PLAN D'AFFAIRES
# ═══════════════════════════════════════════════════════════════════════

def page_plan(m):
    return entete("Plan d'affaires",
                  "PLAN D'AFFAIRES\n   L'actif compté, deux marchés, trois choses "
                  "qui distinguent,\n   et ce que le plan refuse de chiffrer.") + """<body>
<div class="doc">

<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Chantier &mdash; formation en entreprise</p>
<h1>Plan d'affaires</h1>
<p class="chapeau">La plupart des gens qui veulent vendre de la formation ont un plan.
<strong>Vous avez un inventaire.</strong> %(activites)s activités en service, %(pptx)s séances
projetables, %(mp3)s extraits sonores, les huit niveaux du programme couverts &mdash; produits par
une personne. Ce plan part de là, parce que c'est la seule chose qu'un acheteur peut vérifier
lui-même.</p>
<div class="avert">
  <p><strong>Révisé le 31 août 2026, après la recherche de marché.</strong> La première version de
  ce plan visait l'employeur. <a href="analyse-marche.html">Le relevé du marché</a> a montré que
  depuis le 1<sup>er</sup> juillet 2026, la francisation en milieu de travail est livrée
  <strong>gratuitement</strong> par 32 partenaires publics mandatés. Le chapitre des marchés a donc
  été refait&nbsp;: <strong>le client principal n'est pas l'entreprise, c'est le réseau qui la
  sert.</strong> Le reste du plan &mdash; l'actif, les trois différenciateurs, les risques &mdash;
  tenait et n'a pas bougé.</p>
</div>

<section class="premier">
  <h2>1. L'actif, compté</h2>
  <p>Aucun de ces nombres n'est écrit à la main&nbsp;: ils sont relevés sur le disque à chaque
  production de cette page. C'est la seule façon qu'ils soient encore vrais le mois prochain.</p>
  <div class="mes">
    <div><b>%(activites)s</b><span>activités au catalogue &mdash; %(cours)s cours, %(ateliers)s ateliers</span></div>
    <div><b>%(modules)s</b><span>modules interactifs, huit niveaux</span></div>
    <div><b>%(pptx)s</b><span>séances en diaporama, prêtes à projeter</span></div>
    <div><b>%(fiches)s</b><span>sommaires de fiches élèves imprimables</span></div>
    <div><b>%(mp3)s</b><span>extraits sonores enregistrés</span></div>
    <div><b>%(images)s</b><span>images produites pour les exercices</span></div>
    <div><b>%(express)s</b><span>points express de dix minutes</span></div>
    <div><b>%(langues)s</b><span>langues de traduction déjà branchées</span></div>
  </div>
  <div class="these">
    <p class="cle">Ce que ces nombres prouvent n'est pas le catalogue. C'est la chaîne
    qui l'a produit.</p>
    <p>Un catalogue se copie&nbsp;; une chaîne de production, non. Le moteur d'un module est séparé
    de son contenu&nbsp;: écrire un module neuf, c'est écrire sept fichiers de texte, et l'audio,
    les images, les seize séances de diaporama et les fiches à imprimer <strong>se
    fabriquent</strong>. C'est ce qui rend le sur-mesure abordable &mdash; et le sur-mesure est
    exactement ce qu'une entreprise demande.</p>
  </div>
</section>

<section>
  <h2>2. Trois clients, et le principal n'est pas celui qu'on croit</h2>
  <div class="these">
    <p class="cle">On ne vend pas contre la gratuité. On vend à ceux qui la livrent.</p>
    <p>Les 32 partenaires mandatés ont le contrat, l'argent et les groupes. Ce qu'ils n'ont pas,
    c'est le matériel &mdash; et c'est la seule chose que vous ayez en trop.</p>
  </div>
  <div class="roule">
  <table class="cmp">
    <thead><tr><th></th><th>1. Le réseau mandaté <span class="cout">(21 CSS, 11 cégeps)</span></th><th>2. L'entreprise hors programme</th><th>3. L'entreprise servie <em>par</em> un partenaire</th></tr></thead>
    <tbody>
      <tr><td>Ce qu'on vend</td><td>le portail, les %(modules)s modules, la langue d'appui, la production sur mesure</td><td>huit heures sur un métier précis, et le matériel qui reste</td><td>le matériel&nbsp;; c'est le partenaire qui facture la prestation</td></tr>
      <tr><td>Pourquoi il achète</td><td>il doit livrer un service qu'il n'a pas le temps de fabriquer</td><td>la gratuité ne l'atteint pas&nbsp;: 100 salariés et plus, ou pas 40 h à libérer</td><td>il veut son plancher à lui, pas du français général à distance</td></tr>
      <tr><td>Le budget</td><td>public, et déjà attribué au programme</td><td>le sien&nbsp;: formation, SST, intégration</td><td>celui du programme, par son partenaire</td></tr>
      <tr><td>Le cycle</td><td>institutionnel &mdash; mais vous êtes déjà dans ce réseau</td><td>court&nbsp;: une rencontre, une démonstration</td><td>par recommandation du partenaire</td></tr>
      <tr class="f"><td>Verdict</td><td><strong>le client principal</strong></td><td>réel, mais étroit</td><td>la meilleure porte vers l'entreprise</td></tr>
    </tbody>
  </table>
  </div>
  <p><strong>Les trois partagent la totalité de l'outillage</strong> &mdash; le même moteur de
  module, le même audio, le même portail, la même bascule de langue. Ce qui change d'un client à
  l'autre, c'est le scénario et le vocabulaire, jamais la machine.</p>
  <p class="cout">Le renversement tient en une phrase&nbsp;: on ne cherche plus l'employeur qui
  paierait ce que l'État donne. On cherche l'organisme qui doit le donner et qui manque de quoi
  le faire.</p>
</section>

<section>
  <h2>3. Trois choses qui distinguent &mdash; et rien d'autre</h2>
  <p>Une liste de dix avantages ne convainc personne. Voici les trois qu'un concurrent ne peut pas
  recopier en une saison.</p>

  <div class="voie oui">
    <span class="verdict v-oui">Le socle</span>
    <h3>Le diagnostic didactique</h3>
    <p>On ne livre pas un cours&nbsp;: on livre un cours <strong>corrigé par les réponses réelles
    des gens qui l'ont suivi</strong>. Un item raté par la moitié du groupe accuse l'énoncé, pas le
    groupe. Un item réussi par tous occupe une place que rien n'occupe.</p>
    <p>Le portail enregistre déjà ce qu'il faut pour cette boucle&nbsp;: les réponses item par item,
    le temps passé, les abandons, et les demandes d'aide <em>avec le titre de l'exercice qui les a
    provoquées</em>. Ce n'était pas prévu pour ça &mdash; c'était instrumenté pour les enseignants
    &mdash; et c'est devenu le banc d'essai.</p>
    <p class="cout">N'importe qui peut écrire huit heures de contenu. Peu de gens peuvent montrer
    ce que quarante travailleurs ont réellement répondu, et ce qu'ils en ont changé.</p>
  </div>

  <div class="voie oui">
    <span class="verdict v-oui">Ce que personne d'autre ne fait proprement</span>
    <h3>Le multilingue par couches</h3>
    <p>Trois couches, et tout tient à ne pas les confondre. <strong>Le contenu à apprendre ne
    bascule jamais</strong> &mdash; le traduire, c'est supprimer le produit. <strong>La langue
    d'appui bascule</strong>&nbsp;: consignes, explications, rattrapages, boutons, fiche de poche.
    Et la traduction d'un mot à la demande existe déjà, en %(langues)s langues.</p>
    <p>L'appui se pose <strong>sous</strong> le français, jamais à sa place. Ajouter une langue est
    un fichier et une relecture, pas une reprise du cours. Et ce sont des traductions écrites et
    relues d'avance, jamais produites à la volée&nbsp;: une consigne de sécurité mal traduite dans
    une usine n'est pas un défaut d'affichage.</p>
    <p class="cout">C'est la fonction que le marché demande, et celle que les catalogues existants
    règlent le plus mal &mdash; en traduisant tout, donc en supprimant l'apprentissage.</p>
  </div>

  <div class="voie oui">
    <span class="verdict v-oui">Le vrai fossé</span>
    <h3>La chaîne de production</h3>
    <p>Le moteur est séparé du contenu. Un module neuf, ce sont sept fichiers de texte&nbsp;; tout
    le reste se fabrique&nbsp;: l'audio dans quatre voix, les images en format d'exercice, les
    seize séances de diaporama, les fiches imprimables, le découpage en sections datables.</p>
    <p>C'est ce qui permet de dire à un employeur «&nbsp;ce sera <em>votre</em> usine, avec vos
    zones et vos mots&nbsp;» sans que le devis explose. Le sur-mesure est le premier argument de
    vente en entreprise, et celui qui ruine habituellement la marge.</p>
  </div>
</section>

<section>
  <h2>4. Trois lignes de produits</h2>
  <ol class="actions">
    <li><h3>Le portail et son matériel, pour un partenaire du réseau</h3>
      <p>Les %(modules)s modules, la planification par groupe, le suivi, les productions des élèves,
      le mode sans assistance pour une direction qui refuse l'IA, le mode séance sans compte &mdash;
      et la langue d'appui, que rien d'autre n'offre.</p>
      <p class="qui">Revenu récurrent, et le seul qui paie le développement. C'est la ligne
      principale depuis le 31 août 2026.</p></li>
    <li><h3>La production sur mesure</h3>
      <p>Un module à l'image d'un client &mdash; ses machines, ses procédures, ses personnages.
      Vendu au livrable, pas à l'heure. Le commanditaire peut être un partenaire du réseau autant
      qu'une entreprise.</p>
      <p class="qui">Marge la plus élevée, et la seule ligne qui exploite vraiment la chaîne.</p></li>
    <li><h3>La formation en milieu de travail, en direct</h3>
      <p>Huit blocs d'une heure sur les heures payées, précédés d'une demi-journée d'analyse chez le
      client. Pour qui la gratuité n'atteint pas&nbsp;: 100 salariés et plus, ou pas quarante heures
      à libérer.</p>
      <p class="qui">Cycle court, marché étroit. C'est ce qui fait connaître &mdash; et ce qui
      alimente le diagnostic didactique en réponses réelles.</p></li>
  </ol>
</section>

<section>
  <h2>5. Ce qui fait le prix, et ce qui fait le coût</h2>
  <p>Ce plan ne porte aucun montant &mdash; il se décide, il se négocie, il dépend du nombre de
  groupes. Mais les leviers, eux, se nomment.</p>
  <div class="roule">
  <table class="cmp">
    <thead><tr><th>Ce qui fait monter le prix</th><th>Ce qui le fait descendre</th></tr></thead>
    <tbody>
      <tr><td>du sur-mesure réel &mdash; leurs machines, leurs mots</td><td>un programme repris tel quel</td></tr>
      <tr><td>plusieurs quarts, donc plusieurs groupes</td><td>un seul groupe, un seul horaire</td></tr>
      <tr><td>des langues d'appui de plus</td><td>les trois déjà branchées</td></tr>
      <tr><td>la mesure du niveau 3 &mdash; observations avant et après</td><td>s'arrêter à «&nbsp;ils ont aimé&nbsp;»</td></tr>
      <tr><td>l'analyse de plancher, si elle est facturée</td><td>l'analyse offerte, comme argument d'entrée</td></tr>
    </tbody>
  </table>
  </div>
  <div class="avert">
    <p><strong>Le coût dominant n'est pas la technique.</strong> Les médias d'un module se comptent
    en dollars, pas en centaines&nbsp;: une image coûte quelques sous, la synthèse vocale d'un
    corpus entier quelques dizaines de dollars, l'hébergement est marginal. <strong>Le coût, c'est
    le temps de conception</strong> &mdash; écrire un scénario juste, poser les bonnes questions,
    trancher un arbitrage pédagogique. C'est une bonne nouvelle pour la marge et une mauvaise pour
    la capacité&nbsp;: on ne délègue pas ce temps-là facilement.</p>
  </div>
</section>

<section>
  <h2>6. La capacité, et l'endroit où elle casse</h2>
  <p>Le contenu grandit vite&nbsp;: la chaîne y pourvoit. <strong>Les heures d'enseignement, non.</strong>
  Huit blocs pour trois groupes, c'est vingt-quatre heures de présence, et il n'y en a qu'une par
  semaine à vendre.</p>
  <ul class="simple">
    <li><b>Former des formateurs.</b> Le matériel est déjà fait pour ça &mdash; les séances sont
    scénarisées, les fiches existent. C'est la voie la plus naturelle, et la plus lente.</li>
    <li><b>Vendre le portail sans la prestation.</b> Un centre ou une entreprise anime elle-même.
    Marge élevée, mais on perd la boucle du diagnostic didactique, qui est l'atout.</li>
    <li><b>L'autonomie de l'élève.</b> Les points express et la banque d'ateliers se font seuls.
    C'est ce qui permet d'être utile entre deux blocs sans être présent.</li>
  </ul>
  <p class="cout">Ces trois voies ne se choisissent pas maintenant. Elles se nomment maintenant,
  pour que le premier contrat ne ferme aucune des trois.</p>
</section>

<section>
  <h2>7. Les risques, nommés</h2>
  <div class="decisions">
    <div class="dec">
      <div class="ligne"><h3>Une seule personne</h3><span class="badge b-loi">structurel</span></div>
      <p>Tout tient à une tête&nbsp;: la conception, la production, la vente et la prestation. Le
      risque n'est pas l'échec, c'est l'arrêt. La parade n'est pas d'embaucher tout de suite&nbsp;;
      c'est d'écrire ce qui se transmet &mdash; ce que le dépôt fait déjà, méthodiquement.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>Le contenu n'est pas le marché</h3><span class="badge b-dec">à surveiller</span></div>
      <p>%(activites)s activités ne valent rien tant que personne n'a signé. C'est le risque le plus
      probable de tous, et le seul remède est de sortir&nbsp;: des rencontres, pas des modules de
      plus.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>Les données des personnes</h3><span class="badge b-loi">légal</span></div>
      <p>Des réponses d'élèves, des enregistrements de voix, dans l'entreprise qui les emploie. Le
      portail travaille déjà sous pseudonyme, ne conserve pas les corrections privées, et offre un
      mode sans compte&nbsp;; ce qui remonte à un employeur doit rester un constat sur le matériel,
      jamais sur une personne. À écrire noir sur blanc dans chaque contrat.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>La dépendance aux fournisseurs d'IA</h3><span class="badge b-dec">à surveiller</span></div>
      <p>Voix, images, assistance&nbsp;: trois fournisseurs externes, dont les prix et les
      conditions bougent. Le dépôt sait déjà changer de route et le note quand il le fait. Et le
      mode sans assistance prouve que le produit tient debout sans eux.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>Le programme change sous vos pieds</h3><span class="badge b-loi">structurel</span></div>
      <p>Il vient de le faire&nbsp;: le 1<sup>er</sup> juillet 2026, la livraison est passée aux
      partenaires publics et deux pages de conditions ont disparu. Un client dont le mandat vient
      d'une politique peut le perdre par une autre. La parade est de vendre du <strong>matériel
      qui survit au programme</strong> &mdash; il sert aussi en classe ordinaire &mdash; et de ne
      jamais bâtir une ligne de revenus sur une seule enveloppe.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>Vendre à du public, c'est un autre métier</h3><span class="badge b-dec">à surveiller</span></div>
      <p>Cycles budgétaires, règles d'acquisition, seuils d'appel d'offres, une signature de plus
      qu'on ne croyait. Le cycle court de l'entreprise n'existe pas ici. En contrepartie, un
      partenaire qui adopte le matériel ne le change pas l'année suivante.</p>
    </div>
    <div class="dec">
      <div class="ligne"><h3>Le sur-mesure qui mange la marge</h3><span class="badge b-dec">à surveiller</span></div>
      <p>Chaque client voudra son scénario. La chaîne rend ça possible&nbsp;; l'indiscipline rend ça
      ruineux. La règle&nbsp;: on personnalise le <strong>décor</strong> &mdash; noms, zones,
      machines, vocabulaire &mdash; jamais la structure des huit blocs.</p>
    </div>
  </div>
</section>

<section>
  <h2>8. Quatre-vingt-dix jours</h2>
  <ol class="actions">
    <li><h3>Trois services aux entreprises, pas dix employeurs</h3>
      <p>Les partenaires mandatés les plus proches. On ne leur vend pas un cours&nbsp;: on leur
      montre le portail, la bascule de langue et le bloc qui se joue, et on demande ce qui leur
      manque pour livrer leur mandat.</p>
      <p class="qui">C'est une conversation entre gens du même réseau, pas un démarchage à froid.
      C'est votre avantage, et il ne se transfère pas.</p></li>
    <li><h3>Un groupe pilote, obtenu par l'un d'eux</h3>
      <p>Six à huit personnes, une vraie usine, sur les heures payées &mdash; dans un cours que le
      partenaire donne et facture. Le prix du pilote est secondaire&nbsp;: ce qu'on y gagne, ce
      sont les réponses réelles, la matière du diagnostic didactique et la seule preuve qui se
      raconte ensuite.</p></li>
    <li><h3>Écrire les sept autres blocs avec les mots du terrain</h3>
      <p>Pas avant. C'est ce que la demi-journée d'analyse sert à récolter, et ce qui rend le
      deuxième client plus rapide que le premier.</p></li>
    <li><h3>Trancher les deux questions qui restent</h3>
      <p>Le prix, et l'analyse offerte ou facturée. La troisième &mdash; l'employeur en direct ou
      les programmes &mdash; a trouvé sa réponse dans le relevé de marché&nbsp;: <strong>ni l'un
      ni l'autre, le réseau mandaté</strong>.</p></li>
  </ol>
</section>

<section>
  <h2>Ce que ce plan refuse de dire</h2>
  <div class="reserve">
    <p><strong>Aucun prix.</strong> Un montant écrit ici serait périmé à la première négociation, et
    il enlèverait la marge de manœuvre là où elle sert le plus.</p>
    <p><strong>Aucune taille de marché.</strong> On ne la connaît pas. Un nombre inventé dans un
    plan d'affaires est repéré par la première personne du métier qui le lit &mdash; et il emporte
    le reste avec lui.</p>
    <p><strong>Aucun rendement promis.</strong> Sur douze mois, trop de choses bougent dans une
    usine pour attribuer une baisse d'incidents à huit heures de cours. On mesure une tendance.
    Le dire avant qu'on le demande est ce qui fait croire le reste.</p>
  </div>
</section>

<div class="pied">
  <p>Plan d'affaires &mdash; chantier « formation en entreprise ». Chiffres relevés sur le dépôt le %(quand)s.</p>
  <p>Produit par <code>build/plan_affaires.py</code> &mdash; les nombres se recomptent à chaque exécution.</p>
  <p>À lire avec&nbsp;: <a href="analyse-marche.html">Le marché, vérifié</a> &mdash; qui est
  la source de la révision du 31 août &mdash;,
  <a href="strategie-communication.html">La stratégie de communication</a>,
  <a href="programme-belrive.html">Huit heures chez Belrive</a>,
  <a href="diagnostic-didactique.html">Le diagnostic didactique</a></p>
</div>

</div>
</body>
</html>
""" % {k: (nb(v) if isinstance(v, int) else v) for k, v in m.items()}


# ═══════════════════════════════════════════════════════════════════════
#  LA STRATÉGIE DE COMMUNICATION
# ═══════════════════════════════════════════════════════════════════════

# Huit publications, une par semaine pendant deux mois. Chacune est bâtie sur
# une pièce qui existe : c'est ce qui les rend impossibles à écrire pour
# quelqu'un qui n'a rien produit — et c'est tout l'intérêt.
#
# L'accroche est ce qui paraît avant « voir plus » : deux lignes, pas trois.
# Une publication qui a besoin de son troisième paragraphe pour intéresser
# n'intéressera personne.
POSTES = [
    ("« Oui, oui. »",
     "Le mot le plus cher d'une usine",
     "Un contremaître donne trois consignes en huit secondes et repart.\n"
     "La personne répond « oui, oui ». Personne ne saura jamais qu'elle n'a pas compris.",
     "Raconter la scène, puis le coût : la tâche à refaire, et surtout le fait que "
     "vingt minutes plus tard, ça ressemble à une faute de l'employé. Finir sur la "
     "phrase du bloc : « ce cours n'apprend pas des mots, il donne la permission de "
     "les dire ».",
     "L'extrait sonore de huit secondes, ou la capture du premier écran."),

    ("Traduire, c'est supprimer",
     "Pourquoi la traduction automatique tue l'apprentissage",
     "On me demande souvent de « traduire le cours en espagnol ».\n"
     "Si je le fais, il n'y a plus rien à apprendre.",
     "Les trois couches : le contenu à apprendre ne bascule jamais, la langue d'appui "
     "bascule, la traduction d'un mot se demande. Montrer que l'appui se pose SOUS le "
     "français, jamais à sa place.",
     "Les deux captures côte à côte, français et español."),

    ("L'énoncé est en cause",
     "Ce qu'une mauvaise réponse dit vraiment",
     "Quand la moitié d'un groupe rate la même question, ce n'est pas le groupe\n"
     "qui est faible. C'est la question qui est mauvaise.",
     "La distinction qui fonde la méthode : évaluer l'élève, c'est de l'évaluation ; "
     "évaluer le matériel par les réponses de l'élève, c'est du diagnostic didactique. "
     "Ajouter le corollaire, moins intuitif : un item réussi par tout le monde occupe "
     "une place que rien n'occupe.",
     "Aucune image ne vaut mieux qu'une image inutile. Texte seul."),

    ("Le débit se règle à la synthèse",
     "Un détail de production qui s'entend",
     "Ralentir un enregistrement après coup, ça s'entend.\n"
     "Il faut le demander à la voix pendant qu'elle parle.",
     "Le métier derrière l'outil. Deux personnages, deux débits : le superviseur au "
     "débit normal, l'apprenante un palier plus bas. Le contraste EST la leçon — on n'a "
     "pas eu à écrire que le superviseur parle trop vite.",
     "Les deux extraits, l'un après l'autre."),

    ("L'image qui illustre le thème",
     "Le défaut qu'on ne voit qu'en mettant les deux côte à côte",
     "Une image d'exercice doit montrer ce que dit son énoncé.\n"
     "Presque toutes montrent le thème du module. Ce n'est pas la même chose.",
     "Le défaut le plus fréquent, et invisible tant qu'on ne pose pas la phrase sous "
     "l'image. Enchaîner sur la parade dans une usine, où tout porte une inscription : "
     "on n'interdit pas le texte, on cadre pour qu'il sorte du champ.",
     "Une image juste et une image fautive, avec leur énoncé sous chacune."),

    ("Ce que ce n'est pas",
     "Trois choses que je ne vends pas",
     "Ce n'est pas un cours de français général. Je ne promets aucun rendement chiffré.\n"
     "Et huit heures ne rendent personne bilingue.",
     "L'encadré du dépliant, tel quel. C'est la publication qui fait le plus confiance, "
     "parce qu'elle enlève au lieu d'ajouter. Terminer sur ce que ça rend vraiment : "
     "quelqu'un capable de dire « attendez, répétez lentement ».",
     "Texte seul."),

    ("Le programme, au complet",
     "Huit niveaux, et pas un trou",
     "Le programme de francisation compte quatre-vingt-cinq situations de vie,\n"
     "réparties sur huit niveaux. Elles ont toutes leur module.",
     "Le seul post « inventaire » de la série, et il ne vient qu'en septième : on montre "
     "l'ampleur après avoir montré le soin. Nommer aussi ce qui manque — les savoirs que "
     "les ateliers ne couvrent pas encore — parce qu'un inventaire sans trou n'est pas cru.",
     "Le tableau de bord du projet, une capture."),

    ("Le français général se donne déjà",
     "Ce qui manque n'est pas un cours de plus",
     "Au Québec, un travailleur peut suivre un cours de français gratuit sur ses heures payées.\n"
     "Personne ne lui apprend à dire « attendez, répétez lentement ».",
     "La publication la plus utile pour parler au réseau public, et la plus délicate : elle ne "
     "critique pas le service, elle nomme ce qu'il ne peut pas faire — enseigner un poste précis. "
     "Finir sur l'offre : le matériel du poste, à ceux qui donnent déjà le cours.",
     "La capture du bloc, avec le sélecteur de langue visible."),

    ("Une demande d'aide qui se souvient d'où elle vient",
     "Comment une trace devient un outil de conception",
     "Un élève clique « je ne comprends pas ». La trace part avec le titre de\n"
     "l'exercice qui l'a provoquée. C'est là que le matériel commence à se corriger.",
     "Boucler la série sur le diagnostic didactique, cette fois par la mécanique. "
     "Insister sur le fait que rien de tout cela ne remonte nommément à un employeur : "
     "ce qui sort, ce sont des constats sur le matériel.",
     "Une capture de la page de progression, sans aucun nom."),
]

SITE = [
    ("Accueil", "Une page, trois blocs : la scène « oui, oui », ce qu'on livre, "
                "une démonstration qui se joue sans inscription."),
    ("La démarche", "Le diagnostic didactique, écrit pour quelqu'un qui n'est pas "
                    "pédagogue. C'est la page qui distingue, et celle qu'on envoie en lien."),
    ("Les outils", "Ce qui est bâti, en quatre familles : les modules, les ateliers "
                   "libres, les points express, le portail de l'enseignant. Chiffres "
                   "comptés, jamais arrondis à la hausse."),
    ("Les démos", "Trois pièces qui s'ouvrent d'un clic, sans compte. Rien d'autre "
                  "n'a le droit d'être sur cette page."),
    ("Pour les entreprises", "Le dépliant, en page web : les trois moments, les huit "
                             "heures, ce qu'on mesure, ce que ce n'est pas."),
    ("Pour les centres", "Le portail : huit niveaux, la planification par groupe, le "
                         "mode sans assistance, le mode séance sans compte."),
    ("À propos", "Une personne, un métier, et pourquoi ce matériel existe. Court."),
    ("Écrire", "Un formulaire de trois champs. Pas de prise de rendez-vous automatique : "
               "à ce stade, chaque conversation mérite d'être lue."),
]


def page_com(m):
    postes = '\n'.join("""    <li><h3>%s <span class="cout">&mdash; %s</span></h3>
      <p class="acc">%s</p>
      <p>%s</p>
      <p class="qui">À joindre&nbsp;: %s</p></li>"""
        % (t, ang, acc.replace('\n', '<br>'), corps, piece)
        for t, ang, acc, corps, piece in POSTES)
    site = '\n'.join("""      <tr><td class="t">%s</td><td class="q">%s</td></tr>""" % (n, d)
                     for n, d in SITE)
    gabarit = entete("Stratégie de communication",
                     "STRATÉGIE DE COMMUNICATION\n   Le positionnement, LinkedIn "
                     "rédigé, le site, et huit\n   publications prêtes à partir.") + """<body>
<div class="doc">
<style>
  .acc{background:var(--sunken);border-left:3px solid var(--acier);border-radius:3px;
    padding:11px 14px;font-size:16px;line-height:1.55;color:var(--ink);font-weight:600}
  .champ{background:var(--card);border:1px solid var(--line);border-radius:3px;
    padding:18px 20px;margin-top:10px}
  .champ h4{font-size:11.5px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;
    color:var(--muted);margin:0 0 9px}
  .champ p{font-size:15.5px;margin:0 0 9px}
  .champ p:last-child{margin-bottom:0}
  .champ .vide{background:var(--decid-bg);color:var(--decid);font-weight:700;
    padding:0 5px;border-radius:3px}
  ol.actions li h3 .cout{font-weight:600}
</style>

<a class="retour" href="/presentations.html"><span aria-hidden="true">&#8592;</span> Le classeur</a>

<p class="eyebrow">Chantier &mdash; formation en entreprise</p>
<h1>Stratégie de communication</h1>
<p class="chapeau">Ce qu'on dit, à qui, et dans quel ordre. <strong>LinkedIn avant le
site</strong>&nbsp;: un site sans visiteurs ne fait rien, alors qu'une publication amène une
rencontre. Tout ce qui suit est rédigé pour être copié tel quel &mdash; les
<span style="background:#FBF2E2;color:#C07A08;font-weight:700;padding:0 5px;border-radius:3px">cases
en ambre</span> sont les seules choses que vous seul pouvez écrire.</p>

<section class="premier">
  <h2>Le positionnement</h2>
  <div class="these">
    <p class="cle">Pas des cours de français. Les gestes de parole qui manquent à un poste
    de travail.</p>
    <p>C'est la phrase qui sépare de tout le reste du marché. Un employeur n'achète pas
    «&nbsp;du français&nbsp;» &mdash; il n'a aucune idée de ce que ça coûte ni de ce que ça
    rapporte. Il achète la fin d'un moment qui se passe mal dans sa journée.</p>
  </div>
  <p>Et pour la personne, sur un profil&nbsp;: <strong>«&nbsp;Je conçois du matériel de
  francisation, et je le corrige avec les réponses des élèves.&nbsp;»</strong> La seconde moitié de
  la phrase est celle qui fait lever un sourcil, parce que presque personne ne le fait.</p>
</section>

<section>
  <h2>Ce qu'on ne dit jamais</h2>
  <div class="avert">
    <p><strong>Aucun pourcentage inventé.</strong> «&nbsp;30&nbsp;% de reprises en moins&nbsp;» se
    repère en une seconde et emporte le reste de la crédibilité.</p>
    <p><strong>Le mot «&nbsp;IA&nbsp;» n'ouvre jamais une phrase.</strong> Il a quitté l'interface
    du produit&nbsp;; il ne doit pas revenir par la porte du marketing. On parle d'assistance quand
    c'est utile, à la troisième ligne, jamais en titre.</p>
    <p><strong>Ni «&nbsp;révolutionner&nbsp;», ni «&nbsp;clé en main&nbsp;», ni
    «&nbsp;bilingue&nbsp;».</strong> Les deux premiers ne veulent rien dire. Le troisième promet ce
    que huit heures ne peuvent pas livrer.</p>
    <p><strong>Jamais une capture qui contient la réponse d'un élève réel</strong>, même sous
    pseudonyme. La règle du produit vaut aussi pour ce qu'on publie.</p>
  </div>
</section>

<section>
  <h2>Quatre publics, quatre premières phrases</h2>
  <p>L'ordre a changé le 31 août 2026&nbsp;: <a href="analyse-marche.html">le relevé du marché</a>
  a montré que la francisation en milieu de travail est livrée gratuitement par le réseau public.
  Le premier public n'est donc plus l'employeur &mdash; c'est celui qui le sert.</p>
  <div class="roule">
  <table class="cmp">
    <thead><tr><th>À qui</th><th>La première phrase</th><th>Ce qu'on lui montre ensuite</th></tr></thead>
    <tbody>
      <tr class="f"><td>Un service aux entreprises <span class="cout">(CSS, cégep)</span></td><td>«&nbsp;Vous avez le mandat et les groupes. Je fais le matériel &mdash; en français, en espagnol et en anglais, avec les traces qui vous disent ce qui a coincé.&nbsp;»</td><td>le portail, la bascule de langue, et le bloc qui se joue en trois minutes</td></tr>
      <tr><td>Un employeur</td><td>«&nbsp;Vos gens comprennent-ils les consignes&nbsp;? Pas
        “parlent-ils français”&nbsp;— comprennent-ils la consigne donnée en quinze secondes, dans
        le bruit&nbsp;?&nbsp;»</td><td>le bloc de démonstration, joué devant lui, en trois minutes</td></tr>
      <tr><td>Une direction de centre</td><td>«&nbsp;Les huit niveaux du programme ont leur
        matériel. Vos enseignants n'ont plus à le fabriquer.&nbsp;»</td><td>le portail, la
        planification par groupe, le mode sans assistance</td></tr>
      <tr><td>Un enseignant</td><td>«&nbsp;Vous verrez ce que votre classe a répondu, question par
        question, pendant qu'elle répond.&nbsp;»</td><td>le direct de la classe, et les points
        express qu'on envoie à un seul élève</td></tr>
    </tbody>
  </table>
  </div>
</section>

<section>
  <h2>LinkedIn &mdash; le profil</h2>

  <div class="champ">
    <h4>Le titre (sous le nom)</h4>
    <p>Trois formulations, de la plus sobre à la plus tranchante. La deuxième est celle que
    je retiendrais&nbsp;: elle dit un métier et une méthode en huit mots.</p>
    <p>1. Pédagogue en francisation &middot; conception de matériel d'apprentissage</p>
    <p>2. <b>Je conçois du matériel de francisation &mdash; et je le corrige avec les réponses des élèves</b></p>
    <p>3. Francisation en milieu de travail &middot; matériel multilingue, corrigé par l'usage</p>
  </div>

  <div class="champ">
    <h4>La section « Infos »</h4>
    <p>J'enseigne le français à des adultes qui arrivent au Québec. En le faisant, j'ai
    passé des années à fabriquer le matériel qui manquait&nbsp;: des situations vraies, des voix
    qu'on comprend, des exercices qui portent sur ce qu'on va dire demain.</p>
    <p>Ce matériel couvre aujourd'hui les huit niveaux du programme de francisation
    &mdash; %(activites)s activités, %(pptx)s séances prêtes à projeter, %(mp3)s extraits
    sonores. Il tourne dans un portail où l'enseignant planifie, voit sa classe répondre en
    direct, et reçoit les productions orales et écrites de ses élèves.</p>
    <p>Deux partis pris le distinguent.</p>
    <p><b>La langue d'appui.</b> Les consignes et les explications basculent en espagnol,
    en anglais ou dans une autre langue&nbsp;; ce qu'on apprend à dire reste en français.
    Traduire le contenu, ce serait supprimer l'apprentissage.</p>
    <p><b>Le diagnostic didactique.</b> Je ne livre pas un cours&nbsp;: je livre un cours
    corrigé par les réponses réelles des gens qui l'ont suivi. Un exercice raté par la moitié
    d'un groupe accuse l'énoncé, pas le groupe.</p>
    <p>Je travaille maintenant à porter cette approche <b>en milieu de travail</b>&nbsp;:
    des heures courtes sur les moments d'une journée où la langue coûte quelque chose &mdash;
    la consigne du superviseur, le relais de quart, le danger qu'on ne sait pas nommer. Le
    français général se donne déjà très bien&nbsp;; ce qui manque, c'est le poste.</p>
    <p><span class="vide">[une ligne sur votre parcours : où vous enseignez, depuis
    combien de temps, votre formation]</span></p>
    <p><span class="vide">[votre courriel]</span></p>
  </div>

  <div class="champ">
    <h4>La bannière</h4>
    <p><b>Pas un logo.</b> Une capture du premier écran d'un module, avec le sélecteur de
    langue visible en haut à droite. Elle dit en une image ce que trois paragraphes
    expliquent&nbsp;: c'est un vrai outil, et il parle plusieurs langues.</p>
  </div>

  <div class="champ">
    <h4>Les compétences à mettre en avant, dans cet ordre</h4>
    <p>Conception pédagogique &middot; Francisation des adultes &middot; Français langue
    seconde &middot; Formation en milieu de travail &middot; Ingénierie de formation
    &middot; Évaluation des apprentissages &middot; Conception de matériel multilingue</p>
    <p>L'ordre compte&nbsp;: les trois premières disent qui vous êtes, les trois suivantes
    disent où vous allez.</p>
  </div>
</section>

<section>
  <h2>LinkedIn &mdash; huit publications, prêtes</h2>
  <p>Une par semaine, le mardi en matinée. Elles sont dans l'ordre&nbsp;: on montre le
  <em>soin</em> avant de montrer l'<em>ampleur</em>, sans quoi l'inventaire passe pour de la
  vantardise. L'accroche est ce qui paraît avant «&nbsp;voir plus&nbsp;»&nbsp;: deux lignes,
  jamais trois.</p>
  <ol class="actions">
%(postes)s
  </ol>
  <div class="reserve">
    <p><strong>Répondre à tous les commentaires le jour même</strong>, et à la question
    difficile en premier. Une objection publique bien répondue vaut trois publications.</p>
    <p><strong>Ne jamais publier deux fois la même semaine.</strong> La série tient sa force
    de sa régularité, pas de son volume.</p>
  </div>
</section>

<section>
  <h2>Le site</h2>
  <p>Huit pages, pas davantage. Il vient <strong>après</strong> LinkedIn&nbsp;: son rôle
  n'est pas d'attirer, c'est de <em>confirmer</em> quelqu'un qui vient d'entendre parler de vous
  et qui vérifie que vous existez pour de vrai.</p>
  <div class="roule">
  <table class="cmp">
    <thead><tr><th>Page</th><th>Ce qu'elle fait</th></tr></thead>
    <tbody>
%(site)s
    </tbody>
  </table>
  </div>

  <h3 style="margin-top:10px">Le texte de l'accueil</h3>
  <div class="champ">
    <h4>Titre</h4>
    <p><b>Vos gens comprennent-ils les consignes&nbsp;?</b></p>
    <h4>Sous-titre</h4>
    <p>Pas «&nbsp;parlent-ils français&nbsp;». Comprennent-ils la consigne qu'on leur donne
    en quinze secondes, dans le bruit, en marchant&nbsp;? C'est une autre question, et c'est
    celle qui vous coûte quelque chose.</p>
    <h4>Les deux boutons, et rien d'autre</h4>
    <p><b>Essayer une heure de cours</b> &mdash; qui ouvre la démonstration, sans inscription.
    <br><b>Voir la démarche</b> &mdash; qui ouvre la page du diagnostic didactique.</p>
    <h4>Sous les boutons</h4>
    <p>%(activites)s activités en service, les huit niveaux du programme, %(mp3)s extraits
    sonores enregistrés. Conçu et produit au Québec, par une personne qui enseigne.</p>
  </div>

  <h3>Les démos publiables, et la règle</h3>
  <ul class="simple">
    <li><b>Le bloc «&nbsp;Je n'ai pas compris&nbsp;»</b> &mdash; une heure complète, avec sa
    bascule de langue. L'usine est fictive&nbsp;: aucune donnée réelle, aucun consentement à
    demander.</li>
    <li><b>Un point express</b> &mdash; dix minutes, une seule difficulté. Il montre le format
    court, celui qu'un employeur imagine mal avant de l'avoir vu.</li>
    <li><b>Un atelier de la banque</b> &mdash; il se joue seul, sans compte, et prouve que l'élève
    peut travailler entre deux séances.</li>
  </ul>
  <div class="avert">
    <p><strong>Le portail de l'enseignant ne va pas en démonstration publique.</strong> Il montre
    des groupes, des progressions, des productions&nbsp;: même vidé, même sous pseudonyme, on ne
    met pas en vitrine l'écran qui contient le travail de personnes réelles. Pour un client, il se
    montre <em>en direct, devant lui</em>, sur une classe de démonstration &mdash; jamais en libre
    accès.</p>
  </div>
</section>

<section>
  <h2>L'ordre, et rien de plus</h2>
  <ol class="actions">
    <li><h3>Le profil, cette semaine</h3>
      <p>Titre, section «&nbsp;Infos&nbsp;», bannière. Une heure de travail, et c'est la
      seule chose qui existe déjà avant que vous parliez à qui que ce soit.</p></li>
    <li><h3>Les publications, à partir de la semaine suivante</h3>
      <p>Huit semaines. Ne pas attendre le site&nbsp;: chaque publication renvoie vers la
      démonstration, qui est déjà en ligne.</p></li>
    <li><h3>Le site, au bout de quatre publications</h3>
      <p>À ce moment-là, vous saurez lesquelles des huit ont porté &mdash; et ce sont
      celles-là qui donnent le texte des pages.</p>
      <p class="qui">Écrire un site avant de savoir ce qui intéresse, c'est écrire deux fois.</p></li>
    <li><h3>Les rencontres, tout du long</h3>
      <p>La communication ne remplace pas le démarchage&nbsp;: elle le rend plus facile. Le
      premier contrat viendra d'une conversation, pas d'une publication.</p></li>
  </ol>
</section>

<div class="pied">
  <p>Stratégie de communication &mdash; chantier « formation en entreprise ». Chiffres relevés le %(quand)s.</p>
  <p>Produite par <code>build/plan_affaires.py</code>, avec le plan d'affaires&nbsp;: une seule
  source pour un seul inventaire.</p>
  <p>À lire avec&nbsp;: <a href="plan-affaires.html">Le plan d'affaires</a>,
  <a href="depliant-entreprise.html">Le dépliant de démarchage</a></p>
</div>

</div>
</body>
</html>
"""
    jetons = dict({k: (nb(v) if isinstance(v, int) else v) for k, v in m.items()},
                  postes=postes, site=site)
    for cle, val in jetons.items():
        gabarit = gabarit.replace('%(' + cle + ')s', str(val))
    reste = re.findall(r'%\([a-z_]+\)s', gabarit)
    if reste:
        raise SystemExit('jeton non rempli : %s' % ', '.join(sorted(set(reste))))
    return gabarit


def imprimer(source, cible):
    chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    if not pathlib.Path(chrome).exists():
        return
    subprocess.run([chrome, '--headless', '--disable-gpu', '--no-pdf-header-footer',
                    '--print-to-pdf=%s' % cible, source.as_uri()],
                   capture_output=True, timeout=120)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--plan', action='store_true')
    ap.add_argument('--com', action='store_true')
    ap.add_argument('--texte', action='store_true')
    a = ap.parse_args()
    m = mesures()
    if a.texte:
        for k, v in m.items():
            print('  %-12s %s' % (k, nb(v) if isinstance(v, int) else v))
        return
    tout = not (a.plan or a.com)
    if a.plan or tout:
        PLAN.write_text(page_plan(m), encoding='utf-8')
        print('  %-34s %s activités · %s séances' % (PLAN.name, nb(m['activites']), nb(m['pptx'])))
    if a.com or tout:
        COM.write_text(page_com(m), encoding='utf-8')
        print('  %-34s %d publications · %d pages de site' % (COM.name, len(POSTES), len(SITE)))
    print('  À REMPLIR : le profil LinkedIn porte deux cases en ambre (parcours, courriel)')


if __name__ == '__main__':
    main()
