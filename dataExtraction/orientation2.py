import sys
import collections

SERVE = "Serve"
SERVE_SEC = "2nd Serve"
RET_SERVE = "Serve Return"
RET_NORMAL = "Normal Return"
FOREHAND = "Forehand"
BACKHAND = "Backhand"

RES_WIN = "Win Point"
RES_ERROR = "Error"
RES_SERVE_SEC = SERVE_SEC
RES_RET_SERVE = RET_SERVE
RES_RET_NORMAL = RET_NORMAL

T = "T"
K = "K"
M = "M"
S = "S"


orientations = []
servers = []

with open("orientations.csv", "r") as file:
    file.readline()

    for line in file:
        gameNo, server, kPos, sPos, tPos, mPos = line.strip().split(",")

        orientations.append((kPos, sPos, tPos, mPos))
        servers.append(server)

gameNum = 0
numBreaks = 0

# Orientation will always be the positions of K, S, T and M in order at the start of the point
currOrientation = orientations[gameNum]

froResults = collections.defaultdict(lambda: collections.defaultdict(int))
toResults = collections.defaultdict(lambda: collections.defaultdict(int))

i = 0
posChange = {'5':'6', '8':'7', '1':'2', '4':'3', '2':'1', '3':'4', '6':'5', '7':'8'}
for line in sys.stdin:

    hitType, player, fromPos, toPos, stroke, result = line.strip().split(",")

    if not hitType:
        numBreaks += 1

    else:
        # We are on a new point
        if numBreaks == 1:
            # Swap positions of K and S if they are serving
            if servers[gameNum] == K or servers[gameNum] == S:
                currOrientation = (posChange[currOrientation[1]], posChange[currOrientation[0]], currOrientation[2], currOrientation[3])

            else:
                currOrientation = (currOrientation[0], currOrientation[1], posChange[currOrientation[3]], posChange[currOrientation[2]])


        # We are on a new game
        elif numBreaks == 2:
            gameNum += 1
            currOrientation = orientations[gameNum]

        numBreaks = 0

        if hitType == RET_NORMAL:
            froResults[(*currOrientation, fromPos, hitType, stroke, result)][player] += 1
            toResults[(*currOrientation, toPos, hitType, stroke, result)][player] += 1

    i += 1


orientationList = list(froResults)
orientationList.sort()
numStrokes = 0

for orientation in orientationList:
    print("for orientation:", orientation[:-4], "and position", orientation[4])
    print("We have the following pcases:")
    cases = list(froResults[orientation])
    cases.sort()
    caseSum = sum(froResults[orientation].values())
    numStrokes += caseSum
    for case in cases:
        print(f"{orientation[5]}, {orientation[6]}, {orientation[7]}, {case}, {froResults[orientation][case]}")
        print(f"The probability between members is {round(froResults[orientation][case] / caseSum, 2)}")
    print("")

destinationList = list(toResults)
destinationList.sort()
for destination in destinationList:
    print("for destination:", destination[:-4], "and position", destination[4])
    print("We have the following pcases:")
    cases = list(toResults[destination])
    cases.sort()
    caseSum = sum(toResults[destination].values())
    numStrokes += caseSum
    for case in cases:
        print(f"{destination[5]}, {destination[6]}, {destination[7]}, {case}, {toResults[destination][case]}")
        if destination[4] != '9':
            print(f"The probability between members is {round(toResults[destination][case] / caseSum, 2)}")
    print("")
print("Total games done:", gameNum)
print("Num strokes counted:", numStrokes)