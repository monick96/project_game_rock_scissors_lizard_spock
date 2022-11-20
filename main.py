print(''' 
      English Description:
      Welcome to "Rock, paper, scissors, lizard, Spock"
      🥌 📋 ✂ 🦎 🖖
      Rules:
      
      *Scissors cut paper
      *Paper covers stone
      *Stone crushes lizard
      *Lizard poisons Spock
      *Spock breaks scissors
      *Scissors decapitates lizard
      *Lizard devours paper
      *Paper overrules Spock
      *Spock vaporizes stone
      *And as always, stone breaks scissor
      ---------------------------------------------------
      Descripción en Español
      
      Bienvenidos a "Piedra, papel, tijera, lagarto, Spock"
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

user_name = input('Enter your name => ')
user_option= input("Choose an option: Rock, paper, scissors, lizard or Spock => ").lower()
print(f'{user_name} you have selected: {user_option} \n')
print("Now it's the computer's turn")

'''
1 =rock 2=paper 3=scissors 4=lizard 5=spock
'''
computer_option = 0
if computer_option == 1:
    print(f"the computer has chosen: rock")
