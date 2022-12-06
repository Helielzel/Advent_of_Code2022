f = open("input.txt", "r")
inputs = f.readlines()

crates = ["RHMPZ", "BJCP", "DCLGHNS", "LRSQDMTF", "MZTBQPSF", "GBZSFT", "VRN", "MCVDTLGP", "LMFJNQW"]
how_many_to_move = 0
solution = ""

def swap(how_many_to_move, from_w, to_w, crates):
    tmp = ""
    for i in range(how_many_to_move):
        tmp += crates[from_w - 1][i]
    crates[from_w - 1] = crates[from_w - 1][how_many_to_move:]
    tmp = tmp[::-1]
    crates[to_w - 1] = tmp + crates[to_w - 1]
    return (crates)

for elem in inputs:
    instruction = elem.split(" ")
    if (instruction[0] != "move"):
        continue
    crates = swap(int(instruction[1]), int(instruction[3]), int(instruction[5]), crates)

for stack in crates:
    solution += stack[0]
print(solution)