from saisie_entree import get_tournament_config
from creer_tournoi import initialize_players, display_bracket, run_tournament, display_podium

def main():
    """
    Fonction principale qui orchestre le tournoi.
    Suit les 5 étapes du cycle de vie de l'application.
    """
    print("=== Bienvenue dans le Tournoi Chifoumi Pro ===")
    print("Règles : Matches en 3 manches gagnantes (Best of 3).")
    
    # ÉTAPE 1 : Configuration (Nombre de joueurs total et humains)
    total_participants, human_participants = get_tournament_config()
    
    # ÉTAPE 2 : Initialisation (Création et mélange des joueurs)
    players = initialize_players(total_participants, human_participants)
    
    # ÉTAPE 3 : Affichage du Bracket (Tableau initial)
    display_bracket(players)
    
    # ÉTAPE 4 : Déroulement (Lancement des matches jusqu'à la finale)
    winner, runner_up, third_place = run_tournament(players)
    
    # ÉTAPE 5 : Résultats (Affichage du podium final)
    display_podium(winner, runner_up, third_place)

if __name__ == "__main__":
    # Point d'entrée standard Python pour exécuter le script
    main()
