/* Ce qui est injecté dans la page pendant le tournage : un pointeur, ses
   gestes, un défilement doux et un surlignage qui paraît en fondu.
   Tout vit dans la page filmée, pas dans le script de pilotage — c'est la
   seule façon d'obtenir un mouvement à 60 images par seconde. Piloter le
   pointeur depuis Node, un pas par appel, donnerait des saccades.

   Exporté comme une chaîne : `enregistrer.js` l'évalue dans la page. */
module.exports = String.raw`
(() => {
  if (window.__scene) return;

  const RACINE = document.createElement('div');
  RACINE.style.cssText = 'position:fixed;inset:0;z-index:2147483000;pointer-events:none';
  document.body.appendChild(RACINE);

  /* — Le pointeur — un vrai curseur dessiné, pas un rond. Un rond flottant
       ne se lit pas comme une souris ; la flèche, si. */
  const POINTEUR = document.createElement('div');
  POINTEUR.style.cssText = 'position:absolute;left:0;top:0;width:26px;height:26px;'
    + 'opacity:0;transition:opacity .25s;will-change:transform';
  POINTEUR.innerHTML =
    '<svg width="26" height="26" viewBox="0 0 26 26" fill="none">'
    + '<path d="M5 2.5 L5 19.5 L9.6 15.2 L12.6 21.8 L15.9 20.3 L12.9 13.9 L19.3 13.6 Z"'
    + ' fill="#17181A" stroke="#FFFFFF" stroke-width="1.6" stroke-linejoin="round"/>'
    + '</svg>';
  RACINE.appendChild(POINTEUR);

  /* L'onde du clic : elle dit « ça vient d'être cliqué » sans masquer la
     cible, donc jamais opaque et toujours plus grande que le doigt. */
  function onde(x, y) {
    const o = document.createElement('div');
    o.style.cssText = 'position:absolute;left:' + x + 'px;top:' + y + 'px;'
      + 'width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;'
      + 'border:2.5px solid #0A8F5B;background:rgba(10,143,91,.18);';
    RACINE.appendChild(o);
    o.animate(
      [{ transform: 'scale(.6)', opacity: 1 }, { transform: 'scale(4.2)', opacity: 0 }],
      { duration: 620, easing: 'cubic-bezier(.2,.7,.3,1)' },
    ).onfinish = () => o.remove();
  }

  let px = innerWidth * 0.5, py = innerHeight * 0.62;
  const place = () => { POINTEUR.style.transform = 'translate(' + px + 'px,' + py + 'px)'; };
  place();

  const dodo = (ms) => new Promise((r) => setTimeout(r, ms));
  /* Accélération puis freinage : un déplacement linéaire a l'air d'un
     automate, et c'est précisément ce qu'on veut cacher. */
  const adouci = (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);

  function anime(duree, pas) {
    return new Promise((fini) => {
      const depart = performance.now();
      const trame = (maintenant) => {
        const t = Math.min(1, (maintenant - depart) / duree);
        pas(adouci(t));
        if (t < 1) requestAnimationFrame(trame); else fini();
      };
      requestAnimationFrame(trame);
    });
  }

  const centre = (el) => {
    const r = el.getBoundingClientRect();
    return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
  };

  async function versPoint(x, y, duree) {
    POINTEUR.style.opacity = '1';
    const x0 = px, y0 = py;
    const d = Math.hypot(x - x0, y - y0);
    if (d < 2) return;
    await anime(duree ?? Math.min(1100, 320 + d * 0.9), (t) => {
      px = x0 + (x - x0) * t;
      py = y0 + (y - y0) * t;
      place();
    });
  }

  /* Un élément hors de l'écran doit d'abord y être amené : le pointeur ne
     peut pas cliquer ce qu'on ne voit pas, et le spectateur non plus. */
  async function versElement(sel) {
    const el = document.querySelector(sel);
    if (!el) throw new Error('cible absente : ' + sel);
    const r = el.getBoundingClientRect();
    if (r.top < 90 || r.bottom > innerHeight - 40) {
      await defiler(sel);
    }
    const c = centre(document.querySelector(sel));
    await versPoint(c.x, c.y);
    return document.querySelector(sel);
  }

  async function defiler(sel, bloc) {
    const el = typeof sel === 'string' ? document.querySelector(sel) : sel;
    if (!el) throw new Error('cible absente : ' + sel);
    const r = el.getBoundingClientRect();
    const vise = scrollY + r.top + r.height / 2 - innerHeight / 2;
    const cible = Math.max(0, Math.min(vise,
      document.documentElement.scrollHeight - innerHeight));
    const depart = scrollY;
    if (Math.abs(cible - depart) < 4) return;
    await anime(Math.min(1400, 420 + Math.abs(cible - depart) * 0.55),
      (t) => scrollTo(0, depart + (cible - depart) * t));
    await dodo(120);
  }

  async function clic(sel) {
    const el = await versElement(sel);
    onde(px, py);
    await dodo(160);
    el.click();
    await dodo(260);
  }

  /* — Le surlignage — il paraît en fondu, et le voile est plus léger qu'à la
       première version : à 55 % d'encre, l'écran autour devenait illisible et
       la capsule ressemblait à une suite de projecteurs. */
  function surligner(sel) {
    effacer();
    const el = document.querySelector(sel);
    if (!el) return;
    const r = el.getBoundingClientRect();
    const m = 8;
    const b = { x: r.left - m, y: r.top - m, w: r.width + m * 2, h: r.height + m * 2 };
    const voile = (x, y, w, h) => {
      const d = document.createElement('div');
      d.className = 'sc-voile';
      d.style.cssText = 'position:absolute;left:' + x + 'px;top:' + y + 'px;width:'
        + Math.max(0, w) + 'px;height:' + Math.max(0, h) + 'px;'
        + 'background:rgba(23,24,26,.38);opacity:0;transition:opacity .45s';
      RACINE.appendChild(d);
      requestAnimationFrame(() => { d.style.opacity = '1'; });
    };
    voile(0, 0, innerWidth, b.y);
    voile(0, b.y + b.h, innerWidth, innerHeight - b.y - b.h);
    voile(0, Math.max(0, b.y), b.x, Math.min(b.h, innerHeight));
    voile(b.x + b.w, Math.max(0, b.y), innerWidth - b.x - b.w, Math.min(b.h, innerHeight));

    const cadre = document.createElement('div');
    cadre.className = 'sc-cadre';
    cadre.style.cssText = 'position:absolute;left:' + b.x + 'px;top:' + b.y + 'px;width:'
      + b.w + 'px;height:' + b.h + 'px;border:3px solid #0A8F5B;border-radius:12px;'
      + 'opacity:0;transition:opacity .45s,transform .45s;transform:scale(1.015)';
    RACINE.appendChild(cadre);
    requestAnimationFrame(() => {
      cadre.style.opacity = '1';
      cadre.style.transform = 'scale(1)';
    });
    /* Le pointeur passerait pour un oubli au milieu d'un plan surligné. */
    POINTEUR.style.opacity = '0';
  }

  function effacer() {
    RACINE.querySelectorAll('.sc-voile, .sc-cadre').forEach((n) => n.remove());
  }

  /* Promener le pointeur sur une série de cibles : c'est ce qui sauve les
     plans purement descriptifs (« quatre onglets : Planifier, Élèves… »).
     Sans lui, l'écran reste immobile pendant vingt secondes et on retombe
     sur un diaporama commenté. La pause est calée sur le rythme de la
     phrase, pas sur un minutage fixe. */
  async function parcourir(cibles, pause) {
    for (const sel of cibles) {
      const el = document.querySelector(sel);
      if (!el) continue;
      const c = centre(el);
      await versPoint(c.x, c.y);
      await dodo(pause ?? 620);
    }
  }

  /* Un balayage lent de la page, pour un plan d'ouverture : on montre
     l'écran plutôt que de le laisser figé. */
  async function survol(bas) {
    const cible = Math.min(bas ?? 420,
      document.documentElement.scrollHeight - innerHeight);
    await anime(2200, (t) => scrollTo(0, cible * t));
    await dodo(300);
    await anime(1400, (t) => scrollTo(0, cible * (1 - t)));
  }

  /* Taper se voit lettre par lettre : poser la valeur d'un coup, c'est
     l'écran qui change tout seul, et le spectateur ne comprend pas qu'il
     s'agit d'une saisie. Chaque frappe déclenche un événement « input »,
     donc les filtres de la page se resserrent sous les yeux.
     (Pas d'accent grave dans ce fichier : tout le corps est un gabarit de
     chaîne, un seul le refermerait.) */
  async function taper(sel, texte, cadence) {
    const el = await versElement(sel);
    onde(px, py);
    await dodo(180);
    el.focus();
    const poser = Object.getOwnPropertyDescriptor(
      el instanceof HTMLTextAreaElement ? HTMLTextAreaElement.prototype
                                        : HTMLInputElement.prototype, 'value').set;
    poser.call(el, '');
    el.dispatchEvent(new Event('input', { bubbles: true }));
    for (const lettre of texte) {
      poser.call(el, el.value + lettre);
      el.dispatchEvent(new Event('input', { bubbles: true }));
      await dodo(cadence ?? 65);
    }
    el.dispatchEvent(new Event('change', { bubbles: true }));
    await dodo(320);
  }

  /* Une liste déroulante ne s'ouvre pas dans un navigateur sans affichage :
     le menu natif est dessiné par le système, pas par la page. On amène donc
     le pointeur dessus, on marque le clic, puis on pose la valeur — ce qui se
     lit exactement comme un choix. */
  async function choisir(sel, texte) {
    const el = await versElement(sel);
    onde(px, py);
    await dodo(240);
    const option = Array.from(el.options).find((o) => o.text.includes(texte));
    if (!option) throw new Error('option absente : ' + texte);
    el.value = option.value;
    el.dispatchEvent(new Event('change', { bubbles: true }));
    await dodo(420);
  }

  window.__scene = { versPoint, versElement, defiler, clic, surligner, effacer, dodo,
                     parcourir, survol, taper, choisir, pointeur: POINTEUR };
})();
`;
