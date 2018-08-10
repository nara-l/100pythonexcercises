import glob
letter_list = []

for filename in glob.glob("files/*.txt"):
    with open(filename, 'r') as file:
        letter = file.read()
        letter_list.append(letter)

print(sorted(letter_list))

