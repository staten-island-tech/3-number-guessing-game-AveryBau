import random
print(random.randint(1,10))


guess_history = []
guess = int(input("guess a number 1-10"))
guess_history.append(guess)
def we(guess, random):
    global_guess = 0
    for i in range(1,10):
        if guess == random:
            print("correct") 
        elif guess < random:
            print("higher")
            guess_history.append(guess)
        elif guess > random:
            print("lower")
            guess_history.append(guess)







