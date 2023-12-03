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

    reds = []
    greens = []
    blues = []
    
    for draw in draws:
        for colorDraw in draw.split(","):
            color = removeNumbers(colorDraw)
            amount = int(removeLetters(colorDraw))
            if color == "red":
                reds.append(amount)
            if color == "green": 
                greens.append(amount)
            if color == "blue": 
                blues.append(amount)

    

    if reds: minRed = max(reds)
    else: minRed = 0
    if greens: minGreen = max(greens)
    else: greens = 0
    if blues: minBlue = max(blues)
    else: minBlue = 0

    power = minRed*minGreen*minBlue

    total += power

print(total)