# -*- coding: utf-8 -*-
"""Guide de Montréal — circuits, fiches pratiques et mots d'ici.

Voir FORMAT.md pour les règles d'écriture (ton, langues, faits prudents, aucun emoji).
"""

# ---------------------------------------------------------------------------
# 1. CIRCUITS — itinéraires à pied, ou à pied et en métro
# ---------------------------------------------------------------------------

CIRCUITS = [
    {
        "id": "vieux-montreal",
        "nom": {
            "fr": "Le Vieux-Montréal à pied",
            "en": "Old Montréal on Foot",
            "es": "El Viejo Montreal a pie",
        },
        "duree": {
            "fr": "une demi-journée",
            "en": "half a day",
            "es": "medio día",
        },
        "intro": {
            "fr": "La ville est née ici, au bord du fleuve, et ses rues de pierre racontent quatre siècles d'histoire en quelques pas. Vous commencez là où Montréal a été fondée, vous passez par la basilique et la place la plus animée du quartier, puis vous descendez au Vieux-Port. Pour finir, une courte montée vers le quartier chinois, où le dîner vous attend.",
            "en": "This is where the city was born, on the riverbank, and its stone streets pack four centuries of history into a short stroll. You start where Montréal was founded, take in the basilica and the liveliest square in the district, then wander down to the Old Port. To finish, a short walk uphill to Chinatown, where lunch is waiting.",
            "es": "Aquí nació la ciudad, a orillas del río, y sus calles de piedra condensan cuatro siglos de historia en pocos pasos. Usted empieza donde se fundó Montreal, pasa por la basílica y la plaza más animada del barrio, y luego baja al Viejo Puerto. Para terminar, una breve subida hasta el barrio chino, donde lo espera el almuerzo.",
        },
        "etapes": [
            "pointe-a-calliere",
            "notre-dame",
            "place-jacques-cartier",
            "vieux-port",
            "quartier-chinois",
        ],
        "liaisons": {
            "fr": [
                "Environ 7 minutes à pied en remontant la rue Saint-Sulpice jusqu'à la place d'Armes.",
                "Environ 8 minutes à pied vers l'est par la rue Notre-Dame, en passant devant l'hôtel de ville.",
                "Quelques minutes à pied en descendant la place jusqu'à la rue de la Commune et aux quais.",
                "Environ 15 minutes à pied vers le nord par le boulevard Saint-Laurent, ou le métro, ligne orange, de Champ-de-Mars à Place-d'Armes, une station plus loin.",
            ],
            "en": [
                "About 7 minutes on foot up rue Saint-Sulpice to Place d'Armes.",
                "About 8 minutes east along rue Notre-Dame, past City Hall.",
                "A few minutes downhill through the square to rue de la Commune and the quays.",
                "About 15 minutes north on foot along boulevard Saint-Laurent, or take the orange line one stop, from Champ-de-Mars to Place-d'Armes.",
            ],
            "es": [
                "Unos 7 minutos a pie subiendo por la calle Saint-Sulpice hasta la Place d'Armes.",
                "Unos 8 minutos a pie hacia el este por la calle Notre-Dame, pasando frente al ayuntamiento.",
                "Pocos minutos a pie bajando por la plaza hasta la calle de la Commune y los muelles.",
                "Unos 15 minutos a pie hacia el norte por el bulevar Saint-Laurent, o una estación en la línea naranja del metro, de Champ-de-Mars a Place-d'Armes.",
            ],
        },
    },
    {
        "id": "plateau-mile-end",
        "nom": {
            "fr": "Le Plateau et le Mile End gourmands",
            "en": "A Food Lover's Plateau and Mile End",
            "es": "El Plateau y el Mile End para golosos",
        },
        "duree": {
            "fr": "une journée, sans se presser",
            "en": "a full day, at an easy pace",
            "es": "un día completo, sin prisa",
        },
        "intro": {
            "fr": "Voici le circuit des classiques qu'on mange debout, au comptoir ou sur un banc : smoked meat, poutine, poulet portugais, bagels sortis du four à bois. Entre deux bouchées, vous marchez dans les rues aux escaliers extérieurs qui font la réputation du Plateau. Partagez les assiettes : la liste est longue et chaque arrêt mérite qu'on garde un peu de place.",
            "en": "This is the tour of the classics you eat standing up, at a counter or on a park bench: smoked meat, poutine, Portuguese chicken, bagels straight from the wood oven. Between bites, you walk the streets of outdoor staircases that made the Plateau famous. Share your plates: the list is long, and every stop deserves a little room.",
            "es": "Este es el recorrido de los clásicos que se comen de pie, en la barra o en un banco: smoked meat, poutine, pollo portugués, bagels recién salidos del horno de leña. Entre bocado y bocado, usted camina por las calles de escaleras exteriores que dieron fama al Plateau. Comparta los platos: la lista es larga y cada parada merece que le guarde un poco de espacio.",
        },
        "etapes": [
            "schwartz",
            "plateau",
            "la-banquise",
            "romados",
            "mile-end",
            "wilenskys",
            "bagels",
            "cafe-olimpico",
        ],
        "liaisons": {
            "fr": [
                "Environ 10 minutes à pied vers l'est par la rue Duluth, jusqu'à la rue Saint-Denis.",
                "Environ 10 minutes à pied par la rue Rachel, vers le parc La Fontaine.",
                "Environ 20 minutes à pied vers l'ouest par la rue Rachel, presque jusqu'au boulevard Saint-Laurent.",
                "Environ 20 minutes à pied vers le nord par le boulevard Saint-Laurent, ou l'autobus 55.",
                "Quelques minutes à pied jusqu'au coin des rues Fairmount et Clark.",
                "Deux minutes à pied vers l'ouest par la rue Fairmount, ou cinq de plus jusqu'à la rue Saint-Viateur.",
                "Quelques minutes à pied par la rue Saint-Viateur.",
            ],
            "en": [
                "About 10 minutes east on foot along rue Duluth to rue Saint-Denis.",
                "About 10 minutes on foot along rue Rachel toward La Fontaine Park.",
                "About 20 minutes west on foot along rue Rachel, almost to boulevard Saint-Laurent.",
                "About 20 minutes north on foot up boulevard Saint-Laurent, or take the 55 bus.",
                "A few minutes on foot to the corner of Fairmount and Clark.",
                "Two minutes west along rue Fairmount, or five more to rue Saint-Viateur.",
                "A few minutes on foot along rue Saint-Viateur.",
            ],
            "es": [
                "Unos 10 minutos a pie hacia el este por la calle Duluth, hasta la calle Saint-Denis.",
                "Unos 10 minutos a pie por la calle Rachel, hacia el parque La Fontaine.",
                "Unos 20 minutos a pie hacia el oeste por la calle Rachel, casi hasta el bulevar Saint-Laurent.",
                "Unos 20 minutos a pie hacia el norte por el bulevar Saint-Laurent, o el autobús 55.",
                "Pocos minutos a pie hasta la esquina de las calles Fairmount y Clark.",
                "Dos minutos a pie hacia el oeste por la calle Fairmount, o cinco más hasta la calle Saint-Viateur.",
                "Pocos minutos a pie por la calle Saint-Viateur.",
            ],
        },
    },
    {
        "id": "la-montagne",
        "nom": {
            "fr": "La montagne",
            "en": "The Mountain",
            "es": "La montaña",
        },
        "duree": {
            "fr": "une demi-journée",
            "en": "half a day",
            "es": "medio día",
        },
        "intro": {
            "fr": "Les Montréalais disent « la montagne » pour parler du mont Royal, et c'est elle qui donne son nom à la ville. Vous partez de l'Oratoire, le plus haut point de Montréal, vous traversez le parc jusqu'au belvédère qui domine le centre-ville, puis vous descendez à pied vers le musée des beaux-arts. Prévoyez de bonnes chaussures : ça monte, puis ça descend.",
            "en": "Montrealers simply say \"the mountain\" when they mean Mount Royal, the hill that gave the city its name. You start at the Oratory, the highest point in Montréal, cross the park to the lookout above downtown, then walk down to the Museum of Fine Arts. Wear good shoes: it climbs, then it drops.",
            "es": "Los montrealeses dicen simplemente «la montaña» para hablar del monte Royal, la colina que dio su nombre a la ciudad. Usted sale del Oratorio, el punto más alto de Montreal, cruza el parque hasta el mirador que domina el centro y luego baja a pie hacia el Museo de Bellas Artes. Lleve buen calzado: primero se sube y después se baja.",
        },
        "etapes": [
            "oratoire",
            "mont-royal",
            "mbam",
        ],
        "liaisons": {
            "fr": [
                "Une quinzaine de minutes à pied jusqu'au chemin Remembrance, puis l'autobus 11 jusqu'au lac aux Castors ; le chalet et le belvédère sont ensuite à une quinzaine de minutes de marche.",
                "Environ 30 minutes à pied : l'escalier qui part du chalet descend vers l'avenue des Pins, puis la rue Peel mène à la rue Sherbrooke.",
            ],
            "en": [
                "About fifteen minutes on foot to chemin Remembrance, then the 11 bus to Beaver Lake; the chalet and the lookout are about fifteen minutes' walk from there.",
                "About 30 minutes on foot: the staircase below the chalet leads down to avenue des Pins, then rue Peel takes you to rue Sherbrooke.",
            ],
            "es": [
                "Unos quince minutos a pie hasta el camino Remembrance y luego el autobús 11 hasta el lago de los Castores; el chalet y el mirador quedan a unos quince minutos de caminata.",
                "Unos 30 minutos a pie: la escalera que baja del chalet lleva a la avenida des Pins, y luego la calle Peel lo conduce hasta la calle Sherbrooke.",
            ],
        },
    },
    {
        "id": "est-et-fleuve",
        "nom": {
            "fr": "De l'Olympique au fleuve",
            "en": "From the Olympic Park to the River",
            "es": "Del Parque Olímpico al río",
        },
        "duree": {
            "fr": "une journée",
            "en": "a full day",
            "es": "un día completo",
        },
        "intro": {
            "fr": "Ce circuit relie les grands gestes de Montréal : le stade des Jeux de 1976, l'un des plus grands jardins botaniques du monde, puis les deux icônes de l'Expo 67 posées au bord du fleuve. Le métro fait le gros du trajet, et la fin se fait à pied, sur un pont, avec la ville en face de vous. Gardez cette journée pour le beau temps.",
            "en": "This tour links Montréal's grandest gestures: the stadium of the 1976 Games, one of the largest botanical gardens in the world, then the two icons of Expo 67 standing by the river. The metro does most of the travelling, and the last stretch is on foot, across a bridge, with the skyline in front of you. Save this one for a fine day.",
            "es": "Este recorrido une los grandes gestos de Montreal: el estadio de los Juegos de 1976, uno de los jardines botánicos más grandes del mundo y luego los dos íconos de la Expo 67 a orillas del río. El metro hace la mayor parte del trayecto, y el final se hace a pie, sobre un puente, con la ciudad enfrente. Reserve este día para el buen tiempo.",
        },
        "etapes": [
            "parc-olympique",
            "jardin-botanique",
            "biosphere",
            "habitat-67",
        ],
        "liaisons": {
            "fr": [
                "Environ 10 minutes à pied en traversant la rue Sherbrooke, vers le nord.",
                "Environ 35 minutes en métro : ligne verte depuis Pie-IX jusqu'à Berri-UQAM, puis ligne jaune jusqu'à Jean-Drapeau ; la Biosphère est à quelques minutes de la station.",
                "Environ 40 minutes à pied ou 15 minutes à vélo par le pont de la Concorde, jusqu'à la Cité du Havre.",
            ],
            "en": [
                "About 10 minutes on foot, north across rue Sherbrooke.",
                "About 35 minutes by metro: green line from Pie-IX to Berri-UQAM, then the yellow line to Jean-Drapeau; the Biosphere is a few minutes from the station.",
                "About 40 minutes on foot, or 15 by bike, over the Concorde Bridge to Cité du Havre.",
            ],
            "es": [
                "Unos 10 minutos a pie hacia el norte, cruzando la calle Sherbrooke.",
                "Unos 35 minutos en metro: línea verde desde Pie-IX hasta Berri-UQAM y luego línea amarilla hasta Jean-Drapeau; la Biosfera está a pocos minutos de la estación.",
                "Unos 40 minutos a pie, o 15 en bicicleta, por el puente de la Concorde hasta la Cité du Havre.",
            ],
        },
    },
]


