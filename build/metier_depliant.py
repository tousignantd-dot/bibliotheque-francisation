#!/usr/bin/env python3
"""Les dépliants des trousses de métier : comment l'outil fonctionne, pour qui l'achète.

    python3 build/metier_depliant.py            # les deux
    python3 build/metier_depliant.py hotel      # une seule (francoeur | hotel)

Daniel, 28 sept. 2026 : « un dépliant et la même formule » que Compostelle pour
la Maison Francœur (vente de vêtements) et l'Hôtel Rive-Claire (réception), et
« vendre les produits de la même façon ». Le public est la personne qui apprend
la langue de son poste — tout est gratuit sauf le jeu de rôle, vendu par code
au prix de Compostelle (pelerins.offre()). Une ligne renvoie les employeurs à
l'offre d'entreprise, sans montant : ce n'est pas le même lecteur.

Sorties (produites, jamais éditées) :
  assets/presentations/<x>-depliant.html          au classeur (connexion)
  modules-autonomes/<app>/presentation.html        la copie publique, noindex
Les captures sont de vraies pages (build/hotel_captures.mjs,
build/francoeur_captures.mjs, plus une scène jouée en ligne avec un code
d'essai), réduites en JPEG à côté du dépliant. Tout ce qui se compte (mots,
clients, gestes, langues, prix) est relu dans le contenu.
"""
from qr_bloc import bloc  # le code QR de l'application (2 oct. 2026)
import html, importlib.util, json, pathlib, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE))
import pelerins  # noqa: E402
from PIL import Image  # noqa: E402

E = html.escape
MOIS = "janvier février mars avril mai juin juillet août septembre octobre novembre décembre".split()
LANGUES_FR = {"ar": "arabe", "es": "espagnol", "uk": "ukrainien", "fa": "persan", "zh": "chinois", "pt": "portugais",
              "en": "anglais", "ro": "roumain", "ur": "ourdou", "ru": "russe", "ti": "tigrigna"}


def date_fr(iso):
    a, m, j = (int(x) for x in iso.split("-"))
    return f"{'1er' if j == 1 else j} {MOIS[m - 1]} {a}"


def prix(c):
    return f"{c / 100:.2f}".replace(".", ",") + " $"


def charger(nom, chemin):
    s = importlib.util.spec_from_file_location(nom, chemin)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m


