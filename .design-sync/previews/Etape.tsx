import { Etape } from 'francisation-design';

export function AFaireEtFait() {
  return (
    <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
      <Etape href="#" section="vocab" fait>Vocabulaire</Etape>
      <Etape href="#" section="orale">Vrai ou faux</Etape>
    </div>
  );
}

export function LesCinqCouleursDeSection() {
  return (
    <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
      <Etape href="#" section="orale">Compréhension orale</Etape>
      <Etape href="#" section="phonie">Graphie-phonie</Etape>
      <Etape href="#" section="ecriture">J'écris</Etape>
      <Etape href="#" section="ecoute">Écoute et réponds</Etape>
      <Etape href="#" section="vocab">Vocabulaire</Etape>
    </div>
  );
}
