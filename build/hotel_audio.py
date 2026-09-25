#!/usr/bin/env python3
"""La voix de chaque mot de la réception, dans ses trois langues — et son contrôle.

    python3 build/hotel_audio.py              # ce qui manque, puis le contrôle
    python3 build/hotel_audio.py --compter    # extraits et caractères, sans rien payer
    python3 build/hotel_audio.py --controle   # retranscrire seulement
    python3 build/hotel_audio.py --refaire fr:plage en:plage   # ces extraits, de nouveau

Voix décidées le 25 septembre 2026 après audition : pour les MOTS, la voix
féminine de chaque langue — Sylvie (fr-CA), Emma (en-US), Dalia (es-MX), toutes
en HD. Les voix masculines (Thierry, Andrew, Jorge) iront aux clients.

UN DÉBIT : TAUX_SONS (-10 %), comme les mots de Francœur. Un mot qu'on imite
gagne à être posé ; c'est le client, au comptoir, qui parlera vite.

LA LANGUE : la HD choisit sa langue MOT À MOT (mémoire voix-hd-langue-et-hasard).
Un mot seul — « taxi », « minibar », « wifi » — existe dans les trois langues.
D'où <lang xml:lang> autour du texte, et surtout le CONTRÔLE : chaque MP3 est
retranscrit par la reconnaissance d'Azure DANS SA LANGUE et comparé au texte.
Ce qui s'écarte monte en tête de `build/contenu/entreprise-hotel/ecoute.json`.

Ce qui est entre parenthèses au lexique (« l'arrivée (l'enregistrement) ») est
une glose pour la page, pas une chose à dire : on ne le lit pas.

Sortie : assets/interactive/hotel/sons/<fr|en|es>/<id>.mp3
"""
import difflib, html, importlib.util, json, pathlib, re, subprocess, sys, tempfile, unicodedata
from concurrent.futures import ThreadPoolExecutor

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from azure_voix import cle_region, TAUX_SONS  # noqa: E402

_s = importlib.util.spec_from_file_location("hotel_lexique", RACINE / "build/contenu/entreprise-hotel/lexique.py")
LX = importlib.util.module_from_spec(_s); _s.loader.exec_module(LX)

SONS = RACINE / "assets" / "interactive" / "hotel" / "sons"
RELEVE = RACINE / "build" / "contenu" / "entreprise-hotel" / "ecoute.json"
LOCALE = {"fr": "fr-CA", "en": "en-US", "es": "es-MX"}
VOIX_MOTS = {"fr": "fr-CA-Sylvie:DragonHDLatestNeural",
             "en": "en-US-Emma:DragonHDLatestNeural",
             "es": "es-MX-Dalia:DragonHDLatestNeural"}
COL = {"fr": 2, "en": 3, "es": 4}
SEUIL_SIMILITUDE, SEUIL_CONFIANCE = 0.75, 0.60


def a_dire(texte):
    return re.sub(r"\s*\([^)]*\)", "", texte).strip()


def extraits():
    for e in LX.LEXIQUE:
        for l in ("fr", "en", "es"):
            yield l, e[0], a_dire(e[COL[l]])


def synth(langue, texte, dest, cle, region):
    loc = LOCALE[langue]
    doc = (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{loc}">'
           f'<voice name="{VOIX_MOTS[langue]}"><lang xml:lang="{loc}"><prosody rate="{TAUX_SONS}">'
           f'{html.escape(texte)}</prosody></lang></voice></speak>')
    dest.parent.mkdir(parents=True, exist_ok=True)
    f = dest.with_suffix(".xml"); f.write_text(doc, encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-96kbitrate-mono-mp3",
         "-H", "User-Agent: francisation", "--data-binary", f"@{f}", "-o", str(dest),
         "-w", "%{http_code}", f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"],
        capture_output=True, text=True, check=True)
    f.unlink()
    if out.stdout.strip() != "200":
        dest.unlink(missing_ok=True)
        raise RuntimeError(f"{langue}:{dest.stem} HTTP {out.stdout}")


def plat(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9 ]+", " ", t.replace("'", " ")).split()


