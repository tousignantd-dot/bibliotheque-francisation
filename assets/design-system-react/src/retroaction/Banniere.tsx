import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface BanniereProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode;
}

/**
 * Bannière d'aide contextuelle en haut de l'exercice
 * (« Un mot est choisi. Touchez maintenant sa définition. »). Fond ambre, filet 2 px.
 */
export function Banniere({ className, children, ...rest }: BanniereProps) {
  return <div role="status" className={cx('banner', className)} {...rest}>{children}</div>;
}
