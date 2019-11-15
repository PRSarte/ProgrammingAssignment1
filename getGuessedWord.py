def getGuessedWord (secretWord,lettersGuessed): #The function getGuessedWord was created
    word = []                                   #This function shows the word with missing letters
    for x in secretWord:
        if x in lettersGuessed:
            word.append(x)
        else:
            word.append('_')
    return ''.join(word)
