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

**Une capsule = un appel.** Depuis le 3 septembre 2026, les plans d'une
capsule ne se synthétisent plus un par un : ils partent ensemble dans un seul
document SSML, et le son rendu est **découpé** aux frontières de plans. La
raison est un défaut entendu à la capsule 3 : « on passe du sourd au clair »
au milieu du film. La synthèse HD n'est pas déterministe — deux appels du même
texte ne donnent ni la même durée, ni tout à fait le même timbre — et six
appels donnaient donc six timbres bout à bout. Un seul tirage, un seul timbre
du début à la fin.

Le découpage se lit dans **le relevé des mots**, que le SDK rend pendant la
synthèse : on suit les lettres dites, et le plan change quand elles cessent
d'appartenir à son texte. La coupe tombe au milieu du silence qui sépare deux
plans — entre la fin du dernier mot de l'un et le début du premier mot de
l'autre. On synthétise en PCM (`Riff24Khz16BitMonoPcm`) pour couper à
l'échantillon, puis on encode chaque plan au format du dépôt ; découper un MP3
à la trame aurait décalé le son d'un demi-cadre à chaque plan.

**Les `<bookmark>` auraient été plus simples, et les voix HD les ignorent.**
Mesuré le 3 septembre 2026 : le même document rend deux repères avec
`fr-CA-ThierryNeural` et **aucun** avec `fr-CA-Thierry:DragonHDLatestNeural`.
C'est la même famille de silence que `<phoneme>` et `<lang>` autour d'un mot —
la voix HD accepte la balise et n'en fait rien. Ne pas y revenir sans
remesurer.

    python3 build/tutoriels/narrer.py            # tous les plans
    python3 build/tutoriels/narrer.py 01         # une capsule

