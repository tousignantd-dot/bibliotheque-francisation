import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface TrouProps extends HTMLAttributes<HTMLSpanElement> {
  /** `remplie` = un mot y est posé, `juste` / `arevoir` = après correction. */
  etat?: 'remplie' | 'juste' | 'arevoir';
  children?: ReactNode;
}

const ETATS = { remplie: 'is-filled', juste: 'is-ok', arevoir: 'is-no' } as const;

/** Trou cliquable au fil d'une phrase (texte à trous). Toujours dans une `PhraseATrous`. */
export function Trou({ etat, className, children, ...rest }: TrouProps) {
  return (
    <span role="button" tabIndex={0} className={cx('blank', etat && ETATS[etat], className)} {...rest}>
      {children}
    </span>
  );
}
