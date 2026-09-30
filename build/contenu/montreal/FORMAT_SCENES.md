# Montréal en poche — format des scènes (« Parler »)

Public : touristes ANGLOPHONES et HISPANOPHONES qui veulent se débrouiller en
français à Montréal. Débutants ou faux débutants. L'interface leur parle en
anglais ou en espagnol ; le personnage leur parle en FRANÇAIS QUÉBÉCOIS
naturel mais simple (phrases courtes, une idée par réplique, tournures
réellement entendues à Montréal : « Qu'est-ce que je vous sers ? », « Ce sera
tout ? », « Sur place ou pour emporter ? », « Bonne journée ! » ; le vouvoiement
au comptoir est la norme, le tutoiement spontané d'un serveur jeune est
possible et peut être expliqué).

Chaque fichier `scenes_<n>.py` définit `SCENES = [ {...}, ... ]` :

```python
{
  "id": "schwartz",                   # imposé
  "lieu": "schwartz",                 # id d'un lieu du guide, ou None (scène générale)
  "titre": {"fr": "...", "en": "...", "es": "..."},   # ex. « Commander un smoked meat »
  "but":   {"fr": "...", "en": "...", "es": "..."},   # l'objectif, une phrase : « Order a medium smoked meat sandwich and a pickle, to eat here. »
  "perso": {"nom": "Le serveur", "voix": "thierry"},   # voix : sylvie | thierry (HD, à préférer) | jean | antoine
  "tours": [
    # Réplique du personnage : le texte français, et son sens en anglais et en espagnol.
    {"dit": "Bonjour ! Qu'est-ce que je vous sers ?",
     "sens": {"en": "Hi! What can I get you?", "es": "¡Hola! ¿Qué le sirvo?"}},
    # Tour de l'apprenant : TROIS choix. Le PREMIER est la bonne réponse (rétroaction None) ;
    # les deux autres sont des erreurs PLAUSIBLES d'un anglophone ou d'un hispanophone, chacune
    # avec une rétroaction courte et bienveillante qui dit pourquoi (en fr, en, es).
    {"choix": [
      ["Un smoked meat medium, s'il vous plaît.", {"en": "...", "es": "..."}, None],
      ["Je veux un smoked meat.", {"en": "...", "es": "..."},
       {"fr": "...", "en": "Understood, but « je veux » sounds abrupt at a counter: add « s'il vous plaît » or say « Je vais prendre… ».", "es": "..."}],
      ["...", {...}, {...}],
    ]},
    ...
  ],
  "phrases": [   # 3 à 5 phrases à retenir (tirées de la scène), avec leur sens
    ["Je vais prendre un café, s'il vous plaît.", {"en": "...", "es": "..."}],
  ],
  "note": {"fr": "...", "en": "...", "es": "..."},   # une note culturelle, 1-2 phrases (ex. dîner = lunch au Québec)
}
```

Règles
- 6 à 9 tours par scène, qui ALTERNENT personnage / apprenant, en commençant par le personnage
  et en finissant par une réplique du personnage (« Bonne journée ! »). 3 ou 4 tours d'apprenant.
- Les mauvais choix enseignent quelque chose de vrai : faux amis (« Je suis plein », « librairie »),
  anglicismes ou calques de l'espagnol, registre (tu/vous, « je veux »), mot du Québec
  (« dîner » = lunch, « breuvage », « pour emporter »), chiffre ou prix mal compris.
  Jamais de choix absurde. Aucune rétroaction moqueuse.
- Les trois choix ont des longueurs proches (le bon ne doit pas se deviner à sa longueur).
- Les répliques françaises sont LUES PAR UNE SYNTHÈSE VOCALE : pas de parenthèses, pas d'abréviations,
  nombres et prix écrits en lettres (« quatorze dollars cinquante »), ponctuation normale.
- Aucun prix réel précis d'un commerce réel : un montant plausible, présenté comme tel.
- Aucun emoji. Guillemets « » en français, “ ” en anglais, « » en espagnol.
- Le fichier doit s'importer : `python3 -c "import runpy; runpy.run_path('build/contenu/montreal/scenes_1.py')"`.
