#!/usr/bin/env python3
"""Relève à quel instant chaque mot est prononcé, dans chaque narration.

C'est la pièce qui met la voix et l'image d'accord. Sans elle, un plan n'est
calé qu'à son début : la voix dit « ici une production orale » pendant que le
pointeur est encore en route, et l'écart grandit jusqu'à la fin du plan.
Avec ces repères, le tournage déclenche un geste sur un mot précis.

On passe par l'**alignement forcé** d'ElevenLabs, qui lit le MP3 déjà produit
et rend la position de chaque mot. La synthèse « with-timestamps » ferait la
même chose, mais en refabriquant l'audio : on repaierait toutes les
narrations et le son des capsules changerait sans raison.

Relançable : un plan déjà aligné dont le texte n'a pas bougé n'est pas
retraité. Écrire `voix/<plan>.json` est le seul effet.
"""
import json
import os
import sys
import urllib.request
import uuid
from pathlib import Path

ICI = Path(__file__).parent
VOIX = ICI / "voix"


def cle():
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"]
    env = ICI.parent.parent / ".env"
    for ligne in env.read_text().splitlines():
        if ligne.startswith("ELEVENLABS_API_KEY="):
            return ligne.split("=", 1)[1].strip().strip('"').strip("'")
    sys.exit("ELEVENLABS_API_KEY introuvable")


def aligner(api, mp3, texte):
    limite = "----" + uuid.uuid4().hex
    corps = b"".join([
        f'--{limite}\r\nContent-Disposition: form-data; name="text"\r\n\r\n{texte}\r\n'.encode(),
        f'--{limite}\r\nContent-Disposition: form-data; name="file"; '
        f'filename="{mp3.name}"\r\nContent-Type: audio/mpeg\r\n\r\n'.encode(),
        mp3.read_bytes(),
        f"\r\n--{limite}--\r\n".encode(),
    ])
    req = urllib.request.Request("https://api.elevenlabs.io/v1/forced-alignment",
                                 data=corps, method="POST")
    req.add_header("Content-Type", f"multipart/form-data; boundary={limite}")
    req.add_header("xi-api-key", api)
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read().decode())


def main():
    api = cle()
    manifeste = json.loads((ICI / "manifeste.json").read_text())
    faits = refaits = 0
    for capsule in manifeste["capsules"]:
        for plan in capsule["plans"]:
            base = f"{capsule['id']}_{plan['id']}"
            mp3 = VOIX / f"{base}.mp3"
            reperes = VOIX / f"{base}.json"
            if not mp3.exists():
                sys.exit(f"narration absente : {base}.mp3 — lancez narrer.py d'abord")
            faits += 1
            # Le texte est gardé dans le relevé : un plan réécrit doit être
            # réaligné, sinon on cale des gestes sur d'anciens mots.
            if reperes.exists():
                try:
                    if json.loads(reperes.read_text()).get("texte") == plan["texte"]:
                        continue
                except (ValueError, OSError):
                    pass
            r = aligner(api, mp3, plan["texte"])
            mots = [{"mot": m["text"], "debut": m["start"], "fin": m["end"]}
                    for m in r.get("words", [])]
            reperes.write_text(json.dumps(
                {"texte": plan["texte"], "mots": mots,
                 "perte": r.get("loss")}, ensure_ascii=False))
            refaits += 1
            print(f"  {base}  {len(mots)} mots")
    print(f"{faits} plans, {refaits} alignés cette fois")


if __name__ == "__main__":
    main()
