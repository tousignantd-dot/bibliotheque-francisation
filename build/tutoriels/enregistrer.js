/* Enregistre les capsules : un vrai film de l'écran, pas des captures fixes.

   Trois pièces.

   1. **`Page.startScreencast`** du protocole DevTools rend une image chaque
      fois que la page change, avec son horodatage. On les écrit sur le
      disque et on garde les horodatages : c'est eux, et non une cadence
      supposée, qui donneront la vraie durée de chaque image au montage.
      Un écran immobile n'émet aucune image — d'où le besoin des durées.

   2. **`scene.js`**, injecté dans la page : le pointeur, ses déplacements,
      le défilement doux et le surlignage en fondu. Animer depuis Node, un
      pas par appel, donnerait des saccades ; dans la page, c'est fluide.

   3. **Le plan dure au moins sa narration.** On mesure le MP3 avant de
      filmer et on tient l'écran jusqu'à ce que le temps soit couvert, plus
      une respiration. Sans ça, l'image changerait au milieu d'une phrase.

   `node enregistrer.js <port> [idCapsule]` */
const fs = require('fs');
const os = require('os');
const path = require('path');
const crypto = require('crypto');
const { execFileSync } = require('child_process');
const puppeteer = require('puppeteer-core');
const SCENE = require('./scene.js');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const PORT = process.argv[2];
/* Plusieurs capsules d'un coup, séparées par des virgules : les gestes de
   toutes se jouent de toute façon à chaque lancement, et tourner deux
   capsules en deux passes coûtait deux fois la promenade complète. */
const SEULE = process.argv[3] ? process.argv[3].split(',') : null;
const ICI = __dirname;
const SORTIE = path.join(ICI, 'films');
const VOIX = path.join(ICI, 'voix');
const manifeste = JSON.parse(fs.readFileSync(path.join(ICI, 'manifeste.json'), 'utf8'));

/* 1600 × 900 au facteur 2 : le film sort en 1080p, et le texte de 15 px du
   portail reste lisible après compression. */
const LARGEUR = 1600, HAUTEUR = 900, ECHELLE = 2;
const RESPIRATION = 0.7;      // secondes tenues après la fin de la phrase

const dodo = (ms) => new Promise((r) => setTimeout(r, ms));

function identifiants() {
  const bac = process.env.STORAGE_DIR
    || path.join(os.tmpdir(), 'francisation-demo-tutoriels');
  /* Le compte de tournage d'abord : c'est un enseignant ordinaire, ouvert par
     `peupler_demo.py`. Le compte de `identifiants-demo.json` est le fondateur
     de l'arbre, et le portail lui montre « Espace direction » — un bouton que
     le public des capsules n'a pas. On ne le filme plus. */
  for (const nom of ['identifiants-tournage.json', 'identifiants-demo.json']) {
    const fichier = path.join(bac, nom);
    if (fs.existsSync(fichier)) return JSON.parse(fs.readFileSync(fichier, 'utf8'));
  }
  const fichier = path.join(bac, 'identifiants-demo.json');
  if (process.env.PROF_CODE && process.env.PROF_MOTDEPASSE) {
    return { code: process.env.PROF_CODE, motDePasse: process.env.PROF_MOTDEPASSE };
  }
  throw new Error(`Identifiants introuvables (${fichier}). `
    + "Lancez d'abord ./build/tutoriels/lancer_demo.sh");
}

const dureeSon = (f) => parseFloat(execFileSync('ffprobe',
  ['-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', f],
  { encoding: 'utf8' }).trim());

/* — Le repérage : à quelle seconde la voix prononce tel bout de phrase —

   C'est ce qui met l'image d'accord avec la narration. Un geste porte
   `apres: "production orale"` : il se déclenche quand la voix arrive sur ces
   mots, pas quand le plan commence. `aligner.py` a relevé la position de
   chaque mot dans le MP3.

   Le pointeur doit *arriver* sur le mot, pas partir à ce moment-là : on
   avance donc le départ d'une demi-seconde par défaut. */
const AVANCE = 550;

