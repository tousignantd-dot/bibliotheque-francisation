# -*- coding: utf-8 -*-
"""Guide de Montréal — lieux, lot 1 (cat = « voir »). Voir FORMAT.md."""

LIEUX = [
    # ------------------------------------------------------------------ 1
    {
        "id": "vieux-port",
        "cat": "voir",
        "quartier": "Vieux-Montréal",
        "metro": "Champ-de-Mars",
        "adresse": "333, rue de la Commune Ouest",
        "geo": (45.5075, -73.5510),
        "duree": 90,
        "nom": {
            "fr": "Vieux-Port de Montréal",
            "en": "Old Port of Montreal",
            "es": "Viejo Puerto de Montreal",
        },
        "bref": {
            "fr": "Des kilomètres de quais au bord du fleuve, entre grande roue et tour de l'Horloge.",
            "en": "Kilometres of waterfront quays, from the Ferris wheel to the Clock Tower.",
            "es": "Kilómetros de muelles junto al río, entre la noria y la Torre del Reloj.",
        },
        "texte": {
            "fr": (
                "Le Vieux-Port s'étire sur plus de deux kilomètres le long du fleuve Saint-Laurent, au pied du Vieux-Montréal. "
                "Pendant trois siècles, la ville a vécu d'ici : les navires, les entrepôts, les silos à grain, les débardeurs. "
                "Quand le trafic maritime a glissé vers l'est, les vieux quais ont été rendus aux promeneurs, et l'endroit est devenu le grand balcon des Montréalais sur l'eau."
                "\n\n"
                "À l'extrémité est se dresse la tour de l'Horloge, inaugurée en 1922 à la mémoire des marins morts pendant la Première Guerre mondiale. "
                "À la belle saison, vous pouvez grimper ses marches pour une vue sur le pont Jacques-Cartier et les îles. "
                "Plus à l'ouest, la Grande roue offre des nacelles fermées et chauffées, qui tournent même en plein hiver."
                "\n\n"
                "Le port change de visage avec les saisons. "
                "L'été, on loue un vélo, on s'allonge sur le sable de la plage de l'Horloge ou on embarque pour une croisière. "
                "L'hiver, une patinoire s'installe entre les quais, avec la ville illuminée en toile de fond."
            ),
            "en": (
                "The Old Port stretches for more than two kilometres along the St. Lawrence River, at the foot of Old Montreal. "
                "For three centuries, this is where the city made its living: ships, warehouses, grain elevators and dockworkers. "
                "When shipping moved east, the old quays were handed back to the public, and the waterfront became Montreal's favourite front porch."
                "\n\n"
                "At the eastern tip stands the Clock Tower, opened in 1922 to honour the sailors lost in the First World War. "
                "In the warmer months, you can climb its stairs for a view of the Jacques Cartier Bridge and the islands. "
                "Farther west, the big Ferris wheel, La Grande roue, has closed, heated gondolas, so it keeps turning even in the depths of winter."
                "\n\n"
                "The port changes with the seasons. "
                "In summer, rent a bike, stretch out on the sand at Clock Tower Beach, or hop on a river cruise. "
                "In winter, a skating rink appears between the quays, with the lit-up skyline as a backdrop."
            ),
            "es": (
                "El Viejo Puerto se extiende por más de dos kilómetros a lo largo del río San Lorenzo, al pie del Viejo Montreal. "
                "Durante tres siglos, la ciudad vivió de este lugar: barcos, almacenes, silos de granos y estibadores. "
                "Cuando los barcos se mudaron al este, los muelles se abrieron al público y se volvieron el gran balcón de la ciudad sobre el agua."
                "\n\n"
                "En el extremo este se levanta la Torre del Reloj, inaugurada en 1922 en memoria de los marinos que murieron en la Primera Guerra Mundial. "
                "En temporada cálida, puede subir sus escaleras para ver el puente Jacques-Cartier y las islas. "
                "Más al oeste, la gran noria, La Grande roue, tiene cabinas cerradas y con calefacción, así que gira incluso en pleno invierno."
                "\n\n"
                "El puerto cambia con las estaciones. "
                "En verano, alquile una bicicleta, tiéndase en la playa del Reloj o suba a un crucero. "
                "En invierno, una pista de patinaje aparece entre los muelles, con la ciudad iluminada de fondo."
            ),
        },
        "conseil": {
            "fr": "Venez au coucher du soleil et marchez jusqu'au bout du quai de l'Horloge : c'est la plus belle vue sur le pont Jacques-Cartier illuminé.",
            "en": "Come at sunset and walk to the end of the Clock Tower Quay: it has the best view of the Jacques Cartier Bridge when it lights up.",
            "es": "Venga al atardecer y camine hasta el final del muelle del Reloj: desde ahí se tiene la mejor vista del puente Jacques-Cartier iluminado.",
        },
        "anecdote": {
            "fr": "La tour de l'Horloge a longtemps donné l'heure aux travailleurs du port ; son mécanisme a été fabriqué en Angleterre.",
            "en": "For decades, the Clock Tower kept time for the people who worked in the port; its mechanism was made in England.",
            "es": "Durante décadas, la Torre del Reloj marcó la hora de quienes trabajaban en el puerto; su mecanismo se fabricó en Inglaterra.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 2
    {
        "id": "notre-dame",
        "cat": "voir",
        "quartier": "Vieux-Montréal",
        "metro": "Place-d'Armes",
        "adresse": "110, rue Notre-Dame Ouest",
        "geo": (45.5045, -73.5563),
        "duree": 60,
        "nom": {
            "fr": "Basilique Notre-Dame",
            "en": "Notre-Dame Basilica",
            "es": "Basílica de Notre-Dame",
        },
        "bref": {
            "fr": "Une voûte bleu nuit semée d'étoiles d'or, au-dessus de la place d'Armes.",
            "en": "A midnight-blue vault sprinkled with gold stars, right on Place d'Armes.",
            "es": "Una bóveda azul noche salpicada de estrellas doradas, frente a la Place d'Armes.",
        },
        "texte": {
            "fr": (
                "De l'extérieur, la basilique Notre-Dame a l'air sévère avec ses deux tours de pierre grise qui dominent la place d'Armes. "
                "Poussez la porte, et le contraste vous saisit : une voûte bleu profond constellée d'étoiles dorées, des boiseries sculptées partout, une lumière qui tombe en douceur sur l'autel."
                "\n\n"
                "L'église a été construite à partir de 1824 selon les plans de James O'Donnell, un architecte irlandais venu de New York. "
                "Protestant, il s'est converti au catholicisme avant de mourir, et il repose aujourd'hui dans la crypte de son chef-d'œuvre. "
                "Le décor intérieur, plus tardif, est l'œuvre de Victor Bourgeau. "
                "Au fond, l'orgue Casavant compte des milliers de tuyaux et fait vibrer toute la nef."
                "\n\n"
                "Notre-Dame reste une église vivante, où l'on célèbre messes, mariages et funérailles nationales. "
                "Le soir, le spectacle immersif « Aura » transforme la nef en tableau de lumière et de musique. "
                "Le jour, la visite est payante, mais elle vaut largement le détour."
            ),
            "en": (
                "From the outside, Notre-Dame Basilica looks stern, its two grey stone towers looming over Place d'Armes. "
                "Step through the doors, though, and the contrast is stunning: a deep blue vault scattered with golden stars, carved wood on every surface, and soft light pooling over the altar."
                "\n\n"
                "Construction began in 1824, following plans by James O'Donnell, an Irish-born architect who came up from New York. "
                "He was a Protestant, yet he converted to Catholicism before he died, and he is buried in the crypt of his own masterpiece. "
                "The lavish interior came later, designed by Victor Bourgeau. "
                "At the back, the great Casavant organ has thousands of pipes and can make the whole nave tremble."
                "\n\n"
                "Notre-Dame is still a working church, hosting masses, weddings and state funerals. "
                "In the evening, the immersive show called “Aura” turns the nave into a canvas of light and music. "
                "Daytime visits require a ticket, and they are well worth it."
            ),
            "es": (
                "Desde afuera, la basílica de Notre-Dame parece austera, con sus dos torres de piedra gris que dominan la Place d'Armes. "
                "Pero al cruzar la puerta, el contraste lo deja sin aliento: una bóveda de azul profundo cubierta de estrellas doradas, madera tallada por todas partes y una luz suave que cae sobre el altar."
                "\n\n"
                "La construcción empezó en 1824, según los planos de James O'Donnell, un arquitecto irlandés que llegó desde Nueva York. "
                "Era protestante, pero se convirtió al catolicismo antes de morir, y hoy descansa en la cripta de su obra maestra. "
                "La rica decoración interior llegó después, diseñada por Victor Bourgeau. "
                "Al fondo, el gran órgano Casavant tiene miles de tubos y hace vibrar toda la nave."
                "\n\n"
                "Notre-Dame sigue siendo una iglesia en uso, con misas, bodas y funerales de Estado. "
                "Por la noche, el espectáculo inmersivo «Aura» convierte la nave en un cuadro de luz y música. "
                "De día, la visita tiene costo, y vale mucho la pena."
            ),
        },
        "conseil": {
            "fr": "Faites le tour jusqu'à la chapelle du Sacré-Cœur, derrière le chœur : beaucoup de visiteurs la manquent, et son retable de bronze est saisissant.",
            "en": "Head behind the main altar to the Sacred Heart Chapel: many visitors miss it, and its huge bronze altarpiece is striking.",
            "es": "Vaya detrás del altar mayor hasta la capilla del Sagrado Corazón: muchos visitantes no la ven, y su enorme retablo de bronce impresiona.",
        },
        "anecdote": {
            "fr": "Céline Dion s'y est mariée en 1994, devant une foule massée sur la place d'Armes.",
            "en": "Céline Dion was married here in 1994, with crowds packing Place d'Armes outside.",
            "es": "Céline Dion se casó aquí en 1994, con una multitud reunida afuera en la Place d'Armes.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 3
    {
        "id": "place-jacques-cartier",
        "cat": "voir",
        "quartier": "Vieux-Montréal",
        "metro": "Champ-de-Mars",
        "adresse": "Place Jacques-Cartier",
        "geo": (45.5078, -73.5536),
        "duree": 60,
        "nom": {
            "fr": "Place Jacques-Cartier et rue Saint-Paul",
            "en": "Place Jacques-Cartier and Rue Saint-Paul",
            "es": "Place Jacques-Cartier y rue Saint-Paul",
        },
        "bref": {
            "fr": "Le cœur battant du Vieux-Montréal : pavés, terrasses, artistes de rue et hôtel de ville.",
            "en": "The beating heart of Old Montreal: cobblestones, patios, street performers and City Hall.",
            "es": "El corazón del Viejo Montreal: adoquines, terrazas, artistas callejeros y el ayuntamiento.",
        },
        "texte": {
            "fr": (
                "La place Jacques-Cartier descend en pente douce de la rue Notre-Dame jusqu'au fleuve. "
                "C'était autrefois un marché public, où les fermiers venaient vendre leurs légumes. "
                "Aujourd'hui, les terrasses débordent sur les pavés, les amuseurs de rue attirent les attroupements et les fleuristes colorent l'été."
                "\n\n"
                "En haut de la place, la colonne Nelson est le plus vieux monument de Montréal. "
                "Juste en face se dresse l'hôtel de ville, un édifice de style Second Empire. "
                "C'est de son balcon, en 1967, que le général de Gaulle a lancé son célèbre « Vive le Québec libre », une phrase qui a fait le tour du monde."
                "\n\n"
                "Au bas de la place, tournez dans la rue Saint-Paul, l'une des plus anciennes de la ville. "
                "Elle file entre des façades de pierre, des galeries d'art et des boutiques d'artisans. "
                "Suivez-la vers l'est jusqu'au marché Bonsecours, reconnaissable à son dôme argenté, puis jusqu'à la petite chapelle des marins."
            ),
            "en": (
                "Place Jacques-Cartier slopes gently down from Notre-Dame Street to the river. "
                "It started out as a public market, where farmers came to sell their vegetables. "
                "Today, café patios spill onto the cobblestones, street performers gather crowds, and flower sellers brighten the summer."
                "\n\n"
                "At the top of the square, Nelson's Column is the oldest monument in Montreal. "
                "Right across the street stands City Hall, a grand building in the Second Empire style. "
                "It was from its balcony, in 1967, that French president Charles de Gaulle called out “Vive le Québec libre”, long live free Quebec, a phrase that made headlines around the world."
                "\n\n"
                "At the bottom of the square, turn onto Rue Saint-Paul, one of the oldest streets in the city. "
                "It winds between stone facades, art galleries and craft shops. "
                "Follow it east to Bonsecours Market, easy to spot with its silver dome, and on to the little sailors' chapel beyond."
            ),
            "es": (
                "La Place Jacques-Cartier baja en suave pendiente desde la calle Notre-Dame hasta el río. "
                "Antiguamente era un mercado público, donde los agricultores venían a vender sus verduras. "
                "Hoy, las terrazas invaden los adoquines, los artistas callejeros reúnen a los curiosos y los puestos de flores llenan de color el verano."
                "\n\n"
                "En lo alto de la plaza, la columna de Nelson es el monumento más antiguo de Montreal. "
                "Justo enfrente se alza el ayuntamiento, un gran edificio de estilo Segundo Imperio. "
                "Desde su balcón, en 1967, el general francés Charles de Gaulle lanzó su famoso «Vive le Québec libre», viva el Quebec libre, una frase que dio la vuelta al mundo."
                "\n\n"
                "Al pie de la plaza, tome la rue Saint-Paul, una de las calles más antiguas de la ciudad. "
                "Pasa entre fachadas de piedra, galerías de arte y tiendas de artesanos. "
                "Sígala hacia el este hasta el Mercado Bonsecours, fácil de reconocer por su cúpula plateada, y luego hasta la pequeña capilla de los marineros."
            ),
        },
        "conseil": {
            "fr": "Fuyez les restaurants de la place elle-même : marchez deux rues vers l'ouest, rue Saint-Paul ou rue Saint-Vincent, pour mieux manger au calme.",
            "en": "Skip the restaurants right on the square: walk a couple of blocks west along Rue Saint-Paul for better food and fewer crowds.",
            "es": "Evite los restaurantes de la plaza misma: camine un par de cuadras hacia el oeste por la rue Saint-Paul y comerá mejor, con menos gente.",
        },
        "anecdote": {
            "fr": "La colonne Nelson, érigée en 1809, est plus ancienne que la célèbre colonne Nelson de Trafalgar Square, à Londres.",
            "en": "Montreal's Nelson's Column, raised in 1809, is older than the famous one in London's Trafalgar Square.",
            "es": "La columna de Nelson de Montreal, levantada en 1809, es más antigua que la famosa de Trafalgar Square, en Londres.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 4
    {
        "id": "pointe-a-calliere",
        "cat": "voir",
        "quartier": "Vieux-Montréal",
        "metro": "Place-d'Armes",
        "adresse": "350, place Royale",
        "geo": (45.5027, -73.5543),
        "duree": 120,
        "nom": {
            "fr": "Pointe-à-Callière, cité d'archéologie et d'histoire de Montréal",
            "en": "Pointe-à-Callière, Montréal Archaeology and History Complex",
            "es": "Pointe-à-Callière, museo de arqueología e historia de Montreal",
        },
        "bref": {
            "fr": "Descendez sous la ville, à l'endroit exact où Montréal est née en 1642.",
            "en": "Go underground to the very spot where Montreal was founded in 1642.",
            "es": "Baje bajo la ciudad, al lugar exacto donde nació Montreal en 1642.",
        },
        "texte": {
            "fr": (
                "C'est ici, sur une pointe de terre entre le fleuve et une petite rivière, que Paul de Chomedey de Maisonneuve et Jeanne Mance ont fondé Ville-Marie, au printemps de 1642. "
                "Le musée a été construit sur ce lieu même, et il vous fait descendre, littéralement, dans les couches de l'histoire."
                "\n\n"
                "Sous vos pieds, les archéologues ont mis au jour les vestiges du premier cimetière catholique de la ville, des fondations de maisons, un ancien marché et un grand égout collecteur en pierre, que l'on parcourt aujourd'hui à pied. "
                "Les parcours souterrains relient plusieurs bâtiments, et chaque salle ajoute un siècle au récit."
                "\n\n"
                "Pointe-à-Callière raconte aussi ceux qui étaient là avant : les peuples autochtones, qui fréquentaient le site depuis très longtemps pour le commerce et la pêche. "
                "Si la tour d'observation du pavillon principal est ouverte, montez-y : elle offre une vue dégagée sur le Vieux-Port. "
                "Prévoyez du temps, surtout si une grande exposition temporaire est à l'affiche."
            ),
            "en": (
                "Right here, on a point of land between the river and a small stream, Paul de Chomedey de Maisonneuve and Jeanne Mance founded the settlement of Ville-Marie in the spring of 1642. "
                "The museum was built on that very spot, and it takes you down, quite literally, through the layers of history."
                "\n\n"
                "Beneath your feet, archaeologists uncovered the remains of the city's first Catholic cemetery, the foundations of early houses, an old marketplace and a large stone sewer that visitors can now walk through. "
                "Underground passages link several buildings, and each room adds another century to the story."
                "\n\n"
                "Pointe-à-Callière also tells the story of the people who came first: Indigenous nations who had gathered here to trade and fish for a very long time. "
                "If the observation tower in the main building is open, head up for a wide view over the Old Port. "
                "Give yourself plenty of time, especially when a major temporary exhibition is on."
            ),
            "es": (
                "Justo aquí, en una punta de tierra entre el río y un pequeño arroyo, Paul de Chomedey de Maisonneuve y Jeanne Mance fundaron Ville-Marie en la primavera de 1642. "
                "El museo se construyó en ese mismo lugar, y lo lleva a usted a bajar, literalmente, por las capas de la historia."
                "\n\n"
                "Bajo sus pies, los arqueólogos descubrieron los restos del primer cementerio católico de la ciudad, cimientos de casas antiguas, un viejo mercado y una gran alcantarilla de piedra que hoy se recorre a pie. "
                "Pasajes subterráneos conectan varios edificios, y cada sala suma un siglo más al relato."
                "\n\n"
                "Pointe-à-Callière también cuenta la historia de quienes estaban antes: los pueblos indígenas, que desde hacía mucho tiempo se reunían aquí para comerciar y pescar. "
                "Si la torre de observación del edificio principal está abierta, suba para disfrutar de una amplia vista del Viejo Puerto. "
                "Reserve bastante tiempo, sobre todo si hay una gran exposición temporal."
            ),
        },
        "conseil": {
            "fr": "Commencez par le spectacle multimédia de présentation : il donne les repères qui rendent la visite souterraine bien plus parlante.",
            "en": "Start with the introductory multimedia show: it gives you the landmarks that make the underground tour much more meaningful.",
            "es": "Empiece por el espectáculo multimedia de presentación: le da las claves para que el recorrido subterráneo tenga mucho más sentido.",
        },
        "anecdote": {
            "fr": "Le musée a ouvert en 1992, pour le trois cent cinquantième anniversaire de la fondation de Montréal.",
            "en": "The museum opened in 1992, for Montreal's three hundred and fiftieth birthday.",
            "es": "El museo abrió en 1992, para el tricentésimo quincuagésimo aniversario de la fundación de Montreal.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 5
    {
        "id": "mont-royal",
        "cat": "voir",
        "quartier": "Ville-Marie",
        "metro": "Mont-Royal",
        "adresse": "1196, voie Camillien-Houde",
        "geo": (45.5035, -73.5873),
        "duree": 150,
        "nom": {
            "fr": "Parc du Mont-Royal",
            "en": "Mount Royal Park",
            "es": "Parque del Monte Real",
        },
        "bref": {
            "fr": "La montagne au milieu de la ville, et la plus belle vue sur Montréal depuis le belvédère.",
            "en": "The mountain in the middle of the city, with the best view of Montreal from its lookout.",
            "es": "La montaña en medio de la ciudad, con la mejor vista de Montreal desde su mirador.",
        },
        "texte": {
            "fr": (
                "Les Montréalais l'appellent simplement « la montagne ». "
                "Le parc du Mont-Royal a été dessiné par Frederick Law Olmsted, le paysagiste de Central Park, à New York. "
                "Il voulait qu'on y monte lentement, par des chemins en lacets, pour découvrir la ville peu à peu, comme une récompense."
                "\n\n"
                "Au sommet, le belvédère Kondiaronk offre la vue la plus célèbre de Montréal : les gratte-ciel du centre-ville, le fleuve, et par temps clair, les collines au loin. "
                "Il porte le nom d'un grand chef wendat, l'un des artisans de la Grande Paix de Montréal, signée en 1701. "
                "Juste derrière, le chalet du Mont-Royal, avec ses grandes fenêtres et ses tableaux d'histoire, invite à une pause."
                "\n\n"
                "Un peu plus loin, la croix du mont Royal s'illumine chaque soir. "
                "Elle rappelle celle que Maisonneuve avait plantée ici en 1643, pour remercier le ciel d'avoir épargné la colonie d'une inondation. "
                "Le dimanche d'été, au pied de la montagne, les tam-tams font danser la foule."
            ),
            "en": (
                "Montrealers simply call it “the mountain”. "
                "Mount Royal Park was designed by Frederick Law Olmsted, the landscape architect behind New York's Central Park. "
                "He wanted people to climb it slowly, along winding paths, so the city would reveal itself bit by bit, like a reward."
                "\n\n"
                "At the top, the Kondiaronk Lookout offers Montreal's most famous view: the downtown towers, the river and, on a clear day, the hills far beyond. "
                "It is named after a great Wendat chief who helped bring about the Great Peace of Montreal, signed in 1701. "
                "Right behind it, the Mount Royal Chalet, with its tall windows and historical paintings, is a fine place to catch your breath."
                "\n\n"
                "A little farther on, the Mount Royal Cross lights up every night. "
                "It recalls the wooden cross that Maisonneuve planted here in 1643 to give thanks after the young colony was spared from a flood. "
                "On summer Sundays, down at the foot of the mountain, the tam-tam drum circle gets the crowd dancing."
            ),
            "es": (
                "Los montrealeses la llaman simplemente «la montaña». "
                "El parque del Monte Real fue diseñado por Frederick Law Olmsted, el paisajista del Central Park de Nueva York. "
                "Quería que la gente subiera despacio, por caminos en zigzag, para ir descubriendo la ciudad poco a poco, como una recompensa."
                "\n\n"
                "En la cima, el mirador Kondiaronk ofrece la vista más famosa de Montreal: los rascacielos del centro, el río y, en días despejados, las colinas a lo lejos. "
                "Lleva el nombre de un gran jefe wendat, uno de los artífices de la Gran Paz de Montreal, firmada en 1701. "
                "Justo detrás, el chalet del Monte Real, con sus ventanales y sus pinturas históricas, invita a hacer una pausa."
                "\n\n"
                "Un poco más allá, la cruz del Monte Real se ilumina cada noche. "
                "Recuerda la que Maisonneuve plantó aquí en 1643 para dar gracias porque la joven colonia se había salvado de una inundación. "
                "Los domingos de verano, al pie de la montaña, los tambores del tam-tam ponen a bailar a la gente."
            ),
        },
        "conseil": {
            "fr": "Pour monter à pied depuis le centre-ville, prenez l'escalier au bout de la rue Peel : une vingtaine de minutes d'effort, et vous arrivez directement au belvédère.",
            "en": "To walk up from downtown, take the stairs at the top of Peel Street: about twenty minutes of effort and you come out right at the lookout.",
            "es": "Para subir a pie desde el centro, tome las escaleras al final de la calle Peel: unos veinte minutos de esfuerzo y llega directo al mirador.",
        },
        "anecdote": {
            "fr": "Un règlement municipal interdit, en principe, de construire au centre-ville un édifice plus haut que le sommet du mont Royal.",
            "en": "A city bylaw has long kept downtown skyscrapers from rising higher than the summit of Mount Royal.",
            "es": "Una norma municipal impide, en principio, que los rascacielos del centro superen la altura de la cima del Monte Real.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 6
    {
        "id": "oratoire",
        "cat": "voir",
        "quartier": "Côte-des-Neiges–Notre-Dame-de-Grâce",
        "metro": "Côte-des-Neiges",
        "adresse": "3800, chemin Queen-Mary",
        "geo": (45.4921, -73.6180),
        "duree": 90,
        "nom": {
            "fr": "Oratoire Saint-Joseph du Mont-Royal",
            "en": "Saint Joseph's Oratory of Mount Royal",
            "es": "Oratorio de San José del Monte Real",
        },
        "bref": {
            "fr": "Un dôme immense sur le flanc de la montagne, né de la ferveur d'un humble portier.",
            "en": "A vast dome on the mountainside, born from the faith of a humble doorkeeper.",
            "es": "Una cúpula inmensa en la ladera de la montaña, nacida de la fe de un humilde portero.",
        },
        "texte": {
            "fr": (
                "Tout commence avec un homme modeste : le frère André, portier d'un collège voisin, à qui l'on attribuait des guérisons. "
                "Au début du vingtième siècle, il fait bâtir une petite chapelle de bois sur le flanc de la montagne. "
                "Les pèlerins affluent, et de chapelle en crypte, le projet devient l'une des plus grandes églises du monde."
                "\n\n"
                "La basilique, coiffée d'un dôme de cuivre vert visible de loin, a pris plus de quarante ans à achever. "
                "À l'intérieur, l'espace est vaste et dépouillé, presque moderne. "
                "Plus bas, la crypte et la chapelle votive, tapissée de milliers de lampions et de béquilles laissées par les fidèles, sont bien plus émouvantes."
                "\n\n"
                "Le frère André a été proclamé saint en 2010, et son cœur est conservé dans un reliquaire que l'on peut voir. "
                "Devant l'Oratoire, un long escalier grimpe vers l'entrée : certains pèlerins en montent la partie centrale à genoux, en priant. "
                "Même sans être croyant, on vient ici pour la paix du lieu et la vue sur l'ouest de la ville."
            ),
            "en": (
                "It all began with a modest man: Brother André, the doorkeeper of a nearby school, who was credited with miraculous healings. "
                "In the early twentieth century, he had a small wooden chapel built on the side of the mountain. "
                "Pilgrims poured in, and step by step, the project grew into one of the largest churches in the world."
                "\n\n"
                "The basilica, crowned by a green copper dome you can spot from far away, took more than forty years to finish. "
                "Inside, the space is vast and spare, almost modern. "
                "Below, the Votive Chapel, glowing with candles and lined with crutches left by the faithful, is far more moving."
                "\n\n"
                "Brother André was declared a saint in 2010, and his heart is kept in a reliquary that visitors can see. "
                "Out front, a long staircase climbs to the entrance, and some pilgrims still go up its central steps on their knees, praying. "
                "Even if you are not religious, come for the peaceful atmosphere and the view over the west of the city."
            ),
            "es": (
                "Todo empezó con un hombre sencillo: el hermano André, portero de un colegio cercano, a quien se le atribuían curaciones milagrosas. "
                "A principios del siglo veinte, mandó construir una pequeña capilla de madera en la ladera de la montaña. "
                "Los peregrinos llegaron en masa y, poco a poco, el proyecto se convirtió en una de las iglesias más grandes del mundo."
                "\n\n"
                "La basílica, coronada por una cúpula de cobre verde que se ve desde lejos, tardó más de cuarenta años en terminarse. "
                "Por dentro, el espacio es amplio y sobrio, casi moderno. "
                "Más abajo, la capilla votiva, llena de velas y de muletas dejadas por los fieles, conmueve mucho más."
                "\n\n"
                "El hermano André fue proclamado santo en 2010, y su corazón se conserva en un relicario que se puede ver. "
                "Frente al Oratorio, una larga escalinata sube hasta la entrada, y algunos peregrinos todavía suben de rodillas los escalones centrales, rezando. "
                "Aunque no sea creyente, venga por la paz del lugar y la vista de la ciudad."
            ),
        },
        "conseil": {
            "fr": "Il y a des navettes et des ascenseurs pour éviter les marches : demandez à l'accueil, au pied de l'escalier.",
            "en": "Shuttles and elevators let you skip the stairs entirely: just ask at the welcome desk at the bottom of the steps.",
            "es": "Hay traslados y ascensores para evitar las escaleras: pregunte en la recepción, al pie de la escalinata.",
        },
        "anecdote": {
            "fr": "En 1973, le cœur du frère André a été volé ; il a été retrouvé intact plus d'un an plus tard, dans un sous-sol de la région.",
            "en": "In 1973, Brother André's heart was stolen; it turned up intact more than a year later in a basement near Montreal.",
            "es": "En 1973 robaron el corazón del hermano André; apareció intacto más de un año después, en un sótano de la región.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 7
    {
        "id": "parc-olympique",
        "cat": "voir",
        "quartier": "Mercier–Hochelaga-Maisonneuve",
        "metro": "Viau",
        "adresse": "4545, avenue Pierre-De Coubertin",
        "geo": (45.5580, -73.5518),
        "duree": 150,
        "nom": {
            "fr": "Parc olympique",
            "en": "Olympic Park",
            "es": "Parque Olímpico",
        },
        "bref": {
            "fr": "Le Stade de 1976, sa tour penchée vertigineuse et le Biodôme, sous un même toit.",
            "en": "The 1976 Olympic Stadium, its dizzying leaning tower and the Biodôme, all in one place.",
            "es": "El estadio de 1976, su vertiginosa torre inclinada y el Biodôme, en un mismo lugar.",
        },
        "texte": {
            "fr": (
                "En 1976, Montréal accueille les Jeux olympiques d'été, et l'architecte français Roger Taillibert lui dessine un stade qui ne ressemble à aucun autre. "
                "Vu du ciel, on dirait un coquillage de béton. "
                "Les Montréalais l'ont surnommé « le Big O », puis « le Big Owe », tant sa facture a mis de temps à être payée."
                "\n\n"
                "À côté du stade s'élance la tour de Montréal, la plus haute tour inclinée du monde. "
                "Elle penche à quarante-cinq degrés, et un funiculaire en remonte le dos jusqu'à un observatoire qui domine toute l'île. "
                "Fermé pour une grande rénovation, il doit rouvrir avec une nouvelle cabine vitrée : renseignez-vous avant de venir."
                "\n\n"
                "L'ancien vélodrome olympique abrite aujourd'hui le Biodôme, où l'on traverse en quelques pas plusieurs écosystèmes des Amériques : une forêt tropicale humide, une érablière laurentienne, le golfe du Saint-Laurent et des régions polaires, avec leurs manchots. "
                "Comptez une bonne demi-journée si vous voulez tout voir, et combinez la visite avec le Jardin botanique, juste en face."
            ),
            "en": (
                "In 1976, Montreal hosted the Summer Olympics, and French architect Roger Taillibert designed a stadium unlike any other. "
                "From the air, it looks like a giant concrete seashell. "
                "Locals nicknamed it “the Big O”, and later “the Big Owe”, because it took decades to pay off."
                "\n\n"
                "Next to the stadium rises the Montreal Tower, the tallest inclined tower in the world. "
                "It leans at forty-five degrees, and a funicular rides up its back to an observation deck overlooking the whole island. "
                "The deck is closed for a major renovation and is due to reopen with a new glass cabin, so check before you go."
                "\n\n"
                "The former Olympic velodrome is now home to the Biodôme, where a few steps take you through several ecosystems of the Americas: a tropical rainforest, a Laurentian maple forest, the Gulf of St. Lawrence and polar regions, complete with penguins. "
                "Allow a good half-day to see it all, and pair your visit with the Botanical Garden, right across the street."
            ),
            "es": (
                "En 1976, Montreal fue sede de los Juegos Olímpicos de verano, y el arquitecto francés Roger Taillibert diseñó un estadio distinto a todos. "
                "Visto desde el aire, parece una enorme concha de hormigón. "
                "Los montrealeses lo apodaron «Big O», y luego «Big Owe», en inglés «la gran deuda», porque tardaron décadas en pagarlo."
                "\n\n"
                "Junto al estadio se levanta la Torre de Montreal, la torre inclinada más alta del mundo. "
                "Tiene una inclinación de cuarenta y cinco grados, y un funicular sube por su lomo hasta un mirador que domina toda la isla. "
                "El mirador está cerrado por una gran renovación y reabrirá con una nueva cabina de vidrio: infórmese antes de ir."
                "\n\n"
                "El antiguo velódromo olímpico alberga hoy el Biodôme, donde en pocos pasos se recorren varios ecosistemas de las Américas: una selva tropical, un bosque de arces, el golfo del San Lorenzo y las regiones polares, con sus pingüinos. "
                "Calcule una buena media jornada para verlo todo, y combine la visita con el Jardín Botánico, justo enfrente."
            ),
        },
        "conseil": {
            "fr": "L'observatoire de la tour est fermé pour rénovation, avec une réouverture annoncée pour 2027 : vérifiez avant de venir. Au Biodôme, réservez une heure d'entrée.",
            "en": "The tower's observation deck is closed for renovation, with a reopening announced for 2027, so check before you go. For the Biodôme, book a time slot.",
            "es": "El mirador de la torre está cerrado por renovación, con reapertura anunciada para 2027: verifique antes de ir. Para el Biodôme, reserve un horario de entrada.",
        },
        "anecdote": {
            "fr": "La dette du Stade olympique n'a été entièrement remboursée qu'en 2006, trente ans après les Jeux.",
            "en": "The Olympic Stadium's debt was only fully paid off in 2006, thirty years after the Games.",
            "es": "La deuda del Estadio Olímpico recién se terminó de pagar en 2006, treinta años después de los Juegos.",
        },
        "verifier": [
            "Réouverture de l'observatoire de la tour de Montréal annoncée pour 2027 : confirmer l'état au moment de publier",
        ],
    },
    # ------------------------------------------------------------------ 8
    {
        "id": "jardin-botanique",
        "cat": "voir",
        "quartier": "Rosemont–La Petite-Patrie",
        "metro": "Pie-IX",
        "adresse": "4101, rue Sherbrooke Est",
        "geo": (45.5570, -73.5565),
        "duree": 180,
        "nom": {
            "fr": "Jardin botanique de Montréal",
            "en": "Montréal Botanical Garden",
            "es": "Jardín Botánico de Montreal",
        },
        "bref": {
            "fr": "Un jardin chinois, un jardin japonais et des insectes vivants, dans l'est de la ville.",
            "en": "A Chinese garden, a Japanese garden and live insects, in the heart of Montreal's east end.",
            "es": "Un jardín chino, un jardín japonés e insectos vivos, en pleno este de la ciudad.",
        },
        "texte": {
            "fr": (
                "Le Jardin botanique est né en 1931 de la passion du frère Marie-Victorin, un religieux botaniste qui voulait faire aimer les plantes du Québec à tout le monde. "
                "Il s'étend aujourd'hui sur des dizaines d'hectares, avec des serres d'exposition, un arboretum et une trentaine de jardins thématiques. "
                "C'est l'un des plus grands jardins botaniques du monde."
                "\n\n"
                "Deux jardins font sa renommée. "
                "Le jardin de Chine, conçu avec des artisans de Shanghai, déploie pavillons, rocailles et bassins à la manière des jardins de la dynastie Ming. "
                "Le jardin japonais, plus sobre, invite au calme avec son jardin de pierres et son pavillon de thé. "
                "À l'automne, les « Jardins de lumière » les illuminent de lanternes à la tombée du jour."
                "\n\n"
                "Sur le même terrain, l'Insectarium a été entièrement repensé : on y entre sous terre, comme un insecte, avant de rejoindre une grande volière où papillons et autres bestioles vivent en liberté. "
                "Venez tôt en journée, et portez de bonnes chaussures."
            ),
            "en": (
                "The Botanical Garden was born in 1931 from the passion of Brother Marie-Victorin, a botanist and member of a religious order who wanted everyone to fall in love with Quebec's plants. "
                "Today it covers dozens of hectares, with exhibition greenhouses, an arboretum and some thirty themed gardens. "
                "It ranks among the largest botanical gardens in the world."
                "\n\n"
                "Two gardens made its reputation. "
                "The Chinese Garden, created with craftsmen from Shanghai, unfolds pavilions, rockeries and ponds in the style of the Ming dynasty. "
                "The Japanese Garden is quieter, with a stone garden and a tea pavilion that invite you to slow down. "
                "In the fall, the “Gardens of Light” event fills them with glowing lanterns at dusk."
                "\n\n"
                "On the same grounds, the Insectarium has been completely reimagined: you enter underground, as an insect would, before reaching a large enclosure where butterflies and other creatures roam free. "
                "Come early in the day, and wear comfortable shoes."
            ),
            "es": (
                "El Jardín Botánico nació en 1931 gracias a la pasión del hermano Marie-Victorin, un religioso y botánico que quería que todo el mundo amara las plantas de Quebec. "
                "Hoy se extiende sobre decenas de hectáreas, con invernaderos de exhibición, un arboreto y una treintena de jardines temáticos. "
                "Es uno de los jardines botánicos más grandes del mundo."
                "\n\n"
                "Dos jardines le dieron su fama. "
                "El jardín chino, creado con artesanos de Shanghái, despliega pabellones, rocallas y estanques al estilo de la dinastía Ming. "
                "El jardín japonés, más sobrio, invita a la calma con su jardín de piedras y su pabellón de té. "
                "En otoño, los «Jardines de luz» los iluminan con faroles al caer la tarde."
                "\n\n"
                "En el mismo terreno, el Insectarium se renovó por completo: se entra bajo tierra, como lo haría un insecto, y luego se llega a un gran espacio donde mariposas y otros bichos viven en libertad. "
                "Venga temprano y use calzado cómodo."
            ),
        },
        "conseil": {
            "fr": "Achetez un billet combiné avec le Biodôme ou le Planétarium : les deux sont à quelques minutes de marche, de l'autre côté de la rue Sherbrooke.",
            "en": "Get a combined ticket with the Biodôme or the Planetarium: both are a few minutes' walk away, across Sherbrooke Street.",
            "es": "Compre una entrada combinada con el Biodôme o el Planetario: ambos están a pocos minutos a pie, al otro lado de la calle Sherbrooke.",
        },
        "anecdote": {
            "fr": "Le jardin de Chine a été assemblé à Montréal avec des pièces et des matériaux expédiés de Shanghai par bateau.",
            "en": "The Chinese Garden was assembled in Montreal from pieces and materials shipped over from Shanghai.",
            "es": "El jardín chino se armó en Montreal con piezas y materiales enviados en barco desde Shanghái.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 9
    {
        "id": "habitat-67",
        "cat": "voir",
        "quartier": "Ville-Marie",
        "metro": "",
        "adresse": "2600, avenue Pierre-Dupuy",
        "geo": (45.4997, -73.5434),
        "duree": 45,
        "nom": {
            "fr": "Habitat 67",
            "en": "Habitat 67",
            "es": "Habitat 67",
        },
        "bref": {
            "fr": "Des cubes de béton empilés comme un jeu de construction, face au Vieux-Port.",
            "en": "Concrete cubes stacked like building blocks, facing the Old Port.",
            "es": "Cubos de hormigón apilados como un juego de construcción, frente al Viejo Puerto.",
        },
        "texte": {
            "fr": (
                "Habitat 67 est né d'un travail d'étudiant. "
                "À l'Université McGill, un jeune architecte, Moshe Safdie, imagine une façon nouvelle d'habiter la ville : des maisons préfabriquées, empilées les unes sur les autres, où chaque logement aurait son jardin sur le toit du voisin. "
                "Son idée devient l'un des pavillons phares de l'Exposition universelle de 1967."
                "\n\n"
                "Le résultat est une colline de béton faite de centaines de modules identiques, décalés dans tous les sens. "
                "Les cubes ont été coulés sur place, puis hissés par une grue et posés comme des briques géantes. "
                "Plus d'un demi-siècle plus tard, l'ensemble paraît toujours sorti du futur."
                "\n\n"
                "Habitat 67 n'est pas un musée : ce sont des appartements privés, et ses habitants tiennent à leur calme. "
                "On l'admire depuis la jetée de la Cité du Havre, ou de l'autre côté de l'eau, depuis le Vieux-Port. "
                "Des visites guidées permettent parfois d'entrer dans un logement et de découvrir la vue depuis les terrasses."
            ),
            "en": (
                "Habitat 67 started out as a student project. "
                "At McGill University, a young architect named Moshe Safdie imagined a new way to live in the city: prefabricated homes stacked on top of one another, with each unit getting a garden on its neighbour's roof. "
                "His idea became one of the star pavilions of the 1967 World's Fair, Expo 67."
                "\n\n"
                "The result is a hill of concrete made of hundreds of identical modules, stepped and shifted in every direction. "
                "The boxes were cast right on site, then lifted by crane and set in place like giant bricks. "
                "More than half a century later, it still looks like something from the future."
                "\n\n"
                "Habitat 67 is not a museum. These are private homes, and residents value their peace and quiet. "
                "Admire it from the Cité du Havre pier, or from across the water in the Old Port. "
                "Guided tours sometimes let you step inside a unit and take in the view from the terraces."
            ),
            "es": (
                "Habitat 67 nació como un trabajo de estudiante. "
                "En la Universidad McGill, un joven arquitecto llamado Moshe Safdie imaginó una nueva forma de vivir en la ciudad: casas prefabricadas, apiladas unas sobre otras, donde cada vivienda tendría su jardín en el techo del vecino. "
                "Su idea se convirtió en uno de los pabellones estrella de la Exposición Universal de 1967."
                "\n\n"
                "El resultado es una colina de hormigón formada por cientos de módulos idénticos, desplazados en todas las direcciones. "
                "Los cubos se fabricaron en el mismo lugar y luego una grúa los fue colocando como ladrillos gigantes. "
                "Más de medio siglo después, el conjunto todavía parece salido del futuro."
                "\n\n"
                "Habitat 67 no es un museo: son departamentos privados, y sus residentes cuidan su tranquilidad. "
                "Se admira desde el muelle de la Cité du Havre, o desde el otro lado del agua, en el Viejo Puerto. "
                "A veces hay visitas guiadas que permiten entrar en una vivienda y disfrutar la vista desde las terrazas."
            ),
        },
        "conseil": {
            "fr": "Aucun métro n'y mène : combinez la visite avec une balade à vélo depuis le Vieux-Port, par la piste qui longe le fleuve jusqu'au parc de la Cité-du-Havre.",
            "en": "No metro goes there: make it part of a bike ride from the Old Port, along the riverside path to Cité du Havre park.",
            "es": "Ningún metro llega hasta ahí: inclúyalo en un paseo en bicicleta desde el Viejo Puerto, por la ciclovía junto al río hasta el parque de la Cité du Havre.",
        },
        "anecdote": {
            "fr": "Moshe Safdie n'avait pas encore trente ans à l'ouverture d'Expo 67, et il a lui-même acheté plus tard un logement dans son œuvre.",
            "en": "Moshe Safdie was not yet thirty when Expo 67 opened, and he later bought a unit in the building himself.",
            "es": "Moshe Safdie aún no cumplía treinta años cuando abrió la Expo 67, y más tarde compró él mismo una vivienda en el edificio.",
        },
        "verifier": [],
    },
    # ------------------------------------------------------------------ 10
    {
        "id": "biosphere",
        "cat": "voir",
        "quartier": "Ville-Marie",
        "metro": "Jean-Drapeau",
        "adresse": "160, chemin du Tour-de-l'Isle",
        "geo": (45.5141, -73.5317),
        "duree": 90,
        "nom": {
            "fr": "Biosphère",
            "en": "Biosphère",
            "es": "Biosphère",
        },
        "bref": {
            "fr": "La grande bulle d'Expo 67, devenue un musée de l'environnement sur l'île Sainte-Hélène.",
            "en": "The giant bubble from Expo 67, now an environment museum on Île Sainte-Hélène.",
            "es": "La gran burbuja de la Expo 67, hoy un museo del medio ambiente en la isla Sainte-Hélène.",
        },
        "texte": {
            "fr": (
                "Sur l'île Sainte-Hélène, au milieu du fleuve, une immense sphère de métal semble posée sur les arbres. "
                "C'était le pavillon des États-Unis à l'Exposition universelle de 1967, conçu par l'inventeur américain Richard Buckminster Fuller. "
                "Son dôme géodésique, un maillage de triangles d'acier, était alors recouvert d'une peau transparente."
                "\n\n"
                "En 1976, un incendie a détruit cette enveloppe en quelques minutes, et il n'est resté que la structure. "
                "C'est justement ce squelette, léger comme une dentelle, qui fait aujourd'hui sa beauté. "
                "À l'intérieur, la Biosphère est devenue un musée consacré à l'environnement et au climat, avec des expositions interactives qui plaisent autant aux enfants qu'aux adultes."
                "\n\n"
                "Montez sur la terrasse d'observation : la vue porte sur le fleuve et le centre-ville. "
                "Tout autour, le parc Jean-Drapeau invite à la promenade, entre les œuvres d'art de l'Expo, la plage de l'île Notre-Dame et le circuit du Grand Prix. "
                "Le métro vous y dépose en quelques minutes depuis le centre-ville."
            ),
            "en": (
                "On Île Sainte-Hélène, in the middle of the river, a huge metal sphere seems to float above the trees. "
                "It was the United States pavilion at the 1967 World's Fair, designed by American inventor Richard Buckminster Fuller. "
                "Its geodesic dome, a web of steel triangles, was covered back then by a transparent skin."
                "\n\n"
                "In 1976, a fire destroyed that covering in a matter of minutes, leaving only the frame. "
                "Today it is exactly that skeleton, as delicate as lace, that makes it so beautiful. "
                "Inside, the Biosphère has become a museum devoted to the environment and climate, with hands-on exhibits that appeal to kids and adults alike."
                "\n\n"
                "Head up to the observation terrace for a view over the river and downtown. "
                "All around, Parc Jean-Drapeau is perfect for a stroll, with public art left over from Expo 67, the beach on Île Notre-Dame and the Grand Prix racetrack. "
                "The metro gets you here from downtown in just a few minutes."
            ),
            "es": (
                "En la isla Sainte-Hélène, en medio del río, una enorme esfera metálica parece flotar sobre los árboles. "
                "Era el pabellón de Estados Unidos en la Exposición Universal de 1967, diseñado por el inventor estadounidense Richard Buckminster Fuller. "
                "Su cúpula geodésica, una red de triángulos de acero, estaba cubierta entonces por una piel transparente."
                "\n\n"
                "En 1976, un incendio destruyó esa cubierta en pocos minutos, y solo quedó la estructura. "
                "Justamente ese esqueleto, ligero como un encaje, es lo que hoy la hace tan bella. "
                "Por dentro, la Biosphère se convirtió en un museo dedicado al medio ambiente y al clima, con exposiciones interactivas que gustan tanto a niños como a adultos."
                "\n\n"
                "Suba a la terraza de observación para ver el río y el centro de la ciudad. "
                "Alrededor, el parque Jean-Drapeau invita a pasear, entre las obras de arte de la Expo, la playa de la isla Notre-Dame y el circuito del Gran Premio. "
                "El metro lo trae desde el centro en pocos minutos."
            ),
        },
        "conseil": {
            "fr": "Pour la photo, éloignez-vous d'une centaine de pas vers le fleuve : c'est de là qu'on saisit la sphère entière, avec la ville derrière.",
            "en": "For the best photo, walk a hundred steps toward the river: from there you can frame the whole sphere with the city behind it.",
            "es": "Para la mejor foto, aléjese unos cien pasos hacia el río: desde ahí se capta la esfera completa, con la ciudad detrás.",
        },
        "anecdote": {
            "fr": "Pendant Expo 67, un monorail traversait le pavillon américain, en plein cœur de la sphère.",
            "en": "During Expo 67, a monorail ran right through the American pavilion, straight into the heart of the sphere.",
            "es": "Durante la Expo 67, un monorriel atravesaba el pabellón estadounidense, justo por el corazón de la esfera.",
        },
        "verifier": [],
    },
]
