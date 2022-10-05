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

states = collections.defaultdict(lambda: collections.defaultdict(int))

for line in sys.stdin:
    values = line.strip().split(",")
    hitType, player, fromPos, toPos, stroke, result = line.strip().split(",")

    if hitType:
        states[(player, hitType, fromPos)][(toPos, stroke)] += 1

ans = 0

stateList = list(states)
stateList.sort()

for state in stateList:
    print("For state:", state)
    print("We have the following pcases:")
    choices = list(states[state])
    choices.sort()
    for choice in choices:
        print(choice, states[state][choice])
        ans += states[state][choice]

print("total:", ans)