def francoeur():
    C = RACINE / "build" / "contenu" / "entreprise-francoeur"
    lx = charger("md_flx", C / "lexique.py"); cl = charger("md_fcl", C / "clients.py")
    langues = sorted(LANGUES_FR[k] for k in json.loads((C / "traductions.json").read_text(encoding="utf-8")))
    return {
        "cle": "francoeur", "app": "/modules-autonomes/francoeur-planches/", "sortie": "francoeur-depliant",
        "captures": "francoeur-captures",
        "titre": "Maison Francœur — comment ça marche",
        "descripteur": "Aide à l'apprentissage du français", "secteur": "Vente au détail · Vêtements",
        "enseigne": "Maison Francœur",
        "couleurs": {"fond": "#FAFBFD", "papier": "#FFFFFF", "action": "#2B4A78", "fonce": "#16243A", "accent": "#C8692A",
                     "halo": "#FBE9DC", "texte": "#1E2733", "doux": "#4F5B6A", "filet": "#D5DDE7"},
        "sur": "Pour qui travaille, ou veut travailler, dans un magasin de vêtements",
        "h1": "Le français du magasin, <span>client par client</span>.",
        "chapeau": ("Une tuque, un chandail en moyen, « je vais vérifier en arrière » : vous apprenez les mots et les phrases "
                    "du plancher, en images et à l'oreille, puis vous servez de vrais clients qui vous répondent. "
                    "Votre langue vous aide à comprendre ; ce que vous entendez et ce que vous dites reste en français du Québec."),
        "une": ("planche", "scene"), "tampon": (len(cl.CLIENTS), "clients<br>à servir"),
        "chiffres": [(len(lx.LEXIQUE), f"mots du magasin, dessinés, répartis en {len(lx.PLANCHES)} rayons"),
                     (len(langues), "langues d'appui, de l'arabe au tigrigna ; ou le français seul"),
                     (len(cl.CLIENTS), f"clients qui vous parlent vraiment, et {len(cl.GESTES)} gestes du vendeur"),
                     ("0 $", "pour les mots, les exercices, le test et la fiche ; aucune inscription")],
        "chemin_tit": "Cinq étapes, du mot au client",
        "chemin_intro": "L'écran vous dit toujours quelle est la prochaine étape. Rien à planifier : vous faites un peu chaque jour.",
        "etapes": [("Mon niveau", "Un court test pour savoir par où commencer : débutant, fonctionnel ou à l'aise."),
                   ("Apprendre les mots", "Les rayons du magasin, vêtement par vêtement. Vous touchez, vous entendez."),
                   ("Je m'exerce", "Ce que le client veut, ranger le rayon, ce que la gérante demande, ce que je réponds."),
                   ("Les gestes du vendeur", "Les phrases qui tirent d'affaire : faire préciser, faire répéter, passer le relais."),
                   ("Le magasin", "Les clients entrent. Vous les servez, à voix haute.")],
        "ecrans": [("rayons", "Découvrir", "Les rayons du magasin", "Chaque vêtement est dessiné et dit par une voix d'ici. Votre langue reste cachée tant que vous ne la demandez pas."),
                   ("client", "Comprendre", "Ce que le client veut", "Un client parle, vite, comme en vrai. Vous touchez ce qu'il demande : la couleur, la taille, le bon article."),
                   ("magasin", "Agir", "Le magasin", "Vous choisissez le niveau des clients, puis un client. Il entre ; à vous de le servir.")],
        "gestes": [g["nom"] for g in cl.GESTES],
        "bande_tit": "Vous parlez, pour vrai",
        "bande_intro": "Le magasin est la dernière étape : huit clients, chacun avec son idée en tête.",
        "bande_li": ["<b>Monsieur Gagnon</b> regarde et ne veut pas qu'on le pousse ; <b>Madame Ouellet</b> ne connaît pas sa taille ici ; d'autres cherchent un cadeau, un retour, un article en rupture.",
                     "<b>Un bilan geste par geste</b> après chaque visite, dans votre langue : ce que vous avez fait, ce qui manquait.",
                     "<b>Le niveau des clients</b> suit le vôtre : débutant, fonctionnel ou à l'aise."],
        "bande_caps": ("scene",),
        "libre": {
            "titre": "Gratuit, vous apprenez le magasin. Avec le magasin joué, vous le vivez.",
            "intro": "Les mots, les exercices, le test et la fiche sont gratuits, et ils suffisent pour apprendre les phrases. "
                     "Mais un vrai client ne suit pas l'exercice : il ne connaît pas sa taille, il change d'idée, il pose une "
                     "question de plus. Le magasin joué vous y prépare.",
            "gratuit": ["Un client parle, et vous touchez ce qu'il demande.",
                        "« Ce que je réponds » : vous choisissez la bonne réplique parmi trois.",
                        "On vous dit si c'était juste, et pourquoi.",
                        "Idéal pour <b>apprendre</b> les mots et les gestes du vendeur."],
            "payant": ["Vous parlez au client <b>comme au magasin</b>, au micro ou par écrit.",
                       "Huit clients, chacun avec son idée : il vous répond <b>à vous</b>, et son visage change selon ce que vous dites.",
                       "Un <b>bilan geste par geste</b>, dans votre langue : faire préciser, faire répéter, vérifier, passer le relais.",
                       "Vos phrases, corrigées.",
                       "Idéal pour <b>oser</b>, avant votre premier client."],
            "notes": [("Une vraie visite, telle quelle.", "Madame Ouellet cherche un chandail, mais ne connaît pas sa taille ici. "
                       "Le vendeur lui demande une chose à la fois : la couleur, puis la taille."),
                      ("Elle répond comme une vraie cliente.", "« Chez nous, je fais du moyen ou du grand, ça dépend. » Le vendeur "
                       "explique les tailles d'ici et va vérifier en arrière."),
                      ("Et le bilan, geste par geste.", "Faire préciser une chose à la fois, redire, vérifier : chaque geste réussi "
                       "est cité avec la phrase exacte, et ce qui n'était pas nécessaire est dit aussi.")],
            "pourqui": [("Vous commencez bientôt en magasin", "Quelques visites par semaine, et le premier « je cherche… » ne vous prend plus de court."),
                        ("Vous comprenez, mais vous figez pour répondre", "Personne ne vous juge : vous recommencez avec le même client, ou un autre."),
                        ("Vous voulez savoir ce qui vous manque", "Le bilan nomme le geste à travailler : faire répéter, passer le relais à la gérante…")],
            "conv_alt": "Une vraie visite au magasin : Madame Ouellet et le vendeur",
            "bilan_alt": "Le bilan de la visite, geste par geste",
        },
        "appui_tit": "Votre langue vous aide, sans prendre la place",
        "appui": [("langue", "Onze langues d'appui", "Les consignes s'affichent dans votre langue : " + ", ".join(langues) + ". Les mots, eux, restent en français."),
                  ("fiche", "Chaque mot a sa fiche", "La voix, l'image, ce qu'on entend aussi au Québec, et le piège à éviter. La traduction ne paraît que si vous la demandez.")],
        "jeu_nom": "Le magasin joué",
        "jeu_li": lambda o: [f"{o['conversations']} visites de clients, sur {o['jours'] // 30} mois ;",
                             "des clients qui répondent à ce que vous dites, à voix haute ;",
                             "un bilan geste par geste après chaque visite ;",
                             f"au besoin, {o['rechargeConversations']} visites de plus pour {prix(o['recharge'])}."],
        "gratuit_li": [f"les {len(lx.LEXIQUE)} mots et leurs voix ;", "les exercices et les gestes du vendeur ;",
                       "le test de niveau ;", "la fiche de poche, à garder sur soi."],
        "employeur": ("Vous êtes employeur ?", "La trousse s'ajuste à votre magasin : vos rayons, vos mots, votre politique de retour. "
                      "Pilote avec votre équipe, trousse à votre enseigne ou licence annuelle, à prix fixe."),
        "fin_tit": "Bonne première journée !", "fin_p": "Commencez par le test : cinq minutes, et vous savez par où continuer.",
        "fin_cta": "Ouvrir la Maison Francœur",
    }


