from tkinter import *
from random import *
import json

word = 0
word_length = 0
clue = 0

def gui():

    global word, word_length, clue
    jsonFile = open('dictionary.json')
    dictionary = json.load(jsonFile)
    word = choice(dictionary['en'])
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6

    def hangman(hangman):
        graphic = [
            """
                +-------+
                |
                |
                |
                |
                |
            =============
            """, 
            """
                +-------+
                |       |
                |       O
                |
                |
                |
            =============
            """,
            """
                +-------+
                |       |
                |       O
                |       |
                |
                |
            =============
            """,
            """
                +-------+
                |       |
                |       O
                |      -|
                |
                |
            =============
            """,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |
                |
            =============
            """,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |      /
                |
            =============
            """,
            """
                +-------+
                |       |
                |       O
                |      -|-
                |      / \\
                |
            =============
            """
        ]

        graphic_set = graphic[hangman]
        hm_graphic.set(graphic_set)

    def game():
        letters_wrong = incorrect_guesses.get()

        letter = letter_guess.get()
        letter.strip()
        letter.lower()
        first_index = word.find(letter)

        if first_index == -1 :
            letters_wrong += 1
            incorrect_guesses.set(letters_wrong)
        else :
            for i in range(word_length) : 
                if letter == word[i] :
                    clue[i] = letter
        
        hangman(letters_wrong)
        clue_set = " ".join(clue)
        word_output.set(clue_set)

        if letters_wrong == tries :
            result_text = "Game over. The word was : " + word
            result_set.set(result_text)
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)

        if "".join(clue) == word : 
            result_text = "You win ! The word was : " + word
            result_set.set(result_text)
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)
    
    def reset_game():
        global word, word_length, clue
        incorrect_guesses.set(0)
        hangman(0)
        result_set.set("")
        letter_guess.set("")
        word = choice(dictionary['en'])
        word_length = len(word)
        clue = word_length * ["_"]
        new_clue = " ".join(clue)
        word_output.set(new_clue)

    hm_windows = Toplevel()
    hm_windows.title("Hangman")
    incorrect_guesses = IntVar()
    incorrect_guesses.set(0)
    player_score = IntVar()
    computer_score = IntVar()
    result_set = StringVar()
    letter_guess = StringVar()
    word_output = StringVar()
    hm_graphic = StringVar()

    hm_frame = Frame(hm_windows, width = 300)
    hm_frame.grid(column = 0, row = 0, sticky = "nsew")
    hm_frame.columnconfigure(0, weight = 1)
    hm_frame.rowconfigure(0, weight = 1)

    Label(hm_frame, textvariable = hm_graphic, anchor = W, justify = LEFT).grid(column = 2, row = 1)
    Label(hm_frame, text = "Word").grid(column = 2, row = 2)
    Label(hm_frame, textvariable = word_output).grid(column = 2, row = 3)
    
    Label(hm_frame, text = "Enter a letter").grid(column = 2, row = 4)
    hm_entry = Entry(hm_frame, exportselection = 0, textvariable = letter_guess)
    hm_entry.grid(column = 2, row = 5)
    hm_entry_button = Button(hm_frame, text = "Guess", command = game)
    hm_entry_button.grid(column = 2, row = 6)

    Label(hm_frame, text = "Player score ").grid(column = 1, row = 7, sticky = "w")
    Label(hm_frame, textvariable = player_score).grid(column = 1, row = 8, sticky = "w")
    Label(hm_frame, text = "Computer score ").grid(column = 3, row = 7, sticky = "w")
    Label(hm_frame, textvariable = computer_score).grid(column = 3, row = 8, sticky = "w")
    Label(hm_frame, textvariable = result_set).grid(column = 2, row = 9)
    replay_button = Button(hm_frame, text = "Play again", command = reset_game)
    replay_button.grid(column = 2, row = 10) 
    

if __name__ == '__main__':
        gui()





