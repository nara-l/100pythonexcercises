import string
def write_to_file(filename):

    with open(filename, "w") as file:

        for letter in string.ascii_lowercase:
            file.write(letter + "\n")

    return file

write_to_file('letters.txt') # if file is not there, write cretes the file
