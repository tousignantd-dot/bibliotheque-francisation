import type { InputHTMLAttributes, ReactNode } from 'react';
import { cx } from '../interne/cx.js';

export interface ChampProps extends Omit<InputHTMLAttributes<HTMLInputElement>, 'size'> {
  /** Sur-titre du champ, en majuscules 13 px. */
  etiquette?: string;
  /** Phrase d'aide sous le champ (exemple attendu, contrainte de longueur). */
  aide?: ReactNode;
  /** Zone de texte multiligne (112 px de haut) au lieu d'une ligne. */
  multiligne?: boolean;
  /** Réponse validée : filet et fond verts. */
  valide?: boolean;
}

/**
 * Champ de saisie : fond creusé, filet neutre, focus vert de 3 px.
 * Corps de saisie à 17 px — la réponse de l'apprenant doit rester relisible.
 */
export function Champ({ etiquette, aide, multiligne, valide, className, id, ...rest }: ChampProps) {
  const classes = cx('field', multiligne && 'field--area', valide && 'is-good', className);
  return (
    <div>
      {etiquette && <label className="field-label" htmlFor={id}>{etiquette}</label>}
      {multiligne
        ? <textarea className={classes} id={id} {...(rest as InputHTMLAttributes<HTMLTextAreaElement>)} />
        : <input className={classes} id={id} {...rest} />}
      {aide && <p className="field-hint">{aide}</p>}
    </div>
  );
}
