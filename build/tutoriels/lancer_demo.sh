#!/bin/zsh
# Portail de francisation, instance de DÉMONSTRATION pour la capture des
# tutoriels. Le stockage est isolé dans un bac à sable jetable : aucune
# donnée réelle n'est lue ni écrite. Le compte est semé par variables
# d'environnement, comme au premier démarrage sur Railway.
#
#   ./build/tutoriels/lancer_demo.sh
#
# Le mot de passe n'est PAS dans le code : il est tiré au hasard au premier
# lancement et gardé dans le bac à sable, hors du dépôt. Les deux autres
# étapes (peupler_demo.py, capturer.js) le relisent au même endroit. Un mot
# de passe écrit ici partirait sur GitHub à chaque commit.
#
# Il faut le **garder** d'un lancement à l'autre : le compte a été créé avec
# son empreinte au premier démarrage, en tirer un neuf fermerait la porte.
set -e
DEPOT="${0:A:h}/../.."
export STORAGE_DIR="${STORAGE_DIR:-${TMPDIR:-/tmp}/francisation-demo-tutoriels}"
mkdir -p "$STORAGE_DIR"

IDENTIFIANTS="$STORAGE_DIR/identifiants-demo.json"
# Le compte enseignant s'ouvre par un CODE depuis le 28 août 2026 : le
# courriel a quitté ces comptes, et `PROF_COURRIEL` ne sème plus rien. Six
# caractères de l'alphabet sans O, I, 0 ni 1.
export PROF_CODE="${PROF_CODE:-DEMO47}"
# Le compte semé au premier démarrage devient **fondateur** de l'arbre, et le
# portail lui montre « Espace direction » — un bouton que les enseignantes à
# qui les capsules s'adressent n'ont pas. Il ne passe donc pas devant la
# caméra : `peupler_demo.py` ouvre un second compte, ordinaire, et c'est
# celui-là qu'on filme. Celui-ci tient la direction et reste hors champ.
export PROF_NOM="${PROF_NOM:-Direction du centre}"
if [ -z "$PROF_MOTDEPASSE" ]; then
  PROF_MOTDEPASSE=$(python3 - "$IDENTIFIANTS" <<'PY'
import json, secrets, sys
from pathlib import Path
fichier = Path(sys.argv[1])
if fichier.exists():
    print(json.loads(fichier.read_text())["motDePasse"])
else:
    print(secrets.token_urlsafe(18))
PY
)
  export PROF_MOTDEPASSE
fi
python3 - "$IDENTIFIANTS" "$PROF_CODE" "$PROF_MOTDEPASSE" <<'PY'
import json, os, sys, stat
from pathlib import Path
fichier = Path(sys.argv[1])
fichier.write_text(json.dumps(
    {"code": sys.argv[2], "motDePasse": sys.argv[3]}, ensure_ascii=False))
os.chmod(fichier, stat.S_IRUSR | stat.S_IWUSR)   # lisible par vous seul
PY

echo "Instance de démonstration — identifiants dans $IDENTIFIANTS"
cd "$DEPOT"
exec python3 server.py
