# Qui fait quoi, en ce moment

**À lire au démarrage de toute session, et à mettre à jour avant d'écrire le
premier fichier.** Ce fichier ne dit pas le protocole — il est dans
[`deux-agents-en-parallele.md`](deux-agents-en-parallele.md) — il dit **qui
tient quoi, maintenant**.

Il existe parce que le 30 août 2026, deux sessions travaillaient dans cet arbre
et l'une a commité `presentations.html` pendant que l'autre l'éditait. Rien n'a
été perdu, mais l'historique ment : les changements d'une session sont partis
sous le message d'une autre. La règle qui l'aurait évité était déjà écrite
(`git commit -- <chemins>`) ; ce qui manquait, c'était de **savoir** que
quelqu'un tenait ce fichier.

## Comment s'en servir

1. **En ouvrant une session** : `git pull`, lire le tableau, ajouter sa ligne.
2. **Avant de toucher un fichier partagé** (la liste est dans
   `deux-agents-en-parallele.md`) : vérifier qu'aucune autre ligne ne le
   revendique. S'il est pris, faire autre chose et y revenir — pas attendre.
3. **En fermant** : retirer sa ligne, et commiter ce retrait.
4. Une ligne vieille de plus d'une journée est **morte** : la session est
   partie sans nettoyer. La retirer sans hésiter.

Une ligne se commite seule, tout de suite : `git add docs/qui-fait-quoi.md`
puis `git commit -- docs/qui-fait-quoi.md`. Ne jamais la garder en attente avec
autre chose.

## Le tableau

| Session | Ouverte | Ce que je tiens | Jusqu'à |
|---|---|---|---|
| `claude-38` | 30 août, 10 h | `modules-autonomes/`, `build/gabarit/storyline.html`, `build/storyline.py`, `build/contenu/module-n5-rendezvous/storyline.js`, `presentations.html` (par à-coups) | la démo storyline livrée |
| `claude-71` | 30 août, 11 h | `assets/presentations/` (la banque et ses pages), `build/trousse.py`, `build/materiel_pages.py`, `build/menage_proposition.py`, `build/greffe_retour.py`, `build/powerpoints/pitch/`, `presentations.html` (par à-coups) | la trousse de présentation livrée |

Le nom de session est celui que donne `ListAgents` (`claude-38`, `claude-71`…).
Il ne survit pas à la fermeture, et c'est voulu : une ligne dont le nom ne
figure plus dans `ListAgents` est une ligne morte.

## Ce qui n'a pas besoin d'être déclaré

Le contenu d'un module est **isolé par nature**, et c'est ce qui rend le travail
en parallèle possible. Inutile de réserver :

    build/contenu/<slug>/            à toi
    assets/interactive/<slug>/       à toi
    build/powerpoints/decks/<slug>/  à toi
    assets/powerpoints/<slug>/       à toi
    generer_audio_<slug>.py          à toi
    sons_<slug>.json                 à toi

On ne déclare ici que **les fichiers partagés** et **les chantiers
transversaux** — une refonte du gabarit, du système de design, une règle de
couleur : ceux-là touchent tous les modules à la fois et demandent que personne
d'autre n'écrive.
