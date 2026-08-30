# Écrire un point express

Le contrat d'écriture d'un **point express** : dix minutes, une seule
difficulté, envoyé par l'enseignant à l'élève chez qui il a vu la lacune.

Ce fichier existe parce que plusieurs personnes en écrivent en parallèle. Sans
lui, on obtient autant de voix que d'auteurs — et la chose qui distingue un
point express d'une mini-leçon est précisément une manière de faire, pas un
sujet.

Lire d'abord **deux exemples finis** :
`build/parcours/heure-et-date.js` (avec extraits sonores) et
`build/parcours/passe-compose-etre-avoir.js` (sans son).

---

## 1. La règle qui commande tout : ce n'est pas une leçon

**L'élève a déjà lu la mini-leçon.** Nos modules en portent 168 ; huit traitent
le passé composé, six l'heure, six l'imparfait. Un élève envoyé sur un point
express en a très probablement lu deux sur le même sujet. **Redire la même
chose autrement ne sert à rien.**

Avant d'écrire, relever ce qui existe déjà sur le sujet :

```
grep -l "votre sujet" build/contenu/*/plus.js
grep -n "eye:'Mini-leçon', tit:" build/contenu/*/plus.js | grep -i "votre sujet"
```

Puis en lire une en entier, et s'en écarter sur **les cinq points** :

| | La mini-leçon | Le point express |
|---|---|---|
| L'ordre | la règle, puis l'application | **des cas tranchés, PUIS la règle** |
| L'étendue | exhaustive, consultable | **partielle** : un test réutilisable, les cas fréquents |
| Le métalangage | en tête | **après** avoir manipulé la chose |
| Les exemples | ceux du module | pris à **plusieurs** situations |
| L'erreur | sanctionnée | **c'est l'enseignement** |
| Le geste | elle se lit | il **se traverse** |

Concrètement :

- **Aucune règle avant l'écran 3 ou 4.** Les deux ou trois premiers écrans font
  trancher. La règle est ensuite écrite **comme un constat de ce que l'élève
  vient de faire** — « vous avez séparé les déplacements du reste », « vous
  n'avez pas converti, vous avez comparé ».
- **Jamais la liste complète.** La mini-leçon du passé composé donne les quinze
  verbes en tableau ; le point express donne **un test** — « est-ce que
  quelqu'un change d'endroit ou d'état ? » — qui marche sur un verbe jamais vu.
  Une liste s'oublie, un test se réemploie.
- **Le cas par défaut se dit en dernier.** Nommer « avoir » d'entrée fait croire
  à deux règles ; il n'y en a qu'une et une exception.
- **Aucune phrase reprise** d'une mini-leçon, et des exemples pris à plusieurs
  situations — une note à l'école, un message à un employeur, un texto. Un point
  express ne dépend d'aucun module : l'élève doit reconnaître la faute partout.

---

## 2. La forme : dix écrans, trois types

Un point express fait **8 à 12 écrans**, dix de préférence, et se joue en dix
minutes. Le rythme qui marche, éprouvé sur six points :

1. **verif** — une question, sans qu'aucune règle n'ait été donnée. La consigne
   le dit : « Répondez avec ce que vous savez déjà — c'est fait exprès. »
2. **notion** ou **tri** — on écoute, ou on tranche des cas.
3. **tri** — le cœur : ranger six à huit cas en deux ou trois colonnes.
4. **notion** — la règle, écrite comme un constat. Le métalangage arrive ici.
5–8. **verif** et **notion** en alternance — le piège, le cas fréquent, la
   variante qui trompe.
9. **verif** — écrire, pas reconnaître.
10. **verif** — **la fermeture reprend le cas de l'écran 1**. L'élève mesure ce
    qu'il a appris sur la question qu'il a ratée en arrivant.

### Les trois types, et ce qu'ils exigent

```js
{ id:'…', type:'notion', eye:'…', menu:'…', titre:'…',
  paras:['…','…'],                    // du HTML léger : <b> <i> &nbsp;
  sons:[{fichier:'t1/line_13_manon.mp3', qui:'…', texte:'…'}],   // facultatif
  retenir:'…', attente:'Lisez, puis continuez.' }

{ id:'…', type:'verif', eye:'…', menu:'…', titre:'…', consigne:'…',
  sons:[…],                                                       // facultatif
  options:[ {txt:'…', juste:true},
            {txt:'…', rat_t:'le titre du rattrapage', rat:'…pourquoi c\'était tentant…'} ],
  pourquoi:'…', attente:'Choisissez une réponse pour continuer.' }

{ id:'…', type:'tri', eye:'…', menu:'…', titre:'…', consigne:'…',
  colonnes:[{id:'a', t:'Nom de la colonne', b:'Texte du bouton'}, …],
  items:[{txt:'le cas', sous:'précision facultative', ok:'a',
          rat:'…pourquoi ce n\'est pas cette colonne…',
          pourquoi:'…la note verte quand c\'est juste…'}],
  attente:'Tranchez les six cas pour continuer.' }
```

