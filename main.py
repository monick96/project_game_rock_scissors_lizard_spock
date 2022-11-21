import random
 
      
print(''' 
      English Description:
      Welcome to 'Rock, paper, scissors, lizard, Spock'
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
      
      Bienvenidos a 'Piedra, papel, tijera, lagarto, Spock'
       Normas:
      
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
      ''')

options = ['rock', 'paper', 'scissors', 'lizard', 'spock']

user_name = input('Enter your name => ')
user_option = input('Choose an option: Rock, Paper, Scissors, Lizard or Spock => ').lower()

while(not (user_option in options)):
            print('wrong option')
            user_option = input('Choose an option: Rock, Paper, Scissors, Lizard or Spock => ').lower()

# while(True):
#       if user_option in options:
#             break
#       else:
#             print('wrong option')
#             user_option = input('Choose an option: Rock, Paper, Scissors, Lizard or Spock => ').lower()



print(f'{user_name} you have selected: {user_option} \n')
print("Now it's the computer's turn")

'''
1 =rock 2=paper 3=scissors 4=lizard 5=spock
'''
computer_option = options[random.randint(0, 4)]

if computer_option == 'rock':
    print(f'the computer has chosen: {options[0]}')
elif computer_option == 'paper':
    print(f'the computer has chosen: {options[1]}')
elif computer_option == 'scissors':
    print(f'the computer has chosen: {options[2]}') 
elif computer_option == 'lizard':
    print(f'the computer has chosen: {options[3]}')
elif computer_option == 'spock':
    print(f'the computer has chosen: {options[4]}')

print('---------------------------------------')

#combat
if user_option == computer_option:
    print(f'This is a draw!')
elif user_option == 'rock':
    if computer_option == 'scissors':
        print('rock breaks scissor, you win!')
    elif computer_option == 'lizard':
        print('Rock crushes lizard, you win')
    else:
        print('Computer win, you lose :( !')
elif user_option == 'paper':
    if computer_option == 'rock' :
        print('Paper covers stone, you win!')
    elif computer_option == 'spock':
        print('Paper overrules Spock, you win')
    else:
        print('Computer win, you lose :( !')
elif user_option == 'scissors':
    if computer_option == 'paper':
        print('Scissors cut paper, you win!')
    elif computer_option == 'lizard':
        print('Scissors decapitates lizard, you win')
    else:
        print('Computer win, you lose :( !')
elif user_option == 'lizard':
    if computer_option == 'paper':
        print('Lizard devours paper, you win!')
    elif computer_option == 'spock':
        print('Lizard poisons Spock, you win')
    else:
        print('Computer win, you lose :( !')
elif user_option == 'spock':
    if computer_option == 'scissors':
        print('Spock breaks scissors, you win!')
    elif computer_option == 'rock':
        print('Spock vaporizes rock, you win')
    else:
        print('Computer win, you lose :( !')
else:
    print('You choose is invalid!')
    