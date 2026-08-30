# Plan et journal — `module-n3-horaire` (activité 84)

Niveau 3 · situation « Emploi » · numéro 11 dans le niveau · 16 séances,
3 défis (`GRILLE_3_DEFIS`).

## Ce que le programme demande

`python3 build/cadre.py 3 "Emploi"` donne **six intentions**, réparties sur les
quatre compétences — c'est peu, mais c'est complet, et chacune est exerçable :

| Compétence | Intention | Où elle vit dans le module |
|---|---|---|
| CO | Comprendre une consigne | Défi 3, dialogue `t3` et exercice `t3imp` |
| CO / PO | Demander une permission et en comprendre la réponse | Défi 2, `t2poli` et `t2perm` |
| CO / PO | Demander de l'aide ou un service et en comprendre la réponse | Défi 3, `t3aide` |
| PO | Répondre à une demande de service | Défi 3, `t3repondre` (madame Pouliot) |
| CE | Lire des consignes simples | Défi 1, `t1horaire` · Défi 3, `t3liste` |
| PE | Prendre en note une directive ou une information simple | Défi 3, `t3note` et la production écrite |

Le lexique du programme est **généreux** à ce stade et il a servi tel quel
plutôt que d'être inventé : « noms de tâches », et les verbes rattachés
*passer, laisser, livrer, s'occuper de, offrir, s'absenter, abandonner,
justifier, oublier, devoir, aviser, peindre, emprunter, prêter, éteindre*,
avec les quatre tournures d'appel à l'aide que la source donne mot pour mot —
« Qu'est-ce qui se passe ? », « Pouvez-vous m'aider ? », « Passe-moi ton
crayon », « Qui peut m'aider ? », « Est-ce que tu peux m'aider ? ». Elles sont
la matière du Défi 3.

## Ce qui distingue ce module de son voisin du niveau 4

Au niveau 4, le module « Emploi » **annonce une absence** : on téléphone, on
justifie, on négocie à distance, en phrases longues. Au niveau 3, tout se passe
**sur le plancher, en présence, devant un papier affiché** : on lit son quart
sur l'horaire de la semaine, on demande un changement en trois mots au chef
d'équipe, on écoute la tâche du jour et on dit qu'on a fini. Le soutien visuel
— l'horaire, la liste de tâches, le chariot — porte la moitié du sens, et
aucun énoncé du module ne dépasse une ligne.

## Le scénario et les personnages (inventés, rien n'est copié)

**Amara Sissoko**, 34 ans, arrivée du Mali il y a huit mois, commence comme
**préposée à l'entretien ménager** à la **Résidence des Deux-Rives**, à
Longueuil. Trois semaines qu'elle y est ; elle fait bien le travail mais elle
perd le fil dès qu'on lui parle : l'horaire est affiché sur un mur, la tâche du
jour se donne à l'oral, et personne ne répète.

**Yvon Ouimet**, chef d'équipe de l'entretien, 24 ans dans le métier. Il donne
l'horaire le vendredi, la tâche du matin à sept heures, et il n'a jamais le
temps. Il tutoie son équipe et son équipe le tutoie.

**Madame Rachel Pouliot**, 81 ans, chambre 214. Elle demande des petits
services à qui passe dans le corridor. Amara la **vouvoie** — c'est la seule
personne du module qu'on vouvoie, et cette différence-là est enseignée.

Tutoiement dans l'équipe, vouvoiement avec les résidentes : c'est tenu partout,
y compris dans l'écran de fin et dans le jeu de rôle.

## Les quatre sections et leur progression

| Section | Titre | Ce que l'élève apprend à faire |
|---|---|---|
| `prep` | **Je découvre** | Nommer les tâches et les moments de la journée de travail |
| `t1` | **Défi 1 · Mon quart de la semaine** | Lire l'horaire affiché, dire quand on travaille |
| `t2` | **Défi 2 · Demander un changement** | Demander une permission, aviser d'une absence, justifier |
| `t3` | **Défi 3 · La tâche du jour** | Comprendre une consigne, la noter, demander de l'aide, dire qu'on a fini |
| `appli` | **Je me lance** | Jeu de rôle avec Yvon, production orale, note écrite de fin de quart |

## La progression grammaticale — huit points, huit mini-leçons

1. `prPhon` — phonétique : le son de **demain** [ɛ̃] et le son de **dimanche**
   [ɑ̃]. Choisi parce que ce sont les deux sons des jours et des dates, et
   qu'entendre « lundi » pour « lundi prochain » coûte un quart de travail.
2. `prTemps` — les **prépositions de temps** du travail : *de… à, à partir de,
   jusqu'à, avant, après, vers*.
3. `t1futur` — le **futur proche** : *je vais commencer à sept heures*.
4. `t1marq` — les **marqueurs de temps** : *demain, la semaine prochaine, lundi
   prochain, dans deux jours, tous les matins*.
5. `t2poli` — les **auxiliaires de modalité au conditionnel de politesse** :
   *je pourrais, je voudrais, j'aimerais, il faudrait*.
6. `t2neg` — la **phrase négative** : *ne… pas, ne… plus, ne… pas encore*, et le
   « pas » seul de l'oral.
7. `t3imp` — l'**impératif présent** de la consigne : *passe, laisse, éteins,
   prends, va*.
8. `t3pron` — les **pronoms personnels compléments** *le, la, les, lui* pour
   reprendre un GN — nommé explicitement dans les attentes de fin de cours du
   niveau 3.

## Les trois productions de « Je me lance »

1. **Jeu de rôle** avec Yvon Ouimet — scénario `horaire` dans `server.py`,
   trois cas : `changement`, `absence`, `consigne`. Aucun scénario existant ne
   convenait, il a fallu l'écrire.
2. **Production orale** : demander un changement d'horaire au chef d'équipe.
3. **Production écrite** : la note laissée au chef d'équipe à la fin du quart —
   ce qui est fait, ce qui reste, ce qui manque. C'est l'intention de
   production écrite du programme, prise au mot.

## Journal de production

- Le cadre a été sorti avant d'inventer quoi que ce soit :
  `python3 build/cadre.py 3 "Emploi"`.
- Les noms ont été vérifiés contre `build/contenu/` avant d'être retenus :
  *Nadia*, *Marisol*, *Djamila*, *Réjean*, *Suzie* et *Gilles* étaient déjà
  pris par d'autres modules ; *Amara Sissoko*, *Yvon Ouimet* et *Rachel
  Pouliot* ne le sont pas.

### Les médias, à lancer sur un poste qui a les clés

Cet agent tourne dans le nuage : `~/Claude/.env` n'y existe pas. Les deux
générateurs sont **écrits et relançables**, ils n'ont pas été lancés.

    python3 build/contenu/module-n3-horaire/gen_images.py
    # 24 images : 16 vocabulaire + 8 illustrations d'exercice.
    # Route Google en direct d'abord (build/route_images.py). ~0,81 $.

    python3 generer_audio_module_n3_horaire.py
    # 5 dialogues (80 répliques) + les extraits de sons_module_n3_horaire.json.
    # Le relevé des extraits se fait dans le navigateur, module ouvert :
    # le snippet console est en tête du script.
