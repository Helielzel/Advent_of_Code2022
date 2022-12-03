
f = open("input.txt", "r")
inputs = f.readlines()

half_1 = 0
half_2 = 0
total_sum = 0

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper()
dico = {i+1 : alpha[i] for i in range(0, len(alpha))}
dico = {v: k for k, v in dico.items()}

for elem in inputs:
    elem.strip("\n")
    half_1, half_2 = elem[:len(elem)//2], elem[len(elem)//2:]
    for item in half_1:
        if item in half_2:
            total_sum += dico[item]
            break

print(total_sum)