def remove_empty_strings(inputList):
    return list(filter(None, inputList))


file = open("input.txt")

input = []
for line in file:
    input.append(line[:-1])
    print(line[:-1])

total = 0

for lineIndex, line in enumerate(input):
    print(f"\n\n----- Line: {lineIndex} -----")
    splitLine = line.split("|")
    winningNumbers = remove_empty_strings(splitLine[0].split(":")[1].split(" "))
    cardNumbers = remove_empty_strings(splitLine[1].split(" "))

    print("splitline .....:", splitLine)
    print("winningNumbers :", winningNumbers)
    print("cardNumbers ...:", cardNumbers)
    
    cardMatches = 0
    for number in cardNumbers:
        if number in winningNumbers:
            cardMatches += 1

    if cardMatches > 0: total += 2**(cardMatches-1)

    print("cardMatches ...:", cardMatches)

print("\n\n\ntotal..........:", total)