function chercheRepere(mots, fragment) {
  const net = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim();
  const cible = net(fragment);
  if (!cible) return null;
  // On reconstruit la phrase mot à mot en gardant, pour chaque position de
  // caractère, le mot d'où elle vient : le fragment cherché peut couvrir
  // plusieurs mots, et c'est le début du premier qui nous intéresse.
  let phrase = '';
  const depuis = [];
  for (const m of mots) {
    const t = net(m.mot);
    if (!t) continue;
    if (phrase) { phrase += ' '; depuis.push(null); }
    for (let i = 0; i < t.length; i += 1) depuis.push(m.debut);
    phrase += t;
  }
  const i = phrase.indexOf(cible);
  if (i < 0) return null;
  for (let k = i; k < depuis.length; k += 1) if (depuis[k] != null) return depuis[k];
  return null;
}

/* Le même calcul qu'en Python, dans `controle.py` : JSON canonique — clés
   triées, aucune espace — puis SHA-1 tronqué. Les deux doivent rendre la même
   chaîne, sans quoi chaque capsule se dirait périmée. */
function canonique(v) {
  if (v === null || typeof v !== 'object') return JSON.stringify(v ?? null);
  if (Array.isArray(v)) return '[' + v.map(canonique).join(',') + ']';
  return '{' + Object.keys(v).sort()
    .map((k) => JSON.stringify(k) + ':' + canonique(v[k])).join(',') + '}';
}

function empreinte(capsule) {
  const canon = {
    id: capsule.id,
    titre: capsule.titre ?? null,
    prepare: capsule.prepare ?? null,
    plans: capsule.plans.map((p) => {
      const { papier, ...reste } = p;      // eslint-disable-line no-unused-vars
      return reste;
    }),
  };
  return crypto.createHash('sha1').update(canonique(canon), 'utf8')
    .digest('hex').slice(0, 12);
}