# ---------------------------------------------------------------------------
# 2. PRATIQUE — fiches courtes, faits solides seulement
# ---------------------------------------------------------------------------

PRATIQUE = [
    {
        "id": "se-deplacer",
        "titre": {
            "fr": "Se déplacer",
            "en": "Getting Around",
            "es": "Cómo moverse",
        },
        "texte": {
            "fr": "Le métro de la STM compte quatre lignes, qu'on désigne par leur couleur : verte, orange, jaune et bleue. On paie avec la carte OPUS, rechargeable aux distributeurs des stations, ou avec un titre de transport occasionnel ; les passes d'une journée ou de trois jours sont souvent les plus avantageuses. Le même titre vaut pour l'autobus. Aux beaux jours, les vélos en libre-service BIXI sont partout au centre de la ville. Et beaucoup de quartiers se découvrent simplement à pied.",
            "en": "The STM metro has four lines, known by their colour: green, orange, yellow and blue. You pay with an OPUS card, which you can top up at station machines, or with an occasional-use fare; one-day and three-day passes are often the best deal. The same fare works on buses. In the warmer months, BIXI bike-share stations are everywhere in the central neighbourhoods. And many parts of the city are best explored simply on foot.",
            "es": "El metro de la STM tiene cuatro líneas, que se nombran por su color: verde, naranja, amarilla y azul. Se paga con la tarjeta OPUS, recargable en las máquinas de las estaciones, o con un boleto ocasional; los pases de un día o de tres días suelen ser la mejor opción. El mismo boleto sirve en el autobús. En la temporada templada, las bicicletas compartidas BIXI están por todo el centro. Y muchos barrios se descubren simplemente a pie.",
        },
    },
    {
        "id": "aeroport",
        "titre": {
            "fr": "De l'aéroport au centre-ville",
            "en": "From the Airport to Downtown",
            "es": "Del aeropuerto al centro",
        },
        "texte": {
            "fr": "L'autobus 747 de la STM relie l'aéroport Montréal-Trudeau au centre-ville jour et nuit, toute l'année. Le trajet dure souvent entre 45 minutes et une heure, selon la circulation. Achetez votre titre au distributeur de la zone des arrivées : il donne aussi accès au métro et aux autobus pendant 24 heures. Les taxis appliquent un tarif fixe entre l'aéroport et le centre-ville, ce qui évite les mauvaises surprises.",
            "en": "The STM's 747 bus runs between Montréal-Trudeau airport and downtown around the clock, all year. The ride usually takes 45 minutes to an hour, depending on traffic. Buy your fare at the machine in the arrivals area: it also covers the metro and city buses for 24 hours. Taxis charge a flat rate between the airport and downtown, so there are no surprises on the meter.",
            "es": "El autobús 747 de la STM une el aeropuerto Montréal-Trudeau con el centro día y noche, todo el año. El trayecto suele durar entre 45 minutos y una hora, según el tráfico. Compre su boleto en la máquina de la zona de llegadas: también le da acceso al metro y a los autobuses durante 24 horas. Los taxis cobran una tarifa fija entre el aeropuerto y el centro, así que no hay sorpresas.",
        },
    },
    {
        "id": "langue",
        "titre": {
            "fr": "« Bonjour-Hi » et la langue",
            "en": "\"Bonjour-Hi\" and Language",
            "es": "«Bonjour-Hi» y el idioma",
        },
        "texte": {
            "fr": "Au Québec, le français est la seule langue officielle, et c'est la langue de la rue, des affiches et des commerces. Dans les boutiques du centre, on vous accueille souvent d'un « Bonjour-Hi » : vous répondez dans la langue de votre choix, et la conversation suit. Commencez toujours par « Bonjour », même si vous passez ensuite à l'anglais : le geste est remarqué. Les Montréalais changent de langue volontiers, et beaucoup passeront à l'anglais sans que vous le demandiez.",
            "en": "In Québec, French is the only official language, and it's the language of the street, the signs and the shops. Downtown, clerks often greet you with a \"Bonjour-Hi\": answer in the language you prefer and the conversation follows. Always start with \"Bonjour\", even if you switch to English right after; people notice and appreciate it. Montrealers switch languages easily, and many are happy to carry on in English.",
            "es": "En Quebec, el francés es el único idioma oficial, y es la lengua de la calle, de los letreros y de los comercios. En las tiendas del centro suelen recibirlo con un «Bonjour-Hi»: usted responde en el idioma que prefiera y la conversación sigue. Empiece siempre con «Bonjour», aunque luego pase al inglés: el gesto se nota y se agradece. Los montrealeses cambian de idioma con facilidad, y muchos pasarán al inglés sin que usted lo pida.",
        },
    },
    {
        "id": "pourboire",
        "titre": {
            "fr": "Le pourboire",
            "en": "Tipping",
            "es": "La propina",
        },
        "texte": {
            "fr": "Au restaurant et au bar, le service n'est pas compris dans l'addition. L'usage est de laisser de 15 à 20 %, calculé sur le montant avant les taxes. Le terminal de paiement vous propose souvent des pourcentages : vous pouvez aussi entrer le montant vous-même. Au bar, on laisse environ un dollar par consommation si l'on paie à chaque verre. On donne aussi un pourboire au chauffeur de taxi, au coiffeur et au livreur.",
            "en": "In restaurants and bars, service isn't included in the bill. The custom is to leave 15 to 20 percent, calculated on the amount before taxes. The card terminal will often suggest percentages, but you can also enter your own amount. At a bar, leave about a dollar a drink if you pay as you go. Taxi drivers, hairdressers and delivery people are tipped as well.",
            "es": "En restaurantes y bares, el servicio no está incluido en la cuenta. Lo habitual es dejar entre el 15 y el 20 %, calculado sobre el monto antes de impuestos. La terminal de pago suele proponer porcentajes, pero usted también puede escribir la cantidad. En el bar se deja alrededor de un dólar por bebida si paga cada vez. También se da propina al taxista, al peluquero y al repartidor.",
        },
    },
    {
        "id": "taxes",
        "titre": {
            "fr": "Les taxes à la caisse",
            "en": "Taxes at the Till",
            "es": "Los impuestos en la caja",
        },
        "texte": {
            "fr": "Le prix affiché sur l'étiquette ou au menu n'inclut presque jamais les taxes : elles s'ajoutent au moment de payer. Il y en a deux, la TPS, taxe fédérale, et la TVQ, taxe du Québec, qui font ensemble un peu moins de 15 %. Un article affiché à 20 dollars vous coûtera donc environ 23 dollars. Au restaurant, le pourboire s'ajoute par-dessus. Le prix de l'alcool et des billets de spectacle suit la même logique.",
            "en": "The price on the tag or the menu almost never includes tax: it's added when you pay. There are two, the GST, a federal tax, and the QST, Québec's tax, which together come to just under 15 percent. An item marked 20 dollars will cost you about 23. At a restaurant, the tip goes on top of that. Drinks and concert tickets work the same way.",
            "es": "El precio de la etiqueta o del menú casi nunca incluye los impuestos: se suman al momento de pagar. Son dos, la TPS, impuesto federal, y la TVQ, impuesto de Quebec, que juntos suman un poco menos del 15 %. Un artículo marcado a 20 dólares le costará unos 23. En el restaurante, la propina se añade encima. Con las bebidas y las entradas de espectáculos pasa lo mismo.",
        },
    },
    {
        "id": "saisons",
        "titre": {
            "fr": "Les saisons",
            "en": "The Seasons",
            "es": "Las estaciones",
        },
        "texte": {
            "fr": "L'hiver montréalais est long et froid, souvent sous les moins 10 degrés, avec de la neige de décembre à mars. Habillez-vous en couches, avec tuque, mitaines et bottes. Pour circuler au chaud, le RÉSO, qu'on appelle aussi la ville souterraine, relie par des couloirs des stations de métro, des centres commerciaux et des tours du centre-ville. L'été, chaud et humide, est la saison des festivals : il se passe quelque chose presque chaque fin de semaine.",
            "en": "Montréal winters are long and cold, often below minus 10 degrees, with snow from December to March. Dress in layers, with a toque, mittens and boots. To stay warm, the RÉSO, also called the underground city, links metro stations, shopping centres and downtown towers through indoor passages. Summer is hot and humid, and it's festival season: something is happening almost every weekend.",
            "es": "El invierno de Montreal es largo y frío, a menudo por debajo de los 10 grados bajo cero, con nieve de diciembre a marzo. Vístase por capas, con gorro, guantes y botas. Para moverse sin frío, el RÉSO, también llamado la ciudad subterránea, une por pasillos estaciones de metro, centros comerciales y torres del centro. El verano, caluroso y húmedo, es la temporada de festivales: hay algo casi cada fin de semana.",
        },
    },
    {
        "id": "pietons",
        "titre": {
            "fr": "Piétons et voitures",
            "en": "Pedestrians and Cars",
            "es": "Peatones y autos",
        },
        "texte": {
            "fr": "Sur l'île de Montréal, le virage à droite au feu rouge est interdit, contrairement au reste du Québec et à la plupart de l'Amérique du Nord. Si vous conduisez, attendez le feu vert. À pied, traversez aux intersections et suivez la silhouette blanche ; le décompte indique le temps qui reste. Méfiez-vous aussi des cyclistes : les pistes cyclables sont nombreuses, souvent à côté du trottoir, et les vélos y roulent vite.",
            "en": "On the island of Montréal, turning right on a red light is not allowed, unlike the rest of Québec and most of North America. If you're driving, wait for the green. On foot, cross at intersections and follow the white walking figure; the countdown shows how much time is left. Watch out for cyclists too: bike lanes are everywhere, often right next to the sidewalk, and riders move fast.",
            "es": "En la isla de Montreal está prohibido girar a la derecha con el semáforo en rojo, a diferencia del resto de Quebec y de casi toda América del Norte. Si maneja, espere la luz verde. A pie, cruce en las intersecciones y siga la silueta blanca; la cuenta regresiva indica el tiempo que queda. Cuidado también con los ciclistas: hay muchas ciclovías, a menudo junto a la acera, y las bicicletas van rápido.",
        },
    },
    {
        "id": "alcool",
        "titre": {
            "fr": "L'alcool",
            "en": "Buying Alcohol",
            "es": "El alcohol",
        },
        "texte": {
            "fr": "Au Québec, on peut acheter de l'alcool dès 18 ans. Les vins et les spiritueux se vendent surtout à la SAQ, la société d'État, dont les succursales sont nombreuses. La bière et une sélection de vins se trouvent aussi à l'épicerie et au dépanneur du coin. Enfin, cherchez les restaurants marqués « Apportez votre vin » : on y arrive avec sa propre bouteille, et le serveur l'ouvre pour vous. C'est une tradition bien montréalaise.",
            "en": "In Québec, the legal drinking age is 18. Wine and spirits are sold mainly at the SAQ, the provincial liquor stores, which you'll find all over town. Beer and a selection of wines are also sold at grocery stores and at the dépanneur, the corner store. And look for restaurants marked \"Apportez votre vin\", bring your own wine: you arrive with your own bottle and the server opens it for you. It's a true Montréal tradition.",
            "es": "En Quebec se puede comprar alcohol a partir de los 18 años. Los vinos y licores se venden sobre todo en la SAQ, la tienda estatal, con muchas sucursales. La cerveza y una selección de vinos también se encuentran en el supermercado y en el dépanneur, la tienda de la esquina. Y busque los restaurantes marcados «Apportez votre vin», traiga su vino: usted llega con su propia botella y el mesero la abre. Es una tradición muy montrealesa.",
        },
    },
    {
        "id": "securite",
        "titre": {
            "fr": "Sécurité et urgences",
            "en": "Safety and Emergencies",
            "es": "Seguridad y emergencias",
        },
        "texte": {
            "fr": "Montréal est une ville où l'on se promène facilement, de jour comme de soir, avec les précautions habituelles d'une grande ville : surveillez vos sacs dans le métro et les foules des festivals. En cas d'urgence, composez le 911, gratuit depuis n'importe quel téléphone, pour la police, les ambulances et les pompiers. Pour un problème de santé moins pressant, le 811 met en contact avec une infirmière. L'eau du robinet est potable partout.",
            "en": "Montréal is an easy city to walk around, by day or evening, with the usual big-city care: keep an eye on your bags in the metro and in festival crowds. In an emergency, dial 911, free from any phone, for police, ambulance and fire. For a less urgent health question, 811 connects you with a nurse. Tap water is safe to drink everywhere.",
            "es": "Montreal es una ciudad por la que se pasea con facilidad, de día y de noche, con las precauciones normales de una gran ciudad: vigile sus bolsas en el metro y entre la multitud de los festivales. En caso de emergencia, marque el 911, gratis desde cualquier teléfono, para policía, ambulancia y bomberos. Para un problema de salud menos urgente, el 811 lo comunica con una enfermera. El agua del grifo es potable en toda la ciudad.",
        },
    },
    {
        "id": "24-juin-1er-juillet",
        "titre": {
            "fr": "Le 24 juin et le 1er juillet",
            "en": "June 24 and July 1",
            "es": "El 24 de junio y el 1 de julio",
        },
        "texte": {
            "fr": "Le 24 juin, c'est la Fête nationale du Québec, qu'on appelle aussi la Saint-Jean-Baptiste : spectacles en plein air, drapeaux bleus et blancs, feux de joie. Une semaine plus tard, le 1er juillet, c'est la fête du Canada, mais aussi, à Montréal, le jour du déménagement : de nombreux baux se terminent ce jour-là. Attendez-vous à des camions partout, des rues encombrées et des meubles sur les trottoirs.",
            "en": "June 24 is Québec's Fête nationale, also known as Saint-Jean-Baptiste Day: outdoor concerts, blue and white flags, bonfires. A week later, July 1 is Canada Day, and in Montréal it's also Moving Day, because many leases end that day. Expect moving trucks on every block, crowded streets and furniture out on the sidewalks. If you're driving that day, allow plenty of extra time, and book your hotel early for the whole week.",
            "es": "El 24 de junio es la Fiesta Nacional de Quebec, también llamada San Juan Bautista: conciertos al aire libre, banderas azules y blancas, fogatas. Una semana después, el 1 de julio, es el Día de Canadá y, en Montreal, también el día de la mudanza, porque muchos contratos de alquiler terminan ese día. Espere camiones por todas partes, calles llenas y muebles en las aceras.",
        },
    },
]


