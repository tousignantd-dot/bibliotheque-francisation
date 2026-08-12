import { Bouton } from 'francisation-design';

const HautParleur = (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" aria-hidden="true">
    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" fill="currentColor" stroke="none" />
    <path d="M15.5 8.5a5 5 0 0 1 0 7" />
    <path d="M19 5a9 9 0 0 1 0 14" />
  </svg>
);

export function TroisRoles() {
  return (
    <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center' }}>
      <Bouton variante="pri">Corriger</Bouton>
      <Bouton variante="ghost">Recommencer</Bouton>
      <Bouton variante="audio" icone={HautParleur}>Écouter le dialogue</Bouton>
    </div>
  );
}

export function Tailles() {
  return (
    <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center' }}>
      <Bouton variante="pri" taille="sm">Voir la réponse</Bouton>
      <Bouton variante="pri">Corriger</Bouton>
      <Bouton variante="pri" taille="lg">Passer à l'exercice suivant</Bouton>
    </div>
  );
}

export function Desactive() {
  return (
    <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap', alignItems: 'center' }}>
      <Bouton variante="pri" disabled>Envoyer</Bouton>
      <Bouton variante="ghost" disabled>Recommencer</Bouton>
    </div>
  );
}
