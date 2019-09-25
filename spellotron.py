"""
    Name : Aahish Balimane
    Language: Python 3.7
    Description: The program performs the autocorrect function on either the input text file or a string entered by the user.
"""
import sys
LEGAL_WORD_FILE = "american-english.txt"
KEY_ADJACENCY_FILE = "keyboard-letters.txt"

def dict_list ( file_name ):
    """
    Creates a list of words in the english dictionary
    :param file_name: File that is read and converted into a list
    :return: list of english dictionary
    """
    engList = []
    file =  open ( file_name, "r", encoding="utf-8" )
    for line in file:
        line = line.strip()
        engList.append( line )
    return engList

def adjacent_key( file_name ):
    """
    Creates a dict of adjacent letters to a given letter
    :param file_name: file that is read and converted to a dict
    :return: dictionary of keys as letters and corresponding value as list of adjacent keys
    """
    adjacentDict = {}
    file = open( file_name )
    for line in file:
        line = line.strip()
        adjacentDict[line[0]]=line
    return adjacentDict

def adjKeyAutocorrect( adjacentDict, engList, word ):
    """
    The function fixes the word replacing each letter of the word in order with its adjacent key and then searching for
    it in the english dictionary
    :param adjacentDict: dictionary of key as letters and value as list of adjacent keys to the letter.
    :param engList: List of words in the english dictionary
    :param word: the word to be corrected
    :return: corrected word
    """
    size = len( word )
    newList = sizeDict(engList, size)
    if word in newList:
        return word
    for Lidx in range ( len( word ) ):
        if word[Lidx] in adjacentDict:
            adjKeys = adjacentDict[word[Lidx]]
            index = 0
            while index < len(adjKeys):
                temp = word[:]
                temp1 = word[0:Lidx]
                temp2 = word[Lidx+1:]
                middle = adjKeys[index]
                word = temp1+middle+temp2
                if word in newList:
                    return word
                else:
                    word = temp[:]
                    index += 2


def missingAutocorrect( alphaList, engList, word ):
    """
    The function corrects word. The input word has a letter missing in it and is fixed by inserting every letter at every
    position and checks if it is in the dictionary.
    :param alphaList: list of alphabets of english
    :param engList: list of words in the english dictinary
    :param word: the word to be fixed
    :return: the fixed word
    """

    size = len( word )
    newList = sizeDict(engList, size+1)
    if word in newList:
        return word
    else:
        for index in range ( len( word )+1 ):
            for x in range ( len(alphaList) ):
                temp = word[:]
                temp1 = word[0:index]
                temp2 = word[index:]
                middle = alphaList[x]
                wordList = temp1 + middle + temp2
                if wordList in newList :
                    return wordList
                else:
                    word = temp[:]

def extraAutocorrect( engList, word ):
    """
    The function fixes the entered word by removing each letter at a time and comparing it to words in the dictionary to
    see if a match exists
    :param engList: list of letters in the english dictionary
    :param word: the word to be fixed
    :return: the fixed word
    """
    size = len( word )
    newList = sizeDict(engList, size-1)
    if word in newList:
        return word
    else :
        for index in range ( len( word ) ):
            temp = word[:]
            temp1 = word[0:index]
            temp2 = word[index+1:]
            word = temp1 + temp2
            if word in newList:
                return word
            else:
                word = temp[:]


def puncRemove( string ):
    """
    The function strips the punctuations from the start and the end of the word
    :param string: the string from which the punctuations needs to be stripped
    :return: tupple consisting of the punctuautions in the start, the word and punctuautions in the end
    """
    before = ""
    middle = ""
    after = ""
    if string == "":
        return before, middle, after
    if string.isdigit() == True:
        return before, string, after
    if len(string)== 1:
        return before, string, after
    while string[0].isidentifier() == False:
        before += string[0]
        string = string[1:]
        if len(string) == 0:
            return before, middle, after
    while string[len(string)-1].isidentifier() == False:
        after += string[len(string)-1]
        string = string[:len(string)-1]
        if len(string) == 0:
            break
    middle = string[:]
    return before, middle, after

def puncAdd(before, middle, after):
    """
    The function adds back the punctuations to the word
    :param before: the punctuations before the word
    :param middle: the word
    :param after: the punctuations after the word
    :return: the word with punctuations added
    """
    word = before+middle+after
    return word

def sizeDict( dictList, size):
    """
    It picks out the words from the english dictionary that have the same size of that of the word to be corrected
    :param dictList: list of words in the english dictionary
    :param size: Size of words to be picked out of the dict.
    :return: new dict List that has words of the length size.
    """
    newList = []
    for i in dictList:
        if len( i ) == size:
            newList.append(i)
    return newList

def alpha_list_generator():
    """
    Creates a list of alphabets
    :return: list of alphabets
    """
    alphaList = []
    for i in range ( ord('a'), ord('z')+1):
        alphaList.append(chr(i))
    return alphaList

