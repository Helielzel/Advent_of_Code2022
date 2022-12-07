f = open("input.txt", "r")
inputs_list = f.readlines()

input = inputs_list[0]
sequence = ""
result = 0

for i in range(len(input)):
    unique_list = []
    sequence += input[i]
    sequence = sequence[1:] if len(sequence) > 4 else sequence
    if (len(sequence) != 4):
        continue
    for char in sequence:
        if (char not in unique_list):
            unique_list.append(char)
    if len(unique_list) == 4:
        print(i + 1)
        exit()