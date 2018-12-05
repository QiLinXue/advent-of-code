from aocd import get_data
content = get_data(day=4, year=2018)

numGuards = content.count("Guard")
content = content.split("\n")
content.sort()

schedule = [[["a"],["0" for i in range(60)]] for j in range(numGuards)]
currentGuard = 0
currentSpot = -1

startTime = 0
for i in range(0,len(content)):
  line = content[i]
  if "Guard" in line:
    currentSpot += 1
    b1 = line.index("b")
    currentGuard = int(line[26:b1-1])
    schedule[currentSpot][0] = currentGuard

    startTime = int(line[15:17])

    for j in range(startTime,60):
      schedule[currentSpot][1][j] = "1"

  if "wakes" in line:
    startTime = int(line[15:17])
    for j in range(startTime,60):
      schedule[currentSpot][1][j] = "1"

  if "falls" in line:
    startTime = int(line[15:17])
    for j in range(startTime,60):
      schedule[currentSpot][1][j] = "X"

def part1():
    count = []
    for i in schedule:
        if i[0] in [j[0] for j in count]:
            num = count[[j[0] for j in count].index(i[0])][1]
            num += i[1].count("X")
            count[[j[0] for j in count].index(i[0])][1] = num
        else:
            num = i[1].count("X")
            count.append([i[0],num])

    maxSleep = max([i[1] for i in count])
    maxId = count[[i[1] for i in count].index(maxSleep)][0]

    sleepiestMin = (-1,-1)
    for i in range(0,60):
        miniSum = 0
        for j in schedule:
            if j[0] == maxId and j[1][i] == 'X':
                miniSum += 1
        if miniSum > sleepiestMin[1]:
            sleepiestMin = (i,miniSum)

    return sleepiestMin[0]*maxId

def part2():
    elf_list = []
    for i in schedule:
        if not i[0] in elf_list:
            elf_list.append(i[0])

    # Schedule in the format of [[elfId],[0] * 60] * number of elves
    sleepiestElf = (0, 0, 0)
    for elf in elf_list:
        sleepiestMin = (-1,-1)
        for j in range(0,60):
            miniSum = 0
            for k in schedule:
                if k[0] == elf and k[1][j] == 'X':
                    miniSum += 1
            if miniSum > sleepiestMin[1]:
                sleepiestMin = (j,miniSum)
        
        if sleepiestMin[1] > sleepiestElf[1]:
            sleepiestElf = (elf, sleepiestMin[1],sleepiestMin[0])

    return sleepiestElf[0] * sleepiestElf[2]

print(part1())
print(part2())