#!/usr/bin/env python3
"""Le bornage par niveau : ce que la table des accès promet, et ce qu'elle tient.

Décidé le 7 septembre 2026 — un accès peut ne porter que sur certains niveaux
(`assets/presentations/acces-borne-par-niveau.html`). Rien ici n'écrit : le
contrôle lit `data/acces.json`, `data/groups.json` et `data/teachers.json`, et
sort en **code 1** au premier écart, de quoi l'enchaîner dans un `&&`.

Il attrape quatre choses, dont aucune ne lève d'erreur en service :

1. **Un `niveaux` illisible.** Le champ traverse une console, un formulaire et
   un fichier ; `normalize_niveaux()` jette en silence ce qu'il ne comprend
   pas. Un bornage qui se réduit à rien **rouvre tout**, et personne ne le voit.
2. **Un bornage sur le fondateur**, que la route refuse mais qu'une écriture à
   la main dans le fichier poserait quand même.
3. **Un groupe hors de la portée de son titulaire.** C'est le cas prévu, pas
   une anomalie : on borne une personne qui tient déjà un groupe d'un autre
   niveau, et les groupes existants ne sont pas réécrits. Il faut le **voir**,
   pas le corriger en silence — changer sous les pieds d'une enseignante le
   catalogue de sa classe serait pire que l'écart.
4. **Un bornage à demi posé.** Une personne bornée sur une ligne et libre sur
   une autre n'est pas bornée du tout (`niveaux_de()` prend l'union). C'est la
   règle, et elle est volontaire ; mais l'écart entre l'intention et l'effet
   doit se lire quelque part, sinon on croit avoir fermé.

    python3 build/controles/niveaux_acces.py           # contrôle
    python3 build/controles/niveaux_acces.py --etat    # + qui est borné
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
    acces = srv.load_acces()
    groups = srv.load_groups()
    teachers = srv.load_teachers()
    par_id = {t["id"]: t for t in teachers}
    fid = srv.founder_id(teachers)

    for a in acces:
        if a.get("actif") is False:
            continue
        brut = a.get("niveaux")
        if brut in (None, [], ()):
            continue
        propre = srv.normalize_niveaux(brut)
        if not propre:
            ecarts.append(
                f"accès {a.get('id')} ({par_id.get(a.get('teacherId'), {}).get('nom', '?')}) : "
                f"« niveaux » = {brut!r} ne donne aucun niveau lisible — "
                "le bornage ne borne rien")
        elif len(propre) != len(brut if isinstance(brut, (list, tuple)) else [brut]):
            ecarts.append(
                f"accès {a.get('id')} : « niveaux » = {brut!r} se réduit à "
                f"{propre} — une entrée a été jetée en silence")
        if a.get("teacherId") == fid:
            ecarts.append(
                f"accès {a.get('id')} : le fondateur est borné à {propre}. "
                "La route le refuse ; ceci a donc été écrit à la main, et "
                "personne ne pourrait lever le bornage.")

    # — Le bornage à demi posé, et les groupes hors portée —
    for t in teachers:
        if t.get("actif") is False or t["id"] == fid:
            continue
        lignes = [a for a in acces
                  if a.get("teacherId") == t["id"] and a.get("actif", True)]
        if not lignes:
            continue
        bornees = [a for a in lignes if srv.normalize_niveaux(a.get("niveaux"))]
        if bornees and len(bornees) != len(lignes):
            ecarts.append(
                f"compte {t['id']} ({t.get('nom', '?')}) : borné sur "
                f"{len(bornees)} accès sur {len(lignes)} — l'union des lignes "
                "le laisse voir tous les niveaux. Borner chaque ligne, ou aucune.")
        portee = srv.niveaux_de(t, acces)
        if not portee:
            continue
        for g in groups:
            if g.get("teacherId") != t["id"]:
                continue
            niveau = srv.niveau_de_groupe(g)
            if niveau not in portee:
                ecarts.append(
                    f"groupe {g.get('id')} « {g.get('nom', '')} » est du {niveau}, "
                    f"mais son titulaire {t.get('nom', '?')} est borné à "
                    f"{sorted(portee)} — à trancher à la main, groupe par groupe.")
    return ecarts


def afficher_etat(srv):
    acces = srv.load_acces()
    teachers = {t["id"]: t for t in srv.load_teachers()}
    bornes = [a for a in acces
              if a.get("actif", True) and srv.normalize_niveaux(a.get("niveaux"))]
    if not bornes:
        print("Aucun accès borné — tout le monde voit tous les niveaux.")
        return
    print("Accès bornés :")
    for a in bornes:
        print("  · %-24s %-12s %s" % (
            teachers.get(a.get("teacherId"), {}).get("nom", "compte inconnu"),
            a.get("role", ""),
            ", ".join(srv.normalize_niveaux(a.get("niveaux")))))


def main():
    srv = charger_serveur()
    if "--etat" in sys.argv:
        afficher_etat(srv)
        print()
    ecarts = controler(srv)
    if ecarts:
        print("ÉCARTS (%d) :" % len(ecarts))
        for e in ecarts:
            print("  ✗ " + e)
        sys.exit(1)
    print("Bornage par niveau : rien à signaler.")


if __name__ == "__main__":
    main()
