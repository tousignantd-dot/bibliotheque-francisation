#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Séance sans compte, pour la présentation : un code, vingt appareils, un tableau.

    python3 build/demo_seance.py --install   # ouvre la séance et pose les traces
    python3 build/demo_seance.py --purge     # retire la séance et ses traces
    python3 build/demo_seance.py --etat      # dit ce qui est posé

Ce qu'elle montre, et pourquoi elle existe
-------------------------------------------
Le mode sans compte est le plus difficile à raconter des trois : il n'y a rien
à voir avant qu'une classe l'ait utilisé. L'écran de l'enseignante est vide
tant que personne n'a scanné le code, et une démonstration qui commence par un
tableau vide ne démontre rien.

Cette classe-là n'a donc **aucun compte** : vingt appareils sont entrés avec le
même code de six caractères, et le direct de la classe
(`progression.html`, onglet « au direct ») les montre un par un — Participant 1
à 20 — avec ce que chacun a répondu, item par item. C'est exactement
l'argument : rien à créer avant le cours, rien à garder après.

À ne pas confondre avec `build/demo_classe.py`, la classe de quinze élèves avec
comptes et pseudonymes : les deux peuvent cohabiter, elles n'occupent ni les
mêmes identifiants (les participants comptent en **négatif**) ni le même
module.

Trois partis pris
------------------
1. **Le module est celui de la vie réelle, pas le plus court.** « Pouvez-vous
   régler le problème ? » (module 10 du niveau 4) : un dégât d'eau, un
   propriétaire, une réclamation. C'est la situation que la salle reconnaît, et
   c'est ce qui fait qu'on regarde le tableau plutôt que l'outil.
2. **Les réponses ne sont pas tirées au hasard.** Chaque zone porte une
   difficulté, chaque participant une aisance, et trois zones sont
   délibérément dures : sans elles, « ce qui bloque » n'a rien à montrer et la
   démonstration ne dit pas à quoi le tableau sert. Le tirage est **semé**
   (`random.Random(SEMENCE)`) : la même classe deux fois, sinon la salle voit
   des chiffres qui bougent entre deux répétitions.
3. **On s'arrête où une vraie heure s'arrête.** Personne ne fait 176 zones en
   soixante minutes. La séance couvre « Je découvre » en entier et mord sur le
   Défi 1 ; trois participants arrivent en retard et n'ont que le vocabulaire.

