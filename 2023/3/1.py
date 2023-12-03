
file = open("input.txt")

def contains_character(input_string):
    for char in input_string:
        if char.isnumeric() or char == "." or char == " ":
            continue
        return True
    return False

lines = []
for line in file:
    lines.append(line[:-1])


total = 0
preventDupeCount = 0
for l, line in enumerate(lines):
    
    print(f"----Line {l}----")
    for c, char in enumerate(line[:-1]):
        if preventDupeCount > 0: 
            preventDupeCount -= 1
            continue
        if char.isnumeric():
            countNumber = False
            numberGroup = f"{char}"
            nextChar = line[c+1]

            while nextChar.isnumeric():
                numberGroup = f'{numberGroup}{nextChar}'
                try:
                    nextChar = line[c+len(numberGroup)]
                except IndexError:
                    nextChar = "."
            
            rangeStart = max(0, c-1)

            if contains_character(lines[l-1][rangeStart:c+1+len(numberGroup)]) == True: countNumber = True
            elif contains_character(lines[l][rangeStart:c+1+len(numberGroup)]) == True: countNumber = True
            else:
                try:
                    if contains_character(lines[l+1][rangeStart:c+1+len(numberGroup)]) == True: countNumber = True
                except IndexError:
                    pass

            if not countNumber:
                print(f'\nSurrounding {numberGroup}:')
                print(lines[l-1][rangeStart:c+1+len(numberGroup)])
                print(lines[l][rangeStart:c+1+len(numberGroup)])
                try:
                    print(lines[l+1][rangeStart:c+1+len(numberGroup)])
                except:
                    pass
                
            if countNumber: total += int(numberGroup)

            preventDupeCount = len(numberGroup)


print(total)
