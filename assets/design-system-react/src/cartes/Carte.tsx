import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface CarteProps extends HTMLAttributes<HTMLDivElement> {
  /** Bandeau de titre coloré en haut de la carte (majuscules, 12 px). Impose `flush`. */
  bandeau?: string;
  /** Pied de carte sur fond creusé — y placer les boutons d'action. */
  pied?: ReactNode;
  /** Sans rembourrage intérieur : la carte encadre des `CarteRangee`. */
  flush?: boolean;
  /** Filet gauche de 4 px à la couleur de section — le seul usage décoratif permis. */
  marquee?: boolean;
  /** Fond vert très clair au lieu du blanc. Pour un encadré d'appui, jamais pour du texte long. */
  teintee?: boolean;
  children?: ReactNode;
}

/**
 * Carte blanche, filet 1 px, rayon 18 px, ombre presque nulle.
 * Le contenant de base : la structure vient des filets, pas de la profondeur.
 */
export function Carte({ bandeau, pied, flush, marquee, teintee, className, children, ...rest }: CarteProps) {
  const creuse = flush || Boolean(bandeau) || Boolean(pied);
  return (
    <div
      className={cx('card', creuse && 'card--flush', marquee && 'card--marked', teintee && 'card--tinted', className)}
      {...rest}
    >
      {bandeau && <div className="card__band">{bandeau}</div>}
      {creuse && !flush ? <div className="card__row">{children}</div> : children}
      {pied && <div className="card__foot">{pied}</div>}
    </div>
  );
}
