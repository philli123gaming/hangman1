import random
import string

pics = ["  +---+\n      |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="]  # Images used to sho hangman progress

answer = "neither"  # starting answer

while answer != "Y" or answer != "y":  # start confirmation
    answer = input("Do you want to play\n")
    answer = answer.lower()
    if answer == "y" or answer == "yes":
        print("Lets begin")
        break  # starts game
    if answer == "n":
        print("ok then Bye")
        quit()  # self explanatory will need to restart script
    elif answer != "n" and answer != "y":
        print("that answer doesnt work")  # catches any other answer that is unclear

hidden_word_char_number = ""
while type(hidden_word_char_number) == str:  # gives user the option to select the hidden words character count
    try:
        hidden_word_char_number = input("Between 3-10, how many characters do you want your hidden word to have\n")
        hidden_word_char_number = int(hidden_word_char_number)
        if hidden_word_char_number <= 2 or hidden_word_char_number > 10:
            print("That number was not between 1-10")
            continue
    except ValueError:  # stops user from entering anything other than a number
        print("That is not a number")

selected_word = ""
wordraffle = []
with open("wordlist3.txt") as wordlistdoc:
    for line in wordlistdoc:
        line = line.strip()
        if (len(line)) == hidden_word_char_number:
            # if the number of characters in one of the words lines matches the user input it is chosen
            wordraffle.append(line)
        elif hidden_word_char_number <= 2 or hidden_word_char_number > 10:
            print("No word could be found with that number of characters")
            quit()
    selected_word = random.choice(wordraffle)

selected_word_array = []
for selected_word_char in selected_word:
    selected_word_array.append(selected_word_char)

# print(selected_word)
# print(selected_word_array)

hidden_word = []
for char in range(hidden_word_char_number):  # for each character in user input for characters
    hidden_word.append("_")  # add _ to a duplicate variable
# print(hidden_word)

# print(pics[0])
# for pic in pics: #test pictures sourced from chrishorton
# print(pic)

failed_guesses = 0
lives_left = (7 - failed_guesses)
alphabet = string.ascii_letters

# variable list
state = "playing"
guess_attempts = []
guesses_made = 0

while state == "playing":  # games on
    char_list = []
    print(pics[failed_guesses])
    print(hidden_word, "\n")
    # print(len(guess_attempts))
    # print(guesses_made)
    if guesses_made == 0:
        print("no guesses made yet\n")
    elif guesses_made != 0 and len(guess_attempts) == 0:
        print("no Genuine guesses made yet\n")
    else:
        print("You have tried\n", guess_attempts)


    guess = input("Please enter a word or character (in lowercase if you would)\n")
    guess = guess.lower()
    if len(guess) < 1:
        print("Please enter something")
        continue

    for char in guess:
        if char not in alphabet:
            print("Character not in the alphabet\n")
            no_false_character = False
            break
        else:
            no_false_character = True
            break

    if not no_false_character:
        continue

    if guess in guess_attempts:
        print("you already tried this")
        continue

    elif "0" in guess or "1" in guess or "2" in guess or "3" in guess \
            or "4" in guess or "5" in guess or "6" in guess or "7" in guess \
            or "8" in guess or "9" in guess:
        print("numbers aren't accepted")
        continue
    elif guess not in guess_attempts and char in alphabet:
        guess_attempts.append(guess)

    guesses_made += 1
    if guess in selected_word:
        if len(guess) == 1:
            if guess in selected_word:
                for letterindex in range(len(selected_word)):
                    if (selected_word[letterindex] == guess):
                        char_list.append(letterindex)
                # print(char_list)
                # print(type(char_list[0]))
                for index in char_list:
                    # print(index)
                    char_list = []
                    hidden_word[index] = guess
                print("correct")
            else:
                failed_guesses += 1
                # print(failed_guesses)
                lives_left = (7 - failed_guesses)
                print("Incorrect ", lives_left, " lives left")
                # print(lives_left)


        elif len(guess) > 1:
            if guess == selected_word:
                print("continued")

    else:
        print("Incorrect guess \n")
        failed_guesses += 1
        # print(failed_guesses)
        lives_left = (7 - failed_guesses)
        print(lives_left, " lives left")
        # print(lives_left)
    if lives_left == 0 and selected_word_array != hidden_word:
        print("no lives left")
        print("Game Over")
        state = "finished"
        quit()
    elif selected_word_array == hidden_word or guess == selected_word:
        print(pics[failed_guesses])
        print(hidden_word)
        if lives_left == 7:
            print("In one try? How? anyway")
        elif lives_left == 0:
            print("Just barely but,")
        print("Congratulation You Win!")
        state = "finished"
        quit()
quit()
