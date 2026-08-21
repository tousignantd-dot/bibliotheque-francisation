#!/usr/bin/env python3
"""
Générateur d'audio — module « Louer un logement » (module-n5-logement).
Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des cinq dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

Les identifiants de la famille 2 ne s'inventent pas : ils viennent du HTML.
Pour régénérer la liste après une modification de EXOS ou de PLUS, ouvrir le
module dans le navigateur et lancer dans la console :

    (()=>{SECTIONS.forEach(s=>{try{render(s.id)}catch(e){}});
     const m={}; document.querySelectorAll('[onclick*="playWord"]').forEach(el=>{
       const mm=el.getAttribute('onclick').match(
         /playWord\\(this,\\s*'((?:[^'\\\\]|\\\\.)*)'\\s*,\\s*'((?:[^'\\\\]|\\\\.)*)'\\)/);
       if(mm) m[mm[2].replace(/\\\\'/g,"'")]=mm[1].replace(/\\\\'/g,"'");});
     EXOS.filter(e=>e.type==='vf' && (e.cards||e.listen)).forEach(e=>
       e.rows.forEach(r=>{m[e.id+'_'+r.id]=r.txt.replace(/<[^>]+>/g,'')}));
     Object.assign(m, plAudioManifest()); return JSON.stringify(m);})()

puis coller le résultat dans sons_module_n5_logement.json, à côté de ce script.

La deuxième boucle n'est pas un doublon : dans les exercices à cartes
(cards/listen), le bouton d'écoute reçoit son gestionnaire en JS et non par un
attribut onclick — le premier sélecteur ne le voit donc pas.

Usage :  python3 generer_audio_module_n5_logement.py [--force] [--only prefixe,...]
"""
import json
import os
import sys
import time
import unicodedata
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ pip install requests"); sys.exit(1)

from voix_lente import ralentir_si_enseignante

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n5-logement"
MANIFESTE = RACINE / "sons_module_n5_logement.json"

ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s

