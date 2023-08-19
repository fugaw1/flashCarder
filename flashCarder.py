# python3
# flashCarder.py
# By: fugawi
# 17AUG2023
# Splits a file and makes it a flash card prompt. 
# Randomly selects the cards, and allows user 
# to decide if they need to redo that one.

import random
import argparse
from pathlib import Path

# Inputs deck into BridgeKeeper, takes back input for second deck of medium questions. 
def FirstFlash(ques, ans):
    first = True
    mQ, mA = BridgeKeeper(ques, ans, first)
    return mQ, mA

# This is the big function that actually asks the questions. Boolean to determine what to do with it
def BridgeKeeper(questions, answers, turn):
    midQuestions = []
    midAnswers = []
    count = len(questions) - 1
    try:
        while count >= 0:
            choice = random.randint(0, count)
            input(questions[choice] + "\n")
            print(answers[choice])
            difficulty = input("\n j = Easy   k = Medium    l = Hard: \n   > ")
            difficulty = str(difficulty.lower())
            if difficulty == "j":
                del answers[choice]
                del questions[choice]
                count = count - 1
            elif difficulty == "k":
                if turn == True: 
                    midQuestions.append(questions[choice])
                    midAnswers.append(answers[choice])
                    del answers[choice]
                    del questions[choice]
                    count = count - 1
                elif turn == False:
                    continue
                else: 
                    print("something is horribly wrong")
                    continue
            elif difficulty == "l":
                continue
            else:
                print("Oof, we'll move on.")
                continue
        if turn == True:
            return midQuestions, midAnswers
        elif turn == False:
            print(" \n \n You did it. Congrats \n \n")
            return 0
    except KeyboardInterrupt:
        exit()

# With boolean false, takes in the medium questions and reshuffles it to a new deck.
def SecondFlash(midQ, midA):
    if len(midQ) == 0:
        print(" \n \n Wow first try. Congrats \n \n")
        exit()
    else:
        second = False
        print("\n *** Entering the Second Deck *** \n ")
        BridgeKeeper(midQ, midA, second)

# Takes in file and split type, splits file into two lists, checks that the user isn't dumb
def FileReader(fileName, splitter):
    file = open(fileName, "r")
    lines = file.readlines()
    front = []
    back = []
    for line in lines:    
        splitLine = line.split(splitter, maxsplit=1)
        if len(splitLine) == 2:
            front.append(splitLine[0].strip())
            back.append(splitLine[1].strip())
        else:
            print("Error making flash card " + str(splitLine))
            print("Check if you're missing a splitter in your file. \n")
    if len(back) == 0: 
        print("News flash, buddy. You specified the wrong splitter. Do it right.")
        print("Example: \n >  python3 flashCarder -i testfile -s ':' ")
        exit()
    else:
        return front, back

# Checks input for file name
def FileCheck(fileName):
    # Ask the user to specify a file if they didn't
    if fileName == "None":
        fileName = input("What's your file name/path?:\n  > ") 
    return fileName

# Checks input for splitter type
def SplitCheck(splitter):
    if splitter == "None":
        splitter = ',' # you can change this if you want
    return splitter

# Checks boolean option and put the cards into arrays
def FrontOrBack(front, back,  bOption):
    if bOption == False:
        questions = front
        answers = back
    elif bOption == True:
        questions = back
        answers = front
    else:
        print("Boolean third option?! Time is folding on itself.")
    return questions, answers

# Let's start here
def main():
    parser = argparse.ArgumentParser(
            prog='flashCarder.py',
            description='Study flashcards taking an input file. Input file should have a flash card on every line, question/answer seperated by a specific character',
            epilog="Hand writing flash cards is for losers.",
            )

    parser.add_argument('-i', '--input', help="Specify your file.", required=False)
    parser.add_argument('-s', '--split', help="Specify how your lines will be split. Must use single quotes (':'),  default is comma.", required=False)
    parser.add_argument('-b', '--back', help="If you want to study from back of card, default is front.", action="store_true", required=False)
    args = parser.parse_args()
    # Save my args
    fileInput = str(args.input)
    split = str(args.split)
    back = bool(args.back)
    
    # Take the file and make it into dictionary
    fileInput = FileCheck(fileInput)
    split = SplitCheck(split)
    f, b = FileReader(fileInput, split) 
    
    # Starts the show
    q, a = FrontOrBack(f, b, back)
    q, a = FirstFlash(q, a)
    SecondFlash(q, a)
    # FirstFlash sends to SecondFlash, which both use BridgeKeeper()

    return 0

# The whole program fits in this one line
main()
