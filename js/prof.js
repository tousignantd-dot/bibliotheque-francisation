/* =========================================================================
   Session enseignante — partagée par catalogue.html, enseignant.html et lms.html.

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
    // Le mode séance est-il ouvert à ce compte ? Décidé par la direction,
    // remonté par `/api/prof/me`. Vrai par défaut : c'est le réglage hérité.
    seanceAutorisee: true,
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

  /** Le niveau du groupe actif, sous la forme « Niveau N ».

      Un groupe est d'un niveau, et ce niveau borne ce que l'enseignante voit
      du catalogue et du dépôt de matériel : on ne planifie pas un module de
      niveau 7 dans une classe de niveau 4. Le serveur écrit toujours le
      champ ; le repli sur le nom sert aux pages ouvertes avant qu'il ne
      réponde, et à un jeu de données plus ancien. */
  function niveauGroupe(groupe = groupeActif()) {
    const pose = ((groupe || {}).niveau || '').trim();
    if (/^Niveau [1-8]$/.test(pose)) return pose;
    const trouve = /niveau\s*([1-8])/i.exec((groupe || {}).nom || '');
    // Vide quand on ne sait pas, jamais « Niveau 4 ».
    //
    // Le repli inventait un niveau, et ce niveau **bornait** : le catalogue,
    // le dépôt de matériel, les menus de modules. Un groupe sans niveau
    // enregistré et dont le nom n'en porte pas — `testN5`, par exemple — se
    // voyait offrir le niveau 4 en silence, et le catalogue lui affirmait
    // « Niveau 4 — les activités de votre groupe ». Le portail énonçait comme
    // un fait ce qu'il venait de deviner.
    //
    // Chaque écran qui borne doit donc traiter la chaîne vide comme « ne
    // borne pas » : on montre tout. C'est la bonne façon d'échouer — un
    // enseignant qui voit trop le remarque et corrige son groupe ; un
    // enseignant qui voit trop peu croit que le catalogue est pauvre.
    return trouve ? `Niveau ${trouve[1]}` : '';
  }

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
    const retour = location.pathname.split('/').pop() || 'enseignant.html';
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
    // La direction autorise, l'enseignant choisit. Le drapeau voyage déjà dans
    // cette réponse ; il était jeté, et chaque écran qui en avait besoin
    // redemandait `/api/prof/me`. On le garde ici, une fois.
    state.seanceAutorisee = data.seanceAutorisee !== false;
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
    setToken, setGroupes, setGroupeActif, onGroupeChange, groupeActif, niveauGroupe,
    renderBar, versConnexion,
    get groupeId() { return state.groupeId; },
  };
})();
