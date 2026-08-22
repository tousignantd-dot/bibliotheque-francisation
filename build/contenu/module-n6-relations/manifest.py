# -*- coding: utf-8 -*-
"""Identité de module-n6-relations — « Reprendre le fil » (niveau 6).

Situation « Relations sociales », niveau 6 (LAN-5069-8), activité 101,
`numero` 3 du niveau. Ce que `python3 build/cadre.py 6 "Relations sociales"`
donne, et rien d'autre — **quatre intentions**, une orale et trois écrites :

  · PO — décrire quelqu'un ;
  · CE — recevoir des nouvelles ;
  · PE — rédiger un courriel pour donner des nouvelles et raconter un
    évènement ;
  · PE — informer un destinataire par courriel du contenu d'un article
    d'intérêt général.

Trois défis, donc, et non deux : chacune de ces quatre intentions a son
dialogue et ses six exercices, et les trois défis sont **trois retours sur le
même dossier** — le courriel reçu, la personne à reconnaître, le courriel
écrit. C'est la règle du pilote du niveau (`docs/vagues-suivantes.md`, « Le
pilote du niveau 6 »), et le tableau des grilles y donne `GRILLE_3_DEFIS`
pour cette situation.

**Ce que le niveau 6 fait de cette situation.** Le niveau 5 raconte, le
niveau 7 démasque ; le niveau 6 **suit un fil**. Ce qui est difficile ici
n'est ni le vocabulaire ni le jugement : c'est la **cohésion** d'un texte
long. Un courriel de nouvelles de quatre paragraphes dit « on l'avait déjà
vendue », « je t'en reparlerai », « la ville où il travaille maintenant » — et
chaque fois, le petit mot renvoie à quelque chose écrit dix lignes plus haut.
Perdre le fil, ce n'est pas manquer un mot : c'est perdre à quoi il renvoie.
D'où les neuf savoirs retenus sur les cinquante-quatre du niveau, tous choisis
par la même question — *est-ce que ça sert à suivre un texte ?* :

  1. graphie-phonie : « ch » qui dit [k], « x » qui dit [s], « sh/sch » qui
     disent [ʃ] — savoir commun à tout le niveau (Je découvre) ;
  2. tenir compte de la présentation matérielle et de la mise en page — les
     parties d'un courriel (Je découvre) ;
  3. reprise de l'information : « le », « en », « y », les pronoms
     démonstratifs (Défi 1) ;
  4. indicatif plus-que-parfait : une action qui en précède une autre déjà
     passée (Défi 1) ;
  5. accord des adjectifs, et sens de l'adjectif selon sa place — grand,
     propre, ancien (Défi 2) ;
  6. subordonnée relative avec « où », et la structure Dét + nom + relative
     (Défi 2) ;
  7. indicatif passé simple : reconnaître les verbes courants à la
     3e personne et les associer au passé composé — en `match`, jamais en
     `write` : le programme demande de *reconnaître* (Défi 3) ;
  8. connecteurs et relations logiques (Défi 3) ;
  9. ponctuation : le tiret et les guillemets (Défi 3).

**D'où viennent les productions de « Je me lance ».** Les deux productions
écrites sont nommées par la situation elle-même — donner des nouvelles et
raconter un évènement, informer du contenu d'un article — et la production
orale est l'intention « décrire quelqu'un », reprise des attentes de fin de
cours du niveau : « durant un exposé, il décrit de façon détaillée les
caractéristiques physiques ». Rien n'est inventé hors programme.

Le lexique rattaché à la situation est vide, comme presque partout ; mais au
niveau 6 les savoirs lexicaux **du niveau** nomment la situation en deux
lignes, et les seize mots de `FC_CARDS` en sortent : « mots servant à décrire
physiquement une personne : visage allongé, doigts effilés, cheveux ondulés »
et « mots en rapport avec les évènements racontés : naissance, mariage,
enterrement, accident, voyage ».

**Les cinq voisins de la même situation, et ce qui l'en sépare.** Aucun n'est
copié, aucun n'est répété — ce qui change n'est pas le sujet, c'est le
travail :

· `module-n1-presenter` (niveau 1) apprend à dire son nom et à l'épeler.
  Ici, personne ne se présente : les gens se connaissent depuis sept ans.
· `module-n2-bonjour` (niveau 2) tient un échange de deux ou trois répliques
  dans l'entrée d'un immeuble. Ici, un seul courriel fait quatre paragraphes.
· `module-n3-voisins` (niveau 3) tient le lien court et régulier de
  l'escalier : inviter, complimenter, demander une permission. Il décrit lui
  aussi une personne — mais pour retrouver un objet perdu, en trois adjectifs.
  Ici, la description doit suffire à reconnaître quelqu'un dans un terminus,
  et elle est reprise, corrigée, précisée en cours de conversation.
· `module-relations` (niveau 4) raconte une expérience vécue à quelqu'un
  qu'on vient de rencontrer, au passé composé et à l'imparfait. Ici, on ne
  raconte pas à un inconnu : on **reprend** deux ans de nouvelles avec
  quelqu'un qui en connaît déjà la moitié, ce qui oblige à dire ce qui était
  déjà arrivé avant le reste — le plus-que-parfait, et non le passé composé.
· `module-n5-voisinage` (niveau 5) organise une fête de ruelle : accepter,
  refuser, féliciter, laisser un message. Tout s'y joue en quelques phrases.
  Ici, il n'y a rien à organiser et personne à convaincre : il y a un texte
  long à suivre sans en perdre le fil, et un autre à écrire en paragraphes.

Les faits du Québec sont vérifiés plutôt que devinés : Saint-Hyacinthe et
Rouyn-Noranda existent, la distance et le trajet d'autobus qui les sépare
aussi, et la « Table de quartier » est le nom courant des concertations de
quartier au Québec. Tout le reste est **inventé** : Marisol Quintanilla,
Ousmane Diallo, Ghislain Bourbeau, Kadiatou Diallo, la boulangerie Trottier,
le journal « L'Écho de la Yamaska », l'organisme « Le Fil d'ici », les dates,
les heures et les adresses. Un article attribué à un vrai journal serait une
fausse nouvelle ; un organisme réel à qui l'on prête un programme inventé
serait pire.
"""

