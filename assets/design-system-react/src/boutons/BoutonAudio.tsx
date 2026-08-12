import type { ButtonHTMLAttributes } from 'react';
import { cx } from '../interne/cx.js';

export interface BoutonAudioProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /** Texte lu par les lecteurs d'écran — l'icône seule n'annonce rien. */
  etiquette: string;
}

/**
 * Bouton d'écoute rond, icône haut-parleur seule, 44 px minimum.
 * Le seul autre endroit où le rouge audio est permis, avec `Bouton variante="audio"`.
 */
export function BoutonAudio({ etiquette, className, ...rest }: BoutonAudioProps) {
  return (
    <button type="button" aria-label={etiquette} className={cx('btn-audio-round', className)} {...rest}>
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
        <path d="M11 5 6 9H2v6h4l5 4V5Z" />
        <path d="M15.5 8.5a5 5 0 0 1 0 7" />
        <path d="M18.5 5.5a9 9 0 0 1 0 13" />
      </svg>
    </button>
  );
}
