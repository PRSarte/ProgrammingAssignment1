def isWordGuessed (secretWord,lettersGuessed):  #function iswordGuessed was introducted
    for x in secretWord:                        #to check whether the word is already completed or not.
        if x not in lettersGuessed:
            return False
    return True