MANIFESTE = {
    'slug': 'module-n6-relations',

    # `titre` et `niveau` viennent de `build/powerpoints/modules.py`, source
    # unique. Le build s'arrête si un manifeste les contredit.

    'theme': 'Relations sociales',

    # Acier : la couleur du niveau 6. Elle ne se choisit pas — c'est celle du
    # niveau, et `build/couleurs_niveau.py --verifier` la contrôle.
    'accent': '#1D6B8F',
    'accent_doux': '#E7F0F6',

    'ia_oral': "L'élève décrit une personne à quelqu'un qui ne l'a jamais "
               "vue et qui doit la reconnaître dans une foule : il donne "
               "d'abord la silhouette et l'âge approximatif, puis le visage "
               "et les cheveux en détail, puis un signe particulier et ce que "
               "la personne portera. Il emploie des adjectifs accordés, au "
               "moins une subordonnée relative avec « qui », « que » ou "
               "« où », et il termine par ce qui permettrait de ne pas se "
               "tromper. Il tutoie son interlocuteur.",

    'jr_cas': 'terminus',
    'jr_role': 'marisol',
    'jr_scenario': 'reconnaitre',
    'ia_jeu_de_role': "L'élève décrit une personne à quelqu'un qui va la "
                      "chercher au terminus : il donne les caractéristiques "
                      "physiques dans un ordre utile, il répond aux "
                      "demandes de précision sans se contredire, il corrige "
                      "ce qu'il a dit d'inexact, et il reprend l'information "
                      "sans tout répéter.",

    'bravo': "🎉 Bravo, tu as terminé le module « Reprendre le fil » !",
    'relance': "Tu peux revenir sur n\\'importe quel onglet pour pratiquer "
               "encore.",

    'residus_interdits': ['module-consultation', 'Yannick', 'Rosalie', 'Beaulieu',
                          'tendinite', 'Consulter au bon endroit', 'physiothérapie'],
}
