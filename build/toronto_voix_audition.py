#!/usr/bin/env python3
"""L'audition des voix d'« Une semaine à Toronto » — deux phrases par voix.

Décision du 1er octobre 2026 : « Azure : voix du Canada pour les mots ; au
palier 3, les accents de Toronto, auditionnés au cadrage ». Le catalogue tranche
déjà une partie : le Canada n'a que DEUX voix, Clara et Liam, et pas en HD.
L'audition les met donc à côté des voix HD des États-Unis (l'accent général
d'Amérique du Nord est presque le même), des voix émotives MAI pour la
Torontoise qui revient, et de six accents qu'on entend à Toronto.

Deux phrases, choisies pour leurs risques : des prix et des heures (les erreurs
d'oreille qui coûtent : thirteen/thirty, quarter to) et un nom québécois ÉPELÉ
(le geste de l'hôtel). Chaque extrait est retranscrit par la reconnaissance
d'Azure (en-US) : un tirage HD qui déraille se voit à l'écart.

    python3 build/toronto_voix_audition.py      # ne repaie pas ce qui existe
"""
import html, json, pathlib, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from azure_voix import cle_region  # noqa: E402

DEST = RACINE / "assets" / "presentations" / "toronto" / "voix"

PHRASES = (
    "Hi there! Two adults for the ten-fifteen entry? That's thirteen fifty each, plus tax. "
    "And the last ferry leaves at quarter to eleven.",
    "Your last name is Tremblay? That's T, R, E, M, B, L, A, Y. Perfect, you're in room four-twelve.",
)
# (rôle, locale, voix Azure, nom, genre)
VOIX = [
    ("mots", "en-CA", "en-CA-ClaraNeural", "Clara", "F"),
    ("mots", "en-US", "en-US-Ava:DragonHDLatestNeural", "Ava", "F"),
    ("comptoir", "en-CA", "en-CA-LiamNeural", "Liam", "M"),
    ("comptoir", "en-US", "en-US-Andrew:DragonHDLatestNeural", "Andrew", "M"),
    ("torontoise", "en-US", "en-US-Harper:MAI-Voice-2.1", "Harper", "F"),
    ("torontoise", "en-US", "en-US-Olivia:MAI-Voice-2.1", "Olivia", "F"),
    ("accents", "en-IN", "en-IN-Aarti:DragonHDLatestNeural", "Aarti", "F"),
    ("accents", "en-IN", "en-IN-Arjun:DragonHDLatestNeural", "Arjun", "M"),
    ("accents", "en-PH", "en-PH-RosaNeural", "Rosa", "F"),
    ("accents", "en-HK", "en-HK-SamNeural", "Sam", "M"),
    ("accents", "en-NG", "en-NG-EzinneNeural", "Ezinne", "F"),
    ("accents", "en-GB", "en-GB-Ollie:DragonHDLatestNeural", "Ollie", "M"),
    ("accents", "en-IE", "en-IE-ConnorNeural", "Connor", "M"),
]


def dire(texte, langue, voix, dest):
    cle, region = cle_region()
    doc = ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
           f'xml:lang="{langue}"><voice name="{voix}">{html.escape(texte)}</voice></speak>')
    f = dest.with_suffix(".xml"); f.write_text(doc, encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST",
         "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-96kbitrate-mono-mp3",
         "-H", "User-Agent: francisation", "--data-binary", f"@{f}",
         "-o", str(dest), "-w", "%{http_code}",
         f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"],
        capture_output=True, text=True, check=True)
    f.unlink()
    if out.stdout.strip() != "200":
        dest.unlink(missing_ok=True)
        raise RuntimeError(f"{voix} : HTTP {out.stdout}")


def entendre(mp3):
    """Ce que la reconnaissance d'Azure entend : la vérification d'un tirage."""
    cle, region = cle_region()
    wav = mp3.with_suffix(".wav")
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(mp3), "-ar", "16000", "-ac", "1", str(wav)],
                   check=True)
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


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    releve = {}
    for role, langue, voix, nom, genre in VOIX:
        for i, texte in enumerate(PHRASES, 1):
            d = DEST / f"{nom.lower()}-{i}.mp3"
            if not d.exists():
                dire(texte, langue, voix, d)
            releve[d.name] = entendre(d)
            print(f"  {d.name:14} {releve[d.name]}")
    (DEST / "retranscription.json").write_text(json.dumps(releve, ensure_ascii=False, indent=1), encoding="utf-8")
