const PLUS = {
  prPhon: {
    eye:'Mini-leçon', tit:'Les deux façons de dire « eu »',
    blocs:[
      {t:'texte', h:"Deux lettres, deux sons",
       p:"Les lettres <b>eu</b> ne se prononcent pas toujours de la même façon. Il y a le <b>[ø]</b> de « deux », bouche presque fermée et lèvres arrondies vers l'avant, et le <b>[œ]</b> de « peur », bouche nettement plus ouverte. Beaucoup d'élèves les confondent, parce que dans plusieurs langues il n'existe qu'un seul de ces deux sons.",
       note:"Bonne nouvelle : dans presque tous les cas, ce n'est pas à l'oreille qu'il faut deviner — c'est <b>la fin du mot écrit</b> qui vous dit lequel prononcer."},

      {t:'ana', h:"[ø] — le son fermé de « deux »",
       p:"On l'entend quand le mot se termine par <b>-eu</b> ou <b>-eux</b>, c'est-à-dire quand aucune consonne ne se prononce après.",
       mots:[['Fin du mot','-eu / -eux'],['Se dit','[ø]',true],['Comme dans','d{eu}x']],
       say:'deux',
       note:"Autres mots : <em>peu</em>, <em>milieu</em>, <em>dangereux</em>, <em>coûteux</em>, <em>vieux</em>. Astuce : les adjectifs en <b>-eux</b> tombent tous dans cette famille."},

      {t:'ana', h:"[œ] — le son ouvert de « peur »",
       p:"On l'entend quand une consonne se prononce juste après, surtout dans la terminaison <b>-eur</b>.",
       mots:[['Fin du mot','-eur / -eul / -euf'],['Se dit','[œ]',true],['Comme dans','od{eu}r']],
       say:'odeur',
       note:"Autres mots : <em>chaleur</em>, <em>ascenseur</em>, <em>couvreur</em>, <em>immeuble</em>, <em>jeune</em>. La terminaison <b>-eur</b> est partout dans le vocabulaire du logement."},

      {t:'texte', h:"La règle qui règle 90 % des cas",
       p:"Regardez la <b>dernière lettre prononcée</b> du mot. Si le son « eu » est le dernier son du mot → <b>[ø]</b>, fermé. S'il reste une consonne à prononcer après → <b>[œ]</b>, ouvert.",
       note:"C'est pour ça que <em>dangereux</em> ([ø], le <b>x</b> est muet) et <em>couvreur</em> ([œ], le <b>r</b> se prononce) ne riment pas, même s'ils s'écrivent tous les deux avec « eu »."},

      {t:'labo', h:"Comparez les deux sons",
       p:"Choisissez un mot du module et écoutez sa voyelle.",
       axes:[{id:'m', lbl:'Quel mot ?', opts:[['a','deux'],['b','odeur'],['c','dangereux'],['d','couvreur'],['e','immeuble']]}],
       out:{
         a:{w:['d{eu}x'],        say:'deux',       n:'[ø] — rien après, son fermé'},
         b:{w:['od{eu}r'],       say:'odeur',      n:'[œ] — le r se prononce, son ouvert'},
         c:{w:['danger{eu}x'],   say:'dangereux',  n:'[ø] — le x est muet'},
         d:{w:['couvr{eu}r'],    say:'couvreur',   n:'[œ] — le r se prononce'},
         e:{w:['imm{eu}ble'],    say:'immeuble',   n:'[œ] — bl se prononce après'},
       },
       note:"Écoutez <em>dangereux</em> puis <em>couvreur</em> l'un après l'autre : c'est la paire qui fait le mieux entendre la différence."},

      {t:'ex', h:"Les mots du module, classés",
       p:"Écoutez chacun et répétez-le à voix haute en exagérant la position des lèvres.",
       rows:[
         ["deux","[ø] — fermé"],
         ["peu","[ø] — fermé"],
         ["milieu","[ø] — fermé"],
         ["dangereux","[ø] — le x est muet"],
         ["coûteux","[ø] — le x est muet"],
         ["odeur","[œ] — ouvert"],
         ["chaleur","[œ] — ouvert"],
         ["ascenseur","[œ] — ouvert"],
         ["couvreur","[œ] — ouvert"],
         ["immeuble","[œ] — ouvert"],
         ["jeune","[œ] — ouvert"],
       ]},

      {t:'piege', h:"Deux pièges fréquents",
       rows:[
         ["prononcer « couvreur » comme « couvreu »","« couvreur » se dit [kuvʁœʁ]",
          "Le <b>r</b> final se prononce en français. Si vous le laissez tomber, le mot devient un autre son — et souvent un autre mot."],
         ["dire « jeune » avec le son de « deux »","« jeune » se dit [ʒœn], bouche ouverte",
          "Comparez <em>jeune</em> [œ] et <em>jeûne</em> [ø] : ce sont deux mots différents. Dans <em>jeune</em>, le <b>n</b> se prononce, donc le son est ouvert."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides. Elles ne comptent pas dans votre score.",
       qs:[
         {q:"Le mot « chaleur » contient le son…", opts:["[ø] fermé","[œ] ouvert"], ok:1,
          fb:"Le <b>r</b> se prononce après « eu » : le son est ouvert, [œ]."},
         {q:"Le mot « coûteux » contient le son…", opts:["[ø] fermé","[œ] ouvert"], ok:0,
          fb:"Le <b>x</b> final est muet : « eu » est le dernier son du mot, donc [ø] fermé."},
         {q:"Les adjectifs en -eux (dangereux, coûteux, vieux) se disent…", opts:["toujours [ø]","toujours [œ]"], ok:0,
          fb:"Toute la famille des adjectifs en <b>-eux</b> se prononce [ø] — le x ne se prononce jamais."},
         {q:"Dans « immeuble », le son « eu » est…", opts:["fermé, comme dans deux","ouvert, comme dans peur"], ok:1,
          fb:"Les consonnes <b>bl</b> se prononcent après : la bouche reste ouverte, c'est [œ]."},
       ]},
    ]
  },

  prPro: {
    eye:'Mini-leçon', tit:'Le bon professionnel pour le bon problème',
    blocs:[
      {t:'texte', h:"Pourquoi il faut savoir les nommer",
       p:"Quand vous appelez votre propriétaire ou votre concierge, vous n'êtes pas obligé de savoir réparer — mais <b>nommer le bon métier accélère tout</b>. « Il y a un problème dans la salle de bain » peut vouloir dire dix choses. « Le drain de la douche est bouché, ça prendrait un plombier » se règle beaucoup plus vite.",
       note:"Attention : dans un logement loué, vous ne choisissez normalement <b>pas</b> le professionnel vous-même. Vous signalez le problème ; c'est la personne propriétaire qui décide et qui paie."},

      {t:'ana', h:"Ce qui distingue les quatre principaux",
       p:"Retenez-les par ce qu'ils touchent, pas par le nom du problème.",
       mots:[['Tout ce qui coule','le plombier'],['Tout ce qui est électrique','l\'électricien',true],['Tout ce qui est en bois','le menuisier'],['Le toit','le couvreur']],
       say:'le plombier, l\'électricien, le menuisier, le couvreur',
       note:"Cas limite utile : un <b>calorifère</b> qui ne chauffe plus est un problème <b>électrique</b>, pas de chauffage — c'est l'électricien qu'il faut."},

      {t:'texte', h:"Le masculin et le féminin",
       p:"La plupart de ces noms de métier ont deux formes : <em>un plombier / une plombière</em>, <em>un électricien / une électricienne</em>, <em>un menuisier / une menuisière</em>, <em>un serrurier / une serrurière</em>, <em>un installateur / une installatrice</em>, <em>un exterminateur / une exterminatrice</em>, <em>un couvreur / une couvreuse</em>.",
       note:"Deux exceptions à connaître : <b>peintre</b> et <b>concierge</b> ne changent pas de forme — seul le déterminant change : <em>le peintre / la peintre</em>, <em>le concierge / la concierge</em>."},

      {t:'labo', h:"Un problème, un métier",
       p:"Choisissez un problème et voyez qui appeler.",
       axes:[{id:'p', lbl:'Quel problème ?', opts:[['a','le drain est bouché'],['b','le disjoncteur retombe'],['c','la clé tourne dans le vide'],['d','il y a des souris'],['e','le plafond coule'],['f','la porte ne ferme plus']]}],
       out:{
         a:{w:['un','plombier'],       say:'un plombier',       n:'tout ce qui transporte de l\'eau'},
         b:{w:['un','électricien'],    say:'un électricien',    n:'panneau, prises, calorifères'},
         c:{w:['un','serrurier'],      say:'un serrurier',      n:'serrures, cylindres, clés'},
         d:{w:['une','exterminatrice'],say:'une exterminatrice',n:'souris, insectes, punaises'},
         e:{w:['un','couvreur'],       say:'un couvreur',       n:'la toiture, donc le dernier étage'},
         f:{w:['un','menuisier'],      say:'un menuisier',      n:'portes, cadres, armoires, planchers'},
       },
       note:"Une porte qui ne ferme plus est presque toujours du bois qui a gonflé avec l'humidité — d'où le menuisier, et non le serrurier."},

      {t:'ex', h:"Des phrases à réutiliser au téléphone",
       p:"Écoutez et répétez : ce sont des phrases complètes, prêtes à dire.",
       rows:[
         ["Je pense que ça prendrait un plombier.","proposer sans imposer"],
         ["Est-ce que vous pouvez faire venir un électricien ?","demander poliment"],
         ["Le problème vient de la toiture, il faudrait un couvreur.","situer la cause"],
         ["La serrure a été forcée, j'ai appelé un serrurier d'urgence.","cas urgent"],
         ["Il faudrait faire installer un ventilateur dans la salle de bain.","faire + infinitif"],
         ["Le concierge est passé, mais il ne peut pas régler ça lui-même.","préciser une étape déjà faite"],
       ]},

      {t:'piege', h:"Deux erreurs qui font perdre du temps",
       rows:[
         ["appeler soi-même un professionnel et envoyer la facture","prévenir d'abord la personne propriétaire",
          "Si vous engagez quelqu'un sans autorisation, la propriétaire n'est pas obligée de vous rembourser — sauf en cas d'urgence réelle où vous n'avez pas pu la joindre."],
         ["dire « il y a un problème de chauffage » pour un calorifère mort","dire « le disjoncteur du calorifère retombe »",
          "Le premier message fait venir n'importe qui ; le second fait venir un électricien avec les bons outils du premier coup."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le calorifère du salon ne chauffe plus. Qui faut-il ?", opts:["un plombier","un électricien"], ok:1,
          fb:"Au Québec, les calorifères des logements sont électriques : c'est un circuit, donc un électricien."},
         {q:"L'eau de pluie tache le plafond du dernier étage. Qui faut-il ?", opts:["un couvreur","un peintre"], ok:0,
          fb:"Le peintre viendra après, mais tant que la toiture n'est pas réparée, la tache reviendra."},
         {q:"Quelle forme est correcte ?", opts:["la peintre","la peintresse"], ok:0,
          fb:"« Peintre » ne change pas de forme : <em>le peintre / la peintre</em>."},
         {q:"Vous découvrez un dégât d'eau. Quelle est la première chose à faire ?", opts:["appeler un plombier vous-même","prévenir la personne propriétaire ou le concierge"], ok:1,
          fb:"Sauf urgence immédiate, on prévient d'abord : c'est elle ou lui qui mandate et qui paie."},
       ]},
    ]
  },

  t1trib: {
    eye:'Mini-leçon', tit:'Faire valoir ses droits comme locataire',
    blocs:[
      {t:'texte', h:"Trois marches, dans l'ordre",
       p:"Un problème de logement se règle presque toujours par étapes, et sauter une marche fait perdre du temps. <b>1)</b> On parle — un appel, une conversation dans l'entrée. <b>2)</b> On écrit — un courriel daté qui reprend ce qui a été dit. <b>3)</b> On dépose une demande au <b>Tribunal administratif du logement</b> si rien ne bouge.",
       note:"Neuf problèmes sur dix s'arrêtent à la marche 1. La marche 2 existe surtout pour protéger la marche 3."},

      {t:'ana', h:"Ce que contient un bon avis écrit",
       p:"Un courriel de trois lignes suffit, s'il contient ces quatre éléments.",
       mots:[['Le fait','le calorifère ne chauffe plus'],['Depuis quand','depuis le 4 novembre',true],['L\'effet','il fait 14 °C chez moi'],['La demande','faire venir un électricien']],
       say:'Le calorifère ne chauffe plus depuis le 4 novembre. Il fait quatorze degrés chez moi. Pourriez-vous faire venir un électricien ?',
       note:"C'est exactement la même structure qu'une plainte à l'oral : fait, effet, demande — avec une date en plus."},

      {t:'texte', h:"Pourquoi la date change tout",
       p:"Devant le tribunal, la question n'est presque jamais « le problème existe-t-il ? » mais « <b>depuis combien de temps la personne propriétaire le sait-elle ?</b> ». Un courriel envoyé le 4 novembre prouve qu'elle savait le 4 novembre. Un appel téléphonique ne prouve rien.",
       note:"Gardez aussi vos <b>photos avec la date</b>, et notez l'heure de chaque appel dans un carnet ou une note du téléphone. Ça prend trente secondes et ça vaut beaucoup plus tard."},

      {t:'labo', h:"Quelle marche pour quelle situation ?",
       p:"Choisissez une situation et voyez quelle étape est la bonne.",
       axes:[{id:'s', lbl:'Quelle situation ?', opts:[['a','le robinet goutte depuis hier'],['b','deux courriels sans réponse depuis un mois'],['c','le chauffage est mort, il fait 14 °C'],['d','la propriétaire refuse par écrit de réparer']]}],
       out:{
         a:{w:['On','téléphone.'],            say:'On téléphone.',                 n:'marche 1 — un simple appel suffit'},
         b:{w:['On','dépose','une demande.'], say:'On dépose une demande au tribunal.', n:'marche 3 — l\'écrit a déjà été fait'},
         c:{w:['On','appelle,','puis','on','écrit.'], say:'On appelle, puis on écrit.', n:'marches 1 et 2 le même jour — c\'est urgent'},
         d:{w:['On','dépose','une demande.'], say:'On dépose une demande au tribunal.', n:'marche 3 — le refus écrit est votre preuve'},
       },
       note:"Un refus écrit n'est pas une mauvaise nouvelle : c'est la meilleure preuve possible devant le tribunal."},

      {t:'ex', h:"Des phrases pour l'avis écrit",
       p:"Écoutez et réutilisez-les telles quelles dans un courriel.",
       rows:[
         ["Je vous écris pour faire suite à notre conversation téléphonique du 4 novembre.","rappeler l'appel"],
         ["Le problème dure depuis deux semaines et il s'aggrave.","situer dans le temps"],
         ["Vous trouverez une photo en pièce jointe.","joindre la preuve"],
         ["J'aimerais savoir quelle date est prévue pour la réparation.","demander clairement"],
         ["Merci de me confirmer la réception de ce message.","obtenir une trace de réception"],
       ]},

      {t:'piege', h:"Deux erreurs courantes",
       rows:[
         ["cesser de payer son loyer pour faire réagir","continuer à payer et déposer une demande",
          "Arrêter de payer ne fait pas pression : ça donne au contraire un motif d'expulsion. Le loyer se paie même quand la réparation traîne."],
         ["tout régler par appels téléphoniques","doubler chaque appel d'un courriel",
          "Un appel règle vite, mais ne laisse aucune trace. Le courriel de deux lignes envoyé après l'appel est ce qui protège en cas de désaccord."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Le Tribunal administratif du logement, c'est…", opts:["le premier endroit où s'adresser","un recours quand rien ne bouge"], ok:1,
          fb:"On parle d'abord, on écrit ensuite, et le tribunal vient en dernier."},
         {q:"Quelle preuve vaut le plus ?", opts:["un souvenir d'appel téléphonique","un courriel daté"], ok:1,
          fb:"Ce qui est écrit et daté peut être montré ; un appel ne laisse rien."},
         {q:"La réparation traîne. Puis-je arrêter de payer mon loyer ?", opts:["Non","Oui, jusqu'à la réparation"], ok:0,
          fb:"Non — cela donnerait un motif d'expulsion. Le loyer se paie, et on dépose une demande."},
         {q:"Faut-il un avocat pour se présenter au tribunal ?", opts:["Oui, c'est obligatoire","Non, on peut se représenter seul"], ok:1,
          fb:"La représentation par avocat n'est pas obligatoire ; beaucoup de gens s'y présentent seuls."},
       ]},
    ]
  },

  t1leur: {
    eye:'Mini-leçon', tit:'Leur ou leurs : ce qui décide vraiment',
    blocs:[
      {t:'texte', h:"L'erreur de départ à corriger",
       p:"Beaucoup d'élèves croient que <em>leurs</em> prend un <b>s</b> parce qu'il y a plusieurs propriétaires. C'est faux — et c'est justement ce qui cause l'erreur. Avec <em>leur</em>, les propriétaires sont <b>toujours</b> plusieurs (ils, elles) : le <b>s</b> ne peut donc pas servir à ça.",
       note:"Ce qui décide, c'est uniquement le <b>nom placé juste après</b> : un seul objet → <em>leur</em>, plusieurs objets → <em>leurs</em>."},

      {t:'ana', h:"Un seul objet possédé",
       p:"Les voisins du 3B sont plusieurs, mais ils n'ont qu'un seul balcon à eux tous.",
       mots:[['Plusieurs personnes','Les voisins'],['Déterminant','leur',true],['Un seul nom, singulier','balcon']],
       say:'Les voisins nettoient leur balcon.',
       note:"Test rapide : « Il nettoie <em>son</em> balcon » fonctionne au singulier → donc <b>leur</b> au pluriel."},

      {t:'ana', h:"Plusieurs objets possédés",
       p:"Cette fois, chaque famille a ses enfants : le nom qui suit est au pluriel.",
       mots:[['Plusieurs personnes','Les voisins'],['Déterminant','leurs',true],['Nom au pluriel','enfants']],
       say:'Les voisins surveillent leurs enfants.',
       note:"Test rapide : « Il surveille <em>ses</em> enfants » fonctionne → donc <b>leurs</b>."},

      {t:'texte', h:"Le test son / ses, en deux secondes",
       p:"Mettez mentalement la phrase au singulier, avec <b>une seule</b> personne propriétaire. Si vous dites <em>son</em> ou <em>sa</em> → écrivez <b>leur</b>. Si vous dites <em>ses</em> → écrivez <b>leurs</b>. Ce test ne se trompe jamais.",
       note:"Et rappelez-vous qu'il n'existe pas de forme « leure » : <em>leur</em> s'écrit pareil devant un nom masculin ou féminin — <em>leur</em> logement, <em>leur</em> porte."},

      {t:'labo', h:"Changez le nom, observez le déterminant",
       p:"Choisissez le nom possédé et le nombre.",
       axes:[
         {id:'n', lbl:'Quel nom ?', opts:[['a','logement'],['b','clé'],['c','plainte']]},
         {id:'q', lbl:'Combien ?', opts:[['1','un seul'],['2','plusieurs']]},
       ],
       out:{
         a1:{w:['Les locataires aiment','leur','logement.'],   say:'Les locataires aiment leur logement.',   n:'leur — nom singulier (son logement)'},
         a2:{w:['Les locataires aiment','leurs','logements.'], say:'Les locataires aiment leurs logements.', n:'leurs — nom pluriel (ses logements)'},
         b1:{w:['Ils ont perdu','leur','clé.'],                say:'Ils ont perdu leur clé.',                n:'leur — féminin singulier, pas de « leure »'},
         b2:{w:['Ils ont perdu','leurs','clés.'],              say:'Ils ont perdu leurs clés.',              n:'leurs — nom pluriel'},
         c1:{w:['Elles ont envoyé','leur','plainte.'],         say:'Elles ont envoyé leur plainte.',         n:'leur — une seule plainte commune'},
         c2:{w:['Elles ont envoyé','leurs','plaintes.'],       say:'Elles ont envoyé leurs plaintes.',       n:'leurs — chacune la sienne'},
       },
       note:"Regardez la paire « leur clé / leurs clés » : à l'oral, les deux se disent exactement pareil. Seul l'écrit fait la différence — sauf en cas de liaison."},

      {t:'texte', h:"La liaison, le seul indice à l'oral",
       p:"Devant une <b>voyelle</b> ou un <b>h muet</b>, le <b>s</b> de <em>leurs</em> se prononce [z] : <em>leurs_enfants</em>, <em>leurs_appareils</em>, <em>leurs_histoires</em>. C'est souvent la seule façon d'entendre qu'il y a plusieurs objets.",
       note:"Comparez à l'oreille : <em>leur ami</em> (un seul, pas de [z]) et <em>leurs_amis</em> (plusieurs, avec [z]). Cette petite consonne porte toute l'information."},

      {t:'ex', h:"Six phrases du module",
       p:"Écoutez et repérez, à chaque fois, le nom qui suit le déterminant.",
       rows:[
         ["Les locataires du deuxième ont fait refaire leur installation électrique.","leur + nom singulier"],
         ["Leurs enfants marchent dans la graisse du corridor.","leurs + nom pluriel, avec liaison"],
         ["Mes voisins laissent leurs vélos dans le corridor.","leurs + nom pluriel"],
         ["Camille et Samir ont signé leur bail au mois de juillet.","leur + un seul bail commun"],
         ["Les propriétaires doivent respecter leurs obligations.","leurs + nom pluriel"],
         ["Ces deux familles trouvent leur logement trop humide.","leur + un logement chacune, mais un seul nom singulier"],
       ]},

      {t:'piege', h:"Les trois pièges à connaître",
       rows:[
         ["Les voisins nettoient leurs balcon.","Les voisins nettoient leur balcon.",
          "Le <b>s</b> a été mis parce que « les voisins » est pluriel. Mais c'est le nom <em>balcon</em> qui décide, et il est singulier."],
         ["Je leurs ai téléphoné.","Je leur ai téléphoné.",
          "Ici, <em>leur</em> est un <b>pronom</b> (= à eux, à elles), pas un déterminant. Le pronom <em>leur</em> ne prend <b>jamais</b> de s. Repère : il est placé devant un verbe, pas devant un nom."],
         ["Elles ont perdu leure clé.","Elles ont perdu leur clé.",
          "La forme « leure » n'existe pas. <em>Leur</em> ne change pas au féminin."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Cinq questions rapides.",
       qs:[
         {q:"Les voisins rangent ___ vélos au sous-sol.", opts:["leur","leurs"], ok:1,
          fb:"« Il range <em>ses</em> vélos » → donc <b>leurs</b>."},
         {q:"Ces deux familles paient ___ loyer le premier du mois.", opts:["leur","leurs"], ok:0,
          fb:"« Il paie <em>son</em> loyer » → donc <b>leur</b>, même si les familles sont deux."},
         {q:"Je ___ ai envoyé un courriel hier.", opts:["leur","leurs"], ok:0,
          fb:"Ici <em>leur</em> est un pronom placé devant un verbe : jamais de s."},
         {q:"Qu'est-ce qui décide entre leur et leurs ?", opts:["le nombre de propriétaires","le nom qui suit"], ok:1,
          fb:"Toujours le nom qui suit. Les propriétaires sont de toute façon plusieurs."},
         {q:"Dans « leurs appareils », le s de leurs…", opts:["reste muet","se prononce [z]"], ok:1,
          fb:"« appareils » commence par une voyelle : il y a liaison, on entend <em>leurs_appareils</em>."},
       ]},
    ]
  },

  t1depuis: {
    eye:'Mini-leçon', tit:'Dire depuis quand un problème dure',
    blocs:[
      {t:'texte', h:"La question la plus posée au téléphone",
       p:"Dès que vous signalez un problème, la personne propriétaire va demander : « <b>depuis quand ?</b> ». Cette réponse décide souvent de l'urgence de l'intervention. Le français offre trois façons de la donner — et elles veulent dire exactement la même chose.",
       note:"Point commun essentiel : dans les trois cas, le verbe reste au <b>présent</b>, parce que la situation dure encore. <em>Le robinet coule depuis deux jours</em> — et il coule toujours en ce moment."},

      {t:'ana', h:"depuis + un nom ou une durée",
       p:"Après <em>depuis</em>, jamais de verbe conjugué : seulement un moment (hier, lundi, ce matin) ou une durée (deux jours, un mois).",
       mots:[['La situation','Le calorifère est froid'],['Marqueur','depuis',true],['Un nom ou une durée','avant-hier']],
       say:'Le calorifère est froid depuis avant-hier.',
       note:"Deux emplois dans un seul mot : <em>depuis lundi</em> donne le <b>point de départ</b>, <em>depuis deux jours</em> donne la <b>durée</b>."},

      {t:'ana', h:"depuis que + une phrase complète",
       p:"Le petit mot <em>que</em> change tout : il permet de mettre un sujet et un verbe conjugué après.",
       mots:[['La situation','La porte n\'ouvre plus'],['Marqueur','depuis que',true],['Sujet + verbe','vous avez ajouté un vélo']],
       say:'La porte n\'ouvre plus depuis que vous avez ajouté un vélo.',
       note:"<em>Depuis que</em> relie deux actions : la deuxième dure <b>depuis</b> que la première a eu lieu. C'est le marqueur qui explique une cause dans le temps."},

      {t:'ana', h:"ça fait… que + une phrase complète",
       p:"Même sens que <em>depuis</em>, mais la durée passe au début de la phrase, ce qui la met en valeur.",
       mots:[['Ça fait','Ça fait'],['La durée','deux semaines',true],['que + phrase','que la tache est là']],
       say:'Ça fait deux semaines que la tache est là.',
       note:"C'est la forme la plus fréquente à l'oral au Québec. Elle sert souvent à faire sentir que c'est long — donc à insister."},

      {t:'labo', h:"La même idée, trois formulations",
       p:"Choisissez un problème et une façon de le dire.",
       axes:[
         {id:'p', lbl:'Quel problème ?', opts:[['a','la tache au plafond'],['b','les plaintes des voisins']]},
         {id:'f', lbl:'Quelle formulation ?', opts:[['1','depuis'],['2','ça fait… que'],['3','depuis que']]},
       ],
       out:{
         a1:{w:['La tache est là','depuis','deux semaines.'],          say:'La tache est là depuis deux semaines.',          n:'depuis + durée'},
         a2:{w:['Ça fait','deux semaines','que la tache est là.'],     say:'Ça fait deux semaines que la tache est là.',     n:'la durée est mise en avant'},
         a3:{w:['La tache grossit','depuis qu\'','il a plu dimanche.'],say:'La tache grossit depuis qu\'il a plu dimanche.', n:'depuis que + phrase (une cause)'},
         b1:{w:['Les voisins se plaignent','depuis','un mois.'],       say:'Les voisins se plaignent depuis un mois.',       n:'depuis + durée'},
         b2:{w:['Ça fait','un mois','qu\'ils se plaignent.'],          say:'Ça fait un mois qu\'ils se plaignent.',          n:'que devient qu\' devant une voyelle'},
         b3:{w:['Ils se plaignent','depuis que','les vélos sont là.'], say:'Ils se plaignent depuis que les vélos sont là.', n:'depuis que + phrase (une cause)'},
       },
       note:"Comparez a1 et a2 : le contenu est identique, mais a2 insiste sur la longueur. C'est celle-là qu'on choisit quand on commence à trouver le temps long."},

      {t:'ex', h:"Des phrases prêtes à dire au téléphone",
       p:"Écoutez et repérez ce qui suit le marqueur : un nom, ou un sujet + verbe ?",
       rows:[
         ["Le calorifère ne chauffe plus depuis avant-hier.","depuis + moment"],
         ["Ça fait deux semaines que cette tache est au plafond.","ça fait… que + phrase"],
         ["La porte n'ouvre plus depuis qu'il a ajouté un vélo.","depuis que + phrase"],
         ["Les voisins se plaignent depuis un mois.","depuis + durée"],
         ["Ça fait trois heures qu'on attend le plombier.","ça fait… que + phrase"],
         ["L'escalier reste propre depuis que le concierge a posé un tapis.","depuis que + phrase"],
       ]},

      {t:'piege', h:"Trois pièges fréquents",
       rows:[
         ["J'ai habité ici depuis deux ans.","J'habite ici depuis deux ans.",
          "En français, une action qui dure encore reste au <b>présent</b> avec <em>depuis</em>. Le passé composé dirait que vous n'y habitez plus."],
         ["Ça fait deux semaines la tache est là.","Ça fait deux semaines que la tache est là.",
          "Le <b>que</b> est obligatoire : il relie la durée à la phrase qui suit. C'est l'oubli le plus fréquent."],
         ["Le robinet coule depuis que hier.","Le robinet coule depuis hier.",
          "<em>Hier</em> n'est pas une phrase, c'est un moment : il faut <b>depuis</b> tout seul. On n'ajoute <em>que</em> que devant un sujet + verbe."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Cinq questions rapides.",
       qs:[
         {q:"Le calorifère est froid ___ trois jours.", opts:["depuis","depuis que"], ok:0,
          fb:"« trois jours » est une durée, pas une phrase : <b>depuis</b> seul."},
         {q:"Tout va mieux ___ le concierge est arrivé.", opts:["depuis","depuis que"], ok:1,
          fb:"« le concierge est arrivé » est un sujet + verbe : il faut <b>depuis que</b>."},
         {q:"___ un mois que j'attends la réparation.", opts:["Depuis","Ça fait"], ok:1,
          fb:"Quand la durée ouvre la phrase et qu'il y a un <em>que</em>, c'est <b>ça fait… que</b>."},
         {q:"Quel temps de verbe emploie-t-on avec depuis ?", opts:["le présent","le passé composé"], ok:0,
          fb:"Le <b>présent</b>, parce que la situation dure encore au moment où on parle."},
         {q:"Quelle phrase est correcte ?", opts:["Ça fait deux jours il pleut.","Ça fait deux jours qu'il pleut."], ok:1,
          fb:"Le <em>que</em> (ici <em>qu'</em>) est obligatoire après la durée."},
       ]},
    ]
  },

  t2coop: {
    eye:'Mini-leçon', tit:"Trois façons d'habiter au Québec",
    blocs:[
      {t:'texte', h:"Pourquoi c'est utile de connaître la différence",
       p:"Quand on cherche un logement, on rencontre trois modèles très différents, et vos <b>droits, vos coûts et vos obligations</b> ne sont pas les mêmes dans les trois. Une coopérative n'est ni un logement privé, ni un HLM.",
       note:"Dans le module, l'immeuble d'Oksana est un immeuble <b>privé</b> : il appartient à madame Rioux, qui décide et qui paie les réparations."},

      {t:'ana', h:"Le logement locatif privé",
       p:"Le modèle le plus courant : une personne ou une compagnie possède l'immeuble et le loue.",
       mots:[['Qui décide','la personne propriétaire',true],['Qui paie les réparations','la personne propriétaire'],['Ce que fait le locataire','payer le loyer, signaler les problèmes']],
       say:'Dans un logement privé, la personne propriétaire décide et paie les réparations.',
       note:"C'est aussi le modèle où le loyer est le plus élevé, parce que le propriétaire cherche un rendement."},

      {t:'ana', h:"La coopérative d'habitation",
       p:"L'immeuble appartient collectivement à celles et ceux qui y habitent.",
       mots:[['Qui décide','les membres, par vote',true],['Qui paie','la coopérative, sans profit'],['Ce que fait le membre','payer, participer, siéger']],
       say:'Dans une coopérative, les membres décident ensemble et participent à l\'entretien.',
       note:"Chaque membre est à la fois <b>locataire</b> de son logement et <b>copropriétaire</b> de l'immeuble. Il y a plus de 1 000 coopératives au Québec depuis les années 1970."},

      {t:'texte', h:"Et le HLM ?",
       p:"Le <b>HLM</b> (habitation à loyer modique) est un logement social géré par un office public. Le loyer y est calculé selon le revenu — souvent 25 % du revenu du ménage — et l'accès se fait par une liste d'attente selon des critères précis.",
       note:"Résumé en une ligne : <b>privé</b> = le marché · <b>coopérative</b> = un groupe qui se gère lui-même · <b>HLM</b> = un programme public selon le revenu."},

      {t:'labo', h:"Qui règle le problème ?",
       p:"Choisissez un type d'immeuble et voyez à qui vous vous adressez.",
       axes:[{id:'t', lbl:'Quel type de logement ?', opts:[['a','logement privé'],['b','coopérative'],['c','HLM']]}],
       out:{
         a:{w:['On prévient','la propriétaire.'],       say:'On prévient la propriétaire.',       n:'elle décide et elle paie'},
         b:{w:['On prévient','le comité d\'entretien.'],say:'On prévient le comité d\'entretien.', n:'les membres s\'en occupent eux-mêmes'},
         c:{w:['On prévient','l\'office d\'habitation.'],say:'On prévient l\'office d\'habitation.', n:'un organisme public gère l\'immeuble'},
       },
       note:"Dans les trois cas, le réflexe reste le même : <b>signaler tôt, et garder une trace écrite</b>."},

      {t:'ex', h:"Le vocabulaire à retenir",
       p:"Écoutez chaque phrase et repérez le mot clé.",
       rows:[
         ["Les membres de la coopérative votent le budget des rénovations.","décider ensemble"],
         ["Le loyer d'une coopérative est souvent moins cher que sur le marché privé.","l'avantage"],
         ["Chaque membre participe au comité d'entretien.","la contrepartie"],
         ["Quand un membre part, la coopérative reste propriétaire du logement.","la différence avec un condo"],
         ["Dans un HLM, le loyer est calculé selon le revenu du ménage.","le logement social"],
       ]},

      {t:'piege', h:"Deux confusions fréquentes",
       rows:[
         ["croire qu'on achète son logement en coopérative","on devient membre, pas propriétaire d'un logement",
          "On n'achète pas un logement : on achète une <b>part sociale</b> de la coopérative. En partant, on récupère sa part, pas la valeur du logement."],
         ["confondre coopérative et HLM","la coopérative se gère elle-même ; le HLM est géré par un office public",
          "Les deux offrent des loyers plus bas, mais le fonctionnement n'a rien à voir : dans un cas les résidents décident, dans l'autre c'est un organisme public."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Quatre questions rapides.",
       qs:[
         {q:"Dans une coopérative, les membres sont…", opts:["seulement locataires","locataires et copropriétaires"], ok:1,
          fb:"Les deux à la fois : ils louent leur logement et possèdent collectivement l'immeuble."},
         {q:"Le loyer en coopérative est généralement…", opts:["plus bas que sur le marché privé","plus élevé"], ok:0,
          fb:"Plus bas, parce que la coopérative ne cherche pas à faire de profit."},
         {q:"Un membre qui quitte sa coopérative…", opts:["revend son logement","récupère sa part sociale"], ok:1,
          fb:"La coopérative reste propriétaire du logement ; le membre récupère seulement sa part."},
         {q:"Dans un HLM, le loyer est calculé…", opts:["selon le revenu du ménage","selon la grandeur du logement"], ok:0,
          fb:"C'est un logement social : le loyer suit le revenu, souvent autour de 25 %."},
       ]},
    ]
  },

  t2avant: {
    eye:'Mini-leçon', tit:'Avant de, après avoir : mettre les actions en ordre',
    blocs:[
      {t:'texte', h:"Deux actions, une seule phrase",
       p:"Quand vous racontez ce que vous avez fait — au téléphone, dans un courriel, devant le tribunal — vous devez souvent placer <b>deux actions dans l'ordre</b>. <em>Avant de</em> et <em>après</em> servent exactement à ça, et ils fonctionnent en miroir l'un de l'autre.",
       note:"Le piège est là : ce qui suit <em>avant de</em> arrive en <b>deuxième</b>, et ce qui suit <em>après</em> arrive en <b>premier</b>. C'est l'inverse de l'ordre de lecture."},

      {t:'ana', h:"avant de + infinitif présent",
       p:"L'action introduite par <em>avant de</em> n'a pas encore eu lieu : c'est la deuxième.",
       mots:[['1re action','Je vérifie le panneau'],['Marqueur','avant d\'',true],['2e action (infinitif)','appeler la propriétaire']],
       say:'Je vérifie le panneau avant d\'appeler la propriétaire.',
       note:"<em>Avant de</em> devient <em>avant d'</em> devant une voyelle ou un h muet : <em>avant d'appeler</em>, <em>avant d'utiliser</em>, <em>avant d'habiter</em>."},

      {t:'ana', h:"après + infinitif passé",
       p:"L'action introduite par <em>après</em> est déjà terminée : c'est la première.",
       mots:[['1re action (infinitif passé)','Après avoir descendu les vélos,'],['2e action','vous lavez le plancher',true]],
       say:'Après avoir descendu les vélos, vous lavez le plancher.',
       note:"On ne dit jamais « après descendre » : après <em>après</em>, le verbe est obligatoirement à l'<b>infinitif passé</b>."},

      {t:'texte', h:"Comment fabriquer un infinitif passé",
       p:"C'est une formule simple en deux morceaux : <b>avoir</b> ou <b>être</b> à l'infinitif, puis le <b>participe passé</b> du verbe.<br>→ avec <b>avoir</b>, la grande majorité : <em>avoir lavé</em>, <em>avoir vu</em>, <em>avoir pris</em>, <em>avoir fini</em>, <em>avoir écrit</em>.<br>→ avec <b>être</b>, les verbes de déplacement (aller, venir, monter, descendre, entrer, sortir, rentrer, partir, arriver, rester, tomber) et tous les verbes pronominaux : <em>être monté</em>, <em>être rentré</em>, <em>s'être levé</em>.",
       note:"Les terminaisons du participe passé à connaître : <b>-é</b> (parlé, tombé) · <b>-t</b> (fait, écrit) · <b>-u</b> (reçu, vendu, vu) · <b>-i</b> (fini, réussi) · <b>-s</b> (mis, pris)."},

      {t:'texte', h:"L'accord : la seule vraie difficulté",
       p:"Avec <b>être</b>, le participe passé s'accorde avec le sujet : <em>après être monté</em> (lui), <em>après être montée</em> (elle), <em>après être montés</em> (eux), <em>après être montées</em> (elles). Avec <b>avoir</b>, aucun accord avec le sujet : <em>après avoir monté</em> ne change jamais.",
       note:"Truc de mémoire : <b>être</b> regarde le sujet, <b>avoir</b> ne le regarde pas."},

      {t:'labo', h:"Retournez la phrase",
       p:"Choisissez la paire d'actions et le marqueur.",
       axes:[
         {id:'a', lbl:'Quelles actions ?', opts:[['a','vérifier / appeler'],['b','descendre les vélos / laver']]},
         {id:'m', lbl:'Quel marqueur ?', opts:[['1','avant de'],['2','après']]},
       ],
       out:{
         a1:{w:['Je vérifie le panneau','avant d\'','appeler la propriétaire.'],
             say:'Je vérifie le panneau avant d\'appeler la propriétaire.', n:'1) vérifier  2) appeler'},
         a2:{w:['Après avoir','vérifié le panneau,','j\'appelle la propriétaire.'],
             say:'Après avoir vérifié le panneau, j\'appelle la propriétaire.', n:'même ordre, formulation inversée'},
         b1:{w:['Je lave le plancher','avant de','descendre les vélos.'],
             say:'Je lave le plancher avant de descendre les vélos.', n:'1) laver  2) descendre'},
         b2:{w:['Après avoir','descendu les vélos,','je lave le plancher.'],
             say:'Après avoir descendu les vélos, je lave le plancher.', n:'1) descendre  2) laver — l\'ordre change !'},
       },
       note:"Comparez b1 et b2 : les mêmes mots, mais l'ordre réel des actions s'inverse. C'est exactement ce que Samir demande à Jean-Philippe — d'abord descendre, ensuite laver."},

      {t:'ex', h:"Six phrases du module",
       p:"Pour chacune, demandez-vous : quelle action vient en premier ?",
       rows:[
         ["Oksana prend une photo avant d'envoyer son courriel.","1) la photo  2) le courriel"],
         ["Après avoir terminé leur installation, l'électricien montera au quatrième.","1) terminer  2) monter"],
         ["Il faut couper le courant avant de toucher au panneau.","1) couper  2) toucher"],
         ["Après avoir descendu ses vélos, Jean-Philippe a lavé le plancher.","1) descendre  2) laver"],
         ["Après être monté au troisième, Samir a constaté le désordre.","être + accord avec le sujet"],
         ["Lisez bien votre bail avant de le signer.","1) lire  2) signer"],
       ]},

      {t:'piege', h:"Trois pièges à éviter",
       rows:[
         ["Après descendre les vélos, je lave le plancher.","Après avoir descendu les vélos, je lave le plancher.",
          "Après <em>après</em>, on ne met jamais un infinitif présent seul : il faut l'infinitif passé, donc <b>avoir</b> ou <b>être</b> + participe passé."],
         ["Avant d'appeler la propriétaire, elle a vérifié le panneau.","Avant d'appeler la propriétaire, j'ai vérifié le panneau.",
          "Les deux actions doivent avoir le <b>même sujet</b>. Si les sujets diffèrent, on abandonne l'infinitif : <em>avant que la propriétaire appelle…</em>"],
         ["Après être monté, Camille a ouvert la porte.","Après être montée, Camille a ouvert la porte.",
          "Avec <b>être</b>, le participe s'accorde avec le sujet. Camille est une femme : <em>montée</em>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Cinq questions rapides.",
       qs:[
         {q:"« Avant de signer, lisez votre bail. » Quelle action vient en premier ?", opts:["signer","lire"], ok:1,
          fb:"Ce qui suit <em>avant de</em> arrive en deuxième : on lit d'abord, on signe ensuite."},
         {q:"« Après avoir payé, il a reçu un reçu. » Quelle action vient en premier ?", opts:["payer","recevoir"], ok:0,
          fb:"Ce qui suit <em>après</em> arrive en premier : il paie, puis il reçoit."},
         {q:"Quelle forme est correcte ?", opts:["après avoir fini","après finir"], ok:0,
          fb:"Après <em>après</em>, il faut l'infinitif passé : <b>avoir fini</b>."},
         {q:"Elle est rentrée chez elle, puis elle a soupé. On dit…", opts:["Après être rentrée chez elle, elle a soupé.","Après avoir rentrée chez elle, elle a soupé."], ok:0,
          fb:"<em>Rentrer</em> se conjugue avec <b>être</b>, et le participe s'accorde : <em>rentrée</em>."},
         {q:"« Avant d' » s'emploie devant…", opts:["une voyelle ou un h muet","une consonne"], ok:0,
          fb:"<em>Avant de</em> → <em>avant d'</em> devant une voyelle : <em>avant d'appeler</em>."},
       ]},
    ]
  },

  t2faire: {
    eye:'Mini-leçon', tit:'Faire réparer : quand on ne répare pas soi-même',
    blocs:[
      {t:'texte', h:"La construction du locataire",
       p:"Dans un logement loué, vous ne réparez presque rien vous-même — et c'est normal, c'est même souvent interdit par le bail. Le français a une construction faite exactement pour ça : <b>faire + un verbe à l'infinitif</b>. Elle dit que le sujet <b>fait faire</b> l'action par quelqu'un d'autre.",
       note:"Comparez : <em>Je répare la serrure</em> (avec mes outils) et <em>Je fais réparer la serrure</em> (quelqu'un vient la réparer). Dans un logement, c'est presque toujours la deuxième."},

      {t:'ana', h:"faire + infinitif",
       p:"Les deux verbes se suivent directement, sans aucun mot entre eux.",
       mots:[['Sujet','La propriétaire'],['faire, conjugué','fait',true],['Verbe à l\'infinitif','venir un électricien']],
       say:'La propriétaire fait venir un électricien.',
       note:"Le sujet <em>la propriétaire</em> ne vient pas elle-même : elle organise la venue. C'est toute la nuance de la construction."},

      {t:'ana', h:"faire + infinitif + par",
       p:"Quand on veut nommer la personne qui exécute réellement le travail, on l'introduit avec <b>par</b>.",
       mots:[['Sujet','Je'],['faire + infinitif','fais nettoyer'],['Quoi','le corridor'],['Qui exécute','par la compagnie d\'entretien',true]],
       say:'Je fais nettoyer le corridor par la compagnie d\'entretien.',
       note:"Sans <em>par</em>, la phrase reste correcte — on ne dit simplement pas qui fait le travail. C'est utile quand on ne le sait pas encore."},

      {t:'texte', h:"Le verbe faire au présent",
       p:"je <b>fais</b> · tu <b>fais</b> · il / elle <b>fait</b> · nous <b>faisons</b> · vous <b>faites</b> · ils / elles <b>font</b>",
       note:"Deux pièges de prononciation et d'orthographe : <em>nous faisons</em> se dit [fə-zɔ̃] (le <b>ai</b> ne se prononce pas [ɛ]), et <em>vous faites</em> ne prend <b>pas</b> de -ez, contrairement à presque tous les autres verbes."},

      {t:'labo', h:"Changez le sujet, changez le métier",
       p:"Choisissez qui parle et quel travail est demandé.",
       axes:[
         {id:'s', lbl:'Qui parle ?', opts:[['a','je'],['b','nous'],['c','la propriétaire']]},
         {id:'t', lbl:'Quel travail ?', opts:[['1','réparer le calorifère'],['2','installer un ventilateur']]},
       ],
       out:{
         a1:{w:['Je','fais','réparer le calorifère','par un électricien.'],
             say:'Je fais réparer le calorifère par un électricien.', n:'je fais'},
         a2:{w:['Je','fais','installer un ventilateur','par un installateur.'],
             say:'Je fais installer un ventilateur par un installateur.', n:'je fais'},
         b1:{w:['Nous','faisons','réparer le calorifère','par un électricien.'],
             say:'Nous faisons réparer le calorifère par un électricien.', n:'nous faisons — se dit [fə-zɔ̃]'},
         b2:{w:['Nous','faisons','installer un ventilateur','par un installateur.'],
             say:'Nous faisons installer un ventilateur par un installateur.', n:'nous faisons'},
         c1:{w:['La propriétaire','fait','réparer le calorifère','par un électricien.'],
             say:'La propriétaire fait réparer le calorifère par un électricien.', n:'il / elle fait'},
         c2:{w:['La propriétaire','fait','installer un ventilateur','par un installateur.'],
             say:'La propriétaire fait installer un ventilateur par un installateur.', n:'il / elle fait'},
       },
       note:"Remarquez que <b>seul le verbe faire change</b>. Le deuxième verbe reste à l'infinitif dans tous les cas — il ne se conjugue jamais."},

      {t:'ex', h:"Six phrases à réutiliser",
       p:"Écoutez et repérez les deux verbes : le premier conjugué, le second à l'infinitif.",
       rows:[
         ["La propriétaire fait venir un électricien jeudi matin.","faire + infinitif"],
         ["Nous faisons installer un ventilateur dans la salle de bain.","nous faisons"],
         ["Vous faites réparer votre toiture par un couvreur.","vous faites + par"],
         ["Les locataires du deuxième font changer leurs fenêtres.","ils font"],
         ["Je fais nettoyer le corridor par la compagnie d'entretien.","je fais + par"],
         ["Mon voisin fait faire des travaux dans son appartement.","faire faire — c'est correct"],
       ]},

      {t:'piege', h:"Trois pièges fréquents",
       rows:[
         ["Je fais à réparer la serrure.","Je fais réparer la serrure.",
          "Rien ne se place entre <em>faire</em> et l'infinitif : ni <b>à</b>, ni <b>de</b>. Les deux verbes se touchent."],
         ["Je fais réparer la serrure pour le concierge.","Je fais réparer la serrure par le concierge.",
          "<em>Pour</em> dirait que la réparation est un service rendu au concierge. C'est <b>par</b> qui indique qui exécute le travail."],
         ["Vous faisez venir un plombier.","Vous faites venir un plombier.",
          "<em>Faire</em> est irrégulier : <b>vous faites</b>, sans -ez. C'est l'une des trois seules formes de ce type en français, avec <em>vous dites</em> et <em>vous êtes</em>."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Cinq questions rapides.",
       qs:[
         {q:"« La propriétaire fait réparer le toit. » Qui monte sur le toit ?", opts:["la propriétaire","un couvreur"], ok:1,
          fb:"Avec <em>faire + infinitif</em>, le sujet organise mais n'exécute pas."},
         {q:"Complétez : « Nous ___ installer un ventilateur. »", opts:["faisons","faisez"], ok:0,
          fb:"<b>Nous faisons</b> — et attention, ça se prononce [fə-zɔ̃]."},
         {q:"Quelle phrase est correcte ?", opts:["Je fais de réparer la porte.","Je fais réparer la porte."], ok:1,
          fb:"Aucun mot entre <em>faire</em> et l'infinitif."},
         {q:"Pour dire qui exécute le travail, on emploie…", opts:["par","pour"], ok:0,
          fb:"<em>par</em> : « faire nettoyer le corridor <b>par</b> la compagnie »."},
         {q:"Complétez : « Vous ___ changer la serrure. »", opts:["faisez","faites"], ok:1,
          fb:"<b>Vous faites</b>, sans -ez : c'est une forme irrégulière à mémoriser."},
       ]},
    ]
  },

  t3plainte: {
    eye:'Mini-leçon', tit:'Se plaindre efficacement, sans se fâcher',
    blocs:[
      {t:'texte', h:"Décrire, ce n'est pas encore se plaindre",
       p:"« Le bac de recyclage déborde tous les mardis » est une <b>description</b> : ça dit ce qui se passe, et l'autre personne peut très bien répondre « ah oui, en effet » sans rien faire. « Je ne peux plus tolérer que le bac déborde ; pourriez-vous demander une collecte de plus ? » est une <b>plainte</b> : elle contient un jugement et une demande.",
       note:"Une plainte qui n'aboutit pas est très souvent une plainte à laquelle il manquait simplement la <b>demande</b> finale."},

      {t:'ana', h:"La formule en trois temps",
       p:"Presque toutes les plaintes efficaces suivent ce schéma. Retenez-le, il fonctionne à l'oral comme à l'écrit.",
       mots:[['1. Le fait','La musique joue jusqu\'à deux heures.'],['2. L\'effet sur moi','Je commence à sept heures et je ne dors plus.',true],['3. La demande','Pourriez-vous leur en parler ?']],
       say:'La musique joue jusqu\'à deux heures. Je commence à sept heures et je ne dors plus. Pourriez-vous leur en parler ?',
       note:"Le temps 2 est celui qu'on oublie le plus, et c'est pourtant celui qui donne envie d'agir : il transforme un détail en problème réel pour quelqu'un."},

      {t:'texte', h:"Les mots pour dire que ça ne va pas",
       p:"<b>La situation dérange :</b> Cette situation est <em>dérangeante</em>. · C'est très <em>difficile</em> de… · C'est vraiment <em>injuste</em>. · C'est <em>décevant</em>.<br><b>Je dis mon émotion :</b> Je suis <em>irritée</em> par… · Je suis <em>fâché</em> de… · Je suis <em>contrariée</em> par… · Je suis <em>fatigué</em> de… · Je suis très <em>déçue</em>.<br><b>Je suis au bout :</b> Je ne peux plus <em>tolérer</em>… · Je ne peux plus <em>accepter</em> cette situation. · Cette situation doit <em>se terminer</em>. · C'est <em>inacceptable</em>. · C'est <em>inapproprié</em>.",
       note:"Ces expressions montent en intensité. Commencez par le bas de l'échelle : on garde <em>inacceptable</em> pour la deuxième ou la troisième fois, pas pour le premier appel."},

      {t:'labo', h:"Montez l'intensité",
       p:"Choisissez le problème et le degré de fermeté.",
       axes:[
         {id:'p', lbl:'Quel problème ?', opts:[['a','le bruit la nuit'],['b','le corridor encombré']]},
         {id:'d', lbl:'Quel degré ?', opts:[['1','1er contact, doux'],['2','2e fois, ferme'],['3','3e fois, très ferme']]},
       ],
       out:{
         a1:{w:['C\'est un peu dérangeant,','mais je préfère vous en parler.'],
             say:'C\'est un peu dérangeant, mais je préfère vous en parler.', n:'on ouvre la porte'},
         a2:{w:['Je suis fatiguée','de ne pas dormir la semaine.'],
             say:'Je suis fatiguée de ne pas dormir la semaine.', n:'on nomme l\'effet sur soi'},
         a3:{w:['Je ne peux plus tolérer ce bruit :','c\'est inacceptable.'],
             say:'Je ne peux plus tolérer ce bruit : c\'est inacceptable.', n:'dernier avertissement avant l\'écrit'},
         b1:{w:['Le corridor est un peu encombré','ces temps-ci.'],
             say:'Le corridor est un peu encombré ces temps-ci.', n:'on signale, sans accuser'},
         b2:{w:['C\'est difficile de passer','avec une poussette.'],
             say:'C\'est difficile de passer avec une poussette.', n:'on montre la conséquence concrète'},
         b3:{w:['Cette situation est inappropriée :','c\'est une sortie de secours.'],
             say:'Cette situation est inappropriée : c\'est une sortie de secours.', n:'on invoque la sécurité'},
       },
       note:"Observez que même au degré 3, on parle de la <b>situation</b> et jamais de la personne. C'est ce qui garde la conversation possible."},

      {t:'ex', h:"Des phrases prêtes à dire",
       p:"Écoutez et répétez avec un ton ferme, mais calme.",
       rows:[
         ["Je vous appelle parce que cette situation est vraiment dérangeante.","ouvrir"],
         ["Ça fait cinq semaines que ça dure et je ne peux plus le tolérer.","durée + limite"],
         ["Je suis fatiguée de devoir laisser mon auto dans la rue.","effet sur moi"],
         ["Ce n'est pas contre vous, mais il faut que ça change.","garder la relation"],
         ["J'aimerais savoir ce que vous comptez faire cette semaine.","demande claire"],
         ["Est-ce que vous pourriez faire installer une affiche à l'entrée ?","demande précise et polie"],
       ]},

      {t:'piege', h:"Trois façons d'affaiblir sa propre plainte",
       rows:[
         ["Je m'excuse de vous déranger, ce n'est peut-être rien…","Je vous appelle au sujet du bruit du vendredi soir.",
          "Trop d'excuses annonce que le problème n'est pas important. On peut être poli sans s'effacer."],
         ["Vous êtes vraiment désordonné.","Le corridor est encombré depuis un mois.",
          "Attaquer la personne fait fermer la porte. On se plaint d'une <b>situation</b>, jamais de quelqu'un."],
         ["Il faudrait faire quelque chose.","Pourriez-vous faire installer une affiche avant vendredi ?",
          "Sans demande précise ni délai, l'autre personne ne sait pas ce qu'on attend — et rien ne bouge."],
       ]},

      {t:'check', h:"Est-ce que c'est clair maintenant ?",
       p:"Cinq questions rapides.",
       qs:[
         {q:"« Le bac déborde tous les mardis. » Cette phrase…", opts:["se plaint","décrit"], ok:1,
          fb:"Elle décrit un fait, sans jugement ni demande."},
         {q:"« Je ne peux plus tolérer cette situation. » Cette phrase…", opts:["se plaint","décrit"], ok:0,
          fb:"« Je ne peux plus tolérer » exprime clairement le mécontentement."},
         {q:"Quel élément manque le plus souvent dans une plainte ?", opts:["la demande","le fait"], ok:0,
          fb:"On décrit et on s'indigne, mais on oublie de dire ce qu'on veut. Sans demande, rien ne bouge."},
         {q:"Quelle formulation passe le mieux ?", opts:["Vous êtes désordonné.","Le corridor est encombré."], ok:1,
          fb:"On vise la situation, pas la personne : la conversation reste possible."},
         {q:"Au premier appel, on emploie plutôt…", opts:["C'est inacceptable !","C'est dérangeant, je préfère vous en parler."], ok:1,
          fb:"On garde les expressions fortes pour plus tard, si rien ne change."},
       ]},
    ]
  },
};
