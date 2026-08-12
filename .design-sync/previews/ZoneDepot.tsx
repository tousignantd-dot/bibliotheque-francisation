import { ZoneDepot } from 'francisation-design';

export function LesQuatreEtats() {
  return (
    <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
      <ZoneDepot style={{ minWidth: 150 }}>déposez ici</ZoneDepot>
      <ZoneDepot etat="remplie" style={{ minWidth: 150 }}>le matin</ZoneDepot>
      <ZoneDepot etat="juste" style={{ minWidth: 150 }}>le matin</ZoneDepot>
      <ZoneDepot etat="arevoir" style={{ minWidth: 150 }}>le soir</ZoneDepot>
    </div>
  );
}

export function ClassementEnDeuxColonnes() {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
      <div>
        <div style={{ fontSize: 'var(--fs-label)', fontWeight: 'var(--fw-bold)', letterSpacing: 'var(--ls-label)', textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: 8 }}>Le matin</div>
        <ZoneDepot etat="remplie">se lever tôt</ZoneDepot>
      </div>
      <div>
        <div style={{ fontSize: 'var(--fs-label)', fontWeight: 'var(--fw-bold)', letterSpacing: 'var(--ls-label)', textTransform: 'uppercase', color: 'var(--text-muted)', marginBottom: 8 }}>Le soir</div>
        <ZoneDepot>déposez un mot</ZoneDepot>
      </div>
    </div>
  );
}
