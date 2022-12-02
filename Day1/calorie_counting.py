
f = open("input.txt", "r")
inputs = f.readlines()

total_score = 0
all_elves = list()
one_elf = list()

for elem in inputs:
    if (elem != "\n"):
        one_elf.append(int(elem))
    if (elem == "\n" or elem == EOFError):
        all_elves.append(sum(one_elf))
        one_elf = []

print(max(all_elves))