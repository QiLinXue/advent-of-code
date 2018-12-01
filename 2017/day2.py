from aocd import get_data
data = get_data(day=2, year=2017)

content = [x.split() for x in data.split("\n")]

def part1(inputText):
    checkSum = 0
    for x in inputText:
        b = [int(i) for i in x]
        checkSum += max(b)-min(b)
    return checkSum

def part2(inputData):
    sum = 0
    abb = 0
    for x in inputData:
        b = [int(i) for i in x]
        for i in b:
            for j in b:
                if not i == j:
                    if(i % j == 0):
                        sum += i/j
    return sum

print(part1(content))
print(part2(content))