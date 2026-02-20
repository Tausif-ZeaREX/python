import random
random_number = random.randint(0,100) 
guesses = 0
guess_answer = 0

def user_guess():
    guess = int(input('Guess a integer value between 0 and 100:'))
    return guess
guess_answer = user_guess()

while guess_answer != random_number:
    if  guess_answer > random_number:
        print('Go lower')
        guesses += 1
        guess_answer = user_guess()
    elif guess_answer < random_number:
        print('Go higher')
        guesses += 1
        guess_answer = user_guess()
print(' You got it in ' + str(guesses) + ' tries ')    
