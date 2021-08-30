# Word Guessing Game

secret_word = "kimtvak"
guess = ""
count, limit = 0, 5
out_of_guesses = False

while secret_word != guess and not out_of_guesses:
    if count < limit:
        guess = str(input("enter the guess word:\t")).lower()
        count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You Lose")
else:
    print("You won!")