# ---------------------------------------------------------------------------
# 3. MOTS — le français de Montréal, pour le touriste
# ---------------------------------------------------------------------------

MOTS = [
    {
        "fr": "un dépanneur",
        "sens": {
            "fr": "La petite épicerie du coin, ouverte tard, où l'on trouve du lait, des collations, de la bière et du vin.",
            "en": "The corner store, open late, selling milk, snacks, beer and wine.",
            "es": "La tiendita de la esquina, abierta hasta tarde, donde se compra leche, botanas, cerveza y vino.",
        },
        "exemple": "Je vais faire un saut au dépanneur, veux-tu quelque chose?",
    },
    {
        "fr": "une liqueur",
        "sens": {
            "fr": "Au Québec, une boisson gazeuse sucrée, et non un alcool fort.",
            "en": "In Québec, a soft drink or soda, not a spirit.",
            "es": "En Quebec, un refresco con gas, no un licor fuerte.",
        },
        "exemple": "Une poutine pis une liqueur, s'il vous plaît.",
    },
    {
        "fr": "un breuvage",
        "sens": {
            "fr": "Une boisson, n'importe laquelle ; le mot revient souvent dans les menus et au comptoir.",
            "en": "Any drink or beverage; you'll see it on menus and hear it at the counter.",
            "es": "Una bebida, cualquiera; aparece a menudo en los menús y en el mostrador.",
        },
        "exemple": "Le trio vient avec des frites et un breuvage.",
    },
    {
        "fr": "la Main",
        "sens": {
            "fr": "Le surnom du boulevard Saint-Laurent, l'artère qui sépare l'est et l'ouest de la ville.",
            "en": "The nickname for boulevard Saint-Laurent, the street that divides the city into east and west.",
            "es": "El apodo del bulevar Saint-Laurent, la avenida que divide la ciudad entre este y oeste.",
        },
        "exemple": "On se rejoint sur la Main, en face de chez Schwartz's.",
    },
    {
        "fr": "magasiner",
        "sens": {
            "fr": "Faire les boutiques, aller acheter ou simplement regarder dans les magasins.",
            "en": "To go shopping, whether to buy or just to browse.",
            "es": "Ir de compras, ya sea para comprar o solo para mirar.",
        },
        "exemple": "Cet après-midi, on va magasiner sur la rue Sainte-Catherine.",
    },
    {
        "fr": "un char",
        "sens": {
            "fr": "Une voiture, dans la langue de tous les jours.",
            "en": "A car, in everyday speech.",
            "es": "Un auto, en el habla de todos los días.",
        },
        "exemple": "Pas besoin de char, le métro t'amène partout.",
    },
    {
        "fr": "c'est correct",
        "sens": {
            "fr": "Ça va, pas de problème ; on le dit pour accepter, rassurer ou refuser poliment.",
            "en": "It's fine, no problem; used to agree, to reassure, or to politely decline.",
            "es": "Está bien, no hay problema; se usa para aceptar, tranquilizar o rechazar con cortesía.",
        },
        "exemple": "Non merci, c'est correct, j'ai déjà mangé.",
    },
    {
        "fr": "bienvenue",
        "sens": {
            "fr": "En réponse à « merci », l'équivalent de « de rien ».",
            "en": "Said in reply to \"merci\"; it means \"you're welcome\".",
            "es": "Se dice en respuesta a «merci»; equivale a «de nada».",
        },
        "exemple": "Merci pour le plan! — Bienvenue, bonne visite!",
    },
    {
        "fr": "un chum, une blonde",
        "sens": {
            "fr": "Le copain et la copine ; « un chum » veut aussi dire un ami.",
            "en": "Boyfriend and girlfriend; \"un chum\" can also simply mean a friend.",
            "es": "El novio y la novia; «un chum» también puede significar un amigo.",
        },
        "exemple": "Je suis venue avec mon chum, pis ma sœur avec sa blonde.",
    },
    {
        "fr": "déjeuner, dîner, souper",
        "sens": {
            "fr": "Les trois repas de la journée : le matin, le midi et le soir.",
            "en": "The three meals of the day: breakfast, lunch and dinner.",
            "es": "Las tres comidas del día: desayuno, almuerzo y cena.",
        },
        "exemple": "On déjeune au café, on dîne au marché pis on soupe dans le Plateau.",
    },
    {
        "fr": "une tuque",
        "sens": {
            "fr": "Le bonnet de laine qu'on porte tout l'hiver, souvent avec un pompon.",
            "en": "A woolly winter hat, a toque, often with a pompom.",
            "es": "El gorro de lana que se usa todo el invierno, a menudo con pompón.",
        },
        "exemple": "Mets ta tuque, il fait moins vingt dehors.",
    },
    {
        "fr": "il fait frette",
        "sens": {
            "fr": "Il fait très froid ; « frette » est plus fort que « froid ».",
            "en": "It's freezing; \"frette\" is stronger than plain \"cold\".",
            "es": "Hace muchísimo frío; «frette» es más fuerte que «frío».",
        },
        "exemple": "Il fait frette à matin, on prend le métro.",
    },
    {
        "fr": "pas pire",
        "sens": {
            "fr": "Pas mal du tout, plutôt bien ; c'est souvent un vrai compliment.",
            "en": "Not bad at all, pretty good; often a genuine compliment.",
            "es": "Nada mal, bastante bien; muchas veces es un verdadero elogio.",
        },
        "exemple": "Pis, la poutine? — Pas pire pantoute!",
    },
    {
        "fr": "c'est plate",
        "sens": {
            "fr": "C'est ennuyeux ou c'est dommage, selon le contexte.",
            "en": "It's boring, or it's too bad, depending on the context.",
            "es": "Es aburrido, o es una lástima, según el contexto.",
        },
        "exemple": "C'est plate, le musée est fermé aujourd'hui.",
    },
]


