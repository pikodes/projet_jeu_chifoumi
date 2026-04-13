import random # Importation pour permettre à l'IA de faire des choix aléatoires

# Définition des constantes pour éviter les erreurs de saisie et faciliter la lecture
PIERRE = 1
PAPIER = 2
CISEAUX = 3

# Dictionnaire de correspondance pour un affichage plus convivial avec des Emojis
CHOICES = {
    PIERRE: "Pierre ✊",
    PAPIER: "Papier ✋",
    CISEAUX: "Ciseaux ✌️"
}

def get_winner(choice1, choice2):
    """
    Détermine le gagnant d'une manche unique.
    Logique : 1 bat 3, 2 bat 1, 3 bat 2.
    """
    if choice1 == choice2:
        return 0 # Retourne 0 en cas d'égalité
    # Vérification des conditions de victoire pour le joueur 1
    if (choice1 == PIERRE and choice2 == CISEAUX) or \
       (choice1 == PAPIER and choice2 == PIERRE) or \
       (choice1 == CISEAUX and choice2 == PAPIER):
        return 1 # Joueur 1 gagne
    return 2 # Sinon, c'est le joueur 2 qui gagne

def play_match(player1, player2, best_of=3):
    """
    Gère un match complet entre deux joueurs en "3 manches gagnantes" (Best of 3).
    """
    print(f"\n--- MATCH : {player1['name']} VS {player2['name']} ---")
    score1 = 0 # Score initial du joueur 1
    score2 = 0 # Score initial du joueur 2
    needed_to_win = (best_of // 2) + 1 # Calcul du nombre de manches nécessaires pour gagner (2 pour un Best of 3)
    
    # La boucle continue tant qu'aucun joueur n'a atteint le score victorieux
    while score1 < needed_to_win and score2 < needed_to_win:
        print(f"\nScore actuel : {player1['name']} {score1} - {score2} {player2['name']}")
        
        # Gestion du choix du joueur 1 (IA ou Humain)
        if player1['is_ai']:
            choice1 = random.randint(1, 3) # Choix aléatoire pour l'IA
        else:
            choice1 = get_player_choice(player1['name']) # Saisie utilisateur pour l'humain
            
        # Gestion du choix du joueur 2 (IA ou Humain)
        if player2['is_ai']:
            choice2 = random.randint(1, 3)
        else:
            choice2 = get_player_choice(player2['name'])
            
        # Affichage des choix faits par chacun
        print(f"{player1['name']} a choisi {CHOICES[choice1]}")
        print(f"{player2['name']} a choisi {CHOICES[choice2]}")
        
        # Détermination du vainqueur de la manche
        winner = get_winner(choice1, choice2)
        if winner == 1:
            print(f"Manche remportée par {player1['name']} !")
            score1 += 1 # Incrémentation du score du vainqueur
        elif winner == 2:
            print(f"Manche remportée par {player2['name']} !")
            score2 += 1
        else:
            print("Égalité ! On recommence la manche.")
            
    # Fin du match : on retourne le gagnant et le perdant pour la gestion du tournoi
    if score1 > score2:
        print(f"\n🏆 {player1['name']} remporte le match !")
        return player1, player2
    else:
        print(f"\n🏆 {player2['name']} remporte le match !")
        return player2, player1

def get_player_choice(name):
    """
    Saisie sécurisée pour le choix d'un joueur humain.
    """
    while True: # Boucle infinie jusqu'à une saisie valide
        try:
            print(f"\n{name}, c'est à vous !")
            choice = int(input("Choisissez : 1 (Pierre), 2 (Papier), 3 (Ciseaux) : "))
            if choice in [1, 2, 3]:
                return choice # Retourne le choix si valide
            print("Choix invalide. Veuillez choisir 1, 2 ou 3.")
        except ValueError: # Gestion d'erreur si l'utilisateur n'entre pas un nombre
            print("Veuillez entrer un nombre valide.")
