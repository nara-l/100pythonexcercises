import string
for letter in string.ascii_lowercase:
    filename = letter + ".txt"
    with open('files/' + filename, 'w') as file:
        file.write(letter)

