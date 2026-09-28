#!/usr/bin/env python3
"""La page de suivi d'un lot de codes — ce que voit l'employeur qui a acheté pour ses employés.

    python3 build/suivi_codes.py   # → suivi-codes.html (racine, publique, noindex)

Daniel, 28 sept. 2026 : un employeur qui achète plusieurs codes « veut savoir
simplement si l'employé l'a utilisé ou pas ». Le code de suivi (SV…) vient avec
le lot, sur l'écran de retour et sur le reçu de Stripe ; la page le lit par
/api/pelerins/suivi et montre, code par code : pas encore utilisé, ou combien de
conversations et la date de la dernière. Jamais le contenu (il n'est pas gardé),
jamais une personne : qui a reçu quel code, l'employeur l'écrit lui-même, et
c'est gardé dans SON navigateur seulement.

Loi 25 : suivre l'usage d'un employé est un renseignement sur lui. La page le
dit à l'employeur et lui donne la phrase à dire à ses employés.
"""
import json, pathlib

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "suivi-codes.html"

PRODUITS = {"compostelle": "En route vers Compostelle", "francoeur": "Maison Francœur", "hotel": "Hôtel Rive-Claire"}

TXT = {
    "fr": {
        "titre": "Le suivi de vos codes", "intro": "Entrez le code de suivi reçu avec votre achat (il commence par SV). Il est aussi sur votre reçu.",
        "code": "Code de suivi", "voir": "Voir", "inconnu": "Ce code de suivi n'existe pas. Vérifiez-le sur votre reçu.",
        "reseau": "Pas de réseau. Réessayez dans un moment.",
        "resume": "{n} code{s} sur {t} {ont} servi.", "resume0": "Aucun des {t} codes n'a encore servi.", "col_code": "Code", "col_qui": "Donné à", "col_usage": "Usage", "col_fin": "Valide jusqu'au",
        "qui_ph": "un prénom (gardé ici seulement)", "jamais": "Pas encore utilisé", "usage": "{u} conversation{s} sur {c}",
        "dernier": "dernière le {d}", "rembourse": "Remboursé", "reserve": "Paiement non confirmé", "expire": "Expiré",
        "copier": "Copier le tableau", "copie": "Copié ✓", "maj": "Actualiser",
        "voit_tit": "Ce que vous voyez, et ce que vous ne voyez pas",
        "voit": "Vous voyez si chaque code a servi, combien de conversations, et la date de la dernière. Vous ne voyez jamais ce qui a "
                "été dit : les conversations ne sont pas gardées. Les prénoms que vous écrivez ici restent dans ce navigateur ; "
                "nous ne les recevons pas.",
        "dire_tit": "À dire à vos employés",
        "dire": "« Je verrai si ton code a servi, et combien de fois — jamais ce que tu as dit. »",
    },
    "en": {
        "titre": "Tracking your codes", "intro": "Enter the tracking code you received with your purchase (it starts with SV). It is also on your receipt.",
        "code": "Tracking code", "voir": "Show", "inconnu": "This tracking code does not exist. Check it on your receipt.",
        "reseau": "No network. Try again in a moment.",
        "resume": "{n} of {t} code{st} used.", "resume0": "None of the {t} codes used yet.", "col_code": "Code", "col_qui": "Given to", "col_usage": "Use", "col_fin": "Valid until",
        "qui_ph": "a first name (kept here only)", "jamais": "Not used yet", "usage": "{u} conversation{s} of {c}",
        "dernier": "last on {d}", "rembourse": "Refunded", "reserve": "Payment not confirmed", "expire": "Expired",
        "copier": "Copy the table", "copie": "Copied ✓", "maj": "Refresh",
        "voit_tit": "What you see, and what you don't",
        "voit": "You see whether each code was used, how many conversations, and the date of the last one. You never see what "
                "was said: conversations are not kept. The names you type here stay in this browser; we never receive them.",
        "dire_tit": "What to tell your employees",
        "dire": "“I will see whether your code was used, and how often — never what you said.”",
    },
    "es": {
        "titre": "El seguimiento de sus códigos", "intro": "Escriba el código de seguimiento recibido con su compra (empieza por SV). También está en su recibo.",
        "code": "Código de seguimiento", "voir": "Ver", "inconnu": "Este código de seguimiento no existe. Verifíquelo en su recibo.",
        "reseau": "Sin red. Vuelva a intentarlo en un momento.",
        "resume": "{n} de {t} código{st} usado{st}.", "resume0": "Ninguno de los {t} códigos se ha usado todavía.", "col_code": "Código", "col_qui": "Entregado a", "col_usage": "Uso", "col_fin": "Válido hasta",
        "qui_ph": "un nombre (se guarda solo aquí)", "jamais": "Todavía sin usar", "usage": "{u} de {c} conversaciones",
        "dernier": "la última el {d}", "rembourse": "Reembolsado", "reserve": "Pago no confirmado", "expire": "Vencido",
        "copier": "Copiar la tabla", "copie": "Copiado ✓", "maj": "Actualizar",
        "voit_tit": "Lo que usted ve, y lo que no ve",
        "voit": "Usted ve si cada código se usó, cuántas conversaciones y la fecha de la última. Nunca ve lo que se dijo: las "
                "conversaciones no se guardan. Los nombres que escribe aquí se quedan en este navegador; no los recibimos.",
        "dire_tit": "Lo que debe decir a sus empleados",
        "dire": "«Veré si tu código se usó, y cuántas veces — nunca lo que dijiste.»",
    },
}


