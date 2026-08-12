import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface GrillePairesProps extends HTMLAttributes<HTMLDivElement> {
  /** Colonne étroite : les mots. */
  mots: ReactNode;
  /** Colonne large : les définitions. */
  definitions: ReactNode;
}

/** Grille à deux colonnes de l'exercice d'association : mots à gauche, définitions à droite. */
export function GrillePaires({ mots, definitions, className, ...rest }: GrillePairesProps) {
  return (
    <div className={cx('pair-grid', className)} {...rest}>
      <div className="stack">{mots}</div>
      <div className="stack">{definitions}</div>
    </div>
  );
}
