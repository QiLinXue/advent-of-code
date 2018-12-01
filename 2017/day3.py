from aocd import get_data
data = get_data(day=3, year=2017)

content = int(data)

def part1(inputData):
    spiral = [ [ 0 for i in range(515) ] for j in range(515) ]
    x = len(spiral)//2
    y = len(spiral)//2
    center = (x,y)

    lastMove = "down"
    for i in range(1,len(spiral)*len(spiral)+1):
        spiral[y][x] = i

        if lastMove == "down" and spiral[y][x+1] == 0:
            x = x + 1
            lastMove = "right"
        elif lastMove == "up" and spiral[y][x-1] == 0:
            x = x - 1
            lastMove = "left"
        elif lastMove == "right" and spiral[y-1][x] == 0:
            y = y - 1
            lastMove = "up"
        elif lastMove == "left" and spiral[y+1][x] == 0:
            y = y + 1
            lastMove = "down"
        
        elif lastMove == "down":
            y = y + 1
        elif lastMove == "up":
            y = y - 1
        elif lastMove == "right":
            x = x + 1
        elif lastMove == "left":
            x = x - 1
    
    index = (-1,-1)
    key = inputData
    for i in range(0,len(spiral)):
        if key in spiral[i]:
            index = (spiral[i].index(key),i)
    return abs(center[0]-index[0])+abs(center[1]-index[1])

def part2(inputData):
    spiral = [ [ 0 for i in range(515) ] for j in range(515) ]
    x = len(spiral)//2
    y = len(spiral)//2

    spiral[x][y] = 1
    lastMove = "right"
    x = x + 1
    for i in range(2,len(spiral)*len(spiral)+1):
        miniSum = 0
        for a in range(-1,2):
            for b in range(-1,2):
                if x+a >= 0 and x+a < len(spiral) and y+b >= 0 and y+b < len(spiral):
                    miniSum += spiral[y+b][x+a]
        
        spiral[y][x] = miniSum

        if miniSum > inputData:
            return miniSum
        if lastMove == "down" and spiral[y][x+1] == 0:
            x = x + 1
            lastMove = "right"
        elif lastMove == "up" and spiral[y][x-1] == 0:
            x = x - 1
            lastMove = "left"
        elif lastMove == "right" and spiral[y-1][x] == 0:
            y = y - 1
            lastMove = "up"
        elif lastMove == "left" and spiral[y+1][x] == 0:
            y = y + 1
            lastMove = "down"
        
        elif lastMove == "down":
            y = y + 1
        elif lastMove == "up":
            y = y - 1
        elif lastMove == "right":
            x = x + 1
        elif lastMove == "left":
            x = x - 1
    return -1    



print(part1(content))
print(part2(content))