# Liam Pruden
# 100924161

import random

def winningWord(wordLength):
    """
    Selects and returns a random word from list based on the word length.
    """
    if wordLength == 4:
        wordsList = ["past", "tech", "golf", "goose"]
    elif wordLength == 5:
        wordsList = ['apple', 'goose']
    return random.choice(wordsList)

def lengthOfWord():
    """
    Prompts the user to select the difficulty level by choosing the word length.
    """
    while True:
        try:
            wordLength = int(input("Select your difficulty: \n Level 1(4 letters). \n Level 2(5 letters). "))
            if wordLength == 1:
                return 4 
            elif wordLength == 2:
                return 5
            else:
                print("Pick a level from 1-2")
        except ValueError:
            print("Input invalid pick level 1 or 2")

def numberOfGuesses():
    """
    Allows the user to specify the number of guesses they want.
    """
    while True:
        try:
            numberOfGuesses = int(input("Select your difficulty(Amount of Guesses): "))
            if numberOfGuesses >= 1 and numberOfGuesses <= 10:
                print("Finding a random word...")
                return numberOfGuesses
            else:
                print("Please pick a Level from 1-10.")
        except ValueError:
            print("Input invalid pick level 1 or 2")

def play_game():
    """
    Main function to play the "Guess-the-letters" game.
    Handles the game logic including user guesses, tracking correct and incorrect guesses,
    and determining when the game ends.
    """
    wordLength = lengthOfWord()
    word = winningWord(wordLength)
    guessesLeft = numberOfGuesses()
    hiddenWord = ['*' for i in word]
    guessedLetters = set()
    correctLetters = set()

    while guessesLeft > 0:
        print("Word is: ", hiddenWord)
        print("Guesses remaining: ", guessesLeft)
        print("Guessed letters:", guessedLetters)
        guess = input("Guess the letter: ").lower()
        
        if guess == "stop" or guess == "exit":  # Check for 'stop' or 'exit'
            print("Game Ends!")
            return



        inputChecker = len(guessedLetters)

        if  inputChecker!= 0 or not guess.isalpha():
            print("Only one letter allowed (no cheating!).")
            continue

        if guess in guessedLetters:
            print(guess, "has already been guessed.")
            continue
        else:
            guessedLetters.add(guess)

        # Check if the guess is correct
        if guess in word:
            print("******** GUESS CORRECT ************")
            correctLetters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    hiddenWord[i] = guess
            if set(word) == correctLetters:
                print("Congratulations! You guessed the word: ", word)
                return
        else:
            guessesLeft -= 1
            print("Incorrect guess. You have ", guessesLeft, "guesses left. ")




if __name__ == "__main__":
    # Main loop to keep the game running
    while True:
        play_game()

        play_again = input("Play again?[Y/N]").lower()
        if play_again != 'y':
            print("I hope you had fun!")
            break
