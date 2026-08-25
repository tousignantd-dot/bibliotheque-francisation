#!/usr/bin/env python3
"""L'arbre des organisations, ses accès et les rattachements des groupes.

Étape 1 du chantier « Le réseau des centres ». Rien ici n'écrit : le contrôle
lit `data/organisations.json`, `data/acces.json`, `data/groups.json` et
`data/teachers.json`, et sort en **code 1** au premier écart — de quoi
l'enchaîner avec les autres contrôles du dépôt dans un `&&`.

Il attrape ce qu'aucune autre vérification ne regarde, et qui ne lève aucune
erreur en service tant que l'étape 2 n'est pas branchée : un `parentId` qui
pointe dans le vide, un cycle (que `org_chain()` survivrait mais qui ferait
mentir toute portée), un rôle posé sur un type de nœud qui n'a pas de sens, un
groupe sans centre, un compte sans accès. Le jour où la portée décidera
vraiment de qui voit quoi, ces écarts-là fermeraient une classe.

    python3 build/controles/organisations.py             # contrôle
    python3 build/controles/organisations.py --etat      # + l'arbre à l'écran
"""
import importlib.util
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def charger_serveur():
    """Charge server.py sans le démarrer — tout est sous `if __name__`."""
    spec = importlib.util.spec_from_file_location("srv", ROOT / "server.py")
    srv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(srv)
    return srv


def controler(srv):
    ecarts = []
    orgs = srv.load_organisations()
    acces = srv.load_acces()
    groups = srv.load_groups()
    teachers = srv.load_teachers()

    if not orgs:
        # Pas un écart : une installation neuve avant le premier démarrage.
        print("Aucune organisation — l'arbre sera posé au prochain démarrage.")
        return []

    par_id = {o["id"]: o for o in orgs}

    # — La forme de l'arbre —
    racines = [o for o in orgs if o.get("parentId") is None]
    if len(racines) != 1:
        ecarts.append(f"{len(racines)} racines au lieu d'une seule : "
                      f"{[o['id'] for o in racines]}")
    for o in racines:
        if o.get("type") != "reseau":
            ecarts.append(f"la racine {o['id']} est de type « {o.get('type')} », "
                          "attendu « reseau »")

    PARENT_ATTENDU = {"reseau": None, "css": "reseau", "centre": "css"}
    for o in orgs:
        if o.get("type") not in srv.TYPES_ORG:
            ecarts.append(f"organisation {o['id']} : type inconnu « {o.get('type')} »")
            continue
        pid = o.get("parentId")
        attendu = PARENT_ATTENDU[o["type"]]
        if attendu is None:
            continue
        if pid is None:
            ecarts.append(f"organisation {o['id']} « {o.get('nom')} » : "
                          f"un {o['type']} doit avoir un parent")
        elif pid not in par_id:
            ecarts.append(f"organisation {o['id']} : parentId {pid} introuvable")
        elif par_id[pid].get("type") != attendu:
            ecarts.append(f"organisation {o['id']} : un {o['type']} sous un "
                          f"{par_id[pid].get('type')}, attendu sous un {attendu}")

    # — Les cycles. org_chain() s'en protège, mais une portée calculée sur un
    #   cycle serait tronquée en silence, et personne ne le verrait. —
    for o in orgs:
        chaine = srv.org_chain(o["id"], orgs)
        if chaine and chaine[-1].get("parentId") is not None:
            ecarts.append(f"organisation {o['id']} : sa chaîne de parents ne "
                          "remonte pas jusqu'à une racine (cycle probable)")

    # — Les groupes —
    centres = {o["id"] for o in orgs if o.get("type") == "centre"}
    for g in groups:
        cid = g.get("centreId")
        if not cid:
            ecarts.append(f"groupe {g['id']} « {g.get('nom')} » : aucun centre")
        elif cid not in centres:
            ecarts.append(f"groupe {g['id']} : centreId {cid} n'est pas un centre")

    # — Les accès —
    vus = set()
    for a in acces:
        if a.get("role") not in srv.ROLES_ACCES:
            ecarts.append(f"accès {a.get('id')} : rôle inconnu « {a.get('role')} »")
            continue
        org = par_id.get(a.get("orgId"))
        if org is None:
            ecarts.append(f"accès {a.get('id')} : orgId {a.get('orgId')} introuvable")
            continue
        attendus = srv.NOEUD_DU_ROLE[a["role"]]
        if org.get("type") not in attendus:
            ecarts.append(f"accès {a.get('id')} : rôle « {a['role']} » posé sur un "
                          f"{org.get('type')}, attendu sur {' ou '.join(attendus)}")
        cle = (a.get("teacherId"), a.get("orgId"), a.get("role"))
        if cle in vus:
            ecarts.append(f"accès {a.get('id')} : doublon exact de {cle}")
        vus.add(cle)

    # — Les personnes —
    avec_acces = {a.get("teacherId") for a in acces if a.get("actif", True)}
    for t in teachers:
        if t["id"] not in avec_acces:
            ecarts.append(f"compte {t['id']} « {t.get('nom')} » : aucun accès actif")

    fondateurs = [a for a in acces if a.get("role") == "fondateur"
                  and a.get("actif", True)]
    if teachers:
        attendu = srv.founder_id(teachers)
        if len(fondateurs) != 1:
            ecarts.append(f"{len(fondateurs)} accès « fondateur » actifs au lieu d'un")
        elif fondateurs[0].get("teacherId") != attendu:
            ecarts.append(f"l'accès « fondateur » est au compte "
                          f"{fondateurs[0].get('teacherId')}, mais founder_id() "
                          f"désigne le compte {attendu}")
    return ecarts


def afficher_arbre(srv):
    orgs = srv.load_organisations()
    acces = srv.load_acces()
    groups = srv.load_groups()
    noms = {t["id"]: t.get("nom", "") for t in srv.load_teachers()}
    enfants = {}
    for o in orgs:
        enfants.setdefault(o.get("parentId"), []).append(o)

    def descendre(org, creux):
        marge = "  " * creux
        print(f"{marge}[{org.get('type')}] {org['id']} · {org.get('nom')}")
        for a in acces:
            if a.get("orgId") == org["id"]:
                etat = "" if a.get("actif", True) else "  (inactif)"
                print(f"{marge}   · {a.get('role')} — "
                      f"{noms.get(a.get('teacherId'), '?')}{etat}")
        for g in groups:
            if g.get("centreId") == org["id"]:
                print(f"{marge}   ▸ groupe {g['id']} · {g.get('nom')}")
        for e in sorted(enfants.get(org["id"], []), key=lambda x: x["id"]):
            descendre(e, creux + 1)

    for racine in enfants.get(None, []):
        descendre(racine, 0)


def main():
    srv = charger_serveur()
    if "--etat" in sys.argv:
        afficher_arbre(srv)
        print()
    ecarts = controler(srv)
    if ecarts:
        print(f"ÉCART — {len(ecarts)} problème(s) dans l'arbre des organisations :")
        for e in ecarts:
            print(f"  · {e}")
        return 1
    print("Arbre des organisations : aucun écart.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
