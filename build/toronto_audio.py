#!/usr/bin/env python3
"""Les voix d'« Une semaine à Toronto » — Azure, contrôlées par retranscription.

    python3 build/toronto_audio.py --compter     # combien, combien ça coûte, sans rien payer
    python3 build/toronto_audio.py               # produit ce qui manque sur le disque
    python3 build/toronto_audio.py --retenter    # refait les extraits douteux (garde le meilleur de trois)

La liste vient de build/toronto_commun.py, la même que celle de l'application.
Les voix, de build/contenu/toronto/personnages.py (cadrage du 1er oct. 2026).

Chaque extrait est retranscrit par la reconnaissance d'Azure (en-US) et comparé
au texte voulu : la HD choisit sa langue mot à mot et n'est pas déterministe
(mémoire voix-hd-langue-et-hasard). En anglais, la confiance de la
reconnaissance est basse par nature : on trie sur la SIMILITUDE, pas sur la
confiance (leçon de l'hôtel). Encodé à 48 kbit/s : à 96, la poche de
Compostelle pesait 27 Mo.

Gel des MP3 (mémoire gel-des-mp3) : ne se lance qu'avec le feu vert de Daniel.
"""
import difflib, html, json, pathlib, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
import toronto_commun as C  # noqa: E402
from azure_voix import cle_region  # noqa: E402

RELEVE = C.SONS / "releve.json"
# Le texte DIT peut différer du texte affiché (comme PRONONCIATION chez Francœur). Essais du 1er oct. 2026 :
# Clara avale « And you? » en « Nu » (3 tirages identiques : voix neurale) ; une virgule le rend net.
PRONONCIATION = {
    "And you? How about you?": "And, you? How about you?",
    "And you? Where are you from?": "And, you? Where are you from?",
}
SEUIL = 0.80
TARIF = {"neural": 16, "hd": 30}   # $ US par million de caractères (≈, grille Azure)


def voix_de(cle):
    PS = C.charger("personnages")
    nom, voix, locale, *_ = PS.VOIX[cle]
    return voix, locale


def ssml(texte, voix, locale):
    return ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xml:lang="{locale}"><voice name="{voix}">{html.escape(texte)}</voice></speak>')


def dire(texte, cle_voix, dest):
    cle, region = cle_region()
    voix, locale = voix_de(cle_voix)
    dest.parent.mkdir(parents=True, exist_ok=True)
    brut = dest.with_suffix(".brut.mp3")
    f = dest.with_suffix(".xml"); f.write_text(ssml(texte, voix, locale), encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml", "-H", "X-Microsoft-OutputFormat: audio-24khz-96kbitrate-mono-mp3",
         "-H", "User-Agent: francisation", "--data-binary", f"@{f}", "-o", str(brut), "-w", "%{http_code}",
         f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"], capture_output=True, text=True, check=True)
    f.unlink()
    if out.stdout.strip() != "200":
        brut.unlink(missing_ok=True)
        raise RuntimeError(f"{dest.name} : HTTP {out.stdout}")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(brut), "-b:a", "48k", "-ac", "1", str(dest)], check=True)
    brut.unlink()


def entendre(mp3):
    cle, region = cle_region()
    wav = mp3.with_suffix(".wav")
    # ~0,5 s de silence autour : sans lui, un mot seul revient vide (leçon de Francœur).
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp3), "-af", "adelay=500,apad=pad_dur=0.5",
                    "-ar", "16000", "-ac", "1", str(wav)], check=True)
    out = subprocess.run(
        ["curl", "-s", "-m", "60", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000", "--data-binary", f"@{wav}",
         f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1"
         "?language=en-US&format=simple"], capture_output=True, text=True)
    wav.unlink()
    try:
        return json.loads(out.stdout).get("DisplayText", "")
    except ValueError:
        return ""


NOMBRES = set("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen "
              "seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred quarter past "
              "half to o clock am pm a m p m".split())


