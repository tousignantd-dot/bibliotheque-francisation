/* ═══════════════════════════════════════════════════════════════════════════
   « Travailler avec Claude » — version 2, habillée au système de design de la
   bibliothèque de francisation (assets/design-system).

   Jetons repris tels quels : paper-100 en fond de page, cartes blanches à
   filet 1 px, encre #17181A, un seul accent vert, cinq couleurs de section
   pour le REPÉRAGE seulement, violet réservé à la marque francis.
   Règle appliquée partout : jamais d'information portée par la couleur seule.
   ═══════════════════════════════════════════════════════════════════════════ */
const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.layout = "LAYOUT_WIDE";
p.author = "Daniel Tousignant";
p.title  = "Travailler avec Claude";

/* ── Jetons ───────────────────────────────────────────────────────────── */
const PAPER100 = "F7F7F5", PAPER50 = "FBFBFA", PAPER200 = "F0F0EE", BLANC = "FFFFFF";
const LINE100 = "EAEAE8", LINE200 = "D8E8DF", LINE300 = "D6D6D2";
const INK900 = "17181A", INK700 = "3A3D40", INK500 = "4B4F52", INK400 = "6E7175";
const GREEN800 = "07734A", GREEN600 = "0A8F5B", GREEN100 = "E6F5EE", GREEN050 = "EDF6F1";
const ACIER = "1D6B8F",  ACIER100  = "E7F0F6";
const INDIGO = "3B49A0", INDIGO100 = "E8EAFA";
const AMBRE = "B45309",  AMBRE100  = "FBEEDC";
const TEAL = "0D7A6F",   TEAL100   = "DCF2EF";
const FORET = "166534",  FORET100  = "E3F1E7";
const WARNBG = "FEF6E7", WARNLINE = "D9880B", WARNINK = "8A5206";
const MARQUE = "6B4FBB";
const F = "Trebuchet MS";            /* fallback documenté de Nunito */

const ML = 0.75, LARG = 11.83;

/* ── Primitives ───────────────────────────────────────────────────────── */
function page(fond){
  const s = p.addSlide();
  s.background = { color: fond || PAPER100 };
  return s;
}
function txt(s, t, o){
  s.addText(t, Object.assign({ isTextBox:true, margin:0, valign:"top",
    fontFace:F, fontSize:13.5, color:INK700, lineSpacing:19 }, o));
}
/* sur-titre : majuscules, 800, interlettrage .12em */
function surtitre(s, t, x, y, coul, w){
  txt(s, t.toUpperCase(), { x, y, w:w||LARG, h:0.26,
    fontSize:10.5, bold:true, charSpacing:2.2, color: coul || INK400 });
}
function entete(s, sur, titre, coul){
  surtitre(s, sur, ML, 0.42, coul);
  txt(s, titre, { x:ML, y:0.8, w:LARG, h:0.68, fontSize:30, bold:true, color:INK900, lineSpacing:34 });
}
/* carte blanche à filet 1 px — pas d'ombre : le système travaille au filet */
function carte(s, x, y, w, h, fond, filet){
  s.addShape(p.ShapeType.roundRect, { x, y, w, h, rectRadius:0.125,
    fill:{ color: fond || BLANC }, line:{ color: filet || LINE100, width:0.75 } });
}
/* pastille numérotée : aplat de la couleur de section, texte blanc */
function pastille(s, x, y, d, t, fond, encre){
  s.addShape(p.ShapeType.ellipse, { x, y, w:d, h:d, fill:{ color:fond }, line:{type:"none"} });
  txt(s, t, { x, y, w:d, h:d, align:"center", valign:"middle",
    fontSize: d>=0.6 ? 15 : (d>=0.45 ? 12.5 : 10.5), bold:true, color: encre || BLANC, lineSpacing:0 });
}
function fleche(s, x, y, w, coul){
  s.addShape(p.ShapeType.line, { x, y, w, h:0,
    line:{ color: coul || LINE300, width:1.25, endArrowType:"triangle" } });
}
function pied(s, n){
  txt(s, String(n), { x:12.35, y:6.98, w:0.5, h:0.28, align:"right",
    fontSize:9.5, bold:true, color:INK400 });
}
/* logotype francis : le point du « i » est le seul signe de marque */
function marqueFrancis(s, x, cy, taille, encre){
  const em = taille/72;
  txt(s, "francıs", { x, y:cy-0.28, w:2.2, h:0.56, valign:"middle",
    fontSize:taille, bold:true, color: encre || INK900, lineSpacing:0 });
  const d = 0.25*em, base = cy + 0.3585*em;
  s.addShape(p.ShapeType.ellipse, { x: x + 2.556*em - d/2, y: base - 0.838*em,
    w:d, h:d, fill:{ color:MARQUE }, line:{type:"none"} });
  txt(s, "Aide à l'apprentissage du français", { x: x + 3.1605*em + 0.30, y:cy-0.14, w:3.2, h:0.28,
    valign:"middle", fontSize: taille*0.46, bold:true, color: encre ? INK400 : INK400, lineSpacing:0 });
  s.addShape(p.ShapeType.line, { x: x + 3.1605*em + 0.15, y:cy-0.11, w:0, h:0.22,
    line:{ color:LINE300, width:1 } });
}

/* ── Les six sections et leur couleur de repérage ─────────────────────── */
const SEC = [
  { n:"01", c:ACIER,  bg:ACIER100,  nom:"Le mécanisme" },
  { n:"02", c:INDIGO, bg:INDIGO100, nom:"La qualité" },
  { n:"03", c:AMBRE,  bg:AMBRE100,  nom:"L'utilité" },
  { n:"04", c:TEAL,   bg:TEAL100,   nom:"Les outils" },
  { n:"05", c:FORET,  bg:FORET100,  nom:"Les aptitudes" },
  { n:"06", c:INK900, bg:PAPER200,  nom:"Le matériel" },
];

/* ══════════════════════════════════════════════════ 1 · COUVERTURE */
{
  const s = page(GREEN050);
  s.addShape(p.ShapeType.rect, { x:0, y:5.05, w:13.333, h:2.45, fill:{color:PAPER100}, line:{type:"none"} });
  s.addShape(p.ShapeType.line, { x:0, y:5.05, w:13.333, h:0, line:{ color:LINE200, width:1 } });
  surtitre(s, "Proposition de formation · Perfectionnement du personnel enseignant", ML, 1.0, GREEN800);
  txt(s, "Travailler avec Claude", { x:ML, y:1.42, w:11.5, h:1.15,
    fontSize:46, bold:true, color:INK900, lineSpacing:56 });
  txt(s, "Comprendre les modèles de langage, choisir le bon outil,\net produire du matériel pédagogique qui tient la route.",
    { x:ML, y:2.72, w:8.4, h:0.95, fontSize:17, color:INK500, lineSpacing:26 });
  marqueFrancis(s, ML, 4.35, 20);

  /* barre de parcours : les six étapes, comme dans les modules */
  const px0 = ML, pas = 1.92;
  s.addShape(p.ShapeType.line, { x:px0+0.26, y:5.85, w:pas*5, h:0, line:{ color:LINE300, width:1.25 } });
  SEC.forEach((sec,i) => {
    const cx = px0 + i*pas;
    pastille(s, cx, 5.59, 0.52, sec.n, sec.c);
    txt(s, sec.nom, { x:cx-0.42, y:6.25, w:1.36, h:0.5, align:"center",
      fontSize:11.5, bold:true, color:INK700, lineSpacing:14 });
  });
  txt(s, "Daniel Tousignant · Francisation · 2026", { x:ML, y:6.95, w:6, h:0.3,
    fontSize:11.5, bold:true, color:INK400 });
  s.addNotes("Ouverture. La barre de parcours reprend celle des modules : l'auditoire voit d'un coup les six temps et où il en est. Poser le cadre : ce n'est pas une formation sur « l'IA », mais sur un outil précis et sur ce qu'on lui demande dans notre métier.");
}

