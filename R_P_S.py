import random

def play():
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'tie'
    if is_win(user, computer):
        return 'you win'
    return 'you lost'
    
    #'r' > 's', 'p' > 'r', 's' > 'p'

def is_win(player, opponent):
    if( player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') \
        or (player == 's' and opponent == 'p'):
        return True
    
print(play())
        
