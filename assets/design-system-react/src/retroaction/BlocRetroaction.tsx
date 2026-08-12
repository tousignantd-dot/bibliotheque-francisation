import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface BlocRetroactionProps extends HTMLAttributes<HTMLDivElement> {
  /** `juste`, `arevoir` (fond à peine teinté — jamais d'aplat rouge saturé) ou `attention`. */
  ton?: 'juste' | 'arevoir' | 'attention';
  /** Sur-titre du bloc (« CE QUI EST À REVOIR »). */
  titre?: string;
  /** Les remarques, une par puce. Brèves et factuelles : on donne la bonne réponse, on ne juge pas. */
  items: ReactNode[];
}

const TONS = { arevoir: 'fb-box--no', attention: 'fb-box--warn' } as const;

/** Bloc de rétroaction détaillée — la correction d'un écrit, remarque par remarque. */
export function BlocRetroaction({ ton = 'juste', titre, items, className, ...rest }: BlocRetroactionProps) {
  return (
    <div aria-live="polite" className={cx('fb-box', ton !== 'juste' && TONS[ton], className)} {...rest}>
      {titre && <div className="fb-box__title">{titre}</div>}
      {items.map((it, i) => <div className="fb-box__item" key={i}>{it}</div>)}
    </div>
  );
}
