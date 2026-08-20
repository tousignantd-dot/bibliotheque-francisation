const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:"Le féminin qu'on entend",
    blocs:[
      {t:'texte', h:"Une consonne qui se réveille",
       p:"« Petit » et « petite » ne se prononcent pas pareil. Au masculin, le <b>t</b> final est muet ; au féminin, le <b>-e</b> le réveille et on l'entend. C'est vrai pour des dizaines d'adjectifs — et c'est ce qui permet d'entendre le genre sans voir le mot écrit.",
       note:"Dans un magasin de vêtements, cette différence revient à chaque phrase : un manteau gris, une veste grise."},

      {t:'ana', h:"Au masculin : la consonne dort",
       p:"La dernière lettre ne se prononce pas.",
       mots:[['On écrit','peti{t}'],['On entend','peti',true],['Aussi','gri{s} · ver{t} · cour{t}']],
       say:"Un manteau gris, un peu court.",
       note:"Autres exemples : gran<b>d</b>, blan<b>c</b>, lon<b>g</b>, épai<b>s</b>. La consonne est là à l'écrit, muette à l'oral."},

      {t:'ana', h:"Au féminin : elle se réveille",
       p:"Le <b>-e</b> ajouté fait prononcer la consonne d'avant.",
       mots:[['On écrit','peti{te}'],['On entend','petit',true],['Aussi','gri{se} · ver{te} · cour{te}']],
       say:"Une veste grise, un peu courte.",
       note:"C'est la même consonne, mais on l'entend. C'est pour cela qu'on peut reconnaître le genre à l'oreille."},

      {t:'texte', h:"Ce que ça vous donne",
       p:"Deux choses. À l'<b>écoute</b> : si vous entendez la consonne, l'objet est féminin — donc vous savez s'il s'agit d'une veste ou d'un manteau, même si vous avez manqué le nom. À l'<b>écrit</b> : si vous prononcez le mot au féminin dans votre tête, vous entendez la lettre qu'il faut écrire.",
       note:"Ce deuxième usage est très pratique : « court » ou « cour » ? Dites « courte » : le <b>t</b> apparaît."},

      {t:'labo', h:"Écoutez les paires",
       p:"Choisissez une paire et écoutez la consonne apparaître.",
       axes:[{id:'p', lbl:'Quelle paire ?', opts:[
         ['a','petit / petite'],
         ['b','gris / grise'],
         ['c','vert / verte'],
         ['d','court / courte'],
         ['e','grand / grande']]}],
       out:{
         a:{w:['peti{t} → peti{te}'], say:"Un chandail petit, une veste petite.", n:'le t se réveille au féminin'},
         b:{w:['gri{s} → gri{se}'], say:"Un manteau gris, une veste grise.", n:'le s devient [z]'},
         c:{w:['ver{t} → ver{te}'], say:"Un chandail vert, une tuque verte.", n:'le t se réveille'},
         d:{w:['cour{t} → cour{te}'], say:"Un manteau court, une manche courte.", n:'le t se réveille'},
         e:{w:['gran{d} → gran{de}'], say:"Un manteau grand, une taille grande.", n:'le d devient [d]'},
       },
       note:"Dans les cinq paires, la même chose se produit : le <b>-e</b> du féminin fait prononcer la consonne d'avant."},

      {t:'ex', h:"Les adjectifs du module",
       p:"Écoutez chaque paire et répétez-la.",
       rows:[
         ["Un manteau gris, une veste grise.","le s se réveille"],
         ["Un chandail vert, une tuque verte.","le t se réveille"],
         ["Un manteau court, une manche courte.","le t se réveille"],
         ["Un pantalon grand, une taille grande.","le d se réveille"],
         ["Un col épais, une semelle épaisse.","le s se réveille"],
         ["Un manteau chaud, une doublure chaude.","le d se réveille"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["prononcer la consonne au masculin","« un manteau gri », pas « griss »",
          "Au masculin, la consonne finale est muette. La prononcer donne un mot qui n'existe pas."],
         ["oublier le -e à l'écrit","si vous l'entendez, il faut l'écrire",
          "Le <b>-e</b> du féminin ne se prononce pas lui-même : il fait seulement sonner la consonne d'avant. Il s'écrit quand même."],
         ["croire que tous les adjectifs marchent ainsi","« rouge », « jaune », « beige » ne changent pas",
          "Les adjectifs qui finissent déjà par <b>-e</b> au masculin ne bougent pas au féminin : un manteau rouge, une veste rouge."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"« Une veste grise » : le s…", opts:["se prononce","est muet"], ok:0,
          fb:"Le -e du féminin le fait sonner."},
         {q:"« Un manteau gris » : le s…", opts:["se prononce","est muet"], ok:1,
          fb:"Au masculin, la consonne finale dort."},
         {q:"« Rouge » au féminin devient…", opts:["rouge","rougee"], ok:0,
          fb:"Les adjectifs en -e ne changent pas."},
         {q:"Pour savoir s'il faut écrire un t à la fin…", opts:["on dit le mot au féminin","on devine"], ok:0,
          fb:"« courte » fait apparaître le t de « court »."},
       ]},
    ]
  },

  t1taille: {
    eye:'Mini-leçon', tit:"Dire ce qui ne va pas",
    blocs:[
      {t:'texte', h:"Un adjectif, un endroit",
       p:"« Il est un peu <b>serré</b> <b>aux épaules</b>. » Un adjectif et un endroit : c'est tout ce qu'il faut pour qu'on vous propose la bonne chose. Dire seulement « ça ne va pas » oblige la personne à deviner.",
       note:"Cette formule en deux morceaux marche pour n'importe quel vêtement, dans n'importe quel magasin."},

      {t:'ana', h:"Trop petit : serré",
       p:"On ne dit pas « petit » pour un vêtement qu'on porte : on dit <b>serré</b>.",
       mots:[['L\'adjectif','{serré}'],['L\'endroit','aux épaules · à la taille',true],['La phrase','Il est serré aux épaules.']],
       say:"Il est un peu serré aux épaules.",
       note:"« Un peu » adoucit et laisse la porte ouverte : « un peu serré » invite à essayer la taille au-dessus, sans rejeter le vêtement."},

      {t:'ana', h:"Trop grand : large",
       p:"<b>large</b> ou <b>ample</b>. « Ample » est plus neutre : c'est parfois une coupe voulue.",
       mots:[['L\'adjectif','{large} · ample'],['L\'endroit','aux épaules · au dos',true],['La phrase','Il est trop large aux épaules.']],
       say:"Il est trop large aux épaules.",
       note:"Un manteau d'hiver <em>doit</em> être un peu ample : il faut de la place pour un chandail. « Ample » n'est donc pas un défaut."},

      {t:'ana', h:"Les longueurs",
       p:"<b>court</b> et <b>long</b>, pour le vêtement entier ou pour les manches.",
       mots:[['Le vêtement','il est trop {court}'],['Les manches','elles sont trop {longues}',true],['L\'accord','manche est féminin']],
       say:"Les manches sont un peu longues.",
       note:"Attention à l'accord : <em>les manches sont longues</em>, <em>le manteau est long</em>. C'est le nom qui décide."},

      {t:'texte', h:"Dire l'endroit change la réponse",
       p:"« Ça ne me va pas » obtient une autre taille. « C'est serré <b>aux épaules</b> » obtient une autre <b>coupe</b> — parfois la même taille dans un modèle différent. Nommer l'endroit permet à la personne de vous aider vraiment.",
       note:"Les endroits utiles : aux épaules, à la taille, aux manches, à la poitrine, aux hanches, au col."},

      {t:'labo', h:"Quel adjectif ?",
       p:"Choisissez un problème et voyez comment le dire.",
       axes:[{id:'p', lbl:'Quel problème ?', opts:[
         ['a','Je ne peux pas lever les bras.'],
         ['b','Il y a trop de place partout.'],
         ['c','Les manches dépassent la main.'],
         ['d','Le manteau arrive à la taille.'],
         ['e','Je ne peux pas fermer le manteau.']]}],
       out:{
         a:{w:['Il est {serré} aux épaules.'], say:"Il est un peu serré aux épaules.", n:'trop petit › serré'},
         b:{w:['Il est trop {large}.'], say:"Il est trop large aux épaules.", n:'trop grand › large'},
         c:{w:['Les manches sont trop {longues}.'], say:"Les manches sont un peu longues.", n:'accord au féminin pluriel'},
         d:{w:['Il est trop {court}.'], say:"Il est trop court, il faudrait aux genoux.", n:'la longueur du vêtement'},
         e:{w:['Il est {serré} à la poitrine.'], say:"Il est serré à la poitrine.", n:'l\'endroit précise le problème'},
       },
       note:"Cinq problèmes, deux adjectifs : serré et large couvrent presque tout. Ce qui change, c'est l'endroit."},

      {t:'ex', h:"Les phrases de la cabine",
       p:"Écoutez chacune et répétez-la.",
       rows:[
         ["Il est un peu serré aux épaules.","trop petit"],
         ["Je ne peux pas lever les bras.","la preuve que c'est serré"],
         ["Il est trop large aux épaules.","trop grand"],
         ["Les manches sont un peu longues.","la longueur, au féminin pluriel"],
         ["Il est trop court.","la longueur du vêtement"],
         ["Est-ce que vous l'avez dans la taille au-dessus ?","la question qui suit"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « petit » au lieu de « serré »","« il est serré », pas « il est petit »",
          "« Petit » décrit la taille de l'objet ; « serré » décrit ce que vous ressentez en le portant. C'est le second qu'on emploie en cabine."],
         ["ne pas dire l'endroit","« serré aux épaules » plutôt que « ça ne va pas »",
          "L'endroit permet de proposer une autre coupe, pas seulement une autre taille."],
         ["oublier l'accord des manches","« les manches sont longues », au féminin pluriel",
          "Manche est féminin. C'est une des rares fautes d'accord qui s'entendent nettement."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un vêtement trop petit est…", opts:["petit","serré"], ok:1,
          fb:"« Serré » décrit ce qu'on ressent en le portant."},
         {q:"Pourquoi dire l'endroit ?", opts:["pour obtenir une autre coupe","par politesse"], ok:0,
          fb:"Une autre coupe, pas seulement une autre taille."},
         {q:"« Les manches sont… »", opts:["longues","longs"], ok:0,
          fb:"Manche est féminin."},
         {q:"Un manteau d'hiver doit être…", opts:["ajusté","un peu ample"], ok:1,
          fb:"Il faut de la place pour un chandail."},
       ]},
    ]
  },

  t1decrire: {
    eye:'Mini-leçon', tit:"Décrire un vêtement",
    blocs:[
      {t:'texte', h:"Quatre informations suffisent",
       p:"<b>Ce que c'est</b>, <b>la couleur</b>, <b>la matière</b>, <b>la coupe</b>. Avec ces quatre-là, la personne en face voit exactement le vêtement dont vous parlez — au magasin, au téléphone, ou dans un message.",
       note:"« C'est un manteau noir, en duvet, aux genoux. » Une phrase, trois informations, et l'image est claire."},

      {t:'ana', h:"La couleur : après le nom, et accordée",
       p:"Comme tous les adjectifs ordinaires.",
       mots:[['Masculin','un manteau {noir}'],['Féminin','une veste {noire}',true],['Pluriel','des bottes {noires}']],
       say:"C'est un manteau noir.",
       note:"Quelques couleurs ne changent jamais : <b>marine</b>, <b>beige</b>, <b>kaki</b>, <b>crème</b>, <b>orange</b>. « Une veste beige », « des bottes marine »."},

      {t:'ana', h:"La matière : « en » + la matière",
       p:"Un seul petit mot, toujours le même.",
       mots:[['La forme','{en} + la matière'],['Exemples','en laine · en coton · en cuir',true],['Aussi','en duvet · en polyester']],
       say:"C'est un manteau en duvet.",
       note:"On dit aussi « de laine » dans certains cas figés — « un bas de laine » — mais <b>en</b> passe partout et ne se trompe jamais."},

      {t:'ana', h:"La coupe et la longueur",
       p:"Ce qui dit la forme du vêtement.",
       mots:[['La coupe','{ajusté} · ample · droit'],['La longueur','court · long · {aux genoux}',true],['La phrase','un manteau ample, aux genoux']],
       say:"Une coupe ample, aux genoux.",
       note:"« Aux genoux », « à la taille », « à mi-cuisse » : on situe la longueur par rapport au corps, pas en centimètres."},

      {t:'texte', h:"L'ordre des mots",
       p:"Le nom, puis la couleur, puis la matière, puis la coupe : « un manteau <b>noir</b>, <b>en duvet</b>, <b>aux genoux</b> ». On peut en dire moins, jamais dans le désordre.",
       note:"Cet ordre est celui de tous les catalogues et de tous les vendeurs. Le suivre rend la description immédiatement compréhensible."},

      {t:'labo', h:"Construisez la description",
       p:"Choisissez un vêtement et voyez sa description complète.",
       axes:[{id:'p', lbl:'Quel vêtement ?', opts:[
         ['a','un manteau d\'hiver'],
         ['b','une veste de printemps'],
         ['c','des bottes'],
         ['d','un chandail'],
         ['e','un pantalon']]}],
       out:{
         a:{w:['un manteau {noir}, en {duvet}, aux genoux'], say:"C'est un manteau noir, en duvet, aux genoux.", n:'nom, couleur, matière, longueur'},
         b:{w:['une veste {grise}, en {coton}, courte'], say:"C'est une veste grise, en coton, courte.", n:'accord au féminin'},
         c:{w:['des bottes {noires}, en {cuir}, imperméables'], say:"Ce sont des bottes noires, en cuir, imperméables.", n:'accord au féminin pluriel'},
         d:{w:['un chandail {vert}, en {laine}, ample'], say:"C'est un chandail vert, en laine, ample.", n:'la matière la plus courante l\'hiver'},
         e:{w:['un pantalon {beige}, en {coton}, droit'], say:"C'est un pantalon beige, en coton, droit.", n:'beige ne s\'accorde jamais'},
       },
       note:"Remarquez e : <b>beige</b> ne change pas au féminin ni au pluriel. C'est le cas de plusieurs couleurs venues de noms de choses."},

      {t:'ex', h:"Les descriptions du module",
       p:"Écoutez chacune.",
       rows:[
         ["C'est un manteau noir, en duvet, aux genoux.","la description complète"],
         ["Une veste grise, en coton, courte.","au féminin"],
         ["Des bottes noires, en cuir, imperméables.","au féminin pluriel"],
         ["Un chandail vert, en laine, ample.","la matière de l'hiver"],
         ["Un pantalon beige, droit.","une couleur invariable"],
         ["Le capuchon est bordé de fourrure.","un détail utile"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["placer la couleur avant le nom","« un manteau noir », pas « un noir manteau »",
          "La couleur suit toujours le nom en français. C'est l'inverse de plusieurs langues."],
         ["accorder les couleurs invariables","« des bottes marine », sans s",
          "marine, beige, kaki, crème, orange : ces couleurs viennent de noms de choses et ne s'accordent pas."],
         ["employer « de » au lieu de « en »","« en laine », « en cuir »",
          "<b>en</b> passe partout pour la matière. « De laine » n'existe que dans des expressions figées."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"L'ordre est…", opts:["nom, couleur, matière","couleur, nom, matière"], ok:0,
          fb:"« un manteau noir, en duvet »."},
         {q:"Pour la matière, on emploie…", opts:["en","avec"], ok:0,
          fb:"« en laine », « en cuir », « en duvet »."},
         {q:"« Des bottes marine » prend-il un s à marine ?", opts:["oui","non"], ok:1,
          fb:"Marine, beige, kaki : invariables."},
         {q:"Le féminin de « vert » est…", opts:["verte","vert"], ok:0,
          fb:"Et on entend le t."},
       ]},
    ]
  },

  t2opinion: {
    eye:'Mini-leçon', tit:"Demander et donner un avis",
    blocs:[
      {t:'texte', h:"Trois questions, trois réponses",
       p:"Devant un miroir, on demande un avis. Trois formules suffisent pour le demander, trois pour le donner — et une pour le nuancer sans blesser.",
       note:"Le vocabulaire de l'opinion figure explicitement au programme du niveau : « ça vous va bien », « ça vous amincit »."},

      {t:'ana', h:"Demander",
       p:"Court, direct, à un proche.",
       mots:[['La plus employée','Qu\'est-ce que tu en {penses} ?'],['Autre','Comment tu {trouves} ça ?',true],['La plus courte','Ça me {va} ?']],
       say:"Qu'est-ce que tu en penses ?",
       note:"À un vendeur, on vouvoie : « Qu'est-ce que vous en pensez ? » Mais son avis reste un avis de vente."},

      {t:'ana', h:"Donner un avis positif",
       p:"Trois expressions figées. On ne les invente pas, on les réutilise.",
       mots:[['La plus courante','Ça te {va} bien.'],['Sur la coupe','Ça {tombe} bien.',true],['Sur la personne','Il te {fait} bien.']],
       say:"Le noir te va bien.",
       note:"Attention : ce sont des expressions. On ne dit pas « ça te va beau » ni « ça te va joli »."},

      {t:'ana', h:"Nuancer sans blesser",
       p:"Un mot annonce l'avis honnête, et la comparaison remplace la condamnation.",
       mots:[['L\'annonce','{Franchement}, …'],['La formule','Je {trouve que}…',true],['La comparaison','Le noir tombe {mieux}.']],
       say:"Franchement, il est un peu trop grand. Le noir tombe mieux.",
       note:"« Franchement » prévient que l'avis va être honnête — et c'est précisément ce qu'on demande à un ami. Comparer plutôt que condamner adoucit tout."},

      {t:'texte', h:"L'avis du vendeur",
       p:"« Ça vous va bien » est une phrase de vente autant qu'un avis. Elle est parfois vraie, toujours polie. Si vous hésitez, une question plus précise obtient une réponse plus utile : « <b>Est-ce que la coupe me va ?</b> » ou « <b>Est-ce que c'est trop grand aux épaules ?</b> »",
       note:"Une question fermée sur un point précis est plus difficile à esquiver qu'une question générale."},

      {t:'labo', h:"Quelle formule ?",
       p:"Choisissez une situation.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','Vous demandez à une amie.'],
         ['b','Vous trouvez que ça lui va bien.'],
         ['c','Vous trouvez que c\'est trop grand.'],
         ['d','Vous comparez deux manteaux.'],
         ['e','Vous demandez à la vendeuse.']]}],
       out:{
         a:{w:["Qu'est-ce que tu en {penses} ?"], say:"Qu'est-ce que tu en penses ?", n:'la question la plus employée'},
         b:{w:['Le noir te {va} bien.'], say:"Le noir te va bien.", n:'expression figée'},
         c:{w:['{Franchement}, il est un peu trop grand.'], say:"Franchement, il est un peu trop grand.", n:'l\'annonce adoucit'},
         d:{w:['Le noir tombe {mieux} que le bleu.'], say:"Le noir tombe mieux que le bleu.", n:'comparer plutôt que condamner'},
         e:{w:['Est-ce que la coupe me {va} ?'], say:"Est-ce que la coupe me va ?", n:'question précise, réponse utile'},
       },
       note:"La dernière est la plus fine : à un vendeur, une question précise obtient une réponse plus honnête qu'une question générale."},

      {t:'ex', h:"Les avis du module",
       p:"Écoutez chacun.",
       rows:[
         ["Qu'est-ce que tu en penses ?","demander"],
         ["Le noir te va bien.","avis positif"],
         ["Il est sobre, tu pourras le porter au travail.","un argument, pas juste un avis"],
         ["Franchement, il est trop grand aux épaules.","avis nuancé"],
         ["Le noir tombe mieux.","comparer"],
         ["Ce n'est pas décoratif, c'est utile.","corriger une idée reçue"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["dire « ça te va beau »","c'est « ça te va bien »",
          "Ce sont des expressions figées. « Beau » ne s'emploie pas ici, même si le sens serait clair."],
         ["donner un avis sans nuance","« franchement » et la comparaison adoucissent",
          "« C'est laid » ferme la conversation. « Le noir tombe mieux » dit la même chose et laisse le choix."],
         ["prendre l'avis du vendeur pour une vérité","c'est aussi une phrase de vente",
          "Elle n'est pas malhonnête, mais elle est prévisible. Une question précise vaut mieux."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Pour demander un avis à un ami…", opts:["Qu'est-ce que tu en penses ?","Comment c'est ?"], ok:0,
          fb:"La formule la plus employée."},
         {q:"L'expression correcte est…", opts:["ça te va beau","ça te va bien"], ok:1,
          fb:"C'est une expression figée."},
         {q:"« Franchement » annonce…", opts:["un avis honnête","un reproche"], ok:0,
          fb:"C'est ce qu'on attend d'un ami."},
         {q:"L'avis d'un vendeur est…", opts:["toujours vrai","aussi une phrase de vente"], ok:1,
          fb:"Posez une question précise pour obtenir mieux."},
       ]},
    ]
  },

  t2entretien: {
    eye:'Mini-leçon', tit:"Cinq dessins dans le col",
    blocs:[
      {t:'texte', h:"Une étiquette, cinq symboles",
       p:"Dans le col ou la couture de côté, une petite étiquette porte cinq dessins. Ils disent comment laver, blanchir, sécher, repasser et nettoyer. Ces cinq symboles sont les mêmes partout dans le monde — une fois appris, ils servent toute la vie.",
       note:"Un manteau d'hiver mal lavé perd sa chaleur. Ce n'est pas une question d'apparence."},

      {t:'ana', h:"Le bac d'eau : le lavage",
       p:"Le chiffre à l'intérieur est la température maximale.",
       mots:[['Un bac avec 30','laver à {30} degrés'],['Un bac avec une main','lavage à la {main}',true],['Un bac barré','ne pas laver à l\'eau']],
       say:"Le bac d'eau avec un chiffre, c'est la température de lavage.",
       note:"Sur un manteau en duvet, l'eau chaude tasse le duvet et le manteau perd sa chaleur. Trente degrés, jamais plus."},

      {t:'ana', h:"Le triangle : l'eau de Javel",
       p:"Un triangle barré veut dire : jamais de Javel.",
       mots:[['Triangle vide','Javel permise'],['Triangle {barré}','pas de Javel',true],['Sur un manteau','toujours barré']],
       say:"Le triangle barré, c'est : pas d'eau de Javel.",
       note:"C'est le symbole le plus souvent barré : presque tous les vêtements de couleur l'interdisent."},

      {t:'ana', h:"Le carré : le séchage",
       p:"Un cercle dedans veut dire que la sécheuse est permise ; les points donnent la température.",
       mots:[['Carré + cercle + 1 point','sécheuse, {basse} température'],['Carré + cercle + 2 points','température moyenne',true],['Carré {barré}','pas de sécheuse']],
       say:"Un point, c'est basse température.",
       note:"Pour un manteau en duvet, la sécheuse à basse température est <em>utile</em> : elle fait regonfler le duvet. C'est contre-intuitif et important."},

      {t:'ana', h:"Le fer et le cercle",
       p:"Le fer, c'est le repassage ; le cercle seul, le nettoyage à sec.",
       mots:[['Fer avec des points','température de {repassage}'],['Fer {barré}','pas de repassage',true],['Cercle','nettoyage à sec']],
       say:"Le fer barré, c'est : pas de repassage.",
       note:"La lettre dans le cercle s'adresse au nettoyeur, pas à vous : elle lui dit quel produit employer."},

      {t:'labo', h:"Que veut dire ce symbole ?",
       p:"Choisissez un symbole.",
       axes:[{id:'p', lbl:'Quel symbole ?', opts:[
         ['a','un bac d\'eau avec « 30 »'],
         ['b','un triangle barré'],
         ['c','un carré avec un cercle et un point'],
         ['d','un carré barré'],
         ['e','un fer barré']]}],
       out:{
         a:{w:['laver à {30} degrés'], say:"Trente degrés, à l'eau froide.", n:'plus chaud, le duvet se tasse'},
         b:{w:['pas d\'{eau de Javel}'], say:"Pas d'eau de Javel. Jamais, sur un manteau.", n:'le symbole le plus souvent barré'},
         c:{w:['sécheuse, {basse} température'], say:"Un point, c'est basse température.", n:'utile : ça fait regonfler le duvet'},
         d:{w:['{pas} de sécheuse'], say:"Le carré barré : pas de sécheuse.", n:'fréquent sur la laine'},
         e:{w:['{pas} de repassage'], say:"Pas de repassage.", n:'de toute façon, on ne repasse pas un manteau'},
       },
       note:"Cinq symboles, cinq consignes. Ils reviennent sur tous les vêtements que vous achèterez."},

      {t:'ex', h:"Les consignes du module",
       p:"Écoutez chacune.",
       rows:[
         ["Le bac d'eau avec un chiffre, c'est la température de lavage.","le lavage"],
         ["Trente degrés, à l'eau froide.","la température"],
         ["Pas d'eau de Javel. Jamais, sur un manteau.","le triangle"],
         ["Un point, c'est basse température.","la sécheuse"],
         ["Ça fait regonfler le duvet.","pourquoi la sécheuse est utile"],
         ["Une ou deux fois par hiver, pas plus.","la fréquence de lavage"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["laver un manteau à l'eau chaude","le duvet se tasse et le manteau perd sa chaleur",
          "C'est irréversible. Trente degrés, c'est écrit sur l'étiquette, et ce n'est pas une suggestion."],
         ["éviter la sécheuse par prudence","pour le duvet, elle est utile",
          "À basse température, elle fait regonfler le duvet. Sécher un manteau de duvet à l'air le laisse plat et froid."],
         ["laver trop souvent","une ou deux fois par hiver",
          "Chaque lavage use le duvet et l'imperméabilisation. Un manteau se brosse et s'aère plus qu'il ne se lave."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Un bac d'eau avec « 30 » veut dire…", opts:["laver à 30 degrés","30 minutes de lavage"], ok:0,
          fb:"C'est la température maximale."},
         {q:"Un triangle barré veut dire…", opts:["pas de Javel","pas de sécheuse"], ok:0,
          fb:"Le carré, c'est le séchage."},
         {q:"Pour un manteau en duvet, la sécheuse est…", opts:["à éviter","utile à basse température"], ok:1,
          fb:"Elle fait regonfler le duvet."},
         {q:"On lave un manteau d'hiver…", opts:["une ou deux fois par hiver","chaque mois"], ok:0,
          fb:"Trop de lavages usent le duvet."},
       ]},
    ]
  },

  t3echange: {
    eye:'Mini-leçon', tit:"Échanger, se faire rembourser, mettre de côté",
    blocs:[
      {t:'texte', h:"Trois choses différentes",
       p:"<b>Échanger</b> : rapporter un article et en prendre un autre. <b>Se faire rembourser</b> : récupérer son argent. <b>Mettre de côté</b> : demander au magasin de garder un article jusqu'à ce qu'on puisse le payer. Trois démarches, trois vocabulaires.",
       note:"La troisième est peu connue et très utile quand la paie n'arrive que vendredi."},

      {t:'ana', h:"L'échange",
       p:"Le plus simple, et parfois le seul possible.",
       mots:[['Ce qu\'on dit','Je voudrais faire un {échange}.'],['Ce qu\'on apporte','l\'article et la {facture}',true],['Le résultat','un autre article, même prix']],
       say:"Vous voulez un échange ou un remboursement ?",
       note:"Sur un article en solde, l'échange est souvent accepté alors que le remboursement ne l'est pas. Demandez avant d'acheter."},

      {t:'ana', h:"Le remboursement",
       p:"Sur le moyen de paiement utilisé. Ce n'est pas au choix du client.",
       mots:[['Payé par {carte}','remboursé sur la carte'],['Payé {comptant}','remboursé comptant',true],['Le délai','souvent 3 à 5 jours sur une carte']],
       say:"Sur la carte qui a servi à payer, oui.",
       note:"Un remboursement sur carte prend quelques jours à apparaître. Ce n'est pas un refus : c'est le délai de la banque."},

      {t:'ana', h:"La mise de côté",
       p:"Le magasin garde l'article ; vous laissez un dépôt.",
       mots:[['La durée','environ {14} jours'],['Le dépôt','environ {20 %} du prix',true],['Si on ne revient pas','le dépôt est perdu']],
       say:"Vous pouvez le mettre de côté. On le garde quatorze jours.",
       note:"Les conditions sont écrites sur le reçu de mise de côté. Gardez-le : c'est votre seule preuve du dépôt versé."},

      {t:'texte', h:"Les trois conditions, toujours les mêmes",
       p:"<b>La facture</b> — sans elle, presque rien n'est possible. <b>Le délai</b> — souvent trente jours, parfois quinze en solde. <b>L'état</b> — étiquettes en place, article non porté dehors. Les trois doivent être réunies.",
       note:"Pour des bottes, « non portées dehors » est vérifiable en dix secondes : la semelle parle."},

      {t:'labo', h:"Est-ce possible ?",
       p:"Choisissez une situation.",
       axes:[{id:'p', lbl:'Quelle situation ?', opts:[
         ['a','12 jours, facture, jamais portées dehors'],
         ['b','40 jours après l\'achat'],
         ['c','sans facture'],
         ['d','portées deux semaines dans la neige'],
         ['e','remboursement comptant, payé par carte']]}],
       out:{
         a:{w:['{oui} — les trois conditions sont réunies'], say:"Parfait, c'est dans les trente jours.", n:'facture, délai, état'},
         b:{w:['{non} — hors délai'], say:"Le délai est de trente jours.", n:'dix jours de trop'},
         c:{w:['{non} — pas de preuve d\'achat'], say:"Vous avez la facture ?", n:'la condition la plus stricte'},
         d:{w:['{non} — l\'article a servi'], say:"Elles ont été portées dehors ?", n:'la semelle le montre'},
         e:{w:['{non} — sur la carte'], say:"Sur la carte qui a servi à payer, oui.", n:'ce n\'est pas au choix du client'},
       },
       note:"Une seule des cinq situations passe. Les quatre autres échouent sur une des trois conditions — ou sur le moyen de paiement."},

      {t:'ex', h:"Les phrases du service à la clientèle",
       p:"Écoutez chacune.",
       rows:[
         ["Vous avez la facture ?","la première question, toujours"],
         ["C'est dans les trente jours.","le délai"],
         ["Elles ont été portées dehors ?","l'état"],
         ["Vous voulez un échange ou un remboursement ?","le choix qu'on vous offre"],
         ["Sur la carte qui a servi à payer.","le moyen de remboursement"],
         ["On le garde quatorze jours.","la mise de côté"],
       ]},

      {t:'piege', h:"Trois pièges à connaître",
       rows:[
         ["jeter la facture","sans elle, presque rien n'est possible",
          "Photographiez-la le jour de l'achat. Beaucoup de magasins acceptent la photo, et le papier des reçus s'efface en quelques mois."],
         ["porter des chaussures dehors avant d'être sûr","la semelle le montre tout de suite",
          "Essayez-les à l'intérieur, en marchant sur un tapis. Une fois dehors, l'échange est refusé."],
         ["croire que le remboursement se fait comme on veut","c'est sur le moyen de paiement utilisé",
          "Payé par carte, remboursé sur la carte. Ce n'est ni une chicane ni du mauvais vouloir : c'est la règle partout."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Sans facture…", opts:["l'échange est possible","c'est presque toujours refusé"], ok:1,
          fb:"C'est la condition la plus stricte."},
         {q:"Un achat payé par carte est remboursé…", opts:["comptant, au choix","sur la carte"], ok:1,
          fb:"C'est la règle partout."},
         {q:"La mise de côté demande…", opts:["un dépôt","rien du tout"], ok:0,
          fb:"Environ 20 % du prix."},
         {q:"Des bottes portées dehors…", opts:["s'échangent quand même","ne s'échangent plus"], ok:1,
          fb:"La semelle le montre en dix secondes."},
       ]},
    ]
  },
};
