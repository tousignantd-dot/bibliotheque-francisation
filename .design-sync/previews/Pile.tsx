import { Pile, Carte } from 'francisation-design';

export function EcartCourant() {
  return (
    <Pile>
      <Carte>Première consigne de l'exercice.</Carte>
      <Carte>Deuxième consigne de l'exercice.</Carte>
      <Carte>Troisième consigne de l'exercice.</Carte>
    </Pile>
  );
}

export function EcartEntreExercices() {
  return (
    <Pile large>
      <Carte marquee>Exercice 1 · Vrai ou faux</Carte>
      <Carte marquee>Exercice 2 · Le mot et sa définition</Carte>
    </Pile>
  );
}
