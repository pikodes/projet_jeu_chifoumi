
from saisie_entree import saisie,saisie_jeu_poule,saisie_jeu_elim
from joueur_match import joueur_match
from generation_poule import generation_poule
from calcul_point import calcul_point_poule,calcul_point_elim
from le_jeux import le_jeux

#entrée des participants
participants_partie,joueurs=saisie()
joueur_de_partie ,joueur_machine=joueur_match(participants_partie,joueurs)

#creation de poule
le_jeux(generation_poule(joueur_de_partie ,joueur_machine))

#affrontement phase poule
calcul_point_poule(saisie_jeu_poule())
 

#affrontement phase eliminatoire
calcul_point_elim(saisie_jeu_elim())









      