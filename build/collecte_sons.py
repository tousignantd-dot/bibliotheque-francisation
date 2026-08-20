#!/usr/bin/env python3
"""Reçoit du navigateur le relevé des sons d'un module et l'écrit sur disque.

    python3 build/collecte_sons.py module-relations [port]

Pourquoi ce détour. Les identifiants d'audio d'un module ne s'inventent pas :
ils sont produits par le moteur au moment du rendu (`plAudioManifest()`, les
pastilles de mots, les cartes à écouter). La seule source fiable est donc la
page elle-même. Jusqu'ici on collait le relevé à la main dans
`sons_<slug>.json` ; ce script le reçoit directement, sans recopie et sans
risque de troncature.

Le script attend **un seul envoi**, écrit le fichier, et s'arrête.
Le bout de JavaScript à exécuter dans la page est imprimé au démarrage.
"""
import http.server
import json
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    slug = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 8799
    cible = RACINE / ('sons_%s.json' % slug.replace('-', '_'))

    class H(http.server.BaseHTTPRequestHandler):
        def _cors(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Headers', '*')

        def do_OPTIONS(self):
            self.send_response(204); self._cors(); self.end_headers()

        def do_POST(self):
            n = int(self.headers.get('Content-Length', 0))
            brut = self.rfile.read(n).decode('utf-8')
            try:
                sons = json.loads(brut)
            except json.JSONDecodeError as e:
                self.send_response(400); self._cors(); self.end_headers()
                self.wfile.write(str(e).encode()); return
            if not isinstance(sons, dict) or not sons:
                self.send_response(400); self._cors(); self.end_headers()
                self.wfile.write(b'releve vide'); return
            cible.write_text(json.dumps(sons, ensure_ascii=False, indent=1) + '\n',
                             encoding='utf-8')
            self.send_response(200); self._cors(); self.end_headers()
            self.wfile.write(b'ok')
            print('\n%d sons ecrits dans %s' % (len(sons), cible.name))
            raise SystemExit(0)

        def log_message(self, *a):
            pass

    print('En attente du releve de %s sur le port %d.' % (slug, port))
    print('A executer dans la page du module :\n')
    print("""(()=>{SECTIONS.forEach(s=>{try{render(s.id)}catch(e){}});
 const m={};
 document.querySelectorAll('[onclick*="playWord"]').forEach(el=>{
   const mm=el.getAttribute('onclick').match(/playWord\\(this,\\s*'((?:[^'\\\\]|\\\\.)*)'\\s*,\\s*'((?:[^'\\\\]|\\\\.)*)'\\)/);
   if(mm) m[mm[2].replace(/\\\\'/g,"'")]=mm[1].replace(/\\\\'/g,"'");});
 EXOS.filter(e=>e.type==='vf' && (e.cards||e.listen)).forEach(e=>
   e.rows.forEach(r=>{m[e.id+'_'+r.id]=r.txt.replace(/<[^>]+>/g,'')}));
 Object.assign(m, plAudioManifest());
 return fetch('http://127.0.0.1:%d/',{method:'POST',body:JSON.stringify(m)})
   .then(r=>r.text()).then(t=>Object.keys(m).length+' sons envoyes : '+t);})()""" % port)
    try:
        http.server.HTTPServer(('127.0.0.1', port), H).serve_forever()
    except SystemExit:
        pass


if __name__ == '__main__':
    main()
