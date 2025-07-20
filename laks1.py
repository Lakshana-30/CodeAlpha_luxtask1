import random

def hangman():
    words = ["table", "crust", "pages", "pasta", "brush"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word: ", " ".join(guessed))

    while attempts > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! You have {attempts} attempts left.")

        print("Word: ", " ".join(guessed))

    if "_" not in guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("You lost! The word was:", word)

# Run the game
hangman()
