#!/usr/bin/env python3
"""La page « Où manque l'audio », produite depuis le relevé.

    python3 build/audio_page.py        # écrit assets/presentations/audio-manquant.html

Le document est **généré**, jamais écrit à la main : ses chiffres bougent à
chaque générateur qui tourne, et une page recopiée serait fausse une heure
après. La relancer après une production remet la page à jour — c'est le même
principe que `build/tableau_bord.py`.

Habillage : le système de design (`assets/design-system/`), thème clair et
sombre, Newsreader et Nunito comme les autres documents de
`presentations.html`.
"""
import datetime
import html
import pathlib
import sys

RACINE = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / 'build'))
from audio_manquant import releve, mn                      # noqa: E402

SORTIE = RACINE / 'assets' / 'presentations' / 'audio-manquant.html'

NIV = {3: '--niv-3', 4: '--niv-4', 5: '--niv-5', 6: '--niv-6',
       7: '--niv-7', 8: '--niv-8'}

CSS = """
:root{
  --ground:#F7F7F5; --card:#FFFFFF; --sunken:#FBFBFA;
  --ink:#17181A; --body:#3A3D40; --muted:#6E7175;
  --line:#E4E4E0; --line-fort:#D2D2CD;
  --ok:#0A8F5B; --ok-bg:#E6F5EE;
  --trou:#C7302B; --trou-bg:#FBEDEC;
  --part:#C07A08; --part-bg:#FBF2E2;
  --acier:#1D6B8F;
  --niv-3:#B45309; --niv-4:#8C6A07; --niv-5:#0D7A6F;
  --niv-6:#1D6B8F; --niv-7:#3B49A0; --niv-8:#7E3F98;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#151618; --card:#1D1F22; --sunken:#212326;
    --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
    --line:#2E3135; --line-fort:#3D4146;
    --ok:#4BC48D; --ok-bg:#12291F;
    --trou:#EE7A73; --trou-bg:#2E1917;
    --part:#E0A63F; --part-bg:#2C2213;
    --acier:#6DAFD2;
    --niv-3:#E0A63F; --niv-4:#D4BC5C; --niv-5:#5FC3B8;
    --niv-6:#6DAFD2; --niv-7:#8D97DE; --niv-8:#C089D6;
  }
}
:root[data-theme="dark"]{
  --ground:#151618; --card:#1D1F22; --sunken:#212326;
  --ink:#F2F2F0; --body:#CFD1D3; --muted:#94979B;
  --line:#2E3135; --line-fort:#3D4146;
  --ok:#4BC48D; --ok-bg:#12291F;
  --trou:#EE7A73; --trou-bg:#2E1917;
  --part:#E0A63F; --part-bg:#2C2213;
  --acier:#6DAFD2;
  --niv-3:#E0A63F; --niv-4:#D4BC5C; --niv-5:#5FC3B8;
  --niv-6:#6DAFD2; --niv-7:#8D97DE; --niv-8:#C089D6;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--body);
  font-family:Nunito,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  font-size:17px;line-height:1.62;-webkit-font-smoothing:antialiased}
.doc{max-width:880px;margin:0 auto;padding:56px 24px 96px}
.eyebrow{font-size:12px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;
  color:var(--acier);margin:0 0 14px}
h1{font-family:Newsreader,Georgia,serif;font-size:clamp(38px,6.4vw,58px);line-height:1.04;
  font-weight:500;letter-spacing:-.02em;color:var(--ink);margin:0 0 20px;text-wrap:balance}
.chapeau{font-size:19px;line-height:1.6;margin:0;max-width:62ch}
.chapeau strong{color:var(--ink);font-weight:700}
h2{font-family:Newsreader,Georgia,serif;font-size:29px;line-height:1.2;font-weight:600;
  letter-spacing:-.01em;color:var(--ink);margin:0 0 4px;text-wrap:balance}
p{margin:0;max-width:68ch}
section{display:flex;flex-direction:column;gap:16px;padding:44px 0 0;margin:44px 0 0;
  border-top:1px solid var(--line)}
section.premier{border-top:none;margin-top:0;padding-top:40px}
code{font-family:var(--mono);font-size:.86em;background:var(--sunken);
  border:1px solid var(--line);border-radius:4px;padding:1px 5px;color:var(--ink)}
ul.simple{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:8px}
ul.simple li{max-width:66ch} ul.simple li strong{color:var(--ink)}
.these{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--acier);
  border-radius:3px;padding:26px 28px;display:flex;flex-direction:column;gap:12px}
.these p{font-size:18px}
.these .cle{font-family:Newsreader,Georgia,serif;font-size:23px;line-height:1.3;
  font-weight:500;color:var(--ink);font-style:italic}
.chiffres{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:10px}
.ch{background:var(--card);border:1px solid var(--line);border-radius:3px;
  border-top:3px solid var(--trou);padding:15px 16px}
.ch.bon{border-top-color:var(--ok)}
.ch .n{font-family:Newsreader,Georgia,serif;font-size:30px;line-height:1;font-weight:500;
  color:var(--ink);display:block;font-variant-numeric:tabular-nums}
.ch .q{font-size:12.5px;font-weight:700;color:var(--muted);line-height:1.35;display:block;
  margin-top:7px}
.defile{overflow-x:auto;border:1px solid var(--line);border-radius:3px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:15px;min-width:620px}
caption{caption-side:top;text-align:left;padding:0 0 10px;font-size:13.5px;color:var(--muted)}
th,td{padding:11px 15px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
thead th{font-size:11.5px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;
  color:var(--muted);background:var(--sunken);white-space:nowrap}
th.r,td.r{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
tbody tr:last-child td{border-bottom:none}
td.q{font-weight:700;color:var(--ink)}
td small{display:block;color:var(--muted);font-size:13px;line-height:1.45;margin-top:2px}
tbody tr td:first-child{border-left:4px solid transparent}
tfoot td{font-weight:800;color:var(--ink);background:var(--sunken);
  border-top:2px solid var(--line-fort)}
.jauge{display:block;height:7px;border-radius:2px;background:var(--line);margin-top:6px;
  width:150px;overflow:hidden}
.jauge i{display:block;height:100%;background:var(--trou)}
.badge{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:.05em;
  text-transform:uppercase;padding:3px 9px;border-radius:2px;white-space:nowrap}
.b-vide{background:var(--trou-bg);color:var(--trou)}
.b-part{background:var(--part-bg);color:var(--part)}
.b-ok{background:var(--ok-bg);color:var(--ok)}
.reserve{border:1px dashed var(--line-fort);border-radius:3px;padding:20px 24px;
  font-size:15px;color:var(--muted);display:flex;flex-direction:column;gap:9px}
.reserve strong{color:var(--body)}
.pied{margin-top:52px;padding-top:22px;border-top:1px solid var(--line);font-size:13.5px;
  color:var(--muted);display:flex;flex-direction:column;gap:5px}
@media (max-width:620px){ .doc{padding:36px 18px 72px} .jauge{width:96px} }
"""

