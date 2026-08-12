import { Choix } from 'francisation-design';

export function VraiOuFaux() {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      <Choix>VRAI</Choix>
      <Choix>FAUX</Choix>
    </div>
  );
}

export function LesQuatreEtats() {
  return (
    <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
      <Choix etat="choisi">Choisi</Choix>
      <Choix etat="juste">Juste</Choix>
      <Choix etat="arevoir">À revoir</Choix>
      <Choix etat="attendu">Attendue</Choix>
    </div>
  );
}

export function DeuxSons() {
  return (
    <div style={{ display: 'flex', gap: 8 }}>
      <Choix etat="choisi">[e]</Choix>
      <Choix>[ɛ]</Choix>
    </div>
  );
}
