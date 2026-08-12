import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface PileProps extends HTMLAttributes<HTMLDivElement> {
  /** Écart de 48 px au lieu de 12 px — l'espacement entre deux exercices. */
  large?: boolean;
  children?: ReactNode;
}

/** Empilement vertical à écart fixe. `large` sépare des exercices, sinon des rangées. */
export function Pile({ large, className, children, ...rest }: PileProps) {
  return <div className={cx(large ? 'stack-l' : 'stack', className)} {...rest}>{children}</div>;
}
