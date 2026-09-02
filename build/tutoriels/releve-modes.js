/* Relève de l'espace enseignant : le texte visible et les commandes de chaque
   écran. Lancé deux fois — assistance autorisée, puis interdite — sa sortie se
   compare ligne à ligne. */
const fs = require('fs');
const os = require('os');
const path = require('path');
const puppeteer = require('puppeteer-core');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = process.argv[2], SORTIE = process.argv[3];
const dodo = (ms) => new Promise((r) => setTimeout(r, ms));

function identifiants() {
  const bac = process.env.STORAGE_DIR || path.join(os.tmpdir(), 'francisation-demo-tutoriels');
  for (const n of ['identifiants-tournage.json', 'identifiants-demo.json']) {
    const f = path.join(bac, n);
    if (fs.existsSync(f)) return JSON.parse(fs.readFileSync(f, 'utf8'));
  }
  throw new Error('identifiants introuvables');
}

const releveDom = () => {
  const vu = (el) => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0 && el.offsetParent !== null;
  };
  const cmd = [...document.querySelectorAll('button, a, select, input[type=checkbox]')]
    .filter(vu)
    .map((e) => `${e.tagName.toLowerCase()} · ${(e.textContent || e.value || e.id || '').trim().replace(/\s+/g, ' ').slice(0, 70)}`);
  const texte = (document.querySelector('#portail') || document.body).innerText
    .split('\n').map((l) => l.trim()).filter(Boolean);
  return { cmd, texte };
};

(async () => {
  const nav = await puppeteer.launch({ executablePath: CHROME, headless: 'new',
    args: ['--hide-scrollbars'] });
  const page = await nav.newPage();
  await page.setViewport({ width: 1600, height: 1200 });
  const c = identifiants();
  await page.goto(`http://localhost:${PORT}/enseignant.html`, { waitUntil: 'networkidle2' });
  await page.evaluate((c) => {
    const poser = (el, v) => {
      Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set.call(el, v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    };
    poser(document.getElementById('code'), c.code);
    poser(document.getElementById('motDePasse'), c.motDePasse);
    document.getElementById('formConnexion').requestSubmit();
  }, c);
  await page.waitForSelector('#portail:not([hidden])', { timeout: 20000 });
  await dodo(1500);

  const out = [];
  for (const ecran of ['accueil', 'planif', 'materiel', 'eleves', 'groupes']) {
    if (ecran !== 'accueil') {
      await page.evaluate((e) => {
        const el = [...document.querySelectorAll(`[data-ecran="${e}"]`)]
          .find((x) => x.offsetParent !== null);
        if (el) el.click();
      }, ecran);
      await dodo(2500);
    }
    const r = await page.evaluate(releveDom);
    out.push(`########## ÉCRAN ${ecran}`);
    out.push('--- commandes'); out.push(...r.cmd);
    out.push('--- texte'); out.push(...r.texte);
  }
  /* Le compositeur : une page à part, ouverte hors du portail. */
  await page.goto(`http://localhost:${PORT}/assets/outils/compositeur-activite.html?de=enseignant`,
    { waitUntil: 'networkidle2' });
  await dodo(2500);
  const r = await page.evaluate(releveDom);
  out.push('########## PAGE compositeur');
  out.push('--- commandes'); out.push(...r.cmd);
  out.push('--- texte'); out.push(...r.texte);

  fs.writeFileSync(SORTIE, out.join('\n'));
  await nav.close();
  console.log('relevé écrit :', SORTIE, out.length, 'lignes');
})().catch((e) => { console.error('ÉCHEC :', e.message); process.exit(1); });
