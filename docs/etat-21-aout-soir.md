# Où en est le chantier — 21 août 2026, en soirée

Écrit avant une compaction de la conversation. Ce qui vit ici n'a pas besoin
d'être en mémoire d'agent.

## Les douze modules en cours

Tous lancés, aucun n'est en attente de lancement.

| Où | Activités |
|---|---|
| Machine locale | 71 `module-n5-actualite` · 82 `module-n3-voisins` · 93 `module-n2-guichet` |
| Nuage | 72 `module-n5-saisons` · 73 `module-n5-oeuvres` · 74 `module-n5-ecole` |
| Nuage | 83 `module-n3-recherche-emploi` · 84 `module-n3-horaire` · 85 `module-n3-loisirs` · 86 `module-n3-secretariat` |
| Nuage | 94 `module-n2-colis` · 95 `module-n2-secretaire` |

**86 ferme le niveau 3, 95 ferme le niveau 2.** Les agents du nuage produisent
tout sauf les médias : ils laissent `gen_images.py` et le générateur audio
prêts, avec les commandes exactes dans leur journal.

## Ce qui reste à faire, et qui ne peut pas se faire seul

1. **La passe audio.** ElevenLabs à zéro (`401 quota_exceeded`). **Dix-sept
   générateurs** écrits et relançables attendent — plus de trois mille
   extraits. À lancer sur **Sonnet**, pas Opus : c'est mécanique.
2. **Les images des modules du nuage** — un `gen_images.py` par module, tous
   passant par `build/route_images.py`. Environ 0,88 $ par module.
3. **Deux vieux défauts** confirmés par le septième contrôle : quatre pastilles
   qui lisent le mot seul dans `module-n1-presenter` (« prénom », « épeler »,
   « de rien ») et `module-n2-autobus` (« tout droit »). Demande de régénérer
   une poignée de MP3.

## Ce qui a été réglé aujourd'hui, et qu'il ne faut pas rouvrir

- **La panne du catalogue**, remontée jusqu'au bout : volume Railway plein →
  `activities.json` tronqué en pleine écriture → exception non rattrapée →
  502 opaque. Quatre corrections : écriture atomique, réparation automatique
  avec épave conservée, **repli sur la copie du code quand le fichier manque
  ou est illisible**, et suppression de la recopie de 588 Mo jamais lus.
- **La route des images** : `build/route_images.py`. Google en direct d'abord
  (0,0336 $, 3,9 s), fal.ai en repli (0,080 $), puis WaveSpeed (0,070 $). Kie
  AI répond 403. Les quatre revendent le même modèle Google.
- **Le registre des appels** : `~/Claude/generations/journal_appels.py` compte
  les appels facturés, plus les fichiers gardés. Le mur affichait 26,96 $ pour
  ce qui a coûté environ 63 $.
- **Le septième contrôle** : `node build/coherence.js <slug>`.

## Les règles apprises aujourd'hui, à ne pas repayer

- **Un seul `git push` par module, à la fin.** Chaque poussée redéploie et coupe
  la production une minute ; deux cents poussées en un jour, c'est un site
  intermittent. Mais **commiter après chaque fichier** : six agents sont morts
  d'une mise en veille.
- **N'inscrire un module à `data/activities.json` qu'une fois construit.**
  Trois coquilles ont été annoncées au catalogue sans exister.
- **Les agents du nuage survivent à la fermeture du portable, pas les locaux.**
  Il leur manque seulement `~/Claude/.env` ; la skill `module-neuf` est là.