/* — Les gestes, joués *dans* la page pour qu'ils se voient — */
async function jouer(page, geste) {
  const scene = (corps, arg) => page.evaluate(corps, arg);
  switch (geste.do) {
    case 'attendre':
      await dodo(geste.ms);
      break;
    case 'defiler':
      await scene((s) => window.__scene.defiler(s), geste.sel);
      break;
    case 'pointer':
      await scene((s) => window.__scene.versElement(s), geste.sel);
      break;
    case 'parcourir':
      await scene((g) => window.__scene.parcourir(g.cibles, g.pause), geste);
      break;
    case 'taper':
      await scene((g) => window.__scene.taper(g.sel, g.texte, g.cadence), geste);
      break;
    case 'poser':
      await scene((g) => window.__scene.poser(g.sel, g.valeur), geste);
      break;
    case 'choisir':
      await scene((g) => window.__scene.choisir(g.sel, g.texte), geste);
      break;
    /* Une capsule peut sortir du portail : le compositeur est une page
       autonome. La scène vit dans le document, donc elle est perdue au
       changement de page et doit être réinjectée. */
    case 'naviguer':
      await page.goto(`http://localhost:${PORT}${geste.vers}`,
                      { waitUntil: 'networkidle2' });
      await dodo(600);
      await page.evaluate(SCENE);
      await dodo(200);
      break;
    case 'clic-index':
      await scene((g) => {
        const el = document.querySelectorAll(g.sel)[g.n];
        if (!el) throw new Error('cible absente : ' + g.sel + '[' + g.n + ']');
        el.id = el.id || ('cap-' + Math.random().toString(36).slice(2, 8));
        return window.__scene.clic('#' + el.id);
      }, geste);
      break;
    case 'survol':
      await scene((b) => window.__scene.survol(b), geste.bas || null);
      break;
    case 'clic':
      await scene((s) => window.__scene.clic(s), geste.sel);
      break;
    /* La barre d'onglets a disparu de l'espace enseignant : on y va
       maintenant par les boutons de la carte du groupe, qui portent le même
       `data-ecran`. Le sélecteur ne nomme donc plus de classe — plusieurs
       éléments répondent (« Planifier » sous le groupe et « Planifier ce
       groupe » plus bas), et `visible()` prend celui qui est à l'écran. */
    /* — Déplier une liste déroulante —

       Le menu d'un <select> est dessiné par le système, **hors de la page** :
       il n'apparaît sur aucune capture et sur aucune image du film. Une voix
       qui dit « choisissez le niveau » devant une liste fermée ne montre donc
       rien. On donne au select une hauteur (`size`), ce qui le déploie DANS la
       page — les vraies options, à leur vraie place, et cette fois filmables. */
    case 'deplier-liste':
      await scene(async (s) => {
        const el = window.__scene.visible(s);
        if (!el) throw new Error('liste absente : ' + s);
        await window.__scene.defiler(el);
        el.dataset.tailleAvant = el.size;
        el.size = Math.min(el.options.length, 9);
      }, geste.sel);
      await dodo(geste.tenir ?? 900);
      break;
    case 'replier-liste':
      await scene((s) => {
        const el = window.__scene.visible(s);
        if (el) el.size = Number(el.dataset.tailleAvant || 0);
      }, geste.sel);
      break;
    case 'onglet':
      await scene((v) => window.__scene.clic(`[data-ecran="${v}"]`), geste.valeur);
      break;
    /* Cocher se voit case par case : trois cases qui s'allument d'un coup
       ne raconteraient pas le geste dont parle la voix. */
    case 'cocher':
      await scene(async (n) => {
        const cases = Array.from(document.querySelectorAll('[data-coche]')).slice(0, n);
        for (const c of cases) {
          if (!c.checked) await window.__scene.clic(`[data-coche="${c.dataset.coche}"]`);
          await window.__scene.dodo(220);
        }
      }, geste.n);
      break;
    case 'js':
      await page.evaluate(geste.code);
      await dodo(250);
      break;
    /* Un seul module, ouvert une seule fois.

       La version d'avant cherchait le bon module **à l'écran** : elle cliquait
       chaque chevron, regardait s'il avait déplié des sections, et le repliait
       sinon. Douze dossiers s'ouvraient et se refermaient à toute vitesse
       pendant que la voix expliquait le geste — signalé au visionnement, le
       2 septembre 2026. La rangée se reconnaît pourtant sans rien ouvrir : son
       résumé annonce le nombre de sections. On la trouve, on y va, on ouvre. */
    case 'deplier-module':
      await scene(() => document.querySelector('.choice[data-filtre="cours"]')?.click());
      await dodo(700);
      await scene(async () => {
        const rangee = Array.from(document.querySelectorAll('.pe-rangee'))
          .find((r) => /\d+\s+sections/.test(r.textContent));
        const chevron = rangee && rangee.querySelector('.pe-chevron[data-deploi]');
        if (!chevron) throw new Error('aucun module à sections dans la liste');
        await window.__scene.defiler(rangee);
        await window.__scene.dodo(400);
        await window.__scene.clic(`.pe-chevron[data-deploi="${chevron.dataset.deploi}"]`);
      });
      await dodo(800);
      await scene(() => window.__scene.defiler('.pe-sections'));
      break;
    case 'ouvrir-module':
    case 'ouvrir-seance': {
      const present = (code) => page.evaluate((c) => (c
        ? Array.from(document.querySelectorAll('.mat-seance-code'))
            .some((n) => n.textContent.trim() === c)
        : document.querySelectorAll('.mat-seance').length > 0), code || null);
      let trouve = await present(geste.code);
      const ids = await page.$$eval('#matColonne [data-action="deplier"]',
        (n) => n.map((b) => b.dataset.id));
      for (const id of (trouve ? [] : ids)) {
        await scene((i) => window.__scene.clic(
          `#matColonne [data-action="deplier"][data-id="${i}"]`), id);
        await dodo(600);
        trouve = await present(geste.code);
        if (trouve) break;
      }
      if (!trouve) throw new Error(`séance ${geste.code || '(toutes)'} introuvable`);
      if (geste.do === 'ouvrir-seance') {
        await scene(async (code) => {
          const cell = Array.from(document.querySelectorAll('.mat-seance-code'))
            .find((n) => n.textContent.trim() === code);
          const rangee = cell.closest('.mat-seance');
          await window.__scene.defiler(rangee);
          const titre = rangee.querySelector('.mat-seance-titre');
          const r = titre.getBoundingClientRect();
          await window.__scene.versPoint(r.left + 40, r.top + r.height / 2);
          titre.click();
        }, geste.code);
        await dodo(700);
      }
      break;
    }
    default:
      throw new Error('geste inconnu : ' + geste.do);
  }
}

