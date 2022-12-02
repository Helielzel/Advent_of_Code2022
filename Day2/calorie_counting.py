
# ROCK = +1 -> A / X
# PAPER = +2 -> B / Y
# SCISSORS = +3 -> C / Z
# lose -> +0 : draw -> +3 ; win -> +6
# 


f = open("input.txt", "r")
inputs = f.readlines()

total_score = 0

for elem in inputs:
    if (elem[2] == "X"):
        total_score += 1
    if (elem[2] == "Y"):
        total_score += 2
    if (elem[2] == "Z"):
        total_score += 3

    #draw
    if (elem == "A X\n" or elem == "B Y\n" or elem == "C Z\n"):
        total_score += 3
        print("draw")
    #win
    if (elem == "A Y\n" or elem == "B Z\n" or elem == "C X\n"):
        total_score += 6
        print("win")
    #lose
    if (elem == "A Z\n" or elem == "B X\n" or elem == "C Y\n"):
        total_score += 0
        print("lose")
print(total_score)