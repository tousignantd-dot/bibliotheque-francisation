import { BarreParcours, Etape } from 'francisation-design';

export function ParcoursDunModule() {
  return (
    <BarreParcours>
      <Etape href="#e1" fait section="vocab">Vocabulaire</Etape>
      <Etape href="#e2" section="orale">Vrai ou faux</Etape>
      <Etape href="#e3" section="phonie">Les sons</Etape>
      <Etape href="#e4" section="ecriture">J'écris</Etape>
      <Etape href="#e5" section="ecoute">Deux appels</Etape>
    </BarreParcours>
  );
}
