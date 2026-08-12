import { Bande, Carte, Bouton } from 'francisation-design';

const HautParleur = (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" aria-hidden="true">
    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5" fill="currentColor" stroke="none" />
    <path d="M15.5 8.5a5 5 0 0 1 0 7" />
  </svg>
);

export function EnTeteDeModule() {
  return (
    <Bande
      surtitre="Module 4 · Le monde du travail"
      titre="Absent ou en retard : que faire ?"
      chapeau="Karim doit aller chercher sa fille à l'école. Il appelle son superviseur pour le prévenir."
    />
  );
}

export function AvecLaSituation() {
  return (
    <Bande
      surtitre="Module 4 · Le monde du travail"
      titre="Absent ou en retard : que faire ?"
      chapeau="Écoutez l'appel de Karim, puis répondez aux questions."
    >
      <div style={{ marginTop: 20 }}>
        <Carte>
          <p style={{ fontSize: 'var(--fs-body-sm)', fontWeight: 'var(--fw-medium)', marginBottom: 16 }}>
            Il est 7 h 40. Karim ne pourra pas entrer à l'heure. Il téléphone à Nadia, sa superviseure.
          </p>
          <Bouton variante="audio" icone={HautParleur}>Écouter le dialogue</Bouton>
        </Carte>
      </div>
    </Bande>
  );
}
