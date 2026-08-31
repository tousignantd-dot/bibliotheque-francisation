/* L'interrupteur de secours du service worker.

   Un service worker est collant : une fois posé chez un élève, il y reste même
   si on supprime `sw.js` du dépôt — le navigateur garde la copie qu'il a et
   continue de servir depuis elle. Supprimer le fichier ne suffit donc pas ; il
   faut lui dire de partir.

   La marche à suivre, le jour où il faut le retirer :

     cp build/sw-desinstaller.js sw.js     # on REMPLACE, on ne supprime pas
     git add sw.js && git commit && git push

   Chaque navigateur qui revient récupère cette version, se désenregistre,
   vide ses boîtes et recharge ses onglets une fois. Après quelques semaines —
   le temps que tout le monde soit repassé —, on peut supprimer `sw.js` pour de
   bon, et retirer la greffe « installable:début / installable:fin » de
   `eleve.html` et `seance.html`. */

self.addEventListener('install', function () { self.skipWaiting(); });

self.addEventListener('activate', function (e) {
  e.waitUntil((async function () {
    const noms = await caches.keys();
    await Promise.all(noms.map(function (n) { return caches.delete(n); }));
    await self.registration.unregister();
    const onglets = await self.clients.matchAll({ type: 'window' });
    onglets.forEach(function (c) { c.navigate(c.url); });
  })());
});
