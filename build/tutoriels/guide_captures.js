#!/usr/bin/env node
/* Les copies d'écran du guide de validation.
 *
 * Rejoue les gestes du manifeste sur le portail de démonstration — les mêmes
 * gestes, par la même fonction que le tournage — et prend une image au début,
 * au milieu et à la fin de chaque plan. Aucune voix n'est synthétisée : c'est
 * tout l'intérêt. Le guide se relit et se corrige avant qu'un seul appel ne
 * parte chez Azure, et avant qu'on enregistre quoi que ce soit.
 *
 *     node build/tutoriels/guide_captures.js 5321 [idCapsule]
 *
 * Sortie : `guide/<capsule>/<plan>-N.jpg` et `guide/captures.json`.
 *
 * Ce qui est cadré : quand le plan porte un `surligne`, l'image est **rognée
 * sur l'élément surligné**, avec de la marge. Une pleine page à 1600 pixels
 * réduite à la largeur d'une colonne ne montre plus rien de lisible, et un
 * guide papier dont on ne lit pas les copies d'écran ne vaut pas mieux que
 * pas de guide. Sans `surligne`, on garde la fenêtre entière.
 *
 * Les images identiques sont retirées : un plan dont l'écran ne bouge pas
 * n'a pas besoin de trois vignettes du même écran.
 */
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const puppeteer = require('puppeteer-core');
const { jouer, ouvrirSession, dodo, surveillerFenetres,
        LARGEUR, HAUTEUR, CHROME, ICI } = require('./enregistrer.js');

const PORT = process.argv[2];
const SEULE = process.argv[3] || null;
const SORTIE = path.join(ICI, 'guide');
const MARGE = 40;

/* La cadence des voix HD d'Azure, relevée sur les 54 fichiers déjà
   synthétisés : 1 888 mots en 695,8 s. Elle sert à estimer la durée d'un plan
   sans rien synthétiser. C'est un ordre de grandeur — la synthèse HD n'est pas
   déterministe, deux tirages du même texte ne durent pas pareil. */
const MOTS_PAR_SECONDE = 2.71;
const RESPIRATION = 0.7;

