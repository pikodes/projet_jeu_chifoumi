
from saisie_entree import saisie
from joueur_match import joueur_match
from generation_poule import generation_poule

participants_partie,joueurs=saisie()
joueur_de_partie ,joueur_machine=joueur_match(participants_partie,joueurs)

generation_poule(joueur_de_partie ,joueur_machine)


      