def retranscrire(mp3, langue, cle, region):
    with tempfile.NamedTemporaryFile(suffix=".wav") as w:
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp3), "-ac", "1", "-ar", "16000",
                        "-sample_fmt", "s16", "-af", "adelay=500:all=1,apad=pad_dur=0.5", w.name], check=True)
        out = subprocess.run(
            ["curl", "-s", "-m", "60", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
             "-H", "Content-Type: audio/wav; codecs=audio/pcm; samplerate=16000",
             "--data-binary", f"@{w.name}",
             f"https://{region}.stt.speech.microsoft.com/speech/recognition/conversation/"
             f"cognitiveservices/v1?language={LOCALE[langue]}&format=detailed"],
            capture_output=True, text=True, check=True)
    d = json.loads(out.stdout or "{}")
    best = (d.get("NBest") or [{}])[0]
    return d.get("DisplayText", ""), float(best.get("Confidence", 0) or 0)


def controle(cle, region):
    def un(a):
        l, i, texte = a
        entendu, conf = retranscrire(SONS / l / f"{i}.mp3", l, cle, region)
        sim = difflib.SequenceMatcher(None, plat(texte), plat(entendu)).ratio()
        return {"langue": l, "id": i, "attendu": texte, "entendu": entendu,
                "similitude": round(sim, 2), "confiance": round(conf, 2),
                "douteux": sim < SEUIL_SIMILITUDE or conf < SEUIL_CONFIANCE}
    with ThreadPoolExecutor(6) as pool:
        rel = list(pool.map(un, extraits()))
    rel.sort(key=lambda r: (not r["douteux"], r["similitude"]))
    RELEVE.write_text(json.dumps(rel, ensure_ascii=False, indent=1), encoding="utf-8")
    d = [r for r in rel if r["douteux"]]
    print(f"contrôle : {len(rel)} extraits, {len(d)} douteux")
    for r in d:
        print(f"  {r['langue']}:{r['id']:16} attendu « {r['attendu']} » — entendu « {r['entendu']} » "
              f"({r['similitude']}, {r['confiance']})")


def retenter(cibles, cle, region, essais=3):
    """La HD n'est pas déterministe : un extrait suspect se retire jusqu'à trois
    fois, et on GARDE le tirage que la reconnaissance comprend le mieux."""
    import shutil
    txt = {(l, i): t for l, i, t in extraits()}
    for l, i in cibles:
        t, p = txt[(l, i)], SONS / l / f"{i}.mp3"
        def score(f):
            e, c = retranscrire(f, l, cle, region)
            return difflib.SequenceMatcher(None, plat(t), plat(e)).ratio() + c / 10, e
        best, be = score(p)
        for _ in range(essais):
            if best >= 1.05:
                break
            tmp = p.with_name(f"{i}.essai.mp3"); synth(l, t, tmp, cle, region)
            s_, e = score(tmp)
            if s_ > best:
                shutil.move(tmp, p); best, be = s_, e
            else:
                tmp.unlink()
        print(f"  {l}:{i:16} « {t} » → « {be} » {best:.2f}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "--retenter" in args:
        cle, region = cle_region()
        retenter([tuple(a.split(":")) for a in args if ":" in a], cle, region); sys.exit(0)
    tous = list(extraits())
    if "--compter" in args:
        print(f"{len(tous)} extraits, {sum(len(t) for _, _, t in tous)} caractères"); sys.exit(0)
    cle, region = cle_region()
    if "--controle" not in args:
        refaire = {a for a in args if ":" in a}
        if "--refaire" in args:
            for a in refaire:
                l, i = a.split(":"); (SONS / l / f"{i}.mp3").unlink(missing_ok=True)
        a_faire = [x for x in tous if not (SONS / x[0] / f"{x[1]}.mp3").exists()]
        with ThreadPoolExecutor(6) as pool:
            list(pool.map(lambda x: synth(x[0], x[2], SONS / x[0] / f"{x[1]}.mp3", cle, region), a_faire))
        print(f"{len(a_faire)} extraits produits")
    controle(cle, region)
