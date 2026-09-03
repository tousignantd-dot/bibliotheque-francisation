#!/usr/bin/env python3
"""Narration des capsules chez Azure, voix HD — et le relevé des mots.

Remplace, le 2 septembre 2026, la paire `narrer.py` (ElevenLabs) +
`aligner.py` (alignement forcé d'ElevenLabs). Deux raisons, et la seconde
n'est pas la moindre :

· **Le cours a changé de fournisseur.** Les voix se font chez Azure depuis le
  26 août 2026, et les MP3 de la bibliothèque sont gelés. Garder ElevenLabs
  pour les seuls tutoriels aurait laissé un fournisseur en vie pour sept
  fichiers, avec sa clé, son quota et sa facture.

· **Une seule passe au lieu de deux.** Le SDK Azure rend les `WordBoundary`
  *pendant* la synthèse : l'audio et la position de chaque mot sortent du même
  appel. L'ancienne chaîne synthétisait, puis renvoyait le MP3 à un service
  d'alignement — deux appels, deux factures, et un risque de désaccord entre
  le son produit et le son analysé.

La voix est `hd_masculin` (fr-CA-Thierry, modèle DragonHD), déclarée dans
`build/azure_voix.py` comme le reste du dépôt. Pas de taux global : le
narrateur s'adresse à une enseignante, pas à un élève débutant — le +15 % et
l'échelle par niveau n'ont rien à faire ici.

    python3 build/tutoriels/narrer.py            # tous les plans
    python3 build/tutoriels/narrer.py 01         # une capsule

Un plan peut porter un `texte_voix` à côté de son `texte` : c'est alors
celui-là qui part chez Azure, et `texte` ne sert plus qu'aux sous-titres. Il
n'y a pas d'autre moyen de faire dire « francisse » à une voix qui lit
« francis » sans le s final — les balises `<phoneme>` sont **ignorées** par
les voix DragonHD (mesuré : fichier identique à l'octet près), et le lexique
de `azure_voix.py` vaut pour tout le cours, où ce nom ne se dit jamais.

Sortie, par plan : `voix/<capsule>_<plan>.mp3`, `.txt` (le texte dit) et
`.json` (les mots et leur instant). Relançable : un plan dont le texte n'a pas
bougé n'est pas resynthétisé. Effacer son MP3 suffit à le refaire.
"""
import json
import pathlib
import struct
import subprocess
import sys

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))          # pour azure_voix
import azure_voix                             # noqa: E402

ROLE = "hd_masculin"
SORTIE = ICI / "voix"

# Le souffle entre les phrases. Sans lui, Azure enchaîne les phrases d'une
# capsule comme une liste qu'on récite — signalé au visionnement, le
# 3 septembre 2026 : « il n'y a pas beaucoup de pauses après les points ».
# Mesuré : deux `<break time="700ms"/>` allongent un plan de 1,8 s, donc les
# voix HD les honorent — contrairement à `<phoneme>` et à `<lang>` autour d'un
# mot, qu'elles ignorent.
PAUSE_PHRASE = "800ms"     # après un point, un point d'exclamation, un point d'interrogation
PAUSE_SOUFFLE = "350ms"    # après un deux-points ou un point-virgule

# `ssml()` échappe le texte : on ne peut pas y glisser une balise directement.
# On pose donc des caractères de contrôle, qui traversent `html.escape` sans
# être touchés, et on les remplace dans le document produit.
MARQUE_PHRASE, MARQUE_SOUFFLE = chr(1), chr(2)


def respirer(texte):
    """Le texte, marqué là où la voix doit reprendre son souffle."""
    for signe in (". ", "! ", "? "):
        texte = texte.replace(signe, signe[0] + MARQUE_PHRASE + " ")
    for signe in (" : ", " ; "):
        texte = texte.replace(signe, signe[:-1] + MARQUE_SOUFFLE + " ")
    return texte


def document(texte):
    """Le SSML d'un plan, pauses comprises."""
    doc = azure_voix.ssml(respirer(texte), ROLE)
    return (doc.replace(MARQUE_PHRASE, '<break time="%s"/>' % PAUSE_PHRASE)
               .replace(MARQUE_SOUFFLE, '<break time="%s"/>' % PAUSE_SOUFFLE))


def synthese():
    """Le synthétiseur et le flux d'événements, prêts à l'emploi."""
    import azure.cognitiveservices.speech as speechsdk

    cle, region = azure_voix.cle_region()
    if not cle:
        sys.exit("AZURE_SPEECH_KEY absente de ~/Claude/.env")
    config = speechsdk.SpeechConfig(subscription=cle, region=region)
    # Le même format que le reste du dépôt (`azure_voix.FORMAT`) : c'est ce
    # que `monter_film.py` mixe, et un débit binaire plus bas s'entendrait à
    # côté des modules.
    config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Audio24Khz160KBitRateMonoMp3)
    return speechsdk, config


