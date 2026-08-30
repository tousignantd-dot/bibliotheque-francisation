#!/usr/bin/env python3
"""Faire passer les générateurs d'audio d'ElevenLabs à Azure, mécaniquement.

    python3 build/migrer_azure.py --essai              # ce qui serait changé, sans rien écrire
    python3 build/migrer_azure.py audio/generer_audio_module_n1_presenter.py
    python3 build/migrer_azure.py --tous

Ce que la migration change, et ce qu'elle ne touche pas
------------------------------------------------------
Les 110 générateurs sont bâtis sur le même patron : une table `VOIX` de quatre
identifiants ElevenLabs, une fonction locale

    parle(cle, texte, voix, chemin, avant=None, apres=None) -> bool

et un `main()` qui parcourt dialogues et manifeste. **Seule la fonction change.**
La lecture des dialogues, les identifiants de fichiers, les `TEXT_OVERRIDES`,
l'ordre des extraits — tout ce qui tient au contenu reste intact, parce que
c'est là que vit le travail éditorial et qu'une réécriture automatique y ferait
plus de mal que de bien.

Trois lignes disparaissent, et chacune pour une raison :

* `from voix_lente import ralentir_si_enseignante` — le ralenti se faisait à
  l'`atempo` **après** la synthèse, avec un facteur calculé par voix et par
  palier. Mesuré le 26 août 2026 : les quatre voix fr-CA d'Azure, à leur débit
  naturel, tombent déjà entre 12 et 13,4 c/s, soit la bande où cette machinerie
  amenait les MP3 de production (12,5 à 13,8 c/s). Elle produisait à grands
  frais ce qu'Azure donne d'origine.
* `from voix import charge_utile` — le `previous_text` qui empêchait un mot nu
  de sortir à l'anglaise. Le `xml:lang="fr-CA"` du SSML le fait sans rien
  coûter.
* `import requests` — seulement si plus rien ne s'en sert dans le fichier.

Ce que le script refuse de faire
--------------------------------
Il ne convertit un fichier que s'il y reconnaît **exactement** la signature
attendue. Sur les 110, 78 la portent ; les autres ont un `parle` particulier —
une voix par défaut, un traitement de silence, un découpage — et méritent d'être
lus. Le script les liste et n'y touche pas. Convertir à l'aveugle un générateur
dont on n'a pas relu la fonction, c'est exactement la façon dont on perd une
particularité sans que rien ne le signale.

Rien n'est régénéré : ce script modifie du code, pas des MP3. Les fichiers
audio existants restent en place jusqu'à ce qu'on relance un générateur.
"""
import argparse
import pathlib
import re
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent

# Les quatre formes que prennent les 110 générateurs. Elles datent d'époques
# différentes du dépôt et font toutes la même chose : un POST, un MP3, un
# booléen. On garde le nom et la signature de chacune — c'est `main()` qui
# appelle, et il n'est pas touché — et on remplace le corps par une délégation.
#
# La forme « generate » n'a pas de paramètre de voix : elle lit un `VOICE` posé
# au niveau du module. Les 19 fichiers concernés en ont bien un, vérifié.
FORMES = [
    ("def parle(cle, texte, voix, chemin, avant=None, apres=None):",
     "def parle(cle, texte, voix, chemin, avant=None, apres=None):\n"
     "    return parle_compat(cle, texte, voix, chemin)\n"),
    ("def parle(cle, texte, voix, chemin):",
     "def parle(cle, texte, voix, chemin):\n"
     "    return parle_compat(cle, texte, voix, chemin)\n"),
    ("def generate(api_key, text, path):",
     "def generate(api_key, text, path):\n"
     "    return parle_compat(api_key, text, VOICE, path)\n"),
    ("def generate_audio(api_key, text, voice_id, output_path",
     "def generate_audio(api_key, text, voice_id, output_path, *reste, **nommes):\n"
     "    # `voice_settings`, `avant`, `apres` : avalés et ignorés. Les deux\n"
     "    # derniers étaient le contexte français d'ElevenLabs, le premier une\n"
     "    # dérogation de stabilité qui n'a pas d'équivalent en SSML.\n"
     "    return parle_compat(api_key, text, voice_id, output_path)\n"),
]

SIGNATURE = FORMES[0][0]

EN_TETE_IMPORT = '''# L'audio du cours vient d'Azure Speech depuis le 26 août 2026. La fonction
# ci-dessous garde son nom et sa signature — `main()` l'appelle telle quelle —
# mais délègue. La clé ElevenLabs et le contexte `avant`/`apres` sont acceptés
# et ignorés : le `xml:lang="fr-CA"` du SSML rend ce dernier inutile.
from azure_voix import parle_compat  # noqa: E402


'''

