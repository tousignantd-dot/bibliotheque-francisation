#!/usr/bin/env python3
"""Gemini TTS contre ElevenLabs, sur la mini-leçon qui fait le plus mal.

    python3 build/essai_gemini_tts.py

Pourquoi ce banc d'essai
------------------------
ElevenLabs **devine** : la langue d'un mot nu — d'où `voix.py` et son
`previous_text` — et le débit, qu'on ne corrige donc qu'après coup à l'`atempo`,
avec un facteur mesuré voix par voix et palier par palier. Deux rattrapages,
aucun reproductible.

Trois relèves étaient possibles. **Azure** est la plus propre sur le papier
(le SSML *dit* au lieu de deviner : `<prosody rate>`, `<say-as>`), mais il
faut une clé qu'on n'a pas, et il n'offre que quatre voix fr-CA — trop peu
pour les dialogues à personnages. **Google Cloud TTS** est fermé : il refuse
les clés API et exige un compte de service. Reste **l'API Gemini**, qui
accepte la clé AI Studio déjà dans `.env` et donne une trentaine de voix.

Le prix se compte en jetons audio et non en caractères : ~32 jetons par
seconde de parole, mesurés sur le premier appel.

Ce qui reste à prouver
----------------------
Gemini n'a **pas de SSML**. Tout passe par une consigne en langue naturelle
posée devant le texte — « lis lentement, en marquant une pause entre chaque
lettre ». C'est plus souple qu'Azure et moins sûr : rien ne garantit que la
consigne soit suivie, ni qu'elle le soit deux fois pareil. Ce banc mesure donc
les caractères par seconde obtenus, précisément pour voir si « lent » veut
dire quelque chose de stable.

Et l'accent : les voix Gemini ne sont pas marquées par locale. Le québécois se
demande dans la consigne. C'est le point que seule l'oreille tranche, et c'est
le premier à écouter.

Le cobaye est `prAlpha` (« Épeler son nom », module-n1-presenter) : la
mini-leçon qui cumule les lettres nues et le besoin de lenteur.

Quatre blocs dans `~/Claude/generations/essai-gemini`, plus `comparer.html` :

1. **épellation** — trois noms, avec la consigne d'épeler et sans.
2. **ralenti** — la même phrase à trois degrés de lenteur, c/s mesurés.
3. **voix** — six voix sur le même extrait, toutes avec la consigne
   québécoise. C'est l'avantage décisif sur Azure s'il tient à l'oreille.
4. **mots nus** — les 12 de `voix.MOTS_DIFFICILES`, sans contexte.
"""
import base64
import html
import json
import os
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from voix import MOTS_DIFFICILES                      # noqa: E402

SORTIE = pathlib.Path.home() / "Claude" / "generations" / "essai-gemini"
MODELE = "gemini-3.1-flash-tts-preview"
API = ("https://generativelanguage.googleapis.com/v1beta/models/"
       "%s:generateContent" % MODELE)

# Les voix sont neutres quant à la langue : le nom ne dit rien de l'accent, il
# donne un timbre. Six suffisent pour juger si la palette peut porter les
# personnages des dialogues — c'est là qu'Azure, avec ses quatre voix fr-CA,
# ne suit pas.
VOIX = ["Kore", "Aoede", "Leda", "Charon", "Puck", "Orus"]

# La consigne d'accent, posée devant chaque extrait. Elle n'est pas prononcée.
QC = "Lis en français québécois, d'une voix d'enseignante calme et posée"

PALIERS = [
    ("normal",    "%s, à un débit normal" % QC),
    ("lent",      "%s, lentement, en articulant bien" % QC),
    ("tres-lent", "%s, très lentement, en détachant chaque syllabe" % QC),
]

PHRASE = ("Au centre, à la clinique, à la banque. "
          "On vous demandera d'épeler votre nom, lettre par lettre.")


def cle():
    env = pathlib.Path.home() / "Claude" / ".env"
    k = os.environ.get("GOOGLE_API_KEY")
    if not k and env.exists():
        for l in env.read_text().splitlines():
            if l.startswith("GOOGLE_API_KEY="):
                k = l.split("=", 1)[1].strip()
    return k


def synthese(consigne, texte, voix, k, dest):
    """Un appel, un MP3. Renvoie (durée, jetons audio)."""
    corps = {
        "contents": [{"parts": [{"text": "%s : %s" % (consigne, texte)}]}],
        "generationConfig": {
            "responseModalities": ["AUDIO"],
            "speechConfig": {"voiceConfig": {
                "prebuiltVoiceConfig": {"voiceName": voix}}},
        },
    }
    req = urllib.request.Request(
        "%s?key=%s" % (API, k), data=json.dumps(corps).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    part = d["candidates"][0]["content"]["parts"][0]["inlineData"]
    pcm = base64.b64decode(part["data"])
    # L16 24 kHz mono : ffmpeg a besoin qu'on le lui dise, il n'y a pas d'en-tête.
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "s16le", "-ar", "24000",
         "-ac", "1", "-i", "pipe:0", "-b:a", "160k", str(dest)],
        input=pcm, check=True, capture_output=True)
    jetons = d["usageMetadata"]["candidatesTokenCount"]
    return len(pcm) / 2 / 24000, jetons


