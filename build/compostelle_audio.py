#!/usr/bin/env python3
"""Les voix d'« En route vers Compostelle » — synthèse Azure es-ES, et son contrôle.

    python3 build/compostelle_audio.py --compter     # extraits et caractères, sans rien payer
    python3 build/compostelle_audio.py --essai       # un extrait par voix, pour écouter
    python3 build/compostelle_audio.py               # ce qui manque, puis le contrôle
    python3 build/compostelle_audio.py --controle    # retranscrire seulement
    python3 build/compostelle_audio.py --retenter    # refait les douteux, garde le meilleur de trois
    python3 build/compostelle_audio.py --refaire mots/vaso.mp3 roncesvalles/scene-0-m.mp3

La liste des extraits vient de build/compostelle_commun.py, la même que lit la
page. Les voix et les débits, de build/contenu/compostelle/personnages.py.

TROIS FAMILLES DE VOIX, trois SSML :
- DragonHD (Ximena, Tristan) : détection de langue MOT À MOT — `<lang
  xml:lang="es-ES">` autour de tout le corps (mémoire voix-hd-langue-et-hasard).
  Et le tirage n'est pas déterministe : d'où le contrôle et `--retenter`.
- MAI-Voice-2 (Marta) : l'intention se déclare réplique par réplique, avec
  `<mstts:express-as style>` DANS la prosodie (mémoire voix-emotives-azure-mai).
- neurales (les gens du chemin) : déterministes, le SSML simple suffit.

LE TÉLÉPHONE : les répliques marquées `tel` (la pension de Burgos) passent par
un filtre de bande téléphonique — l'exercice est d'entendre sans voir.

LE CONTRÔLE : chaque MP3 est retranscrit par la reconnaissance d'Azure en
es-ES et comparé au texte ; ce qui s'écarte monte en tête de
build/contenu/compostelle/ecoute.json.
"""
import difflib, html, json, pathlib, re, subprocess, sys, tempfile, unicodedata
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from azure_voix import cle_region, rogner_silences  # noqa: E402
import compostelle_commun as C  # noqa: E402

PS = C.charger("personnages").PERSONNAGES
RELEVE = C.CONTENU / "ecoute.json"
SEUIL = 0.80


def ssml(x):
    _, _, _, _, voix, taux, _ = PS[x["perso"]]
    corps = html.escape(x["texte"])
    if x.get("emo") and "MAI-Voice" in voix:
        corps = f'<mstts:express-as style="{x["emo"]}">{corps}</mstts:express-as>'
    corps = f'<prosody rate="{taux}">{corps}</prosody>'
    if "DragonHD" in voix or "Multilingual" in voix:
        corps = f'<lang xml:lang="es-ES">{corps}</lang>'
    return ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="es-ES">'
            f'<voice name="{voix}">{corps}</voice></speak>')


def synth(x, cle, region, dest=None):
    dest = dest or (C.SONS / x["fichier"])
    dest.parent.mkdir(parents=True, exist_ok=True)
    f = dest.with_suffix(".xml"); f.write_text(ssml(x), encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3",
         "-H", "User-Agent: francisation", "--data-binary", f"@{f}", "-o", str(dest),
         "-w", "%{http_code}", f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"],
        capture_output=True, text=True, check=True)
    f.unlink()
    if out.stdout.strip() != "200":
        detail = dest.read_text(errors="replace")[:160] if dest.exists() else ""
        dest.unlink(missing_ok=True)
        raise RuntimeError(f"{x['fichier']} HTTP {out.stdout} {detail}")
    rogner_silences(dest)
    if x.get("tel"):
        tmp = dest.with_suffix(".tel.mp3")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(dest), "-af",
                        "highpass=f=320,lowpass=f=3300,acompressor=threshold=-18dB:ratio=3,volume=1.4",
                        "-b:a", "48k", str(tmp)], check=True)
        tmp.replace(dest)
    return dest


_U = ("cero uno dos tres cuatro cinco seis siete ocho nueve diez once doce trece catorce quince "
      "dieciseis diecisiete dieciocho diecinueve veinte veintiuno veintidos veintitres veinticuatro "
      "veinticinco veintiseis veintisiete veintiocho veintinueve").split()
_D = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
_C = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos",
      6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}


def en_lettres(n):
    """La reconnaissance écrit « a las 7 », le texte dit « a las siete » : on
    compare des mots. 0 à 999 suffit au chemin."""
    if n < 30:
        return _U[n]
    if n < 100:
        d, u = divmod(n, 10)
        return _D[d] + (" y " + _U[u] if u else "")
    if n == 100:
        return "cien"
    if n < 1000:
        c, r = divmod(n, 100)
        return _C[c] + (" " + en_lettres(r) if r else "")
    return str(n)


def plat(t):
    t = re.sub(r"(\d+)[,.](\d+)", lambda m: f"{m.group(1)} con {m.group(2)}", t)
    t = re.sub(r"\d+", lambda m: en_lettres(int(m.group())), t.replace("€", " euros "))
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t).split()


def retranscrire(mp3, cle, region):
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp3), "-ac", "1", "-ar", "16000",
                        "-sample_fmt", "s16", "-af", "adelay=900:all=1,apad=pad_dur=1.0", w.name], check=True)
        out = subprocess.run(
            ["curl", "-s", "-m", "60", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
             "-H", "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000",
             "--data-binary", f"@{w.name}",
             f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/"
             "cognitiveservices/v1?language=es-ES&format=detailed"],
            capture_output=True, text=True, check=True)
    d = json.loads(out.stdout or "{}")
    return d.get("DisplayText", "")


