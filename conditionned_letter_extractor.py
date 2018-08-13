import glob

letter_list = []
python_letters = "python"

for filename in glob.glob("files/*.txt"):
    with open(filename, 'r') as file:
        letter = file.read()
        if letter in python_letters:
            letter_list.append(letter)

print(letter_list)

