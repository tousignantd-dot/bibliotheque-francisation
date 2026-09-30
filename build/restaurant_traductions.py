#!/usr/bin/env python3
"""Les traductions du lexique de Chez Jocelyne, FIGÉES dans un fichier.

    python3 build/restaurant_traductions.py              # les langues qui manquent
    python3 build/restaurant_traductions.py es           # cette langue, de nouveau
    python3 build/restaurant_traductions.py --interface  # les textes de l'écran seulement
    python3 build/restaurant_traductions.py --ids poele  # quelques entrées, après un changement

Deux langues d'appui seulement, l'espagnol et l'anglais (décision de Daniel du
30 septembre 2026) : ce sont les deux qu'on peut faire relire. Même mécanique
que francoeur_traductions.py (dont on reprend l'appel) : le modèle reçoit le mot
d'ici, l'autre ET la note, car c'est le sens EN CUISINE qui se traduit ; chaque
langue naît `"relu": false`.

Sortie : build/contenu/entreprise-restaurant/traductions.json
"""
import json, pathlib, sys, time, urllib.request

RACINE = pathlib.Path(__file__).resolve().parent.parent
CONTENU = RACINE / "build" / "contenu" / "entreprise-restaurant"
sys.path.insert(0, str(CONTENU))
sys.path.insert(0, str(RACINE / "build"))
from lexique import LEXIQUE, PLANCHES  # noqa: E402
import identite as IDE  # noqa: E402

SORTIE = CONTENU / "traductions.json"
MODELE = "claude-opus-5"
NOMS = {"es": ("espagnol (d'Amérique latine, neutre)", "Español", False),
        "en": ("anglais (nord-américain)", "English", False)}
TRANCHE = 50

SCHEMA = {"type": "object", "properties": {"traductions": {"type": "array", "items": {
    "type": "object", "properties": {"id": {"type": "string"}, "mot": {"type": "string"},
                                     "note": {"type": "string"}},
    "required": ["id", "mot", "note"], "additionalProperties": False}}},
    "required": ["traductions"], "additionalProperties": False}
SCHEMA_UI = {"type": "object", "properties": {"textes": {"type": "array", "items": {
    "type": "object", "properties": {"k": {"type": "string"}, "t": {"type": "string"}},
    "required": ["k", "t"], "additionalProperties": False}}},
    "required": ["textes"], "additionalProperties": False}