/* ══════════════════════════════════════════════════ 2 · LE PARCOURS */
{
  const s = page();
  entete(s, "Le parcours", "Six temps, trois heures");
  const det = [
    "Ce qu'est vraiment un modèle de langage — et ce qu'il n'est pas.",
    "Ce qui distingue un bon modèle d'un modèle médiocre.",
    "Où il fait gagner du temps dans le travail d'enseignant.",
    "Claude en conversation, Claude Cowork, Claude Code.",
    "L'art de la consigne : ce qui fait la différence.",
    "Produire des exercices, des fiches, des présentations.",
  ];
  /* rail vertical + six stations */
  s.addShape(p.ShapeType.line, { x:ML+0.36, y:2.0, w:0, h:4.35, line:{ color:LINE300, width:1.25 } });
  SEC.forEach((sec,i) => {
    const y = 1.85 + i*0.78;
    pastille(s, ML+0.1, y, 0.52, sec.n, sec.c);
    txt(s, sec.nom, { x:ML+0.95, y:y+0.02, w:2.5, h:0.32, fontSize:15, bold:true, color:INK900 });
    txt(s, det[i], { x:ML+3.6, y:y+0.04, w:7.9, h:0.32, fontSize:13.5, color:INK500 });
    if (i<5) s.addShape(p.ShapeType.line, { x:ML+0.95, y:y+0.62, w:10.55, h:0,
      line:{ color:LINE100, width:0.75 } });
  });
  carte(s, ML, 6.42, 11.83, 0.72, GREEN100, GREEN600);
  txt(s, "Chaque temps se termine sur quelque chose d'utilisable : une consigne, un document, une décision.",
    { x:ML+0.4, y:6.42, w:11.0, h:0.72, valign:"middle", fontSize:14, bold:true, color:GREEN800 });
  pied(s,2);
  s.addNotes("Annoncer la durée de chaque temps. Les deux premiers sont théoriques mais courts : on ne se sert pas bien d'un outil dont on ignore le fonctionnement.");
}

/* ── Intercalaire de section ──────────────────────────────────────────── */
function intercalaire(i, titre, phrase, note){
  const sec = SEC[i];
  const sombre = sec.c === INK900;
  const s = page(sombre ? INK900 : sec.bg);
  const encre = sombre ? BLANC : INK900;
  txt(s, sec.n, { x:ML, y:2.25, w:2.1, h:1.5, fontSize:88, bold:true,
    color: sombre ? BLANC : sec.c, lineSpacing:96 });
  surtitre(s, sec.nom, 2.85, 2.42, sombre ? PAPER200 : sec.c);
  txt(s, titre, { x:2.85, y:2.72, w:9.5, h:1.0, fontSize:36, bold:true, color:encre, lineSpacing:44 });
  s.addShape(p.ShapeType.line, { x:2.85, y:3.95, w:1.5, h:0,
    line:{ color: sombre ? BLANC : sec.c, width:2.5 } });
  txt(s, phrase, { x:2.85, y:4.18, w:8.6, h:0.8, fontSize:15.5,
    color: sombre ? PAPER200 : INK500, lineSpacing:22 });
  s.addNotes(note);
  return s;
}

/* ══════════════════════════════════════════════════ 3 · SECTION 01 */
intercalaire(0, "Ce qu'est un modèle de langage",
  "Avant de s'en servir, il faut savoir ce qu'il y a dans la boîte.",
  "Pas de mathématiques. Objectif : qu'à la fin de cette partie, personne ne croie que Claude « cherche sur Internet » ou « connaît » la réponse.");

/* ══════════════════════════════════════════════════ 4 · PRÉDIRE */
{
  const s = page();
  entete(s, "Le mécanisme · 1", "Une machine à prédire la suite", ACIER);
  txt(s, "Un modèle de langage ne comprend pas une question et ne va pas chercher une réponse dans une base de données. Il fait une seule chose, des milliards de fois : deviner le mot suivant.",
    { x:ML, y:1.72, w:5.55, h:1.15, fontSize:14 });
  txt(s, "À force de l'entraîner sur d'énormes quantités de textes, cette simple prédiction finit par produire du raisonnement, de la traduction, de la synthèse — parce que bien prédire la suite d'un texte difficile exige de le comprendre.",
    { x:ML, y:3.0, w:5.55, h:1.5, fontSize:14 });
  carte(s, ML, 4.75, 5.55, 1.75, GREEN100, GREEN600);
  surtitre(s, "À retenir", ML+0.38, 5.0, GREEN800, 4.8);
  txt(s, "Il ne récupère pas de l'information : il la reconstruit. C'est pour ça qu'il est brillant sur la forme et parfois faux sur le fait.",
    { x:ML+0.38, y:5.34, w:4.8, h:0.95, fontSize:13.5, bold:true, color:GREEN800 });

  const bx = 7.0;
  carte(s, bx, 1.72, 5.58, 4.78);
  txt(s, "« Je dois prendre rendez-vous chez le… »", { x:bx+0.42, y:2.02, w:4.8, h:0.34,
    fontSize:15, bold:true, color:INK900 });
  surtitre(s, "Les suites que le modèle juge plausibles", bx+0.42, 2.46, INK400, 4.8);
  const mots = [["médecin",41],["dentiste",27],["notaire",11],["coiffeur",8],["une autre suite",13]];
  mots.forEach((m,i) => {
    const y = 2.86 + i*0.66;
    txt(s, m[0], { x:bx+0.42, y:y+0.02, w:1.6, h:0.3, fontSize:13, bold:i===0, color: i===0?INK900:INK500 });
    s.addShape(p.ShapeType.roundRect, { x:bx+2.15, y:y+0.05, w:2.35, h:0.24, rectRadius:0.12,
      fill:{ color:PAPER200 }, line:{type:"none"} });
    s.addShape(p.ShapeType.roundRect, { x:bx+2.15, y:y+0.05, w:2.35*m[1]/45, h:0.24, rectRadius:0.12,
      fill:{ color: i===0 ? ACIER : "A9BFCC" }, line:{type:"none"} });
    txt(s, m[1]+" %", { x:bx+4.6, y:y+0.02, w:0.62, h:0.3, fontSize:11.5, bold:true, color:INK400 });
  });
  txt(s, "Le modèle tire dans cette distribution, mot après mot. Illustration, non une mesure.",
    { x:bx+0.42, y:6.14, w:4.8, h:0.28, fontSize:11, color:INK400 });
  pied(s,4);
  s.addNotes("Les pourcentages sont illustratifs — le dire. Ce qui compte : plusieurs suites sont plausibles et le modèle en choisit une. D'où la variation d'une réponse à l'autre.");
}

/* ══════════════════════════════════════════════════ 5 · TROIS ÉTAPES */
{
  const s = page();
  entete(s, "Le mécanisme · 2", "Trois étapes pour le fabriquer", ACIER);
  const et = [
    ["1","Pré-entraînement","On lui fait lire une quantité de texte qu'aucun humain ne pourrait lire. Il en tire la structure de la langue, des faits, des raisonnements.","Il sait parler."],
    ["2","Ajustement","On lui montre des milliers d'exemples de bonnes réponses à des demandes réelles. Il apprend à être utile plutôt que simplement plausible.","Il sait répondre."],
    ["3","Alignement","Des humains comparent ses réponses deux à deux. On renforce ce qui est honnête, prudent et clair.","Il sait se tenir."],
  ];
  et.forEach((e,i) => {
    const x = ML + i*4.06;
    carte(s, x, 2.35, 3.62, 3.5);
    pastille(s, x+1.41, 2.05, 0.6, e[0], ACIER);
    txt(s, e[1], { x:x+0.3, y:2.82, w:3.02, h:0.36, align:"center", fontSize:17, bold:true, color:INK900 });
    txt(s, e[2], { x:x+0.34, y:3.32, w:2.94, h:1.6, fontSize:13, lineSpacing:18 });
    s.addShape(p.ShapeType.line, { x:x+0.34, y:5.06, w:2.94, h:0, line:{ color:LINE100, width:0.75 } });
    txt(s, e[3], { x:x+0.34, y:5.24, w:2.94, h:0.32, align:"center", fontSize:14, bold:true, color:ACIER });
    if (i<2) fleche(s, x+3.72, 4.1, 0.28, LINE300);
  });
  carte(s, ML, 6.1, 11.83, 0.78, PAPER50, LINE100);
  txt(s, "La troisième étape explique pourquoi deux modèles nourris de textes semblables se comportent très différemment. C'est là que se joue le caractère.",
    { x:ML+0.4, y:6.1, w:11.0, h:0.78, valign:"middle", fontSize:14, color:INK700 });
  pied(s,5);
  s.addNotes("Insister sur l'alignement : c'est ce qui distingue les modèles entre eux bien plus que la taille.");
}

