import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ZoneDepotProps extends HTMLAttributes<HTMLDivElement> {
  /** `remplie` = un mot y est posé (plaque encre), `juste` / `arevoir` = après correction. */
  etat?: 'remplie' | 'survolee' | 'juste' | 'arevoir';
  children?: ReactNode;
}

const ETATS = { remplie: 'is-filled', survolee: 'is-over', juste: 'is-ok', arevoir: 'is-no' } as const;

/** Zone de dépôt d'un exercice de classement : filet pointillé neutre tant qu'elle est vide. */
export function ZoneDepot({ etat, className, children, ...rest }: ZoneDepotProps) {
  return (
    <div role="button" tabIndex={0} className={cx('drop', etat && ETATS[etat], className)} {...rest}>
      {children}
    </div>
  );
}
