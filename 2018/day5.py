from aocd import get_data
content = get_data(day=5, year=2018)

def polymerLength(polymer):
    notDone = True
    j = -1
    while notDone:
        for i in range(len(polymer)):
            j += 1
            if j < len(polymer) - 1:
                # print(j,polymer[j],polymer[j+1])
                if not polymer[j] == polymer[j+1] and polymer[j].lower() == polymer[j+1].lower():
                    # print("a",polymer,i)
                    polymer = polymer[:j]+polymer[j+2:]
                    # print("b",polymer)
                    if j > 1:
                        j -= 1
                    # if j > 2:
                    #     j -= 1
                    j -= 1
                    break
            if j == len(polymer) - 1:
                notDone = False

    return polymer

def partOne(polymer):
    return len(polymerLength(polymerLength(polymer)))

def partTwo(poly):
    shortest = -1
    for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        polymer = poly
        toRun = l.lower() in polymer or l in polymer

        if l.lower() in polymer:
            lo = polymer.count(l.lower()) 
            polymer = polymer.replace(l.lower(),"",lo)
        
        if l in polymer:
            up = polymer.count(l)
            polymer = polymer.replace(l,"",up)
        
        if toRun:
            leng = partOne(polymer)
            if leng < shortest or shortest == -1:
                shortest = leng

    return shortest

print(partOne(content))
print((partTwo(content)))