def main():
    page = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Suivi des codes — francis</title>
<link rel="stylesheet" href="/assets/design-system/styles.css"><link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>
body{margin:0;background:#FBFAF7;color:#1d1d1b;font:17px/1.5 Nunito,system-ui,sans-serif}
.page{max-width:860px;margin:0 auto;padding:22px 16px 60px}
h1{font-size:30px;margin:14px 0 6px} h2{font-size:19px;margin:24px 0 6px}
.langues{display:flex;gap:6px;justify-content:flex-end}
.langues button{font:inherit;font-size:14px;border:1px solid #d6d3cc;background:#fff;border-radius:8px;padding:4px 10px;cursor:pointer}
.langues button[aria-pressed=true]{background:#1d1d1b;color:#fff}
form{display:flex;gap:8px;flex-wrap:wrap;margin:12px 0}
form input{font:800 18px ui-monospace,Menlo,monospace;letter-spacing:.1em;padding:9px 12px;border:1px solid #c9c5bb;border-radius:10px;width:170px;text-transform:uppercase}
.btn{font:inherit;font-weight:800;border-radius:10px;border:1px solid #c9c5bb;background:#fff;padding:9px 14px;cursor:pointer}
.btn.pri{background:#17181A;color:#fff;border-color:#17181A}
.resume{font-size:19px;font-weight:800;margin:14px 0 8px}
table{width:100%;border-collapse:collapse;background:#fff;border:1px solid #e3e0d8;border-radius:12px;overflow:hidden}
th,td{text-align:left;padding:10px 12px;border-bottom:1px solid #eeebe4;vertical-align:middle;font-size:15.5px}
th{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#6b6860;background:#f6f4ef}
td code{font-weight:900;letter-spacing:.06em;font-size:15.5px}
td input{font:inherit;width:100%;padding:6px 8px;border:1px solid #d6d3cc;border-radius:8px}
.etat{display:inline-block;border-radius:99px;padding:2px 10px;font-weight:800;font-size:14px}
.e-oui{background:#E2F4EA;color:#0A6B43} .e-non{background:#F1EFEA;color:#5f5c55} .e-off{background:#FBE9E5;color:#8E2B1A}
.muted{color:#6b6860;font-size:14.5px}
.encart{background:#fff;border-left:4px solid #17181A;border-radius:0 12px 12px 0;padding:12px 16px;margin-top:10px}
.err{color:#8E2B1A;font-weight:700}
@media (max-width:640px){ table,tbody,tr,td{display:block;width:100%} thead{display:none}
 tr{padding:10px 12px;border-bottom:1px solid #eeebe4} td{border:0;padding:3px 0} }
</style></head>
<body><div class="fr-barre"><div class="fr-barre__in"><span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span></span></div></div>
<div class="page">
<div class="langues" id="langues"></div>
<h1 id="titre"></h1><p id="intro" class="muted"></p>
<form id="f"><input id="c" maxlength="8" autocomplete="off" aria-label="code"><button class="btn pri" id="voir"></button></form>
<p id="err" class="err" role="alert"></p>
<div id="res"></div>
<h2 id="voitTit"></h2><p id="voit" class="muted"></p>
<div class="encart"><b id="direTit"></b><p id="dire" style="margin:4px 0 0"></p></div>
</div>
<script>
const TXT = %TXT%, PRODUITS = %PRODUITS%;
const q = new URLSearchParams(location.search);
let L = q.get('l') || (navigator.language || 'fr').slice(0, 2); if (!TXT[L]) L = 'fr';
let donnees = null;
const t = (k, v) => (TXT[L][k] || TXT.fr[k]).replace(/\\{(\\w+)\\}/g, (_, x) => v && v[x] != null ? v[x] : '');
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const date = iso => { if (!iso) return ''; try { return new Date(iso + 'T12:00:00').toLocaleDateString(L === 'fr' ? 'fr-CA' : L, {day:'numeric', month:'long', year:'numeric'}); } catch(e) { return iso; } };
const lire = k => { try { return localStorage.getItem(k) || ''; } catch(e) { return ''; } };
const ecrire = (k, v) => { try { localStorage.setItem(k, v); } catch(e) {} };
function etat(c){
  const auj = new Date().toISOString().slice(0, 10);
  if (c.etat === 'rembourse') return ['e-off', t('rembourse')];
  if (c.etat !== 'actif') return ['e-off', t('reserve')];
  if (c.expire && c.expire < auj) return ['e-off', t('expire') + (c.utilisees ? ' — ' + t('usage', {u: c.utilisees, c: c.conversations, s: c.utilisees > 1 ? 's' : '', es: c.utilisees > 1 ? 'es' : ''}) : '')];
  if (!c.utilisees) return ['e-non', t('jamais')];
  return ['e-oui', t('usage', {u: c.utilisees, c: c.conversations, s: c.utilisees > 1 ? 's' : '', es: c.utilisees > 1 ? 'es' : ''}) + (c.dernier ? ', ' + t('dernier', {d: date(c.dernier)}) : '')];
}
function rendre(){
  document.documentElement.lang = L;
  document.getElementById('langues').innerHTML = ['fr', 'en', 'es'].map(l => `<button type="button" data-l="${l}" aria-pressed="${l === L}">${l.toUpperCase()}</button>`).join('');
  for (const id of ['titre', 'intro', 'voir', 'voitTit', 'voit', 'direTit', 'dire']) document.getElementById(id).textContent = t({voitTit: 'voit_tit', direTit: 'dire_tit'}[id] || id);
  document.getElementById('c').setAttribute('aria-label', t('code')); document.getElementById('c').placeholder = 'SV……';
  const z = document.getElementById('res');
  if (!donnees) { z.innerHTML = ''; return; }
  const n = donnees.codes.filter(c => c.utilisees > 0).length, tot = donnees.codes.length;
  z.innerHTML = `<p class="muted">${esc(PRODUITS[donnees.produit] || '')}</p>
    <p class="resume">${esc(t(n ? 'resume' : 'resume0', {n, t: tot, s: n > 1 ? 's' : '', st: tot > 1 ? 's' : '', ont: n > 1 ? 'ont' : 'a'}))}</p>
    <table><thead><tr><th>#</th><th>${esc(t('col_code'))}</th><th>${esc(t('col_qui'))}</th><th>${esc(t('col_usage'))}</th><th>${esc(t('col_fin'))}</th></tr></thead><tbody>
    ${donnees.codes.map((c, i) => { const [cl, tx] = etat(c); return `<tr><td>${i + 1}</td><td><code>${esc(c.code)}</code></td>
      <td><input data-qui="${esc(c.code)}" placeholder="${esc(t('qui_ph'))}" value="${esc(lire('suivi-codes:' + c.code))}"></td>
      <td><span class="etat ${cl}">${esc(tx)}</span></td><td>${esc(date(c.expire))}</td></tr>`; }).join('')}</tbody></table>
    <p style="margin-top:12px;display:flex;gap:8px;flex-wrap:wrap"><button type="button" class="btn" id="maj">${esc(t('maj'))}</button><button type="button" class="btn" id="copier">${esc(t('copier'))}</button></p>`;
  z.querySelectorAll('[data-qui]').forEach(i => i.oninput = () => ecrire('suivi-codes:' + i.dataset.qui, i.value));
  document.getElementById('maj').onclick = () => charger(donnees.suivi);
  document.getElementById('copier').onclick = e => navigator.clipboard.writeText(donnees.codes.map(c =>
    [c.code, lire('suivi-codes:' + c.code), etat(c)[1], c.expire].join('\\t')).join('\\n')).then(() => { e.target.textContent = t('copie'); });
}
async function charger(code){
  const err = document.getElementById('err'); err.textContent = '';
  code = (code || '').trim().toUpperCase(); if (!code) return;
  try {
    const r = await fetch('/api/pelerins/suivi?code=' + encodeURIComponent(code));
    if (!r.ok) { donnees = null; err.textContent = t('inconnu'); rendre(); return; }
    donnees = await r.json(); ecrire('suivi-codes:dernier', code); document.getElementById('c').value = code;
    history.replaceState(null, '', location.pathname + '?c=' + encodeURIComponent(code) + (q.get('l') ? '&l=' + L : ''));
  } catch(e) { err.textContent = t('reseau'); }
  rendre();
}
document.getElementById('langues').onclick = e => { const b = e.target.closest('button'); if (!b) return; L = b.dataset.l; rendre(); };
document.getElementById('f').onsubmit = e => { e.preventDefault(); charger(document.getElementById('c').value); };
const depart = q.get('c') || lire('suivi-codes:dernier');
document.getElementById('c').value = depart;
rendre(); if (depart) charger(depart);
</script>
</body></html>
"""
    page = page.replace("%TXT%", json.dumps(TXT, ensure_ascii=False)).replace("%PRODUITS%", json.dumps(PRODUITS, ensure_ascii=False))
    SORTIE.write_text(page, encoding="utf-8")
    print(SORTIE.relative_to(RACINE), "— fr, en, es")


if __name__ == "__main__":
    main()
