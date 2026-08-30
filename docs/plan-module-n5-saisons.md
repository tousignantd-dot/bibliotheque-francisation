# Plan et journal — `module-n5-saisons` (activité 72, niveau 5)

Module produit dans le nuage, sans clés d'API : le contenu, le build, les
présentations et les fiches sont faits ; les médias sont **écrits mais pas
lancés**. Les commandes exactes et le nombre d'extraits attendus sont en fin
de fichier.

## 1. Le cadre, tel que le programme le donne

`python3 build/cadre.py 5 "Météo"` rend :

- **une seule intention de communication** — *Écouter un bulletin météo à la
  radio*, en compréhension orale, domaine général **Culture et médias** ;
- **aucun lexique** : la situation n'a aucune entrée dans la progression du
  lexique. Les seize mots du banc sont composés à partir du savoir « Écoute
  d'un bulletin météorologique » (3 points) et de ce que la situation exige
  réellement ;
- les savoirs du niveau, communs à tout le cours : phrases impersonnelles,
  subjonctif présent, futur simple, pronoms personnels conjoints, connecteurs
  et relations logiques, reprise de l'information.

L'attente de fin de cours qui commande le module : « il rapporte le sens
général des propos de quelqu'un **au présent** en employant les pronoms et les
déterminants appropriés » — c'est le défi 3.

## 2. Ce qui distingue ce module de son voisin du niveau 4

**Au niveau 4 (`module-meteo`, Josée), l'élève lit et comprend des prévisions ;
ici, au niveau 5, la prévision ne s'arrête pas à être comprise : elle oblige à
décider, puis à faire porter la décision à d'autres personnes — reporter,
s'équiper, appeler, prévenir par écrit.**

Ce n'est pas non plus `module-n2-neige` (niveau 2), qui nomme le temps qu'il
fait et s'habille en conséquence.

## 3. Le scénario

**Nadia Belkacem**, 41 ans, arrivée d'Algérie il y a deux ans, habite le
Vieux-Longueuil. Elle est **responsable du service de garde** de l'école des
Deux-Ruisseaux. Cent quarante enfants, une sortie prévue au verger le
vendredi, une journée pédagogique le lundi suivant. Chaque matin, à six
heures, la météo décide de sa journée : elle écoute le bulletin, elle regarde
les avertissements, elle tranche, et elle prévient.

Trois personnages récurrents, plus une voix de radio :

| Nom | Rôle | Registre |
|---|---|---|
| **NADIA** | responsable du service de garde | tutoie ses collègues, vouvoie les parents |
| **LINE** | Line Charbonneau, directrice de l'école | tutoie Nadia |
| **GAÉTAN** | Gaétan Thibodeau, transporteur scolaire (Autobus Rive-Sud) | tutoie Nadia |
| **RADIO** | la voix du bulletin de six heures | s'adresse à tout le monde |
| **M. DORVAL** | un parent, au téléphone | vouvoiement mutuel |

Le vouvoiement/tutoiement n'est pas un détail : c'est une matière du module
(« salutations d'usage », registres). Nadia tutoie Line et Gaétan — des
collègues, au Québec, se tutoient — et vouvoie M. Dorval et les parents.

## 4. Les quatre sections

| Section | Titre | Ce qui s'y joue |
|---|---|---|
| `prep` | **Je découvre** | Le bulletin de six heures ; les seize mots ; les nasales [ɑ̃] / [ɔ̃] |
| `t1` | **Défi 1 · Le bulletin de six heures** | En tirer les chiffres et l'essentiel ; phrases impersonnelles ; futur simple |
| `t2` | **Défi 2 · L'avertissement** | Veille / avertissement / alerte ; « si » + présent → futur ; le subjonctif de l'obligation |
| `t3` | **Défi 3 · Prévenir tout le monde** | Rapporter au présent ce qu'a dit quelqu'un ; les pronoms *lui, leur, y, en* |
| `appli` | **Je me lance** | Jeu de rôle, message vocal aux parents, avis écrit |
| `retiens` | **Je retiens des mots** | Le banc des seize mots |

## 5. La progression grammaticale — sept points, sept mini-leçons

1. `prPhon` — **[ɑ̃] et [ɔ̃]**, les deux nasales que le bulletin oppose sans
   arrêt : *le vent* / *ils vont*, *décembre* / *la fonte*, *quand* / *qu'on*.
2. `t1imp` — **les phrases impersonnelles** : *il fait*, *il pleut*, *il
   ventera*, *il y aura*, *il est possible que*. La météo est le seul domaine
   de la langue qui n'a presque que ça.
3. `t1futur` — **le futur simple des prévisions**, opposé au futur proche :
   *il neigera* / *il va neiger*.
4. `t2si` — **« si » + présent → futur** : *si la pluie verglaçante commence,
   nous annulerons la sortie*. Le module s'en sert pour dire une décision
   avant de la prendre.
5. `t2subj` — **le subjonctif après « il faut que » et « pour que »** : *il
   faut que tu appelles*, *pour qu'ils soient prêts*.
6. `t3rapp` — **rapporter au présent** : *Line dit qu'elle annule*, *il
   demande si on part quand même*. C'est l'attente de fin de cours citée plus
   haut, mot pour mot.
7. `t3pron` — **les pronoms conjoints** *lui, leur, y, en* : *je leur ai
   écrit*, *j'y pense*, *on en parle demain*.

Chaque point porte un exercice de `exos.js` et une mini-leçon de `plus.js`
sous la même clé.

## 6. Les trois productions de « Je me lance »

1. **Jeu de rôle** — scénario `avertissement` ajouté à `server.py` (le
   scénario `meteo` existant porte le niveau 4 : il n'est pas réutilisé).
   Trois cas : `transport` (appeler le transporteur), `parent` (un parent
   inquiet au téléphone), `direction` (rapporter à la directrice).
2. **Production orale** — le message vocal laissé aux parents pour annoncer le
   report de la sortie au verger.
3. **Production écrite** — l'avis écrit envoyé aux parents le soir même.

## 7. Les faits québécois employés, vérifiés et non devinés

- **Environnement et Changement climatique Canada** émet trois niveaux
  d'alerte publique : la **veille** (les conditions favorables existent), l'
  **avertissement** (le phénomène est en cours ou imminent) et le **bulletin
  météorologique spécial** (une situation inhabituelle à surveiller).
- Le **refroidissement éolien** est l'indice hivernal ; l'**humidex** est son
  équivalent d'été.
- La **pluie verglaçante** est le phénomène qui ferme les écoles au Québec plus
  souvent que la neige : c'est de l'eau liquide qui gèle en touchant le sol.
- Les commissions scolaires du Québec sont devenues des **centres de services
  scolaires** en 2020 ; c'est le centre de services, avec le transporteur, qui
  décide de la fermeture des écoles, pas l'école elle-même.
- La **poudrerie** est le mot québécois pour la neige déjà tombée que le vent
  soulève ; c'est ce qui coupe la visibilité sur les routes.

L'école des Deux-Ruisseaux, Autobus Rive-Sud, les personnes, les températures
et les heures précises sont **inventés**.

## 8. Les médias — écrits, jamais lancés

Cet agent tourne dans le nuage : `~/Claude/.env` n'existe pas chez lui, donc
ni ElevenLabs ni la route des images ne répondent. Les deux générateurs sont
écrits et relançables tels quels sur la machine locale.

    python3 build/contenu/module-n5-saisons/gen_images.py
    python3 generer_audio_module_n5_saisons.py

Le nombre d'extraits attendu et le relevé des identifiants sont notés en fin
de production, plus bas.

---

## Journal
