import { GrillePaires, Jeton } from 'francisation-design';

export function AssociationMotDefinition() {
  return (
    <GrillePaires
      mots={<>
        <Jeton mot etat="apparie">un retard</Jeton>
        <Jeton mot etat="actif">une boîte vocale</Jeton>
        <Jeton mot>un billet médical</Jeton>
      </>}
      definitions={<>
        <Jeton etat="apparie">Le fait d'arriver après un moment fixé.</Jeton>
        <Jeton etat="manque">Un document du médecin qui confirme une consultation.</Jeton>
        <Jeton>Le système qui enregistre un message quand personne ne répond.</Jeton>
      </>}
    />
  );
}
