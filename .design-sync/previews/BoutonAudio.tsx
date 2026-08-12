import { BoutonAudio } from 'francisation-design';

export function Seul() {
  return <BoutonAudio etiquette="Écouter le mot" />;
}

export function DansUneListeDeMots() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      {['un retard', 'une boîte vocale', 'un billet médical'].map((mot) => (
        <div key={mot} style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
          <BoutonAudio etiquette={`Écouter : ${mot}`} />
          <span style={{ fontSize: 'var(--fs-body-sm)', fontWeight: 'var(--fw-bold)' }}>{mot}</span>
        </div>
      ))}
    </div>
  );
}
