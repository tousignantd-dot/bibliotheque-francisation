"""Le test de positionnement de Chez Jocelyne (étape 3).

    python3 build/contenu/entreprise-restaurant/test.py   # vérifie et compte

Il sert à UNE chose : régler le palier des situations jouées (étape 4), et se
repasse à la fin (l'écart entre les deux passations est la preuve
d'apprentissage). Ce n'est pas un examen. Dix à douze minutes. Le test SITUE ;
il ne certifie pas les seuils du cadrage (18 mots sur 20, 7 consignes sur 8,
5 commandes sur 6), qui se vérifient au pilote — l'écran le dit. Seule
l'allergie est éliminatoire, ici comme au cadrage.

QUATRE PARTIES, alignées sur le cadrage (restauration_etape0.py) :
  A · les mots (O3)           ADAPTATIVE, la seule : cran 1 (distracteurs d'autres
                              planches), cran 2 (même planche), cran 3 (les pièges,
                              contrastes écrits à la main, AUTRES que ceux des
                              exercices). Quatre items par cran ; trois bonnes
                              valident et font monter, deux erreurs arrêtent.
                              Voix d'un client (Thierry), jamais celle des planches.
  B · entendu une fois        PASSÉE EN ENTIER (ce sont deux compétences, pas deux
                              crans — leçon du test de l'hôtel) : quatre consignes
                              du chef (O1), dans le bruit faible, puis quatre
                              commandes (O4). UNE seule écoute, la condition de
                              l'objectif.
  C · l'allergie (O2)         ÉLIMINATOIRE, dit d'avance : la règle et le critère
                              de gravité d'exercices.py s'affichent AVANT (la même
                              source, jamais réécrite). Cinq cas par forme, dont un
                              contre-exemple et au moins deux où le bon geste porte
                              le mauvais allergène ou la mauvaise table.
  D · redire à voix haute     Trois phrases (deux au chef, une au client),
    (O1, O4)                  enregistrées SUR L'APPAREIL, écoutées et notées par
                              le formateur sur deux lignes : ce qui est redit, et
                              la langue.

AUCUNE RÉTROACTION pendant le test : ni vert ni rouge, ni phrase écrite après.

DES CAS NEUFS : aucune phrase des exercices (vérifié par verifier()). La partie
A porte forcément sur les mots des planches — c'est ce qu'elle mesure.

DEUX FORMES PARALLÈLES, nivelées, la première tirée AU HASARD, l'autre à la
passation suivante (sinon la différence de formes se lit comme un apprentissage).
"""

# ── A · les mots ─────────────────────────────────────────────────────────
A = {
    1: {1: ["friteuse", "louche", "tomate", "assiette"],
        2: ["passoire", "champignon", "gants", "plateau"],
        3: [("poele", ["poele-appareil", "bac", "fouet"]),
            ("patates", ["pomme", "carotte", "citron"]),
            ("liqueur", ["cafe", "tasse", "creme"]),
            ("alg-arachides", ["alg-noix", "alg-moutarde", "alg-ble"])]},
    2: {1: ["four", "fouet", "oignon", "verre"],
        2: ["rape", "poivron", "tablier", "napperon"],
        3: [("poele-appareil", ["poele", "hotte", "four"]),
            ("ble-inde", ["feves", "pates", "farine"]),
            ("roties", ["pain", "pain-dore", "tarte-sucre"]),
            ("bleuets", ["citron", "sirop-erable", "pomme"])]},
}
A_VALIDE, A_ARRET = 3, 2   # trois bonnes montent d'un cran ; deux erreurs arrêtent

