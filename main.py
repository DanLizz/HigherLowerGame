import art
import random
import game_data as gd
import replit

#generating two persons randomly
def generate_person():
  return random.choice(gd.data)

def continue_game(score,level):
  level = True
  score = score+1
  print(f"You're right! Current score: {score}.")
  replit.clear()
  return level

def stop_game(score,level):
  level = False
  print(f"Sorry, that's wrong. Final Score: {score}")
  return level


print(art.logo)
level = True
score = 0
A = generate_person()

while(level):

  B = generate_person()
  while A == B:
    B = generate_person()

  print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
  print(art.vs)
  print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}.")

  guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
  
  invalid = guess != 'A' and guess !='B'

  while invalid:
    guess = input("Invalid input.Select A or B: ").capitalize()
    invalid = guess != 'A' and guess !='B'

  if guess == 'A' and A['follower_count'] >= B['follower_count']:
    level = continue_game(score,level)
  elif guess == 'B' and B['follower_count'] >= A['follower_count']:
    level = continue_game(score,level)
    A = B
  else:
    level = stop_game(score,level)
  