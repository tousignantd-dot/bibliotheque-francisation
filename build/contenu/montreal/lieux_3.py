# -*- coding: utf-8 -*-
"""Guide de Montréal — lieux, lot 3 : manger et boire."""

LIEUX = [
    # ------------------------------------------------------------------
    {
        "id": "schwartz",
        "cat": "manger",
        "quartier": "Plateau-Mont-Royal",
        "metro": "Sherbrooke",
        "adresse": "3895, boulevard Saint-Laurent",
        "geo": (45.5163, -73.5777),
        "duree": 60,
        "nom": {
            "fr": "Schwartz's",
            "en": "Schwartz's",
            "es": "Schwartz's",
        },
        "bref": {
            "fr": "Le smoked meat le plus célèbre de la Main, tranché à la main depuis 1928.",
            "en": "The Main's most famous smoked meat, hand-sliced since 1928.",
            "es": "El smoked meat más famoso de la Main, cortado a mano desde 1928.",
        },
        "texte": {
            "fr": (
                "Sur le boulevard Saint-Laurent, que les Montréalais appellent la Main, une file s'allonge presque chaque jour devant une devanture modeste. "
                "C'est Schwartz's, une charcuterie hébraïque ouverte en 1928 par un immigrant juif de Roumanie. "
                "On y sert le smoked meat, une poitrine de bœuf marinée dans les épices pendant plusieurs jours, puis fumée et cuite à la vapeur.\n\n"
                "La salle est étroite et bruyante. On s'assoit souvent à côté d'inconnus, et le serveur arrive vite. "
                "La viande est tranchée à la main, empilée haut entre deux tranches de pain de seigle, avec un peu de moutarde. "
                "Le secret, disent les habitués, c'est le choix du gras : maigre, medium ou gras. "
                "Le medium offre le meilleur équilibre entre tendreté et saveur.\n\n"
                "Le rituel se complète avec un gros cornichon à l'aneth, des frites, et une boisson gazeuse à la cerise noire, "
                "le compagnon traditionnel de la maison. "
                "Ici, rien n'a vraiment changé depuis des générations, et c'est exactement ce que l'on vient chercher."
            ),
            "en": (
                "On Saint-Laurent Boulevard, which locals simply call the Main, a line forms almost every day outside a plain little storefront. "
                "This is Schwartz's, a Hebrew delicatessen opened in 1928 by a Jewish immigrant from Romania. "
                "Its specialty is smoked meat: beef brisket cured in spices for days, then smoked and steamed until it practically melts.\n\n"
                "The room is narrow, noisy and wonderfully cramped. You will probably share a table with strangers, and the waiter will not keep you waiting. "
                "The meat is sliced by hand and piled high on rye bread with a thin layer of yellow mustard. "
                "Regulars will tell you that the real decision is the fat: lean, medium or fatty. "
                "Medium is the classic choice, tender and full of flavour.\n\n"
                "Complete the ritual with a big dill pickle, a side of fries and a black cherry soda, the house's traditional pairing. "
                "Very little has changed here in generations, and that is exactly the point."
            ),
            "es": (
                "Sobre el bulevar Saint-Laurent, que los montrealeses llaman simplemente la Main, casi todos los días se forma una fila frente a una fachada muy sencilla. "
                "Es Schwartz's, una charcutería judía abierta en 1928 por un inmigrante llegado de Rumania. "
                "Su especialidad es el smoked meat: pecho de res marinado varios días en especias, luego ahumado y cocido al vapor.\n\n"
                "El local es angosto y ruidoso. Es muy probable que usted comparta la mesa con desconocidos, y el mesero llega enseguida. "
                "La carne se corta a mano y se apila bien alto sobre pan de centeno, con un poco de mostaza. "
                "Según los clientes de toda la vida, la verdadera decisión es la grasa: magra, media o grasosa. "
                "La media es la elección clásica, tierna y llena de sabor.\n\n"
                "Para completar el ritual, pida un pepinillo grande al eneldo, papas fritas y un refresco de cereza negra, el acompañante tradicional de la casa. "
                "Aquí casi nada ha cambiado en varias generaciones, y eso es justamente lo que uno viene a buscar."
            ),
        },
        "conseil": {
            "fr": "Évitez l'heure du dîner et le samedi soir. Si vous êtes pressé, le comptoir de la boutique d'à côté vend le même smoked meat pour emporter.",
            "en": "Skip the lunch rush and Saturday nights. In a hurry? The take-out counter next door sells the same smoked meat to go.",
            "es": "Evite la hora del almuerzo y los sábados por la noche. Si tiene prisa, el mostrador para llevar de al lado vende el mismo smoked meat.",
        },
        "commander": {
            "fr": "Un sandwich smoked meat medium, un cornichon, des frites et un cola à la cerise noire. Au serveur : « Un smoked meat medium, s'il vous plaît, avec un cornichon. »",
            "en": "A medium smoked meat sandwich, a pickle, fries and a black cherry soda. Tell the waiter: \"Un smoked meat medium, s'il vous plaît, avec un cornichon.\"",
            "es": "Un sándwich de smoked meat medio, un pepinillo, papas fritas y un refresco de cereza negra. Diga al mesero: « Un smoked meat medium, s'il vous plaît, avec un cornichon. »",
        },
        "anecdote": {
            "fr": "En 2012, un groupe d'investisseurs comprenant René Angélil et Céline Dion a racheté Schwartz's.",
            "en": "In 2012, a group of investors including René Angélil and Céline Dion bought Schwartz's.",
            "es": "En 2012, un grupo de inversionistas que incluía a René Angélil y Céline Dion compró Schwartz's.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "bagels",
        "cat": "manger",
        "quartier": "Mile End",
        "metro": "Laurier",
        "adresse": "263, rue Saint-Viateur Ouest",
        "geo": (45.5228, -73.6027),
        "duree": 30,
        "nom": {
            "fr": "Les bagels du Mile End : St-Viateur et Fairmount",
            "en": "Mile End Bagels: St-Viateur and Fairmount",
            "es": "Los bagels del Mile End: St-Viateur y Fairmount",
        },
        "bref": {
            "fr": "Deux fours à bois, deux rivaux, et le bagel le plus montréalais qui soit.",
            "en": "Two wood-fired ovens, two rivals, and the most Montreal bagel there is.",
            "es": "Dos hornos de leña, dos rivales y el bagel más montrealés que existe.",
        },
        "texte": {
            "fr": (
                "Le bagel de Montréal ne ressemble pas à celui de New York. Il est plus petit, plus dense, un peu sucré, avec un grand trou au centre. "
                "Sa recette a été apportée par des boulangers juifs d'Europe de l'Est, installés dans le Mile End au siècle dernier.\n\n"
                "Tout se joue en deux gestes. D'abord, la pâte roulée à la main est plongée quelques instants dans une eau bouillante sucrée au miel. "
                "Ensuite, les bagels sont enfournés sur de longues planches dans un four à bois, qui leur donne une croûte dorée et un goût légèrement fumé. "
                "Derrière le comptoir, vous verrez les boulangers travailler sans relâche, souvent jour et nuit.\n\n"
                "Deux adresses se disputent le titre du meilleur bagel : St-Viateur Bagel, sur la rue du même nom, et Fairmount Bagel, à quelques rues de là. "
                "Les Montréalais ont chacun leur camp. "
                "Le plus simple est de goûter aux deux, encore chauds, et de décider vous-même."
            ),
            "en": (
                "A Montreal bagel is nothing like its New York cousin. It is smaller, denser and slightly sweet, with a generous hole in the middle. "
                "The recipe came with Jewish bakers from Eastern Europe who settled in Mile End in the last century.\n\n"
                "Everything happens in two steps. First, hand-rolled dough is dipped briefly in boiling water sweetened with honey. "
                "Then the bagels slide into a wood-fired oven on long wooden planks, which gives them a golden crust and a faint smoky taste. "
                "From the counter, you can watch the bakers at work, often around the clock.\n\n"
                "Two shops compete for the title of best bagel in town: St-Viateur Bagel, on the street of the same name, and Fairmount Bagel, just a few blocks away. "
                "Every Montrealer has picked a side. "
                "The best plan is to try both while they are still warm, and settle the debate yourself."
            ),
            "es": (
                "El bagel de Montreal no se parece al de Nueva York. Es más pequeño, más denso y ligeramente dulce, con un agujero grande en el centro. "
                "La receta llegó con panaderos judíos de Europa del Este que se instalaron en el Mile End el siglo pasado.\n\n"
                "Todo ocurre en dos pasos. Primero, la masa enrollada a mano se sumerge unos instantes en agua hirviendo endulzada con miel. "
                "Después, los bagels entran en un horno de leña sobre largas tablas de madera, que les da una corteza dorada y un sabor apenas ahumado. "
                "Desde el mostrador, usted puede ver a los panaderos trabajar sin descanso, muchas veces día y noche.\n\n"
                "Dos panaderías se disputan el título del mejor bagel: St-Viateur Bagel, en la calle del mismo nombre, y Fairmount Bagel, a pocas cuadras. "
                "Cada montrealés tiene su favorito. "
                "Lo mejor es probar los dos, todavía calientes, y decidir usted mismo."
            ),
        },
        "conseil": {
            "fr": "Achetez une douzaine et mangez-en un tout de suite, dans la rue : un bagel se goûte chaud. Apportez de l'argent comptant, au cas où.",
            "en": "Buy a dozen and eat one right away on the sidewalk: a bagel is best warm. Bring some cash, just in case.",
            "es": "Compre una docena y coma uno enseguida en la acera: el bagel se disfruta caliente. Lleve algo de efectivo, por si acaso.",
        },
        "commander": {
            "fr": "Le sésame est le classique, le pavot vient juste après. Au comptoir : « Une douzaine au sésame, s'il vous plaît, avec un petit pot de fromage à la crème. »",
            "en": "Sesame is the classic, poppy seed the runner-up. At the counter: \"Une douzaine au sésame, s'il vous plaît.\"",
            "es": "El de sésamo es el clásico; el de amapola, la alternativa. En el mostrador: « Une douzaine au sésame, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "En 2008, l'astronaute Gregory Chamitoff, qui a grandi à Montréal, a emporté des bagels de Fairmount jusqu'à la Station spatiale internationale.",
            "en": "In 2008, astronaut Gregory Chamitoff, who grew up in Montreal, took Fairmount bagels with him to the International Space Station.",
            "es": "En 2008, el astronauta Gregory Chamitoff, que creció en Montreal, llevó bagels de Fairmount a la Estación Espacial Internacional.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "la-banquise",
        "cat": "manger",
        "quartier": "Plateau-Mont-Royal",
        "metro": "Mont-Royal",
        "adresse": "994, rue Rachel Est",
        "geo": (45.5254, -73.5746),
        "duree": 45,
        "nom": {
            "fr": "La Banquise",
            "en": "La Banquise",
            "es": "La Banquise",
        },
        "bref": {
            "fr": "La poutine à toute heure, à deux pas du parc La Fontaine.",
            "en": "Poutine at any hour, steps from La Fontaine Park.",
            "es": "Poutine a cualquier hora, a dos pasos del parque La Fontaine.",
        },
        "texte": {
            "fr": (
                "Impossible de quitter le Québec sans goûter à la poutine. "
                "C'est un plat tout simple : des frites, des morceaux de fromage en grains et une sauce brune bien chaude versée par-dessus. "
                "Le fromage doit être frais, assez pour faire « squick squick » sous la dent, et la sauce le fait fondre juste un peu.\n\n"
                "Née dans les campagnes du Québec à la fin des années cinquante, la poutine a longtemps été moquée avant de devenir un symbole national. "
                "À Montréal, l'adresse la plus connue est La Banquise, rue Rachel, tout près du parc La Fontaine. "
                "Ouverte jour et nuit, elle nourrit aussi bien les familles du dimanche que les fêtards de trois heures du matin.\n\n"
                "Le menu propose des dizaines de versions, garnies de saucisse, de bacon, de légumes ou de viande fumée. "
                "La salle est colorée, sans prétention, et souvent pleine. "
                "Commencez par la classique : c'est elle qui vous fera comprendre pourquoi les Québécois en sont si fiers."
            ),
            "en": (
                "You cannot leave Quebec without trying poutine. "
                "It is a simple dish: French fries, fresh cheese curds and hot brown gravy poured over the top. "
                "The curds should be fresh enough to squeak against your teeth, and the gravy should melt them only a little.\n\n"
                "Poutine was born in rural Quebec in the late nineteen fifties. For years it was mocked, and today it is a point of national pride. "
                "In Montreal, the best-known address is La Banquise, on Rachel Street, right by La Fontaine Park. "
                "It is open day and night, feeding Sunday families and three in the morning party crowds alike.\n\n"
                "The menu lists dozens of versions, topped with sausage, bacon, vegetables or smoked meat. "
                "The dining room is bright, casual and usually packed. "
                "Start with the classic: one bite and you will understand why Quebecers are so proud of it."
            ),
            "es": (
                "No se puede salir de Quebec sin probar la poutine. "
                "Es un plato muy sencillo: papas fritas, trocitos de queso fresco en grano y una salsa oscura bien caliente por encima. "
                "El queso debe estar tan fresco que rechine un poco al morderlo, y la salsa apenas debe derretirlo.\n\n"
                "La poutine nació en el campo quebequense a finales de los años cincuenta. Durante mucho tiempo fue objeto de burlas, y hoy es un orgullo nacional. "
                "En Montreal, la dirección más conocida es La Banquise, en la calle Rachel, junto al parque La Fontaine. "
                "Abre día y noche, y recibe tanto a familias el domingo como a quienes salen de fiesta a las tres de la mañana.\n\n"
                "El menú ofrece decenas de versiones, con salchicha, tocino, verduras o carne ahumada. "
                "El local es colorido, informal y casi siempre está lleno. "
                "Empiece por la clásica: con un bocado entenderá por qué los quebequenses están tan orgullosos de ella."
            ),
        },
        "conseil": {
            "fr": "Une petite portion suffit souvent pour une personne. Passez ensuite digérer au parc La Fontaine, à deux minutes à pied.",
            "en": "A small portion is usually plenty for one. Walk it off afterwards in La Fontaine Park, two minutes away.",
            "es": "Una porción pequeña suele bastar para una persona. Después, camine un poco por el parque La Fontaine, a dos minutos.",
        },
        "commander": {
            "fr": "La poutine classique pour commencer, puis une version garnie si vous êtes plusieurs. Au serveur : « Une poutine classique, petite, s'il vous plaît. »",
            "en": "The classic poutine first, then a loaded version to share. Tell the server: \"Une poutine classique, petite, s'il vous plaît.\"",
            "es": "Primero la poutine clásica, luego una con ingredientes para compartir. Diga al mesero: « Une poutine classique, petite, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "La Banquise a commencé en 1968 comme simple comptoir à crème glacée, d'où son nom.",
            "en": "La Banquise, French for \"ice floe\", opened in 1968 as an ice cream stand.",
            "es": "La Banquise, que significa \"banco de hielo\", abrió en 1968 como heladería.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "wilenskys",
        "cat": "manger",
        "quartier": "Mile End",
        "metro": "Laurier",
        "adresse": "34, avenue Fairmount Ouest",
        "geo": (45.5233, -73.5948),
        "duree": 20,
        "nom": {
            "fr": "Wilensky's Light Lunch",
            "en": "Wilensky's Light Lunch",
            "es": "Wilensky's Light Lunch",
        },
        "bref": {
            "fr": "Un comptoir figé dans le temps et un sandwich qui a ses propres règles.",
            "en": "A lunch counter frozen in time, and a sandwich with rules of its own.",
            "es": "Un mostrador detenido en el tiempo y un sándwich con reglas propias.",
        },
        "texte": {
            "fr": (
                "Au coin de la rue Clark et de l'avenue Fairmount, un petit casse-croûte semble avoir oublié de changer d'époque. "
                "Wilensky's Light Lunch occupe ce local depuis 1952. "
                "Quelques tabourets devant un long comptoir, une vieille caisse, des bouteilles de soda qu'on prépare encore à la main : le décor n'a presque pas bougé.\n\n"
                "La vedette de la maison s'appelle le Special. "
                "C'est un pain kaiser garni de salami et de saucisson de bologne, pressé et grillé sur la plaque. "
                "Il obéit à deux règles célèbres. On ne le coupe jamais en deux, et on y met toujours de la moutarde. "
                "Si vous la refusez, on vous le fera payer un peu plus cher, avec le sourire.\n\n"
                "L'endroit a inspiré le romancier Mordecai Richler, qui a grandi dans le quartier, et il est apparu au cinéma. "
                "Ici, on vient moins pour un repas que pour un moment de l'histoire du Mile End."
            ),
            "en": (
                "At the corner of Clark Street and Fairmount Avenue, a tiny lunch counter seems to have forgotten to change with the times. "
                "Wilensky's Light Lunch has been in this spot since 1952. "
                "A few stools along a long counter, an old cash register, sodas still mixed by hand: the place has barely changed.\n\n"
                "The star of the house is the Special. "
                "It is a kaiser roll filled with salami and bologna, pressed and grilled on the flat top. "
                "It comes with two famous rules. It is never cut in half, and it always gets mustard. "
                "Ask for it without mustard and you will pay a little extra, with a smile.\n\n"
                "The counter inspired the novelist Mordecai Richler, who grew up in the neighbourhood, and it has appeared on the big screen. "
                "People come here less for a meal than for a small, delicious piece of Mile End history."
            ),
            "es": (
                "En la esquina de la calle Clark y la avenida Fairmount, un pequeño local de comidas parece haberse olvidado de cambiar de época. "
                "Wilensky's Light Lunch ocupa este lugar desde 1952. "
                "Unos cuantos taburetes frente a un largo mostrador, una caja registradora antigua y refrescos que todavía se preparan a mano: casi nada ha cambiado.\n\n"
                "La estrella de la casa se llama el Special. "
                "Es un pan kaiser relleno de salami y mortadela, prensado y dorado en la plancha. "
                "Tiene dos reglas famosas. Nunca se corta por la mitad, y siempre lleva mostaza. "
                "Si usted la rechaza, le cobrarán un poco más, eso sí, con una sonrisa.\n\n"
                "El lugar inspiró al novelista Mordecai Richler, que creció en el barrio, y ha aparecido en el cine. "
                "Aquí uno viene menos por la comida que por un pedacito sabroso de la historia del Mile End."
            ),
        },
        "conseil": {
            "fr": "La place est limitée : prenez votre Special au comptoir ou pour emporter, et marchez jusqu'aux bagels de la rue voisine.",
            "en": "Seating is limited: eat at the counter or take it to go, then walk over to the bagel shops nearby.",
            "es": "Hay poco espacio: coma en el mostrador o pídalo para llevar, y luego camine hasta las panaderías de bagels cercanas.",
        },
        "commander": {
            "fr": "Un Special, un cornichon et un soda à la fontaine, cerise ou cola. Au comptoir : « Un Special et un soda à la cerise, s'il vous plaît. »",
            "en": "A Special, a pickle and a fountain soda, cherry or cola. At the counter: \"Un Special et un soda à la cerise, s'il vous plaît.\"",
            "es": "Un Special, un pepinillo y un refresco de fuente, de cereza o cola. En el mostrador: « Un Special et un soda à la cerise, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "Le casse-croûte apparaît dans le film L'apprentissage de Duddy Kravitz, tiré du roman de Mordecai Richler.",
            "en": "The counter appears in The Apprenticeship of Duddy Kravitz, the film based on Mordecai Richler's novel.",
            "es": "El local aparece en la película The Apprenticeship of Duddy Kravitz, basada en la novela de Mordecai Richler.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "orange-julep",
        "cat": "manger",
        "quartier": "Côte-des-Neiges–Notre-Dame-de-Grâce",
        "metro": "Namur",
        "adresse": "7700, boulevard Décarie",
        "geo": (45.4957, -73.6568),
        "duree": 30,
        "nom": {
            "fr": "L'Orange Julep",
            "en": "Orange Julep",
            "es": "Orange Julep",
        },
        "bref": {
            "fr": "Une orange géante au bord de l'autoroute, et une boisson mousseuse au goût d'été.",
            "en": "A giant orange by the expressway, and a frothy drink that tastes like summer.",
            "es": "Una naranja gigante junto a la autopista y una bebida espumosa con sabor a verano.",
        },
        "texte": {
            "fr": (
                "Le long du boulevard Décarie, entre deux voies rapides, surgit une énorme boule orange de trois étages. "
                "Ce n'est pas une œuvre d'art contemporain, c'est l'Orange Julep, un casse-croûte devenu l'un des repères les plus aimés de Montréal.\n\n"
                "L'histoire commence dans les années trente avec la famille Gibeau, qui invente une boisson à l'orange, douce, crémeuse et mousseuse. "
                "Sa recette exacte est restée un secret de famille. "
                "La grosse orange actuelle, construite dans les années soixante, a remplacé une première version plus petite. "
                "On y commande au comptoir, comme dans les années cinquante, des hot-dogs, des frites, des poutines et, bien sûr, le fameux julep.\n\n"
                "Les soirs d'été, le stationnement se transforme en musée à ciel ouvert. "
                "Les amateurs de voitures anciennes s'y donnent rendez-vous pour montrer leurs chromes et leurs moteurs. "
                "C'est l'endroit parfait pour une pause simple, un peu kitsch, et profondément montréalaise."
            ),
            "en": (
                "Along Décarie Boulevard, squeezed between busy expressways, a three-storey orange ball rises out of nowhere. "
                "It is not a piece of modern art. It is the Orange Julep, a roadside snack bar that has become one of Montreal's best-loved landmarks.\n\n"
                "The story begins in the nineteen thirties with the Gibeau family, who created a sweet, creamy, frothy orange drink. "
                "The exact recipe remains a family secret. "
                "The big orange you see today was built in the sixties, replacing a smaller first version. "
                "You order at the window, fifties style: hot dogs, fries, poutine and, of course, the famous julep.\n\n"
                "On summer evenings, the parking lot turns into an open-air car museum. "
                "Classic car fans gather to show off their chrome and polished engines. "
                "It is the perfect stop for something simple, a little kitschy and deeply Montreal."
            ),
            "es": (
                "A lo largo del bulevar Décarie, entre dos autopistas, aparece de pronto una enorme bola anaranjada de tres pisos. "
                "No es una obra de arte contemporáneo. Es el Orange Julep, un puesto de comida que se ha convertido en uno de los íconos más queridos de Montreal.\n\n"
                "La historia empieza en los años treinta con la familia Gibeau, que inventó una bebida de naranja dulce, cremosa y espumosa. "
                "La receta exacta sigue siendo un secreto de familia. "
                "La gran naranja que usted ve hoy se construyó en los años sesenta y reemplazó a una primera versión más pequeña. "
                "Se pide en la ventanilla, como en los años cincuenta: perros calientes, papas fritas, poutine y, claro, el famoso julep.\n\n"
                "En las noches de verano, el estacionamiento se convierte en un museo al aire libre. "
                "Los aficionados a los autos clásicos se reúnen para lucir sus cromados y sus motores. "
                "Es la parada perfecta para algo sencillo, un poco kitsch y muy montrealés."
            ),
        },
        "conseil": {
            "fr": "Venez un mercredi soir d'été pour voir les voitures anciennes. C'est à la belle saison que l'endroit est le plus animé.",
            "en": "Come on a summer Wednesday evening for the classic cars. The place is at its liveliest in the warm months.",
            "es": "Venga un miércoles por la noche en verano para ver los autos clásicos. El lugar tiene más ambiente en la temporada cálida.",
        },
        "commander": {
            "fr": "Un julep, bien sûr, avec un hot-dog steamé. Au comptoir : « Un grand julep et un hot-dog steamé, s'il vous plaît. »",
            "en": "A julep, of course, with a steamed hot dog, a \"steamé\" as locals say. At the window: \"Un grand julep et un hot-dog steamé, s'il vous plaît.\"",
            "es": "Un julep, claro, con un perro caliente al vapor, un « steamé » como dicen aquí. En la ventanilla: « Un grand julep et un hot-dog steamé, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "La grosse orange mesure environ douze mètres de diamètre, soit à peu près la hauteur d'un immeuble de trois étages.",
            "en": "The big orange is about twelve metres across, roughly the height of a three-storey building.",
            "es": "La gran naranja mide unos doce metros de diámetro, casi la altura de un edificio de tres pisos.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "cafe-olimpico",
        "cat": "boire",
        "quartier": "Mile End",
        "metro": "Laurier",
        "adresse": "124, rue Saint-Viateur Ouest",
        "geo": (45.5241, -73.6003),
        "duree": 30,
        "nom": {
            "fr": "Café Olimpico",
            "en": "Café Olimpico",
            "es": "Café Olimpico",
        },
        "bref": {
            "fr": "L'espresso du Mile End, servi sans chichi depuis des décennies.",
            "en": "Mile End's espresso, served without fuss for decades.",
            "es": "El espresso del Mile End, servido sin rodeos desde hace décadas.",
        },
        "texte": {
            "fr": (
                "Rue Saint-Viateur, au cœur du Mile End, un café de quartier fondé par des immigrants italiens est devenu une institution. "
                "Au Café Olimpico, on commande au comptoir, on paie, on trouve une place si on peut. "
                "Aucun menu compliqué, aucune mise en scène : seulement un espresso serré, un cappuccino mousseux et quelques pâtisseries.\n\n"
                "La salle est un vrai portrait du quartier. "
                "Des retraités italiens y discutent de soccer, des étudiants y lisent, des musiciens et des familles se croisent au comptoir. "
                "Les écrans diffusent souvent un match, et quand l'Italie joue, l'ambiance monte d'un cran.\n\n"
                "Aux beaux jours, tout se passe dehors. "
                "Les bancs le long du trottoir et la terrasse se remplissent dès le matin, et le café devient le salon à ciel ouvert du Mile End. "
                "C'est l'arrêt idéal entre deux boutiques, ou juste après un bagel acheté un peu plus loin sur la même rue."
            ),
            "en": (
                "On Saint-Viateur Street, in the heart of Mile End, a neighbourhood café opened by Italian immigrants has become an institution. "
                "At Café Olimpico, you order at the counter, pay, and grab a seat if you can find one. "
                "No complicated menu, no show: just a tight espresso, a foamy cappuccino and a few pastries.\n\n"
                "The room is a portrait of the neighbourhood. "
                "Retired Italian men argue about soccer, students read, musicians and young families cross paths at the counter. "
                "The screens often show a match, and when Italy plays, the volume goes way up.\n\n"
                "In warm weather, everything moves outside. "
                "The benches along the sidewalk and the terrace fill up from early morning, and the café becomes Mile End's open-air living room. "
                "It is the ideal stop between two shops, or right after a warm bagel bought a little farther down the same street."
            ),
            "es": (
                "En la calle Saint-Viateur, en pleno Mile End, un café de barrio abierto por inmigrantes italianos se ha convertido en una institución. "
                "En el Café Olimpico, se pide en el mostrador, se paga y se busca un lugar si lo hay. "
                "No hay menú complicado ni espectáculo: solo un espresso corto, un capuchino espumoso y algunos pasteles.\n\n"
                "El salón es un retrato del barrio. "
                "Jubilados italianos discuten de fútbol, estudiantes leen, músicos y familias se cruzan en el mostrador. "
                "Las pantallas suelen transmitir un partido, y cuando juega Italia, el ambiente se enciende.\n\n"
                "Cuando hace buen tiempo, todo sucede afuera. "
                "Las bancas junto a la acera y la terraza se llenan desde temprano, y el café se vuelve la sala al aire libre del Mile End. "
                "Es la parada ideal entre dos tiendas, o justo después de un bagel comprado un poco más adelante en la misma calle."
            ),
        },
        "conseil": {
            "fr": "Le matin de semaine est le moment le plus calme. La file avance vite : sachez ce que vous voulez avant d'arriver au comptoir.",
            "en": "Weekday mornings are the calmest. The line moves fast, so know your order before you reach the counter.",
            "es": "Las mañanas entre semana son las más tranquilas. La fila avanza rápido: tenga su pedido listo al llegar al mostrador.",
        },
        "commander": {
            "fr": "Un espresso ou un cappuccino, avec une pâtisserie si le cœur vous en dit. Au comptoir : « Un cappuccino, s'il vous plaît, pour ici. »",
            "en": "An espresso or a cappuccino, with a pastry if you like. At the counter: \"Un cappuccino, s'il vous plaît, pour ici.\"",
            "es": "Un espresso o un capuchino, con algún pastelito si se le antoja. En el mostrador: « Un cappuccino, s'il vous plaît, pour ici. »",
        },
        "anecdote": {
            "fr": "À son ouverture en 1970, le café s'annonçait « Open Da Night », une façon bien à lui de dire « ouvert jour et nuit ».",
            "en": "When it opened in 1970, the café billed itself as \"Open Da Night\", its own way of saying open day and night.",
            "es": "Cuando abrió en 1970, el café se anunciaba como \"Open Da Night\", su manera de decir abierto día y noche.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "cafe-italia",
        "cat": "boire",
        "quartier": "Rosemont–La Petite-Patrie",
        "metro": "Jean-Talon",
        "adresse": "6840, boulevard Saint-Laurent",
        "geo": (45.5327, -73.6143),
        "duree": 30,
        "nom": {
            "fr": "Caffè Italia",
            "en": "Caffè Italia",
            "es": "Caffè Italia",
        },
        "bref": {
            "fr": "Le café de la Petite-Italie, inchangé depuis 1956, et bruyant les soirs de match.",
            "en": "Little Italy's café, unchanged since 1956 and roaring on match nights.",
            "es": "El café de la Pequeña Italia, igual desde 1956 y ruidoso en noches de partido.",
        },
        "texte": {
            "fr": (
                "Sur le boulevard Saint-Laurent, au cœur de la Petite-Italie, le Caffè Italia sert le même espresso depuis 1956. "
                "À l'époque, il accueillait la grande vague d'immigrants italiens arrivés à Montréal après la guerre. "
                "Pour eux, c'était un morceau du pays, un endroit où l'on parlait sa langue et où l'on buvait un vrai café.\n\n"
                "Le décor a très peu changé. "
                "Un long comptoir, une machine à espresso qui siffle, des photos d'équipes de soccer, quelques tables serrées. "
                "La maison est toujours tenue par la même famille, et les habitués s'y saluent par leur prénom.\n\n"
                "Le vrai spectacle commence les soirs de match. "
                "Quand l'équipe d'Italie joue, la salle se remplit, les chaises débordent sur le trottoir et chaque but fait trembler le quartier. "
                "Même sans match, prenez le temps d'un espresso debout au comptoir, à l'italienne, "
                "avant d'aller marcher jusqu'au marché Jean-Talon, tout près."
            ),
            "en": (
                "On Saint-Laurent Boulevard, in the heart of Little Italy, Caffè Italia has been pulling the same espresso since 1956. "
                "Back then, it welcomed the great wave of Italian immigrants who came to Montreal after the war. "
                "For them, it was a piece of home, a place to speak their language and drink real coffee.\n\n"
                "The décor has barely changed. "
                "A long counter, a hissing espresso machine, photos of soccer teams and a few tightly packed tables. "
                "The same family still runs the place, and regulars greet each other by first name.\n\n"
                "The real show starts on match nights. "
                "When Italy plays, the room fills up, chairs spill onto the sidewalk and every goal shakes the whole neighbourhood. "
                "Even without a game, take a moment for an espresso standing at the bar, Italian style, "
                "before strolling over to the Jean-Talon Market, just a few blocks away."
            ),
            "es": (
                "Sobre el bulevar Saint-Laurent, en el corazón de la Pequeña Italia, el Caffè Italia sirve el mismo espresso desde 1956. "
                "En aquella época recibía a la gran ola de inmigrantes italianos que llegaron a Montreal después de la guerra. "
                "Para ellos era un pedazo de su tierra, un lugar para hablar su idioma y tomar un café de verdad.\n\n"
                "La decoración casi no ha cambiado. "
                "Un largo mostrador, una cafetera que silba, fotos de equipos de fútbol y unas cuantas mesas muy juntas. "
                "La misma familia sigue al frente del negocio, y los clientes de siempre se saludan por su nombre.\n\n"
                "El verdadero espectáculo empieza las noches de partido. "
                "Cuando juega Italia, el local se llena, las sillas salen a la acera y cada gol hace vibrar al barrio entero. "
                "Aun sin partido, tómese un espresso de pie en la barra, al estilo italiano, "
                "antes de caminar hasta el mercado Jean-Talon, a pocas cuadras."
            ),
        },
        "conseil": {
            "fr": "Consultez le calendrier de l'équipe d'Italie : un soir de grand match, arrivez tôt pour avoir une place.",
            "en": "Check Italy's match schedule: on a big game night, come early to get a spot.",
            "es": "Revise el calendario de la selección italiana: en noche de gran partido, llegue temprano.",
        },
        "commander": {
            "fr": "Un espresso bu debout au comptoir, à l'italienne. Au comptoir : « Un espresso, s'il vous plaît. »",
            "en": "An espresso, drunk standing at the bar, Italian style. At the counter: \"Un espresso, s'il vous plaît.\"",
            "es": "Un espresso tomado de pie en la barra, al estilo italiano. En el mostrador: « Un espresso, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "Après la victoire de l'Italie à la Coupe du monde de 2006, le boulevard Saint-Laurent a été envahi de drapeaux jusqu'au petit matin.",
            "en": "When Italy won the 2006 World Cup, Saint-Laurent Boulevard filled with flags and car horns until dawn.",
            "es": "Cuando Italia ganó el Mundial de 2006, el bulevar Saint-Laurent se llenó de banderas y bocinas hasta el amanecer.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "santropol",
        "cat": "boire",
        "quartier": "Plateau-Mont-Royal",
        "metro": "Mont-Royal",
        "adresse": "3990, rue Saint-Urbain",
        "geo": (45.5156, -73.5805),
        "duree": 60,
        "nom": {
            "fr": "Café Santropol",
            "en": "Café Santropol",
            "es": "Café Santropol",
        },
        "bref": {
            "fr": "Un jardin secret derrière une façade de briques, et des sandwichs de géant.",
            "en": "A secret garden behind a brick façade, and giant sandwiches.",
            "es": "Un jardín secreto detrás de una fachada de ladrillo, y sándwiches gigantes.",
        },
        "texte": {
            "fr": (
                "Au coin des rues Saint-Urbain et Duluth, une maison de briques un peu bohème cache un secret. "
                "Le Café Santropol est ouvert depuis 1976. "
                "Son histoire commence avec une bonne cause : ses fondateurs voulaient sauver l'édifice de la démolition, et ils y ont installé un café.\n\n"
                "À l'intérieur, les chaises sont dépareillées, les murs colorés, et l'atmosphère rappelle un salon d'étudiants. "
                "Mais c'est à l'arrière que le charme opère. "
                "Un jardin plein d'arbres, de fleurs et de petites fontaines forme une oasis de verdure, loin du bruit de la ville. "
                "Aux beaux jours, c'est l'une des terrasses les plus douces du Plateau.\n\n"
                "La maison est réputée pour ses sandwichs très épais, préparés sur du pain maison et garnis de fromage à la crème, de fruits ou de légumes. "
                "On y trouve aussi des soupes, du chili et un grand choix de thés. "
                "Les options végétariennes y sont nombreuses, et on peut partager sans gêne."
            ),
            "en": (
                "At the corner of Saint-Urbain and Duluth, a slightly bohemian brick house hides a secret. "
                "Café Santropol has been open since 1976. "
                "It all began with a good cause: its founders wanted to save the building from demolition, so they opened a café inside.\n\n"
                "Indoors, the chairs are mismatched, the walls are colourful, and the mood feels like a student living room. "
                "The real magic, though, is out back. "
                "A garden full of trees, flowers and little fountains creates a green oasis, far from the noise of the city. "
                "On a sunny day, it is one of the gentlest terraces on the Plateau.\n\n"
                "The house is famous for its towering sandwiches, built on homemade bread and filled with cream cheese, fruit or vegetables. "
                "There are also soups, chili and a long list of teas. "
                "Vegetarians have plenty of choice, and sharing a sandwich is perfectly acceptable."
            ),
            "es": (
                "En la esquina de las calles Saint-Urbain y Duluth, una casa de ladrillo algo bohemia esconde un secreto. "
                "El Café Santropol abrió en 1976. "
                "Su historia empieza con una buena causa: sus fundadores querían salvar el edificio de la demolición, y decidieron abrir un café en él.\n\n"
                "Adentro, las sillas no combinan, las paredes son de colores y el ambiente recuerda a una sala de estudiantes. "
                "Pero la verdadera magia está en la parte de atrás. "
                "Un jardín lleno de árboles, flores y pequeñas fuentes forma un oasis verde, lejos del ruido de la ciudad. "
                "En los días soleados, es una de las terrazas más apacibles del Plateau.\n\n"
                "La casa es famosa por sus sándwiches altísimos, hechos con pan casero y rellenos de queso crema, frutas o verduras. "
                "También hay sopas, chili y una larga lista de tés. "
                "Las opciones vegetarianas abundan, y compartir un sándwich es de lo más normal."
            ),
        },
        "conseil": {
            "fr": "Demandez tout de suite une table au jardin, même s'il faut attendre un peu. Un sandwich suffit largement pour deux appétits moyens.",
            "en": "Ask for a garden table right away, even if it means a short wait. One sandwich easily feeds two moderate appetites.",
            "es": "Pida de inmediato una mesa en el jardín, aunque tenga que esperar un poco. Un sándwich alcanza para dos personas sin mucha hambre.",
        },
        "commander": {
            "fr": "Un sandwich au fromage à la crème, à partager, avec un thé. Au serveur : « Une table au jardin, s'il vous plaît, pour deux. »",
            "en": "A cream cheese sandwich to share, with a pot of tea. Ask the host: \"Une table au jardin, s'il vous plaît, pour deux.\"",
            "es": "Un sándwich de queso crema para compartir, con un té. Pida: « Une table au jardin, s'il vous plaît, pour deux. »",
        },
        "anecdote": {
            "fr": "Le café a donné naissance à Santropol Roulant, un organisme qui livre des repas à des personnes âgées en perte d'autonomie.",
            "en": "The café gave rise to Santropol Roulant, a non-profit that delivers meals to seniors and people with reduced mobility.",
            "es": "Del café nació Santropol Roulant, una organización sin fines de lucro que lleva comidas a personas mayores.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------
    {
        "id": "dieu-du-ciel",
        "cat": "boire",
        "quartier": "Plateau-Mont-Royal",
        "metro": "Laurier",
        "adresse": "29, avenue Laurier Ouest",
        "geo": (45.5226, -73.5934),
        "duree": 90,
        "nom": {
            "fr": "Dieu du Ciel!",
            "en": "Dieu du Ciel!",
            "es": "Dieu du Ciel!",
        },
        "bref": {
            "fr": "La microbrasserie culte de Montréal, où chaque bière est brassée sur place.",
            "en": "Montreal's cult brewpub, where every beer is brewed on site.",
            "es": "La cervecería artesanal de culto de Montreal, donde todo se elabora en casa.",
        },
        "texte": {
            "fr": (
                "Le Québec est l'un des endroits les plus vivants d'Amérique du Nord pour la bière artisanale. "
                "Depuis les années quatre-vingt, des centaines de microbrasseries ont ouvert dans la province, "
                "des grandes villes jusqu'aux petits villages, et chaque région a désormais ses bières locales.\n\n"
                "À Montréal, Dieu du Ciel! est l'une des pionnières. "
                "Ce broue-pub, c'est-à-dire un bar qui brasse lui-même ce qu'il sert, a ouvert en 1998 sur l'avenue Laurier. "
                "Le succès a été tel qu'une usine a ensuite été construite à Saint-Jérôme, au nord de la ville. "
                "Mais c'est ici, dans cette salle chaleureuse et souvent bondée, que tout se goûte en premier.\n\n"
                "Le menu change au fil des saisons. "
                "On y trouve des bières légères, des bières acidulées, des blanches parfumées et des stouts très sombres. "
                "Si vous hésitez, demandez conseil : le personnel adore guider les curieux, et une planche de dégustation permet de tout essayer."
            ),
            "en": (
                "Quebec is one of the liveliest places in North America for craft beer. "
                "Since the nineteen eighties, hundreds of microbreweries have opened across the province, "
                "from big cities to tiny villages, and every region now has beers of its own.\n\n"
                "In Montreal, Dieu du Ciel! is one of the pioneers. "
                "This brewpub, or broue-pub as Quebecers say, opened on Laurier Avenue in 1998 and brews everything it pours. "
                "It became so popular that a full brewery was later built in Saint-Jérôme, north of the city. "
                "Still, this warm and often crowded room is where every new beer is tasted first.\n\n"
                "The menu changes with the seasons. "
                "You will find light ales, tart sour beers, fragrant wheat beers and stouts as dark as night. "
                "If you are unsure, just ask: the staff love guiding curious drinkers, and a tasting flight lets you try a little of everything."
            ),
            "es": (
                "Quebec es uno de los lugares más vivos de América del Norte para la cerveza artesanal. "
                "Desde los años ochenta, cientos de microcervecerías han abierto en la provincia, "
                "desde las grandes ciudades hasta los pueblos más pequeños, y cada región tiene ya sus propias cervezas.\n\n"
                "En Montreal, Dieu du Ciel! es una de las pioneras. "
                "Este brewpub, o broue-pub como dicen los quebequenses, abrió en la avenida Laurier en 1998 y elabora todo lo que sirve. "
                "Tuvo tanto éxito que más tarde construyó una fábrica en Saint-Jérôme, al norte de la ciudad. "
                "Aun así, en este salón cálido y casi siempre lleno es donde cada nueva cerveza se prueba primero.\n\n"
                "La carta cambia con las estaciones. "
                "Hay cervezas ligeras, cervezas ácidas, cervezas de trigo aromáticas y stouts oscurísimas. "
                "Si duda, pida consejo: al personal le encanta orientar a los curiosos, y una tabla de degustación permite probar un poco de todo."
            ),
        },
        "conseil": {
            "fr": "Le bar ne prend pas de réservation et se remplit vite en soirée : venez en fin d'après-midi. Les bières sont souvent fortes, prenez des demi-pintes.",
            "en": "No reservations, and it fills up fast at night: come in the late afternoon. Many beers are strong, so order half pints.",
            "es": "No aceptan reservaciones y se llena rápido por la noche: venga al final de la tarde. Muchas cervezas son fuertes; pida medias pintas.",
        },
        "commander": {
            "fr": "La Péché Mortel, stout au café devenue célèbre, ou la Rosée d'hibiscus, rafraîchissante. Au bar : « Une planche de dégustation, s'il vous plaît. »",
            "en": "Péché Mortel, the famous coffee stout, or the refreshing Rosée d'hibiscus. At the bar: \"Une planche de dégustation, s'il vous plaît.\"",
            "es": "La Péché Mortel, famosa stout de café, o la refrescante Rosée d'hibiscus. En la barra: « Une planche de dégustation, s'il vous plaît. »",
        },
        "anecdote": {
            "fr": "La Péché Mortel, une stout impériale au café, figure depuis des années parmi les bières les mieux notées au monde par les amateurs.",
            "en": "Péché Mortel, an imperial coffee stout, has ranked for years among the world's top-rated beers on enthusiast sites.",
            "es": "La Péché Mortel, una stout imperial de café, figura desde hace años entre las cervezas mejor valoradas del mundo por los aficionados.",
        },
        "verifier": [],
    },
]
