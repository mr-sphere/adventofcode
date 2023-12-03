file = open("input.txt")

lines = []
for line in file:
    lines.append(line[:-1])


total = 0
preventDupeCount = 0
for l, line in enumerate(lines):
    
    print(f"\n\n----Line {l}----")
    for c, char in enumerate(line[:-1]):
        if preventDupeCount > 0: 
            preventDupeCount -= 1
            continue
        if char == "*":
            surroundingChars = []

            if l > 0: surroundingChars.append(lines[l-1][c-1:c+2])
            surroundingChars.append(lines[l][c-1:c+2])
            surroundingChars.append(lines[l+1][c-1:c+2])

            print(f'\nSurrounding *:')
            print(surroundingChars[0])
            print(surroundingChars[1])
            print(surroundingChars[2])

            for ll, localLine in enumerate(surroundingChars):
                for lc, localChar in enumerate(surroundingChars):
                    if lc.isnumeric():
                        


print(total)
