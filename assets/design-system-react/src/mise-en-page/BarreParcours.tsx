import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface BarreParcoursProps extends HTMLAttributes<HTMLElement> {
  /** Les `Etape` du module. */
  children?: ReactNode;
}

/**
 * Barre de parcours collante : niveau 2 de la hiérarchie de page.
 * Seul endroit de tout le système où la transparence et le flou sont permis.
 */
export function BarreParcours({ className, children, ...rest }: BarreParcoursProps) {
  return (
    <nav className={cx('steps', className)} aria-label="Parcours du module" {...rest}>
      <div className="steps__inner">{children}</div>
    </nav>
  );
}
