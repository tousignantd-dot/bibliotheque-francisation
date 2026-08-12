# Francisation — comment construire avec ce système

Système visuel des modules interactifs de francisation pour adultes (FLS niveau 4, français
québécois). Produit pédagogique, pas une marque : **la lisibilité passe avant l'expression
visuelle, toujours.** Écrivez toute l'interface en français, au **vous**, sans émoji.

## Mise en place

**Aucun provider, aucun contexte, aucun thème à initialiser.** Importez les composants et
liez `styles.css` — c'est tout. `styles.css` charge les jetons, le socle et le CSS des
composants ; sans lui, tout s'affiche en police et en couleurs du navigateur.

Enveloppez la page dans `Page` puis `Conteneur` : `Page` pose le fond neutre chaud et l'encre,
`Conteneur` la colonne de 1000 px et la gouttière. Un module suit toujours quatre niveaux, dans
cet ordre : `Bande` (en-tête clair — **jamais noir**) → `BarreParcours` + `Etape` (collante) →
`Exercice` (pastille numérotée, sur-titre, titre, consigne, score) → contenu en `Carte` blanches.

## Cinq règles non négociables

| Règle | Valeur |
|---|---|
| Corps de texte | ≥ 17 px (`--fs-body-sm`) — jamais 15 px pour un énoncé |
| Cibles tactiles | ≥ 44 px (`--tap-min`), 48 px de confort (`--tap-comfort`) |
| Contraste | ≥ 4.5:1, libellés secondaires compris |
| Focus clavier | visible partout — ne jamais retirer `:focus-visible` |
| Couleur | jamais porteuse d'information seule : toujours un glyphe ou un mot en plus |

Corollaire : tout ce qui se fait à la souris doit se faire au clavier. C'est pourquoi
l'association `Jeton` se fait par clic-clic, jamais par glisser-déposer.

## L'idiome de style

Composants React pour les pièces, **classes CSS du système pour votre propre mise en page** — et
jamais de valeur en dur quand un jeton existe (`#0A8F5B` s'écrit `var(--accent)`).

| Famille | Noms réels |
|---|---|
| Mise en page | `.container` `.stack` (12 px) `.stack-l` (48 px) `.grid-auto` `.page` |
| Espacement | `--sp-1` 4 · `--sp-2` 8 · `--sp-3` 12 · `--sp-4` 16 · `--sp-5` 20 · `--sp-6` 24 · `--sp-8` 32 · `--sp-12` 48 — aucune valeur intermédiaire |
| Corps | `--fs-hero` `--fs-h2` 30 · `--fs-h3` 24 · `--fs-lead` 19 · `--fs-body` 18 · `--fs-body-sm` 17 · `--fs-ui` 15 · `--fs-label` 13 |
| Graisses | `--fw-medium` 600 · `--fw-semi` 700 · `--fw-bold` 800 · `--fw-black` 900 |
| Surfaces | `--surface-page` `--surface-card` `--surface-sunken` `--surface-band` |
| Texte | `--text-strong` `--text-body` `--text-muted` `--text-accent` |
| Accent unique | `--accent` `--accent-soft` `--accent-ink` — un seul vert |
| Rétroaction | `--ok-bg/-line/-ink` · `--no-*` · `--warn-*` |
| Section | `--sec` et `--sec-soft`, posés par `Exercice section="orale|phonie|ecriture|ecoute|vocab"` |
| Rayons | `--r-sm` 10 · `--r-md` 14 · `--r-lg` 18 · `--r-pill` |

Trois interdits, par ordre d'importance :

1. **Aucun système de marque externe.** En particulier jamais de palette jaune-noir
   industrielle (« SLB ») : elle a été explicitement rejetée par le client.
2. **Le rouge (`--audio`) est réservé à l'audio** — `Bouton variante="audio"` et `BoutonAudio`.
   L'erreur n'a pas d'aplat saturé : fond à peine teinté, filet et texte rouges.
3. **Sélectionné = plaque encre** (`--sel-bg` #17181A, texte blanc), jamais une teinte de plus.
   La couleur reste ainsi disponible pour dire « juste » ou « à revoir ».

Les couleurs de section ne servent qu'au repérage, à quatre endroits seulement : pastille
numérotée, sur-titre, filet gauche de 4 px, point de la barre de parcours. Aucun dégradé, aucune
texture, aucune illustration décorative. Un seul bloc foncé par page au maximum, jamais l'en-tête.

## Le ton

Phrases courtes, un fait par phrase. Casse normale : les majuscules ne servent qu'aux sur-titres
de 13 px. Titres d'exercice dans la voix de l'apprenant (« Je complète avec le bon son »).
Consigne = une phrase grise sous le titre. Rétroaction brève et factuelle : « ✓ Juste »,
« ✕ La bonne réponse est FAUX » — ni félicitation exagérée, ni jugement. L'article fait partie du
mot de vocabulaire (« un retard »). Québécois : « courriel », « superviseur », `15 h`, `9 h 30`.

## Où est la vérité

Lisez `_ds/<dossier>/styles.css` et les fichiers qu'il importe (`tokens/`, `components/`) avant
de styler quoi que ce soit — c'est la source, pas ce résumé. Chaque composant a son
`<Nom>.prompt.md` et son `<Nom>.d.ts`.

## Exemple

```jsx
<Page>
  <Bande surtitre="Module 4 · Le monde du travail" titre="Absent ou en retard : que faire ?"
         chapeau="Écoutez l'appel de Karim, puis répondez aux questions." />
  <Conteneur>
    <div className="stack-l" style={{ paddingTop: 'var(--sp-8)' }}>
      <Exercice numero="01" surtitre="Compréhension orale" titre="Vrai ou faux"
                consigne="Indiquez si la phrase est vraie ou fausse."
                section="orale" score={<Score>2 / 10 juste</Score>}>
        <Carte flush marquee pied={<Bouton variante="pri">Corriger</Bouton>}>
          <RangeeExercice enonce="Karim doit aller chercher sa fille à l'école.">
            <Choix etat="juste">VRAI</Choix>
            <Choix>FAUX</Choix>
          </RangeeExercice>
        </Carte>
      </Exercice>
    </div>
  </Conteneur>
</Page>
```