def _net(t):
    """Sans les nombres : la reconnaissance écrit « 1350 » pour « thirteen fifty », « 10:15 » pour
    « quarter past ten » ; comparer ces écritures ne dit rien de la voix (relevé du 1er oct. 2026).
    Les nombres se vérifient à l'oreille. « I'm » et « I am » se valent."""
    t = t.lower().replace("i'm", "i am").replace("’", "'")
    t = re.sub(r"[^a-z ]", " ", t.replace("'", ""))
    return [w for w in t.split() if w not in NOMBRES]


def similitude(voulu, entendu):
    v, e = _net(voulu), _net(entendu)
    if not v:   # que des nombres : rien à comparer en mots ; il faut au moins avoir entendu quelque chose
        return 1.0 if entendu.strip() else 0.0
    return difflib.SequenceMatcher(None, v, e).ratio()


def un(x, releve, forcer=False):
    dest = C.SONS / x["fichier"]
    # Un fichier présent dont la phrase a changé (une correction d'audit) se refait : même nom, autre texte.
    vieux = releve.get(x["fichier"], {}).get("voulu")
    if dest.exists() and not forcer and (vieux is None or vieux == x["texte"]):
        return
    dire(PRONONCIATION.get(x["texte"], x["texte"]), x["voix"], dest)
    e = entendre(dest)
    releve[x["fichier"]] = {"voulu": x["texte"], "entendu": e, "sim": round(similitude(x["texte"], e), 2), "voix": x["voix"]}


if __name__ == "__main__":
    args = sys.argv[1:]
    tous = C.extraits()
    if "--compter" in args:
        PS = C.charger("personnages")
        car = {"neural": 0, "hd": 0}
        for x in tous:
            car["hd" if ("HD" in PS.VOIX[x["voix"]][1] or "MAI" in PS.VOIX[x["voix"]][1]) else "neural"] += len(x["texte"])
        cout = sum(car[k] * TARIF[k] / 1e6 for k in car)
        faits = sum(1 for x in tous if (C.SONS / x["fichier"]).exists())
        print(f"{len(tous)} extraits ({faits} déjà faits), {sum(car.values())} caractères "
              f"(neural {car['neural']}, HD/MAI {car['hd']}) ≈ {cout:.2f} $ US, plus la retranscription (≈ 0,05 $)")
        sys.exit(0)
    releve = json.loads(RELEVE.read_text()) if RELEVE.exists() else {}
    if "--recalculer" in args:   # la comparaison a changé : on la refait sur les retranscriptions gardées, sans rien payer
        for k, v in releve.items():
            v["sim"] = round(similitude(v["voulu"], v["entendu"]), 2)
        args.append("--rien")
    if "--retenter" in args:
        douteux = [x for x in tous if releve.get(x["fichier"], {}).get("sim", 1) < SEUIL]
        for x in douteux:
            meilleur = releve[x["fichier"]]
            garde = (C.SONS / x["fichier"]).read_bytes()
            for _ in range(2):
                un(x, releve, forcer=True)
                if releve[x["fichier"]]["sim"] > meilleur["sim"]:
                    meilleur, garde = releve[x["fichier"]], (C.SONS / x["fichier"]).read_bytes()
            (C.SONS / x["fichier"]).write_bytes(garde); releve[x["fichier"]] = meilleur
            print(f"  {x['fichier']:28} {meilleur['sim']:.2f}  « {meilleur['entendu']} »")
    elif "--rien" not in args:
        with ThreadPoolExecutor(4) as ex:
            list(ex.map(lambda x: un(x, releve), tous))
    RELEVE.write_text(json.dumps(releve, ensure_ascii=False, indent=1), encoding="utf-8")
    bas = sorted((v["sim"], k) for k, v in releve.items() if v["sim"] < SEUIL)
    print(f"{len(releve)} relevés, {len(bas)} sous {SEUIL} :")
    for s, k in bas:
        print(f"  {s:.2f}  {k}  voulu « {releve[k]['voulu']} » — entendu « {releve[k]['entendu']} »")