def caseChange( word ):
    """
    changes the case of the first letter of the word
    :param word: word of which the case is changed
    :return: word with case changed
    """
    if len(word) == 0:
        return word
    if ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z"):
        first = word[0].lower()
        word = first + word[1:]
    elif ord(word[0]) >= ord("a") and ord(word[0]) <= ord("z"):
        first = word[0].upper()
        word = first + word[1:]
    return word

def caseIdentifier ( word ):
    """
    Tells what the case of the first letter of the word is.
    :param word: word for which the case needs to be identified
    :return: "Upper" or "Lower" based on the case of the first letter
    """
    if len(word) == 0:
        return "Lower"
    if ord(word[0]) >= ord("A") and ord(word[0]) <= ord("Z"):
        return "Upper"
    elif ord(word[0]) >= ord("a") and ord(word[0]) <= ord("z"):
        return "Lower"

def toLower ( word ):
    """
    Converts the first letter to lower case
    :param word: word of which case has to be changed
    :return: word with lower case
    """
    if len(word) == 0:
        return word
    first = word[0].lower()
    word = first + word[1:]
    return word

def toUpper ( word ):
    """
    Converts the first letter to upper case
    :param word: word of which case has to be changed
    :return: word with upper case
    """
    if len(word) == 0:
        return word
    first = word[0].upper()
    word = first + word[1:]
    return word

