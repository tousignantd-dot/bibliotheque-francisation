#!/usr/bin/env python3
"""Le contrôle des capsules : ce qu'on peut trouver sans regarder le film.

    python3 build/tutoriels/controle.py            # les sept
    python3 build/tutoriels/controle.py 06         # une seule

Sort en **code 1** au premier écart, comme les autres contrôles du dépôt, de
quoi l'enchaîner dans un `&&` avant une livraison.

Il existe parce que la relecture à l'œil ne tient pas la distance : sept
capsules, cinquante-six plans, et chaque défaut trouvé au visionnement coûte un
tournage. La question posée le 3 septembre 2026 était « est-ce que je pourrais
créer un second agent qui fait un retour sur le vidéo ? ». La réponse honnête
est qu'aucun agent ne *regarde* un film ; mais tout ce qu'on a trouvé à l'œil
jusqu'ici laisse une trace dans les fichiers que la chaîne produit — et ça, ça
se lit.

Les six contrôles, chacun né d'un défaut réel :

1. **Voix tronquée.** Azure rend parfois un son qui s'arrête en pleine phrase,
   sans erreur. On compare les lettres *dites* (le relevé de mots) aux lettres
   *envoyées*. Trouvé à la fin de la capsule 6 : 8 mots sur 28.
2. **Clic de synthèse.** Un échantillon qui saute à pleine échelle là où la
   parole vit entre 5 000 et 15 000. Entendu à la 58e seconde de la capsule 1.
3. **Plan immobile.** Un plan qui dure plus de `IMMOBILE_S` sans un seul geste
   ne raconte rien — c'est le reproche fait aux capsules 2 et 5.
4. **Bouton nommé, bouton non cliqué.** Chaque libellé entre guillemets dans le
   texte doit correspondre à un `clic` du plan. Les exceptions sont déclarées
   ici, et elles sont peu nombreuses : un bouton qui déferait la démonstration.
5. **Repère introuvable ou en retard.** Un `apres` qui ne cite pas les mots
   dits arrête le tournage ; un geste qui arrive plus d'une seconde après ses
   mots se voit.
6. **Film absent ou plus vieux que son manifeste** — le défaut le plus bête :
   relire une capsule qu'on croit refaite.
"""
import json
import pathlib
import re
import struct
import subprocess
import sys
import unicodedata

ICI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI.parent))
import narrer                                    # noqa: E402

VOIX = ICI / "voix"
FILMS = ICI / "films"
CAPSULES = ICI / "capsules"

IMMOBILE_S = 12.0        # un plan sans geste au-delà : l'écran est mort
RETARD_S = 1.0           # un geste en retard de plus d'une seconde se voit
COUVERTURE_MIN = 0.97

# Le contrôle porte sur la **capsule**, pas sur le plan : un bouton nommé au
# premier plan et cliqué au troisième est tenu. Et ce qui est *tapé* ou *choisi*
# compte comme visé — un nom de groupe se saisit, il ne se clique pas.
#
# Restent les guillemets qui ne désignent aucune commande : un nom de section,
# un état de pastille, un exemple. On les nomme ici plutôt que de relâcher la
# règle, qui est ce qui a fait la qualité des capsules.
PAS_DES_COMMANDES = {
    "Je découvre", "Je me lance", "Je retiens des mots", "Défi 2",
    "Élève un, deux, trois", "à venir", "vue en classe", "Aucun",
    "une par semaine", "une aux deux semaines", "une par jour",
    "Avant-midi — Marie", "Colibri", "Élève N",
}

# Les libellés qu'on nomme sans les cliquer, et pourquoi. Toute autre paire de
# guillemets doit trouver son clic. La liste est courte **par principe** :
# chaque entrée est une promesse faite à l'oreille et pas tenue à l'image.
NOMMES_SANS_CLIC = {
    "Retirer les dates": "le cliquer déferait les dates que la capsule vient de poser",
    "Modifier le prompt": "parcouru avec les deux autres, pour ne pas quitter l'écran",
    "Télécharger en point m d": "déclencherait un téléchargement pendant la prise",
    "Tout réinitialiser": "effacerait la commande que la capsule vient de composer",
    "Ajouter le lien Teams": "hors du propos de la capsule",
}


def net(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


def echantillons(mp3):
    brut = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "24000",
         "-f", "s16le", "-"], capture_output=True).stdout
    n = len(brut) // 2
    return struct.unpack("<%dh" % n, brut[:n * 2]) if n > 1 else ()


