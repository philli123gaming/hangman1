import random

pics = ["  +---+\n      |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] #Images used to sho hangman progress

answer = "neither" #starting answer

while answer != "Y" or answer != "y": #start confirmation
    answer = input("Do you want to play\n")
    if answer == "Y" or answer == "y":
        break # starts game
    if  answer == "n" or answer == "N":
        print("ok then Bye")
        quit() # self explanatory will need to restart script
    elif answer != "N" and answer != "n" and answer != "Y" and answer != "y":
        print("that answer doesnt work") #catches any other answer that is unclear

print("Lets begin")

hidden_word_char_number = ""
while type(hidden_word_char_number) == str  : #gives user the option to select the hidden words character count
    try:
        hidden_word_char_number = input("Between 3-10, how many characters do you want your hidden word to have\n")
        hidden_word_char_number = int(hidden_word_char_number)
        if hidden_word_char_number <= 2 or hidden_word_char_number > 10:
            print("That number was not between 1-10")
            continue
    except ValueError: #stops user from entering anything other than a number
        print("That is not a number")
selected_word = ""
wordraffle = []
with open("wordlist3.txt") as wordlistdoc:
    for line in wordlistdoc:
        line = line.strip()

        if (len(line)) == hidden_word_char_number:   #if the number of characters in one of the words lines matches the user input it is chosen
            wordraffle.append(line)
        elif hidden_word_char_number <= 2 or hidden_word_char_number > 10:
            print("no word could be found with that number of characters")
            quit()
    selected_word = random.choice(wordraffle)

selected_word_array = []
for selected_word_char in selected_word:
    selected_word_array.append(selected_word_char)

print(selected_word)
#print(selected_word_array)

hidden_word = []
for char in range(hidden_word_char_number):       #for each character in user input for characters
    hidden_word.append("_")                  #add _ to a duplicate variable
#print(hidden_word)

#print(pics[0])
#for pic in pics: #test pictures ourced from chrishorton
#print(pic)

failedguesses = 0
lives_left = (7 - failedguesses)
alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                             #variable list
state = "playing"
guess_attempts = []
guesses_made = 0


while state == "playing":     #games on
    char_list = []
    print(pics[failedguesses])
    print(hidden_word)
    if guesses_made == 0:
        print("no guesses made yet\n")
    else:
        print("You have tried\n", guess_attempts)

    guess = input("please enter a word or character (in lowercase if you would)\n")

    if guess in guess_attempts:
        print("you already tried this")
        continue
    elif "0" in guess or "1" in guess or "2" in guess or "3" in guess \
        or "4" in guess or "5" in guess or "6" in guess or "7" in guess \
        or "8" in guess or "9" in guess:
        print("numbers aren't accepted")
        continue
    else:
        guess_attempts.append(guess)
        guesses_made += 1

    if guess in selected_word:
        if len(guess) == 1:
            if guess in selected_word:
                for letterindex in range(len(selected_word)):
                    if (selected_word[letterindex] == guess):
                        char_list.append(letterindex)
                print(char_list)
                print(type(char_list[0]))
                for index in char_list:
                    #print(index)
                    char_list = []
                    hidden_word[index] = guess
                print("correct")
            else:
                failedguesses += 1
                #print(failedguesses)
                lives_left = (7 - failedguesses)
                print("Incorrect ", lives_left, " lives left")
                #print(lives_left)


        elif len(guess) > 1:
            for guessed_char in guess:
                if guessed_char in selected_word:
                    for letterindex in range(len(selected_word)):
                        if (selected_word[letterindex] == guessed_char):
                            char_list.append(letterindex)
                    #print(char_list)
                    #print(type(char_list[0]))
                    for index in char_list:
                        char_list = []
                        hidden_word[index] = guessed_char

                else:
                    failedguesses += 1
                    #print(failedguesses)
                    lives_left = (7 - failedguesses)
                    print("Incorrect ", lives_left, " lives left")
                    #print(lives_left)
            print("correct")

        elif len(guess) < 1:
            continue

        elif guess not in alphabet:
            print("guess not in the alphabet\n")
            continue

    elif "0" in guess or "1" in guess or "2" in guess or "3" in guess\
        or "4" in guess or "5" in guess or "6" in guess or "7" in guess\
        or "8" in guess or "9" in guess:
        print("numbers aren't accepted")

    else:
        print("incorrect guess not even close\n")
        failedguesses += 1
        #print(failedguesses)
        lives_left = (7 - failedguesses)
        print(lives_left, " lives left")
        #print(lives_left)
    if lives_left == 0 and selected_word_array != hidden_word:
        print("no lives left")
        print("Game Over")
        state = "finished"
        quit()
    elif selected_word_array == hidden_word:
        print(pics[failedguesses])
        print(hidden_word)
        print(lives_left)
        if lives_left == 7:
            print("In one try? How? anyway")
        elif lives_left == 0:
            print("Just barely but,")
        print("Congratulation You Win!")
        state = "finished"
        quit()


