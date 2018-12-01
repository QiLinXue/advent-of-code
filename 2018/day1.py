from aocd import get_data
data = get_data(day=1, year=2018)

content = [int(x) for x in data.split()]

def part1(inputText):
    return sum(inputText)

def part2(inputData):
    frequency = 0
    seen = set([0])

    while(True):
        for i in content:
            frequency += i
            if frequency in seen:
                return frequency
            seen.add(frequency)

print(part1(content))
print(part2(content))