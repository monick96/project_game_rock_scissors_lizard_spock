import random

options = ("rock", "paper", "scissors", "lizard", "spock")

wins = 3
count_wins_player = 0
count_wins_computer = 0

def player_attack():
    attack = input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()
    # validate user input with while
    while(not (attack in options)):
            print("wrong option")
            attack = input("Choose an option: Rock, Paper, Scissors, Lizard or Spock => ").lower()
    #other ways to validate user input with while
    """
    while user_option != "rock"and user_option != "paper" and user_option !="scissors"and user_option!= "lizard"and user_option!= "spock":
        print(f"{user_name} enter a valid option")
        user_option= input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()


    while(True):
        if user_option in options:
                break
        else:
                print("wrong option")
                user_option = input("Choose an option: Rock, Paper, Scissors, Lizard or Spock => ").lower()

    """
    return attack

def computer_attack(computer_option):
    if computer_option == "rock":
        return "the computer has chosen: Rock"
    elif computer_option == "paper":
        return "the computer has chosen: Paper"
    elif computer_option == "scissors":
        return "the computer has chosen: Scissors" 
    elif computer_option == "lizard":
        return "the computer has chosen: Lizard"
    elif computer_option == "spock":
        return "the computer has chosen: Spock"
    
def combat(user_option,computer_option):
    global count_wins_player
    global count_wins_computer
    if user_option == computer_option:
        return "This is a draw!"
    elif user_option == "rock":
        if computer_option == "scissors":
            count_wins_player += 1
            return "rock breaks scissor, you win! 🎉 "
        elif computer_option == "lizard":
            count_wins_player += 1
            return "Rock crushes lizard, you win! 🎉"
        else:
            count_wins_computer += 1
            return "Computer win, you lose 😢 !"
    elif user_option == "paper":
        if computer_option == "rock" :
            count_wins_player += 1
            return "Paper covers stone, you win! 🎉"
        elif computer_option == "spock":
            count_wins_player += 1
            return "Paper overrules Spock, you win! 🎉"
        else:
            count_wins_computer += 1
            return "Computer win, you lose 😢 !"
    elif user_option == "scissors":
        if computer_option == "paper":
            count_wins_player += 1
            return "Scissors cut paper, you win! 🎉"
        elif computer_option == "lizard":
            count_wins_player += 1
            return "Scissors decapitates lizard, you win! 🎉"
        else:
            count_wins_computer += 1
            return "Computer win, you lose 😢 !"
    elif user_option == "lizard":
        if computer_option == "paper":
            count_wins_player += 1
            return "Lizard devours paper, you win! 🎉"
        elif computer_option == "spock":
            count_wins_player += 1
            return "Lizard poisons Spock, you win! 🎉"
        else:
            count_wins_computer += 1
            return "Computer win, you lose 😢 !"
    elif user_option == "spock":
        if computer_option == "scissors":
            count_wins_player += 1
            return "Spock breaks scissors, you win! 🎉"
        elif computer_option == "rock":
            count_wins_player += 1
            return "Spock vaporizes rock, you win! 🎉"
        else:
            count_wins_computer += 1
            return "Computer win, you lose 😢 !"
        
    
print(""" 
      English Description:
      Welcome to "Rock, paper, scissors, lizard, Spock"
      🥌 📋 ✂ 🦎 🖖
      Rules:
      
      *Scissors cut paper
      *Paper covers stone
      *Rock crushes lizard
      *Lizard poisons Spock
      *Spock breaks scissors
      *Scissors decapitates lizard
      *Lizard devours paper
      *Paper overrules Spock
      *Spock vaporizes stone
      *And as always, rock breaks scissor
      ---------------------------------------------------
      Descripción en Español
      
      Bienvenidos a "Piedra, papel, tijera, lagarto, Spock"
      🥌 📋 ✂ 🦎 🖖
       Reglas:
      
       *Tijeras cortan papel
       *Papel cubre piedra
       *Piedra aplasta lagarto
       *Lagarto envenena a Spock
       *Spock rompe tijeras
       *Tijeras decapitan lagarto
       *Lagarto devora papel
       *El papel desautoriza a Spock
       *Spock vaporiza piedra
       *Y como siempre, piedra rompe tijera
      ---------------------------------------------------
      """)


user_name = input("Enter your name => ")
print(f"you must defeat {wins} times to win")

while ((count_wins_player < wins) and (count_wins_computer < wins)):

    user_option = player_attack()
    
    print(f"{user_name} you have selected: {user_option} \n")
    print("Now it's the computer's turn")

    """
    0=rock 1=paper 2=scissors 3=lizard 4=spock
    """
    #random option assignment from option list
    #computer_option = options[random.randint(0, 4)]
computer_option = random.choice(options)

#print computer option
print(computer_attack(computer_option))

print("---------------------------------------")

#combat
print(combat(user_option,computer_option), "\n")

print(f"The player {user_name} wins {count_wins_player} times, computer wins {count_wins_computer} times. \n")

#final message
if count_wins_player == wins:
    print("🎉 CONGRATULATIOS YOU ARE THE WINNER 🎉 \n")
elif count_wins_computer == wins:
    print("😢 Sorry you are the Loser 😢 \n")
