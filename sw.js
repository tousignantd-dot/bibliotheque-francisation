/* Le service worker de francis — ce qui rend le site installable et utilisable
   hors ligne.

   La question n'est pas « comment garder des fichiers » : c'est « comment ne
   jamais servir du périmé ». Le site se déploie plusieurs fois par jour, et un
   élève qui verrait l'exercice d'avant la correction serait un dégât plus grand
   que l'absence de hors-ligne. D'où une stratégie par nature de fichier, et
   jamais une règle unique :

     /api/**            réseau seul, jamais de cache. Ce sont des réponses
                        propres à un élève connecté ; les garder serait montrer
                        le travail de quelqu'un d'autre sur un poste partagé.
     pages (.html)      réseau d'abord, cache en secours. Hors ligne, on rend la
                        dernière version vue ; à défaut, la page d'attente.
     .css / .js         réseau d'abord. Ils changent à chaque déploiement, et un
                        script périmé appellerait d'anciennes routes.
     .mp3               cache d'abord. Les adresses portent `?v=AUDIO_V` : une
                        régénération change l'adresse, donc le cache ne peut pas
                        mentir. Et ce sont les fichiers les plus lourds.
     images, polices    cache d'abord, mais on redemande en arrière-plan et on
                        remplace. Une image refaite sous le même nom serait
                        autrement figée pour toujours chez l'élève qui l'a vue.

   Deux gardes qui ne se voient pas :
   - les requêtes `Range` (ce que fait <audio> pour se déplacer dans un son)
     partent au réseau sans passer par le cache ; une réponse 206 mise en cache
     casse la lecture ;
   - on ne garde que les réponses `ok` et de type `basic` (même origine), jamais
     une réponse opaque ni une erreur — sinon on met en cache un 404.

   Retrait : supprimer ce fichier, puis la greffe repérée par les marqueurs
   « installable:début » / « installable:fin » dans eleve.html et seance.html.
   Un service worker déjà posé chez un élève ne disparaît qu'au `unregister` —
   voir `build/sw-desinstaller.js` si ce jour vient. */

const VERSION = 'francis-1';
const PAGES  = 'pages-' + VERSION;
const MEDIAS = 'medias-' + VERSION;
const ATTENTE = '/hors-ligne.html';

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(PAGES).then(function (c) { return c.add(ATTENTE); }));
});

self.addEventListener('activate', function (e) {
  // On ne réclame pas `skipWaiting` : une version neuve prend la main au
  // prochain démarrage, pas au milieu d'un exercice commencé.
  e.waitUntil(
    caches.keys().then(function (noms) {
      return Promise.all(noms.map(function (n) {
        if (n !== PAGES && n !== MEDIAS) { return caches.delete(n); }
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

function gardable(r) {
  return r && r.ok && r.type === 'basic' && r.status === 200;
}

function reseauDabord(e, boite) {
  return fetch(e.request).then(function (r) {
    if (gardable(r)) {
      const copie = r.clone();
      caches.open(boite).then(function (c) { c.put(e.request, copie); });
    }
    return r;
  }).catch(function () {
    return caches.match(e.request).then(function (c) {
      if (c) { return c; }
      if (e.request.mode === 'navigate') { return caches.match(ATTENTE); }
      throw new Error('hors ligne');
    });
  });
}

function cacheDabord(e, boite, revalider) {
  return caches.match(e.request).then(function (c) {
    const reseau = fetch(e.request).then(function (r) {
      if (gardable(r)) {
        const copie = r.clone();
        caches.open(boite).then(function (b) { b.put(e.request, copie); });
      }
      return r;
    }).catch(function () { return c; });
    if (!c) { return reseau; }
    if (revalider) { reseau; }            // remplacé pour la prochaine fois
    return c;
  });
}

self.addEventListener('fetch', function (e) {
  const req = e.request;
  if (req.method !== 'GET') { return; }
  if (req.headers.has('range')) { return; }        // <audio> qui se déplace

  let u;
  try { u = new URL(req.url); } catch (err) { return; }
  if (u.origin !== self.location.origin) { return; }
  if (u.pathname.startsWith('/api/')) { return; }  // jamais de cache
  if (u.pathname === '/sw.js') { return; }

  const p = u.pathname;
  if (req.mode === 'navigate' || p.endsWith('.html') || p.endsWith('/')) {
    e.respondWith(reseauDabord(e, PAGES));
  } else if (p.endsWith('.css') || p.endsWith('.js') || p.endsWith('.json')) {
    e.respondWith(reseauDabord(e, PAGES));
  } else if (p.endsWith('.mp3')) {
    e.respondWith(cacheDabord(e, MEDIAS, false));
  } else if (/\.(png|jpe?g|svg|webp|gif|woff2?)$/.test(p)) {
    e.respondWith(cacheDabord(e, MEDIAS, true));
  }
});
