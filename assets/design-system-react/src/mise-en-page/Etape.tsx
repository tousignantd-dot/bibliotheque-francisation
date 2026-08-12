import type { AnchorHTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface EtapeProps extends AnchorHTMLAttributes<HTMLAnchorElement> {
  /** Étape réussie : la pastille prend la couleur de section (`--sec` / `--sec-soft`). */
  fait?: boolean;
  /** Couleur de section portée par l'étape, posée en variables CSS locales. */
  section?: 'orale' | 'phonie' | 'ecriture' | 'ecoute' | 'vocab';
  children?: ReactNode;
}

const SECTIONS: Record<string, [string, string]> = {
  orale: ['var(--acier-600)', 'var(--acier-100)'],
  phonie: ['var(--violet-600)', 'var(--violet-100)'],
  ecriture: ['var(--ambre-700)', 'var(--ambre-100)'],
  ecoute: ['var(--teal-700)', 'var(--teal-100)'],
  vocab: ['var(--green-600)', 'var(--green-100)'],
};

/** Pastille d'étape dans la `BarreParcours`. Cliquable, et teintée quand l'étape est réussie. */
export function Etape({ fait, section, className, style, children, ...rest }: EtapeProps) {
  const paire = section ? SECTIONS[section] : undefined;
  return (
    <a
      className={cx('step', fait && 'is-done', className)}
      style={paire ? ({ ['--sec' as string]: paire[0], ['--sec-soft' as string]: paire[1], ...style } as typeof style) : style}
      {...rest}
    >
      {/* La pastille porte la couleur de section — c'est l'un des quatre seuls
          endroits où cette couleur a le droit d'apparaître. */}
      <span className="step__dot" style={{ background: 'var(--sec, currentColor)' }} />
      {children}
    </a>
  );
}
