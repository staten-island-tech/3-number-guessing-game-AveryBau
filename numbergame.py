import random
random_number = (random.randint(1,10))
guess_history = []
guess = 0

while guess != random_number:
    guess = int(input("guess a number 1-10"))
       
    if guess < random_number:
            guess_history.append(guess)
            print("higher", guess_history)
    elif guess > random_number:
            guess_history.append(guess) 
            print("lower", guess_history)
if guess == random_number:
              print("correct", guess_history)




