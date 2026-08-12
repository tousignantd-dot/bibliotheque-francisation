/** Concatène des classes en ignorant les valeurs vides. Usage interne. */
export function cx(...parts: Array<string | false | null | undefined>): string {
  return parts.filter(Boolean).join(' ');
}
