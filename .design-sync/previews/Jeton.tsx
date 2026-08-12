import { Jeton } from 'francisation-design';

export function MotsEtDefinitions() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8, maxWidth: 420 }}>
      <Jeton mot>un retard</Jeton>
      <Jeton>Le fait d'arriver après un moment fixé.</Jeton>
    </div>
  );
}

export function LesTroisEtats() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8, maxWidth: 420 }}>
      <Jeton mot etat="apparie">un retard</Jeton>
      <Jeton mot etat="actif">une boîte vocale</Jeton>
      <Jeton mot etat="manque">un billet médical</Jeton>
      <Jeton mot>un superviseur</Jeton>
    </div>
  );
}
