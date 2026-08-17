/* =========================================
   Bibliothèque d'activités pédagogiques
   Application principale
   ========================================= */

const CONFIG = {
  ITEMS_PER_PAGE: 60,   // 6 colonnes × 10 rangées
  SKELETON_COUNT: 12,   // cartes fantômes au chargement
  // Les dates viennent de la planification du groupe actif, pas du fichier
  // statique : c'est l'API qui les superpose au catalogue commun.
  DATA_PATH: '/api/activities',
};

/* ---- État de l'application ---- */
const state = {
  activities: [],
  filtered: [],
  currentPage: 1,
  searchQuery: '',
};

/* ---- Références DOM ---- */
const DOM = {
  grid: document.getElementById('grid'),
  searchInput: document.getElementById('searchInput'),
  searchClear: document.getElementById('searchClear'),
  counter: document.getElementById('counter'),
  counterTotal: document.getElementById('counterTotal'),
  pagination: document.getElementById('pagination'),
  emptyState: document.getElementById('emptyState'),
  toastContainer: document.getElementById('toastContainer'),
};

function formatDate(iso) {
  if (!iso) return '';
  const [y, m, d] = iso.split('-');
  return `${d}/${m}/${y}`;
}

/* =========================================
   CHARGEMENT DES DONNÉES
   ========================================= */
async function loadActivities() {
  showSkeletons();

  try {
    const response = await Prof.fetch(Prof.withGroup(CONFIG.DATA_PATH));
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.activities = await response.json();
  } catch (err) {
    console.warn('Impossible de charger activities.json, utilisation des données de démonstration.', err);
    state.activities = getDemoActivities();
  }

  // Le badge de niveau ne se justifie que si le catalogue en mêle plusieurs :
  // répété à l'identique sur chaque carte, il ne fait que voler de la largeur
  // au titre, que l'en-tête de page annonce déjà.
  state.plusieursNiveaux =
    new Set(state.activities.map(a => a.level || 'Niveau 4')).size > 1;

  state.filtered = sortActivities([...state.activities]);
  updateCounter();
  render();
}

/* =========================================
   TRI
   ========================================= */
function sortActivities(list) {
  const FAR = '9999-99-99';
  return list.sort((a, b) => {
    const aHasPrevue = !!a.datePrevue;
    const bHasPrevue = !!b.datePrevue;
    const aHasVue   = !!a.dateVue && !a.datePrevue;
    const bHasVue   = !!b.dateVue && !b.datePrevue;

    // Groupe 1 : datePrevue définie
    // Groupe 2 : dateVue définie (sans datePrevue)
    // Groupe 3 : aucune date
    const groupA = aHasPrevue ? 0 : aHasVue ? 1 : 2;
    const groupB = bHasPrevue ? 0 : bHasVue ? 1 : 2;

    if (groupA !== groupB) return groupA - groupB;

    if (groupA === 0) return (a.datePrevue || FAR).localeCompare(b.datePrevue || FAR);
    if (groupA === 1) return (a.dateVue || FAR).localeCompare(b.dateVue || FAR);
    return 0;
  });
}

/* =========================================
   RENDU PRINCIPAL
   ========================================= */
// La couleur de section sert AU REPÉRAGE, jamais à décorer : une teinte par
// bloc, portée par `--sec` / `--sec-soft` et reprise par le filet gauche des
// cartes (`.card--marked`), la pastille de niveau et le compte.
const SECTIONS = [
  {
    cle: 'cours', titre: 'Cours', sousTitre: '4 h — le matin',
    sec: 'var(--green-600)', secSoft: 'var(--green-100)',
  },
  {
    cle: 'atelier', titre: 'Ateliers', sousTitre: '2 h — l’après-midi',
    sec: 'var(--acier-600)', secSoft: 'var(--acier-100)',
  },
];

function render() {
  const start = (state.currentPage - 1) * CONFIG.ITEMS_PER_PAGE;
  const pageItems = state.filtered.slice(start, start + CONFIG.ITEMS_PER_PAGE);

  // État vide
  if (state.filtered.length === 0) {
    DOM.grid.innerHTML = '';
    DOM.emptyState.hidden = false;
    DOM.pagination.hidden = true;
    return;
  }

  DOM.emptyState.hidden = true;

  // Deux blocs distincts : les cours (modules de 4 h, le matin) puis les
  // ateliers (activités de 2 h, l'après-midi).
  DOM.grid.innerHTML = SECTIONS.map(section => {
    const lot = pageItems.filter(a => (a.categorie || 'atelier') === section.cle);
    if (!lot.length) return '';
    return `
      <section class="bib-section" style="--sec:${section.sec};--sec-soft:${section.secSoft}">
        <div class="exo__head">
          <span class="exo__eyebrow">${section.titre}</span>
          <span class="exo__rule"></span>
          <span class="exo__score">${lot.length}</span>
        </div>
        <p class="exo__sub">${section.sousTitre}</p>
        <div class="grid-auto">${lot.map(buildCard).join('')}</div>
      </section>`;
  }).join('');

  renderPagination();
}

