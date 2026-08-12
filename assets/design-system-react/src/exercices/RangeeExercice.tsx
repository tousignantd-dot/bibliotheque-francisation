import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface RangeeExerciceProps extends HTMLAttributes<HTMLDivElement> {
  /** L'énoncé de la question, à gauche (18 px, 700). */
  enonce: ReactNode;
  /** Les contrôles de réponse, à droite — des `Choix` en général. */
  children?: ReactNode;
}

/** Rangée de question : énoncé à gauche, options à droite, filet en dessous. */
export function RangeeExercice({ enonce, className, children, ...rest }: RangeeExerciceProps) {
  return (
    <div className={cx('exo-row', className)} {...rest}>
      <div className="exo-row__txt">{enonce}</div>
      <div className="exo-row__opts">{children}</div>
    </div>
  );
}
