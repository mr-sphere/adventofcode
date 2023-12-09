import re

def calculate_distance(holdTime, timeLimit):
    return holdTime * (timeLimit - holdTime)

file = open("input.txt")

input = []
for line in file:
    input.append(line[:-1])

raceTime = int(re.sub(r'\s', '', input[0].split(":")[1]))
raceRecord =  int(re.sub(r'\s', '', input[1].split(":")[1]))
print(raceTime)
print(raceRecord, "\n\n")

possibleRecords = []
total = 0
winningHoldTimes = 0
for holdTime in range(raceTime):
    distance = calculate_distance(holdTime, raceTime)
    if distance > raceRecord:
        total = (raceTime - (holdTime*2)) + 1
        print("holdTime", holdTime)
        break

print(total)