# Ce que dit l'écran des planches. Changer une phrase ici oblige à relancer --interface.
INTERFACE = {
    "choisir": "Choisissez votre langue",
    "choisir_sous": "Les mots restent en français. Votre langue vous aide à comprendre.",
    "francais_seul": "Français seulement",
    "francais_seul_sous": "Sans traduction",
    "planches": "Les planches du restaurant",
    "planches_sous": "Touchez une planche, puis un mot pour l'entendre.",
    "cuisine": "Cuisine",
    "salle": "Salle",
    "deux": "Cuisine et salle",
    "toucher": "Touchez un mot pour l'entendre.",
    "ecouter": "Écouter",
    "voir": "Voir dans ma langue",
    "cacher": "Cacher",
    "retour": "Toutes les planches",
    "langue": "Changer de langue",
    "non_relu": "Traduction pas encore vérifiée par une personne.",
    "piege": "Attention",
    "aussi": "On entend aussi",
    "suivant": "Suivant",
    "precedent": "Précédent",
    "mots": "mots",
    "decor": "Dans la cuisine",
    "decor_sous": "Touchez un endroit du poste pour entendre son nom.",
    "fermer": "Fermer",
    # Étape 2 : les exercices
    "accueil": "Accueil",
    "apprendre": "Apprendre les mots",
    "apprendre_sous": "Le poste et les douze planches, mot par mot.",
    "exercer": "Je m'exerce",
    "exercer_sous": "Huit exercices, du mot à la consigne du chef.",
    "exercices": "Les exercices",
    "retour_ex": "Tous les exercices",
    "filtre": "Quels mots ?",
    "tous": "Toutes les planches",
    "a_revoir_filtre": "Mes mots à revoir",
    "rien_a_revoir": "Aucun mot à revoir pour l'instant.",
    "ex_ecoute": "Je l'entends, je le trouve",
    "ex_ecoute_c": "Écoutez, puis touchez la bonne image.",
    "ex_image": "Le mot et son image",
    "ex_image_c": "Touchez le bon mot.",
    "ex_rappel": "Je me souviens",
    "ex_rappel_c": "Dites le mot à voix haute, puis vérifiez.",
    "ex_pieges": "Les pièges",
    "ex_pieges_c": "Écoutez le mot d'ici. Touchez la bonne image.",
    "ex_chef": "La consigne du chef",
    "ex_chef_c": "Écoutez le chef, puis répondez à la question.",
    "ex_commande": "La commande modifiée",
    "ex_commande_c": "Écoutez le client. Touchez la bonne commande.",
    "ex_allergie": "L'allergie",
    "ex_allergie_c": "Écoutez. Que faites-vous ?",
    "ex_redis": "Je le redis",
    "ex_redis_c": "Écoutez, puis redites à voix haute. Ensuite, écoutez le modèle.",
    "reecouter": "Réécouter",
    "lentement": "Plus lentement",
    "voir_mot": "Voir le mot",
    "savais": "Je le savais",
    "a_revoir": "À revoir",
    "bravo": "Bien joué !",
    "essaie": "Pas tout à fait. Essayez encore.",
    "reponse": "Voici la bonne réponse.",
    "fin": "Série terminée",
    "premier_coup": "du premier coup",
    "recommencer": "Une autre série",
    "bruit": "Bruit de cuisine",
    "bruit_0": "Aucun",
    "bruit_1": "Faible",
    "bruit_2": "Fort",
    "regle_titre": "La règle",
    "compris": "J'ai compris, je commence",
    "juste_acte": "Oui, c'est le bon geste.",
    "faux_acte": "Ce n'est pas le bon geste.",
    "grave": "Erreur grave.",
    "grave_sous": "Au test, une seule erreur grave fait échouer.",
    "graves": "erreur(s) grave(s)",
    "phrase": "Ce qui a été dit",
    "a_vous": "À vous : dites-le à voix haute.",
    "modele": "Écouter le modèle",
    "question": "Question",
}
for k, t, _p in PLANCHES:
    INTERFACE["p_" + k] = t
# Les textes des exercices qui se lisent (la question, la règle, les actes) :
# l'appui va dessous. Les phrases ENTENDUES, elles, ne se traduisent pas.
import exercices as EX  # noqa: E402
for n, ligne in enumerate(EX.REGLE, 1):
    INTERFACE[f"regle_{n}"] = ligne
INTERFACE["regle_pref"] = EX.REGLE_PREFERENCE
INTERFACE["regle_cuisine"] = EX.REGLE_CUISINE
INTERFACE["critere_grave"] = EX.CRITERE_GRAVE
INTERFACE["auto_bilan"] = "réussis, selon vous"
for k, texte, _ex in EX.FORMULES:
    INTERFACE["formule_" + k] = texte
for k, texte in EX.SEUILS.items():
    INTERFACE["seuil_" + k] = texte
INTERFACE.update({
    "formules_titre": "Deux phrases à dire",
    "une_ecoute": "Une seule écoute, comme en cuisine.",
    "on_repond": "On répond au chef :",
    "bien_dit": "Je l'ai bien dit",
    "a_refaire": "À refaire",
    "ecouter_acte": "Écouter",
})
for k, t in EX.QUI.items():
    INTERFACE["qui_" + k] = t
for i, _ph, q, *_r in EX.CONSIGNES:
    INTERFACE["q_" + i] = q
