// ═══════════════════════════════════════════════════════════════════════════
// Le parcours autonome — niveau 5 · Défi 1 · L'appel à la clinique
//
// Le contenu, et rien que le contenu. La mise en page est dans
// `build/gabarit/storyline.html` ; la construction dans `build/storyline.py`.
// **Ne jamais éditer le HTML produit** : la prochaine construction l'écrase.
//
// Les extraits sonores sont ceux du module de classe `module-n5-rendezvous`,
// rejoués depuis `/assets/interactive/module-n5-rendezvous/`. Rien n'est copié,
// rien n'est resynthétisé : la décision du 30 août 2026 est « narration écrite,
// pas parlée ».
//
// Où sont les répliques : `build/contenu/module-n5-rendezvous/dialogues.js`,
// clé `t1`. Le fichier `t1/line_NN_qui.mp3` porte le rang de la réplique dans
// cette liste, à partir de 1 — `line_13_manon.mp3` est la treizième.
//
// État : deux écrans sur dix-huit. Le storyboard complet est dans
// `modules-autonomes/plan-storyline.html`.
// ═══════════════════════════════════════════════════════════════════════════

const PARCOURS = {
  slug:    'n5-rendezvous-defi1',
  module:  'module-n5-rendezvous',
  titre:   "L'appel à la clinique",
  surtitre:"Niveau 5 · Défi 1",
  niveau:  5,
};

const ECRANS = [

  // ── Écran 2 du storyboard — une NOTION ─────────────────────────────────
  {
    id:   'qui-repond',
    type: 'notion',
    eye:  'Ce qu\'il faut savoir',
    menu: 'Qui répond au téléphone',
    titre: "Ce n'est pas un médecin qui répond.",
    paras: [
      "Vous appelez une clinique pour votre santé, et la personne au bout du fil "
      + "ne soigne personne. C'est une <b>agente administrative</b>. Elle ne vous "
      + "donnera pas de conseil, elle ne dira pas si c'est grave.",

      "Mais c'est elle qui décide d'une chose, et cette chose compte : "
      + "<b>combien de temps le médecin aura pour vous</b>. Quinze minutes, ou trente. "
      + "Elle le décide à partir de ce que vous dites, en une phrase, au début de l'appel.",

      "Écoutez comment elle pose la question — puis ce qu'elle en fait.",
    ],
    sons: [
      { fichier: 't1/line_09_manon.mp3', qui: 'Manon, agente administrative',
        texte: "C'est noté. Et qu'est-ce qui vous amène ? Je ne demande pas de détails, "
             + "seulement de quoi choisir la bonne durée." },
      { fichier: 't1/line_11_manon.mp3', qui: 'Manon, après la réponse de Rachid',
        texte: "D'accord. Trois mois, ce n'est pas rien. Je vous mets une plage de "
             + "trente minutes plutôt que quinze." },
    ],
    retenir: "Dire <b>depuis quand</b> ça dure, c'est ce qui vous fait gagner du temps "
           + "avec le médecin. Pas les détails : la durée.",
    attente: "Écoutez les deux extraits, puis continuez.",
  },

  // ── Écran 15 du storyboard — une VÉRIFICATION ──────────────────────────
  {
    id:   'choisir-moment',
    type: 'verif',
    eye:  'Vérification',
    menu: 'Choisir le moment',
    titre: "Manon vous propose deux moments. Lequel prenez-vous ?",
    consigne: "Rachid est préposé à l'entretien dans une école&nbsp;: il "
            + "<b>finit de travailler à seize heures</b>. Écoutez la proposition, puis "
            + "choisissez la seule réponse possible.",
    sons: [
      { fichier: 't1/line_13_manon.mp3', qui: 'Manon',
        texte: "J'ai le mardi 17 juin à quatorze heures dix, ou le jeudi 19 en fin de "
             + "journée, à dix-sept heures." },
    ],
    options: [
      { txt: "Mardi 17 juin, quatorze heures dix.",
        rat_t: "Quatorze heures dix, c'est deux heures dix de l'après-midi.",
        rat: "Rachid travaille encore. Au Québec, les rendez-vous se donnent presque "
           + "toujours en heures de 0 à 24&nbsp;: <b>quatorze heures</b> = 2 h de l'après-midi, "
           + "<b>dix-sept heures</b> = 5 h. Refaites le calcul, puis réessayez." },
      { txt: "Jeudi 19 juin, dix-sept heures.", juste: true },
      { txt: "Les deux conviennent&nbsp;: il choisira plus tard.",
        rat_t: "Un rendez-vous se fixe pendant l'appel, jamais après.",
        rat: "L'agente a deux places libres <i>maintenant</i>. Si vous ne tranchez pas, "
           + "elles seront prises par quelqu'un d'autre — et il faudra rappeler. "
           + "Une seule des deux convient à quelqu'un qui finit à seize heures." },
    ],
    pourquoi: "« En fin de journée » annonçait déjà l'heure&nbsp;: dix-sept heures, "
            + "soit cinq heures de l'après-midi. Rachid finit à seize heures — c'est le "
            + "seul des deux moments où il est libre.",
    attente: "Choisissez une réponse pour continuer.",
  },

];
