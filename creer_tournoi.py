from le_jeux import play_match # Importation de la fonction de match pour l'utiliser ici
import random # Pour mélanger les joueurs au début

def initialize_players(total_participants, human_participants):
    """
    Crée la liste des joueurs (Humains + IA) et les mélange pour le tirage au sort.
    """
    players = []
    # Création des joueurs humains avec leurs noms personnalisés
    for i in range(human_participants):
        name = input(f"Nom du joueur humain {i+1} : ")
        players.append({"name": name, "is_ai": False}) # Stockage sous forme de dictionnaire
    
    # Remplissage automatique avec des IA pour atteindre le nombre total de participants
    for i in range(total_participants - human_participants):
        players.append({"name": f"IA-{i+1}", "is_ai": True})
        
    random.shuffle(players) # Mélange aléatoire pour simuler un tirage au sort de tournoi
    return players

def display_bracket(players):
    """
    Affiche les premiers affrontements prévus.
    """
    print("\n--- TABLEAU INITIAL DU TOURNOI ---")
    n = len(players)
    # On parcourt la liste deux par deux pour former les duos de matches
    for i in range(0, n, 2):
        print(f"Match {i//2 + 1}: {players[i]['name']} vs {players[i+1]['name']}")

def run_tournament(players):
    """
    Algorithme principal de gestion des tours (Élimination directe).
    """
    current_round_players = players
    # Noms des phases en fonction du nombre de joueurs restants
    rounds_name = {16: "Huitièmes de finale", 8: "Quarts de finale", 4: "Demi-finales"}
    
    semi_final_losers = [] # Liste pour stocker les perdants des demies (pour le match de 3e place)
    final_loser = None # Pour stocker le perdant de la finale (2e place)
    
    # Tant qu'il reste plus d'un joueur, le tournoi continue
    while len(current_round_players) > 1:
        n = len(current_round_players)
        round_label = rounds_name.get(n, "FINALE") # "Finale" si n=2
        print(f"\n{'='*10} {round_label.upper()} {'='*10}")
        
        winners = [] # Liste des gagnants qui passeront au tour suivant
        for i in range(0, n, 2):
            p1 = current_round_players[i]
            p2 = current_round_players[i+1]
            
            # Exécution du match entre p1 et p2
            winner, loser = play_match(p1, p2)
            winners.append(winner) # Le gagnant avance
            
            # Cas spécial : Stockage des perdants des demi-finales pour la petite finale
            if n == 4:
                semi_final_losers.append(loser)
            # Cas spécial : Stockage du perdant de la finale pour la 2e place du podium
            if n == 2:
                final_loser = loser
                
        current_round_players = winners # Les gagnants deviennent les joueurs du tour suivant
        
    final_winner = current_round_players[0] # Le dernier gagnant restant est le champion
    
    # Match pour la 3ème place (Petite finale) entre les deux perdants des demies
    print(f"\n{'='*10} MATCH POUR LA 3ème PLACE {'='*10}")
    third_place_winner, fourth_place = play_match(semi_final_losers[0], semi_final_losers[1])
    
    # On retourne les 3 premiers pour le podium
    return final_winner, final_loser, third_place_winner

def display_podium(first, second, third):
    """
    Affichage final des résultats avec médailles.
    """
    print("\n" + "="*30)
    print("      🏆 PODIUM FINAL 🏆")
    print("="*30)
    print(f"🥇 1ère place : {first['name']}")
    print(f"🥈 2ème place : {second['name']}")
    print(f"🥉 3ème place : {third['name']}")
    print("="*30)
