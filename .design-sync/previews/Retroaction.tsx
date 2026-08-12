import { Retroaction } from 'francisation-design';

export function LesTroisTons() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
      <Retroaction ton="juste">Juste</Retroaction>
      <Retroaction ton="arevoir">La bonne réponse est FAUX</Retroaction>
      <Retroaction ton="attention">Attention à l'accent sur « prévenir »</Retroaction>
    </div>
  );
}

export function SousUnEnonce() {
  return (
    <div>
      <p style={{ fontSize: 'var(--fs-body)', fontWeight: 'var(--fw-semi)', marginBottom: 8 }}>
        Elle observe la lettre avec attention.
      </p>
      <Retroaction ton="juste">Juste — le verbe s'accorde avec « elle ».</Retroaction>
    </div>
  );
}
