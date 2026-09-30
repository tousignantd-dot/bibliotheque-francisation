"""La vente du jeu de rôle d'une trousse de métier — le même geste que Compostelle.

Daniel, 28 sept. 2026 : « vendre les produits de la même façon que pour
Compostelle ». Tout reste gratuit, sauf le jeu de rôle (le magasin de la Maison
Francœur, le comptoir de l'Hôtel Rive-Claire), qui s'ouvre par un code acheté
chez Stripe. Le serveur (pelerins.PRODUITS) fixe le prix et le retour ; cette
page n'écrit aucun montant, elle relit /api/pelerins/offre.

    import vente_trousse
    css, js = vente_trousse.bloc("hotel", "hotel-code", "btn btn--pri")

Le JS attend de la page deux fonctions :
  venteLangue()        → 'fr' | 'en' | 'es' (la langue de l'interface ; sinon fr)
  venteSuite(code)     → quoi faire une fois le code acquis (ouvrir le jeu)
et il expose :
  venteOffre(el)       → écrit l'offre dans el (rien si la vente est fermée)
  venteRetour()        → true si l'adresse est un retour de Stripe (et le traite)
"""
import json

TXT = {
    "fr": {
        "pas_de_code": "Pas encore de code ?",
        "lancement": "Prix de lancement : {prix} au lieu de {regulier}, pour un temps limité{fin}.",
        "jusqu": " — jusqu'au {date} inclusivement",
        "quoi": "<b>{n} conversations</b> avec les clients, pendant <b>{mois} mois</b> : ils vous répondent vraiment, "
                "à voix haute, puis un bilan geste par geste.",
        "gratuit": "Les mots, les exercices, le test et la fiche restent gratuits. Paiement par carte chez Stripe ; "
                   "nous ne recevons ni votre nom ni votre carte. Le code s'affiche ici tout de suite, et il est aussi écrit sur votre reçu.",
        "legal": "Vendu par Boucledidactique. Carte de crédit seulement. Remboursable dans les 14 jours si 3 conversations au plus ont servi. "
                 "Réservé aux personnes majeures (ou avec l'accord d'un parent). Aucune taxe.",
        "conditions": "Conditions de vente",
        "equipe_tit": "Pour une équipe ?",
        "equipe_txt": "Un code par employé, et un code de suivi pour vous : il montre si chaque code a servi et combien de fois — jamais ce qui a été dit.",
        "combien": "Nombre de codes",
        "obtenir_n": "Obtenir {n} codes — {prix}",
        "lot_restant": "{n} conversations par code, jusqu'au {date}.",
        "lot_tit": "Vos codes",
        "lot_suivi": "Votre code de suivi",
        "lot_garder": "Donnez un code par personne. Le code de suivi est pour vous seul. Dites à vos employés que vous verrez si leur code a servi, et combien de fois — jamais ce qu'ils ont dit.",
        "lot_copier": "Copier la liste",
        "lot_copie": "Copié ✓",
        "lot_ouvrir": "Ouvrir le suivi",
        "obtenir": "Obtenir mon code — {prix}",
        "vers": "Vers le paiement…",
        "reessayer": "Réessayer",
        "erreur": "Le paiement ne s'ouvre pas. Réessayez dans un moment.",
        "reseau": "Pas de réseau : le paiement demande une connexion.",
        "merci": "Merci !",
        "acces": "Votre accès",
        "verif": "Nous vérifions le paiement auprès de Stripe…",
        "code": "Votre code d'accès",
        "garder": "Il est gardé dans ce navigateur. Notez-le : il vous servira sur un autre appareil, et il est aussi sur votre reçu.",
        "restant": "{n} conversations, jusqu'au {date}.",
        "commencer": "Commencer",
        "pas_confirme": "Le paiement n'est pas encore confirmé. Si vous avez payé, votre code est écrit sur le reçu reçu par courriel : entrez-le à l'écran du jeu.",
        "annule": "Paiement annulé : rien n'a été facturé.",
        "retour": "Retour",
    },
    "en": {
        "pas_de_code": "No code yet?",
        "lancement": "Launch price: {prix} instead of {regulier}, for a limited time{fin}.",
        "jusqu": " — until {date} inclusive",
        "quoi": "<b>{n} conversations</b> with guests, for <b>{mois} months</b>: they really answer you, "
                "out loud, then a step-by-step review.",
        "gratuit": "The words, the exercises, the test and the pocket card stay free. Card payment with Stripe; "
                   "we never see your name or your card. The code shows up here right away, and it is also on your receipt.",
        "legal": "Sold by Boucledidactique. Credit card only. Refundable within 14 days if 3 conversations or fewer were used. "
                 "Adults only (or with a parent's consent). No tax.",
        "conditions": "Terms of sale (in French)",
        "equipe_tit": "For a team?",
        "equipe_txt": "One code per employee, and a tracking code for you: it shows whether each code was used and how often — never what was said.",
        "combien": "Number of codes",
        "obtenir_n": "Get {n} codes — {prix}",
        "lot_restant": "{n} conversations per code, until {date}.",
        "lot_tit": "Your codes",
        "lot_suivi": "Your tracking code",
        "lot_garder": "Give one code per person. The tracking code is for you only. Tell your employees you will see whether their code was used, and how often — never what they said.",
        "lot_copier": "Copy the list",
        "lot_copie": "Copied ✓",
        "lot_ouvrir": "Open tracking",
        "obtenir": "Get my code — {prix}",
        "vers": "Opening payment…",
        "reessayer": "Try again",
        "erreur": "The payment page won't open. Try again in a moment.",
        "reseau": "No network: payment needs a connection.",
        "merci": "Thank you!",
        "acces": "Your access",
        "verif": "Checking the payment with Stripe…",
        "code": "Your access code",
        "garder": "It is saved in this browser. Write it down: you'll need it on another device, and it is also on your receipt.",
        "restant": "{n} conversations, until {date}.",
        "commencer": "Start",
        "pas_confirme": "The payment is not confirmed yet. If you paid, your code is on the receipt sent by email: enter it on the role-play screen.",
        "annule": "Payment cancelled: nothing was charged.",
        "retour": "Back",
    },
    "es": {
        "pas_de_code": "¿Todavía no tiene código?",
        "lancement": "Precio de lanzamiento: {prix} en lugar de {regulier}, por tiempo limitado{fin}.",
        "jusqu": " — hasta el {date} inclusive",
        "quoi": "<b>{n} conversaciones</b> con los clientes, durante <b>{mois} meses</b>: le responden de verdad, "
                "en voz alta, y luego un balance paso a paso.",
        "gratuit": "Las palabras, los ejercicios, la prueba y la ficha siguen gratis. Pago con tarjeta en Stripe; "
                   "no recibimos ni su nombre ni su tarjeta. El código aparece aquí enseguida, y también está en su recibo.",
        "legal": "Vendido por Boucledidactique. Solo tarjeta de crédito. Reembolsable en 14 días si se usaron 3 conversaciones o menos. "
                 "Solo para mayores de edad (o con el permiso de un padre o madre). Sin impuestos.",
        "conditions": "Condiciones de venta (en francés)",
        "equipe_tit": "¿Para un equipo?",
        "equipe_txt": "Un código por empleado, y un código de seguimiento para usted: muestra si cada código se usó y cuántas veces — nunca lo que se dijo.",
        "combien": "Número de códigos",
        "obtenir_n": "Obtener {n} códigos — {prix}",
        "lot_restant": "{n} conversaciones por código, hasta el {date}.",
        "lot_tit": "Sus códigos",
        "lot_suivi": "Su código de seguimiento",
        "lot_garder": "Dé un código por persona. El código de seguimiento es solo para usted. Diga a sus empleados que verá si su código se usó, y cuántas veces — nunca lo que dijeron.",
        "lot_copier": "Copiar la lista",
        "lot_copie": "Copiado ✓",
        "lot_ouvrir": "Abrir el seguimiento",
        "obtenir": "Obtener mi código — {prix}",
        "vers": "Abriendo el pago…",
        "reessayer": "Reintentar",
        "erreur": "El pago no se abre. Vuelva a intentarlo en un momento.",
        "reseau": "Sin red: el pago necesita conexión.",
        "merci": "¡Gracias!",
        "acces": "Su acceso",
        "verif": "Verificamos el pago con Stripe…",
        "code": "Su código de acceso",
        "garder": "Queda guardado en este navegador. Anótelo: le servirá en otro aparato, y también está en su recibo.",
        "restant": "{n} conversaciones, hasta el {date}.",
        "commencer": "Empezar",
        "pas_confirme": "El pago todavía no está confirmado. Si pagó, su código está en el recibo enviado por correo: escríbalo en la pantalla del juego.",
        "annule": "Pago cancelado: no se cobró nada.",
        "retour": "Volver",
    },
}