/* =========================================
   CONSTRUCTION D'UNE CARTE
   ========================================= */
function buildCard(activity) {
  // Sans image, pas de vignette : un cadre vide de 132 px n'apprend rien et
  // allonge la carte d'autant. Le filet gauche de la carte suffit au repérage.
  const vignette = activity.thumbnail
    ? `<div class="bib-vignette">
         <img src="${escHtml(activity.thumbnail)}" alt=""
              loading="lazy" onerror="this.parentElement.remove()">
       </div>`
    : '';

  // Le champ « slideshow » porte soit un .pptx de photos (activités 4 à 15),
  // soit une page HTML qui regroupe plusieurs présentations (module 9).
  // Le libellé du bouton suit ce qu'il y a au bout du lien.
  const slideshowLabel = /\.html?$/i.test(activity.slideshow || '')
    ? 'Présentations'
    : 'Diaporama photos';

  // Un lien secondaire n'est écrit que si le fichier existe : un bouton mort
  // n'apprend rien. C'est admin.html qui sert à voir ce qui manque.
  const lien = (chemin, libelle, icone, type) => chemin
    ? `<a href="${escHtml(encodePath(chemin))}"
          class="btn btn--sm btn--ghost"
          target="_blank" rel="noopener"
          onclick="trackOpen('${type}', '${escHtml(activity.title)}')">
         ${icone}${libelle}
       </a>`
    : '';

  return `
    <article class="card card--marked bib-carte" data-id="${activity.id}">
      ${vignette}
      <div class="bib-carte-haut">
        <h3 class="bib-carte-titre">${escHtml(activity.title)}</h3>
        ${state.plusieursNiveaux
          ? `<span class="bib-badge">${escHtml(activity.level || 'Niveau 4')}</span>`
          : ''
        }
      </div>
      ${(activity.dateVue || activity.datePrevue) ? `
      <div class="bib-dates">
        ${activity.dateVue
          ? `<span class="bib-date bib-date--vue">✓ Vue <b>${escHtml(formatDate(activity.dateVue))}</b></span>`
          : ''}
        ${activity.datePrevue
          ? `<span class="bib-date bib-date--prevue">→ Prévue <b>${escHtml(formatDate(activity.datePrevue))}</b></span>`
          : ''}
      </div>` : ''}
      <div class="bib-actions">
        <a href="${escHtml(encodePath(activity.interactive))}"
           class="btn btn--sm btn--pri"
           target="_blank" rel="noopener"
           ${activity.parcours ? 'title="Le module complet, en une seule page"' : ''}
           onclick="trackOpen('interactive', '${escHtml(activity.title)}')">
          ${iconPlay()}${activity.parcours ? 'Module' : 'Activité interactive'}
        </a>
        ${activity.parcours
          ? `<a href="${escHtml(encodePath(activity.parcours))}"
               class="btn btn--sm btn--ghost"
               target="_blank" rel="noopener"
               title="Le même contenu, une diapositive à la fois"
               onclick="trackOpen('parcours', '${escHtml(activity.title)}')">
              ${iconParcours()}Parcours
             </a>`
          : ''}
        ${lien(activity.studentDoc, 'Document élève', iconDoc(), 'document')}
        ${lien(activity.slideshow, slideshowLabel, iconSlideshow(), 'slideshow')}
        ${lien(activity.planCours, 'Plan de cours', iconPlan(), 'planCours')}
        ${lien(activity.autres, 'Autres', iconDoc(), 'autres')}
      </div>
    </article>`;
}

/* =========================================
   SQUELETTES DE CHARGEMENT
   ========================================= */
function showSkeletons() {
  DOM.emptyState.hidden = true;
  DOM.pagination.hidden = true;
  DOM.grid.innerHTML = '<div class="grid-auto">' + Array.from({ length: CONFIG.SKELETON_COUNT }, () => `
    <div class="card bib-squelette" aria-hidden="true">
      <div class="bib-os bib-os--titre"></div>
      <div class="bib-os bib-os--ligne"></div>
      <div class="bib-os bib-os--btn"></div>
    </div>`).join('') + '</div>';
}

