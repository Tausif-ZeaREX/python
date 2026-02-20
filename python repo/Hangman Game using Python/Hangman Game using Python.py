word = str(input('Enter your secret word: '))
seceret_word = ''
for i in range(len(word)):
    seceret_word += '*'

def guess():
    guessed_letter = input('Guess a letter: ')
    if len(guessed_letter) > 1:
        guessed_letter = input('guess a single letter: ')
    else:
        return guessed_letter
     
def check_guess(guess):
    global word
    global seceret_word
    my_word = seceret_word
    for i in range(len(word)):
        if word[i] == guess:
            my_word = guess[:i] + guess + my_word[i+1:]
    return my_word

while word != seceret_word:
    print('The Secret word is :' + seceret_word)
    new_guess = guess()
    seceret_word = check_guess(new_guess)

    