#!/usr/bin/env python3
"""Écouter les MP3 du cours à la place de l'oreille — et dire ceux qui mentent.

    python3 build/oreille_azure.py --echantillon 40   # un sondage, quelques cents
    python3 build/oreille_azure.py --tous             # les 21 403 fichiers
    python3 build/oreille_azure.py module-n5-transport
    python3 build/oreille_azure.py --bilan            # relit le journal, n'appelle rien

Ce que les autres contrôles ne peuvent pas faire
------------------------------------------------
`build/audio_manquant.py` dit qu'un fichier EXISTE. Il ne dit pas ce qu'il
CONTIENT. Un MP3 tronqué, un MP3 qui porte le texte du voisin, une épellation
sortie en anglais : tout cela pèse le bon nombre d'octets et passe tous les
contrôles du dépôt. Le seul juge est l'écoute — et 21 403 fichiers, soit près
de dix-neuf heures, ne s'écoutent pas à la main.

On transcrit donc chaque extrait par Azure Speech, et on compare au texte que
le relevé annonce. La comparaison réutilise `couvre()` du gabarit : la même
règle que celle qui juge les réponses des élèves, pour ne pas avoir deux
mesures de « c'est la même phrase » dans le dépôt.

Ce que ça attrape, et ce que ça n'attrape pas
----------------------------------------------
Attrapé : le fichier vide ou tronqué, le mauvais texte, la langue qui dérape,
le mot avalé. **Pas attrapé : l'accent et le naturel.** Une transcription juste
ne prouve pas qu'un élève entendra du français d'ici — c'est déjà écrit dans le
banc d'essai Gemini, et un modèle reste mauvais juge d'un accent. Ce contrôle
réduit l'écoute humaine à une poignée de suspects ; il ne la remplace pas.

Les cinq familles de faux positifs, mesurées sur 330 extraits
--------------------------------------------------------------
Un contrôle qui a tort coûte plus cher que pas de contrôle : on irait écouter
des fichiers sains. Ce qui reste signalé après la conversion des nombres est
presque toujours l'une de ces cinq choses, et aucune n'est un défaut du MP3 :

  · l'impératif entendu à l'infinitif — « Coupez » / « Couper », homophones ;
  · le singulier pour le pluriel — « Ils vérifient » / « Il vérifie », « quels »
    / « quel » : la marque ne s'entend pas en français ;
  · les homophones vrais — « L'avis » / « La vie » ;
  · les noms propres — « Tereza Nogueira » / « Teresa Noguera » ;
  · le mot isolé très court, rendu vide ou déformé : « peu » (0,3 s) ne donne
    rien du tout, « Mets ta tuque ! » revient « Métatique ». C'est la même
    raison qui veut qu'on présente un mot dans une phrase porteuse.

Sur les 330 premiers extraits, 16 signalements, TOUS de ces familles-là, et
aucun fichier fautif. Vérifiez la durée avant d'écouter : un fichier vide ou
tronqué se voit à la seconde, et se distingue ainsi d'un mot que la machine
n'a pas su lire.

Le journal `data/oreille.json` garde ce qui a été écouté : relancer ne repaie
pas ce qui est déjà jugé, et `--bilan` renote sans un seul appel.
"""
import json
import os
import pathlib
import random
import sys
import time
import urllib.error
import urllib.request
import uuid

RACINE = pathlib.Path(__file__).resolve().parent.parent
JOURNAL = RACINE / "data" / "oreille.json"
SEUIL = 0.7          # sous ce taux de mots retrouvés, on signale


def cle_azure():
    c = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not c:
        env = pathlib.Path.home() / "Claude" / ".env"
        if env.exists():
            for l in env.read_text(encoding="utf-8").splitlines():
                if l.strip().startswith("AZURE_SPEECH_KEY="):
                    c = l.split("=", 1)[1].strip().strip("\"'")
    return c


