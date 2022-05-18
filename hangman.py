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
while type(hidden_word_char_number) == str: #gives user the option to select the hidden words character count
    try:
        hidden_word_char_number = input("how many characters do you want your hidden word to have\n")
        hidden_word_char_number = int(hidden_word_char_number)
    except ValueError: #stops user from entering anything other than a number
        print("That is not a number")

#wordlistdoc = open("wordlist2.txt","r")
selected_word = ""
with open("wordlist2.txt") as wordlistdoc: #txt document as a word base
    for line in wordlistdoc:               #for each line in the text file
        print(line)                       #display the line
        print(len(line)-1) # -1 is used becuase it prints the char count +1
        if (len(line)-1) == hidden_word_char_number:   #if the number of characters in one of the words lines matches the user input it is chosen
            selected_word = line


print(selected_word)

hidden_word = []
for char in range(hidden_word_char_number):       #for each character in user input for characters
    hidden_word.append("_")                  #add _ to a duplicate variable
print(hidden_word)

#print(pics[0])
#for pic in pics: #test pictures ourced from chrishorton
    #print(pic)

failedguesses = 0
lives_left = (8 - failedguesses)
alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
                             #variable list
print(pics[failedguesses])
state = "playing"
char_list = []

while state == "playing":     #games on
    guess = input("please enter a character\n")
    if len(guess) != 1:
        print("more or less than 1 character detected\n")
        continue
    elif guess not in alphabet:
        print("guess not in the alphabet\n")
        continue
    else:
        char_list = []
        if guess in selected_word:
            for letterindex in range(len(selected_word)):
                if (selected_word[letterindex - 1] == guess):
                    char_list.append(letterindex)
            print(char_list)
            print(type(char_list[0]))
            for index in char_list:
                print(index)
                hidden_word[(index - 1)] = guess
                print(hidden_word)
                print("correct")
                print(pics[failedguesses])
        else:
            failedguesses += 1
            print(failedguesses)
            lives_left = (7 - failedguesses)
            print(lives_left)
            if lives_left == 0:
                print("Incorrect no lives left")
                print(pics[failedguesses])
                print("Game Over")
                state = "finished"
                quit()
            else:
                print("Incorrect ",lives_left," lives left")
                print(pics[failedguesses])

