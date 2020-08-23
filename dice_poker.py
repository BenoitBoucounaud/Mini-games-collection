from tkinter import *
import random
from itertools import groupby

dice = 0

def gui():
    global dice
    dice = roll(5)
    dice.sort()

    nine = 1
    ten = 2
    jack = 3
    queen = 4
    king = 5
    ace = 6 

    names ={nine: "9", ten : "10", jack: "J", queen: "Q", king: "K", ace:"A"}
    result = "You have " + hand(dice)

    def game():
        throws()
    
    def throws():
        global dice
        dice1_check= dice1.get()
        dice2_check= dice2.get()
        dice3_check= dice3.get()
        dice4_check= dice4.get()
        dice5_check= dice5.get()
        dice_rerolls = [dice1_check, dice2_check, dice3_check, dice4_check, dice5_check]

        for i in range(len(dice_rerolls)):
            if 0 in dice_rerolls:
                dice_rerolls.remove(0)
        if len(dice_rerolls) == 0:
            result = "You finish with " + hand(dice)
            hand_output.set(result)
        else : 
            roll_number = len(dice_rerolls)
            number_rerolls = roll(roll_number)
            dice_changes = range(len(dice_rerolls))
            iterations = 0

            while iterations < roll_number:
                iterations += 1
                dice[dice_changes[iterations - 1]] = number_rerolls[iterations - 1]
            iterations = 0

            while iterations < roll_number:
                iterations += 1
                replacement = number_rerolls[iterations - 1]
                dice[dice_changes[iterations - 1]] = replacement
            dice.sort()
            new_dice_list = [0, 0, 0, 0, 0]

            for i in range(len(dice)):
                new_dice_list[i] = names[dice[i]]
            
            final_dice = " ".join(new_dice_list)
            dice_output.set(final_dice)
            final_result = "You finish with " + hand(dice)
            hand_output.set(final_result)

    def reset_game() :
        global dice
        dice = roll(5)
        dice.sort()
        for i in range(len(dice)):
            empty_dice[i] = names[dice[i]]
        first_dice = " ".join(empty_dice)
        dice_output.set(first_dice)
        result = "You have " + hand(dice)
        hand_output.set(result)

    pd_windows = Toplevel()
    pd_windows.title("Poker dice")
    dice_output = StringVar()
    empty_dice = [0,0,0,0,0]
    for i in range(len(dice)):
        empty_dice[i] = names[dice[i]]
    first_dice = " ".join(empty_dice)
    dice_output.set(first_dice)
    hand_output = StringVar()
    hand_output.set(result)
    dice1 = IntVar()
    dice2 = IntVar()
    dice3 = IntVar()
    dice4 = IntVar()
    dice5 = IntVar()
    result_set = StringVar()
    player_score = IntVar()
    computer_score = IntVar()

    pd_frame = Frame(pd_windows, width = 300)
    pd_frame.grid(column = 0, row =0 , sticky = 'nsew')
    pd_frame.columnconfigure(0, weight = 1)
    pd_frame.rowconfigure(0, weight = 1) 
    Label(pd_frame, text = "Dice").grid(column = 3, row = 1)
    Label(pd_frame, textvariable = dice_output).grid(column = 3, row = 2)
    Label(pd_frame, textvariable = hand_output).grid(column = 3, row = 3)
         
    Label(pd_frame, text = "Reroll dices?").grid(column = 3, row = 4)
    reroll1 = Checkbutton(pd_frame, text = '1', variable = dice1, onvalue = 1, offvalue = 0)
    reroll1.grid(column = 1, row = 5)
    reroll2 = Checkbutton(pd_frame, text = '2', variable = dice2, onvalue = 2, offvalue = 0)
    reroll2.grid(column = 2, row = 5)
    reroll3 = Checkbutton(pd_frame, text = '3', variable = dice3, onvalue = 3, offvalue = 0)
    reroll3.grid(column = 3, row = 5)
    reroll4 = Checkbutton(pd_frame, text = '4', variable = dice4, onvalue = 4, offvalue = 0)
    reroll4.grid(column = 4, row = 5)
    reroll5 = Checkbutton(pd_frame, text = '5', variable = dice5, onvalue = 5, offvalue = 0)
    reroll5.grid(column = 5, row = 5)
    
    pd_reroll_button = Button(pd_frame, text = 'Reroll', command = game)
    pd_reroll_button.grid(column = 3, row = 6)
    pd_reset_button = Button(pd_frame, text = 'Reset', command = reset_game)
    pd_reset_button.grid(column = 3, row = 7)       

def roll(roll_number):
    numbers = [1, 2, 3, 4, 5, 6]
    dice = []
    iterations = 0
    while iterations < roll_number:
        iterations += 1
        dice.append(random.choice(numbers))
    return dice

def hand(dice):
    # groupby : count the numbers that make up the dice variable
    dice_hand = [len(list(group)) for key, group in groupby(dice)]
    dice_hand.sort(reverse=True)
    straight1 = [1,2,3,4,5]
    straight2 = [2,3,4,5,6]

    if dice == straight1 or dice == straight2:
        return "Sequel !"
    elif dice_hand[0] == 5:
        return "Five identical quarters !"
    elif dice_hand[0] == 4:
        return "Poker !"
    elif dice_hand[0] == 3:
        if dice_hand[1] == 2:
            return "Full !"
        else:
            return "Brelan"
    elif dice_hand[0] == 2:
        if dice_hand[1] == 2:
            return "Two pairs"
        else:
            return "One pair"
    else:
        return "A high card"

if __name__ == '__main__':
        gui()