/* ══════════════════════════════════════════════════ 6 · MALENTENDUS */
{
  const s = page();
  entete(s, "Le mécanisme · 3", "Cinq malentendus à écarter tout de suite", ACIER);
  txt(s, "✕   Ce qu'on croit", { x:ML+0.05, y:1.72, w:5.2, h:0.3, fontSize:12.5, bold:true, color:INK400 });
  txt(s, "✓   Ce qui est vrai", { x:6.62, y:1.72, w:5.5, h:0.3, fontSize:12.5, bold:true, color:GREEN800 });
  const paires = [
    ["« Il cherche sur Internet. »","Non, sauf si on lui en donne l'outil. Autrement il répond de mémoire."],
    ["« Il ne se trompe jamais. »","Il invente parfois avec aplomb. On vérifie tout ce qui est vérifiable."],
    ["« Il retient nos échanges. »","Chaque conversation repart à zéro, sauf mémoire activée."],
    ["« Il pense comme nous. »","Il n'a ni intention ni compréhension du monde réel. Il modélise la langue."],
    ["« Il donne toujours la même réponse. »","Non. Reposez la question : la formulation changera."],
  ];
  paires.forEach((pr,i) => {
    const y = 2.15 + i*0.92;
    carte(s, ML, y, 5.42, 0.8, PAPER50, LINE100);
    txt(s, pr[0], { x:ML+0.32, y:y, w:4.85, h:0.8, valign:"middle", fontSize:13.5,
      italic:true, color:INK500 });
    carte(s, 6.55, y, 5.6, 0.8, GREEN100, GREEN600);
    txt(s, pr[1], { x:6.87, y:y, w:5.0, h:0.8, valign:"middle", fontSize:13.5,
      color:INK900, lineSpacing:17 });
    fleche(s, 6.08, y+0.4, 0.34, LINE300);
  });
  pied(s,6);
  s.addNotes("Le deuxième point est le plus important : l'assurance de l'outil n'est pas un indice de justesse. C'est le réflexe à installer avant tout le reste.");
}

/* ══════════════════════════════════════════════════ 7 · SECTION 02 */
intercalaire(1, "Qu'est-ce qui rend un modèle meilleur ?",
  "Tous savent écrire. Ils ne savent pas tous travailler.",
  "Sert à comprendre pourquoi on ne choisit pas au hasard, et pourquoi l'outil gratuit d'il y a deux ans ne donnait pas ces résultats.");

/* ══════════════════════════════════════════════════ 8 · SIX CRITÈRES */
{
  const s = page();
  entete(s, "La qualité · 1", "Six critères qui séparent les modèles", INDIGO);
  const crit = [
    ["A","Le raisonnement","Tenir une chaîne de dix étapes sans perdre le fil ni se contredire."],
    ["B","Le suivi de consigne","Faire exactement ce qui est demandé — y compris les contraintes ennuyeuses."],
    ["C","La mémoire de travail","La quantité de texte qu'il peut garder sous les yeux en une seule fois."],
    ["D","L'honnêteté","Dire « je ne sais pas » plutôt que d'inventer une référence crédible."],
    ["E","L'usage d'outils","Lire un fichier, faire un calcul, chercher, produire un document."],
    ["F","La langue","Un français d'ici, pas une traduction de l'anglais."],
  ];
  crit.forEach((c,i) => {
    const col = i%3, row = Math.floor(i/3);
    const x = ML + col*4.06, y = 1.78 + row*2.18;
    carte(s, x, y, 3.62, 1.95);
    pastille(s, x+0.34, y+0.3, 0.5, c[0], INDIGO);
    txt(s, c[1], { x:x+0.98, y:y+0.34, w:2.4, h:0.42, valign:"middle", fontSize:15, bold:true, color:INK900, lineSpacing:17 });
    txt(s, c[2], { x:x+0.34, y:y+0.98, w:2.94, h:0.85, fontSize:12.5, lineSpacing:16 });
  });
  carte(s, ML, 6.2, 11.83, 0.8, INDIGO100, INDIGO);
  txt(s, "Les palmarès publics mesurent surtout A. Dans notre métier, B et D comptent davantage : un modèle qui suit la consigne et qui avoue ses limites fait gagner plus de temps qu'un modèle brillant et fantaisiste.",
    { x:ML+0.4, y:6.2, w:11.0, h:0.8, valign:"middle", fontSize:13.5, color:INK900 });
  pied(s,8);
}

/* ══════════════════════════════════════════════════ 9 · FENÊTRE */
{
  const s = page();
  entete(s, "La qualité · 2", "La fenêtre de contexte, en clair", INDIGO);
  txt(s, "C'est tout ce que le modèle a « sous les yeux » au moment de répondre : votre demande, les documents fournis, et tout l'historique de la conversation.",
    { x:ML, y:1.72, w:4.6, h:1.15, fontSize:14 });
  txt(s, "Une grande fenêtre change la nature du travail possible. On ne colle plus un paragraphe : on dépose un programme d'études complet, quatre cahiers d'élèves et une grille d'évaluation, puis on demande une analyse croisée.",
    { x:ML, y:2.98, w:4.6, h:1.6, fontSize:14 });
  carte(s, ML, 4.82, 4.6, 1.72, WARNBG, WARNLINE);
  surtitre(s, "! Le corollaire", ML+0.34, 5.06, WARNINK, 3.9);
  txt(s, "Une conversation trop longue se dilue. Mieux vaut ouvrir une conversation neuve par tâche.",
    { x:ML+0.34, y:5.4, w:3.92, h:0.9, fontSize:13.5, bold:true, color:WARNINK });

  /* schéma : la fenêtre comme un cadre qui contient trois blocs */
  const bx = 5.75, bw = 6.83;
  carte(s, bx, 1.72, bw, 4.86, PAPER50, LINE300);
  surtitre(s, "La fenêtre de contexte", bx+0.4, 1.98, INDIGO, 5.0);
  const blocs = [
    ["Les documents que vous déposez","Programme, manuel, copies d'élèves, gabarit.",1.98,INDIGO100,INDIGO],
    ["Votre demande","La consigne du moment.",0.78,BLANC,LINE100],
    ["L'historique de la conversation","Tout ce qui a déjà été dit, des deux côtés.",0.82,BLANC,LINE100],
  ];
  let yy = 2.32;
  blocs.forEach(b => {
    carte(s, bx+0.4, yy, bw-0.8, b[2], b[3], b[4]);
    txt(s, b[0], { x:bx+0.68, y:yy+0.2, w:5.5, h:0.3, fontSize:14, bold:true, color:INK900 });
    txt(s, b[1], { x:bx+0.68, y:yy+0.53, w:5.5, h:0.3, fontSize:12.5, color:INK500 });
    if (b[2] > 1.5) {
      const ex = ["un programme d'études complet","un manuel entier et son corrigé","vingt fiches d'activité à harmoniser"];
      ex.forEach((t,j) => {
        const ey = yy + 0.88 + j*0.34;
        s.addShape(p.ShapeType.ellipse, { x:bx+0.72, y:ey+0.1, w:0.13, h:0.13, fill:{color:INDIGO}, line:{type:"none"} });
        txt(s, t, { x:bx+1.02, y:ey, w:5.2, h:0.32, fontSize:12.5, color:INK700 });
      });
    }
    yy += b[2] + 0.16;
  });
  txt(s, "Tout cela tient ensemble, en une seule fois, sans que vous ayez à résumer quoi que ce soit.",
    { x:bx+0.4, y:6.2, w:6.0, h:0.3, fontSize:12, italic:true, color:INK400 });
  pied(s,9);
  s.addNotes("C'est le critère qui change le plus la pratique. Avant, on résumait pour l'outil ; maintenant, on lui donne la source.");
}

