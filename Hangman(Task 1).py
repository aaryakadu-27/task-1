import random

def get_random_word():
    """
    Selects a random word from a predefined list.
    """
    word_list = ['python', 'developer', 'hangman', 'coding', 'function', 'variable']
    return random.choice(word_list)

def display_current_state(word, guessed_letters):
    """
    Displays the current state of the word with guessed letters revealed.
    """
    display = [letter if letter in guessed_letters else '_' for letter in word]
    print("Word: " + ' '.join(display))

def get_valid_input(guessed_letters):
    """
    Asks the user for a single valid alphabetical character that hasn’t been guessed.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabetical character.")
        elif guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        else:
            return guess

def play_hangman():
    """
    Runs the Hangman game logic.
    """
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("🎮 Welcome to Hangman!")
    print(f"🧩 The word has {len(word)} letters.")

    while incorrect_guesses < max_incorrect:
        display_current_state(word, guessed_letters)
        print(f"❌ Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        guess = get_valid_input(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            incorrect_guesses += 1
            print("❌ Wrong guess.")

        # Check for win
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("\n💀 Game over! The correct word was:", word)

def main():
    """
    Entry point of the program.
    """
    play_hangman()

if __name__ == "__main__":
    main()
