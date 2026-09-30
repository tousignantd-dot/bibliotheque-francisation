#!/usr/bin/env python3
"""L'audioguide de Montréal — le texte de chaque lieu, lu dans les trois langues.

    python3 build/montreal_audio.py --essai   # combien de sons, de caractères
    python3 build/montreal_audio.py           # ce qui manque, ou dont le texte a changé
    python3 build/montreal_audio.py fr/schwartz.mp3

Une voix par langue, toutes trois Azure HD : Sylvie (fr-CA, la ville parle
québécois), Emma (anglais), Dalia (es-MX : la plupart des visiteurs
hispanophones viennent d'Amérique latine). Les exemples des « mots d'ici »
sont dits par Sylvie. `textes.json` garde le texte de chaque son : un son
dont le texte a changé se refait seul au prochain passage.
"""
import html, json, subprocess, sys, threading
from concurrent.futures import ThreadPoolExecutor
import montreal_commun as M
from azure_voix import cle_region

VOIX = {"fr": ("fr-CA", "fr-CA-Sylvie:DragonHDLatestNeural", "-3%"),
        "en": ("en-US", "en-US-Emma:DragonHDLatestNeural", "-3%"),
        "es": ("es-MX", "es-MX-Dalia:DragonHDLatestNeural", "-3%")}
# Les personnages des scènes « Parler » : quatre voix québécoises, un peu
# ralenties — l'auditeur est un touriste qui apprend.
VOIX_SCENE = {"sylvie": "fr-CA-Sylvie:DragonHDLatestNeural", "thierry": "fr-CA-Thierry:DragonHDLatestNeural",
              "jean": "fr-CA-JeanNeural", "antoine": "fr-CA-AntoineNeural"}
TAUX_SCENE = "-8%"
# Filou, la mascotte du mode famille : une voix d'homme par langue, jouée plus
# haut et un peu plus vite — Azure n'a pas de voix d'enfant au Québec.
VOIX_FILOU = {"fr": ("fr-CA", "fr-CA-Thierry:DragonHDLatestNeural"),
              "en": ("en-US", "en-US-Andrew:DragonHDLatestNeural"),
              "es": ("es-MX", "es-MX-Jorge:DragonHDLatestNeural")}
PROSODIE_FILOU = 'rate="+4%" pitch="+9%"'
AUDIO = M.MEDIA / "audio"
TEXTES = AUDIO / "textes.json"


def ssml(lang, texte, perso=None):
    loc, voix, taux = VOIX[lang]
    prosodie = f'rate="{taux}"'
    if perso == "filou":
        loc, voix = VOIX_FILOU[lang]; prosodie = PROSODIE_FILOU
    elif perso:
        voix, prosodie = VOIX_SCENE[perso], f'rate="{TAUX_SCENE}"'
    paras = [p.strip() for p in texte.split("\n\n") if p.strip()]
    corps = '<break time="600ms"/>'.join(html.escape(p) for p in paras)
    return (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="{loc}">'
            f'<voice name="{voix}"><lang xml:lang="{loc}"><prosody {prosodie}>{corps}'
            f'</prosody></lang></voice></speak>')


def synth(rel, lang, texte, perso, cle, region):
    dest = AUDIO / rel; dest.parent.mkdir(parents=True, exist_ok=True)
    f = dest.with_suffix(".xml"); f.write_text(ssml(lang, texte, perso), encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "180", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3",
         "-H", "User-Agent: montreal-en-poche", "--data-binary", f"@{f}", "-o", str(dest),
         "-w", "%{http_code}", f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"],
        capture_output=True, text=True)
    f.unlink()
    if out.stdout.strip() != "200":
        dest.unlink(missing_ok=True)
        raise RuntimeError(f"{rel} HTTP {out.stdout}")
    # Pas de rogner_silences() : une narration d'une minute n'y gagne rien, et
    # chaque passage réencode le fichier. (Un son mesuré PENDANT son écriture
    # paraît tronqué — 22 s pour Jean-Talon le 29 sept. — sans l'être.)


if __name__ == "__main__":
    args = sys.argv[1:]
    faits = json.loads(TEXTES.read_text()) if TEXTES.exists() else {}
    tous = [e if len(e) == 4 else (*e, None) for e in M.extraits()]
    noms = [a for a in args if not a.startswith("--")]
    cibles = ([e for e in tous if e[0] in noms] if noms else
              [e for e in tous if not (AUDIO / e[0]).exists() or faits.get(e[0]) != e[2]])
    if "--essai" in args:
        print(f"{len(cibles)} sons, {sum(len(e[2]) for e in cibles)} caractères"); sys.exit(0)
    cle, region = cle_region()
    echecs, verrou = [], threading.Lock()
    def un(e):
        try:
            synth(*e, cle, region)   # e = (rel, langue, texte, perso)
            with verrou:   # écrit à chaque son : un arrêt en cours de route ne fait rien repayer
                faits[e[0]] = e[2]
                TEXTES.write_text(json.dumps(faits, ensure_ascii=False, indent=1), encoding="utf-8")
            print("  ", e[0], flush=True)
        except Exception as x:
            echecs.append(e[0]); print("  ÉCHEC", x, flush=True)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(un, cibles))
    TEXTES.write_text(json.dumps(faits, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(cibles) - len(echecs)} faits, échecs : {echecs}")
