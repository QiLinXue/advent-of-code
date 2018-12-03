from aocd import get_data
data = get_data(day=2, year=2018)

content = [x for x in data.split()]

def part1(inputText):
    sum2 = 0
    sum3 = 0
    for i in inputText:
        for j in list(i):
            if(i.count(j) == 2):
                sum2 += 1
                break
    for i in inputText:
        for j in list(i):
            if(i.count(j) == 3):
                sum3 += 1
                break
    return sum2*sum3

def dif(a, b):
    return sum(i != j for i, j in zip(a, b))

def part2(inputText):
    mostCorrect = [-1,"str","str"]
    for i in range(len(inputText)):
        for j in range(i+1,len(inputText)):
            difference = dif(inputText[i],inputText[j])
            if mostCorrect[0] == -1 or difference < mostCorrect[0]:
                mostCorrect[0] = difference
                mostCorrect[1] = inputText[i]
                mostCorrect[2] = inputText[j]
    
    revised = []
    for i in range(len(mostCorrect[1])):
        if mostCorrect[1][i] == mostCorrect[2][i]:
            revised.append(mostCorrect[1][i])

    return ''.join(revised)
    
print(part1(content))
print(part2(content))