def hotel():
    C = RACINE / "build" / "contenu" / "entreprise-hotel"
    lx = charger("md_hlx", C / "lexique.py"); cl = charger("md_hcl", C / "clients.py")
    iface = charger("md_hif", C / "interface.py"); ex = charger("md_hex", C / "exercices.py")
    familles = [ex.UI["x_" + f]["fr"] for f in ["entends", "image", "souviens", "dire", "pieges", "epeler", "nombres", "client", "reponds"]]
    themes = [v["fr"] for k, v in iface.PLANCHES.items() if k != "comptoir"]
    return {
        "cle": "hotel", "app": "/modules-autonomes/hotel-reception/", "sortie": "hotellerie-depliant",
        "captures": "hotellerie-captures",
        "titre": "Hôtel Rive-Claire — comment ça marche",
        "descripteur": "français · anglais · espagnol", "secteur": "Hôtellerie · Réception",
        "enseigne": "Hôtel Rive-Claire",
        "couleurs": {"fond": "#FDFBF7", "papier": "#FFFFFF", "action": "#0F5E63", "fonce": "#0B3437", "accent": "#C4613A",
                     "halo": "#F6E3D9", "texte": "#23282A", "doux": "#5E625F", "filet": "#E0D8C8"},
        "sur": "Pour qui travaille, ou veut travailler, à la réception d'un hôtel",
        "h1": "L'accueil à la réception, <span>dans la langue du client</span>.",
        "chapeau": ("Une réservation, un nom épelé au téléphone, deux lits queen pour trois nuits, un frais à expliquer : "
                    "vous apprenez la langue du comptoir, puis vous accueillez de vrais clients qui vous répondent. "
                    "Français, anglais, espagnol : vous choisissez celle que vous parlez et celle que vous apprenez."),
        "une": ("comptoir", "jeu"), "tampon": (len(cl.CLIENTS), "clients<br>à accueillir"),
        "chiffres": [(len(lx.LEXIQUE), f"mots de la réception, en {len(themes)} thèmes et un comptoir à toucher"),
                     ("3", "langues à égalité : six façons d'apprendre (français ↔ anglais ↔ espagnol)"),
                     (len(cl.CLIENTS), f"clients qui vous parlent vraiment, dont un au téléphone, et {len(cl.GESTES)} gestes"),
                     ("0 $", "pour les mots, les exercices, le test et la fiche ; aucune inscription")],
        "chemin_tit": "Du comptoir au client",
        "chemin_intro": "Commencez par votre poste, tel que vous le voyez de votre place. Puis les mots, les exercices, le test, et les clients.",
        "etapes": [("Le comptoir", "Votre poste dessiné : l'écran, le lecteur de carte, l'encodeur de clés. Vous touchez, vous entendez."),
                   ("Les mots, par thème", " · ".join(themes) + "."),
                   ("Je m'exerce", f"{len(familles)} séries : " + ", ".join(f.lower() if i else f for i, f in enumerate(familles)) + "."),
                   ("Mon niveau", "Un test en quatre parties, dont une au téléphone, pour savoir où vous en êtes."),
                   ("Le comptoir joué", "Les clients arrivent. Vous les accueillez, à voix haute.")],
        "ecrans": [("planche", "Découvrir", "Les mots de la réception", "Chaque mot est dessiné et dit par une voix du pays : Québec, Amérique du Nord, Mexique."),
                   ("pieges", "Comprendre", "La série des pièges", "Les faux amis entre vos deux langues, toujours dans une phrase de comptoir : « le dîner » n'est pas « la cena »."),
                   ("client", "S'exercer", "Ce que le client veut", "Un client parle vite : la bonne chambre, le bon nombre de nuits, les dates. Des nombres, des heures et des noms épelés au téléphone, pratiqués avant le vrai comptoir.")],
        "gestes": [g["nom"]["fr"] for g in cl.GESTES],
        "bande_tit": "Vous parlez, pour vrai",
        "bande_intro": "Le comptoir joué est la dernière étape : huit clients, devant le même comptoir.",
        "bande_li": ["<b>Une arrivée</b> avec réservation, <b>un client sans réservation</b> un soir complet, <b>un frais contesté</b>, <b>une demande hors règle</b>… et un appel, sans visage.",
                     "<b>Un bilan geste par geste</b> après chaque client, dans votre langue : ce que vous avez fait, ce qui manquait.",
                     "<b>Promettre ce que l'hôtel ne peut pas tenir</b> fait échouer la situation : on l'apprend avant d'y être."],
        "bande_caps": ("jeu",),
        "libre": {
            "titre": "Gratuit, vous apprenez le comptoir. Avec le comptoir joué, vous le vivez.",
            "intro": "Les mots, le comptoir, les exercices et le test sont gratuits, et ils suffisent pour apprendre les phrases. "
                     "Mais un vrai client ne suit pas l'exercice : il insiste, demande une faveur, épelle son nom au téléphone. "
                     "Le comptoir joué vous y prépare.",
            "gratuit": ["Un client parle, et vous trouvez la bonne chambre, le bon prix, la bonne date.",
                        "« Ce que je réponds » : vous choisissez la bonne réplique parmi trois.",
                        "On vous dit si c'était juste, et pourquoi.",
                        "Idéal pour <b>apprendre</b> les mots et les gestes du comptoir."],
            "payant": ["Vous parlez au client <b>dans la langue que vous apprenez</b>, au micro ou par écrit.",
                       "Huit clients devant le même comptoir, dont un au téléphone : ils vous répondent <b>à vous</b>, et ils insistent.",
                       "Votre écran vous montre la réservation, comme au vrai poste.",
                       "Un <b>bilan geste par geste</b>, dans votre langue, qui relève toute promesse que l'hôtel ne pourrait pas tenir.",
                       "Idéal pour <b>oser</b>, avant votre premier quart de travail."],
            "notes": [("Une vraie conversation, telle quelle.", "Ms. Leblanc fête son anniversaire de mariage et demande une suite "
                       "gratuite. Ce n'est pas à la réceptionniste de décider : elle passe le relais au gérant."),
                      ("La cliente insiste, comme en vrai.", "« Could you please ask him to make an exception? » La réceptionniste "
                       "tient bon sans rien promettre, puis propose ce qu'elle a le droit d'offrir : une table au restaurant, une carte "
                       "dans la chambre."),
                      ("Et le bilan, geste par geste.", "Le geste clé — passer le relais sans promettre — est réussi. Et la phrase à "
                       "reprendre : « it's not me who decide » devient « that's not my decision to make ».")],
            "pourqui": [("Vous commencez à la réception", "Quelques clients par semaine, et le premier « I have a reservation » ne vous prend plus de court."),
                        ("La langue apprise vous gêne au téléphone", "Un des huit clients appelle : pas de visage, seulement la voix."),
                        ("Vous voulez éviter la promesse de trop", "Le bilan relève tout engagement que l'hôtel ne pourrait pas tenir, avant qu'il coûte cher.")],
            "conv_alt": "Une vraie conversation au comptoir : Ms. Leblanc et la réceptionniste",
            "bilan_alt": "Le bilan de la conversation, geste par geste",
        },
        "appui_tit": "Trois langues, à égalité",
        "appui": [("langue", "Vous choisissez", "Je parle français, j'apprends l'anglais ; je parle espagnol, j'apprends le français… L'écran est dans votre langue ; ce que vous entendez et dites, dans celle que vous apprenez."),
                  ("comptoir", "Votre poste, vu de votre place", "Le comptoir dessiné sert du début à la fin : on y touche d'abord les objets, puis les clients s'y présentent, devant le même décor.")],
        "jeu_nom": "Le comptoir joué",
        "jeu_li": lambda o: [f"{o['conversations']} clients à accueillir, sur {o['jours'] // 30} mois ;",
                             "des clients qui répondent à ce que vous dites, à voix haute, dans la langue apprise ;",
                             "un bilan geste par geste après chaque client ;",
                             f"au besoin, {o['rechargeConversations']} clients de plus pour {prix(o['recharge'])}."],
        "gratuit_li": [f"les {len(lx.LEXIQUE)} mots et leurs voix, dans les trois langues ;", "le comptoir à toucher et les exercices ;",
                       "le test de niveau ;", "la fiche de poche, à garder sur soi."],
        "employeur": ("Vous êtes employeur ?", "La trousse s'ajuste à votre hôtel : vos chambres, vos tarifs, vos services, votre politique. "
                      "Pilote avec votre équipe de réception, trousse à votre métier ou licence annuelle, à prix fixe."),
        "fin_tit": "Bienvenue · Welcome · Bienvenido", "fin_p": "Choisissez vos deux langues, et touchez votre comptoir.",
        "fin_cta": "Ouvrir l'Hôtel Rive-Claire",
    }


