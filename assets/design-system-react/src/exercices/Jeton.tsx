import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface JetonProps extends HTMLAttributes<HTMLDivElement> {
  /** `actif` = choisi (plaque encre), `apparie` = paire juste et verrouillée, `manque` = tentative fausse. */
  etat?: 'actif' | 'apparie' | 'manque';
  /** Jeton portant un mot vedette (graisse 800) plutôt qu'une définition. */
  mot?: boolean;
  children?: ReactNode;
}

const ETATS = { actif: 'is-active', apparie: 'is-paired', manque: 'is-miss' } as const;

/**
 * Jeton d'association mot ↔ définition. L'association se fait par clic-clic, jamais par
 * glissement : `role="button"` + `tabindex` + Entrée/Espace, sinon l'exercice est
 * inatteignable au clavier. Une paire juste se verrouille (`aria-disabled`).
 */
export function Jeton({ etat, mot, className, children, ...rest }: JetonProps) {
  const verrouille = etat === 'apparie';
  return (
    <div
      role="button"
      tabIndex={verrouille ? -1 : 0}
      aria-disabled={verrouille || undefined}
      className={cx('chip', mot && 'chip--word', etat && ETATS[etat], className)}
      {...rest}
    >
      {children}
    </div>
  );
}
