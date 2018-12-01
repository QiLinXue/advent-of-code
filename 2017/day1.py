from aocd import get_data
content = get_data(day=1, year=2017)

def part1(inputData):
    inputData = list(inputData)
    sum = 0
    for i in range(0,len(inputData)-1):
        if inputData[i] == inputData[i+1]:
            sum += int(inputData[i])
    if inputData[0] == inputData[len(inputData)-1]:
        sum += int(inputData[0])

    return sum

def part2(inputData):
    inputData = list(inputData)
    size = len(inputData)/2
    sum = 0
    for i in range(0,len(inputData)):
        n = i+size
        if n >= len(inputData):
            n -= len(inputData)
        if inputData[i] == inputData[int(n)]:
            sum += int(inputData[i])

    return sum

print(part1(content))
print(part2(content))