/* =========================================
   Bibliothèque d'activités pédagogiques
   Application principale
   ========================================= */

const CONFIG = {
  ITEMS_PER_PAGE: 60,   // 6 colonnes × 10 rangées
  SKELETON_COUNT: 12,   // cartes fantômes au chargement
  DATA_PATH: 'data/activities.json',
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

/* =========================================
   CHARGEMENT DES DONNÉES
   ========================================= */
async function loadActivities() {
  showSkeletons();

  try {
    const response = await fetch(CONFIG.DATA_PATH);
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    state.activities = await response.json();
  } catch (err) {
    console.warn('Impossible de charger activities.json, utilisation des données de démonstration.', err);
    state.activities = getDemoActivities();
  }

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
function render() {
  const start = (state.currentPage - 1) * CONFIG.ITEMS_PER_PAGE;
  const pageItems = state.filtered.slice(start, start + CONFIG.ITEMS_PER_PAGE);

  // État vide
  if (state.filtered.length === 0) {
    DOM.grid.innerHTML = '';
    DOM.emptyState.classList.add('visible');
    DOM.pagination.classList.add('hidden');
    return;
  }

  DOM.emptyState.classList.remove('visible');
  DOM.grid.innerHTML = pageItems.map(buildCard).join('');
  attachDateEvents();
  renderPagination();
}

/* =========================================
   CONSTRUCTION D'UNE CARTE
   ========================================= */
const CARD_PALETTE = [
  { card: 'linear-gradient(90deg,#3b6ff6,#7c3aed)', thumb: 'linear-gradient(135deg,#dbeafe 0%,#ede9fe 100%)', icon: '#6d85f0' },
  { card: 'linear-gradient(90deg,#0ea5e9,#06b6d4)', thumb: 'linear-gradient(135deg,#e0f2fe 0%,#cffafe 100%)', icon: '#22b8d4' },
  { card: 'linear-gradient(90deg,#10b981,#059669)', thumb: 'linear-gradient(135deg,#d1fae5 0%,#a7f3d0 100%)', icon: '#10b981' },
  { card: 'linear-gradient(90deg,#f59e0b,#ef4444)', thumb: 'linear-gradient(135deg,#fef3c7 0%,#fee2e2 100%)', icon: '#f59e0b' },
  { card: 'linear-gradient(90deg,#ec4899,#a855f7)', thumb: 'linear-gradient(135deg,#fce7f3 0%,#f3e8ff 100%)', icon: '#e879b4' },
  { card: 'linear-gradient(90deg,#f97316,#eab308)', thumb: 'linear-gradient(135deg,#ffedd5 0%,#fef9c3 100%)', icon: '#f97316' },
  { card: 'linear-gradient(90deg,#6366f1,#0ea5e9)', thumb: 'linear-gradient(135deg,#e0e7ff 0%,#e0f2fe 100%)', icon: '#6366f1' },
  { card: 'linear-gradient(90deg,#14b8a6,#3b82f6)', thumb: 'linear-gradient(135deg,#ccfbf1 0%,#dbeafe 100%)', icon: '#14b8a6' },
];

function buildCard(activity) {
  const palette = CARD_PALETTE[(activity.id - 1) % CARD_PALETTE.length];
  const thumb = activity.thumbnail
    ? `<img src="${escHtml(activity.thumbnail)}" alt="${escHtml(activity.title)}"
            loading="lazy" onerror="this.style.display='none';this.nextElementSibling.style.display='flex'">`
    : '';

  const placeholder = `
    <div class="card-thumbnail-placeholder"
         style="${activity.thumbnail ? 'display:none;' : ''}background:${palette.thumb};color:${palette.icon}">
      ${iconImage()}
    </div>`;

  return `
    <article class="card" data-id="${activity.id}" style="--card-color:${palette.card}">
      <div class="card-thumbnail">
        ${thumb}
        ${placeholder}
      </div>
      <div class="card-body">
        <div class="card-meta">
          <h2 class="card-title">${escHtml(activity.title)}</h2>
          <span class="card-badge">${escHtml(activity.level || 'Niveau 4')}</span>
        </div>
        <div class="card-dates">
          <div class="card-date-field vue ${activity.dateVue ? 'filled' : ''}">
            <span class="card-date-label vue">Vue</span>
            <input type="date" class="card-date-input"
                   value="${escHtml(activity.dateVue || '')}"
                   data-id="${activity.id}" data-field="dateVue"
                   title="Date vue" />
          </div>
          <div class="card-date-field prevue ${activity.datePrevue ? 'filled' : ''}">
            <span class="card-date-label prevue">Prévue</span>
            <input type="date" class="card-date-input"
                   value="${escHtml(activity.datePrevue || '')}"
                   data-id="${activity.id}" data-field="datePrevue"
                   title="Date prévue" />
          </div>
        </div>
        <div class="card-actions">
          <a href="${escHtml(encodePath(activity.interactive))}"
             class="btn btn-primary"
             target="_blank" rel="noopener"
             onclick="trackOpen('interactive', '${escHtml(activity.title)}')">
            <span class="btn-icon">${iconPlay()}</span>
            Activité interactive
          </a>
          <a href="${escHtml(encodePath(activity.studentDoc))}"
             class="btn btn-secondary"
             target="_blank" rel="noopener"
             onclick="trackOpen('document', '${escHtml(activity.title)}')">
            <span class="btn-icon">${iconDoc()}</span>
            Document élève
          </a>
          ${activity.slideshow
            ? `<a href="${escHtml(encodePath(activity.slideshow))}"
                 class="btn btn-slideshow"
                 target="_blank" rel="noopener"
                 onclick="trackOpen('slideshow', '${escHtml(activity.title)}')">
                <span class="btn-icon">${iconSlideshow()}</span>
                Diaporama photos
               </a>`
            : `<button class="btn btn-slideshow btn-disabled" disabled title="Aucun diaporama disponible">
                <span class="btn-icon">${iconSlideshow()}</span>
                Diaporama photos
               </button>`
          }
        </div>
      </div>
    </article>`;
}

/* =========================================
   SAUVEGARDE DES DATES
   ========================================= */
function attachDateEvents() {
  document.querySelectorAll('.card-date-input').forEach(input => {
    input.addEventListener('change', async () => {
      const id = input.dataset.id;
      const field = input.dataset.field;
      const value = input.value;

      input.closest('.card-date-field').classList.toggle('filled', !!value);

      try {
        await fetch(`/api/activities/${id}/dates`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ [field]: value }),
        });
      } catch {
        // En mode statique (Netlify), la sauvegarde n'est pas disponible
      }
    });
  });
}

