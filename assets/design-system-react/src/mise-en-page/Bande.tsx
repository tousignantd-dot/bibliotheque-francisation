import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface BandeProps extends HTMLAttributes<HTMLElement> {
  /** Sur-titre en majuscules, 13 px — le seul endroit où les capitales sont permises. */
  surtitre?: string;
  /** Titre du module (62 px, 900). */
  titre: ReactNode;
  /** Chapeau : une ou deux phrases, 19 px, gris encre. */
  chapeau?: ReactNode;
  /** Contenu placé sous le chapeau — typiquement la situation dans une carte blanche. */
  children?: ReactNode;
}

/**
 * Bandeau d'en-tête clair (#EDF6F1) : niveau 1 de la hiérarchie de page.
 * Il n'est JAMAIS noir — le seul bloc foncé permis est l'appel à l'action final.
 */
export function Bande({ surtitre, titre, chapeau, className, children, ...rest }: BandeProps) {
  return (
    <header className={cx('band', className)} {...rest}>
      <div className="container">
        {surtitre && <div className="band__eyebrow">{surtitre}</div>}
        <h1>{titre}</h1>
        {chapeau && <p className="band__lead">{chapeau}</p>}
        {children}
      </div>
    </header>
  );
}
