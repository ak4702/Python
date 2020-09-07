# Appllicant name: Brian Chan
# Email: brianyeung8@gmail.com
# Task for Vestan part-time application
# In this apporach, I store the counted characters inside another array to simplify things out
# but it can also be done with a for loop to check if a character is already being counted
# For actual implementation, functions can also be constructed for reusability

string = "The new patients were an 18-year-old female student who returned from Britain on Friday, and a 61-year-old man whose granddaughter and domestic helper was infected previously, according to Dr Chuang Shuk-kwan, head of the Centre for Health Protection’s communicable disease branch."
char_counter = []
counted_char = []

for character in string:
    char = character

    # convert character to lower for case-insensitive implementation
    if(char.isupper()):
        char = char.lower()

    # checking if character already exists in array
    if(char in counted_char):
        continue # continue if already counted to save computational recources
    else:
        count = string.count(char) # call .count() to count the occurance in string once and for all
        char_counter.append([char, count])  # store the [character, count] array inside char_counter
        counted_char.append(char)
        # store the counted character in dictionary, along with it's index in char_counter array.

for item in char_counter:
    print(item)
