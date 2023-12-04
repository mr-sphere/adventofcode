def remove_empty_strings(inputList):
    return list(filter(None, inputList))


file = open("input.txt")

input = []
copies = []
for line in file:
    input.append(line[:-1])
    copies.append(1)
    print(line[:-1])

total = 0

for lineIndex, line in enumerate(input):
    print(f"\n\n----- Line: {lineIndex} -----")
    ownCopies = copies[lineIndex]
    splitLine = line.split("|")
    winningNumbers = remove_empty_strings(splitLine[0].split(":")[1].split(" "))
    cardNumbers = remove_empty_strings(splitLine[1].split(" "))

    print("ownCopies .....:", ownCopies)
    print("splitline .....:", splitLine)
    print("winningNumbers :", winningNumbers)
    print("cardNumbers ...:", cardNumbers)
    
    cardMatches = 0
    for number in cardNumbers:
        if number in winningNumbers:
            cardMatches += 1

    for i in range(cardMatches):
        copies[lineIndex+i+1] += ownCopies

    print("cardMatches ...:", cardMatches)
    print("copies:",copies)

total = sum(map(float, copies))

print("\n\n\ntotal..........:", total)