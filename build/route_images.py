#!/usr/bin/env python3
"""Une image, la route la moins chère qui répond — et jamais en silence.

Les 794 premières images du projet sont toutes passées par **fal.ai**. Ce
n'était pas un choix : un jour de mai, la voie Google avait renvoyé 403, on
avait branché fal.ai, et plus personne n'y était revenu. Les quatre routes ont
été mesurées le 21 août 2026, même prompt, même format, même résolution :

| Route                  | Délai  | Prix 1K   |
|------------------------|--------|-----------|
| Google direct — Lite   |  3,9 s | 0,0336 $  |
| Google direct — Flash  | 11,9 s | 0,067 $   |
| fal.ai                 | 14,5 s | 0,080 $   |
| WaveSpeed              | 25,9 s | 0,070 $   |
| Kie AI                 |   —    | HTTP 403  |

Les quatre revendent le **même modèle Google** (Nano Banana 2, Gemini 3.1
Flash Image). Le direct est 2,4 fois moins cher que fal.ai et 3,7 fois plus
rapide, pour une qualité que l'œil ne distingue pas. D'où l'ordre ci-dessous.

**On ne masque jamais un changement de route** : `generer_image` renvoie le nom
de celle qui a servi, et l'écrit dans le registre des appels. Une image du banc
produite chez un repli n'est pas un détail — c'est une ligne de facture et,
parfois, une différence de style.

Usage, dans un `gen_images.py` de module :

    sys.path.insert(0, str(BASE.parent.parent))      # jusqu'à build/
    from route_images import generer_image

    data, route = generer_image(prompt, ratio='3:2', module=MODULE,
                                cible=etiquette)
"""

import base64
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

ENV = pathlib.Path.home() / "Claude" / ".env"

# Le registre des appels vit hors du dépôt ; son absence ne doit rien casser
# (un agent distant ne l'a pas).
try:
    sys.path.insert(0, str(pathlib.Path.home() / "Claude" / "generations"))
    from journal_appels import enregistrer_appel
except Exception:                                            # pragma: no cover
    def enregistrer_appel(**_):
        pass


def _cles():
    valeurs = {}
    if not ENV.exists():
        return valeurs
    for ligne in ENV.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne or ligne.startswith("#") or "=" not in ligne:
            continue
        nom, _, val = ligne.partition("=")
        valeurs[nom.strip()] = val.strip().strip('"').strip("'")
    return valeurs


K = _cles()
# La clé Google a porté deux noms selon les époques ; on accepte les deux
# plutôt que de laisser un `.env` valide échouer sur une question d'étiquette.
GOOGLE = K.get("GOOGLE_API_KEY") or K.get("GOOGLE_KEY")
FAL = K.get("FAL_KEY")
WAVESPEED = K.get("WAVESPEED_API_KEY")


def _telecharger(url, delai=300):
    with urllib.request.urlopen(url, timeout=delai) as r:
        return r.read()