Ce qui n'est pas écrit, et c'est voulu
---------------------------------------
Aucune production orale, aucun texte : dans ce mode, l'élève s'enregistre et
s'écoute, **rien ne part**. Une démonstration qui montrerait des dépôts
mentirait sur ce que le mode collecte — et c'est précisément son argument.
Le texte des réponses ouvertes ne monte pas non plus : le serveur ne le garde
que là où une bonne réponse est déclarée, et les exercices d'écriture n'en ont
pas. On reproduit la règle, on ne la contourne pas.
"""
import argparse
import json
import random
import subprocess
import sys
from datetime import datetime, date, timedelta
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DATA = RACINE / "data"
CONTENU = RACINE / "build" / "contenu"

GROUPE = 1
ACTIVITE = 45
SLUG = "module-probleme"
TITRE = "Module 10 — Pouvez-vous régler le problème ?"
CODE = "PROB24"          # fixe : il est imprimé sur la feuille et lu à voix haute
COMBIEN = 20
SEMENCE = 2610

# Les sections travaillées pendant l'heure, dans l'ordre du module. La séance
# ne se limite pas à une section côté serveur — c'est l'écran qui filtre — mais
# une heure ne va pas plus loin, et un tableau où tout est vert après la
# quatrième section se lit comme une démonstration truquée.
SECTIONS = ("prep", "t1")

# Trois zones que la classe rate. Choisies dans le vocabulaire et la
# compréhension, pas dans la grammaire : ce sont celles dont l'enseignante peut
# faire quelque chose dans les dix minutes qui suivent.
DURES = 3


def charger(nom, defaut):
    f = DATA / nom
    if not f.exists():
        return defaut
    return json.loads(f.read_text(encoding="utf-8"))


def ecrire(nom, valeur):
    (DATA / nom).write_text(json.dumps(valeur, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8")


def zones_du_module():
    """Les zones du module, lues dans son contenu — jamais recopiées ici.

    On passe par node plutôt que par une expression régulière : `exos.js` est
    du JavaScript, il appelle `FC_CARDS.map(...)`, et les zones du premier
    exercice n'existent qu'une fois ce code exécuté. Un lecteur maison ne
    verrait pas ces douze-là, et la démonstration porterait sur un module qui
    n'est pas celui du cours.
    """
    dossier = CONTENU / SLUG
    js = r"""
      const fs = require('fs');
      const EXOS = eval(fs.readFileSync(process.argv[1], 'utf8') + '\n'
                      + fs.readFileSync(process.argv[2], 'utf8') + ';EXOS');
      const nu = t => String(t == null ? '' : t).replace(/<[^>]+>/g, '').trim();
      const out = [];
      for (const ex of EXOS) {
        const base = {exo: ex.id, num: ex.num || '', tit: ex.tit || '',
                      sec: ex.sec || '', type: ex.type};
        // `bonne` et `reponse` ne montent que là où le module les envoie :
        // une étiquette pour vf et match, rien pour imgmatch (que le module
        // laisse tomber) ni pour write (aucune bonne réponse déclarée).
        if (ex.type === 'vf') for (const r of ex.rows)
          out.push({...base, zone: r.id, enonce: nu(r.txt || r.q),
                    bonne: nu(r.ok), choix: (ex.tiles || []).map(nu)});
        else if (ex.type === 'match') for (const r of ex.rows)
          out.push({...base, zone: r.id, enonce: nu(r.q),
                    bonne: nu(r.a), choix: ex.rows.map(x => nu(x.a))});
        else if (ex.type === 'imgmatch') for (const r of ex.rows)
          out.push({...base, zone: r.id, enonce: nu(r.txt || r.q || r.l),
                    bonne: '', choix: []});
        else if (ex.type === 'rows') for (const r of ex.rows)
          out.push({...base, zone: r.id, enonce: nu(r.txt || r.q || r.l),
                    bonne: '', choix: []});
        else if (ex.type === 'texte') for (const r of ex.rows)
          out.push({...base, zone: r.id, enonce: nu(r.q || r.txt),
                    bonne: '', choix: []});
        else if (ex.type === 'blanks') for (const s of ex.segs.filter(s => s.k === 'b'))
          out.push({...base, zone: s.id,
                    enonce: ex.segs.map(x => x.k === 'b' ? ' ____ ' : String(x.t || ''))
                                   .join('').replace(/\s+/g, ' ').trim(),
                    bonne: '', choix: []});
        else if (ex.type === 'write') ex.items.forEach((it, i) =>
          out.push({...base, zone: 'w_' + ex.id + '_' + i, enonce: nu(it.q),
                    bonne: '', choix: []}));
      }
      process.stdout.write(JSON.stringify(out));
    """
    sortie = subprocess.run(
        ["node", "-e", js, str(dossier / "fccards.js"), str(dossier / "exos.js")],
        capture_output=True, text=True)
    if sortie.returncode:
        raise SystemExit("Lecture du module impossible :\n" + sortie.stderr.strip())
    return [z for z in json.loads(sortie.stdout) if z["sec"] in SECTIONS]


def quand(minutes_avant):
    return (datetime.now() - timedelta(minutes=minutes_avant)).isoformat(timespec="seconds")


def installer():
    de = random.Random(SEMENCE)
    zones = zones_du_module()
    if not zones:
        raise SystemExit("Aucune zone lue : le module a changé de forme.")

    # ── L'aisance de chacun, et la difficulté de chaque zone ────────────────
    # Deux courbes plutôt qu'un seul tirage : sans la seconde, tout le monde
    # rate au même endroit avec la même probabilité, et le tableau devient un
    # bruit régulier où aucune ligne ne ressort.
    # Les bornes sont réglées sur ce que l'écran affiche, pas au jugé :
    # `progression.html` classe à 80 % (« Solide ») et 60 % (« À suivre ») du
    # **premier coup**. Un tirage plus large mettait quatorze cartes sur vingt
    # en rouge — une classe en train de couler, ce qui donne à la démonstration
    # l'air de montrer un échec plutôt qu'un instrument. On vise une classe
    # ordinaire : quelques-uns solides, la plupart à suivre, quatre ou cinq en
    # difficulté, dont on a quelque chose à faire.
    aisance = [de.uniform(0.62, 0.98) for _ in range(COMBIEN)]
    difficulte = {z["zone"]: de.uniform(0.03, 0.22) for z in zones}
    for z in de.sample([z for z in zones if z["type"] in ("vf", "match")], DURES):
        difficulte[z["zone"]] = 0.80

    # ── Jusqu'où chacun est allé ────────────────────────────────────────────
    # Trois retardataires (le vocabulaire seul), le gros du groupe au bout de
    # « Je découvre », quelques-uns bien engagés dans le Défi 1.
    prep = [z for z in zones if z["sec"] == "prep"]
    fin = []
    for i in range(COMBIEN):
        if i < 3:
            fin.append(de.randint(10, 16))
        elif i < 14:
            fin.append(de.randint(len(prep) - 12, len(prep) + 6))
        else:
            fin.append(de.randint(len(prep) + 8, len(zones)))

    seances = charger("seances.json", [])
    seances = [s for s in seances if s.get("code") != CODE]
    bas = min([p.get("id", 0) for s in seances for p in s.get("participants", [])]
              + [0])

    participants, lignes = [], []
    for i in range(COMBIEN):
        pid = bas - 1 - i
        entre = 58 - i * 2 + de.randint(0, 2)          # ils arrivent en ordre dispersé
        participants.append({
            "id": pid,
            "numero": i + 1,
            "jeton": "SEANCE-DEMO-%02d" % (i + 1),
            "entreLe": quand(entre),
        })
        libelle = "Participant %d" % (i + 1)
        # Quand chacun a répondu pour la dernière fois. L'écran marque « en
        # ligne » ce qui date de moins de dix minutes : dater toutes les
        # dernières traces de maintenant afficherait vingt personnes
        # connectées à la seconde près, ce qui ne se voit jamais. Les trois
        # retardataires sont partis, les autres travaillent encore.
        derniere = de.uniform(18.0, 34.0) if i < 3 else de.uniform(0.0, 13.0)
        for k, z in enumerate(zones[:fin[i]]):
            p = aisance[i] * (1 - difficulte[z["zone"]])
            tirage = de.random()
            if tirage < p:
                ok, essais = True, 0
            elif tirage < p + (1 - p) * 0.55:
                ok, essais = True, de.randint(1, 2)
            else:
                ok, essais = False, de.randint(1, 3)
            # Le serveur ne garde le texte d'une réponse que là où une bonne
            # réponse est déclarée : on ne le fournit pas ailleurs, sinon la
            # démonstration montrerait un écran que le produit ne donne pas.
            if z["bonne"]:
                if ok:
                    reponse = z["bonne"]
                else:
                    autres = [c for c in z["choix"] if c and c != z["bonne"]]
                    reponse = de.choice(autres) if autres else ""
            else:
                reponse = ""
            # Le temps avance avec le travail : la dernière trace de chacun est
            # ce qui fait dire « en ligne » à l'écran, et tout dater de
            # maintenant afficherait vingt personnes connectées à la fois.
            avance = entre - (entre - derniere) * (k + 1) / max(1, fin[i])
            lignes.append({
                "studentId": pid,
                "studentLabel": libelle,
                "groupId": GROUPE,
                "activityId": ACTIVITE,
                "activityTitle": TITRE,
                "zone": z["zone"],
                "exo": z["exo"],
                "exoNum": z["num"],
                "exoTitre": z["tit"],
                "section": z["sec"],
                "type": z["type"],
                "enonce": z["enonce"][:400],
                "bonne": z["bonne"][:200],
                "reponse": reponse[:200],
                "ok": ok,
                "essais": essais,
                "lastSeen": quand(max(0.0, avance)),
            })

    seance = {
        "id": max([s.get("id", 0) for s in seances] + [0]) + 1,
        "code": CODE,
        "groupId": GROUPE,
        "activityId": ACTIVITE,
        "activityTitle": TITRE,
        "teacherId": 1,
        "creeeLe": quand(62),
        # Elle expire ce soir, comme une vraie : la démonstration se rejoue le
        # lendemain d'un `--install`, jamais d'un fichier qui traîne.
        "expire": date.today().isoformat(),
        "plafond": 40,
        "ouverte": True,
        "participants": participants,
        "demo": True,
    }
    seances.append(seance)
    ecrire("seances.json", seances)

    ids = {p["id"] for p in participants}
    direct = [e for e in charger("direct.json", []) if e.get("studentId") not in ids]
    ecrire("direct.json", direct + lignes)

    justes = sum(1 for l in lignes if l["ok"])
    print("Séance ouverte · code %s · groupe %d · %s" % (CODE, GROUPE, TITRE))
    print("%d participants, %d réponses posées, %d justes (%d %%)."
          % (COMBIEN, len(lignes), justes, round(justes / len(lignes) * 100)))
    inscrits = [e for e in charger("students.json", []) if e.get("groupId") == GROUPE]
    if inscrits:
        print("Note : %d élève(s) inscrit(s) au groupe %d figurent aussi au tableau, "
              "sans réponse — c'est le produit qui est ainsi, pas la démonstration."
              % (len(inscrits), GROUPE))
    print("Le direct : progression.html, groupe %d, module « %s »."
          % (GROUPE, TITRE))
    print("La feuille à imprimer : l'espace enseignant, séance sans compte, code %s."
          % CODE)


def purger():
    seances = charger("seances.json", [])
    ids = {p.get("id") for s in seances if s.get("code") == CODE
           for p in s.get("participants", [])}
    restantes = [s for s in seances if s.get("code") != CODE]
    ecrire("seances.json", restantes)
    direct = charger("direct.json", [])
    ecrire("direct.json", [e for e in direct if e.get("studentId") not in ids])
    print("Séance de démonstration retirée : %d participants, %d réponses."
          % (len(ids), sum(1 for e in direct if e.get("studentId") in ids)))


def etat():
    seance = next((s for s in charger("seances.json", []) if s.get("code") == CODE), None)
    if not seance:
        print("Aucune séance de démonstration. `--install` pour la poser.")
        return 1
    ids = {p["id"] for p in seance.get("participants", [])}
    lignes = [e for e in charger("direct.json", []) if e.get("studentId") in ids]
    print("Séance %s · %d participants · %d réponses · expire le %s"
          % (CODE, len(ids), len(lignes), seance.get("expire")))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--install", action="store_true")
    ap.add_argument("--purge", action="store_true")
    ap.add_argument("--etat", action="store_true")
    a = ap.parse_args()
    if a.purge:
        purger()
    elif a.install:
        installer()
    elif a.etat:
        return etat()
    else:
        ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
