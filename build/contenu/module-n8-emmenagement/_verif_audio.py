# Vérifie que le générateur audio s'importe et retrouve ses extraits, SANS
# lancer un seul appel à ElevenLabs — une production complète tourne sur le
# poste, celui-ci s'y ajoutera après.
#
#     python3 build/contenu/module-n8-emmenagement/_verif_audio.py
import importlib.util
import json
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location(
    "gen", RACINE / "generer_audio_module_n8_emmenagement.py")
g = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(RACINE))
spec.loader.exec_module(g)          # n'exécute pas main()

dialogues = g.lire_dialogues()
sons = json.loads(g.MANIFESTE.read_text(encoding="utf-8"))
repliques = sum(len(v) for v in dialogues.values())

ecarts = []
print("manifeste :", g.MANIFESTE.name, "—", len(sons), "sons")
if g.MODULE.replace('-', '_') not in g.MANIFESTE.name:
    ecarts.append("le manifeste ne porte pas le slug du module")
for d, lignes in dialogues.items():
    genres = {g.VOIX_PERSO[p] for p, _ in lignes}
    print("  %-5s %2d répliques  %s" % (d, len(lignes),
          ", ".join(sorted({p for p, _ in lignes}))))
    if len(genres) != len({p for p, _ in lignes}):
        ecarts.append("%s : deux personnages partagent une voix" % d)
inconnus = {p for l in dialogues.values() for p, _ in l} - set(g.VOIX_PERSO)
if inconnus:
    ecarts.append("personnage sans voix : %s" % ", ".join(sorted(inconnus)))
print("total     :", repliques, "répliques +", len(sons), "sons =",
      repliques + len(sons), "extraits")

if ecarts:
    for e in ecarts:
        print("  ✗", e)
    sys.exit(1)
print("✓ le générateur s'importe, ses trois dialogues rendent leurs répliques,")
print("  et aucun personnage ne partage sa voix. Aucun appel n'a été fait.")
