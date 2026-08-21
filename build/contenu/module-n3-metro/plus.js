const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le « in » de lundi et le « an » de trente",
    blocs:[
      {t:'texte', h:"Deux sons qui passent par le nez",
       p:"Au comptoir, presque tout ce qu'on entend est un nombre : un prix, un jour, un âge, une heure. Or les nombres français sont pleins de deux sons qui se ressemblent et qui sortent tous les deux par le nez : le <b>in</b> de « l<b>un</b>di » et le <b>an</b> de « tr<b>en</b>te ». Si on les confond, « v<b>in</b>gt » devient « v<b>en</b>t » et « c<b>in</b>q » devient « s<b>an</b>g ».",
       note:"Ce qui change, c'est la bouche : <b>étirée sur les côtés</b> pour « in », <b>bien ouverte</b> pour « an ». Mets ta main devant ta bouche : pour « an », l'air sort plus large."},

      {t:'ana', h:"Le son « in » — la bouche étirée",
       p:"C'est le son de « lundi », « un », « combien », « moins ».",
       mots:[['On écrit','l{un}di'],['Aussi','{un}, comb{ien}, mo{ins}',true],['La bouche','étirée sur les côtés, presque un sourire']],
       say:"Lundi, un passage, combien, moins cher.",
       note:"Il s'écrit de plusieurs façons : <b>un</b> (lundi), <b>in</b> (matin), <b>ain</b> (main), <b>ien</b> (combien), <b>oin</b> (moins). Le son est le même partout."},

      {t:'ana', h:"Le son « an » — la bouche ouverte",
       p:"C'est le son de « trente », « cent », « comptant », « dimanche ».",
       mots:[['On écrit','tr{en}te'],['Aussi','c{ent}, compt{ant}, dim{an}che',true],['La bouche','bien ouverte, la langue à plat']],
       say:"Trente, cent dix dollars, comptant, dimanche.",
       note:"Il s'écrit <b>an</b> (dimanche) ou <b>en</b> (trente). Devant un p ou un b, on écrit <b>am</b> ou <b>em</b>."},

      {t:'ana', h:"Les nombres où les deux sons se suivent",
       p:"Trois nombres du guichet portent les deux sons dans le même mot. Ce sont les plus difficiles.",
       mots:[['vingt-cinq','v{in}gt-c{in}q — deux fois le son in'],['soixante-quinze','soix{an}te-qu{in}ze — an, puis in',true],['cent vingt','c{ent} v{in}gt — an, puis in']],
       say:"Vingt-cinq. Soixante-quinze. Cent vingt.",
       note:"« Trois dollars soixante-quinze » et « cent vingt minutes » sont les deux expressions les plus fréquentes du module. Dis-les lentement, en deux morceaux."},

      {t:'labo', h:"Écoute les paires",
       p:"Choisis une paire et écoute la différence.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','un / an'],
         ['b','vingt / vent'],
         ['c','lundi / dimanche'],
         ['d','combien / comptant'],
         ['e','dans une phrase']]}],
       out:{
         a:{w:['{un} / {an}'], say:"Un. An.", n:'la bouche étirée, puis ouverte'},
         b:{w:['v{in}gt / v{en}t'], say:"Vingt. Vent.", n:'un nombre et un mot de météo'},
         c:{w:['l{un}di / dim{an}che'], say:"Lundi. Dimanche.", n:'les deux bornes de l’hebdo'},
         d:{w:['comb{ien} / compt{ant}'], say:"Combien. Comptant.", n:'les deux mots de la caisse'},
         e:{w:["« Trente-cinq dollars, comptant ou par carte ? »"], say:"Trente-cinq dollars, comptant ou par carte ?", n:'les deux sons quatre fois'},
       },
       note:"Écoute chaque paire deux fois : la première pour comprendre, la seconde en fermant les yeux."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases entendues au comptoir.",
       rows:[
         ["Un passage, s'il vous plaît.","in deux fois"],
         ["Trente-cinq dollars.","an une fois"],
         ["C'est combien ?","in une fois"],
         ["Du lundi au dimanche.","in puis an"],
         ["Cent dix dollars pour le mois.","an deux fois"],
         ["Trois dollars soixante-quinze.","an puis in"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre vingt et vent","dire « vent-cinq » pour « vingt-cinq »",
          "C'est le piège le plus coûteux : au guichet, un nombre mal dit fait payer le mauvais prix. Étire bien la bouche pour « vingt »."],
         ["prononcer le n","dire « lun-ne-di » en détachant le n",
          "Non : le n ne se prononce pas tout seul, il colore la voyelle. C'est le nez qui travaille, pas la langue."],
         ["oublier que « en » se dit « an »","lire « trente » avec un e ordinaire",
          "Dans « tr<b>en</b>te », les lettres e-n donnent exactement le même son que a-n dans « dim<b>an</b>che ». Deux écritures, un seul son."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Lundi » a le son…", opts:["in","an"], ok:0,
          fb:"La bouche est étirée, presque un sourire."},
         {q:"« Comptant » a le son…", opts:["in","an"], ok:1,
          fb:"La bouche est bien ouverte."},
         {q:"Dans « trente », les lettres e-n donnent le son…", opts:["in","an"], ok:1,
          fb:"Deux écritures, un seul son : an."},
         {q:"Dans « soixante-quinze », on entend…", opts:["deux fois le même son","an puis in"], ok:1,
          fb:"soix<b>an</b>te, puis qu<b>in</b>ze."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux mots repères, et rien d'autre : <b>lundi</b> pour le son « in », <b>trente</b> pour le son « an ». Devant un nombre nouveau, dis-le à côté de l'un des deux, et laisse l'air passer par le nez."},
    ]
  },

  prPrix: {
    eye:'Mini-leçon', tit:"Dire un prix, écrire un prix",
    blocs:[
      {t:'texte', h:"Un prix a deux parties",
       p:"En français, un prix se dit en deux morceaux : d'abord les <b>dollars</b>, ensuite les <b>cents</b>. « 3,75 $ » se dit <b>trois dollars soixante-quinze</b>. Le mot « cents » ne se dit presque jamais à la fin — on s'arrête après le nombre.",
       note:"Au comptoir, on entend surtout la forme courte : <b>trois soixante-quinze</b>. Le mot « dollars » saute. Ce n'est pas du mauvais français, c'est du français parlé normal."},

      {t:'ana', h:"La virgule, pas le point",
       p:"C'est la différence d'écriture la plus visible avec beaucoup d'autres pays.",
       mots:[['On écrit','3,75 $'],['On n’écrit pas','3.75 $',true],['Le signe','après le nombre, avec une espace']],
       say:"Trois dollars soixante-quinze. Trente-trois dollars vingt-cinq.",
       note:"Le signe de dollar se met <b>après</b> le nombre en français : 110 $, et non $110. Sur la grille affichée, c'est toujours écrit ainsi."},

      {t:'ana', h:"Les trois dizaines qui piègent",
       p:"À partir de soixante-dix, le français compte autrement. Ces trois-là reviennent dans tous les prix du transport.",
       mots:[['70','soix{an}te-dix — soixante plus dix'],['80','quatre-v{in}gts — quatre fois vingt',true],['90','quatre-v{in}gt-dix — quatre fois vingt, plus dix']],
       say:"Soixante-dix. Quatre-vingts. Quatre-vingt-dix.",
       note:"Et « soixante-quinze », qu'on entend dans presque tous les prix du transport, se lit : soixante, plus quinze."},

      {t:'ana', h:"Les quatre façons de demander le prix",
       p:"De la plus courte à la plus polie. Toutes les quatre s'entendent au guichet.",
       mots:[['La plus courte',"{c'est combien} ?"],['La plus fréquente',"ça coûte {combien} ?",true],['Avec le nom du titre','{combien coûte le mensuel} ?'],['La plus polie','{combien est-ce que je vous dois} ?']],
       say:"C'est combien ? Ça coûte combien ? Combien coûte le mensuel ?",
       note:"La dernière sert au moment de payer, quand le prix a déjà été dit une fois et qu'on veut le confirmer."},

      {t:'labo', h:"Le prix, dit et écrit",
       p:"Choisis un prix de la grille et écoute-le.",
       axes:[{id:'p', lbl:'Quel prix ?', opts:[
         ['a','3,75 $ — un passage'],
         ['b','35,00 $ — dix passages'],
         ['c','33,25 $ — l’hebdo'],
         ['d','110,00 $ — le mensuel'],
         ['e','6,75 $ — la soirée']]}],
       out:{
         a:{w:['trois dollars soix{an}te-qu{in}ze'], say:"Trois dollars soixante-quinze.", n:'la forme courte : trois soixante-quinze'},
         b:{w:['tr{en}te-c{in}q dollars'], say:"Trente-cinq dollars.", n:'pas de cents : on s’arrête là'},
         c:{w:['tr{en}te-trois dollars v{in}gt-c{in}q'], say:"Trente-trois dollars vingt-cinq.", n:'la forme courte : trente-trois vingt-cinq'},
         d:{w:['c{ent} dix dollars'], say:"Cent dix dollars.", n:'le prix du mois'},
         e:{w:['six dollars soix{an}te-qu{in}ze'], say:"Six dollars soixante-quinze.", n:'de dix-huit heures à cinq heures'},
       },
       note:"Répète chaque prix deux fois, puis écris-le en chiffres sans regarder."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six prix de la grille de la zone A.",
       rows:[
         ["Trois dollars soixante-quinze.","un passage"],
         ["Deux dollars soixante-quinze.","un passage à tarif réduit"],
         ["Trente-cinq dollars.","dix passages"],
         ["Trente-trois dollars vingt-cinq.","l'hebdo"],
         ["Cent dix dollars.","le mensuel"],
         ["Soixante-six dollars.","le mensuel à tarif réduit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire le prix avec un point","3.75 $ au lieu de 3,75 $",
          "En français, la virgule sépare les dollars des cents. Le point sert à séparer les milliers, et encore, on emploie plutôt une espace : 1 250 $."],
         ["mettre le signe avant le nombre","$110 au lieu de 110 $",
          "Le signe de dollar se place après le nombre, séparé par une espace. C'est ainsi sur toutes les grilles affichées."],
         ["dire « soixante-quinze cents » à la fin","« trois dollars soixante-quinze cents »",
          "On ne dit pas « cents » à la fin. On s'arrête au nombre : trois dollars soixante-quinze."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Trente-trois vingt-cinq » s'écrit…", opts:["33,25 $","33.25 $"], ok:0,
          fb:"Avec une virgule, et le signe après."},
         {q:"Le nombre 90 se dit…", opts:["nonante","quatre-vingt-dix"], ok:1,
          fb:"Quatre fois vingt, plus dix."},
         {q:"Au comptoir, on entend le plus souvent…", opts:["trois dollars soixante-quinze","trois soixante-quinze"], ok:1,
          fb:"La forme courte, sans « dollars »."},
         {q:"Pour demander le prix, on dit…", opts:["C'est combien ?","C'est quoi le prix de combien ?"], ok:0,
          fb:"Trois mots suffisent."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Les dollars d'abord, les cents ensuite, une <b>virgule</b> entre les deux et le <b>$</b> après le nombre. Pour demander : <b>C'est combien ?</b> Pour confirmer : <b>Combien est-ce que je vous dois ?</b>"},
    ]
  },

  t1demons: {
    eye:'Mini-leçon', tit:"Ce, cet, cette, ces — montrer une chose du doigt",
    blocs:[
      {t:'texte', h:"Le mot qui remplace le doigt",
       p:"Devant une grille affichée au mur, on ne connaît pas le nom de tout. On montre : « Combien coûte <b>ce</b> titre-là ? » Ces quatre petits mots — <b>ce</b>, <b>cet</b>, <b>cette</b>, <b>ces</b> — servent exactement à ça : désigner la chose qu'on a sous les yeux, sans avoir à la nommer.",
       note:"Ils remplacent « le », « la », « les ». On ne dit jamais « le ce titre » : on choisit l'un ou l'autre."},

      {t:'ana', h:"Devant un mot masculin : ce",
       p:"Le titre, le passage, le comptoir, le prix, le tarif.",
       mots:[['On dit','{ce} titre'],['Aussi','{ce} passage, {ce} comptoir',true],['Et','{ce} tarif']],
       say:"Ce titre, ce passage, ce comptoir.",
       note:"Si tu peux dire « un titre », c'est masculin : ce sera « ce »."},

      {t:'ana', h:"Devant une voyelle : cet",
       p:"Autobus, appareil, argent, horaire commencent par une voyelle ou un h muet.",
       mots:[['On dit','{cet} autobus'],['Aussi','{cet} appareil, {cet} argent',true],['Jamais','« ce autobus »']],
       say:"Cet autobus, cet appareil, cet horaire.",
       note:"« Cet » se prononce comme « cette », mais s'écrit sans les deux dernières lettres. C'est le mot masculin qui change de forme, pas le genre du nom."},

      {t:'ana', h:"Devant un mot féminin : cette",
       p:"La carte, la zone, la semaine, la borne, la place.",
       mots:[['On dit','{cette} carte'],['Aussi','{cette} zone, {cette} semaine',true],['Et','{cette} place']],
       say:"Cette carte, cette zone, cette semaine.",
       note:"Si tu peux dire « une carte », c'est féminin : ce sera « cette »."},

      {t:'ana', h:"Devant un pluriel : ces",
       p:"Un seul mot pour le masculin et le féminin, dès qu'il y a plusieurs choses.",
       mots:[['Masculin pluriel','{ces} titres, {ces} prix'],['Féminin pluriel','{ces} cartes, {ces} places',true],['Toujours','{ces}, jamais autre chose']],
       say:"Ces titres, ces prix, ces cartes, ces places.",
       note:"Au pluriel, plus de choix à faire : c'est « ces » dans tous les cas."},

      {t:'ana', h:"Le « -là » qu'on ajoute au Québec",
       p:"À l'oral, on ajoute presque toujours <b>-là</b> après le nom. Ça veut dire : celui que je te montre, pas un autre.",
       mots:[['Au comptoir','{ce titre-là}'],['Aussi','{cette carte-là}, ces prix-{là}',true],['Ce que ça dit','celui-ci, devant nous, pas un autre']],
       say:"Ce titre-là. Cette carte-là. Ces prix-là.",
       note:"Le trait d'union est obligatoire à l'écrit : ce titre<b>-là</b>. À l'oral, tu l'entendras dans presque toutes les phrases du guichet."},

      {t:'labo', h:"Choisis le bon mot",
       p:"Choisis un nom et vois quel petit mot va devant.",
       axes:[{id:'n', lbl:'Quel nom ?', opts:[
         ['a','titre — masculin'],
         ['b','autobus — voyelle'],
         ['c','carte — féminin'],
         ['d','prix — pluriel'],
         ['e','tous à la suite']]}],
       out:{
         a:{w:['{ce} titre-là'], say:"Ce titre-là.", n:'masculin, consonne'},
         b:{w:['{cet} autobus-là'], say:"Cet autobus-là.", n:'masculin, mais voyelle'},
         c:{w:['{cette} carte-là'], say:"Cette carte-là.", n:'féminin'},
         d:{w:['{ces} prix-là'], say:"Ces prix-là.", n:'pluriel'},
         e:{w:['{ce} titre · {cet} autobus · {cette} carte · {ces} prix'], say:"Ce titre, cet autobus, cette carte, ces prix.", n:'les quatre formes de suite'},
       },
       note:"Répète les quatre à la suite : l'oreille finit par choisir toute seule."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Combien coûte ce titre-là ?","masculin"],
         ["Est-ce que cette carte-là est encore bonne ?","féminin"],
         ["Cet autobus-là va vers le nord.","voyelle"],
         ["Je ne comprends pas ces prix-là.","pluriel"],
         ["Cette zone-là, c'est la zone A.","féminin"],
         ["Ces deux titres-là coûtent le même prix.","pluriel"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ce » devant une voyelle","« ce autobus » au lieu de « cet autobus »",
          "Deux voyelles ne se suivent pas facilement en français. On ajoute un t pour faire la liaison : ce-t-autobus."],
         ["confondre « ces » et « ses »","« ses prix-là » au lieu de « ces prix-là »",
          "« ces » montre du doigt : ces prix, là, sur la grille. « ses » dit à qui c'est : ses prix à lui. Deux mots différents, même son."],
         ["oublier le trait d'union","« ce titre là » en deux mots",
          "À l'écrit, le <b>-là</b> se colle au nom avec un trait d'union : ce titre-là. C'est une seule expression."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant « autobus », on met…", opts:["ce","cet"], ok:1,
          fb:"Le mot commence par une voyelle."},
         {q:"Devant « carte », on met…", opts:["ce","cette"], ok:1,
          fb:"« une carte » : c'est féminin."},
         {q:"Devant « prix » au pluriel, on met…", opts:["ces","cette"], ok:0,
          fb:"Au pluriel, c'est toujours « ces »."},
         {q:"« Ce titre-là » veut dire…", opts:["un titre en général","celui que je montre"], ok:1,
          fb:"Le « -là » désigne ce qu'on a sous les yeux."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Quatre formes, une seule question à se poser : masculin (<b>ce</b>), masculin devant une voyelle (<b>cet</b>), féminin (<b>cette</b>), pluriel (<b>ces</b>). Et au comptoir, ajoute <b>-là</b> : c'est ce qui remplace le doigt."},
    ]
  },

  t2quest: {
    eye:'Mini-leçon', tit:"Poser sa question au comptoir",
    blocs:[
      {t:'texte', h:"Trois façons, une seule à retenir d'abord",
       p:"Le français pose ses questions de trois façons. Deux sont faciles, une est difficile. Au guichet, une seule suffit vraiment : celle avec <b>est-ce que</b>. Elle marche partout, elle ne demande de changer aucun mot de place, et personne ne la trouvera bizarre.",
       note:"Le programme de niveau 3 nomme précisément ce point : les phrases interrogatives. C'est le savoir qui rend possible toute l'intention de production orale du module."},

      {t:'ana', h:"La première façon : la voix qui monte",
       p:"On garde la phrase telle quelle et on monte la voix à la fin. C'est ce qu'on entend le plus souvent entre gens pressés.",
       mots:[['Affirmation','C’est trois dollars.'],['Question',"{c'est combien} ?",true],['Ce qui change','rien, sauf la voix']],
       say:"C'est combien ? Ça coûte combien ?",
       note:"Très fréquente, très naturelle. Le seul risque : si la voix ne monte pas assez, on ne comprend pas que c'est une question."},

      {t:'ana', h:"La deuxième façon : est-ce que",
       p:"On pose « est-ce que » devant la phrase et on ne touche à rien d'autre. C'est la façon la plus sûre.",
       mots:[['Affirmation','Je peux payer par carte.'],['Question','{est-ce que je peux payer par carte} ?',true],['Ce qui change','deux mots ajoutés devant']],
       say:"Est-ce que je peux payer par carte ? Est-ce que je peux payer comptant ?",
       note:"C'est celle à apprendre en premier. Elle fonctionne avec n'importe quelle phrase, sans exception."},

      {t:'ana', h:"La troisième façon : les mots de question",
       p:"Combien, où, quand, comment, pourquoi. Ils se mettent <b>devant</b> « est-ce que ».",
       mots:[['Le prix','{combien coûte le mensuel} ?'],['Le lieu',"{où est-ce qu'on fait la photo} ?",true],['La fin',"{jusqu'à quand c'est bon} ?"]],
       say:"Combien coûte le mensuel ? Où est-ce qu'on fait la photo ?",
       note:"Devant une voyelle, « est-ce que » devient « est-ce qu' » : où <b>est-ce qu'</b>on fait la photo."},

      {t:'ana', h:"Faire répéter — la question la plus utile de toutes",
       p:"Au guichet, on parle vite et on donne des chiffres. Personne ne t'en voudra de faire répéter : c'est ce que font aussi les gens d'ici.",
       mots:[['Le plus court','{pardon} ?'],['Le plus poli','{pouvez-vous répéter} ?',true],['Le plus utile',"{plus lentement s'il vous plaît}"]],
       say:"Pardon ? Pouvez-vous répéter, s'il vous plaît ? Plus lentement, s'il vous plaît.",
       note:"Apprends ces trois-là par cœur. Elles servent dans toutes les situations du module et bien au-delà."},

      {t:'labo', h:"Les quatre questions du guichet",
       p:"Choisis ce que tu veux savoir.",
       axes:[{id:'q', lbl:'Tu veux savoir…', opts:[
         ['a','le prix'],
         ['b','jusqu’à quand c’est bon'],
         ['c','où faire la carte avec photo'],
         ['d','si tu peux payer par carte'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['{combien coûte le mensuel} ?'], say:"Combien coûte le mensuel ?", n:'un mot de question devant'},
         b:{w:["{jusqu'à quand c'est bon} ?"], say:"Jusqu'à quand c'est bon ?", n:'la durée du titre'},
         c:{w:["{où est-ce qu'on fait la photo} ?"], say:"Où est-ce qu'on fait la photo ?", n:'est-ce qu’ devant une voyelle'},
         d:{w:['{est-ce que je peux payer par carte} ?'], say:"Est-ce que je peux payer par carte ?", n:'la façon la plus sûre'},
         e:{w:['Combien ? · Jusqu’à quand ? · Où ? · Est-ce que je peux ?'], say:"Combien coûte le mensuel ? Jusqu'à quand c'est bon ? Où est-ce qu'on fait la photo ? Est-ce que je peux payer par carte ?", n:'prépare-les avant d’arriver'},
       },
       note:"Ces quatre questions couvrent presque tout ce qu'on a besoin de demander au comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six questions à avoir dans la bouche.",
       rows:[
         ["C'est combien ?","la voix monte"],
         ["Est-ce que je peux payer comptant ?","est-ce que"],
         ["Combien coûte le titre mensuel ?","mot de question"],
         ["Où est-ce qu'on fait la carte avec photo ?","est-ce qu' devant voyelle"],
         ["Jusqu'à quand est-ce que ce titre est bon ?","la durée"],
         ["Pardon, pouvez-vous répéter, s'il vous plaît ?","faire répéter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["changer les mots de place après « est-ce que »","« est-ce que puis-je payer »",
          "Non : après « est-ce que », la phrase reste exactement dans l'ordre normal. C'est justement pour ça qu'elle est facile."],
         ["oublier de monter la voix","dire « c'est combien » comme une affirmation",
          "Sans la montée de voix, la personne au comptoir n'entend pas une question. Fais monter la fin de la phrase."],
         ["ne pas oser faire répéter","hocher la tête sans avoir compris le prix",
          "C'est le piège qui coûte le plus cher, littéralement. « Pardon ? » est un mot poli et normal. Sers-t'en."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La façon la plus sûre de poser une question est…", opts:["avec est-ce que","en changeant les mots de place"], ok:0,
          fb:"Elle marche partout, sans rien déplacer."},
         {q:"Devant une voyelle, « est-ce que » devient…", opts:["est-ce qui","est-ce qu'"], ok:1,
          fb:"Où est-ce qu'on fait la photo ?"},
         {q:"Les mots de question se mettent…", opts:["devant est-ce que","après est-ce que"], ok:0,
          fb:"Combien est-ce que… · Où est-ce que…"},
         {q:"Quand tu n'as pas compris un prix…", opts:["tu fais oui de la tête","tu dis « pardon ? »"], ok:1,
          fb:"C'est normal et poli de faire répéter."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une seule à retenir d'abord : <b>est-ce que</b> devant la phrase, et rien d'autre à changer. Devant, ajoute <b>combien</b>, <b>où</b> ou <b>jusqu'à quand</b> selon ce que tu cherches. Et garde <b>« Pardon, pouvez-vous répéter ? »</b> toujours prête."},
    ]
  },

  t2modal: {
    eye:'Mini-leçon', tit:"Je voudrais, je peux, je dois, il faut",
    blocs:[
      {t:'texte', h:"Quatre verbes, quatre intentions différentes",
       p:"Toute la conversation du guichet tient sur quatre petits verbes. Ils ne disent pas la même chose : l'un <b>demande poliment</b>, l'autre <b>demande la permission</b>, le troisième dit ce que <b>je</b> suis obligé de faire, le quatrième ce que <b>tout le monde</b> est obligé de faire.",
       note:"Le programme de niveau 3 les appelle les auxiliaires de modalité. Ils sont suivis d'un verbe qui ne change jamais de forme, ce qui les rend faciles."},

      {t:'ana', h:"Je voudrais — la formule d'entrée",
       p:"C'est ce qu'on dit en arrivant devant le comptoir. Elle est polie sans être compliquée.",
       mots:[['On dit','{je voudrais un titre mensuel}'],['Aussi','{je voudrais acheter} un titre',true],['On évite','« je veux », qui sonne sec']],
       say:"Je voudrais un titre mensuel, s'il vous plaît.",
       note:"« Je voudrais » se dit aussi bien devant un nom (je voudrais un titre) que devant un verbe (je voudrais acheter). Ajoute « s'il vous plaît » : c'est presque obligatoire au Québec."},

      {t:'ana', h:"Est-ce que je peux — demander la permission",
       p:"On demande si c'est possible, si c'est permis. La réponse est oui ou non.",
       mots:[['On dit','{est-ce que je peux payer comptant} ?'],['Aussi','est-ce que je peux recharger ma carte ?',true],['Ce que ça demande','la permission, la possibilité']],
       say:"Est-ce que je peux payer comptant ? Est-ce que je peux recharger ma vieille carte ?",
       note:"Attention à ne pas confondre avec « je voudrais » : « je peux » demande la permission, « je voudrais » demande la chose."},

      {t:'ana', h:"Je dois — ce que moi je suis obligé de faire",
       p:"C'est une obligation qui me concerne, moi, à cause de ma situation.",
       mots:[['On dit',"{je dois apporter une preuve d'âge}"],['Aussi','je dois venir avec ma fille',true],['Qui est obligé','moi, personnellement']],
       say:"Je dois apporter une preuve d'âge. Je dois venir avec elle.",
       note:"« Je dois » change avec la personne : je dois, tu dois, elle doit, nous devons, vous devez, ils doivent."},

      {t:'ana', h:"Il faut — ce qui est obligatoire pour tout le monde",
       p:"C'est la règle, la même pour tous. « Il » ne désigne personne : c'est une forme figée.",
       mots:[['On dit','{il faut une carte avec photo}'],['Aussi','{il faut venir} avec la personne',true],['Qui est obligé','tout le monde, sans exception']],
       say:"Il faut une carte avec photo. Il faut valider son titre.",
       note:"« Il faut » ne change jamais : ni de personne, ni de forme. C'est le verbe le plus simple du français, et le plus utile pour dire une règle."},

      {t:'ana', h:"Ce qui vient après les quatre",
       p:"Le deuxième verbe garde toujours sa forme de base, celle du dictionnaire.",
       mots:[['Je voudrais','{je voudrais acheter} un titre'],['Est-ce que je peux','est-ce que je peux {payer} comptant ?',true],['Il faut','{il faut venir} avec elle']],
       say:"Je voudrais acheter. Je peux payer. Il faut venir.",
       note:"On ne dit jamais « je voudrais j'achète » ni « il faut je viens ». Un seul verbe se conjugue : le premier."},

      {t:'labo', h:"Le bon verbe selon ce que tu veux dire",
       p:"Choisis ton intention.",
       axes:[{id:'i', lbl:'Tu veux…', opts:[
         ['a','demander poliment une chose'],
         ['b','demander la permission'],
         ['c','dire ton obligation à toi'],
         ['d','dire la règle générale'],
         ['e','les quatre à la suite']]}],
       out:{
         a:{w:['{je voudrais un titre mensuel}'], say:"Je voudrais un titre mensuel, s'il vous plaît.", n:'la formule d’entrée'},
         b:{w:['{est-ce que je peux payer comptant} ?'], say:"Est-ce que je peux payer comptant ?", n:'oui ou non'},
         c:{w:["{je dois apporter une preuve d'âge}"], say:"Je dois apporter une preuve d'âge.", n:'moi, personnellement'},
         d:{w:['{il faut une carte avec photo}'], say:"Il faut une carte avec photo.", n:'la même règle pour tous'},
         e:{w:['je voudrais · est-ce que je peux · je dois · il faut'], say:"Je voudrais. Est-ce que je peux. Je dois. Il faut.", n:'les quatre verbes du guichet'},
       },
       note:"Une phrase par intention : c'est tout ce que demande un achat au comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du Défi 2.",
       rows:[
         ["Bonjour. Je voudrais un titre mensuel, s'il vous plaît.","demander poliment"],
         ["Est-ce que je peux payer par carte ?","demander la permission"],
         ["Est-ce que je dois acheter une nouvelle carte ?","mon obligation"],
         ["Pour le tarif réduit, il faut une carte avec photo.","la règle"],
         ["Il faut valider son titre en montant.","la règle"],
         ["Je voudrais acheter un titre pour le mois.","poliment, devant un verbe"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « je veux » au comptoir","« je veux un titre mensuel »",
          "Ce n'est pas faux, mais ça sonne sec, presque impoli. « Je voudrais » demande la même chose et ouvre bien mieux la conversation."],
         ["conjuguer le deuxième verbe","« je voudrais j'achète un titre »",
          "Un seul verbe se conjugue : le premier. Le second garde sa forme de base — acheter, payer, venir, valider."],
         ["confondre « il faut » et « je dois »","« il faut que j'apporte » quand on veut dire son obligation à soi",
          "« Il faut » dit la règle pour tous. « Je dois » dit ton obligation à toi. Les deux sont justes, mais ils ne disent pas la même chose."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour entrer poliment en conversation, on dit…", opts:["je veux","je voudrais"], ok:1,
          fb:"Et on ajoute « s'il vous plaît »."},
         {q:"« Il faut une carte avec photo » veut dire…", opts:["c'est la règle pour tous","c'est mon obligation à moi"], ok:0,
          fb:"« Il faut » ne désigne personne en particulier."},
         {q:"Après « je voudrais », le verbe est…", opts:["conjugué","à sa forme de base"], ok:1,
          fb:"Je voudrais acheter, je voudrais payer."},
         {q:"Pour demander la permission, on dit…", opts:["est-ce que je peux","est-ce que je dois"], ok:0,
          fb:"« Je peux » demande si c'est permis."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Je voudrais</b> pour entrer, <b>est-ce que je peux</b> pour demander la permission, <b>je dois</b> pour mon obligation, <b>il faut</b> pour la règle de tout le monde. Et le verbe qui suit ne bouge jamais."},
    ]
  },

  t3temps: {
    eye:'Mini-leçon', tit:"De, à, du, au, jusqu'à, pendant — lire une durée",
    blocs:[
      {t:'texte', h:"Une grille de tarifs est faite de durées",
       p:"Sur la grille affichée, chaque ligne dit deux choses : un prix et une <b>durée</b>. Et la durée tient toujours dans un ou deux petits mots. « Valide <b>de</b> 18 h <b>à</b> 5 h », « <b>du</b> lundi <b>au</b> dimanche », « bon <b>jusqu'à</b> la fin du mois ». Se tromper sur ces mots-là, c'est acheter le mauvais titre.",
       note:"Le programme de niveau 3 nomme les prépositions parmi ses savoirs. Ici, elles ne sont pas une leçon de grammaire : elles sont ce qui permet de lire le tableau."},

      {t:'ana', h:"De… à… — un début et une fin, avec des heures",
       p:"Le premier mot dit quand ça commence, le second quand ça finit.",
       mots:[['Sur la grille','{valide de dix-huit heures à cinq heures}'],['Aussi','de neuf heures à cinq heures',true],['Ce que ça dit','le début, puis la fin']],
       say:"Valide de dix-huit heures à cinq heures.",
       note:"« De 18 h à 5 h » traverse la nuit : ça commence le soir et ça finit le lendemain matin. La Soirée illimitée fonctionne ainsi."},

      {t:'ana', h:"Du… au… — un début et une fin, avec des jours",
       p:"Devant un jour de la semaine, « de » devient <b>du</b> et « à » devient <b>au</b>.",
       mots:[['Sur la grille','{du lundi au dimanche}'],['Aussi','du vendredi au lundi',true],['Jamais','« de lundi à dimanche »']],
       say:"L'hebdo est bon du lundi au dimanche.",
       note:"C'est une des rares règles sans exception : devant un jour ou un mois, c'est toujours <b>du… au…</b>"},

      {t:'ana', h:"Jusqu'à — seulement la fin",
       p:"On dit quand ça s'arrête, sans dire quand ça a commencé.",
       mots:[['Sur la grille',"{bon jusqu'à la fin du mois}"],['Aussi',"jusqu'à cinq heures du matin",true],['Ce que ça dit','la fin, rien d’autre']],
       say:"Ton titre est bon jusqu'à la fin du mois.",
       note:"Le mensuel se dit toujours ainsi : il finit le dernier jour du mois, peu importe le jour où tu l'as acheté."},

      {t:'ana', h:"À partir de — seulement le début",
       p:"C'est l'inverse de « jusqu'à ». On dit quand ça commence, et avant, ça ne marche pas.",
       mots:[['Sur la grille','{à partir de seize heures}'],['Aussi','à partir de la validation',true],['Ce que ça dit','le début, rien d’autre']],
       say:"Le Week-end illimité est valide à partir de seize heures.",
       note:"Le titre 24 h commence <b>à partir de la validation</b>, c'est-à-dire au moment où tu passes ta carte — pas au moment où tu l'achètes."},

      {t:'ana', h:"Pendant — une longueur de temps",
       p:"Ce n'est ni une heure ni un jour : c'est combien de temps ça dure.",
       mots:[['Sur la grille','{pendant cent vingt minutes}'],['Aussi','pendant trois jours',true],['La question','combien de temps ?']],
       say:"La correspondance dure pendant cent vingt minutes.",
       note:"Les cent vingt minutes de la correspondance commencent au moment de la validation, et elles ne permettent pas de refaire le même parcours en sens inverse."},

      {t:'labo', h:"Les cinq lignes de la grille",
       p:"Choisis un titre et vois comment sa durée est écrite.",
       axes:[{id:'t', lbl:'Quel titre ?', opts:[
         ['a','Soirée illimitée'],
         ['b','Hebdo'],
         ['c','Week-end illimité'],
         ['d','Mensuel'],
         ['e','Correspondance']]}],
       out:{
         a:{w:['{valide de dix-huit heures à cinq heures}'], say:"Valide de dix-huit heures à cinq heures.", n:'de… à…, avec des heures'},
         b:{w:['{du lundi au dimanche}'], say:"Du lundi au dimanche.", n:'du… au…, avec des jours'},
         c:{w:['{à partir de seize heures}, le vendredi'], say:"À partir de seize heures, le vendredi.", n:'seulement le début'},
         d:{w:["{bon jusqu'à la fin du mois}"], say:"Bon jusqu'à la fin du mois.", n:'seulement la fin'},
         e:{w:['{pendant cent vingt minutes}'], say:"Pendant cent vingt minutes.", n:'une longueur de temps'},
       },
       note:"Cinq titres, cinq façons différentes d'écrire une durée. Ce sont exactement celles de la grille affichée."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes lues telles qu'elles sont écrites.",
       rows:[
         ["Soirée illimitée, valide de 18 h à 5 h.","de… à…"],
         ["Hebdo, du lundi au dimanche.","du… au…"],
         ["Week-end illimité, du vendredi 16 h au lundi 5 h.","du… au…"],
         ["Mensuel, bon jusqu'à la fin du mois.","jusqu'à"],
         ["Titre 24 h, à partir de la validation.","à partir de"],
         ["Correspondance : pendant 120 minutes.","pendant"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « de lundi à dimanche »","oublier que « de » devient « du » devant un jour",
          "Devant un jour de la semaine, c'est toujours <b>du… au…</b> : du lundi au dimanche, du vendredi au lundi."],
         ["croire qu'un titre commence à l'achat","penser que le 24 h commence quand on le paie",
          "Non : il commence <b>à partir de la validation</b>, quand tu passes ta carte pour la première fois. Tu peux l'acheter le matin et le commencer le soir."],
         ["confondre « pendant » et « jusqu'à »","« pendant la fin du mois »",
          "« Pendant » se dit devant une durée qui se compte : pendant 120 minutes, pendant trois jours. « Jusqu'à » se dit devant un moment : jusqu'à la fin du mois."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Devant un jour de la semaine, on écrit…", opts:["de lundi à dimanche","du lundi au dimanche"], ok:1,
          fb:"« de » devient « du », « à » devient « au »."},
         {q:"« Valide de 18 h à 5 h » veut dire…", opts:["du soir au matin suivant","seulement entre 5 h et 18 h"], ok:0,
          fb:"Le titre traverse la nuit."},
         {q:"Le titre 24 h commence…", opts:["au moment de l'achat","à partir de la validation"], ok:1,
          fb:"Quand tu passes ta carte pour la première fois."},
         {q:"« Pendant 120 minutes » dit…", opts:["combien de temps ça dure","à quelle heure ça finit"], ok:0,
          fb:"C'est une longueur de temps."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Cinq mots, cinq durées : <b>de… à…</b> pour des heures, <b>du… au…</b> pour des jours, <b>jusqu'à</b> pour la fin seule, <b>à partir de</b> pour le début seul, <b>pendant</b> pour une longueur de temps."},
    ]
  },

  t3compar: {
    eye:'Mini-leçon', tit:"Comparer deux prix, lire une borne d'âge",
    blocs:[
      {t:'texte', h:"Choisir un titre, c'est comparer",
       p:"Rosario payait environ cent quarante dollars par mois sans le savoir, parce qu'elle n'avait jamais comparé. Comparer deux prix demande deux choses en français : le mot <b>plus</b> ou <b>moins</b>, et surtout le petit mot <b>que</b>, qu'on oublie souvent.",
       note:"Et pour lire les catégories d'âge de la grille, il faut savoir lire « 11 ans et moins », « 65 ans et plus », « de 6 à 17 ans » — trois façons d'écrire une borne."},

      {t:'ana', h:"Comparer deux prix : plus cher, moins cher",
       p:"On met « plus » ou « moins » devant l'adjectif, et « que » devant l'autre chose.",
       mots:[['Moins','{moins cher que} le dix passages'],['Plus','{plus cher que} l’hebdo',true],['Pareil','{aussi cher que} l’hebdo']],
       say:"L'hebdo est moins cher que le dix passages.",
       note:"L'ordre ne change jamais : <b>plus / moins</b> + adjectif + <b>que</b> + la chose comparée."},

      {t:'ana', h:"Le « que » qu'on oublie",
       p:"C'est la faute la plus fréquente à ce niveau, et elle s'entend tout de suite.",
       mots:[['On dit',"{moins cher que l'hebdo}"],['On ne dit pas','« moins cher de l’hebdo »',true],['On ne dit pas','« moins cher comme l’hebdo »']],
       say:"Le mensuel est moins cher que quatre hebdos.",
       note:"Devant une voyelle, « que » devient « qu' » : moins cher <b>qu'</b>un mensuel."},

      {t:'ana', h:"Compter des choses : plus de, moins de",
       p:"Devant un nombre, on n'emploie pas « que » mais <b>de</b>.",
       mots:[['Un âge','{moins de douze ans}'],['Un nombre','{plus de cinq enfants}',true],['La différence','de devant un nombre, que devant une chose']],
       say:"Moins de douze ans. Plus de cinq enfants.",
       note:"« Moins cher <b>que</b> l'hebdo » compare deux titres. « Moins <b>de</b> douze ans » compte des années. Deux petits mots différents."},

      {t:'ana', h:"Les trois façons d'écrire une borne d'âge",
       p:"La grille les emploie toutes les trois, parfois dans le même tableau.",
       mots:[['Une limite en bas','{onze ans et moins} — gratuit'],['Une limite en haut','{soixante-cinq ans et plus} — tarif réduit',true],['Un intervalle','de 6 à 17 ans — tarif réduit']],
       say:"Onze ans et moins. Soixante-cinq ans et plus. De six à dix-sept ans.",
       note:"« 11 ans et moins » comprend les enfants de onze ans. « 65 ans et plus » comprend les personnes de soixante-cinq ans. La borne est toujours incluse."},

      {t:'labo', h:"Comparer les titres de la grille",
       p:"Choisis deux titres et vois lequel coûte le moins cher.",
       axes:[{id:'c', lbl:'Quelle comparaison ?', opts:[
         ['a','hebdo 33,25 $ / dix passages 35 $'],
         ['b','mensuel 110 $ / hebdo 33,25 $'],
         ['c','réduit 66 $ / ordinaire 110 $'],
         ['d','zone A 3,75 $ / zone AB 5,00 $'],
         ['e','les âges de la grille']]}],
       out:{
         a:{w:["l'hebdo est {moins cher que} le dix passages"], say:"L'hebdo est moins cher que le dix passages.", n:'un dollar soixante-quinze de moins'},
         b:{w:['le mensuel est {plus cher que} l’hebdo'], say:"Le mensuel est plus cher que l'hebdo.", n:'mais moins cher que quatre hebdos'},
         c:{w:['le tarif réduit est {moins cher que} l’ordinaire'], say:"Le tarif réduit est moins cher que le tarif ordinaire.", n:'quarante-quatre dollars de moins'},
         d:{w:['aller à Laval coûte {plus cher que} rester à Montréal'], say:"Aller à Laval coûte plus cher que rester à Montréal.", n:'la zone change le prix'},
         e:{w:['{onze ans et moins} · de 6 à 17 ans · {soixante-cinq ans et plus}'], say:"Onze ans et moins. De six à dix-sept ans. Soixante-cinq ans et plus.", n:'les trois bornes de la grille'},
       },
       note:"Compare toujours sur un mois complet : c'est là que la différence se voit."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six comparaisons tirées de la grille.",
       rows:[
         ["L'hebdo est moins cher que le dix passages.","33,25 $ contre 35 $"],
         ["Le mensuel est plus cher que l'hebdo.","110 $ contre 33,25 $"],
         ["Le tarif réduit est moins cher que le tarif ordinaire.","66 $ contre 110 $"],
         ["Les enfants de moins de douze ans voyagent gratuitement.","une borne d'âge"],
         ["Une personne ne peut pas accompagner plus de cinq enfants.","un nombre"],
         ["Soixante-cinq ans et plus, c'est le tarif réduit.","une borne d'âge"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["oublier le « que »","« moins cher de l'hebdo »",
          "C'est <b>que</b> qui introduit la chose comparée, jamais « de » ni « comme ». Moins cher <b>que</b> l'hebdo."],
         ["dire « plus que douze ans »","confondre « plus de » et « plus que » devant un nombre",
          "Devant un nombre, c'est <b>de</b> : plus <b>de</b> douze ans, moins <b>de</b> cinq enfants."],
         ["croire que la borne est exclue","penser que « 65 ans et plus » commence à 66 ans",
          "Non : la borne est incluse. Une personne de soixante-cinq ans exactement a droit au tarif réduit."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On compare deux titres avec…", opts:["moins cher que","moins cher de"], ok:0,
          fb:"« que » introduit la chose comparée."},
         {q:"Devant un nombre, on emploie…", opts:["plus que","plus de"], ok:1,
          fb:"Plus de cinq enfants, moins de douze ans."},
         {q:"« 65 ans et plus » comprend…", opts:["une personne de 65 ans","seulement à partir de 66 ans"], ok:0,
          fb:"La borne est toujours incluse."},
         {q:"L'hebdo à 33,25 $ et le dix passages à 35 $ :", opts:["l'hebdo est moins cher","le dix passages est moins cher"], ok:0,
          fb:"Et en plus, l'hebdo est illimité."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"<b>Plus / moins</b> + adjectif + <b>que</b> pour comparer deux choses. <b>Plus de / moins de</b> devant un nombre. Et dans un tableau, la borne d'un âge est toujours <b>incluse</b>."},
    ]
  },

  t3grille: {
    eye:'Mini-leçon', tit:"Lire la grille des tarifs sans se perdre",
    blocs:[
      {t:'texte', h:"Un tableau se lit en croix",
       p:"La grille affichée dans la station a l'air compliquée, mais elle ne pose que deux questions : <b>quel titre</b> (les lignes) et <b>quelle catégorie de personne</b> (les colonnes). On trouve sa ligne, on descend jusqu'à sa colonne, et le prix est à l'intersection. C'est tout.",
       note:"Avant même de lire, il faut savoir une chose : dans quelle <b>zone</b> tu te déplaces. Montréal est la zone A, et c'est la grille de la zone A qu'on lit ici."},

      {t:'ana', h:"Les quatre zones tarifaires",
       p:"Le territoire est découpé en quatre. Le prix dépend d'où tu pars et d'où tu arrives.",
       mots:[['Zone A','l’agglomération de Montréal'],['Zone B','Laval et l’agglomération de Longueuil',true],['Zones C et D','les couronnes, puis hors territoire']],
       say:"Montréal est la zone A. Laval est la zone B.",
       note:"Un titre « Tous modes A » sert seulement dans Montréal. Pour aller à Laval ou à Longueuil, il faut un titre « Tous modes AB », qui coûte plus cher."},

      {t:'ana', h:"Les quatre colonnes de la grille",
       p:"Quatre catégories de personnes, quatre prix pour le même titre.",
       mots:[['Ordinaire','le prix plein, pour la plupart des adultes'],['Réduit 6-17 ans','les enfants et les adolescents',true],['Réduit étudiant','18 ans et plus, aux études à temps plein'],['Réduit 65 ans et plus','les personnes aînées']],
       say:"Ordinaire. Réduit six à dix-sept ans. Réduit étudiant. Réduit soixante-cinq ans et plus.",
       note:"Pour les trois colonnes « Réduit », il faut une carte OPUS <b>avec photo</b>. Sans la photo, on paie le tarif ordinaire, même si on a le bon âge."},

      {t:'ana', h:"Les six lignes qu'il faut connaître",
       p:"La grille en compte plus, mais six suffisent pour la vie de tous les jours dans la zone A.",
       mots:[['{un passage}','3,75 $ ordinaire · 2,75 $ réduit'],['{dix passages}','35,00 $ ordinaire · 23,50 $ réduit',true],['{un titre hebdomadaire}','33,25 $ ordinaire · 20,00 $ réduit'],['{un titre mensuel}','110,00 $ ordinaire · 66,00 $ réduit']],
       say:"Un passage. Dix passages. Un titre hebdomadaire. Un titre mensuel.",
       note:"Et deux titres courts : le 24 h à 11,25 $ et le Week-end illimité à 17,00 $. Ils n'ont pas de tarif réduit."},

      {t:'ana', h:"La correspondance, comprise dans le prix",
       p:"Elle ne se paie pas et ne s'achète pas : elle vient avec le titre.",
       mots:[['La durée','cent vingt minutes après la validation'],['Ce qu’elle permet','changer d’autobus, prendre le métro, puis le train',true],['Ce qu’elle interdit','refaire le même parcours en sens inverse']],
       say:"La correspondance dure cent vingt minutes.",
       note:"Elle s'enregistre toute seule sur la carte : il n'y a rien à demander, rien à garder dans sa poche."},

      {t:'labo', h:"Trouver son prix dans la grille",
       p:"Choisis une personne et vois quelle case la concerne.",
       axes:[{id:'p', lbl:'Qui achète ?', opts:[
         ['a','Rosario, 41 ans, tous les jours'],
         ['b','sa fille, 15 ans'],
         ['c','sa mère, 68 ans'],
         ['d','son garçon, 9 ans'],
         ['e','sa sœur, en visite trois jours']]}],
       out:{
         a:{w:['Mensuel · Ordinaire · {c{ent} dix dollars}'], say:"Mensuel, ordinaire : cent dix dollars.", n:'ligne mensuel, colonne ordinaire'},
         b:{w:['Mensuel · Réduit 6-17 ans · soixante-six dollars'], say:"Mensuel, réduit six à dix-sept ans : soixante-six dollars.", n:'carte avec photo obligatoire'},
         c:{w:['Mensuel · Réduit 65 ans et plus · soixante-six dollars'], say:"Mensuel, réduit soixante-cinq ans et plus : soixante-six dollars.", n:'carte avec photo obligatoire'},
         d:{w:['Gratuit, s’il est accompagné'], say:"Onze ans et moins, c'est gratuit s'il est accompagné.", n:'l’adulte doit avoir un titre validé'},
         e:{w:['Week-end illimité · dix-sept dollars'], say:"Week-end illimité : dix-sept dollars.", n:'sur une carte à puce occasionnelle'},
       },
       note:"Une ligne, une colonne, un prix. C'est la seule chose à faire devant la grille."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six lignes de la grille de la zone A.",
       rows:[
         ["Un passage : trois dollars soixante-quinze.","tarif ordinaire"],
         ["Un passage à tarif réduit : deux dollars soixante-quinze.","carte avec photo"],
         ["Dix passages : trente-cinq dollars.","tarif ordinaire"],
         ["Hebdo : trente-trois dollars vingt-cinq.","du lundi au dimanche"],
         ["Mensuel : cent dix dollars.","jusqu'à la fin du mois"],
         ["Mensuel à tarif réduit : soixante-six dollars.","carte avec photo"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire la grille d'une autre zone","prendre le prix « Tous modes AB » en croyant lire « Tous modes A »",
          "La grille affiche plusieurs blocs, un par zone. Vérifie le titre du bloc avant de lire un prix : le premier est celui de Montréal seul."],
         ["croire que le bon âge suffit","se présenter sans carte avec photo",
          "Le tarif réduit demande <b>deux</b> choses : le bon âge et une carte OPUS avec photo. Sans la photo, on paie le plein prix."],
         ["acheter un mensuel le 28 du mois","penser qu'un mensuel dure trente jours",
          "Non : il finit le dernier jour du mois, pas trente jours après l'achat. Acheté le 28, il ne sert que trois ou quatre jours."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Montréal est la zone…", opts:["A","B"], ok:0,
          fb:"Laval et Longueuil sont la zone B."},
         {q:"Pour avoir le tarif réduit, il faut…", opts:["le bon âge seulement","le bon âge et une carte avec photo"], ok:1,
          fb:"Les deux, toujours."},
         {q:"Un titre mensuel finit…", opts:["trente jours après l'achat","le dernier jour du mois"], ok:1,
          fb:"D'où l'intérêt de l'acheter en début de mois."},
         {q:"La correspondance…", opts:["s'achète en plus","est comprise dans le titre"], ok:1,
          fb:"Cent vingt minutes, enregistrées toutes seules."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Une <b>ligne</b> pour le titre, une <b>colonne</b> pour la catégorie, et le prix à l'intersection. Vérifie d'abord ta <b>zone</b>, et rappelle-toi que tout tarif réduit exige une <b>carte avec photo</b>."},
    ]
  },

  t3places: {
    eye:'Mini-leçon', tit:"Les places réservées et le transport adapté",
    blocs:[
      {t:'texte', h:"Deux choses différentes, souvent confondues",
       p:"Le programme nomme le <b>transport adapté</b> et les <b>places réservées</b> dans la même ligne de son lexique, et beaucoup de gens les mélangent. Ce sont pourtant deux choses très différentes : les places réservées sont des sièges dans l'autobus ordinaire ; le transport adapté est un <b>service à part</b>, avec ses propres véhicules et une inscription à faire d'avance.",
       note:"Savoir les distinguer sert à deux choses : céder sa place au bon moment, et orienter une personne qui ne peut pas prendre l'autobus ordinaire."},

      {t:'ana', h:"Où sont les places réservées",
       p:"Toujours au même endroit, dans tous les autobus : les premières rangées, juste après le chauffeur.",
       mots:[['L’endroit','les premières rangées, en avant'],['Le repère','un petit dessin au-dessus du siège',true],['Le nom','{une place réservée}']],
       say:"Les places réservées sont en avant de l'autobus.",
       note:"On peut s'y asseoir quand elles sont libres. Ce n'est pas interdit : c'est une place qu'on prête."},

      {t:'ana', h:"Pour qui elles sont gardées",
       p:"Trois groupes de personnes, nommés tels quels dans le programme.",
       mots:[['Les personnes','{une personne à mobilité réduite}'],['Les femmes','{une femme enceinte}',true],['Les aînés','les personnes âgées']],
       say:"Pour les personnes à mobilité réduite, les femmes enceintes et les personnes âgées.",
       note:"« À mobilité réduite » veut dire : qui se déplace difficilement. Une canne, un fauteuil, une jambe plâtrée, un grand âge."},

      {t:'ana', h:"Ce qu'on fait quand quelqu'un monte",
       p:"On se lève <b>sans attendre qu'on le demande</b>. C'est ce qui se fait ici, et c'est apprécié.",
       mots:[['Le geste','{laisser sa place} tout de suite'],['La phrase','« Prenez ma place, madame. »',true],['La réponse','« Merci, c’est gentil. »']],
       say:"Prenez ma place, madame. Merci, c'est gentil.",
       note:"Deux phrases courtes suffisent. On ne discute pas, on ne demande pas l'âge de la personne : on se lève."},

      {t:'ana', h:"Le transport adapté, un service à part",
       p:"Pour les personnes qui ne peuvent pas prendre l'autobus ordinaire, même avec une place réservée.",
       mots:[['Ce que c’est','{le transport adapté}'],['Comment ça marche','on réserve son déplacement d’avance',true],['Avant tout','il faut s’inscrire au service']],
       say:"Ma voisine se déplace avec le transport adapté.",
       note:"L'inscription se fait une fois, sur demande, avec un document médical. Ensuite, chaque déplacement se réserve à l'avance par téléphone ou en ligne."},

      {t:'ana', h:"Trois verbes du programme",
       p:"Le programme rattache ces trois verbes à la situation « Déplacement dans une ville ».",
       mots:[['Aller d’un endroit à un autre','{se déplacer}'],['Savoir où on est','{se repérer}',true],['Aller chercher l’information','{se renseigner}']],
       say:"Se déplacer. Se repérer. Se renseigner.",
       note:"Et son contraire, celui qu'on veut éviter : <b>se perdre</b>. « Je me suis perdue » se dit très souvent quand on arrive dans une ville nouvelle."},

      {t:'labo', h:"Qui a droit à quoi",
       p:"Choisis une personne et vois ce qui la concerne.",
       axes:[{id:'q', lbl:'Quelle personne ?', opts:[
         ['a','une femme enceinte'],
         ['b','un homme de 80 ans avec une canne'],
         ['c','une personne en fauteuil roulant'],
         ['d','un étudiant de 20 ans'],
         ['e','les trois groupes ensemble']]}],
       out:{
         a:{w:['{une femme enceinte} — place réservée'], say:"Une femme enceinte a droit à une place réservée.", n:'en avant de l’autobus'},
         b:{w:['personne âgée — place réservée'], say:"Une personne âgée a droit à une place réservée.", n:'et au tarif réduit, à partir de 65 ans'},
         c:{w:['{une personne à mobilité réduite} — place réservée, parfois {le transport adapté}'], say:"Une personne à mobilité réduite a droit à une place réservée, et parfois au transport adapté.", n:'selon ce qu’elle peut faire'},
         d:{w:['aucune place réservée — tarif réduit étudiant'], say:"Un étudiant n'a pas de place réservée, mais il a le tarif réduit.", n:'deux choses différentes'},
         e:{w:['personnes à mobilité réduite · femmes enceintes · personnes âgées'], say:"Les personnes à mobilité réduite, les femmes enceintes et les personnes âgées.", n:'les trois groupes du programme'},
       },
       note:"Le tarif réduit et la place réservée sont deux choses séparées : un étudiant paie moins cher mais n'a pas de place gardée."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases utiles dans l'autobus.",
       rows:[
         ["Les places réservées sont en avant.","où elles sont"],
         ["Prenez ma place, madame.","céder sa place"],
         ["Merci, c'est gentil.","la réponse"],
         ["Ma voisine se déplace avec le transport adapté.","le service à part"],
         ["Il faut s'inscrire avant d'utiliser le service.","l'inscription"],
         ["Excusez-moi, je me suis perdue.","quand on ne se repère plus"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["confondre les deux","croire que « transport adapté » veut dire « places réservées »",
          "Les places réservées sont des sièges dans l'autobus ordinaire. Le transport adapté est un autre service, avec d'autres véhicules et une inscription à faire."],
         ["attendre qu'on demande","rester assis tant que personne ne dit rien",
          "Ici, on se lève de soi-même dès qu'une personne concernée monte. Attendre qu'elle demande la met mal à l'aise."],
         ["croire que le tarif réduit donne une place","penser qu'un étudiant a droit aux sièges d'en avant",
          "Non. Le tarif réduit concerne le <b>prix</b>. La place réservée concerne le <b>siège</b>. Un étudiant a l'un sans avoir l'autre."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Les places réservées sont…", opts:["en avant de l'autobus","au fond, près des portes arrière"], ok:0,
          fb:"Les premières rangées, après le chauffeur."},
         {q:"Quand une personne âgée monte…", opts:["on attend qu'elle demande","on se lève tout de suite"], ok:1,
          fb:"C'est ce qui se fait ici."},
         {q:"Le transport adapté…", opts:["est le même service que l'autobus","est un service à part, avec inscription"], ok:1,
          fb:"D'autres véhicules, une réservation d'avance."},
         {q:"Un étudiant de 20 ans a droit…", opts:["au tarif réduit","à une place réservée"], ok:0,
          fb:"Le prix, oui ; le siège, non."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Les <b>places réservées</b> sont en avant de l'autobus, pour les personnes à mobilité réduite, les femmes enceintes et les personnes âgées — et on se lève sans attendre. Le <b>transport adapté</b> est un autre service, avec une inscription et une réservation."},
    ]
  },
};
