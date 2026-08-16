/* Capture les plans du manifeste dans le portail enseignant.
   Chrome déjà installé sur le poste, piloté par puppeteer-core : aucun
   navigateur téléchargé. La session est ouverte une seule fois, puis les
   capsules se jouent à la suite — rouvrir la session à chaque plan
   remettrait le portail sur l'onglet Planifier. */
const fs = require('fs');
const os = require('os');
const path = require('path');
const puppeteer = require('puppeteer-core');

/* Le compte de démonstration, lu dans le bac à sable — jamais écrit ici.
   `lancer_demo.sh` tire le mot de passe au hasard au premier lancement et le
   dépose à côté du stockage jetable. L'écrire dans ce fichier le ferait
   partir sur GitHub à chaque commit. */
function identifiants() {
  const bac = process.env.STORAGE_DIR
    || path.join(os.tmpdir(), 'francisation-demo-tutoriels');
  const fichier = path.join(bac, 'identifiants-demo.json');
  if (fs.existsSync(fichier)) return JSON.parse(fs.readFileSync(fichier, 'utf8'));
  if (process.env.PROF_COURRIEL && process.env.PROF_MOTDEPASSE) {
    return {
      courriel: process.env.PROF_COURRIEL,
      motDePasse: process.env.PROF_MOTDEPASSE,
    };
  }
  throw new Error(`Identifiants introuvables (${fichier}). `
    + "Lancez d'abord ./build/tutoriels/lancer_demo.sh");
}

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = process.argv[2];
/* `node capturer.js <port> [idCapsule]` — refaire une seule capsule.
   Les gestes des capsules précédentes sont **rejoués quand même**, sans
   capture : l'état de l'écran d'une capsule dépend de celles d'avant
   (un onglet ouvert, une case cochée), et repartir du portail neuf
   donnerait d'autres images que la première fois. */
const SEULE = process.argv[3] || null;
const SORTIE = path.join(__dirname, 'plans');
const manifeste = JSON.parse(fs.readFileSync(path.join(__dirname, 'manifeste.json'), 'utf8'));

/* 1600 × 900, soit le 16:9 du montage. Le facteur 2 donne du 3200 × 1800 :
   redescendu en 1080p, le texte de 15 px reste net. */
const LARGEUR = 1600, HAUTEUR = 900, ECHELLE = 2;

const dodo = (ms) => new Promise((r) => setTimeout(r, ms));

/* Le surlignage : on assombrit la page et on découpe une fenêtre nette
   autour de la pièce dont parle la voix. Quatre voiles plutôt qu'un
   `box-shadow` géant — le voile doit s'arrêter au pixel près sur les bords
   de l'écran, sinon un halo gris traîne dans le montage. */
async function surligner(page, selecteur) {
  await page.evaluate((sel) => {
    document.querySelectorAll('.cap-voile, .cap-cadre').forEach((n) => n.remove());
    const el = document.querySelector(sel);
    if (!el) return;
    const r = el.getBoundingClientRect();
    const m = 8;
    const boite = { x: r.left - m, y: r.top - m, w: r.width + m * 2, h: r.height + m * 2 };
    const voile = (x, y, w, h) => {
      const d = document.createElement('div');
      d.className = 'cap-voile';
      d.style.cssText = `position:fixed;left:${x}px;top:${y}px;width:${w}px;height:${h}px;`
        + 'background:rgba(23,24,26,.55);z-index:9998;pointer-events:none';
      document.body.appendChild(d);
    };
    const W = innerWidth, H = innerHeight;
    voile(0, 0, W, Math.max(0, boite.y));
    voile(0, boite.y + boite.h, W, Math.max(0, H - boite.y - boite.h));
    voile(0, Math.max(0, boite.y), Math.max(0, boite.x), Math.min(boite.h, H));
    voile(boite.x + boite.w, Math.max(0, boite.y), Math.max(0, W - boite.x - boite.w), Math.min(boite.h, H));
    const cadre = document.createElement('div');
    cadre.className = 'cap-cadre';
    cadre.style.cssText = `position:fixed;left:${boite.x}px;top:${boite.y}px;`
      + `width:${boite.w}px;height:${boite.h}px;border:3px solid #0A8F5B;border-radius:12px;`
      + 'box-shadow:0 0 0 3px rgba(10,143,91,.25);z-index:9999;pointer-events:none';
    document.body.appendChild(cadre);
  }, selecteur);
}

