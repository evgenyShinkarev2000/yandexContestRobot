def doLineMove(possibleStepsCount, beginPoint, direction):
    return (beginPoint[0] + possibleStepsCount * direction[0],
            beginPoint[1] + possibleStepsCount * direction[1])


def makePossibleStepsCounts(levelDeep, leftSteps):
    possibleStepsCounts = []
    lineLength = levelDeep * 2
    possibleStepsCounts.append(min((levelDeep - 1) * 2 + 1, leftSteps))
    leftSteps -= possibleStepsCounts[0]
    for i in range(0, 2):
        possibleStepsCounts.append(min(lineLength, leftSteps))
        leftSteps -= lineLength

    possibleStepsCounts.append(min(lineLength + 1, leftSteps))
    leftSteps -= possibleStepsCounts[3]

    return possibleStepsCounts


def solveLeftSteps(leftSteps): #unbuged
    levelSteps = 1
    levelDeep = 0

    while leftSteps >= levelSteps:
        levelDeep += 1
        leftSteps -= levelSteps
        levelSteps = levelDeep * 8

    return (leftSteps, levelDeep)


def findBeginPoint(levelDeep):
    if levelDeep == 0:
        return 0, 0
    return -levelDeep, levelDeep - 1


def findPoint(stepCount):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    leftSteps, levelDeep = solveLeftSteps(stepCount)
    currentPoint = findBeginPoint(levelDeep)
    possibleStepsCounts = makePossibleStepsCounts(levelDeep, leftSteps)

    for i in range(0, 4):
        if possibleStepsCounts[i] <= 0:
            break
        currentPoint = doLineMove(possibleStepsCounts[i], currentPoint, directions[i])

    return currentPoint[0], currentPoint[1]


f = open("input.txt", "r")
r = findPoint(int(f.read()))
f.close()
f = open("output.txt", "w")
f.write(" ".join(map(str, r)))

# print(findPoint(int(input())))