/* — Ouvrir le portail, session faite et scène injectée —

   Sortie de la boucle principale pour que le générateur du guide
   (`guide_captures.js`) rejoue exactement la même mise en place : un guide
   qui montrerait un autre écran que le tournage ne servirait à rien. */
async function ouvrirSession(page, port) {
  const compte = identifiants();
  await page.goto(`http://localhost:${port}/enseignant.html`, { waitUntil: 'networkidle2' });
  await page.evaluate((c) => {
    const poser = (el, v) => {
      const set = Object.getOwnPropertyDescriptor(HTMLInputElement.prototype, 'value').set;
      set.call(el, v);
      el.dispatchEvent(new Event('input', { bubbles: true }));
    };
    // Le compte s'ouvre par un CODE depuis le 28 août 2026 : le champ
    // « courriel » n'existe plus, et `poser()` mourait sur un null.
    poser(document.getElementById('code'), c.code);
    poser(document.getElementById('motDePasse'), c.motDePasse);
    document.getElementById('formConnexion').requestSubmit();
  }, compte);
  await page.waitForSelector('#portail:not([hidden])', { timeout: 15000 });
  await dodo(1200);
  /* Le portail est une page unique : aucune navigation ne recharge le
     document, donc la scène s'injecte une seule fois. */
  await page.evaluate(SCENE);
  console.log('session ouverte, scène injectée');
}