# Fond plus pâle que celui des applications (Daniel, 28 sept. 2026) : sinon les
# captures se fondent dans la page. Les cartes passent au blanc.
CSS = """
:root{--fond:%(fond)s;--papier:%(papier)s;--action:%(action)s;--fonce:%(fonce)s;--accent:%(accent)s;--halo:%(halo)s;
 --texte:%(texte)s;--doux:%(doux)s;--filet:%(filet)s}
*{box-sizing:border-box}
body{margin:0;background:var(--fond);color:var(--texte);font:17px/1.5 Nunito,system-ui,sans-serif}
.cadre{max-width:1040px;margin:0 auto;padding:0 20px}
a{color:var(--action)}
.retour{display:inline-block;margin:14px 0 0;font-size:14px;color:var(--doux);text-decoration:none}
.fr-barre{background:#fff;border-bottom:3px solid var(--accent)}
.fr-barre__in{max-width:1040px;margin:0 auto;padding:12px 20px;display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.secteur{text-align:right;line-height:1.2}
.secteur small{display:block;font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--doux);font-weight:800}
.secteur b{color:var(--action);font-size:17px}
.une{display:grid;grid-template-columns:1.15fr .85fr;gap:28px;align-items:center;padding:34px 0 10px}
.sur{font-size:13px;letter-spacing:.14em;text-transform:uppercase;font-weight:900;color:var(--accent);margin:0 0 8px}
h1{font-size:clamp(34px,5.4vw,54px);line-height:1.04;margin:0 0 14px;color:var(--fonce);letter-spacing:-.01em}
h1{position:relative;padding-top:18px} h1::before{content:'';position:absolute;left:0;top:0;width:64px;height:6px;border-radius:3px;background:var(--accent)}
h1 span{color:var(--action)}   /* choix de Daniel, 29 sept. 2026 : un filet au-dessus */
.chapeau{font-size:19px;line-height:1.5;margin:0 0 18px}
.cta{display:inline-block;background:var(--action);color:#fff;font-weight:900;text-decoration:none;padding:13px 22px;border-radius:12px;font-size:17px}
.cta:hover{filter:brightness(1.08)}
.une .visuel{position:relative;min-height:420px}
.tel{width:100%%;max-width:250px;border-radius:30px;background:#111;padding:9px;box-shadow:0 18px 40px rgba(0,0,0,.22)}
.tel img{display:block;width:100%%;border-radius:22px;aspect-ratio:390/760;object-fit:cover;object-position:top}
.une .tel{position:absolute}
.une .tel.a{left:0;top:0;transform:rotate(-4deg);max-width:230px}
.une .tel.b{right:0;top:40px;transform:rotate(4deg);max-width:230px}
.tampon{position:absolute;left:38%%;bottom:-6px;width:120px;height:120px;border-radius:50%%;border:4px solid var(--accent);
 color:var(--accent);display:grid;place-items:center;text-align:center;font-weight:900;font-size:12.5px;line-height:1.15;
 transform:rotate(-12deg);background:rgba(255,255,255,.92);letter-spacing:.06em;text-transform:uppercase;z-index:2}
.tampon b{display:block;font-size:30px;letter-spacing:0}
.chiffres{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:34px 0 8px}
.chiffres div{background:var(--papier);border:1px solid var(--filet);border-radius:14px;padding:14px 16px}
.chiffres b{display:block;font-size:34px;line-height:1;color:var(--action);font-weight:900}
.chiffres span{font-size:14.5px;color:var(--doux)}
section{margin-top:58px}
h2{font-size:clamp(26px,3.6vw,36px);line-height:1.1;margin:0 0 8px;color:var(--fonce)}
.intro{font-size:18px;max-width:720px;margin:0 0 22px}
.num{display:inline-grid;place-items:center;width:38px;height:38px;border-radius:50%%;background:var(--accent);color:#fff;
 font-weight:900;font-size:19px;margin-right:12px;vertical-align:4px}
.etapes{list-style:none;margin:0 0 26px;padding:0;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;counter-reset:e}
.etapes li{background:var(--papier);border:1px solid var(--filet);border-radius:14px;padding:12px 14px;counter-increment:e;font-size:14.5px;color:var(--doux)}
.etapes li b{display:block;color:var(--fonce);font-size:16px;margin-bottom:2px}
.etapes li b::before{content:counter(e);display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%%;background:var(--action);color:#fff;font-size:13px;margin-right:7px;vertical-align:1px}
.trois{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;align-items:start}
.ecran{text-align:center}
.ecran .tel{margin:0 auto 14px;max-width:236px}
.phase{display:inline-block;font-size:12.5px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;border-radius:99px;padding:4px 11px;margin-bottom:6px;background:var(--halo);color:var(--fonce)}
.ecran h3{margin:2px 0 4px;font-size:19px;color:var(--fonce)}
.ecran p{margin:0 auto;font-size:15px;max-width:290px;color:var(--doux)}
.bande{background:var(--fonce);color:#E9EEF2;border-radius:24px;padding:32px;display:grid;grid-template-columns:1fr auto;gap:26px;align-items:center}
.bande h2{color:#fff}
.bande .intro{color:#CBD5DC}
.bande ul{margin:0;padding:0;list-style:none}
.bande li{padding:8px 0 8px 32px;position:relative;font-size:16px}
.bande li::before{content:"✓";position:absolute;left:0;top:8px;width:22px;height:22px;border-radius:50%%;background:var(--accent);color:#fff;font-weight:900;font-size:13px;display:grid;place-items:center}
.gestes{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0;padding:0;list-style:none}
.gestes li{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.25);border-radius:99px;padding:5px 12px;font-size:14px;font-weight:700}
.gestes li::before{display:none}
.tels{display:flex;gap:16px;justify-content:center}
.bande .tel{max-width:200px;box-shadow:0 14px 34px rgba(0,0,0,.4)}
.duo{display:grid;grid-template-columns:1fr 1fr;gap:20px}
.carte{background:var(--papier);border:1px solid var(--filet);border-radius:20px;padding:22px;display:grid;grid-template-columns:auto 1fr;gap:20px;align-items:start}
.carte .tel{max-width:170px;padding:7px;border-radius:24px}
.carte .tel img{border-radius:18px}
.carte h3{margin:4px 0 6px;font-size:22px;color:var(--fonce)}
.carte p{margin:0;font-size:15.5px}
.prix{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.offre{border-radius:20px;padding:24px;border:2px solid var(--filet);background:var(--papier)}
.offre.plus{border-color:var(--action);background:#fff}
.offre .etiq{font-size:13px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--doux)}
.offre .montant{font-size:46px;font-weight:900;color:var(--fonce);line-height:1.1;margin:4px 0 2px}
.offre .montant small{font-size:16px;color:var(--doux);font-weight:700}
.offre ul{margin:12px 0 0;padding-left:20px;font-size:15.5px}
.offre .barre{font-size:26px;color:var(--doux);font-weight:700}
.lancement{display:inline-block;background:#FBEFC4;color:#5C4400;border:1px solid #E7C75A;border-radius:99px;padding:4px 12px;font-size:14px;font-weight:800;margin:4px 0 0}
.besoin{display:flex;flex-wrap:wrap;gap:10px;margin:22px 0 0;padding:0;list-style:none}
.besoin li{background:#fff;border:1px solid var(--filet);border-radius:12px;padding:10px 14px;font-size:15px}
.besoin b{color:var(--fonce)}
.employeur{margin-top:22px;border-left:4px solid var(--accent);background:#fff;border-radius:0 14px 14px 0;padding:16px 20px}
.employeur h3{margin:0 0 4px;font-size:19px;color:var(--fonce)}
.employeur p{margin:0;font-size:15.5px}
/* pourquoi payer le jeu de rôle (Daniel, 28 sept. 2026) */
.versus{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:6px}
.versus article{border-radius:18px;padding:18px 20px;border:1px solid var(--filet);background:var(--papier)}
.versus article.libre{background:var(--fonce);color:#E9EEF2;border-color:var(--fonce)}
.versus h3{margin:0 0 2px;font-size:21px;color:var(--fonce)} .versus .libre h3{color:#fff}
.versus .etiq{font-size:12.5px;font-weight:900;letter-spacing:.1em;text-transform:uppercase;color:var(--doux);margin:0 0 10px}
.versus .libre .etiq{color:var(--halo)}
.versus ul{margin:0;padding:0;list-style:none}
.versus li{padding:7px 0 7px 28px;position:relative;font-size:15.5px;border-top:1px solid rgba(0,0,0,.06)}
.versus .libre li{border-top-color:rgba(255,255,255,.12)}
.versus li::before{content:"•";position:absolute;left:8px;top:6px;font-weight:900;color:var(--doux)}
.versus .libre li::before{content:"✓";left:4px;color:var(--halo)}
.vraie{display:grid;grid-template-columns:auto 1fr auto;gap:22px;align-items:start;margin-top:26px}
.vraie .tel{max-width:230px}
.notes{display:flex;flex-direction:column;gap:12px;padding-top:26px}
.note{background:#fff;border:1px solid var(--filet);border-left:5px solid var(--accent);border-radius:12px;padding:12px 14px;font-size:15.5px}
.note b{color:var(--fonce)}
.pourqui{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-top:22px}
.pourqui div{background:var(--papier);border:1px solid var(--filet);border-radius:14px;padding:14px 16px;font-size:15.5px}
.pourqui b{display:block;color:var(--fonce);font-size:17px;margin-bottom:2px}
.cout{margin-top:18px;background:#FBEFC4;border:1px solid #E7C75A;border-radius:14px;padding:14px 18px;font-size:16.5px}
@media (max-width:860px){ .versus,.pourqui{grid-template-columns:1fr} .vraie{grid-template-columns:1fr} .vraie .tel{margin:0 auto} .notes{padding-top:0} }
.fin{margin:60px 0 0;background:var(--halo);border-radius:24px;padding:30px;text-align:center}
.fin h2{margin-bottom:6px}
.fin p{margin:0 0 16px;font-size:18px}
footer{text-align:center;font-size:13px;color:var(--doux);padding:26px 0 40px}
@media (max-width:860px){
 .une{grid-template-columns:1fr} .une .visuel{min-height:370px;max-width:420px;margin:0 auto;width:100%%}
 .chiffres{grid-template-columns:repeat(2,1fr)} .etapes{grid-template-columns:1fr 1fr}
 .trois,.duo,.prix{grid-template-columns:1fr}
 .bande{grid-template-columns:1fr;padding:24px} .bande .tel{max-width:46%%}
 .carte{grid-template-columns:1fr} .carte .tel{margin:0 auto}
}
@media (max-width:420px){
 .une .tel.a,.une .tel.b{max-width:175px} .tampon{width:96px;height:96px;font-size:10.5px} .tampon b{font-size:24px}
 .une .visuel{min-height:310px} .etapes{grid-template-columns:1fr}
}
@media print{
 @page{size:letter;margin:12mm}
 body{-webkit-print-color-adjust:exact;print-color-adjust:exact;font-size:12px}
 .retour,.cta{display:none} section{margin-top:22px;break-inside:avoid} .tel{box-shadow:none}
}
"""