CSS = """
.vente{margin-top:16px;border:1px solid var(--vente-filet,#d8dde5);border-radius:12px;background:var(--vente-fond,#fff)}
.vente summary{cursor:pointer;padding:12px 14px;font-weight:800;display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap}
.vente summary s{font-weight:600;opacity:.65;margin-right:4px}
.vente .corps{padding:0 14px 14px;font-size:15.5px;line-height:1.45}
.vente .corps p{margin:0 0 8px}
.vente .petit{font-size:14px;opacity:.8}
.vente .lancement{display:inline-block;background:#FBEFC4;color:#5C4400;border:1px solid #E7C75A;border-radius:10px;padding:4px 10px;font-size:14px;font-weight:700}
.vente button{width:100%}
.vente-equipe{margin-top:14px;padding-top:12px;border-top:1px dashed var(--vente-filet,#d8dde5)}
.vente-equipe label{display:flex;align-items:center;gap:8px;margin:6px 0 10px;font-weight:700}
.vente-equipe input{font:inherit;width:90px;padding:6px 8px;border:1px solid var(--vente-filet,#c9d0da);border-radius:8px}
.vente-liste{font:700 17px/1.6 ui-monospace,Menlo,monospace;letter-spacing:.08em;background:#f6f7f9;border-radius:10px;padding:10px 14px;white-space:pre-wrap}
.vente-code{font:800 30px/1.2 ui-monospace,Menlo,monospace;letter-spacing:.12em;padding:14px;border:2px dashed currentColor;border-radius:12px;text-align:center;margin:10px 0}
"""


