file = open("input.txt")

input = []
for line in file:
    input.append(line[:-1])

directions = input[0]
directionsLength = len(directions)

locationMap = []
for line in input[2:]:
    locationMap.append(line[0:3])

locations = []
for letterIndex, letter in enumerate(locationMap):
    if letter.endswith("A"):
        locations.append(locationMap[letterIndex])

print(locations)

index = 0

zDestinations = 0
while zDestinations != len(locations):
    zDestinations = 0
    direction = directions[index % directionsLength]
    # print("locations: ", locations)
    for pathIndex, path in enumerate(locations):
        # print("path: ", path)
        location = locationMap.index(path)
        if direction == "L":
            nextAdress = input[location+2][-9:-6]
            locations[pathIndex] = nextAdress
        else:
            nextAdress = input[location+2][-4:-1]
            locations[pathIndex] = nextAdress

        if nextAdress[-1] == "Z":
            zDestinations += 1
            if zDestinations > 1:
                print("zDestinations:", zDestinations, "index: ", index)

    index +=1
    if index > 10000000:
        print("---INDEX LIMIT---")
        quit()

print("\n\n", index)