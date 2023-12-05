file = open("input.txt", "r")

total = 0
for line in file:
    newLine = newLine = line
    for i, char in enumerate(line):
        if char.isnumeric():
            firstNumber = char
            break
        # print(line[i:i+5])
        if line[i:i+3] == "one":
            firstNumber = 1
            break
        if line[i:i+3] == "two":
            firstNumber = 2
            break
        if line[i:i+5] == "three":
            firstNumber = 3
            break
        if line[i:i+4] == "four":
            firstNumber = 4
            break
        if line[i:i+4] == "five":
            firstNumber = 5
            break
        if line[i:i+3] == "six":
            firstNumber = 6
            break
        if line[i:i+5] == "seven":
            firstNumber = 7
            break
        if line[i:i+5] == "eight":
            firstNumber = 8
            break
        if line[i:i+4] == "nine":
            firstNumber = 9
            break

        
    for i, char in enumerate(line):
        if char.isnumeric():
            lastNumber = char
            continue
        # print(line[i:i+5])
        if line[i:i+3] == "one":
            lastNumber = 1
            continue
        if line[i:i+3] == "two":
            lastNumber = 2
            continue
        if line[i:i+5] == "three":
            lastNumber = 3
            continue
        if line[i:i+4] == "four":
            lastNumber = 4
            continue
        if line[i:i+4] == "five":
            lastNumber = 5
            continue
        if line[i:i+3] == "six":
            lastNumber = 6
            continue
        if line[i:i+5] == "seven":
            lastNumber = 7
            continue
        if line[i:i+5] == "eight":
            lastNumber = 8
            continue
        if line[i:i+4] == "nine":
            lastNumber = 9
            continue

   
    print(f'Line = {line}')
    print(f'newLine = {newLine}')
    print(f'Add {int(str(firstNumber) + str(lastNumber))}')
    total += int(str(firstNumber) + str(lastNumber))
    print(f"Total = {total}\n\n\n")

file.close()
print(total)