def images(t):
    """Les captures en JPEG réduit, à côté du dépliant (le PNG pèse 300 Ko)."""
    src = RACINE / "assets" / "presentations" / t["captures"]
    dest = RACINE / "assets" / "presentations" / t["sortie"]
    dest.mkdir(parents=True, exist_ok=True)
    noms = set(t["une"]) | {e[0] for e in t["ecrans"]} | set(t["bande_caps"]) | {a[0] for a in t["appui"]} | {"libre_conv", "libre_bilan"}
    for n in sorted(noms):
        im = Image.open(src / f"{n}.png").convert("RGB")
        im = im.resize((520, round(im.height * 520 / im.width)), Image.LANCZOS)
        im.save(dest / f"{n}.jpg", quality=80, optimize=True)
    return dest, noms


def page(t):
    o = pelerins.offre()
    cap = t["sortie"] + "/"
    tel = lambda n, alt="": f'<div class="tel"><img src="{cap}{n}.jpg" alt="{E(alt)}" loading="lazy"></div>'
    chiffres = "".join(f"<div><b>{E(str(n))}</b><span>{E(s)}</span></div>" for n, s in t["chiffres"])
    etapes = "".join(f"<li><b>{E(a)}</b>{E(b)}</li>" for a, b in t["etapes"])
    ecrans = "".join(f'<div class="ecran">{tel(n, h)}<span class="phase">{E(ph)}</span><h3>{E(h)}</h3><p>{E(p)}</p></div>'
                     for n, ph, h, p in t["ecrans"])
    bande_li = "".join(f"<li>{li}</li>" for li in t["bande_li"])
    gestes = "".join(f"<li>{E(g)}</li>" for g in t["gestes"])
    appui = "".join(f'<div class="carte">{tel(n, h)}<div><h3>{E(h)}</h3><p>{E(p)}</p></div></div>' for n, h, p in t["appui"])
    barre = f'<s class="barre">{prix(o["prixRegulier"])}</s> ' if o["promo"] else ""
    lancement = (f'<p class="lancement">Prix de lancement, pour un temps limité'
                 f'{" — jusqu’au " + date_fr(o["promoFin"]) + " inclusivement" if o["promoFin"] else ""}.</p>') if o["promo"] else ""
    L = t["libre"]
    nbsp = lambda x: x.replace("« ", "«&nbsp;").replace(" »", "&nbsp;»")
    libre_html = f"""<section>
  <h2><span class="num">3</span>{nbsp(E(L['titre']))}</h2>
  <p class="intro">{nbsp(E(L['intro']))}</p>
  <div class="versus">
    <article><p class="etiq">Compris · gratuit</p><h3>Les exercices</h3><ul>{"".join(f"<li>{nbsp(x)}</li>" for x in L['gratuit'])}</ul></article>
    <article class="libre"><p class="etiq">En option · {prix(o["prix"])}</p><h3>{E(t['jeu_nom'])}</h3><ul>{"".join(f"<li>{nbsp(x)}</li>" for x in L['payant'])}</ul></article>
  </div>
  <div class="vraie">
    {tel('libre_conv', L['conv_alt'])}
    <div class="notes">{"".join(f'<div class="note"><b>{E(a)}</b> {nbsp(E(b))}</div>' for a, b in L['notes'])}</div>
    {tel('libre_bilan', L['bilan_alt'])}
  </div>
  <div class="pourqui">{"".join(f"<div><b>{E(a)}</b>{nbsp(E(b))}</div>" for a, b in L['pourqui'])}</div>
  <p class="cout"><b>Moins de {round(o["prix"] / o["conversations"])} ¢ la conversation</b>{" au prix de lancement" if o["promo"] else ""} :
  {o["conversations"]} conversations pour {prix(o["prix"])}, pendant {o["jours"] // 30} mois. Essayez d'abord tout le reste gratuitement ;
  le code s'achète en une minute, quand vous voulez.</p>
</section>"""
    return f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(t['titre'])}</title>
