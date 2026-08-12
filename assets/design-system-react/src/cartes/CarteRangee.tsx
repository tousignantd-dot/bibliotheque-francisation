import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface CarteRangeeProps extends HTMLAttributes<HTMLDivElement> {
  children?: ReactNode;
}

/** Rangée d'une carte `flush`, séparée de la suivante par un filet — jamais par une seconde boîte. */
export function CarteRangee({ className, children, ...rest }: CarteRangeeProps) {
  return <div className={cx('card__row', className)} {...rest}>{children}</div>;
}
