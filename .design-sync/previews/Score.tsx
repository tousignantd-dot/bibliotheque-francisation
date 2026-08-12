import { Score, Exercice } from 'francisation-design';

export function Etiquette() {
  return (
    <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
      <Score>2 / 10 juste</Score>
      <Score>8 / 8 juste</Score>
    </div>
  );
}

export function DansUnExercice() {
  return (
    <Exercice
      numero="03"
      surtitre="Graphie-phonie"
      titre="Je complète avec le bon son"
      section="phonie"
      score={<Score>5 / 12 juste</Score>}
    />
  );
}