const nettoyer = (page) => page.evaluate(() =>
  document.querySelectorAll('.cap-voile, .cap-cadre').forEach((n) => n.remove()));

async function jouer(page, geste) {
  switch (geste.do) {
    case 'onglet':
      await page.evaluate((v) => document.querySelector(`.pe-onglet[data-ecran="${v}"]`)?.click(), geste.valeur);
      break;
    case 'clic':
      await page.evaluate((s) => document.querySelector(s)?.click(), geste.sel);
      break;
    case 'js':
      await page.evaluate(geste.code);
      break;
    case 'attendre':
      await dodo(geste.ms);
      break;
    case 'defiler':
      /* `scrollIntoView` centre la pièce : un élément collé en haut de la
         fenêtre passe sous les deux bandes fixes du portail. */
      await page.evaluate((s) => document.querySelector(s)
        ?.scrollIntoView({ block: 'center', behavior: 'instant' }), geste.sel);
      await dodo(250);
      break;
    case 'cocher':
      await page.evaluate((n) => {
        Array.from(document.querySelectorAll('[data-coche]')).slice(0, n)
          .forEach((c) => { if (!c.checked) c.click(); });
      }, geste.n);
      await dodo(400);
      break;
    case 'deplier':
      await page.evaluate(() => document.querySelector('.pe-chevron')?.click());
      await dodo(500);
      break;
    /* Déplier n'importe quel chevron ne donne pas des sections : un atelier
       se déplie sur sa seule fiche pédagogique. On cherche donc le premier
       module qui a réellement des sections, et on garde celui-là. */
    case 'deplier-module':
      await page.evaluate(() => {
        document.querySelector('.choice[data-filtre="cours"]')?.click();
      });
      await dodo(600);
      await page.evaluate(() => {
        const chevrons = Array.from(document.querySelectorAll('.pe-chevron[data-deploi]'));
        for (const c of chevrons) {
          if (c.getAttribute('aria-expanded') !== 'true') c.click();
          const rangee = c.closest('.pe-rangee');
          const sections = rangee?.parentElement?.querySelector('.pe-sections');
          if (sections) { c.dataset.capGarde = '1'; return; }
          if (c.getAttribute('aria-expanded') === 'true') c.click();
        }
      });
      await dodo(700);
      await page.evaluate(() => document.querySelector('.pe-sections')
        ?.scrollIntoView({ block: 'center', behavior: 'instant' }));
      await dodo(300);
      break;
    /* Le catalogue rend les modules repliés : leurs seize séances
       n'existent dans le document qu'une fois « Voir le matériel » cliqué.
       On ouvre donc les modules l'un après l'autre jusqu'à trouver le code
       demandé — les dépôts d'enseignant sont posés sur des séances
       précises, et c'est celles-là que la capsule doit montrer. */
    case 'ouvrir-module':
    case 'ouvrir-seance': {
      const present = (code) => page.evaluate((c) => (c
        ? Array.from(document.querySelectorAll('.mat-seance-code'))
            .some((n) => n.textContent.trim() === c)
        : document.querySelectorAll('.mat-seance').length > 0), code || null);

      const boutons = await page.$$eval('#matColonne [data-action="deplier"]',
        (n) => n.map((b) => b.dataset.id));
      /* Le bouton bascule : le recliquer sur un module déjà ouvert le
         refermerait. Un plan précédent ayant pu l'ouvrir, on ne touche à
         rien si la séance visée est déjà à l'écran. */
      let trouve = await present(geste.code);
      for (const id of (trouve ? [] : boutons)) {
        await page.evaluate((i) => {
          const b = document.querySelector(`#matColonne [data-action="deplier"][data-id="${i}"]`);
          b?.scrollIntoView({ block: 'center', behavior: 'instant' });
          b?.click();
        }, id);
        await dodo(700);
        trouve = await present(geste.code);
        if (trouve) break;
      }
      if (!trouve) {
        throw new Error(geste.code
          ? `séance ${geste.code} introuvable dans le catalogue`
          : 'aucun module ne montre de séances');
      }
      if (geste.do === 'ouvrir-seance') {
        await page.evaluate((code) => {
          const cell = Array.from(document.querySelectorAll('.mat-seance-code'))
            .find((c) => c.textContent.trim() === code);
          const rangee = cell?.closest('.mat-seance');
          rangee?.scrollIntoView({ block: 'center', behavior: 'instant' });
          rangee?.querySelector('.mat-seance-titre')?.click();
        }, geste.code);
        await dodo(500);
      }
      break;
    }
    /* Le panneau de détail est collant : `scrollIntoView` sur une de ses
       pièces ferait défiler la page entière au lieu du panneau. */
    case 'defiler-panneau':
      await page.evaluate((sel) => {
        const cible = document.querySelector(`.mat-aside ${sel}`);
        cible?.scrollIntoView({ block: 'center', behavior: 'instant' });
      }, geste.sel);
      await dodo(300);
      break;
    default:
      throw new Error('geste inconnu : ' + geste.do);
  }
}

