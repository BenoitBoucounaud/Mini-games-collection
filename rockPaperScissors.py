from tkinter import *

import random
import time


def gui():

    rock = 1
    paper = 2
    scissors = 3

    names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
    rules = {rock: scissors, paper: rock, scissors: paper}

    player_score = 0
    computer_score = 0

    def start():
        while game():
            pass

    def game():
        player = player_choice.get()
        computer = random.randint(1, 3)
        computer_choice.set(names[computer])
        result(player, computer)

    def result(player, computer):
        new_score = 0
        if player == computer:
            result_set.set("Tie game.")
        elif rules[player] == computer:
            result_set.set("Your victory has been assured.")
            new_score = player_score.get()
            new_score += 1
            player_score.set(new_score)
        else:
            result_set.set("Computer laughtat you.")
            new_score = computer_score.get()
            new_score += 1
            computer_score.set(new_score)

    rps_windows = Toplevel()
    rps_windows.title("Rock, paper, scissors")

    player_choice = IntVar()
    computer_choice = StringVar()
    result_set = StringVar()
    player_choice.set(1)
    player_score = IntVar()
    computer_score = IntVar()

    rps_frame = Frame(rps_windows)
    rps_frame.grid(column=0, row=0, sticky='nsew')

    Label(rps_frame, text="Player").grid(column=1, row=1, sticky="w")
    Radiobutton(rps_frame, text="Rock", variable=player_choice,
                value=1).grid(column=1, row=2, sticky="w")
    Radiobutton(rps_frame, text="Paper", variable=player_choice,
                value=2).grid(column=1, row=3, sticky="w")
    Radiobutton(rps_frame, text="Scissors", variable=player_choice,
                value=3).grid(column=1, row=4, sticky="w")

    Label(rps_frame, text="Computer").grid(column=3, row=1, sticky="nsew")
    Label(rps_frame, textvariable=computer_choice).grid(
        column=3, row=3, sticky="nsew")

    Label(rps_frame, text="Score").grid(column=1, row=5, sticky="nsew")
    Label(rps_frame, textvariable=player_score).grid(
        column=1, row=6, sticky="nsew")

    Label(rps_frame, text="Score").grid(column=3, row=5, sticky="nsew")
    Label(rps_frame, textvariable=computer_score).grid(
        column=3, row=6, sticky="nsew")

    Button(rps_frame, text="Play", command=start).grid(
        column=2, row=2, stick="nsew")
    Label(rps_frame, textvariable=result_set, width=50).grid(
        column=2, row=7, sticky="nsew")

    rps_windows.columnconfigure(0, weight=1)
    rps_windows.rowconfigure(0, weight=1)

    for i in range(1,4):    
        rps_frame.columnconfigure(i, weight=1)
    for i in range(1, 8):
        rps_frame.rowconfigure(i, weight=1)


if __name__ == '__main__':
    gui()