def dire(speechsdk, config, texte, mp3):
    """Synthétise `texte` dans `mp3`. Renvoie la liste des mots et leur instant.

    Chaque entrée est `{"mot": ..., "debut": secondes}`. Les `WordBoundary`
    d'Azure sont donnés en centaines de nanosecondes depuis le début de
    l'énoncé — d'où la division par dix millions.
    """
    sortie = speechsdk.audio.AudioOutputConfig(filename=str(mp3))
    synthetiseur = speechsdk.SpeechSynthesizer(speech_config=config,
                                               audio_config=sortie)
    mots = []
    synthetiseur.synthesis_word_boundary.connect(
        lambda e: mots.append({"mot": e.text,
                               "debut": round(e.audio_offset / 10_000_000, 3)}))
    resultat = synthetiseur.speak_ssml_async(document(texte)).get()
    if resultat.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
        detail = getattr(resultat, "cancellation_details", None)
        raise RuntimeError("Azure a refusé : %s" % (detail.error_details
                                                    if detail else resultat.reason))
    return mots


# Un clic de synthèse : un échantillon qui saute d'un coup à pleine échelle,
# là où la parole vit entre 5 000 et 15 000. Entendu le 3 septembre 2026 à la
# 58e seconde de la capsule 1 — pic à 31 035 sur 32 767, saut de 16 086 en un
# échantillon, juste après une pause et avant « Ma classe ».
PIC_SUSPECT = 29000
SAUT_SUSPECT = 12000
ESSAIS = 3


def clic(mp3):
    """Le pire pic et le pire saut du fichier. (0, 0) si on ne peut pas lire.

    Le contrôle est nécessaire parce que **la synthèse HD n'est pas
    déterministe** : le même texte rend un fichier propre à un tirage et un
    fichier claqué au suivant. Sans ce contrôle, le défaut ne se trouve qu'au
    visionnement, une fois la capsule montée.
    """
    try:
        brut = subprocess.run(
            ["ffmpeg", "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "24000",
             "-f", "s16le", "-"], capture_output=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return 0, 0
    n = len(brut) // 2
    if n < 2:
        return 0, 0
    v = struct.unpack("<%dh" % n, brut[:n * 2])
    pic = max(abs(x) for x in v)
    saut = max(abs(v[i + 1] - v[i]) for i in range(n - 1))
    return pic, saut


def dire_proprement(speechsdk, config, texte, mp3):
    """Synthétise, et recommence si le tirage sort un clic.

    Trois essais : au-delà, on garde le moins mauvais et on le dit. Boucler
    sans fin sur un texte qui claquerait à tous les coups coûterait des appels
    pour rien.
    """
    meilleur = None
    for essai in range(1, ESSAIS + 1):
        mots = dire(speechsdk, config, texte, mp3)
        pic, saut = clic(mp3)
        if not (pic >= PIC_SUSPECT and saut >= SAUT_SUSPECT):
            return mots
        garde = mp3.with_suffix(".essai%d.mp3" % essai)
        mp3.replace(garde)
        if meilleur is None or saut < meilleur[2]:
            meilleur = (garde, mots, saut)
        print("    clic au tirage %d (pic %d, saut %d) — on recommence"
              % (essai, pic, saut))
    meilleur[0].replace(mp3)
    for reste in mp3.parent.glob(mp3.stem + ".essai*.mp3"):
        reste.unlink()
    print("    %s : %d tirages, tous claqués — on garde le moins mauvais"
          % (mp3.name, ESSAIS))
    return meilleur[1]


def main():
    filtre = sys.argv[1] if len(sys.argv) > 1 else None
    SORTIE.mkdir(exist_ok=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    speechsdk, config = synthese()
    faits = refaits = 0
    for capsule in manifeste["capsules"]:
        if filtre and not capsule["id"].startswith(filtre):
            continue
        for plan in capsule["plans"]:
            base = "%s_%s" % (capsule["id"], plan["id"])
            dit = plan.get("texte_voix", plan["texte"])
            mp3 = SORTIE / (base + ".mp3")
            trace = SORTIE / (base + ".txt")
            releve = SORTIE / (base + ".json")
            faits += 1
            # Le texte dit est gardé à côté du son : se fier à la seule
            # présence du MP3 laisserait un plan réécrit garder l'ancienne
            # narration, et l'erreur ne s'entend qu'au visionnement final.
            inchange = (mp3.exists() and mp3.stat().st_size > 1000
                        and releve.exists() and trace.exists()
                        and trace.read_text(encoding="utf-8") == dit)
            if inchange:
                continue
            mots = dire_proprement(speechsdk, config, dit, mp3)
            trace.write_text(dit, encoding="utf-8")
            # `{"mots": [...]}` et non une liste nue : c'est la forme que
            # `enregistrer.js` lit (`JSON.parse(...).mots`).
            releve.write_text(json.dumps({"mots": mots}, ensure_ascii=False,
                                         indent=1), encoding="utf-8")
            refaits += 1
            print("  %s  (%d ko, %d mots relevés, %.1f s)"
                  % (mp3.name, mp3.stat().st_size // 1024, len(mots),
                     azure_voix.duree(mp3)))
    print("%d plans, %d synthétisés cette fois" % (faits, refaits))


if __name__ == "__main__":
    main()