def transcrire(cle, chemin):
    region = os.environ.get("AZURE_SPEECH_REGION", "").strip() or "canadacentral"
    lim = "----francisation" + uuid.uuid4().hex
    audio = chemin.read_bytes()
    corps = b"".join([
        ("--%s\r\n" % lim).encode(), b'Content-Disposition: form-data; name="definition"\r\n',
        b"Content-Type: application/json\r\n\r\n",
        json.dumps({"locales": ["fr-CA"]}).encode(), b"\r\n",
        ("--%s\r\n" % lim).encode(),
        ('Content-Disposition: form-data; name="audio"; filename="%s"\r\n' % chemin.name).encode(),
        b"Content-Type: application/octet-stream\r\n\r\n", audio, b"\r\n",
        ("--%s--\r\n" % lim).encode(),
    ])
    req = urllib.request.Request(
        "https://%s.api.cognitive.microsoft.com/speechtotext/transcriptions"
        ":transcribe?api-version=2024-11-15" % region,
        data=corps,
        headers={"Ocp-Apim-Subscription-Key": cle,
                 "Content-Type": "multipart/form-data; boundary=%s" % lim,
                 "Accept": "application/json", "User-Agent": "francisation"},
        method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        d = json.loads(r.read().decode("utf-8"))
    return " ".join(p.get("text", "") for p in d.get("combinedPhrases", [])).strip()


# ── la comparaison : celle du gabarit, pas une autre ──────────────────
import re
GAB = (RACINE / "build" / "gabarit" / "module.html").read_text(encoding="utf-8")
_bloc = GAB[GAB.index("const WSTOP"):GAB.index("function wBoutonReponse")]
_STOP = set(re.search(r"new Set\(\('([^']*)'", _bloc.replace("\n", " ")).group(1).split() ) \
    if re.search(r"new Set\(\('([^']*)'", _bloc.replace("\n", " ")) else set()
_STOP |= set("a au aux avec c ce ces cet cette d dans de des du elle en est et eux il ils j je "
             "l la le les leur lui ma mais me mes moi mon n ne nos notre nous on ou par pas plus "
             "pour qu que qui sa se ses son sont sur ta te tes toi ton tous tout tres tu un une "
             "vos votre vous y".split())
# La reconnaissance écrit les nombres en CHIFFRES — « trois cents pages » lui
# revient « 300 pages », « quarante minutes » « 40 min ». Sans conversion, le
# premier sondage de 300 extraits a rendu 38 « suspects » dont presque tous
# n'étaient que cela : un contrôle qui a tort coûte plus cher que pas de
# contrôle, parce qu'on va écouter trente-huit fichiers sains. On ramène donc
# les deux côtés au même alphabet : tout en chiffres.
UNITES = {"zero": 0, "un": 1, "une": 1, "deux": 2, "trois": 3, "quatre": 4, "cinq": 5,
          "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10, "onze": 11, "douze": 12,
          "treize": 13, "quatorze": 14, "quinze": 15, "seize": 16, "vingt": 20,
          "trente": 30, "quarante": 40, "cinquante": 50, "soixante": 60, "cent": 100,
          "cents": 100, "mille": 1000}
ABREV = {"min": "minutes", "h": "heures", "hre": "heures", "hres": "heures",
         "sec": "secondes", "ml": "millilitres", "cl": "centilitres",
         "l": "litres", "kg": "kilogrammes", "g": "grammes", "km": "kilometres",
         "m": "metres", "cm": "centimetres", "$": "dollars", "pct": "pourcent"}


def _chiffrer(ms):
    """« trois cents » → « 300 », « vingt et un » → « 21 ». Laisse le reste."""
    out, i = [], 0
    while i < len(ms):
        if ms[i] not in UNITES:
            out.append(ms[i]); i += 1; continue
        total, courant, j = 0, 0, i
        while j < len(ms) and (ms[j] in UNITES or ms[j] in ("et", "quatre")):
            if ms[j] == "et":
                j += 1; continue
            v = UNITES[ms[j]]
            if v == 1000:
                total += (courant or 1) * 1000; courant = 0
            elif v == 100:
                courant = (courant or 1) * 100
            else:
                courant += v
            j += 1
        out.append(str(total + courant)); i = j
    return out


def mots(s):
    s = (s or "").lower()
    s = "".join(c for c in __import__("unicodedata").normalize("NFD", s)
                if __import__("unicodedata").category(c) != "Mn")
    s = s.replace("½", " et demi").replace("$", " dollars ").replace("%", " pourcent ")
    s = re.sub(r"(\d)\s*h\s*(\d\d)", r"\1 heures \2", s)   # 6h50 → 6 heures 50
    # On chiffre SEGMENT par segment : « Deux. Douze. » sans cette coupure
    # devient un seul nombre, quatorze, et ne ressemble plus à « 2, 12 ».
    segments = [seg for seg in re.split(r"[^a-z0-9]+", s.replace(",", " , ")
                                        .replace(".", " . ")) if seg] \
        if False else [s2 for s2 in re.split(r"[.,;:!?]+", s) if s2.strip()]
    out = []
    for seg in segments:
        ms = [ABREV.get(m, m) for m in re.sub(r"[^a-z0-9]+", " ", seg).split()]
        out += _chiffrer(ms)
    return [m for m in out if len(m) > 1 and m not in _STOP]


def couvre(attendu, entendu):
    a = mots(attendu)
    if not a:
        return 1.0
    d = set(mots(entendu))
    return sum(1 for m in a if m in d) / len(a)


def cibles(filtre):
    """(slug, file_id, chemin, texte attendu) pour tout ce que les relevés annoncent."""
    out = []
    for rel in sorted((RACINE / "manifestes").glob("sons_module_*.json")):
        slug = "module-" + rel.stem[len("sons_module_"):].replace("_", "-")
        if filtre and filtre not in slug:
            continue
        try:
            sons = json.loads(rel.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        for fid, txt in sons.items():
            p = RACINE / "assets" / "interactive" / slug / "sons" / (fid + ".mp3")
            if p.exists():
                out.append((slug, fid, p, txt))
    return out


def main():
    a = sys.argv[1:]
    if "--bilan" in a:
        j = json.loads(JOURNAL.read_text(encoding="utf-8")) if JOURNAL.exists() else {}
        mauvais = {k: v for k, v in j.items() if v.get("taux", 1) < SEUIL}
        print("%d extrait(s) écouté(s) · %d suspect(s)" % (len(j), len(mauvais)))
        for k, v in sorted(mauvais.items(), key=lambda x: x[1]["taux"])[:40]:
            print("  %.2f  %s\n        attendu : %s\n        entendu : %s"
                  % (v["taux"], k, v["attendu"][:80], v["entendu"][:80]))
        return

    cle = cle_azure()
    if not cle:
        sys.exit("❌ AZURE_SPEECH_KEY absente (environnement ou ~/Claude/.env)")

    n = None
    filtre = None
    for i, x in enumerate(a):
        if x == "--echantillon" and i + 1 < len(a):
            n = int(a[i + 1])
        elif not x.startswith("--") and not x.isdigit():
            filtre = x
    liste = cibles(filtre)
    journal = json.loads(JOURNAL.read_text(encoding="utf-8")) if JOURNAL.exists() else {}
    liste = [c for c in liste if (c[0] + "/" + c[1]) not in journal]
    if n:
        # Un sondage, pas les n premiers : les premiers d'une liste triée sont
        # tous du même module, et un module sain ferait croire à un cours sain.
        random.seed(28082026)
        random.shuffle(liste)
        liste = liste[:n]

    print("%d extrait(s) à écouter\n" % len(liste))
    suspects = 0
    for i, (slug, fid, p, txt) in enumerate(liste, 1):
        try:
            entendu = transcrire(cle, p)
        except (urllib.error.HTTPError, urllib.error.URLError, OSError) as e:
            print("  ❌ %s/%s — %s" % (slug, fid, str(e)[:80]))
            continue
        t = couvre(txt, entendu)
        journal[slug + "/" + fid] = {"taux": round(t, 3), "attendu": txt, "entendu": entendu}
        if t < SEUIL:
            suspects += 1
            print("  ⚠️  %.2f  %s/%s\n        attendu : %s\n        entendu : %s"
                  % (t, slug, fid, txt[:80], entendu[:80]))
        if i % 20 == 0:
            JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=1), encoding="utf-8")
            print("     … %d/%d" % (i, len(liste)))
        time.sleep(0.2)
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    JOURNAL.write_text(json.dumps(journal, ensure_ascii=False, indent=1), encoding="utf-8")
    print("\n✅ %d écouté(s) · %d suspect(s) · journal : %s"
          % (len(liste), suspects, JOURNAL.relative_to(RACINE)))


if __name__ == "__main__":
    main()
