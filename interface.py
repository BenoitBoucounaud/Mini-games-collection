#!/usr/bin/env python3

from tkinter import * 

import rockPaperScissors
import hangmanGame
import dice_poker

root = Tk() 
root.title ("Mini games collection")

mainframe = Frame(root, height = 200, width = 500)
mainframe.pack_propagate(0)
mainframe.pack(padx = 5, pady = 5)

intro = Label(mainframe, text = """Welcom to the mini games collection. Please select one of them : """)
intro.pack(side = TOP)

rps_button = Button(mainframe, text = """Rock, paper, scissors""", command = rockPaperScissors.gui)
rps_button.pack()

#hm_button = Button(mainframe, text = """Hangman""", command = hangmanGame.gui)
#hm_button.pack()

#pd_button = Button(mainframe, text = """Poker dice""", command = dice_poker.gui)
#pd_button.pack()

exit_button = Button(mainframe, text = """Quit""", command = root.destroy)
exit_button.pack(side = BOTTOM)

root.mainloop()