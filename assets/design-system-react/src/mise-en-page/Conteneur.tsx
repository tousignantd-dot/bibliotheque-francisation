import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ConteneurProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode;
}

/** Colonne centrée de 1000 px avec la gouttière de 32 px. Toute rangée de contenu passe par là. */
export function Conteneur({ className, children, ...rest }: ConteneurProps) {
  return <div className={cx('container', className)} {...rest}>{children}</div>;
}
