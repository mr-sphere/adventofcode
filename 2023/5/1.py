file = open("input.txt")

input = []
for line in file:
    input.append(line[:-1])



# make function that does the conversions
# TODO make conversionTable format first
def convert(numberToConvert, conversionTable):
    0