Un plan peut porter un `texte_voix` à côté de son `texte` : c'est alors
celui-là qui part chez Azure, et `texte` ne sert plus qu'aux sous-titres. Il
n'y a pas d'autre moyen de faire dire « francisse » à une voix qui lit
« francis » sans le s final — les balises `<phoneme>` sont **ignorées** par
les voix DragonHD (mesuré : fichier identique à l'octet près), et le lexique
de `azure_voix.py` vaut pour tout le cours, où ce nom ne se dit jamais.

Sortie, par plan : `voix/<capsule>_<plan>.mp3`, `.txt` (le texte dit) et
`.json` (les mots et leur instant, **rebasés sur le début du plan**).
Relançable : une capsule dont aucun texte n'a bougé n'est pas resynthétisée.
Effacer un de ses MP3 suffit à la refaire — en entier, puisque c'est
l'unité.
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
# 500 ms, et **rien à l'intérieur d'une phrase**. À 800 ms le propos se
# hachait, et la pause posée après un deux-points s'entendait comme une
# coupure : « une phrase, puis tout à coup une coupure, la phrase reprend
# après ». Corrigé à l'écoute de la capsule 2, le 3 septembre 2026.
PAUSE_PHRASE = "500ms"     # après un point, un point d'exclamation, un point d'interrogation
PAUSE_SOUFFLE = None       # à l'intérieur d'une phrase : aucune
PAUSE_PLAN = "700ms"       # entre deux plans — elle appartient au plan qui finit

# `ssml()` échappe le texte : on ne peut pas y glisser une balise directement.
# On pose donc des caractères de contrôle, qui traversent `html.escape` sans
# être touchés, et on les remplace dans le document produit.
MARQUE_PHRASE, MARQUE_SOUFFLE, MARQUE_PLAN = chr(1), chr(2), chr(3)

TAUX = 24000        # Riff24Khz16BitMonoPcm
ENTETE_WAV = 44     # l'en-tête RIFF que le SDK écrit devant les échantillons


def respirer(texte):
    """Le texte, marqué là où la voix doit reprendre son souffle."""
    for signe in (". ", "! ", "? "):
        texte = texte.replace(signe, signe[0] + MARQUE_PHRASE + " ")
    if PAUSE_SOUFFLE:
        for signe in (" : ", " ; "):
            texte = texte.replace(signe, signe[:-1] + MARQUE_SOUFFLE + " ")
    return texte


def document(textes):
    """Le SSML d'une capsule entière, les plans mis bout à bout.

    `textes` est la liste des textes dits, dans l'ordre des plans. Le repère
    La seule marque posée entre deux plans est la pause qui les sépare ; c'est
    dans son silence que la coupe tombera.
    """
    corps = "".join(MARQUE_PLAN + respirer(t).strip() + " " for t in textes)
    doc = azure_voix.ssml(corps, ROLE)
    doc = doc.replace(MARQUE_PHRASE, '<break time="%s"/>' % PAUSE_PHRASE)
    if PAUSE_SOUFFLE:
        doc = doc.replace(MARQUE_SOUFFLE, '<break time="%s"/>' % PAUSE_SOUFFLE)
    doc = doc.replace(MARQUE_PLAN, "", 1)     # rien devant le premier plan
    return doc.replace(MARQUE_PLAN, '<break time="%s"/>' % PAUSE_PLAN)


def synthese():
    """Le synthétiseur et le flux d'événements, prêts à l'emploi."""
    import azure.cognitiveservices.speech as speechsdk

    cle, region = azure_voix.cle_region()
    if not cle:
        sys.exit("AZURE_SPEECH_KEY absente de ~/Claude/.env")
    config = speechsdk.SpeechConfig(subscription=cle, region=region)
    # On demande du PCM et non du MP3 : le découpage aux frontières de plans
    # doit tomber à l'échantillon près. Une coupe dans un flux MP3 se ferait à
    # la trame — 26 ms — et le décalage s'ajouterait de plan en plan. Le MP3
    # final est encodé par ffmpeg au format du dépôt (`azure_voix.FORMAT`),
    # celui que `monter_film.py` mixe.
    config.set_speech_synthesis_output_format(
        speechsdk.SpeechSynthesisOutputFormat.Riff24Khz16BitMonoPcm)
    return speechsdk, config


def duree(e):
    """La durée d'un mot, en secondes. Le SDK la rend en `timedelta`."""
    d = getattr(e, "duration", 0)
    return d.total_seconds() if hasattr(d, "total_seconds") else d / 10_000_000


def lettres(texte):
    """Le texte réduit à ses lettres et à ses chiffres, en minuscules.

    C'est la seule forme sur laquelle on peut faire correspondre le texte
    envoyé et les mots rendus : Azure découpe « c'est » en deux événements,
    laisse tomber la ponctuation, et rend « 2026 » d'un bloc.
    """
    return "".join(c for c in texte.lower() if c.isalnum())


def coupes(textes, mots):
    """Les instants où couper le son, un par frontière de plans.

    On suit les lettres dites : quand celles du plan courant sont épuisées, le
    plan suivant commence au mot d'après, et la coupe tombe **au milieu du
    silence** qui les sépare — la pause de `PAUSE_PLAN` appartient donc à
    moitié à chacun. Couper sur le premier mot du plan suivant lui collerait
    tout le silence en tête, ce qui s'entend au montage : le film change
    d'image, et la voix se fait attendre.
    """
    # On compte les lettres **telles que la voix les recevra** : `prononce()`
    # réécrit certains passages (les lettres nues, le lexique), et compter sur
    # le texte source décalerait le suivi d'autant.
    # `prononce()` rend du SSML : on retire ses balises et on **déséchappe**
    # ses entités. Sans le déséchappement, chaque apostrophe compte trois
    # lettres de plus (`&#x27;` → « x27 ») et le suivi glisse d'un mot.
    import html as _html
    import re as _re
    attendu = [len(lettres(_html.unescape(
        _re.sub(r"<[^>]+>", "", azure_voix.prononce(t))))) for t in textes]
    bornes, plan, compte = [], 0, 0
    for i, m in enumerate(mots):
        compte += len(lettres(m["mot"]))
        if plan < len(attendu) - 1 and compte >= attendu[plan]:
            suivant = mots[i + 1]["debut"] if i + 1 < len(mots) else m["fin"]
            bornes.append((m["fin"] + suivant) / 2)
            plan += 1
            compte = 0
    if len(bornes) != len(textes) - 1:
        raise RuntimeError(
            "%d frontières pour %d plans — le relevé des mots ne recouvre pas "
            "le texte envoyé" % (len(bornes), len(textes)))
    return bornes


def dire(speechsdk, config, textes, wav):
    """Synthétise la capsule entière dans `wav`. Rend la liste des mots.

    Chaque entrée est `{"mot", "debut", "fin"}`, en secondes depuis le début de
    la capsule. Les événements d'Azure sont donnés en centaines de nanosecondes
    — d'où la division par dix millions.
    """
    sortie = speechsdk.audio.AudioOutputConfig(filename=str(wav))
    synthetiseur = speechsdk.SpeechSynthesizer(speech_config=config,
                                               audio_config=sortie)
    # Azure émet aussi un événement pour la ponctuation, sans lettre et sans
    # durée utile. On l'écarte : il ne sert à aucun repère de tournage, et
    # laissé en place il devenait le « premier mot » du plan suivant, ce qui
    # posait la coupe juste après la dernière syllabe au lieu du milieu du
    # silence.
    mots = []
    synthetiseur.synthesis_word_boundary.connect(
        lambda e: lettres(e.text) and mots.append({
            "mot": e.text,
            "debut": e.audio_offset / 10_000_000,
            "fin": e.audio_offset / 10_000_000 + duree(e)}))

    resultat = synthetiseur.speak_ssml_async(document(textes)).get()
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


def clic(echantillons):
    """Le pire pic et le pire saut d'une suite d'échantillons.

    Le contrôle est nécessaire parce que **la synthèse HD n'est pas
    déterministe** : le même texte rend un fichier propre à un tirage et un
    fichier claqué au suivant. Sans ce contrôle, le défaut ne se trouve qu'au
    visionnement, une fois la capsule montée.
    """
    n = len(echantillons)
    if n < 2:
        return 0, 0
    pic = max(abs(x) for x in echantillons)
    saut = max(abs(echantillons[i + 1] - echantillons[i]) for i in range(n - 1))
    return pic, saut


def echantillons(wav):
    """Les échantillons signés du WAV rendu par Azure."""
    brut = wav.read_bytes()[ENTETE_WAV:]
    n = len(brut) // 2
    return struct.unpack("<%dh" % n, brut[:n * 2])


def encoder(v, debut, fin, mp3):
    """Encode la tranche [debut, fin[ (en échantillons) dans `mp3`."""
    tranche = v[debut:fin]
    brut = struct.pack("<%dh" % len(tranche), *tranche)
    subprocess.run(
        ["ffmpeg", "-y", "-v", "error", "-f", "s16le", "-ar", str(TAUX),
         "-ac", "1", "-i", "-", "-codec:a", "libmp3lame", "-b:a", "160k",
         "-ar", str(TAUX), "-ac", "1", str(mp3)],
        input=brut, check=True, stdout=subprocess.DEVNULL)


def dire_proprement(speechsdk, config, textes, wav):
    """Synthétise la capsule, et recommence si le tirage sort un clic.

    Trois essais : au-delà, on garde le moins mauvais et on le dit. Boucler
    sans fin sur un texte qui claquerait à tous les coups coûterait des appels
    pour rien.
    """
    meilleur = None
    for essai in range(1, ESSAIS + 1):
        mots = dire(speechsdk, config, textes, wav)
        v = echantillons(wav)
        pic, saut = clic(v)
        if not (pic >= PIC_SUSPECT and saut >= SAUT_SUSPECT):
            return mots, v
        if meilleur is None or saut < meilleur[0]:
            meilleur = (saut, mots, v)
        print("    clic au tirage %d (pic %d, saut %d) — on recommence"
              % (essai, pic, saut))
    print("    %d tirages, tous claqués — on garde le moins mauvais" % ESSAIS)
    return meilleur[1], meilleur[2]


def narrer(speechsdk, config, capsule):
    """Une capsule : un appel, puis un fichier par plan."""
    plans = capsule["plans"]
    textes = [p.get("texte_voix", p["texte"]) for p in plans]
    wav = SORTIE / ("%s.wav" % capsule["id"])
    mots, v = dire_proprement(speechsdk, config, textes, wav)

    frontieres = [0.0] + coupes(textes, mots)
    bornes = [int(round(t * TAUX)) for t in frontieres] + [len(v)]
    for i, plan in enumerate(plans):
        base = "%s_%s" % (capsule["id"], plan["id"])
        mp3 = SORTIE / (base + ".mp3")
        encoder(v, bornes[i], bornes[i + 1], mp3)
        (SORTIE / (base + ".txt")).write_text(textes[i], encoding="utf-8")
        # Les instants sont rebasés sur le début du plan : `enregistrer.js`
        # démarre son chronomètre à la première image du plan, pas à celle de
        # la capsule.
        debut, fin = bornes[i] / TAUX, bornes[i + 1] / TAUX
        siens = [{"mot": m["mot"], "debut": round(m["debut"] - debut, 3)}
                 for m in mots if debut - 0.001 <= m["debut"] < fin]
        # `{"mots": [...]}` et non une liste nue : c'est la forme que
        # `enregistrer.js` lit (`JSON.parse(...).mots`).
        (SORTIE / (base + ".json")).write_text(
            json.dumps({"mots": siens}, ensure_ascii=False, indent=1),
            encoding="utf-8")
        print("  %s  (%d ko, %d mots relevés, %.1f s)"
              % (mp3.name, mp3.stat().st_size // 1024, len(siens), fin - debut))
    wav.unlink()


def main():
    filtre = sys.argv[1] if len(sys.argv) > 1 else None
    SORTIE.mkdir(exist_ok=True)
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    faits = refaites = 0
    speechsdk = config = None
    for capsule in manifeste["capsules"]:
        if filtre and not capsule["id"].startswith(filtre):
            continue
        faits += 1
        # Le texte dit est gardé à côté du son : se fier à la seule présence du
        # MP3 laisserait un plan réécrit garder l'ancienne narration, et
        # l'erreur ne s'entend qu'au visionnement final. La capsule entière est
        # l'unité — un plan réécrit fait refaire ses voisins, et c'est le prix
        # du timbre unique.
        inchangee = True
        for plan in capsule["plans"]:
            base = SORTIE / ("%s_%s" % (capsule["id"], plan["id"]))
            mp3, trace, releve = (base.with_suffix(".mp3"),
                                  base.with_suffix(".txt"),
                                  base.with_suffix(".json"))
            if not (mp3.exists() and mp3.stat().st_size > 1000
                    and releve.exists() and trace.exists()
                    and trace.read_text(encoding="utf-8")
                    == plan.get("texte_voix", plan["texte"])):
                inchangee = False
                break
        if inchangee:
            continue
        if speechsdk is None:
            speechsdk, config = synthese()
        print("%s — %d plans en un seul appel" % (capsule["id"],
                                                  len(capsule["plans"])))
        narrer(speechsdk, config, capsule)
        refaites += 1
    print("%d capsules, %d synthétisées cette fois" % (faits, refaites))


if __name__ == "__main__":
    main()
