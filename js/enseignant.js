/* =========================================================================
   Portail enseignant — Planifier · Élèves · Groupes et comptes.

   Rendu selon la remise de design « Portail enseignant ». La page ne connaît
   que trois objets : le catalogue commun (avec les dates du groupe actif),
   les fichiers du groupe, et les élèves du groupe.

   La session (jeton + groupe actif) est partagée avec les autres pages
   enseignantes par les deux mêmes clés de localStorage que `js/prof.js`.
   Cette page ne passe pas par `Prof.fetch` parce qu'elle porte son propre
   écran de connexion : `Prof.fetch` renvoie vers `prof.html` sur un 401.
   ========================================================================= */

(() => {
  'use strict';

  const CLE_JETON = 'prof_token';
  const CLE_GROUPE = 'prof_groupe_actif';
  const JOUR = 86400000;
  const PAS = { meme: 0, jour: 1, semaine: 7, quinzaine: 14 };

  /* Les cinq compétences et les savoirs d'un module ne sont pas dans
     `activities.json` : ils décrivent le contenu pédagogique, pas le fichier.
     Ils vivent donc ici, en clair, une entrée par module de cours. */
  const DETAILS = {
    35: {
      temps: ['impératif présent', 'présent de l’indicatif'],
      savoirs: ['L’impératif des verbes en -er', 'La négation « ne… pas » à l’impératif', 'Les pronoms après l’impératif (allez-y)'],
      actes: ['Demander un renseignement', 'Conseiller un service', 'Situer un lieu'],
      lexique: '18 mots — les services de santé',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Message enregistré d’une clinique, deux écoutes' },
        { code: 'PO', libelle: 'Production orale', texte: 'Dire où aller selon un symptôme, 2 minutes' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Dépliant des services du CLSC' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Quatre conseils à l’impératif' },
      ],
    },
    36: {
      temps: ['passé composé', 'présent de l’indicatif'],
      savoirs: ['Le choix de l’auxiliaire avoir ou être', 'L’accord du participe passé avec être', 'La négation au passé composé'],
      actes: ['Raconter un incident', 'Alerter quelqu’un', 'Rassurer'],
      lexique: '20 mots — les accidents et les premiers soins',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Appel d’urgence au superviseur' },
        { code: 'PO', libelle: 'Production orale', texte: 'Raconter un accident survenu au travail' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Rapport d’incident rempli' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Rapport d’incident, cinq phrases' },
      ],
    },
    39: {
      temps: ['passé composé', 'présent de l’indicatif'],
      savoirs: ['Le passé composé des verbes pronominaux', 'La cause : parce que, à cause de', 'L’heure et la durée (15 h, une demi-heure)'],
      actes: ['S’excuser', 'Justifier un retard', 'Prévenir de son absence'],
      lexique: '16 mots — un retard, un congé, un remplacement',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Deux appels laissés à un superviseur' },
        { code: 'PO', libelle: 'Production orale', texte: 'Laisser un message d’absence' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Politique d’assiduité de l’employeur' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Courriel d’avis d’absence' },
      ],
    },
    40: {
      temps: ['impératif présent', 'futur proche'],
      savoirs: ['L’impératif à la 2e personne du pluriel', 'Les marqueurs de séquence : d’abord, ensuite, enfin', 'Il faut + infinitif'],
      actes: ['Expliquer une procédure', 'Demander une précision', 'Reformuler une consigne'],
      lexique: '22 mots — les consignes et l’équipement',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Consignes de sécurité données en réunion' },
        { code: 'PO', libelle: 'Production orale', texte: 'Expliquer une tâche à un collègue' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Procédure affichée à l’atelier' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Rédiger une procédure en cinq étapes' },
      ],
    },
    41: {
      temps: ['imparfait', 'passé composé'],
      savoirs: ['Imparfait ou passé composé : décor et événement', 'Les indicateurs de temps du récit', 'Le discours rapporté au présent'],
      actes: ['Rapporter une nouvelle', 'Réagir à une nouvelle', 'Donner son opinion'],
      lexique: '20 mots — l’actualité et les médias',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Bulletin de nouvelles à la radio' },
        { code: 'PO', libelle: 'Production orale', texte: 'Résumer une nouvelle entendue' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Article de journal court' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Résumé d’une nouvelle, six phrases' },
      ],
    },
    42: {
      temps: ['futur simple', 'futur proche'],
      savoirs: ['Le futur simple des verbes irréguliers', 'Si + présent, futur simple', 'Les adverbes de probabilité'],
      actes: ['Faire une prévision', 'Proposer une sortie', 'Se préparer à un imprévu'],
      lexique: '18 mots — la météo et les saisons',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Bulletin météo de fin de semaine' },
        { code: 'PO', libelle: 'Production orale', texte: 'Annoncer la météo de la semaine' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Avertissement d’Environnement Canada' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Message de planification, quatre phrases' },
      ],
    },
    43: {
      temps: ['présent de l’indicatif', 'impératif présent'],
      savoirs: ['Le comparatif et le superlatif', 'La place et l’accord de l’adjectif', 'La phrase exclamative'],
      actes: ['Vanter un produit', 'Comparer deux offres', 'Convaincre'],
      lexique: '20 mots — la publicité et les prix',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Deux publicités radio à comparer' },
        { code: 'PO', libelle: 'Production orale', texte: 'Présenter un produit en 90 secondes' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Annonce d’une circulaire' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Rédiger une publicité de cinq lignes' },
      ],
    },
    44: {
      temps: ['présent de l’indicatif'],
      savoirs: ['Les prépositions de lieu', 'L’accord des adjectifs de description', 'Les questions avec quel, quelle'],
      actes: ['Décrire un logement', 'Questionner un propriétaire', 'Comparer deux logements'],
      lexique: '24 mots — les pièces et l’équipement',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Visite guidée d’un appartement' },
        { code: 'PO', libelle: 'Production orale', texte: 'Décrire son logement actuel' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Annonce de location en ligne' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Courriel de questions au propriétaire' },
      ],
    },
    45: {
      temps: ['infinitif passé', 'conditionnel présent'],
      savoirs: ['Après avoir + participe passé', 'Les formules de politesse au conditionnel', 'Les pronoms compléments le, la, lui'],
      actes: ['Signaler un problème', 'Demander une réparation', 'Relancer poliment'],
      lexique: '20 mots — les réparations et l’entretien',
      competences: [
        { code: 'CO', libelle: 'Compréhension orale', texte: 'Appel au propriétaire pour un dégât d’eau' },
        { code: 'PO', libelle: 'Production orale', texte: 'Demander une réparation au téléphone' },
        { code: 'CE', libelle: 'Compréhension écrite', texte: 'Lettre de mise en demeure simplifiée' },
        { code: 'PE', libelle: 'Production écrite', texte: 'Courriel de demande de réparation' },
      ],
    },
  };

  /* ══════════ Outils ══════════ */

  const $ = (id) => document.getElementById(id);

  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => (
    { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  const iso = (d) => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
  const lire = (s) => { const [a, m, j] = String(s).split('-').map(Number); return new Date(a, m - 1, j); };
  const court = (s) => (s ? lire(s).toLocaleDateString('fr-CA', { weekday: 'short', day: 'numeric', month: 'short' }) : '');
  const aujourdhui = () => iso(new Date());
  const pluriel = (n, mot, suffixe = 's') => `${n} ${mot}${n > 1 ? suffixe : ''}`;
  const poids = (o) => (o >= 1000000
    ? `${(o / 1000000).toFixed(1).replace('.', ',')} Mo`
    : `${Math.max(1, Math.round(o / 1000))} ko`);
  const extension = (n) => { const p = String(n).split('.'); return p.length > 1 ? p.pop().toUpperCase() : 'FICHIER'; };

  /** Pastille d'état d'une activité ou d'un fichier : glyphe + mot, toujours. */
  function statut(dates) {
    const auj = aujourdhui();
    const ouverture = (dates && (dates.datePrevue || dates.ouverture)) || '';
    const fermeture = (dates && (dates.dateFin || dates.fermeture)) || '';
    if (!ouverture) return { cle: 'vide', glyphe: '—', texte: 'Sans date' };
    if (fermeture && fermeture < auj) return { cle: 'fermee', glyphe: '✕', texte: `Fermée ${court(fermeture)}` };
    if (ouverture <= auj) return { cle: 'offerte', glyphe: '✓', texte: `Ouverte ${court(ouverture)}` };
    return { cle: 'avenir', glyphe: '→', texte: `À venir ${court(ouverture)}` };
  }

  const libelleCocher = (n) => (n === 1 ? 'Cocher la ligne' : `Cocher les ${n} lignes`);

  const pastille = (st, texte) =>
    `<span class="pe-pastille pe-pastille--${st.cle}"><span aria-hidden="true">${st.glyphe}</span>${esc(texte || st.texte)}</span>`;

  /* ══════════ Session ══════════ */

  const session = {
    jeton: localStorage.getItem(CLE_JETON) || '',
    poser(jeton) {
      session.jeton = jeton || '';
      if (jeton) localStorage.setItem(CLE_JETON, jeton);
      else localStorage.removeItem(CLE_JETON);
    },
  };

  let expiree = false;

  async function api(url, options = {}) {
    const opts = { ...options, headers: { ...(options.headers || {}) } };
    if (session.jeton) opts.headers['X-Prof-Token'] = session.jeton;
    const res = await fetch(url, opts);
    if (res.status === 401) {
      session.poser('');
      if (!expiree) { expiree = true; montrerConnexion(); }
      throw new Error('Session expirée');
    }
    if (!res.ok) {
      let erreur = `HTTP ${res.status}`;
      try { erreur = (await res.json()).error || erreur; } catch { /* réponse non JSON */ }
      throw new Error(erreur);
    }
    return res;
  }

  const json = (url, options) => api(url, options).then((r) => r.json());

  const envoyer = (url, corps, methode = 'POST') => json(url, {
    method: methode,
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(corps),
  });

  /* ══════════ État ══════════ */

  const etat = {
    ecran: 'planif',
    enseignant: null,
    groupes: [],
    groupeId: null,
    activites: [],
    documents: [],
    eleves: [],
    progression: [],
    journal: [],
    enseignants: [],
    deplies: new Set(),
    selection: new Set(),
    recherche: '',
    filtre: 'tous',
    rythme: 'semaine',
    detail: null,
    sourceCopie: null,
    glisse: false,
  };

  const groupeActif = () => etat.groupes.find((g) => g.id === etat.groupeId) || null;

  let minuterie;
  function dire(texte) {
    clearTimeout(minuterie);
    const el = $('message');
    el.textContent = texte;
    el.hidden = false;
    minuterie = setTimeout(() => { el.hidden = true; }, 3200);
  }

  /* ══════════ Démarrage ══════════ */

  async function demarrer() {
    let data;
    try {
      data = await (await fetch('/api/prof/me', {
        headers: session.jeton ? { 'X-Prof-Token': session.jeton } : {},
      })).json();
    } catch {
      montrerConnexion('Le serveur est injoignable. Vérifiez qu’il est démarré.');
      return;
    }
    if (!data.connecte) {
      montrerConnexion('', data.installationRequise);
      return;
    }
    etat.enseignant = data.enseignant;
    poserGroupes(data.groupes);
    if (!etat.groupes.length) {
      // Un enseignant sans groupe ne peut rien planifier.
      etat.ecran = 'groupes';
    }
    ouvrirPortail();
  }

  function poserGroupes(groupes) {
    etat.groupes = groupes || [];
    const memorise = parseInt(localStorage.getItem(CLE_GROUPE) || '', 10);
    const valide = etat.groupes.some((g) => g.id === memorise);
    etat.groupeId = valide ? memorise : (etat.groupes[0] ? etat.groupes[0].id : null);
    if (etat.groupeId) localStorage.setItem(CLE_GROUPE, String(etat.groupeId));
  }

  function montrerConnexion(erreur = '', installationRequise = false) {
    $('portail').hidden = true;
    $('ecranConnexion').hidden = false;
    $('noteInstallation').hidden = !installationRequise;
    const boite = $('erreurConnexion');
    boite.textContent = erreur;
    boite.hidden = !erreur;
    $('courriel').focus();
  }

  async function ouvrirPortail() {
    expiree = false;
    $('ecranConnexion').hidden = true;
    $('portail').hidden = false;
    // Le dépôt de matériel ne connaît ni la session ni les groupes : il reçoit
    // ici les quatre choses dont il a besoin. Le jeton reste l'affaire de
    // cette page, qui porte son propre écran de connexion.
    Materiel.init({
      json,
      api,
      activites: () => etat.activites,
      groupe: groupeActif,
    });
    $('nomEnseignant').textContent = etat.enseignant.nom;
    $('initiales').textContent = etat.enseignant.nom.split(' ').map((m) => m[0]).join('').slice(0, 2).toUpperCase();
    $('carteEnseignants').hidden = etat.enseignant.role !== 'admin';
    // `/api/prof/me` renvoie les groupes bruts ; la liste dédiée y ajoute le
    // nombre d'élèves et le titulaire, affichés dans « Groupes et comptes ».
    try { poserGroupes(await json('/api/prof/groupes')); } catch { /* liste brute */ }
    rendreBandeGroupe();
    await chargerGroupe();
    montrerEcran(etat.ecran);
  }

  /** Recharge tout ce qui appartient au groupe actif. */
  async function chargerGroupe() {
    if (!etat.groupeId) {
      etat.activites = []; etat.documents = []; etat.eleves = [];
      etat.progression = []; etat.journal = [];
      rendreTout();
      return;
    }
    const g = `groupId=${encodeURIComponent(etat.groupeId)}`;
    try {
      const [activites, documents, eleves, progression, journal] = await Promise.all([
        json(`/api/activities?${g}`),
        json(`/api/prof/documents?${g}`),
        json(`/api/admin/students?${g}`),
        json(`/api/admin/progress?${g}`),
        json(`/api/admin/access-log?${g}`),
      ]);
      etat.activites = activites;
      etat.documents = documents;
      etat.eleves = eleves;
      etat.progression = progression;
      etat.journal = journal;
    } catch (e) {
      if (!expiree) dire(`Chargement impossible : ${e.message}`);
      return;
    }
    etat.selection.clear();
    Materiel.changerGroupe();
    rendreTout();
  }

  function rendreTout() {
    rendreBandeGroupe();
    rendreJour();
    rendreListe();
    rendreDocs();
    rendreBarre();
    rendreEleves();
    rendreGroupes();
  }

  /* ══════════ Bande de groupe ══════════ */

  function rendreBandeGroupe() {
    const groupe = groupeActif();
    $('selectGroupe').innerHTML = etat.groupes
      .map((g) => `<option value="${g.id}"${g.id === etat.groupeId ? ' selected' : ''}>${esc(g.nom)}</option>`)
      .join('') || '<option>Aucun groupe</option>';

    const nbEleves = etat.eleves.length;
    $('lienEleves').textContent = nbEleves === 0 ? 'Aucun élève inscrit'
      : nbEleves === 1 ? 'Voir l’élève' : `Voir les ${nbEleves} élèves`;
    const datees = etat.activites.filter((a) => a.datePrevue).length;
    $('resumeGroupe').textContent = groupe
      ? `${pluriel(nbEleves, 'élève')} · ${datees} activité${datees > 1 ? 's' : ''} planifiée${datees > 1 ? 's' : ''} sur ${etat.activites.length}`
      : 'Aucun groupe : créez-en un dans « Groupes et comptes ».';

    const lien = $('lienTeams');
    lien.hidden = !(groupe && groupe.teams);
    if (groupe && groupe.teams) lien.href = groupe.teams;
    $('boutonTeams').textContent = groupe && groupe.teams ? 'Modifier le lien' : 'Ajouter le lien Teams';
    $('boutonTeams').disabled = !groupe;
    $('boutonCopie').disabled = etat.groupes.length < 2;
  }

  /* ══════════ Écran Planifier ══════════ */

  function visibles() {
    const q = etat.recherche.trim().toLowerCase();
    return etat.activites.filter((a) => {
      if (etat.filtre !== 'tous' && (a.categorie || 'atelier') !== etat.filtre) return false;
      if (!q) return true;
      const foin = [a.title, a.domaineDeVie, (a.tempsVerbaux || []).join(' ')].join(' ').toLowerCase();
      return foin.includes(q);
    });
  }

  function rendreJour() {
    const dj = new Date();
    $('dateJour').textContent = dj.toLocaleDateString('fr-CA', { weekday: 'long', day: 'numeric', month: 'long' });
    $('anneeJour').textContent = String(dj.getFullYear());

    const compte = { offerte: 0, avenir: 0, fermee: 0, vide: 0 };
    etat.activites.forEach((a) => { compte[statut(a).cle] += 1; });
    const enParution = etat.documents.filter((d) => statut(d).cle === 'offerte').length;
    $('resumeJour').textContent =
      `${compte.offerte} activité${compte.offerte > 1 ? 's' : ''} ouverte${compte.offerte > 1 ? 's' : ''}`
      + ` · ${compte.avenir} à venir · ${enParution} fichier${enParution > 1 ? 's' : ''} en parution`;

    const auj = aujourdhui();
    const evts = [];
    etat.activites.forEach((a) => {
      if (a.datePrevue === auj) evts.push(['✓', 'var(--accent)', a.title, 'Ouvre aujourd’hui']);
      if (a.dateFin === auj) evts.push(['✕', 'var(--warn-ink)', a.title, 'Ferme aujourd’hui']);
      if (a.dateVue === auj) evts.push(['◆', 'var(--acier-600)', a.title, 'À voir en classe']);
    });
    etat.documents.forEach((d) => {
      if (d.ouverture === auj) evts.push(['✓', 'var(--accent)', d.nom, 'Fichier en parution']);
      if (d.fermeture === auj) evts.push(['✕', 'var(--warn-ink)', d.nom, 'Fichier retiré']);
    });
    $('programme').innerHTML = evts.length
      ? evts.map(([glyphe, couleur, titre, quoi]) => `
          <div class="pe-evt" style="--sec:${couleur}">
            <i aria-hidden="true">${glyphe}</i>
            <div><b>${esc(titre)}</b><span>${esc(quoi)}</span></div>
          </div>`).join('')
      : '<div class="pe-vide">Rien ne s’ouvre ni ne ferme aujourd’hui. Vos élèves continuent ce qui est déjà ouvert.</div>';

    const planifiees = compte.offerte + compte.avenir + compte.fermee;
    $('banniereNeuf').hidden = !(etat.groupeId && etat.activites.length && planifiees === 0);
  }

  function rendreListe() {
    const liste = visibles();
    $('titreListe').textContent = `${liste.length} activité${liste.length > 1 ? 's' : ''} du catalogue`;

    const cours = liste.filter((a) => a.categorie === 'cours' && DETAILS[a.id]);
    const toutDeplie = cours.length > 0 && cours.every((a) => etat.deplies.has(a.id));
    $('boutonDeploiTout').textContent = toutDeplie ? 'Replier les détails' : 'Déplier les détails';
    $('boutonDeploiTout').hidden = cours.length === 0;

    const toutesCochees = liste.length > 0 && liste.every((a) => etat.selection.has(a.id));
    $('boutonToutCocher').textContent = toutesCochees ? 'Tout décocher' : libelleCocher(liste.length);
    $('boutonToutCocher').hidden = liste.length === 0;

    if (!liste.length) {
      $('listeActivites').innerHTML =
        '<div class="card__row" style="padding:var(--sp-8);text-align:center;font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Aucune activité ne correspond à cette recherche.</div>';
      return;
    }

    $('listeActivites').innerHTML = liste.map((a) => {
      const st = statut(a);
      const estCours = a.categorie === 'cours';
      const infos = estCours ? DETAILS[a.id] : null;
      const deplie = etat.deplies.has(a.id);
      const temps = (a.tempsVerbaux && a.tempsVerbaux.length ? a.tempsVerbaux : (infos ? infos.temps : []));
      const meta = estCours
        ? `Cours · ${esc(a.domaineDeVie || 'domaine à préciser')}`
        : `Atelier · ${esc(a.domaineDeVie || 'domaine à préciser')} · ${esc(temps.join(', ') || '—')}`;

      const rangee = `
        <div class="card__row pe-rangee${etat.selection.has(a.id) ? ' is-checked' : ''}" data-id="${a.id}">
          ${infos
            ? `<button type="button" class="pe-chevron" data-deploi="${a.id}" aria-expanded="${deplie}"
                       aria-label="Détails de ${esc(a.title)}">${deplie ? '▾' : '▸'}</button>`
            : '<span style="width:44px;flex:none" aria-hidden="true"></span>'}
          <input type="checkbox" class="pe-case" data-coche="${a.id}"
                 ${etat.selection.has(a.id) ? 'checked' : ''} aria-label="${esc(a.title)}" />
          <div class="pe-rangee-txt">
            <div class="pe-rangee-titre">${esc(a.title)}</div>
            <div class="pe-rangee-meta">${meta}</div>
          </div>
          ${pastille(st)}
          <button type="button" class="btn btn--ghost btn--sm" data-dates="${a.id}">Dates</button>
        </div>`;

      if (!infos || !deplie) return rangee;

      return rangee + `
        <div class="card__row pe-infos">
          <div class="pe-infos-grille">
            <div>
              <h4>Temps de verbe</h4>
              <div class="pe-pilules">${temps.map((t) => `<span class="pe-pilule">${esc(t)}</span>`).join('')}</div>
              <h4>Vocabulaire</h4>
              <p>${esc(infos.lexique)}</p>
            </div>
            <div>
              <h4>Savoirs vus</h4>
              <ul>${infos.savoirs.map((s) => `<li>${esc(s)}</li>`).join('')}</ul>
              <h4>Actes de parole</h4>
              <ul>${infos.actes.map((s) => `<li>${esc(s)}</li>`).join('')}</ul>
            </div>
            <div>
              <h4>Compétences travaillées</h4>
              <div class="pe-comp">${infos.competences.map((c) => `
                <div><span class="pe-code" title="${esc(c.libelle)}">${esc(c.code)}</span><span>${esc(c.texte)}</span></div>`).join('')}
              </div>
            </div>
          </div>
        </div>`;
    }).join('');
  }

  /* — Barre d'action collante — */

  function datesCalculees() {
    const choisies = visibles().filter((a) => etat.selection.has(a.id));
    const pas = PAS[etat.rythme] ?? 7;
    const debut = $('dateDebut').value;
    if (!debut) return [];
    const base = lire(debut);
    const eviter = $('eviterFinDeSemaine').checked;
    return choisies.map((a, i) => {
      const d = new Date(base.getTime() + pas * i * JOUR);
      if (eviter && pas > 0) {
        if (d.getDay() === 6) d.setDate(d.getDate() + 2);
        else if (d.getDay() === 0) d.setDate(d.getDate() + 1);
      }
      return { id: a.id, titre: a.title, date: iso(d) };
    });
  }

  function rendreBarre() {
    const n = etat.selection.size;
    $('barreAction').hidden = n === 0;
    if (!n) return;
    $('libelleSelection').textContent = n > 1 ? `${n} activités cochées` : '1 activité cochée';
    const plan = datesCalculees();
    const cinq = plan.slice(0, 5);
    $('apercuPlan').innerHTML = cinq.length
      ? cinq.map((p) => `<div><em>${esc(p.titre)}</em><b>${esc(court(p.date))}</b></div>`).join('')
        + (plan.length > 5
          ? `<div style="font-size:var(--fs-ui-sm);font-weight:var(--fw-bold);color:var(--text-muted)">+ ${plan.length - 5} autres, jusqu’au ${esc(court(plan[plan.length - 1].date))}</div>`
          : '')
      : '<div style="font-size:var(--fs-ui-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Choisissez une date d’ouverture.</div>';
  }

  async function poserDates(plan, fermeture) {
    // Une requête à la fois : le serveur relit et réécrit schedule.json à
    // chaque appel, des écritures en parallèle se perdraient.
    let faites = 0;
    for (const p of plan) {
      await envoyer(`/api/activities/${p.id}/dates`, {
        groupId: etat.groupeId, datePrevue: p.date, dateFin: fermeture,
      });
      faites += 1;
    }
    return faites;
  }

  async function planifier() {
    const plan = datesCalculees();
    if (!plan.length) { dire('Choisissez une date d’ouverture.'); return; }
    const boutons = [$('boutonPlanifier'), $('boutonRetirerDates')];
    boutons.forEach((b) => { b.disabled = true; });
    try {
      const faites = await poserDates(plan, $('dateFin').value || '');
      dire(`${faites} activité${faites > 1 ? 's planifiées' : ' planifiée'}.`);
    } catch (e) {
      dire(`Interrompu : ${e.message}`);
    } finally {
      boutons.forEach((b) => { b.disabled = false; });
      await chargerGroupe();
    }
  }

  async function retirerDates() {
    const ids = visibles().filter((a) => etat.selection.has(a.id)).map((a) => a.id);
    if (!ids.length) return;
    if (!confirm(`Retirer les dates de ${ids.length} activité(s) ? Elles disparaîtront du portail des élèves de ce groupe.`)) return;
    const boutons = [$('boutonPlanifier'), $('boutonRetirerDates')];
    boutons.forEach((b) => { b.disabled = true; });
    try {
      await poserDates(ids.map((id) => ({ id, date: '' })), '');
      dire('Dates retirées : ces activités disparaissent du portail des élèves.');
    } catch (e) {
      dire(`Interrompu : ${e.message}`);
    } finally {
      boutons.forEach((b) => { b.disabled = false; });
      await chargerGroupe();
    }
  }

  /* — Fichiers du groupe — */

  function rendreDocs() {
    const enParution = etat.documents.filter((d) => statut(d).cle === 'offerte').length;
    $('resumeDocs').textContent = etat.documents.length
      ? `${pluriel(etat.documents.length, 'fichier')} · ${enParution} en parution`
      : 'Aucun fichier partagé pour l’instant';

    const rangees = etat.documents.map((doc) => {
      const st = statut(doc);
      const texte = st.cle === 'offerte' ? `En parution depuis le ${court(doc.ouverture)}`
        : st.cle === 'avenir' ? `Paraît le ${court(doc.ouverture)}`
          : st.cle === 'fermee' ? `Retiré le ${court(doc.fermeture)}`
            : 'Sans date';
      return `
        <div class="card__row pe-doc">
          <span class="pe-ext">${esc(extension(doc.nom))}</span>
          <div class="pe-doc-txt">
            <div class="pe-doc-nom"><a href="${esc(doc.fichier)}" target="_blank" rel="noopener">${esc(doc.nom)}</a></div>
            <div class="pe-doc-meta">${esc(poids(doc.taille))} · ${doc.fermeture ? `retiré le ${esc(court(doc.fermeture))}` : 'sans date de retrait'}</div>
          </div>
          <div class="pe-doc-dates">
            <div class="pe-doc-champ">
              <label class="field-label" for="pub-${doc.id}">Paraît le</label>
              <input id="pub-${doc.id}" class="field" type="date" value="${esc(doc.ouverture)}" data-doc="${doc.id}" data-champ="ouverture" />
            </div>
            <div class="pe-doc-champ">
              <label class="field-label" for="fin-${doc.id}">Retiré le (facultatif)</label>
              <input id="fin-${doc.id}" class="field" type="date" value="${esc(doc.fermeture)}" data-doc="${doc.id}" data-champ="fermeture" />
            </div>
            <div class="pe-doc-etat">
              ${pastille(st, texte)}
              <button type="button" class="btn btn--ghost btn--sm" data-retirer-doc="${doc.id}">Retirer</button>
            </div>
          </div>
        </div>`;
    }).join('');

    $('listeDocs').innerHTML = rangees + `
      <div class="card__row">
        <label class="pe-depot${etat.glisse ? ' is-glisse' : ''}" id="zoneDepot">
          <input type="file" multiple id="champFichiers" />
          <b>Glissez un fichier ici ou cliquez pour le choisir</b>
          <span>Il paraît dès aujourd’hui ; ajustez la période juste à côté.</span>
        </label>
        ${etat.documents.length ? '' : `
        <div style="margin-top:var(--sp-3);font-size:var(--fs-ui);font-weight:var(--fw-semi);color:var(--text-muted)">
          Notes de cours, grilles d’évaluation, corrigés : l’élève voit le fichier seulement pendant sa période de parution.
        </div>`}
      </div>`;
  }

  async function televerser(fichiers) {
    const liste = Array.from(fichiers || []).filter(Boolean);
    if (!liste.length) return;
    try {
      for (const f of liste) {
        const forme = new FormData();
        forme.append('groupId', String(etat.groupeId));
        forme.append('fichier', f);
        await api('/api/prof/documents', { method: 'POST', body: forme });
      }
      dire(liste.length > 1
        ? `${liste.length} fichiers ajoutés, en parution dès aujourd’hui.`
        : `« ${liste[0].name} » ajouté, en parution dès aujourd’hui.`);
    } catch (e) {
      dire(`Téléversement impossible : ${e.message}`);
    }
    etat.glisse = false;
    await chargerGroupe();
  }

  /* ══════════ Écran Élèves ══════════ */

  function rendreEleves() {
    const offertes = etat.activites.filter((a) => statut(a).cle === 'offerte');
    const offertesIds = new Set(offertes.map((a) => a.id));
    const groupe = groupeActif();
    $('bandeEleveGroupe').textContent = groupe ? groupe.nom : '';
    $('titreEleves').textContent = `${pluriel(etat.eleves.length, 'élève')} inscrit${etat.eleves.length > 1 ? 's' : ''}`;

    if (!etat.eleves.length) {
      $('listeEleves').innerHTML =
        '<div class="card__row" style="padding:var(--sp-8);text-align:center;font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Aucun élève inscrit à ce groupe pour l’instant.</div>';
      return;
    }

    $('listeEleves').innerHTML = etat.eleves.map((el) => {
      const traces = etat.progression.filter((p) => p.studentId === el.id);
      const faites = new Set(traces
        .filter((p) => p.event === 'exercise_completed' && offertesIds.has(p.activityId))
        .map((p) => p.activityId)).size;
      const derniere = traces.slice().sort((a, b) => String(b.timestamp).localeCompare(String(a.timestamp)))[0];
      const visites = etat.journal.filter((j) => j.studentId === el.id)
        .map((j) => j.timestamp).sort();
      const derniereVisite = visites.length ? visites[visites.length - 1] : '';
      return `
        <div class="card__row pe-rangee">
          <div class="pe-rangee-txt">
            <div class="pe-rangee-titre" style="font-size:var(--fs-body-sm)">${esc(el.label || 'Élève')}</div>
            <div class="pe-rangee-meta">code ${esc(el.code)} · ${esc(depuis(derniereVisite))} · dernière étape : ${esc(derniere ? derniere.activityTitle || '—' : '—')}</div>
          </div>
          <span class="score">${faites} / ${offertes.length} offertes</span>
        </div>`;
    }).join('');
  }

  /** « vu aujourd'hui » / « vu hier » / « vu il y a N jours ». */
  function depuis(horodatage) {
    if (!horodatage) return 'jamais venu';
    const jour = String(horodatage).slice(0, 10);
    const ecart = Math.round((lire(aujourdhui()) - lire(jour)) / JOUR);
    if (ecart <= 0) return 'vu aujourd’hui';
    if (ecart === 1) return 'vu hier';
    return `vu il y a ${ecart} jours`;
  }

  /* ══════════ Écran Groupes et comptes ══════════ */

  function rendreGroupes() {
    $('listeGroupes').innerHTML = etat.groupes.map((g) => `
      <div class="card__row pe-rangee">
        <div class="pe-rangee-txt">
          <button type="button" class="pe-lien" style="color:var(--text-accent)" data-voir-groupe="${g.id}">${esc(g.nom)}</button>
          <div class="pe-rangee-meta">${pluriel(g.nbEleves || 0, 'élève')} · ${esc(g.titulaire || 'sans titulaire')} · ${g.teams ? 'rencontre Teams liée' : 'aucun lien Teams'}</div>
        </div>
        <button type="button" class="btn btn--ghost btn--sm" data-activer-groupe="${g.id}">Planifier ce groupe</button>
        <button type="button" class="btn btn--ghost btn--sm" data-renommer-groupe="${g.id}">Renommer</button>
      </div>`).join('')
      || '<div class="card__row" style="font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Aucun groupe pour l’instant. Créez-en un ci-dessous.</div>';

    if (etat.enseignant.role !== 'admin') return;
    $('listeEnseignants').innerHTML = etat.enseignants.map((e) => `
      <div class="card__row pe-rangee">
        <div class="pe-rangee-txt">
          <div class="pe-rangee-titre" style="font-size:var(--fs-body-sm)">${esc(e.nom)}</div>
          <div class="pe-rangee-meta">${esc(e.courriel)} · ${pluriel(e.nbGroupes || 0, 'groupe')}</div>
        </div>
        <span class="pe-pastille ${e.role === 'admin' ? 'pe-pastille--offerte' : 'pe-pastille--vide'}">${e.role === 'admin' ? 'Administrateur' : 'Enseignant'}</span>
        <button type="button" class="btn btn--ghost btn--sm" data-reinit="${e.id}">Réinitialiser le mot de passe</button>
      </div>`).join('');
  }

  async function chargerEnseignants() {
    if (!etat.enseignant || etat.enseignant.role !== 'admin') return;
    try {
      etat.enseignants = await json('/api/prof/enseignants');
      rendreGroupes();
    } catch { /* un enseignant non administrateur n'a pas cette liste */ }
  }

  /* ══════════ Aperçu élève ══════════ */

  function rendreApercu() {
    const groupe = groupeActif();
    const ouvertes = etat.activites.filter((a) => statut(a).cle === 'offerte');
    $('apercuTitre').textContent = `Aperçu élève · ${groupe ? groupe.nom : ''}`;
    $('apercuResume').textContent = ouvertes.length
      ? `${pluriel(ouvertes.length, 'activité')} visible${ouvertes.length > 1 ? 's' : ''} aujourd’hui`
      : 'Rien de visible aujourd’hui';
    $('apercuTeams').hidden = !(groupe && groupe.teams);

    $('apercuActivites').innerHTML = ouvertes.length
      ? ouvertes.map((a) => {
        const estCours = a.categorie === 'cours';
        return `
          <div class="pe-apercu-act">
            <div class="pe-eyebrow">${estCours ? 'Cours' : 'Atelier'}</div>
            <div style="margin-top:2px;font-size:var(--fs-body);font-weight:var(--fw-black);color:var(--text-strong)">${esc(a.title)}</div>
            <div style="margin-top:2px;font-size:var(--fs-ui);font-weight:var(--fw-semi);color:var(--ink-500)">${esc(a.domaineDeVie || '')}</div>
            ${a.dateFin ? `<div style="margin-top:var(--sp-2);font-size:var(--fs-ui);font-weight:var(--fw-bold);color:var(--text-muted)">À terminer avant le ${esc(court(a.dateFin))}</div>` : ''}
          </div>`;
      }).join('')
      : `<div style="background:var(--surface-card);border:1px solid var(--border);border-radius:var(--r-md);padding:var(--sp-8);text-align:center;font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">
           L’élève ouvre son portail et ne voit aucune activité. Donnez une date d’ouverture à au moins une activité.
         </div>`;

    const parution = etat.documents.filter((d) => statut(d).cle === 'offerte');
    $('apercuDocs').innerHTML = parution.length
      ? parution.map((d) => `
          <div class="pe-apercu-doc">
            <span class="pe-ext">${esc(extension(d.nom))}</span>
            <span style="font-size:var(--fs-ui);font-weight:var(--fw-bold);color:var(--text-strong)">${esc(d.nom)}</span>
          </div>`).join('')
      : '<div style="font-size:var(--fs-ui);font-weight:var(--fw-semi);color:var(--text-muted)">Aucun document en parution aujourd’hui.</div>';
  }

  /* ══════════ Navigation ══════════ */

  function montrerEcran(nom) {
    etat.ecran = nom;
    $('vuePlanif').hidden = nom !== 'planif';
    $('vueEleves').hidden = nom !== 'eleves';
    $('vueGroupes').hidden = nom !== 'groupes';
    $('vueMateriel').hidden = nom !== 'materiel';
    document.querySelectorAll('.pe-onglet').forEach((b) => {
      if (b.dataset.ecran === nom) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    if (nom === 'groupes') chargerEnseignants();
    // Le dépôt se charge à la première ouverture de l'onglet, pas au
    // démarrage : la plupart des visites au portail ne le touchent pas.
    if (nom === 'materiel') Materiel.afficher();
    window.scrollTo({ top: 0 });
  }

  function ouvrirModale(id) { $(id).hidden = false; }
  function fermerModale(id) { $(id).hidden = true; }

  /* ══════════ Écoutes ══════════ */

  // — Connexion —
  $('formConnexion').addEventListener('submit', async (e) => {
    e.preventDefault();
    const bouton = $('boutonConnexion');
    bouton.disabled = true;
    try {
      const res = await fetch('/api/prof/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          courriel: $('courriel').value.trim(),
          motDePasse: $('motDePasse').value,
        }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || 'Connexion impossible');
      session.poser(data.token);
      etat.enseignant = data.enseignant;
      poserGroupes(data.groupes);
      $('motDePasse').value = '';
      $('erreurConnexion').hidden = true;
      etat.ecran = etat.groupes.length ? 'planif' : 'groupes';
      await ouvrirPortail();
    } catch (err) {
      const boite = $('erreurConnexion');
      boite.textContent = err.message;
      boite.hidden = false;
    } finally {
      bouton.disabled = false;
    }
  });

  $('boutonDeconnexion').addEventListener('click', async () => {
    try { await api('/api/prof/logout', { method: 'POST' }); } catch { /* jeton déjà mort */ }
    session.poser('');
    localStorage.removeItem(CLE_GROUPE);
    location.reload();
  });

  // — Navigation et groupe actif —
  document.addEventListener('click', (e) => {
    const onglet = e.target.closest('[data-ecran]');
    if (onglet) { montrerEcran(onglet.dataset.ecran); return; }
    const fermer = e.target.closest('[data-fermer]');
    if (fermer) { fermerModale(fermer.dataset.fermer); }
  });

  document.querySelectorAll('.pe-modale').forEach((modale) => {
    modale.addEventListener('click', (e) => { if (e.target === modale) modale.hidden = true; });
  });
  document.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    document.querySelectorAll('.pe-modale').forEach((m) => { m.hidden = true; });
  });

  $('selectGroupe').addEventListener('change', async (e) => {
    const id = parseInt(e.target.value, 10);
    if (!etat.groupes.some((g) => g.id === id)) return;
    etat.groupeId = id;
    localStorage.setItem(CLE_GROUPE, String(id));
    await chargerGroupe();
  });

  $('lienEleves').addEventListener('click', () => montrerEcran('eleves'));

  // — Recherche et filtres —
  $('recherche').addEventListener('input', (e) => {
    etat.recherche = e.target.value;
    rendreListe();
    rendreBarre();
  });

  $('filtres').addEventListener('click', (e) => {
    const bouton = e.target.closest('[data-filtre]');
    if (!bouton) return;
    etat.filtre = bouton.dataset.filtre;
    document.querySelectorAll('#filtres .choice').forEach((b) => {
      b.classList.toggle('is-selected', b.dataset.filtre === etat.filtre);
    });
    rendreListe();
    rendreBarre();
  });

  $('rythmes').addEventListener('click', (e) => {
    const bouton = e.target.closest('[data-rythme]');
    if (!bouton) return;
    etat.rythme = bouton.dataset.rythme;
    document.querySelectorAll('#rythmes .choice').forEach((b) => {
      b.classList.toggle('is-selected', b.dataset.rythme === etat.rythme);
    });
    rendreBarre();
  });

  // — Liste d'activités —
  $('listeActivites').addEventListener('change', (e) => {
    const case_ = e.target.closest('[data-coche]');
    if (!case_) return;
    const id = Number(case_.dataset.coche);
    if (case_.checked) etat.selection.add(id); else etat.selection.delete(id);
    case_.closest('.pe-rangee').classList.toggle('is-checked', case_.checked);
    const liste = visibles();
    const toutes = liste.length > 0 && liste.every((a) => etat.selection.has(a.id));
    $('boutonToutCocher').textContent = toutes ? 'Tout décocher' : libelleCocher(liste.length);
    rendreBarre();
  });

  $('listeActivites').addEventListener('click', (e) => {
    const chevron = e.target.closest('[data-deploi]');
    if (chevron) {
      const id = Number(chevron.dataset.deploi);
      if (etat.deplies.has(id)) etat.deplies.delete(id); else etat.deplies.add(id);
      rendreListe();
      return;
    }
    const dates = e.target.closest('[data-dates]');
    if (dates) ouvrirDates(Number(dates.dataset.dates));
  });

  $('boutonDeploiTout').addEventListener('click', () => {
    const cours = visibles().filter((a) => a.categorie === 'cours' && DETAILS[a.id]);
    const toutDeplie = cours.length > 0 && cours.every((a) => etat.deplies.has(a.id));
    if (toutDeplie) cours.forEach((a) => etat.deplies.delete(a.id));
    else cours.forEach((a) => etat.deplies.add(a.id));
    rendreListe();
  });

  $('boutonToutCocher').addEventListener('click', () => {
    const liste = visibles();
    const toutes = liste.length > 0 && liste.every((a) => etat.selection.has(a.id));
    if (toutes) liste.forEach((a) => etat.selection.delete(a.id));
    else liste.forEach((a) => etat.selection.add(a.id));
    rendreListe();
    rendreBarre();
  });

  $('boutonDecocher').addEventListener('click', () => {
    etat.selection.clear();
    rendreListe();
    rendreBarre();
  });

  ['dateDebut', 'dateFin', 'eviterFinDeSemaine'].forEach((id) => {
    $(id).addEventListener('change', rendreBarre);
  });
  $('boutonPlanifier').addEventListener('click', planifier);
  $('boutonRetirerDates').addEventListener('click', retirerDates);

  // — Modale « Dates » —
  function ouvrirDates(id) {
    const a = etat.activites.find((x) => x.id === id);
    if (!a) return;
    etat.detail = id;
    $('detailPortee').textContent = `${groupeActif() ? groupeActif().nom : ''} · ${a.categorie === 'cours' ? 'Module' : 'Atelier'}`;
    $('detailTitre').textContent = a.title;
    $('dOuverture').value = a.datePrevue || '';
    $('dFermeture').value = a.dateFin || '';
    $('dVue').value = a.dateVue || '';
    $('dLien').value = a.lien || '';
    ouvrirModale('modaleDates');
  }

  $('formDates').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      await envoyer(`/api/activities/${etat.detail}/dates`, {
        groupId: etat.groupeId,
        datePrevue: $('dOuverture').value,
        dateFin: $('dFermeture').value,
        dateVue: $('dVue').value,
        lien: $('dLien').value,
      });
      fermerModale('modaleDates');
      dire('Dates enregistrées.');
      await chargerGroupe();
    } catch (err) {
      dire(`Enregistrement impossible : ${err.message}`);
    }
  });

  // — Fichiers —
  $('listeDocs').addEventListener('change', async (e) => {
    const champ = e.target.closest('[data-doc]');
    if (champ) {
      try {
        await envoyer(`/api/prof/documents/${champ.dataset.doc}`,
          { [champ.dataset.champ]: champ.value }, 'PATCH');
        await chargerGroupe();
      } catch (err) {
        dire(`Enregistrement impossible : ${err.message}`);
      }
      return;
    }
    if (e.target.id === 'champFichiers') {
      await televerser(e.target.files);
    }
  });

  $('listeDocs').addEventListener('click', async (e) => {
    const bouton = e.target.closest('[data-retirer-doc]');
    if (!bouton) return;
    if (!confirm('Retirer ce fichier du groupe ? Les élèves ne le verront plus.')) return;
    try {
      await api(`/api/prof/documents/${bouton.dataset.retirerDoc}`, { method: 'DELETE' });
      dire('Fichier retiré du groupe.');
      await chargerGroupe();
    } catch (err) {
      dire(`Suppression impossible : ${err.message}`);
    }
  });

  ['dragover', 'dragenter'].forEach((type) => {
    $('listeDocs').addEventListener(type, (e) => {
      if (!e.target.closest('.pe-depot')) return;
      e.preventDefault();
      if (!etat.glisse) { etat.glisse = true; document.querySelector('.pe-depot').classList.add('is-glisse'); }
    });
  });
  $('listeDocs').addEventListener('dragleave', (e) => {
    if (!e.target.closest('.pe-depot')) return;
    e.preventDefault();
    etat.glisse = false;
    document.querySelector('.pe-depot').classList.remove('is-glisse');
  });
  $('listeDocs').addEventListener('drop', async (e) => {
    if (!e.target.closest('.pe-depot')) return;
    e.preventDefault();
    await televerser(e.dataTransfer && e.dataTransfer.files);
  });

  // — Lien Teams —
  function ouvrirTeams() {
    const groupe = groupeActif();
    if (!groupe) return;
    $('teamsGroupe').textContent = groupe.nom;
    $('champTeams').value = groupe.teams || '';
    ouvrirModale('modaleTeams');
  }
  $('boutonTeams').addEventListener('click', ouvrirTeams);

  async function enregistrerTeams(lien) {
    try {
      await envoyer(`/api/prof/groupes/${etat.groupeId}`, { teams: lien }, 'PATCH');
      const groupe = groupeActif();
      if (groupe) groupe.teams = lien;
      fermerModale('modaleTeams');
      rendreBandeGroupe();
      rendreGroupes();
      dire(lien ? 'Lien Teams enregistré : les élèves du groupe le voient maintenant.' : 'Lien Teams retiré.');
    } catch (err) {
      dire(`Enregistrement impossible : ${err.message}`);
    }
  }

  $('formTeams').addEventListener('submit', (e) => {
    e.preventDefault();
    enregistrerTeams($('champTeams').value.trim());
  });
  $('boutonRetirerTeams').addEventListener('click', () => enregistrerTeams(''));

  // — Copier une planification —
  function ouvrirCopie() {
    const autres = etat.groupes.filter((g) => g.id !== etat.groupeId);
    if (!autres.length) { dire('Il faut un deuxième groupe pour copier une planification.'); return; }
    etat.sourceCopie = autres[0].id;
    const groupe = groupeActif();
    $('copieTexte').innerHTML =
      `Reprend les dates d’un autre groupe pour <strong>${esc(groupe ? groupe.nom : '')}</strong>. Les dates déjà posées sur ce groupe sont remplacées ; vous pourrez ensuite ajuster activité par activité.`;
    rendreSources();
    ouvrirModale('modaleCopie');
  }

  function rendreSources() {
    const autres = etat.groupes.filter((g) => g.id !== etat.groupeId);
    $('listeSources').innerHTML = autres.map((g) => `
      <label class="pe-radio${g.id === etat.sourceCopie ? ' is-choisi' : ''}">
        <input type="radio" name="sourceCopie" value="${g.id}"${g.id === etat.sourceCopie ? ' checked' : ''} />
        <span>${esc(g.nom)}</span>
        <span>${pluriel(g.nbEleves || 0, 'élève')}</span>
      </label>`).join('');
  }

  $('boutonCopie').addEventListener('click', ouvrirCopie);
  $('boutonCopie2').addEventListener('click', ouvrirCopie);
  $('listeSources').addEventListener('change', (e) => {
    etat.sourceCopie = Number(e.target.value);
    rendreSources();
  });

  $('formCopie').addEventListener('submit', async (e) => {
    e.preventDefault();
    try {
      const res = await envoyer('/api/prof/planification/copier', {
        groupId: etat.groupeId,
        sourceGroupId: etat.sourceCopie,
        decalage: Number($('decalage').value) || 0,
      });
      fermerModale('modaleCopie');
      const dec = Number($('decalage').value) || 0;
      dire(res.copiees
        ? `${res.copiees} dates copiées${dec ? `, décalées de ${dec} jours` : ''}.`
        : 'Ce groupe n’a aucune date à copier.');
      await chargerGroupe();
    } catch (err) {
      dire(`Copie impossible : ${err.message}`);
    }
  });

  // — Aperçu élève —
  $('boutonApercu').addEventListener('click', () => {
    rendreApercu();
    ouvrirModale('modaleApercu');
  });

  // — Groupes et comptes —
  $('formGroupe').addEventListener('submit', async (e) => {
    e.preventDefault();
    const nom = $('nouveauGroupe').value.trim();
    if (!nom) return;
    try {
      const res = await envoyer('/api/prof/groupes', { nom });
      $('nouveauGroupe').value = '';
      etat.groupes = await json('/api/prof/groupes');
      etat.groupeId = res.groupe.id;
      localStorage.setItem(CLE_GROUPE, String(etat.groupeId));
      dire('Groupe créé. Il part vide : donnez-lui ses premières dates.');
      await chargerGroupe();
      montrerEcran('planif');
    } catch (err) {
      dire(`Création impossible : ${err.message}`);
    }
  });

  $('listeGroupes').addEventListener('click', async (e) => {
    const voir = e.target.closest('[data-voir-groupe]');
    const activer = e.target.closest('[data-activer-groupe]');
    const renommer = e.target.closest('[data-renommer-groupe]');
    if (voir || activer) {
      const id = Number((voir || activer).dataset.voirGroupe || (voir || activer).dataset.activerGroupe);
      etat.groupeId = id;
      localStorage.setItem(CLE_GROUPE, String(id));
      await chargerGroupe();
      montrerEcran(voir ? 'eleves' : 'planif');
      return;
    }
    if (renommer) {
      const id = Number(renommer.dataset.renommerGroupe);
      const groupe = etat.groupes.find((g) => g.id === id);
      const nom = prompt('Nouveau nom du groupe', groupe ? groupe.nom : '');
      if (!nom || !nom.trim()) return;
      try {
        await envoyer(`/api/prof/groupes/${id}`, { nom: nom.trim() }, 'PATCH');
        etat.groupes = await json('/api/prof/groupes');
        rendreBandeGroupe();
        rendreGroupes();
        dire('Groupe renommé.');
      } catch (err) {
        dire(`Renommage impossible : ${err.message}`);
      }
    }
  });

  $('listeEnseignants').addEventListener('click', async (e) => {
    const bouton = e.target.closest('[data-reinit]');
    if (!bouton) return;
    const mot = prompt('Mot de passe provisoire (8 caractères ou plus)');
    if (!mot) return;
    try {
      await envoyer(`/api/prof/enseignants/${bouton.dataset.reinit}`, { motDePasse: mot }, 'PATCH');
      dire('Mot de passe réinitialisé. Communiquez-le à la personne concernée.');
    } catch (err) {
      dire(`Réinitialisation impossible : ${err.message}`);
    }
  });

  /* ══════════ Amorçage ══════════ */

  $('dateDebut').value = aujourdhui();
  document.querySelector('#filtres [data-filtre="tous"]').classList.add('is-selected');
  document.querySelector('#rythmes [data-rythme="semaine"]').classList.add('is-selected');
  demarrer();
})();
