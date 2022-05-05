import random
import art
import game_data

def random_person():
  '''Pulls data from random account'''
  return random.choice(list(game_data.data))

# create a function to check who has more followers
def greater_followers(first_followers, second_followers):
  '''Checks which person has more followers'''
  if first_followers > second_followers:
    return "a"
  elif first_followers < second_followers:
    return "b"

#create a function that compares the player's guess to the actuals
#def guess_checker(player_guess, most_followers, score, game_continues):


def game():
  '''Runs the guessing game'''
  #initialize variables
  game_continues = True
  score = 0
  
  #import game art
  print(art.logo)
  
  #state game objective
  print("The object of the game is to correctly guess which entity has more followers.")
  
  #grab a random person from the dictionary
  first_person = random_person()
  
  while game_continues:
    #print a string containing info about this person
    print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
    
    #print the 'vs' logo
    print(art.vs)
    
    #grab a second person from the dictionary
    second_person = random_person()

    #grabs a new person if the 1st and 2nd person are the same
    while first_person == second_person:
      second_person = random_person()
    
    #assign follower count to int variables
    first_followers = int(first_person['follower_count'])
    second_followers = int(second_person['follower_count'])
    
    #print a string containing info about this 2nd person
    print(f"Compare A: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")
    
    #ask player to decide who has more followers
    player_guess = input("Who has more followers? A or B? ").lower()
    
    #calculate who actually has more followers
    correct_answer = greater_followers(first_followers, second_followers)
    
    #check guess against correct answer
    if player_guess == correct_answer:
      print(f"Correct! Your current score is {score}.")
      score += 1
      first_person = second_person
    if player_guess != correct_answer:
     print(f"Incorrect! Game over. Your score is {score}.")
     game_continues = False

game()
  
