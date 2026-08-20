# Sauvegardes — commande Météo (19 août 2026)

Copies déplacées ici d'un scratchpad de session, qui allait disparaître.

## Les trois JSON

`activities.json`, `depots.json` et `materiel.json` tels qu'ils étaient à
22 h 18 min 05 s, juste avant une écriture directe sur disque.

Contexte : l'activité 47 (« Qu'est-ce qu'une tornade ? », commande
`7504148e1ff2`) avait déjà été publiée avant que trois défauts soient corrigés
— fiches en markdown au lieu de PDF, deux MP3 à l'accent espagnol, copie
publiée périmée. `POST /api/forge/publier` refuse à dessein de republier une
commande déjà publiée ; les fichiers ont donc été recopiés à la main et les
trois JSON modifiés directement, en contournant le serveur qui tournait. Ces
copies sont le filet de cette opération.

## essais-voix/

Les six essais de prononciation soumis à l'oreille. Un mot isolé qui existe
dans une autre langue en prend l'accent ; le seul levier est l'orthographe,
car `eleven_multilingual_v2` n'accepte ni `<phoneme>` ni `language_code`.

| fichier | texte envoyé à ElevenLabs |
|---|---|
| `*-original.mp3` | `un abri` / `la radio` — accent espagnol, le défaut d'origine |
| `*-a.mp3` | `un abris` / `la radiot` |
| `*-b.mp3` | `un abrit` / `la radiau` |

**Les deux B ont été retenus.** La graphie figée vit dans `PRONONCIATION`, au
milieu de `activites/commandes/7504148e1ff2/generer_audio.py`. Les MP3 servis
à l'élève sont une lecture ultérieure de cette même graphie, pas ces
fichiers-ci : ElevenLabs ne rend jamais deux fois la même chose.