const duree = (texte) => {
  const mots = (texte.match(/[\wÀ-ÿ'’-]+/g) || []).length;
  return Math.round((mots / MOTS_PAR_SECONDE + RESPIRATION) * 10) / 10;
};

async function cadre(page, sel) {
  if (!sel) return null;
  /* L'élément est d'abord AMENÉ à l'écran, d'un coup, puis mesuré. La première
     version mesurait sans bouger et bornait le rectangle à la fenêtre : un
     formulaire sous le bord bas donnait une bande de 40 pixels (donc la pleine
     page, par repli), et un formulaire au-dessus donnait une bande prise en
     haut de l'écran — le titre « Vos groupes » à la place du formulaire.
     Quarante-huit étapes, la moitié fausses, sans une erreur. Vu en mettant
     les captures de l'utilisateur à côté des miennes, le 4 septembre 2026. */
  return page.evaluate(async (s, m) => {
    const vu = [...document.querySelectorAll(s)].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && e.offsetParent !== null;
    });
    if (!vu) return null;
    let r = vu.getBoundingClientRect();
    /* Plus haut que l'écran — une liste de 4 700 px, la colonne du matériel —
       on ne cadre pas : on garde la fenêtre telle que les gestes l'ont laissée,
       c'est-à-dire ce que le film montre au même instant. Le centrer donnait
       le milieu d'une liste, des rangées prises au hasard. */
    if (r.height > innerHeight - m * 2) return null;
    if (r.top < m || r.bottom > innerHeight - m) {
      const vise = scrollY + r.top + r.height / 2 - innerHeight / 2;
      scrollTo({ top: Math.max(0, vise), behavior: 'instant' });
      await new Promise((ok) => setTimeout(ok, 250));
      r = vu.getBoundingClientRect();
    }
    /* Un bouton de 44 px cadré seul ne dit pas où il est : le cadre a une
       taille plancher, centrée sur l'élément, pour qu'on lise ce qui l'entoure. */
    const MIN_L = 720, MIN_H = 240;
    const cx = r.left + r.width / 2, cy = r.top + r.height / 2;
    const l = Math.max(r.width + m * 2, MIN_L), h = Math.max(r.height + m * 2, MIN_H);
    const x = Math.max(0, Math.min(cx - l / 2, innerWidth - l));
    const y = Math.max(0, Math.min(cy - h / 2, innerHeight - h));
    /* Le rectangle que Puppeteer 25 attend est en coordonnées de
       **document**, pas de fenêtre : sur une page défilée de 1 200 px, un
       cadre mesuré dans la fenêtre tombait 1 200 px trop haut — la carte du
       groupe à la place de la barre de rythmes, huit images sur quarante-huit.
       D'où le décalage de `scrollX` / `scrollY`. Entiers, parce que Chrome
       refuse un demi-pixel au bord (« 0 height »). */
    return {
      x: Math.floor(x + scrollX), y: Math.floor(y + scrollY),
      width: Math.floor(Math.min(innerWidth - x, l)),
      height: Math.floor(Math.min(innerHeight - 1 - y, h)),
      mesure: { top: Math.round(r.top), h: Math.round(r.height), scrollY: Math.round(scrollY),
                n: document.querySelectorAll(s).length, tag: vu.tagName + (vu.id ? '#' + vu.id : '') },
    };
  }, sel, MARGE);
}

async function prendre(page, fichier, sel) {
  const clip = await cadre(page, sel);
  const mesure = clip ? clip.mesure : null;
  if (clip) delete clip.mesure;
  const cadrer = clip && clip.width > 60 && clip.height > 60;
  try {
    await page.screenshot({ path: fichier, type: 'jpeg', quality: 88, ...(cadrer ? { clip } : {}) });
  } catch (e) {
    /* Un cadre que Chrome refuse (« 0 height ») : on garde la fenêtre entière
       et on le dit, plutôt que d'arrêter quarante-huit captures pour une. */
    process.stdout.write('  ⚠ cadre refusé ' + JSON.stringify(clip) + ' : ' + e.message + '\n');
    await page.screenshot({ path: fichier, type: 'jpeg', quality: 88 });
  }
  return { empreinte: crypto.createHash('md5').update(fs.readFileSync(fichier)).digest('hex'),
           mesure, clip };
}

(async () => {
  const manifeste = JSON.parse(fs.readFileSync(path.join(ICI, 'manifeste.json'), 'utf8'));
  fs.mkdirSync(SORTIE, { recursive: true });
  const navigateur = await puppeteer.launch({
    executablePath: CHROME, headless: 'new',
    args: ['--force-device-scale-factor=1', '--hide-scrollbars'],
  });
  const page = await navigateur.newPage();
  await page.setViewport({ width: LARGEUR, height: HAUTEUR, deviceScaleFactor: 2 });
  surveillerFenetres(navigateur, page);
  await ouvrirSession(page, PORT);

  const releve = {};
  for (const capsule of manifeste.capsules) {
    const garder = !SEULE || capsule.id === SEULE;
    const dossier = path.join(SORTIE, capsule.id);
    if (garder) {
      fs.rmSync(dossier, { recursive: true, force: true });
      fs.mkdirSync(dossier, { recursive: true });
    }
    /* Même règle qu'au tournage : aucune fenêtre héritée à l'image. */
    await page.evaluate(() => document.querySelectorAll('[data-fermer]')
      .forEach((b) => { if (b.offsetParent !== null) b.click(); }));
    for (const geste of (capsule.prepare || [])) await jouer(page, geste);
    await dodo(400);

    releve[capsule.id] = [];
    for (const plan of capsule.plans) {
      await page.evaluate(() => window.__scene?.effacer());
      const gestes = plan.gestes || [];
      const images = [];
      const vus = new Set();
      const clic = async (n, quand) => {
        if (!garder) return;
        const f = path.join(dossier, `${plan.id}-${quand}.jpg`);
        const { empreinte, mesure, clip } = await prendre(page, f, vise);
        if (vus.has(empreinte)) { fs.unlinkSync(f); return; }
        vus.add(empreinte);
        /* `geste` compte les gestes joués : 0 au début du plan, k après le k-ième. */
        images.push({ quand, geste: n, fichier: path.relative(ICI, f), mesure, clip });
      };

      /* Le surlignage suit **le cadrage du papier**, pas celui du film.

         Les deux diffèrent quand `papier.cadre` est posé : à la capsule 7, le
         film encadre la jauge de jetons (`#barre`, dix pixels de haut) pendant
         que le guide cadre les boutons qui la suivent. Surligner le premier et
         cadrer le second donnait un rectangle vert flottant au-dessus du
         texte, décalé de sa cible — relevé à la page 29 du guide, le
         4 septembre 2026. Le cadre vert doit entourer ce que l'image montre,
         sans quoi il désigne quelque chose qui n'est pas là. */
      const vise = (plan.papier && plan.papier.cadre) || plan.surligne;
      if (vise) {
        await page.evaluate((s) => window.__scene.surligner(s), vise);
        await dodo(500);
      }
      /* Une image APRÈS CHAQUE GESTE, et non plus début-milieu-fin.
         « Il y a comme pas assez de copies d'écran » — relevé au visionnement
         de la capsule 2, le 3 septembre 2026 : la voix nommait la liste des
         niveaux et le storyboard n'en montrait aucune. Les images identiques
         sont écartées, donc un plan où l'écran ne bouge pas n'en donne qu'une,
         et un plan qui montre six choses en donne six. */
      await clic(0, 'debut');
      for (const [i, geste] of gestes.entries()) {
        await jouer(page, geste);
        await dodo(200);
        await clic(i + 1, i + 1 === gestes.length ? 'fin' : 'geste' + (i + 1));
      }
      releve[capsule.id].push({
        plan: plan.id, secondes: duree(plan.texte_voix || plan.texte), images,
      });
      if (garder) process.stdout.write(`  ${capsule.id}_${plan.id} · ${images.length} image(s)\n`);
    }
    /* On s'arrête à la capsule demandée. Les précédentes ont dû être jouées —
       chacune hérite de l'écran que la précédente a laissé — mais celles
       d'après ne servent à rien, et elles coûtent une minute chacune au bouton
       « Mettre à jour ». */
    if (SEULE && capsule.id === SEULE) break;
  }
  fs.writeFileSync(path.join(SORTIE, 'captures.json'), JSON.stringify(releve, null, 1));
  await navigateur.close();
  console.log('captures écrites dans', path.relative(process.cwd(), SORTIE));
})().catch((e) => { console.error('ÉCHEC :', e.message); process.exit(1); });
