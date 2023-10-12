import random

def choose_option(userPoint, computerPoint, rounds):
  print('*' * 10)
  print(f'--Game summary-- User => {userPoint}.  computer => {computerPoint}')
  print('*' * 10)
  print(f'Round number => ', rounds)
  print('-' * 10)
#select option
  options  = ('stone', 'paper', 'scissors')
  user = input('Stone, Paper or scissors => ').lower()
  computer = random.choice(options)
  if not user in options:
    print('This option is not defined. Try again...')
    print(' ')
    return None, None
  return user, computer

def check_rules(user, computer, userPoint, computerPoint, rounds):
  #print(f'The user chose => {user}. the computer chose => {computer}')
  print(f'computadora = {computer}')
  print(' ')
  if user == computer :
    rounds += 1
    print('empate')
    print(' ')
    print(' ')
  elif user == 'stone' and computer == 'scissors':
    print('user wins')
    userPoint += 1
    rounds += 1
    print(' ')
    print(' ')
  elif user == 'paper' and computer == 'stone':
    print('user wins')
    userPoint += 1
    rounds += 1
    print(' ')
    print(' ')
  elif user == 'scissors' and computer == 'paper':
    print('user wins')
    userPoint += 1
    rounds += 1
    print(' ')
    print(' ')
  else:
    print('computer wins')
    computerPoint += 1
    rounds += 1
    print(' ')
    print(' ')
  return userPoint, computerPoint, rounds

def check_winers(userPoint, computerPoint):
  if userPoint == 3:
    print('user is the absolute winer.. ')
    print(f'Summary of the battle user wins {userPoint}   And computer wins {computerPoint}')
  elif computerPoint == 3:
    print('computer is the absolute winer.. ')
    print(f'Summary of the battle user wins {userPoint}   And computer wins {computerPoint}')

def run_game():
  userPoint = 0
  computerPoint = 0
  rounds = 1
  while (userPoint < 3) and (computerPoint < 3):
    user, computer = choose_option(userPoint, computerPoint, rounds)
    userPoint, computerPoint, rounds = check_rules(user, computer, userPoint, computerPoint, rounds)
    check_winers(userPoint, computerPoint)

run_game()