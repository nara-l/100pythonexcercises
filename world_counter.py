def word_counter(file_input):
    with open(file_input, 'r') as file:
        string_file = file.read()
    return len(string_file.split())


file_input = 'words1.txt'

word_count = word_counter(file_input=file_input)

print(word_count)
