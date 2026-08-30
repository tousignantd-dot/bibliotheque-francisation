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

  /* — Sections d'un module —
     Une ligne de planification est soit un module (« 35 »), soit une de ses
     sections (« 35:t1 »). La clé sert de jeton de sélection et de rangée dans
     l'aperçu des dates : une seule liste ordonnée, donc un seul rythme. */

  const cle = (activiteId, sectionId) =>
    (sectionId ? `${activiteId}:${sectionId}` : String(activiteId));

  /** [{id, titre, chapeau, dates}] pour une activité, [] si elle n'est pas
      découpée — un atelier d'une seule page se planifie d'un bloc. */
  function sectionsDe(activiteId) {
    const entree = etat.sections[String(activiteId)];
    if (!entree) return [];
    return (entree.sections || []).map((s) => ({
      ...s, dates: (entree.dates || {})[s.id] || {},
    }));
  }

  /** Une rangée se déplie si elle a des sections à planifier ou des détails
      pédagogiques à montrer — le chevron ne promet jamais du vide. */
  const deployable = (a) => Boolean(DETAILS[a.id] || sectionsDe(a.id).length);

  /** L'état d'une section : sans date propre, elle suit son module. C'est ce
      qui laisse les modules déjà planifiés s'ouvrir en entier comme avant. */
  function statutSection(activite, section) {
    if (!section.dates.datePrevue) {
      const st = statut(activite);
      return st.cle === 'vide'
        ? st
        : { cle: st.cle, glyphe: st.glyphe, texte: `Suit le module · ${st.texte.toLowerCase()}` };
    }
    return statut(section.dates);
  }

  /* Ce que l'état veut dire du côté de l'élève. La pastille porte un mot et
     une date ; ce qu'elle ne peut pas écrire, c'est ce que l'élève voit — et
     c'est la seule chose qu'on cherche à savoir en la regardant. */
  const INFO_ETAT = {
    vide: "Aucune date posée : la ligne n'est pas encore au programme et l'élève ne la voit pas dans son portail.",
    offerte: "L'élève la voit dans son portail et peut y entrer dès maintenant.",
    fermee: "La date de fin est passée : l'élève ne peut plus y entrer, mais ce qu'il a fait reste enregistré.",
    avenir: "La date d'ouverture n'est pas arrivée : l'élève ne la voit pas encore.",
  };

  const pastille = (st, texte) =>
    `<span class="pe-pastille pe-pastille--${st.cle}" tabindex="0" data-info="${esc(INFO_ETAT[st.cle] || '')}"><span aria-hidden="true">${st.glyphe}</span>${esc(texte || st.texte)}</span>`;

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
    // Les élèves créés depuis le dernier chargement, surlignés le temps que
    // l'enseignante note ou imprime leurs codes.
    elevesNeufs: new Set(),
    progression: [],
    journal: [],
    corrigeMoi: [],
    enseignants: [],
    // Le découpage des modules et les dates de section du groupe, tel que
    // `/api/sections` le renvoie : {activiteId: {sections, dates}}.
    sections: {},
    deplies: new Set(),
    // Les lignes cochées, module et sections mêlés. Une clé de section s'écrit
    // « 35:t1 » — une seule liste, donc un seul rythme de dates à appliquer.
    selection: new Set(),
    recherche: '',
    filtre: 'tous',
    rythme: 'semaine',
    detail: null,
    detailSection: '',
    sourceCopie: null,
    glisse: false,
  };

  const groupeActif = () => etat.groupes.find((g) => g.id === etat.groupeId) || null;

  /* Le niveau du groupe, sous la forme « Niveau N ». C'est lui qui borne le
     catalogue et le dépôt de matériel : on ne planifie pas un module de
     niveau 7 dans une classe de niveau 4. Le serveur écrit toujours le champ ;
     le repli sur le nom sert aux groupes créés avant qu'on le demande. */
  const NIVEAUX = Array.from({ length: 8 }, (_, i) => `Niveau ${i + 1}`);
  function niveauDe(groupe) {
    const pose = ((groupe || {}).niveau || '').trim();
    if (NIVEAUX.includes(pose)) return pose;
    const trouve = /niveau\s*([1-8])/i.exec((groupe || {}).nom || '');
    return trouve ? `Niveau ${trouve[1]}` : 'Niveau 4';
  }
  const niveauGroupe = () => niveauDe(groupeActif());

  /** Les activités du niveau du groupe, plus celles qu'il a déjà datées. */
  function bornerAuNiveau(activites) {
    const liste = Array.isArray(activites) ? activites : [];
    const niveau = niveauGroupe();
    if (!niveau) return liste;
    return liste.filter((a) => (a.level || '') === niveau || a.datePrevue);
  }

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
    // La direction autorise, l'enseignant choisit : sans autorisation, le
    // bouton disparaît au lieu de rester là pour échouer devant la classe.
    // Le serveur refuse de toute façon — c'est lui qui garde.
    etat.seanceAutorisee = data.seanceAutorisee !== false;
    $('boutonSeance').hidden = !etat.seanceAutorisee;
    poserGroupes(data.groupes);
    // Sans groupe, il n'y a pas de niveau ; sans niveau, ni catalogue à
    // montrer ni élève à inscrire. La page se réduit donc à un seul écran,
    // et le contexte comme le menu restent cachés jusqu'à ce qu'un groupe
    // existe : un menu offert d'avance laisse chercher ce qui n'est pas là.
    if (!etat.groupes.length) etat.ecran = 'accueil';
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
    $('code').focus();
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
      niveau: niveauGroupe,
    });
    $('nomEnseignant').textContent = etat.enseignant.nom;
    // « Espace direction » ne paraît qu'à qui a la charge d'un centre. C'est le
    // serveur qui le dit — le rôle du compte ne porte plus la portée depuis
    // l'étape 2, et le deviner ici le referait mentir.
    try {
      const p = await json('/api/direction/portees');
      const lien = $('lienDirection');
      if (lien) lien.hidden = !(p.fondateur || p.centres.length);
    } catch { /* pas de portée, pas de lien : le défaut est le silence */ }
    // `/api/prof/me` renvoie les groupes bruts ; la liste dédiée y ajoute le
    // nombre d'élèves et le titulaire, affichés dans « Groupes et comptes ».
    try { poserGroupes(await json('/api/prof/groupes')); } catch { /* liste brute */ }
    rendreBandeGroupe();
    await chargerGroupe();
    montrerEcran(etat.ecran);
  }

  /** Recharge tout ce qui appartient au groupe actif. */
  async function chargerGroupe() {
    etat.elevesNeufs = new Set();
    if (!etat.groupeId) {
      etat.activites = []; etat.documents = []; etat.eleves = [];
      etat.progression = []; etat.journal = []; etat.corrigeMoi = [];
      rendreTout();
      return;
    }
    const g = `groupId=${encodeURIComponent(etat.groupeId)}`;
    try {
      const [activites, documents, eleves, progression, journal, corrigeMoi, sections] = await Promise.all([
        json(`/api/activities?${g}`),
        json(`/api/prof/documents?${g}`),
        json(`/api/admin/students?${g}`),
        json(`/api/admin/progress?${g}`),
        json(`/api/admin/access-log?${g}`),
        json(`/api/admin/corrige-moi?${g}`),
        // Le découpage vient avec les dates du groupe. Un serveur qui n'a pas
        // encore le relevé (`build/sections.py`) répond vide : la liste
        // redevient plate, sans casser la page.
        json(`/api/sections?${g}`).catch(() => ({})),
      ]);
      // Le niveau du groupe borne **tout** ce que l'enseignant voit, et pas
      // seulement `catalogue.html` : la liste à planifier, les compteurs, le
      // programme du jour. Un groupe de niveau 2 devant les 177 activités des
      // huit niveaux, c'est chercher les siennes à chaque fois.
      //
      // Exception, et elle compte : ce qui porte **déjà une date pour ce
      // groupe** reste visible même hors du niveau. Un groupe dont on change
      // le niveau perdrait sinon sa planification de vue — elle existerait
      // toujours côté serveur, et l'élève la verrait, mais plus l'enseignant.
      etat.activites = bornerAuNiveau(activites);
      etat.documents = documents;
      etat.eleves = eleves;
      etat.progression = progression;
      etat.journal = journal;
      etat.corrigeMoi = corrigeMoi;
      etat.sections = sections || {};
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
    // Le libellé était une phrase — « Aucun élève inscrit », « Voir les 12
    // élèves » — parce que ce lien vivait seul au bout de la ligne. Il est
    // maintenant la troisième entrée d'un menu : il prend le nom de sa vue,
    // et le compte le suit sans faire de phrase. Le résumé du bout de ligne
    // dit déjà l'état complet du groupe.
    $('lienEleves').textContent = nbEleves ? `Élèves · ${nbEleves}` : 'Élèves';
    const datees = etat.activites.filter((a) => a.datePrevue).length;
    $('resumeGroupe').textContent = groupe
      ? `${pluriel(nbEleves, 'élève')} · ${datees} activité${datees > 1 ? 's' : ''} planifiée${datees > 1 ? 's' : ''} sur ${etat.activites.length}`
      : 'Aucun groupe : créez-en un dans « Groupes et comptes ».';

    // Le catalogue s'ouvre déjà borné : il ne montre que le niveau du groupe.
    const cat = $('lienCatalogue');
    if (cat) cat.href = groupe ? `catalogue.html?niveau=${encodeURIComponent(niveauDe(groupe))}` : 'catalogue.html';

    const lien = $('lienTeams');
    lien.hidden = !(groupe && groupe.teams);
    if (groupe && groupe.teams) lien.href = groupe.teams;
    $('boutonTeams').textContent = groupe && groupe.teams ? 'Modifier le lien' : 'Ajouter le lien Teams';
    $('boutonTeams').disabled = !groupe;
    $('boutonCopie').disabled = etat.groupes.length < 2;
  }

  /* ══════════ Écran Planifier ══════════ */

  /* Les outils transversaux — « Corrige-moi ! », les cartes de vocabulaire,
     l'analyse grammaticale — ne se planifient pas : ils restent ouverts. Même
     règle de reconnaissance que le catalogue et le portail élève. */
  const DOMAINES_OUTILS = /^(vocabulaire|grammaire transversale|pratique orale libre|graphie et sons)/i;
  const estOutil = (a) => DOMAINES_OUTILS.test(a.domaineDeVie || '');

  function visibles() {
    const q = etat.recherche.trim().toLowerCase();
    const liste = etat.activites.filter((a) => {
      if (etat.filtre !== 'tous' && (a.categorie || 'atelier') !== etat.filtre) return false;
      if (!q) return true;
      const foin = [a.title, a.domaineDeVie, (a.tempsVerbaux || []).join(' ')].join(' ').toLowerCase();
      return foin.includes(q);
    });
    // Les modules (cours de 4 h) ouvrent la liste ; les ateliers suivent.
    // Entre modules, on suit le numéro du titre — « Module 3 » vient après
    // « Module 2 », quel que soit son rang dans activities.json, où l'ordre
    // des enregistrements reflète la date d'ajout, pas la progression.
    // Les ateliers gardent l'ordre du catalogue : le tri est stable.
    const rang = (a) => (estOutil(a) ? 2 : a.categorie === 'cours' ? 0 : 1);
    const numero = (a) => {
      const m = /^Module\s+(\d+)/.exec(a.title || '');
      return m ? parseInt(m[1], 10) : Number.MAX_SAFE_INTEGER;
    };
    return liste.sort((a, b) => {
      const dr = rang(a) - rang(b);
      if (dr) return dr;
      if (rang(a) === 1) return 0;
      return numero(a) - numero(b);
    });
  }

  function rendreJour() {
    const dj = new Date();
    $('dateJour').textContent = dj.toLocaleDateString('fr-CA', { weekday: 'long', day: 'numeric', month: 'long' });

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

    const cours = liste.filter(deployable);
    const toutDeplie = cours.length > 0 && cours.every((a) => etat.deplies.has(a.id));
    $('boutonDeploiTout').textContent = toutDeplie ? 'Replier les détails' : 'Déplier les détails';
    $('boutonDeploiTout').hidden = cours.length === 0;

    const toutesCochees = liste.length > 0 && liste.every((a) => etat.selection.has(cle(a.id)));
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
      const secs = sectionsDe(a.id);
      const deplie = etat.deplies.has(a.id);
      const temps = (a.tempsVerbaux && a.tempsVerbaux.length ? a.tempsVerbaux : (infos ? infos.temps : []));
      // Le type ouvre la méta en étiquette teintée — même code de couleur que
      // le catalogue, et le mot reste lisible sans la couleur.
      const outil = estOutil(a);
      const etiquetteType = `<span class="pe-type">${outil ? 'Outil' : estCours ? 'Cours 4 h' : 'Atelier 2 h'}</span>`;
      // Le niveau d'abord, à sa teinte : c'est le premier tri de l'œil.
      const nNiv = parseInt(String(a.level || '').replace(/\D/g, ''), 10);
      const etiquetteNiveau = outil
        ? ''
        : `<span class="pe-niveau pe-niveau--n${nNiv >= 1 && nNiv <= 8 ? nNiv : 4}">${esc(a.level || 'Niveau 4')}</span>`;
      const meta = estCours
        ? `${etiquetteNiveau}${etiquetteType}${esc(a.domaineDeVie || 'domaine à préciser')}`
        : `${etiquetteNiveau}${etiquetteType}${esc(a.domaineDeVie || 'domaine à préciser')} · ${esc(temps.join(', ') || '—')}`;

      const coche = etat.selection.has(cle(a.id));
      const metaSec = secs.length
        ? `${meta} · ${secs.length} sections`
        : meta;
      const rangee = `
        <div class="card__row pe-rangee pe-rangee--${outil ? 'outil' : estCours ? 'cours' : 'atelier'}${coche ? ' is-checked' : ''}" data-id="${a.id}">
          ${deployable(a)
            ? `<button type="button" class="pe-chevron" data-deploi="${a.id}" aria-expanded="${deplie}"
                       aria-label="Détails de ${esc(a.title)}">${deplie ? '▾' : '▸'}</button>`
            : '<span style="width:44px;flex:none" aria-hidden="true"></span>'}
          <input type="checkbox" class="pe-case" data-coche="${a.id}"
                 ${coche ? 'checked' : ''} aria-label="${esc(a.title)}" />
          <div class="pe-rangee-txt">
            <div class="pe-rangee-titre">${esc(a.title)}</div>
            <div class="pe-rangee-meta">${metaSec}</div>
          </div>
          ${pastille(st)}
          <button type="button" class="btn btn--ghost btn--sm" data-dates="${a.id}">Dates</button>
        </div>`;

      if (!deplie) return rangee;

      // Les sections d'abord : c'est ce qu'on vient chercher en dépliant une
      // rangée pour planifier. Les détails pédagogiques suivent.
      const bloc = !secs.length ? '' : `
        <div class="card__row pe-sections">
          <h4 class="pe-sections-titre">Sections du module</h4>
          ${secs.map((s) => {
            const k = cle(a.id, s.id);
            const cocheSec = etat.selection.has(k);
            const sst = statutSection(a, s);
            return `
            <div class="pe-sec${cocheSec ? ' is-checked' : ''}">
              <input type="checkbox" class="pe-case" data-coche="${a.id}" data-section="${esc(s.id)}"
                     ${cocheSec ? 'checked' : ''} aria-label="${esc(a.title)} — ${esc(s.titre)}" />
              <div class="pe-sec-txt">
                <div class="pe-sec-titre">${esc(s.titre)}</div>
                ${s.chapeau ? `<div class="pe-sec-meta">${esc(s.chapeau)}</div>` : ''}
              </div>
              ${pastille(sst)}
              <button type="button" class="btn btn--ghost btn--sm"
                      data-dates="${a.id}" data-section="${esc(s.id)}">Dates</button>
            </div>`;
          }).join('')}
        </div>`;

      if (!infos) return rangee + bloc;

      return rangee + bloc + `
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

  /** Les lignes cochées dans l'ordre de la liste : un module, puis ses
      sections dépliées. C'est cet ordre que le rythme suit. */
  function lignesChoisies() {
    const out = [];
    visibles().forEach((a) => {
      if (etat.selection.has(cle(a.id))) {
        out.push({ id: a.id, section: '', titre: a.title });
      }
      sectionsDe(a.id).forEach((s) => {
        if (etat.selection.has(cle(a.id, s.id))) {
          out.push({ id: a.id, section: s.id, titre: `${a.title} · ${s.titre}` });
        }
      });
    });
    return out;
  }

  function datesCalculees() {
    const choisies = lignesChoisies();
    const pas = PAS[etat.rythme] ?? 7;
    const debut = $('dateDebut').value;
    if (!debut) return [];
    const base = lire(debut);
    const eviter = $('eviterFinDeSemaine').checked;
    return choisies.map((ligne, i) => {
      const d = new Date(base.getTime() + pas * i * JOUR);
      if (eviter && pas > 0) {
        if (d.getDay() === 6) d.setDate(d.getDate() + 2);
        else if (d.getDay() === 0) d.setDate(d.getDate() + 1);
      }
      return { ...ligne, date: iso(d) };
    });
  }

  function rendreBarre() {
    const n = etat.selection.size;
    $('barreAction').hidden = n === 0;
    if (!n) return;
    // « Ligne » plutôt qu'« activité » : la sélection mêle des modules et des
    // sections, et un module coché avec ses trois défis fait quatre dates.
    const sections = [...etat.selection].filter((k) => k.includes(':')).length;
    $('libelleSelection').textContent = sections
      ? `${n} ligne${n > 1 ? 's cochées' : ' cochée'}, dont ${sections} section${sections > 1 ? 's' : ''}`
      : (n > 1 ? `${n} activités cochées` : '1 activité cochée');
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
        sectionId: p.section || '',
      });
      faites += 1;
    }
    return faites;
  }

  /** Un module sans date ne s'ouvre pas, et ses sections restent invisibles
      quoi qu'on leur donne. Planifier des sections seules ouvre donc le module
      à la première d'entre elles — sinon la classe ne verrait rien. */
  function modulesAOuvrir(plan) {
    const premieres = new Map();
    plan.filter((p) => p.section).forEach((p) => {
      const a = etat.activites.find((x) => x.id === p.id);
      if (!a || a.datePrevue) return;                 // le module a déjà sa date
      const deja = premieres.get(p.id);
      if (!deja || p.date < deja) premieres.set(p.id, p.date);
    });
    return [...premieres].map(([id, date]) => ({ id, section: '', date }));
  }

  async function planifier() {
    const plan = datesCalculees();
    if (!plan.length) { dire('Choisissez une date d’ouverture.'); return; }
    const boutons = [$('boutonPlanifier'), $('boutonRetirerDates')];
    boutons.forEach((b) => { b.disabled = true; });
    try {
      const fermeture = $('dateFin').value || '';
      const faites = await poserDates(plan, fermeture);
      const ouverts = modulesAOuvrir(plan);
      if (ouverts.length) await poserDates(ouverts, fermeture);
      const sections = plan.filter((p) => p.section).length;
      dire(sections
        ? `${faites} ligne${faites > 1 ? 's planifiées' : ' planifiée'}, dont ${sections} section${sections > 1 ? 's' : ''}.`
        : `${faites} activité${faites > 1 ? 's planifiées' : ' planifiée'}.`);
    } catch (e) {
      dire(`Interrompu : ${e.message}`);
    } finally {
      boutons.forEach((b) => { b.disabled = false; });
      await chargerGroupe();
    }
  }

  async function retirerDates() {
    const lignes = lignesChoisies();
    if (!lignes.length) return;
    const sections = lignes.filter((l) => l.section).length;
    const quoi = sections === lignes.length
      ? `${sections} section(s) ? Elles reviendront au régime de leur module.`
      : `${lignes.length} ligne(s) ? Ce qui est retiré disparaît du portail des élèves de ce groupe.`;
    if (!confirm(`Retirer les dates de ${quoi}`)) return;
    const boutons = [$('boutonPlanifier'), $('boutonRetirerDates')];
    boutons.forEach((b) => { b.disabled = true; });
    try {
      await poserDates(lignes.map((l) => ({ ...l, date: '' })), '');
      dire(sections === lignes.length
        ? 'Dates retirées : ces sections suivent de nouveau leur module.'
        : 'Dates retirées : ces activités disparaissent du portail des élèves.');
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
        <div class="card__row pe-rangee${etat.elevesNeufs.has(el.id) ? ' pe-neuf' : ''}">
          <div class="pe-rangee-txt">
            <div class="pe-rangee-titre" style="font-size:var(--fs-body-sm)">${esc(el.label || 'Élève')}</div>
            <div class="pe-rangee-meta">${esc(depuis(derniereVisite))} · dernière étape : ${esc(derniere ? derniere.activityTitle || '—' : '—')}</div>
          </div>
          <span class="pe-acces">${esc(el.code)}</span>
          <span class="score">${faites} / ${offertes.length} offertes</span>
          <div class="pe-eleve-gestes">
            <a class="btn btn--ghost btn--sm" href="fiche-eleve.html?code=${encodeURIComponent(el.code)}">Dossier</a>
            <button type="button" class="btn btn--ghost btn--sm" data-copier="${el.id}">Copier le code</button>
            <button type="button" class="btn btn--ghost btn--sm" data-renommer="${el.id}">Renommer</button>
            <button type="button" class="btn btn--ghost btn--sm" data-retirer="${el.id}">Retirer</button>
          </div>
        </div>`;
    }).join('');

    rendreCorrigeMoi();
  }

  /** Ajouter des élèves, c'est générer leurs codes : le serveur en fabrique un
      par élève et le renvoie. Un élève créé sans pseudo porte « Élève N » — on
      prépare ainsi des codes d'avance, qu'on nomme à l'arrivée. */
  async function ajouterEleves(label, nombre) {
    const res = await envoyer('/api/admin/students',
      { groupId: etat.groupeId, label, count: nombre });
    const neufs = res.students || [];
    etat.eleves = etat.eleves.concat(neufs);
    etat.elevesNeufs = new Set(neufs.map((e) => e.id));
    majNombreEleves();
    rendreEleves();
    return neufs;
  }

  /** Le compte d'élèves paraît à trois endroits (bande, résumé, liste des
      groupes) et ne vient pas du même appel : on le remet d'accord ici plutôt
      que de recharger tout le groupe pour un seul code. */
  function majNombreEleves() {
    const groupe = groupeActif();
    if (groupe) groupe.nbEleves = etat.eleves.length;
    rendreBandeGroupe();
    rendreGroupes();
  }

  /** Le presse-papiers n'existe pas partout (page servie en http simple) :
      on retombe alors sur une sélection de texte, qui marche toujours. */
  async function copier(texte) {
    try {
      await navigator.clipboard.writeText(texte);
      return true;
    } catch {
      const zone = document.createElement('textarea');
      zone.value = texte;
      zone.style.cssText = 'position:fixed;top:-1000px';
      document.body.appendChild(zone);
      zone.select();
      let ok = false;
      try { ok = document.execCommand('copy'); } catch { ok = false; }
      zone.remove();
      return ok;
    }
  }

  /** Les codes s'impriment dans le cadre isolé du dépôt de matériel, en noir
      et blanc : un billet par élève, à découper et à remettre en main propre.
      Rien de l'interface ne peut s'y glisser. */
  function imprimerCodes() {
    if (!etat.eleves.length) { dire('Aucun code à imprimer pour ce groupe.'); return; }
    const groupe = groupeActif();
    const billets = etat.eleves.map((el) => `
      <div class="billet">
        <div class="groupe">${esc(groupe ? groupe.nom : '')}</div>
        <div class="nom">${esc(el.label || 'Élève')}</div>
        <div class="etiquette">Votre code d’accès</div>
        <div class="code">${esc(el.code)}</div>
        <div class="adresse">${esc(location.origin)}/eleve.html</div>
      </div>`).join('');
    const cadre = $('matImpression');
    const d = cadre.contentDocument;
    d.open();
    d.write(`<!DOCTYPE html><html lang="fr"><head><meta charset="utf-8">
      <title>Codes d’accès</title><style>
      @page { size: letter; margin: 14mm; }
      body { margin: 0; font-family: Arial, Helvetica, sans-serif; color: #000; }
      .grille { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; }
      .billet { border: 1.5pt solid #000; padding: 6mm; break-inside: avoid; }
      .groupe { font-size: 9pt; text-transform: uppercase; letter-spacing: .08em; }
      .nom { margin-top: 2mm; font-size: 15pt; font-weight: 800; }
      .etiquette { margin-top: 5mm; font-size: 9pt; }
      .code { margin-top: 1mm; font-family: "Courier New", monospace;
              font-size: 26pt; font-weight: 700; letter-spacing: .18em; }
      .adresse { margin-top: 4mm; font-size: 9pt; }
      </style></head><body><div class="grille">${billets}</div></body></html>`);
    d.close();
    // Laisser les styles s'appliquer avant d'ouvrir le dialogue d'impression.
    setTimeout(() => {
      cadre.contentWindow.focus();
      cadre.contentWindow.print();
      dire(`${pluriel(etat.eleves.length, 'code')} envoyé${etat.eleves.length > 1 ? 's' : ''} à l’impression.`);
    }, 300);
  }

  /** « Corrige-moi ! » : une rangée par élève qui a déjà pratiqué, cumulée
      sur tous les thèmes. L'atelier est libre : il n'y a rien à corriger ni
      à noter, seulement une trace de pratique. */
  function rendreCorrigeMoi() {
    const parEleve = new Map();
    etat.corrigeMoi.forEach((e) => {
      const fiche = parEleve.get(e.studentId) || {
        nom: e.studentLabel || '', themes: [], reponses: 0, justes: 0, derniere: '',
      };
      if (e.studentLabel) fiche.nom = e.studentLabel;
      if (e.themeLabel && !fiche.themes.includes(e.themeLabel)) fiche.themes.push(e.themeLabel);
      fiche.reponses += e.answers || 0;
      fiche.justes += e.firstTryOk || 0;
      if (String(e.lastSeen || '') > fiche.derniere) fiche.derniere = e.lastSeen || '';
      parEleve.set(e.studentId, fiche);
    });

    const rangees = etat.eleves
      .filter((el) => parEleve.has(el.id))
      .map((el) => {
        const f = parEleve.get(el.id);
        const nom = el.label || f.nom || 'Élève';
        return { nom, ...f };
      })
      .sort((a, b) => String(b.derniere).localeCompare(String(a.derniere)));

    if (!rangees.length) {
      $('listeCorrigeMoi').innerHTML =
        '<div class="card__row" style="font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Personne n’a encore pratiqué dans cet atelier.</div>';
      return;
    }

    $('listeCorrigeMoi').innerHTML = rangees.map((f) => `
      <div class="card__row pe-rangee">
        <div class="pe-rangee-txt">
          <div class="pe-rangee-titre" style="font-size:var(--fs-body-sm)">${esc(f.nom)}</div>
          <div class="pe-rangee-meta">${esc(f.themes.join(' · ') || 'aucun thème')} · ${esc(depuis(f.derniere))}</div>
        </div>
        <span class="score">${f.reponses} corrigée${f.reponses > 1 ? 's' : ''} · ${f.justes} juste${f.justes > 1 ? 's' : ''} du premier coup</span>
      </div>`).join('');
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
          <div class="pe-rangee-meta">${esc(niveauDe(g))} · ${pluriel(g.nbEleves || 0, 'élève')} · ${esc(g.titulaire || 'sans titulaire')} · ${g.teams ? 'rencontre Teams liée' : 'aucun lien Teams'}</div>
        </div>
        <button type="button" class="btn btn--ghost btn--sm" data-activer-groupe="${g.id}">Planifier ce groupe</button>
        <button type="button" class="btn btn--ghost btn--sm" data-renommer-groupe="${g.id}">Renommer</button>
        <button type="button" class="btn btn--ghost btn--sm" data-niveau-groupe="${g.id}">Changer le niveau</button>
      </div>`).join('')
      || '<div class="card__row" style="font-size:var(--fs-body-sm);font-weight:var(--fw-bold);color:var(--text-muted)">Aucun groupe pour l’instant. Créez-en un ci-dessous.</div>';
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
    // Aucun groupe : quoi qu'on demande, il n'y a qu'un écran possible.
    if (!etat.groupes.length) nom = 'accueil';
    etat.ecran = nom;
    const accueil = nom === 'accueil';
    $('vueAccueil').hidden = !accueil;
    $('vuePlanif').hidden = accueil || nom !== 'planif';
    $('vueEleves').hidden = accueil || nom !== 'eleves';
    $('vueGroupes').hidden = accueil || nom !== 'groupes';
    $('vueMateriel').hidden = accueil || nom !== 'materiel';
    // Le contexte de groupe et son menu n'ont rien à dire tant qu'aucun
    // groupe n'existe : ils s'effacent en entier plutôt que de s'afficher
    // vides. C'est aussi ce qui rend l'écran d'accueil sans issue — et c'est
    // voulu : la seule chose à faire est d'ouvrir un groupe.
    const contexte = document.querySelector('.pe-contexte');
    if (contexte) contexte.hidden = accueil;
    // La barre des sections a disparu : chaque vue se marque dans la ligne
    // de liens, là où on a cliqué.
    document.querySelectorAll('.pe-liens [data-ecran]').forEach((b) => {
      const courant = b.dataset.ecran === nom;
      b.classList.toggle('is-actif', courant);
      if (courant) b.setAttribute('aria-current', 'page');
      else b.removeAttribute('aria-current');
    });
    // Le dépôt se charge à la première ouverture de l'onglet, pas au
    // démarrage : la plupart des visites au portail ne le touchent pas.
    if (nom === 'materiel') Materiel.afficher();
    window.scrollTo({ top: 0 });
  }

  function ouvrirModale(id) { $(id).hidden = false; }
  function fermerModale(id) { $(id).hidden = true; }

  /* ══════════ Écoutes ══════════ */

  // — Connexion —
  /* Première ouverture : on remplace le code ET le mot de passe temporaires.
     La carte de connexion s'efface — on ne peut pas revenir en arrière sans
     recharger, et recharger sans avoir choisi ramène ici. */
  function ouvrirPremiereConnexion() {
    $('formConnexion').closest('.pe-connexion').hidden = true;
    $('ecranPremiere').hidden = false;
    $('premCode').focus();
  }

  document.addEventListener('submit', async (e) => {
    if (e.target.id !== 'formPremiere') return;
    e.preventDefault();
    const boite = $('erreurPremiere');
    const dire = (m) => { boite.textContent = m; boite.hidden = false; };
    // Vider le texte en plus de cacher la boîte : une erreur corrigée ne doit
    // pas ressortir au prochain refus si celui-ci est d'une autre nature.
    boite.textContent = ''; boite.hidden = true;
    const code = $('premCode').value.trim().toUpperCase();
    const mdp = $('premMotDePasse').value;
    if (mdp !== $('premMotDePasse2').value) return dire('Les deux mots de passe diffèrent.');
    const bouton = $('boutonPremiere');
    bouton.disabled = true;
    try {
      // `envoyer()` porte le jeton, relève un 401 comme partout ailleurs et
      // lève sur un refus en remontant le message du serveur tel quel — c'est
      // lui qui connaît le motif.
      const data = await envoyer('/api/prof/premiere-connexion',
                                 { code: code, motDePasse: mdp });
      etat.enseignant = data.enseignant;
      $('ecranPremiere').hidden = true;
      etat.ecran = etat.groupes.length ? 'planif' : 'accueil';
      await ouvrirPortail();
    } catch (err) {
      dire(err.message);
    } finally {
      bouton.disabled = false;
    }
  });

  $('formConnexion').addEventListener('submit', async (e) => {
    e.preventDefault();
    const bouton = $('boutonConnexion');
    bouton.disabled = true;
    try {
      const res = await fetch('/api/prof/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          code: $('code').value.trim().toUpperCase(),
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
      // Un compte encore temporaire ne va nulle part avant d'avoir choisi son
      // code et son mot de passe : le serveur refuserait tout le reste de
      // toute façon le jour où on l'y obligera, et surtout ce qui a circulé
      // sur un billet ne doit pas rester la clé du compte.
      if (data.doitChanger) { ouvrirPremiereConnexion(); return; }
      etat.ecran = etat.groupes.length ? 'planif' : 'accueil';
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

  // Le premier groupe. Même route et même refus que le formulaire de la vue
  // « Nouveau groupe » — un seul chemin serveur, deux portes. Le niveau est
  // obligatoire des deux côtés : c'est lui qui ouvrira le catalogue.
  $('formPremierGroupe').addEventListener('submit', async (e) => {
    e.preventDefault();
    const nom = $('premierGroupeNom').value.trim();
    const niveau = $('premierGroupeNiveau').value;
    if (!nom) return;
    if (!niveau) { dire('Choisissez le niveau du groupe.'); $('premierGroupeNiveau').focus(); return; }
    try {
      const res = await envoyer('/api/prof/groupes', { nom, niveau });
      $('premierGroupeNom').value = '';
      $('premierGroupeNiveau').value = '';
      // Le groupe neuf devient l'actif : c'est celui qu'on vient de nommer.
      etat.groupes = await json('/api/prof/groupes');
      etat.groupeId = res.groupe.id;
      localStorage.setItem(CLE_GROUPE, String(etat.groupeId));
      await chargerGroupe();
      montrerEcran('planif');
      dire(`Groupe « ${nom} » ouvert en ${niveau}. Il part vide : donnez-lui ses premières dates.`);
    } catch (err) {
      dire(`Groupe impossible : ${err.message}`);
    }
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
    document.querySelectorAll('#filtres .pe-filtre').forEach((b) => {
      const actif = b.dataset.filtre === etat.filtre;
      b.classList.toggle('btn--pri', actif);
      b.classList.toggle('btn--ghost', !actif);
      b.setAttribute('aria-pressed', actif ? 'true' : 'false');
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
    const k = cle(Number(case_.dataset.coche), case_.dataset.section || '');
    if (case_.checked) etat.selection.add(k); else etat.selection.delete(k);
    case_.closest('.pe-rangee, .pe-sec').classList.toggle('is-checked', case_.checked);
    const liste = visibles();
    const toutes = liste.length > 0 && liste.every((a) => etat.selection.has(cle(a.id)));
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
    if (dates) ouvrirDates(Number(dates.dataset.dates), dates.dataset.section || '');
  });

  $('boutonDeploiTout').addEventListener('click', () => {
    const cours = visibles().filter(deployable);
    const toutDeplie = cours.length > 0 && cours.every((a) => etat.deplies.has(a.id));
    if (toutDeplie) cours.forEach((a) => etat.deplies.delete(a.id));
    else cours.forEach((a) => etat.deplies.add(a.id));
    rendreListe();
  });

  $('boutonToutCocher').addEventListener('click', () => {
    const liste = visibles();
    // Ce bouton ne coche que les modules : cocher d'un coup toutes les
    // sections de vingt activités ferait une planification que personne n'a
    // demandée. Les sections se cochent dans la rangée dépliée.
    const toutes = liste.length > 0 && liste.every((a) => etat.selection.has(cle(a.id)));
    if (toutes) liste.forEach((a) => etat.selection.delete(cle(a.id)));
    else liste.forEach((a) => etat.selection.add(cle(a.id)));
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
  function ouvrirDates(id, sectionId) {
    const a = etat.activites.find((x) => x.id === id);
    if (!a) return;
    const sec = sectionId ? sectionsDe(id).find((s) => s.id === sectionId) : null;
    if (sectionId && !sec) return;
    etat.detail = id;
    etat.detailSection = sec ? sec.id : '';
    const groupe = groupeActif() ? groupeActif().nom : '';
    const nature = a.categorie === 'cours' ? 'Module' : 'Atelier';
    $('detailPortee').textContent = sec
      ? `${groupe} · Section de ${esc(a.title)}`
      : `${groupe} · ${nature}`;
    $('detailTitre').textContent = sec ? sec.titre : a.title;
    const source = sec ? sec.dates : a;
    $('dOuverture').value = source.datePrevue || '';
    $('dFermeture').value = source.dateFin || '';
    $('dVue').value = source.dateVue || '';
    $('dLien').value = source.lien || '';
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
        sectionId: etat.detailSection || '',
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

  // — Séance sans compte —
  //
  // La direction autorise, l'enseignant choisit : le bouton n'existe que si
  // le mode est ouvert pour ce centre. Le serveur refuse de toute façon —
  // c'est lui qui garde — mais un bouton qui échoue devant la classe vaut
  // moins qu'un bouton absent.

  function rendreSeances(seances) {
    const liste = $('seanceListe');
    if (!seances.length) {
      liste.innerHTML = '<p style="margin:0;font-size:var(--fs-body-sm);'
        + 'font-weight:var(--fw-semi);color:var(--ink-500)">'
        + 'Aucune séance ouverte pour ce groupe.</p>';
      return;
    }
    liste.innerHTML = seances.map((s) => `
      <div class="pe-seance${s.ouverte ? '' : ' pe-seance--close'}">
        <span class="pe-seance-code">${esc(s.code)}</span>
        <span class="pe-seance-quoi">${esc(s.activityTitle || 'Module')}
          <span>${s.ouverte ? pluriel(s.participants, 'participant')
                            : 'fermée'}</span></span>
        <a class="btn btn--ghost btn--sm" target="_blank" rel="noopener"
           href="feuille-seance.html?code=${encodeURIComponent(s.code)}">La feuille</a>
        ${s.ouverte ? `<a class="btn btn--ghost btn--sm" target="_blank" rel="noopener"
           href="progression.html?module=${s.activityId}">Le direct</a>` : ''}
        ${s.ouverte ? `<button type="button" class="btn btn--ghost btn--sm"
           data-fermer-seance="${s.id}">Fermer</button>` : ''}
      </div>`).join('');
  }

  async function chargerSeances() {
    try {
      const res = await json(`/api/prof/seances?groupId=${etat.groupeId}`);
      rendreSeances(res.seances || []);
    } catch (err) {
      $('seanceListe').textContent = `Séances indisponibles : ${err.message}`;
    }
  }

  $('boutonSeance').addEventListener('click', async () => {
    // Le choix se fait dans les modules qui ont un fichier à ouvrir : une
    // séance sur un module sans fichier n'ouvrirait rien.
    //
    // Les chemins sont lus **à plat** (`a.interactive`) : cette page reçoit
    // les enregistrements bruts du catalogue, et non la forme groupée `files`
    // que sert le portail élève. Le premier jet filtrait sur `files` et
    // rendait une liste vide — sans erreur, sans message, juste un menu sans
    // rien dedans.
    //
    // Et volontairement sans regarder les dates : une séance s'ouvre sur ce
    // qu'on fait aujourd'hui, planifié ou non.
    //
    // `suivable` est calculé par le serveur, qui va voir dans le fichier si
    // l'activité renvoie vraiment les réponses (`rapporte_au_direct`). Les
    // 87 modules et les 56 ateliers de la banque le font ; les ateliers
    // écrits à la main, les cartes mémoire et la cabine d'enregistrement,
    // non. Ouvrir une séance sur l'une d'elles donnait une feuille, une
    // classe qui répond, et un tableau vide sans un mot d'explication.
    const avecFichier = etat.activites.filter((a) => a.parcours || a.interactive);
    const ouvrables = avecFichier.filter((a) => a.suivable);
    const ecartes = avecFichier.length - ouvrables.length;
    $('seanceModule').innerHTML = ouvrables
      .map((a) => `<option value="${a.id}">${esc(a.title)}</option>`).join('');
    $('seanceEcartees').textContent = ecartes
      ? `${ecartes} activité${ecartes > 1 ? 's ne sont' : ' n\'est'} pas dans cette liste : `
        + `${ecartes > 1 ? 'elles ne renvoient' : 'elle ne renvoie'} pas les réponses des `
        + `élèves, et le tableau de la classe resterait vide.`
      : '';
    $('boutonOuvrirSeance').disabled = !ouvrables.length;
    ouvrirModale('modaleSeance');
    await chargerSeances();
  });

  $('formSeance').addEventListener('submit', async (e) => {
    e.preventDefault();
    const activityId = Number($('seanceModule').value);
    if (!activityId) return;
    try {
      const res = await envoyer('/api/prof/seances',
        { groupId: etat.groupeId, activityId });
      dire(`Séance ouverte. Le code est ${res.seance.code}.`);
      await chargerSeances();
      window.open(`feuille-seance.html?code=${encodeURIComponent(res.seance.code)}`,
                  '_blank');
    } catch (err) {
      dire(`Séance impossible : ${err.message}`);
    }
  });

  $('seanceListe').addEventListener('click', async (e) => {
    const bouton = e.target.closest('[data-fermer-seance]');
    if (!bouton) return;
    try {
      await envoyer('/api/prof/seances/fermer',
                    { id: Number(bouton.dataset.fermerSeance) });
      await chargerSeances();
      dire('Séance fermée. Le code ne marche plus.');
    } catch (err) {
      dire(`Fermeture impossible : ${err.message}`);
    }
  });

  // — Aperçu élève —
  $('boutonApercu').addEventListener('click', () => {
    rendreApercu();
    ouvrirModale('modaleApercu');
  });

  // — Groupes et comptes —
  // — Élèves —
  $('formEleve').addEventListener('submit', async (e) => {
    e.preventDefault();
    if (!etat.groupeId) { dire('Créez d’abord un groupe.'); return; }
    const label = $('nouvelEleve').value.trim();
    const nombre = Math.min(30, Math.max(1, parseInt($('nombreEleves').value, 10) || 1));
    // Un nom ne vaut que pour une personne : le serveur le donnerait tel quel
    // aux N élèves créés, et la liste porterait trois fois le même nom.
    if (label && nombre > 1) {
      dire('Un nom ne vaut que pour un élève. Videz le nom pour générer plusieurs codes d’un coup.');
      return;
    }
    const bouton = e.target.querySelector('button[type=submit]');
    bouton.disabled = true;
    try {
      const neufs = await ajouterEleves(label, nombre);
      $('nouvelEleve').value = '';
      $('nombreEleves').value = '1';
      $('nouvelEleve').focus();
      dire(neufs.length === 1
        ? `Code ${neufs[0].code} créé pour ${neufs[0].label}.`
        : `${neufs.length} codes créés : ${neufs.map((n) => n.code).join(', ')}.`);
    } catch (err) {
      dire(`Ajout impossible : ${err.message}`);
    }
    bouton.disabled = false;
  });

  $('boutonImprimerCodes').addEventListener('click', imprimerCodes);

  $('listeEleves').addEventListener('click', async (e) => {
    const bouton = e.target.closest('[data-copier], [data-renommer], [data-retirer]');
    if (!bouton) return;
    const id = parseInt(bouton.dataset.copier || bouton.dataset.renommer || bouton.dataset.retirer, 10);
    const eleve = etat.eleves.find((el) => el.id === id);
    if (!eleve) return;

    if (bouton.dataset.copier) {
      dire(await copier(eleve.code)
        ? `Code ${eleve.code} copié.`
        : `Copie impossible — le code est ${eleve.code}.`);
      return;
    }

    if (bouton.dataset.renommer) {
      const nom = prompt('Pseudo de l’élève', eleve.label || '');
      if (nom === null) return;
      const propre = nom.trim();
      if (!propre || propre === eleve.label) return;
      try {
        await envoyer(`/api/admin/students/${id}`, { label: propre }, 'PATCH');
        eleve.label = propre;
        rendreEleves();
        dire('Pseudo enregistré. Le code d’accès, lui, ne change pas.');
      } catch (err) {
        dire(`Modification impossible : ${err.message}`);
      }
      return;
    }

    // Retirer un élève retire son code : c'est ce que la confirmation doit dire.
    if (!confirm(`Retirer ${eleve.label || 'cet élève'} du groupe ? `
      + `Le code ${eleve.code} cessera de fonctionner et la personne ne pourra plus ouvrir son portail.`)) return;
    try {
      await api(`/api/admin/students/${id}`, { method: 'DELETE' });
      etat.eleves = etat.eleves.filter((el) => el.id !== id);
      etat.elevesNeufs.delete(id);
      majNombreEleves();
      rendreEleves();
      dire('Élève retiré du groupe.');
    } catch (err) {
      dire(`Retrait impossible : ${err.message}`);
    }
  });

  $('formGroupe').addEventListener('submit', async (e) => {
    e.preventDefault();
    const nom = $('nouveauGroupe').value.trim();
    const niveau = $('nouveauNiveau').value;
    if (!nom) return;
    // Le niveau ouvre le catalogue et le dépôt : le groupe ne part pas sans lui.
    if (!niveau) { dire('Choisissez le niveau du groupe.'); $('nouveauNiveau').focus(); return; }
    try {
      const res = await envoyer('/api/prof/groupes', { nom, niveau });
      $('nouveauGroupe').value = '';
      $('nouveauNiveau').value = '';
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
    const changerNiveau = e.target.closest('[data-niveau-groupe]');
    if (changerNiveau) {
      const id = Number(changerNiveau.dataset.niveauGroupe);
      const groupe = etat.groupes.find((g) => g.id === id);
      const rep = prompt(`Niveau du groupe « ${groupe ? groupe.nom : ''} » — un chiffre de 1 à 8.\n\nIl décide de ce que le catalogue et le dépôt de matériel montrent.`,
        String(niveauDe(groupe)).replace(/\D/g, ''));
      if (rep === null) return;
      const n = parseInt(rep.trim(), 10);
      if (!(n >= 1 && n <= 8)) { dire('Le niveau doit être un chiffre de 1 à 8.'); return; }
      try {
        await envoyer(`/api/prof/groupes/${id}`, { niveau: `Niveau ${n}` }, 'PATCH');
        etat.groupes = await json('/api/prof/groupes');
        rendreBandeGroupe();
        rendreGroupes();
        // Le dépôt montre le niveau du groupe : il doit se redessiner.
        Materiel.changerGroupe();
        dire(`Groupe passé au niveau ${n}. Le catalogue et le matériel suivent.`);
      } catch (err) {
        dire(`Changement impossible : ${err.message}`);
      }
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

  /* ══════════ Signalements ══════════ */
  /* L'outil est en développement : le bandeau le dit, ce bouton fait remonter
     ce qui cloche. Le serveur écrit la fiche, demande un premier tri à l'IA et
     envoie la note par courriel — d'où une seule requête ici. */

  const ECRAN_LABEL = {
    planif: 'Planifier', eleves: 'Élèves',
    groupes: 'Groupes et comptes', materiel: 'Matériel',
  };

  function rendreSignalements(entrees) {
    const bloc = $('blocSignalements');
    if (!entrees.length) { bloc.hidden = true; return; }
    bloc.hidden = false;
    // Les trois derniers suffisent : la modale sert à écrire, pas à consulter.
    // Le sort du courriel est affiché avec le reste : sans lui, un envoi
    // manqué ne se voyait qu'à l'absence de courriel, ce qui ne dit rien.
    $('listeSignalements').innerHTML = entrees.slice(0, 3).map((e) => `
      <div class="pe-signal-item">
        <time>${esc(court(String(e.timestamp || '').slice(0, 10)))} · ${esc(e.ecran || '')}</time>
        <p>${esc(e.description || '')}</p>
        ${e.analyse ? `<div class="pe-signal-analyse">${esc(e.analyse)}</div>` : ''}
        <div class="fb ${e.courrielEnvoye ? 'fb--ok' : 'fb--warn'}" style="margin-top:var(--sp-2)">
          ${e.courrielEnvoye ? 'Courriel envoyé' : `Courriel non parti — ${esc(e.courrielRaison || 'raison inconnue')}`}
        </div>
      </div>`).join('');
  }

  $('boutonSignaler').addEventListener('click', async () => {
    $('erreurSignalement').hidden = true;
    $('resultatEssai').hidden = true;
    $('boutonEssaiCourriel').hidden = false;
    $('sEcran').value = ECRAN_LABEL[etat.ecran] || 'Autre';
    ouvrirModale('modaleSignalement');
    $('sDescription').focus();
    try {
      rendreSignalements(await json('/api/signalements'));
    } catch {
      $('blocSignalements').hidden = true;   // l'historique n'est qu'un confort
    }
  });

  $('boutonEssaiCourriel').addEventListener('click', async () => {
    const zone = $('resultatEssai');
    zone.className = 'fb';
    zone.textContent = 'Essai en cours…';
    zone.hidden = false;
    try {
      const r = await envoyer('/api/signalement/essai', {});
      const ou = r.config.destinataire || '(aucune adresse)';
      const voie = r.config.resend ? 'Resend' : (r.config.smtp ? 'SMTP' : 'aucune voie configurée');
      zone.className = `fb ${r.ok ? 'fb--ok' : 'fb--no'}`;
      zone.textContent = r.ok
        ? `Envoyé à ${ou} par ${voie}. Regardez aussi les indésirables.`
        : `Échec (${voie}, destination ${ou}) : ${r.raison}`;
    } catch (err) {
      zone.className = 'fb fb--no';
      zone.textContent = `Essai impossible : ${err.message}`;
    }
  });

  $('formSignalement').addEventListener('submit', async (e) => {
    e.preventDefault();
    const description = $('sDescription').value.trim();
    if (!description) return;
    const bouton = $('boutonEnvoiSignalement');
    bouton.disabled = true;
    bouton.textContent = 'Envoi…';
    try {
      await envoyer('/api/signalement', {
        description,
        ecran: $('sEcran').value,
        url: location.href,
      });
      $('sDescription').value = '';
      fermerModale('modaleSignalement');
      dire('Signalement envoyé. Merci — il sera examiné.');
    } catch (err) {
      const zone = $('erreurSignalement');
      zone.textContent = `Envoi impossible : ${err.message}`;
      zone.hidden = false;
    } finally {
      bouton.disabled = false;
      bouton.textContent = 'Envoyer';
    }
  });

  /* ══════════ Amorçage ══════════ */

  $('dateDebut').value = aujourdhui();
  document.querySelector('#rythmes [data-rythme="semaine"]').classList.add('is-selected');
  demarrer();
})();
