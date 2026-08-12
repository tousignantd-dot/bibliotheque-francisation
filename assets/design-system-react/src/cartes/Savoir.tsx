import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface SavoirRangee {
  /** Colonne de gauche : la forme, le son, la règle (900). */
  cle: ReactNode;
  /** Colonne de droite : l'explication ou les exemples (17 px, interligne large). */
  valeur: ReactNode;
}

export interface SavoirProps extends HTMLAttributes<HTMLDivElement> {
  /** Bandeau coloré du cadre (« LE SON [ɛ] », « LES VERBES PRONOMINAUX »). */
  bandeau?: string;
  /** Les rangées clé / valeur du savoir. */
  rangees: SavoirRangee[];
}

/**
 * Encadré de savoir explicite : bandeau coloré + rangées à deux colonnes.
 * C'est la mini-leçon « En apprendre plus » — la règle à gauche, les exemples à droite.
 */
export function Savoir({ bandeau, rangees, className, ...rest }: SavoirProps) {
  return (
    <div className={cx('savoir', className)} {...rest}>
      {bandeau && <div className="card__band">{bandeau}</div>}
      {rangees.map((r, i) => (
        <div className="savoir__row" key={i}>
          <div className="savoir__key">{r.cle}</div>
          <div className="savoir__val">{r.valeur}</div>
        </div>
      ))}
    </div>
  );
}
