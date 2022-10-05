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

numWinPoints = collections.defaultdict(int)

for line in sys.stdin:
    values = line.strip().split(",")
    hitType, player, fromPos, toPos, stroke, result = line.strip().split(",")

    if hitType and result == RES_WIN:
        numWinPoints[int(toPos)] += 1

ans = 0

for pos in range(1,9):
    print("For position:", pos, ", Num win points landed:", numWinPoints[pos])
    ans += numWinPoints[pos]

print("total:", ans)
