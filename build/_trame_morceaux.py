# Engendré depuis la première mise au point, le 7 septembre 2026.
JETONS = r'''  /* ═══ ESSAI : le classeur au système de design « Trame » ═══
     Les noms de jetons du classeur ne changent pas — ce sont les VALEURS
     qui viennent de systemes-design/trame/tokens.css. Tout le reste de la
     feuille continue de fonctionner, et le retour en arrière tient dans
     ce seul bloc. Ce qu'aucun jeton ne peut dire (les polices de lecture,
     les angles, l'absence d'ombre) est écrit dans la surcouche, plus bas.
     ══════════════════════════════════════════════════════════════════ */
  :root{
    /* Action : en Trame, le bouton principal est en encre, jamais en couleur.
       L'indigo — la « chaîne » — porte les liens et le focus. */
    --accent:#14161F;      --accent-soft:#E4E6F3;  --accent-ink:#1E2A78;
    /* Le champ de marque : le bandeau de tête, une seule fois par écran. */
    --surface-band:#E9A63B;
    --ink-900:#14161F; --ink-700:#3B3D46; --ink-500:#4A4C55; --ink-400:#6A6B6E;
    --surface-page:#F4EEE1; --surface-card:#FBF8F1; --surface-sunken:#F1EADB;
    --paper-200:#EAE2D0;
    --border:#DDD4C2; --border-firm:#C4B99F; --border-tint:rgba(20,22,31,.16);
    /* Trame n'a pas cinq couleurs de section : le sur-titre est en ocre-texte,
       la seule forme d'ocre qui se lise, et les formats redeviennent neutres. */
    --acier-600:#6A6B6E; --acier-100:#EAE2D0;
    --ambre-700:#8A5A0A; --ambre-100:#F6E6C8;
    --teal-700:#6A6B6E;  --teal-100:#EAE2D0;
    --foret-700:#8A5A0A;
    --font-sans:"Manrope",ui-sans-serif,system-ui,"Helvetica Neue",Arial,sans-serif;
    --font-lecture:"Source Serif 4",Georgia,"Times New Roman",serif;
    --sp-1:4px; --sp-2:8px; --sp-3:12px; --sp-4:16px; --sp-5:20px;
    --sp-6:24px; --sp-8:32px; --sp-12:48px;
    --content-max:1000px; --gutter:32px;
    --fs-hero:clamp(38px,6vw,58px); --fs-h2:30px; --fs-h3:24px; --fs-lead:19px;
    --fs-body:17px; --fs-body-sm:16px; --fs-ui:15px; --fs-ui-sm:14px;
    --fs-label:13px; --fs-meta:12px;
    --lh-title:1.18; --ls-hero:-0.03em; --ls-title:-0.02em; --ls-label:0.08em;
    /* Les angles restent des angles : six pixels au plus. */
    --r-sm:2px; --r-md:6px; --r-lg:6px; --r-pill:2px;
    /* Le tissu est plat : aucune ombre, sauf ce qui flotte. */
    --sh-card:none;
    --sh-raise:none;
    --dur:140ms; --ease:cubic-bezier(.4,0,.2,1);
    --tap-min:44px; --tap-comfort:48px;
    --focus-ring:#1E2A78;
  }
'''

SURCOUCHE = r'''  /* ═══ Surcouche « Trame » ═══════════════════════════════════════════
     Trois choses qu'un jeton ne peut pas porter : la police de lecture,
     la graisse maximale de Manrope (800, et non 900), et la barre de
     marque, qui n'est plus celle de francis. ═══════════════════════ */
  body{font-weight:500}
  h1,h2,.fiche .titre,.note b{font-weight:800}
  .eyebrow,.surtitre,.btn,.onglet,.eti,.date,.ou{font-weight:700}
  /* Ce qui se lit longtemps se lit en serif. */
  .chapeau,.tete p,.fiche .quoi,.note p,.vide{
    font-family:var(--font-lecture); font-weight:400; line-height:1.6}
  .fiche .quoi b,.note p b,.chapeau b{font-weight:600; color:var(--ink-900)}
  /* Le sur-titre est en ocre-texte, la seule forme d'ocre qui se lise. */
  .eyebrow{color:var(--ambre-700)}
  /* Le format d'un document n'est pas un signal : les étiquettes
     redeviennent neutres, avec un filet plutôt qu'un aplat. */
  .eti{background:transparent; border:1px solid var(--border-firm);
    color:var(--ink-500); text-transform:none; letter-spacing:0}
  /* Le bandeau de tête est le champ de marque : il porte le motif de fils.
     Le pied de page, lui, redescend sur l'écru enfoncé — un seul champ
     ocre par écran, c'est la règle. */
  .bande{background-image:
    repeating-linear-gradient(0deg, rgba(20,22,31,.10) 0 1px, transparent 1px 16px),
    repeating-linear-gradient(90deg, rgba(20,22,31,.10) 0 1px, transparent 1px 16px)}
  .bande .surtitre{color:var(--ink-900); opacity:.75}
  .bande .chapeau{color:var(--ink-900)}
  footer{background:var(--paper-200)}
  /* La barre de marque de Trame : le verrou, un filet, la destination. */
  .tr-barre{background:var(--surface-card); border-bottom:1px solid var(--border)}
  .tr-barre__in{max-width:var(--content-max); margin:0 auto; padding:14px var(--gutter);
    display:flex; align-items:center; gap:var(--sp-3)}
  .tr-logo{display:inline-flex; align-items:center; gap:.28em; color:var(--ink-900);
    font-size:1.25rem; line-height:1}
  .tr-logo svg{width:.62em; height:.62em; flex-shrink:0; display:block}
  .tr-logo .mot{font-weight:800; letter-spacing:-.045em}
  .tr-trait{width:1px; height:1.1rem; background:var(--border-firm)}
  .tr-desc{font-family:var(--font-lecture); font-size:var(--fs-ui); color:var(--ink-400)}
  @media (max-width:520px){.tr-trait,.tr-desc{display:none}}
  /* Manrope est plus large que Nunito : « 3 septembre 2026 » ne tenait plus
     dans sa colonne et venait buter sur les liens. */
  table.index .c-date{width:8.75rem}
  table.index .c-fam{width:7rem}
  table.index .c-type{width:7.5rem}
  table.index td.c-date{font-size:var(--fs-label)}
  table.index .t-lien{font-size:var(--fs-label)}
'''

BARRE = r'''<div class="tr-barre">
  <div class="tr-barre__in">
    <span class="tr-logo" role="img" aria-label="Trame"><svg viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g fill="currentColor"><rect x="4" y="10" width="3.5" height="8"/><rect x="20.5" y="10" width="19.5" height="8"/><rect x="4" y="26" width="19.5" height="8"/><rect x="36.5" y="26" width="3.5" height="8"/><rect x="10" y="4" width="8" height="19.5"/><rect x="10" y="36.5" width="8" height="3.5"/><rect x="26" y="4" width="8" height="3.5"/><rect x="26" y="20.5" width="8" height="19.5"/></g></svg><span class="mot">Trame</span></span>
    <span class="tr-trait" aria-hidden="true"></span>
    <span class="tr-desc">Le classeur du projet francis</span>
  </div>
</div>
'''
