import { Exercice, Carte, RangeeExercice, Choix, Bouton, Score } from 'francisation-design';

export function EnTeteComplet() {
  return (
    <Exercice
      numero="01"
      surtitre="Compréhension orale"
      titre="Vrai ou faux"
      consigne="Écoutez de nouveau le dialogue, puis indiquez si la phrase est vraie ou fausse."
      score={<Score>2 / 10 juste</Score>}
      section="orale"
    >
      <Carte flush marquee pied={<><Bouton variante="pri">Corriger</Bouton><Bouton variante="ghost">Recommencer</Bouton></>}>
        <RangeeExercice enonce="Karim doit aller chercher sa fille à l'école.">
          <Choix etat="juste">VRAI</Choix>
          <Choix>FAUX</Choix>
        </RangeeExercice>
        <RangeeExercice enonce="Karim et Nadia travaillent ensemble.">
          <Choix etat="choisi">VRAI</Choix>
          <Choix>FAUX</Choix>
        </RangeeExercice>
      </Carte>
    </Exercice>
  );
}

export function LesCinqSections() {
  const sections = [
    ['orale', 'Compréhension orale', 'Vrai ou faux'],
    ['phonie', 'Graphie-phonie', 'Je complète avec le bon son'],
    ['ecriture', 'Écriture', "J'écris mon message"],
    ['ecoute', 'Écoute et réponds', 'Deux appels'],
    ['vocab', 'Vocabulaire · 12 paires', 'Le mot et sa définition'],
  ] as const;
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 32 }}>
      {sections.map(([sec, surtitre, titre]) => (
        <Exercice key={sec} numero={sections.findIndex((s) => s[0] === sec) + 1} surtitre={surtitre} titre={titre} section={sec} />
      ))}
    </div>
  );
}
