import type { ButtonHTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ChoixProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  /**
   * État de la réponse. `choisi` = plaque encre (jamais une teinte de plus),
   * `juste` / `arevoir` = rétroaction, `attendu` = la bonne réponse non choisie (filet pointillé).
   */
  etat?: 'choisi' | 'juste' | 'arevoir' | 'attendu';
  children?: ReactNode;
}

const ETATS = { choisi: 'is-selected', juste: 'is-ok', arevoir: 'is-no', attendu: 'is-answer' } as const;

/**
 * Bouton de choix binaire (vrai/faux, [e]/[ɛ]). Règle d'or : sélectionné = plaque encre,
 * pour que la couleur reste disponible pour dire « juste » ou « à revoir ».
 */
export function Choix({ etat, className, children, ...rest }: ChoixProps) {
  return (
    <button
      type="button"
      aria-pressed={etat === 'choisi' || undefined}
      className={cx('choice', etat && ETATS[etat], className)}
      {...rest}
    >
      {children}
    </button>
  );
}
