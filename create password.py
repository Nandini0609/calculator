import random

def user_choice():
    print("Choose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Enter your choice (1/2/3): "))
    while choice not in [1, 2, 3]:
        print("Invalid choice. Please select 1, 2 or 3.")
        choice = int(input("Enter your choice (1/2/3): "))
    return ["Rock", "Paper", "Scissors"][choice - 1]

def computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "Tie"
    if (user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock"):
        return "User"
    return "Computer"

def main():
    user_score = 0
    computer_score = 0
    while True:
        print("\n*** Rock, Paper, Scissors ***\n")
        user = user_choice()
        comp = computer_choice()
        print(f"You chose {user}. Computer chose {comp}.")
        winner = determine_winner(user, comp)
        if winner == "User":
            print("You Win!")
            user_score += 1
        elif winner == "Computer":
            print("You Lose!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"\nScore: User - {user_score} | Computer - {computer_score}")

        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == "__main__":
    main()