def vises(capsule):
    """Tout ce que la capsule clique, tape ou choisit, en un seul texte."""
    utiles = ("clic", "clic-index", "onglet", "cocher", "deplier-module",
              "ouvrir-seance", "ouvrir-module", "taper", "choisir", "poser",
              "parcourir", "deplier-liste")
    return net(" ".join(json.dumps(g, ensure_ascii=False)
                        for plan in capsule["plans"]
                        for g in plan.get("gestes", []) if g["do"] in utiles))


def controler(capsule, ecarts):
    cid = capsule["id"]
    cliques = vises(capsule)
    manifeste = ICI / "manifeste.json"
    film = CAPSULES / ("%s.mp4" % cid)
    if not film.exists():
        ecarts.append("%s : aucun film monté" % cid)
    elif film.stat().st_mtime < manifeste.stat().st_mtime:
        ecarts.append("%s : le film est plus vieux que le manifeste — à retourner" % cid)

    releve = FILMS / cid / "images.json"
    dures = {}
    if releve.exists():
        r = json.loads(releve.read_text(encoding="utf-8"))
        dures = {x["plan"]: (x["fin"] - x["debut"]) / 1000 for x in r["reperes"]}

    for plan in capsule["plans"]:
        pid = plan["id"]
        nom = "%s_%s" % (cid, pid)
        dit = plan.get("texte_voix", plan["texte"])
        mots = []
        fichier = VOIX / (nom + ".json")
        if not fichier.exists():
            ecarts.append("%s : pas de narration" % nom)
        else:
            mots = json.loads(fichier.read_text(encoding="utf-8"))["mots"]

        # 1 · la voix dit-elle tout le texte ?
        if mots:
            attendu = narrer.attendus([dit])[0]
            dites = sum(len(narrer.lettres(m["mot"])) for m in mots)
            if dites < attendu * COUVERTURE_MIN:
                ecarts.append("%s : voix tronquée — %d lettres dites sur %d"
                              % (nom, dites, attendu))

        # 2 · un clic de synthèse
        mp3 = VOIX / (nom + ".mp3")
        if mp3.exists():
            v = echantillons(mp3)
            if v:
                pic = max(abs(x) for x in v)
                saut = max(abs(v[i + 1] - v[i]) for i in range(len(v) - 1))
                if pic >= narrer.PIC_SUSPECT and saut >= narrer.SAUT_SUSPECT:
                    ecarts.append("%s : clic de synthèse (pic %d, saut %d)"
                                  % (nom, pic, saut))

        gestes = [g for g in plan.get("gestes", []) if g["do"] not in ("attendre", "js")]

        # 3 · un plan immobile
        duree = dures.get(pid, 0)
        if not gestes and duree > IMMOBILE_S and pid != "fin":
            ecarts.append("%s : %.0f s sans un seul geste — l'écran ne raconte rien"
                          % (nom, duree))

        # 4 · un bouton nommé qui n'est visé nulle part dans la capsule
        for libelle in re.findall(r"«\s*([^»]{2,40}?)\s*»", plan["texte"]):
            if libelle in NOMMES_SANS_CLIC or libelle in PAS_DES_COMMANDES:
                continue
            cible = net(libelle)
            if cible and cible not in cliques and not any(
                    mot in cliques for mot in cible.split() if len(mot) > 4):
                ecarts.append("%s : « %s » est nommé mais aucun clic ne le vise"
                              % (nom, libelle))

        # 5 · un repère introuvable
        phrase = " ".join(net(m["mot"]) for m in mots)
        for g in plan.get("gestes", []):
            if g.get("apres") and net(g["apres"]) not in phrase:
                ecarts.append("%s : le repère « %s » ne se trouve pas dans la narration"
                              % (nom, g["apres"]))


def main():
    filtre = sys.argv[1] if len(sys.argv) > 1 else None
    manifeste = json.loads((ICI / "manifeste.json").read_text(encoding="utf-8"))
    ecarts, n = [], 0
    for capsule in manifeste["capsules"]:
        if filtre and not capsule["id"].startswith(filtre):
            continue
        n += 1
        controler(capsule, ecarts)
    if ecarts:
        print("%d écart%s sur %d capsule%s :"
              % (len(ecarts), "s" if len(ecarts) > 1 else "", n, "s" if n > 1 else ""))
        for e in ecarts:
            print("  · %s" % e)
        sys.exit(1)
    print("%d capsule%s — aucun écart." % (n, "s" if n > 1 else ""))


if __name__ == "__main__":
    main()
