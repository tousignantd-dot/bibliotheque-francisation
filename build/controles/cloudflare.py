#!/usr/bin/env python3
"""Le passage chez Cloudflare est-il complet et sans perte ? — rien n'est écrit.

    python3 build/controles/cloudflare.py            # état des lieux
    python3 build/controles/cloudflare.py --cache    # + preuve que le cache sert

Le contrôle répond à trois questions, dans cet ordre, et la troisième est la
seule qui justifie le déménagement :

  1. **La zone est-elle complète ?** Chaque enregistrement relevé chez WHC
     avant le passage doit se retrouver identique. Un oubli ne se voit pas :
     le site continue de servir, et c'est le courriel qui meurt en silence
     trois jours plus tard.
  2. **Le bon nom est-il derrière le proxy ?** `portail` doit l'être — sans
     quoi le trafic ne passe pas par le cache et la facture ne bouge pas. Les
     noms de courriel ne doivent surtout pas l'être : proxifier `send` casse
     l'envoi, parce que le proxy ne parle que HTTP.
  3. **Le cache sert-il vraiment les gros fichiers ?** C'est la seule mesure
     qui dise si le déménagement a payé. Elle se lit dans `cf-cache-status`.

**Le piège que ce script existe pour attraper** : Cloudflare ne met PAS les
`.mp3` en cache par défaut — sa liste d'extensions couvre les images, le CSS
et les polices, pas l'audio. Or les deux tiers des 1,68 Go d'`assets` sont des
MP3. Sans règle de cache explicite, on aura déplacé le DNS **sans toucher à un
sou de la facture de sortie**, et rien à l'écran ne le dira.
"""

import argparse
import ipaddress
import json
import subprocess
import sys
import urllib.request

DOMAINE = "edufrancis.ca"

# ── L'inventaire d'avant, relevé le 2 septembre 2026 sur parking1.whc.ca ─────
# Chaque ligne est un enregistrement qui SERVAIT. Le passage n'a pas le droit
# d'en perdre un seul. `proxy` dit ce que doit être l'état du nuage orange :
#   True  → derrière le proxy (le trafic passe par le cache)
#   False → « DNS seulement », obligatoire pour tout ce qui touche au courriel
ZONE = [
    ("",     "A",     "149.56.225.6",            False,
     "le renvoi 301 de la racine vers le portail, servi par Caddy chez WHC"),
    ("www",  "CNAME", "edufrancis.ca",           False,
     "www suit la racine"),
    ("portail", "CNAME", "mt2s2zez.up.railway.app", True,
     "le site lui-même — LE nom qui doit être derrière le proxy"),
    ("emailfwd", "A",  "149.56.225.6",            False,
     "le relais de courriel de WHC : les renvois confidentialite@ admin@ support@"),
    ("send",  "CNAME", "send.forge.rmta.net",     False,
     "envoi Resend — proxifier ce nom casserait l'envoi"),
    ("rsend", "CNAME", "rsend.forge.rmta.net",    False,
     "envoi Resend, second nom"),
]

# Les enregistrements sans adresse : on vérifie la présence d'une empreinte.
TEXTES = [
    ("", "MX", "emailfwd.edufrancis.ca",
     "la boîte : sans lui, les trois adresses du domaine cessent de recevoir"),
    ("", "TXT", "v=spf1",
     "SPF — dit quels serveurs ont le droit d'écrire en votre nom"),
    ("_dmarc", "TXT", "v=DMARC1",
     "DMARC — ce qui a sorti le domaine des indésirables"),
    ("resend._domainkey", "TXT", "p=MIGfMA0GCSqGSIb3",
     "DKIM — la signature Resend, unique au compte, impossible à redeviner"),
    ("_railway-verify.portail", "TXT", "railway-verify=",
     "la preuve de propriété exigée par Railway ; la retirer libère le domaine"),
]

# Ce qui doit revenir du cache. Un `.mp3` ici est le vrai test : c'est
# l'extension que Cloudflare ignore d'office.
CACHE = [
    ("/assets/interactive/module-n1-classe/prep/line_07_madame_cyr.mp3",
     "un MP3 — les deux tiers du poids du dépôt"),
    ("/assets/design-system/marque-francis-favicon.svg", "une image du système de design"),
]

CF_REPLI = ["104.16.0.0/13", "104.24.0.0/14", "172.64.0.0/13", "162.158.0.0/15",
            "198.41.128.0/17", "173.245.48.0/20", "188.114.96.0/20",
            "190.93.240.0/20", "197.234.240.0/22", "141.101.64.0/18",
            "108.162.192.0/18", "103.21.244.0/22", "103.22.200.0/22",
            "103.31.4.0/22", "131.0.72.0/22"]


def dig(nom, type_, serveur=None):
    cmd = ["dig", "+short"] + (["@" + serveur] if serveur else []) + [nom, type_]
    try:
        return [l.strip() for l in subprocess.run(
            cmd, capture_output=True, text=True, timeout=15).stdout.splitlines()
            if l.strip()]
    except (OSError, subprocess.SubprocessError):
        return []


def reseaux_cloudflare():
    """La liste officielle, avec un repli — un contrôle ne doit pas dépendre
    du réseau pour rendre un verdict."""
    try:
        with urllib.request.urlopen("https://www.cloudflare.com/ips-v4",
                                    timeout=10) as r:
            lignes = r.read().decode().split()
        if lignes:
            return [ipaddress.ip_network(l) for l in lignes]
    except Exception:
        pass
    return [ipaddress.ip_network(p) for p in CF_REPLI]