/* ══════════════════════════════════════════════════ 10 · VITE OU RÉFLÉCHIR */
{
  const s = page();
  entete(s, "La qualité · 3", "Répondre vite ou réfléchir d'abord", INDIGO);
  const ligne = (y, nom, seq, quand, verdict, coul) => {
    carte(s, ML, y, 11.83, 2.15);
    txt(s, nom, { x:ML+0.4, y:y+0.26, w:3.0, h:0.36, fontSize:18, bold:true, color:INK900 });
    /* la séquence, en jetons reliés */
    let x = ML+0.4;
    seq.forEach((et,i) => {
      const w = et[1];
      s.addShape(p.ShapeType.roundRect, { x, y:y+0.78, w, h:0.44, rectRadius:0.1,
        fill:{ color: et[2] ? coul : BLANC }, line:{ color: et[2] ? coul : LINE300, width:1 } });
      txt(s, et[0], { x, y:y+0.78, w, h:0.44, align:"center", valign:"middle",
        fontSize:12, bold:true, color: et[2] ? BLANC : INK700, lineSpacing:0 });
      x += w;
      if (i < seq.length-1) { fleche(s, x+0.06, y+1.0, 0.24, LINE300); x += 0.36; }
    });
    surtitre(s, "Quand", ML+0.4, y+1.42, INK400, 1.2);
    txt(s, quand, { x:ML+1.6, y:y+1.4, w:5.6, h:0.6, fontSize:13, color:INK700, lineSpacing:17 });
    s.addShape(p.ShapeType.line, { x:ML+7.5, y:y+1.38, w:0, h:0.62, line:{ color:LINE100, width:0.75 } });
    surtitre(s, "Verdict", ML+7.75, y+1.42, INK400, 1.3);
    txt(s, verdict, { x:ML+7.75, y:y+1.68, w:3.6, h:0.44, fontSize:13, color:INK700, lineSpacing:17 });
  };
  ligne(1.72, "Réponse immédiate",
    [["votre demande",1.5,false],["la réponse",1.3,true]],
    "Reformuler, traduire, résumer, corriger une phrase, trouver dix synonymes.",
    "Rapide, et suffisant la plupart du temps.", INDIGO);
  ligne(4.12, "Réflexion préalable",
    [["votre demande",1.5,false],["il raisonne",1.3,false],["il se relit",1.2,false],["la réponse",1.3,true]],
    "Bâtir une progression, croiser un programme et un manuel, corriger avec une grille, trouver l'erreur dans un raisonnement.",
    "Plus lent, nettement plus juste.", INDIGO);
  carte(s, ML, 6.5, 11.83, 0.72, GREEN100, GREEN600);
  txt(s, "Le réflexe : si la tâche a plus de trois contraintes, demandez explicitement de réfléchir avant de répondre.",
    { x:ML+0.4, y:6.5, w:11.0, h:0.72, valign:"middle", fontSize:14, bold:true, color:GREEN800 });
  pied(s,10);
}

/* ══════════════════════════════════════════════════ 11 · SECTION 03 */
intercalaire(2, "Pourquoi ça nous aide vraiment",
  "Pas pour enseigner à notre place. Pour libérer le temps qui n'est pas de l'enseignement.",
  "Point sensible : nommer d'emblée la crainte du remplacement, puis la déplacer.");

/* ══════════════════════════════════════════════════ 12 · TRAVAIL INVISIBLE */
{
  const s = page();
  entete(s, "L'utilité · 1", "Le travail qui n'est pas devant la classe", AMBRE);
  txt(s, "Une bonne partie du métier se passe ailleurs qu'en classe. C'est précisément ce travail-là que l'outil sait accompagner.",
    { x:ML, y:1.7, w:11.7, h:0.35, fontSize:14.5 });
  /* six satellites autour d'un noyau */
  const cx = 6.666, cy = 4.35;
  s.addShape(p.ShapeType.ellipse, { x:cx-0.95, y:cy-0.95, w:1.9, h:1.9,
    fill:{ color:AMBRE100 }, line:{ color:AMBRE, width:1.25 } });
  txt(s, "Hors\nclasse", { x:cx-0.9, y:cy-0.9, w:1.8, h:1.8, align:"center", valign:"middle",
    fontSize:17, bold:true, color:AMBRE, lineSpacing:22 });
  const t = [
    ["Préparer","Bâtir une séquence, découper une notion, trouver dix exemples plutôt que trois.",0],
    ["Adapter","Reprendre le même contenu à trois niveaux, pour trois profils d'élèves.",1],
    ["Corriger","Repérer les erreurs récurrentes d'un groupe, rédiger une rétroaction.",2],
    ["Différencier","Le renfort pour l'un, l'enrichissement pour l'autre.",3],
    ["Documenter","Le plan, la grille, le compte rendu, la lettre aux parents.",4],
    ["Explorer","Se faire expliquer une notion, tester une idée avant de l'essayer.",5],
  ];
  const pos = [[ML,2.3],[ML,3.7],[ML,5.1],[8.24,2.3],[8.24,3.7],[8.24,5.1]];
  t.forEach((it,i) => {
    const [x,y] = pos[i], gauche = i<3;
    carte(s, x, y, 4.34, 1.24);
    txt(s, it[0], { x:x+0.32, y:y+0.2, w:3.7, h:0.32, fontSize:15.5, bold:true, color:AMBRE });
    txt(s, it[1], { x:x+0.32, y:y+0.56, w:3.75, h:0.6, fontSize:12.5, lineSpacing:16 });
    const xa = gauche ? x+4.34 : cx+0.95;
    const wa = gauche ? (cx-0.95)-(x+4.34) : x-(cx+0.95);
    s.addShape(p.ShapeType.line, { x:xa, y:y+0.62, w:wa, h: (cy-(y+0.62)),
      line:{ color:LINE300, width:1 } });
  });
  pied(s,12);
  s.addNotes("Faire nommer par le groupe, avant d'afficher, ce qui leur prend le plus de temps hors classe. Les réponses tombent presque toujours dans ces six cases.");
}

