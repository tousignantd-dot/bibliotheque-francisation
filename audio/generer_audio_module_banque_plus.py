#!/usr/bin/env python3
"""
Générateur d'audio — mini-leçons du module « Besoin d'un compte bancaire ? ».

fileId → texte lu ; doit correspondre aux appels playWord() générés par
plAudioId() dans le HTML. Pour régénérer cette liste après une modification de
l'objet PLUS : ouvrir le module dans le navigateur et lancer plAudioManifest()
dans la console — elle renvoie exactement ce dictionnaire, prêt à coller.
"""
import os, sys, time
from pathlib import Path

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent / 'build'))

MODULE_SLUG = "module-banque"
VOICE = "mActWQg9kibLro6Z2ouY"        # ← même voix que les mots isolés du module

CLIPS = {
    # Produit par plAudioManifest() dans la console du module.
    "plus_prPhon_ana1": "le dépôt",
    "plus_prPhon_ana2": "le chèque",
    "plus_prPhon_lab3_fermeprem": "l'épargne",
    "plus_prPhon_lab3_fermedern": "il faut vérifier",
    "plus_prPhon_lab3_ouvertprem": "le chèque",
    "plus_prPhon_lab3_ouvertdern": "le guichet",
    "plus_prPhon_ex4_0": "le dépôt",
    "plus_prPhon_ex4_1": "l'épargne",
    "plus_prPhon_ex4_2": "le chéquier",
    "plus_prPhon_ex4_3": "il faut vérifier",
    "plus_prPhon_ex4_4": "le chèque",
    "plus_prPhon_ex4_5": "la caisse",
    "plus_prPhon_ex4_6": "le guichet",
    "plus_prPhon_ex4_7": "le billet",
    "plus_t1cause_ana1": "J'ouvre un compte parce que mon employeur le demande.",
    "plus_t1cause_lab2_p": "Nour change de forfait parce que les frais montent.",
    "plus_t1cause_lab2_a": "Nour change de forfait à cause des frais.",
    "plus_t1cause_lab2_c": "Nour change de forfait, car les frais montent.",
    "plus_t1cause_ex3_0": "Je viens parce que mon employeur exige un spécimen.",
    "plus_t1cause_ex3_1": "Elle paie des frais à cause de son découvert.",
    "plus_t1cause_ex3_2": "Il prend l'illimité, car il fait beaucoup d'opérations.",
    "plus_t1cause_ex3_3": "Le comptoir est plein parce que c'est jeudi.",
    "plus_t1cause_ex3_4": "Le virement a échoué à cause d'une erreur d'adresse.",
    "plus_t1cause_ex3_5": "Vérifiez le solde, car les frais s'ajoutent chaque jour.",
    "plus_t1quest_ana1": "Est-ce que le dépôt direct est gratuit ?",
    "plus_t1quest_ana2": "Avez-vous une preuve d'adresse ?",
    "plus_t1quest_lab3_en": "Est-ce que le forfait coûte cher ?",
    "plus_t1quest_lab3_ec": "Combien est-ce que le forfait coûte ?",
    "plus_t1quest_lab3_in": "Le forfait coûte-t-il cher ?",
    "plus_t1quest_lab3_ic": "Combien coûte le forfait ?",
    "plus_t1quest_lab3_on": "Le forfait coûte cher ?",
    "plus_t1quest_lab3_oc": "Le forfait coûte combien ?",
    "plus_t1quest_ex4_0": "Est-ce que vous avez deux pièces d'identité ?",
    "plus_t1quest_ex4_1": "Quels papiers faut-il apporter ?",
    "plus_t1quest_ex4_2": "Le virement est-il gratuit ?",
    "plus_t1quest_ex4_3": "Combien d'opérations sont incluses ?",
    "plus_t1quest_ex4_4": "Vous fermez à quelle heure ?",
    "plus_t1quest_ex4_5": "Qu'est-ce qui arrive si je suis à découvert ?",
    "plus_t2present_ana1": "nous déposons",
    "plus_t2present_lab2_jed": "je dépose",
    "plus_t2present_lab2_jea": "j'ai",
    "plus_t2present_lab2_jee": "je suis",
    "plus_t2present_lab2_jeo": "je peux",
    "plus_t2present_lab2_nousd": "nous déposons",
    "plus_t2present_lab2_nousa": "nous avons",
    "plus_t2present_lab2_nouse": "nous sommes",
    "plus_t2present_lab2_nouso": "nous pouvons",
    "plus_t2present_lab2_ilsd": "ils déposent",
    "plus_t2present_lab2_ilsa": "ils ont",
    "plus_t2present_lab2_ilse": "ils sont",
    "plus_t2present_lab2_ilso": "ils peuvent",
    "plus_t2present_ex3_0": "je dépose un chèque",
    "plus_t2present_ex3_1": "nous déposons un chèque",
    "plus_t2present_ex3_2": "ils déposent un chèque",
    "plus_t2present_ex3_3": "vous avez deux pièces d'identité",
    "plus_t2present_ex3_4": "nous sommes au comptoir",
    "plus_t2present_ex3_5": "vous pouvez retirer au guichet",
    "plus_t2neg_ana1": "je ne paie pas de frais",
    "plus_t2neg_lab2_pasc": "je ne paie pas de frais",
    "plus_t2neg_lab2_pasv": "je n'utilise pas ma carte",
    "plus_t2neg_lab2_plusc": "je ne paie plus de frais",
    "plus_t2neg_lab2_plusv": "je n'utilise plus ma carte",
    "plus_t2neg_lab2_jamaisc": "je ne paie jamais de frais",
    "plus_t2neg_lab2_jamaisv": "je n'utilise jamais ma carte",
    "plus_t2neg_ex3_0": "Je ne paie pas de frais mensuels.",
    "plus_t2neg_ex3_1": "Il n'a pas de compte épargne.",
    "plus_t2neg_ex3_2": "Elle ne note jamais son NIP.",
    "plus_t2neg_ex3_3": "Nous n'utilisons plus de chèques.",
    "plus_t2neg_ex3_4": "La caisse ne demande jamais votre NIP au téléphone.",
    "plus_t2neg_ex3_5": "Je n'ai pas reçu mon relevé.",
    "plus_t3plur_ana1": "des comptes courants",
    "plus_t3plur_lab2_sc": "un compte courant",
    "plus_t3plur_lab2_pc": "des comptes courants",
    "plus_t3plur_lab2_si": "un virement international",
    "plus_t3plur_lab2_pi": "des virements internationaux",
    "plus_t3plur_lab2_sb": "un nouveau bureau",
    "plus_t3plur_lab2_pb": "des nouveaux bureaux",
    "plus_t3plur_lab2_st": "un taux avantageux",
    "plus_t3plur_lab2_pt": "des taux avantageux",
    "plus_t3plur_ex3_0": "des comptes courants",
    "plus_t3plur_ex3_1": "des virements internationaux",
    "plus_t3plur_ex3_2": "des nouveaux bureaux",
    "plus_t3plur_ex3_3": "des taux avantageux",
    "plus_t3plur_ex3_4": "des frais mensuels",
    "plus_t3plur_ex3_5": "des relevés de compte",
    "plus_t3devoir_ana1": "vous devez signer",
    "plus_t3devoir_ana2": "il faut vérifier",
    "plus_t3devoir_lab3_jes": "je dois signer le formulaire",
    "plus_t3devoir_lab3_jev": "je dois vérifier le solde",
    "plus_t3devoir_lab3_vouss": "vous devez signer le formulaire",
    "plus_t3devoir_lab3_vousv": "vous devez vérifier le solde",
    "plus_t3devoir_lab3_ons": "il faut signer le formulaire",
    "plus_t3devoir_lab3_onv": "il faut vérifier le solde",
    "plus_t3devoir_ex4_0": "Vous devez signer ici.",
    "plus_t3devoir_ex4_1": "Je dois apporter deux pièces d'identité.",
    "plus_t3devoir_ex4_2": "Il faut cacher le clavier au guichet.",
    "plus_t3devoir_ex4_3": "Elle doit choisir un NIP de quatre chiffres.",
    "plus_t3devoir_ex4_4": "Il faut appeler la caisse tout de suite.",
    "plus_t3devoir_ex4_5": "Nous devons garder mille dollars dans le compte.",
}

