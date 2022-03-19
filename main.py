import random

def set_user_choice(user_string):
  return{
      'rock': 1,
      'paper': 2,
      'scissors': 3
  }.get(user_string, 0)

def compare_ai_and_user(user, ai):
  if (user == ai):
    return "It's a tie, you and a computer both chose the same result."
  elif user == 1:
    if (ai == 2):
      return "You lose."
    else:
      return "You won!"
  elif user == 2:
     if (ai == 3):
      return "You lose."
     else:
      return "You won!"
  elif user == 3:
     if (ai == 1):
      return "You lose."
     else:
      return "You won!"
  else:
    return "Something broke, sorry!"

user_choice_string = input("Enter your choice: rock, paper or scissors.\n")
user_choice = set_user_choice(user_choice_string)

if user_choice == 0:
  print ("You entered your choice incorrectly, please rerun the program and try again. Write \"rock\", \"scissors\" or \"paper\" as a choice.")
  exit()
else:
  random.seed;
  ai_choice = random.randint(1,3)
  result = compare_ai_and_user(user_choice, ai_choice)
  print(result)