def similitude(texte, entendu):
    return round(difflib.SequenceMatcher(None, plat(texte), plat(entendu)).ratio(), 2)


def controle(xs, cle, region):
    def un(x):
        entendu = retranscrire(C.SONS / x["fichier"], cle, region)
        s = similitude(x["texte"], entendu)
        return {"fichier": x["fichier"], "perso": x["perso"], "attendu": x["texte"],
                "entendu": entendu, "similitude": s, "douteux": s < SEUIL}
    with ThreadPoolExecutor(6) as pool:
        rel = list(pool.map(un, xs))
    # Un contrôle partiel (--refaire) FUSIONNE dans le relevé : il l'écrasait,
    # et le relevé des 519 extraits tombait à un seul (vu le 25 sept.).
    if RELEVE.exists() and len(xs) < len(list(C.extraits())):
        vus = {r["fichier"] for r in rel}
        rel += [r for r in json.loads(RELEVE.read_text(encoding="utf-8")) if r["fichier"] not in vus]
    rel.sort(key=lambda r: (not r["douteux"], r["similitude"]))
    RELEVE.write_text(json.dumps(rel, ensure_ascii=False, indent=1), encoding="utf-8")
    d = [r for r in rel if r["douteux"]]
    print(f"contrôle : {len(rel)} extraits, {len(d)} douteux")
    for r in d[:40]:
        print(f"  {r['fichier']:34} {r['similitude']:.2f}  « {r['attendu']} » → « {r['entendu']} »")
    return d


def retenter(cle, region, douteux, par_fichier):
    """Trois tirages de plus pour chaque douteux ; on garde le plus fidèle."""
    for r in douteux:
        x = par_fichier[r["fichier"]]
        meilleur, score = C.SONS / x["fichier"], r["similitude"]
        for n in range(3):
            essai = C.SONS / (x["fichier"][:-4] + f".essai{n}.mp3")
            try:
                synth(x, cle, region, essai)
            except RuntimeError as e:
                print("  ", e); continue
            s = similitude(x["texte"], retranscrire(essai, cle, region))
            if s > score:
                essai.replace(C.SONS / x["fichier"]); score = s
            else:
                essai.unlink(missing_ok=True)
            if score >= 0.95:
                break
        print(f"  {x['fichier']:34} {r['similitude']:.2f} → {score:.2f}")


TEXTES = C.SONS / "textes.json"


def signature(x):
    """Ce qui, s'il change, rend le son périmé : le texte, la voix, le débit, l'intention."""
    _, _, _, _, voix, taux, _ = PS[x["perso"]]
    return f"{voix}|{taux}|{x.get('emo') or ''}|{int(bool(x.get('tel')))}|{x['texte']}"


def lire_textes():
    try:
        return json.loads(TEXTES.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def ecrire_textes(xs):
    t = lire_textes()
    for x in xs:
        if (C.SONS / x["fichier"]).exists():
            t[x["fichier"]] = signature(x)
    TEXTES.write_text(json.dumps(t, ensure_ascii=False, indent=0, sort_keys=True), encoding="utf-8")


def perimes(xs):
    """Les sons absents, ET ceux dont le texte a changé depuis leur synthèse.
    Sans ce relevé, une réplique corrigée gardait son ancien son en silence :
    le générateur ne produisait que ce qui manquait sur le disque."""
    t = lire_textes()
    return [x for x in xs if not (C.SONS / x["fichier"]).exists() or t.get(x["fichier"]) not in (None, signature(x))]


def main():
    args = sys.argv[1:]
    xs = list(C.extraits())
    par_fichier = {x["fichier"]: x for x in xs}
    if "--amorcer" in args:
        # Une fois : noter la signature des sons déjà produits, avant de toucher au texte.
        ecrire_textes(xs); print(f"{len(lire_textes())} signatures notées"); return
    if "--compter" in args:
        manque = perimes(xs)
        print(f"{len(xs)} extraits, {len(manque)} à produire (absents ou texte changé), "
              f"{sum(len(x['texte']) for x in manque)} caractères")
        return
    cle, region = cle_region()
    if "--essai" in args:
        vus = {}
        for x in xs:
            vus.setdefault(x["perso"], x)
        for p, x in vus.items():
            dest = synth(x, cle, region, RACINE / "essais" / "compostelle-voix" / f"{p}.mp3")
            print(f"  {p:10} {dest.relative_to(RACINE)}  « {x['texte']} »")
        return
    if "--refaire" in args:
        cibles = [par_fichier[f] for f in args if f in par_fichier]
        for x in cibles:
            synth(x, cle, region); print("  refait", x["fichier"])
        ecrire_textes(cibles)
        controle(cibles, cle, region)
        return
    if "--controle" not in args and "--retenter" not in args:
        manque = perimes(xs)
        print(f"{len(manque)} extraits à produire (absents ou texte changé)")
        echecs = []
        def un(x):
            try:
                synth(x, cle, region)
            except Exception as e:
                echecs.append(x["fichier"]); print("  ", e)
        with ThreadPoolExecutor(6) as pool:
            list(pool.map(un, manque))
        print(f"produits : {len(manque) - len(echecs)}, échecs : {echecs}")
        ecrire_textes([x for x in manque if x["fichier"] not in echecs])
    douteux = controle(xs, cle, region)
    if "--retenter" in args and douteux:
        retenter(cle, region, douteux, par_fichier)
        controle(xs, cle, region)


if __name__ == "__main__":
    main()
