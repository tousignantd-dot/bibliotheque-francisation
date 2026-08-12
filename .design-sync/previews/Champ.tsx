import { Champ } from 'francisation-design';

export function UneLigne() {
  return <Champ id="c1" etiquette="Votre réponse" placeholder="Écrivez la phrase complète" />;
}

export function AvecAide() {
  return (
    <Champ
      id="c2"
      etiquette="Message à votre superviseur"
      aide="Deux ou trois phrases : qui vous êtes, le problème, l'heure d'arrivée."
      placeholder="Bonjour, c'est…"
    />
  );
}

export function Multiligne() {
  return (
    <Champ
      id="c3"
      multiligne
      etiquette="Votre courriel"
      defaultValue={"Bonjour Nadia,\nJe vais arriver vers 9 h 30. Merci, Karim"}
    />
  );
}

export function Validee() {
  return <Champ id="c4" valide etiquette="Votre réponse" defaultValue="Elle observe la lettre avec attention." />;
}
