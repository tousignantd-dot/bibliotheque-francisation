const SECTIONS = [
  {id:'prep', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-recherche/icons/play.svg" alt="">', title:'Je découvre', color:'#1D6B8F',
   lead:"Nommer les étapes d'un processus de sélection, reprendre un mot sans le répéter, et entendre ce qu'une voix ajoute aux mots.",
   intro:"Shirin Tabatabai est opératrice de production chez un sous-traitant de Sherbrooke. En Iran, elle a dirigé pendant onze ans une équipe de contrôle de la qualité. Mardi, elle a posé sa candidature au poste de superviseure de production, quart de soir, chez Boréalis Emballages. Ce soir, elle rencontre Alexandre Pouliot-Nadeau, un ancien collègue devenu contremaître là-bas — non pas pour qu'il la recommande, mais pour apprendre ce que le site de l'entreprise ne dit pas.",
   dialogue:'prep', next:{id:'t1', tit:"Défi 1 · L'appel de présélection", sub:"Se renseigner de vive voix sur un emploi, et faire dire ce qui n'est pas dit."}},

  {id:'t1', no:'1', title:"Défi 1 · L'appel de présélection", color:'#B45309',
   lead:"S'informer sur une entreprise ou sur un emploi en écoutant, poser des questions ouvertes et faire préciser ce qu'on n'a pas compris.",
   intro:"Défi 1 — Un appel de présélection n'est pas un interrogatoire : c'est la première fois où l'on peut poser des questions, et presque personne ne s'en sert. On y apprend trois gestes. Faire préciser un mot qu'on a manqué sans faire répéter toute la phrase. Poser une question qui ouvre plutôt qu'une question qui se ferme par oui ou par non. Et dire ce qu'on ferait, au conditionnel, quand rien n'est encore décidé.",
   dialogue:'t1', next:{id:'t2', tit:"Défi 2 · Lire l'entreprise", sub:"Lire un profil d'entreprise et une offre d'emploi, et voir ce qu'ils ne disent pas."}},

  {id:'t2', no:'2', title:"Défi 2 · Lire l'entreprise", color:'#0D7A6F',
   lead:"S'informer sur une entreprise ou sur un emploi en lisant : un profil d'entreprise, puis une offre d'emploi complète.",
   intro:"Défi 2 — Deux documents, deux lectures qui n'ont rien à voir. Un profil d'entreprise se lit pour y prélever des faits : des dates, des chiffres, un propriétaire. Une offre d'emploi se lit pour décider — suis-je admissible, et à quoi est-ce que je m'engage ? Ce défi apprend aussi à suivre les phrases longues de ces textes-là : celles qui opposent, celles qui concèdent, et celles où un « dont » ou un « auquel » renvoie à quelque chose écrit trois lignes plus haut.",
   dialogue:'t2', next:{id:'t3', tit:'Défi 3 · L’entrevue devant le comité', sub:"Répondre à ce qui n'est pas demandé, et négocier ce qui n'est pas affiché."}},

  {id:'t3', no:'3', title:"Défi 3 · L'entrevue devant le comité", color:'#A5335F',
   lead:"Participer à la dernière étape d'un processus de sélection : répondre par des exemples, tenir tête à une objection, reconnaître une question interdite et négocier une condition.",
   intro:"Défi 3 — Une entrevue de sélection se gagne rarement sur les bonnes réponses : elle se gagne sur ce qu'on dit avant qu'on vous le demande. Ce défi apprend quatre choses qui ne sont écrites nulle part. Répondre à une objection que personne ne formule. Dire ce qu'on aurait fait autrement, sans se dévaloriser. Reconnaître une question qu'un employeur n'a pas le droit de poser, et y répondre sans s'y soumettre ni se fâcher. Et demander plus que ce qui est offert, en offrant quelque chose en retour.",
   dialogue:'t3', next:{id:'appli', tit:'Je me lance', sub:"Passer l'entrevue avec l'assistant, raconter un cas difficile, écrire le courriel de suivi."}},

  {id:'appli', no:'<img class="icon-svg tno-play" src="/assets/interactive/module-n8-recherche/icons/play.svg" alt="">', title:'Je me lance', color:'#7E3F98', custom:true,
   lead:"Passer une entrevue devant un comité, raconter une situation professionnelle difficile, puis écrire le courriel qui suit l'entrevue.",
   intro:"Je me lance — C'est à vous : vous passez l'entrevue devant le comité, vous racontez à voix haute une situation où vous avez dû décider seul, puis vous écrivez le courriel de remerciement qui reprend, cette fois calmement, ce que vous avez mal expliqué."},

  {id:'retiens', no:'✓', title:'Je retiens des mots', color:'#1D6B8F', custom:true,
   lead:"Rassembler les mots du recrutement, de l'usine et de la négociation des conditions.",
   intro:"Je retiens des mots — Notez vos mots utiles, révisez avec les cartes mémoire, puis évaluez ce que vous êtes maintenant capable de faire."},
];
