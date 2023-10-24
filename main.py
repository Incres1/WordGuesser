import tkinter as tk
from game_logic import new_game, check_guess
from settings import WINDOW_WIDTH, WINDOW_HEIGHT

def main():
    root = tk.Tk()
    root.title("Word Guesser Game")

    # Calculate screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Set the window size and position it at the center of the screen
    x = (screen_width - WINDOW_WIDTH) // 2
    y = (screen_height - WINDOW_HEIGHT) // 2

    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")

    # Create and place widgets (you can move this part to a separate GUI module)
    display_word = tk.StringVar()
    guess_entry = tk.Entry(root)
    result_label = tk.Label(root, text="")

    new_game_button = tk.Button(root, text="New Game", command=lambda: new_game(display_word, guess_entry, result_label))
    word_display = tk.Label(root, textvariable=display_word)
    guess_label = tk.Label(root, text="Guess the word:")
    check_button = tk.Button(root, text="Check Guess", command=lambda: check_guess(guess_entry=guess_entry, display_word=display_word, result_label=result_label))

    new_game_button.pack()
    guess_label.pack()
    word_display.pack()
    guess_entry.pack()
    check_button.pack()
    result_label.pack()

    # Create a new game to start with
    word_to_guess = new_game(display_word, guess_entry, result_label)

    # Start the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
