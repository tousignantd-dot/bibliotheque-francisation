import { Dialogue } from 'francisation-design';

export function AppelAuSuperviseur() {
  return (
    <Dialogue
      lignes={[
        { qui: 'Nadia', texte: 'Bonjour, entrepôt Bellerive, Nadia à l\'appareil.' },
        { qui: 'Karim', texte: 'Bonjour Nadia, c\'est Karim Benali. Je vais arriver en retard ce matin.' },
        { qui: 'Nadia', texte: 'D\'accord. Vous arrivez vers quelle heure ?' },
        { qui: 'Karim', texte: 'Vers 9 h 30. Je dois passer à l\'école chercher ma fille.' },
        { qui: 'Nadia', texte: 'C\'est noté. Merci d\'avoir prévenu.' },
      ]}
    />
  );
}
