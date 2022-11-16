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

results = collections.defaultdict(lambda: collections.defaultdict(int))

i = 0
for line in sys.stdin:

    values = line.strip().split(",")
    hitType, player, fromPos, toPos, stroke, result = line.strip().split(",")

    if not hitType:
        numBreaks += 1

    else:
        # We are on a new point
        if numBreaks == 1:
            # Swap positions of K and S if they are serving
            if servers[gameNum] == K or servers[gameNum] == S:
                currOrientation = (currOrientation[1], currOrientation[0], currOrientation[2], currOrientation[3])

            else:
                currOrientation = (currOrientation[0], currOrientation[1], currOrientation[3], currOrientation[2])

        # We are on a new game
        elif numBreaks == 2:
            gameNum += 1
            currOrientation = orientations[gameNum]

        numBreaks = 0

        if hitType == RET_NORMAL:
            results[(*currOrientation, fromPos)][player] += 1

    i += 1


orientationList = list(results)
orientationList.sort()
strokesCounted = 0

for orientation in orientationList:
    print("for orientation:", orientation[:-1], "and position", orientation[-1])
    print("We have the following pcases:")
    cases = list(results[orientation])
    cases.sort()
    for case in cases:
        print(case, results[orientation][case])
        strokesCounted += results[orientation][case]

print("Total games done:", gameNum)
print("Strokes Counted:", strokesCounted )
