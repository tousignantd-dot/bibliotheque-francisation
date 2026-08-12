import { Carte, CarteRangee, Bouton } from 'francisation-design';

export function CarteSimple() {
  return (
    <Carte>
      <h3 style={{ marginBottom: 8 }}>La situation</h3>
      <p style={{ fontSize: 'var(--fs-body-sm)', fontWeight: 'var(--fw-medium)', color: 'var(--text-body)' }}>
        Il est 7 h 40. Karim ne pourra pas entrer à l'heure. Il téléphone à sa superviseure.
      </p>
    </Carte>
  );
}

export function AvecBandeauEtRangees() {
  return (
    <Carte flush bandeau="Ce qu'il faut dire au téléphone">
      <CarteRangee>Se nommer : « Bonjour, c'est Karim Benali. »</CarteRangee>
      <CarteRangee>Dire le problème : « Je vais arriver en retard ce matin. »</CarteRangee>
      <CarteRangee>Donner l'heure : « Je serai là vers 9 h 30. »</CarteRangee>
    </Carte>
  );
}

export function AvecPied() {
  return (
    <Carte flush pied={<><Bouton variante="pri">Corriger</Bouton><Bouton variante="ghost">Recommencer</Bouton></>}>
      <CarteRangee>Karim doit aller chercher sa fille à l'école.</CarteRangee>
      <CarteRangee>C'est la première absence de Karim ce mois-ci.</CarteRangee>
    </Carte>
  );
}

export function MarqueeEtTeintee() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
      <Carte marquee>Filet gauche de 4 px : cette carte appartient à la section en cours.</Carte>
      <Carte teintee>Fond vert très clair : un encadré d'appui, jamais du texte long.</Carte>
    </div>
  );
}
