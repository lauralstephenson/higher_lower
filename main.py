import random
from art import logo, vs
from game_data import data
from replit import clear

# In our game we are comparing who has the higher number of Instagram hits


def get_random_account():
  """Get data from random account"""
  return random.choice(data)


#Format the account data into printable format
def format_data(account):
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
  #Use an if statement and follow counts and return if they got it right
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  #If the random choice is the same, pick another one
  while account_a == account_b:
    account_b = get_random_account()


#Make the game repeat
  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask the user for their A/B choice
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    #The follower_count must be compared for each choice
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    #Clear the screen between rounds
    clear()
    print(logo)
    #Correct/incorrect feedback and points
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      score -= 1
      #If the guess is wrong, end the game and display the score
      print(f"Sorry, that’s wrong. Final score: {score}.")

game()
