#!/usr/bin/env python3
"""Les leçons narrées d'« Avant de partir » : un MP3 par séance.

    python3 build/compostelle_lecons.py            # ce qui manque
    python3 build/compostelle_lecons.py p1 p3      # refaire ces leçons
    python3 build/compostelle_lecons.py --compter  # caractères, sans rien payer

Le texte vient de build/contenu/compostelle/lecons.py. Chaque segment est
synthétisé seul — la guide en fr-CA (Sylvie HD), les exemples par la voix des
mots de l'application (Ximena HD, es-ES) — puis tout est assemblé par ffmpeg,
avec un court silence entre deux voix. Une voix HD qui lit du français ne sait
pas dire « jamón » : d'où les segments.

La HD déraille parfois sur un son très court (mémoire trousse-de-metier) :
un segment espagnol plus long que prévu est retiré, au meilleur de trois.

Sortie : assets/interactive/compostelle/sons/prep/<id>/lecon.mp3, et les temps
de début de chaque segment dans build/contenu/compostelle/lecons_temps.json —
la page s'en sert pour suivre le texte pendant l'écoute.
"""
import html, json, pathlib, subprocess, sys, tempfile

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from azure_voix import cle_region, rogner_silences  # noqa: E402
import compostelle_commun as C  # noqa: E402
from compostelle_audio import retranscrire, similitude  # noqa: E402

L = C.charger("lecons").LECONS
TEMPS = C.CONTENU / "lecons_temps.json"
VOIX = {"fr": ("fr-CA", "fr-CA-Sylvie:DragonHDLatestNeural", "-6%"),
        "es": ("es-ES", "es-ES-Ximena:DragonHDLatestNeural", "-12%")}
BLANC = {("fr", "fr"): 0.35, ("fr", "es"): 0.45, ("es", "fr"): 0.55, ("es", "es"): 0.4}


def ssml(lang, texte):
    loc, voix, taux = VOIX[lang]
    corps = f'<prosody rate="{taux}">{html.escape(texte)}</prosody>'
    corps = f'<lang xml:lang="{loc}">{corps}</lang>'
    return (f'<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
            f'xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="{loc}">'
            f'<voice name="{voix}">{corps}</voice></speak>')


def synth(lang, texte, dest, cle, region):
    f = dest.with_suffix(".xml"); f.write_text(ssml(lang, texte), encoding="utf-8")
    out = subprocess.run(
        ["curl", "-s", "-m", "120", "-X", "POST", "-H", f"Ocp-Apim-Subscription-Key: {cle}",
         "-H", "Content-Type: application/ssml+xml",
         "-H", "X-Microsoft-OutputFormat: audio-24khz-48kbitrate-mono-mp3",
         "-H", "User-Agent: francisation", "--data-binary", f"@{f}", "-o", str(dest),
         "-w", "%{http_code}", f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"],
        capture_output=True, text=True, check=True)
    f.unlink()
    if out.stdout.strip() != "200":
        raise RuntimeError(f"{dest.name} HTTP {out.stdout}")
    rogner_silences(dest)
    return duree(dest)


def duree(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout)


def attendue(texte):
    # Ximena à -12 % : ~13 caractères par seconde, plus une marge large.
    return 1.5 + len(texte) / 13 * 1.8


def lecon(sid, cle, region):
    segs = L[sid]
    dest = C.SONS / "prep" / sid / "lecon.mp3"
    dest.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        d = pathlib.Path(d)
        morceaux, debuts, t = [], [], 0.0
        for i, (lang, texte) in enumerate(segs):
            p = d / f"{i:02d}.mp3"
            dur = synth(lang, texte, p, cle, region)
            if lang == "es":
                # Contrôle : durée plausible ET retranscription fidèle (es-ES), au meilleur de trois.
                def note(dur):
                    sim = similitude(texte, retranscrire(p, cle, region))
                    return sim - (0.5 if dur > attendue(texte) else 0), sim
                sc, sim = note(dur); meilleur = (sc, sim, dur, p.read_bytes())
                for _ in range(2):
                    if meilleur[0] >= 0.8:
                        break
                    dur2 = synth(lang, texte, p, cle, region); sc2, sim2 = note(dur2)
                    if sc2 > meilleur[0]:
                        meilleur = (sc2, sim2, dur2, p.read_bytes())
                _, sim, dur, octets = meilleur; p.write_bytes(octets)
                if meilleur[0] < 0.8:
                    print(f"  ⚠ {sid} segment {i} douteux (similitude {sim:.2f}, {dur:.1f} s) : « {texte} »")
            if i:
                b = BLANC[(segs[i - 1][0], lang)]
                s = d / f"{i:02d}-blanc.mp3"
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i",
                                "anullsrc=r=24000:cl=mono", "-t", str(b), "-b:a", "48k", str(s)], check=True)
                morceaux.append(s); t += b
            debuts.append(round(t, 2))
            morceaux.append(p); t += dur
        liste = d / "liste.txt"
        liste.write_text("".join(f"file '{m}'\n" for m in morceaux))
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(liste),
                        "-ar", "24000", "-ac", "1", "-b:a", "64k", str(dest)], check=True)
    return debuts, duree(dest)


def main():
    args = sys.argv[1:]
    if "--compter" in args:
        n = {"fr": 0, "es": 0}
        for segs in L.values():
            for lang, t in segs:
                n[lang] += len(t)
        print(n, "caractères")
        return
    temps = json.loads(TEMPS.read_text()) if TEMPS.exists() else {}
    cle, region = cle_region()
    ids = [a for a in args if a in L] or [s for s in L if s not in temps or not (C.SONS / "prep" / s / "lecon.mp3").exists()]
    for sid in ids:
        debuts, total = lecon(sid, cle, region)
        temps[sid] = {"debuts": debuts, "duree": round(total, 1)}
        print(f"{sid} : {total:.0f} s, {len(debuts)} segments")
        TEMPS.write_text(json.dumps(temps, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
