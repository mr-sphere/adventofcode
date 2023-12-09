def calculate_distance(holdTime, timeLimit):
    return holdTime * (timeLimit - holdTime)

file = open("input.txt")

input = []
for line in file:
    input.append(line[:-1])

raceTimes = list(filter(None, input[0].split(":")[1].split(" ")))
raceRecords = list(filter(None, input[1].split(":")[1].split(" ")))

possibleRecords = []
for raceIndex, raceRecord in enumerate(raceRecords):

    lastRecord = 0
    winningHoldTimes = 0
    for holdTime in range(int(raceTimes[raceIndex])):
        distance = calculate_distance(holdTime, int(raceTimes[raceIndex]))
        if distance > int(raceRecord): winningHoldTimes += 1

    possibleRecords.append(winningHoldTimes)

total = 1
for record in possibleRecords:
    total *= record

print(total)