/* ══════════════════════════════════════════════════ 13 · CONFIER / GARDER */
{
  const s = page();
  entete(s, "L'utilité · 2", "La ligne de partage", AMBRE);
  txt(s, "L'outil produit. L'enseignant décide. Cette ligne ne bouge pas.",
    { x:ML, y:1.7, w:11.7, h:0.34, fontSize:14.5, bold:true, color:INK900 });
  const bloc = (x, glyphe, titre, fond, filet, encre, liste, note) => {
    carte(s, x, 2.18, 5.42, 4.2, fond, filet);
    txt(s, glyphe, { x:x+0.36, y:2.44, w:0.5, h:0.42, fontSize:18, bold:true, color:encre, lineSpacing:0 });
    txt(s, titre, { x:x+0.92, y:2.44, w:4.2, h:0.42, valign:"middle", fontSize:19, bold:true, color:encre });
    liste.forEach((l,i) => {
      const y = 3.1 + i*0.56;
      s.addShape(p.ShapeType.line, { x:x+0.36, y:y, w:4.7, h:0, line:{ color:LINE100, width:0.75 } });
      txt(s, l, { x:x+0.36, y:y+0.1, w:4.7, h:0.4, fontSize:13.5, color:INK900 });
    });
    txt(s, note, { x:x+0.36, y:5.92, w:4.7, h:0.34, fontSize:12.5, italic:true, color:INK500 });
  };
  bloc(ML, "→", "On lui confie", BLANC, LINE100, INK900,
    ["Le premier jet, jamais le dernier","La variante, la déclinaison, le doublon","La mise en forme et la mise en page","La relecture et la chasse aux oublis","Le brassage d'idées quand on sèche"],
    "Tout ce qui est long sans être délicat.");
  bloc(7.16, "★", "On garde", GREEN100, GREEN600, GREEN800,
    ["Le choix de ce qu'on enseigne","Le jugement sur l'élève","La relation et le climat de classe","La décision d'évaluation","La responsabilité de ce qu'on distribue"],
    "Tout ce qui engage notre jugement professionnel.");
  s.addShape(p.ShapeType.line, { x:6.58, y:2.18, w:0, h:4.2, line:{ color:LINE300, width:1.25 } });
  carte(s, ML, 6.56, 11.83, 0.62, PAPER50, LINE100);
  txt(s, "Rien ne sort de la classe sans avoir été relu par quelqu'un qui en répond.",
    { x:ML+0.4, y:6.56, w:11.0, h:0.62, valign:"middle", fontSize:13.5, bold:true, color:INK700 });
  pied(s,13);
}

/* ══════════════════════════════════════════════════ 14 · SECTION 04 */
intercalaire(3, "Trois façons de travailler avec Claude",
  "Le même modèle, trois postes de travail très différents.",
  "Cœur pratique de la formation. La plupart des gens ne connaissent que la conversation.");

/* ══════════════════════════════════════════════════ 15 · SPECTRE */
{
  const s = page();
  entete(s, "Les outils · 1", "Le même moteur, trois postes de travail", TEAL);
  const outils = [
    ["Claude","en conversation","Une discussion. Vous écrivez, il répond. Vous copiez le résultat.","Réfléchir, rédiger, expliquer, corriger un texte.","Rien à installer","Le résultat reste dans la fenêtre"],
    ["Claude Cowork","le collègue de bureau","Il travaille dans vos dossiers et vous rend des fichiers finis.","Produire des documents, traiter un lot, monter un dossier.","Aucune compétence technique","Il agit : on relit avant de diffuser"],
    ["Claude Code","l'atelier","Il pilote votre ordinateur : fichiers, scripts, sites, conversions.","Fabriquer et maintenir du matériel à grande échelle.","Puissance maximale","Demande de la méthode"],
  ];
  outils.forEach((o,i) => {
    const x = ML + i*4.06;
    carte(s, x, 1.72, 3.62, 4.0);
    txt(s, o[0], { x:x+0.34, y:2.0, w:3.0, h:0.36, fontSize:18, bold:true, color:INK900 });
    txt(s, o[1], { x:x+0.34, y:2.38, w:3.0, h:0.3, fontSize:13, bold:true, color:TEAL });
    txt(s, o[2], { x:x+0.34, y:2.78, w:2.94, h:1.0, fontSize:12.5, lineSpacing:16 });
    s.addShape(p.ShapeType.line, { x:x+0.34, y:3.9, w:2.94, h:0, line:{ color:LINE100, width:0.75 } });
    surtitre(s, "Pour", x+0.34, 4.02, INK400, 2.9);
    txt(s, o[3], { x:x+0.34, y:4.3, w:2.94, h:0.85, fontSize:12.5, color:INK900, lineSpacing:16 });
    txt(s, "+  " + o[4], { x:x+0.34, y:5.02, w:3.0, h:0.28, fontSize:12, bold:true, color:GREEN800 });
    txt(s, "!  " + o[5], { x:x+0.34, y:5.3, w:3.0, h:0.4, fontSize:12, color:WARNINK, lineSpacing:15 });
  });
  /* axe : de quoi vous repartez */
  s.addShape(p.ShapeType.line, { x:ML+1.5, y:6.05, w:8.6, h:0,
    line:{ color:LINE300, width:1.25, endArrowType:"triangle" } });
  ["un texte","un fichier","une collection"].forEach((t,i) => {
    const x = ML + i*4.06 + 1.81;
    s.addShape(p.ShapeType.ellipse, { x:x-0.09, y:5.96, w:0.18, h:0.18, fill:{color:TEAL}, line:{type:"none"} });
    txt(s, t, { x:x-1.3, y:6.24, w:2.6, h:0.3, align:"center", fontSize:13.5, bold:true, color:TEAL });
  });
  surtitre(s, "Ce dont vous repartez", ML, 6.05, INK400, 1.4);
  carte(s, ML, 6.68, 11.83, 0.6, PAPER50, LINE100);
  txt(s, "La conversation est un collègue au téléphone ; Cowork, un collègue assis à votre bureau ; Code, un collègue à l'atelier, avec les machines.",
    { x:ML+0.4, y:6.68, w:11.0, h:0.6, valign:"middle", fontSize:13, italic:true, color:INK500 });
  pied(s,15);
}

/* ══════════════════════════ 16-18 · CHAQUE OUTIL EN DÉTAIL */
function detail(num, nom, sous, quoi, exemples, piege, note){
  const s = page();
  entete(s, "Les outils · " + (num-14), nom, TEAL);
  txt(s, sous, { x:ML, y:1.52, w:11.7, h:0.32, fontSize:14, bold:true, color:TEAL });
  txt(s, quoi, { x:ML, y:2.1, w:5.3, h:2.5, fontSize:14 });
  carte(s, ML, 4.85, 5.3, 1.62, WARNBG, WARNLINE);
  surtitre(s, "! Le piège", ML+0.34, 5.08, WARNINK, 4.6);
  txt(s, piege, { x:ML+0.34, y:5.4, w:4.62, h:0.9, fontSize:13, bold:true, color:WARNINK });
  carte(s, 6.55, 2.1, 6.03, 4.37, PAPER50, LINE300);
  surtitre(s, "En classe, concrètement", 6.95, 2.38, TEAL, 5.2);
  exemples.forEach((e,i) => {
    const y = 2.78 + i*0.86;
    carte(s, 6.95, y, 5.23, 0.72, BLANC, LINE100);
    pastille(s, 7.14, y+0.16, 0.4, String(i+1), TEAL);
    txt(s, e, { x:7.68, y:y, w:4.35, h:0.72, valign:"middle", fontSize:12.5, color:INK900, lineSpacing:16 });
  });
  pied(s, num);
  s.addNotes(note);
}
detail(16, "Claude en conversation", "Le collègue au bout du fil : il vous répond, vous décidez.",
  "C'est la porte d'entrée, dans le navigateur ou l'application. On dépose une question ou un document, on obtient une réponse, on discute, on affine.\n\nOn peut y joindre des fichiers, y créer des Projets qui gardent le contexte d'un cours, et lui faire produire des pages interactives que les élèves peuvent utiliser telles quelles.",
  ["Faire expliquer une notion de grammaire de quatre façons différentes",
   "Transformer un texte authentique en texte de niveau 4",
   "Rédiger une rétroaction bienveillante à partir de la copie d'un élève",
   "Se faire critiquer une consigne avant de la donner"],
  "Le résultat vit dans la fenêtre. Ce qui n'est pas copié ailleurs est perdu.",
  "Faire ouvrir un Projet en direct pendant l'atelier : c'est la fonction la plus rentable et la moins connue.");
detail(17, "Claude Cowork", "Le collègue assis à votre bureau : il ouvre vos dossiers et rend des fichiers.",
  "Ici, on ne copie plus rien. On lui donne accès à un dossier de travail et il produit directement les documents : Word, PowerPoint, Excel, PDF.\n\nIl travaille en plusieurs étapes, sur un lot complet, et rend compte de ce qu'il a fait. On lui parle en français ordinaire — aucune compétence technique n'est requise.",
  ["Reprendre vingt fiches d'activité au même gabarit visuel",
   "Monter le PowerPoint d'une séquence à partir du plan de cours",
   "Compiler les résultats d'un groupe dans un tableau lisible",
   "Produire le cahier de l'élève et le corrigé de l'enseignant d'un seul coup"],
  "Il agit pour vrai sur vos fichiers. On travaille sur une copie, et on relit avant de diffuser.",
  "C'est l'outil qui convertit le plus d'enseignants : le résultat est un fichier qu'on peut imprimer, pas un texte à recopier.");