<meta name="description" content="{E(t['sur'])}.">
<link rel="stylesheet" href="/assets/design-system/styles.css">
<link rel="stylesheet" href="/assets/design-system/marque-francis.css">
<link rel="icon" href="/assets/design-system/marque-francis-favicon.svg">
<style>{CSS % t['couleurs']}</style>
</head>
<body>
<div class="fr-barre"><div class="fr-barre__in">
  <span class="fr-lockup"><span class="fr-nom" role="img" aria-label="francis">franc<span class="fr-i" aria-hidden="true">ı<span class="fr-point"></span></span>s</span><span class="fr-trait" aria-hidden="true"></span><span class="fr-desc">{E(t['descripteur'])}</span></span>
  <span class="secteur"><small>{E(t['secteur'])}</small><b>{E(t['enseigne'])}</b></span>
</div></div>

<div class="cadre">
<a class="retour" href="/presentations.html">&#8592; Le classeur</a>

<header class="une">
  <div>
    <p class="sur">{E(t['sur'])}</p>
    <h1>{t['h1']}</h1>
    <p class="chapeau">{E(t['chapeau'])}</p>
    <a class="cta" href="{t['app']}" target="_blank" rel="noopener">Essayer gratuitement</a>
    {bloc(t['app'], t['titre'].split(' — ')[0])}
  </div>
  <div class="visuel" aria-hidden="true">
    <div class="tel a"><img src="{cap}{t['une'][0]}.jpg" alt=""></div>
    <div class="tel b"><img src="{cap}{t['une'][1]}.jpg" alt=""></div>
    <div class="tampon"><span><b>{t['tampon'][0]}</b>{t['tampon'][1]}</span></div>
  </div>
