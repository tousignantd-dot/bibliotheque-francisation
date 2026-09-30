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
}
for k, t, _p in PLANCHES:
    INTERFACE["p_" + k] = t


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
    nom = NOMS[code][0]
    lignes = "\n".join(f"- k={k} | {t}" for k, t in INTERFACE.items())
    d = appel(f"Traduis vers l'{nom} les textes de l'écran d'une application où des employés de "
              "restaurant apprennent le vocabulaire français de leur travail. Textes courts, clairs, "
              "vouvoiement ou forme polie neutre, ton simple. Rends chaque `k` exact.\n\n" + lignes,
              SCHEMA_UI)
    ui = {x["k"]: x["t"] for x in d["textes"]}
    manque = [k for k in INTERFACE if k not in ui]
    if manque:
        raise RuntimeError(f"{code} interface : manquent {manque}")
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