# ── B · entendu une fois ─────────────────────────────────────────────────
# Le chef : (id, phrase, question, bonne, [distracteurs]) — même règle que les
# exercices : un autre objet nommé parmi les choix, aucun choix nommé dans la question.
B_CHEF = {
    1: [("t1", "Va porter les verres sales au lave-vaisselle, pas à l'évier.", "Où vont les verres ?",
         "lave-vaisselle", ["evier", "lavabo", "poubelle"]),
        ("t2", "Passe-moi la spatule, pis ramasse la pince qui est tombée.", "Qu'est-ce qu'il faut passer au chef ?",
         "spatule", ["pince", "louche", "fouet"]),
        ("t3", "Mets les œufs dans le frigo, pas dans le congélateur.", "Où vont les œufs ?",
         "frigo", ["congelateur", "chambre-froide", "four"]),
        ("t4", "Émince les oignons. Le persil, je l'ai déjà haché.", "Quel geste faut-il faire ?",
         "emincer", ["hacher", "en-des", "trancher"])],
    2: [("t5", "Sers la soupe avec la louche, pis mets-la dans le bol.", "Avec quoi faut-il servir ?",
         "louche", ["bol-soupe", "tasse-mesurer", "pince"]),
        ("t6", "Va chercher le bœuf haché dans la chambre froide, pis mets-le sur la plaque.", "Où va le bœuf haché, à la fin ?",
         "plaque", ["chambre-froide", "four", "poele"]),
        ("t7", "Coupe les tomates en tranches, pas en dés.", "Comment faut-il couper les tomates ?",
         "trancher", ["en-des", "julienne", "hacher"]),
        ("t8", "Mets ton filet avant d'entrer, pis lave-toi les mains au lavabo.", "Qu'est-ce qu'il faut mettre ?",
         "filet", ["lavabo", "gants", "tablier"])],
}
# La commande : (id, voix, phrase, bonne (plat, changement, ingrédient), autre)
# — les cartes se construisent comme aux exercices (une carte ne diffère que par
# le changement ; vote majoritaire nul). Cuisson : trois cartes du même plat.
B_COMMANDE = {
    1: [("q1", "f", "Un club, sans laitue, s'il vous plaît.", ("club", "sans", "laitue"), ("hamburger", "extra", "fromage")),
        ("q2", "m", "Une poutine, avec les oignons à part.", ("poutine", "a-part", "oignon"), ("frites", "extra", "bacon")),
        ("q3", "f", "Des crêpes, avec un extra de beurre.", ("crepes", "extra", "beurre"), ("roties", "sans", "sirop-erable")),
        ("q4", "m", "Mon steak, bien cuit… non, à point.", ("steak", "a-point", None), None)],
    2: [("q5", "m", "Un hamburger sans tomates, s'il vous plaît.", ("hamburger", "sans", "tomate"), ("club", "a-part", "bacon")),
        ("q6", "f", "Des frites, avec un extra fromage.", ("frites", "extra", "fromage"), ("poutine", "sans", "champignon")),
        ("q7", "m", "Du pain doré, avec le beurre à part.", ("pain-dore", "a-part", "beurre"), ("crepes", "extra", "sirop-erable")),
        ("q8", "f", "Le steak, saignant, s'il vous plaît.", ("steak", "saignant", None), None)],
}
VOIX_CHEF = "m"

# ── C · l'allergie (éliminatoire) ────────────────────────────────────────
# Même format qu'exercices.ALLERGIES, SANS « pourquoi » : le test ne rétroagit pas.
# (id, qui, voix, phrase, contre-exemple ?, [(acte, statut)])
C = {
    1: [("u1", "client", "f", "Je suis allergique aux noix. Il y en a dans la tarte au sucre ?", False, [
            ("Je vérifie avec la cuisine s'il y a des noix.", "juste"),
            ("Je vérifie avec la cuisine s'il y a des arachides.", "grave"),
            ("Non, il n'y a jamais de noix dans la tarte au sucre.", "grave")]),
        ("u2", "salle", "m", "Table trois, le hamburger : allergie à la moutarde !", False, [
            ("Je redis « moutarde, table trois » et je vérifie la sauce.", "juste"),
            ("Je redis « moutarde, table cinq » et je vérifie la sauce.", "grave"),
            ("J'enlève la sauce, pis j'envoie le hamburger comme d'habitude.", "grave")]),
        ("u3", "client", "m", "J'ai une allergie… euh, à quelque chose. Le club, je peux le manger ?", False, [
            ("Pardon, vous êtes allergique à quoi ?", "juste"),
            ("Oui, le club, vous pouvez le manger.", "grave"),
            ("J'écris « allergie » sur la commande.", "grave")]),
        ("u4", "client", "f", "Pas de fromage dans mon hamburger. Je n'en mange pas, c'est tout.", True, [
            ("J'écris « sans fromage », c'est tout.", "juste"),
            ("J'annonce une allergie au fromage à la cuisine.", "faux"),
            ("Je refuse : il vient toujours avec du fromage.", "faux")]),
        ("u5", "chef", "m", "Allergie au sésame, table un ! Pas de pain aux graines.", False, [
            ("« Oui, chef : sésame, table un. » Je prends un autre pain.", "juste"),
            ("« Oui, chef : soya, table un. » Je prends un autre pain.", "grave"),
            ("Je gratte les graines du pain, ça va aller plus vite.", "grave")])],
    2: [("u6", "client", "m", "Ma femme est allergique aux œufs. Il y en a dans les crêpes ?", False, [
            ("Je vérifie avec la cuisine pour les œufs.", "juste"),
            ("Je vérifie avec la cuisine pour le lait.", "grave"),
            ("Non, nos crêpes sont faites sans œufs, monsieur.", "grave")]),
        ("u7", "salle", "f", "Table sept, les frites : allergie au poisson !", False, [
            ("Je redis « poisson, table sept » et je vérifie la friteuse.", "juste"),
            ("Je redis « poisson, table huit » et je vérifie la friteuse.", "grave"),
            ("Je fais les frites comme d'habitude : ce n'est pas du poisson.", "grave")]),
        ("u8", "client", "f", "Je ne tolère pas le blé. Le hot chicken, je peux le manger ?", False, [
            ("C'est une allergie ? Je vérifie avec la cuisine pour le blé.", "juste"),
            ("Oui, le hot chicken, vous pouvez le manger, madame.", "grave"),
            ("C'est une allergie ? Je vérifie avec la cuisine pour le lait.", "grave")]),
        ("u9", "client", "m", "Pas de champignons dans ma poutine : je n'aime pas le goût.", True, [
            ("J'écris « sans champignons », c'est tout.", "juste"),
            ("J'annonce une allergie aux champignons à la cuisine.", "faux"),
            ("Je refuse : on ne change pas la poutine ici.", "faux")]),
        ("u10", "chef", "m", "Allergie aux arachides, table cinq ! Lave la planche avant de commencer.", False, [
            ("« Oui, chef : arachides, table cinq. » Je lave la planche.", "juste"),
            ("« Oui, chef : arachides, table neuf. » Je lave la planche.", "grave"),
            ("Je commence tout de suite, la planche a l'air propre.", "grave")])],
}