/* =========================================
   SQUELETTES DE CHARGEMENT
   ========================================= */
function showSkeletons() {
  DOM.grid.innerHTML = Array.from({ length: CONFIG.SKELETON_COUNT }, () => `
    <div class="card card-skeleton">
      <div class="card-thumbnail">
        <div class="skeleton skel-thumb"></div>
      </div>
      <div class="skeleton skel-title"></div>
      <div class="skeleton skel-title-2"></div>
      <div class="skeleton skel-btn"></div>
      <div class="skeleton skel-btn-2"></div>
    </div>`).join('');
}

/* =========================================
   PAGINATION
   ========================================= */
function renderPagination() {
  const totalPages = Math.ceil(state.filtered.length / CONFIG.ITEMS_PER_PAGE);

  if (totalPages <= 1) {
    DOM.pagination.classList.add('hidden');
    return;
  }

  DOM.pagination.classList.remove('hidden');
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
    <button class="page-btn" id="prevBtn" ${p === 1 ? 'disabled' : ''} aria-label="Page précédente">
      ${iconChevronLeft()} Préc.
    </button>
    ${pages.map(pg =>
      pg === '…'
        ? `<span class="page-ellipsis">…</span>`
        : `<button class="page-btn ${pg === p ? 'active' : ''}"
                   data-page="${pg}" aria-label="Page ${pg}" ${pg === p ? 'aria-current="page"' : ''}>${pg}</button>`
    ).join('')}
    <button class="page-btn" id="nextBtn" ${p === totalPages ? 'disabled' : ''} aria-label="Page suivante">
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
  toast.className = 'toast';
  toast.innerHTML = `<span class="toast-icon">${icon}</span>${escHtml(message)}`;
  DOM.toastContainer.appendChild(toast);

  requestAnimationFrame(() => {
    requestAnimationFrame(() => toast.classList.add('show'));
  });

  setTimeout(() => {
    toast.classList.remove('show');
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
function iconSlideshow() {
  return `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="2" y="3" width="20" height="14" rx="2"></rect>
    <line x1="8" y1="21" x2="16" y2="21"></line>
    <line x1="12" y1="17" x2="12" y2="21"></line></svg>`;
}
function iconImage() {
  return `<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
    <rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect>
    <circle cx="8.5" cy="8.5" r="1.5"></circle>
    <polyline points="21 15 16 10 5 21"></polyline></svg>`;
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
  document.querySelector('.search-icon').innerHTML = iconSearch();
  document.querySelector('.search-clear').innerHTML = iconX();
  document.querySelector('.empty-state-icon').innerHTML = iconEmpty();

  // Événements recherche
  DOM.searchInput.addEventListener('input', e => {
    const q = e.target.value;
    DOM.searchClear.classList.toggle('visible', q.length > 0);
    applySearch(q);
  });

  DOM.searchClear.addEventListener('click', () => {
    DOM.searchInput.value = '';
    DOM.searchClear.classList.remove('visible');
    applySearch('');
    DOM.searchInput.focus();
  });

  DOM.searchInput.addEventListener('keydown', e => {
    if (e.key === 'Escape') {
      DOM.searchInput.value = '';
      DOM.searchClear.classList.remove('visible');
      applySearch('');
    }
  });

  // Charger les activités
  loadActivities();
}

document.addEventListener('DOMContentLoaded', init);