# Le `main()` de chaque générateur exige encore la clé ElevenLabs avant de
# commencer. La laisser en place « marcherait » — la clé est toujours dans
# `.env` et serait simplement ignorée — mais un générateur qui réclame une clé
# dont il ne se sert plus est un piège pour le prochain lecteur, et il
# s'arrêterait net le jour où on retirera la ligne du `.env`.
GARDE_CLE = (
    'ELEVENLABS_API_KEY absente (variable d\'environnement ou .env)',
    'AZURE_SPEECH_KEY absente de ~/Claude/.env',
)

A_RETIRER = [
    "from voix_lente import ralentir_si_enseignante\n",
    "from voix import charge_utile  # contexte français, générique ou de dialogue\n",
]


def fin_de_fonction(src, debut):
    """L'indice où se termine la fonction commencée à `debut`.

    On s'arrête à la première ligne de niveau zéro qui n'est ni vide ni un
    commentaire — `def`, `class`, une constante. Se fier à une ligne vide
    couperait la fonction en deux au premier paragraphe de sa docstring.
    """
    lignes = src[debut:].split("\n")
    for i, ligne in enumerate(lignes[1:], 1):
        if ligne and not ligne[0].isspace() and not ligne.startswith("#"):
            return debut + sum(len(x) + 1 for x in lignes[:i])
    return len(src)


def convertir(chemin, ecrire):
    """Renvoie (statut, détail). Ne modifie rien si `ecrire` est faux."""
    src = chemin.read_text(encoding="utf-8")
    if "azure_voix" in src:
        return "déjà", "converti"
    for debut_sig, corps_neuf in FORMES:
        i = src.find("\n" + debut_sig)
        if i >= 0:
            i += 1
            break
    else:
        motif = re.search(r"^def (parle|generate\w*)\(.*$", src, re.M)
        return "à_lire", (motif.group(0)[:70] if motif
                          else "aucune fonction de synthèse")

    neuf = src[:i] + EN_TETE_IMPORT + corps_neuf + src[fin_de_fonction(src, i):]
    # La clé lue reste passée à `parle`, qui l'ignore : on ne touche qu'au
    # message et au nom de la variable cherchée.
    neuf = neuf.replace("ELEVENLABS_API_KEY", "AZURE_SPEECH_KEY")
    neuf = neuf.replace(GARDE_CLE[0], GARDE_CLE[1])
    # Les générateurs cherchent la clé dans le `.env` **du dépôt** ; celle
    # d'Azure vit dans `~/Claude/.env`, avec les autres clés de génération, et
    # c'est là que `azure_voix` la lit. Sans cette substitution le contrôle de
    # tête échoue alors que la synthèse, elle, aurait fonctionné.
    neuf = neuf.replace('env = RACINE / ".env"',
                        'env = Path.home() / "Claude" / ".env"')

    retires = []
    for ligne in A_RETIRER:
        if ligne in neuf:
            neuf = neuf.replace(ligne, "")
            retires.append(ligne.strip().split(" import ")[-1].split("  #")[0])

    # `requests` ne part que s'il ne sert vraiment plus — plusieurs générateurs
    # s'en servent aussi pour téléverser ou pour interroger le manifeste.
    reste = re.sub(r"^\s*(import requests|try:\n\s*import requests.*)$", "",
                   neuf, flags=re.M)
    if not re.search(r"requests\.", reste):
        neuf = re.sub(
            r"try:\n    import requests\nexcept ImportError:\n"
            r'    print\("❌ pip install requests"\); sys\.exit\(1\)\n\n?',
            "", neuf)
        if "import requests" not in neuf:
            retires.append("requests")

    import ast
    try:
        ast.parse(neuf)
    except SyntaxError as e:
        return "cassé", "ligne %s : %s" % (e.lineno, e.msg)

    if ecrire:
        chemin.write_text(neuf, encoding="utf-8")
    return "converti", "retiré : %s" % (", ".join(retires) or "rien")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fichiers", nargs="*")
    ap.add_argument("--essai", action="store_true",
                    help="montre ce qui serait fait, n'écrit rien")
    ap.add_argument("--tous", action="store_true")
    a = ap.parse_args()

    if a.tous or (a.essai and not a.fichiers):
        cibles = sorted((RACINE / "audio").glob("generer_audio*.py"))
    else:
        cibles = [pathlib.Path(f) if pathlib.Path(f).exists() else RACINE / f
                  for f in a.fichiers]
    if not cibles:
        ap.error("donner un fichier, --tous ou --essai")

    compte = {}
    for f in cibles:
        statut, detail = convertir(f, ecrire=not a.essai)
        compte[statut] = compte.get(statut, 0) + 1
        if statut != "converti" or len(cibles) < 20:
            print("  %-9s %-46s %s" % (statut, f.name, detail))
    print("\n%s" % ("  ".join("%s : %d" % (k, v) for k, v in sorted(compte.items()))))
    if a.essai:
        print("(essai — rien n'a été écrit)")
    if compte.get("à_lire"):
        print("Les « à_lire » ont un `parle` particulier : les ouvrir un par un.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
