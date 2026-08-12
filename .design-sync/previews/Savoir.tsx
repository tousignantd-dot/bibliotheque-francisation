import { Savoir } from 'francisation-design';

export function LesSonsEEtEOuvert() {
  return (
    <Savoir
      bandeau="Des sons et des lettres"
      rangees={[
        { cle: '[ɛ] au début ou au milieu', valeur: 'è, ê, ei, ai + consonne : père, tête, treize, semaine · e + l : nouvelle · e + r : hiver' },
        { cle: '[e] en fin de mot', valeur: 'é, ai, er : dépanné, je travaillerai, dépanner (exceptions : hiver, mer)' },
      ]}
    />
  );
}

export function UnePetiteRegleDeGrammaire() {
  return (
    <Savoir
      bandeau="Prévenir quelqu'un"
      rangees={[
        { cle: 'prévenir + quelqu\'un', valeur: 'Je préviens mon superviseur. · Elle prévient son équipe.' },
        { cle: 'au passé composé', valeur: "J'ai prévenu mon superviseur ce matin." },
        { cle: 'à ne pas confondre', valeur: 'avertir = dire à l\'avance · avouer = dire une faute' },
      ]}
    />
  );
}
