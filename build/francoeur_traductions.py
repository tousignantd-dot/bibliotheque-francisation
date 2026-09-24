#!/usr/bin/env python3
"""Les traductions du lexique de la Maison Francœur, FIGÉES dans un fichier.

    python3 build/francoeur_traductions.py            # les langues qui manquent
    python3 build/francoeur_traductions.py es ar      # ces langues-là, de nouveau

Décision de Daniel du 24 septembre 2026 : les onze langues de l'outil de
traduction dès le départ. Figées plutôt que demandées en direct, pour deux
raisons : le mode sans assistance d'un centre retire la traduction en direct,
et c'est précisément l'employeur qui l'aurait refusée qui a acheté la trousse ;
et une traduction relue une fois vaut mieux que onze tirages différents.

CHAQUE LANGUE NAÎT « NON RELUE » (`"relu": false`) et le reste tant qu'un
locuteur ne l'a pas validée. La page des planches l'affiche.

Le modèle reçoit le mot d'ici ET l'autre mot ET la note : « une veste » seul se
traduirait « jacket » ; avec « un gilet sans manches » et le piège écrit, il
rend « chaleco ». C'est le sens au magasin qui se traduit, pas le mot.

Appels en bibliothèque standard, comme `server.py` — le dépôt n'a aucune
dépendance externe, et un script de build n'en ajoute pas une pour onze appels.

LA LANGUE D'APPUI DE L'ÉCRAN (`--interface`) : les consignes et les boutons
de la page des planches, plus le nom des onze rayons. Elle va SOUS le français,
jamais à sa place (règle des trois couches) — le contenu à apprendre ne se
traduit pas, la consigne qui l'explique, si.

    python3 build/francoeur_traductions.py --interface   # l'écran, dans les onze langues

Sortie : build/contenu/entreprise-francoeur/traductions.json
"""
import json, pathlib, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build" / "contenu" / "entreprise-francoeur"))
from lexique import LEXIQUE, PLANCHES  # noqa: E402

SORTIE = RACINE / "build" / "contenu" / "entreprise-francoeur" / "traductions.json"
MODELE = "claude-opus-5"

# Les onze de VOC_LANGUES (build/gabarit/vocab.js) — même liste, même ordre.
LANGUES = [("ar", "arabe", "العربية", True), ("es", "espagnol", "Español", False),
           ("uk", "ukrainien", "Українська", False), ("fa", "persan", "فارسی", True),
           ("zh", "chinois (mandarin, caractères simplifiés)", "中文", False),
           ("pt", "portugais (du Brésil)", "Português", False),
           ("en", "anglais (nord-américain)", "English", False),
           ("ro", "roumain", "Română", False), ("ur", "ourdou", "اردو", True),
           ("ru", "russe", "Русский", False), ("ti", "tigrigna", "ትግርኛ", False)]

SCHEMA = {
    "type": "object",
    "properties": {"traductions": {"type": "array", "items": {
        "type": "object",
        "properties": {"id": {"type": "string"}, "mot": {"type": "string"},
                       "note": {"type": "string"}},
        "required": ["id", "mot", "note"], "additionalProperties": False}}},
    "required": ["traductions"], "additionalProperties": False}


def cle():
    for l in (pathlib.Path.home() / "Claude" / ".env").read_text().splitlines():
        if l.startswith("ANTHROPIC_API_KEY="):
            return l.split("=", 1)[1].strip().strip('"').strip("'")


def consigne(nom_langue, entrees=LEXIQUE):
    titres = dict(PLANCHES)
    lignes = [f"- id={e[0]} | rayon : {titres[e[1]]} | mot au Québec : {e[2]}"
              + (f" | aussi dit : {e[3]}" if e[3] else "")
              + (f" | note : {e[5]}" if e[5] else "") for e in entrees]
    return (
        f"Tu traduis le lexique d'un magasin de vêtements du Québec vers le {nom_langue}, pour "
        "des EMPLOYÉS qui apprennent le français et qui doivent reconnaître ces mots quand un "
        "client les dit.\n\n"
        "Pour chaque entrée :\n"
        "- `mot` : l'équivalent le plus courant dans la langue cible pour CE QUE LE MOT DÉSIGNE "
        "AU MAGASIN — pas une traduction littérale. Sers-toi de « aussi dit » et de la note pour "
        "lever l'ambiguïté (au Québec, « une veste » est SANS manches ; « des bas » sont des "
        "chaussettes ; « une sacoche » est un sac à main). Un à quatre mots, sans article "
        "superflu si la langue n'en a pas, sans explication, sans parenthèses.\n"
        "- `note` : la note traduite en une phrase courte et simple, ou une chaîne vide si "
        "l'entrée n'a pas de note. Ne traduis pas les mots français cités entre guillemets : "
        "garde-les en français, c'est ce que l'employé doit reconnaître.\n"
        "- Couleurs et tailles : l'adjectif ou le nom usuel de la langue cible.\n"
        "Rends TOUTES les entrées, avec leur `id` exact, dans l'ordre.\n\n"
        + "\n".join(lignes))


# Par tranches : en une seule réponse, les langues aux écritures les plus longues
# (persan, ukrainien, ourdou, tigrigna) voyaient la connexion se fermer avant la
# fin, quatre fois sur quatre le 24 septembre 2026. Trois tranches de cinquante.
TRANCHE = 50


def traduire(code, nom):
    rendu = {}
    for i in range(0, len(LEXIQUE), TRANCHE):
        rendu.update(traduire_tranche(code, nom, LEXIQUE[i:i + TRANCHE]))
    manque = [e[0] for e in LEXIQUE if e[0] not in rendu]
    if manque:
        raise RuntimeError(f"{len(manque)} entrées manquantes : {manque[:6]}")
    return rendu