# Étape 3 : le test (test.py) — les questions et les actes se traduisent en appui.
import test as TE  # noqa: E402
INTERFACE.update({
    "test": "Mon niveau",
    "test_sous": "Un test de dix minutes, sans note.",
    "t_intro1": "Ce test dure environ dix minutes. Il règle le niveau des situations jouées.",
    "t_intro2": "Ce n'est pas un examen. L'écran ne dit pas si la réponse est bonne : répondez comme vous pouvez.",
    "t_cadrage": "Le test situe votre niveau. Il ne vérifie pas les seuils de la formation (18 mots sur 20, 7 consignes sur 8, 5 commandes sur 6) : ils se vérifient pendant la formation. Seule l'allergie est éliminatoire.",
    "commencer": "Commencer",
    "continuer": "Continuer",
    "partA": "Partie A · Les mots",
    "partA_c": "Écoutez. Touchez l'image du mot entendu.",
    "partB": "Partie B · Une seule écoute",
    "partB_c": "Chaque phrase ne joue qu'une fois. Écoutez bien, puis répondez.",
    "partC": "Partie C · L'allergie",
    "partC_c": "Une seule erreur grave fait échouer cette partie. Lisez et écoutez la règle avant de commencer.",
    "partD": "Partie D · Je le redis",
    "partD_c": "Écoutez, puis redites à voix haute. Votre voix reste sur cet appareil.",
    "jouer_une": "Écouter (une seule fois)",
    "deja_joue": "La phrase a joué. Répondez.",
    "enregistrer": "Enregistrer ma réponse",
    "arreter": "Arrêter",
    "passer": "Passer",
    "micro_refuse": "Le micro n'est pas disponible. Vous pouvez passer.",
    "enregistre": "Réponse enregistrée.",
    "resultat": "Votre résultat",
    "palier_propose": "Niveau proposé pour les situations jouées",
    "p_debutant": "Débutant",
    "p_fonctionnel": "Fonctionnel",
    "p_aise": "À l'aise",
    "pas_examen": "Ce n'est pas une note : le formateur confirme le niveau.",
    "c_reussie": "Allergie : aucune erreur grave.",
    "c_ratee": "Allergie : à reprendre avant de travailler seul.",
    "res_A": "Les mots",
    "res_B": "Une seule écoute",
    "res_D": "Je le redis",
    "cran": "cran",
    "non_note": "à écouter par le formateur",
    "formateur": "Pour le formateur",
    "code": "Code du formateur",
    "ouvrir": "Ouvrir",
    "ecouter_reponse": "Écouter la réponse",
    "pas_de_reponse": "Pas de réponse enregistrée.",
    "confirmer": "Confirmer ce niveau",
    "confirme": "Niveau confirmé par le formateur.",
    "notes": "Notes du formateur",
    "refaire_test": "Refaire le test (l'autre forme)",
    "forme": "Forme",
    "oral_redit": "Ce qui est redit",
    "oral_langue": "La langue",
    "provisoire": "Provisoire : le formateur doit encore écouter vos réponses à voix haute.",
    "res_B_chef": "Une seule écoute · le chef",
    "res_B_commande": "Une seule écoute · les commandes",
    "rien_enregistre": "rien d'enregistré",
    "avant_maintenant": "Avant → maintenant",
    "aucun_nom": "aucun nom",
    "provisoire_micro": "Provisoire : le micro n'était pas disponible. Redites les trois phrases à votre formateur.",
    "avec_formateur": "à faire avec le formateur",
    "oral_de_vive_voix": "Sans micro : écoutez la personne redire la phrase, puis notez.",
    "ia_avis": "Ce que vous dites ou écrivez part à un service d'intelligence artificielle, qui répond. Rien n'est gardé ici.",
    "micro_test": "Le micro n'est pas disponible. Continuez : vous redirez ces phrases à votre formateur.",
    "phrase_a_redire": "La phrase à faire redire",
    "non_evalue": "pas évalué cette fois",
    "aller_verifier": "Aller vérifier à la cuisine",
    "cuisine_dit": "La cuisine vous répond :",
    "reessayer": "Réessayer",
})
import situations as _SI  # noqa: E402
for i, txt in _SI.REPONSES_CUISINE.items():
    INTERFACE["rc_" + i] = txt
