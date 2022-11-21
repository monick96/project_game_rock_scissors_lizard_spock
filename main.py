import random

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
    if user_option == computer_option:
        return "This is a draw!"
    elif user_option == "rock":
        if computer_option == "scissors":
            return "rock breaks scissor, you win! 🎉 "
        elif computer_option == "lizard":
            return "Rock crushes lizard, you win! 🎉"
        else:
            return "Computer win, you lose 😢 !"
    elif user_option == "paper":
        if computer_option == "rock" :
            return "Paper covers stone, you win! 🎉"
        elif computer_option == "spock":
            return "Paper overrules Spock, you win! 🎉"
        else:
            return "Computer win, you lose 😢 !"
    elif user_option == "scissors":
        if computer_option == "paper":
            return "Scissors cut paper, you win! 🎉"
        elif computer_option == "lizard":
            return "Scissors decapitates lizard, you win! 🎉"
        else:
            return "Computer win, you lose 😢 !"
    elif user_option == "lizard":
        if computer_option == "paper":
            return "Lizard devours paper, you win! 🎉"
        elif computer_option == "spock":
            return "Lizard poisons Spock, you win! 🎉"
        else:
            return "Computer win, you lose 😢 !"
    elif user_option == "spock":
        if computer_option == "scissors":
            return "Spock breaks scissors, you win! 🎉"
        elif computer_option == "rock":
            return "Spock vaporizes rock, you win! 🎉"
        else:
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
user_option = input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()
options = ["rock", "paper", "scissors", "lizard", "spock"]

# validate user input with while
while(not (user_option in options)):
            print("wrong option")
            user_option = input("Choose an option: Rock, Paper, Scissors, Lizard or Spock => ").lower()


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
    
print(f"{user_name} you have selected: {user_option} \n")
print("Now it's the computer's turn")

"""
1 =rock 2=paper 3=scissors 4=lizard 5=spock
"""
#random option assignment from option list
computer_option = options[random.randint(0, 4)]

#print computer option
print(computer_attack(computer_option))

print("---------------------------------------")

#combat
print(combat(user_option,computer_option))