def traduire_tranche(code, nom, entrees):
    corps = {"model": MODELE, "max_tokens": 16000,
             "output_config": {"effort": "medium",
                               "format": {"type": "json_schema", "schema": SCHEMA}},
             "fallbacks": "default",
             "messages": [{"role": "user", "content": consigne(nom, entrees)}]}
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=json.dumps(corps).encode(),
        headers={"x-api-key": cle(), "anthropic-version": "2023-06-01",
                 "anthropic-beta": "server-side-fallback-2026-07-01",
                 "content-type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=600) as r:
        d = json.loads(r.read())
    if d.get("stop_reason") == "refusal":
        raise RuntimeError(f"refus : {d.get('stop_details')}")
    if d.get("stop_reason") == "max_tokens":
        raise RuntimeError("réponse coupée (max_tokens)")
    texte = "".join(b.get("text", "") for b in d["content"] if b["type"] == "text")
    rendu = {t["id"]: {"mot": t["mot"], "note": t["note"]}
             for t in json.loads(texte)["traductions"]}
    u = d.get("usage", {})
    print(f"  {code}  {len(rendu)} mots  {time.time()-t0:5.1f} s  "
          f"{u.get('input_tokens')} → {u.get('output_tokens')} jetons", flush=True)
    return rendu


# Ce que dit l'écran. Changer une phrase ici oblige à relancer --interface.
INTERFACE = {
    "choisir": "Choisissez votre langue",
    "choisir_sous": "Les mots restent en français. Votre langue vous aide à comprendre.",
    "francais_seul": "Français seulement",
    "rayons": "Les rayons du magasin",
    "toucher": "Touchez un vêtement pour l'entendre.",
    "ecouter": "Écouter",
    "voir": "Voir dans ma langue",
    "cacher": "Cacher",
    "retour": "Retour aux rayons",
    "langue": "Changer de langue",
    "non_relu": "Traduction pas encore vérifiée par une personne.",
    "piege": "Attention",
    "aussi": "On entend aussi",
    "suivant": "Suivant",
    "precedent": "Précédent",
    "mots": "mots",
}


def traduire_interface(code, nom):
    textes = dict(INTERFACE)
    textes.update({f"planche_{k}": t for k, t in PLANCHES})
    schema = {"type": "object", "properties": {k: {"type": "string"} for k in textes},
              "required": list(textes), "additionalProperties": False}
    corps = {"model": MODELE, "max_tokens": 8000,
             "output_config": {"effort": "medium", "format": {"type": "json_schema", "schema": schema}},
             "fallbacks": "default",
             "messages": [{"role": "user", "content":
                 f"Traduis vers le {nom} ces textes d'interface d'une application qui apprend le "
                 "français à des employés d'un magasin de vêtements. Phrases courtes, simples, "
                 "ton poli et direct, comme sur un bouton ou une consigne. Garde chaque clé. "
                 "Les clés planche_* sont des noms de rayons.\n\n"
                 + json.dumps(textes, ensure_ascii=False, indent=1)}]}
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages", data=json.dumps(corps).encode(),
        headers={"x-api-key": cle(), "anthropic-version": "2023-06-01",
                 "anthropic-beta": "server-side-fallback-2026-07-01",
                 "content-type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
    if d.get("stop_reason") != "end_turn":
        raise RuntimeError(f"arrêt : {d.get('stop_reason')} {d.get('stop_details')}")
    texte = "".join(b.get("text", "") for b in d["content"] if b["type"] == "text")
    rendu = json.loads(texte)
    print(f"  {code}  interface, {len(rendu)} textes", flush=True)
    return rendu


def main_interface():
    tout = json.loads(SORTIE.read_text(encoding="utf-8"))
    def un(l):
        try:
            return l[0], traduire_interface(l[0], l[1])
        except Exception as e:
            print(f"  {l[0]}  ÉCHEC {e}", flush=True)
            return l[0], None
    with ThreadPoolExecutor(6) as pool:
        for code, rendu in pool.map(un, [l for l in LANGUES if l[0] in tout]):
            if rendu:
                tout[code]["interface"] = rendu
    SORTIE.write_text(json.dumps(tout, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"interface → {sum('interface' in v for v in tout.values())}/{len(tout)} langues")


def main():
    if "--interface" in sys.argv:
        return main_interface()
    tout = json.loads(SORTIE.read_text(encoding="utf-8")) if SORTIE.exists() else {}
    demandees = sys.argv[1:]
    cibles = [l for l in LANGUES if (l[0] in demandees) or (not demandees and l[0] not in tout)]
    if not cibles:
        print("Les onze langues sont déjà là. Nommer une langue pour la refaire.")
        return

    def un(l):
        code, nom, loc, rtl = l
        try:
            return code, {"nom": nom, "loc": loc, "rtl": rtl, "relu": False,
                          "modele": MODELE, "date": time.strftime("%Y-%m-%d"),
                          "mots": traduire(code, nom)}
        except Exception as e:
            print(f"  {code}  ÉCHEC {e}", flush=True)
            return code, None

    with ThreadPoolExecutor(6) as pool:
        for code, rendu in pool.map(un, cibles):
            if rendu:
                # Une langue refaite perd sa relecture : ce n'est plus le texte relu.
                if code in tout and "interface" in tout[code]:
                    rendu["interface"] = tout[code]["interface"]
                tout[code] = rendu
    ordre = [l[0] for l in LANGUES]
    tout = {k: tout[k] for k in ordre if k in tout}
    SORTIE.write_text(json.dumps(tout, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(tout)}/11 langues → {SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
