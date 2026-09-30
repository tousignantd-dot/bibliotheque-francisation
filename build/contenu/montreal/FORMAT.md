# Guide de Montréal — format du contenu

Chaque fichier `lieux_<n>.py` définit `LIEUX = [ {...}, ... ]`. Une entrée :

```python
{
  "id": "schwartz",                 # imposé (voir la liste)
  "cat": "manger",                  # voir | quartier | manger | boire
  "quartier": "Plateau-Mont-Royal", # nom officiel, en français
  "metro": "Saint-Laurent",         # station la plus pratique (nom officiel), ou "" si aucune
  "adresse": "3895, boulevard Saint-Laurent",   # format québécois ; "" pour un quartier
  "geo": (45.5165, -73.5775),       # lat, lon (4 décimales, exactes)
  "duree": 60,                      # minutes conseillées sur place
  "nom":  {"fr": "...", "en": "...", "es": "..."},  # le nom propre ne se traduit que s'il a un usage établi (Old Port, Viejo Puerto)
  "bref": {"fr": "...", "en": "...", "es": "..."},  # une ligne, ≤ 90 caractères, qui donne envie
  "texte": {"fr": "...", "en": "...", "es": "..."}, # LE TEXTE DU GUIDE : 3 courts paragraphes séparés par "\n\n", 130 à 170 mots. Il sera aussi LU À VOIX HAUTE (audioguide) : phrases qui se disent bien, pas de parenthèses, pas d'abréviations, nombres simples.
  "conseil": {"fr": "...", "en": "...", "es": "..."}, # un conseil pratique d'initié, une ou deux phrases
  "commander": {"fr": "...", "en": "...", "es": "..."}, # SEULEMENT pour manger/boire : quoi commander, et la phrase à dire au comptoir
  "anecdote": {"fr": "...", "en": "...", "es": "..."},  # un fait étonnant, une phrase
  "verifier": ["fait à contrôler avant publication", ...]  # en français ; dates, chiffres, propriétaires
}
```

Règles d'écriture
- Ton : un guide chaleureux, vivant, précis — pas une brochure. Vouvoiement en français, « usted » en espagnol.
- Chaque langue est ÉCRITE pour son lecteur, pas traduite mot à mot. Anglais canadien (colour, centre). Espagnol neutre d'Amérique latine (la majorité des touristes hispanophones), compréhensible en Espagne.
- En français : noms et graphies québécois (smoked meat, dépanneur, métro, « la Main »). En anglais et en espagnol, on peut glisser UN mot français local expliqué (ex. « a dépanneur, the corner store »).
- Faits : seulement ce qui est solidement établi. Aucune heure d'ouverture précise, aucun prix exact (dire « comptez environ » seulement si c'est stable et connu, sinon rien). Tout chiffre, date ou nom propre discutable va aussi dans `verifier`.
- Aucun emoji. Guillemets français « » en français, "…" en anglais, « » ou "…" en espagnol (choisir « »).
- Le fichier doit s'importer sans erreur : `python3 -c "import runpy; runpy.run_path('build/contenu/montreal/lieux_1.py')"`.
