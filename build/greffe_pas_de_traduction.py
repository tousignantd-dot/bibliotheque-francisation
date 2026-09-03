#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le navigateur ne traduit plus les pages de la plateforme.

    python3 build/greffe_pas_de_traduction.py [--retirer]

LE DÉFAUT, TROUVÉ LE 3 SEPTEMBRE 2026
Un bouton affichait « Économiser » là où le code dit « Enregistrer », et
« mars 1er sept. » là où le code calcule « mar. 1 sept. ». Vérifié des deux
côtés : le serveur envoie bien « Enregistrer », et le mot « Économiser »
n'existe nulle part dans le dépôt. **C'était Chrome qui traduisait la page** —
il avait lu « Enregistrer » comme l'anglais *Save*.

CE QUE ÇA COÛTERAIT EN CLASSE, ET C'EST AUTRE CHOSE QU'UN LIBELLÉ
Les élèves sont des personnes immigrantes **qui apprennent le français**, et
leur navigateur est très souvent réglé pour traduire automatiquement les pages
françaises dans leur langue. Un élève ouvre un module, Chrome le traduit en
espagnol, en arabe ou en ukrainien — et **le cours de français devient un cours
dans sa langue** : consignes, dialogues, vocabulaire, corrigés. Ça ne dégrade
pas l'exercice, ça le supprime, et rien à l'écran ne dit qu'il s'est passé
quelque chose.

C'est aussi le contraire de la règle déjà posée dans le projet : les consignes
basculent (fr / es / en), **jamais le contenu**. La traduction du navigateur
ignore cette frontière et prend tout.

LE REMÈDE
Deux consignes, parce qu'elles ne sont pas honorées par les mêmes moteurs :
  · `<meta name="google" content="notranslate">` — ce que Chrome lit pour ne
    même pas proposer la traduction ;
  · `translate="no"` sur `<html>` — l'attribut standard, honoré plus largement.

CE QU'ON PERD, ET IL FAUT LE DIRE
Un élève de niveau 1 perd la traduction du navigateur sur l'interface, pas
seulement sur le contenu. C'est un vrai coût. Il est assumé pour deux raisons :
une leçon de français servie en espagnol est bien pire qu'un portail en
français, et la plateforme a **sa propre** langue d'appui, qui bascule les
consignes sans toucher au contenu. L'étendre au portail est la suite logique.

CE QUI N'EST PAS TOUCHÉ, ET DÉLIBÉRÉMENT
`confidentialite.html` : une politique de confidentialité qu'on ne peut pas
traduire est une politique qu'on n'a pas lue. Là, la traduction est un service,
pas une avarie. Le classeur non plus — il s'adresse à des lecteurs
francophones et rien ne s'y joue.
"""
import argparse
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent

DEBUT = '<!-- PAS-DE-TRADUCTION:début — greffé par build/greffe_pas_de_traduction.py -->'
FIN = '<!-- PAS-DE-TRADUCTION:fin -->'
BLOC = ('%s\n<meta name="google" content="notranslate" />\n%s' % (DEBUT, FIN))


def cibles():
    """Tout ce qu'un élève ou un membre du personnel a sous les yeux dans
    l'application. Le classeur et la politique de confidentialité en sont
    exclus — voir l'en-tête."""
    vues = []
    vues += sorted(BASE.glob("assets/interactive/*/*.html"))
    vues.append(BASE / "build" / "gabarit" / "module.html")
    for nom in ("eleve.html", "seance.html", "viewer.html", "hors-ligne.html",
                "catalogue.html", "enseignant.html", "admin.html", "prof.html",
                "progression.html", "fiche-eleve.html", "direction.html",
                "reseau.html", "chiffres.html", "lms.html", "feuille-seance.html"):
        vues.append(BASE / nom)
    vues += sorted(BASE.glob("vocab-flash-*.html"))
    vus, garde = set(), []
    for p in vues:
        if p.exists() and p not in vus:
            vus.add(p)
            garde.append(p)
    return garde


def poser(t):
    # L'attribut standard, ajouté sans toucher au reste de la balise : les
    # fichiers portent trois variantes de <html>, dont une avec un attribut
    # posé par une autre greffe.
    def ajout(m):
        return m.group(0) if "translate=" in m.group(0) else m.group(0)[:-1] + ' translate="no">'
    t = re.sub(r"<html[^>]*>", ajout, t, count=1)
    # Le méta se pose APRÈS la déclaration de charset, jamais avant : le
    # navigateur doit connaître l'encodage le plus tôt possible, et s'insérer
    # devant lui pour gagner deux lignes serait un mauvais échange. À défaut de
    # charset, on se rabat sur l'ouverture du <head>.
    m = (re.search(r"<meta[^>]*charset[^>]*>", t, re.I)
         or re.search(r"<head[^>]*>", t))
    if not m:
        return None
    return t[:m.end()] + "\n" + BLOC + t[m.end():]


def retirer_de(t):
    """On retire EXACTEMENT ce qu'on a posé, saut de ligne compris.

    La première version remplaçait le bloc par un « \\n », ce qui paraissait
    innocent : six fichiers écrivent `<head><meta charset>` sur une seule
    ligne, et le retrait la coupait en deux. Un dégreffage doit rendre le
    fichier à l'octet près, sinon il n'est pas un dégreffage.
    """
    t = re.sub(r"\n" + re.escape(DEBUT) + r".*?" + re.escape(FIN), "",
               t, flags=re.S, count=1)
    t = re.sub(r"(<html[^>]*?) translate=\"no\"", r"\1", t, count=1)
    return t


def traiter(chemin, retirer=False):
    t = chemin.read_text(encoding="utf-8")
    present = DEBUT in t
    if retirer:
        if not present:
            return "déjà retiré"
        chemin.write_text(retirer_de(t), encoding="utf-8")
        return "retiré"
    if present:
        return "déjà posé"
    neuf = poser(t)
    if neuf is None:
        return "REFUS : pas de <head>"
    chemin.write_text(neuf, encoding="utf-8")
    return "posé"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--retirer", action="store_true")
    a = ap.parse_args()
    bilan, fautes = {}, []
    for c in cibles():
        r = traiter(c, a.retirer)
        bilan[r] = bilan.get(r, 0) + 1
        if r.startswith("REFUS"):
            fautes.append("%s : %s" % (c.name, r))
    for k in sorted(bilan):
        print("  %-22s %d" % (k, bilan[k]))
    for f in fautes:
        print("  ⚠ " + f)
    return 1 if fautes else 0


if __name__ == "__main__":
    sys.exit(main())
