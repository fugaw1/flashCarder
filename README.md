# flashCarder
Little python CLI flash card machine.

## Description
I was learning C using "Learn C the Hard Way", and a chapter asked me to make flash cards.
I decided hand writing flash cards was lame, so I made this program that takes in a file and turns it into flash cards.
It will take input for the file, what character/s you want to split with, and which side of the card you want the question to be.
If you're studying something and want to use flash cards, you can just make a file and run off that instead of using a big bloated website or buying index cards.

I need it's neat.

___
# Installation
```
git clone https://github.com/fugaw1/flashCarder.git
cd /flashCarder
python3 flashCarder.py -h
```

Run the test file
```
python3 flashCarder.py -i testflash -s ':' -b
```
___

```
python3 flashCarder.py -h                                   
usage: flashCarder.py [-h] [-i INPUT] [-s SPLIT] [-b]

Study flashcards taking an input file. Input file should have a flash card on every line, question/answer seperated by a specific character

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Specify your file.
  -s SPLIT, --split SPLIT
                        Specify how your lines will be split. Must use single quotes (':'), default is comma.
  -b, --back            If you want to study from back of card, default is front.

Hand writing flash cards is for losers.
```

Included is testflash, a file you can use to test the functionality.
