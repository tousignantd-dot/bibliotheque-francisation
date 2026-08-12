import { Carte, RangeeExercice, Choix, Retroaction } from 'francisation-design';

export function TroisQuestions() {
  return (
    <Carte flush marquee>
      <RangeeExercice enonce="Karim doit aller chercher sa fille à l'école.">
        <Choix etat="juste">VRAI</Choix>
        <Choix>FAUX</Choix>
      </RangeeExercice>
      <RangeeExercice enonce="C'est la première absence de Karim ce mois-ci.">
        <Choix etat="arevoir">VRAI</Choix>
        <Choix etat="attendu">FAUX</Choix>
      </RangeeExercice>
      <RangeeExercice enonce="Karim et Nadia travaillent ensemble.">
        <Choix etat="choisi">VRAI</Choix>
        <Choix>FAUX</Choix>
      </RangeeExercice>
    </Carte>
  );
}

export function AvecRetroaction() {
  return (
    <Carte flush>
      <RangeeExercice
        enonce={<>C'est la première absence de Karim ce mois-ci.<Retroaction ton="arevoir" style={{ marginTop: 8 }}>La bonne réponse est FAUX</Retroaction></>}
      >
        <Choix etat="arevoir">VRAI</Choix>
        <Choix etat="attendu">FAUX</Choix>
      </RangeeExercice>
    </Carte>
  );
}
