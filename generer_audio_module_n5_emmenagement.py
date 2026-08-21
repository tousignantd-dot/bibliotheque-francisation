#!/usr/bin/env python3
"""
Générateur d'audio — module « Emménager dans un nouveau logement » (module-n5-emmenagement).
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

puis coller le résultat dans sons_module_n5_emmenagement.json, à côté de ce script.

La deuxième boucle n'est pas un doublon : dans les exercices à cartes
(cards/listen), le bouton d'écoute reçoit son gestionnaire en JS et non par un
attribut onclick — le premier sélecteur ne le voit donc pas.

Usage :  python3 generer_audio_module_n5_emmenagement.py [--force] [--only prefixe,...]
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
SORTIE = RACINE / "assets/interactive/module-n5-emmenagement"
MANIFESTE = RACINE / "sons_module_n5_emmenagement.json"

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

# Quatre locuteurs, trois voix. Amadou et Thérèse se répondent d'un bout à
# l'autre du module ; Patricia et Claudine, elles, ne se croisent jamais — la
# répartitrice du camion et l'agente d'Hydro-Québec n'apparaissent pas dans le
# même dialogue — et peuvent donc partager une voix.
# Thérèse prend la voix « enseignante », ralentie à 0,85 : c'est une voisine de
# soixante-douze ans qui explique l'immeuble, et la lenteur lui va.
VOIX_PERSO = {
    "AMADOU":   "masculin_1",
    "THÉRÈSE":  "enseignante",
    "PATRICIA": "feminin_2",
    "CLAUDINE": "feminin_2",
}

# Voix des mots isolés et des mini-leçons : celle de l'enseignante.
VOIX_MOTS = VOIX["enseignante"]

DIALOGUES = {
    "prep": [
        ("AMADOU", "Bonjour, madame. Excusez-moi, je bloque l'escalier avec ma boîte."),
        ("THÉRÈSE", "Prenez votre temps, je ne suis pas pressée. Vous êtes le nouveau du 4 ?"),
        ("AMADOU", "Oui. Amadou Sow. Monsieur Rondeau vient de me remettre les clés, il y a dix minutes."),
        ("THÉRÈSE", "Thérèse Guillemette, le 3, juste en dessous de vous. Ça fait vingt-six ans que je suis dans l'immeuble."),
        ("AMADOU", "Vingt-six ans. Vous devez tout savoir, alors."),
        ("THÉRÈSE", "À peu près, oui. Vous avez fait le tour du logement avec lui, avant de signer le papier ?"),
        ("AMADOU", "On a commencé. Il m'a montré la cuisine, la chambre, le balcon. On n'a pas fini."),
        ("THÉRÈSE", "Finissez-le, et écrivez tout. C'est ça, l'état des lieux : la liste de ce qui est déjà abîmé quand vous entrez."),
        ("AMADOU", "Il y a une égratignure sur le plancher du salon, et la porte de l'armoire ferme mal."),
        ("THÉRÈSE", "Notez-les. Prenez des photos aussi. Sinon, dans trois ans, ce sera vous qui aurez fait l'égratignure."),
        ("AMADOU", "Je n'y avais pas pensé. Merci, madame Guillemette."),
        ("THÉRÈSE", "Appelez-moi Thérèse. Et le vrai déménagement, c'est quand ?"),
        ("AMADOU", "Le premier juillet. Il faut encore que je trouve un camion."),
        ("THÉRÈSE", "Le premier juillet, tout le monde déménage en même temps au Québec. Téléphonez cette semaine, pas en juin."),
    ],
    "t1": [
        ("PATRICIA", "Déménagement Cap-Rouge, bonjour."),
        ("AMADOU", "Bonjour. J'appelle pour faire déménager mes affaires le premier juillet. Est-ce qu'il vous reste de la place ?"),
        ("PATRICIA", "Le premier juillet, il me reste des camions le matin seulement. Vous partez d'où et vous allez où ?"),
        ("AMADOU", "Je pars d'un trois et demie à Beauport et je m'en vais rue des Peupliers, à Limoilou."),
        ("PATRICIA", "D'accord. Vous êtes à quel étage, des deux côtés ?"),
        ("AMADOU", "Au rez-de-chaussée à Beauport, et au deuxième rue des Peupliers. Il n'y a pas d'ascenseur, et l'escalier est en dehors."),
        ("PATRICIA", "Bon à savoir. Un escalier extérieur qui tourne, ça ralentit toujours un peu. Combien de boîtes, à peu près ?"),
        ("AMADOU", "Une quinzaine de boîtes, un divan, un lit, une table et quatre chaises."),
        ("PATRICIA", "C'est raisonnable. Je vous mets deux hommes et un camion : c'est cent quarante-cinq dollars de l'heure, minimum trois heures."),
        ("AMADOU", "Cent quarante-cinq de l'heure. Est-ce qu'il y a autre chose qui s'ajoute ?"),
        ("PATRICIA", "Oui, une heure de déplacement. C'est le temps que le camion met pour sortir du garage et pour y revenir."),
        ("AMADOU", "Donc, si ça prend quatre heures, je paie cinq heures. Ça fait sept cent vingt-cinq dollars."),
        ("PATRICIA", "C'est exactement ça. Et si vous voulez, je vous envoie un troisième homme à quarante-cinq de l'heure : avec votre escalier, il se paie tout seul."),
        ("AMADOU", "Je vais y penser. Est-ce que mes affaires sont assurées ?"),
        ("PATRICIA", "L'assurance de base est comprise. Pour du fragile, il y a une protection complète à quarante-cinq dollars."),
        ("AMADOU", "Et pour réserver, vous me demandez quoi ?"),
        ("PATRICIA", "Un dépôt de cent dollars. Je vous le rembourse si vous annulez sept jours d'avance."),
        ("AMADOU", "Parfait. Le premier juillet, huit heures, alors. Je vous rappelle demain avec ma carte."),
    ],
    "t1b": [
        ("PATRICIA", "On commence par quoi ? Les meubles ou les boîtes ?"),
        ("AMADOU", "Par les meubles, s'il vous plaît. Après, on remplira les trous avec les boîtes."),
        ("PATRICIA", "D'accord. Le divan, on le monte tout de suite ?"),
        ("AMADOU", "Montez-le, oui, mais faites attention au coin de l'escalier. Il tourne serré."),
        ("PATRICIA", "On met des couvertures dessus. Et le matelas, vous le voulez où ?"),
        ("AMADOU", "Dans la chambre du fond, celle qui donne sur la ruelle. Ne le posez pas dans le salon, on ne pourra plus passer."),
        ("AMADOU", "Cette boîte-ci, avec le point rouge, c'est la vaisselle. Ne la mettez pas en dessous des autres."),
        ("PATRICIA", "Les points rouges, on les garde sur le dessus. Vous avez bien fait de les marquer."),
        ("AMADOU", "Celles-là aussi, dans la cuisine. Ce sont les casseroles et le petit four."),
        ("PATRICIA", "Parfait. Et la table de la salle à manger, on la démonte ou on la passe entière ?"),
        ("AMADOU", "Démontez-la. Elle ne passera jamais dans la porte du deuxième."),
        ("PATRICIA", "Vous avez raison. Donnez-moi une clé anglaise et je m'en occupe."),
        ("AMADOU", "Tenez. Et si mon voisin d'en bas sort dans l'escalier, laissez-le passer avant de monter."),
        ("PATRICIA", "Ça, on le fait toujours. C'est le monde de l'immeuble qui reste après nous."),
    ],
    "t2": [
        ("CLAUDINE", "Service à la clientèle, bonjour. Comment puis-je vous aider ?"),
        ("AMADOU", "Bonjour. Je viens d'emménager et j'aimerais ouvrir un compte d'électricité à mon nom."),
        ("CLAUDINE", "Certainement. Vous emménagez à quelle adresse, et à partir de quelle date ?"),
        ("AMADOU", "Au mille deux cent quatre-vingt-sept, rue des Peupliers, appartement 4, à Québec. À partir du premier juillet."),
        ("CLAUDINE", "Je vous répète l'adresse : mille deux cent quatre-vingt-sept, rue des Peupliers, appartement 4. C'est bien ça ?"),
        ("AMADOU", "C'est bien ça."),
        ("CLAUDINE", "Il me faut aussi le relevé du compteur le jour de votre entrée. Le compteur est habituellement au sous-sol."),
        ("AMADOU", "Je le trouverai. Est-ce que je dois faire quelque chose pour mon ancienne adresse ?"),
        ("CLAUDINE", "Oui, et c'est le même appel : je ferme votre compte de Beauport le trente juin, à minuit."),
        ("AMADOU", "Donc je n'ai pas deux comptes ouverts en même temps ?"),
        ("CLAUDINE", "Non. L'ancien se ferme, le nouveau s'ouvre, et vous ne payez jamais l'électricité de quelqu'un d'autre."),
        ("AMADOU", "Ça me rassure. Et pour mon courrier ? Ce n'est pas vous, je sais, mais je suis un peu perdu dans ma liste."),
        ("CLAUDINE", "Ce n'est pas nous, non. Postes Canada offre un service de réacheminement : votre courrier vous suit pendant quelques mois."),
        ("AMADOU", "Il faut que je prévienne bien du monde : la banque, l'école de mon garçon, la SAAQ, la RAMQ."),
        ("CLAUDINE", "Faites-en une liste et cochez au fur et à mesure. Ceux qui oublient la RAMQ s'en aperçoivent chez le médecin."),
        ("AMADOU", "Je note. Merci beaucoup, madame."),
    ],
    "t3": [
        ("AMADOU", "Thérèse, bonjour. Je voulais m'excuser pour hier. On a fait du bruit jusqu'à neuf heures et demie."),
        ("THÉRÈSE", "J'ai entendu, oui. Mais c'était un déménagement, ce n'était pas un party. Ce n'est pas pareil."),
        ("AMADOU", "Le camion est arrivé en retard, et après, il pleuvait. On finissait de monter les boîtes pendant que mon garçon dormait dans l'auto."),
        ("THÉRÈSE", "Pauvre petit. Vous savez, quand je suis arrivée ici, en quatre-vingt-dix-huit, mon mari a échappé la laveuse dans l'escalier."),
        ("AMADOU", "Dans l'escalier ?"),
        ("THÉRÈSE", "Dans l'escalier. Elle est descendue toute seule jusqu'en bas. Tout le monde riait, sauf lui."),
        ("AMADOU", "Bon, alors je me sens moins mal. Je voulais vous demander : la salle de lavage, ça fonctionne comment ?"),
        ("THÉRÈSE", "Au sous-sol, à droite. Deux dollars la brassée, en vingt-cinq sous. Personne ne réserve, mais on ne laisse pas son linge dedans."),
        ("AMADOU", "Compris. Et les poubelles ? J'ai vu un bac brun en avant."),
        ("THÉRÈSE", "Le bac brun, c'est le compost : les restes de table, les pelures. Il se ramasse le mardi matin. Le bac bleu, le recyclage, une semaine sur deux."),
        ("AMADOU", "Je vais écrire ça sur le frigo. Et l'hiver, pour le stationnement ?"),
        ("THÉRÈSE", "Le déneigement se fait tôt le matin. Quand la ville affiche l'interdiction, il faut déplacer les autos avant sept heures, sinon elles sont remorquées."),
        ("AMADOU", "Remorquées. D'accord, ça, je ne l'oublierai pas."),
        ("THÉRÈSE", "Vous allez voir, on s'habitue. Et si vous avez besoin d'une clé anglaise ou d'un tournevis, cognez chez moi."),
    ],
    "t3b": [
        ("THÉRÈSE", "Amadou, une petite question. Je fais du café dimanche après-midi, avec la voisine du 1. Vous viendriez ?"),
        ("AMADOU", "C'est gentil de me le proposer. Dimanche après-midi, par exemple, je travaille : je suis à l'hôpital jusqu'à sept heures."),
        ("THÉRÈSE", "Ah, vous travaillez le dimanche. Ce n'est pas facile, ça."),
        ("AMADOU", "Une fin de semaine sur deux. Mais dimanche prochain, je suis libre, et là, j'accepterais avec plaisir."),
        ("THÉRÈSE", "Parfait, on dit dimanche prochain. Deux heures ? Vous amènerez votre garçon si vous voulez."),
        ("AMADOU", "Il va être content. Est-ce que j'apporte quelque chose ?"),
        ("THÉRÈSE", "Rien du tout. Vous venez de déménager, vous ne trouvez même pas vos tasses."),
        ("AMADOU", "C'est vrai. Elles sont encore dans une boîte, quelque part."),
        ("THÉRÈSE", "Alors venez les mains vides. Et si jamais ça ne marche pas, vous me le direz, ce n'est pas grave."),
        ("AMADOU", "Non, non, dimanche prochain, c'est noté. Deux heures, chez vous, au 3."),
        ("THÉRÈSE", "Au 3. Bienvenue dans l'immeuble, monsieur Sow."),
        ("AMADOU", "Amadou. Merci, Thérèse."),
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

    print(f"🔊 module-n5-emmenagement — {len(taches)} extraits "
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