# Étape 4 : le service joué (situations.py)
import situations as SI  # noqa: E402
INTERFACE.update({
    "service": "Le service",
    "service_accueil": "En cuisine avec le chef, en salle avec les clients.",
    "service_sous": "Choisissez une situation. Vous parlez, on vous répond.",
    "code_aide": "Il faut le code donné par votre formateur.",
    "code_acces": "Votre code",
    "entrer": "Entrer",
    "code_refuse": "Ce code n'est pas reconnu. Demandez-le à votre formateur.",
    "niveau_jeu": "Niveau",
    "faire_test": "faites d'abord le test « Mon niveau »",
    "porte_cuisine": "En cuisine",
    "porte_cuisine_sous": "Le chef vous parle. Vous êtes commis.",
    "porte_salle": "En salle",
    "porte_salle_sous": "Un client vous parle. Vous servez.",
    "mes_gestes": "Les phrases à dire",
    "ecouter_sans_lire": "Écouter sans lire",
    "parler": "Parler",
    "ecrire": "Ou écrivez ici…",
    "envoyer": "Envoyer",
    "fini": "J'ai fini",
    "voir_bilan": "Voir le bilan",
    "vous": "Vous",
    "erreur_reseau": "Problème de connexion. Réessayez.",
    "voix_indispo": "La voix n'est pas disponible pour le moment.",
    "humeur_neutre": "écoute.",
    "humeur_content": "est content.",
    "humeur_content_f": "est contente.",
    "humeur_hesitant": "hésite.",
    "humeur_impatient": "s'impatiente.",
    "bilan_titre": "Le bilan",
    "gestes_titre": "Les gestes",
    "geste_fait": "fait",
    "geste_manque": "à faire la prochaine fois",
    "geste_inutile": "pas nécessaire ici",
    "bilan_attente": "Relecture du service…",
    "vos_phrases": "Vos phrases, corrigées",
    "autre_situation": "Une autre situation",
    "grave_service": "Erreur grave à l'allergie",
})
for i, _p, _n, _v, _pa, carte, *_r in SI.SITUATIONS:
    INTERFACE["carte_" + i] = carte
for g in SI.GESTES:
    INTERFACE["g_" + g["id"]] = g["nom"]
for n, x in enumerate(TE.ORAL_REDIT):
    INTERFACE[f"or_{n}"] = x
for n, x in enumerate(TE.ORAL_LANGUE):
    INTERFACE[f"ol_{n}"] = x
for f in (1, 2):
    for i, _ph, q, *_r in TE.B_CHEF[f]:
        INTERFACE["q_" + i] = q
    for i, _qui, _v, _ph, _c, actes in TE.C[f]:
        for n, (acte, _s) in enumerate(actes):
            INTERFACE[f"acte_{i}_{n}"] = acte
for i, _qui, _v, _ph, _c, actes in EX.ALLERGIES:
    for n, (acte, _s, pourquoi) in enumerate(actes):
        INTERFACE[f"acte_{i}_{n}"] = acte
        if pourquoi:
            INTERFACE[f"pourquoi_{i}_{n}"] = pourquoi


def cle():
    for l in (pathlib.Path.home() / "Claude" / ".env").read_text().splitlines():
        if l.startswith("ANTHROPIC_API_KEY="):
            return l.split("=", 1)[1].strip().strip('"').strip("'")


