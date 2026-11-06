
import random

def play():
    possible_choices = ["pierre", "papier", "ciseaux"]

    wins = 0
    losses = 0

    while wins < 3 and losses < 3:

        user_choice = input("Choisissez Pierre, Papier ou Ciseaux: ").lower()

        if user_choice not in possible_choices:
            print("Choix invalide!")
            continue

        computer_choice = random.choice(possible_choices)

        print(f"Vous avez choisi: {user_choice}")
        print(f"L'ordinateur a choisi: {computer_choice}")

        if user_choice == computer_choice:
            print("C'est une égalité!")

        elif (
            (user_choice == "pierre" and computer_choice == "ciseaux")
            or (user_choice == "papier" and computer_choice == "pierre")
            or (user_choice == "ciseaux" and computer_choice == "papier")
        ):
            print("Vous gagnez!")
            wins += 1

        else:
            print("Vous perdez!")
            losses += 1

        print(f"Vos victoires: {wins}")
        print(f"Vos défaites: {losses}")

    if wins == 3:
        print("Félicitations! Vous avez gagné la partie!")

    else:
        print("Game Over! Vous avez perdu la partie!")


play()
