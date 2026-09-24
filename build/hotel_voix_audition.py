#!/usr/bin/env python3
"""L'audition des voix de la réception — Azure HD, deux phrases par voix.

Décision du 24 septembre 2026 : « Azure HD, deux voix par langue, auditionnées
au cadrage ». Le catalogue HD tranche déjà la moitié : le Mexique n'a que
Dalia et Jorge, le Québec que Sylvie et Thierry. Seul l'anglais offre un vrai
choix : quatre candidates, deux à retenir.

Deux phrases, choisies pour leurs risques : l'accueil (un numéro de chambre et
des heures, là où l'erreur coûte) et un nom ÉPELÉ — le geste le plus fréquent
du comptoir, et le point faible connu d'Azure (les lettres nues sortent à
l'anglaise en français : mémoire `epellation-azure-anglaise`).

    python3 build/hotel_voix_audition.py      # ne repaie pas ce qui existe
"""
import html, pathlib, subprocess, sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "build"))
from azure_voix import cle_region  # noqa: E402

DEST = RACINE / "assets" / "presentations" / "hotel-voix"

PHRASES = {
    "fr-CA": ("Bonjour, bienvenue! Vous êtes à la chambre 412, au quatrième étage. "
              "Le déjeuner est servi de 7 h à 10 h.",
              "Votre nom de famille, c'est bien Moreno? M, O, R, E, N, O."),
    "en-US": ("Good afternoon, and welcome! You're in room four-twelve, on the fourth floor. "
              "Breakfast is served from seven to ten.",
              "Your last name is Moreno? That's M, O, R, E, N, O."),
    "es-MX": ("¡Buenas tardes, bienvenido! Su habitación es la cuatrocientos doce, en el cuarto piso. "
              "El desayuno se sirve de siete a diez.",
              "¿Su apellido es Moreno? Eme, o, erre, e, ene, o."),
}
VOIX = [
    ("fr-CA", "fr-CA-Sylvie:DragonHDLatestNeural", "Sylvie", "F"),
    ("fr-CA", "fr-CA-Thierry:DragonHDLatestNeural", "Thierry", "M"),
    ("es-MX", "es-MX-Dalia:DragonHDLatestNeural", "Dalia", "F"),
    ("es-MX", "es-MX-Jorge:DragonHDLatestNeural", "Jorge", "M"),
    ("en-US", "en-US-Ava:DragonHDLatestNeural", "Ava", "F"),
    ("en-US", "en-US-Emma:DragonHDLatestNeural", "Emma", "F"),
    ("en-US", "en-US-Andrew:DragonHDLatestNeural", "Andrew", "M"),
    ("en-US", "en-US-Brian:DragonHDLatestNeural", "Brian", "M"),
]


def dire(texte, langue, voix, dest):
    cle, region = cle_region()
    doc = ('<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" '
           f'xml:lang="{langue}"><voice name="{voix}"><lang xml:lang="{langue}">'
           f'{html.escape(texte)}</lang></voice></speak>')
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


if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    for langue, voix, nom, _ in VOIX:
        for i, texte in enumerate(PHRASES[langue], 1):
            d = DEST / f"{nom.lower()}-{i}.mp3"
            if not d.exists():
                dire(texte, langue, voix, d)
                print(f"  {d.name}")
