import random

def play_hangman():
    """
    Plays a simple text-based Hangman game.
    """
    words = ["Broomstick","Elephant","Knowledge","Dolphin","Chamelion" ]
    chosen_word = random.choice(words)
    word_display = ["_"] * len(chosen_word)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman! 🎮")
    print(f"The word has {len(chosen_word)} letters. Good luck!")
    print(" ".join(word_display))

    while "_" in word_display and incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print(f"Correct! '{guess}' is in the word.")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    word_display[i] = guess
        else:
            incorrect_guesses += 1
            print(f"Incorrect! '{guess}' is not in the word. You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        print(" ".join(word_display))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

    if "_" not in word_display:
        print(f"\nCongratulations! 🎉 You guessed the word: '{chosen_word}'. You win!")
    else:
        print(f"\nGame over. 💀 You ran out of guesses. The word was '{chosen_word}'.")

# Start the game
play_hangman()