# Voir phase2-audio.md : préférer un déterminant (le/la) à une réorthographie
# phonétique pour un mot qui se lit mal.
#
# Les 25 extraits les plus courts portent déjà un déterminant ou un pronom
# sujet — « le dépôt », « nous déposons » — donc rien à faire pour eux. Restent
# les formes de deux syllabes du laboratoire de conjugaison (« j'ai », « ils
# ont ») : trop maigres pour que le moteur ait un vrai indice de langue. On les
# fait précéder du pronom d'insistance, qui est du français ordinaire et laisse
# la forme conjuguée **en fin de phrase**, là où l'élève doit l'entendre.
# Le texte affiché dans le panneau, lui, ne change pas.
TEXT_OVERRIDES = {
    "plus_t2present_lab2_jed":  "moi, je dépose",
    "plus_t2present_lab2_jea":  "moi, j'ai",
    "plus_t2present_lab2_jee":  "moi, je suis",
    "plus_t2present_lab2_jeo":  "moi, je peux",
    "plus_t2present_lab2_ilsd": "eux, ils déposent",
    "plus_t2present_lab2_ilsa": "eux, ils ont",
    "plus_t2present_lab2_ilse": "eux, ils sont",
    "plus_t2present_lab2_ilso": "eux, ils peuvent",
}


# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


def generate(api_key, text, path):
    return parle_compat(api_key, text, VOICE, path)
def main():
    print(f"🔊 Mini-leçons « Ouvrir la mini-leçon » — {len(CLIPS)} extraits\n")
    api_key = os.environ.get("AZURE_SPEECH_KEY", "").strip()
    if not api_key:
        # Repli sur `~/Claude/.env`, où vit la clé Azure avec les autres clés
        # de génération. Sans ça, ces générateurs de forme ancienne — qui ne
        # lisaient que l'environnement — échouaient dès qu'ils étaient lancés
        # autrement qu'à la main dans un shell où la clé était exportée.
        _env = Path.home() / "Claude" / ".env"
        if _env.exists():
            for _l in _env.read_text(encoding="utf-8").splitlines():
                if _l.strip().startswith("AZURE_SPEECH_KEY="):
                    api_key = _l.split("=", 1)[1].strip().strip("\"'")
    if not api_key:
        print("❌ AZURE_SPEECH_KEY absente"); sys.exit(1)

    out = Path(__file__).resolve().parent / f"assets/interactive/{MODULE_SLUG}/sons"
    out.mkdir(parents=True, exist_ok=True)

    # --force régénère tout ; --only id1,id2 cible des extraits précis ;
    # sans option, on saute ce qui existe déjà (relance après coupure sans
    # repayer les extraits déjà faits).
    force = "--force" in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--only" and i + 1 < len(sys.argv):
            only = set(x.strip() for x in sys.argv[i + 1].split(",") if x.strip())

    ok = skip = fail = 0
    for file_id, text in CLIPS.items():
        if only and file_id not in only:
            continue
        dest = out / f"{file_id}.mp3"
        if dest.exists() and not force and not only:
            skip += 1
            continue
        spoken = TEXT_OVERRIDES.get(file_id, text)
        print(f"  {file_id:26s} « {spoken[:44]} » → ", end="", flush=True)
        if generate(api_key, spoken, dest):
            print("✓"); ok += 1
        else:
            print("✗"); fail += 1
        time.sleep(0.35)   # ne pas saturer l'API

    print(f"\n✅ {ok} générés · {skip} déjà présents · {fail} en échec")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
