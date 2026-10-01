// Les captures du dépliant d'« Une semaine à Toronto », prises sur la vraie page.
//
//     node build/toronto_captures.mjs [port]     # serveur local (5412 par défaut)
//
// Copie de build/hotel_captures.mjs : Chrome piloté par son protocole (WebSocket de Node),
// 390 × 844, densité 2, un profil vierge par capture. La semaine jouée est capturée avec un
// FAUX SERVEUR injecté dans la page (window.fetch remplacé) : une scène écrite d'avance au
// restaurant, sans aucun appel payant, et une capture qui se refait à l'identique.
import { spawn } from 'node:child_process';
import { mkdtempSync, writeFileSync, rmSync, mkdirSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const RACINE = join(dirname(fileURLToPath(import.meta.url)), '..');
const DEST = join(RACINE, 'modules-autonomes', 'toronto', 'depliant');
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = process.argv[2] || '5412';
const BASE = `http://localhost:${PORT}/modules-autonomes/toronto/`;
const pause = ms => new Promise(r => setTimeout(r, ms));

// L'état d'un voyageur à mi-semaine : séances faites, trois cartes gagnées, une écrite.
const ETAT = `localStorage.setItem('toronto:v1', JSON.stringify({lent:false, aide:false, avisMicro:'1er oct. 2026', genre:'',
  prep:{p1:{faits:{ecoute:1,quiz:1,dire:1},fin:'1'},p2:{faits:{ecoute:1,quiz:1,dire:1},fin:'1'},p3:{faits:{ecoute:1,quiz:1,dire:1},fin:'1'},
        p4:{faits:{ecoute:1,quiz:1,dire:1},fin:'1'},p5:{faits:{ecoute:1,quiz:1,dire:1},fin:'1'}},
  cartes:{union:'1er oct. 2026', hotel:'1er oct. 2026', cafe:'2 oct. 2026'},
  ecrits:{cafe:"Hi Léa! This morning I had a coffee in a small café on King Street. The muffins here are huge!"},
  exos:{totaux:'5 sur 6', allergie:'4 sur 4'}})); localStorage.setItem('toronto:code', 'PCDEMO24');`;

// Le faux serveur du restaurant : deux tours, puis le bilan.
const FAUX = `(() => { let k = 0; const R = [
  "Hi there, welcome in! Table for one tonight?",
  "Thanks for telling me. The pasta and the chicken are nut-free; the salmon has a pecan crust, so I'd skip it.",
  "Great choice, the pasta it is. Anything to drink?"];
  const bilan = {resume:"Vous avez dit votre allergie avant de commander et choisi un plat sans noix.",
    compris:["Vous avez dit votre allergie aux noix avant de commander.","Vous avez commandé les pâtes, un plat sans noix."],
    phrases:[{dit:"I take the pasta please.", mieux:"I'll have the pasta, please."}],
    gestes:[{geste:"a",fait:true},{geste:"b",fait:true},{geste:"c",fait:true}],
    conseil:"Pour commander, « I'll have… » est la formule la plus naturelle.", reussi:true};
  window.fetch = async (u, o) => { const b = o && o.body ? JSON.parse(o.body) : {};
    const rep = x => new Response(JSON.stringify(x), {status:200, headers:{'Content-Type':'application/json'}});
    if (String(u).includes('/api/pelerins/etat')) return rep({code:'PCDEMO24', actif:true, restant:21, expire:'2027-10-01', toursMax:16, produit:'toronto'});
    if (String(u).includes('/api/pelerins/offre')) return rep({ouverte:false});
    if (String(u).includes('/api/voix')) return new Response('', {status:503});
    if (b.bilan) return rep({bilan});
    const r = {reponse: R[k++] || 'Enjoy your meal!'}; if (!b.historique || !b.historique.length) r.ouverture = 'Hi!'; return rep(r); };
})();`;

const ECRANS = [
  ['accueil', '#accueil', ''],
  ['semaine', '#semaine', ''],
  ['situation', '#semaine/resto/jouer', ''],
  ['conversation', '#semaine/resto/jouer', `${FAUX} document.querySelector('#go').click(); await p(700);
     const t = document.querySelector('#txt'); t.value = 'Just me. I am allergic to nuts.'; document.querySelector('#env').click(); await p(700);
     t.value = 'I take the pasta please.'; document.querySelector('#env').click(); await p(700);`],
  ['bilan', '#semaine/resto/jouer', `${FAUX} document.querySelector('#go').click(); await p(700);
     const t = document.querySelector('#txt'); t.value = 'Just me. I am allergic to nuts.'; document.querySelector('#env').click(); await p(700);
     t.value = 'I take the pasta please.'; document.querySelector('#env').click(); await p(700);
     document.querySelector('#fin').click(); await p(1200); document.querySelector('#saisie').scrollIntoView(); window.scrollBy(0, -10);`],
  ['carte', '#semaine/cafe', ''],
  ['exercice', '#exos/totaux', ''],
  ['poche', '#poche', `const x = document.querySelector('#prix'); x.value = '50'; x.oninput(); document.querySelector('[data-pb="18"]').click();`],
];

async function capturer(nom, ancre, geste, port) {
  const profil = mkdtempSync(join(tmpdir(), 'to-'));
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
    await cmd('Page.navigate', { url: BASE + '#accueil' }); await pause(1500);
    await cmd('Runtime.evaluate', { expression: ETAT });
    await cmd('Page.navigate', { url: BASE + '?d=' + Date.now() + ancre }); await pause(2500);
    if (geste) {
      const r = await cmd('Runtime.evaluate', { expression: `(async () => { const p = ms => new Promise(r => setTimeout(r, ms)); ${geste} return 'ok'; })()`, awaitPromise: true });
      if (r.exceptionDetails) console.log('  ', nom, 'ERREUR', JSON.stringify(r.exceptionDetails).slice(0, 300));
      await pause(800);
    }
    const { data } = await cmd('Page.captureScreenshot', { format: 'jpeg', quality: 82 });
    writeFileSync(join(DEST, `${nom}.jpg`), Buffer.from(data, 'base64'));
    console.log(`  ${nom.padEnd(12)} ${Math.round(Buffer.from(data, 'base64').length / 1024)} ko`);
    ws.close();
  } finally {
    chrome.kill(); await pause(300);
    rmSync(profil, { recursive: true, force: true });
  }
}

mkdirSync(DEST, { recursive: true });
let port = 9441;
for (const [nom, ancre, geste] of ECRANS) await capturer(nom, ancre, geste, port++);
