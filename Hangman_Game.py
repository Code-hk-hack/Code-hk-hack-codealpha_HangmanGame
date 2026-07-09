import random

def play_hangman():
    # 1. LISTS: Predefined list of 5 words
    word_bank = ["python", "intern", "coding", "program", "solver"]
    
    # RANDOM: Randomly select one word from the bank
    secret_word = random.choice(word_bank)
    
    # LISTS & STRINGS: Create a list of underscores to represent hidden letters
    guessed_word = ["_"] * len(secret_word)
    
    # Trackers for the game state
    incorrect_guesses_left = 6
    guessed_letters = set()

    print("=== Welcome to Hangman! ===")
    print(f"The word has {len(secret_word)} letters.")

    # 2. WHILE LOOP: Keeps running until the player wins or runs out of guesses
    while incorrect_guesses_left > 0 and "_" in guessed_word:
        # Display current progress (e.g., "p _ t h _ _")
        print("\n" + " ".join(guessed_word))
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get console input from the player
        guess = input("Guess a letter: ").lower().strip()

        # 3. IF-ELSE: Input validation to prevent bugs
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        # Add the valid guess to our tracking set
        guessed_letters.add(guess)

        # 4. IF-ELSE: Check if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
            # STRINGS & LISTS: Update the hidden word list with the correct letter
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # 5. IF-ELSE: Game Over Evaluation
    print("\n=======================")
    if "_" not in guessed_word:
        print(f"🎉 Congratulations! You guessed the word: {secret_word.upper()}")
        print("You won! 🏆")
    else:
        print(f"💥 Game Over! You ran out of guesses.")
        print(f"The correct word was: {secret_word.upper()}")
    print("=======================")

# Run the game
if __name__ == "__main__":
    play_hangman()