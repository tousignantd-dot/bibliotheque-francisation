import { GrilleAuto, Carte, BoutonAudio } from 'francisation-design';

export function TuilesDeVocabulaire() {
  const mots = ['un retard', 'une boîte vocale', 'un billet médical', 'un superviseur'];
  return (
    <GrilleAuto>
      {mots.map((mot) => (
        <Carte key={mot}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <BoutonAudio etiquette={`Écouter : ${mot}`} />
            <span style={{ fontSize: 'var(--fs-body-sm)', fontWeight: 'var(--fw-bold)' }}>{mot}</span>
          </div>
        </Carte>
      ))}
    </GrilleAuto>
  );
}