def bloc(produit, cle_code, bouton="btn btn--pri"):
    js = """
/* La vente du jeu de rôle (build/vente_trousse.py, 28 sept. 2026) : même geste que Compostelle. */
const VENTE = {produit: %s, cle: %s, btn: %s, txt: %s};
const vt = (k, v) => { const t = (VENTE.txt[venteLangue()] || VENTE.txt.fr)[k] || VENTE.txt.fr[k];
  return v ? t.replace(/\\{(\\w+)\\}/g, (_, x) => v[x] != null ? v[x] : '') : t; };
const venteEsc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
function venteDollars(c){ const l = venteLangue(); const n = (c / 100).toFixed(2);
  return l === 'en' ? '$' + n : n.replace('.', ',') + ' $'; }
function venteDate(iso){ try { return new Date(iso + 'T12:00:00').toLocaleDateString(venteLangue() === 'fr' ? 'fr-CA' : venteLangue(), {day:'numeric', month:'long', year:'numeric'}); } catch(e) { return iso; } }
let venteO = null;
async function venteOffre(el){
  if (!el) return;
  if (!venteO) { try { const r = await fetch('/api/pelerins/offre'); if (r.ok) venteO = await r.json(); } catch(e) {} }
  const o = venteO; if (!o || !o.ouverte || !document.body.contains(el)) return;
  const promo = o.promo && o.prixRegulier > o.prix;
  const prix = promo ? `<s>${venteDollars(o.prixRegulier)}</s> ${venteDollars(o.prix)}` : venteDollars(o.prix);
  el.innerHTML = `<details class="vente"><summary><span>${venteEsc(vt('pas_de_code'))}</span><span>${prix}</span></summary><div class="corps">
    ${promo ? `<p class="lancement">${venteEsc(vt('lancement', {prix: venteDollars(o.prix), regulier: venteDollars(o.prixRegulier),
        fin: o.promoFin ? vt('jusqu', {date: venteDate(o.promoFin)}) : ''}))}</p>` : ''}
    <p>${vt('quoi', {n: o.conversations, mois: Math.round(o.jours / 30.4)})}</p>
    <p class="petit">${venteEsc(vt('gratuit'))}</p>
    <p class="petit">${venteEsc(vt('legal'))} <a href="/conditions-de-vente.html" target="_blank" rel="noopener">${venteEsc(vt('conditions'))}</a></p>
    <button type="button" class="${VENTE.btn} vente-go">${venteEsc(vt('obtenir', {prix: venteDollars(o.prix)}))}</button>
    <div class="vente-equipe"><p><b>${venteEsc(vt('equipe_tit'))}</b> ${venteEsc(vt('equipe_txt'))}</p>
     <label>${venteEsc(vt('combien'))} <input type="number" class="vente-n" min="${o.lotMin || 2}" max="${o.lotMax || 50}" value="${o.lotMin || 2}" inputmode="numeric"></label>
     <button type="button" class="${VENTE.btn} vente-lot"></button></div></div></details>`;
  el.querySelector('.vente-go').onclick = venteAcheter;
  const n = el.querySelector('.vente-n'), lot = el.querySelector('.vente-lot');
  const borne = () => Math.max(o.lotMin || 2, Math.min(o.lotMax || 50, parseInt(n.value, 10) || 0));
  const libelle = () => { lot.textContent = vt('obtenir_n', {n: borne(), prix: venteDollars(o.prix * borne())}); };
  n.oninput = libelle; n.onchange = () => { n.value = borne(); libelle(); }; libelle();
  lot.onclick = ev => { n.value = borne(); venteAcheter(ev, borne()); };
}
async function venteAcheter(ev, quantite){
  const b = ev && ev.currentTarget; if (b) { b.disabled = true; b.textContent = vt('vers'); }
  try {
    const r = await fetch('/api/pelerins/achat', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({produit: VENTE.produit, quantite: quantite || 1})});
    const d = await r.json().catch(() => ({}));
    if (r.ok && d.url) { location.href = d.url; return; }
    alert(d.error || vt('erreur'));
  } catch(e) { alert(vt('reseau')); }
  if (b) { b.disabled = false; b.textContent = vt('reessayer'); }
}
function venteRetour(){
  const h = location.hash;
  if (h === '#achat-annule') { history.replaceState(null, '', location.pathname + location.search); setTimeout(() => alert(vt('annule')), 300); return false; }
  if (!h.startsWith('#achat/')) return false;
  const sid = decodeURIComponent(h.slice(7)), app = document.getElementById('app');
  app.innerHTML = `<div style="padding:24px 0"><p style="font-weight:800;text-transform:uppercase;letter-spacing:.1em;font-size:13px;margin:0">${venteEsc(vt('merci'))}</p>
    <h1>${venteEsc(vt('acces'))}</h1><p id="venteAtt">${venteEsc(vt('verif'))}</p><div id="venteZ"></div></div>`;
  (async () => {
    let d = null;
    for (let i = 0; i < 6 && !d; i++) {
      try { const r = await fetch('/api/pelerins/session?id=' + encodeURIComponent(sid)); const j = await r.json().catch(() => ({}));
        if (r.ok) d = j; else if (r.status === 409) await new Promise(ok => setTimeout(ok, 2000)); else break;
      } catch(e) { await new Promise(ok => setTimeout(ok, 2000)); }
    }
    document.getElementById('venteAtt').remove();
    const z = document.getElementById('venteZ');
    const fin = () => { history.replaceState(null, '', location.pathname + location.search); venteSuite(d && d.code); };
    if (!d || !d.code) { z.innerHTML = `<p>${venteEsc(vt('pas_confirme'))}</p><button type="button" class="${VENTE.btn}" id="venteOk">${venteEsc(vt('retour'))}</button>`; }
    else if (d.suivi) {
      // Un lot : l'acheteur n'est pas celui qui joue — aucun code n'est gardé ici.
      const liste = d.codes.join('\\n');
      z.innerHTML = `<p><b>${venteEsc(vt('lot_tit'))}</b> (${d.codes.length})</p><pre class="vente-liste">${venteEsc(liste)}</pre>
        <button type="button" class="${VENTE.btn}" id="venteCopier">${venteEsc(vt('lot_copier'))}</button>
        <p style="margin-top:16px"><b>${venteEsc(vt('lot_suivi'))}</b></p><div class="vente-code">${venteEsc(d.suivi)}</div>
        <p>${venteEsc(vt('lot_restant', {n: d.restant, date: venteDate(d.expire)}))}</p><p>${venteEsc(vt('lot_garder'))}</p>
        <a class="${VENTE.btn}" href="/suivi-codes.html?c=${encodeURIComponent(d.suivi)}">${venteEsc(vt('lot_ouvrir'))}</a>`;
      document.getElementById('venteCopier').onclick = e => navigator.clipboard.writeText(liste + '\\n\\n' + vt('lot_suivi') + ' : ' + d.suivi)
        .then(() => { e.target.textContent = vt('lot_copie'); });
      history.replaceState(null, '', location.pathname + location.search);
      return;
    }
    else {
      try { localStorage.setItem(VENTE.cle, d.code); } catch(e) {}
      z.innerHTML = `<p><b>${venteEsc(vt('code'))}</b></p><div class="vente-code">${venteEsc(d.code)}</div>
        <p>${venteEsc(vt('restant', {n: d.restant, date: venteDate(d.expire)}))}</p><p>${venteEsc(vt('garder'))}</p>
        <button type="button" class="${VENTE.btn}" id="venteOk">${venteEsc(vt('commencer'))}</button>`;
    }
    document.getElementById('venteOk').onclick = fin;
  })();
  return true;
}
""" % (json.dumps(produit), json.dumps(cle_code), json.dumps(bouton), json.dumps(TXT, ensure_ascii=False))
    return CSS, js