detail(18, "Claude Code", "L'atelier : la fabrication en série et sur mesure.",
  "Malgré son nom, il ne sert pas qu'à programmer. C'est un assistant qui a la main sur l'ordinateur : il lit et écrit des fichiers, lance des programmes, convertit des formats, publie des pages web.\n\nC'est l'outil du matériel produit à grande échelle et maintenu dans le temps : une bibliothèque d'activités, un portail pour les élèves, une chaîne de production.",
  ["Fabriquer onze modules interactifs bâtis sur le même gabarit",
   "Générer les enregistrements audio de tous les dialogues",
   "Corriger une coquille présente dans deux cents fichiers d'un coup",
   "Publier un portail où les élèves retrouvent tout le matériel"],
  "Il faut de la méthode : travailler par étapes, vérifier, et savoir revenir en arrière.",
  "À présenter comme un horizon, pas comme un prérequis. Un ou deux enseignants par centre y viendront — ce sont eux qui outilleront les autres.");

/* ══════════════════════════════════════════════════ 19 · ARBRE DE DÉCISION */
{
  const s = page();
  entete(s, "Les outils · 4", "Lequel choisir ? Trois questions", TEAL);
  const q = [
    ["Ce que je veux, est-ce un texte ?","À lire, à comprendre, à reformuler.","Claude en conversation"],
    ["Le résultat doit-il être un document livrable ?","Un Word, un PowerPoint, un tableau, un PDF prêt à imprimer.","Claude Cowork"],
    ["Est-ce que je fabrique la même chose vingt fois ?","Une collection, un portail, une chaîne à maintenir dans le temps.","Claude Code"],
  ];
  q.forEach((it,i) => {
    const y = 1.85 + i*1.5;
    carte(s, ML, y, 6.4, 1.24);
    pastille(s, ML+0.3, y+0.35, 0.54, String(i+1), TEAL);
    txt(s, it[0], { x:ML+1.02, y:y+0.24, w:5.1, h:0.34, fontSize:15.5, bold:true, color:INK900 });
    txt(s, it[1], { x:ML+1.02, y:y+0.64, w:5.1, h:0.4, fontSize:12.5, color:INK500 });
    /* branche « oui » vers la pastille de résultat */
    s.addShape(p.ShapeType.line, { x:ML+6.4, y:y+0.62, w:0.55, h:0,
      line:{ color:TEAL, width:1.25, endArrowType:"triangle" } });
    txt(s, "oui", { x:ML+6.42, y:y+0.28, w:0.5, h:0.28, align:"center", fontSize:11, bold:true, color:TEAL });
    s.addShape(p.ShapeType.roundRect, { x:ML+7.05, y:y+0.34, w:3.6, h:0.58, rectRadius:0.29,
      fill:{ color:TEAL100 }, line:{ color:TEAL, width:1 } });
    txt(s, it[2], { x:ML+7.05, y:y+0.34, w:3.6, h:0.58, align:"center", valign:"middle",
      fontSize:13.5, bold:true, color:TEAL, lineSpacing:0 });
    /* branche « non » : on descend */
    if (i<2) {
      s.addShape(p.ShapeType.line, { x:ML+0.57, y:y+1.24, w:0, h:0.26,
        line:{ color:LINE300, width:1.25, endArrowType:"triangle" } });
      txt(s, "non", { x:ML+0.75, y:y+1.26, w:0.6, h:0.24, fontSize:11, bold:true, color:INK400 });
    }
  });
  carte(s, ML, 6.4, 11.83, 0.78, GREEN100, GREEN600);
  txt(s, "En cas de doute : commencer dans la conversation. On y met la pensée au clair, puis on transporte la consigne au bon endroit.",
    { x:ML+0.4, y:6.4, w:11.0, h:0.78, valign:"middle", fontSize:14, bold:true, color:GREEN800 });
  pied(s,19);
}

/* ══════════════════════════════════════════════════ 20 · SECTION 05 */
intercalaire(4, "Développer ses aptitudes",
  "L'écart entre un résultat décevant et un résultat excellent tient presque toujours à la consigne.",
  "Message central : ce n'est pas l'outil qui progresse d'une séance à l'autre, c'est l'utilisateur.");

/* ══════════════════════════════════════════════════ 21 · ANATOMIE */
{
  const s = page();
  entete(s, "Les aptitudes · 1", "Anatomie d'une bonne consigne", FORET);
  /* la consigne, en cinq segments repérés */
  const seg = [
    ["Le rôle","« Tu es enseignant de francisation au niveau 4, auprès d'adultes. »",2.15],
    ["Le contexte","Qui sont les élèves, où on en est dans la séquence, ce qui a déjà été vu.",2.35],
    ["La tâche","Un verbe précis et une quantité : rédige, compare, produis douze items.",2.35],
    ["Les contraintes","Le niveau de langue, la longueur, ce qu'il faut éviter, le format attendu.",2.45],
    ["L'exemple","Un item modèle vaut mieux qu'un paragraphe d'explications.",2.53],
  ];
  let x = ML;
  seg.forEach((g,i) => {
    s.addShape(p.ShapeType.roundRect, { x, y:1.78, w:g[2], h:0.72, rectRadius:0.1,
      fill:{ color: i%2 ? FORET100 : BLANC }, line:{ color:FORET, width:1 } });
    txt(s, String(i+1), { x:x+0.14, y:1.9, w:0.3, h:0.3, fontSize:12, bold:true, color:FORET, lineSpacing:0 });
    txt(s, g[0], { x, y:1.78, w:g[2], h:0.72, align:"center", valign:"middle",
      fontSize:14, bold:true, color:FORET, lineSpacing:0 });
    x += g[2] + 0.08;
  });
  surtitre(s, "Une consigne complète, de gauche à droite", ML, 2.62, INK400, 8);
  /* détail de chaque segment */
  seg.forEach((g,i) => {
    const y = 3.1 + i*0.72;
    pastille(s, ML, y+0.06, 0.44, String(i+1), FORET);
    txt(s, g[0], { x:ML+0.66, y:y+0.1, w:2.1, h:0.36, fontSize:15, bold:true, color:INK900 });
    txt(s, g[1], { x:ML+2.9, y:y+0.1, w:8.6, h:0.4, fontSize:13.5, color:INK500 });
    if (i<4) s.addShape(p.ShapeType.line, { x:ML+0.66, y:y+0.6, w:10.85, h:0, line:{ color:LINE100, width:0.75 } });
  });
  carte(s, ML, 6.72, 11.83, 0.6, GREEN100, GREEN600);
  txt(s, "Et surtout : une consigne se travaille en plusieurs tours. La première réponse sert à ajuster la deuxième demande.",
    { x:ML+0.4, y:6.72, w:11.0, h:0.6, valign:"middle", fontSize:13.5, bold:true, color:GREEN800 });
  pied(s,21);
  s.addNotes("Faire l'exercice en direct : demander au groupe une consigne spontanée, la faire tourner, puis la reconstruire avec les cinq segments et comparer les deux résultats.");
}

