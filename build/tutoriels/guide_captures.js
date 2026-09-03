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
const { jouer, ouvrirSession, dodo, LARGEUR, HAUTEUR, CHROME, ICI } =
  require('./enregistrer.js');

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
  return page.evaluate((s, m) => {
    const vu = [...document.querySelectorAll(s)].find((e) => {
      const r = e.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && e.offsetParent !== null;
    });
    if (!vu) return null;
    const r = vu.getBoundingClientRect();
    const x = Math.max(0, r.left - m);
    const y = Math.max(0, r.top - m);
    return {
      x, y,
      width: Math.min(innerWidth - x, r.width + m * 2),
      height: Math.min(innerHeight - y, r.height + m * 2),
    };
  }, sel, MARGE);
}

async function prendre(page, fichier, sel) {
  const clip = await cadre(page, sel);
  await page.screenshot({ path: fichier, type: 'jpeg', quality: 88,
                          ...(clip && clip.width > 60 && clip.height > 60 ? { clip } : {}) });
  return crypto.createHash('md5').update(fs.readFileSync(fichier)).digest('hex');
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
        const empreinte = await prendre(page, f, plan.surligne);
        if (vus.has(empreinte)) { fs.unlinkSync(f); return; }
        vus.add(empreinte);
        images.push({ quand, fichier: path.relative(ICI, f) });
      };

      /* Le surlignage d'abord : c'est ce que le spectateur voit pendant tout
         le plan, donc ce que le guide doit montrer. */
      if (plan.surligne) {
        await page.evaluate((s) => window.__scene.surligner(s), plan.surligne);
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
        await clic(i, i + 1 === gestes.length ? 'fin' : 'geste' + (i + 1));
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