def derriere_le_proxy(nom, reseaux):
    """Un nom proxifié résout vers une adresse de Cloudflare, jamais vers la
    sienne. C'est la seule lecture possible de l'extérieur : le nuage orange
    ne s'annonce pas dans le DNS."""
    for a in dig(nom, "A"):
        try:
            ip = ipaddress.ip_address(a)
        except ValueError:
            continue
        return any(ip in r for r in reseaux)
    return None


def entetes(url):
    req = urllib.request.Request(url, method="GET",
                                 headers={"User-Agent": "controle-francis"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            return {k.lower(): v for k, v in r.headers.items()}
    except Exception as e:
        return {"_erreur": str(e)}


def controler(domaine, tester_cache):
    ns = sorted(n.rstrip(".") for n in dig(domaine, "NS"))
    chez_cf = any("ns.cloudflare.com" in n for n in ns)
    print("Domaine : %s" % domaine)
    print("Serveurs de noms : %s" % (", ".join(ns) or "aucun"))
    print("→ %s\n" % ("la zone est servie par CLOUDFLARE" if chez_cf else
                      "la zone est encore servie par WHC — le passage n'est pas fait"))

    reseaux = reseaux_cloudflare()
    ennuis = []

    print("── Les enregistrements d'avant sont-ils tous là ? ──")
    for relatif, type_, attendu, proxy_voulu, role in ZONE:
        nom = "%s.%s" % (relatif, domaine) if relatif else domaine
        vals = dig(nom, type_)
        # Un CNAME proxifié ne rend plus son CNAME : Cloudflare répond une
        # adresse. Absence de réponse CNAME n'est donc pas une absence
        # d'enregistrement — il faut le dire, sinon le contrôle a tort.
        proxifie = derriere_le_proxy(nom, reseaux) if chez_cf else False
        trouve = any(attendu.rstrip(".") in v.rstrip(".") for v in vals)
        if not trouve and proxifie and type_ == "CNAME":
            etat, note = "≈", "proxifié : la cible ne se lit plus de l'extérieur"
        elif trouve:
            etat, note = "✓", ""
        else:
            etat, note = "PERDU", "attendu : %s" % attendu
            ennuis.append("%s %s manque" % (relatif or "@", type_))
        print("  %-6s %-26s %s" % (etat, "%s %s" % (relatif or "@", type_), role))
        if note:
            print("         %s" % note)
        if chez_cf and proxifie is not None and proxifie != proxy_voulu:
            if proxy_voulu:
                print("         ⚠ PAS derrière le proxy — le trafic ne passe pas "
                      "par le cache, la facture ne bougera pas.")
                ennuis.append("%s devrait être proxifié" % (relatif or "@"))
            else:
                print("         ⚠ DERRIÈRE LE PROXY, et il ne doit pas l'être — "
                      "le proxy ne parle que HTTP : ceci casse le courriel.")
                ennuis.append("%s ne doit pas être proxifié" % (relatif or "@"))
    print()

    print("── Courriel et preuves de propriété ──")
    for relatif, type_, marque, role in TEXTES:
        nom = "%s.%s" % (relatif, domaine) if relatif else domaine
        trouve = any(marque.lower() in v.lower() for v in dig(nom, type_))
        print("  %-6s %-26s %s" % ("✓" if trouve else "PERDU",
                                   "%s %s" % (relatif or "@", type_), role))
        if not trouve:
            ennuis.append("%s %s manque" % (relatif or "@", type_))
    print()

    if tester_cache:
        print("── Le cache sert-il vraiment ? (deux appels par fichier) ──")
        if not chez_cf:
            print("  · zone encore chez WHC : il n'y a pas de cache à mesurer.\n")
            tester_cache = False
        for chemin, quoi in (CACHE if tester_cache else []):
            url = "https://portail.%s%s" % (domaine, chemin)
            entetes(url)                      # le premier appel remplit
            h = entetes(url)                  # le second doit toucher
            statut = h.get("cf-cache-status", "(absent)")
            cc = h.get("cache-control", "(aucun)")
            bon = statut.upper() in ("HIT", "REVALIDATED")
            print("  %-6s %s" % ("✓" if bon else "FROID", quoi))
            print("         cf-cache-status: %-12s cache-control: %s"
                  % (statut, cc))
            if not bon and chez_cf:
                print("         ⚠ ce fichier repart du serveur à chaque élève. "
                      "Il faut une règle de cache : Cloudflare n'inclut PAS les "
                      ".mp3 dans sa liste d'extensions par défaut.")
                ennuis.append("cache froid sur %s" % chemin)
        print()

    if ennuis:
        print("%d point(s) à régler :" % len(ennuis))
        for e in ennuis:
            print("  · %s" % e)
        return 1
    print("Rien à signaler." if chez_cf else
          "Rien de perdu — le passage reste à faire.")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--domaine", default=DOMAINE)
    ap.add_argument("--cache", action="store_true",
                    help="mesurer si le cache sert les gros fichiers")
    a = ap.parse_args()
    return controler(a.domaine, a.cache)


if __name__ == "__main__":
    sys.exit(main())
