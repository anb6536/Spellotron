import sys
import time

def dict_list ( file_name ):
    engList = []
    file =  open ( file_name, "r", encoding="utf-8" )
    for line in file:
        line = line.strip()
        lst = []
        lst += line
        engList.append( lst )
    return engList

def adjacent_key( file_name ):
    adjacentList = []
    file = open( file_name )
    for line in file:
        line = line.strip()
        line = line.split()
        adjacentList.append(line)
    return adjacentList

def adjKeyAutocorrect( adjacentList, engList, word ):
    wordList = []
    wordList += word
    for i in engList:
        if len( wordList ) == len( i ) and i == wordList:
            return wordList
    for i in engList:
        if len(wordList) == len(i) and i == wordList:
            return wordList
        elif len(wordList) == len(i):
            for Lidx in range ( len( wordList ) ):
                for x in adjacentList:
                    if wordList[Lidx] == x[0]:
                        for index in range ( len(x) ):
                            temp = wordList[Lidx]
                            tempLst1 = wordList[0:Lidx]
                            tempLst2 = wordList[Lidx+1:]
                            wordList = tempLst1+tempLst2
                            wordList.insert(Lidx, x[index])
                            if wordList == i:
                                return i
                            else:
                                tempLst1 = wordList[0:Lidx]
                                tempLst2 = wordList[Lidx+1:]
                                wordList = tempLst1+tempLst2
                                wordList.insert(Lidx, temp)

def missingAutocorrect( alphaList, engList, word ):
    wordList = []
    wordList += word
    for i in engList:
        if len( wordList ) == len( i ):
            if i == wordList:
                return wordList
    for i in engList:
        if len( wordList )+1 == len( i ):
            if i == wordList:
                return wordList
            else:
                for x in range ( len(alphaList) ):
                    for index in range ( len( wordList ) ):
                        tempList = wordList[:]
                        temp1 = wordList[0:index]
                        temp2 = wordList[index:]
                        middle = alphaList[x]
                        wordList = temp1 + [middle] + temp2
                        if wordList == i:
                            return i
                        else:
                            wordList = tempList[:]

def extraAutocorrect( engList, word ):
    wordList = []
    wordList += word
    for i in engList:
        if len( wordList ) == len( i ):
            if i == wordList:
                return wordList
    for i in engList:
        if len( wordList )-1 == len ( i ):
            if i == wordList:
                return wordList
            else:
                for index in range ( len( wordList ) ):
                    temp = wordList[index]
                    temp1 = wordList[0:index]
                    temp2 = wordList[index+1:]
                    wordList = temp1 + temp2
                    if wordList == i:
                        return i
                    else:
                        wordList = temp1 + [temp] + temp2


def list_to_words( lst ):
    word = ''
    for i in range ( len( lst ) ):
        letter = lst[i]
        word += letter
    return word

def alpha_list_generator():
    alphaList = []
    for i in range ( ord('a'), ord('z')+1):
        alphaList.append(chr(i))
    return alphaList

def main():
    mode = sys.argv[1]
    filename = sys.argv[2]
    adjacentList = adjacent_key( "keyboard_letters.txt" )
    dictList = dict_list( "american-english.txt" )
    alphaList = alpha_list_generator()
    file = open( filename )
    for line in file:
        line = line.strip()
        line = line.split()
        for i in line:
            correctedWord = adjKeyAutocorrect( adjacentList, dictList, i )
            if correctedWord != None:
                correctedWord = list_to_words( correctedWord )
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = missingAutocorrect( alphaList, dictList, i )
            if correctedWord != None:
                correctedWord = list_to_words( correctedWord )
                print( correctedWord, sep= " ", end= " ")
                continue
            correctedWord = extraAutocorrect( dictList, i )
            if correctedWord != None:
                correctedWord = list_to_words( correctedWord )
                print( correctedWord, sep= " ", end= " ")
                continue
            else:
                print( i, sep= " ", end= " ")
        print ()

#main()

