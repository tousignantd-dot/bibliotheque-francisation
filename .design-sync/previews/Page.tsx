import { Page, Conteneur, Carte, Bouton } from 'francisation-design';

export function FondDePage() {
  return (
    <Page style={{ padding: '24px 0' }}>
      <Conteneur>
        <Carte>
          <h2 style={{ marginBottom: 8 }}>Je découvre</h2>
          <p style={{ fontSize: 'var(--fs-body-sm)', color: 'var(--text-muted)' }}>
            La carte blanche se détache du fond neutre chaud de la page : c'est tout le contraste
            dont le système a besoin.
          </p>
          <div style={{ marginTop: 16 }}><Bouton variante="pri">Commencer</Bouton></div>
        </Carte>
      </Conteneur>
    </Page>
  );
}