(async () => {
  fs.mkdirSync(SORTIE, { recursive: true });
  const navigateur = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--force-device-scale-factor=1', '--hide-scrollbars'],
  });
  const page = await navigateur.newPage();
  await page.setViewport({ width: LARGEUR, height: HAUTEUR, deviceScaleFactor: ECHELLE });

  await page.goto(`http://localhost:${PORT}/enseignant.html`, { waitUntil: 'networkidle2' });
  await page.evaluate((compte) => {
    const poser = (el, v) => {
      const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      set.call(el, v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    };
    poser(document.getElementById('courriel'), compte.courriel);
    poser(document.getElementById('motDePasse'), compte.motDePasse);
    document.getElementById('formConnexion').requestSubmit();
  }, identifiants());
  await page.waitForSelector('#portail:not([hidden])', { timeout: 15000 });
  await dodo(1500);
  console.log('session ouverte');

  let total = 0;
  for (const capsule of manifeste.capsules) {
    const garder = !SEULE || capsule.id === SEULE;
    for (const plan of capsule.plans) {
      for (const geste of (plan.gestes || [])) await jouer(page, geste);
      if (!garder) continue;
      await dodo(350);
      if (plan.surligne) await surligner(page, plan.surligne);

      const nom = `${capsule.id}_${plan.id}.png`;
      const options = { path: path.join(SORTIE, nom) };
      /* `cadreSel` cadre sur une pièce de l'écran plutôt que sur des pixels :
         un rectangle écrit à la main se décale dès qu'une rangée s'ajoute
         au-dessus. On garde `cadre` pour les cadrages qui ne suivent aucun
         élément précis. */
      if (plan.cadreSel) {
        const boite = await page.evaluate((sel, marge) => {
          const el = document.querySelector(sel);
          if (!el) return null;
          const r = el.getBoundingClientRect();
          return {
            x: Math.max(0, r.left + scrollX - marge),
            y: Math.max(0, r.top + scrollY - marge),
            width: Math.min(r.width + marge * 2, innerWidth),
            height: Math.min(r.height + marge * 2, innerHeight),
          };
        }, plan.cadreSel, plan.marge ?? 16);
        if (!boite) throw new Error(`cadreSel introuvable : ${plan.cadreSel}`);
        options.clip = boite;
      } else if (plan.cadre) {
        /* `cadre` se lit **en coordonnées d'écran**, comme ce qu'on voit :
           c'est le seul repère stable quand un plan précédent a fait
           défiler la page. Puppeteer, lui, découpe en coordonnées de
           document — d'où le report du défilement. Sans ça, un cadrage
           posé sur un panneau visible ressort en aplat vide. */
        const [x, y, w, h] = plan.cadre;
        const { dx, dy } = await page.evaluate(
          () => ({ dx: window.scrollX, dy: window.scrollY }));
        options.clip = { x: x + dx, y: y + dy, width: w, height: h };
      }
      await page.screenshot(options);
      await nettoyer(page);
      total += 1;
      console.log(`  ${nom}`);
    }
    if (garder) console.log(`✓ ${capsule.id}`);
  }
  await navigateur.close();
  console.log(`${total} plans capturés`);
})().catch((e) => { console.error('ÉCHEC :', e.message); process.exit(1); });
