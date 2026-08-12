import type { ButtonHTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface BoutonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Rôle du bouton. `pri` = plaque encre, `ghost` = blanc filet, `audio` = le seul aplat rouge de l'interface (réservé à l'écoute). */
  variante?: 'pri' | 'ghost' | 'audio';
  /** Hauteur. `md` (48 px) par défaut ; `sm` reste à 44 px, le plancher tactile. */
  taille?: 'sm' | 'md' | 'lg';
  /** Icône SVG monochrome placée avant le libellé (héritera de `currentColor`). */
  icone?: ReactNode;
  children?: ReactNode;
}

/**
 * Bouton en pilule, trois rôles seulement. Le rouge (`audio`) est réservé à l'écoute.
 * Hauteur plancher 44 px : ne jamais descendre en dessous, le public est sur téléphone.
 */
export function Bouton({ variante = 'ghost', taille = 'md', icone, className, children, ...rest }: BoutonProps) {
  return (
    <button
      type="button"
      className={cx('btn', `btn--${variante}`, taille !== 'md' && `btn--${taille}`, className)}
      {...rest}
    >
      {icone}
      {children}
    </button>
  );
}
