# Plusieurs clients, et qui paie quoi

Réflexion du 24 août 2026. Rien n'est encore construit : ce document fixe les
décisions à prendre **avant** d'écrire une ligne, parce que trois d'entre elles
sont irréversibles une fois qu'un deuxième centre de services est branché.

La question posée : plusieurs centres de services scolaires, donc plusieurs
clients ; des coûts d'API (ElevenLabs, Anthropic) qui montent avec l'usage ; un
tableau de bord où le client voit sa dépense en direct ; et un pourcentage de
gestion prélevé au passage, qui rentabilise le projet.

Les trois premières parties sont techniques et se répondent proprement. La
quatrième — le pourcentage — est celle où la réponse honnête n'est pas celle
qui était attendue.

---

## 1. Où insérer le client dans la hiérarchie

Aujourd'hui : **enseignant → groupes → élèves**, avec un rôle `admin` qui voit
*tous* les groupes et un compte fondateur au-dessus. Ce modèle tient parce
qu'il n'y a qu'un seul établissement : « tous les groupes » et « les groupes de
mon centre » sont la même chose.

Avec deux clients, ils cessent de l'être, et un `admin` du CSS Marie-Victorin
voit les élèves du CSS de Laval. Ce n'est pas une gêne d'affichage : ce sont des
renseignements personnels d'élèves de deux organismes distincts.

Il faut donc un étage de plus, et **un seul** :

```
plateforme (moi)
└── organisation        ← le client, et l'unité de facturation
    └── enseignant
        └── groupe
            └── élève
```

Quatre rôles, contre trois aujourd'hui :

| Rôle | Ce qu'il peut |
|---|---|
| `fondateur` | tout, sur toutes les organisations ; ouvre une organisation, fixe les tarifs et les plafonds |
| `admin_org` | son organisation seulement : ouvre des comptes enseignants, voit **ses** dépenses, demande un plafond |
| `prof` | ses groupes |
| élève | son code à six caractères — pas de compte |

Le point à ne pas manquer : `admin` d'aujourd'hui devient `admin_org`, et son
pouvoir se **réduit** en même temps qu'un étage apparaît au-dessus. La règle du
fondateur déjà en place (`founder_id()`, trois refus en 403) se transpose telle
quelle d'un cran plus haut : un `admin_org` n'ouvre pas de compte `admin_org`,
et ne touche pas au compte fondateur.

**La migration se fait comme `migrate_multi_groupes()`** : au démarrage,
idempotente, elle crée l'organisation historique, y range les enseignants, les
groupes et les élèves existants. Le jour où on la lance avec une seule
organisation, **rien ne change à l'écran** — et tout est prêt. C'est l'étape
qu'il faut faire tôt et sans client, pas tard et sous pression.

## 2. Ce qui est commun, et ce qui est cloisonné

C'est la décision qui fait l'économie du projet, et elle est déjà prise à
moitié : *« Le catalogue d'activités est **commun** à tous les enseignants ; ce
qui appartient au groupe, c'est la planification. »*

Elle monte d'un cran sans rien changer d'autre :

| Commun à tous les clients | Propre à une organisation |
|---|---|
| `activities.json`, `sections.json`, `materiel.json` | `teachers`, `groups`, `students` |
| les modules, les MP3, les présentations, les fiches | `schedule`, `progress`, `access_log` |
| le cache de voix et le cache d'outils | productions orales et écrites, `corrige_moi` |
| le banc de vocabulaire (`VOCAB_BANK`) | documents de groupe, promotions, signalements |

Le contenu est produit **une fois** et amorti sur tous les clients : vingt et un
modules, 8 538 extraits audio, 3 835 diapositives. C'est là qu'est la valeur, et
c'est ce que le modèle d'affaires devra facturer — j'y reviens.

Deux conséquences qui ne sautent pas aux yeux :

- **Le code élève reste globalement unique.** Six caractères, 36⁶ ≈ 2 milliards
  de combinaisons : la place ne manque pas. Mais toute route qui reçoit un code
  doit déduire l'organisation **de l'élève**, jamais d'un paramètre d'URL. Un
  `?organisationId=` accepté sur parole est la faille de cloisonnement classique.
- **Le cache est partagé, et c'est voulu.** Quand le client B demande une lecture
  déjà payée par le client A, elle est servie gratuitement. Ne pas cloisonner le
  cache par organisation : ce serait payer deux fois le même MP3. La règle de
  comptabilité qui va avec est en §5.

## 3. Compter les coûts : quatre points d'appel, pas un de plus

Bonne nouvelle, et elle n'était pas acquise : **tout ce qui se paie passe
aujourd'hui par quatre endroits.**

