def Hangaroo (secretWord):                              #Main Function line of the whole code.
    Mistakes = 0   
    letts = 0                               
    lettersGuessed = []
    print ('Welcome to hangaroo!!')
    print ('The word is ', len(secretWord), ' letters long.')
    print ('You only have 5 times to make a mistake or the game will end. GOODLUCK!')       
    secretWord = secretWord.lower()
    
    while (5 - Mistakes) > 0:                                            #A 5 mistake marker is created
        if isWordGuessed(secretWord,lettersGuessed) == False:            #If user makes a mistake, marker would decrease, whilst making a
            letter = str(input('Please type a letter: ')).lower()        # correct answer will prompt them to keep going
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