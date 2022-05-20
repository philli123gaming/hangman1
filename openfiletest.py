import random

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
print(selected_word_array)

hidden_word = []
for char in range(hidden_word_char_number):       #for each character in user input for characters
    hidden_word.append("_")                  #add _ to a duplicate variable