# Mêmes identifiants que les autres modules, pour que les personnages sonnent
# pareil d'un module à l'autre.
VOIX = {
    "enseignante": "K7gx0ylJdff0yjM2uVQS",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Trois personnages, trois voix distinctes : Nadège et Hélène se répondent
# d'un bout à l'autre du module et ne peuvent donc pas partager la leur.
# Hélène prend la voix « enseignante », qui est ralentie à 0,85 — c'est un
# avantage ici : elle est la propriétaire au téléphone, celle qu'un élève de
# niveau 5 doit justement arriver à suivre.
VOIX_PERSO = {
    "NADÈGE": "feminin_2",
    "HÉLÈNE": "enseignante",
    "SAMUEL": "masculin_1",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]

DIALOGUES = {
    "prep": [
        ("NADÈGE", "Bonjour. J'ai reçu un papier de mon propriétaire et je ne suis pas certaine de le comprendre."),
        ("SAMUEL", "Assoyez-vous. Vous permettez que je le regarde ? … D'accord. C'est un avis de modification du bail."),
        ("NADÈGE", "Modification, ça veut dire qu'il me met dehors ?"),
        ("SAMUEL", "Non, pas du tout. Il vous annonce ce qu'il veut changer pour l'année prochaine. Ici, il demande soixante-quinze dollars de plus par mois."),
        ("NADÈGE", "Et là, en bas ? Il y a une ligne sur le stationnement."),
        ("SAMUEL", "Il veut aussi vous enlever la case de stationnement. Ça, c'est un deuxième changement, et il doit l'écrire séparément."),
        ("NADÈGE", "Est-ce que je suis obligée de dire oui ?"),
        ("SAMUEL", "Vous avez un mois pour répondre. Vous pouvez accepter, ou refuser par écrit. Si vous refusez, c'est lui qui doit s'adresser au Tribunal administratif du logement."),
        ("NADÈGE", "Un mois. Et si je ne réponds rien du tout ?"),
        ("SAMUEL", "Si vous ne répondez pas, la loi considère que vous avez accepté. C'est pour ça qu'il ne faut jamais laisser cet avis sur la table de cuisine."),
        ("NADÈGE", "De toute façon, ma fille dort dans le salon. Je pense que je vais chercher un quatre et demie."),
        ("SAMUEL", "Alors commençons par là. Regardez les annonces, notez tout ce qu'on vous dit au téléphone, et rappelez-moi avant de signer quoi que ce soit."),
    ],
    "t1": [
        ("HÉLÈNE", "Oui, allô ?"),
        ("NADÈGE", "Bonjour, madame. Je vous appelle pour le quatre et demie de la rue Bowen. Est-ce qu'il est encore libre ?"),
        ("HÉLÈNE", "Il est encore libre, oui. Le premier juillet."),
        ("NADÈGE", "Parfait. J'aimerais vous poser quelques questions, si vous avez deux minutes. Je prends des notes."),
        ("HÉLÈNE", "Allez-y."),
        ("NADÈGE", "Le loyer est de mille cinquante dollars. Est-ce que le chauffage est inclus ?"),
        ("HÉLÈNE", "Le chauffage n'est pas inclus. C'est électrique, et c'est à la charge du locataire. Comptez à peu près cent dollars par mois l'hiver."),
        ("NADÈGE", "Cent dollars l'hiver, d'accord. Et les électroménagers ?"),
        ("HÉLÈNE", "Le poêle et le réfrigérateur sont fournis. La laveuse et la sécheuse, non, mais il y a une buanderie au sous-sol."),
        ("NADÈGE", "Excusez-moi, vous pouvez répéter le dernier mot ?"),
        ("HÉLÈNE", "Une buanderie. Deux laveuses et deux sécheuses, au sous-sol de l'immeuble, deux dollars la brassée."),
        ("NADÈGE", "Merci. Et pour le stationnement ?"),
        ("HÉLÈNE", "Il y a une case derrière l'immeuble, incluse dans le loyer. Une seule, par exemple."),
        ("NADÈGE", "Une seule, ça me suffit. Dernière question : est-ce que je peux visiter cette semaine ?"),
        ("HÉLÈNE", "Jeudi soir, dix-huit heures ? L'adresse, c'est le quatre cent douze, rue Bowen, appartement trois."),
        ("NADÈGE", "Jeudi dix-huit heures, quatre cent douze Bowen, appartement trois. C'est noté. Merci beaucoup, madame."),
    ],
    "t1b": [
        ("SAMUEL", "Puis, cet appel ? Vous avez pris des notes ?"),
        ("NADÈGE", "J'ai tout écrit. Elle me dit que le logement est libre le premier juillet et que le loyer est de mille cinquante dollars."),
        ("SAMUEL", "Est-ce que vous lui avez demandé si le chauffage était compris ?"),
        ("NADÈGE", "C'est la première chose que j'ai demandée. Elle m'explique que le chauffage est électrique et qu'il n'est pas inclus."),
        ("SAMUEL", "Donc il faut ajouter cent dollars par mois à votre calcul, au moins l'hiver."),
        ("NADÈGE", "Elle me dit aussi qu'il y a une buanderie au sous-sol et qu'une case de stationnement vient avec le loyer."),
        ("SAMUEL", "Et vous savez ce qui n'est pas fourni ?"),
        ("NADÈGE", "La laveuse et la sécheuse. Le poêle et le réfrigérateur, eux, sont là."),
        ("SAMUEL", "Vous avez posé les bonnes questions. Il vous manque juste ce que personne ne pense à demander : le bruit, l'isolation, et depuis quand le loyer n'a pas augmenté."),
        ("NADÈGE", "Ça, je le demanderai jeudi, pendant la visite."),
    ],
    "t2": [
        ("HÉLÈNE", "Entrez, entrez. Vous enlevez vos bottes, si ça ne vous dérange pas."),
        ("NADÈGE", "Bien sûr. Oh, c'est clair, ici."),
        ("HÉLÈNE", "C'est la pièce que tout le monde aime. Les fenêtres donnent au sud, alors le salon est ensoleillé jusqu'à quatre heures."),
        ("NADÈGE", "Et le plancher, c'est du bois franc ?"),
        ("HÉLÈNE", "Du bois franc dans le salon et dans le corridor. Les chambres, c'est du flottant, refait l'an dernier."),
        ("NADÈGE", "Il y a deux chambres ?"),
        ("HÉLÈNE", "Deux vraies chambres, oui. Celle-ci donne sur la cour, donc c'est la plus tranquille. En arrivant, vous avez vu la ruelle : c'est de ce côté-là qu'il y a du passage."),
        ("NADÈGE", "Ma fille prendrait celle qui donne sur la cour, alors. Est-ce que c'est insonorisé entre les logements ?"),
        ("HÉLÈNE", "Honnêtement, on entend marcher au-dessus. Ce n'est pas un immeuble neuf. Les voisins d'en haut sont un couple retraité, très tranquilles."),
        ("NADÈGE", "Merci de me le dire. Et la cuisine, la hotte fonctionne ?"),
        ("HÉLÈNE", "Elle fonctionne. Le poêle et le réfrigérateur restent. Là, derrière la porte, c'est une remise : c'est petit, mais ça prend deux vélos."),
        ("NADÈGE", "Ça, c'est utile. Une dernière chose, madame : depuis quand le loyer n'a pas augmenté ?"),
        ("HÉLÈNE", "Bonne question. Le locataire actuel payait mille vingt dollars, et il est ici depuis trois ans. Je vais l'écrire dans le bail, c'est obligatoire."),
        ("NADÈGE", "Je vous remercie. En regardant les autres logements cette semaine, je vais comparer, mais je vous rappelle vendredi."),
        ("HÉLÈNE", "Prenez le temps qu'il faut. Je garde votre numéro."),
    ],
    "t3": [
        ("HÉLÈNE", "Voilà le bail. C'est le formulaire officiel, le même pour tout le monde au Québec."),
        ("NADÈGE", "Je vais le lire au complet, si vous permettez. … Ici, la section G, c'est quoi ?"),
        ("HÉLÈNE", "C'est l'avis au nouveau locataire. Je dois y écrire le loyer le plus bas payé dans les douze derniers mois. Mille vingt dollars, comme je vous l'ai dit."),
        ("NADÈGE", "Et moi, qu'est-ce que je peux faire avec cette information ?"),
        ("HÉLÈNE", "Si vous trouvez que l'augmentation est trop forte, vous avez dix jours après la signature pour demander une révision au Tribunal."),
        ("NADÈGE", "Dix jours. Je le note. Le bail se termine quand ?"),
        ("HÉLÈNE", "Le trente juin de l'année prochaine. Après, il se renouvellera tout seul aux mêmes conditions, sauf si l'un de nous deux envoie un avis."),
        ("NADÈGE", "Donc si je ne dis rien, je reste."),
        ("HÉLÈNE", "C'est exactement ça. Au Québec, le bail se renouvelle automatiquement. C'est une protection pour le locataire."),
        ("NADÈGE", "Et cette feuille-là, avec les règlements de l'immeuble ?"),
        ("HÉLÈNE", "C'est l'annexe. Elle fait partie du bail : pas de tapis dans l'escalier, les poubelles le mardi, et pas de barbecue sur le balcon. C'est le règlement de l'assureur, pas le mien."),
        ("NADÈGE", "Une dernière chose : si je dois partir avant la fin, est-ce que j'ai le droit de sous-louer ?"),
        ("HÉLÈNE", "Vous avez le droit de sous-louer ou de céder votre bail. Vous devez m'aviser par écrit, et je ne peux refuser sans un motif sérieux."),
        ("NADÈGE", "C'est clair. Alors je signe."),
    ],
}


def slug(nom):
    """Même règle que charSlug() dans le HTML — sinon le fichier n'est pas trouvé."""
    s = unicodedata.normalize("NFD", nom.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("'", "").replace(" ", "_")


def parle(cle, texte, voix, chemin):
    """Un extrait, avec reprise sur coupure réseau.

    ElevenLabs coupe la liaison par intermittence (`SSLEOFError`), parfois une
    heure durant. Une panne passagère du fournisseur n'est pas une erreur du
    programme : on réessaie en doublant l'attente, et on ne déclare l'échec
    qu'après cinq tentatives. Le script est relançable — il saute ce qui existe.
    """
    for essai in range(1, ESSAIS + 1):
        try:
            r = requests.post(
                f"https://api.elevenlabs.io/v1/text-to-speech/{voix}",
                json={"text": texte, "model_id": "eleven_multilingual_v2",
                      "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}},
                headers={"xi-api-key": cle, "Content-Type": "application/json"},
                timeout=60)
        except requests.exceptions.RequestException as e:
            if essai == ESSAIS:
                print(f"   ❌ réseau après {ESSAIS} essais : {type(e).__name__}")
                return False
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{attente}s", end="", flush=True)
            time.sleep(attente)
            continue

        # 429 (débit) et 5xx (panne du service) valent aussi une reprise ;
        # un 401 ou un 422 sont des erreurs à nous, inutile d'insister.
        if r.status_code in (429, 500, 502, 503, 504) and essai < ESSAIS:
            attente = ATTENTE_BASE_S * (2 ** (essai - 1))
            print(f"⏳{r.status_code}/{attente}s", end="", flush=True)
            time.sleep(attente)
            continue
        if r.status_code != 200:
            print(f"   ❌ {r.status_code}: {r.text[:150]}")
            return False

        chemin.parent.mkdir(parents=True, exist_ok=True)
        chemin.write_bytes(r.content)
        ralentir_si_enseignante(chemin, voix)
        return True
    return False


def main():
    cle = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not cle:
        env = RACINE / ".env"
        if env.exists():
            for ligne in env.read_text(encoding="utf-8").splitlines():
                if ligne.strip().startswith("ELEVENLABS_API_KEY="):
                    cle = ligne.split("=", 1)[1].strip().strip("\"'")
    if not cle:
        print("❌ ELEVENLABS_API_KEY absente (variable d'environnement ou .env)")
        sys.exit(1)

    force = "--force" in sys.argv
    only = []
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = [x.strip() for x in sys.argv[i + 1].split(",") if x.strip()]

    # ── Les répliques des dialogues ──────────────────────────────────
    taches = []
    for dial_id, lignes in DIALOGUES.items():
        for i, (perso, texte) in enumerate(lignes, 1):
            nom = f"line_{i:02d}_{slug(perso)}.mp3"
            taches.append((f"{dial_id}/{nom}", texte,
                           VOIX[VOIX_PERSO[perso]], SORTIE / dial_id / nom))

    # ── Les mots, phrases et mini-leçons ─────────────────────────────
    if not MANIFESTE.exists():
        print(f"❌ {MANIFESTE.name} introuvable — voir l'en-tête de ce script")
        sys.exit(1)
    sons = json.loads(MANIFESTE.read_text(encoding="utf-8"))
    for file_id, texte in sons.items():
        taches.append((f"sons/{file_id}", texte, VOIX_MOTS,
                       SORTIE / "sons" / f"{file_id}.mp3"))

    print(f"🔊 module-n5-logement — {len(taches)} extraits "
          f"({sum(len(v) for v in DIALOGUES.values())} répliques + {len(sons)} sons)\n")

    ok = saute = echec = 0
    for etiquette, texte, voix, chemin in taches:
        if only and not any(etiquette.startswith(o) or
                            chemin.stem.startswith(o) for o in only):
            continue
        if chemin.exists() and not force and not only:
            saute += 1
            continue
        print(f"  {etiquette:34s} « {texte[:40]} » → ", end="", flush=True)
        if parle(cle, texte, voix, chemin):
            print("✓"); ok += 1
        else:
            print("✗"); echec += 1
        time.sleep(0.35)

    print(f"\n✅ {ok} générés · {saute} déjà présents · {echec} en échec")
    if echec:
        sys.exit(1)


if __name__ == "__main__":
    main()
