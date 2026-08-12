import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface GrilleAutoProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode;
}

/** Grille responsive à colonnes de 280 px minimum. Pour des tuiles de même nature. */
export function GrilleAuto({ className, children, ...rest }: GrilleAutoProps) {
  return <div className={cx('grid-auto', className)} {...rest}>{children}</div>;
}
