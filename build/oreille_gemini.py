#!/usr/bin/env python3
"""Faire écouter les extraits produits par un modèle, avant de les écouter soi.

    python3 build/oreille_gemini.py ~/Claude/generations/essai-gemini/*.mp3

Ce que ça vaut, et ce que ça ne vaut pas
----------------------------------------
Le banc `essai_gemini_tts.py` pose deux questions auxquelles la durée d'un MP3
ne répond pas : les lettres sortent-elles avec leur **nom français** (« a, èm,
i, èn, a ») ou anglais (« ay, em, ai, en, ay »), et l'accent est-il d'ici ?

L'API Gemini sait écouter de l'audio. On lui soumet donc chaque extrait. C'est
un **premier filtre, pas un verdict** : le modèle qui juge est de la même
famille que celui qui a parlé, et un modèle est mauvais juge de l'accent — il
lit surtout le texte qu'il reconnaît. Un « non » ici est un signal fort ; un
« oui » ne dispense pas de l'écoute humaine.

Le juge est un modèle *différent* du synthétiseur, ce qui vaut mieux que rien.
"""
import base64
import json
import pathlib
import subprocess
import sys

JUGE = "gemini-3.5-flash"
API = ("https://generativelanguage.googleapis.com/v1beta/models/"
       "%s:generateContent" % JUGE)

CONSIGNE = """Écoute cet extrait audio de synthèse vocale française. Réponds en trois lignes exactement, sans préambule :
TRANSCRIPTION: ce que tu entends, mot pour mot
LETTRES: si des lettres sont épelées, dis si elles portent leur nom FRANÇAIS (a, bé, cé, èm, èn, i) ou leur nom ANGLAIS (ay, bee, see, em, en, eye). Si aucune lettre n'est épelée, écris « sans objet ».
ACCENT: québécois, français de France, ou autre — et un mot sur ce qui te le fait dire"""


def cle():
    for l in (pathlib.Path.home() / "Claude" / ".env").read_text().splitlines():
        if l.startswith("GOOGLE_API_KEY="):
            return l.split("=", 1)[1].strip()


def juger(mp3, k):
    corps = {"contents": [{"parts": [
        {"text": CONSIGNE},
        {"inlineData": {"mimeType": "audio/mpeg",
                        "data": base64.b64encode(mp3.read_bytes()).decode()}},
    ]}]}
    req = mp3.with_suffix(".juge.json")
    req.write_text(json.dumps(corps))
    out = subprocess.run(
        ["curl", "-s", "-m", "180", "-X", "POST",
         "-H", "Content-Type: application/json", "--data-binary", "@%s" % req,
         "%s?key=%s" % (API, k)], capture_output=True, check=True)
    req.unlink()
    d = json.loads(out.stdout)
    if "error" in d:
        return "ERREUR %s %s" % (d["error"]["code"], d["error"]["message"][:120])
    return d["candidates"][0]["content"]["parts"][0]["text"].strip()


def main():
    k = cle()
    for arg in sys.argv[1:]:
        f = pathlib.Path(arg)
        print("\n=== %s" % f.name)
        print(juger(f, k))
    return 0


if __name__ == "__main__":
    sys.exit(main())
