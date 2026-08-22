#!/usr/bin/env python3
"""Un extrait, une voix, et surtout : un mot isolé qui reste français.

**Le problème.** `eleven_multilingual_v2` devine la langue d'après le texte
qu'on lui donne. Sur une phrase, il ne se trompe jamais. Sur un mot nu, il n'a
presque rien à se mettre sous la dent — et « pain », « brin », « certain »,
« minute » ressortent régulièrement à l'anglaise ou à l'espagnole. Sur les
8413 extraits relevés du dépôt, **661 font deux mots ou moins** : c'est là que
la casse se produit, et c'est précisément le banc de vocabulaire et les cartes
de prononciation, là où l'élève vient chercher le modèle à imiter.

**Ce qui avait été tenté.** Réécrire le mot d'une façon qui n'existe pas en
anglais — « urgence » → « urjance », « minute » → « minutte ». Ça marche, un
mot à la fois, à condition d'avoir écouté le mot et deviné la graphie qui
sauve. Six cent soixante et une fois, ce n'est pas une méthode.

**Ce que fait ce module.** L'API accepte `previous_text` et `next_text` : du
texte qui **conditionne la synthèse sans être prononcé**. On donne donc au
modèle une phrase française avant et après le mot. Le mot sort seul dans le
fichier — l'élève n'entend que lui — mais le modèle, lui, a lu du français
autour et n'hésite plus sur la langue.

    from voix import charge_utile

    corps = charge_utile("pain", VOIX_ID)
    # → previous_text : « Écoutez bien ce mot en français. »
    #   text          : « pain »
    #   next_text     : « Répétez après moi, s'il vous plaît. »

Rien de tout cela n'est facturé comme de l'audio : seul `text` est synthétisé.

**Ce module n'a pas encore été éprouvé sur l'API** — le compte ElevenLabs est
à zéro depuis le 21 août 2026 et toute requête revient en 401. Avant de lancer
les milliers d'extraits en attente, il faut faire tourner
`python3 build/voix.py --essai` : il produit une dizaine de mots réputés
difficiles, à écouter un par un. Payer cinq mille extraits sur une hypothèse
non vérifiée serait exactement la faute que ce fichier existe pour éviter.
"""
import re
import sys

MODELE = "eleven_multilingual_v2"

# Le contexte n'est jamais prononcé : il n'a qu'à être franchement français.
# Une phrase de classe plutôt qu'une phrase quelconque — le registre teinte la
# prosodie, et c'est un professeur qu'on veut entendre.
AVANT = "Écoutez bien ce mot en français."
APRES = "Répétez après moi, s'il vous plaît."

# Au-delà de ce nombre de mots, le texte se suffit à lui-même : le modèle a
# assez de français sous les yeux pour ne pas se tromper de langue.
SEUIL_MOTS = 4


def compte_mots(texte):
    return len(re.findall(r"[\w'’-]+", texte or ""))


def est_court(texte):
    """Un extrait trop court pour porter sa propre langue."""
    return compte_mots(texte) <= SEUIL_MOTS


def charge_utile(texte, voix_id=None, stabilite=0.5, similarite=0.75,
                 avant=None, apres=None):
    """Le corps de la requête, avec le contexte quand le texte est court.

    `avant` et `apres` permettent de donner un contexte **propre à l'extrait**
    — la réplique qui précède dans un dialogue, par exemple, ce qui vaut mieux
    qu'une phrase générique. Sinon, le contexte de classe sert de défaut.
    """
    corps = {
        "text": texte,
        "model_id": MODELE,
        "voice_settings": {"stability": stabilite,
                           "similarity_boost": similarite},
    }
    if est_court(texte):
        corps["previous_text"] = avant if avant is not None else AVANT
        corps["next_text"] = apres if apres is not None else APRES
    elif avant or apres:
        # Un contexte explicite est toujours honoré, même sur un texte long :
        # c'est ce qui donne à une réplique la prosodie de sa réplique voisine.
        if avant:
            corps["previous_text"] = avant
        if apres:
            corps["next_text"] = apres
    return corps


def url(voix_id):
    return "https://api.elevenlabs.io/v1/text-to-speech/%s" % voix_id


# Les mots sur lesquels la langue a réellement basculé par le passé, plus
# quelques voisins du même genre : nasales, finales muettes, faux amis
# graphiques. C'est le banc d'essai à écouter avant de payer le reste.
MOTS_DIFFICILES = ["pain", "brun", "brin", "lundi", "certain", "aucun",
                   "magasin", "urgence", "minute", "pouce", "soupe", "chacun"]


def _essai():
    """Produit les mots difficiles, avec contexte et sans, pour comparer."""
    import json
    import os
    import pathlib
    import urllib.error
    import urllib.request

    env = pathlib.Path.home() / "Claude" / ".env"
    cle = os.environ.get("ELEVENLABS_API_KEY")
    if not cle and env.exists():
        for ligne in env.read_text(encoding="utf-8").splitlines():
            if ligne.strip().startswith("ELEVENLABS_API_KEY"):
                cle = ligne.split("=", 1)[1].strip().strip('"').strip("'")
    if not cle:
        print("✗ aucune clé ELEVENLABS_API_KEY"); return 2

    voix = sys.argv[2] if len(sys.argv) > 2 else "21m00Tcm4TlvDq8ikWAM"
    sortie = pathlib.Path.home() / "Claude" / "generations" / "essai-voix"
    sortie.mkdir(parents=True, exist_ok=True)
    for mot in MOTS_DIFFICILES:
        for etiquette, corps in (("sans", {"text": mot, "model_id": MODELE,
                                           "voice_settings": {"stability": 0.5,
                                           "similarity_boost": 0.75}}),
                                 ("avec", charge_utile(mot, voix))):
            req = urllib.request.Request(
                url(voix), data=json.dumps(corps).encode(),
                headers={"xi-api-key": cle, "Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    (sortie / ("%s-%s.mp3" % (mot, etiquette))).write_bytes(r.read())
                print("  ✓ %-10s %s" % (mot, etiquette))
            except urllib.error.HTTPError as e:
                print("  ✗ %-10s %s — HTTP %s %s"
                      % (mot, etiquette, e.code,
                         e.read()[:160].decode("utf-8", "replace")))
                return 1
    print("\nÀ écouter dans %s : « avec » doit être français, « sans » est le "
          "témoin." % sortie)
    return 0


if __name__ == "__main__":
    if "--essai" in sys.argv:
        sys.exit(_essai())
    for m in ("pain", "Je voudrais du pain brun, s'il vous plaît."):
        import json
        print("\n« %s » (%d mot·s)" % (m, compte_mots(m)))
        print(json.dumps(charge_utile(m, "VOIX"), ensure_ascii=False, indent=2))


def enrichir(corps):
    """Ajoute le contexte à une charge utile déjà construite.

    C'est le point d'entrée des quatre-vingts générateurs déjà écrits : ils
    bâtissent chacun leur charge utile à leur façon, mais ils passent tous par
    un `requests.post(..., json=…)`. Envelopper cet appel suffit, et ça évite
    de réécrire quatre-vingts scripts qui ne se ressemblent pas.

    On ne touche à rien si le contexte est déjà là : un générateur qui donne
    la réplique précédente d'un dialogue sait mieux que nous.
    """
    if not isinstance(corps, dict) or 'text' not in corps:
        return corps
    if 'previous_text' in corps or 'next_text' in corps:
        return corps
    if not est_court(corps['text']):
        return corps
    enrichi = dict(corps)
    enrichi['previous_text'] = AVANT
    enrichi['next_text'] = APRES
    return enrichi
