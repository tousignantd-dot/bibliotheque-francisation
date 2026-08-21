const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « an » de ordonnance et le « on » de comprimé",
    blocs:[
      {t:'texte', h:"Deux sons qui passent par le nez",
       p:"Le français a des sons qui sortent en partie par le nez. Deux d'entre eux se ressemblent beaucoup et se trouvent dans les deux mots les plus fréquents de la pharmacie : le <b>an</b> de « ordonn<b>an</b>ce » et le <b>on</b> de « c<b>om</b>primé ». Ce qui change, c'est la <b>bouche</b> : bien ouverte pour « an », ronde et fermée pour « on ».",
       note:"Au comptoir, ça compte : « dans » et « don », « sans » et « son », « pendant » et « pondant » ne veulent pas dire la même chose."},

      {t:'ana', h:"Le son « an » — la bouche ouverte",
       p:"C'est le son de « ordonnance », « pendant », « médicament ».",
       mots:[['On écrit','ordonn{an}ce'],['Aussi','pend{an}t, av{an}t, d{an}s',true],['La bouche','bien ouverte, la langue à plat']],
       say:"Une ordonnance, pendant sept jours, avant le repas.",
       note:"Il s'écrit de deux façons : <b>an</b> comme dans « pendant », et <b>en</b> comme dans « médicament ». Le son est le même."},

      {t:'ana', h:"Le son « on » — la bouche ronde",
       p:"C'est le son de « comprimé », « comptoir », « mon nom ».",
       mots:[['On écrit','c{om}primé'],['Aussi','c{om}ptoir, m{on} n{om}',true],['La bouche','en rond, presque fermée']],
       say:"Un comprimé, au comptoir, mon nom.",
       note:"Il s'écrit <b>on</b> ou <b>om</b>. Devant un p ou un b, c'est toujours <b>om</b> : c<b>om</b>primé, c<b>om</b>ptoir."},

      {t:'ana', h:"Les paires qui changent le sens",
       p:"Trois paires à connaître, toutes possibles à la pharmacie.",
       mots:[['dans / don','{dans} le sac · un {don} de sang'],['sans / son','{sans} ordonnance · {son} médicament',true],['temps / thon','combien de {temps} · un sandwich au {thon}']],
       say:"Sans ordonnance. Son médicament.",
       note:"Si tu hésites, dis le mot à côté de « ordonnance », puis à côté de « comprimé ». Ton oreille choisit toute seule."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','dans / don'],
         ['b','sans / son'],
         ['c','ordonnance / comprimé'],
         ['d','pendant / comptoir'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['d{an}s / d{on}'], say:"Dans, don.", n:'la bouche ouverte, puis ronde'},
         b:{w:['s{an}s / s{on}'], say:"Sans, son.", n:'deux mots très fréquents'},
         c:{w:['ordonn{an}ce / c{om}primé'], say:"Une ordonnance, un comprimé.", n:'les deux mots du module'},
         d:{w:['pend{an}t / c{om}ptoir'], say:"Pendant, comptoir.", n:'un de chaque'},
         e:{w:["« Un comprimé pendant sept jours, sans ordonnance. »"], say:"Un comprimé pendant sept jours, sans ordonnance.", n:'les deux sons quatre fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases de la pharmacie.",
       rows:[
         ["Une ordonnance, s'il vous plaît.","an deux fois"],
         ["Un comprimé au comptoir.","on trois fois"],
         ["Prenez ce médicament pendant sept jours.","an trois fois"],
         ["Mon nom est écrit sur le flacon.","on deux fois"],
         ["Sans ordonnance, on ne peut pas.","les deux sons dans la même phrase"],
         ["Combien de temps est-ce que ça prend ?","on puis an"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « on » à la place de « an »","« ordonnonce » au lieu de « ordonnance »",
          "C'est le piège le plus fréquent chez les débutants. Ouvre bien la bouche : le son « an » demande de la place."],
         ["prononcer le n","dire « or-do-nan-ne » en détachant le n",
          "Non : le n ne se prononce pas tout seul, il colore la voyelle. C'est le nez qui travaille, pas la langue."],
         ["oublier que « en » se dit « an »","lire « médicament » avec un e ordinaire",
          "Dans « médicam<b>en</b>t », les lettres e-n donnent exactement le même son que a-n. Deux écritures, un seul son."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Ordonnance » a le son…", opts:["an","on"], ok:0,
          fb:"La bouche est bien ouverte."},
         {q:"« Comptoir » a le son…", opts:["an","on"], ok:1,
          fb:"La bouche est en rond, presque fermée."},
         {q:"Dans « médicament », les lettres e-n donnent le son…", opts:["an","on"], ok:0,
          fb:"Deux écritures, un seul son : an."},
         {q:"« Sans ordonnance » et « son médicament »…", opts:["ont le même son","ont deux sons différents"], ok:1,
          fb:"« sans » a le son an, « son » a le son on."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>ordonnance</b> pour le son « an », <b>comprimé</b> pour le son « on ». Devant un mot nouveau, dis-le à côté de l'un des deux, et laisse l'air passer par le nez."},
    ]
  },

  prCorps: {
    eye:'Mini-leçon', tit:"J'ai mal à… — dire où ça fait mal",
    blocs:[
      {t:'texte', h:"Une seule phrase, et le nom d'une partie du corps",
       p:"Au comptoir, la première chose qu'on dit tient en quatre mots : <b>J'ai mal à…</b> Ce qui suit change selon la partie du corps, et c'est là qu'il faut choisir entre quatre petits mots : <b>au</b>, <b>à la</b>, <b>à l'</b> et <b>aux</b>. Le programme de niveau 3 nomme précisément ce point : les principales parties du corps.",
       note:"Le pharmacien ne demande jamais autre chose au début. Si cette phrase est prête, la moitié de la conversation est réglée."},

      {t:'ana', h:"Devant un mot masculin : au",
       p:"Le dos, le ventre, le pied, le genou, le cou, le bras.",
       mots:[['On dit',"j'ai mal {au} dos"],['Aussi',"j'ai mal {au} ventre",true],['Et',"j'ai mal {au} genou"]],
       say:"J'ai mal au dos, j'ai mal au ventre, j'ai mal au genou.",
       note:"Ces mots sont masculins : on peut dire « un dos », « un ventre », « un genou »."},

      {t:'ana', h:"Devant un mot féminin : à la",
       p:"La tête, la gorge, la jambe, la main, la bouche.",
       mots:[['On dit',"j'ai mal {à la} tête"],['Aussi',"j'ai mal {à la} gorge",true],['Et',"j'ai mal {à la} jambe"]],
       say:"J'ai mal à la tête, j'ai mal à la gorge, j'ai mal à la jambe.",
       note:"Ces mots sont féminins : on dit « une tête », « une gorge », « une jambe »."},

      {t:'ana', h:"Devant une voyelle : à l'",
       p:"L'oreille, l'épaule, l'estomac, l'œil.",
       mots:[['On dit',"j'ai mal {à l'}oreille"],['Aussi',"j'ai mal {à l'}épaule",true],['Et',"j'ai mal {à l'}estomac"]],
       say:"J'ai mal à l'oreille, j'ai mal à l'épaule, j'ai mal à l'estomac.",
       note:"On ne dit jamais « à la oreille » : deux voyelles côte à côte, c'est trop dur à prononcer. Le mot se colle."},

      {t:'ana', h:"Devant un pluriel : aux",
       p:"Les dents, les yeux, les jambes, les oreilles.",
       mots:[['On dit',"j'ai mal {aux} dents"],['Aussi',"j'ai mal {aux} yeux",true],['Et',"j'ai mal {aux} jambes"]],
       say:"J'ai mal aux dents, j'ai mal aux yeux, j'ai mal aux jambes.",
       note:"Une seule forme au pluriel, masculin comme féminin. C'est la plus facile des quatre."},

      {t:'labo', h:"Construis ta phrase",
       p:"Choisis une partie du corps et un moment.",
       axes:[
         {id:'v', lbl:'Où as-tu mal ?', opts:[['a','la tête'],['b','le dos'],['c','les dents'],['d',"l'oreille"]]},
         {id:'q', lbl:'Depuis quand ?', opts:[['1','ce matin'],['2','trois jours']]}],
       out:{
         a1:{w:["J'ai mal à la tête depuis ce matin."], say:"J'ai mal à la tête depuis ce matin.", n:'féminin : à la'},
         a2:{w:["J'ai mal à la tête depuis trois jours."], say:"J'ai mal à la tête depuis trois jours.", n:'féminin aussi'},
         b1:{w:["J'ai mal au dos depuis ce matin."], say:"J'ai mal au dos depuis ce matin.", n:'masculin : au'},
         b2:{w:["J'ai mal au dos depuis trois jours."], say:"J'ai mal au dos depuis trois jours.", n:'masculin aussi'},
         c1:{w:["J'ai mal aux dents depuis ce matin."], say:"J'ai mal aux dents depuis ce matin.", n:'pluriel : aux'},
         c2:{w:["J'ai mal aux dents depuis trois jours."], say:"J'ai mal aux dents depuis trois jours.", n:'trois jours de rage de dents'},
         d1:{w:["J'ai mal à l'oreille depuis ce matin."], say:"J'ai mal à l'oreille depuis ce matin.", n:"voyelle : à l'"},
         d2:{w:["J'ai mal à l'oreille depuis trois jours."], say:"J'ai mal à l'oreille depuis trois jours.", n:'huit phrases toutes prêtes'},
       },
       note:"Huit phrases, toutes correctes, toutes utilisables telles quelles au comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ranger les quatre formes.",
       rows:[
         ["J'ai mal à la tête depuis ce matin.","féminin"],
         ["J'ai mal au dos quand je travaille.","masculin"],
         ["Mon garçon a mal à la gorge.","on peut parler de quelqu'un d'autre"],
         ["J'ai mal aux dents depuis deux jours.","pluriel"],
         ["J'ai mal à l'oreille gauche.","devant une voyelle"],
         ["Où avez-vous mal, exactement ?","la question du pharmacien"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « j'ai mal la tête »","oublier le petit mot à",
          "Sans le « à », la phrase ne se dit pas. C'est le mot le plus court et le plus obligatoire de la phrase."],
         ["dire « à la oreille »","garder « la » devant une voyelle",
          "Devant a, e, i, o, u et h, on dit toujours <b>à l'</b> : à l'oreille, à l'épaule, à l'estomac."],
         ["dire « au dents »","oublier le pluriel",
          "Plusieurs dents, plusieurs yeux : c'est <b>aux</b>. Une seule forme, facile à retenir."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"J'ai mal ___ tête.", opts:["au","à la"], ok:1,
          fb:"« tête » est féminin."},
         {q:"J'ai mal ___ dos.", opts:["au","à la"], ok:0,
          fb:"« dos » est masculin."},
         {q:"J'ai mal ___ oreille.", opts:["à la","à l'"], ok:1,
          fb:"Devant une voyelle, le mot se colle."},
         {q:"J'ai mal ___ dents.", opts:["au","aux"], ok:1,
          fb:"Plusieurs dents : aux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre formes, quatre exemples à garder en tête : <b>au</b> dos, <b>à la</b> tête, <b>à l'</b>oreille, <b>aux</b> dents. Si tu ne sais pas si le mot est masculin ou féminin, montre l'endroit avec ta main en disant « j'ai mal ici » : personne ne t'en voudra."},
    ]
  },

  t1decrire: {
    eye:'Mini-leçon', tit:"Les verbes qui disent ce qui ne va pas",
    blocs:[
      {t:'texte', h:"Onze verbes, et le programme les nomme",
       p:"Le programme de niveau 3 donne une liste courte pour cette situation : <b>tousser, avoir de la fièvre, se couper, s'étouffer, se faire mal, consulter, questionner, administrer, persister, rincer</b>. Ce ne sont pas des mots choisis au hasard : ce sont ceux qu'on entend vraiment au comptoir d'une pharmacie, d'un côté comme de l'autre.",
       note:"Trois d'entre eux servent au pharmacien plus qu'à toi — questionner, administrer, persister — mais il faut les comprendre quand il les dit."},

      {t:'ana', h:"Ce qui se passe maintenant : le présent",
       p:"Pour un malaise qui dure encore aujourd'hui.",
       mots:[['On dit','je {tousse}'],['Aussi',"j'{ai} de la fièvre",true],['Et',"j'ai mal à la gorge"]],
       say:"Je tousse. J'ai de la fièvre. J'ai mal à la gorge.",
       note:"C'est le temps de la première phrase au comptoir. Tu ne racontes pas : tu dis ce qui se passe."},

      {t:'ana', h:"Un accident déjà arrivé : le passé composé",
       p:"Pour quelque chose qui est arrivé une fois, avant.",
       mots:[['On dit','je me suis {coupé}'],['Aussi','je me suis {fait mal} au genou',true],['Et','je suis {tombée} dans l\'escalier']],
       say:"Je me suis coupé le doigt. Je me suis fait mal au genou.",
       note:"Ces verbes se construisent avec <b>être</b> : je me <b>suis</b> coupé, je me <b>suis</b> fait mal. Jamais avec « avoir »."},

      {t:'ana', h:"Ce que le pharmacien dit",
       p:"Trois verbes à comprendre, même si tu ne les dis pas souvent.",
       mots:[['persister','si la toux {persiste}, consultez'],['administrer','ne pas {administrer} aux enfants',true],['rincer','{rincez} votre bouche après']],
       say:"Si la toux persiste, consultez un médecin.",
       note:"« Administrer » est le mot écrit sur les boîtes ; à l'oral, le pharmacien dit plutôt « donner »."},

      {t:'labo', h:"Le malaise et le verbe",
       p:"Choisis ce qui t'arrive et depuis quand.",
       axes:[
         {id:'v', lbl:"Qu'est-ce que tu as ?", opts:[['a','la toux'],['b','la fièvre'],['c','une coupure'],['d','une chute']]},
         {id:'q', lbl:'Quand ?', opts:[['1','ça dure encore'],['2',"c'est arrivé avant"]]}],
       out:{
         a1:{w:["Je tousse depuis quatre jours."], say:"Je tousse depuis quatre jours.", n:'présent : ça continue'},
         a2:{w:["J'ai commencé à tousser samedi."], say:"J'ai commencé à tousser samedi.", n:'le début se dit au passé'},
         b1:{w:["J'ai de la fièvre depuis hier soir."], say:"J'ai de la fièvre depuis hier soir.", n:'présent'},
         b2:{w:["J'ai eu de la fièvre hier soir."], say:"J'ai eu de la fièvre hier soir.", n:"c'est fini maintenant"},
         c1:{w:["Ma coupure fait encore mal."], say:"Ma coupure fait encore mal.", n:'présent'},
         c2:{w:["Je me suis coupé le doigt hier."], say:"Je me suis coupé le doigt hier.", n:'passé composé avec être'},
         d1:{w:["J'ai mal au genou depuis ma chute."], say:"J'ai mal au genou depuis ma chute.", n:'le mal dure encore'},
         d2:{w:["Je suis tombée dans l'escalier lundi."], say:"Je suis tombée dans l'escalier lundi.", n:'huit phrases toutes prêtes'},
       },
       note:"Le pharmacien a besoin des deux : ce qui est arrivé, et ce que tu ressens maintenant."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases à dire au comptoir.",
       rows:[
         ["Je tousse et je ne dors pas la nuit.","présent"],
         ["J'ai de la fièvre depuis hier soir.","présent + depuis"],
         ["Je me suis coupé le doigt avec un couteau.","passé composé"],
         ["Je suis tombée et je me suis fait mal au genou.","deux verbes au passé"],
         ["La toux persiste depuis une semaine.","le verbe du pharmacien"],
         ["Est-ce que je dois consulter un médecin ?","la bonne question à poser"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « j'ai coupé mon doigt »","construire la phrase comme en anglais",
          "En français, on dit <b>je me suis coupé le doigt</b> : le petit « me » dit que c'est ton doigt, et on garde « le »."],
         ["dire « je suis fièvre »","traduire mot à mot",
          "La fièvre, ça s'a, ça ne se suis pas : <b>j'ai</b> de la fièvre. Comme « j'ai faim » et « j'ai froid »."],
         ["confondre consulter et questionner","« je vais questionner le médecin »",
          "<b>Consulter</b>, c'est aller voir un professionnel pour sa santé. <b>Questionner</b>, c'est poser des questions — c'est le pharmacien qui te questionne."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour un mal qui dure encore, on dit…", opts:["je tousse","j'ai toussé"], ok:0,
          fb:"Le présent dit ce qui se passe aujourd'hui."},
         {q:"Pour une coupure d'hier, on dit…", opts:["je me coupe","je me suis coupé"], ok:1,
          fb:"Un accident fini se dit au passé composé."},
         {q:"« La toux persiste » veut dire…", opts:["elle continue","elle est finie"], ok:0,
          fb:"Persister, c'est ne pas partir."},
         {q:"Qui questionne, au comptoir ?", opts:["le pharmacien","le flacon"], ok:0,
          fb:"C'est lui qui pose les questions."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux temps, deux usages : <b>je tousse</b> pour ce qui dure, <b>je me suis coupé</b> pour ce qui est arrivé. Et un verbe à reconnaître dans la bouche du pharmacien : <b>persister</b>. Quand il dit « si ça persiste », il te demande de revenir ou d'aller voir un médecin."},
    ]
  },

  t1depuis: {
    eye:'Mini-leçon', tit:'Depuis, ça fait, il y a, pendant, dans',
    blocs:[
      {t:'texte', h:"La deuxième question du pharmacien, toujours la même",
       p:"« Depuis quand est-ce que ça dure ? » Il la pose chaque fois, parce que la réponse change son conseil : une toux de deux jours n'est pas une toux de deux semaines. Le programme de niveau 3 donne exactement ces mots-là — <b>dans, depuis, ça fait, il y a, voilà, pendant</b> — et ils ne veulent pas dire la même chose.",
       note:"Cinq petits mots. Bien rangés une fois, ils servent toute la vie : au travail, chez le médecin, à l'école de tes enfants."},

      {t:'ana', h:"Ce qui dure encore : depuis",
       p:"Ça a commencé avant, et ça continue maintenant.",
       mots:[['On dit','je tousse {depuis} quatre jours'],['Aussi',"j'ai de la fièvre {depuis} hier soir",true],['Et','elle attend {depuis} vingt minutes']],
       say:"Je tousse depuis quatre jours.",
       note:"Après « depuis », on met une durée (quatre jours) ou un moment de départ (hier soir, samedi, lundi)."},

      {t:'ana', h:"La même chose, autrement : ça fait… que",
       p:"Deux morceaux : « ça fait » au début, « que » au milieu.",
       mots:[['On dit','{ça fait} quatre jours {que} je tousse'],['Aussi','{ça fait} deux semaines {qu\'}il a mal',true],['Le sens','exactement le même que depuis']],
       say:"Ça fait quatre jours que je tousse.",
       note:"Au Québec, on l'entend au moins autant que « depuis ». Les deux sont justes : choisis celle qui te vient."},

      {t:'ana', h:"Un moment fini : il y a",
       p:"C'est arrivé une fois, à ce moment-là, et c'est terminé.",
       mots:[['On dit','je me suis coupé {il y a} deux jours'],['Aussi','je suis arrivée au Québec {il y a} un an',true],['Attention','ça ne dure plus : c\'est un point dans le passé']],
       say:"Je me suis coupé le doigt il y a deux jours.",
       note:"« Il y a deux jours » = avant-hier. « Depuis deux jours » = ça continue encore. La différence est réelle."},

      {t:'ana', h:"Une durée complète : pendant · Ce qui vient : dans",
       p:"Les deux mots de l'étiquette et du rendez-vous.",
       mots:[['On dit','prenez-le {pendant} sept jours'],['Et','mon rendez-vous est {dans} six semaines',true],['La différence','pendant = du début à la fin · dans = le temps à attendre']],
       say:"Pendant sept jours. Dans six semaines.",
       note:"« Pendant » sert surtout à la posologie ; « dans » sert aux rendez-vous et aux attentes."},

      {t:'labo', h:"Choisis le bon petit mot",
       p:"Choisis une situation et regarde la phrase juste.",
       axes:[
         {id:'v', lbl:'Quelle situation ?', opts:[['a','une toux qui continue'],['b','une coupure de mardi'],['c','un traitement de sept jours'],['d','un rendez-vous à venir']]},
         {id:'q', lbl:'Quelle forme ?', opts:[['1','la plus courte'],['2',"l'autre façon"]]}],
       out:{
         a1:{w:["Je tousse depuis quatre jours."], say:"Je tousse depuis quatre jours.", n:'depuis + durée'},
         a2:{w:["Ça fait quatre jours que je tousse."], say:"Ça fait quatre jours que je tousse.", n:'même sens, autre forme'},
         b1:{w:["Je me suis coupé il y a trois jours."], say:"Je me suis coupé il y a trois jours.", n:'un moment fini'},
         b2:{w:["Je me suis coupé mardi."], say:"Je me suis coupé mardi.", n:'le jour se dit sans petit mot'},
         c1:{w:["Prenez-le pendant sept jours."], say:"Prenez-le pendant sept jours.", n:'du premier au dernier jour'},
         c2:{w:["Le traitement dure sept jours."], say:"Le traitement dure sept jours.", n:'sans petit mot du tout'},
         d1:{w:["Mon rendez-vous est dans six semaines."], say:"Mon rendez-vous est dans six semaines.", n:'du temps à attendre'},
         d2:{w:["J'ai un rendez-vous le 12 août."], say:"J'ai un rendez-vous le 12 août.", n:'la date exacte'},
       },
       note:"Huit phrases justes. Aucune n'est plus polie qu'une autre : prends celle qui te vient vite."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases pour ranger les cinq mots.",
       rows:[
         ["Je tousse depuis quatre jours.","depuis : ça continue"],
         ["Ça fait deux jours que j'ai mal à la gorge.","ça fait… que"],
         ["Je me suis coupé le doigt il y a trois jours.","il y a : c'est fini"],
         ["Prenez un comprimé pendant sept jours.","pendant : toute la durée"],
         ["Mon rendez-vous est dans six semaines.","dans : à venir"],
         ["Depuis quand est-ce que ça dure ?","la question du pharmacien"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre depuis et il y a","« je tousse il y a quatre jours »",
          "« Il y a » ferme le moment ; « depuis » l'ouvre jusqu'à aujourd'hui. Si tu tousses encore, c'est <b>depuis</b>."],
         ["oublier le que","« ça fait quatre jours je tousse »",
          "« Ça fait » va toujours avec <b>que</b> : ça fait quatre jours <b>que</b> je tousse. Sans lui, la phrase reste ouverte."],
         ["confondre pendant et dans","« prenez-le dans sept jours »",
          "« Dans sept jours » veut dire : commence la semaine prochaine. Pour un traitement, c'est <b>pendant</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Tu tousses encore aujourd'hui. Tu dis…", opts:["depuis quatre jours","il y a quatre jours"], ok:0,
          fb:"Ça continue : depuis."},
         {q:"« Ça fait deux jours ___ j'ai mal. »", opts:["que","et"], ok:0,
          fb:"« Ça fait » va toujours avec « que »."},
         {q:"Sur l'étiquette : « ___ sept jours »", opts:["pendant","dans"], ok:0,
          fb:"Du premier au dernier jour."},
         {q:"Ton rendez-vous n'a pas encore eu lieu. Tu dis…", opts:["dans six semaines","depuis six semaines"], ok:0,
          fb:"Du temps à attendre : dans."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois phrases repères : <b>je tousse depuis quatre jours</b> (ça continue), <b>je me suis coupé il y a trois jours</b> (c'est fini), <b>prenez-le pendant sept jours</b> (toute la durée). Et « ça fait… que » est simplement une autre façon de dire « depuis »."},
    ]
  },

  t2modal: {
    eye:'Mini-leçon', tit:'Pouvoir, devoir, il faut',
    blocs:[
      {t:'texte', h:"Demander, et comprendre ce qui est obligatoire",
       p:"Trois verbes suffisent pour presque tout ce qui se dit au comptoir des ordonnances. <b>Pouvoir</b> sert à demander : est-ce que je peux, est-ce que vous pouvez. <b>Devoir</b> sert à dire ce qui est obligatoire pour une personne : je dois, vous devez. Et <b>il faut</b> dit la même chose sans nommer personne.",
       note:"Ils ne se conjuguent jamais seuls : il y a toujours un deuxième verbe derrière, à l'infinitif. Je peux <b>attendre</b>, vous devez <b>finir</b>, il faut <b>apporter</b>."},

      {t:'ana', h:"Demander : est-ce que je peux…",
       p:"La phrase la plus utile de tout le module.",
       mots:[['On dit','{est-ce que je peux} faire renouveler mon ordonnance ?'],['Aussi','{est-ce que je peux} attendre ici ?',true],['Et','{est-ce que je peux} payer avec ma carte ?']],
       say:"Est-ce que je peux faire renouveler mon ordonnance ?",
       note:"Elle sert partout, pas seulement à la pharmacie : à la banque, au bureau de poste, à l'école."},

      {t:'ana', h:"Demander un service : est-ce que vous pouvez…",
       p:"Quand c'est l'autre personne qui doit faire quelque chose.",
       mots:[['On dit','{est-ce que vous pouvez} regarder mon dossier ?'],['Aussi','{est-ce que vous pouvez} répéter, s\'il vous plaît ?',true],['Et','{est-ce que vous pouvez} écrire le nom sur un papier ?']],
       say:"Est-ce que vous pouvez regarder mon dossier, s'il vous plaît ?",
       note:"Ajoute « s'il vous plaît » à la fin : la demande devient tout de suite plus polie."},

      {t:'ana', h:"Ce qui est obligatoire : je dois, vous devez, il faut",
       p:"Trois façons de dire la même obligation.",
       mots:[['Pour moi','{je dois} prendre un comprimé le matin'],['Pour vous','{vous devez} finir les sept jours',true],['Sans personne','{il faut} apporter sa carte']],
       say:"Je dois prendre un comprimé le matin. Il faut apporter sa carte.",
       note:"« Il faut » ne change jamais de forme, quelle que soit la personne. C'est le plus facile des trois."},

      {t:'labo', h:"Demander ou obliger",
       p:"Choisis ce que tu veux dire.",
       axes:[
         {id:'v', lbl:'Tu veux…', opts:[['a','demander pour toi'],['b','demander un service'],['c','dire ton obligation'],['d','dire la règle']]},
         {id:'q', lbl:'À propos de quoi ?', opts:[['1',"l'ordonnance"],['2','le médicament']]}],
       out:{
         a1:{w:["Est-ce que je peux faire renouveler mon ordonnance ?"], say:"Est-ce que je peux faire renouveler mon ordonnance ?", n:'la demande de base'},
         a2:{w:["Est-ce que je peux avoir ce médicament sans ordonnance ?"], say:"Est-ce que je peux avoir ce médicament sans ordonnance ?", n:'une vraie question de pharmacie'},
         b1:{w:["Est-ce que vous pouvez vérifier mon ordonnance ?"], say:"Est-ce que vous pouvez vérifier mon ordonnance ?", n:"c'est l'autre qui agit"},
         b2:{w:["Est-ce que vous pouvez m'expliquer ce médicament ?"], say:"Est-ce que vous pouvez m'expliquer ce médicament ?", n:'demander une explication'},
         c1:{w:["Je dois renouveler mon ordonnance avant vendredi."], say:"Je dois renouveler mon ordonnance avant vendredi.", n:'mon obligation à moi'},
         c2:{w:["Je dois prendre ce médicament trois fois par jour."], say:"Je dois prendre ce médicament trois fois par jour.", n:"c'est écrit sur l'étiquette"},
         d1:{w:["Il faut une ordonnance pour ce médicament."], say:"Il faut une ordonnance pour ce médicament.", n:'la règle, pour tout le monde'},
         d2:{w:["Il faut prendre ce médicament avec de la nourriture."], say:"Il faut prendre ce médicament avec de la nourriture.", n:'huit phrases toutes prêtes'},
       },
       note:"Remarque que « il faut » peut être suivi d'un nom (une ordonnance) ou d'un verbe (prendre). Les deux se disent."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Est-ce que je peux faire renouveler mon ordonnance ?","la demande la plus fréquente"],
         ["Est-ce que vous pouvez répéter, s'il vous plaît ?","quand on n'a pas compris"],
         ["Je dois prendre un comprimé le matin.","mon obligation"],
         ["Vous devez finir les sept jours.","ce que le pharmacien te dit"],
         ["Il faut apporter sa carte d'assurance maladie.","la règle générale"],
         ["Est-ce que je dois attendre ici ?","demander ce qui est attendu de toi"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je peux avoir » sans question","« je peux avoir mon médicament »",
          "Sans « est-ce que » et sans point d'interrogation dans la voix, ça sonne comme un ordre. Monte la voix à la fin."],
         ["mettre le deuxième verbe au présent","« je dois je prends un comprimé »",
          "Après pouvoir, devoir et falloir, le verbe qui suit ne se conjugue pas : je dois <b>prendre</b>, il faut <b>apporter</b>."],
         ["dire « il faut je »","« il faut je prends mon médicament »",
          "« Il faut » ne se marie pas avec « je ». On dit <b>je dois</b> prendre, ou <b>il faut</b> prendre — jamais les deux ensemble."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour demander poliment, on dit…", opts:["est-ce que je peux","je veux"], ok:0,
          fb:"« Je veux » est trop direct au comptoir."},
         {q:"Après « vous devez », le verbe est…", opts:["conjugué","à l'infinitif"], ok:1,
          fb:"Vous devez finir, jamais « vous devez vous finissez »."},
         {q:"« Il faut apporter sa carte » veut dire…", opts:["c'est obligatoire","c'est possible"], ok:0,
          fb:"« Il faut » dit toujours une obligation."},
         {q:"Pour demander un service à quelqu'un…", opts:["est-ce que vous pouvez","est-ce que je peux"], ok:0,
          fb:"C'est l'autre personne qui agit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois phrases à garder telles quelles : <b>Est-ce que je peux…</b> pour demander, <b>Je dois…</b> pour ton obligation, <b>Il faut…</b> pour la règle de tout le monde. Et derrière chacune, un verbe qui ne se conjugue pas."},
    ]
  },

  t2poss: {
    eye:'Mini-leçon', tit:'Mon, ma, mes — votre, vos',
    blocs:[
      {t:'texte', h:"Dire à qui appartient la carte",
       p:"Au comptoir, on parle sans arrêt de choses qui appartiennent à quelqu'un : <b>ma</b> carte, <b>mon</b> dossier, <b>vos</b> médicaments. Le français change le petit mot selon deux choses seulement : à qui c'est, et si le mot qui suit est masculin, féminin ou pluriel.",
       note:"Le pharmacien te vouvoie : il dira toujours <b>votre</b> et <b>vos</b>. Toi, tu parles de tes affaires : <b>mon</b>, <b>ma</b>, <b>mes</b>."},

      {t:'ana', h:"Ce qui est à moi",
       p:"Trois formes, selon le mot qui suit.",
       mots:[['Masculin','{mon} dossier, {mon} médicament'],['Féminin','{ma} carte, {ma} pharmacie',true],['Pluriel','{mes} comprimés, {mes} médicaments']],
       say:"Mon dossier, ma carte, mes comprimés.",
       note:"Ce n'est pas toi qui décides : c'est le mot qui suit. « Carte » est féminin, donc <b>ma</b> carte, même si tu es un homme."},

      {t:'ana', h:"L'exception qui compte : mon ordonnance",
       p:"Devant une voyelle, « ma » devient « mon ».",
       mots:[['On dit','{mon} ordonnance'],['Aussi','{mon} assurance, {mon} adresse',true],['Jamais','« ma ordonnance » ne se dit pas']],
       say:"Mon ordonnance est finie depuis samedi.",
       note:"Le mot reste féminin — on dit « mon ordonnance est fini<b>e</b> » — mais le petit mot change pour que ce soit plus facile à dire."},

      {t:'ana', h:"Ce qui est à vous",
       p:"Deux formes seulement, et c'est le nombre qui décide.",
       mots:[['Une chose','{votre} nom, {votre} carte'],['Plusieurs choses','{vos} médicaments, {vos} comprimés',true],['Le genre','ne change rien : votre nom, votre carte']],
       say:"Votre carte, s'il vous plaît. Vos médicaments sont prêts.",
       note:"Plus simple que « mon / ma » : masculin ou féminin, c'est <b>votre</b>. Au pluriel, <b>vos</b>."},

      {t:'labo', h:"À qui c'est ?",
       p:"Choisis un objet et une personne.",
       axes:[
         {id:'v', lbl:'Quel objet ?', opts:[['a','la carte'],['b','le dossier'],['c','les comprimés'],['d',"l'ordonnance"]]},
         {id:'q', lbl:'À qui ?', opts:[['1','à moi'],['2','à vous']]}],
       out:{
         a1:{w:["Voici ma carte d'assurance maladie."], say:"Voici ma carte d'assurance maladie.", n:'féminin : ma'},
         a2:{w:["Votre carte, s'il vous plaît ?"], say:"Votre carte, s'il vous plaît ?", n:'votre, masculin comme féminin'},
         b1:{w:["Mon dossier est à la pharmacie du coin."], say:"Mon dossier est à la pharmacie du coin.", n:'masculin : mon'},
         b2:{w:["Votre dossier dit que le médicament a été servi en mai."], say:"Votre dossier dit que le médicament a été servi en mai.", n:'ce que dit le pharmacien'},
         c1:{w:["Je prends mes comprimés le matin."], say:"Je prends mes comprimés le matin.", n:'pluriel : mes'},
         c2:{w:["Vos comprimés seront prêts dans vingt minutes."], say:"Vos comprimés seront prêts dans vingt minutes.", n:'pluriel : vos'},
         d1:{w:["Mon ordonnance est finie."], say:"Mon ordonnance est finie.", n:"voyelle : mon, même au féminin"},
         d2:{w:["Votre ordonnance est échue depuis mai."], say:"Votre ordonnance est échue depuis mai.", n:'huit phrases toutes prêtes'},
       },
       note:"Écoute la différence entre « ma carte » et « votre carte » : c'est la même chose, dite des deux côtés du comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Voici ma carte d'assurance maladie.","féminin : ma"],
         ["Mon ordonnance est finie depuis samedi.","voyelle : mon"],
         ["Je prends mes comprimés le matin.","pluriel : mes"],
         ["Votre nom, s'il vous plaît ?","la première question"],
         ["Vos médicaments seront prêts dans vingt minutes.","pluriel : vos"],
         ["Le pharmacien regarde mon dossier.","masculin : mon"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["choisir selon soi-même","un homme qui dit « mon carte »",
          "Le petit mot suit le nom, jamais la personne qui parle. « Carte » est féminin : <b>ma</b> carte pour tout le monde."],
         ["dire « ma ordonnance »","garder « ma » devant une voyelle",
          "On dit <b>mon</b> ordonnance, <b>mon</b> assurance, <b>mon</b> adresse. Le mot reste féminin, mais le petit mot change."],
         ["confondre votre et vos","« votre médicaments »",
          "Une chose : <b>votre</b>. Plusieurs : <b>vos</b>. Regarde s'il y a un s au bout du mot."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"___ carte, s'il vous plaît ? (le pharmacien parle)", opts:["Votre","Vos"], ok:0,
          fb:"Une seule carte."},
         {q:"___ ordonnance est finie. (je parle de la mienne)", opts:["Ma","Mon"], ok:1,
          fb:"Devant une voyelle, « ma » devient « mon »."},
         {q:"Je prends ___ comprimés le matin.", opts:["mes","ma"], ok:0,
          fb:"Plusieurs comprimés."},
         {q:"Le petit mot suit…", opts:["la personne qui parle","le mot qui vient après"], ok:1,
          fb:"C'est le nom qui décide."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Trois pour toi — <b>mon</b> dossier, <b>ma</b> carte, <b>mes</b> comprimés — et deux pour le pharmacien : <b>votre</b> carte, <b>vos</b> médicaments. Une seule exception à retenir par cœur : <b>mon</b> ordonnance."},
    ]
  },

  t3frequence: {
    eye:'Mini-leçon', tit:"Combien de fois par jour ?",
    blocs:[
      {t:'texte', h:"La ligne la plus importante de l'étiquette",
       p:"Sur une étiquette de pharmacie, tout tient en une phrase : <b>combien</b> de comprimés, <b>combien de fois</b> par jour, <b>quand</b>, et <b>pendant combien de jours</b>. Quatre renseignements, dans cet ordre. Si tu sais lire ces quatre-là, tu sais lire une posologie.",
       note:"Le programme de niveau 3 nomme les marqueurs de fréquence pour cette situation. Ce sont eux, et ils ne sont pas nombreux."},

      {t:'ana', h:"Compter les prises : une fois, deux fois, trois fois",
       p:"Le mot « fois » ne change jamais de forme.",
       mots:[['On dit','une {fois} par jour'],['Aussi','trois {fois} par jour',true],['Et','deux {fois} par semaine']],
       say:"Une fois par jour. Trois fois par jour. Deux fois par semaine.",
       note:"« Fois » s'écrit toujours avec un s, même au singulier : une fois. C'est un mot qui garde son s partout."},

      {t:'ana', h:"Les moments de la journée",
       p:"Quatre mots qui reviennent sur toutes les étiquettes.",
       mots:[['Le jour','{le matin}, le midi, le soir'],['La nuit','{au coucher}, avant de dormir',true],['La règle','trois fois par jour = matin, midi et soir']],
       say:"Le matin, le midi, le soir. Une fois par jour, au coucher.",
       note:"Quand l'étiquette dit seulement « trois fois par jour », le pharmacien traduit : matin, midi et soir, à peu près aux huit heures."},

      {t:'ana', h:"L'heure entre deux comprimés : aux",
       p:"Une façon de parler bien québécoise, et très fréquente.",
       mots:[['On dit','{aux} huit heures'],['Aussi','{aux} quatre heures, {aux} six heures',true],['Ailleurs','en France, on dirait « toutes les huit heures »']],
       say:"Prenez ce médicament aux huit heures.",
       note:"« Aux huit heures » ne veut pas dire « à 8 h » : ça veut dire qu'il y a huit heures entre deux comprimés."},

      {t:'ana', h:"Avant, après, avec de la nourriture",
       p:"Le moment par rapport au repas change l'effet du médicament.",
       mots:[['Estomac vide','{avant} les repas'],['Estomac plein','{après} les repas',true],['Pendant ou juste après','{avec de la nourriture}']],
       say:"Avant les repas. Après les repas. Avec de la nourriture.",
       note:"« Avec de la nourriture » est la formule la plus fréquente sur les étiquettes du Québec. Elle veut dire : pas l'estomac vide."},

      {t:'labo', h:"Lis la posologie à voix haute",
       p:"Choisis une quantité et un moment.",
       axes:[
         {id:'v', lbl:'Combien de fois ?', opts:[['a','une fois'],['b','deux fois'],['c','trois fois'],['d','aux huit heures']]},
         {id:'q', lbl:'Quand ?', opts:[['1','avec de la nourriture'],['2','au coucher']]}],
       out:{
         a1:{w:["Un comprimé une fois par jour, avec de la nourriture."], say:"Un comprimé une fois par jour, avec de la nourriture.", n:'la posologie la plus simple'},
         a2:{w:["Un comprimé une fois par jour, au coucher."], say:"Un comprimé une fois par jour, au coucher.", n:'souvent pour dormir'},
         b1:{w:["Un comprimé deux fois par jour, avec de la nourriture."], say:"Un comprimé deux fois par jour, avec de la nourriture.", n:'matin et soir'},
         b2:{w:["Un comprimé deux fois par jour, dont un au coucher."], say:"Un comprimé deux fois par jour, dont un au coucher.", n:'le soir compte comme une prise'},
         c1:{w:["Un comprimé trois fois par jour, avec de la nourriture."], say:"Un comprimé trois fois par jour, avec de la nourriture.", n:"celle de l'étiquette de Nadia"},
         c2:{w:["Trois fois par jour, et le dernier au coucher."], say:"Trois fois par jour, et le dernier au coucher.", n:'matin, midi, coucher'},
         d1:{w:["Un comprimé aux huit heures, avec de la nourriture."], say:"Un comprimé aux huit heures, avec de la nourriture.", n:'huit heures entre deux prises'},
         d2:{w:["Un comprimé aux huit heures, même la nuit."], say:"Un comprimé aux huit heures, même la nuit.", n:'huit phrases toutes prêtes'},
       },
       note:"Répète la posologie à voix haute devant le pharmacien avant de partir : c'est la meilleure vérification qui existe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases d'étiquette.",
       rows:[
         ["Un comprimé, trois fois par jour.","la plus fréquente"],
         ["Deux fois par semaine, le lundi et le jeudi.","par semaine"],
         ["Prenez ce médicament aux huit heures.","la formule québécoise"],
         ["Ce comprimé se prend après les repas.","estomac plein"],
         ["Ce sirop se prend avant les repas.","estomac vide"],
         ["Une fois par jour, le soir, au coucher.","les trois renseignements ensemble"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["comprendre « aux huit heures » comme une heure","croire qu'il faut le prendre à 8 h du matin",
          "Non : c'est l'écart entre deux comprimés. À 8 h, à 16 h, à minuit, par exemple."],
         ["mettre le mot au pluriel après « par »","« trois fois par jours »",
          "Après <b>par</b>, le mot reste au singulier : trois fois par <b>jour</b>, deux fois par <b>semaine</b>."],
         ["croire que « avec de la nourriture » veut dire un gros repas","attendre le souper pour prendre son comprimé",
          "Une rôtie, un yogourt, un verre de lait suffisent. Le but est seulement de ne pas avoir l'estomac vide."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Trois fois par jour » veut dire…", opts:["matin, midi et soir","trois comprimés le matin"], ok:0,
          fb:"Trois moments, un comprimé chaque fois."},
         {q:"« Aux huit heures » veut dire…", opts:["à 8 h du matin","huit heures entre deux prises"], ok:1,
          fb:"C'est un écart, pas une heure."},
         {q:"« Avec de la nourriture » veut dire…", opts:["l'estomac vide","pendant ou juste après avoir mangé"], ok:1,
          fb:"Jamais l'estomac vide."},
         {q:"On écrit…", opts:["trois fois par jour","trois fois par jours"], ok:0,
          fb:"Après « par », le mot reste au singulier."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre questions à te poser devant une étiquette : <b>combien</b> de comprimés, <b>combien de fois</b> par jour, <b>quand</b> par rapport au repas, <b>pendant combien de jours</b>. Si une réponse manque, demande-la au pharmacien avant de sortir."},
    ]
  },

  t3imperatif: {
    eye:'Mini-leçon', tit:"Prenez, agitez, ne prenez pas",
    blocs:[
      {t:'texte', h:"Comment l'étiquette te parle",
       p:"Une étiquette de pharmacie ne raconte rien : elle donne des ordres, poliment. Le verbe est en premier, il finit par <b>-ez</b>, et il n'y a pas de « vous » devant : <b>Prenez</b> un comprimé. <b>Agitez</b> avant usage. <b>Gardez</b> au froid. C'est ce qu'on appelle l'impératif.",
       note:"Le même temps sert partout dans la vie quotidienne : les recettes, les consignes de sécurité, les instructions d'un appareil."},

      {t:'ana', h:"Donner la consigne : le verbe en premier",
       p:"On enlève le « vous », on garde le verbe.",
       mots:[['Vous prenez →','{prenez} un comprimé'],['Vous agitez →','{agitez} avant d\'ouvrir',true],['Vous gardez →','gardez au froid']],
       say:"Prenez un comprimé. Agitez avant d'ouvrir.",
       note:"C'est la forme que le pharmacien emploie aussi quand il te parle : « Prenez-le avec de la nourriture. »"},

      {t:'ana', h:"Dire de ne pas faire : ne… pas",
       p:"Le petit mot devant, l'autre derrière.",
       mots:[['On dit','{ne prenez pas} deux comprimés'],['Aussi','{n\'arrêtez pas} avant sept jours',true],['La règle','ne devant le verbe, pas derrière']],
       say:"Ne prenez pas deux comprimés en même temps.",
       note:"Devant une voyelle, « ne » devient « n' » : <b>n'</b>arrêtez pas, <b>n'</b>ouvrez pas."},

      {t:'ana', h:"La forme écrite, sans personne : ne pas + infinitif",
       p:"Sur les boîtes, on écrit souvent le verbe sans le conjuguer.",
       mots:[['On écrit','{ne pas donner} aux enfants'],['Aussi','{ne pas conserver} après cette date',true],['Ça veut dire','la même chose que « ne donnez pas »']],
       say:"Ne pas donner aux enfants de moins de six ans.",
       note:"Cette forme s'adresse à tout le monde à la fois. Tu la verras sur presque toutes les boîtes de médicaments."},

      {t:'ana', h:"Rincer et terminer : deux verbes des conseils",
       p:"Deux mots du programme, et ce qu'ils demandent vraiment.",
       mots:[['rincer','{rincez} votre bouche après chaque dose'],['terminer','{terminez} le traitement, même si ça va mieux',true],['Attention','arrêter trop tôt fait revenir la maladie']],
       say:"Rincez votre bouche. Terminez le traitement.",
       note:"« Terminez le traitement » est le conseil que les pharmaciens répètent le plus souvent, et celui qu'on oublie le plus."},

      {t:'labo', h:"Écris la consigne",
       p:"Choisis une action et une forme.",
       axes:[
         {id:'v', lbl:'Quelle action ?', opts:[['a','prendre un comprimé'],['b','agiter la bouteille'],['c','donner aux enfants'],['d','terminer le traitement']]},
         {id:'q', lbl:'Quelle forme ?', opts:[['1','faire'],['2','ne pas faire']]}],
       out:{
         a1:{w:["Prenez un comprimé trois fois par jour."], say:"Prenez un comprimé trois fois par jour.", n:'la consigne de base'},
         a2:{w:["Ne prenez pas deux comprimés en même temps."], say:"Ne prenez pas deux comprimés en même temps.", n:'ne… pas'},
         b1:{w:["Agitez la bouteille avant d'ouvrir."], say:"Agitez la bouteille avant d'ouvrir.", n:'pour les sirops'},
         b2:{w:["N'ouvrez pas la bouteille sans l'agiter."], say:"N'ouvrez pas la bouteille sans l'agiter.", n:"ne devient n' devant une voyelle"},
         c1:{w:["Donnez une cuillère au coucher."], say:"Donnez une cuillère au coucher.", n:'consigne pour un enfant'},
         c2:{w:["Ne pas donner aux enfants de moins de six ans."], say:"Ne pas donner aux enfants de moins de six ans.", n:'la forme écrite des boîtes'},
         d1:{w:["Terminez le traitement, même si ça va mieux."], say:"Terminez le traitement, même si ça va mieux.", n:'le conseil le plus répété'},
         d2:{w:["N'arrêtez pas avant la fin des sept jours."], say:"N'arrêtez pas avant la fin des sept jours.", n:'huit consignes toutes prêtes'},
       },
       note:"Les deux formes disent la même chose : « terminez » et « n'arrêtez pas ». Choisis celle que tu comprends le mieux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six consignes d'étiquette.",
       rows:[
         ["Prenez un comprimé trois fois par jour.","la consigne de base"],
         ["Agitez la bouteille avant d'ouvrir.","pour les sirops"],
         ["Ne prenez pas deux comprimés en même temps.","ne… pas"],
         ["Ne pas donner aux enfants de moins de six ans.","la forme écrite"],
         ["Rincez votre bouche après chaque dose.","un verbe du programme"],
         ["Terminez le traitement, même si ça va mieux.","le conseil le plus important"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire le « vous »","« vous prenez un comprimé » sur une consigne",
          "Ce n'est pas faux, mais ce n'est pas la forme de l'étiquette. La consigne commence par le verbe : <b>Prenez</b>."],
         ["oublier le « ne »","« prenez pas deux comprimés »",
          "À l'oral, beaucoup de gens laissent tomber le « ne ». À l'écrit, il reste obligatoire : <b>ne</b> prenez <b>pas</b>."],
         ["conjuguer après « ne pas »","« ne pas donnez aux enfants »",
          "Dans la forme écrite des boîtes, le verbe ne se conjugue pas : ne pas <b>donner</b>, ne pas <b>conserver</b>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La consigne d'une étiquette commence par…", opts:["le verbe","le mot vous"], ok:0,
          fb:"Prenez, agitez, gardez."},
         {q:"Pour dire de ne pas faire, on met…", opts:["ne devant, pas derrière","pas devant seulement"], ok:0,
          fb:"Le verbe est pris entre les deux."},
         {q:"« Ne pas donner aux enfants » s'adresse…", opts:["à une seule personne","à tout le monde"], ok:1,
          fb:"C'est la forme écrite, sans personne nommée."},
         {q:"« Terminez le traitement » veut dire…", opts:["arrête quand tu vas mieux","prends tous les comprimés"], ok:1,
          fb:"Même si ça va mieux avant."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le verbe en premier, et il finit par <b>-ez</b> : <b>Prenez</b>, <b>Agitez</b>, <b>Gardez</b>, <b>Rincez</b>, <b>Terminez</b>. Pour interdire, deux formes : <b>ne prenez pas</b> quand on te parle, <b>ne pas prendre</b> quand c'est écrit sur la boîte."},
    ]
  },

  t3plusde: {
    eye:'Mini-leçon', tit:'De plus de, de moins de, pas plus de',
    blocs:[
      {t:'texte', h:"Les chiffres qui protègent",
       p:"Les mises en garde d'un médicament sont presque toujours des chiffres : un âge, un nombre de comprimés, un nombre d'heures. Autour de ces chiffres, quatre expressions reviennent — <b>de plus de</b>, <b>de moins de</b>, <b>pas plus de</b>, <b>au moins</b> — et le programme de niveau 3 les nomme explicitement pour cette situation.",
       note:"Se tromper ici n'est pas une faute de français ordinaire : c'est prendre un médicament de travers. Prends le temps."},

      {t:'ana', h:"Les enfants trop jeunes : de moins de",
       p:"En dessous de ce chiffre, c'est interdit.",
       mots:[['On lit','ne pas donner aux enfants {de moins de} six ans'],['Ça veut dire','cinq ans : interdit · sept ans : permis',true],['Sur la boîte','on écrit parfois « 6 ans + »']],
       say:"Ne pas donner aux enfants de moins de six ans.",
       note:"Six ans exactement ? La règle est « moins de six » : à six ans, c'est permis. Dans le doute, demande au pharmacien."},

      {t:'ana', h:"Les personnes assez âgées : de plus de",
       p:"Au-dessus de ce chiffre, c'est permis.",
       mots:[['On lit','pour les adultes {de plus de} dix-huit ans'],['Ça veut dire','dix-neuf ans : permis · seize ans : non',true],['Aussi','si la toux dure {plus de} sept jours, consultez']],
       say:"Pour les adultes de plus de dix-huit ans.",
       note:"« Plus de » sert aussi aux durées : plus de sept jours, plus de deux semaines. C'est le signal d'aller consulter."},

      {t:'ana', h:"La limite à ne pas dépasser : pas plus de",
       p:"Le maximum d'une journée.",
       mots:[['On lit','{pas plus de} quatre comprimés par jour'],['Ça veut dire','quatre : correct · cinq : dangereux',true],['Ailleurs','« maximum 4 par 24 heures » dit la même chose']],
       say:"Pas plus de quatre comprimés par jour.",
       note:"C'est la mise en garde la plus importante des médicaments en vente libre : beaucoup de gens dépassent sans le savoir."},

      {t:'ana', h:"Le minimum à respecter : au moins",
       p:"En dessous, c'est trop tôt.",
       mots:[['On lit','attendez {au moins} quatre heures entre deux doses'],['Ça veut dire','quatre heures : correct · deux heures : trop tôt',true],['Aussi','buvez {au moins} un grand verre d\'eau']],
       say:"Attendez au moins quatre heures entre deux doses.",
       note:"« Au moins » et « pas plus de » sont les deux bornes : l'une dit le minimum, l'autre le maximum."},

      {t:'labo', h:"Lis la mise en garde",
       p:"Choisis un type de limite et un chiffre.",
       axes:[
         {id:'v', lbl:'Quelle limite ?', opts:[['a','un âge minimum'],['b','un âge adulte'],['c','un maximum par jour'],['d','une attente minimale']]},
         {id:'q', lbl:'Quel chiffre ?', opts:[['1','le plus petit'],['2','le plus grand']]}],
       out:{
         a1:{w:["Ne pas donner aux enfants de moins de six ans."], say:"Ne pas donner aux enfants de moins de six ans.", n:'très fréquent sur les sirops'},
         a2:{w:["Ne pas donner aux enfants de moins de douze ans."], say:"Ne pas donner aux enfants de moins de douze ans.", n:'pour les comprimés'},
         b1:{w:["Pour les adultes de plus de dix-huit ans."], say:"Pour les adultes de plus de dix-huit ans.", n:'la limite adulte'},
         b2:{w:["Pour les personnes de plus de soixante-cinq ans, demandez conseil."], say:"Pour les personnes de plus de soixante-cinq ans, demandez conseil.", n:'une autre borne fréquente'},
         c1:{w:["Pas plus de deux comprimés par jour."], say:"Pas plus de deux comprimés par jour.", n:'maximum serré'},
         c2:{w:["Pas plus de quatre comprimés par jour."], say:"Pas plus de quatre comprimés par jour.", n:'le maximum le plus courant'},
         d1:{w:["Attendez au moins quatre heures entre deux doses."], say:"Attendez au moins quatre heures entre deux doses.", n:'minimum'},
         d2:{w:["Attendez au moins huit heures entre deux doses."], say:"Attendez au moins huit heures entre deux doses.", n:'huit phrases toutes prêtes'},
       },
       note:"Relis toujours ces phrases deux fois. Ce sont les seules d'une étiquette où une erreur coûte cher."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mises en garde.",
       rows:[
         ["Ne pas donner aux enfants de moins de six ans.","âge minimum"],
         ["Pour les adultes de plus de dix-huit ans.","âge adulte"],
         ["Pas plus de quatre comprimés par jour.","maximum"],
         ["Attendez au moins quatre heures entre deux doses.","minimum"],
         ["Si la toux dure plus de sept jours, consultez un médecin.","durée"],
         ["Gardez hors de la portée des enfants.","la mise en garde de toutes les boîtes"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre « moins de » et « plus de »","donner à un enfant de cinq ans un sirop marqué « 6 ans et plus »",
          "Cinq ans, c'est <b>moins de</b> six : c'est interdit. Compare toujours le chiffre de la boîte avec l'âge réel."],
         ["oublier « pas » dans « pas plus de »","lire « plus de quatre comprimés par jour »",
          "Sans le « pas », la phrase dit le contraire. C'est le mot le plus court de la mise en garde et le plus important."],
         ["additionner deux médicaments","prendre deux marques différentes le même jour",
          "Deux boîtes peuvent contenir le même médicament sous deux noms. Demande au pharmacien avant de mélanger."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Enfants de moins de six ans » : un enfant de cinq ans…", opts:["peut en prendre","ne peut pas en prendre"], ok:1,
          fb:"Cinq, c'est moins de six."},
         {q:"« Pas plus de quatre par jour » : cinq comprimés, c'est…", opts:["correct","trop"], ok:1,
          fb:"Quatre est le maximum."},
         {q:"« Au moins quatre heures » : attendre deux heures, c'est…", opts:["trop tôt","correct"], ok:0,
          fb:"Quatre heures est le minimum."},
         {q:"« Si ça dure plus de sept jours »…", opts:["continue le sirop","va voir un médecin"], ok:1,
          fb:"C'est le signal d'aller consulter."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux bornes et deux comparaisons : <b>au moins</b> dit le minimum, <b>pas plus de</b> dit le maximum, <b>de moins de</b> désigne les plus jeunes, <b>de plus de</b> les plus âgés. Devant un chiffre que tu ne comprends pas, une seule bonne réponse : demande au pharmacien."},
    ]
  },
};