**Chaque mauvaise option veut son `rat`**, et chaque cas de tri aussi : le
rattrapage explique **pourquoi la mauvaise réponse était tentante**, jamais
« faux, essaie encore ». C'est là qu'est l'enseignement. La construction refuse
un écran qui en manque un.

**Le ton.** Vouvoiement, phrases courtes, aucun mot que le niveau visé ne
connaît pas. On s'adresse à un adulte : ni « bravo ! », ni émoji, ni
familiarité. On peut être direct — « c'est la faute qui coûte le
rendez-vous » — jamais condescendant.

---

## 3. Les sons : rejoués, jamais produits

**Coût média : zéro.** Un point express rejoue les extraits déjà produits pour
les modules, par leur chemin, et n'en copie aucun. `PARCOURS.module` dit d'où
ils viennent.

**Un extrait ne se cite jamais de mémoire.** Le rang du fichier est celui de la
réplique dans `dialogues.js`, à partir de 1 :

```
python3 - <<'PY'
import re, pathlib
s = pathlib.Path('build/contenu/module-nX-slug/dialogues.js').read_text(encoding='utf-8')
for cle in re.findall(r"^  (\w+): \{", s, re.M):
    bloc = s.split(cle + ': {')[1].split('lines: [')[1]
    for i, m in enumerate(re.finditer(r'\["([A-ZÉÈÀ\s]+)","(.*?)"\]', bloc), 1):
        print('%s/line_%02d_%s.mp3  %s' % (cle, i, m.group(1).lower().replace(' ','_'), m.group(2)[:70]))
PY
```

Puis **vérifier que le fichier existe** :
`ls assets/interactive/<module>/<t1>/line_13_manon.mp3`

La construction refuse un extrait absent du disque — mais un extrait qui existe
et ne dit pas ce qu'on annonce passe, lui, sans rien signaler. Recopier le
texte exact dans le champ `texte`.

**Un point express peut n'avoir aucun son**, et c'est parfois la bonne réponse :
l'accord du participe passé ne s'entend pas, et c'est le sujet même du point.

---

## 4. Construire et vérifier

```
python3 build/storyline.py <slug>        # UNIQUEMENT le sien
```

**Ne jamais lancer `--tous`** quand plusieurs personnes travaillent : il
réécrit le registre partagé `data/points_express.json`.

**Ne jamais éditer le HTML produit** — la prochaine construction l'écrase.

La construction refuse ce qui casserait chez l'élève : type inconnu,
identifiant en double, vérification sans bonne réponse ou sans rattrapage,
colonne inexistante, extrait absent. **Elle n'écrit rien tant qu'il reste un
écart.**

Puis **le jouer**, dans le navigateur, écran par écran et dans les deux
chemins. Le contrôle qui vaut, dans la console de la page :

```js
const E = __storyline.ecrans; __storyline.remettre();
for (let i = 0; i < E.length; i++) {
  __storyline.aller(i); await new Promise(r => setTimeout(r, 50));
  const e = E[i];
  if (e.type === 'verif') {
    const b = [...document.querySelectorAll('.choix button')];
    b[e.options.findIndex(o => !o.juste)].click();      // une erreur d'abord
    console.assert(document.querySelector('.rattrap h4'), 'pas de rattrapage écran ' + (i+1));
    document.querySelector('.rattrap .encore').click();
    [...document.querySelectorAll('.choix button')][e.options.findIndex(o => o.juste)].click();
  } else if (e.type === 'tri') {
    [...document.querySelectorAll('.tri__l')].forEach((x, k) => {
      const ic = e.colonnes.findIndex(c => c.id === e.items[k].ok);
      x.querySelectorAll('.tri__c button')[ic].click();
    });
  }
  console.assert(!document.querySelector('.pied .btn').disabled, 'bloqué écran ' + (i+1));
}
```

---

## 5. Ce qu'on n'écrit pas

- **Rien qui demande une IA pour être corrigé.** Un point express doit tourner
  dans un centre en mode sans assistant. Pas de texte libre jugé par un modèle :
  des choix, des tris, des comparaisons de chaînes.
- **Aucun contenu copié** d'un manuel. Le programme donne la spécification, le
  contenu s'invente. Voir la règle du dépôt sur le contenu inventé.
- **Aucun vrai nom d'élève**, aucune photo, aucun émoji.
- **Aucune couleur en dur** : le gabarit porte l'habillage, le contenu porte le
  texte.

---

## 6. En-tête du fichier

Le fichier commence par un commentaire qui dit **de quoi il s'écarte et
pourquoi** — quelles mini-leçons existent déjà sur ce sujet, et comment ce
point express procède autrement. C'est ce qui permet à la personne suivante de
ne pas refaire la même chose. Voir les deux exemples.

Puis :

```js
const PARCOURS = {
  slug:     'kebab-case',
  module:   'module-nX-slug',      // seulement si on rejoue ses extraits
  titre:    "Le titre, tel que l'enseignant le lira dans l'étagère",
  surtitre: "Point express · 10 minutes",
  niveau:   5,
  savoir:   'nX-sYY',              // ou 'lexique · repère culturel'
};

const ECRANS = [ … ];
```
