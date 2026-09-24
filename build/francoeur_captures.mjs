// Les captures de la démo de la Maison Francœur, refaites depuis la vraie page.
//
//     node build/francoeur_captures.mjs      # serveur du dépôt sur localhost:5412
//
// Les images de assets/presentations/francoeur-captures/ montraient l'ancienne
// trousse après le passage à la palette Denim : une capture ne suit pas la page
// toute seule. `chrome --screenshot` ne rend jamais la main sur cette page (le
// son lancé à l'ouverture tient le temps virtuel) ; on pilote donc Chrome par
// son protocole de débogage — le WebSocket est intégré à Node depuis la v22,
// rien à installer. Format téléphone 390 × 844, densité 2, et un profil vierge
// par capture : aucune trace d'une passation précédente.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const RACINE = join(dirname(fileURLToPath(import.meta.url)), '..');
const DEST = join(RACINE, 'assets', 'presentations', 'francoeur-captures');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const BASE = 'http://localhost:5412/modules-autonomes/francoeur-planches/index.html';
const ECRANS = [
  ['langue', 'ecran=langue'],
  ['rayons', 'langue=es&ecran=rayons'],
  ['planche', 'langue=es&ecran=planche&p=exterieur'],
  ['fiche', 'langue=ar&ecran=planche&p=hauts&a=veste&voir=1'],
  ['client', 'langue=es&ecran=exercice&x=client'],
  ['magasin', 'langue=fr&ecran=magasin&niveau=aise&code=DEMO00'],
];
const pause = ms => new Promise(r => setTimeout(r, ms));

async function capturer(nom, q, port) {
  const profil = mkdtempSync(join(tmpdir(), 'mf-'));
  const chrome = spawn(CHROME, ['--headless=new', '--disable-gpu', '--hide-scrollbars', '--mute-audio',
    `--remote-debugging-port=${port}`, `--user-data-dir=${profil}`, 'about:blank'], { stdio: 'ignore' });
  try {
    let cibles;
    for (let i = 0; i < 50 && !cibles; i++) {
      try { cibles = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json(); } catch (e) { await pause(100); }
    }
    const page = cibles.find(c => c.type === 'page');
    const ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise(r => ws.addEventListener('open', r, { once: true }));
    let n = 0; const attente = new Map();
    ws.addEventListener('message', ev => { const m = JSON.parse(ev.data); if (m.id && attente.has(m.id)) { attente.get(m.id)(m.result); attente.delete(m.id); } });
    const cmd = (method, params = {}) => new Promise(r => { const id = ++n; attente.set(id, r); ws.send(JSON.stringify({ id, method, params })); });
    await cmd('Emulation.setDeviceMetricsOverride', { width: 390, height: 844, deviceScaleFactor: 2, mobile: true });
    await cmd('Page.enable');
    await cmd('Page.navigate', { url: `${BASE}?${q}&capture=1` });
    await pause(3500);                                   // images, polices, traduction
    const { data } = await cmd('Page.captureScreenshot', { format: 'png' });
    writeFileSync(join(DEST, `${nom}.png`), Buffer.from(data, 'base64'));
    console.log(`  ${nom.padEnd(8)} ${Math.round(Buffer.from(data, 'base64').length / 1024)} ko`);
    ws.close();
  } finally {
    chrome.kill();
    await pause(300);
    rmSync(profil, { recursive: true, force: true });
  }
}

let port = 9331;
for (const [nom, q] of ECRANS) await capturer(nom, q, port++);