# ---------------------------------------------------------------------------
# Faits à contrôler avant publication
# ---------------------------------------------------------------------------

VERIFIER = [
    "Durées de marche à recouper sur une carte : Biosphère–Habitat 67 par le pont de la Concorde (environ 40 minutes) et Oratoire–chemin Remembrance (environ 15 minutes).",
]


if __name__ == "__main__":
    ids_valides = {
        "vieux-port", "notre-dame", "place-jacques-cartier", "pointe-a-calliere",
        "mont-royal", "oratoire", "parc-olympique", "jardin-botanique", "habitat-67",
        "biosphere", "mbam", "quartier-spectacles", "canal-lachine", "plateau",
        "mile-end", "quartier-chinois", "marche-jean-talon", "marche-atwater",
        "romados", "schwartz", "bagels", "la-banquise", "wilenskys", "orange-julep",
        "cafe-olimpico", "cafe-italia", "santropol", "dieu-du-ciel",
    }
    for c in CIRCUITS:
        assert set(c["etapes"]) <= ids_valides, c["id"]
        for lg in ("fr", "en", "es"):
            assert len(c["liaisons"][lg]) == len(c["etapes"]) - 1, (c["id"], lg)
    print(len(CIRCUITS), "circuits,", len(PRATIQUE), "fiches,", len(MOTS), "mots : OK")
