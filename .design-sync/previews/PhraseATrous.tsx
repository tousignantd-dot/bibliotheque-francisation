import { PhraseATrous, Trou, Carte } from 'francisation-design';

export function TexteATrous() {
  return (
    <Carte marquee>
      <PhraseATrous>
        Bonjour, c'est Karim. Je vais arriver <Trou etat="remplie">en retard</Trou> ce matin.
        Je serai là vers <Trou>9 h 30</Trou>.
      </PhraseATrous>
    </Carte>
  );
}
