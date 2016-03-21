import pyttsx
import sys

""" Very basic tool to practice English spelling,
 reads all of the words in a list (infile) and
 writes all of the ones that you spelled incorrectly
 to outfile. type STOP to write all remaining words
 in the infile to the outfile. """

if len(sys.argv) != 3:
    print('Usage: learn.py infile outfile')
    exit(1)

inFile = open(sys.argv[1])
outFile = open(sys.argv[2], 'w')

class StopException(Exception):
    pass

def speakWord(word):
    engine = pyttsx.init()
    engine.setProperty('rate', 120)
    engine.say(word)
    engine.runAndWait()

def testWord(word):
    speakWord(word)
    userWord = raw_input('Type the word: ')
    if userWord == '':
        testWord(word)
        return

    if userWord == 'STOP':
        raise StopException()
    
    if userWord == word:
        return
    
    else:
        outFile.write(word + '\n')
        print('The correct spelling is: ' + word + '\n')
        while userWord != word:
            userWord = raw_input('Retype the word: ')

stop = 0
for line in inFile:
    word = line.strip()
    if stop == 0:
        try:
            testWord(word)
        except StopException:
            stop = 1
    else:
        outFile.write(word + '\n')




