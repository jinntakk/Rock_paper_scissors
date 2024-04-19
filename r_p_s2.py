import random

user_score = 0
computer_score = 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("(R)ock/(P)aper/(S)cissors? OR Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    # 0 is rock 1 is paper 2 is scissor
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}!")
    if user_input == options[0] and computer_pick == options[2]:
        print("You win!")
        user_score += 1
    elif user_input == options[1] and computer_pick == options[0]:
        print("You win!")
        user_score += 1
    elif user_input == options[2] and computer_pick == options[1]:
        print("You win!")
        user_score += 1
    elif user_input == computer_pick:
        print("Tie!")
    else:
        print("You lost!")
        computer_score += 1

print(f"You won {user_score} times and computer won {computer_score} times.")
print("Goodbye!")

