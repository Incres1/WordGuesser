import os
import tkinter as tk
import random


# Read words
script_directory = os.path.dirname(os.path.abspath(__file__))
file_name = "words/en-basic"
file_path = os.path.join(script_directory, file_name)

words = []
with open(file_path, "r") as f:
    for line in f:
        word = line.strip()
        if len(word) >= 3 and len(word) < 7:
            words.append(word)


# List of words for the game
# words = ["python", "java", "javascript", "html", "css", "ruby", "php"]

# Function to start a new game
def new_game():
    global word_to_guess
    word_to_guess = random.choice(words)
    print(word_to_guess)
    display_word.set("_ " * len(word_to_guess))
    guess_entry.delete(0, tk.END)

# Function to check the user's guess
def check_guess():
    user_guess = guess_entry.get()
    if user_guess == word_to_guess:
        display_word.set(word_to_guess)
        result_label.config(text="Congratulations! You guessed the word.")
    else:
        result_label.config(text="Try again. The word is not correct.")

# Create the main window
root = tk.Tk()
root.title("Word Guesser Game")

# Checkbox logic
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Easy", variable=checkbox_var)
checkbox.pack()

# Calculate screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position it at the center of the screen
window_width = 400
window_height = 200
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a display variable for the word to guess
word_to_guess = ""
display_word = tk.StringVar()

# Create and place widgets
new_game_button = tk.Button(root, text="New Game", command=new_game)
word_display = tk.Label(root, textvariable=display_word)
guess_label = tk.Label(root, text="Guess the word:")
guess_entry = tk.Entry(root)
check_button = tk.Button(root, text="Check Guess", command=check_guess)
result_label = tk.Label(root, text="")


new_game_button.pack()
guess_label.pack()
word_display.pack()
guess_entry.pack()
check_button.pack()
result_label.pack()

# Create a new game to start with
new_game()

# Start the main loop
root.mainloop()