async function main() {
  fs.mkdirSync(SORTIE, { recursive: true });
  const navigateur = await puppeteer.launch({
    executablePath: CHROME,
    headless: 'new',
    args: ['--force-device-scale-factor=1', '--hide-scrollbars',
           '--disable-features=CalculateNativeWinOcclusion'],
  });
  const page = await navigateur.newPage();
  await page.setViewport({ width: LARGEUR, height: HAUTEUR, deviceScaleFactor: ECHELLE });
  await ouvrirSession(page, PORT);

  const cdp = await page.createCDPSession();

  for (const capsule of manifeste.capsules) {
    const garder = !SEULE || SEULE.includes(capsule.id);
    const dossier = path.join(SORTIE, capsule.id);
    if (garder) {
      fs.rmSync(dossier, { recursive: true, force: true });
      fs.mkdirSync(dossier, { recursive: true });
    }

    const images = [];
    let numero = 0;
    const surImage = (trame) => {
      if (garder) {
        const nom = String(numero++).padStart(5, '0') + '.jpg';
        fs.writeFileSync(path.join(dossier, nom), Buffer.from(trame.data, 'base64'));
        images.push({ nom, t: trame.metadata.timestamp });
      }
      cdp.send('Page.screencastFrameAck', { sessionId: trame.sessionId }).catch(() => {});
    };

    /* La mise en place, **avant** que la caméra tourne.

       Une capsule hérite de l'écran que la précédente a laissé : la capsule 3
       s'ouvrait sur l'aperçu élève resté déplié par la capsule 2, visible une
       bonne seconde avant d'être refermé. Ces gestes-là ne racontent rien —
       ils rangent. Ils se jouent donc hors champ. */
    /* Toute fenêtre laissée ouverte par la capsule précédente se referme
       ici, avant la caméra. La règle vaut mieux qu'un `prepare` par capsule :
       elle a été écrite trois fois pour trois modales, et il a suffi de
       changer l'ordre des capsules pour qu'une quatrième passe entre les
       mailles. */
    await page.evaluate(() => document.querySelectorAll('[data-fermer]')
      .forEach((b) => { if (b.offsetParent !== null) b.click(); }));
    for (const geste of (capsule.prepare || [])) {
      await jouer(page, geste);
    }
    await dodo(400);

    if (garder) {
      cdp.on('Page.screencastFrame', surImage);
      await cdp.send('Page.startScreencast', {
        format: 'jpeg', quality: 92, everyNthFrame: 1,
        maxWidth: LARGEUR * ECHELLE, maxHeight: HAUTEUR * ECHELLE,
      });
      await dodo(300);
    }

    const reperes = [];
    for (const plan of capsule.plans) {
      const base = `${capsule.id}_${plan.id}`;
      const son = path.join(VOIX, `${base}.mp3`);
      if (!fs.existsSync(son)) throw new Error(`narration absente : ${base}.mp3`);
      const fichierMots = path.join(VOIX, `${base}.json`);
      const mots = fs.existsSync(fichierMots)
        ? JSON.parse(fs.readFileSync(fichierMots, 'utf8')).mots : [];

      const debut = Date.now();     // la voix commence ici
      await page.evaluate(() => window.__scene?.effacer());

      for (const geste of (plan.gestes || [])) {
        if (geste.apres) {
          const t = chercheRepere(mots, geste.apres);
          if (t == null) {
            throw new Error(`${base} : « ${geste.apres} » ne se trouve pas dans la `
              + 'narration — un repère doit citer les mots dits.');
          }
          const vise = t * 1000 - (geste.avance ?? AVANCE);
          const attente = vise - (Date.now() - debut);
          if (attente > 0) {
            await dodo(attente);
          } else if (attente < -600 && garder) {
            /* Le geste précédent a mordu sur ce repère. On le signale : c'est
               réparable en raccourcissant un geste ou en déplaçant le repère,
               et invisible autrement jusqu'au visionnement. */
            console.log(`    ⚠ ${base} : « ${geste.apres} » manqué de `
              + `${(-attente / 1000).toFixed(1)} s`);
          }
        }
        await jouer(page, geste);
      }
      if (!garder) continue;

      if (plan.surligne) {
        if (plan.surligneApres) {
          const t = chercheRepere(mots, plan.surligneApres);
          const attente = (t ?? 0) * 1000 - (Date.now() - debut);
          if (attente > 0) await dodo(attente);
        }
        await page.evaluate((s) => window.__scene.surligner(s), plan.surligne);
        await dodo(450);
      }
      /* Le plan tient jusqu'à couvrir sa narration : l'image ne doit jamais
         changer au milieu d'une phrase. */
      const voulu = (dureeSon(son) + RESPIRATION) * 1000;
      const reste = voulu - (Date.now() - debut);
      if (reste > 0) await dodo(reste);
      reperes.push({ plan: plan.id, debut, fin: Date.now() });
      console.log(`  ${base}  ${((Date.now() - debut) / 1000).toFixed(1)} s`);
    }

    if (garder) {
      await dodo(400);
      await cdp.send('Page.stopScreencast');
      cdp.off('Page.screencastFrame', surImage);
      /* L'empreinte de ce qui vient d'être filmé — tout le manifeste de la
         capsule sauf `papier`, qui ne décrit que le cadrage des copies
         d'écran du guide. C'est elle que `controle.py` compare, plutôt que
         des dates de fichier : retoucher un cadrage papier n'envoie plus
         quatre capsules au retournage. */
      fs.writeFileSync(path.join(dossier, 'images.json'),
        JSON.stringify({ empreinte: empreinte(capsule), images, reperes }, null, 1));
      console.log(`✓ ${capsule.id} — ${images.length} images`);
    }
  }

  await navigateur.close();
}

module.exports = { jouer, ouvrirSession, chercheRepere, dodo,
                   LARGEUR, HAUTEUR, ECHELLE, CHROME, VOIX, ICI };

/* Lancé directement, il tourne ; requis comme module, il ne fait rien —
   `guide_captures.js` n'a besoin que de ses gestes. */
if (require.main === module) {
  main().catch((e) => { console.error('ÉCHEC :', e.message); process.exit(1); });
}
