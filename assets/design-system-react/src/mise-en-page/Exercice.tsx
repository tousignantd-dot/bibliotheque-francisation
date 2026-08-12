import type { HTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ExerciceProps extends HTMLAttributes<HTMLElement> {
  /** Numéro affiché dans la pastille teintée. */
  numero: ReactNode;
  /** Sur-titre coloré en majuscules (« VOCABULAIRE · 12 PAIRES »). */
  surtitre?: string;
  /** Titre de l'exercice, 30 px, dans la voix de l'apprenant (« Je complète avec le bon son »). */
  titre: ReactNode;
  /** Consigne : une phrase, sous le titre, en gris. */
  consigne?: ReactNode;
  /** Score affiché à droite du sur-titre (« 3 / 8 »). */
  score?: ReactNode;
  /**
   * Couleur de repérage de la section. Elle ne sert QUE à quatre endroits :
   * pastille, sur-titre, filet gauche de 4 px, point de la barre de parcours.
   */
  section?: 'orale' | 'phonie' | 'ecriture' | 'ecoute' | 'vocab';
  children?: ReactNode;
}

/**
 * En-tête d'exercice complet (niveau 3 de la hiérarchie) et conteneur de son contenu.
 * Pose `--sec` / `--sec-soft` : tout ce qui est à l'intérieur lit ces deux variables.
 */
export function Exercice({ numero, surtitre, titre, consigne, score, section, className, children, ...rest }: ExerciceProps) {
  return (
    <section className={cx('exo', section && `exo--${section}`, className)} {...rest}>
      <div className="exo__head">
        <div className="exo__num">{numero}</div>
        {surtitre && <div className="exo__eyebrow">{surtitre}</div>}
        <div className="exo__rule" />
        {score && <div className="exo__score">{score}</div>}
      </div>
      <h2 className="exo__title">{titre}</h2>
      {consigne && <p className="exo__sub">{consigne}</p>}
      {children}
    </section>
  );
}