| Ce qui coûte | Où | Combien d'appelants |
|---|---|---|
| Anthropic (JSON) | `Handler._call_anthropic_json`, `server.py:16070` | 11 |
| Anthropic (dialogue) | `Handler._call_anthropic_dialogue`, `server.py:15651` | 2 |
| ElevenLabs | `/api/voix`, `server.py:15822` | 1 |
| Anthropic (tri des signalements) | `triage_signalement`, `server.py:1820` | 1, en fil de fond |

Instrumenter coûte donc **quatre insertions**, pas quinze. Le quatrième est le
piège : il a son appel HTTP à lui, écrit avant les deux fonctions communes. Si
on l'oublie, il facture à personne — et comme il tourne en arrière-plan sans
rien afficher, personne ne le remarquera.

Les générateurs `generer_audio_*.py` sont **hors registre** : ils tournent sur
le poste local, à ma charge, pour produire le contenu commun. Les compter dans
la facture d'un client reviendrait à lui faire payer un module dont les dix
autres profitent.

## 4. Ce que le registre enregistre

**Une ligne par appel payant.** Et la règle qui vaut pour tout le reste :

> On enregistre des **unités physiques** — jetons, caractères. Le prix est
> appliqué **à la lecture**, depuis une table de tarifs versionnée dans le code.

Ce n'est pas de la coquetterie. Un tarif mal noté se corrige alors sans perdre
une seule mesure, et un changement de prix fournisseur ne réécrit pas
rétroactivement la facture du mois dernier. La table porte une date d'entrée en
vigueur ; une ligne d'août garde le prix d'août. Sans cette règle, relire la
facture de janvier en juin donne un autre chiffre qu'en janvier — et il est
impossible d'expliquer à un client pourquoi.

```json
{ "ts": "2026-08-24T19:12:03Z", "organisationId": 1, "groupId": "g3",
  "enseignantId": 2, "code": "K7M2QP",
  "service": "elevenlabs", "route": "/api/voix", "modele": "eleven_multilingual_v2",
  "caracteres": 187, "jetonsIn": 0, "jetonsCache": 0, "jetonsOut": 0,
  "cache": false }
```

Pour Anthropic, **le coût est exact, pas estimé** : la réponse porte déjà son
`usage` (`input_tokens`, `cache_read_input_tokens`, `output_tokens`) et
`_call_anthropic_dialogue` l'imprime déjà au journal, ligne 15717. Rien à
deviner — contrairement à `forge.py`, qui doit estimer les jetons de sortie
d'après les caractères émis parce que le coût réel n'arrive qu'à la fin.

Pour ElevenLabs, la facturation est au caractère et `len(texte)` est connu
**avant** l'appel. Exact aussi.

**Le registre n'est pas un fichier JSON.** C'est le seul endroit de ce projet où
il ne faut pas suivre l'habitude de la maison. `_save_json()` (ligne 683)
réécrit le fichier entier et **n'a aucun verrou** ; le serveur tourne en
`ThreadingMixIn` depuis l'ajout de « Corrige-moi ! ». Deux élèves qui cliquent
« lire » dans la même seconde écrivent chacun leur version complète du fichier,
et la seconde efface la première. Sur un cache, une perte est bénigne : on
repaie l'extrait. Sur un registre de facturation, c'est une ligne de revenu qui
disparaît sans trace, et c'est irréparable après coup.

`sqlite3` est dans la bibliothèque standard — la règle « stdlib seulement » de
ce dépôt tient. Un `INSERT` par appel, `WAL` activé, et la concurrence est
réglée sans y penser. `data/couts.sqlite` sur le volume, non versionné.

## 5. Ce que le cache change à la comptabilité

Un appel servi par le cache **coûte zéro et s'inscrit quand même**, marqué
`cache: true`.

Sans cette ligne, le client ne voit pas ce que le cache lui épargne — et c'est
précisément l'argument qui justifie qu'on facture une gestion. Le tableau de
bord peut alors dire : *« 4 312 lectures servies, dont 3 980 sans frais »*. Ce
chiffre-là vaut plus qu'une remise.

La règle de partage, en une phrase : **le paiement est compté une fois, à celui
qui a déclenché l'appel ; l'économie est comptée à chacun de ceux qui en
profitent.** Les deux colonnes ne s'additionnent donc pas entre organisations,
et c'est normal — il faut l'écrire sur l'écran, sinon deux clients réclameront
la même économie.

## 6. Le tableau de bord

Deux fois la même page, deux portées : l'`admin_org` voit son organisation, le
fondateur voit toutes les organisations et sa marge.

Ce qu'elle porte, dans cet ordre :

1. **Trois chiffres** — dépense du mois, projection à la fin du mois, part du
   forfait consommée. Comme le bilan en trois chiffres du portail élève.
2. **La ventilation par service** — la voix et la correction sont deux leviers
   distincts, et l'ordre de grandeur les sépare franchement (§7).
