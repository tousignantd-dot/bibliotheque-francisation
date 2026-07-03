#!/usr/bin/env python3
"""
Générateur d'audio pour les dialogues — ElevenLabs
Exécute ce script et rentre ta clé API quand demandé.
"""

import os
import json
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ requests n'est pas installé. Installe-le :")
    print("   pip install requests")
    sys.exit(1)

# ── VOICES ────────────────────────────────────────────────────────────
VOICES = {
    "enseignante": "K7gx0ylJdff0yjM2uVQS",      # 👩 Féminine #1
    "feminin_2": "WW0JfNPk5DgcQdM0d6X6",        # 👩 Féminine #2
    "masculin_1": "93nuHbke4dTER9x2pDwE",       # 👨 Masculin #1
    "narrateur": "IPgYtHTNLjC7Bq7IPHrm",        # 👨 Narrateur
}

VOICE_ASSOC = {
    "AMARA": "feminin_2",
    "JULIE": "feminin_2",
    "FATIMA": "feminin_2",
    "LA RÉCEPTIONNISTE": "enseignante",
    "M. BÉLANGER": "masculin_1",
    "LE DOCTEUR": "masculin_1",
    "LEILA": "feminin_2",
}

# ── DIALOGUES ─────────────────────────────────────────────────────────
DIALOGUES = {
    "je-demenage/dialogue-1": {
        "title": "Je déménage - Dialogue 1",
        "lines": [
            ("AMARA", "Bonjour, j'appelle pour l'appartement à louer sur la rue Fleury. Est-ce qu'il est encore disponible ?"),
            ("M. BÉLANGER", "Oui, tout à fait ! C'est un 4½, meublé, chauffé et éclairé. L'électricité est comprise dans le loyer."),
            ("AMARA", "Combien de chambres est-ce qu'il y a ?"),
            ("M. BÉLANGER", "Il y a une chambre, un salon, une cuisine et une salle de bain. Il y a aussi un grand balcon."),
            ("AMARA", "Est-ce qu'il y a une laveuse et une sécheuse ?"),
            ("M. BÉLANGER", "Non, il n'y en a pas, mais il y a une buanderie dans l'immeuble."),
            ("AMARA", "Parfait. Quel est le montant du loyer ?"),
            ("M. BÉLANGER", "Le loyer est de neuf cent cinquante dollars par mois. Il faut signer un bail d'un an."),
            ("AMARA", "Est-ce que je peux visiter l'appartement cette semaine ?"),
            ("M. BÉLANGER", "Bien sûr ! Êtes-vous libre jeudi à dix-huit heures ?"),
            ("AMARA", "Oui, parfait. Merci beaucoup, à jeudi !"),
        ]
    },
    "je-demenage/dialogue-2": {
        "title": "Je déménage - Dialogue 2",
        "lines": [
            ("M. BÉLANGER", "Bienvenue ! Entrez, je vous en prie. Voici le salon."),
            ("AMARA", "Oh, c'est plus grand que ce que j'imaginais ! Et le salon est très ensoleillé."),
            ("M. BÉLANGER", "Oui, les fenêtres donnent sur le sud. La cuisine a été rénovée l'année passée."),
            ("AMARA", "Elle est vraiment belle. Est-ce que le stationnement est compris dans le loyer ?"),
            ("M. BÉLANGER", "Non, le stationnement coûte cinquante dollars de plus par mois."),
            ("AMARA", "Je vois… Est-ce que le prix du loyer est négociable ?"),
            ("M. BÉLANGER", "Hum… Je ne peux pas baisser le loyer, mais je peux vous offrir le stationnement à moitié prix la première année."),
            ("AMARA", "C'est une bonne offre ! Je vais réfléchir et je vous rappelle demain."),
        ]
    },
    "je-demenage/dialogue-3": {
        "title": "Je déménage - Dialogue 3",
        "lines": [
            ("AMARA", "Allô Julie ! Je t'appelle parce que j'organise une pendaison de crémaillère pour célébrer mon nouvel appartement !"),
            ("JULIE", "Quelle bonne idée ! C'est quand ?"),
            ("AMARA", "Samedi soir, à dix-neuf heures. J'invite dix personnes."),
            ("JULIE", "Super ! Est-ce que je peux apporter quelque chose ? Un dessert, peut-être ?"),
            ("AMARA", "Oui, avec plaisir ! Chacun apporte son plat préféré. Pas besoin de cadeau pour la maison."),
            ("JULIE", "Parfait. Tu veux de l'aide pour préparer ?"),
            ("AMARA", "Oui ! Est-ce que tu peux venir m'aider à décorer vendredi soir ?"),
            ("JULIE", "Bien sûr ! Je les adore, tes soirées. À vendredi !"),
        ]
    },
    "parler-de-sa-sante/dialogue-1": {
        "title": "Parler de sa santé - Dialogue 1",
        "lines": [
            ("FATIMA", "Bonjour, j'aimerais prendre un rendez-vous. Je ne me sens pas bien depuis trois jours."),
            ("LA RÉCEPTIONNISTE", "Bien sûr. Qu'est-ce qui ne va pas exactement ?"),
            ("FATIMA", "J'ai mal à la gorge et j'ai de la fièvre. J'ai aussi beaucoup de difficulté à avaler."),
            ("LA RÉCEPTIONNISTE", "Est-ce que vous toussez ?"),
            ("FATIMA", "Oui, un peu. Et je suis très fatiguée."),
            ("LA RÉCEPTIONNISTE", "D'accord. Est-ce que vous avez déjà consulté le docteur Tremblay ?"),
            ("FATIMA", "Non, c'est la première fois. Est-ce qu'il reste de la place cette semaine ?"),
            ("LA RÉCEPTIONNISTE", "Oui. Il y a une place demain, jeudi, à quatorze heures. Est-ce que ça vous convient ?"),
            ("FATIMA", "Parfait ! Est-ce que je dois apporter ma carte d'assurance maladie ?"),
            ("LA RÉCEPTIONNISTE", "Oui, s'il vous plaît. À demain, madame !"),
        ]
    },
    "parler-de-sa-sante/dialogue-2": {
        "title": "Parler de sa santé - Dialogue 2",
        "lines": [
            ("LE DOCTEUR", "Bonjour Fatima. Alors, qu'est-ce qui vous amène aujourd'hui ?"),
            ("FATIMA", "J'ai très mal à la gorge et j'ai de la difficulté à avaler depuis trois jours."),
            ("LE DOCTEUR", "Est-ce que vous avez de la fièvre ?"),
            ("FATIMA", "Oui, un peu. Et je suis fatiguée à cause de la fièvre. Je dors mal la nuit."),
            ("LE DOCTEUR", "Je vais examiner votre gorge. Ouvrez grand la bouche, s'il vous plaît… Votre gorge est très rouge."),
            ("FATIMA", "Est-ce que c'est grave, docteur ?"),
            ("LE DOCTEUR", "Non, ce n'est pas grave. C'est une pharyngite. Ce n'est pas une infection bactérienne."),
            ("FATIMA", "Est-ce que j'ai besoin d'un antibiotique ?"),
            ("LE DOCTEUR", "Non, l'antibiotique est inutile parce que c'est un virus. Reposez-vous et buvez beaucoup d'eau."),
        ]
    },
    "parler-de-sa-sante/dialogue-3": {
        "title": "Parler de sa santé - Dialogue 3",
        "lines": [
            ("LE DOCTEUR", "Pour soulager votre gorge, prenez un médicament contre la douleur, comme l'acétaminophène."),
            ("FATIMA", "Est-ce que j'ai besoin d'une ordonnance ?"),
            ("LE DOCTEUR", "Non, c'est un médicament en vente libre. Vous pouvez l'acheter directement à la pharmacie."),
            ("FATIMA", "D'accord. Est-ce que je peux prendre des vitamines aussi ?"),
            ("LE DOCTEUR", "Oui, mais attention : ne prenez jamais un médicament périmé. Vérifiez toujours la date."),
            ("FATIMA", "Combien de fois par jour dois-je prendre le médicament ?"),
            ("LE DOCTEUR", "Trois fois par jour, après les repas. Si la fièvre continue plus de cinq jours, revenez me voir."),
            ("FATIMA", "Merci beaucoup, docteur. Je vais suivre vos conseils."),
        ]
    },
    "parler-de-sa-sante/dialogue-4": {
        "title": "Parler de sa santé - Dialogue 4",
        "lines": [
            ("FATIMA", "Julie, tu as la voix bizarre ! Qu'est-ce que tu as ?"),
            ("JULIE", "J'ai une laryngite. J'ai perdu la voix à cause du concert de samedi : j'ai trop crié !"),
            ("FATIMA", "Oh non ! Est-ce que tu prends des antibiotiques ?"),
            ("JULIE", "Non, l'antibiotique est inutile parce que c'est un virus. Le médecin dit de reposer ma voix."),
            ("FATIMA", "Tu dois boire beaucoup d'eau et ne pas chuchoter. Chuchoter fatigue les cordes vocales."),
            ("JULIE", "Je sais ! Grâce à tes conseils, je vais guérir plus vite. Merci, Fatima !"),
        ]
    },
}

