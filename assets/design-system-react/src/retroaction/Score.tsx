import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ScoreProps extends HTMLAttributes<HTMLSpanElement> {
  children?: ReactNode;
}

/** Étiquette de progression en pilule (« 3 / 8 »). Prend la couleur de section de l'`Exercice`. */
export function Score({ className, children, ...rest }: ScoreProps) {
  return <span className={cx('score', className)} {...rest}>{children}</span>;
}
