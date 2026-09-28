"""Les leçons narrées d'« Avant de partir » — une par séance, écoutée avant de jouer.

Demande de Daniel, 27 sept. 2026, après avoir fait la séance 1 : « il faudrait
que quelqu'un explique comment ça marche avant que les gens jouent […] un
fichier son […] la même chose pour les huit ».

Chaque leçon est une suite de segments : ("fr", …) est dit par la guide (voix
québécoise), ("es", …) par la voix d'Espagne des mots. Les segments sont
synthétisés un à un puis assemblés en un seul MP3 (build/compostelle_lecons.py) :
une voix HD qui lit du français ne sait pas prononcer « jamón ».

Règles d'écriture :
- 1 min 30 à 2 min : une idée par phrase, des phrases courtes, à l'oral ;
- la règle d'abord par un exemple entendu, jamais une liste à retenir ;
- chaque leçon finit par ce qu'on fera ensuite dans la séance ;
- pas de genre dans l'audio (le son est le même pour tous) : on dit
  les deux formes quand il le faut.
"""

LECONS = {
"p1": [
    ("fr", "Bonjour, et bienvenue. Avant de partir sur le chemin, on va apprivoiser les sons de l'espagnol. Bonne nouvelle : en espagnol, une lettre se dit presque toujours de la même façon. Si vous connaissez six ou sept sons, vous pouvez lire à voix haute n'importe quel mot."),
    ("fr", "D'abord, les voyelles. Elles sont toujours pleines, jamais avalées. Écoutez :"),
    ("es", "a, e, i, o, u."),
    ("fr", "Le e ne devient jamais « eu », et le u se dit « ou ». Écoutez le mot nuit, en espagnol :"),
    ("es", "noche."),
    ("fr", "Ensuite, le j. Il se racle au fond de la gorge, un peu comme le « ch » allemand de « Bach ». Écoutez le mot jambon, en espagnol :"),
    ("es", "jamón."),
    ("fr", "Les deux l se disent comme un y. Écoutez le mot rue, en espagnol :"),
    ("es", "calle."),
    ("fr", "Et le n avec une vague se dit « gn », comme dans « montagne ». Écoutez le mot Espagne, en espagnol :"),
    ("es", "España."),
    ("fr", "Le r est battu une seule fois. Le double r, lui, roule. Et ça change le sens ! Écoutez le mot mais, puis le mot chien, en espagnol :"),
    ("es", "pero. perro."),
    ("fr", "En Espagne, le z, et le c devant e ou i, se disent la langue entre les dents, comme le « th » anglais. Écoutez le mot merci, en espagnol :"),
    ("es", "gracias."),
    ("fr", "Dernier truc : la syllabe forte. Si le mot finit par une voyelle, un n ou un s, on appuie sur l'avant-dernière syllabe. Sinon, sur la dernière. Et s'il y a un accent écrit, c'est lui qui gagne. Écoutez trois mots en espagnol : chemin, payer, café."),
    ("es", "camino. pagar. café."),
    ("fr", "C'est tout pour la théorie. Maintenant, vous allez écouter des mots du chemin et les répéter à voix haute, puis les reconnaître à l'oreille, et enfin les dire au micro. N'ayez pas peur d'exagérer : c'est comme ça qu'on apprend."),
],
"p2": [
    ("fr", "Dans cet entraînement, on apprend les formules qui ouvrent toutes les portes. Et surtout, celles qui vous sauvent quand vous ne comprenez pas."),
    ("fr", "En espagnol, bonjour change avec l'heure. Le matin, et jusqu'au dîner, vers deux heures de l'après-midi, on dit :"),
    ("es", "Buenos días."),
    ("fr", "L'après-midi, et jusqu'au souper, qui arrive tard en Espagne, on dit :"),
    ("es", "Buenas tardes."),
    ("fr", "Et le soir, pour saluer comme pour dire bonne nuit :"),
    ("es", "Buenas noches."),
    ("fr", "Pour attirer l'attention ou vous excuser, il y a deux formes. Avec un commerçant ou une personne âgée, on vouvoie :"),
    ("es", "Perdone."),
    ("fr", "Entre pèlerins, on se tutoie tout de suite :"),
    ("es", "Perdona."),
    ("fr", "Pour dire merci, et pour répondre de rien :"),
    ("es", "Gracias. De nada."),
    ("fr", "Maintenant, la phrase la plus utile de tout le voyage. Les Espagnols parlent vite. Quand ça va trop vite, dites simplement :"),
    ("es", "Más despacio, por favor."),
    ("fr", "Ça veut dire : plus lentement, s'il vous plaît. Et si vous n'avez rien compris, vous pouvez demander de répéter :"),
    ("es", "¿Puede repetir, por favor?"),
    ("fr", "Retenez bien ceci : ne pas comprendre, ce n'est pas un échec. C'est une situation normale, et vous avez maintenant les mots pour vous en sortir. À vous d'écouter, de reconnaître, puis de le dire."),
],
"p3": [
    ("fr", "Sur le chemin, tout a un prix : un lit, un café, un pansement. Et le prix se dit vite. Dans cet entraînement, on apprend les nombres dont vous aurez besoin, et surtout, ceux qui se ressemblent à l'oreille."),
    ("fr", "Pour dire un prix, on dit les euros, puis un petit mot qui veut dire « avec », puis les centimes. Quatre euros cinquante, en espagnol, c'est :"),
    ("es", "cuatro con cincuenta."),
    ("fr", "Souvent, on ne dit même pas le mot euro. Maintenant, les pièges. Deux et douze se ressemblent. Écoutez bien la fin :"),
    ("es", "dos. doce."),
    ("fr", "Six et sept aussi :"),
    ("es", "seis. siete."),
    ("fr", "Et encore : treize et trente, quinze et cinquante."),
    ("es", "trece. treinta. quince. cincuenta."),
    ("fr", "Le truc : écoutez la fin du mot. Les dizaines, trente, quarante, cinquante, finissent toutes par le même son. Écoutez :"),
    ("es", "treinta. cuarenta. cincuenta."),
    ("fr", "Pour demander le prix, une seule question suffit :"),
    ("es", "¿Cuánto es?"),
    ("fr", "C'est combien ? Et pour payer, par carte, ou comptant :"),
    ("es", "Con tarjeta. En efectivo."),
    ("fr", "Si vous avez un doute sur un nombre, n'hésitez pas : demandez de répéter, ou montrez vos doigts. Maintenant, vous allez entendre des prix, et choisir le bon. Prenez votre temps."),
],
"p4": [
    ("fr", "Sur le chemin, beaucoup de choses se jouent à une heure près : le souper, la porte de l'auberge qui ferme, le magasin qui rouvre après la sieste. Dans cet entraînement, on apprend à comprendre l'heure."),
    ("fr", "Pour une heure, on parle au singulier. À partir de deux heures, au pluriel. Écoutez : à une heure, à deux heures, à trois heures."),
    ("es", "A la una. A las dos. A las tres."),
    ("fr", "Pour les demies et les quarts, on ajoute : et demie, et quart, moins le quart."),
    ("es", "y media. y cuarto. menos cuarto."),
    ("fr", "Donc, huit heures et demie, c'est :"),
    ("es", "a las ocho y media."),
    ("fr", "Attention : en Espagne, les heures de la journée sont décalées. On dîne vers deux heures de l'après-midi, et on soupe vers neuf heures du soir. Et beaucoup de commerces ferment de deux heures à cinq heures."),
    ("fr", "Pour demander à quelle heure ça ouvre :"),
    ("es", "¿A qué hora abre?"),
    ("fr", "Et un piège classique : le même mot veut dire demain, et le matin. Seul, c'est demain :"),
    ("es", "mañana."),
    ("fr", "Mais précédé de deux petits mots, c'est le matin :"),
    ("es", "por la mañana."),
    ("fr", "Vous allez maintenant écouter des heures, les reconnaître, puis demander vous-même à quelle heure ça ouvre."),
],
"p5": [
    ("fr", "Bonne nouvelle : pour vous débrouiller, vous n'avez pas besoin de conjuguer. Quatre formes toutes faites suffisent pour demander presque tout. Il suffit d'ajouter la chose que vous voulez."),
    ("fr", "La première, pour commander poliment. Je voudrais :"),
    ("es", "Quisiera un café."),
    ("fr", "La deuxième, pour savoir si c'est disponible ici. Vous avez ?"),
    ("es", "¿Tiene agua?"),
    ("fr", "La troisième, pour ce qui presse. J'ai besoin de :"),
    ("es", "Necesito una farmacia."),
    ("fr", "Et la quatrième, pour la pharmacie ou le médecin. J'ai mal à, suivi de la partie du corps :"),
    ("es", "Me duele la rodilla."),
    ("fr", "J'ai mal au genou. Une seule chose bouge : quand ce qui fait mal est au pluriel, on ajoute un n. J'ai mal aux pieds :"),
    ("es", "Me duelen los pies."),
    ("fr", "Récapitulons. Je voudrais, vous avez, j'ai besoin de, j'ai mal."),
    ("es", "Quisiera. ¿Tiene? Necesito. Me duele."),
    ("fr", "Avec ces quatre-là, vous pouvez commander, chercher, demander de l'aide et vous soigner. Maintenant, écoutez-les dans des phrases, puis à vous de les dire."),
],
"p6": [
    ("fr", "Dans un village inconnu, il faut trouver l'auberge, l'eau, la pharmacie. Dans cet entraînement, on apprend à poser des questions avec quelques petits mots seulement."),
    ("fr", "Pour demander où est quelque chose :"),
    ("es", "¿Dónde está el albergue?"),
    ("fr", "Pour le prix :"),
    ("es", "¿Cuánto cuesta?"),
    ("fr", "Pour l'heure :"),
    ("es", "¿A qué hora?"),
    ("fr", "Et voici le mot magique. Il veut dire « il y a », et il sert pour tout. Écoutez-le :"),
    ("es", "hay."),
    ("fr", "Il se prononce comme « aïe ». Est-ce qu'il y a de l'eau ? Est-ce qu'il y a une pharmacie ?"),
    ("es", "¿Hay agua? ¿Hay una farmacia?"),
    ("fr", "À l'auberge, pour savoir s'il reste des lits :"),
    ("es", "¿Quedan camas?"),
    ("fr", "Remarquez une chose : en espagnol, une question, c'est souvent une phrase ordinaire, dite avec la voix qui monte à la fin. Écoutez la différence. Il y a de l'eau. Est-ce qu'il y a de l'eau ?"),
    ("es", "Hay agua. ¿Hay agua?"),
    ("fr", "À l'écrit, un point d'interrogation à l'envers ouvre la question. Maintenant, à vous : écoutez, reconnaissez, puis posez vos propres questions au micro."),
],
"p7": [
    ("fr", "Sur le chemin, la première question qu'on vous posera, c'est d'où vous venez. La deuxième, c'est pourquoi vous marchez. Dans cet entraînement, vous préparez vos phrases. Elles vous serviront tous les soirs."),
    ("fr", "Pour dire d'où vous venez, on dit « je suis de », puis votre ville :"),
    ("es", "Soy de Quebec, en Canadá."),
    ("fr", "Pour la raison, on dit « je fais le chemin pour », puis la raison. Pour le sport, pour ma famille, pour la foi :"),
    ("es", "Hago el Camino por el deporte. Por mi familia. Por la fe."),
    ("fr", "Si c'est pour faire quelque chose, on change de petit mot. Pour réfléchir :"),
    ("es", "Para pensar."),
    ("fr", "Maintenant, une petite subtilité : l'espagnol a deux verbes être. Le premier, pour ce que vous êtes de façon durable, par exemple pèlerin. Le second, pour ce qui passe, comme être fatigué. Écoutez-les :"),
    ("es", "Soy. Estoy."),
    ("fr", "Et le mot qui suit change selon que vous êtes un homme ou une femme :"),
    ("es", "Soy peregrino. Soy peregrina."),
    ("es", "Estoy cansado. Estoy cansada."),
    ("fr", "Et pour dire d'où vous êtes parti, par exemple de Roncesvalles :"),
    ("es", "Empecé en Roncesvalles."),
    ("fr", "Entre pèlerins, on se tutoie. On vous demandera :"),
    ("es", "¿De dónde eres? ¿Por qué haces el Camino?"),
    ("fr", "Dans cet entraînement, les phrases s'accordent à ce que vous avez choisi au départ. Écoutez-les, puis dites vos vraies réponses."),
],
"p8": [
    ("fr", "Voici l'entraînement le plus important. Le plus dur, en voyage, ce n'est pas de demander : c'est de comprendre la réponse. Elle arrive vite, avec l'accent d'ici, et souvent avec beaucoup de mots."),
    ("fr", "Le secret, c'est de ne pas tout comprendre. Guettez le mot qui décide, et laissez filer le reste. Écoutez cette réponse :"),
    ("es", "Lo siento mucho, hoy está completo, pero hay otro albergue en la plaza."),
    ("fr", "Vous n'avez peut-être pas tout saisi, mais un mot décide :"),
    ("es", "completo."),
    ("fr", "C'est complet. Voici les mots qui décident, par paires."),
    ("fr", "Il y en a, ou il n'y en a pas :"),
    ("es", "Hay. No hay."),
    ("fr", "Il en reste, ou c'est complet :"),
    ("es", "Quedan. Está completo."),
    ("fr", "À droite, à gauche, tout droit :"),
    ("es", "A la derecha. A la izquierda. Todo recto."),
    ("fr", "Et au restaurant, ce que contient un plat : ça en contient, ou ça n'en contient pas :"),
    ("es", "Lleva. No lleva."),
    ("fr", "Souvent, les Espagnols répètent le oui et le non, comme ceci :"),
    ("es", "Sí, sí. No, no."),
    ("fr", "Ça aide !"),
    ("fr", "Dans les exercices, on vous parlera à vitesse normale. Ne cherchez pas à tout comprendre. Cherchez le mot qui décide. Et si vous ne l'entendez pas, vous savez maintenant quoi dire :"),
    ("es", "Más despacio, por favor."),
],
}


def verifier():
    import sys
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    from preparation import SEANCES
    ids = [s["id"] for s in SEANCES]
    assert list(LECONS) == ids, (list(LECONS), ids)
    for sid, segs in LECONS.items():
        assert segs and segs[0][0] == "fr", sid
        for lang, t in segs:
            assert lang in ("fr", "es") and t.strip(), (sid, t)
            assert "{" not in t, (sid, t)
    return True


if __name__ == "__main__":
    verifier()
    for sid, segs in LECONS.items():
        fr = sum(len(t.split()) for l, t in segs if l == "fr")
        print(sid, f"{len(segs)} segments, {fr} mots en français, ~{fr / 150:.1f} min")
