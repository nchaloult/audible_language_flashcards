from playsound import playsound
from random import shuffle
import os
import sys
import time

"""
Traverses through the user's file system, beginning from the current directory,
and returns a list of local paths to each .mp3 file found.
"""
def findmp3s():
    output = []

    for root, dirs, files in os.walk('.'):
        # path is a list of subdirectories that grows as the traversal continues
        path = root.split(os.sep)

        # prefix contains the current directory at this moment in the traversal
        prefix = ''
        for i in range(1, len(path)):
            prefix += path[i] + '/'

        for file in files:
            if file[-4:] == '.mp3':
                output.append(prefix + file)

    return output

"""
Executes the command that the user has provided.

Any response from the user that begins with a '.' is interpreted as a command.
"""
def processCommand(command, answersAsList, mp3Paths, file):
    if command == 'skip':
        print 'Correct translation: ' + prettifyAnswer(answersAsList)
        time.sleep(1)
    elif command == 'repeat':
        mp3Paths.append(file)
    elif command == 'quit':
        sys.exit()
    elif command == 'help':
        print '\nAudible Language Flashcards\n\n'                                \
                + 'Available Commands:\n'                                      \
                + '\tskip:\tSkips the audio snippet last played, and reveals ' \
                + 'all acceptable answers for that snippet.\n'                 \
                + '\trepeat:\tRepeats the audio snippet that was last '        \
                + 'played.\n'                                                  \
                + '\tquit:\tQuits the utility.\n'                              \
                + '\thelp:\tDisplays available commands.\n\n'                  \
                + 'The last audio snippet has been repeated. To hear it '      \
                + 'again, use the \'repeat\' command.'
        mp3Paths.append(file)
    else:
        print 'Unrecognized command passed to processCommand(). '              \
                + 'Repeating last audio snippet...'
        mp3Paths.append(file)
        time.sleep(1)

"""
Compares the user's response with the correct answer for the audio file that
has just been played, and tells the user if their response was correct. The
correct answer for an audio clip is the name of that audio file, or any of the
words in the audio file's name that are separated by underscores.

If their response is incorrect, that audio file is pushed back onto the top of
the stack so that the user may try to translate that same audio clip again.
"""
def processGuess(guess, answersAsList, mp3Paths, file):
    if guess in answersAsList:
        print 'Correct'

        if len(answersAsList) > 1:
            print 'Acceptable answers were: ' + prettifyAnswer(answersAsList)

        time.sleep(1)
    else:
        print 'Try again'
        mp3Paths.append(file)
        time.sleep(1)

"""
Returns a String containing the correct answer, or all possible correct answers
separated by commas, for the audio clip that was just played.

Removes brackets and single-quote marks from str(answersAsList).
"""
def prettifyAnswer(answersAsList):
    return str(answersAsList)[1:-1].replace('\'', '')

# Main function
if __name__ == '__main__':
    """
    A list of paths to .mp3 files in a random order. This list behaves as a
    stack.
    """
    mp3Paths = findmp3s()
    shuffle(mp3Paths)

    # while mp3Paths is not empty...
    while mp3Paths:
        curFile = mp3Paths.pop()

        playsound(curFile)

        # contains all possible correct answers for curFile
        answersAsList = curFile[curFile.rfind('/') + 1:curFile.find('.')].split('_')
        # the user's response
        guess = raw_input('Translation: ').lower()

        if guess[0] == '.':
            processCommand(guess[1:], answersAsList, mp3Paths, curFile)

            # print new line
            print ''
        else:
            processGuess(guess, answersAsList, mp3Paths, curFile)

            # print new line
            print ''

    print 'Practice complete!'
