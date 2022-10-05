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
        states[(hitType, player, fromPos)][(stroke, toPos)] += 1

ans = 0

stateList = list(states)
stateList.sort()

for state in stateList:
    print("For state:", state)
    print("We have the following", sum(states[state].values()), "pcases:")

    choices = []
    if int(state[-1]) < 5:

        choices = [('Forehand', '5'), \
                   ('Backhand', '5'), \
                   ('Forehand', '6'), \
                   ('Backhand', '6'), \
                   ('Forehand', '7'), \
                   ('Backhand', '7'), \
                   ('Forehand', '8'), \
                   ('Backhand', '8'), \
                   ('Forehand', '9'), \
                   ('Backhand', '9')]

    else:
        choices = [('Forehand', '1'), \
                   ('Backhand', '1'), \
                   ('Forehand', '2'), \
                   ('Backhand', '2'), \
                   ('Forehand', '3'), \
                   ('Backhand', '3'), \
                   ('Forehand', '4'), \
                   ('Backhand', '4'), \
                   ('Forehand', '9'), \
                   ('Backhand', '9')]
    choices.sort()
    for choice in choices:
        print(choice, states[state][choice])
        ans += states[state][choice]

print("total:", ans)
