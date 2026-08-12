import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface PhraseATrousProps extends HTMLAttributes<HTMLParagraphElement> {
  children?: ReactNode;
}

/** Phrase à compléter, 19 px et interligne large pour que les `Trou` restent lisibles. */
export function PhraseATrous({ className, children, ...rest }: PhraseATrousProps) {
  return <p className={cx('gap-sentence', className)} {...rest}>{children}</p>;
}
