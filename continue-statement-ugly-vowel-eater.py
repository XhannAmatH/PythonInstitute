#   Author  :   XhannAmatH

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input()
vowels="aeiou"

for letter in user_word:
    # Complete the body of the for loop.
    if(letter.lower() in vowels):
        continue
    else:
        print(letter.upper())
