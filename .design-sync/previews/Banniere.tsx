import { Banniere, GrillePaires, Jeton } from 'francisation-design';

export function AideContextuelle() {
  return <Banniere>Un mot est choisi. Touchez la définition qui lui correspond.</Banniere>;
}

export function AuDessusDeLexercice() {
  return (
    <div>
      <Banniere>Un mot est choisi. Touchez la définition qui lui correspond.</Banniere>
      <div style={{ padding: 16 }}>
        <GrillePaires
          mots={<Jeton mot etat="actif">une boîte vocale</Jeton>}
          definitions={<>
            <Jeton>Le système qui enregistre un message quand personne ne répond.</Jeton>
            <Jeton>Un document du médecin.</Jeton>
          </>}
        />
      </div>
    </div>
  );
}
