import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface DialogueLigne {
  /** Qui parle. Court : un prénom ou un rôle. */
  qui: string;
  /** La réplique. */
  texte: ReactNode;
}

export interface DialogueProps extends HTMLAttributes<HTMLDivElement> {
  /** Les répliques, dans l'ordre. */
  lignes: DialogueLigne[];
}

/** Transcription d'un dialogue : le locuteur en vert à gauche, la réplique à droite. */
export function Dialogue({ lignes, className, ...rest }: DialogueProps) {
  return (
    <div className={cx('dialogue', className)} {...rest}>
      {lignes.map((l, i) => (
        <div className="dialogue__line" key={i}>
          <div className="dialogue__who">{l.qui}</div>
          <div className="dialogue__txt">{l.texte}</div>
        </div>
      ))}
    </div>
  );
}
