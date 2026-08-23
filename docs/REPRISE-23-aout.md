# Reprise — 23 août 2026, fin de session sur limite d'utilisation

Écrit à chaud, la limite approchant. Une session qui se ferme emporte tout ce
qui n'est pas dans `docs/` : voici l'état exact, et l'ordre des gestes.

## Ce qui tourne encore, et qui ne consomme aucun jeton

**La production audio est lancée** et continue toute seule : c'est un
processus Python local, indépendant de la limite d'utilisation. Ne pas la
relancer par-dessus.

    ps aux | grep audio_tous          # tourne-t-elle encore ?
    find assets -name "*.mp3" | wc -l # avancement (voir les repères ci-dessous)

Repères : **2 982** MP3 juste après l'effacement, **3 379** vingt minutes plus
tard. La cible est d'environ **8 500 + les dix modules muets**. Si le compte
n'a pas bougé depuis longtemps et qu'aucun processus ne tourne, relancer
simplement `python3 build/audio_tous.py` : **rien n'est repayé**, chaque
générateur saute ce qui est déjà sur le disque.

### La règle à ne pas enfreindre

**Ne rien commiter ni pousser dans `assets/interactive/**/*.mp3` tant que la
production n'est pas finie.** Le dépôt local porte en ce moment 5 556 fichiers
effacés volontairement ; les pousser dans cet état retirerait l'audio aux
élèves en production. Le commit se fait **en un bloc, à la fin**, quand le
compte est stable et que `git status` ne montre plus de suppressions.

## Pourquoi 5 556 extraits ont été effacés

La voix « enseignante » a changé d'identifiant. L'ancienne
(`K7gx0ylJdff0yjM2uVQS`) est **abandonnée** ; la nouvelle est
**`mActWQg9kibLro6Z2ouY`**. Mesurée sur une même phrase, l'ancienne sortait à
20,8 caractères par seconde contre 18 à 19 pour les trois autres voix du
dépôt — la plus rapide des quatre, et ralentie à 0,85 elle restait au niveau
des autres non ralenties. La nouvelle débite 17,7 sans traitement, 15,1 une
fois ralentie.

Les générateurs sautant ce qui existe déjà, il fallait effacer pour que la
nouvelle voix soit produite — mais **seulement ce que ce rôle avait produit**,
d'où `build/retirer_voix.py` : 5 556 extraits au lieu des 8 538 qu'un
effacement total aurait fait repayer.

**Trois défauts réglés du même coup**, et c'est la leçon de la journée : les
six lettres de l'exercice d'épellation du niveau 1 sortaient à l'anglaise, et
« brin » se confondait avec « brun » dans l'exercice de `module-achat` qui les
oppose. La nouvelle voix les dit **justes telles quelles**. Seul « I »
résistait, en sortant « ir » ; `TEXT_OVERRIDES` lui envoie `i.` — le point
empêche le modèle de fermer la syllabe. Avant d'écrire une table de
substitution, réécouter avec la voix en service.

## Quatre agents en vol — les quatre derniers modules du programme

| Activité | Slug | `numero` |
|---|---|---|
| 120 | `module-n8-emmenagement` | 3 |
| 121 | `module-n8-habitation` | 4 |
| 122 | `module-n8-actualite` | 5 |
| 123 | `module-n8-oeuvres` | 6 |

Ils ont pour consigne de commiter souvent et de **pousser leur branche sans
fusionner**. Si la limite les a tués, leur travail est dans leurs worktrees :

    ls .claude/worktrees/                                   # les trouver
    for d in .claude/worktrees/agent-*; do (cd $d && git log --oneline -1); done

Les reprendre par `SendMessage` sur leur identifiant, ou relire leur branche.
**Rien de commité n'est perdu** — c'est la règle qui a sauvé quatre agents
cette nuit.

## Fusionner une branche d'agent

Toujours par le script, jamais à la main :

    python3 build/fusionner_module.py worktree-agent-<id>

Il a appris trois choses hier : recoller « le nôtre + la fermeture + le
leur », recoller **deux versions entières d'un même dictionnaire** (le cas des
nuits à plusieurs modules, où chacun rouvre `JEU_DE_ROLE_SCENARIOS`), et
refuser une fusion qui **définirait deux fois** une constante ou une clé —
Python accepterait en silence et le module jouerait le scénario d'un autre.

Après chaque fusion : `python3 build/materiel.py`, puis les sept contrôles de
`CLAUDE.md`.

## Où en est le chantier

Sept niveaux complets sur huit. Il reste **les quatre modules ci-dessus** ;
quand ils sont fusionnés, `python3 build/bilan_programme.py` doit afficher les
huit niveaux complets et **123 activités**, aucune situation du programme sans
son module.

Un écart connu et ancien, qui n'est pas une régression :
`build/controles/pieds_de_page.py` signale `module-n3-horaire`, dont les
seize séances n'ont jamais été produites.

## Ce qui attend une décision de l'utilisateur

- **La planche des images** (`python3 build/planche_images.py`, puis
  `planche-images.html` servi en local) : 501 images d'exercice et 767 de
  vocabulaire, numérotées, à marquer « à refaire » avec leur motif. Aucun
  relevé n'a encore été rendu.