/* ══════════════════════════════════════════════════ 22 · AVANT / APRÈS */
{
  const s = page();
  entete(s, "Les aptitudes · 2", "La même demande, deux résultats", FORET);
  carte(s, ML, 1.78, 5.42, 4.6, PAPER50, LINE300);
  txt(s, "✕   Avant", { x:ML+0.38, y:2.04, w:4.6, h:0.32, fontSize:14, bold:true, color:INK400 });
  txt(s, "« Fais-moi un exercice sur le passé composé. »",
    { x:ML+0.38, y:2.5, w:4.66, h:0.8, fontSize:15, italic:true, color:INK700, lineSpacing:21 });
  s.addShape(p.ShapeType.line, { x:ML+0.38, y:3.45, w:4.66, h:0, line:{ color:LINE300, width:0.75 } });
  surtitre(s, "Ce qu'on obtient", ML+0.38, 3.62, INK400, 4.6);
  txt(s, "Dix phrases à trous, hors contexte, d'un niveau imprévisible, avec des verbes qui ne servent à personne. On recommence.",
    { x:ML+0.38, y:3.92, w:4.66, h:1.4, fontSize:13.5, color:INK700 });
  fleche(s, 6.32, 4.05, 0.44, FORET);
  carte(s, 7.16, 1.78, 5.42, 4.6, FORET100, FORET);
  txt(s, "✓   Après", { x:7.54, y:2.04, w:4.6, h:0.32, fontSize:14, bold:true, color:FORET });
  txt(s, "« Mes élèves sont des adultes en francisation, niveau 4. Ils travaillent la prise de rendez-vous médical. Écris douze phrases au passé composé, au « je » et au « nous », avec des verbes de la vie courante. Une phrase par ligne, l'infinitif entre parenthèses. Pas de verbes pronominaux : on ne les a pas vus. »",
    { x:7.54, y:2.5, w:4.66, h:2.6, fontSize:12.5, italic:true, color:INK900, lineSpacing:17 });
  s.addShape(p.ShapeType.line, { x:7.54, y:5.2, w:4.66, h:0, line:{ color:FORET, width:0.75 } });
  surtitre(s, "Ce qu'on obtient", 7.54, 5.36, FORET, 4.6);
  txt(s, "Un exercice utilisable tel quel, dans le thème de la séquence, au bon niveau.",
    { x:7.54, y:5.66, w:4.66, h:0.6, fontSize:13.5, bold:true, color:FORET });
  carte(s, ML, 6.55, 11.83, 0.62, PAPER50, LINE100);
  txt(s, "La deuxième consigne prend trente secondes de plus à écrire. Elle épargne trois allers-retours.",
    { x:ML+0.4, y:6.55, w:11.0, h:0.62, valign:"middle", fontSize:13.5, bold:true, color:INK700 });
  pied(s,22);
}

/* ══════════════════════════════════════════════════ 23 · LA BOUCLE */
{
  const s = page();
  entete(s, "Les aptitudes · 3", "Quatre réflexes, et ils tournent en boucle", FORET);
  const r = [
    ["Donner la matière","Ne pas décrire un document : le déposer. Le programme, le manuel, la copie de l'élève."],
    ["Demander la critique","« Qu'est-ce qui cloche dans cet exercice ? » — avant de le distribuer."],
    ["Corriger en cours de route","Ne pas tout recommencer : dire ce qui ne va pas et faire reprendre."],
    ["Vérifier ce qui compte","Les faits, les dates, les références, les règles. Le reste, on le lit."],
  ];
  const pos = [[ML,1.9],[7.16,1.9],[7.16,4.3],[ML,4.3]];
  r.forEach((it,i) => {
    const [x,y] = pos[i];
    carte(s, x, y, 5.42, 2.05);
    pastille(s, x+0.36, y+0.32, 0.5, String(i+1), FORET);
    txt(s, it[0], { x:x+1.0, y:y+0.34, w:4.0, h:0.46, valign:"middle", fontSize:16.5, bold:true, color:INK900 });
    txt(s, it[1], { x:x+0.36, y:y+1.02, w:4.7, h:0.85, fontSize:13, lineSpacing:17 });
  });
  /* les quatre flèches du cycle */
  s.addShape(p.ShapeType.line, { x:6.25, y:2.9,  w:0.83, h:0,    line:{ color:FORET, width:1.5, endArrowType:"triangle" } });
  s.addShape(p.ShapeType.line, { x:9.87, y:3.99, w:0,    h:0.32, line:{ color:FORET, width:1.5, endArrowType:"triangle" } });
  s.addShape(p.ShapeType.line, { x:6.25, y:5.3,  w:0.83, h:0,    line:{ color:FORET, width:1.5, beginArrowType:"triangle" } });
  s.addShape(p.ShapeType.line, { x:3.46, y:3.99, w:0,    h:0.32, line:{ color:FORET, width:1.5, beginArrowType:"triangle" } });
  carte(s, ML, 6.52, 11.83, 0.66, FORET100, FORET);
  txt(s, "On repasse par la boucle autant de fois qu'il le faut. C'est normal, et c'est là que la qualité se gagne.",
    { x:ML+0.4, y:6.52, w:11.0, h:0.66, valign:"middle", fontSize:13.5, bold:true, color:FORET });
  pied(s,23);
}

/* ══════════════════════════════════════════════════ 24 · SECTION 06 */
intercalaire(5, "Développer du matériel",
  "De l'exercice unique à la collection cohérente.",
  "Partie la plus attendue. Montrer du vrai matériel produit, pas des captures de démonstration.");

/* ══════════════════════════════════════════════════ 25 · L'ESCALIER */
{
  const s = page();
  entete(s, "Le matériel · 1", "Trois échelles de production", INK900);
  txt(s, "Le même outil, trois ambitions. Chaque marche suppose la précédente — et rapporte davantage.",
    { x:ML, y:1.66, w:11.7, h:0.34, fontSize:14.5 });
  const prod = [
    ["Le quotidien","Exercices, textes adaptés, listes de vocabulaire, corrigés, grilles.","Une conversation, quinze minutes.",1.9,ACIER,ACIER100],
    ["Le document","Cahier de l'élève, présentation, fiche imprimable, plan de cours complet.","Cowork, une avant-midi.",2.55,TEAL,TEAL100],
    ["Le dispositif","Une séquence entière : activités interactives, audio, suivi, portail élève.","Code, un chantier suivi.",3.2,FORET,FORET100],
  ];
  prod.forEach((pr,i) => {
    const x = ML + i*4.06;
    const h = pr[3], y = 5.7 - h;
    carte(s, x, y, 3.62, h, pr[5], pr[4]);
    txt(s, pr[0], { x:x+0.34, y:y+0.26, w:3.0, h:0.4, fontSize:19, bold:true, color:pr[4] });
    txt(s, pr[1], { x:x+0.34, y:y+0.78, w:2.94, h:1.05, fontSize:12.5, color:INK900, lineSpacing:16 });
    txt(s, pr[2], { x:x+0.34, y:h > 2 ? y+h-0.6 : y+h-0.55, w:2.94, h:0.42,
      fontSize:12.5, bold:true, color:pr[4], lineSpacing:16 });
    /* marche */
    s.addShape(p.ShapeType.line, { x:x, y:5.78, w:3.62, h:0, line:{ color:pr[4], width:2.5 } });
    txt(s, "Échelle " + (i+1), { x:x, y:5.86, w:3.62, h:0.28, align:"center",
      fontSize:11.5, bold:true, color:INK400 });
  });
  carte(s, ML, 6.35, 11.83, 0.85, GREEN100, GREEN600);
  txt(s, "La vraie économie n'est pas le premier document — c'est le deuxième, et les dix-huit suivants.",
    { x:ML+0.5, y:6.35, w:10.8, h:0.85, valign:"middle", fontSize:17, bold:true, color:GREEN800 });
  pied(s,25);
  s.addNotes("Ce qui change l'échelle, c'est la cohérence d'une collection : un gabarit décidé une fois, appliqué partout.");
}

