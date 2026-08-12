import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface PageProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode;
}

/** Fond de page neutre chaud (#F7F7F5) et encre par défaut. Enveloppe tout un module. */
export function Page({ className, children, ...rest }: PageProps) {
  return <div className={cx('page', className)} {...rest}>{children}</div>;
}