# ── D · redire à voix haute ──────────────────────────────────────────────
# (id, qui, voix, phrase entendue, ce qu'on attend — le modèle, joué au formateur)
D = {
    1: [("d1", "chef", "m", "Va chercher deux bacs de laitue, pis mets-les sur la ligne.", "Oui, chef : deux bacs de laitue sur la ligne."),
        ("d2", "chef", "m", "Monte la friteuse, pis sors les frites dans cinq minutes.", "Oui, chef : les frites dans cinq minutes."),
        ("d3", "client", "f", "Deux hamburgers, dont un sans oignons, s'il vous plaît.", "Deux hamburgers, un sans oignons, c'est bien ça ?")],
    2: [("d4", "chef", "m", "Sors trois steaks du frigo, pis mets-les sur la plaque.", "Oui, chef : trois steaks sur la plaque."),
        ("d5", "chef", "m", "Lave le chaudron, pis rapporte-moi la passoire.", "Oui, chef : je lave le chaudron et je rapporte la passoire."),
        ("d6", "client", "m", "Une poutine, pis un club sans tomates, s'il vous plaît.", "Une poutine et un club sans tomates, c'est bien ça ?")],
}
ORAL_REDIT = ["Tout redit", "En partie", "Rien ou faux"]
ORAL_LANGUE = ["Formule attendue", "Compréhensible", "Incompréhensible"]
CODE_FORMATEUR = "2413"

# ── Le palier, en données, appliqué une seule fois par la page ───────────
#   debutant   : A ≤ DEBUTANT_A ou B ≤ DEBUTANT_B
#   aise       : A == 3, B ≥ AISE_B, C réussie, et (oral non noté, ou au moins
#                ORAL_AISE « tout redit » et au plus un « incompréhensible »)
#   fonctionnel: sinon
# C ratée ne change pas seulement le palier : l'écran dit « L'allergie est à
# reprendre avant de travailler seul », au formateur comme à l'apprenant.
DEBUTANT_A, DEBUTANT_B, AISE_B, ORAL_AISE = 1, 3, 7, 2
PALIERS = ["debutant", "fonctionnel", "aise"]


