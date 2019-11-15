def getAvailableLetters (lettersGuessed):       #getAvailableLetters was made.
    import string                               #string was imported so that the function of strings can be used.
    x = string.ascii_lowercase
    lettleft = []                               #The function checks for the available letters that have not yet been guessed.
    for a in x :
        if a not in lettersGuessed:
            lettleft.append(a)
    return " ".join(lettleft)
