/* =========================================================================
   Dépôt de matériel — quatrième onglet de l'espace enseignant.

   Rendu selon la remise « Dépôt de matériel ». Deux vues d'un même écran,
   Ma semaine et Le catalogue, avec le même panneau de détail : changer de
   vue ne perd ni la séance ouverte ni la sélection.

   Le module ne connaît ni la session ni les groupes : `enseignant.js` lui
   passe ce dont il a besoin dans `Materiel.init()`. Il ne touche jamais au
   `localStorage` ni à `fetch` directement — le jeton reste l'affaire de la
   page hôte.
   ========================================================================= */

window.Materiel = (() => {
  'use strict';

  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s ?? '').replace(/[&<>"']/g,
    (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /** Recherche insensible aux accents : l'enseignante qui tape « probleme »
      doit trouver « problème ». */
  const plat = (s) => String(s ?? '').normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '').toLowerCase();

  /** Poids en mégaoctets, virgule décimale — nous écrivons en français. */
  function poids(octets) {
    if (!octets && octets !== 0) return '';
    if (octets < 1024) return `${octets} octets`;
    if (octets < 1024 * 1024) return `${Math.round(octets / 1024)} Ko`;
    return `${(octets / (1024 * 1024)).toFixed(1).replace('.', ',')} Mo`;
  }

  const MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
    'août', 'septembre', 'octobre', 'novembre', 'décembre'];
  const JOURS = ['dimanche', 'lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi'];

  /** Le premier du mois s'écrit « 1er », les autres en chiffres nus. */
  const quantieme = (d) => (d.getDate() === 1 ? '1er' : String(d.getDate()));

  const jourDate = (iso) => {
    const d = new Date(`${iso}T12:00:00`);
    return `${JOURS[d.getDay()]} ${quantieme(d)} ${MOIS[d.getMonth()]}`;
  };
  const longDate = (iso) => {
    if (!iso) return '';
    const d = new Date(`${String(iso).slice(0, 10)}T12:00:00`);
    return `${quantieme(d)} ${MOIS[d.getMonth()]} ${d.getFullYear()}`;
  };
  const iso = (d) => new Date(d.getTime() - d.getTimezoneOffset() * 60000)
    .toISOString().slice(0, 10);

  const GENRES = {
    presentation: 'Présentation de séance',
    fiche: 'Fiche élève à imprimer',
    plan: 'Plan de cours',
    annexe: 'Document annexe',
  };
  const ETATS = {
    complet: { classe: 'offerte', glyphe: '✓', mot: 'Complet' },
    partiel: { classe: 'fermee', glyphe: '·', mot: 'Partiel' },
    'a-venir': { classe: 'vide', glyphe: '→', mot: 'À venir' },
  };

  /* ══════════ État ══════════ */

  const etat = {
    vue: 'semaine',
    inventaire: null,
    depots: [],
    promotions: [],
    derniereVisite: '',
    role: 'prof',
    charge: false,
    q: '',
    cat: '', niv: '', dom: '', typ: '', bloc: '',
    ouverts: {},                    // activiteId → module déplié
    detail: null,                   // { activiteId, code } — code null = atelier
    sel: {},                        // "activiteId:code" → true
    televersement: null,            // { nom, pct }
  };

  let ctx = null;                   // fourni par enseignant.js
  let branche = false;
  let minuterie;

  /* ══════════ Accès aux données ══════════ */

  const porteurs = () => (etat.inventaire && etat.inventaire.porteurs) || [];
  const porteur = (id) => porteurs().find((p) => p.activiteId === id) || null;
  const activite = (id) => ctx.activites().find((a) => a.id === id) || null;
  const seanceDe = (p, code) => (p ? p.seances.find((s) => (s.code || null) === code) : null);
  const blocNom = (b) => (etat.inventaire.blocs || {})[b] || '';

  const estNeuf = (d) => Boolean(etat.derniereVisite && d &&
    String(d).slice(0, 10) >= String(etat.derniereVisite).slice(0, 10) &&
    String(d) > String(etat.derniereVisite).slice(0, 10));

  const depotsDe = (id) => etat.depots.filter((d) => d.activiteId === id);

  /** Le fichier officiel qu'un dépôt peut remplacer : même activité, même
      séance, même type. Sans lui, « Remplacer l'officiel » n'a pas de cible
      et le bouton ne paraît pas. */
  function officielPour(depot) {
    const p = porteur(depot.activiteId);
    if (!p) return null;
    const s = p.seances.find((x) => (x.code || null) === (depot.seanceCode || null));
    if (!s) return null;
    return s.fichiers.find((f) => f.type === depot.type) || null;
  }

  const promotionDe = (depotId) => etat.promotions.find((p) => p.depotId === depotId);

  /** Les fichiers d'une séance, dans l'ordre présentation → fiche → plan. */
  const ORDRE = { presentation: 0, fiche: 1, plan: 2, annexe: 3 };
  const fichiersTries = (s) => [...(s.fichiers || [])]
    .sort((a, b) => (ORDRE[a.type] ?? 9) - (ORDRE[b.type] ?? 9));

  /* ══════════ Messages ══════════ */

  function confirmer(texte) {
    const el = $('matConfirme');
    el.innerHTML = `<span aria-hidden="true">✓</span><span>${esc(texte)}</span>`;
    el.hidden = false;
    clearTimeout(minuterie);
    minuterie = setTimeout(() => { el.hidden = true; }, 4200);
  }

  /* ══════════ Chargement ══════════ */

  async function charger() {
    const d = await ctx.json('/api/materiel');
    etat.inventaire = d.materiel;
    etat.depots = d.depots || [];
    etat.promotions = d.promotions || [];
    etat.derniereVisite = d.derniereVisite || '';
    etat.role = d.role || 'prof';
    etat.charge = true;
    // Le repère « nouveau » est calculé avant d'avancer la date : sinon un
    // simple rafraîchissement effacerait les repères avant leur lecture.
    ctx.json('/api/materiel/visite', { method: 'POST' }).catch(() => { /* sans gravité */ });
  }

  /* ══════════ Vue « Ma semaine » ══════════ */

  /** Les activités du groupe actif ayant une date cette semaine.

      La planification porte des dates **par activité**, pas par séance :
      `schedule.json` n'a pas de `sectionId`. On ne peut donc pas écrire
      « mardi, séance B3 ». La rangée affiche l'activité du jour et offre ses
      seize séances en pastilles — c'est le raccourci le plus court que la
      donnée permette honnêtement. */
  function semaine() {
    const auj = new Date();
    const lundi = new Date(auj);
    lundi.setDate(auj.getDate() - ((auj.getDay() + 6) % 7));
    const jours = [];
    for (let i = 0; i < 5; i += 1) {
      const d = new Date(lundi);
      d.setDate(lundi.getDate() + i);
      jours.push(iso(d));
    }
    const demain = iso(new Date(auj.getTime() + 86400000));
    const parJour = {};
    ctx.activites().forEach((a) => {
      const d = (a.datePrevue || '').slice(0, 10);
      if (d && jours.includes(d)) (parJour[d] = parJour[d] || []).push(a);
    });
    return { jours, parJour, auj: iso(auj), demain, lundi: jours[0], vendredi: jours[4] };
  }

  function rendreSemaine() {
    const s = semaine();
    const g = ctx.groupe();
    const remplis = s.jours.filter((j) => s.parJour[j]);

    let html = `
      <div class="mat-entete">
        <div>
          <div class="pe-eyebrow">Semaine du ${esc(longDate(s.lundi))} au ${esc(longDate(s.vendredi))}</div>
          <h2>Ce que ${g ? 'le groupe ' + esc(g.nom) : 'mon groupe'} fait cette semaine</h2>
        </div>
      </div>`;

    if (!remplis.length) {
      html += `
        <div class="card" style="text-align:center;padding:var(--sp-12) var(--sp-6)">
          <div style="font-size:var(--fs-lead);font-weight:var(--fw-semi);color:var(--text-strong)">
            Aucun cours planifié pour ce groupe cette semaine.</div>
          <p style="margin:var(--sp-3) 0 var(--sp-5);font-size:var(--fs-body-sm);font-weight:var(--fw-medium);color:var(--text-muted)">
            Le matériel apparaîtra ici dès qu'une date sera posée dans l'onglet Planifier.</p>
          <button type="button" class="btn btn--ghost" data-action="vue" data-vue="catalogue">Ouvrir le catalogue</button>
        </div>`;
    }

    remplis.forEach((j) => {
      const quand = j === s.auj ? 'auj' : (j === s.demain ? 'demain' : 'autre');
      const etiquette = quand === 'auj' ? '<span class="mat-quand mat-quand--auj">Aujourd\'hui</span>'
        : (quand === 'demain' ? '<span class="mat-quand mat-quand--demain">Demain</span>' : '');
      html += `<div class="card card--flush mat-jour--${quand}">
        <div class="mat-jour-entete"><span>${esc(jourDate(j))}</span>${etiquette}</div>
        ${s.parJour[j].map(rangeePlage).join('')}
      </div>`;
    });

    return html;
  }

  function rangeePlage(a) {
    const p = porteur(a.id);
    const cours = a.categorie === 'cours';
    const heures = cours ? '8 h 30 – 12 h 30' : '13 h 00 – 15 h 00';
    const genre = cours ? 'Cours · 4 h' : 'Atelier · 2 h';

    let etatTexte = 'Aucun matériel au dépôt pour l\'instant.';
    let actions = '';
    let pastilles = '';

    if (p && p.seancesEquipees) {
      const nbFic = p.seances.reduce((n, x) => n + x.fichiers.length, 0);
      etatTexte = cours
        ? `${p.seancesEquipees} séance${p.seancesEquipees > 1 ? 's' : ''} équipée${p.seancesEquipees > 1 ? 's' : ''} sur ${p.seancesPrevues} · ${nbFic} fichier${nbFic > 1 ? 's' : ''}`
        : `${nbFic} fichier${nbFic > 1 ? 's' : ''} au dépôt`;
      const maj = p.seances.flatMap((x) => x.fichiers.map((f) => f.majLe)).sort().pop();
      if (maj) etatTexte += ` · mise à jour le ${longDate(maj)}`;

      actions = `
        <button type="button" class="btn btn--pri btn--sm" data-action="ouvrir-module" data-id="${a.id}">Voir le matériel</button>
        <button type="button" class="btn btn--ghost btn--sm" data-action="archive" data-id="${a.id}" data-portee="presentations">Présentations</button>`;
      if (p.seances.some((x) => x.fichiers.some((f) => f.type === 'fiche'))) {
        actions += `<button type="button" class="btn btn--ghost btn--sm" data-action="archive" data-id="${a.id}" data-portee="fiches">Fiches</button>`;
      }

      if (cours) {
        pastilles = `<div class="mat-pastilles">${p.seances.map((x) => {
          const vide = !x.fichiers.length;
          const ouverte = etat.detail && etat.detail.activiteId === a.id && etat.detail.code === x.code;
          return `<button type="button" class="mat-pastille-seance${ouverte ? ' is-ouverte' : ''}"
            data-action="detail" data-id="${a.id}" data-code="${esc(x.code)}"
            title="${esc(x.titre || x.code)}"${vide ? ' disabled' : ''}>${esc(x.code)}</button>`;
        }).join('')}</div>`;
      }
    }

    return `<div class="mat-plage">
      <div class="mat-heures"><b>${heures}</b><span>${genre}</span></div>
      <div class="mat-plage-txt">
        <div class="pe-eyebrow">${esc(a.level || '')}${a.domaineDeVie ? ' · ' + esc(a.domaineDeVie) : ''}</div>
        <div style="margin-top:2px;font-size:var(--fs-body);font-weight:var(--fw-bold);color:var(--text-strong)">${esc(a.title)}</div>
        <div style="margin-top:2px;font-size:var(--fs-ui-sm);font-weight:var(--fw-medium);color:var(--text-muted)">${esc(etatTexte)}</div>
        ${pastilles}
      </div>
      <div class="mat-plage-actions">${actions}</div>
    </div>`;
  }

  /* ══════════ Vue « Le catalogue » ══════════ */

  function optionsDe(cle) {
    const vues = new Set();
    ctx.activites().forEach((a) => { if (a[cle]) vues.add(a[cle]); });
    return [...vues].sort();
  }

  function selecteur(id, libelle, valeurs, choisi, toutes) {
    return `<div>
      <label class="field-label" for="mat-${id}">${esc(libelle)}</label>
      <select class="field" id="mat-${id}" data-filtre="${id}">
        <option value="">${esc(toutes)}</option>
        ${valeurs.map((v) => `<option value="${esc(v.val ?? v)}"${(v.val ?? v) === choisi ? ' selected' : ''}>${esc(v.lib ?? v)}</option>`).join('')}
      </select>
    </div>`;
  }

  /** Un porteur passe-t-il les filtres ? La recherche porte sur le titre du
      module, le code et le titre des séances, et les mots-clés de l'activité. */
  function garde(p) {
    const a = activite(p.activiteId);
    if (!a) return false;
    if (etat.cat && a.categorie !== etat.cat) return false;
    if (etat.niv && a.level !== etat.niv) return false;
    if (etat.dom && a.domaineDeVie !== etat.dom) return false;
    if (etat.typ && !p.seances.some((s) => s.fichiers.some((f) => f.type === etat.typ))) return false;
    if (etat.bloc && !p.seances.some((s) => s.bloc === etat.bloc)) return false;
    if (etat.q) {
      const q = plat(etat.q);
      const foin = plat([a.title, a.domaineDeVie, (a.keywords || []).join(' '),
        p.seances.map((s) => `${s.code || ''} ${s.titre || ''}`).join(' ')].join(' '));
      if (!foin.includes(q)) return false;
    }
    return true;
  }

  /** Les séances retenues à l'intérieur d'un module. Un module dont le titre
      correspond à la recherche garde toutes ses séances. */
  function seancesVisibles(p) {
    const a = activite(p.activiteId);
    const titreCorrespond = !etat.q || plat(a.title).includes(plat(etat.q));
    return p.seances.filter((s) => {
      if (etat.bloc && s.bloc !== etat.bloc) return false;
      if (etat.typ && !s.fichiers.some((f) => f.type === etat.typ)) return false;
      if (etat.q && !titreCorrespond) {
        return plat(`${s.code || ''} ${s.titre || ''}`).includes(plat(etat.q));
      }
      return true;
    });
  }

  function rendreCatalogue() {
    const retenus = porteurs().filter(garde);
    const cours = retenus.filter((p) => p.categorie === 'cours');
    const ateliers = retenus.filter((p) => p.categorie === 'atelier');
    const niveaux = optionsDe('level');
    const domaines = optionsDe('domaineDeVie');

    const nbSeances = cours.reduce((n, p) => n + p.seancesEquipees, 0);
    const nbNeufs = porteurs().reduce((n, p) => n + p.seances
      .reduce((m, s) => m + s.fichiers.filter((f) => estNeuf(f.majLe)).length, 0), 0);

    let html = `<div class="card">
      <div class="stack">
        <div style="display:flex;gap:var(--sp-3);flex-wrap:wrap">
          <input class="field" type="search" id="matRecherche" style="flex:1;min-width:260px"
                 value="${esc(etat.q)}"
                 placeholder="Chercher un module, une séance, un mot-clé (les accents sont facultatifs)" />
          <button type="button" class="btn btn--ghost btn--sm" data-action="reinitialiser">Réinitialiser</button>
        </div>
        <div class="mat-filtres-grille">
          ${selecteur('cat', 'Type de séance', [{ val: 'cours', lib: 'Cours (4 h, matin)' }, { val: 'atelier', lib: 'Ateliers (2 h, après-midi)' }], etat.cat, 'Cours et ateliers')}
          ${niveaux.length > 1 ? selecteur('niv', 'Niveau', niveaux, etat.niv, 'Tous les niveaux') : ''}
          ${selecteur('dom', 'Domaine de vie', domaines, etat.dom, 'Tous les domaines')}
          ${selecteur('typ', 'Type de fichier', [{ val: 'presentation', lib: 'Présentation' }, { val: 'fiche', lib: 'Fiche à imprimer' }, { val: 'plan', lib: 'Plan de cours' }], etat.typ, 'Tous les fichiers')}
          ${selecteur('bloc', 'Bloc de séance', Object.entries(etat.inventaire.blocs || {}).map(([k, v]) => ({ val: k, lib: `${k} · ${v}` })), etat.bloc, 'Tous les blocs')}
        </div>
        <div style="font-size:var(--fs-ui-sm);font-weight:var(--fw-medium);color:var(--text-muted)">
          ${cours.length} module${cours.length > 1 ? 's' : ''} · ${nbSeances} séance${nbSeances > 1 ? 's' : ''} équipée${nbSeances > 1 ? 's' : ''} ·
          ${ateliers.length} atelier${ateliers.length > 1 ? 's' : ''} · ${nbNeufs} fichier${nbNeufs > 1 ? 's' : ''} nouveau${nbNeufs > 1 ? 'x' : ''}${etat.derniereVisite ? ` depuis votre dernière visite du ${esc(longDate(etat.derniereVisite))}` : ''}.
        </div>
      </div>
    </div>`;

    if (!retenus.length) {
      return html + `<div class="card" style="text-align:center;padding:var(--sp-12) var(--sp-6)">
        <div style="font-size:var(--fs-lead);font-weight:var(--fw-semi);color:var(--text-strong)">
          Aucun résultat${etat.q ? ` pour « ${esc(etat.q)} »` : ''}.</div>
        <p style="margin:var(--sp-3) 0 var(--sp-5);font-size:var(--fs-body-sm);font-weight:var(--fw-medium);color:var(--text-muted)">
          Essayez un mot du titre du module, un code de séance (B3), ou retirez un filtre.</p>
        <button type="button" class="btn btn--ghost" data-action="reinitialiser">Retirer les filtres</button>
      </div>`;
    }

    if (cours.length) {
      html += `<section><div class="pe-entete-section"><div class="pe-titre-section">Modules de cours</div></div>
        <div class="stack">${cours.map(carteModule).join('')}</div></section>`;
    }
    if (ateliers.length) {
      html += `<section>
        <div class="pe-entete-section" style="align-items:baseline">
          <div class="pe-titre-section">Ateliers de l'après-midi</div>
          <div class="pe-resume">Une présentation par atelier, sans découpage en séances.</div>
        </div>
        <div class="grid-auto">${ateliers.map(carteAtelier).join('')}</div></section>`;
    }
    return html;
  }

  function carteModule(p) {
    const a = activite(p.activiteId);
    const e = ETATS[p.etat];
    const ouvert = Boolean(etat.ouverts[p.activiteId]);
    const visibles = seancesVisibles(p);
    const neuf = p.seances.some((s) => s.fichiers.some((f) => estNeuf(f.majLe)));

    const actions = p.etat === 'a-venir' ? '' : `
      <button type="button" class="btn btn--pri btn--sm" data-action="archive" data-id="${p.activiteId}" data-portee="module">Tout prendre</button>
      <button type="button" class="btn btn--ghost btn--sm" data-action="archive" data-id="${p.activiteId}" data-portee="fiches">Les fiches</button>`;

    return `<div class="card card--flush">
      <div class="mat-module-entete">
        <button type="button" class="pe-chevron" data-action="deplier" data-id="${p.activiteId}"
                aria-expanded="${ouvert}" aria-label="${ouvert ? 'Replier' : 'Déplier'} ${esc(a.title)}">${ouvert ? '–' : '+'}</button>
        <div class="mat-module-txt">
          <div class="pe-eyebrow">${esc(a.level || '')} · ${esc(a.domaineDeVie || '')} · cours de 4 h</div>
          <h3>${esc(a.title)}</h3>
          <div class="mat-module-etat">
            <span class="pe-pastille pe-pastille--${e.classe}"><span aria-hidden="true">${e.glyphe}</span>${e.mot}</span>
            <span style="font-size:var(--fs-ui-sm);font-weight:var(--fw-semi);color:var(--text-muted)">
              ${p.seancesEquipees} séance${p.seancesEquipees > 1 ? 's' : ''} équipée${p.seancesEquipees > 1 ? 's' : ''} sur ${p.seancesPrevues}</span>
            ${neuf ? '<span class="mat-neuf">Nouveau</span>' : ''}
          </div>
        </div>
        <div class="mat-module-actions">${actions}</div>
      </div>
      ${ouvert ? visibles.map((s) => rangeeSeance(p, s)).join('') : ''}
    </div>`;
  }

  function rangeeSeance(p, s) {
    const cle = `${p.activiteId}:${s.code}`;
    const choisie = Boolean(etat.sel[cle]);
    const aPres = s.fichiers.some((f) => f.type === 'presentation');
    const aFiche = s.fichiers.some((f) => f.type === 'fiche');
    const fic = !s.fichiers.length ? '<span class="mat-seance-fic mat-seance-fic--rien">Rien encore</span>'
      : `<span class="mat-seance-fic">${[aPres ? 'Prés.' : '', aFiche ? 'Fiche' : ''].filter(Boolean).join(' + ')}</span>`;

    return `<div class="mat-seance${choisie ? ' is-choisie' : ''}">
      <input type="checkbox" class="pe-case" data-action="cocher" data-cle="${esc(cle)}"
             ${choisie ? 'checked' : ''}${s.fichiers.length ? '' : ' disabled'}
             aria-label="Choisir la séance ${esc(s.code)}" />
      <span class="mat-seance-code">${esc(s.code)}</span>
      <span class="mat-seance-bloc">${esc(blocNom(s.bloc))}</span>
      <button type="button" class="mat-seance-titre" data-action="detail"
              data-id="${p.activiteId}" data-code="${esc(s.code)}">${esc(s.titre || 'Séance ' + s.code)}</button>
      ${fic}
      <button type="button" class="btn btn--ghost btn--sm" data-action="detail"
              data-id="${p.activiteId}" data-code="${esc(s.code)}">Voir</button>
    </div>`;
  }

  function carteAtelier(p) {
    const a = activite(p.activiteId);
    const nb = p.seances.reduce((n, s) => n + s.fichiers.length, 0);
    return `<div class="card">
      <div class="pe-eyebrow">${esc(a.level || '')} · ${esc(a.domaineDeVie || '')} · atelier de 2 h</div>
      <div style="margin-top:var(--sp-2);font-size:var(--fs-body);font-weight:var(--fw-black);color:var(--text-strong)">${esc(a.title)}</div>
      <div style="margin-top:var(--sp-2);font-size:var(--fs-ui-sm);font-weight:var(--fw-medium);color:var(--text-muted)">
        ${nb ? `${nb} fichier${nb > 1 ? 's' : ''} au dépôt` : 'Aucun fichier au dépôt'}</div>
      <div style="margin-top:var(--sp-4)">
        <button type="button" class="btn btn--ghost btn--sm" data-action="detail" data-id="${p.activiteId}"
                ${nb ? '' : 'disabled'}>Voir le matériel</button>
      </div>
    </div>`;
  }

  /* ══════════ Dépôts de l'équipe ══════════ */

  /** Les gestes réservés à l'administration sur une rangée de dépôt.
      L'absence du bouton n'est pas une garde : le serveur revalide le rôle
      à chaque requête. */
  function boutonsAdmin(d) {
    if (etat.role !== 'admin') return '';
    const promue = promotionDe(d.id);
    if (promue) {
      return `<button type="button" class="btn btn--ghost btn--sm"
        data-action="rendre-officiel" data-fichier="${esc(promue.fichierId)}">Rendre l'officiel</button>
        <button type="button" class="btn btn--ghost btn--sm" data-action="retirer-depot" data-dep="${esc(d.id)}">Retirer</button>`;
    }
    const cible = officielPour(d);
    return `${cible ? `<button type="button" class="btn btn--ghost btn--sm"
        data-action="promouvoir" data-dep="${esc(d.id)}" data-fichier="${esc(cible.id)}"
        title="Ce dépôt sera servi à la place du fichier officiel de la séance ${esc(d.seanceCode || '')}">Remplacer l'officiel</button>` : ''}
      <button type="button" class="btn btn--ghost btn--sm" data-action="retirer-depot" data-dep="${esc(d.id)}">Retirer</button>`;
  }

  function rendreDepots() {
    const cible = etat.detail ? etat.detail.activiteId : null;
    const liste = cible ? depotsDe(cible) : etat.depots;
    const a = cible ? activite(cible) : null;

    const t = etat.televersement;
    const barre = t ? `<div class="card__row">
      <div style="width:100%">
        <div style="display:flex;gap:var(--sp-3);font-size:var(--fs-ui-sm);font-weight:var(--fw-bold)">
          <span style="flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap">Téléversement de ${esc(t.nom)}</span>
          <span>${t.pct} %</span>
        </div>
        <div class="mat-barre" style="margin-top:var(--sp-2)"><i style="width:${t.pct}%"></i></div>
      </div>
    </div>` : '';

    const rangees = liste.length ? liste.map((d) => {
      const act = activite(d.activiteId);
      return `<div class="card__row">
        <div class="pe-doc">
          <span class="pe-ext">${esc((d.format || '').toUpperCase())}</span>
          <div class="pe-doc-txt">
            <div class="pe-doc-nom">${esc((d.seanceCode ? d.seanceCode + ' — ' : '') + (d.note || d.nom))}</div>
            <div class="pe-doc-meta">Dépôt de ${esc(d.auteur ? d.auteur.nom : 'un collègue')} · ${esc(d.format)} ·
              ${esc(poids(d.octets))} · ${esc(longDate(d.deposeLe))}${act && !cible ? ' · ' + esc(act.title) : ''} ·
              à côté du fichier officiel</div>
          </div>
          <div style="margin-left:auto;display:flex;gap:var(--sp-2);flex-wrap:wrap">
            <a class="btn btn--ghost btn--sm" href="${esc(d.chemin)}" download>Télécharger</a>
            ${boutonsAdmin(d)}
          </div>
        </div>
      </div>` ;
    }).join('') : `<div class="card__row"><div class="pe-doc-meta">
      ${cible ? 'Personne n\'a encore déposé de fichier pour cette activité. Le vôtre serait le premier.'
        : 'Aucun dépôt pour l\'instant. Ouvrez une séance pour y déposer votre version.'}</div></div>`;

    return `<section>
      <div class="pe-entete-section" style="align-items:baseline">
        <div class="pe-titre-section">Dépôts de l'équipe</div>
        <div class="pe-resume">Vos versions retravaillées se placent à côté du fichier officiel, jamais à sa place.</div>
      </div>
      <div class="card card--flush">
        ${cible ? `<div class="card__band">${esc(a.title)}</div>` : ''}
        ${rangees}
        ${barre}
        <div class="card__row" style="background:var(--surface-sunken)">
          ${cible ? `<label class="pe-depot">
            <input type="file" id="matFichier" data-action="televerser" data-id="${cible}" />
            <b>Téléverser un fichier</b>
            <span>Il sera marqué à votre nom, à côté du fichier officiel${etat.detail.code ? ' de la séance ' + esc(etat.detail.code) : ''}.</span>
          </label>` : `<div class="pe-doc-meta">Ouvrez une séance à gauche pour y téléverser votre version.</div>`}
        </div>
      </div>
    </section>`;
  }

  /* ══════════ Panneau de détail ══════════ */

  function rendreAside() {
    let html = '';

    const cles = Object.keys(etat.sel).filter((k) => etat.sel[k]);
    if (cles.length) html += carteSelection(cles);

    html += etat.detail ? carteDetail() : `<div class="card card--tinted">
      <div style="font-size:var(--fs-body-sm);font-weight:var(--fw-medium);color:var(--text-body)">
        Choisissez une séance à gauche : sa présentation et sa fiche élève s'affichent ici,
        avec l'aperçu, le poids et la date de mise à jour.</div>
    </div>`;

    html += carteEtatDepot();
    return html;
  }

  function carteSelection(cles) {
    const parModule = {};
    cles.forEach((k) => {
      const [id, code] = k.split(':');
      (parModule[id] = parModule[id] || []).push(code);
    });
    const ids = Object.keys(parModule);
    const unSeul = ids.length === 1;
    const codes = unSeul ? parModule[ids[0]].sort() : [];
    const p = unSeul ? porteur(Number(ids[0])) : null;
    const nom = unSeul
      ? `${p.slug || 'materiel'}_${codes.slice(0, 4).join('-')}${codes.length > 4 ? `-et-${codes.length - 4}-autres` : ''}.zip`
      : 'Choisissez des séances d\'un seul module à la fois.';

    return `<div class="mat-selection">
      <b>${cles.length} séance${cles.length > 1 ? 's' : ''} choisie${cles.length > 1 ? 's' : ''}</b>
      <code>${esc(nom)}</code>
      <div class="mat-selection-actions">
        ${unSeul ? `
        <button type="button" class="btn btn--ghost btn--sm" data-action="archive" data-id="${ids[0]}" data-portee="presentations" data-sel="1">Télécharger les présentations</button>
        <button type="button" class="btn btn--ghost btn--sm" data-action="archive" data-id="${ids[0]}" data-portee="fiches" data-sel="1">Télécharger les fiches</button>
        <button type="button" class="btn btn--ghost btn--sm" data-action="imprimer-selection">Imprimer les fiches choisies</button>` : ''}
        <button type="button" class="btn btn--ghost btn--sm" data-action="vider">Vider la sélection</button>
      </div>
    </div>`;
  }

  function carteDetail() {
    const p = porteur(etat.detail.activiteId);
    const s = seanceDe(p, etat.detail.code);
    const a = activite(etat.detail.activiteId);
    if (!p || !s || !a) return '';

    const cours = p.categorie === 'cours';
    const surtitre = cours
      ? `${esc(a.title)} · séance ${esc(s.code)}${s.bloc ? ' · ' + esc(blocNom(s.bloc)) : ''}`
      : `Atelier de 2 h · ${esc(a.level || '')} · ${esc(a.domaineDeVie || '')}`;
    const titre = cours ? (s.titre || `Séance ${s.code}`) : a.title;
    const contexte = cours
      ? `${esc(a.level || '')} · ${esc(a.domaineDeVie || '')}${s.duree ? ' · ' + esc(s.duree) : ''}`
      : 'Séance unique, l\'après-midi.';

    const blocs = fichiersTries(s).map((f) => blocFichier(p, s, f)).join('')
      + (cours && !s.fichiers.some((f) => f.type === 'fiche') ? manque(p, 'fiche') : '')
      + (cours && !s.fichiers.some((f) => f.type === 'presentation') ? manque(p, 'presentation') : '');

    return `<div class="card card--flush card--marked">
      <div style="padding:var(--sp-5) var(--sp-6) 0">
        <div class="pe-eyebrow">${surtitre}</div>
        <h3 style="margin:var(--sp-2) 0 0;font-size:var(--fs-h3);font-weight:var(--fw-black);color:var(--text-strong)">${esc(titre)}</h3>
        <div style="margin-top:4px;font-size:var(--fs-ui-sm);font-weight:var(--fw-medium);color:var(--text-muted)">${contexte}</div>
      </div>
      ${blocs}
      <div class="card__row" style="background:var(--surface-sunken);display:flex;gap:var(--sp-2);flex-wrap:wrap">
        ${s.fichiers.length ? `<button type="button" class="btn btn--pri btn--sm" data-action="archive"
           data-id="${p.activiteId}" data-portee="${cours ? 'seances' : 'module'}" data-codes="${esc(s.code || '')}">Prendre la séance complète</button>` : ''}
        <button type="button" class="btn btn--ghost btn--sm" data-action="fermer">Fermer</button>
      </div>
    </div>`;
  }

  function blocFichier(p, s, f) {
    const neuf = estNeuf(f.majLe);
    const estFiche = f.type === 'fiche';
    const titre = s.code ? `Séance ${s.code} — ${s.titre || ''}` : (activite(p.activiteId) || {}).title;

    let apercu = '';
    if (f.type === 'presentation') {
      apercu = `<div class="mat-apercu">
        ${f.vignette
          ? `<img src="${esc(f.vignette)}" alt="Première diapositive de la séance ${esc(s.code || '')}" loading="lazy" />`
          : `<div class="mat-substitut">${esc(titre)}</div>`}
        <div class="mat-legende">${f.vignette
          ? `Aperçu de la diapositive 1${f.diapositives ? ` sur ${f.diapositives}` : ''}`
          : (f.promotion
            ? 'Pas de vignette : les vignettes sont produites par le build, un fichier déposé n\'en a pas.'
            : 'Vignette non produite — relancez build/vignettes.py')}</div>
      </div>`;
    } else if (estFiche) {
      apercu = `<div class="mat-apercu">
        <iframe src="${esc(f.chemin)}" title="Aperçu de la fiche" loading="lazy"
                style="width:100%;aspect-ratio:16/9;border:1px solid var(--border-tint);border-radius:6px;background:var(--white)"></iframe>
        <div class="mat-legende">Aperçu à l'écran · l'impression sort en noir et blanc, sans interface</div>
      </div>`;
    }

    const meta = [
      f.format === 'pptx' ? 'PowerPoint' : (f.format || '').toUpperCase(),
      poids(f.octets),
      f.diapositives ? `${f.diapositives} diapositives` : '',
      f.blocs ? `${f.blocs} blocs` : '',
      f.impression === 'lettre-nb' ? 'lettre noir et blanc' : '',
      f.majLe ? `mise à jour le ${longDate(f.majLe)}` : '',
    ].filter(Boolean).join(' · ');

    // Un fichier promu n'est jamais servi en silence : la rangée dit de qui
    // il vient, et l'officiel reste téléchargeable à côté.
    const promo = f.promotion;
    const marque = promo ? `
      <div class="mat-manque" style="background:var(--accent-soft);border-color:var(--accent)">
        <b style="color:var(--accent-ink)">Version de ${esc(promo.auteur ? promo.auteur.nom : 'l\'équipe')}, mise à la place de l'officiel</b>
        <span style="color:var(--accent-ink)">${esc(promo.note || 'Sans note.')} Remplacée le ${esc(longDate(promo.leQuand))} par ${esc(promo.parNom || 'l\'administration')}.</span>
        ${promo.perimee ? `<span style="color:var(--warn-ink);font-weight:var(--fw-bold)">
          Attention : le fichier officiel a été reproduit depuis. Cette version cache une production plus récente.</span>` : ''}
        <div class="mat-actions">
          <a class="btn btn--ghost btn--sm" href="${esc(f.cheminOfficiel || '')}" download>Télécharger l'officiel</a>
          ${etat.role === 'admin' ? `<button type="button" class="btn btn--ghost btn--sm"
            data-action="rendre-officiel" data-fichier="${esc(f.id)}">Rendre l'officiel</button>` : ''}
        </div>
      </div>` : '';

    return `<div class="mat-fichier">
      <div style="display:flex;gap:var(--sp-3);align-items:center;flex-wrap:wrap">
        <span class="mat-genre">${esc(GENRES[f.type] || f.type)}</span>
        ${neuf ? '<span class="mat-neuf">Nouveau</span>' : ''}
        ${promo ? '<span class="mat-neuf" style="background:var(--accent);color:var(--white)">Remplacé</span>' : ''}
      </div>
      ${marque}
      <div class="mat-fichier-titre">${esc(titre)}</div>
      ${f.resume ? `<div class="mat-resume">${esc(f.resume)}</div>` : ''}
      ${apercu}
      <div class="mat-meta">${esc(meta)}</div>
      <div class="mat-actions">
        ${estFiche ? `<a class="btn btn--pri btn--sm" href="${esc(f.chemin)}" target="_blank" rel="noopener">Ouvrir</a>` : ''}
        <a class="btn btn--ghost btn--sm" href="${esc(f.chemin)}" download>Télécharger</a>
        ${estFiche ? `<button type="button" class="btn btn--ghost btn--sm" data-action="imprimer" data-chemin="${esc(f.chemin)}">Imprimer</button>` : ''}
      </div>
    </div>`;
  }

  /** Jamais de case vide muette : ce qui manque se dit, avec le motif que
      l'inventaire permet réellement d'établir. */
  function manque(p, type) {
    const quoi = type === 'fiche' ? 'La fiche élève' : 'La présentation';
    const motif = p.etat === 'partiel'
      ? `Production en cours : le module compte ${p.seancesEquipees} séances équipées sur ${p.seancesPrevues}.`
      : 'Ce fichier n\'a pas été produit pour cette séance.';
    return `<div class="mat-fichier">
      <div class="mat-manque">
        <b>${quoi} n'est pas encore produite</b>
        <span>${esc(motif)}</span>
      </div>
    </div>`;
  }

  function carteEtatDepot() {
    const r = etat.inventaire.resume || {};
    const maj = porteurs().flatMap((p) => p.seances.flatMap((s) => s.fichiers.map((f) => f.majLe)))
      .filter(Boolean).sort().pop();
    return `<div class="card card--tinted">
      <div class="pe-eyebrow">État du dépôt</div>
      <div style="margin-top:var(--sp-2);font-size:var(--fs-ui-sm);font-weight:var(--fw-medium);color:var(--text-body)">
        ${r.coursComplets} module${r.coursComplets > 1 ? 's' : ''} complet${r.coursComplets > 1 ? 's' : ''} sur ${r.cours} ·
        ${r.coursPartiels} partiel${r.coursPartiels > 1 ? 's' : ''} · ${r.coursAVenir} à venir.
        ${r.ateliers} ateliers, ${r.ateliersEquipes} équipés.
        ${maj ? `Dernière production : ${esc(longDate(maj))}.` : ''}
      </div>
    </div>`;
  }

  /* ══════════ Rendu ══════════ */

  function rendre() {
    if (!etat.charge) return;
    document.querySelectorAll('#matVues [data-vue]').forEach((b) => {
      b.classList.toggle('btn--pri', b.dataset.vue === etat.vue);
      b.classList.toggle('btn--ghost', b.dataset.vue !== etat.vue);
    });
    $('matColonne').innerHTML =
      (etat.vue === 'semaine' ? rendreSemaine() : rendreCatalogue()) + rendreDepots();
    $('matAside').innerHTML = rendreAside();
  }

  /* ══════════ Actions ══════════ */

  /** Télécharge une archive. Le jeton voyage en en-tête, donc un simple lien
      ne suffit pas : on récupère le zip puis on déclenche l'enregistrement. */
  async function archive(id, portee, codes) {
    const params = new URLSearchParams({ activiteId: id, portee });
    if (codes && codes.length) params.set('codes', codes.join(','));
    confirmer('Archive en préparation…');
    try {
      const res = await ctx.api(`/api/materiel/archive?${params}`);
      const blob = await res.blob();
      const nom = (res.headers.get('Content-Disposition') || '')
        .match(/filename="([^"]+)"/)?.[1] || 'materiel.zip';
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url; a.download = nom;
      document.body.appendChild(a); a.click(); a.remove();
      setTimeout(() => URL.revokeObjectURL(url), 4000);
      confirmer(`Téléchargement démarré : ${nom} (${poids(blob.size)}).`);
    } catch (e) {
      confirmer(`Archive impossible : ${e.message}`);
    }
  }

  /** Imprime une ou plusieurs fiches. Les fiches sont déjà des documents
      imprimables, en noir et blanc, sans interface : on les charge dans le
      cadre isolé avec leurs propres styles, et on imprime le cadre. Rien de
      la page hôte n'y entre, donc aucun en-tête ne peut s'y glisser. */
  async function imprimer(chemins) {
    if (!chemins.length) return;
    confirmer(chemins.length === 1 ? 'Préparation de la fiche…'
      : `Préparation des ${chemins.length} fiches…`);
    try {
      const docs = await Promise.all(chemins.map(async (c) => {
        const html = await (await fetch(c)).text();
        return new DOMParser().parseFromString(html, 'text/html');
      }));
      // Toutes les fiches sortent du même générateur : leurs styles sont
      // identiques, ceux de la première suffisent pour la série entière.
      const tetes = [...docs[0].head.querySelectorAll('style, link[rel="stylesheet"]')]
        .map((n) => n.outerHTML).join('');
      const pages = docs.map((d, i) => `<div${i < docs.length - 1
        ? ' style="page-break-after:always"' : ''}>${d.body.innerHTML}</div>`).join('');

      const cadre = $('matImpression');
      const d = cadre.contentDocument;
      d.open();
      d.write(`<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">${tetes}
        <style>@page { size: letter; margin: 18mm 16mm; }</style>
        </head><body>${pages}</body></html>`);
      d.close();
      // Laisser la police et les styles s'appliquer avant d'ouvrir le dialogue.
      setTimeout(() => {
        cadre.contentWindow.focus();
        cadre.contentWindow.print();
        confirmer(chemins.length === 1 ? 'Fiche envoyée à l\'impression.'
          : `${chemins.length} fiches envoyées à l'impression, une par page.`);
      }, 400);
    } catch (e) {
      confirmer(`Impression impossible : ${e.message}`);
    }
  }

  function fichesChoisies() {
    return Object.keys(etat.sel).filter((k) => etat.sel[k]).map((k) => {
      const [id, code] = k.split(':');
      const s = seanceDe(porteur(Number(id)), code);
      return s && (s.fichiers.find((f) => f.type === 'fiche') || {}).chemin;
    }).filter(Boolean);
  }

  async function televerser(input, activiteId) {
    const fichier = input.files && input.files[0];
    if (!fichier) return;
    const corps = new FormData();
    corps.append('activiteId', activiteId);
    if (etat.detail && etat.detail.code) corps.append('seanceCode', etat.detail.code);
    corps.append('type', /\.pptx?$/i.test(fichier.name) ? 'presentation' : 'fiche');
    corps.append('note', '');
    corps.append('fichier', fichier);

    etat.televersement = { nom: fichier.name, pct: 0 };
    rendre();
    const avance = setInterval(() => {
      if (!etat.televersement) return;
      etat.televersement.pct = Math.min(90, etat.televersement.pct + 12);
      const barre = document.querySelector('.mat-barre > i');
      if (barre) barre.style.width = `${etat.televersement.pct}%`;
    }, 180);

    try {
      const d = await ctx.json('/api/materiel/depot', { method: 'POST', body: corps });
      etat.depots.push(d.depot);
      confirmer(`Téléversement terminé. Votre fichier est déposé à côté du fichier officiel${
        d.depot.seanceCode ? ' de la séance ' + d.depot.seanceCode : ''}.`);
    } catch (e) {
      confirmer(`Téléversement impossible : ${e.message}`);
    } finally {
      clearInterval(avance);
      etat.televersement = null;
      rendre();
    }
  }

  /** Recharge l'inventaire : la substitution se fait côté serveur, donc
      l'écran doit relire plutôt que deviner ce qui a changé. */
  async function relire() {
    const d = await ctx.json('/api/materiel');
    etat.inventaire = d.materiel;
    etat.depots = d.depots || [];
    etat.promotions = d.promotions || [];
    rendre();
  }

  async function promouvoir(depotId, fichierId) {
    try {
      await ctx.json('/api/materiel/promotion', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ depotId, fichierId }),
      });
      await relire();
      confirmer('Ce dépôt est maintenant servi à la place du fichier officiel. '
        + "L'officiel n'est pas effacé : il reste téléchargeable, et le geste se défait.");
    } catch (e) {
      confirmer(`Remplacement impossible : ${e.message}`);
    }
  }

  async function rendreOfficiel(fichierId) {
    try {
      await ctx.json(`/api/materiel/promotion/${encodeURIComponent(fichierId)}`,
        { method: 'DELETE' });
      await relire();
      confirmer('Retour au fichier officiel.');
    } catch (e) {
      confirmer(`Retour impossible : ${e.message}`);
    }
  }

  async function retirerDepot(id) {
    try {
      await ctx.json(`/api/materiel/depot/${encodeURIComponent(id)}`, { method: 'DELETE' });
      // Relire plutôt que retirer la rangée : si le dépôt était promu, le
      // serveur a aussi défait la promotion, et l'inventaire a changé.
      await relire();
      confirmer('Dépôt retiré.');
    } catch (e) {
      confirmer(`Retrait impossible : ${e.message}`);
    }
  }

  /* ══════════ Écoutes ══════════ */

  function brancher() {
    const racine = $('vueMateriel');

    racine.addEventListener('click', (e) => {
      const b = e.target.closest('[data-action], [data-vue]');
      if (!b) return;
      const id = Number(b.dataset.id);

      switch (b.dataset.action || (b.dataset.vue ? 'vue' : '')) {
        case 'vue':
          etat.vue = b.dataset.vue; rendre(); break;
        case 'deplier':
          etat.ouverts[id] = !etat.ouverts[id]; rendre(); break;
        case 'detail':
          etat.detail = { activiteId: id, code: b.dataset.code || null }; rendre(); break;
        case 'ouvrir-module': {
          // Depuis « Ma semaine » : ouvrir le module dans le catalogue, déplié.
          etat.vue = 'catalogue';
          etat.ouverts[id] = true;
          const p = porteur(id);
          const premiere = p && p.seances.find((s) => s.fichiers.length);
          if (premiere) etat.detail = { activiteId: id, code: premiere.code };
          rendre();
          break;
        }
        case 'fermer':
          etat.detail = null; rendre(); break;
        case 'archive': {
          // Trois provenances de codes : une séance nommée (« Prendre la
          // séance complète »), la sélection cochée (`data-sel`), ou aucune —
          // et l'archive prend alors tout le module.
          const codes = b.dataset.codes ? [b.dataset.codes]
            : (b.dataset.sel || b.dataset.portee === 'seances'
              ? Object.keys(etat.sel).filter((k) => etat.sel[k] && k.startsWith(`${id}:`))
                .map((k) => k.split(':')[1])
              : []);
          archive(id, b.dataset.portee, codes);
          break;
        }
        case 'imprimer':
          imprimer([b.dataset.chemin]); break;
        case 'imprimer-selection':
          imprimer(fichesChoisies()); break;
        case 'vider':
          etat.sel = {}; rendre(); break;
        case 'reinitialiser':
          etat.q = ''; etat.cat = ''; etat.niv = ''; etat.dom = ''; etat.typ = ''; etat.bloc = '';
          rendre(); break;
        case 'retirer-depot':
          retirerDepot(b.dataset.dep); break;
        case 'promouvoir':
          promouvoir(b.dataset.dep, b.dataset.fichier); break;
        case 'rendre-officiel':
          rendreOfficiel(b.dataset.fichier); break;
        default: break;
      }
    });

    racine.addEventListener('change', (e) => {
      const el = e.target;
      if (el.dataset.action === 'cocher') {
        etat.sel[el.dataset.cle] = el.checked;
        if (!el.checked) delete etat.sel[el.dataset.cle];
        rendre();
        return;
      }
      if (el.dataset.action === 'televerser') { televerser(el, Number(el.dataset.id)); return; }
      if (el.dataset.filtre) { etat[el.dataset.filtre] = el.value; rendre(); }
    });

    // La recherche se filtre à la frappe, sans redessiner la colonne à chaque
    // touche : on garde le curseur dans le champ.
    let attente;
    racine.addEventListener('input', (e) => {
      if (e.target.id !== 'matRecherche') return;
      etat.q = e.target.value;
      clearTimeout(attente);
      attente = setTimeout(() => {
        rendre();
        const champ = $('matRecherche');
        if (champ) { champ.focus(); champ.setSelectionRange(champ.value.length, champ.value.length); }
      }, 220);
    });
  }

  /* ══════════ Interface publique ══════════ */

  return {
    /** @param c {{ json, api, activites, groupe }} fourni par enseignant.js.
        `ouvrirPortail()` peut être rappelée (reconnexion après expiration) :
        les écoutes ne se posent qu'une fois, sinon chaque clic agirait deux
        fois. */
    init(c) {
      ctx = c;
      if (!branche) { brancher(); branche = true; }
    },

    /** Appelée à l'ouverture de l'onglet. Ne charge qu'une fois. */
    async afficher() {
      if (!etat.charge) {
        try { await charger(); } catch (e) {
          $('matColonne').innerHTML = `<div class="card"><div class="fb fb--no">Le dépôt n'a pas pu être chargé : ${esc(e.message)}</div></div>`;
          return;
        }
      }
      rendre();
    },

    /** Le groupe actif a changé : la semaine n'est plus la même, et le
        panneau de détail se ferme (décision de la remise). */
    changerGroupe() {
      etat.detail = null;
      etat.sel = {};
      if (etat.charge) rendre();
    },
  };
})();