def modeLines1 (filename, dictList, adjacentDict, alphaList):
    """
    Prints the file after fixing the words in it in lines mode.
    :param filename: name of the file in which fixes needs to be done
    :param dictList: list of words in the english dictionary
    :param adjacentDict: dictionary of adjacent keys
    :param alphaList: list of english alphabets
    :return: none
    """
    wordCount = 0
    correctedCount = 0
    incorrectCount = 0
    correctedList = []
    correctList = []
    incorrectList = []
    file = open( filename )
    for line in file:
        line = line.strip()
        line = line.split()
        for i in line:
            wordCount += 1
            before, word, after = puncRemove(i)
            case = caseIdentifier( word )
            if len(word) == 0:
                continue
            if word in dictList:
                if case == "Upper":
                    word = toUpper(word)
                elif case == "Lower":
                    word = toLower(word)
                word = before+word+after
                print( word, sep= " ", end= " ")
                continue
            if case == "Upper":
                word = caseChange(word)
            if word in dictList:
                if case == "Upper":
                    word = toUpper(word)
                elif case == "Lower":
                    word = toLower(word)
                word = before+word+after
                print( word, sep= " ", end= " ")
                continue
            if case == "Upper":
                word = caseChange(word)
            correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = missingAutocorrect( alphaList, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = extraAutocorrect( dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            if case == "Upper":
                word = caseChange(word)
            correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = missingAutocorrect( alphaList, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = extraAutocorrect( dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print( correctedWord, sep= " ", end= " ")
                continue
            else:
                if len(word) == 1 or word.isdigit() == True:
                    print( word, sep= " ", end= " ")
                    continue
                incorrectCount += 1
                if case == "Upper":
                    word = toUpper(word)
                if case == "Lower":
                    word = toLower(word)
                word = before+word+after
                incorrectList.append(word)
                print( word, sep= " ", end= " ")
        print ()
    print ()
    print( wordCount, "words read from file")
    print()
    print( correctedCount, "Corrected Words")
    print( correctedList )
    print()
    print(incorrectCount, "Unknown Words")
    print( incorrectList )

def modeWords1(filename, dictList, adjacentDict, alphaList):
    """
    Prints the file after fixing the words in it in words mode.
    :param filename: name of the file in which fixes needs to be done
    :param dictList: list of words in the english dictionary
    :param adjacentDict: dictionary of adjacent keys
    :param alphaList: list of english alphabets
    :return: none
    """
    wordCount = 0
    correctedCount = 0
    incorrectCount = 0
    correctedList = []
    correctList = []
    incorrectList = []
    file = open( filename )
    for line in file:
        line = line.strip()
        line = line.split()
        for i in line:
            wordCount += 1
            before, word, after = puncRemove(i)
            case = caseIdentifier( word )
            if len(word) == 0:
                continue
            if word in dictList:
                continue
            if case == "Upper":
                word = caseChange(word)
            if word in dictList:
                continue
            if case == "Upper":
                word = caseChange(word)

            correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            correctedWord = missingAutocorrect( alphaList, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            correctedWord = extraAutocorrect( dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            if case == "Upper":
                word = caseChange(word)
            correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            correctedWord = missingAutocorrect( alphaList, dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            correctedWord = extraAutocorrect( dictList, word )
            if correctedWord != None:
                correctedCount += 1
                if case == "Upper":
                    correctedWord = toUpper(correctedWord)
                elif case == "Lower":
                    correctedWord = toLower(correctedWord)
                correctedWord = before+correctedWord+after
                correctedList.append(i)
                correctList.append(correctedWord)
                print(i, "->", correctedWord)
                continue
            else:
                if len(word) == 1 or word.isdigit() == True:
                    continue
                incorrectCount += 1
                word = caseChange(word)
                word = before+word+after
                incorrectList.append(word)
    print ()
    print( wordCount, "words read from file")
    print()
    print( correctedCount, "Corrected Words")
    print( correctedList )
    print()
    print(incorrectCount, "Unknown Words")
    print( incorrectList )

def modeLines2(dictList, adjacentDict, alphaList):
    """
    Prints the string after fixing the words in it in lines mode.
    :param dictList: list of words in the english dictionary
    :param adjacentDict: dictionary of adjacent keys
    :param alphaList: list of english alphabets
    :return: none
    """
    wordCount = 0
    correctedCount = 0
    incorrectCount = 0
    correctedList = []
    correctList = []
    incorrectList = []
    line = input()
    line = line.strip()
    line = line.split()
    for i in line:
        wordCount += 1
        before, word, after = puncRemove(i)
        case = caseIdentifier( word )
        if len(word) == 0:
            continue
        if word in dictList:
            if case == "Upper":
                word = toUpper(word)
            elif case == "Lower":
                word = toLower(word)
            word = before+word+after
            print( word, sep= " ", end= " ")
            continue
        if case == "Upper":
            word = caseChange(word)
        if word in dictList:
            if case == "Upper":
                word = toUpper(word)
            elif case == "Lower":
                word = toLower(word)
            word = before+word+after
            print( word, sep= " ", end= " ")
            continue
        if case == "Upper":
            word = caseChange(word)
        correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        correctedWord = missingAutocorrect( alphaList, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        correctedWord = extraAutocorrect( dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        if case == "Upper":
            word = caseChange( word )
        correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        correctedWord = missingAutocorrect( alphaList, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        correctedWord = extraAutocorrect( dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print( correctedWord, sep= " ", end= " ")
            continue
        else:
            if len(word) == 1 or word.isdigit() == True:
                print( word, sep= " ", end= " ")
                continue
            incorrectCount += 1
            if case == "Upper":
                word = toUpper(word)
            if case == "Lower":
                word = toLower(word)
            word = before+word+after
            incorrectList.append(word)
            print( word, sep= " ", end= " ")

    print()
    print()
    print( wordCount, "words read from input")
    print()
    print( correctedCount, "Corrected Words")
    print( correctedList )
    print()
    print(incorrectCount, "Unknown Words")
    print( incorrectList )

def modeWords2(dictList, adjacentDict, alphaList):
    """
    Prints the string after fixing the words in it in words mode.
    :param dictList: list of words in the english dictionary
    :param adjacentDict: dictionary of adjacent keys
    :param alphaList: list of english alphabets
    :return: none
    """
    wordCount = 0
    correctedCount = 0
    incorrectCount = 0
    correctedList = []
    correctList = []
    incorrectList = []
    line = input()
    line = line.strip()
    line = line.split()
    for i in line:
        wordCount += 1
        before, word, after = puncRemove(i)
        case = caseIdentifier(word)
        if len(word) == 0:
            continue
        if word in dictList:
            continue
        if case == "Upper":
            word = caseChange(word)
        if word in dictList:
            continue
        if case == "Upper":
            word = caseChange(word)
        correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        correctedWord = missingAutocorrect( alphaList, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        correctedWord = extraAutocorrect( dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        if case == "Upper":
            word = caseChange(word)

        correctedWord = adjKeyAutocorrect( adjacentDict, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        correctedWord = missingAutocorrect( alphaList, dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        correctedWord = extraAutocorrect( dictList, word )
        if correctedWord != None:
            correctedCount += 1
            if case == "Upper":
                correctedWord = toUpper(correctedWord)
            elif case == "Lower":
                correctedWord = toLower(correctedWord)
            correctedWord = before+correctedWord+after
            correctedList.append(i)
            correctList.append(correctedWord)
            print(i, "->", correctedWord)
            continue
        else:
            if len(word) == 1 or word.isdigit() == True:
                continue
            incorrectCount += 1
            word = caseChange(word)
            word = before+word+after
            incorrectList.append(word)
    print ()
    print( wordCount, "words read from file")
    print()
    print( correctedCount, "Corrected Words")
    print( correctedList )
    print()
    print(incorrectCount, "Unknown Words")
    print( incorrectList )

def main():
    """
    The main function calls other function to fix the words and to print it
    :return: None
    """
    mode = sys.argv[1]
    if mode != "words" and mode != "lines":
        print( "Error!! Invalid mode entered.", file = sys.stderr)
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        choice = 1
    elif len(sys.argv) == 2:
       choice = 2
    adjacentDict = adjacent_key( KEY_ADJACENCY_FILE )
    dictList = dict_list( LEGAL_WORD_FILE )
    alphaList = alpha_list_generator()
    if mode == "lines" and choice == 1:
        modeLines1(filename, dictList, adjacentDict, alphaList)
    elif mode == "words" and choice == 1:
        modeWords1(filename, dictList, adjacentDict, alphaList)
    elif mode == "lines" and choice == 2:
        modeLines2(dictList, adjacentDict, alphaList)
    elif mode == "words" and choice == 2:
        modeWords2(dictList, adjacentDict, alphaList)


main()

