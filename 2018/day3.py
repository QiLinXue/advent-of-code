from aocd import get_data
data = get_data(day=3, year=2018)

content = [x for x in data.split("\n")]
realContent = []
for i in range(1,len(content)):
    b0 = content[i].index('@')
    b1 = content[i].index(',')
    b2 = content[i].index(':')
    b3 = content[i].index('x')
    num1 = int(content[i][b0+2:b1])
    num2 = int(content[i][b1+1:b2])
    width = int(content[i][b2+2:b3])
    height = int(content[i][b3+1:len(content[i])])

    temp = [num1,num2,width,height,i]
    realContent.append(temp)

# Determines array size
maxX = max([i[0]+i[2] for i in realContent])
maxY = max([i[1]+i[3] for i in realContent])

# Initializes the array
field = [ [ 0 for i in range(maxY) ] for j in range(maxX) ]

def part1():
    for j in realContent:
        for x in range(j[0],j[0]+j[2]):
            for y in range(j[1],j[1]+j[3]):

                if field[y][x] == 0:
                    field[y][x] = 1
                elif field[y][x] == 1:
                    field[y][x] = 2

    count = 0
    for j in field:
        count += j.count(2)
    
    return count

def part2():
    field = [ [ 0 for i in range(maxY) ] for j in range(maxX) ]

    for j in realContent:
        for x in range(j[0],j[0]+j[2]):
            for y in range(j[1],j[1]+j[3]):
                if field[y][x] == 0:
                    field[y][x] = j[4]
                else:
                    field[y][x] = -1

    count = [0 for i in realContent]

    for x in range(len(field)):
        for y in range(len(field)):
            if field[y][x] > 0:
                count[field[y][x]-1] += 1
    
    for i in range(len(count)):
        product = realContent[i][2]*realContent[i][3]
        if product == count[i]:
            return i+1
    return -1

print(part1())
print(part2())
