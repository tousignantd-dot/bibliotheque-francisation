// La version PDF des quatre dépliants, posée à côté de chacun (presentation.pdf).
//
//     node build/depliants_pdf.mjs [port]      # serveur local (5497 par défaut)
//
// Demande de Daniel, 2 oct. 2026 : « fais une version pdf de chacun des dépliants ».
// Les dépliants sont faits pour l'écran : imprimés avec leur @media print, ils sortaient en
// 11 à 16 pages à moitié vides, téléphones superposés (relu sur planche-contact). On imprime donc
// la VERSION ÉCRAN (Emulation.setEmulatedMedia screen), à 820 px de large, réduite sur une page
// lettre, fonds compris, et on interdit seulement de couper une capture, une carte ou un titre.
// Chrome piloté par son protocole (WebSocket de Node), comme build/toronto_captures.mjs.
// Le prix est FIGÉ dans le PDF au moment de l'impression : refaire après un changement de prix.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const RACINE = join(dirname(fileURLToPath(import.meta.url)), '..');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = process.argv[2] || '5497';
const DEPLIANTS = ['compostelle', 'toronto', 'francoeur-planches', 'hotel-reception'];
const pause = ms => new Promise(r => setTimeout(r, ms));

// Ce qu'on ne coupe jamais en deux, et ce qui n'a rien à faire sur papier.
const CSS = `
  img, svg, figure, .tel, .tels, .visuel, .carte, .card, .etape, .chiffre, .chiffres > *, .qrb, details,
  h1, h2, h3, h4, li, tr, .prix, .offre, .bloc, .encadre { break-inside: avoid; }
  h1, h2, h3 { break-after: avoid; }
  .retour, .cta, nav.sticky { display: none !important; }
  details > *:not(summary) { display: block !important; }
  html, body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }`;

async function imprimer(slug, port) {
  const profil = mkdtempSync(join(tmpdir(), 'dep-'));
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
    `--remote-debugging-port=${port}`, `--user-data-dir=${profil}`, 'about:blank'], { stdio: 'ignore' });
  try {
    let cibles;
    for (let i = 0; i < 50 && !cibles; i++) {
      try { cibles = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); } catch (e) { await pause(100); }
    }
    const ws = new WebSocket(cibles.find(c => c.type === 'page').webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r, { once: true }));
    let n = 0; const attente = new Map();
    ws.addEventListener('message', ev => { const m = JSON.parse(ev.data); if (m.id && attente.has(m.id)) { attente.get(m.id)(m.result); attente.delete(m.id); } });
    const cmd = (method, params = {}) => new Promise(r => { const id = ++n; attente.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
    await cmd('Page.enable');
    await cmd('Emulation.setDeviceMetricsOverride', { width: 820, height: 1100, deviceScaleFactor: 2, mobile: false });
    await cmd('Emulation.setEmulatedMedia', { media: 'screen' });
    await cmd('Page.navigate', { url: `http://localhost:${PORT}/modules-autonomes/${slug}/presentation.html` });
    await pause(3500);
    // Les images paresseuses : on les force, puis on attend qu'elles soient toutes là.
    await cmd('Runtime.evaluate', { awaitPromise: true, expression: `(async () => {
      document.querySelectorAll('img[loading="lazy"]').forEach(i => i.loading = 'eager');
      const s = document.createElement('style'); s.textContent = ${JSON.stringify(CSS)}; document.head.append(s);
      document.querySelectorAll('details').forEach(d => d.open = true);
      await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
      await document.fonts.ready; })()` });
    await pause(800);
    const r = await cmd('Page.printToPDF', { paperWidth: 8.5, paperHeight: 11, printBackground: true, scale: 0.78,
      marginTop: 0.4, marginBottom: 0.4, marginLeft: 0.4, marginRight: 0.4, preferCSSPageSize: false });
    const sortie = join(RACINE, 'modules-autonomes', slug, 'presentation.pdf');
    const b = Buffer.from(r.data, 'base64');
    writeFileSync(sortie, b);
    const boites = new Set([...b.toString('latin1').matchAll(/\/MediaBox\s*\[\s*0 0 ([\d.]+) ([\d.]+)/g)].map(m => m[1] + 'x' + m[2]));
    const pages = (b.toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length;
    if (boites.size !== 1 || !boites.has('612x792')) throw new Error(`${slug} : format inattendu ${[...boites]}`);
    console.log(`modules-autonomes/${slug}/presentation.pdf — ${pages} pages lettre, ${Math.round(b.length / 1024)} Ko`);
    ws.close();
  } finally {
    chrome.kill(); await pause(300); rmSync(profil, { recursive: true, force: true });
  }
}

let p = 9301;
for (const s of DEPLIANTS) await imprimer(s, p++);