3. **Par groupe et par enseignant** — c'est ce qui permet à une direction de
   comprendre, et le seul niveau de détail légitime. Descendre jusqu'à l'élève
   nommé ferait un tableau de surveillance des enfants ; on n'y va pas.
4. **La courbe des jours du mois** — un dépassement se voit à sa pente, jamais
   à son total.
5. **Ce que le cache a épargné.**

**« En direct » veut dire « à la minute », et il faut le dire ainsi.** Le
registre est écrit au moment de l'appel ; la page se rafraîchit toute seule
chaque minute. Pas de WebSocket, pas de flux poussé : ni la banque ni le
fournisseur d'électricité n'en offrent, et personne ne le leur reproche. Promettre
le temps réel pour livrer une minute de retard est une déception gratuite.

**L'écriture au registre ne doit jamais faire échouer la réponse à l'élève.**
Même règle que le signalement, qui écrit sa fiche puis répond, et laisse le tri
et le courriel à un fil de fond. Une base pleine ne doit pas casser une classe.

## 7. Les plafonds, et pourquoi ils ne sont pas négociables

C'est ma carte de crédit qui paie ElevenLabs et Anthropic, un mois avant que le
client soit facturé. Un module en boucle, une classe enthousiaste, un script
d'élève curieux : le trou est pour moi.

Chaque organisation porte donc un plafond mensuel, et le dépassement se dégrade
au lieu de couper :

- à **80 %**, l'`admin_org` reçoit un avertissement à l'écran et par courriel
  (la chaîne Resend existe déjà) ;
- à **100 %**, les appels neufs s'arrêtent, **mais le cache continue de
  servir** — une classe qui relit un module déjà lu ne s'aperçoit de rien ;
- **jamais de message d'erreur qui parle d'argent à un élève.** Il voit le même
  503 propre que quand la clé manque : « la voix est momentanément
  indisponible ». Un élève qui hésite à cliquer sur « lire » parce que ça coûte
  est un échec pédagogique, pas une économie.

## 8. Le pourcentage : ce qu'il ne peut pas faire

Voici l'arithmétique, avec les ordres de grandeur d'aujourd'hui. Les prix
d'ElevenLabs varient selon le forfait et sont à confirmer ; ceux d'Anthropic
pour Haiku 4.5 sont de 1 $ par million de jetons d'entrée et 5 $ en sortie.

| Geste | Unités | Coût |
|---|---|---|
| une correction « Corrige-moi ! » | ~700 jetons entrée, 150 sortie | ~0,15 ¢ |
| une lecture de consigne à voix haute | ~180 caractères | ~3 ¢ |

**Une lecture à voix haute coûte ce que coûtent vingt corrections par l'IA.** Le
`CLAUDE.md` le disait déjà — *« c'est le plus gros poste de la facture d'API »*
— et le tableau de bord doit s'ouvrir là-dessus, pas sur le total.

Montons à l'échelle d'un client. Un CSS avec vingt groupes de vingt-cinq élèves,
usage soutenu, **avant cache** : de l'ordre de 500 $ par mois. Après cache — et
le cache est efficace, trente élèves surlignent les mêmes consignes — plutôt
150 à 250 $.

À 15 % de gestion, cela fait **entre 22 $ et 75 $ par mois** pour ce client.
Environ 500 $ par an. Pour un centre de services scolaire entier.

Trois choses en découlent, et aucune n'est une opinion :

1. **Le montant ne rentabilise rien.** Le coût réel de cette plateforme n'est pas
   l'API : c'est le temps de production. Vingt et un modules, 8 538 extraits
   audio déjà payés, 3 835 diapositives, une chaîne de fabrication complète.
   Prélever un pourcentage sur l'API, c'est facturer l'accessoire et donner le
   principal gratuitement.
2. **Le modèle est désaligné.** Il paie plus quand ça coûte plus cher. Chaque
   MP3 mis en cache, chaque prompt raccourci, chaque optimisation réduit le
   revenu. Le cache de voix — une des meilleures idées techniques du projet —
   coûte de l'argent sous ce modèle. Un modèle d'affaires qui punit le bon
   travail d'ingénierie finit toujours par l'obtenir.
3. **Il est difficile à acheter.** Un centre de services scolaire est un acheteur
   public : il vote un budget, émet un bon de commande, signe pour un montant.
   « On vous facturera ce que ça aura coûté, plus 15 % » n'entre pas dans cette
   case. « 12 $ par élève par session » y entre trivialement.

## 9. Ce que je recommande à la place

Garder l'idée — la refacturation à coût majoré est juste — mais lui donner la
place qui est la sienne : **le dépassement, pas la base.**

**Trois étages :**

1. **Une licence par élève actif et par session.** C'est ce qui paie le contenu,
   les mises à jour, l'hébergement et le soutien. C'est le gros du revenu, et
   il est prévisible des deux côtés — le client peut le budgéter, moi je peux
   compter dessus.