def _google(prompt, ratio, resolution):
    """Gemini 3.1 Flash Lite Image, en direct. La clé va dans l'URL."""
    modele = "gemini-3.1-flash-lite-image"
    url = ("https://generativelanguage.googleapis.com/v1beta/models/"
           "%s:generateContent?key=%s" % (modele, GOOGLE))
    corps = {"contents": [{"parts": [{"text": prompt}]}],
             "generationConfig": {"responseModalities": ["IMAGE"],
                                  "imageConfig": {"aspectRatio": ratio}}}
    req = urllib.request.Request(url, data=json.dumps(corps).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
        entetes = dict(r.headers)
    for part in d["candidates"][0]["content"]["parts"]:
        ligne = part.get("inlineData") or part.get("inline_data")
        if ligne:
            return base64.b64decode(ligne["data"]), entetes, modele
    raise RuntimeError("réponse Google sans image")


def _fal(prompt, ratio, resolution):
    corps = {"prompt": prompt, "num_images": 1, "aspect_ratio": ratio,
             "resolution": resolution, "output_format": "jpeg"}
    req = urllib.request.Request(
        "https://fal.run/fal-ai/nano-banana-2", data=json.dumps(corps).encode(),
        headers={"Authorization": "Key " + FAL,
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
        entetes = dict(r.headers)
    return _telecharger(d["images"][0]["url"]), entetes, "fal-ai/nano-banana-2"


def _wavespeed(prompt, ratio, resolution):
    corps = {"prompt": prompt, "aspect_ratio": ratio,
             "resolution": resolution.lower(), "output_format": "jpeg"}
    req = urllib.request.Request(
        "https://api.wavespeed.ai/api/v3/google/nano-banana-2/text-to-image",
        data=json.dumps(corps).encode(),
        headers={"Authorization": "Bearer " + WAVESPEED,
                 "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=300) as r:
        d = json.loads(r.read())
        entetes = dict(r.headers)
    ident = (d.get("data") or {}).get("id") or d.get("id")
    if not ident:
        raise RuntimeError("WaveSpeed : aucun identifiant de prédiction")
    suivi = urllib.request.Request(
        "https://api.wavespeed.ai/api/v3/predictions/%s/result" % ident,
        headers={"Authorization": "Bearer " + WAVESPEED})
    for _ in range(90):
        time.sleep(2)
        with urllib.request.urlopen(suivi, timeout=120) as r:
            data = (json.loads(r.read()).get("data") or {})
        if data.get("status") == "completed":
            sorties = data.get("outputs") or []
            if not sorties:
                raise RuntimeError("WaveSpeed : terminé sans image")
            return _telecharger(sorties[0]), entetes, "wavespeed/nano-banana-2"
        if data.get("status") in ("failed", "error"):
            raise RuntimeError("WaveSpeed : %s" % str(data.get("error"))[:150])
    raise RuntimeError("WaveSpeed : délai dépassé")


# L'ordre est celui du prix, mesuré — pas celui de l'habitude.
ROUTES = (("google", lambda: GOOGLE, _google),
          ("fal.ai", lambda: FAL, _fal),
          ("wavespeed", lambda: WAVESPEED, _wavespeed))


def generer_image(prompt, ratio="3:2", resolution="1K", module="", cible="",
                  bavard=True):
    """Rend `(données, route)`. Essaie les routes dans l'ordre du prix.

    Chaque tentative — réussie ou non — entre au registre des appels : c'est
    ce qui permet de compter ce qui est facturé plutôt que ce qui est gardé.
    """
    echecs = []
    for nom, cle, fonction in ROUTES:
        if not cle():
            echecs.append("%s : clé absente" % nom)
            continue
        try:
            data, entetes, modele = fonction(prompt, ratio, resolution)
        except urllib.error.HTTPError as e:
            detail = e.read()[:150].decode("utf-8", "replace")
            enregistrer_appel(fournisseur=nom, modele=nom, module=module,
                              cible=cible, statut="echec", http=e.code,
                              note=detail)
            echecs.append("%s : HTTP %s %s" % (nom, e.code, detail))
            if bavard:
                print("     ↳ %s a refusé (HTTP %s), route suivante"
                      % (nom, e.code), flush=True)
            continue
        except Exception as e:
            enregistrer_appel(fournisseur=nom, modele=nom, module=module,
                              cible=cible, statut="echec", note=str(e)[:150])
            echecs.append("%s : %s" % (nom, str(e)[:120]))
            if bavard:
                print("     ↳ %s a échoué (%s), route suivante"
                      % (nom, str(e)[:80]), flush=True)
            continue

        enregistrer_appel(fournisseur=nom, modele=modele, module=module,
                          cible=cible, statut="ok", entetes=entetes)
        if bavard and nom != "google":
            # Un repli ne passe jamais inaperçu : il coûte plus cher, et il
            # peut se voir dans le style de l'image.
            print("     ↳ produite par %s (repli), pas par Google" % nom,
                  flush=True)
        return data, nom

    raise RuntimeError("aucune route n'a produit l'image :\n  "
                       + "\n  ".join(echecs))


ESTIMATIONS = {"google": 0.0336, "fal.ai": 0.080, "wavespeed": 0.070}


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or (
        "Photographie réaliste, format paysage, lumière naturelle. Une tasse "
        "de café sur une table de bois. Aucun texte, aucun logo.")
    debut = time.time()
    data, route = generer_image(prompt, module="essai", cible="essai")
    cible = pathlib.Path.home() / "Claude" / "generations" / "essai-route.jpg"
    cible.write_bytes(data)
    print("✓ %s · %.1f s · %.0f Ko · %s"
          % (route, time.time() - debut, len(data) / 1024, cible))
