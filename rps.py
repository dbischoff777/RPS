import random


def RSP():
    print("Let's play a little game")

    r = "Rock"
    p = "Paper"
    s = "Scissors"
    all_choices = [r, p, s]

    user = input(f"Enter a choice ({r}, {p}, {s}): ")

    if user not in all_choices:
        print("Invalid choice")
        return

    computer = random.choice(all_choices)

    print(f"User chose {user} and computer chose: {computer}")

    if user == computer:
        print("Tie")
    elif (user == r and computer == s) or (user == p and computer == r) or (user == s and computer == p):
        print("You won!")
    else:
        print("You lost!")

if __name__ == "__main__":
    RSP()

