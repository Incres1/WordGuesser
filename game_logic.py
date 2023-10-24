import random
import os

# List of words for the game
script_directory = os.path.dirname(os.path.abspath(__file__))
file_name = "words/en-basic"
file_path = os.path.join(script_directory, file_name)

words = []
with open(file_path, "r") as f:
    for line in f:
        word = line.strip()
        if len(word) == 4:
            words.append(word)

# Initialize word_to_guess as an empty string
word_to_guess = ""

# Function to start a new game and update word_to_guess
def new_game(display_word, guess_entry, result_label):
    global word_to_guess  # Use the global word_to_guess variable
    word_to_guess = random.choice(words)
    print(word_to_guess)
    display_word.set("_ " * len(word_to_guess))
    guess_entry.delete(0, "end")
    return word_to_guess

# Function to check the user's guess and update the display
def check_guess(guess_entry, display_word, result_label):
    global word_to_guess  # Use the global word_to_guess variable
    user_guess = guess_entry.get()  # Get the text from the Entry widget

    if is_a_word(user_guess, word_to_guess):
        print(user_guess)

        if user_guess == word_to_guess:
            display_word.set(word_to_guess)
            result_label.config(text="Congratulations! You guessed the word.")
        else:
            # Convert the word_to_guess and user_guess to lists for easier manipulation
            word_to_guess_array = [char for char in word_to_guess]
            user_guess_array = [char for char in user_guess]

            # fixing the stupid _ and space problem
            display_word_string = display_word.get()
            display_word_string = display_word_string.replace(" ", "")
            updated_display_array = [char for char in display_word_string]
            print(updated_display_array)
            # Loop through the user_guess_array and update the updated_display_array
            for i in range(len(user_guess_array)):
                for j in range(len(word_to_guess_array)):
                    if user_guess_array[i] == word_to_guess_array[j]:
                        updated_display_array[j] = user_guess_array[i]

            # Update the display
            print(updated_display_array)
            display_word.set(" ".join(updated_display_array))
            result_label.config(text="Try again. The word is not correct.")
    else:
        result_label.config(text="The word is not in the dictionary.")




def is_a_word(user_guess, word_to_guess):
    if len(user_guess) == len(word_to_guess):
        return True
    else:
        return False
