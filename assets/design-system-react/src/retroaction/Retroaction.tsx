import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface RetroactionProps extends HTMLAttributes<HTMLParagraphElement> {
  /** `juste` (✓), `arevoir` (✕) ou `attention` (!). Le glyphe est ajouté en CSS. */
  ton: 'juste' | 'arevoir' | 'attention';
  children?: ReactNode;
}

const TONS = { juste: 'fb--ok', arevoir: 'fb--no', attention: 'fb--warn' } as const;

/**
 * Ligne de rétroaction courte et factuelle (« ✓ Juste », « ✕ La bonne réponse est VRAI »).
 * Jamais la couleur seule : chaque état porte un glyphe. Annoncée avec `aria-live="polite"`.
 */
export function Retroaction({ ton, className, children, ...rest }: RetroactionProps) {
  return (
    <p aria-live="polite" className={cx('fb', TONS[ton], className)} {...rest}>{children}</p>
  );
}
