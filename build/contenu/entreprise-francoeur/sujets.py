"""Ce que montre chaque croquis de la Maison Francœur — une description de FORME.

Trois familles, qui n'appellent pas le même préambule (voir
`build/francoeur_croquis.py`) :

- "vetement" — l'article seul, à plat, de face : le dessin des catalogues ;
- "detail"   — le vêtement entier en gris pâle, et SEULE la partie nommée en
               couleur. Montrer « une manche » isolée ne se lit pas : on
               montre où elle est ;
- "objet"    — un objet du magasin, même trait, même aplat, sans vêtement.

Règles d'écriture, payées ailleurs :
- décrire la forme, jamais le mot seul — un mot polysémique se dessine selon
  son autre sens ;
- donner la couleur dans la description, et varier les couleurs d'une planche
  à l'autre : une planche toute bleue ne dit rien des couleurs ;
- tout objet qui PORTE un texte (étiquette, reçu, carte, écran, cadran) est
  décrit vierge, ou son texte remplacé par des filets gris ;
- une paire se dit « ONE PAIR » et se décrit côte à côte.
"""

V, D, O = "vetement", "detail", "objet"

SUJETS = {
    # ── Les hauts ────────────────────────────────────────────────────────
    "chandail": (V, "a long-sleeved crew-neck knit sweater with ribbed cuffs, ribbed hem and ribbed "
                    "round neckline. HORIZONTAL STRIPES all over: navy blue stripes alternating with "
                    "off-white stripes of equal width, the stripes running straight across the body "
                    "and around the sleeves."),
    "t-shirt":  (V, "a plain short-sleeved crew-neck t-shirt in solid heather grey, straight hem."),
    "chemise":  (V, "a men's long-sleeved button-up dress shirt in solid light blue, pointed collar, "
                    "a straight row of small white buttons down the front, buttoned cuffs, one chest "
                    "pocket on the left."),
    "blouse":   (V, "a women's light, flowing long-sleeved blouse in soft coral pink, a small round "
                    "collar, a short row of tiny buttons at the neck only, gathered cuffs, a gently "
                    "curved hem."),
    "polo":     (V, "a short-sleeved polo shirt in solid bottle green: a soft folded collar, a short "
                    "placket with two buttons below the collar, ribbed sleeve bands."),
    "camisole": (V, "a sleeveless tank top in solid white with thin straps over the shoulders, a "
                    "scoop neckline and deep armholes."),
    "coton-ouate": (V, "a long-sleeved crew-neck sweatshirt in solid burgundy, thick fleece fabric, "
                    "wide ribbed cuffs and ribbed waistband. No hood, no pocket, no zipper."),
    "kangourou": (V, "a pullover hooded sweatshirt in solid charcoal grey: a hood with two drawstring "
                    "cords hanging at the front, ONE large pouch pocket across the belly open on both "
                    "sides, ribbed cuffs and waistband. No zipper."),
    "cardigan": (V, "a long-sleeved knit cardigan in solid oatmeal beige, open V-neck, buttoned all the "
                    "way down the front with five round buttons, ribbed cuffs and hem, two small patch "
                    "pockets at the hips."),
    "col-roule": (V, "a long-sleeved fine-knit sweater in solid black with a tall folded-over "
                    "turtleneck collar that covers the whole neck, ribbed cuffs and hem."),
    "veste":    (V, "a SLEEVELESS quilted puffer vest in solid mustard yellow: NO SLEEVES AT ALL, open "
                    "armholes, a stand-up collar, a central front zipper, horizontal quilting lines, "
                    "two zipped hand pockets."),
    "haut-court": (V, "a short-sleeved cropped t-shirt in solid lilac that stops above the waist, "
                    "shorter than a normal t-shirt, straight cropped hem."),

    # ── Les bas du corps ─────────────────────────────────────────────────
    "pantalon": (V, "a pair of straight-leg casual trousers in solid khaki beige, belt loops, a front "
                    "button and fly, two slanted front pockets, a sharp crease down each leg, full length."),
    "jeans":    (V, "a pair of classic five-pocket blue denim jeans in medium indigo blue, belt loops, a "
                    "metal button, curved front pockets, contrast topstitching in golden thread, "
                    "straight legs, full length."),
    "jupe":     (V, "a knee-length A-line skirt in solid royal blue, a flat waistband, flaring gently "
                    "toward the hem."),
    "short":    (V, "a pair of casual shorts in solid navy blue cotton ending mid-thigh, belt loops, "
                    "front button, two front pockets, turned-up hems."),
    "legging":  (V, "a pair of tight stretchy leggings in solid black, a wide elastic waistband, the "
                    "legs narrow and close-fitting down to the ankles, no pockets, no seams detail."),
    "cargo":    (V, "a pair of loose cargo trousers in olive green, belt loops, and a LARGE PATCH "
                    "POCKET WITH A FLAP on the side of each thigh, full length, elastic at the ankles."),
    "jogging":  (V, "a pair of jogging pants in solid heather grey fleece: an elastic waistband with a "
                    "white drawstring cord tied in a bow, two side pockets, ribbed cuffs gathered at "
                    "the ankles."),
    "salopette": (V, "a pair of denim overalls in light blue denim: a bib panel on the chest with a "
                    "pocket, two shoulder straps with metal buckles, straight legs, full length."),
    "bermuda":  (V, "a pair of long Bermuda shorts in solid sand beige ending just above the knee, belt "
                    "loops, front button, two front pockets."),
    "pantalon-habit": (V, "a pair of formal dress trousers in solid charcoal grey wool, a narrow "
                    "waistband with a hook closure, a pressed central crease on each leg, slim straight "
                    "legs, full length, no visible pockets on the front."),

    # ── Robes et habits ──────────────────────────────────────────────────
    "robe":     (V, "a simple short-sleeved day dress in solid emerald green, round neckline, fitted "
                    "at the waist with a thin self-fabric belt, a flared skirt ending at the knee."),
    "robe-soiree": (V, "a long elegant sleeveless evening gown in deep midnight blue, a V-neckline, "
                    "thin straps, a fitted bodice and a long flowing skirt reaching the floor."),
    "combinaison": (V, "a one-piece jumpsuit in solid rust orange: a sleeveless top and full-length "
                    "wide-leg trousers joined at the waist in ONE garment, a tie belt at the waist."),
    "habit":    (V, "a men's two-piece business suit in solid navy blue shown together: a single-"
                    "breasted jacket with notched lapels and two buttons ABOVE matching full-length "
                    "trousers, the jacket placed above the trousers, both flat and centred."),
    "veston":   (V, "a men's single-breasted suit jacket alone in solid medium grey: notched lapels, two "
                    "front buttons, a breast pocket, two flap pockets at the hips, long sleeves."),
    "tailleur": (V, "a women's two-piece skirt suit in solid black shown together: a fitted short "
                    "jacket with lapels and three buttons ABOVE a matching straight knee-length skirt."),
    "cravate":  (V, "one long necktie in solid wine red, laid straight and vertical, knotted at the "
                    "top, the wide pointed end at the bottom."),
    "noeud-pap": (V, "one bow tie in solid black, tied, seen from the front, with a thin neck band "
                    "going out to each side."),

    # ── L'extérieur ──────────────────────────────────────────────────────
    "parka":    (V, "a long hooded winter parka reaching mid-thigh, in solid dark forest green. A hood "
                    "with a faux-fur trim around the face opening, a central front zipper covered by a "
                    "snap-button placket, two large flap pockets at the hips, two chest pockets, and "
                    "elastic storm cuffs at the wrists. The hood is up and empty, seen from the front."),
    "manteau":  (V, "a long classic wool overcoat in solid camel brown reaching the knee, wide notched "
                    "lapels, double-breasted with two rows of three buttons, two flap pockets, long "
                    "sleeves."),
    "impermeable": (V, "a long belted trench coat raincoat in solid khaki beige, reaching the knee, a "
                    "wide collar, double-breasted buttons, a belt tied at the waist, shoulder flaps."),
    "coupe-vent": (V, "a light zip-up windbreaker jacket in bright red thin nylon, a stand-up collar, "
                    "a full front zipper, elastic cuffs and hem, hip length. No hood."),
    "manteau-duvet": (V, "a hip-length puffer down jacket in solid navy blue with LONG SLEEVES, puffy "
                    "horizontal quilted chambers all over, a stand-up collar and a central zipper."),
    "tuque":    (V, "a knitted winter hat in solid red, ribbed knit, a folded cuff at the bottom and a "
                    "round white pompom on top, seen from the front."),
    "foulard":  (V, "a long knitted winter scarf in solid teal blue, laid flat in one long vertical "
                    "band folded once, with short fringes at both ends."),
    "cache-cou": (V, "a neck warmer: a short closed tube of thick fleece in solid black, like a wide "
                    "ring, seen from the front, slightly flattened."),
    "mitaines": (V, "ONE PAIR of thick winter mittens in solid royal blue, side by side, each with a "
                    "separate thumb and ONE single pocket for the four other fingers together — NO "
                    "separate fingers — ribbed wrist cuffs."),
    "gants":    (V, "ONE PAIR of leather gloves in solid dark brown, side by side, each with FIVE "
                    "separate fingers."),
    "cache-oreilles": (V, "a pair of earmuffs: two round fluffy pads in soft pink fur joined by a thin "
                    "curved headband, seen from the front."),
    "habit-neige": (V, "a child's one-piece snowsuit in bright purple: hood, long sleeves and long legs "
                    "all in ONE puffy piece, a central zipper from the neck to the crotch, elastic "
                    "cuffs, reflective strips on the legs."),

    # ── Dessous et nuit ──────────────────────────────────────────────────
    "bas-chaussettes": (V, "ONE PAIR of plain crew socks in solid white with grey heel and toe, side "
                    "by side, seen in profile."),
    "collants": (V, "a pair of sheer tights in solid black laid flat: waistband at the top, two "
                    "legs down to closed feet, seamless."),
    "brassiere": (V, "a simple everyday bra in solid nude beige: two smooth cups, thin adjustable "
                    "straps, a narrow band under the cups, catalogue flat drawing."),
    "culotte":  (V, "a pair of plain women's briefs in solid light blue cotton, catalogue flat "
                    "drawing, elastic waistband."),
    "boxer":    (V, "a pair of men's boxer briefs in solid dark grey, a wide elastic waistband in "
                    "black, short close-fitting legs, catalogue flat drawing."),
    "pyjama":   (V, "a two-piece pyjama set in soft sky blue with small white stars: a long-sleeved "
                    "button-up top with a collar ABOVE matching long loose trousers with an elastic "
                    "waist."),
    "jaquette": (V, "a long women's nightgown in soft pale lavender cotton, short puffed sleeves, a "
                    "gathered round neckline with a small bow, loose and reaching the ankles."),
    "robe-chambre": (V, "a bathrobe in thick white terry cloth, long sleeves, a shawl collar, two "
                    "patch pockets, a matching belt tied at the waist, reaching the knee."),
    "maillot":  (V, "a women's one-piece swimsuit in solid turquoise, a scoop neckline, thin straps, "
                    "high-cut legs."),

    # ── Les chaussures ───────────────────────────────────────────────────
    "espadrilles": (V, "ONE PAIR of casual lace-up athletic sneakers, the two shoes side by side, "
                    "seen from the outer side in profile, toes pointing left: white rubber sole, light "
                    "grey upper, white laces, a small padded collar at the heel. Plain, without any "
                    "stripes or logo on the side."),
    "souliers": (V, "ONE PAIR of classic men's leather lace-up dress shoes in polished dark brown, "
                    "side by side, in profile, toes pointing left, thin leather soles, low heel."),
    "bottes":   (V, "ONE PAIR of tall insulated winter boots, side by side, in profile, toes pointing "
                    "left: thick dark rubber soles with deep treads, a black waterproof lower part, "
                    "a quilted upper shaft in dark grey reaching mid-calf, a faux-fur trim at the top."),
    "bottes-pluie": (V, "ONE PAIR of rubber rain boots in glossy yellow, side by side, in profile, "
                    "toes pointing left, reaching mid-calf, smooth with no laces."),
    "bottillons": (V, "ONE PAIR of ankle boots in tan suede, side by side, seen from the OUTER SIDE in full profile, toes pointing left, the whole shoe outline visible from toe to heel: the shaft ends just above the ankle, an elastic side panel, a low block heel."),
    "sandales": (V, "ONE PAIR of flat summer sandals in natural light brown leather, side by side, "
                    "seen from above: a thin sole, two crossing straps over the foot and a strap "
                    "around the heel with a small buckle."),
    "gougounes": (V, "ONE PAIR of flip-flops in bright orange rubber, side by side, seen from above: "
                    "a flat sole and a thin Y-shaped strap that passes between the toes."),
    "talons":   (V, "ONE PAIR of classic pointed-toe high-heeled pumps in glossy black, side by side, "
                    "in profile, toes pointing left, a thin tall stiletto heel."),
    "pantoufles": (V, "ONE PAIR of cosy slip-on house slippers in soft grey felt, side by side, seen "
                    "at three-quarters, a closed toe, an open back, a fluffy white lining."),
    "claques":  (V, "ONE PAIR of thin black rubber overshoes, side by side, in profile, toes pointing "
                    "left: low, smooth, shaped like a shoe outline, meant to be pulled over a dress shoe."),

    # ── Les accessoires ──────────────────────────────────────────────────
    "ceinture": (V, "one leather belt in solid brown, laid in a loose horizontal curve, a plain "
                    "rectangular metal buckle at one end, a row of holes at the other."),
    "sacoche":  (V, "a women's structured handbag in solid cognac brown leather, two short rounded "
                    "handles on top, a flap with a small metal clasp, seen from the front."),
    "portefeuille": (V, "a closed bifold wallet in solid black leather, seen from the front, "
                    "slightly open to show two empty card slots, no cards inside."),
    "casquette": (V, "a baseball cap in solid navy blue, seen at three-quarters from the front, a "
                    "curved brim, six panels and a button on top. Completely plain, no logo, no "
                    "embroidery."),
    "chapeau":  (V, "a wide-brimmed summer hat in natural straw, a round crown with a black ribbon "
                    "band, seen from the front, slightly from above."),
    "lunettes-soleil": (V, "one pair of sunglasses seen from the front, black frames, dark tinted "
                    "lenses, temples folded open."),
    "collier":  (V, "a delicate gold chain necklace laid in a U shape, with one small round pendant "
                    "at the bottom."),
    "boucles":  (V, "ONE PAIR of earrings side by side: small gold hoops, each with a small pearl "
                    "hanging from it."),
    "bracelet": (V, "a simple bracelet of polished silver links, laid in a circle, seen from above."),
    "montre":   (V, "a wristwatch seen from the front: a round silver case, a plain white face with "
                    "twelve small tick marks and two hands, NO NUMBERS and no brand, a brown leather "
                    "strap going up and down out of the frame."),
    "sac-dos":  (V, "a backpack in solid forest green, seen from the front: two top loops, a large "
                    "front pocket with a zipper, two shoulder straps visible at the sides. No logo."),
    "parapluie": (V, "an open umbrella in solid dark red seen from the side, eight panels, a straight "
                    "black shaft and a curved J-shaped handle."),

    # ── Le vêtement en détail : le vêtement en gris, la partie en couleur ─
    "manche":   (D, "a long-sleeved t-shirt. ONLY the LEFT SLEEVE (the sleeve on the viewer's right) "
                    "is filled in bright orange; the body and the other sleeve stay pale grey."),
    "col":      (D, "a button-up shirt. ONLY the COLLAR around the neck is filled in bright blue; "
                    "the rest of the shirt stays pale grey."),
    "capuchon": (D, "a zip-up hooded sweatshirt, hood up and empty. ONLY the HOOD is filled in bright "
                    "green; the rest stays pale grey."),
    "poche":    (D, "a pair of jeans. ONLY the two front POCKETS are filled in bright red; the rest "
                    "of the jeans stays pale grey."),
    "fermeture": (D, "a zip-up jacket seen from the front, fully closed. ONLY the ZIPPER is coloured: a WIDE bright yellow zipper tape running from the collar to the hem down the centre, its teeth drawn large and clearly visible, and a big yellow pull tab at the top. The rest of the jacket stays pale grey."),
    "bouton":   (D, "a cardigan buttoned down the front. ONLY the five round BUTTONS are filled in "
                    "bright red, drawn slightly larger than usual; the rest stays pale grey."),
    "ourlet":   (D, "a pair of trousers. ONLY the folded HEM at the bottom of each leg — a narrow band "
                    "with a visible line of stitching — is filled in bright purple; the rest stays pale grey."),
    "doublure": (D, "a suit jacket shown OPEN, the two front panels folded back so that the inside is "
                    "visible. ONLY the inner LINING is filled in bright teal with a subtle sheen; the "
                    "outside of the jacket stays pale grey."),
    "poignet":  (D, "a long-sleeved sweater. ONLY the two ribbed CUFFS at the end of the sleeves, at "
                    "the wrists, are filled in bright orange; the rest stays pale grey."),
    "bretelle": (D, "a sleeveless summer dress with thin straps. ONLY the two thin shoulder STRAPS are "
                    "filled in bright pink; the rest of the dress stays pale grey."),
    "taille-ceinture": (D, "a pair of trousers. ONLY the WAISTBAND at the top, with its belt loops, "
                    "is filled in bright blue; the rest stays pale grey."),
    "etiquette-soin": (O, "a small white fabric care label sewn into a garment seam, enlarged: on it "
                    "a single row of five simple black laundry care pictograms — a wash tub, a "
                    "triangle, a square with a circle inside, an iron, a circle. NO WORDS, NO LETTERS, "
                    "NO NUMBERS on the label."),
    "jambe":    (D, "a pair of trousers. ONLY the LEFT LEG (on the viewer's right), from the crotch to "
                    "the ankle, is filled in bright green; the rest stays pale grey."),
    "cordon":   (D, "a hooded sweatshirt, hood up. ONLY the two DRAWSTRING CORDS hanging from the hood "
                    "are drawn in bright red, slightly thicker than usual; the rest stays pale grey."),

    # ── Motifs qui demandent un dessin ───────────────────────────────────
    "fleuri":   (V, "a short-sleeved summer blouse with an all-over FLORAL PRINT: small pink and "
                    "yellow flowers with green leaves scattered on a white background."),
    "imprime":  (V, "a short-sleeved t-shirt with ONE large simple graphic printed in the middle of "
                    "the chest: a stylised orange sun over three blue wavy lines. No words, no letters."),

    # ── Tailles et coupes ────────────────────────────────────────────────
    "ajuste":   (V, "a slim-fit long-sleeved shirt in solid white, narrow and close to the body, "
                    "tapered at the waist, narrow sleeves."),
    "ample":    (V, "an oversized loose long-sleeved shirt in solid white, very wide and boxy, dropped "
                    "shoulders, wide sleeves, hanging loose."),
    "taille-haute": (V, "a pair of high-waisted wide-leg trousers in solid camel, the waistband sitting "
                    "very HIGH, well above where normal trousers stop, with a tall waistband and two "
                    "buttons."),

    # ── Le magasin ───────────────────────────────────────────────────────
    "cabine":   (O, "a single fitting room seen from the front: a small cubicle with a tall curtain in "
                    "deep teal half drawn, a small stool and a coat hook inside, a mirror on the back "
                    "wall. No sign above it."),
    "cintre":   (O, "one clothes hanger alone: a smooth wooden hanger in light natural wood, a curved "
                    "silver metal hook on top, a straight bar across the bottom."),
    "presentoir": (O, "a round display table in light wood on a single central pedestal, seen at a slight angle from above, with three neat stacks of folded sweaters in different colours (red, navy, cream) on its top. Nothing else: no hangers, no rail, no sign, no price."),
    "rayon":    (O, "a long straight clothing rail seen from the front, holding a row of ten shirts on "
                    "hangers in a gradient of colours from white to navy, on a low wooden shelf with "
                    "folded jeans below. No sign, no text."),
    "etiquette-prix": (O, "a blank rectangular cardboard price tag in kraft brown, a small hole at "
                    "the top with a short white string tied through it. The tag is completely BLANK: no "
                    "numbers, no letters, no barcode."),
    "antivol": (O, "a folded blue sweater seen from above, and clipped to its bottom edge a SMALL round grey plastic anti-theft security tag, about the size of a coin compared to the sweater, with a metal pin through the fabric."),
    "caisse":   (O, "a small shop checkout counter in light wood seen from the customer's side at "
                    "three-quarters: a black card payment terminal with its screen OFF and blank, a "
                    "closed cash drawer, a small stack of folded paper bags. No text, no sign."),
    "recu":     (O, "a long narrow paper shop receipt, slightly curled at the bottom. Instead of text, "
                    "only thin grey horizontal lines of different lengths. NO letters, NO numbers."),
    "sac":      (O, "a paper shopping bag in solid kraft brown with two twisted paper handles, standing, "
                    "seen from the front. Completely plain, no logo, no text."),
    "vitrine":  (O, "a clothing shop window seen from the street: a large glass pane in a dark green "
                    "frame, inside it two faceless display mannequins wearing a coat and a dress. No "
                    "sign, no lettering, no text on the glass."),
    "mannequin": (O, "one full-body faceless display mannequin in smooth white, standing straight on a "
                    "small round base, wearing a simple navy blue dress. The face is smooth, with no "
                    "features."),
    "miroir":   (O, "a tall standing full-length mirror in a thin black metal frame, on a small stand, "
                    "the glass drawn as pale blue with two diagonal light streaks, reflecting nothing."),
    "carte-cadeau": (O, "a blank plastic gift card in solid red with a small white ribbon bow drawn on "
                    "one corner. The card is completely BLANK: no words, no letters, no numbers, no "
                    "logo."),
}
