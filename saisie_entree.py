def get_tournament_config():
    """
    Récupère la configuration du tournoi auprès de l'utilisateur.
    """
    # Boucle pour valider le nombre total de participants
    while True:
        try:
            total = int(input("Choisissez le nombre total de participants (4, 8, 16) : "))
            if total in [4, 8, 16]: # Seuls les formats standards sont acceptés
                break
            print("Choix invalide. Veuillez choisir 4, 8 ou 16.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            
    # Boucle pour valider le nombre d'humains
    while True:
        try:
            humans = int(input(f"Combien d'humains participent (max {total}) ? : "))
            if 0 <= humans <= total: # Doit être entre 0 et le total choisi
                break
            print(f"Nombre invalide. Veuillez entrer un nombre entre 0 et {total}.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            
    return total, humans # Retourne les paramètres de configuration
