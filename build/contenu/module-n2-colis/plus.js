const PLUS = {
  prSon: {
    eye:'Mini-leçon', tit:"« Timbre » et « enveloppe » : deux sons du nez",
    blocs:[
      {t:'texte', h:"Deux sons, et deux mots de la poste",
       p:"Les deux premiers mots du module portent chacun un son du nez. Dans <b>timbre</b>, on entend le son de <b>cinq</b> et de <b>demain</b>. Dans <b>enveloppe</b>, on entend le son de <b>cent</b> et de <b>dedans</b>. Les deux passent par le nez, mais la bouche n'est pas dans la même position, et le mot change.",
       note:"Commencer par faire écouter la paire « cinq / cent » en série, sans explication. Au comptoir, ces deux nombres se disent tous les jours."},

      {t:'ana', h:"Le son de « timbre » : la bouche étirée",
       p:"C'est le son de cinq, de demain et du chemin.",
       mots:[["On dit","un t{im}bre — les lèvres s'étirent"],["Aussi","c{in}q · v{ingt} · un chem{in}"],["Aussi","dem{ain} · pl{ein} · la m{ain}"],["On ne dit pas","« un tambre » ni « cent » pour « cinq »",true]],
       say:"Un timbre. Cinq. Un chemin. Demain.",
       note:"Faire sourire les élèves pendant qu'ils disent le son : la bouche prend d'elle-même la bonne forme."},

      {t:'ana', h:"Le son de « enveloppe » : la bouche grande ouverte",
       p:"C'est le son de cent, de trente et de dedans.",
       mots:[["On dit","une {en}veloppe — la bouche s'ouvre grand"],["Aussi","c{ent} · tr{ente} · quar{ante}"],["Aussi","ded{ans} · dev{ant} · comm{ent}"],["On ne dit pas","« une inveloppe »",true]],
       say:"Une enveloppe. Cent. Trente. Dedans.",
       note:"Faire poser la main sous le menton : la mâchoire descend. C'est le repère le plus sûr pour ce son."},

      {t:'ana', h:"Les deux façons d'écrire chaque son",
       p:"Un seul son, quatre écritures. Devant b et p, on écrit m.",
       mots:[["Son de timbre","{in} · {im} · {ain} · {ein}"],["Exemples","un chem{in} · un t{im}bre · dem{ain} · pl{ein}"],["Son d'enveloppe","{an} · {am} · {en} · {em}"],["Exemples","ded{ans} · une l{am}pe · une {en}veloppe · nov{em}bre"],["La règle du m","devant b et p, jamais n : t{im}bre, l{am}pe",true]],
       say:"Un chemin. Un timbre. Dedans. Une enveloppe.",
       note:"La règle « m devant b et p » explique timbre, lampe, novembre. Une seule règle, et l'orthographe de quatre mots du module devient sûre."},

      {t:'labo', h:"Écoute les deux sons",
       p:"Choisis un son et une façon de l'entendre.",
       axes:[
         {id:'p', lbl:'Quel son ?', opts:[
           ['a','le son de « timbre »'],
           ['b','le son de « enveloppe »'],
           ['c','les deux, à la suite']]},
         {id:'q', lbl:'Dans quoi ?', opts:[['1','un mot seul'],['2','un nombre'],['3','une phrase du comptoir']]}],
       out:{
         a1:{w:["un timbre"], say:"Un timbre.", n:'les lèvres s\'étirent'},
         a2:{w:["cinq, vingt"], say:"Cinq. Vingt.", n:'deux nombres qu\'on entend au comptoir'},
         a3:{w:["Un timbre, s'il vous plaît."], say:"Un timbre, s'il vous plaît.", n:'la phrase la plus utile du module'},
         b1:{w:["une enveloppe"], say:"Une enveloppe.", n:'la bouche s\'ouvre grand'},
         b2:{w:["cent, trente"], say:"Cent. Trente.", n:'deux nombres, même son'},
         b3:{w:["Qu'est-ce qu'il y a dedans ?"], say:"Qu'est-ce qu'il y a dedans ?", n:'la question du préposé pour un colis'},
         c1:{w:["timbre, enveloppe"], say:"Timbre. Enveloppe.", n:'la paire à entendre en premier'},
         c2:{w:["cinq, cent"], say:"Cinq. Cent.", n:'la paire la plus difficile : un prix se joue là'},
         c3:{w:["Cinq timbres dans une enveloppe."], say:"Cinq timbres dans une enveloppe.", n:'les deux sons dans la même phrase'},
       },
       note:"Neuf extraits. Les faire écouter les yeux fermés, puis lever une main pour « in », deux pour « an »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six mots de la poste, trois par son.",
       rows:[
         ["un timbre","son de « in »"],
         ["cinq","son de « in »"],
         ["demain","son de « in »"],
         ["une enveloppe","son de « an »"],
         ["cent","son de « an »"],
         ["dedans","son de « an »"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « cent » pour « cinq »","la bouche est ouverte au lieu d'être étirée",
          "C'est le piège qui coûte de l'argent : cinq dollars et cent dollars ne sont pas la même chose. Étire les lèvres, comme pour sourire, et le son sort juste."],
         ["prononcer le n ou le m à la fin","le son passe par le nez, pas par la langue",
          "Dans « timbre », on n'entend pas de « m » séparé. La langue ne touche rien. Si tu entends « tim-beu-reu », c'est trop."],
         ["écrire « tinbre » au lieu de « timbre »","devant b et p, on écrit m",
          "C'est la même règle que pour lampe et novembre. Elle vaut pour les deux sons du nez, pas seulement pour un."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Cinq » a le son de…", opts:["timbre","enveloppe"], ok:0,
          fb:"Le son de « timbre » : les lèvres s'étirent."},
         {q:"« Trente » a le son de…", opts:["enveloppe","timbre"], ok:0,
          fb:"Le son de « enveloppe » : la bouche s'ouvre grand."},
         {q:"On écrit « ti___bre » avec…", opts:["m","n"], ok:0,
          fb:"Devant b et p, on écrit toujours m."},
         {q:"Dans « dedans », on entend le « s » de la fin ?", opts:["non","oui"], ok:0,
          fb:"Non. On dit « de-dan », et le mot s'arrête là."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Deux sons, deux positions de bouche. <b>Timbre, cinq, demain</b> : les lèvres s'étirent. <b>Enveloppe, cent, trente</b> : la bouche s'ouvre. Et devant b et p, on écrit toujours m."},
    ]
  },

  prCombien: {
    eye:'Mini-leçon', tit:"Demander le prix, et vérifier ce qu'on a entendu",
    blocs:[
      {t:'texte', h:"Une question, et elle sert partout",
       p:"Le programme donne cette question telle quelle : <b>Combien ça coûte ?</b> Elle sert au comptoir postal, à l'épicerie, à la pharmacie et au dépanneur. Trois mots, et on obtient un prix. Ce qui est difficile n'est pas de poser la question : c'est de comprendre la réponse, parce qu'un prix se dit vite.",
       note:"Faire dire la question par chacun, debout, avant toute explication. Elle doit sortir sans réfléchir."},

      {t:'ana', h:"Dire ce qu'on veut, en trois mots",
       p:"On n'a pas besoin d'une phrase longue.",
       mots:[["On dit","Un {timbre}, s'il vous plaît."],["Aussi","Je {veux} envoyer cette lettre."],["Aussi","C'est pour {Sherbrooke}."],["On ne dit pas","« Je voudrais savoir si je peux acheter… »",true]],
       say:"Un timbre, s'il vous plaît. Je veux envoyer cette lettre. C'est pour Sherbrooke.",
       note:"Insister : au comptoir, une phrase courte est polie. Le « s'il vous plaît » suffit à la politesse."},

      {t:'ana', h:"Demander le prix",
       p:"Deux façons, et la première est celle du programme.",
       mots:[["On dit","{Combien} ça coûte ?"],["Aussi","Ça coûte {combien} ?"],["Aussi","C'est {combien} ?"],["On ne dit pas","« Quel est le coût ? » — personne ne parle comme ça au comptoir",true]],
       say:"Combien ça coûte ? Ça coûte combien ? C'est combien ?",
       note:"Les trois se disent. Faire choisir la sienne à chaque élève et la garder : une seule bien tenue vaut mieux que trois hésitantes."},

      {t:'ana', h:"Lire un prix en dollars",
       p:"Le nombre avant la virgule, puis celui d'après.",
       mots:[["On dit","1,44 $ → un {dollar} quarante-quatre"],["Aussi","1,24 $ → un dollar {vingt-quatre}"],["Aussi","18,50 $ → dix-huit dollars {cinquante}"],["Aussi","20 $ → {vingt} dollars"],["On ne dit pas","« un point quarante-quatre »",true]],
       say:"Un dollar quarante-quatre. Un dollar vingt-quatre. Dix-huit dollars cinquante. Vingt dollars.",
       note:"Au Québec, on dit « et quarante-quatre » ou seulement « quarante-quatre ». Les deux s'entendent au comptoir ; les faire reconnaître toutes les deux."},

      {t:'labo', h:"Au comptoir : demande et vérifie",
       p:"Choisis ce que tu achètes et ce que tu dis.",
       axes:[
         {id:'p', lbl:'Tu achètes quoi ?', opts:[
           ['a','un timbre'],
           ['b','un colis pour Sherbrooke'],
           ['c','un carnet de timbres']]},
         {id:'q', lbl:'Tu dis quoi ?', opts:[['1','je demande'],['2','je demande le prix'],['3','je vérifie le montant']]}],
       out:{
         a1:{w:["Un timbre, s'il vous plaît."], say:"Un timbre, s'il vous plaît.", n:'la phrase de base'},
         a2:{w:["Combien ça coûte ?"], say:"Combien ça coûte ?", n:'la question du programme'},
         a3:{w:["Un dollar quarante-quatre ?"], say:"Un dollar quarante-quatre ?", n:'on redit le montant, la voix monte'},
         b1:{w:["Je veux envoyer ce colis."], say:"Je veux envoyer ce colis.", n:'on pose la boîte sur le comptoir en le disant'},
         b2:{w:["Ça coûte combien ?"], say:"Ça coûte combien ?", n:'pour un colis, le prix dépend du poids'},
         b3:{w:["Dix-huit dollars cinquante ?"], say:"Dix-huit dollars cinquante ?", n:'on vérifie avant de sortir sa carte'},
         c1:{w:["Un carnet de timbres, s'il vous plaît."], say:"Un carnet de timbres, s'il vous plaît.", n:'le carnet coûte moins cher par timbre'},
         c2:{w:["C'est combien, le carnet ?"], say:"C'est combien, le carnet ?", n:'la forme la plus courte des trois'},
         c3:{w:["Pouvez-vous répéter, s'il vous plaît ?"], say:"Pouvez-vous répéter, s'il vous plaît ?", n:'quand le montant est passé trop vite'},
       },
       note:"Neuf extraits. Faire jouer la scène debout, deux par deux, avec une vraie boîte et une vraie enveloppe."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six phrases du comptoir.",
       rows:[
         ["Un timbre, s'il vous plaît.","je demande"],
         ["Je veux envoyer cette lettre.","je dis ce que je veux"],
         ["Combien ça coûte ?","je demande le prix"],
         ["Un dollar quarante-quatre ?","je vérifie"],
         ["Pouvez-vous répéter, s'il vous plaît ?","je fais répéter"],
         ["Merci beaucoup. Bonne journée.","je pars"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["partir sans avoir compris le montant","on paie sans savoir combien",
          "Redire le nombre entendu est la stratégie la plus utile du module. « Un dollar quarante-quatre ? » — et le préposé confirme ou corrige."],
         ["dire « Combien coûte ? » sans le « ça »","il manque un mot",
          "La question complète est « Combien ça coûte ? ». Le « ça » remplace l'objet posé sur le comptoir."],
         ["confondre cinq et cent dans un prix","les deux sons du nez",
          "« Cinq dollars » et « cent dollars » se ressemblent pour une oreille neuve. En cas de doute, on redit le nombre : c'est fait pour ça."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"La question du programme, c'est…", opts:["Combien ça coûte ?","Quel est le coût ?"], ok:0,
          fb:"Trois mots, et ils servent dans tous les commerces."},
         {q:"1,44 $ se dit…", opts:["un dollar quarante-quatre","un point quarante-quatre"], ok:0,
          fb:"On ne dit jamais « point » pour un prix."},
         {q:"Après avoir entendu le prix, on…", opts:["redit le nombre","paie tout de suite"], ok:0,
          fb:"On redit le nombre pour vérifier. La voix monte à la fin."},
         {q:"« Un timbre, s'il vous plaît » est…", opts:["poli","impoli"], ok:0,
          fb:"Court et poli. Le « s'il vous plaît » suffit."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Je dis ce que je veux en trois mots. Je demande : <b>Combien ça coûte ?</b> Je redis le montant pour vérifier. Et si c'est trop vite : <b>Pouvez-vous répéter, s'il vous plaît ?</b>"},
    ]
  },

  t1adresse: {
    eye:'Mini-leçon', tit:"Les lignes d'une adresse du Québec",
    blocs:[
      {t:'texte', h:"Un ordre qui ne change jamais",
       p:"Une adresse du Québec s'écrit toujours dans le même ordre : d'abord la personne, puis l'endroit, du plus petit au plus grand. Le nom, le numéro et la rue, la ville et la province, le code postal. Si l'ordre change, la lettre voyage plus longtemps — et parfois elle revient.",
       note:"C'est l'une des deux intentions du programme pour cette situation : « adresser une enveloppe ». Faire écrire une vraie enveloppe en classe, pas un exercice sur une feuille."},

      {t:'ana', h:"Ligne par ligne, de haut en bas",
       p:"Quatre lignes suffisent presque toujours.",
       mots:[["Ligne 1","{Ousmane Diallo}"],["Ligne 2","145, {rue} King Ouest, app. 6"],["Ligne 3","Sherbrooke {(Québec)}"],["Ligne 4","{J1H 1P4}"],["On ne dit pas","le code postal avant la ville",true]],
       say:"Ousmane Diallo. 145, rue King Ouest, appartement 6. Sherbrooke, Québec. J1H 1P4.",
       note:"Écrire les quatre lignes au tableau et les effacer une à une : le groupe doit pouvoir les redire dans l'ordre."},

      {t:'ana', h:"Le numéro, la rue, l'appartement",
       p:"Le numéro d'abord, l'appartement à la fin.",
       mots:[["On dit","4520, {rue} Bélanger, app. 3"],["Aussi","1250, {boul.} Saint-Laurent"],["Aussi","78, {av.} du Parc, app. 12"],["Une virgule","après le numéro, et avant l'appartement"],["On ne dit pas","« app. 3, 4520 rue Bélanger »",true]],
       say:"4520, rue Bélanger, appartement 3. 1250, boulevard Saint-Laurent.",
       note:"Le numéro civique vient toujours en premier au Québec. Beaucoup d'élèves viennent de pays où c'est l'inverse : le dire explicitement."},

      {t:'ana', h:"L'expéditeur et le destinataire",
       p:"Deux personnes, deux places sur l'enveloppe.",
       mots:[["En haut, à gauche","l'{expéditeur} — celui qui envoie, en petit"],["Au milieu","le {destinataire} — celui qui reçoit, en plus gros"],["En haut, à droite","le {timbre}"],["Pourquoi les deux ?","si la personne a déménagé, la lettre revient chez toi"],["On ne dit pas","« l'envoyeur » ni « le receveur »",true]],
       say:"L'expéditeur en haut, à gauche. Le destinataire au milieu. Le timbre en haut, à droite.",
       note:"Dessiner un grand rectangle au tableau et faire venir trois élèves y placer les trois éléments. Ça se retient par le geste."},

      {t:'labo', h:"Où va chaque chose ?",
       p:"Choisis une partie de l'enveloppe et ce que tu veux savoir.",
       axes:[
         {id:'p', lbl:'Quelle partie ?', opts:[
           ['a','le nom'],
           ['b','le numéro et la rue'],
           ['c','la ville et le code postal']]},
         {id:'q', lbl:'Tu veux quoi ?', opts:[['1','un exemple'],['2','la place sur l\'enveloppe'],['3','une question à poser']]}],
       out:{
         a1:{w:["Ousmane Diallo"], say:"Ousmane Diallo.", n:'le prénom, puis le nom de famille'},
         a2:{w:["Au milieu de l'enveloppe."], say:"Au milieu de l'enveloppe.", n:'c\'est la ligne la plus grosse'},
         a3:{w:["Comment ça s'écrit, votre nom ?"], say:"Comment ça s'écrit, votre nom ?", n:'à poser avant d\'écrire, jamais après'},
         b1:{w:["145, rue King Ouest, app. 6"], say:"145, rue King Ouest, appartement 6.", n:'numéro, rue, appartement'},
         b2:{w:["Sous le nom, sur la deuxième ligne."], say:"Sous le nom, sur la deuxième ligne.", n:'toujours juste en dessous'},
         b3:{w:["Vous habitez à quel numéro ?"], say:"Vous habitez à quel numéro ?", n:'le numéro civique, pas l\'appartement'},
         c1:{w:["Sherbrooke (Québec) J1H 1P4"], say:"Sherbrooke, Québec. J1H 1P4.", n:'la province entre parenthèses'},
         c2:{w:["Sur la dernière ligne, tout en bas."], say:"Sur la dernière ligne, tout en bas.", n:'la ville et le code ensemble'},
         c3:{w:["Quel est votre code postal ?"], say:"Quel est votre code postal ?", n:'on le fait toujours répéter'},
       },
       note:"Neuf extraits. Terminer en faisant écrire une vraie enveloppe, avec l'adresse du centre de formation."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Une adresse complète, une ligne à la fois.",
       rows:[
         ["Ousmane Diallo","ligne 1 — le nom"],
         ["145, rue King Ouest, app. 6","ligne 2 — le numéro et la rue"],
         ["Sherbrooke (Québec)","ligne 3 — la ville et la province"],
         ["J1H 1P4","ligne 4 — le code postal"],
         ["Amara Diallo, 4520, rue Bélanger, app. 3","l'expéditeur, en haut à gauche"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire l'appartement avant le numéro","l'ordre est inversé",
          "Au Québec, le numéro civique vient toujours en premier : 4520, rue Bélanger, app. 3. Beaucoup de pays font l'inverse — c'est l'erreur la plus fréquente en classe."],
         ["oublier son propre nom sur l'enveloppe","il n'y a pas d'expéditeur",
          "Sans expéditeur, une lettre qui n'arrive pas ne revient pas : elle disparaît. En haut, à gauche, en petit."],
         ["écrire la province en toutes lettres sans parenthèses","« Sherbrooke Québec »",
          "On écrit Sherbrooke (Québec). Les parenthèses sont la forme du Québec ; l'abréviation QC existe aussi, sur une ligne à part."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sur la première ligne, on écrit…", opts:["le nom","la rue"], ok:0,
          fb:"Le nom de la personne, prénom d'abord."},
         {q:"« app. 6 » s'écrit…", opts:["après la rue","avant le numéro"], ok:0,
          fb:"Numéro, rue, puis appartement."},
         {q:"L'expéditeur va…", opts:["en haut, à gauche","au milieu"], ok:0,
          fb:"En petit, en haut à gauche. Le milieu est pour le destinataire."},
         {q:"Le code postal va…", opts:["à la fin","avant la ville"], ok:0,
          fb:"Toujours à la fin, avec la ville ou juste en dessous."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Le nom, le numéro et la rue, la ville et la province, le code postal. Toujours dans cet ordre. Le destinataire au milieu, l'expéditeur en haut à gauche, le timbre en haut à droite."},
    ]
  },

  t1code: {
    eye:'Mini-leçon', tit:"Le code postal, six caractères",
    blocs:[
      {t:'texte', h:"Six caractères, et la lettre trouve sa rue",
       p:"Un code postal du Canada a toujours six caractères : trois, un espace, trois. Une lettre, un chiffre, une lettre — espace — un chiffre, une lettre, un chiffre. Il ne se devine pas et il ne s'invente pas : on le demande, et on le fait répéter.",
       note:"Faire chercher le code postal du centre de formation sur le téléphone, en classe. Chaque élève repart avec le sien écrit dans son carnet."},

      {t:'ana', h:"La forme, toujours la même",
       p:"Lettre, chiffre, lettre — espace — chiffre, lettre, chiffre.",
       mots:[["Montréal","{H1T 1C5}"],["Sherbrooke","{J1H 1P4}"],["La forme","{A1A 1A1}"],["L'espace","au milieu, après trois caractères"],["On ne dit pas","« H mille cent »",true]],
       say:"H, un, T, un, C, cinq. J, un, H, un, P, quatre.",
       note:"Les faire dire caractère par caractère, lentement. C'est un exercice d'alphabet autant qu'un exercice d'adresse."},

      {t:'ana', h:"La première lettre dit la région",
       p:"Elle se reconnaît de loin.",
       mots:[["H","{Montréal}"],["J","la Montérégie et l'{Estrie}"],["G","la ville de {Québec}"],["K","l'{Outaouais} et l'est de l'Ontario"],["On ne dit pas","que la lettre donne la rue : elle donne la région",true]],
       say:"H, Montréal. J, l'Estrie. G, Québec.",
       note:"Utile en classe : demander à chacun la première lettre de son code postal. Le groupe se répartit sur une carte en deux minutes."},

      {t:'ana', h:"Le demander et le faire répéter",
       p:"Trois phrases suffisent.",
       mots:[["On demande","Quel est votre {code postal} ?"],["On fait répéter","Pouvez-vous {répéter}, s'il vous plaît ?"],["On vérifie","H, un, T… un, C, {cinq} ?"],["On épelle","H comme Henri, T comme Thomas"],["On ne dit pas","« redis-le » à un préposé",true]],
       say:"Quel est votre code postal ? Pouvez-vous répéter, s'il vous plaît ? H, un, T, un, C, cinq ?",
       note:"L'épellation avec un prénom est la stratégie des préposés eux-mêmes. La donner comme un outil, pas comme une curiosité."},

      {t:'labo', h:"Un code postal, trois façons de s'en servir",
       p:"Choisis une ville et ce que tu veux faire.",
       axes:[
         {id:'p', lbl:'Quelle ville ?', opts:[
           ['a','Montréal'],
           ['b','Sherbrooke'],
           ['c','Québec']]},
         {id:'q', lbl:'Tu fais quoi ?', opts:[['1','je lis le code'],['2','je le demande'],['3','je le vérifie']]}],
       out:{
         a1:{w:["H1T 1C5"], say:"H, un, T, un, C, cinq.", n:'un code de Montréal commence par H'},
         a2:{w:["Quel est votre code postal ?"], say:"Quel est votre code postal ?", n:'la question, telle quelle'},
         a3:{w:["H1T 1C5 ? Merci."], say:"H, un, T, un, C, cinq ? Merci.", n:'on redit, puis on remercie'},
         b1:{w:["J1H 1P4"], say:"J, un, H, un, P, quatre.", n:'un code de l\'Estrie commence par J'},
         b2:{w:["C'est quoi, le code postal ?"], say:"C'est quoi, le code postal ?", n:'la forme courte, entre amis'},
         b3:{w:["J comme Jacques ?"], say:"J comme Jacques ?", n:'on épelle avec un prénom quand la lettre est floue'},
         c1:{w:["G1R 5A5"], say:"G, un, R, cinq, A, cinq.", n:'un code de la ville de Québec commence par G'},
         c2:{w:["Pouvez-vous écrire le code, s'il vous plaît ?"], say:"Pouvez-vous écrire le code, s'il vous plaît ?", n:'écrire vaut mieux que redire, au téléphone'},
         c3:{w:["Six caractères, c'est bien ça ?"], say:"Six caractères, c'est bien ça ?", n:'le compte est la vérification la plus rapide'},
       },
       note:"Neuf extraits. Terminer en faisant dicter à voix haute le code postal de chacun à son voisin, qui l'écrit."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Trois codes et trois phrases.",
       rows:[
         ["H1T 1C5","Montréal"],
         ["J1H 1P4","Sherbrooke"],
         ["G1R 5A5","Québec"],
         ["Quel est votre code postal ?","je demande"],
         ["Pouvez-vous répéter, s'il vous plaît ?","je fais répéter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["lire le code comme un nombre","« H mille cent »",
          "On dit chaque caractère un par un : H, un, T, un, C, cinq. Jamais de nombre entier."],
         ["oublier l'espace du milieu","H1T1C5",
          "L'espace se met après trois caractères. Sur un formulaire, il y a souvent une case vide à cet endroit : c'est elle."],
         ["confondre le zéro et la lettre O","0 ou O ?",
          "Ils existent tous les deux dans les codes postaux. En cas de doute, on demande : « zéro ou la lettre O ? » Le préposé répond sans se fâcher."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un code postal a…", opts:["six caractères","cinq chiffres"], ok:0,
          fb:"Six : trois, un espace, trois."},
         {q:"Le premier caractère est…", opts:["une lettre","un chiffre"], ok:0,
          fb:"Une lettre, et elle dit la région."},
         {q:"H1T 1C5 se lit…", opts:["H, un, T, un, C, cinq","H cent un T"], ok:0,
          fb:"Un caractère à la fois."},
         {q:"Un code de Montréal commence par…", opts:["H","G"], ok:0,
          fb:"H pour Montréal, G pour la ville de Québec."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Six caractères : lettre, chiffre, lettre — espace — chiffre, lettre, chiffre. On les dit un par un. On le demande, et on le fait répéter."},
    ]
  },

  t2form: {
    eye:'Mini-leçon', tit:"Les mots d'un formulaire",
    blocs:[
      {t:'texte', h:"Les mêmes mots partout",
       p:"Un formulaire de la poste, une fiche d'inscription, un formulaire de la clinique : ce sont toujours les mêmes mots dans les mêmes cases. <b>Nom</b>, <b>prénom</b>, <b>adresse</b>, <b>ville</b>, <b>code postal</b>, <b>téléphone</b>, <b>signature</b>, <b>date</b>. Les reconnaître une fois, c'est les reconnaître partout.",
       note:"C'est l'intention principale du programme pour cette situation : « lire et remplir un formulaire ». Apporter trois formulaires réels et les faire comparer — les mots sont les mêmes."},

      {t:'ana', h:"Qui es-tu ?",
       p:"Les quatre premières cases parlent de la personne.",
       mots:[["Nom","le nom de {famille} : Diallo"],["Prénom","le petit nom : {Amara}"],["Date de naissance","le jour, le mois, l'{année}"],["Téléphone","dix {chiffres}, avec l'indicatif"],["On ne dit pas","« mon petit nom » sur un formulaire",true]],
       say:"Nom. Prénom. Date de naissance. Téléphone.",
       note:"Attention : dans plusieurs pays, la case « nom » attend le nom complet. Ici, elle attend le nom de famille seul. Le dire."},

      {t:'ana', h:"Tu habites où ?",
       p:"Les trois cases suivantes reprennent l'adresse du Défi 1.",
       mots:[["Adresse","le numéro, la {rue}, l'appartement"],["Ville","{Montréal}"],["Province","{Québec}, ou QC"],["Code postal","{H1T 1C5}"],["On ne dit pas","le pays, sauf si l'envoi part du Canada",true]],
       say:"Adresse. Ville. Province. Code postal.",
       note:"Faire remarquer que c'est la même adresse qu'au Défi 1, découpée en cases. Rien de neuf, une autre présentation."},

      {t:'ana', h:"Signer, et dater",
       p:"Les deux dernières cases, et les plus oubliées.",
       mots:[["Signature","ton nom écrit à la {main}"],["Date","le jour où tu {signes}"],["Où ?","en {bas}, souvent à droite"],["Attention","une signature n'est pas en lettres détachées"],["On ne dit pas","« je signe plus tard » : sans signature, rien ne part",true]],
       say:"Signature. Date. En bas, à droite.",
       note:"Faire signer une feuille blanche à chacun. Beaucoup n'ont jamais fixé leur signature en caractères latins, et hésitent devant un vrai comptoir."},

      {t:'labo', h:"Case par case",
       p:"Choisis une case et ce que tu veux savoir.",
       axes:[
         {id:'p', lbl:'Quelle case ?', opts:[
           ['a','Nom et prénom'],
           ['b','Adresse'],
           ['c','Signature']]},
         {id:'q', lbl:'Tu veux quoi ?', opts:[['1','ce qu\'on écrit'],['2','un exemple'],['3','une question à poser']]}],
       out:{
         a1:{w:["Le nom de famille, puis le prénom."], say:"Le nom de famille, puis le prénom.", n:'deux cases, jamais une seule'},
         a2:{w:["Nom : Diallo · Prénom : Amara"], say:"Nom, Diallo. Prénom, Amara.", n:'l\'exemple du module'},
         a3:{w:["Je mets quoi ici ?"], say:"Je mets quoi ici ?", n:'la question la plus utile devant un formulaire'},
         b1:{w:["Le numéro, la rue, l'appartement."], say:"Le numéro, la rue, l'appartement.", n:'la ville a sa propre case'},
         b2:{w:["4520, rue Bélanger, app. 3"], say:"4520, rue Bélanger, appartement 3.", n:'l\'adresse d\'Amara'},
         b3:{w:["J'écris l'appartement où ?"], say:"J'écris l'appartement où ?", n:'certaines fiches ont une case à part'},
         c1:{w:["Ton nom écrit à la main."], say:"Ton nom écrit à la main.", n:'pas en lettres détachées'},
         c2:{w:["Signature : Amara Diallo"], say:"Signature. Amara Diallo.", n:'toujours la même, d\'un papier à l\'autre'},
         c3:{w:["Je signe où ?"], say:"Je signe où ?", n:'trois mots, et le préposé montre du doigt'},
       },
       note:"Neuf extraits. Faire remplir un vrai formulaire vierge, debout, contre le mur : c'est la position du comptoir."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les huit mots des cases.",
       rows:[
         ["Nom","le nom de famille"],
         ["Prénom","le petit nom"],
         ["Adresse","numéro, rue, appartement"],
         ["Ville","Montréal"],
         ["Code postal","six caractères"],
         ["Signature","à la main, en bas"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["écrire son nom complet dans la case « Nom »","la case attend le nom de famille",
          "« Nom » et « Prénom » sont deux cases séparées. Le nom de famille va dans la première, le prénom dans la seconde."],
         ["laisser la case « Signature » vide","le formulaire n'est pas valide",
          "Sans signature, rien ne part et rien ne se remet. C'est la case que le préposé regarde en dernier, et la première qu'il redemande."],
         ["signer en lettres détachées","ce n'est pas une signature",
          "Une signature s'écrit à la main, attachée, et reste la même d'un papier à l'autre. C'est elle qui vous identifie."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans la case « Nom », on écrit…", opts:["le nom de famille","le nom complet"], ok:0,
          fb:"Le prénom a sa propre case."},
         {q:"La signature va…", opts:["en bas","en haut"], ok:0,
          fb:"En bas, souvent à droite."},
         {q:"Une signature s'écrit…", opts:["à la main","en lettres détachées"], ok:0,
          fb:"À la main, toujours la même."},
         {q:"« Je mets quoi ici ? » sert à…", opts:["demander de l'aide","refuser"], ok:0,
          fb:"C'est la question à poser devant une case qu'on ne comprend pas."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Nom, prénom, adresse, ville, code postal, signature, date. Les mêmes cases sur tous les formulaires. Et devant une case obscure : <b>Je mets quoi ici ?</b>"},
    ]
  },

  t2imper: {
    eye:'Mini-leçon', tit:"Écrivez, signez, remplissez",
    blocs:[
      {t:'texte', h:"Le verbe qui donne une consigne",
       p:"Au comptoir, on ne vous dit pas « vous écrivez votre nom ». On vous dit <b>écrivez votre nom</b>. Le mot « vous » disparaît, et il ne reste que le verbe. C'est la forme des consignes : celle des préposés, celle des formulaires, celle des affiches.",
       note:"C'est un savoir du programme au niveau 2 : l'impératif présent. Ne pas nommer la forme d'abord ; la faire reconnaître, puis la nommer."},

      {t:'ana', h:"Les six verbes de la poste",
       p:"Ils reviennent à chaque visite.",
       mots:[["On dit","{Posez} la boîte ici."],["Aussi","{Remplissez} le formulaire."],["Aussi","{Écrivez} votre nom."],["Aussi","{Signez} en bas."],["Aussi","{Gardez} votre reçu. · {Apportez} une carte."],["On ne dit pas","« Vous posez la boîte » pour donner une consigne",true]],
       say:"Posez la boîte ici. Remplissez le formulaire. Écrivez votre nom. Signez en bas.",
       note:"Six verbes, et le comptoir est couvert. Les faire mimer : poser, remplir, écrire, signer, garder, apporter."},

      {t:'ana', h:"La forme est facile : le verbe finit par -ez",
       p:"On prend la forme de « vous », et on enlève le mot « vous ».",
       mots:[["Vous signez","→ {Signez} !"],["Vous écrivez","→ {Écrivez} !"],["Vous remplissez","→ {Remplissez} !"],["Vous apportez","→ {Apportez} !"],["On ne dit pas","« Vous signez ici » quand on donne un ordre poli",true]],
       say:"Vous signez. Signez. Vous écrivez. Écrivez.",
       note:"La règle tient en un geste : on efface le « vous » avec la main. Le faire vraiment, au tableau."},

      {t:'ana', h:"Et quand on dit « tu »",
       p:"Un ami, un enfant, un camarade de classe.",
       mots:[["On dit","{Signe} ici."],["Aussi","{Écris} ton nom."],["Aussi","{Remplis} le formulaire."],["Attention","{signe} s'écrit sans s, mais {écris} et {remplis} gardent le leur"],["On ne dit pas","« Tu signes ici » pour demander à quelqu'un de signer",true]],
       say:"Signe ici. Écris ton nom. Remplis le formulaire.",
       note:"Le préposé vouvoie toujours. Karim tutoie Amara : c'est là qu'on entend la forme en « tu » dans le module."},

      {t:'labo', h:"La même consigne, deux façons",
       p:"Choisis un verbe et à qui tu parles.",
       axes:[
         {id:'p', lbl:'Quel verbe ?', opts:[
           ['a','signer'],
           ['b','écrire'],
           ['c','remplir']]},
         {id:'q', lbl:'Tu parles à qui ?', opts:[['1','au comptoir (vous)'],['2','à un ami (tu)'],['3','je demande où']]}],
       out:{
         a1:{w:["Signez en bas, à droite."], say:"Signez en bas, à droite.", n:'la phrase du préposé'},
         a2:{w:["Signe ici."], say:"Signe ici.", n:'deux mots, entre amis'},
         a3:{w:["Je signe où ?"], say:"Je signe où ?", n:'la question qui règle tout'},
         b1:{w:["Écrivez votre nom dans la case."], say:"Écrivez votre nom dans la case.", n:'« votre » va avec « écrivez »'},
         b2:{w:["Écris ton nom ici."], say:"Écris ton nom ici.", n:'« ton » va avec « écris »'},
         b3:{w:["J'écris mon nom où ?"], say:"J'écris mon nom où ?", n:'on montre la feuille en le disant'},
         c1:{w:["Remplissez ce formulaire, s'il vous plaît."], say:"Remplissez ce formulaire, s'il vous plaît.", n:'le « s\'il vous plaît » adoucit l\'ordre'},
         c2:{w:["Remplis le formulaire."], say:"Remplis le formulaire.", n:'sans -ez, mais le s reste'},
         c3:{w:["Je remplis quelle case ?"], say:"Je remplis quelle case ?", n:'plus précis que « je fais quoi ? »'},
       },
       note:"Neuf extraits. Faire jouer le comptoir : un élève donne les six consignes, l'autre les exécute vraiment sur une feuille."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Les six consignes du comptoir.",
       rows:[
         ["Posez la boîte ici.","poser"],
         ["Remplissez le formulaire.","remplir"],
         ["Écrivez votre nom.","écrire"],
         ["Signez en bas.","signer"],
         ["Gardez votre reçu.","garder"],
         ["Apportez une carte avec votre photo.","apporter"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « vous signez » pour demander de signer","le « vous » reste",
          "Pour donner une consigne, on enlève le « vous » : Signez ici. Avec le « vous », la phrase raconte ce que vous faites, elle ne demande rien."],
         ["mettre un s à « écris » quand on tutoie","Écris ton nom, pas « écrits »",
          "À l'ordre, la forme en « tu » perd son s pour les verbes en -er : signe, écoute, apporte. Écris et remplis gardent le leur parce qu'ils sont d'un autre groupe."],
         ["croire que la consigne est impolie","« Signez ici » n'est pas sec",
          "C'est la forme normale au comptoir. Le « s'il vous plaît » l'adoucit, mais elle est déjà polie sans lui."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le préposé dit…", opts:["Signez ici.","Vous signez ici."], ok:0,
          fb:"On enlève le « vous » pour donner une consigne."},
         {q:"À un ami, on dit…", opts:["Signe ici.","Signez ici."], ok:0,
          fb:"La forme en « tu », sans -ez."},
         {q:"« Gardez votre reçu » veut dire…", opts:["ne le jetez pas","donnez-le-moi"], ok:0,
          fb:"Le reçu prouve que vous avez payé. On le garde."},
         {q:"Le verbe de la consigne finit par…", opts:["-ez","-ent"], ok:0,
          fb:"-ez, comme la forme de « vous »."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"On enlève le « vous » : <b>Posez · Remplissez · Écrivez · Signez · Gardez · Apportez</b>. Avec un ami, on enlève le -ez : <b>Signe · Écris · Remplis</b>."},
    ]
  },

  t2poss: {
    eye:'Mini-leçon', tit:"Mon nom, votre nom",
    blocs:[
      {t:'texte', h:"Le petit mot qui dit à qui c'est",
       p:"Devant un nom, un petit mot dit à qui appartient la chose. Quand je parle de moi : <b>mon</b>, <b>ma</b>, <b>mes</b>. Quand le préposé me parle : <b>votre</b>, <b>vos</b>. Ce sont les deux seules séries dont on a besoin au comptoir, et elles reviennent dans chaque phrase.",
       note:"C'est un savoir du programme au niveau 2 : les déterminants possessifs. Se limiter à ces deux séries — « son », « leur » et le reste viendront plus tard."},

      {t:'ana', h:"Quand je parle de moi",
       p:"Trois formes, et c'est le nom qui décide.",
       mots:[["Devant un mot masculin","{mon} nom · {mon} colis · {mon} reçu"],["Devant un mot féminin","{ma} rue · {ma} signature · {ma} lettre"],["Devant plusieurs choses","{mes} papiers · {mes} timbres"],["Attention","{mon} adresse, jamais « ma adresse »"],["On ne dit pas","« ma nom » ni « mon rue »",true]],
       say:"Mon nom. Ma rue. Mes papiers. Mon adresse.",
       note:"La règle du « mon adresse » se retient par l'oreille : « ma adresse » fait deux voyelles collées, et la bouche refuse."},

      {t:'ana', h:"Quand le préposé me parle",
       p:"Deux formes seulement, et c'est plus facile.",
       mots:[["Une seule chose","{votre} nom · {votre} adresse · {votre} signature"],["Plusieurs choses","{vos} papiers · {vos} timbres"],["Le genre","ne change rien : {votre} nom, {votre} rue"],["Au comptoir","on entend « votre » dix fois par visite"],["On ne dit pas","« ton nom » à un préposé",true]],
       say:"Votre nom. Votre adresse. Vos papiers.",
       note:"Insister : le masculin et le féminin ne changent rien à « votre ». C'est plus simple que « mon / ma », et ça rassure."},

      {t:'ana', h:"Les deux dans la même phrase",
       p:"C'est ainsi qu'on les entend vraiment.",
       mots:[["Le préposé dit","Écrivez {votre} nom ici."],["Je réponds","{Mon} nom, c'est Diallo."],["Le préposé dit","{Vos} papiers, s'il vous plaît."],["Je réponds","Voici {mes} papiers."],["On ne dit pas","« Voici votre papiers » quand on parle de soi",true]],
       say:"Écrivez votre nom ici. Mon nom, c'est Diallo. Vos papiers, s'il vous plaît. Voici mes papiers.",
       note:"Faire jouer ce court échange debout, deux par deux. C'est exactement la scène du Défi 2."},

      {t:'labo', h:"Mon ou votre ?",
       p:"Choisis un mot et qui parle.",
       axes:[
         {id:'p', lbl:'Quel mot ?', opts:[
           ['a','le nom'],
           ['b','la rue'],
           ['c','les papiers']]},
         {id:'q', lbl:'Qui parle ?', opts:[['1','moi'],['2','le préposé'],['3','la règle']]}],
       out:{
         a1:{w:["Mon nom, c'est Diallo."], say:"Mon nom, c'est Diallo.", n:'nom est masculin : mon'},
         a2:{w:["Écrivez votre nom."], say:"Écrivez votre nom.", n:'le préposé dit toujours « votre »'},
         a3:{w:["mon (masculin) · votre (les deux)"], say:"Mon nom. Votre nom.", n:'une forme change, l\'autre non'},
         b1:{w:["Ma rue, c'est la rue Bélanger."], say:"Ma rue, c'est la rue Bélanger.", n:'rue est féminin : ma'},
         b2:{w:["Quelle est votre rue ?"], say:"Quelle est votre rue ?", n:'« votre » ne change pas au féminin'},
         b3:{w:["ma (féminin) · votre (les deux)"], say:"Ma rue. Votre rue.", n:'le féminin n\'existe que du côté de « ma »'},
         c1:{w:["Voici mes papiers."], say:"Voici mes papiers.", n:'plusieurs choses : mes'},
         c2:{w:["Vos papiers, s'il vous plaît."], say:"Vos papiers, s'il vous plaît.", n:'plusieurs choses : vos'},
         c3:{w:["mes · vos — quand il y en a plusieurs"], say:"Mes papiers. Vos papiers.", n:'les deux prennent un s'},
       },
       note:"Neuf extraits. Faire le tour de la classe : chacun dit « mon nom, c'est… » et « ma rue, c'est… »."},

      {t:'ex', h:"À écouter et à répéter",
       p:"Six phrases du comptoir.",
       rows:[
         ["Mon nom, c'est Diallo.","masculin : mon"],
         ["Ma rue, c'est la rue Bélanger.","féminin : ma"],
         ["Mon adresse est à Montréal.","voyelle : mon"],
         ["Voici mes papiers.","plusieurs : mes"],
         ["Écrivez votre adresse.","le préposé : votre"],
         ["Vos papiers, s'il vous plaît.","plusieurs : vos"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ma adresse »","le mot commence par une voyelle",
          "On dit mon adresse, mon enveloppe, mon appartement — même si le mot est féminin. Deux voyelles collées ne se disent pas."],
         ["dire « ton nom » au préposé","c'est le tutoiement",
          "Au comptoir, on vouvoie : votre nom, votre adresse. « Ton » est pour un ami ou un enfant."],
         ["dire « mes » pour une seule chose","« mes reçu »",
          "« mes » s'emploie seulement quand il y en a plusieurs : mes papiers, mes timbres. Pour un seul : mon reçu."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"On dit…", opts:["mon adresse","ma adresse"], ok:0,
          fb:"Le mot commence par une voyelle : mon."},
         {q:"« rue » est féminin, alors on dit…", opts:["ma rue","mon rue"], ok:0,
          fb:"Ma rue. Mais « votre rue » ne change pas."},
         {q:"Le préposé dit…", opts:["votre nom","ton nom"], ok:0,
          fb:"Au comptoir, on vouvoie toujours."},
         {q:"Pour plusieurs papiers, je dis…", opts:["mes papiers","mon papiers"], ok:0,
          fb:"Mes, avec un s, comme le nom."},
       ]},

      {t:'revoir', h:"À retenir",
       p:"Moi : <b>mon</b> (masculin), <b>ma</b> (féminin), <b>mes</b> (plusieurs) — et <b>mon</b> devant une voyelle. Le préposé : <b>votre</b> pour une chose, <b>vos</b> pour plusieurs."},
    ]
  },
};