</header>

<div class="chiffres">{chiffres}</div>

<section>
  <h2><span class="num">1</span>{E(t['chemin_tit'])}</h2>
  <p class="intro">{E(t['chemin_intro'])}</p>
  <ol class="etapes">{etapes}</ol>
  <div class="trois">{ecrans}</div>
</section>

<section>
  <div class="bande">
    <div>
      <h2>{E(t['bande_tit'])}</h2>
      <p class="intro">{E(t['bande_intro'])}</p>
      <ul>{bande_li}</ul>
      <ul class="gestes" aria-label="Les gestes travaillés">{gestes}</ul>
    </div>
    <div class="tels">{"".join(tel(n) for n in t['bande_caps'])}</div>
  </div>
</section>

<section>
  <h2><span class="num">2</span>{E(t['appui_tit'])}</h2>
  <div class="duo">{appui}</div>
</section>

{libre_html}

<section>
  <h2><span class="num">4</span>Ce que ça coûte</h2>
  <div class="prix">
    <div class="offre">
      <p class="etiq">Tout le reste</p>
      <p class="montant">Gratuit</p>
      <ul>{"".join(f"<li>{E(x)}</li>" for x in t['gratuit_li'])}</ul>
    </div>
    <div class="offre plus">
      <p class="etiq">En option · {E(t['jeu_nom'])}</p>
      <p class="montant">{barre}{prix(o["prix"])} <small>une fois, pour {o["jours"] // 30} mois</small></p>
      {lancement}
      <ul>{"".join(f"<li>{E(x)}</li>" for x in t['jeu_li'](o))}</ul>
    </div>
  </div>
  <ul class="besoin">
    <li><b>Un téléphone</b> (ou une tablette), dans le navigateur — rien à installer</li>
    <li><b>Des écouteurs</b>, pour l'autobus</li>
    <li><b>Un micro</b> : celui du téléphone suffit</li>
    <li><b>Quinze minutes</b> par jour</li>
  </ul>
  <div class="employeur"><h3>{E(t['employeur'][0])}</h3><p>{E(t['employeur'][1])} Écrivez-nous : <a href="mailto:support@edufrancis.ca">support@edufrancis.ca</a>.</p></div>
</section>

<div class="fin">
  <h2>{E(t['fin_tit'])}</h2>
  <p>{E(t['fin_p'])}</p>
  <a class="cta" href="{t['app']}" target="_blank" rel="noopener">{E(t['fin_cta'])}</a>
</div>

<footer>francis · {E(t['enseigne'])} · portail.edufrancis.ca{t['app']}</footer>
</div>
</body>
</html>
"""


def construire(t):
    dest, noms = images(t)
    html_ = page(t)
    sortie = RACINE / "assets" / "presentations" / f"{t['sortie']}.html"
    sortie.write_text(html_, encoding="utf-8")
    # La copie publique : le classeur demande une connexion, les proches et les
    # clients n'en ont pas. Même page, à côté de l'application, noindex.
    pub_dir = RACINE / t["app"].strip("/") / "depliant"
    pub_dir.mkdir(parents=True, exist_ok=True)
    for n in noms:
        (pub_dir / f"{n}.jpg").write_bytes((dest / f"{n}.jpg").read_bytes())
    pub = (html_.replace(f'src="{t["sortie"]}/', 'src="depliant/')
                .replace('<a class="retour" href="/presentations.html">&#8592; Le classeur</a>', '')
                .replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">'))
    assert t["sortie"] + "/" not in pub
    (pub_dir.parent / "presentation.html").write_text(pub, encoding="utf-8")
    print(sortie.relative_to(RACINE), "+", (pub_dir.parent / "presentation.html").relative_to(RACINE), f"— {len(noms)} captures")


if __name__ == "__main__":
    choix = sys.argv[1:] or ["francoeur", "hotel"]
    for c in choix:
        construire({"francoeur": francoeur, "hotel": hotel}[c]())