/* =========================================
   PAGINATION
   ========================================= */
function renderPagination() {
  const totalPages = Math.ceil(state.filtered.length / CONFIG.ITEMS_PER_PAGE);

  if (totalPages <= 1) {
    DOM.pagination.hidden = true;
    return;
  }

  DOM.pagination.hidden = false;
  const p = state.currentPage;

  let pages = [];

  if (totalPages <= 7) {
    pages = Array.from({ length: totalPages }, (_, i) => i + 1);
  } else {
    pages = [1];
    if (p > 3) pages.push('…');
    for (let i = Math.max(2, p - 1); i <= Math.min(totalPages - 1, p + 1); i++) pages.push(i);
    if (p < totalPages - 2) pages.push('…');
    pages.push(totalPages);
  }

  DOM.pagination.innerHTML = `
    <button type="button" class="btn btn--sm btn--ghost" id="prevBtn"
            ${p === 1 ? 'disabled' : ''} aria-label="Page précédente">
      ${iconChevronLeft()} Préc.
    </button>
    ${pages.map(pg =>
      pg === '…'
        ? `<span class="bib-points">…</span>`
        : `<button type="button" class="btn btn--sm ${pg === p ? 'btn--pri' : 'btn--ghost'}"
                   data-page="${pg}" aria-label="Page ${pg}" ${pg === p ? 'aria-current="page"' : ''}>${pg}</button>`
    ).join('')}
    <button type="button" class="btn btn--sm btn--ghost" id="nextBtn"
            ${p === totalPages ? 'disabled' : ''} aria-label="Page suivante">
      Suiv. ${iconChevronRight()}
    </button>`;

  document.getElementById('prevBtn').addEventListener('click', () => goToPage(p - 1));
  document.getElementById('nextBtn').addEventListener('click', () => goToPage(p + 1));
  DOM.pagination.querySelectorAll('[data-page]').forEach(btn => {
    btn.addEventListener('click', () => goToPage(Number(btn.dataset.page)));
  });
}