2. **Un usage compris dans la licence.** Un quota mensuel de voix et de
   correction par élève, calibré pour que **neuf groupes sur dix n'en sortent
   jamais**. Le quota se fixe une fois le registre en place, pas avant : c'est la
   raison la plus concrète de construire l'étape 0 dès maintenant.
3. **Le dépassement refacturé à coût majoré.** Là, et là seulement, le
   pourcentage est légitime : il paie l'avance de trésorerie, le suivi et le
   risque. Et il est facile à défendre, parce que le tableau de bord montre
   exactement d'où il vient.

Ce que ça change :

- Le tableau de bord devient **plus** nécessaire, pas moins : c'est lui qui
  justifie le dépassement, et qui donne au client le moyen de l'éviter.
- Les intérêts se réalignent. Un quota inclus rend chaque optimisation
  directement profitable : le cache travaille pour moi au lieu de contre moi.
- Le client signe un montant annuel. C'est la condition d'entrée chez un
  acheteur public, pas une préférence.

## 10. Chemin de mise en œuvre

L'ordre compte plus que le contenu, et la première étape n'attend aucun client.

**Étape 0 — le registre.** Instrumenter les quatre points d'appel, écrire
`data/couts.sqlite`, ajouter un écran « Dépenses » visible du fondateur seul.
Utile même avec un seul établissement : c'est ce qui donne le **coût réel par
élève et par mois**, sans lequel aucun prix ne peut être fixé. Un jour de
travail, et c'est la seule étape dont le résultat est immédiatement exploitable.

**Étape 1 — le cloisonnement.** `organisationId` sur les enseignants, les
groupes, les élèves ; migration idempotente au démarrage ; filtres dans
`groups_of_teacher()` et partout où un `admin` voit « tous ». Aucun écran neuf,
rien qui change à l'usage. À faire pendant qu'il n'y a qu'une organisation :
c'est cent fois moins cher que sous le regard d'un deuxième client.

**Étape 2 — l'écran client.** Le tableau de bord de la §6, les plafonds de la
§7, l'alerte à 80 %.

**Étape 3 — le contrat.** Quotas, dépassement, facture mensuelle en PDF. La
chaîne d'impression existe déjà : `fiche_pdf.py` rend un format lettre par
Chrome sans interface et refuse tout ce qui ne fait pas 612 × 792 pt.

**Étape 4 — l'isolement des données**, quand le nombre d'organisations le
demande : partition par organisation, ou passage à SQLite pour la progression
et le journal. `progress.json` réécrit en entier à chaque événement tiendra
mal à cinq cents élèves de trois centres.

## 11. Ce qui n'est pas technique et bloquera quand même

- **La Loi 25.** Dès le deuxième organisme, la plateforme héberge des
  renseignements personnels d'élèves pour le compte de tiers. Un CSS demandera
  une entente de traitement, une politique de conservation, un registre des
  incidents, et posera la question de l'hébergement des données hors Québec.
  Railway déploie par région : c'est un réglage aujourd'hui, une renégociation
  de contrat plus tard. À regarder **avant** le premier appel d'offres, pas
  pendant.
- **La trésorerie.** Je paie les fournisseurs le mois M, le client paie à 30 ou
  60 jours. Avec plusieurs clients, c'est du fonds de roulement réel. Le quota
  prépayé de la §9 règle ça au passage — c'est même son deuxième mérite.
- **Le soutien.** Un pourcentage sur l'API ne finance aucune heure de soutien, et
  c'est ce que le client appellera en premier.

## 12. Pièges propres à ce dépôt

- **`init_storage()` et `USER_FIELDS`** : pour les activités, le volume gagne sur
  le code. La table des **tarifs** doit vivre dans le code, versionnée, jamais
  dans le volume — sinon un redéploiement peut ramener un prix périmé sans que
  rien ne le dise. Le **registre**, lui, est une donnée : volume, non versionné.
- **`_save_json()` n'a pas de verrou** et le serveur est multi-fils. Voir §4 :
  c'est la raison technique du choix de SQLite, pas une préférence.
- **Le cache de voix est plafonné à 300 Mo avec élagage des moins récents.** Avec
  plusieurs organisations, il se remplit plus vite et l'élagage frappe plus
  souvent : le taux de service par le cache baissera, donc le coût par élève
  montera. Le plafond est à relever **avant** le deuxième client, pas après —
  et le tableau de bord le rendra visible, ce qui vaut mieux qu'une surprise.
- **`triage_signalement()` a son propre appel HTTP.** Voir §3 : c'est celui qu'on
  oublie.
- **Ne jamais exposer un coût à un élève**, ni dans une interface, ni dans un
  message d'erreur. Voir §7.
