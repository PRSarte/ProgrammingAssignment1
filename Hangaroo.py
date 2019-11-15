def isWordGuessed (secretWord,lettersGuessed):  #function iswordGuessed was introducted
    for x in secretWord:                        #to check whether the word is already completed or not.
        if x not in lettersGuessed:
            return False
    return True

def getGuessedWord (secretword,lettersGuessed): #The function getGuessedWord was created
    word = []                                   #This function shows the word with missing letters
    for x in secretWord:
        if x in lettersGuessed:
            word.append(x)
        else:
            word.append('_')
    return " ".join(word)

def getAvailableLetters (lettersGuessed):       #getAvailableLetters was made.
    import string                               #string was imported so that the function of strings can be used.
    x = string.ascii_lowercase
    lettleft = []                               #The function checks for the available letters that have not yet been guessed.
    for a in x :
        if a not in lettersGuessed:
            lettleft.append(a)
    return " ".join(lettleft)

def loadWords(ChooseWord):                      #LoadWords checks from two categories, fruits and vegetables.
    import random
    f = ['apple','banana','cantaloupe','durian','grapes','kiwi','lime','mango','orange','tangerine']
    v = ['asparagus','beetroot','broccoli','cabbage','celery','cucumber','lettuce','onion','potato','spinach']
    while ChooseWord != 'v' or ChooseWord != 'f' or ChooseWord != 'V' or ChooseWord != 'F':
         ChooseWord = str(input('Please choose if the word would be a fruit or a vegetable by typing f or v! :'))
         if ChooseWord == 'v' or ChooseWord == 'V':     
             secretWord = random.choice(v)              #The user inputs whether they want fruits or vegetables to guess
             return secretWord                          #Then loadWords chooses randomly inside of a pre-made list of fruits to be guessed.
         elif ChooseWord == 'f' or ChooseWord == 'F':
             secretWord = random.choice(f)
             return secretWord
         else:
           continue                                    #user inputs anything other than f or v, it will ask for another input again til it gets f or v

def Hangaroo (secretWord):                              #Main Function line of the whole code.
    Mistakes = 0   
    letts = 0                               
    lettersGuessed = []
    print ('The word is ', len(secretWord), ' letters long.')
    print ('You only have 5 times to make a mistake or the game will end. GOODLUCK!')       
    
    while (5 - Mistakes) > 0:                                       #A 5 mistake marker is created
        if isWordGuessed(secretWord,lettersGuessed) == False:       #If user makes a mistake, marker would decrease, whilst making a
            letter = str(input('Please type a letter: ')).lower()   # correct answer will prompt them to keep going
            if letter in secretWord and letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print ('Good job! keep going!\n',getGuessedWord(secretWord,lettersGuessed))
            elif letter not in secretWord :
                print ('The letter is not included in the secret word, please try again\n',getGuessedWord(secretWord,lettersGuessed))
                lettersGuessed.append(letter)
                print ('You have ', (4- Mistakes),'mistakes remaining')
                Mistakes += 1
                                
                while letts != 'y' or letts != 'Y' or letts != 'n' or letts != 'N':     #This loop checks whether to person wants to check 
                    letts = str(input('Do you want to check for letters left?: '))      #for what available letters are remaining
                    if letts == 'y' or letts =='Y':
                        print ('The available letters are: \n',getAvailableLetters(lettersGuessed))
                        break
                    elif letts == 'n' or letts == 'N':
                        break
                    else:
                        print ('Please choose only from yes or no by typing Y or N')
                    
            elif letter in lettersGuessed and letter in secretWord:
                lettersGuessed.append(letter)
                print ('letter was already used, here are your remaining letters: \n',getGuessedWord(secretWord,lettersGuessed))
                print (getAvailableLetters(lettersGuessed))
            else:
                lettersGuessed.append(letter)
                print ('letter was already used, here are your remaining letters: \n',getGuessedWord(secretWord,lettersGuessed))
                print (getAvailableLetters(lettersGuessed))

        else:
            print ('NICE! You completed the word ', secretWord)
            break
        
    if (5- Mistakes) == 0:                                                      #conditional statement checking when you have commited 5 mistakes
        print ('You have used up all your tries to find the word, sorry!\n')    #if condition is met, game will end.
        print ('Game over! The secret word is: ',secretWord, '\n')



print ('Welcome to hangaroo! this game will be played with categories from fruits and vegetables')
ChooseWord = 0                          #The Code that will run the 5 functions from earlier
secretWord = loadWords(ChooseWord)      #ChooseWord was given a value of 0 to initiate it but not necessary
print(Hangaroo(secretWord))

