def word_counter(file_input):
    with open(file_input, 'r') as file:
        string_file = file.read()
    return len(string_file.split())

# METHOD 2 IMPORT RE AND USE RE ON SPLIT

import re

def word_counter(file_input):
    with open(file_input, 'r') as file:
        string_file = file.read()
        # We're using the split method from re module and the expression ",| " is meant to replace commas with spaces.
        re_string_file = re.split(",| ", string_file)
    return len(re_string_file)


file_input = 'words2.txt'

word_count = word_counter(file_input=file_input)

print(word_count)