def verifier():
    import importlib.util, pathlib, re
    ici = pathlib.Path(__file__).parent

    def charger(nom):
        spec = importlib.util.spec_from_file_location(f"resto_{nom}", ici / f"{nom}.py")
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
    L, EX = charger("lexique"), charger("exercices")
    img = {e[0] for e in L.LEXIQUE if e[4] == "croquis"}
    mots = {e[0]: e[2] for e in L.LEXIQUE}
    planche = {e[0]: e[1] for e in L.LEXIQUE}
    deja = {x[1] for x in EX.CONSIGNES} | {x[2] for x in EX.COMMANDES} | {x[3] for x in EX.ALLERGIES}
    for f in (1, 2):
        mots_a = A[f][1] + A[f][2] + [x for x, _ in A[f][3]]
        assert all(m in img for m in mots_a), f"forme {f} : mot sans croquis"
        assert len(set(mots_a)) == len(mots_a) == 12, f"forme {f} : 12 mots distincts"
        for x, c in A[f][3]:
            assert all(m in img for m in c) and mots[x].strip(), x
            ex = dict(EX.PIEGES).get(x)
            assert ex is None or set(c) != set(ex), f"{x} : mêmes contrastes qu'aux exercices"
        # les deux formes ne partagent aucun mot
    a1 = set(A[1][1] + A[1][2] + [x for x, _ in A[1][3]]); a2 = set(A[2][1] + A[2][2] + [x for x, _ in A[2][3]])
    assert not a1 & a2, f"mots communs aux deux formes : {a1 & a2}"

    def nomme(ident, phrase):
        tete = re.sub(r"^(le |la |les |l'|un |une |des )", "", mots[ident].lower()).split(" ")[0]
        base = tete[:-1] if tete.endswith(("s", "x")) and len(tete) > 4 else tete
        return bool(re.search(r"(?<![\w-])" + re.escape(base) + r"[sx]?(?![\w-])", phrase.lower()))
    for f in (1, 2):
        n_autre = 0
        for i, ph, q, b, d in B_CHEF[f]:
            assert ph not in deja, f"{i} : phrase des exercices"
            assert b in img and all(x in img for x in d) and len(set([b] + d)) == 4, i
            noms = [x for x in [b] + d if re.match(r"^(le |la |les |l'|un |une |des )", mots[x])]
            assert not any(nomme(x, q) for x in noms), f"{i} : un choix est nommé dans la question"
            n_autre += any(nomme(x, ph) for x in d)
        assert n_autre * 2 >= len(B_CHEF[f]), f"forme {f} : trop peu de consignes à autre objet nommé"
        for i, _v, ph, bon, autre in B_COMMANDE[f]:
            assert ph not in deja, i
            if bon[2] is None:
                assert bon[1] in EX.CUISSONS and autre is None, i
            else:
                assert all(a != b for a, b in zip(bon, autre)) and all(x in img for x in (bon[0], bon[2], autre[0], autre[2])), i
        assert sum(x[3][2] is None for x in B_COMMANDE[f]) == 1, f"forme {f} : une cuisson par forme"
        # C : un contre-exemple, au moins deux « voisins », la juste nomme le bon
        ALG = ["arachides", "noix", "sésame", "soya", "poisson", "fruits de mer", "lait", "œufs", "moutarde", "blé"]
        TAB = [f"table {n}" for n in ("un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf")]
        def noms_c(t):
            t = t.lower(); return {a for a in ALG + TAB if re.search(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])", t)}
        contre = voisins = 0
        for i, qui, _v, ph, c, actes in C[f]:
            assert ph not in deja and qui in EX.QUI, i
            assert sum(s == "juste" for _a, s in actes) == 1, i
            n = [len(a) for a, _s in actes]
            assert max(n) <= 1.25 * min(n) + 6, f"{i} : longueurs {n}"
            contre += c
            if c:
                continue
            assert any(s == "grave" for _a, s in actes), i
            for a, s in actes:
                if s == "faux":
                    assert not re.search(r"correct|conseille|prenez|pas de problème|manger", a.lower()), f"{i} : « {a} » devrait être grave"
            juste = next(a for a, s in actes if s == "juste")
            if any(s == "grave" and noms_c(a) and not noms_c(a) <= noms_c(ph) for a, s in actes):
                voisins += 1
                assert noms_c(juste) & noms_c(ph), f"{i} : la juste ne nomme pas le bon allergène ou la bonne table"
        assert contre == 1, f"forme {f} : un contre-exemple"
        assert voisins >= 2, f"forme {f} : {voisins} cas « voisins »"
        plus_longue = sum(max(a, key=lambda x: len(x[0]))[1] == "juste" for *_x, a in C[f])
        assert plus_longue <= 2, f"forme {f} : la bonne est la plus longue {plus_longue} fois"
        for i, qui, _v, ph, _m in D[f]:
            assert ph not in deja and qui in ("chef", "client"), i
    return True


if __name__ == "__main__":
    verifier()
    for f in (1, 2):
        print(f"forme {f} : A {sum(len(v) for v in A[f].values())} mots · B {len(B_CHEF[f])} consignes + "
              f"{len(B_COMMANDE[f])} commandes · C {len(C[f])} allergies · D {len(D[f])} à redire")
