// Couche React du système de design de la bibliothèque de francisation.
// Chaque composant n'applique que les classes de assets/design-system/ —
// aucune règle CSS n'est écrite ici.

export { Bouton, type BoutonProps } from './boutons/Bouton.js';
export { BoutonAudio, type BoutonAudioProps } from './boutons/BoutonAudio.js';

export { Carte, type CarteProps } from './cartes/Carte.js';
export { CarteRangee, type CarteRangeeProps } from './cartes/CarteRangee.js';
export { Savoir, type SavoirProps, type SavoirRangee } from './cartes/Savoir.js';
export { Dialogue, type DialogueProps, type DialogueLigne } from './cartes/Dialogue.js';

export { Champ, type ChampProps } from './formulaires/Champ.js';

export { Choix, type ChoixProps } from './exercices/Choix.js';
export { RangeeExercice, type RangeeExerciceProps } from './exercices/RangeeExercice.js';
export { Jeton, type JetonProps } from './exercices/Jeton.js';
export { GrillePaires, type GrillePairesProps } from './exercices/GrillePaires.js';
export { ZoneDepot, type ZoneDepotProps } from './exercices/ZoneDepot.js';
export { Trou, type TrouProps } from './exercices/Trou.js';
export { PhraseATrous, type PhraseATrousProps } from './exercices/PhraseATrous.js';

export { Retroaction, type RetroactionProps } from './retroaction/Retroaction.js';
export { BlocRetroaction, type BlocRetroactionProps } from './retroaction/BlocRetroaction.js';
export { Score, type ScoreProps } from './retroaction/Score.js';
export { Banniere, type BanniereProps } from './retroaction/Banniere.js';

export { Page, type PageProps } from './mise-en-page/Page.js';
export { Conteneur, type ConteneurProps } from './mise-en-page/Conteneur.js';
export { Bande, type BandeProps } from './mise-en-page/Bande.js';
export { BarreParcours, type BarreParcoursProps } from './mise-en-page/BarreParcours.js';
export { Etape, type EtapeProps } from './mise-en-page/Etape.js';
export { Exercice, type ExerciceProps } from './mise-en-page/Exercice.js';
export { Pile, type PileProps } from './mise-en-page/Pile.js';
export { GrilleAuto, type GrilleAutoProps } from './mise-en-page/GrilleAuto.js';