MOIS = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet',
        'août', 'septembre', 'octobre', 'novembre', 'décembre']


def page():
    tout = releve()
    troues = [d for d in tout if d['sons_manquants'] or d['dial_manquantes']]
    sans_releve = [d for d in tout if not d['releve']]
    vides = [d for d in troues if d['dial_manquantes'] and not d['dial_presentes']]
    partiels = [d for d in troues if d['dial_manquantes'] and d['dial_presentes']]

    n_sons = sum(d['sons_manquants'] for d in troues)
    n_dial = sum(d['dial_manquantes'] for d in troues)
    sec = sum(d['sec_sons'] + d['sec_dial'] for d in troues)

    fam = {}
    for d in troues:
        for f, n in d['par_famille'].items():
            fam[f] = fam.get(f, 0) + n

    par_niveau = {}
    for d in tout:
        n = d['niveau'] or 0
        c = par_niveau.setdefault(n, {'mods': 0, 'troues': 0, 'sons': 0,
                                      'dial': 0, 'sec': 0.0, 'att': 0})
        c['mods'] += 1
        c['att'] += d['dial_attendues']
        if d in troues:
            c['troues'] += 1
            c['sons'] += d['sons_manquants']
            c['dial'] += d['dial_manquantes']
            c['sec'] += d['sec_sons'] + d['sec_dial']

    e = html.escape
    j = datetime.date.today()
    date = '%d %s %d' % (j.day, MOIS[j.month - 1], j.year)

    o = []
    o.append('<!DOCTYPE html>\n<html lang="fr">\n<head>\n<meta charset="utf-8" />')
    o.append('<meta name="viewport" content="width=device-width, initial-scale=1.0" />')
    o.append('<title>Où manque l\'audio</title>')
    o.append('<link rel="preconnect" href="https://fonts.googleapis.com">')
    o.append('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    o.append('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
             'family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600'
             '&family=Nunito:ital,wght@0,400;0,600;0,700;0,800&display=swap">')
    o.append('<style>%s</style>\n</head>\n<body>\n<article class="doc">' % CSS)

    o.append('<p class="eyebrow">Bibliothèque de francisation · %s</p>' % date)
    o.append('<h1>Où manque l\'audio</h1>')
    if troues:
        o.append('<p class="chapeau">Le relevé de ce qui n\'a pas encore de voix : '
                 '<strong>%d modules sur %d</strong>, %s fichiers, environ %s de '
                 'synthèse. Compté sur le disque, jamais estimé.</p>'
                 % (len(troues), len(tout), fmt(n_sons + n_dial), mn(sec)))
    else:
        o.append('<p class="chapeau">Tous les modules ont leur audio : '
                 '<strong>aucun fichier ne manque</strong>, ni pastille haut-parleur '
                 'ni réplique de dialogue.</p>')

    # ── Les chiffres ────────────────────────────────────────
    o.append('<section class="premier"><div class="chiffres">')
    o.append(carte(len(troues), 'modules avec des trous', bon=not troues))
    o.append(carte(n_dial, 'répliques de dialogue', bon=not n_dial))
    o.append(carte(n_sons, 'pastilles haut-parleur', bon=not n_sons))
    o.append(carte(len(vides), 'modules sans un seul dialogue', bon=not vides))
    o.append(carte(mn(sec), 'de synthèse à produire', bon=not troues))
    o.append('</div></section>')

    if troues:
        # ── La thèse ────────────────────────────────────────
        o.append('<section><div class="these">')
        o.append('<p class="cle">Ce qui manque n\'est presque que le bouton '
                 '« Écouter » de Je découvre.</p>')
        o.append('<p>Les pastilles haut-parleur des exercices sont produites partout, '
                 'à %s près. Tout le reste — %s fichiers — ce sont les répliques des '
                 'dialogues : sans elles, le bouton d\'écoute ne joue rien, et c\'est '
                 'la première chose que l\'élève touche dans un module.</p>'
                 % (('un module' if len([d for d in troues if d['sons_manquants']]) == 1
                     else '%d modules' % len([d for d in troues if d['sons_manquants']])),
                    fmt(n_dial)))
        o.append('</div></section>')

        # ── Par niveau ──────────────────────────────────────
        o.append('<section><p class="eyebrow">Par niveau</p>')
        o.append('<h2>Où sont les trous</h2>')
        o.append('<div class="defile"><table><caption>Les modules sans trou ne '
                 'figurent pas dans les colonnes de droite.</caption>')
        o.append('<thead><tr><th>Niveau</th><th class="r">Modules</th>'
                 '<th class="r">Troués</th><th class="r">Sons</th>'
                 '<th class="r">Répliques</th><th class="r">Durée</th></tr></thead><tbody>')
        for n in sorted(par_niveau):
            c = par_niveau[n]
            coul = NIV.get(n)
            style = (' style="border-left-color:var(%s)"' % coul) if coul else ''
            o.append('<tr><td class="q"%s>Niveau %s</td><td class="r">%d</td>'
                     '<td class="r">%s</td><td class="r">%s</td><td class="r">%s</td>'
                     '<td class="r">%s</td></tr>'
                     % (style, n or '?', c['mods'],
                        c['troues'] or '—', c['sons'] or '—',
                        fmt(c['dial']) if c['dial'] else '—',
                        mn(c['sec']) if c['sec'] else '—'))
        o.append('</tbody><tfoot><tr><td>Total</td><td class="r">%d</td>'
                 '<td class="r">%d</td><td class="r">%s</td><td class="r">%s</td>'
                 '<td class="r">%s</td></tr></tfoot></table></div></section>'
                 % (len(tout), len(troues), fmt(n_sons), fmt(n_dial), mn(sec)))

        # ── Deux situations ─────────────────────────────────
        o.append('<section><p class="eyebrow">Deux situations, pas une</p>')
        o.append('<h2>Muet, ou commencé puis arrêté</h2>')
        o.append('<ul class="simple">')
        o.append('<li><strong>%d modules n\'ont pas une seule réplique enregistrée.</strong> '
                 'Leur bouton « Écouter » ne joue rien du tout.</li>' % len(vides))
        if partiels:
            o.append('<li><strong>%d modules ont un dialogue commencé puis arrêté</strong> — '
                     '%s répliques. Ceux-là sont les plus trompeurs : le bouton répond, '
                     'et s\'arrête au milieu.</li>'
                     % (len(partiels), fmt(sum(d['dial_manquantes'] for d in partiels))))
        if fam:
            o.append('<li><strong>Les pastilles manquantes se concentrent dans les '
                     'mini-leçons</strong> : %s.</li>'
                     % ', '.join('%s pour les %s' % (fmt(v), k)
                                 for k, v in sorted(fam.items(), key=lambda x: -x[1])))
        o.append('</ul></section>')

        # ── Le détail ───────────────────────────────────────
        o.append('<section><p class="eyebrow">Module par module</p>')
        o.append('<h2>Du plus troué au moins troué</h2>')
        o.append('<div class="defile"><table><caption>La jauge montre la part du '
                 'dialogue qui manque.</caption>')
        o.append('<thead><tr><th>Module</th><th>Ce qui manque</th>'
                 '<th class="r">Durée</th></tr></thead><tbody>')
        for d in sorted(troues, key=lambda x: -(x['sons_manquants'] + x['dial_manquantes'])):
            coul = NIV.get(d['niveau'])
            style = (' style="border-left-color:var(%s)"' % coul) if coul else ''
            part = (100.0 * d['dial_manquantes'] / d['dial_attendues']
                    if d['dial_attendues'] else 0)
            bits = []
            if d['sons_manquants']:
                bits.append('%s pastilles sur %s' % (fmt(d['sons_manquants']),
                                                     fmt(d['sons_attendus'])))
            if d['dial_manquantes']:
                bits.append('%s répliques sur %s' % (fmt(d['dial_manquantes']),
                                                     fmt(d['dial_attendues'])))
            badge = ('<span class="badge b-vide">muet</span>' if d in vides
                     else '<span class="badge b-part">partiel</span>')
            o.append('<tr><td class="q"%s>%s<small>niveau %s · %s</small></td>'
                     '<td>%s %s<span class="jauge"><i style="width:%d%%"></i></span></td>'
                     '<td class="r">%s</td></tr>'
                     % (style, e(d['slug']), d['niveau'] or '?', e(d['titre']),
                        badge, e(' · '.join(bits)), round(part),
                        mn(d['sec_sons'] + d['sec_dial'])))
        o.append('</tbody></table></div></section>')

    # ── Réserves ────────────────────────────────────────────
    o.append('<section><p class="eyebrow">Ce que ce relevé ne voit pas</p>')
    o.append('<h2>Les réserves</h2><ul class="simple">')
    if sans_releve:
        o.append('<li><strong>%d modules n\'ont pas de relevé de sons</strong> — '
                 '%s. Leurs pastilles ne peuvent pas être vérifiées : les dix plus '
                 'anciens ont été sonorisés avant que les relevés existent et sont '
                 'complets, mais le script les nomme au lieu de les déclarer bons '
                 'sans preuve.</li>'
                 % (len(sans_releve),
                    ', '.join('<code>%s</code>' % e(d['slug']) for d in sans_releve)))
    o.append('<li><strong>La durée est un ordre de grandeur</strong>, calculée sur la '
             'longueur du texte à débit constant. Elle sert à décider, pas à '
             'facturer.</li>')
    o.append('<li><strong>Rien n\'est repayé.</strong> Les générateurs sautent ce qui '
             'est déjà sur le disque : relancer après une coupure reprend où l\'on en '
             'était.</li>')
    o.append('</ul></section>')

    o.append('<div class="reserve"><p><strong>Cette page est produite, pas '
             'écrite.</strong> <code>python3 build/audio_page.py</code> la relit du '
             'disque et la réécrit ; le relevé lui-même est '
             '<code>build/audio_manquant.py</code>, qui ne fait que comparer les '
             'relevés de sons et les dialogues à ce qui existe. Ni l\'un ni l\'autre '
             'n\'appelle jamais l\'API de synthèse. Après une production, la relancer '
             'remet les chiffres à jour.</p></div>')

    o.append('<div class="pied"><p>Bibliothèque de francisation · relevé de l\'audio '
             'manquant au %s.</p><p>Compté par <code>build/audio_manquant.py</code> '
             'sur les %d modules du dépôt.</p></div>' % (date, len(tout)))

    o.append('</article>\n</body>\n</html>')
    return '\n'.join(o)


def fmt(n):
    return format(n, ',').replace(',', ' ') if isinstance(n, int) else str(n)


def carte(valeur, quoi, bon=False):
    return ('<div class="ch%s"><span class="n">%s</span><span class="q">%s</span></div>'
            % (' bon' if bon else '', fmt(valeur), quoi))


def main():
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(page(), encoding='utf-8')
    print('écrit : %s (%d Ko)' % (SORTIE.relative_to(RACINE),
                                  round(SORTIE.stat().st_size / 1024)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