# ── GÉNÉRATION ────────────────────────────────────────────────────────
def generate_audio(api_key, text, voice_id, output_path):
    """Génère un fichier audio avec ElevenLabs."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75,
        }
    }

    try:
        response = requests.post(url, json=payload, headers=headers, timeout=30)

        if response.status_code != 200:
            print(f"   ❌ Erreur {response.status_code}: {response.text[:200]}")
            return False

        with open(output_path, "wb") as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"   ❌ Erreur : {e}")
        return False

def main():
    print("🎙️  Générateur d'audio pour les dialogues\n")

    # Lire la clé API depuis la variable d'environnement
    api_key = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not api_key:
        # Demander comme fallback
        api_key = input("Colle ta clé ElevenLabs : ").strip()
        if not api_key:
            print("❌ Clé API requise")
            sys.exit(1)

    base_dir = Path("/Users/danieltousignant/Claude/bibliotheque-francisation/assets/interactive")

    total = 0
    success = 0

    for dial_id, dial_data in DIALOGUES.items():
        print(f"\n📖 {dial_data['title']}")

        dir_path = base_dir / dial_id
        dir_path.mkdir(parents=True, exist_ok=True)

        for i, (character, text) in enumerate(dial_data["lines"], 1):
            voice_name = VOICE_ASSOC.get(character, "feminin_2")
            voice_id = VOICES[voice_name]

            filename = f"line_{i:02d}_{character.lower().replace(' ', '_')}.mp3"
            output_path = dir_path / filename

            print(f"  {i:2d}. {character[:20]:20s} → ", end="", flush=True)
            total += 1

            if generate_audio(api_key, text, voice_id, output_path):
                print(f"✓ {filename}")
                success += 1
            else:
                print(f"✗ {filename}")

    print(f"\n{'='*60}")
    print(f"✅ {success}/{total} fichiers générés")

    if success == total:
        print("🎉 Tous les fichiers audio sont prêts !")
    else:
        print(f"⚠️  {total - success} fichier(s) manquant(s)")

if __name__ == "__main__":
    main()
