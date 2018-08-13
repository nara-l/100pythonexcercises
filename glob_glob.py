import glob

letter_list = []
list_of_files = glob.iglob("files/*.txt")
for filename in list_of_files:
    with open(filename, 'r') as file:
        letter = file.read()
        letter_list.append(letter)

print(sorted(letter_list))

