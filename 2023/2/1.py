import re


def removeNumbers(input_string):
    return re.sub(r'[^a-zA-Z]', '', input_string)

def removeLetters(input_string):
    return re.sub(r'[^0-9]', '', input_string)

file = open("input.txt")

total = 0
for line in file:
    draws = line.replace(" ", "").split(":")[1][:-1].split(";")
    print(draws)
    
    gameId = int(line.split(":")[0][4:])

    for draw in draws:
        possible = True
        for colorDraw in draw.split(","):
            color = removeNumbers(colorDraw)
            amount = int(removeLetters(colorDraw))
            if color == "red" and amount > 12: 
                possible = False
                break
            if color == "green" and amount > 13: 
                possible = False
                break
            if color == "blue" and amount > 14: 
                possible = False
                break

        if not possible:
            break

    if possible:
        total += gameId

print(total)