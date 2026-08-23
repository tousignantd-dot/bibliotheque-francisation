#!/usr/bin/env python3
"""
Générateur d'audio — module « Les services de ma ville » (module-n5-services).
Deux familles de fichiers, comme dans les autres modules :

  1. les répliques des quatre dialogues → <module>/<dialId>/line_NN_<perso>.mp3
  2. les mots, phrases et mini-leçons → <module>/sons/<fileId>.mp3

Les identifiants de la famille 2 ne s'inventent pas : ils viennent du HTML
produit, relevés dans sons_module_n5_services.json (115 extraits). Pour les
refaire après une modification de EXOS ou de PLUS, ouvrir le module dans le
navigateur et lancer dans la console :

    (()=>{SECTIONS.forEach(s=>{try{render(s.id)}catch(e){}});
     const m={}; document.querySelectorAll('[onclick*="playWord"]').forEach(el=>{
       const mm=el.getAttribute('onclick').match(
         /playWord\\(this,\\s*'((?:[^'\\\\]|\\\\.)*)'\\s*,\\s*'((?:[^'\\\\]|\\\\.)*)'\\)/);
       if(mm) m[mm[2].replace(/\\\\'/g,"'")]=mm[1].replace(/\\\\'/g,"'");});
     EXOS.filter(e=>e.type==='vf' && (e.cards||e.listen)).forEach(e=>
       e.rows.forEach(r=>{m[e.id+'_'+r.id]=r.txt.replace(/<[^>]+>/g,'')}));
     Object.assign(m, plAudioManifest()); return JSON.stringify(m);})()

La deuxième boucle n'est pas un doublon : dans les exercices à cartes
(cards/listen), le bouton d'écoute reçoit son gestionnaire en JS et non par un
attribut onclick — le premier sélecteur ne le voit donc pas.

**ElevenLabs coupe la liaison TLS par intermittence depuis le 20 août 2026.**
`parle()` réessaie cinq fois en doublant l'attente, et le script est relançable :
il saute ce qui existe déjà. Un échec réseau ne dit rien du texte. Le lancer
hors du bac à sable (`dangerouslyDisableSandbox`) et boucler la relance plutôt
que de surveiller la première passe — voir docs/chantier-tous-niveaux.md.

Usage :  python3 generer_audio_module_n5_services.py [--force] [--only prefixe,...]
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
import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))
from voix import enrichir  # contexte français pour les mots isolés

RACINE = Path(__file__).resolve().parent
SORTIE = RACINE / "assets/interactive/module-n5-services"
MANIFESTE = RACINE / "sons_module_n5_services.json"

ESSAIS = 5           # tentatives par extrait
ATTENTE_BASE_S = 4   # doublée à chaque échec : 4, 8, 16, 32 s

# Mêmes identifiants que les autres modules, pour que les personnages sonnent
# pareil d'un module à l'autre.
VOIX = {
    "enseignante": "mActWQg9kibLro6Z2ouY",   # 👩 féminine #1
    "feminin_2":   "WW0JfNPk5DgcQdM0d6X6",   # 👩 féminine #2
    "masculin_1":  "93nuHbke4dTER9x2pDwE",   # 👨 masculin #1
    "narrateur":   "IPgYtHTNLjC7Bq7IPHrm",   # 👨 narrateur
}

# Cinq locuteurs, quatre voix. Leïla parle à Micheline (défi 1) et à Gaétan
# (défi 3) : elles ne peuvent pas partager la leur. Micheline prend la voix
# « enseignante », ralentie à 0,85 — un avantage ici, puisqu'elle est la
# préposée au téléphone, celle qu'un élève de niveau 5 doit arriver à suivre.
# VOIX (le menu automatisé) et Pierre-Luc partagent `masculin_1` : ils ne se
# répondent jamais, le menu ne parlant qu'au début des défis 1 et 3.
VOIX_PERSO = {
    "LEÏLA":      "feminin_2",
    "MICHELINE":  "enseignante",
    "GAÉTAN":     "narrateur",
    "PIERRE-LUC": "masculin_1",
    "VOIX":       "masculin_1",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]

DIALOGUES = {
    "prep": [
        ("LEÏLA", "Pierre-Luc, tu as reçu ça, toi ? C'est arrivé dans ma boîte aux lettres hier."),
        ("PIERRE-LUC", "Fais voir… Oui, c'est la brochure de la Ville. Ils l'envoient à tout le monde deux fois par année."),
        ("LEÏLA", "Il y a trois bacs dessus. Trois. Chez moi, dans l'entrée, il y en a deux."),
        ("PIERRE-LUC", "Le gris, c'est les ordures. Le vert, c'est le recyclage. Et le brun, c'est les restes de table."),
        ("LEÏLA", "Les restes de table dans un bac ? Pour quoi faire ?"),
        ("PIERRE-LUC", "Ça devient du compost. C'est ramassé une fois par semaine, mais pas le même jour que le reste."),
        ("LEÏLA", "Et je le sais comment, le jour ?"),
        ("PIERRE-LUC", "Tu entres ton code postal sur le site de la Ville, et il te sort ton horaire. Ça s'appelle Info-collectes."),
        ("LEÏLA", "D'accord. Et ça, en bas de la page, « écocentre » ? Le mot ne me dit rien."),
        ("PIERRE-LUC", "C'est un endroit où tu apportes ce qui n'entre dans aucun bac. Un vieux micro-ondes, de la peinture, des branches."),
        ("LEÏLA", "C'est payant ?"),
        ("PIERRE-LUC", "Pas pour les résidents, dans la plupart des cas. Mais il faut que tu apportes une preuve que tu habites la ville."),
        ("LEÏLA", "Une preuve… comme quoi ?"),
        ("PIERRE-LUC", "Un permis de conduire, une facture à ton nom, un bail. Quelque chose avec ton adresse dessus."),
        ("LEÏLA", "Bon. Alors je garde le papier. Je pensais que c'était de la publicité, je l'avais mis avec les circulaires."),
        ("PIERRE-LUC", "Beaucoup de monde fait ça. Puis après, on se demande pourquoi le bac reste plein."),
    ],
    "t1": [
        ("VOIX", "Vous avez joint le service à la clientèle de la Ville. Pour le français, faites le un."),
        ("VOIX", "Pour un problème de collecte, faites le trois. Pour parler à un préposé, restez en ligne. Le temps d'attente est d'environ quatre minutes."),
        ("MICHELINE", "Bonjour, Micheline à l'appareil. Comment puis-je vous aider ?"),
        ("LEÏLA", "Bonjour. Je vous appelle parce que mon bac brun n'a pas été ramassé depuis deux semaines."),
        ("MICHELINE", "Deux semaines, d'accord. Vous êtes à quelle adresse ?"),
        ("LEÏLA", "Au 7412, rue De Normanville, appartement 3. À Villeray."),
        ("MICHELINE", "Et votre code postal, s'il vous plaît ?"),
        ("LEÏLA", "H2R 2V8. Je peux vous l'épeler : H, deux, R, deux, V, huit."),
        ("MICHELINE", "C'est bien noté. Alors, dans votre secteur, la collecte des résidus alimentaires se fait le mardi matin."),
        ("LEÏLA", "Le mardi. Est-ce que vous pouvez me dire à quelle heure il faut que je sorte le bac ?"),
        ("MICHELINE", "La veille au soir après vingt heures, ou avant sept heures le matin même."),
        ("LEÏLA", "Ah. Moi, je le sortais le mardi vers midi, en revenant de mon cours."),
        ("MICHELINE", "C'est ce qui explique tout, madame. Le camion était déjà passé."),
        ("LEÏLA", "Je voudrais savoir si le bac va être vidé cette semaine quand même."),
        ("MICHELINE", "J'ouvre une requête pour un ramassage supplémentaire. Le délai est de trois jours ouvrables."),
        ("LEÏLA", "Trois jours ouvrables. Et comment est-ce que je fais pour suivre ma demande ?"),
        ("MICHELINE", "Je vous donne un numéro de requête. Vous notez ? 24-118-7690."),
        ("LEÏLA", "Vingt-quatre, cent dix-huit, sept mille six cent quatre-vingt-dix. C'est bien ça ?"),
        ("MICHELINE", "C'est exact. Gardez-le : si personne ne passe d'ici vendredi, vous nous rappelez avec ce numéro-là."),
        ("LEÏLA", "Parfait. Merci beaucoup, madame. Bonne journée."),
    ],
    "t2": [
        ("LEÏLA", "Pierre-Luc, viens voir. J'ai trouvé la page dont tu m'avais parlé, mais je ne comprends pas la moitié."),
        ("PIERRE-LUC", "Montre. Ah oui, c'est la page de l'écocentre. Elle est longue, mais elle est bien faite."),
        ("LEÏLA", "Il y a deux colonnes. « Matières acceptées » et « Matières refusées ». Ça, ça va."),
        ("PIERRE-LUC", "Lis la deuxième. C'est celle qui cause des problèmes : les gens chargent leur auto et ils repartent avec."),
        ("LEÏLA", "« Matières refusées : les matières dangereuses non identifiées, les pneus de camion, les déchets qui viennent d'un chantier commercial. »"),
        ("PIERRE-LUC", "Ta peinture, elle est encore dans son pot d'origine ?"),
        ("LEÏLA", "Oui, avec l'étiquette."),
        ("PIERRE-LUC", "Alors elle passe. C'est ce que veut dire « non identifiées » : un bidon sans étiquette, ils ne le prennent pas."),
        ("LEÏLA", "D'accord. Et là, le petit encadré gris, en haut à droite ?"),
        ("PIERRE-LUC", "« Avant de vous déplacer. » C'est toujours l'encadré le plus important d'une page comme celle-là."),
        ("LEÏLA", "« Vérifiez le temps d'attente en direct. Apportez une preuve de résidence. Le nombre de visites gratuites est limité par année. »"),
        ("PIERRE-LUC", "Trois phrases, et elles t'évitent trois voyages pour rien."),
        ("LEÏLA", "Il y a un mot que je ne connais pas : « en vigueur ». « Tarifs en vigueur au 1er avril »."),
        ("PIERRE-LUC", "Ça veut dire : les prix qui s'appliquent aujourd'hui. Une loi, un tarif, un horaire : ce qui est en vigueur, c'est ce qui compte maintenant."),
        ("LEÏLA", "Donc si la page dit « en vigueur au 1er avril », les prix d'avant ne comptent plus."),
        ("PIERRE-LUC", "Voilà. Tu viens d'apprendre le mot le plus utile de toute la page."),
    ],
    "t3": [
        ("VOIX", "Numéro B quarante-sept, au comptoir trois."),
        ("GAÉTAN", "Bonjour ! Vous pouvez vous asseoir. Qu'est-ce qui vous amène ?"),
        ("LEÏLA", "Bonjour. Je viens pour ma carte de citoyenne. J'ai commencé la demande en ligne, mais elle n'a pas fonctionné."),
        ("GAÉTAN", "Elle n'a pas fonctionné comment ? Elle a été refusée, ou elle est restée bloquée ?"),
        ("LEÏLA", "Elle est restée bloquée à la dernière page. J'avais rempli tout le formulaire et il me redemandait mon adresse."),
        ("GAÉTAN", "Ah, ça arrive quand l'adresse est écrite autrement que dans notre système. Vous aviez mis « appartement » au long ?"),
        ("LEÏLA", "Oui, j'avais écrit « appartement 3 »."),
        ("GAÉTAN", "C'est ça. Le système veut « app. 3 ». Ce n'est pas votre faute, c'est une vraie faiblesse du formulaire."),
        ("LEÏLA", "Bon. Alors je peux la faire ici ?"),
        ("GAÉTAN", "Tout à fait. Il faut que vous me montriez deux pièces : une avec votre photo, et une avec votre adresse."),
        ("LEÏLA", "J'ai mon permis de conduire, et j'ai apporté mon bail."),
        ("GAÉTAN", "Le permis, parfait. Le bail… voyons voir. Il est à quel nom ?"),
        ("LEÏLA", "Au mien et à celui de mon fils."),
        ("GAÉTAN", "Alors il fait la job. Ce qui manque parfois, c'est une facture trop vieille — il faut qu'elle date de moins de trois mois."),
        ("LEÏLA", "Je note. Combien de temps ça prend, après ?"),
        ("GAÉTAN", "La carte est imprimée pendant que vous attendez. Vous repartez avec dans dix minutes."),
        ("LEÏLA", "Dix minutes ! J'ai passé trois soirées sur le site Web."),
        ("GAÉTAN", "Vous n'êtes pas la première à me dire ça. La prochaine fois, appelez-nous avant : on vous dit tout de suite si ça se règle en ligne ou non."),
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
                json=enrichir({"text": texte, "model_id": "eleven_multilingual_v2",
                      "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}),
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

    print(f"🔊 module-n5-services — {len(taches)} extraits "
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
