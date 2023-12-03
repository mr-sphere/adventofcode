file = open("input.txt")

lines = []
for line in file:
    lines.append(line[:-1])


total = 0
for l, line in enumerate(lines):
    
    print(f"\n\n----Line {l}----")
    for c, char in enumerate(line[:-1]):
        if char == "*":
            surroundingChars = []

            if l > 0: surroundingChars.append(lines[l-1][c-1:c+2])
            else: surroundingChars.append("...")
            surroundingChars.append(lines[l][c-1:c+2])
            surroundingChars.append(lines[l+1][c-1:c+2])

            print(f'\nSurrounding *:')
            print(surroundingChars[0])
            print(surroundingChars[1])
            print(surroundingChars[2])
            print('\n')

            surroundingNumbers = []
            preventDupeCount = 0
            for ll, localLine in enumerate(surroundingChars):
                for lc, localChar in enumerate(localLine):
                    if preventDupeCount > 0:
                        preventDupeCount -= 1
                        continue
                    print("(indexes) | ll", ll, "| lc", lc)
                    if localChar.isnumeric():
                        
                        nextChar = lines[l+(ll-1)][c+(lc-1)-1]
                        newNumber = str(localChar)
                        print("initialnew = ", newNumber)
                        index = 1
                        while nextChar.isnumeric():
                            print("< nextChar =", nextChar)
                            print("< newNumber =" ,newNumber)
                            newNumber = f"{nextChar}{newNumber}"
                            print("< newNumber set to", newNumber)
                            if c+lc-index >= 0:
                                nextChar = lines[l+(ll-1)][c+lc-index-2]
                            else: nextChar="."
                            index += 1
                            preventDupeCount -= 1

                        print(":: newNumber =", newNumber)
                        nextChar = lines[l+(ll-1)][c+lc]
                        print(":: nextChar = ", nextChar)
                        index = 1
                        while nextChar.isnumeric():
                            print("> nextChar = ", nextChar)
                            print("> newNumber =" ,newNumber)
                            newNumber = f"{newNumber}{nextChar}"
                            print("> newNumber set to", newNumber)
                            try:
                                nextChar = lines[l+(ll-1)][c+lc+index]
                            except IndexError:
                                break

                            index += 1
                        print("final newNumber =" ,newNumber)
                        surroundingNumbers.append(newNumber)

                        preventDupeCount += min(2-lc, len(newNumber))

            if len(surroundingNumbers) == 2: total += int(surroundingNumbers[0])  * int(surroundingNumbers[1])
            print("surrounding full numbers =", surroundingNumbers)

print(total)
