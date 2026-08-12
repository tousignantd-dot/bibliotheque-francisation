import { Conteneur, Carte } from 'francisation-design';

export function ColonneCentree() {
  return (
    <div style={{ background: 'var(--surface-page)', padding: '20px 0' }}>
      <Conteneur>
        <Carte>
          <p style={{ fontSize: 'var(--fs-body-sm)', fontWeight: 'var(--fw-medium)' }}>
            Colonne de 1000 px au maximum, centrée, avec une gouttière de 32 px de chaque côté.
            Tout le contenu d'un module passe par là.
          </p>
        </Carte>
      </Conteneur>
    </div>
  );
}