def appel(contenu, schema):
    corps = {"model": MODELE, "max_tokens": 16000,
             "output_config": {"effort": "medium", "format": {"type": "json_schema", "schema": schema}},
             "fallbacks": "default", "messages": [{"role": "user", "content": contenu}]}
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=json.dumps(corps).encode(),
        headers={"x-api-key": cle(), "anthropic-version": "2023-06-01",
                 "anthropic-beta": "server-side-fallback-2026-07-01",
                 "content-type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=600) as r:
        d = json.loads(r.read())
    if d.get("stop_reason") in ("refusal", "max_tokens"):
        raise RuntimeError(d.get("stop_reason"))
    u = d.get("usage", {})
    print(f"    {time.time()-t0:5.1f} s  {u.get('input_tokens')} → {u.get('output_tokens')} jetons", flush=True)
    return json.loads("".join(b.get("text", "") for b in d["content"] if b["type"] == "text"))


def consigne(nom, entrees):
    titres = {k: t for k, t, _ in PLANCHES}
    lignes = [f"- id={e[0]} | planche : {titres[e[1]]} | mot au Québec : {e[2]}"
              + (f" | aussi dit : {e[3]}" if e[3] else "")
              + (f" | note : {e[5]}" if e[5] else "") for e in entrees]
    return (
        f"Tu traduis le lexique d'un restaurant familial du Québec ({IDE.NOM} : déjeuners, poutine, "
        f"pâté chinois, pour emporter) vers l'{nom}, pour des EMPLOYÉS de cuisine et de salle qui "
        "apprennent le français et doivent reconnaître ces mots quand le chef ou un client les dit.\n\n"
        "Pour chaque entrée :\n"
        "- `mot` : l'équivalent le plus courant dans la langue cible pour CE QUE LE MOT DÉSIGNE AU "
        "RESTAURANT, pas une traduction littérale. Sers-toi de « aussi dit » et de la note pour lever "
        "l'ambiguïté (au Québec, « le poêle » est la cuisinière, « une liqueur » est une boisson "
        "gazeuse, « le dîner » est le repas du midi). Un plat du Québec sans équivalent garde son nom "
        "français suivi d'une courte glose (ex. « poutine (papas fritas con queso y salsa) »). Un à six "
        "mots, sans explication.\n"
        "- `note` : la note traduite en une phrase courte et simple, ou une chaîne vide si l'entrée n'a "
        "pas de note. Ne traduis pas les mots français cités entre guillemets : garde-les en français, "
        "c'est ce que l'employé doit reconnaître. Garde le préfixe « PIÈGE : » traduit par le mot "
        "« Attention : » de la langue cible.\n"
        "Rends TOUTES les entrées, avec leur `id` exact, dans l'ordre.\n\n" + "\n".join(lignes))


def traduire_mots(code, entrees):
    nom = NOMS[code][0]
    rendu = {}
    for i in range(0, len(entrees), TRANCHE):
        d = appel(consigne(nom, entrees[i:i + TRANCHE]), SCHEMA)
        rendu.update({t["id"]: {"mot": t["mot"], "note": t["note"]} for t in d["traductions"]})
    manque = [e[0] for e in entrees if e[0] not in rendu]
    if manque:
        raise RuntimeError(f"{code} : {len(manque)} manquantes {manque[:6]}")
    return rendu


def traduire_interface(code):
    # Par tranches de 60 : à 205 textes d'un bloc, la connexion se fermait
    # avant la fin (30 sept. 2026), comme les longues langues de Francœur.
    nom = NOMS[code][0]
    cles = list(INTERFACE)
    ui = {}
    for i in range(0, len(cles), 60):
        lignes = "\n".join(f"- k={k} | {INTERFACE[k]}" for k in cles[i:i + 60])
        d = appel(f"Traduis vers l'{nom} les textes de l'écran d'une application où des employés de "
                  "restaurant apprennent le vocabulaire français de leur travail. Textes courts, clairs, "
                  "vouvoiement ou forme polie neutre, ton simple. Les `acte_…` sont des gestes de l'employé, "
                  "à la première personne : garde-les à la première personne. Garde EN FRANÇAIS les phrases citées "
                  "entre « » (ce que l'employé dit à voix haute) ; mais les NOMS d'aliments et d'allergènes hors "
                  "guillemets se TRADUISENT, sans ajouter de guillemets (« arachides » → maní / peanuts). « La salle » est la salle à manger "
                  "du restaurant (où sont les clients), « le serveur » la personne qui sert. Rends chaque `k` exact.\n\n"
                  + lignes, SCHEMA_UI)
        ui.update({x["k"]: x["t"] for x in d["textes"]})
    manque = [k for k in INTERFACE if k not in ui]
    if manque:
        raise RuntimeError(f"{code} interface : manquent {manque[:8]}")
    return ui


def main():
    args = sys.argv[1:]
    data = json.loads(SORTIE.read_text(encoding="utf-8")) if SORTIE.exists() else {}
    codes = [a for a in args if a in NOMS] or [c for c in IDE.LANGUES_APPUI if c not in data]
    if "--interface" in args:
        codes = [a for a in args if a in NOMS] or list(IDE.LANGUES_APPUI)
    ids = args[args.index("--ids") + 1:] if "--ids" in args else None
    for code in codes:
        print(f"  {code}", flush=True)
        v = data.setdefault(code, {"loc": NOMS[code][1], "rtl": NOMS[code][2], "relu": False, "mots": {}})
        if "--interface" not in args:
            entrees = [e for e in LEXIQUE if not ids or e[0] in ids]
            v["mots"].update(traduire_mots(code, entrees))
            if ids:
                v["relu"] = False
        v["interface"] = traduire_interface(code)
        SORTIE.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("→", SORTIE.relative_to(RACINE))


if __name__ == "__main__":
    main()
