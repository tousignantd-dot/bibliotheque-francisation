import { Trou, PhraseATrous } from 'francisation-design';

export function DansUnePhrase() {
  return (
    <PhraseATrous>
      Karim <Trou etat="remplie">prévient</Trou> sa superviseure avant <Trou>7 h 45</Trou>.
    </PhraseATrous>
  );
}

export function ApresCorrection() {
  return (
    <PhraseATrous>
      Elle <Trou etat="juste">observe</Trou> la lettre, puis elle <Trou etat="arevoir">prévient</Trou> son superviseur.
    </PhraseATrous>
  );
}
