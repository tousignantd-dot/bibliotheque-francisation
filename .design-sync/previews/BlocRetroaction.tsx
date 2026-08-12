import { BlocRetroaction } from 'francisation-design';

export function CorrectionDunEcrit() {
  return (
    <BlocRetroaction
      titre="Correction"
      items={['La phrase est juste.', 'Le message dit bien l\'heure d\'arrivée.']}
    />
  );
}

export function ARevoir() {
  return (
    <BlocRetroaction
      ton="arevoir"
      titre="À revoir"
      items={[
        'Le verbe ne s\'accorde pas avec le sujet : « Je vais arriver », pas « Je vas arriver ».',
        'Il manque l\'heure d\'arrivée.',
      ]}
    />
  );
}

export function Attention() {
  return (
    <BlocRetroaction
      ton="attention"
      titre="Presque"
      items={['Attention à l\'accent sur « prévenir ».', 'On écrit « 9 h 30 », avec des espaces.']}
    />
  );
}
