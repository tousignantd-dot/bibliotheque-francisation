#!/usr/bin/env python3
"""Le domaine peut-il envoyer du courriel ? — contrôle DNS, rien n'est écrit.

    python3 build/controles/courriel_domaine.py
    python3 build/controles/courriel_domaine.py --domaine autre.ca

Tant que le domaine n'est pas vérifié chez Resend, la plateforme envoie depuis
l'adresse de bac à sable `onboarding@resend.dev`, **qui n'écrit qu'au
propriétaire du compte**. Impossible, donc, de router les signalements vers
`support@edufrancis.ca` : ils se perdraient en silence.

Trois enregistrements sont à poser, et Resend les donne quand on ajoute le
domaine à son tableau de bord (la clé d'API en service est restreinte à
l'envoi : elle ne peut pas les demander). Ce script ne les invente pas — il
**vérifie qu'ils sont publiés**.

**Le piège qu'il existe pour attraper** : l'éditeur de zone de WHC affiche le
brouillon, pas ce qui est réellement servi. On a déjà perdu une soirée dessus
avec `_railway-verify`. Le script interroge donc les **serveurs autoritatifs**
du domaine, jamais le résolveur du poste, et compare les deux quand ils
divergent — c'est la seule mesure qui dise la vérité.
"""

import argparse
import subprocess
import sys

DOMAINE = "edufrancis.ca"

# nom relatif, type, ce qu'on doit y trouver, à quoi ça sert
#
# ATTENTION — ces trois-là sont ceux que Resend demande AUJOURD'HUI, relevés
# sur son écran « Fill in your DNS Records » le 2 septembre 2026. Le premier
# jet de ce script cherchait un MX et un TXT SPF sur `send`, l'ancienne
# méthode : il annonçait « MANQUE » sur deux enregistrements que Resend ne
# demande plus, devant une zone parfaitement correcte. **Un contrôle qui a tort
# coûte plus cher que pas de contrôle** — on cherche une panne qui n'existe
# pas. Si Resend change encore, c'est ici qu'on recopie son écran.
ATTENDUS = [
    ("resend._domainkey", "TXT", "p=",
     "DKIM : la signature qui prouve que le message vient bien de vous"),
    ("send", "CNAME", "mta.net",
     "envoi : délégué au service d'acheminement de Resend"),
    ("rsend", "CNAME", "mta.net",
     "envoi : le second nom, demandé avec le premier"),
]

# Facultatif pour Resend, **nécessaire en pratique** : sans lui, le premier
# essai d'envoi est arrivé dans les indésirables le 2 septembre 2026, alors que
# DKIM et SPF étaient parfaitement en place. Gmail et Outlook s'en servent pour
# décider s'ils font confiance à un domaine qu'ils ne connaissent pas encore.
CONSEILLE = [
    ("_dmarc", "TXT", "v=DMARC1",
     "DMARC : dit aux boîtes de réception quoi faire d'un message non signé"),
]

# `p=none` surveille sans rien bloquer : une politique stricte posée d'emblée
# sur un domaine neuf ferait rejeter ses propres courriels au premier réglage
# de travers. On durcit plus tard, une fois les rapports lus.
DMARC_SUGGERE = "v=DMARC1; p=none; rua=mailto:admin@%s"


def dig(nom, type_, serveur=None):
    cmd = ["dig", "+short"]
    if serveur:
        cmd.append("@" + serveur)
    cmd += [nom, type_]
    try:
        sortie = subprocess.run(cmd, capture_output=True, text=True,
                                timeout=15).stdout
    except (OSError, subprocess.SubprocessError):
        return []
    return [l.strip() for l in sortie.splitlines() if l.strip()]


def autoritatifs(domaine):
    return [n.rstrip(".") for n in dig(domaine, "NS")] or [None]


def serie(domaine, serveur):
    """Le numéro de série de la zone servie — il dit qui est à jour."""
    for ligne in dig(domaine, "SOA", serveur):
        bouts = ligne.split()
        if len(bouts) > 2:
            return bouts[2]
    return "?"


def controler(domaine):
    serveurs = autoritatifs(domaine)
    print("Domaine : %s" % domaine)
    # **Tous** les serveurs, jamais le premier venu. `dig NS` rend la liste dans
    # un ordre qui change à chaque appel : n'en interroger qu'un rendait le
    # contrôle NON REPRODUCTIBLE — il a annoncé « MANQUE » sur deux CNAME
    # parfaitement posés, le 2 septembre 2026, simplement parce que le second
    # serveur de WHC avait trois versions de retard. Un contrôle qui a tort
    # coûte plus cher que pas de contrôle.
    for s in serveurs:
        print("  %-22s zone n° %s" % (s or "(résolveur local)", serie(domaine, s)))
    print()
    manque = 0
    for groupe, titre, obligatoire in ((ATTENDUS, "Requis par Resend", True),
                                       (CONSEILLE, "Recommandé", False)):
        print("── %s ──" % titre)
        for relatif, type_, marque, role in groupe:
            nom = "%s.%s" % (relatif, domaine) if relatif else domaine
            porteurs = [s for s in serveurs
                        if any(marque.lower() in v.lower()
                               for v in dig(nom, type_, s))]
            trouve = bool(porteurs)
            etat = "✓" if trouve else ("·" if not obligatoire else "MANQUE")
            print("  %-8s %-28s %s" % (etat, "%s %s" % (relatif or "@", type_), role))
            if not trouve and obligatoire:
                manque += 1
            # Posé quelque part mais pas partout : la zone est bonne, la
            # réplication est en cours. Ce n'est pas un manquement — le dire
            # comme tel enverrait reposer un enregistrement déjà là.
            elif trouve and len(porteurs) < len(serveurs):
                print("     ⚠ présent sur %d serveur(s) sur %d — réplication en "
                      "cours, rien à refaire." % (len(porteurs), len(serveurs)))
        print()

    if manque:
        print("%d enregistrement(s) requis manquant(s).\n" % manque)
        print("À faire, dans cet ordre :")
        print("  1. resend.com → Domains → Add Domain → %s" % domaine)
        print("     Resend affiche alors les trois valeurs exactes (le DKIM est")
        print("     unique à votre compte : personne ne peut le deviner).")
        print("  2. Les poser dans la zone WHC, puis PUBLIER — l'éditeur montre")
        print("     le brouillon tant qu'on ne publie pas.")
        print("  3. Relancer ce contrôle.")
        print("  4. Une fois tout au vert : poser RESEND_EXPEDITEUR et faire")
        print("     pointer SIGNALEMENT_DESTINATAIRE vers support@%s" % domaine)
        return 1

    print("Tout est en place. La plateforme peut envoyer depuis ce domaine.")
    # Même règle que plus haut : tous les serveurs, pas le premier venu.
    if not any(marque.lower() in v.lower()
               for relatif, type_, marque, _ in CONSEILLE
               for srv in serveurs
               for v in dig("%s.%s" % (relatif, domaine), type_, srv)):
        print()
        print("Il manque le DMARC, et il ne s'agit pas d'un détail : sans lui,")
        print("un domaine neuf part souvent dans les indésirables. À poser :")
        print("  TXT  _dmarc  %s" % (DMARC_SUGGERE % domaine))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domaine", default=DOMAINE)
    return controler(ap.parse_args().domaine)


if __name__ == "__main__":
    sys.exit(main())
