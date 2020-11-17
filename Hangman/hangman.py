#!/usr/bin/python

import random
import time

print("\nWelcome to Hangman")
name = input("Enter your name: ")
print("Hello " + name + "! Best of luck!")
print("The game is about to start!\n Let's play Hangman!")


def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    words_to_guess = [
        "january",
        "border",
        "image",
        "film",
        "promise",
        "kids",
        "lungs",
        "doll",
        "rhyme",
        "damage",
        "plants",
    ]
    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""


def play_loop():
    global play_game
    play_game = input("Do you want to play again? y/n\n")
    while play_game not in ["y", "Y", "n", "N"]:
        play_game = input("Do you want to play again? y/n \n")
    if play_game == "y" or "Y":
        main()
    elif play_game == "n" or "N":
        print("Thanks for Playing!")
        exit()


def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess = input("This is the word: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in word:
        already_guessed.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1 :]
        display = display[:index] + guess + display[index + 1 :]
        print(display + "\n")

    else:
        count += 1

        if count == 1:
            print(
                "   _____ \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print("Wrong guess. " + str(limit - count) + " guesses reamining\n")

        elif count == 2:
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print("Wrong guess. " + str(limit - count) + " guesses reamining\n")

        elif count == 3:
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |     o\n"
                "  |      \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print("Wrong guess. " + str(limit - count) + " guesses reamining\n")

        elif count == 4:
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |     o\n"
                "  |    /|\ \n"
                "  |      \n"
                "  |      \n"
                "__|__\n"
            )
            print("Wrong guess. " + str(limit - count) + " last guess reamining\n")

        elif count == 5:
            print(
                "   _____ \n"
                "  |     |\n"
                "  |     |\n"
                "  |     |\n"
                "  |     o\n"
                "  |    /|\ \n"
                "  |    / \ \n"
                "  |      \n"
                "__|__\n"
            )
            print("Wrong guess. You have been hanged!\n")
            print("The word was:", already_guessed, word)
            play_loop()

    if word == "_" * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()

    elif count != limit:
        hangman()


main()

hangman()
