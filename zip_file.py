# create a script to generate a file where english alphabeths are ligned side by side
import string
letters = zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2])

with open('doubleletters.txt', 'w') as file:
    for k, v in letters:
        pair = k + v
        file.write(pair+"\n")



letters = zip(string.ascii_lowercase[0::2], string.ascii_lowercase[1::2], string.ascii_lowercase[2::2])

print(letters)
with open('tripleletters.txt', 'w') as file:
    for i, k, v in letters:
        pair = i + k + v
        file.write(pair+"\n")