function goToPage(page) {
  state.currentPage = page;
  render();
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

/* =========================================
   RECHERCHE
   ========================================= */
function applySearch(query) {
  state.searchQuery = query.trim().toLowerCase();
  state.currentPage = 1;

  if (!state.searchQuery) {
    state.filtered = sortActivities([...state.activities]);
  } else {
    state.filtered = sortActivities(state.activities.filter(a =>
      a.title.toLowerCase().includes(state.searchQuery) ||
      (a.keywords || []).some(k => k.toLowerCase().includes(state.searchQuery))
    ));
  }

  updateCounter();
  render();
}

/* =========================================
   COMPTEUR
   ========================================= */
function updateCounter() {
  const total = state.activities.length;
  const visible = state.filtered.length;
  DOM.counterTotal.textContent = total;

  if (state.searchQuery && visible !== total) {
    DOM.counter.innerHTML = `<span>${visible}</span> résultat${visible !== 1 ? 's' : ''} sur <span>${total}</span> activité${total !== 1 ? 's' : ''}`;
  } else {
    DOM.counter.innerHTML = `<span>${total}</span> activité${total !== 1 ? 's' : ''}`;
  }
}

/* =========================================
   TOAST
   ========================================= */
function showToast(message, icon = iconCheck()) {
  const toast = document.createElement('div');
  toast.className = 'bib-gazouillis-item';
  toast.innerHTML = `${icon}${escHtml(message)}`;
  DOM.toastContainer.appendChild(toast);

  requestAnimationFrame(() => {
    requestAnimationFrame(() => toast.classList.add('is-visible'));
  });

  setTimeout(() => {
    toast.classList.remove('is-visible');
    setTimeout(() => toast.remove(), 250);
  }, 2800);
}

/* =========================================
   TRACKING (ouverture de fichier)
   ========================================= */
function trackOpen(type, title) {
  const label = type === 'interactive' ? 'Activité interactive' : 'Document élève';
  showToast(`Ouverture — ${title}`);
}

/* =========================================
   ICÔNES SVG
   ========================================= */
function iconPlay() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <polygon points="5 3 19 12 5 21 5 3"></polygon></svg>`;
}
function iconDoc() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
    <polyline points="14 2 14 8 20 8"></polyline></svg>`;
}
function iconPlan() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path>
    <path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>`;
}
function iconSlideshow() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="2" y="3" width="20" height="14" rx="2"></rect>
    <line x1="8" y1="21" x2="16" y2="21"></line>
    <line x1="12" y1="17" x2="12" y2="21"></line></svg>`;
}
// Parcours guidé : une diapositive au premier plan, les suivantes derrière.
function iconParcours() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="5" width="13" height="14" rx="2"></rect>
    <path d="M19 8v8"></path>
    <path d="M9 10l3 2-3 2"></path></svg>`;
}
function iconSearch() {
  return `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>`;
}
function iconX() {
  return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
}
function iconCheck() {
  return `<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="20 6 9 17 4 12"></polyline></svg>`;
}
function iconEmpty() {
  return `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line>
    <line x1="8" y1="11" x2="14" y2="11"></line></svg>`;
}
function iconChevronLeft() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="15 18 9 12 15 6"></polyline></svg>`;
}
function iconChevronRight() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <polyline points="9 18 15 12 9 6"></polyline></svg>`;
}

/* =========================================
   UTILITAIRES
   ========================================= */
function encodePath(path) {
  if (!path) return '';
  return path.split('/').map(segment => encodeURIComponent(segment)).join('/');
}

function escHtml(str) {
  return String(str ?? '')
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

/* =========================================
   DONNÉES DE DÉMONSTRATION
   (utilisées si activities.json est absent)
   ========================================= */
function getDemoActivities() {
  const titles = [
    "Le Vieux-Port de Montréal",
    "Le marché Jean-Talon",
    "La poutine — culture québécoise",
    "Les transports en commun",
    "Le système de santé au Québec",
    "Chercher un logement",
    "Au bureau de poste",
    "La météo et les saisons",
    "Les fêtes québécoises",
    "Faire ses courses au supermarché",
    "Les droits et responsabilités",
    "Le réseau scolaire québécois",
  ];
  return titles.map((title, i) => ({
    id: i + 1,
    title,
    level: "Niveau 4",
    thumbnail: "",
    interactive: `assets/interactive/activite-${i + 1}/index.html`,
    studentDoc: `assets/documents/activite-${i + 1}.pdf`,
    slideshow: ``,
    keywords: [],
  }));
}

/* =========================================
   INITIALISATION
   ========================================= */
function init() {
  // Injecter icônes statiques
  document.getElementById('iconeLoupe').innerHTML = iconSearch();
  document.getElementById('searchClear').innerHTML = iconX();
  document.getElementById('iconeVide').innerHTML = iconEmpty();

  // Événements recherche
  DOM.searchInput.addEventListener('input', e => {
    const q = e.target.value;
    DOM.searchClear.classList.toggle('is-visible', q.length > 0);
    applySearch(q);
  });

  DOM.searchClear.addEventListener('click', () => {
    DOM.searchInput.value = '';
    DOM.searchClear.classList.remove('is-visible');
    applySearch('');
    DOM.searchInput.focus();
  });

  DOM.searchInput.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      DOM.searchInput.value = '';
      DOM.searchClear.classList.remove('is-visible');
      applySearch('');
    }
  });

  // Charger les activités
  loadActivities();
}

/* =========================================
   BARRE DE GROUPE

   La page rend elle-même le sélecteur plutôt que d'appeler `Prof.renderBar` :
   celle-ci injecte sa propre feuille de style, avec des bleus codés en dur qui
   n'appartiennent pas au système de design. `admin.html` et `lms.html`
   continuent de l'utiliser telle quelle — rien n'y change.
   ========================================= */
function renderBandeGroupe() {
  const select = document.getElementById('selectGroupe');
  select.innerHTML = Prof.state.groupes
    .map(g => `<option value="${g.id}"${g.id === Prof.groupeId ? ' selected' : ''}>${escHtml(g.nom)}</option>`)
    .join('');
  select.addEventListener('change', e => {
    Prof.setGroupeActif(e.target.value);
    loadActivities();
  });

  const nom = Prof.state.enseignant?.nom || '';
  document.getElementById('nomEnseignant').textContent = nom;
  document.getElementById('initiales').textContent =
    nom.split(' ').map(m => m[0]).join('').slice(0, 2).toUpperCase();
  document.getElementById('boutonDeconnexion').addEventListener('click', Prof.logout);
}

document.addEventListener('DOMContentLoaded', async () => {
  // Sans session enseignante, Prof.init() redirige vers prof.html.
  if (!await Prof.init()) return;
  renderBandeGroupe();
  init();
});
