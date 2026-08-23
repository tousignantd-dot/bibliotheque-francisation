# Le contrôle de la clé de jeu de rôle en double, celui que l'activité 116 a
# payé : deux clés identiques dans un littéral de dictionnaire Python ne
# provoquent rien, la dernière gagne en silence, et le module joue le scénario
# d'un autre niveau. À passer après tout ajout à `JEU_DE_ROLE_SCENARIOS`.
#
#     python3 build/contenu/module-n8-emmenagement/_verif_jr.py
import importlib.util
import os
import re
import sys

SLUG = 'module-n8-emmenagement'
os.environ.setdefault('STORAGE_DIR', '/tmp/verif_' + SLUG)

spec = importlib.util.spec_from_file_location("srv", "server.py")
m = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(m)
except SystemExit:
    pass

man = open('build/contenu/%s/manifest.py' % SLUG, encoding='utf-8').read()
sid = re.search(r"'jr_scenario':\s*'([^']+)'", man).group(1)
role = re.search(r"'jr_role':\s*'([^']+)'", man).group(1)
cas = re.search(r"'jr_cas':\s*'([^']+)'", man).group(1)

s = m.JEU_DE_ROLE_SCENARIOS[sid]
src = open('server.py', encoding='utf-8').read()

ecarts = []
print("scenario  :", sid)
print("rôles     :", list(s['roles']))
print("cas       :", list(s['cas']))
print("ouverture :", list(s['ouverture']))
if role not in s['roles']:
    ecarts.append("jr_role « %s » absent des rôles" % role)
if cas not in s['cas']:
    ecarts.append("jr_cas « %s » absent des cas" % cas)
if set(s['ouverture']) != set(s['roles']):
    ecarts.append("ouverture et rôles ne coïncident pas")
n = src.count('    "%s": {' % sid)
if n != 1:
    ecarts.append("la clé « %s » paraît %d fois dans server.py" % (sid, n))
print("scénarios :", len(m.JEU_DE_ROLE_SCENARIOS))

if ecarts:
    for e in ecarts:
        print("  ✗", e)
    sys.exit(1)
print("✓ le scénario est unique et ses rôles sont ceux du manifeste")