/* ══════════════════════════════════════════════════ 26 · CAS RÉEL */
{
  const s = page();
  entete(s, "Le matériel · 2", "Un cas réel : cette bibliothèque-ci", INK900);
  const stats = [["11","modules complets"],["16","séances par module"],["8","niveaux couverts"],["100 %","contenu original"]];
  stats.forEach((st,i) => {
    const x = ML + i*3.0;
    carte(s, x, 1.72, 2.72, 1.6);
    txt(s, st[0], { x:x, y:1.9, w:2.72, h:0.8, align:"center", fontSize:40, bold:true, color:INK900, lineSpacing:46 });
    txt(s, st[1], { x:x, y:2.78, w:2.72, h:0.36, align:"center", fontSize:12.5, bold:true, color:INK400 });
  });
  /* onze carrés : un par module */
  surtitre(s, "Onze modules, un seul gabarit", ML, 3.6, INK400, 6);
  for (let i=0;i<11;i++){
    s.addShape(p.ShapeType.roundRect, { x:ML + i*0.42, y:3.9, w:0.32, h:0.32, rectRadius:0.06,
      fill:{ color:GREEN600 }, line:{type:"none"} });
  }
  txt(s, "Le douzième coûte le même effort que le deuxième.", { x:ML+5.0, y:3.92, w:6.5, h:0.3,
    fontSize:13, italic:true, color:INK500 });
  const lec = [
    ["Le gabarit d'abord","Une seule structure décidée au départ, puis appliquée à tous les modules."],
    ["Le contenu inventé","Le manuel du commerce sert de modèle de progression, jamais de source à recopier."],
    ["L'enseignant décide","Chaque scénario, chaque personnage, chaque intention pédagogique vient de nous."],
  ];
  lec.forEach((l,i) => {
    const x = ML + i*4.06;
    carte(s, x, 4.55, 3.62, 1.68, PAPER50, LINE100);
    txt(s, l[0], { x:x+0.32, y:4.78, w:3.0, h:0.34, fontSize:15, bold:true, color:GREEN800 });
    txt(s, l[1], { x:x+0.32, y:5.18, w:3.0, h:0.9, fontSize:12.5, lineSpacing:16 });
  });
  carte(s, ML, 6.42, 11.83, 0.76, PAPER50, LINE100);
  txt(s, "Aucun de ces chiffres n'aurait été atteignable à la main. Aucun n'aurait tenu debout sans un enseignant derrière.",
    { x:ML+0.4, y:6.42, w:11.0, h:0.76, valign:"middle", fontSize:14, bold:true, color:INK700 });
  pied(s,26);
  s.addNotes("Chiffres à revalider avant la présentation. Montrer un module en direct si le réseau le permet.");
}

/* ══════════════════════════════════════════════════ 27 · VIGILANCE */
{
  const s = page();
  entete(s, "Le matériel · 3", "Ce à quoi on fait attention", INK900);
  const v = [
    ["Les renseignements personnels","Jamais de nom d'élève, de dossier, de coordonnées. On travaille avec des pseudonymes ou des extraits anonymisés."],
    ["La Loi 25","Les données sortent de l'établissement. Vérifier ce que la direction autorise avant d'y déposer quoi que ce soit d'institutionnel."],
    ["Le droit d'auteur","Un manuel sert de modèle de structure, pas de réservoir à recopier. Le contenu qu'on distribue doit être le nôtre."],
    ["La justesse","Tout ce qui est vérifiable se vérifie : les faits, les règles, les références, les niveaux de langue."],
  ];
  v.forEach((it,i) => {
    const col = i%2, row = Math.floor(i/2);
    const x = ML + col*6.05, y = 1.78 + row*2.2;
    carte(s, x, y, 5.72, 1.95, WARNBG, WARNLINE);
    pastille(s, x+0.36, y+0.3, 0.48, "!", WARNLINE);
    txt(s, it[0], { x:x+0.98, y:y+0.32, w:4.4, h:0.44, valign:"middle", fontSize:16, bold:true, color:WARNINK });
    txt(s, it[1], { x:x+0.36, y:y+0.94, w:5.0, h:0.9, fontSize:13, color:INK900, lineSpacing:17 });
  });
  carte(s, ML, 6.32, 11.83, 0.86, GREEN100, GREEN600);
  txt(s, "Une règle simple et suffisante : rien qui permette d'identifier un élève ne sort de l'établissement.",
    { x:ML+0.5, y:6.32, w:10.8, h:0.86, valign:"middle", fontSize:16, bold:true, color:GREEN800 });
  pied(s,27);
}

/* ══════════════════════════════════════════════════ 28 · LES ATELIERS */
{
  const s = page();
  entete(s, "La proposition", "Trois ateliers, trois heures chacun", GREEN800);
  const at = [
    ["Atelier 1","Comprendre et converser","Le mécanisme, les malentendus, l'art de la consigne. Chacun repart avec trois consignes qui fonctionnent pour son cours.","Aucun prérequis"],
    ["Atelier 2","Produire du matériel","Cowork en main : cahier de l'élève, présentation, corrigé. Chacun repart avec un document fini.","Avoir suivi l'atelier 1"],
    ["Atelier 3","Bâtir une collection","Gabarit, cohérence, production en série, mise en ligne. Pour ceux qui veulent outiller leur équipe.","Volontaires"],
  ];
  s.addShape(p.ShapeType.line, { x:ML+1.81, y:2.15, w:8.12, h:0, line:{ color:LINE300, width:1.5 } });
  at.forEach((a,i) => {
    const x = ML + i*4.06;
    pastille(s, x+1.53, 1.89, 0.56, String(i+1), GREEN600);
    carte(s, x, 2.72, 3.62, 3.35);
    surtitre(s, a[0], x+0.34, 2.98, INK400, 3.0);
    txt(s, a[1], { x:x+0.34, y:3.26, w:3.0, h:0.72, fontSize:17, bold:true, color:INK900, lineSpacing:22 });
    txt(s, a[2], { x:x+0.34, y:4.1, w:2.94, h:1.5, fontSize:13, lineSpacing:17 });
    s.addShape(p.ShapeType.line, { x:x+0.34, y:5.6, w:2.94, h:0, line:{ color:LINE100, width:0.75 } });
    txt(s, a[3], { x:x+0.34, y:5.72, w:2.94, h:0.3, fontSize:12.5, bold:true, color:GREEN800 });
  });
  carte(s, ML, 6.32, 11.83, 0.86, GREEN100, GREEN600);
  txt(s, "Chaque atelier se termine sur du matériel utilisable dès le lendemain. Rien de théorique qui ne serve pas.",
    { x:ML+0.5, y:6.32, w:10.8, h:0.86, valign:"middle", fontSize:16, bold:true, color:GREEN800 });
  pied(s,28);
}

/* ══════════════════════════════════════════════════ 29 · POUR FINIR */
{
  const s = page(GREEN050);
  s.addShape(p.ShapeType.rect, { x:0, y:5.35, w:13.333, h:2.15, fill:{color:PAPER100}, line:{type:"none"} });
  s.addShape(p.ShapeType.line, { x:0, y:5.35, w:13.333, h:0, line:{ color:LINE200, width:1 } });
  surtitre(s, "Pour finir", ML, 1.35, GREEN800);
  txt(s, "L'outil ne remplace pas le jugement.\nIl lui laisse de la place.",
    { x:ML, y:1.75, w:11.5, h:1.7, fontSize:38, bold:true, color:INK900, lineSpacing:50 });
  txt(s, "Ce qu'un enseignant sait — de sa matière, de ses élèves, de ce qui bloque le mardi matin — reste ce qu'il y a de plus rare. Le reste peut être délégué.",
    { x:ML, y:3.65, w:8.6, h:0.9, fontSize:16, color:INK500, lineSpacing:24 });
  marqueFrancis(s, ML, 5.95, 20);
  txt(s, "Daniel Tousignant · tousignantd@gmail.com", { x:ML, y:6.55, w:6, h:0.3,
    fontSize:12.5, bold:true, color:INK400 });
  s.addNotes("Terminer sur une question ouverte : qu'est-ce que chacun aimerait ne plus jamais avoir à faire à la main ?");
}

p.writeFile({ fileName: process.argv[2] }).then(f => console.log("écrit :", f));