def plan():
    """(bloc, nom, consigne, texte, voix, texte affiché)."""
    p = []
    epeler = ("%s, en épelant lettre par lettre, avec une pause nette entre "
              "chaque lettre, puis dis le nom en entier" % QC)
    for mot in ("Amina", "Tremblay", "Benali"):
        lettres = "%s. %s." % (", ".join(mot.upper()), mot.capitalize())
        p.append(("epellation", "%s-consigne" % mot.lower(), epeler,
                  "%s. %s." % (mot.capitalize(), mot.capitalize()),
                  "Kore", "consigne « épelle » sur le nom seul"))
        p.append(("epellation", "%s-brut" % mot.lower(), PALIERS[1][1],
                  lettres, "Kore", lettres))
    for nom, consigne in PALIERS:
        p.append(("ralenti", "phrase-%s" % nom, consigne, PHRASE, "Kore",
                  "%s  [%s]" % (PHRASE, nom)))
    for v in VOIX:
        p.append(("voix", "phrase-%s" % v.lower(), PALIERS[1][1], PHRASE, v,
                  "%s  [%s]" % (PHRASE, v)))
    for mot in MOTS_DIFFICILES:
        p.append(("mots-nus", mot, "%s, dis ce seul mot" % QC, mot, "Kore", mot))
    return p


def page(res):
    blocs = {}
    for r in res:
        blocs.setdefault(r["bloc"], []).append(r)
    out = ["<meta charset='utf-8'><title>Essai Gemini TTS fr-CA</title>",
           "<style>body{font:16px/1.5 system-ui;max-width:54rem;margin:2rem "
           "auto;padding:0 1rem}h2{margin-top:2.5rem;border-bottom:1px solid "
           "#ddd;padding-bottom:.3rem}td{padding:.35rem .8rem .35rem 0;"
           "vertical-align:middle}td.t{color:#444}td.d{color:#888;"
           "font-variant-numeric:tabular-nums;white-space:nowrap}"
           "audio{height:2rem}</style>",
           "<h1>Gemini TTS — français québécois</h1>",
           "<p>Mini-leçon <b>prAlpha « Épeler son nom »</b>. "
           "Écouter d'abord le bloc <b>voix</b> : l'accent est-il d'ici ? "
           "Puis <b>épellation</b> : les lettres sortent-elles en français ?</p>"]
    for nom in ("voix", "epellation", "ralenti", "mots-nus"):
        for r in blocs.get(nom, []):
            pass
        if nom not in blocs:
            continue
        out.append("<h2>%s</h2><table>" % nom)
        for r in blocs[nom]:
            cs = len(r["texte"]) / r["duree"] if r["duree"] else 0
            out.append("<tr><td><audio controls src='%s'></audio></td>"
                       "<td class='t'>%s</td>"
                       "<td class='d'>%.1f s · %.1f c/s</td></tr>"
                       % (r["fichier"], html.escape(r["affiche"]), r["duree"], cs))
        out.append("</table>")
    return "\n".join(out)


def main():
    k = cle()
    if not k:
        print("GOOGLE_API_KEY absente de ~/Claude/.env")
        return 1
    SORTIE.mkdir(parents=True, exist_ok=True)
    travaux, res, jetons = plan(), [], 0
    print("%d extraits, modèle %s" % (len(travaux), MODELE))
    for bloc, nom, consigne, texte, voix, affiche in travaux:
        f = SORTIE / ("%s--%s.mp3" % (bloc, nom))
        try:
            d, j = synthese(consigne, texte, voix, k, f)
        except urllib.error.HTTPError as e:
            print("  %-24s HTTP %s %s" % (nom, e.code, e.read().decode()[:160]))
            continue
        jetons += j
        res.append({"bloc": bloc, "nom": nom, "texte": texte, "affiche": affiche,
                    "fichier": f.name, "duree": d})
        print("  %-24s %5.2f s  %4d jetons" % (nom, d, j))
    (SORTIE / "comparer.html").write_text(page(res))
    secs = sum(r["duree"] for r in res)
    print("\n%d fichiers · %.0f s d'audio · %d jetons audio" % (len(res), secs, jetons))
    if secs:
        print("→ %.1f jetons/seconde de parole" % (jetons / secs))
    print("Ouvrir %s/comparer.html" % SORTIE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
