/* =========================================================================
   Session enseignante — partagée par catalogue.html, index.html et lms.html.

   Le portail est passé d'un enseignant unique à plusieurs enseignants ayant
   chacun un ou plusieurs groupes. Le catalogue d'activités reste commun ;
   ce qui appartient au groupe, c'est la planification (dates), les élèves,
   la progression et les productions orales. Toute requête d'administration
   porte donc deux choses : le jeton de session et le groupe actif.
   ========================================================================= */

const Prof = (() => {
  const TOKEN_KEY = 'prof_token';
  const GROUP_KEY = 'prof_groupe_actif';

  const state = {
    token: localStorage.getItem(TOKEN_KEY) || '',
    enseignant: null,
    groupes: [],
    groupeId: null,
  };

  const listeners = [];

  function setToken(token) {
    state.token = token || '';
    if (token) localStorage.setItem(TOKEN_KEY, token);
    else localStorage.removeItem(TOKEN_KEY);
  }

  function setGroupes(groupes) {
    state.groupes = groupes || [];
    const memorise = parseInt(localStorage.getItem(GROUP_KEY) || '', 10);
    const valide = state.groupes.some(g => g.id === memorise);
    state.groupeId = valide ? memorise : (state.groupes[0]?.id ?? null);
    if (state.groupeId) localStorage.setItem(GROUP_KEY, String(state.groupeId));
  }

  function setGroupeActif(id) {
    const gid = parseInt(id, 10);
    if (!state.groupes.some(g => g.id === gid)) return;
    state.groupeId = gid;
    localStorage.setItem(GROUP_KEY, String(gid));
    listeners.forEach(fn => fn(gid));
  }

  function onGroupeChange(fn) { listeners.push(fn); }

  function groupeActif() {
    return state.groupes.find(g => g.id === state.groupeId) || null;
  }

  /* --- Requêtes authentifiées ------------------------------------------ */

  async function fetchAuth(url, options = {}) {
    const opts = { ...options, headers: { ...(options.headers || {}) } };
    if (state.token) opts.headers['X-Prof-Token'] = state.token;
    const res = await fetch(url, opts);
    if (res.status === 401) {
      setToken('');
      versConnexion();
      throw new Error('Session expirée');
    }
    return res;
  }

  /** Ajoute ?groupId=… à une URL (le groupe actif par défaut). */
  function withGroup(url, groupId = state.groupeId) {
    const sep = url.includes('?') ? '&' : '?';
    return `${url}${sep}groupId=${encodeURIComponent(groupId ?? '')}`;
  }

  /** Insère groupId dans un corps JSON. */
  function body(obj = {}) {
    return JSON.stringify({ ...obj, groupId: state.groupeId });
  }

  function versConnexion() {
    const retour = location.pathname.split('/').pop() || 'index.html';
    location.href = `prof.html?retour=${encodeURIComponent(retour)}`;
  }

  /* --- Démarrage -------------------------------------------------------- */

  /**
   * À appeler au chargement d'une page enseignante. Redirige vers l'écran de
   * connexion si la session est absente ou expirée. Résout avec l'état une
   * fois l'enseignant et ses groupes connus.
   */
  async function init({ redirect = true } = {}) {
    let data;
    try {
      const res = await fetchAuth('/api/prof/me');
      data = await res.json();
    } catch {
      return null;
    }
    if (!data.connecte) {
      if (redirect) versConnexion();
      return null;
    }
    state.enseignant = data.enseignant;
    setGroupes(data.groupes);
    if (!state.groupes.length && redirect) {
      // Un enseignant sans groupe ne peut rien planifier : on l'envoie
      // directement créer son premier groupe. Les groupes vivent dans le
      // portail (onglet « Groupes et comptes ») ; `prof.html` ne porte plus
      // que les comptes.
      location.href = 'enseignant.html';
      return null;
    }
    return state;
  }

  async function logout() {
    try { await fetchAuth('/api/prof/logout', { method: 'POST' }); } catch {}
    setToken('');
    localStorage.removeItem(GROUP_KEY);
    location.href = 'prof.html';
  }

  /* --- Barre de groupe -------------------------------------------------- */

  const BAR_CSS = `
    .prof-bar {
      display: flex; align-items: center; gap: 12px; flex-wrap: wrap;
      font-family: inherit; font-size: 13px;
    }
    .prof-bar-group {
      display: flex; align-items: center; gap: 7px;
      background: rgba(59,111,246,.08); border: 1px solid rgba(59,111,246,.25);
      border-radius: 8px; padding: 5px 10px;
    }
    .prof-bar-label {
      font-size: 11px; font-weight: 700; letter-spacing: .4px;
      text-transform: uppercase; color: #3b6ff6;
    }
    .prof-bar select {
      border: none; background: transparent; font: inherit; font-weight: 600;
      color: inherit; cursor: pointer; max-width: 220px;
    }
    .prof-bar select:focus { outline: none; }
    .prof-bar-nom { color: inherit; opacity: .75; }
    .prof-bar a, .prof-bar button.prof-bar-link {
      background: none; border: none; padding: 0; font: inherit;
      color: inherit; opacity: .75; cursor: pointer; text-decoration: none;
    }
    .prof-bar a:hover, .prof-bar button.prof-bar-link:hover {
      opacity: 1; text-decoration: underline;
    }
  `;

  /**
   * Rend le sélecteur de groupe + le nom de l'enseignant dans `container`.
   * `onChange` est appelé quand l'enseignant bascule de groupe.
   */
  function renderBar(container, onChange) {
    if (!container) return;
    if (!document.getElementById('profBarCss')) {
      const style = document.createElement('style');
      style.id = 'profBarCss';
      style.textContent = BAR_CSS;
      document.head.appendChild(style);
    }
    const options = state.groupes
      .map(g => `<option value="${g.id}"${g.id === state.groupeId ? ' selected' : ''}>${escapeHtml(g.nom)}</option>`)
      .join('');
    container.innerHTML = `
      <div class="prof-bar">
        <div class="prof-bar-group">
          <span class="prof-bar-label">Groupe</span>
          <select id="profGroupeSelect" aria-label="Groupe actif">${options}</select>
        </div>
        <span class="prof-bar-nom">${escapeHtml(state.enseignant?.nom || '')}</span>
        <a href="prof.html">Comptes enseignants</a>
        <button type="button" class="prof-bar-link" id="profLogout">Déconnexion</button>
      </div>`;
    container.querySelector('#profGroupeSelect').addEventListener('change', e => {
      setGroupeActif(e.target.value);
      if (onChange) onChange(state.groupeId);
    });
    container.querySelector('#profLogout').addEventListener('click', logout);
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, c => (
      { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    ));
  }

  return {
    state, init, logout, fetch: fetchAuth, withGroup, body,
    setToken, setGroupes, setGroupeActif, onGroupeChange, groupeActif,
    renderBar, versConnexion,
    get groupeId() { return state.groupeId; },
  };
})();
