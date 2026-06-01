import random

print("This is a Stone, Paper, Scissors Game!")

print("You have given three choices you have to choose one at once. Choices are:\n - Stone\n - Paper \n - Scissors")

choices = ["Paper", "Stone", "Scissors"]


while True: 
    try: 

        computer = random.choice(choices)
        user = input("Enter your choice here: ").capitalize()


        if user == "Stone" and computer == "Stone":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("It's a tie!")

        elif user == "Paper" and computer == "Scissors":
            print(f"You have chosen {user} and computer had chosen {computer}")
            print("Computer won!")

        elif user == "Scissors" or "Scisors" and computer == "Paper":
            print(f"You have chosen {user} and the computer had chosen {computer}")
            print("You won!")

        elif user == "Stone" and computer == "Paper":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("Computer won!")

        elif user == "Paper" and computer == "Paper":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("It's a tie!")

        elif user == "Scissors" or "Scisors" and computer == "Stone":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("Computer won!")

        elif user == "Scissors" or "Scisors" and computer == "Scissors":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("It's a tie!")

        elif user == "Paper" and computer == "Stone":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("You won!")

        elif user == "Stone" and computer == "Scissors":
            print(f"You have chosen {user} and computer has chosen {computer}")
            print("You won!")

        elif user == "quit" or "exit":
            print("Game over!")
            break
        print("Game executed successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    


















